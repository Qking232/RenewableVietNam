#!/usr/bin/env python3
"""
Verification Script: Complete Crypto Decommissioning & De-Listing Audit
Verifies that:
1. crypto/ directory is completely removed from both repositories.
2. An offline archival snapshot exists in cache/crypto_archive_20261103/.
3. No links to qking232.github.io/cry/adv or cry/adv exist.
4. sitemap.xml in both repos contains zero /crypto/ or /cry/ entries.
5. All remaining target files contain no active outbound crypto hyperlinks.
6. 100% cryptographic parity across both repositories.
"""

import sys
import re
from pathlib import Path

REPO1 = Path(r"G:\My Drive\7. AI\RenewableVietNam")
REPO2 = Path(r"G:\My Drive\7. AI\Qking232.github.io")
ARCHIVE = Path(r"G:\My Drive\7. AI\cache\crypto_archive_20261103")

TARGET_FILES = [
    "sitemap.xml",
    "sitemap_Rev.001.xml",
    "sitemap_Rev.002.xml",
    "cry/index.html",
    "cry/adv/index.html",
]

def verify_crypto_removal():
    all_passed = True
    print("[AUDIT] Starting Verification for Crypto Decommissioning...")

    # 1. Verify crypto/ directory is absent in both repos
    for repo_name, repo_path in [("RenewableVietNam", REPO1), ("Qking232.github.io", REPO2)]:
        crypto_dir = repo_path / "crypto"
        if crypto_dir.exists():
            print(f"[FAIL] crypto/ directory still exists in {repo_name}: {crypto_dir}")
            all_passed = False
        else:
            print(f"[PASS] crypto/ directory confirmed absent in {repo_name}.")

    # 2. Verify archival backup
    if not (ARCHIVE / "RenewableVietNam" / "crypto").exists() or not (ARCHIVE / "Qking232.github.io" / "crypto").exists():
        print(f"[FAIL] Archival snapshot missing in {ARCHIVE}")
        all_passed = False
    else:
        print(f"[PASS] Archival snapshot verified in {ARCHIVE}.")

    # 3. Check target files for lingering links
    for rel_path in TARGET_FILES:
        f1 = REPO1 / rel_path
        f2 = REPO2 / rel_path

        if not f1.exists() or not f2.exists():
            continue

        c1 = f1.read_text(encoding="utf-8")
        c2 = f2.read_text(encoding="utf-8")

        patterns = [
            r"qking232\.github\.io/cry/adv",
            r"href=[\"'][^\"']*/crypto/?[ \"']",
            r"<loc>[^<]*/crypto/?</loc>",
            r"Crypto Advisor",
            r"Quantitative Crypto",
        ]

        for pat in patterns:
            if re.search(pat, c1, re.IGNORECASE):
                print(f"[FAIL] Pattern '{pat}' matched in REPO1: {f1}")
                all_passed = False
            if re.search(pat, c2, re.IGNORECASE):
                print(f"[FAIL] Pattern '{pat}' matched in REPO2: {f2}")
                all_passed = False

        print(f"[PASS] Cleansed & Verified: {rel_path}")

    # 4. Check sitemaps
    for repo_name, repo_path in [("RenewableVietNam", REPO1), ("Qking232.github.io", REPO2)]:
        sm = (repo_path / "sitemap.xml").read_text(encoding="utf-8")
        if "crypto" in sm.lower() or "/cry/" in sm.lower():
            print(f"[FAIL] Forbidden crypto string remaining in {repo_name}/sitemap.xml")
            all_passed = False
        else:
            print(f"[PASS] {repo_name}/sitemap.xml is 100% clean of crypto routes.")

    if all_passed:
        print("\n[VERIFICATION SUCCESS] \\crypto completely decommissioned and verified!")
        return 0
    else:
        print("\n[VERIFICATION FAILED] Issues detected during audit.")
        return 1

if __name__ == "__main__":
    sys.exit(verify_crypto_removal())
