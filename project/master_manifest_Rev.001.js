/**
 * Master Project Directorate & Engineering Registry - Rev.001
 * Target: project.renewablevietnam.com
 * Multi-Project Architecture: Garments, Hyperscale Data Center, and Extensible Future Verticals
 */
window.PROJECTS_REGISTRY = {
  garments: {
    id: "garments",
    name: "Garments Regional Capital Projects",
    shortName: "Garments & Light Industry",
    code: "GARMENTS",
    badge: "Active Operational Project",
    badgeColor: "emerald",
    subtitle: "Regional Engineering & Capital Projects Architecture | Multi-Site Governance (Vietnam & Sri Lanka)",
    sector: "Light Manufacturing Decarbonization",
    metrics: [
      { label: "BAC", value: "$14.50M USD" },
      { label: "Solar / BESS", value: "2.80 MWp + 1.2 MWh" },
      { label: "Efficiency", value: "LEED Platinum (84 Pts)" },
      { label: "Permits", value: "QCVN 06:2022 PCCC" }
    ],
    defaultModule: "charter_report",
    standaloneUrl: "/garments/",
    modules: [
      {
        id: "charter_report",
        tag: "CHARTER",
        shortTitle: "BOD Executive Report",
        category: "Board of Directors",
        title: "BOD CAPEX Project Charter Report",
        description: "Board-Level Executive Investment & Governance Charter: Capital Allocation, IRR/NPV Sensitivity, Permitting Timelines & Enterprise Risk Matrix.",
        badge: "BOD Charter",
        file: "modules/bod_capex_charter_report.html"
      },
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
        category: "Commissioning & Closeout",
        title: "Domain 5: Commissioning, Operations & Handover",
        description: "Level 1-5 Commissioning Sequence, Cold/Hot Commissioning Protocols, Commercial COD Handover, and Operational As-Built Asset Transfer.",
        badge: "Commissioning",
        file: "modules/domain5_commissioning_handover.html"
      }
    ]
  },

  dc: {
    id: "dc",
    name: "Hyperscale Data Center Campus (45 MW)",
    shortName: "Hyperscale Data Center",
    code: "DATACENTER",
    badge: "Tier III / 45 MW Campus",
    badgeColor: "sky",
    subtitle: "Hyperscale Data Center Executive Portal | 45 MW Critical IT Capacity | Tier III Concurrently Maintainable",
    sector: "Digital Infrastructure & High-Density Compute",
    metrics: [
      { label: "BAC", value: "$180.00M USD" },
      { label: "PUE", value: "1.280 Design" },
      { label: "Power", value: "Dual 110kV / 22kV" },
      { label: "Standard", value: "ANSI/TIA-942 Rated 3" }
    ],
    defaultModule: "charter_report",
    standaloneUrl: "/dc/",
    modules: [
      {
        id: "charter_report",
        tag: "CHARTER",
        shortTitle: "BOD Executive Report",
        category: "Board of Directors",
        title: "BOD CAPEX Project Charter Report",
        description: "Comprehensive 45 MW Hyperscale DC Investment Charter: Stage-Gate Authorization, Financial Projections, Power Allocation & Execution Roadmap.",
        badge: "BOD Charter",
        file: "/dc/modules/bod_capex_charter_report_Rev.003.html"
      },
      {
        id: "master_governance",
        tag: "FRAMEWORK",
        shortTitle: "Project Delivery",
        category: "Executive Governance",
        title: "Project Delivery Framework",
        description: "The '5+3' Capital Delivery System: 24-Month Master Plan, 6 BOD Submission Stage Gates, 30 Statutory Deliverables & Capital Tranches.",
        badge: "Framework",
        file: "/dc/modules/master_project_governance_Rev.003.html"
      },
      {
        id: "domain1_permitting",
        tag: "DOMAIN 1",
        shortTitle: "Permits & Statutory",
        category: "Statutory Compliance",
        title: "Domain 1: Permits, Grid Tie & Statutory Approvals",
        description: "Dual-Track Fast-Track GPXD (4.5 Mo Saved), 12 Master Licenses, QCVN 06:2022 PCCC Fire Design, Decree 08/2022 GPMT, and EVN 110kV Dual-Substation DPPA Protocol.",
        badge: "Permits",
        file: "/dc/modules/domain1_statutory_permitting_Rev.003.html"
      },
      {
        id: "domain2_engineering_esg",
        tag: "DOMAIN 2",
        shortTitle: "Critical Engineering",
        category: "Core Engineering & Systems",
        title: "Domain 2: Critical Power, Thermal Engineering & Facility Infrastructure",
        description: "45 MW Critical IT Capacity, Dual 110kV/22kV Substation, 10x 3,000 kVA Gensets, Standby QSK95, 15,000 RT Magnetic Chillers, 80 kW AI DLC, PUE 1.280.",
        badge: "Engineering Systems",
        file: "/dc/modules/domain2_datacenter_engineering_Rev.027.html"
      },
      {
        id: "domain3_capex",
        tag: "DOMAIN 3",
        shortTitle: "Cost & Contracts",
        category: "Commercial & Controls",
        title: "Domain 3: Project Cost, EVM & Wholesale Commercials",
        description: "$180.00M BAC Breakdown (12 WBS Packages), Rust WebAssembly Monte Carlo Engine, Exact Newton-Raphson 15-Year IRR Solver, FIDIC Silver Book SOW.",
        badge: "Cost & Contracts",
        file: "/dc/modules/domain3_capex_cost_contracts_Rev.011.html"
      },
      {
        id: "domain4_construction",
        tag: "DOMAIN 4",
        shortTitle: "Civil & Construction",
        category: "Physical Delivery",
        title: "Domain 4: Physical Construction & Civil Infrastructure",
        description: "14-Month Master Gantt Schedule, Milestone Gates MS-01 to MS-06, 1,250 PHC Piles to -38m, 1.8m Mass Raft Slab, 12,000 m² White Space, ITP QA/QC.",
        badge: "Construction",
        file: "/dc/modules/domain4_physical_construction_Rev.006.html"
      },
      {
        id: "domain5_handover",
        tag: "DOMAIN 5",
        shortTitle: "5-Level Cx & Handover",
        category: "Commissioning & Handover",
        title: "Domain 5: 5-Level Commissioning & Operational Handover",
        description: "5-Level Commissioning (L1 Factory, L2 Component, L3 System, L4 Integrated IST, L5 Operational Handover), Black Building Test, Tier III Certification.",
        badge: "Commissioning",
        file: "/dc/modules/domain5_commissioning_handover_Rev.002.html"
      }
    ]
  },

  portfolio: {
    id: "portfolio",
    name: "Portfolio Overview & Pipeline Verticals",
    shortName: "Portfolio & Pipeline",
    code: "PORTFOLIO",
    badge: "Multi-Vertical Directorate",
    badgeColor: "amber",
    subtitle: "Renewable Viet Nam Capital Projects Directorate | Portfolio Analytics & Extensible Future Verticals",
    sector: "Multi-Sector Infrastructure Directorate",
    metrics: [
      { label: "Portfolio CAPEX", value: "$250.00M+ USD" },
      { label: "Active Verticals", value: "2 Deployed" },
      { label: "Pipeline Verticals", value: "3 In Development" },
      { label: "Edge Gateway", value: "5 Gateways Live" }
    ],
    defaultModule: "overview",
    standaloneUrl: "https://project.renewablevietnam.com/",
    pipelineProjects: [
      {
        id: "offshore_wind",
        name: "Offshore Wind & Marine Energy EPC",
        stage: "Pre-Feasibility & Interconnection Study",
        capacity: "500 MW Phase 1 (Bình Thuận / Ninh Thuận)",
        capex: "$1.20B USD Projected",
        standard: "IEC 61400-3-1 & DNV-ST-0119",
        status: "PDP8 Target Allocation",
        statusColor: "sky"
      },
      {
        id: "green_hydrogen",
        name: "Green Hydrogen & Ammonia Production Hub",
        stage: "Techno-Economic & Water Resource Modeling",
        capacity: "100,000 Tonnes / Year Green NH3",
        capex: "$450.00M USD Projected",
        standard: "ISO 22734 / Decree 80 DPPA Green Power",
        status: "Feasibility Stage",
        statusColor: "emerald"
      },
      {
        id: "industrial_bess",
        name: "Industrial Rooftop Solar & BESS Microgrids",
        stage: "EPC Execution & Direct Power Purchase (DPPA)",
        capacity: "65 MWp Distributed + 30 MWh BESS",
        capex: "$62.00M USD Committed",
        standard: "Decree 80/2024/ND-CP DPPA Protocol",
        status: "Active Execution",
        statusColor: "teal"
      }
    ]
  }
};
