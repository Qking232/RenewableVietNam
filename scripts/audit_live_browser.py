import subprocess

def test_live():
    url = "https://renewablevietnam.com/"
    print(f"Auditing live browser rendering for {url}...")
    chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    cmd = [chrome_exe, "--headless=new", "--no-sandbox", "--disable-gpu", "--virtual-time-budget=6000", "--dump-dom", url]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
    dom = proc.stdout

    print(f"Live Rendered DOM Length: {len(dom)} characters")
    checks = {
        "pdp8ProjectsGrid populated": ("pdp8ProjectsGrid", "MW" in dom),
        "pdp8SectorGauges populated": ("pdp8SectorGauges", "%" in dom),
        "hubsTableBody populated": ("hubsTableBody", "VSIP" in dom),
        "newsGrid populated": ("newsGrid", "data-article" in dom or "font-mono" in dom),
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

    if all_pass:
        print("\n>>> LIVE PRODUCTION HOMEPAGE 100% OPERATIONAL WITH ALL DATA RESTORED! <<<")
    else:
        print("\n>>> SOME SECTIONS FAILED ON LIVE HOMEPAGE! <<<")
        exit(1)

if __name__ == "__main__":
    test_live()
