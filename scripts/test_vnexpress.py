import urllib.request
import xml.etree.ElementTree as ET
import re

req = urllib.request.Request('https://e.vnexpress.net/rss/business.rss', headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=8) as resp:
        root = ET.fromstring(resp.read())
        for item in root.findall('.//item')[:3]:
            title = item.find('title').text
            desc = item.find('description').text or ''
            img = re.search(r'<img[^>]+src=["\']([^"\']+)["\']', desc)
            print("Title:", title[:40])
            print("  Img:", img.group(1) if img else None)
except Exception as e:
    print("Error:", e)
