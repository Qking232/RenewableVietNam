#!/usr/bin/env python3
"""
Automated Migration Script: /projectenergy -> /energy
Executes non-destructive directory migration, legacy redirection,
worker configuration updates, and sitemap synchronization.
"""

import os
import shutil
import re

BASE_DIR = r"G:\My Drive\7. AI\RenewableVietNam"

def step1_create_energy_directory():
    print("--- Step 1: Creating /energy Directory and Copying Assets ---")
    src_dir = os.path.join(BASE_DIR, "projectenergy")
    dst_dir = os.path.join(BASE_DIR, "energy")
    
    os.makedirs(dst_dir, exist_ok=True)
    
    # Copy vendor folder
    src_vendor = os.path.join(src_dir, "vendor")
    dst_vendor = os.path.join(dst_dir, "vendor")
    if os.path.exists(src_vendor):
        if os.path.exists(dst_vendor):
            shutil.rmtree(dst_vendor)
        shutil.copytree(src_vendor, dst_vendor)
        print("Copied vendor directory to energy/vendor.")

    # Read latest projectenergy/index.html
    src_index = os.path.join(src_dir, "index.html")
    with open(src_index, "r", encoding="utf-8") as f:
        content = f.read()

    # Update canonical links, meta tags, and redirect logic
    updated = content
    # Update script redirect
    updated = updated.replace(
        "var targetPath = window.location.pathname.replace(/^\\/projectenergy/, '') || '/';",
        "var targetPath = window.location.pathname.replace(/^\\/energy/, '') || '/';"
    )
    # Update canonical and OpenGraph/Twitter URLs
    updated = updated.replace(
        '<link rel="canonical" href="https://renewablevietnam.com/projectenergy/" />',
        '<link rel="canonical" href="https://energy.renewablevietnam.com/" />'
    )
    updated = updated.replace(
        '<meta property="og:url" content="https://renewablevietnam.com/projectenergy/" />',
        '<meta property="og:url" content="https://energy.renewablevietnam.com/" />'
    )
    updated = updated.replace(
        '<meta name="twitter:url" content="https://renewablevietnam.com/projectenergy/" />',
        '<meta name="twitter:url" content="https://energy.renewablevietnam.com/" />'
    )
    updated = updated.replace(
        '"url": "https://renewablevietnam.com/projectenergy/"',
        '"url": "https://energy.renewablevietnam.com/"'
    )

    # Write energy/index_Rev.001.html and energy/index.html
    dst_rev1 = os.path.join(dst_dir, "index_Rev.001.html")
    dst_index = os.path.join(dst_dir, "index.html")
    with open(dst_rev1, "w", encoding="utf-8") as f:
        f.write(updated)
    with open(dst_index, "w", encoding="utf-8") as f:
        f.write(updated)
    print("Created energy/index_Rev.001.html and energy/index.html.")

def step2_redirect_legacy_projectenergy():
    print("--- Step 2: Creating Legacy Redirect in projectenergy/index.html ---")
    src_dir = os.path.join(BASE_DIR, "projectenergy")
    src_index = os.path.join(src_dir, "index.html")
    
    # Save revision index_Rev.010.html
    rev10_path = os.path.join(src_dir, "index_Rev.010.html")
    if not os.path.exists(rev10_path):
        shutil.copy2(src_index, rev10_path)
        print("Archived current projectenergy/index.html to index_Rev.010.html.")

    redirect_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Redirecting to Energy Portal...</title>
  <link rel="canonical" href="https://energy.renewablevietnam.com/">
  <meta http-equiv="refresh" content="0; url=https://energy.renewablevietnam.com/">
  <script>
    var targetPath = window.location.pathname.replace(/^\\/projectenergy/, '') || '/';
    window.location.replace('https://energy.renewablevietnam.com' + targetPath + window.location.search + window.location.hash);
  </script>
</head>
<body style="font-family: sans-serif; padding: 2rem; background: #070A12; color: #F1F5F9; text-align: center;">
  <p>Redirecting to Vietnam Clean Energy Asset Registry at <a href="https://energy.renewablevietnam.com/" style="color: #38BDF8;">energy.renewablevietnam.com</a>...</p>
