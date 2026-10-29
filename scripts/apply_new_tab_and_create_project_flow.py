import os
import re

def apply_updates(invm_dir):
    index_path = os.path.join(invm_dir, "index.html")
    rev23_path = os.path.join(invm_dir, "index_Rev.023.html")

    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Update Revision Header Comment
    html = re.sub(
        r"<!-- Vietnam Investment Project Legal Management & M&A Engine Rev \d+\.\d+[^>]*-->",
        "<!-- Vietnam Investment Project Legal Management & M&A Engine Rev 0.23 - New Tab Legal & CPM Routing & Dedicated Project Initialization - invest.renewablevietnam.com -->",
        html
    )

    # 2. Update Header:
    # A) Replace "Hồ Sơ & CPM" button to open in new tab (target="_blank")
    # B) Replace "Áp Dụng" with "+ Khởi Tạo Dự Án"
    old_header_start = html.find('<header class="w-full max-w-full bg-slate-900')
    old_header_end = html.find('</header>') + len('</header>')

    if old_header_start == -1 or old_header_end == -1:
        print(f"Error: Could not locate <header> in {invm_dir}")
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

        <!-- Right Group: Project Selector & Dedicated Creation Row -->
        <div class="flex items-center gap-1.5 flex-wrap shrink-0">

          <!-- Active Project Selector (Right-Aligned) -->
          <div class="flex items-center gap-0.5 bg-slate-800/90 border border-slate-700 rounded-lg px-1.5 py-0.5 shrink-0">
            <i data-lucide="folder-kanban" class="w-3.5 h-3.5 text-slate-300 shrink-0"></i>
            <select id="projectSelector" class="bg-transparent text-white text-[11px] font-semibold py-0.5 px-1 outline-none cursor-pointer max-w-[140px] sm:max-w-[180px] truncate" title="Chọn dự án đang làm việc">
              <!-- Rendered by JS -->
            </select>
            <button id="btnNewProject" onclick="openNewProjectWithScenario()" class="p-1 text-slate-300 hover:text-white hover:bg-slate-700 rounded transition cursor-pointer" title="Tạo dự án mới">
              <i data-lucide="plus" class="w-3 h-3"></i>
            </button>
            <button id="btnRenameProject" class="p-1 text-slate-300 hover:text-white hover:bg-slate-700 rounded transition cursor-pointer" title="Đổi tên dự án">
              <i data-lucide="edit-2" class="w-3 h-3"></i>
            </button>
            <button id="btnDeleteProject" class="p-1 text-slate-300 hover:text-rose-400 hover:bg-slate-700 rounded transition cursor-pointer" title="Xóa dự án">
              <i data-lucide="trash-2" class="w-3 h-3"></i>
            </button>
          </div>

          <!-- Parameter Setup 1: Loại Hình Dự Án -->
          <div class="hidden lg:flex items-center gap-1 text-[11px] bg-slate-800/80 px-1.5 py-0.5 rounded-lg border border-slate-700 shrink-0">
            <label class="text-[9.5px] font-bold text-slate-400 uppercase tracking-wider whitespace-nowrap">Loại:</label>
            <select id="homeProjectTypeSelector" onchange="applyProjectType(this.value)" class="bg-transparent text-[11px] font-semibold text-white focus:outline-none cursor-pointer py-0.5">
              <option value="URBAN_TOWN" class="bg-slate-900" selected>1. Đô Thị / Nhà Ở</option>
              <option value="INDUSTRIAL" class="bg-slate-900">2. BĐS Công Nghiệp</option>
              <option value="ENERGY" class="bg-slate-900">3. Năng Lượng</option>
              <option value="RESORT" class="bg-slate-900">4. Nghỉ Dưỡng</option>
            </select>
          </div>

          <!-- Parameter Setup 2: Mốc Tiếp Quản & Kịch Bản M&A -->
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

          <!-- Dedicated Project Initialization Trigger (Transformed from 'Áp Dụng') -->
          <button id="btnApplyScenario" onclick="openNewProjectWithScenario()" class="px-2.5 py-1 bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-[11px] rounded-md transition shadow-xs flex items-center gap-1.5 shrink-0 cursor-pointer" title="Khởi tạo dự án đầu tư mới theo loại hình và mốc tiếp quản đã chọn">
            <i data-lucide="folder-plus" class="w-3.5 h-3.5"></i>
            <span class="whitespace-nowrap">+ Khởi Tạo Dự Án</span>
          </button>

          <!-- Mode Controls: Dashboard (In-Place) vs Hồ Sơ & CPM (New Tab) -->
          <div class="flex items-center bg-slate-800 p-0.5 rounded-lg border border-slate-700 shrink-0 shadow-inner">
            <button id="btnViewDashboard" onclick="switchViewMode('dashboard')" class="px-2 sm:px-2.5 py-1 rounded-md text-[11px] font-bold transition flex items-center gap-1 bg-blue-600 text-white shadow-xs cursor-pointer" title="Bảng điều hành tổng quan dự án đầu tư">
              <i data-lucide="layout-dashboard" class="w-3 h-3"></i>
              <span class="whitespace-nowrap">Bảng Điều Hành</span>
            </button>
            <a href="./?view=legal" target="_blank" rel="noopener noreferrer" id="btnViewLegalEngine" class="px-2 sm:px-2.5 py-1 rounded-md text-[11px] font-bold transition flex items-center gap-1 text-slate-300 hover:text-white hover:bg-slate-700/60 cursor-pointer" title="Mở Hồ Sơ Pháp Lý & CPM trong tab mới">
              <i data-lucide="list-checks" class="w-3 h-3 text-blue-400"></i>
              <span class="whitespace-nowrap">Hồ Sơ &amp; CPM</span>
              <i data-lucide="external-link" class="w-2.5 h-2.5 text-slate-400 ml-0.5"></i>
            </a>
          </div>

          <!-- Fast-Action Tool Links -->
          <button onclick="openGanttModal()" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-semibold text-[11px] rounded-lg transition shadow-xs flex items-center gap-1 shrink-0 cursor-pointer" title="Mở biểu đồ CPM Gantt toàn màn hình">
            <i data-lucide="calendar-range" class="w-3 h-3 text-blue-400"></i>
            <span class="whitespace-nowrap hidden sm:inline">Gantt</span>
          </button>
          <a href="./quyhoach/" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-semibold text-[11px] rounded-lg transition shadow-xs flex items-center gap-1 shrink-0 cursor-pointer" title="Cổng dữ liệu quy hoạch xây dựng quốc gia">
            <i data-lucide="map" class="w-3 h-3 text-emerald-400"></i>
            <span class="whitespace-nowrap hidden sm:inline">Quy Hoạch</span>
          </a>
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
    print(f"Replaced header with New Tab + Khởi Tạo Dự Án layout in {invm_dir}")

    # 3. Add openNewProjectWithScenario JS helper function
    js_helper = '''
    // Dedicated project creation helper: pre-populates type and scenario from header selects
    function openNewProjectWithScenario() {
      if (typeof openNewProjectModal === 'function') {
        openNewProjectModal();
        const homeTypeSel = document.getElementById('homeProjectTypeSelector');
        const maSel = document.getElementById('maEntrySelector');
        const modalTypeSel = document.getElementById('selectProjectType');
        const modalScSel = document.getElementById('selectScenarioTemplate');

        if (homeTypeSel && modalTypeSel) {
          if (homeTypeSel.value === 'INDUSTRIAL') modalTypeSel.value = 'Khu Công Nghiệp / CCN';
          else if (homeTypeSel.value === 'URBAN_TOWN') modalTypeSel.value = 'Khu Đô Thị / Nhà Ở';
          else if (homeTypeSel.value === 'ENERGY') modalTypeSel.value = 'Năng Lượng / Hạ Tầng Kỹ Thuật';
          else if (homeTypeSel.value === 'RESORT') modalTypeSel.value = 'Thương Mại & Dịch Vụ / Resort';
        }
        if (maSel && modalScSel) {
          modalScSel.value = maSel.value;
        }
      }
    }
'''

    if "function openNewProjectWithScenario" not in html:
        # insert before the last </script>
        last_script_idx = html.rfind('</script>')
        if last_script_idx != -1:
            html = html[:last_script_idx] + js_helper + "\n" + html[last_script_idx:]
            print(f"Injected openNewProjectWithScenario helper in {invm_dir}")

    # 4. Save index_Rev.023.html and index.html
    with open(rev23_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Created {rev23_path}")

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Updated {index_path}")

def main():
    rvn_invm = r"G:\My Drive\7. AI\RenewableVietNam\invm"
    qking_invm = r"G:\My Drive\7. AI\Qking232.github.io\invm"

    print("--- Applying Rev 0.23 in RenewableVietNam ---")
    apply_updates(rvn_invm)

    print("--- Applying Rev 0.23 in Qking232.github.io ---")
    apply_updates(qking_invm)

    print("--- Completed all updates ---")

if __name__ == "__main__":
    main()
