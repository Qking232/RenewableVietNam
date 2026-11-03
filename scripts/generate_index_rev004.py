#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate index_Rev.004.html integrating the National Power Grid model into energy.renewablevietnam.com
"""

import re
from pathlib import Path

SOURCE_HTML = Path(r"G:\My Drive\7. AI\RenewableVietNam\projectenergy\index.html")
TARGET_HTML = Path(r"G:\My Drive\7. AI\RenewableVietNam\projectenergy\index_Rev.004.html")

def generate_revision():
    with open(SOURCE_HTML, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Add Leaflet CSS & JS in <head> if not already present
    leaflet_tags = """  <!-- Leaflet GIS Cartography Engine for National Transmission Grid -->
  <link rel="stylesheet" href="vendor/leaflet/leaflet.css" />
  <script src="vendor/leaflet/leaflet.js"></script>
"""
    if "vendor/leaflet/leaflet.css" not in html:
        html = html.replace("</head>", f"{leaflet_tags}\n</head>", 1)

    # 2. Expand Hero Telemetry strip from 4 to 5 cards
    grid_hero_card = """        <div class="p-3 rounded-xl bg-white dark:bg-darkCard border border-borderSlate dark:border-darkBorder shadow-sm space-y-0.5">
          <span class="font-mono text-[9px] sm:text-[10px] uppercase tracking-wider text-inkMuted dark:text-textDarkMuted">Transmission Grid</span>
          <div class="text-lg sm:text-xl font-bold font-mono text-rose-600 dark:text-rose-400">65,566 <span class="text-xs font-normal">km</span></div>
          <p class="text-[9px] sm:text-[10px] text-inkMuted dark:text-textDarkMuted">1,915 Substations (500/220/110kV)</p>
        </div>"""

    # Replace grid-cols-2 lg:grid-cols-4 with grid-cols-2 lg:grid-cols-5
    html = html.replace('grid grid-cols-2 lg:grid-cols-4 gap-2.5 sm:gap-3 pt-0.5', 'grid grid-cols-2 lg:grid-cols-5 gap-2.5 sm:gap-3 pt-0.5', 1)
    
    # Add the 5th card after Required Pipeline Delta card
    delta_card_marker = """<div class="p-3 rounded-xl bg-white dark:bg-darkCard border border-borderSlate dark:border-darkBorder shadow-sm space-y-0.5">\n          <span class="font-mono text-[9px] sm:text-[10px] uppercase tracking-wider text-inkMuted dark:text-textDarkMuted">Required Pipeline Delta</span>"""
    
    # Let's find the closing div of Required Pipeline Delta card
    pattern = r'(<div class="p-3 rounded-xl bg-white dark:bg-darkCard border border-borderSlate dark:border-darkBorder shadow-sm space-y-0.5">\s*<span[^>]*>Required Pipeline Delta</span>[\s\S]*?</div>\s*</div>)'
    
    def repl_delta(match):
        return match.group(1).rsplit('</div>', 1)[0] + '</div>\n\n' + grid_hero_card + '\n      </div>'
        
    html = re.sub(pattern, repl_delta, html, count=1)

    # 3. Add 3rd View Switcher Tab (National Grid)
    tab_replacement = """              <button id="tabAssetsBtn" class="flex-1 sm:flex-initial px-3 py-1 rounded-md bg-teal-600 text-white font-semibold transition-all cursor-pointer">
                Assets Dossier (<span id="totalAssetsCount">960</span>)
              </button>
              <button id="tabPipelineBtn" class="flex-1 sm:flex-initial px-3 py-1 rounded-md text-inkMuted dark:text-textDarkMuted hover:text-inkPrimary dark:hover:text-white transition-all cursor-pointer">
                PDP8 Priority (<span id="pipelineCount">10</span>)
              </button>
              <button id="tabGridBtn" class="flex-1 sm:flex-initial px-3 py-1 rounded-md text-inkMuted dark:text-textDarkMuted hover:text-inkPrimary dark:hover:text-white transition-all cursor-pointer">
                National Grid (<span id="totalGridSubstationsCount">1,915</span>)
              </button>"""

    tab_pattern = r'<button id="tabAssetsBtn"[\s\S]*?<button id="tabPipelineBtn"[\s\S]*?</button>'
    html = re.sub(tab_pattern, tab_replacement, html, count=1)

    # 4. Insert VIEW 3: National Grid Container into dossierScrollArea
    grid_view_html = """          <!-- VIEW 3: NATIONAL ELECTRICAL GRID NETWORK (NSMO 2025 MODEL) -->
          <div id="viewGridContainer" class="hidden space-y-3">
            <!-- Grid Navigation Sub-Bar & Voltage Filters -->
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2.5 p-3 rounded-xl bg-slate-50/80 dark:bg-darkCard/60 border border-borderSlate dark:border-darkBorder">
              <div class="flex items-center gap-1 font-mono text-[11px]">
                <button id="gridSubViewMapBtn" class="px-2.5 py-1 rounded-md bg-rose-600 text-white font-semibold cursor-pointer">
                  Topology Map
                </button>
                <button id="gridSubViewSubstationsBtn" class="px-2.5 py-1 rounded-md bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder text-inkMuted dark:text-textDarkMuted hover:text-rose-600 cursor-pointer">
                  Substations (1,915)
                </button>
                <button id="gridSubViewLinesBtn" class="px-2.5 py-1 rounded-md bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder text-inkMuted dark:text-textDarkMuted hover:text-rose-600 cursor-pointer">
                  Transmission Lines (2,877)
                </button>
              </div>

              <!-- Voltage Selector Pills -->
              <div class="flex items-center gap-1 font-mono text-[10px] overflow-x-auto no-scrollbar">
                <span class="text-slate-400 uppercase tracking-wider mr-1 shrink-0">Voltage:</span>
                <button data-v="ALL" class="grid-v-pill px-2 py-0.5 rounded bg-rose-600 text-white font-semibold cursor-pointer">All</button>
                <button data-v="500" class="grid-v-pill px-2 py-0.5 rounded bg-white dark:bg-darkSurface border border-rose-300 dark:border-rose-800 text-rose-600 dark:text-rose-400 cursor-pointer">500 kV (92)</button>
                <button data-v="220" class="grid-v-pill px-2 py-0.5 rounded bg-white dark:bg-darkSurface border border-amber-300 dark:border-amber-800 text-amber-600 dark:text-amber-400 cursor-pointer">220 kV (326)</button>
                <button data-v="110" class="grid-v-pill px-2 py-0.5 rounded bg-white dark:bg-darkSurface border border-sky-300 dark:border-sky-800 text-sky-600 dark:text-sky-400 cursor-pointer">110 kV (1,497)</button>
              </div>
            </div>

            <!-- SUB-VIEW A: LEAFLET GIS TOPOLOGY MAP -->
            <div id="gridSubViewMap" class="space-y-2">
              <div class="relative w-full h-[540px] rounded-xl border border-borderSlate dark:border-darkBorder overflow-hidden shadow-inner bg-slate-900">
                <div id="gridTopologyMap" class="w-full h-full z-10"></div>
                <!-- Interactive Floating Legend -->
                <div class="absolute bottom-3 left-3 z-20 p-2.5 rounded-lg bg-white/90 dark:bg-darkSurface/90 backdrop-blur-md border border-borderSlate dark:border-darkBorder shadow-md font-mono text-[10px] space-y-1">
                  <div class="font-bold text-inkPrimary dark:text-textDarkPrimary uppercase tracking-wider mb-1">Grid Corridors</div>
                  <div class="flex items-center gap-2">
                    <span class="w-3.5 h-1 rounded-full bg-rose-500"></span>
                    <span class="text-inkPrimary dark:text-textDarkPrimary font-semibold">500 kV Supergrid (15,888 km)</span>
                  </div>
                  <div class="flex items-center gap-2">
                    <span class="w-3.5 h-1 rounded-full bg-amber-500"></span>
                    <span class="text-inkPrimary dark:text-textDarkPrimary font-semibold">220 kV Regional Grid (27,007 km)</span>
                  </div>
                  <div class="flex items-center gap-2">
                    <span class="w-3.5 h-1 rounded-full bg-cyan-500"></span>
                    <span class="text-inkPrimary dark:text-textDarkPrimary font-semibold">110 kV Interties (22,672 km)</span>
                  </div>
                  <div class="pt-1 border-t border-borderSlate/60 dark:border-darkBorder/60 text-[9px] text-slate-400">
                    Source: NSMO Model Vietnam 2025
                  </div>
                </div>
              </div>
            </div>

            <!-- SUB-VIEW B: SUBSTATIONS DIRECTORY TABLE -->
            <div id="gridSubViewSubstations" class="hidden space-y-2.5">
              <div class="flex items-center gap-2">
                <input type="text" id="gridSubstationSearchInput" placeholder="Search substations by name, province, or bay code..." class="flex-1 px-3 py-1.5 rounded-lg bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder text-inkPrimary dark:text-textDarkPrimary text-xs font-mono focus:outline-none focus:border-rose-500" />
                <span id="gridSubstationCountBadge" class="font-mono text-[11px] text-inkMuted dark:text-textDarkMuted px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-darkCard border border-borderSlate dark:border-darkBorder whitespace-nowrap">
                  Showing 1,915 Substations
                </span>
              </div>
              <div class="rounded-xl border border-borderSlate dark:border-darkBorder overflow-hidden">
                <div class="overflow-x-auto max-h-[500px]">
                  <table class="w-full text-left border-collapse text-xs">
                    <thead class="sticky top-0 z-10 bg-slate-100 dark:bg-darkCard font-mono text-[10px] uppercase text-inkMuted dark:text-textDarkMuted border-b border-borderSlate dark:border-darkBorder">
                      <tr>
                        <th class="p-2.5">Substation Name</th>
                        <th class="p-2.5 text-center">Voltage Class</th>
                        <th class="p-2.5 text-right">Transformers</th>
                        <th class="p-2.5 text-right">Generation</th>
                        <th class="p-2.5">Location / Province</th>
                        <th class="p-2.5 text-right">Technical Dossier</th>
                      </tr>
                    </thead>
                    <tbody id="gridSubstationsTableBody" class="divide-y divide-borderSlate dark:divide-darkBorder font-mono">
                      <!-- Populated dynamically via renderGridSubstationsTable() -->
                    </tbody>
                  </table>
                </div>
              </div>
            </div>

            <!-- SUB-VIEW C: TRANSMISSION LINES DIRECTORY TABLE -->
            <div id="gridSubViewLines" class="hidden space-y-2.5">
              <div class="flex items-center gap-2">
                <input type="text" id="gridLineSearchInput" placeholder="Search transmission lines by corridor, substation, or conductor..." class="flex-1 px-3 py-1.5 rounded-lg bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder text-inkPrimary dark:text-textDarkPrimary text-xs font-mono focus:outline-none focus:border-rose-500" />
                <span id="gridLineCountBadge" class="font-mono text-[11px] text-inkMuted dark:text-textDarkMuted px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-darkCard border border-borderSlate dark:border-darkBorder whitespace-nowrap">
                  Showing 2,877 Circuits
                </span>
              </div>
              <div class="rounded-xl border border-borderSlate dark:border-darkBorder overflow-hidden">
                <div class="overflow-x-auto max-h-[500px]">
                  <table class="w-full text-left border-collapse text-xs">
                    <thead class="sticky top-0 z-10 bg-slate-100 dark:bg-darkCard font-mono text-[10px] uppercase text-inkMuted dark:text-textDarkMuted border-b border-borderSlate dark:border-darkBorder">
                      <tr>
                        <th class="p-2.5">Circuit Corridor (From - To)</th>
                        <th class="p-2.5 text-center">Voltage</th>
                        <th class="p-2.5">Conductor</th>
                        <th class="p-2.5 text-right">R (Ω)</th>
                        <th class="p-2.5 text-right">X (Ω)</th>
                        <th class="p-2.5 text-right">Length (km)</th>
                      </tr>
                    </thead>
                    <tbody id="gridLinesTableBody" class="divide-y divide-borderSlate dark:divide-darkBorder font-mono">
                      <!-- Populated dynamically via renderGridLinesTable() -->
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>"""

    # Insert grid_view_html right after viewPipelineContainer
    pipeline_closing_tag = """            <div id="pdp8ProjectsGrid" class="space-y-2.5">\n              <!-- Populated dynamically from pdp8_targets.json priority_projects -->\n            </div>\n          </div>"""
    if pipeline_closing_tag in html:
        html = html.replace(pipeline_closing_tag, f"{pipeline_closing_tag}\n\n{grid_view_html}", 1)
    else:
        # Fallback placement before closing dossierScrollArea
        html = html.replace('</div>\n\n        <!-- Sticky Bottom Pagination Bar -->', f'{grid_view_html}\n        </div>\n\n        <!-- Sticky Bottom Pagination Bar -->', 1)

    # 5. Add Substation Technical Dossier Modal
    substation_modal_html = """  <!-- ==================================================================== -->
  <!-- SUBSTATION TECHNICAL DOSSIER MODAL                                   -->
  <!-- ==================================================================== -->
  <div id="substationModalOverlay" class="fixed inset-0 z-50 bg-black/60 backdrop-blur-xs flex items-center justify-center p-4 hidden">
    <div class="bg-white dark:bg-darkCard border border-borderSlate dark:border-darkBorder rounded-2xl max-w-xl w-full p-6 shadow-2xl space-y-5 animate-in fade-in duration-200">
      <div class="flex items-start justify-between pb-3 border-b border-borderSlate dark:border-darkBorder">
        <div>
          <span id="substationModalVoltageBadge" class="px-2 py-0.5 rounded text-[10px] font-mono font-bold uppercase bg-rose-500/10 text-rose-600 border border-rose-500/20">
            500 kV Substation
          </span>
          <h3 id="substationModalName" class="text-xl font-bold text-inkPrimary dark:text-textDarkPrimary mt-1">
            Substation Name
          </h3>
          <p id="substationModalPlace" class="text-xs text-inkMuted dark:text-textDarkMuted font-mono">Location, Vietnam</p>
        </div>
        <button id="closeSubstationModalBtn" class="text-slate-400 hover:text-slate-700 dark:hover:text-white p-1 rounded-lg cursor-pointer">
          <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>

      <div class="space-y-4 font-mono text-xs">
        <div class="grid grid-cols-2 gap-3">
          <div class="p-3 rounded-lg bg-slate-50 dark:bg-darkSurface border border-borderSlate dark:border-darkBorder space-y-0.5">
            <span class="text-slate-400 text-[10px] uppercase">Installed Transformers</span>
            <div id="substationModalTx" class="text-sm font-bold text-inkPrimary dark:text-textDarkPrimary">-- Units / -- MVA</div>
          </div>
          <div class="p-3 rounded-lg bg-slate-50 dark:bg-darkSurface border border-borderSlate dark:border-darkBorder space-y-0.5">
            <span class="text-slate-400 text-[10px] uppercase">Connected Generation</span>
            <div id="substationModalGen" class="text-sm font-bold text-rose-600 dark:text-rose-400">-- Units / -- MW</div>
          </div>
        </div>

        <div class="p-3 rounded-lg bg-slate-50 dark:bg-darkSurface border border-borderSlate dark:border-darkBorder space-y-1">
          <span class="text-slate-400 text-[10px] uppercase">Substation Bay Codes &amp; Feeders</span>
          <div id="substationModalBays" class="text-xs text-inkPrimary dark:text-textDarkPrimary font-mono break-all">--</div>
        </div>

        <div class="p-3 rounded-lg bg-slate-50 dark:bg-darkSurface border border-borderSlate dark:border-darkBorder space-y-1">
          <span class="text-slate-400 text-[10px] uppercase">Geospatial Telemetry (WGS84)</span>
          <div id="substationModalCoords" class="text-xs text-inkMuted dark:text-textDarkMuted">Lat: --, Lng: --</div>
        </div>
      </div>

      <div class="flex items-center justify-end gap-2 pt-2 border-t border-borderSlate dark:border-darkBorder">
        <a id="substationModalGmapsLink" href="#" target="_blank" rel="noopener noreferrer" class="px-3.5 py-1.5 rounded-lg bg-rose-600 hover:bg-rose-500 text-white font-mono text-xs font-semibold flex items-center gap-1.5 transition-colors">
          <span>Satellite Inspection</span>
          <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
          </svg>
        </a>
      </div>
    </div>
  </div>"""

    # Insert substation modal before footer
    html = html.replace('<!-- ==================================================================== -->\n  <!-- INSTITUTIONAL FOOTER', f'{substation_modal_html}\n\n  <!-- ==================================================================== -->\n  <!-- INSTITUTIONAL FOOTER', 1)

    # 6. Insert Grid JavaScript Logic
    grid_js_code = """
    // ========================================================================
    // NATIONAL TRANSMISSION GRID LOGIC (NSMO 2025 MODEL INTEGRATION)
    // ========================================================================
    let ALL_GRID_SUBSTATIONS = [];
    let ALL_GRID_LINES = [];
    let FILTERED_GRID_SUBSTATIONS = [];
    let FILTERED_GRID_LINES = [];
    let selectedGridVoltage = "ALL";
    let gridMapInstance = null;
    let gridMapLayerGroup = null;

    async function loadGridData() {
      try {
        if (window.RV_Supabase) {
          const subsRaw = await window.RV_Supabase.getWithFallback('grid_substations', '/data/vietnam_grid_substations.json', {
            cacheKey: 'grid_substations'
          });
          const linesRaw = await window.RV_Supabase.getWithFallback('grid_lines', '/data/vietnam_grid_lines.json', {
            cacheKey: 'grid_lines'
          });
          if (Array.isArray(subsRaw) && subsRaw.length > 0) ALL_GRID_SUBSTATIONS = subsRaw;
          if (Array.isArray(linesRaw) && linesRaw.length > 0) ALL_GRID_LINES = linesRaw;
        } else {
          const [sRes, lRes] = await Promise.all([
            fetch('/data/vietnam_grid_substations.json'),
            fetch('/data/vietnam_grid_lines.json')
          ]);
          if (sRes.ok) ALL_GRID_SUBSTATIONS = await sRes.json();
          if (lRes.ok) ALL_GRID_LINES = await lRes.json();
        }

        FILTERED_GRID_SUBSTATIONS = ALL_GRID_SUBSTATIONS;
        FILTERED_GRID_LINES = ALL_GRID_LINES;

        const subCountEl = document.getElementById('totalGridSubstationsCount');
        if (subCountEl) subCountEl.textContent = ALL_GRID_SUBSTATIONS.length.toLocaleString();

        renderGridSubstationsTable();
        renderGridLinesTable();
        if (activeTab === 'grid') {
          setTimeout(initGridMap, 100);
        }
      } catch (err) {
        console.warn('Grid data load bypassed:', err);
      }
    }

    function initGridMap() {
      const mapContainer = document.getElementById('gridTopologyMap');
      if (!mapContainer || typeof L === 'undefined') return;

      if (!gridMapInstance) {
        gridMapInstance = L.map('gridTopologyMap', {
          center: [16.0, 106.5],
          zoom: 6,
          zoomControl: true,
          attributionControl: false
        });

        // High-contrast clean dark/light cartography base tiles
        const isDark = document.documentElement.classList.contains('dark');
        const tileUrl = isDark 
          ? 'https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png'
          : 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png';

        L.tileLayer(tileUrl, { maxZoom: 18 }).addTo(gridMapInstance);
        gridMapLayerGroup = L.layerGroup().addTo(gridMapInstance);
      }

      renderGridMapVectors();
    }

    function renderGridMapVectors() {
      if (!gridMapInstance || !gridMapLayerGroup) return;
      gridMapLayerGroup.clearLayers();

      const vFilter = selectedGridVoltage;

      // 1. Render Transmission Line Vectors
      ALL_GRID_LINES.forEach(l => {
        if (!l.coords || l.coords.length < 2) return;
        if (vFilter !== 'ALL' && String(l.v_kv) !== String(vFilter)) return;

        const latLngs = [[l.coords[0][1], l.coords[0][0]], [l.coords[1][1], l.coords[1][0]]];
        let color = '#06b6d4'; // 110kV
        let weight = 1.4;
        let opacity = 0.65;

        if (l.v_kv === 500) {
          color = '#f43f5e';
          weight = 3.2;
          opacity = 0.9;
        } else if (l.v_kv === 220) {
          color = '#f59e0b';
          weight = 2.0;
          opacity = 0.8;
        }

        const poly = L.polyline(latLngs, {
          color: color,
          weight: weight,
          opacity: opacity,
          dashArray: l.dashed ? '4, 4' : null
        });

        poly.bindPopup(`
          <div class="font-mono text-xs space-y-1 p-1">
            <div class="font-bold text-rose-600 dark:text-rose-400">${l.v_kv} kV Transmission Circuit</div>
            <div><strong>From:</strong> ${l.s1_name || l.s1_id}</div>
            <div><strong>To:</strong> ${l.s2_name || l.s2_id}</div>
            <div><strong>Conductor:</strong> ${l.conductor || 'Standard'}</div>
            <div><strong>Est. Length:</strong> ${l.len_km} km</div>
            <div><strong>Impedance:</strong> R=${l.r} Ω, X=${l.x} Ω</div>
          </div>
        `);

        poly.addTo(gridMapLayerGroup);
      });

      // 2. Render Substation Circle Markers
      ALL_GRID_SUBSTATIONS.forEach(s => {
        if (s.lat === null || s.lng === null) return;
        if (vFilter !== 'ALL' && !s.voltages.includes(parseInt(vFilter))) return;

        let fillColor = '#06b6d4';
        let radius = 3.5;
        if (s.max_v >= 500) {
          fillColor = '#f43f5e';
          radius = 6.5;
        } else if (s.max_v >= 220) {
          fillColor = '#f59e0b';
          radius = 4.8;
        }

        const marker = L.circleMarker([s.lat, s.lng], {
          radius: radius,
          fillColor: fillColor,
          color: '#ffffff',
          weight: 1,
          opacity: 0.9,
          fillOpacity: 0.85
        });

        marker.on('click', () => openSubstationModal(s.id));
        marker.bindTooltip(`<strong>${s.name}</strong> (${s.max_v}kV)`, { direction: 'top', offset: [0, -5] });
        marker.addTo(gridMapLayerGroup);
      });
    }

    function renderGridSubstationsTable() {
      const tbody = document.getElementById('gridSubstationsTableBody');
      if (!tbody) return;

      const q = (document.getElementById('gridSubstationSearchInput')?.value || '').toLowerCase().trim();
      const vFilter = selectedGridVoltage;

      const list = ALL_GRID_SUBSTATIONS.filter(s => {
        if (vFilter !== 'ALL' && !s.voltages.includes(parseInt(vFilter))) return false;
        if (q) {
          const matchName = (s.name || '').toLowerCase().includes(q);
          const matchPlace = (s.place || '').toLowerCase().includes(q);
          const matchBays = (s.bay_codes || '').toLowerCase().includes(q);
          if (!matchName && !matchPlace && !matchBays) return false;
        }
        return true;
      });

      const badge = document.getElementById('gridSubstationCountBadge');
      if (badge) badge.textContent = `Showing ${list.length.toLocaleString()} of ${ALL_GRID_SUBSTATIONS.length.toLocaleString()} Substations`;

      // Render top 100 for responsive scrolling
      tbody.innerHTML = list.slice(0, 100).map(s => {
        const vBadgeColor = s.max_v >= 500 
          ? 'bg-rose-500/10 text-rose-600 border-rose-500/20' 
          : (s.max_v >= 220 ? 'bg-amber-500/10 text-amber-600 border-amber-500/20' : 'bg-sky-500/10 text-sky-600 border-sky-500/20');

        return `
          <tr class="hover:bg-slate-50/80 dark:hover:bg-darkCard/50 transition-colors cursor-pointer" onclick="openSubstationModal('${s.id}')">
            <td class="p-2.5 font-semibold text-inkPrimary dark:text-textDarkPrimary">${s.name}</td>
            <td class="p-2.5 text-center">
              <span class="px-2 py-0.5 rounded text-[10px] font-bold border ${vBadgeColor}">
                ${s.voltages.join('/')} kV
              </span>
            </td>
            <td class="p-2.5 text-right font-medium text-inkPrimary dark:text-textDarkPrimary">
              ${s.tx_count > 0 ? `${s.tx_count} tx (${s.total_tx_mva} MVA)` : '-'}
            </td>
            <td class="p-2.5 text-right font-medium text-rose-600 dark:text-rose-400">
              ${s.gen_count > 0 ? `${s.gen_count} gen (${s.total_gen_mw} MW)` : '-'}
            </td>
            <td class="p-2.5 text-inkMuted dark:text-textDarkMuted text-[11px] truncate max-w-[200px]">${s.place || 'Vietnam'}</td>
            <td class="p-2.5 text-right">
              <button onclick="event.stopPropagation(); openSubstationModal('${s.id}')" class="px-2.5 py-1 rounded bg-slate-100 dark:bg-darkCard hover:bg-rose-50 dark:hover:bg-rose-950/40 text-inkPrimary dark:text-textDarkPrimary hover:text-rose-600 dark:hover:text-rose-400 border border-borderSlate dark:border-darkBorder text-[10px] cursor-pointer">
                Dossier &rarr;
              </button>
            </td>
          </tr>
        `;
      }).join('');
    }

    function renderGridLinesTable() {
      const tbody = document.getElementById('gridLinesTableBody');
      if (!tbody) return;

      const q = (document.getElementById('gridLineSearchInput')?.value || '').toLowerCase().trim();
      const vFilter = selectedGridVoltage;

      const list = ALL_GRID_LINES.filter(l => {
        if (vFilter !== 'ALL' && String(l.v_kv) !== String(vFilter)) return false;
        if (q) {
          const matchS1 = (l.s1_name || l.s1_id || '').toLowerCase().includes(q);
          const matchS2 = (l.s2_name || l.s2_id || '').toLowerCase().includes(q);
          const matchCond = (l.conductor || '').toLowerCase().includes(q);
          if (!matchS1 && !matchS2 && !matchCond) return false;
        }
        return true;
      });

      const badge = document.getElementById('gridLineCountBadge');
      if (badge) badge.textContent = `Showing ${list.length.toLocaleString()} of ${ALL_GRID_LINES.length.toLocaleString()} Circuits`;

      tbody.innerHTML = list.slice(0, 100).map(l => {
        const vBadgeColor = l.v_kv === 500 
          ? 'bg-rose-500/10 text-rose-600 border-rose-500/20' 
          : (l.v_kv === 220 ? 'bg-amber-500/10 text-amber-600 border-amber-500/20' : 'bg-sky-500/10 text-sky-600 border-sky-500/20');

        return `
          <tr class="hover:bg-slate-50/80 dark:hover:bg-darkCard/50 transition-colors">
            <td class="p-2.5 font-semibold text-inkPrimary dark:text-textDarkPrimary">
              <span>${l.s1_name || l.s1_id}</span>
              <span class="text-slate-400 mx-1">&rarr;</span>
              <span>${l.s2_name || l.s2_id}</span>
            </td>
            <td class="p-2.5 text-center">
              <span class="px-2 py-0.5 rounded text-[10px] font-bold border ${vBadgeColor}">
                ${l.v_kv} kV
              </span>
            </td>
            <td class="p-2.5 text-inkMuted dark:text-textDarkMuted">${l.conductor || 'Standard ACSR'}</td>
            <td class="p-2.5 text-right font-mono">${l.r !== null ? l.r : '-'}</td>
            <td class="p-2.5 text-right font-mono">${l.x !== null ? l.x : '-'}</td>
            <td class="p-2.5 text-right font-bold text-inkPrimary dark:text-textDarkPrimary">${l.len_km} km</td>
          </tr>
        `;
      }).join('');
    }

    function openSubstationModal(subId) {
      const s = ALL_GRID_SUBSTATIONS.find(x => x.id === subId);
      if (!s) return;

      const overlay = document.getElementById('substationModalOverlay');
      if (!overlay) return;

      document.getElementById('substationModalName').textContent = s.name;
      document.getElementById('substationModalPlace').textContent = s.place || 'National Grid Vietnam';
      document.getElementById('substationModalVoltageBadge').textContent = `${s.voltages.join('/')} kV Substation`;
      document.getElementById('substationModalTx').textContent = s.tx_count > 0 ? `${s.tx_count} Transformers (${s.total_tx_mva} MVA)` : 'None Recorded';
      document.getElementById('substationModalGen').textContent = s.gen_count > 0 ? `${s.gen_count} Generation Units (${s.total_gen_mw} MW)` : 'No Generation Units';
      document.getElementById('substationModalBays').textContent = s.bay_codes || 'Standard Feeder Bays';
      document.getElementById('substationModalCoords').textContent = (s.lat && s.lng) ? `Lat: ${s.lat}, Lng: ${s.lng} (WGS84)` : 'Coordinates Unmapped';

      const gmapsLink = document.getElementById('substationModalGmapsLink');
      if (gmapsLink) {
        gmapsLink.href = (s.lat && s.lng) 
          ? `https://maps.google.com/maps?t=k&q=loc:${s.lat},${s.lng}&gl=vn&hl=vi`
          : `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(s.name + ' TBA Vietnam')}`;
      }

      overlay.classList.remove('hidden');
    }
