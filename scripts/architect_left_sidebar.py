#!/usr/bin/env python3
"""
====================================================================
Architect Dedicated Left Sidebar Workspace for Clean Power Sizer,
EVN Tariff Estimator & EU Green Indicators
====================================================================
Transforms the single-column stacked layout into a responsive 2-column
workspace with sticky left sidebar:
  - Left Sidebar (<aside id="toolsSidebar">):
      • Utility Toolkit Header
      • Compact 3-Tab Selector (Power Sizer, EVN Tariff, Green CBAM)
      • Tab 1: Corporate Power Sizer
      • Tab 2: EVN Electricity Tariff Estimator
      • Tab 3: Green Indicators (EU CBAM & Principles)
  - Right Workspace:
      • Real-Time Market Intelligence Wire (#marketWire)
      • Hero Header & PDP8 Statutory Telemetry Tracker
      • Interactive Industrial Zone Directory & GIS Map (#hubs)
Synchronized across all 4 production files:
  1. RenewableVietNam/index.html
  2. RenewableVietNam/green/index.html
  3. Qking232.github.io/index.html
  4. Qking232.github.io/green/index.html
====================================================================
"""

import os
import re

TARGET_FILES = [
    r"G:\My Drive\7. AI\Gemini\RenewableVietNam\index.html",
    r"G:\My Drive\7. AI\Gemini\RenewableVietNam\green\index.html",
    r"G:\My Drive\7. AI\Gemini\Qking232.github.io\index.html",
    r"G:\My Drive\7. AI\Gemini\Qking232.github.io\green\index.html",
]

