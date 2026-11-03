#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate index_Rev.009.html:
Implement Sovereign Pure Vector Cartography of Vietnam (No third-party raster tiles):
1. Purge L.tileLayer entirely (zero API key watermark, zero third-party tile requests).
2. Render high-definition Vietnam mainland, Phú Quốc, Côn Đảo, and sovereign archipelagos:
   - Quần đảo Hoàng Sa (TP. Đà Nẵng, Việt Nam)
   - Quần đảo Trường Sa (Tỉnh Khánh Hòa, Việt Nam)
3. Permanent institutional sovereignty beacons & labels for Hoàng Sa, Trường Sa, Biển Đông, Hà Nội, Đà Nẵng, TP.HCM.
4. Kinetic 500kV Supergrid flow vectors and 220kV intertie corridors rendered with high contrast over the OLED territory.
"""

import re
from pathlib import Path

SOURCE_HTML = Path(r"G:\My Drive\7. AI\RenewableVietNam\projectenergy\index.html")
TARGET_HTML = Path(r"G:\My Drive\7. AI\RenewableVietNam\projectenergy\index_Rev.009.html")

def generate_rev009():
    with open(SOURCE_HTML, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Add CSS for sovereign labels and territorial beacons
    sovereign_css = """
    /* Sovereign Territorial Toponymy & Island Beacon Styling */
    .sovereignty-badge {
      background: rgba(13, 22, 40, 0.88) !important;
      border: 1px solid rgba(244, 63, 94, 0.5) !important;
      border-radius: 6px !important;
      color: #F8FAFC !important;
      font-family: monospace !important;
      font-size: 10px !important;
      font-weight: 700 !important;
      padding: 3px 6px !important;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.5) !important;
      pointer-events: auto !important;
    }
    .sovereignty-badge:hover {
      border-color: #F43F5E !important;
      box-shadow: 0 0 12px rgba(244, 63, 94, 0.8) !important;
    }
    .sea-label {
      background: transparent !important;
      border: none !important;
      color: rgba(148, 163, 184, 0.35) !important;
      font-family: monospace !important;
      font-size: 13px !important;
      font-weight: 700 !important;
      letter-spacing: 0.25em !important;
      text-transform: uppercase !important;
      box-shadow: none !important;
      pointer-events: none !important;
    }
    .city-label {
      background: rgba(15, 23, 42, 0.85) !important;
      border: 1px solid rgba(255, 255, 255, 0.15) !important;
      border-radius: 4px !important;
      color: #F8FAFC !important;
      font-family: monospace !important;
      font-size: 9px !important;
      font-weight: 600 !important;
      padding: 1px 4px !important;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.4) !important;
    }
"""
    html = html.replace(".headroom-pulse-rose {", f"{sovereign_css}\n    .headroom-pulse-rose {{", 1)

    # 2. Add vietnamTerritoryData state variable & loader
    territory_loader_js = """
    // ========================================================================
    // SOVEREIGN VIETNAM VECTOR TERRITORY LOADER (NO RASTER TILES)
    // ========================================================================
    let VIETNAM_TERRITORY_GEOJSON = null;
    let mainTerritoryLayer = null;

    async function loadVietnamTerritory() {
      try {
        if (window.RV_Supabase) {
          const raw = await window.RV_Supabase.getWithFallback('vietnam_territory', '/data/vietnam_territory.json', {
            cacheKey: 'vietnam_territory'
          });
          if (raw && raw.features) {
            VIETNAM_TERRITORY_GEOJSON = raw;
            renderVietnamTerritoryVectors();
            return;
          }
        }
        const res = await fetch('/data/vietnam_territory.json');
        if (res.ok) {
          VIETNAM_TERRITORY_GEOJSON = await res.json();
          renderVietnamTerritoryVectors();
        }
      } catch (e) {
        console.warn('Territory vector load bypassed:', e);
      }
    }

    function renderVietnamTerritoryVectors() {
      if (!VIETNAM_TERRITORY_GEOJSON) return;

      const isDark = document.documentElement.classList.contains('dark');
      const landFill = isDark ? '#0D172A' : '#F1F5F9';
      const landBorder = isDark ? '#334155' : '#94A3B8';
      const islandFill = '#F43F5E';

      [mainFlowMapInstance, gridMapInstance].forEach(mapInstance => {
        if (!mapInstance) return;

        // Render GeoJSON Landmass Polygons
        L.geoJSON(VIETNAM_TERRITORY_GEOJSON, {
          style: function(feature) {
            const isArchipelago = feature.properties?.type === 'archipelago';
            return {
              fillColor: isArchipelago ? islandFill : landFill,
              fillOpacity: isArchipelago ? 0.95 : 0.92,
              color: isArchipelago ? '#FFFFFF' : landBorder,
              weight: isArchipelago ? 1.5 : 1.2
            };
          }
        }).addTo(mapInstance);

        // Add Sovereign Permanent Anchors & Labels for Hoàng Sa and Trường Sa
        // 1. Quần đảo Hoàng Sa (TP. Đà Nẵng, Việt Nam)
        const hsMarker = L.circleMarker([16.5, 112.0], {
          radius: 8,
          fillColor: '#F43F5E',
          color: '#FFFFFF',
          weight: 2,
          opacity: 1,
          fillOpacity: 0.95
        }).addTo(mapInstance);

        hsMarker.bindTooltip(
          '<div class="text-left font-mono"><strong>QUẦN ĐẢO HOÀNG SA</strong><br><span class="text-[9px] text-slate-300">TP. Đà Nẵng &middot; Việt Nam</span></div>',
          { permanent: true, direction: 'top', offset: [0, -10], className: 'sovereignty-badge' }
        );

        // 2. Quần đảo Trường Sa (Tỉnh Khánh Hòa, Việt Nam)
        const tsMarker = L.circleMarker([9.5, 114.2], {
          radius: 8,
          fillColor: '#F43F5E',
          color: '#FFFFFF',
          weight: 2,
          opacity: 1,
          fillOpacity: 0.95
        }).addTo(mapInstance);

        tsMarker.bindTooltip(
          '<div class="text-left font-mono"><strong>QUẦN ĐẢO TRƯỜNG SA</strong><br><span class="text-[9px] text-slate-300">Tỉnh Khánh Hòa &middot; Việt Nam</span></div>',
          { permanent: true, direction: 'top', offset: [0, -10], className: 'sovereignty-badge' }
        );

        // 3. Biển Đông (East Sea) Maritime Watermark Label
        const seaLabel = L.marker([14.5, 113.8], {
          icon: L.divIcon({
            className: 'sea-label',
            html: 'BIỂN ĐÔNG (EAST SEA)',
            iconSize: [220, 24]
          })
        }).addTo(mapInstance);

        // 4. Key National Cities
        const cities = [
          { name: 'HÀ NỘI', lat: 21.0285, lng: 105.8542 },
          { name: 'ĐÀ NẴNG', lat: 16.0544, lng: 108.2022 },
          { name: 'TP. HỒ CHÍ MINH', lat: 10.7769, lng: 106.7009 }
        ];

        cities.forEach(c => {
          L.circleMarker([c.lat, c.lng], {
            radius: 4.5,
            fillColor: '#FFFFFF',
            color: '#0F172A',
            weight: 1.5,
            opacity: 1,
            fillOpacity: 1
          }).addTo(mapInstance).bindTooltip(
            c.name,
            { permanent: true, direction: 'right', offset: [8, 0], className: 'city-label' }
          );
        });
      });
    }
