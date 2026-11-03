#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate index_Rev.011.html:
Integrates the 3 requested institutional energy modules:
1. The 12 Strategic Pillars of Vietnam Energy Transition (#energy12PillarsSection)
   - 12 comprehensive cards across Generation, Grid/Interties, and Market/Decarbonization dimensions.
2. Transition Energy Flow & Dynamic Power Balance Workstation (#transitionFlowSection)
   - Interactive 2025 Baseline vs 2030 PDP8 vs 2050 Net-Zero dynamic flow diagram.
3. National Energy Situation & Wholesale Electricity Market Terminal (#energyMarketSection)
   - Supply-demand balance, regional reserve margins, wheeling loads, SMP spot ticker, CAN price, DPPA wheeling fees, and TOU tariffs.
"""

from pathlib import Path

SOURCE_HTML = Path(r"G:\My Drive\7. AI\RenewableVietNam\projectenergy\index_Rev.010.html")
TARGET_REV = Path(r"G:\My Drive\7. AI\RenewableVietNam\projectenergy\index_Rev.011.html")

def generate():
    with open(SOURCE_HTML, "r", encoding="utf-8") as f:
        html = f.read()

    # =========================================================================
    # MODULE 1: THE 12 STRATEGIC PILLARS OF VIETNAM ENERGY TRANSITION
    # =========================================================================
    pillars_section_html = """
    <!-- ==================================================================== -->
    <!-- MODULE 1: THE 12 STRATEGIC PILLARS OF VIETNAM ENERGY TRANSITION     -->
    <!-- ==================================================================== -->
    <section id="energy12PillarsSection" class="p-4 sm:p-5 lg:p-6 rounded-2xl bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder shadow-sm space-y-5">
      
      <!-- Section Header -->
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-borderSlate dark:border-darkBorder">
        <div class="space-y-1">
          <div class="flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-teal-500 animate-pulse"></span>
            <span class="font-mono text-[10px] sm:text-[11px] uppercase tracking-wider text-teal-600 dark:text-teal-400 font-semibold">
              DECISION 500/QĐ-TTg &middot; RESOLUTION 55-NQ/TW &middot; NET-ZERO 2050 PATHWAY
            </span>
          </div>
          <h2 class="text-xl sm:text-2xl font-bold tracking-tight text-inkPrimary dark:text-textDarkPrimary">
            The 12 Strategic Pillars of Vietnam's National Energy Transition
          </h2>
          <p class="text-xs text-inkMuted dark:text-textDarkMuted font-light max-w-4xl">
            Institutional master architecture orchestrating utility-scale generation expansion, ultra-high-voltage transmission corridors, competitive wholesale power markets, and green hydrogen power-to-X infrastructure across $134.7B in statutory capital requirements through 2030.
          </p>
        </div>

        <!-- Dimension Filter Toolbar -->
        <div class="flex flex-wrap items-center gap-1.5 font-mono text-[11px] shrink-0">
          <button onclick="filterPillars('ALL')" id="pillarFilterAll" class="px-2.5 py-1.5 rounded-lg bg-teal-600 text-white font-semibold transition-all cursor-pointer">
            All Pillars (12)
          </button>
          <button onclick="filterPillars('GENERATION')" id="pillarFilterGen" class="px-2.5 py-1.5 rounded-lg bg-slate-100 dark:bg-darkCard hover:bg-slate-200 dark:hover:bg-slate-800 text-inkMuted dark:text-textDarkMuted transition-all cursor-pointer">
            Generation (6)
          </button>
          <button onclick="filterPillars('GRID')" id="pillarFilterGrid" class="px-2.5 py-1.5 rounded-lg bg-slate-100 dark:bg-darkCard hover:bg-slate-200 dark:hover:bg-slate-800 text-inkMuted dark:text-textDarkMuted transition-all cursor-pointer">
            Grid &amp; Interties (3)
          </button>
          <button onclick="filterPillars('MARKET')" id="pillarFilterMarket" class="px-2.5 py-1.5 rounded-lg bg-slate-100 dark:bg-darkCard hover:bg-slate-200 dark:hover:bg-slate-800 text-inkMuted dark:text-textDarkMuted transition-all cursor-pointer">
            Market &amp; Policy (3)
          </button>
        </div>
      </div>

      <!-- 12 Strategic Pillars Grid -->
      <div id="pillarsGridContainer" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-3.5">
        
        <!-- Pillar 1: Offshore Wind -->
        <div class="pillar-card p-4 rounded-xl bg-slate-50/70 dark:bg-darkCard/60 border border-borderSlate dark:border-darkBorder hover:border-teal-500/60 transition-all space-y-2.5" data-category="GENERATION">
          <div class="flex items-center justify-between">
            <span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold uppercase bg-blue-500/10 text-blue-600 dark:text-blue-400 border border-blue-500/20">Pillar 01 &middot; Generation</span>
            <span class="text-[10px] font-mono font-semibold text-slate-400">$18.5B Est. Capex</span>
          </div>
          <h3 class="font-bold text-sm text-inkPrimary dark:text-textDarkPrimary">Offshore Wind Supergrid</h3>
          <p class="text-xs text-inkMuted dark:text-textDarkMuted leading-relaxed">
            Deployment of utility-scale marine wind clusters across South Central &amp; Northern Gulf of Tonkin to anchor baseload green power.
          </p>
          <div class="space-y-1 font-mono text-[11px] pt-1 border-t border-borderSlate/60 dark:border-darkBorder/60">
            <div class="flex justify-between text-slate-500 dark:text-slate-400">
              <span>Target 2030:</span>
              <strong class="text-inkPrimary dark:text-textDarkPrimary">6,000 MW</strong>
            </div>
            <div class="flex justify-between text-slate-500 dark:text-slate-400">
              <span>2050 Vision:</span>
              <strong class="text-blue-600 dark:text-blue-400">70,000 - 91,500 MW</strong>
            </div>
            <div class="w-full bg-slate-200 dark:bg-slate-800 h-1.5 rounded-full overflow-hidden mt-1.5">
              <div class="bg-blue-500 h-full rounded-full" style="width: 5%"></div>
            </div>
            <span class="text-[9px] text-slate-400 block pt-0.5">Statutory: Decision 500/QĐ-TTg, Marine Spatial Plan</span>
          </div>
        </div>

        <!-- Pillar 2: Onshore & Nearshore Wind -->
        <div class="pillar-card p-4 rounded-xl bg-slate-50/70 dark:bg-darkCard/60 border border-borderSlate dark:border-darkBorder hover:border-teal-500/60 transition-all space-y-2.5" data-category="GENERATION">
          <div class="flex items-center justify-between">
            <span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold uppercase bg-teal-500/10 text-teal-600 dark:text-teal-400 border border-teal-500/20">Pillar 02 &middot; Generation</span>
            <span class="text-[10px] font-mono font-semibold text-slate-400">$26.2B Est. Capex</span>
          </div>
          <h3 class="font-bold text-sm text-inkPrimary dark:text-textDarkPrimary">Onshore &amp; Nearshore Wind Corridors</h3>
          <p class="text-xs text-inkMuted dark:text-textDarkMuted leading-relaxed">
            Accelerated wind corridors in Central Highlands (Gia Lai, Đắk Lắk) and Mekong Delta coastline (Bạc Liêu, Sóc Trăng, Bến Tre).
          </p>
          <div class="space-y-1 font-mono text-[11px] pt-1 border-t border-borderSlate/60 dark:border-darkBorder/60">
            <div class="flex justify-between text-slate-500 dark:text-slate-400">
              <span>Target 2030:</span>
              <strong class="text-inkPrimary dark:text-textDarkPrimary">21,880 MW</strong>
            </div>
            <div class="flex justify-between text-slate-500 dark:text-slate-400">
              <span>Current COD:</span>
              <strong class="text-teal-600 dark:text-teal-400">4,798 MW (21.9%)</strong>
            </div>
            <div class="w-full bg-slate-200 dark:bg-slate-800 h-1.5 rounded-full overflow-hidden mt-1.5">
              <div class="bg-teal-500 h-full rounded-full" style="width: 22%"></div>
            </div>
            <span class="text-[9px] text-slate-400 block pt-0.5">Statutory: Decision 500/QĐ-TTg Table 1</span>
          </div>
        </div>

        <!-- Pillar 3: Solar PV & Rooftop Self-Consumption -->
        <div class="pillar-card p-4 rounded-xl bg-slate-50/70 dark:bg-darkCard/60 border border-borderSlate dark:border-darkBorder hover:border-teal-500/60 transition-all space-y-2.5" data-category="GENERATION">
          <div class="flex items-center justify-between">
            <span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold uppercase bg-amber-500/10 text-amber-600 dark:text-amber-400 border border-amber-500/20">Pillar 03 &middot; Generation</span>
            <span class="text-[10px] font-mono font-semibold text-slate-400">$14.1B Est. Capex</span>
          </div>
          <h3 class="font-bold text-sm text-inkPrimary dark:text-textDarkPrimary">Utility &amp; Rooftop Solar PV</h3>
          <p class="text-xs text-inkMuted dark:text-textDarkMuted leading-relaxed">
            Consolidating centralized solar farms with nationwide self-consumption rooftop solar for 50% of residential and office structures.
          </p>
          <div class="space-y-1 font-mono text-[11px] pt-1 border-t border-borderSlate/60 dark:border-darkBorder/60">
            <div class="flex justify-between text-slate-500 dark:text-slate-400">
              <span>Target 2030:</span>
              <strong class="text-inkPrimary dark:text-textDarkPrimary">12,836 MW + RTS</strong>
            </div>
            <div class="flex justify-between text-slate-500 dark:text-slate-400">
              <span>Operating Capacity:</span>
              <strong class="text-amber-600 dark:text-amber-400">16,500+ MW</strong>
            </div>
            <div class="w-full bg-slate-200 dark:bg-slate-800 h-1.5 rounded-full overflow-hidden mt-1.5">
              <div class="bg-amber-500 h-full rounded-full" style="width: 85%"></div>
            </div>
            <span class="text-[9px] text-slate-400 block pt-0.5">Statutory: Decree 135/2024/NĐ-CP (Self-Consumption)</span>
          </div>
        </div>

        <!-- Pillar 4: Flexible Hydro, Pumped Storage & BESS -->
        <div class="pillar-card p-4 rounded-xl bg-slate-50/70 dark:bg-darkCard/60 border border-borderSlate dark:border-darkBorder hover:border-teal-500/60 transition-all space-y-2.5" data-category="GENERATION">
          <div class="flex items-center justify-between">
            <span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold uppercase bg-cyan-500/10 text-cyan-600 dark:text-cyan-400 border border-cyan-500/20">Pillar 04 &middot; Generation</span>
            <span class="text-[10px] font-mono font-semibold text-slate-400">$11.8B Est. Capex</span>
          </div>
          <h3 class="font-bold text-sm text-inkPrimary dark:text-textDarkPrimary">Flexible Hydro, Pumped Storage &amp; BESS</h3>
          <p class="text-xs text-inkMuted dark:text-textDarkMuted leading-relaxed">
            Maximizing multi-purpose cascade hydro paired with utility pumped hydro (Bác Ái 1,200 MW, Đơn Dương) and 300 MW grid-scale BESS.
          </p>
          <div class="space-y-1 font-mono text-[11px] pt-1 border-t border-borderSlate/60 dark:border-darkBorder/60">
            <div class="flex justify-between text-slate-500 dark:text-slate-400">
              <span>Hydro Baseload:</span>
              <strong class="text-inkPrimary dark:text-textDarkPrimary">29,346 MW</strong>
            </div>
            <div class="flex justify-between text-slate-500 dark:text-slate-400">
              <span>Pumped + BESS:</span>
              <strong class="text-cyan-600 dark:text-cyan-400">2,700 MW by 2030</strong>
            </div>
            <div class="w-full bg-slate-200 dark:bg-slate-800 h-1.5 rounded-full overflow-hidden mt-1.5">
              <div class="bg-cyan-500 h-full rounded-full" style="width: 78%"></div>
            </div>
            <span class="text-[9px] text-slate-400 block pt-0.5">Statutory: Decision 500/QĐ-TTg, Pumped Storage Roadmap</span>
          </div>
        </div>

        <!-- Pillar 5: Domestic Natural Gas & Transition LNG -->
        <div class="pillar-card p-4 rounded-xl bg-slate-50/70 dark:bg-darkCard/60 border border-borderSlate dark:border-darkBorder hover:border-teal-500/60 transition-all space-y-2.5" data-category="GENERATION">
          <div class="flex items-center justify-between">
            <span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold uppercase bg-indigo-500/10 text-indigo-600 dark:text-indigo-400 border border-indigo-500/20">Pillar 05 &middot; Generation</span>
            <span class="text-[10px] font-mono font-semibold text-slate-400">$31.4B Est. Capex</span>
          </div>
          <h3 class="font-bold text-sm text-inkPrimary dark:text-textDarkPrimary">Domestic Gas &amp; Transition LNG Terminals</h3>
          <p class="text-xs text-inkMuted dark:text-textDarkMuted leading-relaxed">
            Bridging baseload reliability via Block B Ô Môn, Cá Voi Xanh upstream gas, and 13 world-scale LNG receiving terminals (Thị Vải, Sơn Mỹ).
          </p>
          <div class="space-y-1 font-mono text-[11px] pt-1 border-t border-borderSlate/60 dark:border-darkBorder/60">
            <div class="flex justify-between text-slate-500 dark:text-slate-400">
              <span>Domestic Gas Target:</span>
              <strong class="text-inkPrimary dark:text-textDarkPrimary">14,930 MW</strong>
            </div>
            <div class="flex justify-between text-slate-500 dark:text-slate-400">
              <span>Import LNG Target:</span>
              <strong class="text-indigo-600 dark:text-indigo-400">22,400 MW</strong>
            </div>
            <div class="w-full bg-slate-200 dark:bg-slate-800 h-1.5 rounded-full overflow-hidden mt-1.5">
              <div class="bg-indigo-500 h-full rounded-full" style="width: 25%"></div>
            </div>
            <span class="text-[9px] text-slate-400 block pt-0.5">Statutory: National LNG Terminal Master Plan</span>
          </div>
        </div>

        <!-- Pillar 6: Biomass, Waste-to-Energy & Cogeneration -->
        <div class="pillar-card p-4 rounded-xl bg-slate-50/70 dark:bg-darkCard/60 border border-borderSlate dark:border-darkBorder hover:border-teal-500/60 transition-all space-y-2.5" data-category="GENERATION">
          <div class="flex items-center justify-between">
            <span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold uppercase bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border border-emerald-500/20">Pillar 06 &middot; Generation</span>
            <span class="text-[10px] font-mono font-semibold text-slate-400">$3.6B Est. Capex</span>
          </div>
          <h3 class="font-bold text-sm text-inkPrimary dark:text-textDarkPrimary">Biomass, Waste-to-Energy &amp; Cogen</h3>
          <p class="text-xs text-inkMuted dark:text-textDarkMuted leading-relaxed">
            Converting agricultural residues (rice husk, wood pellets, bagasse) and municipal solid waste into continuous, low-carbon baseload power.
          </p>
          <div class="space-y-1 font-mono text-[11px] pt-1 border-t border-borderSlate/60 dark:border-darkBorder/60">
            <div class="flex justify-between text-slate-500 dark:text-slate-400">
              <span>Target 2030:</span>
              <strong class="text-inkPrimary dark:text-textDarkPrimary">2,270 MW</strong>
            </div>
            <div class="flex justify-between text-slate-500 dark:text-slate-400">
              <span>2050 Potential:</span>
              <strong class="text-emerald-600 dark:text-emerald-400">6,015 MW</strong>
            </div>
            <div class="w-full bg-slate-200 dark:bg-slate-800 h-1.5 rounded-full overflow-hidden mt-1.5">
              <div class="bg-emerald-500 h-full rounded-full" style="width: 28%"></div>
            </div>
            <span class="text-[9px] text-slate-400 block pt-0.5">Statutory: Circular Economy &amp; Waste Management Directives</span>
          </div>
        </div>

        <!-- Pillar 7: 500kV North-South Supergrid Spine -->
        <div class="pillar-card p-4 rounded-xl bg-slate-50/70 dark:bg-darkCard/60 border border-borderSlate dark:border-darkBorder hover:border-rose-500/60 transition-all space-y-2.5" data-category="GRID">
          <div class="flex items-center justify-between">
            <span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold uppercase bg-rose-500/10 text-rose-600 dark:text-rose-400 border border-rose-500/20">Pillar 07 &middot; Supergrid</span>
            <span class="text-[10px] font-mono font-semibold text-slate-400">$14.9B Est. Capex</span>
          </div>
          <h3 class="font-bold text-sm text-inkPrimary dark:text-textDarkPrimary">500kV Supergrid Backbone Spine</h3>
          <p class="text-xs text-inkMuted dark:text-textDarkMuted leading-relaxed">
            Tripling North-South transfer capacity via 500kV Circuit-3 (Quảng Trạch &ndash; Phố Nối 519 km), relieving Central-to-North transmission bottlenecks.
          </p>
          <div class="space-y-1 font-mono text-[11px] pt-1 border-t border-borderSlate/60 dark:border-darkBorder/60">
            <div class="flex justify-between text-slate-500 dark:text-slate-400">
              <span>Circuit Extent:</span>
              <strong class="text-inkPrimary dark:text-textDarkPrimary">15,888 km (180 Circuits)</strong>
            </div>
            <div class="flex justify-between text-slate-500 dark:text-slate-400">
              <span>Wheeling Capacity:</span>
              <strong class="text-rose-600 dark:text-rose-400">Up to 5,000 MW Northward</strong>
            </div>
            <div class="w-full bg-slate-200 dark:bg-slate-800 h-1.5 rounded-full overflow-hidden mt-1.5">
              <div class="bg-rose-500 h-full rounded-full" style="width: 100%"></div>
            </div>
            <span class="text-[9px] text-slate-400 block pt-0.5">Statutory: National Key Infrastructure Project (Circuit-3 COD 2024)</span>
          </div>
        </div>

        <!-- Pillar 8: Cross-Border ASEAN Grid Interconnections -->
        <div class="pillar-card p-4 rounded-xl bg-slate-50/70 dark:bg-darkCard/60 border border-borderSlate dark:border-darkBorder hover:border-rose-500/60 transition-all space-y-2.5" data-category="GRID">
          <div class="flex items-center justify-between">
            <span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold uppercase bg-violet-500/10 text-violet-600 dark:text-violet-400 border border-violet-500/20">Pillar 08 &middot; Supergrid</span>
            <span class="text-[10px] font-mono font-semibold text-slate-400">$4.2B Est. Capex</span>
          </div>
          <h3 class="font-bold text-sm text-inkPrimary dark:text-textDarkPrimary">Cross-Border ASEAN Grid Interties</h3>
          <p class="text-xs text-inkMuted dark:text-textDarkMuted leading-relaxed">
            Integrating Lao PDR cross-border clean energy imports (Monsoon Wind 600 MW via 500kV Thạnh Mỹ) and planned subsea HVDC export to Singapore.
          </p>
          <div class="space-y-1 font-mono text-[11px] pt-1 border-t border-borderSlate/60 dark:border-darkBorder/60">
            <div class="flex justify-between text-slate-500 dark:text-slate-400">
              <span>Lao Import Quota:</span>
              <strong class="text-inkPrimary dark:text-textDarkPrimary">5,000 - 8,000 MW</strong>
            </div>
            <div class="flex justify-between text-slate-500 dark:text-slate-400">
              <span>Subsea Export Vision:</span>
              <strong class="text-violet-600 dark:text-violet-400">1,200 MW to Singapore</strong>
            </div>
            <div class="w-full bg-slate-200 dark:bg-slate-800 h-1.5 rounded-full overflow-hidden mt-1.5">
              <div class="bg-violet-500 h-full rounded-full" style="width: 35%"></div>
            </div>
            <span class="text-[9px] text-slate-400 block pt-0.5">Statutory: Vietnam-Laos Energy Cooperation Agreement</span>
          </div>
        </div>

        <!-- Pillar 9: Smart Grid, SCADA/EMS & Digital Substations -->
        <div class="pillar-card p-4 rounded-xl bg-slate-50/70 dark:bg-darkCard/60 border border-borderSlate dark:border-darkBorder hover:border-rose-500/60 transition-all space-y-2.5" data-category="GRID">
          <div class="flex items-center justify-between">
            <span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold uppercase bg-fuchsia-500/10 text-fuchsia-600 dark:text-fuchsia-400 border border-fuchsia-500/20">Pillar 09 &middot; Supergrid</span>
            <span class="text-[10px] font-mono font-semibold text-slate-400">$3.8B Est. Capex</span>
          </div>
          <h3 class="font-bold text-sm text-inkPrimary dark:text-textDarkPrimary">Smart Grid Automation &amp; Digital SCADA</h3>
          <p class="text-xs text-inkMuted dark:text-textDarkMuted leading-relaxed">
            Digitalizing all 1,915 substations to IEC 61850 standards, enabling Dynamic Line Rating (DLR) and 2,000 MW Demand-Side Response (DSM).
          </p>
          <div class="space-y-1 font-mono text-[11px] pt-1 border-t border-borderSlate/60 dark:border-darkBorder/60">
            <div class="flex justify-between text-slate-500 dark:text-slate-400">
              <span>Digital Substations:</span>
              <strong class="text-inkPrimary dark:text-textDarkPrimary">100% Unmanned by 2030</strong>
            </div>
            <div class="flex justify-between text-slate-500 dark:text-slate-400">
              <span>DSM Flexibility:</span>
              <strong class="text-fuchsia-600 dark:text-fuchsia-400">2,000 MW Shaving</strong>
            </div>
            <div class="w-full bg-slate-200 dark:bg-slate-800 h-1.5 rounded-full overflow-hidden mt-1.5">
              <div class="bg-fuchsia-500 h-full rounded-full" style="width: 65%"></div>
            </div>
            <span class="text-[9px] text-slate-400 block pt-0.5">Statutory: Prime Minister Decision 1670/QĐ-TTg (Smart Grid)</span>
          </div>
        </div>

        <!-- Pillar 10: Direct Power Purchase Agreement (DPPA) -->
        <div class="pillar-card p-4 rounded-xl bg-slate-50/70 dark:bg-darkCard/60 border border-borderSlate dark:border-darkBorder hover:border-emerald-500/60 transition-all space-y-2.5" data-category="MARKET">
          <div class="flex items-center justify-between">
            <span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold uppercase bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border border-emerald-500/20">Pillar 10 &middot; Market Reform</span>
            <span class="text-[10px] font-mono font-semibold text-slate-400">Private Wheeling</span>
          </div>
          <h3 class="font-bold text-sm text-inkPrimary dark:text-textDarkPrimary">Direct Power Purchase Agreement (DPPA)</h3>
          <p class="text-xs text-inkMuted dark:text-textDarkMuted leading-relaxed">
            Statutory private power wheeling allowing multinational industrial clients (RE100) to contract clean electricity directly via private wire or grid CfD.
          </p>
          <div class="space-y-1 font-mono text-[11px] pt-1 border-t border-borderSlate/60 dark:border-darkBorder/60">
            <div class="flex justify-between text-slate-500 dark:text-slate-400">
              <span>Mechanisms:</span>
              <strong class="text-inkPrimary dark:text-textDarkPrimary">Direct Wire &amp; Grid-Connected</strong>
            </div>
            <div class="flex justify-between text-slate-500 dark:text-slate-400">
              <span>Eligibility:</span>
              <strong class="text-emerald-600 dark:text-emerald-400">&ge; 200,000 kWh/month</strong>
            </div>
            <div class="w-full bg-slate-200 dark:bg-slate-800 h-1.5 rounded-full overflow-hidden mt-1.5">
              <div class="bg-emerald-500 h-full rounded-full" style="width: 90%"></div>
            </div>
            <span class="text-[9px] text-slate-400 block pt-0.5">Statutory: Decree 80/2024/NĐ-CP (Enacted July 3, 2024)</span>
          </div>
        </div>

        <!-- Pillar 11: Competitive Wholesale & Retail Market (VWEM/VREM) -->
        <div class="pillar-card p-4 rounded-xl bg-slate-50/70 dark:bg-darkCard/60 border border-borderSlate dark:border-darkBorder hover:border-emerald-500/60 transition-all space-y-2.5" data-category="MARKET">
          <div class="flex items-center justify-between">
            <span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold uppercase bg-amber-500/10 text-amber-600 dark:text-amber-400 border border-amber-500/20">Pillar 11 &middot; Market Reform</span>
            <span class="text-[10px] font-mono font-semibold text-slate-400">Spot Clearing</span>
          </div>
          <h3 class="font-bold text-sm text-inkPrimary dark:text-textDarkPrimary">Competitive Power Market (VWEM / VREM)</h3>
          <p class="text-xs text-inkMuted dark:text-textDarkMuted leading-relaxed">
            Maturation of the Vietnam Wholesale Electricity Market (VWEM) with nodal clearing prices (SMP + CAN) and phased rollout of Retail Choice (VREM).
          </p>
          <div class="space-y-1 font-mono text-[11px] pt-1 border-t border-borderSlate/60 dark:border-darkBorder/60">
            <div class="flex justify-between text-slate-500 dark:text-slate-400">
              <span>Market Design:</span>
              <strong class="text-inkPrimary dark:text-textDarkPrimary">SMP + Capacity (CAN)</strong>
            </div>
            <div class="flex justify-between text-slate-500 dark:text-slate-400">
              <span>Retail Choice (VREM):</span>
              <strong class="text-amber-600 dark:text-amber-400">Target Full Rollout 2026+</strong>
            </div>
            <div class="w-full bg-slate-200 dark:bg-slate-800 h-1.5 rounded-full overflow-hidden mt-1.5">
              <div class="bg-amber-500 h-full rounded-full" style="width: 70%"></div>
            </div>
            <span class="text-[9px] text-slate-400 block pt-0.5">Statutory: Amended Electricity Law 2024, ERAV Circulars</span>
          </div>
        </div>

        <!-- Pillar 12: Green Hydrogen, Ammonia & Power-to-X -->
        <div class="pillar-card p-4 rounded-xl bg-slate-50/70 dark:bg-darkCard/60 border border-borderSlate dark:border-darkBorder hover:border-emerald-500/60 transition-all space-y-2.5" data-category="MARKET">
          <div class="flex items-center justify-between">
            <span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold uppercase bg-teal-500/10 text-teal-600 dark:text-teal-400 border border-teal-500/20">Pillar 12 &middot; Net-Zero Tech</span>
            <span class="text-[10px] font-mono font-semibold text-slate-400">$6.2B Est. Capex</span>
          </div>
          <h3 class="font-bold text-sm text-inkPrimary dark:text-textDarkPrimary">Green Hydrogen, Ammonia &amp; Power-to-X</h3>
          <p class="text-xs text-inkMuted dark:text-textDarkMuted leading-relaxed">
            Establishing green hydrogen &amp; green ammonia export hubs in South Central Vietnam to decarbonize coal co-firing, steel, and marine transport.
          </p>
          <div class="space-y-1 font-mono text-[11px] pt-1 border-t border-borderSlate/60 dark:border-darkBorder/60">
            <div class="flex justify-between text-slate-500 dark:text-slate-400">
              <span>Target 2030:</span>
              <strong class="text-inkPrimary dark:text-textDarkPrimary">100k - 500k tons/year</strong>
            </div>
            <div class="flex justify-between text-slate-500 dark:text-slate-400">
              <span>2050 Scale:</span>
              <strong class="text-teal-600 dark:text-teal-400">10 - 20 Million tons/yr</strong>
            </div>
            <div class="w-full bg-slate-200 dark:bg-slate-800 h-1.5 rounded-full overflow-hidden mt-1.5">
              <div class="bg-teal-500 h-full rounded-full" style="width: 15%"></div>
            </div>
            <span class="text-[9px] text-slate-400 block pt-0.5">Statutory: Decision 165/QĐ-TTg (Hydrogen Strategy)</span>
          </div>
        </div>

      </div>
    </section>
"""

    # =========================================================================
    # MODULE 2: TRANSITION ENERGY FLOW & DYNAMIC POWER BALANCE WORKSTATION
    # =========================================================================
    transition_flow_html = """
    <!-- ==================================================================== -->
    <!-- MODULE 2: TRANSITION ENERGY FLOW & DYNAMIC POWER BALANCE WORKSTATION -->
    <!-- ==================================================================== -->
    <section id="transitionFlowSection" class="p-4 sm:p-5 lg:p-6 rounded-2xl bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder shadow-sm space-y-5">
      
      <!-- Section Header -->
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-borderSlate dark:border-darkBorder">
        <div class="space-y-1">
          <div class="flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-rose-500 animate-pulse"></span>
            <span class="font-mono text-[10px] sm:text-[11px] uppercase tracking-wider text-rose-600 dark:text-rose-400 font-semibold">
              DYNAMIC ENERGY BALANCE MODEL &middot; PRIMARY GENERATION TO INDUSTRIAL SINK
            </span>
          </div>
          <h2 class="text-xl sm:text-2xl font-bold tracking-tight text-inkPrimary dark:text-textDarkPrimary">
            National Energy Transition Flow &amp; Power Balance Trajectory
          </h2>
          <p class="text-xs text-inkMuted dark:text-textDarkMuted font-light max-w-4xl">
            Simulated end-to-end power flow tracing primary energy supply transformation, transmission wheeling through the 500kV/220kV supergrid, and sectoral consumption sinks across Vietnam's phased decarbonization roadmap.
          </p>
        </div>

        <!-- Timeline Scenario Selector -->
        <div class="flex items-center gap-1 p-1 rounded-xl bg-slate-100 dark:bg-darkCard border border-borderSlate dark:border-darkBorder font-mono text-[11px] shrink-0">
          <button id="scenario2025Btn" onclick="switchTransitionScenario('2025')" class="px-3 py-1.5 rounded-lg bg-white dark:bg-darkSurface text-inkPrimary dark:text-white font-semibold shadow-xs transition-all cursor-pointer">
            2025 Baseline
          </button>
          <button id="scenario2030Btn" onclick="switchTransitionScenario('2030')" class="px-3 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-inkPrimary dark:hover:text-white transition-all cursor-pointer">
            2030 Mandate (PDP8)
          </button>
          <button id="scenario2050Btn" onclick="switchTransitionScenario('2050')" class="px-3 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-inkPrimary dark:hover:text-white transition-all cursor-pointer">
            2050 Net-Zero
          </button>
        </div>
      </div>

      <!-- Key Macro Indicators for Selected Scenario -->
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 font-mono">
        <div class="p-3 rounded-xl bg-slate-50 dark:bg-darkCard border border-borderSlate dark:border-darkBorder space-y-0.5">
          <span class="text-slate-400 text-[10px] uppercase">Annual Generation</span>
          <div id="flowMetricGen" class="text-base sm:text-lg font-bold text-inkPrimary dark:text-textDarkPrimary">280.5 TWh</div>
          <span class="text-[10px] text-teal-600 dark:text-teal-400 font-semibold" id="flowMetricGenDelta">+8.2% YoY growth</span>
        </div>
        <div class="p-3 rounded-xl bg-slate-50 dark:bg-darkCard border border-borderSlate dark:border-darkBorder space-y-0.5">
          <span class="text-slate-400 text-[10px] uppercase">Peak Demand (Pmax)</span>
          <div id="flowMetricPeak" class="text-base sm:text-lg font-bold text-inkPrimary dark:text-textDarkPrimary">48,500 MW</div>
          <span class="text-[10px] text-rose-600 dark:text-rose-400 font-semibold" id="flowMetricPeakSub">National High: May 2024</span>
        </div>
        <div class="p-3 rounded-xl bg-slate-50 dark:bg-darkCard border border-borderSlate dark:border-darkBorder space-y-0.5">
          <span class="text-slate-400 text-[10px] uppercase">Renewable Share</span>
          <div id="flowMetricReShare" class="text-base sm:text-lg font-bold text-teal-600 dark:text-teal-400">43.2%</div>
          <span class="text-[10px] text-slate-400" id="flowMetricReBreakdown">Hydro 29% + Solar/Wind 14%</span>
        </div>
        <div class="p-3 rounded-xl bg-slate-50 dark:bg-darkCard border border-borderSlate dark:border-darkBorder space-y-0.5">
          <span class="text-slate-400 text-[10px] uppercase">Grid Carbon Intensity</span>
          <div id="flowMetricCarbon" class="text-base sm:text-lg font-bold text-amber-600 dark:text-amber-400">0.68 tCO2/MWh</div>
          <span class="text-[10px] text-emerald-600 dark:text-emerald-400 font-semibold" id="flowMetricCarbonTarget">Target &le; 0.42 by 2030</span>
        </div>
      </div>

      <!-- Multi-Stage Flow Diagram Matrix -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-3.5 items-stretch font-mono text-xs">
        
        <!-- Stage 1: Primary Supply Vectors (4 cols) -->
        <div class="lg:col-span-4 p-4 rounded-xl bg-slate-50/70 dark:bg-darkCard/50 border border-borderSlate dark:border-darkBorder space-y-3">
          <div class="flex items-center justify-between pb-2 border-b border-borderSlate dark:border-darkBorder">
            <span class="text-slate-400 text-[10px] uppercase font-bold tracking-wider">Stage 1 &middot; Primary Generation</span>
            <span id="stage1TotalPill" class="px-2 py-0.5 rounded text-[10px] bg-slate-200 dark:bg-slate-800 font-bold">84,000 MW Installed</span>
          </div>
          
          <div class="space-y-2.5" id="flowSupplyStreams">
            <!-- Hydro -->
            <div class="space-y-1">
              <div class="flex justify-between text-[11px]">
                <span class="font-semibold text-cyan-600 dark:text-cyan-400">Hydropower (Run-of-River &amp; Reservoir)</span>
                <span id="hydroFlowVal" class="font-bold">23,500 MW (28.0%)</span>
              </div>
              <div class="w-full bg-slate-200 dark:bg-slate-800 h-2 rounded-full overflow-hidden">
                <div id="hydroFlowBar" class="bg-cyan-500 h-full rounded-full transition-all duration-500" style="width: 28%"></div>
              </div>
            </div>
            
            <!-- Coal Thermal -->
            <div class="space-y-1">
              <div class="flex justify-between text-[11px]">
                <span class="font-semibold text-slate-600 dark:text-slate-300">Coal Thermal (Phasing Down)</span>
                <span id="coalFlowVal" class="font-bold">26,800 MW (31.9%)</span>
              </div>
              <div class="w-full bg-slate-200 dark:bg-slate-800 h-2 rounded-full overflow-hidden">
                <div id="coalFlowBar" class="bg-slate-500 h-full rounded-full transition-all duration-500" style="width: 32%"></div>
              </div>
            </div>

            <!-- Gas & LNG -->
            <div class="space-y-1">
              <div class="flex justify-between text-[11px]">
                <span class="font-semibold text-indigo-600 dark:text-indigo-400">Domestic Gas &amp; Transition LNG</span>
                <span id="gasFlowVal" class="font-bold">7,200 MW (8.6%)</span>
              </div>
              <div class="w-full bg-slate-200 dark:bg-slate-800 h-2 rounded-full overflow-hidden">
                <div id="gasFlowBar" class="bg-indigo-500 h-full rounded-full transition-all duration-500" style="width: 9%"></div>
              </div>
            </div>

            <!-- Solar PV -->
            <div class="space-y-1">
              <div class="flex justify-between text-[11px]">
                <span class="font-semibold text-amber-600 dark:text-amber-400">Solar PV (Utility + Rooftop RTS)</span>
                <span id="solarFlowVal" class="font-bold">16,500 MW (19.6%)</span>
              </div>
              <div class="w-full bg-slate-200 dark:bg-slate-800 h-2 rounded-full overflow-hidden">
                <div id="solarFlowBar" class="bg-amber-500 h-full rounded-full transition-all duration-500" style="width: 20%"></div>
              </div>
            </div>

            <!-- Wind Corridors -->
            <div class="space-y-1">
              <div class="flex justify-between text-[11px]">
                <span class="font-semibold text-teal-600 dark:text-teal-400">Wind Corridors (Onshore/Offshore)</span>
                <span id="windFlowVal" class="font-bold">4,800 MW (5.7%)</span>
              </div>
              <div class="w-full bg-slate-200 dark:bg-slate-800 h-2 rounded-full overflow-hidden">
                <div id="windFlowBar" class="bg-teal-500 h-full rounded-full transition-all duration-500" style="width: 6%"></div>
              </div>
            </div>

            <!-- Biomass & Storage -->
            <div class="space-y-1">
              <div class="flex justify-between text-[11px]">
                <span class="font-semibold text-violet-600 dark:text-violet-400">Storage BESS, Imports &amp; Biomass</span>
                <span id="otherFlowVal" class="font-bold">5,200 MW (6.2%)</span>
              </div>
              <div class="w-full bg-slate-200 dark:bg-slate-800 h-2 rounded-full overflow-hidden">
                <div id="otherFlowBar" class="bg-violet-500 h-full rounded-full transition-all duration-500" style="width: 6%"></div>
              </div>
            </div>
          </div>
        </div>

        <!-- Stage 2: Transmission & Grid Conversion (4 cols) -->
        <div class="lg:col-span-4 p-4 rounded-xl bg-slate-50/70 dark:bg-darkCard/50 border border-borderSlate dark:border-darkBorder space-y-3 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-2 border-b border-borderSlate dark:border-darkBorder">
              <span class="text-slate-400 text-[10px] uppercase font-bold tracking-wider">Stage 2 &middot; Supergrid &amp; Wheeling</span>
              <span class="px-2 py-0.5 rounded text-[10px] bg-rose-500/10 text-rose-600 dark:text-rose-400 font-bold border border-rose-500/20">65,566 km Circuits</span>
            </div>

            <div class="space-y-3 mt-3">
              <div class="p-3 rounded-lg bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder space-y-1">
                <div class="flex justify-between text-[11px]">
                  <span class="text-slate-500 dark:text-slate-400">500kV Supergrid Spine Wheeling:</span>
                  <strong class="text-rose-600 dark:text-rose-400" id="flowSpineVal">~3,200 MW Peak (Central &rarr; North)</strong>
                </div>
                <p class="text-[10px] text-slate-400">
                  Transmitting renewable energy from Southern/Central surplus regions to industrial manufacturing clusters in Northern Vietnam.
                </p>
              </div>

              <div class="p-3 rounded-lg bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder space-y-1">
                <div class="flex justify-between text-[11px]">
                  <span class="text-slate-500 dark:text-slate-400">220kV Regional Interties:</span>
                  <strong class="text-amber-600 dark:text-amber-400">27,007 km (780 Circuits)</strong>
                </div>
                <p class="text-[10px] text-slate-400">
                  Regional inter-provincial pooling substations collecting utility solar, wind, and cascade hydropower.
                </p>
              </div>

              <div class="p-3 rounded-lg bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder space-y-1">
                <div class="flex justify-between text-[11px]">
                  <span class="text-slate-500 dark:text-slate-400">Transmission Losses &amp; Reserve:</span>
                  <strong class="text-slate-600 dark:text-slate-300" id="flowLossVal">6.25% Grid Loss</strong>
                </div>
                <p class="text-[10px] text-slate-400">
                  Technical loss optimized down from 7.5% through Circuit-3 500kV operation and automated VAR compensation.
                </p>
              </div>
            </div>
          </div>

          <div class="p-2.5 rounded-lg bg-teal-50 dark:bg-teal-950/30 border border-teal-200 dark:border-teal-800/40 text-[10px] text-teal-800 dark:text-teal-300">
            <strong>Direct Wheeling Protocol:</strong> High-voltage substations dynamically route green energy under Decree 80/2024 DPPA to subscribed industrial off-takers.
          </div>
        </div>

        <!-- Stage 3: End-Use Consumption Sinks (4 cols) -->
        <div class="lg:col-span-4 p-4 rounded-xl bg-slate-50/70 dark:bg-darkCard/50 border border-borderSlate dark:border-darkBorder space-y-3">
          <div class="flex items-center justify-between pb-2 border-b border-borderSlate dark:border-darkBorder">
            <span class="text-slate-400 text-[10px] uppercase font-bold tracking-wider">Stage 3 &middot; Sectoral Demand Sinks</span>
            <span id="stage3TotalPill" class="px-2 py-0.5 rounded text-[10px] bg-slate-200 dark:bg-slate-800 font-bold">100% Demand</span>
          </div>

          <div class="space-y-3" id="flowDemandSinks">
            <!-- Industrial -->
            <div class="space-y-1">
              <div class="flex justify-between text-[11px]">
                <span class="font-semibold text-inkPrimary dark:text-textDarkPrimary">Industrial Parks &amp; Clean Manufacturing</span>
                <span id="indDemandVal" class="font-bold text-teal-600 dark:text-teal-400">54.2% (~152 TWh)</span>
              </div>
              <div class="w-full bg-slate-200 dark:bg-slate-800 h-2 rounded-full overflow-hidden">
                <div id="indDemandBar" class="bg-teal-500 h-full rounded-full transition-all duration-500" style="width: 54%"></div>
              </div>
              <span class="text-[9px] text-slate-400 block">High-tech semiconductors, steel, electronics &amp; RE100 manufacturing</span>
            </div>

            <!-- Residential & Commercial -->
            <div class="space-y-1">
              <div class="flex justify-between text-[11px]">
                <span class="font-semibold text-inkPrimary dark:text-textDarkPrimary">Residential &amp; Commercial Buildings</span>
                <span id="resDemandVal" class="font-bold text-indigo-600 dark:text-indigo-400">35.8% (~100 TWh)</span>
              </div>
              <div class="w-full bg-slate-200 dark:bg-slate-800 h-2 rounded-full overflow-hidden">
                <div id="resDemandBar" class="bg-indigo-500 h-full rounded-full transition-all duration-500" style="width: 36%"></div>
              </div>
              <span class="text-[9px] text-slate-400 block">Urban municipal loads, HVAC cooling, urban lighting &amp; commercial towers</span>
            </div>

            <!-- Transportation Mobility & EVs -->
            <div class="space-y-1">
              <div class="flex justify-between text-[11px]">
                <span class="font-semibold text-inkPrimary dark:text-textDarkPrimary">Electric Mobility &amp; EV Charging Corridors</span>
                <span id="evDemandVal" class="font-bold text-emerald-600 dark:text-emerald-400">6.5% (~18 TWh)</span>
              </div>
              <div class="w-full bg-slate-200 dark:bg-slate-800 h-2 rounded-full overflow-hidden">
                <div id="evDemandBar" class="bg-emerald-500 h-full rounded-full transition-all duration-500" style="width: 7%"></div>
              </div>
              <span class="text-[9px] text-slate-400 block">Fast-growing EV fleet (VinFast &amp; public transport) across 22,055+ charging ports</span>
            </div>

            <!-- Green Hydrogen & Power-to-X -->
            <div class="space-y-1">
              <div class="flex justify-between text-[11px]">
                <span class="font-semibold text-inkPrimary dark:text-textDarkPrimary">Green Hydrogen, Ammonia &amp; Export</span>
                <span id="h2DemandVal" class="font-bold text-violet-600 dark:text-violet-400">3.5% (~10 TWh)</span>
              </div>
              <div class="w-full bg-slate-200 dark:bg-slate-800 h-2 rounded-full overflow-hidden">
                <div id="h2DemandBar" class="bg-violet-500 h-full rounded-full transition-all duration-500" style="width: 4%"></div>
              </div>
              <span class="text-[9px] text-slate-400 block">Power-to-Gas electrolysis, green steel, and maritime shipping fuels</span>
            </div>
          </div>
        </div>

      </div>
    </section>
"""

    # =========================================================================
    # MODULE 3: NATIONAL ENERGY SITUATION & WHOLESALE MARKET TERMINAL
    # =========================================================================
    market_section_html = """
    <!-- ==================================================================== -->
    <!-- MODULE 3: NATIONAL ENERGY SITUATION & WHOLESALE MARKET TERMINAL     -->
    <!-- ==================================================================== -->
    <section id="energyMarketSection" class="p-4 sm:p-5 lg:p-6 rounded-2xl bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder shadow-sm space-y-5">
      
      <!-- Section Header -->
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-borderSlate dark:border-darkBorder">
        <div class="space-y-1">
          <div class="flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
            <span class="font-mono text-[10px] sm:text-[11px] uppercase tracking-wider text-emerald-600 dark:text-emerald-400 font-semibold">
              NATIONAL DISPATCH AUTHORITY &middot; VWEM WHOLESALE CLEARING &middot; DECREE 80 DPPA
            </span>
          </div>
          <h2 class="text-xl sm:text-2xl font-bold tracking-tight text-inkPrimary dark:text-textDarkPrimary">
            National Energy Situation &amp; Wholesale Market Intelligence Terminal
          </h2>
          <p class="text-xs text-inkMuted dark:text-textDarkMuted font-light max-w-4xl">
            Real-time national dispatch balance telemetry, regional grid reserve margins, Vietnam Wholesale Electricity Market (VWEM) spot clearing rates, and Decree 80/2024 DPPA tariff schedules.
          </p>
        </div>

        <!-- Live Market Status Tag -->
        <div class="flex items-center gap-2 font-mono text-[11px] shrink-0">
          <div class="px-2.5 py-1.5 rounded-lg bg-emerald-50 dark:bg-emerald-950/40 border border-emerald-200 dark:border-emerald-800/40 text-emerald-700 dark:text-emerald-400 font-semibold flex items-center gap-1.5 shadow-sm">
            <span class="w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span>
            <span>VWEM Spot Market: Active</span>
          </div>
        </div>
      </div>

      <!-- Dual Column Layout: Left Situation Telemetry, Right Wholesale Market -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-4 items-stretch font-mono text-xs">
        
        <!-- Left: Energy Situation & Dispatch Balance (6 cols) -->
        <div class="lg:col-span-6 p-4 rounded-xl bg-slate-50/70 dark:bg-darkCard/50 border border-borderSlate dark:border-darkBorder space-y-4 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-2 border-b border-borderSlate dark:border-darkBorder">
              <span class="text-slate-400 text-[10px] uppercase font-bold tracking-wider">System Balance &amp; Operational Reserve</span>
              <span class="text-[10px] text-teal-600 dark:text-teal-400 font-semibold">Dispatch Cycle: Real-Time</span>
            </div>

            <!-- Instantaneous Supply vs Demand Meter -->
            <div class="mt-3 p-3.5 rounded-xl bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder space-y-2">
              <div class="flex justify-between items-center text-xs">
                <span class="text-slate-500 dark:text-slate-400 font-bold uppercase">National Peak Demand vs Capacity</span>
                <span class="text-rose-600 dark:text-rose-400 font-bold">57.7% System Loading</span>
              </div>
              <div class="flex items-baseline justify-between">
                <div>
                  <span class="text-xs text-slate-400">Current Peak Load:</span>
                  <div class="text-xl font-bold text-inkPrimary dark:text-textDarkPrimary">48,500 MW</div>
                </div>
                <div class="text-right">
                  <span class="text-xs text-slate-400">Total Installed Capacity:</span>
                  <div class="text-xl font-bold text-teal-600 dark:text-teal-400">84,000 MW</div>
                </div>
              </div>
              <div class="w-full bg-slate-200 dark:bg-slate-800 h-2.5 rounded-full overflow-hidden">
                <div class="bg-gradient-to-r from-teal-500 via-amber-500 to-rose-500 h-full rounded-full" style="width: 58%"></div>
              </div>
            </div>

            <!-- Regional Reserve Margins -->
            <div class="mt-3 space-y-2">
              <span class="text-slate-400 text-[10px] uppercase font-bold tracking-wider">Regional Grid Reserve Margins</span>
              
              <div class="grid grid-cols-3 gap-2">
                <!-- North -->
                <div class="p-2.5 rounded-lg bg-white dark:bg-darkSurface border border-amber-500/30 space-y-1">
                  <span class="text-slate-400 text-[10px] uppercase font-bold">Northern Grid</span>
                  <div class="text-sm font-bold text-amber-600 dark:text-amber-400">12.4% Reserve</div>
                  <span class="text-[9px] text-slate-400 block">Summer Peak Dependent</span>
                </div>
                <!-- Central -->
                <div class="p-2.5 rounded-lg bg-white dark:bg-darkSurface border border-teal-500/30 space-y-1">
                  <span class="text-slate-400 text-[10px] uppercase font-bold">Central Grid</span>
                  <div class="text-sm font-bold text-teal-600 dark:text-teal-400">46.8% Reserve</div>
                  <span class="text-[9px] text-slate-400 block">Clean Energy Surplus</span>
                </div>
                <!-- South -->
                <div class="p-2.5 rounded-lg bg-white dark:bg-darkSurface border border-blue-500/30 space-y-1">
                  <span class="text-slate-400 text-[10px] uppercase font-bold">Southern Grid</span>
                  <div class="text-sm font-bold text-blue-600 dark:text-blue-400">28.5% Reserve</div>
                  <span class="text-[9px] text-slate-400 block">Industrial Baseload</span>
                </div>
              </div>
            </div>

            <!-- Inter-Regional Power Wheeling & Hydro Storage -->
            <div class="mt-3 grid grid-cols-2 gap-2">
              <div class="p-2.5 rounded-lg bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder space-y-0.5">
                <span class="text-slate-400 text-[10px] uppercase">500kV Northward Wheeling</span>
                <div class="text-sm font-bold text-rose-600 dark:text-rose-400">3,200 MW Continuous</div>
                <span class="text-[9px] text-slate-400">Central/South &rarr; North</span>
              </div>
              <div class="p-2.5 rounded-lg bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder space-y-0.5">
                <span class="text-slate-400 text-[10px] uppercase">Cascade Hydro Storage</span>
                <div class="text-sm font-bold text-cyan-600 dark:text-cyan-400">78.5% Reservoir Cap</div>
                <span class="text-[9px] text-slate-400">Sơn La &amp; Hòa Bình Dam</span>
              </div>
            </div>
          </div>

          <div class="p-2.5 rounded-lg bg-slate-100 dark:bg-darkSurface text-[10px] text-slate-500 dark:text-slate-400">
            <strong>System Security Note:</strong> National Load Dispatch Centre (NLDC / NSMO) coordinates dynamic AGC and secondary reserves across all 500kV interties to ensure grid frequency stability at 50.0 &plusmn; 0.2 Hz.
          </div>
        </div>

        <!-- Right: Competitive Wholesale Electricity Market (VWEM & DPPA) (6 cols) -->
        <div class="lg:col-span-6 p-4 rounded-xl bg-slate-50/70 dark:bg-darkCard/50 border border-borderSlate dark:border-darkBorder space-y-4 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between pb-2 border-b border-borderSlate dark:border-darkBorder">
              <span class="text-slate-400 text-[10px] uppercase font-bold tracking-wider">Wholesale Market Clearing &amp; Tariff Structure</span>
              <span class="text-[10px] text-amber-600 dark:text-amber-400 font-semibold">VWEM Spot Reference</span>
            </div>

            <!-- Spot Market Price Ticker -->
            <div class="mt-3 grid grid-cols-3 gap-2">
              <div class="p-2.5 rounded-lg bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder space-y-0.5">
                <span class="text-slate-400 text-[10px] uppercase">System Marginal (SMP)</span>
                <div class="text-sm font-bold text-inkPrimary dark:text-textDarkPrimary">1,640 VND</div>
                <span class="text-[9px] text-slate-400">$0.066 / kWh</span>
              </div>
              <div class="p-2.5 rounded-lg bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder space-y-0.5">
                <span class="text-slate-400 text-[10px] uppercase">Capacity Payment (CAN)</span>
                <div class="text-sm font-bold text-inkPrimary dark:text-textDarkPrimary">185 VND</div>
                <span class="text-[9px] text-slate-400">$0.0075 / kWh</span>
              </div>
              <div class="p-2.5 rounded-lg bg-white dark:bg-darkSurface border border-emerald-500/30 space-y-0.5">
                <span class="text-slate-400 text-[10px] uppercase">Full Market (FMP)</span>
                <div class="text-sm font-bold text-emerald-600 dark:text-emerald-400">1,825 VND</div>
                <span class="text-[9px] text-emerald-600 dark:text-emerald-400 font-semibold">$0.073 / kWh</span>
              </div>
            </div>

            <!-- Decree 80/2024 DPPA Wheeling Tariff Breakdown -->
            <div class="mt-3 p-3 rounded-xl bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder space-y-2">
              <div class="flex justify-between items-center text-xs">
                <span class="font-bold text-inkPrimary dark:text-textDarkPrimary">Decree 80/2024/NĐ-CP DPPA Wheeling Fee</span>
                <span class="text-xs font-bold text-teal-600 dark:text-teal-400">Total: ~280.0 VND/kWh ($0.011)</span>
              </div>
              <div class="grid grid-cols-3 gap-1.5 text-[10px]">
                <div class="p-1.5 rounded bg-slate-50 dark:bg-darkCard">
                  <span class="text-slate-400 block">Transmission Fee:</span>
                  <strong class="text-inkPrimary dark:text-textDarkPrimary">79.5 VND/kWh</strong>
                </div>
                <div class="p-1.5 rounded bg-slate-50 dark:bg-darkCard">
                  <span class="text-slate-400 block">Distribution Fee:</span>
                  <strong class="text-inkPrimary dark:text-textDarkPrimary">165.2 VND/kWh</strong>
                </div>
                <div class="p-1.5 rounded bg-slate-50 dark:bg-darkCard">
                  <span class="text-slate-400 block">Dispatch Ancillary:</span>
                  <strong class="text-inkPrimary dark:text-textDarkPrimary">35.3 VND/kWh</strong>
                </div>
              </div>
            </div>

            <!-- Industrial Time-of-Use (TOU) Retail Price Reference -->
            <div class="mt-3 p-3 rounded-xl bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder space-y-2">
              <div class="flex justify-between items-center text-xs">
                <span class="font-bold text-inkPrimary dark:text-textDarkPrimary">Industrial Retail Electricity TOU Tiers (MoIT)</span>
                <span class="text-[10px] text-slate-400 font-semibold">Decision 2699/QĐ-BCT</span>
              </div>
              <div class="grid grid-cols-3 gap-2 text-[11px]">
                <div class="p-2 rounded-lg bg-emerald-50 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-800/40 text-center">
                  <span class="text-[9px] uppercase text-emerald-600 font-bold block">Off-Peak (22:00-04:00)</span>
                  <strong class="text-emerald-700 dark:text-emerald-300 text-sm">1,100 VND</strong>
                  <span class="text-[9px] text-slate-400 block">$0.044/kWh</span>
                </div>
                <div class="p-2 rounded-lg bg-slate-50 dark:bg-darkCard border border-borderSlate dark:border-darkBorder text-center">
                  <span class="text-[9px] uppercase text-slate-500 font-bold block">Normal Hours</span>
                  <strong class="text-inkPrimary dark:text-textDarkPrimary text-sm">1,685 VND</strong>
                  <span class="text-[9px] text-slate-400 block">$0.068/kWh</span>
                </div>
                <div class="p-2 rounded-lg bg-rose-50 dark:bg-rose-950/30 border border-rose-200 dark:border-rose-800/40 text-center">
                  <span class="text-[9px] uppercase text-rose-600 font-bold block">Peak (09:30-11:30, 17-20)</span>
                  <strong class="text-rose-700 dark:text-rose-300 text-sm">3,171 VND</strong>
                  <span class="text-[9px] text-slate-400 block">$0.128/kWh</span>
                </div>
              </div>
            </div>
          </div>

          <div class="p-2.5 rounded-lg bg-slate-100 dark:bg-darkSurface text-[10px] text-slate-500 dark:text-slate-400">
            <strong>Investment Brief:</strong> Under Decree 80 DPPA, clean generators sell at spot VWEM prices while contracting virtual Contracts-for-Difference (CfD) with corporate buyers, de-risking capital investments.
          </div>
        </div>

      </div>
    </section>
"""

    # 1. Inject Pillars section before pdp8SectorTableSection
    assert 'id="pdp8SectorTableSection"' in html, "Failed to find pdp8SectorTableSection"
    html = html.replace(
        '<section id="pdp8SectorTableSection"',
        f'{pillars_section_html}\n\n    <section id="pdp8SectorTableSection"',
        1
    )

    # 2. Inject Transition Flow & Market terminal after flowCockpitSection
    assert '</section>\n\n\n    <!-- FULL-WIDTH ASSET DOSSIER & PDP8 PIPELINE WORKSPACE -->' in html or 'id="flowCockpitSection"' in html
    flow_section_anchor = '    <!-- FULL-WIDTH ASSET DOSSIER & PDP8 PIPELINE WORKSPACE -->'
    assert flow_section_anchor in html, "Failed to find flow_section_anchor"
    html = html.replace(
        flow_section_anchor,
        f'{transition_flow_html}\n\n{market_section_html}\n\n    {flow_section_anchor}',
        1
    )

    # 3. Add JavaScript handlers for Pillars filter and Transition scenario switcher
    js_logic = """
    // ========================================================================
    // 12 PILLARS FILTER & TRANSITION FLOW SCENARIO SWITCHER
    // ========================================================================
    function filterPillars(category) {
      const cards = document.querySelectorAll('.pillar-card');
      const buttons = {
        'ALL': document.getElementById('pillarFilterAll'),
        'GENERATION': document.getElementById('pillarFilterGen'),
        'GRID': document.getElementById('pillarFilterGrid'),
        'MARKET': document.getElementById('pillarFilterMarket')
      };

      Object.keys(buttons).forEach(k => {
        const btn = buttons[k];
        if (!btn) return;
        if (k === category) {
          btn.className = 'px-2.5 py-1.5 rounded-lg bg-teal-600 text-white font-semibold transition-all cursor-pointer';
        } else {
          btn.className = 'px-2.5 py-1.5 rounded-lg bg-slate-100 dark:bg-darkCard hover:bg-slate-200 dark:hover:bg-slate-800 text-inkMuted dark:text-textDarkMuted transition-all cursor-pointer';
        }
      });

      cards.forEach(card => {
        if (category === 'ALL' || card.getAttribute('data-category') === category) {
          card.classList.remove('hidden');
        } else {
          card.classList.add('hidden');
        }
      });
    }

    const TRANSITION_SCENARIOS = {
      '2025': {
        gen: '280.5 TWh',
        genDelta: '+8.2% YoY growth',
        peak: '48,500 MW',
        peakSub: 'National High: May 2024',
        reShare: '43.2%',
        reBreakdown: 'Hydro 29% + Solar/Wind 14%',
        carbon: '0.68 tCO2/MWh',
        carbonTarget: 'Target <= 0.42 by 2030',
        stage1Pill: '84,000 MW Installed',
        hydroVal: '23,500 MW (28.0%)', hydroBar: '28%',
        coalVal: '26,800 MW (31.9%)', coalBar: '32%',
        gasVal: '7,200 MW (8.6%)', gasBar: '9%',
        solarVal: '16,500 MW (19.6%)', solarBar: '20%',
        windVal: '4,800 MW (5.7%)', windBar: '6%',
        otherVal: '5,200 MW (6.2%)', otherBar: '6%',
        spineVal: '~3,200 MW Peak (Central -> North)',
        lossVal: '6.25% Grid Loss',
        indVal: '54.2% (~152 TWh)', indBar: '54%',
        resVal: '35.8% (~100 TWh)', resBar: '36%',
        evVal: '6.5% (~18 TWh)', evBar: '7%',
        h2Val: '3.5% (~10 TWh)', h2Bar: '4%'
      },
      '2030': {
        gen: '570.0 TWh',
        genDelta: 'Mandated PDP8 Targets',
        peak: '70,500 MW',
        peakSub: 'Projected Peak Demand',
        reShare: '50.3%',
        reBreakdown: 'Hydro 20% + Solar/Wind 30%',
        carbon: '0.42 tCO2/MWh',
        carbonTarget: 'Statutory NDC Commitment',
        stage1Pill: '150,489 MW Mandate',
        hydroVal: '29,346 MW (19.5%)', hydroBar: '20%',
        coalVal: '30,127 MW (20.0%)', coalBar: '20%',
        gasVal: '37,330 MW (24.8%)', gasBar: '25%',
        solarVal: '20,500 MW (13.6%)', solarBar: '14%',
        windVal: '27,880 MW (18.5%)', windBar: '19%',
        otherVal: '5,306 MW (3.5%)', otherBar: '4%',
        spineVal: '~5,000 MW (Circuit-3 Max Flow)',
        lossVal: '5.80% Optimized Loss',
        indVal: '56.0% (~319 TWh)', indBar: '56%',
        resVal: '32.0% (~182 TWh)', resBar: '32%',
        evVal: '9.0% (~51 TWh)', evBar: '9%',
        h2Val: '3.0% (~17 TWh)', h2Bar: '3%'
      },
      '2050': {
        gen: '1,250.0 TWh',
        genDelta: 'Net-Zero Decarbonization',
        peak: '140,000 MW',
        peakSub: 'Full Electrification',
        reShare: '84.5%',
        reBreakdown: 'Wind/Solar 68% + Hydro/BESS 16%',
        carbon: '0.04 tCO2/MWh',
        carbonTarget: 'Net-Zero Carbon Realized',
        stage1Pill: '500,000+ MW Capacity',
        hydroVal: '36,000 MW (7.2%)', hydroBar: '7%',
        coalVal: '0 MW (0.0% Phased Out)', coalBar: '0%',
        gasVal: '42,000 MW (8.4% Clean Ammonia)', gasBar: '8%',
        solarVal: '180,000 MW (36.0%)', solarBar: '36%',
        windVal: '160,000 MW (32.0% Offshore/Onshore)', windBar: '32%',
        otherVal: '82,000 MW (16.4% BESS/Storage)', otherBar: '16%',
        spineVal: '~12,000 MW HVDC Supergrid',
        lossVal: '4.50% Ultra-Efficient Loss',
        indVal: '50.0% (~625 TWh)', indBar: '50%',
        resVal: '28.0% (~350 TWh)', resBar: '28%',
        evVal: '14.0% (~175 TWh)', evBar: '14%',
        h2Val: '8.0% (~100 TWh)', h2Bar: '8%'
      }
    };

    function switchTransitionScenario(year) {
      const data = TRANSITION_SCENARIOS[year];
      if (!data) return;

      ['2025', '2030', '2050'].forEach(y => {
        const btn = document.getElementById(`scenario${y}Btn`);
        if (!btn) return;
        if (y === year) {
          btn.className = 'px-3 py-1.5 rounded-lg bg-white dark:bg-darkSurface text-inkPrimary dark:text-white font-semibold shadow-xs transition-all cursor-pointer';
        } else {
          btn.className = 'px-3 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-inkPrimary dark:hover:text-white transition-all cursor-pointer';
        }
      });

      document.getElementById('flowMetricGen').textContent = data.gen;
      document.getElementById('flowMetricGenDelta').textContent = data.genDelta;
      document.getElementById('flowMetricPeak').textContent = data.peak;
      document.getElementById('flowMetricPeakSub').textContent = data.peakSub;
      document.getElementById('flowMetricReShare').textContent = data.reShare;
      document.getElementById('flowMetricReBreakdown').textContent = data.reBreakdown;
      document.getElementById('flowMetricCarbon').textContent = data.carbon;
      document.getElementById('flowMetricCarbonTarget').textContent = data.carbonTarget;

      document.getElementById('stage1TotalPill').textContent = data.stage1Pill;
      document.getElementById('hydroFlowVal').textContent = data.hydroVal;
      document.getElementById('hydroFlowBar').style.width = data.hydroBar;
      document.getElementById('coalFlowVal').textContent = data.coalVal;
      document.getElementById('coalFlowBar').style.width = data.coalBar;
      document.getElementById('gasFlowVal').textContent = data.gasVal;
      document.getElementById('gasFlowBar').style.width = data.gasBar;
      document.getElementById('solarFlowVal').textContent = data.solarVal;
      document.getElementById('solarFlowBar').style.width = data.solarBar;
      document.getElementById('windFlowVal').textContent = data.windVal;
      document.getElementById('windFlowBar').style.width = data.windBar;
      document.getElementById('otherFlowVal').textContent = data.otherVal;
      document.getElementById('otherFlowBar').style.width = data.otherBar;

      document.getElementById('flowSpineVal').textContent = data.spineVal;
      document.getElementById('flowLossVal').textContent = data.lossVal;

      document.getElementById('indDemandVal').textContent = data.indVal;
      document.getElementById('indDemandBar').style.width = data.indBar;
      document.getElementById('resDemandVal').textContent = data.resVal;
      document.getElementById('resDemandBar').style.width = data.resBar;
      document.getElementById('evDemandVal').textContent = data.evVal;
      document.getElementById('evDemandBar').style.width = data.evBar;
      document.getElementById('h2DemandVal').textContent = data.h2Val;
      document.getElementById('h2DemandBar').style.width = data.h2Bar;
    }
"""

    html = html.replace(
        "function resetNodeInspectionPanel() {",
        f"{js_logic}\n\n    function resetNodeInspectionPanel() {{",
        1
    )

    with open(TARGET_REV, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Successfully generated {TARGET_REV} ({len(html)} bytes)")

if __name__ == "__main__":
    generate()
