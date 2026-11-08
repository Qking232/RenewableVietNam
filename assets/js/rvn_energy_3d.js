/**
 * Renewable Viet Nam - 3D Geospatial Clean Energy Digital Twin & 500kV Supergrid Spine
 * WebGL 3D Engine powered by Three.js
 * Visualizes 12 National Energy Hubs, 500kV Circuit-3 Supergrid Bézier Arcs, and EV Corridors.
 */
(function(window) {
  'use strict';

  // 12 Major Regional Energy Hubs across Vietnam
  const ENERGY_HUBS = [
    { id: 'son_la', name: 'Sơn La Hydro Complex', category: 'hydro', mw: 2400, lat: 21.49, lng: 103.99, desc: 'Largest hydroelectric plant in SE Asia (6x 400MW units)' },
    { id: 'hoa_binh', name: 'Hòa Bình Hydro Baseload', category: 'hydro', mw: 1920, lat: 20.81, lng: 105.32, desc: 'Critical northern frequency regulation & flood control' },
    { id: 'quang_ninh', name: 'Quảng Ninh Energy & LNG Hub', category: 'lng', mw: 2400, lat: 21.03, lng: 107.12, desc: 'Northern baseload coastal cluster & deep-water LNG port' },
    { id: 'pho_noi', name: 'Phố Nối 500kV Supergrid Hub', category: 'substation', mw: 5000, lat: 20.93, lng: 106.05, desc: 'Northern terminus of 519 km 500kV Circuit-3 Supergrid' },
    { id: 'nghi_son', name: 'Nghi Sơn Strategic Hub', category: 'hybrid', mw: 1800, lat: 19.33, lng: 105.78, desc: 'North-Central intertie node & industrial refinery complex' },
    { id: 'quang_trach', name: 'Quảng Trạch 500kV Hub', category: 'substation', mw: 5000, lat: 17.80, lng: 106.45, desc: 'Circuit-3 origin wheeling central clean power northward' },
    { id: 'gia_lai', name: 'Gia Lai Onshore Wind Cluster', category: 'wind', mw: 1450, lat: 13.98, lng: 108.00, desc: 'High-plateau wind corridor & 500kV Pleiku transmission hub' },
    { id: 'dak_lak', name: 'Đắk Lắk Clean Energy Hub', category: 'wind', mw: 1200, lat: 12.80, lng: 108.15, desc: 'Ea Nam onshore wind farm & Central Highlands solar farm' },
    { id: 'ninh_thuan', name: 'Ninh Thuận Renewable Capital', category: 'solar', mw: 3200, lat: 11.68, lng: 108.95, desc: 'National renewable zone: Trung Nam, Bim, and Bác Ái PSP' },
    { id: 'binh_thuan', name: 'Bình Thuận Marine Wind & Solar', category: 'solar', mw: 2800, lat: 11.10, lng: 108.20, desc: 'Offshore wind concessions & ground-mount utility solar' },
    { id: 'phu_my', name: 'Phú Mỹ / Long An LNG Center', category: 'lng', mw: 3000, lat: 10.58, lng: 107.03, desc: 'Southern gas-fired generation & Thi Vai LNG terminal' },
    { id: 'tra_vinh', name: 'Trà Vinh / Bạc Liêu Offshore', category: 'wind', mw: 2000, lat: 9.25, lng: 105.75, desc: 'Mekong Delta tidal & nearshore marine wind turbine clusters' }
  ];

  // Colors Palette
  const THEME_PALETTES = {
    dark: {
      bg: 0x070a12,
      fog: 0x070a12,
      grid: 0x1e293b,
      land: 0x0f172a,
      landBorder: 0x334155,
      ambient: 0x64748b,
      dirLight: 0xffffff,
      arcCircuit3: 0x06b6d4, // Cyan
      arcCircuit12: 0x3b82f6, // Blue
      evColor: 0x10b981
    },
    light: {
      bg: 0xf8fafc,
      fog: 0xf8fafc,
      grid: 0xe2e8f0,
      land: 0xffffff,
      landBorder: 0xcbd5e1,
      ambient: 0x94a3b8,
      dirLight: 0xffffff,
      arcCircuit3: 0x0891b2, // Cyan darker
      arcCircuit12: 0x2563eb, // Blue darker
      evColor: 0x059669
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

  let scene, camera, renderer, controls;
  let containerEl, canvasEl, tooltipEl;
  let isInitialized = false;
  let isVisible = false;
  let animFrameId = null;

  // Groups
  let landGroup, hubsGroup, arcsGroup, evGroup, gridHelper;
  let dirLight, ambientLight;
  let interactiveObjects = [];
  let raycaster, mouse;
  let arcParticles = [];

  // Active Filter States
  const activeLayers = {
    grid: true,
    renewables: true,
    ev: true
  };

  // Convert (lat, lng) to 3D Scene (X, Z) coordinates
  // Vietnam center: Lat ~16.0, Lng ~106.0
  function geoTo3D(lat, lng) {
    const scale = 2.4;
    const x = (lng - 106.0) * scale;
    const z = -(lat - 16.0) * scale;
    return { x, z };
  }

  // Asynchronously load Three.js & OrbitControls if not present
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

    // Controls
    controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.06;
    controls.maxPolarAngle = Math.PI / 2.15;
    controls.minDistance = 12;
    controls.maxDistance = 75;
    controls.target.set(0, 0, 0);

    // Lights
    ambientLight = new THREE.AmbientLight(p.ambient, 1.2);
    scene.add(ambientLight);

    dirLight = new THREE.DirectionalLight(p.dirLight, 1.5);
    dirLight.position.set(20, 45, 25);
    dirLight.castShadow = true;
    scene.add(dirLight);

    // Ground Grid Helper
    gridHelper = new THREE.GridHelper(90, 45, p.grid, p.grid);
    gridHelper.position.y = -0.05;
    scene.add(gridHelper);

    // Raycaster for Hover Telemetry
    raycaster = new THREE.Raycaster();
    mouse = new THREE.Vector2();

    // Groups
    landGroup = new THREE.Group();
    hubsGroup = new THREE.Group();
    arcsGroup = new THREE.Group();
    evGroup = new THREE.Group();

    scene.add(landGroup);
    scene.add(hubsGroup);
    scene.add(arcsGroup);
    scene.add(evGroup);

    buildVietnamTerritory(p);
    buildHubPillars();
    buildSupergridTransmissionArcs(p);
    buildEvCorridorCloud(p);

    // Events
    window.addEventListener('resize', onWindowResize);
    canvasEl.addEventListener('pointermove', onPointerMove);
    canvasEl.addEventListener('pointerdown', onPointerDown);

    // Observe theme class changes
    const observer = new MutationObserver(updateThemeColors);
    observer.observe(document.documentElement, { attributes: true, attributeFilter: ['class', 'data-theme'] });

    isInitialized = true;
  }

  // 1. Procedural Vietnam Territorial Ribbon & Islands
  function buildVietnamTerritory(p) {
    landGroup.clear();

    // S-shape coastal spine points (Lat, Lng)
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
    // Return path for thickness
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
    geometry.rotateX(Math.PI / 2); // Lay flat on XZ plane

    const material = new THREE.MeshStandardMaterial({
      color: p.land,
      roughness: 0.6,
      metalness: 0.1
    });

    const mesh = new THREE.Mesh(geometry, material);
    mesh.position.y = 0.0;
    mesh.receiveShadow = true;
    landGroup.add(mesh);

    // Offshore Islands (Hoàng Sa & Trường Sa representation)
    const hs = geoTo3D(16.5, 112.0);
    const ts = geoTo3D(10.0, 114.5);

    const islandMat = new THREE.MeshStandardMaterial({ color: 0x0ea5e9, roughness: 0.4 });
    const hsMesh = new THREE.Mesh(new THREE.CylinderGeometry(0.5, 0.5, 0.25, 8), islandMat);
    hsMesh.position.set(hs.x, 0.12, hs.z);
    landGroup.add(hsMesh);

    const tsMesh = new THREE.Mesh(new THREE.CylinderGeometry(0.6, 0.6, 0.25, 8), islandMat);
    tsMesh.position.set(ts.x, 0.12, ts.z);
    landGroup.add(tsMesh);
  }

  // 2. 3D Regional Generation Hub Pillars
  function buildHubPillars() {
    hubsGroup.clear();
    interactiveObjects = [];

    ENERGY_HUBS.forEach((hub) => {
      const pos = geoTo3D(hub.lat, hub.lng);
      const height = Math.max(1.5, (hub.mw / 5000) * 8.0);
      const colorHex = CATEGORY_COLORS[hub.category] || 0x10b981;

      // Hexagonal / Cylindrical Pillar
      const geom = new THREE.CylinderGeometry(0.35, 0.45, height, 6);
      geom.translate(0, height / 2, 0);

      const mat = new THREE.MeshStandardMaterial({
        color: colorHex,
        roughness: 0.3,
        metalness: 0.6,
        emissive: colorHex,
        emissiveIntensity: 0.25
      });

      const pillar = new THREE.Mesh(geom, mat);
      pillar.position.set(pos.x, 0.35, pos.z);
      pillar.castShadow = true;
      pillar.userData = hub;

      // Halo cap at top
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
      pillar.add(halo);

      hubsGroup.add(pillar);
      interactiveObjects.push(pillar);
    });
  }

  // 3. 500kV Circuit-3 Supergrid Arcs with Moving Photon Particles
  function buildSupergridTransmissionArcs(p) {
    arcsGroup.clear();
    arcParticles = [];

    // Transmission corridors:
    // 1. Circuit-3: Quảng Trạch (17.80, 106.45) -> Phố Nối (20.93, 106.05) via Nghi Sơn (19.33, 105.78)
    // 2. Circuit 1&2 Southern Extension: Quảng Trạch -> Pleiku -> Phú Mỹ
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

      // Photon particles flowing along the arc
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

    const count = 450; // Visual sampled representation of 22k nodes along main highways
    const positions = new Float32Array(count * 3);

    for (let i = 0; i < count; i++) {
      // Linear interpolation along Vietnam's highway spine with slight scatter
      const t = i / count;
      const lat = 8.8 + t * (21.5 - 8.8);
      // S-curve approximation for longitude
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

  // Animation Loop
  function animate() {
    if (!isVisible) return;
    animFrameId = requestAnimationFrame(animate);

    // Update Controls
    if (controls) controls.update();

    // Animate photon particles along 500kV arcs
    arcParticles.forEach((p) => {
      p.progress += p.speed;
      if (p.progress > 1.0) p.progress = 0.0;
      const pos = p.curve.getPoint(p.progress);
      p.mesh.position.copy(pos);
    });

    // Gentle rotation of pillar halo rings
    hubsGroup.children.forEach((pillar) => {
      if (pillar.children[0]) {
        pillar.children[0].rotation.z += 0.02;
      }
    });

    renderer.render(scene, camera);
  }

  // Pointer & Raycasting Handlers
  function onPointerMove(e) {
    const rect = canvasEl.getBoundingClientRect();
    mouse.x = ((e.clientX - rect.left) / rect.width) * 2 - 1;
    mouse.y = -((e.clientY - rect.top) / rect.height) * 2 + 1;

    raycaster.setFromCamera(mouse, camera);
    const intersects = raycaster.intersectObjects(interactiveObjects);

    if (intersects.length > 0) {
      const hub = intersects[0].object.userData;
      showTooltip(e.clientX, e.clientY, hub);
      canvasEl.style.cursor = 'pointer';
    } else {
      hideTooltip();
      canvasEl.style.cursor = 'grab';
    }
  }

  function onPointerDown() {
    canvasEl.style.cursor = 'grabbing';
  }

  function showTooltip(clientX, clientY, hub) {
    if (!tooltipEl) return;
    tooltipEl.innerHTML = `
      <div class="font-mono text-[9px] uppercase font-bold text-teal-600 dark:text-teal-400">
        ${hub.category.toUpperCase()} HUB &middot; ${hub.mw.toLocaleString()} MW
      </div>
      <div class="text-xs font-bold text-slate-900 dark:text-slate-100 mt-0.5">
        ${hub.name}
      </div>
      <div class="text-[11px] text-slate-500 dark:text-slate-400 mt-1 leading-snug">
        ${hub.desc}
      </div>
      <div class="mt-1.5 pt-1 border-t border-slate-100 dark:border-slate-800 font-mono text-[10px] text-slate-400 flex justify-between">
        <span>Coords: ${hub.lat.toFixed(2)}°N, ${hub.lng.toFixed(2)}°E</span>
        <span class="text-emerald-600 font-semibold">Live Monitored</span>
      </div>
    `;
    tooltipEl.style.display = 'block';

    const rect = containerEl.getBoundingClientRect();
    const x = clientX - rect.left + 15;
    const y = clientY - rect.top - 20;

    tooltipEl.style.left = `${Math.min(x, rect.width - 240)}px`;
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
    buildSupergridTransmissionArcs(p);
    buildEvCorridorCloud(p);
  }

  // Public API
  const RVN_ENERGY_3D = {
    init: async function(containerId = 'energy3dContainer', canvasId = 'energy3dCanvas', tooltipId = 'energy3dTooltip') {
      containerEl = document.getElementById(containerId);
      canvasEl = document.getElementById(canvasId);
      tooltipEl = document.getElementById(tooltipId);

      if (!containerEl || !canvasEl) {
        console.warn('[RVN_3D] Container or Canvas element not found.');
        return false;
      }

      await loadThreeLibraries();
      initScene();

      // Intersection Observer for zero render waste
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

    resetView: function() {
      this.setCameraPreset('national');
    }
  };

  window.RVN_ENERGY_3D = RVN_ENERGY_3D;
})(window);
