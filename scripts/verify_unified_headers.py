"""
Rigorous automated verification script for Unified Institutional Header deployment.
"""
import os
import sys

REPO1 = "G:/My Drive/7. AI/Gemini/RenewableVietNam"
REPO2 = "G:/My Drive/7. AI/Gemini/Qking232.github.io"

def verify_page_header(filepath, active_key, extra_checks=None):
    if not os.path.exists(filepath):
        print(f"[FAIL] Missing {filepath}")
        return False
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    base_checks = [
        ("Logo SVG", "logo.svg"),
        ("Brand Text", "RENEWABLE INFRASTRUCTURE"),
        ("Nav Industrial Hubs", 'href="/"'),
        ("Nav Energy Map", 'href="/projectenergy/"'),
        ("Nav EV Stations", 'href="/evcharging/"'),
        ("Nav Power Sizer", 'href="/calculator/"'),
        ("Nav The Library", 'href="/hub/"'),
        ("Live Wire CTA", "Live Wire"),
        ("Mobile Carousel", "no-scrollbar")
    ]

    active_markers = {
        'hubs': 'href="/" class="px-2.5 py-1 rounded-md text-white font-semibold bg-white/10 border border-white/40 shadow-sm transition-all">Industrial Hubs</a>',
        'energy': 'href="/projectenergy/" class="px-2.5 py-1 rounded-md text-white font-semibold bg-white/10 border border-white/40 shadow-sm transition-all">Energy Map</a>',
        'ev': 'href="/evcharging/" class="px-2.5 py-1 rounded-md text-white font-semibold bg-white/10 border border-white/40 shadow-sm transition-all">EV Stations</a>',
        'calc': 'href="/calculator/" class="px-2.5 py-1 rounded-md text-white font-semibold bg-white/10 border border-white/40 shadow-sm transition-all">Power Sizer &amp; Tariffs</a>',
        'hub': 'href="/hub/" class="px-2.5 py-1 rounded-md text-white font-semibold bg-white/10 border border-white/40 shadow-sm transition-all">The Library</a>'
    }

    if active_key in active_markers:
        base_checks.append((f"Active Route Pill ({active_key})", active_markers[active_key]))

    if extra_checks:
        base_checks.extend(extra_checks)

    all_ok = True
    rel = os.path.relpath(filepath, "G:/My Drive/7. AI/Gemini")
    for desc, pattern in base_checks:
        if pattern not in content:
            print(f"[FAIL] {rel}: Missing '{desc}'")
            all_ok = False
        else:
            print(f"[OK] {rel}: Found '{desc}'")
    return all_ok

def check_parity(rel_file):
    p1 = os.path.join(REPO1, rel_file)
    p2 = os.path.join(REPO2, rel_file)
    if not os.path.exists(p1) or not os.path.exists(p2):
        print(f"[FAIL] Parity check failed, file missing: {p1} or {p2}")
        return False
    with open(p1, "r", encoding="utf-8") as f1, open(p2, "r", encoding="utf-8") as f2:
        c1 = f1.read()
        c2 = f2.read()
    if c1 == c2:
        print(f"[OK] 100% PARITY for {rel_file}")
        return True
    else:
        print(f"[FAIL] Parity mismatch for {rel_file}: {len(c1)} vs {len(c2)} bytes")
        return False

def main():
    print("=== 1. Auditing RenewableVietNam Headers ===")
    ok = True
    ok &= verify_page_header(os.path.join(REPO1, "index.html"), 'hubs', [("Theme Toggle", 'id="themeToggleBtn"')])
    ok &= verify_page_header(os.path.join(REPO1, "projectenergy", "index.html"), 'energy', [("Lang EN", 'id="btn-lang-en"'), ("Lang VI", 'id="btn-lang-vi"')])
    ok &= verify_page_header(os.path.join(REPO1, "evcharging", "index.html"), 'ev', [("Sidebar Toggle", 'id="toggleSide"'), ("Theme Btn", 'id="themeBtn"')])
    ok &= verify_page_header(os.path.join(REPO1, "_src", "hub_source_v0.63.html"), 'hub', [("Sign Up", 'id="keyBtn"'), ("Theme Btn", 'id="themeBtn"')])
    ok &= verify_page_header(os.path.join(REPO1, "calculator", "index.html"), 'calc', [("Theme Toggle", 'id="themeToggleBtn"')])

    print("\n=== 2. Auditing Qking232.github.io Headers ===")
    ok &= verify_page_header(os.path.join(REPO2, "index.html"), 'hubs')
    ok &= verify_page_header(os.path.join(REPO2, "projectenergy", "index.html"), 'energy')
    ok &= verify_page_header(os.path.join(REPO2, "evcharging", "index.html"), 'ev')
    ok &= verify_page_header(os.path.join(REPO2, "calculator", "index.html"), 'calc')

    print("\n=== 3. Auditing Multi-Repo Parity ===")
    ok &= check_parity("index.html")
    ok &= check_parity(os.path.join("green", "index.html"))
    ok &= check_parity(os.path.join("projectenergy", "index.html"))
    ok &= check_parity(os.path.join("evcharging", "index.html"))
    ok &= check_parity(os.path.join("calculator", "index.html"))
    ok &= check_parity(os.path.join("green", "calculator", "index.html"))
    ok &= check_parity(os.path.join("hub", "index.html"))

    if ok:
        print("\n>>> ALL UNIFIED INSTITUTIONAL HEADER AUDITS PASSED 100% <<<")
        sys.exit(0)
    else:
        print("\n>>> AUDIT FAILED <<<")
        sys.exit(1)

if __name__ == "__main__":
    main()
