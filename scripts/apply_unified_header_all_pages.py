"""
Deploy unified institutional glassmorphic header across all portal pages:
1. projectenergy/index.html (Energy Map)
2. evcharging/index.html (EV Stations)
3. _src/hub_source_v0.63.html -> compiled to hub/index.html (The Library)
4. calculator/index.html & green/calculator/index.html (Power Sizer & Tariffs)
5. index.html & green/index.html (Industrial Hubs)
And synchronize 100% across RenewableVietNam and Qking232.github.io.
"""
import os
import re
import subprocess

REPO1 = "G:/My Drive/7. AI/Gemini/RenewableVietNam"
REPO2 = "G:/My Drive/7. AI/Gemini/Qking232.github.io"

# Shared Header Components
def get_brand_html():
    return '''<a href="/" class="flex items-center gap-2.5 sm:gap-3 group shrink-0" aria-label="Renewable Vietnam — home">
            <img src="/assets/images/logo.svg" alt="Renewable Viet Nam Mark" width="34" height="34" class="w-8 h-8 sm:w-8.5 sm:h-8.5 rounded-lg shrink-0 shadow-sm" />
            <span class="text-[11px] sm:text-xs font-mono uppercase tracking-[0.14em] sm:tracking-[0.24em] text-white font-semibold">
              RENEWABLE INFRASTRUCTURE
            </span>
          </a>'''

def get_desktop_nav_html(active_route):
    # Route keys: 'hubs', 'energy', 'ev', 'calc', 'hub'
    def item(key, label, url, color_hover="teal"):
        if key == active_route:
            return f'<a href="{url}" class="px-2.5 py-1 rounded-md text-white font-semibold bg-white/10 border border-white/40 shadow-sm transition-all">{label}</a>'
        return f'<a href="{url}" class="px-2.5 py-1 rounded-md text-slate-400 hover:text-{color_hover}-400 hover:bg-slate-800/40 transition-colors">{label}</a>'

    dot = '<span class="text-slate-600">&middot;</span>'
    nav_links = [
        item('hubs', 'Industrial Hubs', '/'),
        dot,
        item('energy', 'Energy Map', '/projectenergy/', 'emerald'),
        dot,
        item('ev', 'EV Stations', '/evcharging/', 'amber'),
        dot,
        item('calc', 'Power Sizer &amp; Tariffs', '/calculator/', 'teal'),
        dot,
        item('hub', 'The Library', '/hub/', 'sky')
    ]
    return f'''<nav class="hidden md:flex items-center gap-1 font-mono text-[11px] tracking-wider text-slate-400">
            {' '.join(nav_links)}
          </nav>'''

def get_mobile_nav_html(active_route):
    def item(key, label, url, color_active="teal"):
        if key == active_route:
            return f'<a href="{url}" class="px-2.5 py-1.5 rounded-lg text-white font-semibold bg-white/10 border border-white/40 shrink-0">{label}</a>'
        return f'<a href="{url}" class="px-2.5 py-1.5 rounded-lg text-slate-400 hover:text-white bg-white/5 border border-white/10 shrink-0">{label}</a>'

    return f'''<nav class="flex md:hidden items-center gap-1.5 overflow-x-auto no-scrollbar pt-1.5 pb-0.5 font-mono text-[11px] tracking-wider whitespace-nowrap">
        {item('hubs', 'Industrial Hubs', '/')}
        {item('energy', 'Energy Map', '/projectenergy/')}
        {item('ev', 'EV Stations', '/evcharging/')}
        {item('calc', 'Power Sizer', '/calculator/')}
        {item('hub', 'The Library', '/hub/')}
      </nav>'''

