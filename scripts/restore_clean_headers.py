import os
import re

REPOS = [
    r"G:\My Drive\7. AI\Gemini\RenewableVietNam",
    r"G:\My Drive\7. AI\Gemini\Qking232.github.io"
]

ORIGINAL_HEADER_HUBS = '''  <header class="sticky top-0 z-40 w-full bg-alabaster/95 dark:bg-obsidian/95 backdrop-blur-md border-b border-borderSlate dark:border-darkBorder -mx-4 sm:-mx-6 lg:-mx-8 px-4 sm:px-6 lg:px-8 transition-colors shadow-sm">
    <div class="max-w-7xl mx-auto flex flex-col gap-2 py-2.5 sm:py-3.5">
      <!-- Top Row: Brand, Desktop Nav, and Header CTAs -->
      <div class="flex items-center justify-between w-full">
        <div class="flex items-center gap-6">
          <a href="/" class="flex items-center gap-2.5 sm:gap-3 group shrink-0" aria-label="Renewable Vietnam — home">
            <img src="/assets/images/logo.svg" alt="Renewable Viet Nam Mark" width="34" height="34" class="w-8 h-8 sm:w-8.5 sm:h-8.5 rounded-lg shrink-0 shadow-sm" />
            <span class="text-[11px] sm:text-xs font-mono uppercase tracking-[0.14em] sm:tracking-[0.24em] text-inkPrimary dark:text-textDarkPrimary font-semibold">
              RENEWABLE INFRASTRUCTURE
            </span>
          </a>

          <!-- Quick Inter-Domain Jump Navigation (Desktop) -->
          <nav class="hidden md:flex items-center gap-1 font-mono text-[11px] tracking-wider text-inkMuted dark:text-textDarkMuted">
            <a href="/" class="px-2.5 py-1 rounded-md text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20">Industrial Hubs</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/projectenergy/" class="px-2.5 py-1 rounded-md hover:text-emerald-600 dark:hover:text-emerald-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Energy Map</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/evcharging/" class="px-2.5 py-1 rounded-md hover:text-amber-600 dark:hover:text-amber-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">EV Stations</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="#pdp8" class="px-2.5 py-1 rounded-md hover:text-teal-600 dark:hover:text-teal-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">PDP8 Tracker</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/calculator/" class="px-2.5 py-1 rounded-md hover:text-teal-600 dark:hover:text-teal-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Power Sizer &amp; Tariffs</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/hub/" class="px-2.5 py-1 rounded-md hover:text-sky-600 dark:hover:text-sky-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">The Library</a>
          </nav>
        </div>

        <!-- Right Controls -->
        <div class="flex items-center gap-1.5 sm:gap-2">
          <a href="#marketWire" class="inline-flex items-center gap-1.5 px-2.5 sm:px-3 py-1.5 rounded-lg font-mono text-[10px] sm:text-[11px] text-inkPrimary dark:text-textDarkPrimary bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder hover:border-teal-500 dark:hover:border-teal-400/40 transition-all shadow-sm">
            <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse shrink-0"></span>
            <span>Live Wire</span>
          </a>

          <a href="/calculator/" class="hidden sm:inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg font-mono text-[11px] text-inkPrimary dark:text-textDarkPrimary bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder hover:border-teal-500 dark:hover:border-teal-400/40 transition-all shadow-sm">
            <svg class="w-3.5 h-3.5 text-teal-500 dark:text-teal-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
            </svg>
            <span>Power Sizer &amp; Tariffs</span>
          </a>

          <button id="themeToggleBtn" aria-label="Toggle Theme" class="flex items-center justify-center w-8.5 h-8.5 rounded-lg bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder shadow-sm hover:border-slate-400 dark:hover:border-slate-500 text-inkMuted dark:text-textDarkMuted transition-all cursor-pointer">
            <svg id="sunIcon" class="hidden w-4 h-4 text-amber-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.6">
              <path stroke-linecap="round" stroke-linejoin="round" d="M12 3v2.25m6.364.386-1.591 1.591M21 12h-2.25m-.386 6.364-1.591-1.591M12 18.75V21m-4.773-4.227-1.591 1.591M5.25 12H3m4.227-4.773L5.636 5.636M15.75 12a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0Z" />
            </svg>
            <svg id="moonIcon" class="w-4 h-4 text-slate-700 dark:text-slate-300" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.6">
              <path stroke-linecap="round" stroke-linejoin="round" d="M21.752 15.002A9.72 9.72 0 0 1 18 15.75c-5.385 0-9.75-4.365-9.75-9.75 0-1.33.266-2.597.748-3.752A9.753 9.753 0 0 0 3 11.25C3 16.635 7.365 21 12.75 21a9.753 9.753 0 0 0 9.002-5.998Z" />
            </svg>
          </button>
        </div>
      </div>

      <!-- Mobile Touch Navigation Carousel (Visible ONLY on mobile < 768px) -->
      <nav class="flex md:hidden items-center gap-1.5 overflow-x-auto no-scrollbar pt-1.5 pb-0.5 font-mono text-[11px] tracking-wider whitespace-nowrap">
        <a href="/" class="px-2.5 py-1.5 rounded-lg text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20 shrink-0">Industrial Hubs</a>
        <a href="/projectenergy/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-emerald-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">Energy Map</a>
        <a href="/evcharging/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-amber-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">EV Stations</a>
        <a href="#pdp8" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-teal-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">PDP8 Tracker</a>
        <a href="/calculator/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-teal-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">Power Sizer</a>
        <a href="/hub/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-sky-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">The Library</a>
      </nav>
    </div>
  </header>'''

