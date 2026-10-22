import http.server
import socketserver
import threading
import time
import subprocess
import os

PORT = 8893
DIRECTORY = r"G:\My Drive\7. AI\Gemini\RenewableVietNam"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def audit_url(url, required_tokens):
    chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    cmd = [chrome_exe, "--headless=new", "--no-sandbox", "--disable-gpu", "--virtual-time-budget=6000", "--dump-dom", url]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    dom = proc.stdout
    print(f"\n--- Auditing: {url} (Rendered DOM Length: {len(dom)} chars) ---")
    all_ok = True
    for t in required_tokens:
        found = t in dom
        status = "PASS" if found else "FAIL"
        print(f"  [{status}] Token: {t}")
        if not found:
            all_ok = False
    return all_ok

def main():
    server = socketserver.TCPServer(("127.0.0.1", PORT), Handler)
    t = threading.Thread(target=server.serve_forever)
    t.daemon = True
    t.start()
    time.sleep(1)

    tests = [
        (f"http://127.0.0.1:{PORT}/index.html", [
            "Industrial Hubs",
            "RENEWABLE INFRASTRUCTURE",
            "Geospatial Clean Power Grid",
            "Satellite (Esri World Imagery)",
            "pdp8ProjectsGrid"
        ]),
        (f"http://127.0.0.1:{PORT}/projectenergy/index.html", [
            "Energy Map",
            "80,612",
            "Geospatial Generation Asset Atlas",
            "Satellite (Esri World Imagery)",
            "projectsTableBody"
        ]),
        (f"http://127.0.0.1:{PORT}/evcharging/index.html", [
            "EV Stations",
            "22,055",
            "Geospatial EV Station Atlas",
            "Satellite (Esri World Imagery)",
            "evTableBody",
            "evcharging/ev"
        ]),
        (f"http://127.0.0.1:{PORT}/evcharging/ev/index.html", [
            "22,055",
            "mapWrap",
            "itinPickDepart"
        ]),
        (f"http://127.0.0.1:{PORT}/calculator/index.html", [
            "Power Sizer & Tariffs",
            "calcDemandSlider",
            "calcMwhSlider"
        ])
    ]

    overall_pass = True
    for url, tokens in tests:
        if not audit_url(url, tokens):
            overall_pass = False

    server.shutdown()

    if overall_pass:
        print("\n>>> ALL 5 PORTAL ROUTES DYNAMICALLY RENDERED & VERIFIED WITH 100% SUCCESS! <<<")
    else:
        print("\n>>> ONE OR MORE ROUTES FAILED VERIFICATION! <<<")
        exit(1)

if __name__ == "__main__":
    main()
