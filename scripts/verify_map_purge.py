#!/usr/bin/env python3
"""
verify_map_purge.py - Verify complete removal of map containers and validate script syntax
"""

import os
import re
import hashlib
import subprocess

REPO_A = r"G:\My Drive\7. AI\Gemini\RenewableVietNam"
REPO_B = r"G:\My Drive\7. AI\Gemini\Qking232.github.io"

def calc_sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def test_audit():
    print("===================================================================")
    print("Green Industrial & PDP8 Energy Satellite Map Purge Verification")
    print("===================================================================\n")

    # 1. Check index.html
    path_index = os.path.join(REPO_A, "index.html")
    with open(path_index, "r", encoding="utf-8") as f:
        c_index = f.read()
    assert "id=\"ecoParkMapContainer\"" not in c_index, "ecoParkMapContainer still found in index.html"
    assert "id=\"ecoParkMap\"" not in c_index, "ecoParkMap still found in index.html"
    assert "id=\"hubDossierContainer\"" in c_index, "hubDossierContainer missing from index.html"
    print("[TEST 1] index.html: ecoParkMapContainer successfully purged; hubDossierContainer present.")

    # 2. Check green/index.html
    path_green = os.path.join(REPO_A, "green", "index.html")
    with open(path_green, "r", encoding="utf-8") as f:
        c_green = f.read()
    assert "id=\"ecoParkMapContainer\"" not in c_green, "ecoParkMapContainer still found in green/index.html"
    assert "id=\"ecoParkMap\"" not in c_green, "ecoParkMap still found in green/index.html"
    assert "id=\"hubsTableBody\"" in c_green, "hubsTableBody missing from green/index.html"
    print("[TEST 2] green/index.html: ecoParkMapContainer successfully purged; table body present.")

    # 3. Check projectenergy/index.html
    path_pe = os.path.join(REPO_A, "projectenergy", "index.html")
    with open(path_pe, "r", encoding="utf-8") as f:
        c_pe = f.read()
    assert "id=\"energyMapContainer\"" not in c_pe, "energyMapContainer still found in projectenergy/index.html"
    assert "id=\"energyMap\"" not in c_pe, "energyMap still found in projectenergy/index.html"
    assert "id=\"dossierContainer\"" in c_pe, "dossierContainer missing from projectenergy/index.html"
    print("[TEST 3] projectenergy/index.html: energyMapContainer successfully purged; dossierContainer present.")

    # 4. Extract and syntax check JS
    for name, content in [("index.html", c_index), ("projectenergy/index.html", c_pe)]:
        scripts = re.findall(r'<script.*?>([\s\S]*?)</script>', content)
        assert len(scripts) > 0, f"No scripts in {name}"
        longest_script = max(scripts, key=len)
        temp_js = f"C:/Users/Quan/.gemini/antigravity/brain/81e8845a-d5e4-493e-95ba-f70531d86d2c/scratch/check_{os.path.basename(name)}.js"
        with open(temp_js, "w", encoding="utf-8") as f:
            f.write(longest_script)
        res = subprocess.run(["node", "--check", temp_js], capture_output=True, text=True)
        assert res.returncode == 0, f"JS Syntax error in {name}: {res.stderr}"
        print(f"[TEST 4] {name}: JavaScript syntax check PASSED cleanly.")

    # 5. Dual-Repository Synchronization
    files_to_sync = [
        "index.html",
        os.path.join("green", "index.html"),
        os.path.join("projectenergy", "index.html")
    ]

    print("\n--- Synchronizing Purged Routes to Qking232.github.io ---")
    for rel_path in files_to_sync:
        src = os.path.join(REPO_A, rel_path)
        dst = os.path.join(REPO_B, rel_path)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(src, "rb") as sf:
            s_data = sf.read()
        with open(dst, "wb") as df:
            df.write(s_data)
        
        sha_a = calc_sha256(src)
        sha_b = calc_sha256(dst)
        assert sha_a == sha_b, f"Parity mismatch for {rel_path}"
        print(f"  ✓ {rel_path}: SHA-256 match ({sha_a[:12]}...)")

    print("\n===================================================================")
    print("ALL MAP PURGE TESTS PASSED WITH 100% PARITY")
    print("===================================================================")

if __name__ == "__main__":
    test_audit()
