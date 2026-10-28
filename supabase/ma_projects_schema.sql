-- ==============================================================================
-- Vietnam Investment Project Legal Management & M&A Engine Schema
-- Supabase Table & RLS Policy for Cross-Device Project & State Synchronization
-- ==============================================================================

-- 1. Create Dedicated Table for Legal M&A Projects
create table if not exists public.ma_projects (
  id text primary key,
  name text not null,
  project_type text not null default 'URBAN_TOWN',
  scenario_key text not null default 'GREENFIELD',
  location text default 'Toàn quốc',
  tasks jsonb not null default '[]'::jsonb,
  revision text not null default '1.0',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

-- 2. Enable Row Level Security (RLS)
alter table public.ma_projects enable row level security;

-- 3. RLS Policies: Allow Read, Insert, Update, and Delete
drop policy if exists "Allow public select on ma_projects" on public.ma_projects;
create policy "Allow public select on ma_projects"
  on public.ma_projects for select
  using (true);

drop policy if exists "Allow public insert on ma_projects" on public.ma_projects;
create policy "Allow public insert on ma_projects"
  on public.ma_projects for insert
  with check (true);

drop policy if exists "Allow public update on ma_projects" on public.ma_projects;
create policy "Allow public update on ma_projects"
  on public.ma_projects for update
  using (true)
  with check (true);

drop policy if exists "Allow public delete on ma_projects" on public.ma_projects;
create policy "Allow public delete on ma_projects"
  on public.ma_projects for delete
  using (true);

-- 4. High-Performance Indices
create index if not exists ma_projects_updated_at_idx on public.ma_projects(updated_at desc);
create index if not exists ma_projects_project_type_idx on public.ma_projects(project_type);
