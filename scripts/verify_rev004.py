#!/usr/bin/env python3
# -*- coding: utf-8 -*-
with open(r"G:\My Drive\7. AI\RenewableVietNam\projectenergy\index_Rev.004.html", "r", encoding="utf-8") as f:
    content = f.read()

required_ids = [
    "tabAssetsBtn", "tabPipelineBtn", "tabGridBtn",
    "viewAssetsDossier", "viewPipelineContainer", "viewGridContainer",
    "gridTopologyMap", "gridSubstationsTableBody", "gridLinesTableBody",
    "substationModalOverlay", "substationModalName", "substationModalVoltageBadge"
]

missing = [x for x in required_ids if f'id="{x}"' not in content]
if missing:
    print("MISSING IDS:", missing)
else:
    print("All required IDs verified present.")

# Check Leaflet assets
assert "vendor/leaflet/leaflet.css" in content, "Missing Leaflet CSS"
assert "vendor/leaflet/leaflet.js" in content, "Missing Leaflet JS"
assert "/data/vietnam_grid_substations.json" in content, "Missing grid substations JSON reference"
assert "/data/vietnam_grid_lines.json" in content, "Missing grid lines JSON reference"

print("All asset references and DOM IDs verified successfully.")
