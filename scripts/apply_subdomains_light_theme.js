const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const baseDir = path.resolve('G:/My Drive/7. AI/RenewableVietNam');

// ============================================================================
// 1. REFACTOR green/index.html (ind.renewablevietnam.com)
// ============================================================================
function updateGreen() {
  const file = path.join(baseDir, 'green', 'index.html');
  const revFile = path.join(baseDir, 'green', 'index_Rev.002.html');
  let content = fs.readFileSync(file, 'utf8');

  // Replace anti-FOUC script
  const oldScript = `  <script>
    const savedTheme = localStorage.getItem('rvn-theme');
    if (savedTheme === 'light') {
      document.documentElement.classList.remove('dark');
    } else {
      document.documentElement.classList.add('dark');
      if (!savedTheme) localStorage.setItem('rvn-theme', 'dark');
    }
  </script>`;

  const newScript = `  <script>
    (function () {
      try {
        var savedTheme = localStorage.getItem('rvn_theme_v2');
        if (savedTheme === 'dark') {
          document.documentElement.classList.add('dark');
        } else {
          document.documentElement.classList.remove('dark');
        }
      } catch (e) {}
    })();
  </script>`;

  if (content.includes(oldScript)) {
    content = content.replace(oldScript, newScript);
  } else {
    console.warn('Warning: oldScript pattern in green/index.html did not match exactly, applying regex replace');
    content = content.replace(/<script>\s*const savedTheme = localStorage\.getItem\('rvn-theme'\);[\s\S]*?<\/script>/, newScript);
  }

  // Replace toggle persistence key
  content = content.replace(
    "localStorage.setItem('rvn-theme', isDark ? 'dark' : 'light');",
    "localStorage.setItem('rvn_theme_v2', isDark ? 'dark' : 'light');"
  );

  fs.writeFileSync(revFile, content, 'utf8');
  fs.writeFileSync(file, content, 'utf8');
  console.log('[SUCCESS] green/index.html updated & index_Rev.002.html created');
}

// ============================================================================
// 2. REFACTOR evcharging/index.html (ev.renewablevietnam.com)
// ============================================================================
function updateEvCharging() {
  const file = path.join(baseDir, 'evcharging', 'index.html');
  const revFile = path.join(baseDir, 'evcharging', 'index_Rev.002.html');
  let content = fs.readFileSync(file, 'utf8');

  // Remove static 'dark' class
  content = content.replace('<html lang="en" class="dark">', '<html lang="en">');

  // Replace anti-FOUC script
  const oldScript = `  <script>
    const savedTheme = localStorage.getItem('rvn-theme');
    if (savedTheme === 'light') {
      document.documentElement.classList.remove('dark');
    } else {
      document.documentElement.classList.add('dark');
      if (!savedTheme) localStorage.setItem('rvn-theme', 'dark');
    }
  </script>`;

  const newScript = `  <script>
    (function () {
      try {
        var savedTheme = localStorage.getItem('rvn_theme_v2');
        if (savedTheme === 'dark') {
          document.documentElement.classList.add('dark');
        } else {
          document.documentElement.classList.remove('dark');
        }
      } catch (e) {}
    })();
  </script>`;

  if (content.includes(oldScript)) {
    content = content.replace(oldScript, newScript);
  } else {
    console.warn('Warning: oldScript in evcharging/index.html regex replacing');
    content = content.replace(/<script>\s*const savedTheme = localStorage\.getItem\('rvn-theme'\);[\s\S]*?<\/script>/, newScript);
  }

  // Replace toggle persistence key
  content = content.replace(
    'localStorage.setItem("rvn-theme", isDark ? "dark" : "light");',
    'localStorage.setItem("rvn_theme_v2", isDark ? "dark" : "light");'
  );

  fs.writeFileSync(revFile, content, 'utf8');
  fs.writeFileSync(file, content, 'utf8');
  console.log('[SUCCESS] evcharging/index.html updated & index_Rev.002.html created');
}

// ============================================================================
// 3. REFACTOR projectenergy/index.html (energy.renewablevietnam.com)
// ============================================================================
function updateProjectEnergy() {
  const file = path.join(baseDir, 'projectenergy', 'index.html');
  const revFile = path.join(baseDir, 'projectenergy', 'index_Rev.002.html');
  let content = fs.readFileSync(file, 'utf8');

  // Remove static 'dark' class
  content = content.replace('<html lang="en" class="dark">', '<html lang="en">');

  // Replace anti-FOUC script
  const oldScript = `  <script>
    const savedTheme = localStorage.getItem('rvn-theme');
    if (savedTheme === 'light') {
      document.documentElement.classList.remove('dark');
    } else {
      document.documentElement.classList.add('dark');
      if (!savedTheme) localStorage.setItem('rvn-theme', 'dark');
    }
  </script>`;

  const newScript = `  <script>
    (function () {
      try {
        var savedTheme = localStorage.getItem('rvn_theme_v2');
        if (savedTheme === 'dark') {
          document.documentElement.classList.add('dark');
        } else {
          document.documentElement.classList.remove('dark');
        }
      } catch (e) {}
    })();
  </script>`;

  if (content.includes(oldScript)) {
    content = content.replace(oldScript, newScript);
  } else {
    console.warn('Warning: oldScript in projectenergy/index.html regex replacing');
    content = content.replace(/<script>\s*const savedTheme = localStorage\.getItem\('rvn-theme'\);[\s\S]*?<\/script>/, newScript);
  }

  // Replace toggle persistence key
  content = content.replace(
    'localStorage.setItem("rvn-theme", isDark ? "dark" : "light");',
    'localStorage.setItem("rvn_theme_v2", isDark ? "dark" : "light");'
  );

  fs.writeFileSync(revFile, content, 'utf8');
  fs.writeFileSync(file, content, 'utf8');
  console.log('[SUCCESS] projectenergy/index.html updated & index_Rev.002.html created');
}

