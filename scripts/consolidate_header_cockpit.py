import os
import re

def consolidate_header(invm_dir):
    index_path = os.path.join(invm_dir, "index.html")
    rev21_path = os.path.join(invm_dir, "index_Rev.021.html")

    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Update Revision Header Comment
    html = re.sub(
        r"<!-- Vietnam Investment Project Legal Management & M&A Engine Rev \d+\.\d+[^>]*-->",
        "<!-- Vietnam Investment Project Legal Management & M&A Engine Rev 0.21 - Unified Compact Header & Single Viewport Cockpit - invest.renewablevietnam.com -->",
        html
    )

    # 2. Update <title>
    html = re.sub(
        r"<title>.*?</title>",
        "<title>Hệ Thống Điều Hành Dự Án Đầu Tư &amp; Quản Trị Pháp Lý</title>",
        html,
        count=1
    )

    # 3. Create the Unified Compact Header (Replacing the 2-tier header)
    old_header_start = html.find('<header class="w-full max-w-full bg-slate-900')
    old_header_end = html.find('</header>') + len('</header>')

    if old_header_start == -1 or old_header_end == -1:
        print(f"Error: Could not locate <header> in {invm_dir}")
        return

    new_header_html = '''  <!-- Unified Slimline Executive Navbar (Single Compact Cockpit Header) -->
  <header class="w-full max-w-full bg-slate-900 text-white border-b border-slate-800 static xl:sticky xl:top-0 z-30 shadow-md backdrop-blur-md bg-opacity-95 no-print">
    <div class="w-full max-w-[1720px] mx-auto px-3 sm:px-5 lg:px-6 py-2">
      <div class="flex flex-col xl:flex-row xl:items-center justify-between gap-2">
        
        <!-- Left Group: Canonical Title & Project Selector -->
        <div class="flex items-center gap-2.5 flex-wrap">
          <div class="flex items-center gap-2 shrink-0">
            <span class="inline-flex items-center justify-center p-1.5 bg-slate-800 rounded-lg text-white border border-slate-700 shadow-2xs shrink-0">
              <i data-lucide="layers" class="w-4 h-4 text-white"></i>
            </span>
            <h1 class="text-xs sm:text-sm font-bold tracking-tight text-white uppercase whitespace-normal sm:whitespace-nowrap leading-tight">
              HỆ THỐNG ĐIỀU HÀNH DỰ ÁN ĐẦU TƯ &amp; QUẢN TRỊ PHÁP LÝ
            </h1>
          </div>

          <!-- Compact Project Selector Strip -->
          <div class="flex items-center gap-1 bg-slate-800/90 border border-slate-700 rounded-lg px-1.5 py-0.5 shrink-0">
            <i data-lucide="folder-kanban" class="w-3.5 h-3.5 text-slate-300 shrink-0"></i>
            <select id="projectSelector" class="bg-transparent text-white text-xs font-semibold py-0.5 px-1 outline-none cursor-pointer max-w-[160px] sm:max-w-[200px] truncate" title="Chọn dự án đang làm việc">
              <!-- Rendered by JS -->
            </select>
            <button id="btnNewProject" class="p-1 text-slate-300 hover:text-white hover:bg-slate-700 rounded transition cursor-pointer" title="Tạo dự án mới">
              <i data-lucide="plus" class="w-3.5 h-3.5"></i>
            </button>
            <button id="btnRenameProject" class="p-1 text-slate-300 hover:text-white hover:bg-slate-700 rounded transition cursor-pointer" title="Đổi tên dự án">
              <i data-lucide="edit-2" class="w-3.5 h-3.5"></i>
            </button>
            <button id="btnDeleteProject" class="p-1 text-slate-300 hover:text-rose-400 hover:bg-slate-700 rounded transition cursor-pointer" title="Xóa dự án">
              <i data-lucide="trash-2" class="w-3.5 h-3.5"></i>
            </button>
          </div>

          <!-- Hidden Metadata Anchors for JS Compatibility -->
          <span id="heroProjectId" class="hidden"></span>
          <span id="heroProjectBadge" class="hidden"></span>
          <span id="heroProjectTitle" class="hidden"></span>
          <span id="heroProjectDesc" class="hidden"></span>
        </div>

        <!-- Right Group: Type Selector, Scenario Selector, Mode Switcher, and Fast Action Dispatches -->
        <div class="flex items-center gap-1.5 sm:gap-2 flex-wrap">
          
          <!-- Select 1: Loại Hình Dự Án -->
          <div class="flex items-center gap-1 text-xs bg-slate-800/80 px-2 py-0.5 rounded-lg border border-slate-700 shrink-0">
            <label class="text-[10px] font-bold text-slate-400 uppercase tracking-wider whitespace-nowrap">Loại Hình:</label>
            <select id="homeProjectTypeSelector" onchange="applyProjectType(this.value)" class="bg-transparent text-xs font-semibold text-white focus:outline-none cursor-pointer py-0.5">
              <option value="URBAN_TOWN" class="bg-slate-900" selected>1. Khu Đô Thị / Nhà Ở</option>
              <option value="INDUSTRIAL" class="bg-slate-900">2. BĐS Công Nghiệp (KCN)</option>
              <option value="ENERGY" class="bg-slate-900">3. Năng Lượng Tái Tạo</option>
              <option value="RESORT" class="bg-slate-900">4. Du Lịch Nghỉ Dưỡng</option>
            </select>
          </div>

          <!-- Select 2: Mốc Tiếp Quản & Kịch Bản M&A -->
          <div class="flex items-center gap-1 text-xs bg-slate-800/80 px-2 py-0.5 rounded-lg border border-slate-700 shrink-0">
            <label class="text-[10px] font-bold text-slate-400 uppercase tracking-wider whitespace-nowrap">Mốc Tiếp Quản:</label>
            <select id="maEntrySelector" class="bg-transparent text-xs font-semibold text-white focus:outline-none cursor-pointer max-w-[150px] sm:max-w-[180px] truncate py-0.5">
              <option value="GREENFIELD" class="bg-slate-900" selected>1. Phát triển từ đầu</option>
              <option value="POST_POLICY" class="bg-slate-900">2. Sau Chấp thuận CTĐT</option>
              <option value="POST_1_500" class="bg-slate-900">3. Sau Phê duyệt 1/500</option>
              <option value="POST_LAND" class="bg-slate-900">4. Sau Giao/Thuê đất</option>
              <option value="POST_PERMIT" class="bg-slate-900">5. Đã có GPXD / Đang XD</option>
              <option value="OPERATIONAL" class="bg-slate-900">6. Dự án đang vận hành</option>
            </select>
          </div>

          <!-- Mode Switcher: Dashboard vs Legal Engine -->
          <div class="flex items-center bg-slate-800 p-0.5 rounded-lg border border-slate-700 shrink-0 shadow-inner">
            <button id="btnViewDashboard" onclick="switchViewMode('dashboard')" class="px-2.5 py-1 rounded-md text-xs font-bold transition flex items-center gap-1.5 bg-blue-600 text-white shadow-xs cursor-pointer" title="Bảng điều hành tổng quan dự án đầu tư">
              <i data-lucide="layout-dashboard" class="w-3.5 h-3.5"></i>
              <span class="whitespace-nowrap">Bảng Điều Hành</span>
            </button>
            <button id="btnViewLegalEngine" onclick="switchViewMode('legal')" class="px-2.5 py-1 rounded-md text-xs font-bold transition flex items-center gap-1.5 text-slate-300 hover:text-white hover:bg-slate-700/60 cursor-pointer" title="Chi tiết hồ sơ pháp lý & phân tích đường găng CPM">
              <i data-lucide="list-checks" class="w-3.5 h-3.5"></i>
              <span class="whitespace-nowrap">Hồ Sơ Pháp Lý &amp; CPM</span>
            </button>
          </div>

          <!-- Fast-Action Controls -->
          <button onclick="openGanttModal()" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-semibold text-xs rounded-lg transition shadow-xs flex items-center gap-1.5 shrink-0 cursor-pointer" title="Mở biểu đồ CPM Gantt toàn màn hình">
            <i data-lucide="calendar-range" class="w-3.5 h-3.5 text-blue-400"></i>
            <span class="whitespace-nowrap hidden sm:inline">Biểu Đồ Gantt</span>
          </button>
          <a href="./quyhoach/" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-semibold text-xs rounded-lg transition shadow-xs flex items-center gap-1.5 shrink-0 cursor-pointer" title="Cổng dữ liệu quy hoạch xây dựng quốc gia">
            <i data-lucide="map" class="w-3.5 h-3.5 text-emerald-400"></i>
            <span class="whitespace-nowrap hidden sm:inline">Quy Hoạch BXD</span>
          </a>
          <button id="btnApplyScenario" onclick="openDateSyncModal()" class="px-3 py-1 bg-white hover:bg-slate-100 text-slate-900 font-bold text-xs rounded-lg transition shadow-xs flex items-center gap-1.5 shrink-0 cursor-pointer" title="Áp dụng kịch bản và đồng bộ ngày thực hiện">
            <i data-lucide="sliders" class="w-3.5 h-3.5"></i>
            <span class="whitespace-nowrap">Áp Dụng</span>
          </button>
          <button id="btnCloudSync" onclick="triggerManualCloudSync()" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-semibold text-xs rounded-lg transition shadow-xs flex items-center gap-1.5 shrink-0 cursor-pointer" title="Đồng bộ dữ liệu thời gian thực với Supabase Cloud">
            <i data-lucide="cloud" class="w-3.5 h-3.5 text-slate-300"></i>
            <span id="cloudSyncDot" class="w-2 h-2 rounded-full bg-emerald-400 shrink-0"></span>
            <span id="cloudSyncText" class="whitespace-nowrap hidden md:inline">Cloud</span>
          </button>

        </div>

      </div>
    </div>
  </header>'''

    html = html[:old_header_start] + new_header_html + html[old_header_end:]
    print(f"Replaced header with consolidated slimline navbar in {invm_dir}")

    # 4. Remove the redundant giant Hero Command Strip
    hero_pattern = r'<!-- HERO COMMAND STRIP: DỰ ÁN & VỐN ĐẦU TƯ -->\s*<section class="bg-gradient-to-r from-slate-900.*?</section>'
    if re.search(hero_pattern, html, flags=re.DOTALL):
        html = re.sub(hero_pattern, '', html, flags=re.DOTALL)
        print(f"Purged redundant hero command strip in {invm_dir}")

    # 5. Save index_Rev.021.html and index.html
    with open(rev21_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Created {rev21_path}")

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Updated {index_path}")

def main():
    rvn_invm = r"G:\My Drive\7. AI\RenewableVietNam\invm"
    qking_invm = r"G:\My Drive\7. AI\Qking232.github.io\invm"

    print("--- Consolidating Header in RenewableVietNam ---")
    consolidate_header(rvn_invm)

    print("--- Consolidating Header in Qking232.github.io ---")
    consolidate_header(qking_invm)

    print("--- Execution Complete ---")

if __name__ == "__main__":
    main()
