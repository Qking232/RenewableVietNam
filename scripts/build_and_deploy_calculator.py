import os
import re

REPOS = [
    "G:/My Drive/7. AI/Gemini/RenewableVietNam",
    "G:/My Drive/7. AI/Gemini/Qking232.github.io"
]

ROOT_INDEX = "G:/My Drive/7. AI/Gemini/RenewableVietNam/index.html"
with open(ROOT_INDEX, "r", encoding="utf-8") as f:
    orig_html = f.read()

# -------------------------------------------------------------
# 1. BUILD calculator/index.html
# -------------------------------------------------------------
# Extract the calculator section markup from <section id="calculator"> to </section>
sec_match = re.search(r'(<section id="calculator".*?</section>)', orig_html, re.DOTALL)
if not sec_match:
    raise ValueError("Could not find section#calculator in index.html!")

calc_section = sec_match.group(1)

# In calculator/index.html, we improve the layout on large screens:
# Replace grid-cols-1 with grid-cols-1 lg:grid-cols-2 inside each tab container
# Tab 1:
calc_section_enhanced = calc_section.replace(
    '<div class="grid grid-cols-1 gap-4 items-start">\n        <!-- Sliders Form -->',
    '<div class="grid grid-cols-1 lg:grid-cols-2 gap-6 items-start">\n        <!-- Sliders Form -->'
)
# Tab 2:
calc_section_enhanced = calc_section_enhanced.replace(
    '<div class="grid grid-cols-1 gap-4 items-start">\n          <!-- Left Column: Appliance Inventory & Daily Usage Modeler -->',
    '<div class="grid grid-cols-1 lg:grid-cols-2 gap-6 items-start">\n          <!-- Left Column: Appliance Inventory & Daily Usage Modeler -->'
)
# Tab 3:
calc_section_enhanced = calc_section_enhanced.replace(
    '<div class="grid grid-cols-1 gap-4 items-start">\n          <!-- Interactive Parameter Controls (Left Column) -->',
    '<div class="grid grid-cols-1 lg:grid-cols-2 gap-6 items-start">\n          <!-- Interactive Parameter Controls (Left Column) -->'
)

# Extract FALLBACK_HUBS
start_hubs = orig_html.find("const FALLBACK_HUBS = [")
end_hubs = orig_html.find("let HUBS = [...FALLBACK_HUBS];") + len("let HUBS = [...FALLBACK_HUBS];")
hubs_js = orig_html[start_hubs:end_hubs]

# Extract Calculator JS (functions & algorithms)
start_calc_fn = orig_html.find("function updateCalculator() {")
end_calc_fn = orig_html.find("document.addEventListener(\"DOMContentLoaded\", () => {")
calc_functions_js = orig_html[start_calc_fn:end_calc_fn]

# Extract Calculator event listeners & initialization
start_tab_init = orig_html.find("// Calculator Suite Tab Switcher")
end_evn_listeners = orig_html.find("// ====================================================================\n      // REAL-TIME INDUSTRY NEWS WIRE CONTROLLER")
# We also need the 3 calcDemandSlider listeners
calc_sliders_chunk = """
      document.getElementById("calcDemandSlider")?.addEventListener("input", updateCalculator);
      document.getElementById("calcMwhSlider")?.addEventListener("input", updateCalculator);
      document.getElementById("calcReSlider")?.addEventListener("input", updateCalculator);
"""

