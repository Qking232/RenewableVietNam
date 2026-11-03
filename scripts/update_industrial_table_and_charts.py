import os
import re

base_dir = r"G:\My Drive\7. AI\RenewableVietNam\industrial"
src_file = os.path.join(base_dir, "index.html")
rev2_file = os.path.join(base_dir, "index_Rev.002.html")

with open(src_file, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Add Chart.js to <head>
if "chart.umd.min.js" not in html:
    html = html.replace(
        '<script src="https://cdn.tailwindcss.com"></script>',
        '<script src="https://cdn.tailwindcss.com"></script>\n  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.2/dist/chart.umd.min.js"></script>'
    )

# 2. Standardize navigation labels
html = html.replace('>PDP8 Energy<', '>Energy<')
html = html.replace('>Green Industrial<', '>Industrial<')
html = html.replace('>Investment M&A<', '>Legal<')
html = html.replace('>Investment M&amp;A<', '>Legal<')

# 3. Set Table view pill as default active in view mode selector
html = html.replace(
    'id="viewModeBothBtn" class="view-mode-pill px-2.5 py-1 rounded-md bg-teal-600 text-white font-medium transition-colors cursor-pointer flex items-center gap-1.5"',
    'id="viewModeBothBtn" class="view-mode-pill px-2.5 py-1 rounded-md text-inkMuted dark:text-textDarkMuted hover:text-inkPrimary dark:hover:text-white transition-colors cursor-pointer flex items-center gap-1.5"'
)
html = html.replace(
    'id="viewModeTableBtn" class="view-mode-pill px-2.5 py-1 rounded-md text-inkMuted dark:text-textDarkMuted hover:text-inkPrimary dark:hover:text-white transition-colors cursor-pointer flex items-center gap-1.5"',
    'id="viewModeTableBtn" class="view-mode-pill px-2.5 py-1 rounded-md bg-teal-600 text-white font-medium transition-colors cursor-pointer flex items-center gap-1.5"'
)

# 4. Insert Interactive Charts Section right before <section id="hubs"
charts_markup = """
    <!-- INTERACTIVE REGIONAL INDUSTRIAL FOOTPRINT & SOLAR POTENTIAL CHARTS -->
    <section class="p-4 sm:p-5 rounded-2xl bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder shadow-sm space-y-3.5">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-borderSlate/60 dark:border-darkBorder/60 pb-2.5">
        <div>
          <h2 class="text-sm sm:text-base font-bold text-inkPrimary dark:text-textDarkPrimary flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-teal-500 animate-pulse"></span>
            Eco-Industrial Regional Footprint &amp; Siting Telemetry
          </h2>
          <p class="text-xs text-inkMuted dark:text-textDarkMuted font-light mt-0.5">
            Interactive multi-dimensional analytics across 168 national parks. Click any bar or slice to filter the directory table below.
          </p>
        </div>
        <span class="font-mono text-[10px] text-teal-600 dark:text-teal-400 bg-teal-500/10 px-2 py-0.5 rounded border border-teal-500/20 self-start sm:self-auto">
          Interactive Table Cross-Filter Active
        </span>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-4">
        <!-- Chart 1: Regional Footprint & Solar Potential (6 cols) -->
        <div class="lg:col-span-6 p-3 rounded-xl bg-slate-50/70 dark:bg-darkCard/60 border border-borderSlate dark:border-darkBorder space-y-2">
          <div class="flex items-center justify-between font-mono text-[10px] text-inkMuted dark:text-textDarkMuted">
            <span class="font-bold text-inkPrimary dark:text-textDarkPrimary uppercase tracking-wider">Regional Footprint &amp; Solar Potential</span>
            <span class="text-teal-600 dark:text-teal-400">Click &rarr; Filter Region</span>
          </div>
          <div class="relative h-56">
            <canvas id="indRegionalSolarChart"></canvas>
          </div>
        </div>

        <!-- Chart 2: Substation Voltage Class (3 cols) -->
        <div class="lg:col-span-3 p-3 rounded-xl bg-slate-50/70 dark:bg-darkCard/60 border border-borderSlate dark:border-darkBorder space-y-2 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between font-mono text-[10px] text-inkMuted dark:text-textDarkMuted mb-1">
              <span class="font-bold text-inkPrimary dark:text-textDarkPrimary uppercase tracking-wider">Substation Voltage</span>
              <span class="text-teal-600 dark:text-teal-400">Click &rarr; Filter</span>
            </div>
            <div class="relative h-44 flex items-center justify-center">
              <canvas id="indSubstationDoughnutChart"></canvas>
            </div>
          </div>
          <div class="pt-1.5 border-t border-borderSlate/60 dark:border-darkBorder/60 flex items-center justify-between font-mono text-[9px] text-slate-400">
            <span>220kV / 110kV</span>
            <span>Grid Interties</span>
          </div>
        </div>

        <!-- Chart 3: Decree 80 DPPA Readiness (3 cols) -->
        <div class="lg:col-span-3 p-3 rounded-xl bg-slate-50/70 dark:bg-darkCard/60 border border-borderSlate dark:border-darkBorder space-y-2 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between font-mono text-[10px] text-inkMuted dark:text-textDarkMuted mb-1">
              <span class="font-bold text-inkPrimary dark:text-textDarkPrimary uppercase tracking-wider">DPPA Readiness</span>
              <span class="text-teal-600 dark:text-teal-400">Click &rarr; Filter</span>
            </div>
            <div class="relative h-44 flex items-center justify-center">
              <canvas id="indDppaTiersChart"></canvas>
            </div>
          </div>
          <div class="pt-1.5 border-t border-borderSlate/60 dark:border-darkBorder/60 flex items-center justify-between font-mono text-[9px] text-slate-400">
            <span>Decree 80 Scope</span>
            <span>168 Parks</span>
          </div>
        </div>
      </div>
    </section>
"""

html = html.replace('<section id="hubs" class="space-y-5">', charts_markup + '\n    <section id="hubs" class="space-y-5">')

# 5. Add JavaScript Chart logic and table cross-filtering
chart_js_code = """
    // =========================================================================
    // INTERACTIVE CHARTS: INDUSTRIAL FOOTPRINT, SUBSTATIONS & DPPA TIERS
    // =========================================================================
    let indRegionalChartInstance = null;
    let indSubstationChartInstance = null;
    let indDppaChartInstance = null;

    function initIndustrialCharts() {
      if (!HUBS || HUBS.length === 0) return;
      const isDark = document.documentElement.classList.contains('dark');
      const textColor = isDark ? '#94A3B8' : '#64748B';
      const gridColor = isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)';
      const tooltipBg = isDark ? '#141D32' : '#FFFFFF';
      const tooltipText = isDark ? '#F8FAFC' : '#0F172A';

      // 1. Aggregate metrics by region
      const regions = ['South', 'North', 'Central'];
      const regArea = { South: 0, North: 0, Central: 0 };
      const regSolar = { South: 0, North: 0, Central: 0 };
      const regCount = { South: 0, North: 0, Central: 0 };

      // 2. Voltage breakdown
      const voltCount = { '220kV Intertie': 0, '110kV Onsite': 0, '22kV/35kV Feeder': 0 };

      // 3. DPPA Tiers breakdown
      const dppaCount = { 'Cat 1 & 2 Ready': 0, 'Cat 2 Wheeling': 0, 'Developing': 0 };

      HUBS.forEach(h => {
        const reg = h.region || 'South';
        if (regArea[reg] !== undefined) {
          regArea[reg] += (h.totalAreaHa || 0);
          regSolar[reg] += (h.rooftopPotentialMWp || 0);
          regCount[reg] += 1;
        }

        const kv = h.substationKv || 0;
        if (kv >= 220) voltCount['220kV Intertie'] += 1;
        else if (kv >= 110) voltCount['110kV Onsite'] += 1;
        else voltCount['22kV/35kV Feeder'] += 1;

        if (h.dppaClass === 'ready') dppaCount['Cat 1 & 2 Ready'] += 1;
        else if (h.dppaClass === 'cat2') dppaCount['Cat 2 Wheeling'] += 1;
        else dppaCount['Developing'] += 1;
      });

      // Chart 1: Regional Solar & Land Area
      const ctxReg = document.getElementById('indRegionalSolarChart')?.getContext('2d');
      if (ctxReg) {
        if (indRegionalChartInstance) indRegionalChartInstance.destroy();
        indRegionalChartInstance = new Chart(ctxReg, {
          type: 'bar',
          data: {
            labels: ['Southern Zone', 'Northern Zone', 'Central Zone'],
            datasets: [
              {
                label: 'Rooftop Solar Potential (MWp)',
                data: [Math.round(regSolar.South), Math.round(regSolar.North), Math.round(regSolar.Central)],
                backgroundColor: '#14B8A6',
                borderRadius: 4,
                barPercentage: 0.5,
                yAxisID: 'y'
              },
              {
                label: 'Industrial Land (ha / 10)',
                data: [Math.round(regArea.South / 10), Math.round(regArea.North / 10), Math.round(regArea.Central / 10)],
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
                labels: { color: textColor, font: { size: 10, family: 'monospace' }, boxWidth: 10 }
              },
              tooltip: {
                backgroundColor: tooltipBg,
                titleColor: tooltipText,
                bodyColor: tooltipText,
                borderColor: 'rgba(255,255,255,0.1)',
                borderWidth: 1,
                callbacks: {
                  afterLabel: () => 'Click bar to filter directory table'
                }
              }
            },
            scales: {
              x: { grid: { display: false }, ticks: { color: textColor, font: { size: 10 } } },
              y: {
                type: 'linear',
                position: 'left',
                grid: { color: gridColor },
                ticks: { color: textColor, font: { size: 10, family: 'monospace' }, callback: val => `${val} MWp` }
              },
              y1: {
                type: 'linear',
                position: 'right',
                grid: { display: false },
                ticks: { color: textColor, font: { size: 10, family: 'monospace' }, callback: val => `${val * 10} ha` }
              }
            },
            onClick: (evt, elements) => {
              if (elements.length > 0) {
                const idx = elements[0].index;
                const regKey = regions[idx];
                currentFilter.region = regKey;
                document.querySelectorAll('.filter-pill-region').forEach(p => {
                  if (p.getAttribute('data-filter-region') === regKey) {
                    p.className = 'filter-pill-region px-2.5 py-1 rounded-md bg-teal-600 text-white font-medium transition-colors';
                  } else {
                    p.className = 'filter-pill-region px-2.5 py-1 rounded-md bg-slate-100 dark:bg-darkCard text-inkPrimary dark:text-textDarkMuted hover:bg-slate-200 dark:hover:bg-darkCard/80 transition-colors';
                  }
                });
                renderTable();
                document.getElementById('hubs')?.scrollIntoView({ behavior: 'smooth' });
              }
            }
          }
        });
      }

      // Chart 2: Substation Voltage Doughnut
      const ctxSub = document.getElementById('indSubstationDoughnutChart')?.getContext('2d');
      if (ctxSub) {
        if (indSubstationChartInstance) indSubstationChartInstance.destroy();
        indSubstationChartInstance = new Chart(ctxSub, {
          type: 'doughnut',
          data: {
            labels: Object.keys(voltCount),
            datasets: [{
              data: Object.values(voltCount),
              backgroundColor: ['#3B82F6', '#14B8A6', '#94A3B8'],
              borderWidth: 2,
              borderColor: isDark ? '#0E1424' : '#FFFFFF'
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            cutout: '68%',
            plugins: {
              legend: {
                position: 'bottom',
                labels: { color: textColor, font: { size: 9, family: 'monospace' }, boxWidth: 8 }
              },
              tooltip: {
                backgroundColor: tooltipBg,
                titleColor: tooltipText,
                bodyColor: tooltipText,
                borderColor: 'rgba(255,255,255,0.1)',
                borderWidth: 1,
                callbacks: {
                  label: ctx => ` ${ctx.label}: ${ctx.raw} Hubs`
                }
              }
            },
            onClick: (evt, elements) => {
              if (elements.length > 0) {
                const idx = elements[0].index;
                const subSelect = document.getElementById('filterSubstationSelect');
                if (subSelect) {
                  if (idx === 0) subSelect.value = '220';
                  else if (idx === 1) subSelect.value = '110';
                  else subSelect.value = 'all';
                  currentFilter.substation = subSelect.value;
                  renderTable();
                  document.getElementById('hubs')?.scrollIntoView({ behavior: 'smooth' });
                }
              }
            }
          }
        });
      }

      // Chart 3: DPPA Readiness Horizontal Bar
      const ctxDppa = document.getElementById('indDppaTiersChart')?.getContext('2d');
      if (ctxDppa) {
        if (indDppaChartInstance) indDppaChartInstance.destroy();
        indDppaChartInstance = new Chart(ctxDppa, {
          type: 'bar',
          data: {
            labels: Object.keys(dppaCount),
            datasets: [{
              data: Object.values(dppaCount),
              backgroundColor: ['#10B981', '#06B6D4', '#F59E0B'],
              borderRadius: 4
            }]
          },
          options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: { display: false },
              tooltip: {
                backgroundColor: tooltipBg,
                titleColor: tooltipText,
                bodyColor: tooltipText,
                borderColor: 'rgba(255,255,255,0.1)',
                borderWidth: 1,
                callbacks: {
                  label: ctx => ` ${ctx.label}: ${ctx.raw} Hubs`
                }
              }
            },
            scales: {
              x: { grid: { color: gridColor }, ticks: { color: textColor, font: { size: 9, family: 'monospace' } } },
              y: { grid: { display: false }, ticks: { color: textColor, font: { size: 9, weight: '600' } } }
            },
            onClick: (evt, elements) => {
              if (elements.length > 0) {
                const idx = elements[0].index;
                const dppaSelect = document.getElementById('filterDppaSelect');
                if (dppaSelect) {
                  if (idx === 0) dppaSelect.value = 'ready';
                  else if (idx === 1) dppaSelect.value = 'cat2';
                  else if (idx === 2) dppaSelect.value = 'developing';
                  currentFilter.dppa = dppaSelect.value;
                  renderTable();
                  document.getElementById('hubs')?.scrollIntoView({ behavior: 'smooth' });
                }
              }
            }
          }
        });
      }
    }
"""

html = html.replace('updateCalculator();\n    }', 'updateCalculator();\n      initIndustrialCharts();\n    }')
html = html.replace('applyTheme(!isDark);', 'applyTheme(!isDark);\n      initIndustrialCharts();')
html = html.replace('window.addEventListener("resize", () => {', chart_js_code + '\n    window.addEventListener("resize", () => {\n      initIndustrialCharts();')

with open(rev2_file, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Created sequential revision: {rev2_file}")

with open(src_file, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Updated active file: {src_file}")
