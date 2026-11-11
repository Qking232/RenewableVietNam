#!/usr/bin/env python3
"""
Deploy Unified Sleek 52px Glass Header Shell, Light-Default Cross-Domain Theme Cookie,
and Smooth Same-Origin Transitions across RenewableVietNam & Qking232.github.io - Rev.003.

Safety:
- Inspects highest existing index_Rev.xxx.html in each target folder first.
- Writes sequential pre-edit snapshot before updating active file.
- Does NOT touch excluded routes (evcharging/ev/index.html, hub/index.html, datacenter/index.html).
"""

import os
import re
import shutil

REPO1 = r"G:\My Drive\7. AI\RenewableVietNam"
REPO2 = r"G:\My Drive\7. AI\Qking232.github.io"

TARGETS = [
    {"rel": "index.html", "active": "cockpit", "mode": "standard", "canon": "https://renewablevietnam.com/"},
    {"rel": "energy/index.html", "active": "energy", "mode": "standard", "canon": "https://renewablevietnam.com/energy/"},
    {"rel": "projectenergy/index.html", "active": "energy", "mode": "standard", "canon": "https://renewablevietnam.com/energy/"},
    {"rel": "industrial/index.html", "active": "industrial", "mode": "standard", "canon": "https://renewablevietnam.com/industrial/"},
    {"rel": "industrial/calculator/index.html", "active": "industrial", "mode": "standard", "canon": "https://renewablevietnam.com/industrial/calculator/"},
    {"rel": "evcharging/index.html", "active": "ev", "mode": "standard", "canon": "https://renewablevietnam.com/evcharging/"},
    {"rel": "invm/index.html", "active": "legal", "mode": "standard", "canon": "https://renewablevietnam.com/invm/"},
    {"rel": "invm/quyhoach/index.html", "active": "legal", "mode": "quyhoach", "canon": "https://renewablevietnam.com/invm/quyhoach/"},
    {"rel": "project/index.html", "active": "project", "mode": "standard", "canon": "https://renewablevietnam.com/project/"},
    {"rel": "project/dc/index.html", "active": "project", "mode": "dc", "canon": None},
    {"rel": "project/garments/index.html", "active": "project", "mode": "garments", "canon": "https://renewablevietnam.com/project/garments/"},
    {"rel": "dc/index.html", "active": "project", "mode": "dc", "canon": None},
    {"rel": "garments/index.html", "active": "project", "mode": "garments", "canon": "https://renewablevietnam.com/garments/"},
    {"rel": "livewire/index.html", "active": "cockpit", "mode": "standard", "canon": "https://renewablevietnam.com/livewire/"},
    {"rel": "roadmap/index.html", "active": "roadmap", "mode": "standard", "canon": "https://renewablevietnam.com/roadmap/"},
    {"rel": "calculator/index.html", "active": "industrial", "mode": "standard", "canon": "https://renewablevietnam.com/calculator/", "repo2_only": True},
]

PREPAINT_AND_CSS = """  <script id="rvn-prepaint-theme">
    (function () {
      try {
        var m = document.cookie.match(/(?:^|;\\s*)rvn_theme=(dark|light)/);
        var t = m ? m[1] : localStorage.getItem('rvn_theme_v2');
        document.documentElement.classList.toggle('dark', t === 'dark');
      } catch (e) {}
    })();
  </script>
  <link rel="stylesheet" href="/assets/built/rvn-shell.css?v=2" />"""

HEAD_THEME_PATTERNS = [
    re.compile(r'<script id="rvn-prepaint-theme">[\s\S]*?</script>\s*', re.IGNORECASE),
    re.compile(r'<link[^>]+href="/assets/built/rvn-shell\.css[^"]*"[^>]*/?>\s*', re.IGNORECASE),
    re.compile(r'<!--\s*Theme Initialization\s*-->\s*<script>[\s\S]*?rvn-theme[\s\S]*?</script>\s*', re.IGNORECASE),
    re.compile(r'<script>\s*(?://[^\n]*\n\s*)?\(function\s*\(\)\s*\{[\s\S]*?(?:rvn_theme_v2|rvn-theme)[\s\S]*?\}\)\(\);\s*</script>\s*', re.IGNORECASE),
    re.compile(r'<script>\s*const savedTheme\s*=\s*localStorage\.getItem\([\'"]rvn-theme[\'"]\);[\s\S]*?</script>\s*', re.IGNORECASE),
]

