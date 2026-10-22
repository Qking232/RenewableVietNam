#!/usr/bin/env python3
"""
====================================================================
Implement "My Location" & "Select Location" Buttons in EV Charging
====================================================================
Embeds dual geolocation controls:
  1. "My Location" (GPS Auto-locate via locateMe())
  2. "Select Location" (Crosshair pin-drop via startPick())
Into:
  - Header Quick Filter Chips row (#gmChipsRow)
  - Floating Map Quick Action dock (#mapFloatingLocationControls)
Across:
  - RenewableVietNam/evcharging/index.html
  - Qking232.github.io/evcharging/index.html
====================================================================
"""

import os
import shutil

SOURCE_FILE = r"G:\My Drive\7. AI\Gemini\RenewableVietNam\evcharging\index.html"
DEST_DIR = r"G:\My Drive\7. AI\Gemini\Qking232.github.io\evcharging"
DEST_FILE = os.path.join(DEST_DIR, "index.html")

def update_evcharging():
    with open(SOURCE_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    crlf = "\r\n" in content
    le = "\r\n" if crlf else "\n"

    def norm(s):
        return s.replace("\r\n", "\n").replace("\n", le)

    # 1. Add CSS rules before </style>
    css_to_add = """
  /* Floating & Chip Geolocation Controls (rev 0.0.30) */
  .gm-chip svg.chip-icon {
    margin-right: 5px;
    vertical-align: -2.5px;
    flex-shrink: 0;
  }
  .gm-chip.active-loc {
    background: var(--accent) !important;
    color: #ffffff !important;
    border-color: var(--accent) !important;
  }
  .gm-chip.active-loc svg {
    stroke: #ffffff;
  }
  .map-floating-location-controls {
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
  }
  .map-loc-btn:hover {
    border-color: var(--accent);
    color: var(--accent);
    transform: scale(1.06);
  }
  .map-loc-btn.active-loc {
    background: var(--accent);
    color: #ffffff;
    border-color: var(--accent);
  }
  .map-loc-btn.picking {
    animation: locPulse 1.2s infinite ease-in-out;
    border-color: var(--accent);
  }
  @keyframes locPulse {
    0%, 100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(47,158,111,0.5); }
    50% { transform: scale(1.08); box-shadow: 0 0 0 8px rgba(47,158,111,0); }
  }
"""
    if "/* Floating & Chip Geolocation Controls" not in content:
        content = content.replace("</style>", css_to_add + "\n</style>", 1)
        print("  [OK] Added CSS styles for location controls")

    # 2. Add buttons in #gmChipsRow
    old_chips_row = """      <!-- 2. Horizontal Quick Filter Chips Row (Only 'Lập lộ trình' and 'Gần tôi') -->
      <div class="gm-chips-row" id="gmChipsRow">
        <button class="gm-chip" id="chipItinToggle" type="button" title="Lập lộ trình &amp; Gợi ý sạc EV">
          <span class="chip-text" style="font-weight:650">Lập lộ trình</span>
        </button>

        <button class="gm-chip" id="pillNear" type="button" title="Tìm các trạm sạc gần bạn (chọn hãng)">
          <span class="chip-text" id="pillNearTxt" style="font-weight:650">Gần tôi</span>
        </button>
      </div>"""

    new_chips_row = """      <!-- 2. Horizontal Quick Filter Chips Row (Lập lộ trình, Gần tôi, My Location, Select Location) -->
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

    if "id=\"btnMyLocation\"" not in content:
        content = content.replace(norm(old_chips_row), norm(new_chips_row))
        print("  [OK] Added My Location and Select Location buttons to #gmChipsRow")

    # 3. Add floating map action buttons in #mapWrap
    old_map_wrap = """    <div id="mapWrap">
      <div id="map"></div>
      <div id="toast"></div>
      <div id="loadbar"><i></i></div>"""

    new_map_wrap = """    <div id="mapWrap">
      <div id="map"></div>
      <div id="toast"></div>
      <div id="loadbar"><i></i></div>

      <!-- Floating Map Quick Action Dock (My Location & Select Location) -->
      <div class="map-floating-location-controls" id="mapFloatingLocationControls">
        <button class="map-loc-btn" id="mapBtnMyLocation" type="button" title="Vị trí của tôi (My Location)" aria-label="My Location">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
            <path d="M12 2v3m0 14v3M2 12h3m14 0h3" />
            <circle cx="12" cy="12" r="7" />
            <circle cx="12" cy="12" r="2.5" fill="currentColor" />
          </svg>
        </button>
        <button class="map-loc-btn" id="mapBtnSelectLocation" type="button" title="Chọn vị trí trên bản đồ (Select Location)" aria-label="Select Location">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
            <path d="M12 21s-6-5.33-6-10a6 6 0 0 1 12 0c0 4.67-6 10-6 10z" />
            <circle cx="12" cy="11" r="2.5" />
          </svg>
        </button>
      </div>"""

    if "id=\"mapBtnMyLocation\"" not in content:
        content = content.replace(norm(old_map_wrap), norm(new_map_wrap))
        print("  [OK] Added floating location controls to #mapWrap")

    # 4. Attach JavaScript event listeners
    old_listeners = """    // Click handler for 'Gần tôi' chip
    if(pillNear) pillNear.addEventListener("click", toggleNearPopover);"""

    new_listeners = """    // Click handler for 'Gần tôi' chip
    if(pillNear) pillNear.addEventListener("click", toggleNearPopover);

    // Event Handlers for 'My Location' and 'Select Location' Buttons
    const btnMyLocation = document.getElementById("btnMyLocation");
    const btnSelectLocation = document.getElementById("btnSelectLocation");
    const mapBtnMyLocation = document.getElementById("mapBtnMyLocation");
    const mapBtnSelectLocation = document.getElementById("mapBtnSelectLocation");

    function triggerMyLocation(e) {
      if (e) e.stopPropagation();
      if (typeof closeNearPopover === "function") closeNearPopover();
      if (btnSelectLocation) btnSelectLocation.classList.remove("active-loc", "picking");
      if (mapBtnSelectLocation) mapBtnSelectLocation.classList.remove("active-loc", "picking");

      if (btnMyLocation) btnMyLocation.classList.add("active-loc");
      if (mapBtnMyLocation) mapBtnMyLocation.classList.add("active-loc");

      locateMe();
    }

    function triggerSelectLocation(e) {
      if (e) e.stopPropagation();
      if (typeof closeNearPopover === "function") closeNearPopover();

      if (btnSelectLocation) btnSelectLocation.classList.toggle("picking");
      if (mapBtnSelectLocation) mapBtnSelectLocation.classList.toggle("picking");

      startPick("Nhấp vào bất kỳ điểm nào trên bản đồ để chọn vị trí / Click map to set reference location");
    }

    if (btnMyLocation) btnMyLocation.addEventListener("click", triggerMyLocation);
    if (mapBtnMyLocation) mapBtnMyLocation.addEventListener("click", triggerMyLocation);

    if (btnSelectLocation) btnSelectLocation.addEventListener("click", triggerSelectLocation);
    if (mapBtnSelectLocation) mapBtnSelectLocation.addEventListener("click", triggerSelectLocation);"""

    if "triggerMyLocation" not in content:
        content = content.replace(norm(old_listeners), norm(new_listeners))
        print("  [OK] Attached event listeners for My Location and Select Location")

    # Also update map click listener so picking state resets visual classes
    old_map_click = """map.on("click", e=>{ if(!picking) return; picking=false; map.getContainer().style.cursor=""; setMyLoc(e.latlng.lat, e.latlng.lng, 0); });"""
    new_map_click = """map.on("click", e=>{
      if(!picking) return;
      picking=false;
      map.getContainer().style.cursor="";
      const bSel = document.getElementById("btnSelectLocation");
      const mSel = document.getElementById("mapBtnSelectLocation");
      if(bSel) { bSel.classList.remove("picking"); bSel.classList.add("active-loc"); }
      if(mSel) { mSel.classList.remove("picking"); mSel.classList.add("active-loc"); }
      const bMy = document.getElementById("btnMyLocation");
      const mMy = document.getElementById("mapBtnMyLocation");
      if(bMy) bMy.classList.remove("active-loc");
      if(mMy) mMy.classList.remove("active-loc");
      setMyLoc(e.latlng.lat, e.latlng.lng, 0);
    });"""

    if "bSel.classList.remove" not in content:
        content = content.replace(norm(old_map_click), norm(new_map_click))
        print("  [OK] Updated map click handler for visual feedback reset")

    with open(SOURCE_FILE, "w", encoding="utf-8", newline="") as f:
        f.write(content)
    print(f"[SUCCESS] Updated {SOURCE_FILE}")

    # 5. Mirror to Qking232.github.io/evcharging/index.html
    os.makedirs(DEST_DIR, exist_ok=True)
    shutil.copy2(SOURCE_FILE, DEST_FILE)
    print(f"[SUCCESS] Mirrored to {DEST_FILE}")

if __name__ == "__main__":
    update_evcharging()
