import os
import re

base_dir = r"G:\My Drive\7. AI\RenewableVietNam"

# 1. Update projectenergy/index.html
pe_path = os.path.join(base_dir, "projectenergy", "index.html")
with open(pe_path, "r", encoding="utf-8") as f:
    pe_content = f.read()

pe_content = pe_content.replace(
    "window.location.replace('https://wind.renewablevietnam.com'",
    "window.location.replace('https://energy.renewablevietnam.com'"
)
pe_content = pe_content.replace(
    "if (window.location.hostname === 'renewablevietnam.com')",
    "if (window.location.hostname === 'renewablevietnam.com' || window.location.hostname === 'wind.renewablevietnam.com')"
)
with open(pe_path, "w", encoding="utf-8") as f:
    f.write(pe_content)
print("Updated projectenergy/index.html")

# 2. Update standardize_subdomain_nav.py
nav_script = os.path.join(base_dir, "scripts", "standardize_subdomain_nav.py")
with open(nav_script, "r", encoding="utf-8") as f:
    nav_content = f.read()
nav_content = nav_content.replace("https://wind.renewablevietnam.com/", "https://energy.renewablevietnam.com/")
with open(nav_script, "w", encoding="utf-8") as f:
    f.write(nav_content)
print("Updated standardize_subdomain_nav.py")

# 3. Update generate_master_dashboard.py
dash_script = os.path.join(base_dir, "scripts", "generate_master_dashboard.py")
with open(dash_script, "r", encoding="utf-8") as f:
    dash_content = f.read()

dash_content = dash_content.replace("https://wind.renewablevietnam.com/", "https://energy.renewablevietnam.com/")
dash_content = dash_content.replace("wind.renewablevietnam.com", "energy.renewablevietnam.com")
with open(dash_script, "w", encoding="utf-8") as f:
    f.write(dash_content)
print("Updated generate_master_dashboard.py")