calculator_html = f"""<!DOCTYPE html>
<html lang="en" class="dark scroll-smooth">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
  <title>Vietnam Clean Energy Sizing &amp; EVN Tariff Suite — Renewable Vietnam</title>
  <meta name="description" content="Institutional modeling suite for corporate DPPA clean power siting, EVN statutory 6-tier progressive retail tariffs, and European Green Deal CBAM carbon compliance." />
  <link rel="canonical" href="https://renewablevietnam.com/calculator/" />

  <!-- Fonts: Inter & JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet" />

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['Inter', 'system-ui', 'sans-serif'],
            mono: ['"JetBrains Mono"', 'monospace'],
          }},
          colors: {{
            obsidian: '#070A12',
            darkSurface: '#0D1322',
            darkCard: '#131B2E',
            darkBorder: '#1F293D',
            borderSlate: '#E2E8F0',
            alabaster: '#F8FAFC',
            inkPrimary: '#0F172A',
            inkMuted: '#64748B',
            textDarkPrimary: '#F1F5F9',
            textDarkMuted: '#94A3B8',
          }}
        }}
      }}
    }};
  </script>

  <!-- Theme Initialization -->
  <script>
    (function () {{
      var theme = localStorage.getItem('rvn-theme') || 'dark';
      if (theme === 'dark') {{
        document.documentElement.classList.add('dark');
      }} else {{
        document.documentElement.classList.remove('dark');
      }}
    }})();
  </script>

  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="icon" href="/assets/images/favicon.ico" sizes="any">
  <link rel="icon" type="image/png" href="/assets/images/favicon-32.png" sizes="32x32">
  <link rel="icon" type="image/png" href="/assets/images/favicon.png" sizes="180x180">
  <link rel="apple-touch-icon" href="/assets/images/apple-touch-icon.png">
</head>

<body class="min-h-screen text-inkPrimary dark:text-textDarkPrimary antialiased bg-alabaster dark:bg-obsidian font-sans selection:bg-teal-500 selection:text-white dark:selection:bg-teal-400 dark:selection:text-obsidian transition-colors duration-500 flex flex-col justify-between p-4 sm:p-6 lg:p-8">

  <!-- ==================================================================== -->
  <!-- TOP EXECUTIVE NAVIGATION BAR                                        -->
  <!-- ==================================================================== -->
  <header class="relative z-20 w-full max-w-7xl mx-auto flex items-center justify-between pb-6 border-b border-borderSlate dark:border-darkBorder">
    <div class="flex items-center gap-6">
      <a href="/" class="flex items-center gap-3 group" aria-label="Renewable Vietnam — home">
        <img src="/assets/images/logo.svg" alt="Renewable Viet Nam Mark" width="34" height="34" class="w-8.5 h-8.5 rounded-lg shrink-0 shadow-sm" />
        <span class="text-[11px] sm:text-xs font-mono uppercase tracking-[0.16em] sm:tracking-[0.24em] text-inkPrimary dark:text-textDarkPrimary font-semibold">
          RENEWABLE INFRASTRUCTURE
        </span>
      </a>

      <!-- Quick Inter-Domain Jump Navigation -->
      <nav class="hidden md:flex items-center gap-1 font-mono text-[11px] tracking-wider text-inkMuted dark:text-textDarkMuted">
        <a href="/" class="px-2.5 py-1 rounded-md hover:text-teal-600 dark:hover:text-teal-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Industrial Hubs</a>
        <span class="text-slate-300 dark:text-slate-700">&middot;</span>
        <a href="/projectenergy/" class="px-2.5 py-1 rounded-md hover:text-emerald-600 dark:hover:text-emerald-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Energy Map</a>
        <span class="text-slate-300 dark:text-slate-700">&middot;</span>
        <a href="/evcharging/" class="px-2.5 py-1 rounded-md hover:text-amber-600 dark:hover:text-amber-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">EV Stations</a>
        <span class="text-slate-300 dark:text-slate-700">&middot;</span>
        <a href="/calculator/" class="px-2.5 py-1 rounded-md text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20">Power Sizer &amp; Tariffs</a>
        <span class="text-slate-300 dark:text-slate-700">&middot;</span>
        <a href="/hub/" class="px-2.5 py-1 rounded-md hover:text-sky-600 dark:hover:text-sky-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">The Library</a>
      </nav>
    </div>

    <!-- Right Controls -->
    <div class="flex items-center gap-2">
      <a href="/" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg font-mono text-[11px] text-inkPrimary dark:text-textDarkPrimary bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder hover:border-teal-500 dark:hover:border-teal-400/40 transition-all shadow-sm">
        <svg class="w-3.5 h-3.5 text-teal-500 dark:text-teal-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
        </svg>
        <span>Back to Hubs</span>
      </a>

      <button id="themeToggleBtn" aria-label="Toggle Theme" class="flex items-center justify-center w-8.5 h-8.5 rounded-lg bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder shadow-sm hover:border-slate-400 dark:hover:border-slate-500 text-inkMuted dark:text-textDarkMuted transition-all cursor-pointer">
        <svg id="sunIcon" class="hidden w-4 h-4 text-amber-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.6">
          <path stroke-linecap="round" stroke-linejoin="round" d="M12 3v2.25m6.364.386-1.591 1.591M21 12h-2.25m-.386 6.364-1.591-1.591M12 18.75V21m-4.773-4.227-1.591 1.591M5.25 12H3m4.227-4.773L5.636 5.636M15.75 12a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0Z" />
        </svg>
        <svg id="moonIcon" class="w-4 h-4 text-slate-700" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.6">
          <path stroke-linecap="round" stroke-linejoin="round" d="M21.752 15.002A9.72 9.72 0 0 1 18 15.75c-5.385 0-9.75-4.365-9.75-9.75 0-1.33.266-2.597.748-3.752A9.753 9.753 0 0 0 3 11.25C3 16.635 7.365 21 12.75 21a9.753 9.753 0 0 0 9.002-5.998Z" />
        </svg>
      </button>
    </div>
  </header>

  <!-- ==================================================================== -->
  <!-- MAIN WORKSPACE: FULL PAGE INTERACTIVE CALCULATOR SUITE               -->
  <!-- ==================================================================== -->
  <main class="relative z-10 flex-1 w-full max-w-6xl mx-auto py-6 sm:py-8 space-y-6">
    <!-- Header Hero Banner -->
    <div class="space-y-1">
      <div class="flex items-center gap-2">
        <span class="inline-block w-2.5 h-2.5 rounded-full bg-teal-500 animate-pulse"></span>
        <span class="font-mono text-[11px] uppercase tracking-wider text-teal-600 dark:text-teal-400 font-semibold">
          Decision 2699/QD-BCT &middot; Decree 80/2024 DPPA &middot; Regulation (EU) 2023/956
        </span>
      </div>
      <h1 class="text-2xl sm:text-3xl font-semibold tracking-tight text-inkPrimary dark:text-textDarkPrimary">
        Clean Power Sizer, EVN Tariff &amp; CBAM Suite
      </h1>
      <p class="text-xs sm:text-sm text-inkMuted dark:text-textDarkMuted font-light">
        Engineering-grade quantitative simulators for corporate DPPA siting, statutory EVN residential 6-tier waterfall bills, and European Green Deal CBAM carbon border compliance.
      </p>
    </div>

    {calc_section_enhanced}
  </main>

  <!-- ==================================================================== -->
  <!-- FOOTER                                                               -->
  <!-- ==================================================================== -->
  <footer class="relative z-10 w-full max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-y-2 pt-8 sm:pt-10 border-t border-borderSlate dark:border-darkBorder text-[11px] font-mono text-inkMuted dark:text-textDarkMuted">
    <div class="flex items-center gap-3">
      <span>&copy; 2026 Renewable Viet Nam</span>
      <span>&middot;</span>
      <a href="https://renewablevietnam.com" class="hover:text-inkPrimary dark:hover:text-white transition-colors">renewablevietnam.com</a>
    </div>

    <div class="flex items-center gap-3">
      <a href="/" class="hover:text-inkPrimary dark:hover:text-white transition-colors">Industrial Hubs</a>
      <span>&middot;</span>
      <a href="/projectenergy/" class="hover:text-inkPrimary dark:hover:text-white transition-colors">Energy Map</a>
      <span>&middot;</span>
      <a href="/evcharging/" class="hover:text-inkPrimary dark:hover:text-white transition-colors">EV Stations</a>
      <span>&middot;</span>
      <a href="/hub/" class="hover:text-inkPrimary dark:hover:text-white transition-colors">The Library</a>
      <span>&middot;</span>
      <a href="mailto:info@renewablevietnam.com" class="hover:text-inkPrimary dark:hover:text-white transition-colors">info@renewablevietnam.com</a>
    </div>
  </footer>

  <!-- ==================================================================== -->
  <!-- JAVASCRIPT LOGIC & COMPUTATION ENGINES                               -->
  <!-- ==================================================================== -->
  <script>
    {hubs_js}

    {calc_functions_js}

    document.addEventListener("DOMContentLoaded", () => {{
      updateCalculator();
      updateEvnEstimator();
      updateGreenIndicators();

      // Calculator Suite Tab Switcher
      const tabCorporateSizerBtn = document.getElementById("tabCorporateSizerBtn");
      const tabEvnEstimatorBtn = document.getElementById("tabEvnEstimatorBtn");
      const tabGreenIndicatorBtn = document.getElementById("tabGreenIndicatorBtn");
      const corporateSizerContainer = document.getElementById("corporateSizerContainer");
      const evnEstimatorContainer = document.getElementById("evnEstimatorContainer");
      const greenIndicatorContainer = document.getElementById("greenIndicatorContainer");

      const activateTab = (activeBtn, activeContainer) => {{
        [tabCorporateSizerBtn, tabEvnEstimatorBtn, tabGreenIndicatorBtn].forEach(btn => {{
          if (!btn) return;
          if (btn === activeBtn) {{
            btn.className = "calc-tab-btn py-1.5 px-1 rounded-lg bg-teal-600 text-white font-semibold shadow-sm transition-all cursor-pointer text-center truncate";
          }} else {{
            btn.className = "calc-tab-btn py-1.5 px-1 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-inkPrimary dark:hover:text-white transition-all cursor-pointer text-center truncate";
          }}
        }});
        [corporateSizerContainer, evnEstimatorContainer, greenIndicatorContainer].forEach(c => {{
          if (!c) return;
          if (c === activeContainer) {{
            c.classList.remove("hidden");
          }} else {{
            c.classList.add("hidden");
          }}
        }});
      }};

      if (tabCorporateSizerBtn && tabEvnEstimatorBtn && tabGreenIndicatorBtn) {{
        tabCorporateSizerBtn.addEventListener("click", () => activateTab(tabCorporateSizerBtn, corporateSizerContainer));
        tabEvnEstimatorBtn.addEventListener("click", () => {{
          activateTab(tabEvnEstimatorBtn, evnEstimatorContainer);
          updateEvnEstimator();
        }});
        tabGreenIndicatorBtn.addEventListener("click", () => {{
          activateTab(tabGreenIndicatorBtn, greenIndicatorContainer);
          updateGreenIndicators();
        }});
      }}

      // EVN Region Selection Listeners
      document.querySelectorAll(".evn-region-btn").forEach(btn => {{
        btn.addEventListener("click", () => {{
          evnSelectedRegion = btn.getAttribute("data-evn-region");
          document.querySelectorAll(".evn-region-btn").forEach(b => {{
            b.className = "evn-region-btn px-2.5 py-1.5 rounded-lg bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder text-inkPrimary dark:text-textDarkMuted hover:bg-slate-100 transition-colors cursor-pointer text-center";
          }});
          btn.className = "evn-region-btn px-2.5 py-1.5 rounded-lg bg-teal-600 text-white font-medium transition-colors cursor-pointer text-center";

          const labelEl = document.getElementById("evnRegionLabel");
          if (labelEl) {{
            if (evnSelectedRegion === "south") labelEl.textContent = "Southern Vietnam (Tropical Cooling)";
            else if (evnSelectedRegion === "central") labelEl.textContent = "Central Vietnam (Coastal & High Solar)";
            else if (evnSelectedRegion === "north") labelEl.textContent = "Northern Vietnam (Subtropical & Winter Heating)";
          }}
          updateEvnEstimator();
        }});
      }});

      // EVN Input Sliders & Dropdowns Listeners
      const evnInputs = ["evnAcUnitsSlider", "evnAcHoursSlider", "evnAcTempSelect", "evnFridgeSelect", "evnWaterSlider", "evnCookSlider", "evnWashSlider", "evnElecSlider"];
      evnInputs.forEach(id => {{
        const el = document.getElementById(id);
        if (el) {{
          el.addEventListener("input", updateEvnEstimator);
          el.addEventListener("change", updateEvnEstimator);
        }}
      }});

      // Green Indicators Input Listeners
      const greenInputs = ["greenSectorSelect", "greenMwhSlider", "greenReSlider", "greenEtsSlider"];
      greenInputs.forEach(id => {{
        const el = document.getElementById(id);
        if (el) {{
          el.addEventListener("input", updateGreenIndicators);
          el.addEventListener("change", updateGreenIndicators);
        }}
      }});

      // Copy Green ESG Brief Listener
      const copyGreenBriefBtn = document.getElementById("copyGreenBriefBtn");
      if (copyGreenBriefBtn) {{
        copyGreenBriefBtn.addEventListener("click", () => {{
          const sec = document.getElementById("greenSectorSelect");
          const secText = sec ? sec.options[sec.selectedIndex].text : "Export Industry";
          const mwh = document.getElementById("greenMwhVal").textContent;
          const re = document.getElementById("greenReVal").textContent;
          const ets = document.getElementById("greenEtsVal").textContent;
          const baseCo2 = document.getElementById("greenBaselineCo2").textContent;
          const abatedCo2 = document.getElementById("greenAbatedCo2").textContent;
          const avoidedEur = document.getElementById("greenCbamAvoidedEur").textContent;
          const avoidedUsd = document.getElementById("greenCbamAvoidedUsd").textContent;
          const score = document.getElementById("greenIndexScore").textContent;
          const badge = document.getElementById("greenIndexRatingBadge").textContent.trim();

          const summary = `[EUROPEAN GREEN DEAL & CBAM CARBON COMPLIANCE AUDIT]\\n` +
            `- Sector & Scope: ${{secText}}\\n` +
            `- Monthly Electricity Demand: ${{mwh}}\\n` +
            `- Clean Sourcing (Solar/DPPA): ${{re}}\\n` +
            `- EU ETS Benchmark Price: ${{ets}}\\n` +
            `- Scope 2 Baseline: ${{baseCo2}} (MONRE EF = 0.7221 tCO2e/MWh)\\n` +
            `- Annual Decarbonization: ${{abatedCo2}}\\n` +
            `- Avoided EU CBAM Liability: ${{avoidedEur}} (${{avoidedUsd}})\\n` +
            `- Vietnam Green Growth Index: ${{score}} / 100 (${{badge}})\\n` +
            `- Statutory Citations: Regulation (EU) 2023/956, Decree 80/2024 DPPA, Decision 1658/QD-TTg\\n` +
            `- Source: https://renewablevietnam.com`;

          navigator.clipboard.writeText(summary).then(() => {{
            const orig = copyGreenBriefBtn.innerHTML;
            copyGreenBriefBtn.innerHTML = `<span class="text-emerald-500 font-semibold font-mono text-[10px]">✓ Copied!</span>`;
            setTimeout(() => {{ copyGreenBriefBtn.innerHTML = orig; }}, 2000);
          }});
        }});
      }}

      // Copy EVN Brief Listener
      const copyEvnBriefBtn = document.getElementById("copyEvnBriefBtn");
      if (copyEvnBriefBtn) {{
        copyEvnBriefBtn.addEventListener("click", () => {{
          const kwh = document.getElementById("evnTotalKwh").textContent;
          const vnd = document.getElementById("evnTotalVnd").textContent;
          const usd = document.getElementById("evnTotalUsd").textContent;
          const ac = document.getElementById("evnAcVal").textContent;
          const fridge = document.getElementById("evnFridgeVal") ? document.getElementById("evnFridgeVal").textContent : "";

          const summary = `[EVN STATUTORY TARIFF & CONSUMPTION ESTIMATE]\\n` +
            `- Monthly Consumption: ${{kwh}}\\n` +
            `- Total Bill: ${{vnd}} (${{usd}})\\n` +
            `- AC Units & Runtime: ${{ac}}\\n` +
            `- Refrigerator: ${{fridge}}\\n` +
            `- Statutory Tariff: Decision 2699/QD-BCT (6 Progressive Tiers)\\n` +
            `- Source: https://renewablevietnam.com/calculator/`;

          navigator.clipboard.writeText(summary).then(() => {{
            const orig = copyEvnBriefBtn.innerHTML;
            copyEvnBriefBtn.innerHTML = `<span class="text-emerald-500 font-semibold font-mono text-[10px]">✓ Copied!</span>`;
            setTimeout(() => {{ copyEvnBriefBtn.innerHTML = orig; }}, 2000);
          }});
        }});
      }}

      {calc_sliders_chunk}

      // Theme toggle handler
      const themeToggleBtn = document.getElementById('themeToggleBtn');
      const sunIcon = document.getElementById('sunIcon');
      const moonIcon = document.getElementById('moonIcon');

      function updateIcons(isDark) {{
        if (isDark) {{
          sunIcon.classList.remove('hidden');
          moonIcon.classList.add('hidden');
        }} else {{
          sunIcon.classList.add('hidden');
          moonIcon.classList.remove('hidden');
        }}
      }}
      updateIcons(document.documentElement.classList.contains('dark'));

      themeToggleBtn.addEventListener('click', () => {{
        const isDark = document.documentElement.classList.toggle('dark');
        localStorage.setItem('rvn-theme', isDark ? 'dark' : 'light');
        updateIcons(isDark);
      }});
    }});
  </script>
</body>
</html>
"""

