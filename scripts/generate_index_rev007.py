#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate index_Rev.007.html:
1. Replace relative Leaflet paths with official CDN (unpkg.com/leaflet@1.9.4) matching evcharging.
2. Fix asynchronous vector race condition: trigger renderMainFlowVectors() dynamically in loadGridData() and loadProjectsData().
3. Add robust multi-stage invalidateSize() (100ms, 300ms, 600ms, 1200ms) and Vietnam fitBounds.
4. Add tile fallback to OpenStreetMap if CartoDB tile errors occur.
5. Hoist initEnergyCharts() to global scope and trigger on load.
"""

import re
from pathlib import Path

SOURCE_HTML = Path(r"G:\My Drive\7. AI\RenewableVietNam\projectenergy\index.html")
TARGET_HTML = Path(r"G:\My Drive\7. AI\RenewableVietNam\projectenergy\index_Rev.007.html")

def generate_rev007():
    with open(SOURCE_HTML, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Replace relative Leaflet CSS & JS with unpkg CDN
    old_leaflet_tags = """  <!-- Leaflet GIS Cartography Engine for National Transmission Grid -->
  <link rel="stylesheet" href="vendor/leaflet/leaflet.css" />
  <script src="vendor/leaflet/leaflet.js"></script>"""

    new_leaflet_tags = """  <!-- Leaflet GIS Cartography Engine (Official CDN & Root Fallback) -->
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin="" />
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>"""

    if old_leaflet_tags in html:
        html = html.replace(old_leaflet_tags, new_leaflet_tags, 1)
    else:
        # Fallback replacement
        html = re.sub(r'<link rel="stylesheet" href="[^"]*leaflet\.css"[^>]*>', '<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />', html)
        html = re.sub(r'<script src="[^"]*leaflet\.js"[^>]*></script>', '<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>', html)

    # 2. Update initMainFlowMap implementation with bounds fitting, fallback tiles & multi-stage invalidateSize
    old_init_map_pattern = r'function initMainFlowMap\(\)[\s\S]*?renderMainFlowVectors\(\);\s*}'
    
    new_init_map_code = """function initMainFlowMap() {
      const mapEl = document.getElementById('mainEnergyFlowMap');
      if (!mapEl) return;
      if (typeof L === 'undefined') {
        console.warn('Leaflet engine loading delayed, retrying in 250ms...');
        setTimeout(initMainFlowMap, 250);
        return;
      }

      if (!mainFlowMapInstance) {
        mainFlowMapInstance = L.map('mainEnergyFlowMap', {
          center: [16.2, 107.5],
          zoom: 6,
          zoomControl: true,
          attributionControl: false
        });

        const isDark = document.documentElement.classList.contains('dark');
        const tileUrl = isDark 
          ? 'https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png'
          : 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png';

        const baseTileLayer = L.tileLayer(tileUrl, {
          maxZoom: 18,
          subdomains: 'abcd',
          attribution: '&copy; CartoDB &copy; OpenStreetMap'
        });

        baseTileLayer.on('tileerror', function() {
          console.warn('CartoDB tile warning, activating OpenStreetMap fallback');
          L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', { maxZoom: 18 }).addTo(mainFlowMapInstance);
        });

        baseTileLayer.addTo(mainFlowMapInstance);

        mainFlow500Layer = L.layerGroup().addTo(mainFlowMapInstance);
        mainGrid220Layer = L.layerGroup();
        mainAssetsLayer = L.layerGroup().addTo(mainFlowMapInstance);

        // Bind filter toggles
        document.getElementById('mapToggleFlow500Btn')?.addEventListener('click', function() {
          show500Flow = !show500Flow;
          if (show500Flow) {
            mainFlowMapInstance.addLayer(mainFlow500Layer);
            this.classList.add('bg-rose-600', 'text-white', 'font-semibold');
            this.classList.remove('bg-white', 'dark:bg-darkCard', 'text-inkMuted', 'dark:text-textDarkMuted');
          } else {
            mainFlowMapInstance.removeLayer(mainFlow500Layer);
            this.classList.remove('bg-rose-600', 'text-white', 'font-semibold');
            this.classList.add('bg-white', 'dark:bg-darkCard', 'text-inkMuted', 'dark:text-textDarkMuted');
          }
        });

        document.getElementById('mapToggleGrid220Btn')?.addEventListener('click', function() {
          show220Grid = !show220Grid;
          if (show220Grid) {
            mainFlowMapInstance.addLayer(mainGrid220Layer);
            this.classList.add('bg-amber-600', 'text-white', 'font-semibold');
            this.classList.remove('bg-white', 'dark:bg-darkCard', 'text-inkMuted', 'dark:text-textDarkMuted');
          } else {
            mainFlowMapInstance.removeLayer(mainGrid220Layer);
            this.classList.remove('bg-amber-600', 'text-white', 'font-semibold');
            this.classList.add('bg-white', 'dark:bg-darkCard', 'text-inkMuted', 'dark:text-textDarkMuted');
          }
        });

        document.getElementById('mapToggleAssetsBtn')?.addEventListener('click', function() {
          showCleanAssets = !showCleanAssets;
          if (showCleanAssets) {
            mainFlowMapInstance.addLayer(mainAssetsLayer);
            this.classList.add('bg-teal-600', 'text-white', 'font-semibold');
            this.classList.remove('bg-white', 'dark:bg-darkCard', 'text-inkMuted', 'dark:text-textDarkMuted');
          } else {
            mainFlowMapInstance.removeLayer(mainAssetsLayer);
            this.classList.remove('bg-teal-600', 'text-white', 'font-semibold');
            this.classList.add('bg-white', 'dark:bg-darkCard', 'text-inkMuted', 'dark:text-textDarkMuted');
          }
        });

        document.getElementById('mapToggleResetViewBtn')?.addEventListener('click', function() {
          mainFlowMapInstance.fitBounds([[8.4, 102.1], [23.4, 109.5]], { padding: [15, 15] });
        });

        // Set initial bounds to entire Vietnam
        mainFlowMapInstance.fitBounds([[8.4, 102.1], [23.4, 109.5]], { padding: [15, 15] });
      }

      // Multi-stage size invalidation ensuring zero black container tiles
      [80, 200, 500, 1000].forEach(delay => {
        setTimeout(() => {
          if (mainFlowMapInstance) mainFlowMapInstance.invalidateSize();
        }, delay);
      });

      renderMainFlowVectors();
    }"""

    html = re.sub(old_init_map_pattern, new_init_map_code, html, count=1)

    # 3. Update loadGridData to explicitly call renderMainFlowVectors() and invalidateSize()
    old_load_grid_end = """        renderGridSubstationsTable();
        renderGridLinesTable();
        if (activeTab === 'grid') {
          setTimeout(initGridMap, 100);
        }
      } catch (err) {"""

    new_load_grid_end = """        renderGridSubstationsTable();
        renderGridLinesTable();
        renderMainFlowVectors();
        if (mainFlowMapInstance) mainFlowMapInstance.invalidateSize();
        if (activeTab === 'grid') {
          setTimeout(initGridMap, 100);
        }
      } catch (err) {"""

    html = html.replace(old_load_grid_end, new_load_grid_end, 1)

    # 4. Update loadProjectsData to explicitly call renderMainFlowVectors()
    old_load_proj_pattern = r'initEnergyCharts\(\);\s*initMainFlowMap\(\);\s*return;'
    new_load_proj_code = """initEnergyCharts();
          initMainFlowMap();
          renderMainFlowVectors();
          return;"""

    html = re.sub(old_load_proj_pattern, new_load_proj_code, html)

    # 5. Add window.addEventListener('load') to guarantee late triggers
    late_trigger = """      // Initial Data Loading & Multi-Stage Cartography Trigger
      loadProjectsData();
      loadPdp8Data();
      loadGridData();
      setTimeout(initMainFlowMap, 150);
      setTimeout(initEnergyCharts, 250);
    });

    window.addEventListener('load', () => {
      setTimeout(() => {
        if (typeof initEnergyCharts === 'function') initEnergyCharts();
        if (typeof initMainFlowMap === 'function') initMainFlowMap();
        if (mainFlowMapInstance) mainFlowMapInstance.invalidateSize();
      }, 300);
    });"""

    dom_end_marker = """      // Initial Data Loading
      loadProjectsData();
      loadPdp8Data();
    });"""

    if dom_end_marker in html:
        html = html.replace(dom_end_marker, late_trigger, 1)
    else:
        # Alternative placement
        html = re.sub(r'loadProjectsData\(\);\s*loadPdp8Data\(\);\s*}\);', late_trigger, html)

    with open(TARGET_HTML, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Generated {TARGET_HTML} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_rev007()
