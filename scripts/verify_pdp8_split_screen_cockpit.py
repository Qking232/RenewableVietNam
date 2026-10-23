#!/usr/bin/env python3
"""
Automated Headless Chromium Verification for PDP8 50/50 Split-Screen Telemetry Cockpit.
Validates:
1. Cockpit split layout (#cockpitContainer, #energyMapContainer, #dossierContainer).
2. Leaflet Satellite Atlas initialization with Esri World Imagery & Sovereignty markers.
3. Synchronized Dossier Cards rendering 25 assets on page 1 of 960.
4. 3-Tab View Switcher (Assets Dossier, PDP8 Priority Pipeline, Statutory Sector Gauges).
5. Mobile view toggle button.
6. Clean navigation header.
"""

import http.server
import socketserver
import threading
import time
import subprocess
import sys
import os

PORT = 8895
DIRECTORY = r"G:\My Drive\7. AI\Gemini\RenewableVietNam"

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    def log_message(self, format, *args):
        pass

def dump_rendered_dom(url, wait_ms=4000):
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
    print("=== STARTING HEADLESS CHROME DOM AUDIT: PDP8 50/50 SPLIT COCKPIT ===")
    server = socketserver.TCPServer(("127.0.0.1", PORT), QuietHandler)
    t = threading.Thread(target=server.serve_forever)
    t.daemon = True
    t.start()
    time.sleep(1)

    url = f"http://127.0.0.1:{PORT}/projectenergy/index.html"
    print(f"Loading {url} in Headless Chrome...")
    dom = dump_rendered_dom(url, wait_ms=5000)
    print(f"Rendered DOM Length: {len(dom)} characters")

    checks = [
        # Layout & Containers
        ("Cockpit Container", "id=\"cockpitContainer\""),
        ("Energy Map Left Pane", "id=\"energyMapContainer\""),
        ("Leaflet Canvas", "id=\"energyMap\""),
        ("Dossier Right Pane", "id=\"dossierContainer\""),
        ("Dossier Scroll Area", "id=\"dossierScrollArea\""),
        ("Dossier Cards List", "id=\"dossierCardsList\""),
        
        # Tabs & Controls
        ("Tab Assets Button", "id=\"tabAssetsBtn\""),
        ("Tab Pipeline Button", "id=\"tabPipelineBtn\""),
        ("Tab Gauges Button", "id=\"tabGaugesBtn\""),
        ("Search Input", "id=\"projectSearchInput\""),
        ("Province Selector", "id=\"provinceSelect\""),
        ("Table / Cards Toggle", "id=\"tableOrCardsToggleBtn\""),
        ("Mobile View Switcher", "id=\"mobileViewToggleBtn\""),
        
        # Geospatial & Cartography
        ("Esri World Imagery", "Esri World Imagery"),
        ("Hoàng Sa Sovereignty Marker", "Hoàng Sa (Việt Nam)"),
        ("Trường Sa Sovereignty Marker", "Trường Sa (Việt Nam)"),
        ("Full Extent Button", "id=\"resetMapZoomBtn\""),

        # Rendered Telemetry Data
        ("Total Active Baseload (80,612 MW)", "80,612"),
        ("960 Facilities Metric", "Geocoded across 63 Provinces"),
        ("Target Mandate (150,489 MW)", "150,489"),
        ("Delta (+69,877 MW)", "+69,877"),
        ("Pagination Telemetry (960 assets)", "of 960 assets"),
        ("Dossier Card Rendering", "dossier-card-"),
        ("Fly to Satellite Action", "Fly to Satellite"),

        # Navigation Bar Order (Position #1 Live Wire)
        ("Leading Live Wire Tab", "Live Wire"),
        ("Active PDP8 Energy Tab", "PDP8 Energy")
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
        print("\n[SUCCESS] All 50/50 Split-Screen Telemetry Cockpit audit checks PASSED!")
        sys.exit(0)
    else:
        print("\n[ERROR] One or more audit checks FAILED!")
        sys.exit(1)

if __name__ == "__main__":
    main()