print(f"Generated calculator/index.html ({len(calculator_html)} bytes)")

# -------------------------------------------------------------
# 2. REFACTOR index.html (Homepage)
# -------------------------------------------------------------
# 2.1 In header nav, add "Power Sizer & Tariffs" link
old_nav = """      <!-- Quick Inter-Domain Jump Navigation -->
      <nav class="hidden md:flex items-center gap-1 font-mono text-[11px] tracking-wider text-inkMuted dark:text-textDarkMuted">
        <a href="/" class="px-2.5 py-1 rounded-md text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20">Industrial Hubs</a>
        <span class="text-slate-300 dark:text-slate-700">&middot;</span>
        <a href="/projectenergy/" class="px-2.5 py-1 rounded-md hover:text-emerald-600 dark:hover:text-emerald-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Energy Map</a>
        <span class="text-slate-300 dark:text-slate-700">&middot;</span>
        <a href="/evcharging/" class="px-2.5 py-1 rounded-md hover:text-amber-600 dark:hover:text-amber-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">EV Stations</a>
        <span class="text-slate-300 dark:text-slate-700">&middot;</span>
        <a href="/hub/" class="px-2.5 py-1 rounded-md hover:text-sky-600 dark:hover:text-sky-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">The Library</a>
      </nav>"""

