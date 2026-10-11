-- ===========================================================================
--  Renewable Viet Nam — EV charging map : shared sync store  (Supabase/Postgres)
--  Idempotent. Read is public; writing is only possible through ev_push(), which
--  checks the admin password hash, so the publishable key alone cannot write.
-- ===========================================================================

create extension if not exists "pgcrypto";

-- stations that differ from the copy baked into the page (new or updated) ----
create table if not exists public.ev_delta (
  id          text primary key,
  updated_at  timestamptz not null default now(),
  kind        text not null default 'upd',
  name        text not null,
  lat         double precision not null,
  lng         double precision not null,
  port        text,
  cpo         text,
  addr        text,
  conn        text
);
alter table public.ev_delta enable row level security;

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

grant select on public.ev_delta to anon, authenticated;
grant select on public.ev_sync  to anon, authenticated;

drop policy if exists ev_delta_read on public.ev_delta;
create policy ev_delta_read on public.ev_delta for select to anon, authenticated using (true);
drop policy if exists ev_sync_read on public.ev_sync;
create policy ev_sync_read  on public.ev_sync  for select to anon, authenticated using (true);

-- password-checked write (no direct INSERT/UPDATE policy for anon) -----------
create or replace function public.ev_push(p_key text, p_rows jsonb, p_meta jsonb default '{}'::jsonb)
returns jsonb language plpgsql security definer set search_path = public, extensions as $$
declare h text; n int := 0;
begin
  h := encode(digest(p_key, 'sha256'), 'hex');
  if h is distinct from 'b7fc3f4a204fa9ea3923fc66b02c13608652dc048f0a3430b0277fc7ea1d133e' then
    raise exception 'unauthorized' using errcode = '28000';
  end if;

  if p_rows is not null and jsonb_array_length(p_rows) > 0 then
    insert into public.ev_delta (id, updated_at, kind, name, lat, lng, port, cpo, addr, conn)
    select r.id, now(), coalesce(r.kind,'upd'), r.name, r.lat, r.lng, r.port, r.cpo, r.addr, r.conn
    from jsonb_to_recordset(p_rows) as r(id text, kind text, name text, lat double precision,
                                         lng double precision, port text, cpo text, addr text, conn text)
    where coalesce(r.id,'') <> ''
    on conflict (id) do update set
      updated_at = now(), kind = excluded.kind, name = excluded.name,
      lat = excluded.lat, lng = excluded.lng, port = excluded.port,
      cpo = excluded.cpo, addr = excluded.addr, conn = excluded.conn;
    get diagnostics n = row_count;
  end if;

  insert into public.ev_sync (id, updated_at, stations, added, updated_count, sources)
  values ('latest', now(),
          coalesce((p_meta->>'stations')::int, 0),
          coalesce((p_meta->>'added')::int, 0),
          coalesce((p_meta->>'updated')::int, 0),
          coalesce(p_meta->'sources', '[]'::jsonb))
  on conflict (id) do update set
    updated_at = now(), stations = excluded.stations, added = excluded.added,
    updated_count = excluded.updated_count, sources = excluded.sources;

  return jsonb_build_object('ok', true, 'rows', n, 'at', now());
end $$;

revoke all on function public.ev_push(text, jsonb, jsonb) from public;
grant execute on function public.ev_push(text, jsonb, jsonb) to anon, authenticated;

-- clear every synced change (admin only) -------------------------------------
create or replace function public.ev_reset(p_key text)
returns jsonb language plpgsql security definer set search_path = public, extensions as $$
declare h text;
begin
  h := encode(digest(p_key, 'sha256'), 'hex');
  if h is distinct from 'b7fc3f4a204fa9ea3923fc66b02c13608652dc048f0a3430b0277fc7ea1d133e' then
    raise exception 'unauthorized' using errcode = '28000';
  end if;
  delete from public.ev_delta;
  delete from public.ev_sync;
  return jsonb_build_object('ok', true);
end $$;

revoke all on function public.ev_reset(text) from public;
grant execute on function public.ev_reset(text) to anon, authenticated;
