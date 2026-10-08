# renewablevietnam.com

Static site for <https://renewablevietnam.com> — a Jekyll site plus standalone
static tools served from subfolders.

| Path | What it is |
| --- | --- |
| `/` | Card hub: Energy Projects · EV Charging · Data Center · Hub |
| `/projectenergy/` | Interactive energy potential & grid map |
| `/datacenter/` | APAC data-centre & subsea cable map |
| `/hub/` | **Library for Discussion** — curated topics + shared submissions |
| `/blog/` | Jekyll blog posts |
| `/presskit/` | Press kit |

Deployment is automatic: pushing to `main` builds with Jekyll
(`.github/workflows/jekyll-build.yml`) and publishes to GitHub Pages.

---

## The Hub's shared store (Supabase)

`/hub/` keeps its twelve editorial topics inside the page itself. Everything
visitors contribute — new topics, and views on a topic — is stored in
**Supabase** (Postgres) and only appears publicly once *approved*.

Submissions land as `pending`, so the shelf cannot be flooded with spam; you
approve or delete them in a web UI.

### One-time setup

1. Create a project at <https://supabase.com> (the free tier is enough).
2. Open **SQL Editor → New query**, paste the contents of
   [`supabase/schema.sql`](supabase/schema.sql), and run it. This creates the
   `hub_topics` and `hub_views` tables, turns on row-level security, and lets
   the public insert `pending` rows only.
3. Open **Project Settings → API** and copy two values:
   - the **Project URL**, e.g. `https://abcdefghijkl.supabase.co`
   - the **anon public** key
4. Paste them into the config block near the top of `hub/index.html`:

   ```js
   var SUPABASE_URL = "https://abcdefghijkl.supabase.co";
   var SUPABASE_ANON_KEY = "eyJhbGciOi...";
   ```

   The anon key is *meant* to be public — row-level security is what protects
   the data, not secrecy of the key.
5. Add the same two values as repository secrets so the keep-warm job can use
   them: **Settings → Secrets and variables → Actions → New repository secret**
   — create `SUPABASE_URL` and `SUPABASE_ANON_KEY`. Without them the job simply
   skips, so nothing breaks if you skip this step.

While those values are blank the Hub runs in local-only mode: the editorial
library works, and anything you add stays in your own browser.

### Moderating

Open **Table Editor → `hub_topics`** and change a row's `status` from `pending`
to `approved` to publish it. Do the same for `hub_views`. Delete junk rows
freely; you can also use `rejected` to keep a record instead of deleting.

### Why the keep-warm job

Supabase's free tier pauses a project after 7 days without activity, which would
make saving fail for occasional visitors. `.github/workflows/supabase-keepalive.yml`
pings the API once a day to keep the project awake.

---

## Editing the Hub

`hub/index.html` is a single self-contained file — no build step, no
dependencies, no CDN. It can be opened directly from disk. Revisions are kept
side by side (`rev-0.01.html`, `rev-0.02.html`, …) with the current version in
`index.html`.
