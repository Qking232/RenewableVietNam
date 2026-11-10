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
            ground: new THREE.MeshStandardMaterial({ color: 0xe2e8f0, roughness: 0.95, metalness: 0.05 }),
            asphalt: new THREE.MeshStandardMaterial({ color: 0x334155, roughness: 0.88, metalness: 0.12 }),
            roadMarking: new THREE.MeshBasicMaterial({ color: 0xffffff }),
            grass: new THREE.MeshStandardMaterial({ color: 0x15803d, roughness: 0.92, metalness: 0.0 }),
            fencePost: new THREE.MeshStandardMaterial({ color: 0x64748b, roughness: 0.45, metalness: 0.85, map: T.brushedMetal }),
            fenceWire: new THREE.MeshStandardMaterial({ color: 0x94a3b8, wireframe: true }),
            
            // Concrete & Structural (Applied Procedural Concrete Texture)
            concretePiles: new THREE.MeshStandardMaterial({ color: 0x94a3b8, roughness: 0.9, metalness: 0.1 }),
            rebar: new THREE.MeshStandardMaterial({ color: 0x9a3412, roughness: 0.65, metalness: 0.7 }),
            concreteSlab: new THREE.MeshStandardMaterial({ color: 0xf1f5f9, roughness: 0.75, metalness: 0.15, map: T.concrete }),
            concreteCured: new THREE.MeshStandardMaterial({ color: 0xe2e8f0, roughness: 0.65, metalness: 0.12, map: T.concrete }),
            columns: new THREE.MeshStandardMaterial({ color: 0xcbd5e1, roughness: 0.7, metalness: 0.15, map: T.concrete }),
            steelTruss: new THREE.MeshStandardMaterial({ color: 0x64748b, roughness: 0.38, metalness: 0.88, map: T.brushedMetal }),
            steelGantry: new THREE.MeshStandardMaterial({ color: 0xf59e0b, roughness: 0.35, metalness: 0.75, map: T.hazardStripes }),
            
            // Envelope & Architecture
            facadeDark: new THREE.MeshStandardMaterial({ color: 0xe2e8f0, roughness: 0.42, metalness: 0.65, map: T.brushedMetal }),
            facadeLight: new THREE.MeshStandardMaterial({ color: 0xf8fafc, roughness: 0.48, metalness: 0.45 }),
            facadeAccent: new THREE.MeshStandardMaterial({ color: 0x0284c7, emissive: 0x0284c7, emissiveIntensity: 0.6 }),
            roofTPO: new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 0.55, metalness: 0.1 }),
            glass: new THREE.MeshPhysicalMaterial({ color: 0x0284c7, transmission: 0.82, opacity: 0.55, transparent: true, roughness: 0.08, ior: 1.5 }),
            glassHAC: new THREE.MeshPhysicalMaterial({ color: 0x0284c7, transmission: 0.88, opacity: 0.4, transparent: true, roughness: 0.05 }),
            louvers: new THREE.MeshStandardMaterial({ color: 0x64748b, roughness: 0.5, metalness: 0.85 }),
            doors: new THREE.MeshStandardMaterial({ color: 0x94a3b8, roughness: 0.6, metalness: 0.5 }),
            
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
            craneTreads: new THREE.MeshStandardMaterial({ color: 0x18181b, roughness: 0.9, metalness: 0.3 }),

            // Ancillary Facilities & Realism Materials
            water: new THREE.MeshStandardMaterial({ color: 0x0284c7, roughness: 0.08, metalness: 0.82, transparent: true, opacity: 0.85 }),
            riprap: new THREE.MeshStandardMaterial({ color: 0x57534e, roughness: 0.95, metalness: 0.05 }),
            treeFoliage: new THREE.MeshStandardMaterial({ color: 0x166534, roughness: 0.88, metalness: 0.0 }),
            treeBark: new THREE.MeshStandardMaterial({ color: 0x3e2723, roughness: 0.92, metalness: 0.04 }),
            k12Yellow: new THREE.MeshStandardMaterial({ color: 0xf59e0b, roughness: 0.32, metalness: 0.65 }),
            anprCamera: new THREE.MeshStandardMaterial({ color: 0x18181b, roughness: 0.4, metalness: 0.7 }),
            evGreenGlow: new THREE.MeshStandardMaterial({ color: 0x10b981, emissive: 0x10b981, emissiveIntensity: 0.85 }),
            solarPanel: new THREE.MeshStandardMaterial({ color: 0x1e3a8a, roughness: 0.18, metalness: 0.88 }),
            truckCab: new THREE.MeshStandardMaterial({ color: 0xd97706, roughness: 0.35, metalness: 0.68 }),
            truckTrailer: new THREE.MeshStandardMaterial({ color: 0xf8fafc, roughness: 0.5, metalness: 0.35 }),
            manholeCover: new THREE.MeshStandardMaterial({ color: 0x475569, roughness: 0.82, metalness: 0.55 }),
            blastWall: new THREE.MeshStandardMaterial({ color: 0xd1d5db, roughness: 0.82, metalness: 0.12, map: T.concrete }),
            curbYellow: new THREE.MeshStandardMaterial({ color: 0xf59e0b, roughness: 0.65, metalness: 0.1 }),
            curtainGlass: new THREE.MeshPhysicalMaterial({ color: 0x0284c7, transmission: 0.88, opacity: 0.6, transparent: true, roughness: 0.05, ior: 1.52 })
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

    // 1. Build Base Campus Terrain, Ancillary Facilities & Infrastructure
    function createCampusSite(M) {
        const group = new THREE.Group();
        group.name = "CampusSite";

        // Outer Regional Terrain Ground (Subdued dark industrial earth)
        const groundGeo = new THREE.PlaneGeometry(320, 260);
        const groundMesh = new THREE.Mesh(groundGeo, M.ground);
        groundMesh.rotation.x = -Math.PI / 2;
        groundMesh.receiveShadow = true;
        group.add(groundMesh);

        // Heavy-Duty Asphalt Campus Site Pad
        const campusGeo = new THREE.PlaneGeometry(240, 180);
        const campusMesh = new THREE.Mesh(campusGeo, M.asphalt);
        campusMesh.rotation.x = -Math.PI / 2;
        campusMesh.position.y = 0.04;
        campusMesh.receiveShadow = true;
        group.add(campusMesh);

        // Perimeter Grass & Landscaping Berms
        const grassBermN = new THREE.Mesh(new THREE.PlaneGeometry(236, 12), M.grass);
        grassBermN.rotation.x = -Math.PI / 2;
        grassBermN.position.set(0, 0.06, -82);
        grassBermN.receiveShadow = true;
        group.add(grassBermN);

        const grassBermE = new THREE.Mesh(new THREE.PlaneGeometry(12, 172), M.grass);
        grassBermE.rotation.x = -Math.PI / 2;
        grassBermE.position.set(112, 0.06, 0);
        grassBermE.receiveShadow = true;
        group.add(grassBermE);

        const grassBermW = new THREE.Mesh(new THREE.PlaneGeometry(12, 172), M.grass);
        grassBermW.rotation.x = -Math.PI / 2;
        grassBermW.position.set(-112, 0.06, 0);
        grassBermW.receiveShadow = true;
        group.add(grassBermW);

        // Security Perimeter Anti-Climb Fence with Concrete Curb
        const fenceGroup = new THREE.Group();
        const fencePoints = [[-115, -85], [115, -85], [115, 85], [-115, 85]];
        for (let i = 0; i < 4; i++) {
            const p1 = fencePoints[i];
            const p2 = fencePoints[(i + 1) % 4];
            const len = Math.hypot(p2[0] - p1[0], p2[1] - p1[1]);
            const angle = Math.atan2(p2[1] - p1[1], p2[0] - p1[0]);

            // Continuous concrete security plinth curb
            const curb = new THREE.Mesh(new THREE.BoxGeometry(len, 0.6, 0.4), M.concreteSlab);
            curb.position.set((p1[0] + p2[0]) / 2, 0.3, (p1[1] + p2[1]) / 2);
            curb.rotation.y = -angle;
            fenceGroup.add(curb);

            // Steel fence posts with anti-climb outriggers every 6m
            const postCount = Math.floor(len / 6);
            for (let j = 0; j <= postCount; j++) {
                const t = j / postCount;
                const px = p1[0] + (p2[0] - p1[0]) * t;
                const pz = p1[1] + (p2[1] - p1[1]) * t;
                
                // Main post
                const post = new THREE.Mesh(new THREE.CylinderGeometry(0.08, 0.08, 3.2, 8), M.fencePost);
                post.position.set(px, 1.9, pz);
                fenceGroup.add(post);

                // Y-crank razor wire outrigger arms
                const outrigger = new THREE.Mesh(new THREE.BoxGeometry(0.04, 0.6, 0.04), M.fencePost);
                outrigger.rotation.z = Math.PI / 4;
                outrigger.position.set(px + 0.15, 3.6, pz);
                fenceGroup.add(outrigger);
            }
        }
        group.add(fenceGroup);

        // --- SUB-FACILITY 1: Primary Security Gatehouse & Checkpoint ---
        const gateGroup = new THREE.Group();
        gateGroup.name = "SecurityGatehouseCheckpoint";
        gateGroup.position.set(-68, 0, 72);

        // Architectural Guardhouse
        const ghBase = new THREE.Mesh(new THREE.BoxGeometry(7.5, 3.4, 4.4), M.facadeDark);
        ghBase.position.set(0, 1.7, 0);
        ghBase.castShadow = true;
        gateGroup.add(ghBase);

        // Security Window Glazing Band
        const ghGlass = new THREE.Mesh(new THREE.BoxGeometry(7.3, 1.5, 4.2), M.glass);
        ghGlass.position.set(0, 2.2, 0);
        gateGroup.add(ghGlass);

        // Overhanging Architectural Roof Canopy
        const ghCanopy = new THREE.Mesh(new THREE.BoxGeometry(9.6, 0.35, 6.2), M.facadeLight);
        ghCanopy.position.set(0, 3.55, 0);
        ghCanopy.castShadow = true;
        gateGroup.add(ghCanopy);

        // Raised Island Median
        const median = new THREE.Mesh(new THREE.BoxGeometry(15, 0.25, 1.6), M.curbYellow);
        median.position.set(11, 0.12, 0);
        median.receiveShadow = true;
        gateGroup.add(median);

        // Automated Inbound & Outbound Barrier Arms (Reflective red-white)
        [-2.8, 2.8].forEach((laneZ, lIdx) => {
            // Barrier motor pedestal
            const pedestal = new THREE.Mesh(new THREE.BoxGeometry(0.5, 1.1, 0.5), M.k12Yellow);
            pedestal.position.set(6, 0.55, laneZ > 0 ? 0.6 : -0.6);
            gateGroup.add(pedestal);

            // Boom arm
            const arm = new THREE.Mesh(new THREE.BoxGeometry(5.2, 0.12, 0.08), M.cautionStripe);
            arm.position.set(8.6, 1.05, laneZ);
            gateGroup.add(arm);

            // Directional Tire Spike Plate in roadway
            const spikePlate = new THREE.Mesh(new THREE.BoxGeometry(3.6, 0.05, 0.7), M.transformerTank);
            spikePlate.position.set(11, 0.06, laneZ);
            gateGroup.add(spikePlate);

            // ANPR / CCTV Camera Stanchion
            const camPole = new THREE.Mesh(new THREE.CylinderGeometry(0.06, 0.06, 2.6, 8), M.fencePost);
            camPole.position.set(4.5, 1.3, laneZ + (laneZ > 0 ? 1.6 : -1.6));
            const camHead = new THREE.Mesh(new THREE.BoxGeometry(0.18, 0.14, 0.35), M.anprCamera);
            camHead.position.set(4.5, 2.5, laneZ + (laneZ > 0 ? 1.6 : -1.6));
            gateGroup.add(camPole, camHead);
        });

        // 8x K12 Crash-Rated Heavy Safety Bollards
        for (let b = 0; b < 4; b++) {
            const bx = 4.5 + b * 4.2;
            const bollard1 = new THREE.Mesh(new THREE.CylinderGeometry(0.14, 0.14, 1.05, 12), M.k12Yellow);
            bollard1.position.set(bx, 0.52, 0);
            bollard1.castShadow = true;
            gateGroup.add(bollard1);
        }

        // Visitor Pedestrian Turnstile Portal Canopy
        const turnstileCanopy = new THREE.Mesh(new THREE.BoxGeometry(5.5, 0.25, 3.8), M.facadeDark);
        turnstileCanopy.position.set(-6.5, 3.2, 0);
        const tsLeg1 = new THREE.Mesh(new THREE.CylinderGeometry(0.06, 0.06, 3.2, 8), M.steelTruss);
        tsLeg1.position.set(-8.8, 1.6, 1.6);
        const tsLeg2 = tsLeg1.clone();
        tsLeg2.position.set(-8.8, 1.6, -1.6);
        gateGroup.add(turnstileCanopy, tsLeg1, tsLeg2);

        // 2x Full-Height Turnstiles
        [-0.9, 0.9].forEach(tz => {
            const cage = new THREE.Mesh(new THREE.CylinderGeometry(0.9, 0.9, 2.4, 8, 1, true), M.fenceWire);
            cage.position.set(-6.5, 1.2, tz);
            const shaft = new THREE.Mesh(new THREE.CylinderGeometry(0.05, 0.05, 2.4, 8), M.fencePost);
            shaft.position.set(-6.5, 1.2, tz);
            gateGroup.add(cage, shaft);
        });

        group.add(gateGroup);

        // --- SUB-FACILITY 2: Commercial Vehicle Inspection Canopy & Logistics Staging ---
        const inspectGroup = new THREE.Group();
        inspectGroup.name = "VehicleInspectionCanopy";
        inspectGroup.position.set(-36, 0, 72);

        // Cantilever Steel Portal Frame
        const portalRoof = new THREE.Mesh(new THREE.BoxGeometry(11, 0.4, 8), M.facadeDark);
        portalRoof.position.set(0, 5.4, 0);
        portalRoof.castShadow = true;
        inspectGroup.add(portalRoof);

        const pColumn1 = new THREE.Mesh(new THREE.BoxGeometry(0.4, 5.4, 0.4), M.steelTruss);
        pColumn1.position.set(-5, 2.7, -3.6);
        const pColumn2 = pColumn1.clone();
        pColumn2.position.set(5, 2.7, -3.6);
        const pColumn3 = pColumn1.clone();
        pColumn3.position.set(-5, 2.7, 3.6);
        const pColumn4 = pColumn1.clone();
        pColumn4.position.set(5, 2.7, 3.6);
        inspectGroup.add(pColumn1, pColumn2, pColumn3, pColumn4);

        // Convex Mirror & Inspection Floodlights
        const mirror = new THREE.Mesh(new THREE.SphereGeometry(0.45, 16, 16, 0, Math.PI * 2, 0, Math.PI / 2), M.curtainGlass);
        mirror.rotation.x = Math.PI / 3;
        mirror.position.set(-4.5, 4.6, 3.2);
        inspectGroup.add(mirror);

        group.add(inspectGroup);

        // Waste Management & Recycling Corral
        const wasteCorral = new THREE.Group();
        wasteCorral.name = "WasteManagementCorral";
        wasteCorral.position.set(-92, 0, 36);

        const corralWall = new THREE.Mesh(new THREE.BoxGeometry(8, 2.4, 5), M.blastWall);
        corralWall.position.set(0, 1.2, 0);
        wasteCorral.add(corralWall);

        // 3x Color-Coded Commercial Dumpsters (General, Cardboard, E-Waste)
        const dumpsterColors = [0x15803d, 0x0284c7, 0x475569];
        dumpsterColors.forEach((col, dIdx) => {
            const dumpMat = new THREE.MeshStandardMaterial({ color: col, roughness: 0.5, metalness: 0.5 });
            const dump = new THREE.Mesh(new THREE.BoxGeometry(1.6, 1.3, 2.4), dumpMat);
            dump.position.set(-2.2 + dIdx * 2.2, 0.65, 0);
            wasteCorral.add(dump);
        });
        group.add(wasteCorral);

        // Pallet Staging Area with Timber Pallets
        const palletGroup = new THREE.Group();
        palletGroup.name = "PalletStaging";
        palletGroup.position.set(-92, 0, 16);
        for (let pz = -4; pz <= 4; pz += 2.2) {
            for (let py = 0; py < 3; py++) {
                const pallet = new THREE.Mesh(new THREE.BoxGeometry(2.0, 0.18, 1.6), M.treeBark);
                pallet.position.set(0, 0.1 + py * 0.22, pz);
                palletGroup.add(pallet);
            }
        }
        group.add(palletGroup);

        // --- SUB-FACILITY 3: Diverse Telecommunications Meet-Me-Room (MMR) Vaults ---
        // Path A Vault (Northwest)
        const mmrA = new THREE.Group();
        mmrA.name = "Telecom_MMR_Path_A";
        mmrA.position.set(-90, 0.05, -55);
        const mmrManholeA = new THREE.Mesh(new THREE.CylinderGeometry(0.7, 0.7, 0.08, 16), M.manholeCover);
        mmrManholeA.position.y = 0.04;
        const mmrCollarA = new THREE.Mesh(new THREE.BoxGeometry(2.2, 0.06, 2.2), M.concreteCured);
        mmrA.add(mmrManholeA, mmrCollarA);
        group.add(mmrA);

        // Path B Vault (Southeast Diverse Feed)
        const mmrB = new THREE.Group();
        mmrB.name = "Telecom_MMR_Path_B";
        mmrB.position.set(90, 0.05, 55);
        const mmrManholeB = mmrManholeA.clone();
        const mmrCollarB = mmrCollarA.clone();
        mmrB.add(mmrManholeB, mmrCollarB);
        group.add(mmrB);

        // Water Utility & Backflow Preventer Vault
        const waterVault = new THREE.Group();
        waterVault.name = "WaterUtilityVault";
        waterVault.position.set(-82, 0, 72);
        const wBox = new THREE.Mesh(new THREE.BoxGeometry(3.6, 1.2, 2.4), M.blastWall);
        wBox.position.y = 0.6;
        const valve1 = new THREE.Mesh(new THREE.CylinderGeometry(0.12, 0.12, 1.8, 8), M.valveBlue);
        valve1.rotation.z = Math.PI / 2;
        valve1.position.set(0, 1.3, -0.4);
        waterVault.add(wBox, valve1);
        group.add(waterVault);

        // --- SUB-FACILITY 4: Parking, EV Charging & Micro-Mobility Shelter ---
        const parkGroup = new THREE.Group();
        parkGroup.name = "ParkingAndMobility";
        parkGroup.position.set(65, 0, 52);

        // 20 Striped Parking Bays (White thermoplastic lines)
        for (let s = 0; s < 10; s++) {
            const sz = -18 + s * 3.6;
            const line = new THREE.Mesh(new THREE.PlaneGeometry(5.2, 0.15), M.roadMarking);
            line.rotation.x = -Math.PI / 2;
            line.position.set(0, 0.06, sz);
            parkGroup.add(line);
        }

        // 4 Dedicated EV Charging Bays (Green surface painting)
        for (let e = 0; e < 4; e++) {
            const ez = 4 + e * 3.6;
            const evBay = new THREE.Mesh(new THREE.PlaneGeometry(5.0, 3.2), M.evGreenGlow);
            evBay.rotation.x = -Math.PI / 2;
            evBay.position.set(0, 0.06, ez);
            parkGroup.add(evBay);

            // EV Fast Charger Arch Pylon
            const chargerArch = new THREE.Mesh(new THREE.BoxGeometry(0.3, 1.6, 0.6), M.facadeDark);
            chargerArch.position.set(2.8, 0.8, ez);
            const chargerLight = new THREE.Mesh(new THREE.BoxGeometry(0.32, 0.1, 0.5), M.evGreenGlow);
            chargerLight.position.set(2.8, 1.55, ez);
            parkGroup.add(chargerArch, chargerLight);
        }

        // Covered Bicycle & Scooter Shelter with Solar BIPV Glass
        const bikeShelter = new THREE.Group();
        bikeShelter.position.set(-8, 0, 0);
        const shelterRoof = new THREE.Mesh(new THREE.BoxGeometry(4.2, 0.18, 14), M.solarPanel);
        shelterRoof.position.set(0, 2.6, 0);
        shelterRoof.rotation.z = -0.12;
        shelterRoof.castShadow = true;
        const bPost1 = new THREE.Mesh(new THREE.BoxGeometry(0.15, 2.6, 0.15), M.steelTruss);
        bPost1.position.set(-1.8, 1.3, -6.5);
        const bPost2 = bPost1.clone();
        bPost2.position.set(-1.8, 1.3, 6.5);
        bikeShelter.add(shelterRoof, bPost1, bPost2);
        parkGroup.add(bikeShelter);

        group.add(parkGroup);

        // --- SUB-FACILITY 5: Engineered Stormwater Retention Basin & Landscape ---
        const basinGroup = new THREE.Group();
        basinGroup.name = "StormwaterRetentionBasin";
        basinGroup.position.set(78, 0, -42);

        // Excavated Basin Depression with Riprap Slopes
        const riprapBank = new THREE.Mesh(new THREE.BoxGeometry(42, 1.8, 28), M.riprap);
        riprapBank.position.y = 0.4;
        basinGroup.add(riprapBank);

        // Water Surface Reflection Plane
        const waterMesh = new THREE.Mesh(new THREE.PlaneGeometry(36, 22), M.water);
        waterMesh.rotation.x = -Math.PI / 2;
        waterMesh.position.y = 0.75;
        basinGroup.add(waterMesh);

        // Safety Lifebuoy Ring Post
        const lifebuoyPost = new THREE.Mesh(new THREE.CylinderGeometry(0.04, 0.04, 1.4, 8), M.k12Yellow);
        lifebuoyPost.position.set(-19, 0.7, 0);
        const ring = new THREE.Mesh(new THREE.TorusGeometry(0.28, 0.08, 8, 16), M.valveRed);
        ring.position.set(-19, 1.1, 0);
        basinGroup.add(lifebuoyPost, ring);

        group.add(basinGroup);

        // Perimeter Trees & Buffer Vegetation
        const treePositions = [
            [-108, -75], [-92, -75], [-76, -75], [-60, -75], [60, -75], [76, -75], [92, -75], [108, -75],
            [108, -55], [108, -35], [108, -15], [108, 15], [108, 35], [108, 55], [108, 75],
            [-108, -55], [-108, -35], [-108, -15], [-108, 15], [-108, 35], [-108, 55], [-108, 75]
        ];

        const foliageGeo = new THREE.ConeGeometry(1.8, 4.5, 8);
        const trunkGeo = new THREE.CylinderGeometry(0.2, 0.28, 1.8, 8);

        treePositions.forEach(tp => {
            const tree = new THREE.Group();
            tree.position.set(tp[0], 0, tp[1]);

            const trunk = new THREE.Mesh(trunkGeo, M.treeBark);
            trunk.position.y = 0.9;
            trunk.castShadow = true;

            const foliage = new THREE.Mesh(foliageGeo, M.treeFoliage);
            foliage.position.y = 3.8;
            foliage.castShadow = true;

            tree.add(trunk, foliage);
            group.add(tree);
        });

        // --- SUB-FACILITY 6: 110kV Steel Lattice Transmission Pylons ---
        const transmissionGroup = new THREE.Group();
        transmissionGroup.name = "Transmission110kVPylons";

        [-32, 28].forEach(tx => {
            const pylon = new THREE.Group();
            pylon.position.set(tx, 0, 92);

            // 4-Leg Lattice Base Tower
            const towerLegs = new THREE.Mesh(new THREE.CylinderGeometry(0.8, 2.8, 24, 4), M.steelTruss);
            towerLegs.position.y = 12;
            towerLegs.rotation.y = Math.PI / 4;
            pylon.add(towerLegs);

            // Crossarms for 3-Phase Conductors
            [-6, 0, 6].forEach((cx, cIdx) => {
                const arm = new THREE.Mesh(new THREE.BoxGeometry(6.5, 0.5, 0.5), M.steelTruss);
                arm.position.set(cx, 16 + cIdx * 2.8, 0);
                pylon.add(arm);

                // Hanging Ceramic Insulator Strings
                const ins = new THREE.Mesh(new THREE.CylinderGeometry(0.08, 0.08, 1.8, 8), M.bushingPorcelain);
                ins.position.set(cx + (cx >= 0 ? 3.0 : -3.0), 15 + cIdx * 2.8, 0);
                pylon.add(ins);
            });

            transmissionGroup.add(pylon);
        });

        // High Voltage Overhead Sagging Transmission Feed Lines into Substation Gantry
        for (let c = -1; c <= 1; c++) {
            const pStart = new THREE.Vector3(-32 + c * 3, 20, 92);
            const pMid = new THREE.Vector3(c * 6, 15, 75);
            const pEnd = new THREE.Vector3(28 + c * 3, 20, 92);
            const catCurve = new THREE.CatmullRomCurve3([pStart, pMid, pEnd]);
            const catMesh = new THREE.Mesh(new THREE.TubeGeometry(catCurve, 32, 0.035, 6, false), M.copperBus);
            transmissionGroup.add(catMesh);
        }

        group.add(transmissionGroup);

        // Roadway Thermoplastic Markings Network
        const roadMarkingsGroup = new THREE.Group();
        // Inbound lane center line
        const centerLine1 = new THREE.Mesh(new THREE.PlaneGeometry(160, 0.3), M.roadMarking);
        centerLine1.rotation.x = -Math.PI / 2;
        centerLine1.position.set(0, 0.07, 72);
        roadMarkingsGroup.add(centerLine1);

        // Pedestrian Crosswalk Zebra Stripes
        for (let z = -4; z <= 4; z += 1.4) {
            const stripe = new THREE.Mesh(new THREE.PlaneGeometry(0.7, 4.2), M.roadMarking);
            stripe.rotation.x = -Math.PI / 2;
            stripe.position.set(-52, 0.07, 72 + z);
            roadMarkingsGroup.add(stripe);
        }
        group.add(roadMarkingsGroup);

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

        // Two-Storey Structural Glass Curtain-Wall Corporate Lobby Entrance (East Facade)
        const lobbyGroup = new THREE.Group();
        lobbyGroup.name = "ExecutiveEntranceLobby";
        lobbyGroup.position.set(50.35, 4.8, 0);

        // Glass Curtain Wall
        const curtainGlass = new THREE.Mesh(new THREE.BoxGeometry(0.3, 8.5, 18), M.curtainGlass);
        curtainGlass.position.set(0, 0, 0);
        lobbyGroup.add(curtainGlass);

        // Structural Aluminum Mullions
        for (let mz = -8; mz <= 8; mz += 2.0) {
            const mullion = new THREE.Mesh(new THREE.BoxGeometry(0.35, 8.6, 0.08), M.facadeDark);
            mullion.position.set(0.05, 0, mz);
            lobbyGroup.add(mullion);
        }
        for (let my = -3.5; my <= 3.5; my += 2.2) {
            const hMullion = new THREE.Mesh(new THREE.BoxGeometry(0.35, 0.08, 18), M.facadeDark);
            hMullion.position.set(0.05, my, 0);
            lobbyGroup.add(hMullion);
        }

        // Entrance Portal Canopy & Glowing Brand Sign
        const entranceCanopy = new THREE.Mesh(new THREE.BoxGeometry(3.5, 0.3, 8), M.facadeDark);
        entranceCanopy.position.set(1.6, -0.6, 0);
        entranceCanopy.castShadow = true;
        lobbyGroup.add(entranceCanopy);

        // Glowing Datacenter Signage
        const brandSign = new THREE.Mesh(new THREE.BoxGeometry(0.1, 0.7, 7.5), M.facadeAccent);
        brandSign.position.set(3.4, 0.1, 0);
        lobbyGroup.add(brandSign);

        facadeGroup.add(lobbyGroup);

        // Logistics Loading Dock & 40ft Semi-Trailer (West Facade)
        const dockGroup = new THREE.Group();
        dockGroup.name = "LogisticsLoadingDock";
        dockGroup.position.set(-40.35, 0, -14);

        // Dual Industrial Sectional Roll-Up Doors
        [-5.5, 5.5].forEach((dz, idx) => {
            const doorFrame = new THREE.Mesh(new THREE.BoxGeometry(0.35, 4.6, 4.2), M.blastWall);
            doorFrame.position.set(0, 2.3, dz);
            const doorCurtain = new THREE.Mesh(new THREE.BoxGeometry(0.2, 4.2, 3.8), M.louvers);
            doorCurtain.position.set(-0.1, 2.3, dz);
            const bumperL = new THREE.Mesh(new THREE.BoxGeometry(0.4, 0.8, 0.25), M.craneTreads);
            bumperL.position.set(-0.3, 0.8, dz - 1.8);
            const bumperR = bumperL.clone();
            bumperR.position.set(-0.3, 0.8, dz + 1.8);
            dockGroup.add(doorFrame, doorCurtain, bumperL, bumperR);
        });

        // Docked 40ft Logistics Semi-Trailer Truck at Bay 1
        const truckGroup = new THREE.Group();
        truckGroup.name = "LogisticsSemiTrailerTruck";
        truckGroup.position.set(-9.5, 0, -8.5);

        // 40ft Shipping Container Trailer
        const trailer = new THREE.Mesh(new THREE.BoxGeometry(12.5, 3.8, 2.6), M.truckTrailer);
        trailer.position.set(0, 2.4, 0);
        trailer.castShadow = true;
        truckGroup.add(trailer);

        // Trailer Wheels (Dual Bogie Tandem)
        for (let w = -1; w <= 1; w += 2) {
            const wheel1 = new THREE.Mesh(new THREE.CylinderGeometry(0.5, 0.5, 0.4, 12), M.craneTreads);
            wheel1.rotation.x = Math.PI / 2;
            wheel1.position.set(4.2, 0.5, w * 1.1);
            const wheel2 = wheel1.clone();
            wheel2.position.set(5.5, 0.5, w * 1.1);
            truckGroup.add(wheel1, wheel2);
        }

        // Heavy Tractor Truck Cab
        const cab = new THREE.Mesh(new THREE.BoxGeometry(3.6, 3.4, 2.5), M.truckCab);
        cab.position.set(-8.2, 2.0, 0);
        cab.castShadow = true;
        const cabWindshield = new THREE.Mesh(new THREE.BoxGeometry(1.2, 1.2, 2.4), M.glass);
        cabWindshield.position.set(-9.5, 2.7, 0);
        truckGroup.add(cab, cabWindshield);

        dockGroup.add(truckGroup);
        facadeGroup.add(dockGroup);

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

        // NFPA 850 Reinforced Concrete Blast Separation Firewall
        const blastWall = new THREE.Mesh(new THREE.BoxGeometry(0.5, 6.5, 7.5), M.blastWall);
        blastWall.position.set(-5, 3.25, 0);
        blastWall.castShadow = true;
        subGroup.add(blastWall);

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

        // Bulk Fuel Storage Tanks & Reinforced Concrete Spill Bund
        const fuelSkid = new THREE.Group();
        fuelSkid.position.set(0, 0, 36);

        // Concrete Retention Spill Bund
        const bundWall1 = new THREE.Mesh(new THREE.BoxGeometry(16, 1.4, 0.4), M.blastWall);
        bundWall1.position.set(0, 0.9, -11);
        const bundWall2 = new THREE.Mesh(new THREE.BoxGeometry(16, 1.4, 0.4), M.blastWall);
        bundWall2.position.set(0, 0.9, 11);
        const bundWall3 = new THREE.Mesh(new THREE.BoxGeometry(0.4, 1.4, 22), M.blastWall);
        bundWall3.position.set(-8, 0.9, 0);
        const bundWall4 = new THREE.Mesh(new THREE.BoxGeometry(0.4, 1.4, 22), M.blastWall);
        bundWall4.position.set(8, 0.9, 0);
        fuelSkid.add(bundWall1, bundWall2, bundWall3, bundWall4);

        for (let t = -6; t <= 6; t += 12) {
            const tank = new THREE.Mesh(new THREE.CylinderGeometry(1.6, 1.6, 12.0, 16), M.fuelTank);
            tank.rotation.z = Math.PI / 2;
            tank.position.set(0, 2.0, t);
            tank.castShadow = true;
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
