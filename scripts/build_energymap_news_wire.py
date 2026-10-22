"""
Script to build and deploy the Multi-Source News Aggregation Wire & Industrial Zone UI Feed
into Renewable Vietnam's Energy Map (/projectenergy/ and /energymap/).
"""
import os
import json
import re

REPO1 = "G:/My Drive/7. AI/Gemini/RenewableVietNam"
REPO2 = "G:/My Drive/7. AI/Gemini/Qking232.github.io"

# 1. Enrich data/industry_news.json
def enrich_news_data():
    news_path = os.path.join(REPO1, "data", "industry_news.json")
    with open(news_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    provinces_map = {
        "Bình Dương": ["bình dương", "binh duong"],
        "Quảng Ninh": ["quảng ninh", "quang ninh"],
        "Bà Rịa - Vũng Tàu": ["bà rịa", "ba ria", "vũng tàu", "vung tau"],
        "Bắc Ninh": ["bắc ninh", "bac ninh"],
        "Hải Phòng": ["hải phòng", "hai phong"],
        "Đồng Nai": ["đồng nai", "dong nai"],
        "Ninh Thuận": ["ninh thuận", "ninh thuan"],
        "Bình Thuận": ["bình thuận", "binh thuan"],
        "Hà Nội": ["hà nội", "hanoi"],
        "TP. Hồ Chí Minh": ["hồ chí minh", "tp.hcm", "hcmc", "ho chi minh"],
        "Cần Thơ": ["cần thơ", "can tho"],
        "Đà Nẵng": ["đà nẵng", "da nang"],
        "Long An": ["long an"],
        "Gia Lai": ["gia lai"],
        "Đắk Lắk": ["đắk lắk", "dak lak"],
        "Khánh Hòa": ["khánh hòa", "khanh hoa"],
        "Trà Vinh": ["trà vinh", "tra vinh"],
        "Sóc Trăng": ["sóc trăng", "soc trang"],
        "Bến Tre": ["bến tre", "ben tre"],
        "Quảng Trị": ["quảng trị", "quang tri"],
        "Hà Tĩnh": ["hà tĩnh", "ha tinh"],
        "Thanh Hóa": ["thanh hóa", "thanh hoa"],
        "Nghệ An": ["nghệ an", "nghe an"],
        "Thái Nguyên": ["thái nguyên", "thai nguyen"],
        "Vĩnh Phúc": ["vĩnh phúc", "vinh phuc"],
        "Hưng Yên": ["hưng yên", "hung yen"],
        "Hải Dương": ["hải dương", "hai duong"]
    }

    zone_map = {
        "VSIP Industrial Park": ["vsip"],
        "DEEP C Industrial Zones": ["deep c"],
        "Amata City Hub": ["amata"],
        "WHA Smart Technology": ["wha"],
        "Phú Mỹ Industrial Complex": ["phú mỹ", "phu my"],
        "Lego Carbon-Neutral Factory": ["lego"],
        "Samsung Electronics Clean Complex": ["samsung"],
        "Foxconn Technology Campus": ["foxconn"],
        "500kV Circuit 3 Transmission": ["500kv", "circuit 3", "mạch 3"],
        "Decree 80 DPPA Pilot Corridor": ["dppa", "decree 80", "nghị định 80"],
        "Offshore Wind Zone": ["offshore wind", "ngoài khơi", "cip", "orsted", "corio"]
    }

    articles = data.get("articles", [])
    for art in articles:
        text = (art.get("title", "") + " " + art.get("snippet", "")).lower()
        
        # Province matching
        matched_prov = None
        for prov, aliases in provinces_map.items():
            if any(a in text for a in aliases):
                matched_prov = prov
                break
        art["province"] = matched_prov
        
        # Zone matching
        matched_zone = None
        for zone, aliases in zone_map.items():
            if any(a in text for a in aliases):
                matched_zone = zone
                break
        art["zone_match"] = matched_zone

    # Write enriched data to both repos
    for repo in [REPO1, REPO2]:
        out_dir = os.path.join(repo, "data")
        os.makedirs(out_dir, exist_ok=True)
        out_file = os.path.join(out_dir, "industry_news.json")
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Enriched news data written to {out_file}")

# 2. Build Section 05 HTML string
def get_section05_html():
    return '''
  <!-- ==================== SECTION 05: GRID & MARKET INTELLIGENCE WIRE ==================== -->
  <section id="marketWire" class="border-b border-brand-border bg-brand-black">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 sm:py-16 space-y-6">
      
      <!-- Section Header -->
      <div class="flex flex-col md:flex-row md:items-end justify-between pb-4 border-b border-brand-border gap-4">
        <div>
          <div class="inline-flex items-center gap-2 px-2 py-0.5 mb-2 border border-brand-border bg-brand-card font-mono text-[10px] text-emerald-400 tracking-wider uppercase">
            <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
            <span data-en="LIVE INTELLIGENCE WIRE • MULTI-SOURCE FEED" data-vi="BẢN TIN TRỰC TUYẾN • ĐA NGUỒN DỮ LIỆU">LIVE INTELLIGENCE WIRE • MULTI-SOURCE FEED</span>
          </div>
          <h2 data-en="Section 05 // Grid Developments & Market Intelligence Wire" data-vi="Mục 05 // Bản tin Lưới điện & Thị trường Năng lượng" class="font-mono text-xs uppercase tracking-widest text-slate-400">Section 05 // Grid Developments & Market Intelligence Wire</h2>
          <p data-en="Vietnam Clean Energy & Eco-Park Market Telemetry" data-vi="Thông tin Thị trường Năng lượng Tái tạo & KCN Sinh thái" class="text-xl sm:text-2xl font-light text-white mt-1">Vietnam Clean Energy & Eco-Park Market Telemetry</p>
          <p data-en="Real-time regulatory decrees (Decree 80 DPPA, Decree 135 rooftop solar), 500kV Circuit 3 dispatch, and industrial zone green power off-take." data-vi="Cập nhật cơ chế DPPA (Nghị định 80), điện mặt trời mái nhà (Nghị định 135), đường dây 500kV mạch 3 và hợp đồng mua bán điện sạch KCN." class="text-xs text-slate-500 mt-1 max-w-3xl font-light">Real-time regulatory decrees (Decree 80 DPPA, Decree 135 rooftop solar), 500kV Circuit 3 dispatch, and industrial zone green power off-take.</p>
        </div>

        <!-- Sync status & Refresh button -->
        <div class="flex items-center gap-2.5 font-mono text-xs shrink-0">
          <span id="newsSyncStatus" class="border border-brand-border bg-brand-card px-2.5 py-1 text-slate-400 text-[11px] flex items-center gap-1.5">
            <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
            <span id="newsSyncText">Syncing...</span>
          </span>
          <button id="refreshNewsBtn" onclick="fetchNewsData(true)" class="border border-brand-border bg-brand-card hover:bg-brand-surface text-slate-200 px-3 py-1 flex items-center gap-1.5 transition-colors cursor-pointer text-[11px]">
            <i data-lucide="refresh-cw" class="w-3.5 h-3.5 text-emerald-400"></i>
            <span data-en="Refresh" data-vi="Làm mới">Refresh</span>
          </button>
        </div>
      </div>

      <!-- Real-Time Breaking Ticker Tape -->
      <div class="flex items-center gap-3 px-3.5 py-2.5 bg-brand-card border border-brand-border text-xs overflow-hidden">
        <span class="font-mono text-[10px] uppercase font-bold tracking-wider px-2 py-0.5 bg-emerald-600 text-white shrink-0 flex items-center gap-1">
          <span class="w-1.5 h-1.5 rounded-full bg-white animate-ping"></span>
          <span data-en="BREAKING" data-vi="MỚI NHẤT">BREAKING</span>
        </span>
        <div id="breakingTickerContainer" class="flex-1 truncate font-mono text-slate-200 text-xs">
          <span class="text-slate-500">Loading latest clean energy market intelligence dispatches...</span>
        </div>
      </div>

      <!-- Filter & Search Controls -->
      <div class="bg-brand-card border border-brand-border p-3 sm:p-4 space-y-3">
        <div class="flex flex-col sm:flex-row gap-3 items-stretch sm:items-center justify-between">
          <!-- Text Search -->
          <div class="relative flex-1">
            <i data-lucide="search" class="w-3.5 h-3.5 text-slate-500 absolute left-3 top-2.5"></i>
            <input 
              type="text" 
              id="newsSearchInput" 
              oninput="handleNewsSearch(this.value)"
              data-placeholder-en="Filter dispatches by keyword, policy, project, or industrial park..." 
              data-placeholder-vi="Lọc bản tin theo từ khóa, cơ chế, dự án, KCN..." 
              placeholder="Filter dispatches by keyword, policy, project, or industrial park..." 
              class="w-full pl-9 pr-4 py-1.5 bg-brand-surface border border-brand-border text-xs text-white placeholder-slate-500 focus:outline-none focus:border-slate-400 font-mono"
            />
          </div>

          <!-- Total Count -->
          <div class="font-mono text-[11px] text-slate-400 shrink-0 self-center">
            <span data-en="Showing" data-vi="Hiển thị">Showing</span> 
            <span id="filteredNewsCount" class="font-semibold text-white">0</span> 
            <span data-en="dispatches" data-vi="tin tức">dispatches</span>
          </div>
        </div>

        <!-- Sector Pills Toolbar -->
        <div class="flex flex-wrap items-center gap-2 pt-2 border-t border-brand-border text-[11px] font-mono">
          <span data-en="Sector:" data-vi="Lĩnh vực:" class="text-slate-500 uppercase tracking-wider text-[10px]">Sector:</span>
          <button data-news-sector="all" onclick="selectNewsSector('all')" class="news-sector-pill px-2.5 py-1 text-[11px] font-medium bg-emerald-600 text-white transition-colors cursor-pointer border border-emerald-500/40">All Signals</button>
          <button data-news-sector="Policy & DPPA" onclick="selectNewsSector('Policy & DPPA')" class="news-sector-pill px-2.5 py-1 text-[11px] font-medium bg-brand-surface text-slate-300 hover:text-white border border-brand-border transition-colors cursor-pointer">Policy &amp; DPPA</button>
          <button data-news-sector="Eco-Parks & Siting" onclick="selectNewsSector('Eco-Parks & Siting')" class="news-sector-pill px-2.5 py-1 text-[11px] font-medium bg-brand-surface text-slate-300 hover:text-white border border-brand-border transition-colors cursor-pointer">Eco-Parks &amp; Siting</button>
          <button data-news-sector="Solar & Wind" onclick="selectNewsSector('Solar & Wind')" class="news-sector-pill px-2.5 py-1 text-[11px] font-medium bg-brand-surface text-slate-300 hover:text-white border border-brand-border transition-colors cursor-pointer">Solar &amp; Wind</button>
          <button data-news-sector="Grid & Interconnect" onclick="selectNewsSector('Grid & Interconnect')" class="news-sector-pill px-2.5 py-1 text-[11px] font-medium bg-brand-surface text-slate-300 hover:text-white border border-brand-border transition-colors cursor-pointer">Grid &amp; Interconnect</button>
          <button data-news-sector="Finance & ESG" onclick="selectNewsSector('Finance & ESG')" class="news-sector-pill px-2.5 py-1 text-[11px] font-medium bg-brand-surface text-slate-300 hover:text-white border border-brand-border transition-colors cursor-pointer">Finance &amp; ESG</button>
        </div>
      </div>

      <!-- News Articles Grid -->
      <div id="newsGrid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
        <!-- Injected via JavaScript -->
      </div>

      <!-- Expand/Collapse Button Container -->
      <div id="newsExpandContainer" class="pt-4 text-center">
        <button id="toggleNewsExpandBtn" onclick="toggleNewsExpand()" class="px-5 py-2.5 bg-brand-card hover:bg-brand-surface border border-brand-border text-slate-300 hover:text-white font-mono text-xs inline-flex items-center gap-2 transition-colors cursor-pointer">
          <span id="newsExpandBtnText" data-en="View All 200 Intelligence Dispatches" data-vi="Xem Tất Cả 200 Bản Tin">View All 200 Intelligence Dispatches</span>
          <i data-lucide="chevron-down" id="newsExpandIcon" class="w-4 h-4 text-emerald-400"></i>
        </button>
      </div>

    </div>
  </section>
'''

# 3. Build News JS string to append before </script>
def get_news_js():
    return '''
    // =========================================================================
    // SECTION 05: GRID & MARKET INTELLIGENCE WIRE LOGIC
    // =========================================================================
    let allNewsArticles = [];
    let activeNewsSector = "all";
    let newsSearchTerm = "";
    let isNewsExpanded = false;
    const INITIAL_NEWS_LIMIT = 12;
    let breakingTickerIndex = 0;
    let tickerInterval = null;

    const sectorBadgeStyles = {
      "Policy & DPPA": "bg-amber-500/10 text-amber-400 border-amber-500/30",
      "Solar & Wind": "bg-teal-500/10 text-teal-400 border-teal-500/30",
      "Eco-Parks & Siting": "bg-indigo-500/10 text-indigo-400 border-indigo-500/30",
      "Grid & Interconnect": "bg-sky-500/10 text-sky-400 border-sky-500/30",
      "Finance & ESG": "bg-purple-500/10 text-purple-400 border-purple-500/30",
      "FDI & Infrastructure": "bg-emerald-500/10 text-emerald-400 border-emerald-500/30"
    };

    const defaultSectorImages = {
      "Solar & Wind": "https://images.unsplash.com/photo-1509391365360-2e959784a276?auto=format&fit=crop&w=800&q=80",
      "Policy & DPPA": "https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?auto=format&fit=crop&w=800&q=80",
      "Eco-Parks & Siting": "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&w=800&q=80",
      "Grid & Interconnect": "https://images.unsplash.com/photo-1544724569-5f546fd6f2b5?auto=format&fit=crop&w=800&q=80",
      "Finance & ESG": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80",
      "FDI & Infrastructure": "https://images.unsplash.com/photo-1504917599217-d4dc5ebe6122?auto=format&fit=crop&w=800&q=80"
    };

    async function fetchNewsData(forceRefresh = false) {
      const syncBadge = document.getElementById("newsSyncText");
      if (syncBadge) syncBadge.innerText = currentLang === 'vi' ? 'Đang đồng bộ...' : 'Syncing...';

      const cacheKey = "rvn_energymap_news_cache";
      const cacheTimeKey = "rvn_energymap_news_time";

      if (!forceRefresh) {
        const cached = localStorage.getItem(cacheKey);
        const cachedTime = localStorage.getItem(cacheTimeKey);
        if (cached && cachedTime && (Date.now() - parseInt(cachedTime, 10)) < 15 * 60 * 1000) {
          try {
            const parsed = JSON.parse(cached);
            allNewsArticles = parsed.articles || [];
            updateNewsSyncBadge(parsed.updated_at);
            renderNewsGrid();
            renderBreakingTicker();
            return;
          } catch (e) {
            console.warn("Corrupt news cache", e);
          }
        }
      }

      try {
        const res = await fetch("/data/industry_news.json?t=" + Date.now());
        if (!res.ok) throw new Error("Status " + res.status);
        const data = await res.json();
        allNewsArticles = data.articles || [];
        localStorage.setItem(cacheKey, JSON.stringify(data));
        localStorage.setItem(cacheTimeKey, Date.now().toString());
        updateNewsSyncBadge(data.updated_at);
        renderNewsGrid();
        renderBreakingTicker();
      } catch (err) {
        console.warn("Local JSON fetch failed, trying fallback:", err);
        fallbackNewsFetch();
      }
    }

    async function fallbackNewsFetch() {
      try {
        const rssUrl = encodeURIComponent("https://news.google.com/rss/search?q=Vietnam+renewable+energy+OR+DPPA+OR+industrial+park&hl=en-US&gl=US&ceid=US:en");
        const res = await fetch(`https://api.rss2json.com/v1/api.json?rss_url=${rssUrl}`);
        const data = await res.json();
        if (data && data.items && data.items.length > 0) {
          allNewsArticles = data.items.map(item => ({
            title: item.title,
            link: item.link,
            source: item.author || "Google News",
            relative_time: "Recent",
            snippet: item.description ? item.description.replace(/<[^>]+>/g, '').slice(0, 180) + '...' : '',
            sector: item.title.toLowerCase().includes("dppa") ? "Policy & DPPA" : (item.title.toLowerCase().includes("solar") || item.title.toLowerCase().includes("wind") ? "Solar & Wind" : "Eco-Parks & Siting"),
            image_url: null
          }));
          updateNewsSyncBadge(null);
          renderNewsGrid();
          renderBreakingTicker();
        }
      } catch (e) {
        console.error("All news feed vectors failed", e);
        const syncBadge = document.getElementById("newsSyncText");
        if (syncBadge) syncBadge.innerText = currentLang === 'vi' ? 'Lưu trữ ngoại tuyến' : 'Offline Archive';
      }
    }

    function updateNewsSyncBadge(updatedAt) {
      const syncBadge = document.getElementById("newsSyncText");
      if (!syncBadge) return;
      if (updatedAt) {
        try {
          const d = new Date(updatedAt);
          const timeStr = d.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
          syncBadge.innerText = currentLang === 'vi' ? `Đã đồng bộ ${timeStr}` : `Synced ${timeStr}`;
        } catch (_) {
          syncBadge.innerText = currentLang === 'vi' ? 'Trực tuyến' : 'Live Sync';
        }
      } else {
        syncBadge.innerText = currentLang === 'vi' ? 'Trực tuyến' : 'Live Feed';
      }
    }

    function selectNewsSector(sector) {
      activeNewsSector = sector;
      document.querySelectorAll(".news-sector-pill").forEach(btn => {
        if (btn.getAttribute("data-news-sector") === sector) {
          btn.className = "news-sector-pill px-2.5 py-1 text-[11px] font-medium bg-emerald-600 text-white transition-colors cursor-pointer border border-emerald-500/40";
        } else {
          btn.className = "news-sector-pill px-2.5 py-1 text-[11px] font-medium bg-brand-surface text-slate-300 hover:text-white border border-brand-border transition-colors cursor-pointer";
        }
      });
      renderNewsGrid();
    }

    function handleNewsSearch(val) {
      newsSearchTerm = val.trim();
      renderNewsGrid();
    }

    function toggleNewsExpand() {
      isNewsExpanded = !isNewsExpanded;
      const btnText = document.getElementById("newsExpandBtnText");
      const icon = document.getElementById("newsExpandIcon");
      if (isNewsExpanded) {
        btnText.innerText = currentLang === 'vi' ? 'Thu gọn danh sách bản tin' : 'Collapse Intelligence Archives';
        if (icon) icon.setAttribute("data-lucide", "chevron-up");
      } else {
        btnText.innerText = currentLang === 'vi' ? `Xem Tất Cả ${allNewsArticles.length} Bản Tin` : `View All ${allNewsArticles.length} Intelligence Dispatches`;
        if (icon) icon.setAttribute("data-lucide", "chevron-down");
        const wireElem = document.getElementById("marketWire");
        if (wireElem) wireElem.scrollIntoView({ behavior: 'smooth' });
      }
      renderNewsGrid();
    }

    function renderBreakingTicker() {
      const container = document.getElementById("breakingTickerContainer");
      if (!container || allNewsArticles.length === 0) return;

      const headlines = allNewsArticles.slice(0, 8);
      if (tickerInterval) clearInterval(tickerInterval);

      function updateTicker() {
        const item = headlines[breakingTickerIndex % headlines.length];
        const provBadge = item.province ? `<span class="px-1.5 py-0.5 rounded bg-brand-surface border border-brand-border text-emerald-400 font-semibold mr-1.5">${item.province}</span>` : '';
        container.innerHTML = `
          <a href="${item.link}" target="_blank" rel="noopener noreferrer" class="hover:text-emerald-400 transition-colors inline-flex items-center gap-2">
            ${provBadge}
            <span class="font-semibold text-white">[${item.source}]</span>
            <span class="text-slate-200">${item.title}</span>
            <span class="text-slate-500">(${item.relative_time})</span>
          </a>
        `;
        breakingTickerIndex++;
      }

      updateTicker();
      tickerInterval = setInterval(updateTicker, 4500);
    }

    function renderNewsGrid() {
      const grid = document.getElementById("newsGrid");
      const countSpan = document.getElementById("filteredNewsCount");
      const expandContainer = document.getElementById("newsExpandContainer");
      if (!grid) return;

      let filtered = allNewsArticles.filter(art => {
        const matchesSector = activeNewsSector === "all" || art.sector === activeNewsSector;
        const norm = newsSearchTerm.toLowerCase();
        const matchesSearch = !norm ||
          (art.title && art.title.toLowerCase().includes(norm)) ||
          (art.snippet && art.snippet.toLowerCase().includes(norm)) ||
          (art.source && art.source.toLowerCase().includes(norm)) ||
          (art.province && art.province.toLowerCase().includes(norm)) ||
          (art.zone_match && art.zone_match.toLowerCase().includes(norm));
        return matchesSector && matchesSearch;
      });

      if (countSpan) countSpan.innerText = filtered.length;

      if (filtered.length === 0) {
        grid.innerHTML = `
          <div class="col-span-full py-12 text-center font-mono text-xs text-slate-500 bg-brand-card border border-brand-border">
            ${currentLang === 'vi' ? 'Không tìm thấy bản tin phù hợp với bộ lọc hiện tại.' : 'No intelligence dispatches matched current filters.'}
          </div>
        `;
        if (expandContainer) expandContainer.classList.add("hidden");
        return;
      }

      if (expandContainer) expandContainer.classList.remove("hidden");

      const displayItems = isNewsExpanded ? filtered : filtered.slice(0, INITIAL_NEWS_LIMIT);
      const isDefaultView = (activeNewsSector === "all" && !newsSearchTerm && !isNewsExpanded && displayItems.length >= 4);

      let html = "";

      if (isDefaultView) {
        const lead = displayItems[0];
        const remaining = displayItems.slice(1);
        const fallbackImg = defaultSectorImages[lead.sector] || "https://images.unsplash.com/photo-1509391365360-2e959784a276?auto=format&fit=crop&w=1200&q=80";
        const leadImg = lead.image_url || fallbackImg;
        const leadSectorStyle = sectorBadgeStyles[lead.sector] || "bg-emerald-500/10 text-emerald-400 border-emerald-500/30";

        html += `
          <!-- FEATURED LEAD DISPATCH (HERO SPOTLIGHT) -->
          <div class="col-span-full bg-brand-card border border-brand-border hover:border-slate-500 transition-all overflow-hidden group">
            <div class="grid grid-cols-1 lg:grid-cols-12 items-stretch">
              <div class="relative lg:col-span-7 h-60 sm:h-72 lg:h-80 overflow-hidden bg-brand-surface">
                <img src="${leadImg}" alt="${lead.title.replace(/"/g, '&quot;')}" loading="lazy" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" onerror="this.onerror=null;this.src='${fallbackImg}';" />
                <div class="absolute inset-0 bg-gradient-to-t from-brand-black/90 via-transparent to-brand-black/30 pointer-events-none"></div>
                <div class="absolute top-3 left-3 flex flex-wrap items-center gap-2">
                  <span class="font-mono text-[9px] uppercase font-bold tracking-wider px-2 py-0.5 bg-emerald-600 text-white flex items-center gap-1.5">
                    <span class="w-1.5 h-1.5 rounded-full bg-white animate-ping"></span>
                    FEATURED LEAD DISPATCH
                  </span>
                  <span class="font-mono text-[9px] uppercase font-semibold px-2 py-0.5 backdrop-blur-md bg-black/70 text-white border border-white/10">
                    ${lead.sector}
                  </span>
                  ${lead.province ? `<span class="font-mono text-[9px] uppercase font-semibold px-2 py-0.5 backdrop-blur-md bg-emerald-950/80 text-emerald-300 border border-emerald-700/50">📍 ${lead.province}</span>` : ''}
                </div>
                <span class="absolute bottom-3 right-3 font-mono text-[10px] px-2 py-0.5 bg-black/80 text-slate-300 backdrop-blur-sm border border-brand-border">
                  ${lead.relative_time}
                </span>
              </div>
              <div class="lg:col-span-5 p-5 sm:p-6 flex flex-col justify-between space-y-4">
                <div class="space-y-2.5">
                  <div class="flex items-center gap-2 font-mono text-[11px] text-emerald-400">
                    <span class="inline-block w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
                    <span class="font-semibold uppercase tracking-wider">${lead.source}</span>
                    <span class="text-slate-600">&middot;</span>
                    <span class="text-slate-400 font-normal">${lead.relative_time}</span>
                  </div>
                  <h3 class="text-base sm:text-lg lg:text-xl font-light leading-snug text-white group-hover:text-emerald-400 transition-colors">
                    <a href="${lead.link}" target="_blank" rel="noopener noreferrer">
                      ${lead.title}
                    </a>
                  </h3>
                  <p class="text-xs text-slate-400 font-light leading-relaxed line-clamp-3">
                    ${lead.snippet}
                  </p>
                </div>
                <div class="pt-3 border-t border-brand-border flex items-center justify-between font-mono text-xs">
                  ${lead.zone_match ? `<span class="text-[10px] text-emerald-400 bg-brand-surface px-2 py-0.5 border border-brand-border">⚡ ${lead.zone_match}</span>` : `<span class="text-[10px] text-slate-500">Verified Energy Telemetry</span>`}
                  <a href="${lead.link}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-1.5 text-slate-300 hover:text-white transition-colors">
                    <span>${currentLang === 'vi' ? 'Xem toàn văn' : 'Read Dispatch'}</span>
                    <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
                  </a>
                </div>
              </div>
            </div>
          </div>
        `;

        remaining.forEach(art => {
          html += renderArticleCard(art);
        });
      } else {
        displayItems.forEach(art => {
          html += renderArticleCard(art);
        });
      }

      grid.innerHTML = html;
      if (window.lucide) lucide.createIcons();
    }

    function renderArticleCard(art) {
      const fallbackImg = defaultSectorImages[art.sector] || "https://images.unsplash.com/photo-1509391365360-2e959784a276?auto=format&fit=crop&w=800&q=80";
      const cardImg = art.image_url || fallbackImg;
      const sectorStyle = sectorBadgeStyles[art.sector] || "bg-brand-surface text-slate-300 border-brand-border";

      return `
        <div class="flex flex-col bg-brand-card border border-brand-border hover:border-slate-500 transition-all overflow-hidden group">
          <!-- Thumbnail Image -->
          <div class="relative h-44 overflow-hidden bg-brand-surface">
            <img src="${cardImg}" alt="${art.title.replace(/"/g, '&quot;')}" loading="lazy" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" onerror="this.onerror=null;this.src='${fallbackImg}';" />
            <div class="absolute inset-0 bg-gradient-to-t from-brand-black/90 via-transparent to-brand-black/20 pointer-events-none"></div>
            <div class="absolute top-2.5 left-2.5 flex flex-wrap items-center gap-1.5">
              <span class="font-mono text-[9px] uppercase font-semibold px-2 py-0.5 border ${sectorStyle} backdrop-blur-md bg-black/60">
                ${art.sector}
              </span>
              ${art.province ? `<span class="font-mono text-[9px] uppercase font-semibold px-1.5 py-0.5 bg-black/70 text-emerald-300 border border-emerald-500/30 backdrop-blur-md">📍 ${art.province}</span>` : ''}
            </div>
            <span class="absolute bottom-2 right-2 font-mono text-[9px] px-1.5 py-0.5 bg-black/80 text-slate-300 border border-brand-border backdrop-blur-sm">
              ${art.relative_time}
            </span>
          </div>

          <!-- Card Content -->
          <div class="p-4 flex-1 flex flex-col justify-between space-y-3">
            <div class="space-y-2">
              <div class="flex items-center justify-between font-mono text-[10px] text-slate-400">
                <span class="font-semibold uppercase text-emerald-400">${art.source}</span>
                ${art.zone_match ? `<span class="text-slate-400 truncate max-w-[140px]" title="${art.zone_match}">⚡ ${art.zone_match}</span>` : `<span>${art.relative_time}</span>`}
              </div>
              <h4 class="text-sm font-normal text-white group-hover:text-emerald-400 transition-colors line-clamp-2 leading-snug">
                <a href="${art.link}" target="_blank" rel="noopener noreferrer">
                  ${art.title}
                </a>
              </h4>
              <p class="text-xs text-slate-400 font-light line-clamp-2 leading-relaxed">
                ${art.snippet}
              </p>
            </div>

            <!-- Card Action Footer -->
            <div class="pt-3 border-t border-brand-border flex items-center justify-between font-mono text-xs">
              ${art.province ? `
              <a href="/?search=${encodeURIComponent(art.province)}" class="text-[10px] text-slate-400 hover:text-white flex items-center gap-1 transition-colors">
                <span>View Hubs</span>
                <i data-lucide="chevron-right" class="w-3 h-3 text-emerald-400"></i>
              </a>` : `<span class="text-[10px] text-slate-600">National Grid</span>`}
              <a href="${art.link}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-1 text-[11px] text-emerald-400 hover:text-emerald-300 transition-colors font-medium">
                <span>${currentLang === 'vi' ? 'Xem tin' : 'Read'}</span>
                <i data-lucide="external-link" class="w-3 h-3"></i>
              </a>
            </div>
          </div>
        </div>
      `;
    }
'''

def update_projectenergy():
    html_file = os.path.join(REPO1, "projectenergy", "index.html")
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update Header Navigation to include Market Wire link
    nav_pattern = r'(<nav class="hidden md:flex items-center gap-2 font-mono text-xs text-slate-400">.*?)(</nav>)'
    
    def repl_nav(m):
        cur = m.group(1)
        if '#marketWire' not in cur:
            cur += '''\n        <span class="text-slate-600">&middot;</span>\n        <a href="#marketWire" class="hover:text-white transition-colors flex items-center gap-1.5"><span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span> Market Wire</a>'''
        return cur + m.group(2)

    content = re.sub(nav_pattern, repl_nav, content, flags=re.DOTALL)

    # Also add Wire button in header tools (mobile)
    tools_pattern = r'(<!-- Header Tools & Language Selector -->\s*<div [^>]*>)'
    def repl_tools(m):
        wire_btn = '''\n        <a href="#marketWire" class="md:hidden px-2 py-0.5 border border-brand-border bg-brand-card text-[10px] text-emerald-400 hover:text-white flex items-center gap-1"><span class="w-1 h-1 rounded-full bg-emerald-500"></span> Wire</a>'''
        if '#marketWire' not in content[:m.end() + 300]:
            return m.group(1) + wire_btn
        return m.group(1)

    content = re.sub(tools_pattern, repl_tools, content)

    # 2. Insert Section 05 before footer
    footer_pos = content.find("<!-- ==================== FOOTER ==================== -->")
    if footer_pos != -1 and 'id="marketWire"' not in content:
        content = content[:footer_pos] + get_section05_html() + "\n  " + content[footer_pos:]
        print("Inserted Section 05 into projectenergy/index.html")
    elif 'id="marketWire"' in content:
        print("Section 05 already present in projectenergy/index.html")

    # 3. Insert News JS and hook into DOMContentLoaded
    if "function fetchNewsData" not in content:
        # Insert before window.addEventListener('DOMContentLoaded'
        dom_pos = content.find("window.addEventListener('DOMContentLoaded', () => {")
        if dom_pos != -1:
            content = content[:dom_pos] + get_news_js() + "\n\n    " + content[dom_pos:]
            print("Inserted News JS logic into projectenergy/index.html")

        # Hook into DOMContentLoaded
        content = content.replace("syncProjectsFromSupabase();", "syncProjectsFromSupabase();\n      fetchNewsData();")
        print("Hooked fetchNewsData() into DOMContentLoaded")

    # 4. Save to RenewableVietNam and copy to Qking232.github.io
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {html_file}")

    qking_html = os.path.join(REPO2, "projectenergy", "index.html")
    os.makedirs(os.path.dirname(qking_html), exist_ok=True)
    with open(qking_html, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Mirrored to {qking_html}")

def create_energymap_redirects():
    redirect_html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="refresh" content="0; url=/projectenergy/">
<link rel="canonical" href="https://renewablevietnam.com/projectenergy/">
<meta name="robots" content="noindex">
<title>Redirecting to Vietnam Clean Energy Atlas</title>
</head>
<body>
<p>This page has moved to <a href="/projectenergy/">/projectenergy/</a>.</p>
</body>
</html>
'''
    for repo in [REPO1, REPO2]:
        d = os.path.join(repo, "energymap")
        os.makedirs(d, exist_ok=True)
        target = os.path.join(d, "index.html")
        with open(target, "w", encoding="utf-8") as f:
            f.write(redirect_html)
        print(f"Created canonical redirect at {target}")

def main():
    print("Enriching news dataset with industrial zone & province schemas...")
    enrich_news_data()
    print("\nIntegrating Section 05 into projectenergy/index.html...")
    update_projectenergy()
    print("\nCreating /energymap/ route aliases...")
    create_energymap_redirects()
    print("\n[SUCCESS] EnergyMap News Wire & Industrial Zone UI Feed fully integrated!")

if __name__ == "__main__":
    main()
