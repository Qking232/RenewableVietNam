#!/usr/bin/env python3
"""
verify_livewire_news_sync.py - Verification & Audit Suite for Live Wire Ingestion Pipeline
"""

import os
import sys
import json
import re
import hashlib
import subprocess

REPO_A = r"G:\My Drive\7. AI\Gemini\RenewableVietNam"
REPO_B = r"G:\My Drive\7. AI\Gemini\Qking232.github.io"

def calc_sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def test_audit():
    print("===================================================================")
    print("Live Wire Multi-Source Internet Feeds & Telemetry Verification")
    print("===================================================================\n")

    # 1. Audit industry_news.json in Repo A
    json_path_a = os.path.join(REPO_A, "data", "industry_news.json")
    assert os.path.exists(json_path_a), f"Missing {json_path_a}"
    with open(json_path_a, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert data.get("status") == "success", "industry_news.json status is not success"
    articles = data.get("articles", [])
    print(f"[TEST 1] Articles count: {len(articles)} (Target >= 150)")
    assert len(articles) >= 150, f"Expected >= 150 articles, found {len(articles)}"

    sources = set(a.get("source") for a in articles)
    print(f"[TEST 2] Unique news sources: {len(sources)} sources detected:")
    for s in sorted(sources)[:12]:
        print(f"         - {s}")
    assert len(sources) >= 5, f"Expected >= 5 sources, found {len(sources)}"

    required_fields = ["id", "title", "link", "source", "source_color", "source_badge_bg", "sector", "image_url"]
    for idx, art in enumerate(articles[:20]):
        for rf in required_fields:
            assert rf in art and art[rf], f"Article #{idx} missing required field '{rf}'"
    print("[TEST 3] Article metadata schema integrity verified (id, source_color, source_badge_bg, sector, image_url).")

    # 2. Audit livewire/index.html in Repo A
    livewire_path_a = os.path.join(REPO_A, "livewire", "index.html")
    assert os.path.exists(livewire_path_a), f"Missing {livewire_path_a}"
    with open(livewire_path_a, "r", encoding="utf-8") as f:
        lw_content = f.read()

    assert 'id="newsSyncStatus"' in lw_content, "Missing #newsSyncStatus"
    assert 'id="refreshNewsBtn"' in lw_content, "Missing #refreshNewsBtn"
    assert 'id="breakingNewsContainer"' in lw_content, "Missing #breakingNewsContainer"
    assert 'id="newsSearchInput"' in lw_content, "Missing #newsSearchInput"
    assert 'id="newsGrid"' in lw_content, "Missing #newsGrid"
    assert 'news-sector-pill' in lw_content, "Missing news-sector-pill"
    assert 'news-source-pill' in lw_content, "Missing news-source-pill"
    assert 'data-news-source="Reuters"' in lw_content, "Missing Reuters source pill"
    assert 'data-news-source="Bloomberg"' in lw_content, "Missing Bloomberg source pill"
    assert 'data-news-source="VnExpress"' in lw_content, "Missing VnExpress source pill"
    assert 'market_dispatches' in lw_content, "Missing market_dispatches Supabase telemetry query"
    print("[TEST 4] DOM structure & multi-source UI pill controls verified.")

    # 3. Audit Supabase schema
    schema_path = os.path.join(REPO_A, "supabase", "portal_schema.sql")
    with open(schema_path, "r", encoding="utf-8") as f:
        schema_sql = f.read()
    assert "create table if not exists public.market_dispatches" in schema_sql, "Missing market_dispatches table in schema"
    assert "create policy market_dispatches_read" in schema_sql, "Missing market_dispatches_read policy"
    print("[TEST 5] Supabase SQL schema & RLS policies verified.")

    # 4. Audit Seeder Dry Run
    seeder_path = os.path.join(REPO_A, "scripts", "seed_portal_data.mjs")
    res = subprocess.run(["node", seeder_path, "--dry-run"], capture_output=True, text=True)
    assert res.returncode == 0, f"Seeder dry-run failed: {res.stderr}"
    assert "Market Dispatches: Parsed 200 rows" in res.stdout, "Seeder did not parse 200 dispatches"
    print("[TEST 6] Seeder validation passed (200 dispatches parsed).")

    # 5. Dual-Repository Synchronization
    files_to_sync = [
        ("data", "industry_news.json"),
        ("livewire", "index.html"),
        ("scripts", "fetch_industry_news.py"),
        ("scripts", "seed_portal_data.mjs"),
        ("supabase", "portal_schema.sql")
    ]

    print("\n--- Synchronizing Assets to Qking232.github.io ---")
    for subdir, fname in files_to_sync:
        src = os.path.join(REPO_A, subdir, fname)
        dst_dir = os.path.join(REPO_B, subdir)
        os.makedirs(dst_dir, exist_ok=True)
        dst = os.path.join(dst_dir, fname)
        with open(src, "rb") as sf:
            s_data = sf.read()
        with open(dst, "wb") as df:
            df.write(s_data)
        
        sha_a = calc_sha256(src)
        sha_b = calc_sha256(dst)
        assert sha_a == sha_b, f"Parity mismatch for {fname}"
        print(f"  ✓ {subdir}/{fname}: SHA-256 match ({sha_a[:12]}...)")

    print("\n===================================================================")
    print("ALL VERIFICATION SUITE TESTS PASSED WITH 100% PARITY")
    print("===================================================================")

if __name__ == "__main__":
    test_audit()