HEAD_REDIRECT_PATTERNS = [
    re.compile(r'<script>\s*(?://[^\n]*\n\s*)?if\s*\(\s*window\.location\.hostname[\s\S]*?window\.location\.replace\([\s\S]*?</script>\s*', re.IGNORECASE),
    re.compile(r'<script>\s*(?://[^\n]*\n\s*)?\(function\(\)\s*\{\s*if\s*\(\s*window\.location\.hostname[\s\S]*?window\.location\.replace\([\s\S]*?</script>\s*', re.IGNORECASE),
]


def next_rev_path(full_path):
    d = os.path.dirname(full_path)
    max_rev = 0
    for fn in os.listdir(d):
        m = re.match(r'^index_Rev\.(\d+)\.html$', fn)
        if m:
            val = int(m.group(1))
            if val > max_rev:
                max_rev = val
    return os.path.join(d, f"index_Rev.{max_rev + 1:03d}.html")


def normalize_tailwind_order(head):
    cfg_re = re.compile(r'<script>\s*tailwind\.config\s*=[\s\S]*?</script>', re.IGNORECASE)
    cdn_re = re.compile(r'<script[^>]+src="https://cdn\.tailwindcss\.com"[^>]*>\s*</script>', re.IGNORECASE)
    cdn_m = cdn_re.search(head)
    cfg_m = cfg_re.search(head)
    if cdn_m and cfg_m and cfg_m.start() < cdn_m.start():
        cfg_tag = cfg_m.group(0)
        head = head[:cfg_m.start()] + head[cfg_m.end():]
        cdn_m = cdn_re.search(head)
        head = head[:cdn_m.end()] + "\n  " + cfg_tag + head[cdn_m.end():]
    elif cdn_m and not cfg_m:
        ins = "\n  <script>\n    tailwind.config = { darkMode: 'class', theme: { extend: {} } };\n  </script>"
        head = head[:cdn_m.end()] + ins + head[cdn_m.end():]
    return head


def replace_urls_for_same_origin(text):
    mapping = {
        "https://invest.renewablevietnam.com/": "https://renewablevietnam.com/invm/",
        "https://invest.renewablevietnam.com": "https://renewablevietnam.com/invm",
        "https://legal.renewablevietnam.com/quyhoach/": "https://renewablevietnam.com/invm/quyhoach/",
        "https://legal.renewablevietnam.com/": "https://renewablevietnam.com/invm/",
        "https://legal.renewablevietnam.com": "https://renewablevietnam.com/invm",
        "https://ev.renewablevietnam.com/": "https://renewablevietnam.com/evcharging/",
        "https://ev.renewablevietnam.com": "https://renewablevietnam.com/evcharging",
        "https://ind.renewablevietnam.com/": "https://renewablevietnam.com/industrial/",
        "https://ind.renewablevietnam.com": "https://renewablevietnam.com/industrial",
        "https://energy.renewablevietnam.com/": "https://renewablevietnam.com/energy/",
        "https://energy.renewablevietnam.com": "https://renewablevietnam.com/energy",
        "https://industrial.renewablevietnam.com/": "https://renewablevietnam.com/industrial/",
        "https://industrial.renewablevietnam.com": "https://renewablevietnam.com/industrial",
        "https://project.renewablevietnam.com/garments/": "https://renewablevietnam.com/garments/",
        "https://project.renewablevietnam.com/": "https://renewablevietnam.com/project/",
        "https://project.renewablevietnam.com": "https://renewablevietnam.com/project",
    }
    for old, new in mapping.items():
        text = text.replace(old, new)
    return text


