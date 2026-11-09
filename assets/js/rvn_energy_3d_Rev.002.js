/**
 * Renewable Viet Nam - 3D Geospatial Clean Energy Digital Twin & Engineering Asset Suite
 * Release Rev.002 (Synchronized to Apex Homepage Release Rev.043)
 * WebGL 3D Engine powered by Three.js (Procedural Buffer Geometries, Zero External 3D Weight)
 * 
 * 5X DENSITY SCALING:
 *  - 60+ National Energy Generation Hubs & 500kV Supergrid Substations (North, Central, South).
 *  - 15 Interconnected 500kV/220kV Transmission Corridors with 210 Dynamic Energy Photon Particles.
 *  - 2,250 Georeferenced EV Charging Highway & Metropolitan Nodes.
 *  - 92-Vertex High-Fidelity Coastal/Border Perimeter with Truong Son Mountain Elevation Topography.
 *  - 8 Strategic Offshore Islands & Marine Concessions (Hoang Sa, Truong Sa, Phu Quoc, Con Dao, etc.).
 *  - Mode B Engineering Asset Explorer: 5 High-Resolution 3D Models (Wind, Solar, Pylon, Transformer, BESS).
 */
(function(window) {
  'use strict';

  // 60+ Major Energy Generation Facilities, Storage Hubs & 500kV Substations
  const ENERGY_HUBS = [
    // --- NORTHERN GRID (MIEN BAC) ---
    { id: 'son_la', name: 'Sơn La Hydro Complex', category: 'hydro', mw: 2400, lat: 21.49, lng: 103.99, region: 'north', desc: 'Largest hydroelectric plant in SE Asia (6x 400MW Francis units)' },
    { id: 'hoa_binh', name: 'Hòa Bình Hydro Baseload', category: 'hydro', mw: 1920, lat: 20.81, lng: 105.32, region: 'north', desc: 'Critical northern frequency regulation & flood control' },
    { id: 'lai_chau', name: 'Lai Châu Hydroelectric Dam', category: 'hydro', mw: 1200, lat: 22.14, lng: 102.91, region: 'north', desc: 'Upstream Da River cascade hydro generator (3x 400MW)' },
    { id: 'huoi_quang', name: 'Huội Quảng Underground Hydro', category: 'hydro', mw: 520, lat: 21.72, lng: 103.88, region: 'north', desc: 'First large-scale underground hydropower cavern in Vietnam' },
    { id: 'ban_chat', name: 'Bản Chát Hydropower Plant', category: 'hydro', mw: 220, lat: 21.86, lng: 103.74, region: 'north', desc: 'Upstream Nam Mu tributary reservoir storage regulation' },
    { id: 'tuyen_quang', name: 'Tuyên Quang Hydropower', category: 'hydro', mw: 342, lat: 22.35, lng: 105.40, region: 'north', desc: 'Gam River multi-purpose flood regulation & clean power' },
    { id: 'thac_ba', name: 'Thác Bà Historic Hydro', category: 'hydro', mw: 120, lat: 21.75, lng: 105.03, region: 'north', desc: 'First hydroelectric plant constructed in Northern Vietnam' },
    { id: 'quang_ninh_lng', name: 'Quảng Ninh Energy & LNG Hub', category: 'lng', mw: 2400, lat: 21.03, lng: 107.12, region: 'north', desc: 'Northern coastal clean baseload cluster & deep-water LNG port' },
    { id: 'pho_noi', name: 'Phố Nối 500kV Supergrid Hub', category: 'substation', mw: 5000, lat: 20.93, lng: 106.05, region: 'north', desc: 'Northern terminus of 519 km 500kV Circuit-3 Supergrid' },
    { id: 'nam_dinh_1', name: 'Nam Định 1 500kV Substation', category: 'substation', mw: 4500, lat: 20.25, lng: 106.18, region: 'north', desc: 'Circuit-3 Red River Delta intertie & industrial hub' },
    { id: 'hiep_hoa', name: 'Hiệp Hòa 500kV Transmission Node', category: 'substation', mw: 4000, lat: 21.33, lng: 105.98, region: 'north', desc: 'Northern ring transmission junction serving Samsung industrial cluster' },
    { id: 'soc_son_wte', name: 'Sóc Sơn Waste-to-Energy Plant', category: 'hybrid', mw: 75, lat: 21.30, lng: 105.85, region: 'north', desc: 'Largest modern waste-to-energy incineration plant in Hanoi' },
    { id: 'thanh_hoa_500kv', name: 'Thanh Hóa 500kV Substation', category: 'substation', mw: 4500, lat: 19.80, lng: 105.77, region: 'north', desc: 'North-Central intertie node of 500kV Circuit-3 transmission' },
    { id: 'nghi_son', name: 'Nghi Sơn Strategic Energy Hub', category: 'hybrid', mw: 1800, lat: 19.33, lng: 105.78, region: 'north', desc: 'Deep-water petrochemical refinery port & LNG generation hub' },

    // --- CENTRAL GRID (MIEN TRUNG & TAY NGUYEN) ---
    { id: 'quynh_luu', name: 'Quỳnh Lưu 500kV Substation', category: 'substation', mw: 4500, lat: 19.15, lng: 105.65, region: 'central', desc: 'Circuit-3 intertie node transmitting power across Nghe An' },
    { id: 'ban_ve', name: 'Bản Vẽ Hydropower Station', category: 'hydro', mw: 320, lat: 19.31, lng: 104.49, region: 'central', desc: 'Largest reservoir in Nghe An province on the Nam Non river' },
    { id: 'vung_ang', name: 'Vũng Áng Energy & Intertie Node', category: 'substation', mw: 3600, lat: 18.02, lng: 106.38, region: 'central', desc: 'Ha Tinh deep-water port & industrial energy corridor' },
    { id: 'quang_trach', name: 'Quảng Trạch 500kV Hub', category: 'substation', mw: 5000, lat: 17.80, lng: 106.45, region: 'central', desc: 'Circuit-3 origin wheeling central clean power northward' },
    { id: 'huong_linh', name: 'Hướng Linh Wind Corridor', category: 'wind', mw: 350, lat: 16.71, lng: 106.75, region: 'central', desc: 'Quang Tri western mountain wind cluster along Highway 9' },
    { id: 'phong_dien', name: 'Phong Điền Solar Complex', category: 'solar', mw: 50, lat: 16.58, lng: 107.31, region: 'central', desc: 'First utility-scale solar PV plant commissioned in Vietnam (2018)' },
    { id: 'da_nang_500kv', name: 'Đà Nẵng 500kV Transmission Hub', category: 'substation', mw: 4000, lat: 16.05, lng: 108.15, region: 'central', desc: 'Central coastal grid backbone & Hoa Khanh hi-tech park intertie' },
    { id: 'a_vuong', name: 'A Vương Hydropower Station', category: 'hydro', mw: 210, lat: 15.86, lng: 107.64, region: 'central', desc: 'Quang Nam high-head peak load balancing plant' },
    { id: 'song_tranh_2', name: 'Sông Tranh 2 Hydropower', category: 'hydro', mw: 190, lat: 15.33, lng: 108.15, region: 'central', desc: 'Thu Bon river basin hydro facility with 730M kWh/year' },
    { id: 'quang_ngai_solar', name: 'Mộ Đức Solar Farm', category: 'solar', mw: 50, lat: 15.01, lng: 108.88, region: 'central', desc: 'Coastal Quang Ngai utility-scale photovoltaic park' },
    { id: 'yaly', name: 'Yaly Hydroelectric Complex', category: 'hydro', mw: 720, lat: 14.22, lng: 107.82, region: 'central', desc: 'Se San river flagship cascade hydropower & 360MW expansion' },
    { id: 'se_san_4', name: 'Sê San 4 Hydro & Solar', category: 'solar', mw: 399, lat: 13.97, lng: 107.51, region: 'central', desc: 'Hybrid floating & ground solar co-located with 360MW hydro' },
    { id: 'pleiku_500kv', name: 'Pleiku 500kV Supergrid Hub', category: 'substation', mw: 6000, lat: 13.98, lng: 108.00, region: 'central', desc: 'Historic 500kV Central Highlands transmission junction (Circuits 1, 2, 3)' },
    { id: 'chu_prong_wind', name: 'Chư Prông Wind Cluster', category: 'wind', mw: 300, lat: 13.75, lng: 107.95, region: 'central', desc: 'Gia Lai high-altitude plateau onshore wind turbine array' },
    { id: 'ea_nam', name: 'Ea Nam Wind Farm (Trung Nam)', category: 'wind', mw: 400, lat: 13.15, lng: 108.20, region: 'central', desc: 'Largest onshore wind farm in Vietnam (84x 4.8MW turbines)' },
    { id: 'ea_sup_solar', name: 'Xuân Thiện Ea Súp Solar Park', category: 'solar', mw: 600, lat: 13.10, lng: 107.85, region: 'central', desc: 'One of the largest utility solar PV installations in SE Asia' },
    { id: 'cu_mgar', name: "Cư M'gar Clean Energy Hub", category: 'wind', mw: 180, lat: 12.82, lng: 108.10, region: 'central', desc: 'Dak Lak highland wind and battery energy storage cluster' },
    { id: 'dak_nong_500kv', name: 'Đắk Nông 500kV Substation', category: 'substation', mw: 4000, lat: 12.00, lng: 107.69, region: 'central', desc: 'Bauxite industry power corridor & regional transmission node' },
    { id: 'cam_lam_solar', name: 'Cam Lâm Solar Park', category: 'solar', mw: 100, lat: 12.02, lng: 109.12, region: 'central', desc: 'Khanh Hoa utility solar installation near Cam Ranh bay' },
    { id: 'bac_ai_psp', name: 'Bác Ái Pumped Storage Hydro', category: 'hydro', mw: 1200, lat: 11.95, lng: 108.85, region: 'central', desc: 'Vietnam flagship 1,200 MW pumped storage clean grid battery' },
    { id: 'trung_nam_thuan_nam', name: 'Trung Nam Thuận Nam Solar', category: 'solar', mw: 450, lat: 11.60, lng: 108.90, region: 'central', desc: 'Integrated 450 MW solar plant with dedicated 500kV substation' },
    { id: 'bim_ninh_thuan', name: 'BIM 1-2-3 Solar Complex', category: 'solar', mw: 330, lat: 11.52, lng: 108.85, region: 'central', desc: 'Ninh Thuan salt-field photovoltaic array generating 500M kWh/yr' },
    { id: 'mui_dinh_wind', name: 'Mũi Dinh Ecopark Wind Farm', category: 'wind', mw: 100, lat: 11.48, lng: 109.02, region: 'central', desc: 'Coastal aerodynamic headland wind turbines on sand dunes' },
    { id: 'phuoc_thai_solar', name: 'Phước Thái Solar Hub', category: 'solar', mw: 200, lat: 11.55, lng: 108.92, region: 'central', desc: 'EVN invested solar farm with automated robotic dry-cleaning' },
    { id: 'dam_nai_wind', name: 'Đầm Nại Onshore Wind Farm', category: 'wind', mw: 80, lat: 11.66, lng: 108.98, region: 'central', desc: 'Scatec ASA utility wind farm operating in Ninh Thuan' },
    { id: 'di_linh_500kv', name: 'Di Linh 500kV Substation', category: 'substation', mw: 4000, lat: 11.50, lng: 108.05, region: 'central', desc: 'Southern highlands intertie connecting hydro and wind to HCMC' },
    { id: 'cau_dat_wind', name: 'Cầu Đất Đà Lạt Wind Farm', category: 'wind', mw: 55, lat: 11.85, lng: 108.55, region: 'central', desc: 'High-altitude mountain ridge wind farm in Lam Dong' },

    // --- SOUTHERN GRID (MIEN NAM) ---
    { id: 'vinh_tan_solar', name: 'Vĩnh Tân Solar & Wind Hub', category: 'solar', mw: 280, lat: 11.32, lng: 108.83, region: 'south', desc: 'Binh Thuan strategic energy port & marine transmission intertie' },
    { id: 'hong_phong_solar', name: 'Hồng Phong 1A/1B Solar', category: 'solar', mw: 250, lat: 11.08, lng: 108.38, region: 'south', desc: 'Red sand terrain utility solar array with high horizontal irradiance' },
    { id: 'tuy_phong_wind', name: 'Tuy Phong Pioneer Wind Farm', category: 'wind', mw: 60, lat: 11.23, lng: 108.68, region: 'south', desc: 'First commercial wind farm connected to national grid in Vietnam' },
    { id: 'phu_lac_wind', name: 'Phú Lạc Wind Power Plant', category: 'wind', mw: 50, lat: 11.19, lng: 108.62, region: 'south', desc: 'KfW funded high-efficiency onshore wind turbine cluster' },
    { id: 'dau_tieng_solar', name: 'Dầu Tiếng 1-2-3 Solar Complex', category: 'solar', mw: 500, lat: 11.35, lng: 106.22, region: 'south', desc: 'Largest semi-submerged solar PV installation on Dau Tieng lake' },
    { id: 'loc_ninh_solar', name: 'Lộc Ninh 1-5 Solar Array', category: 'solar', mw: 800, lat: 11.85, lng: 106.60, region: 'south', desc: 'Binh Phuoc massive border utility solar cluster with 220kV substation' },
    { id: 'tan_dinh_500kv', name: 'Tân Định 500kV Substation', category: 'substation', mw: 5000, lat: 11.12, lng: 106.65, region: 'south', desc: 'Binh Duong industrial corridor primary grid receiving terminal' },
    { id: 'tri_an_hydro', name: 'Trị An Hydroelectric Dam', category: 'hydro', mw: 400, lat: 11.11, lng: 107.01, region: 'south', desc: 'Dong Nai river hydro baseload & 200MW expansion facility' },
    { id: 'nhon_trach_lng', name: 'Nhơn Trạch 3 & 4 LNG Hub', category: 'lng', mw: 1624, lat: 10.65, lng: 106.90, region: 'south', desc: 'Vietnam first high-efficiency Class H LNG combined cycle plant' },
    { id: 'thi_vai_lng', name: 'Thị Vải LNG Terminal & Port', category: 'lng', mw: 3000, lat: 10.55, lng: 107.03, region: 'south', desc: '1 MTPA cryogenic LNG import terminal & Thi Vai regasification train' },
    { id: 'phu_my_complex', name: 'Phú Mỹ Power & Substation Center', category: 'substation', mw: 5000, lat: 10.58, lng: 107.05, region: 'south', desc: 'Largest thermal & 500kV transmission hub in Southern Vietnam' },
    { id: 'long_an_lng', name: 'Long An 1 & 2 LNG Mega-Project', category: 'lng', mw: 3000, lat: 10.45, lng: 106.72, region: 'south', desc: 'Southern industrial belt green LNG baseload power conversion' },
    { id: 'cau_bong_500kv', name: 'Cầu Bông 500kV Ring Substation', category: 'substation', mw: 4500, lat: 10.92, lng: 106.52, region: 'south', desc: 'Western HCMC 500kV ring transmission node & intertie' },
    { id: 'nha_be_500kv', name: 'Nhà Bè 500kV Substation', category: 'substation', mw: 4000, lat: 10.68, lng: 106.74, region: 'south', desc: 'Hiep Phuoc port & Southern HCMC heavy load grid anchor' },
    { id: 'ben_tre_wind', name: 'Ba Tri Offshore Wind Farm', category: 'wind', mw: 110, lat: 10.05, lng: 106.65, region: 'south', desc: 'Mekong Delta tidal coastal intertidal wind turbine array' },
    { id: 'tra_vinh_wind', name: 'Trà Vinh Duyên Hải Wind Cluster', category: 'wind', mw: 144, lat: 9.60, lng: 106.55, region: 'south', desc: 'Nearshore marine wind turbines operating in coastal mudflats' },
    { id: 'soc_trang_wind', name: 'Sóc Trăng Wind Project 7', category: 'wind', mw: 120, lat: 9.35, lng: 106.10, region: 'south', desc: 'Offshore intertidal renewable generation corridor' },
    { id: 'bac_lieu_wind', name: 'Bạc Liêu Iconic Marine Wind Farm', category: 'wind', mw: 291, lat: 9.25, lng: 105.75, region: 'south', desc: 'First nearshore marine wind farm in Vietnam (133x GE 2.05MW)' },
    { id: 'tan_thuan_wind', name: 'Tân Thuận Cà Mau Offshore Wind', category: 'wind', mw: 75, lat: 8.95, lng: 105.40, region: 'south', desc: 'Ca Mau peninsula coastal marine wind turbine park' },
    { id: 'ca_mau_gas', name: 'Cà Mau Gas-Power-Fertilizer Hub', category: 'lng', mw: 1500, lat: 8.85, lng: 105.05, region: 'south', desc: 'Southernmost offshore gas pipeline landfall & baseload plant' }
  ];

  // 15 Interconnected 500kV & 220kV Transmission Supergrid Corridors
  const SUPERGRID_CORRIDORS = [
    // 500kV Circuit-3 Supergrid Spine
    { id: 'c3_sec1', name: 'Circuit-3 (Quảng Trạch -> Quỳnh Lưu)', from: [17.80, 106.45], mid: [18.45, 106.10], to: [19.15, 105.65], color: 'c3', particles: 15 },
    { id: 'c3_sec2', name: 'Circuit-3 (Quỳnh Lưu -> Thanh Hóa)', from: [19.15, 105.65], mid: [19.45, 105.70], to: [19.80, 105.77], color: 'c3', particles: 14 },
    { id: 'c3_sec3', name: 'Circuit-3 (Thanh Hóa -> Nam Định 1)', from: [19.80, 105.77], mid: [20.05, 106.00], to: [20.25, 106.18], color: 'c3', particles: 14 },
    { id: 'c3_sec4', name: 'Circuit-3 (Nam Định 1 -> Phố Nối)', from: [20.25, 106.18], mid: [20.60, 106.12], to: [20.93, 106.05], color: 'c3', particles: 16 },

    // Central Backbone & Circuit 1-2 Interties
    { id: 'spine_vt_qt', name: '500kV Central Spine (Vũng Áng -> Quảng Trạch)', from: [18.02, 106.38], mid: [17.90, 106.40], to: [17.80, 106.45], color: 'c12', particles: 12 },
    { id: 'spine_qt_dn', name: '500kV Central Spine (Quảng Trạch -> Đà Nẵng)', from: [17.80, 106.45], mid: [16.85, 107.40], to: [16.05, 108.15], color: 'c12', particles: 15 },
    { id: 'spine_dn_pk', name: '500kV Highland Intertie (Đà Nẵng -> Pleiku)', from: [16.05, 108.15], mid: [15.00, 108.10], to: [13.98, 108.00], color: 'c12', particles: 16 },
    { id: 'spine_pk_dnong', name: '500kV Highland Spine (Pleiku -> Đắk Nông)', from: [13.98, 108.00], mid: [13.00, 107.85], to: [12.00, 107.69], color: 'c12', particles: 14 },
    { id: 'spine_dnong_dl', name: '500kV Highland Spine (Đắk Nông -> Di Linh)', from: [12.00, 107.69], mid: [11.75, 107.85], to: [11.50, 108.05], color: 'c12', particles: 13 },
    { id: 'spine_dl_td', name: '500kV Southern Corridor (Di Linh -> Tân Định)', from: [11.50, 108.05], mid: [11.30, 107.35], to: [11.12, 106.65], color: 'c12', particles: 15 },

    // Northern Ring Transmission Grid
    { id: 'ring_sl_hb', name: '500kV Hydro Intertie (Sơn La -> Hòa Bình)', from: [21.49, 103.99], mid: [21.15, 104.65], to: [20.81, 105.32], color: 'c12', particles: 14 },
    { id: 'ring_hb_pn', name: '500kV Northern Corridor (Hòa Bình -> Phố Nối)', from: [20.81, 105.32], mid: [20.85, 105.70], to: [20.93, 106.05], color: 'c12', particles: 14 },
    { id: 'ring_pn_qn', name: '500kV Coastal Loop (Phố Nối -> Quảng Ninh)', from: [20.93, 106.05], mid: [21.00, 106.60], to: [21.03, 107.12], color: 'c12', particles: 14 },

    // Southern Ring Transmission Grid
    { id: 'south_ring_td_pm', name: '500kV Industrial Ring (Tân Định -> Phú Mỹ)', from: [11.12, 106.65], mid: [10.85, 106.90], to: [10.58, 107.05], color: 'c12', particles: 15 },
    { id: 'south_ring_pm_cb', name: '500kV Metropolitan Loop (Phú Mỹ -> Cầu Bông)', from: [10.58, 107.05], mid: [10.75, 106.80], to: [10.92, 106.52], color: 'c12', particles: 15 }
  ];

  // 5 Detailed Engineering Asset Profiles (Mode B)
  const ASSET_PROFILES = {
    wind_turbine: {
      id: 'wind_turbine',
      name: '6.2 MW Offshore/Onshore Wind Turbine',
      category: 'Wind Generation',
      subtitle: 'Type IV Direct-Drive Permanent Magnet Synchronous Generator',
      specs: [
        { label: 'Rated Capacity', value: '6.2 MW' },
        { label: 'Rotor Diameter', value: '172 m' },
        { label: 'Hub Height', value: '115 m' },
        { label: 'Cut-in / Cut-out Wind', value: '3.0 / 25.0 m/s' },
        { label: 'Operating Voltage', value: '690 V / 35 kV' },
        { label: 'IEC Class', value: 'IEC S / Typhoon T' }
      ],
      description: 'Utility-scale turbine engineered for high humidity and tropical wind conditions across Vietnam coastal corridors (Bình Thuận, Trà Vinh, Bạc Liêu). Features carbon-hybrid aerofoil blades and dual-bearing direct-drive train.'
    },
    solar_tracker: {
      id: 'solar_tracker',
      name: 'Utility Single-Axis Solar PV Tracker',
      category: 'Solar Photovoltaic',
      subtitle: 'Two-in-Portrait (2P) High-Torque Astronomical Tracking Table',
      specs: [
        { label: 'Module Type', value: 'N-Type TOPCon Bifacial' },
        { label: 'Module Capacity', value: '620 Wp / panel' },
        { label: 'Tracking Range', value: '±55° with Backtracking' },
        { label: 'String Inverter', value: '330 kW, 1500 Vdc' },
        { label: 'Bifaciality Factor', value: '80% ± 5%' },
        { label: 'Wind Resistance', value: '160 km/h stowed' }
      ],
      description: 'Utility-scale solar array deployed across Ninh Thuận and Central Highlands. Real-time smart backtracking algorithms eliminate inter-row shading, boosting energy yield by up to 24% over fixed-tilt racking.'
    },
    pylon_500kv: {
      id: 'pylon_500kv',
      name: '500kV Circuit-3 Supergrid Lattice Tower',
      category: 'Transmission Infrastructure',
      subtitle: 'Double-Circuit Galvanized Structural Steel Suspension Pylon',
      specs: [
        { label: 'Nominal Voltage', value: '500 kV AC (3-Phase)' },
        { label: 'Total Height', value: '68.5 m' },
        { label: 'Base Footprint', value: '14.2 m × 14.2 m' },
        { label: 'Conductor Bundle', value: 'Quad 4×ACSR 330/43' },
        { label: 'Insulator Strings', value: 'Glass/Composite 28-disc' },
        { label: 'Design Span', value: '450 m average' }
      ],
      description: 'Standard heavy suspension pylon of the 519 km 500kV Circuit-3 Supergrid (Quảng Trạch to Phố Nối), capable of transmitting up to 3,000 MW of renewable power from Central Vietnam into the Northern industrial basin.'
    },
    transformer_500kv: {
      id: 'transformer_500kv',
      name: '500kV / 220kV Step-Up Power Transformer',
      category: 'Substation Engineering',
      subtitle: 'Three-Phase Oil-Immersed Auto-Transformer (ODAF Cooling)',
      specs: [
        { label: 'Rated Capacity', value: '900 MVA (3×300 MVA)' },
        { label: 'Voltage Ratio', value: '500 ± 8×1.25% / 225 / 35 kV' },
        { label: 'Cooling Method', value: 'ONAN / ONAF / ODAF' },
        { label: 'Total Weight', value: '345 Tonnes (with oil)' },
        { label: 'Efficiency', value: '99.78% at full load' },
        { label: 'Standard', value: 'IEC 60076 & EVN Spec' }
      ],
      description: 'Core intertie transformer operating at 500kV substations (Phố Nối, Nghi Sơn, Quảng Trạch). Equipped with on-load tap changers (OLTC), Buchholz relays, nitrogen fire extinguishing, and online DGA gas monitors.'
    },
    bess_container: {
      id: 'bess_container',
      name: '5 MWh Utility BESS Energy Storage Container',
      category: 'Energy Storage Systems',
      subtitle: '40ft High-Cube Modular LFP Battery Storage System',
      specs: [
        { label: 'Energy Capacity', value: '5.016 MWh' },
        { label: 'Power Rating', value: '2.5 MW (0.5C discharge)' },
        { label: 'Cell Chemistry', value: 'LFP (Lithium Iron Phosphate)' },
        { label: 'Thermal Management', value: 'Closed-Loop Liquid Chiller' },
        { label: 'Cycle Life', value: '≥ 8,000 cycles at 80% DoD' },
        { label: 'Safety Compliance', value: 'UL 9540A & NFPA 855' }
      ],
      description: 'Grid-scale BESS for peak shaving, rapid primary frequency response (FCR), and solar clipping mitigation. Integrated liquid cooling keeps cell temperature variation within ≤ 2.5°C across the container.'
    }
  };

  // Color Palettes for WebGL Canvas
  const THEME_PALETTES = {
    dark: {
      bg: 0x070a12,
      fog: 0x070a12,
      grid: 0x1e293b,
      land: 0x0f172a,
      landBorder: 0x334155,
      mountain: 0x1e293b,
      ambient: 0x718096,
      dirLight: 0xffffff,
      arcCircuit3: 0x06b6d4, // Cyan
      arcCircuit12: 0x3b82f6, // Blue
      evColor: 0x10b981,
      steel: 0x475569,
      steelLight: 0x94a3b8,
      pvBlue: 0x1e3a8a,
      copper: 0xb45309,
      accent: 0x0ea5e9
    },
    light: {
      bg: 0xf8fafc,
      fog: 0xf8fafc,
      grid: 0xe2e8f0,
      land: 0xffffff,
      landBorder: 0xcbd5e1,
      mountain: 0xf1f5f9,
      ambient: 0xa0aec0,
      dirLight: 0xffffff,
      arcCircuit3: 0x0891b2, // Cyan darker
      arcCircuit12: 0x2563eb, // Blue darker
      evColor: 0x059669,
      steel: 0x64748b,
      steelLight: 0xcbd5e1,
      pvBlue: 0x1e40af,
      copper: 0xd97706,
      accent: 0x0284c7
    }
  };

  const CATEGORY_COLORS = {
    solar: 0x10b981,     // Emerald
    wind: 0x06b6d4,      // Cyan
    hydro: 0x3b82f6,     // Blue
    lng: 0xf59e0b,       // Amber
    substation: 0xa855f7,// Purple
    hybrid: 0x6366f1      // Indigo
  };

  // Core Engine Variables
  let scene, camera, renderer, controls;
  let containerEl, canvasEl, tooltipEl, specCardEl;
  let isInitialized = false;
  let isVisible = false;
  let animFrameId = null;
  let isAnimationPlaying = true;
  let isWireframeActive = false;

  // View Mode: 'twin' | 'asset'
  let currentViewMode = 'twin';
  let currentAssetId = 'wind_turbine';
  let activeRegionFilter = 'all'; // 'all' | 'north' | 'central' | 'south'

  // Scene Object Groups
  let landGroup, hubsGroup, arcsGroup, evGroup, assetGroup;
  let gridHelper, assetGridHelper;
  let dirLight, ambientLight, assetKeyLight;
  let interactiveObjects = [];
  let raycaster, mouse;
  let arcParticles = [];

  // Dynamic Animated Sub-nodes
  let animatedRotorMesh = null;
  let animatedTrackerMesh = null;
  let miniTurbineRotors = [];

  // Active Map Filter States
  const activeLayers = {
    grid: true,
    renewables: true,
    ev: true
  };

  // Coordinate Conversion: (lat, lng) -> 3D Scene (X, Z)
  function geoTo3D(lat, lng) {
    const scale = 2.4;
    const x = (lng - 106.0) * scale;
    const z = -(lat - 16.0) * scale;
    return { x, z };
  }

  // Asynchronous Dynamic Dependency Loader
  async function loadThreeLibraries() {
    if (window.THREE && window.THREE.OrbitControls) return true;

    const loadScript = (src) => new Promise((resolve, reject) => {
      const s = document.createElement('script');
      s.src = src;
      s.onload = resolve;
      s.onerror = reject;
      document.head.appendChild(s);
    });

    if (!window.THREE) {
      await loadScript('https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js');
    }
    if (!window.THREE.OrbitControls) {
      await loadScript('https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js');
    }
    return true;
  }

  // Scene & Renderer Initialization
  function initScene() {
    const isDark = document.documentElement.classList.contains('dark');
    const p = isDark ? THEME_PALETTES.dark : THEME_PALETTES.light;

    scene = new THREE.Scene();
    scene.background = new THREE.Color(p.bg);
    scene.fog = new THREE.FogExp2(p.fog, 0.012);

    const aspect = containerEl.clientWidth / containerEl.clientHeight;
    camera = new THREE.PerspectiveCamera(45, aspect, 1, 500);
    camera.position.set(0, 32, 42);

    renderer = new THREE.WebGLRenderer({ canvas: canvasEl, antialias: true, alpha: true });
    renderer.setSize(containerEl.clientWidth, containerEl.clientHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2.0));
    renderer.shadowMap.enabled = true;
    renderer.shadowMap.type = THREE.PCFSoftShadowMap;

    // Controls
    controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.06;
    controls.maxPolarAngle = Math.PI / 2.1;
    controls.minDistance = 6;
    controls.maxDistance = 85;
    controls.target.set(0, 0, 0);

    // Global Lighting
    ambientLight = new THREE.AmbientLight(p.ambient, 1.35);
    scene.add(ambientLight);

    dirLight = new THREE.DirectionalLight(p.dirLight, 1.6);
    dirLight.position.set(20, 50, 30);
    dirLight.castShadow = true;
    dirLight.shadow.mapSize.width = 1024;
    dirLight.shadow.mapSize.height = 1024;
    scene.add(dirLight);

    assetKeyLight = new THREE.DirectionalLight(0xffffff, 0.8);
    assetKeyLight.position.set(-20, 20, -20);
    scene.add(assetKeyLight);

    // Grid Helpers
    gridHelper = new THREE.GridHelper(90, 45, p.grid, p.grid);
    gridHelper.position.y = -0.05;
    scene.add(gridHelper);

    assetGridHelper = new THREE.PolarGridHelper(16, 16, 8, 32, p.accent, p.grid);
    assetGridHelper.position.y = 0;
    assetGridHelper.visible = false;
    scene.add(assetGridHelper);

    // Raycaster
    raycaster = new THREE.Raycaster();
    mouse = new THREE.Vector2();

    // Scene Groups
    landGroup = new THREE.Group();
    hubsGroup = new THREE.Group();
    arcsGroup = new THREE.Group();
    evGroup = new THREE.Group();
    assetGroup = new THREE.Group();
    assetGroup.visible = false;

    scene.add(landGroup);
    scene.add(hubsGroup);
    scene.add(arcsGroup);
    scene.add(evGroup);
    scene.add(assetGroup);

    // Build 5x Density Geospatial Twin
    buildVietnamTerritory(p);
    buildHubPillarsWithMiniModels(p);
    buildSupergridTransmissionArcs(p);
    buildEvCorridorCloud(p);

    // Build Initial Selected Asset (Mode B)
    buildDetailedAssetModel(currentAssetId, p);

    // Event Listeners
    window.addEventListener('resize', onWindowResize);
    canvasEl.addEventListener('pointermove', onPointerMove);
    canvasEl.addEventListener('pointerdown', onPointerDown);

    const observer = new MutationObserver(updateThemeColors);
    observer.observe(document.documentElement, { attributes: true, attributeFilter: ['class', 'data-theme'] });

    isInitialized = true;
  }

  // 1. 92-VERTEX GEOGRAPHIC TERRITORY & MOUNTAIN SPINES (5X GEOMETRY)
  function buildVietnamTerritory(p) {
    landGroup.clear();

    // 92-Point Coastal and Border Perimeter Vertices [Lat, Lng]
    const perimeterCoords = [
      // Northern Border & Northeast Coast
      [23.38, 105.32], [23.10, 105.80], [22.80, 106.50], [22.25, 106.75], [21.80, 107.50],
      [21.53, 107.97], [21.20, 107.60], [20.95, 107.08], [20.86, 106.68], [20.55, 106.40],
      [20.25, 106.18], [20.00, 106.05], [19.80, 105.95], [19.50, 105.85], [19.15, 105.75],
      [18.80, 105.70], [18.40, 105.85], [18.02, 106.38], [17.80, 106.45], [17.50, 106.60],
      [17.10, 107.05], [16.80, 107.30], [16.58, 107.55], [16.30, 107.90], [16.15, 108.15],
      // Central Coast & South-Central Promontories
      [16.05, 108.25], [15.85, 108.40], [15.55, 108.65], [15.25, 108.85], [14.85, 109.00],
      [14.40, 109.05], [14.05, 109.20], [13.75, 109.25], [13.40, 109.30], [13.05, 109.35],
      [12.80, 109.30], [12.50, 109.25], [12.20, 109.20], [11.95, 109.15], [11.60, 108.95],
      [11.35, 108.85], [11.10, 108.60], [10.90, 108.25], [10.70, 107.80], [10.50, 107.30],
      [10.35, 107.05],
      // Mekong Delta Coast & Ca Mau Peninsula
      [10.20, 106.75], [10.05, 106.65], [9.80, 106.50], [9.55, 106.40], [9.35, 106.15],
      [9.15, 105.85], [8.95, 105.50], [8.75, 105.20], [8.60, 104.75], [8.75, 104.80],
      [9.00, 104.90], [9.30, 105.00], [9.60, 105.05], [9.90, 105.05], [10.20, 104.75],
      [10.40, 104.45],
      // Southwest Cambodian Border to Central Highlands
      [10.60, 104.60], [10.85, 105.10], [11.00, 105.50], [11.20, 106.00], [11.50, 106.35],
      [11.85, 106.60], [12.00, 107.20], [12.30, 107.50], [12.80, 107.60], [13.20, 107.50],
      [13.70, 107.45], [14.30, 107.40], [14.80, 107.50], [15.20, 107.40],
      // Truong Son Mountain Spine returning North (Laotian Border)
      [15.80, 107.20], [16.30, 106.80], [16.70, 106.40], [17.10, 106.00], [17.50, 105.80],
      [18.00, 105.60], [18.50, 105.30], [19.00, 104.80], [19.50, 104.30], [20.00, 104.00],
      [20.50, 103.80], [21.00, 103.40], [21.50, 103.00], [22.00, 102.50], [22.40, 102.30],
      [22.80, 103.00], [23.00, 104.00], [23.25, 104.80]
    ];

    const shape = new THREE.Shape();
    const first = geoTo3D(perimeterCoords[0][0], perimeterCoords[0][1]);
    shape.moveTo(first.x, first.z);

    for (let i = 1; i < perimeterCoords.length; i++) {
      const pt = geoTo3D(perimeterCoords[i][0], perimeterCoords[i][1]);
      shape.lineTo(pt.x, pt.z);
    }
    shape.closePath();

    const extrudeSettings = {
      steps: 2,
      depth: 0.45,
      bevelEnabled: true,
      bevelThickness: 0.15,
      bevelSize: 0.12,
      bevelSegments: 3
    };

    const geometry = new THREE.ExtrudeGeometry(shape, extrudeSettings);
    geometry.rotateX(Math.PI / 2);

    const material = new THREE.MeshStandardMaterial({
      color: p.land,
      roughness: 0.55,
      metalness: 0.15,
      wireframe: isWireframeActive
    });

    const landMesh = new THREE.Mesh(geometry, material);
    landMesh.receiveShadow = true;
    landGroup.add(landMesh);

    // 3D Truong Son Mountain Ridge Topographic Relief
    const ridgePoints = [
      [21.5, 104.0], [20.5, 105.0], [19.5, 105.2], [18.5, 105.4],
      [17.5, 106.0], [16.5, 107.0], [15.5, 107.8], [14.5, 108.0],
      [13.5, 108.2], [12.5, 108.0], [11.8, 107.8]
    ];
    ridgePoints.forEach(pt => {
      const pos = geoTo3D(pt[0], pt[1]);
      const mGeom = new THREE.ConeGeometry(0.85, 0.65, 5);
      mGeom.translate(0, 0.32, 0);
      const mMat = new THREE.MeshStandardMaterial({ color: p.mountain, roughness: 0.7 });
      const mMesh = new THREE.Mesh(mGeom, mMat);
      mMesh.position.set(pos.x, 0.45, pos.z);
      landGroup.add(mMesh);
    });

    // 8 Strategic Maritime Islands & Archipelagos
    const maritimeAssets = [
      { name: 'Quần đảo Hoàng Sa (Paracel Islands)', lat: 16.5, lng: 112.0, r: 0.75, color: 0x0ea5e9 },
      { name: 'Quần đảo Trường Sa (Spratly Islands)', lat: 10.0, lng: 114.5, r: 0.95, color: 0x0ea5e9 },
      { name: 'Đảo Phú Quốc Clean Island Hub', lat: 10.28, lng: 103.95, r: 0.65, color: 0x10b981 },
      { name: 'Côn Đảo Eco-Energy Reserve', lat: 8.68, lng: 106.60, r: 0.45, color: 0x0ea5e9 },
      { name: 'Đảo Bạch Long Vĩ Wind Radar', lat: 20.13, lng: 107.72, r: 0.35, color: 0x0ea5e9 },
      { name: 'Đảo Cồn Cỏ Maritime Node', lat: 17.16, lng: 107.33, r: 0.30, color: 0x0ea5e9 },
      { name: 'Đảo Lý Sơn Marine Hub', lat: 15.38, lng: 109.12, r: 0.40, color: 0x10b981 },
      { name: 'Đảo Phú Quý Offshore Wind', lat: 10.53, lng: 108.95, r: 0.42, color: 0x06b6d4 }
    ];

    maritimeAssets.forEach(isl => {
      const pos = geoTo3D(isl.lat, isl.lng);
      const geom = new THREE.CylinderGeometry(isl.r, isl.r * 1.1, 0.3, 12);
      const mat = new THREE.MeshStandardMaterial({ color: isl.color, roughness: 0.4 });
      const mesh = new THREE.Mesh(geom, mat);
      mesh.position.set(pos.x, 0.15, pos.z);
      mesh.userData = { name: isl.name, category: 'maritime', mw: 150, lat: isl.lat, lng: isl.lng, desc: 'Strategic maritime island & clean energy territory' };
      landGroup.add(mesh);
      interactiveObjects.push(mesh);
    });
  }

  // 2. 60+ REGIONAL GENERATION & SUBSTATION HUBS (5X DENSITY)
  function buildHubPillarsWithMiniModels(p) {
    hubsGroup.clear();
    miniTurbineRotors = [];
    interactiveObjects = [];

    ENERGY_HUBS.forEach((hub) => {
      // Apply region filter if active
      if (activeRegionFilter !== 'all' && hub.region !== activeRegionFilter) return;

      const pos = geoTo3D(hub.lat, hub.lng);
      const height = Math.max(1.2, (hub.mw / 5000) * 6.5);
      const colorHex = CATEGORY_COLORS[hub.category] || 0x10b981;

      const hubRoot = new THREE.Group();
      hubRoot.position.set(pos.x, 0.45, pos.z);

      // Base Pillar Geometry
      const baseGeom = new THREE.CylinderGeometry(0.28, 0.40, height, 6);
      baseGeom.translate(0, height / 2, 0);

      const baseMat = new THREE.MeshStandardMaterial({
        color: colorHex,
        roughness: 0.35,
        metalness: 0.45,
        emissive: colorHex,
        emissiveIntensity: 0.28,
        wireframe: isWireframeActive
      });

      const baseMesh = new THREE.Mesh(baseGeom, baseMat);
      baseMesh.castShadow = true;
      baseMesh.userData = hub;
      hubRoot.add(baseMesh);
      interactiveObjects.push(baseMesh);

      // Emissive Halo Cap
      const haloGeom = new THREE.RingGeometry(0.35, 0.65, 16);
      haloGeom.rotateX(-Math.PI / 2);
      const haloMat = new THREE.MeshBasicMaterial({
        color: colorHex,
        side: THREE.DoubleSide,
        transparent: true,
        opacity: 0.75
      });
      const halo = new THREE.Mesh(haloGeom, haloMat);
      halo.position.set(0, height + 0.04, 0);
      hubRoot.add(halo);

      // Dedicated Miniature 3D Models
      if (hub.category === 'wind') {
        const miniTurbine = createMiniTurbine(p);
        miniTurbine.position.set(0, height + 0.05, 0);
        hubRoot.add(miniTurbine);
      } else if (hub.category === 'solar') {
        const miniSolar = createMiniSolar(p);
        miniSolar.position.set(0, height + 0.05, 0);
        hubRoot.add(miniSolar);
      } else if (hub.category === 'hydro') {
        const miniDam = createMiniDam(p);
        miniDam.position.set(0, height + 0.05, 0);
        hubRoot.add(miniDam);
      } else if (hub.category === 'substation') {
        const miniPylon = createMiniPylon(p);
        miniPylon.position.set(0, height + 0.05, 0);
        hubRoot.add(miniPylon);
      } else if (hub.category === 'lng') {
        const miniLng = createMiniLng(p);
        miniLng.position.set(0, height + 0.05, 0);
        hubRoot.add(miniLng);
      }

      hubsGroup.add(hubRoot);
    });
  }

  // Miniature Procedural Builders
  function createMiniTurbine(p) {
    const group = new THREE.Group();
    const towerGeom = new THREE.CylinderGeometry(0.05, 0.10, 1.3, 8);
    towerGeom.translate(0, 0.65, 0);
    const towerMat = new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 0.4 });
    group.add(new THREE.Mesh(towerGeom, towerMat));

    const nacelleGeom = new THREE.BoxGeometry(0.16, 0.12, 0.32);
    nacelleGeom.translate(0, 1.35, 0);
    group.add(new THREE.Mesh(nacelleGeom, towerMat));

    const rotorGroup = new THREE.Group();
    rotorGroup.position.set(0, 1.35, 0.18);

    const hubCone = new THREE.ConeGeometry(0.07, 0.12, 8);
    hubCone.rotateX(Math.PI / 2);
    rotorGroup.add(new THREE.Mesh(hubCone, towerMat));

    for (let i = 0; i < 3; i++) {
      const bladeGeom = new THREE.BoxGeometry(0.05, 0.70, 0.02);
      bladeGeom.translate(0, 0.35, 0);
      const bladeMesh = new THREE.Mesh(bladeGeom, towerMat);
      bladeMesh.rotation.z = (i * Math.PI * 2) / 3;
      rotorGroup.add(bladeMesh);
    }

    group.add(rotorGroup);
    miniTurbineRotors.push(rotorGroup);
    return group;
  }

  function createMiniSolar(p) {
    const group = new THREE.Group();
    const panelGeom = new THREE.BoxGeometry(0.95, 0.03, 0.65);
    panelGeom.rotateX(-Math.PI / 6);
    const panelMat = new THREE.MeshStandardMaterial({ color: 0x1e3a8a, roughness: 0.3, metalness: 0.5 });
    const panel = new THREE.Mesh(panelGeom, panelMat);
    panel.position.set(0, 0.32, 0);
    group.add(panel);

    const postGeom = new THREE.CylinderGeometry(0.03, 0.03, 0.32, 6);
    postGeom.translate(0, 0.16, 0);
    group.add(new THREE.Mesh(postGeom, new THREE.MeshStandardMaterial({ color: 0x94a3b8 })));
    return group;
  }

  function createMiniDam(p) {
    const group = new THREE.Group();
    const damGeom = new THREE.BoxGeometry(0.75, 0.40, 0.35);
    const dam = new THREE.Mesh(damGeom, new THREE.MeshStandardMaterial({ color: 0x64748b, roughness: 0.8 }));
    dam.position.set(0, 0.20, 0);
    group.add(dam);

    const waterGeom = new THREE.BoxGeometry(0.22, 0.12, 0.55);
    const water = new THREE.Mesh(waterGeom, new THREE.MeshStandardMaterial({ color: 0x38bdf8, transparent: true, opacity: 0.85 }));
    water.position.set(0, 0.20, 0.08);
    group.add(water);
    return group;
  }

  function createMiniPylon(p) {
    const group = new THREE.Group();
    const towerGeom = new THREE.ConeGeometry(0.18, 1.1, 4);
    towerGeom.translate(0, 0.55, 0);
    group.add(new THREE.Mesh(towerGeom, new THREE.MeshStandardMaterial({ color: 0xa855f7, metalness: 0.7, wireframe: true })));

    const armGeom = new THREE.BoxGeometry(0.65, 0.04, 0.04);
    armGeom.translate(0, 0.85, 0);
    group.add(new THREE.Mesh(armGeom, new THREE.MeshStandardMaterial({ color: 0xa855f7 })));
    return group;
  }

  function createMiniLng(p) {
    const group = new THREE.Group();
    const tankGeom = new THREE.CylinderGeometry(0.35, 0.35, 0.45, 16);
    tankGeom.translate(0, 0.22, 0);
    group.add(new THREE.Mesh(tankGeom, new THREE.MeshStandardMaterial({ color: 0xf59e0b, roughness: 0.4 })));
    return group;
  }

  // 3. 15-CORRIDOR 500kV SUPERGRID NETWORK & 210 PHOTON PARTICLES (5X DENSITY)
  function buildSupergridTransmissionArcs(p) {
    arcsGroup.clear();
    arcParticles = [];

    SUPERGRID_CORRIDORS.forEach((corr) => {
      const p1 = geoTo3D(corr.from[0], corr.from[1]);
      const pm = geoTo3D(corr.mid[0], corr.mid[1]);
      const p2 = geoTo3D(corr.to[0], corr.to[1]);

      const v1 = new THREE.Vector3(p1.x, 1.8, p1.z);
      const vm = new THREE.Vector3(pm.x, 5.8, pm.z);
      const v2 = new THREE.Vector3(p2.x, 1.8, p2.z);

      const curve = new THREE.QuadraticBezierCurve3(v1, vm, v2);
      const points = curve.getPoints(40);
      const geometry = new THREE.BufferGeometry().setFromPoints(points);

      const colorHex = corr.color === 'c3' ? p.arcCircuit3 : p.arcCircuit12;
      const material = new THREE.LineBasicMaterial({
        color: colorHex,
        linewidth: 2,
        transparent: true,
        opacity: 0.85
      });

      const line = new THREE.Line(geometry, material);
      arcsGroup.add(line);

      // Flowing Energy Photons
      const particleGeom = new THREE.SphereGeometry(0.14, 8, 8);
      const particleMat = new THREE.MeshBasicMaterial({ color: 0xffffff });

      for (let i = 0; i < corr.particles; i++) {
        const mesh = new THREE.Mesh(particleGeom, particleMat);
        arcsGroup.add(mesh);
        arcParticles.push({
          mesh: mesh,
          curve: curve,
          progress: i / corr.particles,
          speed: 0.0035 + (i % 3) * 0.0008
        });
      }
    });
  }

  // 4. 2,250 GEOREFERENCED EV CHARGING NODES (5X DENSITY)
  function buildEvCorridorCloud(p) {
    evGroup.clear();

    const totalCount = 2250;
    const positions = new Float32Array(totalCount * 3);

    for (let i = 0; i < totalCount; i++) {
      let lat, lng;

      // Realistic clustering based on national traffic distribution
      if (i < 1200) {
        // Highway 1A & North-South Expressway Spine
        const t = i / 1200;
        lat = 8.65 + t * (21.5 - 8.65);
        // S-curve highway routing
        const sOffset = Math.sin(t * Math.PI) * 3.4;
        lng = 105.10 + sOffset + (Math.random() - 0.5) * 0.38;
      } else if (i < 1600) {
        // Hanoi Capital Metropolitan Cluster (Ring Roads 3, 3.5, 4)
        const angle = Math.random() * Math.PI * 2;
        const radius = Math.random() * 0.45;
        lat = 21.02 + Math.sin(angle) * radius;
        lng = 105.85 + Math.cos(angle) * radius;
      } else if (i < 2000) {
        // Ho Chi Minh City Metropolitan Cluster (Beltways 2, 3 & Binh Duong/Dong Nai)
        const angle = Math.random() * Math.PI * 2;
        const radius = Math.random() * 0.52;
        lat = 10.82 + Math.sin(angle) * radius;
        lng = 106.68 + Math.cos(angle) * radius;
      } else {
        // Da Nang & Central Coast Cluster
        const t = (i - 2000) / 250;
        lat = 15.20 + t * (16.80 - 15.20);
        lng = 108.15 + (Math.random() - 0.5) * 0.25;
      }

      const pt = geoTo3D(lat, lng);
      positions[i * 3 + 0] = pt.x;
      positions[i * 3 + 1] = 0.48 + (i % 5) * 0.04;
      positions[i * 3 + 2] = pt.z;
    }

    const geometry = new THREE.BufferGeometry();
    geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));

    const material = new THREE.PointsMaterial({
      color: p.evColor,
      size: 0.32,
      transparent: true,
      opacity: 0.80
    });

    const pointCloud = new THREE.Points(geometry, material);
    evGroup.add(pointCloud);
  }

  // =========================================================================
  // 5. HIGH-RESOLUTION PROCEDURAL 3D ENGINEERING ASSET BUILDERS (MODE B)
  // =========================================================================

  function buildDetailedAssetModel(assetId, p) {
    assetGroup.clear();
    animatedRotorMesh = null;
    animatedTrackerMesh = null;

    if (currentViewMode === 'asset') {
      interactiveObjects = [];
    }

    switch(assetId) {
      case 'wind_turbine':
        buildWindTurbineAsset(p);
        break;
      case 'solar_tracker':
        buildSolarTrackerAsset(p);
        break;
      case 'pylon_500kv':
        buildPylonAsset(p);
        break;
      case 'transformer_500kv':
        buildTransformerAsset(p);
        break;
      case 'bess_container':
        buildBessContainerAsset(p);
        break;
      default:
        buildWindTurbineAsset(p);
    }
  }

  // Asset 1: 6.2 MW Utility Wind Turbine Model
  function buildWindTurbineAsset(p) {
    const root = new THREE.Group();

    const steelMat = new THREE.MeshStandardMaterial({ color: 0xe2e8f0, roughness: 0.35, metalness: 0.3, wireframe: isWireframeActive });
    const darkMat = new THREE.MeshStandardMaterial({ color: 0x334155, roughness: 0.5, metalness: 0.7, wireframe: isWireframeActive });
    const redMat = new THREE.MeshStandardMaterial({ color: 0xef4444, roughness: 0.4, wireframe: isWireframeActive });

    const foundGeom = new THREE.CylinderGeometry(4.2, 4.6, 0.8, 24);
    foundGeom.translate(0, 0.4, 0);
    const foundMesh = new THREE.Mesh(foundGeom, darkMat);
    foundMesh.receiveShadow = true;
    root.add(foundMesh);

    const towerGeom = new THREE.CylinderGeometry(0.75, 1.35, 18.0, 32);
    towerGeom.translate(0, 9.8, 0);
    const towerMesh = new THREE.Mesh(towerGeom, steelMat);
    towerMesh.castShadow = true;
    towerMesh.userData = { title: 'Tubular Steel Tower', desc: '115m multi-section conical steel tower with internal service hoist and cable tray.' };
    root.add(towerMesh);
    if (currentViewMode === 'asset') interactiveObjects.push(towerMesh);

    const nacelleRoot = new THREE.Group();
    nacelleRoot.position.set(0, 18.8, 0);

    const nacelleGeom = new THREE.BoxGeometry(2.4, 2.2, 5.2);
    nacelleGeom.translate(0, 0.2, -0.6);
    const nacelleMesh = new THREE.Mesh(nacelleGeom, steelMat);
    nacelleMesh.castShadow = true;
    nacelleMesh.userData = { title: 'Nacelle & Direct-Drive Generator', desc: 'Houses 6.2 MW permanent magnet synchronous generator (PMSG), converter, and transformer.' };
    nacelleRoot.add(nacelleMesh);
    if (currentViewMode === 'asset') interactiveObjects.push(nacelleMesh);

    const coolerGeom = new THREE.BoxGeometry(1.6, 0.8, 1.2);
    coolerGeom.translate(0, 1.4, -2.2);
    nacelleRoot.add(new THREE.Mesh(coolerGeom, darkMat));

    const beaconGeom = new THREE.CylinderGeometry(0.12, 0.12, 0.25, 12);
    beaconGeom.translate(0, 1.8, -1.0);
    nacelleRoot.add(new THREE.Mesh(beaconGeom, new THREE.MeshBasicMaterial({ color: 0xff0000 })));

    const rotorHub = new THREE.Group();
    rotorHub.position.set(0, 0.2, 2.1);

    const spinnerGeom = new THREE.ConeGeometry(0.95, 1.8, 24);
    spinnerGeom.rotateX(Math.PI / 2);
    rotorHub.add(new THREE.Mesh(spinnerGeom, steelMat));

    for (let i = 0; i < 3; i++) {
      const bladeGroup = new THREE.Group();
      bladeGroup.rotation.z = (i * Math.PI * 2) / 3;

      const bladeRootGeom = new THREE.CylinderGeometry(0.32, 0.38, 1.2, 16);
      bladeRootGeom.translate(0, 0.6, 0);
      bladeGroup.add(new THREE.Mesh(bladeRootGeom, darkMat));

      const bladeGeom = new THREE.ConeGeometry(0.38, 12.5, 16);
      bladeGeom.translate(0, 7.2, 0);
      const bladeMesh = new THREE.Mesh(bladeGeom, steelMat);
      bladeMesh.castShadow = true;
      bladeMesh.userData = { title: 'Aerofoil Rotor Blade (84m)', desc: 'Carbon-hybrid structural spar with aerodynamic twist and lightning receptor strips.' };
      bladeGroup.add(bladeMesh);
      if (currentViewMode === 'asset') interactiveObjects.push(bladeMesh);

      const tipGeom = new THREE.ConeGeometry(0.12, 2.2, 16);
      tipGeom.translate(0, 12.3, 0);
      bladeGroup.add(new THREE.Mesh(tipGeom, redMat));

      rotorHub.add(bladeGroup);
    }

    nacelleRoot.add(rotorHub);
    root.add(nacelleRoot);

    animatedRotorMesh = rotorHub;
    assetGroup.add(root);
  }

  // Asset 2: Utility Single-Axis Solar PV Tracker Array
  function buildSolarTrackerAsset(p) {
    const root = new THREE.Group();
    const metalMat = new THREE.MeshStandardMaterial({ color: 0x94a3b8, roughness: 0.4, metalness: 0.8, wireframe: isWireframeActive });
    const pvMat = new THREE.MeshStandardMaterial({ color: 0x1e3a8a, roughness: 0.25, metalness: 0.6, wireframe: isWireframeActive });
    const frameMat = new THREE.MeshStandardMaterial({ color: 0xcbd5e1, roughness: 0.3, metalness: 0.8, wireframe: isWireframeActive });

    for (let x = -7.5; x <= 7.5; x += 5.0) {
      const pierGeom = new THREE.BoxGeometry(0.7, 0.8, 0.7);
      pierGeom.translate(x, 0.4, 0);
      root.add(new THREE.Mesh(pierGeom, metalMat));

      const postGeom = new THREE.BoxGeometry(0.25, 3.2, 0.35);
      postGeom.translate(x, 2.0, 0);
      root.add(new THREE.Mesh(postGeom, metalMat));
    }

    const trackerAssembly = new THREE.Group();
    trackerAssembly.position.set(0, 3.6, 0);

    const tubeGeom = new THREE.CylinderGeometry(0.2, 0.2, 19.0, 16);
    tubeGeom.rotateZ(Math.PI / 2);
    trackerAssembly.add(new THREE.Mesh(tubeGeom, metalMat));

    const motorGeom = new THREE.CylinderGeometry(0.55, 0.55, 0.8, 16);
    const motorMesh = new THREE.Mesh(motorGeom, new THREE.MeshStandardMaterial({ color: 0x334155, metalness: 0.9 }));
    motorMesh.position.set(0, 0, 0);
    motorMesh.userData = { title: 'Slewing Drive & Smart Controller', desc: 'High-torque self-locking slew gear driven by astronomical tracking algorithm with wind stow.' };
    trackerAssembly.add(motorMesh);
    if (currentViewMode === 'asset') interactiveObjects.push(motorMesh);

    for (let x = -8.5; x <= 8.5; x += 1.55) {
      if (Math.abs(x) < 0.8) continue;

      const tableGroup = new THREE.Group();
      tableGroup.position.set(x, 0, 0);

      const upperPanel = new THREE.Mesh(new THREE.BoxGeometry(1.45, 0.04, 2.2), pvMat);
      upperPanel.position.set(0, 0.08, 1.2);
      upperPanel.castShadow = true;
      upperPanel.userData = { title: 'Bifacial TOPCon PV Module (620Wp)', desc: 'N-Type monocrystalline cells with 80% bifaciality factor collecting albedo irradiance.' };
      tableGroup.add(upperPanel);
      if (currentViewMode === 'asset') interactiveObjects.push(upperPanel);

      const lowerPanel = new THREE.Mesh(new THREE.BoxGeometry(1.45, 0.04, 2.2), pvMat);
      lowerPanel.position.set(0, 0.08, -1.2);
      lowerPanel.castShadow = true;
      lowerPanel.userData = { title: 'Bifacial TOPCon PV Module (620Wp)', desc: 'Silver busbars with anti-reflective tempered glass and anodized aluminum frame.' };
      tableGroup.add(lowerPanel);
      if (currentViewMode === 'asset') interactiveObjects.push(lowerPanel);

      const rafter = new THREE.Mesh(new THREE.BoxGeometry(0.08, 0.12, 4.8), frameMat);
      rafter.position.set(0, -0.06, 0);
      tableGroup.add(rafter);

      trackerAssembly.add(tableGroup);
    }

    const invGeom = new THREE.BoxGeometry(1.2, 1.4, 0.6);
    invGeom.translate(2.5, 2.2, 0.8);
    const invMesh = new THREE.Mesh(invGeom, new THREE.MeshStandardMaterial({ color: 0x475569, metalness: 0.6 }));
    invMesh.userData = { title: '330 kW String Inverter (1500 Vdc)', desc: 'Multi-MPPT power conversion with integrated DC arc fault protection (AFCI) and rapid shutdown.' };
    root.add(invMesh);
    if (currentViewMode === 'asset') interactiveObjects.push(invMesh);

    root.add(trackerAssembly);
    animatedTrackerMesh = trackerAssembly;
    assetGroup.add(root);
  }

  // Asset 3: 500kV Supergrid Lattice Transmission Tower
  function buildPylonAsset(p) {
    const root = new THREE.Group();
    const steelMat = new THREE.MeshStandardMaterial({ color: 0x94a3b8, roughness: 0.35, metalness: 0.85, wireframe: isWireframeActive });
    const insulMat = new THREE.MeshStandardMaterial({ color: 0x0284c7, roughness: 0.1, transparent: true, opacity: 0.85 });

    const corners = [
      [-3.0, -3.0], [3.0, -3.0], [3.0, 3.0], [-3.0, 3.0]
    ];
    corners.forEach(c => {
      const pier = new THREE.Mesh(new THREE.CylinderGeometry(0.7, 0.85, 1.0, 8), new THREE.MeshStandardMaterial({ color: 0x64748b, roughness: 0.8 }));
      pier.position.set(c[0], 0.5, c[1]);
      root.add(pier);
    });

    const lowerBodyGeom = new THREE.CylinderGeometry(1.2, 3.8, 12.0, 4, 6, true);
    lowerBodyGeom.translate(0, 7.0, 0);
    lowerBodyGeom.rotateY(Math.PI / 4);
    root.add(new THREE.Mesh(lowerBodyGeom, new THREE.MeshStandardMaterial({ color: 0x94a3b8, wireframe: true })));

    const upperBodyGeom = new THREE.BoxGeometry(1.6, 8.0, 1.6);
    upperBodyGeom.translate(0, 17.0, 0);
    const upperBody = new THREE.Mesh(upperBodyGeom, new THREE.MeshStandardMaterial({ color: 0x64748b, wireframe: true }));
    upperBody.userData = { title: 'Galvanized Steel Truss Mast', desc: 'Engineered for 500kV wind load class III with double-laced diagonal members.' };
    root.add(upperBody);
    if (currentViewMode === 'asset') interactiveObjects.push(upperBody);

    const arm1Geom = new THREE.BoxGeometry(13.5, 0.7, 1.4);
    arm1Geom.translate(0, 16.5, 0);
    root.add(new THREE.Mesh(arm1Geom, steelMat));

    const arm2Geom = new THREE.BoxGeometry(10.5, 0.6, 1.4);
    arm2Geom.translate(0, 19.5, 0);
    root.add(new THREE.Mesh(arm2Geom, steelMat));

    const peakGeom = new THREE.ConeGeometry(0.8, 2.5, 4);
    peakGeom.translate(0, 22.25, 0);
    peakGeom.rotateY(Math.PI / 4);
    root.add(new THREE.Mesh(peakGeom, steelMat));

    const insulatorPositions = [
      [-6.0, 16.2, 0], [6.0, 16.2, 0], [-3.8, 16.2, 0], [3.8, 16.2, 0],
      [-4.6, 19.2, 0], [4.6, 19.2, 0]
    ];

    insulatorPositions.forEach(pos => {
      const insulGroup = new THREE.Group();
      insulGroup.position.set(pos[0], pos[1], pos[2]);

      const stringGeom = new THREE.CylinderGeometry(0.18, 0.18, 2.4, 12, 16);
      stringGeom.translate(0, -1.2, 0);
      const stringMesh = new THREE.Mesh(stringGeom, insulMat);
      stringMesh.userData = { title: '500kV Composite Insulator (28 Discs)', desc: 'Creepage distance > 16,000 mm with anti-fog silicon shed profile and corona discharge rings.' };
      insulGroup.add(stringMesh);
      if (currentViewMode === 'asset') interactiveObjects.push(stringMesh);

      const clampGeom = new THREE.BoxGeometry(0.8, 0.15, 0.8);
      clampGeom.translate(0, -2.45, 0);
      insulGroup.add(new THREE.Mesh(clampGeom, steelMat));

      root.add(insulGroup);
    });

    assetGroup.add(root);
  }

  // Asset 4: 500kV / 220kV Step-Up Substation Power Transformer
  function buildTransformerAsset(p) {
    const root = new THREE.Group();

    const tankMat = new THREE.MeshStandardMaterial({ color: 0x475569, roughness: 0.4, metalness: 0.7, wireframe: isWireframeActive });
    const darkMat = new THREE.MeshStandardMaterial({ color: 0x1e293b, roughness: 0.5, metalness: 0.8, wireframe: isWireframeActive });
    const copperMat = new THREE.MeshStandardMaterial({ color: 0xd97706, roughness: 0.3, metalness: 0.8, wireframe: isWireframeActive });
    const bushingMat = new THREE.MeshStandardMaterial({ color: 0x991b1b, roughness: 0.2, metalness: 0.3, wireframe: isWireframeActive });

    const foundation = new THREE.Mesh(new THREE.BoxGeometry(11.0, 0.6, 9.0), new THREE.MeshStandardMaterial({ color: 0x64748b, roughness: 0.8 }));
    foundation.position.set(0, 0.3, 0);
    root.add(foundation);

    const tankGeom = new THREE.BoxGeometry(5.2, 4.4, 4.2);
    tankGeom.translate(0, 2.8, 0);
    const tankMesh = new THREE.Mesh(tankGeom, tankMat);
    tankMesh.castShadow = true;
    tankMesh.userData = { title: 'Transformer Core Oil Tank (900 MVA)', desc: 'High-permeability silicon steel core immersed in inhibited mineral dielectric oil.' };
    root.add(tankMesh);
    if (currentViewMode === 'asset') interactiveObjects.push(tankMesh);

    for (let side of [-1, 1]) {
      const radGroup = new THREE.Group();
      radGroup.position.set(side * 3.6, 2.6, 0);

      for (let z = -1.6; z <= 1.6; z += 0.45) {
        const fin = new THREE.Mesh(new THREE.BoxGeometry(0.12, 3.2, 0.35), darkMat);
        fin.position.set(0, 0, z);
        radGroup.add(fin);
      }

      for (let z = -1.0; z <= 1.0; z += 1.0) {
        const fanGeom = new THREE.CylinderGeometry(0.45, 0.45, 0.25, 16);
        fanGeom.rotateZ(Math.PI / 2);
        fanGeom.translate(side * 0.3, -1.0, z);
        radGroup.add(new THREE.Mesh(fanGeom, darkMat));
      }

      radGroup.userData = { title: 'ODAF Cooling Radiator Bank', desc: 'Forced oil and forced air circulation maintaining winding hotspot temperature < 98°C.' };
      root.add(radGroup);
      if (currentViewMode === 'asset') interactiveObjects.push(radGroup);
    }

    const consGeom = new THREE.CylinderGeometry(0.7, 0.7, 4.6, 24);
    consGeom.rotateZ(Math.PI / 2);
    consGeom.translate(0, 5.8, -1.5);
    const consMesh = new THREE.Mesh(consGeom, tankMat);
    consMesh.userData = { title: 'Oil Conservator & Buchholz Relay', desc: 'Accommodates thermal oil expansion with rubber diaphragm bag and silica gel moisture breather.' };
    root.add(consMesh);
    if (currentViewMode === 'asset') interactiveObjects.push(consMesh);

    for (let i = -1; i <= 1; i++) {
      const bushGroup = new THREE.Group();
      bushGroup.position.set(i * 1.5, 5.0, 0.8);
      bushGroup.rotation.x = -Math.PI / 10;

      const bGeom = new THREE.CylinderGeometry(0.24, 0.38, 3.2, 16, 20);
      bGeom.translate(0, 1.6, 0);
      const bMesh = new THREE.Mesh(bGeom, bushingMat);
      bMesh.userData = { title: '500kV RIP Condenser Bushing', desc: 'Resin-impregnated paper high-voltage bushing with capacitive grading and test tap.' };
      bushGroup.add(bMesh);
      if (currentViewMode === 'asset') interactiveObjects.push(bMesh);

      const ball = new THREE.Mesh(new THREE.SphereGeometry(0.35, 16, 16), copperMat);
      ball.position.set(0, 3.2, 0);
      bushGroup.add(ball);

      root.add(bushGroup);
    }

    const kiosk = new THREE.Mesh(new THREE.BoxGeometry(0.8, 1.6, 0.6), darkMat);
    kiosk.position.set(1.8, 1.4, 2.3);
    kiosk.userData = { title: 'Marshalling Local Control Kiosk', desc: 'Fiber-optic monitoring interface for temperature sensors, OLTC controls, and dissolved gas analyzer.' };
    root.add(kiosk);
    if (currentViewMode === 'asset') interactiveObjects.push(kiosk);

    assetGroup.add(root);
  }

  // Asset 5: 5 MWh Utility BESS Container
  function buildBessContainerAsset(p) {
    const root = new THREE.Group();

    const containerMat = new THREE.MeshStandardMaterial({ color: 0x0f766e, roughness: 0.35, metalness: 0.3, wireframe: isWireframeActive });
    const whiteMat = new THREE.MeshStandardMaterial({ color: 0xf8fafc, roughness: 0.3, metalness: 0.2, wireframe: isWireframeActive });
    const darkMat = new THREE.MeshStandardMaterial({ color: 0x1e293b, roughness: 0.6, metalness: 0.8, wireframe: isWireframeActive });
    const yellowMat = new THREE.MeshStandardMaterial({ color: 0xeab308, roughness: 0.4 });

    const plinth = new THREE.Mesh(new THREE.BoxGeometry(13.2, 0.5, 4.2), new THREE.MeshStandardMaterial({ color: 0x64748b, roughness: 0.8 }));
    plinth.position.set(0, 0.25, 0);
    root.add(plinth);

    const boxGeom = new THREE.BoxGeometry(12.2, 2.9, 2.5);
    boxGeom.translate(0, 1.95, 0);
    const boxMesh = new THREE.Mesh(boxGeom, containerMat);
    boxMesh.castShadow = true;
    boxMesh.userData = { title: '40ft ISO High-Cube BESS Enclosure', desc: 'C5-M marine anti-corrosion rated steel container housing LFP battery modules and BMS racks.' };
    root.add(boxMesh);
    if (currentViewMode === 'asset') interactiveObjects.push(boxMesh);

    for (let x = -5.8; x <= 5.8; x += 0.35) {
      const rib = new THREE.Mesh(new THREE.BoxGeometry(0.12, 2.7, 0.08), darkMat);
      rib.position.set(x, 1.95, 1.28);
      root.add(rib);

      const ribBack = new THREE.Mesh(new THREE.BoxGeometry(0.12, 2.7, 0.08), darkMat);
      ribBack.position.set(x, 1.95, -1.28);
      root.add(ribBack);
    }

    for (let side of [-2.8, 2.8]) {
      const hvacGeom = new THREE.BoxGeometry(2.4, 0.8, 1.8);
      hvacGeom.translate(side, 3.8, 0);
      const hvacMesh = new THREE.Mesh(hvacGeom, whiteMat);
      hvacMesh.userData = { title: 'Closed-Loop Liquid Thermal Chiller', desc: 'Maintains cell operating temperature at 23°C ± 2°C, extending LFP cycle life to > 8,000 cycles.' };
      root.add(hvacMesh);
      if (currentViewMode === 'asset') interactiveObjects.push(hvacMesh);

      const fan1 = new THREE.Mesh(new THREE.CylinderGeometry(0.4, 0.4, 0.15, 16), darkMat);
      fan1.position.set(side - 0.55, 4.25, 0);
      root.add(fan1);

      const fan2 = new THREE.Mesh(new THREE.CylinderGeometry(0.4, 0.4, 0.15, 16), darkMat);
      fan2.position.set(side + 0.55, 4.25, 0);
      root.add(fan2);
    }

    for (let x of [-4.5, 0, 4.5]) {
      const vent = new THREE.Mesh(new THREE.BoxGeometry(0.9, 0.15, 0.9), yellowMat);
      vent.position.set(x, 3.48, 0);
      vent.userData = { title: 'NFPA 68 Explosion Relief Vent', desc: 'Overpressure safety relief panels and Novec 1230 / aerosol gas fire extinguishing manifold.' };
      root.add(vent);
      if (currentViewMode === 'asset') interactiveObjects.push(vent);
    }

    const doorFrame = new THREE.Mesh(new THREE.BoxGeometry(0.2, 2.4, 2.0), darkMat);
    doorFrame.position.set(6.12, 1.7, 0);
    root.add(doorFrame);

    assetGroup.add(root);
  }

  // =========================================================================
  // ANIMATION LOOP & INTERACTION
  // =========================================================================

  function animate() {
    if (!isVisible) return;
    animFrameId = requestAnimationFrame(animate);

    if (controls) controls.update();

    if (isAnimationPlaying) {
      if (currentViewMode === 'twin') {
        // Animate 210 photon particles along 15 corridors
        arcParticles.forEach((p) => {
          p.progress += p.speed;
          if (p.progress > 1.0) p.progress = 0.0;
          const pos = p.curve.getPoint(p.progress);
          p.mesh.position.copy(pos);
        });

        // Rotate miniature wind turbine rotors
        miniTurbineRotors.forEach((rotor) => {
          rotor.rotation.z += 0.035;
        });

        // Rotate hub ring halos
        hubsGroup.children.forEach((hub) => {
          if (hub.children[1]) {
            hub.children[1].rotation.z += 0.016;
          }
        });
      } else if (currentViewMode === 'asset') {
        if (animatedRotorMesh) {
          animatedRotorMesh.rotation.z += 0.024;
        }
        if (animatedTrackerMesh) {
          animatedTrackerMesh.rotation.z = Math.sin(Date.now() * 0.0006) * 0.52;
        }
      }
    }

    renderer.render(scene, camera);
  }

  // Pointer & Raycasting Handlers
  function onPointerMove(e) {
    const rect = canvasEl.getBoundingClientRect();
    mouse.x = ((e.clientX - rect.left) / rect.width) * 2 - 1;
    mouse.y = -((e.clientY - rect.top) / rect.height) * 2 + 1;

    raycaster.setFromCamera(mouse, camera);
    const intersects = raycaster.intersectObjects(interactiveObjects, true);

    if (intersects.length > 0) {
      let targetObj = intersects[0].object;
      while (targetObj && !targetObj.userData.name && !targetObj.userData.title && targetObj.parent) {
        targetObj = targetObj.parent;
      }

      if (targetObj && targetObj.userData) {
        showTooltip(e.clientX, e.clientY, targetObj.userData);
        canvasEl.style.cursor = 'pointer';
        return;
      }
    }

    hideTooltip();
    canvasEl.style.cursor = 'grab';
  }

  function onPointerDown() {
    canvasEl.style.cursor = 'grabbing';
  }

  function showTooltip(clientX, clientY, data) {
    if (!tooltipEl) return;

    if (currentViewMode === 'twin' && data.category) {
      const regLabel = data.region ? (data.region === 'north' ? 'MIỀN BẮC' : (data.region === 'central' ? 'MIỀN TRUNG' : 'MIỀN NAM')) : 'TOÀN QUỐC';
      tooltipEl.innerHTML = `
        <div class="font-mono text-[9px] uppercase font-bold text-teal-600 dark:text-teal-400 flex items-center justify-between">
          <span>${(data.category || '').toUpperCase()} HUB &middot; ${(data.mw || 0).toLocaleString()} MW</span>
          <span class="text-[8.5px] px-1 rounded bg-slate-100 dark:bg-slate-800 text-slate-500">${regLabel}</span>
        </div>
        <div class="text-xs font-bold text-slate-900 dark:text-slate-100 mt-0.5">
          ${data.name}
        </div>
        <div class="text-[11px] text-slate-500 dark:text-slate-400 mt-1 leading-snug">
          ${data.desc}
        </div>
        <div class="mt-1.5 pt-1 border-t border-slate-100 dark:border-slate-800 font-mono text-[10px] text-slate-400 flex justify-between">
          <span>Coords: ${data.lat ? data.lat.toFixed(2) : ''}°N, ${data.lng ? data.lng.toFixed(2) : ''}°E</span>
          <span class="text-emerald-600 font-semibold">Live Monitored</span>
        </div>
      `;
    } else if (data.title) {
      tooltipEl.innerHTML = `
        <div class="font-mono text-[9px] uppercase font-bold text-cyan-600 dark:text-cyan-400">
          ENGINEERING COMPONENT &middot; 3D INSPECTION
        </div>
        <div class="text-xs font-bold text-slate-900 dark:text-slate-100 mt-0.5">
          ${data.title}
        </div>
        <div class="text-[11px] text-slate-600 dark:text-slate-300 mt-1 leading-snug">
          ${data.desc}
        </div>
      `;
    } else {
      return;
    }

    tooltipEl.style.display = 'block';
    const rect = containerEl.getBoundingClientRect();
    const x = clientX - rect.left + 15;
    const y = clientY - rect.top - 20;

    tooltipEl.style.left = `${Math.min(x, rect.width - 260)}px`;
    tooltipEl.style.top = `${Math.max(10, y)}px`;
  }

  function hideTooltip() {
    if (tooltipEl) tooltipEl.style.display = 'none';
  }

  function onWindowResize() {
    if (!renderer || !camera || !containerEl) return;
    camera.aspect = containerEl.clientWidth / containerEl.clientHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(containerEl.clientWidth, containerEl.clientHeight);
  }

  function updateThemeColors() {
    if (!scene) return;
    const isDark = document.documentElement.classList.contains('dark');
    const p = isDark ? THEME_PALETTES.dark : THEME_PALETTES.light;

    scene.background.set(p.bg);
    scene.fog.color.set(p.fog);
    ambientLight.color.set(p.ambient);

    gridHelper.material.color.set(p.grid);
    buildVietnamTerritory(p);
    buildHubPillarsWithMiniModels(p);
    buildSupergridTransmissionArcs(p);
    buildEvCorridorCloud(p);
    buildDetailedAssetModel(currentAssetId, p);
  }

  function updateSpecCard(assetId) {
    if (!specCardEl) {
      specCardEl = document.getElementById('energy3dSpecCard');
    }
    if (!specCardEl) return;

    const profile = ASSET_PROFILES[assetId] || ASSET_PROFILES.wind_turbine;
    let specsHtml = profile.specs.map(s => `
      <div class="flex items-center justify-between py-1 border-b border-slate-100 dark:border-slate-800 text-[11px]">
        <span class="text-slate-500 dark:text-slate-400">${s.label}</span>
        <span class="font-mono font-semibold text-slate-900 dark:text-slate-100">${s.value}</span>
      </div>
    `).join('');

    specCardEl.innerHTML = `
      <div class="space-y-2">
        <div class="flex items-center justify-between">
          <span class="font-mono text-[9px] uppercase font-bold text-cyan-600 dark:text-cyan-400 tracking-wider">
            ${profile.category}
          </span>
          <span class="px-1.5 py-0.5 rounded text-[9px] font-mono bg-emerald-50 dark:bg-emerald-950/60 text-emerald-600 border border-emerald-200/50">
            IEC Certified
          </span>
        </div>
        <div>
          <h3 class="text-xs sm:text-sm font-bold text-slate-900 dark:text-slate-100 leading-snug">
            ${profile.name}
          </h3>
          <p class="text-[10px] text-slate-500 dark:text-slate-400 mt-0.5">
            ${profile.subtitle}
          </p>
        </div>
        <div class="mt-2 pt-1">
          ${specsHtml}
        </div>
        <p class="text-[10.5px] text-slate-600 dark:text-slate-300 leading-relaxed pt-1">
          ${profile.description}
        </p>
      </div>
    `;
  }

  // =========================================================================
  // PUBLIC CONTROLLER API
  // =========================================================================

  const RVN_ENERGY_3D = {
    init: async function(containerId = 'energy3dContainer', canvasId = 'energy3dCanvas', tooltipId = 'energy3dTooltip', specCardId = 'energy3dSpecCard') {
      containerEl = document.getElementById(containerId);
      canvasEl = document.getElementById(canvasId);
      tooltipEl = document.getElementById(tooltipId);
      specCardEl = document.getElementById(specCardId);

      if (!containerEl || !canvasEl) {
        console.warn('[RVN_3D] Target elements not found.');
        return false;
      }

      await loadThreeLibraries();
      initScene();
      updateSpecCard(currentAssetId);

      const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            isVisible = true;
            if (!animFrameId) animate();
          } else {
            isVisible = false;
            if (animFrameId) {
              cancelAnimationFrame(animFrameId);
              animFrameId = null;
            }
          }
        });
      }, { threshold: 0.1 });

      observer.observe(containerEl);
      return true;
    },

    switchViewMode: function(mode) {
      if (mode !== 'twin' && mode !== 'asset') return;
      currentViewMode = mode;

      const isDark = document.documentElement.classList.contains('dark');
      const p = isDark ? THEME_PALETTES.dark : THEME_PALETTES.light;

      if (mode === 'twin') {
        landGroup.visible = true;
        hubsGroup.visible = activeLayers.renewables;
        arcsGroup.visible = activeLayers.grid;
        evGroup.visible = activeLayers.ev;
        assetGroup.visible = false;

        gridHelper.visible = true;
        assetGridHelper.visible = false;

        this.setCameraPreset('national');

        const twinControls = document.getElementById('energy3dTwinControls');
        const assetControls = document.getElementById('energy3dAssetControls');
        const specCard = document.getElementById('energy3dSpecCard');
        if (twinControls) twinControls.style.display = 'flex';
        if (assetControls) assetControls.style.display = 'none';
        if (specCard) specCard.style.display = 'none';

        interactiveObjects = [];
        hubsGroup.children.forEach(h => {
          if (h.children[0]) interactiveObjects.push(h.children[0]);
        });
      } else {
        landGroup.visible = false;
        hubsGroup.visible = false;
        arcsGroup.visible = false;
        evGroup.visible = false;
        assetGroup.visible = true;

        gridHelper.visible = false;
        assetGridHelper.visible = true;

        if (camera && controls) {
          camera.position.set(0, 10, 22);
          controls.target.set(0, 6, 0);
          controls.update();
        }

        const twinControls = document.getElementById('energy3dTwinControls');
        const assetControls = document.getElementById('energy3dAssetControls');
        const specCard = document.getElementById('energy3dSpecCard');
        if (twinControls) twinControls.style.display = 'none';
        if (assetControls) assetControls.style.display = 'flex';
        if (specCard) specCard.style.display = 'block';

        this.loadAsset(currentAssetId);
      }
    },

    filterRegion: function(region, btn) {
      activeRegionFilter = region;
      const isDark = document.documentElement.classList.contains('dark');
      const p = isDark ? THEME_PALETTES.dark : THEME_PALETTES.light;
      buildHubPillarsWithMiniModels(p);

      const btns = document.querySelectorAll('.btn-3d-preset');
      btns.forEach(b => {
        b.className = 'btn-3d-preset px-2 py-1 rounded text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white transition-colors';
      });
      if (btn) {
        btn.className = 'btn-3d-preset px-2 py-1 rounded bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-200 font-semibold shadow-2xs hover:text-teal-600 transition-colors';
      }

      this.setCameraPreset(region);
    },

    loadAsset: function(assetId) {
      if (!ASSET_PROFILES[assetId]) return;
      currentAssetId = assetId;

      const isDark = document.documentElement.classList.contains('dark');
      const p = isDark ? THEME_PALETTES.dark : THEME_PALETTES.light;

      buildDetailedAssetModel(assetId, p);
      updateSpecCard(assetId);

      if (camera && controls) {
        if (assetId === 'wind_turbine') {
          camera.position.set(0, 14, 30);
          controls.target.set(0, 11, 0);
        } else if (assetId === 'solar_tracker') {
          camera.position.set(0, 10, 18);
          controls.target.set(0, 2.5, 0);
        } else if (assetId === 'pylon_500kv') {
          camera.position.set(0, 15, 32);
          controls.target.set(0, 12, 0);
        } else if (assetId === 'transformer_500kv') {
          camera.position.set(0, 8, 16);
          controls.target.set(0, 3.5, 0);
        } else if (assetId === 'bess_container') {
          camera.position.set(0, 6, 17);
          controls.target.set(0, 2.0, 0);
        }
        controls.update();
      }

      const buttons = document.querySelectorAll('.btn-asset-select');
      buttons.forEach(b => {
        if (b.getAttribute('data-asset') === assetId) {
          b.className = 'btn-asset-select px-2.5 py-1 rounded bg-cyan-600 text-white font-semibold shadow-2xs transition-all';
        } else {
          b.className = 'btn-asset-select px-2.5 py-1 rounded text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white transition-all';
        }
      });
    },

    setCameraPreset: function(preset) {
      if (!camera || !controls) return;
      const targets = {
        all: { pos: [0, 32, 42], target: [0, 0, 0] },
        national: { pos: [0, 32, 42], target: [0, 0, 0] },
        north: { pos: [-2, 16, -2], target: [-2, 0, -12] },
        central: { pos: [8, 18, 10], target: [2, 0, 0] },
        south: { pos: [4, 18, 26], target: [2, 0, 14] }
      };

      const t = targets[preset] || targets.all;
      controls.target.set(t.target[0], t.target[1], t.target[2]);
      camera.position.set(t.pos[0], t.pos[1], t.pos[2]);
      controls.update();
    },

    toggleLayer: function(layerName) {
      if (activeLayers[layerName] === undefined) return;
      activeLayers[layerName] = !activeLayers[layerName];

      if (layerName === 'grid' && arcsGroup) arcsGroup.visible = activeLayers.grid;
      if (layerName === 'renewables' && hubsGroup) hubsGroup.visible = activeLayers.renewables;
      if (layerName === 'ev' && evGroup) evGroup.visible = activeLayers.ev;

      return activeLayers[layerName];
    },

    toggleAnimation: function() {
      isAnimationPlaying = !isAnimationPlaying;
      return isAnimationPlaying;
    },

    toggleWireframe: function() {
      isWireframeActive = !isWireframeActive;
      const isDark = document.documentElement.classList.contains('dark');
      const p = isDark ? THEME_PALETTES.dark : THEME_PALETTES.light;
      if (currentViewMode === 'twin') {
        buildVietnamTerritory(p);
        buildHubPillarsWithMiniModels(p);
      } else {
        buildDetailedAssetModel(currentAssetId, p);
      }
      return isWireframeActive;
    },

    resetView: function() {
      if (currentViewMode === 'twin') {
        this.setCameraPreset('national');
      } else {
        this.loadAsset(currentAssetId);
      }
    }
  };

  window.RVN_ENERGY_3D = RVN_ENERGY_3D;
})(window);
