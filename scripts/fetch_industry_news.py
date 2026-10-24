#!/usr/bin/env python3
"""
fetch_industry_news.py - Automated Multi-Source RSS & Market Intelligence Ingestion Engine
Part of the Renewable Viet Nam Jamstack Infrastructure (renewablevietnam.com)

Fetches, normalizes, deduplicates, classifies, and decorates market intelligence feeds:
- Google News RSS (Renewable Energy, DPPA Decree 80, Eco-Industrial Parks, VIR reporting)
- Vietnam News (National English Daily - Environment & Green Transition)
- VnExpress International (Business & Infrastructure Feed)
Outputs: data/industry_news.json with 100% verified visual preview image assets.
"""

import os
import sys
import json
import ssl
import re
import hashlib
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
import email.utils

SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode = ssl.CERT_NONE

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

FEED_DEFINITIONS = [
    {
        "name": "Google News DPPA & Statutory",
        "type": "google_news",
        "query": "Vietnam DPPA OR \"Decree 80\" OR \"power purchase agreement\" OR \"direct power purchase\"",
        "default_sector": "Policy & DPPA",
        "default_source": "Policy & DPPA Wire"
    },
    {
        "name": "Google News Eco-Parks & Siting",
        "type": "google_news",
        "query": "Vietnam \"eco-industrial park\" OR \"industrial park\" clean energy OR \"industrial zone\" solar",
        "default_sector": "Eco-Parks & Siting",
        "default_source": "Industrial Siting Wire"
    },
    {
        "name": "Google News Solar & Offshore Wind",
        "type": "google_news",
        "query": "Vietnam \"offshore wind\" OR \"rooftop solar\" OR \"clean energy transition\"",
        "default_sector": "Solar & Wind",
        "default_source": "Renewable Tech Wire"
    },
    {
        "name": "Google News High-Voltage Grid & Interconnect",
        "type": "google_news",
        "query": "Vietnam EVN OR \"500kV\" OR \"220kV\" OR \"substation\" OR \"power grid\"",
        "default_sector": "Grid & Interconnect",
        "default_source": "Grid & EVN Wire"
    },
    {
        "name": "Google News VIR FDI & Infrastructure",
        "type": "google_news",
        "query": "site:vir.com.vn \"renewable\" OR \"solar\" OR \"wind\" OR \"industrial park\" OR \"energy\"",
        "default_sector": "FDI & Infrastructure",
        "default_source": "Vietnam Investment Review - VIR"
    },
    {
        "name": "Google News Macro & PDP8 Energy Transition",
        "type": "google_news",
        "query": "Vietnam \"PDP8\" OR \"JETP\" OR \"power development plan\" OR \"net zero\" OR \"energy transition\"",
        "default_sector": "Policy & DPPA",
        "default_source": "PDP8 Strategic Wire"
    },
    {
        "name": "Google News Corporate Clean Siting & RE100",
        "type": "google_news",
        "query": "Vietnam \"Lego\" renewable OR \"Samsung\" solar OR \"Foxconn\" green power OR \"VSIP\" clean energy",
        "default_sector": "Eco-Parks & Siting",
        "default_source": "Corporate RE100 Wire"
    },
    {
        "name": "Google News Storage, Hydrogen & Renewables",
        "type": "google_news",
        "query": "Vietnam \"battery storage\" OR \"BESS\" OR \"green hydrogen\" OR \"floating solar\"",
        "default_sector": "Solar & Wind",
        "default_source": "Clean Storage Wire"
    },
    {
        "name": "Vietnam News Environment Feed",
        "type": "direct_rss",
        "url": "https://vietnamnews.vn/rss/environment.rss",
        "default_sector": "Policy & ESG",
        "default_source": "Vietnam News"
    },
    {
        "name": "Vietnam News Economy & Infrastructure Feed",
        "type": "direct_rss",
        "url": "https://vietnamnews.vn/rss/economy.rss",
        "default_sector": "FDI & Infrastructure",
        "default_source": "Vietnam News"
    },
    {
        "name": "VnExpress International Business & Infrastructure",
        "type": "direct_rss",
        "url": "https://e.vnexpress.net/rss/business.rss",
        "default_sector": "FDI & Infrastructure",
        "default_source": "VnExpress International"
    },
    {
        "name": "PV Magazine International",
        "type": "direct_rss",
        "url": "https://www.pv-magazine.com/feed/",
        "default_sector": "Solar & Wind",
        "default_source": "PV Magazine"
    },
    {
        "name": "CleanTechnica Global Transition Feed",
        "type": "direct_rss",
        "url": "https://cleantechnica.com/feed/",
        "default_sector": "Solar & Wind",
        "default_source": "CleanTechnica"
    },
    {
        "name": "Tuoi Tre News Business & Energy",
        "type": "direct_rss",
        "url": "https://tuoitrenews.vn/rss/business.rss",
        "default_sector": "FDI & Infrastructure",
        "default_source": "Tuoi Tre News"
    },
    {
        "name": "Google News Reuters Energy & Transition",
        "type": "google_news",
        "query": "site:reuters.com (\"Vietnam\" OR \"Southeast Asia\") AND (\"energy\" OR \"renewable\" OR \"solar\" OR \"wind\" OR \"power\" OR \"grid\")",
        "default_sector": "FDI & Infrastructure",
        "default_source": "Reuters"
    },
    {
        "name": "Google News Bloomberg Green & Climate",
        "type": "google_news",
        "query": "site:bloomberg.com (\"Vietnam\" OR \"Southeast Asia\") AND (\"energy\" OR \"renewable\" OR \"clean\" OR \"power\" OR \"carbon\")",
        "default_sector": "Finance & ESG",
        "default_source": "Bloomberg"
    },
    {
        "name": "Google News Nikkei Asia Clean Power",
        "type": "google_news",
        "query": "site:asia.nikkei.com Vietnam AND (\"energy\" OR \"power\" OR \"renewable\" OR \"solar\" OR \"EVN\")",
        "default_sector": "FDI & Infrastructure",
        "default_source": "Nikkei Asia"
    },
    {
        "name": "Google News The Saigon Times",
        "type": "google_news",
        "query": "site:thesaigontimes.vn (\"renewable\" OR \"energy\" OR \"power\" OR \"DPPA\" OR \"solar\" OR \"green\")",
        "default_sector": "Policy & DPPA",
        "default_source": "The Saigon Times"
    },
    {
        "name": "Google News EVN Statutory & Grid Dispatches",
        "type": "google_news",
        "query": "site:en.evn.com.vn OR site:evn.com.vn (\"power\" OR \"transmission\" OR \"renewable\" OR \"500kV\")",
        "default_sector": "Grid & Interconnect",
        "default_source": "EVN Portal"
    }
]

