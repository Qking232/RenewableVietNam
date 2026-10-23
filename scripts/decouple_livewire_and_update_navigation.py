#!/usr/bin/env python3
"""
decouple_livewire_and_update_navigation.py
=========================================
1. Decouples #marketWire section and news JS controllers from index.html and green/index.html.
2. Standardizes desktop and mobile header navigation across all portal pages:
   - Industrial Hubs (/)
   - PDP8 Energy (/projectenergy/)
   - EV Tech (/evcharging/) [Renamed from EV Stations]
   - Power Sizer & Tariffs (/calculator/)
   - Legal Framework (/hub/) [Renamed from The Library]
   - Live Wire (/livewire/) [New dedicated route]
3. Recompiles hub/index.html from _src/hub_source_v0.63.html.
4. Updates sitemap.xml with /livewire/.
5. Mirrors all modified files to Qking232.github.io for 100% cryptographic parity.
"""

import os
import re
import shutil
import subprocess

REPO_PRIMARY = r"G:\My Drive\7. AI\Gemini\RenewableVietNam"
REPO_SECONDARY = r"G:\My Drive\7. AI\Gemini\Qking232.github.io"

def update_index_html():
    path = os.path.join(REPO_PRIMARY, "index.html")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update right header Live Wire link
    content = content.replace('href="#marketWire"', 'href="/livewire/"')

    # 2. Desktop Navigation in index.html
    old_desktop_nav = """          <!-- Quick Inter-Domain Jump Navigation (Desktop) -->
          <nav class="hidden md:flex items-center gap-1 font-mono text-[11px] tracking-wider text-inkMuted dark:text-textDarkMuted">
            <a href="/" class="px-2.5 py-1 rounded-md text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20">Industrial Hubs</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/projectenergy/" class="px-2.5 py-1 rounded-md hover:text-emerald-600 dark:hover:text-emerald-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">PDP8 Energy</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/evcharging/" class="px-2.5 py-1 rounded-md hover:text-amber-600 dark:hover:text-amber-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">EV Stations</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/calculator/" class="px-2.5 py-1 rounded-md hover:text-teal-600 dark:hover:text-teal-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Power Sizer &amp; Tariffs</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/hub/" class="px-2.5 py-1 rounded-md hover:text-sky-600 dark:hover:text-sky-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">The Library</a>
          </nav>"""

    new_desktop_nav = """          <!-- Quick Inter-Domain Jump Navigation (Desktop) -->
          <nav class="hidden md:flex items-center gap-1 font-mono text-[11px] tracking-wider text-inkMuted dark:text-textDarkMuted">
            <a href="/" class="px-2.5 py-1 rounded-md text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20">Industrial Hubs</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/projectenergy/" class="px-2.5 py-1 rounded-md hover:text-emerald-600 dark:hover:text-emerald-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">PDP8 Energy</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/evcharging/" class="px-2.5 py-1 rounded-md hover:text-amber-600 dark:hover:text-amber-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">EV Tech</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/calculator/" class="px-2.5 py-1 rounded-md hover:text-teal-600 dark:hover:text-teal-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Power Sizer &amp; Tariffs</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/hub/" class="px-2.5 py-1 rounded-md hover:text-sky-600 dark:hover:text-sky-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Legal Framework</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/livewire/" class="px-2.5 py-1 rounded-md hover:text-teal-600 dark:hover:text-teal-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Live Wire</a>
          </nav>"""

    if old_desktop_nav in content:
        content = content.replace(old_desktop_nav, new_desktop_nav)
        print("[index.html] Desktop nav updated.")
    else:
        print("[index.html] WARNING: Old desktop nav not matched!")

    # 3. Mobile Navigation in index.html
    old_mobile_nav = """      <!-- Mobile Touch Navigation Carousel (Visible ONLY on mobile < 768px) -->
      <nav class="flex md:hidden items-center gap-1.5 overflow-x-auto no-scrollbar pt-1.5 pb-0.5 font-mono text-[11px] tracking-wider whitespace-nowrap w-full -mx-3 px-3 sm:mx-0 sm:px-0">
        <a href="/" class="px-2.5 py-1.5 rounded-lg text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20 shrink-0">Industrial Hubs</a>
        <a href="/projectenergy/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-emerald-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">PDP8 Energy</a>
        <a href="/evcharging/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-amber-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">EV Stations</a>
        <a href="/calculator/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-teal-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">Power Sizer</a>
        <a href="/hub/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-sky-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">The Library</a>
      </nav>"""

    new_mobile_nav = """      <!-- Mobile Touch Navigation Carousel (Visible ONLY on mobile < 768px) -->
      <nav class="flex md:hidden items-center gap-1.5 overflow-x-auto no-scrollbar pt-1.5 pb-0.5 font-mono text-[11px] tracking-wider whitespace-nowrap w-full -mx-3 px-3 sm:mx-0 sm:px-0">
        <a href="/" class="px-2.5 py-1.5 rounded-lg text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20 shrink-0">Industrial Hubs</a>
        <a href="/projectenergy/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-emerald-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">PDP8 Energy</a>
        <a href="/evcharging/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-amber-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">EV Tech</a>
        <a href="/calculator/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-teal-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">Power Sizer</a>
        <a href="/hub/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-sky-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">Legal Framework</a>
        <a href="/livewire/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-teal-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">Live Wire</a>
      </nav>"""

    if old_mobile_nav in content:
        content = content.replace(old_mobile_nav, new_mobile_nav)
        print("[index.html] Mobile nav updated.")
    else:
        print("[index.html] WARNING: Old mobile nav not matched!")

    # 4. Remove section id="marketWire"
    market_sec_regex = r'<!-- ==================================================================== -->\s*<!-- REAL-TIME INDUSTRY MARKET INTELLIGENCE WIRE \(RSS & APIS\)           -->\s*<!-- ==================================================================== -->\s*<section id="marketWire".*?</section>\s*(?=<!-- HERO & MACRO TELEMETRY HEADER -->)'
    content, count = re.subn(market_sec_regex, '', content, flags=re.DOTALL)
    print(f"[index.html] Purged marketWire section: {count} matches removed.")

    # 5. Update footer
    old_footer = """    <div class="flex items-center gap-3">
      <a href="/projectenergy/" class="hover:text-inkPrimary dark:hover:text-white transition-colors">Energy Map</a>
      <span>&middot;</span>
      <a href="/evcharging/" class="hover:text-inkPrimary dark:hover:text-white transition-colors">EV Stations</a>
      <span>&middot;</span>
      <a href="/hub/" class="hover:text-inkPrimary dark:hover:text-white transition-colors">The Library</a>
      <span>&middot;</span>
      <a href="mailto:info@renewablevietnam.com" class="hover:text-inkPrimary dark:hover:text-white transition-colors">info@renewablevietnam.com</a>
    </div>"""

    new_footer = """    <div class="flex flex-wrap items-center gap-x-3 gap-y-1">
      <a href="/projectenergy/" class="hover:text-inkPrimary dark:hover:text-white transition-colors">PDP8 Energy</a>
      <span>&middot;</span>
      <a href="/evcharging/" class="hover:text-inkPrimary dark:hover:text-white transition-colors">EV Tech</a>
      <span>&middot;</span>
      <a href="/calculator/" class="hover:text-inkPrimary dark:hover:text-white transition-colors">Power Sizer &amp; Tariffs</a>
      <span>&middot;</span>
      <a href="/hub/" class="hover:text-inkPrimary dark:hover:text-white transition-colors">Legal Framework</a>
      <span>&middot;</span>
      <a href="/livewire/" class="hover:text-inkPrimary dark:hover:text-white transition-colors">Live Wire</a>
      <span>&middot;</span>
      <a href="mailto:info@renewablevietnam.com" class="hover:text-inkPrimary dark:hover:text-white transition-colors">info@renewablevietnam.com</a>
    </div>"""

    if old_footer in content:
        content = content.replace(old_footer, new_footer)
        print("[index.html] Footer updated.")
    else:
        print("[index.html] WARNING: Old footer not matched!")

    # 6. Remove news controller javascript
    news_js_regex = r'// ====================================================================\s*// REAL-TIME INDUSTRY NEWS WIRE CONTROLLER\s*// ====================================================================.*?(?=fetchNewsData\(\);\s*\}\);)'
    content, count_js = re.subn(news_js_regex, '', content, flags=re.DOTALL)
    print(f"[index.html] Purged news JS controller: {count_js} matches removed.")

    content = content.replace('fetchNewsData();\n    });', '});')
    content = content.replace('fetchNewsData();\r\n    });', '});')

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("[index.html] Successfully saved clean version.")

