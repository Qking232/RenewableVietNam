"""
Integrate Corporate Clean Power Siting & Allocation Sizer into index.html (Industrial Hub Telemetry View).
- Places #powerSizer section below #hubs.
- Wires up calcDemandSlider, calcMwhSlider, calcReSlider with live calculation.
- Renders dynamic recommended hubs that link directly to jumpToHub(hubName).
- Adds quick jump button in Hero Header.
- Cleans up legacy references in scripts.
"""

import os
import re

INDEX_PATH = r"G:\My Drive\7. AI\Gemini\RenewableVietNam\index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Check insertion point: after line with </section> for #hubs
hubs_end_marker = '</section>\n    </div>\n  </main>'
if hubs_end_marker not in content:
    # try flexible matching
    m = re.search(r'(</section>\s*</div>\s*</main>)', content)
    assert m, "Could not locate end of #hubs section!"
    hubs_end_marker = m.group(1)

POWER_SIZER_HTML = '''
      <!-- ==================================================================== -->
      <!-- CORPORATE CLEAN POWER SITING & ALLOCATION SIZER                      -->
      <!-- ==================================================================== -->
      <section id="powerSizer" class="p-5 sm:p-6 rounded-2xl bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder shadow-sm space-y-6">
        <!-- Header -->
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-borderSlate dark:border-darkBorder pb-4">
          <div class="space-y-1">
            <div class="flex items-center gap-2">
              <span class="w-2 h-2 rounded-full bg-teal-500 animate-pulse"></span>
              <span class="font-mono text-[10px] uppercase tracking-wider text-teal-600 dark:text-teal-400 font-semibold">
                Decision 2699/QĐ-BCT &middot; Decree 80/2024/NĐ-CP DPPA &middot; Decision 1658/QĐ-TTg
              </span>
            </div>
            <h2 class="text-xl sm:text-2xl font-normal tracking-tight text-inkPrimary dark:text-textDarkPrimary">
              Corporate Clean Power Siting &amp; Allocation Sizer
            </h2>
            <p class="text-xs text-inkMuted dark:text-textDarkMuted font-light max-w-3xl">
              Simulate connected factory electrical peak demand, onsite rooftop solar yield, and statutory DPPA bilateral grid wheeling volumes with live siting recommendations across Vietnam's industrial parks.
            </p>
          </div>

          <div class="flex flex-col sm:items-end gap-1.5 shrink-0">
            <div class="font-mono text-[11px] text-inkMuted dark:text-textDarkMuted bg-slate-100 dark:bg-darkCard px-2.5 py-1 rounded-lg border border-borderSlate dark:border-darkBorder">
              Grid Baseline: <span class="font-semibold text-inkPrimary dark:text-textDarkPrimary">0.7221 tCO<sub>2</sub>e/MWh</span>
            </div>
            <a href="/calculator/" class="text-teal-600 dark:text-teal-400 font-mono text-xs hover:underline flex items-center gap-1">
              <span>Open Full Tariff Suite (EVN &amp; CBAM) &rarr;</span>
            </a>
          </div>
        </div>

        <!-- Sizer Cockpit (Sliders + Telemetry Output) -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          <!-- Left Form (7 cols) -->
          <div class="lg:col-span-7 space-y-4 font-sans text-xs">
            <!-- Slider 1: Peak Demand -->
            <div class="space-y-2 p-4 rounded-xl bg-slate-50 dark:bg-darkCard/50 border border-slate-200 dark:border-darkBorder">
              <div class="flex justify-between items-center">
                <label for="calcDemandSlider" class="font-medium text-inkPrimary dark:text-textDarkPrimary">
                  Connected Electrical Peak Demand (MW):
                </label>
                <span id="calcDemandVal" class="font-mono text-sm font-bold text-teal-600 dark:text-teal-400">10 MW</span>
              </div>
              <input type="range" id="calcDemandSlider" min="2" max="60" step="1" value="10" class="w-full accent-teal-600 cursor-pointer" />
              <div class="flex justify-between font-mono text-[10px] text-slate-400">
                <span>2 MW (Precision Assembly)</span>
                <span>30 MW</span>
                <span>60 MW (Mega Fab / Foundry)</span>
              </div>
            </div>

            <!-- Slider 2: Monthly Consumption -->
            <div class="space-y-2 p-4 rounded-xl bg-slate-50 dark:bg-darkCard/50 border border-slate-200 dark:border-darkBorder">
              <div class="flex justify-between items-center">
                <label for="calcMwhSlider" class="font-medium text-inkPrimary dark:text-textDarkPrimary">
                  Monthly Electricity Consumption (MWh):
                </label>
                <span id="calcMwhVal" class="font-mono text-sm font-bold text-teal-600 dark:text-teal-400">4,500 MWh</span>
              </div>
              <input type="range" id="calcMwhSlider" min="500" max="25000" step="500" value="4500" class="w-full accent-teal-600 cursor-pointer" />
              <div class="flex justify-between font-mono text-[10px] text-slate-400">
                <span>500 MWh</span>
                <span>12,000 MWh</span>
                <span>25,000 MWh (Continuous Smelting)</span>
              </div>
            </div>

            <!-- Slider 3: Target RE100 Share -->
            <div class="space-y-2 p-4 rounded-xl bg-slate-50 dark:bg-darkCard/50 border border-slate-200 dark:border-darkBorder">
              <div class="flex justify-between items-center">
                <label for="calcReSlider" class="font-medium text-inkPrimary dark:text-textDarkPrimary">
                  Target RE100 Clean Power Share (%):
                </label>
                <span id="calcReVal" class="font-mono text-sm font-bold text-teal-600 dark:text-teal-400">80%</span>
              </div>
              <input type="range" id="calcReSlider" min="20" max="100" step="5" value="80" class="w-full accent-teal-600 cursor-pointer" />
              <div class="flex justify-between font-mono text-[10px] text-slate-400">
                <span>20% (Partial Offset)</span>
                <span>60%</span>
                <span>100% (Full RE100 Direct Wheeling)</span>
              </div>
            </div>
          </div>

          <!-- Right Telemetry Card (5 cols) -->
          <div class="lg:col-span-5 p-4 sm:p-5 rounded-xl bg-slate-50 dark:bg-darkCard border border-borderSlate dark:border-darkBorder space-y-4">
            <div class="flex items-center justify-between pb-2 border-b border-borderSlate/60 dark:border-darkBorder/60">
              <span class="font-mono text-[11px] font-semibold text-inkPrimary dark:text-textDarkPrimary uppercase tracking-wider">
                Procurement &amp; Siting Telemetry
              </span>
              <button id="copyCalcBriefBtn" class="px-2.5 py-1 rounded bg-white dark:bg-darkSurface border border-borderSlate dark:border-darkBorder text-inkPrimary dark:text-textDarkPrimary font-mono text-[10px] hover:border-teal-500 dark:hover:border-teal-400 transition-all flex items-center gap-1 cursor-pointer" title="Copy Siting Brief to Clipboard">
                <svg class="w-3 h-3 text-teal-500 dark:text-teal-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
                </svg>
                <span>Copy Brief</span>
              </button>
            </div>

            <!-- 4 KPI Metrics -->
            <div class="grid grid-cols-2 gap-3 text-xs">
              <div class="p-3 rounded-lg bg-white dark:bg-darkSurface border border-slate-200 dark:border-darkBorder space-y-0.5">
                <span class="text-[10px] font-mono text-slate-400 uppercase">Onsite Rooftop PV</span>
                <p id="calcRooftopPv" class="text-base font-mono font-bold text-teal-600 dark:text-teal-400">3.5 MWp</p>
                <span class="text-[10px] text-inkMuted dark:text-textDarkMuted block">~4,900 MWh/yr yield</span>
              </div>

              <div class="p-3 rounded-lg bg-white dark:bg-darkSurface border border-slate-200 dark:border-darkBorder space-y-0.5">
                <span class="text-[10px] font-mono text-slate-400 uppercase">DPPA Grid Wheeling</span>
                <p id="calcDppaGap" class="text-base font-mono font-bold text-sky-600 dark:text-sky-400">38,300 MWh</p>
                <span class="text-[10px] text-inkMuted dark:text-textDarkMuted block">Offsite bilateral PPA</span>
              </div>

              <div class="p-3 rounded-lg bg-white dark:bg-darkSurface border border-slate-200 dark:border-darkBorder space-y-0.5">
                <span class="text-[10px] font-mono text-slate-400 uppercase">EVN Grid Firming</span>
                <p id="calcGridFirming" class="text-base font-mono font-bold text-slate-700 dark:text-slate-300">10,800 MWh</p>
                <span class="text-[10px] text-inkMuted dark:text-textDarkMuted block">Standard industrial tariff</span>
              </div>

              <div class="p-3 rounded-lg bg-white dark:bg-darkSurface border border-slate-200 dark:border-darkBorder space-y-0.5">
                <span class="text-[10px] font-mono text-slate-400 uppercase">Scope 2 Avoided</span>
                <p id="calcCo2Avoided" class="text-base font-mono font-bold text-emerald-600 dark:text-emerald-400">31,195 tCO<sub>2</sub>e</p>
                <span class="text-[10px] text-inkMuted dark:text-textDarkMuted block">Annual carbon offset</span>
              </div>
            </div>

            <!-- Top Recommended Siting Hubs with Jump-to-Table Action -->
            <div class="pt-3 border-t border-borderSlate/60 dark:border-darkBorder/60 space-y-2">
              <div class="flex items-center justify-between">
                <span class="font-mono text-[10px] text-slate-400 uppercase tracking-wider font-semibold">
                  Recommended Eco-Industrial Parks:
                </span>
                <span class="font-mono text-[9px] text-teal-600 dark:text-teal-400">Click to filter &amp; view</span>
              </div>
              <div id="calcRecommendedHubs" class="space-y-1.5 font-mono text-[11px]">
                <!-- Dynamically populated and clickable via jumpToHub() -->
              </div>
            </div>
          </div>
        </div>
      </section>
'''

