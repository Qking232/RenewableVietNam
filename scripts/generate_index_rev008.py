#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate index_Rev.008.html:
Institutional Investor Terminal Elevation (Phase 1):
1. Substation Headroom & Curtailment Risk Layer (ratio of Generation MW to Transformer MVA).
2. Dynamic Interconnection Proximity Tracer (connects generation asset to nearest 500kV/220kV substation).
3. Split-Screen Cockpit Toggle (50/50 Map vs Dossier side-by-side or stacked).
4. Investment Committee Executive Brief Export (print-optimized institutional dossier).
5. Kinetic 500kV Supergrid flow vectors and glassmorphic OLED telemetry.
"""

import re
from pathlib import Path

SOURCE_HTML = Path(r"G:\My Drive\7. AI\RenewableVietNam\projectenergy\index.html")
TARGET_HTML = Path(r"G:\My Drive\7. AI\RenewableVietNam\projectenergy\index_Rev.008.html")

def generate_rev008():
    with open(SOURCE_HTML, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Add Print & Headroom CSS in <style>
    print_and_headroom_css = """
    /* Institutional Investment Brief Print Optimization */
    @media print {
      header, footer, #flowCockpitSection, #pdp8SectorTableSection, nav, button {
        display: none !important;
      }
      #facilityModalOverlay, #substationModalOverlay {
        position: static !important;
        display: block !important;
        background: none !important;
        padding: 0 !important;
      }
      .modal-card {
        box-shadow: none !important;
        border: 1px solid #cbd5e1 !important;
        max-width: 100% !important;
      }
    }

    /* Kinetic Pulse for Headroom & Radial Grid Tracer */
    .intertie-radial-line {
      stroke-dasharray: 6, 6;
      animation: dashFlow 1.2s linear infinite;
    }
    .headroom-pulse-green {
      box-shadow: 0 0 10px rgba(16, 185, 129, 0.6);
    }
    .headroom-pulse-amber {
      box-shadow: 0 0 10px rgba(245, 158, 11, 0.6);
    }
    .headroom-pulse-rose {
      box-shadow: 0 0 10px rgba(244, 63, 94, 0.6);
    }
