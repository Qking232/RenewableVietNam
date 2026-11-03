import os
import re
import shutil
import hashlib

REPOS = [
    r"G:\My Drive\7. AI\RenewableVietNam",
    r"G:\My Drive\7. AI\Qking232.github.io"
]

TARGET_FILES = [
    ("evcharging/index.html", "index_Rev.004.html"),
    ("evcharging/ev/index.html", "index_Rev.002.html"),
    ("livewire/index.html", "index_Rev.002.html"),
    ("projectenergy/index.html", "index_Rev.005.html"),
    ("industrial/index.html", "index_Rev.004.html"),
    ("sitemap.xml", "sitemap_Rev.003.xml"),
]

def clean_html(content):
    # Desktop nav link pattern:
    # <span class="text-slate-300 dark:text-slate-700">&middot;</span>\s*<a href="https://legal\.renewablevietnam\.com/"[^>]*>Legal Framework</a>
    p_desktop = re.compile(
        r'\s*<span class="text-slate-300 dark:text-slate-700">&middot;</span>\s*<a href="https://legal\.renewablevietnam\.com/"[^>]*>Legal Framework</a>',
        re.MULTILINE
    )
    # Mobile nav link pattern:
    # <a href="https://legal\.renewablevietnam\.com/"[^>]*>Legal Framework</a>
    p_mobile = re.compile(
        r'\s*<a href="https://legal\.renewablevietnam\.com/"[^>]*>Legal Framework</a>',
        re.MULTILINE
    )
    c = p_desktop.sub('', content)
    c = p_mobile.sub('', c)
    return c

def clean_sitemap(content):
    # Remove <url> block containing https://renewablevietnam.com/hub/
    p_hub = re.compile(
        r'\s*<url>\s*<loc>https://renewablevietnam\.com/hub/</loc>.*?</url>',
        re.DOTALL
    )
    return p_hub.sub('', content)

print("=== APPLYING LEGAL DECOMMISSIONING CLEANUP ===")

for repo in REPOS:
    repo_name = os.path.basename(repo)
    print(f"\nProcessing repository: {repo_name}")
    for rel_path, rev_name in TARGET_FILES:
        full_path = os.path.join(repo, rel_path)
        if not os.path.exists(full_path):
            print(f"  [SKIP] {rel_path} does not exist")
            continue

        dir_path = os.path.dirname(full_path)
        rev_path = os.path.join(dir_path, rev_name)

        # 1. Create non-destructive revision backup
        shutil.copyfile(full_path, rev_path)
        print(f"  [BACKUP] {rel_path} -> {rev_name}")

        # 2. Read and clean
        with open(full_path, 'r', encoding='utf-8') as fp:
            original = fp.read()

        if rel_path.endswith('.xml'):
            cleaned = clean_sitemap(original)
        else:
            cleaned = clean_html(original)

        with open(full_path, 'w', encoding='utf-8') as fp:
            fp.write(cleaned)
        print(f"  [UPDATED] {rel_path}")

print("\n=== VERIFYING CRYPTOGRAPHIC SHA-256 PARITY ===")
parity_ok = True
for rel_path, _ in TARGET_FILES:
    p1 = os.path.join(REPOS[0], rel_path)
    p2 = os.path.join(REPOS[1], rel_path)
    if os.path.exists(p1) and os.path.exists(p2):
        h1 = hashlib.sha256(open(p1, 'rb').read()).hexdigest()
        h2 = hashlib.sha256(open(p2, 'rb').read()).hexdigest()
        if h1 == h2:
            print(f"  [PASS] {rel_path} hash parity: {h1[:8]}")
        else:
            print(f"  [FAIL] {rel_path} mismatch: REPO1={h1[:8]} REPO2={h2[:8]}")
            parity_ok = False
    else:
        print(f"  [WARN] Missing file in one repo: {rel_path}")

if parity_ok:
    print("\n[RESULT] 100% Cryptographic Parity Verified across both repositories!")
else:
    print("\n[RESULT] Mismatch detected!")
