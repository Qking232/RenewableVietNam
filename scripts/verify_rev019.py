#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verification script for index_Rev.019.html (Homepage 12 Pillars).
"""

from pathlib import Path

TARGET = Path(r"G:\My Drive\7. AI\RenewableVietNam\index_Rev.019.html")

def verify():
    assert TARGET.exists(), "Target file missing"
    html = TARGET.read_text(encoding="utf-8")

    # 1. Section presence
    assert 'id="homepage12PillarsSection"' in html, "homepage12PillarsSection missing"
    assert 'id="homepagePillarsContainer"' in html, "homepagePillarsContainer missing"
    assert 'id="nodeInspectorPanel"' in html, "nodeInspectorPanel missing"
    print("PASS: Homepage 12 pillars section and drawer container verified.")

    # 2. Check all 12 pillars in HTML
    for i in range(1, 13):
        tag = f"PILLAR {i:02d}"
        assert tag in html, f"Missing {tag} in HTML"
    print("PASS: All 12 pillar cards present in HTML (Pillars 01 to 12).")

    # 3. Check all 12 entries in JavaScript nodeDetails array
    for i in range(1, 13):
        js_tag = f'"PILLAR {i:02d} &middot;'
        assert js_tag in html, f"Missing {js_tag} in JavaScript nodeDetails"
    print("PASS: All 12 pillar definitions present in JavaScript nodeDetails array.")

    # 4. Check category filter function
    assert "function filterHomepagePillars" in html, "filterHomepagePillars function missing"
    assert "hpFilterAll" in html and "hpFilterGen" in html and "hpFilterGrid" in html and "hpFilterMarket" in html, "Filter buttons missing"
    print("PASS: Category filter function and buttons verified.")

    # 5. Check integrity of other sections
    assert "Interactive Graph Suite" in html, "Multi-graph section missing"
    assert "Subdomain Command Console" in html, "Subdomain console missing"
    print("PASS: Other homepage sections intact.")

    print("ALL HOMEPAGE REV 019 CHECKS PASSED.")

if __name__ == "__main__":
    verify()
