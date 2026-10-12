-- ===========================================================================
--  Renewable Viet Nam — EV charging map : shared station store (Supabase)
--  Idempotent. Reads are public; writing is only possible through
--  ev_push_stations(), which checks the admin password hash, so the publishable
--  key shipped in the page can read but never write.
--
--  The page keeps NO station data of its own: it fetches just the 40 km around
--  the visitor (lat/lng bounding box, then a true 40 km circle client-side).
--  PostgREST caps one response at 1000 rows, so the page pages with Range
--  headers — index lat and lng so those queries stay fast.
-- ===========================================================================

create extension if not exists "pgcrypto";

-- one row per physical site -------------------------------------------------
create table if not exists public.ev_stations (
  site_key    text primary key,           -- norm(name)|lat3,lng3  (lowercased, whitespace collapsed)
  name        text not null,
  lat         double precision not null,
  lng         double precision not null,
  port        text,                       -- e.g. 'Charging port: DC 120 kW'
  cpo         text,                       -- charge point operator
  addr        text,
  conn        text,                       -- e.g. 'DC:2*120+AC:3*11'
  src         text,                       -- orig | fast | slow | lq
  updated_at  timestamptz not null default now()
);
create index if not exists ev_stations_lat_idx on public.ev_stations (lat);
create index if not exists ev_stations_lng_idx on public.ev_stations (lng);
alter table public.ev_stations enable row level security;
grant select on public.ev_stations to anon, authenticated;

drop policy if exists ev_stations_read on public.ev_stations;
create policy ev_stations_read on public.ev_stations for select to anon, authenticated using (true);

-- one row describing the last Live Query run ---------------------------------
create table if not exists public.ev_sync (
  id             text primary key,
  updated_at     timestamptz not null default now(),
  stations       int,
  added          int,
  updated_count  int,
  sources        jsonb default '[]'::jsonb
);
alter table public.ev_sync enable row level security;
grant select on public.ev_sync to anon, authenticated;
drop policy if exists ev_sync_read on public.ev_sync;
create policy ev_sync_read on public.ev_sync for select to anon, authenticated using (true);

-- password-checked upsert ----------------------------------------------------
-- There is deliberately no INSERT/UPDATE policy for anon, so the only way in is
-- through this function. On conflict it keeps the existing port/operator (the
-- first source to describe the site wins) and merges the connector list, so a
-- site that appears in both the DC and AC maps ends up with both connectors
-- rather than a duplicate row.
create or replace function public.ev_push_stations(p_key text, p_rows jsonb)
returns jsonb language plpgsql security definer set search_path = public, extensions as $$
declare h text; newkeys jsonb; nnew int;
begin
  h := encode(digest(p_key, 'sha256'), 'hex');
  if h is distinct from 'b7fc3f4a204fa9ea3923fc66b02c13608652dc048f0a3430b0277fc7ea1d133e' then
    raise exception 'unauthorized' using errcode = '28000';
  end if;

  if p_rows is null or jsonb_array_length(p_rows) = 0 then
    return jsonb_build_object('ok', true, 'inserted', 0, 'keys', '[]'::jsonb);
  end if;

  with up as (
    insert into public.ev_stations (site_key, name, lat, lng, port, cpo, addr, conn, src, updated_at)
    select r.site_key, r.name, r.lat, r.lng, r.port, r.cpo, r.addr, r.conn, coalesce(r.src,'lq'), now()
    from jsonb_to_recordset(p_rows) as r(site_key text, name text, lat double precision, lng double precision,
                                          port text, cpo text, addr text, conn text, src text)
    where coalesce(r.site_key,'') <> ''
    on conflict (site_key) do update set
      name = excluded.name,
      lat  = excluded.lat,
      lng  = excluded.lng,
      addr = coalesce(nullif(excluded.addr,''), public.ev_stations.addr),
      conn = case
               when public.ev_stations.conn is null or public.ev_stations.conn = '' then excluded.conn
               when excluded.conn is null or excluded.conn = '' then public.ev_stations.conn
               when position(excluded.conn in public.ev_stations.conn) > 0 then public.ev_stations.conn
               else public.ev_stations.conn || '+' || excluded.conn
             end,
      updated_at = now()
    returning site_key, (xmax = 0) as is_new
  )
  select coalesce(jsonb_agg(site_key) filter (where is_new), '[]'::jsonb),
         count(*) filter (where is_new)::int
    into newkeys, nnew
    from up;

  insert into public.ev_sync (id, updated_at, stations)
  select 'latest', now(), count(*)::int from public.ev_stations
  on conflict (id) do update set updated_at = now(), stations = excluded.stations;

  return jsonb_build_object('ok', true, 'inserted', coalesce(nnew,0), 'keys', newkeys);
end $$;

revoke all on function public.ev_push_stations(text, jsonb) from public;
grant execute on function public.ev_push_stations(text, jsonb) to anon, authenticated;

-- wipe every station (admin only; used to re-seed from scratch) --------------
create or replace function public.ev_reset_stations(p_key text)
returns jsonb language plpgsql security definer set search_path = public, extensions as $$
declare h text;
begin
  h := encode(digest(p_key, 'sha256'), 'hex');
  if h is distinct from 'b7fc3f4a204fa9ea3923fc66b02c13608652dc048f0a3430b0277fc7ea1d133e' then
    raise exception 'unauthorized' using errcode = '28000';
  end if;
  delete from public.ev_stations where site_key is not null;
  delete from public.ev_sync where id is not null;
  return jsonb_build_object('ok', true);
end $$;

revoke all on function public.ev_reset_stations(text) from public;
grant execute on function public.ev_reset_stations(text) to anon, authenticated;

-- ---------------------------------------------------------------------------
--  Loading the stations
--
--  The 20,822 rows were seeded once from the three Google My Maps exports
--  (EV-Charging-Map/index.html at rev-0.44) using authenticated REST inserts,
--  then the anon INSERT policy that allowed it was dropped. To re-seed, bulk
--  insert in batches of 500 with `Prefer: resolution=merge-duplicates` while a
--  temporary `ev_stations_load` policy exists, then drop that policy again.
--  After the first load, ordinary refreshes go through the admin console's
--  Live Query, which calls ev_push_stations().
--
--  site_key must match the browser exactly:
--    lower(trim(name)) with runs of whitespace collapsed, then '|', then
--    lat and lng each rounded to 3 decimals as "d.ddd".
-- ---------------------------------------------------------------------------