def update_green_html():
    path = os.path.join(REPO_PRIMARY, "green", "index.html")
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Right live wire link
    content = content.replace('href="#marketWire"', 'href="/livewire/"')

    # Desktop nav
    old_desktop_nav = """          <!-- Quick Inter-Domain Jump Navigation (Desktop) -->
          <nav class="hidden md:flex items-center gap-1 font-mono text-[11px] tracking-wider text-inkMuted dark:text-textDarkMuted">
            <a href="/" class="px-2.5 py-1 rounded-md text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20">Industrial Hubs</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/projectenergy/" class="px-2.5 py-1 rounded-md hover:text-emerald-600 dark:hover:text-emerald-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">PDP8 Energy</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/evcharging/" class="px-2.5 py-1 rounded-md hover:text-amber-600 dark:hover:text-amber-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">EV Stations</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/calculator/" class="px-2.5 py-1 rounded-md hover:text-teal-600 dark:hover:text-teal-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Power Sizer &amp; Tariffs</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/hub/" class="px-2.5 py-1 rounded-md hover:text-sky-600 dark:hover:text-sky-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">The Library</a>
          </nav>"""

    new_desktop_nav = """          <!-- Quick Inter-Domain Jump Navigation (Desktop) -->
          <nav class="hidden md:flex items-center gap-1 font-mono text-[11px] tracking-wider text-inkMuted dark:text-textDarkMuted">
            <a href="/" class="px-2.5 py-1 rounded-md hover:text-teal-600 dark:hover:text-teal-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Industrial Hubs</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/projectenergy/" class="px-2.5 py-1 rounded-md hover:text-emerald-600 dark:hover:text-emerald-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">PDP8 Energy</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/evcharging/" class="px-2.5 py-1 rounded-md hover:text-amber-600 dark:hover:text-amber-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">EV Tech</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/calculator/" class="px-2.5 py-1 rounded-md hover:text-teal-600 dark:hover:text-teal-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Power Sizer &amp; Tariffs</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/hub/" class="px-2.5 py-1 rounded-md hover:text-sky-600 dark:hover:text-sky-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Legal Framework</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/livewire/" class="px-2.5 py-1 rounded-md hover:text-teal-600 dark:hover:text-teal-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Live Wire</a>
          </nav>"""

    if old_desktop_nav in content:
        content = content.replace(old_desktop_nav, new_desktop_nav)

    # Mobile nav
    old_mobile_nav = """      <!-- Mobile Touch Navigation Carousel (Visible ONLY on mobile < 768px) -->
      <nav class="flex md:hidden items-center gap-1.5 overflow-x-auto no-scrollbar pt-1.5 pb-0.5 font-mono text-[11px] tracking-wider whitespace-nowrap w-full -mx-3 px-3 sm:mx-0 sm:px-0">
        <a href="/" class="px-2.5 py-1.5 rounded-lg text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20 shrink-0">Industrial Hubs</a>
        <a href="/projectenergy/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-emerald-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">PDP8 Energy</a>
        <a href="/evcharging/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-amber-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">EV Stations</a>
        <a href="/calculator/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-teal-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">Power Sizer</a>
        <a href="/hub/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-sky-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">The Library</a>
      </nav>"""

    new_mobile_nav = """      <!-- Mobile Touch Navigation Carousel (Visible ONLY on mobile < 768px) -->
      <nav class="flex md:hidden items-center gap-1.5 overflow-x-auto no-scrollbar pt-1.5 pb-0.5 font-mono text-[11px] tracking-wider whitespace-nowrap w-full -mx-3 px-3 sm:mx-0 sm:px-0">
        <a href="/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-teal-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">Industrial Hubs</a>
        <a href="/projectenergy/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-emerald-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">PDP8 Energy</a>
        <a href="/evcharging/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-amber-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">EV Tech</a>
        <a href="/calculator/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-teal-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">Power Sizer</a>
        <a href="/hub/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-sky-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">Legal Framework</a>
        <a href="/livewire/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-teal-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">Live Wire</a>
      </nav>"""

    if old_mobile_nav in content:
        content = content.replace(old_mobile_nav, new_mobile_nav)

    # Purge marketWire section from green/index.html
    market_sec_regex = r'<!-- ==================================================================== -->\s*<!-- REAL-TIME INDUSTRY MARKET INTELLIGENCE WIRE \(RSS & APIS\)           -->\s*<!-- ==================================================================== -->\s*<section id="marketWire".*?</section>\s*(?=<!-- HERO & MACRO TELEMETRY HEADER -->)'
    content, count = re.subn(market_sec_regex, '', content, flags=re.DOTALL)

    # Purge news JS controller from green/index.html
    news_js_regex = r'// ====================================================================\s*// REAL-TIME INDUSTRY NEWS WIRE CONTROLLER\s*// ====================================================================.*?(?=fetchNewsData\(\);\s*\}\);)'
    content, count_js = re.subn(news_js_regex, '', content, flags=re.DOTALL)
    content = content.replace('fetchNewsData();\n    });', '});')
    content = content.replace('fetchNewsData();\r\n    });', '});')

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("[green/index.html] Successfully updated and cleaned.")

