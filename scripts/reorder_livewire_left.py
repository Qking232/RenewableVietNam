#!/usr/bin/env python3
"""
reorder_livewire_left.py
========================
Moves 'Live Wire' to position #2 (immediately after 'Industrial Hubs')
across all desktop headers, mobile touch carousels, and footers.
Recompiles hub/index.html and mirrors to Qking232.github.io.
"""

import os
import re
import shutil
import subprocess

REPO_PRIMARY = r"G:\My Drive\7. AI\Gemini\RenewableVietNam"
REPO_SECONDARY = r"G:\My Drive\7. AI\Gemini\Qking232.github.io"

# Helper generator for Desktop Nav
def generate_desktop_nav(active_route):
    def link(href, label, color_hover="teal"):
        is_active = (href == active_route)
        if href == "/livewire/":
            if is_active:
                return """<a href="/livewire/" class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20 shadow-sm transition-colors">
              <span class="relative flex h-2 w-2 shrink-0">
                <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                <span class="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
              </span>
              <span>Live Wire</span>
            </a>"""
            else:
                return """<a href="/livewire/" class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md hover:text-teal-600 dark:hover:text-teal-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors group">
              <span class="relative flex h-2 w-2 shrink-0">
                <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                <span class="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
              </span>
              <span>Live Wire</span>
            </a>"""
        else:
            if is_active:
                return f"""<a href="{href}" class="px-2.5 py-1 rounded-md text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20">{label}</a>"""
            else:
                return f"""<a href="{href}" class="px-2.5 py-1 rounded-md hover:text-{color_hover}-600 dark:hover:text-{color_hover}-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">{label}</a>"""

    dot = """\n            <span class="text-slate-300 dark:text-slate-700">&middot;</span>\n            """
    items = [
        link("/", "Industrial Hubs", "teal"),
        link("/livewire/", "Live Wire", "teal"),
        link("/projectenergy/", "PDP8 Energy", "emerald"),
        link("/evcharging/", "EV Tech", "amber"),
        link("/calculator/", "Power Sizer &amp; Tariffs", "teal"),
        link("/hub/", "Legal Framework", "sky")
    ]

    return f"""<!-- Quick Inter-Domain Jump Navigation (Desktop) -->\n          <nav class="hidden md:flex items-center gap-1 font-mono text-[11px] tracking-wider text-inkMuted dark:text-textDarkMuted">\n            {dot.join(items)}\n          </nav>"""

# Helper generator for Mobile Nav
def generate_mobile_nav(active_route):
    def mlink(href, label, color_hover="teal"):
        is_active = (href == active_route)
        if href == "/livewire/":
            if is_active:
                return """<a href="/livewire/" class="inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20 shrink-0">
          <span class="relative flex h-2 w-2 shrink-0">
            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
            <span class="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
          </span>
          <span>Live Wire</span>
        </a>"""
            else:
                return """<a href="/livewire/" class="inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-teal-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">
          <span class="relative flex h-2 w-2 shrink-0">
            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
            <span class="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
          </span>
          <span>Live Wire</span>
        </a>"""
        else:
            if is_active:
                return f"""<a href="{href}" class="px-2.5 py-1.5 rounded-lg text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20 shrink-0">{label}</a>"""
            else:
                return f"""<a href="{href}" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-{color_hover}-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">{label}</a>"""

    items = [
        mlink("/", "Industrial Hubs", "teal"),
        mlink("/livewire/", "Live Wire", "teal"),
        mlink("/projectenergy/", "PDP8 Energy", "emerald"),
        mlink("/evcharging/", "EV Tech", "amber"),
        mlink("/calculator/", "Power Sizer", "teal"),
        mlink("/hub/", "Legal Framework", "sky")
    ]
    sep = "\n        "
    return f"""<!-- Mobile Touch Navigation Carousel (Visible ONLY on mobile < 768px) -->\n      <nav class="flex md:hidden items-center gap-1.5 overflow-x-auto no-scrollbar pt-1.5 pb-0.5 font-mono text-[11px] tracking-wider whitespace-nowrap w-full -mx-3 px-3 sm:mx-0 sm:px-0">\n        {sep.join(items)}\n      </nav>"""

def update_html_page(rel_path, active_route):
    path = os.path.join(REPO_PRIMARY, rel_path)
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Replace desktop nav
    d_regex = r'<!-- Quick Inter-Domain Jump Navigation \(Desktop\) -->\s*<nav class="hidden md:flex[^"]*">.*?</nav>'
    new_d = generate_desktop_nav(active_route)
    content, count_d = re.subn(d_regex, new_d, content, flags=re.DOTALL)

    # 2. Replace mobile nav
    m_regex = r'(?:<!-- Mobile Touch Navigation Carousel.*?-->\s*)?<nav class="flex md:hidden[^"]*">.*?</nav>'
    new_m = generate_mobile_nav(active_route)
    content, count_m = re.subn(m_regex, new_m, content, flags=re.DOTALL)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[{rel_path}] Updated nav hierarchy (Desktop: {count_d}, Mobile: {count_m}).")

