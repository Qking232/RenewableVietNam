#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate optimized JSON and GZIP streaming payloads for Vietnam National Electrical Grid
from Grid_Model_Vietnam.sqlite into RenewableVietNam/data.
"""

import os
import sys
import json
import gzip
import sqlite3
from pathlib import Path

DB_PATH = Path(r"c:\Users\Quan\Downloads\GridTwinVN\GridTwinVN\database\Grid_Model_Vietnam.sqlite")
if not DB_PATH.exists():
    DB_PATH = Path(r"G:\My Drive\7. AI\RenewableVietNam\data\grid_twin\Grid_Model_Vietnam.sqlite")

OUTPUT_DIR = Path(r"G:\My Drive\7. AI\RenewableVietNam\data")

def export_payloads():
    if not DB_PATH.exists():
        raise FileNotFoundError(f"Database not found at {DB_PATH}")

    print(f"Connecting to SQLite database: {DB_PATH}")
    conn = sqlite3.connect(str(DB_PATH))
    cur = conn.cursor()

    # 1. Substations Payload
    print("Exporting substations payload...")
    cur.execute("""
    SELECT 
        s.id, s.name, s.geo_lat, s.geo_lng, s.place, s.kind, s.bay_codes, s.geo_source, s.dashed_2025,
        GROUP_CONCAT(DISTINCT CAST(vl.nominal_v AS TEXT)) as voltages,
        COUNT(DISTINCT tx.id) as tx_count,
        ROUND(SUM(tx.rated_s), 1) as total_tx_mva,
        COUNT(DISTINCT g.id) as gen_count,
        ROUND(SUM(g.max_p), 1) as total_gen_mw
    FROM substations s
    LEFT JOIN voltage_levels vl ON s.id = vl.substation_id
    LEFT JOIN two_windings_transformers tx ON s.id = tx.substation_id
    LEFT JOIN generators g ON s.id = g.substation_id
    GROUP BY s.id
    ORDER BY s.name ASC
    """)

    substations = []
    sub_by_v = {}
    for r in cur.fetchall():
        v_list = []
        if r[9]:
            for v_str in r[9].split(','):
                try:
                    v_list.append(int(float(v_str)))
                except (ValueError, TypeError):
                    pass
        v_list = sorted(list(set(v_list)), reverse=True)
        max_v = v_list[0] if v_list else 110

        sub_by_v[max_v] = sub_by_v.get(max_v, 0) + 1

        substations.append({
            "id": r[0],
            "name": r[1],
            "lat": round(r[2], 5) if r[2] is not None else None,
            "lng": round(r[3], 5) if r[3] is not None else None,
            "place": r[4],
            "kind": r[5],
            "bay_codes": r[6],
            "geo_src": r[7],
            "dashed": bool(r[8]),
            "voltages": v_list,
            "max_v": max_v,
            "tx_count": r[10] or 0,
            "total_tx_mva": r[11] or 0.0,
            "gen_count": r[12] or 0,
            "total_gen_mw": r[13] or 0.0
        })

    # 2. Transmission Lines Payload
    print("Exporting transmission lines payload...")
    cur.execute("""
    SELECT 
        l.id, l.v_kv, l.conductor, l.r, l.x, l.length_km_est, l.dashed_2025,
        l.substation_id_1, l.substation_name_1, s1.geo_lat, s1.geo_lng,
        l.substation_id_2, l.substation_name_2, s2.geo_lat, s2.geo_lng
    FROM transmission_lines l
    LEFT JOIN substations s1 ON l.substation_id_1 = s1.id
    LEFT JOIN substations s2 ON l.substation_id_2 = s2.id
    ORDER BY l.v_kv DESC, l.id ASC
    """)

    lines = []
    km_by_v = {}
    lines_by_v = {}
    total_km = 0.0

    for r in cur.fetchall():
        v_kv = int(r[1]) if r[1] is not None else 110
        length_km = round(r[5], 1) if r[5] is not None else 0.0
        total_km += length_km

        km_by_v[v_kv] = round(km_by_v.get(v_kv, 0.0) + length_km, 1)
        lines_by_v[v_kv] = lines_by_v.get(v_kv, 0) + 1

        coords = None
        if r[9] is not None and r[10] is not None and r[13] is not None and r[14] is not None:
            coords = [
                [round(r[10], 5), round(r[9], 5)],
                [round(r[14], 5), round(r[13], 5)]
            ]

        lines.append({
            "id": r[0],
            "v_kv": v_kv,
            "conductor": r[2],
            "r": round(r[3], 4) if r[3] is not None else None,
            "x": round(r[4], 4) if r[4] is not None else None,
            "len_km": length_km,
            "dashed": bool(r[6]),
            "s1_id": r[7],
            "s1_name": r[8],
            "s2_id": r[11],
            "s2_name": r[12],
            "coords": coords
        })

    # 3. Summary Payload
    print("Computing national grid statistics...")
    cur.execute("SELECT COUNT(*), ROUND(SUM(rated_s), 1) FROM two_windings_transformers")
    tx_total_count, tx_total_mva = cur.fetchone()

    cur.execute("SELECT COUNT(*), ROUND(SUM(max_p), 1) FROM generators")
    gen_total_count, gen_total_mw = cur.fetchone()

    summary = {
        "timestamp": "2026-11-03T09:00:00Z",
        "model_source": "NSMO Grid Model Vietnam 2025 (Decision 500/QĐ-TTg Reference)",
        "substations": {
            "total": len(substations),
            "georeferenced": sum(1 for s in substations if s["lat"] is not None and s["lng"] is not None),
            "by_voltage": sub_by_v
        },
        "lines": {
            "total": len(lines),
            "georeferenced": sum(1 for l in lines if l["coords"] is not None),
            "total_km": round(total_km, 1),
            "by_voltage_count": lines_by_v,
            "by_voltage_km": km_by_v
        },
        "transformers": {
            "total_count": tx_total_count,
            "total_mva": tx_total_mva or 0.0
        },
        "generators": {
            "total_count": gen_total_count,
            "total_mw": gen_total_mw or 0.0
        }
    }

    conn.close()

    # Write files with compression
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    files_to_write = [
        ("vietnam_grid_substations.json", substations),
        ("vietnam_grid_lines.json", lines),
        ("vietnam_grid_summary.json", summary),
    ]

    for filename, data_obj in files_to_write:
        raw_path = OUTPUT_DIR / filename
        gz_path = OUTPUT_DIR / f"{filename}.gz"

        raw_str = json.dumps(data_obj, ensure_ascii=False, separators=(',', ':'))
        raw_bytes = raw_str.encode("utf-8")
        gz_bytes = gzip.compress(raw_bytes, compresslevel=9)

        with open(raw_path, "w", encoding="utf-8") as f:
            f.write(raw_str)

        with open(gz_path, "wb") as f:
            f.write(gz_bytes)

        print(f"Generated {filename}: Raw {len(raw_bytes)/1024:.1f} KB -> GZ {len(gz_bytes)/1024:.1f} KB")

    print("\nGrid web payload generation complete.")

if __name__ == "__main__":
    export_payloads()
