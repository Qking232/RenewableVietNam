#!/usr/bin/env python3
"""
====================================================================
Relocate Live Intelligence Market Wire Section Superior to PDP8 Tracker
====================================================================
Re-orders the primary sections in <main> so that:
  1. #marketWire (Live Intelligence Wire & RSS Feed)
  2. Hero Section & PDP8 Statutory Telemetry Tracker
  3. #hubs (Interactive Industrial Zone Directory & Map)
  4. #calculator (Power Sizer, EVN Estimator & EU Green Indicators)
Across:
  - RenewableVietNam/index.html
  - RenewableVietNam/green/index.html
  - Qking232.github.io/index.html
  - Qking232.github.io/green/index.html
====================================================================
"""

import os
import re

TARGET_FILES = [
    r"G:\My Drive\7. AI\Gemini\RenewableVietNam\index.html",
    r"G:\My Drive\7. AI\Gemini\RenewableVietNam\green\index.html",
    r"G:\My Drive\7. AI\Gemini\Qking232.github.io\index.html",
    r"G:\My Drive\7. AI\Gemini\Qking232.github.io\green\index.html",
]

def relocate_sections(filepath):
    if not os.path.exists(filepath):
        print(f"[WARN] File not found: {filepath}")
        return False

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Determine line ending
    crlf = "\r\n" in content
    le = "\r\n" if crlf else "\n"

    # Pattern to find the Hero Section and Market Wire Section
    # Hero starts at <!-- HERO & MACRO TELEMETRY HEADER --> or <section class="space-y-4">
    # MarketWire starts at <!-- ==================================================================== -->\s*<!-- REAL-TIME INDUSTRY MARKET INTELLIGENCE WIRE (RSS & APIS)
    
    # Let's locate the markers
    hero_comment = "<!-- HERO & MACRO TELEMETRY HEADER -->"
    market_comment = "<!-- REAL-TIME INDUSTRY MARKET INTELLIGENCE WIRE (RSS & APIS)"
    hubs_comment = "<!-- INTERACTIVE RENEWABLE INDUSTRIAL HUB SCREENER & DIRECTORY"

    if hero_comment not in content or market_comment not in content or hubs_comment not in content:
        print(f"[SKIP] Required comments not found in {filepath}")
        return False

    idx_hero = content.find(hero_comment)
    idx_market = content.find(market_comment)
    idx_hubs = content.find(hubs_comment)

    # Check if marketWire is already before hero
    if idx_market < idx_hero:
        print(f"[INFO] MarketWire already before Hero in {os.path.basename(filepath)}")
        return True

    # Extract Hero block (from hero_comment up to market_comment)
    # Note: preceding separator comment
    # Let's find start of hero section:
    # Look back for "<!-- ==================================================================== -->" before hero_comment if any
    hero_start = content.rfind("<!-- ===", 0, idx_hero)
    if hero_start == -1 or idx_hero - hero_start > 120:
        hero_start = idx_hero

    # Market wire start:
    market_start = content.rfind("<!-- ===", 0, idx_market)
    if market_start == -1 or idx_market - market_start > 120:
        market_start = idx_market

    # Hubs start:
    hubs_start = content.rfind("<!-- ===", 0, idx_hubs)
    if hubs_start == -1 or idx_hubs - hubs_start > 120:
        hubs_start = idx_hubs

    hero_block = content[hero_start:market_start].strip()
    market_block = content[market_start:hubs_start].strip()

    # Update "Across 20 Geocoded Parks" -> "Across 168 Geocoded Parks" in hero_block
    hero_block = hero_block.replace("Across 20 Geocoded Parks", "Across 168 Geocoded Parks")

    # Reconstruct the swapped content
    new_combined = market_block + le + le + "    " + hero_block + le + le + "    "

    content_before = content[:hero_start]
    content_after = content[hubs_start:]

    new_content = content_before + new_combined + content_after

    with open(filepath, "w", encoding="utf-8", newline="") as f:
        f.write(new_content)

    print(f"[SUCCESS] Relocated Market Wire superior to PDP8 Tracker in {os.path.basename(filepath)}")
    return True

if __name__ == "__main__":
    for p in TARGET_FILES:
        print(f"Processing {p}...")
        relocate_sections(p)
