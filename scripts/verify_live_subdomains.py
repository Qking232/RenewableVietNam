import subprocess

urls = [
    "https://ind.renewablevietnam.com/",
    "https://ev.renewablevietnam.com/",
    "https://energy.renewablevietnam.com/",
    "https://legal.renewablevietnam.com/"
]

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
for u in urls:
    res = subprocess.run(
        [chrome, "--headless=new", "--no-sandbox", "--disable-gpu", "--virtual-time-budget=5000", "--dump-dom", u],
        capture_output=True,
        text=True,
        timeout=15
    )
    dom = res.stdout
    end = dom.find(">") + 1 if ">" in dom else 100
    tag = dom[:end]
    has_dark = 'class="dark"' in tag or 'data-theme="dark"' in tag
    has_v2 = "rvn_theme_v2" in dom
    print(f"[AUDIT] {u}")
    print(f"        Tag: {tag}")
    print(f"        Dark flag in tag: {has_dark}")
    print(f"        rvn_theme_v2 present: {has_v2}")
