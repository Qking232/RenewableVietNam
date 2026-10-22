import os
import re
import subprocess

REPOS = [
    r"G:\My Drive\7. AI\Gemini\RenewableVietNam",
    r"G:\My Drive\7. AI\Gemini\Qking232.github.io"
]

FILES = ["index.html", "green/index.html"]

def fix_file(file_path):
    print(f"Inspecting {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Remove dangling btn.classList and closing braces
    # Target pattern:
    # renderMapMarkers(HUBS.slice(0, 50));
    # \s*btn\.classList\.add\("bg-teal-600", "text-white"\);
    # \s*btn\.classList\.remove\("bg-white", "dark:bg-darkCard", "text-inkPrimary", "dark:text-textDarkMuted"\);
    # \s*\}\);
    # \s*\}\);
    dangling_pattern = re.compile(
        r'renderMapMarkers\(HUBS\.slice\(0,\s*50\)\);\s*'
        r'btn\.classList\.add\("bg-teal-600",\s*"text-white"\);\s*'
        r'btn\.classList\.remove\("bg-white",\s*"dark:bg-darkCard",\s*"text-inkPrimary",\s*"dark:text-textDarkMuted"\);\s*'
        r'\}\);\s*'
        r'\}\);',
        re.MULTILINE
    )

    if dangling_pattern.search(content):
        content = dangling_pattern.sub('renderMapMarkers(HUBS.slice(0, 50));', content)
        print("  [FIXED] Removed dangling JS button toggle tokens.")
    else:
        # Fallback check for any btn.classList.add("bg-teal-600", "text-white");
        print("  [WARN] Regex pattern did not match exact block, checking manual replacement...")
        bad_chunk = '''                btn.classList.add("bg-teal-600", "text-white");
          btn.classList.remove("bg-white", "dark:bg-darkCard", "text-inkPrimary", "dark:text-textDarkMuted");
        });
      });'''
        if bad_chunk in content:
            content = content.replace(bad_chunk, '')
            print("  [FIXED] Removed exact bad chunk.")

    # 2. Fix the DOM in ecoParkMapContainer: ensure resetMapZoomBtn and proper closing </div>
    # Look for ecoParkMapContainer header row
    dom_target = '''          <div class="flex items-center gap-2 font-mono text-[10px]">
            <!-- Basemap Indicator (Locked to High-Resolution Satellite) -->
            <div class="flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-darkCard border border-borderSlate dark:border-darkBorder text-teal-600 dark:text-teal-400 font-semibold shadow-sm">
              <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span>
              <span>Satellite (Esri World Imagery)</span>
            </div>
          </div>

        <!-- Leaflet Map Canvas -->'''

    dom_replacement = '''          <div class="flex items-center gap-2 font-mono text-[10px]">
            <!-- Basemap Indicator (Locked to High-Resolution Satellite) -->
            <div class="flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-darkCard border border-borderSlate dark:border-darkBorder text-teal-600 dark:text-teal-400 font-semibold shadow-sm">
              <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span>
              <span>Satellite (Esri World Imagery)</span>
            </div>

            <button id="resetMapZoomBtn" class="px-2 py-1 rounded bg-slate-100 dark:bg-darkCard border border-borderSlate dark:border-darkBorder text-inkMuted dark:text-textDarkMuted hover:text-teal-600 dark:hover:text-teal-400 transition-colors cursor-pointer" title="Reset Zoom">
              Full Extent
            </button>
          </div>
        </div>

        <!-- Leaflet Map Canvas -->'''

    if dom_target in content:
        content = content.replace(dom_target, dom_replacement)
        print("  [FIXED] Restored resetMapZoomBtn and closed header flex container </div>.")
    else:
        print("  [NOTE] DOM target pattern not matched or already updated.")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  [SAVED] {file_path}")

def main():
    for repo in REPOS:
        for f in FILES:
            path = os.path.join(repo, f)
            if os.path.exists(path):
                fix_file(path)
            else:
                print(f"File not found: {path}")

if __name__ == "__main__":
    main()
