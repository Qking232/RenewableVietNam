import os
import re

BASE_DIR = r"G:\My Drive\7. AI\RenewableVietNam"

def get_nav_markup(active_page):
    def pill(name, url, is_active):
        if is_active:
            return f'<a href="{url}" class="px-2.5 py-1 rounded text-slate-900 dark:text-white font-medium bg-slate-200/80 dark:bg-slate-800 transition-colors">{name}</a>'
        return f'<a href="{url}" class="px-2.5 py-1 rounded text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">{name}</a>'

    def mobile_pill(name, url, is_active):
        if is_active:
            return f'<a href="{url}" class="px-2.5 py-1 rounded bg-slate-200 dark:bg-slate-800 text-slate-900 dark:text-white font-medium shrink-0">{name}</a>'
        return f'<a href="{url}" class="px-2.5 py-1 rounded text-slate-600 dark:text-slate-400 hover:text-slate-900 bg-white dark:bg-darkSurface border border-slate-200 dark:border-darkBorder shrink-0">{name}</a>'

    dot = '<span class="text-slate-300 dark:text-slate-700">&middot;</span>'

    # Zone 2 buttons with distinct structural indicator
    def zone2_btn(name, url, is_active):
        active_cls = "bg-white dark:bg-darkCard text-slate-900 dark:text-white shadow-xs" if is_active else "text-slate-700 dark:text-slate-300 hover:text-slate-900 dark:hover:text-white hover:bg-white dark:hover:bg-darkCard"
        return f'<a href="{url}" class="px-2 py-0.5 rounded text-[10px] uppercase font-semibold {active_cls} transition-all flex items-center gap-1"><span>{name}</span><span class="text-[9px] text-slate-400">&nearr;</span></a>'

    desktop_nav = f"""<nav class="hidden md:flex items-center gap-1.5 font-mono text-[11px] tracking-wide text-slate-500 dark:text-slate-400">
            {pill("Overview", "https://renewablevietnam.com/", active_page == "home")}
            {dot}
            {pill("PDP8 Energy", "https://energy.renewablevietnam.com/", active_page == "wind")}
            {dot}
            {pill("Green Industrial", "https://ind.renewablevietnam.com/", active_page == "ind")}
            {dot}
            {pill("EV Tech", "https://ev.renewablevietnam.com/", active_page == "ev")}
            <div class="h-4 w-px bg-slate-300 dark:bg-slate-700 mx-2"></div>
            <div class="flex items-center gap-1.5 p-0.5 rounded-md border border-slate-300/80 dark:border-slate-700/80 bg-slate-100/50 dark:bg-slate-900/40">
              {zone2_btn("Legal Framework", "https://legal.renewablevietnam.com/", active_page == "legal")}
              {dot}
              {zone2_btn("Investment M&A", "https://invest.renewablevietnam.com/", active_page == "invest")}
            </div>
          </nav>"""

    mobile_nav = f"""<nav class="flex md:hidden items-center gap-1.5 overflow-x-auto no-scrollbar pt-1 pb-0.5 font-mono text-[11px] whitespace-nowrap w-full">
        {mobile_pill("Overview", "https://renewablevietnam.com/", active_page == "home")}
        {mobile_pill("PDP8 Energy", "https://energy.renewablevietnam.com/", active_page == "wind")}
        {mobile_pill("Green Industrial", "https://ind.renewablevietnam.com/", active_page == "ind")}
        {mobile_pill("EV Tech", "https://ev.renewablevietnam.com/", active_page == "ev")}
        <div class="h-4 w-px bg-slate-300 dark:bg-slate-700 shrink-0 mx-1"></div>
        <a href="https://legal.renewablevietnam.com/" class="px-2 py-1 rounded text-[10px] uppercase font-semibold text-slate-700 dark:text-slate-300 bg-slate-100 dark:bg-slate-900 border border-slate-300 dark:border-slate-700 shrink-0">Legal Framework &nearr;</a>
        <a href="https://invest.renewablevietnam.com/" class="px-2 py-1 rounded text-[10px] uppercase font-semibold text-slate-700 dark:text-slate-300 bg-slate-100 dark:bg-slate-900 border border-slate-300 dark:border-slate-700 shrink-0">Investment M&A &nearr;</a>
      </nav>"""

    return desktop_nav, mobile_nav

PAGES = [
    {
        "file": os.path.join(BASE_DIR, "evcharging", "index.html"),
        "key": "ev"
    },
    {
        "file": os.path.join(BASE_DIR, "evcharging", "ev", "index.html"),
        "key": "ev"
    },
    {
        "file": os.path.join(BASE_DIR, "projectenergy", "index.html"),
        "key": "wind"
    },
    {
        "file": os.path.join(BASE_DIR, "green", "index.html"),
        "key": "ind"
    },
    {
        "file": os.path.join(BASE_DIR, "livewire", "index.html"),
        "key": "livewire"
    }
]

desktop_pattern = re.compile(r'<nav class="hidden md:flex items-center gap-1.*?</nav>', re.DOTALL)
mobile_pattern = re.compile(r'<nav class="flex md:hidden items-center gap-1\.5 overflow-x-auto no-scrollbar.*?</nav>', re.DOTALL)

for p in PAGES:
    fpath = p["file"]
    key = p["key"]
    desktop_nav, mobile_nav = get_nav_markup(key)

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Brand link update to strictly Renewable Viet Nam
    content = content.replace("RENEWABLE INFRASTRUCTURE", "RENEWABLE VIET NAM")
    content = content.replace("ECO-INDUSTRIAL INFRASTRUCTURE", "RENEWABLE VIET NAM")
    content = content.replace("EV CHARGING INFRASTRUCTURE", "RENEWABLE VIET NAM")

    new_content = desktop_pattern.sub(desktop_nav, content)
    new_content = mobile_pattern.sub(mobile_nav, new_content)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"Successfully standardized navigation in {fpath} (Active: {key})")
