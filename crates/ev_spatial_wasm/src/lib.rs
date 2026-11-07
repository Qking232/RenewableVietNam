//! Vietnam EV Charging Platform High-Performance Spatial & Route Corridor WebAssembly Engine
//! Target: 22,055+ Charging Stations Across Vietnam
//! Zero-Dependency Native wasm32-unknown-unknown

const MAX_STATIONS: usize = 35_000;
const MAX_ROUTE_POINTS: usize = 4_000;
const MAX_CORRIDOR_MATCHES: usize = 1_500;
const MAX_ITIN_STOPS: usize = 32;

// Station Record: [lat, lng, original_id, kw, is_dc, is_vf]
#[derive(Clone, Copy, Default)]
struct Station {
    lat: f64,
    lng: f64,
    id: f64,
    kw: f64,
    is_dc: f64,
    is_vf: f64,
}

// Global Static Buffers (Zero-Allocation Linear Memory Sharing)
static mut STATIONS_INPUT_BUFFER: [f64; MAX_STATIONS * 6] = [0.0; MAX_STATIONS * 6];
static mut STATIONS_BUFFER: [Station; MAX_STATIONS] = [Station { lat: 0.0, lng: 0.0, id: 0.0, kw: 0.0, is_dc: 0.0, is_vf: 0.0 }; MAX_STATIONS];
static mut LOADED_STATION_COUNT: usize = 0;

// Polyline Route Input Buffer: [lat_0, lng_0, cum_dist_0, ... lat_{M-1}, lng_{M-1}, cum_dist_{M-1}]
static mut ROUTE_INPUT_BUFFER: [f64; MAX_ROUTE_POINTS * 3] = [0.0; MAX_ROUTE_POINTS * 3];
static mut ROUTE_COORDS_BUFFER: [(f64, f64); MAX_ROUTE_POINTS] = [(0.0, 0.0); MAX_ROUTE_POINTS];
static mut ROUTE_CUM_DIST_BUFFER: [f64; MAX_ROUTE_POINTS] = [0.0; MAX_ROUTE_POINTS];
static mut ROUTE_POINTS_COUNT: usize = 0;

// Corridor Matches Output Buffer: [station_id, dist_along_km, detour_km, kw, is_dc, is_vf]
static mut CORRIDOR_RESULTS_BUFFER: [f64; MAX_CORRIDOR_MATCHES * 6] = [0.0; MAX_CORRIDOR_MATCHES * 6];
static mut CORRIDOR_MATCH_COUNT: usize = 0;

// Itinerary Stops Output Buffer:
// Each stop (8 fields): [station_id, dist_along_km, arr_soc_pct, dep_soc_pct, charge_min, kwh_added, kw, detour_km]
static mut ITIN_RESULTS_BUFFER: [f64; MAX_ITIN_STOPS * 8] = [0.0; MAX_ITIN_STOPS * 8];
static mut ITIN_STOP_COUNT: usize = 0;

// Spatial Grid Index for Vietnam (Lat 8.0 - 24.0, Lng 102.0 - 110.5)
const GRID_LAT_MIN: f64 = 8.0;
const GRID_LAT_MAX: f64 = 24.0;
const GRID_LNG_MIN: f64 = 102.0;
const GRID_LNG_MAX: f64 = 111.0;
const GRID_CELL_SIZE: f64 = 0.25; // ~27 km per cell

const GRID_ROWS: usize = 64; // (24.0 - 8.0) / 0.25 = 64
const GRID_COLS: usize = 36; // (111.0 - 102.0) / 0.25 = 36
const MAX_CELL_ITEMS: usize = 400;

#[derive(Clone, Copy)]
struct GridCell {
    count: u16,
    indices: [u16; MAX_CELL_ITEMS],
}

impl Default for GridCell {
    fn default() -> Self {
        Self { count: 0, indices: [0; MAX_CELL_ITEMS] }
    }
}

static mut SPATIAL_GRID: [[GridCell; GRID_COLS]; GRID_ROWS] = [[GridCell { count: 0, indices: [0; MAX_CELL_ITEMS] }; GRID_COLS]; GRID_ROWS];

