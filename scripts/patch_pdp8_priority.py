#!/usr/bin/env python3
import os

def patch_energy_pdp8():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    new_code = '''// 14. Render PDP8 Priority Pipeline
    function renderPdp8Projects() {
      const container = document.getElementById("pdp8ProjectsGrid");
      if (!container || !pdp8Dataset || !pdp8Dataset.priority_projects) return;

      const pipelineBadge = document.getElementById("pipelineCount");
      if (pipelineBadge) pipelineBadge.textContent = pdp8Dataset.priority_projects.length;

      let html = "";
      pdp8Dataset.priority_projects.forEach(p => {
        const isConstruction = p.status && (p.status.includes("Construction") || p.status.includes("Testing"));
        const badgeColor = isConstruction ? "bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border-emerald-500/20" : "bg-slate-600/10 text-slate-700 dark:text-slate-300 border-amber-500/20";
        const pLon = p.lon || p.lng;
        const gmapsUrl = (p.lat && pLon)
          ? `https://www.google.com/maps/search/?api=1&query=${p.lat},${pLon}`
          : `https://www.google.com/maps/search/?api=1&query=${encodeURIComponent((p.name || '') + ' ' + (p.province || p.location || 'Vietnam'))}`;

        const firstWord = (p.name || '').split(' ')[0] || '';
        const safeName = (p.name || '').replace(/'/g, "\\\\'");
        const safeProv = (p.province || '').replace(/'/g, "\\\\'");

        // Safe match with ALL_PROJECTS if available
        let matchedAssetIdx = -1;
        if (Array.isArray(ALL_PROJECTS)) {
          matchedAssetIdx = ALL_PROJECTS.findIndex(proj => 
            (proj.name && p.name && (proj.name.toLowerCase().includes(p.name.toLowerCase()) || p.name.toLowerCase().includes(proj.name.toLowerCase()))) ||
            (proj.name && firstWord.length > 2 && proj.name.toLowerCase().includes(firstWord.toLowerCase()))
          );
        }

        const intertieBtn = (matchedAssetIdx !== -1)
          ? `<button onclick="event.stopPropagation(); traceAssetInterconnection(${matchedAssetIdx});" class="inline-flex items-center gap-1 text-emerald-600 dark:text-emerald-400 hover:underline font-semibold cursor-pointer" title="Trace Intertie to Nearest Substation">
               <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" /></svg>
               <span>Grid Intertie</span>
             </button>`
          : '';

        html += `
          <div class="p-3.5 rounded-xl bg-slate-50/80 dark:bg-darkCard/80 border border-borderSlate dark:border-darkBorder hover:border-teal-500/50 dark:hover:border-teal-400/40 transition-all flex flex-col justify-between space-y-2.5">
            <div class="space-y-1.5">
              <div class="flex items-center justify-between font-mono text-[10px]">
                <span class="px-2 py-0.5 rounded border ${badgeColor} font-semibold">${p.status}</span>
                <span class="text-inkMuted dark:text-textDarkMuted">COD: <b class="text-inkPrimary dark:text-textDarkPrimary">${p.target_cod}</b></span>
              </div>
              <div class="flex items-start gap-2">
                <a href="${gmapsUrl}" target="_blank" rel="noopener" title="Open ${p.name} in Google Maps" onclick="event.stopPropagation()" class="mt-0.5 p-1 rounded bg-slate-100 dark:bg-darkCard hover:bg-slate-700 hover:text-white text-slate-500 dark:text-slate-400 transition-colors inline-flex items-center shrink-0">
                  <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="3 6 9 3 15 6 21 3 21 18 15 21 9 18 3 21"></polygon><line x1="9" y1="3" x2="9" y2="18"></line><line x1="15" y1="6" x2="15" y2="21"></line></svg>
                </a>
                <h4 class="text-xs sm:text-sm font-semibold text-inkPrimary dark:text-textDarkPrimary leading-snug">
                  ${p.name}
                </h4>
              </div>
              <p class="text-[11px] text-inkMuted dark:text-textDarkMuted font-light line-clamp-2">
                ${p.notes}
              </p>
            </div>

            <!-- Progress Bar -->
            <div class="space-y-1 font-mono text-[10px]">
              <div class="flex justify-between text-inkMuted dark:text-textDarkMuted">
                <span>Progress: <b class="text-teal-600 dark:text-teal-400">${p.progress_pct}%</b></span>
                <span>${(p.capacity_mw || 0).toLocaleString()} MW &middot; ${p.province}</span>
              </div>
              <div class="w-full h-1.5 rounded-full bg-slate-200 dark:bg-darkSurface overflow-hidden">
                <div class="h-full bg-teal-500 rounded-full transition-all duration-500" style="width: ${p.progress_pct}%"></div>
              </div>
            </div>

            <div class="pt-2 border-t border-borderSlate/60 dark:border-darkBorder/60 flex items-center justify-between font-mono text-[10px]">
              <span class="text-slate-400 truncate max-w-[200px]">${p.investor}</span>
              <div class="flex items-center gap-2">
                <button onclick="locatePdp8ProjectOnMap('${safeName}', '${safeProv}')" class="inline-flex items-center gap-1 text-teal-600 dark:text-teal-400 hover:underline font-semibold cursor-pointer">
                  <span>Locate on Map &rarr;</span>
                </button>
                ${intertieBtn}
              </div>
            </div>
          </div>
        `;
      });

      container.innerHTML = html;
    }

    // 15. Locate Priority Project on Satellite Map
    function locatePdp8ProjectOnMap(name, province) {
      const cleanName = (name || '').toLowerCase();
      const cleanProv = (province || '').toLowerCase();
      const firstWord = cleanName.split(' ')[0] || '';

      const match = ALL_PROJECTS.find(p => {
        const pName = (p.name || '').toLowerCase();
        const pLoc = (p.location || p.province || '').toLowerCase();
        return (cleanName && pName.includes(cleanName)) ||
               (cleanName && pName && cleanName.includes(pName)) ||
               (firstWord.length > 2 && pName.includes(firstWord)) ||
               (cleanProv && pLoc && pLoc.includes(cleanProv));
      });

      if (match) {
        const matchIdx = ALL_PROJECTS.indexOf(match);
        selectAssetFromMap(matchIdx);
      } else {
        searchQuery = name;
        const sInput = document.getElementById("projectSearchInput");
        if (sInput) sInput.value = name;
        switchDossierTab('assets');
        applyFilters();
      }
    }'''

    for sub in ['energy', 'projectenergy']:
        fn = os.path.join(base_dir, sub, 'index.html')
        with open(fn, 'r', encoding='utf-8') as f:
            t = f.read()

        idx = t.find('// 14. Render PDP8 Priority Pipeline')
        end = t.find('// 15B. Render Independent PDP8 Sector Targets Table', idx)
        assert idx != -1 and end != -1, f'Target not found in {fn}'
        
        t_new = t[:idx] + new_code + '\n\n    ' + t[end:]
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(t_new)
        print(f'Updated {fn} successfully!')

if __name__ == '__main__':
    patch_energy_pdp8()
