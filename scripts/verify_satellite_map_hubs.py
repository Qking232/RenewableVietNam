"""
Verification script confirming exclusive Satellite (Esri World Imagery) cartography
and 0 OpenStreetMap references across Industrial Hubs pages.
"""
import os
import sys

REPO1 = "G:/My Drive/7. AI/Gemini/RenewableVietNam"
REPO2 = "G:/My Drive/7. AI/Gemini/Qking232.github.io"

def verify_file(filepath):
    if not os.path.exists(filepath):
        print(f"[FAIL] Missing {filepath}")
        return False
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    rel = os.path.relpath(filepath, "G:/My Drive/7. AI/Gemini")
    all_ok = True

    # 1. Negative Checks (Must NOT be present)
    prohibited = [
        ("OpenStreetMap France domain", "tile.openstreetmap.fr"),
        ("OpenStreetMap base domain", "openstreetmap.org"),
        ("osmfr identifier", "osmfr"),
        ("basemap switcher button class", "map-basemap-btn")
    ]
    for desc, pattern in prohibited:
        if pattern in content:
            print(f"[FAIL] {rel}: Found PROHIBITED pattern '{desc}' ('{pattern}')")
            all_ok = False
        else:
            print(f"[OK] {rel}: Verified ABSENCE of '{desc}'")

    # 2. Positive Checks (MUST be present)
    required = [
        ("ArcGIS Esri satellite tile URL", "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"),
        ("defaultProvider set to satellite", "defaultProvider = 'satellite'"),
        ("Satellite Basemap UI indicator", "Satellite (Esri World Imagery)"),
        ("Hoang Sa marker", "QĐ. Hoàng Sa (Việt Nam)"),
        ("Truong Sa marker", "QĐ. Trường Sa (Việt Nam)")
    ]
    for desc, pattern in required:
        if pattern not in content:
            print(f"[FAIL] {rel}: Missing REQUIRED pattern '{desc}'")
            all_ok = False
        else:
            print(f"[OK] {rel}: Found '{desc}'")

    return all_ok

def check_parity(rel_file):
    p1 = os.path.join(REPO1, rel_file)
    p2 = os.path.join(REPO2, rel_file)
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
    print("=== 1. Auditing RenewableVietNam Industrial Hubs ===")
    ok = True
    ok &= verify_file(os.path.join(REPO1, "index.html"))
    ok &= verify_file(os.path.join(REPO1, "green", "index.html"))

    print("\n=== 2. Auditing Qking232.github.io Industrial Hubs ===")
    ok &= verify_file(os.path.join(REPO2, "index.html"))
    ok &= verify_file(os.path.join(REPO2, "green", "index.html"))

    print("\n=== 3. Auditing Multi-Repo Parity ===")
    ok &= check_parity("index.html")
    ok &= check_parity(os.path.join("green", "index.html"))

    if ok:
        print("\n>>> ALL EXCLUSIVE SATELLITE CARTOGRAPHY AUDITS PASSED 100% <<<")
        sys.exit(0)
    else:
        print("\n>>> AUDIT FAILED <<<")
        sys.exit(1)

if __name__ == "__main__":
    main()
