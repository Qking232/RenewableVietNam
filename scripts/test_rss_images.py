import urllib.request
import xml.etree.ElementTree as ET
import re

url = "https://vietnamnews.vn/rss/environment.rss"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        root = ET.fromstring(resp.read())
        for item in root.findall('.//item')[:5]:
            title = item.find('title').text
            desc = item.find('description').text or ''
            enc = item.find('enclosure')
            enc_url = enc.get('url') if enc is not None else None
            img_match = re.search(r'<img[^>]+src=["\']([^"\']+)["\']', desc)
            img_src = img_match.group(1) if img_match else None
            print(f"Title: {title[:50]}...")
            print(f"  enclosure: {enc_url}")
            print(f"  img_src: {img_src}")
except Exception as e:
    print("Error:", e)
