"""
Script to build, enrich, and deploy the PDP8 Statutory Tracker (2026-2030)
across Renewable Vietnam and Qking232.github.io.
"""
import os
import json
import re

REPO1 = "G:/My Drive/7. AI/Gemini/RenewableVietNam"
REPO2 = "G:/My Drive/7. AI/Gemini/Qking232.github.io"

# 1. Create data/pdp8_targets.json
def generate_pdp8_json():
    pdp8_data = {
        "metadata": {
            "statutory_decree": "Decision 500/QD-TTg & Decision 262/QD-TTg",
            "statutory_title": "National Power Development Plan VIII (PDP8)",
            "planning_horizon": "2021-2030 (Vision to 2050)",
            "total_statutory_capacity_2030_mw": 150489,
            "current_operating_baseload_mw": 80612,
            "statutory_delta_mw": 69877,
            "updated_at": "2026-10-22T12:00:00Z"
        },
        "fuel_targets": [
            {
                "fuel": "Hydropower",
                "fuel_vi": "Thủy điện",
                "target_2030_mw": 29346,
                "current_operating_mw": 19101,
                "pipeline_mw": 10245,
                "target_share_pct": 19.5,
                "color": "blue",
                "hex": "#3b82f6",
                "status_note": "Expansion of major dams (Ialy, Tri An, Hoa Binh) + small hydro run-of-river"
            },
            {
                "fuel": "Onshore Wind",
                "fuel_vi": "Điện gió trên bờ & gần bờ",
                "target_2030_mw": 21880,
                "current_operating_mw": 4603,
                "pipeline_mw": 17277,
                "target_share_pct": 14.5,
                "color": "teal",
                "hex": "#14b8a6",
                "status_note": "Heavy deployment in Central Highlands, South Central Coast & Mekong Delta"
            },
            {
                "fuel": "Offshore Wind",
                "fuel_vi": "Điện gió ngoài khơi",
                "target_2030_mw": 6000,
                "current_operating_mw": 0,
                "pipeline_mw": 6000,
                "target_share_pct": 4.0,
                "color": "cyan",
                "hex": "#06b6d4",
                "status_note": "Pioneering pilot concessions (Thang Long, La Gan, Ca Mau) awaiting marine spatial licenses"
            },
            {
                "fuel": "Solar Power",
                "fuel_vi": "Điện mặt trời (Tập trung & Mái nhà)",
                "target_2030_mw": 15436,
                "current_operating_mw": 11467,
                "pipeline_mw": 3969,
                "target_share_pct": 10.3,
                "color": "amber",
                "hex": "#f59e0b",
                "status_note": "12,836 MW utility-scale + 2,600 MW self-consumption under Decree 135/2024/ND-CP"
            },
            {
                "fuel": "Biomass & Waste",
                "fuel_vi": "Sinh khối & Điện rác",
                "target_2030_mw": 2270,
                "current_operating_mw": 620,
                "pipeline_mw": 1650,
                "target_share_pct": 1.5,
                "color": "emerald",
                "hex": "#10b981",
                "status_note": "Wood pellets, bagasse, and municipal solid waste-to-energy facilities"
            },
            {
                "fuel": "Domestic Gas & LNG",
                "fuel_vi": "Nhiệt điện Khí & LNG",
                "target_2030_mw": 37330,
                "current_operating_mw": 7200,
                "pipeline_mw": 30130,
                "target_share_pct": 24.8,
                "color": "purple",
                "hex": "#a855f7",
                "status_note": "14,930 MW domestic gas (Block B, Ca Voi Xanh) + 22,400 MW imported LNG fleet"
            },
            {
                "fuel": "Grid Storage & Pumped Hydro",
                "fuel_vi": "Thủy điện tích năng & Pin lưu trữ (BESS)",
                "target_2030_mw": 2700,
                "current_operating_mw": 0,
                "pipeline_mw": 2700,
                "target_share_pct": 1.8,
                "color": "indigo",
                "hex": "#6366f1",
                "status_note": "Bac Ai 1,200 MW pumped storage + pilot utility BESS frequency regulation systems"
            },
            {
                "fuel": "Coal Thermal (Capped)",
                "fuel_vi": "Nhiệt điện than (Đạt đỉnh & Khống chế)",
                "target_2030_mw": 30127,
                "current_operating_mw": 26000,
                "pipeline_mw": 4127,
                "target_share_pct": 20.0,
                "color": "slate",
                "hex": "#64748b",
                "status_note": "Strict cap under JETP; no new coal-fired plants approved after 2030"
            },
            {
                "fuel": "Power Imports",
                "fuel_vi": "Nhập khẩu điện",
                "target_2030_mw": 5400,
                "current_operating_mw": 1621,
                "pipeline_mw": 3779,
                "target_share_pct": 3.6,
                "color": "rose",
                "hex": "#f43f5e",
                "status_note": "Cross-border transmission lines from southern Laos and China"
            }
        ],
        "priority_projects": [
            {
                "id": "NT34-LNG",
                "name": "Nhon Trach 3 & 4 LNG Thermal Plant",
                "name_vi": "Nhà máy Nhiệt điện LNG Nhơn Trạch 3 & 4",
                "fuel": "LNG",
                "capacity_mw": 1624,
                "province": "Đồng Nai",
                "investor": "PV Power (PetroVietnam)",
                "target_cod": "2025-2026",
                "status": "Under Construction",
                "status_vi": "Đang xây dựng",
                "progress_pct": 92,
                "decree_ref": "Decision 500/QD-TTg Priority Baseload",
                "notes": "First utility-scale imported LNG power project in Vietnam, high efficiency CCGT"
            },
            {
                "id": "BACAI-PH",
                "name": "Bac Ai Pumped Storage Hydroelectric Plant",
                "name_vi": "Thủy điện Tích năng Bác Ái",
                "fuel": "Hydro & Storage",
                "capacity_mw": 1200,
                "province": "Ninh Thuận",
                "investor": "EVN (Electricity of Vietnam)",
                "target_cod": "2028-2029",
                "status": "Under Construction",
                "status_vi": "Đang thi công",
                "progress_pct": 45,
                "decree_ref": "Decision 500/QD-TTg Grid Stabilization",
                "notes": "Vital national grid storage facility balancing solar and wind curtailment in South Central"
            },
            {
                "id": "THLON-OW",
                "name": "Thang Long Offshore Wind Farm",
                "name_vi": "Dự án Điện gió Ngoài khơi ThangLong Wind",
                "fuel": "Offshore Wind",
                "capacity_mw": 3400,
                "province": "Bình Thuận",
                "investor": "Enterprize Energy Group",
                "target_cod": "2029-2030",
                "status": "Marine Survey & Feasibility",
                "status_vi": "Khảo sát biển & FS",
                "progress_pct": 30,
                "decree_ref": "Decision 500/QD-TTg Offshore Pioneer",
                "notes": "Deep offshore wind cluster with potential green hydrogen/ammonia synthesis export"
            },
            {
                "id": "LAGAN-OW",
                "name": "La Gan Offshore Wind Project",
                "name_vi": "Dự án Điện gió Ngoài khơi La Gàn",
                "fuel": "Offshore Wind",
                "capacity_mw": 3500,
                "province": "Bình Thuận",
                "investor": "Copenhagen Infrastructure Partners (CIP) / Asiapetro",
                "target_cod": "2029-2030",
                "status": "Permitting & Feasibility",
                "status_vi": "Cấp phép & Lập dự án",
                "progress_pct": 28,
                "decree_ref": "Decision 500/QD-TTg Offshore Pioneer",
                "notes": "$10.5B capital expenditure commitment, 3.5 GW multi-phase marine array"
            },
            {
                "id": "SONMY-LNG",
                "name": "Son My 1 & 2 LNG Power Complex",
                "name_vi": "Trung tâm Điện khí LNG Sơn Mỹ 1 & 2",
                "fuel": "LNG",
                "capacity_mw": 4500,
                "province": "Bình Thuận",
                "investor": "EDF / Sojitz / AES Corporation",
                "target_cod": "2028-2030",
                "status": "Feasibility & PPA",
                "status_vi": "Chuẩn bị đầu tư & PPA",
                "progress_pct": 35,
                "decree_ref": "Decision 500/QD-TTg South Central Hub",
                "notes": "Anchor consumer for Son My LNG receiving terminal, replacing coal baseline"
            },
            {
                "id": "BACLI-LNG",
                "name": "Bac Lieu LNG Clean Energy Project",
                "name_vi": "Dự án Điện khí LNG Bạc Liêu",
                "fuel": "LNG",
                "capacity_mw": 3200,
                "province": "Bạc Liêu",
                "investor": "Delta Offshore Energy (DOE)",
                "target_cod": "2028-2029",
                "status": "PPA Negotiation",
                "status_vi": "Đàm phán PPA",
                "progress_pct": 40,
                "decree_ref": "Decision 500/QD-TTg Mekong Anchor",
                "notes": "Floating storage and regasification unit (FSRU) offshore power plant"
            },
            {
                "id": "HAILA-LNG",
                "name": "Hai Lang LNG Power Center (Phase 1)",
                "name_vi": "Trung tâm Điện khí LNG Hải Lăng (Giai đoạn 1)",
                "fuel": "LNG",
                "capacity_mw": 1500,
                "province": "Quảng Trị",
                "investor": "T&T Group / Hanwha Energy / KOGAS / KOSPO",
                "target_cod": "2028",
                "status": "Engineering & Site Prep",
                "status_vi": "Chuẩn bị mặt bằng & Thiết kế",
                "progress_pct": 32,
                "decree_ref": "Decision 500/QD-TTg North Central Anchor",
                "notes": "Regional gas turbine power complex supporting Central Vietnam industrial corridor"
            },
            {
                "id": "IALY-EXP",
                "name": "Ialy Hydropower Plant Expansion",
                "name_vi": "Dự án Mở rộng Thủy điện Ialy",
                "fuel": "Hydropower",
                "capacity_mw": 360,
                "province": "Gia Lai",
                "investor": "EVN (Electricity of Vietnam)",
                "target_cod": "2025-2026",
                "status": "Testing & Commissioning",
                "status_vi": "Chạy thử & Phát điện",
                "progress_pct": 96,
                "decree_ref": "Decision 500/QD-TTg Peak Load Hydro",
                "notes": "Two 180 MW turbine units providing essential peak regulation and grid inertia"
            },
            {
                "id": "TRIAN-EXP",
                "name": "Tri An Hydropower Plant Expansion",
                "name_vi": "Dự án Mở rộng Thủy điện Trị An",
                "fuel": "Hydropower",
                "capacity_mw": 200,
                "province": "Đồng Nai",
                "investor": "EVN (Electricity of Vietnam)",
                "target_cod": "2026",
                "status": "Under Construction",
                "status_vi": "Đang thi công",
                "progress_pct": 60,
                "decree_ref": "Decision 500/QD-TTg Southern Peaking",
                "notes": "Crucial peak generation support for Ho Chi Minh City metropolitan economic zone"
            },
            {
                "id": "CAMAU-W",
                "name": "Ca Mau 1 Wind Power Cluster (Phases 1-4)",
                "name_vi": "Cụm Nhà máy Điện gió Cà Mau 1",
                "fuel": "Onshore Wind",
                "capacity_mw": 350,
                "province": "Cà Mau",
                "investor": "WTO (Vietracimex)",
                "target_cod": "2026",
                "status": "Under Construction",
                "status_vi": "Đang lắp đặt",
                "progress_pct": 75,
                "decree_ref": "Decision 500/QD-TTg Mekong Wind Hub",
                "notes": "Largest intertidal wind farm in the southern coastal tip of Vietnam"
            }
        ]
    }

    for repo in [REPO1, REPO2]:
        out_dir = os.path.join(repo, "data")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "pdp8_targets.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(pdp8_data, f, indent=2, ensure_ascii=False)
        print(f"Written PDP8 targets JSON to {out_path}")

