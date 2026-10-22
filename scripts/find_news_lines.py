with open('G:/My Drive/7. AI/Gemini/RenewableVietNam/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if '<section id="marketWire"' in line or 'function renderNewsGrid()' in line:
        print(f"{idx+1}: {line.strip()[:80]}")