def update_hub_source():
    path = os.path.join(REPO_PRIMARY, "_src", "hub_source_v0.63.html")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Desktop nav in hub source
    d_hub_regex = r'<nav class="hidden md:flex items-center gap-1 font-mono text-\[11px\] tracking-wider text-slate-400">.*?</nav>'
    new_d_hub = """<nav class="hidden md:flex items-center gap-1 font-mono text-[11px] tracking-wider text-slate-400">
            <a href="/" class="px-2.5 py-1 rounded-md text-slate-400 hover:text-teal-400 hover:bg-slate-800/40 transition-colors">Industrial Hubs</a> <span class="text-slate-600">&middot;</span> <a href="/livewire/" class="inline-flex items-center gap-1 px-2 py-0.5 rounded text-slate-400 hover:text-teal-400 hover:bg-slate-800/40 transition-colors">
              <span class="relative flex h-1.5 w-1.5 shrink-0">
                <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                <span class="relative inline-flex rounded-full h-1.5 w-1.5 bg-emerald-500"></span>
              </span>
              <span>Live Wire</span>
            </a> <span class="text-slate-600">&middot;</span> <a href="/projectenergy/" class="px-2.5 py-1 rounded-md text-slate-400 hover:text-emerald-400 hover:bg-slate-800/40 transition-colors">PDP8 Energy</a> <span class="text-slate-600">&middot;</span> <a href="/evcharging/" class="px-2.5 py-1 rounded-md text-slate-400 hover:text-amber-400 hover:bg-slate-800/40 transition-colors">EV Tech</a> <span class="text-slate-600">&middot;</span> <a href="/calculator/" class="px-2.5 py-1 rounded-md text-slate-400 hover:text-teal-400 hover:bg-slate-800/40 transition-colors">Power Sizer &amp; Tariffs</a> <span class="text-slate-600">&middot;</span> <a href="/hub/" class="px-2.5 py-1 rounded-md text-white font-semibold bg-white/10 border border-white/40 shadow-sm transition-all">Legal Framework</a>
          </nav>"""
    content = re.sub(d_hub_regex, new_d_hub, content, flags=re.DOTALL)

    # Mobile nav in hub source
    m_hub_regex = r'<nav class="flex md:hidden items-center gap-1\.5 overflow-x-auto no-scrollbar pt-1\.5 pb-0\.5 font-mono text-\[11px\] tracking-wider whitespace-nowrap">.*?</nav>'
    new_m_hub = """<nav class="flex md:hidden items-center gap-1.5 overflow-x-auto no-scrollbar pt-1.5 pb-0.5 font-mono text-[11px] tracking-wider whitespace-nowrap">
        <a href="/" class="px-2.5 py-1.5 rounded-lg text-slate-400 hover:text-white bg-white/5 border border-white/10 shrink-0">Industrial Hubs</a>
        <a href="/livewire/" class="inline-flex items-center gap-1 px-2.5 py-1.5 rounded-lg text-slate-400 hover:text-white bg-white/5 border border-white/10 shrink-0">
          <span class="relative flex h-1.5 w-1.5 shrink-0">
            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
            <span class="relative inline-flex rounded-full h-1.5 w-1.5 bg-emerald-500"></span>
          </span>
          <span>Live Wire</span>
        </a>
        <a href="/projectenergy/" class="px-2.5 py-1.5 rounded-lg text-slate-400 hover:text-white bg-white/5 border border-white/10 shrink-0">PDP8 Energy</a>
        <a href="/evcharging/" class="px-2.5 py-1.5 rounded-lg text-slate-400 hover:text-white bg-white/5 border border-white/10 shrink-0">EV Tech</a>
        <a href="/calculator/" class="px-2.5 py-1.5 rounded-lg text-slate-400 hover:text-white bg-white/5 border border-white/10 shrink-0">Power Sizer</a>
        <a href="/hub/" class="px-2.5 py-1.5 rounded-lg text-white font-semibold bg-white/10 border border-white/40 shrink-0">Legal Framework</a>
      </nav>"""
    content = re.sub(m_hub_regex, new_m_hub, content, flags=re.DOTALL)

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
    print("=== REORDERING NAVIGATION HIERARCHY: LIVE WIRE TO LEFT ===")
    update_html_page("index.html", "/")
    update_html_page(os.path.join("green", "index.html"), "/")
    update_html_page(os.path.join("livewire", "index.html"), "/livewire/")
    update_html_page(os.path.join("projectenergy", "index.html"), "/projectenergy/")
    update_html_page(os.path.join("evcharging", "index.html"), "/evcharging/")
    update_html_page(os.path.join("calculator", "index.html"), "/calculator/")
    update_hub_source()
    mirror()
    print("=== COMPLETE ===")
