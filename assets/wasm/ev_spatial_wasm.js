/**
 * Rust WebAssembly EV Spatial & Route Corridor Computing Bridge
 * High-Performance 2D K-D Tree Indexing, Polyline Projection & Battery SoC Simulation
 * Targets: 22,055+ EV Charging Stations Across Vietnam
 */
(function(window) {
  'use strict';

  let wasmInstance = null;
  let isReady = false;
  let indexedStationsMap = null; // map station index -> station object reference

  async function initWasm(wasmUrl = '/assets/wasm/ev_spatial_wasm.wasm') {
    if (isReady && wasmInstance) return true;

    try {
      let result;
      if (typeof WebAssembly.instantiateStreaming === 'function') {
        try {
          result = await WebAssembly.instantiateStreaming(fetch(wasmUrl));
        } catch (streamErr) {
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
      console.log('[EV_RUST_WASM] ev_spatial_wasm initialized successfully (36.9 KB)');
      return true;
    } catch (err) {
      console.warn('[EV_RUST_WASM] Failed to initialize WebAssembly, falling back to JavaScript engine:', err);
      isReady = false;
      return false;
    }
  }

  function isWasmReady() {
    return isReady && wasmInstance !== null;
  }

  function loadStations(stations) {
    if (!isWasmReady() || !Array.isArray(stations) || !stations.length) return 0;

    const n = Math.min(stations.length, 35000);
    indexedStationsMap = new Array(n);

    const ptr = wasmInstance.exports.get_stations_input_buffer_ptr();
    const mem = new Float64Array(wasmInstance.exports.memory.buffer, ptr, n * 6);

    for (let i = 0; i < n; i++) {
      const s = stations[i];
      indexedStationsMap[i] = s;

      const lat = parseFloat(s.lat || s.latitude) || 0.0;
      const lng = parseFloat(s.lng || s.longitude) || 0.0;
      const kw = parseFloat(s.kw || s.power || 0.0) || 60.0;
      const isDC = (s.isDC || /dc|fast|ultra/i.test(s.conn || s.port || '')) ? 1.0 : 0.0;
      const isVF = (/vinfast/i.test(s.cpo || '') || /vinfast/i.test(s.name || '')) ? 1.0 : 0.0;

      const off = i * 6;
      mem[off] = lat;
      mem[off + 1] = lng;
      mem[off + 2] = i; // internal index
      mem[off + 3] = kw;
      mem[off + 4] = isDC;
      mem[off + 5] = isVF;
    }

    const t0 = performance.now();
    const loadedCount = wasmInstance.exports.load_stations_from_input_buffer(n);
    const t1 = performance.now();
    console.log(`[EV_RUST_WASM] Indexed ${loadedCount} stations into 2D spatial grid in ${(t1 - t0).toFixed(2)} ms`);
    return loadedCount;
  }

  function findNearest(userLat, userLng, dcOnly = 0, nonVfOnly = 0, maxRadiusKm = 100.0) {
    if (!isWasmReady()) return null;

    const t0 = performance.now();
    const id = wasmInstance.exports.find_nearest_station(userLat, userLng, dcOnly ? 1 : 0, nonVfOnly ? 1 : 0, maxRadiusKm);
    const t1 = performance.now();

    if (id < 0 || !indexedStationsMap) return null;
    const station = indexedStationsMap[id];
    return {
      station: station,
      queryTimeMs: t1 - t0
    };
  }

  function projectCorridor(coords, cumDist, maxDetourKm = 5.0, dcOnly = 0, nonVfOnly = 0, minAlong = 5.0, maxAlong = 99999.0) {
    if (!isWasmReady() || !coords || coords.length < 2) return null;

    const m = Math.min(coords.length, 4000);
    const routePtr = wasmInstance.exports.get_route_input_buffer_ptr();
    const routeMem = new Float64Array(wasmInstance.exports.memory.buffer, routePtr, m * 3);

    for (let j = 0; j < m; j++) {
      const c = coords[j];
      const off = j * 3;
      // coords can be [lng, lat] (GeoJSON) or [lat, lng]
      const lat = (c[1] !== undefined) ? c[1] : c.lat;
      const lng = (c[0] !== undefined) ? c[0] : c.lng;
      const d = cumDist[j] || 0.0;

      routeMem[off] = lat;
      routeMem[off + 1] = lng;
      routeMem[off + 2] = d;
    }

    wasmInstance.exports.load_route_from_input_buffer(m);

    const t0 = performance.now();
    const count = wasmInstance.exports.project_corridor_stations(
      maxDetourKm,
      dcOnly ? 1 : 0,
      nonVfOnly ? 1 : 0,
      minAlong,
      maxAlong
    );
    const t1 = performance.now();

    const outPtr = wasmInstance.exports.get_corridor_results_ptr();
    const outMem = new Float64Array(wasmInstance.exports.memory.buffer, outPtr, count * 6);

    const matchedStations = [];
    for (let k = 0; k < count; k++) {
      const off = k * 6;
      const sId = outMem[off];
      const distAlong = outMem[off + 1];
      const detour = outMem[off + 2];
      const kw = outMem[off + 3];
      const isDC = outMem[off + 4] > 0.5;
      const isVF = outMem[off + 5] > 0.5;

      const station = (indexedStationsMap && indexedStationsMap[sId]) || null;
      if (station) {
        matchedStations.push({
          station: station,
          distAlongKm: distAlong,
          detourKm: detour,
          kw: kw,
          isDC: isDC,
          isVF: isVF
        });
      }
    }

    return {
      stations: matchedStations,
      count: count,
      scanTimeMs: t1 - t0
    };
  }

  function simulateEvStops(totalDistKm, batteryKwh, maxRangeKm, startSocPct, minSocPct, targetSocPct, carMaxKw = 150.0) {
    if (!isWasmReady()) return null;

    const t0 = performance.now();
    const stopsCount = wasmInstance.exports.simulate_ev_stops(
      totalDistKm,
      batteryKwh,
      maxRangeKm,
      startSocPct,
      minSocPct,
      targetSocPct,
      carMaxKw
    );
    const t1 = performance.now();

    const itinPtr = wasmInstance.exports.get_itin_results_ptr();
    const itinMem = new Float64Array(wasmInstance.exports.memory.buffer, itinPtr, stopsCount * 8);

    const stops = [];
    for (let s = 0; s < stopsCount; s++) {
      const off = s * 8;
      const sId = itinMem[off];
      const distAlong = itinMem[off + 1];
      const arrSoc = itinMem[off + 2];
      const depSoc = itinMem[off + 3];
      const chargeMin = itinMem[off + 4];
      const kwhAdded = itinMem[off + 5];
      const kw = itinMem[off + 6];
      const detour = itinMem[off + 7];

      const station = (indexedStationsMap && indexedStationsMap[sId]) || null;
      stops.push({
        station: station,
        distAlongKm: distAlong,
        arrSocPct: arrSoc,
        depSocPct: depSoc,
        chargeMin: chargeMin,
        kwhAdded: kwhAdded,
        kw: kw,
        detourKm: detour
      });
    }

    return {
      stops: stops,
      stopsCount: stopsCount,
      simTimeMs: t1 - t0
    };
  }

  window.EV_WASM_SPATIAL = {
    init: initWasm,
    isReady: isWasmReady,
    loadStations: loadStations,
    findNearest: findNearest,
    projectCorridor: projectCorridor,
    simulateEvStops: simulateEvStops
  };
})(window);
