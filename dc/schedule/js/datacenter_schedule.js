// Institutional DC36-T3 Hyperscale Datacenter Schedule Dataset
// Oracle Primavera P6 Relational Schema / DCMA-14 Standard Compliance

window.DC36_SCHEDULE = {
    project_id: "DC36-T3",
    project_name: "Hyperscale Data Center Facility 36MW Tier III",
    min_date: "2027-01-04",
    max_date: "2029-10-01",
    min_timestamp: 1799024400000,
    max_timestamp: 1885510800000,
    total_calendar_days: 1001,
    total_activities: 105,
    wbs_hierarchy: [
  {
    "id": "100",
    "parent_id": "",
    "code": "DC36-T3",
    "name": "Hyperscale Data Center Facility 36MW Tier III"
  },
  {
    "id": "110",
    "parent_id": "100",
    "code": "1.0-PM",
    "name": "1.0 Project Management, Permitting & Utilities"
  },
  {
    "id": "120",
    "parent_id": "100",
    "code": "2.0-ENG",
    "name": "2.0 Detailed Engineering & BIM LOD 400"
  },
  {
    "id": "130",
    "parent_id": "100",
    "code": "3.0-PROC",
    "name": "3.0 Long-Lead Procurement & Factory Acceptance Testing"
  },
  {
    "id": "140",
    "parent_id": "100",
    "code": "4.0-CIVIL",
    "name": "4.0 Civil, Structural & Building Shell"
  },
  {
    "id": "141",
    "parent_id": "140",
    "code": "4.1-SUB",
    "name": "4.1 Substructure & Deep Foundation Piling"
  },
  {
    "id": "142",
    "parent_id": "140",
    "code": "4.2-SUPER",
    "name": "4.2 Concrete Superstructure & Steel Framing"
  },
  {
    "id": "143",
    "parent_id": "140",
    "code": "4.3-ENVEL",
    "name": "4.3 Building Envelope, Facade & Weatherproofing"
  },
  {
    "id": "150",
    "parent_id": "100",
    "code": "5.0-MEP",
    "name": "5.0 MEP Infrastructure & White Space Fit-Out"
  },
  {
    "id": "151",
    "parent_id": "150",
    "code": "5.1-ELEC",
    "name": "5.1 110kV/22kV Substation & High/Medium Voltage Distribution"
  },
  {
    "id": "152",
    "parent_id": "150",
    "code": "5.2-GEN",
    "name": "5.2 Emergency Generator Farm & Fuel Storage Facility"
  },
  {
    "id": "153",
    "parent_id": "150",
    "code": "5.3-MECH",
    "name": "5.3 Central Chilled Water Plant & Hydronic Piping"
  },
  {
    "id": "154",
    "parent_id": "150",
    "code": "5.4-WS",
    "name": "5.4 Data Halls White Space Fit-Out (Halls 1-4)"
  },
  {
    "id": "155",
    "parent_id": "150",
    "code": "5.5-ICT",
    "name": "5.5 BMS, EPMS, Fire Life Safety & Security Systems"
  },
  {
    "id": "160",
    "parent_id": "100",
    "code": "6.0-CX",
    "name": "6.0 Quality Assurance & Commissioning (Cx Levels 1-5)"
  },
  {
    "id": "161",
    "parent_id": "160",
    "code": "6.1-L12",
    "name": "6.1 Cx Levels 1 & 2: Factory Acceptance & Field QA/QC"
  },
  {
    "id": "162",
    "parent_id": "160",
    "code": "6.2-L3",
    "name": "6.2 Cx Level 3: Pre-Functional Static Component Testing"
  },
  {
    "id": "163",
    "parent_id": "160",
    "code": "6.3-L4",
    "name": "6.3 Cx Level 4: Functional System Dynamic Performance"
  },
  {
    "id": "164",
    "parent_id": "160",
    "code": "6.4-L5",
    "name": "6.4 Cx Level 5: Integrated Systems Testing (IST with 36MW Load)"
  },
  {
    "id": "170",
    "parent_id": "100",
    "code": "7.0-COD",
    "name": "7.0 Authority Clearance, Uptime Certification & Handover"
  }
],
    milestones: [
  {
    "id": "2001",
    "code": "M1000",
    "name": "Notice to Proceed & Project Kickoff Milestone",
    "wbs_id": "110",
    "wbs_code": "1.0-PM",
    "wbs_name": "1.0 Project Management, Permitting & Utilities",
    "duration": 0,
    "type": "TT_Mile",
    "start": "2027-01-04",
    "finish": "2027-01-04",
    "startTimestamp": 1799024400000,
    "finishTimestamp": 1799024400000,
    "late_start": "2027-01-04",
    "late_finish": "2027-01-04",
    "total_float": 0,
    "is_critical": true,
    "phase": 1,
    "tag": "pm_eng",
    "predecessors": [],
    "successors": [
      "A1010",
      "A1020",
      "A1030",
      "A1040",
      "A1050",
      "A2010",
      "A2020"
    ]
  },
  {
    "id": "2007",
    "code": "M1060",
    "name": "All Statutory Permits & Authorizations Secured Milestone",
    "wbs_id": "110",
    "wbs_code": "1.0-PM",
    "wbs_name": "1.0 Project Management, Permitting & Utilities",
    "duration": 0,
    "type": "TT_FinMile",
    "start": "2027-03-29",
    "finish": "2027-03-29",
    "startTimestamp": 1806282000000,
    "finishTimestamp": 1806282000000,
    "late_start": "2027-03-29",
    "late_finish": "2027-03-29",
    "total_float": 0,
    "is_critical": true,
    "phase": 1,
    "tag": "pm_eng",
    "predecessors": [
      "A1010",
      "A1020",
      "A1030",
      "A1040",
      "A1050"
    ],
    "successors": [
      "A4110"
    ]
  },
  {
    "id": "2020",
    "code": "M2110",
    "name": "IFC Engineering Design Freeze & BIM LOD 400 Sign-Off",
    "wbs_id": "120",
    "wbs_code": "2.0-ENG",
    "wbs_name": "2.0 Detailed Engineering & BIM LOD 400",
    "duration": 0,
    "type": "TT_FinMile",
    "start": "2027-07-12",
    "finish": "2027-07-12",
    "startTimestamp": 1815354000000,
    "finishTimestamp": 1815354000000,
    "late_start": "2028-02-07",
    "late_finish": "2028-02-07",
    "total_float": 150,
    "is_critical": false,
    "phase": 1,
    "tag": "pm_eng",
    "predecessors": [
      "A2040",
      "A2060",
      "A2080",
      "A2090",
      "A2100"
    ],
    "successors": [
      "A3010",
      "A3020",
      "A3030",
      "A3040",
      "A3050",
      "A3060",
      "A3070",
      "A3080",
      "A3090",
      "A3100",
      "A3110"
    ]
  },
  {
    "id": "2041",
    "code": "M3120",
    "name": "Long-Lead Equipment Factory Acceptance & Delivery Milestone",
    "wbs_id": "130",
    "wbs_code": "3.0-PROC",
    "wbs_name": "3.0 Long-Lead Procurement & Factory Acceptance Testing",
    "duration": 0,
    "type": "TT_FinMile",
    "start": "2027-12-27",
    "finish": "2027-12-27",
    "startTimestamp": 1829869200000,
    "finishTimestamp": 1829869200000,
    "late_start": "2028-11-06",
    "late_finish": "2028-11-06",
    "total_float": 225,
    "is_critical": false,
    "phase": 1,
    "tag": "pm_eng",
    "predecessors": [
      "A3010",
      "A3020",
      "A3030",
      "A3040",
      "A3050",
      "A3060",
      "A3070",
      "A3080",
      "A3090",
      "A3100",
      "A3110"
    ],
    "successors": [
      "A6110"
    ]
  },
  {
    "id": "2074",
    "code": "M4350",
    "name": "Building Shell 100% Weather-Tight Milestone",
    "wbs_id": "143",
    "wbs_code": "4.3-ENVEL",
    "wbs_name": "4.3 Building Envelope, Facade & Weatherproofing",
    "duration": 0,
    "type": "TT_FinMile",
    "start": "2028-07-17",
    "finish": "2028-07-17",
    "startTimestamp": 1847408400000,
    "finishTimestamp": 1847408400000,
    "late_start": "2028-07-17",
    "late_finish": "2028-07-17",
    "total_float": 0,
    "is_critical": true,
    "phase": 4,
    "tag": "envelope_doors",
    "predecessors": [
      "A4340"
    ],
    "successors": [
      "A5110",
      "A5210",
      "A5310",
      "A5330",
      "A5410",
      "A5430",
      "A5480"
    ]
  },
  {
    "id": "2126",
    "code": "M5570",
    "name": "MEP Infrastructure & White Space Fit-Out Completion Milestone",
    "wbs_id": "155",
    "wbs_code": "5.5-ICT",
    "wbs_name": "5.5 BMS, EPMS, Fire Life Safety & Security Systems",
    "duration": 0,
    "type": "TT_FinMile",
    "start": "2029-01-15",
    "finish": "2029-01-15",
    "startTimestamp": 1863133200000,
    "finishTimestamp": 1863133200000,
    "late_start": "2029-01-15",
    "late_finish": "2029-01-15",
    "total_float": 0,
    "is_critical": true,
    "phase": 6,
    "tag": "bms_fire",
    "predecessors": [
      "A5150",
      "A5230",
      "A5250",
      "A5420",
      "A5460",
      "A5470",
      "A5510",
      "A5520",
      "A5540",
      "A5550",
      "A5560"
    ],
    "successors": [
      "A6210",
      "A6230",
      "A6250"
    ]
  },
  {
    "id": "2145",
    "code": "M6260",
    "name": "Pre-Functional Static Energization Ready Milestone",
    "wbs_id": "162",
    "wbs_code": "6.2-L3",
    "wbs_name": "6.2 Cx Level 3: Pre-Functional Static Component Testing",
    "duration": 0,
    "type": "TT_FinMile",
    "start": "2029-03-19",
    "finish": "2029-03-19",
    "startTimestamp": 1868576400000,
    "finishTimestamp": 1868576400000,
    "late_start": "2029-03-19",
    "late_finish": "2029-03-19",
    "total_float": 0,
    "is_critical": true,
    "phase": 7,
    "tag": "cx_static",
    "predecessors": [
      "A6240",
      "A6250"
    ],
    "successors": [
      "A6310"
    ]
  },
  {
    "id": "2156",
    "code": "M6370",
    "name": "Functional Performance Testing Level 4 Completed Milestone",
    "wbs_id": "163",
    "wbs_code": "6.3-L4",
    "wbs_name": "6.3 Cx Level 4: Functional System Dynamic Performance",
    "duration": 0,
    "type": "TT_FinMile",
    "start": "2029-05-14",
    "finish": "2029-05-14",
    "startTimestamp": 1873414800000,
    "finishTimestamp": 1873414800000,
    "late_start": "2029-05-14",
    "late_finish": "2029-05-14",
    "total_float": 0,
    "is_critical": true,
    "phase": 7,
    "tag": "cx_dynamic",
    "predecessors": [
      "A6320",
      "A6330",
      "A6350",
      "A6360"
    ],
    "successors": [
      "A6410"
    ]
  },
  {
    "id": "2166",
    "code": "M6470",
    "name": "Cx Level 5 Integrated Systems Testing 100% Passed Milestone",
    "wbs_id": "164",
    "wbs_code": "6.4-L5",
    "wbs_name": "6.4 Cx Level 5: Integrated Systems Testing (IST with 36MW Load)",
    "duration": 0,
    "type": "TT_FinMile",
    "start": "2029-07-23",
    "finish": "2029-07-23",
    "startTimestamp": 1879462800000,
    "finishTimestamp": 1879462800000,
    "late_start": "2029-07-23",
    "late_finish": "2029-07-23",
    "total_float": 0,
    "is_critical": true,
    "phase": 7,
    "tag": "cx_load_banks",
    "predecessors": [
      "A6460"
    ],
    "successors": [
      "A7010",
      "A7020"
    ]
  },
  {
    "id": "2175",
    "code": "M7060",
    "name": "Commercial Operation Date (COD) & Final Acceptance Milestone",
    "wbs_id": "170",
    "wbs_code": "7.0-COD",
    "wbs_name": "7.0 Authority Clearance, Uptime Certification & Handover",
    "duration": 0,
    "type": "TT_FinMile",
    "start": "2029-10-01",
    "finish": "2029-10-01",
    "startTimestamp": 1885510800000,
    "finishTimestamp": 1885510800000,
    "late_start": "2029-10-01",
    "late_finish": "2029-10-01",
    "total_float": 0,
    "is_critical": true,
    "phase": 8,
    "tag": "cod_operational",
    "predecessors": [
      "A7050"
    ],
    "successors": []
  }
],
    activities: [
  {
    "id": "2001",
    "code": "M1000",
    "name": "Notice to Proceed & Project Kickoff Milestone",
    "wbs_id": "110",
    "wbs_code": "1.0-PM",
    "wbs_name": "1.0 Project Management, Permitting & Utilities",
    "duration": 0,
    "type": "TT_Mile",
    "start": "2027-01-04",
    "finish": "2027-01-04",
    "startTimestamp": 1799024400000,
    "finishTimestamp": 1799024400000,
    "late_start": "2027-01-04",
    "late_finish": "2027-01-04",
    "total_float": 0,
    "is_critical": true,
    "phase": 1,
    "tag": "pm_eng",
    "predecessors": [],
    "successors": [
      "A1010",
      "A1020",
      "A1030",
      "A1040",
      "A1050",
      "A2010",
      "A2020"
    ]
  },
  {
    "id": "2002",
    "code": "A1010",
    "name": "Environmental Impact Assessment (EIA) Approval",
    "wbs_id": "110",
    "wbs_code": "1.0-PM",
    "wbs_name": "1.0 Project Management, Permitting & Utilities",
    "duration": 40,
    "type": "TT_Task",
    "start": "2027-01-04",
    "finish": "2027-03-01",
    "startTimestamp": 1799024400000,
    "finishTimestamp": 1803862800000,
    "late_start": "2027-02-01",
    "late_finish": "2027-03-29",
    "total_float": 20,
    "is_critical": false,
    "phase": 1,
    "tag": "pm_eng",
    "predecessors": [
      "M1000"
    ],
    "successors": [
      "M1060"
    ]
  },
  {
    "id": "2003",
    "code": "A1020",
    "name": "Municipal Building Construction Permit",
    "wbs_id": "110",
    "wbs_code": "1.0-PM",
    "wbs_name": "1.0 Project Management, Permitting & Utilities",
    "duration": 50,
    "type": "TT_Task",
    "start": "2027-01-04",
    "finish": "2027-03-15",
    "startTimestamp": 1799024400000,
    "finishTimestamp": 1805072400000,
    "late_start": "2027-01-18",
    "late_finish": "2027-03-29",
    "total_float": 10,
    "is_critical": false,
    "phase": 1,
    "tag": "pm_eng",
    "predecessors": [
      "M1000"
    ],
    "successors": [
      "M1060"
    ]
  },
  {
    "id": "2004",
    "code": "A1030",
    "name": "110kV High-Voltage Utility Interconnect Agreement",
    "wbs_id": "110",
    "wbs_code": "1.0-PM",
    "wbs_name": "1.0 Project Management, Permitting & Utilities",
    "duration": 60,
    "type": "TT_Task",
    "start": "2027-01-04",
    "finish": "2027-03-29",
    "startTimestamp": 1799024400000,
    "finishTimestamp": 1806282000000,
    "late_start": "2027-01-04",
    "late_finish": "2027-03-29",
    "total_float": 0,
    "is_critical": true,
    "phase": 1,
    "tag": "pm_eng",
    "predecessors": [
      "M1000"
    ],
    "successors": [
      "M1060",
      "A6310"
    ]
  },
  {
    "id": "2005",
    "code": "A1040",
    "name": "Aviation Obstruction & Height Clearance Sign-Off",
    "wbs_id": "110",
    "wbs_code": "1.0-PM",
    "wbs_name": "1.0 Project Management, Permitting & Utilities",
    "duration": 30,
    "type": "TT_Task",
    "start": "2027-01-04",
    "finish": "2027-02-15",
    "startTimestamp": 1799024400000,
    "finishTimestamp": 1802653200000,
    "late_start": "2027-02-15",
    "late_finish": "2027-03-29",
    "total_float": 30,
    "is_critical": false,
    "phase": 1,
    "tag": "pm_eng",
    "predecessors": [
      "M1000"
    ],
    "successors": [
      "M1060"
    ]
  },
  {
    "id": "2006",
    "code": "A1050",
    "name": "Fire Authority (Civil Defense) Concept Approval",
    "wbs_id": "110",
    "wbs_code": "1.0-PM",
    "wbs_name": "1.0 Project Management, Permitting & Utilities",
    "duration": 45,
    "type": "TT_Task",
    "start": "2027-01-04",
    "finish": "2027-03-08",
    "startTimestamp": 1799024400000,
    "finishTimestamp": 1804467600000,
    "late_start": "2027-01-25",
    "late_finish": "2027-03-29",
    "total_float": 15,
    "is_critical": false,
    "phase": 1,
    "tag": "pm_eng",
    "predecessors": [
      "M1000"
    ],
    "successors": [
      "M1060"
    ]
  },
  {
    "id": "2010",
    "code": "A2010",
    "name": "BIM Execution Plan & Common Data Environment (CDE) Setup",
    "wbs_id": "120",
    "wbs_code": "2.0-ENG",
    "wbs_name": "2.0 Detailed Engineering & BIM LOD 400",
    "duration": 15,
    "type": "TT_Task",
    "start": "2027-01-04",
    "finish": "2027-01-25",
    "startTimestamp": 1799024400000,
    "finishTimestamp": 1800838800000,
    "late_start": "2027-01-18",
    "late_finish": "2027-02-08",
    "total_float": 10,
    "is_critical": false,
    "phase": 1,
    "tag": "pm_eng",
    "predecessors": [
      "M1000"
    ],
    "successors": [
      "A2030",
      "A2050",
      "A2070"
    ]
  },
  {
    "id": "2011",
    "code": "A2020",
    "name": "Geotechnical Borehole Investigation & Soil Bearing Report",
    "wbs_id": "120",
    "wbs_code": "2.0-ENG",
    "wbs_name": "2.0 Detailed Engineering & BIM LOD 400",
    "duration": 25,
    "type": "TT_Task",
    "start": "2027-01-04",
    "finish": "2027-02-08",
    "startTimestamp": 1799024400000,
    "finishTimestamp": 1802048400000,
    "late_start": "2027-01-04",
    "late_finish": "2027-02-08",
    "total_float": 0,
    "is_critical": true,
    "phase": 1,
    "tag": "pm_eng",
    "predecessors": [
      "M1000"
    ],
    "successors": [
      "A2030"
    ]
  },
  {
    "id": "2007",
    "code": "M1060",
    "name": "All Statutory Permits & Authorizations Secured Milestone",
    "wbs_id": "110",
    "wbs_code": "1.0-PM",
    "wbs_name": "1.0 Project Management, Permitting & Utilities",
    "duration": 0,
    "type": "TT_FinMile",
    "start": "2027-03-29",
    "finish": "2027-03-29",
    "startTimestamp": 1806282000000,
    "finishTimestamp": 1806282000000,
    "late_start": "2027-03-29",
    "late_finish": "2027-03-29",
    "total_float": 0,
    "is_critical": true,
    "phase": 1,
    "tag": "pm_eng",
    "predecessors": [
      "A1010",
      "A1020",
      "A1030",
      "A1040",
      "A1050"
    ],
    "successors": [
      "A4110"
    ]
  },
  {
    "id": "2014",
    "code": "A2050",
    "name": "110kV/22kV Substation SLD & Protection Coordination Study",
    "wbs_id": "120",
    "wbs_code": "2.0-ENG",
    "wbs_name": "2.0 Detailed Engineering & BIM LOD 400",
    "duration": 40,
    "type": "TT_Task",
    "start": "2027-01-25",
    "finish": "2027-03-22",
    "startTimestamp": 1800838800000,
    "finishTimestamp": 1805677200000,
    "late_start": "2027-08-23",
    "late_finish": "2027-10-18",
    "total_float": 150,
    "is_critical": false,
    "phase": 1,
    "tag": "pm_eng",
    "predecessors": [
      "A2010"
    ],
    "successors": [
      "A2060"
    ]
  },
  {
    "id": "2016",
    "code": "A2070",
    "name": "Chilled Water Plant P&ID & Hydronic Piping Isometrics",
    "wbs_id": "120",
    "wbs_code": "2.0-ENG",
    "wbs_name": "2.0 Detailed Engineering & BIM LOD 400",
    "duration": 40,
    "type": "TT_Task",
    "start": "2027-01-25",
    "finish": "2027-03-22",
    "startTimestamp": 1800838800000,
    "finishTimestamp": 1805677200000,
    "late_start": "2027-11-01",
    "late_finish": "2027-12-27",
    "total_float": 200,
    "is_critical": false,
    "phase": 1,
    "tag": "pm_eng",
    "predecessors": [
      "A2010"
    ],
    "successors": [
      "A2080",
      "A2100"
    ]
  },
  {
    "id": "2012",
    "code": "A2030",
    "name": "Piling & Deep Foundation IFC Package (BIM LOD 400)",
    "wbs_id": "120",
    "wbs_code": "2.0-ENG",
    "wbs_name": "2.0 Detailed Engineering & BIM LOD 400",
    "duration": 35,
    "type": "TT_Task",
    "start": "2027-02-08",
    "finish": "2027-03-29",
    "startTimestamp": 1802048400000,
    "finishTimestamp": 1806282000000,
    "late_start": "2027-02-08",
    "late_finish": "2027-03-29",
    "total_float": 0,
    "is_critical": true,
    "phase": 1,
    "tag": "pm_eng",
    "predecessors": [
      "A2010",
      "A2020"
    ],
    "successors": [
      "A2040",
      "A4110"
    ]
  },
  {
    "id": "2015",
    "code": "A2060",
    "name": "MV/LV Power Distribution & Fault Current Calculations",
    "wbs_id": "120",
    "wbs_code": "2.0-ENG",
    "wbs_name": "2.0 Detailed Engineering & BIM LOD 400",
    "duration": 45,
    "type": "TT_Task",
    "start": "2027-03-22",
    "finish": "2027-05-24",
    "startTimestamp": 1805677200000,
    "finishTimestamp": 1811120400000,
    "late_start": "2027-10-18",
    "late_finish": "2027-12-20",
    "total_float": 150,
    "is_critical": false,
    "phase": 1,
    "tag": "pm_eng",
    "predecessors": [
      "A2050"
    ],
    "successors": [
      "A2090",
      "M2110"
    ]
  },
  {
    "id": "2017",
    "code": "A2080",
    "name": "White Space CFD Thermal Modeling & Airflow Optimization",
    "wbs_id": "120",
    "wbs_code": "2.0-ENG",
    "wbs_name": "2.0 Detailed Engineering & BIM LOD 400",
    "duration": 30,
    "type": "TT_Task",
    "start": "2027-03-22",
    "finish": "2027-05-03",
    "startTimestamp": 1805677200000,
    "finishTimestamp": 1809306000000,
    "late_start": "2027-12-27",
    "late_finish": "2028-02-07",
    "total_float": 200,
    "is_critical": false,
    "phase": 1,
    "tag": "pm_eng",
    "predecessors": [
      "A2070"
    ],
    "successors": [
      "M2110"
    ]
  },
  {
    "id": "2019",
    "code": "A2100",
    "name": "VESDA & Clean Agent Fire Suppression Hydraulic Calcs",
    "wbs_id": "120",
    "wbs_code": "2.0-ENG",
    "wbs_name": "2.0 Detailed Engineering & BIM LOD 400",
    "duration": 30,
    "type": "TT_Task",
    "start": "2027-03-22",
    "finish": "2027-05-03",
    "startTimestamp": 1805677200000,
    "finishTimestamp": 1809306000000,
    "late_start": "2027-12-27",
    "late_finish": "2028-02-07",
    "total_float": 200,
    "is_critical": false,
    "phase": 1,
    "tag": "pm_eng",
    "predecessors": [
      "A2070"
    ],
    "successors": [
      "M2110"
    ]
  },
  {
    "id": "2013",
    "code": "A2040",
    "name": "Reinforced Concrete Superstructure & Steel Roof IFC",
    "wbs_id": "120",
    "wbs_code": "2.0-ENG",
    "wbs_name": "2.0 Detailed Engineering & BIM LOD 400",
    "duration": 45,
    "type": "TT_Task",
    "start": "2027-03-29",
    "finish": "2027-05-31",
    "startTimestamp": 1806282000000,
    "finishTimestamp": 1811725200000,
    "late_start": "2027-12-06",
    "late_finish": "2028-02-07",
    "total_float": 180,
    "is_critical": false,
    "phase": 1,
    "tag": "pm_eng",
    "predecessors": [
      "A2030"
    ],
    "successors": [
      "M2110"
    ]
  },
  {
    "id": "2050",
    "code": "A4110",
    "name": "Site Clearing, Bulk Excavation & Engineered Fill",
    "wbs_id": "141",
    "wbs_code": "4.1-SUB",
    "wbs_name": "4.1 Substructure & Deep Foundation Piling",
    "duration": 30,
    "type": "TT_Task",
    "start": "2027-03-29",
    "finish": "2027-05-10",
    "startTimestamp": 1806282000000,
    "finishTimestamp": 1809910800000,
    "late_start": "2027-03-29",
    "late_finish": "2027-05-10",
    "total_float": 0,
    "is_critical": true,
    "phase": 1,
    "tag": "excavation",
    "predecessors": [
      "M1060",
      "A2030"
    ],
    "successors": [
      "A4120"
    ]
  },
  {
    "id": "2018",
    "code": "A2090",
    "name": "BMS & EPMS I/O Points List & Network Architecture",
    "wbs_id": "120",
    "wbs_code": "2.0-ENG",
    "wbs_name": "2.0 Detailed Engineering & BIM LOD 400",
    "duration": 35,
    "type": "TT_Task",
    "start": "2027-05-24",
    "finish": "2027-07-12",
    "startTimestamp": 1811120400000,
    "finishTimestamp": 1815354000000,
    "late_start": "2027-12-20",
    "late_finish": "2028-02-07",
    "total_float": 150,
    "is_critical": false,
    "phase": 1,
    "tag": "pm_eng",
    "predecessors": [
      "A2060"
    ],
    "successors": [
      "M2110"
    ]
  },
  {
    "id": "2051",
    "code": "A4120",
    "name": "Bored Cast-in-Place Concrete Piling (600 piles)",
    "wbs_id": "141",
    "wbs_code": "4.1-SUB",
    "wbs_name": "4.1 Substructure & Deep Foundation Piling",
    "duration": 45,
    "type": "TT_Task",
    "start": "2027-05-10",
    "finish": "2027-07-12",
    "startTimestamp": 1809910800000,
    "finishTimestamp": 1815354000000,
    "late_start": "2027-05-10",
    "late_finish": "2027-07-12",
    "total_float": 0,
    "is_critical": true,
    "phase": 1,
    "tag": "piling",
    "predecessors": [
      "A4110"
    ],
    "successors": [
      "A4130"
    ]
  },
  {
    "id": "2020",
    "code": "M2110",
    "name": "IFC Engineering Design Freeze & BIM LOD 400 Sign-Off",
    "wbs_id": "120",
    "wbs_code": "2.0-ENG",
    "wbs_name": "2.0 Detailed Engineering & BIM LOD 400",
    "duration": 0,
    "type": "TT_FinMile",
    "start": "2027-07-12",
    "finish": "2027-07-12",
    "startTimestamp": 1815354000000,
    "finishTimestamp": 1815354000000,
    "late_start": "2028-02-07",
    "late_finish": "2028-02-07",
    "total_float": 150,
    "is_critical": false,
    "phase": 1,
    "tag": "pm_eng",
    "predecessors": [
      "A2040",
      "A2060",
      "A2080",
      "A2090",
      "A2100"
    ],
    "successors": [
      "A3010",
      "A3020",
      "A3030",
      "A3040",
      "A3050",
      "A3060",
      "A3070",
      "A3080",
      "A3090",
      "A3100",
      "A3110"
    ]
  },
  {
    "id": "2052",
    "code": "A4130",
    "name": "Pile Head Trimming & Low-Strain Pile Integrity Testing (PIT)",
    "wbs_id": "141",
    "wbs_code": "4.1-SUB",
    "wbs_name": "4.1 Substructure & Deep Foundation Piling",
    "duration": 15,
    "type": "TT_Task",
    "start": "2027-07-12",
    "finish": "2027-08-02",
    "startTimestamp": 1815354000000,
    "finishTimestamp": 1817168400000,
    "late_start": "2027-07-12",
    "late_finish": "2027-08-02",
    "total_float": 0,
    "is_critical": true,
    "phase": 1,
    "tag": "piling",
    "predecessors": [
      "A4120"
    ],
    "successors": [
      "A4140"
    ]
  },
  {
    "id": "2030",
    "code": "A3010",
    "name": "Procure & FAT 110kV/22kV Substation Transformers (2x 45MVA)",
    "wbs_id": "130",
    "wbs_code": "3.0-PROC",
    "wbs_name": "3.0 Long-Lead Procurement & Factory Acceptance Testing",
    "duration": 110,
    "type": "TT_Task",
    "start": "2027-07-12",
    "finish": "2027-12-13",
    "startTimestamp": 1815354000000,
    "finishTimestamp": 1828659600000,
    "late_start": "2028-03-06",
    "late_finish": "2028-08-07",
    "total_float": 170,
    "is_critical": false,
    "phase": 1,
    "tag": "pm_eng",
    "predecessors": [
      "M2110"
    ],
    "successors": [
      "M3120",
      "A5110"
    ]
  },
  {
    "id": "2031",
    "code": "A3020",
    "name": "Procure & FAT 22kV GIS/AIS Medium Voltage Switchgear",
    "wbs_id": "130",
    "wbs_code": "3.0-PROC",
    "wbs_name": "3.0 Long-Lead Procurement & Factory Acceptance Testing",
    "duration": 100,
    "type": "TT_Task",
    "start": "2027-07-12",
    "finish": "2027-11-29",
    "startTimestamp": 1815354000000,
    "finishTimestamp": 1827450000000,
    "late_start": "2028-04-17",
    "late_finish": "2028-09-04",
    "total_float": 200,
    "is_critical": false,
    "phase": 1,
    "tag": "pm_eng",
    "predecessors": [
      "M2110"
    ],
    "successors": [
      "M3120",
      "A5120"
    ]
  },
  {
    "id": "2032",
    "code": "A3030",
    "name": "Procure & FAT 2.5MVA Standby Diesel Generators (16 units)",
    "wbs_id": "130",
    "wbs_code": "3.0-PROC",
    "wbs_name": "3.0 Long-Lead Procurement & Factory Acceptance Testing",
    "duration": 120,
    "type": "TT_Task",
    "start": "2027-07-12",
    "finish": "2027-12-27",
    "startTimestamp": 1815354000000,
    "finishTimestamp": 1829869200000,
    "late_start": "2028-04-17",
    "late_finish": "2028-10-02",
    "total_float": 200,
    "is_critical": false,
    "phase": 1,
    "tag": "pm_eng",
    "predecessors": [
      "M2110"
    ],
    "successors": [
      "M3120",
      "A5220"
    ]
  },
  {
    "id": "2033",
    "code": "A3040",
    "name": "Procure & Deliver Underground Bulk Fuel Storage (3x 80m3)",
    "wbs_id": "130",
    "wbs_code": "3.0-PROC",
    "wbs_name": "3.0 Long-Lead Procurement & Factory Acceptance Testing",
    "duration": 80,
    "type": "TT_Task",
    "start": "2027-07-12",
    "finish": "2027-11-01",
    "startTimestamp": 1815354000000,
    "finishTimestamp": 1825030800000,
    "late_start": "2028-05-08",
    "late_finish": "2028-08-28",
    "total_float": 215,
    "is_critical": false,
    "phase": 1,
    "tag": "pm_eng",
    "predecessors": [
      "M2110"
    ],
    "successors": [
      "M3120",
      "A5210"
    ]
  },
  {
    "id": "2034",
    "code": "A3050",
    "name": "Procure & FAT Static Modular UPS Systems (36x 1000kVA)",
    "wbs_id": "130",
    "wbs_code": "3.0-PROC",
    "wbs_name": "3.0 Long-Lead Procurement & Factory Acceptance Testing",
    "duration": 105,
    "type": "TT_Task",
    "start": "2027-07-12",
    "finish": "2027-12-06",
    "startTimestamp": 1815354000000,
    "finishTimestamp": 1828054800000,
    "late_start": "2028-06-05",
    "late_finish": "2028-10-30",
    "total_float": 235,
    "is_critical": false,
    "phase": 1,
    "tag": "pm_eng",
    "predecessors": [
      "M2110"
    ],
    "successors": [
      "M3120",
      "A5410"
    ]
  },
  {
    "id": "2035",
    "code": "A3060",
    "name": "Procure & Deliver Lithium-Ion Battery Racks & BMS Modules",
    "wbs_id": "130",
    "wbs_code": "3.0-PROC",
    "wbs_name": "3.0 Long-Lead Procurement & Factory Acceptance Testing",
    "duration": 95,
    "type": "TT_Task",
    "start": "2027-07-12",
    "finish": "2027-11-22",
    "startTimestamp": 1815354000000,
    "finishTimestamp": 1826845200000,
    "late_start": "2028-06-26",
    "late_finish": "2028-11-06",
    "total_float": 250,
    "is_critical": false,
    "phase": 1,
    "tag": "pm_eng",
    "predecessors": [
      "M2110"
    ],
    "successors": [
      "M3120",
      "A5420"
    ]
  },
  {
    "id": "2036",
    "code": "A3070",
    "name": "Procure & FAT Centrifugal Chillers (6x 1200 RT N+2)",
    "wbs_id": "130",
    "wbs_code": "3.0-PROC",
    "wbs_name": "3.0 Long-Lead Procurement & Factory Acceptance Testing",
    "duration": 115,
    "type": "TT_Task",
    "start": "2027-07-12",
    "finish": "2027-12-20",
    "startTimestamp": 1815354000000,
    "finishTimestamp": 1829264400000,
    "late_start": "2028-02-07",
    "late_finish": "2028-07-17",
    "total_float": 150,
    "is_critical": false,
    "phase": 1,
    "tag": "pm_eng",
    "predecessors": [
      "M2110"
    ],
    "successors": [
      "M3120",
      "A5310"
    ]
  },
  {
    "id": "2037",
    "code": "A3080",
    "name": "Procure & Deliver Induced Draft Cooling Towers (6 units)",
    "wbs_id": "130",
    "wbs_code": "3.0-PROC",
    "wbs_name": "3.0 Long-Lead Procurement & Factory Acceptance Testing",
    "duration": 90,
    "type": "TT_Task",
    "start": "2027-07-12",
    "finish": "2027-11-15",
    "startTimestamp": 1815354000000,
    "finishTimestamp": 1826240400000,
    "late_start": "2028-04-10",
    "late_finish": "2028-08-14",
    "total_float": 195,
    "is_critical": false,
    "phase": 1,
    "tag": "pm_eng",
    "predecessors": [
      "M2110"
    ],
    "successors": [
      "M3120",
      "A5330"
    ]
  },
  {
    "id": "2038",
    "code": "A3090",
    "name": "Procure White Space CRAH Units (72 units EC fans)",
    "wbs_id": "130",
    "wbs_code": "3.0-PROC",
    "wbs_name": "3.0 Long-Lead Procurement & Factory Acceptance Testing",
    "duration": 85,
    "type": "TT_Task",
    "start": "2027-07-12",
    "finish": "2027-11-08",
    "startTimestamp": 1815354000000,
    "finishTimestamp": 1825635600000,
    "late_start": "2028-07-10",
    "late_finish": "2028-11-06",
    "total_float": 260,
    "is_critical": false,
    "phase": 1,
    "tag": "pm_eng",
    "predecessors": [
      "M2110"
    ],
    "successors": [
      "M3120",
      "A5450"
    ]
  },
  {
    "id": "2039",
    "code": "A3100",
    "name": "Procure 415V Track Busway Systems & Tap-Off Boxes",
    "wbs_id": "130",
    "wbs_code": "3.0-PROC",
    "wbs_name": "3.0 Long-Lead Procurement & Factory Acceptance Testing",
    "duration": 75,
    "type": "TT_Task",
    "start": "2027-07-12",
    "finish": "2027-10-25",
    "startTimestamp": 1815354000000,
    "finishTimestamp": 1824426000000,
    "late_start": "2028-07-24",
    "late_finish": "2028-11-06",
    "total_float": 270,
    "is_critical": false,
    "phase": 1,
    "tag": "pm_eng",
    "predecessors": [
      "M2110"
    ],
    "successors": [
      "M3120",
      "A5440"
    ]
  },
  {
    "id": "2040",
    "code": "A3110",
    "name": "Procure Server Racks & Hot Aisle Containment (HAC) Kits",
    "wbs_id": "130",
    "wbs_code": "3.0-PROC",
    "wbs_name": "3.0 Long-Lead Procurement & Factory Acceptance Testing",
    "duration": 65,
    "type": "TT_Task",
    "start": "2027-07-12",
    "finish": "2027-10-11",
    "startTimestamp": 1815354000000,
    "finishTimestamp": 1823216400000,
    "late_start": "2028-08-07",
    "late_finish": "2028-11-06",
    "total_float": 280,
    "is_critical": false,
    "phase": 1,
    "tag": "pm_eng",
    "predecessors": [
      "M2110"
    ],
    "successors": [
      "M3120",
      "A5470"
    ]
  },
  {
    "id": "2053",
    "code": "A4140",
    "name": "Deep Foundation Reinforced Raft Slab Casting",
    "wbs_id": "141",
    "wbs_code": "4.1-SUB",
    "wbs_name": "4.1 Substructure & Deep Foundation Piling",
    "duration": 35,
    "type": "TT_Task",
    "start": "2027-08-02",
    "finish": "2027-09-20",
    "startTimestamp": 1817168400000,
    "finishTimestamp": 1821402000000,
    "late_start": "2027-08-02",
    "late_finish": "2027-09-20",
    "total_float": 0,
    "is_critical": true,
    "phase": 2,
    "tag": "raft_slab",
    "predecessors": [
      "A4130"
    ],
    "successors": [
      "A4150"
    ]
  },
  {
    "id": "2041",
    "code": "M3120",
    "name": "Long-Lead Equipment Factory Acceptance & Delivery Milestone",
    "wbs_id": "130",
    "wbs_code": "3.0-PROC",
    "wbs_name": "3.0 Long-Lead Procurement & Factory Acceptance Testing",
    "duration": 0,
    "type": "TT_FinMile",
    "start": "2027-12-27",
    "finish": "2027-12-27",
    "startTimestamp": 1829869200000,
    "finishTimestamp": 1829869200000,
    "late_start": "2028-11-06",
    "late_finish": "2028-11-06",
    "total_float": 225,
    "is_critical": false,
    "phase": 1,
    "tag": "pm_eng",
    "predecessors": [
      "A3010",
      "A3020",
      "A3030",
      "A3040",
      "A3050",
      "A3060",
      "A3070",
      "A3080",
      "A3090",
      "A3100",
      "A3110"
    ],
    "successors": [
      "A6110"
    ]
  },
  {
    "id": "2054",
    "code": "A4150",
    "name": "Subgrade Waterproofing Membrane & Ground Earthing Grid",
    "wbs_id": "141",
    "wbs_code": "4.1-SUB",
    "wbs_name": "4.1 Substructure & Deep Foundation Piling",
    "duration": 20,
    "type": "TT_Task",
    "start": "2027-09-20",
    "finish": "2027-10-18",
    "startTimestamp": 1821402000000,
    "finishTimestamp": 1823821200000,
    "late_start": "2027-09-20",
    "late_finish": "2027-10-18",
    "total_float": 0,
    "is_critical": true,
    "phase": 2,
    "tag": "raft_slab",
    "predecessors": [
      "A4140"
    ],
    "successors": [
      "A4210"
    ]
  },
  {
    "id": "2130",
    "code": "A6110",
    "name": "Cx Level 1: Factory Acceptance Test Witness Records Verification",
    "wbs_id": "161",
    "wbs_code": "6.1-L12",
    "wbs_name": "6.1 Cx Levels 1 & 2: Factory Acceptance & Field QA/QC",
    "duration": 15,
    "type": "TT_Task",
    "start": "2027-12-27",
    "finish": "2028-01-17",
    "startTimestamp": 1829869200000,
    "finishTimestamp": 1831683600000,
    "late_start": "2028-11-06",
    "late_finish": "2028-11-27",
    "total_float": 225,
    "is_critical": false,
    "phase": 7,
    "tag": "cx_static",
    "predecessors": [
      "M3120"
    ],
    "successors": [
      "A6120"
    ]
  },
  {
    "id": "2060",
    "code": "A4210",
    "name": "Cast Ground Floor Heavy Equipment Plinths & Columns",
    "wbs_id": "142",
    "wbs_code": "4.2-SUPER",
    "wbs_name": "4.2 Concrete Superstructure & Steel Framing",
    "duration": 30,
    "type": "TT_Task",
    "start": "2027-10-18",
    "finish": "2027-11-29",
    "startTimestamp": 1823821200000,
    "finishTimestamp": 1827450000000,
    "late_start": "2027-10-18",
    "late_finish": "2027-11-29",
    "total_float": 0,
    "is_critical": true,
    "phase": 2,
    "tag": "plinths_columns_g",
    "predecessors": [
      "A4150"
    ],
    "successors": [
      "A4220"
    ]
  },
  {
    "id": "2131",
    "code": "A6120",
    "name": "Cx Level 2: Field Receiving, Physical Unboxing & Damage QA/QC Inspection",
    "wbs_id": "161",
    "wbs_code": "6.1-L12",
    "wbs_name": "6.1 Cx Levels 1 & 2: Factory Acceptance & Field QA/QC",
    "duration": 20,
    "type": "TT_Task",
    "start": "2028-01-17",
    "finish": "2028-02-14",
    "startTimestamp": 1831683600000,
    "finishTimestamp": 1834102800000,
    "late_start": "2028-11-27",
    "late_finish": "2028-12-25",
    "total_float": 225,
    "is_critical": false,
    "phase": 7,
    "tag": "cx_static",
    "predecessors": [
      "A6110"
    ],
    "successors": [
      "A6130"
    ]
  },
  {
    "id": "2061",
    "code": "A4220",
    "name": "Form & Pour Level 1 Suspended Slab (18 kN/m2 load)",
    "wbs_id": "142",
    "wbs_code": "4.2-SUPER",
    "wbs_name": "4.2 Concrete Superstructure & Steel Framing",
    "duration": 25,
    "type": "TT_Task",
    "start": "2027-11-29",
    "finish": "2028-01-03",
    "startTimestamp": 1827450000000,
    "finishTimestamp": 1830474000000,
    "late_start": "2027-11-29",
    "late_finish": "2028-01-03",
    "total_float": 0,
    "is_critical": true,
    "phase": 3,
    "tag": "slab_l1",
    "predecessors": [
      "A4210"
    ],
    "successors": [
      "A4230"
    ]
  },
  {
    "id": "2132",
    "code": "A6130",
    "name": "Pre-Placement Equipment Alignment, Anchor & Torque Verification",
    "wbs_id": "161",
    "wbs_code": "6.1-L12",
    "wbs_name": "6.1 Cx Levels 1 & 2: Factory Acceptance & Field QA/QC",
    "duration": 15,
    "type": "TT_Task",
    "start": "2028-02-14",
    "finish": "2028-03-06",
    "startTimestamp": 1834102800000,
    "finishTimestamp": 1835917200000,
    "late_start": "2028-12-25",
    "late_finish": "2029-01-15",
    "total_float": 225,
    "is_critical": false,
    "phase": 7,
    "tag": "cx_static",
    "predecessors": [
      "A6120"
    ],
    "successors": [
      "A6210"
    ]
  },
  {
    "id": "2062",
    "code": "A4230",
    "name": "Form & Pour Level 2 Suspended Slab (Data Hall Level)",
    "wbs_id": "142",
    "wbs_code": "4.2-SUPER",
    "wbs_name": "4.2 Concrete Superstructure & Steel Framing",
    "duration": 25,
    "type": "TT_Task",
    "start": "2028-01-03",
    "finish": "2028-02-07",
    "startTimestamp": 1830474000000,
    "finishTimestamp": 1833498000000,
    "late_start": "2028-01-03",
    "late_finish": "2028-02-07",
    "total_float": 0,
    "is_critical": true,
    "phase": 3,
    "tag": "slab_l2_shear",
    "predecessors": [
      "A4220"
    ],
    "successors": [
      "A4240",
      "A4250"
    ]
  },
  {
    "id": "2063",
    "code": "A4240",
    "name": "Erect Roof Structural Steel Framing & Chiller Support Gantry",
    "wbs_id": "142",
    "wbs_code": "4.2-SUPER",
    "wbs_name": "4.2 Concrete Superstructure & Steel Framing",
    "duration": 30,
    "type": "TT_Task",
    "start": "2028-02-07",
    "finish": "2028-03-20",
    "startTimestamp": 1833498000000,
    "finishTimestamp": 1837126800000,
    "late_start": "2028-02-07",
    "late_finish": "2028-03-20",
    "total_float": 0,
    "is_critical": true,
    "phase": 4,
    "tag": "steel_roof_gantry",
    "predecessors": [
      "A4230"
    ],
    "successors": [
      "A4310"
    ]
  },
  {
    "id": "2064",
    "code": "A4250",
    "name": "Construct Concrete Shear Walls & Heavy Shaft Risers",
    "wbs_id": "142",
    "wbs_code": "4.2-SUPER",
    "wbs_name": "4.2 Concrete Superstructure & Steel Framing",
    "duration": 25,
    "type": "TT_Task",
    "start": "2028-02-07",
    "finish": "2028-03-13",
    "startTimestamp": 1833498000000,
    "finishTimestamp": 1836522000000,
    "late_start": "2028-02-14",
    "late_finish": "2028-03-20",
    "total_float": 5,
    "is_critical": false,
    "phase": 3,
    "tag": "slab_l2_shear",
    "predecessors": [
      "A4230"
    ],
    "successors": [
      "A4310"
    ]
  },
  {
    "id": "2070",
    "code": "A4310",
    "name": "Install Precast Concrete Insulated Facade Panels",
    "wbs_id": "143",
    "wbs_code": "4.3-ENVEL",
    "wbs_name": "4.3 Building Envelope, Facade & Weatherproofing",
    "duration": 35,
    "type": "TT_Task",
    "start": "2028-03-20",
    "finish": "2028-05-08",
    "startTimestamp": 1837126800000,
    "finishTimestamp": 1841360400000,
    "late_start": "2028-03-20",
    "late_finish": "2028-05-08",
    "total_float": 0,
    "is_critical": true,
    "phase": 4,
    "tag": "facade_panels",
    "predecessors": [
      "A4240",
      "A4250"
    ],
    "successors": [
      "A4320"
    ]
  },
  {
    "id": "2071",
    "code": "A4320",
    "name": "Install Multi-Layer Roof Insulation & TPO Waterproof Membrane",
    "wbs_id": "143",
    "wbs_code": "4.3-ENVEL",
    "wbs_name": "4.3 Building Envelope, Facade & Weatherproofing",
    "duration": 25,
    "type": "TT_Task",
    "start": "2028-05-08",
    "finish": "2028-06-12",
    "startTimestamp": 1841360400000,
    "finishTimestamp": 1844384400000,
    "late_start": "2028-05-08",
    "late_finish": "2028-06-12",
    "total_float": 0,
    "is_critical": true,
    "phase": 4,
    "tag": "roof_membrane",
    "predecessors": [
      "A4310"
    ],
    "successors": [
      "A4330"
    ]
  },
  {
    "id": "2072",
    "code": "A4330",
    "name": "Perform 48-Hour Roof Ponding & Flood Water Test",
    "wbs_id": "143",
    "wbs_code": "4.3-ENVEL",
    "wbs_name": "4.3 Building Envelope, Facade & Weatherproofing",
    "duration": 5,
    "type": "TT_Task",
    "start": "2028-06-12",
    "finish": "2028-06-19",
    "startTimestamp": 1844384400000,
    "finishTimestamp": 1844989200000,
    "late_start": "2028-06-12",
    "late_finish": "2028-06-19",
    "total_float": 0,
    "is_critical": true,
    "phase": 4,
    "tag": "roof_membrane",
    "predecessors": [
      "A4320"
    ],
    "successors": [
      "A4340"
    ]
  },
  {
    "id": "2073",
    "code": "A4340",
    "name": "Install Exterior Louvers, Blast Doors & Penetration Seals",
    "wbs_id": "143",
    "wbs_code": "4.3-ENVEL",
    "wbs_name": "4.3 Building Envelope, Facade & Weatherproofing",
    "duration": 20,
    "type": "TT_Task",
    "start": "2028-06-19",
    "finish": "2028-07-17",
    "startTimestamp": 1844989200000,
    "finishTimestamp": 1847408400000,
    "late_start": "2028-06-19",
    "late_finish": "2028-07-17",
    "total_float": 0,
    "is_critical": true,
    "phase": 4,
    "tag": "envelope_doors",
    "predecessors": [
      "A4330"
    ],
    "successors": [
      "M4350"
    ]
  },
  {
    "id": "2074",
    "code": "M4350",
    "name": "Building Shell 100% Weather-Tight Milestone",
    "wbs_id": "143",
    "wbs_code": "4.3-ENVEL",
    "wbs_name": "4.3 Building Envelope, Facade & Weatherproofing",
    "duration": 0,
    "type": "TT_FinMile",
    "start": "2028-07-17",
    "finish": "2028-07-17",
    "startTimestamp": 1847408400000,
    "finishTimestamp": 1847408400000,
    "late_start": "2028-07-17",
    "late_finish": "2028-07-17",
    "total_float": 0,
    "is_critical": true,
    "phase": 4,
    "tag": "envelope_doors",
    "predecessors": [
      "A4340"
    ],
    "successors": [
      "A5110",
      "A5210",
      "A5310",
      "A5330",
      "A5410",
      "A5430",
      "A5480"
    ]
  },
  {
    "id": "2080",
    "code": "A5110",
    "name": "Rig & Position 110kV/22kV Substation Transformers",
    "wbs_id": "151",
    "wbs_code": "5.1-ELEC",
    "wbs_name": "5.1 110kV/22kV Substation & High/Medium Voltage Distribution",
    "duration": 20,
    "type": "TT_Task",
    "start": "2028-07-17",
    "finish": "2028-08-14",
    "startTimestamp": 1847408400000,
    "finishTimestamp": 1849827600000,
    "late_start": "2028-08-07",
    "late_finish": "2028-09-04",
    "total_float": 15,
    "is_critical": false,
    "phase": 5,
    "tag": "substation",
    "predecessors": [
      "M4350",
      "A3010"
    ],
    "successors": [
      "A5120"
    ]
  },
  {
    "id": "2090",
    "code": "A5210",
    "name": "Install Underground Bulk Fuel Tanks & Fuel Polishing Skid",
    "wbs_id": "152",
    "wbs_code": "5.2-GEN",
    "wbs_name": "5.2 Emergency Generator Farm & Fuel Storage Facility",
    "duration": 25,
    "type": "TT_Task",
    "start": "2028-07-17",
    "finish": "2028-08-21",
    "startTimestamp": 1847408400000,
    "finishTimestamp": 1850432400000,
    "late_start": "2028-08-28",
    "late_finish": "2028-10-02",
    "total_float": 30,
    "is_critical": false,
    "phase": 5,
    "tag": "generators",
    "predecessors": [
      "M4350",
      "A3040"
    ],
    "successors": [
      "A5220"
    ]
  },
  {
    "id": "2100",
    "code": "A5310",
    "name": "Rig & Level 6x 1200 RT Centrifugal Water Chillers",
    "wbs_id": "153",
    "wbs_code": "5.3-MECH",
    "wbs_name": "5.3 Central Chilled Water Plant & Hydronic Piping",
    "duration": 25,
    "type": "TT_Task",
    "start": "2028-07-17",
    "finish": "2028-08-21",
    "startTimestamp": 1847408400000,
    "finishTimestamp": 1850432400000,
    "late_start": "2028-07-17",
    "late_finish": "2028-08-21",
    "total_float": 0,
    "is_critical": true,
    "phase": 5,
    "tag": "chillers",
    "predecessors": [
      "M4350",
      "A3070"
    ],
    "successors": [
      "A5320"
    ]
  },
  {
    "id": "2102",
    "code": "A5330",
    "name": "Assemble Rooftop Induced-Draft Cooling Towers & Basins",
    "wbs_id": "153",
    "wbs_code": "5.3-MECH",
    "wbs_name": "5.3 Central Chilled Water Plant & Hydronic Piping",
    "duration": 25,
    "type": "TT_Task",
    "start": "2028-07-17",
    "finish": "2028-08-21",
    "startTimestamp": 1847408400000,
    "finishTimestamp": 1850432400000,
    "late_start": "2028-08-14",
    "late_finish": "2028-09-18",
    "total_float": 20,
    "is_critical": false,
    "phase": 5,
    "tag": "cooling_towers",
    "predecessors": [
      "M4350",
      "A3080"
    ],
    "successors": [
      "A5340"
    ]
  },
  {
    "id": "2110",
    "code": "A5410",
    "name": "Rig & Install Static UPS Modules & Input/Output Switchboards",
    "wbs_id": "154",
    "wbs_code": "5.4-WS",
    "wbs_name": "5.4 Data Halls White Space Fit-Out (Halls 1-4)",
    "duration": 30,
    "type": "TT_Task",
    "start": "2028-07-17",
    "finish": "2028-08-28",
    "startTimestamp": 1847408400000,
    "finishTimestamp": 1851037200000,
    "late_start": "2028-10-30",
    "late_finish": "2028-12-11",
    "total_float": 75,
    "is_critical": false,
    "phase": 6,
    "tag": "ups_batteries",
    "predecessors": [
      "M4350",
      "A3050"
    ],
    "successors": [
      "A5420",
      "A5520"
    ]
  },
  {
    "id": "2112",
    "code": "A5430",
    "name": "Install Anti-Static Raised Access Flooring (800mm void height)",
    "wbs_id": "154",
    "wbs_code": "5.4-WS",
    "wbs_name": "5.4 Data Halls White Space Fit-Out (Halls 1-4)",
    "duration": 25,
    "type": "TT_Task",
    "start": "2028-07-17",
    "finish": "2028-08-21",
    "startTimestamp": 1847408400000,
    "finishTimestamp": 1850432400000,
    "late_start": "2028-10-09",
    "late_finish": "2028-11-13",
    "total_float": 60,
    "is_critical": false,
    "phase": 6,
    "tag": "raised_floor",
    "predecessors": [
      "M4350"
    ],
    "successors": [
      "A5440",
      "A5450",
      "A5530",
      "A5550"
    ]
  },
  {
    "id": "2117",
    "code": "A5480",
    "name": "Fit-Out Meet-Me-Rooms (MMR-A & MMR-B) & Diverse Fiber Ducting",
    "wbs_id": "154",
    "wbs_code": "5.4-WS",
    "wbs_name": "5.4 Data Halls White Space Fit-Out (Halls 1-4)",
    "duration": 25,
    "type": "TT_Task",
    "start": "2028-07-17",
    "finish": "2028-08-21",
    "startTimestamp": 1847408400000,
    "finishTimestamp": 1850432400000,
    "late_start": "2028-11-13",
    "late_finish": "2028-12-18",
    "total_float": 85,
    "is_critical": false,
    "phase": 6,
    "tag": "white_space",
    "predecessors": [
      "M4350"
    ],
    "successors": [
      "A5560"
    ]
  },
  {
    "id": "2081",
    "code": "A5120",
    "name": "Install 22kV Gas Insulated Switchgear (GIS) Lineups A & B",
    "wbs_id": "151",
    "wbs_code": "5.1-ELEC",
    "wbs_name": "5.1 110kV/22kV Substation & High/Medium Voltage Distribution",
    "duration": 25,
    "type": "TT_Task",
    "start": "2028-08-14",
    "finish": "2028-09-18",
    "startTimestamp": 1849827600000,
    "finishTimestamp": 1852851600000,
    "late_start": "2028-09-04",
    "late_finish": "2028-10-09",
    "total_float": 15,
    "is_critical": false,
    "phase": 5,
    "tag": "substation",
    "predecessors": [
      "A5110",
      "A3020"
    ],
    "successors": [
      "A5130",
      "A5250"
    ]
  },
  {
    "id": "2091",
    "code": "A5220",
    "name": "Rig & Mount 16x 2.5MVA Standby Diesel Generators on Spring Isolators",
    "wbs_id": "152",
    "wbs_code": "5.2-GEN",
    "wbs_name": "5.2 Emergency Generator Farm & Fuel Storage Facility",
    "duration": 30,
    "type": "TT_Task",
    "start": "2028-08-21",
    "finish": "2028-10-02",
    "startTimestamp": 1850432400000,
    "finishTimestamp": 1854061200000,
    "late_start": "2028-10-02",
    "late_finish": "2028-11-13",
    "total_float": 30,
    "is_critical": false,
    "phase": 5,
    "tag": "generators",
    "predecessors": [
      "A5210",
      "A3030"
    ],
    "successors": [
      "A5230",
      "A5240"
    ]
  },
  {
    "id": "2101",
    "code": "A5320",
    "name": "Install Primary & Secondary Chilled Water Pumps & VFDs",
    "wbs_id": "153",
    "wbs_code": "5.3-MECH",
    "wbs_name": "5.3 Central Chilled Water Plant & Hydronic Piping",
    "duration": 20,
    "type": "TT_Task",
    "start": "2028-08-21",
    "finish": "2028-09-18",
    "startTimestamp": 1850432400000,
    "finishTimestamp": 1852851600000,
    "late_start": "2028-08-21",
    "late_finish": "2028-09-18",
    "total_float": 0,
    "is_critical": true,
    "phase": 5,
    "tag": "chillers",
    "predecessors": [
      "A5310"
    ],
    "successors": [
      "A5340"
    ]
  },
  {
    "id": "2111",
    "code": "A5420",
    "name": "Erect Lithium-Ion Battery Racks, DC Cabling & Battery Breakers",
    "wbs_id": "154",
    "wbs_code": "5.4-WS",
    "wbs_name": "5.4 Data Halls White Space Fit-Out (Halls 1-4)",
    "duration": 25,
    "type": "TT_Task",
    "start": "2028-08-28",
    "finish": "2028-10-02",
    "startTimestamp": 1851037200000,
    "finishTimestamp": 1854061200000,
    "late_start": "2028-12-11",
    "late_finish": "2029-01-15",
    "total_float": 75,
    "is_critical": false,
    "phase": 6,
    "tag": "ups_batteries",
    "predecessors": [
      "A5410",
      "A3060"
    ],
    "successors": [
      "M5570"
    ]
  },
  {
    "id": "2113",
    "code": "A5440",
    "name": "Suspend Overhead 415V Plug-in Busways across Data Halls 1-4",
    "wbs_id": "154",
    "wbs_code": "5.4-WS",
    "wbs_name": "5.4 Data Halls White Space Fit-Out (Halls 1-4)",
    "duration": 25,
    "type": "TT_Task",
    "start": "2028-08-21",
    "finish": "2028-09-25",
    "startTimestamp": 1850432400000,
    "finishTimestamp": 1853456400000,
    "late_start": "2028-11-13",
    "late_finish": "2028-12-18",
    "total_float": 60,
    "is_critical": false,
    "phase": 6,
    "tag": "overhead_busways",
    "predecessors": [
      "A5430",
      "A3100"
    ],
    "successors": [
      "A5470"
    ]
  },
  {
    "id": "2114",
    "code": "A5450",
    "name": "Position & Anchor 72x CRAH Units on Structural Pedestals",
    "wbs_id": "154",
    "wbs_code": "5.4-WS",
    "wbs_name": "5.4 Data Halls White Space Fit-Out (Halls 1-4)",
    "duration": 25,
    "type": "TT_Task",
    "start": "2028-08-21",
    "finish": "2028-09-25",
    "startTimestamp": 1850432400000,
    "finishTimestamp": 1853456400000,
    "late_start": "2028-11-13",
    "late_finish": "2028-12-18",
    "total_float": 60,
    "is_critical": false,
    "phase": 6,
    "tag": "crah_units",
    "predecessors": [
      "A5430",
      "A3090"
    ],
    "successors": [
      "A5460"
    ]
  },
  {
    "id": "2122",
    "code": "A5530",
    "name": "Install Aspirating Smoke Detection (VESDA) Pipe Networks",
    "wbs_id": "155",
    "wbs_code": "5.5-ICT",
    "wbs_name": "5.5 BMS, EPMS, Fire Life Safety & Security Systems",
    "duration": 20,
    "type": "TT_Task",
    "start": "2028-08-21",
    "finish": "2028-09-18",
    "startTimestamp": 1850432400000,
    "finishTimestamp": 1852851600000,
    "late_start": "2028-11-20",
    "late_finish": "2028-12-18",
    "total_float": 65,
    "is_critical": false,
    "phase": 6,
    "tag": "bms_fire",
    "predecessors": [
      "A5430"
    ],
    "successors": [
      "A5540"
    ]
  },
  {
    "id": "2124",
    "code": "A5550",
    "name": "Install Double-Interlock Pre-Action Sprinkler Piping in Data Halls",
    "wbs_id": "155",
    "wbs_code": "5.5-ICT",
    "wbs_name": "5.5 BMS, EPMS, Fire Life Safety & Security Systems",
    "duration": 25,
    "type": "TT_Task",
    "start": "2028-08-21",
    "finish": "2028-09-25",
    "startTimestamp": 1850432400000,
    "finishTimestamp": 1853456400000,
    "late_start": "2028-12-11",
    "late_finish": "2029-01-15",
    "total_float": 80,
    "is_critical": false,
    "phase": 6,
    "tag": "bms_fire",
    "predecessors": [
      "A5430"
    ],
    "successors": [
      "M5570"
    ]
  },
  {
    "id": "2125",
    "code": "A5560",
    "name": "Install Access Control, CCTV & Biometric Security Man-Traps",
    "wbs_id": "155",
    "wbs_code": "5.5-ICT",
    "wbs_name": "5.5 BMS, EPMS, Fire Life Safety & Security Systems",
    "duration": 20,
    "type": "TT_Task",
    "start": "2028-08-21",
    "finish": "2028-09-18",
    "startTimestamp": 1850432400000,
    "finishTimestamp": 1852851600000,
    "late_start": "2028-12-18",
    "late_finish": "2029-01-15",
    "total_float": 85,
    "is_critical": false,
    "phase": 6,
    "tag": "bms_fire",
    "predecessors": [
      "A5480"
    ],
    "successors": [
      "M5570"
    ]
  },
  {
    "id": "2082",
    "code": "A5130",
    "name": "Pull, Terminate & Splice 22kV Heavy Armored Feeders",
    "wbs_id": "151",
    "wbs_code": "5.1-ELEC",
    "wbs_name": "5.1 110kV/22kV Substation & High/Medium Voltage Distribution",
    "duration": 20,
    "type": "TT_Task",
    "start": "2028-09-18",
    "finish": "2028-10-16",
    "startTimestamp": 1852851600000,
    "finishTimestamp": 1855270800000,
    "late_start": "2028-10-09",
    "late_finish": "2028-11-06",
    "total_float": 15,
    "is_critical": false,
    "phase": 5,
    "tag": "substation",
    "predecessors": [
      "A5120"
    ],
    "successors": [
      "A5140"
    ]
  },
  {
    "id": "2092",
    "code": "A5230",
    "name": "Install Generator Sound-Attenuated Exhaust Stacks & Silencers",
    "wbs_id": "152",
    "wbs_code": "5.2-GEN",
    "wbs_name": "5.2 Emergency Generator Farm & Fuel Storage Facility",
    "duration": 20,
    "type": "TT_Task",
    "start": "2028-10-02",
    "finish": "2028-10-30",
    "startTimestamp": 1854061200000,
    "finishTimestamp": 1856480400000,
    "late_start": "2028-12-18",
    "late_finish": "2029-01-15",
    "total_float": 55,
    "is_critical": false,
    "phase": 5,
    "tag": "generators",
    "predecessors": [
      "A5220"
    ],
    "successors": [
      "M5570"
    ]
  },
  {
    "id": "2093",
    "code": "A5240",
    "name": "Connect Day Tanks, Redundant Fuel Pumps & Return Piping",
    "wbs_id": "152",
    "wbs_code": "5.2-GEN",
    "wbs_name": "5.2 Emergency Generator Farm & Fuel Storage Facility",
    "duration": 20,
    "type": "TT_Task",
    "start": "2028-10-02",
    "finish": "2028-10-30",
    "startTimestamp": 1854061200000,
    "finishTimestamp": 1856480400000,
    "late_start": "2028-11-13",
    "late_finish": "2028-12-11",
    "total_float": 30,
    "is_critical": false,
    "phase": 5,
    "tag": "generators",
    "predecessors": [
      "A5220"
    ],
    "successors": [
      "A5250"
    ]
  },
  {
    "id": "2103",
    "code": "A5340",
    "name": "Weld Carbon Steel Chilled Water Header Loops (DN400/DN500)",
    "wbs_id": "153",
    "wbs_code": "5.3-MECH",
    "wbs_name": "5.3 Central Chilled Water Plant & Hydronic Piping",
    "duration": 35,
    "type": "TT_Task",
    "start": "2028-09-18",
    "finish": "2028-11-06",
    "startTimestamp": 1852851600000,
    "finishTimestamp": 1857085200000,
    "late_start": "2028-09-18",
    "late_finish": "2028-11-06",
    "total_float": 0,
    "is_critical": true,
    "phase": 5,
    "tag": "chillers",
    "predecessors": [
      "A5320",
      "A5330"
    ],
    "successors": [
      "A5350"
    ]
  },
  {
    "id": "2116",
    "code": "A5470",
    "name": "Erect Hot Aisle Containment (HAC) Roof Panels & End Doors",
    "wbs_id": "154",
    "wbs_code": "5.4-WS",
    "wbs_name": "5.4 Data Halls White Space Fit-Out (Halls 1-4)",
    "duration": 20,
    "type": "TT_Task",
    "start": "2028-09-25",
    "finish": "2028-10-23",
    "startTimestamp": 1853456400000,
    "finishTimestamp": 1855875600000,
    "late_start": "2028-12-18",
    "late_finish": "2029-01-15",
    "total_float": 60,
    "is_critical": false,
    "phase": 6,
    "tag": "server_racks_hac",
    "predecessors": [
      "A5440",
      "A3110"
    ],
    "successors": [
      "M5570"
    ]
  },
  {
    "id": "2123",
    "code": "A5540",
    "name": "Install Clean Agent Gas Fire Suppression (Novec 1230 Cylinders & Nozzles)",
    "wbs_id": "155",
    "wbs_code": "5.5-ICT",
    "wbs_name": "5.5 BMS, EPMS, Fire Life Safety & Security Systems",
    "duration": 20,
    "type": "TT_Task",
    "start": "2028-09-18",
    "finish": "2028-10-16",
    "startTimestamp": 1852851600000,
    "finishTimestamp": 1855270800000,
    "late_start": "2028-12-18",
    "late_finish": "2029-01-15",
    "total_float": 65,
    "is_critical": false,
    "phase": 6,
    "tag": "bms_fire",
    "predecessors": [
      "A5530"
    ],
    "successors": [
      "M5570"
    ]
  },
  {
    "id": "2083",
    "code": "A5140",
    "name": "Very Low Frequency (VLF) Hi-Pot & Tan-Delta Cable Testing",
    "wbs_id": "151",
    "wbs_code": "5.1-ELEC",
    "wbs_name": "5.1 110kV/22kV Substation & High/Medium Voltage Distribution",
    "duration": 10,
    "type": "TT_Task",
    "start": "2028-10-16",
    "finish": "2028-10-30",
    "startTimestamp": 1855270800000,
    "finishTimestamp": 1856480400000,
    "late_start": "2028-11-06",
    "late_finish": "2028-11-20",
    "total_float": 15,
    "is_critical": false,
    "phase": 5,
    "tag": "substation",
    "predecessors": [
      "A5130"
    ],
    "successors": [
      "A5150"
    ]
  },
  {
    "id": "2094",
    "code": "A5250",
    "name": "Install Generator Paralleling Switchgear & Master Control Board",
    "wbs_id": "152",
    "wbs_code": "5.2-GEN",
    "wbs_name": "5.2 Emergency Generator Farm & Fuel Storage Facility",
    "duration": 25,
    "type": "TT_Task",
    "start": "2028-10-30",
    "finish": "2028-12-04",
    "startTimestamp": 1856480400000,
    "finishTimestamp": 1859504400000,
    "late_start": "2028-12-11",
    "late_finish": "2029-01-15",
    "total_float": 30,
    "is_critical": false,
    "phase": 5,
    "tag": "generators",
    "predecessors": [
      "A5240",
      "A5120"
    ],
    "successors": [
      "M5570"
    ]
  },
  {
    "id": "2104",
    "code": "A5350",
    "name": "Perform Hydrostatic Pressure Test on Chilled Water Piping (1.5x WP)",
    "wbs_id": "153",
    "wbs_code": "5.3-MECH",
    "wbs_name": "5.3 Central Chilled Water Plant & Hydronic Piping",
    "duration": 10,
    "type": "TT_Task",
    "start": "2028-11-06",
    "finish": "2028-11-20",
    "startTimestamp": 1857085200000,
    "finishTimestamp": 1858294800000,
    "late_start": "2028-11-06",
    "late_finish": "2028-11-20",
    "total_float": 0,
    "is_critical": true,
    "phase": 5,
    "tag": "chillers",
    "predecessors": [
      "A5340"
    ],
    "successors": [
      "A5360"
    ]
  },
  {
    "id": "2084",
    "code": "A5150",
    "name": "Install 22kV/415V Cast Resin Distribution Transformers",
    "wbs_id": "151",
    "wbs_code": "5.1-ELEC",
    "wbs_name": "5.1 110kV/22kV Substation & High/Medium Voltage Distribution",
    "duration": 15,
    "type": "TT_Task",
    "start": "2028-10-30",
    "finish": "2028-11-20",
    "startTimestamp": 1856480400000,
    "finishTimestamp": 1858294800000,
    "late_start": "2028-11-20",
    "late_finish": "2028-12-11",
    "total_float": 15,
    "is_critical": false,
    "phase": 5,
    "tag": "substation",
    "predecessors": [
      "A5140"
    ],
    "successors": [
      "A5510",
      "A5520",
      "M5570"
    ]
  },
  {
    "id": "2105",
    "code": "A5360",
    "name": "Flushing, Chemical Passivation & Thermal Insulation of Piping",
    "wbs_id": "153",
    "wbs_code": "5.3-MECH",
    "wbs_name": "5.3 Central Chilled Water Plant & Hydronic Piping",
    "duration": 15,
    "type": "TT_Task",
    "start": "2028-11-20",
    "finish": "2028-12-11",
    "startTimestamp": 1858294800000,
    "finishTimestamp": 1860109200000,
    "late_start": "2028-11-20",
    "late_finish": "2028-12-11",
    "total_float": 0,
    "is_critical": true,
    "phase": 5,
    "tag": "chillers",
    "predecessors": [
      "A5350"
    ],
    "successors": [
      "A5460",
      "A5510"
    ]
  },
  {
    "id": "2121",
    "code": "A5520",
    "name": "Deploy EPMS Smart Power Meters & High-Speed Modbus/Ethernet",
    "wbs_id": "155",
    "wbs_code": "5.5-ICT",
    "wbs_name": "5.5 BMS, EPMS, Fire Life Safety & Security Systems",
    "duration": 25,
    "type": "TT_Task",
    "start": "2028-11-20",
    "finish": "2028-12-25",
    "startTimestamp": 1858294800000,
    "finishTimestamp": 1861318800000,
    "late_start": "2028-12-11",
    "late_finish": "2029-01-15",
    "total_float": 15,
    "is_critical": false,
    "phase": 6,
    "tag": "bms_fire",
    "predecessors": [
      "A5150",
      "A5410"
    ],
    "successors": [
      "M5570"
    ]
  },
  {
    "id": "2115",
    "code": "A5460",
    "name": "Connect Underfloor Chilled Water Dual-Feed Flexible Run-Outs",
    "wbs_id": "154",
    "wbs_code": "5.4-WS",
    "wbs_name": "5.4 Data Halls White Space Fit-Out (Halls 1-4)",
    "duration": 20,
    "type": "TT_Task",
    "start": "2028-12-11",
    "finish": "2029-01-08",
    "startTimestamp": 1860109200000,
    "finishTimestamp": 1862528400000,
    "late_start": "2028-12-18",
    "late_finish": "2029-01-15",
    "total_float": 5,
    "is_critical": false,
    "phase": 6,
    "tag": "crah_units",
    "predecessors": [
      "A5450",
      "A5360"
    ],
    "successors": [
      "M5570"
    ]
  },
  {
    "id": "2120",
    "code": "A5510",
    "name": "Mount BMS DDC Panels & Field Sensor Wiring (Temp/RH/Flow)",
    "wbs_id": "155",
    "wbs_code": "5.5-ICT",
    "wbs_name": "5.5 BMS, EPMS, Fire Life Safety & Security Systems",
    "duration": 25,
    "type": "TT_Task",
    "start": "2028-12-11",
    "finish": "2029-01-15",
    "startTimestamp": 1860109200000,
    "finishTimestamp": 1863133200000,
    "late_start": "2028-12-11",
    "late_finish": "2029-01-15",
    "total_float": 0,
    "is_critical": true,
    "phase": 6,
    "tag": "bms_fire",
    "predecessors": [
      "A5150",
      "A5360"
    ],
    "successors": [
      "M5570"
    ]
  },
  {
    "id": "2126",
    "code": "M5570",
    "name": "MEP Infrastructure & White Space Fit-Out Completion Milestone",
    "wbs_id": "155",
    "wbs_code": "5.5-ICT",
    "wbs_name": "5.5 BMS, EPMS, Fire Life Safety & Security Systems",
    "duration": 0,
    "type": "TT_FinMile",
    "start": "2029-01-15",
    "finish": "2029-01-15",
    "startTimestamp": 1863133200000,
    "finishTimestamp": 1863133200000,
    "late_start": "2029-01-15",
    "late_finish": "2029-01-15",
    "total_float": 0,
    "is_critical": true,
    "phase": 6,
    "tag": "bms_fire",
    "predecessors": [
      "A5150",
      "A5230",
      "A5250",
      "A5420",
      "A5460",
      "A5470",
      "A5510",
      "A5520",
      "A5540",
      "A5550",
      "A5560"
    ],
    "successors": [
      "A6210",
      "A6230",
      "A6250"
    ]
  },
  {
    "id": "2140",
    "code": "A6210",
    "name": "Static Wire Insulation Resistance (Megger) & Continuity Testing",
    "wbs_id": "162",
    "wbs_code": "6.2-L3",
    "wbs_name": "6.2 Cx Level 3: Pre-Functional Static Component Testing",
    "duration": 15,
    "type": "TT_Task",
    "start": "2029-01-15",
    "finish": "2029-02-05",
    "startTimestamp": 1863133200000,
    "finishTimestamp": 1864947600000,
    "late_start": "2029-01-15",
    "late_finish": "2029-02-05",
    "total_float": 0,
    "is_critical": true,
    "phase": 7,
    "tag": "cx_static",
    "predecessors": [
      "M5570",
      "A6130"
    ],
    "successors": [
      "A6220"
    ]
  },
  {
    "id": "2142",
    "code": "A6230",
    "name": "Chilled Water Loop Static Fill, Venting & Nitrogen Leak Test",
    "wbs_id": "162",
    "wbs_code": "6.2-L3",
    "wbs_name": "6.2 Cx Level 3: Pre-Functional Static Component Testing",
    "duration": 10,
    "type": "TT_Task",
    "start": "2029-01-15",
    "finish": "2029-01-29",
    "startTimestamp": 1863133200000,
    "finishTimestamp": 1864342800000,
    "late_start": "2029-02-12",
    "late_finish": "2029-02-26",
    "total_float": 20,
    "is_critical": false,
    "phase": 7,
    "tag": "cx_static",
    "predecessors": [
      "M5570"
    ],
    "successors": [
      "A6240"
    ]
  },
  {
    "id": "2144",
    "code": "A6250",
    "name": "VESDA Smoke Particle Sensitivity & Aerosol Test",
    "wbs_id": "162",
    "wbs_code": "6.2-L3",
    "wbs_name": "6.2 Cx Level 3: Pre-Functional Static Component Testing",
    "duration": 10,
    "type": "TT_Task",
    "start": "2029-01-15",
    "finish": "2029-01-29",
    "startTimestamp": 1863133200000,
    "finishTimestamp": 1864342800000,
    "late_start": "2029-03-05",
    "late_finish": "2029-03-19",
    "total_float": 35,
    "is_critical": false,
    "phase": 7,
    "tag": "cx_static",
    "predecessors": [
      "M5570"
    ],
    "successors": [
      "M6260",
      "A6360"
    ]
  },
  {
    "id": "2141",
    "code": "A6220",
    "name": "Protective Relay Secondary Current Injection & Trip Settings Test",
    "wbs_id": "162",
    "wbs_code": "6.2-L3",
    "wbs_name": "6.2 Cx Level 3: Pre-Functional Static Component Testing",
    "duration": 15,
    "type": "TT_Task",
    "start": "2029-02-05",
    "finish": "2029-02-26",
    "startTimestamp": 1864947600000,
    "finishTimestamp": 1866762000000,
    "late_start": "2029-02-05",
    "late_finish": "2029-02-26",
    "total_float": 0,
    "is_critical": true,
    "phase": 7,
    "tag": "cx_static",
    "predecessors": [
      "A6210"
    ],
    "successors": [
      "A6240"
    ]
  },
  {
    "id": "2155",
    "code": "A6360",
    "name": "Pre-Action Sprinkler & Fire Alarm Integration Dry Trip Test",
    "wbs_id": "163",
    "wbs_code": "6.3-L4",
    "wbs_name": "6.3 Cx Level 4: Functional System Dynamic Performance",
    "duration": 10,
    "type": "TT_Task",
    "start": "2029-01-29",
    "finish": "2029-02-12",
    "startTimestamp": 1864342800000,
    "finishTimestamp": 1865552400000,
    "late_start": "2029-04-30",
    "late_finish": "2029-05-14",
    "total_float": 65,
    "is_critical": false,
    "phase": 7,
    "tag": "cx_dynamic",
    "predecessors": [
      "A6250"
    ],
    "successors": [
      "M6370"
    ]
  },
  {
    "id": "2143",
    "code": "A6240",
    "name": "BMS Point-to-Point Sensor Calibration & Control Valve Stroking",
    "wbs_id": "162",
    "wbs_code": "6.2-L3",
    "wbs_name": "6.2 Cx Level 3: Pre-Functional Static Component Testing",
    "duration": 15,
    "type": "TT_Task",
    "start": "2029-02-26",
    "finish": "2029-03-19",
    "startTimestamp": 1866762000000,
    "finishTimestamp": 1868576400000,
    "late_start": "2029-02-26",
    "late_finish": "2029-03-19",
    "total_float": 0,
    "is_critical": true,
    "phase": 7,
    "tag": "cx_static",
    "predecessors": [
      "A6220",
      "A6230"
    ],
    "successors": [
      "M6260"
    ]
  },
  {
    "id": "2145",
    "code": "M6260",
    "name": "Pre-Functional Static Energization Ready Milestone",
    "wbs_id": "162",
    "wbs_code": "6.2-L3",
    "wbs_name": "6.2 Cx Level 3: Pre-Functional Static Component Testing",
    "duration": 0,
    "type": "TT_FinMile",
    "start": "2029-03-19",
    "finish": "2029-03-19",
    "startTimestamp": 1868576400000,
    "finishTimestamp": 1868576400000,
    "late_start": "2029-03-19",
    "late_finish": "2029-03-19",
    "total_float": 0,
    "is_critical": true,
    "phase": 7,
    "tag": "cx_static",
    "predecessors": [
      "A6240",
      "A6250"
    ],
    "successors": [
      "A6310"
    ]
  },
  {
    "id": "2150",
    "code": "A6310",
    "name": "Initial 22kV Energization from Utility Substation",
    "wbs_id": "163",
    "wbs_code": "6.3-L4",
    "wbs_name": "6.3 Cx Level 4: Functional System Dynamic Performance",
    "duration": 10,
    "type": "TT_Task",
    "start": "2029-03-19",
    "finish": "2029-04-02",
    "startTimestamp": 1868576400000,
    "finishTimestamp": 1869786000000,
    "late_start": "2029-03-19",
    "late_finish": "2029-04-02",
    "total_float": 0,
    "is_critical": true,
    "phase": 7,
    "tag": "cx_dynamic",
    "predecessors": [
      "M6260",
      "A1030"
    ],
    "successors": [
      "A6320",
      "A6330",
      "A6340"
    ]
  },
  {
    "id": "2151",
    "code": "A6320",
    "name": "Standalone Generator Black-Start & 100% Resistive Load Step Test",
    "wbs_id": "163",
    "wbs_code": "6.3-L4",
    "wbs_name": "6.3 Cx Level 4: Functional System Dynamic Performance",
    "duration": 15,
    "type": "TT_Task",
    "start": "2029-04-02",
    "finish": "2029-04-23",
    "startTimestamp": 1869786000000,
    "finishTimestamp": 1871600400000,
    "late_start": "2029-04-23",
    "late_finish": "2029-05-14",
    "total_float": 15,
    "is_critical": false,
    "phase": 7,
    "tag": "cx_dynamic",
    "predecessors": [
      "A6310"
    ],
    "successors": [
      "M6370"
    ]
  },
  {
    "id": "2152",
    "code": "A6330",
    "name": "Static UPS Dynamic Load Bank Step & Battery Autonomy Run-Down Test",
    "wbs_id": "163",
    "wbs_code": "6.3-L4",
    "wbs_name": "6.3 Cx Level 4: Functional System Dynamic Performance",
    "duration": 15,
    "type": "TT_Task",
    "start": "2029-04-02",
    "finish": "2029-04-23",
    "startTimestamp": 1869786000000,
    "finishTimestamp": 1871600400000,
    "late_start": "2029-04-23",
    "late_finish": "2029-05-14",
    "total_float": 15,
    "is_critical": false,
    "phase": 7,
    "tag": "cx_dynamic",
    "predecessors": [
      "A6310"
    ],
    "successors": [
      "M6370"
    ]
  },
  {
    "id": "2153",
    "code": "A6340",
    "name": "Chiller Plant Dynamic Staging, Flow Balancing & Lead-Lag Failover",
    "wbs_id": "163",
    "wbs_code": "6.3-L4",
    "wbs_name": "6.3 Cx Level 4: Functional System Dynamic Performance",
    "duration": 15,
    "type": "TT_Task",
    "start": "2029-04-02",
    "finish": "2029-04-23",
    "startTimestamp": 1869786000000,
    "finishTimestamp": 1871600400000,
    "late_start": "2029-04-02",
    "late_finish": "2029-04-23",
    "total_float": 0,
    "is_critical": true,
    "phase": 7,
    "tag": "cx_dynamic",
    "predecessors": [
      "A6310"
    ],
    "successors": [
      "A6350"
    ]
  },
  {
    "id": "2154",
    "code": "A6350",
    "name": "CRAH Fan Matrix Balancing & Airflow Static Pressure Verification",
    "wbs_id": "163",
    "wbs_code": "6.3-L4",
    "wbs_name": "6.3 Cx Level 4: Functional System Dynamic Performance",
    "duration": 15,
    "type": "TT_Task",
    "start": "2029-04-23",
    "finish": "2029-05-14",
    "startTimestamp": 1871600400000,
    "finishTimestamp": 1873414800000,
    "late_start": "2029-04-23",
    "late_finish": "2029-05-14",
    "total_float": 0,
    "is_critical": true,
    "phase": 7,
    "tag": "cx_dynamic",
    "predecessors": [
      "A6340"
    ],
    "successors": [
      "M6370"
    ]
  },
  {
    "id": "2156",
    "code": "M6370",
    "name": "Functional Performance Testing Level 4 Completed Milestone",
    "wbs_id": "163",
    "wbs_code": "6.3-L4",
    "wbs_name": "6.3 Cx Level 4: Functional System Dynamic Performance",
    "duration": 0,
    "type": "TT_FinMile",
    "start": "2029-05-14",
    "finish": "2029-05-14",
    "startTimestamp": 1873414800000,
    "finishTimestamp": 1873414800000,
    "late_start": "2029-05-14",
    "late_finish": "2029-05-14",
    "total_float": 0,
    "is_critical": true,
    "phase": 7,
    "tag": "cx_dynamic",
    "predecessors": [
      "A6320",
      "A6330",
      "A6350",
      "A6360"
    ],
    "successors": [
      "A6410"
    ]
  },
  {
    "id": "2160",
    "code": "A6410",
    "name": "Deploy & Terminate 36MW Portable Resistive-Reactive Load Banks",
    "wbs_id": "164",
    "wbs_code": "6.4-L5",
    "wbs_name": "6.4 Cx Level 5: Integrated Systems Testing (IST with 36MW Load)",
    "duration": 15,
    "type": "TT_Task",
    "start": "2029-05-14",
    "finish": "2029-06-04",
    "startTimestamp": 1873414800000,
    "finishTimestamp": 1875229200000,
    "late_start": "2029-05-14",
    "late_finish": "2029-06-04",
    "total_float": 0,
    "is_critical": true,
    "phase": 7,
    "tag": "cx_load_banks",
    "predecessors": [
      "M6370"
    ],
    "successors": [
      "A6420"
    ]
  },
  {
    "id": "2161",
    "code": "A6420",
    "name": "Perform Full-Load 36MW Continuous 48-Hour Thermal Heat Soak Run",
    "wbs_id": "164",
    "wbs_code": "6.4-L5",
    "wbs_name": "6.4 Cx Level 5: Integrated Systems Testing (IST with 36MW Load)",
    "duration": 10,
    "type": "TT_Task",
    "start": "2029-06-04",
    "finish": "2029-06-18",
    "startTimestamp": 1875229200000,
    "finishTimestamp": 1876438800000,
    "late_start": "2029-06-04",
    "late_finish": "2029-06-18",
    "total_float": 0,
    "is_critical": true,
    "phase": 7,
    "tag": "cx_load_banks",
    "predecessors": [
      "A6410"
    ],
    "successors": [
      "A6430"
    ]
  },
  {
    "id": "2162",
    "code": "A6430",
    "name": "IST Scenario 1: Utility Grid Total Blackout Simulation (<10s ATS to Genset)",
    "wbs_id": "164",
    "wbs_code": "6.4-L5",
    "wbs_name": "6.4 Cx Level 5: Integrated Systems Testing (IST with 36MW Load)",
    "duration": 5,
    "type": "TT_Task",
    "start": "2029-06-18",
    "finish": "2029-06-25",
    "startTimestamp": 1876438800000,
    "finishTimestamp": 1877043600000,
    "late_start": "2029-06-18",
    "late_finish": "2029-06-25",
    "total_float": 0,
    "is_critical": true,
    "phase": 7,
    "tag": "cx_load_banks",
    "predecessors": [
      "A6420"
    ],
    "successors": [
      "A6440"
    ]
  },
  {
    "id": "2163",
    "code": "A6440",
    "name": "IST Scenario 2: Concurrent Maintainability UPS & Switchgear Isolation",
    "wbs_id": "164",
    "wbs_code": "6.4-L5",
    "wbs_name": "6.4 Cx Level 5: Integrated Systems Testing (IST with 36MW Load)",
    "duration": 5,
    "type": "TT_Task",
    "start": "2029-06-25",
    "finish": "2029-07-02",
    "startTimestamp": 1877043600000,
    "finishTimestamp": 1877648400000,
    "late_start": "2029-06-25",
    "late_finish": "2029-07-02",
    "total_float": 0,
    "is_critical": true,
    "phase": 7,
    "tag": "cx_load_banks",
    "predecessors": [
      "A6430"
    ],
    "successors": [
      "A6450"
    ]
  },
  {
    "id": "2164",
    "code": "A6450",
    "name": "IST Scenario 3: Chiller Plant Failure & Thermal Storage Ride-Through",
    "wbs_id": "164",
    "wbs_code": "6.4-L5",
    "wbs_name": "6.4 Cx Level 5: Integrated Systems Testing (IST with 36MW Load)",
    "duration": 5,
    "type": "TT_Task",
    "start": "2029-07-02",
    "finish": "2029-07-09",
    "startTimestamp": 1877648400000,
    "finishTimestamp": 1878253200000,
    "late_start": "2029-07-02",
    "late_finish": "2029-07-09",
    "total_float": 0,
    "is_critical": true,
    "phase": 7,
    "tag": "cx_load_banks",
    "predecessors": [
      "A6440"
    ],
    "successors": [
      "A6460"
    ]
  },
  {
    "id": "2165",
    "code": "A6460",
    "name": "Demobilize 36MW Load Banks & Clean Room Deep Decontamination",
    "wbs_id": "164",
    "wbs_code": "6.4-L5",
    "wbs_name": "6.4 Cx Level 5: Integrated Systems Testing (IST with 36MW Load)",
    "duration": 10,
    "type": "TT_Task",
    "start": "2029-07-09",
    "finish": "2029-07-23",
    "startTimestamp": 1878253200000,
    "finishTimestamp": 1879462800000,
    "late_start": "2029-07-09",
    "late_finish": "2029-07-23",
    "total_float": 0,
    "is_critical": true,
    "phase": 7,
    "tag": "cx_load_banks",
    "predecessors": [
      "A6450"
    ],
    "successors": [
      "M6470"
    ]
  },
  {
    "id": "2166",
    "code": "M6470",
    "name": "Cx Level 5 Integrated Systems Testing 100% Passed Milestone",
    "wbs_id": "164",
    "wbs_code": "6.4-L5",
    "wbs_name": "6.4 Cx Level 5: Integrated Systems Testing (IST with 36MW Load)",
    "duration": 0,
    "type": "TT_FinMile",
    "start": "2029-07-23",
    "finish": "2029-07-23",
    "startTimestamp": 1879462800000,
    "finishTimestamp": 1879462800000,
    "late_start": "2029-07-23",
    "late_finish": "2029-07-23",
    "total_float": 0,
    "is_critical": true,
    "phase": 7,
    "tag": "cx_load_banks",
    "predecessors": [
      "A6460"
    ],
    "successors": [
      "A7010",
      "A7020"
    ]
  },
  {
    "id": "2170",
    "code": "A7010",
    "name": "Local Fire Authority Final Code Compliance Inspection & Sign-Off",
    "wbs_id": "170",
    "wbs_code": "7.0-COD",
    "wbs_name": "7.0 Authority Clearance, Uptime Certification & Handover",
    "duration": 15,
    "type": "TT_Task",
    "start": "2029-07-23",
    "finish": "2029-08-13",
    "startTimestamp": 1879462800000,
    "finishTimestamp": 1881277200000,
    "late_start": "2029-07-23",
    "late_finish": "2029-08-13",
    "total_float": 0,
    "is_critical": true,
    "phase": 8,
    "tag": "cod_operational",
    "predecessors": [
      "M6470"
    ],
    "successors": [
      "A7030"
    ]
  },
  {
    "id": "2171",
    "code": "A7020",
    "name": "Electrical Inspectorate Final Live Operating License",
    "wbs_id": "170",
    "wbs_code": "7.0-COD",
    "wbs_name": "7.0 Authority Clearance, Uptime Certification & Handover",
    "duration": 15,
    "type": "TT_Task",
    "start": "2029-07-23",
    "finish": "2029-08-13",
    "startTimestamp": 1879462800000,
    "finishTimestamp": 1881277200000,
    "late_start": "2029-07-23",
    "late_finish": "2029-08-13",
    "total_float": 0,
    "is_critical": true,
    "phase": 8,
    "tag": "cod_operational",
    "predecessors": [
      "M6470"
    ],
    "successors": [
      "A7030"
    ]
  },
  {
    "id": "2172",
    "code": "A7030",
    "name": "Utility Dual-Feed Permanent Power Tariff Synchronization",
    "wbs_id": "170",
    "wbs_code": "7.0-COD",
    "wbs_name": "7.0 Authority Clearance, Uptime Certification & Handover",
    "duration": 10,
    "type": "TT_Task",
    "start": "2029-08-13",
    "finish": "2029-08-27",
    "startTimestamp": 1881277200000,
    "finishTimestamp": 1882486800000,
    "late_start": "2029-08-13",
    "late_finish": "2029-08-27",
    "total_float": 0,
    "is_critical": true,
    "phase": 8,
    "tag": "cod_operational",
    "predecessors": [
      "A7010",
      "A7020"
    ],
    "successors": [
      "A7040"
    ]
  },
  {
    "id": "2173",
    "code": "A7040",
    "name": "Uptime Institute Tier III Constructed Facility Site Audit",
    "wbs_id": "170",
    "wbs_code": "7.0-COD",
    "wbs_name": "7.0 Authority Clearance, Uptime Certification & Handover",
    "duration": 15,
    "type": "TT_Task",
    "start": "2029-08-27",
    "finish": "2029-09-17",
    "startTimestamp": 1882486800000,
    "finishTimestamp": 1884301200000,
    "late_start": "2029-08-27",
    "late_finish": "2029-09-17",
    "total_float": 0,
    "is_critical": true,
    "phase": 8,
    "tag": "cod_operational",
    "predecessors": [
      "A7030"
    ],
    "successors": [
      "A7050"
    ]
  },
  {
    "id": "2174",
    "code": "A7050",
    "name": "Final Client Punch-List Clearance & O&M Manual Handover",
    "wbs_id": "170",
    "wbs_code": "7.0-COD",
    "wbs_name": "7.0 Authority Clearance, Uptime Certification & Handover",
    "duration": 10,
    "type": "TT_Task",
    "start": "2029-09-17",
    "finish": "2029-10-01",
    "startTimestamp": 1884301200000,
    "finishTimestamp": 1885510800000,
    "late_start": "2029-09-17",
    "late_finish": "2029-10-01",
    "total_float": 0,
    "is_critical": true,
    "phase": 8,
    "tag": "cod_operational",
    "predecessors": [
      "A7040"
    ],
    "successors": [
      "M7060"
    ]
  },
  {
    "id": "2175",
    "code": "M7060",
    "name": "Commercial Operation Date (COD) & Final Acceptance Milestone",
    "wbs_id": "170",
    "wbs_code": "7.0-COD",
    "wbs_name": "7.0 Authority Clearance, Uptime Certification & Handover",
    "duration": 0,
    "type": "TT_FinMile",
    "start": "2029-10-01",
    "finish": "2029-10-01",
    "startTimestamp": 1885510800000,
    "finishTimestamp": 1885510800000,
    "late_start": "2029-10-01",
    "late_finish": "2029-10-01",
    "total_float": 0,
    "is_critical": true,
    "phase": 8,
    "tag": "cod_operational",
    "predecessors": [
      "A7050"
    ],
    "successors": []
  }
],
    
    // Phase metadata
    phases: [
        { id: 1, name: "Site Clearing, Bulk Excavation & Piling", start_date: "2027-01-04", finish_date: "2027-07-30", target_mw: 0 },
        { id: 2, name: "Substructure Raft Slab & Ground Plinths", start_date: "2027-08-02", finish_date: "2027-11-26", target_mw: 0 },
        { id: 3, name: "Concrete Superstructure (L1 & L2 Slabs)", start_date: "2027-11-29", finish_date: "2028-03-10", target_mw: 0 },
        { id: 4, name: "Steel Roof Trusses & Precast Facade Envelope", start_date: "2028-02-07", finish_date: "2028-07-17", target_mw: 0 },
        { id: 5, name: "Heavy MEP (110kV Substation, 16 Gensets, 6 Chillers)", start_date: "2028-07-17", finish_date: "2028-12-08", target_mw: 0 },
        { id: 6, name: "White Space Fit-Out (Halls 1-4, Busways, CRAH & Racks)", start_date: "2028-07-17", finish_date: "2029-01-15", target_mw: 0 },
        { id: 7, name: "Testing & Commissioning (Cx L1-L5, 36MW Heat Soak)", start_date: "2029-01-15", finish_date: "2029-07-23", target_mw: 36 },
        { id: 8, name: "Commercial Operation Date (COD) & Hyperscale Live", start_date: "2029-07-23", finish_date: "2029-10-01", target_mw: 36 }
    ]
};
