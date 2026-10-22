with open(r'G:\My Drive\7. AI\Gemini\RenewableVietNam\evcharging\index.html', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if 'map-floating-location-controls' in line or 'mapBtnMyLocation' in line:
            print(f"Line {i+1}: {line.strip()[:80]}")
