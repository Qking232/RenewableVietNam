"""
Refactor index.html (Industrial Hub) into an Institutional 50/50 Split-Screen Telemetry Cockpit.
- Left 50%: Fixed ArcGIS Esri Satellite Map with sovereignty markers, full extent button, DPPA legend, and live active pin counter.
- Right 50%: Synchronized Industrial Hub Dossier with sticky filter toolbar, cards / table toggle, pagination, and bi-directional interaction.
- Mobile quick toggle button.
- Retains #powerSizer immediately below the cockpit.
"""

import os
import re

INDEX_PATH = r"G:\My Drive\7. AI\Gemini\RenewableVietNam\index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# Verify presence of #hubs and #powerSizer
assert '<section id="hubs"' in content, "Section #hubs not found!"
assert '<section id="powerSizer"' in content, "Section #powerSizer not found!"

# Find start of #hubs and start of #powerSizer
hubs_start = content.find('<section id="hubs"')
power_sizer_start = content.find('<section id="powerSizer"')

pre_hubs = content[:hubs_start]
from_power_sizer = content[power_sizer_start:]

NEW_HUBS_SECTION = '''<section id="hubs" class="space-y-3.5">
      <!-- Section Title & Meta Header -->
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
        <div class="space-y-0.5">
          <div class="flex items-center gap-2">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-teal-500 dark:bg-teal-400"></span>
            <span class="font-mono text-[11px] uppercase tracking-wider text-teal-600 dark:text-teal-400 font-semibold">
              Vietnam Industrial Zone Directory &middot; Decree 80/2024/NĐ-CP DPPA
            </span>
          </div>
          <h2 class="text-xl sm:text-2xl font-normal tracking-tight text-inkPrimary dark:text-textDarkPrimary">
            Eco-Industrial Parks &amp; Clean Power Interconnections
          </h2>
        </div>

        <!-- Active Results & Total Badge -->
        <div class="flex items-center gap-2 font-mono text-[11px]">
          <span class="text-inkMuted dark:text-textDarkMuted bg-slate-100 dark:bg-darkCard px-2.5 py-1 rounded-lg border border-borderSlate dark:border-darkBorder">
            Showing <span id="filteredHubsCount" class="font-bold text-teal-600 dark:text-teal-400">168</span> of <span id="totalAvailableHubs" class="font-semibold text-inkPrimary dark:text-textDarkPrimary">168</span> national hubs
          </span>
        </div>
      </div>

      <!-- 50/50 SPLIT-SCREEN COCKPIT GRID -->
      <div id="hubCockpitContainer" class="grid grid-cols-1 lg:grid-cols-12 gap-4 lg:h-[calc(100vh-210px)] min-h-[640px] items-stretch">
        
        <!-- LEFT PANE: SATELLITE GIS ATLAS COCKPIT (50%) -->
        <div id="ecoParkMapContainer" class="lg:col-span-6 flex flex-col h-[460px] sm:h-[520px] lg:h-full rounded-2xl bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder shadow-sm p-3 relative overflow-hidden">
          <!-- Top Map Controls -->
          <div class="flex items-center justify-between pb-2 mb-2 border-b border-borderSlate/60 dark:border-darkBorder/60 shrink-0">
            <div class="flex items-center gap-2">
              <span class="w-2 h-2 rounded-full bg-teal-500 animate-pulse"></span>
              <span class="font-mono text-[11px] font-semibold text-inkPrimary dark:text-textDarkPrimary uppercase tracking-wider">
                ArcGIS Satellite GIS Atlas (WGS84)
              </span>
            </div>
            <div class="flex items-center gap-1.5 font-mono text-[10px]">
              <span class="hidden sm:inline-flex items-center gap-1 px-2 py-0.5 rounded bg-slate-100 dark:bg-darkCard border border-borderSlate dark:border-darkBorder text-teal-600 dark:text-teal-400 font-semibold">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span>
                <span>Esri World Imagery</span>
              </span>
              <button id="resetMapZoomBtn" class="px-2.5 py-1 rounded bg-slate-100 dark:bg-darkCard border border-borderSlate dark:border-darkBorder text-inkMuted dark:text-textDarkMuted hover:text-teal-600 dark:hover:text-teal-400 transition-colors cursor-pointer" title="Reset Zoom to Vietnam extent">
                Full Extent
              </button>
            </div>
          </div>

          <!-- Leaflet Map Canvas -->
          <div id="ecoParkMap" class="flex-1 w-full rounded-xl overflow-hidden border border-slate-200 dark:border-darkBorder relative z-0"></div>

          <!-- Bottom Map Legend Bar -->
          <div class="flex flex-wrap items-center justify-between gap-2 pt-2 mt-2 border-t border-borderSlate/60 dark:border-darkBorder/60 shrink-0 font-mono text-[10px] text-inkMuted dark:text-textDarkMuted">
            <div class="flex flex-wrap items-center gap-2 sm:gap-3">
              <span class="text-slate-400 uppercase tracking-wider">Legend:</span>
              <span class="flex items-center gap-1"><span class="w-2 h-2 rounded-full bg-emerald-500"></span>Cat 1 &amp; 2 Ready</span>
              <span class="flex items-center gap-1"><span class="w-2 h-2 rounded-full bg-sky-500"></span>Cat 2 Wheeling</span>
              <span class="flex items-center gap-1"><span class="w-2 h-2 rounded-full bg-slate-500"></span>Developing</span>
              <span class="flex items-center gap-1"><span class="px-1 py-0.2 rounded bg-purple-500/20 text-purple-400 font-bold border border-purple-500/30 text-[9px]">220k</span>220kV Intertie</span>
            </div>
            <div>
              Active Pins: <strong id="visibleHubPinsCount" class="text-inkPrimary dark:text-textDarkPrimary font-bold">168</strong>
            </div>
          </div>
        </div>

        <!-- RIGHT PANE: SYNCHRONIZED INDUSTRIAL HUB DOSSIER (50%) -->
        <div id="hubDossierContainer" class="lg:col-span-6 flex flex-col h-full lg:max-h-full rounded-2xl bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder shadow-sm overflow-hidden">
          
          <!-- Top Sticky Filter & Mode Toolbar -->
          <div class="p-3 sm:p-3.5 border-b border-borderSlate dark:border-darkBorder bg-slate-50/70 dark:bg-darkCard/50 space-y-2.5 shrink-0">
            <!-- Search bar + View Toggle Button -->
            <div class="flex items-center gap-2">
              <div class="relative flex-1">
                <input type="text" id="hubSearchInput" placeholder="Search park, province, developer, tenant (LEGO, Pegatron, Foxconn)..." class="w-full pl-8 pr-3 py-1.5 rounded-lg bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder text-inkPrimary dark:text-textDarkPrimary text-xs focus:outline-none focus:border-teal-500 font-sans transition-colors" />
                <svg class="w-3.5 h-3.5 text-slate-400 absolute left-2.5 top-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                </svg>
              </div>

              <button id="tableOrCardsToggleBtn" class="inline-flex items-center gap-1 px-2.5 py-1.5 rounded-lg bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder text-inkMuted dark:text-textDarkMuted hover:text-teal-600 font-mono text-[10px] cursor-pointer shrink-0" title="Toggle Cards / Table Layout">
                <span id="viewModeIcon">☷</span>
                <span id="viewModeText">Table</span>
              </button>
            </div>

            <!-- Facet Filter Toolbar -->
            <div class="flex flex-wrap items-center gap-1.5 font-mono text-[10px]">
              <!-- Region Pills -->
              <span class="text-slate-400 uppercase tracking-wider mr-0.5">Region:</span>
              <button data-filter-region="all" class="filter-pill-region px-2 py-0.5 rounded bg-teal-600 text-white font-semibold cursor-pointer">All</button>
              <button data-filter-region="North" class="filter-pill-region px-2 py-0.5 rounded bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder text-inkPrimary dark:text-textDarkMuted hover:text-teal-600 cursor-pointer">North</button>
              <button data-filter-region="Central" class="filter-pill-region px-2 py-0.5 rounded bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder text-inkPrimary dark:text-textDarkMuted hover:text-teal-600 cursor-pointer">Central</button>
              <button data-filter-region="South" class="filter-pill-region px-2 py-0.5 rounded bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder text-inkPrimary dark:text-textDarkMuted hover:text-teal-600 cursor-pointer">South</button>

              <span class="text-slate-300 dark:text-slate-700 mx-0.5">&middot;</span>

              <!-- Dropdowns -->
              <select id="filterProvinceSelect" class="bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder text-inkPrimary dark:text-textDarkPrimary rounded px-2 py-0.5 text-[10px] focus:outline-none max-w-[120px] sm:max-w-[140px] cursor-pointer">
                <option value="all">All Provinces</option>
              </select>

              <select id="filterDppaSelect" class="bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder text-inkPrimary dark:text-textDarkPrimary rounded px-2 py-0.5 text-[10px] focus:outline-none max-w-[110px] cursor-pointer">
                <option value="all">All DPPA</option>
                <option value="ready">Cat 1 &amp; 2 Ready</option>
                <option value="cat2">Cat 2 Wheeling</option>
                <option value="developing">Developing</option>
              </select>

              <select id="filterSubstationSelect" class="bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder text-inkPrimary dark:text-textDarkPrimary rounded px-2 py-0.5 text-[10px] focus:outline-none max-w-[110px] cursor-pointer">
                <option value="all">All Grid</option>
                <option value="220">220kV Dedicated</option>
                <option value="110">110kV Onsite</option>
              </select>

              <button id="resetFiltersBtn" class="ml-auto text-slate-400 hover:text-slate-700 dark:hover:text-slate-200 text-[10px] underline cursor-pointer">
                Reset
              </button>
            </div>
          </div>

          <!-- Scrollable Dossier Content -->
          <div id="hubDossierScrollArea" class="flex-1 overflow-y-auto p-3 sm:p-3.5 space-y-2.5 custom-scrollbar">
            <!-- View 1: Dossier Cards Container -->
            <div id="hubCardsList" class="space-y-2">
              <!-- Dynamically rendered via renderHubsDossier() -->
              <div class="p-8 text-center text-slate-400 font-mono text-xs">
                Loading Eco-Industrial Hubs Telemetry...
              </div>
            </div>

            <!-- View 2: Compact Sortable Table (Hidden by default, toggled via tableOrCardsToggleBtn) -->
            <div id="hubsTableContainer" class="hidden rounded-xl border border-borderSlate dark:border-darkBorder overflow-hidden">
              <div class="overflow-x-auto">
                <table class="w-full text-left text-xs border-collapse">
                  <thead>
                    <tr class="font-mono text-[10px] text-inkMuted dark:text-textDarkMuted border-b border-borderSlate dark:border-darkBorder bg-slate-50/80 dark:bg-darkCard/60 uppercase tracking-wider">
                      <th class="py-2.5 px-3">#</th>
                      <th class="py-2.5 px-3 cursor-pointer hover:text-inkPrimary dark:hover:text-white" data-sort="name">Industrial Park</th>
                      <th class="py-2.5 px-3 cursor-pointer hover:text-inkPrimary dark:hover:text-white" data-sort="province">Province</th>
                      <th class="py-2.5 px-3">Grid</th>
                      <th class="py-2.5 px-3 cursor-pointer hover:text-inkPrimary dark:hover:text-white" data-sort="solar">Rooftop Solar</th>
                      <th class="py-2.5 px-3 cursor-pointer hover:text-inkPrimary dark:hover:text-white" data-sort="clean">Clean %</th>
                      <th class="py-2.5 px-3">DPPA</th>
                      <th class="py-2.5 px-3 text-right">Action</th>
                    </tr>
                  </thead>
                  <tbody id="hubsTableBody" class="divide-y divide-borderSlate dark:divide-darkBorder font-mono">
                    <!-- Dynamically rendered rows -->
                  </tbody>
                </table>
              </div>
            </div>
          </div>

          <!-- Sticky Bottom Pagination Bar -->
          <div id="hubPaginationBar" class="p-2.5 sm:p-3 border-t border-borderSlate dark:border-darkBorder bg-slate-50/60 dark:bg-darkCard/50 flex items-center justify-between text-xs font-mono text-inkMuted dark:text-textDarkMuted shrink-0">
            <div class="flex items-center gap-2">
              <span>Rows:</span>
              <select id="pageSizeSelect" class="bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder rounded px-2 py-0.5 text-[10px] text-inkPrimary dark:text-textDarkPrimary focus:outline-none cursor-pointer">
                <option value="25" selected>25</option>
                <option value="50">50</option>
                <option value="100">100</option>
                <option value="all">All</option>
              </select>
              <span id="pageRangeInfo" class="text-slate-400 text-[11px]">Showing 1–25 of 168</span>
            </div>

            <div class="flex items-center gap-1.5" id="paginationControls">
              <button id="prevPageBtn" class="px-2 py-0.5 rounded bg-white dark:bg-darkSurface hover:bg-slate-100 dark:hover:bg-darkBorder border border-borderSlate dark:border-darkBorder text-inkPrimary dark:text-textDarkPrimary transition-colors cursor-pointer disabled:opacity-40 disabled:cursor-not-allowed text-[11px]">
                &larr; Prev
              </button>
              <span class="px-2 py-0.5 rounded bg-teal-600 text-white font-semibold text-[11px]" id="currentPageIndicator">1</span>
              <span class="text-slate-400">/</span>
              <span id="totalPagesIndicator" class="text-slate-400 font-semibold text-[11px]">7</span>
              <button id="nextPageBtn" class="px-2 py-0.5 rounded bg-white dark:bg-darkSurface hover:bg-slate-100 dark:hover:bg-darkBorder border border-borderSlate dark:border-darkBorder text-inkPrimary dark:text-textDarkPrimary transition-colors cursor-pointer disabled:opacity-40 disabled:cursor-not-allowed text-[11px]">
                Next &rarr;
              </button>
            </div>
          </div>

        </div>

      </div>
    </section>

    <!-- MOBILE FLOATING SWITCHER BUTTON (< 1024px) -->
    <div class="lg:hidden fixed bottom-4 right-4 z-40">
      <button id="mobileHubViewToggleBtn" class="flex items-center gap-2 px-3.5 py-2 rounded-full bg-teal-600 hover:bg-teal-500 text-white font-mono text-xs font-semibold shadow-lg shadow-teal-500/20 border border-teal-400/30 transition-all cursor-pointer">
        <span id="mobileHubToggleIcon">📋</span>
        <span id="mobileHubToggleText">View Dossier</span>
      </button>
    </div>
'''

