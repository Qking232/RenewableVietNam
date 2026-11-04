import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# -------------------------------------------------------------
# 1. Update project/index.html (Sequential Rev: index_Rev.010.html)
# -------------------------------------------------------------
project_dir = os.path.join(BASE_DIR, "project")
project_index = os.path.join(project_dir, "index.html")
project_rev010 = os.path.join(project_dir, "index_Rev.010.html")

with open(project_index, "r", encoding="utf-8") as f:
    project_html = f.read()

# Add Project Delivery to header desktop and mobile nav if not present
if "project.renewablevietnam.com" not in project_html[project_html.find('<nav class="hidden md:flex'):project_html.find('</nav>')]:
    project_html = project_html.replace(
        '<a href="https://invest.renewablevietnam.com/" class="px-2.5 py-1 rounded-md hover:text-slate-900 dark:hover:text-slate-100 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors">Invest &amp; Legal</a></nav>',
        '<a href="https://invest.renewablevietnam.com/" class="px-2.5 py-1 rounded-md hover:text-slate-900 dark:hover:text-slate-100 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors">Invest &amp; Legal</a>\n'
        '          <span class="text-slate-300 dark:text-slate-700">&middot;</span>\n'
        '          <a href="https://project.renewablevietnam.com/" class="px-2.5 py-1 rounded-md text-teal-700 dark:text-teal-300 font-semibold bg-slate-100 dark:bg-slate-800 transition-colors">Project Delivery</a></nav>'
    )

if 'href="https://project.renewablevietnam.com/"' not in project_html[project_html.find('<!-- Mobile Quick Navigation Ribbon -->'):project_html.find('</header>')]:
    project_html = project_html.replace(
        '<a href="https://invest.renewablevietnam.com/" class="px-2.5 py-1 rounded-md text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200 bg-slate-50 dark:bg-slate-800/50 border border-slate-200/60 dark:border-slate-700/50 shrink-0">Invest &amp; Legal</a></div>',
        '<a href="https://invest.renewablevietnam.com/" class="px-2.5 py-1 rounded-md text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200 bg-slate-50 dark:bg-slate-800/50 border border-slate-200/60 dark:border-slate-700/50 shrink-0">Invest &amp; Legal</a>\n'
        '      <a href="https://project.renewablevietnam.com/" class="px-2.5 py-1 rounded-md text-teal-700 dark:text-teal-300 font-semibold bg-slate-100 dark:bg-slate-800 border border-teal-500/20 shrink-0">Project Delivery</a></div>'
    )

# Inject the 7-segment navigation bar and active module status bar before </header>
nav_block = """    <!-- Executive 7-Segment Grid Navigation -->
    <div class="w-full max-w-[1920px] 2xl:max-w-full mx-auto px-4 sm:px-6 lg:px-8 xl:px-12 border-t border-slate-100 dark:border-slate-800/80 py-2.5">
      <nav id="module-nav-bar" class="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-7 gap-2">
        <!-- Rendered dynamically -->
      </nav>
    </div>

    <!-- Active Viewport Toolbar -->
    <div class="bg-slate-50/80 dark:bg-slate-900/60 border-t border-slate-200/80 dark:border-slate-800 px-4 sm:px-6 lg:px-8 xl:px-12 py-2 text-xs">
      <div class="w-full max-w-[1920px] 2xl:max-w-full mx-auto flex flex-col sm:flex-row sm:items-center justify-between gap-1.5 sm:gap-2 text-slate-600 dark:text-slate-400">
        <div class="flex items-center gap-2 min-w-0">
          <span class="w-2 h-2 rounded-full bg-sky-500 shrink-0"></span>
          <span class="text-slate-400 dark:text-slate-500 uppercase font-semibold text-[9.5px] sm:text-[10px] shrink-0">Active Module:</span>
          <strong id="active-module-title" class="text-slate-900 dark:text-slate-100 font-bold text-xs truncate">Loading...</strong>
        </div>
        <a id="open-standalone-link" href="#" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-sky-700 dark:text-sky-300 font-medium hover:bg-sky-50 dark:hover:bg-slate-700 transition-colors shadow-2xs text-[11px] shrink-0 self-end sm:self-auto">
          <span>Open Module in New Window</span>
          <span class="text-[11px]">&nearr;</span>
        </a>
      </div>
    </div>
  </header>"""

if 'id="module-nav-bar"' not in project_html:
    project_html = project_html.replace('  </header>', nav_block, 1)

# Ensure main container is wide enough for modules
project_html = project_html.replace(
    '<main class="flex-1 max-w-7xl w-full mx-auto px-1 py-1.5 sm:px-4 sm:py-4">',
    '<main class="flex-1 w-full max-w-[1920px] 2xl:max-w-full mx-auto px-2 py-2 sm:px-6 sm:py-4">'
)

# Write sequential revision and update active file
with open(project_rev010, "w", encoding="utf-8") as f:
    f.write(project_html)
with open(project_index, "w", encoding="utf-8") as f:
    f.write(project_html)
print(f"Created {project_rev010} and updated active {project_index}")

# -------------------------------------------------------------
# 2. Update index.html (Sequential Rev: index_Rev.032.html)
# -------------------------------------------------------------
root_index = os.path.join(BASE_DIR, "index.html")
root_rev032 = os.path.join(BASE_DIR, "index_Rev.032.html")

