import os
import shutil
import hashlib

REPOS = [
    r"G:\My Drive\7. AI\RenewableVietNam",
    r"G:\My Drive\7. AI\Qking232.github.io"
]

TARGETS = [
    ("invm/index.html", "index_Rev.029.html"),
    ("invm/quyhoach/index.html", "index_Rev.002.html"),
    ("index.html", "index_Rev.017.html", "index_Rev.012.html"),
    ("evcharging/index.html", "index_Rev.005.html"),
    ("evcharging/ev/index.html", "index_Rev.003.html"),
    ("livewire/index.html", "index_Rev.003.html"),
    ("projectenergy/index.html", "index_Rev.006.html"),
    ("industrial/index.html", "index_Rev.005.html"),
    ("project/index.html", "index_Rev.004.html"),
]

def update_content(text):
    # Replace URL endpoints
    text = text.replace("https://invest.renewablevietnam.com/", "https://legal.renewablevietnam.com/")
    text = text.replace("https://invest.renewablevietnam.com", "https://legal.renewablevietnam.com")
    text = text.replace("invest.renewablevietnam.com", "legal.renewablevietnam.com")
    return text

print("=== EXECUTING INVEST -> LEGAL SUBDOMAIN MIGRATION ===")

for repo_idx, repo in enumerate(REPOS):
    repo_name = os.path.basename(repo)
    print(f"\nProcessing Repository: {repo_name}")
    for item in TARGETS:
        rel_path = item[0]
        if len(item) == 3:
            rev_name = item[1] if repo_idx == 0 else item[2]
        else:
            rev_name = item[1]

        full_path = os.path.join(repo, rel_path)
        if not os.path.exists(full_path):
            print(f"  [SKIP] {rel_path} not found")
            continue

        dir_path = os.path.dirname(full_path)
        rev_path = os.path.join(dir_path, rev_name)

        # 1. Non-destructive revision backup
        shutil.copyfile(full_path, rev_path)
        print(f"  [BACKUP] {rel_path} -> {rev_name}")

        # 2. Read and transform
        with open(full_path, "r", encoding="utf-8") as fp:
            content = fp.read()

        updated = update_content(content)

        with open(full_path, "w", encoding="utf-8") as fp:
            fp.write(updated)
        print(f"  [UPDATED] {rel_path}")

# Check SHA-256 Parity
print("\n=== VERIFYING CRYPTOGRAPHIC SHA-256 PARITY ===")
parity_all_pass = True
for item in TARGETS:
    rel_path = item[0]
    p1 = os.path.join(REPOS[0], rel_path)
    p2 = os.path.join(REPOS[1], rel_path)
    if os.path.exists(p1) and os.path.exists(p2):
        h1 = hashlib.sha256(open(p1, "rb").read()).hexdigest()
        h2 = hashlib.sha256(open(p2, "rb").read()).hexdigest()
        if h1 == h2:
            print(f"  [PASS] {rel_path:25}: {h1[:8]}")
        else:
            print(f"  [FAIL] {rel_path:25}: REPO1={h1[:8]} REPO2={h2[:8]}")
            # Align from REPO1 to REPO2
            shutil.copyfile(p1, p2)
            print(f"    -> Aligned REPO2 to match canonical REPO1")
    else:
        print(f"  [WARN] Missing file: {rel_path}")

print("\nMigration complete.")