new_nav = """      <!-- Quick Inter-Domain Jump Navigation -->
      <nav class="hidden md:flex items-center gap-1 font-mono text-[11px] tracking-wider text-inkMuted dark:text-textDarkMuted">
        <a href="/" class="px-2.5 py-1 rounded-md text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20">Industrial Hubs</a>
        <span class="text-slate-300 dark:text-slate-700">&middot;</span>
        <a href="/projectenergy/" class="px-2.5 py-1 rounded-md hover:text-emerald-600 dark:hover:text-emerald-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Energy Map</a>
        <span class="text-slate-300 dark:text-slate-700">&middot;</span>
        <a href="/evcharging/" class="px-2.5 py-1 rounded-md hover:text-amber-600 dark:hover:text-amber-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">EV Stations</a>
        <span class="text-slate-300 dark:text-slate-700">&middot;</span>
        <a href="/calculator/" class="px-2.5 py-1 rounded-md hover:text-teal-600 dark:hover:text-teal-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Power Sizer &amp; Tariffs</a>
        <span class="text-slate-300 dark:text-slate-700">&middot;</span>
        <a href="/hub/" class="px-2.5 py-1 rounded-md hover:text-sky-600 dark:hover:text-sky-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">The Library</a>
      </nav>"""

new_index_html = orig_html.replace(old_nav, new_nav)
if new_index_html == orig_html:
    raise ValueError("Failed to replace navigation in index.html!")

