# ⚡ Renewable Viet Nam

[![Live Site](https://img.shields.io/badge/Live%20Site-renewablevietnam.com-059669?style=flat&logo=google-chrome&logoColor=white)](https://renewablevietnam.com)
[![Jekyll](https://img.shields.io/badge/Jekyll-4.3-CC0000?style=flat&logo=jekyll&logoColor=white)](https://jekyllrb.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.x-38B2AC?style=flat&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![Supabase](https://img.shields.io/badge/Backend-Supabase%20%2F%20Postgres-3ECF8E?style=flat&logo=supabase&logoColor=white)](https://supabase.com/)
[![GitHub Pages](https://img.shields.io/badge/Deployed%20on-GitHub%20Pages-222222?style=flat&logo=github&logoColor=white)](https://pages.github.com/)

> **Tracking Viet Nam's renewable energy transition — progress, infrastructure, projects, and outlook to 2030.**

**Renewable Viet Nam** is an open data and interactive geospatial intelligence platform providing transparent, accessible data on Vietnam's clean energy transition. The platform monitors utility-scale power assets, EV charging networks, hyperscale data centers, and the regulatory landscape under the National Power Development Plan 8 (PDP8).

---

## 🌟 Key Pillars & Features

### 1. 🗺️ Energy Projects Map (`/projectenergy/`)
* **Interactive Geospatial Registry:** Nationwide interactive map visualizing utility-scale energy projects across Viet Nam.
* **Multi-Source Generation Tracking:** Solar (rooftop & utility-scale), Onshore & Offshore Wind, Hydro, Biomass, LNG, and Battery Energy Storage Systems (BESS).
* **Granular Project Data:** Nameplate capacity (MW), operational status (Operating, Under Construction, Planned, Feasibility), commercial operating dates (COD), developers, and regional grid connection points.

### 2. 🔌 EV Charging Network (`/evcharging/`)
* **Nationwide Infrastructure Directory:** Tracks public and private electric vehicle charging stations across all 63 provinces and municipalities.
* **Operator & Hardware Metadata:** Aggregates multi-network deployment data (VinFast, Charge+, EV ONE, PV Power, etc.), connector standards (CCS2, Type 2, GB/T, CHAdeMO), and charging power tiers (AC slow to DC ultra-fast).
* **Live Aggregated Telemetry:** Powered by Supabase PostgREST queries with client-side geospatial clustering.

### 3. 🏢 APAC Data Centers (`/datacenter/`)
* **Digital Infrastructure Demand:** Catalog of enterprise and colocation data centers in Vietnam and across APAC.
* **Energy Footprint & Sustainability:** Monitors power capacity allocations (MW), Power Usage Effectiveness (PUE) metrics, and alignment with Direct Power Purchase Agreements (DPPA) and RE100 commitments.

### 4. 📚 Policy & Knowledge Hub (`/hub/` & `_posts/`)
* **Regulatory & Market Insights:** Articles, policy analysis, and updates on Decree 80/2024/ND-CP (DPPA mechanism), PDP8 implementation plans, feed-in-tariffs (FIT), and transmission grid investments.

---

## 🏗️ Architecture & Technology Stack

| Layer | Technologies |
| :--- | :--- |
| **Static Site Generator** | [Jekyll 4.3](https://jekyllrb.com/) with Rouge syntax highlighter and Kramdown |
| **Theme & UI** | Tailored Jasper2 theme with custom Apple SF Pro typography and Tailwind CSS |
| **Mapping & GIS** | Leaflet.js, custom vector tiles, coordinate projection, responsive popups |
| **Database & API** | [Supabase](https://supabase.com/) (PostgreSQL 15+, `pgcrypto`, PostgREST API) |
| **Security & Access** | Row-Level Security (RLS) — read-only public access via publishable anon key |
| **ETL & Data Pipeline** | Node.js ESM scripts (`scripts/seed_energy.mjs`) for database synchronization |
| **Hosting & CDN** | GitHub Pages with custom domain DNS routing (`renewablevietnam.com`) |

---

## 📂 Repository Structure

```text
RenewableVietNam/
├── _config.yml          # Jekyll site configuration and metadata
├── _data/               # YAML/JSON data files for navigation and references
├── _includes/           # Modular HTML templates and partials
├── _layouts/            # Page and post layout templates
├── _plugins/            # Custom Jekyll plugins (tags, pagination, author pages)
├── _posts/              # Markdown articles and policy briefs
├── assets/              # Static assets (brand SVG logos, favicons, stylesheets)
├── datacenter/          # APAC Data Center directory & visualization interface
├── evcharging/          # EV charging stations map and revision history
├── projectenergy/       # Energy projects GIS map interface and database
├── map/                 # Canonical redirect to /projectenergy/
├── hub/                 # Resource collection and analysis hub
├── scripts/             # Data migration and database seeding utilities
│   └── seed_energy.mjs  # Node.js ETL script to sync database from local fixtures
├── supabase/            # SQL schemas and Row-Level Security definitions
│   ├── energy_schema.sql# PostgreSQL schema for energy projects
│   ├── ev_schema.sql    # PostgreSQL schema for EV charging stations
│   └── schema.sql       # Consolidated database definitions
├── CNAME                # Custom domain configuration (renewablevietnam.com)
├── Gemfile              # Ruby dependencies
└── README.md            # Repository documentation
```

---

## 🚀 Getting Started Locally

### Prerequisites
- **Ruby:** `3.0+` (with Bundler: `gem install bundler`)
- **Node.js:** `18.0+` (for ETL and database scripts)

### 1. Clone the Repository
```bash
git clone https://github.com/Qking232/RenewableVietNam.git
cd RenewableVietNam
```

### 2. Install Ruby Dependencies
```bash
bundle install
```

### 3. Run the Local Development Server
```bash
bundle exec jekyll serve --livereload
```
Visit `http://localhost:4000` in your browser.

---

## 🗄️ Database Setup & Seeding

The platform utilizes a public read-only model backed by Supabase with Row Level Security (RLS).

### Database Initialization
1. In your **Supabase Dashboard**, navigate to the **SQL Editor**.
2. Run [`supabase/energy_schema.sql`](supabase/energy_schema.sql) and [`supabase/ev_schema.sql`](supabase/ev_schema.sql).
3. The schema sets up table structures, UUID generators (`pgcrypto`), indexes, and applies `anon` SELECT-only policies.

### Running the Seed Script
To populate or refresh project records:

**PowerShell (Windows):**
```powershell
$env:SUPABASE_SECRET_KEY = "sb_secret_your_service_role_key"
node scripts/seed_energy.mjs --dry-run    # Preview operations
node scripts/seed_energy.mjs              # Apply updates
```

**Bash (Linux / macOS):**
```bash
export SUPABASE_SECRET_KEY="sb_secret_your_service_role_key"
node scripts/seed_energy.mjs --dry-run
node scripts/seed_energy.mjs
```

> **Security Note:** Never commit `SUPABASE_SECRET_KEY` or `service_role` tokens to source control. The frontend exclusively consumes the public anonymous key.

---

## 🤝 Contributing

Contributions to dataset accuracy, interface enhancements, and policy analyses are welcome!

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/add-project-data`).
3. Commit your changes (`git commit -m 'feat: add Ninh Thuan offshore wind farm details'`).
4. Push to the branch (`git push origin feature/add-project-data`).
5. Open a Pull Request.

---

## 📬 Contact & Feedback

- **Website:** [renewablevietnam.com](https://renewablevietnam.com)
- **General Inquiries:** [info@renewablevietnam.com](mailto:info@renewablevietnam.com)
- **Maintainer:** [@Qking232](https://github.com/Qking232)

---

## 📄 License

This repository is maintained for open data and educational purposes. Underlying Jekyll themes and libraries adhere to their respective open-source licenses (Jasper2 MIT).
