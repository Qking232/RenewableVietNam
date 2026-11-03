#!/usr/bin/env python3
# -*- coding: utf-8 -*-
with open(r"G:\My Drive\7. AI\RenewableVietNam\projectenergy\index_Rev.007.html", "r", encoding="utf-8") as f:
    content = f.read()

assert "https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" in content, "Missing unpkg Leaflet JS CDN"
assert "https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" in content, "Missing unpkg Leaflet CSS CDN"
assert "renderMainFlowVectors()" in content, "Missing renderMainFlowVectors"
assert "mainFlowMapInstance.fitBounds" in content, "Missing fitBounds"
assert "mainFlowMapInstance.invalidateSize()" in content, "Missing invalidateSize"
assert "energyTopProvincesChart" in content, "Missing energyTopProvincesChart"

print("All verifications for Rev 007 passed successfully!")