def update_projectenergy_html():
    path = os.path.join(REPO_PRIMARY, "projectenergy", "index.html")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Desktop nav
    old_desktop_nav = """<nav class="hidden md:flex items-center gap-1 font-mono text-[11px] tracking-wider text-inkMuted dark:text-textDarkMuted">
            <a href="/" class="px-2.5 py-1 rounded-md hover:text-teal-600 dark:hover:text-teal-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Industrial Hubs</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/projectenergy/" class="px-2.5 py-1 rounded-md text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20">PDP8 Energy</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/evcharging/" class="px-2.5 py-1 rounded-md hover:text-amber-600 dark:hover:text-amber-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">EV Stations</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/calculator/" class="px-2.5 py-1 rounded-md hover:text-teal-600 dark:hover:text-teal-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Power Sizer &amp; Tariffs</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/hub/" class="px-2.5 py-1 rounded-md hover:text-sky-600 dark:hover:text-sky-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">The Library</a>
          </nav>"""

    new_desktop_nav = """<nav class="hidden md:flex items-center gap-1 font-mono text-[11px] tracking-wider text-inkMuted dark:text-textDarkMuted">
            <a href="/" class="px-2.5 py-1 rounded-md hover:text-teal-600 dark:hover:text-teal-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Industrial Hubs</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/projectenergy/" class="px-2.5 py-1 rounded-md text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20">PDP8 Energy</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/evcharging/" class="px-2.5 py-1 rounded-md hover:text-amber-600 dark:hover:text-amber-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">EV Tech</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/calculator/" class="px-2.5 py-1 rounded-md hover:text-teal-600 dark:hover:text-teal-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Power Sizer &amp; Tariffs</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/hub/" class="px-2.5 py-1 rounded-md hover:text-sky-600 dark:hover:text-sky-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Legal Framework</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/livewire/" class="px-2.5 py-1 rounded-md hover:text-teal-600 dark:hover:text-teal-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Live Wire</a>
          </nav>"""

    if old_desktop_nav in content:
        content = content.replace(old_desktop_nav, new_desktop_nav)
        print("[projectenergy/index.html] Desktop nav updated.")

    # Mobile nav
    old_mobile_nav = """<nav class="flex md:hidden items-center gap-1.5 overflow-x-auto no-scrollbar pt-1.5 pb-0.5 font-mono text-[11px] tracking-wider whitespace-nowrap w-full -mx-3 px-3 sm:mx-0 sm:px-0">
        <a href="/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-teal-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">Industrial Hubs</a>
        <a href="/projectenergy/" class="px-2.5 py-1.5 rounded-lg text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20 shrink-0">PDP8 Energy</a>
        <a href="/evcharging/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-amber-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">EV Stations</a>
        <a href="/calculator/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-teal-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">Power Sizer</a>
        <a href="/hub/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-sky-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">The Library</a>
      </nav>"""

    new_mobile_nav = """<nav class="flex md:hidden items-center gap-1.5 overflow-x-auto no-scrollbar pt-1.5 pb-0.5 font-mono text-[11px] tracking-wider whitespace-nowrap w-full -mx-3 px-3 sm:mx-0 sm:px-0">
        <a href="/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-teal-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">Industrial Hubs</a>
        <a href="/projectenergy/" class="px-2.5 py-1.5 rounded-lg text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20 shrink-0">PDP8 Energy</a>
        <a href="/evcharging/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-amber-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">EV Tech</a>
        <a href="/calculator/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-teal-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">Power Sizer</a>
        <a href="/hub/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-sky-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">Legal Framework</a>
        <a href="/livewire/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-teal-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">Live Wire</a>
      </nav>"""

    if old_mobile_nav in content:
        content = content.replace(old_mobile_nav, new_mobile_nav)
        print("[projectenergy/index.html] Mobile nav updated.")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("[projectenergy/index.html] Successfully saved.")

