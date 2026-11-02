import http.server
import socketserver
import threading
import subprocess
import time
import sys
import os

PORT = 8993
DIRECTORY = r"G:\My Drive\7. AI\RenewableVietNam"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    def log_message(self, format, *args):
        pass

def run_chrome(url):
    chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    cmd = [
        chrome_exe,
        "--headless=new",
        "--no-sandbox",
        "--disable-gpu",
        "--virtual-time-budget=5000",
        "--dump-dom",
        url
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
    return proc.stdout

def main():
    print("[TEST SETUP] Starting local test HTTP server...")
    server = socketserver.TCPServer(("127.0.0.1", PORT), Handler)
    t = threading.Thread(target=server.serve_forever)
    t.daemon = True
    t.start()
    time.sleep(1)

    url = f"http://127.0.0.1:{PORT}/index.html"
    print(f"[TEST EXECUTION] Launching Headless Chrome against {url}...")
    dom = run_chrome(url)

    failures = 0

    # 1. Check Root Element Tag in Rendered DOM
    print("\n--- TEST 1: Root Element Theme Verification ---")
    if 'class="dark"' in dom[:500]:
        print("[-] FAIL: Rendered <html> tag contains static 'class=\"dark\"' attribute.")
        failures += 1
    else:
        print("[+] PASS: Rendered <html> tag does NOT contain 'dark' class by default.")

    # 2. Check Anti-FOUC Script in Head with rvn_theme_v2
    print("\n--- TEST 2: Anti-FOUC Script Key Verification ---")
    if "localStorage.getItem('rvn_theme_v2')" in dom and "document.documentElement.classList.add('dark')" in dom:
        print("[+] PASS: Anti-FOUC inline script correctly reads versioned 'rvn_theme_v2' key.")
    else:
        print("[-] FAIL: Anti-FOUC script does not use 'rvn_theme_v2'.")
        failures += 1

    # 3. Check Toggle Button Icon States
    print("\n--- TEST 3: Theme Toggle Button Icon State Verification ---")
    if 'id="sunIcon"' in dom and 'hidden' in dom[dom.find('id="sunIcon"') - 50:dom.find('id="sunIcon"') + 50]:
        print("[+] PASS: Sun icon is hidden in default light mode.")
    else:
        print("[-] FAIL: Sun icon is not hidden in default light mode.")
        failures += 1

    moon_idx = dom.find('id="moonIcon"')
    if moon_idx != -1:
        moon_snippet = dom[moon_idx - 50:moon_idx + 50]
        if "hidden" not in moon_snippet:
            print("[+] PASS: Moon icon is visible in default light mode.")
        else:
            print("[-] FAIL: Moon icon is unexpectedly hidden in default light mode.")
            failures += 1
    else:
        print("[-] FAIL: Moon icon not found in rendered DOM.")
        failures += 1

    # 4. Check Theme Evaluation Logic in Script
    print("\n--- TEST 4: Script Evaluation Logic Verification ---")
    if "applyTheme(savedTheme === 'dark')" in dom and "localStorage.getItem('rvn_theme_v2')" in dom:
        print("[+] PASS: Theme initialization strictly evaluates `applyTheme(savedTheme === 'dark')` with 'rvn_theme_v2'.")
    else:
        print("[-] FAIL: Theme initialization logic does not enforce `savedTheme === 'dark'` with 'rvn_theme_v2'.")
        failures += 1

    # 5. Interactive Theme Toggle & Legacy Poisoning Invalidation Harness
    print("\n--- TEST 5: Legacy Poisoning Invalidation & Interactive Behavior ---")
    harness_path = os.path.join(DIRECTORY, "scripts", "temp_theme_harness.html")
    harness_html = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Theme Test Harness</title>
</head>
<body>
  <iframe id="testFrame" src="/index.html" style="width: 800px; height: 600px;"></iframe>
  <div id="results"></div>
  <script>
    const frame = document.getElementById('testFrame');
    frame.onload = function() {{
      try {{
        const doc = frame.contentDocument;
        const win = frame.contentWindow;
        const res = document.getElementById('results');
        const log = [];

        // Simulate legacy poisoned state: visitor previously had localStorage.setItem('theme', 'dark')
        win.localStorage.setItem('theme', 'dark');

        // Check 1: Even with legacy 'theme'='dark', site MUST remain in light mode by default!
        const initialDark = doc.documentElement.classList.contains('dark');
        log.push('POISONED_LEGACY_IS_DARK=' + initialDark);

        // Check 2: Click toggle button -> activates dark mode
        const btn = doc.getElementById('themeToggleBtn');
        btn.click();
        const afterClick1Dark = doc.documentElement.classList.contains('dark');
        const storedTheme1 = win.localStorage.getItem('rvn_theme_v2');
        log.push('CLICK1_IS_DARK=' + afterClick1Dark);
        log.push('STORED_V2_THEME1=' + storedTheme1);

        // Check 3: Click toggle button again -> reverts to light mode
        btn.click();
        const afterClick2Dark = doc.documentElement.classList.contains('dark');
        const storedTheme2 = win.localStorage.getItem('rvn_theme_v2');
        log.push('CLICK2_IS_DARK=' + afterClick2Dark);
        log.push('STORED_V2_THEME2=' + storedTheme2);

        res.innerHTML = '<pre id="testOutput">' + log.join('\\n') + '</pre>';
      }} catch (err) {{
        document.getElementById('results').innerHTML = '<pre id="testOutput">ERROR: ' + err.message + '</pre>';
      }}
    }};
  </script>
</body>
</html>"""

    with open(harness_path, "w", encoding="utf-8") as f:
        f.write(harness_html)

    harness_url = f"http://127.0.0.1:{PORT}/scripts/temp_theme_harness.html"
    harness_dom = run_chrome(harness_url)

    if os.path.exists(harness_path):
        os.remove(harness_path)

    if "POISONED_LEGACY_IS_DARK=false" in harness_dom:
        print("[+] PASS: Legacy poisoned localStorage ('theme'='dark') is successfully ignored; site remains LIGHT by default.")
    else:
        print("[-] FAIL: Legacy poisoned state caused site to revert to dark mode.")
        failures += 1

    if "CLICK1_IS_DARK=true" in harness_dom and "STORED_V2_THEME1=dark" in harness_dom:
        print("[+] PASS: Clicking themeToggleBtn transitions to dark mode and writes rvn_theme_v2='dark'.")
    else:
        print("[-] FAIL: First click did not transition correctly to dark mode.")
        failures += 1

    if "CLICK2_IS_DARK=false" in harness_dom and "STORED_V2_THEME2=light" in harness_dom:
        print("[+] PASS: Clicking themeToggleBtn second time transitions back to light mode and writes rvn_theme_v2='light'.")
    else:
        print("[-] FAIL: Second click did not revert correctly to light mode.")
        failures += 1

    server.shutdown()

    print("\n=======================================================")
    if failures == 0:
        print("[MODEL VERIFICATION REPORT] ALL THEME TESTS PASSED (100% SUCCESS)")
        sys.exit(0)
    else:
        print(f"[MODEL VERIFICATION REPORT] {failures} TEST(S) FAILED")
        sys.exit(1)

if __name__ == "__main__":
    main()