# 1. Update projectenergy/index.html
def update_projectenergy():
    print("Updating projectenergy/index.html...")
    for repo in [REPO1, REPO2]:
        path = os.path.join(repo, "projectenergy", "index.html")
        if not os.path.exists(path):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        new_header = f'''  <!-- ==================== HEADER ==================== -->
  <header class="sticky top-0 z-50 w-full bg-[#090B0E]/95 backdrop-blur-md border-b border-[#232834] transition-colors shadow-sm">
    <div class="max-w-7xl mx-auto flex flex-col gap-2 py-2.5 sm:py-3.5 px-4 sm:px-6 lg:px-8">
      <!-- Top Row: Brand, Desktop Nav, and Header CTAs -->
      <div class="flex items-center justify-between w-full">
        <div class="flex items-center gap-6">
          {get_brand_html()}

          <!-- Desktop Navigation -->
          {get_desktop_nav_html('energy')}
        </div>

        <!-- Right Controls -->
        <div class="flex items-center gap-1.5 sm:gap-2">
          <a href="#marketWire" class="inline-flex items-center gap-1.5 px-2.5 sm:px-3 py-1.5 rounded-lg font-mono text-[10px] sm:text-[11px] text-white bg-[#171C26] border border-[#232834] hover:border-teal-500 transition-all shadow-sm">
            <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse shrink-0"></span>
            <span>Live Wire</span>
          </a>

          <a href="/calculator/" class="hidden sm:inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg font-mono text-[11px] text-white bg-[#171C26] border border-[#232834] hover:border-teal-500 transition-all shadow-sm">
            <svg class="w-3.5 h-3.5 text-teal-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
            </svg>
            <span>Power Sizer &amp; Tariffs</span>
          </a>

          <!-- Language Selector -->
          <div class="inline-flex border border-[#232834] bg-[#171C26] p-0.5 rounded">
            <button onclick="setLanguage('en')" id="btn-lang-en" class="px-2 py-0.5 bg-white text-black font-medium transition-colors text-[10px] rounded-sm">EN</button>
            <button onclick="setLanguage('vi')" id="btn-lang-vi" class="px-2 py-0.5 text-slate-400 hover:text-white transition-colors text-[10px] rounded-sm">VI</button>
          </div>
        </div>
      </div>

      <!-- Mobile Touch Navigation Carousel -->
      {get_mobile_nav_html('energy')}
    </div>
  </header>'''

        # Replace existing header
        pattern = r'<!-- ==================== HEADER ==================== -->.*?<!-- ==================== HERO SECTION ==================== -->'
        replacement = new_header + "\n\n  <!-- ==================== HERO SECTION ==================== -->"
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  Written {path}")

# 2. Update evcharging/index.html
def update_evcharging():
    print("Updating evcharging/index.html...")
    for repo in [REPO1, REPO2]:
        path = os.path.join(repo, "evcharging", "index.html")
        if not os.path.exists(path):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        new_header = f'''<header class="app-header" style="padding: 6px 14px; background: #090B0E; border-bottom: 1px solid #232834; display: flex; flex-direction: column; gap: 6px; z-index: 1000;">
    <div style="display: flex; align-items: center; justify-content: space-between; width: 100%;">
      <div style="display: flex; align-items: center; gap: 16px;">
        <button class="header-icon-btn" id="toggleSide" title="Ẩn / hiện thanh bên" data-i18n-title="panel_t" aria-label="Menu" style="width: 30px; height: 30px; border-radius: 6px; border: 1px solid #232834; background: #171C26; color: #fff; cursor: pointer; font-size: 13px;">&#9776;</button>
        {get_brand_html()}
        <!-- Desktop Nav -->
        {get_desktop_nav_html('ev')}
      </div>

      <!-- Right Controls -->
      <div style="display: flex; align-items: center; gap: 8px;">
        <a href="/#marketWire" class="hidden sm:inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg font-mono text-[11px] text-white bg-[#171C26] border border-[#232834] hover:border-teal-500 transition-all shadow-sm" style="text-decoration:none;">
          <span style="display:inline-block; width:7px; height:7px; border-radius:50%; background:#10b981;"></span>
          <span>Live Wire</span>
        </a>
        <a href="/calculator/" class="hidden sm:inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg font-mono text-[11px] text-white bg-[#171C26] border border-[#232834] hover:border-teal-500 transition-all shadow-sm" style="text-decoration:none;">
          <svg style="width:14px; height:14px; color:#2dd4bf;" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
          </svg>
          <span>Power Sizer</span>
        </a>
        <button class="header-btn" id="langBtn" title="Ngôn ngữ / Language" data-i18n-title="lang_t" style="height:30px; padding:0 8px; border-radius:6px; border:1px solid #232834; background:#171C26; color:#fff; cursor:pointer; font-size:11px;">
          <span class="lang-icon">🌐</span> <span id="langTxt">EN</span>
        </button>
        <button class="header-icon-btn" id="themeBtn" title="Đổi sáng / tối" data-i18n-title="theme_t" aria-label="Theme" style="width:30px; height:30px; border-radius:6px; border:1px solid #232834; background:#171C26; color:#fbbf24; cursor:pointer; font-size:13px;">&#9788;</button>
      </div>
    </div>
    {get_mobile_nav_html('ev')}
  </header>'''

        # Replace existing header
        pattern = r'<header class="app-header">.*?</header>'
        content = re.sub(pattern, new_header, content, flags=re.DOTALL)

        # Ensure Tailwind classes for font-mono and no-scrollbar exist in evcharging
        if '.no-scrollbar' not in content:
            style_inject = '''<style>
.no-scrollbar::-webkit-scrollbar { display: none; }
.no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
</style>'''
            content = content.replace('</head>', f'{style_inject}\n</head>')

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  Written {path}")

