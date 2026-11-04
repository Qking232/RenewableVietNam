/**
 * Hyperscale Data Center Executive Portal Module Manifest - Rev.024 (Multi-Scenario Sensitivity Edition)
 * Target: 45 MW IT Capacity Tier III / Tier IV Mission-Critical Facility Vietnam
 * Architecture: Executive 6-Module Portfolio Grid
 */
window.PORTAL_MODULES = [
  {
    id: "master_governance",
    tag: "FRAMEWORK",
    shortTitle: "Project Delivery",
    category: "Executive Governance",
    title: "Project Delivery Framework",
    description: "The '5+3' Capital Delivery System: 6-Stage Gate Process, 30-Deliverable RACI Matrix, and 8 Mission-Critical Execution Pillars.",
    badge: "Framework",
    file: "modules/master_project_governance_Rev.001.html"
  },
  {
    id: "domain1_permitting",
    tag: "DOMAIN 1",
    shortTitle: "Permits & Statutory",
    category: "Statutory Compliance",
    title: "Domain 1: Permits, Grid Tie & Statutory Approvals",
    description: "IRC/ERC, 1/500 Detailed Plan, TKCS Basic Design, QCVN 06:2022 PCCC Fire Safety, Decree 08/2022 GPMT, and EVN 110kV Substation Interconnection.",
    badge: "Permits",
    file: "modules/domain1_statutory_permitting_Rev.001.html"
  },
  {
    id: "domain2_engineering_esg",
    tag: "DOMAIN 2",
    shortTitle: "Critical Engineering",
    category: "Core Engineering & ESG",
    title: "Domain 2: Critical Power, Thermal Engineering & Facility Infrastructure",
    description: "45 MW Critical IT Capacity, Dual 110kV/22kV Substation, 10x 3,000 kVA Gensets, 2N UPS + 30 MWh BESS, 15,000 RT Magnetic Chillers, 80 kW AI DLC, PUE 1.280.",
    badge: "Engineering Systems",
    file: "modules/domain2_datacenter_engineering_Rev.020.html"
  },
  {
    id: "domain3_capex",
    tag: "DOMAIN 3",
    shortTitle: "Cost & Contracts",
    category: "Commercial & Controls",
    title: "Domain 3: Project Cost, EVM & Wholesale Commercials",
    description: "$180.00M BAC Breakdown (12 WBS Packages), 6-Tab Financial Navigator, 15-Year DCF Calsheet, Multi-Scenario Sensitivity Simulator, S-Curve Engine & FIDIC Silver Book SOW.",
    badge: "Cost & Contracts",
    file: "modules/domain3_capex_cost_contracts_Rev.005.html"
  },
  {
    id: "domain4_handover",
    tag: "DOMAIN 4",
    shortTitle: "5-Level Cx & Handover",
    category: "Commissioning & Ops",
    title: "Domain 4: 5-Level Commissioning & Operational Handover",
    description: "ASHRAE Guideline 0-2019 Levels 1-5 Cx, Integrated Systems Testing (IST), Blackout Transfer, Heat Load Bank Testing, and Uptime Tier III Certification.",
    badge: "Commissioning",
    file: "modules/domain4_commissioning_handover_Rev.001.html"
  },
  {
    id: "domain5_board_qa",
    tag: "DOMAIN 5",
    shortTitle: "Board Room Defense",
    category: "Executive Defense",
    title: "Domain 5: Boardroom Q&A & Investor Due Diligence Defense",
    description: "30 Master Defense Cards across Capital Allocation, Technical Risk, ESG & Carbon Quotas, Permitting Hurdles, and Commercial SLA Guarantees.",
    badge: "Defense Cards",
    file: "modules/domain5_board_defense_qa_Rev.001.html"
  }
];
