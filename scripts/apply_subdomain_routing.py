import os

def update_invm_index():
    invm_path = os.path.join(r"G:\My Drive\7. AI\RenewableVietNam\invm", "index.html")
    rev_path = os.path.join(r"G:\My Drive\7. AI\RenewableVietNam\invm", "index_Rev.017.html")
    
    with open(invm_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Update header comment
    content_mod = content.replace(
        "<!-- Vietnam Investment Project Legal Management & M&A Engine Rev 0.16 -->",
        "<!-- Vietnam Investment Project Legal Management & M&A Engine Rev 0.17 - Subdomain Canonical invest.renewablevietnam.com -->"
    )

    # Insert canonical & transition script into head
    canonical_tag = """  <link rel="canonical" href="https://invest.renewablevietnam.com/">
  <script>
    // Canonical Transition: Route renewablevietnam.com/invm traffic to invest.renewablevietnam.com
    (function() {
      if (window.location.hostname === 'renewablevietnam.com') {
        var subpath = window.location.pathname.replace(/^\\/invm\\/?/, '/');
        window.location.replace('https://invest.renewablevietnam.com' + subpath + window.location.search + window.location.hash);
      }
    })();
  </script>
"""

    target_head = '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, viewport-fit=cover">\n'
    if target_head in content_mod:
        content_mod = content_mod.replace(target_head, target_head + canonical_tag, 1)
    else:
        content_mod = content_mod.replace("<head>", "<head>\n" + canonical_tag, 1)

    # Update relative navigation link for quyhoach
    content_mod = content_mod.replace('href="/invm/quyhoach"', 'href="./quyhoach/"')

    with open(rev_path, "w", encoding="utf-8") as f:
        f.write(content_mod)

    with open(invm_path, "w", encoding="utf-8") as f:
        f.write(content_mod)

    print("invm index updated successfully.")

def update_quyhoach_index():
    qh_path = os.path.join(r"G:\My Drive\7. AI\RenewableVietNam\invm\quyhoach", "index.html")
    rev_path = os.path.join(r"G:\My Drive\7. AI\RenewableVietNam\invm\quyhoach", "index_Rev.001.html")

    with open(qh_path, "r", encoding="utf-8") as f:
        content = f.read()

    canonical_tag = """  <link rel="canonical" href="https://invest.renewablevietnam.com/quyhoach/">
  <script>
    // Canonical Transition: Route renewablevietnam.com/invm/quyhoach to invest.renewablevietnam.com/quyhoach
    (function() {
      if (window.location.hostname === 'renewablevietnam.com') {
        var subpath = window.location.pathname.replace(/^\\/invm\\/?/, '/');
        window.location.replace('https://invest.renewablevietnam.com' + subpath + window.location.search + window.location.hash);
      }
    })();
  </script>
"""

    target_head = '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, viewport-fit=cover">\n'
    if target_head in content:
        content_mod = content.replace(target_head, target_head + canonical_tag, 1)
    else:
        content_mod = content.replace("<head>", "<head>\n" + canonical_tag, 1)

    # Update back button
    content_mod = content_mod.replace(
        'href="/invm"',
        'href="../"'
    )
    content_mod = content_mod.replace(
        'title="Về Quản Lý Dự Án (/invm)"',
        'title="Về Quản Lý Đầu Tư"'
    )
    content_mod = content_mod.replace(
        '<span class="hidden md:inline">Về /invm</span>',
        '<span class="hidden md:inline">Về Đầu Tư</span>'
    )

    with open(rev_path, "w", encoding="utf-8") as f:
        f.write(content_mod)

    with open(qh_path, "w", encoding="utf-8") as f:
        f.write(content_mod)

    print("quyhoach index updated successfully.")

if __name__ == "__main__":
    update_invm_index()
    update_quyhoach_index()
