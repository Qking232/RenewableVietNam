//! Vietnam National Energy Grid High-Performance WebAssembly Analytical Engine
//! Target: 960+ Generation Plants, 1,915 Grid Substations & 500kV/220kV Transmission Interconnections
//! Zero-Dependency Native wasm32-unknown-unknown

#![allow(static_mut_refs)]
#![allow(dead_code)]

const MAX_SUBSTATIONS: usize = 3_000;
const MAX_PLANTS: usize = 3_000;

// -----------------------------------------------------------------------------
// Data Structures
// -----------------------------------------------------------------------------

#[derive(Clone, Copy, Default)]
struct Substation {
    lat: f64,
    lng: f64,
    orig_idx: f64,
    max_v: f64,
    tx_mva: f64,
}

#[derive(Clone, Copy, Default)]
struct Plant {
    lat: f64,
    lng: f64,
    orig_idx: f64,
    fuel_code: f64, // 1: Solar, 2: Wind, 3: Hydro, 4: Gas/LNG, 5: Biomass, 6: Other
    capacity_mw: f64,
    province_hash: f64,
}

// -----------------------------------------------------------------------------
// Spatial Grid Index for Vietnam Grid Substations
// Lat: 8.0 to 24.0 (16 deg) / Lng: 102.0 to 111.0 (9 deg)
// Cell Size: 0.25 deg (~27 km)
// Rows: 64, Cols: 36
// -----------------------------------------------------------------------------
const GRID_LAT_MIN: f64 = 8.0;
const GRID_LAT_MAX: f64 = 24.0;
const GRID_LNG_MIN: f64 = 102.0;
const GRID_LNG_MAX: f64 = 111.0;
const GRID_CELL_SIZE: f64 = 0.25;

const GRID_ROWS: usize = 64;
const GRID_COLS: usize = 36;
const MAX_CELL_ITEMS: usize = 128;

#[derive(Clone, Copy)]
struct SpatialCell {
    indices: [u16; MAX_CELL_ITEMS],
    count: u16,
}

impl Default for SpatialCell {
    fn default() -> Self {
        Self {
            indices: [0; MAX_CELL_ITEMS],
            count: 0,
        }
    }
}

// -----------------------------------------------------------------------------
// Global Static Memory Buffers (Zero-Allocation Linear Memory Sharing)
// -----------------------------------------------------------------------------
static mut SUBSTATIONS_INPUT_BUFFER: [f64; MAX_SUBSTATIONS * 5] = [0.0; MAX_SUBSTATIONS * 5];
static mut SUBSTATIONS_BUFFER: [Substation; MAX_SUBSTATIONS] = [Substation {
    lat: 0.0,
    lng: 0.0,
    orig_idx: 0.0,
    max_v: 0.0,
    tx_mva: 0.0,
}; MAX_SUBSTATIONS];
static mut LOADED_SUB_COUNT: usize = 0;

static mut PLANTS_INPUT_BUFFER: [f64; MAX_PLANTS * 6] = [0.0; MAX_PLANTS * 6];
static mut PLANTS_BUFFER: [Plant; MAX_PLANTS] = [Plant {
    lat: 0.0,
    lng: 0.0,
    orig_idx: 0.0,
    fuel_code: 0.0,
    capacity_mw: 0.0,
    province_hash: 0.0,
}; MAX_PLANTS];
static mut LOADED_PLANT_COUNT: usize = 0;

static mut SUB_GRID: [[SpatialCell; GRID_COLS]; GRID_ROWS] = [[SpatialCell {
    indices: [0; MAX_CELL_ITEMS],
    count: 0,
}; GRID_COLS]; GRID_ROWS];

// Result Buffers
// Nearest Sub: [sub_orig_idx, dist_km, max_v, tx_mva, line_loss_mw, capex_usd, headroom_pct, status_code]
static mut NEAREST_SUB_RESULTS: [f64; 8] = [0.0; 8];

// Filter Matches: Array of original plant indices that passed filter
static mut FILTER_MATCHES_BUFFER: [f64; MAX_PLANTS] = [0.0; MAX_PLANTS];

// Aggregation: [matched_count, total_mw, solar_mw, wind_mw, hydro_mw, gas_mw, biomass_mw, avg_mw]
static mut AGGREGATION_RESULTS: [f64; 8] = [0.0; 8];

// -----------------------------------------------------------------------------
// Geodesic Mathematics
// -----------------------------------------------------------------------------
const PI: f64 = core::f64::consts::PI;
const EARTH_RADIUS_KM: f64 = 6371.0088;

