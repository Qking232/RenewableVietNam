/**
 * Renewable Vietnam Apex Homepage High-Performance WebAssembly Analytical Engine
 * Target: 12-Pillars Vector Engine, Decree 80 DPPA Economic Solver & PDP8 Decarbonization Math
 * Zero-copy static linear memory bridge
 */
(function(window) {
  'use strict';

  let wasmInstance = null;
  let wasmMemory = null;
  let dppaResultsPtr = 0;
  let pillarsResultsPtr = 0;
  let trajectoryResultsPtr = 0;
  let isInitialized = false;

  const RVN_WASM_HOMEPAGE = {
    isReady: function() {
      return isInitialized;
    },

    init: async function(wasmPath = '/assets/wasm/rvn_homepage_wasm.wasm') {
      if (isInitialized) return true;
      try {
        let response = null;
        try {
          response = await fetch(wasmPath);
        } catch(netErr) {
          response = await fetch('assets/wasm/rvn_homepage_wasm.wasm');
        }

        if (!response.ok) {
          throw new Error(`HTTP error ${response.status} loading ${wasmPath}`);
        }

        let module = null;
        if (typeof WebAssembly.instantiateStreaming === 'function') {
          try {
            const streamed = await WebAssembly.instantiateStreaming(response.clone(), {});
            wasmInstance = streamed.instance;
          } catch(streamErr) {
            const buffer = await response.arrayBuffer();
            const instantiated = await WebAssembly.instantiate(buffer, {});
            wasmInstance = instantiated.instance;
          }
        } else {
          const buffer = await response.arrayBuffer();
          const instantiated = await WebAssembly.instantiate(buffer, {});
          wasmInstance = instantiated.instance;
        }

        wasmMemory = wasmInstance.exports.memory;
        dppaResultsPtr = wasmInstance.exports.get_dppa_results_ptr();
        pillarsResultsPtr = wasmInstance.exports.get_pillars_results_ptr();
        trajectoryResultsPtr = wasmInstance.exports.get_trajectory_results_ptr();
        isInitialized = true;

        console.log('[RVN_WASM] Homepage Analytical Engine initialized successfully (5.3 KB).');
        return true;
      } catch (err) {
        console.warn('[RVN_WASM] WebAssembly instantiation fallback:', err);
        return false;
      }
    },

    calculateDppa: function(capacityMw, capacityFactorPct, retailTariff = 0.082, ppaTariff = 0.065, wheelingCharge = 0.012, isDirect = 1.0) {
      if (!isInitialized) return null;
      wasmInstance.exports.calculate_dppa_economics(
        Number(capacityMw) || 50.0,
        Number(capacityFactorPct) || 22.5,
        Number(retailTariff) || 0.082,
        Number(ppaTariff) || 0.065,
        Number(wheelingCharge) || 0.012,
        Number(isDirect) || 1.0
      );

      const mem = new Float64Array(wasmMemory.buffer, dppaResultsPtr, 8);
      return {
        netAnnualMwh: mem[0],
        co2Tonnes: mem[1],
        annualSavingsMillions: mem[2],
        capexMillions: mem[3],
        simplePaybackYears: mem[4],
        npvMillions: mem[5],
        lcoeUsdKwh: mem[6],
        grossAnnualMwh: mem[7]
      };
    },

    getPillarsSummary: function(categoryFilter = 0) {
      if (!isInitialized) return null;
      wasmInstance.exports.filter_and_aggregate_pillars(parseInt(categoryFilter, 10) || 0);
      const mem = new Float64Array(wasmMemory.buffer, pillarsResultsPtr, 5);
      return {
        count: mem[0],
        totalCapexBillion: mem[1],
        totalTargetMw: mem[2],
        totalCodMw: mem[3],
        codPct: mem[4]
      };
    },

    getTrajectory: function(year = 2030) {
      if (!isInitialized) return null;
      wasmInstance.exports.project_pdp8_trajectory(Number(year) || 2030.0);
      const mem = new Float64Array(wasmMemory.buffer, trajectoryResultsPtr, 4);
      return {
        totalCapacityGw: mem[0],
        renewableSharePct: mem[1],
        gridEmissionFactor: mem[2],
        cumulativeAbatedMt: mem[3]
      };
    },

    benchmark: function(iterations = 10000) {
      if (!isInitialized) return null;
      const t0 = performance.now();
      wasmInstance.exports.run_wasm_benchmark(iterations);
      const t1 = performance.now();
      const elapsedMs = t1 - t0;
      const usPerOp = (elapsedMs * 1000) / iterations;
      return {
        iterations,
        elapsedMs: elapsedMs.toFixed(3),
        usPerOp: usPerOp.toFixed(3)
      };
    }
  };

  window.RVN_WASM_HOMEPAGE = RVN_WASM_HOMEPAGE;
})(window);
