#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verification script for index_Rev.010.html: Side-by-Side Workstation layout.
"""

from pathlib import Path

TARGET = Path(r"G:\My Drive\7. AI\RenewableVietNam\projectenergy\index_Rev.010.html")

def verify():
    assert TARGET.exists(), "Target file does not exist"
    html = TARGET.read_text(encoding="utf-8")

    # 1. Side-by-side grid classes
    assert "lg:col-span-8" in html, "Missing lg:col-span-8 for vector map"
    assert "lg:col-span-4" in html, "Missing lg:col-span-4 for node inspection panel"
    assert "nodeInspectionContainer" in html, "Missing nodeInspectionContainer element"
    assert "nodePanelContent" in html, "Missing nodePanelContent container"
    print("PASS: Side-by-side grid layout classes verified.")

    # 2. Logic functions
    assert "function selectGridSubstation" in html, "selectGridSubstation function missing"
    assert "function resetNodeInspectionPanel" in html, "resetNodeInspectionPanel function missing"
    assert "function selectCleanPlant" in html, "selectCleanPlant function missing"
    assert "function quickSelectHub" in html, "quickSelectHub function missing"
    print("PASS: Workstation state handlers verified.")

    # 3. Modal routing
    assert "function openSubstationModal(subId)" in html, "openSubstationModal missing"
    assert "selectGridSubstation(subId, true);" in html, "openSubstationModal does not route to selectGridSubstation"
    print("PASS: Modal calls routed to side-by-side dossier panel.")

    # 4. Sovereignty and tileLayer
    assert "QUẦN ĐẢO HOÀNG SA" in html, "Hoang Sa marker missing"
    assert "QUẦN ĐẢO TRƯỜNG SA" in html, "Truong Sa marker missing"
    assert "L.tileLayer" not in html, "L.tileLayer still found!"
    print("PASS: Sovereignty beacons and zero raster tile requirements verified.")

    print("ALL REV 010 VERIFICATION CHECKS PASSED.")

if __name__ == "__main__":
    verify()
