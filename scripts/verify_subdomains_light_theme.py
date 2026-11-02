import http.server
import socketserver
import threading
import subprocess
import time
import sys
import os

PORT = 8995
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
    print("[TEST SETUP] Starting local test HTTP server on port", PORT)
    server = socketserver.TCPServer(("127.0.0.1", PORT), Handler)
    t = threading.Thread(target=server.serve_forever)
    t.daemon = True
    t.start()
    time.sleep(1)

    portals = [
        {"name": "ind (green)", "path": "/green/index.html", "type": "class"},
        {"name": "ev (evcharging)", "path": "/evcharging/index.html", "type": "class"},
        {"name": "energy (projectenergy)", "path": "/projectenergy/index.html", "type": "class"},
        {"name": "legal (hub)", "path": "/hub/index.html", "type": "data-theme"}
    ]

    total_failures = 0

    for p in portals:
        url = f"http://127.0.0.1:{PORT}{p['path']}"
        print(f"\n=======================================================")
        print(f"VERIFYING PORTAL: {p['name']} ({url})")
        print(f"=======================================================")
        dom = run_chrome(url)

        # Check 1: Root Element
        if p["type"] == "class":
            if 'class="dark"' in dom[:500]:
                print(f"[-] FAIL [{p['name']}]: Rendered <html> tag contains static 'class=\"dark\"'")
                total_failures += 1
            else:
                print(f"[+] PASS [{p['name']}]: Rendered <html> tag does NOT contain 'dark' class by default.")
        elif p["type"] == "data-theme":
            if 'data-theme="dark"' in dom[:500]:
                print(f"[-] FAIL [{p['name']}]: Rendered <html> tag contains 'data-theme=\"dark\"'")
                total_failures += 1
            else:
                print(f"[+] PASS [{p['name']}]: Rendered <html> tag has data-theme='light' by default.")

        # Check 2: Storage Key
        if "rvn_theme_v2" in dom:
            print(f"[+] PASS [{p['name']}]: Script references versioned key 'rvn_theme_v2'.")
        else:
            print(f"[-] FAIL [{p['name']}]: Missing 'rvn_theme_v2' reference.")
            total_failures += 1

        # Check 3: Interactive Behavioral Simulation in Iframe
        harness_path = os.path.join(DIRECTORY, "scripts", f"temp_harness_{p['name'].split()[0]}.html")
        harness_html = f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"></head>
<body>
  <iframe id="testFrame" src="{p['path']}" style="width: 800px; height: 600px;"></iframe>
  <div id="results"></div>
  <script>
    const frame = document.getElementById('testFrame');
    frame.onload = function() {{
      setTimeout(function() {{
        try {{
          const doc = frame.contentDocument;
          const win = frame.contentWindow;
          const log = [];

          // 1. Initial State
          const isDark = doc.documentElement.classList.contains('dark') || doc.documentElement.getAttribute('data-theme') === 'dark';
          log.push('INITIAL_IS_DARK=' + isDark);

          // 2. Click Theme Toggle Button
          const btn = doc.getElementById('themeToggleBtn') || doc.getElementById('themeBtn');
          if (btn) {{
            btn.click();
            const after1Dark = doc.documentElement.classList.contains('dark') || doc.documentElement.getAttribute('data-theme') === 'dark';
            const stored1 = win.localStorage.getItem('rvn_theme_v2');
            log.push('CLICK1_IS_DARK=' + after1Dark);
            log.push('STORED_V2_1=' + stored1);

            btn.click();
            const after2Dark = doc.documentElement.classList.contains('dark') || doc.documentElement.getAttribute('data-theme') === 'dark';
            const stored2 = win.localStorage.getItem('rvn_theme_v2');
            log.push('CLICK2_IS_DARK=' + after2Dark);
            log.push('STORED_V2_2=' + stored2);
          }} else {{
            log.push('BTN_NOT_FOUND');
          }}

          document.getElementById('results').innerHTML = '<pre>' + log.join('\\n') + '</pre>';
        }} catch (err) {{
          document.getElementById('results').innerHTML = '<pre>ERROR: ' + err.message + '</pre>';
        }}
      }}, 500);
    }};
  </script>
</body>
</html>"""

        with open(harness_path, "w", encoding="utf-8") as f:
            f.write(harness_html)

        harness_url = f"http://127.0.0.1:{PORT}/scripts/{os.path.basename(harness_path)}"
        harness_dom = run_chrome(harness_url)

        if os.path.exists(harness_path):
            os.remove(harness_path)

        if "INITIAL_IS_DARK=false" in harness_dom:
            print(f"[+] PASS [{p['name']}]: Interactive initial load confirmed in light mode (INITIAL_IS_DARK=false).")
        else:
            print(f"[-] FAIL [{p['name']}]: Initial load was not in light mode. Harness output:\n{harness_dom[:300]}")
            total_failures += 1

        if "CLICK1_IS_DARK=true" in harness_dom and "STORED_V2_1=dark" in harness_dom:
            print(f"[+] PASS [{p['name']}]: First click toggles to dark mode and writes rvn_theme_v2='dark'.")
        else:
            print(f"[-] FAIL [{p['name']}]: First click failed to toggle to dark mode.")
            total_failures += 1

        if "CLICK2_IS_DARK=false" in harness_dom and "STORED_V2_2=light" in harness_dom:
            print(f"[+] PASS [{p['name']}]: Second click reverts to light mode and writes rvn_theme_v2='light'.")
        else:
            print(f"[-] FAIL [{p['name']}]: Second click failed to revert to light mode.")
            total_failures += 1

    server.shutdown()

    print("\n=======================================================")
    if total_failures == 0:
        print("[MODEL VERIFICATION REPORT] ALL 4 SUBDOMAINS PASSED LIGHT THEME AUDIT (100% SUCCESS)")
        sys.exit(0)
    else:
        print(f"[MODEL VERIFICATION REPORT] {total_failures} TEST(S) FAILED ACROSS SUBDOMAINS")
        sys.exit(1)

if __name__ == "__main__":
    main()
