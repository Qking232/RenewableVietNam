#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate index_Rev.005.html:
1. Fix normalizeProjects and initEnergyCharts to properly parse capacity_mw and province.
2. Fix loadPdp8Data by removing premature return so renderPdp8Projects, renderIndependentSectorTable, and renderPdp8Gauges always fire.
3. Add full priority_projects fallback array if pdp8_targets.json is missing or network fails.
4. Integrate an Interactive Power Grid & Renewable Transmission Flow GIS Cartography Cockpit with animated flow vectors directly above the dossiers.
"""

import re
from pathlib import Path

SOURCE_HTML = Path(r"G:\My Drive\7. AI\RenewableVietNam\projectenergy\index.html")
TARGET_HTML = Path(r"G:\My Drive\7. AI\RenewableVietNam\projectenergy\index_Rev.005.html")

def generate_rev005():
    with open(SOURCE_HTML, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Add CSS for animated transmission power flow
    flow_css = """    /* Animated directional power flow along 500kV Backbone */
    @keyframes dashFlow {
      to {
        stroke-dashoffset: -32;
      }
    }
    .grid-flow-500kv {
      stroke-dasharray: 10, 6 !important;
      animation: dashFlow 1.5s linear infinite !important;
    }
    .grid-flow-220kv {
      stroke-dasharray: 8, 6 !important;
      animation: dashFlow 2.2s linear infinite !important;
    }"""

    if "grid-flow-500kv" not in html:
        html = html.replace(".project-marker-pin:hover {", f"{flow_css}\n    .project-marker-pin:hover {{", 1)

    # 2. Fix normalizeProjects function
    old_norm = """    // 3. Load External Projects Data
    function normalizeProjects(list) {
      return (list || []).map(p => ({
        ...p,
        name: p.name || "Unnamed Facility",
        company: p.company || p.developer || "MOIT / Provincial EPC Allocation",
        developer: p.company || p.developer || "MOIT / Provincial EPC Allocation",
        capacity: p.capacity || p.cap || (p.capacity_mw ? `${p.capacity_mw} MW` : "Planned"),
        location: p.location || p.loc || p.province || "Vietnam",
        lat: p.lat || null,
        lon: p.lon || p.lng || null
      }));
    }"""

    new_norm = """    // 3. Load External Projects Data (Normalized Schema)
    function normalizeProjects(list) {
      return (list || []).map(p => {
        const parsedCap = parseFloat(p.capacity || p.cap || p.capacity_mw) || 0;
        const prov = p.province || p.location || p.loc || "Vietnam";
        return {
          ...p,
          name: p.name || "Unnamed Facility",
          company: p.company || p.developer || "MOIT / Provincial EPC Allocation",
          developer: p.company || p.developer || "MOIT / Provincial EPC Allocation",
          capacity: p.capacity || (parsedCap ? `${parsedCap} MW` : "Planned"),
          capacity_mw: parsedCap,
          location: prov,
          province: prov,
          status: p.status || p.cod_status || "Operational (COD)",
          type: p.type || p.fuel || "Renewable",
          lat: p.lat || null,
          lon: p.lon || p.lng || null
        };
      });
    }"""

    html = html.replace(old_norm, new_norm, 1)

    # 3. Fix loadPdp8Data to eliminate premature return and provide robust fallback
    pdp8_pattern = r'async function loadPdp8Data\(\)[\s\S]*?renderPdp8Projects\(\);\s*}'
    
    new_pdp8_code = """async function loadPdp8Data() {
      try {
        if (window.RV_Supabase) {
          const raw = await window.RV_Supabase.getWithFallback('pdp8_fuel_targets', '/data/pdp8_targets.json', {
            cacheKey: 'pdp8_fuel_targets'
          });
          if (raw && (raw.fuel_targets || raw.priority_projects)) {
            pdp8Dataset = raw;
          }
        }
        if (!pdp8Dataset) {
          const res = await fetch("/data/pdp8_targets.json?t=" + Date.now());
          if (res.ok) pdp8Dataset = await res.json();
        }
      } catch (e) {
        console.warn("PDP8 JSON fetch error, attempting fallback targets:", e);
      }

      if (!pdp8Dataset || !pdp8Dataset.fuel_targets || !pdp8Dataset.priority_projects) {
        pdp8Dataset = {
          metadata: {
            statutory_decree: "Decision 500/QD-TTg & Decision 262/QD-TTg",
            statutory_title: "National Power Development Plan VIII (PDP8)",
            planning_horizon: "2021-2030 (Vision to 2050)",
            total_statutory_capacity_2030_mw: 150489,
            current_operating_baseload_mw: 80612,
            statutory_delta_mw: 69877
          },
          fuel_targets: [
            { fuel: "Hydropower", fuel_vi: "Thủy điện", target_2030_mw: 29346, current_operating_mw: 19101, pipeline_mw: 10245, target_share_pct: 19.5, hex: "#3b82f6", status_note: "Expansion of major dams (Ialy, Tri An, Hoa Binh) + small hydro run-of-river" },
            { fuel: "Onshore Wind", fuel_vi: "Điện gió trên bờ & gần bờ", target_2030_mw: 21880, current_operating_mw: 4603, pipeline_mw: 17277, target_share_pct: 14.5, hex: "#14b8a6", status_note: "Heavy deployment in Central Highlands, South Central Coast & Mekong Delta" },
            { fuel: "Offshore Wind", fuel_vi: "Điện gió ngoài khơi", target_2030_mw: 6000, current_operating_mw: 0, pipeline_mw: 6000, target_share_pct: 4.0, hex: "#06b6d4", status_note: "Pioneering pilot concessions awaiting marine spatial licenses" },
            { fuel: "Solar Power", fuel_vi: "Điện mặt trời (Tập trung & Mái nhà)", target_2030_mw: 15436, current_operating_mw: 11467, pipeline_mw: 3969, target_share_pct: 10.3, hex: "#f59e0b", status_note: "12,836 MW utility-scale + 2,600 MW self-consumption under Decree 135/2024/ND-CP" },
            { fuel: "Biomass & Waste", fuel_vi: "Sinh khối & Điện rác", target_2030_mw: 2270, current_operating_mw: 620, pipeline_mw: 1650, target_share_pct: 1.5, hex: "#10b981", status_note: "Wood pellets, bagasse, and municipal solid waste-to-energy facilities" },
            { fuel: "Domestic Gas & LNG", fuel_vi: "Nhiệt điện Khí & LNG", target_2030_mw: 37330, current_operating_mw: 7200, pipeline_mw: 30130, target_share_pct: 24.8, hex: "#a855f7", status_note: "14,930 MW domestic gas + 22,400 MW imported LNG fleet" },
            { fuel: "Grid Storage & Pumped Hydro", fuel_vi: "Thủy điện tích năng & Pin lưu trữ (BESS)", target_2030_mw: 2700, current_operating_mw: 0, pipeline_mw: 2700, target_share_pct: 1.8, hex: "#6366f1", status_note: "Bac Ai 1,200 MW pumped storage + pilot utility BESS frequency regulation" },
            { fuel: "Coal Thermal (Capped)", fuel_vi: "Nhiệt điện than (Đạt đỉnh & Khống chế)", target_2030_mw: 30127, current_operating_mw: 26000, pipeline_mw: 4127, target_share_pct: 20.0, hex: "#64748b", status_note: "Strict cap under JETP; no new coal-fired plants approved after 2030" },
            { fuel: "Power Imports", fuel_vi: "Nhập khẩu điện", target_2030_mw: 5400, current_operating_mw: 1621, pipeline_mw: 3779, target_share_pct: 3.6, hex: "#f43f5e", status_note: "Cross-border transmission lines from southern Laos and China" }
          ],
          priority_projects: [
            { id: "NT34-LNG", name: "Nhà máy Nhiệt điện LNG Nhơn Trạch 3 & 4", fuel: "LNG", capacity_mw: 1624, province: "Đồng Nai", investor: "PV Power (PetroVietnam)", target_cod: "2025-2026", status: "Under Construction", progress_pct: 92, notes: "First utility-scale imported LNG power project in Vietnam, high efficiency CCGT", lat: 10.687, lon: 106.924 },
            { id: "BAC-AI-PSH", name: "Thủy điện tích năng Bác Ái (1,200 MW)", fuel: "Hydro", capacity_mw: 1200, province: "Ninh Thuận", investor: "EVN", target_cod: "2028-2029", status: "Under Construction", progress_pct: 45, notes: "Largest grid storage asset in Southeast Asia, absorbing renewable curtailment", lat: 11.833, lon: 108.917 },
            { id: "QUANG-TRACH-1", name: "Nhiệt điện Quảng Trạch 1 (2x701 MW)", fuel: "Thermal", capacity_mw: 1403, province: "Quảng Bình", investor: "EVN", target_cod: "2026", status: "Under Construction", progress_pct: 78, notes: "Ultra-supercritical baseload generation hub", lat: 17.892, lon: 106.495 },
            { id: "IALY-EXP", name: "Thủy điện Ialy Mở rộng (2x180 MW)", fuel: "Hydro", capacity_mw: 360, province: "Gia Lai", investor: "EVN", target_cod: "2025", status: "Under Construction", progress_pct: 95, notes: "Peak load shaving and frequency regulation on Sesan river", lat: 14.218, lon: 107.828 },
            { id: "HOA-BINH-EXP", name: "Thủy điện Hòa Bình Mở rộng (2x240 MW)", fuel: "Hydro", capacity_mw: 480, province: "Hòa Bình", investor: "EVN", target_cod: "2025-2026", status: "Under Construction", progress_pct: 85, notes: "Northern grid balancing and flood discharge utilization", lat: 20.812, lon: 105.328 },
            { id: "TRI-AN-EXP", name: "Thủy điện Trị An Mở rộng (2x100 MW)", fuel: "Hydro", capacity_mw: 200, province: "Đồng Nai", investor: "EVN", target_cod: "2026-2027", status: "In Development", progress_pct: 30, notes: "Southern peaking capacity expansion on Dong Nai river", lat: 11.116, lon: 106.998 },
            { id: "BLOCK-B-OMON", name: "Chuỗi dự án Khí - Điện Lô B & Ô Môn", fuel: "LNG / gas", capacity_mw: 3810, province: "Cần Thơ", investor: "PVN / Marubeni", target_cod: "2027-2028", status: "In Development", progress_pct: 40, notes: "Strategic upstream gas-to-power flagship supplying Southwest grid", lat: 10.125, lon: 105.655 },
            { id: "HAI-LANG-LNG", name: "Trung tâm Điện khí LNG Hải Lăng GĐ 1", fuel: "LNG", capacity_mw: 1500, province: "Quảng Trị", investor: "T&T / KOGAS / KOSPO / HANWHA", target_cod: "2028-2029", status: "In Development", progress_pct: 25, notes: "Central coast LNG receiving terminal and power complex", lat: 16.712, lon: 107.315 },
            { id: "THANG-LONG-OW", name: "Điện gió ngoài khơi Thăng Long (GĐ Thí điểm)", fuel: "Wind", capacity_mw: 3400, province: "Bình Thuận", investor: "Enterprize Energy", target_cod: "2029-2030", status: "In Development", progress_pct: 20, notes: "Pioneering deepwater offshore wind pilot 50km off Ke Ga cape", lat: 10.550, lon: 108.200 },
            { id: "LA-GAN-OW", name: "Điện gió ngoài khơi La Gàn (GĐ Thí điểm)", fuel: "Wind", capacity_mw: 3500, province: "Bình Thuận", investor: "Copenhagen Infrastructure Partners (CIP)", target_cod: "2029-2030", status: "In Development", progress_pct: 20, notes: "Statutory pilot offshore concession under marine spatial licensing", lat: 11.020, lon: 108.680 }
          ]
        };
      }

      renderIndependentSectorTable();
      renderPdp8Gauges();
      renderPdp8Projects();
    }"""

    html = re.sub(pdp8_pattern, new_pdp8_code, html, count=1)

    # 4. Enhance initEnergyCharts with proper field extraction & robust rendering
    old_charts_pattern = r'function initEnergyCharts\(\)[\s\S]*?^    }'
    new_charts_code = """function initEnergyCharts() {
      if (!ALL_PROJECTS || ALL_PROJECTS.length === 0) return;
      if (typeof Chart === 'undefined') return;

      const isDark = document.documentElement.classList.contains('dark');
      const textColor = isDark ? '#94A3B8' : '#64748B';
      const gridColor = isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)';
      const tooltipBg = isDark ? '#141D32' : '#FFFFFF';
      const tooltipText = isDark ? '#F8FAFC' : '#0F172A';

      // Aggregate capacity by province
      const provMap = {};
      const statusMap = { 'Operational (COD)': 0, 'Under Construction': 0, 'In Development': 0, 'Planned': 0 };

      ALL_PROJECTS.forEach(p => {
        const prov = p.province || p.location || 'Unknown';
        if (!provMap[prov]) {
          provMap[prov] = { total: 0, wind: 0, solar: 0, hydro: 0, lng: 0, other: 0 };
        }
        const cap = parseFloat(p.capacity_mw) || parseFloat(p.capacity) || 0;
        provMap[prov].total += cap;
        const fuel = (p.type || p.fuel || '').toLowerCase();
        if (fuel.includes('wind')) provMap[prov].wind += cap;
        else if (fuel.includes('solar')) provMap[prov].solar += cap;
        else if (fuel.includes('hydro')) provMap[prov].hydro += cap;
        else if (fuel.includes('gas') || fuel.includes('lng')) provMap[prov].lng += cap;
        else provMap[prov].other += cap;

        const stat = (p.status || p.cod_status || 'Operational (COD)').toLowerCase();
        if (stat.includes('operat') || stat.includes('cod') || stat.includes('active')) {
          statusMap['Operational (COD)'] += cap;
        } else if (stat.includes('construct')) {
          statusMap['Under Construction'] += cap;
        } else if (stat.includes('permit') || stat.includes('develop') || stat.includes('approv')) {
          statusMap['In Development'] += cap;
        } else {
          statusMap['Planned'] += cap;
        }
      });

      // Top 10 Provinces by Total Clean Energy Capacity
      const sortedProvs = Object.keys(provMap)
        .filter(pr => pr !== 'Unknown' && provMap[pr].total > 0)
        .sort((a, b) => provMap[b].total - provMap[a].total)
        .slice(0, 10);

      const provLabels = sortedProvs;
      const windData = sortedProvs.map(pr => Math.round(provMap[pr].wind));
      const solarData = sortedProvs.map(pr => Math.round(provMap[pr].solar));
      const hydroData = sortedProvs.map(pr => Math.round(provMap[pr].hydro));
      const lngData = sortedProvs.map(pr => Math.round(provMap[pr].lng));
      const otherData = sortedProvs.map(pr => Math.round(provMap[pr].other));

      // Chart 1: Top 10 Provinces Horizontal Stacked Bar
      const canvasProv = document.getElementById('energyTopProvincesChart');
      if (canvasProv) {
        if (energyTopProvChartInstance) energyTopProvChartInstance.destroy();
        energyTopProvChartInstance = new Chart(canvasProv.getContext('2d'), {
          type: 'bar',
          data: {
            labels: provLabels,
            datasets: [
              { label: 'Wind', data: windData, backgroundColor: '#10B981', stack: 'stack1' },
              { label: 'Solar', data: solarData, backgroundColor: '#F59E0B', stack: 'stack1' },
              { label: 'Hydro', data: hydroData, backgroundColor: '#06B6D4', stack: 'stack1' },
              { label: 'LNG / Gas', data: lngData, backgroundColor: '#3B82F6', stack: 'stack1' },
              { label: 'Biomass/Other', data: otherData, backgroundColor: '#8B5CF6', stack: 'stack1' }
            ]
          },
          options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: false,
            onClick: (e, elements) => {
              if (elements && elements.length > 0) {
                const idx = elements[0].index;
                const clickedProv = provLabels[idx];
                const provSel = document.getElementById('provinceSelect');
                if (provSel) {
                  provSel.value = clickedProv;
                  selectedProvince = clickedProv;
                  applyFilters();
                  document.getElementById('cockpitContainer')?.scrollIntoView({ behavior: 'smooth' });
                }
              }
            },
            plugins: {
              legend: {
                position: 'top',
                labels: { color: textColor, font: { size: 10, family: 'monospace' }, boxWidth: 10 }
              },
              tooltip: {
                backgroundColor: tooltipBg,
                titleColor: tooltipText,
                bodyColor: tooltipText,
                borderColor: 'rgba(255,255,255,0.1)',
                borderWidth: 1,
                callbacks: {
                  afterLabel: () => 'Click bar to filter directory'
                }
              }
            },
            scales: {
              x: {
                stacked: true,
                grid: { color: gridColor },
                ticks: { color: textColor, font: { size: 9, family: 'monospace' }, callback: v => v.toLocaleString() + ' MW' }
              },
              y: {
                stacked: true,
                grid: { display: false },
                ticks: { color: textColor, font: { size: 10, family: 'monospace', weight: 'bold' } }
              }
            }
          }
        });
      }

      // Chart 2: Asset Status Lifecycle Doughnut
      const canvasStatus = document.getElementById('energyStatusDoughnutChart');
      if (canvasStatus) {
        if (energyStatusChartInstance) energyStatusChartInstance.destroy();
        const statusLabels = Object.keys(statusMap);
        const statusValues = Object.values(statusMap).map(v => Math.round(v));

        energyStatusChartInstance = new Chart(canvasStatus.getContext('2d'), {
          type: 'doughnut',
          data: {
            labels: statusLabels,
            datasets: [{
              data: statusValues,
              backgroundColor: ['#10B981', '#F59E0B', '#3B82F6', '#64748B'],
              borderWidth: 2,
              borderColor: isDark ? '#0D1322' : '#FFFFFF'
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            cutout: '72%',
            plugins: {
              legend: {
                position: 'bottom',
                labels: { color: textColor, font: { size: 9, family: 'monospace' }, boxWidth: 8, padding: 8 }
              },
              tooltip: {
                backgroundColor: tooltipBg,
                titleColor: tooltipText,
                bodyColor: tooltipText,
                borderColor: 'rgba(255,255,255,0.1)',
                borderWidth: 1,
                callbacks: {
                  label: ctx => ` ${ctx.label}: ${ctx.raw.toLocaleString()} MW`
                }
              }
            }
          }
        });
      }
    }"""

    html = re.sub(old_charts_pattern, new_charts_code, html, count=1, flags=re.MULTILINE)

    # 5. Insert Interactive Power Flow GIS Cockpit directly above the Dossier Workspace
    flow_cockpit_html = """    <!-- ==================================================================== -->
    <!-- INTERACTIVE GIS TRANSMISSION & RENEWABLE POWER FLOW COCKPIT          -->
    <!-- ==================================================================== -->
    <section id="flowCockpitSection" class="p-4 sm:p-5 rounded-2xl bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder shadow-sm space-y-3.5">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2.5 pb-2.5 border-b border-borderSlate/60 dark:border-darkBorder/60">
        <div class="space-y-0.5">
          <div class="flex items-center gap-2">
            <span class="w-2.5 h-2.5 rounded-full bg-rose-500 animate-ping"></span>
            <span class="font-mono text-[10px] sm:text-[11px] uppercase tracking-wider text-rose-600 dark:text-rose-400 font-semibold">
              Decision 500/QĐ-TTg &middot; 500kV Supergrid Backbone &middot; Inter-Regional Wheeling Flow
            </span>
          </div>
          <h2 class="text-base sm:text-lg font-bold text-inkPrimary dark:text-textDarkPrimary">
            National Electrical Transmission Spine &amp; Clean Energy Power Flow
          </h2>
          <p class="text-xs text-inkMuted dark:text-textDarkMuted font-light max-w-4xl">
            Live geospatial topology visualizing North-South power wheeling corridors between Central/Southern renewable hubs and Northern load centers across 65,566 km of AC circuits and 1,915 substations.
          </p>
        </div>

        <!-- Quick Flow Telemetry Metrics -->
        <div class="flex flex-wrap items-center gap-2 font-mono text-[11px] shrink-0">
          <div class="px-2.5 py-1.5 rounded-lg bg-rose-50 dark:bg-rose-950/40 border border-rose-200 dark:border-rose-800/40 text-rose-700 dark:text-rose-400 font-semibold flex items-center gap-1.5 shadow-sm">
            <span class="w-2 h-2 rounded-full bg-rose-500 animate-pulse"></span>
            <span>500kV Flow: 15,888 km (180 Circuits)</span>
          </div>
          <div class="px-2.5 py-1.5 rounded-lg bg-amber-50 dark:bg-amber-950/40 border border-amber-200 dark:border-amber-800/40 text-amber-700 dark:text-amber-400 font-semibold flex items-center gap-1.5 shadow-sm">
            <span class="w-2 h-2 rounded-full bg-amber-500"></span>
            <span>220kV Grid: 27,007 km (780 Circuits)</span>
          </div>
        </div>
      </div>

      <!-- Main Leaflet Flow Map Container -->
      <div class="relative w-full h-[460px] sm:h-[520px] rounded-xl border border-borderSlate dark:border-darkBorder overflow-hidden shadow-inner bg-slate-950">
        <div id="mainEnergyFlowMap" class="w-full h-full z-10"></div>

        <!-- Top Right Layer Filter Pills -->
        <div class="absolute top-3 right-3 z-20 flex items-center gap-1.5 p-1.5 rounded-xl bg-white/95 dark:bg-darkSurface/95 backdrop-blur-md border border-borderSlate dark:border-darkBorder shadow-lg font-mono text-[10px]">
          <button id="mapToggleFlow500Btn" class="px-2.5 py-1 rounded-lg bg-rose-600 text-white font-semibold transition-all cursor-pointer">
            500kV Spine Flow
          </button>
          <button id="mapToggleGrid220Btn" class="px-2.5 py-1 rounded-lg bg-white dark:bg-darkCard text-inkMuted dark:text-textDarkMuted hover:text-amber-600 border border-borderSlate dark:border-darkBorder transition-all cursor-pointer">
            220kV Grid
          </button>
          <button id="mapToggleAssetsBtn" class="px-2.5 py-1 rounded-lg bg-white dark:bg-darkCard text-inkMuted dark:text-textDarkMuted hover:text-teal-600 border border-borderSlate dark:border-darkBorder transition-all cursor-pointer">
            Clean Plants (960)
          </button>
          <button id="mapToggleResetViewBtn" class="px-2 py-1 rounded-lg bg-slate-100 dark:bg-darkCard hover:bg-slate-200 text-slate-600 dark:text-slate-300 transition-all cursor-pointer" title="Reset Vietnam View">
            Reset ⟲
          </button>
        </div>

        <!-- Bottom Left Interactive Flow Telemetry Legend -->
        <div class="absolute bottom-3 left-3 z-20 p-3 rounded-xl bg-white/95 dark:bg-darkSurface/95 backdrop-blur-md border border-borderSlate dark:border-darkBorder shadow-lg font-mono text-[10px] space-y-1.5 max-w-xs">
          <div class="font-bold text-inkPrimary dark:text-textDarkPrimary uppercase tracking-wider text-[11px] flex items-center justify-between">
            <span>Transmission Corridor Flow</span>
            <span class="w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span>
          </div>
          <div class="flex items-center gap-2">
            <span class="w-4 h-1 rounded-full bg-rose-500 shadow-sm"></span>
            <span class="text-inkPrimary dark:text-textDarkPrimary font-semibold">500kV North-South Spine (Directional Flow)</span>
          </div>
          <div class="flex items-center gap-2">
            <span class="w-4 h-1 rounded-full bg-amber-500"></span>
            <span class="text-inkPrimary dark:text-textDarkPrimary">220kV Intertie Regional Corridors</span>
          </div>
          <div class="flex items-center gap-2">
            <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 border border-white"></span>
            <span class="text-inkPrimary dark:text-textDarkPrimary">Operational Generation Plants (Solar/Wind/Hydro)</span>
          </div>
          <div class="pt-1.5 border-t border-borderSlate/60 dark:border-darkBorder/60 flex items-center justify-between text-[9px] text-slate-400">
            <span>Model: NSMO Vietnam 2025</span>
            <span>65,566 km Circuits</span>
          </div>
        </div>
      </div>
    </section>
"""

    cockpit_marker = '<!-- FULL-WIDTH ASSET DOSSIER & PDP8 PIPELINE WORKSPACE -->\n    <section id="cockpitContainer"'
    if cockpit_marker in html:
        html = html.replace(cockpit_marker, f"{flow_cockpit_html}\n\n    {cockpit_marker}", 1)

    # 6. Add JavaScript initialization for mainEnergyFlowMap
    flow_map_js = """
    // ========================================================================
    // INTEGRATED GIS POWER FLOW & TRANSMISSION CARTOGRAPHY (MAIN DASHBOARD)
    // ========================================================================
    let mainFlowMapInstance = null;
    let mainFlow500Layer = null;
    let mainGrid220Layer = null;
    let mainAssetsLayer = null;
    let show500Flow = true;
    let show220Grid = false;
    let showCleanAssets = true;

    function initMainFlowMap() {
      const mapEl = document.getElementById('mainEnergyFlowMap');
      if (!mapEl || typeof L === 'undefined') return;

      if (!mainFlowMapInstance) {
        mainFlowMapInstance = L.map('mainEnergyFlowMap', {
          center: [16.2, 107.5],
          zoom: 6,
          zoomControl: true,
          attributionControl: false
        });

        const isDark = document.documentElement.classList.contains('dark');
        const tileUrl = isDark 
          ? 'https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png'
          : 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png';

        L.tileLayer(tileUrl, { maxZoom: 18 }).addTo(mainFlowMapInstance);

        mainFlow500Layer = L.layerGroup().addTo(mainFlowMapInstance);
        mainGrid220Layer = L.layerGroup();
        mainAssetsLayer = L.layerGroup().addTo(mainFlowMapInstance);

        // Bind filter toggles
        document.getElementById('mapToggleFlow500Btn')?.addEventListener('click', function() {
          show500Flow = !show500Flow;
          if (show500Flow) {
            mainFlowMapInstance.addLayer(mainFlow500Layer);
            this.classList.add('bg-rose-600', 'text-white', 'font-semibold');
            this.classList.remove('bg-white', 'dark:bg-darkCard', 'text-inkMuted', 'dark:text-textDarkMuted');
          } else {
            mainFlowMapInstance.removeLayer(mainFlow500Layer);
            this.classList.remove('bg-rose-600', 'text-white', 'font-semibold');
            this.classList.add('bg-white', 'dark:bg-darkCard', 'text-inkMuted', 'dark:text-textDarkMuted');
          }
        });

        document.getElementById('mapToggleGrid220Btn')?.addEventListener('click', function() {
          show220Grid = !show220Grid;
          if (show220Grid) {
            mainFlowMapInstance.addLayer(mainGrid220Layer);
            this.classList.add('bg-amber-600', 'text-white', 'font-semibold');
            this.classList.remove('bg-white', 'dark:bg-darkCard', 'text-inkMuted', 'dark:text-textDarkMuted');
          } else {
            mainFlowMapInstance.removeLayer(mainGrid220Layer);
            this.classList.remove('bg-amber-600', 'text-white', 'font-semibold');
            this.classList.add('bg-white', 'dark:bg-darkCard', 'text-inkMuted', 'dark:text-textDarkMuted');
          }
        });

        document.getElementById('mapToggleAssetsBtn')?.addEventListener('click', function() {
          showCleanAssets = !showCleanAssets;
          if (showCleanAssets) {
            mainFlowMapInstance.addLayer(mainAssetsLayer);
            this.classList.add('bg-teal-600', 'text-white', 'font-semibold');
            this.classList.remove('bg-white', 'dark:bg-darkCard', 'text-inkMuted', 'dark:text-textDarkMuted');
          } else {
            mainFlowMapInstance.removeLayer(mainAssetsLayer);
            this.classList.remove('bg-teal-600', 'text-white', 'font-semibold');
            this.classList.add('bg-white', 'dark:bg-darkCard', 'text-inkMuted', 'dark:text-textDarkMuted');
          }
        });

        document.getElementById('mapToggleResetViewBtn')?.addEventListener('click', function() {
          mainFlowMapInstance.setView([16.2, 107.5], 6);
        });
      }

      renderMainFlowVectors();
    }

    function renderMainFlowVectors() {
      if (!mainFlowMapInstance || !mainFlow500Layer) return;
      mainFlow500Layer.clearLayers();
      if (mainGrid220Layer) mainGrid220Layer.clearLayers();
      if (mainAssetsLayer) mainAssetsLayer.clearLayers();

      // 1. Render 500kV Power Flow Spine (with animated directional pulse)
      if (Array.isArray(ALL_GRID_LINES)) {
        ALL_GRID_LINES.forEach(l => {
          if (!l.coords || l.coords.length < 2) return;
          const latLngs = [[l.coords[0][1], l.coords[0][0]], [l.coords[1][1], l.coords[1][0]]];

          if (l.v_kv === 500) {
            const poly = L.polyline(latLngs, {
              color: '#f43f5e',
              weight: 3.5,
              opacity: 0.9,
              className: 'grid-flow-500kv'
            });
            poly.bindPopup(`
              <div class="font-mono text-xs space-y-1 p-1">
                <div class="font-bold text-rose-600 dark:text-rose-400">500 kV Supergrid Transmission Spine</div>
                <div><strong>Corridor:</strong> ${l.s1_name || l.s1_id} &rarr; ${l.s2_name || l.s2_id}</div>
                <div><strong>Conductor:</strong> ${l.conductor || '4xACSR400'}</div>
                <div><strong>Distance:</strong> ${l.len_km} km</div>
                <div><strong>Impedance:</strong> R=${l.r} Ω, X=${l.x} Ω</div>
              </div>
            `);
            poly.addTo(mainFlow500Layer);
          } else if (l.v_kv === 220 && mainGrid220Layer) {
            const poly220 = L.polyline(latLngs, {
              color: '#f59e0b',
              weight: 2.0,
              opacity: 0.75,
              className: 'grid-flow-220kv'
            });
            poly220.bindPopup(`
              <div class="font-mono text-xs space-y-1 p-1">
                <div class="font-bold text-amber-600 dark:text-amber-400">220 kV Regional Sub-transmission</div>
                <div><strong>Corridor:</strong> ${l.s1_name || l.s1_id} &rarr; ${l.s2_name || l.s2_id}</div>
                <div><strong>Distance:</strong> ${l.len_km} km</div>
              </div>
            `);
            poly220.addTo(mainGrid220Layer);
          }
        });
      }

      // 2. Render 500kV Substations
      if (Array.isArray(ALL_GRID_SUBSTATIONS)) {
        ALL_GRID_SUBSTATIONS.forEach(s => {
          if (s.lat === null || s.lng === null || s.max_v < 500) return;
          const marker = L.circleMarker([s.lat, s.lng], {
            radius: 6,
            fillColor: '#f43f5e',
            color: '#ffffff',
            weight: 1.5,
            opacity: 1,
            fillOpacity: 0.9
          });
          marker.bindTooltip(`<strong>${s.name}</strong> (500kV TBA)<br>${s.total_tx_mva} MVA &middot; ${s.place || 'Vietnam'}`, { direction: 'top' });
          marker.on('click', () => openSubstationModal(s.id));
          marker.addTo(mainFlow500Layer);
        });
      }

      // 3. Render Generation Plants (Clean Generation Clusters)
      if (Array.isArray(ALL_PROJECTS) && mainAssetsLayer) {
        ALL_PROJECTS.slice(0, 300).forEach(p => {
          const lat = parseFloat(p.lat);
          const lon = parseFloat(p.lon || p.lng);
          if (!lat || !lon) return;

          const fuel = (p.type || p.fuel || '').toLowerCase();
          let color = '#10B981';
          if (fuel.includes('solar')) color = '#F59E0B';
          else if (fuel.includes('wind')) color = '#06B6D4';
          else if (fuel.includes('hydro')) color = '#3B82F6';

          const marker = L.circleMarker([lat, lon], {
            radius: 3.5,
            fillColor: color,
            color: '#ffffff',
            weight: 0.8,
            opacity: 0.9,
            fillOpacity: 0.8
          });

          marker.bindTooltip(`<strong>${p.name}</strong><br>${p.capacity_mw || p.capacity} &middot; ${p.type}`, { direction: 'top' });
          marker.addTo(mainAssetsLayer);
        });
      }
    }
"""

    html = html.replace('// ========================================================================\n    // NATIONAL TRANSMISSION GRID LOGIC (NSMO 2025 MODEL INTEGRATION)', f'{flow_map_js}\n\n    // ========================================================================\n    // NATIONAL TRANSMISSION GRID LOGIC (NSMO 2025 MODEL INTEGRATION)', 1)

    # 7. Add initMainFlowMap trigger in DOMContentLoaded and after loadProjectsData/loadGridData
    html = html.replace('initEnergyCharts();\n            return;\n          }\n        }\n        const res = await fetch("/data/vietnam_clean_energy_projects.json', 'initEnergyCharts();\n            initMainFlowMap();\n            return;\n          }\n        }\n        const res = await fetch("/data/vietnam_clean_energy_projects.json', 1)

    html = html.replace('initEnergyCharts();\n          return;\n        }\n      } catch (e)', 'initEnergyCharts();\n          initMainFlowMap();\n          return;\n        }\n      } catch (e)', 1)

    html = html.replace('loadGridData();', 'loadGridData();\n      setTimeout(initMainFlowMap, 150);', 1)

    with open(TARGET_HTML, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Generated {TARGET_HTML} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_rev005()
