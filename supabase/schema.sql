-- ===========================================================================
--  Renewable Viet Nam — Hub discussion store  (Supabase / Postgres)
--  Run (or re-run) in: Supabase Dashboard -> SQL Editor -> New query -> Run.
--  It is idempotent, so running it again just updates the defaults/policies.
--
--  AUTO-APPROVE MODE. Submissions are inserted as 'approved' and appear on the
--  shelf immediately — there is no review step. The public anon key may INSERT
--  and read approved rows, nothing else.
--
--  To go back to moderated submissions, change the two column defaults below to
--  'pending' and the two INSERT policies' WITH CHECK to (status = 'pending').
-- ===========================================================================

create extension if not exists "pgcrypto";

-- ------------------------------------------------------------------ topics
create table if not exists public.hub_topics (
  id          uuid primary key default gen_random_uuid(),
  created_at  timestamptz not null default now(),
  status      text not null default 'approved' check (status in ('pending','approved','rejected')),
  theme       text not null default 'grid'     check (char_length(theme) <= 40),
  title       text not null                    check (char_length(title) between 3 and 200),
  author      text                             check (char_length(coalesce(author,'')) <= 120),
  context     text                             check (char_length(coalesce(context,'')) <= 4000),
  questions   jsonb not null default '[]'::jsonb,
  refs        jsonb not null default '[]'::jsonb,
  -- Context images, stored as small data-URL strings (the page scales them
  -- down before sending). Optional: without this column the Hub still works,
  -- it just posts topics without images.
  images      jsonb not null default '[]'::jsonb check (jsonb_typeof(images) = 'array')
);

-- ------------------------------------------------------------------- views
create table if not exists public.hub_views (
  id          uuid primary key default gen_random_uuid(),
  created_at  timestamptz not null default now(),
  status      text not null default 'approved' check (status in ('pending','approved','rejected')),
  topic_id    text not null,
  author      text                             check (char_length(coalesce(author,'')) <= 120),
  body        text not null                    check (char_length(body) between 2 and 4000)
);

-- Keep already-created tables in step when this file is re-run.
alter table public.hub_topics alter column status set default 'approved';
alter table public.hub_views  alter column status set default 'approved';
alter table public.hub_topics add column if not exists images jsonb not null default '[]'::jsonb;

create index if not exists hub_topics_status_idx on public.hub_topics (status, created_at);
create index if not exists hub_views_topic_idx   on public.hub_views (topic_id, status, created_at);

-- --------------------------------------------------------------- privileges
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

-- Anyone may submit, and it is published immediately (auto-approve).
drop policy if exists "public submits topics" on public.hub_topics;
create policy "public submits topics"
  on public.hub_topics for insert
  with check (status = 'approved');

drop policy if exists "public submits views" on public.hub_views;
create policy "public submits views"
  on public.hub_views for insert
  with check (status = 'approved');

-- Deliberately no UPDATE/DELETE policies: the public cannot change or remove
-- rows. The Supabase dashboard (service role) bypasses RLS, so you can still
-- edit or delete anything there — e.g. set status to 'rejected' to hide a row.

-- ===========================================================================
--  OPTIONAL: throttle submissions per client IP (recommended with auto-approve)
--  Uncomment and run this block if the shelf starts collecting spam. It allows
--  10 submissions per hour per address and fails open if the address is unknown.
-- ===========================================================================
-- alter table public.hub_topics add column if not exists client_ip text;
-- alter table public.hub_views  add column if not exists client_ip text;
--
-- create or replace function public.hub_rate_ok() returns trigger
-- language plpgsql set search_path = public as $$
-- declare ip text; hits integer;
-- begin
--   ip := btrim(coalesce(
--     split_part(coalesce(current_setting('request.headers', true), '{}')::json ->> 'x-forwarded-for', ',', 1),
--     'unknown'));
--   if ip <> 'unknown' then
--     execute format('select count(*) from public.%I where client_ip = $1 and created_at > now() - interval ''1 hour''', TG_TABLE_NAME)
--       into hits using ip;
--     if hits >= 10 then
--       raise exception 'Too many submissions from this address — please try again later.'
--         using errcode = 'check_violation';
--     end if;
--   end if;
--   new.client_ip := ip;
--   return new;
-- end $$;
--
-- drop trigger if exists hub_topics_rate on public.hub_topics;
-- create trigger hub_topics_rate before insert on public.hub_topics
--   for each row execute function public.hub_rate_ok();
-- drop trigger if exists hub_views_rate on public.hub_views;
-- create trigger hub_views_rate before insert on public.hub_views
--   for each row execute function public.hub_rate_ok();