ORIGINAL_HEADER_CALC = '''  <header class="sticky top-0 z-40 w-full bg-alabaster/95 dark:bg-obsidian/95 backdrop-blur-md border-b border-borderSlate dark:border-darkBorder -mx-4 sm:-mx-6 lg:-mx-8 px-4 sm:px-6 lg:px-8 transition-colors shadow-sm">
    <div class="max-w-7xl mx-auto flex flex-col gap-2 py-2.5 sm:py-3.5">
      <!-- Top Row: Brand, Desktop Nav, and Header CTAs -->
      <div class="flex items-center justify-between w-full">
        <div class="flex items-center gap-6">
          <a href="/" class="flex items-center gap-2.5 sm:gap-3 group shrink-0" aria-label="Renewable Vietnam — home">
            <img src="/assets/images/logo.svg" alt="Renewable Viet Nam Mark" width="34" height="34" class="w-8 h-8 sm:w-8.5 sm:h-8.5 rounded-lg shrink-0 shadow-sm" />
            <span class="text-[11px] sm:text-xs font-mono uppercase tracking-[0.14em] sm:tracking-[0.24em] text-inkPrimary dark:text-textDarkPrimary font-semibold">
              RENEWABLE INFRASTRUCTURE
            </span>
          </a>

          <!-- Quick Inter-Domain Jump Navigation (Desktop) -->
          <nav class="hidden md:flex items-center gap-1 font-mono text-[11px] tracking-wider text-inkMuted dark:text-textDarkMuted">
            <a href="/" class="px-2.5 py-1 rounded-md hover:text-teal-600 dark:hover:text-teal-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Industrial Hubs</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/projectenergy/" class="px-2.5 py-1 rounded-md hover:text-emerald-600 dark:hover:text-emerald-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">Energy Map</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/evcharging/" class="px-2.5 py-1 rounded-md hover:text-amber-600 dark:hover:text-amber-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">EV Stations</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/calculator/" class="px-2.5 py-1 rounded-md text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20">Power Sizer &amp; Tariffs</a>
            <span class="text-slate-300 dark:text-slate-700">&middot;</span>
            <a href="/hub/" class="px-2.5 py-1 rounded-md hover:text-sky-600 dark:hover:text-sky-400 hover:bg-slate-100 dark:hover:bg-darkCard transition-colors">The Library</a>
          </nav>
        </div>

        <!-- Right Controls -->
        <div class="flex items-center gap-1.5 sm:gap-2">
          <a href="/#marketWire" class="inline-flex items-center gap-1.5 px-2.5 sm:px-3 py-1.5 rounded-lg font-mono text-[10px] sm:text-[11px] text-inkPrimary dark:text-textDarkPrimary bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder hover:border-teal-500 dark:hover:border-teal-400/40 transition-all shadow-sm">
            <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse shrink-0"></span>
            <span>Live Wire</span>
          </a>

          <a href="/" class="hidden sm:inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg font-mono text-[11px] text-inkPrimary dark:text-textDarkPrimary bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder hover:border-teal-500 dark:hover:border-teal-400/40 transition-all shadow-sm">
            <svg class="w-3.5 h-3.5 text-teal-500 dark:text-teal-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
            </svg>
            <span>Back to Hubs</span>
          </a>

          <button id="themeToggleBtn" aria-label="Toggle Theme" class="flex items-center justify-center w-8.5 h-8.5 rounded-lg bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder shadow-sm hover:border-slate-400 dark:hover:border-slate-500 text-inkMuted dark:text-textDarkMuted transition-all cursor-pointer">
            <svg id="sunIcon" class="hidden w-4 h-4 text-amber-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.6">
              <path stroke-linecap="round" stroke-linejoin="round" d="M12 3v2.25m6.364.386-1.591 1.591M21 12h-2.25m-.386 6.364-1.591-1.591M12 18.75V21m-4.773-4.227-1.591 1.591M5.25 12H3m4.227-4.773L5.636 5.636M15.75 12a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0Z" />
            </svg>
            <svg id="moonIcon" class="w-4 h-4 text-slate-700 dark:text-slate-300" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.6">
              <path stroke-linecap="round" stroke-linejoin="round" d="M21.752 15.002A9.72 9.72 0 0 1 18 15.75c-5.385 0-9.75-4.365-9.75-9.75 0-1.33.266-2.597.748-3.752A9.753 9.753 0 0 0 3 11.25C3 16.635 7.365 21 12.75 21a9.753 9.753 0 0 0 9.002-5.998Z" />
            </svg>
          </button>
        </div>
      </div>

      <!-- Mobile Touch Navigation Carousel (Visible ONLY on mobile < 768px) -->
      <nav class="flex md:hidden items-center gap-1.5 overflow-x-auto no-scrollbar pt-1.5 pb-0.5 font-mono text-[11px] tracking-wider whitespace-nowrap">
        <a href="/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-teal-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">Industrial Hubs</a>
        <a href="/projectenergy/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-emerald-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">Energy Map</a>
        <a href="/evcharging/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-amber-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">EV Stations</a>
        <a href="/calculator/" class="px-2.5 py-1.5 rounded-lg text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20 shrink-0">Power Sizer</a>
        <a href="/hub/" class="px-2.5 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-sky-500 bg-white/60 dark:bg-darkSurface/60 border border-borderSlate dark:border-darkBorder shrink-0">The Library</a>
      </nav>
    </div>
  </header>'''

def update_file(path, new_header):
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Match <header[\s\S]*?</header>
    pattern = re.compile(r'<header[\s\S]*?</header>', re.IGNORECASE)
    if pattern.search(content):
        updated = pattern.sub(new_header.strip(), content, count=1)
        with open(path, "w", encoding="utf-8") as f:
            f.write(updated)
        print(f"Updated header in: {path}")
    else:
        print(f"Header tag not found in: {path}")

def main():
    for repo in REPOS:
        update_file(os.path.join(repo, "index.html"), ORIGINAL_HEADER_HUBS)
        update_file(os.path.join(repo, "green", "index.html"), ORIGINAL_HEADER_HUBS)
        update_file(os.path.join(repo, "calculator", "index.html"), ORIGINAL_HEADER_CALC)

if __name__ == "__main__":
    main()
