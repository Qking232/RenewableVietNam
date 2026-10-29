import os
import re

BASE_DIR = r"G:\My Drive\7. AI\RenewableVietNam"

TARGETS = [
    {
        "file": os.path.join(BASE_DIR, "projectenergy", "index.html"),
        "subdomain": "wind.renewablevietnam.com",
        "subpath": "/projectenergy"
    },
    {
        "file": os.path.join(BASE_DIR, "green", "index.html"),
        "subdomain": "ind.renewablevietnam.com",
        "subpath": "/green"
    },
    {
        "file": os.path.join(BASE_DIR, "evcharging", "index.html"),
        "subdomain": "ev.renewablevietnam.com",
        "subpath": "/evcharging"
    },
    {
        "file": os.path.join(BASE_DIR, "hub", "index.html"),
        "subdomain": "legal.renewablevietnam.com",
        "subpath": "/hub"
    }
]

for t in TARGETS:
    fpath = t["file"]
    subdomain = t["subdomain"]
    subpath = t["subpath"]
    
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    snippet = f"""<script>
    if (window.location.hostname === 'renewablevietnam.com') {{
      var targetPath = window.location.pathname.replace(/^\\{subpath}/, '') || '/';
      window.location.replace('https://{subdomain}' + targetPath + window.location.search + window.location.hash);
    }}
  </script>"""

    if "window.location.hostname === 'renewablevietnam.com'" in content:
        print(f"Skipping {fpath}: already contains canonical redirect.")
        continue

    # Insert right after <head> or <head ...>
    pattern = re.compile(r"(<head[^>]*>)", re.IGNORECASE)
    match = pattern.search(content)
    if match:
        pos = match.end()
        new_content = content[:pos] + "\n  " + snippet + content[pos:]
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Successfully updated {fpath} with canonical redirect to https://{subdomain}")
    else:
        print(f"ERROR: Could not find <head> tag in {fpath}")
