#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verification script for index_Rev.020.html (10-Module Visual Telemetry Suite).
"""

from pathlib import Path

TARGET = Path(r"G:\My Drive\7. AI\RenewableVietNam\index_Rev.020.html")

def verify():
    assert TARGET.exists(), "Target file missing"
    html = TARGET.read_text(encoding="utf-8")

    # 1. Section presence
    assert 'id="visualTelemetrySuiteSection"' in html, "visualTelemetrySuiteSection missing"
    assert "Comprehensive 10-Module Visual Telemetry" in html, "Suite header missing"
    print("PASS: 10-Module Visual Telemetry section header verified.")

    # 2. Check all 10 visuals
    visual_ids = [
        "trajectoryChart",
        "pdp8MixChart",
        "regionalRadarChart",
        "evNetworkChart",
        "dailyDispatchChart",
        "capexAllocationChart",
        "substationHierarchyChart",
        "marketClearingChart",
        "topProvincesEcoparkChart"
    ]
    for cid in visual_ids:
        assert f'id="{cid}"' in html, f"Missing canvas id: {cid}"
        assert f"document.getElementById('{cid}')" in html, f"Missing init logic for: {cid}"

    # Visual 10: Directional Pipeline
    assert "Systemic Energy Flow &amp; Power Balance Pipeline" in html, "Visual 10 title missing"
    assert "84.0 GW Installed" in html, "Visual 10 inputs missing"
    assert "65,566 km Circuits" in html, "Visual 10 supergrid missing"
    print("PASS: All 10 visual modules and canvas targets verified.")

    # 3. Check 12 pillars intact
    assert 'id="homepage12PillarsSection"' in html, "12 Pillars section missing"
    for i in range(1, 13):
        assert f"PILLAR {i:02d}" in html, f"Missing PILLAR {i:02d}"
    print("PASS: 12 Strategic Pillars framework remains 100% intact.")

    # 4. Check other sections
    assert "Decree 80/2024 DPPA Bilateral Offtake Simulator" in html, "DPPA simulator missing"
    assert "Subdomain Command Console" in html, "Subdomain console missing"
    print("PASS: DPPA simulator and subdomain consoles intact.")

    print("ALL HOMEPAGE REV 020 CHECKS PASSED.")

if __name__ == "__main__":
    verify()