def update_evcharging_html():
    path = os.path.join(REPO_PRIMARY, "evcharging", "index.html")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Desktop nav
    old_desktop_nav = """<nav class="hidden md:flex items-center gap-1 font-mono text-[11px] tracking-wider text-inkMuted dark:text-textDarkMuted">
            <a href="/" class="px-2.5 py-1 rounded-md hover:text-teal-600 dark:hover:text-teal-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Industrial Hubs</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/projectenergy/" class="px-2.5 py-1 rounded-md hover:text-emerald-600 dark:hover:text-emerald-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">PDP8 Energy</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/evcharging/" class="px-2.5 py-1 rounded-md text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20">EV Stations</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/calculator/" class="px-2.5 py-1 rounded-md hover:text-teal-600 dark:hover:text-teal-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Power Sizer &amp; Tariffs</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/hub/" class="px-2.5 py-1 rounded-md hover:text-sky-600 dark:hover:text-sky-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">The Library</a>
          </nav>"""

    new_desktop_nav = """<nav class="hidden md:flex items-center gap-1 font-mono text-[11px] tracking-wider text-inkMuted dark:text-textDarkMuted">
            <a href="/" class="px-2.5 py-1 rounded-md hover:text-teal-600 dark:hover:text-teal-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Industrial Hubs</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/projectenergy/" class="px-2.5 py-1 rounded-md hover:text-emerald-600 dark:hover:text-emerald-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">PDP8 Energy</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/evcharging/" class="px-2.5 py-1 rounded-md text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20">EV Tech</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/calculator/" class="px-2.5 py-1 rounded-md hover:text-teal-600 dark:hover:text-teal-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Power Sizer &amp; Tariffs</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/hub/" class="px-2.5 py-1 rounded-md hover:text-sky-600 dark:hover:text-sky-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Legal Framework</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/livewire/" class="px-2.5 py-1 rounded-md hover:text-teal-600 dark:hover:text-teal-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Live Wire</a>
          </nav>"""

    if old_desktop_nav in content:
        content = content.replace(old_desktop_nav, new_desktop_nav)
        print("[evcharging/index.html] Desktop nav updated.")

    # Mobile nav
    old_mobile_nav = """<nav class="flex md:hidden items-center gap-1.5 overflow-x-auto no-scrollbar pt-1.5 pb-0.5 font-mono text-[11px] tracking-wider whitespace-nowrap w-full -mx-3 px-3 sm:mx-0 sm:px-0">
        <a href="/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-teal-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">Industrial Hubs</a>
        <a href="/projectenergy/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-emerald-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">PDP8 Energy</a>
        <a href="/evcharging/" class="px-2.5 py-1.5 rounded-lg text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20 shrink-0">EV Stations</a>
        <a href="/calculator/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-teal-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">Power Sizer</a>
        <a href="/hub/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-sky-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">The Library</a>
      </nav>"""

    new_mobile_nav = """<nav class="flex md:hidden items-center gap-1.5 overflow-x-auto no-scrollbar pt-1.5 pb-0.5 font-mono text-[11px] tracking-wider whitespace-nowrap w-full -mx-3 px-3 sm:mx-0 sm:px-0">
        <a href="/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-teal-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">Industrial Hubs</a>
        <a href="/projectenergy/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-emerald-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">PDP8 Energy</a>
        <a href="/evcharging/" class="px-2.5 py-1.5 rounded-lg text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20 shrink-0">EV Tech</a>
        <a href="/calculator/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-teal-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">Power Sizer</a>
        <a href="/hub/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-sky-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">Legal Framework</a>
        <a href="/livewire/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-teal-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">Live Wire</a>
      </nav>"""

    if old_mobile_nav in content:
        content = content.replace(old_mobile_nav, new_mobile_nav)
        print("[evcharging/index.html] Mobile nav updated.")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("[evcharging/index.html] Successfully saved.")

