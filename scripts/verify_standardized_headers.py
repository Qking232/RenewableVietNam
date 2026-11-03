import os
import re

REPO = r"G:\My Drive\7. AI\RenewableVietNam"
FILES = [
    "index.html",
    "projectenergy/index.html",
    "industrial/index.html",
    "industrial/calculator/index.html",
    "evcharging/index.html",
    "evcharging/ev/index.html",
    "livewire/index.html",
    "project/index.html",
    "invm/index.html"
]

REQUIRED_SUBSTRINGS = [
    "RENEWABLE VIETNAM",
    "https://renewablevietnam.com/",
    "https://energy.renewablevietnam.com/",
    "https://industrial.renewablevietnam.com/",
    "https://ev.renewablevietnam.com/",
    "https://legal.renewablevietnam.com/",
    "4 Edge Gateways Live",
]

FORBIDDEN_SUBSTRINGS = [
    "https://legal.renewablevietnam.com/hub",
    "https://invest.renewablevietnam.com",
    "https://ind.renewablevietnam.com",
    "href=\"/green",
    "href=\"https://renewablevietnam.com/green"
]

all_pass = True
print("=== VERIFYING STANDARDIZED HEADER ON ALL PAGES ===")

for rel in FILES:
    fpath = os.path.join(REPO, rel)
    with open(fpath, "r", encoding="utf-8") as fp:
        c = fp.read()

    missing = [req for req in REQUIRED_SUBSTRINGS if req not in c]
    forbidden_found = [f for f in FORBIDDEN_SUBSTRINGS if f in c]

    if not missing and not forbidden_found:
        print(f"[PASS] {rel:35} -> All header components & links validated")
    else:
        print(f"[FAIL] {rel:35}")
        if missing:
            print(f"       Missing: {missing}")
        if forbidden_found:
            print(f"       Forbidden found: {forbidden_found}")
        all_pass = False

print("\nHEADER AUDIT RESULT:", "100% SUCCESS" if all_pass else "AUDIT FAILED")
