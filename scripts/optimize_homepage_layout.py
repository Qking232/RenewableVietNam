import re
import os

src_file = "RenewableVietNam/index.html"
with open(src_file, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Locate main slices
idx_gateways = text.find("<!-- SECTION: 5 CORE EXECUTIVE EDGE GATEWAYS (BENTO GRID) -->")
idx_pillars = text.find("<!-- SECTION 1: THE 12 STRATEGIC PILLARS OF VIETNAM ENERGY TRANSITION -->")
idx_telemetry = text.find("<!-- SECTION 2: 10-MODULE INSTITUTIONAL VISUAL TELEMETRY SUITE -->")
idx_sim = text.find("<!-- SECTION 3: INTERACTIVE DECREE 80 DPPA ECONOMIC SIMULATOR -->")
idx_console = text.find("<!-- SECTION 4: BENTO SUBDOMAIN COMMAND CONSOLE -->")
idx_main_end = text.find("</main>")

head_and_hero = text[:idx_gateways]

# Make Quick Metrics in Hero interactive buttons
metrics_old = """      <!-- Quick Metrics Ribbon -->
      <div class="flex items-center gap-3 sm:gap-4 shrink-0 font-mono text-[11px] pt-2 md:pt-0 border-t md:border-t-0 border-slate-100 dark:border-slate-700/50">
        <div class="text-right">
          <span class="block text-slate-500 dark:text-slate-400 text-[10px]">Generation Pipeline</span>
          <strong class="text-sm font-semibold text-slate-800 dark:text-slate-200">107.5 GW</strong>
        </div>
        <div class="w-px h-7 bg-slate-200 dark:bg-slate-700"></div>
        <div class="text-right">
          <span class="block text-slate-500 dark:text-slate-400 text-[10px]">EV Charging Ports</span>
          <strong class="text-sm font-semibold text-slate-800 dark:text-slate-200">22,055+</strong>
        </div>
        <div class="w-px h-7 bg-slate-200 dark:bg-slate-700"></div>
        <div class="text-right">
          <span class="block text-slate-500 dark:text-slate-400 text-[10px]">Industrial Footprint</span>
          <strong class="text-sm font-semibold text-slate-800 dark:text-slate-200">104.4K ha</strong>
        </div>
        <div class="w-px h-7 bg-slate-200 dark:bg-slate-700"></div>
        <div class="text-right">
          <span class="block text-slate-500 dark:text-slate-400 text-[10px]">Cloud Telemetry</span>
          <strong id="telemetryStatusBadge" class="text-[11px] font-semibold text-emerald-600 dark:text-emerald-400">Syncing...</strong>
        </div>
      </div>"""

metrics_new = """      <!-- Quick Metrics Ribbon (Interactive Workstation Triggers) -->
      <div class="flex items-center gap-2.5 sm:gap-4 shrink-0 font-mono text-[11px] pt-2 md:pt-0 border-t md:border-t-0 border-slate-100 dark:border-slate-700/50">
        <button type="button" onclick="switchHomepageWorkstation('telemetry', true); switchHomepageTelemetryLens('generation');" class="text-right hover:opacity-80 transition-opacity cursor-pointer" title="Jump to Generation Telemetry">
          <span class="block text-slate-500 dark:text-slate-400 text-[10px]">Generation Pipeline &nearr;</span>
          <strong class="text-xs sm:text-sm font-semibold text-teal-600 dark:text-teal-400">107.5 GW</strong>
        </button>
        <div class="w-px h-7 bg-slate-200 dark:bg-slate-700"></div>
        <button type="button" onclick="switchHomepageWorkstation('telemetry', true); switchHomepageTelemetryLens('market');" class="text-right hover:opacity-80 transition-opacity cursor-pointer" title="Jump to EV Telemetry">
          <span class="block text-slate-500 dark:text-slate-400 text-[10px]">EV Charging Ports &nearr;</span>
          <strong class="text-xs sm:text-sm font-semibold text-cyan-600 dark:text-cyan-400">22,055+</strong>
        </button>
        <div class="w-px h-7 bg-slate-200 dark:bg-slate-700"></div>
        <button type="button" onclick="switchHomepageWorkstation('telemetry', true); switchHomepageTelemetryLens('grid');" class="text-right hover:opacity-80 transition-opacity cursor-pointer" title="Jump to Grid Telemetry">
          <span class="block text-slate-500 dark:text-slate-400 text-[10px]">Industrial Footprint &nearr;</span>
          <strong class="text-xs sm:text-sm font-semibold text-amber-600 dark:text-amber-400">104.4K ha</strong>
        </button>
        <div class="w-px h-7 bg-slate-200 dark:bg-slate-700"></div>
        <div class="text-right">
          <span class="block text-slate-500 dark:text-slate-400 text-[10px]">Cloud Telemetry</span>
          <strong id="telemetryStatusBadge" class="text-[11px] font-semibold text-emerald-600 dark:text-emerald-400">Syncing...</strong>
        </div>
      </div>"""

if metrics_old in head_and_hero:
    head_and_hero = head_and_hero.replace(metrics_old, metrics_new)

# Mode Switcher markup
workstation_switcher = """    <!-- WORKSTATION ARCHITECTURAL MODE SWITCHER & ACTIVE FILTER HUD -->
    <div id="homepageWorkstationSwitcher" class="sticky top-14 sm:top-16 z-30 bg-white/95 dark:bg-slate-900/95 backdrop-blur-md p-2 rounded-2xl border border-slate-200/80 dark:border-slate-800 shadow-sm flex flex-col md:flex-row md:items-center justify-between gap-3 transition-colors">
      <!-- 3-Segmented Mode Switcher -->
      <div class="flex items-center gap-1.5 p-1 bg-slate-100 dark:bg-slate-800 rounded-xl font-mono text-xs w-full md:w-auto overflow-x-auto no-scrollbar">
        <button id="hpModeBtnOverview" type="button" onclick="switchHomepageWorkstation('overview')" class="hp-mode-btn flex items-center gap-2 px-3.5 py-2 rounded-lg font-semibold transition-all bg-white dark:bg-slate-700/80 text-teal-600 dark:text-teal-400 shadow-xs cursor-pointer">
          <svg class="w-4 h-4 text-teal-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"></path>
          </svg>
          <span>Executive Gateways &amp; 12 Pillars</span>
          <span class="text-[10px] px-1.5 py-0.5 rounded bg-teal-500/10 text-teal-600 dark:text-teal-400 font-mono font-bold">Flagship</span>
        </button>

        <button id="hpModeBtnTelemetry" type="button" onclick="switchHomepageWorkstation('telemetry')" class="hp-mode-btn flex items-center gap-2 px-3.5 py-2 rounded-lg font-semibold transition-all text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white cursor-pointer">
          <svg class="w-4 h-4 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path>
          </svg>
          <span>10-Module Telemetry Suite</span>
          <span class="text-[10px] px-1.5 py-0.5 rounded bg-blue-500/10 text-blue-600 dark:text-blue-400 font-mono font-bold">10 Charts</span>
        </button>

        <button id="hpModeBtnSimulator" type="button" onclick="switchHomepageWorkstation('simulator')" class="hp-mode-btn flex items-center gap-2 px-3.5 py-2 rounded-lg font-semibold transition-all text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white cursor-pointer">
          <svg class="w-4 h-4 text-emerald-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z"></path>
          </svg>
          <span>Decree 80 DPPA Simulator &amp; Hubs</span>
          <span class="text-[10px] px-1.5 py-0.5 rounded bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 font-mono font-bold">Decree 80</span>
        </button>
      </div>

      <div class="hidden lg:flex items-center gap-3 font-mono text-[11px] text-slate-500 dark:text-slate-400 pr-2">
        <div class="flex items-center gap-1.5">
          <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
          <span id="activeWorkstationStatusLabel">Mode: Executive Overview &amp; 12 Pillars</span>
        </div>
      </div>
    </div>
"""

# WORKSTATION VIEW 1: OVERVIEW (Gateways + 12 Pillars)
view_overview_content = text[idx_gateways:idx_telemetry]
view_overview = f"""
    <!-- ================================================================== -->
    <!-- WORKSTATION VIEW 1: EXECUTIVE GATEWAYS & 12 PILLARS                -->
    <!-- ================================================================== -->
    <div id="workstationViewOverview" class="space-y-6">
{view_overview_content.rstrip()}
    </div>
"""

# Extract Telemetry elements
telemetry_raw = text[idx_telemetry:idx_sim]

# Extract Telemetry header and KPI cards
idx_r1 = telemetry_raw.find("<!-- VISUAL ROW 1:")
telemetry_header_and_kpis = telemetry_raw[:idx_r1].rstrip()

# Extract each row
idx_r2 = telemetry_raw.find("<!-- VISUAL ROW 2:")
idx_r3 = telemetry_raw.find("<!-- VISUAL ROW 3:")
idx_r4 = telemetry_raw.find("<!-- VISUAL ROW 4:")
idx_r5 = telemetry_raw.find("<!-- VISUAL ROW 5:")

row1_content = telemetry_raw[idx_r1:idx_r2].strip()
row2_content = telemetry_raw[idx_r2:idx_r3].strip()
row3_content = telemetry_raw[idx_r3:idx_r4].strip()
row4_content = telemetry_raw[idx_r4:idx_r5].strip()
row5_content = telemetry_raw[idx_r5:].strip()

# Deconstruct Row 2: Chart 03 & Chart 04
c3_start = row2_content.find("<!-- Visual 03:")
c4_start = row2_content.find("<!-- Visual 04:")
chart03_div = row2_content[c3_start:c4_start].strip()
chart04_raw = row2_content[c4_start:].strip()
# remove the 1 closing </div> of row 2
if chart04_raw.endswith("</div>"):
    chart04_div = chart04_raw[:-6].strip()
else:
    chart04_div = chart04_raw

# Deconstruct Row 4: Chart 07 & Chart 08
c7_start = row4_content.find("<!-- Visual 07:")
c8_start = row4_content.find("<!-- Visual 08:")
chart07_div = row4_content[c7_start:c8_start].strip()
chart08_raw = row4_content[c8_start:].strip()
# remove the 1 closing </div> of row 4
if chart08_raw.endswith("</div>"):
    chart08_div = chart08_raw[:-6].strip()
else:
    chart08_div = chart08_raw

# Deconstruct Row 5: Chart 09 & Module 10
c9_start = row5_content.find("<!-- Visual 09:")
c10_start = row5_content.find("<!-- Visual 10:")
chart09_div = row5_content[c9_start:c10_start].strip()
chart10_raw = row5_content[c10_start:].strip()
# remove exactly 1 closing </div> of row 5
if chart10_raw.endswith("</div>"):
    chart10_div = chart10_raw[:-6].strip()
else:
    chart10_div = chart10_raw

# Build 3 Lens Groups
lens_switcher = """      <!-- 3-LENS SUB-TAB SWITCHER -->
      <div class="flex flex-wrap items-center justify-between gap-3 border-b border-slate-200/70 dark:border-slate-700/60 pb-3">
        <div class="flex items-center gap-1.5 p-1 bg-slate-100 dark:bg-slate-800 rounded-xl font-mono text-xs overflow-x-auto no-scrollbar">
          <button id="hpTelemetryLensBtnAll" type="button" onclick="switchHomepageTelemetryLens('all')" class="telemetry-lens-btn px-3 py-1.5 rounded-lg font-semibold transition-all bg-white dark:bg-slate-700/80 text-teal-600 dark:text-teal-400 shadow-xs cursor-pointer">
            All 10 Visuals
          </button>
          <button id="hpTelemetryLensBtnGen" type="button" onclick="switchHomepageTelemetryLens('generation')" class="telemetry-lens-btn px-3 py-1.5 rounded-lg font-semibold transition-all text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white cursor-pointer">
            Lens 1: Generation &amp; Trajectory (4)
          </button>
          <button id="hpTelemetryLensBtnGrid" type="button" onclick="switchHomepageTelemetryLens('grid')" class="telemetry-lens-btn px-3 py-1.5 rounded-lg font-semibold transition-all text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white cursor-pointer">
            Lens 2: Grid &amp; Supergrid (3)
          </button>
          <button id="hpTelemetryLensBtnMarket" type="button" onclick="switchHomepageTelemetryLens('market')" class="telemetry-lens-btn px-3 py-1.5 rounded-lg font-semibold transition-all text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white cursor-pointer">
            Lens 3: Market &amp; E-Mobility (3)
          </button>
        </div>
        <div class="text-[11px] font-mono text-slate-500 dark:text-slate-400 hidden sm:block">
          Interactive analytical telemetry &middot; Horizon 2026&ndash;2050
        </div>
      </div>
"""

# Lens 1: Generation & Trajectory (Charts 01, 02, 05, 06)
lens1_group = f"""      <!-- ================================================================ -->
      <!-- LENS 1: GENERATION & PDP8 TRAJECTORY (CHARTS 01, 02, 05, 06)       -->
      <!-- ================================================================ -->
      <div id="telemetryLensGroupGeneration" class="space-y-4">
        <div class="p-3 rounded-xl bg-teal-500/5 dark:bg-teal-500/10 border border-teal-500/20 text-xs text-slate-700 dark:text-slate-300 font-light flex flex-col sm:flex-row sm:items-center justify-between gap-2">
          <div class="flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-teal-500"></span>
            <span><strong>Generation Trajectory Takeaway</strong>: PDP8 target of 150 GW by 2030 requires $134.7B generation capital, shifting baseload from coal to LNG and offshore wind.</span>
          </div>
          <span class="font-mono text-[10px] text-teal-600 dark:text-teal-400 font-semibold shrink-0">4 Active Models</span>
        </div>

        {row1_content}

        {row3_content}
      </div>
"""

# Lens 2: Grid & Supergrid (Charts 03, 07, 10)
chart10_full = chart10_div.replace("lg:col-span-6", "lg:col-span-12", 1)

lens2_group = f"""      <!-- ================================================================ -->
      <!-- LENS 2: GRID CORRIDORS & REGIONAL INTERTIES (CHARTS 03, 07, 10)   -->
      <!-- ================================================================ -->
      <div id="telemetryLensGroupGrid" class="space-y-4">
        <div class="p-3 rounded-xl bg-blue-500/5 dark:bg-blue-500/10 border border-blue-500/20 text-xs text-slate-700 dark:text-slate-300 font-light flex flex-col sm:flex-row sm:items-center justify-between gap-2">
          <div class="flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-blue-500"></span>
            <span><strong>Grid Supergrid Takeaway</strong>: North-to-South 500kV corridors transmit 3.2 GW inter-regional power flow, connecting Central/Southern renewable hubs to northern industrial centers.</span>
          </div>
          <span class="font-mono text-[10px] text-blue-600 dark:text-blue-400 font-semibold shrink-0">3 Active Models</span>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-4">
          {chart03_div}
          {chart07_div}
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-4">
          {chart10_full}
        </div>
      </div>
"""

# Lens 3: Market & Infrastructure (Charts 04, 08, 09)
chart09_full = chart09_div.replace("lg:col-span-6", "lg:col-span-12", 1)

lens3_group = f"""      <!-- ================================================================ -->
      <!-- LENS 3: MARKET & E-MOBILITY INFRASTRUCTURE (CHARTS 04, 08, 09)     -->
      <!-- ================================================================ -->
      <div id="telemetryLensGroupMarket" class="space-y-4">
        <div class="p-3 rounded-xl bg-amber-500/5 dark:bg-amber-500/10 border border-amber-500/20 text-xs text-slate-700 dark:text-slate-300 font-light flex flex-col sm:flex-row sm:items-center justify-between gap-2">
          <div class="flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-amber-500"></span>
            <span><strong>Market &amp; E-Mobility Takeaway</strong>: Decree 80 DPPA establishes bilateral renewable offtake while 22,055+ EV charging ports build national highway density.</span>
          </div>
          <span class="font-mono text-[10px] text-amber-600 dark:text-amber-400 font-semibold shrink-0">3 Active Models</span>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-4">
          {chart04_div}
          {chart08_div}
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-4">
          {chart09_full}
        </div>
      </div>
"""

# WORKSTATION VIEW 2: TELEMETRY
view_telemetry = f"""
    <!-- ================================================================== -->
    <!-- WORKSTATION VIEW 2: 10-MODULE VISUAL TELEMETRY SUITE               -->
    <!-- ================================================================== -->
    <div id="workstationViewTelemetry" class="space-y-6 hidden">
      {telemetry_header_and_kpis}

{lens_switcher}

{lens1_group}

{lens2_group}

{lens3_group}

      </section>
    </div>
"""

# Extract Simulator and Bento Console
sim_content_raw = text[idx_sim:idx_console].strip()
if sim_content_raw.endswith("</section>"):
    sim_content_raw = sim_content_raw[:-10].strip()

console_content_raw = text[idx_console:idx_main_end].strip()

# WORKSTATION VIEW 3: SIMULATOR & HUBS
view_simulator = f"""
    <!-- ================================================================== -->
    <!-- WORKSTATION VIEW 3: DECREE 80 DPPA SIMULATOR & HUBS                -->
    <!-- ================================================================== -->
    <div id="workstationViewSimulator" class="space-y-6 hidden">
      <section class="space-y-4" id="decree80SimulatorSection">
{sim_content_raw}
      </section>

{console_content_raw}
    </div>
"""

# Now assemble main body
new_main = f"""{head_and_hero.rstrip()}

{workstation_switcher}

{view_overview}

{view_telemetry}

{view_simulator}
  </main>
"""

# Script portion (from </main> onwards)
script_section = text[idx_main_end + len("</main>"):].strip()

# JavaScript enhancements for Workstation & Lens controllers
js_controllers = """
    // ========================================================================
    // WORKSTATION ARCHITECTURE & TELEMETRY LENS CONTROLLERS
    // ========================================================================
    let activeHomepageWorkstation = 'overview';
    let activeHomepageLens = 'all';
    let chartsInitialized = false;

    function switchHomepageWorkstation(mode, scrollToTop = false) {
      activeHomepageWorkstation = mode;

      const viewOverview = document.getElementById('workstationViewOverview');
      const viewTelemetry = document.getElementById('workstationViewTelemetry');
      const viewSimulator = document.getElementById('workstationViewSimulator');

      const btnOverview = document.getElementById('hpModeBtnOverview');
      const btnTelemetry = document.getElementById('hpModeBtnTelemetry');
      const btnSimulator = document.getElementById('hpModeBtnSimulator');
      const statusLabel = document.getElementById('activeWorkstationStatusLabel');

      const activeClasses = 'hp-mode-btn flex items-center gap-2 px-3.5 py-2 rounded-lg font-semibold transition-all bg-white dark:bg-slate-700/80 text-teal-600 dark:text-teal-400 shadow-xs cursor-pointer';
      const inactiveClasses = 'hp-mode-btn flex items-center gap-2 px-3.5 py-2 rounded-lg font-semibold transition-all text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white cursor-pointer';

      [btnOverview, btnTelemetry, btnSimulator].forEach(btn => {
        if (btn) btn.className = inactiveClasses;
      });

      if (viewOverview) viewOverview.classList.add('hidden');
      if (viewTelemetry) viewTelemetry.classList.add('hidden');
      if (viewSimulator) viewSimulator.classList.add('hidden');

      if (mode === 'telemetry') {
        if (viewTelemetry) viewTelemetry.classList.remove('hidden');
        if (btnTelemetry) btnTelemetry.className = activeClasses;
        if (statusLabel) statusLabel.textContent = 'Mode: 10-Module Telemetry Suite';
        history.replaceState(null, null, '#telemetry');

        // Lazy chart initialization on first activation
        if (!chartsInitialized) {
          safeInitCharts();
          chartsInitialized = true;
        } else {
          resizeActiveCharts();
        }
      } else if (mode === 'simulator') {
        if (viewSimulator) viewSimulator.classList.remove('hidden');
        if (btnSimulator) btnSimulator.className = activeClasses;
        if (statusLabel) statusLabel.textContent = 'Mode: Decree 80 DPPA Simulator & Hubs';
        history.replaceState(null, null, '#simulator');
        updateSimulator();
      } else {
        // default overview
        if (viewOverview) viewOverview.classList.remove('hidden');
        if (btnOverview) btnOverview.className = activeClasses;
        if (statusLabel) statusLabel.textContent = 'Mode: Executive Overview & 12 Pillars';
        history.replaceState(null, null, '#overview');
      }

      if (scrollToTop) {
        const switcher = document.getElementById('homepageWorkstationSwitcher');
        if (switcher) switcher.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }

    function switchHomepageTelemetryLens(lens) {
      activeHomepageLens = lens;

      const btnAll = document.getElementById('hpTelemetryLensBtnAll');
      const btnGen = document.getElementById('hpTelemetryLensBtnGen');
      const btnGrid = document.getElementById('hpTelemetryLensBtnGrid');
      const btnMarket = document.getElementById('hpTelemetryLensBtnMarket');

      const gGen = document.getElementById('telemetryLensGroupGeneration');
      const gGrid = document.getElementById('telemetryLensGroupGrid');
      const gMarket = document.getElementById('telemetryLensGroupMarket');

      const activeBtnClass = 'telemetry-lens-btn px-3 py-1.5 rounded-lg font-semibold transition-all bg-white dark:bg-slate-700/80 text-teal-600 dark:text-teal-400 shadow-xs cursor-pointer';
      const inactiveBtnClass = 'telemetry-lens-btn px-3 py-1.5 rounded-lg font-semibold transition-all text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white cursor-pointer';

      [btnAll, btnGen, btnGrid, btnMarket].forEach(btn => {
        if (btn) btn.className = inactiveBtnClass;
      });

      if (lens === 'generation') {
        if (btnGen) btnGen.className = activeBtnClass;
        if (gGen) gGen.classList.remove('hidden');
        if (gGrid) gGrid.classList.add('hidden');
        if (gMarket) gMarket.classList.add('hidden');
      } else if (lens === 'grid') {
        if (btnGrid) btnGrid.className = activeBtnClass;
        if (gGen) gGen.classList.add('hidden');
        if (gGrid) gGrid.classList.remove('hidden');
        if (gMarket) gMarket.classList.add('hidden');
      } else if (lens === 'market') {
        if (btnMarket) btnMarket.className = activeBtnClass;
        if (gGen) gGen.classList.add('hidden');
        if (gGrid) gGrid.classList.add('hidden');
        if (gMarket) gMarket.classList.remove('hidden');
      } else {
        // all
        if (btnAll) btnAll.className = activeBtnClass;
        if (gGen) gGen.classList.remove('hidden');
        if (gGrid) gGrid.classList.remove('hidden');
        if (gMarket) gMarket.classList.remove('hidden');
      }

      resizeActiveCharts();
    }

    function resizeActiveCharts() {
      setTimeout(() => {
        [
          trajectoryChartInstance, pdp8ChartInstance, regionalRadarChartInstance,
          evChartInstance, dailyDispatchChartInstance, capexAllocationChartInstance,
          substationHierarchyChartInstance, marketClearingChartInstance,
          topProvincesEcoparkChartInstance
        ].forEach(inst => {
          if (inst && typeof inst.resize === 'function') {
            try { inst.resize(); } catch (e) {}
          }
        });
      }, 50);
    }
"""

if "function safeInitCharts(attempts = 0) {" in script_section:
    script_section = script_section.replace("function safeInitCharts(attempts = 0) {", js_controllers + "\n    function safeInitCharts(attempts = 0) {")

old_init_block = """    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', () => safeInitCharts());
    } else {
      safeInitCharts();
    }
    window.addEventListener('load', () => safeInitCharts());"""

new_init_block = """    // Workstation Hash Routing & Lazy Chart Init
    function initWorkstationRouting() {
      const initHash = window.location.hash.replace('#', '').toLowerCase();
      if (['overview', 'telemetry', 'simulator'].includes(initHash)) {
        switchHomepageWorkstation(initHash);
      } else {
        switchHomepageWorkstation('overview');
      }

      window.addEventListener('hashchange', () => {
        const h = window.location.hash.replace('#', '').toLowerCase();
        if (['overview', 'telemetry', 'simulator'].includes(h) && h !== activeHomepageWorkstation) {
          switchHomepageWorkstation(h);
        }
      });
    }

    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', initWorkstationRouting);
    } else {
      initWorkstationRouting();
    }"""

if old_init_block in script_section:
    script_section = script_section.replace(old_init_block, new_init_block)

final_html = new_main + "\n  " + script_section

rev_file = "RenewableVietNam/index_Rev.028.html"
with open(rev_file, "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"Successfully generated {rev_file} ({len(final_html)} bytes)")
