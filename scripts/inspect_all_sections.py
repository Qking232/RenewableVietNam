import re

for filename in ['index.html', 'green/index.html', 'projectenergy/index.html']:
    path = f'G:/My Drive/7. AI/Gemini/RenewableVietNam/{filename}'
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    sections = re.findall(r'<section[^>]*id=["\']([^"\']*)["\']', text)
    print(f'=== {filename} ===')
    for s in sections:
        print(f'  - #{s}')
