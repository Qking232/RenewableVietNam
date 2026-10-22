with open(r'G:\My Drive\7. AI\Gemini\RenewableVietNam\index.html', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if any(x in line for x in ['<main', '</main>', 'id="marketWire"', 'id="hubs"', 'id="calculator"', 'id="corporateSizerContainer"', 'id="evnEstimatorContainer"', 'id="greenIndicatorContainer"']):
            print(f"Line {i+1}: {line.strip()[:80]}")
