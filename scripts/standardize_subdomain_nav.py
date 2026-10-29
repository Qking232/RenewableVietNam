import os
import re

BASE_DIR = r"G:\My Drive\7. AI\RenewableVietNam"

def get_nav_markup(active_page):
    def pill(name, url, is_active, active_class="text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20", inactive_class="hover:text-teal-600 dark:hover:text-teal-400 hover:bg-slate-100 dark:hover:bg-darkCard"):
        cls = active_class if is_active else inactive_class
        return f'<a href="{url}" class="px-2.5 py-1 rounded-md {cls} transition-colors">{name}</a>'

    def mobile_pill(name, url, is_active, active_class="text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20", inactive_class="text-inkMuted dark:text-textDarkMuted hover:text-teal-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder"):
        cls = active_class if is_active else inactive_class
        return f'<a href="{url}" class="px-2.5 py-1.5 rounded-lg {cls} shrink-0">{name}</a>'

    dot = '<span class="text-slate-300 dark:text-slate-700">&middot;</span>'

    lw_cls = "text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20 shadow-sm" if active_page == "livewire" else "hover:text-teal-600 dark:hover:text-teal-400 hover:bg-slate-100 dark:hover:bg-darkCard"
    lw_mob_cls = "text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20 shadow-sm" if active_page == "livewire" else "text-inkMuted dark:text-textDarkMuted hover:text-teal-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder"

    desktop_nav = f"""<nav class="hidden md:flex items-center gap-1 font-mono text-[11px] tracking-wider text-inkMuted dark:text-textDarkMuted">
            <a href="https://renewablevietnam.com/livewire/" class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md {lw_cls} transition-colors group">
              <span class="relative flex h-2 w-2 shrink-0">
                <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                <span class="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
              </span>
              <span>Live Wire</span>
            </a>
            {dot}
            {pill("Master Dashboard", "https://renewablevietnam.com/", active_page == "home")}
            {dot}
            {pill("PDP8 Energy", "https://wind.renewablevietnam.com/", active_page == "wind")}
            {dot}
            {pill("Green Industrial", "https://ind.renewablevietnam.com/", active_page == "ind")}
            {dot}
            {pill("EV Tech", "https://ev.renewablevietnam.com/", active_page == "ev")}
            {dot}
            {pill("Legal Framework", "https://legal.renewablevietnam.com/", active_page == "legal")}
            {dot}
            {pill("Investment M&A", "https://invest.renewablevietnam.com/", active_page == "invest", "text-blue-600 dark:text-blue-400 font-semibold bg-blue-500/10 dark:bg-blue-400/10 border border-blue-500/20", "hover:text-blue-600 dark:hover:text-blue-400 hover:bg-slate-100 dark:hover:bg-darkCard")}
          </nav>"""

    mobile_nav = f"""<nav class="flex md:hidden items-center gap-1.5 overflow-x-auto no-scrollbar pt-1.5 pb-0.5 font-mono text-[11px] tracking-wider whitespace-nowrap w-full -mx-3 px-3 sm:mx-0 sm:px-0">
        <a href="https://renewablevietnam.com/livewire/" class="inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg {lw_mob_cls} shrink-0">
          <span class="relative flex h-2 w-2 shrink-0">
            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
            <span class="relative inline-flex rounded-full h-2 w-2 bg-emerald-500"></span>
          </span>
          <span>Live Wire</span>
        </a>
        {mobile_pill("Dashboard", "https://renewablevietnam.com/", active_page == "home")}
        {mobile_pill("PDP8 Energy", "https://wind.renewablevietnam.com/", active_page == "wind")}
        {mobile_pill("Green Industrial", "https://ind.renewablevietnam.com/", active_page == "ind")}
        {mobile_pill("EV Tech", "https://ev.renewablevietnam.com/", active_page == "ev")}
        {mobile_pill("Legal Framework", "https://legal.renewablevietnam.com/", active_page == "legal")}
        {mobile_pill("Investment M&A", "https://invest.renewablevietnam.com/", active_page == "invest", "text-blue-600 dark:text-blue-400 font-semibold bg-blue-500/10 dark:bg-blue-400/10 border border-blue-500/20", "text-inkMuted dark:text-textDarkMuted hover:text-blue-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder")}
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

desktop_pattern = re.compile(r'<nav class="hidden md:flex items-center gap-1 font-mono text-\[11px\].*?</nav>', re.DOTALL)
mobile_pattern = re.compile(r'<nav class="flex md:hidden items-center gap-1\.5 overflow-x-auto no-scrollbar.*?</nav>', re.DOTALL)

for p in PAGES:
    fpath = p["file"]
    key = p["key"]
    desktop_nav, mobile_nav = get_nav_markup(key)

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Brand link update
    content = re.sub(r'<a href="/" class="flex items-center gap-2\.5 sm:gap-3 group shrink-0"', r'<a href="https://renewablevietnam.com/" class="flex items-center gap-2.5 sm:gap-3 group shrink-0"', content)

    # Remove calculator links from footer
    content = re.sub(r'<a href="/calculator/".*?</a>', '', content)

    new_content = desktop_pattern.sub(desktop_nav, content)
    new_content = mobile_pattern.sub(mobile_nav, new_content)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"Successfully standardized navigation in {fpath} (Active: {key})")
