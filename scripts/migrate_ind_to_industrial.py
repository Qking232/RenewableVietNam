#!/usr/bin/env python3
"""
Migrate all occurrences of ind.renewablevietnam.com to industrial.renewablevietnam.com
across all pages, maintaining non-destructive sequential revisioning and mirroring
100% to Qking232.github.io.
"""

import os
import shutil

REPO1 = r"G:\My Drive\7. AI\RenewableVietNam"
REPO2 = r"G:\My Drive\7. AI\Qking232.github.io"

TASKS = [
    {
        "rel": os.path.join("green", "index.html"),
        "rev_rel": os.path.join("green", "index_Rev.002.html"),
        "special_redirect": True
    },
    {
        "rel": os.path.join("projectenergy", "index.html"),
        "rev_rel": os.path.join("projectenergy", "index_Rev.002.html"),
        "special_redirect": False
    },
    {
        "rel": os.path.join("evcharging", "index.html"),
        "rev_rel": os.path.join("evcharging", "index_Rev.002.html"),
        "special_redirect": False
    },
    {
        "rel": os.path.join("evcharging", "ev", "index.html"),
        "rev_rel": os.path.join("evcharging", "ev", "index_Rev.001.html"),
        "special_redirect": False
    },
    {
        "rel": os.path.join("livewire", "index.html"),
        "rev_rel": os.path.join("livewire", "index_Rev.001.html"),
        "special_redirect": False
    }
]

def migrate():
    print("--- Starting Subdomain Migration to industrial.renewablevietnam.com ---")
    
    for t in TASKS:
        src_path = os.path.join(REPO1, t["rel"])
        rev_path = os.path.join(REPO1, t["rev_rel"])
        
        with open(src_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        if t["special_redirect"]:
            # In green/index.html, handle the redirect script
            content = content.replace("https://ind.renewablevietnam.com", "https://industrial.renewablevietnam.com")
            content = content.replace(
                "if (window.location.hostname === 'renewablevietnam.com')",
                "if (window.location.hostname === 'renewablevietnam.com' || window.location.hostname === 'ind.renewablevietnam.com')"
            )
        else:
            content = content.replace("https://ind.renewablevietnam.com", "https://industrial.renewablevietnam.com")
            content = content.replace("ind.renewablevietnam.com", "industrial.renewablevietnam.com")
            
        # Write revision file in REPO1
        with open(rev_path, "w", encoding="utf-8") as f:
            f.write(content)
        # Write active file in REPO1
        with open(src_path, "w", encoding="utf-8") as f:
            f.write(content)
            
        print(f"[REPO1] Updated {t['rel']} -> {t['rev_rel']}")
        
        # Mirror to REPO2
        dest_src = os.path.join(REPO2, t["rel"])
        dest_rev = os.path.join(REPO2, t["rev_rel"])
        
        os.makedirs(os.path.dirname(dest_src), exist_ok=True)
        with open(dest_src, "w", encoding="utf-8") as f:
            f.write(content)
        with open(dest_rev, "w", encoding="utf-8") as f:
            f.write(content)
            
        print(f"[REPO2] Mirrored {t['rel']} and {t['rev_rel']}")

    # Also mirror index.html and index_Rev.010.html to REPO2
    idx1 = os.path.join(REPO1, "index.html")
    idx1_rev = os.path.join(REPO1, "index_Rev.010.html")
    idx2 = os.path.join(REPO2, "index.html")
    idx2_rev = os.path.join(REPO2, "index_Rev.010.html")
    
    with open(idx1, "r", encoding="utf-8") as f:
        idx_content = f.read()
    with open(idx2, "w", encoding="utf-8") as f:
        f.write(idx_content)
    with open(idx2_rev, "w", encoding="utf-8") as f:
        f.write(idx_content)
    print(f"[REPO2] Mirrored index.html and index_Rev.010.html")

    # Also mirror cloudflare worker files
    cf1 = os.path.join(REPO1, "cloudflare", "subdomain_gateway_worker.js")
    cf1_rev = os.path.join(REPO1, "cloudflare", "subdomain_gateway_worker_Rev.002.js")
    # If REPO2 has cloudflare folder, mirror there
    cf2_dir = os.path.join(REPO2, "cloudflare")
    if os.path.exists(cf2_dir):
        shutil.copy(cf1, os.path.join(cf2_dir, "subdomain_gateway_worker.js"))
        shutil.copy(cf1_rev, os.path.join(cf2_dir, "subdomain_gateway_worker_Rev.002.js"))
        print("[REPO2] Mirrored cloudflare worker files")

    print("\n[SUCCESS] Subdomain migration completed across all target files!")

if __name__ == "__main__":
    migrate()