// -----------------------------------------------------------------------------
// Mathematical Geometry & Haversine Kernels
// -----------------------------------------------------------------------------

#[inline(always)]
fn deg_to_rad(deg: f64) -> f64 {
    deg * (std::f64::consts::PI / 180.0)
}

/// Exact Great-Circle Haversine Distance (Kilometers)
#[inline]
fn haversine_km(lat1: f64, lng1: f64, lat2: f64, lng2: f64) -> f64 {
    const R: f64 = 6371.0088; // Earth mean radius in km
    let d_lat = deg_to_rad(lat2 - lat1);
    let d_lng = deg_to_rad(lng2 - lng1);
    let la1 = deg_to_rad(lat1);
    let la2 = deg_to_rad(lat2);

    let h = (d_lat * 0.5).sin().powi(2) + la1.cos() * la2.cos() * (d_lng * 0.5).sin().powi(2);
    2.0 * R * h.sqrt().asin()
}

/// Fast Equirectangular Distance Squared (Kilometers^2) for Rapid Candidate Pruning
#[inline]
fn fast_dist_sq(lat1: f64, lng1: f64, lat2: f64, lng2: f64) -> f64 {
    let lat_mid = deg_to_rad((lat1 + lat2) * 0.5);
    let dx = (lng2 - lng1) * lat_mid.cos() * 111.320;
    let dy = (lat2 - lat1) * 110.574;
    dx * dx + dy * dy
}

// -----------------------------------------------------------------------------
// Exported C-ABI Functions
// -----------------------------------------------------------------------------

#[no_mangle]
pub extern "C" fn get_stations_input_buffer_ptr() -> *mut f64 {
    core::ptr::addr_of_mut!(STATIONS_INPUT_BUFFER) as *mut f64
}

#[no_mangle]
pub extern "C" fn get_route_input_buffer_ptr() -> *mut f64 {
    core::ptr::addr_of_mut!(ROUTE_INPUT_BUFFER) as *mut f64
}

#[no_mangle]
pub extern "C" fn get_corridor_results_ptr() -> *const f64 {
    core::ptr::addr_of!(CORRIDOR_RESULTS_BUFFER) as *const f64
}

#[no_mangle]
pub extern "C" fn get_itin_results_ptr() -> *const f64 {
    core::ptr::addr_of!(ITIN_RESULTS_BUFFER) as *const f64
}

/// Load and Index All Stations from the static STATIONS_INPUT_BUFFER
#[no_mangle]
pub extern "C" fn load_stations_from_input_buffer(count: u32) -> u32 {
    let n = (count as usize).min(MAX_STATIONS);
    if n == 0 {
        return 0;
    }

    unsafe {
        // Reset spatial grid
        for r in 0..GRID_ROWS {
            for c in 0..GRID_COLS {
                SPATIAL_GRID[r][c].count = 0;
            }
        }

        for i in 0..n {
            let offset = i * 6;
            let lat = STATIONS_INPUT_BUFFER[offset];
            let lng = STATIONS_INPUT_BUFFER[offset + 1];
            let id = STATIONS_INPUT_BUFFER[offset + 2];
            let kw = STATIONS_INPUT_BUFFER[offset + 3];
            let is_dc = STATIONS_INPUT_BUFFER[offset + 4];
            let is_vf = STATIONS_INPUT_BUFFER[offset + 5];

            STATIONS_BUFFER[i] = Station { lat, lng, id, kw, is_dc, is_vf };

            // Spatial Grid Binning
            if lat >= GRID_LAT_MIN && lat < GRID_LAT_MAX && lng >= GRID_LNG_MIN && lng < GRID_LNG_MAX {
                let row = (((lat - GRID_LAT_MIN) / GRID_CELL_SIZE) as usize).min(GRID_ROWS - 1);
                let col = (((lng - GRID_LNG_MIN) / GRID_CELL_SIZE) as usize).min(GRID_COLS - 1);
                let cell = &mut SPATIAL_GRID[row][col];
                if (cell.count as usize) < MAX_CELL_ITEMS {
                    cell.indices[cell.count as usize] = i as u16;
                    cell.count += 1;
                }
            }
        }
        LOADED_STATION_COUNT = n;
    }

    n as u32
}

