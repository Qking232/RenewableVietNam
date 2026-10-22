import os
import hashlib
import re

REPOS = [
    r"G:\My Drive\7. AI\Gemini\RenewableVietNam",
    r"G:\My Drive\7. AI\Gemini\Qking232.github.io"
]

def sha256_file(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

# -----------------------------------------------------------------------------
# 1. READ BASE FILES
# -----------------------------------------------------------------------------
energy_path = os.path.join(REPOS[0], "projectenergy", "index.html")
with open(energy_path, "r", encoding="utf-8") as f:
    energy_html = f.read()

index_path = os.path.join(REPOS[0], "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

ev_path = os.path.join(REPOS[0], "evcharging", "index.html")
with open(ev_path, "r", encoding="utf-8") as f:
    ev_html = f.read()

calc_path = os.path.join(REPOS[0], "calculator", "index.html")
with open(calc_path, "r", encoding="utf-8") as f:
    calc_html = f.read()

# -----------------------------------------------------------------------------
# 2. PDP8 COMPONENTS TO INJECT INTO ENERGY MAP
# -----------------------------------------------------------------------------
pdp8_gauges_section = '''
    <!-- SECTOR PROGRESS METERS: STATUTORY PDP8 2030 TRAJECTORY & ACTIVE FLEET -->
    <section class="p-5 rounded-2xl bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder shadow-sm space-y-4">
      <div class="flex items-center justify-between pb-2 border-b border-borderSlate dark:border-darkBorder">
        <h3 class="font-mono text-xs uppercase tracking-wider font-bold text-inkPrimary dark:text-textDarkPrimary flex items-center gap-2">
          <span class="w-2 h-2 rounded-full bg-teal-500"></span>
          Statutory Fuel Trajectory &amp; Operationalization Delta (MW)
        </h3>
        <span class="font-mono text-[10px] text-inkMuted dark:text-textDarkMuted">Solid = Operational &middot; Striped = Pipeline Required</span>
      </div>

      <div id="pdp8SectorGauges" class="space-y-3.5">
        <!-- Dynamically populated via loadPdp8Data() -->
      </div>
    </section>
'''

pdp8_projects_section = '''
    <!-- STATUTORY PRIORITY CAPITAL PROJECTS PIPELINE (DECISION 262/QD-TTg) -->
    <section class="p-5 rounded-2xl bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder shadow-sm space-y-4">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-2 border-b border-borderSlate dark:border-darkBorder">
        <div>
          <h3 class="font-mono text-xs uppercase tracking-wider font-bold text-inkPrimary dark:text-textDarkPrimary flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
            Statutory Priority Project Pipeline (Decision 262/QD-TTg Implementation)
          </h3>
          <p class="text-xs text-inkMuted dark:text-textDarkMuted font-light mt-0.5">
            Nationally prioritized utility-scale clean generation, LNG baseload, and pumped storage projects scheduled for 2026–2030 COD.
          </p>
        </div>

        <!-- Filter by Fuel -->
        <div class="flex flex-wrap items-center gap-1.5 font-mono text-[10px]">
          <span class="text-inkMuted dark:text-textDarkMuted uppercase">Filter:</span>
          <button onclick="filterPdp8Projects('all')" class="pdp8-proj-filter px-2 py-1 rounded bg-teal-600 text-white font-medium cursor-pointer" data-filter="all">All (10)</button>
          <button onclick="filterPdp8Projects('Offshore Wind')" class="pdp8-proj-filter px-2 py-1 rounded bg-slate-100 dark:bg-darkCard text-inkPrimary dark:text-textDarkMuted hover:bg-slate-200 cursor-pointer" data-filter="Offshore Wind">Offshore Wind</button>
          <button onclick="filterPdp8Projects('LNG')" class="pdp8-proj-filter px-2 py-1 rounded bg-slate-100 dark:bg-darkCard text-inkPrimary dark:text-textDarkMuted hover:bg-slate-200 cursor-pointer" data-filter="LNG">LNG Baseload</button>
          <button onclick="filterPdp8Projects('Hydropower')" class="pdp8-proj-filter px-2 py-1 rounded bg-slate-100 dark:bg-darkCard text-inkPrimary dark:text-textDarkMuted hover:bg-slate-200 cursor-pointer" data-filter="Hydropower">Hydro &amp; Storage</button>
        </div>
      </div>

      <!-- Project Cards Grid -->
      <div id="pdp8ProjectsGrid" class="grid grid-cols-1 md:grid-cols-2 gap-3.5">
        <!-- Dynamically populated via loadPdp8Data() -->
      </div>
    </section>
'''

pdp8_js_code = '''
    // =========================================================================
    // PDP8 STATUTORY DATASET & CAPITAL PIPELINE ENGINE
    // =========================================================================
    let pdp8Dataset = null;
    let activePdp8Filter = "all";

    async function loadPdp8Data() {
      try {
        const res = await fetch("/data/pdp8_targets.json?t=" + Date.now());
        if (!res.ok) throw new Error("Status " + res.status);
        pdp8Dataset = await res.json();
        renderPdp8Gauges();
        renderPdp8Projects();
      } catch (e) {
        console.warn("PDP8 JSON fetch error:", e);
      }
    }

    function renderPdp8Gauges() {
      const container = document.getElementById("pdp8SectorGauges");
      if (!container || !pdp8Dataset || !pdp8Dataset.fuel_targets) return;

      let html = "";
      pdp8Dataset.fuel_targets.forEach(item => {
        const opPct = Math.min(100, Math.round((item.current_operating_mw / item.target_2030_mw) * 100));
        const pipePct = Math.min(100 - opPct, Math.round((item.pipeline_mw / item.target_2030_mw) * 100));

        html += `
          <div class="space-y-1.5 font-mono text-xs">
            <div class="flex items-center justify-between text-inkPrimary dark:text-textDarkPrimary">
              <span class="font-semibold flex items-center gap-1.5">
                <span class="w-2 h-2 rounded-full" style="background-color: ${item.hex}"></span>
                ${item.fuel}
              </span>
              <span class="text-[11px] text-inkMuted dark:text-textDarkMuted">
                <b class="text-inkPrimary dark:text-textDarkPrimary font-bold">${item.current_operating_mw.toLocaleString()}</b> / ${item.target_2030_mw.toLocaleString()} MW 
                <span class="text-teal-600 dark:text-teal-400 font-bold ml-1">(${opPct}%)</span>
              </span>
            </div>
            <!-- Dual Progress Bar -->
            <div class="w-full h-3 rounded-full bg-slate-100 dark:bg-darkCard overflow-hidden flex border border-borderSlate/60 dark:border-darkBorder/60 shadow-inner">
              <div class="h-full transition-all duration-700" style="width: ${opPct}%; background-color: ${item.hex};" title="Operating: ${item.current_operating_mw} MW (${opPct}%)"></div>
              <div class="h-full opacity-60 transition-all duration-700" style="width: ${pipePct}%; background-color: ${item.hex}; background-image: repeating-linear-gradient(45deg, transparent, transparent 4px, rgba(255,255,255,0.3) 4px, rgba(255,255,255,0.3) 8px);" title="Pipeline: ${item.pipeline_mw} MW"></div>
            </div>
            <div class="flex items-center justify-between text-[10px] text-inkMuted dark:text-textDarkMuted">
              <span class="truncate max-w-[70%] text-[10px] text-slate-400 dark:text-slate-500">${item.status_note}</span>
              <span>Target Share: <b>${item.target_share_pct}%</b></span>
            </div>
          </div>
        `;
      });

      container.innerHTML = html;
    }

    function renderPdp8Projects() {
      const container = document.getElementById("pdp8ProjectsGrid");
      if (!container || !pdp8Dataset || !pdp8Dataset.priority_projects) return;

      const filtered = pdp8Dataset.priority_projects.filter(p => {
        if (activePdp8Filter === "all") return true;
        if (activePdp8Filter === "Hydropower") return p.fuel.includes("Hydro");
        return p.fuel.includes(activePdp8Filter);
      });

      let html = "";
      filtered.forEach(p => {
        const isConstruction = p.status.includes("Construction") || p.status.includes("Testing");
        const badgeColor = isConstruction ? "bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border-emerald-500/20" : "bg-amber-500/10 text-amber-600 dark:text-amber-400 border-amber-500/20";

        html += `
          <div class="p-3.5 rounded-xl bg-slate-50/80 dark:bg-darkCard/80 border border-borderSlate dark:border-darkBorder hover:border-teal-500/50 dark:hover:border-teal-400/40 transition-all flex flex-col justify-between space-y-3">
            <div class="space-y-1.5">
              <div class="flex items-center justify-between font-mono text-[10px]">
                <span class="px-2 py-0.5 rounded border ${badgeColor} font-semibold">${p.status}</span>
                <span class="text-inkMuted dark:text-textDarkMuted">COD: <b class="text-inkPrimary dark:text-textDarkPrimary">${p.target_cod}</b></span>
              </div>
              <h4 class="text-sm font-semibold text-inkPrimary dark:text-textDarkPrimary leading-snug">
                ${p.name}
              </h4>
              <p class="text-xs text-inkMuted dark:text-textDarkMuted font-light line-clamp-2">
                ${p.notes}
              </p>
            </div>

            <div class="pt-2 border-t border-borderSlate/60 dark:border-darkBorder/60 flex items-center justify-between font-mono text-[11px]">
              <div>
                <span class="font-bold text-teal-600 dark:text-teal-400">${p.capacity_mw.toLocaleString()} MW</span>
                <span class="text-slate-300 dark:text-slate-600 mx-1">&middot;</span>
                <span class="text-inkMuted dark:text-textDarkMuted">${p.province}</span>
              </div>
              <button onclick="filterByProjectName('${p.name.split(' ')[0]}')" class="inline-flex items-center gap-1 text-[10px] text-teal-600 dark:text-teal-400 hover:underline font-semibold cursor-pointer">
                <span>View on Table &rarr;</span>
              </button>
            </div>
          </div>
        `;
      });

      container.innerHTML = html;
    }

    function filterPdp8Projects(filterKey) {
      activePdp8Filter = filterKey;
      document.querySelectorAll(".pdp8-proj-filter").forEach(b => {
        if (b.getAttribute("data-filter") === filterKey) {
          b.className = "pdp8-proj-filter px-2 py-1 rounded bg-teal-600 text-white font-medium cursor-pointer";
        } else {
          b.className = "pdp8-proj-filter px-2 py-1 rounded bg-slate-100 dark:bg-darkCard text-inkPrimary dark:text-textDarkMuted hover:bg-slate-200 cursor-pointer";
        }
      });
      renderPdp8Projects();
    }

    function filterByProjectName(keyword) {
      searchQuery = keyword;
      const searchInput = document.getElementById("projectSearchInput");
      if (searchInput) searchInput.value = keyword;
      applyFilters();
      document.getElementById("projectsDirectoryContainer")?.scrollIntoView({ behavior: 'smooth' });
    }
'''

# -----------------------------------------------------------------------------
# 3. BUILD REVISED projectenergy/index.html
# -----------------------------------------------------------------------------
# Title and Hero Header
new_energy = energy_html.replace(
    "<title>Vietnam Clean Energy Projects Map (960 Assets, 80.6 GW) | Renewable Viet Nam</title>",
    "<title>Vietnam PDP8 Clean Energy Map & Statutory Asset Pipeline | Renewable Viet Nam</title>"
).replace(
    "Vietnam Clean Energy Projects Map &amp; Grid Pipeline",
    "Vietnam PDP8 Clean Energy Map &amp; Statutory Asset Pipeline"
).replace(
    "Authoritative geospatial asset registry tracking 960+ utility-scale generation facilities",
    "Authoritative statutory compliance tracker and geospatial asset registry comparing Vietnam's active commercial baseload (80.6 GW across 960 utility assets) against the 150.5 GW statutory capacity mandate under Decision 500/QĐ-TTg and Decision 262/QĐ-TTg"
)

# Standardize Header Nav in projectenergy (PDP8 Energy is active)
old_energy_desktop_nav = re.search(r'<nav class="hidden md:flex items-center gap-1 font-mono text-\[11px\] tracking-wider[^"]*">([\s\S]*?)</nav>', new_energy).group(0)
new_energy_desktop_nav = '''<nav class="hidden md:flex items-center gap-1 font-mono text-[11px] tracking-wider text-inkMuted dark:text-textDarkMuted">
            <a href="/" class="px-2.5 py-1 rounded-md hover:text-teal-600 dark:hover:text-teal-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Industrial Hubs</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/projectenergy/" class="px-2.5 py-1 rounded-md text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20">PDP8 Energy</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/evcharging/" class="px-2.5 py-1 rounded-md hover:text-amber-600 dark:hover:text-amber-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">EV Stations</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/calculator/" class="px-2.5 py-1 rounded-md hover:text-teal-600 dark:hover:text-teal-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Power Sizer &amp; Tariffs</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/hub/" class="px-2.5 py-1 rounded-md hover:text-sky-600 dark:hover:text-sky-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">The Library</a>
          </nav>'''
new_energy = new_energy.replace(old_energy_desktop_nav, new_energy_desktop_nav, 1)

old_energy_mobile_nav = re.search(r'<nav class="flex md:hidden items-center gap-1.5 overflow-x-auto no-scrollbar pt-1.5 pb-0.5 font-mono text-\[11px\] tracking-wider whitespace-nowrap w-full[^"]*">([\s\S]*?)</nav>', new_energy).group(0)
new_energy_mobile_nav = '''<nav class="flex md:hidden items-center gap-1.5 overflow-x-auto no-scrollbar pt-1.5 pb-0.5 font-mono text-[11px] tracking-wider whitespace-nowrap w-full -mx-3 px-3 sm:mx-0 sm:px-0">
        <a href="/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-teal-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">Industrial Hubs</a>
        <a href="/projectenergy/" class="px-2.5 py-1.5 rounded-lg text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20 shrink-0">PDP8 Energy</a>
        <a href="/evcharging/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-amber-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">EV Stations</a>
        <a href="/calculator/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-teal-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">Power Sizer</a>
        <a href="/hub/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-sky-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">The Library</a>
      </nav>'''
new_energy = new_energy.replace(old_energy_mobile_nav, new_energy_mobile_nav, 1)

# Inject PDP8 gauges section right after the 4-metric grid (before the map)
# The 4-metric grid ends with </section> around line 125
metric_section_end = '</section>\n\n    <!-- INTERACTIVE GEOSPATIAL MAP COCKPIT'
new_energy = new_energy.replace(
    metric_section_end,
    '</section>\n\n' + pdp8_gauges_section.strip() + '\n\n    <!-- INTERACTIVE GEOSPATIAL MAP COCKPIT',
    1
)

# Inject PDP8 priority projects section right before the facilities directory
directory_section_start = '<!-- CLEAN GENERATION FACILITIES DIRECTORY &amp; SCREENER TABLE -->'
new_energy = new_energy.replace(
    directory_section_start,
    pdp8_projects_section.strip() + '\n\n    <!-- CLEAN GENERATION FACILITIES DIRECTORY & SCREENER TABLE -->',
    1
)

# Inject PDP8 JS before loadProjectsData() call in DOMContentLoaded
new_energy = new_energy.replace(
    'document.addEventListener("DOMContentLoaded", () => {\n      loadProjectsData();\n    });',
    pdp8_js_code.strip() + '\n\n    document.addEventListener("DOMContentLoaded", () => {\n      loadProjectsData();\n      loadPdp8Data();\n    });',
    1
)

# -----------------------------------------------------------------------------
# 4. STANDARDIZE NAV IN index.html, evcharging/index.html, calculator/index.html
# -----------------------------------------------------------------------------
def update_nav_links(html, active_tab):
    # Desktop nav
    hubs_cls = 'px-2.5 py-1 rounded-md text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20' if active_tab == 'hubs' else 'px-2.5 py-1 rounded-md hover:text-teal-600 dark:hover:text-teal-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors'
    energy_cls = 'px-2.5 py-1 rounded-md text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20' if active_tab == 'energy' else 'px-2.5 py-1 rounded-md hover:text-emerald-600 dark:hover:text-emerald-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors'
    ev_cls = 'px-2.5 py-1 rounded-md text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20' if active_tab == 'ev' else 'px-2.5 py-1 rounded-md hover:text-amber-600 dark:hover:text-amber-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors'
    calc_cls = 'px-2.5 py-1 rounded-md text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20' if active_tab == 'calc' else 'px-2.5 py-1 rounded-md hover:text-teal-600 dark:hover:text-teal-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors'

    target_desktop_nav = f'''<nav class="hidden md:flex items-center gap-1 font-mono text-[11px] tracking-wider text-inkMuted dark:text-textDarkMuted">
            <a href="/" class="{hubs_cls}">Industrial Hubs</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/projectenergy/" class="{energy_cls}">PDP8 Energy</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/evcharging/" class="{ev_cls}">EV Stations</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/calculator/" class="{calc_cls}">Power Sizer &amp; Tariffs</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/hub/" class="px-2.5 py-1 rounded-md hover:text-sky-600 dark:hover:text-sky-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">The Library</a>
          </nav>'''

    # Mobile nav
    hubs_m_cls = 'px-2.5 py-1.5 rounded-lg text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20 shrink-0' if active_tab == 'hubs' else 'px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-teal-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0'
    energy_m_cls = 'px-2.5 py-1.5 rounded-lg text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20 shrink-0' if active_tab == 'energy' else 'px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-emerald-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0'
    ev_m_cls = 'px-2.5 py-1.5 rounded-lg text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20 shrink-0' if active_tab == 'ev' else 'px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-amber-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0'
    calc_m_cls = 'px-2.5 py-1.5 rounded-lg text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20 shrink-0' if active_tab == 'calc' else 'px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-teal-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0'

    target_mobile_nav = f'''<nav class="flex md:hidden items-center gap-1.5 overflow-x-auto no-scrollbar pt-1.5 pb-0.5 font-mono text-[11px] tracking-wider whitespace-nowrap w-full -mx-3 px-3 sm:mx-0 sm:px-0">
        <a href="/" class="{hubs_m_cls}">Industrial Hubs</a>
        <a href="/projectenergy/" class="{energy_m_cls}">PDP8 Energy</a>
        <a href="/evcharging/" class="{ev_m_cls}">EV Stations</a>
        <a href="/calculator/" class="{calc_m_cls}">Power Sizer</a>
        <a href="/hub/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-sky-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">The Library</a>
      </nav>'''

    # Replace desktop nav
    cur_desk = re.search(r'<nav class="hidden md:flex items-center gap-1 font-mono text-\[11px\] tracking-wider[^"]*">[\s\S]*?</nav>', html)
    if cur_desk:
        html = html.replace(cur_desk.group(0), target_desktop_nav, 1)

    # Replace mobile nav
    cur_mob = re.search(r'<nav class="flex md:hidden items-center gap-1.5 overflow-x-auto no-scrollbar pt-1.5 pb-0.5 font-mono text-\[11px\] tracking-wider whitespace-nowrap w-full[^"]*">[\s\S]*?</nav>', html)
    if cur_mob:
        html = html.replace(cur_mob.group(0), target_mobile_nav, 1)

    return html

new_index = update_nav_links(index_html, 'hubs')
# Remove PDP8 hero badge in index
new_index = re.sub(
    r'<a href="/pdp8/" class="font-mono text-\[10px\] sm:text-\[11px\] text-inkMuted dark:text-textDarkMuted bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder hover:border-teal-500 dark:hover:border-teal-400/50 p-2.5 rounded-xl shrink-0 shadow-sm transition-all flex items-center gap-1.5 group">[\s\S]*?</a>',
    '''<div class="font-mono text-[10px] sm:text-[11px] text-inkMuted dark:text-textDarkMuted bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder p-2.5 rounded-xl shrink-0 shadow-sm flex items-center gap-1.5">
          <span class="inline-block w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
          <span>ECO-INDUSTRIAL SITING REGISTRY &middot; 2026</span>
        </div>''',
    new_index
)

new_ev = update_nav_links(ev_html, 'ev')
new_calc = update_nav_links(calc_html, 'calc')

# Redirect for /pdp8/
pdp8_redirect_html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; url=/projectenergy/">
  <link rel="canonical" href="https://renewablevietnam.com/projectenergy/">
  <title>Redirecting to PDP8 Energy | Renewable Viet Nam</title>
  <script>
    window.location.replace("/projectenergy/");
  </script>
</head>
<body style="background:#0a0d12; color:#94a3b8; font-family:monospace; display:flex; flex-direction:column; align-items:center; justify-content:center; height:100vh; margin:0; text-align:center;">
  <h2>Relocating to PDP8 Energy...</h2>
  <p>The PDP8 Statutory Tracker and Clean Energy Map are now unified at <a href="/projectenergy/" style="color:#2dd4bf; text-decoration:underline;">/projectenergy/ &rarr;</a></p>
</body>
</html>
'''

# -----------------------------------------------------------------------------
# 5. WRITE TO BOTH REPOSITORIES
# -----------------------------------------------------------------------------
files_map = {
    "projectenergy/index.html": new_energy,
    "index.html": new_index,
    "green/index.html": new_index, # identical mirror
    "evcharging/index.html": new_ev,
    "calculator/index.html": new_calc,
    "pdp8/index.html": pdp8_redirect_html
}

for repo in REPOS:
    for rel_path, content in files_map.items():
        dest = os.path.join(repo, rel_path.replace("/", os.sep))
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        print(f"Wrote {dest} ({len(content)} chars)")

print("\n--- Verifying SHA256 parity ---")
all_ok = True
for rel_path in files_map.keys():
    h1 = sha256_file(os.path.join(REPOS[0], rel_path.replace("/", os.sep)))
    h2 = sha256_file(os.path.join(REPOS[1], rel_path.replace("/", os.sep)))
    match = (h1 == h2)
    print(f"[{'MATCH' if match else 'MISMATCH'}] {rel_path} -> {h1[:12]}")
    if not match:
        all_ok = False

if all_ok:
    print("\nALL FILES 100% SYNCHRONIZED & PARITY VERIFIED!")
else:
    raise RuntimeError("SHA256 Parity Mismatch detected!")
