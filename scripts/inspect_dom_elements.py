import re

with open(r'G:\My Drive\7. AI\Gemini\RenewableVietNam\index.html', encoding='utf-8') as f:
    text = f.read()

pdp8_ids = set(re.findall(r'id=["\'](pdp8[^"\']+)["\']', text))
print("PDP8 IDs:", sorted(list(pdp8_ids)))

table_ids = set(re.findall(r'id=["\']([^"\']*table[^"\']*)["\']', text, re.I))
print("Table IDs:", sorted(list(table_ids)))

grid_ids = set(re.findall(r'id=["\']([^"\']*grid[^"\']*)["\']', text, re.I))
print("Grid IDs:", sorted(list(grid_ids)))
