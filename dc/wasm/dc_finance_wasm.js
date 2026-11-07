/**
 * Rust WebAssembly Financial Computing & Monte Carlo Loader
 * Zero external dependencies. High-performance direct linear memory sharing.
 */
(function(window) {
  'use strict';

  let wasmInstance = null;
  let isReady = false;

  async function initWasm(wasmUrl = '../wasm/dc_finance_wasm.wasm') {
    if (isReady && wasmInstance) return true;

    try {
      let result;
      if (typeof WebAssembly.instantiateStreaming === 'function') {
        try {
          result = await WebAssembly.instantiateStreaming(fetch(wasmUrl));
        } catch (streamErr) {
          // Fallback if streaming failed or MIME type was not application/wasm
          const resp = await fetch(wasmUrl);
          const bytes = await resp.arrayBuffer();
          result = await WebAssembly.instantiate(bytes);
        }
      } else {
        const resp = await fetch(wasmUrl);
        const bytes = await resp.arrayBuffer();
        result = await WebAssembly.instantiate(bytes);
      }

      wasmInstance = result.instance;
      isReady = true;
      console.log('[RUST_WASM] dc_finance_wasm initialized successfully (30.7 KB)');
      return true;
    } catch (err) {
      console.warn('[RUST_WASM] Failed to load WebAssembly module, utilizing JavaScript fallback:', err);
      isReady = false;
      return false;
    }
  }

  function isWasmReady() {
    return isReady && wasmInstance !== null;
  }

  function calculateNPV(tariff, capexPct, wacc, exitMult) {
    if (!isWasmReady()) return null;
    return wasmInstance.exports.calculate_npv(tariff, capexPct, wacc, exitMult);
  }

  function calculateExactIRR(tariff, capexPct, exitMult) {
    if (!isWasmReady()) return null;
    return wasmInstance.exports.calculate_exact_irr(tariff, capexPct, exitMult);
  }

  function runMonteCarlo(iterations, baseTariff, baseCapex, baseWacc, baseExit) {
    if (!isWasmReady()) return null;

    const t0 = performance.now();
    const seed = Date.now() + Math.random() * 1000000;
    wasmInstance.exports.run_monte_carlo(iterations, baseTariff, baseCapex, baseWacc, baseExit, seed);
    const t1 = performance.now();
    const elapsedMs = t1 - t0;

    const ptr = wasmInstance.exports.get_results_buffer_ptr();
    const mem = new Float64Array(wasmInstance.exports.memory.buffer, ptr, 48);

    const histBins = [];
    for (let i = 0; i < 32; i++) {
      histBins.push(mem[12 + i]);
    }

    return {
      p10: mem[0],
      p25: mem[1],
      p50: mem[2],
      p75: mem[3],
      p90: mem[4],
      mean: mem[5],
      stdDev: mem[6],
      var95: mem[7],
      var99: mem[8],
      hurdleRisk: mem[9],
      meanNpv: mem[10],
      p50Npv: mem[11],
      histBins: histBins,
      elapsedMs: elapsedMs,
      iterations: iterations
    };
  }

  window.DC_WASM_FINANCE = {
    init: initWasm,
    isReady: isWasmReady,
    calculateNPV: calculateNPV,
    calculateExactIRR: calculateExactIRR,
    runMonteCarlo: runMonteCarlo
  };
})(window);
