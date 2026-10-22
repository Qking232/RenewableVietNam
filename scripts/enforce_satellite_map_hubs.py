"""
Enforce exclusive high-resolution Satellite (ArcGIS Esri World Imagery) cartography
and eliminate OpenStreetMap (OSM France/OSM VN) across Industrial Hubs pages:
- RenewableVietNam/index.html & green/index.html
- Qking232.github.io/index.html & green/index.html
"""
import os
import re

REPO1 = "G:/My Drive/7. AI/Gemini/RenewableVietNam"
REPO2 = "G:/My Drive/7. AI/Gemini/Qking232.github.io"

TARGETS = [
    os.path.join(REPO1, "index.html"),
    os.path.join(REPO1, "green", "index.html"),
    os.path.join(REPO2, "index.html"),
    os.path.join(REPO2, "green", "index.html")
]

def update_file(path):
    if not os.path.exists(path):
        print(f"Skipping non-existent: {path}")
        return
    
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Remove tile.openstreetmap.fr prefetch and update comment
    content = content.replace(
        '  <link rel="dns-prefetch" href="https://tile.openstreetmap.fr">\n',
        ''
    )
    content = content.replace(
        '<!-- Leaflet Map CSS & JS with OpenStreetMap France Support -->',
        '<!-- Leaflet Map CSS & JS with Satellite Imagery Support -->'
    )

    # 2. Update map container comment and basemap toolbar in HTML
    content = content.replace(
        '<!-- INTERACTIVE GEOSPATIAL MAP COCKPIT (OPENSTREETMAP FRANCE) -->',
        '<!-- INTERACTIVE GEOSPATIAL MAP COCKPIT (HIGH-RESOLUTION SATELLITE) -->'
    )

    old_toolbar_pattern = r'<!-- Basemap Switcher -->.*?</div>\s*</div>'
    new_toolbar = '''<!-- Basemap Indicator (Locked to High-Resolution Satellite) -->
            <div class="flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-darkCard border border-borderSlate dark:border-darkBorder text-teal-600 dark:text-teal-400 font-semibold shadow-sm">
              <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span>
              <span>Satellite (Esri World Imagery)</span>
            </div>
          </div>'''

    content = re.sub(old_toolbar_pattern, new_toolbar, content, flags=re.DOTALL)

    # 3. Update MAP_BASEMAPS and initEcoParkMap in JavaScript
    old_engine_pattern = r'// =+?\n\s*// OPENSTREETMAP \(FRANCE\) LEAFLET MAP ENGINE.*?function initEcoParkMap\(\) \{.*?hubMarkersLayer = L\.layerGroup\(\)\.addTo\(hubMap\);\s*renderMapMarkers\(HUBS\.slice\(0, 50\)\);'
    
    new_engine = '''// =========================================================================
    // HIGH-RESOLUTION SATELLITE (ESRI WORLD IMAGERY) LEAFLET MAP ENGINE
    // =========================================================================
    let hubMap = null;
    let hubMarkersLayer = null;
    let baseTileLayer = null;

    const MAP_BASEMAPS = {
      satellite: {
        url: 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attribution: 'Tiles &copy; Esri &mdash; Source: Esri, Maxar, Earthstar Geographics',
        maxZoom: 19
      }
    };

    function initEcoParkMap() {
      const mapEl = document.getElementById("ecoParkMap");
      if (!mapEl || hubMap || typeof L === "undefined") return;

      const defaultProvider = 'satellite';

      hubMap = L.map('ecoParkMap', {
        center: [15.8, 107.5],
        zoom: 6,
        minZoom: 5,
        maxZoom: 19,
        scrollWheelZoom: false,
        preferCanvas: true
      });

      // Enable scroll-wheel zoom upon user click
      hubMap.on('click', () => {
        hubMap.scrollWheelZoom.enable();
      });

      baseTileLayer = L.tileLayer(MAP_BASEMAPS[defaultProvider].url, {
        subdomains: 'abcd',
        attribution: MAP_BASEMAPS[defaultProvider].attribution,
        maxZoom: MAP_BASEMAPS[defaultProvider].maxZoom
      }).addTo(hubMap);

      // Hoàng Sa & Trường Sa territorial sovereignty markers
      L.marker([16.5, 112.0], {
        icon: L.divIcon({ className: "island-lbl", html: '<div style="background:rgba(20,30,40,0.85);color:#2dd4bf;padding:2px 6px;border-radius:4px;border:1px solid #2dd4bf;font-weight:700;font-size:10px;white-space:nowrap;font-family:monospace;">🇻🇳 QĐ. Hoàng Sa (Việt Nam)</div>' }),
        keyboard: false
      }).addTo(hubMap);

      L.marker([9.5, 113.5], {
        icon: L.divIcon({ className: "island-lbl", html: '<div style="background:rgba(20,30,40,0.85);color:#2dd4bf;padding:2px 6px;border-radius:4px;border:1px solid #2dd4bf;font-weight:700;font-size:10px;white-space:nowrap;font-family:monospace;">🇻🇳 QĐ. Trường Sa (Việt Nam)</div>' }),
        keyboard: false
      }).addTo(hubMap);

      hubMarkersLayer = L.layerGroup().addTo(hubMap);
      renderMapMarkers(HUBS.slice(0, 50));'''

    content = re.sub(old_engine_pattern, new_engine, content, flags=re.DOTALL)

    # 4. Remove dead basemap switcher event listeners in JS
    dead_listener_pattern = r'// Basemap switcher buttons\s*document\.querySelectorAll\("\.map-basemap-btn"\)\.forEach\(btn => \{.*?\n\s*\}\);\n'
    content = re.sub(dead_listener_pattern, '', content, flags=re.DOTALL)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[UPDATED] {path}")

def main():
    print("Enforcing Satellite-only basemap across Industrial Hubs pages...")
    for target in TARGETS:
        update_file(target)
    print("\n[SUCCESS] Exclusive Satellite map applied and OpenStreetMap purged!")

if __name__ == "__main__":
    main()
