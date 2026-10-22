#!/usr/bin/env python3
"""
====================================================================
European Green Deal & CBAM Carbon Compliance Assessment Suite
====================================================================
Integrates Tab 3 ("Green Indicators (EU CBAM & Principles)") into
the Clean Power & EVN Tariff Calculator Suite across all production
HTML files:
  1. RenewableVietNam/index.html
  2. RenewableVietNam/green/index.html
  3. Qking232.github.io/index.html
  4. Qking232.github.io/green/index.html
====================================================================
"""

import os
import sys

TARGET_FILES = [
    r"G:\My Drive\7. AI\Gemini\RenewableVietNam\index.html",
    r"G:\My Drive\7. AI\Gemini\RenewableVietNam\green\index.html",
    r"G:\My Drive\7. AI\Gemini\Qking232.github.io\index.html",
    r"G:\My Drive\7. AI\Gemini\Qking232.github.io\green\index.html",
]

JS_TAB_OLD = """    document.addEventListener("DOMContentLoaded", () => {
      loadNationalIndustrialHubs();
      updateEvnEstimator();
      initEcoParkMap();

      // Calculator Suite Tab Switcher
      const tabCorporateSizerBtn = document.getElementById("tabCorporateSizerBtn");
      const tabEvnEstimatorBtn = document.getElementById("tabEvnEstimatorBtn");
      const corporateSizerContainer = document.getElementById("corporateSizerContainer");
      const evnEstimatorContainer = document.getElementById("evnEstimatorContainer");

      if (tabCorporateSizerBtn && tabEvnEstimatorBtn && corporateSizerContainer && evnEstimatorContainer) {
        tabCorporateSizerBtn.addEventListener("click", () => {
          tabCorporateSizerBtn.className = "calc-tab-btn px-3 py-1.5 rounded-lg bg-teal-600 text-white font-semibold shadow-sm transition-all cursor-pointer flex items-center gap-2";
          tabEvnEstimatorBtn.className = "calc-tab-btn px-3 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-inkPrimary dark:hover:text-white transition-all cursor-pointer flex items-center gap-2";
          corporateSizerContainer.classList.remove("hidden");
          evnEstimatorContainer.classList.add("hidden");
        });

        tabEvnEstimatorBtn.addEventListener("click", () => {
          tabEvnEstimatorBtn.className = "calc-tab-btn px-3 py-1.5 rounded-lg bg-teal-600 text-white font-semibold shadow-sm transition-all cursor-pointer flex items-center gap-2";
          tabCorporateSizerBtn.className = "calc-tab-btn px-3 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-inkPrimary dark:hover:text-white transition-all cursor-pointer flex items-center gap-2";
          evnEstimatorContainer.classList.remove("hidden");
          corporateSizerContainer.classList.add("hidden");
          updateEvnEstimator();
        });
      }"""

