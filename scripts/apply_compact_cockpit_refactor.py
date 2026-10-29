import os
import re

def apply_refactor(invm_dir):
    index_path = os.path.join(invm_dir, "index.html")
    rev22_path = os.path.join(invm_dir, "index_Rev.022.html")

    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Update Revision Header Comment
    html = re.sub(
        r"<!-- Vietnam Investment Project Legal Management & M&A Engine Rev \d+\.\d+[^>]*-->",
        "<!-- Vietnam Investment Project Legal Management & M&A Engine Rev 0.22 - Compact Right-Aligned Project Selector & Phase CPM Telemetry - invest.renewablevietnam.com -->",
        html
    )

    # 2. Replace Header with Compact Single-Row Layout (Project Selector on the Right)
    old_header_start = html.find('<header class="w-full max-w-full bg-slate-900')
    old_header_end = html.find('</header>') + len('</header>')

    if old_header_start == -1 or old_header_end == -1:
        print(f"Error: Could not find <header> in {invm_dir}")
        return

    new_header_html = '''  <!-- Unified Slimline Executive Navbar (Single Compact Cockpit Header) -->
  <header class="w-full max-w-full bg-slate-900 text-white border-b border-slate-800 static xl:sticky xl:top-0 z-30 shadow-md backdrop-blur-md bg-opacity-95 no-print">
    <div class="w-full max-w-[1720px] mx-auto px-3 sm:px-4 lg:px-5 py-1.5">
      <div class="flex items-center justify-between gap-2 flex-wrap">
        
        <!-- Left: Brand Title with Home Anchor Link -->
        <a href="https://invest.renewablevietnam.com/" onclick="switchViewMode('dashboard')" class="flex items-center gap-2 shrink-0 hover:text-blue-300 transition cursor-pointer group" title="Quay về Trang chủ Bảng điều hành invest.renewablevietnam.com">
          <span class="inline-flex items-center justify-center p-1.5 bg-slate-800 rounded-lg text-white border border-slate-700 shadow-2xs shrink-0 group-hover:border-blue-500 transition">
            <i data-lucide="layers" class="w-4 h-4 text-white"></i>
          </span>
          <span class="text-xs sm:text-[13px] font-bold tracking-tight text-white uppercase whitespace-normal sm:whitespace-nowrap leading-tight">
            HỆ THỐNG ĐIỀU HÀNH DỰ ÁN ĐẦU TƯ &amp; QUẢN TRỊ PHÁP LÝ
          </span>
        </a>

        <!-- Right Group: Project Selector (Moved to Right Side) & Compact Controls -->
        <div class="flex items-center gap-1.5 flex-wrap shrink-0">

          <!-- Compact Project Selector Strip (Right-Aligned) -->
          <div class="flex items-center gap-0.5 bg-slate-800/90 border border-slate-700 rounded-lg px-1.5 py-0.5 shrink-0">
            <i data-lucide="folder-kanban" class="w-3.5 h-3.5 text-slate-300 shrink-0"></i>
            <select id="projectSelector" class="bg-transparent text-white text-[11px] font-semibold py-0.5 px-1 outline-none cursor-pointer max-w-[150px] sm:max-w-[190px] truncate" title="Chọn dự án đang làm việc">
              <!-- Rendered by JS -->
            </select>
            <button id="btnNewProject" class="p-1 text-slate-300 hover:text-white hover:bg-slate-700 rounded transition cursor-pointer" title="Tạo dự án mới">
              <i data-lucide="plus" class="w-3 h-3"></i>
            </button>
            <button id="btnRenameProject" class="p-1 text-slate-300 hover:text-white hover:bg-slate-700 rounded transition cursor-pointer" title="Đổi tên dự án">
              <i data-lucide="edit-2" class="w-3 h-3"></i>
            </button>
            <button id="btnDeleteProject" class="p-1 text-slate-300 hover:text-rose-400 hover:bg-slate-700 rounded transition cursor-pointer" title="Xóa dự án">
              <i data-lucide="trash-2" class="w-3 h-3"></i>
            </button>
          </div>

          <!-- Select 1: Loại Hình Dự Án (Compact) -->
          <div class="hidden lg:flex items-center gap-1 text-[11px] bg-slate-800/80 px-1.5 py-0.5 rounded-lg border border-slate-700 shrink-0">
            <label class="text-[9.5px] font-bold text-slate-400 uppercase tracking-wider whitespace-nowrap">Loại:</label>
            <select id="homeProjectTypeSelector" onchange="applyProjectType(this.value)" class="bg-transparent text-[11px] font-semibold text-white focus:outline-none cursor-pointer py-0.5">
              <option value="URBAN_TOWN" class="bg-slate-900" selected>1. Đô Thị / Nhà Ở</option>
              <option value="INDUSTRIAL" class="bg-slate-900">2. BĐS Công Nghiệp</option>
              <option value="ENERGY" class="bg-slate-900">3. Năng Lượng</option>
              <option value="RESORT" class="bg-slate-900">4. Nghỉ Dưỡng</option>
            </select>
          </div>

          <!-- Select 2: Mốc Tiếp Quản (Compact) -->
          <div class="hidden xl:flex items-center gap-1 text-[11px] bg-slate-800/80 px-1.5 py-0.5 rounded-lg border border-slate-700 shrink-0">
            <label class="text-[9.5px] font-bold text-slate-400 uppercase tracking-wider whitespace-nowrap">Mốc:</label>
            <select id="maEntrySelector" class="bg-transparent text-[11px] font-semibold text-white focus:outline-none cursor-pointer max-w-[130px] sm:max-w-[155px] truncate py-0.5">
              <option value="GREENFIELD" class="bg-slate-900" selected>1. Phát triển từ đầu</option>
              <option value="POST_POLICY" class="bg-slate-900">2. Sau Chấp thuận CTĐT</option>
              <option value="POST_1_500" class="bg-slate-900">3. Sau Phê duyệt 1/500</option>
              <option value="POST_LAND" class="bg-slate-900">4. Sau Giao/Thuê đất</option>
              <option value="POST_PERMIT" class="bg-slate-900">5. Đã có GPXD / Đang XD</option>
              <option value="OPERATIONAL" class="bg-slate-900">6. Dự án đang vận hành</option>
            </select>
          </div>

          <!-- Mode Switcher: Dashboard vs Legal Engine (Compact) -->
          <div class="flex items-center bg-slate-800 p-0.5 rounded-lg border border-slate-700 shrink-0 shadow-inner">
            <button id="btnViewDashboard" onclick="switchViewMode('dashboard')" class="px-2 sm:px-2.5 py-1 rounded-md text-[11px] font-bold transition flex items-center gap-1 bg-blue-600 text-white shadow-xs cursor-pointer" title="Bảng điều hành tổng quan dự án đầu tư">
              <i data-lucide="layout-dashboard" class="w-3 h-3"></i>
              <span class="whitespace-nowrap">Bảng Điều Hành</span>
            </button>
            <button id="btnViewLegalEngine" onclick="switchViewMode('legal')" class="px-2 sm:px-2.5 py-1 rounded-md text-[11px] font-bold transition flex items-center gap-1 text-slate-300 hover:text-white hover:bg-slate-700/60 cursor-pointer" title="Chi tiết hồ sơ pháp lý & phân tích đường găng CPM">
              <i data-lucide="list-checks" class="w-3 h-3"></i>
              <span class="whitespace-nowrap">Hồ Sơ &amp; CPM</span>
            </button>
          </div>

          <!-- Fast-Action Controls (Compact) -->
          <button onclick="openGanttModal()" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-semibold text-[11px] rounded-lg transition shadow-xs flex items-center gap-1 shrink-0 cursor-pointer" title="Mở biểu đồ CPM Gantt toàn màn hình">
            <i data-lucide="calendar-range" class="w-3 h-3 text-blue-400"></i>
            <span class="whitespace-nowrap hidden sm:inline">Gantt</span>
          </button>
          <a href="./quyhoach/" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-semibold text-[11px] rounded-lg transition shadow-xs flex items-center gap-1 shrink-0 cursor-pointer" title="Cổng dữ liệu quy hoạch xây dựng quốc gia">
            <i data-lucide="map" class="w-3 h-3 text-emerald-400"></i>
            <span class="whitespace-nowrap hidden sm:inline">Quy Hoạch</span>
          </a>
          <button id="btnApplyScenario" onclick="openDateSyncModal()" class="px-2.5 py-1 bg-white hover:bg-slate-100 text-slate-900 font-bold text-[11px] rounded-lg transition shadow-xs flex items-center gap-1 shrink-0 cursor-pointer" title="Áp dụng kịch bản và đồng bộ ngày thực hiện">
            <i data-lucide="sliders" class="w-3 h-3"></i>
            <span class="whitespace-nowrap">Áp Dụng</span>
          </button>
          <button id="btnCloudSync" onclick="triggerManualCloudSync()" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-semibold text-[11px] rounded-lg transition shadow-xs flex items-center gap-1 shrink-0 cursor-pointer" title="Đồng bộ dữ liệu thời gian thực với Supabase Cloud">
            <span id="cloudSyncDot" class="w-1.5 h-1.5 rounded-full bg-emerald-400 shrink-0"></span>
            <span id="cloudSyncText" class="whitespace-nowrap text-[10px] hidden md:inline">Cloud</span>
          </button>

          <!-- Hidden Metadata Anchors for JS Compatibility -->
          <span id="heroProjectId" class="hidden"></span>
          <span id="heroProjectBadge" class="hidden"></span>
          <span id="heroProjectTitle" class="hidden"></span>
          <span id="heroProjectDesc" class="hidden"></span>
        </div>

      </div>
    </div>
  </header>'''

    html = html[:old_header_start] + new_header_html + html[old_header_end:]
    print(f"Updated Header layout in {invm_dir}")

    # 3. Purge the 4 Bulky KPI Metric Boxes
    kpi_pattern = r'<!-- EXECUTIVE 4-PILLAR KPI METRIC RIBBON.*?<!-- STAGE-GATE STATUTORY PIPELINE'
    if re.search(kpi_pattern, html, flags=re.DOTALL):
        html = re.sub(kpi_pattern, '<!-- STAGE-GATE STATUTORY PIPELINE', html, flags=re.DOTALL)
        print(f"Purged 4-pillar KPI metric ribbon in {invm_dir}")

    # 4. Add 'Đường găng CPM & điểm nghẽn' box under label of each phase
    for p in range(1, 7):
        # Look for the phase ratio header inside each phase card
        old_phase_header = f'<span id="phase{p}Ratio" class="text-[11px] font-bold text-slate-600">0/'
        cpm_box_html = f'''</div>
            <!-- Đường găng CPM & điểm nghẽn Box -->
            <div class="my-2 px-2 py-1 rounded-lg bg-slate-100/90 border border-slate-200/90 flex items-center justify-between gap-1 text-[10.5px]">
              <span class="font-bold text-slate-700 flex items-center gap-1.5">
                <i data-lucide="git-commit" class="w-3.5 h-3.5 text-blue-600"></i>
                <span>Đường găng CPM:</span>
              </span>
              <span id="phase{p}CpmBadge" class="font-bold px-2 py-0.5 rounded text-[10px] bg-emerald-50 text-emerald-700 border border-emerald-200 whitespace-nowrap">
                <span class="inline-block w-1.5 h-1.5 rounded-full bg-emerald-500 mr-1"></span>Tiến độ chuẩn
              </span>
            </div>
            <div style="display:none">'''
        
        # We replace the closing </div> of the top header row of each phase card
        card_marker = f'<!-- Phase {p} -->'
        marker_pos = html.find(card_marker)
        if marker_pos != -1:
            # find first </div> after marker
            first_div_close = html.find('</div>', marker_pos)
            if first_div_close != -1 and f'id="phase{p}CpmBadge"' not in html:
                insertion = f'''
            <!-- Đường găng CPM & điểm nghẽn Box -->
            <div class="my-2 px-2.5 py-1.5 rounded-lg bg-slate-100/90 border border-slate-200/90 flex items-center justify-between gap-1 text-[10.5px]">
              <span class="font-bold text-slate-700 flex items-center gap-1.5">
                <i data-lucide="git-commit" class="w-3.5 h-3.5 text-blue-600"></i>
                <span>Đường găng CPM &amp; Điểm nghẽn:</span>
              </span>
              <span id="phase{p}CpmBadge" class="font-bold px-2 py-0.5 rounded text-[10px] bg-emerald-50 text-emerald-700 border border-emerald-200 whitespace-nowrap">
                <span class="inline-block w-1.5 h-1.5 rounded-full bg-emerald-500 mr-1"></span>Tiến độ chuẩn
              </span>
            </div>'''
                html = html[:first_div_close+6] + insertion + html[first_div_close+6:]
                print(f"Inserted CPM Box for Phase {p} in {invm_dir}")

    # 5. Update updateDashboardViewStats JS function to calculate phase CPM badge status
    old_update_stats_func = "function updateDashboardViewStats() {"
    new_update_stats_logic = """function updateDashboardViewStats() {
      const activeProj = typeof getActiveProject === 'function' ? getActiveProject() : null;
      if (!activeProj) return;

      const heroTitleEl = document.getElementById('heroProjectTitle');
      if (heroTitleEl) heroTitleEl.textContent = activeProj.name || "Dự Án Đầu Tư Tổ Hợp";

      const heroProjIdEl = document.getElementById('heroProjectId');
      if (heroProjIdEl) heroProjIdEl.textContent = activeProj.id || "PROJ-DEFAULT";

      const activeTasks = (typeof taskList !== 'undefined' && Array.isArray(taskList)) ? taskList : [];
      const total = activeTasks.length;

      for (let p = 1; p <= 6; p++) {
        const pKey = `Giai đoạn ${p}`;
        const pTasks = activeTasks.filter(t => t.phase && t.phase.startsWith(pKey));
        const pTotal = pTasks.length;
        const pDone = pTasks.filter(t => t.completed || t.status === 'Đã hoàn thành').length;
        const pPercent = pTotal > 0 ? Math.round((pDone / pTotal) * 100) : 0;

        const ratioEl = document.getElementById(`phase${p}Ratio`);
        if (ratioEl) ratioEl.textContent = `${pDone}/${pTotal} thủ tục`;

        const barEl = document.getElementById(`phase${p}Bar`);
        if (barEl) barEl.style.width = `${pPercent}%`;

        // Update Phase CPM & Bottlenecks status badge
        const delayedTasks = pTasks.filter(t => t.status === 'Bị nghẽn / Trễ hạn');
        const phaseCpmBadge = document.getElementById(`phase${p}CpmBadge`);
        if (phaseCpmBadge) {
          if (delayedTasks.length > 0) {
            phaseCpmBadge.className = "font-bold px-2 py-0.5 rounded text-[10px] bg-amber-50 text-amber-700 border border-amber-300 animate-pulse whitespace-nowrap";
            phaseCpmBadge.innerHTML = `<span class="inline-block w-1.5 h-1.5 rounded-full bg-amber-500 mr-1"></span>${delayedTasks.length} Điểm nghẽn CPM`;
          } else {
            phaseCpmBadge.className = "font-bold px-2 py-0.5 rounded text-[10px] bg-emerald-50 text-emerald-700 border border-emerald-200 whitespace-nowrap";
            phaseCpmBadge.innerHTML = `<span class="inline-block w-1.5 h-1.5 rounded-full bg-emerald-500 mr-1"></span>Tiến độ chuẩn`;
          }
        }
      }
    }

    function _deprecated_updateDashboardViewStats() {"""

    if old_update_stats_func in html and "phaseCpmBadge" not in html:
        html = html.replace(old_update_stats_func, new_update_stats_logic, 1)
        print(f"Updated updateDashboardViewStats() logic in {invm_dir}")

    # 6. Save index_Rev.022.html and index.html
    with open(rev22_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Created {rev22_path}")

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Updated {index_path}")

def main():
    rvn_invm = r"G:\My Drive\7. AI\RenewableVietNam\invm"
    qking_invm = r"G:\My Drive\7. AI\Qking232.github.io\invm"

    print("--- Applying Refactor in RenewableVietNam ---")
    apply_refactor(rvn_invm)

    print("--- Applying Refactor in Qking232.github.io ---")
    apply_refactor(qking_invm)

    print("--- Completed all operations successfully ---")

if __name__ == "__main__":
    main()
