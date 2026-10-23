"""
Reposition Corporate Clean Power Siting & Allocation Sizer above the #hubs cockpit in index.html.
Excise the outbound link to /calculator/.
"""

import os
import re

INDEX_PATH = r"G:\My Drive\7. AI\Gemini\RenewableVietNam\index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Locate #powerSizer section
sizer_match = re.search(r'(<section id="powerSizer".*?</section>)', text, re.DOTALL)
assert sizer_match, "Could not find <section id=\"powerSizer\">!"

sizer_html = sizer_match.group(1)

# 2. Excise the outbound link [Open Full Tariff Suite (EVN & CBAM) →]
old_header_right = re.search(r'<div class="flex flex-col sm:items-end gap-1.5 shrink-0">.*?</div>\s*</div>', sizer_html, re.DOTALL)
assert old_header_right, "Could not find header right in power sizer!"

new_header_right = '''<div class="flex items-center gap-1.5 shrink-0">
            <div class="font-mono text-[11px] text-inkMuted dark:text-textDarkMuted bg-slate-100 dark:bg-darkCard px-2.5 py-1 rounded-lg border border-borderSlate dark:border-darkBorder">
              Grid Baseline: <span class="font-semibold text-inkPrimary dark:text-textDarkPrimary">0.7221 tCO<sub>2</sub>e/MWh</span>
            </div>
          </div>'''

# Replace inside sizer_html
sizer_cleaned = sizer_html.replace(old_header_right.group(0), new_header_right, 1)

# 3. Remove original #powerSizer from text
text_without_sizer = text.replace(sizer_html, "", 1)

# 4. Insert sizer_cleaned immediately before <section id="hubs"
hubs_match = re.search(r'(<section id="hubs")', text_without_sizer)
assert hubs_match, "Could not find <section id=\"hubs\">!"

final_text = text_without_sizer[:hubs_match.start()] + sizer_cleaned + '\n\n    ' + text_without_sizer[hubs_match.start():]

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(final_text)

print("[SUCCESS] Repositioned #powerSizer above #hubs and removed /calculator/ link in index.html!")
print(f"Total bytes written: {len(final_text.encode('utf-8'))}")
