import os

files = [
    r"G:\My Drive\7. AI\Gemini\RenewableVietNam\index.html",
    r"G:\My Drive\7. AI\Gemini\RenewableVietNam\green\index.html",
    r"G:\My Drive\7. AI\Gemini\Qking232.github.io\index.html",
    r"G:\My Drive\7. AI\Gemini\Qking232.github.io\green\index.html"
]

required_ids = [
    "toolsSidebar",
    "calculator",
    "tabCorporateSizerBtn",
    "tabEvnEstimatorBtn",
    "tabGreenIndicatorBtn",
    "corporateSizerContainer",
    "evnEstimatorContainer",
    "greenIndicatorContainer",
    "calcDemandSlider",
    "calcMwhSlider",
    "calcReSlider",
    "evnAcUnitsSlider",
    "greenSectorSelect",
    "greenMwhSlider",
    "marketWire",
    "hubs"
]

all_ok = True
for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    missing = [rid for rid in required_ids if f'id="{rid}"' not in content]
    has_aside = "<aside id=\"toolsSidebar\"" in content and "</aside>" in content
    has_main_7xl = 'max-w-7xl' in content
    main_open = content.count("<main")
    main_close = content.count("</main>")
    aside_open = content.count("<aside")
    aside_close = content.count("</aside>")

    print(f"{os.path.basename(fpath)}:")
    print(f"  Length: {len(content)} bytes")
    print(f"  Missing IDs: {missing}")
    print(f"  Has Aside: {has_aside} (Open: {aside_open}, Close: {aside_close})")
    print(f"  Main Tag Balance: Open {main_open}, Close {main_close}")
    print(f"  Has max-w-7xl: {has_main_7xl}")

    if missing or not has_aside or main_open != main_close or aside_open != aside_close:
        all_ok = False

if all_ok:
    print("\n[SUCCESS] 100% Verification passed across all files!")
else:
    print("\n[FAIL] Errors detected.")
    exit(1)
