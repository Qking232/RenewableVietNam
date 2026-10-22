import urllib.request
import time
import sys

URLS = [
    ("https://renewablevietnam.com/", ["Industrial Hubs", "PDP8 Energy", "ECO-INDUSTRIAL SITING REGISTRY"]),
    ("https://renewablevietnam.com/projectenergy/", ["PDP8 Energy", "pdp8SectorGauges", "energyMap", "pdp8ProjectsGrid", "projectsTableBody"]),
    ("https://renewablevietnam.com/evcharging/", ["EV Stations", "PDP8 Energy", "22,055"]),
    ("https://renewablevietnam.com/evcharging/ev/", ["EV Stations Map", "VinFast", "Route Planner"]),
    ("https://renewablevietnam.com/calculator/", ["Power Sizer", "PDP8 Energy", "EVN"]),
    ("https://renewablevietnam.com/pdp8/", ["Redirecting to PDP8 Energy", "/projectenergy/"]),
    ("https://qking232.github.io/", ["Industrial Hubs", "PDP8 Energy", "ECO-INDUSTRIAL SITING REGISTRY"]),
    ("https://qking232.github.io/projectenergy/", ["PDP8 Energy", "pdp8SectorGauges", "energyMap", "pdp8ProjectsGrid", "projectsTableBody"]),
    ("https://qking232.github.io/evcharging/", ["EV Stations", "PDP8 Energy", "22,055"]),
    ("https://qking232.github.io/evcharging/ev/", ["EV Stations Map", "VinFast", "Route Planner"]),
    ("https://qking232.github.io/calculator/", ["Power Sizer", "PDP8 Energy", "EVN"]),
    ("https://qking232.github.io/pdp8/", ["Redirecting to PDP8 Energy", "/projectenergy/"])
]

def verify_all():
    print("Auditing live CDNs for PDP8 Energy portal unification...")
    for attempt in range(1, 16):
        print(f"\nAttempt {attempt} of 15:")
        all_ok = True
        for url, required_tokens in URLS:
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
                with urllib.request.urlopen(req, timeout=12) as resp:
                    if resp.status != 200:
                        print(f"  [WAIT] {url} -> HTTP {resp.status}")
                        all_ok = False
                        continue
                    body = resp.read().decode("utf-8", errors="ignore")
                    missing = [t for t in required_tokens if t not in body]
                    if missing:
                        print(f"  [WAIT] {url} -> missing tokens: {missing}")
                        all_ok = False
                    else:
                        print(f"  [LIVE OK] {url} -> 200 OK & Verified ({len(body)} bytes)")
            except Exception as e:
                print(f"  [FAIL] {url} -> {e}")
                all_ok = False
        
        if all_ok:
            print("\n>>> ALL 12 LIVE CDN PRODUCTION ENDPOINTS 100% VERIFIED & SYNCHRONIZED! <<<")
            return True
        time.sleep(3)
    return False

if __name__ == "__main__":
    success = verify_all()
    sys.exit(0 if success else 1)
