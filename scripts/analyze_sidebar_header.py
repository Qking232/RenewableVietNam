with open('G:/My Drive/7. AI/Gemini/RenewableVietNam/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f'Total lines: {len(lines)}')

# Find header nav links
print("\n--- Header / Nav Section ---")
for idx, line in enumerate(lines[:140]):
    if any(k in line.lower() for k in ['header', 'nav', 'href=', 'calculator', 'bản đồ']):
        print(f"{idx+1}: {line.strip()}")

# Find sidebar structure
print("\n--- Sidebar Section ---")
for idx, line in enumerate(lines):
    if any(k in line.lower() for k in ['sidebar-workspace', 'id="sidebar', 'class="sidebar']):
        print(f"{idx+1}: {line.strip()[:100]}")
