-- ===========================================================================
--  Renewable Viet Nam — Universal Portal Schemas (Supabase / Postgres)
-- ===========================================================================
--  Run in: Supabase Dashboard -> SQL Editor -> New query -> Run.
--  Idempotent: Re-running updates policies and table constraints safely.
--
--  Access Model:
--   - Public frontend pages read via PostgREST with the PUBLISHABLE key (SELECT only).
--   - Mutations / Data Ingestion are strictly performed by local administration scripts
--     using the SECRET key (service_role) which bypasses RLS.
-- ===========================================================================

create extension if not exists "pgcrypto";

-- ---------------------------------------------------------------------------
-- 1. Industrial Hubs & Clean Siting Directory (public.industrial_hubs)
-- ---------------------------------------------------------------------------
create table if not exists public.industrial_hubs (
  id                    text primary key,
  name                  text not null,
  vietnamese_name       text,
  developer             text default 'Not stated',
  province              text not null,
  region                text not null check (region in ('North', 'Central', 'South')),
  total_area_ha         double precision not null default 0,
  substation            text,
  substation_kv         integer not null default 110,
  rooftop_installed_mwp double precision not null default 0,
  rooftop_potential_mwp double precision not null default 0,
  dppa_tier             text default 'Pending Evaluation',
  dppa_class            text default 'evaluating',
  clean_energy_share    double precision not null default 0,
  certifications        jsonb not null default '[]'::jsonb,
  anchor_tenants        jsonb not null default '[]'::jsonb,
  lat                   double precision not null check (lat between 8.0 and 24.0),
  lng                   double precision not null check (lng between 102.0 and 111.0),
  dppa_summary          text,
  created_at            timestamptz not null default now(),
  updated_at            timestamptz not null default now()
);

create index if not exists industrial_hubs_province_idx on public.industrial_hubs (province);
create index if not exists industrial_hubs_region_idx on public.industrial_hubs (region);
create index if not exists industrial_hubs_geo_idx on public.industrial_hubs (lat, lng);

alter table public.industrial_hubs enable row level security;
grant select on public.industrial_hubs to anon, authenticated;

drop policy if exists industrial_hubs_read on public.industrial_hubs;
create policy industrial_hubs_read on public.industrial_hubs for select to anon, authenticated using (true);


-- ---------------------------------------------------------------------------
-- 2. PDP8 Fuel Targets & Capacity Breakdown (public.pdp8_fuel_targets)
-- ---------------------------------------------------------------------------
create table if not exists public.pdp8_fuel_targets (
  fuel                  text primary key,
  fuel_vi               text not null,
  target_2030_mw        double precision not null,
  current_operating_mw  double precision not null default 0,
  pipeline_mw           double precision not null default 0,
  target_share_pct      double precision not null default 0,
  color                 text not null default 'teal',
  hex                   text not null default '#14b8a6',
  status_note           text,
  updated_at            timestamptz not null default now()
);

alter table public.pdp8_fuel_targets enable row level security;
grant select on public.pdp8_fuel_targets to anon, authenticated;

drop policy if exists pdp8_fuel_targets_read on public.pdp8_fuel_targets;
create policy pdp8_fuel_targets_read on public.pdp8_fuel_targets for select to anon, authenticated using (true);


-- ---------------------------------------------------------------------------
-- 3. PDP8 Strategic Priority Infrastructure (public.pdp8_priority_projects)
-- ---------------------------------------------------------------------------
create table if not exists public.pdp8_priority_projects (
  id                    text primary key,
  name                  text not null,
  name_vi               text,
  fuel                  text not null,
  capacity_mw           double precision not null,
  province              text not null,
  investor              text,
  target_cod            text,
  status                text not null default 'Planning',
  status_vi             text,
  progress_pct          double precision not null default 0,
  decree_ref            text,
  notes                 text,
  updated_at            timestamptz not null default now()
);

alter table public.pdp8_priority_projects enable row level security;
grant select on public.pdp8_priority_projects to anon, authenticated;

drop policy if exists pdp8_priority_projects_read on public.pdp8_priority_projects;
create policy pdp8_priority_projects_read on public.pdp8_priority_projects for select to anon, authenticated using (true);


-- ---------------------------------------------------------------------------
-- 4. National Statutory Tariff Schedules & CBAM Coefficients (public.tariff_schedules)
-- ---------------------------------------------------------------------------
create table if not exists public.tariff_schedules (
  category              text primary key,
  voltage_level         text not null,
  normal_hours_vnd      double precision not null,
  offpeak_hours_vnd     double precision not null,
  peakhours_vnd         double precision not null,
  effective_date        date not null default '2024-10-11',
  regulatory_mandate    text not null default 'Decision 2699/QD-BCT'
);

alter table public.tariff_schedules enable row level security;
grant select on public.tariff_schedules to anon, authenticated;

drop policy if exists tariff_schedules_read on public.tariff_schedules;
create policy tariff_schedules_read on public.tariff_schedules for select to anon, authenticated using (true);


-- ---------------------------------------------------------------------------
-- 5. Real-Time Market Dispatches & Multi-Source Wire Feeds (public.market_dispatches)
-- ---------------------------------------------------------------------------
create table if not exists public.market_dispatches (
  id                    text primary key,
  title                 text not null,
  link                  text not null,
  source                text not null,
  source_tier           text default 'Wire',
  source_color          text default '#0d9488',
  source_badge_bg       text default 'rgba(13,148,136,0.12)',
  source_category       text default 'Market Intelligence Wire',
  sector                text not null,
  snippet               text,
  image_url             text,
  pub_date_raw          text,
  iso_date              timestamptz not null default now(),
  timestamp             bigint,
  relative_time         text,
  created_at            timestamptz not null default now(),
  updated_at            timestamptz not null default now()
);

create index if not exists market_dispatches_date_idx on public.market_dispatches (iso_date desc);
create index if not exists market_dispatches_sector_idx on public.market_dispatches (sector);
create index if not exists market_dispatches_source_idx on public.market_dispatches (source);

alter table public.market_dispatches enable row level security;
grant select on public.market_dispatches to anon, authenticated;

drop policy if exists market_dispatches_read on public.market_dispatches;
create policy market_dispatches_read on public.market_dispatches for select to anon, authenticated using (true);

