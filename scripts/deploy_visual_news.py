import os
import re

REPOS = [
    "G:/My Drive/7. AI/Gemini/RenewableVietNam",
    "G:/My Drive/7. AI/Gemini/Qking232.github.io"
]

ROOT_INDEX = "G:/My Drive/7. AI/Gemini/RenewableVietNam/index.html"
with open(ROOT_INDEX, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Sector Pills Toolbar in section#marketWire
old_pills = """        <!-- Category Pills -->
        <div class="flex flex-wrap items-center gap-2 pt-2 border-t border-slate-100 dark:border-white/[0.04] text-[11px] font-mono">
          <span class="text-slate-400 dark:text-slate-500 uppercase tracking-wider text-[10px]">Sector:</span>
          <button data-news-sector="all" class="news-sector-pill px-2.5 py-1 rounded-md bg-teal-600 text-white font-medium transition-colors cursor-pointer">All Signals</button>
          <button data-news-sector="Policy & DPPA" class="news-sector-pill px-2.5 py-1 rounded-md bg-slate-100 dark:bg-darkCard text-inkPrimary dark:text-textDarkMuted hover:bg-slate-200 dark:hover:bg-darkCard/80 transition-colors cursor-pointer">Policy &amp; DPPA</button>
          <button data-news-sector="Eco-Parks & Siting" class="news-sector-pill px-2.5 py-1 rounded-md bg-slate-100 dark:bg-darkCard text-inkPrimary dark:text-textDarkMuted hover:bg-slate-200 dark:hover:bg-darkCard/80 transition-colors cursor-pointer">Eco-Parks &amp; Siting</button>
          <button data-news-sector="Solar & Wind" class="news-sector-pill px-2.5 py-1 rounded-md bg-slate-100 dark:bg-darkCard text-inkPrimary dark:text-textDarkMuted hover:bg-slate-200 dark:hover:bg-darkCard/80 transition-colors cursor-pointer">Solar &amp; Wind</button>
          <button data-news-sector="Grid & Interconnect" class="news-sector-pill px-2.5 py-1 rounded-md bg-slate-100 dark:bg-darkCard text-inkPrimary dark:text-textDarkMuted hover:bg-slate-200 dark:hover:bg-darkCard/80 transition-colors cursor-pointer">Grid &amp; Interconnect</button>
        </div>"""

new_pills = """        <!-- Category Pills -->
        <div class="flex flex-wrap items-center gap-2 pt-2 border-t border-slate-100 dark:border-white/[0.04] text-[11px] font-mono">
          <span class="text-slate-400 dark:text-slate-500 uppercase tracking-wider text-[10px]">Sector:</span>
          <button data-news-sector="all" class="news-sector-pill px-2.5 py-1 rounded-md bg-teal-600 text-white font-medium transition-colors cursor-pointer">All Signals</button>
          <button data-news-sector="Solar & Wind" class="news-sector-pill px-2.5 py-1 rounded-md bg-slate-100 dark:bg-darkCard text-inkPrimary dark:text-textDarkMuted hover:bg-slate-200 dark:hover:bg-darkCard/80 transition-colors cursor-pointer">Solar &amp; Wind</button>
          <button data-news-sector="Policy & DPPA" class="news-sector-pill px-2.5 py-1 rounded-md bg-slate-100 dark:bg-darkCard text-inkPrimary dark:text-textDarkMuted hover:bg-slate-200 dark:hover:bg-darkCard/80 transition-colors cursor-pointer">Policy &amp; DPPA</button>
          <button data-news-sector="Eco-Parks & Siting" class="news-sector-pill px-2.5 py-1 rounded-md bg-slate-100 dark:bg-darkCard text-inkPrimary dark:text-textDarkMuted hover:bg-slate-200 dark:hover:bg-darkCard/80 transition-colors cursor-pointer">Eco-Parks &amp; Siting</button>
          <button data-news-sector="Grid & Interconnect" class="news-sector-pill px-2.5 py-1 rounded-md bg-slate-100 dark:bg-darkCard text-inkPrimary dark:text-textDarkMuted hover:bg-slate-200 dark:hover:bg-darkCard/80 transition-colors cursor-pointer">Grid &amp; Interconnect</button>
          <button data-news-sector="Finance & ESG" class="news-sector-pill px-2.5 py-1 rounded-md bg-slate-100 dark:bg-darkCard text-inkPrimary dark:text-textDarkMuted hover:bg-slate-200 dark:hover:bg-darkCard/80 transition-colors cursor-pointer">Finance &amp; ESG</button>
          <button data-news-sector="FDI & Infrastructure" class="news-sector-pill px-2.5 py-1 rounded-md bg-slate-100 dark:bg-darkCard text-inkPrimary dark:text-textDarkMuted hover:bg-slate-200 dark:hover:bg-darkCard/80 transition-colors cursor-pointer">FDI &amp; Infrastructure</button>
        </div>"""

if old_pills in content:
    content = content.replace(old_pills, new_pills)
    print("Replaced category pills successfully")
else:
    print("Warning: old_pills not matched directly")

# 2. Update sectorBadgeStyles in JS
old_badge_styles = """      const sectorBadgeStyles = {
        "Policy & DPPA": "bg-amber-500/10 text-amber-600 dark:text-amber-400 border-amber-500/20",
        "Solar & Wind": "bg-teal-500/10 text-teal-600 dark:text-teal-400 border-teal-500/20",
        "Eco-Parks & Siting": "bg-indigo-500/10 text-indigo-600 dark:text-indigo-400 border-indigo-500/20",
        "Grid & Interconnect": "bg-sky-500/10 text-sky-600 dark:text-sky-400 border-sky-500/20",
        "FDI & Infrastructure": "bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border-emerald-500/20"
      };"""

new_badge_styles = """      const sectorBadgeStyles = {
        "Policy & DPPA": "bg-amber-500/10 text-amber-600 dark:text-amber-400 border-amber-500/20",
        "Solar & Wind": "bg-teal-500/10 text-teal-600 dark:text-teal-400 border-teal-500/20",
        "Eco-Parks & Siting": "bg-indigo-500/10 text-indigo-600 dark:text-indigo-400 border-indigo-500/20",
        "Grid & Interconnect": "bg-sky-500/10 text-sky-600 dark:text-sky-400 border-sky-500/20",
        "Finance & ESG": "bg-purple-500/10 text-purple-600 dark:text-purple-400 border-purple-500/20",
        "FDI & Infrastructure": "bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border-emerald-500/20"
      };

      const defaultSectorImages = {
        "Solar & Wind": "https://images.unsplash.com/photo-1509391365360-2e959784a276?auto=format&fit=crop&w=800&q=80",
        "Policy & DPPA": "https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?auto=format&fit=crop&w=800&q=80",
        "Eco-Parks & Siting": "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&w=800&q=80",
        "Grid & Interconnect": "https://images.unsplash.com/photo-1544724569-5f546fd6f2b5?auto=format&fit=crop&w=800&q=80",
        "Finance & ESG": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80",
        "FDI & Infrastructure": "https://images.unsplash.com/photo-1513836279014-a89f7a76ae86?auto=format&fit=crop&w=800&q=80"
      };"""

if old_badge_styles in content:
    content = content.replace(old_badge_styles, new_badge_styles)
    print("Replaced sectorBadgeStyles successfully")

# 3. Replace renderNewsGrid() with Visual Image Preview and Hero Spotlight Engine
old_render_start = content.find("function renderNewsGrid() {")
old_render_end = content.find("async function fetchNewsData(forceRefresh = false) {")

new_render_fn = """function renderNewsGrid() {
        const grid = document.getElementById("newsGrid");
        const countSpan = document.getElementById("filteredNewsCount");
        const expandContainer = document.getElementById("newsExpandContainer");
        const expandBtnText = document.getElementById("newsExpandBtnText");
        const expandIcon = document.getElementById("newsExpandIcon");
        if (!grid) return;

        let filtered = allNewsArticles.filter(art => {
          const matchesSector = activeNewsSector === "all" || art.sector === activeNewsSector;
          const searchNorm = newsSearchTerm.toLowerCase();
          const matchesSearch = !searchNorm ||
            (art.title && art.title.toLowerCase().includes(searchNorm)) ||
            (art.snippet && art.snippet.toLowerCase().includes(searchNorm)) ||
            (art.source && art.source.toLowerCase().includes(searchNorm)) ||
            (art.sector && art.sector.toLowerCase().includes(searchNorm));
          return matchesSector && matchesSearch;
        });

        countSpan.innerText = filtered.length;

        if (filtered.length === 0) {
          grid.innerHTML = `
            <div class="col-span-full py-12 text-center font-mono text-xs text-inkMuted dark:text-textDarkMuted bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder rounded-2xl">
              No intelligence dispatches matched your current filters.
            </div>
          `;
          expandContainer.classList.add("hidden");
          return;
        }

        const displayItems = isNewsExpanded ? filtered : filtered.slice(0, INITIAL_NEWS_LIMIT);

        // Determine if Hero Spotlight is appropriate (default overview mode)
        const isDefaultView = (activeNewsSector === "all" && !newsSearchTerm && !isNewsExpanded && displayItems.length >= 4);

        let html = "";

        if (isDefaultView) {
          const leadArt = displayItems[0];
          const remainingItems = displayItems.slice(1);
          const leadBadgeClass = sectorBadgeStyles[leadArt.sector] || "bg-teal-500/10 text-teal-600 dark:text-teal-400 border-teal-500/20";
          const fallbackImg = defaultSectorImages[leadArt.sector] || "https://images.unsplash.com/photo-1509391365360-2e959784a276?auto=format&fit=crop&w=1200&q=80";
          const leadImg = leadArt.image_url || fallbackImg;

          html += `
            <!-- FEATURED LEAD DISPATCH (HERO SPOTLIGHT) -->
            <div class="col-span-full rounded-2xl bg-white dark:bg-darkCard border border-borderSlate dark:border-darkBorder shadow-sm hover:border-teal-500/40 dark:hover:border-teal-400/30 transition-all overflow-hidden group">
              <div class="grid grid-cols-1 lg:grid-cols-12 items-stretch">
                <div class="relative lg:col-span-7 h-60 sm:h-72 lg:h-80 overflow-hidden bg-slate-100 dark:bg-darkSurface">
                  <img src="${leadImg}" alt="${leadArt.title.replace(/"/g, '&quot;')}" loading="lazy" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" onerror="this.onerror=null;this.src='${fallbackImg}';" />
                  <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-transparent to-black/20 pointer-events-none"></div>
                  <div class="absolute top-3 left-3 flex items-center gap-2">
                    <span class="font-mono text-[9px] uppercase font-bold tracking-wider px-2 py-0.5 rounded bg-emerald-500 text-white shadow-sm flex items-center gap-1.5">
                      <span class="w-1.5 h-1.5 rounded-full bg-white animate-ping"></span>
                      FEATURED LEAD DISPATCH
                    </span>
                    <span class="font-mono text-[9px] uppercase font-semibold px-2 py-0.5 rounded backdrop-blur-md bg-black/60 text-white border border-white/10 shadow-sm">
                      ${leadArt.sector}
                    </span>
                  </div>
                  <span class="absolute bottom-3 right-3 font-mono text-[10px] px-2 py-0.5 rounded bg-black/70 text-white backdrop-blur-sm">
                    ${leadArt.relative_time}
                  </span>
                </div>
                <div class="lg:col-span-5 p-5 sm:p-6 flex flex-col justify-between space-y-4">
                  <div class="space-y-2.5">
                    <div class="flex items-center gap-2 font-mono text-[11px] text-teal-600 dark:text-teal-400">
                      <span class="inline-block w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
                      <span class="font-semibold uppercase tracking-wider">${leadArt.source}</span>
                      <span class="text-slate-300 dark:text-slate-600">&middot;</span>
                      <span class="text-slate-400 font-normal">${leadArt.relative_time}</span>
                    </div>
                    <h3 class="text-base sm:text-lg lg:text-xl font-semibold leading-snug text-inkPrimary dark:text-textDarkPrimary group-hover:text-teal-600 dark:group-hover:text-teal-400 transition-colors">
                      <a href="${leadArt.link}" target="_blank" rel="noopener noreferrer">
                        ${leadArt.title}
                      </a>
                    </h3>
                    <p class="text-xs sm:text-sm text-inkMuted dark:text-textDarkMuted font-light leading-relaxed">
                      ${leadArt.snippet || "Institutional renewable market update and policy dispatch from Vietnam."}
                    </p>
                  </div>
                  <div class="pt-3 border-t border-slate-100 dark:border-white/[0.04] flex items-center justify-between">
                    <span class="font-mono text-[10px] text-slate-400 uppercase tracking-wider">Priority Intelligence Wire</span>
                    <a href="${leadArt.link}" target="_blank" rel="noopener noreferrer" class="px-3.5 py-1.5 rounded-lg bg-teal-600 hover:bg-teal-500 text-white font-mono text-xs font-medium transition-colors flex items-center gap-1.5 shadow-sm">
                      <span>Read Dispatch</span>
                      <svg class="w-3.5 h-3.5 group-hover:translate-x-0.5 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
                      </svg>
                    </a>
                  </div>
                </div>
              </div>
            </div>
          `;

          // Render remaining cards
          remainingItems.forEach(art => {
            html += renderArticleCard(art);
          });
        } else {
          // Standard Grid rendering
          displayItems.forEach(art => {
            html += renderArticleCard(art);
          });
        }

        grid.innerHTML = html;

        if (filtered.length > INITIAL_NEWS_LIMIT) {
          expandContainer.classList.remove("hidden");
          expandBtnText.innerText = isNewsExpanded ? "Show Initial 20 Articles" : `Show All Dispatches (${filtered.length})`;
          if (isNewsExpanded) {
            expandIcon.classList.add("rotate-180");
          } else {
            expandIcon.classList.remove("rotate-180");
          }
        } else {
          expandContainer.classList.add("hidden");
        }
      }

      function renderArticleCard(art) {
        const badgeClass = sectorBadgeStyles[art.sector] || "bg-slate-500/10 text-slate-600 dark:text-slate-400 border-slate-500/20";
        const fallbackImg = defaultSectorImages[art.sector] || "https://images.unsplash.com/photo-1509391365360-2e959784a276?auto=format&fit=crop&w=800&q=80";
        const cardImg = art.image_url || fallbackImg;

        return `
          <article class="rounded-2xl bg-white dark:bg-darkCard border border-borderSlate dark:border-darkBorder shadow-sm hover:shadow-md hover:border-teal-500/40 dark:hover:border-teal-400/30 transition-all flex flex-col justify-between overflow-hidden group">
            <!-- Article Preview Thumbnail -->
            <div class="relative w-full h-44 overflow-hidden bg-slate-100 dark:bg-darkSurface">
              <img src="${cardImg}" alt="${art.title.replace(/"/g, '&quot;')}" loading="lazy" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" onerror="this.onerror=null;this.src='${fallbackImg}';" />
              <div class="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-black/20 pointer-events-none"></div>
              <span class="absolute top-2.5 left-2.5 font-mono text-[9px] uppercase font-semibold px-2 py-0.5 rounded backdrop-blur-md bg-black/60 text-white border border-white/10 shadow-sm">
                ${art.sector}
              </span>
              <span class="absolute bottom-2 right-2 font-mono text-[9px] px-1.5 py-0.5 rounded bg-black/70 text-white backdrop-blur-sm">
                ${art.relative_time}
              </span>
            </div>

            <!-- Card Content -->
            <div class="p-4 space-y-2 flex-1 flex flex-col justify-between">
              <div class="space-y-1.5">
                <h3 class="text-xs sm:text-sm font-medium leading-snug text-inkPrimary dark:text-textDarkPrimary group-hover:text-teal-600 dark:group-hover:text-teal-400 transition-colors line-clamp-2">
                  <a href="${art.link}" target="_blank" rel="noopener noreferrer">
                    ${art.title}
                  </a>
                </h3>

                <p class="text-[11px] sm:text-xs text-inkMuted dark:text-textDarkMuted font-light leading-relaxed line-clamp-2">
                  ${art.snippet || "Institutional renewable market update and policy dispatch from Vietnam."}
                </p>
              </div>

              <div class="pt-3 mt-3 border-t border-slate-100 dark:border-white/[0.04] flex items-center justify-between text-[11px] font-mono">
                <span class="text-slate-400 dark:text-slate-500 truncate max-w-[140px]" title="${art.source}">
                  ${art.source}
                </span>
                <a href="${art.link}" target="_blank" rel="noopener noreferrer" class="text-teal-600 dark:text-teal-400 hover:underline flex items-center gap-1 font-medium">
                  <span>Dispatch</span>
                  <svg class="w-3 h-3 group-hover:translate-x-0.5 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
                  </svg>
                </a>
              </div>
            </div>
          </article>
        `;
      }

      """

content = content[:old_render_start] + new_render_fn + content[old_render_end:]
print("Updated renderNewsGrid function successfully!")

# Write updated index.html across all 4 locations
for repo in REPOS:
    root_p = os.path.join(repo, "index.html")
    green_p = os.path.join(repo, "green", "index.html")
    
    with open(root_p, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written: {root_p}")
    
    with open(green_p, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written: {green_p}")

print("\n[SUCCESS] Homepage visual media updates applied across all locations!")
