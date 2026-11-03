#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate index_Rev.019.html for the master homepage (renewablevietnam.com):
1. Upgrades Section 1 into the comprehensive 12 Strategic Pillars of Vietnam Energy Transition.
2. Implements category filter buttons: All Pillars (12), Generation (6), Grid & Supergrid (3), Market & Policy (3).
3. Expands the interactive node inspector drawer to cover all 12 pillars with technical KPIs, statutory basis, and direct subdomain gateway CTAs.
4. Preserves all other sections (multi-graph suite, subdomain consoles, header, footer) with zero disruption.
"""

from pathlib import Path
import re

SOURCE_HTML = Path(r"G:\My Drive\7. AI\RenewableVietNam\index.html")
TARGET_REV = Path(r"G:\My Drive\7. AI\RenewableVietNam\index_Rev.019.html")

def generate():
    with open(SOURCE_HTML, "r", encoding="utf-8") as f:
        html = f.read()

    # Define the 12-pillar HTML section
    pillars_section_html = """    <!-- SECTION 1: THE 12 STRATEGIC PILLARS OF VIETNAM ENERGY TRANSITION -->
    <section id="homepage12PillarsSection" class="bg-white dark:bg-slate-800/80 border border-slate-200/70 dark:border-slate-700/60 rounded-2xl p-4 sm:p-5 shadow-xs space-y-4">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-100 dark:border-slate-700/50 pb-3">
        <div class="space-y-1">
          <div class="flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-teal-600 dark:bg-teal-400 animate-pulse"></span>
            <span class="font-mono text-[10px] uppercase font-semibold text-teal-700 dark:text-teal-300">
              DECISION 500/QĐ-TTG &middot; RESOLUTION 55-NQ/TW &middot; NET-ZERO 2050 PATHWAY
            </span>
          </div>
          <h2 class="text-base sm:text-lg font-bold tracking-tight text-slate-900 dark:text-slate-100">
            The 12 Strategic Pillars of Vietnam's National Energy Transition
          </h2>
          <p class="text-xs text-slate-500 dark:text-slate-400 max-w-4xl leading-relaxed">
            Statutory framework orchestrating utility-scale generation expansion, ultra-high-voltage transmission corridors, competitive wholesale power markets, and green hydrogen power-to-X infrastructure across $134.7B in capital allocation through 2030. Click any pillar to inspect telemetry and direct gateway.
          </p>
        </div>

        <!-- Pillar Dimension Filter Toolbar -->
        <div class="flex flex-wrap items-center gap-1.5 font-mono text-[11px] shrink-0">
          <button onclick="filterHomepagePillars('ALL')" id="hpFilterAll" class="px-2.5 py-1.5 rounded-lg bg-teal-600 text-white font-semibold transition-all cursor-pointer shadow-xs">
            All Pillars (12)
          </button>
          <button onclick="filterHomepagePillars('GENERATION')" id="hpFilterGen" class="px-2.5 py-1.5 rounded-lg bg-slate-100 dark:bg-slate-700/60 hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-600 dark:text-slate-300 transition-all cursor-pointer">
            Generation (6)
          </button>
          <button onclick="filterHomepagePillars('GRID')" id="hpFilterGrid" class="px-2.5 py-1.5 rounded-lg bg-slate-100 dark:bg-slate-700/60 hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-600 dark:text-slate-300 transition-all cursor-pointer">
            Grid &amp; Supergrid (3)
          </button>
          <button onclick="filterHomepagePillars('MARKET')" id="hpFilterMarket" class="px-2.5 py-1.5 rounded-lg bg-slate-100 dark:bg-slate-700/60 hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-600 dark:text-slate-300 transition-all cursor-pointer">
            Market &amp; Policy (3)
          </button>
        </div>
      </div>

      <!-- 12 Strategic Pillars Grid -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-3" id="homepagePillarsContainer">
        
        <!-- Pillar 01: Offshore Wind -->
        <div class="flow-node active-node pillar-card p-3.5 rounded-xl bg-slate-50/80 dark:bg-slate-800 border border-slate-200/70 dark:border-slate-700/70 cursor-pointer hover:border-teal-500/60 transition-all space-y-2" data-node="0" data-category="GENERATION">
          <div class="flex items-center justify-between font-mono text-[10px]">
            <span class="text-blue-700 dark:text-blue-300 font-semibold">PILLAR 01 &middot; GENERATION</span>
            <span class="text-slate-400 font-medium">$18.5B Capex</span>
          </div>
          <strong class="block text-xs font-semibold text-slate-800 dark:text-slate-200">Offshore Wind Supergrid</strong>
          <span class="block text-[11px] text-slate-500 dark:text-slate-400 leading-snug">Marine wind clusters in South Central &amp; Northern Gulf of Tonkin.</span>
          <div class="space-y-1 font-mono text-[10px] pt-1.5 border-t border-slate-200/50 dark:border-slate-700/50">
            <div class="flex justify-between text-slate-600 dark:text-slate-300">
              <span>Target 2030:</span>
              <strong class="text-slate-900 dark:text-slate-100">6,000 MW</strong>
            </div>
            <div class="w-full bg-slate-200 dark:bg-slate-700 h-1.5 rounded-full overflow-hidden">
              <div class="bg-blue-500 h-full rounded-full" style="width: 5%"></div>
            </div>
          </div>
        </div>

        <!-- Pillar 02: Onshore & Nearshore Wind -->
        <div class="flow-node pillar-card p-3.5 rounded-xl bg-slate-50/80 dark:bg-slate-800 border border-slate-200/70 dark:border-slate-700/70 cursor-pointer hover:border-teal-500/60 transition-all space-y-2" data-node="1" data-category="GENERATION">
          <div class="flex items-center justify-between font-mono text-[10px]">
            <span class="text-teal-700 dark:text-teal-300 font-semibold">PILLAR 02 &middot; GENERATION</span>
            <span class="text-slate-400 font-medium">$26.2B Capex</span>
          </div>
          <strong class="block text-xs font-semibold text-slate-800 dark:text-slate-200">Onshore/Nearshore Wind</strong>
          <span class="block text-[11px] text-slate-500 dark:text-slate-400 leading-snug">High-resource corridors in Central Highlands and Mekong Delta.</span>
          <div class="space-y-1 font-mono text-[10px] pt-1.5 border-t border-slate-200/50 dark:border-slate-700/50">
            <div class="flex justify-between text-slate-600 dark:text-slate-300">
              <span>Target 2030:</span>
              <strong class="text-teal-600 dark:text-teal-400">21,880 MW (4,798 MW COD)</strong>
            </div>
            <div class="w-full bg-slate-200 dark:bg-slate-700 h-1.5 rounded-full overflow-hidden">
              <div class="bg-teal-500 h-full rounded-full" style="width: 22%"></div>
            </div>
          </div>
        </div>

        <!-- Pillar 03: Solar PV & Rooftop RTS -->
        <div class="flow-node pillar-card p-3.5 rounded-xl bg-slate-50/80 dark:bg-slate-800 border border-slate-200/70 dark:border-slate-700/70 cursor-pointer hover:border-teal-500/60 transition-all space-y-2" data-node="2" data-category="GENERATION">
          <div class="flex items-center justify-between font-mono text-[10px]">
            <span class="text-amber-700 dark:text-amber-300 font-semibold">PILLAR 03 &middot; GENERATION</span>
            <span class="text-slate-400 font-medium">$14.1B Capex</span>
          </div>
          <strong class="block text-xs font-semibold text-slate-800 dark:text-slate-200">Solar PV &amp; Rooftop RTS</strong>
          <span class="block text-[11px] text-slate-500 dark:text-slate-400 leading-snug">Utility ground-mount and 50% rooftop self-consumption (Decree 135).</span>
          <div class="space-y-1 font-mono text-[10px] pt-1.5 border-t border-slate-200/50 dark:border-slate-700/50">
            <div class="flex justify-between text-slate-600 dark:text-slate-300">
              <span>Installed:</span>
              <strong class="text-amber-600 dark:text-amber-400">16,500+ MW</strong>
            </div>
            <div class="w-full bg-slate-200 dark:bg-slate-700 h-1.5 rounded-full overflow-hidden">
              <div class="bg-amber-500 h-full rounded-full" style="width: 85%"></div>
            </div>
          </div>
        </div>

        <!-- Pillar 04: Flexible Hydro & Storage -->
        <div class="flow-node pillar-card p-3.5 rounded-xl bg-slate-50/80 dark:bg-slate-800 border border-slate-200/70 dark:border-slate-700/70 cursor-pointer hover:border-teal-500/60 transition-all space-y-2" data-node="3" data-category="GENERATION">
          <div class="flex items-center justify-between font-mono text-[10px]">
            <span class="text-cyan-700 dark:text-cyan-300 font-semibold">PILLAR 04 &middot; GENERATION</span>
            <span class="text-slate-400 font-medium">$11.8B Capex</span>
          </div>
          <strong class="block text-xs font-semibold text-slate-800 dark:text-slate-200">Flexible Hydro &amp; BESS</strong>
          <span class="block text-[11px] text-slate-500 dark:text-slate-400 leading-snug">Cascade reservoir dispatch + 2,400 MW Pumped Hydro (Bác Ái) &amp; BESS.</span>
          <div class="space-y-1 font-mono text-[10px] pt-1.5 border-t border-slate-200/50 dark:border-slate-700/50">
            <div class="flex justify-between text-slate-600 dark:text-slate-300">
              <span>Baseload + Storage:</span>
              <strong class="text-cyan-600 dark:text-cyan-400">29,346 MW + 2.7 GW</strong>
            </div>
            <div class="w-full bg-slate-200 dark:bg-slate-700 h-1.5 rounded-full overflow-hidden">
              <div class="bg-cyan-500 h-full rounded-full" style="width: 78%"></div>
            </div>
          </div>
        </div>

        <!-- Pillar 05: Domestic Gas & LNG -->
        <div class="flow-node pillar-card p-3.5 rounded-xl bg-slate-50/80 dark:bg-slate-800 border border-slate-200/70 dark:border-slate-700/70 cursor-pointer hover:border-teal-500/60 transition-all space-y-2" data-node="4" data-category="GENERATION">
          <div class="flex items-center justify-between font-mono text-[10px]">
            <span class="text-indigo-700 dark:text-indigo-300 font-semibold">PILLAR 05 &middot; GENERATION</span>
            <span class="text-slate-400 font-medium">$31.4B Capex</span>
          </div>
          <strong class="block text-xs font-semibold text-slate-800 dark:text-slate-200">Domestic Gas &amp; LNG Terminals</strong>
          <span class="block text-[11px] text-slate-500 dark:text-slate-400 leading-snug">Baseload firming via Block B upstream gas &amp; 13 world-scale LNG ports.</span>
          <div class="space-y-1 font-mono text-[10px] pt-1.5 border-t border-slate-200/50 dark:border-slate-700/50">
            <div class="flex justify-between text-slate-600 dark:text-slate-300">
              <span>Target 2030:</span>
              <strong class="text-indigo-600 dark:text-indigo-400">37,330 MW Gas/LNG</strong>
            </div>
            <div class="w-full bg-slate-200 dark:bg-slate-700 h-1.5 rounded-full overflow-hidden">
              <div class="bg-indigo-500 h-full rounded-full" style="width: 25%"></div>
            </div>
          </div>
        </div>

        <!-- Pillar 06: Biomass & Waste-to-Energy -->
        <div class="flow-node pillar-card p-3.5 rounded-xl bg-slate-50/80 dark:bg-slate-800 border border-slate-200/70 dark:border-slate-700/70 cursor-pointer hover:border-teal-500/60 transition-all space-y-2" data-node="5" data-category="GENERATION">
          <div class="flex items-center justify-between font-mono text-[10px]">
            <span class="text-emerald-700 dark:text-emerald-300 font-semibold">PILLAR 06 &middot; GENERATION</span>
            <span class="text-slate-400 font-medium">$3.6B Capex</span>
          </div>
          <strong class="block text-xs font-semibold text-slate-800 dark:text-slate-200">Biomass &amp; Waste-to-Energy</strong>
          <span class="block text-[11px] text-slate-500 dark:text-slate-400 leading-snug">Converting agricultural residues and municipal waste into clean power.</span>
          <div class="space-y-1 font-mono text-[10px] pt-1.5 border-t border-slate-200/50 dark:border-slate-700/50">
            <div class="flex justify-between text-slate-600 dark:text-slate-300">
              <span>Target 2030:</span>
              <strong class="text-emerald-600 dark:text-emerald-400">2,270 MW</strong>
            </div>
            <div class="w-full bg-slate-200 dark:bg-slate-700 h-1.5 rounded-full overflow-hidden">
              <div class="bg-emerald-500 h-full rounded-full" style="width: 28%"></div>
            </div>
          </div>
        </div>

        <!-- Pillar 07: 500kV Supergrid Spine -->
        <div class="flow-node pillar-card p-3.5 rounded-xl bg-slate-50/80 dark:bg-slate-800 border border-slate-200/70 dark:border-slate-700/70 cursor-pointer hover:border-teal-500/60 transition-all space-y-2" data-node="6" data-category="GRID">
          <div class="flex items-center justify-between font-mono text-[10px]">
            <span class="text-rose-700 dark:text-rose-300 font-semibold">PILLAR 07 &middot; SUPERGRID</span>
            <span class="text-slate-400 font-medium">$14.9B Capex</span>
          </div>
          <strong class="block text-xs font-semibold text-slate-800 dark:text-slate-200">500kV Supergrid Backbone Spine</strong>
          <span class="block text-[11px] text-slate-500 dark:text-slate-400 leading-snug">15,888 km circuits, Circuit-3 Quảng Trạch &ndash; Phố Nối 519 km.</span>
          <div class="space-y-1 font-mono text-[10px] pt-1.5 border-t border-slate-200/50 dark:border-slate-700/50">
            <div class="flex justify-between text-slate-600 dark:text-slate-300">
              <span>Wheeling Capacity:</span>
              <strong class="text-rose-600 dark:text-rose-400">5,000 MW Northward</strong>
            </div>
            <div class="w-full bg-slate-200 dark:bg-slate-700 h-1.5 rounded-full overflow-hidden">
              <div class="bg-rose-500 h-full rounded-full" style="width: 100%"></div>
            </div>
          </div>
        </div>

        <!-- Pillar 08: ASEAN Grid Interties -->
        <div class="flow-node pillar-card p-3.5 rounded-xl bg-slate-50/80 dark:bg-slate-800 border border-slate-200/70 dark:border-slate-700/70 cursor-pointer hover:border-teal-500/60 transition-all space-y-2" data-node="7" data-category="GRID">
          <div class="flex items-center justify-between font-mono text-[10px]">
            <span class="text-violet-700 dark:text-violet-300 font-semibold">PILLAR 08 &middot; SUPERGRID</span>
            <span class="text-slate-400 font-medium">$4.2B Capex</span>
          </div>
          <strong class="block text-xs font-semibold text-slate-800 dark:text-slate-200">Cross-Border ASEAN Grid</strong>
          <span class="block text-[11px] text-slate-500 dark:text-slate-400 leading-snug">Monsoon 500kV Lao import and planned subsea HVDC link to Singapore.</span>
          <div class="space-y-1 font-mono text-[10px] pt-1.5 border-t border-slate-200/50 dark:border-slate-700/50">
            <div class="flex justify-between text-slate-600 dark:text-slate-300">
              <span>Lao Clean Import:</span>
              <strong class="text-violet-600 dark:text-violet-400">5,000 - 8,000 MW</strong>
            </div>
            <div class="w-full bg-slate-200 dark:bg-slate-700 h-1.5 rounded-full overflow-hidden">
              <div class="bg-violet-500 h-full rounded-full" style="width: 35%"></div>
            </div>
          </div>
        </div>

        <!-- Pillar 09: Smart Grid Automation -->
        <div class="flow-node pillar-card p-3.5 rounded-xl bg-slate-50/80 dark:bg-slate-800 border border-slate-200/70 dark:border-slate-700/70 cursor-pointer hover:border-teal-500/60 transition-all space-y-2" data-node="8" data-category="GRID">
          <div class="flex items-center justify-between font-mono text-[10px]">
            <span class="text-fuchsia-700 dark:text-fuchsia-300 font-semibold">PILLAR 09 &middot; SUPERGRID</span>
            <span class="text-slate-400 font-medium">$3.8B Capex</span>
          </div>
          <strong class="block text-xs font-semibold text-slate-800 dark:text-slate-200">Smart Grid SCADA &amp; Automation</strong>
          <span class="block text-[11px] text-slate-500 dark:text-slate-400 leading-snug">100% digital substations IEC 61850 &amp; 2,000 MW Demand-Side Response.</span>
          <div class="space-y-1 font-mono text-[10px] pt-1.5 border-t border-slate-200/50 dark:border-slate-700/50">
            <div class="flex justify-between text-slate-600 dark:text-slate-300">
              <span>Digital Automation:</span>
              <strong class="text-fuchsia-600 dark:text-fuchsia-400">1,915 Unmanned TBA</strong>
            </div>
            <div class="w-full bg-slate-200 dark:bg-slate-700 h-1.5 rounded-full overflow-hidden">
              <div class="bg-fuchsia-500 h-full rounded-full" style="width: 65%"></div>
            </div>
          </div>
        </div>

        <!-- Pillar 10: DPPA Wheeling Mechanism -->
        <div class="flow-node pillar-card p-3.5 rounded-xl bg-slate-50/80 dark:bg-slate-800 border border-slate-200/70 dark:border-slate-700/70 cursor-pointer hover:border-teal-500/60 transition-all space-y-2" data-node="9" data-category="MARKET">
          <div class="flex items-center justify-between font-mono text-[10px]">
            <span class="text-emerald-700 dark:text-emerald-300 font-semibold">PILLAR 10 &middot; MARKET</span>
            <span class="text-slate-400 font-medium">Private Wheeling</span>
          </div>
          <strong class="block text-xs font-semibold text-slate-800 dark:text-slate-200">Direct PPA (DPPA Mechanism)</strong>
          <span class="block text-[11px] text-slate-500 dark:text-slate-400 leading-snug">Decree 80/2024 private wire and national grid CfD wheeling for RE100.</span>
          <div class="space-y-1 font-mono text-[10px] pt-1.5 border-t border-slate-200/50 dark:border-slate-700/50">
            <div class="flex justify-between text-slate-600 dark:text-slate-300">
              <span>Statutory Basis:</span>
              <strong class="text-emerald-600 dark:text-emerald-400">Decree 80/2024/NĐ-CP</strong>
            </div>
            <div class="w-full bg-slate-200 dark:bg-slate-700 h-1.5 rounded-full overflow-hidden">
              <div class="bg-emerald-500 h-full rounded-full" style="width: 90%"></div>
            </div>
          </div>
        </div>

        <!-- Pillar 11: Competitive Electricity Market (VWEM/VREM) -->
        <div class="flow-node pillar-card p-3.5 rounded-xl bg-slate-50/80 dark:bg-slate-800 border border-slate-200/70 dark:border-slate-700/70 cursor-pointer hover:border-teal-500/60 transition-all space-y-2" data-node="10" data-category="MARKET">
          <div class="flex items-center justify-between font-mono text-[10px]">
            <span class="text-amber-700 dark:text-amber-300 font-semibold">PILLAR 11 &middot; MARKET</span>
            <span class="text-slate-400 font-medium">Spot Clearing</span>
          </div>
          <strong class="block text-xs font-semibold text-slate-800 dark:text-slate-200">Wholesale Market (VWEM/VREM)</strong>
          <span class="block text-[11px] text-slate-500 dark:text-slate-400 leading-snug">Spot market clearing (SMP + CAN) and roadmap to competitive retail choice.</span>
          <div class="space-y-1 font-mono text-[10px] pt-1.5 border-t border-slate-200/50 dark:border-slate-700/50">
            <div class="flex justify-between text-slate-600 dark:text-slate-300">
              <span>Full Market Clearing:</span>
              <strong class="text-amber-600 dark:text-amber-400">SMP + CAN (~$0.073)</strong>
            </div>
            <div class="w-full bg-slate-200 dark:bg-slate-700 h-1.5 rounded-full overflow-hidden">
              <div class="bg-amber-500 h-full rounded-full" style="width: 70%"></div>
            </div>
          </div>
        </div>

        <!-- Pillar 12: Green Hydrogen & Power-to-X -->
        <div class="flow-node pillar-card p-3.5 rounded-xl bg-slate-50/80 dark:bg-slate-800 border border-slate-200/70 dark:border-slate-700/70 cursor-pointer hover:border-teal-500/60 transition-all space-y-2" data-node="11" data-category="MARKET">
          <div class="flex items-center justify-between font-mono text-[10px]">
            <span class="text-teal-700 dark:text-teal-300 font-semibold">PILLAR 12 &middot; NET-ZERO</span>
            <span class="text-slate-400 font-medium">$6.2B Capex</span>
          </div>
          <strong class="block text-xs font-semibold text-slate-800 dark:text-slate-200">Green Hydrogen &amp; Power-to-X</strong>
          <span class="block text-[11px] text-slate-500 dark:text-slate-400 leading-snug">Green hydrogen, ammonia co-firing, green steel, and maritime exports.</span>
          <div class="space-y-1 font-mono text-[10px] pt-1.5 border-t border-slate-200/50 dark:border-slate-700/50">
            <div class="flex justify-between text-slate-600 dark:text-slate-300">
              <span>Target 2030:</span>
              <strong class="text-teal-600 dark:text-teal-400">100k - 500k t/yr</strong>
            </div>
            <div class="w-full bg-slate-200 dark:bg-slate-700 h-1.5 rounded-full overflow-hidden">
              <div class="bg-teal-500 h-full rounded-full" style="width: 15%"></div>
            </div>
          </div>
        </div>

      </div>

      <!-- Real-Time Node Inspector Drawer (Syncs with all 12 pillars) -->
      <div id="nodeInspectorPanel" class="p-4 sm:p-4.5 rounded-xl bg-slate-50/90 dark:bg-slate-800/60 border border-slate-200/70 dark:border-slate-700/60 transition-all flex flex-col md:flex-row md:items-center justify-between gap-3 shadow-xs">
        <div class="space-y-1">
          <div class="flex items-center gap-2">
            <span id="inspectorBadge" class="font-mono text-[9px] uppercase font-semibold text-blue-700 dark:text-blue-300 bg-blue-100 dark:bg-blue-900/40 px-2 py-0.5 rounded border border-blue-200 dark:border-blue-800/40">
              PILLAR 01 &middot; CLEAN GENERATION
            </span>
            <span id="inspectorStatute" class="font-mono text-[10px] text-slate-500 dark:text-slate-400">
              Statutory Basis: Decision 500/QĐ-TTg &middot; Marine Spatial Plan
            </span>
          </div>
          <h3 id="inspectorTitle" class="text-sm sm:text-base font-bold text-slate-800 dark:text-slate-100">
            Offshore Wind Supergrid &amp; Marine Spatial Corridors
          </h3>
          <p id="inspectorDesc" class="text-xs text-slate-600 dark:text-slate-400 max-w-3xl leading-relaxed">
            Deployment of utility-scale marine wind clusters across South Central Vietnam (Bình Thuận, Ninh Thuận) and Northern Gulf of Tonkin to anchor baseload green power.
          </p>
        </div>

        <div class="flex items-center gap-3 shrink-0">
          <div class="text-right font-mono text-[11px] pr-2">
            <span class="block text-slate-500 dark:text-slate-400 text-[10px]">2030 Mandate</span>
            <strong id="inspectorMetric" class="text-slate-900 dark:text-slate-100 text-xs sm:text-sm font-bold">6,000 MW Target ($18.5B)</strong>
          </div>
          <a id="inspectorLaunchBtn" href="https://energy.renewablevietnam.com/" class="px-3.5 py-2 rounded-lg bg-teal-600 hover:bg-teal-500 text-white font-mono text-xs font-semibold shadow-xs transition-all flex items-center gap-1.5">
            <span>Launch Gateway</span>
            <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 19.5l15-15m0 0H8.25m11.25 0v11.25"/></svg>
          </a>
        </div>
      </div>
    </section>"""

    # Replace Section 1
    old_section_1_pattern = r'<!-- SECTION 1: INTERACTIVE ENERGY NETWORK TOPOLOGY GRAPH[\s\S]*?<\/section>'
    assert re.search(old_section_1_pattern, html), "Failed to find Section 1 in source HTML"
    html = re.sub(old_section_1_pattern, pillars_section_html, html, count=1)

    # Replace nodeDetails array with 12 Pillars data
    new_node_details_js = """    // The 12 Strategic Pillars of Vietnam Energy Transition Data
    const nodeDetails = [
      {
        badge: "PILLAR 01 &middot; CLEAN GENERATION",
        statute: "Statutory Basis: Decision 500/QĐ-TTg &middot; Marine Spatial Plan",
        title: "Offshore Wind Supergrid & Marine Spatial Corridors",
        desc: "Deployment of utility-scale marine wind clusters across South Central Vietnam (Bình Thuận, Ninh Thuận) and Northern Gulf of Tonkin to anchor baseload green power.",
        metric: "6,000 MW ($18.5B)",
        url: "https://energy.renewablevietnam.com/"
      },
      {
        badge: "PILLAR 02 &middot; CLEAN GENERATION",
        statute: "Statutory Basis: Decision 500/QĐ-TTg Table 1",
        title: "Onshore & Nearshore Wind Resource Corridors",
        desc: "Accelerated wind development across Central Highlands (Gia Lai, Đắk Lắk) and Mekong Delta coastline (Bạc Liêu, Sóc Trăng, Bến Tre, Trà Vinh).",
        metric: "21,880 MW ($26.2B)",
        url: "https://energy.renewablevietnam.com/"
      },
      {
        badge: "PILLAR 03 &middot; CLEAN GENERATION",
        statute: "Statutory Basis: Decree 135/2024/NĐ-CP (Self-Consumption)",
        title: "Utility Solar PV & Distributed Rooftop (RTS)",
        desc: "Consolidating centralized solar farms with nationwide self-consumption rooftop solar for 50% of residential and office structures, paired with industrial park net-metering.",
        metric: "12,836 MW + RTS ($14.1B)",
        url: "https://industrial.renewablevietnam.com/"
      },
      {
        badge: "PILLAR 04 &middot; CLEAN GENERATION",
        statute: "Statutory Basis: Decision 500/QĐ-TTg & Pumped Storage Roadmap",
        title: "Flexible Cascade Hydro, Pumped Storage & BESS",
        desc: "Maximizing multi-purpose cascade hydro paired with utility pumped hydro (Bác Ái 1,200 MW, Đơn Dương) and 300 MW grid-scale battery energy storage systems (BESS).",
        metric: "29,346 MW + 2.7 GW ($11.8B)",
        url: "https://energy.renewablevietnam.com/"
      },
      {
        badge: "PILLAR 05 &middot; TRANSITION FUEL",
        statute: "Statutory Basis: National LNG Terminal Master Plan",
        title: "Domestic Natural Gas & Transition LNG Terminals",
        desc: "Bridging baseload reliability via Block B Ô Môn, Cá Voi Xanh upstream gas, and 13 world-scale LNG receiving terminals including Thị Vải, Sơn Mỹ, Hải Lăng, and Hiệp Phước.",
        metric: "37,330 MW Gas/LNG ($31.4B)",
        url: "https://legal.renewablevietnam.com/"
      },
      {
        badge: "PILLAR 06 &middot; CIRCULAR ENERGY",
        statute: "Statutory Basis: Circular Economy & Waste Management Directives",
        title: "Biomass, Waste-to-Energy & Industrial Cogeneration",
        desc: "Converting agricultural residues (rice husk, wood pellets, bagasse) and municipal solid waste into continuous, low-carbon baseload power for industrial decarbonization.",
        metric: "2,270 MW ($3.6B)",
        url: "https://industrial.renewablevietnam.com/"
      },
      {
        badge: "PILLAR 07 &middot; SUPERGRID INFRASTRUCTURE",
        statute: "Statutory Basis: National Key Project (Circuit-3 COD 2024)",
        title: "500kV Supergrid Backbone Spine & Wheeling",
        desc: "Tripling North-South transfer capacity via 500kV Circuit-3 (Quảng Trạch – Phố Nối 519 km across 4 projects), relieving Central-to-North transmission bottlenecks.",
        metric: "15,888 km (5,000 MW Wheel)",
        url: "https://energy.renewablevietnam.com/"
      },
      {
        badge: "PILLAR 08 &middot; SUPERGRID INFRASTRUCTURE",
        statute: "Statutory Basis: Vietnam-Laos Energy Cooperation Agreement",
        title: "Cross-Border ASEAN Power Grid Interconnections",
        desc: "Integrating Lao PDR cross-border clean energy imports (Monsoon Wind 600 MW via 500kV Thạnh Mỹ) and planned subsea HVDC power export interconnection to Singapore.",
        metric: "5,000 - 8,000 MW Import",
        url: "https://energy.renewablevietnam.com/"
      },
      {
        badge: "PILLAR 09 &middot; SUPERGRID INFRASTRUCTURE",
        statute: "Statutory Basis: Prime Minister Decision 1670/QĐ-TTg",
        title: "Smart Grid Automation, SCADA/EMS & Digital Substations",
        desc: "Digitalizing all 1,915 substations to IEC 61850 standards, enabling Dynamic Line Rating (DLR), automated AGC dispatch, and 2,000 MW Demand-Side Response (DSM).",
        metric: "100% Unmanned TBA ($3.8B)",
        url: "https://energy.renewablevietnam.com/"
      },
      {
        badge: "PILLAR 10 &middot; MARKET MECHANISMS",
        statute: "Statutory Basis: Decree 80/2024/NĐ-CP (Enacted July 3, 2024)",
        title: "Direct Power Purchase Agreement (DPPA Mechanism)",
        desc: "Statutory private power wheeling allowing multinational industrial clients (RE100) to contract clean electricity directly via private wire or national grid CfD wheeling.",
        metric: "Decree 80 Direct Wheeling",
        url: "https://industrial.renewablevietnam.com/"
      },
      {
        badge: "PILLAR 11 &middot; MARKET MECHANISMS",
        statute: "Statutory Basis: Amended Electricity Law 2024 & ERAV Circulars",
        title: "Competitive Wholesale & Retail Electricity Market (VWEM/VREM)",
        desc: "Maturation of the Vietnam Wholesale Electricity Market (VWEM) with nodal spot market clearing prices (SMP + CAN) and roadmap toward full retail choice (VREM).",
        metric: "SMP + CAN (~$0.073/kWh)",
        url: "https://legal.renewablevietnam.com/"
      },
      {
        badge: "PILLAR 12 &middot; NET-ZERO TECHNOLOGY",
        statute: "Statutory Basis: Decision 165/QĐ-TTg (Hydrogen Strategy)",
        title: "Green Hydrogen, Ammonia & Power-to-X Infrastructure",
        desc: "Establishing green hydrogen & green ammonia production hubs in South Central Vietnam to decarbonize coal co-firing, green steel, and international marine transport.",
        metric: "100k - 500k tons/yr ($6.2B)",
        url: "https://legal.renewablevietnam.com/"
      }
    ];

    function filterHomepagePillars(category) {
      const cards = document.querySelectorAll('.pillar-card');
      const buttons = {
        'ALL': document.getElementById('hpFilterAll'),
        'GENERATION': document.getElementById('hpFilterGen'),
        'GRID': document.getElementById('hpFilterGrid'),
        'MARKET': document.getElementById('hpFilterMarket')
      };

      Object.keys(buttons).forEach(k => {
        const btn = buttons[k];
        if (!btn) return;
        if (k === category) {
          btn.className = 'px-2.5 py-1.5 rounded-lg bg-teal-600 text-white font-semibold transition-all cursor-pointer shadow-xs';
        } else {
          btn.className = 'px-2.5 py-1.5 rounded-lg bg-slate-100 dark:bg-slate-700/60 hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-600 dark:text-slate-300 transition-all cursor-pointer';
        }
      });

      cards.forEach(card => {
        if (category === 'ALL' || card.getAttribute('data-category') === category) {
          card.classList.remove('hidden');
        } else {
          card.classList.add('hidden');
        }
      });
    }"""

    old_node_details_pattern = r'// Node Inspector Data[\s\S]*?const nodeDetails = \[[\s\S]*?\];'
    assert re.search(old_node_details_pattern, html), "Failed to find old nodeDetails array"
    html = re.sub(old_node_details_pattern, new_node_details_js, html, count=1)

    with open(TARGET_REV, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Successfully generated {TARGET_REV} ({len(html)} bytes)")

if __name__ == "__main__":
    generate()
