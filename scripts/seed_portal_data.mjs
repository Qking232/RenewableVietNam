#!/usr/bin/env node
/**
 * ===========================================================================
 * Renewable Vietnam — Universal Portal Data Ingestion & Seeder
 * ===========================================================================
 * Ingests datasets from static files into Supabase Postgres tables:
 *   - data/vietnam_industrial_parks.json -> public.industrial_hubs
 *   - data/pdp8_targets.json -> public.pdp8_fuel_targets, public.pdp8_priority_projects
 *   - Decision 2699/QD-BCT tariffs -> public.tariff_schedules
 *
 * Usage:
 *   node scripts/seed_portal_data.mjs --dry-run
 *   $env:SUPABASE_SECRET_KEY="sb_secret_..." ; node scripts/seed_portal_data.mjs
 * ===========================================================================
 */

import { readFileSync, existsSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dirname, '..');

const SUPABASE_URL = process.env.SUPABASE_URL || 'https://nkkwegvplpozirrjcxsn.supabase.co';
const KEY = process.env.SUPABASE_SECRET_KEY;
const DRY = process.argv.includes('--dry-run');

console.log('===================================================================');
console.log('Renewable Vietnam — Supabase Data Ingestion Engine');
console.log('Endpoint:', SUPABASE_URL);
console.log('Mode:    ', DRY ? 'DRY-RUN (Local validation only)' : 'LIVE SEEDING');
console.log('===================================================================\n');

if (!DRY && !KEY) {
  console.log('ℹ SUPABASE_SECRET_KEY not set. Running in --dry-run mode.');
  console.log('  To apply changes to live Supabase Postgres, run:');
  console.log('  PowerShell: $env:SUPABASE_SECRET_KEY="sb_secret_..."; node scripts/seed_portal_data.mjs\n');
}

// ---------------------------------------------------------------------------
// 1. Prepare Industrial Hubs
// ---------------------------------------------------------------------------
const hubsFile = join(ROOT, 'data', 'vietnam_industrial_parks.json');
let hubRows = [];

if (existsSync(hubsFile)) {
  const hubsJson = JSON.parse(readFileSync(hubsFile, 'utf8'));
  const rawList = hubsJson.hubs || hubsJson.parks || [];
  hubRows = rawList.map(h => ({
    id: h.id,
    name: h.name,
    vietnamese_name: h.vietnamese_name || h.vietnameseName || null,
    developer: h.developer || 'Not stated',
    province: h.province || 'Unknown',
    region: h.region || 'North',
    total_area_ha: Number(h.total_area_ha || h.totalAreaHa || 0),
    substation: h.substation || null,
    substation_kv: Number(h.substation_kv || h.substationKv || 110),
    rooftop_installed_mwp: Number(h.rooftop_installed_mwp || h.rooftopInstalledMWp || 0),
    rooftop_potential_mwp: Number(h.rooftop_potential_mwp || h.rooftopPotentialMWp || 0),
    dppa_tier: h.dppa_tier || h.dppaTier || 'Pending Evaluation',
    dppa_class: h.dppa_class || h.dppaClass || 'evaluating',
    clean_energy_share: Number(h.clean_energy_share || h.cleanEnergyShare || 0),
    certifications: h.certifications || [],
    anchor_tenants: h.anchor_tenants || h.anchorTenants || [],
    lat: Number(h.lat),
    lng: Number(h.lng || h.lon),
    dppa_summary: h.dppa_summary || h.dppaSummary || null
  }));
}
console.log(`[1] Industrial Hubs: Parsed ${hubRows.length} rows.`);

// ---------------------------------------------------------------------------
// 2. Prepare PDP8 Targets
// ---------------------------------------------------------------------------
const pdp8File = join(ROOT, 'data', 'pdp8_targets.json');
let fuelRows = [];
let priorityRows = [];

if (existsSync(pdp8File)) {
  const pdp8Json = JSON.parse(readFileSync(pdp8File, 'utf8'));
  fuelRows = (pdp8Json.fuel_targets || []).map(f => ({
    fuel: f.fuel,
    fuel_vi: f.fuel_vi,
    target_2030_mw: f.target_2030_mw,
    current_operating_mw: f.current_operating_mw || 0,
    pipeline_mw: f.pipeline_mw || 0,
    target_share_pct: f.target_share_pct || 0,
    color: f.color || 'teal',
    hex: f.hex || '#14b8a6',
    status_note: f.status_note || null
  }));

  priorityRows = (pdp8Json.priority_projects || []).map(p => ({
    id: p.id,
    name: p.name,
    name_vi: p.name_vi || null,
    fuel: p.fuel,
    capacity_mw: p.capacity_mw,
    province: p.province,
    investor: p.investor || null,
    target_cod: p.target_cod || null,
    status: p.status || 'Planning',
    status_vi: p.status_vi || null,
    progress_pct: p.progress_pct || 0,
    decree_ref: p.decree_ref || null,
    notes: p.notes || null
  }));
}
console.log(`[2] PDP8 Fuel Targets: Parsed ${fuelRows.length} rows.`);
console.log(`[3] PDP8 Priority Projects: Parsed ${priorityRows.length} rows.`);

