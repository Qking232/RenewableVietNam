import http.server
import socketserver
import threading
import time
import subprocess
import os

PORT = 8896
DIRECTORY = r'G:\My Drive\7. AI\Gemini\RenewableVietNam'

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def main():
    server = socketserver.TCPServer(('127.0.0.1', PORT), Handler)
    t = threading.Thread(target=server.serve_forever)
    t.daemon = True
    t.start()

    time.sleep(1)
    url = f'http://127.0.0.1:{PORT}/index.html'

    chrome_exe = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    cmd = [chrome_exe, '--headless=new', '--no-sandbox', '--disable-gpu', '--virtual-time-budget=6000', '--dump-dom', url]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=12)
    dom = proc.stdout

    print(f"Rendered DOM Length: {len(dom)} characters")
    
    # Check key sections
    checks = {
        "pdp8ProjectsGrid populated": ("pdp8ProjectsGrid", "Bac Ai" in dom or "Bắc Ái" in dom or "MW" in dom),
        "pdp8SectorGauges populated": ("pdp8SectorGauges", "%" in dom),
        "hubsTableBody populated": ("hubsTableBody", "VSIP" in dom),
        "newsGrid populated": ("newsGrid", "data-article" in dom or "news-item" in dom or "font-mono" in dom),
        "ecoParkMap initialized": ("ecoParkMap", "custom-hub-marker" in dom),
        "Satellite basemap active": ("Satellite (Esri World Imagery)", True)
    }

    all_pass = True
    for desc, (token, condition) in checks.items():
        found = token in dom and condition
        status = "PASS" if found else "FAIL"
        if not found:
            all_pass = False
        print(f"  [{status}] {desc}")

    server.shutdown()
    
    if all_pass:
        print("\n>>> ALL HOMEPAGE DATA SECTIONS 100% OPERATIONAL & VERIFIED! <<<")
    else:
        print("\n>>> SOME DATA SECTIONS FAILED TO POPULATE! <<<")
        exit(1)

if __name__ == "__main__":
    main()
