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

-- ------------------------------------------------------- shared collections
-- The collections shown in "Browse Docs", shared so every device sees the same
-- list: a row can add a new collection, rename one (including a built-in, via its
-- key) or hide it (hidden = true). Upserts only, so no delete policy is needed.
create table if not exists public.hub_collections (
  key        text primary key check (char_length(key) between 1 and 60),
  label      text not null       check (char_length(label) between 1 and 120),
  tone       jsonb,
  hidden     boolean not null default false,
  created_at timestamptz not null default now(),
  updated    timestamptz not null default now()
);

grant select, insert, update on public.hub_collections to anon, authenticated;
revoke delete, truncate, references, trigger on public.hub_collections from anon, authenticated;

alter table public.hub_collections enable row level security;

drop policy if exists "public reads collections" on public.hub_collections;
create policy "public reads collections"
  on public.hub_collections for select using (true);

drop policy if exists "public adds collections" on public.hub_collections;
create policy "public adds collections"
  on public.hub_collections for insert with check (true);

drop policy if exists "public updates collections" on public.hub_collections;
create policy "public updates collections"
  on public.hub_collections for update using (true) with check (true);

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

-- ===========================================================================
--  OPTIONAL: password-protected edits/deletes (Hub "Edit" and "Delete" buttons)
--  The publishable key still cannot UPDATE or DELETE hub_documents directly, so
--  these SECURITY DEFINER functions do the write AFTER checking a password that
--  only lives here (not in the page). Change the password below to change it.
-- ===========================================================================
create or replace function public.hub_admin_ok(pw text)
returns boolean language sql immutable as $$
  select coalesce(pw, '') = '123';
$$;

-- Update one document's fields, addressed by uuid. Returns true if a row changed.
create or replace function public.hub_update_document(p_id uuid, pw text, p jsonb)
returns boolean language plpgsql security definer set search_path = public, extensions as $$
begin
  if not public.hub_admin_ok(pw) then
    raise exception 'wrong password' using errcode = '42501';
  end if;
  update public.hub_documents set
    doc_type   = coalesce(p->>'doc_type', doc_type),
    collection = coalesce(p->>'collection', collection),
    title      = coalesce(p->>'title', title),
    author     = coalesce(p->>'author', author),
    year       = coalesce(p->>'year', year),
    lang       = coalesce(p->>'lang', lang),
    summary    = coalesce(p->>'summary', summary),
    source     = coalesce(p->>'source', source),
    license    = coalesce(p->>'license', license),
    points     = coalesce(p->'points', points),
    refs       = coalesce(p->'refs', refs),
    links      = coalesce(p->'links', links),
    rev        = coalesce(p->>'rev', rev),
    updated    = now()
  where id = p_id;
  return found;
end $$;

-- Delete documents by uuid list. Returns how many rows were removed.
create or replace function public.hub_delete_documents(p_ids uuid[], pw text)
returns integer language plpgsql security definer set search_path = public, extensions as $$
declare n integer;
begin
  if not public.hub_admin_ok(pw) then
    raise exception 'wrong password' using errcode = '42501';
  end if;
  delete from public.hub_documents where id = any(p_ids);
  get diagnostics n = row_count;
  return n;
end $$;

revoke all on function public.hub_admin_ok(text) from public;
revoke all on function public.hub_update_document(uuid, text, jsonb) from public;
revoke all on function public.hub_delete_documents(uuid[], text) from public;
grant execute on function public.hub_update_document(uuid, text, jsonb) to anon, authenticated;
grant execute on function public.hub_delete_documents(uuid[], text) to anon, authenticated;

-- Aggregated view counts for the shelf. One small response instead of paging
-- through every hub_doc_views row (the public API caps a request at 1000 rows,
-- which silently under-counts once a document has a few hundred views).
create or replace function public.hub_view_counts()
returns table(doc_id text, n bigint)
language sql stable security definer set search_path = public as $$
  select doc_id, count(*)::bigint from public.hub_doc_views group by doc_id;
$$;
revoke all on function public.hub_view_counts() from public;
grant execute on function public.hub_view_counts() to anon, authenticated;

-- ===========================================================================
--  BTC portfolio  (page: /test/btc/)   — private per person
--  Each device sets a private code. The page sends sha256(code) in the
--  x-owner-hash request header and every row is keyed to it, so RLS lets the
--  publishable key see and touch ONLY the rows for the hash it sends: one
--  visitor cannot read another's list. The same code on another device gives
--  the same portfolio, with no login. No UPDATE — rows are added or removed.
-- ===========================================================================
create table if not exists public.btc_portfolio (
  id         uuid primary key default gen_random_uuid(),
  created_at timestamptz not null default now(),
  owner_hash text not null,
  pair       text not null check (char_length(pair) between 3 and 40),
  base       text not null check (char_length(base) between 1 and 20),
  name       text          check (char_length(coalesce(name, '')) <= 120)
);

