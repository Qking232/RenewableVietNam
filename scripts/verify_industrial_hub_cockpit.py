#!/usr/bin/env python3
"""
Automated Headless Chromium Verification for Industrial Hubs 50/50 Split Cockpit in index.html.
"""

import http.server
import socketserver
import threading
import time
import subprocess
import sys

PORT = 8899
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
    print("=== STARTING HEADLESS CHROME AUDIT: INDUSTRIAL HUB 50/50 SPLIT COCKPIT ===")
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
        # Cockpit Containers
        ("Hub Cockpit Container", 'id="hubCockpitContainer"'),
        ("Map Container Left Pane", 'id="ecoParkMapContainer"'),
        ("Leaflet Map Canvas", 'id="ecoParkMap"'),
        ("Dossier Right Pane", 'id="hubDossierContainer"'),
        ("Dossier Scroll Area", 'id="hubDossierScrollArea"'),
        ("Hub Cards List", 'id="hubCardsList"'),
        ("Cards / Table Toggle", 'id="tableOrCardsToggleBtn"'),
        ("Hubs Table Container", 'id="hubsTableContainer"'),
        ("Mobile View Switcher", 'id="mobileHubViewToggleBtn"'),
        
        # Geospatial & Basemap
        ("Esri World Imagery", 'Esri World Imagery'),
        ("Full Extent Button", 'id="resetMapZoomBtn"'),
        ("Hoàng Sa Sovereignty Marker", 'Hoàng Sa (Việt Nam)'),
        ("Trường Sa Sovereignty Marker", 'Trường Sa (Việt Nam)'),
        ("Active Pins Counter", 'id="visibleHubPinsCount"'),

        # Rendered Dossier Telemetry
        ("168 National Hubs Count", '168</span> national hubs'),
        ("Hub Dossier Card Rendering", 'hub-card-'),
        ("Fly to Satellite Action", 'Fly to Satellite'),
        ("Technical Dossier Action", 'Technical Dossier'),
        ("Rows Pagination Select", 'id="pageSizeSelect"'),

        # Section 2: Power Sizer
        ("Embedded Power Sizer Section", 'id="powerSizer"'),
        ("Power Sizer Sliders", 'id="calcDemandSlider"'),
        ("Power Sizer Output", 'id="calcRooftopPv"'),

        # Navigation Header
        ("Leading Live Wire Tab", 'Live Wire'),
        ("Active Industrial Hubs Tab", 'Industrial Hubs')
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
        print("\n[SUCCESS] All checks for Industrial Hub 50/50 Split Cockpit in index.html PASSED!")
        sys.exit(0)
    else:
        print("\n[ERROR] One or more checks FAILED!")
        sys.exit(1)

if __name__ == "__main__":
    main()