</body>
</html>
"""
    with open(src_index, "w", encoding="utf-8") as f:
        f.write(redirect_html)
    print("Updated projectenergy/index.html with canonical redirect.")

def step3_update_cloudflare_gateway():
    print("--- Step 3: Updating Cloudflare Subdomain Gateway Worker ---")
    cf_dir = os.path.join(BASE_DIR, "cloudflare")
    worker_path = os.path.join(cf_dir, "subdomain_gateway_worker.js")
    rev7_path = os.path.join(cf_dir, "subdomain_gateway_worker_Rev.007.js")
    
    # Read current worker
    with open(worker_path, "r", encoding="utf-8") as f:
        worker_code = f.read()

    # Save revision Rev.007
    with open(rev7_path, "w", encoding="utf-8") as f:
        f.write(worker_code)
    print("Saved current worker to subdomain_gateway_worker_Rev.007.js.")

    # Update HOST_PATH_MAP
    updated_worker = worker_code.replace(
        "'energy.renewablevietnam.com': '/projectenergy',",
        "'energy.renewablevietnam.com': '/energy',"
    ).replace(
        "'wind.renewablevietnam.com': '/projectenergy',",
        "'wind.renewablevietnam.com': '/energy',"
    )

    # Add legacy redirect for /projectenergy if not present
    if "pathname.startsWith('/projectenergy')" not in updated_worker:
        inject_marker = "if (pathname.startsWith('/green')) {"
        legacy_redirect_snippet = """    // Edge HTTP 301 Permanent Redirect: /projectenergy -> /energy
    if (pathname.startsWith('/projectenergy')) {
      const remainingPath = pathname.replace(/^\\/projectenergy/, '') || '/';
      return Response.redirect(`https://energy.renewablevietnam.com${remainingPath}${url.search}`, 301);
    }

"""
        updated_worker = updated_worker.replace(inject_marker, legacy_redirect_snippet + "    " + inject_marker)

    with open(worker_path, "w", encoding="utf-8") as f:
        f.write(updated_worker)
    print("Updated subdomain_gateway_worker.js with /energy mapping and legacy 301 redirect.")

def step4_update_sitemap_and_nav():
    print("--- Step 4: Updating Sitemap and Navigation Template ---")
    # Sitemap
    sitemap_path = os.path.join(BASE_DIR, "sitemap.xml")
    sitemap_rev4 = os.path.join(BASE_DIR, "sitemap_Rev.004.xml")
    with open(sitemap_path, "r", encoding="utf-8") as f:
        sitemap_content = f.read()

    if not os.path.exists(sitemap_rev4):
        with open(sitemap_rev4, "w", encoding="utf-8") as f:
            f.write(sitemap_content)
        print("Saved current sitemap to sitemap_Rev.004.xml.")

    sitemap_updated = sitemap_content.replace(
        "<loc>https://renewablevietnam.com/projectenergy/</loc>",
        "<loc>https://renewablevietnam.com/energy/</loc>\n    <lastmod>2026-11-03</lastmod>\n    <changefreq>daily</changefreq>\n    <priority>0.95</priority>\n  </url>\n  <url>\n    <loc>https://energy.renewablevietnam.com/</loc>"
    )
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(sitemap_updated)
    print("Updated sitemap.xml.")

    # Navigation template
    nav_path = os.path.join(BASE_DIR, "_includes", "navigation.html")
    nav_rev1 = os.path.join(BASE_DIR, "_includes", "navigation_Rev.001.html")
    if os.path.exists(nav_path):
        with open(nav_path, "r", encoding="utf-8") as f:
            nav_content = f.read()
        if not os.path.exists(nav_rev1):
            with open(nav_rev1, "w", encoding="utf-8") as f:
                f.write(nav_content)
            print("Saved navigation.html to navigation_Rev.001.html.")
        nav_updated = nav_content.replace("projectenergy/", "energy/")
        with open(nav_path, "w", encoding="utf-8") as f:
            f.write(nav_updated)
        print("Updated _includes/navigation.html.")

if __name__ == "__main__":
    step1_create_energy_directory()
    step2_redirect_legacy_projectenergy()
    step3_update_cloudflare_gateway()
    step4_update_sitemap_and_nav()
    print("--- Migration Completed Successfully ---")
