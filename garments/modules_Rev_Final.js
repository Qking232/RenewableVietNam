/**
 * Executive Portal Module Manifest - Rev_Final
 * Target: Garments Company Regional Engineering & Capital Projects Portal
 * Architecture: Executive 6-Segment Simultaneous Visibility Grid
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
    id: "domain2_utilities",
    tag: "DOMAIN 2",
    shortTitle: "Plant & Utilities",
    category: "Core Engineering",
    title: "Domain 2: Plant Engineering & Utilities",
    description: "35,000 m² 2.5D Isometric Plant Map, 15 TPH Biomass Steam, 1,573 CFM VFD Compressed Air, 35 ACH Celdek HVAC, and 1,200 m³/d ZLD ETP.",
    badge: "Engineering",
    file: "modules/domain2_utilities_engineering.html"
  },
  {
    id: "domain3_esg",
    tag: "DOMAIN 3",
    shortTitle: "Green & Solar",
    category: "Sustainability & Energy",
    title: "Domain 3: Green Energy & Sustainability",
    description: "2.80 MWp Rooftop Solar PV, -10,838 tCO₂e/yr Net Carbon Abatement, LEED v4 BD+C Platinum (84 Pts), and Higg FEM 4.0 Standards.",
    badge: "Sustainability",
    file: "modules/domain3_esg_leed_solar.html"
  },
  {
    id: "domain4_capex",
    tag: "DOMAIN 4",
    shortTitle: "Cost & Contracts",
    category: "Commercial & Controls",
    title: "Domain 4: Project Cost & Contracts",
    description: "$14.50M BAC Breakdown, EVM S-Curve Progress Verification, 7-Year Operating DCF Valuation ($1.85M NPV, 15.65% IRR), and FIDIC Risk Allocation.",
    badge: "Cost & Contracts",
    file: "modules/domain4_capex_calsheet.html"
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