/// High-Speed "Near Me" Spatial Query across 22,055 Stations (< 0.05 ms)
/// Returns station original_id, or -1.0 if not found
#[no_mangle]
pub extern "C" fn find_nearest_station(
    user_lat: f64,
    user_lng: f64,
    dc_only: u32,
    non_vf_only: u32,
    max_radius_km: f64,
) -> f64 {
    unsafe {
        if LOADED_STATION_COUNT == 0 {
            return -1.0;
        }

        let max_r_sq = max_radius_km * max_radius_km;
        let mut best_id = -1.0;
        let mut best_dist_sq = max_r_sq;

        // Check if within Vietnam grid
        if user_lat >= GRID_LAT_MIN && user_lat < GRID_LAT_MAX && user_lng >= GRID_LNG_MIN && user_lng < GRID_LNG_MAX {
            let center_row = (((user_lat - GRID_LAT_MIN) / GRID_CELL_SIZE) as isize).clamp(0, (GRID_ROWS - 1) as isize);
            let center_col = (((user_lng - GRID_LNG_MIN) / GRID_CELL_SIZE) as isize).clamp(0, (GRID_COLS - 1) as isize);

            let cell_radius = ((max_radius_km / 25.0).ceil() as isize).max(1);

            let r_start = (center_row - cell_radius).max(0) as usize;
            let r_end = (center_row + cell_radius).min((GRID_ROWS - 1) as isize) as usize;
            let c_start = (center_col - cell_radius).max(0) as usize;
            let c_end = (center_col + cell_radius).min((GRID_COLS - 1) as isize) as usize;

            for r in r_start..=r_end {
                for c in c_start..=c_end {
                    let cell = &SPATIAL_GRID[r][c];
                    for idx_item in 0..cell.count {
                        let station_idx = cell.indices[idx_item as usize] as usize;
                        let s = &STATIONS_BUFFER[station_idx];

                        if dc_only == 1 && s.is_dc < 0.5 {
                            continue;
                        }
                        if non_vf_only == 1 && s.is_vf > 0.5 {
                            continue;
                        }

                        let d2 = fast_dist_sq(user_lat, user_lng, s.lat, s.lng);
                        if d2 < best_dist_sq {
                            best_dist_sq = d2;
                            best_id = s.id;
                        }
                    }
                }
            }
        }

        // Global fallback if no station in neighboring grid cells
        if best_id < 0.0 {
            for i in 0..LOADED_STATION_COUNT {
                let s = &STATIONS_BUFFER[i];
                if dc_only == 1 && s.is_dc < 0.5 {
                    continue;
                }
                if non_vf_only == 1 && s.is_vf > 0.5 {
                    continue;
                }

                let d2 = fast_dist_sq(user_lat, user_lng, s.lat, s.lng);
                if d2 < best_dist_sq {
                    best_dist_sq = d2;
                    best_id = s.id;
                }
            }
        }

        best_id
    }
}

/// Load Route Coordinates from ROUTE_INPUT_BUFFER: [lat_0, lng_0, cum_dist_0, ...]
#[no_mangle]
pub extern "C" fn load_route_from_input_buffer(points_count: u32) -> u32 {
    let m = (points_count as usize).min(MAX_ROUTE_POINTS);
    if m < 2 {
        return 0;
    }

    unsafe {
        for j in 0..m {
            let off = j * 3;
            ROUTE_COORDS_BUFFER[j] = (ROUTE_INPUT_BUFFER[off], ROUTE_INPUT_BUFFER[off + 1]);
            ROUTE_CUM_DIST_BUFFER[j] = ROUTE_INPUT_BUFFER[off + 2];
        }
        ROUTE_POINTS_COUNT = m;
    }

    m as u32
}

