with open(r'G:\My Drive\7. AI\Gemini\RenewableVietNam\evcharging\index.html', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if any(w in line.lower() for w in ['geolocation', 'navigator.geolocation', 'locate', 'location', 'gần tôi', 'near']):
            if i > 2750: # HTML or JS part
                print(f"Line {i+1}: {line.strip()[:80]}")