def update_calculator_html():
    path = os.path.join(REPO_PRIMARY, "calculator", "index.html")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Desktop nav
    old_desktop_nav = """<nav class="hidden md:flex items-center gap-1 font-mono text-[11px] tracking-wider text-inkMuted dark:text-textDarkMuted">
            <a href="/" class="px-2.5 py-1 rounded-md hover:text-teal-600 dark:hover:text-teal-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Industrial Hubs</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/projectenergy/" class="px-2.5 py-1 rounded-md hover:text-emerald-600 dark:hover:text-emerald-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">PDP8 Energy</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/evcharging/" class="px-2.5 py-1 rounded-md hover:text-amber-600 dark:hover:text-amber-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">EV Stations</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/calculator/" class="px-2.5 py-1 rounded-md text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20">Power Sizer &amp; Tariffs</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/hub/" class="px-2.5 py-1 rounded-md hover:text-sky-600 dark:hover:text-sky-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">The Library</a>
          </nav>"""

    new_desktop_nav = """<nav class="hidden md:flex items-center gap-1 font-mono text-[11px] tracking-wider text-inkMuted dark:text-textDarkMuted">
            <a href="/" class="px-2.5 py-1 rounded-md hover:text-teal-600 dark:hover:text-teal-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Industrial Hubs</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/projectenergy/" class="px-2.5 py-1 rounded-md hover:text-emerald-600 dark:hover:text-emerald-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">PDP8 Energy</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/evcharging/" class="px-2.5 py-1 rounded-md hover:text-amber-600 dark:hover:text-amber-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">EV Tech</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/calculator/" class="px-2.5 py-1 rounded-md text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20">Power Sizer &amp; Tariffs</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/hub/" class="px-2.5 py-1 rounded-md hover:text-sky-600 dark:hover:text-sky-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Legal Framework</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/livewire/" class="px-2.5 py-1 rounded-md hover:text-teal-600 dark:hover:text-teal-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Live Wire</a>
          </nav>"""

    if old_desktop_nav in content:
        content = content.replace(old_desktop_nav, new_desktop_nav)
        print("[calculator/index.html] Desktop nav updated.")

    # Mobile nav
    old_mobile_nav = """<nav class="flex md:hidden items-center gap-1.5 overflow-x-auto no-scrollbar pt-1.5 pb-0.5 font-mono text-[11px] tracking-wider whitespace-nowrap w-full -mx-3 px-3 sm:mx-0 sm:px-0">
        <a href="/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-teal-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">Industrial Hubs</a>
        <a href="/projectenergy/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-emerald-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">PDP8 Energy</a>
        <a href="/evcharging/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-amber-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">EV Stations</a>
        <a href="/calculator/" class="px-2.5 py-1.5 rounded-lg text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20 shrink-0">Power Sizer</a>
        <a href="/hub/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-sky-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">The Library</a>
      </nav>"""

    new_mobile_nav = """<nav class="flex md:hidden items-center gap-1.5 overflow-x-auto no-scrollbar pt-1.5 pb-0.5 font-mono text-[11px] tracking-wider whitespace-nowrap w-full -mx-3 px-3 sm:mx-0 sm:px-0">
        <a href="/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-teal-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">Industrial Hubs</a>
        <a href="/projectenergy/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-emerald-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">PDP8 Energy</a>
        <a href="/evcharging/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-amber-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">EV Tech</a>
        <a href="/calculator/" class="px-2.5 py-1.5 rounded-lg text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20 shrink-0">Power Sizer</a>
        <a href="/hub/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-sky-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">Legal Framework</a>
        <a href="/livewire/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-teal-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">Live Wire</a>
      </nav>"""

    if old_mobile_nav in content:
        content = content.replace(old_mobile_nav, new_mobile_nav)
        print("[calculator/index.html] Mobile nav updated.")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("[calculator/index.html] Successfully saved.")