JS_TAB_NEW = """    // ====================================================================
    // EUROPEAN GREEN DEAL & CBAM CARBON COMPLIANCE ENGINE
    // ====================================================================
    function updateGreenIndicators() {
      const sectorSelect = document.getElementById("greenSectorSelect");
      const mwhSlider = document.getElementById("greenMwhSlider");
      const reSlider = document.getElementById("greenReSlider");
      const etsSlider = document.getElementById("greenEtsSlider");
      if (!sectorSelect || !mwhSlider || !reSlider || !etsSlider) return;

      const sector = sectorSelect.value;
      const mwhMonthly = parseFloat(mwhSlider.value);
      const rePct = parseFloat(reSlider.value);
      const etsPriceEur = parseFloat(etsSlider.value);

      document.getElementById("greenMwhVal").textContent = `${mwhMonthly.toLocaleString()} MWh`;
      document.getElementById("greenReVal").textContent = `${rePct}% Clean`;
      document.getElementById("greenEtsVal").textContent = `\u20ac ${etsPriceEur} / tCO2e`;

      const badgeEl = document.getElementById("greenSectorBadge");
      if (badgeEl) {
        if (["steel", "aluminum", "chemicals"].includes(sector)) {
          badgeEl.className = "font-mono text-[10px] font-semibold text-amber-600 dark:text-amber-400 px-2 py-0.5 rounded bg-amber-500/10 border border-amber-500/20";
          badgeEl.textContent = "Direct CBAM Scope (Annex I)";
        } else if (sector === "electronics") {
          badgeEl.className = "font-mono text-[10px] font-semibold text-sky-600 dark:text-sky-400 px-2 py-0.5 rounded bg-sky-500/10 border border-sky-500/20";
          badgeEl.textContent = "CSRD & RE100 Scope 2";
        } else {
          badgeEl.className = "font-mono text-[10px] font-semibold text-emerald-600 dark:text-emerald-400 px-2 py-0.5 rounded bg-emerald-500/10 border border-emerald-500/20";
          badgeEl.textContent = "EU Ecodesign & Supply Chain";
        }
      }

      // Mathematical Formulation
      const annualMwh = mwhMonthly * 12.0;
      const gridEf = 0.7221; // MONRE Vietnam baseline tCO2e / MWh
      const baselineCo2 = annualMwh * gridEf;
      const reRatio = rePct / 100.0;
      const abatedCo2 = baselineCo2 * reRatio;
      const residualCo2 = baselineCo2 * (1.0 - reRatio);

      const avoidedEur = abatedCo2 * etsPriceEur;
      const avoidedUsd = avoidedEur * 1.09; // EUR/USD exchange baseline

      // Vietnam Institutional Alignment Score (0 - 100)
      const baseScore = 72.0;
      const reBonus = reRatio * 23.0; // up to 23 pts from clean power share
      const eipBonus = 5.0; // Siting in Vietnam master-planned zone
      const indexScore = Math.min(100.0, baseScore + reBonus + eipBonus);

      // DOM Updates
      document.getElementById("greenBaselineCo2").innerHTML = `${Math.round(baselineCo2).toLocaleString()} t/yr`;
      document.getElementById("greenAbatedCo2").innerHTML = `${Math.round(abatedCo2).toLocaleString()} t/yr`;
      document.getElementById("greenAbatedPctLabel").textContent = `${rePct}% Decarbonized`;
      document.getElementById("greenCbamAvoidedEur").innerHTML = `&euro; ${Math.round(avoidedEur).toLocaleString()}`;
      document.getElementById("greenCbamAvoidedUsd").textContent = `\u2248 $${Math.round(avoidedUsd).toLocaleString()} USD/yr`;

      const scoreEl = document.getElementById("greenIndexScore");
      const ratingBadgeEl = document.getElementById("greenIndexRatingBadge");
      const riskLevelEl = document.getElementById("greenCbamRiskLevel");
      const progressBarEl = document.getElementById("greenIndexProgressBar");
      const pillarPowerEl = document.getElementById("greenPillarPower");

      if (scoreEl) scoreEl.textContent = indexScore.toFixed(1);
      if (progressBarEl) progressBarEl.style.width = `${indexScore}%`;

      if (rePct >= 70) {
        if (ratingBadgeEl) {
          ratingBadgeEl.className = "text-[11px] font-mono font-semibold text-emerald-600 dark:text-emerald-400 px-2 py-0.5 rounded bg-emerald-500/10 border border-emerald-500/20 ml-1";
          ratingBadgeEl.textContent = "Tier-1 EU Green Deal Verified";
        }
        if (riskLevelEl) {
          riskLevelEl.className = "text-xs font-mono font-semibold text-emerald-600 dark:text-emerald-400";
          riskLevelEl.textContent = "Negligible CBAM Exposure";
        }
        if (pillarPowerEl) pillarPowerEl.textContent = "Exemplary (RE100 / DPPA)";
      } else if (rePct >= 35) {
        if (ratingBadgeEl) {
          ratingBadgeEl.className = "text-[11px] font-mono font-semibold text-teal-600 dark:text-teal-400 px-2 py-0.5 rounded bg-teal-500/10 border border-teal-500/20 ml-1";
          ratingBadgeEl.textContent = "High Alignment / Transition Ready";
        }
        if (riskLevelEl) {
          riskLevelEl.className = "text-xs font-mono font-semibold text-teal-600 dark:text-teal-400";
          riskLevelEl.textContent = "Low CBAM Exposure";
        }
        if (pillarPowerEl) pillarPowerEl.textContent = "Substantial Solar Offset";
      } else {
        if (ratingBadgeEl) {
          ratingBadgeEl.className = "text-[11px] font-mono font-semibold text-sky-600 dark:text-sky-400 px-2 py-0.5 rounded bg-sky-500/10 border border-sky-500/20 ml-1";
          ratingBadgeEl.textContent = "Positive Grid Baseline";
        }
        if (riskLevelEl) {
          riskLevelEl.className = "text-xs font-mono font-semibold text-sky-600 dark:text-sky-400";
          riskLevelEl.textContent = "Protected via Hydro Base";
        }
        if (pillarPowerEl) pillarPowerEl.textContent = "Grid Hydro Advantage";
      }
    }

    document.addEventListener("DOMContentLoaded", () => {
      loadNationalIndustrialHubs();
      updateEvnEstimator();
      updateGreenIndicators();
      initEcoParkMap();

      // Calculator Suite Tab Switcher
      const tabCorporateSizerBtn = document.getElementById("tabCorporateSizerBtn");
      const tabEvnEstimatorBtn = document.getElementById("tabEvnEstimatorBtn");
      const tabGreenIndicatorBtn = document.getElementById("tabGreenIndicatorBtn");
      const corporateSizerContainer = document.getElementById("corporateSizerContainer");
      const evnEstimatorContainer = document.getElementById("evnEstimatorContainer");
      const greenIndicatorContainer = document.getElementById("greenIndicatorContainer");

      const activateTab = (activeBtn, activeContainer) => {
        [tabCorporateSizerBtn, tabEvnEstimatorBtn, tabGreenIndicatorBtn].forEach(btn => {
          if (!btn) return;
          if (btn === activeBtn) {
            btn.className = "calc-tab-btn px-3 py-1.5 rounded-lg bg-teal-600 text-white font-semibold shadow-sm transition-all cursor-pointer flex items-center gap-2";
          } else {
            btn.className = "calc-tab-btn px-3 py-1.5 rounded-lg text-inkMuted dark:text-textDarkMuted hover:text-inkPrimary dark:hover:text-white transition-all cursor-pointer flex items-center gap-2";
          }
        });
        [corporateSizerContainer, evnEstimatorContainer, greenIndicatorContainer].forEach(c => {
          if (!c) return;
          if (c === activeContainer) {
            c.classList.remove("hidden");
          } else {
            c.classList.add("hidden");
          }
        });
      };

      if (tabCorporateSizerBtn && tabEvnEstimatorBtn && tabGreenIndicatorBtn) {
        tabCorporateSizerBtn.addEventListener("click", () => activateTab(tabCorporateSizerBtn, corporateSizerContainer));
        tabEvnEstimatorBtn.addEventListener("click", () => {
          activateTab(tabEvnEstimatorBtn, evnEstimatorContainer);
          updateEvnEstimator();
        });
        tabGreenIndicatorBtn.addEventListener("click", () => {
          activateTab(tabGreenIndicatorBtn, greenIndicatorContainer);
          updateGreenIndicators();
        });
      }"""

def process_file(filepath):
    if not os.path.exists(filepath):
        print(f"[WARN] File not found: {filepath}")
        return False

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    crlf = "\r\n" in content
    le = "\r\n" if crlf else "\n"

    def norm(s):
        return s.replace("\r\n", "\n").replace("\n", le)

    target = norm(JS_TAB_OLD)
    repl = norm(JS_TAB_NEW)
    if target in content:
        content = content.replace(target, repl, 1)
        print(f"  [OK] JS Tab Switcher & Engine added in {os.path.basename(filepath)}")
        with open(filepath, "w", encoding="utf-8", newline="") as f:
            f.write(content)
        return True
    else:
        print(f"  [SKIP] JS Tab target not found or already updated in {os.path.basename(filepath)}")
        return False

if __name__ == "__main__":
    for p in TARGET_FILES:
        print(f"\nProcessing {p}...")
        process_file(p)
