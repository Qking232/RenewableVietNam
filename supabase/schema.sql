-- ===========================================================================
--  Renewable Viet Nam — Hub discussion store  (Supabase / Postgres)
--  Run once: Supabase Dashboard -> SQL Editor -> New query -> paste -> Run.
--
--  Model: every submission is inserted as 'pending'. Only rows an editor flips
--  to 'approved' are readable by the public. The public anon key may INSERT
--  (pending only) and read approved rows — nothing else.
-- ===========================================================================

create extension if not exists "pgcrypto";

-- ------------------------------------------------------------------ topics
create table if not exists public.hub_topics (
  id          uuid primary key default gen_random_uuid(),
  created_at  timestamptz not null default now(),
  status      text not null default 'pending' check (status in ('pending','approved','rejected')),
  theme       text not null default 'grid'    check (char_length(theme) <= 40),
  title       text not null                   check (char_length(title) between 3 and 200),
  author      text                            check (char_length(coalesce(author,'')) <= 120),
  context     text                            check (char_length(coalesce(context,'')) <= 4000),
  questions   jsonb not null default '[]'::jsonb,
  refs        jsonb not null default '[]'::jsonb
);

create index if not exists hub_topics_status_idx on public.hub_topics (status, created_at);

-- ------------------------------------------------------------------- views
create table if not exists public.hub_views (
  id          uuid primary key default gen_random_uuid(),
  created_at  timestamptz not null default now(),
  status      text not null default 'pending' check (status in ('pending','approved','rejected')),
  topic_id    text not null,
  author      text                            check (char_length(coalesce(author,'')) <= 120),
  body        text not null                   check (char_length(body) between 2 and 4000)
);

create index if not exists hub_views_topic_idx on public.hub_views (topic_id, status, created_at);

-- --------------------------------------------------------------- privileges
-- Deterministic grants for the API roles (RLS still decides which rows).
grant usage on schema public to anon, authenticated;
grant select, insert on public.hub_topics to anon, authenticated;
grant select, insert on public.hub_views  to anon, authenticated;
revoke update, delete, truncate, references, trigger on public.hub_topics from anon, authenticated;
revoke update, delete, truncate, references, trigger on public.hub_views  from anon, authenticated;

-- ---------------------------------------------------------------------- RLS
alter table public.hub_topics enable row level security;
alter table public.hub_views  enable row level security;

-- Anyone may read approved rows.
drop policy if exists "public reads approved topics" on public.hub_topics;
create policy "public reads approved topics"
  on public.hub_topics for select
  using (status = 'approved');

drop policy if exists "public reads approved views" on public.hub_views;
create policy "public reads approved views"
  on public.hub_views for select
  using (status = 'approved');

-- Anyone may submit — but only as 'pending' (they cannot self-approve).
drop policy if exists "public submits topics" on public.hub_topics;
create policy "public submits topics"
  on public.hub_topics for insert
  with check (status = 'pending');

drop policy if exists "public submits views" on public.hub_views;
create policy "public submits views"
  on public.hub_views for insert
  with check (status = 'pending');

-- Deliberately no UPDATE/DELETE policies: the public cannot change or remove
-- rows. The Supabase dashboard (service role) bypasses RLS, which is how you
-- moderate.
