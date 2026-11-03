#!/usr/bin/env python3
"""
Standardize Homepage Header across all pages in RenewableVietNam and Qking232.github.io.
Blueprint: renewablevietnam.com/index.html
"""

import os
import re
import shutil
import hashlib

REPOS = [
    r"G:\My Drive\7. AI\RenewableVietNam",
    r"G:\My Drive\7. AI\Qking232.github.io"
]

CONFIG = [
    {
        "path": "projectenergy/index.html",
        "active": "energy",
        "subtitle": "Energy Infrastructure",
        "rev": "index_Rev.007.html"
    },
    {
        "path": "industrial/index.html",
        "active": "industrial",
        "subtitle": "Industrial Siting & Hubs",
        "rev": "index_Rev.006.html"
    },
    {
        "path": "industrial/calculator/index.html",
        "active": "industrial",
        "subtitle": "DPPA Power Sizer",
        "rev": "index_Rev.002.html"
    },
    {
        "path": "evcharging/index.html",
        "active": "ev",
        "subtitle": "EV Charging Ecosystem",
        "rev": "index_Rev.006.html"
    },
    {
        "path": "evcharging/ev/index.html",
        "active": "ev",
        "subtitle": "EV Route Planner",
        "rev": "index_Rev.004.html"
    },
    {
        "path": "livewire/index.html",
        "active": "cockpit",
        "subtitle": "Real-Time Power Wire",
        "rev": "index_Rev.004.html"
    },
    {
        "path": "project/index.html",
        "active": "legal",
        "subtitle": "Project Management",
        "rev": "index_Rev.005.html"
    },
    {
        "path": "calculator/index.html",
        "active": "industrial",
        "subtitle": "Power Sizer & Tariffs",
        "rev": "index_Rev.002.html",
        "repo2_only": True
    }
]

def render_header(active_nav, subtitle):
    # Desktop pill classes
    active_desktop = "px-2.5 py-1 rounded-md text-teal-700 dark:text-teal-300 font-medium bg-slate-100 dark:bg-slate-800 transition-colors"
    inactive_desktop = "px-2.5 py-1 rounded-md hover:text-slate-900 dark:hover:text-slate-100 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors"
    dot = '<span class="text-slate-300 dark:text-slate-700">&middot;</span>'

    # Mobile pill classes
    active_mobile = "px-2.5 py-1 rounded-md text-teal-700 dark:text-teal-300 font-semibold bg-slate-100 dark:bg-slate-800 border border-teal-500/20 shrink-0"
    inactive_mobile = "px-2.5 py-1 rounded-md text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200 bg-slate-50 dark:bg-slate-800/50 border border-slate-200/60 dark:border-slate-700/50 shrink-0"

    cockpit_d = active_desktop if active_nav == "cockpit" else inactive_desktop
    energy_d = active_desktop if active_nav == "energy" else inactive_desktop
    industrial_d = active_desktop if active_nav == "industrial" else inactive_desktop
    ev_d = active_desktop if active_nav == "ev" else inactive_desktop
    legal_d = active_desktop if active_nav == "legal" else inactive_desktop

    cockpit_m = active_mobile if active_nav == "cockpit" else inactive_mobile
    energy_m = active_mobile if active_nav == "energy" else inactive_mobile
    industrial_m = active_mobile if active_nav == "industrial" else inactive_mobile
    ev_m = active_mobile if active_nav == "ev" else inactive_mobile
    legal_m = active_mobile if active_nav == "legal" else inactive_mobile

    header_html = f"""  <header class="sticky top-0 z-50 w-full bg-white/90 dark:bg-slate-900/90 backdrop-blur-md border-b border-slate-200/70 dark:border-slate-800 px-3 sm:px-6 lg:px-8 transition-colors shadow-xs">
    <div class="w-full max-w-[1920px] 2xl:max-w-full mx-auto px-4 sm:px-6 lg:px-8 xl:px-12 flex items-center justify-between py-2.5 sm:py-3">
      <div class="flex items-center gap-6">
        <a href="https://renewablevietnam.com/" class="flex items-center gap-2.5 group shrink-0" aria-label="Renewable Vietnam home">
          <img src="/assets/images/logo.svg" alt="Renewable Viet Nam Mark" width="28" height="28" class="w-7 h-7 rounded-lg shrink-0 opacity-90 group-hover:opacity-100 transition-opacity" />
          <div class="flex flex-col">
            <span class="text-[12px] font-mono uppercase tracking-[0.16em] text-slate-800 dark:text-slate-200 font-semibold leading-tight">
              RENEWABLE VIETNAM
            </span>
            <span class="text-[9px] font-mono tracking-wider text-slate-500 dark:text-slate-400 uppercase">
              {subtitle}
            </span>
          </div>
        </a>

        <!-- Desktop Quick Jump Navigation -->
        <nav class="hidden md:flex items-center gap-1 font-mono text-[11px] text-slate-600 dark:text-slate-400">
          <a href="https://renewablevietnam.com/" class="{cockpit_d}">Cockpit</a>
          {dot}
          <a href="https://energy.renewablevietnam.com/" class="{energy_d}">Energy</a>
          {dot}
          <a href="https://industrial.renewablevietnam.com/" class="{industrial_d}">Industrial</a>
          {dot}
          <a href="https://ev.renewablevietnam.com/" class="{ev_d}">EV Tech</a>
          {dot}
          <a href="https://legal.renewablevietnam.com/" class="{legal_d}">Legal</a>
        </nav>
      </div>

      <!-- Controls & Theme -->
      <div class="flex items-center gap-2">
        <div class="hidden sm:flex items-center gap-1.5 px-2.5 py-1 rounded-md bg-slate-100 dark:bg-slate-800 border border-slate-200/60 dark:border-slate-700/50 font-mono text-[10px] text-slate-600 dark:text-slate-400">
          <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
          <span>4 Edge Gateways Live</span>
        </div>

        <button id="themeToggleBtn" aria-label="Toggle Theme" class="flex items-center justify-center w-8 h-8 rounded-lg bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300 shadow-xs hover:bg-slate-50 dark:hover:bg-slate-700/60 transition-all cursor-pointer">
          <svg id="sunIcon" class="hidden w-4 h-4 text-amber-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.8">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 3v2.25m6.364.386-1.591 1.591M21 12h-2.25m-.386 6.364-1.591-1.591M12 18.75V21m-4.773-4.227-1.591 1.591M5.25 12H3m4.227-4.773L5.636 5.636M15.75 12a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0Z" />
          </svg>
          <svg id="moonIcon" class="w-4 h-4 text-slate-600 dark:text-slate-300" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.8">
            <path stroke-linecap="round" stroke-linejoin="round" d="M21.752 15.002A9.72 9.72 0 0 1 18 15.75c-5.385 0-9.75-4.365-9.75-9.75 0-1.33.266-2.597.748-3.752A9.753 9.753 0 0 0 3 11.25C3 16.635 7.365 21 12.75 21a9.753 9.753 0 0 0 9.002-5.998Z" />
          </svg>
        </button>
      </div>
    </div>
    <!-- Mobile Quick Navigation Ribbon -->
    <div class="flex items-center gap-1.5 overflow-x-auto no-scrollbar md:hidden px-4 pb-2 pt-1 border-t border-slate-100 dark:border-slate-800 font-mono text-[10px]">
      <a href="https://renewablevietnam.com/" class="{cockpit_m}">Cockpit</a>
      <a href="https://energy.renewablevietnam.com/" class="{energy_m}">Energy</a>
      <a href="https://industrial.renewablevietnam.com/" class="{industrial_m}">Industrial</a>
      <a href="https://ev.renewablevietnam.com/" class="{ev_m}">EV Tech</a>
      <a href="https://legal.renewablevietnam.com/" class="{legal_m}">Legal</a>
    </div>
  </header>"""
    return header_html