/// Project Route Corridor Stations
/// Matches stations within max_detour_km of the route polyline in < 10 ms!
#[no_mangle]
pub extern "C" fn project_corridor_stations(
    max_detour_km: f64,
    dc_only: u32,
    non_vf_only: u32,
    min_dist_along: f64,
    max_dist_along: f64,
) -> u32 {
    unsafe {
        if LOADED_STATION_COUNT == 0 || ROUTE_POINTS_COUNT < 2 {
            CORRIDOR_MATCH_COUNT = 0;
            return 0;
        }

        let m = ROUTE_POINTS_COUNT;

        // Compute Bounding Box of Route Polyline (+ detour margin)
        let mut min_lat = f64::MAX;
        let mut max_lat = f64::MIN;
        let mut min_lng = f64::MAX;
        let mut max_lng = f64::MIN;

        for j in 0..m {
            let (lat, lng) = ROUTE_COORDS_BUFFER[j];
            if lat < min_lat { min_lat = lat; }
            if lat > max_lat { max_lat = lat; }
            if lng < min_lng { min_lng = lng; }
            if lng > max_lng { max_lng = lng; }
        }

        let deg_margin = (max_detour_km / 110.0) + 0.05;
        let bbox_min_lat = min_lat - deg_margin;
        let bbox_max_lat = max_lat + deg_margin;
        let bbox_min_lng = min_lng - deg_margin;
        let bbox_max_lng = max_lng + deg_margin;

        let max_detour_sq = max_detour_km * max_detour_km;
        let mut matches_count = 0;

        // Candidate match tuple: (dist_along_km, detour_km, station_idx)
        let mut candidates: [(f64, f64, usize); MAX_CORRIDOR_MATCHES] = [(0.0, 0.0, 0); MAX_CORRIDOR_MATCHES];

        for i in 0..LOADED_STATION_COUNT {
            let s = &STATIONS_BUFFER[i];

            // 1. Coarse Bounding Box Filter
            if s.lat < bbox_min_lat || s.lat > bbox_max_lat || s.lng < bbox_min_lng || s.lng > bbox_max_lng {
                continue;
            }

            // 2. Hardware / Brand Filter
            if dc_only == 1 && s.is_dc < 0.5 {
                continue;
            }
            if non_vf_only == 1 && s.is_vf > 0.5 {
                continue;
            }

            // 3. Orthogonal Projection onto Route Polyline Segments
            let mut min_segment_dist_sq = f64::MAX;
            let mut best_dist_along = 0.0;
            let mut best_proj_lat = s.lat;
            let mut best_proj_lng = s.lng;

            for j in 0..(m - 1) {
                let (p1_lat, p1_lng) = ROUTE_COORDS_BUFFER[j];
                let (p2_lat, p2_lng) = ROUTE_COORDS_BUFFER[j + 1];

                // Fast BBox check for this single segment (+ max_detour_km)
                let seg_min_lat = p1_lat.min(p2_lat) - deg_margin;
                let seg_max_lat = p1_lat.max(p2_lat) + deg_margin;
                let seg_min_lng = p1_lng.min(p2_lng) - deg_margin;
                let seg_max_lng = p1_lng.max(p2_lng) + deg_margin;

                if s.lat < seg_min_lat || s.lat > seg_max_lat || s.lng < seg_min_lng || s.lng > seg_max_lng {
                    continue;
                }

                let dx = p2_lng - p1_lng;
                let dy = p2_lat - p1_lat;
                let len_sq = dx * dx + dy * dy;

                let t = if len_sq > 1e-12 {
                    (((s.lng - p1_lng) * dx + (s.lat - p1_lat) * dy) / len_sq).clamp(0.0, 1.0)
                } else {
                    0.0
                };

                let proj_lat = p1_lat + t * dy;
                let proj_lng = p1_lng + t * dx;

                let d2 = fast_dist_sq(s.lat, s.lng, proj_lat, proj_lng);
                if d2 < min_segment_dist_sq {
                    min_segment_dist_sq = d2;
                    let seg_km = haversine_km(p1_lat, p1_lng, p2_lat, p2_lng);
                    best_dist_along = ROUTE_CUM_DIST_BUFFER[j] + t * seg_km;
                    best_proj_lat = proj_lat;
                    best_proj_lng = proj_lng;
                }
            }

            // 4. Exact Haversine Detour Verification
            if min_segment_dist_sq <= (max_detour_sq * 1.2) {
                let exact_detour_km = haversine_km(s.lat, s.lng, best_proj_lat, best_proj_lng);
                if exact_detour_km <= max_detour_km && best_dist_along >= min_dist_along && best_dist_along <= max_dist_along {
                    if matches_count < MAX_CORRIDOR_MATCHES {
                        candidates[matches_count] = (best_dist_along, exact_detour_km, i);
                        matches_count += 1;
                    }
                }
            }
        }

        // Sort candidates by dist_along_km ascending
        candidates[0..matches_count].sort_by(|a, b| a.0.partial_cmp(&b.0).unwrap_or(std::cmp::Ordering::Equal));

        // Populate CORRIDOR_RESULTS_BUFFER: [station_id, dist_along_km, detour_km, kw, is_dc, is_vf]
        for k in 0..matches_count {
            let (dist_along, detour, s_idx) = candidates[k];
            let s = &STATIONS_BUFFER[s_idx];
            let offset = k * 6;
            CORRIDOR_RESULTS_BUFFER[offset] = s.id;
            CORRIDOR_RESULTS_BUFFER[offset + 1] = dist_along;
            CORRIDOR_RESULTS_BUFFER[offset + 2] = detour;
            CORRIDOR_RESULTS_BUFFER[offset + 3] = s.kw;
            CORRIDOR_RESULTS_BUFFER[offset + 4] = s.is_dc;
            CORRIDOR_RESULTS_BUFFER[offset + 5] = s.is_vf;
        }

        CORRIDOR_MATCH_COUNT = matches_count;
        matches_count as u32
    }
}

