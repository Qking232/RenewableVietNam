#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import time

for attempt in range(6):
    try:
        url = f"https://renewablevietnam.com/projectenergy/?cb={int(time.time())}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
        if 'mapToggleHeadroomBtn' in html and 'traceAssetInterconnection' in html:
            print(f"Verified live in attempt {attempt+1}! HTML length: {len(html)}")
            break
        else:
            print(f"Attempt {attempt+1}: Build still compiling (HTML length: {len(html)})...")
    except Exception as e:
        print(f"Attempt {attempt+1} error: {e}")
    time.sleep(10)
