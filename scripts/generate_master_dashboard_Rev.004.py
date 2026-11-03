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
  <meta name="description" content="Master institutional visual intelligence cockpit uniting Vietnam's clean energy ecosystem: interactive PDP8 generation mix, 168 green industrial hubs, 22,055+ EV charging ports, and CPM legal M&A engine." />
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

    /* Node graph hover states */
    .flow-node {
      cursor: pointer;
      transition: all 0.25s ease;
    }
    .flow-node:hover {
      transform: translateY(-2px);
      filter: drop-shadow(0 4px 12px rgba(20, 184, 166, 0.25));
    }
    .flow-node.active-node {
      border-color: #14B8A6 !important;
      box-shadow: 0 0 0 2px rgba(20, 184, 166, 0.3);
    }
  </style>
</head>
<body class="bg-slate-50/70 dark:bg-obsidian text-inkPrimary dark:text-textDarkPrimary min-h-screen flex flex-col antialiased selection:bg-teal-500 selection:text-white transition-colors duration-200">

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
              Master Intelligence Cockpit
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
          <span>Edge Sync &middot; 4 Subdomains</span>
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

    <!-- HERO HEADER WITH TELEMETRY RIBBON -->
    <section class="flex flex-col md:flex-row md:items-center justify-between gap-4 bg-white/70 dark:bg-darkSurface/70 backdrop-blur-sm border border-slate-200/80 dark:border-darkBorder rounded-2xl p-5 shadow-xs">
      <div class="space-y-1">
        <div class="flex items-center gap-2">
          <span class="font-mono text-[10px] uppercase font-bold text-teal-600 dark:text-teal-400 bg-teal-500/10 px-2 py-0.5 rounded border border-teal-500/20">
            Interactive Intelligence Cockpit
          </span>
          <span class="font-mono text-[10px] text-slate-400">PDP8 &middot; Decree 80 DPPA &middot; Law on Electricity 2024</span>
        </div>
        <h1 class="text-xl sm:text-2xl font-semibold tracking-tight text-inkPrimary dark:text-textDarkPrimary">
          Vietnam Clean Energy &amp; Ecological Transition Master Cockpit
        </h1>
        <p class="text-xs text-inkMuted dark:text-textDarkMuted max-w-3xl">
          Real-time interactive telemetry tracking statutory generation assets, 500kV/220kV transmission, eco-industrial wheeling, and EV fast-charging corridors.
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
          <span class="block text-slate-400 text-[10px]">Industrial Parks</span>
          <strong class="text-sm font-bold text-teal-600 dark:text-teal-400">168 Hubs</strong>
        </div>
      </div>
    </section>

    <!-- SECTION 1: INTERACTIVE ENERGY NETWORK TOPOLOGY GRAPH (FLOW ENGINE) -->
    <section class="bg-white/80 dark:bg-darkSurface/80 backdrop-blur-sm border border-slate-200/80 dark:border-darkBorder rounded-2xl p-5 shadow-xs space-y-4">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-100 dark:border-darkBorder pb-3">
        <div>
          <div class="flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-teal-500"></span>
            <h2 class="text-xs sm:text-sm font-bold uppercase tracking-wider text-slate-800 dark:text-slate-200">
              Interactive Energy Flow Topology Network
            </h2>
          </div>
          <p class="text-[11px] text-slate-500 dark:text-slate-400 mt-0.5">
            Click on any segment node to inspect operational parameters, legal basis, and direct edge telemetry.
          </p>
        </div>
        <span class="font-mono text-[10px] text-slate-400 bg-slate-100 dark:bg-darkCard px-2 py-0.5 rounded border border-slate-200/60 dark:border-darkBorder">
          Interactive Node Selection Active
        </span>
      </div>

      <!-- 5 Interactive Flow Nodes -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-3" id="flowNodesContainer">
        <!-- Node 1: PDP8 Generation -->
        <div class="flow-node active-node p-3.5 rounded-xl bg-slate-50/90 dark:bg-darkCard/90 border border-slate-200/80 dark:border-darkBorder" data-node="0">
          <div class="flex items-center justify-between font-mono text-[10px] mb-1">
            <span class="text-emerald-600 dark:text-emerald-400 font-bold">NODE 01</span>
            <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
          </div>
          <strong class="block text-xs font-semibold text-slate-900 dark:text-white">PDP8 Generation</strong>
          <span class="block text-[10px] text-slate-500 dark:text-slate-400 mt-0.5">Wind, Solar &amp; Hydro Quotas</span>
          <div class="mt-2 pt-1.5 border-t border-slate-200/50 dark:border-darkBorder/50 font-mono text-[10px] text-emerald-600 dark:text-emerald-400 font-bold">
            107.5 GW Pipeline
          </div>
        </div>

        <!-- Node 2: Permitting CPM -->
        <div class="flow-node p-3.5 rounded-xl bg-slate-50/90 dark:bg-darkCard/90 border border-slate-200/80 dark:border-darkBorder" data-node="1">
          <div class="flex items-center justify-between font-mono text-[10px] mb-1">
            <span class="text-blue-500 dark:text-blue-400 font-bold">NODE 02</span>
            <span class="w-1.5 h-1.5 rounded-full bg-blue-500"></span>
          </div>
          <strong class="block text-xs font-semibold text-slate-900 dark:text-white">Permitting CPM</strong>
          <span class="block text-[10px] text-slate-500 dark:text-slate-400 mt-0.5">Statutory &amp; Land Leases</span>
          <div class="mt-2 pt-1.5 border-t border-slate-200/50 dark:border-darkBorder/50 font-mono text-[10px] text-blue-500 dark:text-blue-400 font-bold">
            30+ Critical Milestones
          </div>
        </div>

        <!-- Node 3: Transmission Intertie -->
        <div class="flow-node p-3.5 rounded-xl bg-slate-50/90 dark:bg-darkCard/90 border border-slate-200/80 dark:border-darkBorder" data-node="2">
          <div class="flex items-center justify-between font-mono text-[10px] mb-1">
            <span class="text-emerald-600 dark:text-emerald-400 font-bold">NODE 03</span>
            <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
          </div>
          <strong class="block text-xs font-semibold text-slate-900 dark:text-white">Grid Intertie</strong>
          <span class="block text-[10px] text-slate-500 dark:text-slate-400 mt-0.5">500kV/220kV Substation</span>
          <div class="mt-2 pt-1.5 border-t border-slate-200/50 dark:border-darkBorder/50 font-mono text-[10px] text-emerald-600 dark:text-emerald-400 font-bold">
            High-Voltage Loops
          </div>
        </div>

        <!-- Node 4: Industrial Offtake -->
        <div class="flow-node p-3.5 rounded-xl bg-slate-50/90 dark:bg-darkCard/90 border border-slate-200/80 dark:border-darkBorder" data-node="3">
          <div class="flex items-center justify-between font-mono text-[10px] mb-1">
            <span class="text-teal-600 dark:text-teal-400 font-bold">NODE 04</span>
            <span class="w-1.5 h-1.5 rounded-full bg-teal-500"></span>
          </div>
          <strong class="block text-xs font-semibold text-slate-900 dark:text-white">DPPA Industrial Offtake</strong>
          <span class="block text-[10px] text-slate-500 dark:text-slate-400 mt-0.5">Decree 80 Direct Wheeling</span>
          <div class="mt-2 pt-1.5 border-t border-slate-200/50 dark:border-darkBorder/50 font-mono text-[10px] text-teal-600 dark:text-teal-400 font-bold">
            5,655 MWp Rooftop
          </div>
        </div>

        <!-- Node 5: EV Corridors -->
        <div class="flow-node p-3.5 rounded-xl bg-slate-50/90 dark:bg-darkCard/90 border border-slate-200/80 dark:border-darkBorder" data-node="4">
          <div class="flex items-center justify-between font-mono text-[10px] mb-1">
            <span class="text-amber-500 dark:text-amber-400 font-bold">NODE 05</span>
            <span class="w-1.5 h-1.5 rounded-full bg-amber-500"></span>
          </div>
          <strong class="block text-xs font-semibold text-slate-900 dark:text-white">EV Freight Corridors</strong>
          <span class="block text-[10px] text-slate-500 dark:text-slate-400 mt-0.5">Expressway DC Fast Network</span>
          <div class="mt-2 pt-1.5 border-t border-slate-200/50 dark:border-darkBorder/50 font-mono text-[10px] text-amber-500 dark:text-amber-400 font-bold">
            22,055+ CCS2 Ports
          </div>
        </div>
      </div>

      <!-- Real-Time Node Inspector Drawer -->
      <div id="nodeInspectorPanel" class="p-4 rounded-xl bg-slate-50 dark:bg-darkCard border border-slate-200/80 dark:border-darkBorder transition-all flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div class="space-y-1">
          <div class="flex items-center gap-2">
            <span id="inspectorBadge" class="font-mono text-[9px] uppercase font-bold text-emerald-600 dark:text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded border border-emerald-500/20">
              STAGE 01 &middot; STATUTORY ZONING
            </span>
            <span id="inspectorStatute" class="font-mono text-[10px] text-slate-400">
              Statutory Basis: PDP8 Decision 500/QD-TTg
            </span>
          </div>
          <h3 id="inspectorTitle" class="text-sm font-bold text-slate-900 dark:text-white">
            PDP8 Clean Energy &amp; Power Generation Statutory Quotas
          </h3>
          <p id="inspectorDesc" class="text-xs text-slate-500 dark:text-slate-400 max-w-3xl">
            Provincial resource allocation allocating 107.5 GW total clean capacity across onshore/offshore wind, utility-scale solar farms, biomass, and pumped-storage hydro installations.
          </p>
        </div>

        <div class="flex items-center gap-3 shrink-0">
          <div class="text-right font-mono text-[11px] pr-2">
            <span class="block text-slate-400 text-[10px]">Key Metric</span>
            <strong id="inspectorMetric" class="text-emerald-600 dark:text-emerald-400 text-xs font-bold">107.5 GW Target</strong>
          </div>
          <a id="inspectorLaunchBtn" href="https://energy.renewablevietnam.com/" class="px-3.5 py-2 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-mono text-xs font-semibold shadow-xs transition-all flex items-center gap-1.5">
            <span>Explore Subdomain</span>
            <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 19.5l15-15m0 0H8.25m11.25 0v11.25"/></svg>
          </a>
        </div>
      </div>
    </section>

    <!-- SECTION 2: MULTI-GRAPH INTERACTIVE VISUALIZATION SUITE -->
    <section class="space-y-4">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-100 dark:border-darkBorder pb-2">
        <div>
          <h2 class="text-xs sm:text-sm font-bold uppercase tracking-wider text-slate-800 dark:text-slate-200 flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
            Interactive Graph Suite &amp; Transition Telemetry
          </h2>
          <p class="text-[11px] text-slate-500 dark:text-slate-400 mt-0.5">
            Interactive multi-horizon projections, statutory technology slices, and regional 5-axis competitiveness.
          </p>
        </div>
        <span class="font-mono text-[10px] text-slate-400">Horizon: 2026&ndash;2050 Net Zero</span>
      </div>

      <!-- 4 Compact Telemetry Gauges -->
      <div class="grid grid-cols-2 lg:grid-cols-4 gap-3">
        <div class="bg-white/80 dark:bg-darkSurface/80 backdrop-blur-sm border border-slate-200/80 dark:border-darkBorder rounded-xl p-3.5 shadow-xs">
          <div class="flex justify-between items-baseline font-mono text-[10px]">
            <span class="text-slate-400">PDP8 RE Target</span>
            <strong class="text-emerald-600 dark:text-emerald-400 font-bold text-xs">31.5%</strong>
          </div>
          <div class="w-full bg-slate-100 dark:bg-darkCard h-1.5 rounded-full mt-2 overflow-hidden">
            <div class="bg-emerald-500 h-full rounded-full" style="width: 31.5%"></div>
          </div>
          <span class="block text-[9px] font-mono text-slate-400 mt-1.5">14.8 GW Active / 47.0 GW Target</span>
        </div>

        <div class="bg-white/80 dark:bg-darkSurface/80 backdrop-blur-sm border border-slate-200/80 dark:border-darkBorder rounded-xl p-3.5 shadow-xs">
          <div class="flex justify-between items-baseline font-mono text-[10px]">
            <span class="text-slate-400">Decree 80 DPPA</span>
            <strong class="text-teal-600 dark:text-teal-400 font-bold text-xs">100%</strong>
          </div>
          <div class="w-full bg-slate-100 dark:bg-darkCard h-1.5 rounded-full mt-2 overflow-hidden">
            <div class="bg-teal-500 h-full rounded-full" style="width: 100%"></div>
          </div>
          <span class="block text-[9px] font-mono text-slate-400 mt-1.5">Statutory Clearance Operational</span>
        </div>

        <div class="bg-white/80 dark:bg-darkSurface/80 backdrop-blur-sm border border-slate-200/80 dark:border-darkBorder rounded-xl p-3.5 shadow-xs">
          <div class="flex justify-between items-baseline font-mono text-[10px]">
            <span class="text-slate-400">Expressway Fast EV</span>
            <strong class="text-amber-500 dark:text-amber-400 font-bold text-xs">95.2%</strong>
          </div>
          <div class="w-full bg-slate-100 dark:bg-darkCard h-1.5 rounded-full mt-2 overflow-hidden">
            <div class="bg-amber-500 h-full rounded-full" style="width: 95.2%"></div>
          </div>
          <span class="block text-[9px] font-mono text-slate-400 mt-1.5">National Route 1A &amp; CT.01 Corridors</span>
        </div>

        <div class="bg-white/80 dark:bg-darkSurface/80 backdrop-blur-sm border border-slate-200/80 dark:border-darkBorder rounded-xl p-3.5 shadow-xs">
          <div class="flex justify-between items-baseline font-mono text-[10px]">
            <span class="text-slate-400">Eco-Park ESG Conversion</span>
            <strong class="text-blue-500 dark:text-blue-400 font-bold text-xs">42.0%</strong>
          </div>
          <div class="w-full bg-slate-100 dark:bg-darkCard h-1.5 rounded-full mt-2 overflow-hidden">
            <div class="bg-blue-500 h-full rounded-full" style="width: 42.0%"></div>
          </div>
          <span class="block text-[9px] font-mono text-slate-400 mt-1.5">71 of 168 Hubs Certified</span>
        </div>
      </div>

      <!-- INTERACTIVE GRAPH ROW 1: TRAJECTORY AREA GRAPH & PDP8 MIX DOUGHNUT -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-4">
        
        <!-- Graph 2: 2025-2050 Net Zero Transition Trajectory (7 cols) -->
        <div class="lg:col-span-7 bg-white/80 dark:bg-darkSurface/80 backdrop-blur-sm border border-slate-200/80 dark:border-darkBorder rounded-2xl p-5 shadow-xs flex flex-col justify-between">
          <div>
            <div class="flex flex-col sm:flex-row sm:items-center justify-between pb-3 mb-3 border-b border-slate-100 dark:border-darkBorder gap-2">
              <div>
                <span class="text-xs font-bold text-slate-800 dark:text-slate-200">Vietnam Clean Energy Trajectory (2020&ndash;2050)</span>
                <span class="text-[10px] text-slate-400 block">Long-term transition path from baseline to 500 GW Net Zero</span>
              </div>
              <!-- Interactive metric toggles -->
              <div class="flex items-center gap-1 font-mono text-[10px] bg-slate-100 dark:bg-darkCard p-1 rounded-lg border border-slate-200/60 dark:border-darkBorder self-start sm:self-auto">
                <button id="btnTrajectoryCapacity" class="px-2 py-0.5 rounded bg-white dark:bg-darkSurface text-teal-600 dark:text-teal-400 font-bold shadow-xs">GW</button>
                <button id="btnTrajectoryShare" class="px-2 py-0.5 rounded text-slate-500 dark:text-slate-400 hover:text-teal-600">RE %</button>
                <button id="btnTrajectoryCarbon" class="px-2 py-0.5 rounded text-slate-500 dark:text-slate-400 hover:text-teal-600">CO2 Mt</button>
              </div>
            </div>
            <div class="relative h-60">
              <canvas id="trajectoryChart"></canvas>
            </div>
          </div>
          <div class="flex items-center justify-between font-mono text-[10px] text-slate-400 pt-3 border-t border-slate-100 dark:border-darkBorder">
            <span>2020: 69.3 GW</span>
            <span>2030 (PDP8): 150.5 GW</span>
            <span>2050 (Net Zero): 500.0 GW</span>
          </div>
        </div>

        <!-- Graph 3: PDP8 Statutory Capacity Breakdown (5 cols) -->
        <div class="lg:col-span-5 bg-white/80 dark:bg-darkSurface/80 backdrop-blur-sm border border-slate-200/80 dark:border-darkBorder rounded-2xl p-5 shadow-xs flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-3 mb-3 border-b border-slate-100 dark:border-darkBorder">
              <div>
                <span class="text-xs font-bold text-slate-800 dark:text-slate-200">PDP8 Technology Mix (2030)</span>
                <span class="text-[10px] text-slate-400 block">Statutory allocation across generation archetypes</span>
              </div>
              <span class="font-mono text-[10px] text-emerald-600 dark:text-emerald-400 font-bold bg-emerald-500/10 px-2 py-0.5 rounded border border-emerald-500/20">
                150.5 GW
              </span>
            </div>
            <div class="relative h-60 flex items-center justify-center">
              <canvas id="pdp8MixChart"></canvas>
            </div>
          </div>
          <div class="grid grid-cols-3 gap-1.5 text-center font-mono text-[9px] pt-3 border-t border-slate-100 dark:border-darkBorder">
            <div class="p-1 rounded bg-slate-50 dark:bg-darkCard">
              <span class="text-slate-400 block">Thermal LNG</span>
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

      </div>

      <!-- INTERACTIVE GRAPH ROW 2: 5-AXIS RADAR GRAPH & EV CHARGING VELOCITY -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-4">

        <!-- Graph 4: 5-Axis Regional Clean Energy Competitiveness Radar (6 cols) -->
        <div class="lg:col-span-6 bg-white/80 dark:bg-darkSurface/80 backdrop-blur-sm border border-slate-200/80 dark:border-darkBorder rounded-2xl p-5 shadow-xs flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-3 mb-2 border-b border-slate-100 dark:border-darkBorder">
              <div>
                <span class="text-xs font-bold text-slate-800 dark:text-slate-200">5-Axis Regional Competitiveness</span>
                <span class="text-[10px] text-slate-400 block">South vs North vs Central across 5 infrastructure vectors</span>
              </div>
              <span class="font-mono text-[10px] text-teal-600 dark:text-teal-400 font-bold bg-teal-500/10 px-2 py-0.5 rounded border border-teal-500/20">
                168 Hubs
              </span>
            </div>
            <div class="relative h-64 flex items-center justify-center">
              <canvas id="regionalRadarChart"></canvas>
            </div>
          </div>
          <div class="flex items-center justify-between text-[10px] font-mono text-slate-400 pt-3 border-t border-slate-100 dark:border-darkBorder">
            <span class="text-teal-500 font-semibold">South: High Solar &amp; Demand</span>
            <span class="text-blue-500 font-semibold">North: High Grid Stability</span>
            <span class="text-amber-500 font-semibold">Central: High Wind</span>
          </div>
        </div>

        <!-- Graph 5: National EV Charging Infrastructure Footprint (6 cols) -->
        <div class="lg:col-span-6 bg-white/80 dark:bg-darkSurface/80 backdrop-blur-sm border border-slate-200/80 dark:border-darkBorder rounded-2xl p-5 shadow-xs flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-3 mb-2 border-b border-slate-100 dark:border-darkBorder">
              <div>
                <span class="text-xs font-bold text-slate-800 dark:text-slate-200">EV Charging Network Velocity</span>
                <span class="text-[10px] text-slate-400 block">22,055+ verified ports across operators &amp; charging tiers</span>
              </div>
              <span class="font-mono text-[10px] text-amber-500 font-bold bg-amber-500/10 px-2 py-0.5 rounded border border-amber-500/20">
                62% DC Fast
              </span>
            </div>
            <div class="relative h-64">
              <canvas id="evNetworkChart"></canvas>
            </div>
          </div>
          <div class="grid grid-cols-4 gap-1 text-center font-mono text-[9px] pt-3 border-t border-slate-100 dark:border-darkBorder">
            <div class="p-1 rounded bg-slate-50 dark:bg-darkCard">
              <span class="text-slate-400 block">VinFast</span>
              <strong class="text-amber-500">18,500</strong>
            </div>
            <div class="p-1 rounded bg-slate-50 dark:bg-darkCard">
              <span class="text-slate-400 block">EV ONE</span>
              <strong class="text-slate-700 dark:text-slate-200">1,800</strong>
            </div>
            <div class="p-1 rounded bg-slate-50 dark:bg-darkCard">
              <span class="text-slate-400 block">Charge+</span>
              <strong class="text-slate-700 dark:text-slate-200">1,755</strong>
            </div>
            <div class="p-1 rounded bg-slate-50 dark:bg-darkCard">
              <span class="text-slate-400 block">DC Fast &ge;60kW</span>
              <strong class="text-emerald-500">13,674</strong>
            </div>
          </div>
        </div>

      </div>

      <!-- SECTION 3: INTERACTIVE DECREE 80 DPPA ECONOMIC SIMULATOR -->
      <div class="bg-white/80 dark:bg-darkSurface/80 backdrop-blur-sm border border-slate-200/80 dark:border-darkBorder rounded-2xl p-5 shadow-xs space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between pb-3 border-b border-slate-100 dark:border-darkBorder gap-2">
          <div>
            <div class="flex items-center gap-2">
              <span class="w-2 h-2 rounded-full bg-blue-500"></span>
              <h3 class="text-xs sm:text-sm font-bold uppercase tracking-wider text-slate-800 dark:text-slate-200">
                Decree 80/2024 DPPA Bilateral Offtake Simulator
              </h3>
            </div>
            <p class="text-[11px] text-slate-500 dark:text-slate-400 mt-0.5">
              Simulate clean electricity offtake, annual output, carbon abatement, and projected 10-year tariff parity savings.
            </p>
          </div>
          <span class="font-mono text-[10px] text-teal-600 dark:text-teal-400 bg-teal-500/10 px-2 py-0.5 rounded border border-teal-500/20 self-start sm:self-auto">
            Reactive Calculation Engine
          </span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-12 gap-5 items-center">
          <!-- Controls (6 cols) -->
          <div class="md:col-span-6 space-y-4">
            <div>
              <div class="flex justify-between items-baseline text-xs font-mono mb-1.5">
                <span class="text-slate-600 dark:text-slate-300 font-medium">Offtake Capacity Requirement:</span>
                <strong id="sliderCapacityVal" class="text-emerald-600 dark:text-emerald-400 font-bold text-sm">15 MW</strong>
              </div>
              <input type="range" id="sliderCapacity" min="1" max="50" value="15" step="1" class="w-full h-1.5 bg-slate-200 dark:bg-darkCard rounded-lg appearance-none cursor-pointer accent-emerald-500" />
              <div class="flex justify-between text-[10px] font-mono text-slate-400 mt-1">
                <span>1 MW</span>
                <span>25 MW</span>
                <span>50 MW</span>
              </div>
            </div>

            <div>
              <div class="flex justify-between items-baseline text-xs font-mono mb-1.5">
                <span class="text-slate-600 dark:text-slate-300 font-medium">Plant Capacity Factor:</span>
                <strong id="sliderFactorVal" class="text-teal-600 dark:text-teal-400 font-bold text-sm">22% (Solar Rooftop)</strong>
              </div>
              <input type="range" id="sliderFactor" min="15" max="45" value="22" step="1" class="w-full h-1.5 bg-slate-200 dark:bg-darkCard rounded-lg appearance-none cursor-pointer accent-teal-500" />
              <div class="flex justify-between text-[10px] font-mono text-slate-400 mt-1">
                <span>15% (Rooftop Low)</span>
                <span>22% (Solar Avg)</span>
                <span>45% (Wind High)</span>
              </div>
            </div>
          </div>

          <!-- Dynamic Output Telemetry Cards (6 cols) -->
          <div class="md:col-span-6 grid grid-cols-2 gap-3 font-mono">
            <div class="p-3.5 rounded-xl bg-slate-50 dark:bg-darkCard border border-slate-200/60 dark:border-darkBorder">
              <span class="text-[10px] text-slate-400 block">Annual Clean Output</span>
              <strong id="simEnergyOut" class="text-base sm:text-lg font-bold text-emerald-600 dark:text-emerald-400">28,908 MWh</strong>
              <span class="text-[10px] text-slate-400 block mt-0.5">Dispatched to Hub</span>
            </div>

            <div class="p-3.5 rounded-xl bg-slate-50 dark:bg-darkCard border border-slate-200/60 dark:border-darkBorder">
              <span class="text-[10px] text-slate-400 block">Carbon Abatement</span>
              <strong id="simCo2Out" class="text-base sm:text-lg font-bold text-teal-600 dark:text-teal-400">20,874 tCO2e</strong>
              <span class="text-[10px] text-slate-400 block mt-0.5">Scope 2 Reduction</span>
            </div>

            <div class="p-3.5 rounded-xl bg-slate-50 dark:bg-darkCard border border-slate-200/60 dark:border-darkBorder">
              <span class="text-[10px] text-slate-400 block">10-Yr Grid Parity Savings</span>
              <strong id="simSavingsOut" class="text-base sm:text-lg font-bold text-blue-500">$5.78 M</strong>
              <span class="text-[10px] text-slate-400 block mt-0.5">Vs. Standard Retail Tariff</span>
            </div>

            <div class="p-3.5 rounded-xl bg-slate-50 dark:bg-darkCard border border-slate-200/60 dark:border-darkBorder flex flex-col justify-between">
              <div>
                <span class="text-[10px] text-slate-400 block">DPPA Mechanism</span>
                <strong class="text-xs font-bold text-slate-800 dark:text-slate-200">Decree 80 Direct Line</strong>
              </div>
              <a href="https://invest.renewablevietnam.com/" class="text-[10px] font-semibold text-blue-500 hover:underline inline-flex items-center gap-1 mt-1">
                <span>Start Legal Audit &rarr;</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 4: BENTO SUBDOMAIN COMMAND CONSOLE -->
    <section class="space-y-3">
      <div class="flex items-center justify-between border-b border-slate-100 dark:border-darkBorder pb-2">
        <h2 class="text-xs sm:text-sm font-bold uppercase tracking-wider text-slate-800 dark:text-slate-200 flex items-center gap-2">
          <span class="w-2 h-2 rounded-full bg-blue-500"></span>
          Subdomain Command Console
        </h2>
        <span class="font-mono text-[10px] text-slate-400">4 Operational Gateways</span>
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

  <!-- SCRIPT: INTERACTIVE FLOW NODES, DYNAMIC CHARTS, & DECREE 80 SIMULATOR -->
  <script>
    const themeBtn = document.getElementById('themeToggleBtn');
    const sunIcon = document.getElementById('sunIcon');
    const moonIcon = document.getElementById('moonIcon');

    // Chart instances
    let trajectoryChartInstance = null;
    let pdp8ChartInstance = null;
    let regionalRadarChartInstance = null;
    let evChartInstance = null;

    // Node Inspector Data
    const nodeDetails = [
      {
        badge: "NODE 01 &middot; STATUTORY ZONING",
        statute: "Statutory Basis: PDP8 Decision 500/QD-TTg",
        title: "PDP8 Clean Energy & Power Generation Statutory Quotas",
        desc: "Provincial resource allocation allocating 107.5 GW total clean capacity across onshore/offshore wind, utility-scale solar farms, biomass, and pumped-storage hydro installations.",
        metric: "107.5 GW Pipeline",
        url: "https://energy.renewablevietnam.com/",
        color: "text-emerald-600 dark:text-emerald-400"
      },
      {
        badge: "NODE 02 &middot; STATUTORY PERMITTING",
        statute: "Statutory Basis: Investment Law 2020 & Land Law 2024",
        title: "4-Tier Permitting Critical Path Method (CPM) Due Diligence",
        desc: "30+ statutory CPM milestones: in-principle investment approval, land lease allocation, Environmental Impact Assessment (EIA), and fire protection (PCCC) validation.",
        metric: "30+ CPM Milestones",
        url: "https://invest.renewablevietnam.com/",
        color: "text-blue-500 dark:text-blue-400"
      },
      {
        badge: "NODE 03 &middot; TRANSMISSION INTERTIE",
        statute: "Statutory Basis: Law on Electricity 2024 & EVN Dispatch Code",
        title: "High-Voltage 500kV/220kV Grid Interconnection & Loop",
        desc: "Substation proximity buffers, intertie agreements, N-1 contingency modeling, and curtailment dispatch simulations along the North-South 500kV backbone.",
        metric: "500kV / 220kV Backbone",
        url: "https://energy.renewablevietnam.com/",
        color: "text-emerald-600 dark:text-emerald-400"
      },
      {
        badge: "NODE 04 &middot; INDUSTRIAL OFFTAKE",
        statute: "Statutory Basis: Decree 80/2024/ND-CP DPPA Wheeling",
        title: "Direct Power Purchase Agreements (DPPA) & RE100 Siting",
        desc: "Decree 80 bilateral wheeling mechanisms connecting clean generators to multinational manufacturing off-takers across 168 cataloged Tier-1 eco-industrial parks.",
        metric: "5,655 MWp Rooftop",
        url: "https://industrial.renewablevietnam.com/",
        color: "text-teal-600 dark:text-teal-400"
      },
      {
        badge: "NODE 05 &middot; E-MOBILITY CORRIDORS",
        statute: "Statutory Basis: National Green Transport Action Plan",
        title: "National EV Charging Infrastructure & Highway Fast Network",
        desc: "22,055+ verified charging ports across 63 provinces, featuring CCS2 DC fast-charging hubs along National Route 1A and North-South Expressway CT.01.",
        metric: "22,055+ CCS2 Ports",
        url: "https://ev.renewablevietnam.com/",
        color: "text-amber-500 dark:text-amber-400"
      }
    ];

    // Wire up Node Click Events
    document.querySelectorAll('.flow-node').forEach(nodeEl => {
      nodeEl.addEventListener('click', () => {
        document.querySelectorAll('.flow-node').forEach(n => n.classList.remove('active-node'));
        nodeEl.classList.add('active-node');

        const idx = parseInt(nodeEl.getAttribute('data-node'), 10);
        const data = nodeDetails[idx];
        if (!data) return;

        document.getElementById('inspectorBadge').innerHTML = data.badge;
        document.getElementById('inspectorStatute').textContent = data.statute;
        document.getElementById('inspectorTitle').textContent = data.title;
        document.getElementById('inspectorDesc').textContent = data.desc;
        document.getElementById('inspectorMetric').textContent = data.metric;
        document.getElementById('inspectorMetric').className = `${data.color} text-xs font-bold`;
        document.getElementById('inspectorLaunchBtn').href = data.url;
      });
    });

    // Theme Color Helper
    function getChartThemeColors(isDark) {
      return {
        textColor: isDark ? '#94A3B8' : '#64748B',
        gridColor: isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)',
        tooltipBg: isDark ? '#141D32' : '#FFFFFF',
        tooltipText: isDark ? '#F8FAFC' : '#0F172A',
        tooltipBorder: isDark ? 'rgba(255, 255, 255, 0.1)' : '#E2E8F0',
      };
    }

    // Trajectory Chart Current Mode: 'capacity', 'share', 'carbon'
    let currentTrajectoryMode = 'capacity';

    const trajectoryData = {
      years: ['2020', '2023', '2026', '2030 (PDP8)', '2035', '2040', '2050 (Net Zero)'],
      capacity: {
        total: [69.3, 80.5, 87.2, 150.5, 210.0, 320.0, 500.0],
        clean: [26.0, 38.0, 44.5, 75.0, 135.0, 240.0, 420.0],
        fossil: [43.3, 42.5, 42.7, 75.5, 75.0, 80.0, 80.0],
        unit: 'GW'
      },
      share: {
        total: [37.5, 47.2, 51.0, 49.8, 64.3, 75.0, 84.0],
        clean: [37.5, 47.2, 51.0, 49.8, 64.3, 75.0, 84.0],
        fossil: [62.5, 52.8, 49.0, 50.2, 35.7, 25.0, 16.0],
        unit: '%'
      },
      carbon: {
        total: [255, 275, 280, 245, 190, 110, 25],
        clean: [45, 72, 95, 165, 260, 390, 540],
        unit: 'Mt CO2'
      }
    };

    function initCharts() {
      const isDark = document.documentElement.classList.contains('dark');
      const theme = getChartThemeColors(isDark);

      // 1. Trajectory Area Chart
      const ctxTraj = document.getElementById('trajectoryChart')?.getContext('2d');
      if (ctxTraj) {
        if (trajectoryChartInstance) trajectoryChartInstance.destroy();
        
        const activeData = trajectoryData[currentTrajectoryMode];
        const datasets = currentTrajectoryMode === 'capacity' ? [
          {
            label: 'Clean & Renewable Capacity (GW)',
            data: activeData.clean,
            borderColor: '#10B981',
            backgroundColor: isDark ? 'rgba(16, 185, 129, 0.15)' : 'rgba(16, 185, 129, 0.1)',
            fill: true,
            tension: 0.35,
            pointRadius: 3
          },
          {
            label: 'Total Power Generation Capacity (GW)',
            data: activeData.total,
            borderColor: '#3B82F6',
            backgroundColor: isDark ? 'rgba(59, 130, 246, 0.1)' : 'rgba(59, 130, 246, 0.05)',
            fill: true,
            tension: 0.35,
            pointRadius: 3
          }
        ] : currentTrajectoryMode === 'share' ? [
          {
            label: 'Renewable & Clean Share (%)',
            data: activeData.clean,
            borderColor: '#14B8A6',
            backgroundColor: isDark ? 'rgba(20, 184, 166, 0.2)' : 'rgba(20, 184, 166, 0.1)',
            fill: true,
            tension: 0.35,
            pointRadius: 4
          }
        ] : [
          {
            label: 'Power Sector CO2 Abatement (Mt CO2e)',
            data: activeData.clean,
            borderColor: '#10B981',
            backgroundColor: isDark ? 'rgba(16, 185, 129, 0.2)' : 'rgba(16, 185, 129, 0.1)',
            fill: true,
            tension: 0.35,
            pointRadius: 4
          },
          {
            label: 'Residual Grid Carbon Emissions (Mt CO2e)',
            data: activeData.total,
            borderColor: '#EF4444',
            backgroundColor: 'transparent',
            borderDash: [4, 4],
            tension: 0.35,
            pointRadius: 3
          }
        ];

        trajectoryChartInstance = new Chart(ctxTraj, {
          type: 'line',
          data: {
            labels: trajectoryData.years,
            datasets: datasets
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            interaction: { mode: 'index', intersect: false },
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
              x: { grid: { color: theme.gridColor }, ticks: { color: theme.textColor, font: { size: 10 } } },
              y: {
                grid: { color: theme.gridColor },
                ticks: {
                  color: theme.textColor,
                  font: { size: 10, family: 'monospace' },
                  callback: val => `${val} ${activeData.unit}`
                }
              }
            }
          }
        });
      }

      // 2. PDP8 Mix Doughnut
      const ctxPdp8 = document.getElementById('pdp8MixChart')?.getContext('2d');
      if (ctxPdp8) {
        if (pdp8ChartInstance) pdp8ChartInstance.destroy();
        pdp8ChartInstance = new Chart(ctxPdp8, {
          type: 'doughnut',
          data: {
            labels: ['Thermal LNG', 'Coal Phase-down', 'Hydro', 'Onshore Wind', 'Solar', 'Biomass & Storage', 'Offshore Wind'],
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

      // 3. Regional 5-Axis Radar Chart
      const ctxRadar = document.getElementById('regionalRadarChart')?.getContext('2d');
      if (ctxRadar) {
        if (regionalRadarChartInstance) regionalRadarChartInstance.destroy();
        regionalRadarChartInstance = new Chart(ctxRadar, {
          type: 'radar',
          data: {
            labels: ['Solar Irradiance', 'Grid Transmission', 'Industrial Demand', 'DPPA Readiness', 'EV Fast Density'],
            datasets: [
              {
                label: 'Southern Economic Zone',
                data: [95, 78, 92, 88, 85],
                borderColor: '#14B8A6',
                backgroundColor: isDark ? 'rgba(20, 184, 166, 0.25)' : 'rgba(20, 184, 166, 0.15)',
                borderWidth: 2,
                pointRadius: 3
              },
              {
                label: 'Northern Economic Zone',
                data: [65, 92, 85, 74, 82],
                borderColor: '#3B82F6',
                backgroundColor: isDark ? 'rgba(59, 130, 246, 0.25)' : 'rgba(59, 130, 246, 0.15)',
                borderWidth: 2,
                pointRadius: 3
              },
              {
                label: 'Central Coastal Zone',
                data: [88, 70, 55, 80, 68],
                borderColor: '#F59E0B',
                backgroundColor: isDark ? 'rgba(245, 158, 11, 0.25)' : 'rgba(245, 158, 11, 0.15)',
                borderWidth: 2,
                pointRadius: 3
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
              r: {
                angleLines: { color: theme.gridColor },
                grid: { color: theme.gridColor },
                pointLabels: { color: theme.textColor, font: { size: 10 } },
                ticks: { display: false, maxTicksLimit: 5 }
              }
            }
          }
        });
      }

      // 4. EV Network Speed & Operator Bar
      const ctxEv = document.getElementById('evNetworkChart')?.getContext('2d');
      if (ctxEv) {
        if (evChartInstance) evChartInstance.destroy();
        evChartInstance = new Chart(ctxEv, {
          type: 'bar',
          data: {
            labels: ['VinFast (V-GREEN)', 'EV ONE Network', 'Charge+ & Autel', 'Other Independent CPOs'],
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

    // Trajectory Mode Switcher Buttons
    function setTrajectoryMode(mode) {
      currentTrajectoryMode = mode;
      const btnCap = document.getElementById('btnTrajectoryCapacity');
      const btnShare = document.getElementById('btnTrajectoryShare');
      const btnCarbon = document.getElementById('btnTrajectoryCarbon');

      [btnCap, btnShare, btnCarbon].forEach(b => {
        b.className = 'px-2 py-0.5 rounded text-slate-500 dark:text-slate-400 hover:text-teal-600';
      });

      if (mode === 'capacity') {
        btnCap.className = 'px-2 py-0.5 rounded bg-white dark:bg-darkSurface text-teal-600 dark:text-teal-400 font-bold shadow-xs';
      } else if (mode === 'share') {
        btnShare.className = 'px-2 py-0.5 rounded bg-white dark:bg-darkSurface text-teal-600 dark:text-teal-400 font-bold shadow-xs';
      } else if (mode === 'carbon') {
        btnCarbon.className = 'px-2 py-0.5 rounded bg-white dark:bg-darkSurface text-teal-600 dark:text-teal-400 font-bold shadow-xs';
      }

      initCharts();
    }

    document.getElementById('btnTrajectoryCapacity')?.addEventListener('click', () => setTrajectoryMode('capacity'));
    document.getElementById('btnTrajectoryShare')?.addEventListener('click', () => setTrajectoryMode('share'));
    document.getElementById('btnTrajectoryCarbon')?.addEventListener('click', () => setTrajectoryMode('carbon'));

    // Decree 80 Simulator Logic
    const sliderCapacity = document.getElementById('sliderCapacity');
    const sliderFactor = document.getElementById('sliderFactor');
    const sliderCapacityVal = document.getElementById('sliderCapacityVal');
    const sliderFactorVal = document.getElementById('sliderFactorVal');
    const simEnergyOut = document.getElementById('simEnergyOut');
    const simCo2Out = document.getElementById('simCo2Out');
    const simSavingsOut = document.getElementById('simSavingsOut');

    function updateSimulator() {
      const capMw = parseFloat(sliderCapacity.value);
      const factorPct = parseFloat(sliderFactor.value);

      sliderCapacityVal.textContent = `${capMw} MW`;
      let factorLabel = `${factorPct}%`;
      if (factorPct <= 18) factorLabel += ' (Rooftop Low)';
      else if (factorPct <= 25) factorLabel += ' (Solar Avg)';
      else factorLabel += ' (Wind High)';
      sliderFactorVal.textContent = factorLabel;

      // Annual Energy: MW * 8760 hours * (factor / 100)
      const annualMwh = Math.round(capMw * 8760 * (factorPct / 100));
      // CO2 Abatement: Vietnam grid emission factor 0.7221 tCO2/MWh
      const co2Tonnes = Math.round(annualMwh * 0.7221);
      // 10-Yr Grid Parity Savings: Assume ~$20/MWh net savings vs standard industrial retail tariff
      const savingsUsdM = ((annualMwh * 20 * 10) / 1000000).toFixed(2);

      simEnergyOut.textContent = `${annualMwh.toLocaleString()} MWh`;
      simCo2Out.textContent = `${co2Tonnes.toLocaleString()} tCO2e`;
      simSavingsOut.textContent = `$${savingsUsdM} M`;
    }

    sliderCapacity?.addEventListener('input', updateSimulator);
    sliderFactor?.addEventListener('input', updateSimulator);

    // Theme Switcher Logic
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

    // Run simulator initial pass
    updateSimulator();
  </script>
</body>
</html>
"""

base_dir = r"G:\My Drive\7. AI\RenewableVietNam"
index_file = os.path.join(base_dir, "index.html")
rev13_file = os.path.join(base_dir, "index_Rev.013.html")

# Non-destructive sequential revision
with open(rev13_file, "w", encoding="utf-8") as f:
    f.write(DASHBOARD_HTML)
print(f"Created sequential revision: {rev13_file}")

with open(index_file, "w", encoding="utf-8") as f:
    f.write(DASHBOARD_HTML)
print(f"Updated active homepage: {index_file}")
