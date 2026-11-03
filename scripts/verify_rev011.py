#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verification script for index_Rev.011.html:
12 Pillars, Transition Energy Flow, and National Energy Market Terminal.
"""

from pathlib import Path

TARGET = Path(r"G:\My Drive\7. AI\RenewableVietNam\projectenergy\index_Rev.011.html")

def verify():
    assert TARGET.exists(), "Target file does not exist"
    html = TARGET.read_text(encoding="utf-8")

    # 1. 12 Pillars
    assert 'id="energy12PillarsSection"' in html, "energy12PillarsSection missing"
    for i in range(1, 13):
        pillar_tag = f"Pillar {i:02d}"
        assert pillar_tag in html, f"Missing {pillar_tag}"
    assert "function filterPillars" in html, "filterPillars JS missing"
    print("PASS: 12 Strategic Pillars verified (Pillars 01 to 12).")

    # 2. Transition Energy Flow
    assert 'id="transitionFlowSection"' in html, "transitionFlowSection missing"
    assert "switchTransitionScenario" in html, "switchTransitionScenario JS missing"
    assert "TRANSITION_SCENARIOS" in html, "TRANSITION_SCENARIOS data missing"
    assert "scenario2025Btn" in html and "scenario2030Btn" in html and "scenario2050Btn" in html, "Scenario buttons missing"
    print("PASS: Transition Energy Flow dynamic balance model verified.")

    # 3. National Energy Situation & Market Terminal
    assert 'id="energyMarketSection"' in html, "energyMarketSection missing"
    assert "System Marginal (SMP)" in html, "SMP ticker missing"
    assert "Capacity Payment (CAN)" in html, "CAN price missing"
    assert "Decree 80/2024/NĐ-CP DPPA Wheeling Fee" in html, "DPPA wheeling missing"
    assert "Industrial Retail Electricity TOU Tiers" in html, "TOU tiers missing"
    assert "Regional Grid Reserve Margins" in html, "Reserve margins missing"
    print("PASS: National Energy Situation & Market Terminal verified.")

    # 4. Integrity checks
    assert "lg:col-span-8" in html and "lg:col-span-4" in html, "Side-by-side grid missing"
    assert "nodeInspectionContainer" in html, "Node dossier missing"
    assert "QUẦN ĐẢO HOÀNG SA" in html and "QUẦN ĐẢO TRƯỜNG SA" in html, "Sovereign markers missing"
    assert "L.tileLayer" not in html, "L.tileLayer found!"
    print("PASS: Workstation layout and cartographic sovereignty intact.")

    print("ALL REV 011 CHECKS PASSED.")

if __name__ == "__main__":
    verify()