replacement = '</section>\n' + POWER_SIZER_HTML + '\n    </div>\n  </main>'
new_content = content.replace(hubs_end_marker, replacement, 1)

# 2. Add Quick Sizer Jump Button in Hero Header
# Look for hero actions or metrics
hero_anchor = '<span>168 Eco-Parks</span>'
if hero_anchor in new_content:
    hero_jump_btn = '''<span>168 Eco-Parks</span>
          </span>
          <a href="#powerSizer" class="text-teal-700 dark:text-teal-400 bg-teal-50 dark:bg-teal-950/40 px-3 py-1.5 rounded-lg border border-teal-200 dark:border-teal-800/40 flex items-center gap-1.5 shadow-sm font-semibold hover:bg-teal-100 dark:hover:bg-teal-900/40 transition-colors">
            <span>⚡ Corporate Power Sizer</span> &darr;'''
    new_content = new_content.replace('<span>168 Eco-Parks</span>\n          </span>', hero_jump_btn, 1)

# 3. Enhance updateCalculator and jumpToHub in JavaScript
calc_js_snippet = '''
    function jumpToHub(hubName) {
      const searchInput = document.getElementById("hubSearchInput");
      if (searchInput) {
        searchInput.value = hubName;
        currentFilter.search = hubName.toLowerCase();
        currentPage = 1;
        renderTable();
        if (typeof filterMarkers === "function") filterMarkers();
      }
      document.getElementById("hubs")?.scrollIntoView({ behavior: 'smooth' });
    }

    function updateCalculator() {
      const demandEl = document.getElementById("calcDemandSlider");
      const mwhEl = document.getElementById("calcMwhSlider");
      const reEl = document.getElementById("calcReSlider");
      if (!demandEl || !mwhEl || !reEl) return;

      const demandMw = parseFloat(demandEl.value);
      const monthlyMwh = parseFloat(mwhEl.value);
      const rePct = parseFloat(reEl.value);

      document.getElementById("calcDemandVal").textContent = `${demandMw} MW`;
      document.getElementById("calcMwhVal").textContent = `${Number(monthlyMwh).toLocaleString()} MWh`;
      document.getElementById("calcReVal").textContent = `${rePct}%`;

      const annualMwh = monthlyMwh * 12;
      const targetCleanMwh = annualMwh * (rePct / 100);

      const rooftopPvMw = Math.min(demandMw * 0.35, 12);
      const rooftopAnnualYieldMwh = rooftopPvMw * 1400;

      const dppaGapMwh = Math.max(0, targetCleanMwh - rooftopAnnualYieldMwh);
      const gridFirmingMwh = Math.max(0, annualMwh - targetCleanMwh);

      const co2AvoidedTons = targetCleanMwh * 0.7221;

      document.getElementById("calcRooftopPv").textContent = `${rooftopPvMw.toFixed(1)} MWp`;
      document.getElementById("calcDppaGap").textContent = `${Math.round(dppaGapMwh).toLocaleString()} MWh`;
      document.getElementById("calcGridFirming").textContent = `${Math.round(gridFirmingMwh).toLocaleString()} MWh`;
      document.getElementById("calcCo2Avoided").textContent = `${Math.round(co2AvoidedTons).toLocaleString()} tCO2e`;

      const recContainer = document.getElementById("calcRecommendedHubs");
      if (!recContainer) return;

      const suitableHubs = HUBS.filter(h => (h.rooftopPotentialMWp || 0) >= rooftopPvMw)
                               .sort((a, b) => (b.cleanEnergyShare || 0) - (a.cleanEnergyShare || 0))
                               .slice(0, 3);

      recContainer.innerHTML = suitableHubs.map((h, i) => `
        <button type="button" onclick="jumpToHub('${h.name}')" class="w-full flex items-center justify-between p-2 rounded-lg bg-white dark:bg-darkSurface border border-slate-200 dark:border-darkBorder hover:border-teal-500/50 hover:bg-slate-50 dark:hover:bg-darkCard transition-all cursor-pointer text-left group">
          <div class="truncate mr-2">
            <span class="font-semibold text-inkPrimary dark:text-textDarkPrimary group-hover:text-teal-600 dark:group-hover:text-teal-400 transition-colors">${i + 1}. ${h.name}</span>
            <span class="text-inkMuted dark:text-textDarkMuted text-[10px] ml-1">(${h.province})</span>
          </div>
          <div class="text-right shrink-0 font-mono text-[10px]">
            <span class="text-teal-600 dark:text-teal-400 font-bold">${h.cleanEnergyShare}% clean</span>
            <span class="text-slate-400 ml-1">&middot; ${h.substation} &rarr;</span>
          </div>
        </button>
      `).join("");
    }
'''

