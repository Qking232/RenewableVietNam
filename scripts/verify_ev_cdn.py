import urllib.request
import time

urls = [
    'https://renewablevietnam.com/evcharging/',
    'https://qking232.github.io/evcharging/'
]

for attempt in range(1, 10):
    all_ready = True
    print(f"Attempt {attempt}:")
    for u in urls:
        try:
            req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = resp.read()
                has_my_loc = b'id="btnMyLocation"' in data
                has_sel_loc = b'id="btnSelectLocation"' in data
                print(f"  {resp.status} | Len: {len(data):>7} | MyLoc: {has_my_loc} | SelLoc: {has_sel_loc} | {u}")
                if not has_my_loc or not has_sel_loc:
                    all_ready = False
        except Exception as e:
            print(f"  ERR | {e} | {u}")
            all_ready = False
    if all_ready:
        print("\n[SUCCESS] Both live EV Charging endpoints serving My Location & Select Location buttons!")
        break
    time.sleep(5)
