import os
import re

def fix_invm_repo(repo_invm_dir):
    index_path = os.path.join(repo_invm_dir, "index.html")
    rev20_path = os.path.join(repo_invm_dir, "index_Rev.020.html")

    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Update Revision header comment
    html = re.sub(
        r"<!-- Vietnam Investment Project Legal Management & M&A Engine Rev \d+\.\d+[^>]*-->",
        "<!-- Vietnam Investment Project Legal Management & M&A Engine Rev 0.20 - Legal Documents Checklist & CPM Engine Visibility Restored - invest.renewablevietnam.com -->",
        html
    )

    # 2. Fix the nested hidden container
    target_block = '''    <!-- ========================================== -->
    <!-- LEGAL COMPLIANCE & CPM ENGINE (VIEW 2)     -->
    <!-- ========================================== -->
    <div id="investLegalEngineContainer" class="hidden w-full max-w-full min-w-0 space-y-4 sm:space-y-5 animate-in fade-in duration-300">

    <div id="dashboardRoot" class="w-full max-w-full min-w-0 space-y-4 sm:space-y-5">'''

    clean_block = '''    <!-- ========================================== -->
    <!-- LEGAL COMPLIANCE & CPM ENGINE (VIEW 2)     -->
    <!-- ========================================== -->
    <div id="dashboardRoot" class="hidden w-full max-w-full min-w-0 space-y-4 sm:space-y-5 animate-in fade-in duration-300">'''

    if target_block in html:
        html = html.replace(target_block, clean_block, 1)
        print(f"Cleaned container nesting in {repo_invm_dir}")
        
        # Remove the extra </div> before </main>
        old_main_close = "</div>\n  </main>"
        if old_main_close in html:
            html = html.replace(old_main_close, "</main>", 1)
            print(f"Removed extra closing div before </main> in {repo_invm_dir}")

    # 3. Harden switchViewMode runtime implementation
    old_switch_pattern = r"// ==========================================\s*// EXECUTIVE INVESTMENT DASHBOARD RUNTIME LOGIC.*?(?=\(function handleUrlViewParams)"
    
    new_switch_code = """// ==========================================
    // EXECUTIVE INVESTMENT DASHBOARD RUNTIME LOGIC (Rev 0.20)
    // ==========================================
    let currentViewMode = 'dashboard';

    function switchViewMode(mode) {
      currentViewMode = mode;
      try {
        localStorage.setItem('INVEST_VIEW_MODE', mode);
      } catch(e) {}

      const dashEl = document.getElementById('investExecutiveDashboard');
      const legalEl = document.getElementById('dashboardRoot');
      const legalContainerEl = document.getElementById('investLegalEngineContainer');
      const btnDash = document.getElementById('btnViewDashboard');
      const btnLegal = document.getElementById('btnViewLegalEngine');

      if (mode === 'dashboard') {
        if (dashEl) dashEl.classList.remove('hidden');
        if (legalEl) legalEl.classList.add('hidden');
        if (legalContainerEl) legalContainerEl.classList.add('hidden');
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
        if (legalContainerEl) legalContainerEl.classList.remove('hidden');
        if (btnDash) {
          btnDash.className = "px-2.5 sm:px-3 py-1.5 sm:py-1 rounded-md text-xs font-bold transition flex items-center gap-1.5 text-slate-300 hover:text-white hover:bg-slate-700/60 cursor-pointer";
        }
        if (btnLegal) {
          btnLegal.className = "px-2.5 sm:px-3 py-1.5 sm:py-1 rounded-md text-xs font-bold transition flex items-center gap-1.5 bg-blue-600 text-white shadow-xs cursor-pointer";
        }
        if (typeof render === 'function') {
          render();
        } else {
          if (typeof renderTable === 'function') renderTable();
          if (typeof updateStats === 'function') updateStats();
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

    """

    html = re.sub(old_switch_pattern, new_switch_code, html, flags=re.DOTALL)

    # 4. Save Rev.020 and index.html
    with open(rev20_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Created {rev20_path}")

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Updated {index_path}")

def main():
    rvn_invm = r"G:\My Drive\7. AI\RenewableVietNam\invm"
    qking_invm = r"G:\My Drive\7. AI\Qking232.github.io\invm"

    print("--- Fixing Legal Checklist Visibility in RenewableVietNam ---")
    fix_invm_repo(rvn_invm)

    print("--- Fixing Legal Checklist Visibility in Qking232.github.io ---")
    fix_invm_repo(qking_invm)

    print("--- Execution Complete ---")

if __name__ == "__main__":
    main()
