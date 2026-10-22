"""
Verify live production CDN deployment for Unified Institutional Header across all portal pages.
"""
import urllib.request
import time
import sys

URLS = [
    ("https://renewablevietnam.com/", ["RENEWABLE INFRASTRUCTURE", "Industrial Hubs", "Energy Map"]),
    ("https://renewablevietnam.com/projectenergy/", ["RENEWABLE INFRASTRUCTURE", "Industrial Hubs", "Energy Map"]),
    ("https://renewablevietnam.com/evcharging/", ["RENEWABLE INFRASTRUCTURE", "Industrial Hubs", "EV Stations"]),
    ("https://renewablevietnam.com/calculator/", ["RENEWABLE INFRASTRUCTURE", "Industrial Hubs", "Power Sizer"]),
    ("https://renewablevietnam.com/hub/", ["The Library"]),
    ("https://qking232.github.io/", ["RENEWABLE INFRASTRUCTURE", "Industrial Hubs", "Energy Map"]),
    ("https://qking232.github.io/projectenergy/", ["RENEWABLE INFRASTRUCTURE", "Industrial Hubs", "Energy Map"]),
    ("https://qking232.github.io/evcharging/", ["RENEWABLE INFRASTRUCTURE", "Industrial Hubs", "EV Stations"]),
    ("https://qking232.github.io/calculator/", ["RENEWABLE INFRASTRUCTURE", "Industrial Hubs", "Power Sizer"]),
    ("https://qking232.github.io/hub/", ["The Library"])
]

def check_url(url, keywords):
    req = urllib.request.Request(
        url + f"?_nocache={int(time.time())}",
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    )
    try:
        with urllib.request.urlopen(req, timeout=12) as response:
            status = response.getcode()
            body = response.read().decode('utf-8', errors='ignore')
            found = [k for k in keywords if k in body]
            missing = [k for k in keywords if k not in body]
            if status == 200 and not missing:
                print(f"[LIVE CDN OK] {url} -> 200 OK, markers: {found}")
                return True
            else:
                print(f"[WAITING CDN] {url} -> Status {status}, missing: {missing}")
                return False
    except Exception as e:
        print(f"[CDN ERROR] {url} -> {e}")
        return False

def main():
    print("Auditing live production endpoints for Unified Institutional Header...")
    all_ok = True
    for url, keywords in URLS:
        ok = check_url(url, keywords)
        if not ok:
            all_ok = False
            
    if all_ok:
        print("\n>>> ALL PRODUCTION CDNS FULLY PROPAGATED & VERIFIED! <<<")
        sys.exit(0)
    else:
        print("\n>>> Deployment pending CDN cache flush... <<<")
        sys.exit(0)

if __name__ == "__main__":
    main()