# 2.2 In header right controls, replace #toolsSidebar button with /calculator/ link
old_sidebar_btn = """      <a href="#toolsSidebar" class="hidden sm:inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg font-mono text-[11px] text-inkPrimary dark:text-textDarkPrimary bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder hover:border-teal-500 dark:hover:border-teal-400/40 transition-all shadow-sm">
        <svg class="w-3.5 h-3.5 text-teal-500 dark:text-teal-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
        </svg>
        <span>Tools Sidebar</span>
      </a>"""

new_sidebar_btn = """      <a href="/calculator/" class="hidden sm:inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg font-mono text-[11px] text-inkPrimary dark:text-textDarkPrimary bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder hover:border-teal-500 dark:hover:border-teal-400/40 transition-all shadow-sm">
        <svg class="w-3.5 h-3.5 text-teal-500 dark:text-teal-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
        </svg>
        <span>Power Sizer &amp; Tariffs</span>
      </a>"""

new_index_html = new_index_html.replace(old_sidebar_btn, new_sidebar_btn)

# 2.3 Decommission <aside id="toolsSidebar"> from <main>
old_main_start = """  <main class="relative z-10 flex-1 w-full max-w-7xl mx-auto py-6 sm:py-8">
    <div class="flex flex-col lg:flex-row gap-8 items-start">

    <!-- ==================================================================== -->
    <!-- DEDICATED LEFT SIDEBAR: CALCULATION & SIZING TOOLKIT               -->
    <!-- ==================================================================== -->
    <aside id="toolsSidebar" class="w-full lg:w-[410px] xl:w-[430px] shrink-0 lg:sticky lg:top-6 self-start space-y-4">"""