def refactor_file(filepath):
    if not os.path.exists(filepath):
        print(f"[WARN] File not found: {filepath}")
        return False

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    crlf = "\r\n" in content
    le = "\r\n" if crlf else "\n"

    def norm(s):
        return s.replace("\r\n", "\n").replace("\n", le)

    # 1. Expand max-w-6xl to max-w-7xl on header, main, and footer
    content = content.replace(
        '<header class="relative z-20 w-full max-w-6xl mx-auto flex items-center justify-between pb-6 border-b border-borderSlate dark:border-darkBorder">',
        '<header class="relative z-20 w-full max-w-7xl mx-auto flex items-center justify-between pb-6 border-b border-borderSlate dark:border-darkBorder">'
    )
    content = content.replace(
        '<footer class="relative z-10 w-full max-w-6xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-y-2 pt-8 sm:pt-10 border-t border-borderSlate dark:border-darkBorder text-[11px] font-mono text-inkMuted dark:text-textDarkMuted">',
        '<footer class="relative z-10 w-full max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-y-2 pt-8 sm:pt-10 border-t border-borderSlate dark:border-darkBorder text-[11px] font-mono text-inkMuted dark:text-textDarkMuted">'
    )

    # Update top navbar button to point to #toolsSidebar
    old_nav_calc = """      <a href="#calculator" class="hidden sm:inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg font-mono text-[11px] text-inkPrimary dark:text-textDarkPrimary bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder hover:border-teal-500 dark:hover:border-teal-400/40 transition-all shadow-sm">
        <svg class="w-3.5 h-3.5 text-teal-500 dark:text-teal-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z" />
        </svg>
        <span>Power Sizer</span>
      </a>"""

    new_nav_calc = """      <a href="#toolsSidebar" class="hidden sm:inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg font-mono text-[11px] text-inkPrimary dark:text-textDarkPrimary bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder hover:border-teal-500 dark:hover:border-teal-400/40 transition-all shadow-sm">
        <svg class="w-3.5 h-3.5 text-teal-500 dark:text-teal-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
        </svg>
        <span>Tools Sidebar</span>
      </a>"""

    content = content.replace(norm(old_nav_calc), norm(new_nav_calc))

    # 2. Extract Calculator section
    calc_start_marker = "<!-- CLEAN POWER & EVN TARIFF CALCULATOR SUITE"
    if calc_start_marker not in content:
        calc_start_marker = '<section id="calculator"'
    
    idx_calc_start = content.find(calc_start_marker)
    # Find preceding separator comment if any
    sep_marker = "<!-- ==================================================================== -->"
    idx_sep = content.rfind(sep_marker, 0, idx_calc_start)
    if idx_sep != -1 and idx_calc_start - idx_sep < 120:
        actual_calc_start = idx_sep
    else:
        actual_calc_start = idx_calc_start

    idx_main_close = content.find("</main>")
    if actual_calc_start == -1 or idx_main_close == -1:
        print(f"[ERROR] Could not find calculator or main closing tag in {filepath}")
        return False

    calc_raw = content[actual_calc_start:idx_main_close].strip()

    # Refactor internal grid layout of calculator to fit sidebar:
    # 1. Replace multi-column grid classes in corporate, evn, green containers with single-column space-y-4
    calc_raw = calc_raw.replace('grid grid-cols-1 lg:grid-cols-12 gap-6 items-start', 'grid grid-cols-1 gap-4 items-start')
    calc_raw = calc_raw.replace('class="lg:col-span-6 space-y-4', 'class="w-full space-y-4')
    calc_raw = calc_raw.replace('class="lg:col-span-6 p-4 rounded-xl', 'class="w-full p-4 rounded-xl')

    # 2. Refactor Tab switcher buttons to compact 3-column grid
    tab_switcher_old = """      <!-- CALCULATOR SUITE TAB SWITCHER -->
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-borderSlate dark:border-darkBorder pb-4">
        <div class="flex flex-wrap items-center gap-1.5 p-1 rounded-xl bg-slate-100 dark:bg-darkCard border border-borderSlate dark:border-darkBorder font-mono text-xs">
          <button id="tabCorporateSizerBtn" class="calc-tab-btn px-3 py-1.5 rounded-lg bg-teal-600 text-white font-semibold shadow-sm transition-all cursor-pointer flex items-center gap-2">
            <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
            </svg>
            <span>Corporate Power Sizer (B2B &middot; DPPA)</span>
          </button>
          <button id="tabEvnEstimatorBtn" class="calc-tab-btn px-3 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-inkPrimary dark:hover:text-white transition-all cursor-pointer flex items-center gap-2">
            <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M13 10V3L4 14h7v7l9-11h-7z" />
            </svg>
            <span>EVN Tariff &amp; Consumption Estimator (English)</span>
          </button>
          <button id="tabGreenIndicatorBtn" class="calc-tab-btn px-3 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-inkPrimary dark:hover:text-white transition-all cursor-pointer flex items-center gap-2">
            <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
            </svg>
            <span>Green Indicators (EU CBAM &amp; Principles)</span>
          </button>
        </div>

        <div class="font-mono text-[11px] text-inkMuted dark:text-textDarkMuted flex items-center gap-2">
          <span class="inline-block w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
          <span>EU CBAM &amp; STATUTORY TARIFF 2026</span>
        </div>
      </div>"""

    tab_switcher_sidebar = """      <!-- SIDEBAR TOOLKIT HEADER -->
      <div class="flex items-center justify-between border-b border-borderSlate dark:border-darkBorder pb-3">
        <div class="flex items-center gap-2.5">
          <div class="w-8 h-8 rounded-lg bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20 flex items-center justify-center text-teal-600 dark:text-teal-400 shrink-0">
            <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
            </svg>
          </div>
          <div>
            <span class="font-mono text-[9px] uppercase tracking-wider text-teal-600 dark:text-teal-400 font-semibold block">Interactive Utility Suite</span>
            <h2 class="text-sm font-semibold text-inkPrimary dark:text-textDarkPrimary leading-tight">Energy Sizing &amp; Tariffs</h2>
          </div>
        </div>
        <span class="font-mono text-[10px] text-teal-600 dark:text-teal-400 px-2 py-0.5 rounded bg-teal-500/10 border border-teal-500/20 font-semibold shrink-0">B2B &middot; B2C</span>
      </div>

      <!-- COMPACT 3-TAB SELECTOR -->
      <div class="grid grid-cols-3 gap-1 p-1 rounded-xl bg-slate-100 dark:bg-darkCard border border-borderSlate dark:border-darkBorder font-mono text-[11px]">
        <button id="tabCorporateSizerBtn" class="calc-tab-btn py-1.5 px-1 rounded-lg bg-teal-600 text-white font-semibold shadow-sm transition-all cursor-pointer text-center truncate" title="Corporate Power Sizer (B2B &middot; DPPA)">
          Power Sizer
        </button>
        <button id="tabEvnEstimatorBtn" class="calc-tab-btn py-1.5 px-1 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-inkPrimary dark:hover:text-white transition-all cursor-pointer text-center truncate" title="EVN Tariff &amp; Consumption Estimator (English)">
          EVN Tariff
        </button>
        <button id="tabGreenIndicatorBtn" class="calc-tab-btn py-1.5 px-1 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-inkPrimary dark:hover:text-white transition-all cursor-pointer text-center truncate" title="Green Indicators (EU CBAM &amp; Principles)">
          Green CBAM
        </button>
      </div>"""

    calc_raw = calc_raw.replace(norm(tab_switcher_old), norm(tab_switcher_sidebar))

    # Wrap calculator inside <aside id="toolsSidebar">
    sidebar_block = f"""    <!-- ==================================================================== -->
    <!-- DEDICATED LEFT SIDEBAR: CALCULATION & SIZING TOOLKIT               -->
    <!-- ==================================================================== -->
    <aside id="toolsSidebar" class="w-full lg:w-[410px] xl:w-[430px] shrink-0 lg:sticky lg:top-6 self-start space-y-4">
{calc_raw}
    </aside>"""

    # Extract Right Workspace content (from <main> start to actual_calc_start)
    idx_main_open = content.find("<main")
    idx_main_open_end = content.find(">", idx_main_open) + 1
    right_raw = content[idx_main_open_end:actual_calc_start].strip()

    # Construct new 2-column main body
    new_main_content = f"""
    <div class="flex flex-col lg:flex-row gap-8 items-start">

{sidebar_block}

      <!-- ==================================================================== -->
      <!-- RIGHT PRIMARY WORKSPACE: MARKET INTELLIGENCE & SITES DIRECTORY       -->
      <!-- ==================================================================== -->
      <div class="flex-1 min-w-0 space-y-8 sm:space-y-10">
{right_raw}
      </div>

    </div>
  """

    # Replace <main class="...">...</main>
    # Change main class to max-w-7xl
    content_before_main = content[:idx_main_open]
    content_after_main = content[idx_main_close:]

    new_content = (
        content_before_main +
        '<main class="relative z-10 flex-1 w-full max-w-7xl mx-auto py-6 sm:py-8">' +
        norm(new_main_content) +
        content_after_main
    )

    # 3. Update JavaScript tab button styling in activateTab()
    js_tab_btn_old = 'btn.className = "calc-tab-btn px-3 py-1.5 rounded-lg bg-teal-600 text-white font-semibold shadow-sm transition-all cursor-pointer flex items-center gap-2";'
    js_tab_btn_new = 'btn.className = "calc-tab-btn py-1.5 px-1 rounded-lg bg-teal-600 text-white font-semibold shadow-sm transition-all cursor-pointer text-center truncate";'

    js_tab_inactive_old = 'btn.className = "calc-tab-btn px-3 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-inkPrimary dark:hover:text-white transition-all cursor-pointer flex items-center gap-2";'
    js_tab_inactive_new = 'btn.className = "calc-tab-btn py-1.5 px-1 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-inkPrimary dark:hover:text-white transition-all cursor-pointer text-center truncate";'

    new_content = new_content.replace(js_tab_btn_old, js_tab_btn_new)
    new_content = new_content.replace(js_tab_inactive_old, js_tab_inactive_new)

    with open(filepath, "w", encoding="utf-8", newline="") as f:
        f.write(new_content)

    print(f"[SUCCESS] Refactored {os.path.basename(filepath)} with Left Sidebar Workspace!")
    return True

if __name__ == "__main__":
    for p in TARGET_FILES:
        print(f"\nProcessing {p}...")
        refactor_file(p)
