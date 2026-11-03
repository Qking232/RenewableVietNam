#!/usr/bin/env python3
"""
Automated Verification Suite: Energy Path Migration Validation
Tests directory integrity, canonical links, legacy redirection,
worker configuration, and sitemap entries.
"""

import os
import sys

BASE_DIR = r"G:\My Drive\7. AI\RenewableVietNam"

def test_assertions():
    errors = []

    # 1. energy/index.html exists and non-empty
    energy_index = os.path.join(BASE_DIR, "energy", "index.html")
    if not os.path.exists(energy_index):
        errors.append("energy/index.html does not exist")
    else:
        size = os.path.getsize(energy_index)
        if size < 50000:
            errors.append(f"energy/index.html size unexpectedly small: {size} bytes")
        with open(energy_index, "r", encoding="utf-8") as f:
            content = f.read()
            if 'canonical" href="https://energy.renewablevietnam.com/"' not in content:
                errors.append("Canonical URL in energy/index.html is not https://energy.renewablevietnam.com/")
            if "projectenergy" in content:
                errors.append("Stale 'projectenergy' reference remains in energy/index.html")

    # 2. energy/vendor/leaflet assets
    leaflet_js = os.path.join(BASE_DIR, "energy", "vendor", "leaflet", "leaflet.js")
    leaflet_css = os.path.join(BASE_DIR, "energy", "vendor", "leaflet", "leaflet.css")
    if not os.path.exists(leaflet_js) or not os.path.exists(leaflet_css):
        errors.append("Leaflet vendor assets missing in energy/vendor/leaflet")

    # 3. projectenergy/index.html redirect
    proj_index = os.path.join(BASE_DIR, "projectenergy", "index.html")
    if not os.path.exists(proj_index):
        errors.append("projectenergy/index.html missing")
    else:
        with open(proj_index, "r", encoding="utf-8") as f:
            c = f.read()
            if "https://energy.renewablevietnam.com" not in c:
                errors.append("Legacy redirect to https://energy.renewablevietnam.com missing in projectenergy/index.html")

    # 4. projectenergy/index_Rev.010.html
    proj_rev10 = os.path.join(BASE_DIR, "projectenergy", "index_Rev.010.html")
    if not os.path.exists(proj_rev10):
        errors.append("projectenergy/index_Rev.010.html revision missing")

    # 5. Cloudflare worker
    worker = os.path.join(BASE_DIR, "cloudflare", "subdomain_gateway_worker.js")
    with open(worker, "r", encoding="utf-8") as f:
        wc = f.read()
        if "'energy.renewablevietnam.com': '/energy'" not in wc:
            errors.append("energy.renewablevietnam.com mapping to /energy missing in subdomain_gateway_worker.js")
        if "pathname.startsWith('/projectenergy')" not in wc:
            errors.append("Legacy /projectenergy redirect handler missing in subdomain_gateway_worker.js")

    # 6. Sitemap.xml
    sitemap = os.path.join(BASE_DIR, "sitemap.xml")
    with open(sitemap, "r", encoding="utf-8") as f:
        sc = f.read()
        if "https://renewablevietnam.com/energy/" not in sc:
            errors.append("https://renewablevietnam.com/energy/ missing from sitemap.xml")
        if "https://energy.renewablevietnam.com/" not in sc:
            errors.append("https://energy.renewablevietnam.com/ missing from sitemap.xml")

    # 7. Navigation template
    nav = os.path.join(BASE_DIR, "_includes", "navigation.html")
    with open(nav, "r", encoding="utf-8") as f:
        nc = f.read()
        if "projectenergy" in nc:
            errors.append("Stale 'projectenergy' reference remains in _includes/navigation.html")

    if errors:
        print(f"[FAIL] {len(errors)} verification checks failed:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("[PASS] All energy migration verification checks passed successfully!")

if __name__ == "__main__":
    test_assertions()