"""

    html = html.replace(
        '// ========================================================================\n    // INSTITUTIONAL HEADROOM & INTERCONNECTION AUDIT LOGIC (PHASE 1)',
        f'{territory_loader_js}\n\n    // ========================================================================\n    // INSTITUTIONAL HEADROOM & INTERCONNECTION AUDIT LOGIC (PHASE 1)',
        1
    )

    # 3. Overwrite initMainFlowMap to remove raster tiles completely
    old_init_map_pattern = r'function initMainFlowMap\(\)[\s\S]*?renderMainFlowVectors\(\);\s*}'
    new_init_map_code = """function initMainFlowMap() {
      const mapEl = document.getElementById('mainEnergyFlowMap');
      if (!mapEl) return;
      if (typeof L === 'undefined') {
        setTimeout(initMainFlowMap, 250);
        return;
      }

      if (!mainFlowMapInstance) {
        // Pure Vector Map: Zero Raster Tiles, Zero Watermarks, Instant Load
        mainFlowMapInstance = L.map('mainEnergyFlowMap', {
          center: [15.5, 109.0],
          zoom: 5.8,
          zoomControl: true,
          attributionControl: false,
          maxBounds: [[4.0, 98.0], [26.0, 120.0]]
        });

        // Set dark/light container ocean background
        const isDark = document.documentElement.classList.contains('dark');
        mapEl.style.backgroundColor = isDark ? '#070A12' : '#F8FAFC';

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
          mainFlowMapInstance.fitBounds([[7.5, 102.0], [23.5, 116.5]], { padding: [15, 15] });
        });

        // Frame all of Vietnam including Hoàng Sa & Trường Sa
        mainFlowMapInstance.fitBounds([[7.5, 102.0], [23.5, 116.5]], { padding: [15, 15] });

        // Trigger territory render
        renderVietnamTerritoryVectors();
      }

      // Size invalidation
      [50, 150, 400, 800].forEach(delay => {
        setTimeout(() => {
          if (mainFlowMapInstance) mainFlowMapInstance.invalidateSize();
        }, delay);
      });

      renderMainFlowVectors();
    }"""

    html = re.sub(old_init_map_pattern, new_init_map_code, html, count=1)

    # 4. Overwrite initGridMap inside the National Grid tab to also use vector territory (no raster tiles)
    old_init_grid_map = r'function initGridMap\(\)[\s\S]*?renderGridMapVectors\(\);\s*}'
    new_init_grid_map = """function initGridMap() {
      const mapContainer = document.getElementById('gridTopologyMap');
      if (!mapContainer || typeof L === 'undefined') return;

      if (!gridMapInstance) {
        gridMapInstance = L.map('gridTopologyMap', {
          center: [15.5, 109.0],
          zoom: 5.8,
          zoomControl: true,
          attributionControl: false
        });

        const isDark = document.documentElement.classList.contains('dark');
        mapContainer.style.backgroundColor = isDark ? '#070A12' : '#F8FAFC';

        gridMapLayerGroup = L.layerGroup().addTo(gridMapInstance);
        renderVietnamTerritoryVectors();
        gridMapInstance.fitBounds([[7.5, 102.0], [23.5, 116.5]], { padding: [15, 15] });
      }

      renderGridMapVectors();
    }"""

    html = re.sub(old_init_grid_map, new_init_grid_map, html, count=1)

    # 5. Add loadVietnamTerritory() call to DOMContentLoaded
    html = html.replace("loadGridData();", "loadVietnamTerritory();\n      loadGridData();", 1)

    with open(TARGET_HTML, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Successfully generated {TARGET_HTML} ({len(html)} bytes)")

if __name__ == "__main__":
    generate_rev009()
