import os
import re

# We will read RenewableVietNam/index.html
ROOT_INDEX = "G:/My Drive/7. AI/Gemini/RenewableVietNam/index.html"
with open(ROOT_INDEX, "r", encoding="utf-8") as f:
    orig_html = f.read()

# 1. Extract the calculator section markup
aside_match = re.search(r'(<!-- =+ -->\s*<!-- DEDICATED LEFT SIDEBAR: CALCULATION & SIZING TOOLKIT.*?<!-- =+ -->\s*<!-- RIGHT PRIMARY WORKSPACE)', orig_html, re.DOTALL)
if not aside_match:
    print("Could not find aside block!")
    exit(1)

aside_content = aside_match.group(1)
print(f"Extracted aside block length: {len(aside_content)} chars")

# Extract the inner <section id="calculator" ... </section>
sec_match = re.search(r'(<section id="calculator".*?</section>)', aside_content, re.DOTALL)
if not sec_match:
    print("Could not find section#calculator!")
    exit(1)

calc_section = sec_match.group(1)
print(f"Extracted calc_section length: {len(calc_section)} chars")

# Extract the FALLBACK_HUBS and calculator javascript
start_hubs = orig_html.find("const FALLBACK_HUBS = [")
end_hubs = orig_html.find("let HUBS = [...FALLBACK_HUBS];") + len("let HUBS = [...FALLBACK_HUBS];")
hubs_js = orig_html[start_hubs:end_hubs]
print(f"Extracted hubs_js length: {len(hubs_js)} chars")

start_calc_js = orig_html.find("function updateCalculator() {")
end_calc_js = orig_html.find("// ====================================================================\n    // NATIONWIDE INDUSTRIAL PARKS REGISTRY")
calc_js = orig_html[start_calc_js:end_calc_js]
print(f"Extracted calc_js length: {len(calc_js)} chars")

start_sliders_js = orig_html.find('document.getElementById("calcDemandSlider")')
end_sliders_js = orig_html.find('// EVN Region Selection Listeners')
sliders_js = orig_html[start_sliders_js:end_sliders_js]
print(f"Extracted sliders_js length: {len(sliders_js)} chars")

print("All segments extracted successfully!")
