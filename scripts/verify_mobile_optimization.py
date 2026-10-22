"""
Rigorous verification script for mobile layout optimization and sticky header CTAs.
"""
import os
import sys

def verify_file(filepath, checks):
    if not os.path.exists(filepath):
        print(f"[FAIL] Missing file: {filepath}")
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    all_ok = True
    rel_path = os.path.relpath(filepath, "G:/My Drive/7. AI/Gemini")
    for desc, pattern in checks:
        if pattern not in content:
            print(f"[FAIL] {rel_path}: Missing '{desc}'")
            all_ok = False
        else:
            print(f"[OK] {rel_path}: Found '{desc}'")
    return all_ok

def check_parity(path_a, path_b):
    if not os.path.exists(path_a) or not os.path.exists(path_b):
        print(f"[FAIL] Cannot compare {path_a} and {path_b}: file not found.")
        return False
    with open(path_a, 'r', encoding='utf-8') as fa, open(path_b, 'r', encoding='utf-8') as fb:
        ca = fa.read()
        cb = fb.read()
    if ca == cb:
        rel_a = os.path.relpath(path_a, "G:/My Drive/7. AI/Gemini")
        print(f"[OK] 100% PARITY for {rel_a} across repos")
        return True
    else:
        print(f"[FAIL] Parity mismatch between {path_a} and {path_b} (length {len(ca)} vs {len(cb)})")
        return False

def main():
    repo1 = "G:/My Drive/7. AI/Gemini/RenewableVietNam"
    repo2 = "G:/My Drive/7. AI/Gemini/Qking232.github.io"
    
    main_checks = [
        ("no-scrollbar CSS", ".no-scrollbar"),
        ("Sticky Header Blur & Stretch", "sticky top-0 z-40 w-full bg-alabaster/95 dark:bg-obsidian/95 backdrop-blur-md"),
        ("Sticky Header Margin Offset", "-mx-4 sm:-mx-6 lg:-mx-8 px-4 sm:px-6 lg:px-8"),
        ("Mobile Touch Navigation Carousel", 'flex md:hidden items-center gap-1.5 overflow-x-auto no-scrollbar'),
        ("Carousel Hubs Link", 'href="/" class="px-2.5 py-1.5 rounded-lg text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20 shrink-0">Industrial Hubs</a>'),
        ("Carousel Energy Map Link", 'href="/projectenergy/"'),
        ("Carousel EV Stations Link", 'href="/evcharging/"'),
        ("Carousel Power Sizer Link", 'href="/calculator/"'),
        ("Carousel The Library Link", 'href="/hub/"'),
        ("Header Live Wire CTA", 'href="#marketWire" class="inline-flex items-center gap-1.5 px-2.5 sm:px-3 py-1.5 rounded-lg font-mono text-[10px] sm:text-[11px]'),
        ("Header Theme Toggle", 'id="themeToggleBtn"')
    ]
    
    calc_checks = [
        ("no-scrollbar CSS", ".no-scrollbar"),
        ("Sticky Header Blur & Stretch", "sticky top-0 z-40 w-full bg-alabaster/95 dark:bg-obsidian/95 backdrop-blur-md"),
        ("Sticky Header Margin Offset", "-mx-4 sm:-mx-6 lg:-mx-8 px-4 sm:px-6 lg:px-8"),
        ("Mobile Touch Navigation Carousel", 'flex md:hidden items-center gap-1.5 overflow-x-auto no-scrollbar'),
        ("Carousel Hubs Link", 'href="/"'),
        ("Carousel Power Sizer Active Link", 'href="/calculator/" class="px-2.5 py-1.5 rounded-lg text-teal-600 dark:text-teal-400 font-semibold bg-teal-500/10 dark:bg-teal-400/10 border border-teal-500/20 shrink-0">Power Sizer</a>'),
        ("Header Return to Hubs CTA", 'href="/" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg font-mono text-[11px]'),
    ]

    ev_checks = [
        ("Header Hubs Action Link", 'href="/" class="header-btn" title="Khu công nghiệp / Industrial Hubs"'),
        ("Header Calculator Action Link", 'href="/calculator/" class="header-btn" title="Bộ tính toán / Calculators"')
    ]

    proj_checks = [
        ("Header Nav Industrial Hubs", '<a href="/" class="hover:text-white transition-colors">Industrial Hubs</a>'),
        ("Header Nav EV Charging", '<a href="/evcharging/" class="hover:text-white transition-colors">EV Stations</a>'),
        ("Header Nav Calculator", '<a href="/calculator/" class="hover:text-white transition-colors">Power Sizer</a>')
    ]

    success = True
    print("\n--- Verifying RenewableVietNam ---")
    success &= verify_file(os.path.join(repo1, "index.html"), main_checks)
    success &= verify_file(os.path.join(repo1, "calculator", "index.html"), calc_checks)
    success &= verify_file(os.path.join(repo1, "evcharging", "index.html"), ev_checks)
    success &= verify_file(os.path.join(repo1, "projectenergy", "index.html"), proj_checks)

    print("\n--- Verifying Qking232.github.io ---")
    success &= verify_file(os.path.join(repo2, "index.html"), main_checks)
    success &= verify_file(os.path.join(repo2, "calculator", "index.html"), calc_checks)
    success &= verify_file(os.path.join(repo2, "evcharging", "index.html"), ev_checks)
    success &= verify_file(os.path.join(repo2, "projectenergy", "index.html"), proj_checks)

    print("\n--- Verifying Cross-Repo Parity ---")
    success &= check_parity(os.path.join(repo1, "index.html"), os.path.join(repo2, "index.html"))
    success &= check_parity(os.path.join(repo1, "green", "index.html"), os.path.join(repo2, "green", "index.html"))
    success &= check_parity(os.path.join(repo1, "calculator", "index.html"), os.path.join(repo2, "calculator", "index.html"))
    success &= check_parity(os.path.join(repo1, "green", "calculator", "index.html"), os.path.join(repo2, "green", "calculator", "index.html"))
    success &= check_parity(os.path.join(repo1, "evcharging", "index.html"), os.path.join(repo2, "evcharging", "index.html"))
    success &= check_parity(os.path.join(repo1, "projectenergy", "index.html"), os.path.join(repo2, "projectenergy", "index.html"))

    if success:
        print("\n>>> ALL MOBILE LAYOUT & PARITY AUDITS PASSED 100% <<<")
        sys.exit(0)
    else:
        print("\n>>> VERIFICATION FAILED <<<")
        sys.exit(1)

if __name__ == "__main__":
    main()
