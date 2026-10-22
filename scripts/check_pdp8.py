with open('G:/My Drive/7. AI/Gemini/RenewableVietNam/index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

start = orig.find('<section id="pdp8"')
if start != -1:
    end = orig.find('</section>', start)
    print("Found section#pdp8! Length:", end - start)
    print(orig[start:start+600])
else:
    print("Not found")