#[inline(always)]
fn to_radians(deg: f64) -> f64 {
    deg * (PI / 180.0)
}

fn haversine_km(lat1: f64, lng1: f64, lat2: f64, lng2: f64) -> f64 {
    let d_lat = to_radians(lat2 - lat1);
    let d_lng = to_radians(lng2 - lng1);
    let r_lat1 = to_radians(lat1);
    let r_lat2 = to_radians(lat2);

    let sin_dlat_2 = (d_lat * 0.5).sin();
    let sin_dlng_2 = (d_lng * 0.5).sin();

    let a = sin_dlat_2 * sin_dlat_2 + r_lat1.cos() * r_lat2.cos() * sin_dlng_2 * sin_dlng_2;
    let a_clamped = if a > 1.0 { 1.0 } else if a < 0.0 { 0.0 } else { a };
    let c = 2.0 * a_clamped.sqrt().atan2((1.0 - a_clamped).sqrt());
    EARTH_RADIUS_KM * c
}

// -----------------------------------------------------------------------------
// Spatial Grid Coordinate Helper
// -----------------------------------------------------------------------------
#[inline(always)]
fn get_grid_coords(lat: f64, lng: f64) -> Option<(usize, usize)> {
    if lat < GRID_LAT_MIN || lat >= GRID_LAT_MAX || lng < GRID_LNG_MIN || lng >= GRID_LNG_MAX {
        return None;
    }
    let row = ((lat - GRID_LAT_MIN) / GRID_CELL_SIZE) as usize;
    let col = ((lng - GRID_LNG_MIN) / GRID_CELL_SIZE) as usize;
    if row < GRID_ROWS && col < GRID_COLS {
        Some((row, col))
    } else {
        None
    }
}

// -----------------------------------------------------------------------------
// Exported Substation Ingestion & Spatial Indexing
// -----------------------------------------------------------------------------
#[no_mangle]
pub unsafe extern "C" fn get_substations_buffer_ptr() -> *mut f64 {
    SUBSTATIONS_INPUT_BUFFER.as_mut_ptr()
}

#[no_mangle]
pub unsafe extern "C" fn load_substations(count: usize) -> usize {
    let actual_count = if count > MAX_SUBSTATIONS { MAX_SUBSTATIONS } else { count };
    LOADED_SUB_COUNT = actual_count;

    // Reset Spatial Grid
    for r in 0..GRID_ROWS {
        for c in 0..GRID_COLS {
            SUB_GRID[r][c].count = 0;
        }
    }

    for i in 0..actual_count {
        let base = i * 5;
        let lat = SUBSTATIONS_INPUT_BUFFER[base];
        let lng = SUBSTATIONS_INPUT_BUFFER[base + 1];
        let orig_idx = SUBSTATIONS_INPUT_BUFFER[base + 2];
        let max_v = SUBSTATIONS_INPUT_BUFFER[base + 3];
        let tx_mva = SUBSTATIONS_INPUT_BUFFER[base + 4];

        SUBSTATIONS_BUFFER[i] = Substation {
            lat,
            lng,
            orig_idx,
            max_v,
            tx_mva,
        };

        if let Some((row, col)) = get_grid_coords(lat, lng) {
            let cell = &mut SUB_GRID[row][col];
            if (cell.count as usize) < MAX_CELL_ITEMS {
                cell.indices[cell.count as usize] = i as u16;
                cell.count += 1;
            }
        }
    }

    LOADED_SUB_COUNT
}

// -----------------------------------------------------------------------------
// Exported Plant Ingestion
// -----------------------------------------------------------------------------
#[no_mangle]
pub unsafe extern "C" fn get_plants_buffer_ptr() -> *mut f64 {
    PLANTS_INPUT_BUFFER.as_mut_ptr()
}

#[no_mangle]
pub unsafe extern "C" fn load_plants(count: usize) -> usize {
    let actual_count = if count > MAX_PLANTS { MAX_PLANTS } else { count };
    LOADED_PLANT_COUNT = actual_count;

    for i in 0..actual_count {
        let base = i * 6;
        PLANTS_BUFFER[i] = Plant {
            lat: PLANTS_INPUT_BUFFER[base],
            lng: PLANTS_INPUT_BUFFER[base + 1],
            orig_idx: PLANTS_INPUT_BUFFER[base + 2],
            fuel_code: PLANTS_INPUT_BUFFER[base + 3],
            capacity_mw: PLANTS_INPUT_BUFFER[base + 4],
            province_hash: PLANTS_INPUT_BUFFER[base + 5],
        };
    }

    LOADED_PLANT_COUNT
}

