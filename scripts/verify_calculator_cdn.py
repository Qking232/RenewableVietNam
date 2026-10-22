import urllib.request
import time

endpoints = [
    ("https://renewablevietnam.com/", False, True), # (has_sidebar=False, has_calc_link=True)
    ("https://renewablevietnam.com/calculator/", True, True), # (has_calculator=True, has_corp=True)
    ("https://qking232.github.io/", False, True),
    ("https://qking232.github.io/calculator/", True, True)
]

for attempt in range(1, 15):
    all_ready = True
    print(f"\nAttempt {attempt}:")
    for url, expect_calc, expect_link in endpoints:
        try:
            req = urllib.request.Request(f"{url}?ts={int(time.time())}", headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
            with urllib.request.urlopen(req, timeout=12) as resp:
                data = resp.read()
                if "calculator" in url:
                    has_calc = b'id="corporateSizerContainer"' in data and b'id="evnEstimatorContainer"' in data
                    print(f"  {resp.status} | Len: {len(data):>7} | CalcContainer: {has_calc} | {url}")
                    if not has_calc:
                        all_ready = False
                else:
                    has_sidebar = b'id="toolsSidebar"' in data
                    has_nav = b'href="/calculator/"' in data
                    print(f"  {resp.status} | Len: {len(data):>7} | NoSidebar: {not has_sidebar} | NavLink: {has_nav} | {url}")
                    if has_sidebar or not has_nav:
                        all_ready = False
        except Exception as e:
            print(f"  ERR | {e} | {url}")
            all_ready = False
            
    if all_ready:
        print("\n[SUCCESS] All live production CDN endpoints are fully deployed and serving updated assets!")
        break
    time.sleep(5)
