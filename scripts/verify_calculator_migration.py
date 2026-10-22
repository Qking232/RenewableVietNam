import os

REPOS = [
    "G:/My Drive/7. AI/Gemini/RenewableVietNam",
    "G:/My Drive/7. AI/Gemini/Qking232.github.io"
]

all_passed = True

for repo in REPOS:
    print(f"=== Testing {repo} ===")
    
    # Check index.html
    index_path = os.path.join(repo, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        idx_content = f.read()

    has_sidebar = 'id="toolsSidebar"' in idx_content
    has_calc_link = '<a href="/calculator/"' in idx_content
    has_w_full = '<div class="w-full space-y-8 sm:space-y-10">' in idx_content
    has_clean_main = '</div>\n  </main>' in idx_content

    print(f"  index.html ({len(idx_content)} bytes):")
    print(f"    has_sidebar: {has_sidebar} (Expected: False)")
    print(f"    has_calc_link: {has_calc_link} (Expected: True)")
    print(f"    has_w_full: {has_w_full} (Expected: True)")
    print(f"    has_clean_main: {has_clean_main} (Expected: True)")

    if has_sidebar or not has_calc_link or not has_w_full or not has_clean_main:
        print("    [FAIL] index.html validation failed!")
        all_passed = False

    # Check calculator/index.html
    calc_path = os.path.join(repo, "calculator", "index.html")
    with open(calc_path, "r", encoding="utf-8") as f:
        calc_content = f.read()

    has_calc_sec = 'id="calculator"' in calc_content
    has_corp = 'id="corporateSizerContainer"' in calc_content
    has_evn = 'id="evnEstimatorContainer"' in calc_content
    has_green = 'id="greenIndicatorContainer"' in calc_content
    has_tabs = 'id="tabCorporateSizerBtn"' in calc_content and 'id="tabEvnEstimatorBtn"' in calc_content and 'id="tabGreenIndicatorBtn"' in calc_content
    has_hubs = 'const FALLBACK_HUBS' in calc_content
    has_update_calc = 'function updateCalculator()' in calc_content
    has_2col_grid = 'lg:grid-cols-2 gap-6' in calc_content

    print(f"  calculator/index.html ({len(calc_content)} bytes):")
    print(f"    has_calc_sec: {has_calc_sec} (Expected: True)")
    print(f"    has_corp: {has_corp} (Expected: True)")
    print(f"    has_evn: {has_evn} (Expected: True)")
    print(f"    has_green: {has_green} (Expected: True)")
    print(f"    has_tabs: {has_tabs} (Expected: True)")
    print(f"    has_hubs: {has_hubs} (Expected: True)")
    print(f"    has_update_calc: {has_update_calc} (Expected: True)")
    print(f"    has_2col_grid: {has_2col_grid} (Expected: True)")

    if not all([has_calc_sec, has_corp, has_evn, has_green, has_tabs, has_hubs, has_update_calc, has_2col_grid]):
        print("    [FAIL] calculator/index.html validation failed!")
        all_passed = False

    # Check green/ mirrors
    green_index = os.path.join(repo, "green", "index.html")
    green_calc = os.path.join(repo, "green", "calculator", "index.html")
    with open(green_index, "r", encoding="utf-8") as f:
        green_idx_content = f.read()
    with open(green_calc, "r", encoding="utf-8") as f:
        green_calc_content = f.read()

    idx_match = (idx_content == green_idx_content)
    calc_match = (calc_content == green_calc_content)
    print(f"  Mirror parity: green/index == root/index: {idx_match}, green/calc == root/calc: {calc_match}")
    if not idx_match or not calc_match:
        all_passed = False

# Cross-repo parity check
with open("G:/My Drive/7. AI/Gemini/RenewableVietNam/index.html", "r", encoding="utf-8") as f1, \
     open("G:/My Drive/7. AI/Gemini/Qking232.github.io/index.html", "r", encoding="utf-8") as f2:
    repos_idx_match = (f1.read() == f2.read())

with open("G:/My Drive/7. AI/Gemini/RenewableVietNam/calculator/index.html", "r", encoding="utf-8") as f1, \
     open("G:/My Drive/7. AI/Gemini/Qking232.github.io/calculator/index.html", "r", encoding="utf-8") as f2:
    repos_calc_match = (f1.read() == f2.read())

print(f"\nCross-repository parity:")
print(f"  RenewableVietNam vs Qking232 index.html match: {repos_idx_match}")
print(f"  RenewableVietNam vs Qking232 calculator/index.html match: {repos_calc_match}")

if repos_idx_match and repos_calc_match and all_passed:
    print("\n[SUCCESS] 100% Verification passed across all 8 files!")
else:
    print("\n[ERROR] Verification failed!")
