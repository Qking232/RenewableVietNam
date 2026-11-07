//! Renewable Vietnam Apex Homepage High-Performance WebAssembly Analytical Engine
//! Target: Decree 80 DPPA Economic Simulator, 12-Pillars Vector Aggregator & PDP8 Trajectory Math
//! Zero-Dependency Native wasm32-unknown-unknown

// -----------------------------------------------------------------------------
// Global Static Memory Buffers (Zero-Allocation Linear Memory Sharing)
// -----------------------------------------------------------------------------
static mut DPPA_RESULTS_BUFFER: [f64; 16] = [0.0; 16];
static mut PILLARS_RESULTS_BUFFER: [f64; 8] = [0.0; 8];
static mut TRAJECTORY_RESULTS_BUFFER: [f64; 8] = [0.0; 8];

// -----------------------------------------------------------------------------
// 12 Strategic Pillars Static Vector Data
// -----------------------------------------------------------------------------
#[derive(Clone, Copy)]
struct Pillar {
    #[allow(dead_code)]
    id: usize,
    category: i32, // 1: GENERATION, 2: GRID, 3: MARKET
    capex_billion: f64,
    target_mw: f64,
    cod_mw: f64,
}

const PILLARS_DATA: [Pillar; 12] = [
    // 01: Offshore Wind
    Pillar { id: 1, category: 1, capex_billion: 18.5, target_mw: 6000.0, cod_mw: 300.0 },
    // 02: Onshore & Nearshore Wind
    Pillar { id: 2, category: 1, capex_billion: 26.2, target_mw: 21880.0, cod_mw: 4798.0 },
    // 03: Solar PV & Rooftop RTS
    Pillar { id: 3, category: 1, capex_billion: 14.1, target_mw: 16500.0, cod_mw: 16500.0 },
    // 04: Flexible Hydro & Storage
    Pillar { id: 4, category: 1, capex_billion: 11.8, target_mw: 32046.0, cod_mw: 29346.0 },
    // 05: Domestic Gas & LNG
    Pillar { id: 5, category: 1, capex_billion: 31.4, target_mw: 37330.0, cod_mw: 9330.0 },
    // 06: Biomass & Waste-to-Energy
    Pillar { id: 6, category: 1, capex_billion: 3.6, target_mw: 2270.0, cod_mw: 635.0 },
    // 07: 500kV Supergrid Spine
    Pillar { id: 7, category: 2, capex_billion: 14.9, target_mw: 5000.0, cod_mw: 5000.0 },
    // 08: ASEAN Grid Interties
    Pillar { id: 8, category: 2, capex_billion: 2.8, target_mw: 2500.0, cod_mw: 1500.0 },
    // 09: Smart Distribution & DERMS
    Pillar { id: 9, category: 2, capex_billion: 4.3, target_mw: 1500.0, cod_mw: 600.0 },
    // 10: Decree 80 DPPA Mechanism
    Pillar { id: 10, category: 3, capex_billion: 3.2, target_mw: 1000.0, cod_mw: 200.0 },
    // 11: Competitive Wholesale (VWEM/VREM)
    Pillar { id: 11, category: 3, capex_billion: 7.7, target_mw: 0.0, cod_mw: 0.0 },
    // 12: Green Hydrogen & Power-to-X
    Pillar { id: 12, category: 3, capex_billion: 6.2, target_mw: 0.0, cod_mw: 0.0 },
];

// -----------------------------------------------------------------------------
// Exported C-ABI Engine Kernels
// -----------------------------------------------------------------------------

/// Pointers to Output Buffers
#[no_mangle]
pub extern "C" fn get_dppa_results_ptr() -> *const f64 {
    core::ptr::addr_of!(DPPA_RESULTS_BUFFER) as *const f64
}

#[no_mangle]
pub extern "C" fn get_pillars_results_ptr() -> *const f64 {
    core::ptr::addr_of!(PILLARS_RESULTS_BUFFER) as *const f64
}

#[no_mangle]
pub extern "C" fn get_trajectory_results_ptr() -> *const f64 {
    core::ptr::addr_of!(TRAJECTORY_RESULTS_BUFFER) as *const f64
}

