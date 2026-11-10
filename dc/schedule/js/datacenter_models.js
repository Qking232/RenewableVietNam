// Institutional Three.js Procedural PBR Models for DC36-T3 Hyperscale Datacenter
// AAA Graphics Edition: High-Density Mechanical & Architectural BIM LOD 400 Assets

(function() {
    window.DC36_MODELS = {};

    let T = null; // Procedural Textures Registry

    function initMaterials() {
        if (!T) {
            T = window.DC36_TEXTURES.init();
        }

        return {
            // Site & Terrain
            ground: new THREE.MeshStandardMaterial({ color: 0x1f2327, roughness: 0.95, metalness: 0.05 }),
            asphalt: new THREE.MeshStandardMaterial({ color: 0x17191d, roughness: 0.88, metalness: 0.12 }),
            roadMarking: new THREE.MeshBasicMaterial({ color: 0xf1f5f9 }),
            grass: new THREE.MeshStandardMaterial({ color: 0x223822, roughness: 0.92, metalness: 0.0 }),
            fencePost: new THREE.MeshStandardMaterial({ color: 0x475569, roughness: 0.45, metalness: 0.85, map: T.brushedMetal }),
            fenceWire: new THREE.MeshStandardMaterial({ color: 0x64748b, wireframe: true }),
            
            // Concrete & Structural (Applied Procedural Concrete Texture)
            concretePiles: new THREE.MeshStandardMaterial({ color: 0x64748b, roughness: 0.9, metalness: 0.1 }),
            rebar: new THREE.MeshStandardMaterial({ color: 0x9a3412, roughness: 0.65, metalness: 0.7 }),
            concreteSlab: new THREE.MeshStandardMaterial({ color: 0x94a3b8, roughness: 0.75, metalness: 0.15, map: T.concrete }),
            concreteCured: new THREE.MeshStandardMaterial({ color: 0x838a92, roughness: 0.65, metalness: 0.12, map: T.concrete }),
            columns: new THREE.MeshStandardMaterial({ color: 0x64748b, roughness: 0.7, metalness: 0.15, map: T.concrete }),
            steelTruss: new THREE.MeshStandardMaterial({ color: 0x334155, roughness: 0.38, metalness: 0.88, map: T.brushedMetal }),
            steelGantry: new THREE.MeshStandardMaterial({ color: 0xf59e0b, roughness: 0.35, metalness: 0.75, map: T.hazardStripes }),
            
            // Envelope & Architecture
            facadeDark: new THREE.MeshStandardMaterial({ color: 0x0f172a, roughness: 0.42, metalness: 0.65, map: T.brushedMetal }),
            facadeLight: new THREE.MeshStandardMaterial({ color: 0x334155, roughness: 0.48, metalness: 0.45 }),
            facadeAccent: new THREE.MeshStandardMaterial({ color: 0x00e5ff, emissive: 0x00e5ff, emissiveIntensity: 0.6 }),
            roofTPO: new THREE.MeshStandardMaterial({ color: 0xe2e8f0, roughness: 0.55, metalness: 0.1 }),
            glass: new THREE.MeshPhysicalMaterial({ color: 0x0284c7, transmission: 0.82, opacity: 0.55, transparent: true, roughness: 0.08, ior: 1.5 }),
            glassHAC: new THREE.MeshPhysicalMaterial({ color: 0x00e5ff, transmission: 0.88, opacity: 0.4, transparent: true, roughness: 0.05 }),
            louvers: new THREE.MeshStandardMaterial({ color: 0x1e293b, roughness: 0.5, metalness: 0.85 }),
            doors: new THREE.MeshStandardMaterial({ color: 0x1e293b, roughness: 0.6, metalness: 0.5 }),
            
            // MEP Electrical
            transformerTank: new THREE.MeshStandardMaterial({ color: 0x243224, roughness: 0.4, metalness: 0.75, map: T.brushedMetal }),
            copperBus: new THREE.MeshStandardMaterial({ color: 0xb87333, roughness: 0.28, metalness: 0.92 }),
            bushingPorcelain: new THREE.MeshStandardMaterial({ color: 0x7c2d12, roughness: 0.15, metalness: 0.1 }),
            switchgear: new THREE.MeshStandardMaterial({ color: 0x18181b, roughness: 0.38, metalness: 0.65 }),
            generatorBody: new THREE.MeshStandardMaterial({ color: 0xb45309, roughness: 0.38, metalness: 0.65, map: T.brushedMetal }),
            exhaustStack: new THREE.MeshStandardMaterial({ color: 0x94a3b8, roughness: 0.25, metalness: 0.9, map: T.brushedMetal }),
            fuelTank: new THREE.MeshStandardMaterial({ color: 0x71717a, roughness: 0.4, metalness: 0.75 }),
            upsCabinet: new THREE.MeshStandardMaterial({ color: 0x09090b, roughness: 0.4, metalness: 0.65 }),
            batteryCabinet: new THREE.MeshStandardMaterial({ color: 0x18181b, roughness: 0.3, metalness: 0.7, map: T.pcb }),
            valveRed: new THREE.MeshStandardMaterial({ color: 0xdc2626, roughness: 0.3, metalness: 0.7 }),
            valveBlue: new THREE.MeshStandardMaterial({ color: 0x0284c7, roughness: 0.3, metalness: 0.7 }),
            springSteel: new THREE.MeshStandardMaterial({ color: 0x475569, roughness: 0.2, metalness: 0.95 }),

            // MEP Mechanical
            chillerBlue: new THREE.MeshStandardMaterial({ color: 0x0369a1, roughness: 0.32, metalness: 0.78, map: T.brushedMetal }),
            pumpYellow: new THREE.MeshStandardMaterial({ color: 0xd97706, roughness: 0.38, metalness: 0.65 }),
            chwSupplyPipe: new THREE.MeshStandardMaterial({ color: 0x0284c7, roughness: 0.28, metalness: 0.8 }),
            chwReturnPipe: new THREE.MeshStandardMaterial({ color: 0x0f766e, roughness: 0.28, metalness: 0.8 }),
            coolingTowerCasing: new THREE.MeshStandardMaterial({ color: 0x64748b, roughness: 0.5, metalness: 0.45 }),
            coolingTowerFan: new THREE.MeshStandardMaterial({ color: 0x09090b, roughness: 0.35, metalness: 0.85 }),
            crahUnit: new THREE.MeshStandardMaterial({ color: 0x1e293b, roughness: 0.4, metalness: 0.55 }),
            raisedFloor: new THREE.MeshStandardMaterial({ color: 0x475569, roughness: 0.65, metalness: 0.28 }),
            underfloorFlex: new THREE.MeshStandardMaterial({ color: 0x0284c7, roughness: 0.5, metalness: 0.3 }),
            fiberTrayYellow: new THREE.MeshStandardMaterial({ color: 0xeab308, roughness: 0.4, metalness: 0.5 }),

            // IT White Space
            serverRackBody: new THREE.MeshStandardMaterial({ color: 0x09090b, roughness: 0.4, metalness: 0.85 }),
            serverRackMesh: new THREE.MeshStandardMaterial({ color: 0x18181b, roughness: 0.6, metalness: 0.8, map: T.hexMesh }),
            serverBladePCB: new THREE.MeshStandardMaterial({ color: 0x064e3b, roughness: 0.3, metalness: 0.7, map: T.pcb }),
            serverRackGlow: new THREE.MeshStandardMaterial({ color: 0x00e5ff, emissive: 0x00e5ff, emissiveIntensity: 1.2 }),
            serverRackAlert: new THREE.MeshStandardMaterial({ color: 0xf59e0b, emissive: 0xf59e0b, emissiveIntensity: 1.2 }),
            buswayTrunk: new THREE.MeshStandardMaterial({ color: 0xb45309, roughness: 0.35, metalness: 0.75, map: T.hazardStripes }),
            
            // Load Banks & Construction
            loadBank: new THREE.MeshStandardMaterial({ color: 0xb91c1c, roughness: 0.38, metalness: 0.65 }),
            cautionStripe: new THREE.MeshStandardMaterial({ color: 0xf59e0b, map: T.hazardStripes }),
            cableOrange: new THREE.MeshStandardMaterial({ color: 0xea580c, roughness: 0.55, metalness: 0.1 }),
            craneYellow: new THREE.MeshStandardMaterial({ color: 0xd97706, roughness: 0.35, metalness: 0.7 }),
            craneTreads: new THREE.MeshStandardMaterial({ color: 0x18181b, roughness: 0.9, metalness: 0.3 })
        };
    }

    // Helper: Parametric Helical Compression Spring for Vibration Isolators
    function createHelicalSpring(radius, height, coils, wireRadius, material) {
        const points = [];
        const segments = coils * 32;
        for (let i = 0; i <= segments; i++) {
            const t = i / segments;
            const angle = t * coils * Math.PI * 2;
            const x = radius * Math.cos(angle);
            const z = radius * Math.sin(angle);
            const y = t * height;
            points.push(new THREE.Vector3(x, y, z));
        }
        const curve = new THREE.CatmullRomCurve3(points);
        const geo = new THREE.TubeGeometry(curve, segments, wireRadius, 8, false);
        return new THREE.Mesh(geo, material);
    }

    // Helper: Industrial Pipe with Flanged Ends & Butterfly Valve
    function createFlangedPipeWithValve(length, radius, pipeMat, valveMat) {
        const group = new THREE.Group();
        
        // Main Pipe Tube
        const pipe = new THREE.Mesh(new THREE.CylinderGeometry(radius, radius, length, 16), pipeMat);
        pipe.rotation.z = Math.PI / 2;
        group.add(pipe);

        // Flange Rings (Ends and Center)
        const flangeGeo = new THREE.CylinderGeometry(radius * 1.45, radius * 1.45, radius * 0.4, 16);
        [-length/2, 0, length/2].forEach(x => {
            const flange = new THREE.Mesh(flangeGeo, pipeMat);
            flange.rotation.z = Math.PI / 2;
            flange.position.x = x;
            group.add(flange);
        });

        // Center Butterfly Valve Handwheel
        const wheelHub = new THREE.Mesh(new THREE.CylinderGeometry(radius * 0.25, radius * 0.25, radius * 1.8, 8), valveMat);
        wheelHub.position.y = radius * 1.2;
        const wheelRim = new THREE.Mesh(new THREE.TorusGeometry(radius * 0.8, radius * 0.12, 8, 16), valveMat);
        wheelRim.rotation.x = Math.PI / 2;
        wheelRim.position.y = radius * 2.1;
        group.add(wheelHub, wheelRim);

        return group;
    }

    // 1. Build Base Campus Terrain & Perimeter
    function createCampusSite(M) {
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

        // Landscaping Green Strips
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
        const roadLine = new THREE.Mesh(new THREE.PlaneGeometry(190, 0.4), M.roadMarking);
        roadLine.rotation.x = -Math.PI / 2;
        roadLine.position.set(0, 0.09, 65);
        group.add(roadLine);

        // Security Perimeter Fence
        const fenceGroup = new THREE.Group();
        const fencePoints = [[-102, -72], [102, -72], [102, 72], [-102, 72]];
        for (let i = 0; i < 4; i++) {
            const p1 = fencePoints[i];
            const p2 = fencePoints[(i + 1) % 4];
            const len = Math.hypot(p2[0] - p1[0], p2[1] - p1[1]);
            const angle = Math.atan2(p2[1] - p1[1], p2[0] - p1[0]);

            const curb = new THREE.Mesh(new THREE.BoxGeometry(len, 0.6, 0.4), M.concreteSlab);
            curb.position.set((p1[0] + p2[0]) / 2, 0.3, (p1[1] + p2[1]) / 2);
            curb.rotation.y = -angle;
            fenceGroup.add(curb);

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

        // Guard House
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
    function createGroundworkAndPiling(M) {
        const group = new THREE.Group();
        group.name = "GroundworkAndPiling";
        group.userData = { phase: 1, tag: "piling", wbs: "4.1-SUB" };

        const pitBorder = new THREE.Mesh(new THREE.BoxGeometry(92, 0.8, 62), M.ground);
        pitBorder.position.set(5, 0.4, 0);
        group.add(pitBorder);

        const pitFloor = new THREE.Mesh(new THREE.PlaneGeometry(90, 60), M.ground);
        pitFloor.rotation.x = -Math.PI / 2;
        pitFloor.position.set(5, 0.1, 0);
        group.add(pitFloor);

        // Bored Concrete Piling Grid (600 piles represented by 16x10 clusters with rebar cages)
        const pilesGroup = new THREE.Group();
        const pileGeo = new THREE.CylinderGeometry(0.35, 0.35, 3.5, 12);
        const rebarGeo = new THREE.CylinderGeometry(0.28, 0.28, 1.2, 8);

        const cols = 16, rows = 10;
        const startX = -36 + 5, startZ = -24;
        const spacingX = 72 / (cols - 1), spacingZ = 48 / (rows - 1);

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

        // Hydraulic Piling Rig
        const rigGroup = new THREE.Group();
        rigGroup.position.set(-20, 0, 15);
        const tread1 = new THREE.Mesh(new THREE.BoxGeometry(4.5, 1.2, 1.0), M.craneTreads);
        tread1.position.set(0, 0.6, -1.5);
        const tread2 = tread1.clone();
        tread2.position.set(0, 0.6, 1.5);
        rigGroup.add(tread1, tread2);

        const cab = new THREE.Mesh(new THREE.BoxGeometry(3.5, 2.2, 2.6), M.craneYellow);
        cab.position.set(0, 2.0, 0);
        cab.castShadow = true;
        rigGroup.add(cab);

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
    function createFoundationAndPlinths(M) {
        const group = new THREE.Group();
        group.name = "FoundationAndPlinths";
        group.userData = { phase: 2, tag: "raft_slab", wbs: "4.1-SUB" };

        const raft = new THREE.Mesh(new THREE.BoxGeometry(90, 1.8, 60), M.concreteCured);
        raft.position.set(5, 0.9, 0);
        raft.receiveShadow = true;
        raft.castShadow = true;
        group.add(raft);

        const earthGrid = new THREE.Mesh(new THREE.BoxGeometry(92, 0.1, 62), M.copperBus);
        earthGrid.position.set(5, 0.05, 0);
        group.add(earthGrid);

        // Generator Plinths (West Yard)
        const genPlinthGroup = new THREE.Group();
        for (let i = 0; i < 8; i++) {
            const z = -28 + i * 8;
            const plinthA = new THREE.Mesh(new THREE.BoxGeometry(7.5, 0.6, 3.2), M.concreteSlab);
            plinthA.position.set(-60, 0.3, z);
            plinthA.castShadow = true;
            const plinthB = new THREE.Mesh(new THREE.BoxGeometry(7.5, 0.6, 3.2), M.concreteSlab);
            plinthB.position.set(-72, 0.3, z);
            plinthB.castShadow = true;
            genPlinthGroup.add(plinthA, plinthB);
        }
        group.add(genPlinthGroup);

        // Substation Transformer Plinths (South Yard)
        const subPlinthA = new THREE.Mesh(new THREE.BoxGeometry(10, 0.8, 8), M.concreteSlab);
        subPlinthA.position.set(-20, 0.4, 48);
        subPlinthA.castShadow = true;

        const subPlinthB = new THREE.Mesh(new THREE.BoxGeometry(10, 0.8, 8), M.concreteSlab);
        subPlinthB.position.set(10, 0.4, 48);
        subPlinthB.castShadow = true;

        group.add(subPlinthA, subPlinthB);
        return group;
    }

    // 4. Phase 3: Concrete Superstructure
    function createSuperstructure(M) {
        const group = new THREE.Group();
        group.name = "Superstructure";
        group.userData = { phase: 3, tag: "superstructure", wbs: "4.2-SUPER" };

        const colGrid = new THREE.Group();
        const colGeo = new THREE.BoxGeometry(0.9, 10.5, 0.9);
        const cols = 9, rows = 7;
        const startX = -38 + 5, startZ = -26;
        const stepX = 76 / (cols - 1), stepZ = 52 / (rows - 1);

        for (let c = 0; c < cols; c++) {
            for (let r = 0; r < rows; r++) {
                const col = new THREE.Mesh(colGeo, M.columns);
                col.position.set(startX + c * stepX, 1.8 + 10.5 / 2, startZ + r * stepZ);
                col.castShadow = true;
                col.receiveShadow = true;
                colGrid.add(col);
            }
        }
        group.add(colGrid);

        const wallGeo = new THREE.BoxGeometry(1.2, 11, 14);
        const wallA = new THREE.Mesh(wallGeo, M.columns);
        wallA.position.set(-15 + 5, 7.3, 0);
        wallA.castShadow = true;
        const wallB = new THREE.Mesh(wallGeo, M.columns);
        wallB.position.set(15 + 5, 7.3, 0);
        wallB.castShadow = true;
        group.add(wallA, wallB);

        const slabL1 = new THREE.Mesh(new THREE.BoxGeometry(89, 0.6, 59), M.concreteSlab);
        slabL1.position.set(5, 7.0, 0);
        slabL1.castShadow = true;
        slabL1.receiveShadow = true;
        slabL1.name = "SlabL1";
        group.add(slabL1);

        const slabL2 = new THREE.Mesh(new THREE.BoxGeometry(89, 0.6, 59), M.concreteSlab);
        slabL2.position.set(5, 12.3, 0);
        slabL2.castShadow = true;
        slabL2.receiveShadow = true;
        slabL2.name = "SlabL2";
        group.add(slabL2);

        return group;
    }

    // 5. Phase 4: Structural Steel Roof Trusses & Building Envelope
    function createRoofAndEnvelope(M) {
        const group = new THREE.Group();
        group.name = "RoofAndEnvelope";
        group.userData = { phase: 4, tag: "envelope", wbs: "4.3-ENVEL" };

        const roofSteel = new THREE.Group();
        for (let i = 0; i < 9; i++) {
            const x = -38 + 5 + i * (76 / 8);
            const trussBeam = new THREE.Mesh(new THREE.BoxGeometry(0.5, 1.2, 59), M.steelTruss);
            trussBeam.position.set(x, 18.0, 0);
            trussBeam.castShadow = true;
            roofSteel.add(trussBeam);
        }
        group.add(roofSteel);

        const gantry = new THREE.Mesh(new THREE.BoxGeometry(54, 0.4, 22), M.steelGantry);
        gantry.position.set(5, 18.8, 0);
        gantry.castShadow = true;
        group.add(gantry);

        const roof = new THREE.Mesh(new THREE.BoxGeometry(90.5, 0.5, 60.5), M.roofTPO);
        roof.position.set(5, 18.5, 0);
        roof.receiveShadow = true;
        roof.name = "RoofMembrane";
        group.add(roof);

        // Precast Insulated Architectural Facade Panels
        const facadeGroup = new THREE.Group();
        facadeGroup.name = "BuildingFacade";

        const southWall = new THREE.Mesh(new THREE.BoxGeometry(90.6, 17, 0.4), M.facadeDark);
        southWall.position.set(5, 10.3, 30.2);
        southWall.castShadow = true;
        facadeGroup.add(southWall);

        const northWall = new THREE.Mesh(new THREE.BoxGeometry(90.6, 17, 0.4), M.facadeDark);
        northWall.position.set(5, 10.3, -30.2);
        northWall.castShadow = true;
        facadeGroup.add(northWall);

        const westWall = new THREE.Mesh(new THREE.BoxGeometry(0.4, 17, 60.4), M.facadeLight);
        westWall.position.set(-40.2, 10.3, 0);
        westWall.castShadow = true;
        facadeGroup.add(westWall);

        const eastWall = new THREE.Mesh(new THREE.BoxGeometry(0.4, 17, 60.4), M.facadeLight);
        eastWall.position.set(50.2, 10.3, 0);
        eastWall.castShadow = true;
        facadeGroup.add(eastWall);

        // Radiant Cyan LED Architectural Reveal Ribbon (Post-processing bloom target)
        const accentBand = new THREE.Mesh(new THREE.BoxGeometry(91, 0.35, 61), M.facadeAccent);
        accentBand.position.set(5, 18.6, 0);
        facadeGroup.add(accentBand);

        for (let l = 0; l < 8; l++) {
            const louver = new THREE.Mesh(new THREE.BoxGeometry(0.5, 3.5, 5), M.louvers);
            louver.position.set(-40.3, 3.5, -24 + l * 7);
            facadeGroup.add(louver);
        }

        const mainDoor = new THREE.Mesh(new THREE.BoxGeometry(0.5, 4.0, 5.0), M.doors);
        mainDoor.position.set(50.3, 3.8, 0);
        facadeGroup.add(mainDoor);

        group.add(facadeGroup);
        return group;
    }

    // 6. Phase 5: Heavy MEP (Substation, 16 Gensets, 6 Chillers & Cooling Towers)
    function createHeavyMEP(M) {
        const group = new THREE.Group();
        group.name = "HeavyMEP";
        group.userData = { phase: 5, tag: "heavy_mep", wbs: "5.0-MEP" };

        // --- A. 110kV/22kV Substation ---
        const subGroup = new THREE.Group();
        subGroup.name = "MainSubstation";
        subGroup.position.set(0, 0, 48);

        // 2x 45MVA Power Transformers with Corrugated Radiator Banks & Oil Conservators
        [-20, 10].forEach((tx, idx) => {
            const tr = new THREE.Group();
            tr.position.set(tx, 0.8, 0);
            tr.name = `Transformer_${idx + 1}_45MVA`;

            const tank = new THREE.Mesh(new THREE.BoxGeometry(5.2, 4.2, 4.0), M.transformerTank);
            tank.position.y = 2.1;
            tank.castShadow = true;
            tr.add(tank);

            // Corrugated Radiator Vanes
            for (let f = -1.8; f <= 1.8; f += 0.45) {
                const fin = new THREE.Mesh(new THREE.BoxGeometry(5.4, 3.4, 0.08), M.transformerTank);
                fin.position.set(0, 2.1, f);
                tr.add(fin);
            }

            // High Voltage Multi-Skirt Ceramic Bushings
            for (let b = -1.2; b <= 1.2; b += 1.2) {
                const bushingBase = new THREE.Mesh(new THREE.CylinderGeometry(0.12, 0.25, 2.2, 8), M.bushingPorcelain);
                bushingBase.position.set(b, 5.3, 0);
                tr.add(bushingBase);
                // Petticoat Skirt Rings
                for (let k = 0; k < 4; k++) {
                    const skirt = new THREE.Mesh(new THREE.CylinderGeometry(0.28, 0.28, 0.06, 12), M.bushingPorcelain);
                    skirt.position.set(b, 4.6 + k * 0.4, 0);
                    tr.add(skirt);
                }
            }

            // Conservator Tank
            const cons = new THREE.Mesh(new THREE.CylinderGeometry(0.65, 0.65, 4.0, 16), M.transformerTank);
            cons.rotation.z = Math.PI / 2;
            cons.position.set(0, 5.2, 1.5);
            tr.add(cons);

            subGroup.add(tr);
        });

        // Substation High-Voltage Gantry Tower with Sagging Catenary Curves
        const gantryTower = new THREE.Group();
        gantryTower.position.set(-5, 0, 8);
        const postA = new THREE.Mesh(new THREE.CylinderGeometry(0.2, 0.35, 14, 8), M.steelTruss);
        postA.position.set(-18, 7, 0);
        const postB = new THREE.Mesh(new THREE.CylinderGeometry(0.2, 0.35, 14, 8), M.steelTruss);
        postB.position.set(18, 7, 0);
        const crossArm = new THREE.Mesh(new THREE.BoxGeometry(40, 0.8, 0.8), M.steelTruss);
        crossArm.position.set(0, 13, 0);
        gantryTower.add(postA, postB, crossArm);

        // 3 Braided Overhead Conductors with Catenary Sag
        [-10, 0, 10].forEach(cx => {
            const p1 = new THREE.Vector3(cx, 13, 0);
            const pMid = new THREE.Vector3(cx, 9.5, 20); // Sagging belly
            const p2 = new THREE.Vector3(cx - 5, 6, 40); // Transformer drop
            const curve = new THREE.CatmullRomCurve3([p1, pMid, p2]);
            const wireMesh = new THREE.Mesh(new THREE.TubeGeometry(curve, 32, 0.04, 6, false), M.copperBus);
            gantryTower.add(wireMesh);
        });
        subGroup.add(gantryTower);
        group.add(subGroup);

        // --- B. 16x 2.5MVA Standby Diesel Generators with Helical Springs & Exhaust Stacks ---
        const genGroup = new THREE.Group();
        genGroup.name = "GeneratorFarm";
        genGroup.position.set(-66, 0, 0);

        for (let i = 0; i < 8; i++) {
            const z = -28 + i * 8;
            [-6, 6].forEach((xOff, bankIdx) => {
                const genset = new THREE.Group();
                genset.position.set(xOff, 0.6, z);
                genset.name = `Genset_${i * 2 + bankIdx + 1}_2.5MVA`;

                const container = new THREE.Mesh(new THREE.BoxGeometry(6.5, 2.8, 2.6), M.generatorBody);
                container.position.y = 1.4;
                container.castShadow = true;
                genset.add(container);

                const louverEnd = new THREE.Mesh(new THREE.BoxGeometry(0.15, 2.2, 2.3), M.louvers);
                louverEnd.position.set(3.3, 1.4, 0);
                genset.add(louverEnd);

                const stack = new THREE.Mesh(new THREE.CylinderGeometry(0.25, 0.25, 6.0, 12), M.exhaustStack);
                stack.position.set(-2.0, 4.4, 0);
                stack.castShadow = true;
                genset.add(stack);

                // 4 Real Helical Compression Springs
                for (let sx of [-2.5, 2.5]) {
                    for (let sz of [-1.0, 1.0]) {
                        const spring = createHelicalSpring(0.18, 0.45, 5, 0.03, M.springSteel);
                        spring.position.set(sx, 0.05, sz);
                        genset.add(spring);
                    }
                }

                genGroup.add(genset);
            });
        }

        // Bulk Fuel Storage Tanks & Manifold
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

        // --- C. Central Chilled Water Plant (6 Chillers & Rooftop Cooling Towers) ---
        const chwPlant = new THREE.Group();
        chwPlant.name = "ChilledWaterPlant";

        // 6 Centrifugal Chillers with Flanged Butterfly Valves & Compressor
        const chillersGroup = new THREE.Group();
        chillersGroup.name = "CentrifugalChillers";
        for (let i = 0; i < 6; i++) {
            const ch = new THREE.Group();
            const cz = -20 + i * 8;
            ch.position.set(-18 + 5, 7.3, cz);
            ch.name = `Chiller_${i + 1}_1200RT`;

            const evap = new THREE.Mesh(new THREE.CylinderGeometry(0.9, 0.9, 6.0, 16), M.chillerBlue);
            evap.rotation.z = Math.PI / 2;
            evap.position.y = 1.0;
            evap.castShadow = true;
            ch.add(evap);

            const cond = new THREE.Mesh(new THREE.CylinderGeometry(0.8, 0.8, 5.8, 16), M.chillerBlue);
            cond.rotation.z = Math.PI / 2;
            cond.position.set(0, 2.3, 0.4);
            cond.castShadow = true;
            ch.add(cond);

            const comp = new THREE.Mesh(new THREE.CylinderGeometry(0.65, 0.65, 2.0, 12), M.pumpYellow);
            comp.position.set(0, 3.4, 0);
            ch.add(comp);

            // Flanged Water Box Inlets
            const valveA = createFlangedPipeWithValve(1.8, 0.22, M.chwSupplyPipe, M.valveBlue);
            valveA.position.set(2.8, 1.0, 0);
            ch.add(valveA);

            chillersGroup.add(ch);
        }
        chwPlant.add(chillersGroup);

        // Dual Header Chilled Water Pipes (DN500 Supply & Return)
        const headerSupply = createFlangedPipeWithValve(48, 0.3, M.chwSupplyPipe, M.valveBlue);
        headerSupply.position.set(-23 + 5, 10.5, 0);
        chwPlant.add(headerSupply);

        const headerReturn = createFlangedPipeWithValve(48, 0.3, M.chwReturnPipe, M.valveRed);
        headerReturn.position.set(-22 + 5, 10.5, 0);
        chwPlant.add(headerReturn);

        // 6 Rooftop Cooling Towers with Rotating Fans
        const coolingTowers = new THREE.Group();
        coolingTowers.name = "RooftopCoolingTowers";
        window.DC36_COOLING_FANS = [];

        for (let ct = 0; ct < 6; ct++) {
            const tower = new THREE.Group();
            const tz = -18 + ct * 7.2;
            tower.position.set(5, 19.0, tz);
            tower.name = `CoolingTower_${ct + 1}`;

            const casing = new THREE.Mesh(new THREE.BoxGeometry(5.0, 4.0, 5.0), M.coolingTowerCasing);
            casing.position.y = 2.0;
            casing.castShadow = true;
            tower.add(casing);

            const louverBase = new THREE.Mesh(new THREE.BoxGeometry(5.1, 1.2, 5.1), M.louvers);
            louverBase.position.y = 0.6;
            tower.add(louverBase);

            const cowl = new THREE.Mesh(new THREE.CylinderGeometry(1.8, 1.9, 1.2, 16), M.coolingTowerFan);
            cowl.position.y = 4.6;
            tower.add(cowl);

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

    // 7. Phase 6: White Space Fit-Out (Halls 1 to 4 with Hex Racks & Underfloor Trays)
    function createWhiteSpaceFitOut(M) {
        const group = new THREE.Group();
        group.name = "WhiteSpaceFitOut";
        group.userData = { phase: 6, tag: "white_space", wbs: "5.4-WS" };

        window.DC36_SERVER_LEDS = [];

        // 800mm Raised Floor
        const raisedFloor = new THREE.Mesh(new THREE.BoxGeometry(78, 0.1, 48), M.raisedFloor);
        raisedFloor.position.set(5, 13.1, 0);
        raisedFloor.receiveShadow = true;
        group.add(raisedFloor);

        // Underfloor Secondary Chilled Water Flex Runs & Yellow Fiber Trays (Visible in cutaway)
        for (let z = -20; z <= 20; z += 10) {
            const chwFlex = new THREE.Mesh(new THREE.CylinderGeometry(0.14, 0.14, 76, 12), M.underfloorFlex);
            chwFlex.rotation.z = Math.PI / 2;
            chwFlex.position.set(5, 12.6, z);
            group.add(chwFlex);

            const fiberTray = new THREE.Mesh(new THREE.BoxGeometry(76, 0.12, 0.5), M.fiberTrayYellow);
            fiberTray.position.set(5, 12.8, z + 2);
            group.add(fiberTray);
        }

        // 4 Symmetrical Data Halls: Quad 1 to 4
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

            for (let pod = 0; pod < 3; pod++) {
                const podCenterZ = -7.2 + pod * 7.2;

                // Hot Aisle Containment Roof & Sliding Glass Doors
                const hacRoof = new THREE.Mesh(new THREE.BoxGeometry(20, 0.08, 1.6), M.glassHAC);
                hacRoof.position.set(0, 2.5, podCenterZ);
                hallGroup.add(hacRoof);

                const doorWest = new THREE.Mesh(new THREE.BoxGeometry(0.1, 2.4, 1.6), M.glassHAC);
                doorWest.position.set(-10, 1.2, podCenterZ);
                const doorEast = new THREE.Mesh(new THREE.BoxGeometry(0.1, 2.4, 1.6), M.glassHAC);
                doorEast.position.set(10, 1.2, podCenterZ);
                hallGroup.add(doorWest, doorEast);

                // Overhead 415V Busway Distribution Trunks
                const buswayA = new THREE.Mesh(new THREE.BoxGeometry(22, 0.25, 0.25), M.buswayTrunk);
                buswayA.position.set(0, 3.2, podCenterZ - 0.9);
                const buswayB = new THREE.Mesh(new THREE.BoxGeometry(22, 0.25, 0.25), M.buswayTrunk);
                buswayB.position.set(0, 3.2, podCenterZ + 0.9);
                hallGroup.add(buswayA, buswayB);

                // Rows of 42U Server Racks with Hex Door Mesh & Blinking LED strips
                [-0.8, 0.8].forEach(zOffset => {
                    for (let r = 0; r < 14; r++) {
                        const rx = -8.5 + r * 1.3;
                        const rack = new THREE.Group();
                        rack.position.set(rx, 0, podCenterZ + zOffset);

                        const body = new THREE.Mesh(new THREE.BoxGeometry(0.8, 2.2, 1.0), M.serverRackBody);
                        body.position.y = 1.1;
                        body.castShadow = true;
                        rack.add(body);

                        // Hex Front Door Mesh
                        const doorMesh = new THREE.Mesh(new THREE.PlaneGeometry(0.76, 2.1), M.serverRackMesh);
                        doorMesh.position.set(0, 1.1, zOffset > 0 ? -0.51 : 0.51);
                        if (zOffset > 0) doorMesh.rotation.y = Math.PI;
                        rack.add(doorMesh);

                        // Emissive Telemetry LED Array
                        const led = new THREE.Mesh(new THREE.BoxGeometry(0.65, 0.08, 0.02), M.serverRackGlow.clone());
                        led.position.set(0, 1.8, zOffset > 0 ? -0.52 : 0.52);
                        rack.add(led);
                        window.DC36_SERVER_LEDS.push(led);

                        hallGroup.add(rack);
                    }
                });
            }

            // CRAH Units
            for (let c = -9; c <= 9; c += 6) {
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

        // Modular Static UPS & Battery Rooms
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
    function createCommissioningLoadBanks(M) {
        const group = new THREE.Group();
        group.name = "CommissioningLoadBanks";
        group.userData = { phase: 7, tag: "load_banks", wbs: "6.4-L5" };

        const lbCount = 8;
        for (let i = 0; i < lbCount; i++) {
            const z = -25 + i * 7.2;
            const lb = new THREE.Group();
            lb.position.set(58, 0.4, z);
            lb.name = `LoadBank_${i + 1}_4.5MW`;

            const chassis = new THREE.Mesh(new THREE.BoxGeometry(6.5, 0.6, 2.8), M.craneTreads);
            chassis.position.y = 0.3;
            lb.add(chassis);

            const body = new THREE.Mesh(new THREE.BoxGeometry(5.8, 2.4, 2.6), M.loadBank);
            body.position.y = 1.8;
            body.castShadow = true;
            lb.add(body);

            const vent = new THREE.Mesh(new THREE.BoxGeometry(4.5, 0.4, 2.0), M.louvers);
            vent.position.y = 3.1;
            lb.add(vent);

            const cable = new THREE.Mesh(new THREE.CylinderGeometry(0.12, 0.12, 8.0, 8), M.cableOrange);
            cable.rotation.z = Math.PI / 2;
            cable.position.set(-4.0, 0.3, 0);
            lb.add(cable);

            group.add(lb);
        }

        const ringGeo = new THREE.RingGeometry(48, 52, 32);
        const ringMat = new THREE.MeshBasicMaterial({ color: 0x00e5ff, side: THREE.DoubleSide, transparent: true, opacity: 0.35 });
        const ring = new THREE.Mesh(ringGeo, ringMat);
        ring.rotation.x = -Math.PI / 2;
        ring.position.set(5, 0.2, 0);
        ring.name = "IST_PulseRing";
        group.add(ring);

        return group;
    }

    // Master Scene Assembly
    window.DC36_MODELS.buildDatacenterScene = function(scene) {
        const M = initMaterials();
        window.DC36_MATERIALS = M;

        const root = new THREE.Group();
        root.name = "DC36_DatacenterRoot";

        const site = createCampusSite(M);
        const p1 = createGroundworkAndPiling(M);
        const p2 = createFoundationAndPlinths(M);
        const p3 = createSuperstructure(M);
        const p4 = createRoofAndEnvelope(M);
        const p5 = createHeavyMEP(M);
        const p6 = createWhiteSpaceFitOut(M);
        const p7 = createCommissioningLoadBanks(M);

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
