import os
import re

def update_invm_dashboard(invm_dir):
    """
    Ensures invm/index.html has the complete JavaScript runtime logic for switchViewMode,
    updateDashboardViewStats, filterByPhaseAndSwitch, and URL param routing.
    Creates index_Rev.019.html and updates index.html.
    """
    index_path = os.path.join(invm_dir, "index.html")
    rev19_path = os.path.join(invm_dir, "index_Rev.019.html")

    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Update revision banner comment
    html = re.sub(
        r"<!-- Vietnam Investment Project Legal Management & M&A Engine Rev \d+\.\d+[^>]*-->",
        "<!-- Vietnam Investment Project Legal Management & M&A Engine Rev 0.19 - Executive Investment Dashboard Runtime Restored & Subdomain Canonical invest.renewablevietnam.com -->",
        html
    )

    # Check if switchViewMode already exists
    if "function switchViewMode" not in html:
        js_addon = """
    // ==========================================
    // EXECUTIVE INVESTMENT DASHBOARD RUNTIME LOGIC (Rev 0.19)
    // ==========================================
    let currentViewMode = 'dashboard';

    function switchViewMode(mode) {
      currentViewMode = mode;
      const dashEl = document.getElementById('investExecutiveDashboard');
      const legalEl = document.getElementById('dashboardRoot');
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
        for (let i = 0; i < phaseFilterEl.options.length; i++) {
          if (phaseFilterEl.options[i].value.startsWith(phasePrefix)) {
            phaseFilterEl.selectedIndex = i;
            break;
          }
        }
        if (typeof renderTable === 'function') renderTable();
      }
    }

    function updateDashboardViewStats() {
      const activeProj = typeof getActiveProject === 'function' ? getActiveProject() : null;
      if (!activeProj) return;

      const heroTitleEl = document.getElementById('heroProjectTitle');
      if (heroTitleEl) heroTitleEl.textContent = activeProj.name || "Dự Án Đầu Tư Tổ Hợp";

      const heroProjIdEl = document.getElementById('heroProjectId');
      if (heroProjIdEl) heroProjIdEl.textContent = activeProj.id || "PROJ-DEFAULT";

      const activeTasks = (typeof taskList !== 'undefined' && Array.isArray(taskList)) ? taskList : [];
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

    // Hook into updateStats
    if (typeof updateStats === 'function') {
      const originalUpdateStats = updateStats;
      updateStats = function() {
        originalUpdateStats();
        updateDashboardViewStats();
      };
    }

    // Auto routing by URL search parameters
    (function handleUrlViewParams() {
      const urlParams = new URLSearchParams(window.location.search);
      const viewParam = urlParams.get('view');
      if (viewParam === 'legal') {
        setTimeout(() => switchViewMode('legal'), 80);
      } else if (viewParam === 'gantt') {
        setTimeout(() => {
          switchViewMode('legal');
          if (typeof openGanttModal === 'function') openGanttModal();
        }, 120);
      } else {
        setTimeout(() => switchViewMode('dashboard'), 80);
      }
    })();
"""
        # Insert before the last </script>
        last_script_idx = html.rfind('</script>')
        if last_script_idx != -1:
            html = html[:last_script_idx] + js_addon + "\n" + html[last_script_idx:]
            print(f"Inserted dashboard runtime logic before last </script> in {invm_dir}")

    # Write Rev.019 and index.html
    with open(rev19_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Created {rev19_path}")

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Updated {index_path}")


def update_root_homepage(repo_dir):
    """
    Updates root index.html to integrate the Executive Investment Dashboard Cockpit,
    updating the navigation links across desktop and mobile, and creating index_Rev.001.html.
    """
    index_path = os.path.join(repo_dir, "index.html")
    rev01_path = os.path.join(repo_dir, "index_Rev.001.html")

    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Update Revision header comment
    rev_header_comment = """<!--
  Renewable Viet Nam - Primary Root Homepage & Renewable Industrial Hub Portal
  Rev 1.11  Executive Investment Cockpit & Subdomain Integration:
            - Integrated National Investment Project Governance Cockpit (invest.renewablevietnam.com).
            - 4-Pillar Executive CapEx & Statutory Compliance Ribbon (Material Design 3 Expressive).
            - 6-Stage Statutory Lifecycle Stage-Gate Pipeline with direct interactive routing.
            - Inter-domain executive navigation jumps for desktop and mobile touch carousels.
            - Deep Midnight Blue Palette (#070A12 canvas, #0D1322 nautical slate, #131B2E indigo navy).
-->"""
    
    html = re.sub(r"<!--\s*Renewable Viet Nam - Primary Root Homepage.*?-->", rev_header_comment, html, flags=re.DOTALL)

    # 2. Update Desktop Navigation: Add "Invest Cockpit"
    old_desktop_nav = '<nav class="hidden md:flex items-center gap-1 font-mono text-[11px] tracking-wider text-inkMuted dark:text-textDarkMuted">'
    new_desktop_nav = '''<nav class="hidden md:flex items-center gap-1 font-mono text-[11px] tracking-wider text-inkMuted dark:text-textDarkMuted">
            <a href="https://invest.renewablevietnam.com/" class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md text-blue-600 dark:text-blue-400 font-semibold bg-blue-500/10 dark:bg-blue-400/10 border border-blue-500/20 hover:bg-blue-500/20 transition-colors" title="Cổng Điều Hành Dự Án Đầu Tư & Quản Trị Pháp Lý">
              <span class="relative flex h-2 w-2 shrink-0">
                <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-blue-400 opacity-75"></span>
                <span class="relative inline-flex rounded-full h-2 w-2 bg-blue-500"></span>
              </span>
              <span>Invest Cockpit</span>
            </a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>'''

    if old_desktop_nav in html and 'href="https://invest.renewablevietnam.com/"' not in html:
        html = html.replace(old_desktop_nav, new_desktop_nav, 1)
        print(f"Updated Desktop Nav in {repo_dir}")

    # 3. Update Mobile Touch Navigation Carousel
    old_mobile_nav = '<nav class="flex md:hidden items-center gap-1.5 overflow-x-auto no-scrollbar pt-1.5 pb-0.5 font-mono text-[11px] tracking-wider whitespace-nowrap w-full -mx-3 px-3 sm:mx-0 sm:px-0">\n        <a href="/livewire/"'
    new_mobile_nav = '''<nav class="flex md:hidden items-center gap-1.5 overflow-x-auto no-scrollbar pt-1.5 pb-0.5 font-mono text-[11px] tracking-wider whitespace-nowrap w-full -mx-3 px-3 sm:mx-0 sm:px-0">
        <a href="https://invest.renewablevietnam.com/" class="inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg text-blue-600 dark:text-blue-400 font-semibold bg-blue-500/10 dark:bg-blue-400/10 border border-blue-500/20 shrink-0">
          <span class="relative flex h-2 w-2 shrink-0">
            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-blue-400 opacity-75"></span>
            <span class="relative inline-flex rounded-full h-2 w-2 bg-blue-500"></span>
          </span>
          <span>Invest Cockpit</span>
        </a>
        <a href="/livewire/"'''

    if old_mobile_nav in html:
        html = html.replace(old_mobile_nav, new_mobile_nav, 1)
        print(f"Updated Mobile Nav in {repo_dir}")

    # 4. Insert Executive Investment Dashboard Section into Homepage
    # Placement: Directly before <section id="powerSizer"
    dashboard_section_html = '''
    <!-- ==================================================================== -->
    <!-- NATIONAL INVESTMENT PROJECT GOVERNANCE & EXECUTIVE COCKPIT           -->
    <!-- Gateway to invest.renewablevietnam.com                               -->
    <!-- ==================================================================== -->
    <section id="investExecutiveCockpit" class="p-5 sm:p-7 rounded-2xl bg-white dark:bg-darkSurface border border-blue-500/30 dark:border-blue-500/20 shadow-md space-y-6 relative overflow-hidden transition-all duration-300">
      
      <!-- Ambient Glow Decorative Element -->
      <div class="absolute -top-24 -right-24 w-80 h-80 bg-blue-500/10 dark:bg-blue-500/5 rounded-full blur-3xl pointer-events-none"></div>

      <!-- Top Header & Primary Command Bar -->
      <div class="flex flex-col lg:flex-row lg:items-center justify-between gap-4 border-b border-borderSlate dark:border-darkBorder pb-5 relative z-10">
        <div class="space-y-1.5 max-w-3xl">
          <div class="flex flex-wrap items-center gap-2">
            <span class="relative flex h-2.5 w-2.5 shrink-0">
              <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-blue-400 opacity-75"></span>
              <span class="relative inline-flex rounded-full h-2.5 w-2.5 bg-blue-600 dark:bg-blue-400"></span>
            </span>
            <span class="font-mono text-[10px] uppercase tracking-wider text-blue-600 dark:text-blue-400 font-bold px-2 py-0.5 rounded bg-blue-500/10 dark:bg-blue-400/10 border border-blue-500/20">
              NATIONAL INVESTMENT GOVERNANCE &middot; STATUTORY STAGE-GATE &middot; CPM PIPELINE
            </span>
            <span class="font-mono text-[10px] text-slate-500 dark:text-slate-400">
              SUBDOMAIN: <a href="https://invest.renewablevietnam.com" target="_blank" rel="noopener noreferrer" class="font-semibold text-blue-600 dark:text-blue-400 hover:underline">invest.renewablevietnam.com</a>
            </span>
          </div>
          <h2 class="text-xl sm:text-2xl font-bold tracking-tight text-inkPrimary dark:text-textDarkPrimary flex items-center gap-2.5">
            <span>Cổng Điều Hành Dự Án Đầu Tư &amp; Quản Trị Pháp Lý Quốc Gia</span>
            <span class="px-2 py-0.5 text-[10px] font-bold bg-blue-600 text-white rounded uppercase tracking-wider hidden sm:inline">Cockpit</span>
          </h2>
          <p class="text-xs sm:text-sm text-inkMuted dark:text-textDarkMuted font-light leading-relaxed">
            Hệ thống quản trị tiến độ đầu tư toàn diện theo Luật Đầu tư 2020, Luật Đất đai 2024, Quy hoạch Điện VIII và Luật Xây dựng. Kiểm soát tiến độ đường găng CPM, phân tích rủi ro tắc nghẽn pháp lý và điều hành dòng vốn đầu tư các dự án công nghiệp - năng lượng trọng điểm.
          </p>
        </div>

        <!-- Primary Action Dispatches -->
        <div class="flex items-center gap-2 flex-wrap shrink-0 relative z-10">
          <a href="https://invest.renewablevietnam.com/" class="inline-flex items-center gap-2 px-4 py-2 rounded-xl bg-blue-600 hover:bg-blue-700 text-white font-semibold text-xs transition shadow-sm hover:shadow-md cursor-pointer">
            <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 3v11.25A2.25 2.25 0 0 0 6 16.5h2.25M3.75 3h-1.5m1.5 0h16.5m0 0h1.5m-1.5 0v11.25A2.25 2.25 0 0 1 18 16.5h-2.25m-7.5 0h7.5m-7.5 0-1 3m8.5-3 1 3m0 0 .5 1.5m-.5-1.5h-9.5m0 0-.5 1.5m.75-9 3-3 2.143 2.143L15.429 8M3 16.5h18" />
            </svg>
            <span>Mở Bảng Điều Hành Cockpit</span>
            <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 6H5.25A2.25 2.25 0 0 0 3 8.25v10.5A2.25 2.25 0 0 0 5.25 21h10.5A2.25 2.25 0 0 0 18 18.75V10.5m-10.5 6L21 3m0 0h-5.25M21 3v5.25" />
            </svg>
          </a>
          <a href="https://invest.renewablevietnam.com/?view=gantt" class="inline-flex items-center gap-1.5 px-3.5 py-2 rounded-xl bg-white dark:bg-darkCard hover:bg-slate-50 dark:hover:bg-slate-800 text-inkPrimary dark:text-textDarkPrimary border border-borderSlate dark:border-darkBorder font-medium text-xs transition shadow-2xs">
            <svg class="w-4 h-4 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M6.75 3v2.25M17.25 3v2.253 3H3.75A2.25 2.25 0 0 0 1.5 7.5v11.25A2.25 2.25 0 0 0 3.75 21h16.5A2.25 2.25 0 0 0 22.5 18.75V7.5A2.25 2.25 0 0 0 20.25 5.25H6.75Z" />
            </svg>
            <span>Biểu Đồ CPM Gantt</span>
          </a>
          <a href="https://invest.renewablevietnam.com/quyhoach/" class="inline-flex items-center gap-1.5 px-3.5 py-2 rounded-xl bg-white dark:bg-darkCard hover:bg-slate-50 dark:hover:bg-slate-800 text-inkPrimary dark:text-textDarkPrimary border border-borderSlate dark:border-darkBorder font-medium text-xs transition shadow-2xs">
            <svg class="w-4 h-4 text-emerald-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M9 6.75V15m6-6v8.25m.503-14.788 4.25 2.125a1.125 1.125 0 0 1 .622 1.006v11.854a1.125 1.125 0 0 1-.622 1.006l-4.75 2.375a1.125 1.125 0 0 1-.948 0l-5-2.5a1.125 1.125 0 0 0-.948 0l-4.75 2.375a1.125 1.125 0 0 1-1.124-.094A1.125 1.125 0 0 1 2.25 19.354V7.5a1.125 1.125 0 0 1 .622-1.006l4.75-2.375a1.125 1.125 0 0 1 .948 0l5 2.5a1.125 1.125 0 0 0 .948 0l4.25-2.125a1.125 1.125 0 0 1 .985-.006Z" />
            </svg>
            <span>Quy Hoạch BXD</span>
          </a>
        </div>
      </div>

      <!-- 4-PILLAR EXECUTIVE KPI METRIC RIBBON (Material Design 3 Expressive) -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3.5 relative z-10">
        
        <!-- Pillar 1: Total CapEx Pipeline -->
        <div class="p-4 rounded-xl bg-slate-50/70 dark:bg-darkCard/80 border border-borderSlate dark:border-darkBorder shadow-2xs flex flex-col justify-between hover:border-blue-400 dark:hover:border-blue-500/50 transition">
          <div class="flex items-center justify-between mb-2">
            <span class="font-mono text-[10.5px] uppercase tracking-wider text-inkMuted dark:text-textDarkMuted font-bold">Tổng Vốn Dự Án (CapEx)</span>
            <span class="p-1.5 rounded-lg bg-blue-500/10 text-blue-600 dark:text-blue-400">
              <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 6v12m-3-2.818.879.659c1.171.879 3.07.879 4.242 0 1.172-.879 1.172-2.303 0-3.182C13.536 12.219 12.768 12 12 12c-.725 0-1.45-.22-2.003-.659-1.106-.879-1.106-2.303 0-3.182s2.9-.879 4.006 0l.415.33M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
              </svg>
            </span>
          </div>
          <div class="flex items-baseline gap-2">
            <span class="text-2xl font-mono font-extrabold text-blue-600 dark:text-blue-400 tracking-tight">28,500</span>
            <span class="text-xs font-bold text-inkPrimary dark:text-textDarkPrimary">Tỷ VNĐ</span>
          </div>
          <p class="text-[11px] text-inkMuted dark:text-textDarkMuted mt-1.5 flex items-center justify-between">
            <span>~1.14 Tỷ USD Quy Mô</span>
            <span class="font-mono text-[10px] text-emerald-600 dark:text-emerald-400 font-semibold">Vốn Vay 80%</span>
          </p>
        </div>

        <!-- Pillar 2: Statutory Legal Procedures -->
        <div class="p-4 rounded-xl bg-slate-50/70 dark:bg-darkCard/80 border border-borderSlate dark:border-darkBorder shadow-2xs flex flex-col justify-between hover:border-blue-400 dark:hover:border-blue-500/50 transition">
          <div class="flex items-center justify-between mb-2">
            <span class="font-mono text-[10.5px] uppercase tracking-wider text-inkMuted dark:text-textDarkMuted font-bold">Chuẩn Hóa Pháp Lý</span>
            <span class="p-1.5 rounded-lg bg-emerald-500/10 text-emerald-600 dark:text-emerald-400">
              <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75 11.25 15 15 9.75M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
              </svg>
            </span>
          </div>
          <div class="flex items-baseline gap-2">
            <span class="text-2xl font-mono font-extrabold text-inkPrimary dark:text-textDarkPrimary tracking-tight">46</span>
            <span class="text-xs font-bold text-inkPrimary dark:text-textDarkPrimary">Thủ Tục Thẩm Quyền</span>
          </div>
          <p class="text-[11px] text-inkMuted dark:text-textDarkMuted mt-1.5 flex items-center justify-between">
            <span>6 Giai Đoạn Thẩm Định</span>
            <span class="font-mono text-[10px] text-blue-600 dark:text-blue-400 font-semibold">100% Khung Luật</span>
          </p>
        </div>

        <!-- Pillar 3: CPM Critical Path & Bottlenecks -->
        <div class="p-4 rounded-xl bg-slate-50/70 dark:bg-darkCard/80 border border-borderSlate dark:border-darkBorder shadow-2xs flex flex-col justify-between hover:border-blue-400 dark:hover:border-blue-500/50 transition">
          <div class="flex items-center justify-between mb-2">
            <span class="font-mono text-[10.5px] uppercase tracking-wider text-inkMuted dark:text-textDarkMuted font-bold">Đường Găng CPM &amp; Rủi Ro</span>
            <span class="p-1.5 rounded-lg bg-amber-500/10 text-amber-600 dark:text-amber-400">
              <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v3.75m-9.303 3.376c-.866 1.5.217 3.374 1.948 3.374h14.71c1.73 0 2.813-1.874 1.948-3.374L13.949 3.378c-.866-1.5-3.032-1.5-3.898 0L2.697 16.126ZM12 15.75h.007v.008H12v-.008Z" />
              </svg>
            </span>
          </div>
          <div class="flex items-baseline gap-2">
            <span class="text-2xl font-mono font-extrabold text-amber-600 dark:text-amber-400 tracking-tight">12/46</span>
            <span class="text-xs font-bold text-inkPrimary dark:text-textDarkPrimary">Nút Thắt Trọng Yếu</span>
          </div>
          <p class="text-[11px] text-inkMuted dark:text-textDarkMuted mt-1.5 flex items-center justify-between">
            <span>Quy Hoạch &middot; GPMB &middot; ĐTM</span>
            <span class="font-mono text-[10px] text-amber-600 dark:text-amber-400 font-semibold">Kiểm Soát Real-time</span>
          </p>
        </div>

        <!-- Pillar 4: Industrial Land & Infrastructure -->
        <div class="p-4 rounded-xl bg-slate-50/70 dark:bg-darkCard/80 border border-borderSlate dark:border-darkBorder shadow-2xs flex flex-col justify-between hover:border-blue-400 dark:hover:border-blue-500/50 transition">
          <div class="flex items-center justify-between mb-2">
            <span class="font-mono text-[10.5px] uppercase tracking-wider text-inkMuted dark:text-textDarkMuted font-bold">Hạ Tầng &amp; Năng Lượng</span>
            <span class="p-1.5 rounded-lg bg-teal-500/10 text-teal-600 dark:text-teal-400">
              <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 13.5l10.5-11.25L12 10.5h8.25L9.75 21.75 12 13.5H3.75z" />
              </svg>
            </span>
          </div>
          <div class="flex items-baseline gap-2">
            <span class="text-2xl font-mono font-extrabold text-teal-600 dark:text-teal-400 tracking-tight">1,200+</span>
            <span class="text-xs font-bold text-inkPrimary dark:text-textDarkPrimary">Hécta Quỹ Đất</span>
          </div>
          <p class="text-[11px] text-inkMuted dark:text-textDarkMuted mt-1.5 flex items-center justify-between">
            <span>150 MWp Điện Tự Dùng</span>
            <span class="font-mono text-[10px] text-teal-600 dark:text-teal-400 font-semibold">Tích Hợp DPPA</span>
          </p>
        </div>
      </div>

      <!-- 6-STAGE STATUTORY LIFECYCLE STAGE-GATE PIPELINE -->
      <div class="space-y-3 relative z-10">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-2">
            <span class="w-1.5 h-4 bg-blue-600 rounded-full"></span>
            <h3 class="text-xs font-bold uppercase tracking-wider text-inkPrimary dark:text-textDarkPrimary">
              Tiến Trình 6 Giai Đoạn Thẩm Quyền Pháp Lý &amp; Đầu Tư (Stage-Gate Pipeline)
            </h3>
          </div>
          <a href="https://invest.renewablevietnam.com/?view=legal" class="text-xs font-bold text-blue-600 dark:text-blue-400 hover:underline flex items-center gap-1">
            <span>Chi Tiết Toàn Bộ 46 Thủ Tục</span>
            <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5 21 12m0 0-7.5 7.5M21 12H3" />
            </svg>
          </a>
        </div>

        <!-- 6 Phase Interactive Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
          
          <!-- Phase 1 -->
          <a href="https://invest.renewablevietnam.com/?view=legal" class="p-3.5 rounded-xl border border-borderSlate dark:border-darkBorder bg-slate-50/50 dark:bg-darkCard/50 hover:bg-white dark:hover:bg-darkCard hover:border-blue-500 transition group block">
            <div class="flex items-center justify-between mb-1.5">
              <span class="px-2 py-0.5 rounded bg-slate-200 dark:bg-slate-700 text-slate-800 dark:text-slate-200 text-[9.5px] font-extrabold uppercase">Giai Đoạn 1</span>
              <span class="text-[11px] font-mono font-bold text-slate-500 dark:text-slate-400">6 Thủ Tục</span>
            </div>
            <h4 class="text-xs font-bold text-inkPrimary dark:text-textDarkPrimary group-hover:text-blue-600 dark:group-hover:text-blue-400 transition mb-1 leading-snug">
              Chuẩn Bị Đầu Tư &amp; Chủ Trương
            </h4>
            <p class="text-[11px] text-inkMuted dark:text-textDarkMuted line-clamp-2 mb-2.5">
              Khảo sát địa điểm, lập đề xuất dự án, thẩm định Sở KH&amp;ĐT và phê duyệt Chấp thuận chủ trương tại UBND Tỉnh / Thủ tướng.
            </p>
            <div class="w-full bg-slate-200 dark:bg-slate-700 h-1.5 rounded-full overflow-hidden">
              <div class="bg-blue-600 h-full rounded-full" style="width: 100%;"></div>
            </div>
          </a>

          <!-- Phase 2 -->
          <a href="https://invest.renewablevietnam.com/?view=legal" class="p-3.5 rounded-xl border border-borderSlate dark:border-darkBorder bg-slate-50/50 dark:bg-darkCard/50 hover:bg-white dark:hover:bg-darkCard hover:border-blue-500 transition group block">
            <div class="flex items-center justify-between mb-1.5">
              <span class="px-2 py-0.5 rounded bg-slate-200 dark:bg-slate-700 text-slate-800 dark:text-slate-200 text-[9.5px] font-extrabold uppercase">Giai Đoạn 2</span>
              <span class="text-[11px] font-mono font-bold text-slate-500 dark:text-slate-400">8 Thủ Tục</span>
            </div>
            <h4 class="text-xs font-bold text-inkPrimary dark:text-textDarkPrimary group-hover:text-blue-600 dark:group-hover:text-blue-400 transition mb-1 leading-snug">
              Quy Hoạch Xây Dựng (1/2000 &middot; 1/500)
            </h4>
            <p class="text-[11px] text-inkMuted dark:text-textDarkMuted line-clamp-2 mb-2.5">
              Lập Nhiệm vụ &amp; Đồ án quy hoạch phân khu 1/2000, quy hoạch chi tiết 1/500 trình Sở Xây Dựng thẩm định và UBND Tỉnh phê duyệt.
            </p>
            <div class="w-full bg-slate-200 dark:bg-slate-700 h-1.5 rounded-full overflow-hidden">
              <div class="bg-blue-600 h-full rounded-full" style="width: 75%;"></div>
            </div>
          </a>

          <!-- Phase 3 -->
          <a href="https://invest.renewablevietnam.com/?view=legal" class="p-3.5 rounded-xl border border-borderSlate dark:border-darkBorder bg-slate-50/50 dark:bg-darkCard/50 hover:bg-white dark:hover:bg-darkCard hover:border-blue-500 transition group block">
            <div class="flex items-center justify-between mb-1.5">
              <span class="px-2 py-0.5 rounded bg-slate-200 dark:bg-slate-700 text-slate-800 dark:text-slate-200 text-[9.5px] font-extrabold uppercase">Giai Đoạn 3</span>
              <span class="text-[11px] font-mono font-bold text-slate-500 dark:text-slate-400">9 Thủ Tục</span>
            </div>
            <h4 class="text-xs font-bold text-inkPrimary dark:text-textDarkPrimary group-hover:text-blue-600 dark:group-hover:text-blue-400 transition mb-1 leading-snug">
              Giao Đất, Thuê Đất &amp; GPMB
            </h4>
            <p class="text-[11px] text-inkMuted dark:text-textDarkMuted line-clamp-2 mb-2.5">
              Thu hồi đất, đền bù giải phóng mặt bằng, chuyển mục đích sử dụng đất, định giá đất cụ thể và ký hợp đồng thuê đất Sở TN&amp;MT.
            </p>
            <div class="w-full bg-slate-200 dark:bg-slate-700 h-1.5 rounded-full overflow-hidden">
              <div class="bg-blue-600 h-full rounded-full" style="width: 50%;"></div>
            </div>
          </a>

          <!-- Phase 4 -->
          <a href="https://invest.renewablevietnam.com/?view=legal" class="p-3.5 rounded-xl border border-borderSlate dark:border-darkBorder bg-slate-50/50 dark:bg-darkCard/50 hover:bg-white dark:hover:bg-darkCard hover:border-blue-500 transition group block">
            <div class="flex items-center justify-between mb-1.5">
              <span class="px-2 py-0.5 rounded bg-slate-200 dark:bg-slate-700 text-slate-800 dark:text-slate-200 text-[9.5px] font-extrabold uppercase">Giai Đoạn 4</span>
              <span class="text-[11px] font-mono font-bold text-slate-500 dark:text-slate-400">9 Thủ Tục</span>
            </div>
            <h4 class="text-xs font-bold text-inkPrimary dark:text-textDarkPrimary group-hover:text-blue-600 dark:group-hover:text-blue-400 transition mb-1 leading-snug">
              Thiết Kế Cơ Sở, PCCC &amp; ĐTM
            </h4>
            <p class="text-[11px] text-inkMuted dark:text-textDarkMuted line-clamp-2 mb-2.5">
              Thẩm định Báo cáo nghiên cứu khả thi (FS), phê duyệt Báo cáo ĐTM Bộ TN&amp;MT, thẩm duyệt thiết kế PCCC Cục C07.
            </p>
            <div class="w-full bg-slate-200 dark:bg-slate-700 h-1.5 rounded-full overflow-hidden">
              <div class="bg-blue-600 h-full rounded-full" style="width: 35%;"></div>
            </div>
          </a>

          <!-- Phase 5 -->
          <a href="https://invest.renewablevietnam.com/?view=legal" class="p-3.5 rounded-xl border border-borderSlate dark:border-darkBorder bg-slate-50/50 dark:bg-darkCard/50 hover:bg-white dark:hover:bg-darkCard hover:border-blue-500 transition group block">
            <div class="flex items-center justify-between mb-1.5">
              <span class="px-2 py-0.5 rounded bg-slate-200 dark:bg-slate-700 text-slate-800 dark:text-slate-200 text-[9.5px] font-extrabold uppercase">Giai Đoạn 5</span>
              <span class="text-[11px] font-mono font-bold text-slate-500 dark:text-slate-400">8 Thủ Tục</span>
            </div>
            <h4 class="text-xs font-bold text-inkPrimary dark:text-textDarkPrimary group-hover:text-blue-600 dark:group-hover:text-blue-400 transition mb-1 leading-snug">
              Cấp GPXD &amp; Thi Công Hạ Tầng
            </h4>
            <p class="text-[11px] text-inkMuted dark:text-textDarkMuted line-clamp-2 mb-2.5">
              Hồ sơ cấp Giấy phép xây dựng, thông báo khởi công, đấu thầu EPC thi công hạ tầng kỹ thuật, đường giao thông và trạm biến áp.
            </p>
            <div class="w-full bg-slate-200 dark:bg-slate-700 h-1.5 rounded-full overflow-hidden">
              <div class="bg-blue-600 h-full rounded-full" style="width: 15%;"></div>
            </div>
          </a>

          <!-- Phase 6 -->
          <a href="https://invest.renewablevietnam.com/?view=legal" class="p-3.5 rounded-xl border border-borderSlate dark:border-darkBorder bg-slate-50/50 dark:bg-darkCard/50 hover:bg-white dark:hover:bg-darkCard hover:border-blue-500 transition group block">
            <div class="flex items-center justify-between mb-1.5">
              <span class="px-2 py-0.5 rounded bg-slate-200 dark:bg-slate-700 text-slate-800 dark:text-slate-200 text-[9.5px] font-extrabold uppercase">Giai Đoạn 6</span>
              <span class="text-[11px] font-mono font-bold text-slate-500 dark:text-slate-400">6 Thủ Tục</span>
            </div>
            <h4 class="text-xs font-bold text-inkPrimary dark:text-textDarkPrimary group-hover:text-blue-600 dark:group-hover:text-blue-400 transition mb-1 leading-snug">
              Nghiệm Thu &amp; Vận Hành Khai Thác
            </h4>
            <p class="text-[11px] text-inkMuted dark:text-textDarkMuted line-clamp-2 mb-2.5">
              Nghiệm thu PCCC, cấp Giấy phép môi trường (GPMT), kiểm tra công tác nghiệm thu Sở Xây Dựng và bàn giao hạ tầng cho nhà đầu tư thứ cấp.
            </p>
            <div class="w-full bg-slate-200 dark:bg-slate-700 h-1.5 rounded-full overflow-hidden">
              <div class="bg-blue-600 h-full rounded-full" style="width: 5%;"></div>
            </div>
          </a>
        </div>
      </div>

      <!-- Quick Fast-Action Tools Dispatch Footer -->
      <div class="p-3.5 rounded-xl bg-slate-100/80 dark:bg-darkCard/90 border border-borderSlate dark:border-darkBorder flex flex-col sm:flex-row sm:items-center justify-between gap-3 text-xs text-inkMuted dark:text-textDarkMuted relative z-10">
        <div class="flex items-center gap-2">
          <span class="font-mono text-[10.5px] text-blue-600 dark:text-blue-400 font-bold uppercase">Hệ Thống Trực Tuyến:</span>
          <span class="font-light">Đồng bộ dữ liệu thời gian thực giữa Báo cáo Pháp lý A4, CPM Gantt &amp; CSDL Quy hoạch Quốc gia.</span>
        </div>
        <div class="flex items-center gap-3 shrink-0 font-mono text-[11px]">
          <a href="https://invest.renewablevietnam.com/" class="text-blue-600 dark:text-blue-400 font-semibold hover:underline flex items-center gap-1">
            <span>invest.renewablevietnam.com</span>
            <svg class="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round" d="M13.5 6H5.25A2.25 2.25 0 0 0 3 8.25v10.5A2.25 2.25 0 0 0 5.25 21h10.5A2.25 2.25 0 0 0 18 18.75V10.5m-10.5 6L21 3m0 0h-5.25M21 3v5.25" />
            </svg>
          </a>
        </div>
      </div>

    </section>
'''

    target_anchor = '<section id="powerSizer"'
    if target_anchor in html and 'id="investExecutiveCockpit"' not in html:
        html = html.replace(target_anchor, dashboard_section_html + "\n    " + target_anchor, 1)
        print(f"Inserted Executive Investment Dashboard Section into {repo_dir}")

    # Write Rev.001 and index.html
    with open(rev01_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Created {rev01_path}")

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Updated {index_path}")


def main():
    qking_dir = r"G:\My Drive\7. AI\Qking232.github.io"
    rvn_dir = r"G:\My Drive\7. AI\RenewableVietNam"

    # Step 1: Update invm dashboard logic
    print("--- 1. Updating invm dashboard runtime logic ---")
    update_invm_dashboard(os.path.join(rvn_dir, "invm"))
    update_invm_dashboard(os.path.join(qking_dir, "invm"))

    # Step 2: Update root homepage
    print("--- 2. Updating root homepage ---")
    update_root_homepage(rvn_dir)
    update_root_homepage(qking_dir)

    print("--- Completed all updates successfully ---")

if __name__ == "__main__":
    main()
