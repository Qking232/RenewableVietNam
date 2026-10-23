#!/usr/bin/env python3
"""
Headless Chromium Audit for Relocated Power Sizer Module in index.html.
"""

import http.server
import socketserver
import threading
import time
import subprocess
import sys

PORT = 8897
DIRECTORY = r"G:\My Drive\7. AI\Gemini\RenewableVietNam"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    def log_message(self, format, *args):
        pass

def dump_dom(url, wait_ms=4000):
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
    print("=== STARTING HEADLESS CHROME AUDIT: RELOCATED POWER SIZER IN INDEX.HTML ===")
    server = socketserver.TCPServer(("127.0.0.1", PORT), Handler)
    t = threading.Thread(target=server.serve_forever)
    t.daemon = True
    t.start()
    time.sleep(1)

    url = f"http://127.0.0.1:{PORT}/index.html"
    print(f"Loading {url} in Headless Chrome...")
    dom = dump_dom(url, wait_ms=5000)
    print(f"Rendered DOM Length: {len(dom)} characters")

    checks = [
        ("Power Sizer Section Container", 'id="powerSizer"'),
        ("Power Sizer Header Title", 'Corporate Clean Power Siting &amp; Allocation Sizer'),
        ("Statutory Decrees", 'Decree 80/2024/NĐ-CP DPPA'),
        ("Connected Demand Slider", 'id="calcDemandSlider"'),
        ("Monthly Consumption Slider", 'id="calcMwhSlider"'),
        ("RE100 Target Slider", 'id="calcReSlider"'),
        ("Demand Value Badge", 'id="calcDemandVal"'),
        ("Rooftop PV Output", 'id="calcRooftopPv"'),
        ("DPPA Wheeling Gap Output", 'id="calcDppaGap"'),
        ("Grid Firming Output", 'id="calcGridFirming"'),
        ("Scope 2 CO2e Avoided Output", 'id="calcCo2Avoided"'),
        ("Recommended Hubs Container", 'id="calcRecommendedHubs"'),
        ("Jump to Hub Click Handler", 'jumpToHub('),
        ("Copy Siting Brief Button", 'id="copyCalcBriefBtn"'),
        ("Hero Power Sizer Jump Link", 'href="#powerSizer"'),
        ("Full Tariff Suite Cross-Link", 'href="/calculator/"'),
        ("Industrial Hubs Directory Intact", 'id="hubs"'),
        ("Eco Park Satellite Map Intact", 'id="ecoParkMap"'),
        ("Leading Live Wire Navigation", 'Live Wire')
    ]

    all_passed = True
    for label, token in checks:
        found = token in dom
        status = "PASS" if found else "FAIL"
        print(f"  [{status}] {label}: '{token}'")
        if not found:
            all_passed = False

    server.shutdown()
    if all_passed:
        print("\n[SUCCESS] All checks for Relocated Power Sizer in index.html PASSED!")
        sys.exit(0)
    else:
        print("\n[ERROR] One or more checks FAILED!")
        sys.exit(1)

if __name__ == "__main__":
    main()