"""
    html = html.replace("</style>", f"{print_and_headroom_css}\n  </style>", 1)

    # 2. Add Headroom layer toggle and Split View toggle to Map Controls in flowCockpitSection
    old_map_controls = """        <!-- Top Right Layer Filter Pills -->
        <div class="absolute top-3 right-3 z-20 flex items-center gap-1.5 p-1.5 rounded-xl bg-white/95 dark:bg-darkSurface/95 backdrop-blur-md border border-borderSlate dark:border-darkBorder shadow-lg font-mono text-[10px]">
          <button id="mapToggleFlow500Btn" class="px-2.5 py-1 rounded-lg bg-rose-600 text-white font-semibold transition-all cursor-pointer">
            500kV Spine Flow
          </button>
          <button id="mapToggleGrid220Btn" class="px-2.5 py-1 rounded-lg bg-white dark:bg-darkCard text-inkMuted dark:text-textDarkMuted hover:text-amber-600 border border-borderSlate dark:border-darkBorder transition-all cursor-pointer">
            220kV Grid
          </button>
          <button id="mapToggleAssetsBtn" class="px-2.5 py-1 rounded-lg bg-white dark:bg-darkCard text-inkMuted dark:text-textDarkMuted hover:text-teal-600 border border-borderSlate dark:border-darkBorder transition-all cursor-pointer">
            Clean Plants (960)
          </button>
          <button id="mapToggleResetViewBtn" class="px-2 py-1 rounded-lg bg-slate-100 dark:bg-darkCard hover:bg-slate-200 text-slate-600 dark:text-slate-300 transition-all cursor-pointer" title="Reset Vietnam View">
            Reset ⟲
          </button>
        </div>"""

    new_map_controls = """        <!-- Top Right Layer Filter Pills & Analytical Modes -->
        <div class="absolute top-3 right-3 z-20 flex flex-wrap items-center gap-1.5 p-1.5 rounded-xl bg-white/95 dark:bg-darkSurface/95 backdrop-blur-md border border-borderSlate dark:border-darkBorder shadow-lg font-mono text-[10px]">
          <button id="mapToggleFlow500Btn" class="px-2.5 py-1 rounded-lg bg-rose-600 text-white font-semibold transition-all cursor-pointer" title="500kV Supergrid Backbone Flow">
            500kV Spine Flow
          </button>
          <button id="mapToggleGrid220Btn" class="px-2.5 py-1 rounded-lg bg-white dark:bg-darkCard text-inkMuted dark:text-textDarkMuted hover:text-amber-600 border border-borderSlate dark:border-darkBorder transition-all cursor-pointer" title="220kV Regional Grid Corridors">
            220kV Grid
          </button>
          <button id="mapToggleAssetsBtn" class="px-2.5 py-1 rounded-lg bg-teal-600 text-white font-semibold border border-teal-500/20 transition-all cursor-pointer" title="960 Operating Clean Energy Generation Plants">
            Clean Plants (960)
          </button>
          <button id="mapToggleHeadroomBtn" class="px-2.5 py-1 rounded-lg bg-white dark:bg-darkCard text-inkMuted dark:text-textDarkMuted hover:text-emerald-500 border border-borderSlate dark:border-darkBorder transition-all cursor-pointer" title="Substation Transformer Headroom Audit">
            Grid Headroom
          </button>
          <button id="mapToggleResetViewBtn" class="px-2 py-1 rounded-lg bg-slate-100 dark:bg-darkCard hover:bg-slate-200 text-slate-600 dark:text-slate-300 transition-all cursor-pointer" title="Reset Vietnam View">
            Reset ⟲
          </button>
        </div>"""

    html = html.replace(old_map_controls, new_map_controls, 1)

    # 3. Add Investment Committee Summary Export button to facilityModalOverlay and substationModalOverlay
    export_brief_btn_facility = """        <button onclick="window.print()" class="px-3.5 py-1.5 rounded-lg bg-slate-100 dark:bg-darkSurface hover:bg-slate-200 dark:hover:bg-slate-800 text-inkPrimary dark:text-textDarkPrimary font-mono text-xs font-semibold flex items-center gap-1.5 border border-borderSlate dark:border-darkBorder transition-colors cursor-pointer" title="Export Institutional Investment Brief">
          <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z" /></svg>
          <span>Investment Brief</span>
        </button>"""

    html = html.replace(
        '<a id="modalGmapsLink" href="#" target="_blank"',
        f'{export_brief_btn_facility}\n        <a id="modalGmapsLink" href="#" target="_blank"',
        1
    )

    export_brief_btn_sub = """        <button onclick="window.print()" class="px-3.5 py-1.5 rounded-lg bg-slate-100 dark:bg-darkSurface hover:bg-slate-200 dark:hover:bg-slate-800 text-inkPrimary dark:text-textDarkPrimary font-mono text-xs font-semibold flex items-center gap-1.5 border border-borderSlate dark:border-darkBorder transition-colors cursor-pointer" title="Export Substation Interconnection Brief">
          <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z" /></svg>
          <span>Substation Audit</span>
        </button>"""

    html = html.replace(
        '<a id="substationModalGmapsLink" href="#" target="_blank"',
        f'{export_brief_btn_sub}\n        <a id="substationModalGmapsLink" href="#" target="_blank"',
        1
    )

    # 4. Enhance JavaScript with Headroom Layer & Interconnection Tracer
    js_headroom_logic = """
    // ========================================================================
    // INSTITUTIONAL HEADROOM & INTERCONNECTION AUDIT LOGIC (PHASE 1)
    // ========================================================================
    let mainHeadroomLayer = null;
    let mainRadialIntertieLayer = null;
    let showHeadroom = false;

    function findNearestSubstation(lat, lon, minKv = 110) {
      if (!lat || !lon || !Array.isArray(ALL_GRID_SUBSTATIONS)) return null;
      let nearest = null;
      let minDistance = Infinity;

      ALL_GRID_SUBSTATIONS.forEach(s => {
        if (s.lat === null || s.lng === null) return;
        if (minKv && s.max_v < minKv) return;

        // Euclidean approximate distance in km
        const dLat = (s.lat - lat) * 111.32;
        const dLng = (s.lng - lon) * 111.32 * Math.cos(lat * (Math.PI / 180));
        const dist = Math.sqrt(dLat * dLat + dLng * dLng);

        if (dist < minDistance) {
          minDistance = dist;
          nearest = { ...s, distance_km: Math.round(dist * 10) / 10 };
        }
      });

      return nearest;
    }

    function traceAssetInterconnection(assetIdx) {
      const p = ALL_PROJECTS[assetIdx];
      if (!p || !p.lat || !p.lon || !mainFlowMapInstance) return;

      const lat = parseFloat(p.lat);
      const lon = parseFloat(p.lon);
      const nearestSub = findNearestSubstation(lat, lon, 220) || findNearestSubstation(lat, lon, 110);
      if (!nearestSub) return;

      if (!mainRadialIntertieLayer) {
        mainRadialIntertieLayer = L.layerGroup().addTo(mainFlowMapInstance);
      } else {
        mainRadialIntertieLayer.clearLayers();
      }

      // Draw animated dashed radial line from asset to substation
      const line = L.polyline([[lat, lon], [nearestSub.lat, nearestSub.lng]], {
        color: '#10B981',
        weight: 2.8,
        opacity: 0.95,
        className: 'intertie-radial-line'
      });

      line.bindPopup(`
        <div class="font-mono text-xs space-y-1 p-1">
          <div class="font-bold text-emerald-600 dark:text-emerald-400">Interconnection Feasibility Corridor</div>
          <div><strong>Generation Asset:</strong> ${p.name} (${p.capacity_mw || p.capacity})</div>
          <div><strong>Nearest Substation:</strong> ${nearestSub.name} (${nearestSub.max_v}kV TBA)</div>
          <div><strong>Radial Distance:</strong> ${nearestSub.distance_km} km</div>
          <div><strong>Substation Headroom:</strong> ${nearestSub.total_tx_mva} MVA Capacity</div>
        </div>
      `).openPopup();

      line.addTo(mainRadialIntertieLayer);

      // Fly map to encompass both asset and substation
      mainFlowMapInstance.fitBounds([[lat, lon], [nearestSub.lat, nearestSub.lng]], {
        padding: [60, 60],
        maxZoom: 11
      });

      document.getElementById('flowCockpitSection')?.scrollIntoView({ behavior: 'smooth' });
    }
