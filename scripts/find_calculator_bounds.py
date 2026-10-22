with open(r'G:\My Drive\7. AI\Gemini\RenewableVietNam\index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

calc_start = None
calc_end = None
for i, l in enumerate(lines):
    if '<section id="calculator"' in l:
        calc_start = i
    if calc_start is not None and '</section>' in l:
        calc_end = i
        # check if it closes the calculator section
        if i > 1150: # calculator closes around line 1206
            break

print(f"Calculator section: lines {calc_start+1} to {calc_end+1} ({calc_end - calc_start + 1} lines)")
