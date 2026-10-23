#!/usr/bin/env python3
"""
Automated Headless Chromium Verification for Repositioned Power Sizer in index.html.
"""

import http.server
import socketserver
import threading
import time
import subprocess
import sys

PORT = 8901
DIRECTORY = r"G:\My Drive\7. AI\Gemini\RenewableVietNam"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    def log_message(self, format, *args):
        pass

def dump_dom(url, wait_ms=4500):
    chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    cmd = [
        chrome_exe,
        "--headless=new",
        "--no-sandbox",
        "--disable-gpu",
        f"--virtual-time-budget={wait_ms}",
        "--dump-dom",
        url
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=35)
    return proc.stdout

def main():
    print("=== STARTING HEADLESS CHROME AUDIT: REPOSITIONED POWER SIZER ABOVE MAP ===")
    server = socketserver.TCPServer(("127.0.0.1", PORT), Handler)
    t = threading.Thread(target=server.serve_forever)
    t.daemon = True
    t.start()
    time.sleep(1)

    url = f"http://127.0.0.1:{PORT}/index.html"
    print(f"Loading {url} in Headless Chrome...")
    dom = dump_dom(url, wait_ms=5000)
    print(f"Rendered DOM Length: {len(dom)} characters")

    pos_sizer = dom.find('id="powerSizer"')
    pos_hubs = dom.find('id="hubs"')

    all_passed = True

    # 1. Check relative order
    if pos_sizer != -1 and pos_hubs != -1 and pos_sizer < pos_hubs:
        print(f"  [PASS] Order check: #powerSizer (idx {pos_sizer}) precedes #hubs (idx {pos_hubs})")
    else:
        print(f"  [FAIL] Order check: #powerSizer (idx {pos_sizer}) does not precede #hubs (idx {pos_hubs})")
        all_passed = False

    # 2. Check forbidden link
    forbidden_token = "Open Full Tariff Suite"
    if forbidden_token in dom:
        print(f"  [FAIL] Forbidden link found: '{forbidden_token}'")
        all_passed = False
    else:
        print(f"  [PASS] Forbidden link absent: '{forbidden_token}'")

    # 3. Check power sizer elements
    checks = [
        ("Power Sizer Header", "Corporate Clean Power Siting &amp; Allocation Sizer"),
        ("Grid Baseline Badge", "0.7221 tCO"),
        ("Demand Slider", 'id="calcDemandSlider"'),
        ("Monthly MWh Slider", 'id="calcMwhSlider"'),
        ("RE100 Slider", 'id="calcReSlider"'),
        ("Rooftop PV Output", 'id="calcRooftopPv"'),
        ("DPPA Wheeling Gap Output", 'id="calcDppaGap"'),
        ("Grid Firming Output", 'id="calcGridFirming"'),
        ("Scope 2 Avoided Output", 'id="calcCo2Avoided"'),
        ("Recommended Hubs Box", 'id="calcRecommendedHubs"'),
        ("Jump to Hub Function", 'jumpToHub('),
        ("Copy Siting Brief", 'id="copyCalcBriefBtn"'),
        ("50/50 Cockpit Container", 'id="hubCockpitContainer"'),
        ("Satellite Map Canvas", 'id="ecoParkMap"'),
        ("Hub Dossier Container", 'id="hubDossierContainer"'),
        ("Hub Dossier Cards", 'hub-card-'),
        ("Hoàng Sa Sovereignty", 'Hoàng Sa (Việt Nam)'),
        ("Trường Sa Sovereignty", 'Trường Sa (Việt Nam)'),
        ("Leading Live Wire Tab", 'Live Wire')
    ]

    for label, token in checks:
        found = token in dom
        status = "PASS" if found else "FAIL"
        print(f"  [{status}] {label}: '{token}'")
        if not found:
            all_passed = False

    server.shutdown()
    if all_passed:
        print("\n[SUCCESS] All checks for Repositioned Power Sizer above Map in index.html PASSED!")
        sys.exit(0)
    else:
        print("\n[ERROR] One or more checks FAILED!")
        sys.exit(1)

if __name__ == "__main__":
    main()
