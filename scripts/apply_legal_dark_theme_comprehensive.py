import re
import os

src_path = "RenewableVietNam/invm/index.html"
with open(src_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Pipeline Header Section
text = text.replace(
    '<section class="bg-white rounded-2xl p-4 sm:p-6 border border-slate-200/90 shadow-xs space-y-4">',
    '<section class="bg-white dark:bg-slate-800/80 rounded-2xl p-4 sm:p-6 border border-slate-200/90 dark:border-slate-700/60 shadow-xs space-y-4">'
)
text = text.replace(
    '<div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-3 border-b border-slate-100">',
    '<div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-3 border-b border-slate-100 dark:border-slate-700/60">'
)
text = text.replace(
    '<h3 id="pipelineHeaderTitle" class="text-sm sm:text-base font-extrabold text-slate-900 tracking-tight flex items-center gap-2">',
    '<h3 id="pipelineHeaderTitle" class="text-sm sm:text-base font-extrabold text-slate-900 dark:text-slate-100 tracking-tight flex items-center gap-2">'
)
text = text.replace(
    '<p id="pipelineHeaderSubtitle" class="text-xs text-slate-500">Standardized per Law on Investment 2020, Land Law 2024, Construction Law &amp; PDP8.</p>',
    '<p id="pipelineHeaderSubtitle" class="text-xs text-slate-500 dark:text-slate-400">Standardized per Law on Investment 2020, Land Law 2024, Construction Law &amp; PDP8.</p>'
)

# 2. Phase 1-6 Cards
text = re.sub(
    r'class="p-3\.5 rounded-xl border border-slate-200 (hover:border-[a-z]+-500) hover:shadow-md transition-all cursor-pointer group bg-slate-50/50 hover:bg-white flex flex-col justify-between"',
    r'class="p-3.5 rounded-xl border border-slate-200 dark:border-slate-700/70 \1 hover:shadow-md transition-all cursor-pointer group bg-slate-50/50 dark:bg-slate-800/50 hover:bg-white dark:hover:bg-slate-800 flex flex-col justify-between"',
    text
)
text = text.replace(
    'class="px-2 py-0.5 rounded-md bg-slate-200 text-slate-800 text-[10px] font-extrabold uppercase tracking-wider"',
    'class="px-2 py-0.5 rounded-md bg-slate-200 dark:bg-slate-700 text-slate-800 dark:text-slate-200 text-[10px] font-extrabold uppercase tracking-wider"'
)
for color in ['sky', 'orange', 'emerald', 'teal', 'indigo']:
    text = text.replace(
        f'class="px-2 py-0.5 rounded-md bg-{color}-100 text-{color}-800 text-[10px] font-extrabold uppercase tracking-wider"',
        f'class="px-2 py-0.5 rounded-md bg-{color}-100 dark:bg-{color}-950/60 text-{color}-800 dark:text-{color}-300 text-[10px] font-extrabold uppercase tracking-wider border border-{color}-200/60 dark:border-{color}-800/50"'
    )
text = re.sub(
    r'id="phase([1-6])Ratio" class="text-\[11px\] font-bold text-slate-600"',
    r'id="phase\1Ratio" class="text-[11px] font-bold text-slate-600 dark:text-slate-300"',
    text
)
text = text.replace(
    'class="my-2 px-2.5 py-1.5 rounded-lg bg-slate-100/90 border border-slate-200/90 flex items-center justify-between text-[11px]"',
    'class="my-2 px-2.5 py-1.5 rounded-lg bg-slate-100/90 dark:bg-slate-700/60 border border-slate-200/90 dark:border-slate-700/60 flex items-center justify-between text-[11px]"'
)
text = text.replace(
    'class="font-bold text-slate-700 flex items-center gap-1.5"',
    'class="font-bold text-slate-700 dark:text-slate-200 flex items-center gap-1.5"'
)
text = text.replace(
    'class="font-bold px-2 py-0.5 rounded text-[10px] bg-emerald-50 text-emerald-800 border border-emerald-200 shadow-2xs whitespace-nowrap"',
    'class="font-bold px-2 py-0.5 rounded text-[10px] bg-emerald-50 dark:bg-emerald-950/60 text-emerald-800 dark:text-emerald-300 border border-emerald-200 dark:border-emerald-800/50 shadow-2xs whitespace-nowrap"'
)
text = re.sub(
    r'id="phase([1-6])Title" class="text-xs font-bold text-slate-900',
    r'id="phase\1Title" class="text-xs font-bold text-slate-900 dark:text-slate-100',
    text
)
text = re.sub(
    r'id="phase([1-6])Desc" class="text-\[11px\] text-slate-500',
    r'id="phase\1Desc" class="text-[11px] text-slate-500 dark:text-slate-400',
    text
)
text = text.replace(
    'class="w-full bg-slate-200 h-1.5 rounded-full overflow-hidden"',
    'class="w-full bg-slate-200 dark:bg-slate-700 h-1.5 rounded-full overflow-hidden"'
)

# 3. KPI Risk Header & Button
text = text.replace(
    '<h2 id="kpiSectionTitle" class="text-xs sm:text-sm font-bold text-slate-900 uppercase tracking-wide">',
    '<h2 id="kpiSectionTitle" class="text-xs sm:text-sm font-bold text-slate-900 dark:text-slate-100 uppercase tracking-wide">'
)
text = text.replace(
    '<p id="kpiSectionSubtitle" class="text-[11px] text-slate-500">Risk matrix analysis and Critical Path Method (CPM) schedule.</p>',
    '<p id="kpiSectionSubtitle" class="text-[11px] text-slate-500 dark:text-slate-400">Risk matrix analysis and Critical Path Method (CPM) schedule.</p>'
)

# 4. KPI Cards
# cardTotal
text = text.replace(
    '<div id="cardTotal" class="col-span-2 sm:col-span-1 bg-white rounded-xl p-3 shadow-sm border border-slate-200/90 flex flex-col justify-between cursor-pointer hover:border-slate-400 hover:shadow-md transition group"',
    '<div id="cardTotal" class="col-span-2 sm:col-span-1 bg-white dark:bg-slate-800/90 rounded-xl p-3 shadow-sm border border-slate-200/90 dark:border-slate-700/70 flex flex-col justify-between cursor-pointer hover:border-slate-400 dark:hover:border-slate-500 hover:shadow-md transition group"'
)
text = text.replace(
    '<span id="kpiLabelTotal" class="text-[11px] font-semibold text-slate-500 uppercase tracking-wider group-hover:text-slate-800 truncate">',
    '<span id="kpiLabelTotal" class="text-[11px] font-semibold text-slate-500 dark:text-slate-400 uppercase tracking-wider group-hover:text-slate-800 dark:group-hover:text-slate-200 truncate">'
)
text = text.replace(
    '<div class="grid grid-cols-2 gap-2 mt-1.5 pt-1.5 border-t border-slate-100 items-baseline">',
    '<div class="grid grid-cols-2 gap-2 mt-1.5 pt-1.5 border-t border-slate-100 dark:border-slate-700/60 items-baseline">'
)
text = text.replace(
    '<h3 id="statTotal" class="text-2xl font-bold text-slate-900 leading-tight">',
    '<h3 id="statTotal" class="text-2xl font-bold text-slate-900 dark:text-slate-100 leading-tight">'
)
text = text.replace(
    '<div class="border-l border-slate-200/80 pl-2.5">',
    '<div class="border-l border-slate-200/80 dark:border-slate-700 pl-2.5">'
)
text = text.replace(
    '<h3 id="statSubItemsTotal" class="text-2xl font-bold text-slate-900 leading-tight">',
    '<h3 id="statSubItemsTotal" class="text-2xl font-bold text-slate-900 dark:text-slate-100 leading-tight">'
)

# cardPhases
text = text.replace(
    '<div id="cardPhases" class="bg-white rounded-xl p-3.5 shadow-sm border border-slate-200 flex flex-col justify-between cursor-pointer hover:border-slate-400 hover:shadow-md transition group"',
    '<div id="cardPhases" class="bg-white dark:bg-slate-800/90 rounded-xl p-3.5 shadow-sm border border-slate-200 dark:border-slate-700/70 flex flex-col justify-between cursor-pointer hover:border-slate-400 dark:hover:border-slate-500 hover:shadow-md transition group"'
)
text = text.replace(
    '<h3 id="statPhasesCount" class="text-2xl font-bold text-slate-900 leading-tight">',
    '<h3 id="statPhasesCount" class="text-2xl font-bold text-slate-900 dark:text-slate-100 leading-tight">'
)

# cardAuthorities
text = text.replace(
    '<div id="cardAuthorities" class="bg-white rounded-xl p-3.5 shadow-sm border border-slate-200 flex flex-col justify-between cursor-pointer hover:border-slate-400 hover:shadow-md transition group"',
    '<div id="cardAuthorities" class="bg-white dark:bg-slate-800/90 rounded-xl p-3.5 shadow-sm border border-slate-200 dark:border-slate-700/70 flex flex-col justify-between cursor-pointer hover:border-slate-400 dark:hover:border-slate-500 hover:shadow-md transition group"'
)
text = text.replace(
    '<h3 id="statAuthoritiesCount" class="text-2xl font-bold text-slate-900 leading-tight">',
    '<h3 id="statAuthoritiesCount" class="text-2xl font-bold text-slate-900 dark:text-slate-100 leading-tight">'
)

# cardCompleted
text = text.replace(
    '<div id="cardCompleted" class="bg-white rounded-xl p-3.5 shadow-sm border border-emerald-100 flex flex-col justify-between bg-gradient-to-br from-white to-emerald-50/40 cursor-pointer hover:border-emerald-300 hover:shadow-md transition group"',
    '<div id="cardCompleted" class="bg-white dark:bg-slate-800/90 rounded-xl p-3.5 shadow-sm border border-emerald-100 dark:border-emerald-900/50 flex flex-col justify-between bg-gradient-to-br from-white dark:from-slate-800 to-emerald-50/40 dark:to-emerald-950/30 cursor-pointer hover:border-emerald-300 dark:hover:border-emerald-600 hover:shadow-md transition group"'
)

# cardRemaining
text = text.replace(
    '<div id="cardRemaining" class="bg-white rounded-xl p-3.5 shadow-sm border border-amber-200/90 flex flex-col justify-between bg-gradient-to-br from-white to-amber-50/40 cursor-pointer hover:border-amber-400 hover:shadow-md transition group"',
    '<div id="cardRemaining" class="bg-white dark:bg-slate-800/90 rounded-xl p-3.5 shadow-sm border border-amber-200/90 dark:border-amber-900/50 flex flex-col justify-between bg-gradient-to-br from-white dark:from-slate-800 to-amber-50/40 dark:to-amber-950/30 cursor-pointer hover:border-amber-400 dark:hover:border-amber-600 hover:shadow-md transition group"'
)
text = text.replace(
    '<h3 id="statRemainingTasks" class="text-2xl font-bold text-slate-900">0</h3>',
    '<h3 id="statRemainingTasks" class="text-2xl font-bold text-slate-900 dark:text-slate-100">0</h3>'
)

# cardInProgress
text = text.replace(
    '<div id="cardInProgress" class="bg-white rounded-xl p-3.5 shadow-sm border border-blue-100 flex flex-col justify-between bg-gradient-to-br from-white to-blue-50/40 cursor-pointer hover:border-blue-300 hover:shadow-md transition group"',
    '<div id="cardInProgress" class="bg-white dark:bg-slate-800/90 rounded-xl p-3.5 shadow-sm border border-blue-100 dark:border-blue-900/50 flex flex-col justify-between bg-gradient-to-br from-white dark:from-slate-800 to-blue-50/40 dark:to-blue-950/30 cursor-pointer hover:border-blue-300 dark:hover:border-blue-600 hover:shadow-md transition group"'
)

# cardDelayed
text = text.replace(
    '<div id="cardDelayed" class="bg-white rounded-xl p-3.5 shadow-sm border border-rose-100 flex flex-col justify-between bg-gradient-to-br from-white to-rose-50/40 cursor-pointer hover:border-rose-300 hover:shadow-md transition group"',
    '<div id="cardDelayed" class="bg-white dark:bg-slate-800/90 rounded-xl p-3.5 shadow-sm border border-rose-100 dark:border-rose-900/50 flex flex-col justify-between bg-gradient-to-br from-white dark:from-slate-800 to-rose-50/40 dark:to-rose-950/30 cursor-pointer hover:border-rose-300 dark:hover:border-rose-600 hover:shadow-md transition group"'
)

# Overall Progress card (card 8)
text = text.replace(
    '<div class="bg-white rounded-xl p-3.5 shadow-sm border border-slate-200 flex flex-col justify-between">\n        <div class="flex items-center justify-between">\n          <span id="kpiLabelOverallProgress" class="text-[11px] font-semibold text-slate-500 uppercase tracking-wider">Progress</span>\n          <span id="statPercentBadge" class="text-[11px] font-bold px-2 py-0.5 rounded-full bg-blue-100 text-blue-800">0%</span>\n        </div>\n        <div class="w-full bg-slate-100 rounded-full h-2 mt-2 overflow-hidden">\n          <div id="statProgressBar" class="bg-blue-600 h-2 rounded-full transition-all duration-500" style="width: 0%"></div>\n        </div>\n      </div>',
    '<div class="bg-white dark:bg-slate-800/90 rounded-xl p-3.5 shadow-sm border border-slate-200 dark:border-slate-700/70 flex flex-col justify-between">\n        <div class="flex items-center justify-between">\n          <span id="kpiLabelOverallProgress" class="text-[11px] font-semibold text-slate-500 dark:text-slate-400 uppercase tracking-wider">Progress</span>\n          <span id="statPercentBadge" class="text-[11px] font-bold px-2 py-0.5 rounded-full bg-blue-100 dark:bg-blue-950/60 text-blue-800 dark:text-blue-300">0%</span>\n        </div>\n        <div class="w-full bg-slate-100 dark:bg-slate-700/60 rounded-full h-2 mt-2 overflow-hidden">\n          <div id="statProgressBar" class="bg-blue-600 dark:bg-blue-500 h-2 rounded-full transition-all duration-500" style="width: 0%"></div>\n        </div>\n      </div>'
)

# 5. Filter Toolbar Section
text = text.replace(
    '<section class="bg-white rounded-xl p-3.5 shadow-sm border border-slate-200 no-print flex flex-col md:flex-row items-stretch md:items-center justify-between gap-3">',
    '<section class="bg-white dark:bg-slate-800/90 rounded-xl p-3.5 shadow-sm border border-slate-200 dark:border-slate-700/70 no-print flex flex-col md:flex-row items-stretch md:items-center justify-between gap-3">'
)
text = text.replace(
    'class="w-full pl-10 pr-4 py-2 bg-slate-50 border border-slate-200 rounded-lg text-xs sm:text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:bg-white transition"',
    'class="w-full pl-10 pr-4 py-2 bg-slate-50 dark:bg-slate-900/70 border border-slate-200 dark:border-slate-700 text-slate-900 dark:text-slate-100 rounded-lg text-xs sm:text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:bg-white dark:focus:bg-slate-900 transition placeholder:text-slate-400"'
)
text = text.replace(
    'class="w-full md:w-72 py-2 px-2.5 bg-slate-50 border border-slate-200 rounded-lg text-xs text-slate-700 focus:outline-none focus:ring-2 focus:ring-slate-500 transition font-medium truncate"',
    'class="w-full md:w-72 py-2 px-2.5 bg-slate-50 dark:bg-slate-900/70 border border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-200 rounded-lg text-xs focus:outline-none focus:ring-2 focus:ring-slate-500 transition font-medium truncate"'
)
text = text.replace(
    'class="w-full md:w-44 py-2 px-2.5 bg-slate-50 border border-slate-200 rounded-lg text-xs text-slate-700 focus:outline-none focus:ring-2 focus:ring-slate-500 transition font-medium"',
    'class="w-full md:w-44 py-2 px-2.5 bg-slate-50 dark:bg-slate-900/70 border border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-200 rounded-lg text-xs focus:outline-none focus:ring-2 focus:ring-slate-500 transition font-medium"'
)

# Filter buttons
text = text.replace(
    'class="flex-1 sm:flex-none px-3 py-2 bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-semibold rounded-lg transition-colors flex items-center justify-center gap-1.5 border border-slate-200 shadow-2xs cursor-pointer"',
    'class="flex-1 sm:flex-none px-3 py-2 bg-slate-100 dark:bg-slate-700/80 hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 text-xs font-semibold rounded-lg transition-colors flex items-center justify-center gap-1.5 border border-slate-200 dark:border-slate-600 shadow-2xs cursor-pointer"'
)
text = text.replace(
    'class="flex-1 sm:flex-none px-3 py-2 bg-slate-900 hover:bg-black text-white text-xs font-bold rounded-lg transition-colors flex items-center justify-center gap-1.5 shadow-xs cursor-pointer"',
    'class="flex-1 sm:flex-none px-3 py-2 bg-slate-900 hover:bg-black dark:bg-blue-600 dark:hover:bg-blue-500 text-white text-xs font-bold rounded-lg transition-colors flex items-center justify-center gap-1.5 shadow-xs cursor-pointer"'
)

# 6. Table Section & Headings
text = text.replace(
    '<section class="hidden md:block w-full max-w-full bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden">',
    '<section class="hidden md:block w-full max-w-full bg-white dark:bg-slate-800/90 rounded-xl shadow-sm border border-slate-200 dark:border-slate-700/70 overflow-hidden">'
)
text = text.replace(
    '<thead class="bg-slate-100 border-b-2 border-slate-300">',
    '<thead class="bg-slate-100 dark:bg-slate-900/90 border-b-2 border-slate-300 dark:border-slate-700">'
)
text = text.replace(
    '<tr class="text-slate-800 font-bold uppercase tracking-wider text-[11px]">',
    '<tr class="text-slate-800 dark:text-slate-200 font-bold uppercase tracking-wider text-[11px]">'
)
text = text.replace(
    '<tbody id="checklistTableBody" class="divide-y divide-slate-200 text-slate-800">',
    '<tbody id="checklistTableBody" class="divide-y divide-slate-200 dark:divide-slate-700 text-slate-800 dark:text-slate-200">'
)
text = text.replace(
    'thColId" class="py-2.5 px-2 w-20 text-center border-r border-slate-200',
    'thColId" class="py-2.5 px-2 w-20 text-center border-r border-slate-200 dark:border-slate-700/80'
)
text = text.replace(
    'thColStatus" class="py-2.5 px-2 text-center w-36 min-w-[125px] border-r border-slate-200',
    'thColStatus" class="py-2.5 px-2 text-center w-36 min-w-[125px] border-r border-slate-200 dark:border-slate-700/80'
)
text = text.replace(
    'thColTitle" class="py-2.5 px-3 min-w-[240px] border-r border-slate-200',
    'thColTitle" class="py-2.5 px-3 min-w-[240px] border-r border-slate-200 dark:border-slate-700/80'
)
text = text.replace(
    'thColTimeline" class="py-2.5 px-2.5 min-w-[120px] border-r border-slate-200',
    'thColTimeline" class="py-2.5 px-2.5 min-w-[120px] border-r border-slate-200 dark:border-slate-700/80'
)
text = text.replace(
    'thColSubInputs" class="py-2.5 px-2 w-32 min-w-[115px] text-center border-r border-slate-200',
    'thColSubInputs" class="py-2.5 px-2 w-32 min-w-[115px] text-center border-r border-slate-200 dark:border-slate-700/80'
)
text = text.replace(
    'thColOutputs" class="py-2.5 px-3 min-w-[200px] border-r border-slate-200',
    'thColOutputs" class="py-2.5 px-3 min-w-[200px] border-r border-slate-200 dark:border-slate-700/80'
)
text = text.replace(
    'thColPic" class="py-2.5 px-2.5 w-24 border-r border-slate-200',
    'thColPic" class="py-2.5 px-2.5 w-24 border-r border-slate-200 dark:border-slate-700/80'
)

# 7. Dynamic Table Rendering (renderTable)
# phaseTr
old_phase_tr = """          const phaseTr = document.createElement('tr');
          phaseTr.className = 'bg-slate-100/95 border-y-2 border-slate-300 text-xs text-slate-800 no-print';
          phaseTr.innerHTML = `
            <td colspan="8" class="py-2.5 px-4 bg-slate-100/90">
              <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-1.5">
                <div class="flex items-center gap-2">
                  <span class="w-2.5 h-2.5 rounded-full bg-slate-800 shadow-xs"></span>
                  <span class="font-extrabold text-xs uppercase tracking-wider text-slate-900">${currentPhaseTracker === 'M&A & DD' ? (currentLang === 'en' ? 'M&A MODULE: DUE DILIGENCE &amp; TRANSACTION CLOSING' : 'KHỐI M&A: THẨM ĐỊNH CHUYÊN SÂU &amp; GIAO DỊCH DỰ ÁN (DD)') : escapeHtml(getLocalizedPhaseName(currentPhaseTracker))}</span>
                  <span class="text-[10.5px] font-semibold text-slate-600 bg-white px-2 py-0.5 rounded-md border border-slate-200 shadow-2xs">
                    ${phaseTasks.length} ${currentLang === 'en' ? 'Milestones' : 'thủ tục'}
                  </span>
                </div>
                <div class="text-[11px] text-slate-500 font-medium flex items-center gap-2">
                  <span>${currentPhaseTracker === 'M&A & DD' ? (currentLang === 'en' ? 'Due Diligence Progress:' : 'Tiến độ thẩm định & giao dịch:') : (currentLang === 'en' ? 'Stage Progress:' : 'Tiến độ giai đoạn:')}</span>
                  <span class="font-bold text-slate-800 bg-white px-2 py-0.5 rounded border border-slate-200 shadow-2xs">
                    ${phaseDone}/${phaseTasks.length} ${currentLang === 'en' ? 'Completed' : 'hoàn tất'} (${phasePct}%)
                  </span>
                </div>
              </div>
            </td>
          `;"""

new_phase_tr = """          const phaseTr = document.createElement('tr');
          phaseTr.className = 'bg-slate-100/95 dark:bg-slate-800/95 border-y-2 border-slate-300 dark:border-slate-700 text-xs text-slate-800 dark:text-slate-200 no-print';
          phaseTr.innerHTML = `
            <td colspan="8" class="py-2.5 px-4 bg-slate-100/90 dark:bg-slate-800/90">
              <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-1.5">
                <div class="flex items-center gap-2">
                  <span class="w-2.5 h-2.5 rounded-full bg-slate-800 dark:bg-slate-200 shadow-xs"></span>
                  <span class="font-extrabold text-xs uppercase tracking-wider text-slate-900 dark:text-slate-100">${currentPhaseTracker === 'M&A & DD' ? (currentLang === 'en' ? 'M&A MODULE: DUE DILIGENCE &amp; TRANSACTION CLOSING' : 'KHỐI M&A: THẨM ĐỊNH CHUYÊN SÂU &amp; GIAO DỊCH DỰ ÁN (DD)') : escapeHtml(getLocalizedPhaseName(currentPhaseTracker))}</span>
                  <span class="text-[10.5px] font-semibold text-slate-600 dark:text-slate-300 bg-white dark:bg-slate-700 px-2 py-0.5 rounded-md border border-slate-200 dark:border-slate-600 shadow-2xs">
                    ${phaseTasks.length} ${currentLang === 'en' ? 'Milestones' : 'thủ tục'}
                  </span>
                </div>
                <div class="text-[11px] text-slate-500 dark:text-slate-400 font-medium flex items-center gap-2">
                  <span>${currentPhaseTracker === 'M&A & DD' ? (currentLang === 'en' ? 'Due Diligence Progress:' : 'Tiến độ thẩm định & giao dịch:') : (currentLang === 'en' ? 'Stage Progress:' : 'Tiến độ giai đoạn:')}</span>
                  <span class="font-bold text-slate-800 dark:text-slate-200 bg-white dark:bg-slate-700 px-2 py-0.5 rounded border border-slate-200 dark:border-slate-600 shadow-2xs">
                    ${phaseDone}/${phaseTasks.length} ${currentLang === 'en' ? 'Completed' : 'hoàn tất'} (${phasePct}%)
                  </span>
                </div>
              </div>
            </td>
          `;"""

if old_phase_tr in text:
    text = text.replace(old_phase_tr, new_phase_tr)
    print("Replaced phaseTr")

# Task rowBg
old_task_rowbg = """        let rowBg = 'hover:bg-slate-50/80 transition-colors';
        if (isCompleted) {
          rowBg = 'bg-emerald-50/20 hover:bg-emerald-50/35';
        } else if (isDelayed) {
          rowBg = 'bg-rose-50/25 hover:bg-rose-50/40';
        }
        tr.id = `task-row-${task.id}`;
        tr.className = `${rowBg} border-b border-slate-200/80 transition-all duration-200`;"""

new_task_rowbg = """        let rowBg = 'hover:bg-slate-50/80 dark:hover:bg-slate-800/60 transition-colors';
        if (isCompleted) {
          rowBg = 'bg-emerald-50/20 dark:bg-emerald-950/20 hover:bg-emerald-50/35 dark:hover:bg-emerald-950/35';
        } else if (isDelayed) {
          rowBg = 'bg-rose-50/25 dark:bg-rose-950/25 hover:bg-rose-50/40 dark:hover:bg-rose-950/40';
        }
        tr.id = `task-row-${task.id}`;
        tr.className = `${rowBg} border-b border-slate-200/80 dark:border-slate-700/70 transition-all duration-200 text-slate-800 dark:text-slate-200`;"""

if old_task_rowbg in text:
    text = text.replace(old_task_rowbg, new_task_rowbg)
    print("Replaced task rowBg")

text = text.replace(
    'align-middle text-center border-r border-slate-200',
    'align-middle text-center border-r border-slate-200 dark:border-slate-700/70'
)
text = text.replace(
    'align-middle border-r border-slate-200',
    'align-middle border-r border-slate-200 dark:border-slate-700/70'
)

old_task_title = """<div class="font-bold text-slate-900 text-xs sm:text-[12.5px] leading-snug group-hover/title:text-blue-600 transition-colors ${isCompleted ? 'line-through text-slate-400' : ''}">"""
new_task_title = """<div class="font-bold text-slate-900 dark:text-slate-100 text-xs sm:text-[12.5px] leading-snug group-hover/title:text-blue-600 dark:group-hover/title:text-blue-400 transition-colors ${isCompleted ? 'line-through text-slate-400 dark:text-slate-500' : ''}">"""
text = text.replace(old_task_title, new_task_title)

# Detail Drawer (detailTr)
old_detail_tr = """          const detailTr = document.createElement('tr');
          detailTr.id = `detail-drawer-${task.id}`;
          detailTr.className = 'detail-drawer bg-slate-100/90 border-b border-slate-300/80 text-xs animate-in fade-in duration-150';"""

new_detail_tr = """          const detailTr = document.createElement('tr');
          detailTr.id = `detail-drawer-${task.id}`;
          detailTr.className = 'detail-drawer bg-slate-100/90 dark:bg-slate-900/95 border-b border-slate-300/80 dark:border-slate-700/80 text-xs animate-in fade-in duration-150';"""
text = text.replace(old_detail_tr, new_detail_tr)

text = text.replace(
    '<td colspan="8" class="p-4 bg-slate-50/70 border-y border-slate-200 shadow-inner">',
    '<td colspan="8" class="p-4 bg-slate-50/70 dark:bg-slate-900/90 border-y border-slate-200 dark:border-slate-700/80 shadow-inner">'
)
text = text.replace(
    '<div class="lg:col-span-5 bg-white p-3.5 rounded-xl border border-slate-200 shadow-2xs flex flex-col justify-between">',
    '<div class="lg:col-span-5 bg-white dark:bg-slate-800 p-3.5 rounded-xl border border-slate-200 dark:border-slate-700 shadow-2xs flex flex-col justify-between">'
)
text = text.replace(
    '<div class="lg:col-span-4 bg-white p-3.5 rounded-xl border border-slate-200 shadow-2xs flex flex-col justify-between">',
    '<div class="lg:col-span-4 bg-white dark:bg-slate-800 p-3.5 rounded-xl border border-slate-200 dark:border-slate-700 shadow-2xs flex flex-col justify-between">'
)
text = text.replace(
    '<div class="lg:col-span-3 bg-white p-3.5 rounded-xl border border-slate-200 shadow-2xs flex flex-col justify-between">',
    '<div class="lg:col-span-3 bg-white dark:bg-slate-800 p-3.5 rounded-xl border border-slate-200 dark:border-slate-700 shadow-2xs flex flex-col justify-between">'
)
text = text.replace(
    '<h4 class="font-bold text-slate-900 text-xs uppercase tracking-wide">',
    '<h4 class="font-bold text-slate-900 dark:text-slate-100 text-xs uppercase tracking-wide">'
)
text = text.replace(
    'hover:bg-white cursor-pointer transition select-none border border-transparent hover:border-slate-200',
    'hover:bg-white dark:hover:bg-slate-700/60 cursor-pointer transition select-none border border-transparent hover:border-slate-200 dark:hover:border-slate-600'
)
text = text.replace(
    'text-slate-800 font-medium group-hover:text-blue-900',
    'text-slate-800 dark:text-slate-200 font-medium group-hover:text-blue-900 dark:group-hover:text-blue-400'
)
text = text.replace(
    'bg-blue-50/60 border border-blue-200/80 p-2.5 rounded-lg text-blue-950 leading-relaxed font-normal shadow-2xs flex flex-col gap-1',
    'bg-blue-50/60 dark:bg-blue-950/40 border border-blue-200/80 dark:border-blue-800/60 p-2.5 rounded-lg text-blue-950 dark:text-blue-200 leading-relaxed font-normal shadow-2xs flex flex-col gap-1'
)
text = text.replace(
    'bg-slate-50 border border-slate-200 p-2.5 rounded-lg text-slate-800 leading-relaxed font-medium shadow-2xs',
    'bg-slate-50 dark:bg-slate-900/60 border border-slate-200 dark:border-slate-700 p-2.5 rounded-lg text-slate-800 dark:text-slate-200 leading-relaxed font-medium shadow-2xs'
)
text = text.replace(
    'bg-amber-50/60 border border-amber-200/80 p-2.5 rounded-lg text-amber-950 leading-relaxed shadow-2xs text-[11.5px]',
    'bg-amber-50/60 dark:bg-amber-950/40 border border-amber-200/80 dark:border-amber-800/60 p-2.5 rounded-lg text-amber-950 dark:text-amber-200 leading-relaxed shadow-2xs text-[11.5px]'
)

# 8. Modals
text = text.replace(
    '<div class="bg-white border border-slate-200 rounded-2xl w-full max-w-md shadow-2xl p-6 text-slate-800 animate-in fade-in zoom-in-95 duration-200">',
    '<div class="bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-2xl w-full max-w-md shadow-2xl p-6 text-slate-800 dark:text-slate-200 animate-in fade-in zoom-in-95 duration-200">'
)
text = text.replace(
    '<div class="bg-white rounded-2xl shadow-2xl max-w-2xl w-full max-h-[90vh] overflow-y-auto border border-slate-200 animate-in fade-in zoom-in-95 duration-200 p-6 text-slate-800">',
    '<div class="bg-white dark:bg-slate-800 rounded-2xl shadow-2xl max-w-2xl w-full max-h-[90vh] overflow-y-auto border border-slate-200 dark:border-slate-700 animate-in fade-in zoom-in-95 duration-200 p-6 text-slate-800 dark:text-slate-200">'
)
text = text.replace(
    '<div class="bg-white rounded-2xl shadow-2xl max-w-md w-full border border-slate-200 animate-in fade-in zoom-in-95 duration-200 p-6 text-slate-800">',
    '<div class="bg-white dark:bg-slate-800 rounded-2xl shadow-2xl max-w-md w-full border border-slate-200 dark:border-slate-700 animate-in fade-in zoom-in-95 duration-200 p-6 text-slate-800 dark:text-slate-200">'
)

# 9. Gantt Modal
text = text.replace(
    '<div class="w-full h-full flex flex-col overflow-hidden bg-white text-slate-800">',
    '<div class="w-full h-full flex flex-col overflow-hidden bg-white dark:bg-slate-900 text-slate-800 dark:text-slate-200">'
)
text = text.replace(
    '<div class="px-5 py-2.5 border-b border-slate-200 bg-white flex flex-wrap items-center justify-between gap-3 shadow-xs">',
    '<div class="px-5 py-2.5 border-b border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 flex flex-wrap items-center justify-between gap-3 shadow-xs">'
)
text = text.replace(
    '<h2 class="text-xs sm:text-sm font-bold text-slate-900 uppercase tracking-wide">Project Schedule &amp; CPM Gantt</h2>',
    '<h2 class="text-xs sm:text-sm font-bold text-slate-900 dark:text-slate-100 uppercase tracking-wide">Project Schedule &amp; CPM Gantt</h2>'
)
text = text.replace(
    '<span id="ganttProjectBadge" class="px-2 py-0.5 text-xs rounded-md bg-slate-100 text-slate-700 border border-slate-200 font-semibold font-mono">Project</span>',
    '<span id="ganttProjectBadge" class="px-2 py-0.5 text-xs rounded-md bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-700 font-semibold font-mono">Project</span>'
)
text = text.replace(
    '<span id="ganttActiveProjectTypeBadge" class="px-2 py-0.5 text-xs rounded-md bg-blue-50 text-blue-700 border border-blue-200 font-semibold">Urban</span>',
    '<span id="ganttActiveProjectTypeBadge" class="px-2 py-0.5 text-xs rounded-md bg-blue-50 dark:bg-blue-950/60 text-blue-700 dark:text-blue-300 border border-blue-200 dark:border-blue-800/60 font-semibold">Urban</span>'
)
text = text.replace(
    'class="bg-white border border-slate-300 rounded-md px-2 py-1 text-xs text-slate-700 font-mono shadow-2xs focus:ring-1 focus:ring-blue-500"',
    'class="bg-white dark:bg-slate-800 border border-slate-300 dark:border-slate-700 rounded-md px-2 py-1 text-xs text-slate-700 dark:text-slate-200 font-mono shadow-2xs focus:ring-1 focus:ring-blue-500"'
)
text = text.replace(
    'class="bg-white border border-slate-300 rounded-md px-2 py-1 text-xs text-slate-700 font-semibold shadow-2xs focus:ring-1 focus:ring-blue-500 cursor-pointer"',
    'class="bg-white dark:bg-slate-800 border border-slate-300 dark:border-slate-700 rounded-md px-2 py-1 text-xs text-slate-700 dark:text-slate-200 font-semibold shadow-2xs focus:ring-1 focus:ring-blue-500 cursor-pointer"'
)
text = text.replace(
    '<div class="px-5 py-2 bg-slate-50 border-b border-slate-200 grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3 text-xs">',
    '<div class="px-5 py-2 bg-slate-50 dark:bg-slate-800/60 border-b border-slate-200 dark:border-slate-800 grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3 text-xs">'
)

# 10. Gantt Time Axis & Grid
old_gantt_time_axis = """      let timeAxisHtml = `
        <div class="grid items-stretch border-b-2 border-slate-300 bg-slate-100 py-1.5 sticky top-0 z-30 shadow-xs" style="grid-template-columns: 440px 1fr;">
          <div class="text-xs font-black text-slate-700 pl-3 pr-3 uppercase flex items-center border-r-2 border-slate-300">${currentLang === 'en' ? 'Statutory Milestone &amp; Schedule' : 'Thủ Tục Pháp Lý &amp; Tiến Độ'}</div>
          <div class="relative h-8 flex items-center pr-2">
            <div class="absolute inset-0 flex border-l border-r border-t border-b border-slate-300 rounded-t bg-slate-200/90 overflow-hidden">
      `;
      for (let q = 0; q < totalQuarters; q++) {
        const qDate = new Date(startEpoch + q * 91.25 * 86400000);
        const qNum = Math.floor(qDate.getMonth() / 3) + 1;
        const qYear = String(qDate.getFullYear()).slice(2);
        const isAlt = q % 2 === 1;
        timeAxisHtml += `<div class="flex-1 text-center flex items-center justify-center border-r last:border-r-0 border-slate-300 font-mono text-slate-800 font-extrabold text-xs ${isAlt ? 'bg-slate-200/80' : 'bg-slate-100'}">Q${qNum}/${qYear}</div>`;
      }"""

new_gantt_time_axis = """      let timeAxisHtml = `
        <div class="grid items-stretch border-b-2 border-slate-300 dark:border-slate-700 bg-slate-100 dark:bg-slate-800 py-1.5 sticky top-0 z-30 shadow-xs" style="grid-template-columns: 440px 1fr;">
          <div class="text-xs font-black text-slate-700 dark:text-slate-200 pl-3 pr-3 uppercase flex items-center border-r-2 border-slate-300 dark:border-slate-700">${currentLang === 'en' ? 'Statutory Milestone &amp; Schedule' : 'Thủ Tục Pháp Lý &amp; Tiến Độ'}</div>
          <div class="relative h-8 flex items-center pr-2">
            <div class="absolute inset-0 flex border-l border-r border-t border-b border-slate-300 dark:border-slate-700 rounded-t bg-slate-200/90 dark:bg-slate-750 overflow-hidden">
      `;
      for (let q = 0; q < totalQuarters; q++) {
        const qDate = new Date(startEpoch + q * 91.25 * 86400000);
        const qNum = Math.floor(qDate.getMonth() / 3) + 1;
        const qYear = String(qDate.getFullYear()).slice(2);
        const isAlt = q % 2 === 1;
        timeAxisHtml += `<div class="flex-1 text-center flex items-center justify-center border-r last:border-r-0 border-slate-300 dark:border-slate-700 font-mono text-slate-800 dark:text-slate-200 font-extrabold text-xs ${isAlt ? 'bg-slate-200/80 dark:bg-slate-700/80' : 'bg-slate-100 dark:bg-slate-800'}">Q${qNum}/${qYear}</div>`;
      }"""

if old_gantt_time_axis in text:
    text = text.replace(old_gantt_time_axis, new_gantt_time_axis)
    print("Replaced Gantt Time Axis")

old_gantt_grid = """      // Reusable Vertical Gridlines Generator for Each Row (Continuous Full-Height Grid Lines with Alternating Lanes)
      let gridColsHtml = '<div class="absolute inset-0 flex border-r border-slate-300 pointer-events-none">';
      for (let q = 0; q < totalQuarters; q++) {
        const isAlt = q % 2 === 1;
        gridColsHtml += `<div class="flex-1 border-r last:border-r-0 border-slate-300 h-full ${isAlt ? 'bg-slate-100/50' : 'bg-white'}"></div>`;
      }
      gridColsHtml += '</div>';"""

new_gantt_grid = """      // Reusable Vertical Gridlines Generator for Each Row (Continuous Full-Height Grid Lines with Alternating Lanes)
      let gridColsHtml = '<div class="absolute inset-0 flex border-r border-slate-300 dark:border-slate-700 pointer-events-none">';
      for (let q = 0; q < totalQuarters; q++) {
        const isAlt = q % 2 === 1;
        gridColsHtml += `<div class="flex-1 border-r last:border-r-0 border-slate-300 dark:border-slate-700 h-full ${isAlt ? 'bg-slate-100/50 dark:bg-slate-800/40' : 'bg-white dark:bg-slate-900'}"></div>`;
      }
      gridColsHtml += '</div>';"""

if old_gantt_grid in text:
    text = text.replace(old_gantt_grid, new_gantt_grid)
    print("Replaced Gantt Grid Generator")

text = text.replace(
    'class="px-3 py-1.5 bg-slate-100 border-b border-slate-300 font-bold text-xs uppercase text-slate-800 flex items-center justify-between sticky left-0 z-20"',
    'class="px-3 py-1.5 bg-slate-100 dark:bg-slate-800 border-b border-slate-300 dark:border-slate-700 font-bold text-xs uppercase text-slate-800 dark:text-slate-200 flex items-center justify-between sticky left-0 z-20"'
)
text = text.replace(
    'class="grid items-center border-b border-slate-200 hover:bg-slate-50 transition-colors relative" style="grid-template-columns: 440px 1fr;"',
    'class="grid items-center border-b border-slate-200 dark:border-slate-800 hover:bg-slate-50 dark:hover:bg-slate-800/60 transition-colors relative" style="grid-template-columns: 440px 1fr;"'
)
text = text.replace(
    'class="text-xs font-semibold text-slate-900 truncate leading-snug',
    'class="text-xs font-semibold text-slate-900 dark:text-slate-100 truncate leading-snug'
)

# 11. Theme Toggle Script (Re-render Table and Gantt on theme change)
old_theme_script = """    themeBtn?.addEventListener('click', function() {
      const isDark = document.documentElement.classList.contains('dark');
      if (isDark) {
        document.documentElement.classList.remove('dark');
        localStorage.setItem('rvn_theme_v2', 'light');
      } else {
        document.documentElement.classList.add('dark');
        localStorage.setItem('rvn_theme_v2', 'dark');
      }
      updateIcons();
    });"""

new_theme_script = """    themeBtn?.addEventListener('click', function() {
      const isDark = document.documentElement.classList.contains('dark');
      if (isDark) {
        document.documentElement.classList.remove('dark');
        localStorage.setItem('rvn_theme_v2', 'light');
      } else {
        document.documentElement.classList.add('dark');
        localStorage.setItem('rvn_theme_v2', 'dark');
      }
      updateIcons();
      if (typeof renderTable === 'function') renderTable();
      const ganttModalEl = document.getElementById('ganttModal');
      if (ganttModalEl && !ganttModalEl.classList.contains('hidden') && typeof renderGanttView === 'function') {
        renderGanttView();
      }
    });"""

if old_theme_script in text:
    text = text.replace(old_theme_script, new_theme_script)
    print("Replaced Theme Toggle Script")

# Write out index_Rev.036.html
rev_path = "RenewableVietNam/invm/index_Rev.036.html"
with open(rev_path, "w", encoding="utf-8") as f:
    f.write(text)

print(f"Successfully generated {rev_path} ({len(text)} bytes)")
