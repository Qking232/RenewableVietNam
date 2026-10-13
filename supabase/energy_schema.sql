-- ===========================================================================
--  Renewable Viet Nam  —  Energy projects store  (Supabase / Postgres)
--  Run in: Supabase Dashboard -> SQL Editor -> New query -> Run.
--  Idempotent: re-running updates defaults and policies in place.
--
--  Mirrors the PROJECTS_DB array the /projectenergy/ page renders.
--
--  ACCESS MODEL: the public page reads with the PUBLISHABLE key and may only
--  SELECT. There is no INSERT/UPDATE/DELETE policy for anon, so writes are
--  impossible from the browser. Rows are loaded by scripts/seed_energy.mjs,
--  which runs locally with the SECRET key taken from an environment variable.
--  Never put a secret key (sb_secret_… / service_role) in a page or a commit.
-- ===========================================================================

create extension if not exists "pgcrypto";

-- ---------------------------------------------------------------- projects
create table if not exists public.energy_projects (
  id        uuid primary key default gen_random_uuid(),
  name      text not null,
  company   text not null default 'Not stated',
  country   text not null default 'Viet Nam',
  type      text not null check (type in ('solar','wind','hydro','lng','nuclear',
                                          'coal','oil','biomass')),
  cap       text not null default 'Not stated',
  loc       text,
  lat       double precision not null check (lat between 8.0 and 23.5),
  lon       double precision not null check (lon between 102.0 and 110.5),
  note      text,
  -- provenance: which source list a row came from, for traceability
  source    text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

-- A plant of one energy type may share a name with a different-type plant
-- (e.g. "Long Sơn" exists as both gas and solar), so uniqueness is per (type,name).
create unique index if not exists energy_projects_type_name_key
  on public.energy_projects (type, name);

create index if not exists energy_projects_type_idx on public.energy_projects (type);
create index if not exists energy_projects_loc_idx  on public.energy_projects (loc);

-- keep updated_at honest on upsert
create or replace function public.energy_projects_touch()
returns trigger language plpgsql as $$
begin
  new.updated_at = now();
  return new;
end $$;

drop trigger if exists energy_projects_touch_trg on public.energy_projects;
create trigger energy_projects_touch_trg
  before update on public.energy_projects
  for each row execute function public.energy_projects_touch();

-- ------------------------------------------------------------- privileges
grant usage on schema public to anon, authenticated;
grant select on public.energy_projects to anon, authenticated;
-- explicitly deny everything else to the public roles
revoke insert, update, delete, truncate, references, trigger
  on public.energy_projects from anon, authenticated;

-- --------------------------------------------------------------------- RLS
alter table public.energy_projects enable row level security;

-- Public may read every row. No write policy exists, and privileges are
-- revoked, so the publishable key can only ever SELECT.
drop policy if exists "public reads energy projects" on public.energy_projects;
create policy "public reads energy projects"
  on public.energy_projects for select
  to anon, authenticated
  using (true);

-- --------------------------------------------------------------- reporting
-- Handy sanity query: run after seeding.
--   select type, count(*) from public.energy_projects group by type order by 2 desc;
