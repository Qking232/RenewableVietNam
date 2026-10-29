import os
import re

def build_invest_dashboard():
    invm_dir = r"G:\My Drive\7. AI\RenewableVietNam\invm"
    index_path = os.path.join(invm_dir, "index.html")
    rev18_path = os.path.join(invm_dir, "index_Rev.018.html")

    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Update Revision header
    html = html.replace(
        "<!-- Vietnam Investment Project Legal Management & M&A Engine Rev 0.17 - Subdomain Canonical invest.renewablevietnam.com -->",
        "<!-- Vietnam Investment Project Legal Management & M&A Engine Rev 0.18 - Executive Investment Dashboard for invest.renewablevietnam.com -->"
    )

    # 2. Add Tab Switcher in the Header
    # Look for the header title container
    old_header_title = '''            <h1 class="text-xs sm:text-base font-bold tracking-tight text-white uppercase whitespace-normal sm:whitespace-nowrap leading-tight">
              HỆ THỐNG QUẢN LÝ DỰ ÁN ĐẦU TƯ
            </h1>'''
    
    new_header_title = '''            <div>
              <h1 class="text-xs sm:text-base font-bold tracking-tight text-white uppercase whitespace-normal sm:whitespace-nowrap leading-tight flex items-center gap-2">
                <span>INVEST.RENEWABLEVIETNAM.COM</span>
                <span class="px-2 py-0.5 text-[10px] font-semibold bg-blue-600/90 text-white rounded-md uppercase tracking-wider hidden md:inline">Cockpit</span>
              </h1>
              <p class="text-[10px] text-slate-400 font-medium hidden sm:block">Cổng Điều Hành Dự Án Đầu Tư & Quản Trị Pháp Lý Quốc Gia</p>
            </div>'''

    if old_header_title in html:
        html = html.replace(old_header_title, new_header_title, 1)

    # Insert View Mode Switcher in Header (Dashboard vs Legal Engine)
    old_nav_tools = '<div class="col-span-1 sm:col-span-2 xl:col-auto flex items-center gap-2">'
    new_nav_tools = '''<div class="col-span-1 sm:col-span-2 xl:col-auto flex items-center gap-2 flex-wrap">
            <!-- Mode Switcher: Dashboard vs Legal Engine -->
            <div class="flex items-center bg-slate-800/90 p-0.5 rounded-lg border border-slate-700 shrink-0 shadow-inner">
              <button id="btnViewDashboard" onclick="switchViewMode('dashboard')" class="px-2.5 sm:px-3 py-1.5 sm:py-1 rounded-md text-xs font-bold transition flex items-center gap-1.5 bg-blue-600 text-white shadow-xs cursor-pointer" title="Bảng điều hành tổng quan dự án đầu tư">
                <i data-lucide="layout-dashboard" class="w-3.5 h-3.5"></i>
                <span class="whitespace-nowrap">Bảng Điều Hành</span>
              </button>
              <button id="btnViewLegalEngine" onclick="switchViewMode('legal')" class="px-2.5 sm:px-3 py-1.5 sm:py-1 rounded-md text-xs font-bold transition flex items-center gap-1.5 text-slate-300 hover:text-white hover:bg-slate-700/60 cursor-pointer" title="Chi tiết hồ sơ pháp lý & phân tích đường găng CPM">
                <i data-lucide="list-checks" class="w-3.5 h-3.5"></i>
                <span class="whitespace-nowrap">Hồ Sơ Pháp Lý & CPM</span>
              </button>
            </div>'''
    
    if old_nav_tools in html:
        html = html.replace(old_nav_tools, new_nav_tools, 1)

    # 3. Insert the Executive Dashboard Component
    # We will insert #investExecutiveDashboard right after <main ...> and wrap the existing content in #investLegalEngineContainer
    main_open_tag = '<main class="w-full max-w-[1720px] mx-auto px-3 sm:px-6 lg:px-8 py-3.5 sm:py-6 space-y-4 sm:space-y-5 flex-1 min-w-0">'
    
    dashboard_html = '''
    <!-- ========================================== -->
    <!-- EXECUTIVE INVESTMENT DASHBOARD (VIEW 1)    -->
    <!-- ========================================== -->
    <div id="investExecutiveDashboard" class="w-full max-w-full min-w-0 space-y-5 animate-in fade-in duration-300">
      
      <!-- HERO COMMAND STRIP: DỰ ÁN & VỐN ĐẦU TƯ -->
      <section class="bg-gradient-to-r from-slate-900 via-slate-850 to-slate-900 text-white rounded-2xl p-4 sm:p-6 border border-slate-800 shadow-xl relative overflow-hidden">
        <div class="absolute -right-16 -bottom-16 w-64 h-64 bg-blue-600/10 rounded-full blur-3xl pointer-events-none"></div>
        <div class="relative z-10 flex flex-col lg:flex-row lg:items-center justify-between gap-4">
          <div class="space-y-1.5 max-w-2xl">
            <div class="flex items-center gap-2 flex-wrap">
              <span class="px-2.5 py-0.5 rounded-full bg-blue-500/20 text-blue-300 border border-blue-500/40 text-[10.5px] font-bold uppercase tracking-wider flex items-center gap-1.5">
                <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                Dự Án Đang Quản Trị
              </span>
              <span id="heroProjectBadge" class="px-2.5 py-0.5 rounded-full bg-slate-800 text-slate-300 border border-slate-700 text-[10.5px] font-semibold">
                Khu Đô Thị & Năng Lượng Xanh
              </span>
              <span class="px-2 py-0.5 text-[10.5px] text-slate-400 font-mono">ID: <span id="heroProjectId">PROJ-DEFAULT</span></span>
            </div>
            <h2 id="heroProjectTitle" class="text-lg sm:text-2xl font-extrabold text-white tracking-tight leading-tight">
              Dự Án Đầu Tư Tổ Hợp Công Nghiệp - Đô Thị & Năng Lượng Tái Tạo
            </h2>
            <p id="heroProjectDesc" class="text-xs sm:text-sm text-slate-300 leading-relaxed font-normal">
              Quy mô dự án tích hợp hệ sinh thái điện mặt trời, cụm công nghiệp sinh thái và hạ tầng giao thông kết nối theo định hướng phát triển bền vững và giảm phát thải ròng Net Zero.
            </p>
          </div>

          <!-- Quick Action Buttons in Hero -->
          <div class="flex items-center gap-2.5 flex-wrap shrink-0">
            <button onclick="openGanttModal()" class="px-3.5 py-2 bg-blue-600 hover:bg-blue-500 text-white text-xs font-bold rounded-xl transition shadow-md flex items-center gap-2 cursor-pointer">
              <i data-lucide="calendar-range" class="w-4 h-4"></i>
              <span>Biểu Đồ CPM Gantt</span>
            </button>
            <button onclick="switchViewMode('legal')" class="px-3.5 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-bold rounded-xl transition shadow-sm flex items-center gap-2 cursor-pointer">
              <i data-lucide="file-text" class="w-4 h-4"></i>
              <span>Hồ Sơ Pháp Lý (46 Mục)</span>
            </button>
            <a href="./quyhoach/" class="px-3.5 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-bold rounded-xl transition shadow-sm flex items-center gap-2 cursor-pointer">
              <i data-lucide="map" class="w-4 h-4 text-blue-400"></i>
              <span>Quy Hoạch BXD</span>
            </a>
          </div>
        </div>
      </section>

      <!-- EXECUTIVE 4-PILLAR KPI METRIC RIBBON (Material Design 3 Expressive) -->
      <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3.5">
        
        <!-- Metric 1: Tổng Vốn Đầu Tư -->
        <div class="bg-white rounded-2xl p-4 shadow-xs border border-slate-200/90 flex flex-col justify-between hover:shadow-md transition">
          <div class="flex items-center justify-between mb-2">
            <span class="text-[11px] font-bold text-slate-500 uppercase tracking-wider">Tổng Vốn Dự Án (CapEx)</span>
            <span class="p-2 bg-blue-50 text-blue-600 rounded-xl">
              <i data-lucide="badge-dollar-sign" class="w-4 h-4"></i>
            </span>
          </div>
          <div class="space-y-1">
            <div class="flex items-baseline gap-2">
              <h3 id="dashCapexTotal" class="text-2xl font-extrabold text-slate-900 tracking-tight">48.500</h3>
              <span class="text-xs font-bold text-slate-500">Tỷ VNĐ</span>
            </div>
            <div class="flex items-center justify-between text-[11px] text-slate-500 pt-1.5 border-t border-slate-100">
              <span>Tương đương: <strong class="text-slate-700 font-semibold">~$1.95B USD</strong></span>
              <span class="text-emerald-600 font-bold bg-emerald-50 px-1.5 py-0.5 rounded">FDI / Trong nước</span>
            </div>
          </div>
        </div>

        <!-- Metric 2: Tỷ Lệ Hoàn Thành Pháp Lý -->
        <div class="bg-white rounded-2xl p-4 shadow-xs border border-slate-200/90 flex flex-col justify-between hover:shadow-md transition">
          <div class="flex items-center justify-between mb-2">
            <span class="text-[11px] font-bold text-slate-500 uppercase tracking-wider">Chỉ Số Pháp Lý Hoàn Tất</span>
            <span class="p-2 bg-emerald-50 text-emerald-600 rounded-xl">
              <i data-lucide="shield-check" class="w-4 h-4"></i>
            </span>
          </div>
          <div class="space-y-2">
            <div class="flex items-baseline justify-between">
              <div class="flex items-baseline gap-1.5">
                <h3 id="dashLegalPercent" class="text-2xl font-extrabold text-slate-900 tracking-tight">0%</h3>
                <span class="text-[11px] text-slate-500 font-medium">hoàn thành</span>
              </div>
              <span id="dashCompletedRatio" class="text-xs font-bold text-emerald-600">0/0 thủ tục</span>
            </div>
            <!-- Wavy Sinusoidal-style Expressive Progress Bar -->
            <div class="w-full bg-slate-100 h-2.5 rounded-full overflow-hidden p-0.5">
              <div id="dashLegalProgressBar" class="bg-gradient-to-r from-blue-600 to-emerald-500 h-full rounded-full transition-all duration-500" style="width: 0%"></div>
            </div>
          </div>
        </div>

        <!-- Metric 3: Quỹ Đất & Diện Tích Khảo Sát -->
        <div class="bg-white rounded-2xl p-4 shadow-xs border border-slate-200/90 flex flex-col justify-between hover:shadow-md transition">
          <div class="flex items-center justify-between mb-2">
            <span class="text-[11px] font-bold text-slate-500 uppercase tracking-wider">Quy Mô Quỹ Đất Dự Án</span>
            <span class="p-2 bg-purple-50 text-purple-600 rounded-xl">
              <i data-lucide="map-pin" class="w-4 h-4"></i>
            </span>
          </div>
          <div class="space-y-1">
            <div class="flex items-baseline gap-2">
              <h3 id="dashLandArea" class="text-2xl font-extrabold text-slate-900 tracking-tight">3.250</h3>
              <span class="text-xs font-bold text-slate-500">Héc-ta (Ha)</span>
            </div>
            <div class="flex items-center justify-between text-[11px] text-slate-500 pt-1.5 border-t border-slate-100">
              <span>Đất sạch đã GPMB: <strong class="text-slate-700 font-semibold">1.820 Ha</strong></span>
              <span class="text-purple-700 font-bold bg-purple-50 px-1.5 py-0.5 rounded">63 Tỉnh Thành</span>
            </div>
          </div>
        </div>

        <!-- Metric 4: Tình Trạng Tiến Độ CPM & Điểm Nghẽn -->
        <div class="bg-white rounded-2xl p-4 shadow-xs border border-slate-200/90 flex flex-col justify-between hover:shadow-md transition">
          <div class="flex items-center justify-between mb-2">
            <span class="text-[11px] font-bold text-slate-500 uppercase tracking-wider">Đường Găng CPM & Điểm Nghẽn</span>
            <span class="p-2 bg-amber-50 text-amber-600 rounded-xl">
              <i data-lucide="alert-triangle" class="w-4 h-4"></i>
            </span>
          </div>
          <div class="space-y-1">
            <div class="flex items-baseline gap-2">
              <h3 id="dashDelayedCount" class="text-2xl font-extrabold text-amber-600 tracking-tight">0</h3>
              <span class="text-xs font-bold text-slate-500">thủ tục trễ hạn</span>
            </div>
            <div class="flex items-center justify-between text-[11px] text-slate-500 pt-1.5 border-t border-slate-100">
              <span>Đang xử lý: <strong id="dashInProgressCount" class="text-slate-700 font-semibold">0</strong></span>
              <span id="dashCpmStatusBadge" class="text-emerald-700 font-bold bg-emerald-50 px-1.5 py-0.5 rounded">Tiến độ chuẩn</span>
            </div>
          </div>
        </div>

      </section>

      <!-- STAGE-GATE STATUTORY PIPELINE (6 GIAI ĐOẠN ĐẦU TƯ LIÊN HOÀN) -->
      <section class="bg-white rounded-2xl p-4 sm:p-6 border border-slate-200/90 shadow-xs space-y-4">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 pb-3 border-b border-slate-100">
          <div>
            <h3 class="text-sm sm:text-base font-extrabold text-slate-900 tracking-tight flex items-center gap-2">
              <i data-lucide="git-commit" class="w-4 h-4 text-blue-600"></i>
              Tiến Trình 6 Giai Đoạn Thẩm Quyền Pháp Lý & Đầu Tư (Stage-Gate Pipeline)
            </h3>
            <p class="text-xs text-slate-500">Quy trình chuẩn hóa theo Luật Đầu tư 2020, Luật Đất đai 2024, Luật Xây dựng và Quy hoạch Điện VIII.</p>
          </div>
          <button onclick="switchViewMode('legal')" class="text-xs font-bold text-blue-600 hover:text-blue-700 flex items-center gap-1 cursor-pointer">
            Xem Bảng Danh Mục Chi Tiết <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
          </button>
        </div>

        <!-- 6 Phase Interactive Cards Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-3.5">
          
          <!-- Phase 1 -->
          <div onclick="filterByPhaseAndSwitch('Giai đoạn 1')" class="p-3.5 rounded-xl border border-slate-200 hover:border-blue-500 hover:shadow-md transition cursor-pointer bg-slate-50/50 hover:bg-white group">
            <div class="flex items-center justify-between mb-2">
              <span class="px-2 py-0.5 rounded-md bg-slate-200 text-slate-800 text-[10px] font-extrabold uppercase">Giai Đoạn 1</span>
              <span id="phase1Ratio" class="text-[11px] font-bold text-slate-600">0/6 thủ tục</span>
            </div>
            <h4 class="text-xs font-bold text-slate-900 group-hover:text-blue-600 transition mb-1 leading-snug">
              Chuẩn Bị Đầu Tư & Chấp Thuận Chủ Trương
            </h4>
            <p class="text-[11px] text-slate-500 mb-3 line-clamp-2">
              Khảo sát địa điểm, lập hồ sơ đề xuất dự án, trình thẩm định tại Sở KH&ĐT và phê duyệt Chấp thuận chủ trương tại UBND cấp Tỉnh / Thủ tướng.
            </p>
            <div class="w-full bg-slate-200 h-1.5 rounded-full overflow-hidden">
              <div id="phase1Bar" class="bg-blue-600 h-full rounded-full transition-all duration-300" style="width: 0%"></div>
            </div>
          </div>

          <!-- Phase 2 -->
          <div onclick="filterByPhaseAndSwitch('Giai đoạn 2')" class="p-3.5 rounded-xl border border-slate-200 hover:border-sky-500 hover:shadow-md transition cursor-pointer bg-slate-50/50 hover:bg-white group">
            <div class="flex items-center justify-between mb-2">
              <span class="px-2 py-0.5 rounded-md bg-sky-100 text-sky-800 text-[10px] font-extrabold uppercase">Giai Đoạn 2</span>
              <span id="phase2Ratio" class="text-[11px] font-bold text-slate-600">0/10 thủ tục</span>
            </div>
            <h4 class="text-xs font-bold text-slate-900 group-hover:text-sky-600 transition mb-1 leading-snug">
              Quy Hoạch Chi Tiết 1/500 & Thiết Kế Cơ Sở
            </h4>
            <p class="text-[11px] text-slate-500 mb-3 line-clamp-2">
              Lập nhiệm vụ và đồ án quy hoạch 1/500, lấy ý kiến cộng đồng dân cư, thẩm định thiết kế cơ sở và công nghệ tại Sở Xây dựng / Bộ quản lý ngành.
            </p>
            <div class="w-full bg-slate-200 h-1.5 rounded-full overflow-hidden">
              <div id="phase2Bar" class="bg-sky-600 h-full rounded-full transition-all duration-300" style="width: 0%"></div>
            </div>
          </div>

          <!-- Phase 3 -->
          <div onclick="filterByPhaseAndSwitch('Giai đoạn 3')" class="p-3.5 rounded-xl border border-slate-200 hover:border-orange-500 hover:shadow-md transition cursor-pointer bg-slate-50/50 hover:bg-white group">
            <div class="flex items-center justify-between mb-2">
              <span class="px-2 py-0.5 rounded-md bg-orange-100 text-orange-800 text-[10px] font-extrabold uppercase">Giai Đoạn 3</span>
              <span id="phase3Ratio" class="text-[11px] font-bold text-slate-600">0/8 thủ tục</span>
            </div>
            <h4 class="text-xs font-bold text-slate-900 group-hover:text-orange-600 transition mb-1 leading-snug">
              Bồi Thường GPMB, Giao Đất & Nghĩa Vụ Tài Chính
            </h4>
            <p class="text-[11px] text-slate-500 mb-3 line-clamp-2">
              Kế hoạch sử dụng đất, thu hồi đất, định giá đất cụ thể theo bảng giá đất Luật Đất đai 2024, nộp tiền thuê đất/tiền sử dụng đất và cấp Giấy chứng nhận (Sổ đỏ).
            </p>
            <div class="w-full bg-slate-200 h-1.5 rounded-full overflow-hidden">
              <div id="phase3Bar" class="bg-orange-600 h-full rounded-full transition-all duration-300" style="width: 0%"></div>
            </div>
          </div>

          <!-- Phase 4 -->
          <div onclick="filterByPhaseAndSwitch('Giai đoạn 4')" class="p-3.5 rounded-xl border border-slate-200 hover:border-emerald-500 hover:shadow-md transition cursor-pointer bg-slate-50/50 hover:bg-white group">
            <div class="flex items-center justify-between mb-2">
              <span class="px-2 py-0.5 rounded-md bg-emerald-100 text-emerald-800 text-[10px] font-extrabold uppercase">Giai Đoạn 4</span>
              <span id="phase4Ratio" class="text-[11px] font-bold text-slate-600">0/6 thủ tục</span>
            </div>
            <h4 class="text-xs font-bold text-slate-900 group-hover:text-emerald-600 transition mb-1 leading-snug">
              Môi Trường (ĐTM) & Phòng Cháy Chữa Cháy (PCCC)
            </h4>
            <p class="text-[11px] text-slate-500 mb-3 line-clamp-2">
              Lập báo cáo đánh giá tác động môi trường (ĐTM), thẩm định cấp Giấy phép môi trường tại Bộ TN&MT và thẩm duyệt thiết kế PCCC tại C07 / PC07.
            </p>
            <div class="w-full bg-slate-200 h-1.5 rounded-full overflow-hidden">
              <div id="phase4Bar" class="bg-emerald-600 h-full rounded-full transition-all duration-300" style="width: 0%"></div>
            </div>
          </div>

          <!-- Phase 5 -->
          <div onclick="filterByPhaseAndSwitch('Giai đoạn 5')" class="p-3.5 rounded-xl border border-slate-200 hover:border-teal-500 hover:shadow-md transition cursor-pointer bg-slate-50/50 hover:bg-white group">
            <div class="flex items-center justify-between mb-2">
              <span class="px-2 py-0.5 rounded-md bg-teal-100 text-teal-800 text-[10px] font-extrabold uppercase">Giai Đoạn 5</span>
              <span id="phase5Ratio" class="text-[11px] font-bold text-slate-600">0/5 thủ tục</span>
            </div>
            <h4 class="text-xs font-bold text-slate-900 group-hover:text-teal-600 transition mb-1 leading-snug">
              Giấy Phép Xây Dựng (GPXD) & Thi Công
            </h4>
            <p class="text-[11px] text-slate-500 mb-3 line-clamp-2">
              Thẩm định thiết kế bản vẽ thi công (TKBVTC), thẩm duyệt an toàn kết cấu, cấp Giấy phép xây dựng và khởi công xây dựng công trình.
            </p>
            <div class="w-full bg-slate-200 h-1.5 rounded-full overflow-hidden">
              <div id="phase5Bar" class="bg-teal-600 h-full rounded-full transition-all duration-300" style="width: 0%"></div>
            </div>
          </div>

          <!-- Phase 6 -->
          <div onclick="filterByPhaseAndSwitch('Giai đoạn 6')" class="p-3.5 rounded-xl border border-slate-200 hover:border-indigo-500 hover:shadow-md transition cursor-pointer bg-slate-50/50 hover:bg-white group">
            <div class="flex items-center justify-between mb-2">
              <span class="px-2 py-0.5 rounded-md bg-indigo-100 text-indigo-800 text-[10px] font-extrabold uppercase">Giai Đoạn 6</span>
              <span id="phase6Ratio" class="text-[11px] font-bold text-slate-600">0/5 thủ tục</span>
            </div>
            <h4 class="text-xs font-bold text-slate-900 group-hover:text-indigo-600 transition mb-1 leading-snug">
              Nghiệm Thu Hoàn Thành, Đấu Nối & Vận Hành (COD)
            </h4>
            <p class="text-[11px] text-slate-500 mb-3 line-clamp-2">
              Nghiệm thu PCCC, kiểm tra công tác nghiệm thu công trình xây dựng của cơ quan chuyên môn, thỏa thuận đấu nối kỹ thuật và đưa dự án vào vận hành thương mại.
            </p>
            <div class="w-full bg-slate-200 h-1.5 rounded-full overflow-hidden">
              <div id="phase6Bar" class="bg-indigo-600 h-full rounded-full transition-all duration-300" style="width: 0%"></div>
            </div>
          </div>

        </div>
      </section>

      <!-- ECOSYSTEM GATEWAYS (4 TRỤ CỘT ĐIỀU HÀNH QUỐC GIA) -->
      <section class="space-y-3">
        <div class="flex items-center justify-between">
          <h3 class="text-sm sm:text-base font-extrabold text-slate-900 tracking-tight flex items-center gap-2">
            <i data-lucide="compass" class="w-4 h-4 text-blue-600"></i>
            Hệ Sinh Thái Điều Hành & Bản Đồ Dự Án (Ecosystem Gateways)
          </h3>
          <span class="text-xs text-slate-500">Tích hợp dữ liệu liên kết 4 phân hệ</span>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3.5">
          
          <!-- Gateway 1: Cổng Quy Hoạch BXD -->
          <a href="./quyhoach/" class="bg-white rounded-2xl p-4 border border-slate-200/90 shadow-xs hover:border-blue-500 hover:shadow-lg transition-all group flex flex-col justify-between block cursor-pointer">
            <div class="space-y-2">
              <div class="w-10 h-10 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center group-hover:bg-blue-600 group-hover:text-white transition">
                <i data-lucide="map" class="w-5 h-5"></i>
              </div>
              <h4 class="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-blue-600 transition">
                Cổng Quy Hoạch Xây Dựng BXD
              </h4>
              <p class="text-[11px] text-slate-500 leading-relaxed">
                Hệ thống dữ liệu đồ án quy hoạch xây dựng quốc gia tích hợp 63 tỉnh thành, tra cứu ranh giới phân khu và quy hoạch chi tiết.
              </p>
            </div>
            <div class="pt-3 border-t border-slate-100 flex items-center justify-between text-xs font-bold text-blue-600">
              <span>Mở Cổng Quy Hoạch</span>
              <i data-lucide="arrow-up-right" class="w-3.5 h-3.5 group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition"></i>
            </div>
          </a>

          <!-- Gateway 2: Quy Hoạch Điện VIII -->
          <a href="https://renewablevietnam.com/pdp8/" target="_blank" class="bg-white rounded-2xl p-4 border border-slate-200/90 shadow-xs hover:border-emerald-500 hover:shadow-lg transition-all group flex flex-col justify-between block cursor-pointer">
            <div class="space-y-2">
              <div class="w-10 h-10 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center group-hover:bg-emerald-600 group-hover:text-white transition">
                <i data-lucide="zap" class="w-5 h-5"></i>
              </div>
              <h4 class="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-emerald-600 transition">
                Danh Mục Quy Hoạch Điện VIII (PDP8)
              </h4>
              <p class="text-[11px] text-slate-500 leading-relaxed">
                Theo dõi tiến độ pháp lý danh mục dự án nguồn điện gió, điện mặt trời, điện sinh khối và hệ thống lưới truyền tải 500kV/220kV.
              </p>
            </div>
            <div class="pt-3 border-t border-slate-100 flex items-center justify-between text-xs font-bold text-emerald-600">
              <span>Mở PDP8 Tracker</span>
              <i data-lucide="arrow-up-right" class="w-3.5 h-3.5 group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition"></i>
            </div>
          </a>

          <!-- Gateway 3: Cụm KCN Xanh Hub -->
          <a href="https://renewablevietnam.com/hub/" target="_blank" class="bg-white rounded-2xl p-4 border border-slate-200/90 shadow-xs hover:border-purple-500 hover:shadow-lg transition-all group flex flex-col justify-between block cursor-pointer">
            <div class="space-y-2">
              <div class="w-10 h-10 rounded-xl bg-purple-50 text-purple-600 flex items-center justify-center group-hover:bg-purple-600 group-hover:text-white transition">
                <i data-lucide="factory" class="w-5 h-5"></i>
              </div>
              <h4 class="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-purple-600 transition">
                Bất Động Sản Công Nghiệp & KCN Xanh
              </h4>
              <p class="text-[11px] text-slate-500 leading-relaxed">
                Cơ sở dữ liệu 400+ Khu công nghiệp & Cụm công nghiệp toàn quốc, bản đồ vệ tinh, hạ tầng trạm sạc EV và chỉ số xanh ESG.
              </p>
            </div>
            <div class="pt-3 border-t border-slate-100 flex items-center justify-between text-xs font-bold text-purple-600">
              <span>Mở Industrial Hub</span>
              <i data-lucide="arrow-up-right" class="w-3.5 h-3.5 group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition"></i>
            </div>
          </a>

          <!-- Gateway 4: Công Cụ Tính Toán Năng Lượng & Suất Đầu Tư -->
          <a href="https://renewablevietnam.com/calculator/" target="_blank" class="bg-white rounded-2xl p-4 border border-slate-200/90 shadow-xs hover:border-amber-500 hover:shadow-lg transition-all group flex flex-col justify-between block cursor-pointer">
            <div class="space-y-2">
              <div class="w-10 h-10 rounded-xl bg-amber-50 text-amber-600 flex items-center justify-center group-hover:bg-amber-600 group-hover:text-white transition">
                <i data-lucide="calculator" class="w-5 h-5"></i>
              </div>
              <h4 class="text-xs sm:text-sm font-bold text-slate-900 group-hover:text-amber-600 transition">
                Tính Toán Suất Đầu Tư & Hiệu Quả Tài Chính
              </h4>
              <p class="text-[11px] text-slate-500 leading-relaxed">
                Mô hình định lượng suất đầu tư, dòng tiền CapEx, OpEx, chỉ số IRR, NPV, LCOE và thời gian hoàn vốn cho dự án năng lượng & công nghiệp.
              </p>
            </div>
            <div class="pt-3 border-t border-slate-100 flex items-center justify-between text-xs font-bold text-amber-600">
              <span>Mở Công Cụ Tính Toán</span>
              <i data-lucide="arrow-up-right" class="w-3.5 h-3.5 group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition"></i>
            </div>
          </a>

        </div>
      </section>

      <!-- REGULATORY BOTTLENECK RADAR & POLICY WIRE ROW -->
      <section class="grid grid-cols-1 lg:grid-cols-2 gap-4">
        
        <!-- Bottleneck & Escalation Radar -->
        <div class="bg-white rounded-2xl p-4 sm:p-5 border border-slate-200/90 shadow-xs space-y-3">
          <div class="flex items-center justify-between pb-2 border-b border-slate-100">
            <div class="flex items-center gap-2">
              <span class="p-1.5 rounded-lg bg-amber-100 text-amber-700">
                <i data-lucide="alert-octagon" class="w-4 h-4"></i>
              </span>
              <h4 class="text-xs sm:text-sm font-bold text-slate-900">
                Điểm Nghẽn & Cảnh Báo Rủi Ro Pháp Lý Trọng Yếu
              </h4>
            </div>
            <span class="text-[10px] font-bold text-amber-700 bg-amber-50 border border-amber-200 px-2 py-0.5 rounded-full">Cần xử lý ưu tiên</span>
          </div>
          
          <div id="dashBottlenecksList" class="space-y-2 text-xs">
            <!-- Rendered by JS based on delayed/in-progress critical path tasks -->
            <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 flex items-start gap-2.5">
              <i data-lucide="clock" class="w-4 h-4 text-amber-600 shrink-0 mt-0.5"></i>
              <div>
                <strong class="text-slate-800 font-semibold block">Thẩm duyệt thiết kế Phòng cháy & Chữa cháy (C07 / PC07)</strong>
                <span class="text-[11px] text-slate-500">Cần đồng bộ hồ sơ kiến trúc với quy chuẩn QCVN 06:2022/BXD sửa đổi.</span>
              </div>
            </div>
            <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 flex items-start gap-2.5">
              <i data-lucide="alert-circle" class="w-4 h-4 text-blue-600 shrink-0 mt-0.5"></i>
              <div>
                <strong class="text-slate-800 font-semibold block">Định giá đất cụ thể & Phương pháp thặng dư (Luật Đất đai 2024)</strong>
                <span class="text-[11px] text-slate-500">Chờ Hội đồng thẩm định giá đất cấp Tỉnh thông qua phương án tài chính.</span>
              </div>
            </div>
            <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 flex items-start gap-2.5">
              <i data-lucide="check-circle-2" class="w-4 h-4 text-emerald-600 shrink-0 mt-0.5"></i>
              <div>
                <strong class="text-slate-800 font-semibold block">Thỏa thuận đấu nối kỹ thuật lưới điện truyền tải</strong>
                <span class="text-[11px] text-slate-500">Đã cơ bản hoàn tất văn bản thỏa thuận nguyên tắc với Tổng công ty Điện lực.</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Policy Catalysts & Statutory Intelligence Wire -->
        <div class="bg-white rounded-2xl p-4 sm:p-5 border border-slate-200/90 shadow-xs space-y-3">
          <div class="flex items-center justify-between pb-2 border-b border-slate-100">
            <div class="flex items-center gap-2">
              <span class="p-1.5 rounded-lg bg-blue-100 text-blue-700">
                <i data-lucide="newspaper" class="w-4 h-4"></i>
              </span>
              <h4 class="text-xs sm:text-sm font-bold text-slate-900">
                Điểm Tin Thể Chế & Xúc Tiến Đầu Tư Quốc Gia
              </h4>
            </div>
            <span class="text-[10px] font-bold text-blue-700 bg-blue-50 border border-blue-200 px-2 py-0.5 rounded-full">Pháp luật mới 2024 - 2026</span>
          </div>

          <div class="space-y-2.5 text-xs">
            <div class="p-2.5 rounded-xl border border-slate-100 hover:bg-slate-50 transition">
              <div class="flex items-center justify-between text-[10px] text-slate-400 mb-0.5 font-mono">
                <span>Nghị định 80/2024/NĐ-CP</span>
                <span>Chính phủ</span>
              </div>
              <h5 class="font-bold text-slate-800 hover:text-blue-600 transition cursor-pointer">
                Cơ Chế Mua Bán Điện Trực Tiếp (DPPA) Giữa Khách Hàng Lớn & Đơn Vị Phát Điện Tái Tạo
              </h5>
              <p class="text-[11px] text-slate-500 mt-0.5 line-clamp-1">
                Cho phép đấu nối trực tiếp hoặc qua lưới điện quốc gia, mở khóa dòng vốn FDI vào năng lượng sạch.
              </p>
            </div>

            <div class="p-2.5 rounded-xl border border-slate-100 hover:bg-slate-50 transition">
              <div class="flex items-center justify-between text-[10px] text-slate-400 mb-0.5 font-mono">
                <span>Nghị định 71/2024/NĐ-CP</span>
                <span>Bộ Tài nguyên & Môi trường</span>
              </div>
              <h5 class="font-bold text-slate-800 hover:text-blue-600 transition cursor-pointer">
                Quy Định Mới Về Định Giá Đất Cụ Thể Theo Bảng Giá Đất Luật Đất Đai 2024
              </h5>
              <p class="text-[11px] text-slate-500 mt-0.5 line-clamp-1">
                Chi tiết phương pháp so sánh, thu nhập, thặng dư và hệ số điều chỉnh giá đất, tháo gỡ điểm nghẽn nghĩa vụ tài chính.
              </p>
            </div>

            <div class="p-2.5 rounded-xl border border-slate-100 hover:bg-slate-50 transition">
              <div class="flex items-center justify-between text-[10px] text-slate-400 mb-0.5 font-mono">
                <span>Nghị định 135/2024/NĐ-CP</span>
                <span>Bộ Công Thương</span>
              </div>
              <h5 class="font-bold text-slate-800 hover:text-blue-600 transition cursor-pointer">
                Cơ Chế Khuyến Khích Phát Triển Điện Mặt Trời Mái Nhà Tự Sản Tự Tiêu
              </h5>
              <p class="text-[11px] text-slate-500 mt-0.5 line-clamp-1">
                Miễn trừ giấy phép hoạt động điện lực cho hệ thống tự dùng dưới 1MW, áp dụng chứng nhận công trình xanh.
              </p>
            </div>
          </div>
        </div>

      </section>

    </div>

    <!-- ========================================== -->
    <!-- LEGAL COMPLIANCE & CPM ENGINE (VIEW 2)     -->
    <!-- ========================================== -->
    <div id="investLegalEngineContainer" class="hidden w-full max-w-full min-w-0 space-y-4 sm:space-y-5 animate-in fade-in duration-300">
'''

    if main_open_tag in html:
        html = html.replace(main_open_tag, main_open_tag + "\n" + dashboard_html, 1)
        # Close #investLegalEngineContainer right before </main>
        html = html.replace("</main>", "</div>\n  </main>", 1)

    # 4. Add JavaScript to manage View Modes and Dynamic Dashboard Stats
    js_addon = '''
    // ============================================================
    // EXECUTIVE DASHBOARD CONTROLLER & VIEW SWITCHER (Rev 0.18)
    // ============================================================
    let currentViewMode = localStorage.getItem('INVEST_VIEW_MODE') || 'dashboard';

    function switchViewMode(mode) {
      currentViewMode = mode;
      localStorage.setItem('INVEST_VIEW_MODE', mode);

      const dashEl = document.getElementById('investExecutiveDashboard');
      const legalEl = document.getElementById('investLegalEngineContainer');
      const btnDash = document.getElementById('btnViewDashboard');
      const btnLegal = document.getElementById('btnViewLegalEngine');

      if (mode === 'dashboard') {
        if (dashEl) dashEl.classList.remove('hidden');
        if (legalEl) legalEl.classList.add('hidden');

        if (btnDash) {
          btnDash.className = "px-2.5 sm:px-3 py-1.5 sm:py-1 rounded-md text-xs font-bold transition flex items-center gap-1.5 bg-blue-600 text-white shadow-xs cursor-pointer";
        }
        if (btnLegal) {
          btnLegal.className = "px-2.5 sm:px-3 py-1.5 sm:py-1 rounded-md text-xs font-bold transition flex items-center gap-1.5 text-slate-300 hover:text-white hover:bg-slate-700/60 cursor-pointer";
        }
        updateDashboardViewStats();
      } else {
        if (dashEl) dashEl.classList.add('hidden');
        if (legalEl) legalEl.classList.remove('hidden');

        if (btnDash) {
          btnDash.className = "px-2.5 sm:px-3 py-1.5 sm:py-1 rounded-md text-xs font-bold transition flex items-center gap-1.5 text-slate-300 hover:text-white hover:bg-slate-700/60 cursor-pointer";
        }
        if (btnLegal) {
          btnLegal.className = "px-2.5 sm:px-3 py-1.5 sm:py-1 rounded-md text-xs font-bold transition flex items-center gap-1.5 bg-blue-600 text-white shadow-xs cursor-pointer";
        }
      }

      if (window.lucide) {
        window.lucide.createIcons();
      }
    }

    function filterByPhaseAndSwitch(phasePrefix) {
      switchViewMode('legal');
      const phaseFilterEl = document.getElementById('phaseFilter');
      if (phaseFilterEl) {
        // Find matching option
        for (let i = 0; i < phaseFilterEl.options.length; i++) {
          if (phaseFilterEl.options[i].value.startsWith(phasePrefix)) {
            phaseFilterEl.selectedIndex = i;
            break;
          }
        }
        // Trigger filter event
        renderTable();
      }
    }

    function updateDashboardViewStats() {
      const activeProj = getActiveProject();
      if (!activeProj) return;

      // Update Hero section details
      const heroTitleEl = document.getElementById('heroProjectTitle');
      if (heroTitleEl) heroTitleEl.textContent = activeProj.name || "Dự Án Đầu Tư Tổ Hợp";

      const heroProjIdEl = document.getElementById('heroProjectId');
      if (heroProjIdEl) heroProjIdEl.textContent = activeProj.id || "PROJ-DEFAULT";

      // Calculate task metrics
      const activeTasks = taskList || [];
      const total = activeTasks.length;
      const completed = activeTasks.filter(t => t.completed || t.status === 'Đã hoàn thành').length;
      const inProgress = activeTasks.filter(t => t.status === 'Đang xử lý').length;
      const delayed = activeTasks.filter(t => t.status === 'Bị nghẽn / Trễ hạn').length;
      const percent = total > 0 ? Math.round((completed / total) * 100) : 0;

      const dashPercentEl = document.getElementById('dashLegalPercent');
      if (dashPercentEl) dashPercentEl.textContent = `${percent}%`;

      const dashBarEl = document.getElementById('dashLegalProgressBar');
      if (dashBarEl) dashBarEl.style.width = `${percent}%`;

      const dashRatioEl = document.getElementById('dashCompletedRatio');
      if (dashRatioEl) dashRatioEl.textContent = `${completed}/${total} thủ tục`;

      const dashDelayedEl = document.getElementById('dashDelayedCount');
      if (dashDelayedEl) dashDelayedEl.textContent = `${delayed}`;

      const dashInProgressEl = document.getElementById('dashInProgressCount');
      if (dashInProgressEl) dashInProgressEl.textContent = `${inProgress}`;

      const dashCpmBadgeEl = document.getElementById('dashCpmStatusBadge');
      if (dashCpmBadgeEl) {
        if (delayed > 0) {
          dashCpmBadgeEl.className = "text-amber-700 font-bold bg-amber-50 px-1.5 py-0.5 rounded";
          dashCpmBadgeEl.textContent = "Có điểm nghẽn";
        } else {
          dashCpmBadgeEl.className = "text-emerald-700 font-bold bg-emerald-50 px-1.5 py-0.5 rounded";
          dashCpmBadgeEl.textContent = "Tiến độ chuẩn";
        }
      }

      // Update 6 Phases
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
      }
    }

    // Hook into updateStats to automatically refresh dashboard metrics
    const originalUpdateStats = updateStats;
    updateStats = function() {
      originalUpdateStats();
      updateDashboardViewStats();
    };

    // Auto initialize view mode on page load
    window.addEventListener('DOMContentLoaded', function() {
      switchViewMode(currentViewMode);
    });
'''

    # Insert JS before closing </script>
    html = html.replace("</script>\n</body>", js_addon + "\n</script>\n</body>")

    with open(rev18_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Created {rev18_path}")

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Updated {index_path}")

if __name__ == "__main__":
    build_invest_dashboard()
