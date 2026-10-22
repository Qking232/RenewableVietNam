import os

files = [
    r"G:\My Drive\7. AI\Gemini\RenewableVietNam\index.html",
    r"G:\My Drive\7. AI\Gemini\RenewableVietNam\green\index.html",
    r"G:\My Drive\7. AI\Gemini\Qking232.github.io\index.html",
    r"G:\My Drive\7. AI\Gemini\Qking232.github.io\green\index.html"
]

required_ids = [
    "tabCorporateSizerBtn",
    "tabEvnEstimatorBtn",
    "tabGreenIndicatorBtn",
    "corporateSizerContainer",
    "evnEstimatorContainer",
    "greenIndicatorContainer",
    "greenSectorSelect",
    "greenMwhSlider",
    "greenReSlider",
    "greenEtsSlider",
    "greenBaselineCo2",
    "greenAbatedCo2",
    "greenCbamAvoidedEur",
    "greenIndexScore",
    "greenIndexRatingBadge",
    "copyGreenBriefBtn"
]

all_ok = True
for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    missing = [rid for rid in required_ids if f'id="{rid}"' not in content]
    has_fn = "function updateGreenIndicators" in content
    has_cit = "EU Regulation 2023/956" in content
    print(f"{fpath}:")
    print(f"  Length: {len(content)} bytes")
    print(f"  Missing IDs: {missing}")
    print(f"  Has Fn updateGreenIndicators: {has_fn}")
    print(f"  Has EU citations: {has_cit}")
    if missing or not has_fn or not has_cit:
        all_ok = False

if all_ok:
    print("\n[SUCCESS] 100% Verification across all 4 production files passed!")
else:
    print("\n[FAIL] Verification errors detected.")
    exit(1)
