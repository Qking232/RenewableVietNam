# Institutional Master Specification: Renewable Viet Nam Infrastructure Platform

## Document Metadata
- **Platform**: `renewablevietnam.com`
- **Apex Domain**: `renewablevietnam.com`
- **Cloudflare Zone ID**: `eed02d9917c1a0c6144972136e836eba`
- **Cloudflare Account ID**: `a17978d12dc9d62ca76f7712fe8f758c`
- **Primary Repository**: `https://github.com/Qking232/RenewableVietNam.git`
- **Mirror Repository**: `https://github.com/Qking232/Qking232.github.io.git`
- **Database Engine**: Supabase Cloud PostgreSQL (`https://nkkwegvplpozirrjcxsn.supabase.co`)

---

## 1. Executive Mission & Target Audiences
`Renewable Viet Nam` is engineered as Vietnam's premier institutional energy transition, industrial infrastructure, and statutory compliance intelligence terminal. The platform serves three distinct commercial and industrial personas:

1. **Multinational RE100 Corporate Offtakers**:
   - Corporations (Samsung, Foxconn, Apple, Lego, Amkor, Intel) requiring high-volume clean energy contracts to comply with EU Carbon Border Adjustment Mechanism (CBAM), corporate ESG mandates, and supply chain decarbonization.
   - Core Need: Decree 80/2024/NĐ-CP DPPA bilateral tariff calculations, grid wheeling corridor analysis, and substation interconnection clearance.

2. **Global Infrastructure Funds & IPP Developers**:
   - Institutional equity investors (Copenhagen Infrastructure Partners, ACWA Power, Sembcorp, Actis) and multilateral development banks (ADB, IFC, JICA).
   - Core Need: Statutory PDP8 project quota tracking (Decision 500/QĐ-TTg, Decision 262/QĐ-TTg), M&A secondary deal screening, curtailment risk assessment, and licensing bankability audits.

3. **Engineering, Procurement & Construction (EPC) Contractors & Industrial Park Operators**:
   - Developers constructing utility-scale plants, factory rooftop solar, and eco-industrial parks (Decree 35/2022/NĐ-CP).
   - Core Need: Substation tie-in capacity, high-voltage transformer logistics, and electrical load archetype modeling.

---

## 2. Multi-Gateway Edge Routing Architecture

The platform routes user traffic across an Apex Executive Cockpit and five specialized edge gateways via Cloudflare Workers (`subdomain_gateway_worker.js`):

```
Hostname                            Origin Path       Domain Function
----------------------------------------------------------------------------------------------------------------------
renewablevietnam.com                /                 Apex Executive Cockpit & Universal Telemetry
energy.renewablevietnam.com         /energy/          PDP8 Clean Energy Registry & Transmission Grid
industrial.renewablevietnam.com     /industrial/      Industrial Parks (446 IP), Eco-IPs & Load Archetypes
ev.renewablevietnam.com             /evcharging/      National EV Charging Stations (22,055 CPO Points)
legal.renewablevietnam.com          /invm/            Decree 80 DPPA Legal Compliance & M&A Deal Room
invest.renewablevietnam.com         /invm/            Investment Portal Alias (Permanent Sync)
project.renewablevietnam.com        /project/         Project Delivery & Industrial Construction EPC
```

---

## 3. Detailed Portal Specifications

### A. Energy Portal (`energy.renewablevietnam.com`)
- **Statutory Mandate Baseline**: Vietnam Power Development Plan VIII (PDP8) approved under Decision 500/QĐ-TTg with implementation plan under Decision 262/QĐ-TTg.
- **Key Metrics Tracked**:
  - Clean Baseload: 80,612 MW active commercial baseload (53.6% of statutory mandate).
  - 2030 Mandate Target: 150,489 MW.
  - Pipeline Delta Gap: +69,877 MW mandated for 2026-2030 commercial operation date (COD).
  - Tracked Facilities: 960 utility-scale generating facilities geocoded across 63 provinces.
  - Transmission Backbone: 65,566 km transmission circuits, 1,915 substations (500kV, 220kV, 110kV).
- **Core Modules**:
  1. 8-Pillar Executive Market Intelligence Matrix.
  2. 14 Strategic Pillars of Energy Transition (Offshore Wind, Onshore Wind, Solar PV, Hydro/BESS, LNG, Biomass, Regional Interties, Digital SCADA, DPPA, VWEM Power Market, Hydrogen/Ammonia, Carbon Market/ETS, DSM/SMR).
  3. Interactive Cartographic GIS Viewer (Leaflet map displaying substation pooling points and generation clusters).
  4. Node Telemetry Dossier & 500kV Power Flow Simulator.