def transform_dc_header(header_html):
    sec = re.sub(r'^<header\b[^>]*>', '<section class="bg-white border-b border-slate-200 shadow-2xs">', header_html.strip())
    sec = re.sub(r'</header>$', '</section>', sec)
    sec = sec.replace("https://invest.renewablevietnam.com/", "https://renewablevietnam.com/invm/")
    return f'<header id="rvn-header" data-active="project"></header>\n  <script src="/assets/js/rvn-header.js?v=2"></script>\n  {sec}'


def transform_garments_header(header_html):
    m_grid = re.search(r'(<!--\s*Executive 7-Segment Grid Navigation[\s\S]*?)<!--\s*Active Viewport Toolbar', header_html)
    m_toolbar = re.search(r'(<!--\s*Active Viewport Toolbar[\s\S]*?)</header>', header_html)
    if not (m_grid and m_toolbar):
        raise RuntimeError("Unexpected garments header structure")
    sub_strip = """  <div class="w-full max-w-[1920px] 2xl:max-w-full mx-auto px-4 sm:px-6 lg:px-8 xl:px-12 py-2 flex items-center justify-between gap-2">
      <div class="flex items-center gap-2 min-w-0">
        <span class="text-[11px] font-mono uppercase tracking-wider text-slate-700 dark:text-slate-200 font-semibold truncate">Garments Capital Projects</span>
        <span class="hidden sm:inline-flex items-center gap-1.5 px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800 border border-slate-200/60 dark:border-slate-700/50 font-mono text-[10px] text-slate-600 dark:text-slate-400">
          <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
          <span>$14.50M BAC &middot; Multi-Site</span>
        </span>
      </div>
      <a href="https://renewablevietnam.com/project/" class="inline-flex items-center gap-1 px-2.5 py-1 rounded-md bg-sky-50 dark:bg-sky-950/40 border border-sky-200 dark:border-sky-800 text-sky-700 dark:text-sky-300 hover:bg-sky-100 text-[11px] font-semibold transition-colors shadow-2xs shrink-0">&larr; Projects Home</a>
    </div>"""
    sec = f"""<header id="rvn-header" data-active="project"></header>
  <script src="/assets/js/rvn-header.js?v=2"></script>
  <section class="bg-white/95 dark:bg-slate-900/95 border-b border-slate-200/80 dark:border-slate-800 shadow-xs">
  {sub_strip}
    {m_grid.group(1).strip()}
    {m_toolbar.group(1).strip()}
  </section>"""
    return sec


def transform_quyhoach_header(header_html):
    sec = re.sub(r'^<header\b[^>]*>', '<section class="bg-white border-b border-slate-200 shadow-xs">', header_html.strip())
    sec = re.sub(r'</header>$', '</section>', sec)
    return f'<header id="rvn-header" data-active="legal"></header>\n  <script src="/assets/js/rvn-header.js?v=2"></script>\n  {sec}'


