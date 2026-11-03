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
            inkMuted: '#475569',
            obsidian: '#070A12',
            darkSurface: '#0D1322',
            darkCard: '#131B2E',
            darkBorder: 'rgba(59, 130, 246, 0.16)',
            textDarkPrimary: '#F1F5F9',
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
    ::-webkit-scrollbar-thumb:hover { background: rgba(59, 130, 246, 0.4); }
  </style>
</head>
<body class="bg-alabaster dark:bg-obsidian text-inkPrimary dark:text-textDarkPrimary min-h-screen flex flex-col antialiased selection:bg-teal-500 selection:text-white transition-colors duration-200">

  <!-- TOP EXECUTIVE NAVIGATION BAR -->
  <header class="sticky top-0 z-40 w-full bg-alabaster/95 dark:bg-obsidian/95 backdrop-blur-md border-b border-borderSlate dark:border-darkBorder px-3 sm:px-6 lg:px-8 transition-colors shadow-sm">
    <div class="w-full max-w-7xl mx-auto flex flex-col gap-2 py-2.5 sm:py-3.5">
      <div class="flex items-center justify-between w-full">
        <div class="flex items-center gap-6">
          <a href="https://renewablevietnam.com/" class="flex items-center gap-2.5 sm:gap-3 group shrink-0" aria-label="Renewable Vietnam — home">
            <img src="/assets/images/logo.svg" alt="Renewable Viet Nam Mark" width="34" height="34" class="w-8 h-8 sm:w-8.5 sm:h-8.5 rounded-lg shrink-0 shadow-sm" />
            <span class="text-[11px] sm:text-xs font-mono uppercase tracking-[0.14em] sm:tracking-[0.24em] text-inkPrimary dark:text-textDarkPrimary font-semibold">
              RENEWABLE INFRASTRUCTURE
            </span>
          </a>

          <!-- Desktop Quick Jump Navigation -->
          <nav class="hidden md:flex items-center gap-1 font-mono text-[11px] tracking-wider text-inkMuted dark:text-textDarkMuted">
            <a href="https://renewablevietnam.com/" class="px-2.5 py-1 rounded-md text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20 transition-colors">Master Cockpit</a>
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

        <!-- Controls -->
        <div class="flex items-center gap-2">
          <button id="themeToggleBtn" aria-label="Toggle Theme" class="flex items-center justify-center w-8.5 h-8.5 rounded-lg bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder shadow-sm hover:border-slate-400 dark:hover:border-slate-500 text-inkMuted dark:text-textDarkMuted transition-all cursor-pointer">
            <svg id="sunIcon" class="hidden w-4 h-4 text-amber-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.6">
              <path stroke-linecap="round" stroke-linejoin="round" d="M12 3v2.25m6.364.386-1.591 1.591M21 12h-2.25m-.386 6.364-1.591-1.591M12 18.75V21m-4.773-4.227-1.591 1.591M5.25 12H3m4.227-4.773L5.636 5.636M15.75 12a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0Z" />
            </svg>
            <svg id="moonIcon" class="w-4 h-4 text-slate-700 dark:text-slate-300" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.6">
              <path stroke-linecap="round" stroke-linejoin="round" d="M21.752 15.002A9.72 9.72 0 0 1 18 15.75c-5.385 0-9.75-4.365-9.75-9.75 0-1.33.266-2.597.748-3.752A9.753 9.753 0 0 0 3 11.25C3 16.635 7.365 21 12.75 21a9.753 9.753 0 0 0 9.002-5.998Z" />
            </svg>
          </button>
        </div>
      </div>

      <!-- Mobile Touch Navigation Carousel -->
      <nav class="flex md:hidden items-center gap-1.5 overflow-x-auto no-scrollbar pt-1.5 pb-0.5 font-mono text-[11px] tracking-wider whitespace-nowrap w-full -mx-3 px-3 sm:mx-0 sm:px-0">
        <a href="https://renewablevietnam.com/" class="px-2.5 py-1.5 rounded-lg text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20 shrink-0">Cockpit</a>
        <a href="https://energy.renewablevietnam.com/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-emerald-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">PDP8 Energy</a>
        <a href="https://industrial.renewablevietnam.com/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-teal-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">Green Industrial</a>
        <a href="https://ev.renewablevietnam.com/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-amber-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">EV Tech</a>
        <a href="https://invest.renewablevietnam.com/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-blue-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">Investment M&A</a>
      </nav>
    </div>
  </header>

  <!-- MAIN MASTER WORKSPACE -->
  <main class="relative z-10 flex-1 w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 sm:py-8 space-y-8 sm:space-y-10">

    <!-- HERO & MACRO TELEMETRY HEADER -->
    <section class="space-y-4">
      <div class="flex flex-col md:flex-row md:items-end justify-between gap-4">
        <div class="space-y-1.5 max-w-3xl">
          <div class="flex items-center gap-2">
            <span class="font-mono text-[10px] uppercase tracking-wider text-teal-600 dark:text-teal-400 font-semibold px-2 py-0.5 rounded bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20">
              National Infrastructure Telemetry
            </span>
            <span class="font-mono text-[10px] text-slate-500 dark:text-slate-400 border border-slate-200 dark:border-darkBorder px-1.5 py-0.5 rounded">
              Decree 80 / PDP8 Compliant
            </span>
          </div>
          <h1 class="text-2xl sm:text-3xl font-semibold tracking-tight text-inkPrimary dark:text-textDarkPrimary">
            Vietnam Clean Energy &amp; Ecological Transition Master Cockpit
          </h1>
          <p class="text-xs sm:text-sm text-inkMuted dark:text-textDarkMuted font-light leading-relaxed">
            Integrated telemetry uniting statutory power generation, eco-industrial master planning, EV mobility corridors, and M&amp;A legal execution.
          </p>
        </div>

        <div class="flex items-center gap-2 shrink-0">
          <div class="font-mono text-[10px] sm:text-[11px] text-inkMuted dark:text-textDarkMuted bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder p-2 sm:p-2.5 rounded-xl shadow-sm flex items-center gap-2">
            <span class="inline-block w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
            <span>SYSTEM STATUS &middot; <strong class="text-slate-900 dark:text-white font-semibold">4 ACTIVE SUBDOMAINS</strong> &middot; <span class="text-emerald-600 dark:text-emerald-400 font-medium">100% OPERATIONAL</span></span>
          </div>
        </div>
      </div>

      <!-- 4-PILLAR MACRO TELEMETRY GRID -->
      <div class="grid grid-cols-2 md:grid-cols-4 gap-2.5 sm:gap-3.5 pt-1">
        <!-- Pillar 1: PDP8 Generation (energy) -->
        <a href="https://energy.renewablevietnam.com/" class="p-3.5 sm:p-4 rounded-xl bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder shadow-sm flex flex-col justify-between hover:border-emerald-500/50 hover:shadow-md transition-all group">
          <div class="flex items-center justify-between">
            <span class="font-mono text-[10px] tracking-wider uppercase text-emerald-600 dark:text-emerald-400 font-semibold">Clean Generation</span>
            <span class="inline-block w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
          </div>
          <div class="my-2">
            <div class="flex items-baseline gap-1.5">
              <span class="text-xl sm:text-2xl font-mono font-bold text-inkPrimary dark:text-textDarkPrimary group-hover:text-emerald-500 transition-colors">960+</span>
              <span class="text-xs font-mono text-inkMuted dark:text-textDarkMuted">Plants</span>
            </div>
            <div class="w-full bg-slate-100 dark:bg-darkCard h-1 rounded-full mt-1.5 overflow-hidden">
              <div class="bg-emerald-500 h-full rounded-full" style="width: 71.4%"></div>
            </div>
          </div>
          <p class="text-[10px] sm:text-[11px] font-mono text-inkMuted dark:text-textDarkMuted">107.5 GW Statutory Pipeline</p>
        </a>

        <!-- Pillar 2: Green Industrial (industrial) -->
        <a href="https://industrial.renewablevietnam.com/" class="p-3.5 sm:p-4 rounded-xl bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder shadow-sm flex flex-col justify-between hover:border-teal-500/50 hover:shadow-md transition-all group">
          <div class="flex items-center justify-between">
            <span class="font-mono text-[10px] tracking-wider uppercase text-teal-600 dark:text-teal-400 font-semibold">Industrial Siting</span>
            <span class="inline-block w-1.5 h-1.5 rounded-full bg-teal-500"></span>
          </div>
          <div class="my-2">
            <div class="flex items-baseline gap-1.5">
              <span class="text-xl sm:text-2xl font-mono font-bold text-inkPrimary dark:text-textDarkPrimary group-hover:text-teal-500 transition-colors">168</span>
              <span class="text-xs font-mono text-inkMuted dark:text-textDarkMuted">Hubs</span>
            </div>
            <div class="w-full bg-slate-100 dark:bg-darkCard h-1 rounded-full mt-1.5 overflow-hidden">
              <div class="bg-teal-500 h-full rounded-full" style="width: 62.0%"></div>
            </div>
          </div>
          <p class="text-[10px] sm:text-[11px] font-mono text-inkMuted dark:text-textDarkMuted">104.4K ha &middot; 5,655 MWp Solar</p>
        </a>

        <!-- Pillar 3: EV Infrastructure (ev) -->
        <a href="https://ev.renewablevietnam.com/" class="p-3.5 sm:p-4 rounded-xl bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder shadow-sm flex flex-col justify-between hover:border-amber-500/50 hover:shadow-md transition-all group">
          <div class="flex items-center justify-between">
            <span class="font-mono text-[10px] tracking-wider uppercase text-amber-500 dark:text-amber-400 font-semibold">EV Mobility</span>
            <span class="inline-block w-1.5 h-1.5 rounded-full bg-amber-500"></span>
          </div>
          <div class="my-2">
            <div class="flex items-baseline gap-1.5">
              <span class="text-xl sm:text-2xl font-mono font-bold text-inkPrimary dark:text-textDarkPrimary group-hover:text-amber-500 transition-colors">22,055+</span>
              <span class="text-xs font-mono text-inkMuted dark:text-textDarkMuted">Ports</span>
            </div>
            <div class="w-full bg-slate-100 dark:bg-darkCard h-1 rounded-full mt-1.5 overflow-hidden">
              <div class="bg-amber-500 h-full rounded-full" style="width: 83.9%"></div>
            </div>
          </div>
          <p class="text-[10px] sm:text-[11px] font-mono text-inkMuted dark:text-textDarkMuted">63 Provinces &middot; DC Fast Grid</p>
        </a>

        <!-- Pillar 4: Investment Engine (invest) -->
        <a href="https://invest.renewablevietnam.com/" class="p-3.5 sm:p-4 rounded-xl bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder shadow-sm flex flex-col justify-between hover:border-blue-500/50 hover:shadow-md transition-all group">
          <div class="flex items-center justify-between">
            <span class="font-mono text-[10px] tracking-wider uppercase text-blue-500 dark:text-blue-400 font-semibold">M&amp;A Permitting</span>
            <span class="inline-block w-1.5 h-1.5 rounded-full bg-blue-500"></span>
          </div>
          <div class="my-2">
            <div class="flex items-baseline gap-1.5">
              <span class="text-xl sm:text-2xl font-mono font-bold text-inkPrimary dark:text-textDarkPrimary group-hover:text-blue-500 transition-colors">4-Tier</span>
              <span class="text-xs font-mono text-inkMuted dark:text-textDarkMuted">Audit</span>
            </div>
            <div class="w-full bg-slate-100 dark:bg-darkCard h-1 rounded-full mt-1.5 overflow-hidden">
              <div class="bg-blue-500 h-full rounded-full" style="width: 100.0%"></div>
            </div>
          </div>
          <p class="text-[10px] sm:text-[11px] font-mono text-inkMuted dark:text-textDarkMuted">30+ CPM Steps &middot; Gantt Engine</p>
        </a>
      </div>
    </section>

    <!-- SECTION 1: INTERACTIVE 5-STAGE TRANSITION WORKFLOW -->
    <section class="p-5 sm:p-6 rounded-2xl bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder shadow-sm space-y-4">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-borderSlate/60 dark:border-darkBorder/60 pb-3">
        <div>
          <h2 class="text-base sm:text-lg font-semibold tracking-tight text-inkPrimary dark:text-textDarkPrimary flex items-center gap-2">
            <svg class="w-4.5 h-4.5 text-teal-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
            End-to-End Ecological Transition Architecture
          </h2>
          <p class="text-xs text-inkMuted dark:text-textDarkMuted font-light">
            Standardized 5-stage lifecycle from statutory resource zoning to corporate offtake and mobility corridors.
          </p>
        </div>
        <div class="flex items-center gap-1.5 self-start sm:self-auto font-mono text-[10px] text-teal-600 dark:text-teal-400 bg-teal-500/10 px-2 py-0.5 rounded border border-teal-500/20">
          <span class="w-1.5 h-1.5 rounded-full bg-teal-500"></span>
          <span>Bilateral Direct Offtake Flow</span>
        </div>
      </div>

      <!-- 5-Step Connected Flow Cards -->
      <div class="grid grid-cols-1 md:grid-cols-5 gap-3 pt-1">
        <!-- Stage 1 -->
        <a href="https://energy.renewablevietnam.com/" class="group p-3.5 rounded-xl bg-slate-50 dark:bg-darkCard border border-borderSlate dark:border-darkBorder/70 hover:border-emerald-500/60 transition-all flex flex-col justify-between">
          <div class="space-y-1.5">
            <div class="flex items-center justify-between">
              <span class="font-mono text-[9px] uppercase font-bold text-emerald-600 dark:text-emerald-400 bg-emerald-500/10 px-1.5 py-0.5 rounded border border-emerald-500/20">STAGE 01</span>
              <span class="text-[10px] font-mono text-slate-400 group-hover:text-emerald-500 transition-colors">&rarr;</span>
            </div>
            <h3 class="text-xs font-semibold text-inkPrimary dark:text-textDarkPrimary group-hover:text-emerald-500 transition-colors">
              PDP8 Resource Zoning
            </h3>
            <p class="text-[11px] text-inkMuted dark:text-textDarkMuted leading-relaxed font-light">
              Provincial quota allocation across onshore/offshore wind, utility solar, and hydro.
            </p>
          </div>
          <div class="mt-3 pt-2 border-t border-borderSlate/50 dark:border-darkBorder/50 flex items-center justify-between text-[10px] font-mono text-slate-500">
            <span>Pipeline</span>
            <strong class="text-emerald-500">107.5 GW</strong>
          </div>
        </a>

        <!-- Stage 2 -->
        <a href="https://invest.renewablevietnam.com/" class="group p-3.5 rounded-xl bg-slate-50 dark:bg-darkCard border border-borderSlate dark:border-darkBorder/70 hover:border-blue-500/60 transition-all flex flex-col justify-between">
          <div class="space-y-1.5">
            <div class="flex items-center justify-between">
              <span class="font-mono text-[9px] uppercase font-bold text-blue-500 dark:text-blue-400 bg-blue-500/10 px-1.5 py-0.5 rounded border border-blue-500/20">STAGE 02</span>
              <span class="text-[10px] font-mono text-slate-400 group-hover:text-blue-500 transition-colors">&rarr;</span>
            </div>
            <h3 class="text-xs font-semibold text-inkPrimary dark:text-textDarkPrimary group-hover:text-blue-500 transition-colors">
              4-Tier Permitting CPM
            </h3>
            <p class="text-[11px] text-inkMuted dark:text-textDarkMuted leading-relaxed font-light">
              Investment policy, land lease, EIA feasibility, and fire safety (PCCC) validation.
            </p>
          </div>
          <div class="mt-3 pt-2 border-t border-borderSlate/50 dark:border-darkBorder/50 flex items-center justify-between text-[10px] font-mono text-slate-500">
            <span>Critical Path</span>
            <strong class="text-blue-500">30+ Nodes</strong>
          </div>
        </a>

        <!-- Stage 3 -->
        <a href="https://energy.renewablevietnam.com/" class="group p-3.5 rounded-xl bg-slate-50 dark:bg-darkCard border border-borderSlate dark:border-darkBorder/70 hover:border-emerald-500/60 transition-all flex flex-col justify-between">
          <div class="space-y-1.5">
            <div class="flex items-center justify-between">
              <span class="font-mono text-[9px] uppercase font-bold text-emerald-600 dark:text-emerald-400 bg-emerald-500/10 px-1.5 py-0.5 rounded border border-emerald-500/20">STAGE 03</span>
              <span class="text-[10px] font-mono text-slate-400 group-hover:text-emerald-500 transition-colors">&rarr;</span>
            </div>
            <h3 class="text-xs font-semibold text-inkPrimary dark:text-textDarkPrimary group-hover:text-emerald-500 transition-colors">
              Grid Interconnection
            </h3>
            <p class="text-[11px] text-inkMuted dark:text-textDarkMuted leading-relaxed font-light">
              500kV/220kV substation access, intertie agreements, and dispatch simulation.
            </p>
          </div>
          <div class="mt-3 pt-2 border-t border-borderSlate/50 dark:border-darkBorder/50 flex items-center justify-between text-[10px] font-mono text-slate-500">
            <span>Backbone Loop</span>
            <strong class="text-emerald-500">500kV / 220kV</strong>
          </div>
        </a>

        <!-- Stage 4 -->
        <a href="https://industrial.renewablevietnam.com/" class="group p-3.5 rounded-xl bg-slate-50 dark:bg-darkCard border border-borderSlate dark:border-darkBorder/70 hover:border-teal-500/60 transition-all flex flex-col justify-between">
          <div class="space-y-1.5">
            <div class="flex items-center justify-between">
              <span class="font-mono text-[9px] uppercase font-bold text-teal-600 dark:text-teal-400 bg-teal-500/10 px-1.5 py-0.5 rounded border border-teal-500/20">STAGE 04</span>
              <span class="text-[10px] font-mono text-slate-400 group-hover:text-teal-500 transition-colors">&rarr;</span>
            </div>
            <h3 class="text-xs font-semibold text-inkPrimary dark:text-textDarkPrimary group-hover:text-teal-500 transition-colors">
              Industrial Offtake (DPPA)
            </h3>
            <p class="text-[11px] text-inkMuted dark:text-textDarkMuted leading-relaxed font-light">
              Decree 80 bilateral wheeling, rooftop solar adoption, and RE100 compliance.
            </p>
          </div>
          <div class="mt-3 pt-2 border-t border-borderSlate/50 dark:border-darkBorder/50 flex items-center justify-between text-[10px] font-mono text-slate-500">
            <span>Rooftop Solar</span>
            <strong class="text-teal-500">5,655 MWp</strong>
          </div>
        </a>

        <!-- Stage 5 -->
        <a href="https://ev.renewablevietnam.com/" class="group p-3.5 rounded-xl bg-slate-50 dark:bg-darkCard border border-borderSlate dark:border-darkBorder/70 hover:border-amber-500/60 transition-all flex flex-col justify-between">
          <div class="space-y-1.5">
            <div class="flex items-center justify-between">
              <span class="font-mono text-[9px] uppercase font-bold text-amber-500 dark:text-amber-400 bg-amber-500/10 px-1.5 py-0.5 rounded border border-amber-500/20">STAGE 05</span>
              <span class="text-[10px] font-mono text-slate-400 group-hover:text-amber-500 transition-colors">&rarr;</span>
            </div>
            <h3 class="text-xs font-semibold text-inkPrimary dark:text-textDarkPrimary group-hover:text-amber-500 transition-colors">
              E-Mobility Corridors
            </h3>
            <p class="text-[11px] text-inkMuted dark:text-textDarkMuted leading-relaxed font-light">
              DC fast-charging hubs, freight logistics electrification, and national highway corridors.
            </p>
          </div>
          <div class="mt-3 pt-2 border-t border-borderSlate/50 dark:border-darkBorder/50 flex items-center justify-between text-[10px] font-mono text-slate-500">
            <span>Verified Ports</span>
            <strong class="text-amber-500">22,055+</strong>
          </div>
        </a>
      </div>
    </section>

    <!-- SECTION 2: EXECUTIVE CHARTS & INFOGRAPHICS SUITE -->
    <section class="space-y-4">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
        <div>
          <h2 class="text-base sm:text-lg font-semibold tracking-tight text-inkPrimary dark:text-textDarkPrimary flex items-center gap-2">
            <svg class="w-4.5 h-4.5 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>
            Macro Transition Infographics &amp; Telemetry Charts
          </h2>
          <p class="text-xs text-inkMuted dark:text-textDarkMuted font-light">
            Real-time visual benchmarks across capacity targets, charging infrastructure share, and industrial footprint.
          </p>
        </div>
        <div class="flex items-center gap-2">
          <span class="font-mono text-[10px] text-slate-500 dark:text-slate-400 bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder px-2.5 py-1 rounded-lg shadow-sm">
            DATA HORIZON: 2026&ndash;2030
          </span>
        </div>
      </div>

      <!-- 4 INFOGRAPHIC PROGRESS GAUGES -->
      <div class="grid grid-cols-2 lg:grid-cols-4 gap-3 sm:gap-4">
        <!-- Gauge 1 -->
        <div class="p-4 rounded-xl bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder shadow-sm flex flex-col justify-between">
          <div class="flex items-center justify-between">
            <span class="font-mono text-[10px] uppercase text-emerald-600 dark:text-emerald-400 font-semibold">PDP8 2030 Clean Goal</span>
            <span class="font-mono text-[11px] font-bold text-emerald-500">31.5%</span>
          </div>
          <div class="my-2.5">
            <div class="w-full bg-slate-100 dark:bg-darkCard h-2 rounded-full overflow-hidden">
              <div class="bg-emerald-500 h-full rounded-full transition-all duration-500" style="width: 31.5%"></div>
            </div>
          </div>
          <div class="flex items-center justify-between text-[10px] font-mono text-inkMuted dark:text-textDarkMuted">
            <span>Target: 47.0 GW RE</span>
            <span>14.8 GW Active</span>
          </div>
        </div>

        <!-- Gauge 2 -->
        <div class="p-4 rounded-xl bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder shadow-sm flex flex-col justify-between">
          <div class="flex items-center justify-between">
            <span class="font-mono text-[10px] uppercase text-teal-600 dark:text-teal-400 font-semibold">Decree 80 DPPA Status</span>
            <span class="font-mono text-[11px] font-bold text-teal-500">100%</span>
          </div>
          <div class="my-2.5">
            <div class="w-full bg-slate-100 dark:bg-darkCard h-2 rounded-full overflow-hidden">
              <div class="bg-teal-500 h-full rounded-full transition-all duration-500" style="width: 100%"></div>
            </div>
          </div>
          <div class="flex items-center justify-between text-[10px] font-mono text-inkMuted dark:text-textDarkMuted">
            <span>Statutory Clearance</span>
            <span>Operational Active</span>
          </div>
        </div>

        <!-- Gauge 3 -->
        <div class="p-4 rounded-xl bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder shadow-sm flex flex-col justify-between">
          <div class="flex items-center justify-between">
            <span class="font-mono text-[10px] uppercase text-amber-500 dark:text-amber-400 font-semibold">Expressway Fast Charge</span>
            <span class="font-mono text-[11px] font-bold text-amber-500">95.2%</span>
          </div>
          <div class="my-2.5">
            <div class="w-full bg-slate-100 dark:bg-darkCard h-2 rounded-full overflow-hidden">
              <div class="bg-amber-500 h-full rounded-full transition-all duration-500" style="width: 95.2%"></div>
            </div>
          </div>
          <div class="flex items-center justify-between text-[10px] font-mono text-inkMuted dark:text-textDarkMuted">
            <span>Route 1A &amp; North-South</span>
            <span>&le; 50km Spacing</span>
          </div>
        </div>

        <!-- Gauge 4 -->
        <div class="p-4 rounded-xl bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder shadow-sm flex flex-col justify-between">
          <div class="flex items-center justify-between">
            <span class="font-mono text-[10px] uppercase text-blue-500 dark:text-blue-400 font-semibold">Eco-Park ESG Conversion</span>
            <span class="font-mono text-[11px] font-bold text-blue-500">42.0%</span>
          </div>
          <div class="my-2.5">
            <div class="w-full bg-slate-100 dark:bg-darkCard h-2 rounded-full overflow-hidden">
              <div class="bg-blue-500 h-full rounded-full transition-all duration-500" style="width: 42.0%"></div>
            </div>
          </div>
          <div class="flex items-center justify-between text-[10px] font-mono text-inkMuted dark:text-textDarkMuted">
            <span>168 Cataloged Hubs</span>
            <span>71 Certified Eco</span>
          </div>
        </div>
      </div>

      <!-- 3 INTERACTIVE TELEMETRY CHARTS (2-Column Grid) -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-4">
        <!-- Chart 1: PDP8 Generation Target Mix (5 cols) -->
        <div class="lg:col-span-5 p-4 sm:p-5 rounded-2xl bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder shadow-sm flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between border-b border-borderSlate/60 dark:border-darkBorder/60 pb-2.5 mb-3">
              <div>
                <h3 class="text-xs sm:text-sm font-semibold text-inkPrimary dark:text-textDarkPrimary">
                  PDP8 Statutory Generation Mix (2030 Horizon)
                </h3>
                <p class="text-[10px] text-inkMuted dark:text-textDarkMuted font-light">
                  Target planned capacity: 150.5 GW national total.
                </p>
              </div>
              <span class="font-mono text-[10px] font-bold text-emerald-500 bg-emerald-500/10 px-2 py-0.5 rounded border border-emerald-500/20">
                150.5 GW
              </span>
            </div>
            <div class="relative h-56 sm:h-64 flex items-center justify-center">
              <canvas id="pdp8MixChart"></canvas>
            </div>
          </div>
          <div class="pt-3 border-t border-borderSlate/60 dark:border-darkBorder/60 grid grid-cols-3 gap-1.5 text-center font-mono text-[10px]">
            <div class="p-1.5 rounded bg-slate-50 dark:bg-darkCard">
              <span class="block text-slate-400">Thermal LNG</span>
              <strong class="text-slate-700 dark:text-slate-200">37.3 GW</strong>
            </div>
            <div class="p-1.5 rounded bg-slate-50 dark:bg-darkCard">
              <span class="block text-slate-400">Hydro</span>
              <strong class="text-slate-700 dark:text-slate-200">29.3 GW</strong>
            </div>
            <div class="p-1.5 rounded bg-slate-50 dark:bg-darkCard">
              <span class="block text-slate-400">Wind/Solar</span>
              <strong class="text-emerald-500">40.7 GW</strong>
            </div>
          </div>
        </div>

        <!-- Chart 2: Regional Eco-Industrial Solar Density (7 cols) -->
        <div class="lg:col-span-7 p-4 sm:p-5 rounded-2xl bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder shadow-sm flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between border-b border-borderSlate/60 dark:border-darkBorder/60 pb-2.5 mb-3">
              <div>
                <h3 class="text-xs sm:text-sm font-semibold text-inkPrimary dark:text-textDarkPrimary">
                  Regional Eco-Industrial Density &amp; Rooftop Solar Potential
                </h3>
                <p class="text-[10px] text-inkMuted dark:text-textDarkMuted font-light">
                  Tier-1 hub concentration vs available rooftop solar capacity across key economic zones.
                </p>
              </div>
              <span class="font-mono text-[10px] font-bold text-teal-600 dark:text-teal-400 bg-teal-500/10 px-2 py-0.5 rounded border border-teal-500/20">
                168 Hubs
              </span>
            </div>
            <div class="relative h-56 sm:h-64">
              <canvas id="regionalIndustrialChart"></canvas>
            </div>
          </div>
          <div class="pt-3 border-t border-borderSlate/60 dark:border-darkBorder/60 flex items-center justify-between text-[10px] font-mono text-inkMuted dark:text-textDarkMuted">
            <span>South: 58.2k ha &middot; 3,120 MWp</span>
            <span>North: 34.8k ha &middot; 1,890 MWp</span>
            <span>Central: 11.4k ha &middot; 645 MWp</span>
          </div>
        </div>

        <!-- Chart 3: National EV Charging Network Ecosystem (Full-width 12 cols) -->
        <div class="lg:col-span-12 p-4 sm:p-5 rounded-2xl bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder shadow-sm">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between border-b border-borderSlate/60 dark:border-darkBorder/60 pb-2.5 mb-3 gap-2">
            <div>
              <h3 class="text-xs sm:text-sm font-semibold text-inkPrimary dark:text-textDarkPrimary">
                National EV Charging Infrastructure: Network Share &amp; Charger Velocity
              </h3>
              <p class="text-[10px] text-inkMuted dark:text-textDarkMuted font-light">
                22,055+ verified ports across 63 provinces categorized by operator footprint and DC Fast vs AC Level 2 throughput.
              </p>
            </div>
            <div class="flex items-center gap-2 font-mono text-[10px]">
              <span class="px-2 py-0.5 rounded bg-amber-500/10 text-amber-500 border border-amber-500/20 font-bold">
                22,055+ Total Ports
              </span>
              <span class="px-2 py-0.5 rounded bg-slate-100 dark:bg-darkCard text-slate-500 border border-borderSlate dark:border-darkBorder">
                62% DC Fast
              </span>
            </div>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
            <div class="md:col-span-7 relative h-48 sm:h-52">
              <canvas id="evNetworkChart"></canvas>
            </div>
            <div class="md:col-span-5 grid grid-cols-2 gap-2 text-[10px] font-mono">
              <div class="p-2.5 rounded-xl bg-slate-50 dark:bg-darkCard border border-borderSlate/60 dark:border-darkBorder/60">
                <span class="block text-slate-400">VinFast V-GREEN</span>
                <strong class="text-sm font-bold text-amber-500">18,500+</strong>
                <span class="block text-slate-400 mt-0.5">83.9% Market Dominance</span>
              </div>
              <div class="p-2.5 rounded-xl bg-slate-50 dark:bg-darkCard border border-borderSlate/60 dark:border-darkBorder/60">
                <span class="block text-slate-400">EV ONE Network</span>
                <strong class="text-sm font-bold text-inkPrimary dark:text-textDarkPrimary">1,800+</strong>
                <span class="block text-slate-400 mt-0.5">8.2% Commercial Hubs</span>
              </div>
              <div class="p-2.5 rounded-xl bg-slate-50 dark:bg-darkCard border border-borderSlate/60 dark:border-darkBorder/60">
                <span class="block text-slate-400">Charge+ / Autel / Others</span>
                <strong class="text-sm font-bold text-inkPrimary dark:text-textDarkPrimary">1,755+</strong>
                <span class="block text-slate-400 mt-0.5">7.9% Independent CPOs</span>
              </div>
              <div class="p-2.5 rounded-xl bg-slate-50 dark:bg-darkCard border border-borderSlate/60 dark:border-darkBorder/60">
                <span class="block text-slate-400">CCS2 / DC Fast Ports</span>
                <strong class="text-sm font-bold text-emerald-500">13,674</strong>
                <span class="block text-slate-400 mt-0.5">&ge; 60kW Fast Charging</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 3: SUBDOMAIN COMMAND LAUNCHPAD -->
    <section class="space-y-4">
      <div class="flex items-center justify-between border-b border-borderSlate/60 dark:border-darkBorder/60 pb-2">
        <div>
          <h2 class="text-base sm:text-lg font-semibold tracking-tight text-inkPrimary dark:text-textDarkPrimary flex items-center gap-2">
            <svg class="w-4.5 h-4.5 text-teal-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"/></svg>
            Subdomain Command Launchpad
          </h2>
          <p class="text-xs text-inkMuted dark:text-textDarkMuted font-light">
            Dedicated high-throughput specialized intelligence portals hosted under independent edge subdomains.
          </p>
        </div>
      </div>

      <!-- 4 Subdomain Master Cards (2x2 Grid) -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 sm:gap-5">

        <!-- Card 1: energy.renewablevietnam.com -->
        <div class="p-4 sm:p-5 rounded-2xl bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder shadow-sm flex flex-col justify-between hover:border-emerald-500/60 transition-all group">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <span class="font-mono text-[10px] font-bold uppercase tracking-wider text-emerald-600 dark:text-emerald-400 px-2 py-0.5 rounded bg-emerald-500/10 border border-emerald-500/20">
                energy.renewablevietnam.com
              </span>
              <span class="inline-flex items-center gap-1 font-mono text-[10px] text-emerald-600 dark:text-emerald-400">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span> Live Edge
              </span>
            </div>

            <div>
              <h3 class="text-sm sm:text-base font-bold text-inkPrimary dark:text-textDarkPrimary group-hover:text-emerald-500 transition-colors">
                PDP8 Clean Energy &amp; Power Grid Atlas
              </h3>
              <p class="text-xs text-inkMuted dark:text-textDarkMuted font-light mt-1">
                Geospatial statutory atlas of Vietnam's national clean generation assets, wind, solar, and 500kV/220kV interties.
              </p>
            </div>

            <!-- Metric Chips -->
            <div class="grid grid-cols-3 gap-2 py-2 border-y border-borderSlate/60 dark:border-darkBorder/60">
              <div class="text-center">
                <span class="block text-xs font-mono font-bold text-emerald-500">960+</span>
                <span class="text-[10px] text-inkMuted dark:text-textDarkMuted">Plants</span>
              </div>
              <div class="text-center">
                <span class="block text-xs font-mono font-bold text-inkPrimary dark:text-textDarkPrimary">107.5 GW</span>
                <span class="text-[10px] text-inkMuted dark:text-textDarkMuted">Pipeline</span>
              </div>
              <div class="text-center">
                <span class="block text-xs font-mono font-bold text-slate-500">500kV/220kV</span>
                <span class="text-[10px] text-inkMuted dark:text-textDarkMuted">Grid Loops</span>
              </div>
            </div>

            <!-- Feature Tags -->
            <div class="flex flex-wrap gap-1.5 pt-0.5">
              <span class="font-mono text-[9px] px-2 py-0.5 rounded bg-slate-100 dark:bg-darkCard text-slate-600 dark:text-slate-300">Onshore Wind</span>
              <span class="font-mono text-[9px] px-2 py-0.5 rounded bg-slate-100 dark:bg-darkCard text-slate-600 dark:text-slate-300">Offshore Wind</span>
              <span class="font-mono text-[9px] px-2 py-0.5 rounded bg-slate-100 dark:bg-darkCard text-slate-600 dark:text-slate-300">Utility Solar</span>
              <span class="font-mono text-[9px] px-2 py-0.5 rounded bg-slate-100 dark:bg-darkCard text-slate-600 dark:text-slate-300">DPPA Corridors</span>
            </div>
          </div>

          <div class="pt-4">
            <a href="https://energy.renewablevietnam.com/" class="w-full flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-mono text-xs font-semibold shadow-sm transition-all">
              <span>Launch PDP8 Energy Atlas</span>
              <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
            </a>
          </div>
        </div>

        <!-- Card 2: industrial.renewablevietnam.com -->
        <div class="p-4 sm:p-5 rounded-2xl bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder shadow-sm flex flex-col justify-between hover:border-teal-500/60 transition-all group">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <span class="font-mono text-[10px] font-bold uppercase tracking-wider text-teal-600 dark:text-teal-400 px-2 py-0.5 rounded bg-teal-500/10 border border-teal-500/20">
                industrial.renewablevietnam.com
              </span>
              <span class="inline-flex items-center gap-1 font-mono text-[10px] text-teal-600 dark:text-teal-400">
                <span class="w-1.5 h-1.5 rounded-full bg-teal-500"></span> Live Edge
              </span>
            </div>

            <div>
              <h3 class="text-sm sm:text-base font-bold text-inkPrimary dark:text-textDarkPrimary group-hover:text-teal-500 transition-colors">
                Green Industrial Siting &amp; DPPA Portal
              </h3>
              <p class="text-xs text-inkMuted dark:text-textDarkMuted font-light mt-1">
                National siting directory of Vietnam's Tier-1 eco-industrial parks, rooftop solar capacity, and Decree 80 feasibility.
              </p>
            </div>

            <!-- Metric Chips -->
            <div class="grid grid-cols-3 gap-2 py-2 border-y border-borderSlate/60 dark:border-darkBorder/60">
              <div class="text-center">
                <span class="block text-xs font-mono font-bold text-teal-500">168</span>
                <span class="text-[10px] text-inkMuted dark:text-textDarkMuted">Parks</span>
              </div>
              <div class="text-center">
                <span class="block text-xs font-mono font-bold text-inkPrimary dark:text-textDarkPrimary">104.4K ha</span>
                <span class="text-[10px] text-inkMuted dark:text-textDarkMuted">Footprint</span>
              </div>
              <div class="text-center">
                <span class="block text-xs font-mono font-bold text-slate-500">5,655 MWp</span>
                <span class="text-[10px] text-inkMuted dark:text-textDarkMuted">Rooftop Solar</span>
              </div>
            </div>

            <!-- Feature Tags -->
            <div class="flex flex-wrap gap-1.5 pt-0.5">
              <span class="font-mono text-[9px] px-2 py-0.5 rounded bg-slate-100 dark:bg-darkCard text-slate-600 dark:text-slate-300">Decree 80 DPPA</span>
              <span class="font-mono text-[9px] px-2 py-0.5 rounded bg-slate-100 dark:bg-darkCard text-slate-600 dark:text-slate-300">Eco-Industrial</span>
              <span class="font-mono text-[9px] px-2 py-0.5 rounded bg-slate-100 dark:bg-darkCard text-slate-600 dark:text-slate-300">ISO 14001</span>
              <span class="font-mono text-[9px] px-2 py-0.5 rounded bg-slate-100 dark:bg-darkCard text-slate-600 dark:text-slate-300">Substation Proximity</span>
            </div>
          </div>

          <div class="pt-4">
            <a href="https://industrial.renewablevietnam.com/" class="w-full flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl bg-teal-600 hover:bg-teal-500 text-white font-mono text-xs font-semibold shadow-sm transition-all">
              <span>Launch Industrial Siting</span>
              <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
            </a>
          </div>
        </div>

        <!-- Card 3: ev.renewablevietnam.com -->
        <div class="p-4 sm:p-5 rounded-2xl bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder shadow-sm flex flex-col justify-between hover:border-amber-500/60 transition-all group">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <span class="font-mono text-[10px] font-bold uppercase tracking-wider text-amber-500 dark:text-amber-400 px-2 py-0.5 rounded bg-amber-500/10 border border-amber-500/20">
                ev.renewablevietnam.com
              </span>
              <span class="inline-flex items-center gap-1 font-mono text-[10px] text-amber-500 dark:text-amber-400">
                <span class="w-1.5 h-1.5 rounded-full bg-amber-500"></span> Live Edge
              </span>
            </div>

            <div>
              <h3 class="text-sm sm:text-base font-bold text-inkPrimary dark:text-textDarkPrimary group-hover:text-amber-500 transition-colors">
                National EV Charging Cockpit
              </h3>
              <p class="text-xs text-inkMuted dark:text-textDarkMuted font-light mt-1">
                Electric mobility cartography tracking 22,055+ verified charging ports across VinFast, EV ONE, and Charge+ networks.
              </p>
            </div>

            <!-- Metric Chips -->
            <div class="grid grid-cols-3 gap-2 py-2 border-y border-borderSlate/60 dark:border-darkBorder/60">
              <div class="text-center">
                <span class="block text-xs font-mono font-bold text-amber-500">22,055+</span>
                <span class="text-[10px] text-inkMuted dark:text-textDarkMuted">Ports</span>
              </div>
              <div class="text-center">
                <span class="block text-xs font-mono font-bold text-inkPrimary dark:text-textDarkPrimary">63 Prov.</span>
                <span class="text-[10px] text-inkMuted dark:text-textDarkMuted">Coverage</span>
              </div>
              <div class="text-center">
                <span class="block text-xs font-mono font-bold text-slate-500">CCS2 / DC</span>
                <span class="text-[10px] text-inkMuted dark:text-textDarkMuted">Fast Corridors</span>
              </div>
            </div>

            <!-- Feature Tags -->
            <div class="flex flex-wrap gap-1.5 pt-0.5">
              <span class="font-mono text-[9px] px-2 py-0.5 rounded bg-slate-100 dark:bg-darkCard text-slate-600 dark:text-slate-300">VinFast V-GREEN</span>
              <span class="font-mono text-[9px] px-2 py-0.5 rounded bg-slate-100 dark:bg-darkCard text-slate-600 dark:text-slate-300">EV ONE</span>
              <span class="font-mono text-[9px] px-2 py-0.5 rounded bg-slate-100 dark:bg-darkCard text-slate-600 dark:text-slate-300">Highway Corridors</span>
              <span class="font-mono text-[9px] px-2 py-0.5 rounded bg-slate-100 dark:bg-darkCard text-slate-600 dark:text-slate-300">DC Fast Nav</span>
            </div>
          </div>

          <div class="pt-4">
            <a href="https://ev.renewablevietnam.com/" class="w-full flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl bg-amber-600 hover:bg-amber-500 text-white font-mono text-xs font-semibold shadow-sm transition-all">
              <span>Launch EV Tech Cockpit</span>
              <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
            </a>
          </div>
        </div>

        <!-- Card 4: invest.renewablevietnam.com -->
        <div class="p-4 sm:p-5 rounded-2xl bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder shadow-sm flex flex-col justify-between hover:border-blue-500/60 transition-all group">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <span class="font-mono text-[10px] font-bold uppercase tracking-wider text-blue-500 dark:text-blue-400 px-2 py-0.5 rounded bg-blue-500/10 border border-blue-500/20">
                invest.renewablevietnam.com
              </span>
              <span class="inline-flex items-center gap-1 font-mono text-[10px] text-blue-500 dark:text-blue-400">
                <span class="w-1.5 h-1.5 rounded-full bg-blue-500"></span> Live Edge
              </span>
            </div>

            <div>
              <h3 class="text-sm sm:text-base font-bold text-inkPrimary dark:text-textDarkPrimary group-hover:text-blue-500 transition-colors">
                Investment Project Legal Management &amp; M&amp;A Engine
              </h3>
              <p class="text-xs text-inkMuted dark:text-textDarkMuted font-light mt-1">
                Institutional project development, critical path method (CPM) statutory permitting, land allocation, and valuation due diligence.
              </p>
            </div>

            <!-- Metric Chips -->
            <div class="grid grid-cols-4 gap-2 py-2 border-y border-borderSlate/60 dark:border-darkBorder/60">
              <div class="text-center">
                <span class="block text-xs font-mono font-bold text-blue-500">4 Tiers</span>
                <span class="text-[10px] text-inkMuted dark:text-textDarkMuted">Audit</span>
              </div>
              <div class="text-center">
                <span class="block text-xs font-mono font-bold text-inkPrimary dark:text-textDarkPrimary">30+ Steps</span>
                <span class="text-[10px] text-inkMuted dark:text-textDarkMuted">Statutory CPM</span>
              </div>
              <div class="text-center">
                <span class="block text-xs font-mono font-bold text-slate-500">Gantt</span>
                <span class="text-[10px] text-inkMuted dark:text-textDarkMuted">Telemetry</span>
              </div>
              <div class="text-center">
                <span class="block text-xs font-mono font-bold text-emerald-500">Quy Hoach</span>
                <span class="text-[10px] text-inkMuted dark:text-textDarkMuted">Integrated</span>
              </div>
            </div>

            <!-- Feature Tags -->
            <div class="flex flex-wrap gap-1.5 pt-0.5">
              <span class="font-mono text-[9px] px-2 py-0.5 rounded bg-slate-100 dark:bg-darkCard text-slate-600 dark:text-slate-300">Legal Due Diligence</span>
              <span class="font-mono text-[9px] px-2 py-0.5 rounded bg-slate-100 dark:bg-darkCard text-slate-600 dark:text-slate-300">Investment Policy</span>
              <span class="font-mono text-[9px] px-2 py-0.5 rounded bg-slate-100 dark:bg-darkCard text-slate-600 dark:text-slate-300">Land Allocation</span>
              <span class="font-mono text-[9px] px-2 py-0.5 rounded bg-slate-100 dark:bg-darkCard text-slate-600 dark:text-slate-300">EIA Feasibility</span>
            </div>
          </div>

          <div class="pt-4">
            <a href="https://invest.renewablevietnam.com/" class="w-full flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl bg-blue-600 hover:bg-blue-500 text-white font-mono text-xs font-semibold shadow-sm transition-all">
              <span>Launch Investment M&amp;A Engine</span>
              <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
            </a>
          </div>
        </div>

      </div>
    </section>

  </main>

  <!-- INSTITUTIONAL FOOTER -->
  <footer class="w-full bg-white dark:bg-darkSurface border-t border-borderSlate dark:border-darkBorder mt-12 py-8 px-4 sm:px-6 lg:px-8 text-xs text-inkMuted dark:text-textDarkMuted font-light">
    <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-4">
      <div class="flex items-center gap-3">
        <img src="/assets/images/logo.svg" alt="Renewable Viet Nam" width="24" height="24" class="w-6 h-6 rounded" />
        <span class="font-mono text-[11px] font-semibold text-inkPrimary dark:text-textDarkPrimary">RENEWABLE VIET NAM &middot; MASTER INTELLIGENCE ECOSYSTEM</span>
      </div>

      <div class="flex flex-wrap items-center justify-center gap-4 font-mono text-[11px]">
        <a href="https://energy.renewablevietnam.com/" class="hover:text-emerald-500 transition-colors">Clean Generation</a>
        <a href="https://industrial.renewablevietnam.com/" class="hover:text-teal-500 transition-colors">Industrial Hubs</a>
        <a href="https://ev.renewablevietnam.com/" class="hover:text-amber-500 transition-colors">EV Mobility</a>
        <a href="https://invest.renewablevietnam.com/" class="hover:text-blue-500 transition-colors">Investment M&amp;A</a>
      </div>

      <div class="text-[11px] font-mono text-slate-400">
        &copy; 2026 Renewable Viet Nam. Institutional Distribution.
      </div>
    </div>
  </footer>

  <!-- SCRIPT: THEME TOGGLE & DYNAMIC CHART.JS INITIALIZATION -->
  <script>
    const themeBtn = document.getElementById('themeToggleBtn');
    const sunIcon = document.getElementById('sunIcon');
    const moonIcon = document.getElementById('moonIcon');

    let pdp8ChartInstance = null;
    let industrialChartInstance = null;
    let evChartInstance = null;

    function getChartThemeColors(isDark) {
      return {
        textColor: isDark ? '#94A3B8' : '#475569',
        gridColor: isDark ? 'rgba(255, 255, 255, 0.06)' : 'rgba(0, 0, 0, 0.06)',
        tooltipBg: isDark ? '#131B2E' : '#FFFFFF',
        tooltipText: isDark ? '#F1F5F9' : '#0F172A',
        tooltipBorder: isDark ? 'rgba(59, 130, 246, 0.25)' : '#E2E8F0',
      };
    }

    function initCharts() {
      const isDark = document.documentElement.classList.contains('dark');
      const theme = getChartThemeColors(isDark);

      // 1. PDP8 Generation Target Mix Doughnut Chart
      const ctxPdp8 = document.getElementById('pdp8MixChart')?.getContext('2d');
      if (ctxPdp8) {
        if (pdp8ChartInstance) pdp8ChartInstance.destroy();
        pdp8ChartInstance = new Chart(ctxPdp8, {
          type: 'doughnut',
          data: {
            labels: [
              'Thermal LNG (37.3 GW)',
              'Coal Phase-down (30.1 GW)',
              'Hydro Generation (29.3 GW)',
              'Onshore Wind (21.9 GW)',
              'Solar Farms (12.8 GW)',
              'Biomass & Storage (13.1 GW)',
              'Offshore Wind (6.0 GW)'
            ],
            datasets: [{
              data: [37.3, 30.1, 29.3, 21.9, 12.8, 13.1, 6.0],
              backgroundColor: [
                '#3B82F6', // Blue (LNG)
                '#64748B', // Slate (Coal)
                '#06B6D4', // Cyan (Hydro)
                '#10B981', // Emerald (Onshore Wind)
                '#F59E0B', // Amber (Solar)
                '#8B5CF6', // Purple (Biomass/Storage)
                '#14B8A6'  // Teal (Offshore Wind)
              ],
              borderWidth: 2,
              borderColor: isDark ? '#0D1322' : '#FFFFFF'
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            cutout: '68%',
            plugins: {
              legend: {
                display: false
              },
              tooltip: {
                backgroundColor: theme.tooltipBg,
                titleColor: theme.tooltipText,
                bodyColor: theme.tooltipText,
                borderColor: theme.tooltipBorder,
                borderWidth: 1,
                padding: 10,
                callbacks: {
                  label: function(context) {
                    const total = 150.5;
                    const val = context.raw || 0;
                    const pct = ((val / total) * 100).toFixed(1);
                    return ` ${context.label}: ${val} GW (${pct}%)`;
                  }
                }
              }
            }
          }
        });
      }

      // 2. Regional Eco-Industrial Solar Density Bar Chart
      const ctxInd = document.getElementById('regionalIndustrialChart')?.getContext('2d');
      if (ctxInd) {
        if (industrialChartInstance) industrialChartInstance.destroy();
        industrialChartInstance = new Chart(ctxInd, {
          type: 'bar',
          data: {
            labels: ['Southern Economic Zone', 'Northern Economic Zone', 'Central Coastal Zone'],
            datasets: [
              {
                label: 'Rooftop Solar Potential (MWp)',
                data: [3120, 1890, 645],
                backgroundColor: '#14B8A6', // Teal
                borderRadius: 6,
                barPercentage: 0.6,
                yAxisID: 'y'
              },
              {
                label: 'Industrial Parks (Count)',
                data: [92, 54, 22],
                backgroundColor: '#3B82F6', // Blue
                borderRadius: 6,
                barPercentage: 0.6,
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
                labels: {
                  color: theme.textColor,
                  font: { family: 'ui-monospace, monospace', size: 10 },
                  boxWidth: 12
                }
              },
              tooltip: {
                backgroundColor: theme.tooltipBg,
                titleColor: theme.tooltipText,
                bodyColor: theme.tooltipText,
                borderColor: theme.tooltipBorder,
                borderWidth: 1,
                padding: 10
              }
            },
            scales: {
              x: {
                grid: { display: false },
                ticks: { color: theme.textColor, font: { size: 11 } }
              },
              y: {
                type: 'linear',
                position: 'left',
                grid: { color: theme.gridColor },
                ticks: {
                  color: theme.textColor,
                  font: { family: 'ui-monospace, monospace', size: 10 },
                  callback: val => `${val} MWp`
                }
              },
              y1: {
                type: 'linear',
                position: 'right',
                grid: { display: false },
                ticks: {
                  color: theme.textColor,
                  font: { family: 'ui-monospace, monospace', size: 10 },
                  callback: val => `${val} Hubs`
                }
              }
            }
          }
        });
      }

      // 3. National EV Charging Network Ecosystem
      const ctxEv = document.getElementById('evNetworkChart')?.getContext('2d');
      if (ctxEv) {
        if (evChartInstance) evChartInstance.destroy();
        evChartInstance = new Chart(ctxEv, {
          type: 'bar',
          data: {
            labels: ['VinFast (V-GREEN)', 'EV ONE Network', 'Charge+ & Autel', 'Other Independent CPOs'],
            datasets: [
              {
                label: 'DC Fast Charging (\u2265 60kW)',
                data: [12000, 950, 480, 244],
                backgroundColor: '#F59E0B', // Amber
                borderRadius: 6,
                stack: 'Stack 0'
              },
              {
                label: 'AC Level 2 (\u2264 22kW)',
                data: [6500, 850, 650, 381],
                backgroundColor: '#94A3B8', // Slate
                borderRadius: 6,
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
                labels: {
                  color: theme.textColor,
                  font: { family: 'ui-monospace, monospace', size: 10 },
                  boxWidth: 12
                }
              },
              tooltip: {
                backgroundColor: theme.tooltipBg,
                titleColor: theme.tooltipText,
                bodyColor: theme.tooltipText,
                borderColor: theme.tooltipBorder,
                borderWidth: 1,
                padding: 10
              }
            },
            scales: {
              x: {
                stacked: true,
                grid: { color: theme.gridColor },
                ticks: {
                  color: theme.textColor,
                  font: { family: 'ui-monospace, monospace', size: 10 },
                  callback: val => `${val.toLocaleString()} ports`
                }
              },
              y: {
                stacked: true,
                grid: { display: false },
                ticks: { color: theme.textColor, font: { size: 11 } }
              }
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

    // Re-render charts on window resize
    window.addEventListener('resize', () => {
      initCharts();
    });
  </script>
</body>
</html>
"""

base_dir = r"G:\My Drive\7. AI\RenewableVietNam"
index_file = os.path.join(base_dir, "index.html")
rev11_file = os.path.join(base_dir, "index_Rev.011.html")

# Non-destructive sequential revision
with open(rev11_file, "w", encoding="utf-8") as f:
    f.write(DASHBOARD_HTML)
print(f"Created sequential revision: {rev11_file}")

with open(index_file, "w", encoding="utf-8") as f:
    f.write(DASHBOARD_HTML)
print(f"Updated active homepage: {index_file}")