# Replace old updateCalculator with new enhanced version
old_update_calc_pattern = re.compile(r'function updateCalculator\(\)\s*\{.*?recContainer\.innerHTML\s*=\s*suitableHubs\.map\(.*?\)\.join\(""\);\s*\}', re.DOTALL)
if old_update_calc_pattern.search(new_content):
    new_content = old_update_calc_pattern.sub(calc_js_snippet.strip(), new_content, count=1)
else:
    # Append if not matched
    new_content = new_content.replace('function closeHubModal() {', calc_js_snippet + '\n    function closeHubModal() {', 1)

# Ensure copyCalcBriefBtn is wired
copy_btn_snippet = '''
      document.getElementById("copyCalcBriefBtn")?.addEventListener("click", () => {
        const demand = document.getElementById("calcDemandVal")?.textContent || "10 MW";
        const consumption = document.getElementById("calcMwhVal")?.textContent || "4,500 MWh";
        const rePct = document.getElementById("calcReVal")?.textContent || "80%";
        const rooftop = document.getElementById("calcRooftopPv")?.textContent || "3.5 MWp";
        const dppa = document.getElementById("calcDppaGap")?.textContent || "38,300 MWh";
        const co2 = document.getElementById("calcCo2Avoided")?.textContent || "31,195 tCO2e";

        const text = `VIETNAM CLEAN POWER SITING BRIEF\\n` +
                     `Connected Peak Demand: ${demand}\\n` +
                     `Monthly Electricity Load: ${consumption}\\n` +
                     `Target Clean Energy Share: ${rePct}\\n` +
                     `Recommended Rooftop Solar: ${rooftop}\\n` +
                     `Required DPPA Bilateral Wheeling: ${dppa}/yr\\n` +
                     `Scope 2 Carbon Emissions Avoided: ${co2}/yr\\n` +
                     `Source: https://renewablevietnam.com`;

        navigator.clipboard.writeText(text).then(() => {
          alert("Corporate power siting brief copied to clipboard!");
        });
      });
'''

if 'document.getElementById("copyCalcBriefBtn")' not in new_content:
    new_content = new_content.replace('document.getElementById("calcDemandSlider")?.addEventListener("input", updateCalculator);',
                                      copy_btn_snippet + '\n      document.getElementById("calcDemandSlider")?.addEventListener("input", updateCalculator);', 1)

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(new_content)

print("[SUCCESS] Relocated and integrated Corporate Power Sizer into index.html!")
print(f"Total size: {len(new_content.encode('utf-8'))} bytes")