-- Bring an older (shared) table up to date without touching existing rows.
alter table public.btc_portfolio add column if not exists owner_hash text;

-- One row per coin per owner. The earlier global-uniqueness index would stop
-- two people both holding BTC, so it is replaced by the per-owner one.
drop index if exists public.btc_portfolio_pair_idx;
create unique index if not exists btc_portfolio_owner_pair_idx on public.btc_portfolio (owner_hash, pair);
create index if not exists btc_portfolio_owner_idx on public.btc_portfolio (owner_hash, created_at);

grant select, insert, delete on public.btc_portfolio to anon, authenticated;
revoke update, truncate, references, trigger on public.btc_portfolio from anon, authenticated;

alter table public.btc_portfolio enable row level security;

-- Retire the shared-list policies.
drop policy if exists "public reads btc portfolio"   on public.btc_portfolio;
drop policy if exists "public adds btc portfolio"    on public.btc_portfolio;
drop policy if exists "public removes btc portfolio" on public.btc_portfolio;

drop policy if exists "owner reads own portfolio"   on public.btc_portfolio;
drop policy if exists "owner adds own portfolio"    on public.btc_portfolio;
drop policy if exists "owner removes own portfolio" on public.btc_portfolio;

create policy "owner reads own portfolio"
  on public.btc_portfolio for select
  using (owner_hash = coalesce(current_setting('request.headers', true), '{}')::json ->> 'x-owner-hash');

create policy "owner adds own portfolio"
  on public.btc_portfolio for insert
  with check (owner_hash = coalesce(current_setting('request.headers', true), '{}')::json ->> 'x-owner-hash');

create policy "owner removes own portfolio"
  on public.btc_portfolio for delete
  using (owner_hash = coalesce(current_setting('request.headers', true), '{}')::json ->> 'x-owner-hash');

-- ===========================================================================
--  Hub favourites  (page: /hub/)   — private per person, cross-device
--  Signing in on /hub/ with a private key derives sha256('hub:' + key) and
--  sends it in the x-owner-hash request header. Each row is keyed to that hash,
--  so RLS lets the publishable key see and touch ONLY the favourites for the
--  hash it sends: one visitor cannot read another's list. The same private key
--  on another device gives the same favourites, with no login server-side.
-- ===========================================================================
create table if not exists public.hub_favourites (
  id         uuid primary key default gen_random_uuid(),
  created_at timestamptz not null default now(),
  owner_hash text not null check (char_length(owner_hash) between 1 and 80),
  doc_id     text not null check (char_length(doc_id) between 1 and 160),
  name       text          check (char_length(coalesce(name, '')) <= 120),
  email      text          check (char_length(coalesce(email, '')) <= 200)
);

create unique index if not exists hub_favourites_owner_doc_idx on public.hub_favourites (owner_hash, doc_id);
create index if not exists hub_favourites_owner_idx on public.hub_favourites (owner_hash, created_at);

grant select, insert, delete on public.hub_favourites to anon, authenticated;
revoke update, truncate, references, trigger on public.hub_favourites from anon, authenticated;

alter table public.hub_favourites enable row level security;

drop policy if exists "owner reads own favourites"   on public.hub_favourites;
drop policy if exists "owner adds own favourites"    on public.hub_favourites;
drop policy if exists "owner removes own favourites" on public.hub_favourites;

create policy "owner reads own favourites"
  on public.hub_favourites for select
  using (owner_hash = coalesce(current_setting('request.headers', true), '{}')::json ->> 'x-owner-hash');

create policy "owner adds own favourites"
  on public.hub_favourites for insert
  with check (owner_hash = coalesce(current_setting('request.headers', true), '{}')::json ->> 'x-owner-hash');

create policy "owner removes own favourites"
  on public.hub_favourites for delete
  using (owner_hash = coalesce(current_setting('request.headers', true), '{}')::json ->> 'x-owner-hash');

-- ===========================================================================
--  Hub users & admin console  (page: /hub/admin/)  — presence + who may delete
--  Signing in on /hub/ records the user (owner_hash = sha256('hub:' + key)), and
--  each sign-in updates last_seen, so the admin console can monitor who is using
--  the library. hub_users is not readable or writable with the publishable key —
--  only through these SECURITY DEFINER functions.
-- ===========================================================================
create table if not exists public.hub_users (
  owner_hash text primary key check (char_length(owner_hash) between 1 and 80),
  name       text          check (char_length(coalesce(name, '')) <= 120),
  email      text          check (char_length(coalesce(email, '')) <= 200),
  can_delete boolean not null default false,
  first_seen timestamptz not null default now(),
  last_seen  timestamptz not null default now()
);

