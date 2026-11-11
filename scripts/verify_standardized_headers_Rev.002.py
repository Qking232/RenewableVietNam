#!/usr/bin/env python3
"""
Verify Unified Sleek 52px Glass Header Shell, Light-Default Theme Cookie,
and Pre-Paint Head Optimization across RenewableVietNam & Qking232.github.io - Rev.002.
"""

import hashlib
import os
import re
import sys

REPO1 = r"G:\My Drive\7. AI\RenewableVietNam"
REPO2 = r"G:\My Drive\7. AI\Qking232.github.io"

R1_TARGETS = [
    "index.html",
    "energy/index.html",
    "projectenergy/index.html",
    "industrial/index.html",
    "industrial/calculator/index.html",
    "evcharging/index.html",
    "invm/index.html",
    "invm/quyhoach/index.html",
    "project/index.html",
    "project/dc/index.html",
    "project/garments/index.html",
    "dc/index.html",
    "garments/index.html",
    "livewire/index.html",
    "roadmap/index.html",
]

R2_TARGETS = [
    "index.html",
    "energy/index.html",
    "projectenergy/index.html",
    "industrial/index.html",
    "industrial/calculator/index.html",
    "evcharging/index.html",
    "invm/index.html",
    "invm/quyhoach/index.html",
    "project/index.html",
    "dc/index.html",
    "livewire/index.html",
    "roadmap/index.html",
    "calculator/index.html",
]

SHARED_ASSETS = [
    "assets/built/rvn-shell.css",
    "assets/js/rvn-header.js",
    "assets/images/logo.svg",
]

FORBIDDEN_URLS = [
    'href="https://invest.',
    'href="https://ind.',
    'href="https://ev.',
    'invest.renewablevietnam.com',
    '/assets/css/rvn-header',
]


def audit_file(repo_path, rel):
    fpath = os.path.join(repo_path, rel)
    errs = []
    if not os.path.exists(fpath):
        return [f"Missing file {fpath}"]
    txt = open(fpath, "r", encoding="utf-8").read()
    head_end = txt.find("</head>")
    if head_end == -1:
        return ["Missing </head>"]
    head = txt[:head_end]
    body = txt[head_end:]

    if 'id="rvn-prepaint-theme"' not in head:
        errs.append("Missing #rvn-prepaint-theme in <head>")
    if "t === 'dark'" not in head:
        errs.append("Missing light-default cookie guard (t === 'dark') in #rvn-prepaint-theme")
    if '/assets/built/rvn-shell.css?v=1' not in head:
        errs.append("Missing /assets/built/rvn-shell.css?v=1 in <head>")

    html_m = re.search(r'<html\b[^>]*>', head, re.IGNORECASE)
    if html_m and re.search(r'\bdark\b', html_m.group(0)):
        errs.append(f"Hardcoded dark class on <html>: {html_m.group(0)}")

    if "window.location.replace(" in head:
        errs.append("Legacy blocking window.location.replace() still present in <head>")

    cdn_m = re.search(r'src="https://cdn\.tailwindcss\.com"', head)
    cfg_m = re.search(r'tailwind\.config\s*=', head)
    if cfg_m and cdn_m and cfg_m.start() < cdn_m.start():
        errs.append("Tailwind CDN ordering bug: tailwind.config precedes cdn.tailwindcss.com")

    headers = re.findall(r'<header\b[^>]*>', body, re.IGNORECASE)
    if len(headers) != 1 or 'id="rvn-header"' not in headers[0]:
        errs.append(f"Expected single <header id=\"rvn-header\">, found: {headers}")

    if '<script src="/assets/js/rvn-header.js?v=1"></script>' not in body:
        errs.append("Missing /assets/js/rvn-header.js?v=1")

    if "Edge Gateways Live" in body:
        errs.append("Legacy Edge Gateways Live badge still in body")

    if re.search(r"theme(?:Toggle)?Btn\??\.addEventListener\(['\"]click", body):
        errs.append("Legacy duplicate #themeToggleBtn click listener still present in body")

    for bad in FORBIDDEN_URLS:
        if bad in txt:
            errs.append(f"Forbidden legacy string found: {bad}")

    return errs


def sha256(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def main():
    ok = True
    print("=== AUDIT 1: SHARED SHELL ASSETS & REPO PARITY ===")
    for rel in SHARED_ASSETS:
        p1 = os.path.join(REPO1, rel)
        p2 = os.path.join(REPO2, rel)
        if not (os.path.exists(p1) and os.path.exists(p2)):
            print(f"  [FAIL] {rel}: missing in R1 or R2")
            ok = False
            continue
        h1, h2 = sha256(p1), sha256(p2)
        if h1 == h2:
            print(f"  [PASS] {rel:30} sha256={h1[:12]} (size={os.path.getsize(p1)}B)")
        else:
            print(f"  [FAIL] {rel:30} parity mismatch R1={h1[:12]} R2={h2[:12]}")
            ok = False

    for name, repo, files in [
        ("RenewableVietNam", REPO1, R1_TARGETS),
        ("Qking232.github.io", REPO2, R2_TARGETS),
    ]:
        print(f"\n=== AUDIT 2: {name} ({len(files)} targets) ===")
        for rel in files:
            errs = audit_file(repo, rel)
            if not errs:
                print(f"  [PASS] {rel}")
            else:
                ok = False
                print(f"  [FAIL] {rel}")
                for e in errs:
                    print(f"         - {e}")

    # Confirm excluded routes remain untouched cleanly
    print("\n=== AUDIT 3: EXCLUDED ROUTES CHECK ===")
    for p in [
        os.path.join(REPO1, "evcharging/ev/index.html"),
        os.path.join(REPO2, "datacenter/index.html"),
        os.path.join(REPO2, "garments/index.html"),
    ]:
        txt = open(p, "r", encoding="utf-8").read()
        if "rvn-shell.css" not in txt and "rvn-header.js" not in txt:
            print(f"  [PASS] Excluded cleanly: {os.path.relpath(p, r'G:\My Drive\7. AI')}")
        else:
            ok = False
            print(f"  [FAIL] Excluded file unexpectedly modified: {p}")

    print("\nRESULT:", "ALL AUDITS PASSED" if ok else "AUDIT FAILED")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