# 3. Update _src/hub_source_v0.63.html and recompile
def update_hub():
    print("Updating _src/hub_source_v0.63.html and recompiling hub/index.html...")
    src_path = os.path.join(REPO1, "_src", "hub_source_v0.63.html")
    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_header = f'''<header class="top" style="position: sticky; top: 0; z-index: 40; background: #090B0E; border-bottom: 1px solid #232834; display: flex; flex-direction: column; gap: 6px; padding: 8px 18px;">
    <div style="display: flex; align-items: center; justify-content: space-between; width: 100%;">
      <div style="display: flex; align-items: center; gap: 20px;">
        {get_brand_html()}
        {get_desktop_nav_html('hub')}
      </div>
      <div class="top-actions" style="display: flex; align-items: center; gap: 8px;">
        <a href="/#marketWire" class="link-btn" style="display:inline-flex; align-items:center; gap:5px; font-family:monospace; font-size:11px; padding:5px 10px; border-radius:6px; border:1px solid #232834; background:#171C26; color:#fff; text-decoration:none;">
          <span style="display:inline-block; width:6px; height:6px; border-radius:50%; background:#10b981;"></span> Live Wire
        </a>
        <a href="/calculator/" class="link-btn" style="display:inline-flex; align-items:center; gap:5px; font-family:monospace; font-size:11px; padding:5px 10px; border-radius:6px; border:1px solid #232834; background:#171C26; color:#fff; text-decoration:none;">
          <span>⚙ Tariffs</span>
        </a>
        <button class="btn small" id="keyBtn" type="button" title="Sign up with a name, email and private key">Sign Up</button>
        <button class="btn small" id="keyReBtn" type="button" title="Sign in with the email and private key you registered">Sign in</button>
        <button class="icon-btn" id="themeBtn" type="button" aria-label="Toggle light / dark theme">
          <svg id="iconSun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" style="display:none">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 3v2.25m6.364.386-1.591 1.591M21 12h-2.25m-.386 6.364-1.591-1.591M12 18.75V21m-4.773-4.227-1.591 1.591M5.25 12H3m4.227-4.773L5.636 5.636M15.75 12a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0Z" />
          </svg>
          <svg id="iconMoon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6">
            <path stroke-linecap="round" stroke-linejoin="round" d="M21.752 15.002A9.72 9.72 0 0 1 18 15.75c-5.385 0-9.75-4.365-9.75-9.75 0-1.33.266-2.597.748-3.752A9.753 9.753 0 0 0 3 11.25C3 16.635 7.365 21 12.75 21a9.753 9.753 0 0 0 9.002-5.998Z" />
          </svg>
        </button>
      </div>
    </div>
    {get_mobile_nav_html('hub')}
  </header>'''

    pattern = r'<header class="top">.*?</header>'
    content = re.sub(pattern, new_header, content, flags=re.DOTALL)

    with open(src_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  Written {src_path}")

    # Recompile hub
    compile_script = os.path.join(REPO1, "scripts", "build-protected-hub.js")
    subprocess.run(["node", compile_script], check=True)

# 4. Update calculator/index.html & green/calculator/index.html
def update_calculator():
    print("Updating calculator/index.html and green/calculator/index.html...")
    targets = [
        os.path.join(REPO1, "calculator", "index.html"),
        os.path.join(REPO1, "green", "calculator", "index.html"),
        os.path.join(REPO2, "calculator", "index.html"),
        os.path.join(REPO2, "green", "calculator", "index.html")
    ]
    for path in targets:
        if not os.path.exists(path):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        new_header = f'''  <header class="sticky top-0 z-40 w-full bg-[#090B0E]/95 backdrop-blur-md border-b border-[#232834] -mx-4 sm:-mx-6 lg:-mx-8 px-4 sm:px-6 lg:px-8 transition-colors shadow-sm">
    <div class="max-w-7xl mx-auto flex flex-col gap-2 py-2.5 sm:py-3.5">
      <!-- Top Row: Brand, Desktop Nav, and Header CTAs -->
      <div class="flex items-center justify-between w-full">
        <div class="flex items-center gap-6">
          {get_brand_html()}

          <!-- Desktop Navigation -->
          {get_desktop_nav_html('calc')}
        </div>

        <!-- Right Controls -->
        <div class="flex items-center gap-1.5 sm:gap-2">
          <a href="/#marketWire" class="inline-flex items-center gap-1.5 px-2.5 sm:px-3 py-1.5 rounded-lg font-mono text-[10px] sm:text-[11px] text-white bg-[#171C26] border border-[#232834] hover:border-teal-500 transition-all shadow-sm">
            <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse shrink-0"></span>
            <span>Live Wire</span>
          </a>

          <a href="/" class="hidden sm:inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg font-mono text-[11px] text-white bg-[#171C26] border border-[#232834] hover:border-teal-500 transition-all shadow-sm">
            <svg class="w-3.5 h-3.5 text-teal-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
            </svg>
            <span>Back to Hubs</span>
          </a>

          <button id="themeToggleBtn" aria-label="Toggle Theme" class="flex items-center justify-center w-8.5 h-8.5 rounded-lg bg-[#171C26] border border-[#232834] shadow-sm hover:border-slate-400 text-slate-300 transition-all cursor-pointer">
            <svg id="sunIcon" class="hidden w-4 h-4 text-amber-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.6">
              <path stroke-linecap="round" stroke-linejoin="round" d="M12 3v2.25m6.364.386-1.591 1.591M21 12h-2.25m-.386 6.364-1.591-1.591M12 18.75V21m-4.773-4.227-1.591 1.591M5.25 12H3m4.227-4.773L5.636 5.636M15.75 12a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0Z" />
            </svg>
            <svg id="moonIcon" class="w-4 h-4 text-slate-300" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.6">
              <path stroke-linecap="round" stroke-linejoin="round" d="M21.752 15.002A9.72 9.72 0 0 1 18 15.75c-5.385 0-9.75-4.365-9.75-9.75 0-1.33.266-2.597.748-3.752A9.753 9.753 0 0 0 3 11.25C3 16.635 7.365 21 12.75 21a9.753 9.753 0 0 0 9.002-5.998Z" />
            </svg>
          </button>
        </div>
      </div>

      <!-- Mobile Touch Navigation Carousel -->
      {get_mobile_nav_html('calc')}
    </div>
  </header>'''

        pattern = r'<header class="sticky top-0.*?<!-- ==================================================================== -->'
        replacement = new_header + "\n\n    <!-- ==================================================================== -->"
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  Written {path}")

# 5. Update index.html & green/index.html
def update_index():
    print("Updating index.html and green/index.html...")
    targets = [
        os.path.join(REPO1, "index.html"),
        os.path.join(REPO1, "green", "index.html"),
        os.path.join(REPO2, "index.html"),
        os.path.join(REPO2, "green", "index.html")
    ]
    for path in targets:
        if not os.path.exists(path):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        new_header = f'''  <header class="sticky top-0 z-40 w-full bg-[#090B0E]/95 backdrop-blur-md border-b border-[#232834] -mx-4 sm:-mx-6 lg:-mx-8 px-4 sm:px-6 lg:px-8 transition-colors shadow-sm">
    <div class="max-w-7xl mx-auto flex flex-col gap-2 py-2.5 sm:py-3.5">
      <!-- Top Row: Brand, Desktop Nav, and Header CTAs -->
      <div class="flex items-center justify-between w-full">
        <div class="flex items-center gap-6">
          {get_brand_html()}

          <!-- Desktop Navigation -->
          {get_desktop_nav_html('hubs')}
        </div>

        <!-- Right Controls -->
        <div class="flex items-center gap-1.5 sm:gap-2">
          <a href="#marketWire" class="inline-flex items-center gap-1.5 px-2.5 sm:px-3 py-1.5 rounded-lg font-mono text-[10px] sm:text-[11px] text-white bg-[#171C26] border border-[#232834] hover:border-teal-500 transition-all shadow-sm">
            <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse shrink-0"></span>
            <span>Live Wire</span>
          </a>

          <a href="/calculator/" class="hidden sm:inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg font-mono text-[11px] text-white bg-[#171C26] border border-[#232834] hover:border-teal-500 transition-all shadow-sm">
            <svg class="w-3.5 h-3.5 text-teal-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
            </svg>
            <span>Power Sizer &amp; Tariffs</span>
          </a>

          <button id="themeToggleBtn" aria-label="Toggle Theme" class="flex items-center justify-center w-8.5 h-8.5 rounded-lg bg-[#171C26] border border-[#232834] shadow-sm hover:border-slate-400 text-slate-300 transition-all cursor-pointer">
            <svg id="sunIcon" class="hidden w-4 h-4 text-amber-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.6">
              <path stroke-linecap="round" stroke-linejoin="round" d="M12 3v2.25m6.364.386-1.591 1.591M21 12h-2.25m-.386 6.364-1.591-1.591M12 18.75V21m-4.773-4.227-1.591 1.591M5.25 12H3m4.227-4.773L5.636 5.636M15.75 12a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0Z" />
            </svg>
            <svg id="moonIcon" class="w-4 h-4 text-slate-300" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.6">
              <path stroke-linecap="round" stroke-linejoin="round" d="M21.752 15.002A9.72 9.72 0 0 1 18 15.75c-5.385 0-9.75-4.365-9.75-9.75 0-1.33.266-2.597.748-3.752A9.753 9.753 0 0 0 3 11.25C3 16.635 7.365 21 12.75 21a9.753 9.753 0 0 0 9.002-5.998Z" />
            </svg>
          </button>
        </div>
      </div>

      <!-- Mobile Touch Navigation Carousel -->
      {get_mobile_nav_html('hubs')}
    </div>
  </header>'''

        pattern = r'<header class="sticky top-0.*?<!-- ==================================================================== -->'
        replacement = new_header + "\n\n    <!-- ==================================================================== -->"
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  Written {path}")

def main():
    print("=== Deploying Unified Institutional Header across Portal ===")
    update_projectenergy()
    update_evcharging()
    update_hub()
    update_calculator()
    update_index()
    print("\n[SUCCESS] Unified Institutional Header applied across all portal routes!")

if __name__ == "__main__":
    main()
