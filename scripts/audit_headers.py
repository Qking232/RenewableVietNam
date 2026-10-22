import os
import re

REPO = r"G:\My Drive\7. AI\Gemini\RenewableVietNam"
pages = [
    "index.html",
    "green/index.html",
    "projectenergy/index.html",
    "evcharging/index.html",
    "calculator/index.html",
    "hub/index.html"
]

for p in pages:
    path = os.path.join(REPO, p)
    if not os.path.exists(path):
        print(f"Missing: {p}")
        continue
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()
    hdr = re.findall(r'<header[\s\S]*?</header>', c)
    body_match = re.search(r'<body[^>]*class="([^"]*)"', c)
    body_class = body_match.group(1) if body_match else ""
    has_toggle = 'themeToggleBtn' in c
    print(f"\n--- {p} ---")
    print(f"Body class: {body_class[:80]}...")
    print(f"Has theme toggle: {has_toggle}")
    if hdr:
        header_class = re.search(r'<header[^>]*class="([^"]*)"', hdr[0])
        print(f"Header class: {header_class.group(1) if header_class else ''}")