// -----------------------------------------------------------------------------
// High-Speed Spatial Nearest Substation & Interconnection Feasibility Solver
// -----------------------------------------------------------------------------
#[no_mangle]
pub unsafe extern "C" fn find_nearest_substation(
    lat: f64,
    lng: f64,
    min_kv: f64,
    plant_mw: f64,
) -> usize {
    if LOADED_SUB_COUNT == 0 || lat == 0.0 || lng == 0.0 {
        NEAREST_SUB_RESULTS[0] = -1.0;
        return 0;
    }

    let mut min_dist = f64::MAX;
    let mut best_sub_idx: Option<usize> = None;

    // Fast Path: Try spatial grid search within expanding concentric ring
    if let Some((origin_row, origin_col)) = get_grid_coords(lat, lng) {
        let max_radius: isize = 12; // Search up to ~300km radius
        for r_offset in 0..=max_radius {
            let mut checked_in_ring = false;
            let r_min = (origin_row as isize - r_offset).max(0) as usize;
            let r_max = (origin_row as isize + r_offset).min(GRID_ROWS as isize - 1) as usize;
            let c_min = (origin_col as isize - r_offset).max(0) as usize;
            let c_max = (origin_col as isize + r_offset).min(GRID_COLS as isize - 1) as usize;

            for r in r_min..=r_max {
                for c in c_min..=c_max {
                    // Only examine perimeter cells if r_offset > 0
                    if r_offset > 0
                        && r != r_min
                        && r != r_max
                        && c != c_min
                        && c != c_max
                    {
                        continue;
                    }

                    let cell = &SUB_GRID[r][c];
                    let count = cell.count as usize;
                    for k in 0..count {
                        checked_in_ring = true;
                        let sub_idx = cell.indices[k] as usize;
                        let sub = &SUBSTATIONS_BUFFER[sub_idx];

                        if sub.max_v < min_kv {
                            continue;
                        }

                        let dist = haversine_km(lat, lng, sub.lat, sub.lng);
                        if dist < min_dist {
                            min_dist = dist;
                            best_sub_idx = Some(sub_idx);
                        }
                    }
                }
            }

            // Early exit: if candidate found and ring radius exceeds candidate distance, terminate search
            if checked_in_ring && best_sub_idx.is_some() {
                let cell_radius_km = (r_offset as f64) * GRID_CELL_SIZE * 111.0;
                if cell_radius_km > min_dist {
                    break;
                }
            }
        }
    }

    // Fallback: If no candidate found in spatial grid, exhaustive scan
    if best_sub_idx.is_none() {
        for i in 0..LOADED_SUB_COUNT {
            let sub = &SUBSTATIONS_BUFFER[i];
            if sub.lat == 0.0 || sub.lng == 0.0 || sub.max_v < min_kv {
                continue;
            }
            let dist = haversine_km(lat, lng, sub.lat, sub.lng);
            if dist < min_dist {
                min_dist = dist;
                best_sub_idx = Some(i);
            }
        }
    }

    if let Some(idx) = best_sub_idx {
        let sub = &SUBSTATIONS_BUFFER[idx];
        let dist_km = min_dist;

        // Engineering Feasibility Calculations:
        // Transmission line loss: ~0.035% per km for 220kV, ~0.065% for 110kV, ~0.015% for 500kV
        let loss_coeff = if sub.max_v >= 500.0 {
            0.00015
        } else if sub.max_v >= 220.0 {
            0.00035
        } else {
            0.00065
        };
        let line_loss_mw = plant_mw * (loss_coeff * dist_km).min(0.12);

        // Radial Interconnection Line Capex:
        // 500kV: $160,000/km; 220kV: $75,000/km; 110kV: $38,000/km
        let capex_per_km = if sub.max_v >= 500.0 {
            160_000.0
        } else if sub.max_v >= 220.0 {
            75_000.0
        } else {
            38_000.0
        };
        let capex_usd = dist_km * capex_per_km;

        // Headroom: percentage of plant capacity relative to transformer rating
        let headroom_pct = if sub.tx_mva > 0.0 {
            (plant_mw / sub.tx_mva) * 100.0
        } else {
            0.0
        };

        NEAREST_SUB_RESULTS[0] = sub.orig_idx;
        NEAREST_SUB_RESULTS[1] = (dist_km * 10.0).round() / 10.0;
        NEAREST_SUB_RESULTS[2] = sub.max_v;
        NEAREST_SUB_RESULTS[3] = sub.tx_mva;
        NEAREST_SUB_RESULTS[4] = (line_loss_mw * 100.0).round() / 100.0;
        NEAREST_SUB_RESULTS[5] = capex_usd.round();
        NEAREST_SUB_RESULTS[6] = (headroom_pct * 10.0).round() / 10.0;
        NEAREST_SUB_RESULTS[7] = 1.0; // Success code

        1
    } else {
        NEAREST_SUB_RESULTS[0] = -1.0;
        NEAREST_SUB_RESULTS[7] = 0.0;
        0
    }
}