new_html = pre_hubs + NEW_HUBS_SECTION + '\n\n    ' + from_power_sizer

# Now update the JavaScript to support Cards View, Table View toggle, and Bi-directional Spatial Sync
JS_DOSSIER_CONTROLLER = '''
    let activeHubView = "cards"; // "cards" or "table"
    window.hubMarkerMap = new Map();

    function renderHubsDossier(filtered) {
      const cardsList = document.getElementById("hubCardsList");
      const tbody = document.getElementById("hubsTableBody");
      const countEl = document.getElementById("filteredHubsCount");
      const totalAvailEl = document.getElementById("totalAvailableHubs");
      if (totalAvailEl) totalAvailEl.textContent = HUBS.length;

      countEl.textContent = filtered.length;

      if (filtered.length === 0) {
        if (cardsList) cardsList.innerHTML = `<div class="p-8 text-center text-slate-400 font-mono text-xs">No industrial hubs match active filters across ${HUBS.length} national records.</div>`;
        if (tbody) tbody.innerHTML = `<tr><td colspan="8" class="p-8 text-center text-slate-400 font-mono text-xs">No matching industrial hubs.</td></tr>`;
        updatePaginationBar(0, 0, 0);
        return;
      }

      const effectivePageSize = pageSize === "all" ? filtered.length : parseInt(pageSize);
      const totalPages = Math.max(1, Math.ceil(filtered.length / effectivePageSize));
      if (currentPage > totalPages) currentPage = totalPages;
      const startIdx = (currentPage - 1) * effectivePageSize;
      const endIdx = Math.min(startIdx + effectivePageSize, filtered.length);
      const paged = filtered.slice(startIdx, endIdx);

      updatePaginationBar(filtered.length, startIdx, endIdx);

      // Render Cards View
      let cardsHtml = "";
      let tableHtml = "";

      paged.forEach((hub, idx) => {
        const globalIdx = startIdx + idx;
        const isReady = hub.dppaClass === "ready";
        const isCat2 = hub.dppaClass === "cat2";
        const dppaBadge = isReady 
          ? `<span class="px-2 py-0.5 rounded font-mono text-[9px] bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 font-semibold border border-emerald-500/20">Cat 1 &amp; 2 Ready</span>`
          : (isCat2 
            ? `<span class="px-2 py-0.5 rounded font-mono text-[9px] bg-sky-500/10 text-sky-600 dark:text-sky-400 font-semibold border border-sky-500/20">Cat 2 Wheeling</span>`
            : `<span class="px-2 py-0.5 rounded font-mono text-[9px] bg-amber-500/10 text-amber-600 dark:text-amber-400 font-semibold border border-amber-500/20">Developing</span>`);

        const tenantsList = (hub.anchorTenants || []).slice(0, 3).join(", ");

        cardsHtml += `
          <div id="hub-card-${hub.id}" onclick="selectHubFromCard('${hub.id}', ${hub.lat}, ${hub.lng}, event)" class="hub-dossier-card p-3 rounded-xl bg-slate-50/70 dark:bg-darkCard/70 border border-borderSlate dark:border-darkBorder hover:border-teal-500/60 dark:hover:border-teal-400/50 transition-all cursor-pointer group flex flex-col justify-between gap-2">
            <div class="flex items-start justify-between gap-2">
              <div class="space-y-1 flex-1 min-w-0">
                <div class="flex items-center gap-1.5 font-mono text-[10px]">
                  ${dppaBadge}
                  <span class="text-inkMuted dark:text-textDarkMuted truncate">${hub.province} &middot; ${hub.region}</span>
                </div>
                <h4 class="text-xs sm:text-sm font-semibold text-inkPrimary dark:text-textDarkPrimary group-hover:text-teal-600 dark:group-hover:text-teal-400 transition-colors truncate">
                  ${hub.name}
                </h4>
                <div class="text-[11px] text-inkMuted dark:text-textDarkMuted truncate">
                  ${hub.developer} &middot; <span class="font-mono text-teal-600 dark:text-teal-400 font-semibold">${hub.totalAreaHa} ha</span>
                </div>
                ${tenantsList ? `<div class="text-[10px] text-slate-400 dark:text-slate-500 truncate">Tenants: ${tenantsList}</div>` : ""}
              </div>

              <div class="text-right shrink-0 font-mono">
                <div class="text-xs sm:text-sm font-bold text-teal-600 dark:text-teal-400">
                  ${hub.cleanEnergyShare}% <span class="text-[9px] text-slate-400 font-normal">clean</span>
                </div>
                <div class="text-[10px] text-inkMuted dark:text-textDarkMuted">
                  ${hub.rooftopPotentialMWp} MWp
                </div>
                <div class="text-[9px] text-purple-600 dark:text-purple-400 font-semibold">
                  ${hub.substationKv}kV Intertie
                </div>
              </div>
            </div>

            <div class="flex items-center justify-between pt-1.5 border-t border-borderSlate/50 dark:border-darkBorder/50 font-mono text-[10px]">
              <button type="button" onclick="event.stopPropagation(); selectHubFromCard('${hub.id}', ${hub.lat}, ${hub.lng}, null);" class="text-teal-600 dark:text-teal-400 hover:underline flex items-center gap-1 font-semibold">
                <span>Fly to Satellite</span> &rarr;
              </button>

              <button type="button" onclick="event.stopPropagation(); openHubModal('${hub.id}');" class="px-2 py-0.5 rounded bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder text-inkMuted dark:text-textDarkMuted hover:text-inkPrimary dark:hover:text-white transition-colors">
                Technical Dossier &rarr;
              </button>
            </div>
          </div>
        `;

        tableHtml += `
          <tr class="hover:bg-slate-50/80 dark:hover:bg-darkCard/50 transition-colors cursor-pointer" onclick="selectHubFromCard('${hub.id}', ${hub.lat}, ${hub.lng}, event)">
            <td class="py-2.5 px-3 text-slate-400 font-mono">${String(globalIdx + 1).padStart(3, '0')}</td>
            <td class="py-2.5 px-3 font-semibold text-inkPrimary dark:text-textDarkPrimary truncate max-w-[170px]">${hub.name}</td>
            <td class="py-2.5 px-3 text-inkMuted dark:text-textDarkMuted">${hub.province}</td>
            <td class="py-2.5 px-3 text-purple-600 dark:text-purple-400 font-bold">${hub.substationKv}kV</td>
            <td class="py-2.5 px-3 text-teal-600 dark:text-teal-400 font-bold">${hub.rooftopPotentialMWp} MWp</td>
            <td class="py-2.5 px-3">${hub.cleanEnergyShare}%</td>
            <td class="py-2.5 px-3">${dppaBadge}</td>
            <td class="py-2.5 px-3 text-right">
              <button onclick="event.stopPropagation(); openHubModal('${hub.id}');" class="px-2 py-0.5 rounded bg-slate-100 dark:bg-darkCard border border-borderSlate dark:border-darkBorder text-inkMuted dark:text-textDarkMuted hover:text-teal-600 text-[10px]">Inspect</button>
            </td>
          </tr>
        `;
      });

      if (cardsList) cardsList.innerHTML = cardsHtml;
      if (tbody) tbody.innerHTML = tableHtml;

      if (hubMap && hubMarkersLayer) {
        renderMapMarkers(paged.length > 0 ? paged : filtered.slice(0, 50));
      }
    }

    // Bi-Directional Synchronizer: Map Pin Click -> Select Card in Dossier
    function selectHubFromMap(hubId) {
      const filtered = getFilteredHubs();
      const idx = filtered.findIndex(h => h.id === hubId);
      if (idx !== -1) {
        const effectivePageSize = pageSize === "all" ? filtered.length : parseInt(pageSize);
        const targetPage = Math.floor(idx / effectivePageSize) + 1;
        if (currentPage !== targetPage) {
          currentPage = targetPage;
          renderHubsDossier(filtered);
        }
      }

      highlightHubCard(hubId);
    }

    // Bi-Directional Synchronizer: Dossier Card Click -> Map FlyTo
    function selectHubFromCard(hubId, lat, lng, event) {
      if (event && event.target.closest('button') && !event.target.closest('button').classList.contains('fly-action')) return;

      highlightHubCard(hubId);

      if (lat && lng && hubMap) {
        hubMap.flyTo([lat, lng], 13, { duration: 0.85 });
        const marker = window.hubMarkerMap.get(hubId);
        if (marker) {
          setTimeout(() => {
            marker.openPopup();
          }, 900);
        }
      }
    }

    function highlightHubCard(hubId) {
      document.querySelectorAll('.hub-dossier-card').forEach(c => {
        c.classList.remove('ring-2', 'ring-teal-500', 'bg-teal-500/10', 'dark:bg-teal-950/40');
      });

      const card = document.getElementById(`hub-card-${hubId}`);
      if (card) {
        card.classList.add('ring-2', 'ring-teal-500', 'bg-teal-500/10', 'dark:bg-teal-950/40');
        card.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
    }

    function getFilteredHubs() {
      return HUBS.filter(hub => {
        if (currentFilter.search) {
          const q = currentFilter.search.toLowerCase();
          const matchName = hub.name && hub.name.toLowerCase().includes(q);
          const matchDev = hub.developer && hub.developer.toLowerCase().includes(q);
          const matchProv = hub.province && hub.province.toLowerCase().includes(q);
          const matchTenants = hub.anchorTenants && hub.anchorTenants.some(t => t.toLowerCase().includes(q));
          if (!matchName && !matchDev && !matchProv && !matchTenants) return false;
        }

        if (currentFilter.region !== "all" && hub.region !== currentFilter.region) return false;
        if (currentFilter.province && currentFilter.province !== "all" && hub.province !== currentFilter.province) return false;

        if (currentFilter.dppa !== "all") {
          if (currentFilter.dppa === "ready" && hub.dppaClass !== "ready") return false;
          if (currentFilter.dppa === "cat2" && hub.dppaClass !== "cat2") return false;
          if (currentFilter.dppa === "developing" && hub.dppaClass !== "developing") return false;
        }

        if (currentFilter.substation !== "all") {
          if (currentFilter.substation === "220" && hub.substationKv < 220) return false;
          if (currentFilter.substation === "110" && hub.substationKv > 110) return false;
        }

        return true;
      });
    }
'''

