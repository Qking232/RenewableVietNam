import os
import re

base_dir = r"G:\My Drive\7. AI\RenewableVietNam"
index_file = os.path.join(base_dir, "index.html")
rev14_file = os.path.join(base_dir, "index_Rev.014.html")

with open(index_file, "r", encoding="utf-8") as f:
    html = f.read()

# Replace desktop navigation
html = html.replace('>PDP8 Energy<', '>Energy<')
html = html.replace('>Green Industrial<', '>Industrial<')
html = html.replace('>Investment M&A<', '>Legal<')
html = html.replace('>Investment M&amp;A<', '>Legal<')

# Replace aria labels & card titles where appropriate
html = html.replace('aria-label="Open PDP8 Energy Atlas"', 'aria-label="Open Energy Atlas"')
html = html.replace('aria-label="Open Investment M&A Engine"', 'aria-label="Open Legal M&A Engine"')
html = html.replace('Green Industrial Siting &amp; DPPA Portal', 'Industrial Siting &amp; DPPA Portal')
html = html.replace('Launch M&amp;A Engine &rarr;', 'Launch Legal Engine &rarr;')

# Footer navigation updates
html = html.replace('>Generation<', '>Energy<')
html = html.replace('>Investment<', '>Legal<')

# Write non-destructive sequential revision
with open(rev14_file, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Created sequential revision: {rev14_file}")

with open(index_file, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Updated active homepage: {index_file}")
