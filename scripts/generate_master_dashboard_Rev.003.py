import os

DASHBOARD_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0" />
  <script>
    (function () {
      try {
        var savedTheme = localStorage.getItem('rvn_theme_v2');
        if (savedTheme === 'dark') {
          document.documentElement.classList.add('dark');
        } else {
          document.documentElement.classList.remove('dark');
        }
      } catch (e) {}
    })();
  </script>
  <!-- RenewableVietNam Brand Favicon & Touch Icons -->
  <link rel="icon" href="./assets/images/favicon.svg" type="image/svg+xml">
  <link rel="icon" href="./assets/images/favicon.ico" sizes="any">
  <link rel="icon" type="image/png" href="./assets/images/favicon-32.png" sizes="32x32">
  <link rel="icon" type="image/png" href="./assets/images/favicon.png" sizes="180x180">
  <link rel="apple-touch-icon" href="./assets/images/apple-touch-icon.png">

  <title>Renewable Viet Nam | National Clean Energy & Ecological Transition Master Intelligence Cockpit</title>
  <meta name="description" content="Institutional visual telemetry cockpit uniting Vietnam's clean energy ecosystem: PDP8 generation mix, 168 green industrial hubs, 22,055+ EV charging ports, and CPM legal M&A engine." />
  <meta name="keywords" content="Vietnam renewable energy, PDP8 energy atlas, green industrial parks Vietnam, EV charging Vietnam, DPPA Decree 80, clean energy investment Vietnam" />
  <link rel="canonical" href="https://renewablevietnam.com/" />

  <!-- Open Graph / Social Sharing -->
  <meta property="og:type" content="website" />
  <meta property="og:url" content="https://renewablevietnam.com/" />
  <meta property="og:title" content="Renewable Viet Nam | Master Intelligence Cockpit" />
  <meta property="og:description" content="Visual executive dashboard uniting Vietnam's clean generation, eco-industrial hubs, EV infrastructure, and M&A pipeline." />
  <meta property="og:image" content="https://renewablevietnam.com/assets/images/blog-cover.jpg" />

  <!-- Twitter Meta -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:url" content="https://renewablevietnam.com/" />
  <meta name="twitter:title" content="Renewable Viet Nam | Master Intelligence Cockpit" />
  <meta name="twitter:description" content="Visual executive dashboard uniting Vietnam's clean generation, eco-industrial hubs, EV infrastructure, and M&A pipeline." />
  <meta name="twitter:image" content="https://renewablevietnam.com/assets/images/blog-cover.jpg" />

  <!-- Performance & Fonts -->
  <link rel="preconnect" href="https://cdn.tailwindcss.com" crossorigin>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.2/dist/chart.umd.min.js"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          colors: {
            alabaster: '#F8FAFC',
            surfaceLight: '#FFFFFF',
            borderSlate: '#E2E8F0',
            inkPrimary: '#0F172A',
            inkMuted: '#64748B',
            obsidian: '#090D16',
            darkSurface: '#0E1424',
            darkCard: '#141D32',
            darkBorder: 'rgba(255, 255, 255, 0.08)',
            textDarkPrimary: '#F8FAFC',
            textDarkMuted: '#94A3B8',
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
      font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "SF Pro Display", "Inter", "Roboto", sans-serif;
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
    ::-webkit-scrollbar-thumb:hover { background: rgba(59, 130, 246, 0.4); }
  </style>