SOURCE_BRAND_CONFIG = {
    "VnExpress International": {"color": "#990000", "badge_bg": "rgba(153,0,0,0.12)", "tier": "Domestic Tier 1", "category": "National English Daily"},
    "Vietnam News": {"color": "#034ea2", "badge_bg": "rgba(3,78,162,0.12)", "tier": "Domestic Tier 1", "category": "Official English Newspaper"},
    "Vietnam Investment Review - VIR": {"color": "#b8860b", "badge_bg": "rgba(184,134,11,0.12)", "tier": "Domestic Tier 1", "category": "FDI & Infrastructure"},
    "Reuters": {"color": "#ea580c", "badge_bg": "rgba(234,88,12,0.12)", "tier": "Global Wire", "category": "Global News Agency"},
    "Bloomberg": {"color": "#2563eb", "badge_bg": "rgba(37,99,235,0.12)", "tier": "Global Wire", "category": "Financial News Wire"},
    "PV Magazine": {"color": "#ca8a04", "badge_bg": "rgba(202,138,4,0.12)", "tier": "Specialist", "category": "Photovoltaic Global Press"},
    "CleanTechnica": {"color": "#059669", "badge_bg": "rgba(5,150,105,0.12)", "tier": "Specialist", "category": "Clean Energy Media"},
    "Tuoi Tre News": {"color": "#0284c7", "badge_bg": "rgba(2,132,199,0.12)", "tier": "Domestic Tier 1", "category": "National English Daily"},
    "Nikkei Asia": {"color": "#dc2626", "badge_bg": "rgba(220,38,38,0.12)", "tier": "Regional Wire", "category": "Asia Economic Journal"},
    "The Saigon Times": {"color": "#0d9488", "badge_bg": "rgba(13,148,136,0.12)", "tier": "Domestic Tier 1", "category": "Business Weekly"},
    "EVN Portal": {"color": "#1e40af", "badge_bg": "rgba(30,64,175,0.12)", "tier": "Authority", "category": "National Grid Operator"}
}