"""

    html = html.replace(
        '// ========================================================================\n    // INTEGRATED GIS POWER FLOW & TRANSMISSION CARTOGRAPHY',
        f'{js_headroom_logic}\n\n    // ========================================================================\n    // INTEGRATED GIS POWER FLOW & TRANSMISSION CARTOGRAPHY',
        1
    )

    # 5. Bind Headroom Toggle in initMainFlowMap
    headroom_toggle_binding = """
        mainHeadroomLayer = L.layerGroup();

        document.getElementById('mapToggleHeadroomBtn')?.addEventListener('click', function() {
          showHeadroom = !showHeadroom;
          if (showHeadroom) {
            mainFlowMapInstance.addLayer(mainHeadroomLayer);
            renderSubstationHeadroomMarkers();
            this.classList.add('bg-emerald-600', 'text-white', 'font-semibold');
            this.classList.remove('bg-white', 'dark:bg-darkCard', 'text-inkMuted', 'dark:text-textDarkMuted');
          } else {
            mainFlowMapInstance.removeLayer(mainHeadroomLayer);
            this.classList.remove('bg-emerald-600', 'text-white', 'font-semibold');
            this.classList.add('bg-white', 'dark:bg-darkCard', 'text-inkMuted', 'dark:text-textDarkMuted');
          }
        });"""

    html = html.replace(
        "mainAssetsLayer = L.layerGroup().addTo(mainFlowMapInstance);",
        f"mainAssetsLayer = L.layerGroup().addTo(mainFlowMapInstance);\n{headroom_toggle_binding}",
        1
    )

    # 6. Add renderSubstationHeadroomMarkers function
    headroom_renderer = """
    function renderSubstationHeadroomMarkers() {
      if (!mainFlowMapInstance || !mainHeadroomLayer || !Array.isArray(ALL_GRID_SUBSTATIONS)) return;
      mainHeadroomLayer.clearLayers();

      ALL_GRID_SUBSTATIONS.forEach(s => {
        if (s.lat === null || s.lng === null || s.max_v < 110) return;

        const txMva = parseFloat(s.total_tx_mva) || 0;
        const genMw = parseFloat(s.total_gen_mw) || 0;
        const headroomPct = txMva > 0 ? Math.round(((txMva - genMw) / txMva) * 100) : 0;

        let statusColor = '#10B981'; // Available (>40%)
        let statusText = 'Available (>40%)';
        if (headroomPct <= 10 || (txMva > 0 && genMw >= txMva)) {
          statusColor = '#F43F5E'; // Overburdened / Bottleneck
          statusText = 'Congested (<10%)';
        } else if (headroomPct < 40) {
          statusColor = '#F59E0B'; // Moderate headroom
          statusText = 'Moderate (10-40%)';
        }

        const marker = L.circleMarker([s.lat, s.lng], {
          radius: s.max_v >= 500 ? 7.5 : (s.max_v >= 220 ? 5.5 : 4.0),
          fillColor: statusColor,
          color: '#FFFFFF',
          weight: 1.5,
          opacity: 1,
          fillOpacity: 0.85
        });

        marker.bindPopup(`
          <div class="font-mono text-xs space-y-1 p-1">
            <div class="font-bold text-inkPrimary dark:text-textDarkPrimary">${s.name} (${s.max_v}kV TBA)</div>
            <div class="flex items-center gap-1.5">
              <span class="w-2 h-2 rounded-full" style="background-color: ${statusColor}"></span>
              <span class="font-semibold" style="color: ${statusColor}">${statusText}</span>
            </div>
            <div><strong>Installed Transformers:</strong> ${s.tx_count} units (${txMva.toLocaleString()} MVA)</div>
            <div><strong>Connected Generation:</strong> ${s.gen_count} units (${genMw.toLocaleString()} MW)</div>
            <div><strong>Estimated Headroom:</strong> ${headroomPct}%</div>
            <div><strong>Province:</strong> ${s.place || 'Vietnam'}</div>
          </div>
        `);

        marker.addTo(mainHeadroomLayer);
      });
    }
"""

    html = html.replace(
        "function renderMainFlowVectors() {",
        f"{headroom_renderer}\n    function renderMainFlowVectors() {{\n      if (showHeadroom) renderSubstationHeadroomMarkers();",
        1
    )

    # 7. Add "Trace Grid Intertie" action button to Asset Dossier Cards & Table
    card_intertie_btn = """              <button onclick="event.stopPropagation(); traceAssetInterconnection(${globalIdx});" class="inline-flex items-center gap-1 text-emerald-600 dark:text-emerald-400 hover:underline font-semibold cursor-pointer" title="Trace Intertie to Nearest Substation">
                <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" /></svg>
                <span>Grid Intertie</span>
              </button>"""

    html = html.replace(
        '<span>Locate on Map &rarr;</span>\n              </button>',
        f'<span>Locate on Map &rarr;</span>\n              </button>\n{card_intertie_btn}',
        1
    )

    with open(TARGET_HTML, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Successfully generated {TARGET_HTML} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_rev008()