print("=== DEPLOYING STANDARDIZED HOMEPAGE HEADER ACROSS ALL PAGES ===")

header_regex = re.compile(r'<header.*?</header>', re.DOTALL)

for repo_idx, repo in enumerate(REPOS):
    repo_name = os.path.basename(repo)
    print(f"\nProcessing Repository: {repo_name}")
    for item in CONFIG:
        rel_path = item["path"]
        if item.get("repo2_only") and repo_idx == 0:
            continue

        full_path = os.path.join(repo, rel_path)
        if not os.path.exists(full_path):
            print(f"  [SKIP] Not found: {rel_path}")
            continue

        dir_path = os.path.dirname(full_path)
        rev_path = os.path.join(dir_path, item["rev"])

        # 1. Non-destructive revision backup
        shutil.copyfile(full_path, rev_path)
        print(f"  [BACKUP] {rel_path} -> {item['rev']}")

        # 2. Read and replace header
        with open(full_path, "r", encoding="utf-8") as fp:
            content = fp.read()

        new_hdr = render_header(item["active"], item["subtitle"])
        new_content, count = header_regex.subn(new_hdr, content, count=1)

        if count == 0:
            print(f"  [WARN] No <header> tag found in {rel_path}")
        else:
            with open(full_path, "w", encoding="utf-8") as fp:
                fp.write(new_content)
            print(f"  [UPDATED] {rel_path} with standardized header")

# Synchronize repo1 to repo2 for files that exist in both
print("\n=== SYNCHRONIZING TO QKING232.GITHUB.IO ===")
for item in CONFIG:
    rel_path = item["path"]
    p1 = os.path.join(REPOS[0], rel_path)
    p2 = os.path.join(REPOS[1], rel_path)
    if os.path.exists(p1) and os.path.exists(p2):
        shutil.copyfile(p1, p2)
        print(f"  Synced {rel_path}")

# Parity Check
print("\n=== VERIFYING CRYPTOGRAPHIC SHA-256 PARITY ===")
parity_all_pass = True
for item in CONFIG:
    rel_path = item["path"]
    p1 = os.path.join(REPOS[0], rel_path)
    p2 = os.path.join(REPOS[1], rel_path)
    if os.path.exists(p1) and os.path.exists(p2):
        h1 = hashlib.sha256(open(p1, "rb").read()).hexdigest()
        h2 = hashlib.sha256(open(p2, "rb").read()).hexdigest()
        if h1 == h2:
            print(f"  [PASS] {rel_path:35}: {h1[:8]}")
        else:
            print(f"  [FAIL] {rel_path:35}: REPO1={h1[:8]} REPO2={h2[:8]}")
            parity_all_pass = False

print("\nResult:", "100% PARITY VERIFIED" if parity_all_pass else "PARITY MISMATCH")