/// Decree 80 DPPA Economic & Technical Generation Kernel
/// - capacity_mw: Rated generation capacity (e.g. 5 to 500 MW)
/// - capacity_factor_pct: Capacity factor % (e.g. 15% to 45%)
/// - retail_tariff_usd_kwh: Baseline grid retail tariff ($0.082 default)
/// - ppa_tariff_usd_kwh: Negotiated DPPA strike tariff ($0.065 default)
/// - wheeling_charge_usd_kwh: EVN wheeling + transmission fee ($0.012 default)
/// - is_direct: 1.0 = Direct Private Wire, 0.0 = Grid Wheeling
#[no_mangle]
pub extern "C" fn calculate_dppa_economics(
    capacity_mw: f64,
    capacity_factor_pct: f64,
    retail_tariff_usd_kwh: f64,
    ppa_tariff_usd_kwh: f64,
    wheeling_charge_usd_kwh: f64,
    is_direct: f64,
) -> i32 {
    unsafe {
        // Transmission loss factor: 0.0% for direct wire, 4.2% for national grid wheeling
        let loss_factor = if is_direct >= 0.5 { 0.0 } else { 0.042 };
        let hours_per_year = 8760.0;
        let cf = capacity_factor_pct / 100.0;

        let gross_annual_mwh = capacity_mw * hours_per_year * cf;
        let net_annual_mwh = gross_annual_mwh * (1.0 - loss_factor);

        // Emission factor for Vietnam grid: 0.7221 tCO2e / MWh
        let co2_tonnes_abated = net_annual_mwh * 0.7221;

        // Corporate Tariff Differential ($/MWh)
        // Retail: retail_tariff_usd_kwh * 1000
        // Effective DPPA: (ppa_tariff + wheeling) * 1000
        let retail_rate_mwh = retail_tariff_usd_kwh * 1000.0;
        let dppa_effective_rate_mwh = if is_direct >= 0.5 {
            ppa_tariff_usd_kwh * 1000.0
        } else {
            (ppa_tariff_usd_kwh + wheeling_charge_usd_kwh) * 1000.0
        };

        let unit_savings_mwh = (retail_rate_mwh - dppa_effective_rate_mwh).max(0.0);
        let annual_savings_usd = net_annual_mwh * unit_savings_mwh;
        let annual_savings_millions = annual_savings_usd / 1_000_000.0;

        // Estimated Capex ($650k / MW for ground/rooftop solar, $1.4M / MW for wind)
        let capex_per_mw = if capacity_factor_pct > 25.0 { 1_350_000.0 } else { 680_000.0 };
        let total_capex_usd = capacity_mw * capex_per_mw;

        // Simple Payback Period (Years)
        let simple_payback = if annual_savings_usd > 0.0 {
            total_capex_usd / annual_savings_usd
        } else {
            99.0
        };

        // 15-Year Net Present Value (NPV) at 8.5% WACC
        let wacc: f64 = 0.085;
        let mut npv_usd: f64 = -total_capex_usd;
        let opex_per_year: f64 = total_capex_usd * 0.018; // 1.8% annual O&M
        let net_annual_cash_flow: f64 = annual_savings_usd - opex_per_year;

        for t in 1..=15 {
            let discount_factor = (1.0_f64 + wacc).powi(t);
            npv_usd += net_annual_cash_flow / discount_factor;
        }
        let npv_millions = npv_usd / 1_000_000.0;

        // Levelized Cost of Electricity (LCOE in $/kWh)
        let total_discounted_mwh: f64 = (1..=15)
            .map(|t| (net_annual_mwh * (1.0_f64 - 0.005_f64.powi(t))) / (1.0_f64 + wacc).powi(t))
            .sum();
        let total_discounted_cost: f64 = total_capex_usd + (1..=15).map(|t| opex_per_year / (1.0_f64 + wacc).powi(t)).sum::<f64>();
        let lcoe_usd_kwh = (total_discounted_cost / (total_discounted_mwh * 1000.0)).max(0.035);

        DPPA_RESULTS_BUFFER[0] = net_annual_mwh;
        DPPA_RESULTS_BUFFER[1] = co2_tonnes_abated;
        DPPA_RESULTS_BUFFER[2] = annual_savings_millions;
        DPPA_RESULTS_BUFFER[3] = total_capex_usd / 1_000_000.0;
        DPPA_RESULTS_BUFFER[4] = simple_payback;
        DPPA_RESULTS_BUFFER[5] = npv_millions;
        DPPA_RESULTS_BUFFER[6] = lcoe_usd_kwh;
        DPPA_RESULTS_BUFFER[7] = gross_annual_mwh;
    }
    1
}

