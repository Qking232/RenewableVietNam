"""
Safely inject news rerender hooks into setLanguage in projectenergy/index.html.
"""
for path in ['G:/My Drive/7. AI/Gemini/RenewableVietNam/projectenergy/index.html', 'G:/My Drive/7. AI/Gemini/Qking232.github.io/projectenergy/index.html']:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    old_target = "renderTablePage();\n      updateMapStatusBar();"
    new_target = "renderTablePage();\n      updateMapStatusBar();\n      if (typeof renderNewsGrid === 'function') renderNewsGrid();\n      if (typeof renderBreakingTicker === 'function') renderBreakingTicker();"
    
    if old_target in content:
        content = content.replace(old_target, new_target)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated LF: {path}")
    elif old_target.replace("\n", "\r\n") in content:
        content = content.replace(old_target.replace("\n", "\r\n"), new_target.replace("\n", "\r\n"))
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated CRLF: {path}")
    else:
        print(f"Target already modified or not found: {path}")
