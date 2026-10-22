import urllib.request
import time

urls = [
    'https://renewablevietnam.com/',
    'https://renewablevietnam.com/green/',
    'https://qking232.github.io/',
    'https://qking232.github.io/green/'
]

for attempt in range(1, 10):
    all_ready = True
    print(f"Attempt {attempt}:")
    for u in urls:
        try:
            req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = resp.read()
                has_sidebar = b'id="toolsSidebar"' in data
                has_7xl = b'max-w-7xl' in data
                print(f"  {resp.status} | Len: {len(data):>7} | Sidebar: {has_sidebar} | Max7xl: {has_7xl} | {u}")
                if not has_sidebar or not has_7xl:
                    all_ready = False
        except Exception as e:
            print(f"  ERR | {e} | {u}")
            all_ready = False
    if all_ready:
        print("\n[SUCCESS] All live endpoints serving Left Sidebar Workspace!")
        break
    time.sleep(5)
