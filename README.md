# renewablevietnam.com

Static site for <https://renewablevietnam.com> — a Jekyll site plus standalone
static tools served from subfolders.

| Path | What it is |
| --- | --- |
| `/` | Card hub: Energy Projects · EV Charging · Data Center · Hub |
| `/projectenergy/` | Interactive energy potential & grid map |
| `/datacenter/` | APAC data-centre & subsea cable map |
| `/hub/` | **The Library** — documents (reports, datasets, policy, maps) with files, summaries and comments |
| `/blog/` | Jekyll blog posts |
| `/presskit/` | Press kit |
| `/old/` | Archive: previous page revisions, the retired `worldmap/` build and `presskit-src/`. Not part of the site — kept for reference only. |

Deployment is automatic: pushing to `main` builds with Jekyll
(`.github/workflows/jekyll-build.yml`) and publishes to GitHub Pages.

---

## The Library's shared store (Supabase)

`/hub/` keeps its twelve editorial documents inside the page itself. Everything
visitors contribute — a new document, its **file**, and comments on a document —
is stored in **Supabase** and, in the current configuration, **published
immediately** (no review queue).

| What | Where |
| --- | --- |
| Document metadata (title, type, collection, summary, points, refs…) | Postgres table `hub_documents` |
| The document **file** (PDF, Office, CSV, image…) | Storage bucket `hub-docs` (public) |
| Comments on a document | Postgres table `hub_views` (`topic_id` = document id) |

Files are uploaded straight from the browser to the `hub-docs` bucket (25 MB per
file) and referenced by path; the page builds the public download URL from the
bucket. Re-run [`supabase/schema.sql`](supabase/schema.sql) to create the table,
the bucket and its read/upload policies — it is idempotent.

### Setup status

This is already configured. For the record, setup was:

1. A project was created at <https://supabase.com> (free tier).
2. [`supabase/schema.sql`](supabase/schema.sql) was run in **SQL Editor → New
   query**. It creates the `hub_topics` and `hub_views` tables, turns on
   row-level security, and lets the public insert `pending` rows only.
3. Two values were copied from **Settings → API Keys** and pasted into the
   config block near the top of `hub/index.html`:

   ```js
   var SUPABASE_URL = "https://nkkwegvplpozirrjcxsn.supabase.co";
   var SUPABASE_ANON_KEY = "sb_publishable_…";
   ```

   Publishable keys (`sb_publishable_…`) are *meant* to be public — row-level
   security is what protects the data, not secrecy of the key. Never put a
   secret key (`sb_secret_…`) in the page: it bypasses all security.

   **Heads-up on header format:** publishable/secret keys are not JWTs, so they
   are sent on the `apikey` header only. Adding `Authorization: Bearer` makes
   PostgREST try to parse the key as a JWT and return 401. Legacy `anon` JWTs
   (`eyJ…`) need *both* headers — `hub/index.html` handles either automatically.

If you ever rotate the key, update it in two places: `hub/index.html` and
`.github/workflows/supabase-keepalive.yml`.

### Submissions are auto-approved

New topics and views publish immediately — there is no review queue. To remove
something, open **Table Editor → `hub_topics`** (or `hub_views`) and delete the
row, or set its `status` to `rejected` to hide it while keeping a record.

Going back to moderated submissions means editing `supabase/schema.sql`: set the
two `status` column defaults to `'pending'` and the two INSERT policies'
`WITH CHECK` to `(status = 'pending')`, then re-run the file. Also set
`AUTO_APPROVE = false` in `hub/index.html` so the wording matches.

Because nothing screens submissions any more, `supabase/schema.sql` carries an
optional per-IP throttle (10 submissions per hour) at the bottom, commented out.
Uncomment that block and run the file if the shelf starts collecting spam.

### Context images (optional)

Topics can carry up to three context images. The Hub scales each one down in the
browser and stores it as a data-URL string in the `hub_topics.images` jsonb
column. Re-run [`supabase/schema.sql`](supabase/schema.sql) (it is idempotent) to
add that column; until it exists the page still posts topics — it just retries
without the images so nothing else breaks. Your own topics keep their images in
the browser and are unaffected either way.

### Why the keep-warm job

Supabase's free tier pauses a project after 7 days without activity, which would
make saving fail for occasional visitors. `.github/workflows/supabase-keepalive.yml`
pings the API once a day to keep the project awake.

---

## Editing the Library

`hub/index.html` is a single self-contained file — no build step, no
dependencies, no CDN. It can be opened directly from disk. Revisions are kept
side by side under `old/hub/` (`old/hub/rev-0.01.html`, `old/hub/rev-0.02.html`,
…) with the current version in `index.html`. `old/hub/rev-0.10.html` is the first
document-library build; `old/hub/rev-0.11.html` makes each shelf row open the
document in **its own window** (`/hub/#/doc/<id>`) as a full page, with the
inline preview panel removed.
Without Supabase keys it runs local-only (small files inline, export/import as
JSON); with them, documents and files are shared for everyone.

The same convention applies to every page: earlier revisions of the homepage,
`/projectenergy/`, and the retired `worldmap/` map all live under `old/` (mirroring
their original folder structure), with the current version in place as `index.html`.
`old/presskit-src/` holds the presskit.html generator sources and unused theme
assets are parked in `old/assets/`.
