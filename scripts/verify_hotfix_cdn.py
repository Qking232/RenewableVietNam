import urllib.request
import time
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

URLS = [
    "https://renewablevietnam.com/",
    "https://renewablevietnam.com/green/",
    "https://qking232.github.io/",
    "https://qking232.github.io/green/"
]

def check_url(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            content = resp.read().decode("utf-8", errors="ignore")
            # Check for bad token specific to the removed basemap switcher
            bad_token = 'btn.classList.remove("bg-white", "dark:bg-darkCard", "text-inkPrimary", "dark:text-textDarkMuted");'
            has_bad_token = bad_token in content
            has_reset_btn = 'resetMapZoomBtn' in content
            has_satellite = 'Satellite (Esri World Imagery)' in content
            
            if not has_bad_token and has_reset_btn and has_satellite:
                return True, "Fixed & Verified"
            else:
                return False, f"has_bad_token={has_bad_token}, has_reset_btn={has_reset_btn}"
    except Exception as e:
        return False, str(e)

def main():
    print("Auditing live CDNs for JavaScript hotfix propagation...", flush=True)
    for attempt in range(1, 15):
        print(f"\nAttempt {attempt} of 15:", flush=True)
        all_ok = True
        for u in URLS:
            ok, msg = check_url(u)
            status = "LIVE HOTFIX OK" if ok else "PROPAGATING"
            print(f"[{status}] {u} -> {msg}", flush=True)
            if not ok:
                all_ok = False
        if all_ok:
            print("\n>>> ALL PRODUCTION CDNS FULLY PROPAGATED & VERIFIED! <<<", flush=True)
            return
        time.sleep(4)

if __name__ == "__main__":
    main()
