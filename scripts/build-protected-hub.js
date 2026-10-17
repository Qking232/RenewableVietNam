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

// 4. Extract SEO head content from source to preserve search indexing
const headMatch = rawHtml.match(/<head[^>]*>([\s\S]*?)<\/head>/i);
let seoHead = '';
if (headMatch && headMatch[1]) {
  const lines = headMatch[1].split('\n');
  const preservedLines = lines.filter(line => {
    const trimmed = line.trim();
    return (
      trimmed.startsWith('<meta') ||
      trimmed.startsWith('<title') ||
      trimmed.startsWith('<link rel="canonical"') ||
      trimmed.startsWith('<link rel="icon"') ||
      trimmed.startsWith('<script type="application/ld+json"') ||
      trimmed.includes('"@context"') ||
      trimmed.includes('"@type"') ||
      trimmed.includes('"Vietnam renewable energy"') ||
      trimmed.startsWith('</script>')
    );
  });
  seoHead = preservedLines.join('\n');
}

// 5. Generate production gatekeeper wrapper
const productionHtml = `<!DOCTYPE html>
<!--
  Renewable Viet Nam — The Library
  Protected Production Distribution · Rev 0.63
  Authenticated AES-256-GCM in-memory unpacking.
-->
<html lang="en" data-theme="dark">
<head>
${seoHead}
<style>
  :root {
    --bg: #000000;
    --accent: #0092CC;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    background: var(--bg);
    color: #ffffff;
    font-family: "Slate Pro", "Slate", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    min-height: 100vh;
    overflow: hidden;
  }
  .app-loader {
    position: fixed;
    inset: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 16px;
    background: #000000;
    z-index: 9999;
    transition: opacity 0.25s ease;
  }
  .top-accent {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(90deg, #0072BC, #00A0E0 55%, #3FC0F5);
  }
  .loader-spinner {
    width: 28px;
    height: 28px;
    border: 2px solid rgba(255, 255, 255, 0.12);
    border-top-color: var(--accent);
    border-radius: 50%;
    animation: spin 0.8s linear infinite;
  }
  .loader-text {
    font-size: 11px;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: rgba(255, 255, 255, 0.45);
    font-weight: 600;
  }
  @keyframes spin {
    to { transform: rotate(360deg); }
  }
</style>
</head>
<body>
<div class="top-accent"></div>
<div class="app-loader" id="loader">
  <div class="loader-spinner"></div>
  <div class="loader-text">Loading The Library&hellip;</div>
</div>

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

    // Mount application into DOM
    document.open();
    document.write(appHtml);
    document.close();
  } catch (err) {
    console.error('Failed to unpack protected application:', err);
    const loader = document.getElementById('loader');
    if (loader) {
      loader.innerHTML = '<div style="color:#f87171;font-size:13px;letter-spacing:0.04em;">Unable to load library. Please refresh or verify network access.</div>';
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

// 7. Write to destination 2: C:\Gemini\Qking232.github.io\hub\index.html
const dest2Dir = path.resolve('C:\\Gemini\\Qking232.github.io\\hub');
if (!fs.existsSync(dest2Dir)) {
  fs.mkdirSync(dest2Dir, { recursive: true });
}
const dest2 = path.join(dest2Dir, 'index.html');
fs.writeFileSync(dest2, productionHtml, 'utf8');
console.log('✓ Successfully deployed copy to:', dest2);

console.log('Protected payload size: ' + Math.round(ciphertext.length / 1024) + ' KB encrypted hex.');
