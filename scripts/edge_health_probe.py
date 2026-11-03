#!/usr/bin/env python3
"""
==============================================================================
Vietnam Clean Energy Platform: Multi-Domain Edge Health Probe & Audit Utility
Platform: Renewable Viet Nam (renewablevietnam.com)
Zone ID: eed02d9917c1a0c6144972136e836eba
==============================================================================
"""

import sys
import time
import json
import urllib.request
import urllib.error

ENDPOINTS = [
    {"name": "Apex Cockpit", "url": "https://renewablevietnam.com/", "expected_status": 200},
    {"name": "Energy Portal", "url": "https://energy.renewablevietnam.com/", "expected_status": 200},
    {"name": "Industrial Portal", "url": "https://industrial.renewablevietnam.com/", "expected_status": 200},
    {"name": "EV Tech Portal", "url": "https://ev.renewablevietnam.com/", "expected_status": 200},
    {"name": "Legal & M&A Portal", "url": "https://legal.renewablevietnam.com/", "expected_status": 200},
    {"name": "Project Delivery", "url": "https://project.renewablevietnam.com/", "expected_status": 200},
    {"name": "Roadmap Radar", "url": "https://renewablevietnam.com/roadmap/", "expected_status": 200}
]

def probe_url(target):
    url = target["url"]
    name = target["name"]
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) RenewableVietNam-Probe/1.0"}
    )
    start_time = time.time()
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            elapsed_ms = round((time.time() - start_time) * 1000, 1)
            content = resp.read()
            status = resp.status
            cf_ray = resp.headers.get("cf-ray", "N/A")
            cf_cache = resp.headers.get("cf-cache-status", "DYNAMIC")
            return {
                "name": name,
                "url": url,
                "status": status,
                "ok": (status == target["expected_status"]),
                "latency_ms": elapsed_ms,
                "bytes": len(content),
                "cf_ray": cf_ray,
                "cf_cache": cf_cache,
                "error": None
            }
    except urllib.error.HTTPError as e:
        elapsed_ms = round((time.time() - start_time) * 1000, 1)
        return {
            "name": name,
            "url": url,
            "status": e.code,
            "ok": False,
            "latency_ms": elapsed_ms,
            "bytes": 0,
            "cf_ray": e.headers.get("cf-ray", "N/A"),
            "cf_cache": e.headers.get("cf-cache-status", "N/A"),
            "error": str(e)
        }
    except Exception as e:
        elapsed_ms = round((time.time() - start_time) * 1000, 1)
        return {
            "name": name,
            "url": url,
            "status": 0,
            "ok": False,
            "latency_ms": elapsed_ms,
            "bytes": 0,
            "cf_ray": "N/A",
            "cf_cache": "N/A",
            "error": str(e)
        }

def main():
    json_mode = "--json" in sys.argv
    results = []
    all_ok = True

    if not json_mode:
        print("=" * 80)
        print("RENEWABLE VIET NAM: MULTI-GATEWAY EDGE HEALTH PROBE MATRIX")
        print("=" * 80)
        print(f"{'GATEWAY NAME':<22} | {'STATUS':<10} | {'LATENCY':<10} | {'BYTES':<10} | {'CF-CACHE'}")
        print("-" * 80)

    for ep in ENDPOINTS:
        res = probe_url(ep)
        results.append(res)
        if not res["ok"]:
            all_ok = False
        if not json_mode:
            status_str = f"HTTP {res['status']}" if res['status'] else "ERR"
            ok_mark = "[OK]" if res["ok"] else "[FAIL]"
            print(f"{res['name']:<22} | {status_str:<10} | {str(res['latency_ms']) + 'ms':<10} | {str(res['bytes']) + 'B':<10} | {res['cf_cache']} {ok_mark}")

    if not json_mode:
        print("=" * 80)
        total_endpoints = len(results)
        passed = sum(1 for r in results if r["ok"])
        print(f"Audit Summary: {passed}/{total_endpoints} Gateways Operational (All OK: {all_ok})")
        print("=" * 80)

    if json_mode:
        print(json.dumps({"all_ok": all_ok, "results": results}, indent=2))

    sys.exit(0 if all_ok else 1)

if __name__ == "__main__":
    main()
