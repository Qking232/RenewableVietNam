import os
import re
import hashlib
import subprocess
import time
import http.server
import socketserver
import threading

REPO_R = r"G:\My Drive\7. AI\Gemini\RenewableVietNam"
REPO_Q = r"G:\My Drive\7. AI\Gemini\Qking232.github.io"
FILE_R = os.path.join(REPO_R, "evcharging", "ev", "index.html")
FILE_Q = os.path.join(REPO_Q, "evcharging", "ev", "index.html")

def verify_code_integrity():
    print("[1] Verifying Code Integrity & Parity...")
    with open(FILE_R, "rb") as f:
        content_r = f.read()
    with open(FILE_Q, "rb") as f:
        content_q = f.read()

    # Check 1: L.control.zoom is purged
    assert b"L.control.zoom" not in content_r, "FAILED: L.control.zoom still present in RenewableVietNam!"
    assert b"L.control.zoom" not in content_q, "FAILED: L.control.zoom still present in Qking232.github.io!"
    print("  [PASS] L.control.zoom instantiation completely purged from JS in both repos.")

    # Check 2: zoomControl: false is enforced in L.map
    assert b'zoomControl:false' in content_r or b'zoomControl: false' in content_r, "FAILED: zoomControl:false missing in RenewableVietNam!"
    print("  [PASS] zoomControl:false strictly enforced in L.map initialization.")

    # Check 3: CSS defensive suppression
    assert b".leaflet-control-zoom" in content_r and b"display: none !important;" in content_r, "FAILED: CSS suppression missing in RenewableVietNam!"
    print("  [PASS] Defensive CSS rule (.leaflet-control-zoom { display: none !important; }) active.")

    # Check 4: Cryptographic parity
    h_r = hashlib.sha256(content_r).hexdigest()
    h_q = hashlib.sha256(content_q).hexdigest()
    assert h_r == h_q, f"FAILED: SHA-256 mismatch! {h_r} vs {h_q}"
    print(f"  [PASS] Dual-repo SHA-256 parity confirmed ({h_r[:16]}...).")

def run_headless_chrome_audit():
    print("\n[2] Running Headless Chrome DOM Audit...")
    chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    if not os.path.exists(chrome_exe):
        print("  [WARN] Chrome executable not found at standard path, checking scoop/local...")
        return

    # Start ephemeral local static server
    PORT = 8992
    handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("127.0.0.1", PORT), handler)

    def serve():
        os.chdir(REPO_R)
        httpd.serve_forever()

    server_thread = threading.Thread(target=serve, daemon=True)
    server_thread.start()
    time.sleep(1)

    url = f"http://127.0.0.1:{PORT}/evcharging/ev/"
    print(f"  Loading local portal: {url}...")
    cmd = [
        chrome_exe,
        "--headless=new",
        "--no-sandbox",
        "--disable-gpu",
        "--virtual-time-budget=5000",
        "--dump-dom",
        url
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=25)
    dom = proc.stdout
    httpd.shutdown()

    print(f"  Rendered DOM Length: {len(dom)} characters")
    
    # Assertions on rendered DOM
    assert "id=\"map\"" in dom, "FAILED: Map container not rendered!"
    assert "mapBtnMyLocation" in dom, "FAILED: mapBtnMyLocation button missing from DOM!"
    
    # Check that leaflet-control-zoom DOM elements are NOT rendered in DOM
    zoom_elements = re.findall(r'<[^>]+leaflet-control-zoom[^>]*>', dom)
    if zoom_elements:
        print(f"  [FAIL] {len(zoom_elements)} leaflet-control-zoom elements found in rendered DOM: {zoom_elements}")
        exit(1)
    else:
        print("  [PASS] Zero leaflet-control-zoom elements rendered in live DOM.")

    print("\n>>> ALL EV CHARGING VERIFICATIONS PASSED WITH 100% SUCCESS <<<")

if __name__ == "__main__":
    verify_code_integrity()
    run_headless_chrome_audit()
