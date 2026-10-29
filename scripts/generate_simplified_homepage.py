import os

SIMPLIFIED_HTML = """<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0" />
  
  <title>Renewable Viet Nam | National Clean Energy & Ecological Transition Platform</title>
  <meta name="description" content="National clean energy and ecological transition intelligence platform: PDP8 power generation, green industrial siting, EV charging infrastructure, and statutory investment advisory." />
  <meta name="keywords" content="Vietnam renewable energy, PDP8 energy atlas, green industrial parks Vietnam, EV charging Vietnam, DPPA Decree 80, clean energy investment Vietnam" />
  <link rel="canonical" href="https://renewablevietnam.com/" />

  <!-- Open Graph / Social Sharing -->
  <meta property="og:type" content="website" />
  <meta property="og:url" content="https://renewablevietnam.com/" />
  <meta property="og:title" content="Renewable Viet Nam" />
  <meta property="og:description" content="National clean energy and ecological transition intelligence platform." />
  <meta property="og:image" content="https://renewablevietnam.com/assets/images/logo.svg" />

  <!-- Twitter Meta -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:url" content="https://renewablevietnam.com/" />
  <meta name="twitter:title" content="Renewable Viet Nam" />
  <meta name="twitter:description" content="National clean energy and ecological transition intelligence platform." />
  <meta name="twitter:image" content="https://renewablevietnam.com/assets/images/logo.svg" />

  <!-- Performance & Tailwind -->
  <link rel="preconnect" href="https://cdn.tailwindcss.com" crossorigin>
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          colors: {
            obsidian: '#090D16',
            darkSurface: '#0E1422',
            darkCard: '#131B2C',
            darkBorder: '#1E293B',
          }
        }
      }
    }
  </script>

  <style>
    html, body {
      overflow-x: hidden;
      max-width: 100vw;
    }
    .no-scrollbar::-webkit-scrollbar { display: none; }
    .no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; -webkit-overflow-scrolling: touch; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "SF Pro Display", "Roboto", "Helvetica Neue", sans-serif;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      text-rendering: optimizeLegibility;
      letter-spacing: -0.011em;
    }
    .font-mono, td, th, .tabular-nums {
      font-variant-numeric: tabular-nums lining-nums;
    }
    ::-webkit-scrollbar { width: 5px; height: 5px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: rgba(148, 163, 184, 0.25); border-radius: 9999px; }
    ::-webkit-scrollbar-thumb:hover { background: rgba(148, 163, 184, 0.4); }
  </style>
</head>
<body class="bg-slate-50 dark:bg-obsidian text-slate-900 dark:text-slate-100 min-h-screen flex flex-col antialiased selection:bg-slate-300 dark:selection:bg-slate-700 transition-colors duration-150">

  <!-- TOP NAVIGATION BAR -->
  <header class="sticky top-0 z-40 w-full bg-white/95 dark:bg-obsidian/95 backdrop-blur-md border-b border-slate-200 dark:border-darkBorder px-4 sm:px-6 lg:px-8 transition-colors">
    <div class="w-full max-w-7xl mx-auto flex flex-col gap-2 py-3">
      <div class="flex items-center justify-between w-full">
        <div class="flex items-center gap-6">
          <a href="https://renewablevietnam.com/" class="flex items-center gap-2.5 group shrink-0" aria-label="Renewable Viet Nam">
            <img src="/assets/images/logo.svg" alt="Renewable Viet Nam Mark" width="28" height="28" class="w-7 h-7 rounded shrink-0" />
            <span class="text-xs sm:text-sm font-semibold tracking-wider uppercase text-slate-900 dark:text-slate-100">
              Renewable Viet Nam
            </span>
          </a>

          <!-- Desktop Navigation with Two Distinct Zones -->
          <nav class="hidden md:flex items-center gap-1.5 font-mono text-[11px] tracking-wide text-slate-500 dark:text-slate-400">
            <!-- Zone 1: Overview & Geospatial Platforms -->
            <a href="https://renewablevietnam.com/" class="px-2.5 py-1 rounded text-slate-900 dark:text-white font-medium bg-slate-200/70 dark:bg-slate-800 transition-colors">Overview</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="https://energy.renewablevietnam.com/" class="px-2.5 py-1 rounded hover:text-slate-900 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">PDP8 Energy</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="https://ind.renewablevietnam.com/" class="px-2.5 py-1 rounded hover:text-slate-900 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Green Industrial</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="https://ev.renewablevietnam.com/" class="px-2.5 py-1 rounded hover:text-slate-900 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">EV Tech</a>

            <!-- Zone Separator -->
            <div class="h-4 w-px bg-slate-300 dark:bg-slate-700 mx-2"></div>

            <!-- Zone 2: Statutory Library & Advisory Workflow (Distinct Format Indicator) -->
            <div class="flex items-center gap-1.5 p-0.5 rounded-md border border-slate-300/80 dark:border-slate-700/80 bg-slate-100/50 dark:bg-slate-900/40">
              <a href="https://legal.renewablevietnam.com/" class="px-2 py-0.5 rounded text-[10px] uppercase font-semibold text-slate-700 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white hover:bg-white dark:hover:bg-darkCard transition-all flex items-center gap-1">
                <span>Legal Framework</span>
                <span class="text-[9px] text-slate-400">&nearr;</span>
              </a>
              <span class="text-slate-300 dark:text-slate-700">&middot;</span>
              <a href="https://invest.renewablevietnam.com/" class="px-2 py-0.5 rounded text-[10px] uppercase font-semibold text-slate-700 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white hover:bg-white dark:hover:bg-darkCard transition-all flex items-center gap-1">
                <span>Investment M&A</span>
                <span class="text-[9px] text-slate-400">&nearr;</span>
              </a>
            </div>
          </nav>
        </div>

        <!-- Controls: Wording-Based Theme Switcher -->
        <div class="flex items-center gap-2">
          <button id="themeToggleBtn" aria-label="Toggle Theme" class="px-2.5 py-1 rounded border border-slate-300 dark:border-slate-700 bg-white dark:bg-darkSurface hover:bg-slate-50 dark:hover:bg-darkCard font-mono text-[11px] text-slate-700 dark:text-slate-300 transition-colors cursor-pointer">
            <span id="themeToggleLabel">Theme: Dark</span>
          </button>
        </div>
      </div>

      <!-- Mobile Touch Navigation -->
      <nav class="flex md:hidden items-center gap-1.5 overflow-x-auto no-scrollbar pt-1 pb-0.5 font-mono text-[11px] whitespace-nowrap w-full">
        <a href="https://renewablevietnam.com/" class="px-2.5 py-1 rounded bg-slate-200 dark:bg-slate-800 text-slate-900 dark:text-white font-medium shrink-0">Overview</a>
        <a href="https://energy.renewablevietnam.com/" class="px-2.5 py-1 rounded text-slate-600 dark:text-slate-400 hover:text-slate-900 bg-white dark:bg-darkSurface border border-slate-200 dark:border-darkBorder shrink-0">PDP8 Energy</a>
        <a href="https://ind.renewablevietnam.com/" class="px-2.5 py-1 rounded text-slate-600 dark:text-slate-400 hover:text-slate-900 bg-white dark:bg-darkSurface border border-slate-200 dark:border-darkBorder shrink-0">Green Industrial</a>
        <a href="https://ev.renewablevietnam.com/" class="px-2.5 py-1 rounded text-slate-600 dark:text-slate-400 hover:text-slate-900 bg-white dark:bg-darkSurface border border-slate-200 dark:border-darkBorder shrink-0">EV Tech</a>
        <div class="h-4 w-px bg-slate-300 dark:bg-slate-700 shrink-0 mx-1"></div>
        <a href="https://legal.renewablevietnam.com/" class="px-2 py-1 rounded text-[10px] uppercase font-semibold text-slate-700 dark:text-slate-300 bg-slate-100 dark:bg-slate-900 border border-slate-300 dark:border-slate-700 shrink-0">Legal Framework &nearr;</a>
        <a href="https://invest.renewablevietnam.com/" class="px-2 py-1 rounded text-[10px] uppercase font-semibold text-slate-700 dark:text-slate-300 bg-slate-100 dark:bg-slate-900 border border-slate-300 dark:border-slate-700 shrink-0">Investment M&A &nearr;</a>
      </nav>
    </div>
  </header>

  <!-- MAIN WORKSPACE -->
  <main class="flex-1 w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 sm:py-10 space-y-10">

    <!-- HERO HEADER (SUBDUED & MONOCHROMATIC) -->
    <section class="space-y-3 max-w-3xl">
      <div class="inline-block font-mono text-[10px] uppercase tracking-wider text-slate-500 dark:text-slate-400 border border-slate-300 dark:border-slate-700 px-2 py-0.5 rounded">
        National Clean Energy Transition Platform
      </div>
      <h1 class="text-3xl sm:text-4xl font-normal tracking-tight text-slate-900 dark:text-slate-100">
        Renewable Viet Nam
      </h1>
      <p class="text-sm text-slate-600 dark:text-slate-400 leading-relaxed font-light">
        Unified infrastructure intelligence across Vietnam's power generation, green industrial hubs, electric mobility corridors, statutory frameworks, and clean energy transactions.
      </p>
      <div class="pt-1 flex items-center gap-2 font-mono text-xs text-slate-500 dark:text-slate-400">
        <span class="inline-block w-1.5 h-1.5 rounded-full bg-slate-400 dark:bg-slate-500"></span>
        <span>Operational Subdomains: 5 Nodes Connected</span>
      </div>
    </section>

    <!-- ZONE 1: GEOSPATIAL TELEMETRY PLATFORMS -->
    <section class="space-y-4">
      <div class="flex items-center justify-between border-b border-slate-200 dark:border-darkBorder pb-2">
        <div class="space-y-0.5">
          <h2 class="text-xs font-mono uppercase tracking-wider text-slate-500 dark:text-slate-400 font-semibold">
            Zone A &middot; Geospatial Telemetry Platforms
          </h2>
          <p class="text-xs text-slate-500 dark:text-slate-400 font-light">
            Interactive GIS cartography, geospatial asset coordinates, and live infrastructure indices.
          </p>
        </div>
        <span class="font-mono text-[10px] text-slate-400 uppercase">Cartography Mode</span>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <!-- Node 1: PDP8 Energy Atlas -->
        <a href="https://energy.renewablevietnam.com/" class="p-5 rounded-xl bg-white dark:bg-darkSurface border border-slate-200 dark:border-darkBorder hover:border-slate-400 dark:hover:border-slate-600 transition-all flex flex-col justify-between group">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <span class="font-mono text-[10px] text-slate-500 uppercase tracking-wider">
                energy.renewablevietnam.com
              </span>
              <span class="font-mono text-xs text-slate-400 group-hover:text-slate-900 dark:group-hover:text-white transition-colors">&rarr;</span>
            </div>
            <div>
              <h3 class="text-base font-semibold text-slate-900 dark:text-slate-100 group-hover:underline">
                PDP8 Clean Energy Atlas
              </h3>
              <p class="text-xs text-slate-600 dark:text-slate-400 font-light mt-1.5 leading-relaxed">
                National clean generation assets: onshore/offshore wind, solar plants, hydro, biomass, and 500kV/220kV transmission substations.
              </p>
            </div>
          </div>
          <div class="pt-5 border-t border-slate-100 dark:border-slate-800/80 mt-4 flex items-baseline justify-between font-mono">
            <div>
              <span class="text-lg font-bold text-slate-900 dark:text-white">960+</span>
              <span class="text-[10px] text-slate-500 ml-1">Plants</span>
            </div>
            <span class="text-xs text-slate-500">107.5 GW</span>
          </div>
        </a>

        <!-- Node 2: Green Industrial Siting -->
        <a href="https://ind.renewablevietnam.com/" class="p-5 rounded-xl bg-white dark:bg-darkSurface border border-slate-200 dark:border-darkBorder hover:border-slate-400 dark:hover:border-slate-600 transition-all flex flex-col justify-between group">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <span class="font-mono text-[10px] text-slate-500 uppercase tracking-wider">
                ind.renewablevietnam.com
              </span>
              <span class="font-mono text-xs text-slate-400 group-hover:text-slate-900 dark:group-hover:text-white transition-colors">&rarr;</span>
            </div>
            <div>
              <h3 class="text-base font-semibold text-slate-900 dark:text-slate-100 group-hover:underline">
                Green Industrial Siting
              </h3>
              <p class="text-xs text-slate-600 dark:text-slate-400 font-light mt-1.5 leading-relaxed">
                Directory of 168 industrial parks: substation proximity, rooftop solar potential, and Decree 80 bilateral wheeling feasibility.
              </p>
            </div>
          </div>
          <div class="pt-5 border-t border-slate-100 dark:border-slate-800/80 mt-4 flex items-baseline justify-between font-mono">
            <div>
              <span class="text-lg font-bold text-slate-900 dark:text-white">168</span>
              <span class="text-[10px] text-slate-500 ml-1">Hubs</span>
            </div>
            <span class="text-xs text-slate-500">104.4K ha</span>
          </div>
        </a>

        <!-- Node 3: EV Mobility Infrastructure -->
        <a href="https://ev.renewablevietnam.com/" class="p-5 rounded-xl bg-white dark:bg-darkSurface border border-slate-200 dark:border-darkBorder hover:border-slate-400 dark:hover:border-slate-600 transition-all flex flex-col justify-between group">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <span class="font-mono text-[10px] text-slate-500 uppercase tracking-wider">
                ev.renewablevietnam.com
              </span>
              <span class="font-mono text-xs text-slate-400 group-hover:text-slate-900 dark:group-hover:text-white transition-colors">&rarr;</span>
            </div>
            <div>
              <h3 class="text-base font-semibold text-slate-900 dark:text-slate-100 group-hover:underline">
                EV Mobility Infrastructure
              </h3>
              <p class="text-xs text-slate-600 dark:text-slate-400 font-light mt-1.5 leading-relaxed">
                National charging infrastructure: 22,055+ verified ports across VinFast, EV ONE, and Charge+ networks on interactive cartography.
              </p>
            </div>
          </div>
          <div class="pt-5 border-t border-slate-100 dark:border-slate-800/80 mt-4 flex items-baseline justify-between font-mono">
            <div>
              <span class="text-lg font-bold text-slate-900 dark:text-white">22,055+</span>
              <span class="text-[10px] text-slate-500 ml-1">Ports</span>
            </div>
            <span class="text-xs text-slate-500">63 Prov.</span>
          </div>
        </a>
      </div>
    </section>

    <!-- ZONE 2: STATUTORY & INSTITUTIONAL ADVISORY PLATFORMS -->
    <section class="space-y-4">
      <div class="flex items-center justify-between border-b border-slate-200 dark:border-darkBorder pb-2">
        <div class="space-y-0.5">
          <h2 class="text-xs font-mono uppercase tracking-wider text-slate-500 dark:text-slate-400 font-semibold">
            Zone B &middot; Statutory Framework &amp; Advisory Engines
          </h2>
          <p class="text-xs text-slate-500 dark:text-slate-400 font-light">
            Document library, legal directives, permitting workflows, and M&amp;A due diligence frameworks.
          </p>
        </div>
        <span class="font-mono text-[10px] text-slate-400 uppercase">Document &amp; Workflow Mode</span>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <!-- Node 4: Legal Framework Library -->
        <a href="https://legal.renewablevietnam.com/" class="p-5 rounded-xl bg-slate-100/60 dark:bg-darkCard/80 border border-slate-300 dark:border-slate-700/80 hover:border-slate-500 dark:hover:border-slate-500 transition-all flex flex-col justify-between group">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-1.5 font-mono text-[10px] text-slate-600 dark:text-slate-300">
                <span class="font-semibold uppercase tracking-wider">legal.renewablevietnam.com</span>
                <span class="text-slate-400">&middot;</span>
                <span class="text-[9px] uppercase px-1.5 py-0.2 rounded border border-slate-300 dark:border-slate-600">Library</span>
              </div>
              <span class="font-mono text-xs text-slate-400 group-hover:text-slate-900 dark:group-hover:text-white transition-colors">&nearr;</span>
            </div>
            <div>
              <h3 class="text-base font-semibold text-slate-900 dark:text-slate-100 group-hover:underline">
                Statutory Energy Library
              </h3>
              <p class="text-xs text-slate-600 dark:text-slate-400 font-light mt-1.5 leading-relaxed">
                Centralized statutory archive: Decree 80/2024 Direct PPA mechanism, PDP8 Decisions 500/QD-TTg, MOIT circulars, grid integration criteria, and legal gazettes.
              </p>
            </div>
          </div>
          <div class="pt-4 border-t border-slate-200 dark:border-slate-700/60 mt-4 flex items-center justify-between font-mono text-xs text-slate-500">
            <span>Primary Legal Corpus</span>
            <span>Document Directory</span>
          </div>
        </a>

        <!-- Node 5: Investment M&A Engine -->
        <a href="https://invest.renewablevietnam.com/" class="p-5 rounded-xl bg-slate-100/60 dark:bg-darkCard/80 border border-slate-300 dark:border-slate-700/80 hover:border-slate-500 dark:hover:border-slate-500 transition-all flex flex-col justify-between group">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-1.5 font-mono text-[10px] text-slate-600 dark:text-slate-300">
                <span class="font-semibold uppercase tracking-wider">invest.renewablevietnam.com</span>
                <span class="text-slate-400">&middot;</span>
                <span class="text-[9px] uppercase px-1.5 py-0.2 rounded border border-slate-300 dark:border-slate-600">Advisory</span>
              </div>
              <span class="font-mono text-xs text-slate-400 group-hover:text-slate-900 dark:group-hover:text-white transition-colors">&nearr;</span>
            </div>
            <div>
              <h3 class="text-base font-semibold text-slate-900 dark:text-slate-100 group-hover:underline">
                Investment Project M&amp;A Engine
              </h3>
              <p class="text-xs text-slate-600 dark:text-slate-400 font-light mt-1.5 leading-relaxed">
                Statutory permitting Critical Path Method (CPM), land allocation clearance steps, Environmental Impact Assessment (EIA), and valuation due diligence.
              </p>
            </div>
          </div>
          <div class="pt-4 border-t border-slate-200 dark:border-slate-700/60 mt-4 flex items-center justify-between font-mono text-xs text-slate-500">
            <span>4-Tier Due Diligence</span>
            <span>CPM Gantt Workflow</span>
          </div>
        </a>
      </div>
    </section>

  </main>

  <!-- INSTITUTIONAL FOOTER -->
  <footer class="w-full bg-white dark:bg-darkSurface border-t border-slate-200 dark:border-darkBorder mt-12 py-6 px-4 sm:px-6 lg:px-8 text-xs text-slate-500 dark:text-slate-400 font-light">
    <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-4 font-mono text-[11px]">
      <div class="flex items-center gap-2">
        <img src="/assets/images/logo.svg" alt="Renewable Viet Nam" width="20" height="20" class="w-5 h-5 rounded" />
        <span class="font-semibold text-slate-900 dark:text-slate-100">Renewable Viet Nam</span>
      </div>

      <div class="flex flex-wrap items-center justify-center gap-3">
        <a href="https://energy.renewablevietnam.com/" class="hover:text-slate-900 dark:hover:text-white">PDP8 Energy</a>
        <span>&middot;</span>
        <a href="https://ind.renewablevietnam.com/" class="hover:text-slate-900 dark:hover:text-white">Green Industrial</a>
        <span>&middot;</span>
        <a href="https://ev.renewablevietnam.com/" class="hover:text-slate-900 dark:hover:text-white">EV Tech</a>
        <span>&middot;</span>
        <a href="https://legal.renewablevietnam.com/" class="hover:text-slate-900 dark:hover:text-white">Legal Framework</a>
        <span>&middot;</span>
        <a href="https://invest.renewablevietnam.com/" class="hover:text-slate-900 dark:hover:text-white">Investment M&A</a>
      </div>

      <div class="text-slate-400">
        &copy; 2026 Renewable Viet Nam.
      </div>
    </div>
  </footer>

  <!-- THEME LOGIC (WORDING BASED) -->
  <script>
    const themeBtn = document.getElementById('themeToggleBtn');
    const themeLabel = document.getElementById('themeToggleLabel');

    function applyTheme(isDark) {
      if (isDark) {
        document.documentElement.classList.add('dark');
        if (themeLabel) themeLabel.textContent = 'Theme: Dark';
        localStorage.setItem('theme', 'dark');
      } else {
        document.documentElement.classList.remove('dark');
        if (themeLabel) themeLabel.textContent = 'Theme: Light';
        localStorage.setItem('theme', 'light');
      }
    }

    const savedTheme = localStorage.getItem('theme');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    applyTheme(savedTheme ? savedTheme === 'dark' : prefersDark);

    themeBtn?.addEventListener('click', () => {
      const isDark = document.documentElement.classList.contains('dark');
      applyTheme(!isDark);
    });
  </script>
</body>
</html>
"""

base_dir = r"G:\My Drive\7. AI\RenewableVietNam"
index_file = os.path.join(base_dir, "index.html")
rev5_file = os.path.join(base_dir, "index_Rev.005.html")

# Non-destructive sequential revision
with open(rev5_file, "w", encoding="utf-8") as f:
    f.write(SIMPLIFIED_HTML)
print(f"Created baseline revision: {rev5_file}")

with open(index_file, "w", encoding="utf-8") as f:
    f.write(SIMPLIFIED_HTML)
print(f"Updated active homepage: {index_file}")
