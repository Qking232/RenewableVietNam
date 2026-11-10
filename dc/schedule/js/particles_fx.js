// Visual Effects, CFD Airflow Simulation & Particle Systems for DC36-T3
(function() {
    window.DC36_PARTICLES = {};

    // 1. Cooling Tower Vapor Steam System
    function createCoolingTowerSteam(scene) {
        const count = 300;
        const geo = new THREE.BufferGeometry();
        const positions = new Float32Array(count * 3);
        const velocities = new Float32Array(count * 3);
        const lifetimes = new Float32Array(count);

        // 6 cooling tower top centers: X = 5, Y = 23.5, Z from -18 to 18
        const towerZ = [-18, -10.8, -3.6, 3.6, 10.8, 18];

        for (let i = 0; i < count; i++) {
            const tIdx = i % 6;
            const tz = towerZ[tIdx];

            positions[i * 3 + 0] = 5 + (Math.random() - 0.5) * 2.2;
            positions[i * 3 + 1] = 23.6 + Math.random() * 5.0;
            positions[i * 3 + 2] = tz + (Math.random() - 0.5) * 2.2;

            velocities[i * 3 + 0] = (Math.random() - 0.5) * 0.08 + 0.04;
            velocities[i * 3 + 1] = 0.08 + Math.random() * 0.09;
            velocities[i * 3 + 2] = (Math.random() - 0.5) * 0.08;

            lifetimes[i] = Math.random();
        }

        geo.setAttribute('position', new THREE.BufferAttribute(positions, 3));

        // Create round soft sprite texture procedurally
        const canvas = document.createElement('canvas');
        canvas.width = 64;
        canvas.height = 64;
        const ctx = canvas.getContext('2d');
        const grad = ctx.createRadialGradient(32, 32, 0, 32, 32, 32);
        grad.addColorStop(0, 'rgba(255,255,255,0.7)');
        grad.addColorStop(0.4, 'rgba(210,235,255,0.3)');
        grad.addColorStop(1, 'rgba(255,255,255,0)');
        ctx.fillStyle = grad;
        ctx.fillRect(0, 0, 64, 64);
        const tex = new THREE.CanvasTexture(canvas);

        const mat = new THREE.PointsMaterial({
            size: 3.5,
            map: tex,
            transparent: true,
            opacity: 0.45,
            depthWrite: false,
            blending: THREE.NormalBlending
        });

        const points = new THREE.Points(geo, mat);
        points.name = "CoolingTowerSteam";
        points.visible = false;
        scene.add(points);

        return {
            points,
            update: function(dt) {
                if (!points.visible) return;
                const pos = points.geometry.attributes.position.array;
                for (let i = 0; i < count; i++) {
                    const idx3 = i * 3;
                    pos[idx3 + 0] += velocities[idx3 + 0];
                    pos[idx3 + 1] += velocities[idx3 + 1];
                    pos[idx3 + 2] += velocities[idx3 + 2];

                    if (pos[idx3 + 1] > 32.0) {
                        const tIdx = i % 6;
                        pos[idx3 + 0] = 5 + (Math.random() - 0.5) * 2.2;
                        pos[idx3 + 1] = 23.6;
                        pos[idx3 + 2] = towerZ[tIdx] + (Math.random() - 0.5) * 2.2;
                    }
                }
                points.geometry.attributes.position.needsUpdate = true;
            }
        };
    }

    // 2. CFD Thermal Airflow Particles (Cold Aisle Blue vs Hot Aisle Red)
    function createCFDAirflowSystem(scene) {
        const count = 600;
        const geo = new THREE.BufferGeometry();
        const positions = new Float32Array(count * 3);
        const colors = new Float32Array(count * 3);
        const speeds = new Float32Array(count);

        // 4 Data Halls on Level 2 (Y: 13.2m to 16.5m)
        const quadCenters = [
            { x: -16 + 5, z: -14 },
            { x: 16 + 5, z: -14 },
            { x: -16 + 5, z: 14 },
            { x: 16 + 5, z: 14 }
        ];

        for (let i = 0; i < count; i++) {
            const isCold = (i % 2 === 0);
            const quad = quadCenters[i % 4];
            const podOffsetZ = (-7.2 + Math.floor((i % 12) / 4) * 7.2);

            const px = quad.x + (Math.random() - 0.5) * 16;
            const py = 13.2 + Math.random() * 3.0;
            // Cold aisles are at outer edges (offset +/- 1.8), hot aisles at pod center
            const pz = quad.z + podOffsetZ + (isCold ? (Math.random() > 0.5 ? 1.8 : -1.8) : (Math.random() - 0.5) * 0.8);

            positions[i * 3 + 0] = px;
            positions[i * 3 + 1] = py;
            positions[i * 3 + 2] = pz;

            // Cold is Cyan/Blue (0, 0.7, 1.0), Hot is Orange/Red (1.0, 0.25, 0.05)
            if (isCold) {
                colors[i * 3 + 0] = 0.0;
                colors[i * 3 + 1] = 0.75;
                colors[i * 3 + 2] = 1.0;
            } else {
                colors[i * 3 + 0] = 1.0;
                colors[i * 3 + 1] = 0.3;
                colors[i * 3 + 2] = 0.05;
            }

            speeds[i] = 0.04 + Math.random() * 0.05;
        }

        geo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
        geo.setAttribute('color', new THREE.BufferAttribute(colors, 3));

        const mat = new THREE.PointsMaterial({
            size: 0.35,
            vertexColors: true,
            transparent: true,
            opacity: 0.85,
            depthWrite: false,
            blending: THREE.AdditiveBlending
        });

        const points = new THREE.Points(geo, mat);
        points.name = "CFD_Airflow";
        points.visible = false;
        scene.add(points);

        return {
            points,
            update: function() {
                if (!points.visible) return;
                const pos = points.geometry.attributes.position.array;
                for (let i = 0; i < count; i++) {
                    const isCold = (i % 2 === 0);
                    if (isCold) {
                        // Cold air flows upward from floor tiles into rack intake
                        pos[i * 3 + 1] += speeds[i];
                        if (pos[i * 3 + 1] > 15.6) {
                            pos[i * 3 + 1] = 13.2;
                        }
                    } else {
                        // Hot air rises faster inside contained hot aisle into ceiling return
                        pos[i * 3 + 1] += speeds[i] * 1.5;
                        if (pos[i * 3 + 1] > 16.5) {
                            pos[i * 3 + 1] = 13.5;
                        }
                    }
                }
                points.geometry.attributes.position.needsUpdate = true;
            }
        };
    }

    // 3. Generator Exhaust Smoke Puffs
    function createGeneratorSmoke(scene) {
        const count = 120;
        const geo = new THREE.BufferGeometry();
        const positions = new Float32Array(count * 3);

        for (let i = 0; i < count; i++) {
            positions[i * 3 + 0] = -68 + (Math.random() - 0.5) * 6;
            positions[i * 3 + 1] = 7.0 + Math.random() * 4;
            positions[i * 3 + 2] = -28 + (i % 8) * 8 + (Math.random() - 0.5) * 1.5;
        }

        geo.setAttribute('position', new THREE.BufferAttribute(positions, 3));

        const mat = new THREE.PointsMaterial({
            size: 1.2,
            color: 0x555555,
            transparent: true,
            opacity: 0.35,
            depthWrite: false
        });

        const points = new THREE.Points(geo, mat);
        points.name = "GeneratorSmoke";
        points.visible = false;
        scene.add(points);

        return {
            points,
            update: function() {
                if (!points.visible) return;
                const pos = points.geometry.attributes.position.array;
                for (let i = 0; i < count; i++) {
                    pos[i * 3 + 1] += 0.05;
                    pos[i * 3 + 0] += 0.02;
                    if (pos[i * 3 + 1] > 13.0) {
                        pos[i * 3 + 1] = 7.0;
                    }
                }
                points.geometry.attributes.position.needsUpdate = true;
            }
        };
    }

    window.DC36_PARTICLES.init = function(scene) {
        const steam = createCoolingTowerSteam(scene);
        const cfd = createCFDAirflowSystem(scene);
        const smoke = createGeneratorSmoke(scene);

        return {
            steam,
            cfd,
            smoke,
            update: function(dt) {
                steam.update(dt);
                cfd.update(dt);
                smoke.update(dt);
            }
        };
    };
})();
