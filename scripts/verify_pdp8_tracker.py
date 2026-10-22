"""
Comprehensive verification audit for PDP8 Statutory Tracker (2026-2030) deployment.
"""
import os
import json
import sys

REPO1 = "G:/My Drive/7. AI/Gemini/RenewableVietNam"
REPO2 = "G:/My Drive/7. AI/Gemini/Qking232.github.io"

def verify_json(repo):
    path = os.path.join(repo, "data", "pdp8_targets.json")
    if not os.path.exists(path):
        print(f"[FAIL] Missing {path}")
        return False
    with open(path, "r", encoding="utf-8") as f:
        d = json.load(f)
    meta = d.get("metadata", {})
    if meta.get("total_statutory_capacity_2030_mw") != 150489:
        print(f"[FAIL] Unexpected total statutory capacity: {meta.get('total_statutory_capacity_2030_mw')}")
        return False
    if meta.get("current_operating_baseload_mw") != 80612:
        print(f"[FAIL] Unexpected operating baseload: {meta.get('current_operating_baseload_mw')}")
        return False
    fuels = d.get("fuel_targets", [])
    if len(fuels) < 8:
        print(f"[FAIL] Expected >= 8 fuel categories, got {len(fuels)}")
        return False
    projects = d.get("priority_projects", [])
    if len(projects) < 10:
        print(f"[FAIL] Expected >= 10 priority projects, got {len(projects)}")
        return False
    
    print(f"[OK] {os.path.basename(repo)}/data/pdp8_targets.json: {len(fuels)} fuels, {len(projects)} priority projects, metadata verified.")
    return True

def verify_html(repo, rel_file):
    path = os.path.join(repo, rel_file)
    if not os.path.exists(path):
        print(f"[FAIL] Missing {path}")
        return False
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    checks = [
        ("Header PDP8 link", 'href="#pdp8"'),
        ("Section #pdp8 element", 'id="pdp8"'),
        ("PDP8 sector gauges container", 'id="pdp8SectorGauges"'),
        ("PDP8 projects grid container", 'id="pdp8ProjectsGrid"'),
        ("PDP8 project filter buttons", 'pdp8-proj-filter'),
        ("Deep link to Atlas", '/projectenergy/?search='),
        ("JS function loadPdp8Data", 'function loadPdp8Data'),
        ("JS function renderPdp8Gauges", 'function renderPdp8Gauges'),
        ("JS function renderPdp8Projects", 'function renderPdp8Projects'),
        ("JS function filterPdp8Projects", 'function filterPdp8Projects'),
        ("Invocation of loadPdp8Data()", 'loadPdp8Data();')
    ]

    all_ok = True
    prefix = f"{os.path.basename(repo)}/{rel_file}"
    for desc, pattern in checks:
        if pattern not in content:
            print(f"[FAIL] {prefix}: Missing '{desc}'")
            all_ok = False
        else:
            print(f"[OK] {prefix}: Found '{desc}'")
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
    print("--- 1. Auditing PDP8 Targets Dataset ---")
    s1 = verify_json(REPO1)
    s2 = verify_json(REPO2)

    print("\n--- 2. Auditing HTML UI & JavaScript Integration ---")
    s3 = verify_html(REPO1, "index.html")
    s4 = verify_html(REPO1, os.path.join("green", "index.html"))
    s5 = verify_html(REPO2, "index.html")
    s6 = verify_html(REPO2, os.path.join("green", "index.html"))

    print("\n--- 3. Auditing Cross-Repo Parity ---")
    s7 = check_parity(os.path.join("data", "pdp8_targets.json"))
    s8 = check_parity("index.html")
    s9 = check_parity(os.path.join("green", "index.html"))

    if all([s1, s2, s3, s4, s5, s6, s7, s8, s9]):
        print("\n>>> ALL PDP8 STATUTORY TRACKER AUDITS PASSED 100% <<<")
        sys.exit(0)
    else:
        print("\n>>> VERIFICATION AUDIT FAILED <<<")
        sys.exit(1)

if __name__ == "__main__":
    main()
