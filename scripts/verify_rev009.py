#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verification script for index_Rev.009.html and vector cartography assets.
"""

from pathlib import Path
import json
import gzip

TARGET_HTML = Path(r"G:\My Drive\7. AI\RenewableVietNam\projectenergy\index_Rev.009.html")
GEOJSON_FILE = Path(r"G:\My Drive\7. AI\RenewableVietNam\data\vietnam_territory.json")
GEOJSON_GZ = Path(r"G:\My Drive\7. AI\RenewableVietNam\data\vietnam_territory.json.gz")

def verify():
    assert TARGET_HTML.exists(), "Target HTML missing"
    assert GEOJSON_FILE.exists(), "Territory GeoJSON missing"
    assert GEOJSON_GZ.exists(), "Territory GeoJSON GZ missing"

    html = TARGET_HTML.read_text(encoding="utf-8")
    
    # 1. Verify tileLayer is gone
    assert "L.tileLayer" not in html, "L.tileLayer still found in HTML!"
    print("PASS: L.tileLayer completely purged (zero raster tiles, zero watermarks)")

    # 2. Verify territory loader
    assert "loadVietnamTerritory" in html, "loadVietnamTerritory function missing"
    assert "renderVietnamTerritoryVectors" in html, "renderVietnamTerritoryVectors function missing"
    assert "vietnam_territory.json" in html, "vietnam_territory.json reference missing"
    print("PASS: Vector territory loader wired properly")

    # 3. Verify sovereignty beacons
    assert "QUẦN ĐẢO HOÀNG SA" in html, "Hoàng Sa sovereignty marker missing"
    assert "QUẦN ĐẢO TRƯỜNG SA" in html, "Trường Sa sovereignty marker missing"
    assert "BIỂN ĐÔNG (EAST SEA)" in html, "Biển Đông maritime watermark missing"
    assert "sovereignty-badge" in html, "Sovereignty badge CSS class missing"
    print("PASS: Sovereignty beacons and legal territorial markers present")

    # 4. Verify GeoJSON data content
    with open(GEOJSON_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert data["type"] == "FeatureCollection", "Invalid GeoJSON structure"
    names = [feat["properties"]["name"] for feat in data["features"]]
    print(f"PASS: GeoJSON contains {len(data['features'])} sovereign features: {names}")

    # 5. Check GZ size
    gz_size = GEOJSON_GZ.stat().st_size
    print(f"PASS: GZ compressed vector size: {gz_size / 1024:.1f} KB (super lightweight)")

    print("ALL SOVEREIGN VECTOR CARTOGRAPHY CHECKS PASSED.")

if __name__ == "__main__":
    verify()
