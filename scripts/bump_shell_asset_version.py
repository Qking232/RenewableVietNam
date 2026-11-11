#!/usr/bin/env python3
"""
Bump unified shell asset cache-buster query string (?v=1 -> ?v=2) safely
across RenewableVietNam and Qking232.github.io HTML targets, creating sequential
index_Rev.xxx.html backups first and syncing shared Rev.002 shell assets.
"""

import os
import re
import shutil

REPO1 = r"G:\My Drive\7. AI\RenewableVietNam"
REPO2 = r"G:\My Drive\7. AI\Qking232.github.io"

R1_TARGETS = [
    "index.html",
    "energy/index.html",
    "projectenergy/index.html",
    "industrial/index.html",
    "industrial/calculator/index.html",
    "evcharging/index.html",
    "invm/index.html",
    "invm/quyhoach/index.html",
    "project/index.html",
    "project/dc/index.html",
    "project/garments/index.html",
    "dc/index.html",
    "garments/index.html",
    "livewire/index.html",
    "roadmap/index.html",
]

R2_TARGETS = [
    "index.html",
    "energy/index.html",
    "projectenergy/index.html",
    "industrial/index.html",
    "industrial/calculator/index.html",
    "evcharging/index.html",
    "invm/index.html",
    "invm/quyhoach/index.html",
    "project/index.html",
    "dc/index.html",
    "livewire/index.html",
    "roadmap/index.html",
    "calculator/index.html",
]


def next_rev_path(full_path):
    d = os.path.dirname(full_path)
    max_rev = 0
    for fn in os.listdir(d):
        m = re.match(r"^index_Rev\.(\d+)\.html$", fn)
        if m:
            val = int(m.group(1))
            if val > max_rev:
                max_rev = val
    return os.path.join(d, f"index_Rev.{max_rev + 1:03d}.html")


def bump_file(repo_path, rel):
    full_path = os.path.join(repo_path, rel)
    txt = open(full_path, "r", encoding="utf-8").read()
    updated = (
        txt.replace("/assets/built/rvn-shell.css?v=1", "/assets/built/rvn-shell.css?v=2")
        .replace("/assets/js/rvn-header.js?v=1", "/assets/js/rvn-header.js?v=2")
    )
    if updated == txt:
        print(f"  [SKIP] no v=1 change needed: {rel}")
        return
    rev_path = next_rev_path(full_path)
    shutil.copyfile(full_path, rev_path)
    with open(full_path, "w", encoding="utf-8", newline="\n") as fp:
        fp.write(updated)
    print(f"  [OK] {rel:34} -> v=2 (backup {os.path.basename(rev_path)})")


def main():
    # Save Rev.002 shell snapshots inside R1 and sync to R2
    shutil.copyfile(
        os.path.join(REPO1, "assets/built/rvn-shell.css"),
        os.path.join(REPO1, "assets/built/rvn-shell_Rev.002.css"),
    )
    shutil.copyfile(
        os.path.join(REPO1, "assets/js/rvn-header.js"),
        os.path.join(REPO1, "assets/js/rvn-header_Rev.002.js"),
    )
    for rel in [
        "assets/built/rvn-shell.css",
        "assets/built/rvn-shell_Rev.002.css",
        "assets/js/rvn-header.js",
        "assets/js/rvn-header_Rev.002.js",
    ]:
        shutil.copyfile(os.path.join(REPO1, rel), os.path.join(REPO2, rel))
    print("[SYNC] Synced rvn-shell.css & rvn-header.js (Rev.002) to Qking232.github.io")

    # Preserve Rev.003 copies of scripts
    for s in ["verify_standardized_headers", "deploy_sleek_header_shell"]:
        shutil.copyfile(
            os.path.join(REPO1, f"scripts/{s}.py"),
            os.path.join(REPO1, f"scripts/{s}_Rev.003.py"),
        )

    for name, repo, targets in [
        ("RenewableVietNam", REPO1, R1_TARGETS),
        ("Qking232.github.io", REPO2, R2_TARGETS),
    ]:
        print(f"\n=== Bumping ?v=1 -> ?v=2 in {name} ===")
        for rel in targets:
            bump_file(repo, rel)


if __name__ == "__main__":
    main()