# Find where </aside> ends
aside_close_idx = new_index_html.find("</aside>")
right_workspace_idx = new_index_html.find('<div class="flex-1 min-w-0 space-y-8 sm:space-y-10">', aside_close_idx)
after_right_workspace_idx = right_workspace_idx + len('<div class="flex-1 min-w-0 space-y-8 sm:space-y-10">')

# We replace from <div class="flex flex-col lg:flex-row gap-8 items-start"> down to after right_workspace
main_before = new_index_html[:new_index_html.find('<div class="flex flex-col lg:flex-row gap-8 items-start">')]
main_after = new_index_html[after_right_workspace_idx:]

new_index_html = main_before + '<div class="w-full space-y-8 sm:space-y-10">' + main_after

# Now replace the double closing </div>\n\n    </div>\n  </main> with single </div>\n  </main>
old_main_end = """      </div>

    </div>
  </main>"""
new_main_end = """    </div>
  </main>"""

if old_main_end in new_index_html:
    new_index_html = new_index_html.replace(old_main_end, new_main_end)
else:
    # Try regex match
    new_index_html = re.sub(r'</div>\s*</div>\s*</main>', '</div>\n  </main>', new_index_html)

# 2.4 Remove or guard calculator JS in index.html to avoid null element references
# Replace DOMContentLoaded calls to updateEvnEstimator() and updateGreenIndicators()
new_index_html = new_index_html.replace("      updateEvnEstimator();\n", "")
new_index_html = new_index_html.replace("      updateGreenIndicators();\n", "")