def update_hub_source():
    path = os.path.join(REPO_PRIMARY, "_src", "hub_source_v0.63.html")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Desktop nav
    old_desktop_nav = """<nav class="hidden md:flex items-center gap-1 font-mono text-[11px] tracking-wider text-slate-400">
            <a href="/" class="px-2.5 py-1 rounded-md text-slate-400 hover:text-teal-400 hover:bg-slate-800/40 transition-colors">Industrial Hubs</a> <span class="text-slate-600">&middot;</span> <a href="/projectenergy/" class="px-2.5 py-1 rounded-md text-slate-400 hover:text-emerald-400 hover:bg-slate-800/40 transition-colors">Energy Map</a> <span class="text-slate-600">&middot;</span> <a href="/evcharging/" class="px-2.5 py-1 rounded-md text-slate-400 hover:text-amber-400 hover:bg-slate-800/40 transition-colors">EV Stations</a> <span class="text-slate-600">&middot;</span> <a href="/calculator/" class="px-2.5 py-1 rounded-md text-slate-400 hover:text-teal-400 hover:bg-slate-800/40 transition-colors">Power Sizer &amp; Tariffs</a> <span class="text-slate-600">&middot;</span> <a href="/hub/" class="px-2.5 py-1 rounded-md text-white font-semibold bg-white/10 border border-white/40 shadow-sm transition-all">The Library</a>
          </nav>"""

    new_desktop_nav = """<nav class="hidden md:flex items-center gap-1 font-mono text-[11px] tracking-wider text-slate-400">
            <a href="/" class="px-2.5 py-1 rounded-md text-slate-400 hover:text-teal-400 hover:bg-slate-800/40 transition-colors">Industrial Hubs</a> <span class="text-slate-600">&middot;</span> <a href="/projectenergy/" class="px-2.5 py-1 rounded-md text-slate-400 hover:text-emerald-400 hover:bg-slate-800/40 transition-colors">PDP8 Energy</a> <span class="text-slate-600">&middot;</span> <a href="/evcharging/" class="px-2.5 py-1 rounded-md text-slate-400 hover:text-amber-400 hover:bg-slate-800/40 transition-colors">EV Tech</a> <span class="text-slate-600">&middot;</span> <a href="/calculator/" class="px-2.5 py-1 rounded-md text-slate-400 hover:text-teal-400 hover:bg-slate-800/40 transition-colors">Power Sizer &amp; Tariffs</a> <span class="text-slate-600">&middot;</span> <a href="/hub/" class="px-2.5 py-1 rounded-md text-white font-semibold bg-white/10 border border-white/40 shadow-sm transition-all">Legal Framework</a> <span class="text-slate-600">&middot;</span> <a href="/livewire/" class="px-2.5 py-1 rounded-md text-slate-400 hover:text-teal-400 hover:bg-slate-800/40 transition-colors">Live Wire</a>
          </nav>"""

    if old_desktop_nav in content:
        content = content.replace(old_desktop_nav, new_desktop_nav)
        print("[_src/hub_source_v0.63.html] Desktop nav updated.")

    # Mobile nav
    old_mobile_nav = """<nav class="flex md:hidden items-center gap-1.5 overflow-x-auto no-scrollbar pt-1.5 pb-0.5 font-mono text-[11px] tracking-wider whitespace-nowrap">
        <a href="/" class="px-2.5 py-1.5 rounded-lg text-slate-400 hover:text-white bg-white/5 border border-white/10 shrink-0">Industrial Hubs</a>
        <a href="/projectenergy/" class="px-2.5 py-1.5 rounded-lg text-slate-400 hover:text-white bg-white/5 border border-white/10 shrink-0">Energy Map</a>
        <a href="/evcharging/" class="px-2.5 py-1.5 rounded-lg text-slate-400 hover:text-white bg-white/5 border border-white/10 shrink-0">EV Stations</a>
        <a href="/calculator/" class="px-2.5 py-1.5 rounded-lg text-slate-400 hover:text-white bg-white/5 border border-white/10 shrink-0">Power Sizer</a>
        <a href="/hub/" class="px-2.5 py-1.5 rounded-lg text-white font-semibold bg-white/10 border border-white/40 shrink-0">The Library</a>
      </nav>"""

    new_mobile_nav = """<nav class="flex md:hidden items-center gap-1.5 overflow-x-auto no-scrollbar pt-1.5 pb-0.5 font-mono text-[11px] tracking-wider whitespace-nowrap">
        <a href="/" class="px-2.5 py-1.5 rounded-lg text-slate-400 hover:text-white bg-white/5 border border-white/10 shrink-0">Industrial Hubs</a>
        <a href="/projectenergy/" class="px-2.5 py-1.5 rounded-lg text-slate-400 hover:text-white bg-white/5 border border-white/10 shrink-0">PDP8 Energy</a>
        <a href="/evcharging/" class="px-2.5 py-1.5 rounded-lg text-slate-400 hover:text-white bg-white/5 border border-white/10 shrink-0">EV Tech</a>
        <a href="/calculator/" class="px-2.5 py-1.5 rounded-lg text-slate-400 hover:text-white bg-white/5 border border-white/10 shrink-0">Power Sizer</a>
        <a href="/hub/" class="px-2.5 py-1.5 rounded-lg text-white font-semibold bg-white/10 border border-white/40 shrink-0">Legal Framework</a>
        <a href="/livewire/" class="px-2.5 py-1.5 rounded-lg text-slate-400 hover:text-white bg-white/5 border border-white/10 shrink-0">Live Wire</a>
      </nav>"""

    if old_mobile_nav in content:
        content = content.replace(old_mobile_nav, new_mobile_nav)
        print("[_src/hub_source_v0.63.html] Mobile nav updated.")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    # Recompile hub/index.html using Node.js script
    print("Recompiling hub/index.html...")
    build_script = os.path.join(REPO_PRIMARY, "scripts", "build-protected-hub.js")
    res = subprocess.run(["node", build_script], capture_output=True, text=True, cwd=REPO_PRIMARY)
    print("Build output:", res.stdout, res.stderr)