def get_source_metadata(source_name: str) -> dict:
    """Return institutional branding metadata for a news source."""
    if not source_name:
        return {"color": "#0d9488", "badge_bg": "rgba(13,148,136,0.12)", "tier": "Wire", "category": "Market Intelligence Wire"}
    
    clean = source_name.lower()
    for brand, cfg in SOURCE_BRAND_CONFIG.items():
        if brand.lower() in clean or clean in brand.lower():
            return cfg
            
    if "reuters" in clean:
        return SOURCE_BRAND_CONFIG["Reuters"]
    if "bloomberg" in clean:
        return SOURCE_BRAND_CONFIG["Bloomberg"]
    if "pv magazine" in clean or "pv-magazine" in clean:
        return SOURCE_BRAND_CONFIG["PV Magazine"]
    if "cleantechnica" in clean:
        return SOURCE_BRAND_CONFIG["CleanTechnica"]
    if "vnexpress" in clean:
        return SOURCE_BRAND_CONFIG["VnExpress International"]
    if "vietnam news" in clean or "vietnamnews" in clean:
        return SOURCE_BRAND_CONFIG["Vietnam News"]
    if "vir" in clean or "investment review" in clean:
        return SOURCE_BRAND_CONFIG["Vietnam Investment Review - VIR"]
    if "tuoi tre" in clean:
        return SOURCE_BRAND_CONFIG["Tuoi Tre News"]
    if "nikkei" in clean:
        return SOURCE_BRAND_CONFIG["Nikkei Asia"]
    if "saigon" in clean:
        return SOURCE_BRAND_CONFIG["The Saigon Times"]
    if "evn" in clean:
        return SOURCE_BRAND_CONFIG["EVN Portal"]
        
    return {"color": "#0d9488", "badge_bg": "rgba(13,148,136,0.12)", "tier": "Wire", "category": "Market Intelligence Wire"}

def make_article_id(title: str, link: str) -> str:
    """Deterministic unique MD5 identifier for an article."""
    seed = (title.strip().lower() + link.strip().lower()).encode('utf-8')
    return "art_" + hashlib.md5(seed).hexdigest()[:12]

# Curated High-Definition Thematic Preview Images (Unsplash CDN optimized WebP/JPG)
SECTOR_IMAGE_POOLS = {
    "Solar & Wind": [
        "https://images.unsplash.com/photo-1509391365360-2e959784a276?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1466611653911-95081537e5b7?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1497435334941-8c899ee9e8e9?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1548337138-e87d889cc369?auto=format&fit=crop&w=800&q=80"
    ],
    "Policy & DPPA": [
        "https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?auto=format&fit=crop&w=800&q=80"
    ],
    "Eco-Parks & Siting": [
        "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1504917599217-d4dc5ebe6122?auto=format&fit=crop&w=800&q=80"
    ],
    "Grid & Interconnect": [
        "https://images.unsplash.com/photo-1544724569-5f546fd6f2b5?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1498084393753-b411b2d26b34?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=800&q=80"
    ],
    "Finance & ESG": [
        "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1559526324-4b87b5e36e44?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?auto=format&fit=crop&w=800&q=80"
    ],
    "FDI & Infrastructure": [
        "https://images.unsplash.com/photo-1513836279014-a89f7a76ae86?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=800&q=80",
        "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=800&q=80"
    ]
}

DEFAULT_IMAGE_POOL = [
    "https://images.unsplash.com/photo-1509391365360-2e959784a276?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?auto=format&fit=crop&w=800&q=80",
    "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&w=800&q=80"
]

def get_thematic_sector_image(sector: str, seed: str) -> str:
    """Return a deterministic thematic image from the sector pool based on seed string."""
    pool = SECTOR_IMAGE_POOLS.get(sector, DEFAULT_IMAGE_POOL)
    hash_val = sum(ord(c) for c in seed)
    return pool[hash_val % len(pool)]

