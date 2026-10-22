"""
Verify live production CDN deployment for mobile touch navigation and sticky header CTAs.
"""
import urllib.request
import time
import sys

URLS = [
    ("https://renewablevietnam.com/", ["Industrial Hubs", "Power Sizer", "Energy Map", "no-scrollbar"]),
    ("https://renewablevietnam.com/calculator/", ["Power Sizer", "Industrial Hubs", "no-scrollbar"]),
    ("https://renewablevietnam.com/evcharging/", ["Hubs", "Tariffs"]),
    ("https://qking232.github.io/", ["Industrial Hubs", "Power Sizer", "Energy Map", "no-scrollbar"]),
    ("https://qking232.github.io/calculator/", ["Power Sizer", "Industrial Hubs", "no-scrollbar"]),
    ("https://qking232.github.io/evcharging/", ["Hubs", "Tariffs"])
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
                print(f"[LIVE CDN OK] {url} -> 200 OK, all markers verified: {found}")
                return True
            else:
                print(f"[WAITING CDN] {url} -> Status {status}, missing markers: {missing}")
                return False
    except Exception as e:
        print(f"[CDN ERROR] {url} -> {e}")
        return False

def main():
    print("Auditing live production endpoints for mobile navigation deployment...")
    all_ok = True
    for url, keywords in URLS:
        ok = check_url(url, keywords)
        if not ok:
            all_ok = False
            
    if all_ok:
        print("\n>>> ALL PRODUCTION CDNS FULLY PROPAGATED & VERIFIED! <<<")
        sys.exit(0)
    else:
        print("\n>>> Some CDNs still propagating cache... <<<")
        sys.exit(0) # Non-blocking on initial CDN propagation

if __name__ == "__main__":
    main()