# 2. Build Section #pdp8 HTML
def get_pdp8_section_html():
    return '''
    <!-- ==================================================================== -->
    <!-- PDP8 STATUTORY CAPACITY TRACKER & 2026-2030 CAPITAL PIPELINE         -->
    <!-- Decision 500/QD-TTg & Implementation Plan Decision 262/QD-TTg        -->
    <!-- ==================================================================== -->
    <section id="pdp8" class="space-y-6 pt-4">
      <!-- Section Header -->
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-borderSlate dark:border-darkBorder pb-4">
        <div class="space-y-1">
          <div class="flex items-center gap-2">
            <span class="inline-block w-2.5 h-2.5 rounded-full bg-teal-500 animate-pulse"></span>
            <span class="font-mono text-[11px] uppercase tracking-wider text-teal-600 dark:text-teal-400 font-semibold">
              Statutory Governance &middot; Decision 500/QĐ-TTg &amp; 262/QĐ-TTg
            </span>
          </div>
          <h2 class="text-xl sm:text-2xl font-normal tracking-tight text-inkPrimary dark:text-textDarkPrimary">
            PDP8 Statutory Tracker &amp; 2026–2030 Capital Project Pipeline
          </h2>
          <p class="text-xs text-inkMuted dark:text-textDarkMuted font-light max-w-3xl">
            Real-time compliance tracking comparing Vietnam's active commercial baseload (80.6 GW) against the 150.5 GW statutory capacity mandate by 2030 across wind, solar, LNG, hydro, and grid storage.
          </p>
        </div>

        <div class="flex items-center gap-2 font-mono text-[11px] shrink-0">
          <a href="/projectenergy/#atlas" class="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-teal-600 hover:bg-teal-500 text-white font-medium transition-colors shadow-sm">
            <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7" />
            </svg>
            <span>Geospatial Atlas</span>
          </a>
        </div>
      </div>

      <!-- Telemetry Metric Cards -->
      <div class="grid grid-cols-2 lg:grid-cols-4 gap-3 sm:gap-4 font-mono">
        <div class="p-4 rounded-xl bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder shadow-sm space-y-1">
          <div class="text-[10px] uppercase text-inkMuted dark:text-textDarkMuted">2030 Statutory Target</div>
          <div class="text-xl sm:text-2xl font-bold text-inkPrimary dark:text-textDarkPrimary">150,489 <span class="text-xs font-normal text-teal-600 dark:text-teal-400">MW</span></div>
          <div class="text-[10px] text-inkMuted dark:text-textDarkMuted">Decision 500/QD-TTg Horizon</div>
        </div>

        <div class="p-4 rounded-xl bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder shadow-sm space-y-1">
          <div class="text-[10px] uppercase text-inkMuted dark:text-textDarkMuted">Empirical Operating Baseload</div>
          <div class="text-xl sm:text-2xl font-bold text-emerald-600 dark:text-emerald-400">80,612 <span class="text-xs font-normal text-inkMuted">MW</span></div>
          <div class="text-[10px] text-inkMuted dark:text-textDarkMuted">53.6% of 2030 Mandate Active</div>
        </div>

        <div class="p-4 rounded-xl bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder shadow-sm space-y-1">
          <div class="text-[10px] uppercase text-inkMuted dark:text-textDarkMuted">Statutory Delta (to 2030)</div>
          <div class="text-xl sm:text-2xl font-bold text-amber-600 dark:text-amber-400">+69,877 <span class="text-xs font-normal text-inkMuted">MW</span></div>
          <div class="text-[10px] text-inkMuted dark:text-textDarkMuted">Required Commissioning Pipeline</div>
        </div>

        <div class="p-4 rounded-xl bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder shadow-sm space-y-1">
          <div class="text-[10px] uppercase text-inkMuted dark:text-textDarkMuted">Clean Energy Share Target</div>
          <div class="text-xl sm:text-2xl font-bold text-teal-600 dark:text-teal-400">~47.3% <span class="text-xs font-normal text-inkMuted">Target</span></div>
          <div class="text-[10px] text-inkMuted dark:text-textDarkMuted">Excluding Capped Coal Thermal</div>
        </div>
      </div>

      <!-- Sector Progress Meters (Decision 500 vs Active Fleet) -->
      <div class="p-5 rounded-2xl bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder shadow-sm space-y-4">
        <div class="flex items-center justify-between pb-2 border-b border-borderSlate dark:border-darkBorder">
          <h3 class="font-mono text-xs uppercase tracking-wider font-bold text-inkPrimary dark:text-textDarkPrimary flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-teal-500"></span>
            Statutory Fuel Trajectory &amp; Operationalization Delta (MW)
          </h3>
          <span class="font-mono text-[10px] text-inkMuted dark:text-textDarkMuted">Solid = Operational &middot; Striped = Pipeline Required</span>
        </div>

        <div id="pdp8SectorGauges" class="space-y-3.5">
          <!-- Dynamically populated via JS -->
        </div>
      </div>

      <!-- Major Priority Capital Projects Roadmap (2026-2030) -->
      <div class="p-5 rounded-2xl bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder shadow-sm space-y-4">
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
          <!-- Dynamically populated via JS -->
        </div>
      </div>
    </section>
'''

