#!/usr/bin/env python3
import http.server
import socketserver
import threading
import time
import subprocess
import os
import sys

PORT = 8894
DIRECTORY = r"G:\My Drive\7. AI\Gemini\RenewableVietNam"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    def log_message(self, format, *args):
        pass # suppress server logs

def audit_url(url, required_tokens, forbidden_tokens=[]):
    chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    cmd = [chrome_exe, "--headless=new", "--no-sandbox", "--disable-gpu", "--virtual-time-budget=6000", "--dump-dom", url]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    dom = proc.stdout
    print(f"\n--- Auditing: {url} (Rendered DOM Length: {len(dom)} chars) ---")
    all_ok = True
    for t in required_tokens:
        found = t in dom
        status = "PASS" if found else "FAIL"
        print(f"  [{status}] Required: '{t}'")
        if not found:
            all_ok = False
    for f in forbidden_tokens:
        found = f in dom
        status = "FAIL (Forbidden found)" if found else "PASS (Clean)"
        print(f"  [{status}] Forbidden: '{f}'")
        if found:
            all_ok = False
    return all_ok

def main():
    server = socketserver.TCPServer(("127.0.0.1", PORT), Handler)
    t = threading.Thread(target=server.serve_forever)
    t.daemon = True
    t.start()
    time.sleep(1)

    tests = [
        (f"http://127.0.0.1:{PORT}/livewire/index.html", [
            "Vietnam Clean Energy &amp; Infrastructure Live Wire",
            "BREAKING #1",
            "BREAKING #5",
            "Breaking Market Signals",
            "50",
            "EV Tech",
            "Legal Framework",
            "Live Wire",
            "Solar & Wind"
        ], [
            "id=\"marketWire\""
        ]),
        (f"http://127.0.0.1:{PORT}/index.html", [
            "Vietnam Renewable Industrial Hubs &amp; Clean Siting Portal",
            "Industrial Hubs",
            "PDP8 Energy",
            "EV Tech",
            "Legal Framework",
            "/livewire/"
        ], [
            "id=\"marketWire\"",
            "id=\"breakingTickerContainer\"",
            "fetchNewsData();"
        ]),
        (f"http://127.0.0.1:{PORT}/projectenergy/index.html", [
            "PDP8 Energy",
            "EV Tech",
            "Legal Framework",
            "/livewire/"
        ], [])
    ]

    all_passed = True
    for url, req, forb in tests:
        if not audit_url(url, req, forb):
            all_passed = False

    server.shutdown()
    if all_passed:
        print("\n[SUCCESS] All DOM and dynamic telemetry rendering verification tests PASSED!")
        sys.exit(0)
    else:
        print("\n[ERROR] One or more verification checks failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
