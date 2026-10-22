import urllib.request
import time

urls = [
    'https://renewablevietnam.com/evcharging/',
    'https://qking232.github.io/evcharging/'
]

for attempt in range(1, 12):
    all_ready = True
    print(f"Attempt {attempt}:")
    for u in urls:
        try:
            req = urllib.request.Request(f"{u}?v={int(time.time())}", headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = resp.read()
                has_btn_in_chips = b'id="btnMyLocation"' in data
                has_fab = b'id="mapBtnMyLocation"' in data
                has_css = b'bottom: 32px' in data
                print(f"  {resp.status} | Len: {len(data):>7} | ChipRemoved: {not has_btn_in_chips} | FABExists: {has_fab} | CSS32px: {has_css} | {u}")
                if has_btn_in_chips or not has_fab or not has_css:
                    all_ready = False
        except Exception as e:
            print(f"  ERR | {e} | {u}")
            all_ready = False
    if all_ready:
        print("\n[SUCCESS] Both live EV Charging endpoints serving icon-only bottom-right My Location FAB!")
        break
    time.sleep(6)