# Update renderTable to delegate to renderHubsDossier
new_html = re.sub(r'function renderTable\(\)\s*\{.*?updatePaginationBar\(filtered\.length, startIdx, endIdx\);.*?if \(hubMap && hubMarkersLayer\) \{.*?\}\s*\}',
                  'function renderTable() {\n      const filtered = getFilteredHubs();\n      renderHubsDossier(filtered);\n    }',
                  new_html, flags=re.DOTALL)

# Insert JS_DOSSIER_CONTROLLER before renderTable
new_html = new_html.replace('function renderTable() {', JS_DOSSIER_CONTROLLER + '\n    function renderTable() {', 1)

# Update renderMapMarkers to register marker in window.hubMarkerMap and bind click
marker_register_snippet = '''
        const marker = L.marker([hub.lat, hub.lng], { icon: customIcon });
        marker.bindPopup(popupContent, { maxWidth: 280 });
        marker.on('click', () => {
          selectHubFromMap(hub.id);
        });
        hubMarkersLayer.addLayer(marker);
        window.hubMarkerMap.set(hub.id, marker);
'''

new_html = re.sub(r'const marker = L\.marker\(\[hub\.lat, hub\.lng\], \{ icon: customIcon \}\);\s*marker\.bindPopup\(popupContent, \{ maxWidth: 280 \}\);\s*hubMarkersLayer\.addLayer\(marker\);',
                  marker_register_snippet.strip(),
                  new_html)

