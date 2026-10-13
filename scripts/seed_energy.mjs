#!/usr/bin/env node
/*
 * Seed public.energy_projects from the project list embedded in
 * projectenergy/index.html.
 *
 * USAGE (run locally, never in CI):
 *
 *   $env:SUPABASE_SECRET_KEY = "sb_secret_..."      # PowerShell
 *   node scripts/seed_energy.mjs --dry-run          # show what would change
 *   node scripts/seed_energy.mjs                    # apply
 *
 * The secret key is read from the environment and is NEVER written to a file,
 * printed, or committed. It is required because the public page has no write
 * policy — by design — so seeding must use a key that bypasses RLS.
 *
 * Requires Node 18+ (global fetch).
 */

import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dirname, '..');

const SUPABASE_URL = process.env.SUPABASE_URL || 'https://nkkwegvplpozirrjcxsn.supabase.co';
const KEY = process.env.SUPABASE_SECRET_KEY;
const DRY = process.argv.includes('--dry-run');
const TABLE = 'energy_projects';

if (!KEY) {
  console.error('SUPABASE_SECRET_KEY is not set.');
  console.error('PowerShell:  $env:SUPABASE_SECRET_KEY = "sb_secret_..."');
  console.error('bash:        export SUPABASE_SECRET_KEY="sb_secret_..."');
  process.exit(1);
}
if (!/^sb_secret_/.test(KEY)) {
  console.error('Refusing to run: SUPABASE_SECRET_KEY does not look like a secret key.');
  console.error('The publishable key cannot seed (RLS blocks writes) — use the secret key.');
  process.exit(1);
}

// ---------------------------------------------------------------- extract
const html = readFileSync(join(ROOT, 'projectenergy', 'index.html'), 'utf8');
const start = html.indexOf('var PROJECTS_DB = [');
const end = html.indexOf('\n    ];', start);
if (start < 0 || end < 0) {
  console.error('Could not locate PROJECTS_DB in projectenergy/index.html');
  process.exit(1);
}
const literal = html.slice(start + 'var PROJECTS_DB = '.length, end + '\n    ]'.length);
const rows = eval(literal);           // the literal is plain data, no calls
console.log(`parsed ${rows.length} rows from index.html`);

const byType = rows.reduce((a, p) => ((a[p.type] = (a[p.type] || 0) + 1), a), {});
console.log('by type:', byType);

function sourceOf(note) {
  if (!note) return null;
  const m = note.match(/source:\s*([^·]+)/);
  return m ? m[1].trim() : null;
}

const payload = rows.map((p) => ({
  name: p.name,
  company: p.company || 'Not stated',
  country: p.country || 'Viet Nam',
  type: p.type,
  cap: p.cap || 'Not stated',
  loc: p.loc || null,
  lat: Number(p.lat),
  lon: Number(p.lon),
  note: p.note || null,
  source: sourceOf(p.note),
}));

const bad = payload.filter(
  (p) => !p.name || !p.type || !Number.isFinite(p.lat) || !Number.isFinite(p.lon)
);
if (bad.length) {
  console.error(`${bad.length} malformed rows, aborting:`, bad.slice(0, 5));
  process.exit(1);
}

if (DRY) {
  console.log(`\n--dry-run: would upsert ${payload.length} rows into ${TABLE}`);
  console.log('sample:', JSON.stringify(payload[0], null, 1));
  process.exit(0);
}

// ----------------------------------------------------------------- upsert
const BATCH = 200;
let done = 0;
for (let i = 0; i < payload.length; i += BATCH) {
  const batch = payload.slice(i, i + BATCH);
  const res = await fetch(`${SUPABASE_URL}/rest/v1/${TABLE}?on_conflict=type,name`, {
    method: 'POST',
    headers: {
      apikey: KEY,
      Authorization: `Bearer ${KEY}`,
      'Content-Type': 'application/json',
      // merge duplicate (type,name) pairs instead of failing
      Prefer: 'resolution=merge-duplicates,return=minimal',
    },
    body: JSON.stringify(batch),
  });
  if (!res.ok) {
    console.error(`batch ${i / BATCH + 1} failed: ${res.status} ${res.statusText}`);
    console.error((await res.text()).slice(0, 800));
    process.exit(1);
  }
  done += batch.length;
  process.stdout.write(`\r  upserted ${done}/${payload.length}`);
}
console.log('\ndone.');