def patch_body_scripts(rel, text):
    if rel == "index.html":
        pat = re.compile(
            r"// Theme Switcher Logic\s*\n\s*function applyTheme\(isDark\) \{[\s\S]*?themeBtn\?\.addEventListener\('click',\s*\(\)\s*=>\s*\{[\s\S]*?\}\);",
            re.MULTILINE
        )
        repl = """// Theme Switcher Listener (managed by /assets/js/rvn-header.js)
    window.addEventListener('rvn:themechange', (e) => {
      safeInitCharts();
      if (window.syncThemeToThree) window.syncThemeToThree(!!(e && e.detail && e.detail.isDark));
    });"""
        text, n = pat.subn(repl, text, count=1)
        assert n == 1, "index.html theme block not matched"

        t_pat = re.compile(r"\(function init3DSupergridMatrix\(\) \{([\s\S]*?window\.syncThemeToThree = function\(isDark\) \{[\s\S]*?\};\s*)\}\)\(\);")
        if t_pat.search(text):
            def _wrap_home_three(m):
                return f"""function init3DSupergridMatrix() {{{m.group(1)}}}
    if (document.readyState === 'loading') {{
      document.addEventListener('DOMContentLoaded', init3DSupergridMatrix);
    }} else {{
      init3DSupergridMatrix();
    }}"""
            text, n2 = t_pat.subn(_wrap_home_three, text, count=1)
            assert n2 == 1, "index.html Three.js block not matched"

        text = re.sub(
            r"    const themeBtn = document\.getElementById\('themeToggleBtn'\);\s*\n    const sunIcon = document\.getElementById\('sunIcon'\);\s*\n    const moonIcon = document\.getElementById\('moonIcon'\);\s*\n",
            "",
            text
        )

    elif rel in ("energy/index.html", "projectenergy/index.html"):
        pat = re.compile(
            r"//\s*1\.\s*Theme toggle handling\s*\n\s*const themeBtn = document\.getElementById\(\"themeToggleBtn\"\);[\s\S]*?if\s*\(themeBtn\)\s*\{\s*\n\s*themeBtn\.addEventListener\(\"click\",\s*\(\)\s*=>\s*\{[\s\S]*?updateIcons\(\);\s*\n\s*\}\);\s*\n\s*\}",
            re.MULTILINE
        )
        repl = """// 1. Theme Sync Listener (managed by /assets/js/rvn-header.js)
    window.addEventListener("rvn:themechange", () => {
      if (typeof initEnergyCharts === "function") initEnergyCharts();
    });"""
        text, n = pat.subn(repl, text, count=1)
        assert n == 1, f"{rel} theme block not matched"

    elif rel == "evcharging/index.html":
        pat = re.compile(
            r"//\s*Theme toggle handling\s*\n\s*const themeBtn = document\.getElementById\(\"themeToggleBtn\"\);[\s\S]*?if\s*\(themeBtn\)\s*\{\s*\n\s*themeBtn\.addEventListener\(\"click\",\s*\(\)\s*=>\s*\{[\s\S]*?updateIcons\(\);\s*\n\s*\}\);\s*\n\s*\}",
            re.MULTILINE
        )
        repl = """// Theme Sync Listener (managed by /assets/js/rvn-header.js)
    window.addEventListener("rvn:themechange", () => {
      if (typeof initEvTelemetryCharts === "function") initEvTelemetryCharts();
    });"""
        text, n = pat.subn(repl, text, count=1)
        assert n == 1, "evcharging/index.html theme block not matched"

    elif rel == "industrial/index.html":
        pat = re.compile(
            r"//[^\n]*Theme Controller[^\n]*\n\s*\(function initThemeController\(\)\s*\{[\s\S]*?\}\)\(\);",
            re.MULTILINE
        )
        repl = """// 1. Theme Sync Listener (state & icons managed by /assets/js/rvn-header.js)
    window.addEventListener("rvn:themechange", () => {
      if (typeof initIndustrialCharts === "function") initIndustrialCharts();
    });"""
        text, n = pat.subn(repl, text, count=1)
        assert n == 1, "industrial/index.html theme block not matched"

    elif rel in ("industrial/calculator/index.html", "calculator/index.html"):
        pat = re.compile(
            r"\s*// Theme toggle handler\s*\n\s*const themeToggleBtn = document\.getElementById\('themeToggleBtn'\);[\s\S]*?themeToggleBtn\.addEventListener\('click',\s*\(\)\s*=>\s*\{[\s\S]*?updateIcons\(isDark\);\s*\n\s*\}\);",
            re.MULTILINE
        )
        text, n = pat.subn("", text, count=1)
        assert n == 1, f"{rel} theme block not matched"

    elif rel == "invm/index.html":
        pat = re.compile(
            r"<script>\s*\(function\(\)\s*\{\s*const themeBtn = document\.getElementById\('themeToggleBtn'\);[\s\S]*?\}\)\(\);\s*</script>",
            re.MULTILINE
        )
        repl = """<script>
  window.addEventListener('rvn:themechange', function() {
    if (typeof renderTable === 'function') renderTable();
    const ganttModalEl = document.getElementById('ganttModal');
    if (ganttModalEl && !ganttModalEl.classList.contains('hidden') && typeof renderGanttView === 'function') {
      renderGanttView();
    }
  });
</script>"""
        text, n = pat.subn(repl, text, count=1)
        assert n == 1, "invm/index.html theme block not matched"

    elif rel == "project/index.html":
        pat = re.compile(
            r"// Theme Toggle Controller\s*\n\s*const themeBtn = document\.getElementById\('themeToggleBtn'\);[\s\S]*?themeBtn\.addEventListener\('click',\s*\(\)\s*=>\s*\{[\s\S]*?applyTheme\(isDark\);\s*\n\s*\}\);",
            re.MULTILINE
        )
        if pat.search(text):
            repl = """// Theme Change Sync (managed by /assets/js/rvn-header.js)
    window.addEventListener('rvn:themechange', (e) => {
      if (window.syncThemeToThree) {
        window.syncThemeToThree(!!(e && e.detail && e.detail.isDark));
      }
    });"""
            text, n = pat.subn(repl, text, count=1)
            assert n == 1, "project/index.html theme block not matched"

        t_pat = re.compile(r"\(function init3DParticleMatrix\(\) \{([\s\S]*?window\.syncThemeToThree = function\(isDark\) \{[\s\S]*?\};\s*)\}\)\(\);")
        if t_pat.search(text):
            def _wrap_proj_three(m):
                return f"""function init3DParticleMatrix() {{{m.group(1)}}}
    if (document.readyState === 'loading') {{
      document.addEventListener('DOMContentLoaded', init3DParticleMatrix);
    }} else {{
      init3DParticleMatrix();
    }}"""
            text, n2 = t_pat.subn(_wrap_proj_three, text, count=1)
            assert n2 == 1, "project/index.html Three.js block not matched"

    elif rel in ("project/garments/index.html", "garments/index.html"):
        pat = re.compile(
            r"// Theme Toggle Support\s*\n\s*const themeBtn = document\.getElementById\('themeToggleBtn'\);[\s\S]*?themeBtn\.addEventListener\('click',\s*\(\)\s*=>\s*\{[\s\S]*?applyTheme\(isDark\);\s*\n\s*\}\);",
            re.MULTILINE
        )
        text, n = pat.subn("// Theme managed by /assets/js/rvn-header.js", text, count=1)
        assert n == 1, f"{rel} theme block not matched"

    elif rel == "livewire/index.html":
        pat = re.compile(
            r"// 1\. Theme Switcher Logic\s*\n\s*const themeToggleBtn = document\.getElementById\(\"themeToggleBtn\"\);[\s\S]*?if \(themeToggleBtn\)\s*\{\s*\n\s*themeToggleBtn\.addEventListener\(\"click\",\s*\(\)\s*=>\s*\{[\s\S]*?updateThemeIcons\(\);\s*\n\s*\}\);\s*\n\s*\}",
            re.MULTILINE
        )
        text, n = pat.subn("// 1. Theme Switcher managed by /assets/js/rvn-header.js", text, count=1)
        assert n == 1, "livewire/index.html theme block not matched"

    elif rel == "roadmap/index.html":
        pat = re.compile(
            r"// Theme Toggle Controller\s*\n\s*\(function initTheme\(\)\s*\{[\s\S]*?\}\)\(\);",
            re.MULTILINE
        )
        text, n = pat.subn("// Theme Toggle managed by /assets/js/rvn-header.js", text, count=1)
        assert n == 1, "roadmap/index.html theme block not matched"

    return text