#[no_mangle]
pub unsafe extern "C" fn get_nearest_sub_results_ptr() -> *const f64 {
    NEAREST_SUB_RESULTS.as_ptr()
}

// -----------------------------------------------------------------------------
// Plant Filtering & Instant Vector Statistical Aggregation
// -----------------------------------------------------------------------------
#[no_mangle]
pub unsafe extern "C" fn filter_and_aggregate_plants(
    fuel_filter: u32,
    min_mw: f64,
    max_mw: f64,
) -> usize {
    let mut matched_count: usize = 0;
    let mut total_mw: f64 = 0.0;
    let mut solar_mw: f64 = 0.0;
    let mut wind_mw: f64 = 0.0;
    let mut hydro_mw: f64 = 0.0;
    let mut gas_mw: f64 = 0.0;
    let mut biomass_mw: f64 = 0.0;

    for i in 0..LOADED_PLANT_COUNT {
        let plant = &PLANTS_BUFFER[i];

        // Fuel filter: 0 = ALL, 1 = Solar, 2 = Wind, 3 = Hydro, 4 = Gas/LNG, 5 = Biomass
        if fuel_filter != 0 && (plant.fuel_code as u32) != fuel_filter {
            continue;
        }

        // Capacity bounds check
        if min_mw > 0.0 && plant.capacity_mw < min_mw {
            continue;
        }
        if max_mw > 0.0 && plant.capacity_mw > max_mw {
            continue;
        }

        // Record matched index
        if matched_count < MAX_PLANTS {
            FILTER_MATCHES_BUFFER[matched_count] = plant.orig_idx;
            matched_count += 1;
        }

        // Aggregate statistics
        total_mw += plant.capacity_mw;
        match plant.fuel_code as u32 {
            1 => solar_mw += plant.capacity_mw,
            2 => wind_mw += plant.capacity_mw,
            3 => hydro_mw += plant.capacity_mw,
            4 => gas_mw += plant.capacity_mw,
            5 => biomass_mw += plant.capacity_mw,
            _ => {}
        }
    }

    let avg_mw = if matched_count > 0 {
        total_mw / (matched_count as f64)
    } else {
        0.0
    };

    AGGREGATION_RESULTS[0] = matched_count as f64;
    AGGREGATION_RESULTS[1] = total_mw.round();
    AGGREGATION_RESULTS[2] = solar_mw.round();
    AGGREGATION_RESULTS[3] = wind_mw.round();
    AGGREGATION_RESULTS[4] = hydro_mw.round();
    AGGREGATION_RESULTS[5] = gas_mw.round();
    AGGREGATION_RESULTS[6] = biomass_mw.round();
    AGGREGATION_RESULTS[7] = (avg_mw * 10.0).round() / 10.0;

    matched_count
}

#[no_mangle]
pub unsafe extern "C" fn get_filter_matches_ptr() -> *const f64 {
    FILTER_MATCHES_BUFFER.as_ptr()
}

#[no_mangle]
pub unsafe extern "C" fn get_aggregation_results_ptr() -> *const f64 {
    AGGREGATION_RESULTS.as_ptr()
}

// -----------------------------------------------------------------------------
// High-Frequency WASM Execution Benchmark
// -----------------------------------------------------------------------------
#[no_mangle]
pub unsafe extern "C" fn run_wasm_benchmark(iterations: usize) -> f64 {
    let mut accumulator: f64 = 0.0;
    let actual_iter = if iterations > 50_000 { 50_000 } else { iterations };

    for i in 0..actual_iter {
        let lat = 10.0 + ((i % 140) as f64) * 0.1;
        let lng = 104.0 + ((i % 70) as f64) * 0.1;
        let found = find_nearest_substation(lat, lng, 110.0, 50.0);
        accumulator += (found as f64) + NEAREST_SUB_RESULTS[1];
    }

    accumulator
}