# Guard calculator tab switcher & sliders
old_tab_switcher = """      // Calculator Suite Tab Switcher
      const tabCorporateSizerBtn = document.getElementById("tabCorporateSizerBtn");
      const tabEvnEstimatorBtn = document.getElementById("tabEvnEstimatorBtn");
      const tabGreenIndicatorBtn = document.getElementById("tabGreenIndicatorBtn");
      const corporateSizerContainer = document.getElementById("corporateSizerContainer");
      const evnEstimatorContainer = document.getElementById("evnEstimatorContainer");
      const greenIndicatorContainer = document.getElementById("greenIndicatorContainer");

      const activateTab = (activeBtn, activeContainer) => {
        [tabCorporateSizerBtn, tabEvnEstimatorBtn, tabGreenIndicatorBtn].forEach(btn => {
          if (!btn) return;
          if (btn === activeBtn) {
            btn.className = "calc-tab-btn py-1.5 px-1 rounded-lg bg-teal-600 text-white font-semibold shadow-sm transition-all cursor-pointer text-center truncate";
          } else {
            btn.className = "calc-tab-btn py-1.5 px-1 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-inkPrimary dark:hover:text-white transition-all cursor-pointer text-center truncate";
          }
        });
        [corporateSizerContainer, evnEstimatorContainer, greenIndicatorContainer].forEach(c => {
          if (!c) return;
          if (c === activeContainer) {
            c.classList.remove("hidden");
          } else {
            c.classList.add("hidden");
          }
        });
      };

      if (tabCorporateSizerBtn && tabEvnEstimatorBtn && tabGreenIndicatorBtn) {
        tabCorporateSizerBtn.addEventListener("click", () => activateTab(tabCorporateSizerBtn, corporateSizerContainer));
        tabEvnEstimatorBtn.addEventListener("click", () => {
          activateTab(tabEvnEstimatorBtn, evnEstimatorContainer);
          updateEvnEstimator();
        });
        tabGreenIndicatorBtn.addEventListener("click", () => {
          activateTab(tabGreenIndicatorBtn, greenIndicatorContainer);
          updateGreenIndicators();
        });
      }"""