"""

    # Update switchDossierTab to handle 'grid'
    old_switch_tab = """    // 13. Tab View Switcher (Assets Dossier & PDP8 Priority Pipeline)
    function switchDossierTab(tabKey) {
      activeTab = tabKey;
      const tabAssets = document.getElementById('tabAssetsBtn');
      const tabPipeline = document.getElementById('tabPipelineBtn');
      
      const viewAssets = document.getElementById('viewAssetsDossier');
      const viewPipeline = document.getElementById('viewPipelineContainer');
      const filtersBox = document.getElementById('dossierFiltersContainer');
      const paginationBar = document.getElementById('dossierPaginationBar');

      [tabAssets, tabPipeline].forEach(btn => {
        if (!btn) return;
        btn.classList.remove('bg-teal-600', 'text-white', 'font-semibold');
        btn.classList.add('text-inkMuted', 'dark:text-textDarkMuted');
      });

      [viewAssets, viewPipeline].forEach(v => {
        if (v) v.classList.add('hidden');
      });

      if (tabKey === 'pipeline') {
        if (tabPipeline) {
          tabPipeline.classList.add('bg-teal-600', 'text-white', 'font-semibold');
          tabPipeline.classList.remove('text-inkMuted', 'dark:text-textDarkMuted');
        }
        if (viewPipeline) viewPipeline.classList.remove('hidden');
        if (filtersBox) filtersBox.classList.add('hidden');
        if (paginationBar) paginationBar.classList.add('hidden');
      } else {
        if (tabAssets) {
          tabAssets.classList.add('bg-teal-600', 'text-white', 'font-semibold');
          tabAssets.classList.remove('text-inkMuted', 'dark:text-textDarkMuted');
        }
        if (viewAssets) viewAssets.classList.remove('hidden');
        if (filtersBox) filtersBox.classList.remove('hidden');
        if (paginationBar) paginationBar.classList.remove('hidden');
      }
    }"""

    new_switch_tab = """    // 13. Tab View Switcher (Assets Dossier, PDP8 Priority & National Grid)
    function switchDossierTab(tabKey) {
      activeTab = tabKey;
      const tabAssets = document.getElementById('tabAssetsBtn');
      const tabPipeline = document.getElementById('tabPipelineBtn');
      const tabGrid = document.getElementById('tabGridBtn');
      
      const viewAssets = document.getElementById('viewAssetsDossier');
      const viewPipeline = document.getElementById('viewPipelineContainer');
      const viewGrid = document.getElementById('viewGridContainer');
      const filtersBox = document.getElementById('dossierFiltersContainer');
      const paginationBar = document.getElementById('dossierPaginationBar');

      [tabAssets, tabPipeline, tabGrid].forEach(btn => {
        if (!btn) return;
        btn.classList.remove('bg-teal-600', 'bg-rose-600', 'text-white', 'font-semibold');
        btn.classList.add('text-inkMuted', 'dark:text-textDarkMuted');
      });

      [viewAssets, viewPipeline, viewGrid].forEach(v => {
        if (v) v.classList.add('hidden');
      });

      if (tabKey === 'grid') {
        if (tabGrid) {
          tabGrid.classList.add('bg-rose-600', 'text-white', 'font-semibold');
          tabGrid.classList.remove('text-inkMuted', 'dark:text-textDarkMuted');
        }
        if (viewGrid) viewGrid.classList.remove('hidden');
        if (filtersBox) filtersBox.classList.add('hidden');
        if (paginationBar) paginationBar.classList.add('hidden');
        setTimeout(() => {
          initGridMap();
          if (gridMapInstance) gridMapInstance.invalidateSize();
        }, 120);
      } else if (tabKey === 'pipeline') {
        if (tabPipeline) {
          tabPipeline.classList.add('bg-teal-600', 'text-white', 'font-semibold');
          tabPipeline.classList.remove('text-inkMuted', 'dark:text-textDarkMuted');
        }
        if (viewPipeline) viewPipeline.classList.remove('hidden');
        if (filtersBox) filtersBox.classList.add('hidden');
        if (paginationBar) paginationBar.classList.add('hidden');
      } else {
        if (tabAssets) {
          tabAssets.classList.add('bg-teal-600', 'text-white', 'font-semibold');
          tabAssets.classList.remove('text-inkMuted', 'dark:text-textDarkMuted');
        }
        if (viewAssets) viewAssets.classList.remove('hidden');
        if (filtersBox) filtersBox.classList.remove('hidden');
        if (paginationBar) paginationBar.classList.remove('hidden');
      }
    }"""

    if old_switch_tab in html:
        html = html.replace(old_switch_tab, new_switch_tab, 1)

    # 7. Add Grid Event Listeners & initialization in DOMContentLoaded
    dom_content_marker = """      document.getElementById("tabAssetsBtn")?.addEventListener("click", () => switchDossierTab("assets"));\n      document.getElementById("tabPipelineBtn")?.addEventListener("click", () => switchDossierTab("pipeline"));"""
    dom_content_replacement = """      document.getElementById("tabAssetsBtn")?.addEventListener("click", () => switchDossierTab("assets"));
      document.getElementById("tabPipelineBtn")?.addEventListener("click", () => switchDossierTab("pipeline"));
      document.getElementById("tabGridBtn")?.addEventListener("click", () => switchDossierTab("grid"));

      // Grid Sub-View Switchers
      const subMapBtn = document.getElementById("gridSubViewMapBtn");
      const subSubsBtn = document.getElementById("gridSubViewSubstationsBtn");
      const subLinesBtn = document.getElementById("gridSubViewLinesBtn");

      const subMapView = document.getElementById("gridSubViewMap");
      const subSubsView = document.getElementById("gridSubViewSubstations");
      const subLinesView = document.getElementById("gridSubViewLines");

      function setGridSubView(viewKey) {
        [subMapBtn, subSubsBtn, subLinesBtn].forEach(b => {
          if (!b) return;
          b.classList.remove('bg-rose-600', 'text-white', 'font-semibold');
          b.classList.add('bg-white', 'dark:bg-darkSurface', 'border', 'border-borderSlate', 'dark:border-darkBorder', 'text-inkMuted', 'dark:text-textDarkMuted');
        });
        [subMapView, subSubsView, subLinesView].forEach(v => {
          if (v) v.classList.add('hidden');
        });

        if (viewKey === 'map') {
          subMapBtn?.classList.add('bg-rose-600', 'text-white', 'font-semibold');
          subMapBtn?.classList.remove('bg-white', 'dark:bg-darkSurface', 'border', 'text-inkMuted', 'dark:text-textDarkMuted');
          subMapView?.classList.remove('hidden');
          setTimeout(() => { if (gridMapInstance) gridMapInstance.invalidateSize(); }, 80);
        } else if (viewKey === 'substations') {
          subSubsBtn?.classList.add('bg-rose-600', 'text-white', 'font-semibold');
          subSubsBtn?.classList.remove('bg-white', 'dark:bg-darkSurface', 'border', 'text-inkMuted', 'dark:text-textDarkMuted');
          subSubsView?.classList.remove('hidden');
        } else if (viewKey === 'lines') {
          subLinesBtn?.classList.add('bg-rose-600', 'text-white', 'font-semibold');
          subLinesBtn?.classList.remove('bg-white', 'dark:bg-darkSurface', 'border', 'text-inkMuted', 'dark:text-textDarkMuted');
          subLinesView?.classList.remove('hidden');
        }
      }

      subMapBtn?.addEventListener('click', () => setGridSubView('map'));
      subSubsBtn?.addEventListener('click', () => setGridSubView('substations'));
      subLinesBtn?.addEventListener('click', () => setGridSubView('lines'));

      // Voltage Filter Pills
      document.querySelectorAll('.grid-v-pill').forEach(pill => {
        pill.addEventListener('click', () => {
          document.querySelectorAll('.grid-v-pill').forEach(p => {
            p.classList.remove('bg-rose-600', 'text-white', 'font-semibold');
            p.classList.add('bg-white', 'dark:bg-darkSurface', 'border');
          });
          pill.classList.add('bg-rose-600', 'text-white', 'font-semibold');
          pill.classList.remove('bg-white', 'dark:bg-darkSurface', 'border');
          selectedGridVoltage = pill.getAttribute('data-v');
          renderGridMapVectors();
          renderGridSubstationsTable();
          renderGridLinesTable();
        });
      });

      // Substation Search Input
      document.getElementById('gridSubstationSearchInput')?.addEventListener('input', () => {
        renderGridSubstationsTable();
      });

      // Line Search Input
      document.getElementById('gridLineSearchInput')?.addEventListener('input', () => {
        renderGridLinesTable();
      });

      // Close Substation Modal
      const closeSubModalBtn = document.getElementById('closeSubstationModalBtn');
      const subModalOverlay = document.getElementById('substationModalOverlay');
      if (closeSubModalBtn && subModalOverlay) {
        closeSubModalBtn.addEventListener('click', () => subModalOverlay.classList.add('hidden'));
        subModalOverlay.addEventListener('click', (e) => {
          if (e.target === subModalOverlay) subModalOverlay.classList.add('hidden');
        });
      }

      // Trigger grid data load
      loadGridData();"""

    if dom_content_marker in html:
        html = html.replace(dom_content_marker, dom_content_replacement, 1)

    # Append grid_js_code right before </script> of the main script
    html = html.replace('// 15C. Bi-Directional Sector Filtering Logic (Table -> GIS Map & Dossier)', f'{grid_js_code}\n\n    // 15C. Bi-Directional Sector Filtering Logic (Table -> GIS Map & Dossier)', 1)

    with open(TARGET_HTML, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Successfully generated {TARGET_HTML} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_revision()
