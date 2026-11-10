// Institutional Three.js Procedural PBR Models for DC36-T3 Hyperscale Datacenter
// High-Fidelity Architectural & MEP BIM LOD 400 Digital Twin

(function() {
    window.DC36_MODELS = {};

    // Common PBR Materials Registry
    const M = {
        // Site & Terrain
        ground: new THREE.MeshStandardMaterial({ color: 0x222629, roughness: 0.95, metalness: 0.05 }),
        asphalt: new THREE.MeshStandardMaterial({ color: 0x1b1e22, roughness: 0.85, metalness: 0.1 }),
        roadMarking: new THREE.MeshBasicMaterial({ color: 0xf5f5f5 }),
        grass: new THREE.MeshStandardMaterial({ color: 0x2d4a2d, roughness: 0.9, metalness: 0.0 }),
        gravel: new THREE.MeshStandardMaterial({ color: 0x4a4d4e, roughness: 0.95, metalness: 0.1 }),
        dirt: new THREE.MeshStandardMaterial({ color: 0x4a3b2c, roughness: 0.98, metalness: 0.0 }),
        fencePost: new THREE.MeshStandardMaterial({ color: 0x555c63, roughness: 0.5, metalness: 0.8 }),
        fenceWire: new THREE.MeshStandardMaterial({ color: 0x777e85, wireframe: true }),
        
        // Concrete & Structural
        concretePiles: new THREE.MeshStandardMaterial({ color: 0x7b8188, roughness: 0.9, metalness: 0.1 }),
        rebar: new THREE.MeshStandardMaterial({ color: 0x8b4513, roughness: 0.7, metalness: 0.6 }),
        concreteSlab: new THREE.MeshStandardMaterial({ color: 0x848a90, roughness: 0.75, metalness: 0.15 }),
        concreteCured: new THREE.MeshStandardMaterial({ color: 0x9ba2a8, roughness: 0.6, metalness: 0.1 }),
        columns: new THREE.MeshStandardMaterial({ color: 0x787f86, roughness: 0.7, metalness: 0.15 }),
        steelTruss: new THREE.MeshStandardMaterial({ color: 0x3d444d, roughness: 0.4, metalness: 0.85 }),
        steelGantry: new THREE.MeshStandardMaterial({ color: 0xffaa00, roughness: 0.4, metalness: 0.7 }),
        
        // Envelope & Architecture
        facadeDark: new THREE.MeshStandardMaterial({ color: 0x1e2227, roughness: 0.4, metalness: 0.6 }),
        facadeLight: new THREE.MeshStandardMaterial({ color: 0x4a525d, roughness: 0.5, metalness: 0.4 }),
        facadeAccent: new THREE.MeshStandardMaterial({ color: 0x0088ff, roughness: 0.3, metalness: 0.5 }),
        roofTPO: new THREE.MeshStandardMaterial({ color: 0xdde2e6, roughness: 0.6, metalness: 0.1 }),
        glass: new THREE.MeshPhysicalMaterial({ color: 0x113355, transmission: 0.8, opacity: 0.6, transparent: true, roughness: 0.1, ior: 1.5 }),
        glassHAC: new THREE.MeshPhysicalMaterial({ color: 0x00aaff, transmission: 0.85, opacity: 0.45, transparent: true, roughness: 0.1 }),
        louvers: new THREE.MeshStandardMaterial({ color: 0x2b3038, roughness: 0.5, metalness: 0.8 }),
        doors: new THREE.MeshStandardMaterial({ color: 0x374151, roughness: 0.6, metalness: 0.5 }),
        
        // MEP Electrical
        transformerTank: new THREE.MeshStandardMaterial({ color: 0x3a483a, roughness: 0.4, metalness: 0.7 }),
        copperBus: new THREE.MeshStandardMaterial({ color: 0xb87333, roughness: 0.3, metalness: 0.9 }),
        bushingPorcelain: new THREE.MeshStandardMaterial({ color: 0x6e3c23, roughness: 0.2, metalness: 0.1 }),
        switchgear: new THREE.MeshStandardMaterial({ color: 0x2f3640, roughness: 0.4, metalness: 0.6 }),
        generatorBody: new THREE.MeshStandardMaterial({ color: 0xc87d28, roughness: 0.4, metalness: 0.6 }),
        exhaustStack: new THREE.MeshStandardMaterial({ color: 0x8a9096, roughness: 0.3, metalness: 0.85 }),
        fuelTank: new THREE.MeshStandardMaterial({ color: 0x808080, roughness: 0.4, metalness: 0.7 }),
        upsCabinet: new THREE.MeshStandardMaterial({ color: 0x1f242d, roughness: 0.4, metalness: 0.6 }),
        batteryCabinet: new THREE.MeshStandardMaterial({ color: 0x232931, roughness: 0.3, metalness: 0.7 }),
        
        // MEP Mechanical
        chillerBlue: new THREE.MeshStandardMaterial({ color: 0x0055aa, roughness: 0.35, metalness: 0.7 }),
        pumpYellow: new THREE.MeshStandardMaterial({ color: 0xcc8800, roughness: 0.4, metalness: 0.6 }),
        chwSupplyPipe: new THREE.MeshStandardMaterial({ color: 0x0077cc, roughness: 0.3, metalness: 0.75 }),
        chwReturnPipe: new THREE.MeshStandardMaterial({ color: 0x009988, roughness: 0.3, metalness: 0.75 }),
        coolingTowerCasing: new THREE.MeshStandardMaterial({ color: 0x8c96a0, roughness: 0.5, metalness: 0.4 }),
        coolingTowerFan: new THREE.MeshStandardMaterial({ color: 0x1a1e22, roughness: 0.4, metalness: 0.8 }),
        crahUnit: new THREE.MeshStandardMaterial({ color: 0x39424e, roughness: 0.4, metalness: 0.5 }),
        raisedFloor: new THREE.MeshStandardMaterial({ color: 0x5a636d, roughness: 0.6, metalness: 0.3 }),
        perforatedTile: new THREE.MeshStandardMaterial({ color: 0x3d444d, roughness: 0.7, metalness: 0.4, wireframe: false }),
        
        // IT White Space
        serverRack: new THREE.MeshStandardMaterial({ color: 0x111317, roughness: 0.4, metalness: 0.8 }),
        serverRackGlow: new THREE.MeshStandardMaterial({ color: 0x00e5ff, emissive: 0x00e5ff, emissiveIntensity: 0.8 }),
        serverRackAlert: new THREE.MeshStandardMaterial({ color: 0xff9900, emissive: 0xff9900, emissiveIntensity: 0.8 }),
        buswayTrunk: new THREE.MeshStandardMaterial({ color: 0xd97706, roughness: 0.4, metalness: 0.7 }),
        
        // Load Banks & Testing
        loadBank: new THREE.MeshStandardMaterial({ color: 0xd32f2f, roughness: 0.4, metalness: 0.6 }),
        cautionStripe: new THREE.MeshStandardMaterial({ color: 0xf59e0b, roughness: 0.5, metalness: 0.2 }),
        cableOrange: new THREE.MeshStandardMaterial({ color: 0xff6600, roughness: 0.5, metalness: 0.1 }),

        // Construction Equipment
        craneYellow: new THREE.MeshStandardMaterial({ color: 0xf59e0b, roughness: 0.35, metalness: 0.7 }),
        craneTreads: new THREE.MeshStandardMaterial({ color: 0x202020, roughness: 0.9, metalness: 0.3 })
    };

    window.DC36_MATERIALS = M;

    // 1. Build Base Campus Terrain & Perimeter
    function createCampusSite() {
        const group = new THREE.Group();
        group.name = "CampusSite";

        // Outer Ground
        const groundGeo = new THREE.PlaneGeometry(260, 200);
        const groundMesh = new THREE.Mesh(groundGeo, M.ground);
        groundMesh.rotation.x = -Math.PI / 2;
        groundMesh.receiveShadow = true;
        group.add(groundMesh);

        // Asphalt Campus Pad
        const campusGeo = new THREE.PlaneGeometry(210, 150);
        const campusMesh = new THREE.Mesh(campusGeo, M.asphalt);
        campusMesh.rotation.x = -Math.PI / 2;
        campusMesh.position.y = 0.05;
        campusMesh.receiveShadow = true;
        group.add(campusMesh);

        // Landscaping Green Strips (North and East perimeter)
        const lawn1 = new THREE.Mesh(new THREE.PlaneGeometry(200, 10), M.grass);
        lawn1.rotation.x = -Math.PI / 2;
        lawn1.position.set(0, 0.08, -70);
        lawn1.receiveShadow = true;
        group.add(lawn1);

        const lawn2 = new THREE.Mesh(new THREE.PlaneGeometry(10, 130), M.grass);
        lawn2.rotation.x = -Math.PI / 2;
        lawn2.position.set(98, 0.08, 0);
        lawn2.receiveShadow = true;
        group.add(lawn2);

        // Roadway Markings
        const roadLineGeo = new THREE.PlaneGeometry(190, 0.4);
        const roadLine = new THREE.Mesh(roadLineGeo, M.roadMarking);
        roadLine.rotation.x = -Math.PI / 2;
        roadLine.position.set(0, 0.09, 65);
        group.add(roadLine);

        // Security Perimeter Fence with Concrete Curbs
        const fenceGroup = new THREE.Group();
        const fencePoints = [
            [-102, -72], [102, -72], [102, 72], [-102, 72]
        ];
        for (let i = 0; i < 4; i++) {
            const p1 = fencePoints[i];
            const p2 = fencePoints[(i + 1) % 4];
            const len = Math.hypot(p2[0] - p1[0], p2[1] - p1[1]);
            const angle = Math.atan2(p2[1] - p1[1], p2[0] - p1[0]);
            
            // Wall / curb
            const curbGeo = new THREE.BoxGeometry(len, 0.6, 0.4);
            const curb = new THREE.Mesh(curbGeo, M.concreteSlab);
            curb.position.set((p1[0] + p2[0]) / 2, 0.3, (p1[1] + p2[1]) / 2);
            curb.rotation.y = -angle;
            fenceGroup.add(curb);

            // Fence posts & wire mesh
            const postCount = Math.floor(len / 6);
            for (let j = 0; j <= postCount; j++) {
                const t = j / postCount;
                const px = p1[0] + (p2[0] - p1[0]) * t;
                const pz = p1[1] + (p2[1] - p1[1]) * t;
                const post = new THREE.Mesh(new THREE.CylinderGeometry(0.08, 0.08, 3, 8), M.fencePost);
                post.position.set(px, 1.8, pz);
                fenceGroup.add(post);
            }
        }
        group.add(fenceGroup);

        // Guard House & Security Boom Barrier
        const guardHouse = new THREE.Group();
        guardHouse.position.set(-85, 0, 65);
        const ghBase = new THREE.Mesh(new THREE.BoxGeometry(6, 3.2, 4), M.facadeDark);
        ghBase.position.y = 1.6;
        ghBase.castShadow = true;
        guardHouse.add(ghBase);
        
        const ghGlass = new THREE.Mesh(new THREE.BoxGeometry(5.8, 1.4, 3.8), M.glass);
        ghGlass.position.y = 2.0;
        guardHouse.add(ghGlass);

        const barrierArm = new THREE.Mesh(new THREE.BoxGeometry(6, 0.15, 0.15), M.cautionStripe);
        barrierArm.position.set(5, 1.0, 0);
        guardHouse.add(barrierArm);

        group.add(guardHouse);

        return group;
    }

    // 2. Phase 1: Site Clearing, Bulk Excavation & Piling
    function createGroundworkAndPiling() {
        const group = new THREE.Group();
        group.name = "GroundworkAndPiling";
        group.userData = { phase: 1, tag: "piling", wbs: "4.1-SUB" };

        // Excavation Pit (Depression beneath main building footprint: 90m x 60m x 2.5m)
        const pitBorderGeo = new THREE.BoxGeometry(92, 0.8, 62);
        const pitBorder = new THREE.Mesh(pitBorderGeo, M.dirt);
        pitBorder.position.set(5, 0.4, 0);
        group.add(pitBorder);

        const pitFloorGeo = new THREE.PlaneGeometry(90, 60);
        const pitFloor = new THREE.Mesh(pitFloorGeo, M.dirt);
        pitFloor.rotation.x = -Math.PI / 2;
        pitFloor.position.set(5, 0.1, 0);
        group.add(pitFloor);

        // Bored Concrete Piling Grid (600 piles represented by 12x8 clusters with rebar cage tops)
        const pilesGroup = new THREE.Group();
        pilesGroup.name = "PilesGrid";

        const pileGeo = new THREE.CylinderGeometry(0.35, 0.35, 3.5, 12);
        const rebarGeo = new THREE.CylinderGeometry(0.28, 0.28, 1.2, 8);

        const cols = 16;
        const rows = 10;
        const startX = -36 + 5;
        const startZ = -24;
        const spacingX = 72 / (cols - 1);
        const spacingZ = 48 / (rows - 1);

        for (let c = 0; c < cols; c++) {
            for (let r = 0; r < rows; r++) {
                const px = startX + c * spacingX;
                const pz = startZ + r * spacingZ;

                const pile = new THREE.Mesh(pileGeo, M.concretePiles);
                pile.position.set(px, 1.2, pz);
                pile.castShadow = true;
                pilesGroup.add(pile);

                const cage = new THREE.Mesh(rebarGeo, M.rebar);
                cage.position.set(px, 3.2, pz);
                pilesGroup.add(cage);
            }
        }
        group.add(pilesGroup);

        // Mobile Hydraulic Piling Rig
        const rigGroup = new THREE.Group();
        rigGroup.position.set(-20, 0, 15);
        
        // Treads
        const tread1 = new THREE.Mesh(new THREE.BoxGeometry(4.5, 1.2, 1.0), M.craneTreads);
        tread1.position.set(0, 0.6, -1.5);
        const tread2 = tread1.clone();
        tread2.position.set(0, 0.6, 1.5);
        rigGroup.add(tread1, tread2);

        // Cabin
        const cab = new THREE.Mesh(new THREE.BoxGeometry(3.5, 2.2, 2.6), M.craneYellow);
        cab.position.set(0, 2.0, 0);
        cab.castShadow = true;
        rigGroup.add(cab);

        // Vertical Drilling Mast & Auger
        const mast = new THREE.Mesh(new THREE.BoxGeometry(0.8, 16, 0.8), M.steelTruss);
        mast.position.set(2.5, 9.0, 0);
        rigGroup.add(mast);

        const auger = new THREE.Mesh(new THREE.CylinderGeometry(0.3, 0.3, 10, 8), M.exhaustStack);
        auger.position.set(2.5, 6.0, 0);
        rigGroup.add(auger);

        group.add(rigGroup);

        return group;
    }

    // 3. Phase 2: Raft Foundation Slab & Heavy Equipment Plinths
    function createFoundationAndPlinths() {
        const group = new THREE.Group();
        group.name = "FoundationAndPlinths";
        group.userData = { phase: 2, tag: "raft_slab", wbs: "4.1-SUB" };

        // Main Deep Foundation Raft Slab (90m x 60m x 1.8m thick)
        const raftGeo = new THREE.BoxGeometry(90, 1.8, 60);
        const raft = new THREE.Mesh(raftGeo, M.concreteCured);
        raft.position.set(5, 0.9, 0);
        raft.receiveShadow = true;
        raft.castShadow = true;
        group.add(raft);

        // Copper Ground Earthing Grid lines around slab perimeter
        const earthGrid = new THREE.Mesh(new THREE.BoxGeometry(92, 0.1, 62), M.copperBus);
        earthGrid.position.set(5, 0.05, 0);
        group.add(earthGrid);

        // External Plinths for 16 Diesel Generators (West Yard: 8x2 pairs)
        const genPlinthGroup = new THREE.Group();
        genPlinthGroup.name = "GeneratorPlinths";
        for (let i = 0; i < 8; i++) {
            const z = -28 + i * 8;
            const plinthA = new THREE.Mesh(new THREE.BoxGeometry(7.5, 0.6, 3.2), M.concreteSlab);
            plinthA.position.set(-60, 0.3, z);
            plinthA.castShadow = true;
            plinthA.receiveShadow = true;

            const plinthB = new THREE.Mesh(new THREE.BoxGeometry(7.5, 0.6, 3.2), M.concreteSlab);
            plinthB.position.set(-72, 0.3, z);
            plinthB.castShadow = true;
            plinthB.receiveShadow = true;

            genPlinthGroup.add(plinthA, plinthB);
        }
        group.add(genPlinthGroup);

        // External Plinths for 110kV/22kV Substation Transformers (South Yard)
        const subPlinthA = new THREE.Mesh(new THREE.BoxGeometry(10, 0.8, 8), M.concreteSlab);
        subPlinthA.position.set(-20, 0.4, 48);
        subPlinthA.castShadow = true;

        const subPlinthB = new THREE.Mesh(new THREE.BoxGeometry(10, 0.8, 8), M.concreteSlab);
        subPlinthB.position.set(10, 0.4, 48);
        subPlinthB.castShadow = true;

        group.add(subPlinthA, subPlinthB);

        return group;
    }

    // 4. Phase 3: Concrete Superstructure (Columns, L1 & L2 Slabs, Shear Walls)
    function createSuperstructure() {
        const group = new THREE.Group();
        group.name = "Superstructure";
        group.userData = { phase: 3, tag: "superstructure", wbs: "4.2-SUPER" };

        const colGrid = new THREE.Group();
        colGrid.name = "ColumnsGrid";

        // Heavy Columns (0.9m x 0.9m) spanning Ground to L1 (h = 5m) and L1 to L2 (h = 5m), total 10m
        const colGeo = new THREE.BoxGeometry(0.9, 10.5, 0.9);
        const cols = 9;
        const rows = 7;
        const startX = -38 + 5;
        const startZ = -26;
        const stepX = 76 / (cols - 1);
        const stepZ = 52 / (rows - 1);

        for (let c = 0; c < cols; c++) {
            for (let r = 0; r < rows; r++) {
                const cx = startX + c * stepX;
                const cz = startZ + r * stepZ;
                const col = new THREE.Mesh(colGeo, M.columns);
                col.position.set(cx, 1.8 + 10.5 / 2, cz);
                col.castShadow = true;
                col.receiveShadow = true;
                colGrid.add(col);
            }
        }
        group.add(colGrid);

        // Concrete Shear Walls (Central seismic cores & riser shafts)
        const wallGeo = new THREE.BoxGeometry(1.2, 11, 14);
        const wallA = new THREE.Mesh(wallGeo, M.columns);
        wallA.position.set(-15 + 5, 7.3, 0);
        wallA.castShadow = true;
        
        const wallB = new THREE.Mesh(wallGeo, M.columns);
        wallB.position.set(15 + 5, 7.3, 0);
        wallB.castShadow = true;

        group.add(wallA, wallB);

        // Level 1 Suspended Slab (18 kN/m2 design load, h = 5.5m)
        const slabL1Geo = new THREE.BoxGeometry(89, 0.6, 59);
        const slabL1 = new THREE.Mesh(slabL1Geo, M.concreteSlab);
        slabL1.position.set(5, 7.0, 0);
        slabL1.castShadow = true;
        slabL1.receiveShadow = true;
        slabL1.name = "SlabL1";
        group.add(slabL1);

        // Level 2 Suspended Slab (Data Hall Floor, h = 11.5m)
        const slabL2Geo = new THREE.BoxGeometry(89, 0.6, 59);
        const slabL2 = new THREE.Mesh(slabL2Geo, M.concreteSlab);
        slabL2.position.set(5, 12.3, 0);
        slabL2.castShadow = true;
        slabL2.receiveShadow = true;
        slabL2.name = "SlabL2";
        group.add(slabL2);

        return group;
    }

    // 5. Phase 4: Structural Steel Roof Trusses & Building Architectural Envelope
    function createRoofAndEnvelope() {
        const group = new THREE.Group();
        group.name = "RoofAndEnvelope";
        group.userData = { phase: 4, tag: "envelope", wbs: "4.3-ENVEL" };

        // Roof Structural Steel Trusses & Gantry
        const roofSteel = new THREE.Group();
        roofSteel.name = "RoofSteelStructure";
        for (let i = 0; i < 9; i++) {
            const x = -38 + 5 + i * (76 / 8);
            // Main truss beam across width (Z axis)
            const trussBeam = new THREE.Mesh(new THREE.BoxGeometry(0.5, 1.2, 59), M.steelTruss);
            trussBeam.position.set(x, 18.0, 0);
            trussBeam.castShadow = true;
            roofSteel.add(trussBeam);
        }
        group.add(roofSteel);

        // Rooftop Chiller Support Gantry (Elevated heavy steel platform: 50m x 20m)
        const gantryGeo = new THREE.BoxGeometry(54, 0.4, 22);
        const gantry = new THREE.Mesh(gantryGeo, M.steelGantry);
        gantry.position.set(5, 18.8, 0);
        gantry.castShadow = true;
        group.add(gantry);

        // High-Albedo White TPO Membrane Roof
        const roofSlabGeo = new THREE.BoxGeometry(90.5, 0.5, 60.5);
        const roof = new THREE.Mesh(roofSlabGeo, M.roofTPO);
        roof.position.set(5, 18.5, 0);
        roof.receiveShadow = true;
        roof.name = "RoofMembrane";
        group.add(roof);

        // Precast Insulated Architectural Facade Panels (Modular sandwich panels)
        const facadeGroup = new THREE.Group();
        facadeGroup.name = "BuildingFacade";

        // South Wall (Length = 90.6m, Height = 17m)
        const southWallGeo = new THREE.BoxGeometry(90.6, 17, 0.4);
        const southWall = new THREE.Mesh(southWallGeo, M.facadeDark);
        southWall.position.set(5, 10.3, 30.2);
        southWall.castShadow = true;
        facadeGroup.add(southWall);

        // North Wall
        const northWallGeo = new THREE.BoxGeometry(90.6, 17, 0.4);
        const northWall = new THREE.Mesh(northWallGeo, M.facadeDark);
        northWall.position.set(5, 10.3, -30.2);
        northWall.castShadow = true;
        facadeGroup.add(northWall);

        // West Wall (Generators side)
        const westWallGeo = new THREE.BoxGeometry(0.4, 17, 60.4);
        const westWall = new THREE.Mesh(westWallGeo, M.facadeLight);
        westWall.position.set(-40.2, 10.3, 0);
        westWall.castShadow = true;
        facadeGroup.add(westWall);

        // East Wall (Main entrance & offices)
        const eastWallGeo = new THREE.BoxGeometry(0.4, 17, 60.4);
        const eastWall = new THREE.Mesh(eastWallGeo, M.facadeLight);
        eastWall.position.set(50.2, 10.3, 0);
        eastWall.castShadow = true;
        facadeGroup.add(eastWall);

        // Architectural Accents: Blue LED band and Datacenter Signage
        const accentBand = new THREE.Mesh(new THREE.BoxGeometry(91, 0.4, 61), M.facadeAccent);
        accentBand.position.set(5, 18.6, 0);
        facadeGroup.add(accentBand);

        // Exterior Industrial Air Intake Louvers (West side ground floor for generators)
        for (let l = 0; l < 8; l++) {
            const louver = new THREE.Mesh(new THREE.BoxGeometry(0.5, 3.5, 5), M.louvers);
            louver.position.set(-40.3, 3.5, -24 + l * 7);
            facadeGroup.add(louver);
        }

        // Blast-Resistant Double Access Doors
        const mainDoor = new THREE.Mesh(new THREE.BoxGeometry(0.5, 4.0, 5.0), M.doors);
        mainDoor.position.set(50.3, 3.8, 0);
        facadeGroup.add(mainDoor);

        group.add(facadeGroup);

        return group;
    }

    // 6. Phase 5: Heavy MEP (110kV/22kV Substation, 16 Gensets, 6 Chillers & Cooling Towers)
    function createHeavyMEP() {
        const group = new THREE.Group();
        group.name = "HeavyMEP";
        group.userData = { phase: 5, tag: "heavy_mep", wbs: "5.0-MEP" };

        // --- A. 110kV/22kV High-Voltage Substation ---
        const subGroup = new THREE.Group();
        subGroup.name = "MainSubstation";
        subGroup.position.set(0, 0, 48);

        // 2x 45MVA Power Transformers
        [-20, 10].forEach((tx, idx) => {
            const tr = new THREE.Group();
            tr.position.set(tx, 0.8, 0);
            tr.name = `Transformer_${idx + 1}_45MVA`;

            // Main oil tank
            const tank = new THREE.Mesh(new THREE.BoxGeometry(5.2, 4.2, 4.0), M.transformerTank);
            tank.position.y = 2.1;
            tank.castShadow = true;
            tr.add(tank);

            // Radiator Cooling Fins (Flanks)
            for (let f = -1.6; f <= 1.6; f += 0.8) {
                const fin = new THREE.Mesh(new THREE.BoxGeometry(5.4, 3.2, 0.15), M.transformerTank);
                fin.position.set(0, 2.1, f);
                tr.add(fin);
            }

            // High Voltage Bushings (3 ceramic cones on top)
            for (let b = -1.2; b <= 1.2; b += 1.2) {
                const bushing = new THREE.Mesh(new THREE.CylinderGeometry(0.12, 0.25, 2.0, 8), M.bushingPorcelain);
                bushing.position.set(b, 5.2, 0);
                tr.add(bushing);
            }

            // Cylindrical Oil Conservator Tank on Top
            const cons = new THREE.Mesh(new THREE.CylinderGeometry(0.6, 0.6, 3.8, 12), M.transformerTank);
            cons.rotation.z = Math.PI / 2;
            cons.position.set(0, 5.0, 1.5);
            tr.add(cons);

            subGroup.add(tr);
        });

        // Substation 110kV Gantry Tower (Lattice steel structure)
        const gantryTower = new THREE.Group();
        gantryTower.position.set(-5, 0, 8);
        const postA = new THREE.Mesh(new THREE.CylinderGeometry(0.2, 0.3, 12, 8), M.steelTruss);
        postA.position.set(-18, 6, 0);
        const postB = new THREE.Mesh(new THREE.CylinderGeometry(0.2, 0.3, 12, 8), M.steelTruss);
        postB.position.set(18, 6, 0);
        const crossArm = new THREE.Mesh(new THREE.BoxGeometry(40, 0.6, 0.6), M.steelTruss);
        crossArm.position.set(0, 11, 0);
        gantryTower.add(postA, postB, crossArm);
        subGroup.add(gantryTower);

        group.add(subGroup);

        // --- B. Standby Emergency Diesel Generator Farm (16 units x 2.5MVA) ---
        const genGroup = new THREE.Group();
        genGroup.name = "GeneratorFarm";
        genGroup.position.set(-66, 0, 0);

        for (let i = 0; i < 8; i++) {
            const z = -28 + i * 8;
            [-6, 6].forEach((xOff, bankIdx) => {
                const genset = new THREE.Group();
                genset.position.set(xOff, 0.6, z);
                genset.name = `Genset_${i * 2 + bankIdx + 1}_2.5MVA`;

                // Container Enclosure
                const container = new THREE.Mesh(new THREE.BoxGeometry(6.5, 2.8, 2.6), M.generatorBody);
                container.position.y = 1.4;
                container.castShadow = true;
                genset.add(container);

                // Acoustic Intake/Discharge Louvers
                const louverEnd = new THREE.Mesh(new THREE.BoxGeometry(0.15, 2.2, 2.3), M.louvers);
                louverEnd.position.set(3.3, 1.4, 0);
                genset.add(louverEnd);

                // Vertical Stainless Steel Exhaust Stack with Silencer
                const stack = new THREE.Mesh(new THREE.CylinderGeometry(0.25, 0.25, 6.0, 10), M.exhaustStack);
                stack.position.set(-2.0, 4.4, 0);
                stack.castShadow = true;
                genset.add(stack);

                // Vibration Spring Isolators beneath container
                for (let sx of [-2.5, 2.5]) {
                    for (let sz of [-1.0, 1.0]) {
                        const spring = new THREE.Mesh(new THREE.CylinderGeometry(0.15, 0.15, 0.4, 8), M.steelTruss);
                        spring.position.set(sx, 0.2, sz);
                        genset.add(spring);
                    }
                }

                genGroup.add(genset);
            });
        }

        // Underground Bulk Fuel Storage Skid & Pumps (3x 80m3 tanks)
        const fuelSkid = new THREE.Group();
        fuelSkid.position.set(0, 0, 36);
        for (let t = -8; t <= 8; t += 8) {
            const tank = new THREE.Mesh(new THREE.CylinderGeometry(1.6, 1.6, 9.0, 16), M.fuelTank);
            tank.rotation.z = Math.PI / 2;
            tank.position.set(0, 1.8, t);
            fuelSkid.add(tank);
        }
        genGroup.add(fuelSkid);
        group.add(genGroup);

        // --- C. Central Chilled Water Plant (6x 1200 RT Chillers on L1 & Rooftop Cooling Towers) ---
        const chwPlant = new THREE.Group();
        chwPlant.name = "ChilledWaterPlant";

        // 6 Centrifugal Chillers (Located inside Level 1 Mechanical Bay: X: 5m, Z: -15m to 15m)
        const chillersGroup = new THREE.Group();
        chillersGroup.name = "CentrifugalChillers";
        for (let i = 0; i < 6; i++) {
            const ch = new THREE.Group();
            const cz = -20 + i * 8;
            ch.position.set(-18 + 5, 7.3, cz);
            ch.name = `Chiller_${i + 1}_1200RT`;

            // Evaporator Lower Shell
            const evap = new THREE.Mesh(new THREE.CylinderGeometry(0.9, 0.9, 6.0, 16), M.chillerBlue);
            evap.rotation.z = Math.PI / 2;
            evap.position.y = 1.0;
            evap.castShadow = true;
            ch.add(evap);

            // Condenser Upper Shell
            const cond = new THREE.Mesh(new THREE.CylinderGeometry(0.8, 0.8, 5.8, 16), M.chillerBlue);
            cond.rotation.z = Math.PI / 2;
            cond.position.set(0, 2.3, 0.4);
            cond.castShadow = true;
            ch.add(cond);

            // Centrifugal Compressor & Motor Housing
            const comp = new THREE.Mesh(new THREE.CylinderGeometry(0.65, 0.65, 2.0, 12), M.pumpYellow);
            comp.position.set(0, 3.4, 0);
            ch.add(comp);

            chillersGroup.add(ch);
        }
        chwPlant.add(chillersGroup);

        // Dual Header Chilled Water Carbon Steel Piping (DN500 Supply & Return Loops)
        const headerSupply = new THREE.Mesh(new THREE.CylinderGeometry(0.3, 0.3, 48, 12), M.chwSupplyPipe);
        headerSupply.position.set(-23 + 5, 10.5, 0);
        chwPlant.add(headerSupply);

        const headerReturn = new THREE.Mesh(new THREE.CylinderGeometry(0.3, 0.3, 48, 12), M.chwReturnPipe);
        headerReturn.position.set(-22 + 5, 10.5, 0);
        chwPlant.add(headerReturn);

        // 6 Rooftop Induced-Draft Cooling Towers (Mounted on steel gantry platform, Y = 19.0m)
        const coolingTowers = new THREE.Group();
        coolingTowers.name = "RooftopCoolingTowers";
        window.DC36_COOLING_FANS = [];

        for (let ct = 0; ct < 6; ct++) {
            const tower = new THREE.Group();
            const tz = -18 + ct * 7.2;
            tower.position.set(5, 19.0, tz);
            tower.name = `CoolingTower_${ct + 1}`;

            // Casing
            const casing = new THREE.Mesh(new THREE.BoxGeometry(5.0, 4.0, 5.0), M.coolingTowerCasing);
            casing.position.y = 2.0;
            casing.castShadow = true;
            tower.add(casing);

            // Air intake louver base
            const louverBase = new THREE.Mesh(new THREE.BoxGeometry(5.1, 1.2, 5.1), M.louvers);
            louverBase.position.y = 0.6;
            tower.add(louverBase);

            // Fan Cowl Cylinder on Top
            const cowl = new THREE.Mesh(new THREE.CylinderGeometry(1.8, 1.9, 1.2, 16), M.coolingTowerFan);
            cowl.position.y = 4.6;
            tower.add(cowl);

            // 4-blade Rotating Impeller
            const fanHub = new THREE.Group();
            fanHub.position.y = 4.6;
            for (let b = 0; b < 4; b++) {
                const blade = new THREE.Mesh(new THREE.BoxGeometry(1.6, 0.05, 0.3), M.coolingTowerFan);
                blade.rotation.y = (b * Math.PI) / 2;
                blade.position.x = Math.cos((b * Math.PI) / 2) * 0.8;
                blade.position.z = Math.sin((b * Math.PI) / 2) * 0.8;
                fanHub.add(blade);
            }
            tower.add(fanHub);
            window.DC36_COOLING_FANS.push(fanHub);

            coolingTowers.add(tower);
        }
        chwPlant.add(coolingTowers);
        group.add(chwPlant);

        return group;
    }

    // 7. Phase 6: White Space Data Halls Fit-Out (Halls 1 to 4, Raised Floor, Busways, CRAH & Racks)
    function createWhiteSpaceFitOut() {
        const group = new THREE.Group();
        group.name = "WhiteSpaceFitOut";
        group.userData = { phase: 6, tag: "white_space", wbs: "5.4-WS" };

        window.DC36_SERVER_LEDS = [];

        // Data Hall Level Floor Y = 12.3m
        // 800mm Anti-Static Raised Access Floor
        const floorGeo = new THREE.BoxGeometry(78, 0.1, 48);
        const raisedFloor = new THREE.Mesh(floorGeo, M.raisedFloor);
        raisedFloor.position.set(5, 13.1, 0);
        raisedFloor.receiveShadow = true;
        group.add(raisedFloor);

        // 4 Symmetrical Data Halls: Quad 1 to 4
        // Hall 1 (NW), Hall 2 (NE), Hall 3 (SW), Hall 4 (SE)
        const quadCenters = [
            { x: -16 + 5, z: -14, name: "DataHall_1" },
            { x: 16 + 5, z: -14, name: "DataHall_2" },
            { x: -16 + 5, z: 14, name: "DataHall_3" },
            { x: 16 + 5, z: 14, name: "DataHall_4" }
        ];

        quadCenters.forEach(quad => {
            const hallGroup = new THREE.Group();
            hallGroup.position.set(quad.x, 13.15, quad.z);
            hallGroup.name = quad.name;

            // 6 Rows of Server Racks per Data Hall, paired into 3 Hot Aisle Containment Pods
            const rowSpacingZ = 3.6;
            for (let pod = 0; pod < 3; pod++) {
                const podCenterZ = -7.2 + pod * 7.2;

                // Hot Aisle Containment Roof & End Glass Doors
                const hacRoof = new THREE.Mesh(new THREE.BoxGeometry(20, 0.08, 1.6), M.glassHAC);
                hacRoof.position.set(0, 2.5, podCenterZ);
                hallGroup.add(hacRoof);

                const doorWest = new THREE.Mesh(new THREE.BoxGeometry(0.1, 2.4, 1.6), M.glassHAC);
                doorWest.position.set(-10, 1.2, podCenterZ);
                const doorEast = new THREE.Mesh(new THREE.BoxGeometry(0.1, 2.4, 1.6), M.glassHAC);
                doorEast.position.set(10, 1.2, podCenterZ);
                hallGroup.add(doorWest, doorEast);

                // Overhead 415V Redundant Track Busways (A & B Feeds)
                const buswayA = new THREE.Mesh(new THREE.BoxGeometry(22, 0.25, 0.25), M.buswayTrunk);
                buswayA.position.set(0, 3.2, podCenterZ - 0.9);
                const buswayB = new THREE.Mesh(new THREE.BoxGeometry(22, 0.25, 0.25), M.buswayTrunk);
                buswayB.position.set(0, 3.2, podCenterZ + 0.9);
                hallGroup.add(buswayA, buswayB);

                // Two facing rows of 42U Server Racks (16 racks per row = 32 racks per pod)
                [-0.8, 0.8].forEach(zOffset => {
                    for (let r = 0; r < 14; r++) {
                        const rx = -8.5 + r * 1.3;
                        const rack = new THREE.Group();
                        rack.position.set(rx, 0, podCenterZ + zOffset);

                        // 42U Rack Body
                        const body = new THREE.Mesh(new THREE.BoxGeometry(0.8, 2.2, 1.0), M.serverRack);
                        body.position.y = 1.1;
                        body.castShadow = true;
                        rack.add(body);

                        // Front LED Activity Indicator strip
                        const led = new THREE.Mesh(new THREE.BoxGeometry(0.65, 0.08, 0.02), M.serverRackGlow.clone());
                        led.position.set(0, 1.8, zOffset > 0 ? -0.51 : 0.51);
                        rack.add(led);
                        window.DC36_SERVER_LEDS.push(led);

                        hallGroup.add(rack);
                    }
                });
            }

            // Perimeter CRAH Units (Computer Room Air Handlers with EC fans)
            for (let c = -9; c <= 9; c += 6) {
                // North and South perimeter walls of the hall
                const crahN = new THREE.Mesh(new THREE.BoxGeometry(2.4, 2.5, 1.0), M.crahUnit);
                crahN.position.set(c, 1.25, -11.5);
                crahN.castShadow = true;
                const crahS = new THREE.Mesh(new THREE.BoxGeometry(2.4, 2.5, 1.0), M.crahUnit);
                crahS.position.set(c, 1.25, 11.5);
                crahS.castShadow = true;
                hallGroup.add(crahN, crahS);
            }

            group.add(hallGroup);
        });

        // Modular Static UPS & Lithium-Ion Battery Rooms (Ground & L1 Electrical Rooms)
        const upsRoom = new THREE.Group();
        upsRoom.position.set(28 + 5, 7.3, 0);
        upsRoom.name = "UPS_Battery_Rooms";
        for (let u = -16; u <= 16; u += 4) {
            const ups = new THREE.Mesh(new THREE.BoxGeometry(1.6, 2.2, 1.2), M.upsCabinet);
            ups.position.set(0, 1.1, u);
            const batt = new THREE.Mesh(new THREE.BoxGeometry(1.6, 2.2, 1.2), M.batteryCabinet);
            batt.position.set(4, 1.1, u);
            upsRoom.add(ups, batt);
        }
        group.add(upsRoom);

        return group;
    }

    // 8. Phase 7: Testing & Commissioning 36MW Portable Load Banks
    function createCommissioningLoadBanks() {
        const group = new THREE.Group();
        group.name = "CommissioningLoadBanks";
        group.userData = { phase: 7, tag: "load_banks", wbs: "6.4-L5" };

        // 36MW Portable Resistive-Reactive Load Bank Trailers (Staged outside along East yard)
        const lbCount = 8;
        for (let i = 0; i < lbCount; i++) {
            const z = -25 + i * 7.2;
            const lb = new THREE.Group();
            lb.position.set(58, 0.4, z);
            lb.name = `LoadBank_${i + 1}_4.5MW`;

            // Mobile trailer chassis
            const chassis = new THREE.Mesh(new THREE.BoxGeometry(6.5, 0.6, 2.8), M.craneTreads);
            chassis.position.y = 0.3;
            lb.add(chassis);

            // Red Load Bank Enclosure with Exhaust Cowls
            const body = new THREE.Mesh(new THREE.BoxGeometry(5.8, 2.4, 2.6), M.loadBank);
            body.position.y = 1.8;
            body.castShadow = true;
            lb.add(body);

            // Heat Exhaust Vents
            const vent = new THREE.Mesh(new THREE.BoxGeometry(4.5, 0.4, 2.0), M.louvers);
            vent.position.y = 3.1;
            lb.add(vent);

            // Heavy Temporary Flexible Power Feeders (Orange cables running into building)
            const cable = new THREE.Mesh(new THREE.CylinderGeometry(0.12, 0.12, 8.0, 8), M.cableOrange);
            cable.rotation.z = Math.PI / 2;
            cable.position.set(-4.0, 0.3, 0);
            lb.add(cable);

            group.add(lb);
        }

        // Active Energization / IST Test Pulse Ring (Ground Projection)
        const ringGeo = new THREE.RingGeometry(48, 52, 32);
        const ringMat = new THREE.MeshBasicMaterial({ color: 0x00e5ff, side: THREE.DoubleSide, transparent: true, opacity: 0.35 });
        const ring = new THREE.Mesh(ringGeo, ringMat);
        ring.rotation.x = -Math.PI / 2;
        ring.position.set(5, 0.2, 0);
        ring.name = "IST_PulseRing";
        group.add(ring);

        return group;
    }

    // Master Model Generator: Assembles all evolutionary layers
    window.DC36_MODELS.buildDatacenterScene = function(scene) {
        const root = new THREE.Group();
        root.name = "DC36_DatacenterRoot";

        const site = createCampusSite();
        const p1 = createGroundworkAndPiling();
        const p2 = createFoundationAndPlinths();
        const p3 = createSuperstructure();
        const p4 = createRoofAndEnvelope();
        const p5 = createHeavyMEP();
        const p6 = createWhiteSpaceFitOut();
        const p7 = createCommissioningLoadBanks();

        root.add(site, p1, p2, p3, p4, p5, p6, p7);
        scene.add(root);

        return {
            root,
            site,
            p1_piling: p1,
            p2_foundation: p2,
            p3_superstructure: p3,
            p4_envelope: p4,
            p5_mep: p5,
            p6_whitespace: p6,
            p7_loadbanks: p7
        };
    };
})();
