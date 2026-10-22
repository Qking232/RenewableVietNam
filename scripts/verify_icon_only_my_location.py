import os
import re

files = [
    r"G:\My Drive\7. AI\Gemini\RenewableVietNam\evcharging\index.html",
    r"G:\My Drive\7. AI\Gemini\Qking232.github.io\evcharging\index.html"
]

all_ok = True
for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        c = f.read()

    # 1. Ensure btnMyLocation is NOT in gmChipsRow
    chips_match = re.search(r'<div class="gm-chips-row" id="gmChipsRow">(.*?)</div>', c, re.DOTALL)
    has_btn_in_chips = False
    if chips_match:
        has_btn_in_chips = 'id="btnMyLocation"' in chips_match.group(1)

    # 2. Extract mapBtnMyLocation element and check it has NO text
    btn_match = re.search(r'(<button class="map-loc-btn" id="mapBtnMyLocation"[^>]*>)(.*?)(</button>)', c, re.DOTALL)
    btn_inner = btn_match.group(2).strip() if btn_match else ""
    # Strip SVG and whitespace, check remaining text
    non_svg_text = re.sub(r'<svg[^>]*>.*?</svg>', '', btn_inner, flags=re.DOTALL).strip()

    has_fab = 'id="mapBtnMyLocation"' in c
    has_fab_css = 'right: 16px;\n    bottom: 32px;' in c or 'right: 16px;\r\n    bottom: 32px;' in c

    print(f"{os.path.basename(fpath)}:")
    print(f"  Length: {len(c)} bytes")
    print(f"  Has btnMyLocation in Chips: {has_btn_in_chips} (Expected: False)")
    print(f"  Has mapBtnMyLocation FAB: {has_fab} (Expected: True)")
    print(f"  Non-SVG Text in FAB: '{non_svg_text}' (Expected: empty)")
    print(f"  Has 16px/32px Bottom-Right CSS: {has_fab_css}")

    if has_btn_in_chips or not has_fab or non_svg_text != "" or not has_fab_css:
        all_ok = False

if all_ok:
    print("\n[SUCCESS] 100% Verification passed: 'My Location' is strictly an icon FAB at bottom-right with ZERO text!")
else:
    print("\n[FAIL] Verification errors.")
    exit(1)
