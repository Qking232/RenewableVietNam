#!/usr/bin/env python3
"""
Renewable Vietnam — Automated Static Dataset GZIP Synchronization Engine
Scans RenewableVietNam/data/ for all JSON datasets and generates maximum-compression
(.json.gz) archives for transparent native DecompressionStream ingestion.
"""

import os
import gzip
import json
import sys

DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))

def sync_gzip():
    if not os.path.isdir(DATA_DIR):
        print(f"Error: Data directory not found: {DATA_DIR}")
        sys.exit(1)

    json_files = [f for f in os.listdir(DATA_DIR) if f.endswith('.json') and not f.endswith('.json.gz')]
    print(f"[GZIP ENGINE] Found {len(json_files)} JSON datasets in {DATA_DIR}")

    total_raw_bytes = 0
    total_gz_bytes = 0

    for fname in sorted(json_files):
        json_path = os.path.join(DATA_DIR, fname)
        gz_path = os.path.join(DATA_DIR, fname + '.gz')

        raw_size = os.path.getsize(json_path)
        total_raw_bytes += raw_size

        # Verify JSON validity before compression
        try:
            with open(json_path, 'rb') as f_in:
                raw_bytes = f_in.read()
                json.loads(raw_bytes.decode('utf-8'))
        except Exception as err:
            print(f"  [ERROR] Invalid JSON in {fname}: {err}")
            continue

        # Check if .gz exists and is newer than source
        need_recompress = True
        if os.path.exists(gz_path):
            if os.path.getmtime(gz_path) >= os.path.getmtime(json_path):
                # Verify GZIP validity
                try:
                    with gzip.open(gz_path, 'rb') as f_gz:
                        decompressed = f_gz.read()
                        if decompressed == raw_bytes:
                            need_recompress = False
                            gz_size = os.path.getsize(gz_path)
                            total_gz_bytes += gz_size
                            ratio = (1 - (gz_size / raw_size)) * 100 if raw_size else 0
                            print(f"  [UP-TO-DATE] {fname:<45} Raw: {raw_size/1024:>8.1f} KB | GZ: {gz_size/1024:>8.1f} KB (-{ratio:.1f}%)")
                except Exception:
                    need_recompress = True

        if need_recompress:
            with open(json_path, 'rb') as f_in:
                with gzip.open(gz_path, 'wb', compresslevel=9) as f_out:
                    f_out.write(raw_bytes)
            gz_size = os.path.getsize(gz_path)
            total_gz_bytes += gz_size
            ratio = (1 - (gz_size / raw_size)) * 100 if raw_size else 0
            print(f"  [COMPRESSED] {fname:<45} Raw: {raw_size/1024:>8.1f} KB | GZ: {gz_size/1024:>8.1f} KB (-{ratio:.1f}%)")

    overall_reduction = (1 - (total_gz_bytes / total_raw_bytes)) * 100 if total_raw_bytes else 0
    print(f"\n[GZIP SUMMARY] Total Raw: {total_raw_bytes/1024/1024:.2f} MB | Total GZ: {total_gz_bytes/1024/1024:.2f} MB | Overall Bandwidth Reduction: -{overall_reduction:.1f}%")

if __name__ == '__main__':
    sync_gzip()
