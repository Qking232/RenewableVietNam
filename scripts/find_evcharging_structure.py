with open(r'G:\My Drive\7. AI\Gemini\RenewableVietNam\evcharging\index.html', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if any(k in line for k in ['<header', '</header>', 'id="map"', 'class="filters"', 'id="app"']):
            print(f"Line {i+1}: {line.strip()[:80]}")