def patch_sticky_and_layout(rel, text):
    if rel == "index.html":
        text = text.replace("sticky top-14 sm:top-16 z-30", "sticky top-[52px] z-30")
    elif rel in ("energy/index.html", "projectenergy/index.html", "industrial/index.html", "evcharging/index.html"):
        text = text.replace("sticky top-16 z-30", "sticky top-[52px] z-30")
    elif rel == "invm/index.html":
        text = text.replace("sticky top-[57px] md:top-[61px] z-40", "sticky top-[52px] z-40")
    elif rel == "industrial/calculator/index.html":
        text = text.replace('class="min-h-screen text-inkPrimary dark:text-textDarkPrimary antialiased bg-alabaster dark:bg-obsidian font-sans selection:bg-teal-500 selection:text-white dark:selection:bg-teal-400 dark:selection:text-obsidian transition-colors duration-500 flex flex-col justify-between p-4 sm:p-6 lg:p-8"',
                            'class="min-h-screen text-inkPrimary dark:text-textDarkPrimary antialiased bg-alabaster dark:bg-obsidian font-sans selection:bg-teal-500 selection:text-white dark:selection:bg-teal-400 dark:selection:text-obsidian transition-colors duration-500 flex flex-col justify-between"')
        text = text.replace('<main class="relative z-10 flex-1 w-full max-w-6xl mx-auto py-6 sm:py-8 space-y-6">',
                            '<main class="relative z-10 flex-1 w-full max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-6 sm:py-8 space-y-6">')
    elif rel == "calculator/index.html":
        text = text.replace('<main class="relative z-10 flex-1 w-full max-w-6xl mx-auto py-6 sm:py-8 space-y-6">',
                            '<main class="relative z-10 flex-1 w-full max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-6 sm:py-8 space-y-6">')
    return text