# 3. Build PDP8 JS logic
def get_pdp8_js():
    return '''
    // =========================================================================
    // PDP8 STATUTORY TRACKER & PIPELINE RENDERING
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
        console.warn("PDP8 JSON fetch error, using embedded statutory baseline", e);
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
              <a href="/projectenergy/?search=${encodeURIComponent(p.name.split(' ')[0])}" class="inline-flex items-center gap-1 text-[10px] text-teal-600 dark:text-teal-400 hover:underline font-semibold">
                <span>View on Atlas</span>
                <svg class="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
                </svg>
              </a>
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
'''

def update_html_files():
    targets = [
        os.path.join(REPO1, "index.html"),
        os.path.join(REPO1, "green", "index.html"),
        os.path.join(REPO2, "index.html"),
        os.path.join(REPO2, "green", "index.html")
    ]

    pdp8_sec = get_pdp8_section_html()
    pdp8_js = get_pdp8_js()

    for path in targets:
        if not os.path.exists(path):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        # 1. Add #pdp8 link to Desktop Navigation
        if 'href="#pdp8"' not in content:
            content = content.replace(
                '<a href="/calculator/" class="px-2.5 py-1 rounded-md hover:text-teal-600',
                '<a href="#pdp8" class="px-2.5 py-1 rounded-md hover:text-teal-600 dark:hover:text-teal-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">PDP8 Tracker</a>\n              <span class="text-slate-300 dark:text-slate-700">&middot;</span>\n              <a href="/calculator/" class="px-2.5 py-1 rounded-md hover:text-teal-600'
            )

        # 2. Add #pdp8 link to Mobile Touch Navigation Carousel
        if 'href="#pdp8" class="px-2.5 py-1.5' not in content:
            content = content.replace(
                '<a href="/calculator/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-teal-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">Power Sizer</a>',
                '<a href="#pdp8" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-teal-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">PDP8 Tracker</a>\n          <a href="/calculator/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-teal-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">Power Sizer</a>'
            )

        # 3. Insert Section #pdp8 right before section#hubs
        if 'id="pdp8"' not in content:
            hubs_pos = content.find('<section id="hubs"')
            if hubs_pos != -1:
                content = content[:hubs_pos] + pdp8_sec + "\n\n    " + content[hubs_pos:]
                print(f"Inserted section#pdp8 into {path}")

        # 4. Insert PDP8 JS logic right before fetchNewsData();
        if 'function loadPdp8Data' not in content:
            target_harvest = "fetchNewsData();"
            harvest_pos = content.rfind(target_harvest)
            if harvest_pos != -1:
                content = content[:harvest_pos] + pdp8_js + "\n\n      " + target_harvest + "\n      loadPdp8Data();" + content[harvest_pos + len(target_harvest):]
                print(f"Inserted PDP8 JS and loadPdp8Data() into {path}")

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {path}")

def main():
    print("Generating data/pdp8_targets.json...")
    generate_pdp8_json()
    print("\nUpdating index.html and green/index.html across repositories...")
    update_html_files()
    print("\n[SUCCESS] PDP8 Statutory Tracker deployed!")

if __name__ == "__main__":
    main()