alter table public.hub_users enable row level security;
-- Deliberately no policies: the publishable key cannot touch this table directly.

-- Record a sign-in (called by /hub/ once the private key is accepted).
create or replace function public.hub_user_ping(p_hash text, p_name text, p_email text)
returns boolean language plpgsql security definer set search_path = public as $$
begin
  if char_length(coalesce(p_hash, '')) < 1 then return false; end if;
  insert into public.hub_users(owner_hash, name, email, last_seen)
  values (p_hash, left(coalesce(p_name, ''), 120), left(coalesce(p_email, ''), 200), now())
  on conflict (owner_hash) do update
    set name = excluded.name, email = excluded.email, last_seen = now();
  return true;
end $$;
revoke all on function public.hub_user_ping(text, text, text) from public;
grant execute on function public.hub_user_ping(text, text, text) to anon, authenticated;

-- May this user delete shared documents?
create or replace function public.hub_user_can_delete(p_hash text)
returns boolean language sql stable security definer set search_path = public as $$
  select coalesce((select can_delete from public.hub_users where owner_hash = p_hash), false);
$$;
revoke all on function public.hub_user_can_delete(text) from public;
grant execute on function public.hub_user_can_delete(text) to anon, authenticated;

-- Admin console: list every user, with their favourites count.
create or replace function public.hub_admin_users(pw text)
returns table(owner_hash text, name text, email text, can_delete boolean,
              first_seen timestamptz, last_seen timestamptz, favourites bigint)
language plpgsql security definer set search_path = public as $$
begin
  if not public.hub_admin_ok(pw) then
    raise exception 'wrong password' using errcode = '42501';
  end if;
  return query
    select u.owner_hash, u.name, u.email, u.can_delete, u.first_seen, u.last_seen,
           (select count(*) from public.hub_favourites f where f.owner_hash = u.owner_hash)::bigint
    from public.hub_users u
    order by u.last_seen desc;
end $$;
revoke all on function public.hub_admin_users(text) from public;
grant execute on function public.hub_admin_users(text) to anon, authenticated;

-- Admin console: allow or stop one user from deleting documents.
create or replace function public.hub_admin_set_delete(pw text, p_hash text, p_can boolean)
returns boolean language plpgsql security definer set search_path = public as $$
begin
  if not public.hub_admin_ok(pw) then
    raise exception 'wrong password' using errcode = '42501';
  end if;
  update public.hub_users set can_delete = coalesce(p_can, false) where owner_hash = p_hash;
  return found;
end $$;
revoke all on function public.hub_admin_set_delete(text, text, boolean) from public;
grant execute on function public.hub_admin_set_delete(text, text, boolean) to anon, authenticated;

-- Editing a shared document: allowed for the admin key, or any user who has signed in.
create or replace function public.hub_update_document(p_id uuid, pw text, p jsonb)
returns boolean language plpgsql security definer set search_path = public, extensions as $$
declare h text;
begin
  h := encode(digest('hub:' || coalesce(pw, ''), 'sha256'), 'hex');
  if not public.hub_admin_ok(pw)
     and not exists (select 1 from public.hub_users u where u.owner_hash = h) then
    raise exception 'wrong password' using errcode = '42501';
  end if;
  update public.hub_documents set
    doc_type   = coalesce(p->>'doc_type', doc_type),
    collection = coalesce(p->>'collection', collection),
    title      = coalesce(p->>'title', title),
    author     = coalesce(p->>'author', author),
    year       = coalesce(p->>'year', year),
    lang       = coalesce(p->>'lang', lang),
    summary    = coalesce(p->>'summary', summary),
    source     = coalesce(p->>'source', source),
    license    = coalesce(p->>'license', license),
    points     = coalesce(p->'points', points),
    refs       = coalesce(p->'refs', refs),
    links      = coalesce(p->'links', links),
    rev        = coalesce(p->>'rev', rev),
    updated    = now()
  where id = p_id;
  return found;
end $$;

-- Deleting documents: allowed for the admin key, or a user the admin marked
-- "can delete". Calls are rejected with 'not allowed' otherwise.
create or replace function public.hub_delete_documents(p_ids uuid[], pw text)
returns integer language plpgsql security definer set search_path = public, extensions as $$
declare n integer; h text;
begin
  h := encode(digest('hub:' || coalesce(pw, ''), 'sha256'), 'hex');
  if not public.hub_admin_ok(pw)
     and not exists (select 1 from public.hub_users u where u.owner_hash = h and u.can_delete) then
    raise exception 'not allowed' using errcode = '42501';
  end if;
  delete from public.hub_documents where id = any(p_ids);
  get diagnostics n = row_count;
  return n;
end $$;

notify pgrst, 'reload schema';