def transform_content(rel, orig):
    head_end = orig.find("</head>")
    if head_end == -1:
        raise RuntimeError(f"Missing </head> in {rel}")
    before_head_end = orig[:head_end]
    after_head_end = orig[head_end:]

    hdr_re = re.compile(r'<header\b[\s\S]*?</header>', re.IGNORECASE)
    hdr_m = hdr_re.search(after_head_end)
    if not hdr_m:
        return None  # Redirect stub without header

    before_head_end = re.sub(r'(<html\b[^>]*class="[^"]*)\bdark\s*', r'\1', before_head_end, count=1)

    before_head_end = before_head_end.replace(
        'substations."s 960+ utility-scale clean generation facilities: Solar, Wind, Hydro, Biomass, and LNG with direct DPPA corridors and grid capacity on high-resolution satellite cartography."',
        'substations and 960+ utility-scale solar, wind, hydro, biomass, and LNG assets."'
    )
    before_head_end = before_head_end.replace(
        'capacity."s 22,055+ electric vehicle charging ports and stations (VinFast, EV ONE, Charge+, Autel) with direct satellite cartography and route navigation."',
        'capacity across 22,055+ EV charging ports (VinFast, EV ONE, Charge+, Autel)."'
    )

    for pat in HEAD_REDIRECT_PATTERNS + HEAD_THEME_PATTERNS:
        before_head_end = pat.sub("", before_head_end)

    return before_head_end, after_head_end, hdr_m