new_index_html = new_index_html.replace(old_tab_switcher, "      // (Calculator suite relocated to /calculator/)")

# Guard the 3 slider listeners on index.html:
new_index_html = new_index_html.replace(
    'document.getElementById("calcDemandSlider").addEventListener("input", updateCalculator);',
    'document.getElementById("calcDemandSlider")?.addEventListener("input", updateCalculator);'
)
new_index_html = new_index_html.replace(
    'document.getElementById("calcMwhSlider").addEventListener("input", updateCalculator);',
    'document.getElementById("calcMwhSlider")?.addEventListener("input", updateCalculator);'
)
new_index_html = new_index_html.replace(
    'document.getElementById("calcReSlider").addEventListener("input", updateCalculator);',
    'document.getElementById("calcReSlider")?.addEventListener("input", updateCalculator);'
)

print(f"Generated clean full-width index.html ({len(new_index_html)} bytes)")

# -------------------------------------------------------------
# 3. WRITE TO ALL DESTINATIONS
# -------------------------------------------------------------
for repo in REPOS:
    print(f"\nUpdating {repo}...")
    
    # 3.1 Write calculator/index.html
    calc_dir = os.path.join(repo, "calculator")
    os.makedirs(calc_dir, exist_ok=True)
    calc_path = os.path.join(calc_dir, "index.html")
    with open(calc_path, "w", encoding="utf-8") as f:
        f.write(calculator_html)
    print(f"  Written {calc_path}")

    # 3.2 Write green/calculator/index.html
    green_calc_dir = os.path.join(repo, "green", "calculator")
    os.makedirs(green_calc_dir, exist_ok=True)
    green_calc_path = os.path.join(green_calc_dir, "index.html")
    with open(green_calc_path, "w", encoding="utf-8") as f:
        f.write(calculator_html)
    print(f"  Written {green_calc_path}")

    # 3.3 Write root index.html
    root_index_path = os.path.join(repo, "index.html")
    with open(root_index_path, "w", encoding="utf-8") as f:
        f.write(new_index_html)
    print(f"  Written {root_index_path}")

    # 3.4 Write green/index.html
    green_index_path = os.path.join(repo, "green", "index.html")
    with open(green_index_path, "w", encoding="utf-8") as f:
        f.write(new_index_html)
    print(f"  Written {green_index_path}")

print("\n[SUCCESS] All files updated across all repositories and mirror routes!")
