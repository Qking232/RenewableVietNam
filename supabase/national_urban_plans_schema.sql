-- ==============================================================================
-- Vietnam National Urban Planning Data Schema (quyhoach.xaydung.gov.vn)
-- Supabase Cloud Table & Row Level Security (RLS) Policies
-- Run this in your Supabase SQL Editor: https://supabase.com/dashboard/project/nkkwegvplpozirrjcxsn/sql
-- ==============================================================================

-- 1. Create Dedicated Table for National Urban Planning Records
create table if not exists public.national_urban_plans (
  project_id bigint primary key,
  province text not null,
  title text not null,
  planning_type text,
  approval_decision text,
  approval_date text,
  approval_authority text,
  organizing_agency text,
  consultant text,
  location_desc text,
  total_area_m2 numeric,
  land_use_table jsonb default '[]'::jsonb,
  attached_files jsonb default '[]'::jsonb,
  source_url text not null,
  raw_summary text,
  ingested_at timestamptz not null default now(),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

-- 2. Enable Row Level Security (RLS)
alter table public.national_urban_plans enable row level security;

-- 3. RLS Policies: Allow Public Read, Insert, Update, and Delete
drop policy if exists "Allow public select on national_urban_plans" on public.national_urban_plans;
create policy "Allow public select on national_urban_plans"
  on public.national_urban_plans for select
  using (true);

drop policy if exists "Allow public insert on national_urban_plans" on public.national_urban_plans;
create policy "Allow public insert on national_urban_plans"
  on public.national_urban_plans for insert
  with check (true);

drop policy if exists "Allow public update on national_urban_plans" on public.national_urban_plans;
create policy "Allow public update on national_urban_plans"
  on public.national_urban_plans for update
  using (true)
  with check (true);

drop policy if exists "Allow public delete on national_urban_plans" on public.national_urban_plans;
create policy "Allow public delete on national_urban_plans"
  on public.national_urban_plans for delete
  using (true);

-- 4. High-Performance Indices for Nationwide Querying
create index if not exists idx_national_plans_province on public.national_urban_plans(province);
create index if not exists idx_national_plans_type on public.national_urban_plans(planning_type);
create index if not exists idx_national_plans_updated_at on public.national_urban_plans(updated_at desc);