/// 12 Strategic Pillars Vector Filter & Aggregator Kernel
/// - category_filter: 0 = ALL, 1 = GENERATION, 2 = GRID, 3 = MARKET
#[no_mangle]
pub extern "C" fn filter_and_aggregate_pillars(category_filter: i32) -> i32 {
    unsafe {
        let mut count: f64 = 0.0;
        let mut total_capex: f64 = 0.0;
        let mut total_target_mw: f64 = 0.0;
        let mut total_cod_mw: f64 = 0.0;

        for pillar in PILLARS_DATA.iter() {
            if category_filter == 0 || pillar.category == category_filter {
                count += 1.0;
                total_capex += pillar.capex_billion;
                total_target_mw += pillar.target_mw;
                total_cod_mw += pillar.cod_mw;
            }
        }

        let cod_pct = if total_target_mw > 0.0 {
            (total_cod_mw / total_target_mw) * 100.0
        } else {
            100.0
        };

        PILLARS_RESULTS_BUFFER[0] = count;
        PILLARS_RESULTS_BUFFER[1] = total_capex; // in Billion USD
        PILLARS_RESULTS_BUFFER[2] = total_target_mw;
        PILLARS_RESULTS_BUFFER[3] = total_cod_mw;
        PILLARS_RESULTS_BUFFER[4] = cod_pct;
    }
    1
}

/// Decarbonization Trajectory (2025-2050) Interpolator Kernel
/// Computes capacity, renewable share, and carbon intensity for given year
#[no_mangle]
pub extern "C" fn project_pdp8_trajectory(year: f64) -> i32 {
    unsafe {
        let y = year.clamp(2025.0, 2050.0);
        let t = (y - 2025.0) / 25.0; // Normalized 0.0 to 1.0

        // National Generation Capacity: 90 GW (2025) -> 150 GW (2030) -> 500 GW (2050)
        let total_capacity_gw = if y <= 2030.0 {
            let t_sub = (y - 2025.0) / 5.0;
            90.0 + (150.0 - 90.0) * t_sub
        } else {
            let t_sub = (y - 2030.0) / 20.0;
            150.0 + (500.0 - 150.0) * t_sub.powf(1.15)
        };

        // Renewable Share (%): 32% (2025) -> 45% (2030) -> 85% (2050)
        let renewable_share_pct = if y <= 2030.0 {
            let t_sub = (y - 2025.0) / 5.0;
            32.0 + (45.0 - 32.0) * t_sub
        } else {
            let t_sub = (y - 2030.0) / 20.0;
            45.0 + (85.0 - 45.0) * t_sub.powf(0.85)
        };

        // Grid Emission Factor (gCO2 / kWh): 722 (2025) -> 450 (2030) -> 40 (2050 Net-Zero)
        let grid_emission_factor = if y <= 2030.0 {
            let t_sub = (y - 2025.0) / 5.0;
            722.0 - (722.0 - 450.0) * t_sub
        } else {
            let t_sub = (y - 2030.0) / 20.0;
            450.0 - (450.0 - 40.0) * t_sub.powf(0.9)
        };

        // Cumulative Carbon Abated (Million Tonnes CO2e from 2025)
        let cumulative_abated_mt = t * 1450.0;

        TRAJECTORY_RESULTS_BUFFER[0] = total_capacity_gw;
        TRAJECTORY_RESULTS_BUFFER[1] = renewable_share_pct;
        TRAJECTORY_RESULTS_BUFFER[2] = grid_emission_factor;
        TRAJECTORY_RESULTS_BUFFER[3] = cumulative_abated_mt;
    }
    1
}

/// Execution Speed Benchmark Function (Returns executed iterations)
#[no_mangle]
pub extern "C" fn run_wasm_benchmark(iterations: i32) -> f64 {
    let mut accumulator: f64 = 0.0;
    for i in 0..iterations {
        calculate_dppa_economics(50.0 + (i as f64) * 0.1, 22.5, 0.082, 0.065, 0.012, 1.0);
        filter_and_aggregate_pillars(i % 4);
        project_pdp8_trajectory(2025.0 + ((i % 25) as f64));
        unsafe {
            accumulator += DPPA_RESULTS_BUFFER[0] + PILLARS_RESULTS_BUFFER[1] + TRAJECTORY_RESULTS_BUFFER[0];
        }
    }
    accumulator
}