def process_file(repo_path, cfg, dry_run=False):
    rel = cfg["rel"]
    full_path = os.path.join(repo_path, rel)
    if not os.path.exists(full_path):
        print(f"  [SKIP] missing {rel}")
        return False

    orig = open(full_path, "r", encoding="utf-8").read()
    parsed = transform_content(rel, orig)
    if parsed is None:
        print(f"  [SKIP] redirect stub (no <header>): {rel}")
        return False

    before_head_end, after_head_end, hdr_m = parsed

    if cfg.get("canon"):
        before_head_end = re.sub(
            r'(<link\s+rel="canonical"\s+href=")[^"]+(")',
            r'\g<1>' + cfg["canon"] + r'\g<2>',
            before_head_end
        )
        before_head_end = re.sub(
            r'(<meta\s+property="og:url"\s+content=")[^"]+(")',
            r'\g<1>' + cfg["canon"] + r'\g<2>',
            before_head_end
        )
        before_head_end = re.sub(
            r'(<meta\s+name="twitter:url"\s+content=")[^"]+(")',
            r'\g<1>' + cfg["canon"] + r'\g<2>',
            before_head_end
        )

    before_head_end = before_head_end.replace(
        '<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>',
        '<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js" defer></script>'
    )
    before_head_end = before_head_end.replace(
        '<script src="https://unpkg.com/lucide@latest"></script>',
        '<script src="https://unpkg.com/lucide@latest" defer></script>'
    )

    before_head_end = normalize_tailwind_order(before_head_end)

    vp_m = re.search(r'<meta\s+name="viewport"[^>]*>\s*', before_head_end, re.IGNORECASE)
    assert vp_m, f"Missing viewport meta in {rel}"
    before_head_end = before_head_end[:vp_m.end()] + PREPAINT_AND_CSS + "\n" + before_head_end[vp_m.end():]

    old_hdr = hdr_m.group(0)
    mode = cfg["mode"]
    if mode == "standard" and "Executive 7-Segment Grid Navigation" in old_hdr:
        # Handle Qking232.github.io older project/index.html containing Garments module toolbar inside <header>
        new_hdr = transform_garments_header(old_hdr)
    elif mode == "standard":
        new_hdr = f'<header id="rvn-header" data-active="{cfg["active"]}"></header>\n  <script src="/assets/js/rvn-header.js?v=2"></script>'
    elif mode == "dc":
        new_hdr = transform_dc_header(old_hdr)
    elif mode == "garments":
        new_hdr = transform_garments_header(old_hdr)
    elif mode == "quyhoach":
        new_hdr = transform_quyhoach_header(old_hdr)
    else:
        raise RuntimeError(f"Unknown mode {mode}")

    after_head_end = after_head_end[:hdr_m.start()] + new_hdr + after_head_end[hdr_m.end():]

    after_head_end = replace_urls_for_same_origin(after_head_end)
    after_head_end = patch_sticky_and_layout(rel, after_head_end)
    after_head_end = patch_body_scripts(rel, after_head_end)

    updated = before_head_end + after_head_end

    if dry_run:
        delta = len(updated) - len(orig)
        print(f"  [DRY-OK] {rel:34} delta={delta:+6d} bytes (orig={len(orig)})")
        return True

    rev_path = next_rev_path(full_path)
    shutil.copyfile(full_path, rev_path)
    with open(full_path, "w", encoding="utf-8", newline="\n") as fp:
        fp.write(updated)
    print(f"  [OK] {rel:34} (backup -> {os.path.basename(rev_path)})")
    return True


def sync_shared_shell_to_repo2():
    os.makedirs(os.path.join(REPO2, "assets", "built"), exist_ok=True)
    os.makedirs(os.path.join(REPO2, "assets", "js"), exist_ok=True)
    files_to_copy = [
        ("assets/built/rvn-shell.css", "assets/built/rvn-shell.css"),
        ("assets/built/rvn-shell_Rev.001.css", "assets/built/rvn-shell_Rev.001.css"),
        ("assets/built/rvn-shell_Rev.002.css", "assets/built/rvn-shell_Rev.002.css"),
        ("assets/js/rvn-header.js", "assets/js/rvn-header.js"),
        ("assets/js/rvn-header_Rev.001.js", "assets/js/rvn-header_Rev.001.js"),
        ("assets/js/rvn-header_Rev.002.js", "assets/js/rvn-header_Rev.002.js"),
    ]
    for src_rel, dst_rel in files_to_copy:
        shutil.copyfile(os.path.join(REPO1, src_rel), os.path.join(REPO2, dst_rel))
    print("[SYNC] Copied shared shell CSS & JS into Qking232.github.io")


def main():
    import sys
    dry_run = "--dry-run" in sys.argv
    if not dry_run:
        sync_shared_shell_to_repo2()
    for rname, rpath in [("RenewableVietNam", REPO1), ("Qking232.github.io", REPO2)]:
        print(f"\n=== Deploying Sleek Shell to {rname}{' (DRY RUN)' if dry_run else ''} ===")
        for cfg in TARGETS:
            if cfg.get("repo2_only") and rpath == REPO1:
                continue
            process_file(rpath, cfg, dry_run=dry_run)


if __name__ == "__main__":
    main()
