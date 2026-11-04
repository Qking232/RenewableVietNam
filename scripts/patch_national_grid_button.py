#!/usr/bin/env python3
import os

def patch_national_grid():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    html_tab_old = '''              <button id="tabAssetsBtn" class="flex-1 sm:flex-initial px-3 py-1 rounded-md bg-teal-600 text-white font-semibold transition-all cursor-pointer">
                Assets Dossier (<span id="totalAssetsCount">960</span>)
              </button>
              <button id="tabPipelineBtn" class="flex-1 sm:flex-initial px-3 py-1 rounded-md text-inkMuted dark:text-textDarkMuted hover:text-inkPrimary dark:hover:text-white transition-all cursor-pointer">
                PDP8 Priority (<span id="pipelineCount">10</span>)
              </button>
              <button id="tabGridBtn" class="flex-1 sm:flex-initial px-3 py-1 rounded-md text-inkMuted dark:text-textDarkMuted hover:text-inkPrimary dark:hover:text-white transition-all cursor-pointer">
                National Grid (<span id="totalGridSubstationsCount">1,915</span>)
              </button>'''

    html_tab_new = '''              <button id="tabAssetsBtn" onclick="switchDossierTab('assets')" class="flex-1 sm:flex-initial px-3 py-1 rounded-md bg-teal-600 text-white font-semibold transition-all cursor-pointer">
                Assets Dossier (<span id="totalAssetsCount">960</span>)
              </button>
              <button id="tabPipelineBtn" onclick="switchDossierTab('pipeline')" class="flex-1 sm:flex-initial px-3 py-1 rounded-md text-inkMuted dark:text-textDarkMuted hover:text-inkPrimary dark:hover:text-white transition-all cursor-pointer">
                PDP8 Priority (<span id="pipelineCount">10</span>)
              </button>
              <button id="tabGridBtn" onclick="switchDossierTab('grid')" class="flex-1 sm:flex-initial px-3 py-1 rounded-md text-inkMuted dark:text-textDarkMuted hover:text-inkPrimary dark:hover:text-white transition-all cursor-pointer">
                National Grid (<span id="totalGridSubstationsCount">1,915</span>)
              </button>'''

    html_subview_old = '''                <button id="gridSubViewMapBtn" class="px-2.5 py-1 rounded-md bg-rose-600 text-white font-semibold cursor-pointer">
                  Topology Map
                </button>
                <button id="gridSubViewSubstationsBtn" class="px-2.5 py-1 rounded-md bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder text-inkMuted dark:text-textDarkMuted hover:text-rose-600 cursor-pointer">
                  Substations (1,915)
                </button>
                <button id="gridSubViewLinesBtn" class="px-2.5 py-1 rounded-md bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder text-inkMuted dark:text-textDarkMuted hover:text-rose-600 cursor-pointer">
                  Transmission Lines (2,877)
                </button>'''

    html_subview_new = '''                <button id="gridSubViewMapBtn" onclick="switchGridSubView('map')" class="px-2.5 py-1 rounded-md bg-rose-600 text-white font-semibold cursor-pointer">
                  Topology Map
                </button>
                <button id="gridSubViewSubstationsBtn" onclick="switchGridSubView('substations')" class="px-2.5 py-1 rounded-md bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder text-inkMuted dark:text-textDarkMuted hover:text-rose-600 cursor-pointer">
                  Substations (1,915)
                </button>
                <button id="gridSubViewLinesBtn" onclick="switchGridSubView('lines')" class="px-2.5 py-1 rounded-md bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder text-inkMuted dark:text-textDarkMuted hover:text-rose-600 cursor-pointer">
                  Transmission Lines (2,877)
                </button>'''

    js_listeners_old = '''      // Tab Listeners
      document.getElementById("tabAssetsBtn")?.addEventListener("click", () => switchDossierTab('assets'));
      document.getElementById("tabPipelineBtn")?.addEventListener("click", () => switchDossierTab('pipeline'));'''

    js_listeners_new = '''      // Tab Listeners
      document.getElementById("tabAssetsBtn")?.addEventListener("click", () => switchDossierTab('assets'));
      document.getElementById("tabPipelineBtn")?.addEventListener("click", () => switchDossierTab('pipeline'));
      document.getElementById("tabGridBtn")?.addEventListener("click", () => switchDossierTab('grid'));

      // Grid Workstation Sub-Views
      window.switchGridSubView = function(mode) {
        const viewMap = document.getElementById('gridSubViewMap');
        const viewSubs = document.getElementById('gridSubViewSubstations');
        const viewLines = document.getElementById('gridSubViewLines');
        const btnMap = document.getElementById('gridSubViewMapBtn');
        const btnSubs = document.getElementById('gridSubViewSubstationsBtn');
        const btnLines = document.getElementById('gridSubViewLinesBtn');

        [viewMap, viewSubs, viewLines].forEach(v => v && v.classList.add('hidden'));
        [btnMap, btnSubs, btnLines].forEach(b => {
          if (!b) return;
          b.className = 'px-2.5 py-1 rounded-md bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder text-inkMuted dark:text-textDarkMuted hover:text-rose-600 cursor-pointer';
        });

        if (mode === 'substations') {
          if (viewSubs) viewSubs.classList.remove('hidden');
          if (btnSubs) btnSubs.className = 'px-2.5 py-1 rounded-md bg-rose-600 text-white font-semibold cursor-pointer';
          renderGridSubstationsTable();
        } else if (mode === 'lines') {
          if (viewLines) viewLines.classList.remove('hidden');
          if (btnLines) btnLines.className = 'px-2.5 py-1 rounded-md bg-rose-600 text-white font-semibold cursor-pointer';
          renderGridLinesTable();
        } else {
          if (viewMap) viewMap.classList.remove('hidden');
          if (btnMap) btnMap.className = 'px-2.5 py-1 rounded-md bg-rose-600 text-white font-semibold cursor-pointer';
          setTimeout(() => {
            initGridMap();
            if (gridMapInstance) gridMapInstance.invalidateSize();
          }, 100);
        }
      };

      document.getElementById('gridSubViewMapBtn')?.addEventListener('click', () => switchGridSubView('map'));
      document.getElementById('gridSubViewSubstationsBtn')?.addEventListener('click', () => switchGridSubView('substations'));
      document.getElementById('gridSubViewLinesBtn')?.addEventListener('click', () => switchGridSubView('lines'));

      // Grid Voltage Selector Pills
      document.querySelectorAll('.grid-v-pill').forEach(pill => {
        pill.addEventListener('click', () => {
          selectedGridVoltage = pill.dataset.v || 'ALL';
          document.querySelectorAll('.grid-v-pill').forEach(p => {
            p.classList.remove('bg-rose-600', 'text-white', 'font-semibold');
            p.classList.add('bg-white', 'dark:bg-darkSurface');
          });
          pill.classList.add('bg-rose-600', 'text-white', 'font-semibold');
          pill.classList.remove('bg-white', 'dark:bg-darkSurface');

          renderGridMapVectors();
          renderGridSubstationsTable();
          renderGridLinesTable();
        });
      });

      // Grid Substation & Line Search Inputs
      document.getElementById('gridSubstationSearchInput')?.addEventListener('input', () => {
        renderGridSubstationsTable();
      });
      document.getElementById('gridLineSearchInput')?.addEventListener('input', () => {
        renderGridLinesTable();
      });'''

    for sub in ['energy', 'projectenergy']:
        fn = os.path.join(base_dir, sub, 'index.html')
        with open(fn, 'r', encoding='utf-8') as f:
            t = f.read()

        assert html_tab_old in t, f'html_tab_old not in {fn}'
        assert html_subview_old in t, f'html_subview_old not in {fn}'
        assert js_listeners_old in t, f'js_listeners_old not in {fn}'

        t = t.replace(html_tab_old, html_tab_new)
        t = t.replace(html_subview_old, html_subview_new)
        t = t.replace(js_listeners_old, js_listeners_new)

        with open(fn, 'w', encoding='utf-8') as f:
            f.write(t)
        print(f'Successfully updated {fn}!')

if __name__ == '__main__':
    patch_national_grid()
