#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate index_Rev.010.html:
Redesign National Electrical Transmission Spine into a Side-by-Side Dual-Column Workstation:
1. Replace single-column map container with responsive dual-column grid (lg:col-span-8 map, lg:col-span-4 inspection panel).
2. Create persistent #nodeInspectionPanel that updates in real time on node clicks without any blocking modal.
3. Wire selectGridSubstation, resetNodeInspectionPanel, selectCleanPlant, and quickSelectHub handlers.
4. Route openSubstationModal directly to selectGridSubstation so all map and table events update the side panel.
"""

from pathlib import Path
import re

SOURCE_HTML = Path(r"G:\My Drive\7. AI\RenewableVietNam\projectenergy\index_Rev.009.html")
TARGET_REV = Path(r"G:\My Drive\7. AI\RenewableVietNam\projectenergy\index_Rev.010.html")

def generate():
    with open(SOURCE_HTML, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Replace the Map Container with the Side-by-Side Grid
    old_map_container = """      <!-- Main Leaflet Flow Map Container -->
      <div class="relative w-full h-[460px] sm:h-[520px] rounded-xl border border-borderSlate dark:border-darkBorder overflow-hidden shadow-inner bg-slate-950">
        <div id="mainEnergyFlowMap" class="w-full h-full z-10"></div>

        <!-- Top Right Layer Filter Pills & Analytical Modes -->
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
        </div>

        <!-- Bottom Left Interactive Flow Telemetry Legend -->
        <div class="absolute bottom-3 left-3 z-20 p-3 rounded-xl bg-white/95 dark:bg-darkSurface/95 backdrop-blur-md border border-borderSlate dark:border-darkBorder shadow-lg font-mono text-[10px] space-y-1.5 max-w-xs">
          <div class="font-bold text-inkPrimary dark:text-textDarkPrimary uppercase tracking-wider text-[11px] flex items-center justify-between">
            <span>Transmission Corridor Flow</span>
            <span class="w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span>
          </div>
          <div class="flex items-center gap-2">
            <span class="w-4 h-1 rounded-full bg-rose-500 shadow-sm"></span>
            <span class="text-inkPrimary dark:text-textDarkPrimary font-semibold">500kV North-South Spine (Directional Flow)</span>
          </div>
          <div class="flex items-center gap-2">
            <span class="w-4 h-1 rounded-full bg-amber-500"></span>
            <span class="text-inkPrimary dark:text-textDarkPrimary">220kV Intertie Regional Corridors</span>
          </div>
          <div class="flex items-center gap-2">
            <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 border border-white"></span>
            <span class="text-inkPrimary dark:text-textDarkPrimary">Operational Generation Plants (Solar/Wind/Hydro)</span>
          </div>
          <div class="pt-1.5 border-t border-borderSlate/60 dark:border-darkBorder/60 flex items-center justify-between text-[9px] text-slate-400">
            <span>Model: NSMO Vietnam 2025</span>
            <span>65,566 km Circuits</span>
          </div>
        </div>
      </div>"""

    new_map_container = """      <!-- SIDE-BY-SIDE TRANSMISSION MAP & NODE TELEMETRY WORKSTATION -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-4 items-stretch">
        
        <!-- Left: Sovereign Vector Map (lg:col-span-8) -->
        <div class="lg:col-span-8 relative h-[560px] sm:h-[620px] rounded-2xl border border-borderSlate dark:border-darkBorder overflow-hidden shadow-sm bg-slate-950 flex flex-col">
          <div id="mainEnergyFlowMap" class="w-full h-full z-10"></div>

          <!-- Top Right Layer Filter Pills & Analytical Modes -->
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
          </div>

          <!-- Bottom Left Interactive Flow Telemetry Legend -->
          <div class="absolute bottom-3 left-3 z-20 p-3 rounded-xl bg-white/95 dark:bg-darkSurface/95 backdrop-blur-md border border-borderSlate dark:border-darkBorder shadow-lg font-mono text-[10px] space-y-1.5 max-w-xs">
            <div class="font-bold text-inkPrimary dark:text-textDarkPrimary uppercase tracking-wider text-[11px] flex items-center justify-between">
              <span>Transmission Corridor Flow</span>
              <span class="w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span>
            </div>
            <div class="flex items-center gap-2">
              <span class="w-4 h-1 rounded-full bg-rose-500 shadow-sm"></span>
              <span class="text-inkPrimary dark:text-textDarkPrimary font-semibold">500kV North-South Spine</span>
            </div>
            <div class="flex items-center gap-2">
              <span class="w-4 h-1 rounded-full bg-amber-500"></span>
              <span class="text-inkPrimary dark:text-textDarkPrimary">220kV Intertie Regional Corridors</span>
            </div>
            <div class="flex items-center gap-2">
              <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 border border-white"></span>
              <span class="text-inkPrimary dark:text-textDarkPrimary">Operational Generation Plants (960)</span>
            </div>
            <div class="pt-1.5 border-t border-borderSlate/60 dark:border-darkBorder/60 flex items-center justify-between text-[9px] text-slate-400">
              <span>Model: NSMO Vietnam 2025</span>
              <span>65,566 km Circuits</span>
            </div>
          </div>
        </div>

        <!-- Right: Node Telemetry & Substation Inspection Dossier (lg:col-span-4) -->
        <div id="nodeInspectionContainer" class="lg:col-span-4 h-[560px] sm:h-[620px] flex flex-col rounded-2xl border border-borderSlate dark:border-darkBorder bg-white dark:bg-darkSurface shadow-sm overflow-hidden">
          <!-- Dynamic Dossier Header -->
          <div class="p-3.5 border-b border-borderSlate dark:border-darkBorder bg-slate-50/70 dark:bg-darkCard/50 flex items-center justify-between shrink-0">
            <div class="flex items-center gap-2">
              <span class="w-2.5 h-2.5 rounded-full bg-rose-500 animate-pulse"></span>
              <h3 class="font-mono text-xs font-bold uppercase tracking-wider text-inkPrimary dark:text-textDarkPrimary">Node Telemetry Dossier</h3>
            </div>
            <div class="flex items-center gap-1.5">
              <span id="nodeStatusPill" class="px-2 py-0.5 rounded text-[10px] font-mono font-semibold bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-300">National Overview</span>
              <button id="resetNodePanelBtn" onclick="resetNodeInspectionPanel()" class="p-1 rounded text-slate-400 hover:text-rose-600 dark:hover:text-rose-400 transition-colors hidden cursor-pointer" title="Reset to National Overview">
                <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" /></svg>
              </button>
            </div>
          </div>

          <!-- Dynamic Dossier Body Content -->
          <div id="nodePanelContent" class="flex-1 p-4 overflow-y-auto space-y-4 font-mono text-xs">
            <!-- Populated via resetNodeInspectionPanel() on DOM load -->
          </div>
        </div>

      </div>"""

    assert old_map_container in html, "Failed to find old map container in source HTML"
    html = html.replace(old_map_container, new_map_container, 1)

    # 2. Add Node Inspection Dossier JavaScript logic
    side_by_side_js = """
    // ========================================================================
    // SIDE-BY-SIDE NODE TELEMETRY DOSSIER & GIS WORKSTATION LOGIC
    // ========================================================================
    let ACTIVE_SELECTED_SUBSTATION_ID = null;

    function resetNodeInspectionPanel() {
      ACTIVE_SELECTED_SUBSTATION_ID = null;
      const panel = document.getElementById('nodePanelContent');
      const statusPill = document.getElementById('nodeStatusPill');
      const resetBtn = document.getElementById('resetNodePanelBtn');
      if (!panel) return;

      if (statusPill) {
        statusPill.textContent = 'National Overview';
        statusPill.className = 'px-2 py-0.5 rounded text-[10px] font-mono font-semibold bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-300';
      }
      if (resetBtn) resetBtn.classList.add('hidden');

      panel.innerHTML = `
        <div class="p-3 rounded-xl bg-teal-50 dark:bg-teal-950/30 border border-teal-200 dark:border-teal-800/40 text-teal-800 dark:text-teal-300 space-y-1">
          <div class="font-bold flex items-center gap-1.5">
            <span class="w-2 h-2 rounded-full bg-teal-500"></span>
            <span>Interactive Grid Workstation</span>
          </div>
          <p class="text-[11px] text-teal-700/80 dark:text-teal-400">
            Click any substation, 500kV corridor, or clean power plant on the map to inspect its real-time telemetry side by side with the topology.
          </p>
        </div>

        <div class="space-y-2">
          <span class="text-slate-400 text-[10px] uppercase font-bold tracking-wider">National Grid Telemetry</span>
          <div class="grid grid-cols-2 gap-2">
            <div class="p-2.5 rounded-lg bg-slate-50 dark:bg-darkCard border border-borderSlate dark:border-darkBorder space-y-0.5">
              <span class="text-slate-400 text-[10px] uppercase">Total Substations</span>
              <div class="text-sm font-bold text-inkPrimary dark:text-textDarkPrimary">1,915 Units</div>
            </div>
            <div class="p-2.5 rounded-lg bg-slate-50 dark:bg-darkCard border border-borderSlate dark:border-darkBorder space-y-0.5">
              <span class="text-slate-400 text-[10px] uppercase">Clean Facilities</span>
              <div class="text-sm font-bold text-teal-600 dark:text-teal-400">960 Monitored</div>
            </div>
            <div class="p-2.5 rounded-lg bg-slate-50 dark:bg-darkCard border border-borderSlate dark:border-darkBorder space-y-0.5">
              <span class="text-slate-400 text-[10px] uppercase">500kV Backbone</span>
              <div class="text-sm font-bold text-rose-600 dark:text-rose-400">15,888 km</div>
            </div>
            <div class="p-2.5 rounded-lg bg-slate-50 dark:bg-darkCard border border-borderSlate dark:border-darkBorder space-y-0.5">
              <span class="text-slate-400 text-[10px] uppercase">220kV Grid</span>
              <div class="text-sm font-bold text-amber-600 dark:text-amber-400">27,007 km</div>
            </div>
          </div>
        </div>

        <div class="space-y-2">
          <span class="text-slate-400 text-[10px] uppercase font-bold tracking-wider">Strategic 500kV Intertie Hubs</span>
          <div class="flex flex-wrap gap-1.5" id="strategicHubPills">
            <button onclick="quickSelectHub('DỐC SỎI')" class="px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-darkCard hover:bg-rose-600 hover:text-white border border-borderSlate dark:border-darkBorder transition-colors cursor-pointer text-[11px] font-semibold">Dốc Sỏi</button>
            <button onclick="quickSelectHub('PLEIKU')" class="px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-darkCard hover:bg-rose-600 hover:text-white border border-borderSlate dark:border-darkBorder transition-colors cursor-pointer text-[11px] font-semibold">Pleiku</button>
            <button onclick="quickSelectHub('PHỐ NỐI')" class="px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-darkCard hover:bg-rose-600 hover:text-white border border-borderSlate dark:border-darkBorder transition-colors cursor-pointer text-[11px] font-semibold">Phố Nối</button>
            <button onclick="quickSelectHub('ĐÀ NẴNG')" class="px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-darkCard hover:bg-rose-600 hover:text-white border border-borderSlate dark:border-darkBorder transition-colors cursor-pointer text-[11px] font-semibold">Đà Nẵng</button>
            <button onclick="quickSelectHub('CẦU BÔNG')" class="px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-darkCard hover:bg-rose-600 hover:text-white border border-borderSlate dark:border-darkBorder transition-colors cursor-pointer text-[11px] font-semibold">Cầu Bông</button>
            <button onclick="quickSelectHub('HIỆP HÒA')" class="px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-darkCard hover:bg-rose-600 hover:text-white border border-borderSlate dark:border-darkBorder transition-colors cursor-pointer text-[11px] font-semibold">Hiệp Hòa</button>
          </div>
        </div>

        <div class="p-3 rounded-lg bg-slate-50 dark:bg-darkCard border border-borderSlate dark:border-darkBorder space-y-1">
          <span class="text-slate-400 text-[10px] uppercase">Institutional Sovereign Cartography</span>
          <p class="text-[11px] text-slate-500 dark:text-slate-400">
            Rendered with zero third-party raster tiles. Integrates mainland frontiers, Quần đảo Hoàng Sa (TP. Đà Nẵng), and Quần đảo Trường Sa (Tỉnh Khánh Hòa).
          </p>
        </div>
      `;
    }

    function selectGridSubstation(subId, zoomTo = true) {
      const s = ALL_GRID_SUBSTATIONS.find(x => x.id === subId);
      if (!s) return;
      ACTIVE_SELECTED_SUBSTATION_ID = subId;

      const panel = document.getElementById('nodePanelContent');
      const statusPill = document.getElementById('nodeStatusPill');
      const resetBtn = document.getElementById('resetNodePanelBtn');
      if (!panel) return;

      if (statusPill) {
        statusPill.textContent = 'Live Inspection';
        statusPill.className = 'px-2 py-0.5 rounded text-[10px] font-mono font-bold uppercase bg-rose-500/10 text-rose-600 border border-rose-500/20';
      }
      if (resetBtn) resetBtn.classList.remove('hidden');

      const txMva = s.total_tx_mva || 0;
      const genMw = s.total_gen_mw || 0;
      const headroomEstimate = Math.max(0, txMva - genMw);
      const headroomBadge = txMva > 0 
        ? (headroomEstimate > 500 
            ? '<span class="text-emerald-500 font-bold">High Headroom (~' + headroomEstimate.toLocaleString() + ' MVA)</span>'
            : '<span class="text-amber-500 font-bold">Moderate Headroom (~' + headroomEstimate.toLocaleString() + ' MVA)</span>')
        : '<span class="text-slate-400 font-semibold">Not Applicable</span>';

      const gmapsUrl = (s.lat && s.lng) 
        ? `https://maps.google.com/maps?t=k&q=loc:${s.lat},${s.lng}&gl=vn&hl=vi`
        : `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(s.name + ' TBA Vietnam')}`;

      panel.innerHTML = `
        <div class="space-y-1.5 pb-3 border-b border-borderSlate dark:border-darkBorder">
          <span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold uppercase bg-rose-500/10 text-rose-600 border border-rose-500/20">
            ${s.voltages.join('/')} kV Substation
          </span>
          <h4 class="text-lg font-bold text-inkPrimary dark:text-textDarkPrimary">${s.name}</h4>
          <p class="text-xs text-inkMuted dark:text-textDarkMuted">${s.place || 'National Grid Vietnam'}</p>
        </div>

        <div class="grid grid-cols-2 gap-2">
          <div class="p-2.5 rounded-lg bg-slate-50 dark:bg-darkCard border border-borderSlate dark:border-darkBorder space-y-0.5">
            <span class="text-slate-400 text-[10px] uppercase">Installed Transformers</span>
            <div class="text-sm font-bold text-inkPrimary dark:text-textDarkPrimary">${s.tx_count > 0 ? s.tx_count + ' Units (' + s.total_tx_mva.toLocaleString() + ' MVA)' : 'None Recorded'}</div>
          </div>
          <div class="p-2.5 rounded-lg bg-slate-50 dark:bg-darkCard border border-borderSlate dark:border-darkBorder space-y-0.5">
            <span class="text-slate-400 text-[10px] uppercase">Connected Generation</span>
            <div class="text-sm font-bold text-rose-600 dark:text-rose-400">${s.gen_count > 0 ? s.gen_count + ' Units (' + s.total_gen_mw.toLocaleString() + ' MW)' : 'No Generation Units'}</div>
          </div>
        </div>

        <div class="p-2.5 rounded-lg bg-slate-50 dark:bg-darkCard border border-borderSlate dark:border-darkBorder space-y-1">
          <span class="text-slate-400 text-[10px] uppercase">Transformer Intertie Headroom</span>
          <div class="text-xs">${headroomBadge}</div>
        </div>

        <div class="p-2.5 rounded-lg bg-slate-50 dark:bg-darkCard border border-borderSlate dark:border-darkBorder space-y-1">
          <span class="text-slate-400 text-[10px] uppercase">Substation Bay Codes &amp; Feeders</span>
          <div class="text-[11px] text-inkPrimary dark:text-textDarkPrimary max-h-24 overflow-y-auto break-all font-mono">${s.bay_codes || 'Standard Feeder Bays'}</div>
        </div>

        <div class="p-2.5 rounded-lg bg-slate-50 dark:bg-darkCard border border-borderSlate dark:border-darkBorder space-y-1">
          <span class="text-slate-400 text-[10px] uppercase">Geospatial Telemetry (WGS84)</span>
          <div class="text-xs text-inkMuted dark:text-textDarkMuted">${(s.lat && s.lng) ? 'Lat: ' + s.lat + ', Lng: ' + s.lng : 'Coordinates Unmapped'}</div>
        </div>

        <div class="pt-2 flex items-center gap-2">
          <button onclick="window.print()" class="flex-1 py-2 rounded-lg bg-slate-100 dark:bg-darkCard hover:bg-slate-200 dark:hover:bg-slate-800 text-inkPrimary dark:text-textDarkPrimary font-semibold flex items-center justify-center gap-1.5 border border-borderSlate dark:border-darkBorder transition-colors cursor-pointer text-xs" title="Export Substation Brief">
            <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z" /></svg>
            <span>Substation Audit</span>
          </button>
          <a href="${gmapsUrl}" target="_blank" rel="noopener noreferrer" class="flex-1 py-2 rounded-lg bg-rose-600 hover:bg-rose-500 text-white font-semibold flex items-center justify-center gap-1.5 transition-colors text-xs text-center">
            <span>Satellite Inspection</span>
            <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" /></svg>
          </a>
        </div>
      `;

      if (zoomTo && mainFlowMapInstance && s.lat && s.lng) {
        mainFlowMapInstance.flyTo([s.lat, s.lng], 9, { duration: 0.8 });
      }
    }

    function selectCleanPlant(plant) {
      const panel = document.getElementById('nodePanelContent');
      const statusPill = document.getElementById('nodeStatusPill');
      const resetBtn = document.getElementById('resetNodePanelBtn');
      if (!panel) return;

      if (statusPill) {
        statusPill.textContent = 'Plant Telemetry';
        statusPill.className = 'px-2 py-0.5 rounded text-[10px] font-mono font-bold uppercase bg-teal-500/10 text-teal-600 border border-teal-500/20';
      }
      if (resetBtn) resetBtn.classList.remove('hidden');

      let nearestSubInfo = 'Calculating...';
      if (plant.lat && plant.lng && typeof findNearestSubstation === 'function') {
        const nearest = findNearestSubstation(plant.lat, plant.lng, 220);
        if (nearest) {
          nearestSubInfo = `${nearest.substation.name} (~${nearest.distanceKm.toFixed(1)} km)`;
        }
      }

      const gmapsUrl = (plant.lat && plant.lng)
        ? `https://maps.google.com/maps?t=k&q=loc:${plant.lat},${plant.lng}&gl=vn&hl=vi`
        : `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(plant.name + ' Vietnam')}`;

      panel.innerHTML = `
        <div class="space-y-1.5 pb-3 border-b border-borderSlate dark:border-darkBorder">
          <span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold uppercase bg-teal-500/10 text-teal-600 border border-teal-500/20">
            ${plant.type || 'Clean Energy'} Asset
          </span>
          <h4 class="text-lg font-bold text-inkPrimary dark:text-textDarkPrimary">${plant.name}</h4>
          <p class="text-xs text-inkMuted dark:text-textDarkMuted">${plant.province || plant.location || 'Vietnam'}</p>
        </div>

        <div class="grid grid-cols-2 gap-2">
          <div class="p-2.5 rounded-lg bg-slate-50 dark:bg-darkCard border border-borderSlate dark:border-darkBorder space-y-0.5">
            <span class="text-slate-400 text-[10px] uppercase">Capacity</span>
            <div class="text-sm font-bold text-teal-600 dark:text-teal-400">${(parseFloat(plant.capacity_mw) || 0).toLocaleString()} MW</div>
          </div>
          <div class="p-2.5 rounded-lg bg-slate-50 dark:bg-darkCard border border-borderSlate dark:border-darkBorder space-y-0.5">
            <span class="text-slate-400 text-[10px] uppercase">Status</span>
            <div class="text-sm font-bold text-inkPrimary dark:text-textDarkPrimary">${plant.status || 'Operational'}</div>
          </div>
        </div>

        <div class="p-2.5 rounded-lg bg-slate-50 dark:bg-darkCard border border-borderSlate dark:border-darkBorder space-y-1">
          <span class="text-slate-400 text-[10px] uppercase">Developer / Operator</span>
          <div class="text-xs font-semibold text-inkPrimary dark:text-textDarkPrimary">${plant.developer || plant.investor || 'Institutional Energy Operator'}</div>
        </div>

        <div class="p-2.5 rounded-lg bg-slate-50 dark:bg-darkCard border border-borderSlate dark:border-darkBorder space-y-1">
          <span class="text-slate-400 text-[10px] uppercase">Nearest Grid Intertie Corridor</span>
          <div class="text-xs font-bold text-amber-600 dark:text-amber-400">${nearestSubInfo}</div>
        </div>

        <div class="p-2.5 rounded-lg bg-slate-50 dark:bg-darkCard border border-borderSlate dark:border-darkBorder space-y-1">
          <span class="text-slate-400 text-[10px] uppercase">Coordinates (WGS84)</span>
          <div class="text-xs text-inkMuted dark:text-textDarkMuted">${(plant.lat && plant.lng) ? 'Lat: ' + plant.lat + ', Lng: ' + plant.lng : 'Unmapped'}</div>
        </div>

        <div class="pt-2 flex items-center gap-2">
          <a href="${gmapsUrl}" target="_blank" rel="noopener noreferrer" class="flex-1 py-2 rounded-lg bg-teal-600 hover:bg-teal-500 text-white font-semibold flex items-center justify-center gap-1.5 transition-colors text-xs text-center">
            <span>Satellite Inspection</span>
            <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" /></svg>
          </a>
        </div>
      `;
    }

    function quickSelectHub(hubName) {
      const norm = hubName.toUpperCase();
      const sub = ALL_GRID_SUBSTATIONS.find(x => x.name.toUpperCase().includes(norm));
      if (sub) {
        selectGridSubstation(sub.id, true);
      }
    }
