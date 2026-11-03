import os
import re

base_dir = r"G:\My Drive\7. AI\RenewableVietNam\projectenergy"
src_file = os.path.join(base_dir, "index.html")
rev3_file = os.path.join(base_dir, "index_Rev.003.html")

with open(src_file, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Add Chart.js to <head> if not present
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

# 3. Set Table View as default in HTML markup
html = html.replace(
    '<span id="viewModeText">Table</span>',
    '<span id="viewModeText">Cards</span>'
)
html = html.replace(
    '<div id="dossierCardsList" class="space-y-2">',
    '<div id="dossierCardsList" class="hidden space-y-2">'
)
html = html.replace(
    '<div id="dossierTableContainer" class="hidden rounded-xl border border-borderSlate dark:border-darkBorder overflow-hidden">',
    '<div id="dossierTableContainer" class="rounded-xl border border-borderSlate dark:border-darkBorder overflow-hidden">'
)

# 4. Set activeDossierView = "table" in JavaScript
html = html.replace(
    'let activeDossierView = "cards";',
    'let activeDossierView = "table";'
)

# 5. Insert Interactive Charts Section above #cockpitContainer
charts_markup = """
    <!-- INTERACTIVE PROVINCIAL CAPACITY & ASSET LIFECYCLE CHARTS -->
    <section class="p-4 sm:p-5 rounded-2xl bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder shadow-sm space-y-3.5">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-borderSlate/60 dark:border-darkBorder/60 pb-2.5">
        <div>
          <h2 class="text-sm sm:text-base font-bold text-inkPrimary dark:text-textDarkPrimary flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-teal-500 animate-pulse"></span>
            Provincial Capacity Intelligence &amp; Asset Lifecycle Analytics
          </h2>
          <p class="text-xs text-inkMuted dark:text-textDarkMuted font-light mt-0.5">
            Interactive multi-fuel generation analytics across 960+ assets. Click any province bar or status slice to filter the table below.
          </p>
        </div>
        <span class="font-mono text-[10px] text-teal-600 dark:text-teal-400 bg-teal-500/10 px-2 py-0.5 rounded border border-teal-500/20 self-start sm:self-auto">
          Interactive Cross-Filter Enabled
        </span>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-4">
        <!-- Chart 1: Top 10 Energy Provinces (8 cols) -->
        <div class="lg:col-span-8 p-3 rounded-xl bg-slate-50/70 dark:bg-darkCard/60 border border-borderSlate dark:border-darkBorder space-y-2">
          <div class="flex items-center justify-between font-mono text-[10px] text-inkMuted dark:text-textDarkMuted">
            <span class="font-bold text-inkPrimary dark:text-textDarkPrimary uppercase tracking-wider">Top 10 Energy Provinces (MW Capacity)</span>
            <span class="text-teal-600 dark:text-teal-400">Click bar &rarr; Filter Table</span>
          </div>
          <div class="relative h-56">
            <canvas id="energyTopProvincesChart"></canvas>
          </div>
        </div>

        <!-- Chart 2: Asset Status Lifecycle (4 cols) -->
        <div class="lg:col-span-4 p-3 rounded-xl bg-slate-50/70 dark:bg-darkCard/60 border border-borderSlate dark:border-darkBorder space-y-2 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between font-mono text-[10px] text-inkMuted dark:text-textDarkMuted mb-1">
              <span class="font-bold text-inkPrimary dark:text-textDarkPrimary uppercase tracking-wider">Commercial Status</span>
              <span class="text-teal-600 dark:text-teal-400">Click &rarr; Filter</span>
            </div>
            <div class="relative h-48 flex items-center justify-center">
              <canvas id="energyStatusDoughnutChart"></canvas>
            </div>
          </div>
          <div class="pt-2 border-t border-borderSlate/60 dark:border-darkBorder/60 flex items-center justify-between font-mono text-[10px] text-slate-400">
            <span>Operational Baselines</span>
            <span>PDP8 Quota Target</span>
          </div>
        </div>
      </div>
    </section>
"""

target_marker = '    <!-- FULL-WIDTH ASSET DOSSIER & PDP8 PIPELINE WORKSPACE -->'
if target_marker in html:
    html = html.replace(target_marker, charts_markup + "\n" + target_marker)
else:
    html = html.replace('<section id="cockpitContainer"', charts_markup + '\n    <section id="cockpitContainer"')

# 6. Add JavaScript for Chart initialization & reactive cross-filtering
chart_js_code = """
    // =========================================================================
    // INTERACTIVE CHARTS: PROVINCIAL CAPACITY & ASSET LIFECYCLE
    // =========================================================================
    let energyTopProvChartInstance = null;
    let energyStatusChartInstance = null;

    function initEnergyCharts() {
      if (!ALL_PROJECTS || ALL_PROJECTS.length === 0) return;
      const isDark = document.documentElement.classList.contains('dark');
      const textColor = isDark ? '#94A3B8' : '#64748B';
      const gridColor = isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)';
      const tooltipBg = isDark ? '#141D32' : '#FFFFFF';
      const tooltipText = isDark ? '#F8FAFC' : '#0F172A';

      // Aggregate capacity by province
      const provMap = {};
      const statusMap = { 'Operational (COD)': 0, 'Under Construction': 0, 'In Development': 0, 'Planned': 0 };

      ALL_PROJECTS.forEach(p => {
        const prov = p.province || 'Unknown';
        if (!provMap[prov]) {
          provMap[prov] = { total: 0, wind: 0, solar: 0, hydro: 0, lng: 0, other: 0 };
        }
        const cap = parseFloat(p.capacity_mw) || 0;
        provMap[prov].total += cap;
        const fuel = (p.type || '').toLowerCase();
        if (fuel.includes('wind')) provMap[prov].wind += cap;
        else if (fuel.includes('solar')) provMap[prov].solar += cap;
        else if (fuel.includes('hydro')) provMap[prov].hydro += cap;
        else if (fuel.includes('gas') || fuel.includes('lng')) provMap[prov].lng += cap;
        else provMap[prov].other += cap;

        const stat = (p.status || p.cod_status || '').toLowerCase();
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

      // Top 10 Provinces
      const sortedProvs = Object.keys(provMap).sort((a, b) => provMap[b].total - provMap[a].total).slice(0, 10);
      const provLabels = sortedProvs;
      const windData = sortedProvs.map(pr => Math.round(provMap[pr].wind));
      const solarData = sortedProvs.map(pr => Math.round(provMap[pr].solar));
      const hydroData = sortedProvs.map(pr => Math.round(provMap[pr].hydro));
      const lngData = sortedProvs.map(pr => Math.round(provMap[pr].lng));
      const otherData = sortedProvs.map(pr => Math.round(provMap[pr].other));

      // Chart 1: Top 10 Provinces Horizontal Stacked Bar
      const ctxProv = document.getElementById('energyTopProvincesChart')?.getContext('2d');
      if (ctxProv) {
        if (energyTopProvChartInstance) energyTopProvChartInstance.destroy();
        energyTopProvChartInstance = new Chart(ctxProv, {
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
                  afterLabel: (ctx) => 'Click bar to filter table'
                }
              }
            },
            scales: {
              x: {
                stacked: true,
                grid: { color: gridColor },
                ticks: { color: textColor, font: { size: 10, family: 'monospace' }, callback: val => `${val} MW` }
              },
              y: {
                stacked: true,
                grid: { display: false },
                ticks: { color: textColor, font: { size: 10, weight: '600' } }
              }
            },
            onClick: (evt, elements) => {
              if (elements.length > 0) {
                const elem = elements[0];
                const selectedProv = provLabels[elem.index];
                const provSelect = document.getElementById('provinceSelect');
                if (provSelect) {
                  // Find matching option
                  for (let i = 0; i < provSelect.options.length; i++) {
                    if (provSelect.options[i].value.toLowerCase() === selectedProv.toLowerCase() ||
                        provSelect.options[i].text.toLowerCase().includes(selectedProv.toLowerCase())) {
                      provSelect.selectedIndex = i;
                      selectedProvince = provSelect.options[i].value;
                      break;
                    }
                  }
                  applyFilters();
                  document.getElementById('cockpitContainer')?.scrollIntoView({ behavior: 'smooth' });
                }
              }
            }
          }
        });
      }

      // Chart 2: Status Lifecycle Doughnut
      const ctxStatus = document.getElementById('energyStatusDoughnutChart')?.getContext('2d');
      if (ctxStatus) {
        if (energyStatusChartInstance) energyStatusChartInstance.destroy();
        const statusLabels = Object.keys(statusMap);
        const statusValues = Object.values(statusMap).map(v => Math.round(v));

        energyStatusChartInstance = new Chart(ctxStatus, {
          type: 'doughnut',
          data: {
            labels: statusLabels,
            datasets: [{
              data: statusValues,
              backgroundColor: ['#10B981', '#F59E0B', '#3B82F6', '#94A3B8'],
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
                  label: ctx => ` ${ctx.label}: ${ctx.raw.toLocaleString()} MW`
                }
              }
            },
            onClick: (evt, elements) => {
              if (elements.length > 0) {
                const elem = elements[0];
                const label = statusLabels[elem.index];
                const searchInput = document.getElementById('projectSearchInput');
                if (searchInput) {
                  searchInput.value = label.includes('COD') ? 'COD' : label;
                  searchQuery = searchInput.value.trim().toLowerCase();
                  applyFilters();
                  document.getElementById('cockpitContainer')?.scrollIntoView({ behavior: 'smooth' });
                }
              }
            }
          }
        });
      }
    }
"""

# Hook initEnergyCharts into loadProjectsData and theme switch
html = html.replace('initDirectory();', 'initDirectory();\n          initEnergyCharts();')
html = html.replace('applyTheme(!isDark);', 'applyTheme(!isDark);\n      initEnergyCharts();')

# Append the chart functions before the closing script tag
html = html.replace('// Initial Data Loading', chart_js_code + '\n      // Initial Data Loading')

# Save sequential revision
with open(rev3_file, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Created sequential revision: {rev3_file}")

with open(src_file, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Updated active file: {src_file}")
