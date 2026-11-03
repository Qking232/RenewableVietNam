#!/usr/bin/env python3
import urllib.request
import urllib.error

tests = [
    ("https://industrial.renewablevietnam.com/", 200, "Industrial Hubs"),
    ("https://industrial.renewablevietnam.com/calculator/", 200, "DPPA"),
    ("https://ind.renewablevietnam.com/", 301, "https://industrial.renewablevietnam.com/"),
]

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

opener = urllib.request.build_opener(NoRedirect)

all_ok = True
print("=== LIVE EDGE ROUTING AUDIT ===")

for url, exp_status, check in tests:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 Edge/120.0"})
    try:
        try:
            resp = opener.open(req, timeout=10)
            status = resp.getcode()
            body = resp.read().decode("utf-8", errors="ignore")
            loc = resp.headers.get("Location", "")
        except urllib.error.HTTPError as e:
            status = e.code
            body = e.read().decode("utf-8", errors="ignore")
            loc = e.headers.get("Location", "")
        
        status_ok = (status == exp_status)
        if exp_status == 301:
            content_ok = check in loc
            detail = f"Location -> {loc}"
        else:
            content_ok = check.lower() in body.lower()
            detail = f"Matched keyword '{check}' in response body"
        
        passed = status_ok and content_ok
        mark = "[PASS]" if passed else "[FAIL]"
        print(f"{mark} {url} | HTTP {status} | {detail}")
        if not passed:
            all_ok = False
    except Exception as exc:
        print(f"[FAIL] {url} -> Exception: {exc}")
        all_ok = False

if all_ok:
    print("\n[AUDIT RESULT] 100% OPERATIONAL: industrial.renewablevietnam.com is fully live and functioning at the edge.")
else:
    print("\n[AUDIT RESULT] FAILED: Some endpoints did not return expected responses.")
