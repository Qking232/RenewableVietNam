import os
import sys

def main():
    base_dir = r"G:\My Drive\7. AI\RenewableVietNam"
    index_path = os.path.join(base_dir, "index.html")
    rev9_path = os.path.join(base_dir, "index_Rev.009.html")

    if not os.path.exists(index_path):
        print(f"Error: {index_path} not found")
        sys.exit(1)

    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update anti-FOUC script in <head> to use versioned key 'rvn_theme_v2'
    old_fouc = "var savedTheme = localStorage.getItem('theme');"
    new_fouc = "var savedTheme = localStorage.getItem('rvn_theme_v2');"
    if old_fouc in content:
        content = content.replace(old_fouc, new_fouc, 1)

    # 2. Update bottom script storage operations to use 'rvn_theme_v2'
    old_dark_store = "localStorage.setItem('theme', 'dark');"
    new_dark_store = "localStorage.setItem('rvn_theme_v2', 'dark');"
    content = content.replace(old_dark_store, new_dark_store, 1)

    old_light_store = "localStorage.setItem('theme', 'light');"
    new_light_store = "localStorage.setItem('rvn_theme_v2', 'light');"
    content = content.replace(old_light_store, new_light_store, 1)

    old_read_theme = "const savedTheme = localStorage.getItem('theme');"
    new_read_theme = "const savedTheme = localStorage.getItem('rvn_theme_v2');"
    content = content.replace(old_read_theme, new_read_theme, 1)

    # Write sequential revision index_Rev.009.html
    with open(rev9_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created sequential revision: {rev9_path}")

    # Synchronize active homepage index.html
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated active homepage: {index_path}")

if __name__ == "__main__":
    main()
