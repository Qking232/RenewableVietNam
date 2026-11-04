import re
import os

src_path = "RenewableVietNam/invm/index.html"
with open(src_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Stage 1-6 Outer Card Container
text = re.sub(
    r'(<div onclick="filterByPhaseAndSwitch\(\'Giai đoạn [1-6]\'\)" class="p-3\.5 rounded-xl border border-slate-200 hover:border-[a-z]+-500 hover:shadow-md transition cursor-pointer )bg-slate-50/50 hover:bg-white( group">)',
    r'\1bg-slate-50/50 dark:bg-slate-800/80 hover:bg-white dark:hover:bg-slate-750 border-slate-200 dark:border-slate-700/80\2',
    text
)

# 2. Stage 1-6 Middle CPM Strip Container
text = text.replace(
    'class="my-2 px-2.5 py-1.5 rounded-lg bg-slate-100/90 border border-slate-200/90 flex items-center justify-between gap-1 text-[10.5px]"',
    'class="my-2 px-2.5 py-1.5 rounded-lg bg-slate-100/90 dark:bg-slate-750/90 border border-slate-200/90 dark:border-slate-700/70 flex items-center justify-between gap-1 text-[10.5px]"'
)

# 3. Stage 1-6 CPM Status Badges
text = text.replace(
    'class="font-bold px-2 py-0.5 rounded text-[10px] bg-emerald-50 text-emerald-700 border border-emerald-200 whitespace-nowrap"',
    'class="font-bold px-2 py-0.5 rounded text-[10px] bg-emerald-50 dark:bg-emerald-950/70 text-emerald-700 dark:text-emerald-300 border border-emerald-200 dark:border-emerald-800/60 whitespace-nowrap"'
)

# 4. Stage 1-6 Description Text Contrast Enhancement
text = text.replace(
    'text-[11px] text-slate-500 dark:text-slate-400 mb-3 line-clamp-2',
    'text-[11px] text-slate-500 dark:text-slate-300 mb-3 line-clamp-2'
)

# 5. KPI Card 4: cardCompleted
old_card_completed = """      <!-- Đã hoàn thành -->
      <div id="cardCompleted" class="bg-white rounded-xl p-3.5 shadow-sm border border-emerald-100 flex flex-col justify-between bg-gradient-to-br from-white to-emerald-50/30 cursor-pointer hover:border-emerald-300 hover:shadow-md transition group" title="Bấm để lọc các thủ tục đã hoàn thành">
        <span id="kpiLabelCompleted" class="text-[11px] font-semibold text-emerald-600 uppercase tracking-wider group-hover:text-emerald-800">Approved &amp; Completed</span>
        <div class="flex items-baseline justify-between mt-1">
          <h3 id="statCompleted" class="text-2xl font-bold text-emerald-700">0</h3>
          <span class="p-1.5 bg-emerald-100 rounded-lg text-emerald-600 group-hover:bg-emerald-200 transition"><i data-lucide="check-circle-2" class="w-4 h-4"></i></span>
        </div>
      </div>"""

new_card_completed = """      <!-- Đã hoàn thành -->
      <div id="cardCompleted" class="bg-white dark:bg-slate-800/90 rounded-xl p-3.5 shadow-sm border border-emerald-100 dark:border-emerald-900/50 flex flex-col justify-between bg-gradient-to-br from-white dark:from-slate-800 to-emerald-50/30 dark:to-emerald-950/30 cursor-pointer hover:border-emerald-300 dark:hover:border-emerald-600 hover:shadow-md transition group" title="Bấm để lọc các thủ tục đã hoàn thành">
        <span id="kpiLabelCompleted" class="text-[11px] font-semibold text-emerald-600 dark:text-emerald-400 uppercase tracking-wider group-hover:text-emerald-800 dark:group-hover:text-emerald-300">Approved &amp; Completed</span>
        <div class="flex items-baseline justify-between mt-1">
          <h3 id="statCompleted" class="text-2xl font-bold text-emerald-700 dark:text-emerald-400">0</h3>
          <span class="p-1.5 bg-emerald-100 dark:bg-emerald-950/70 rounded-lg text-emerald-600 dark:text-emerald-400 group-hover:bg-emerald-200 dark:group-hover:bg-emerald-900/60 transition"><i data-lucide="check-circle-2" class="w-4 h-4"></i></span>
        </div>
      </div>"""

if old_card_completed in text:
    text = text.replace(old_card_completed, new_card_completed)
    print("Replaced cardCompleted")
else:
    print("Warning: old_card_completed not found verbatim")

# 6. KPI Card 5: cardRemaining
old_card_remaining = """      <!-- Thủ tục pháp lý còn lại -->
      <div id="cardRemaining" class="bg-white rounded-xl p-3.5 shadow-sm border border-amber-200/90 flex flex-col justify-between bg-gradient-to-br from-white to-amber-50/30 cursor-pointer hover:border-amber-400 hover:shadow-md transition group" title="Bấm để lọc các thủ tục pháp lý còn lại (chưa hoàn thành)">
        <span id="kpiLabelRemaining" class="text-[11px] font-semibold text-amber-700 uppercase tracking-wider group-hover:text-amber-900 truncate">Pending Approvals</span>
        <div class="flex items-baseline justify-between mt-1">
          <h3 id="statRemaining" class="text-2xl font-bold text-amber-700">0</h3>
          <span class="p-1.5 bg-amber-100 rounded-lg text-amber-600 group-hover:bg-amber-200 transition">
            <i data-lucide="list-todo" class="w-4 h-4"></i>
          </span>
        </div>
      </div>"""

new_card_remaining = """      <!-- Thủ tục pháp lý còn lại -->
      <div id="cardRemaining" class="bg-white dark:bg-slate-800/90 rounded-xl p-3.5 shadow-sm border border-amber-200/90 dark:border-amber-900/50 flex flex-col justify-between bg-gradient-to-br from-white dark:from-slate-800 to-amber-50/30 dark:to-amber-950/30 cursor-pointer hover:border-amber-400 dark:hover:border-amber-600 hover:shadow-md transition group" title="Bấm để lọc các thủ tục pháp lý còn lại (chưa hoàn thành)">
        <span id="kpiLabelRemaining" class="text-[11px] font-semibold text-amber-700 dark:text-amber-400 uppercase tracking-wider group-hover:text-amber-900 dark:group-hover:text-amber-300 truncate">Pending Approvals</span>
        <div class="flex items-baseline justify-between mt-1">
          <h3 id="statRemaining" class="text-2xl font-bold text-amber-700 dark:text-amber-400">0</h3>
          <span class="p-1.5 bg-amber-100 dark:bg-amber-950/70 rounded-lg text-amber-600 dark:text-amber-400 group-hover:bg-amber-200 dark:group-hover:bg-amber-900/60 transition">
            <i data-lucide="list-todo" class="w-4 h-4"></i>
          </span>
        </div>
      </div>"""

if old_card_remaining in text:
    text = text.replace(old_card_remaining, new_card_remaining)
    print("Replaced cardRemaining")
else:
    print("Warning: old_card_remaining not found verbatim")

# 7. KPI Card 6: cardInProgress
old_card_in_progress = """      <!-- Đang xử lý -->
      <div id="cardInProgress" class="bg-white rounded-xl p-3.5 shadow-sm border border-blue-100 flex flex-col justify-between bg-gradient-to-br from-white to-blue-50/30 cursor-pointer hover:border-blue-300 hover:shadow-md transition group" title="Bấm để lọc các thủ tục đang xử lý">
        <span id="kpiLabelInProgress" class="text-[11px] font-semibold text-blue-600 uppercase tracking-wider group-hover:text-blue-800">Under Statutory Review</span>
        <div class="flex items-baseline justify-between mt-1">
          <h3 id="statInProgress" class="text-2xl font-bold text-blue-700">0</h3>
          <span class="p-1.5 bg-blue-100 rounded-lg text-blue-600 group-hover:bg-blue-200 transition"><i data-lucide="timer" class="w-4 h-4"></i></span>
        </div>
      </div>"""

new_card_in_progress = """      <!-- Đang xử lý -->
      <div id="cardInProgress" class="bg-white dark:bg-slate-800/90 rounded-xl p-3.5 shadow-sm border border-blue-100 dark:border-blue-900/50 flex flex-col justify-between bg-gradient-to-br from-white dark:from-slate-800 to-blue-50/30 dark:to-blue-950/30 cursor-pointer hover:border-blue-300 dark:hover:border-blue-600 hover:shadow-md transition group" title="Bấm để lọc các thủ tục đang xử lý">
        <span id="kpiLabelInProgress" class="text-[11px] font-semibold text-blue-600 dark:text-blue-400 uppercase tracking-wider group-hover:text-blue-800 dark:group-hover:text-blue-300">Under Statutory Review</span>
        <div class="flex items-baseline justify-between mt-1">
          <h3 id="statInProgress" class="text-2xl font-bold text-blue-700 dark:text-blue-400">0</h3>
          <span class="p-1.5 bg-blue-100 dark:bg-blue-950/70 rounded-lg text-blue-600 dark:text-blue-400 group-hover:bg-blue-200 dark:group-hover:bg-blue-900/60 transition"><i data-lucide="timer" class="w-4 h-4"></i></span>
        </div>
      </div>"""

if old_card_in_progress in text:
    text = text.replace(old_card_in_progress, new_card_in_progress)
    print("Replaced cardInProgress")
else:
    print("Warning: old_card_in_progress not found verbatim")

# 8. KPI Card 7: cardDelayed
old_card_delayed = """      <!-- Chậm trễ / Điểm nghẽn -->
      <div id="cardDelayed" class="bg-white rounded-xl p-3.5 shadow-sm border border-rose-100 flex flex-col justify-between bg-gradient-to-br from-white to-rose-50/30 cursor-pointer hover:border-rose-300 hover:shadow-md transition group" title="Bấm để lọc các thủ tục bị nghẽn/trễ hạn">
        <span id="kpiLabelDelayed" class="text-[11px] font-semibold text-rose-600 uppercase tracking-wider group-hover:text-rose-800">Schedule Bottlenecks / Warning</span>
        <div class="flex items-baseline justify-between mt-1">
          <h3 id="statDelayed" class="text-2xl font-bold text-rose-700">0</h3>
          <span class="p-1.5 bg-rose-100 rounded-lg text-rose-600 group-hover:bg-rose-200 transition"><i data-lucide="alert-triangle" class="w-4 h-4"></i></span>
        </div>
      </div>"""

new_card_delayed = """      <!-- Chậm trễ / Điểm nghẽn -->
      <div id="cardDelayed" class="bg-white dark:bg-slate-800/90 rounded-xl p-3.5 shadow-sm border border-rose-100 dark:border-rose-900/50 flex flex-col justify-between bg-gradient-to-br from-white dark:from-slate-800 to-rose-50/30 dark:to-rose-950/30 cursor-pointer hover:border-rose-300 dark:hover:border-rose-600 hover:shadow-md transition group" title="Bấm để lọc các thủ tục bị nghẽn/trễ hạn">
        <span id="kpiLabelDelayed" class="text-[11px] font-semibold text-rose-600 dark:text-rose-400 uppercase tracking-wider group-hover:text-rose-800 dark:group-hover:text-rose-300">Schedule Bottlenecks / Warning</span>
        <div class="flex items-baseline justify-between mt-1">
          <h3 id="statDelayed" class="text-2xl font-bold text-rose-700 dark:text-rose-400">0</h3>
          <span class="p-1.5 bg-rose-100 dark:bg-rose-950/70 rounded-lg text-rose-600 dark:text-rose-400 group-hover:bg-rose-200 dark:group-hover:bg-rose-900/60 transition"><i data-lucide="alert-triangle" class="w-4 h-4"></i></span>
        </div>
      </div>"""

if old_card_delayed in text:
    text = text.replace(old_card_delayed, new_card_delayed)
    print("Replaced cardDelayed")
else:
    print("Warning: old_card_delayed not found verbatim")

# 9. KPI Card 8: Overall Progress
old_card_overall = """      <!-- Tiến độ chung -->
      <div class="bg-white rounded-xl p-3.5 shadow-sm border border-slate-200 flex flex-col justify-between">
        <div class="flex items-center justify-between">
          <span id="kpiLabelOverallProgress" class="text-[11px] font-semibold text-slate-500 uppercase tracking-wider">OVERALL STATUTORY PROGRESS</span>
          <span id="statPercentBadge" class="text-[11px] font-bold px-2 py-0.5 rounded-full bg-blue-100 text-blue-800">0%</span>
        </div>
        <div class="w-full bg-slate-100 rounded-full h-2 mt-2 overflow-hidden">
          <div id="statProgressBar" class="bg-blue-600 h-2 rounded-full transition-all duration-500" style="width: 0%"></div>
        </div>
      </div>"""

new_card_overall = """      <!-- Tiến độ chung -->
      <div class="bg-white dark:bg-slate-800/90 rounded-xl p-3.5 shadow-sm border border-slate-200 dark:border-slate-700/70 flex flex-col justify-between">
        <div class="flex items-center justify-between">
          <span id="kpiLabelOverallProgress" class="text-[11px] font-semibold text-slate-500 dark:text-slate-400 uppercase tracking-wider">OVERALL STATUTORY PROGRESS</span>
          <span id="statPercentBadge" class="text-[11px] font-bold px-2 py-0.5 rounded-full bg-blue-100 dark:bg-blue-950/70 text-blue-800 dark:text-blue-300">0%</span>
        </div>
        <div class="w-full bg-slate-100 dark:bg-slate-700/60 rounded-full h-2 mt-2 overflow-hidden">
          <div id="statProgressBar" class="bg-blue-600 dark:bg-blue-500 h-2 rounded-full transition-all duration-500" style="width: 0%"></div>
        </div>
      </div>"""

if old_card_overall in text:
    text = text.replace(old_card_overall, new_card_overall)
    print("Replaced cardOverall")
else:
    print("Warning: old_card_overall not found verbatim")

# 10. Buttons: btnDensityToggle & btnToggleAllDrawers
old_btn_density = """        <button id="btnDensityToggle" class="justify-center px-2 py-2 bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-semibold rounded-lg transition whitespace-nowrap flex items-center gap-1" title="Toggle compact / comfortable density">
          <i data-lucide="unfold-vertical" class="w-3.5 h-3.5"></i> <span id="densityToggleText">Compact</span>
        </button>"""

new_btn_density = """        <button id="btnDensityToggle" class="justify-center px-2 py-2 bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 border border-slate-200 dark:border-slate-700 text-xs font-semibold rounded-lg transition whitespace-nowrap flex items-center gap-1 cursor-pointer" title="Toggle compact / comfortable density">
          <i data-lucide="unfold-vertical" class="w-3.5 h-3.5"></i> <span id="densityToggleText">Compact</span>
        </button>"""

if old_btn_density in text:
    text = text.replace(old_btn_density, new_btn_density)
    print("Replaced btnDensityToggle")
else:
    print("Warning: old_btn_density not found verbatim")

old_btn_drawers = """        <button id="btnToggleAllDrawers" class="justify-center px-2 py-2 bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-semibold rounded-lg transition whitespace-nowrap flex items-center gap-1" title="Expand or collapse all detail drawers">
          <i data-lucide="chevrons-up-down" class="w-3.5 h-3.5"></i> <span id="toggleAllDrawersText">Expand All</span>
        </button>"""

new_btn_drawers = """        <button id="btnToggleAllDrawers" class="justify-center px-2 py-2 bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 border border-slate-200 dark:border-slate-700 text-xs font-semibold rounded-lg transition whitespace-nowrap flex items-center gap-1 cursor-pointer" title="Expand or collapse all detail drawers">
          <i data-lucide="chevrons-up-down" class="w-3.5 h-3.5"></i> <span id="toggleAllDrawersText">Expand All</span>
        </button>"""

if old_btn_drawers in text:
    text = text.replace(old_btn_drawers, new_btn_drawers)
    print("Replaced btnToggleAllDrawers")
else:
    print("Warning: old_btn_drawers not found verbatim")

# Write out index_Rev.037.html
rev_path = "RenewableVietNam/invm/index_Rev.037.html"
with open(rev_path, "w", encoding="utf-8") as f:
    f.write(text)

print(f"Successfully generated {rev_path} ({len(text)} bytes)")
