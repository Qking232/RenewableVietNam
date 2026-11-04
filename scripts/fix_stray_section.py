with open('RenewableVietNam/invm/index_Rev.036.html', 'r', encoding='utf-8') as f:
    text = f.read()

target = '            </div>\n          </div>\n        </div>\n      </div>\n    </div>\n\n    <!-- Action Bar:'
replacement = '            </div>\n          </div>\n        </div>\n      </div>\n\n    <!-- Action Bar:'

if target in text:
    text = text.replace(target, replacement)
    with open('RenewableVietNam/invm/index_Rev.036.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Cleaned successfully!")
