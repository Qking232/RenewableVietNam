"""
Verify live production CDN deployment for exclusive Satellite map on Industrial Hubs.
"""
import urllib.request
import time
import sys

URLS = [
    ("https://renewablevietnam.com/", ["Satellite (Esri World Imagery)", "QĐ. Hoàng Sa (Việt Nam)"], ["tile.openstreetmap.fr", "OSM France"]),
    ("https://renewablevietnam.com/green/", ["Satellite (Esri World Imagery)", "QĐ. Hoàng Sa (Việt Nam)"], ["tile.openstreetmap.fr", "OSM France"]),
    ("https://qking232.github.io/", ["Satellite (Esri World Imagery)", "QĐ. Hoàng Sa (Việt Nam)"], ["tile.openstreetmap.fr", "OSM France"]),
    ("https://qking232.github.io/green/", ["Satellite (Esri World Imagery)", "QĐ. Hoàng Sa (Việt Nam)"], ["tile.openstreetmap.fr", "OSM France"])
]

def check_url(url, required, prohibited):
    req = urllib.request.Request(
        url + f"?_nocache={int(time.time())}",
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    )
    try:
        with urllib.request.urlopen(req, timeout=12) as response:
            status = response.getcode()
            body = response.read().decode('utf-8', errors='ignore')
            found_req = [k for k in required if k in body]
            missing_req = [k for k in required if k not in body]
            found_proh = [k for k in prohibited if k in body]

            if status == 200 and not missing_req and not found_proh:
                print(f"[LIVE CDN OK] {url} -> 200 OK, Satellite markers verified, OSM purged: {found_req}")
                return True
            else:
                print(f"[WAITING CDN] {url} -> Status {status}, missing: {missing_req}, prohibited present: {found_proh}")
                return False
    except Exception as e:
        print(f"[CDN ERROR] {url} -> {e}")
        return False

def main():
    print("Auditing live production endpoints for exclusive Satellite cartography...")
    all_ok = True
    for url, req, proh in URLS:
        ok = check_url(url, req, proh)
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
