#!/usr/bin/env python3
"""
fetch_industry_news.py - Automated Multi-Source RSS & Market Intelligence Ingestion Engine
Part of the Renewable Viet Nam Jamstack Infrastructure (renewablevietnam.com)

Fetches, normalizes, deduplicates, and classifies market intelligence feeds:
- Google News RSS (Renewable Energy, DPPA Decree 80, Eco-Industrial Parks, VIR reporting)
- Vietnam News (National English Daily - Environment & Green Transition)
Outputs: data/industry_news.json
"""

import os
import sys
import json
import ssl
import re
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
        "default_sector": "Policy & DPPA"
    },
    {
        "name": "Google News Eco-Parks & Siting",
        "type": "google_news",
        "query": "Vietnam \"eco-industrial park\" OR \"industrial park\" clean energy OR \"industrial zone\" solar",
        "default_sector": "Eco-Parks & Siting"
    },
    {
        "name": "Google News Solar & Offshore Wind",
        "type": "google_news",
        "query": "Vietnam \"offshore wind\" OR \"rooftop solar\" OR \"clean energy transition\"",
        "default_sector": "Solar & Wind"
    },
    {
        "name": "Google News High-Voltage Grid & Interconnect",
        "type": "google_news",
        "query": "Vietnam EVN OR \"500kV\" OR \"220kV\" OR \"substation\" OR \"power grid\"",
        "default_sector": "Grid & Interconnect"
    },
    {
        "name": "Google News VIR FDI & Infrastructure",
        "type": "google_news",
        "query": "site:vir.com.vn \"renewable\" OR \"solar\" OR \"wind\" OR \"industrial park\" OR \"energy\"",
        "default_sector": "FDI & Infrastructure"
    },
    {
        "name": "Google News Macro & PDP8 Energy Transition",
        "type": "google_news",
        "query": "Vietnam \"PDP8\" OR \"JETP\" OR \"power development plan\" OR \"net zero\" OR \"energy transition\"",
        "default_sector": "Policy & DPPA"
    },
    {
        "name": "Google News Corporate Clean Siting & RE100",
        "type": "google_news",
        "query": "Vietnam \"Lego\" renewable OR \"Samsung\" solar OR \"Foxconn\" green power OR \"VSIP\" clean energy",
        "default_sector": "Eco-Parks & Siting"
    },
    {
        "name": "Google News Storage, Hydrogen & Renewables",
        "type": "google_news",
        "query": "Vietnam \"battery storage\" OR \"BESS\" OR \"green hydrogen\" OR \"floating solar\"",
        "default_sector": "Solar & Wind"
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
    }
]

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
    """Fetch and parse XML feed items."""
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
                
                items_out.append({
                    "title": clean_title,
                    "link": raw_link,
                    "source": source_name,
                    "pub_date_raw": raw_pub_date,
                    "iso_date": pub_dt.isoformat(),
                    "timestamp": int(pub_dt.timestamp()),
                    "relative_time": parse_relative_time(pub_dt),
                    "snippet": snippet,
                    "sector": sector
                })
    except Exception as e:
        print(f"Warning: Failed to fetch {feed_def.get('name')}: {e}", file=sys.stderr)
        
    return items_out

def main():
    print("[INGESTION] Commencing automated multi-source industry feed harvest...")
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
        "generator": "RenewableVietNam Ingestion Pipeline v1.0",
        "articles": final_selection
    }
    
    # Ensure destination directory exists
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(repo_root, "data")
    os.makedirs(data_dir, exist_ok=True)
    out_file = os.path.join(data_dir, "industry_news.json")
    
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
        
    print(f"\n[SUCCESS] Serialized {len(final_selection)} articles to {out_file}")

if __name__ == "__main__":
    main()
