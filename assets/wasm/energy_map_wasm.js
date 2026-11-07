/**
 * Renewable Vietnam National Energy Grid & Cartography WebAssembly Engine
 * Target: 960+ Clean Generation Plants, 1,915 Grid Substations & Radial Intertie Calculations
 * Zero-copy static linear memory bridge
 */
(function(window) {
  'use strict';

  let wasmInstance = null;
  let wasmMemory = null;
  let subInPtr = 0;
  let plantInPtr = 0;
  let nearestSubResultsPtr = 0;
  let filterMatchesPtr = 0;
  let aggregationResultsPtr = 0;
  let isInitialized = false;

  const RVN_WASM_ENERGY_MAP = {
    isReady: function() {
      return isInitialized;
    },

    init: async function(wasmPath = '/assets/wasm/energy_map_wasm.wasm') {
      if (isInitialized) return true;
      try {
        let response = null;
        try {
          response = await fetch(wasmPath);
        } catch(netErr) {
          response = await fetch('assets/wasm/energy_map_wasm.wasm');
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
        subInPtr = wasmInstance.exports.get_substations_buffer_ptr();
        plantInPtr = wasmInstance.exports.get_plants_buffer_ptr();
        nearestSubResultsPtr = wasmInstance.exports.get_nearest_sub_results_ptr();
        filterMatchesPtr = wasmInstance.exports.get_filter_matches_ptr();
        aggregationResultsPtr = wasmInstance.exports.get_aggregation_results_ptr();
        isInitialized = true;

        console.log('[RVN_WASM] Energy Map Spatial & Transmission Engine initialized successfully (30 KB).');
        return true;
      } catch (err) {
        console.warn('[RVN_WASM] Energy Map WebAssembly instantiation fallback:', err);
        return false;
      }
    },

    loadSubstations: function(subsArray) {
      if (!isInitialized || !Array.isArray(subsArray)) return 0;
      const count = Math.min(subsArray.length, 3000);
      const inMem = new Float64Array(wasmMemory.buffer, subInPtr, count * 5);

      let validCount = 0;
      for (let i = 0; i < count; i++) {
        const s = subsArray[i];
        const lat = (s && s.lat !== null && !isNaN(s.lat)) ? Number(s.lat) : 0.0;
        const lng = (s && s.lng !== null && !isNaN(s.lng)) ? Number(s.lng) : 0.0;
        const origIdx = Number(i);
        const maxV = (s && s.max_v) ? Number(s.max_v) : 0.0;
        const txMva = (s && s.total_tx_mva) ? Number(s.total_tx_mva) : 0.0;

        const base = validCount * 5;
        inMem[base] = lat;
        inMem[base + 1] = lng;
        inMem[base + 2] = origIdx;
        inMem[base + 3] = maxV;
        inMem[base + 4] = txMva;
        validCount++;
      }

      return wasmInstance.exports.load_substations(validCount);
    },

    loadPlants: function(plantsArray) {
      if (!isInitialized || !Array.isArray(plantsArray)) return 0;
      const count = Math.min(plantsArray.length, 3000);
      const inMem = new Float64Array(wasmMemory.buffer, plantInPtr, count * 6);

      const fuelMap = {
        'solar': 1,
        'wind': 2,
        'hydro': 3,
        'hydropower': 3,
        'gas': 4,
        'lng': 4,
        'lng / gas': 4,
        'biomass': 5
      };

      for (let i = 0; i < count; i++) {
        const p = plantsArray[i];
        const lat = (p && p.lat) ? Number(p.lat) : 0.0;
        const lng = (p && (p.lng || p.lon)) ? Number(p.lng || p.lon) : 0.0;
        const origIdx = Number(i);
        const fuelSlug = (p && (p.fuel_slug || p.type || '')).toLowerCase();
        let fuelCode = 6; // Other
        for (const [k, v] of Object.entries(fuelMap)) {
          if (fuelSlug.includes(k)) {
            fuelCode = v;
            break;
          }
        }
        const capMw = (p && p.capacity_mw) ? Number(p.capacity_mw) : (parseFloat(p.capacity) || 0.0);
        const provHash = 0.0;

        const base = i * 6;
        inMem[base] = lat;
        inMem[base + 1] = lng;
        inMem[base + 2] = origIdx;
        inMem[base + 3] = fuelCode;
        inMem[base + 4] = capMw;
        inMem[base + 5] = provHash;
      }

      return wasmInstance.exports.load_plants(count);
    },

    findNearestSubstation: function(lat, lng, minKv = 110, plantMw = 50.0) {
      if (!isInitialized) return null;
      const found = wasmInstance.exports.find_nearest_substation(
        Number(lat) || 0.0,
        Number(lng) || 0.0,
        Number(minKv) || 110.0,
        Number(plantMw) || 50.0
      );

      if (!found) return null;

      const mem = new Float64Array(wasmMemory.buffer, nearestSubResultsPtr, 8);
      if (mem[0] < 0 || mem[7] === 0.0) return null;

      return {
        substationIndex: Math.round(mem[0]),
        distanceKm: mem[1],
        maxV: mem[2],
        txMva: mem[3],
        lineLossMw: mem[4],
        capexUsd: mem[5],
        headroomPct: mem[6]
      };
    },

    filterAndAggregatePlants: function(fuelCode = 0, minMw = 0.0, maxMw = 0.0) {
      if (!isInitialized) return null;
      const matchedCount = wasmInstance.exports.filter_and_aggregate_plants(
        parseInt(fuelCode, 10) || 0,
        Number(minMw) || 0.0,
        Number(maxMw) || 0.0
      );

      const aggMem = new Float64Array(wasmMemory.buffer, aggregationResultsPtr, 8);
      const matchMem = new Float64Array(wasmMemory.buffer, filterMatchesPtr, matchedCount);
      const matchedIndices = Array.from(matchMem).map(idx => Math.round(idx));

      return {
        matchedCount: Math.round(aggMem[0]),
        totalMw: aggMem[1],
        solarMw: aggMem[2],
        windMw: aggMem[3],
        hydroMw: aggMem[4],
        gasMw: aggMem[5],
        biomassMw: aggMem[6],
        avgMw: aggMem[7],
        matchedIndices: matchedIndices
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

  window.RVN_WASM_ENERGY_MAP = RVN_WASM_ENERGY_MAP;
})(window);
