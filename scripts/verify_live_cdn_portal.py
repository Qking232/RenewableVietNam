import urllib.request
import ssl
import time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

ROUTES = [
    ("https://renewablevietnam.com/", ["Industrial Hubs", "bg-alabaster/95", "Satellite (Esri World Imagery)"]),
    ("https://renewablevietnam.com/projectenergy/", ["Energy Map", "80,612", "Satellite (Esri World Imagery)", "projectsTableBody"]),
    ("https://renewablevietnam.com/evcharging/", ["EV Stations", "22,055", "Satellite (Esri World Imagery)", "evTableBody", "evcharging/ev"]),
    ("https://renewablevietnam.com/evcharging/ev/", ["22,055", "mapWrap", "itinPickDepart"]),
    ("https://renewablevietnam.com/calculator/", ["Power Sizer &amp; Tariffs", "calcDemandSlider"]),
    ("https://qking232.github.io/", ["Industrial Hubs", "bg-alabaster/95", "Satellite (Esri World Imagery)"]),
    ("https://qking232.github.io/projectenergy/", ["Energy Map", "80,612", "Satellite (Esri World Imagery)", "projectsTableBody"]),
    ("https://qking232.github.io/evcharging/", ["EV Stations", "22,055", "Satellite (Esri World Imagery)", "evTableBody", "evcharging/ev"]),
    ("https://qking232.github.io/evcharging/ev/", ["22,055", "mapWrap", "itinPickDepart"]),
    ("https://qking232.github.io/calculator/", ["Power Sizer &amp; Tariffs", "calcDemandSlider"])
]

def check_route(url, expected_tokens):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=12) as resp:
            content = resp.read().decode("utf-8", errors="ignore")
            missing = [t for t in expected_tokens if t not in content]
            if not missing:
                return True, f"200 OK & Verified ({len(content)} bytes)"
            else:
                return False, f"Missing tokens: {missing}"
    except Exception as e:
        return False, str(e)

def main():
    print("Auditing live CDNs for universal design unification propagation...", flush=True)
    for attempt in range(1, 15):
        print(f"\nAttempt {attempt} of 15:", flush=True)
        all_ok = True
        for url, tokens in ROUTES:
            ok, msg = check_route(url, tokens)
            status = "LIVE OK" if ok else "PROPAGATING"
            print(f"  [{status}] {url} -> {msg}", flush=True)
            if not ok:
                all_ok = False
        if all_ok:
            print("\n>>> ALL 10 LIVE CDN PRODUCTION ENDPOINTS 100% VERIFIED & SYNCHRONIZED! <<<", flush=True)
            return
        time.sleep(5)

if __name__ == "__main__":
    main()
