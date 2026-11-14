/**
 * Industrial Park CBAM Shield & Rooftop Solar Estimator - Revision 001
 * Material Design 3 Expressive Calculation Engine
 * Compliant with Decree 135/2024/ND-CP and EU Carbon Border Adjustment Mechanism (CBAM)
 */

(function () {
  'use strict';

  // Provincial Solar Irradiance Benchmark (Peak Sun Hours / day)
  const REGIONAL_IRRADIANCE = {
    // Northern Industrial Hubs (GHI ~ 3.8 - 4.1 h/day)
    'Bac Ninh': { ghi: 3.9, region: 'North', name: 'Bac Ninh (VSIP, Yen Phong, Que Vo)' },
    'Hai Phong': { ghi: 3.9, region: 'North', name: 'Hai Phong (DEEP C, Trang Due, Dinh Vu)' },
    'Hanoi': { ghi: 3.8, region: 'North', name: 'Hanoi (Thang Long, Quang Minh, Sai Dong)' },
    'Hai Duong': { ghi: 3.9, region: 'North', name: 'Hai Duong (Dai An, Tan Truong)' },
    'Hung Yen': { ghi: 3.9, region: 'North', name: 'Hung Yen (Thang Long II, Pho Noi A)' },
    'Vinh Phuc': { ghi: 3.8, region: 'North', name: 'Vinh Phuc (Khai Quang, Binh Xuyen)' },

    // Central Industrial Hubs (GHI ~ 4.4 - 4.8 h/day)
    'Da Nang': { ghi: 4.6, region: 'Central', name: 'Da Nang (Hoa Khanh, Lien Chieu)' },
    'Quang Nam': { ghi: 4.7, region: 'Central', name: 'Quang Nam (Chu Lai Open Economic Zone)' },
    'Khanh Hoa': { ghi: 4.8, region: 'Central', name: 'Khanh Hoa (Suoi Dau, Van Phong)' },

    // Southern Industrial Hubs (GHI ~ 4.8 - 5.2 h/day)
    'Binh Duong': { ghi: 4.9, region: 'South', name: 'Binh Duong (VSIP I/II/III, My Phuoc, Bau Bang)' },
    'Dong Nai': { ghi: 4.9, region: 'South', name: 'Dong Nai (Amata, Bien Hoa II, Nhon Trach)' },
    'Ho Chi Minh City': { ghi: 4.9, region: 'South', name: 'Ho Chi Minh City (Tan Thuan, Hiep Phuoc, Linh Trung)' },
    'Long An': { ghi: 5.0, region: 'South', name: 'Long An (Long Hau, Duc Hoa, Thu Thua)' },
    'Ba Ria - Vung Tau': { ghi: 5.1, region: 'South', name: 'Ba Ria - Vung Tau (Phu My, Cai Mep, Chau Duc)' }
  };

  // Technical & Economic Constants
  const CONSTANTS = {
    MODULE_EFFICIENCY_DENSITY: 0.165, // 165 Wp / m2 (~580W-620W N-type TOPCon)
    USABLE_ROOF_FACTOR: 0.75,         // 75% usable area after setbacks and skylights
    PERFORMANCE_RATIO: 0.81,          // 81% system efficiency (inverter, soiling, temp losses)
    GRID_EMISSION_FACTOR: 0.7221,     // 0.7221 tCO2e / MWh (Vietnam National Baseline)
    EU_ETS_CARBON_PRICE_USD: 80.0,    // $80 / tCO2 (~€75 benchmark EU allowance)
    EVN_COMMERCIAL_TARIFF_USD: 0.088, // ~$0.088 / kWh (average industrial tariff)
    TURNKEY_CAPEX_PER_KWP_USD: 580.0  // $580 / kWp turnkey commercial rooftop EPC
  };

  function calculateCBAMMetrics(params) {
    const {
      roofAreaM2,
      monthlyConsumptionKWh,
      province,
      decreeMode, // 'zero_export' or 'grid_tied'
      operatingShifts // 1, 2, or 3 shifts
    } = params;

    const irradiance = REGIONAL_IRRADIANCE[province] || { ghi: 4.8, region: 'South' };

    // 1. Solar Peak Capacity (kWp)
    const solarCapacityKWp = roofAreaM2 * CONSTANTS.MODULE_EFFICIENCY_DENSITY * CONSTANTS.USABLE_ROOF_FACTOR;

    // 2. Annual Energy Yield (MWh/year)
    const annualYieldMWh = (solarCapacityKWp * irradiance.ghi * 365 * CONSTANTS.PERFORMANCE_RATIO) / 1000;
    const annualYieldKWh = annualYieldMWh * 1000;

    // 3. Factory Annual Demand
    const annualConsumptionKWh = monthlyConsumptionKWh * 12;

    // 4. Shift Direct Solar Self-Consumption Ratio
    let directSolarUseRatio = 0.95; // 1-shift (Daytime peak)
    if (operatingShifts === 2) directSolarUseRatio = 0.78;
    if (operatingShifts === 3) directSolarUseRatio = 0.55;

    // 5. Utilized Solar Power (kWh/year)
    let utilizedYieldKWh = Math.min(annualYieldKWh * directSolarUseRatio, annualConsumptionKWh);
    let surplusYieldKWh = Math.max(0, annualYieldKWh - utilizedYieldKWh);

    // Decree 135 adjustment: If zero-export, surplus is curtailed
    let exportRevenueUSD = 0;
    if (decreeMode === 'grid_tied') {
      const allowedSellbackKWh = Math.min(surplusYieldKWh, annualYieldKWh * 0.20); // 20% cap
      exportRevenueUSD = allowedSellbackKWh * (CONSTANTS.EVN_COMMERCIAL_TARIFF_USD * 0.55); // ~55% avoided cost tariff
    }

    // 6. Annual Power Bill Savings ($)
    const annualPowerSavingsUSD = (utilizedYieldKWh * CONSTANTS.EVN_COMMERCIAL_TARIFF_USD) + exportRevenueUSD;

    // 7. Carbon Avoidance (tCO2e/year)
    const carbonAvoidedTons = (utilizedYieldKWh / 1000) * CONSTANTS.GRID_EMISSION_FACTOR;

    // 8. EU CBAM Tax Avoidance ($/year)
    const cbamTaxShieldUSD = carbonAvoidedTons * CONSTANTS.EU_ETS_CARBON_PRICE_USD;

    // 9. Total Combined Annual Value ($/year)
    const totalAnnualValueUSD = annualPowerSavingsUSD + cbamTaxShieldUSD;

    // 10. Financial Turnkey CAPEX & Payback Amortization
    const totalCapexUSD = solarCapacityKWp * CONSTANTS.TURNKEY_CAPEX_PER_KWP_USD;
    const paybackPeriodYears = totalAnnualValueUSD > 0 ? (totalCapexUSD / totalAnnualValueUSD) : 0;

    // 11. Energy Coverage Percentage
    const energyGreenedPercent = annualConsumptionKWh > 0
      ? Math.min(100, Math.round((utilizedYieldKWh / annualConsumptionKWh) * 100))
      : 0;

    return {
      solarCapacityKWp: Math.round(solarCapacityKWp),
      annualYieldMWh: Math.round(annualYieldMWh),
      annualPowerSavingsUSD: Math.round(annualPowerSavingsUSD),
      carbonAvoidedTons: Math.round(carbonAvoidedTons),
      cbamTaxShieldUSD: Math.round(cbamTaxShieldUSD),
      totalAnnualValueUSD: Math.round(totalAnnualValueUSD),
      totalCapexUSD: Math.round(totalCapexUSD),
      paybackPeriodYears: Number(paybackPeriodYears.toFixed(1)),
      energyGreenedPercent: energyGreenedPercent,
      regionName: irradiance.name,
      peakSunHours: irradiance.ghi
    };
  }

  // Export to global scope
  window.RVN_CBAM_Estimator = {
    calculate: calculateCBAMMetrics,
    REGIONAL_IRRADIANCE: REGIONAL_IRRADIANCE,
    CONSTANTS: CONSTANTS
  };
})();
