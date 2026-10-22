#!/usr/bin/env python3
"""
====================================================================
Move "My Location" to Bottom-Right Floating Map Icon (Zero Text)
====================================================================
1. Removes #btnMyLocation text chip from #gmChipsRow.
2. Ensures #mapBtnMyLocation is a dedicated, elevated circular FAB
   floating at bottom-right (right: 16px; bottom: 30px;) with pure
   reticle icon and NO text.
3. Synchronizes across RenewableVietNam and Qking232.github.io.
====================================================================
"""

import os
import shutil

TARGET_FILES = [
    r"G:\My Drive\7. AI\Gemini\RenewableVietNam\evcharging\index.html",
    r"G:\My Drive\7. AI\Gemini\Qking232.github.io\evcharging\index.html"
]

def update_file(filepath):
    if not os.path.exists(filepath):
        print(f"[WARN] File not found: {filepath}")
        return False

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    crlf = "\r\n" in content
    le = "\r\n" if crlf else "\n"

    def norm(s):
        return s.replace("\r\n", "\n").replace("\n", le)

    # 1. Update Chips Row: Remove #btnMyLocation
    old_chips = """      <!-- 2. Horizontal Quick Filter Chips Row (Lập lộ trình, Gần tôi, My Location, Select Location) -->
      <div class="gm-chips-row" id="gmChipsRow">
        <button class="gm-chip" id="chipItinToggle" type="button" title="Lập lộ trình &amp; Gợi ý sạc EV">
          <span class="chip-text" style="font-weight:650">Lập lộ trình</span>
        </button>

        <button class="gm-chip" id="pillNear" type="button" title="Tìm các trạm sạc gần bạn (chọn hãng)">
          <span class="chip-text" id="pillNearTxt" style="font-weight:650">Gần tôi</span>
        </button>

        <button class="gm-chip" id="btnMyLocation" type="button" title="Lấy vị trí GPS hiện tại của tôi (My Location)">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" class="chip-icon">
            <path d="M12 2v3m0 14v3M2 12h3m14 0h3" />
            <circle cx="12" cy="12" r="7" />
            <circle cx="12" cy="12" r="2" fill="currentColor" />
          </svg>
          <span class="chip-text" style="font-weight:650">My Location</span>
        </button>

        <button class="gm-chip" id="btnSelectLocation" type="button" title="Nhấp chọn vị trí bất kỳ trên bản đồ (Select Location)">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" class="chip-icon">
            <path d="M12 21s-6-5.33-6-10a6 6 0 0 1 12 0c0 4.67-6 10-6 10z" />
            <circle cx="12" cy="11" r="2.5" />
          </svg>
          <span class="chip-text" style="font-weight:650">Select Location</span>
        </button>
      </div>"""

    new_chips = """      <!-- 2. Horizontal Quick Filter Chips Row (Lập lộ trình, Gần tôi, Select Location) -->
      <div class="gm-chips-row" id="gmChipsRow">
        <button class="gm-chip" id="chipItinToggle" type="button" title="Lập lộ trình &amp; Gợi ý sạc EV">
          <span class="chip-text" style="font-weight:650">Lập lộ trình</span>
        </button>

        <button class="gm-chip" id="pillNear" type="button" title="Tìm các trạm sạc gần bạn (chọn hãng)">
          <span class="chip-text" id="pillNearTxt" style="font-weight:650">Gần tôi</span>
        </button>

        <button class="gm-chip" id="btnSelectLocation" type="button" title="Nhấp chọn vị trí bất kỳ trên bản đồ (Select Location)">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" class="chip-icon">
            <path d="M12 21s-6-5.33-6-10a6 6 0 0 1 12 0c0 4.67-6 10-6 10z" />
            <circle cx="12" cy="11" r="2.5" />
          </svg>
          <span class="chip-text" style="font-weight:650">Select Location</span>
        </button>
      </div>"""

    if norm(old_chips) in content:
        content = content.replace(norm(old_chips), norm(new_chips))
        print(f"  [OK] Removed #btnMyLocation text chip from #gmChipsRow in {os.path.basename(filepath)}")

    # 2. Refactor CSS for .map-loc-btn to 44px elevated Google Maps style
    old_css = """  .map-floating-location-controls {
    position: absolute;
    right: 14px;
    bottom: 30px;
    display: flex;
    flex-direction: column;
    gap: 8px;
    z-index: 1000;
  }
  .map-loc-btn {
    width: 42px;
    height: 42px;
    border-radius: 50%;
    background: var(--panel);
    border: 1px solid var(--line);
    color: var(--txt);
    box-shadow: 0 4px 14px rgba(0,0,0,0.18);
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: all 0.18s ease;
  }"""

    new_css = """  .map-floating-location-controls {
    position: absolute;
    right: 16px;
    bottom: 32px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    z-index: 1000;
  }
  .map-loc-btn {
    width: 44px;
    height: 44px;
    border-radius: 50%;
    background: var(--panel);
    border: 1px solid var(--line);
    color: var(--txt);
    box-shadow: 0 4px 16px rgba(0,0,0,0.22);
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: all 0.18s ease;
  }"""

    if norm(old_css) in content:
        content = content.replace(norm(old_css), norm(new_css))
        print(f"  [OK] Updated CSS for 44px elevated FAB in {os.path.basename(filepath)}")

    with open(filepath, "w", encoding="utf-8", newline="") as f:
        f.write(content)

    print(f"[SUCCESS] Updated {filepath}")
    return True

if __name__ == "__main__":
    for p in TARGET_FILES:
        print(f"\nProcessing {p}...")
        update_file(p)
