#!/usr/bin/env python3
# -*- coding: utf-8 -*-
with open(r"G:\My Drive\7. AI\RenewableVietNam\projectenergy\index_Rev.005.html", "r", encoding="utf-8") as f:
    content = f.read()

required_ids = [
    "mainEnergyFlowMap", "mapToggleFlow500Btn", "mapToggleGrid220Btn", "mapToggleAssetsBtn",
    "energyTopProvincesChart", "energyStatusDoughnutChart",
    "pdp8ProjectsGrid", "viewPipelineContainer", "viewAssetsDossier", "viewGridContainer",
    "gridTopologyMap", "gridSubstationsTableBody", "gridLinesTableBody",
    "substationModalOverlay", "substationModalName"
]

missing = [x for x in required_ids if f'id="{x}"' not in content]
if missing:
    print("MISSING IDS in Rev 005:", missing)
    exit(1)
else:
    print("All required DOM IDs verified in Rev 005.")

assert "grid-flow-500kv" in content, "Missing grid-flow-500kv CSS class"
assert "const parsedCap = parseFloat(p.capacity" in content, "Missing parsedCap in normalizeProjects"
assert "initMainFlowMap()" in content, "Missing initMainFlowMap invocation"

print("Integrity checks passed 100%.")
