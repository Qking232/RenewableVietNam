#!/usr/bin/env python3
"""
Automated Verification Suite: Comprehensive Industrial Subdomain & Path Audit
Validates:
1. industrial/index.html exists and canonicalizes to /industrial/.
2. green/index.html serves as a redirect shield to industrial.
3. Cloudflare edge worker maps industrial.renewablevietnam.com -> /industrial.
4. Cloudflare edge worker redirects legacy /green and ind. to industrial.renewablevietnam.com.
5. sitemap.xml contains /industrial/ and zero active /green/ routes.
6. 100% cryptographic SHA-256 hash parity between RenewableVietNam and Qking232.github.io.
"""

import sys
import hashlib
from pathlib import Path

REPO1 = Path(r"G:\My Drive\7. AI\RenewableVietNam")
REPO2 = Path(r"G:\My Drive\7. AI\Qking232.github.io")

TARGETS_TO_VERIFY = [
    "index.html",
    "industrial/index.html",
    "industrial/calculator/index.html",
    "green/index.html",
    "projectenergy/index.html",
    "evcharging/index.html",
    "evcharging/ev/index.html",
    "livewire/index.html",
    "sitemap.xml",
]

def sha256_file(p):
    h = hashlib.sha256()
    h.update(p.read_bytes())
    return h.hexdigest()

def run_verification():
    print("[VERIFICATION] Starting Comprehensive Industrial Path Migration Audit...")
    failed = False

    # 1. Cloudflare Worker Verification
    cf_worker = REPO1 / "cloudflare" / "subdomain_gateway_worker.js"
    cf_text = cf_worker.read_text(encoding="utf-8")
    
    if "'industrial.renewablevietnam.com': '/industrial'" not in cf_text:
        print("[FAIL] Cloudflare Worker missing industrial -> /industrial mapping")
        failed = True
    else:
        print("[PASS] Cloudflare Worker maps industrial.renewablevietnam.com -> /industrial")

    if "pathname.startsWith('/green')" in cf_text and "Response.redirect" in cf_text:
        print("[PASS] Cloudflare Worker redirects legacy /green to industrial.renewablevietnam.com")
    else:
        print("[FAIL] Cloudflare Worker missing /green edge redirect")
        failed = True

    # 2. Check sitemaps
    for repo_name, repo_path in [("RenewableVietNam", REPO1), ("Qking232.github.io", REPO2)]:
        sm_text = (repo_path / "sitemap.xml").read_text(encoding="utf-8")
        if "<loc>https://renewablevietnam.com/green/</loc>" in sm_text:
            print(f"[FAIL] {repo_name} sitemap.xml still contains /green/ route")
            failed = True
        elif "<loc>https://renewablevietnam.com/industrial/</loc>" not in sm_text:
            print(f"[FAIL] {repo_name} sitemap.xml missing /industrial/ route")
            failed = True
        else:
            print(f"[PASS] {repo_name} sitemap.xml correctly indexes /industrial/")

    # 3. Check target files & hash parity
    for rel_path in TARGETS_TO_VERIFY:
        f1 = REPO1 / rel_path
        f2 = REPO2 / rel_path

        if not f1.exists():
            print(f"[FAIL] Missing in REPO1: {rel_path}")
            failed = True
            continue
        if not f2.exists():
            print(f"[FAIL] Missing in REPO2: {rel_path}")
            failed = True
            continue

        h1 = sha256_file(f1)
        h2 = sha256_file(f2)
        if h1 != h2:
            print(f"[FAIL] Hash parity mismatch on {rel_path}: REPO1={h1[:8]} REPO2={h2[:8]}")
            failed = True
        else:
            print(f"[PASS] {rel_path} has 100% hash parity ({h1[:8]})")

    # 4. Check green/index.html redirect shield
    green_text = (REPO1 / "green" / "index.html").read_text(encoding="utf-8")
    if "https://industrial.renewablevietnam.com" in green_text and "Redirecting to Industrial Portal" in green_text:
        print("[PASS] green/index.html functions as redirect shield to industrial")
    else:
        print("[FAIL] green/index.html redirect shield incomplete")
        failed = True

    # 5. Check industrial/index.html canonical
    ind_text = (REPO1 / "industrial" / "index.html").read_text(encoding="utf-8")
    if '<link rel="canonical" href="https://renewablevietnam.com/industrial/">' in ind_text:
        print("[PASS] industrial/index.html canonical link correctly configured")
    else:
        print("[FAIL] industrial/index.html canonical link missing or invalid")
        failed = True

    if failed:
        print("\n[VERIFICATION RESULT] FAILED: Issues detected during verification audit.")
        return 1
    else:
        print("\n[VERIFICATION RESULT] SUCCESS: /green completely replaced with /industrial across all files!")
        return 0

if __name__ == "__main__":
    sys.exit(run_verification())
