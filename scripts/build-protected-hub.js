const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const srcPath = path.resolve(__dirname, '..', '_src', 'hub_source_v0.63.html');
if (!fs.existsSync(srcPath)) {
  console.error('Source file not found at:', srcPath);
  process.exit(1);
}

const rawHtml = fs.readFileSync(srcPath, 'utf8');

// 1. Generate AES-256-GCM key and IV
const key = crypto.randomBytes(32);
const iv = crypto.randomBytes(12);

// 2. Encrypt application payload
const cipher = crypto.createCipheriv('aes-256-gcm', key, iv);
let ciphertext = cipher.update(rawHtml, 'utf8', 'hex');
ciphertext += cipher.final('hex');
const authTag = cipher.getAuthTag();

// 3. Shard the key into two XOR polymorphic masks (A ^ B = key)
const shardA = crypto.randomBytes(32);
const shardB = Buffer.alloc(32);
for (let i = 0; i < 32; i++) {
  shardB[i] = key[i] ^ shardA[i];
}

const payload = {
  iv: iv.toString('hex'),
  tag: authTag.toString('hex'),
  sA: shardA.toString('hex'),
  sB: shardB.toString('hex'),
  data: ciphertext
};

// 4. Extract SEO metadata from source cleanly (including full JSON-LD schema)
let seoHead = '';
const titleMatch = rawHtml.match(/<title>[\s\S]*?<\/title>/i);
const metaMatches = rawHtml.match(/<meta[^>]*>/gi) || [];
const canonicalMatch = rawHtml.match(/<link\s+rel="canonical"[^>]*>/i);
const iconMatch = rawHtml.match(/<link\s+rel="icon"[^>]*>/i);
const jsonLdMatch = rawHtml.match(/<script\s+type="application\/ld\+json">[\s\S]*?<\/script>/i);

const headParts = [];
if (titleMatch) headParts.push(titleMatch[0]);
headParts.push(...metaMatches);
if (canonicalMatch) headParts.push(canonicalMatch[0]);
if (iconMatch) headParts.push(iconMatch[0]);
if (jsonLdMatch) headParts.push(jsonLdMatch[0]);

seoHead = headParts.join('\n');

// 5. Generate production gatekeeper wrapper (non-blocking, instant in-memory mount)
const productionHtml = `<!DOCTYPE html>
<!--
  Renewable Viet Nam — The Library
  Protected Production Distribution · Rev 0.63
  Authenticated AES-256-GCM in-memory unpacking.
-->
<html lang="en" data-theme="dark">
<head>
<meta charset="utf-8" />
${seoHead}
<style>
  :root {
    --bg: #000000;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    background: var(--bg);
    color: #ffffff;
    font-family: "Slate Pro", "Slate", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    margin: 0;
  }
  #loader {
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    font-size: 12px;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: rgba(255, 255, 255, 0.4);
    font-weight: 600;
  }
</style>
</head>
<body>
<header style="position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0;">
  <h1>Vietnam Clean Energy Transition Statutory Library & Legal Directives</h1>
  <p>Shared repository of Decree 80/2024 DPPA, PDP8 implementation plans, MOIT circulars, and power sector legal directives.</p>
</header>
<div id="loader">Loading The Library&hellip;</div>

<script>
(async function() {
  const P = ${JSON.stringify(payload)};

  function h2b(hex) {
    const bytes = new Uint8Array(hex.length / 2);
    for (let i = 0; i < hex.length; i += 2) {
      bytes[i / 2] = parseInt(hex.substr(i, 2), 16);
    }
    return bytes;
  }

  try {
    const sA = h2b(P.sA);
    const sB = h2b(P.sB);
    const rawKey = new Uint8Array(32);
    for (let i = 0; i < 32; i++) {
      rawKey[i] = sA[i] ^ sB[i];
    }

    const iv = h2b(P.iv);
    const tag = h2b(P.tag);
    const ct = h2b(P.data);

    // Merge ciphertext + 128-bit authentication tag for WebCrypto
    const combined = new Uint8Array(ct.length + tag.length);
    combined.set(ct, 0);
    combined.set(tag, ct.length);

    // Import key & decrypt in RAM
    const cryptoKey = await window.crypto.subtle.importKey(
      'raw',
      rawKey,
      'AES-GCM',
      false,
      ['decrypt']
    );

    const decrypted = await window.crypto.subtle.decrypt(
      { name: 'AES-GCM', iv: iv, tagLength: 128 },
      cryptoKey,
      combined
    );

    const appHtml = new TextDecoder('utf-8').decode(decrypted);

    // Explicitly remove placeholder loader before mounting
    const loaderEl = document.getElementById('loader');
    if (loaderEl) loaderEl.remove();

    // Mount application into DOM
    document.open();
    document.write(appHtml);
    document.close();
  } catch (err) {
    console.error('Failed to unpack protected application:', err);
    const loaderEl = document.getElementById('loader');
    if (loaderEl) {
      loaderEl.innerHTML = '<span style="color:#f87171;">Unable to load library. Please refresh.</span>';
    }
  }
})();
</script>
</body>
</html>`;

// 6. Write to destination 1: C:\Gemini\RenewableVietNam\hub\index.html
const dest1 = path.resolve(__dirname, '..', 'hub', 'index.html');
fs.writeFileSync(dest1, productionHtml, 'utf8');
console.log('✓ Successfully compiled to:', dest1);

// 7. Write to destination 2: G:\My Drive\7. AI\Gemini\Qking232.github.io\hub\index.html
const dest2Dir = path.resolve(__dirname, '..', '..', 'Qking232.github.io', 'hub');
if (!fs.existsSync(dest2Dir)) {
  fs.mkdirSync(dest2Dir, { recursive: true });
}
const dest2 = path.join(dest2Dir, 'index.html');
fs.writeFileSync(dest2, productionHtml, 'utf8');
console.log('✓ Successfully deployed copy to:', dest2);

console.log('Protected payload size: ' + Math.round(ciphertext.length / 1024) + ' KB encrypted hex.');
