import os

files = [
    r"G:\My Drive\7. AI\Gemini\RenewableVietNam\evcharging\index.html",
    r"G:\My Drive\7. AI\Gemini\Qking232.github.io\evcharging\index.html"
]

required_strings = [
    'id="btnMyLocation"',
    'id="btnSelectLocation"',
    'id="mapBtnMyLocation"',
    'id="mapBtnSelectLocation"',
    'function triggerMyLocation',
    'function triggerSelectLocation',
    '.map-floating-location-controls'
]

all_ok = True
for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        c = f.read()
    missing = [s for s in required_strings if s not in c]
    print(f"{fpath} (Length: {len(c)} bytes): Missing: {missing}")
    if missing:
        all_ok = False

if all_ok:
    print("\n[SUCCESS] 100% Verification passed for EV Charging location controls!")
else:
    print("\n[FAIL] Errors detected.")
    exit(1)
