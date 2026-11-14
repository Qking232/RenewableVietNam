#!/usr/bin/env python3
"""
Renewable Viet Nam — Edge Health & Architecture v3.0 Polling Suite
Rev.001 (Automated Verification of Apex, Edge Subdomains, and Core Assets)
"""

import sys
import time
import urllib.request
import urllib.error

ENDPOINTS = [
    {
        "name": "Apex Cockpit Root",
        "url": "https://renewablevietnam.com/",
        "expected_status": [200],
        "allow_redirects": True
    },
    {
        "name": "M3 Expressive CSS Asset",
        "url": "https://renewablevietnam.com/assets/css/rvn_m3_expressive.css",
        "expected_status": [200],
        "allow_redirects": True
    },
    {
        "name": "Supabase Client Data Layer",
        "url": "https://renewablevietnam.com/assets/js/supabase-client.js",
        "expected_status": [200],
        "allow_redirects": True
    },
    {
        "name": "Unified Sleek Header M3 Controller",
        "url": "https://renewablevietnam.com/assets/js/rvn-header.js",
        "expected_status": [200],
        "allow_redirects": True
    },
    {
        "name": "CBAM & Solar Estimator Script",
        "url": "https://renewablevietnam.com/assets/js/cbam_solar_estimator.js",
        "expected_status": [200],
        "allow_redirects": True
    },
    {
        "name": "Industrial Calculator Index",
        "url": "https://renewablevietnam.com/industrial/calculator/index.html",
        "expected_status": [200],
        "allow_redirects": True
    },
    {
        "name": "Energy Edge Subdomain",
        "url": "https://energy.renewablevietnam.com/",
        "expected_status": [200],
        "allow_redirects": True
    },
    {
        "name": "Industrial Edge Subdomain",
        "url": "https://industrial.renewablevietnam.com/",
        "expected_status": [200],
        "allow_redirects": True
    },
    {
        "name": "Invest Subdomain (Canonical 301 Check)",
        "url": "https://invest.renewablevietnam.com/",
        "expected_status": [200, 301, 302],
        "allow_redirects": True
    },
    {
        "name": "EV Subdomain (Canonical 301 Check)",
        "url": "https://ev.renewablevietnam.com/",
        "expected_status": [200, 301, 302],
        "allow_redirects": True
    }
]

class NoRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

def test_endpoint(target):
    name = target["name"]
    url = target["url"]
    expected = target["expected_status"]
    allow_redirects = target.get("allow_redirects", True)

    opener = urllib.request.build_opener() if allow_redirects else urllib.request.build_opener(NoRedirectHandler)
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "RVN-Architecture-v3-Verifier/1.0 (+https://renewablevietnam.com)",
            "Accept": "*/*"
        }
    )

    t0 = time.time()
    try:
        with opener.open(req, timeout=10) as resp:
            dur = (time.time() - t0) * 1000.0
            status = resp.status
            content_type = resp.headers.get("Content-Type", "unknown")
            size = len(resp.read())
            passed = status in expected
            return {
                "name": name,
                "url": url,
                "status": status,
                "duration_ms": round(dur, 1),
                "content_type": content_type,
                "size_bytes": size,
                "passed": passed,
                "error": None
            }
    except urllib.error.HTTPError as e:
        dur = (time.time() - t0) * 1000.0
        passed = e.code in expected
        return {
            "name": name,
            "url": url,
            "status": e.code,
            "duration_ms": round(dur, 1),
            "content_type": e.headers.get("Content-Type", "unknown") if e.headers else "unknown",
            "size_bytes": 0,
            "passed": passed,
            "error": str(e) if not passed else None
        }
    except Exception as e:
        dur = (time.time() - t0) * 1000.0
        return {
            "name": name,
            "url": url,
            "status": 0,
            "duration_ms": round(dur, 1),
            "content_type": "none",
            "size_bytes": 0,
            "passed": False,
            "error": str(e)
        }

def main():
    print("=" * 80)
    print("Renewable Viet Nam — Edge Architecture v3.0 Production Health Audit")
    print("=" * 80)

    total = len(ENDPOINTS)
    passed_count = 0
    results = []

    for idx, target in enumerate(ENDPOINTS, 1):
        res = test_endpoint(target)
        results.append(res)
        status_flag = "PASS" if res["passed"] else "FAIL"
        if res["passed"]:
            passed_count += 1
        print(f"[{idx}/{total}] [{status_flag}] {res['name']}")
        print(f"      URL: {res['url']}")
        print(f"      Status: {res['status']} | Latency: {res['duration_ms']}ms | Size: {res['size_bytes']}B")
        if res["error"]:
            print(f"      Error: {res['error']}")
        print("-" * 80)

    success_rate = (passed_count / total) * 100.0
    print(f"Audit Summary: {passed_count}/{total} Passed ({success_rate:.1f}%)")
    print("=" * 80)

    if passed_count < total:
        print("[WARNING] One or more edge endpoints failed assertion.")
        return 1
    else:
        print("[SUCCESS] All Architecture v3.0 edge targets verified healthy.")
        return 0

if __name__ == "__main__":
    sys.exit(main())
