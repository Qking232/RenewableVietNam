-- Platapp: Supabase Database Schema for Cross-Device Micro-Apps
-- Run this in your Supabase SQL Editor: https://supabase.com/dashboard/project/nkkwegvplpozirrjcxsn/sql

-- 1. Create table for Platapp micro-apps
create table if not exists public.platapp_apps (
  id text primary key,
  title text not null,
  category text not null default 'visual',
  description text default '',
  prompt text default '',
  author text default 'you',
  code text not null,
  thumbnail text,
  revision text not null default '1.0',
  revision_history jsonb not null default '[]'::jsonb,
  password_hash text, -- SHA-256 hash; null if public
  views integer not null default 0,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

-- 2. Enable Row Level Security (RLS)
alter table public.platapp_apps enable row level security;

-- 3. Public Read: anyone across devices can view and run apps
drop policy if exists "Allow public read access" on public.platapp_apps;
create policy "Allow public read access"
  on public.platapp_apps for select
  using (true);

-- 4. Public Insert: anyone can upload a new micro-app
drop policy if exists "Allow public insert access" on public.platapp_apps;
create policy "Allow public insert access"
  on public.platapp_apps for insert
  with check (true);

-- 5. Public Update: allow saving revisions and view counts
drop policy if exists "Allow public update access" on public.platapp_apps;
create policy "Allow public update access"
  on public.platapp_apps for update
  using (true)
  with check (true);

-- 6. Public Delete: allow deleting apps (password protection guarded client-side)
drop policy if exists "Allow public delete access" on public.platapp_apps;
create policy "Allow public delete access"
  on public.platapp_apps for delete
  using (true);

-- 7. High-Performance Indices for feed queries
create index if not exists platapp_apps_created_at_idx on public.platapp_apps(created_at desc);
create index if not exists platapp_apps_category_idx on public.platapp_apps(category);
