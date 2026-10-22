import os
import re
import json

REPOS = [
    r"G:\My Drive\7. AI\Gemini\RenewableVietNam",
    r"G:\My Drive\7. AI\Gemini\Qking232.github.io"
]

SRC_FILE = r"G:\My Drive\7. AI\Gemini\RenewableVietNam\projectenergy\index.html"

def main():
    with open(SRC_FILE, "r", encoding="utf-8") as f:
        text = f.read()

    m = re.search(r'let PROJECTS\s*=\s*(\[[\s\S]*?\]);', text)
    if not m:
        raise ValueError("Could not find let PROJECTS = [...] in projectenergy/index.html")

    data = json.loads(m.group(1))
    print(f"Extracted {len(data)} projects from {SRC_FILE}")

    for repo in REPOS:
        out_dir = os.path.join(repo, "data")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "vietnam_clean_energy_projects.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Saved: {out_path} ({os.path.getsize(out_path)} bytes)")

if __name__ == "__main__":
    main()