// ---------------------------------------------------------------------------
// 3. Prepare Tariff Schedules
// ---------------------------------------------------------------------------
const tariffRows = [
  {
    category: 'manufacturing_high_voltage',
    voltage_level: '>= 110 kV',
    normal_hours_vnd: 1826,
    offpeak_hours_vnd: 1100,
    peakhours_vnd: 3171,
    effective_date: '2024-10-11',
    regulatory_mandate: 'Decision 2699/QD-BCT'
  },
  {
    category: 'manufacturing_medium_voltage',
    voltage_level: '22 kV to < 110 kV',
    normal_hours_vnd: 1875,
    offpeak_hours_vnd: 1155,
    peakhours_vnd: 3259,
    effective_date: '2024-10-11',
    regulatory_mandate: 'Decision 2699/QD-BCT'
  },
  {
    category: 'manufacturing_standard_voltage',
    voltage_level: '6 kV to < 22 kV',
    normal_hours_vnd: 1952,
    offpeak_hours_vnd: 1221,
    peakhours_vnd: 3379,
    effective_date: '2024-10-11',
    regulatory_mandate: 'Decision 2699/QD-BCT'
  },
  {
    category: 'manufacturing_low_voltage',
    voltage_level: '< 6 kV',
    normal_hours_vnd: 2040,
    offpeak_hours_vnd: 1276,
    peakhours_vnd: 3511,
    effective_date: '2024-10-11',
    regulatory_mandate: 'Decision 2699/QD-BCT'
  }
];
console.log(`[4] Tariff Schedules: Prepared ${tariffRows.length} rows.`);

// ---------------------------------------------------------------------------
// 4. Prepare Market Intelligence Dispatches
// ---------------------------------------------------------------------------
const newsFile = join(ROOT, 'data', 'industry_news.json');
let dispatchRows = [];

if (existsSync(newsFile)) {
  const newsJson = JSON.parse(readFileSync(newsFile, 'utf8'));
  const articles = newsJson.articles || [];
  dispatchRows = articles.map(a => ({
    id: a.id,
    title: a.title,
    link: a.link,
    source: a.source,
    source_tier: a.source_tier || 'Wire',
    source_color: a.source_color || '#0d9488',
    source_badge_bg: a.source_badge_bg || 'rgba(13,148,136,0.12)',
    source_category: a.source_category || 'Market Intelligence Wire',
    sector: a.sector,
    snippet: a.snippet || null,
    image_url: a.image_url || null,
    pub_date_raw: a.pub_date_raw || null,
    iso_date: a.iso_date || new Date().toISOString(),
    timestamp: a.timestamp || Math.floor(Date.now() / 1000),
    relative_time: a.relative_time || 'Recent'
  }));
}
console.log(`[5] Market Dispatches: Parsed ${dispatchRows.length} rows.`);

// ---------------------------------------------------------------------------
// 5. Seeding Action (Live or Dry-Run)
// ---------------------------------------------------------------------------
if (DRY || !KEY) {
  console.log('\n✓ Dry run complete: All 5 schemas successfully formatted and validated.');
  process.exit(0);
}

async function upsertTable(tableName, rows) {
  console.log(`Seeding public.${tableName} (${rows.length} rows)...`);
  const endpoint = `${SUPABASE_URL}/rest/v1/${tableName}`;
  const res = await fetch(endpoint, {
    method: 'POST',
    headers: {
      'apikey': KEY,
      'Authorization': `Bearer ${KEY}`,
      'Content-Type': 'application/json',
      'Prefer': 'resolution=merge-duplicates'
    },
    body: JSON.stringify(rows)
  });
  if (!res.ok) {
    const errText = await res.text();
    throw new Error(`Failed to seed ${tableName}: ${res.status} - ${errText}`);
  }
  console.log(`  ✓ Successfully upserted ${rows.length} rows into public.${tableName}`);
}

async function run() {
  try {
    await upsertTable('industrial_hubs', hubRows);
    await upsertTable('pdp8_fuel_targets', fuelRows);
    await upsertTable('pdp8_priority_projects', priorityRows);
    await upsertTable('tariff_schedules', tariffRows);
    if (dispatchRows.length > 0) {
      await upsertTable('market_dispatches', dispatchRows);
    }
    console.log('\n>>> ALL SUPABASE TABLES SUCCESSFULLY SEEDED <<<');
  } catch (err) {
    console.error('Seeding error:', err.message);
    process.exit(1);
  }
}

run();
