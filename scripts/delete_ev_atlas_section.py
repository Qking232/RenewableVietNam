import os
import re
import shutil
import hashlib

REPOS = [
    r"G:\My Drive\7. AI\RenewableVietNam",
    r"G:\My Drive\7. AI\Qking232.github.io"
]

print("=== REMOVING GEOSPATIAL EV ATLAS SECTION ===")

for repo in REPOS:
    fpath = os.path.join(repo, "evcharging", "index.html")
    rev_path = os.path.join(repo, "evcharging", "index_Rev.007.html")

    # 1. Non-destructive revision backup
    shutil.copyfile(fpath, rev_path)
    print(f"Created backup: {rev_path}")

    with open(fpath, "r", encoding="utf-8") as fp:
        content = fp.read()

    # 2. Remove evMapContainer section
    p_map_section = re.compile(
        r'\s*<!-- INTERACTIVE GEOSPATIAL MAP COCKPIT.*?<section id="evMapContainer".*?</section>',
        re.DOTALL
    )
    new_content, c1 = p_map_section.subn('', content)
    print(f"Removed evMapContainer section: {c1} match")

    # 3. Remove View Mode Switcher
    p_view_toggle = re.compile(
        r'\s*<!-- View Mode Switcher -->\s*<div class="flex items-center gap-1 p-0.5 rounded-lg bg-slate-100.*?</div>',
        re.DOTALL
    )
    new_content, c2 = p_view_toggle.subn('', new_content)
    print(f"Removed view mode switcher: {c2} match")

    # 4. Save
    with open(fpath, "w", encoding="utf-8") as fp:
        fp.write(new_content)
    print(f"Updated {fpath}")

# Parity check
h1 = hashlib.sha256(open(os.path.join(REPOS[0], "evcharging", "index.html"), "rb").read()).hexdigest()
h2 = hashlib.sha256(open(os.path.join(REPOS[1], "evcharging", "index.html"), "rb").read()).hexdigest()
print(f"\nParity match: {h1 == h2} (Hash: {h1[:8]})")
