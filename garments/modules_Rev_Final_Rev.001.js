/**
 * Executive Portal Module Manifest - Rev_Final
 * Target: Garments Company Regional Engineering & Capital Projects Portal
 * Architecture: Executive 7-Module Portfolio Grid
 */
window.PORTAL_MODULES = [
  {
    id: "master_governance",
    tag: "FRAMEWORK",
    shortTitle: "Project Delivery",
    category: "Executive Governance",
    title: "Project Delivery Framework",
    description: "The '5+3' Capital Delivery System: 6-Stage Gate Process, 10-Role RACI Matrix, and 8 Integrated Execution Pillars.",
    badge: "Framework",
    file: "modules/master_project_governance.html"
  },
  {
    id: "domain1_permitting",
    tag: "DOMAIN 1",
    shortTitle: "Permits & Legal",
    category: "Statutory Compliance",
    title: "Domain 1: Permits & Legal Approvals",
    description: "Vietnam Land Use Right (Sổ Đỏ), 1/500 Master Plan, TKCS Basic Design, QCVN 06:2022 Fire Safety, Phased GPXD Móng/Thân, and GPMT Licensing.",
    badge: "Permits",
    file: "modules/domain1_pccc_permitting.html"
  },
  {
    id: "domain2_engineering_esg",
    tag: "DOMAIN 2",
    shortTitle: "Plant & ESG Tech",
    category: "Core Engineering & ESG",
    title: "Domain 2: Plant Engineering, Clean Utilities & ESG Infrastructure",
    description: "35,000 m² 2.5D Plant Map, 15 TPH Biomass Steam, 1,573 CFM VFD Air, 2.80 MWp Solar + 1.2 MWh BESS, 180 km/h PEB Typhoon, AWS Water & LEED Platinum (84 Pts).",
    badge: "Engineering & ESG",
    file: "modules/domain2_utilities_engineering.html"
  },
  {
    id: "domain3_capex",
    tag: "DOMAIN 3",
    shortTitle: "Cost & Contracts",
    category: "Commercial & Controls",
    title: "Domain 3: Project Cost & Contracts",
    description: "$14.50M BAC Breakdown, EVM S-Curve Progress Verification, 7-Year Operating DCF Valuation ($1.85M NPV, 15.65% IRR), and FIDIC Risk Allocation.",
    badge: "Cost & Contracts",
    file: "modules/domain4_capex_calsheet.html"
  },
  {
    id: "domain4_construction",
    tag: "DOMAIN 4",
    shortTitle: "Physical Construction",
    category: "Civil, PEB & MEP Execution",
    title: "Domain 4: Physical Construction & Site Execution",
    description: "Deep Piling Substructure, 180 km/h Typhoon PEB Steel Superstructure, Building Envelope, MEP Rough-in, 3-Tier ITP QA/QC Gates, and Zero-Harm HSE Protocol.",
    badge: "Construction",
    file: "modules/domain4_physical_construction.html"
  },
  {
    id: "domain5_handover",
    tag: "DOMAIN 5",
    shortTitle: "T&C Handover",
    category: "Operational Readiness",
    title: "Domain 5: Testing, Commissioning & Handover",
    description: "Integrated T&C Protocols (ASHRAE 0-2019), Decree 06/2021 Statutory Hoan Cong, 9.8s Blackout ATS Transfer, FIDIC Clause 10.1 TOC, and $725k DLP Bond.",
    badge: "T&C Handover",
    file: "modules/domain5_commissioning_handover.html"
  },
  {
    id: "bod_charter",
    tag: "BOARD DOSSIER",
    shortTitle: "Board Report",
    category: "Executive Authorization",
    title: "Board Report & Project Charter",
    description: "Executive Capital Authorization Dossier: Technical Sizing, Financial Sensitivity Stress Testing, and Formal Board Resolution.",
    badge: "Board Report",
    file: "modules/bod_capex_charter_report.html"
  }
];
