#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate index_Rev.020.html for the master homepage (renewablevietnam.com):
Expands Section 2 into a 10-Module Institutional Visual Telemetry Suite:
1. Vietnam Clean Energy Trajectory (2020-2050) [Multi-Horizon Line/Area]
2. PDP8 Statutory Technology Mix (2030 Mandate) [Doughnut]
3. 5-Axis Regional Clean Energy Competitiveness [Radar]
4. National EV Charging Network Velocity & CPO Slices [Stacked Bar]
5. National 24-Hour Load Curve & Merit-Order Dispatch [Stacked Area / Step-Line]
6. PDP8 Statutory Capital Expenditure (CapEx) Allocation [Polar Area]
7. Substation Voltage & Headroom Hierarchy [Layered Bar]
8. Wholesale Electricity Market (VWEM) Price Clearing Dynamics [Multi-Series Curve]
9. Top 10 Energy Provinces: Capacity vs Eco-Industrial Parks [Dual-Axis Mixed Bar & Line]
10. End-to-End Systemic Energy Transition Flow & Power Balance [Directional Pipeline Balance Diagram]
"""

from pathlib import Path
import re

SOURCE_HTML = Path(r"G:\My Drive\7. AI\RenewableVietNam\index_Rev.019.html")
TARGET_REV = Path(r"G:\My Drive\7. AI\RenewableVietNam\index_Rev.020.html")

def generate():
    with open(SOURCE_HTML, "r", encoding="utf-8") as f:
        html = f.read()

    # Define the 10-module HTML Section 2
    section_2_html = """    <!-- SECTION 2: 10-MODULE INSTITUTIONAL VISUAL TELEMETRY SUITE -->
    <section class="space-y-4" id="visualTelemetrySuiteSection">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-100 dark:border-slate-700/50 pb-2">
        <div>
          <h2 class="text-xs sm:text-sm font-semibold uppercase tracking-wider text-slate-800 dark:text-slate-200 flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
            Comprehensive 10-Module Visual Telemetry &amp; Analytical Suite
          </h2>
          <p class="text-[11px] text-slate-500 dark:text-slate-400 mt-0.5">
            Quantitative models covering long-term net-zero trajectories, merit-order dispatch curves, capital expenditure allocations, grid voltage hierarchies, wholesale market clearing, and territorial power balance.
          </p>
        </div>
        <div class="flex items-center gap-2 font-mono text-[10px]">
          <span class="px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border border-emerald-500/20 font-semibold">10 Active Visualizations</span>
          <span class="text-slate-400">Horizon: 2026&ndash;2050</span>
        </div>
      </div>

      <!-- 4 Compact Telemetry KPI Gauges -->
      <div class="grid grid-cols-2 lg:grid-cols-4 gap-2.5 sm:gap-3 font-mono">
        <div class="bg-white dark:bg-slate-800/80 border border-slate-200/70 dark:border-slate-700/60 rounded-xl p-3 shadow-xs">
          <div class="flex justify-between items-baseline text-[10px]">
            <span class="text-slate-500 dark:text-slate-400">PDP8 RE Realization</span>
            <strong class="text-slate-800 dark:text-slate-200 font-semibold text-xs">31.5%</strong>
          </div>
          <div class="w-full bg-slate-100 dark:bg-slate-700/60 h-1.5 rounded-full mt-2 overflow-hidden">
            <div class="bg-teal-600 dark:bg-teal-400 h-full rounded-full" style="width: 31.5%"></div>
          </div>
          <span class="block text-[9px] text-slate-500 dark:text-slate-400 mt-1.5">14.8 GW / 47.0 GW Target</span>
        </div>

        <div class="bg-white dark:bg-slate-800/80 border border-slate-200/70 dark:border-slate-700/60 rounded-xl p-3 shadow-xs">
          <div class="flex justify-between items-baseline text-[10px]">
            <span class="text-slate-500 dark:text-slate-400">Decree 80 DPPA</span>
            <strong class="text-slate-800 dark:text-slate-200 font-semibold text-xs">100%</strong>
          </div>
          <div class="w-full bg-slate-100 dark:bg-slate-700/60 h-1.5 rounded-full mt-2 overflow-hidden">
            <div class="bg-teal-600 dark:bg-teal-400 h-full rounded-full" style="width: 100%"></div>
          </div>
          <span class="block text-[9px] text-slate-500 dark:text-slate-400 mt-1.5">Statutory Clearance Active</span>
        </div>

        <div class="bg-white dark:bg-slate-800/80 border border-slate-200/70 dark:border-slate-700/60 rounded-xl p-3 shadow-xs">
          <div class="flex justify-between items-baseline text-[10px]">
            <span class="text-slate-500 dark:text-slate-400">Expressway EV Fast</span>
            <strong class="text-slate-800 dark:text-slate-200 font-semibold text-xs">95.2%</strong>
          </div>
          <div class="w-full bg-slate-100 dark:bg-slate-700/60 h-1.5 rounded-full mt-2 overflow-hidden">
            <div class="bg-amber-600 dark:bg-amber-400 h-full rounded-full" style="width: 95.2%"></div>
          </div>
          <span class="block text-[9px] text-slate-500 dark:text-slate-400 mt-1.5">Route 1A &amp; CT.01 Corridors</span>
        </div>

        <div class="bg-white dark:bg-slate-800/80 border border-slate-200/70 dark:border-slate-700/60 rounded-xl p-3 shadow-xs">
          <div class="flex justify-between items-baseline text-[10px]">
            <span class="text-slate-500 dark:text-slate-400">Eco-Park ESG Share</span>
            <strong class="text-slate-800 dark:text-slate-200 font-semibold text-xs">42.0%</strong>
          </div>
          <div class="w-full bg-slate-100 dark:bg-slate-700/60 h-1.5 rounded-full mt-2 overflow-hidden">
            <div class="bg-blue-600 dark:bg-blue-400 h-full rounded-full" style="width: 42.0%"></div>
          </div>
          <span class="block text-[9px] text-slate-500 dark:text-slate-400 mt-1.5">71 of 168 Hubs Certified</span>
        </div>
      </div>

      <!-- VISUAL ROW 1: TRAJECTORY AREA & PDP8 TECHNOLOGY MIX (CHARTS 01 & 02) -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-4">
        
        <!-- Visual 01: 2025-2050 Net Zero Transition Trajectory (7 cols) -->
        <div class="lg:col-span-7 bg-white dark:bg-slate-800/80 border border-slate-200/70 dark:border-slate-700/60 rounded-2xl p-4 sm:p-5 shadow-xs flex flex-col justify-between">
          <div>
            <div class="flex flex-col sm:flex-row sm:items-center justify-between pb-2.5 mb-2.5 border-b border-slate-100 dark:border-slate-700/50 gap-2">
              <div>
                <span class="font-mono text-[9px] uppercase font-bold text-teal-600 dark:text-teal-400 block">VISUAL 01 &middot; MULTI-HORIZON TRAJECTORY</span>
                <span class="text-xs font-semibold text-slate-800 dark:text-slate-200">Vietnam Clean Energy Trajectory (2020&ndash;2050)</span>
                <span class="text-[10px] text-slate-500 dark:text-slate-400 block">Long-term transition path from baseline to 500 GW Net Zero</span>
              </div>
              <div class="flex items-center gap-1 font-mono text-[10px] bg-slate-100 dark:bg-slate-700/50 p-0.5 rounded-lg border border-slate-200/60 dark:border-slate-600/50 self-start sm:self-auto">
                <button id="btnTrajectoryCapacity" class="px-2 py-0.5 rounded bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-200 font-medium shadow-xs">GW</button>
                <button id="btnTrajectoryShare" class="px-2 py-0.5 rounded text-slate-500 dark:text-slate-400 hover:text-slate-800 dark:hover:text-slate-200">RE %</button>
                <button id="btnTrajectoryCarbon" class="px-2 py-0.5 rounded text-slate-500 dark:text-slate-400 hover:text-slate-800 dark:hover:text-slate-200">CO2 Mt</button>
              </div>
            </div>
            <div class="relative h-60">
              <canvas id="trajectoryChart"></canvas>
            </div>
          </div>
          <div class="flex items-center justify-between font-mono text-[10px] text-slate-500 dark:text-slate-400 pt-2.5 border-t border-slate-100 dark:border-slate-700/50">
            <span>2020: 69.3 GW</span>
            <span>2030 (PDP8): 150.5 GW</span>
            <span>2050 (Net Zero): 500.0 GW</span>
          </div>
        </div>

        <!-- Visual 02: PDP8 Statutory Capacity Breakdown (5 cols) -->
        <div class="lg:col-span-5 bg-white dark:bg-slate-800/80 border border-slate-200/70 dark:border-slate-700/60 rounded-2xl p-4 sm:p-5 shadow-xs flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-2.5 mb-2.5 border-b border-slate-100 dark:border-slate-700/50">
              <div>
                <span class="font-mono text-[9px] uppercase font-bold text-blue-600 dark:text-blue-400 block">VISUAL 02 &middot; STATUTORY ALLOCATION</span>
                <span class="text-xs font-semibold text-slate-800 dark:text-slate-200">PDP8 Technology Quota Mix (2030)</span>
                <span class="text-[10px] text-slate-500 dark:text-slate-400 block">Statutory allocation across generation archetypes</span>
              </div>
              <span class="font-mono text-[10px] text-slate-700 dark:text-slate-300 font-semibold bg-slate-100 dark:bg-slate-700/50 px-2 py-0.5 rounded border border-slate-200/60 dark:border-slate-600/50">
                150.5 GW
              </span>
            </div>
            <div class="relative h-60 flex items-center justify-center">
              <canvas id="pdp8MixChart"></canvas>
            </div>
          </div>
          <div class="grid grid-cols-3 gap-1.5 text-center font-mono text-[9px] pt-2.5 border-t border-slate-100 dark:border-slate-700/50">
            <div class="p-1 rounded bg-slate-50 dark:bg-slate-800/50">
              <span class="text-slate-500 dark:text-slate-400 block">Thermal LNG</span>
              <strong class="text-slate-700 dark:text-slate-300">37.3 GW</strong>
            </div>
            <div class="p-1 rounded bg-slate-50 dark:bg-slate-800/50">
              <span class="text-slate-500 dark:text-slate-400 block">Hydro</span>
              <strong class="text-slate-700 dark:text-slate-300">29.3 GW</strong>
            </div>
            <div class="p-1 rounded bg-slate-50 dark:bg-slate-800/50">
              <span class="text-slate-500 dark:text-slate-400 block">Wind/Solar</span>
              <strong class="text-teal-700 dark:text-teal-300">40.7 GW</strong>
            </div>
          </div>
        </div>

      </div>

      <!-- VISUAL ROW 2: 5-AXIS RADAR & EV CHARGING VELOCITY (CHARTS 03 & 04) -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-4">

        <!-- Visual 03: 5-Axis Regional Clean Energy Competitiveness Radar (6 cols) -->
        <div class="lg:col-span-6 bg-white dark:bg-slate-800/80 border border-slate-200/70 dark:border-slate-700/60 rounded-2xl p-4 sm:p-5 shadow-xs flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-2.5 mb-2 border-b border-slate-100 dark:border-slate-700/50">
              <div>
                <span class="font-mono text-[9px] uppercase font-bold text-amber-600 dark:text-amber-400 block">VISUAL 03 &middot; REGIONAL VECTOR ANALYSIS</span>
                <span class="text-xs font-semibold text-slate-800 dark:text-slate-200">5-Axis Regional Clean Competitiveness</span>
                <span class="text-[10px] text-slate-500 dark:text-slate-400 block">South vs North vs Central across 5 infrastructure vectors</span>
              </div>
              <span class="font-mono text-[10px] text-slate-700 dark:text-slate-300 font-semibold bg-slate-100 dark:bg-slate-700/50 px-2 py-0.5 rounded border border-slate-200/60 dark:border-slate-600/50">
                168 Hubs
              </span>
            </div>
            <div class="relative h-64 flex items-center justify-center">
              <canvas id="regionalRadarChart"></canvas>
            </div>
          </div>
          <div class="flex items-center justify-between text-[10px] font-mono text-slate-500 dark:text-slate-400 pt-2.5 border-t border-slate-100 dark:border-slate-700/50">
            <span>South: High Solar &amp; Demand</span>
            <span>North: High Grid Stability</span>
            <span>Central: High Wind</span>
          </div>
        </div>

        <!-- Visual 04: National EV Charging Infrastructure Footprint (6 cols) -->
        <div class="lg:col-span-6 bg-white dark:bg-slate-800/80 border border-slate-200/70 dark:border-slate-700/60 rounded-2xl p-4 sm:p-5 shadow-xs flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-2.5 mb-2 border-b border-slate-100 dark:border-slate-700/50">
              <div>
                <span class="font-mono text-[9px] uppercase font-bold text-emerald-600 dark:text-emerald-400 block">VISUAL 04 &middot; E-MOBILITY DENSITY</span>
                <span class="text-xs font-semibold text-slate-800 dark:text-slate-200">EV Charging Network Velocity &amp; CPO Slices</span>
                <span class="text-[10px] text-slate-500 dark:text-slate-400 block">22,055+ verified ports across operators &amp; charging tiers</span>
              </div>
              <span class="font-mono text-[10px] text-slate-700 dark:text-slate-300 font-semibold bg-slate-100 dark:bg-slate-700/50 px-2 py-0.5 rounded border border-slate-200/60 dark:border-slate-600/50">
                62% DC Fast
              </span>
            </div>
            <div class="relative h-64">
              <canvas id="evNetworkChart"></canvas>
            </div>
          </div>
          <div class="grid grid-cols-4 gap-1 text-center font-mono text-[9px] pt-2.5 border-t border-slate-100 dark:border-slate-700/50">
            <div class="p-1 rounded bg-slate-50 dark:bg-slate-800/50">
              <span class="text-slate-500 dark:text-slate-400 block">VinFast</span>
              <strong class="text-slate-800 dark:text-slate-200 font-medium">18,500</strong>
            </div>
            <div class="p-1 rounded bg-slate-50 dark:bg-slate-800/50">
              <span class="text-slate-500 dark:text-slate-400 block">EV ONE</span>
              <strong class="text-slate-800 dark:text-slate-200 font-medium">1,800</strong>
            </div>
            <div class="p-1 rounded bg-slate-50 dark:bg-slate-800/50">
              <span class="text-slate-500 dark:text-slate-400 block">Charge+</span>
              <strong class="text-slate-800 dark:text-slate-200 font-medium">1,755</strong>
            </div>
            <div class="p-1 rounded bg-slate-50 dark:bg-slate-800/50">
              <span class="text-slate-500 dark:text-slate-400 block">DC Fast &ge;60kW</span>
              <strong class="text-teal-700 dark:text-teal-300 font-medium">13,674</strong>
            </div>
          </div>
        </div>

      </div>

      <!-- VISUAL ROW 3: 24H LOAD CURVE & CAPEX ALLOCATION (CHARTS 05 & 06) -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-4">

        <!-- Visual 05: National 24-Hour Load Curve & Merit-Order Dispatch (7 cols) -->
        <div class="lg:col-span-7 bg-white dark:bg-slate-800/80 border border-slate-200/70 dark:border-slate-700/60 rounded-2xl p-4 sm:p-5 shadow-xs flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-2.5 mb-2 border-b border-slate-100 dark:border-slate-700/50">
              <div>
                <span class="font-mono text-[9px] uppercase font-bold text-rose-600 dark:text-rose-400 block">VISUAL 05 &middot; MERIT-ORDER DISPATCH</span>
                <span class="text-xs font-semibold text-slate-800 dark:text-slate-200">National 24-Hour Load Curve &amp; Merit-Order Dispatch</span>
                <span class="text-[10px] text-slate-500 dark:text-slate-400 block">Simulating solar midday belly, wind evening ramp, and hydro peak shaving</span>
              </div>
              <span class="font-mono text-[10px] text-rose-600 dark:text-rose-400 font-semibold bg-rose-50 dark:bg-rose-950/40 px-2 py-0.5 rounded border border-rose-200 dark:border-rose-800/40">
                Pmax 48.5 GW
              </span>
            </div>
            <div class="relative h-64">
              <canvas id="dailyDispatchChart"></canvas>
            </div>
          </div>
          <div class="flex items-center justify-between text-[10px] font-mono text-slate-500 dark:text-slate-400 pt-2.5 border-t border-slate-100 dark:border-slate-700/50">
            <span>Midday Solar: Peak 16.5 GW</span>
            <span>Evening Peak (18-20h): 48.5 GW</span>
            <span>Night Baseload: 28.0 GW</span>
          </div>
        </div>

        <!-- Visual 06: PDP8 Statutory Capital Expenditure (CapEx) Allocation (5 cols) -->
        <div class="lg:col-span-5 bg-white dark:bg-slate-800/80 border border-slate-200/70 dark:border-slate-700/60 rounded-2xl p-4 sm:p-5 shadow-xs flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-2.5 mb-2 border-b border-slate-100 dark:border-slate-700/50">
              <div>
                <span class="font-mono text-[9px] uppercase font-bold text-violet-600 dark:text-violet-400 block">VISUAL 06 &middot; CAPITAL EXPENDITURE ALLOCATION</span>
                <span class="text-xs font-semibold text-slate-800 dark:text-slate-200">PDP8 Statutory CapEx Allocation</span>
                <span class="text-[10px] text-slate-500 dark:text-slate-400 block">$134.7B statutory capital requirements through 2030</span>
              </div>
              <span class="font-mono text-[10px] text-violet-600 dark:text-violet-400 font-semibold bg-violet-50 dark:bg-violet-950/40 px-2 py-0.5 rounded border border-violet-200 dark:border-violet-800/40">
                $134.7B Total
              </span>
            </div>
            <div class="relative h-64 flex items-center justify-center">
              <canvas id="capexAllocationChart"></canvas>
            </div>
          </div>
          <div class="grid grid-cols-3 gap-1.5 text-center font-mono text-[9px] pt-2.5 border-t border-slate-100 dark:border-slate-700/50">
            <div class="p-1 rounded bg-slate-50 dark:bg-slate-800/50">
              <span class="text-slate-500 dark:text-slate-400 block">Gas &amp; LNG</span>
              <strong class="text-slate-700 dark:text-slate-300">$31.4B</strong>
            </div>
            <div class="p-1 rounded bg-slate-50 dark:bg-slate-800/50">
              <span class="text-slate-500 dark:text-slate-400 block">Onshore Wind</span>
              <strong class="text-teal-700 dark:text-teal-300">$26.2B</strong>
            </div>
            <div class="p-1 rounded bg-slate-50 dark:bg-slate-800/50">
              <span class="text-slate-500 dark:text-slate-400 block">Offshore Wind</span>
              <strong class="text-blue-700 dark:text-blue-300">$18.5B</strong>
            </div>
          </div>
        </div>

      </div>

      <!-- VISUAL ROW 4: SUBSTATION HIERARCHY & MARKET CLEARING PRICES (CHARTS 07 & 08) -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-4">

        <!-- Visual 07: Substation Voltage & Headroom Hierarchy (6 cols) -->
        <div class="lg:col-span-6 bg-white dark:bg-slate-800/80 border border-slate-200/70 dark:border-slate-700/60 rounded-2xl p-4 sm:p-5 shadow-xs flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-2.5 mb-2 border-b border-slate-100 dark:border-slate-700/50">
              <div>
                <span class="font-mono text-[9px] uppercase font-bold text-fuchsia-600 dark:text-fuchsia-400 block">VISUAL 07 &middot; GRID TOPOLOGY HIERARCHY</span>
                <span class="text-xs font-semibold text-slate-800 dark:text-slate-200">Substation Voltage &amp; Transformer Headroom</span>
                <span class="text-[10px] text-slate-500 dark:text-slate-400 block">1,915 national substations: Installed MVA vs available headroom</span>
              </div>
              <span class="font-mono text-[10px] text-slate-700 dark:text-slate-300 font-semibold bg-slate-100 dark:bg-slate-700/50 px-2 py-0.5 rounded border border-slate-200/60 dark:border-slate-600/50">
                1,915 Units
              </span>
            </div>
            <div class="relative h-64">
              <canvas id="substationHierarchyChart"></canvas>
            </div>
          </div>
          <div class="flex items-center justify-between text-[10px] font-mono text-slate-500 dark:text-slate-400 pt-2.5 border-t border-slate-100 dark:border-slate-700/50">
            <span>500kV: 8,700 MVA Peak Hub</span>
            <span>220kV: 27,007 km Circuits</span>
            <span>110kV: Industrial Feeders</span>
          </div>
        </div>

        <!-- Visual 08: Wholesale Market (VWEM) Price Clearing Dynamics (6 cols) -->
        <div class="lg:col-span-6 bg-white dark:bg-slate-800/80 border border-slate-200/70 dark:border-slate-700/60 rounded-2xl p-4 sm:p-5 shadow-xs flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-2.5 mb-2 border-b border-slate-100 dark:border-slate-700/50">
              <div>
                <span class="font-mono text-[9px] uppercase font-bold text-amber-600 dark:text-amber-400 block">VISUAL 08 &middot; MARKET CLEARING DYNAMICS</span>
                <span class="text-xs font-semibold text-slate-800 dark:text-slate-200">VWEM Spot Clearing vs DPPA vs TOU Retail</span>
                <span class="text-[10px] text-slate-500 dark:text-slate-400 block">System Marginal Price (SMP) dynamics vs industrial retail tariff schedules</span>
              </div>
              <span class="font-mono text-[10px] text-emerald-600 dark:text-emerald-400 font-semibold bg-emerald-50 dark:bg-emerald-950/40 px-2 py-0.5 rounded border border-emerald-200 dark:border-emerald-800/40">
                FMP 1,825 VND
              </span>
            </div>
            <div class="relative h-64">
              <canvas id="marketClearingChart"></canvas>
            </div>
          </div>
          <div class="flex items-center justify-between text-[10px] font-mono text-slate-500 dark:text-slate-400 pt-2.5 border-t border-slate-100 dark:border-slate-700/50">
            <span>Off-Peak: 1,100 VND</span>
            <span>Normal: 1,685 VND</span>
            <span>Peak TOU: 3,171 VND</span>
          </div>
        </div>

      </div>

      <!-- VISUAL ROW 5: PROVINCIAL CAPACITY & SYSTEMIC ENERGY FLOW (CHARTS 09 & 10) -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-4">

        <!-- Visual 09: Top 10 Energy Provinces: Clean Capacity vs Eco-Parks (6 cols) -->
        <div class="lg:col-span-6 bg-white dark:bg-slate-800/80 border border-slate-200/70 dark:border-slate-700/60 rounded-2xl p-4 sm:p-5 shadow-xs flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-2.5 mb-2 border-b border-slate-100 dark:border-slate-700/50">
              <div>
                <span class="font-mono text-[9px] uppercase font-bold text-cyan-600 dark:text-cyan-400 block">VISUAL 09 &middot; TERRITORIAL CLUSTERING</span>
                <span class="text-xs font-semibold text-slate-800 dark:text-slate-200">Top 10 Energy Provinces: Capacity vs Eco-Parks</span>
                <span class="text-[10px] text-slate-500 dark:text-slate-400 block">Correlating clean generation (MW) with industrial manufacturing hubs</span>
              </div>
              <span class="font-mono text-[10px] text-cyan-600 dark:text-cyan-400 font-semibold bg-cyan-50 dark:bg-cyan-950/40 px-2 py-0.5 rounded border border-cyan-200 dark:border-cyan-800/40">
                10 Strategic Provinces
              </span>
            </div>
            <div class="relative h-64">
              <canvas id="topProvincesEcoparkChart"></canvas>
            </div>
          </div>
          <div class="flex items-center justify-between text-[10px] font-mono text-slate-500 dark:text-slate-400 pt-2.5 border-t border-slate-100 dark:border-slate-700/50">
            <span>Top Generation: Ninh Thuận &amp; Bình Thuận</span>
            <span>Top Demand: Bình Dương &amp; Đồng Nai</span>
          </div>
        </div>

        <!-- Visual 10: End-to-End Systemic Energy Transition Flow Diagram (6 cols) -->
        <div class="lg:col-span-6 bg-white dark:bg-slate-800/80 border border-slate-200/70 dark:border-slate-700/60 rounded-2xl p-4 sm:p-5 shadow-xs flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-2.5 mb-2 border-b border-slate-100 dark:border-slate-700/50">
              <div>
                <span class="font-mono text-[9px] uppercase font-bold text-teal-600 dark:text-teal-400 block">VISUAL 10 &middot; SYSTEMIC POWER BALANCE</span>
                <span class="text-xs font-semibold text-slate-800 dark:text-slate-200">Systemic Energy Flow &amp; Power Balance Pipeline</span>
                <span class="text-[10px] text-slate-500 dark:text-slate-400 block">Primary supply sources &rarr; 500kV supergrid transmission &rarr; sectoral demand sinks</span>
              </div>
              <span class="font-mono text-[10px] text-teal-600 dark:text-teal-400 font-semibold bg-teal-50 dark:bg-teal-950/40 px-2 py-0.5 rounded border border-teal-200 dark:border-teal-800/40">
                280.5 TWh Baseline
              </span>
            </div>

            <!-- Directional Flow Diagram Canvas -->
            <div class="p-3 rounded-xl bg-slate-50 dark:bg-slate-900/60 border border-slate-200/60 dark:border-slate-700/50 font-mono text-xs space-y-2.5 my-2">
              <div class="grid grid-cols-3 gap-2 text-center text-[10px]">
                <div class="p-2 rounded-lg bg-white dark:bg-slate-800 border border-slate-200/60 dark:border-slate-700/60 space-y-1">
                  <span class="text-slate-400 uppercase text-[9px] font-bold block">1. Generation Inputs</span>
                  <div class="text-xs font-bold text-teal-600 dark:text-teal-400">84.0 GW Installed</div>
                  <span class="text-[9px] text-slate-500 block">Solar, Wind, Hydro, LNG</span>
                </div>
                <div class="p-2 rounded-lg bg-white dark:bg-slate-800 border border-slate-200/60 dark:border-slate-700/60 space-y-1">
                  <span class="text-slate-400 uppercase text-[9px] font-bold block">2. Supergrid Wheel</span>
                  <div class="text-xs font-bold text-rose-600 dark:text-rose-400">65,566 km Circuits</div>
                  <span class="text-[9px] text-slate-500 block">500kV/220kV 3.2 GW Flow</span>
                </div>
                <div class="p-2 rounded-lg bg-white dark:bg-slate-800 border border-slate-200/60 dark:border-slate-700/60 space-y-1">
                  <span class="text-slate-400 uppercase text-[9px] font-bold block">3. Demand Sinks</span>
                  <div class="text-xs font-bold text-blue-600 dark:text-blue-400">100% Allocation</div>
                  <span class="text-[9px] text-slate-500 block">Industry, EVs, Urban</span>
                </div>
              </div>

              <!-- Stream Vector Progressions -->
              <div class="space-y-1.5 pt-1 text-[10px]">
                <div class="flex justify-between">
                  <span class="text-slate-600 dark:text-slate-400 font-semibold">Industrial Clean Manufacturing (RE100)</span>
                  <strong class="text-teal-600 dark:text-teal-400">54.2% (~152 TWh)</strong>
                </div>
                <div class="w-full bg-slate-200 dark:bg-slate-700 h-1.5 rounded-full overflow-hidden">
                  <div class="bg-teal-500 h-full rounded-full" style="width: 54%"></div>
                </div>

                <div class="flex justify-between pt-1">
                  <span class="text-slate-600 dark:text-slate-400 font-semibold">Commercial Buildings &amp; Urban Load</span>
                  <strong class="text-indigo-600 dark:text-indigo-400">35.8% (~100 TWh)</strong>
                </div>
                <div class="w-full bg-slate-200 dark:bg-slate-700 h-1.5 rounded-full overflow-hidden">
                  <div class="bg-indigo-500 h-full rounded-full" style="width: 36%"></div>
                </div>

                <div class="flex justify-between pt-1">
                  <span class="text-slate-600 dark:text-slate-400 font-semibold">Electric Mobility &amp; Charging Fleet</span>
                  <strong class="text-emerald-600 dark:text-emerald-400">6.5% (~18 TWh)</strong>
                </div>
                <div class="w-full bg-slate-200 dark:bg-slate-700 h-1.5 rounded-full overflow-hidden">
                  <div class="bg-emerald-500 h-full rounded-full" style="width: 7%"></div>
                </div>

                <div class="flex justify-between pt-1">
                  <span class="text-slate-600 dark:text-slate-400 font-semibold">Green Hydrogen Synthesis &amp; Export</span>
                  <strong class="text-violet-600 dark:text-violet-400">3.5% (~10 TWh)</strong>
                </div>
                <div class="w-full bg-slate-200 dark:bg-slate-700 h-1.5 rounded-full overflow-hidden">
                  <div class="bg-violet-500 h-full rounded-full" style="width: 4%"></div>
                </div>
              </div>
            </div>
          </div>
          <div class="flex items-center justify-between text-[10px] font-mono text-slate-500 dark:text-slate-400 pt-2.5 border-t border-slate-100 dark:border-slate-700/50">
            <span>Transmission Loss: 6.25%</span>
            <span>Decree 80 Direct Wheeling Active</span>
          </div>
        </div>

      </div>"""

    # Replace Section 2 HTML
    old_section_2_pattern = r'<!-- SECTION 2: MULTI-GRAPH INTERACTIVE VISUALIZATION SUITE -->[\s\S]*?<!-- SECTION 3: INTERACTIVE DECREE 80 DPPA ECONOMIC SIMULATOR -->'
    assert re.search(old_section_2_pattern, html), "Failed to find Section 2 in source HTML"
    html = re.sub(old_section_2_pattern, f"{section_2_html}\n\n      <!-- SECTION 3: INTERACTIVE DECREE 80 DPPA ECONOMIC SIMULATOR -->", html, count=1)

    # Now add all new chart instances and initialization code
    new_chart_instances = """    // Chart instances
    let trajectoryChartInstance = null;
    let pdp8ChartInstance = null;
    let regionalRadarChartInstance = null;
    let evChartInstance = null;
    let dailyDispatchChartInstance = null;
    let capexAllocationChartInstance = null;
    let substationHierarchyChartInstance = null;
    let marketClearingChartInstance = null;
    let topProvincesEcoparkChartInstance = null;"""

    html = html.replace(
        """    // Chart instances
    let trajectoryChartInstance = null;
    let pdp8ChartInstance = null;
    let regionalRadarChartInstance = null;
    let evChartInstance = null;""",
        new_chart_instances,
        1
    )

    # Append new Chart implementations inside initCharts()
    new_charts_init_js = """
      // 5. National 24-Hour Load Curve & Merit-Order Dispatch (Stacked Area)
      const ctxDispatch = document.getElementById('dailyDispatchChart')?.getContext('2d');
      if (ctxDispatch) {
        if (dailyDispatchChartInstance) dailyDispatchChartInstance.destroy();
        dailyDispatchChartInstance = new Chart(ctxDispatch, {
          type: 'line',
          data: {
            labels: ['00:00', '02:00', '04:00', '06:00', '08:00', '10:00', '12:00', '14:00', '16:00', '18:00', '20:00', '22:00'],
            datasets: [
              {
                label: 'Baseload Gas/Coal (GW)',
                data: [18.0, 17.5, 17.0, 18.5, 20.0, 20.5, 20.0, 20.5, 21.0, 21.5, 20.5, 19.0],
                fill: true,
                backgroundColor: isDark ? 'rgba(100, 116, 139, 0.4)' : 'rgba(148, 163, 184, 0.35)',
                borderColor: '#64748B',
                tension: 0.3,
                borderWidth: 1.5,
                pointRadius: 0
              },
              {
                label: 'Cascade Hydro (GW)',
                data: [6.0, 5.5, 5.0, 6.5, 8.0, 7.5, 7.0, 7.5, 9.0, 14.5, 13.0, 8.0],
                fill: true,
                backgroundColor: isDark ? 'rgba(6, 182, 212, 0.4)' : 'rgba(6, 182, 212, 0.35)',
                borderColor: '#06B6D4',
                tension: 0.3,
                borderWidth: 1.5,
                pointRadius: 0
              },
              {
                label: 'Solar PV Surge (GW)',
                data: [0, 0, 0, 1.2, 7.5, 14.0, 16.5, 15.0, 8.0, 0.5, 0, 0],
                fill: true,
                backgroundColor: isDark ? 'rgba(245, 158, 11, 0.45)' : 'rgba(245, 158, 11, 0.35)',
                borderColor: '#F59E0B',
                tension: 0.3,
                borderWidth: 1.5,
                pointRadius: 0
              },
              {
                label: 'Wind Corridors (GW)',
                data: [3.8, 3.6, 3.5, 3.2, 3.0, 2.8, 3.2, 3.8, 4.5, 5.2, 5.0, 4.2],
                fill: true,
                backgroundColor: isDark ? 'rgba(16, 185, 129, 0.45)' : 'rgba(16, 185, 129, 0.35)',
                borderColor: '#10B981',
                tension: 0.3,
                borderWidth: 1.5,
                pointRadius: 0
              },
              {
                label: 'Pumped Hydro & BESS (GW)',
                data: [-1.5, -2.0, -1.8, 0, 0, -2.5, -3.0, -2.0, 0, 4.2, 3.5, 0],
                fill: false,
                borderColor: '#EC4899',
                borderWidth: 2,
                tension: 0.3,
                pointRadius: 2
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            interaction: { mode: 'index', intersect: false },
            plugins: {
              legend: {
                position: 'top',
                labels: { color: theme.textColor, font: { size: 9, family: 'monospace' }, boxWidth: 8 }
              },
              tooltip: {
                backgroundColor: theme.tooltipBg,
                titleColor: theme.tooltipText,
                bodyColor: theme.tooltipText,
                borderColor: theme.tooltipBorder,
                borderWidth: 1,
                callbacks: {
                  label: ctx => ` ${ctx.dataset.label}: ${ctx.raw} GW`
                }
              }
            },
            scales: {
              x: { grid: { color: theme.gridColor }, ticks: { color: theme.textColor, font: { size: 9 } } },
              y: {
                grid: { color: theme.gridColor },
                ticks: { color: theme.textColor, font: { size: 9, family: 'monospace' }, callback: v => `${v} GW` }
              }
            }
          }
        });
      }

      // 6. PDP8 Statutory CapEx Allocation Breakdown (Polar Area)
      const ctxCapex = document.getElementById('capexAllocationChart')?.getContext('2d');
      if (ctxCapex) {
        if (capexAllocationChartInstance) capexAllocationChartInstance.destroy();
        capexAllocationChartInstance = new Chart(ctxCapex, {
          type: 'polarArea',
          data: {
            labels: [
              'Gas & LNG ($31.4B)',
              'Onshore Wind ($26.2B)',
              'Offshore Wind ($18.5B)',
              '500kV/220kV Grid ($14.9B)',
              'Solar PV ($14.1B)',
              'Hydro & BESS ($11.8B)',
              'Hydrogen P2X ($6.2B)',
              'Smart Grid ($3.8B)',
              'Biomass ($3.6B)'
            ],
            datasets: [{
              data: [31.4, 26.2, 18.5, 14.9, 14.1, 11.8, 6.2, 3.8, 3.6],
              backgroundColor: [
                'rgba(59, 130, 246, 0.75)',
                'rgba(16, 185, 129, 0.75)',
                'rgba(20, 184, 166, 0.75)',
                'rgba(244, 63, 94, 0.75)',
                'rgba(245, 158, 11, 0.75)',
                'rgba(6, 182, 212, 0.75)',
                'rgba(139, 92, 246, 0.75)',
                'rgba(217, 70, 239, 0.75)',
                'rgba(34, 197, 94, 0.75)'
              ],
              borderColor: isDark ? '#1E293B' : '#FFFFFF',
              borderWidth: 1.5
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { display: false },
              tooltip: {
                backgroundColor: theme.tooltipBg,
                titleColor: theme.tooltipText,
                bodyColor: theme.tooltipText,
                borderColor: theme.tooltipBorder,
                borderWidth: 1,
                callbacks: {
                  label: ctx => ` ${ctx.label}: $${ctx.raw}B (${((ctx.raw / 134.7) * 100).toFixed(1)}%)`
                }
              }
            },
            scales: {
              r: {
                grid: { color: theme.gridColor },
                ticks: { display: false }
              }
            }
          }
        });
      }

      // 7. Substation Voltage & Headroom Hierarchy (Grouped Bar)
      const ctxSubH = document.getElementById('substationHierarchyChart')?.getContext('2d');
      if (ctxSubH) {
        if (substationHierarchyChartInstance) substationHierarchyChartInstance.destroy();
        substationHierarchyChartInstance = new Chart(ctxSubH, {
          type: 'bar',
          data: {
            labels: ['500kV Supergrid Hubs', '220kV Regional Hubs', '110kV Industrial Offtakes'],
            datasets: [
              {
                label: 'Installed Transformer Capacity (MVA)',
                data: [42500, 78200, 96000],
                backgroundColor: '#3B82F6',
                borderRadius: 4
              },
              {
                label: 'Available Intertie Headroom (MVA)',
                data: [14800, 22400, 31200],
                backgroundColor: '#10B981',
                borderRadius: 4
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
                labels: { color: theme.textColor, font: { size: 9, family: 'monospace' }, boxWidth: 10 }
              },
              tooltip: {
                backgroundColor: theme.tooltipBg,
                titleColor: theme.tooltipText,
                bodyColor: theme.tooltipText,
                borderColor: theme.tooltipBorder,
                borderWidth: 1,
                callbacks: {
                  label: ctx => ` ${ctx.dataset.label}: ${ctx.raw.toLocaleString()} MVA`
                }
              }
            },
            scales: {
              x: {
                grid: { color: theme.gridColor },
                ticks: { color: theme.textColor, font: { size: 9, family: 'monospace' }, callback: v => `${(v/1000).toFixed(0)}k MVA` }
              },
              y: {
                grid: { display: false },
                ticks: { color: theme.textColor, font: { size: 9, family: 'monospace' } }
              }
            }
          }
        });
      }

      // 8. Wholesale Market (VWEM) Price Clearing Dynamics (Multi-Series Line)
      const ctxMkt = document.getElementById('marketClearingChart')?.getContext('2d');
      if (ctxMkt) {
        if (marketClearingChartInstance) marketClearingChartInstance.destroy();
        marketClearingChartInstance = new Chart(ctxMkt, {
          type: 'line',
          data: {
            labels: ['00:00', '03:00', '06:00', '09:00', '11:00', '14:00', '17:00', '19:00', '21:00', '23:00'],
            datasets: [
              {
                label: 'VWEM Spot SMP (VND/kWh)',
                data: [1420, 1380, 1490, 1780, 1690, 1620, 1890, 1850, 1650, 1450],
                borderColor: '#10B981',
                backgroundColor: 'rgba(16, 185, 129, 0.08)',
                fill: true,
                tension: 0.35,
                borderWidth: 2,
                pointRadius: 2.5
              },
              {
                label: 'DPPA CfD Strike Benchmark (VND/kWh)',
                data: [1650, 1650, 1650, 1650, 1650, 1650, 1650, 1650, 1650, 1650],
                borderColor: '#3B82F6',
                borderDash: [5, 4],
                fill: false,
                borderWidth: 1.5,
                pointRadius: 0
              },
              {
                label: 'EVN Industrial Peak TOU (VND/kWh)',
                data: [1100, 1100, 1100, 3171, 3171, 1685, 3171, 3171, 1685, 1100],
                borderColor: '#F43F5E',
                fill: false,
                borderWidth: 1.5,
                stepped: true,
                pointRadius: 0
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            interaction: { mode: 'index', intersect: false },
            plugins: {
              legend: {
                position: 'top',
                labels: { color: theme.textColor, font: { size: 9, family: 'monospace' }, boxWidth: 10 }
              },
              tooltip: {
                backgroundColor: theme.tooltipBg,
                titleColor: theme.tooltipText,
                bodyColor: theme.tooltipText,
                borderColor: theme.tooltipBorder,
                borderWidth: 1,
                callbacks: {
                  label: ctx => ` ${ctx.dataset.label}: ${ctx.raw.toLocaleString()} VND`
                }
              }
            },
            scales: {
              x: { grid: { color: theme.gridColor }, ticks: { color: theme.textColor, font: { size: 9 } } },
              y: {
                grid: { color: theme.gridColor },
                ticks: { color: theme.textColor, font: { size: 9, family: 'monospace' }, callback: v => `${v} VND` }
              }
            }
          }
        });
      }

      // 9. Top 10 Energy Provinces: Clean Capacity vs Eco-Parks (Mixed Bar & Line)
      const ctxProv = document.getElementById('topProvincesEcoparkChart')?.getContext('2d');
      if (ctxProv) {
        if (topProvincesEcoparkChartInstance) topProvincesEcoparkChartInstance.destroy();
        topProvincesEcoparkChartInstance = new Chart(ctxProv, {
          type: 'bar',
          data: {
            labels: ['Ninh Thuận', 'Bình Thuận', 'Gia Lai', 'Đắk Lắk', 'Quảng Trị', 'Bình Dương', 'Đồng Nai', 'Hải Phòng', 'Bắc Ninh', 'Bà Rịa'],
            datasets: [
              {
                type: 'bar',
                label: 'Operating Clean Capacity (MW)',
                data: [3850, 3420, 2980, 2450, 1890, 850, 720, 650, 520, 1650],
                backgroundColor: '#14B8A6',
                yAxisID: 'y',
                borderRadius: 4
              },
              {
                type: 'line',
                label: 'Tier-1 Industrial Parks (Hubs)',
                data: [4, 6, 3, 2, 5, 29, 32, 14, 16, 15],
                borderColor: '#F59E0B',
                backgroundColor: '#F59E0B',
                borderWidth: 2,
                pointRadius: 3,
                yAxisID: 'y1'
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            interaction: { mode: 'index', intersect: false },
            plugins: {
              legend: {
                position: 'top',
                labels: { color: theme.textColor, font: { size: 9, family: 'monospace' }, boxWidth: 10 }
              },
              tooltip: {
                backgroundColor: theme.tooltipBg,
                titleColor: theme.tooltipText,
                bodyColor: theme.tooltipText,
                borderColor: theme.tooltipBorder,
                borderWidth: 1
              }
            },
            scales: {
              x: { grid: { color: theme.gridColor }, ticks: { color: theme.textColor, font: { size: 9 } } },
              y: {
                type: 'linear',
                position: 'left',
                grid: { color: theme.gridColor },
                ticks: { color: theme.textColor, font: { size: 9, family: 'monospace' }, callback: v => `${v} MW` }
              },
              y1: {
                type: 'linear',
                position: 'right',
                grid: { display: false },
                ticks: { color: '#F59E0B', font: { size: 9, family: 'monospace' }, callback: v => `${v} IPs` }
              }
            }
          }
        });
      }
"""

    # Inject new_charts_init_js right before closing bracket of initCharts()
    chart_init_anchor = "      // 4. EV Network Speed & Operator Bar"
    assert chart_init_anchor in html, "Failed to find chart_init_anchor"
    
    # Locate where evNetworkChart ends and inject
    old_ev_chart_pattern = r"(// 4\. EV Network Speed & Operator Bar[\s\S]*?}\s*}\);\s*})"
    m_ev = re.search(old_ev_chart_pattern, html)
    assert m_ev, "Failed to match evNetworkChart block"
    
    html = html[:m_ev.end(1)] + "\n" + new_charts_init_js + html[m_ev.end(1):]

    with open(TARGET_REV, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Successfully generated {TARGET_REV} ({len(html)} bytes)")

if __name__ == "__main__":
    generate()
