with open('G:/My Drive/7. AI/Gemini/RenewableVietNam/evcharging/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if any(k in line for k in ['<header', 'id="appHeader"', 'class="header', 'gm-header', 'gm-search-card']):
        print(f"{idx+1}: {line.strip()[:80]}")
