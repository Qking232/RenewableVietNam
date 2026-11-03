import os
import re
import shutil

BASE_DIR = r"G:\My Drive\7. AI\RenewableVietNam"

def get_nav(active_key):
    def pill(name, url, is_active):
        if is_active:
            cls = "px-2.5 py-1 rounded-md text-teal-700 dark:text-teal-300 font-medium bg-slate-100 dark:bg-slate-800 transition-colors"
        else:
            cls = "px-2.5 py-1 rounded-md hover:text-slate-900 dark:hover:text-slate-100 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors"
        return f'<a href="{url}" class="{cls}">{name}</a>'

    dot = '<span class="text-slate-300 dark:text-slate-700">&middot;</span>'

    desktop = f"""<nav class="hidden md:flex items-center gap-1 font-mono text-[11px] text-slate-600 dark:text-slate-400">
          {pill("Cockpit", "https://renewablevietnam.com/", active_key == "home")}
          {dot}
          {pill("Energy", "https://energy.renewablevietnam.com/", active_key == "energy")}
          {dot}
          {pill("Industrial", "https://industrial.renewablevietnam.com/", active_key == "industrial")}
          {dot}
          {pill("EV Tech", "https://ev.renewablevietnam.com/", active_key == "ev")}
          {dot}
          {pill("Legal &amp; Investment M&amp;A", "https://invest.renewablevietnam.com/", active_key == "invest")}
          {dot}
          {pill("Project Delivery", "https://project.renewablevietnam.com/", active_key == "project")}
        </nav>"""
    return desktop

def get_mobile(active_key):
    def mpill(name, url, is_active):
        if is_active:
            cls = "px-2.5 py-1 rounded-md text-teal-700 dark:text-teal-300 font-semibold bg-slate-100 dark:bg-slate-800 border border-teal-500/20 shrink-0"
        else:
            cls = "px-2.5 py-1 rounded-md text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200 bg-slate-50 dark:bg-slate-800/50 border border-slate-200/60 dark:border-slate-700/50 shrink-0"
        return f'<a href="{url}" class="{cls}">{name}</a>'

    mobile = f"""<!-- Mobile Quick Navigation Ribbon -->
    <div class="flex items-center gap-1.5 overflow-x-auto no-scrollbar md:hidden px-4 pb-2 pt-1 border-t border-slate-100 dark:border-slate-800 font-mono text-[10px]">
      {mpill("Cockpit", "https://renewablevietnam.com/", active_key == "home")}
      {mpill("Energy", "https://energy.renewablevietnam.com/", active_key == "energy")}
      {mpill("Industrial", "https://industrial.renewablevietnam.com/", active_key == "industrial")}
      {mpill("EV Tech", "https://ev.renewablevietnam.com/", active_key == "ev")}
      {mpill("Legal &amp; M&amp;A", "https://invest.renewablevietnam.com/", active_key == "invest")}
      {mpill("Project Delivery", "https://project.renewablevietnam.com/", active_key == "project")}
    </div>"""
    return mobile

PAGES = [
    {
        "file": os.path.join(BASE_DIR, "projectenergy", "index.html"),
        "key": "energy",
        "rev": os.path.join(BASE_DIR, "projectenergy", "index_Rev.012.html")
    },
    {
        "file": os.path.join(BASE_DIR, "industrial", "index.html"),
        "key": "industrial",
        "rev": os.path.join(BASE_DIR, "industrial", "index_Rev.007.html")
    },
    {
        "file": os.path.join(BASE_DIR, "evcharging", "index.html"),
        "key": "ev",
        "rev": os.path.join(BASE_DIR, "evcharging", "index_Rev.008.html")
    },
    {
        "file": os.path.join(BASE_DIR, "evcharging", "ev", "index.html"),
        "key": "ev",
        "rev": os.path.join(BASE_DIR, "evcharging", "ev", "index_Rev.005.html")
    },
    {
        "file": os.path.join(BASE_DIR, "invm", "index.html"),
        "key": "invest",
        "rev": os.path.join(BASE_DIR, "invm", "index_Rev.032.html")
    },
    {
        "file": os.path.join(BASE_DIR, "project", "index.html"),
        "key": "project",
        "rev": os.path.join(BASE_DIR, "project", "index_Rev.006.html")
    },
    {
        "file": os.path.join(BASE_DIR, "livewire", "index.html"),
        "key": "livewire",
        "rev": os.path.join(BASE_DIR, "livewire", "index_Rev.005.html")
    }
]

desktop_pattern = re.compile(r'<nav class="hidden md:flex items-center gap-1 font-mono text-\[11px\].*?</nav>', re.DOTALL)
mobile_pattern = re.compile(r'<!-- Mobile Quick Navigation Ribbon -->\s*<div class="flex items-center gap-1\.5 overflow-x-auto no-scrollbar md:hidden.*?</div>', re.DOTALL)
badge_pattern = re.compile(r'<span>\d+ Edge Gateways Live</span>')

for p in PAGES:
    fpath = p["file"]
    key = p["key"]
    rev_path = p["rev"]

    if not os.path.exists(fpath):
        print(f"Skipping {fpath}: file not found")
        continue

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Save sequential revision first
    with open(rev_path, "w", encoding="utf-8") as rf:
        rf.write(content)
    print(f"Preserved revision: {rev_path}")

    # Generate updated markups
    desktop_nav = get_nav(key)
    mobile_nav = get_mobile(key)

    new_content = desktop_pattern.sub(desktop_nav, content)
    new_content = mobile_pattern.sub(mobile_nav, new_content)
    new_content = badge_pattern.sub('<span>5 Edge Gateways Live</span>', new_content)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"Standardized navigation in {fpath} (Active: {key})")

if __name__ == "__main__":
    print("All portals standardized to 5-gateway network successfully.")
