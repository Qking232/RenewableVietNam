import os
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
    content_r = open(FILE_R, "r", encoding="utf-8").read()
    content_q = open(FILE_Q, "r", encoding="utf-8").read()

    # Check 1: btnSelectLocation purged
    assert 'id="btnSelectLocation"' not in content_r, "FAILED: btnSelectLocation found in RenewableVietNam!"
    assert 'id="btnSelectLocation"' not in content_q, "FAILED: btnSelectLocation found in Qking232.github.io!"
    print("  [PASS] #btnSelectLocation completely purged from HTML.")

    # Check 2: selectLocPopover purged
    assert 'id="selectLocPopover"' not in content_r, "FAILED: selectLocPopover found in RenewableVietNam!"
    assert 'id="selectLocPopover"' not in content_q, "FAILED: selectLocPopover found in Qking232.github.io!"
    print("  [PASS] #selectLocPopover completely purged from HTML.")

    # Check 3: Active chips preserved
    assert 'id="chipItinToggle"' in content_r and 'id="pillNear"' in content_r, "FAILED: Essential chips missing!"
    print("  [PASS] Essential chips (chipItinToggle, pillNear) intact.")

    # Check 4: mapBtnMyLocation preserved
    assert 'id="mapBtnMyLocation"' in content_r, "FAILED: mapBtnMyLocation missing!"
    print("  [PASS] #mapBtnMyLocation preserved in floating dock.")

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

    PORT = 8994
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

    # Assertions
    assert "btnSelectLocation" not in dom, "FAILED: btnSelectLocation found in rendered DOM!"
    assert "selectLocPopover" not in dom, "FAILED: selectLocPopover found in rendered DOM!"
    print("  [PASS] Zero Select Location buttons or popovers rendered in live DOM.")

    assert "chipItinToggle" in dom, "FAILED: chipItinToggle missing in DOM!"
    assert "pillNear" in dom, "FAILED: pillNear missing in DOM!"
    assert "mapBtnMyLocation" in dom, "FAILED: mapBtnMyLocation missing in DOM!"
    print("  [PASS] Core elements (chipItinToggle, pillNear, mapBtnMyLocation) fully rendered.")

    print("\n>>> ALL REMOVAL VERIFICATIONS PASSED WITH 100% SUCCESS <<<")

if __name__ == "__main__":
    verify_code_integrity()
    run_headless_chrome_audit()