"""

    html = html.replace(
        "let ALL_GRID_SUBSTATIONS = [];",
        f"let ALL_GRID_SUBSTATIONS = [];\n{side_by_side_js}\n",
        1
    )

    # 3. Update openSubstationModal to seamlessly route to selectGridSubstation
    old_open_sub = """function openSubstationModal(subId) {
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
    }"""

    new_open_sub = """function openSubstationModal(subId) {
      selectGridSubstation(subId, true);
    }"""

    assert old_open_sub in html, "Failed to find old openSubstationModal in source HTML"
    html = html.replace(old_open_sub, new_open_sub, 1)

    # 4. Update Clean Plants marker click handler to also trigger selectCleanPlant(p)
    old_plant_marker_click = "marker.bindTooltip(`<strong>${p.name}</strong><br><span class=\"text-[10px] text-slate-400\">${p.capacity_mw || '--'} MW &middot; ${p.type}</span>`, { direction: 'top' });"
    new_plant_marker_click = """marker.bindTooltip(`<strong>${p.name}</strong><br><span class=\"text-[10px] text-slate-400\">${p.capacity_mw || '--'} MW &middot; ${p.type}</span>`, { direction: 'top' });
          marker.on('click', () => selectCleanPlant(p));"""

    if old_plant_marker_click in html:
        html = html.replace(old_plant_marker_click, new_plant_marker_click, 1)

    # 5. Initialize the side panel with resetNodeInspectionPanel() in DOMContentLoaded
    html = html.replace(
        "loadVietnamTerritory();",
        "resetNodeInspectionPanel();\n      loadVietnamTerritory();",
        1
    )

    with open(TARGET_REV, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Successfully generated {TARGET_REV} ({len(html)} bytes)")

if __name__ == "__main__":
    generate()
