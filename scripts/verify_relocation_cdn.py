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
                idx_market = data.find(b'id="marketWire"')
                idx_pdp8 = data.find(b'PDP8 STATUTORY TRACKER')
                is_relocated = (0 < idx_market < idx_pdp8) if (idx_market > 0 and idx_pdp8 > 0) else False
                print(f"  {resp.status} | Len: {len(data):>7} | MarketBeforePDP8: {is_relocated} | {u}")
                if not is_relocated:
                    all_ready = False
        except Exception as e:
            print(f"  ERR | {e} | {u}")
            all_ready = False
    if all_ready:
        print("\n[SUCCESS] All live endpoints verified with Market Wire superior to PDP8 Tracker!")
        break
    time.sleep(5)
