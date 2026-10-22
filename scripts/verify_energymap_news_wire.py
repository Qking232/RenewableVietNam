"""
Verification script for EnergyMap Multi-Source News Wire & Industrial Zone UI Feed Integration.
"""
import os
import json
import sys

REPO1 = "G:/My Drive/7. AI/Gemini/RenewableVietNam"
REPO2 = "G:/My Drive/7. AI/Gemini/Qking232.github.io"

def verify_json_data(repo):
    path = os.path.join(repo, "data", "industry_news.json")
    if not os.path.exists(path):
        print(f"[FAIL] Missing {path}")
        return False
    with open(path, "r", encoding="utf-8") as f:
        d = json.load(f)
    articles = d.get("articles", [])
    if len(articles) < 100:
        print(f"[FAIL] Expected >= 100 articles, got {len(articles)}")
        return False
    
    # Check schema
    sample = articles[0]
    required = ["title", "link", "source", "sector", "relative_time", "province", "zone_match"]
    missing = [k for k in required if k not in sample]
    if missing:
        print(f"[FAIL] Missing keys {missing} in article schema")
        return False

    provinces_count = sum(1 for a in articles if a.get("province"))
    zones_count = sum(1 for a in articles if a.get("zone_match"))
    print(f"[OK] {os.path.basename(repo)}/data/industry_news.json: {len(articles)} articles ({provinces_count} province matches, {zones_count} industrial zone matches)")
    return True

def verify_html_elements(repo):
    path = os.path.join(repo, "projectenergy", "index.html")
    if not os.path.exists(path):
        print(f"[FAIL] Missing {path}")
        return False
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    checks = [
        ("Header Market Wire link", 'href="#marketWire"'),
        ("Section 05 element", 'id="marketWire"'),
        ("Breaking ticker container", 'id="breakingTickerContainer"'),
        ("Search input", 'id="newsSearchInput"'),
        ("Sector pills", 'news-sector-pill'),
        ("News grid container", 'id="newsGrid"'),
        ("Expand container", 'id="newsExpandContainer"'),
        ("JS function fetchNewsData", 'function fetchNewsData'),
        ("JS function selectNewsSector", 'function selectNewsSector'),
        ("JS function handleNewsSearch", 'function handleNewsSearch'),
        ("JS function toggleNewsExpand", 'function toggleNewsExpand'),
        ("JS function renderBreakingTicker", 'function renderBreakingTicker'),
        ("JS function renderNewsGrid", 'function renderNewsGrid'),
        ("JS function renderArticleCard", 'function renderArticleCard'),
        ("Language hook in setLanguage", 'renderNewsGrid();'),
        ("DOMContentLoaded news hook", 'fetchNewsData();')
    ]

    all_ok = True
    rel_repo = os.path.basename(repo)
    for desc, pattern in checks:
        if pattern not in content:
            print(f"[FAIL] {rel_repo}/projectenergy/index.html: Missing '{desc}'")
            all_ok = False
        else:
            print(f"[OK] {rel_repo}/projectenergy/index.html: Found '{desc}'")
    return all_ok

def verify_redirect(repo):
    path = os.path.join(repo, "energymap", "index.html")
    if not os.path.exists(path):
        print(f"[FAIL] Missing redirect: {path}")
        return False
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    if 'url=/projectenergy/' not in content:
        print(f"[FAIL] Invalid redirect target in {path}")
        return False
    print(f"[OK] {os.path.basename(repo)}/energymap/index.html: Valid canonical redirect")
    return True

def check_parity(file_rel):
    p1 = os.path.join(REPO1, file_rel)
    p2 = os.path.join(REPO2, file_rel)
    with open(p1, "r", encoding="utf-8") as f1, open(p2, "r", encoding="utf-8") as f2:
        c1 = f1.read()
        c2 = f2.read()
    if c1 == c2:
        print(f"[OK] 100% PARITY for {file_rel}")
        return True
    else:
        print(f"[FAIL] Parity mismatch for {file_rel}: {len(c1)} vs {len(c2)} bytes")
        return False

def main():
    print("--- 1. Auditing News Data Schemas ---")
    s1 = verify_json_data(REPO1)
    s2 = verify_json_data(REPO2)

    print("\n--- 2. Auditing HTML & JavaScript Components ---")
    s3 = verify_html_elements(REPO1)
    s4 = verify_html_elements(REPO2)

    print("\n--- 3. Auditing /energymap/ Route Aliases ---")
    s5 = verify_redirect(REPO1)
    s6 = verify_redirect(REPO2)

    print("\n--- 4. Auditing Multi-Repo Parity ---")
    s7 = check_parity(os.path.join("data", "industry_news.json"))
    s8 = check_parity(os.path.join("projectenergy", "index.html"))
    s9 = check_parity(os.path.join("energymap", "index.html"))

    if all([s1, s2, s3, s4, s5, s6, s7, s8, s9]):
        print("\n>>> ALL ENERGYMAP NEWS WIRE AUDITS PASSED 100% <<<")
        sys.exit(0)
    else:
        print("\n>>> VERIFICATION AUDIT FAILED <<<")
        sys.exit(1)

if __name__ == "__main__":
    main()
