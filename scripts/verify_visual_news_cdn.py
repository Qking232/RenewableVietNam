import urllib.request
import time

urls = [
    ("https://renewablevietnam.com/", True),
    ("https://renewablevietnam.com/data/industry_news.json", False),
    ("https://qking232.github.io/", True),
    ("https://qking232.github.io/data/industry_news.json", False)
]

for attempt in range(1, 15):
    all_ready = True
    print(f"\nAttempt {attempt}:")
    for u, is_html in urls:
        try:
            req = urllib.request.Request(f"{u}?ts={int(time.time())}", headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
            with urllib.request.urlopen(req, timeout=12) as resp:
                data = resp.read()
                if is_html:
                    has_hero = b'FEATURED LEAD DISPATCH' in data
                    has_img_logic = b'defaultSectorImages' in data
                    print(f"  {resp.status} | Len: {len(data):>7} | Hero: {has_hero} | ImgLogic: {has_img_logic} | {u}")
                    if not has_hero or not has_img_logic:
                        all_ready = False
                else:
                    has_img_url = b'"image_url":' in data
                    print(f"  {resp.status} | Len: {len(data):>7} | ImageUrl: {has_img_url} | {u}")
                    if not has_img_url:
                        all_ready = False
        except Exception as e:
            print(f"  ERR | {e} | {u}")
            all_ready = False

    if all_ready:
        print("\n[SUCCESS] Both production CDN domains serving elevated visual news feed with image previews!")
        break
    time.sleep(6)