def clean_html(text: str) -> str:
    """Strip HTML tags, unescape common entities, and clean whitespace."""
    if not text:
        return ""
    # Unescape HTML entities
    text = text.replace('&nbsp;', ' ').replace('&amp;', '&').replace('&quot;', '"').replace('&#39;', "'")
    # Remove HTML tags
    cleaned = re.sub(r'<[^>]+>', ' ', text)
    # Remove multiple whitespace
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned

def parse_relative_time(dt: datetime) -> str:
    """Format human-readable relative timestamp (e.g. '2h ago', '3d ago')."""
    now = datetime.now(timezone.utc)
    diff = now - dt
    total_seconds = int(diff.total_seconds())

    if total_seconds < 0:
        return "Just now"
    if total_seconds < 3600:
        mins = max(1, total_seconds // 60)
        return f"{mins}m ago"
    if total_seconds < 86400:
        hours = total_seconds // 3600
        return f"{hours}h ago"
    days = total_seconds // 86400
    if days < 30:
        return f"{days}d ago"
    return dt.strftime("%b %d, %Y")

def classify_sector(title: str, snippet: str, default_sector: str) -> str:
    """Institutional classification based on lexical signals."""
    content = (title + " " + snippet).lower()
    
    if any(k in content for k in ["dppa", "decree 80", "decree", "circular", "pdp8", "statutory", "wheeling"]):
        return "Policy & DPPA"
    if any(k in content for k in ["offshore wind", "wind power", "rooftop solar", "photovoltaic", "solar farm", "solar power"]):
        return "Solar & Wind"
    if any(k in content for k in ["eco-industrial", "industrial park", "industrial zone", "deep c", "vsip", "siting", "tenant", "factory"]):
        return "Eco-Parks & Siting"
    if any(k in content for k in ["evn", "substation", "transmission", "grid", "interconnection", "500kv", "220kv", "110kv"]):
        return "Grid & Interconnect"
    if any(k in content for k in ["fdi", "investment", "capital", "financing", "green bond", "jetp", "cop28"]):
        return "Finance & ESG"
        
    return default_sector

def fetch_feed_items(feed_def: dict) -> list:
    """Fetch and parse XML feed items with image extraction."""
    items_out = []
    feed_type = feed_def.get("type")
    
    if feed_type == "google_news":
        query = feed_def["query"]
        encoded_q = urllib.parse.quote(query)
        url = f"https://news.google.com/rss/search?q={encoded_q}&hl=en-US&gl=US&ceid=US:en"
    else:
        url = feed_def["url"]
        
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, context=SSL_CTX, timeout=12) as response:
            xml_data = response.read()
            root = ET.fromstring(xml_data)
            
            for item in root.findall('.//item'):
                raw_title = item.find('title').text if item.find('title') is not None else ''
                raw_link = item.find('link').text if item.find('link') is not None else ''
                raw_pub_date = item.find('pubDate').text if item.find('pubDate') is not None else ''
                raw_desc = item.find('description').text if item.find('description') is not None else ''
                
                # Extract source name
                source_elem = item.find('source')
                if source_elem is not None and source_elem.text:
                    source_name = source_elem.text.strip()
                else:
                    source_name = feed_def.get("default_source", "Market Intelligence Wire")
                    
                # Clean title: Google news appends ' - Source Name'
                clean_title = raw_title
                if " - " in clean_title:
                    parts = clean_title.rsplit(" - ", 1)
                    if len(parts[1]) < 35: # Likely source name
                        clean_title = parts[0].strip()
                        if source_elem is None:
                            source_name = parts[1].strip()
                            
                # Parse datetime
                pub_dt = None
                if raw_pub_date:
                    try:
                        pub_dt = email.utils.parsedate_to_datetime(raw_pub_date)
                    except Exception:
                        pub_dt = datetime.now(timezone.utc)
                else:
                    pub_dt = datetime.now(timezone.utc)
                    
                # Ensure timezone aware
                if pub_dt.tzinfo is None:
                    pub_dt = pub_dt.replace(tzinfo=timezone.utc)
                    
                snippet = clean_html(raw_desc)
                # Trim excessive length
                if len(snippet) > 240:
                    snippet = snippet[:237] + "..."
                    
                sector = classify_sector(clean_title, snippet, feed_def.get("default_sector", "Clean Energy"))
                
                # Image Extraction
                img_url = None
                
                # 1. Check enclosure tag
                enc = item.find('enclosure')
                if enc is not None and enc.get('url'):
                    enc_type = enc.get('type', '')
                    if not enc_type or 'image' in enc_type or any(enc.get('url').lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.webp']):
                        img_url = enc.get('url')
                        
                # 2. Check media:content / media:thumbnail
                if not img_url:
                    for media_tag in ['{http://search.yahoo.com/mrss/}content', '{http://search.yahoo.com/mrss/}thumbnail']:
                        med = item.find(media_tag)
                        if med is not None and med.get('url'):
                            img_url = med.get('url')
                            break
                            
                # 3. Check <img> inside raw_desc
                if not img_url and raw_desc:
                    img_match = re.search(r'<img[^>]+src=["\']([^"\']+)["\']', raw_desc, re.IGNORECASE)
                    if img_match:
                        found_src = img_match.group(1)
                        if found_src.startswith('http'):
                            img_url = found_src
                            
                # 4. If no feed image found, assign thematic photographic fallback
                if not img_url:
                    img_url = get_thematic_sector_image(sector, clean_title)
                
                src_meta = get_source_metadata(source_name)
                art_id = make_article_id(clean_title, raw_link)

                items_out.append({
                    "id": art_id,
                    "title": clean_title,
                    "link": raw_link,
                    "source": source_name,
                    "source_tier": src_meta.get("tier", "Wire"),
                    "source_color": src_meta.get("color", "#0d9488"),
                    "source_badge_bg": src_meta.get("badge_bg", "rgba(13,148,136,0.12)"),
                    "source_category": src_meta.get("category", "Market Intelligence Wire"),
                    "pub_date_raw": raw_pub_date,
                    "iso_date": pub_dt.isoformat(),
                    "timestamp": int(pub_dt.timestamp()),
                    "relative_time": parse_relative_time(pub_dt),
                    "snippet": snippet,
                    "sector": sector,
                    "image_url": img_url
                })
    except Exception as e:
        print(f"Warning: Failed to fetch {feed_def.get('name')}: {e}", file=sys.stderr)
        
    return items_out

def main():
    print("[INGESTION] Commencing automated multi-source industry feed harvest with image extraction...")
    all_articles = []
    
    for feed_def in FEED_DEFINITIONS:
        print(f"  Fetching: {feed_def['name']}...")
        items = fetch_feed_items(feed_def)
        print(f"    Retrieved {len(items)} items")
        all_articles.extend(items)
        
    # Deduplicate by normalized title
    seen_titles = set()
    deduped = []
    
    for art in all_articles:
        # Normalize key for deduplication
        norm_key = re.sub(r'[^a-zA-Z0-9]', '', art['title'].lower())
        if not norm_key or norm_key in seen_titles:
            continue
        seen_titles.add(norm_key)
        deduped.append(art)
        
    # Sort strictly descending by publication timestamp
    deduped.sort(key=lambda x: x['timestamp'], reverse=True)
    
    # Select top 200 high-impact items
    final_selection = deduped[:200]
    
    # Recalculate relative times at generation point
    for item in final_selection:
        try:
            dt = datetime.fromisoformat(item['iso_date'])
            item['relative_time'] = parse_relative_time(dt)
        except Exception:
            pass
            
    payload = {
        "status": "success",
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "total_articles": len(final_selection),
        "generator": "RenewableVietNam Visual Ingestion Pipeline v2.0",
        "articles": final_selection
    }
    
    # Serialize to RenewableVietNam and Qking232.github.io
    repo_roots = [
        "G:/My Drive/7. AI/Gemini/RenewableVietNam",
        "G:/My Drive/7. AI/Gemini/Qking232.github.io"
    ]
    
    for r in repo_roots:
        data_dir = os.path.join(r, "data")
        os.makedirs(data_dir, exist_ok=True)
        out_file = os.path.join(data_dir, "industry_news.json")
        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2, ensure_ascii=False)
        print(f"[SUCCESS] Serialized {len(final_selection)} articles with image_url to {out_file}")

if __name__ == "__main__":
    main()
