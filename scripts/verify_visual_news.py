import os
import json

REPOS = [
    "G:/My Drive/7. AI/Gemini/RenewableVietNam",
    "G:/My Drive/7. AI/Gemini/Qking232.github.io"
]

all_passed = True

for repo in REPOS:
    print(f"=== Testing {repo} ===")
    
    # 1. Test index.html
    index_path = os.path.join(repo, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    has_hero = "FEATURED LEAD DISPATCH" in html
    has_card_render = "function renderArticleCard(art)" in html
    has_images = "defaultSectorImages" in html
    has_finance = 'data-news-sector="Finance & ESG"' in html
    has_fdi = 'data-news-sector="FDI & Infrastructure"' in html
    has_img_tag = '<img src="${cardImg}"' in html or '<img src="${leadImg}"' in html

    print(f"  index.html ({len(html)} bytes):")
    print(f"    has_hero: {has_hero}")
    print(f"    has_card_render: {has_card_render}")
    print(f"    has_images: {has_images}")
    print(f"    has_finance: {has_finance}")
    print(f"    has_fdi: {has_fdi}")
    print(f"    has_img_tag: {has_img_tag}")

    if not all([has_hero, has_card_render, has_images, has_finance, has_fdi, has_img_tag]):
        print("  [FAIL] index.html missing visual news components!")
        all_passed = False

    # 2. Test green/index.html parity
    green_index_path = os.path.join(repo, "green", "index.html")
    with open(green_index_path, "r", encoding="utf-8") as f:
        green_html = f.read()
    if html != green_html:
        print("  [FAIL] green/index.html does not match root index.html!")
        all_passed = False
    else:
        print("  green/index.html == root index.html: True")

    # 3. Test industry_news.json
    news_path = os.path.join(repo, "data", "industry_news.json")
    with open(news_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    articles = data.get("articles", [])
    has_200 = len(articles) == 200
    all_have_images = all(art.get("image_url", "").startswith("http") for art in articles)
    print(f"  industry_news.json: total={len(articles)} (expected 200: {has_200}), all_have_images: {all_have_images}")
    if not has_200 or not all_have_images:
        print("  [FAIL] industry_news.json validation failed!")
        all_passed = False

# Cross-repo parity check
with open("G:/My Drive/7. AI/Gemini/RenewableVietNam/index.html", "r", encoding="utf-8") as f1, \
     open("G:/My Drive/7. AI/Gemini/Qking232.github.io/index.html", "r", encoding="utf-8") as f2:
    idx_match = (f1.read() == f2.read())

with open("G:/My Drive/7. AI/Gemini/RenewableVietNam/data/industry_news.json", "r", encoding="utf-8") as f1, \
     open("G:/My Drive/7. AI/Gemini/Qking232.github.io/data/industry_news.json", "r", encoding="utf-8") as f2:
    news_match = (f1.read() == f2.read())

print(f"\nCross-repo parity:")
print(f"  index.html match: {idx_match}")
print(f"  industry_news.json match: {news_match}")

if all_passed and idx_match and news_match:
    print("\n[SUCCESS] 100% Verification passed across both repositories and all mirrors!")
else:
    print("\n[ERROR] Verification failed!")
