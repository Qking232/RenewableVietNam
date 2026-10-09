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

-- -------------------------------------------------------------- documents
-- Rev 0.10: the Hub became a document library. Metadata lives here; the files
-- themselves live in the storage bucket below (path recorded in file_path).
create table if not exists public.hub_documents (
  id          uuid primary key default gen_random_uuid(),
  created_at  timestamptz not null default now(),
  status      text not null default 'approved' check (status in ('pending','approved','rejected')),
  doc_type    text not null default 'report'   check (char_length(doc_type) <= 40),
  collection  text not null default 'grid'     check (char_length(collection) <= 40),
  title       text not null                    check (char_length(title) between 3 and 300),
  author      text                             check (char_length(coalesce(author,'')) <= 200),
  year        text                             check (char_length(coalesce(year,'')) <= 12),
  lang        text                             check (char_length(coalesce(lang,'')) <= 8),
  summary     text                             check (char_length(coalesce(summary,'')) <= 4000),
  points      jsonb not null default '[]'::jsonb,
  refs        jsonb not null default '[]'::jsonb,
  source      text                             check (char_length(coalesce(source,'')) <= 500),
  license     text                             check (char_length(coalesce(license,'')) <= 200),
  -- Download links used when no file is uploaded. `links` is an array of
  -- { url, updated } objects (a direct file URL or a magnet:/.torrent link);
  -- download_link is the older single-link column, still read for compatibility.
  download_link text,
  links       jsonb not null default '[]'::jsonb check (jsonb_typeof(links) = 'array'),
  file_path   text,
  file_name   text,
  file_type   text,
  file_size   bigint,
  downloads   integer not null default 0
);

create index if not exists hub_documents_status_idx on public.hub_documents (status, created_at);

grant select, insert on public.hub_documents to anon, authenticated;
revoke update, delete, truncate, references, trigger on public.hub_documents from anon, authenticated;

alter table public.hub_documents enable row level security;

drop policy if exists "public reads approved documents" on public.hub_documents;
create policy "public reads approved documents"
  on public.hub_documents for select using (status = 'approved');

drop policy if exists "public submits documents" on public.hub_documents;
create policy "public submits documents"
  on public.hub_documents for insert with check (status = 'approved');

-- Columns carried by newer documents (idempotent). `updated` is the last-modified
-- date shown in the table; `rev` is the document's revision label.
alter table public.hub_documents add column if not exists updated timestamptz;
alter table public.hub_documents add column if not exists rev text;
alter table public.hub_documents add column if not exists download_link text;
alter table public.hub_documents add column if not exists links jsonb not null default '[]'::jsonb;

-- ------------------------------------------------------------- view counts
-- One row per view (insert-only), counted client-side. This keeps the public key
-- insert-only while still yielding a shared "views" number for each document.
create table if not exists public.hub_doc_views (
  id         uuid primary key default gen_random_uuid(),
  created_at timestamptz not null default now(),
  doc_id     text not null
);
create index if not exists hub_doc_views_doc_idx on public.hub_doc_views (doc_id);

grant select, insert on public.hub_doc_views to anon, authenticated;
revoke update, delete, truncate, references, trigger on public.hub_doc_views from anon, authenticated;

alter table public.hub_doc_views enable row level security;

drop policy if exists "public reads doc views" on public.hub_doc_views;
create policy "public reads doc views"
  on public.hub_doc_views for select using (true);

drop policy if exists "public logs doc views" on public.hub_doc_views;
create policy "public logs doc views"
  on public.hub_doc_views for insert with check (true);

-- ------------------------------------------------------------ shared links
-- Download links anyone can add to any document, so a link saved on one device
-- shows up on every device (a document's own `links` column only covers links
-- given at upload time). Insert-only for everyone; a row may be removed by the
-- browser that added it, identified by the x-link-token request header.
create table if not exists public.hub_doc_links (
  id         uuid primary key default gen_random_uuid(),
  created_at timestamptz not null default now(),
  doc_id     text not null,
  url        text not null check (char_length(url) between 4 and 2000),
  owner      text check (char_length(coalesce(owner,'')) <= 60)
);
create index if not exists hub_doc_links_doc_idx on public.hub_doc_links (doc_id, created_at);

grant select, insert, delete on public.hub_doc_links to anon, authenticated;
revoke update, truncate, references, trigger on public.hub_doc_links from anon, authenticated;

alter table public.hub_doc_links enable row level security;

drop policy if exists "public reads doc links" on public.hub_doc_links;
create policy "public reads doc links"
  on public.hub_doc_links for select using (true);

drop policy if exists "public adds doc links" on public.hub_doc_links;
create policy "public adds doc links"
  on public.hub_doc_links for insert with check (true);

-- Only the browser that added a link (holding its owner token) may delete it.
drop policy if exists "owner removes doc links" on public.hub_doc_links;
create policy "owner removes doc links"
  on public.hub_doc_links for delete
  using (owner is not null
     and owner = (coalesce(current_setting('request.headers', true), '{}')::json ->> 'x-link-token'));

-- ------------------------------------------------------------- file storage
-- A public bucket for the document files. Anyone may read or upload a file;
-- the per-object size cap (25 MB) matches the page's client-side limit.
insert into storage.buckets (id, name, public, file_size_limit)
values ('hub-docs', 'hub-docs', true, 26214400)
on conflict (id) do update set public = true;

drop policy if exists "public reads hub files" on storage.objects;
create policy "public reads hub files"
  on storage.objects for select using (bucket_id = 'hub-docs');

drop policy if exists "public uploads hub files" on storage.objects;
create policy "public uploads hub files"
  on storage.objects for insert with check (bucket_id = 'hub-docs');

-- hub_views is reused unchanged for per-document comments (topic_id = document id).

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
