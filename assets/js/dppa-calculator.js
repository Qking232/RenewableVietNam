/**
 * ==============================================================================
 * Vietnam Decree 80/2024/NĐ-CP DPPA Wheeling & Tariff Simulation Engine
 * Platform: Renewable Viet Nam (renewablevietnam.com)
 * Standard: Decree 80/2024/NĐ-CP & Ministry of Industry and Trade (MOIT) Guidelines
 * ==============================================================================
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    define([], factory);
  } else if (typeof module === 'object' && module.exports) {
    module.exports = factory();
  } else {
    root.DPPACalculator = factory();
  }
}(typeof self !== 'undefined' ? self : this, function() {
  'use strict';

  // Constants & Statutory Baselines (2025/2026 Reference)
  var STATUTORY_CONSTANTS = {
    USD_VND_EXCHANGE_RATE: 25400,
    GRID_EMISSION_FACTOR_TCO2_PER_MWH: 0.7221, // MONRE / EVN Grid Emission Factor
    
    // EVN Time-of-Use Average Industrial Tariffs (VND/kWh, before VAT)
    EVN_INDUSTRIAL_TARIFFS: {
      voltage_above_110kv: { normal: 1685, peak: 2980, off_peak: 1044, avg: 1780 },
      voltage_22_to_110kv: { normal: 1720, peak: 3085, off_peak: 1085, avg: 1840 },
      voltage_under_22kv:   { normal: 1810, peak: 3171, off_peak: 1133, avg: 1920 }
    },

    // Statutory EVN Wheeling Cost Components (VND/kWh)
    WHEELING_COMPONENTS: {
      transmission_500_220kv: 79.4,   // EVN NPT transmission fee
      distribution_110kv: 145.0,      // Regional PC distribution fee (110kV)
      distribution_22kv: 240.0,       // Regional PC distribution fee (medium voltage)
      system_dispatch_ancillary: 45.0 // NSMO market operation & spinning reserve fee
    }
  };

  var DPPACalculator = {};

  /**
   * Case 1: Direct Private Line DPPA (Đường dây riêng)
   * Plant and consumer connected directly without routing through national grid.
   * 
   * @param {Object} params
   * @param {number} params.plantCapacityMW - Nameplate generation capacity (MW)
   * @param {number} params.annualGenerationGWh - Annual clean electricity generated (GWh)
   * @param {number} params.lineDistanceKm - Physical dedicated transmission line length (km)
   * @param {number} params.voltageKV - Voltage level (e.g. 22 or 110)
   * @param {number} [params.lineCapexPerKmUSD] - Construction cost per km (default $85,000 for 110kV, $35,000 for 22kV)
   * @param {number} [params.contractYears] - PPA contract duration (default 20 years)
   * @param {number} [params.generatorBasePpaUSD] - Generator PPA price ($/kWh, default $0.065)
   * @returns {Object} Comprehensive financial & carbon metrics
   */
  DPPACalculator.calculateCase1DirectPrivate = function(params) {
    var capacityMW = Number(params.plantCapacityMW) || 10;
    var genGWh = Number(params.annualGenerationGWh) || (capacityMW * 8760 * 0.18 / 1000); // 18% CF default
    var distanceKm = Number(params.lineDistanceKm) || 5;
    var voltageKV = Number(params.voltageKV) || 22;
    var years = Number(params.contractYears) || 20;
    var basePpaPriceUSD = Number(params.generatorBasePpaUSD) || 0.065;
    
    var capexPerKm = params.lineCapexPerKmUSD || (voltageKV >= 110 ? 85000 : 35000);
    var totalLineCapexUSD = distanceKm * capexPerKm;
    var annualLineAmortizationUSD = totalLineCapexUSD / years;
    var annualLineOmUSD = totalLineCapexUSD * 0.02; // 2% annual O&M
    
    var totalAnnualGenKWh = genGWh * 1000000;
    var levelizedLineCostUSDPerKWh = (annualLineAmortizationUSD + annualLineOmUSD) / totalAnnualGenKWh;
    var levelizedLineCostVNDPerKWh = levelizedLineCostUSDPerKWh * STATUTORY_CONSTANTS.USD_VND_EXCHANGE_RATE;
    
    var deliveredPowerPriceUSD = basePpaPriceUSD + levelizedLineCostUSDPerKWh;
    var deliveredPowerPriceVND = deliveredPowerPriceUSD * STATUTORY_CONSTANTS.USD_VND_EXCHANGE_RATE;
    
    var baselineEvnRateVND = STATUTORY_CONSTANTS.EVN_INDUSTRIAL_TARIFFS.voltage_22_to_110kv.avg;
    var annualCostSavingsVND = (baselineEvnRateVND - deliveredPowerPriceVND) * totalAnnualGenKWh;
    var annualCarbonAvoidedTons = genGWh * 1000 * STATUTORY_CONSTANTS.GRID_EMISSION_FACTOR_TCO2_PER_MWH;

    return {
      mechanism: 'CASE_1_DIRECT_PRIVATE_WIRE',
      statutoryReference: 'Decree 80/2024/NĐ-CP Chapter II',
      totalLineCapexUSD: Math.round(totalLineCapexUSD),
      levelizedLineCostVNDPerKWh: Math.round(levelizedLineCostVNDPerKWh * 10) / 10,
      deliveredPowerPriceUSDPerKWh: Math.round(deliveredPowerPriceUSD * 10000) / 10000,
      deliveredPowerPriceVNDPerKWh: Math.round(deliveredPowerPriceVND),
      baselineEvnRateVNDPerKWh: baselineEvnRateVND,
      annualCostSavingsVND: Math.round(annualCostSavingsVND),
      annualCostSavingsUSD: Math.round(annualCostSavingsVND / STATUTORY_CONSTANTS.USD_VND_EXCHANGE_RATE),
      annualCarbonAvoidedTonsCO2: Math.round(annualCarbonAvoidedTons),
      twentyYearCarbonAvoidedTonsCO2: Math.round(annualCarbonAvoidedTons * years)
    };
  };

  /**
   * Case 2: Grid-Connected DPPA via National Grid (Qua lưới điện quốc gia)
   * Power wheeled through EVN grid; consumer settles retail with EVN + CfD hedge with generator.
   * 
   * @param {Object} params
   * @param {number} params.annualContractGWh - Annual contracted volume (GWh)
   * @param {number} params.strikePriceVNDPerKWh - Agreed bilateral strike price with generator (VND/kWh)
   * @param {number} [params.voltageTier] - 'voltage_above_110kv' | 'voltage_22_to_110kv' | 'voltage_under_22kv'
   * @param {number} [params.imbalanceReserveVND] - Allowance for spot market imbalance buffer (default 35 VND)
   * @returns {Object} Comprehensive tariff breakdown & net effective cost
   */
  DPPACalculator.calculateCase2NationalGrid = function(params) {
    var volumeGWh = Number(params.annualContractGWh) || 50;
    var strikePrice = Number(params.strikePriceVNDPerKWh) || 1650;
    var tierKey = params.voltageTier || 'voltage_22_to_110kv';
    var imbalanceBuffer = Number(params.imbalanceReserveVND) || 35.0;

    var distFee = (tierKey === 'voltage_above_110kv') 
      ? STATUTORY_CONSTANTS.WHEELING_COMPONENTS.distribution_110kv 
      : STATUTORY_CONSTANTS.WHEELING_COMPONENTS.distribution_22kv;

    var transmissionFee = STATUTORY_CONSTANTS.WHEELING_COMPONENTS.transmission_500_220kv;
    var dispatchFee = STATUTORY_CONSTANTS.WHEELING_COMPONENTS.system_dispatch_ancillary;
    var totalWheelingCharge = transmissionFee + distFee + dispatchFee;

    // Net all-in delivered tariff (Strike Price + EVN Wheeling Charges + Imbalance Buffer)
    var allInCleanTariffVND = strikePrice + totalWheelingCharge + imbalanceBuffer;
    var allInCleanTariffUSD = allInCleanTariffVND / STATUTORY_CONSTANTS.USD_VND_EXCHANGE_RATE;

    var benchmarkEvn = STATUTORY_CONSTANTS.EVN_INDUSTRIAL_TARIFFS[tierKey] || STATUTORY_CONSTANTS.EVN_INDUSTRIAL_TARIFFS.voltage_22_to_110kv;
    var totalAnnualKWh = volumeGWh * 1000000;
    
    // Difference vs Standard EVN Retail Grid Power
    var annualDifferentialVND = (benchmarkEvn.avg - allInCleanTariffVND) * totalAnnualKWh;
    var annualCarbonAvoidedTons = volumeGWh * 1000 * STATUTORY_CONSTANTS.GRID_EMISSION_FACTOR_TCO2_PER_MWH;

    return {
      mechanism: 'CASE_2_NATIONAL_GRID_WHEELING',
      statutoryReference: 'Decree 80/2024/NĐ-CP Chapter III',
      volumeMWh: volumeGWh * 1000,
      strikePriceVNDPerKWh: strikePrice,
      wheelingCostBreakdownVND: {
        transmissionFee: transmissionFee,
        distributionFee: distFee,
        dispatchAncillaryFee: dispatchFee,
        totalWheelingFee: totalWheelingCharge
      },
      imbalanceBufferVND: imbalanceBuffer,
      allInCleanTariffVNDPerKWh: Math.round(allInCleanTariffVND),
      allInCleanTariffUSDPerKWh: Math.round(allInCleanTariffUSD * 10000) / 10000,
      benchmarkEvnAvgTariffVND: benchmarkEvn.avg,
      costPremiumOrDiscountPct: Math.round(((allInCleanTariffVND - benchmarkEvn.avg) / benchmarkEvn.avg) * 1000) / 10,
      annualCostDifferentialVND: Math.round(annualDifferentialVND),
      annualCostDifferentialUSD: Math.round(annualDifferentialVND / STATUTORY_CONSTANTS.USD_VND_EXCHANGE_RATE),
      annualCarbonAvoidedTonsCO2: Math.round(annualCarbonAvoidedTons)
    };
  };

  return DPPACalculator;
}));
