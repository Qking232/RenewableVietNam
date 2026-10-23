#!/usr/bin/env python3
"""
apply_clean_livewire_styling.py
===============================
Standardizes 'Live Wire' navigation tab styling to match 'Industrial Hubs'
clean text styling with a dual-ring pulsing green indicator dot across all portal headers.
Removes legacy button pill from right controls.
"""

import os
import re
import shutil
import subprocess

REPO_PRIMARY = r"G:\My Drive\7. AI\Gemini\RenewableVietNam"
REPO_SECONDARY = r"G:\My Drive\7. AI\Gemini\Qking232.github.io"

# Target Snippets
CLEAN_LIVEWIRE_INACTIVE_DESKTOP = """<a href="/livewire/" class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md hover:text-teal-600 dark:hover:text-teal-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors group">
              <span class="relative flex h-2 w-2 shrink-0">
                <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                <span class="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
              </span>
              <span>Live Wire</span>
            </a>"""

CLEAN_LIVEWIRE_ACTIVE_DESKTOP = """<a href="/livewire/" class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20 shadow-sm transition-colors">
              <span class="relative flex h-2 w-2 shrink-0">
                <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                <span class="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
              </span>
              <span>Live Wire</span>
            </a>"""

CLEAN_LIVEWIRE_INACTIVE_MOBILE = """<a href="/livewire/" class="inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-teal-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">
          <span class="relative flex h-2 w-2 shrink-0">
            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
            <span class="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
          </span>
          <span>Live Wire</span>
        </a>"""

CLEAN_LIVEWIRE_ACTIVE_MOBILE = """<a href="/livewire/" class="inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20 shrink-0">
          <span class="relative flex h-2 w-2 shrink-0">
            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
            <span class="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
          </span>
          <span>Live Wire</span>
        </a>"""

def update_file(rel_path, is_livewire_page=False):
    path = os.path.join(REPO_PRIMARY, rel_path)
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update Desktop Navigation
    desktop_target = CLEAN_LIVEWIRE_ACTIVE_DESKTOP if is_livewire_page else CLEAN_LIVEWIRE_INACTIVE_DESKTOP
    
    # Replace any plain <a href="/livewire/" ...>Live Wire</a> in desktop nav
    content = re.sub(
        r'<a href="/livewire/" class="[^"]*">Live Wire</a>',
        desktop_target,
        content
    )

    # 2. Update Mobile Navigation
    mobile_target = CLEAN_LIVEWIRE_ACTIVE_MOBILE if is_livewire_page else CLEAN_LIVEWIRE_INACTIVE_MOBILE
    
    # Matches mobile link: <a href="/livewire/" class="[^"]*shrink-0">Live Wire</a>
    content = re.sub(
        r'<a href="/livewire/" class="[^"]*shrink-0">Live Wire</a>',
        mobile_target,
        content
    )

    # 3. Remove redundant right-control button pill
    pill_regex = r'<a href="/livewire/" class="inline-flex items-center gap-1\.5 px-2\.5 sm:px-3 py-1\.5 rounded-lg font-mono text-\[10px\] sm:text-\[11px\][^>]*>.*?<span>Live Wire</span>\s*</a>\s*'
    content = re.sub(pill_regex, '', content, flags=re.DOTALL)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[{rel_path}] Updated navigation and purged redundant pill.")

def update_hub_source():
    path = os.path.join(REPO_PRIMARY, "_src", "hub_source_v0.63.html")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Desktop nav link
    hub_desktop = """<a href="/livewire/" class="inline-flex items-center gap-1 px-2 py-0.5 rounded text-slate-400 hover:text-teal-400 hover:bg-slate-800/40 transition-colors">
              <span class="relative flex h-1.5 w-1.5 shrink-0">
                <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                <span class="relative inline-flex rounded-full h-1.5 w-1.5 bg-emerald-500"></span>
              </span>
              <span>Live Wire</span>
            </a>"""
    content = re.sub(r'<a href="/livewire/" class="[^"]*">Live Wire</a>', hub_desktop, content)

    # Mobile nav link
    hub_mobile = """<a href="/livewire/" class="inline-flex items-center gap-1 px-2.5 py-1.5 rounded-lg text-slate-400 hover:text-white bg-white/5 border border-white/10 shrink-0">
          <span class="relative flex h-1.5 w-1.5 shrink-0">
            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
            <span class="relative inline-flex rounded-full h-1.5 w-1.5 bg-emerald-500"></span>
          </span>
          <span>Live Wire</span>
        </a>"""
    content = re.sub(r'<a href="/livewire/" class="[^"]*shrink-0">Live Wire</a>', hub_mobile, content)

    # Purge legacy right button pill in hub source if present
    content = re.sub(r'<a href="/livewire/" class="inline-flex items-center gap-1\.5 px-2\.5 sm:px-3 py-1\.5 rounded-lg font-mono text-\[10px\] sm:text-\[11px\][^>]*>.*?<span>Live Wire</span>\s*</a>\s*', '', content, flags=re.DOTALL)
    content = re.sub(r'<a href="/livewire/" class="[^"]*live-wire-btn[^"]*">.*?</a>\s*', '', content, flags=re.DOTALL)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("[_src/hub_source_v0.63.html] Updated hub source.")

    # Recompile hub/index.html
    build_script = os.path.join(REPO_PRIMARY, "scripts", "build-protected-hub.js")
    res = subprocess.run(["node", build_script], capture_output=True, text=True, cwd=REPO_PRIMARY)
    print("Recompiled hub/index.html:", res.stdout.strip())

def mirror():
    files = [
        "index.html",
        os.path.join("green", "index.html"),
        os.path.join("projectenergy", "index.html"),
        os.path.join("evcharging", "index.html"),
        os.path.join("calculator", "index.html"),
        os.path.join("hub", "index.html"),
        os.path.join("livewire", "index.html"),
        os.path.join("_src", "hub_source_v0.63.html")
    ]
    for rel in files:
        src = os.path.join(REPO_PRIMARY, rel)
        dst = os.path.join(REPO_SECONDARY, rel)
        if os.path.exists(src):
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
            print(f"[MIRROR] {rel} -> Qking232.github.io")

if __name__ == "__main__":
    print("=== APPLYING CLEAN LIVE WIRE STYLING ===")
    update_file("index.html", is_livewire_page=False)
    update_file(os.path.join("green", "index.html"), is_livewire_page=False)
    update_file(os.path.join("projectenergy", "index.html"), is_livewire_page=False)
    update_file(os.path.join("evcharging", "index.html"), is_livewire_page=False)
    update_file(os.path.join("calculator", "index.html"), is_livewire_page=False)
    update_file(os.path.join("livewire", "index.html"), is_livewire_page=True)
    update_hub_source()
    mirror()
    print("=== COMPLETE ===")
