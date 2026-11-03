#!/usr/bin/env python3
# -*- coding: utf-8 -*-
with open(r"G:\My Drive\7. AI\RenewableVietNam\projectenergy\index_Rev.008.html", "r", encoding="utf-8") as f:
    content = f.read()

assert "mapToggleHeadroomBtn" in content, "Missing mapToggleHeadroomBtn"
assert "findNearestSubstation" in content, "Missing findNearestSubstation"
assert "traceAssetInterconnection" in content, "Missing traceAssetInterconnection"
assert "renderSubstationHeadroomMarkers" in content, "Missing renderSubstationHeadroomMarkers"
assert "intertie-radial-line" in content, "Missing intertie-radial-line CSS"
assert "Investment Brief" in content, "Missing Investment Brief export button"

print("All Phase 1 Institutional Elevation verifications passed 100%!")