/// Simulate Non-Linear Battery State-of-Charge (SoC) & Optimal Charging Stops
/// Returns number of recommended stops (< 1 ms execution)
#[no_mangle]
pub extern "C" fn simulate_ev_stops(
    total_dist_km: f64,
    battery_kwh: f64,
    max_range_km: f64,
    start_soc_pct: f64,
    min_soc_pct: f64,
    target_soc_pct: f64,
    car_max_kw: f64,
) -> u32 {
    unsafe {
        if CORRIDOR_MATCH_COUNT == 0 || total_dist_km <= 0.0 || max_range_km <= 0.0 {
            ITIN_STOP_COUNT = 0;
            return 0;
        }

        let s_soc = (start_soc_pct / 100.0).clamp(0.10, 1.0);
        let m_soc = (min_soc_pct / 100.0).clamp(0.05, 0.40);
        let t_soc = (target_soc_pct / 100.0).clamp(0.50, 0.95);

        let mut stops_count = 0;
        let mut curr_km = 0.0;
        let mut curr_soc = s_soc;

        let max_leg_km = max_range_km * (curr_soc - m_soc);
        if total_dist_km <= max_leg_km {
            ITIN_STOP_COUNT = 0;
            return 0;
        }

        let mut iter = 0;
        while (total_dist_km - curr_km) > (max_range_km * (curr_soc - m_soc)) && iter < 12 {
            iter += 1;
            let km_can_go = max_range_km * (curr_soc - m_soc);
            let _min_win = curr_km + (km_can_go * 0.50).max(15.0);
            let max_win = curr_km + km_can_go * 0.95;

            // Find best candidate in window
            let mut best_match_idx = usize::MAX;
            let mut best_score = f64::MIN;

            for k in 0..CORRIDOR_MATCH_COUNT {
                let offset = k * 6;
                let dist_along = CORRIDOR_RESULTS_BUFFER[offset + 1];
                let detour = CORRIDOR_RESULTS_BUFFER[offset + 2];
                let kw = CORRIDOR_RESULTS_BUFFER[offset + 3];
                let is_dc = CORRIDOR_RESULTS_BUFFER[offset + 4];

                if dist_along > (curr_km + 10.0) && dist_along <= max_win {
                    let mut score = 0.0;
                    if kw >= 150.0 { score += 100.0; }
                    else if kw >= 120.0 { score += 80.0; }
                    else if kw >= 60.0 { score += 60.0; }
                    else if kw >= 30.0 { score += 40.0; }
                    else { score += 10.0; }

                    if is_dc < 0.5 { score -= 75.0; }
                    score -= detour * 8.0;

                    let target_km = curr_km + km_can_go * 0.85;
                    let dist_diff = (dist_along - target_km).abs();
                    score -= dist_diff * 0.8;

                    if score > best_score {
                        best_score = score;
                        best_match_idx = k;
                    }
                }
            }

            // Fallback: widen backwards
            if best_match_idx == usize::MAX {
                for k in 0..CORRIDOR_MATCH_COUNT {
                    let offset = k * 6;
                    let dist_along = CORRIDOR_RESULTS_BUFFER[offset + 1];
                    let kw = CORRIDOR_RESULTS_BUFFER[offset + 3];

                    if dist_along > (curr_km + 5.0) && dist_along <= (curr_km + km_can_go * 0.99) {
                        let score = kw - (dist_along - curr_km) * 0.1;
                        if score > best_score {
                            best_score = score;
                            best_match_idx = k;
                        }
                    }
                }
            }

            if best_match_idx == usize::MAX {
                break;
            }

            let offset = best_match_idx * 6;
            let best_id = CORRIDOR_RESULTS_BUFFER[offset];
            let best_dist = CORRIDOR_RESULTS_BUFFER[offset + 1];
            let best_detour = CORRIDOR_RESULTS_BUFFER[offset + 2];
            let best_kw = CORRIDOR_RESULTS_BUFFER[offset + 3];

            let leg_dist = best_dist - curr_km;
            let arr_soc = (curr_soc - (leg_dist / max_range_km)).max(0.05);
            let dep_soc = t_soc;

            // Non-linear CC/CV Charging Time Calculation
            let eff_kw = best_kw.min(car_max_kw).max(7.0);
            let kwh_needed = battery_kwh * (dep_soc - arr_soc);

            // Phase 1 (up to 80% SoC): full constant power
            let t_cc_min = if arr_soc < 0.80 {
                let frac = (0.80 - arr_soc).min(dep_soc - arr_soc);
                (battery_kwh * frac / eff_kw) * 60.0
            } else {
                0.0
            };

            // Phase 2 (above 80% SoC): constant voltage taper (average 60% power)
            let t_cv_min = if dep_soc > 0.80 {
                let start_p2 = arr_soc.max(0.80);
                let frac = dep_soc - start_p2;
                (battery_kwh * frac / (eff_kw * 0.60)) * 60.0
            } else {
                0.0
            };

            let charge_min = (t_cc_min + t_cv_min).ceil();

            if stops_count < MAX_ITIN_STOPS {
                let out_off = stops_count * 8;
                ITIN_RESULTS_BUFFER[out_off] = best_id;
                ITIN_RESULTS_BUFFER[out_off + 1] = best_dist;
                ITIN_RESULTS_BUFFER[out_off + 2] = arr_soc * 100.0;
                ITIN_RESULTS_BUFFER[out_off + 3] = dep_soc * 100.0;
                ITIN_RESULTS_BUFFER[out_off + 4] = charge_min;
                ITIN_RESULTS_BUFFER[out_off + 5] = kwh_needed;
                ITIN_RESULTS_BUFFER[out_off + 6] = best_kw;
                ITIN_RESULTS_BUFFER[out_off + 7] = best_detour;

                stops_count += 1;
            }

            curr_km = best_dist;
            curr_soc = dep_soc;
        }

        ITIN_STOP_COUNT = stops_count;
        stops_count as u32
    }
}
