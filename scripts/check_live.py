#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import time

urls = [
    'https://renewablevietnam.com/projectenergy/',
    'https://energy.renewablevietnam.com/',
    'https://renewablevietnam.com/data/vietnam_grid_summary.json',
    'https://renewablevietnam.com/data/vietnam_grid_substations.json.gz',
    'https://renewablevietnam.com/data/vietnam_grid_lines.json.gz'
]

print("Polling live endpoints...")
for attempt in range(6):
    all_ok = True
    for u in urls:
        try:
            req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
            with urllib.request.urlopen(req, timeout=10) as resp:
                print(f"[OK {resp.status}] {u}")
        except Exception as e:
            all_ok = False
            print(f"[PENDING] {u} -> {e}")
    if all_ok:
        print("\nAll production endpoints are LIVE and verified!")
        break
    time.sleep(10)