def update_sitemap():
    path = os.path.join(REPO_PRIMARY, "sitemap.xml")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if "https://renewablevietnam.com/livewire/" not in content:
        target = """  <url>
    <loc>https://renewablevietnam.com/green/</loc>"""
        livewire_entry = """  <url>
    <loc>https://renewablevietnam.com/livewire/</loc>
    <lastmod>2026-10-23</lastmod>
    <changefreq>hourly</changefreq>
    <priority>0.9</priority>
  </url>
"""
        content = content.replace(target, livewire_entry + target)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("[sitemap.xml] Inserted /livewire/ entry.")

def mirror_to_secondary():
    files_to_mirror = [
        "index.html",
        os.path.join("green", "index.html"),
        os.path.join("projectenergy", "index.html"),
        os.path.join("evcharging", "index.html"),
        os.path.join("calculator", "index.html"),
        os.path.join("hub", "index.html"),
        os.path.join("livewire", "index.html"),
        os.path.join("_src", "hub_source_v0.63.html"),
        "sitemap.xml"
    ]

    for rel in files_to_mirror:
        src = os.path.join(REPO_PRIMARY, rel)
        dst = os.path.join(REPO_SECONDARY, rel)
        if os.path.exists(src):
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
            print(f"[MIRROR] Copied {rel} -> Qking232.github.io")

if __name__ == "__main__":
    print("=== DECOUPLING LIVE WIRE & HARMONIZING NAVIGATION ===")
    update_index_html()
    update_green_html()
    update_projectenergy_html()
    update_evcharging_html()
    update_calculator_html()
    update_hub_source()
    update_sitemap()
    mirror_to_secondary()
    print("=== ALL TRANSFORMS COMPLETED SUCCESSFULLY ===")