</head>
<body class="bg-slate-50/60 dark:bg-obsidian text-inkPrimary dark:text-textDarkPrimary min-h-screen flex flex-col antialiased selection:bg-teal-500 selection:text-white transition-colors duration-200">

  <!-- TOP EXECUTIVE NAVIGATION BAR -->
  <header class="sticky top-0 z-50 w-full bg-white/85 dark:bg-obsidian/85 backdrop-blur-md border-b border-slate-200/80 dark:border-darkBorder px-3 sm:px-6 lg:px-8 transition-colors">
    <div class="w-full max-w-7xl mx-auto flex items-center justify-between py-3">
      <div class="flex items-center gap-6">
        <a href="https://renewablevietnam.com/" class="flex items-center gap-2.5 group shrink-0" aria-label="Renewable Vietnam home">
          <img src="/assets/images/logo.svg" alt="Renewable Viet Nam Mark" width="30" height="30" class="w-7.5 h-7.5 rounded-lg shrink-0" />
          <div class="flex flex-col">
            <span class="text-[12px] font-mono uppercase tracking-[0.16em] text-inkPrimary dark:text-textDarkPrimary font-bold leading-tight">
              RENEWABLE VIETNAM
            </span>
            <span class="text-[9px] font-mono tracking-wider text-slate-400 dark:text-slate-500 uppercase">
              Master Cockpit
            </span>
          </div>
        </a>

        <!-- Desktop Quick Jump Navigation -->
        <nav class="hidden md:flex items-center gap-1 font-mono text-[11px] text-inkMuted dark:text-textDarkMuted">
          <a href="https://renewablevietnam.com/" class="px-2.5 py-1 rounded-md text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 transition-colors">Cockpit</a>
          <span class="text-slate-300 dark:text-slate-700">&middot;</span>
          <a href="https://energy.renewablevietnam.com/" class="px-2.5 py-1 rounded-md hover:text-emerald-600 dark:hover:text-emerald-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">PDP8 Energy</a>
          <span class="text-slate-300 dark:text-slate-700">&middot;</span>
          <a href="https://industrial.renewablevietnam.com/" class="px-2.5 py-1 rounded-md hover:text-teal-600 dark:hover:text-teal-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Green Industrial</a>
          <span class="text-slate-300 dark:text-slate-700">&middot;</span>
          <a href="https://ev.renewablevietnam.com/" class="px-2.5 py-1 rounded-md hover:text-amber-500 dark:hover:text-amber-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">EV Tech</a>
          <span class="text-slate-300 dark:text-slate-700">&middot;</span>
          <a href="https://invest.renewablevietnam.com/" class="px-2.5 py-1 rounded-md hover:text-blue-500 dark:hover:text-blue-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Investment M&A</a>
        </nav>
      </div>

      <!-- Controls & Theme -->
      <div class="flex items-center gap-2">
        <div class="hidden sm:flex items-center gap-2 px-2.5 py-1 rounded-full bg-slate-100/80 dark:bg-darkCard border border-slate-200/80 dark:border-darkBorder font-mono text-[10px] text-slate-500 dark:text-slate-400">
          <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span>
          <span>Edge Active</span>
        </div>

        <button id="themeToggleBtn" aria-label="Toggle Theme" class="flex items-center justify-center w-8 h-8 rounded-lg bg-white dark:bg-darkSurface border border-slate-200/80 dark:border-darkBorder shadow-xs hover:border-slate-300 dark:hover:border-slate-600 text-slate-600 dark:text-slate-300 transition-all cursor-pointer">
          <svg id="sunIcon" class="hidden w-4 h-4 text-amber-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.8">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 3v2.25m6.364.386-1.591 1.591M21 12h-2.25m-.386 6.364-1.591-1.591M12 18.75V21m-4.773-4.227-1.591 1.591M5.25 12H3m4.227-4.773L5.636 5.636M15.75 12a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0Z" />
          </svg>
          <svg id="moonIcon" class="w-4 h-4 text-slate-700 dark:text-slate-300" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.8">
            <path stroke-linecap="round" stroke-linejoin="round" d="M21.752 15.002A9.72 9.72 0 0 1 18 15.75c-5.385 0-9.75-4.365-9.75-9.75 0-1.33.266-2.597.748-3.752A9.753 9.753 0 0 0 3 11.25C3 16.635 7.365 21 12.75 21a9.753 9.753 0 0 0 9.002-5.998Z" />
          </svg>
        </button>
      </div>
    </div>
  </header>

  <!-- MAIN MASTER WORKSPACE -->
  <main class="relative z-10 flex-1 w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 space-y-6">

    <!-- HERO HEADER: MINIMAL HIGH-SIGNAL EXECUTIVE SUMMARY -->
    <section class="flex flex-col md:flex-row md:items-center justify-between gap-4 bg-white/70 dark:bg-darkSurface/70 backdrop-blur-sm border border-slate-200/80 dark:border-darkBorder rounded-2xl p-5 shadow-xs">
      <div class="space-y-1">
        <div class="flex items-center gap-2">
          <span class="font-mono text-[10px] uppercase font-bold text-teal-600 dark:text-teal-400 bg-teal-500/10 px-2 py-0.5 rounded border border-teal-500/20">
            Institutional Telemetry
          </span>
          <span class="font-mono text-[10px] text-slate-400">PDP8 &middot; Decree 80 DPPA</span>
        </div>
        <h1 class="text-xl sm:text-2xl font-semibold tracking-tight text-inkPrimary dark:text-textDarkPrimary">
          Vietnam Clean Energy &amp; Ecological Transition Master Cockpit
        </h1>
        <p class="text-xs text-inkMuted dark:text-textDarkMuted max-w-3xl">
          Unified telemetry unifying 107.5 GW generation pipelines, 168 eco-industrial hubs, 22,055+ EV charging ports, and CPM statutory permitting.
        </p>
      </div>

      <!-- Quick Metrics Ribbon -->
      <div class="flex items-center gap-3 sm:gap-4 shrink-0 font-mono text-[11px] pt-2 md:pt-0 border-t md:border-t-0 border-slate-100 dark:border-darkBorder">
        <div class="text-right">
          <span class="block text-slate-400 text-[10px]">Active Pipeline</span>
          <strong class="text-sm font-bold text-emerald-600 dark:text-emerald-400">107.5 GW</strong>
        </div>
        <div class="w-px h-7 bg-slate-200 dark:bg-darkBorder"></div>
        <div class="text-right">
          <span class="block text-slate-400 text-[10px]">Charging Ports</span>
          <strong class="text-sm font-bold text-amber-500">22,055+</strong>
        </div>
        <div class="w-px h-7 bg-slate-200 dark:bg-darkBorder"></div>
        <div class="text-right">
          <span class="block text-slate-400 text-[10px]">Industrial Footprint</span>
          <strong class="text-sm font-bold text-teal-600 dark:text-teal-400">104.4K ha</strong>
        </div>
      </div>
    </section>

    <!-- WORKFLOW PIPELINE: SLEEK CHEVRON PROGRESSION -->
    <section class="bg-white/80 dark:bg-darkSurface/80 backdrop-blur-sm border border-slate-200/80 dark:border-darkBorder rounded-2xl p-5 shadow-xs space-y-3">
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-2">
          <span class="w-2 h-2 rounded-full bg-teal-500"></span>
          <h2 class="text-xs sm:text-sm font-bold uppercase tracking-wider text-slate-700 dark:text-slate-300">
            End-to-End Ecological Transition Architecture
          </h2>
        </div>
        <span class="font-mono text-[10px] text-slate-400">5-Stage Linear Flow</span>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-2.5">
        <!-- Stage 01 -->
        <a href="https://energy.renewablevietnam.com/" class="p-3 rounded-xl bg-slate-50/80 dark:bg-darkCard/80 border border-slate-200/60 dark:border-darkBorder hover:border-emerald-500/50 transition-all group flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between font-mono text-[10px] mb-1">
              <span class="text-emerald-600 dark:text-emerald-400 font-bold">STAGE 01</span>
              <span class="text-slate-400 group-hover:text-emerald-500 transition-colors">&rarr;</span>
            </div>
            <strong class="block text-xs font-semibold text-slate-800 dark:text-slate-200 group-hover:text-emerald-500 transition-colors">PDP8 Zoning</strong>
            <p class="text-[10px] text-slate-500 dark:text-slate-400 mt-0.5">Provincial quota mapping for wind, solar &amp; hydro.</p>
          </div>
          <div class="mt-2.5 pt-1.5 border-t border-slate-200/40 dark:border-darkBorder/40 font-mono text-[10px] text-emerald-600 dark:text-emerald-400 font-semibold">
            107.5 GW Target
          </div>
        </a>

        <!-- Stage 02 -->
        <a href="https://invest.renewablevietnam.com/" class="p-3 rounded-xl bg-slate-50/80 dark:bg-darkCard/80 border border-slate-200/60 dark:border-darkBorder hover:border-blue-500/50 transition-all group flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between font-mono text-[10px] mb-1">
              <span class="text-blue-500 dark:text-blue-400 font-bold">STAGE 02</span>
              <span class="text-slate-400 group-hover:text-blue-500 transition-colors">&rarr;</span>
            </div>
            <strong class="block text-xs font-semibold text-slate-800 dark:text-slate-200 group-hover:text-blue-500 transition-colors">Permitting CPM</strong>
            <p class="text-[10px] text-slate-500 dark:text-slate-400 mt-0.5">Statutory approvals, land allocation &amp; EIA clearance.</p>
          </div>
          <div class="mt-2.5 pt-1.5 border-t border-slate-200/40 dark:border-darkBorder/40 font-mono text-[10px] text-blue-500 dark:text-blue-400 font-semibold">
            30+ Milestones
          </div>
        </a>

        <!-- Stage 03 -->
        <a href="https://energy.renewablevietnam.com/" class="p-3 rounded-xl bg-slate-50/80 dark:bg-darkCard/80 border border-slate-200/60 dark:border-darkBorder hover:border-emerald-500/50 transition-all group flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between font-mono text-[10px] mb-1">
              <span class="text-emerald-600 dark:text-emerald-400 font-bold">STAGE 03</span>
              <span class="text-slate-400 group-hover:text-emerald-500 transition-colors">&rarr;</span>
            </div>
            <strong class="block text-xs font-semibold text-slate-800 dark:text-slate-200 group-hover:text-emerald-500 transition-colors">Grid Intertie</strong>
            <p class="text-[10px] text-slate-500 dark:text-slate-400 mt-0.5">500kV/220kV loop access &amp; curtailment simulation.</p>
          </div>
          <div class="mt-2.5 pt-1.5 border-t border-slate-200/40 dark:border-darkBorder/40 font-mono text-[10px] text-emerald-600 dark:text-emerald-400 font-semibold">
            500kV/220kV Loop
          </div>
        </a>

        <!-- Stage 04 -->
        <a href="https://industrial.renewablevietnam.com/" class="p-3 rounded-xl bg-slate-50/80 dark:bg-darkCard/80 border border-slate-200/60 dark:border-darkBorder hover:border-teal-500/50 transition-all group flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between font-mono text-[10px] mb-1">
              <span class="text-teal-600 dark:text-teal-400 font-bold">STAGE 04</span>
              <span class="text-slate-400 group-hover:text-teal-500 transition-colors">&rarr;</span>
            </div>
            <strong class="block text-xs font-semibold text-slate-800 dark:text-slate-200 group-hover:text-teal-500 transition-colors">Industrial Offtake</strong>
            <p class="text-[10px] text-slate-500 dark:text-slate-400 mt-0.5">Decree 80 bilateral DPPA &amp; RE100 manufacturing.</p>
          </div>
          <div class="mt-2.5 pt-1.5 border-t border-slate-200/40 dark:border-darkBorder/40 font-mono text-[10px] text-teal-600 dark:text-teal-400 font-semibold">
            5,655 MWp Solar
          </div>
        </a>

        <!-- Stage 05 -->
        <a href="https://ev.renewablevietnam.com/" class="p-3 rounded-xl bg-slate-50/80 dark:bg-darkCard/80 border border-slate-200/60 dark:border-darkBorder hover:border-amber-500/50 transition-all group flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between font-mono text-[10px] mb-1">
              <span class="text-amber-500 dark:text-amber-400 font-bold">STAGE 05</span>
              <span class="text-slate-400 group-hover:text-amber-500 transition-colors">&rarr;</span>
            </div>
            <strong class="block text-xs font-semibold text-slate-800 dark:text-slate-200 group-hover:text-amber-500 transition-colors">EV Corridors</strong>
            <p class="text-[10px] text-slate-500 dark:text-slate-400 mt-0.5">National highway DC fast charging &amp; electric freight.</p>
          </div>
          <div class="mt-2.5 pt-1.5 border-t border-slate-200/40 dark:border-darkBorder/40 font-mono text-[10px] text-amber-500 dark:text-amber-400 font-semibold">
            22,055+ Ports
          </div>
        </a>
      </div>
    </section>

    <!-- BENTO GRID: REFINED SUBDOMAIN COMMAND CONSOLE -->
    <section class="space-y-3">
      <div class="flex items-center justify-between">
        <h2 class="text-xs sm:text-sm font-bold uppercase tracking-wider text-slate-700 dark:text-slate-300 flex items-center gap-2">
          <span class="w-2 h-2 rounded-full bg-blue-500"></span>
          Subdomain Command Console
        </h2>
        <span class="font-mono text-[10px] text-slate-400">4 Edge Portals</span>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">

        <!-- Console 1: energy.renewablevietnam.com -->
        <div class="bg-white/80 dark:bg-darkSurface/80 backdrop-blur-sm border border-slate-200/80 dark:border-darkBorder rounded-2xl p-5 shadow-xs hover:border-emerald-500/60 transition-all flex flex-col justify-between group">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-2">
                <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
                <span class="font-mono text-[11px] font-semibold text-emerald-600 dark:text-emerald-400">
                  energy.renewablevietnam.com
                </span>
              </div>
              <a href="https://energy.renewablevietnam.com/" class="w-7 h-7 rounded-lg bg-slate-100 dark:bg-darkCard hover:bg-emerald-500 hover:text-white flex items-center justify-center text-slate-500 dark:text-slate-400 transition-all" aria-label="Open PDP8 Energy Atlas">
                <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 19.5l15-15m0 0H8.25m11.25 0v11.25"/></svg>
              </a>
            </div>

            <div>
              <h3 class="text-sm font-bold text-slate-900 dark:text-white group-hover:text-emerald-500 transition-colors">
                PDP8 Clean Energy &amp; Power Grid Atlas
              </h3>
              <p class="text-xs text-slate-500 dark:text-slate-400 mt-1">
                Geospatial statutory atlas of generation assets, onshore/offshore wind, utility solar, and 500kV/220kV intertie loops.
              </p>
            </div>

            <div class="grid grid-cols-3 gap-2 py-2 border-y border-slate-100 dark:border-darkBorder/60 font-mono text-[11px]">
              <div>
                <span class="block text-slate-400 text-[10px]">Generation</span>
                <strong class="text-slate-900 dark:text-white font-bold text-xs">960+ Plants</strong>
              </div>
              <div>
                <span class="block text-slate-400 text-[10px]">Statutory Cap</span>
                <strong class="text-emerald-600 dark:text-emerald-400 font-bold text-xs">107.5 GW</strong>
              </div>
              <div>
                <span class="block text-slate-400 text-[10px]">Intertie</span>
                <strong class="text-slate-900 dark:text-white font-bold text-xs">500kV/220kV</strong>
              </div>
            </div>
          </div>

          <div class="flex items-center justify-between pt-3 mt-1">
            <div class="flex items-center gap-1.5 font-mono text-[10px] text-slate-400">
              <span class="px-2 py-0.5 rounded bg-slate-100 dark:bg-darkCard">Wind/Solar</span>
              <span class="px-2 py-0.5 rounded bg-slate-100 dark:bg-darkCard">Substations</span>
            </div>
            <a href="https://energy.renewablevietnam.com/" class="inline-flex items-center gap-1 text-xs font-mono font-semibold text-emerald-600 dark:text-emerald-400 hover:underline">
              Launch Atlas &rarr;
            </a>
          </div>
        </div>

        <!-- Console 2: industrial.renewablevietnam.com -->
        <div class="bg-white/80 dark:bg-darkSurface/80 backdrop-blur-sm border border-slate-200/80 dark:border-darkBorder rounded-2xl p-5 shadow-xs hover:border-teal-500/60 transition-all flex flex-col justify-between group">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-2">
                <span class="w-2 h-2 rounded-full bg-teal-500"></span>
                <span class="font-mono text-[11px] font-semibold text-teal-600 dark:text-teal-400">
                  industrial.renewablevietnam.com
                </span>
              </div>
              <a href="https://industrial.renewablevietnam.com/" class="w-7 h-7 rounded-lg bg-slate-100 dark:bg-darkCard hover:bg-teal-500 hover:text-white flex items-center justify-center text-slate-500 dark:text-slate-400 transition-all" aria-label="Open Industrial Siting">
                <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 19.5l15-15m0 0H8.25m11.25 0v11.25"/></svg>
              </a>
            </div>

            <div>
              <h3 class="text-sm font-bold text-slate-900 dark:text-white group-hover:text-teal-500 transition-colors">
                Green Industrial Siting &amp; DPPA Portal
              </h3>
              <p class="text-xs text-slate-500 dark:text-slate-400 mt-1">
                National siting directory of Tier-1 eco-industrial parks, rooftop solar potential, and Decree 80 bilateral wheeling feasibility.
              </p>
            </div>

            <div class="grid grid-cols-3 gap-2 py-2 border-y border-slate-100 dark:border-darkBorder/60 font-mono text-[11px]">
              <div>
                <span class="block text-slate-400 text-[10px]">Tier-1 Hubs</span>
                <strong class="text-slate-900 dark:text-white font-bold text-xs">168 Parks</strong>
              </div>
              <div>
                <span class="block text-slate-400 text-[10px]">Land Area</span>
                <strong class="text-teal-600 dark:text-teal-400 font-bold text-xs">104.4K ha</strong>
              </div>
              <div>
                <span class="block text-slate-400 text-[10px]">Rooftop Cap</span>
                <strong class="text-slate-900 dark:text-white font-bold text-xs">5,655 MWp</strong>
              </div>
            </div>
          </div>

          <div class="flex items-center justify-between pt-3 mt-1">
            <div class="flex items-center gap-1.5 font-mono text-[10px] text-slate-400">
              <span class="px-2 py-0.5 rounded bg-slate-100 dark:bg-darkCard">Decree 80</span>
              <span class="px-2 py-0.5 rounded bg-slate-100 dark:bg-darkCard">ISO 14001</span>
            </div>
            <a href="https://industrial.renewablevietnam.com/" class="inline-flex items-center gap-1 text-xs font-mono font-semibold text-teal-600 dark:text-teal-400 hover:underline">
              Launch Siting &rarr;
            </a>
          </div>
        </div>

        <!-- Console 3: ev.renewablevietnam.com -->
        <div class="bg-white/80 dark:bg-darkSurface/80 backdrop-blur-sm border border-slate-200/80 dark:border-darkBorder rounded-2xl p-5 shadow-xs hover:border-amber-500/60 transition-all flex flex-col justify-between group">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-2">
                <span class="w-2 h-2 rounded-full bg-amber-500"></span>
                <span class="font-mono text-[11px] font-semibold text-amber-500 dark:text-amber-400">
                  ev.renewablevietnam.com
                </span>
              </div>
              <a href="https://ev.renewablevietnam.com/" class="w-7 h-7 rounded-lg bg-slate-100 dark:bg-darkCard hover:bg-amber-500 hover:text-white flex items-center justify-center text-slate-500 dark:text-slate-400 transition-all" aria-label="Open EV Tech Cockpit">
                <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 19.5l15-15m0 0H8.25m11.25 0v11.25"/></svg>
              </a>
            </div>

            <div>
              <h3 class="text-sm font-bold text-slate-900 dark:text-white group-hover:text-amber-500 transition-colors">
                National EV Charging Cockpit
              </h3>
              <p class="text-xs text-slate-500 dark:text-slate-400 mt-1">
                Verified charging infrastructure directory across VinFast, EV ONE, and Charge+ networks on national expressway corridors.
              </p>
            </div>

            <div class="grid grid-cols-3 gap-2 py-2 border-y border-slate-100 dark:border-darkBorder/60 font-mono text-[11px]">
              <div>
                <span class="block text-slate-400 text-[10px]">Charging Ports</span>
                <strong class="text-amber-500 dark:text-amber-400 font-bold text-xs">22,055+</strong>
              </div>
              <div>
                <span class="block text-slate-400 text-[10px]">Geographic Reach</span>
                <strong class="text-slate-900 dark:text-white font-bold text-xs">63 Prov.</strong>
              </div>
              <div>
                <span class="block text-slate-400 text-[10px]">Fast Charging</span>
                <strong class="text-slate-900 dark:text-white font-bold text-xs">62% DC Fast</strong>
              </div>
            </div>
          </div>

          <div class="flex items-center justify-between pt-3 mt-1">
            <div class="flex items-center gap-1.5 font-mono text-[10px] text-slate-400">
              <span class="px-2 py-0.5 rounded bg-slate-100 dark:bg-darkCard">CCS2 Standard</span>
              <span class="px-2 py-0.5 rounded bg-slate-100 dark:bg-darkCard">V-GREEN</span>
            </div>
            <a href="https://ev.renewablevietnam.com/" class="inline-flex items-center gap-1 text-xs font-mono font-semibold text-amber-500 dark:text-amber-400 hover:underline">
              Launch EV Cockpit &rarr;
            </a>
          </div>
        </div>

        <!-- Console 4: invest.renewablevietnam.com -->
        <div class="bg-white/80 dark:bg-darkSurface/80 backdrop-blur-sm border border-slate-200/80 dark:border-darkBorder rounded-2xl p-5 shadow-xs hover:border-blue-500/60 transition-all flex flex-col justify-between group">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-2">
                <span class="w-2 h-2 rounded-full bg-blue-500"></span>
                <span class="font-mono text-[11px] font-semibold text-blue-500 dark:text-blue-400">
                  invest.renewablevietnam.com
                </span>
              </div>
              <a href="https://invest.renewablevietnam.com/" class="w-7 h-7 rounded-lg bg-slate-100 dark:bg-darkCard hover:bg-blue-500 hover:text-white flex items-center justify-center text-slate-500 dark:text-slate-400 transition-all" aria-label="Open Investment M&A Engine">
                <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 19.5l15-15m0 0H8.25m11.25 0v11.25"/></svg>
              </a>
            </div>

            <div>
              <h3 class="text-sm font-bold text-slate-900 dark:text-white group-hover:text-blue-500 transition-colors">
                Investment Project Legal Management &amp; M&amp;A Engine
              </h3>
              <p class="text-xs text-slate-500 dark:text-slate-400 mt-1">
                Institutional critical path method (CPM) statutory permitting, land allocation, and transaction due diligence.
              </p>
            </div>

            <div class="grid grid-cols-3 gap-2 py-2 border-y border-slate-100 dark:border-darkBorder/60 font-mono text-[11px]">
              <div>
                <span class="block text-slate-400 text-[10px]">Framework</span>
                <strong class="text-blue-500 dark:text-blue-400 font-bold text-xs">4 Tiers</strong>
              </div>
              <div>
                <span class="block text-slate-400 text-[10px]">Statutory CPM</span>
                <strong class="text-slate-900 dark:text-white font-bold text-xs">30+ Nodes</strong>
              </div>
              <div>
                <span class="block text-slate-400 text-[10px]">Telemetry</span>
                <strong class="text-slate-900 dark:text-white font-bold text-xs">Gantt Active</strong>
              </div>
            </div>
          </div>

          <div class="flex items-center justify-between pt-3 mt-1">
            <div class="flex items-center gap-1.5 font-mono text-[10px] text-slate-400">
              <span class="px-2 py-0.5 rounded bg-slate-100 dark:bg-darkCard">Due Diligence</span>
              <span class="px-2 py-0.5 rounded bg-slate-100 dark:bg-darkCard">Quy Hoach</span>
            </div>
            <a href="https://invest.renewablevietnam.com/" class="inline-flex items-center gap-1 text-xs font-mono font-semibold text-blue-500 dark:text-blue-400 hover:underline">
              Launch M&amp;A Engine &rarr;
            </a>
          </div>
        </div>

      </div>
    </section>

    <!-- EXECUTIVE CHARTS & TELEMETRY SUITE -->
    <section class="space-y-4">
      <div class="flex items-center justify-between">
        <h2 class="text-xs sm:text-sm font-bold uppercase tracking-wider text-slate-700 dark:text-slate-300 flex items-center gap-2">
          <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
          National Visual Telemetry &amp; Infographics
        </h2>
        <span class="font-mono text-[10px] text-slate-400">Horizon: 2026&ndash;2030</span>
      </div>

      <!-- 4 Low-Profile Gauges -->
      <div class="grid grid-cols-2 lg:grid-cols-4 gap-3">
        <div class="bg-white/80 dark:bg-darkSurface/80 backdrop-blur-sm border border-slate-200/80 dark:border-darkBorder rounded-xl p-3.5 shadow-xs">
          <div class="flex justify-between items-baseline font-mono text-[10px]">
            <span class="text-slate-400">PDP8 RE Target</span>
            <strong class="text-emerald-600 dark:text-emerald-400 font-bold text-xs">31.5%</strong>
          </div>
          <div class="w-full bg-slate-100 dark:bg-darkCard h-1.5 rounded-full mt-2 overflow-hidden">
            <div class="bg-emerald-500 h-full rounded-full" style="width: 31.5%"></div>
          </div>
          <span class="block text-[9px] font-mono text-slate-400 mt-1.5">14.8 GW / 47.0 GW Target</span>
        </div>

        <div class="bg-white/80 dark:bg-darkSurface/80 backdrop-blur-sm border border-slate-200/80 dark:border-darkBorder rounded-xl p-3.5 shadow-xs">
          <div class="flex justify-between items-baseline font-mono text-[10px]">
            <span class="text-slate-400">Decree 80 DPPA</span>
            <strong class="text-teal-600 dark:text-teal-400 font-bold text-xs">100%</strong>
          </div>
          <div class="w-full bg-slate-100 dark:bg-darkCard h-1.5 rounded-full mt-2 overflow-hidden">
            <div class="bg-teal-500 h-full rounded-full" style="width: 100%"></div>
          </div>
          <span class="block text-[9px] font-mono text-slate-400 mt-1.5">Statutory Clearance Active</span>
        </div>

        <div class="bg-white/80 dark:bg-darkSurface/80 backdrop-blur-sm border border-slate-200/80 dark:border-darkBorder rounded-xl p-3.5 shadow-xs">
          <div class="flex justify-between items-baseline font-mono text-[10px]">
            <span class="text-slate-400">Expressway Fast EV</span>
            <strong class="text-amber-500 dark:text-amber-400 font-bold text-xs">95.2%</strong>
          </div>
          <div class="w-full bg-slate-100 dark:bg-darkCard h-1.5 rounded-full mt-2 overflow-hidden">
            <div class="bg-amber-500 h-full rounded-full" style="width: 95.2%"></div>
          </div>
          <span class="block text-[9px] font-mono text-slate-400 mt-1.5">National Route 1A &amp; CT.01</span>
        </div>

        <div class="bg-white/80 dark:bg-darkSurface/80 backdrop-blur-sm border border-slate-200/80 dark:border-darkBorder rounded-xl p-3.5 shadow-xs">
          <div class="flex justify-between items-baseline font-mono text-[10px]">
            <span class="text-slate-400">Eco-Park ESG Share</span>
            <strong class="text-blue-500 dark:text-blue-400 font-bold text-xs">42.0%</strong>
          </div>
          <div class="w-full bg-slate-100 dark:bg-darkCard h-1.5 rounded-full mt-2 overflow-hidden">
            <div class="bg-blue-500 h-full rounded-full" style="width: 42.0%"></div>
          </div>
          <span class="block text-[9px] font-mono text-slate-400 mt-1.5">71 of 168 Hubs Certified</span>
        </div>
      </div>

      <!-- 3 Charts Grid -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-4">
        <!-- Chart 1: Donut PDP8 Target (5 Cols) -->
        <div class="lg:col-span-5 bg-white/80 dark:bg-darkSurface/80 backdrop-blur-sm border border-slate-200/80 dark:border-darkBorder rounded-2xl p-5 shadow-xs flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-2 mb-2 border-b border-slate-100 dark:border-darkBorder">
              <span class="text-xs font-bold text-slate-800 dark:text-slate-200">PDP8 Statutory Capacity (2030)</span>
              <span class="font-mono text-[10px] text-emerald-600 dark:text-emerald-400 font-bold">150.5 GW</span>
            </div>
            <div class="relative h-56 flex items-center justify-center">
              <canvas id="pdp8MixChart"></canvas>
            </div>
          </div>
          <div class="grid grid-cols-3 gap-1.5 text-center font-mono text-[9px] pt-3 border-t border-slate-100 dark:border-darkBorder">
            <div class="p-1 rounded bg-slate-50 dark:bg-darkCard">
              <span class="text-slate-400 block">LNG Gas</span>
              <strong class="text-slate-700 dark:text-slate-200">37.3 GW</strong>
            </div>
            <div class="p-1 rounded bg-slate-50 dark:bg-darkCard">
              <span class="text-slate-400 block">Hydro</span>
              <strong class="text-slate-700 dark:text-slate-200">29.3 GW</strong>
            </div>
            <div class="p-1 rounded bg-slate-50 dark:bg-darkCard">
              <span class="text-slate-400 block">Wind/Solar</span>
              <strong class="text-emerald-500">40.7 GW</strong>
            </div>
          </div>
        </div>

        <!-- Chart 2: Regional Solar Potential (7 Cols) -->
        <div class="lg:col-span-7 bg-white/80 dark:bg-darkSurface/80 backdrop-blur-sm border border-slate-200/80 dark:border-darkBorder rounded-2xl p-5 shadow-xs flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-2 mb-2 border-b border-slate-100 dark:border-darkBorder">
              <span class="text-xs font-bold text-slate-800 dark:text-slate-200">Regional Eco-Industrial Solar Density</span>
              <span class="font-mono text-[10px] text-teal-600 dark:text-teal-400 font-bold">168 Hubs Cataloged</span>
            </div>
            <div class="relative h-56">
              <canvas id="regionalIndustrialChart"></canvas>
            </div>
          </div>
          <div class="flex items-center justify-between text-[10px] font-mono text-slate-400 pt-3 border-t border-slate-100 dark:border-darkBorder">
            <span>South: 3,120 MWp Solar</span>
            <span>North: 1,890 MWp Solar</span>
            <span>Central: 645 MWp Solar</span>
          </div>
        </div>

        <!-- Chart 3: EV Infrastructure (Full-width 12 Cols) -->
        <div class="lg:col-span-12 bg-white/80 dark:bg-darkSurface/80 backdrop-blur-sm border border-slate-200/80 dark:border-darkBorder rounded-2xl p-5 shadow-xs">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between pb-2 mb-3 border-b border-slate-100 dark:border-darkBorder gap-2">
            <div>
              <span class="text-xs font-bold text-slate-800 dark:text-slate-200">National EV Charging Infrastructure Share</span>
              <span class="text-[10px] text-slate-400 block">22,055+ verified ports categorized by CPO operator and DC Fast (&ge; 60kW) vs AC Level 2</span>
            </div>
            <span class="font-mono text-[10px] px-2 py-0.5 rounded bg-amber-500/10 text-amber-500 border border-amber-500/20 font-bold self-start sm:self-auto">
              22,055+ Ports &middot; 62% DC Fast
            </span>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
            <div class="md:col-span-8 relative h-44">
              <canvas id="evNetworkChart"></canvas>
            </div>
            <div class="md:col-span-4 grid grid-cols-2 gap-2 font-mono text-[10px]">
              <div class="p-2 rounded-xl bg-slate-50 dark:bg-darkCard border border-slate-100 dark:border-darkBorder">
                <span class="text-slate-400 block">VinFast</span>
                <strong class="text-amber-500 font-bold text-xs">18,500+</strong>
                <span class="text-[9px] text-slate-400 block">83.9% Share</span>
              </div>
              <div class="p-2 rounded-xl bg-slate-50 dark:bg-darkCard border border-slate-100 dark:border-darkBorder">
                <span class="text-slate-400 block">EV ONE</span>
                <strong class="text-slate-800 dark:text-slate-200 font-bold text-xs">1,800+</strong>
                <span class="text-[9px] text-slate-400 block">8.2% Share</span>
              </div>
              <div class="p-2 rounded-xl bg-slate-50 dark:bg-darkCard border border-slate-100 dark:border-darkBorder">
                <span class="text-slate-400 block">Others</span>
                <strong class="text-slate-800 dark:text-slate-200 font-bold text-xs">1,755+</strong>
                <span class="text-[9px] text-slate-400 block">7.9% Share</span>
              </div>
              <div class="p-2 rounded-xl bg-slate-50 dark:bg-darkCard border border-slate-100 dark:border-darkBorder">
                <span class="text-slate-400 block">DC Fast</span>
                <strong class="text-emerald-500 font-bold text-xs">13,674</strong>
                <span class="text-[9px] text-slate-400 block">&ge; 60kW</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

  </main>

  <!-- INSTITUTIONAL FOOTER -->
  <footer class="w-full bg-white dark:bg-darkSurface border-t border-slate-200/80 dark:border-darkBorder mt-8 py-6 px-4 sm:px-6 lg:px-8 text-xs text-slate-400 font-light">
    <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-4 font-mono text-[11px]">
      <div class="flex items-center gap-2.5">
        <img src="/assets/images/logo.svg" alt="Renewable Viet Nam" width="20" height="20" class="w-5 h-5 rounded" />
        <span class="text-slate-700 dark:text-slate-300 font-medium">RENEWABLE VIET NAM &middot; MASTER INTELLIGENCE ECOSYSTEM</span>
      </div>

      <div class="flex items-center gap-4">
        <a href="https://energy.renewablevietnam.com/" class="hover:text-emerald-500 transition-colors">Generation</a>
        <a href="https://industrial.renewablevietnam.com/" class="hover:text-teal-500 transition-colors">Industrial</a>
        <a href="https://ev.renewablevietnam.com/" class="hover:text-amber-500 transition-colors">EV Mobility</a>
        <a href="https://invest.renewablevietnam.com/" class="hover:text-blue-500 transition-colors">Investment</a>
      </div>

      <div class="text-slate-400">
        &copy; 2026 Renewable Viet Nam. Institutional Distribution.
      </div>
    </div>
  </footer>

  <!-- SCRIPT: THEME & DYNAMIC CHARTS -->
  <script>
    const themeBtn = document.getElementById('themeToggleBtn');
    const sunIcon = document.getElementById('sunIcon');
    const moonIcon = document.getElementById('moonIcon');

    let pdp8ChartInstance = null;
    let industrialChartInstance = null;
    let evChartInstance = null;

    function getChartThemeColors(isDark) {
      return {
        textColor: isDark ? '#94A3B8' : '#64748B',
        gridColor: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)',
        tooltipBg: isDark ? '#141D32' : '#FFFFFF',
        tooltipText: isDark ? '#F8FAFC' : '#0F172A',
        tooltipBorder: isDark ? 'rgba(255, 255, 255, 0.1)' : '#E2E8F0',
      };
    }

    function initCharts() {
      const isDark = document.documentElement.classList.contains('dark');
      const theme = getChartThemeColors(isDark);

      // 1. PDP8 Mix Chart
      const ctxPdp8 = document.getElementById('pdp8MixChart')?.getContext('2d');
      if (ctxPdp8) {
        if (pdp8ChartInstance) pdp8ChartInstance.destroy();
        pdp8ChartInstance = new Chart(ctxPdp8, {
          type: 'doughnut',
          data: {
            labels: ['Thermal LNG', 'Coal', 'Hydro', 'Onshore Wind', 'Solar', 'Biomass/Storage', 'Offshore Wind'],
            datasets: [{
              data: [37.3, 30.1, 29.3, 21.9, 12.8, 13.1, 6.0],
              backgroundColor: ['#3B82F6', '#64748B', '#06B6D4', '#10B981', '#F59E0B', '#8B5CF6', '#14B8A6'],
              borderWidth: 2,
              borderColor: isDark ? '#0E1424' : '#FFFFFF'
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            cutout: '72%',
            plugins: {
              legend: { display: false },
              tooltip: {
                backgroundColor: theme.tooltipBg,
                titleColor: theme.tooltipText,
                bodyColor: theme.tooltipText,
                borderColor: theme.tooltipBorder,
                borderWidth: 1,
                padding: 8,
                callbacks: {
                  label: ctx => ` ${ctx.label}: ${ctx.raw} GW (${((ctx.raw / 150.5) * 100).toFixed(1)}%)`
                }
              }
            }
          }
        });
      }

      // 2. Regional Eco-Industrial Chart
      const ctxInd = document.getElementById('regionalIndustrialChart')?.getContext('2d');
      if (ctxInd) {
        if (industrialChartInstance) industrialChartInstance.destroy();
        industrialChartInstance = new Chart(ctxInd, {
          type: 'bar',
          data: {
            labels: ['Southern Zone', 'Northern Zone', 'Central Zone'],
            datasets: [
              {
                label: 'Rooftop Solar (MWp)',
                data: [3120, 1890, 645],
                backgroundColor: '#14B8A6',
                borderRadius: 4,
                barPercentage: 0.5,
                yAxisID: 'y'
              },
              {
                label: 'Hubs (Count)',
                data: [92, 54, 22],
                backgroundColor: '#3B82F6',
                borderRadius: 4,
                barPercentage: 0.5,
                yAxisID: 'y1'
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: {
                position: 'top',
                labels: { color: theme.textColor, font: { size: 10, family: 'monospace' }, boxWidth: 10 }
              },
              tooltip: {
                backgroundColor: theme.tooltipBg,
                titleColor: theme.tooltipText,
                bodyColor: theme.tooltipText,
                borderColor: theme.tooltipBorder,
                borderWidth: 1,
                padding: 8
              }
            },
            scales: {
              x: { grid: { display: false }, ticks: { color: theme.textColor, font: { size: 10 } } },
              y: {
                type: 'linear',
                position: 'left',
                grid: { color: theme.gridColor },
                ticks: { color: theme.textColor, font: { size: 10, family: 'monospace' }, callback: val => `${val} MWp` }
              },
              y1: {
                type: 'linear',
                position: 'right',
                grid: { display: false },
                ticks: { color: theme.textColor, font: { size: 10, family: 'monospace' }, callback: val => `${val} Hubs` }
              }
            }
          }
        });
      }

      // 3. EV Charging Network Chart
      const ctxEv = document.getElementById('evNetworkChart')?.getContext('2d');
      if (ctxEv) {
        if (evChartInstance) evChartInstance.destroy();
        evChartInstance = new Chart(ctxEv, {
          type: 'bar',
          data: {
            labels: ['VinFast (V-GREEN)', 'EV ONE', 'Charge+ & Autel', 'Others'],
            datasets: [
              {
                label: 'DC Fast (\u2265 60kW)',
                data: [12000, 950, 480, 244],
                backgroundColor: '#F59E0B',
                borderRadius: 4,
                stack: 'Stack 0'
              },
              {
                label: 'AC Level 2 (\u2264 22kW)',
                data: [6500, 850, 650, 381],
                backgroundColor: '#94A3B8',
                borderRadius: 4,
                stack: 'Stack 0'
              }
            ]
          },
          options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: {
                position: 'top',
                labels: { color: theme.textColor, font: { size: 10, family: 'monospace' }, boxWidth: 10 }
              },
              tooltip: {
                backgroundColor: theme.tooltipBg,
                titleColor: theme.tooltipText,
                bodyColor: theme.tooltipText,
                borderColor: theme.tooltipBorder,
                borderWidth: 1,
                padding: 8
              }
            },
            scales: {
              x: {
                stacked: true,
                grid: { color: theme.gridColor },
                ticks: { color: theme.textColor, font: { size: 10, family: 'monospace' }, callback: val => `${val.toLocaleString()} ports` }
              },
              y: { stacked: true, grid: { display: false }, ticks: { color: theme.textColor, font: { size: 10 } } }
            }
          }
        });
      }
    }

    function applyTheme(isDark) {
      if (isDark) {
        document.documentElement.classList.add('dark');
        sunIcon?.classList.remove('hidden');
        moonIcon?.classList.add('hidden');
        localStorage.setItem('rvn_theme_v2', 'dark');
      } else {
        document.documentElement.classList.remove('dark');
        sunIcon?.classList.add('hidden');
        moonIcon?.classList.remove('hidden');
        localStorage.setItem('rvn_theme_v2', 'light');
      }
      initCharts();
    }

    const savedTheme = localStorage.getItem('rvn_theme_v2');
    applyTheme(savedTheme === 'dark');

    themeBtn?.addEventListener('click', () => {
      const isDark = document.documentElement.classList.contains('dark');
      applyTheme(!isDark);
    });

    window.addEventListener('resize', () => {
      initCharts();
    });
  </script>
</body>
</html>
"""

base_dir = r"G:\My Drive\7. AI\RenewableVietNam"
index_file = os.path.join(base_dir, "index.html")
rev12_file = os.path.join(base_dir, "index_Rev.012.html")

# Non-destructive sequential revision
with open(rev12_file, "w", encoding="utf-8") as f:
    f.write(DASHBOARD_HTML)
print(f"Created sequential revision: {rev12_file}")

with open(index_file, "w", encoding="utf-8") as f:
    f.write(DASHBOARD_HTML)
print(f"Updated active homepage: {index_file}")
