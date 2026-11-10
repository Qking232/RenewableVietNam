// Main Application Controller & Three.js WebGL Engine for DC36-T3
// Institutional Mission-Critical 4D Digital Twin Orchestrator

(function() {
    let scene, camera, renderer, controls;
    let particles, modelsRef;
    let raycaster, mouse;
    let dirLight, hemiLight, rimLight, nightFloodlights = [];
    let currentLightingMode = 'day';
    let isBlackoutActive = false;

    const cameraPresets = {
        campus: { pos: [130, 105, 150], target: [0, 10, 0] },
        substation: { pos: [-15, 30, 95], target: [-10, 5, 45] },
        generators: { pos: [-115, 32, 10], target: [-65, 5, 0] },
        rooftop: { pos: [25, 52, 40], target: [5, 20, 0] },
        whitespace: { pos: [-12, 16.5, -7], target: [-12, 14.5, -14] }
    };

    function init() {
        const container = document.getElementById('webgl-container');

        // Scene Setup
        scene = new THREE.Scene();
        scene.background = new THREE.Color(0x0a0c10);
        scene.fog = new THREE.FogExp2(0x0a0c10, 0.0035);

        // Camera Setup
        camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.5, 1000);
        camera.position.set(130, 105, 150);

        // WebGL Renderer with Shadows & Color Management
        renderer = new THREE.WebGLRenderer({ antialias: true, powerPreference: "high-performance" });
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
        renderer.shadowMap.enabled = true;
        renderer.shadowMap.type = THREE.PCFSoftShadowMap;
        renderer.toneMapping = THREE.ACESFilmicToneMapping;
        renderer.toneMappingExposure = 1.15;
        container.appendChild(renderer.domElement);

        // OrbitControls
        controls = new THREE.OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true;
        controls.dampingFactor = 0.05;
        controls.maxPolarAngle = Math.PI / 2 - 0.02; // Keep above ground plane
        controls.minDistance = 5;
        controls.maxDistance = 400;
        controls.target.set(0, 10, 0);

        // Lighting Architecture (Day / Dusk / Night)
        setupLighting();

        // Build 3D Datacenter Evolutionary Meshes
        modelsRef = window.DC36_MODELS.buildDatacenterScene(scene);

        // Initialize Particle Systems (Cooling Steam, CFD Airflow, Generator Smoke)
        particles = window.DC36_PARTICLES.init(scene);

        // Initialize 4D Timeline Engine with P6 Schedule Data
        window.DC36_TIMELINE.init(window.DC36_SCHEDULE, modelsRef, particles);

        // Initialize Interactive Gantt Timeline & P6 Task Table
        window.DC36_GANTT.init(window.DC36_SCHEDULE, handleScheduleJump);

        // Raycasting for Interactive Equipment Inspection
        raycaster = new THREE.Raycaster();
        mouse = new THREE.Vector2();

        window.addEventListener('resize', onWindowResize);
        window.addEventListener('mousemove', onMouseMove);
        window.addEventListener('click', onClick);

        // Wire HUD UI Controls, Audio, Lighting & Dock
        setupUI();

        // Start Rendering Loop
        animate();
    }

    function setupLighting() {
        // Ambient Hemisphere Light
        hemiLight = new THREE.HemisphereLight(0xddeeff, 0x1a202c, 0.65);
        hemiLight.position.set(0, 100, 0);
        scene.add(hemiLight);

        // Primary Directional Sunlight with Soft Shadows
        dirLight = new THREE.DirectionalLight(0xfffaed, 1.4);
        dirLight.position.set(100, 140, 80);
        dirLight.castShadow = true;
        dirLight.shadow.mapSize.width = 2048;
        dirLight.shadow.mapSize.height = 2048;
        dirLight.shadow.camera.near = 10;
        dirLight.shadow.camera.far = 400;
        const d = 130;
        dirLight.shadow.camera.left = -d;
        dirLight.shadow.camera.right = d;
        dirLight.shadow.camera.top = d;
        dirLight.shadow.camera.bottom = -d;
        dirLight.shadow.bias = -0.0005;
        scene.add(dirLight);

        // Secondary Soft Blue Rim Light
        rimLight = new THREE.DirectionalLight(0x38bdf8, 0.4);
        rimLight.position.set(-100, 80, -90);
        scene.add(rimLight);

        // Perimeter Night Security High-Mast Floodlights
        const mastPositions = [
            [-95, 20, -65], [95, 20, -65],
            [-95, 20, 65], [95, 20, 65]
        ];
        mastPositions.forEach(p => {
            const flood = new THREE.PointLight(0xffeedd, 0.0, 120);
            flood.position.set(...p);
            scene.add(flood);
            nightFloodlights.push(flood);
        });

        // Interior Data Hall Point Light
        const lightHall1 = new THREE.PointLight(0x00e5ff, 1.2, 45);
        lightHall1.position.set(5, 16.0, 0);
        scene.add(lightHall1);
    }

    function setLightingMode(mode) {
        currentLightingMode = mode;
        if (mode === 'day') {
            scene.background.setHex(0x0a0c10);
            scene.fog.color.setHex(0x0a0c10);
            dirLight.color.setHex(0xfffaed);
            dirLight.intensity = 1.4;
            dirLight.position.set(100, 140, 80);
            hemiLight.intensity = 0.65;
            nightFloodlights.forEach(f => f.intensity = 0.0);
        } else if (mode === 'dusk') {
            scene.background.setHex(0x1a0f1e);
            scene.fog.color.setHex(0x1a0f1e);
            dirLight.color.setHex(0xff7733);
            dirLight.intensity = 1.7;
            dirLight.position.set(140, 25, 40); // Low sun angle
            hemiLight.intensity = 0.4;
            nightFloodlights.forEach(f => f.intensity = 0.4);
        } else if (mode === 'night') {
            scene.background.setHex(0x030508);
            scene.fog.color.setHex(0x030508);
            dirLight.intensity = 0.15;
            hemiLight.intensity = 0.12;
            nightFloodlights.forEach(f => f.intensity = 1.8);
        }
    }

    function onWindowResize() {
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(window.innerWidth, window.innerHeight);
    }

    function onMouseMove(event) {
        mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
        mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;
    }

    function onClick() {
        raycaster.setFromCamera(mouse, camera);
        const intersects = raycaster.intersectObjects(modelsRef.root.children, true);

        if (intersects.length > 0) {
            let obj = intersects[0].object;
            while (obj.parent && obj.parent !== modelsRef.root && (!obj.name || obj.name.startsWith("Mesh"))) {
                obj = obj.parent;
            }
            if (obj && obj.name && !obj.name.startsWith("Mesh")) {
                showInspectionHUD(obj.name);
            }
        }
    }

    function showInspectionHUD(name) {
        const hud = document.getElementById('inspection-card');
        const title = document.getElementById('insp-title');
        const spec = document.getElementById('insp-spec');
        const wbs = document.getElementById('insp-wbs');
        const status = document.getElementById('insp-status');
        if (!hud) return;

        hud.style.display = 'block';
        title.innerText = name.replace(/_/g, " ");

        if (name.includes("Transformer")) {
            spec.innerText = "Rating: 45MVA 110kV/22kV Oil-Immersed Step-Down. Redundancy: 2x 100% Dual Utility Feeds.";
            wbs.innerText = "WBS 5.1 Substation & HV/MV (Act A5110)";
            status.innerText = "Commissioned & Energized via 110kV Ring";
        } else if (name.includes("Genset")) {
            spec.innerText = "Rating: 2.5MVA Standby Diesel Generator. 16 Units N+2 Topology with Spring Vibration Isolators.";
            wbs.innerText = "WBS 5.2 Emergency Generator Farm (Act A5220)";
            status.innerText = "Black-Start Tested (<10s ATS Transfer)";
        } else if (name.includes("Chiller")) {
            spec.innerText = "Rating: 1200 RT Centrifugal Water-Cooled Chiller (6 units N+2). Eco-friendly R-1233zd refrigerant.";
            wbs.innerText = "WBS 5.3 Central Chilled Water Plant (Act A5310)";
            status.innerText = "Lead-Lag Dynamically Staged";
        } else if (name.includes("CoolingTower")) {
            spec.innerText = "Induced-Draft Counter-Flow Fiberglass Cooling Tower with Variable Speed EC Fans.";
            wbs.innerText = "WBS 5.3 Mechanical (Act A5330)";
            status.innerText = "Continuous Wet-Bulb Heat Rejection";
        } else if (name.includes("DataHall")) {
            spec.innerText = "Capacity: 9MW IT Load per Hall (36MW Campus). 300 Racks @ 12kW-30kW High-Density HAC.";
            wbs.innerText = "WBS 5.4 White Space Fit-Out (Act A5470)";
            status.innerText = "IST 36MW Full-Load Soak Passed";
        } else if (name.includes("LoadBank")) {
            spec.innerText = "Rating: 4.5MW Mobile Resistive-Reactive 0.8PF Testing Load Bank (36MW Cluster).";
            wbs.innerText = "WBS 6.4 Integrated Systems Testing (Act A6410)";
            status.innerText = "IST Cx Level 5 Validation Complete";
        } else {
            spec.innerText = "Tier III Hyperscale Engineered BIM LOD 400 Structural/MEP Element.";
            wbs.innerText = "DC36-T3 Standard Architecture";
            status.innerText = "Quality Assured / FQC Verified";
        }
    }

    function handleScheduleJump(timestamp, taskCode) {
        const state = window.DC36_TIMELINE.updateToTime(timestamp);
        updateHUD(state);
        window.DC36_GANTT.updateTime(timestamp);

        const slider = document.getElementById('timeline-slider');
        if (slider) slider.value = (state.progressPercent * 10);

        // Automatically point camera to corresponding equipment area
        if (taskCode.startsWith('A51')) switchCamera('substation');
        else if (taskCode.startsWith('A52')) switchCamera('generators');
        else if (taskCode.startsWith('A53')) switchCamera('rooftop');
        else if (taskCode.startsWith('A54')) switchCamera('whitespace');
        else if (taskCode.startsWith('A41')) switchCamera('campus');
        else if (taskCode.startsWith('A64')) switchCamera('generators');
    }

    function runBlackoutDrill() {
        if (isBlackoutActive) return;
        isBlackoutActive = true;
        const banner = document.getElementById('blackout-banner');
        if (banner) banner.style.display = 'flex';

        // Play switchgear click & initiate generator rumble
        window.DC36_AUDIO.playSwitchgearClick();
        window.DC36_AUDIO.updateState(8, true);

        // Flash lights down to emergency red
        dirLight.intensity = 0.05;
        hemiLight.intensity = 0.05;
        const alertLight = new THREE.PointLight(0xff0033, 2.5, 90);
        alertLight.position.set(5, 18, 0);
        scene.add(alertLight);

        // Turn on generator exhaust smoke
        if (particles && particles.smoke) {
            particles.smoke.points.visible = true;
        }

        setTimeout(() => {
            // After 6 seconds, ATS transfers to 16 generators, restoring full power
            window.DC36_AUDIO.playSwitchgearClick();
            scene.remove(alertLight);
            setLightingMode(currentLightingMode);
            window.DC36_AUDIO.updateState(8, false);

            if (banner) {
                banner.innerHTML = '<i class="fas fa-check-circle"></i> ATS Transfer Succeeded in 6.8s &bull; 16 Diesel Gensets Online &bull; 0ms IT Drop';
                setTimeout(() => {
                    banner.style.display = 'none';
                    banner.innerHTML = '<i class="fas fa-exclamation-triangle"></i> Grid Blackout Initiated &bull; Simulating ATS Failover to 16 Gensets...';
                    isBlackoutActive = false;
                }, 4000);
            }
        }, 6000);
    }

    function setupUI() {
        const playBtn = document.getElementById('btn-play');
        const slider = document.getElementById('timeline-slider');
        const speedSel = document.getElementById('speed-select');
        const cutawayToggle = document.getElementById('toggle-cutaway');
        const cfdToggle = document.getElementById('toggle-cfd');
        const audioBtn = document.getElementById('btn-audio');
        const blackoutBtn = document.getElementById('btn-blackout');
        const lightingSelect = document.getElementById('lighting-select');

        // Play/Pause
        playBtn.addEventListener('click', () => {
            const playing = window.DC36_TIMELINE.togglePlay();
            playBtn.innerHTML = playing ? '<i class="fas fa-pause"></i> Pause' : '<i class="fas fa-play"></i> Play';
        });

        // Timeline Slider
        slider.addEventListener('input', (e) => {
            const fraction = parseFloat(e.target.value) / 1000;
            const state = window.DC36_TIMELINE.updateToProgress(fraction);
            updateHUD(state);
            window.DC36_GANTT.updateTime(state.timestamp);
            window.DC36_AUDIO.updateState(state.activePhase, isBlackoutActive);
        });

        // Playback Speed
        speedSel.addEventListener('change', (e) => {
            window.DC36_TIMELINE.setSpeed(parseFloat(e.target.value));
        });

        // Cutaway Toggle
        cutawayToggle.addEventListener('change', (e) => {
            window.DC36_TIMELINE.setCutaway(e.target.checked);
        });

        // CFD Airflow Toggle
        cfdToggle.addEventListener('change', (e) => {
            window.DC36_TIMELINE.setCFD(e.target.checked);
        });

        // Procedural Audio Synthesizer Toggle
        audioBtn.addEventListener('click', () => {
            const isMuted = window.DC36_AUDIO.toggleMute();
            audioBtn.innerHTML = isMuted ? '<i class="fas fa-volume-mute"></i> Sound OFF' : '<i class="fas fa-volume-up"></i> Sound ON';
            audioBtn.classList.toggle('audio-active', !isMuted);
        });

        // Blackout Simulation Button
        if (blackoutBtn) {
            blackoutBtn.addEventListener('click', runBlackoutDrill);
        }

        // Lighting Mode Selector
        if (lightingSelect) {
            lightingSelect.addEventListener('change', (e) => {
                setLightingMode(e.target.value);
            });
        }

        // Camera Preset Buttons
        document.querySelectorAll('.cam-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                const targetKey = btn.getAttribute('data-cam');
                switchCamera(targetKey);
            });
        });

        // Milestone Quick-Jump Buttons
        document.querySelectorAll('.mile-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                const code = btn.getAttribute('data-code');
                const state = window.DC36_TIMELINE.jumpToMilestone(code);
                updateHUD(state);
                window.DC36_GANTT.updateTime(state.timestamp);
                window.DC36_AUDIO.updateState(state.activePhase, isBlackoutActive);
                slider.value = (state.progressPercent * 10);
            });
        });

        // Collapsible Bottom Dock Tabs & Toggle
        const dockToggleBtn = document.getElementById('dock-toggle-btn');
        const bottomDock = document.getElementById('bottom-dock');
        const tabGantt = document.getElementById('tab-btn-gantt');
        const tabTable = document.getElementById('tab-btn-table');
        const paneGantt = document.getElementById('dock-pane-gantt');
        const paneTable = document.getElementById('dock-pane-table');

        if (dockToggleBtn && bottomDock) {
            dockToggleBtn.addEventListener('click', () => {
                bottomDock.classList.toggle('dock-collapsed');
                const isCollapsed = bottomDock.classList.contains('dock-collapsed');
                dockToggleBtn.innerHTML = isCollapsed ? '<i class="fas fa-chevron-up"></i> Expand Dock' : '<i class="fas fa-chevron-down"></i> Collapse';
            });
        }

        if (tabGantt && tabTable) {
            tabGantt.addEventListener('click', () => {
                tabGantt.classList.add('active');
                tabTable.classList.remove('active');
                paneGantt.style.display = 'block';
                paneTable.style.display = 'none';
            });

            tabTable.addEventListener('click', () => {
                tabTable.classList.add('active');
                tabGantt.classList.remove('active');
                paneTable.style.display = 'block';
                paneGantt.style.display = 'none';
            });
        }

        // Close Inspection Card
        const closeInsp = document.getElementById('close-insp');
        if (closeInsp) {
            closeInsp.addEventListener('click', () => {
                document.getElementById('inspection-card').style.display = 'none';
            });
        }
    }

    function switchCamera(presetKey) {
        const preset = cameraPresets[presetKey];
        if (!preset) return;

        const startPos = camera.position.clone();
        const startTarget = controls.target.clone();
        const endPos = new THREE.Vector3(...preset.pos);
        const endTarget = new THREE.Vector3(...preset.target);

        let t = 0;
        const dur = 40;
        function lerpCam() {
            t++;
            const p = t / dur;
            const ease = p < 0.5 ? 2 * p * p : -1 + (4 - 2 * p) * p;

            camera.position.lerpVectors(startPos, endPos, ease);
            controls.target.lerpVectors(startTarget, endTarget, ease);
            controls.update();

            if (t < dur) {
                requestAnimationFrame(lerpCam);
            }
        }
        lerpCam();
    }

    function updateHUD(state) {
        if (!state) return;

        document.getElementById('hud-date').innerText = state.dateString;
        document.getElementById('hud-days').innerText = `Day ${state.elapsedDays} of ${state.totalDays}`;
        document.getElementById('hud-progress').innerText = `${state.progressPercent}%`;
        document.getElementById('hud-progress-bar').style.width = `${state.progressPercent}%`;
        document.getElementById('hud-phase').innerText = `Phase ${state.activePhase}: ${state.phaseName}`;

        // Metrics
        document.getElementById('metric-mw').innerText = `${state.activeMW} MW`;
        document.getElementById('metric-concrete').innerText = `${state.concreteM3.toLocaleString()} m³`;
        document.getElementById('metric-racks').innerText = `${state.racksDeployed.toLocaleString()} / 1,200`;
        document.getElementById('metric-pue').innerText = state.currentPUE;

        // Active Tasks Feed
        const taskListEl = document.getElementById('active-tasks-list');
        if (taskListEl) {
            if (state.activeTasks.length === 0) {
                taskListEl.innerHTML = '<div class="task-item empty">Phase Milestone Rest Period</div>';
            } else {
                taskListEl.innerHTML = state.activeTasks.slice(0, 5).map(task => `
                    <div class="task-item ${task.is_critical ? 'critical' : ''}">
                        <div class="task-header">
                            <span class="task-code">${task.code}</span>
                            <span class="task-wbs">${task.wbs_code}</span>
                            ${task.is_critical ? '<span class="crit-badge">CRITICAL</span>' : ''}
                        </div>
                        <div class="task-name">${task.name}</div>
                        <div class="task-duration">${task.duration} working days</div>
                    </div>
                `).join('');
            }
        }
    }

    function animate(now) {
        requestAnimationFrame(animate);

        controls.update();

        // Rotate Cooling Tower Fans if Chilled Water / COD active
        if (window.DC36_COOLING_FANS) {
            window.DC36_COOLING_FANS.forEach(fan => {
                fan.rotation.y += 0.08;
            });
        }

        // Advance 4D Timeline State if playing
        const state = window.DC36_TIMELINE.tick(now);
        if (state) {
            updateHUD(state);
            window.DC36_GANTT.updateTime(state.timestamp);
            window.DC36_AUDIO.updateState(state.activePhase, isBlackoutActive);
            const slider = document.getElementById('timeline-slider');
            if (slider) slider.value = (state.progressPercent * 10);
        }

        // Update Particle Systems
        if (particles) {
            particles.update(0.016);
        }

        renderer.render(scene, camera);
    }

    window.addEventListener('DOMContentLoaded', init);
})();