with open(root_index, "r", encoding="utf-8") as f:
    root_html = f.read()

# Desktop header link
if "project.renewablevietnam.com" not in root_html[root_html.find('<nav class="hidden md:flex'):root_html.find('</nav>')]:
    root_html = root_html.replace(
        '<a href="https://invest.renewablevietnam.com/" class="px-2.5 py-1 rounded-md hover:text-slate-900 dark:hover:text-slate-100 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors">Invest &amp; Legal</a></nav>',
        '<a href="https://invest.renewablevietnam.com/" class="px-2.5 py-1 rounded-md hover:text-slate-900 dark:hover:text-slate-100 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors">Invest &amp; Legal</a>\n'
        '          <span class="text-slate-300 dark:text-slate-700">&middot;</span>\n'
        '          <a href="https://project.renewablevietnam.com/" class="px-2.5 py-1 rounded-md hover:text-slate-900 dark:hover:text-slate-100 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors">Project Delivery</a></nav>'
    )

# Mobile ribbon link
if 'href="https://project.renewablevietnam.com/"' not in root_html[root_html.find('<!-- Mobile Quick Navigation Ribbon -->'):root_html.find('</header>')]:
    root_html = root_html.replace(
        '<a href="https://invest.renewablevietnam.com/" class="px-2.5 py-1 rounded-md text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200 bg-slate-50 dark:bg-slate-800/50 border border-slate-200/60 dark:border-slate-700/50 shrink-0">Invest &amp; Legal</a></div>',
        '<a href="https://invest.renewablevietnam.com/" class="px-2.5 py-1 rounded-md text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200 bg-slate-50 dark:bg-slate-800/50 border border-slate-200/60 dark:border-slate-700/50 shrink-0">Invest &amp; Legal</a>\n'
        '      <a href="https://project.renewablevietnam.com/" class="px-2.5 py-1 rounded-md text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200 bg-slate-50 dark:bg-slate-800/50 border border-slate-200/60 dark:border-slate-700/50 shrink-0">Project Delivery</a></div>'
    )

# Section title: 5 Live Operational Portals
root_html = root_html.replace(
    'Dedicated Edge Infrastructure Gateways &middot; 4 Core Portals',
    'Dedicated Edge Infrastructure Gateways &middot; 5 Live Operational Portals'
)

# Expand grid from lg:grid-cols-4 to lg:grid-cols-3 xl:grid-cols-5
root_html = root_html.replace(
    '<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">',
    '<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-3">'
)

gateway_5_card = """        <!-- Gateway 5: Project Delivery -->
        <a href="https://project.renewablevietnam.com/" class="group flex flex-col justify-between p-4 rounded-xl bg-white dark:bg-slate-800/90 border border-slate-200/70 dark:border-slate-700/60 hover:border-purple-500/50 dark:hover:border-purple-400/50 shadow-xs hover:shadow-md transition-all">
          <div class="space-y-2">
            <div class="flex items-center justify-between">
              <span class="font-mono text-[9px] font-semibold uppercase tracking-wider px-2 py-0.5 rounded bg-purple-50 dark:bg-purple-950/40 text-purple-700 dark:text-purple-300 border border-purple-200/60 dark:border-purple-800/40">
                EPC Execution
              </span>
              <span class="font-mono text-[10px] text-slate-400 group-hover:text-purple-600 dark:group-hover:text-purple-400 transition-colors">&rarr;</span>
            </div>
            <div>
              <div class="text-sm font-bold text-slate-900 dark:text-slate-100 group-hover:text-purple-600 dark:group-hover:text-purple-400 transition-colors">
                Project Delivery &amp; EPC
              </div>
              <div class="font-mono text-[10px] text-slate-500 dark:text-slate-400 mt-0.5">
                project.renewablevietnam.com
              </div>
            </div>
            <p class="text-xs text-slate-600 dark:text-slate-400 leading-relaxed">
              7-domain engineering suite: Civil, 180 km/h PEB steel superstructures, MEP rough-in, HSE &amp; commissioning.
            </p>
          </div>
          <div class="mt-3 pt-3 border-t border-slate-100 dark:border-slate-700/50 flex items-center justify-between font-mono text-[10px] text-slate-500 dark:text-slate-400">
            <span>Engineering Suite</span>
            <strong class="font-semibold text-slate-800 dark:text-slate-200">7 Domains</strong>
          </div>
        </a>"""

if "Gateway 5: Project Delivery" not in root_html:
    # Insert right after Gateway 4 card closing tag
    target_needle = '<!-- Gateway 4: Invest & Legal -->'
    g4_idx = root_html.find(target_needle)
    if g4_idx != -1:
        # find closing </a> of Gateway 4
        g4_end = root_html.find('</a>', g4_idx) + 4
        root_html = root_html[:g4_end] + "\n\n" + gateway_5_card + root_html[g4_end:]

# Write sequential revision and update active file
with open(root_rev032, "w", encoding="utf-8") as f:
    f.write(root_html)
with open(root_index, "w", encoding="utf-8") as f:
    f.write(root_html)
print(f"Created {root_rev032} and updated active {root_index}")