# Update visible pins badge in renderMapMarkers
visible_pins_update = '''
      const countEl = document.getElementById("visibleHubPinsCount");
      if (countEl) countEl.textContent = hubsToRender.length;
'''
new_html = new_html.replace('hubMarkersLayer.clearLayers();', 'hubMarkersLayer.clearLayers();\n      window.hubMarkerMap.clear();' + visible_pins_update, 1)

# Add event listeners for table/cards toggle and mobile switcher
event_listeners_snippet = '''
      // Table / Cards Layout Toggle
      const tableCardsBtn = document.getElementById("tableOrCardsToggleBtn");
      const cardsList = document.getElementById("hubCardsList");
      const tableContainer = document.getElementById("hubsTableContainer");
      const modeText = document.getElementById("viewModeText");

      if (tableCardsBtn && cardsList && tableContainer) {
        tableCardsBtn.addEventListener("click", () => {
          if (activeHubView === "cards") {
            activeHubView = "table";
            cardsList.classList.add("hidden");
            tableContainer.classList.remove("hidden");
            if (modeText) modeText.textContent = "Cards";
          } else {
            activeHubView = "cards";
            cardsList.classList.remove("hidden");
            tableContainer.classList.add("hidden");
            if (modeText) modeText.textContent = "Table";
          }
        });
      }

      // Mobile Quick View Switcher
      const mobileHubBtn = document.getElementById("mobileHubViewToggleBtn");
      if (mobileHubBtn) {
        let isMapMode = false;
        mobileHubBtn.addEventListener("click", () => {
          isMapMode = !isMapMode;
          if (isMapMode) {
            document.getElementById("ecoParkMapContainer")?.scrollIntoView({ behavior: 'smooth' });
            document.getElementById("mobileHubToggleIcon").textContent = "📋";
            document.getElementById("mobileHubToggleText").textContent = "View Dossier";
          } else {
            document.getElementById("hubDossierContainer")?.scrollIntoView({ behavior: 'smooth' });
            document.getElementById("mobileHubToggleIcon").textContent = "🗺️";
            document.getElementById("mobileHubToggleText").textContent = "View Map";
          }
        });
      }
'''

new_html = new_html.replace('document.getElementById("closeModalBtn").addEventListener("click", closeHubModal);',
                            event_listeners_snippet + '\n      document.getElementById("closeModalBtn").addEventListener("click", closeHubModal);', 1)

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(new_html)

print("[SUCCESS] Refactored index.html to 50/50 Split-Screen Telemetry Cockpit!")
print(f"Total size: {len(new_html.encode('utf-8'))} bytes")