### B. Industrial Portal (`industrial.renewablevietnam.com`)
- **Scope**: Complete geodatabase of 446 industrial parks across Northern, Central, and Southern economic corridors.
- **Core Modules**:
  1. Power Demand Archetype Selector:
     - Semiconductor Fab: High baseload, uninterrupted power supply, zero voltage sag tolerance.
     - Hyperscale Data Center: 50-150 MW load, PUE < 1.3, multi-substation dual feed.
     - Green Steel / Heavy Industry: Direct high-voltage induction melting, demand response flexibility.
     - Light Manufacturing & Assembly: High daytime peak load, optimized for rooftop solar self-consumption.
  2. National Industrial Park Registry: Geocoded directory with occupancy rates, developer entity, power substation tie-in, and water treatment capacity.
  3. Rooftop Solar & Self-Consumption Sizing: Sizing model aligned with Decree 135/2024/NĐ-CP.

### C. EV Tech Portal (`ev.renewablevietnam.com`)
- **Scope**: Comprehensive national registry of 22,055 public and commercial EV charging stations.
- **Core Modules**:
  1. CPO Directory & Map: VinFast (V-Green), EV ONE, Charge+, Porsche, ABB, EBOOST.
  2. Connector Breakdown: CCS2, Type 2, GB/T, CHAdeMO.
  3. Grid Impact Matrix: Coincident peak load simulation for urban distribution substations.

### D. Legal & Investment M&A Portal (`legal.renewablevietnam.com`)
- **Scope**: Statutory regulatory hub and transaction due diligence engine.
- **Core Modules**:
  1. Decree 80/2024/NĐ-CP DPPA Framework:
     - Direct Private Line: Physical direct connection between renewable plant and consumer.
     - National Grid Wheeling: Bilateral Contract for Difference (CfD) via spot market pool (VWEM).
  2. Statutory Due Diligence Audit Matrix (IRC, ERC, EIA, PCCC, Grid Interconnection, Land Rights).
  3. Decision 262/QĐ-TTg Provincial Allocation Tracker.
  4. M&A Deal Flow & Asset Transaction Registry.

### E. Project Delivery Portal (`project.renewablevietnam.com`)
- **Scope**: Physical EPC execution, supply chain logistics, and substation interconnection construction.

### F. Apex Executive Cockpit (`renewablevietnam.com`)
- **Scope**: Universal master dashboard synthesizing cross-gateway intelligence, macro KPIs, and unified search.

---

## 4. Technical Architecture & Data Engine

```
+-------------------------------------------------------------------------------+
|                             CLIENT BROWSER (EDGE)                             |
|  - HTML5 / Tailwind CSS / Vanilla JS / Leaflet GIS Cartography                |
|  - Compressed IndexedDB Cache (RVN_Storage) via DecompressionStream('gzip')   |
|  - SWR (Stale-While-Revalidate) In-Memory Query Engine                        |
+-------------------------------------------------------------------------------+
                                      |
                           HTTPS via Edge Proxy
                                      v
+-------------------------------------------------------------------------------+
|                             CLOUDFLARE EDGE LAYER                             |
|  - Zone ID: eed02d9917c1a0c6144972136e836eba                                  |
|  - Workers: subdomain_gateway_worker.js, invest_worker.js                     |
|  - Reverse proxy, URL canonicalization, and zero-downtime routing             |
+-------------------------------------------------------------------------------+
                   |                                           |
       Origin Fetch (GitHub Pages)                    REST API & JSON Stream
                   v                                           v
+---------------------------------------+   +-----------------------------------+
|      DUAL GITHUB STATIC REPOSITORIES  |   |     SUPABASE POSTGRESQL ENGINE    |
|  - RenewableVietNam (Primary)         |   |  - ev_stations (22,055 records)   |
|  - Qking232.github.io (Mirror)        |   |  - energy_projects (960 records)  |
|  - Automated Release Train via Git    |   |  - industrial_hubs (446 records)  |
|  - Sequential Revisions (_Rev.xxx)    |   |  - pdp8_fuel_targets              |
+---------------------------------------+   +-----------------------------------+
```

---

## 5. Quantitative Progress Tracking Framework

Progress is measured systematically across four integrated operational layers:

### Layer 1: Super Productivity Task & Time Engine
- **Workspace**: Super Productivity REST API on `localhost:3876`.
- **Project**: `f3qXADKDasmPut2jy69s6` / `CUkYos3qQPgiiWT3ksjw1`.
- **Hierarchy**: Parent Milestone Task -> Modular Subtasks ($\le 90$ mins each) with duration estimates -> Approval Gates (`🟢 [APPROVE]` / `🔴 [REWORK]`).

### Layer 2: Dual-Remote Git Release Train & Non-Destructive Versioning
- **Commit Pattern**: Institutional technical commit messages adhering to Conventional Commits.
- **Revisioning**: Production files versioned sequentially (`index_Rev.xxx.html`) before refactors.
- **Deployment**: Synchronous push to both remotes followed by global Cloudflare purge.

### Layer 3: Automated Health & Syntax Verification Suite
- **Health Probes**: Automated multi-domain HTTP status, latency, and content integrity verification via `scripts/edge_health_probe.py`.
- **Syntax Integrity**: Pre-deployment DOM tag validation.

### Layer 4: Public Platform Health & Execution Burndown Radar
- **Public URL**: `https://renewablevietnam.com/roadmap/`
- **Telemetry**: Real-time display of tracked megawatts, database sync timestamps, active feature matrix, and execution progress.
