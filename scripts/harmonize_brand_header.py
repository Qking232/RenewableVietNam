import os

base_dir = r"G:\My Drive\7. AI\RenewableVietNam"
index_path = os.path.join(base_dir, "index.html")
rev7_path = os.path.join(base_dir, "index_Rev.007.html")
script_path = os.path.join(base_dir, "scripts", "generate_master_dashboard.py")

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("RENEWABLE VIETNAM &middot; MASTER COCKPIT", "RENEWABLE INFRASTRUCTURE")
content = content.replace('aria-label="Renewable Vietnam — Master Cockpit"', 'aria-label="Renewable Vietnam — home"')

with open(index_path, "w", encoding="utf-8") as f:
    f.write(content)

with open(rev7_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Updated {index_path} and created {rev7_path}")

# Also update generate_master_dashboard.py so baseline scripts remain aligned
if os.path.exists(script_path):
    with open(script_path, "r", encoding="utf-8") as f:
        s_content = f.read()
    s_content = s_content.replace("RENEWABLE VIETNAM &middot; MASTER COCKPIT", "RENEWABLE INFRASTRUCTURE")
    s_content = s_content.replace('aria-label="Renewable Vietnam — Master Cockpit"', 'aria-label="Renewable Vietnam — home"')
    with open(script_path, "w", encoding="utf-8") as f:
        f.write(s_content)
    print(f"Updated {script_path}")