// ============================================================================
// 4. DECRYPT, UPDATE & RE-ENCRYPT hub/index.html (legal.renewablevietnam.com)
// ============================================================================
function updateHub() {
  const file = path.join(baseDir, 'hub', 'index.html');
  const revFile = path.join(baseDir, 'hub', 'index_Rev.002.html');
  const content = fs.readFileSync(file, 'utf8');

  // Extract payload P
  const pMatch = content.match(/const P = ({[\s\S]*?});/);
  if (!pMatch) throw new Error('Payload P not found in hub/index.html');
  const P = JSON.parse(pMatch[1]);

  // Decrypt payload
  const sA = Buffer.from(P.sA, 'hex');
  const sB = Buffer.from(P.sB, 'hex');
  const rawKey = Buffer.alloc(32);
  for (let i = 0; i < 32; i++) rawKey[i] = sA[i] ^ sB[i];

  const decipher = crypto.createDecipheriv('aes-256-gcm', rawKey, Buffer.from(P.iv, 'hex'));
  decipher.setAuthTag(Buffer.from(P.tag, 'hex'));
  let dec = decipher.update(Buffer.from(P.data, 'hex'), null, 'utf8') + decipher.final('utf8');

  // Update inner decrypted application HTML:
  // 1) Replace root html tag data-theme
  dec = dec.replace('<html lang="en" data-theme="dark">', '<html lang="en" data-theme="light">');

  // 2) Replace inner anti-FOUC theme logic
  const oldInnerTheme = `    (function () {
      var t = null;
      try { t = localStorage.getItem('theme'); } catch (e) {}
      if (t !== 'dark' && t !== 'light') t = 'dark';
      document.documentElement.setAttribute('data-theme', t);
      if (t === 'dark') {
        document.documentElement.classList.add('dark');
      } else {
        document.documentElement.classList.remove('dark');
      }
    })();`;

  const newInnerTheme = `    (function () {
      var t = null;
      try { t = localStorage.getItem('rvn_theme_v2'); } catch (e) {}
      if (t !== 'dark' && t !== 'light') t = 'light';
      document.documentElement.setAttribute('data-theme', t);
      if (t === 'dark') {
        document.documentElement.classList.add('dark');
      } else {
        document.documentElement.classList.remove('dark');
      }
    })();`;

  if (dec.includes(oldInnerTheme)) {
    dec = dec.replace(oldInnerTheme, newInnerTheme);
  } else {
    console.warn('Warning: inner theme snippet in hub decrypted payload did not match exactly, using flexible replace');
    dec = dec.replace(/try\s*\{\s*t\s*=\s*localStorage\.getItem\('theme'\);[\s\S]*?if\s*\(t\s*!==\s*'dark'[\s\S]*?t\s*=\s*'dark';/,
      "try { t = localStorage.getItem('rvn_theme_v2'); } catch (e) {}\n      if (t !== 'dark' && t !== 'light') t = 'light';");
  }

  // 3) Replace inner toggle function storage key
  dec = dec.replace('try { localStorage.setItem("theme", next); } catch (e) {}',
                    'try { localStorage.setItem("rvn_theme_v2", next); } catch (e) {}');

  // Re-encrypt inner decrypted payload
  const newKey = crypto.randomBytes(32);
  const newIv = crypto.randomBytes(12);
  const cipher = crypto.createCipheriv('aes-256-gcm', newKey, newIv);
  let newCiphertext = cipher.update(dec, 'utf8', 'hex');
  newCiphertext += cipher.final('hex');
  const newAuthTag = cipher.getAuthTag();

  const newShardA = crypto.randomBytes(32);
  const newShardB = Buffer.alloc(32);
  for (let i = 0; i < 32; i++) newShardB[i] = newKey[i] ^ newShardA[i];

  const newP = {
    iv: newIv.toString('hex'),
    tag: newAuthTag.toString('hex'),
    sA: newShardA.toString('hex'),
    sB: newShardB.toString('hex'),
    data: newCiphertext
  };

  // Update outer distribution wrapper
  let newOuter = content;
  newOuter = newOuter.replace('<html lang="en" data-theme="dark">', '<html lang="en" data-theme="light">');
  newOuter = newOuter.replace(/--bg:\s*#000000;/, '--bg: #F8FAFC;');
  newOuter = newOuter.replace(/color:\s*#ffffff;/, 'color: #0F172A;');
  newOuter = newOuter.replace(/color:\s*rgba\(255,\s*255,\s*255,\s*0\.4\);/, 'color: rgba(15, 23, 42, 0.4);');
  newOuter = newOuter.replace(/const P = ({[\s\S]*?});/, `const P = ${JSON.stringify(newP)};`);

  fs.writeFileSync(revFile, newOuter, 'utf8');
  fs.writeFileSync(file, newOuter, 'utf8');
  console.log('[SUCCESS] hub/index.html re-encrypted & index_Rev.002.html created');

  // Also sync Qking232.github.io/hub/index.html if directory exists
  const dest2Dir = path.resolve(baseDir, '..', 'Qking232.github.io', 'hub');
  if (fs.existsSync(dest2Dir)) {
    fs.writeFileSync(path.join(dest2Dir, 'index.html'), newOuter, 'utf8');
    console.log('[SUCCESS] Synchronized copy to Qking232.github.io/hub/index.html');
  }
}

// Execute all
console.log('--- Applying Light Theme as Default across 4 Subdomains ---');
updateGreen();
updateEvCharging();
updateProjectEnergy();
updateHub();
console.log('--- All subdomains refactored successfully ---');
