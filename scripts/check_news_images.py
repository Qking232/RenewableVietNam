import json

with open("G:/My Drive/7. AI/Gemini/RenewableVietNam/data/industry_news.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for idx, art in enumerate(data['articles'][:8]):
    print(f"{idx+1}. [{art['sector']}] {art['title'][:55]}...")
    print(f"   Source: {art['source']} | Time: {art['relative_time']}")
    print(f"   Image: {art.get('image_url')}")
