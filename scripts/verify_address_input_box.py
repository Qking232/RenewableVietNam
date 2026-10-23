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
    with open(FILE_R, "r", encoding="utf-8") as f:
        content_r = f.read()
    with open(FILE_Q, "r", encoding="utf-8") as f:
        content_q = f.read()

    # Check 1: mapBtnSelectLocation purged
    assert 'id="mapBtnSelectLocation"' not in content_r, "FAILED: mapBtnSelectLocation still present in RenewableVietNam!"
    assert 'id="mapBtnSelectLocation"' not in content_q, "FAILED: mapBtnSelectLocation still present in Qking232.github.io!"
    print("  [PASS] mapBtnSelectLocation icon successfully purged from bottom-right dock.")

    # Check 2: mapBtnMyLocation retained
    assert 'id="mapBtnMyLocation"' in content_r, "FAILED: mapBtnMyLocation missing in RenewableVietNam!"
    assert 'id="mapBtnMyLocation"' in content_q, "FAILED: mapBtnMyLocation missing in Qking232.github.io!"
    print("  [PASS] mapBtnMyLocation preserved in bottom-right floating dock.")

    # Check 3: selectLocPopover & customAddressInput injected
    assert 'id="selectLocPopover"' in content_r and 'id="customAddressInput"' in content_r, "FAILED: Popover missing in RenewableVietNam!"
    assert 'id="selectLocPopover"' in content_q and 'id="customAddressInput"' in content_q, "FAILED: Popover missing in Qking232.github.io!"
    print("  [PASS] selectLocPopover and customAddressInput verified in both repos.")

    # Check 4: window.geocode exported
    assert 'window.geocode = geocode;' in content_r, "FAILED: window.geocode not exported in RenewableVietNam!"
    assert 'window.geocode = geocode;' in content_q, "FAILED: window.geocode not exported in Qking232.github.io!"
    print("  [PASS] window.geocode export verified.")

    # Check 5: Cryptographic parity
    h_r = hashlib.sha256(content_r.encode('utf-8')).hexdigest()
    h_q = hashlib.sha256(content_q.encode('utf-8')).hexdigest()
    assert h_r == h_q, f"FAILED: SHA-256 mismatch! {h_r} vs {h_q}"
    print(f"  [PASS] Dual-repo SHA-256 parity confirmed ({h_r[:16]}...).")

def run_headless_chrome_audit():
    print("\n[2] Running Headless Chrome DOM Audit...")
    chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    if not os.path.exists(chrome_exe):
        print("  [WARN] Chrome executable not found, skipping headless DOM audit.")
        return

    PORT = 8993
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

    # Verify DOM elements
    assert "mapBtnMyLocation" in dom, "FAILED: mapBtnMyLocation missing in rendered DOM!"
    assert "mapBtnSelectLocation" not in dom, "FAILED: mapBtnSelectLocation unexpectedly present in rendered DOM!"
    print("  [PASS] Rendered DOM verified: mapBtnSelectLocation purged, mapBtnMyLocation active.")

    assert "selectLocPopover" in dom, "FAILED: selectLocPopover missing in rendered DOM!"
    assert "customAddressInput" in dom, "FAILED: customAddressInput missing in rendered DOM!"
    assert "btnSubmitCustomAddress" in dom, "FAILED: btnSubmitCustomAddress missing in rendered DOM!"
    assert "quick-city-chip" in dom, "FAILED: quick-city-chip missing in rendered DOM!"
    print("  [PASS] Rendered DOM verified: selectLocPopover with address input & city chips present.")

    print("\n>>> ALL SELECT LOCATION & ADDRESS BOX VERIFICATIONS PASSED WITH 100% SUCCESS <<<")

if __name__ == "__main__":
    verify_code_integrity()
    run_headless_chrome_audit()
