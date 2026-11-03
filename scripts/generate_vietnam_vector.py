#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate Sovereign Vietnam Territorial Vector GeoJSON (vietnam_territory.json and .json.gz)
Features:
- High-definition Mainland Vietnam S-curve from Natural Earth 10m
- Quần đảo Hoàng Sa (Paracel Islands - TP. Đà Nẵng)
- Quần đảo Trường Sa (Spratly Islands - Tỉnh Khánh Hòa)
- Đảo Phú Quốc (Kiên Giang), Côn Đảo (Bà Rịa - Vũng Tàu), Phú Quý, Lý Sơn, Bạch Long Vĩ
"""

import os
import sys
import json
import gzip
import urllib.request
from pathlib import Path

OUTPUT_DIR = Path(r"G:\My Drive\7. AI\RenewableVietNam\data")

def build_vietnam_territory():
    print("Fetching Natural Earth 10m Vietnam boundary...")
    ne_url = "https://raw.githubusercontent.com/martynafford/natural-earth-geojson/master/10m/cultural/ne_10m_admin_0_countries.json"
    req = urllib.request.Request(ne_url, headers={'User-Agent': 'Mozilla/5.0'})
    
    with urllib.request.urlopen(req, timeout=15) as resp:
        d = json.loads(resp.read().decode('utf-8'))
    
    vn_feature = [f for f in d['features'] if f['properties'].get('SOVEREIGNT') == 'Vietnam' or f['properties'].get('NAME') == 'Vietnam'][0]
    raw_parts = vn_feature['geometry']['coordinates']

    features = []

    # 1. Add Mainland & coastal islands from Natural Earth 10m
    features.append({
        "type": "Feature",
        "properties": {
            "name": "Việt Nam (Đất liền & Hải đảo ven bờ)",
            "name_en": "Vietnam (Mainland & Coastal Islands)",
            "type": "mainland_and_coastal"
        },
        "geometry": {
            "type": "MultiPolygon",
            "coordinates": raw_parts
        }
    })

    # 2. Add Quần đảo Hoàng Sa (Paracel Islands &middot; TP. Đà Nẵng, Việt Nam)
    # Extent: 15.7 - 17.1 N, 111.0 - 113.0 E
    # Modeling distinct island polygons and territorial baseline
    hoang_sa_islands = [
        # Đảo Hoàng Sa (Pattle Island)
        [[[111.59, 16.52], [111.62, 16.52], [111.62, 16.55], [111.59, 16.55], [111.59, 16.52]]],
        # Đảo Phú Lâm (Woody Island)
        [[[112.31, 16.82], [112.35, 16.82], [112.35, 16.85], [112.31, 16.85], [112.31, 16.82]]],
        # Đảo Quang Hòa (Duncan Island)
        [[[111.70, 16.52], [111.73, 16.52], [111.73, 16.54], [111.70, 16.54], [111.70, 16.52]]],
        # Đảo Tri Tôn (Triton Island)
        [[[111.19, 15.77], [111.22, 15.77], [111.22, 15.80], [111.19, 15.80], [111.19, 15.77]]],
        # Đảo Linh Côn (Lincoln Island)
        [[[112.72, 16.65], [112.75, 16.65], [112.75, 16.68], [112.72, 16.68], [112.72, 16.65]]],
        # Đảo Cây (Tree Island) & Bắc
        [[[112.26, 16.97], [112.29, 16.97], [112.29, 17.00], [112.26, 17.00], [112.26, 16.97]]],
        # Bãi Bông Bay (Bomb Bay Reef)
        [[[112.48, 16.02], [112.55, 16.02], [112.55, 16.07], [112.48, 16.07], [112.48, 16.02]]]
    ]

    features.append({
        "type": "Feature",
        "properties": {
            "name": "Quần đảo Hoàng Sa (TP. Đà Nẵng, Việt Nam)",
            "name_en": "Paracel Islands (Da Nang, Vietnam)",
            "type": "archipelago",
            "sovereignty": "Vietnam",
            "jurisdiction": "TP. Đà Nẵng",
            "center": [112.0, 16.5]
        },
        "geometry": {
            "type": "MultiPolygon",
            "coordinates": hoang_sa_islands
        }
    })

    # 3. Add Quần đảo Trường Sa (Spratly Islands &middot; Tỉnh Khánh Hòa, Việt Nam)
    # Extent: 7.5 - 11.8 N, 111.5 - 116.5 E
    truong_sa_islands = [
        # Đảo Trường Sa Lớn (Spratly Island)
        [[[111.90, 8.63], [111.94, 8.63], [111.94, 8.66], [111.90, 8.66], [111.90, 8.63]]],
        # Đảo Song Tử Tây (Southwest Cay)
        [[[114.32, 11.42], [114.35, 11.42], [114.35, 11.45], [114.32, 11.45], [114.32, 11.42]]],
        # Đảo Nam Yết (Namyit Island)
        [[[114.35, 10.17], [114.38, 10.17], [114.38, 10.20], [114.35, 10.20], [114.35, 10.17]]],
        # Đảo Sinh Tồn (Sin Cowe Island)
        [[[114.30, 9.87], [114.34, 9.87], [114.34, 9.90], [114.30, 9.90], [114.30, 9.87]]],
        # Đảo Sơn Ca (Sand Cay)
        [[[114.46, 10.36], [114.49, 10.36], [114.49, 10.39], [114.46, 10.39], [114.46, 10.36]]],
        # Đảo Ba Bình (Itu Aba Island)
        [[[114.35, 10.36], [114.38, 10.36], [114.38, 10.39], [114.35, 10.39], [114.35, 10.36]]],
        # Đảo Phan Vinh (Pearson Reef)
        [[[113.67, 8.95], [113.72, 8.95], [113.72, 9.00], [113.67, 9.00], [113.67, 8.95]]],
        # Đảo Thuyền Chài (Barque Canada Reef)
        [[[114.78, 8.15], [114.83, 8.15], [114.83, 8.20], [114.78, 8.20], [114.78, 8.15]]],
        # Đảo An Bang (Amboyna Cay)
        [[[112.89, 7.87], [112.93, 7.87], [112.93, 7.90], [112.89, 7.90], [112.89, 7.87]]],
        # Đảo Trường Sa Đông (Central London Reef)
        [[[112.33, 8.90], [112.38, 8.90], [112.38, 8.94], [112.33, 8.94], [112.33, 8.90]]],
        # Đảo Nam Vinh & Cô Lin
        [[[114.21, 9.82], [114.25, 9.82], [114.25, 9.86], [114.21, 9.86], [114.21, 9.82]]]
    ]

    features.append({
        "type": "Feature",
        "properties": {
            "name": "Quần đảo Trường Sa (Tỉnh Khánh Hòa, Việt Nam)",
            "name_en": "Spratly Islands (Khanh Hoa, Vietnam)",
            "type": "archipelago",
            "sovereignty": "Vietnam",
            "jurisdiction": "Tỉnh Khánh Hòa",
            "center": [114.0, 9.5]
        },
        "geometry": {
            "type": "MultiPolygon",
            "coordinates": truong_sa_islands
        }
    })

    # 4. Maritime Boundary Anchor Buffer & Toponyms
    territory_geojson = {
        "type": "FeatureCollection",
        "name": "Vietnam_National_Territory_Sovereign",
        "crs": {
            "type": "name",
            "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" }
        },
        "metadata": {
            "sovereignty": "Nước Cộng hòa Xã hội Chủ nghĩa Việt Nam",
            "statutory_reference": "Luật Biển Việt Nam 2012 / Hiến pháp 2013",
            "archipelagos": ["Quần đảo Hoàng Sa", "Quần đảo Trường Sa"],
            "major_islands": ["Phú Quốc", "Côn Đảo", "Phú Quý", "Lý Sơn", "Bạch Long Vĩ"]
        },
        "features": features
    }

    # Write raw and gzip files
    raw_path = OUTPUT_DIR / "vietnam_territory.json"
    gz_path = OUTPUT_DIR / "vietnam_territory.json.gz"

    raw_json_str = json.dumps(territory_geojson, ensure_ascii=False, separators=(',', ':'))
    raw_bytes = raw_json_str.encode('utf-8')
    gz_bytes = gzip.compress(raw_bytes, compresslevel=9)

    with open(raw_path, 'w', encoding='utf-8') as f:
        f.write(raw_json_str)

    with open(gz_path, 'wb') as f:
        f.write(gz_bytes)

    print(f"Generated {raw_path} ({len(raw_bytes)/1024:.1f} KB, GZ: {len(gz_bytes)/1024:.1f} KB)")
    print("Features included: Mainland + Hoang Sa Archipelago + Truong Sa Archipelago")

if __name__ == "__main__":
    build_vietnam_territory()
