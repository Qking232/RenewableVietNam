/**
 * Renewable Viet Nam - 3D Geospatial Clean Energy Digital Twin & Engineering Asset Suite
 * Release Rev.001 (Synchronized to Apex Homepage Release Rev.041)
 * WebGL 3D Engine powered by Three.js (Procedural Buffer Geometries, Zero External 3D Weight)
 * 
 * Features:
 *  1. Dual-Mode Viewport:
 *     - 'twin': 3D Geospatial Digital Twin (Extruded Vietnam ribbon, 12 regional hubs with 3D miniature assets, 500kV Circuit-3 arcs, EV point cloud)
 *     - 'asset': 3D Engineering Asset Explorer (5 high-resolution procedural models: 6.2MW Wind Turbine, Solar Tracker, 500kV Pylon, 500kV Transformer, 5MWh BESS)
 *  2. Interactive Component Inspection with Raycasting Hotspots & Technical Spec HUD.
 *  3. Dynamic Animation Loops (spinning rotor, tracking tilt, photon power transfer).
 *  4. Zero-Render-Waste Lifecycle via IntersectionObserver & Theme Synchronization.
 */
(function(window) {
  'use strict';

  // 12 Major Regional Energy Hubs across Vietnam
  const ENERGY_HUBS = [
    { id: 'son_la', name: 'Sơn La Hydro Complex', category: 'hydro', mw: 2400, lat: 21.49, lng: 103.99, desc: 'Largest hydroelectric plant in SE Asia (6x 400MW Francis units)' },
    { id: 'hoa_binh', name: 'Hòa Bình Hydro Baseload', category: 'hydro', mw: 1920, lat: 20.81, lng: 105.32, desc: 'Critical northern frequency regulation & flood control' },
    { id: 'quang_ninh', name: 'Quảng Ninh Energy & LNG Hub', category: 'lng', mw: 2400, lat: 21.03, lng: 107.12, desc: 'Northern baseload coastal cluster & deep-water LNG port' },
    { id: 'pho_noi', name: 'Phố Nối 500kV Supergrid Hub', category: 'substation', mw: 5000, lat: 20.93, lng: 106.05, desc: 'Northern terminus of 519 km 500kV Circuit-3 Supergrid' },
    { id: 'nghi_son', name: 'Nghi Sơn Strategic Hub', category: 'hybrid', mw: 1800, lat: 19.33, lng: 105.78, desc: 'North-Central intertie node & industrial refinery complex' },
    { id: 'quang_trach', name: 'Quảng Trạch 500kV Hub', category: 'substation', mw: 5000, lat: 17.80, lng: 106.45, desc: 'Circuit-3 origin wheeling central clean power northward' },
    { id: 'gia_lai', name: 'Gia Lai Onshore Wind Cluster', category: 'wind', mw: 1450, lat: 13.98, lng: 108.00, desc: 'High-plateau wind corridor & 500kV Pleiku transmission hub' },
    { id: 'dak_lak', name: 'Đắk Lắk Clean Energy Hub', category: 'wind', mw: 1200, lat: 12.80, lng: 108.15, desc: 'Ea Nam onshore wind farm & Central Highlands solar farm' },
    { id: 'ninh_thuan', name: 'Ninh Thuận Renewable Capital', category: 'solar', mw: 3200, lat: 11.68, lng: 108.95, desc: 'National renewable zone: Trung Nam, Bim, and Bác Ái PSP' },
    { id: 'binh_thuan', name: 'Bình Thuận Marine Wind & Solar', category: 'solar', mw: 2800, lat: 11.10, lng: 108.20, desc: 'Offshore wind concessions & ground-mount utility solar' },
    { id: 'phu_my', name: 'Phú Mỹ / Long An LNG Center', category: 'lng', mw: 3000, lat: 10.58, lng: 107.03, desc: 'Southern gas-fired generation & Thị Vải LNG terminal' },
    { id: 'tra_vinh', name: 'Trà Vinh / Bạc Liêu Offshore', category: 'wind', mw: 2000, lat: 9.25, lng: 105.75, desc: 'Mekong Delta tidal & nearshore marine wind turbine clusters' }
  ];

  // 5 Detailed Engineering Asset Profiles
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
      ambient: 0x718096,
      dirLight: 0xffffff,
      arcCircuit3: 0x06b6d4,
      arcCircuit12: 0x3b82f6,
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
      ambient: 0xa0aec0,
      dirLight: 0xffffff,
      arcCircuit3: 0x0891b2,
      arcCircuit12: 0x2563eb,
      evColor: 0x059669,
      steel: 0x64748b,
      steelLight: 0xcbd5e1,
      pvBlue: 0x1e40af,
      copper: 0xd97706,
      accent: 0x0284c7
    }
  };

  const CATEGORY_COLORS = {
    solar: 0x10b981,
    wind: 0x06b6d4,
    hydro: 0x3b82f6,
    lng: 0xf59e0b,
    substation: 0xa855f7,
    hybrid: 0x6366f1
  };

  // Core Three.js Engine Variables
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
    scene.fog = new THREE.FogExp2(p.fog, 0.015);

    const aspect = containerEl.clientWidth / containerEl.clientHeight;
    camera = new THREE.PerspectiveCamera(45, aspect, 1, 500);
    camera.position.set(0, 32, 42);

    renderer = new THREE.WebGLRenderer({ canvas: canvasEl, antialias: true, alpha: true });
    renderer.setSize(containerEl.clientWidth, containerEl.clientHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2.0));
    renderer.shadowMap.enabled = true;
    renderer.shadowMap.type = THREE.PCFSoftShadowMap;

    // OrbitControls
    controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.06;
    controls.maxPolarAngle = Math.PI / 2.1;
    controls.minDistance = 6;
    controls.maxDistance = 80;
    controls.target.set(0, 0, 0);

    // Global Lighting
    ambientLight = new THREE.AmbientLight(p.ambient, 1.3);
    scene.add(ambientLight);

    dirLight = new THREE.DirectionalLight(p.dirLight, 1.6);
    dirLight.position.set(20, 45, 25);
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

    // Interaction Setup
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

    // Construct Geospatial Digital Twin
    buildVietnamTerritory(p);
    buildHubPillarsWithMiniModels(p);
    buildSupergridTransmissionArcs(p);
    buildEvCorridorCloud(p);

    // Build Initial Selected Asset (Wind Turbine)
    buildDetailedAssetModel(currentAssetId, p);

    // Event Listeners
    window.addEventListener('resize', onWindowResize);
    canvasEl.addEventListener('pointermove', onPointerMove);
    canvasEl.addEventListener('pointerdown', onPointerDown);

    // Observer for Theme Changes
    const observer = new MutationObserver(updateThemeColors);
    observer.observe(document.documentElement, { attributes: true, attributeFilter: ['class', 'data-theme'] });

    isInitialized = true;
  }

  // 1. Procedural Vietnam Territorial Ribbon & Maritime Islands
  function buildVietnamTerritory(p) {
    landGroup.clear();

    const spineCoords = [
      [22.8, 105.0], [21.5, 104.2], [21.0, 105.8], [20.8, 106.7],
      [19.8, 105.9], [18.6, 105.7], [17.8, 106.5], [16.5, 107.6],
      [16.0, 108.2], [15.2, 108.8], [14.0, 109.1], [13.0, 109.3],
      [12.2, 109.2], [11.5, 108.9], [10.8, 107.8], [10.2, 106.5],
      [9.2, 105.5], [8.6, 104.8]
    ];

    const shape = new THREE.Shape();
    const first = geoTo3D(spineCoords[0][0], spineCoords[0][1]);
    shape.moveTo(first.x, first.z);

    for (let i = 1; i < spineCoords.length; i++) {
      const pt = geoTo3D(spineCoords[i][0], spineCoords[i][1]);
      shape.lineTo(pt.x, pt.z);
    }
    for (let i = spineCoords.length - 1; i >= 0; i--) {
      const pt = geoTo3D(spineCoords[i][0], spineCoords[i][1] - 0.7);
      shape.lineTo(pt.x, pt.z);
    }
    shape.closePath();

    const extrudeSettings = {
      steps: 1,
      depth: 0.35,
      bevelEnabled: true,
      bevelThickness: 0.1,
      bevelSize: 0.1,
      bevelSegments: 2
    };

    const geometry = new THREE.ExtrudeGeometry(shape, extrudeSettings);
    geometry.rotateX(Math.PI / 2);

    const material = new THREE.MeshStandardMaterial({
      color: p.land,
      roughness: 0.6,
      metalness: 0.1,
      wireframe: isWireframeActive
    });

    const mesh = new THREE.Mesh(geometry, material);
    mesh.position.y = 0.0;
    mesh.receiveShadow = true;
    landGroup.add(mesh);

    // Offshore Islands (Hoàng Sa & Trường Sa representation)
    const hs = geoTo3D(16.5, 112.0);
    const ts = geoTo3D(10.0, 114.5);

    const islandMat = new THREE.MeshStandardMaterial({ color: 0x0ea5e9, roughness: 0.4, wireframe: isWireframeActive });
    const hsMesh = new THREE.Mesh(new THREE.CylinderGeometry(0.5, 0.5, 0.25, 8), islandMat);
    hsMesh.position.set(hs.x, 0.12, hs.z);
    landGroup.add(hsMesh);

    const tsMesh = new THREE.Mesh(new THREE.CylinderGeometry(0.6, 0.6, 0.25, 8), islandMat);
    tsMesh.position.set(ts.x, 0.12, ts.z);
    landGroup.add(tsMesh);
  }

  // 2. 3D Regional Generation Hub Pillars with Miniature Procedural Assets
  function buildHubPillarsWithMiniModels(p) {
    hubsGroup.clear();
    miniTurbineRotors = [];
    interactiveObjects = [];

    ENERGY_HUBS.forEach((hub) => {
      const pos = geoTo3D(hub.lat, hub.lng);
      const height = Math.max(1.4, (hub.mw / 5000) * 6.5);
      const colorHex = CATEGORY_COLORS[hub.category] || 0x10b981;

      const hubRoot = new THREE.Group();
      hubRoot.position.set(pos.x, 0.35, pos.z);

      // Base Hexagonal Foundation Pillar
      const baseGeom = new THREE.CylinderGeometry(0.35, 0.48, height, 6);
      baseGeom.translate(0, height / 2, 0);

      const baseMat = new THREE.MeshStandardMaterial({
        color: colorHex,
        roughness: 0.3,
        metalness: 0.5,
        emissive: colorHex,
        emissiveIntensity: 0.25,
        wireframe: isWireframeActive
      });

      const baseMesh = new THREE.Mesh(baseGeom, baseMat);
      baseMesh.castShadow = true;
      baseMesh.userData = hub;
      hubRoot.add(baseMesh);
      interactiveObjects.push(baseMesh);

      // Halo Cap
      const haloGeom = new THREE.RingGeometry(0.4, 0.75, 16);
      haloGeom.rotateX(-Math.PI / 2);
      const haloMat = new THREE.MeshBasicMaterial({
        color: colorHex,
        side: THREE.DoubleSide,
        transparent: true,
        opacity: 0.8
      });
      const halo = new THREE.Mesh(haloGeom, haloMat);
      halo.position.set(0, height + 0.05, 0);
      hubRoot.add(halo);

      // Attach 3D Miniature Model on Top of Hub
      if (hub.category === 'wind') {
        // Mini Wind Turbine
        const miniTurbine = createMiniTurbine(p);
        miniTurbine.position.set(0, height + 0.1, 0);
        hubRoot.add(miniTurbine);
      } else if (hub.category === 'solar') {
        // Mini Solar PV Array
        const miniSolar = createMiniSolar(p);
        miniSolar.position.set(0, height + 0.1, 0);
        hubRoot.add(miniSolar);
      } else if (hub.category === 'hydro') {
        // Mini Hydro Dam
        const miniDam = createMiniDam(p);
        miniDam.position.set(0, height + 0.1, 0);
        hubRoot.add(miniDam);
      } else if (hub.category === 'substation') {
        // Mini 500kV Pylon Tower
        const miniPylon = createMiniPylon(p);
        miniPylon.position.set(0, height + 0.1, 0);
        hubRoot.add(miniPylon);
      }

      hubsGroup.add(hubRoot);
    });
  }

  // Miniature Procedural Builders for Map Hubs
  function createMiniTurbine(p) {
    const group = new THREE.Group();
    // Tower
    const towerGeom = new THREE.CylinderGeometry(0.06, 0.12, 1.4, 8);
    towerGeom.translate(0, 0.7, 0);
    const towerMat = new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 0.4, metalness: 0.2 });
    const tower = new THREE.Mesh(towerGeom, towerMat);
    group.add(tower);

    // Nacelle
    const nacelleGeom = new THREE.BoxGeometry(0.18, 0.14, 0.35);
    nacelleGeom.translate(0, 1.45, 0);
    const nacelle = new THREE.Mesh(nacelleGeom, towerMat);
    group.add(nacelle);

    // Rotor & 3 Blades
    const rotorGroup = new THREE.Group();
    rotorGroup.position.set(0, 1.45, 0.2);

    const hubGeom = new THREE.ConeGeometry(0.08, 0.14, 8);
    hubGeom.rotateX(Math.PI / 2);
    const hubMesh = new THREE.Mesh(hubGeom, towerMat);
    rotorGroup.add(hubMesh);

    for (let i = 0; i < 3; i++) {
      const bladeGeom = new THREE.BoxGeometry(0.06, 0.75, 0.02);
      bladeGeom.translate(0, 0.38, 0);
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
    const panelGeom = new THREE.BoxGeometry(1.0, 0.04, 0.7);
    panelGeom.rotateX(-Math.PI / 6); // 30 deg tilt
    const panelMat = new THREE.MeshStandardMaterial({ color: 0x1e3a8a, roughness: 0.3, metalness: 0.5 });
    const panel = new THREE.Mesh(panelGeom, panelMat);
    panel.position.set(0, 0.35, 0);
    group.add(panel);

    const postGeom = new THREE.CylinderGeometry(0.04, 0.04, 0.35, 6);
    postGeom.translate(0, 0.17, 0);
    const postMat = new THREE.MeshStandardMaterial({ color: 0x94a3b8, metalness: 0.8 });
    group.add(new THREE.Mesh(postGeom, postMat));
    return group;
  }

  function createMiniDam(p) {
    const group = new THREE.Group();
    const damGeom = new THREE.BoxGeometry(0.8, 0.45, 0.4);
    const damMat = new THREE.MeshStandardMaterial({ color: 0x64748b, roughness: 0.8 });
    const dam = new THREE.Mesh(damGeom, damMat);
    dam.position.set(0, 0.22, 0);
    group.add(dam);

    // Water channel
    const waterGeom = new THREE.BoxGeometry(0.25, 0.15, 0.6);
    const waterMat = new THREE.MeshStandardMaterial({ color: 0x38bdf8, roughness: 0.1, transparent: true, opacity: 0.85 });
    const water = new THREE.Mesh(waterGeom, waterMat);
    water.position.set(0, 0.22, 0.1);
    group.add(water);
    return group;
  }

  function createMiniPylon(p) {
    const group = new THREE.Group();
    const towerGeom = new THREE.ConeGeometry(0.2, 1.2, 4);
    towerGeom.translate(0, 0.6, 0);
    const towerMat = new THREE.MeshStandardMaterial({ color: 0xa855f7, metalness: 0.7, wireframe: true });
    group.add(new THREE.Mesh(towerGeom, towerMat));

    // Crossarm
    const armGeom = new THREE.BoxGeometry(0.7, 0.04, 0.04);
    armGeom.translate(0, 0.95, 0);
    group.add(new THREE.Mesh(armGeom, towerMat));
    return group;
  }

  // 3. 500kV Circuit-3 Supergrid Arcs with Moving Photon Particles
  function buildSupergridTransmissionArcs(p) {
    arcsGroup.clear();
    arcParticles = [];

    const corridors = [
      {
        name: '500kV Circuit-3 (Quảng Trạch - Nghi Sơn - Phố Nối)',
        from: [17.80, 106.45],
        mid: [19.33, 105.78],
        to: [20.93, 106.05],
        color: p.arcCircuit3,
        particleCount: 16
      },
      {
        name: '500kV Central Spine (Quảng Trạch - Gia Lai)',
        from: [17.80, 106.45],
        mid: [15.80, 107.50],
        to: [13.98, 108.00],
        color: p.arcCircuit12,
        particleCount: 12
      },
      {
        name: '500kV Southern Spine (Gia Lai - Phú Mỹ)',
        from: [13.98, 108.00],
        mid: [12.20, 107.50],
        to: [10.58, 107.03],
        color: p.arcCircuit12,
        particleCount: 14
      }
    ];

    corridors.forEach((corr) => {
      const p1 = geoTo3D(corr.from[0], corr.from[1]);
      const pm = geoTo3D(corr.mid[0], corr.mid[1]);
      const p2 = geoTo3D(corr.to[0], corr.to[1]);

      const v1 = new THREE.Vector3(p1.x, 2.0, p1.z);
      const vm = new THREE.Vector3(pm.x, 6.5, pm.z);
      const v2 = new THREE.Vector3(p2.x, 2.0, p2.z);

      const curve = new THREE.QuadraticBezierCurve3(v1, vm, v2);
      const points = curve.getPoints(50);
      const geometry = new THREE.BufferGeometry().setFromPoints(points);

      const material = new THREE.LineBasicMaterial({
        color: corr.color,
        linewidth: 2,
        transparent: true,
        opacity: 0.85
      });

      const line = new THREE.Line(geometry, material);
      arcsGroup.add(line);

      const particleGeom = new THREE.SphereGeometry(0.16, 8, 8);
      const particleMat = new THREE.MeshBasicMaterial({ color: 0xffffff });

      for (let i = 0; i < corr.particleCount; i++) {
        const mesh = new THREE.Mesh(particleGeom, particleMat);
        arcsGroup.add(mesh);
        arcParticles.push({
          mesh: mesh,
          curve: curve,
          progress: i / corr.particleCount,
          speed: 0.0035 + Math.random() * 0.001
        });
      }
    });
  }

  // 4. 22,055 EV Charging Corridor Point Cloud
  function buildEvCorridorCloud(p) {
    evGroup.clear();

    const count = 450;
    const positions = new Float32Array(count * 3);

    for (let i = 0; i < count; i++) {
      const t = i / count;
      const lat = 8.8 + t * (21.5 - 8.8);
      let lng = 105.0 + Math.sin(t * Math.PI) * 3.5 + (Math.random() - 0.5) * 0.45;

      const pt = geoTo3D(lat, lng);
      positions[i * 3 + 0] = pt.x;
      positions[i * 3 + 1] = 0.45 + Math.random() * 0.2;
      positions[i * 3 + 2] = pt.z;
    }

    const geometry = new THREE.BufferGeometry();
    geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));

    const material = new THREE.PointsMaterial({
      color: p.evColor,
      size: 0.4,
      transparent: true,
      opacity: 0.75
    });

    const pointCloud = new THREE.Points(geometry, material);
    evGroup.add(pointCloud);
  }

  // =========================================================================
  // 5. HIGH-RESOLUTION PROCEDURAL 3D ENGINEERING ASSET BUILDERS
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

    // Materials
    const steelMat = new THREE.MeshStandardMaterial({ color: 0xe2e8f0, roughness: 0.35, metalness: 0.3, wireframe: isWireframeActive });
    const darkMat = new THREE.MeshStandardMaterial({ color: 0x334155, roughness: 0.5, metalness: 0.7, wireframe: isWireframeActive });
    const redMat = new THREE.MeshStandardMaterial({ color: 0xef4444, roughness: 0.4, wireframe: isWireframeActive });

    // Foundation Platform
    const foundGeom = new THREE.CylinderGeometry(4.2, 4.6, 0.8, 24);
    foundGeom.translate(0, 0.4, 0);
    const foundMesh = new THREE.Mesh(foundGeom, darkMat);
    foundMesh.receiveShadow = true;
    root.add(foundMesh);

    // Tapered Steel Tubular Tower (Height: 18)
    const towerGeom = new THREE.CylinderGeometry(0.75, 1.35, 18.0, 32);
    towerGeom.translate(0, 9.8, 0);
    const towerMesh = new THREE.Mesh(towerGeom, steelMat);
    towerMesh.castShadow = true;
    towerMesh.userData = { title: 'Tubular Steel Tower', desc: '115m multi-section conical steel tower with internal service hoist and cable tray.' };
    root.add(towerMesh);
    if (currentViewMode === 'asset') interactiveObjects.push(towerMesh);

    // Nacelle Bedplate & Housing
    const nacelleRoot = new THREE.Group();
    nacelleRoot.position.set(0, 18.8, 0);

    const nacelleGeom = new THREE.BoxGeometry(2.4, 2.2, 5.2);
    nacelleGeom.translate(0, 0.2, -0.6);
    const nacelleMesh = new THREE.Mesh(nacelleGeom, steelMat);
    nacelleMesh.castShadow = true;
    nacelleMesh.userData = { title: 'Nacelle & Direct-Drive Generator', desc: 'Houses 6.2 MW permanent magnet synchronous generator (PMSG), converter, and transformer.' };
    nacelleRoot.add(nacelleMesh);
    if (currentViewMode === 'asset') interactiveObjects.push(nacelleMesh);

    // Cooler Unit at Rear
    const coolerGeom = new THREE.BoxGeometry(1.6, 0.8, 1.2);
    coolerGeom.translate(0, 1.4, -2.2);
    const coolerMesh = new THREE.Mesh(coolerGeom, darkMat);
    nacelleRoot.add(coolerMesh);

    // Aviation Warning Strobe Beacon
    const beaconGeom = new THREE.CylinderGeometry(0.12, 0.12, 0.25, 12);
    beaconGeom.translate(0, 1.8, -1.0);
    const beaconMesh = new THREE.Mesh(beaconGeom, new THREE.MeshBasicMaterial({ color: 0xff0000 }));
    nacelleRoot.add(beaconMesh);

    // Rotor Hub & Spinner Cone
    const rotorHub = new THREE.Group();
    rotorHub.position.set(0, 0.2, 2.1);

    const spinnerGeom = new THREE.ConeGeometry(0.95, 1.8, 24);
    spinnerGeom.rotateX(Math.PI / 2);
    const spinnerMesh = new THREE.Mesh(spinnerGeom, steelMat);
    rotorHub.add(spinnerMesh);

    // 3 Aerodynamic Blades (Rotor Diameter ~28 units)
    for (let i = 0; i < 3; i++) {
      const bladeGroup = new THREE.Group();
      bladeGroup.rotation.z = (i * Math.PI * 2) / 3;

      // Blade Root
      const bladeRootGeom = new THREE.CylinderGeometry(0.32, 0.38, 1.2, 16);
      bladeRootGeom.translate(0, 0.6, 0);
      bladeGroup.add(new THREE.Mesh(bladeRootGeom, darkMat));

      // Main Aerofoil Blade
      const bladeGeom = new THREE.ConeGeometry(0.38, 12.5, 16);
      bladeGeom.translate(0, 7.2, 0);
      const bladeMesh = new THREE.Mesh(bladeGeom, steelMat);
      bladeMesh.castShadow = true;
      bladeMesh.userData = { title: 'Aerofoil Rotor Blade (84m)', desc: 'Carbon-hybrid structural spar with aerodynamic twist and lightning receptor strips.' };
      bladeGroup.add(bladeMesh);
      if (currentViewMode === 'asset') interactiveObjects.push(bladeMesh);

      // Red Aviation Tip Marking
      const tipGeom = new THREE.ConeGeometry(0.12, 2.2, 16);
      tipGeom.translate(0, 12.3, 0);
      const tipMesh = new THREE.Mesh(tipGeom, redMat);
      bladeGroup.add(tipMesh);

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

    // Ground Base Concrete Footings
    for (let x = -7.5; x <= 7.5; x += 5.0) {
      const pierGeom = new THREE.BoxGeometry(0.7, 0.8, 0.7);
      pierGeom.translate(x, 0.4, 0);
      root.add(new THREE.Mesh(pierGeom, metalMat));

      // I-Beam Vertical Support Posts
      const postGeom = new THREE.BoxGeometry(0.25, 3.2, 0.35);
      postGeom.translate(x, 2.0, 0);
      root.add(new THREE.Mesh(postGeom, metalMat));
    }

    // Rotating Torque Tube Assembly (Tracking Axis)
    const trackerAssembly = new THREE.Group();
    trackerAssembly.position.set(0, 3.6, 0);

    const tubeGeom = new THREE.CylinderGeometry(0.2, 0.2, 19.0, 16);
    tubeGeom.rotateZ(Math.PI / 2);
    const tubeMesh = new THREE.Mesh(tubeGeom, metalMat);
    trackerAssembly.add(tubeMesh);

    // Slewing Drive Motor in Center
    const motorGeom = new THREE.CylinderGeometry(0.55, 0.55, 0.8, 16);
    const motorMesh = new THREE.Mesh(motorGeom, new THREE.MeshStandardMaterial({ color: 0x334155, metalness: 0.9 }));
    motorMesh.position.set(0, 0, 0);
    motorMesh.userData = { title: 'Slewing Drive & Smart Controller', desc: 'High-torque self-locking slew gear driven by astronomical tracking algorithm with wind stow.' };
    trackerAssembly.add(motorMesh);
    if (currentViewMode === 'asset') interactiveObjects.push(motorMesh);

    // Two-in-Portrait (2P) PV Module Tables (12 module tables along tracker)
    for (let x = -8.5; x <= 8.5; x += 1.55) {
      if (Math.abs(x) < 0.8) continue; // Gap for center motor

      const tableGroup = new THREE.Group();
      tableGroup.position.set(x, 0, 0);

      // Upper PV Module
      const upperPanel = new THREE.Mesh(new THREE.BoxGeometry(1.45, 0.04, 2.2), pvMat);
      upperPanel.position.set(0, 0.08, 1.2);
      upperPanel.castShadow = true;
      upperPanel.userData = { title: 'Bifacial TOPCon PV Module (620Wp)', desc: 'N-Type monocrystalline cells with 80% bifaciality factor collecting albedo irradiance.' };
      tableGroup.add(upperPanel);
      if (currentViewMode === 'asset') interactiveObjects.push(upperPanel);

      // Lower PV Module
      const lowerPanel = new THREE.Mesh(new THREE.BoxGeometry(1.45, 0.04, 2.2), pvMat);
      lowerPanel.position.set(0, 0.08, -1.2);
      lowerPanel.castShadow = true;
      lowerPanel.userData = { title: 'Bifacial TOPCon PV Module (620Wp)', desc: 'Silver busbars with anti-reflective tempered glass and anodized aluminum frame.' };
      tableGroup.add(lowerPanel);
      if (currentViewMode === 'asset') interactiveObjects.push(lowerPanel);

      // Structural Cross Rafters
      const rafter = new THREE.Mesh(new THREE.BoxGeometry(0.08, 0.12, 4.8), frameMat);
      rafter.position.set(0, -0.06, 0);
      tableGroup.add(rafter);

      trackerAssembly.add(tableGroup);
    }

    // String Inverter Unit mounted near middle post
    const invGeom = new THREE.BoxGeometry(1.2, 1.4, 0.6);
    invGeom.translate(2.5, 2.2, 0.8);
    const invMat = new THREE.MeshStandardMaterial({ color: 0x475569, metalness: 0.6 });
    const invMesh = new THREE.Mesh(invGeom, invMat);
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
    const lineMat = new THREE.LineBasicMaterial({ color: 0x64748b });
    const insulMat = new THREE.MeshStandardMaterial({ color: 0x0284c7, roughness: 0.1, transparent: true, opacity: 0.85 });

    // Concrete Footings (4 corners)
    const corners = [
      [-3.0, -3.0], [3.0, -3.0], [3.0, 3.0], [-3.0, 3.0]
    ];
    corners.forEach(c => {
      const pier = new THREE.Mesh(new THREE.CylinderGeometry(0.7, 0.85, 1.0, 8), new THREE.MeshStandardMaterial({ color: 0x64748b, roughness: 0.8 }));
      pier.position.set(c[0], 0.5, c[1]);
      root.add(pier);
    });

    // 4 Corner Legs rising to waist (Pyramidal Truss)
    const legPoints = [];
    corners.forEach(c => {
      legPoints.push(new THREE.Vector3(c[0], 1.0, c[1]));
      legPoints.push(new THREE.Vector3(c[0] * 0.35, 13.0, c[1] * 0.35));
    });
    const legGeom = new THREE.BufferGeometry().setFromPoints(legPoints);
    root.add(new THREE.LineSegments(legGeom, new THREE.LineBasicMaterial({ color: 0x94a3b8, linewidth: 2 })));

    // Lattice Body Meshes (Stylized Truss Frames)
    const lowerBodyGeom = new THREE.CylinderGeometry(1.2, 3.8, 12.0, 4, 6, true);
    lowerBodyGeom.translate(0, 7.0, 0);
    lowerBodyGeom.rotateY(Math.PI / 4);
    const lowerBody = new THREE.Mesh(lowerBodyGeom, new THREE.MeshStandardMaterial({ color: 0x94a3b8, wireframe: true }));
    root.add(lowerBody);

    // Upper Vertical Tower Trunk
    const upperBodyGeom = new THREE.BoxGeometry(1.6, 8.0, 1.6);
    upperBodyGeom.translate(0, 17.0, 0);
    const upperBody = new THREE.Mesh(upperBodyGeom, new THREE.MeshStandardMaterial({ color: 0x64748b, wireframe: true }));
    upperBody.userData = { title: 'Galvanized Steel Truss Mast', desc: 'Engineered for 500kV wind load class III with double-laced diagonal members.' };
    root.add(upperBody);
    if (currentViewMode === 'asset') interactiveObjects.push(upperBody);

    // Crossarm 1 (Lower 500kV Phase)
    const arm1Geom = new THREE.BoxGeometry(13.5, 0.7, 1.4);
    arm1Geom.translate(0, 16.5, 0);
    const arm1 = new THREE.Mesh(arm1Geom, steelMat);
    root.add(arm1);

    // Crossarm 2 (Upper 500kV Phase)
    const arm2Geom = new THREE.BoxGeometry(10.5, 0.6, 1.4);
    arm2Geom.translate(0, 19.5, 0);
    const arm2 = new THREE.Mesh(arm2Geom, steelMat);
    root.add(arm2);

    // Peak Ground Wire Peak (OPGW)
    const peakGeom = new THREE.ConeGeometry(0.8, 2.5, 4);
    peakGeom.translate(0, 22.25, 0);
    peakGeom.rotateY(Math.PI / 4);
    root.add(new THREE.Mesh(peakGeom, steelMat));

    // 500kV Suspension Insulator Strings (6 positions)
    const insulatorPositions = [
      [-6.0, 16.2, 0], [6.0, 16.2, 0], [-3.8, 16.2, 0], [3.8, 16.2, 0],
      [-4.6, 19.2, 0], [4.6, 19.2, 0]
    ];

    insulatorPositions.forEach(pos => {
      const insulGroup = new THREE.Group();
      insulGroup.position.set(pos[0], pos[1], pos[2]);

      // Ribbed Ceramic Insulator String
      const stringGeom = new THREE.CylinderGeometry(0.18, 0.18, 2.4, 12, 16);
      stringGeom.translate(0, -1.2, 0);
      const stringMesh = new THREE.Mesh(stringGeom, insulMat);
      stringMesh.userData = { title: '500kV Composite Insulator (28 Discs)', desc: 'Creepage distance > 16,000 mm with anti-fog silicon shed profile and corona discharge rings.' };
      insulGroup.add(stringMesh);
      if (currentViewMode === 'asset') interactiveObjects.push(stringMesh);

      // Conductor Bundle Clamp & Quad Wires
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

    // Concrete Substation Foundation & Oil Pit Sump
    const foundation = new THREE.Mesh(new THREE.BoxGeometry(11.0, 0.6, 9.0), new THREE.MeshStandardMaterial({ color: 0x64748b, roughness: 0.8 }));
    foundation.position.set(0, 0.3, 0);
    root.add(foundation);

    // Main Oil Tank Body
    const tankGeom = new THREE.BoxGeometry(5.2, 4.4, 4.2);
    tankGeom.translate(0, 2.8, 0);
    const tankMesh = new THREE.Mesh(tankGeom, tankMat);
    tankMesh.castShadow = true;
    tankMesh.userData = { title: 'Transformer Core Oil Tank (900 MVA)', desc: 'High-permeability silicon steel core immersed in inhibited mineral dielectric oil.' };
    root.add(tankMesh);
    if (currentViewMode === 'asset') interactiveObjects.push(tankMesh);

    // Detached Radiator Bank (Cooling Fins)
    for (let side of [-1, 1]) {
      const radGroup = new THREE.Group();
      radGroup.position.set(side * 3.6, 2.6, 0);

      for (let z = -1.6; z <= 1.6; z += 0.45) {
        const fin = new THREE.Mesh(new THREE.BoxGeometry(0.12, 3.2, 0.35), darkMat);
        fin.position.set(0, 0, z);
        radGroup.add(fin);
      }

      // Fan Housing Cowls
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

    // Elevated Oil Conservator Tank
    const consGeom = new THREE.CylinderGeometry(0.7, 0.7, 4.6, 24);
    consGeom.rotateZ(Math.PI / 2);
    consGeom.translate(0, 5.8, -1.5);
    const consMesh = new THREE.Mesh(consGeom, tankMat);
    consMesh.userData = { title: 'Oil Conservator & Buchholz Relay', desc: 'Accommodates thermal oil expansion with rubber diaphragm bag and silica gel moisture breather.' };
    root.add(consMesh);
    if (currentViewMode === 'asset') interactiveObjects.push(consMesh);

    // 3 High-Voltage 500kV Porcelain Bushings
    for (let i = -1; i <= 1; i++) {
      const bushGroup = new THREE.Group();
      bushGroup.position.set(i * 1.5, 5.0, 0.8);
      bushGroup.rotation.x = -Math.PI / 10;

      // Ribbed Ceramic Column
      const bGeom = new THREE.CylinderGeometry(0.24, 0.38, 3.2, 16, 20);
      bGeom.translate(0, 1.6, 0);
      const bMesh = new THREE.Mesh(bGeom, bushingMat);
      bMesh.userData = { title: '500kV RIP Condenser Bushing', desc: 'Resin-impregnated paper high-voltage bushing with capacitive grading and test tap.' };
      bushGroup.add(bMesh);
      if (currentViewMode === 'asset') interactiveObjects.push(bMesh);

      // Top Terminal Stud & Corona Sphere
      const ball = new THREE.Mesh(new THREE.SphereGeometry(0.35, 16, 16), copperMat);
      ball.position.set(0, 3.2, 0);
      bushGroup.add(ball);

      root.add(bushGroup);
    }

    // Marshalling Kiosk Control Cabinet
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

    // Concrete Plinth Foundation
    const plinth = new THREE.Mesh(new THREE.BoxGeometry(13.2, 0.5, 4.2), new THREE.MeshStandardMaterial({ color: 0x64748b, roughness: 0.8 }));
    plinth.position.set(0, 0.25, 0);
    root.add(plinth);

    // 40ft ISO High-Cube Container Main Body (12.2m x 2.9m x 2.4m)
    const boxGeom = new THREE.BoxGeometry(12.2, 2.9, 2.5);
    boxGeom.translate(0, 1.95, 0);
    const boxMesh = new THREE.Mesh(boxGeom, containerMat);
    boxMesh.castShadow = true;
    boxMesh.userData = { title: '40ft ISO High-Cube BESS Enclosure', desc: 'C5-M marine anti-corrosion rated steel container housing LFP battery modules and BMS racks.' };
    root.add(boxMesh);
    if (currentViewMode === 'asset') interactiveObjects.push(boxMesh);

    // Corrugation Rib Siding Simulation
    for (let x = -5.8; x <= 5.8; x += 0.35) {
      const rib = new THREE.Mesh(new THREE.BoxGeometry(0.12, 2.7, 0.08), darkMat);
      rib.position.set(x, 1.95, 1.28);
      root.add(rib);

      const ribBack = new THREE.Mesh(new THREE.BoxGeometry(0.12, 2.7, 0.08), darkMat);
      ribBack.position.set(x, 1.95, -1.28);
      root.add(ribBack);
    }

    // Dual Roof HVAC Liquid-Cooling Chillers
    for (let side of [-2.8, 2.8]) {
      const hvacGeom = new THREE.BoxGeometry(2.4, 0.8, 1.8);
      hvacGeom.translate(side, 3.8, 0);
      const hvacMesh = new THREE.Mesh(hvacGeom, whiteMat);
      hvacMesh.userData = { title: 'Closed-Loop Liquid Thermal Chiller', desc: 'Maintains cell operating temperature at 23°C ± 2°C, extending LFP cycle life to > 8,000 cycles.' };
      root.add(hvacMesh);
      if (currentViewMode === 'asset') interactiveObjects.push(hvacMesh);

      // Fan Cowls
      const fan1 = new THREE.Mesh(new THREE.CylinderGeometry(0.4, 0.4, 0.15, 16), darkMat);
      fan1.position.set(side - 0.55, 4.25, 0);
      root.add(fan1);

      const fan2 = new THREE.Mesh(new THREE.CylinderGeometry(0.4, 0.4, 0.15, 16), darkMat);
      fan2.position.set(side + 0.55, 4.25, 0);
      root.add(fan2);
    }

    // Emergency Fire Suppression & Deflagration Vents on Roof
    for (let x of [-4.5, 0, 4.5]) {
      const vent = new THREE.Mesh(new THREE.BoxGeometry(0.9, 0.15, 0.9), yellowMat);
      vent.position.set(x, 3.48, 0);
      vent.userData = { title: 'NFPA 68 Explosion Relief Vent', desc: 'Overpressure safety relief panels and Novec 1230 / aerosol gas fire extinguishing manifold.' };
      root.add(vent);
      if (currentViewMode === 'asset') interactiveObjects.push(vent);
    }

    // Front Double Access Doors with Hazard Marking
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
        // Animate Circuit-3 photon arcs
        arcParticles.forEach((p) => {
          p.progress += p.speed;
          if (p.progress > 1.0) p.progress = 0.0;
          const pos = p.curve.getPoint(p.progress);
          p.mesh.position.copy(pos);
        });

        // Rotate miniature wind turbine rotors on map
        miniTurbineRotors.forEach((rotor) => {
          rotor.rotation.z += 0.035;
        });

        // Rotate hub ring halos
        hubsGroup.children.forEach((hub) => {
          if (hub.children[1]) {
            hub.children[1].rotation.z += 0.018;
          }
        });
      } else if (currentViewMode === 'asset') {
        // Rotate 6.2MW wind turbine rotor
        if (animatedRotorMesh) {
          animatedRotorMesh.rotation.z += 0.024;
        }

        // Oscillate solar PV tracker
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
      tooltipEl.innerHTML = `
        <div class="font-mono text-[9px] uppercase font-bold text-teal-600 dark:text-teal-400">
          ${(data.category || '').toUpperCase()} HUB &middot; ${(data.mw || 0).toLocaleString()} MW
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

  // Update Spec Card HUD in Asset View
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

      // Intersection Observer for Zero Render Waste
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

        // Reset camera to national overview
        this.setCameraPreset('national');

        // Toggle UI toolbars
        const twinControls = document.getElementById('energy3dTwinControls');
        const assetControls = document.getElementById('energy3dAssetControls');
        const specCard = document.getElementById('energy3dSpecCard');
        if (twinControls) twinControls.style.display = 'flex';
        if (assetControls) assetControls.style.display = 'none';
        if (specCard) specCard.style.display = 'none';

        // Re-index map objects for raycaster
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

        // Position camera for 3D asset inspection
        if (camera && controls) {
          camera.position.set(0, 10, 22);
          controls.target.set(0, 6, 0);
          controls.update();
        }

        // Toggle UI toolbars
        const twinControls = document.getElementById('energy3dTwinControls');
        const assetControls = document.getElementById('energy3dAssetControls');
        const specCard = document.getElementById('energy3dSpecCard');
        if (twinControls) twinControls.style.display = 'none';
        if (assetControls) assetControls.style.display = 'flex';
        if (specCard) specCard.style.display = 'block';

        this.loadAsset(currentAssetId);
      }
    },

    loadAsset: function(assetId) {
      if (!ASSET_PROFILES[assetId]) return;
      currentAssetId = assetId;

      const isDark = document.documentElement.classList.contains('dark');
      const p = isDark ? THEME_PALETTES.dark : THEME_PALETTES.light;

      buildDetailedAssetModel(assetId, p);
      updateSpecCard(assetId);

      // Reframe camera based on asset dimensions
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

      // Update active asset button state in UI
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
        national: { pos: [0, 32, 42], target: [0, 0, 0] },
        north: { pos: [-2, 16, 0], target: [-2, 0, -12] },
        central: { pos: [8, 18, 12], target: [2, 0, 0] },
        south: { pos: [4, 18, 28], target: [2, 0, 14] }
      };

      const t = targets[preset] || targets.national;
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
