// Main Application Controller & Three.js WebGL Engine for DC36-T3
// AAA Graphics Edition: Post-Processing, Cinematic Drone Tour & FPV Walkthrough

(function() {
    let scene, camera, renderer, controls, composer;
    let particles, modelsRef;
    let raycaster, mouse;
    let dirLight, hemiLight, rimLight, nightFloodlights = [];
    let currentLightingMode = 'day';
    let isBlackoutActive = false;

    // Cinematic Drone Tour Engine
    let isDroneTourActive = false;
    let droneSpline = null;
    let droneLookSpline = null;
    let droneTourProgress = 0;

    // First-Person Walkthrough (FPV)
    let isFPVActive = false;
    let fpvKeys = { forward: false, backward: false, left: false, right: false };
    let fpvVelocity = new THREE.Vector3();
    let fpvDirection = new THREE.Vector3();

    // Diagnostics Profiler
    let lastFpsTime = performance.now();
    let frameCount = 0;
    let currentFps = 60;

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
        scene.background = new THREE.Color(0xf8fafc);
        scene.fog = new THREE.FogExp2(0xf8fafc, 0.0012);

        // Camera Setup
        camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.5, 1200);
        camera.position.set(130, 105, 150);

        // WebGL Renderer with Shadows & Color Management
        renderer = new THREE.WebGLRenderer({ antialias: true, powerPreference: "high-performance" });
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
        renderer.shadowMap.enabled = true;
        renderer.shadowMap.type = THREE.PCFSoftShadowMap;
        renderer.toneMapping = THREE.ACESFilmicToneMapping;
        renderer.toneMappingExposure = 1.18;
        container.appendChild(renderer.domElement);

        // OrbitControls
        controls = new THREE.OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true;
        controls.dampingFactor = 0.05;
        controls.maxPolarAngle = Math.PI / 2 - 0.02;
        controls.minDistance = 2;
        controls.maxDistance = 450;
        controls.target.set(0, 10, 0);

        // Setup Lighting Architecture
        setupLighting();

        // Build 3D Models
        modelsRef = window.DC36_MODELS.buildDatacenterScene(scene);

        // Particle Systems
        particles = window.DC36_PARTICLES.init(scene);

        // 4D Timeline Engine (Defaults to Completed Campus Reality)
        const initState = window.DC36_TIMELINE.init(window.DC36_SCHEDULE, modelsRef, particles);

        // Gantt Chart & P6 Table
        window.DC36_GANTT.init(window.DC36_SCHEDULE, handleScheduleJump);

        if (initState) {
            updateHUD(initState);
            const slider = document.getElementById('timeline-slider');
            if (slider) slider.value = (initState.progressPercent * 10);
        }

        // Post-Processing Pipeline (EffectComposer + Bloom + FXAA)
        setupPostProcessing();

        // Setup Cinematic Drone Tour Spline Paths
        setupDroneSplines();

        // Setup Keyboard Handlers for FPV Walkthrough
        setupFPVControls();

        window.addEventListener('resize', onWindowResize);
        window.addEventListener('mousemove', onMouseMove);

        // Wire HUD UI Controls
        setupUI();

        // Start Rendering Loop
        animate();
    }

    let skyMesh = null;
    function updateSkyGradient(topColor, bottomColor) {
        try {
            const canvas = document.createElement('canvas');
            canvas.width = 32;
            canvas.height = 128;
            const ctx = canvas.getContext('2d');
            const grad = ctx.createLinearGradient(0, 0, 0, 128);
            grad.addColorStop(0, topColor);
            grad.addColorStop(1, bottomColor);
            ctx.fillStyle = grad;
            ctx.fillRect(0, 0, 32, 128);
            const texture = new THREE.CanvasTexture(canvas);
            texture.magFilter = THREE.LinearFilter;
            texture.minFilter = THREE.LinearFilter;

            if (!skyMesh) {
                const skyGeo = new THREE.SphereGeometry(650, 32, 16);
                const skyMat = new THREE.MeshBasicMaterial({ map: texture, side: THREE.BackSide, depthWrite: false });
                skyMesh = new THREE.Mesh(skyGeo, skyMat);
                scene.add(skyMesh);
            } else {
                skyMesh.material.map.dispose();
                skyMesh.material.map = texture;
                skyMesh.material.needsUpdate = true;
            }
        } catch(e) {
            console.warn("Sky dome gradient creation skipped", e);
        }
    }

    function setupLighting() {
        hemiLight = new THREE.HemisphereLight(0xffffff, 0xcbd5e1, 0.85);
        hemiLight.position.set(0, 100, 0);
        scene.add(hemiLight);

        dirLight = new THREE.DirectionalLight(0xffffff, 1.65);
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

        rimLight = new THREE.DirectionalLight(0x38bdf8, 0.45);
        rimLight.position.set(-100, 80, -90);
        scene.add(rimLight);

        // Perimeter Night Floodlights
        const mastPositions = [[-95, 20, -65], [95, 20, -65], [-95, 20, 65], [95, 20, 65]];
        mastPositions.forEach(p => {
            const flood = new THREE.PointLight(0xffeedd, 0.0, 120);
            flood.position.set(...p);
            scene.add(flood);
            nightFloodlights.push(flood);
        });

        // Interior Data Hall Glow
        const lightHall1 = new THREE.PointLight(0x00e5ff, 1.4, 45);
        lightHall1.position.set(5, 16.0, 0);
        scene.add(lightHall1);

        // Initial Sky Dome Gradient (Photorealistic architectural daylight & white horizon haze)
        updateSkyGradient('#38bdf8', '#f8fafc');
    }

    function setLightingMode(mode) {
        currentLightingMode = mode;
        if (mode === 'day') {
            updateSkyGradient('#38bdf8', '#f8fafc');
            scene.background = null;
            scene.fog.color.setHex(0xf8fafc);
            dirLight.color.setHex(0xffffff);
            dirLight.intensity = 1.65;
            dirLight.position.set(100, 140, 80);
            hemiLight.color.setHex(0xffffff);
            hemiLight.groundColor.setHex(0xcbd5e1);
            hemiLight.intensity = 0.85;
            nightFloodlights.forEach(f => f.intensity = 0.0);
        } else if (mode === 'dusk') {
            updateSkyGradient('#1e1b4b', '#ea580c');
            scene.background = null;
            scene.fog.color.setHex(0x7c2d12);
            dirLight.color.setHex(0xff7733);
            dirLight.intensity = 1.8;
            dirLight.position.set(140, 25, 40);
            hemiLight.intensity = 0.45;
            nightFloodlights.forEach(f => f.intensity = 0.5);
        } else if (mode === 'night') {
            updateSkyGradient('#020617', '#0f172a');
            scene.background = null;
            scene.fog.color.setHex(0x0a0c10);
            dirLight.intensity = 0.15;
            hemiLight.intensity = 0.15;
            nightFloodlights.forEach(f => f.intensity = 1.8);
        }
    }

    function setupPostProcessing() {
        if (typeof THREE.EffectComposer === 'undefined') return;

        composer = new THREE.EffectComposer(renderer);
        const renderPass = new THREE.RenderPass(scene, camera);
        composer.addPass(renderPass);

        // UnrealBloomPass: Tuned for Radiant Server LEDs, Neon Revealing Ribbons & Blackout Beacons
        if (typeof THREE.UnrealBloomPass !== 'undefined') {
            const bloomPass = new THREE.UnrealBloomPass(
                new THREE.Vector2(window.innerWidth, window.innerHeight),
                0.82, // strength
                0.60, // radius
                0.72  // threshold
            );
            composer.addPass(bloomPass);
        }

        // FXAAShader for Anti-Aliased Trusses
        if (typeof THREE.ShaderPass !== 'undefined' && typeof THREE.FXAAShader !== 'undefined') {
            const fxaaPass = new THREE.ShaderPass(THREE.FXAAShader);
            const pixelRatio = renderer.getPixelRatio();
            fxaaPass.material.uniforms['resolution'].value.x = 1 / (window.innerWidth * pixelRatio);
            fxaaPass.material.uniforms['resolution'].value.y = 1 / (window.innerHeight * pixelRatio);
            composer.addPass(fxaaPass);
        }
    }

    // 60-Second Automated Cinematic Drone Flight Spline
    function setupDroneSplines() {
        const cameraWaypoints = [
            new THREE.Vector3(140, 110, 150),  // High campus overview
            new THREE.Vector3(20, 45, 120),    // Sweeping past 110kV substation
            new THREE.Vector3(-15, 25, 80),    // Substation transformer close-up
            new THREE.Vector3(-110, 30, 20),   // 16 Generator farm flyby
            new THREE.Vector3(-45, 25, -50),   // Mechanical yard & fuel skids
            new THREE.Vector3(15, 38, -20),    // Rooftop chillers & cooling tower plume
            new THREE.Vector3(5, 15.5, -5),    // Entering Data Hall 1 White Space
            new THREE.Vector3(-12, 14.5, -14), // Cold aisle glide
            new THREE.Vector3(80, 50, 60),     // Ascending to exit
            new THREE.Vector3(140, 110, 150)   // Return to start
        ];
        droneSpline = new THREE.CatmullRomCurve3(cameraWaypoints, true);

        const lookWaypoints = [
            new THREE.Vector3(0, 10, 0),
            new THREE.Vector3(-10, 5, 45),
            new THREE.Vector3(-20, 4, 48),
            new THREE.Vector3(-66, 4, 0),
            new THREE.Vector3(-20, 8, 0),
            new THREE.Vector3(5, 20, 0),
            new THREE.Vector3(-10, 14, -14),
            new THREE.Vector3(-10, 14, -20),
            new THREE.Vector3(5, 12, 0),
            new THREE.Vector3(0, 10, 0)
        ];
        droneLookSpline = new THREE.CatmullRomCurve3(lookWaypoints, true);
    }

    function toggleDroneTour() {
        isDroneTourActive = !isDroneTourActive;
        const btn = document.getElementById('btn-drone-tour');
        if (btn) {
            btn.innerHTML = isDroneTourActive ? '<i class="fas fa-video-slash"></i> Exit Drone Tour' : '<i class="fas fa-video"></i> Drone Tour';
            btn.classList.toggle('audio-active', isDroneTourActive);
        }
        if (isDroneTourActive) {
            controls.enabled = false;
            droneTourProgress = 0;
        } else {
            controls.enabled = true;
            controls.target.set(0, 10, 0);
        }
    }

    function setupFPVControls() {
        window.addEventListener('keydown', (e) => {
            if (!isFPVActive) return;
            switch(e.code) {
                case 'KeyW': case 'ArrowUp': fpvKeys.forward = true; break;
                case 'KeyS': case 'ArrowDown': fpvKeys.backward = true; break;
                case 'KeyA': case 'ArrowLeft': fpvKeys.left = true; break;
                case 'KeyD': case 'ArrowRight': fpvKeys.right = true; break;
                case 'Escape': toggleFPVMode(false); break;
            }
        });

        window.addEventListener('keyup', (e) => {
            switch(e.code) {
                case 'KeyW': case 'ArrowUp': fpvKeys.forward = false; break;
                case 'KeyS': case 'ArrowDown': fpvKeys.backward = false; break;
                case 'KeyA': case 'ArrowLeft': fpvKeys.left = false; break;
                case 'KeyD': case 'ArrowRight': fpvKeys.right = false; break;
            }
        });
    }

    function toggleFPVMode(forceState) {
        isFPVActive = (typeof forceState !== 'undefined') ? forceState : !isFPVActive;
        const btn = document.getElementById('btn-fpv');
        const crosshair = document.getElementById('fpv-crosshair');
        if (btn) {
            btn.innerHTML = isFPVActive ? '<i class="fas fa-walking"></i> Exit FPV' : '<i class="fas fa-walking"></i> Data Hall FPV';
            btn.classList.toggle('audio-active', isFPVActive);
        }
        if (crosshair) crosshair.style.display = isFPVActive ? 'block' : 'none';

        if (isFPVActive) {
            if (isDroneTourActive) toggleDroneTour();
            // Automatically switch cutaway ON so roof doesn't block interior
            window.DC36_TIMELINE.setCutaway(true);
            const cutawayToggle = document.getElementById('toggle-cutaway');
            if (cutawayToggle) cutawayToggle.checked = true;

            // Teleport camera inside Data Hall 1 Cold Aisle
            camera.position.set(-10, 14.2, -10);
            controls.target.set(-10, 14.2, -18);
            controls.minDistance = 0.5;
            controls.maxDistance = 60;
        } else {
            controls.minDistance = 5;
            controls.maxDistance = 450;
            switchCamera('campus');
        }
    }

    function updateFPVMotion(dt) {
        if (!isFPVActive) return;

        const moveSpeed = 6.0; // m/s
        fpvDirection.z = Number(fpvKeys.forward) - Number(fpvKeys.backward);
        fpvDirection.x = Number(fpvKeys.right) - Number(fpvKeys.left);
        fpvDirection.normalize();

        const forward = new THREE.Vector3();
        camera.getWorldDirection(forward);
        forward.y = 0;
        forward.normalize();

        const side = new THREE.Vector3(-forward.z, 0, forward.x);

        if (fpvKeys.forward || fpvKeys.backward) {
            camera.position.addScaledVector(forward, fpvDirection.z * moveSpeed * dt);
            controls.target.addScaledVector(forward, fpvDirection.z * moveSpeed * dt);
        }
        if (fpvKeys.left || fpvKeys.right) {
            camera.position.addScaledVector(side, fpvDirection.x * moveSpeed * dt);
            controls.target.addScaledVector(side, fpvDirection.x * moveSpeed * dt);
        }

        // Clamp camera Y inside Data Hall level
        camera.position.y = 14.2;
        controls.target.y = 14.2;
    }

    function onWindowResize() {
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(window.innerWidth, window.innerHeight);
        if (composer) composer.setSize(window.innerWidth, window.innerHeight);
    }

    function onMouseMove(event) {
        mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
        mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;
    }

    function handleScheduleJump(timestamp, taskCode) {
        const state = window.DC36_TIMELINE.updateToTime(timestamp);
        updateHUD(state);
        window.DC36_GANTT.updateTime(timestamp);

        const slider = document.getElementById('timeline-slider');
        if (slider) slider.value = (state.progressPercent * 10);

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

        window.DC36_AUDIO.playSwitchgearClick();
        window.DC36_AUDIO.updateState(8, true);

        dirLight.intensity = 0.05;
        hemiLight.intensity = 0.05;
        const alertLight = new THREE.PointLight(0xff0033, 2.5, 90);
        alertLight.position.set(5, 18, 0);
        scene.add(alertLight);

        if (particles && particles.smoke) {
            particles.smoke.points.visible = true;
        }

        setTimeout(() => {
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
        function bindAction(el, fn) {
            if (!el) return;
            el.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                fn(e);
            });
            el.addEventListener('pointerdown', (e) => {
                e.stopPropagation();
            });
        }

        // Insulate all UI glass panels from OrbitControls pointer capture
        ['top-bar', 'left-panel', 'right-panel', 'bottom-bar', 'bottom-dock'].forEach(id => {
            const p = document.getElementById(id);
            if (p) {
                p.addEventListener('pointerdown', (e) => e.stopPropagation());
                p.addEventListener('mousedown', (e) => e.stopPropagation());
            }
        });

        const playBtn = document.getElementById('btn-play');
        const slider = document.getElementById('timeline-slider');
        const speedSel = document.getElementById('speed-select');
        const cutawayToggle = document.getElementById('toggle-cutaway');
        const cfdToggle = document.getElementById('toggle-cfd');
        const audioBtn = document.getElementById('btn-audio');
        const blackoutBtn = document.getElementById('btn-blackout');
        const lightingSelect = document.getElementById('lighting-select');
        const droneTourBtn = document.getElementById('btn-drone-tour');
        const fpvBtn = document.getElementById('btn-fpv');

        bindAction(playBtn, () => {
            const playing = window.DC36_TIMELINE.togglePlay();
            playBtn.innerHTML = playing ? '<i class="fas fa-pause"></i> Pause' : '<i class="fas fa-play"></i> Play';
        });

        if (slider) {
            slider.addEventListener('input', (e) => {
                const fraction = parseFloat(e.target.value) / 1000;
                const state = window.DC36_TIMELINE.updateToProgress(fraction);
                updateHUD(state);
                window.DC36_GANTT.updateTime(state.timestamp);
                window.DC36_AUDIO.updateState(state.activePhase, isBlackoutActive);
            });
        }

        if (speedSel) {
            speedSel.addEventListener('change', (e) => {
                window.DC36_TIMELINE.setSpeed(parseFloat(e.target.value));
            });
        }

        if (cutawayToggle) {
            cutawayToggle.addEventListener('change', (e) => {
                window.DC36_TIMELINE.setCutaway(e.target.checked);
            });
        }

        if (cfdToggle) {
            cfdToggle.addEventListener('change', (e) => {
                window.DC36_TIMELINE.setCFD(e.target.checked);
            });
        }

        bindAction(audioBtn, () => {
            const isMuted = window.DC36_AUDIO.toggleMute();
            audioBtn.innerHTML = isMuted ? '<i class="fas fa-volume-mute"></i> Sound OFF' : '<i class="fas fa-volume-up"></i> Sound ON';
            audioBtn.classList.toggle('audio-active', !isMuted);
        });

        bindAction(blackoutBtn, () => runBlackoutDrill());
        if (lightingSelect) lightingSelect.addEventListener('change', (e) => setLightingMode(e.target.value));
        bindAction(droneTourBtn, () => toggleDroneTour());
        bindAction(fpvBtn, () => toggleFPVMode());

        // Campus Reality vs 4D Construction Evolution Mode Handler
        let isRealityMode = true;
        const btnModeToggle = document.getElementById('btn-mode-toggle');
        const txtModeToggle = document.getElementById('txt-mode-toggle');
        const iconModeToggle = document.getElementById('icon-mode-toggle');
        if (btnModeToggle) {
            bindAction(btnModeToggle, () => {
                isRealityMode = !isRealityMode;
                if (isRealityMode) {
                    btnModeToggle.classList.add('active');
                    if (txtModeToggle) txtModeToggle.innerText = 'Reality';
                    if (iconModeToggle) iconModeToggle.className = 'fas fa-city';
                    const state = window.DC36_TIMELINE.setCampusMode('reality');
                    if (state) {
                        updateHUD(state);
                        window.DC36_GANTT.updateTime(state.timestamp);
                        window.DC36_AUDIO.updateState(state.activePhase, isBlackoutActive);
                        if (slider) slider.value = (state.progressPercent * 10);
                    }
                } else {
                    btnModeToggle.classList.remove('active');
                    if (txtModeToggle) txtModeToggle.innerText = '4D Evol.';
                    if (iconModeToggle) iconModeToggle.className = 'fas fa-hard-hat';
                    const state = window.DC36_TIMELINE.setCampusMode('construction');
                    if (state) {
                        updateHUD(state);
                        window.DC36_GANTT.updateTime(state.timestamp);
                        window.DC36_AUDIO.updateState(state.activePhase, isBlackoutActive);
                        if (slider) slider.value = 0;
                    }
                }
            });
        }

        document.querySelectorAll('.cam-btn').forEach(btn => {
            bindAction(btn, () => {
                if (isDroneTourActive) toggleDroneTour();
                if (isFPVActive) toggleFPVMode(false);
                switchCamera(btn.getAttribute('data-cam'));
            });
        });

        document.querySelectorAll('.mile-btn').forEach(btn => {
            bindAction(btn, () => {
                const code = btn.getAttribute('data-code');
                const state = window.DC36_TIMELINE.jumpToMilestone(code);
                updateHUD(state);
                window.DC36_GANTT.updateTime(state.timestamp);
                window.DC36_AUDIO.updateState(state.activePhase, isBlackoutActive);
                if (slider) slider.value = (state.progressPercent * 10);
                if (playBtn) playBtn.innerHTML = '<i class="fas fa-play"></i> Play';
            });
        });

        // Bottom Dock & Drawer Handlers
        const bottomDock = document.getElementById('bottom-dock');
        const btnToggleSchedule = document.getElementById('btn-toggle-schedule');
        const dockCloseBtn = document.getElementById('dock-close-btn');
        const tabGantt = document.getElementById('tab-btn-gantt');
        const tabTable = document.getElementById('tab-btn-table');
        const paneGantt = document.getElementById('dock-pane-gantt');
        const paneTable = document.getElementById('dock-pane-table');

        bindAction(btnToggleSchedule, () => {
            if (!bottomDock) return;
            bottomDock.classList.toggle('dock-open');
            const isOpen = bottomDock.classList.contains('dock-open');
            btnToggleSchedule.innerHTML = isOpen 
                ? '<i class="fas fa-times"></i> Close Schedule' 
                : '<i class="fas fa-calendar-alt"></i> P6 Schedule';
        });

        bindAction(dockCloseBtn, () => {
            if (!bottomDock) return;
            bottomDock.classList.remove('dock-open');
            if (btnToggleSchedule) {
                btnToggleSchedule.innerHTML = '<i class="fas fa-calendar-alt"></i> P6 Schedule';
            }
        });

        // Left & Right Collapsible Panels Handlers
        function toggleLeftPanel(e) {
            if (e) { e.preventDefault(); e.stopPropagation(); }
            const panel = document.getElementById('left-panel');
            if (!panel) return;
            const isCol = panel.classList.toggle('panel-collapsed');
            const btnTopTasks = document.getElementById('btn-top-tasks');
            if (btnTopTasks) {
                btnTopTasks.classList.toggle('active', !isCol);
            }
            // Auto-collapse opposite drawer on compact/split screens
            if (!isCol && window.innerWidth < 1100) {
                const right = document.getElementById('right-panel');
                if (right && !right.classList.contains('panel-collapsed')) {
                    right.classList.add('panel-collapsed');
                    const btnTopTelemetry = document.getElementById('btn-top-telemetry');
                    if (btnTopTelemetry) btnTopTelemetry.classList.remove('active');
                }
            }
        }
        window.toggleLeftPanel = toggleLeftPanel;

        function toggleRightPanel(e) {
            if (e) { e.preventDefault(); e.stopPropagation(); }
            const panel = document.getElementById('right-panel');
            if (!panel) return;
            const isCol = panel.classList.toggle('panel-collapsed');
            const btnTopTelemetry = document.getElementById('btn-top-telemetry');
            if (btnTopTelemetry) {
                btnTopTelemetry.classList.toggle('active', !isCol);
            }
            // Auto-collapse opposite drawer on compact/split screens
            if (!isCol && window.innerWidth < 1100) {
                const left = document.getElementById('left-panel');
                if (left && !left.classList.contains('panel-collapsed')) {
                    left.classList.add('panel-collapsed');
                    const btnTopTasks = document.getElementById('btn-top-tasks');
                    if (btnTopTasks) btnTopTasks.classList.remove('active');
                }
            }
        }
        window.toggleRightPanel = toggleRightPanel;

        const btnToggleLeft = document.getElementById('btn-toggle-left');
        const btnTopTasks = document.getElementById('btn-top-tasks');
        const btnCloseLeft = document.getElementById('btn-close-left');
        if (btnToggleLeft) bindAction(btnToggleLeft, toggleLeftPanel);
        if (btnTopTasks) bindAction(btnTopTasks, toggleLeftPanel);
        if (btnCloseLeft) bindAction(btnCloseLeft, toggleLeftPanel);

        const btnToggleRight = document.getElementById('btn-toggle-right');
        const btnTopTelemetry = document.getElementById('btn-top-telemetry');
        const btnCloseRight = document.getElementById('btn-close-right');
        if (btnToggleRight) bindAction(btnToggleRight, toggleRightPanel);
        if (btnTopTelemetry) bindAction(btnTopTelemetry, toggleRightPanel);
        if (btnCloseRight) bindAction(btnCloseRight, toggleRightPanel);

        if (tabGantt && tabTable) {
            bindAction(tabGantt, () => {
                tabGantt.classList.add('active');
                tabTable.classList.remove('active');
                paneGantt.style.display = 'block';
                paneTable.style.display = 'none';
            });

            bindAction(tabTable, () => {
                tabTable.classList.add('active');
                tabGantt.classList.remove('active');
                paneTable.style.display = 'block';
                paneGantt.style.display = 'none';
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

        document.getElementById('metric-mw').innerText = `${state.activeMW} MW`;
        document.getElementById('metric-concrete').innerText = `${state.concreteM3.toLocaleString()} m³`;
        document.getElementById('metric-racks').innerText = `${state.racksDeployed.toLocaleString()} / 1,200`;
        document.getElementById('metric-pue').innerText = state.currentPUE;

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

    function updateProfiler() {
        frameCount++;
        const now = performance.now();
        if (now - lastFpsTime >= 1000) {
            currentFps = frameCount;
            frameCount = 0;
            lastFpsTime = now;

            const fpsEl = document.getElementById('prof-fps');
            const callsEl = document.getElementById('prof-calls');
            const trisEl = document.getElementById('prof-tris');

            if (fpsEl) fpsEl.innerText = `${currentFps} FPS`;
            if (callsEl && renderer.info) callsEl.innerText = `${renderer.info.render.calls} Calls`;
            if (trisEl && renderer.info) trisEl.innerText = `${Math.floor(renderer.info.render.triangles / 1000)}k Tris`;
        }
    }

    function animate(now) {
        requestAnimationFrame(animate);

        const dt = 0.016;

        // Cinematic Drone Spline Update
        if (isDroneTourActive && droneSpline && droneLookSpline) {
            droneTourProgress += (dt / 60); // 60 seconds per loop
            if (droneTourProgress > 1) droneTourProgress = 0;

            const camPos = droneSpline.getPoint(droneTourProgress);
            const lookPos = droneLookSpline.getPoint(droneTourProgress);

            camera.position.copy(camPos);
            camera.lookAt(lookPos);
            controls.target.copy(lookPos);
        } else if (isFPVActive) {
            updateFPVMotion(dt);
            controls.update();
        } else {
            controls.update();
        }

        // Rotate Cooling Tower Fans
        if (window.DC36_COOLING_FANS) {
            window.DC36_COOLING_FANS.forEach(fan => {
                fan.rotation.y += 0.08;
            });
        }

        // Timeline Step
        const state = window.DC36_TIMELINE.tick(now);
        if (state) {
            updateHUD(state);
            window.DC36_GANTT.updateTime(state.timestamp);
            window.DC36_AUDIO.updateState(state.activePhase, isBlackoutActive);
            const slider = document.getElementById('timeline-slider');
            if (slider) slider.value = (state.progressPercent * 10);
            if (state.playbackFinished) {
                const playBtn = document.getElementById('btn-play');
                if (playBtn) playBtn.innerHTML = '<i class="fas fa-play"></i> Play';
            }
        }

        // Update Particle Systems
        if (particles) {
            particles.update(dt);
        }

        // Update Render Profiler
        updateProfiler();

        // Render via EffectComposer (Bloom + FXAA) or fallback to WebGLRenderer
        if (composer) {
            composer.render();
        } else {
            renderer.render(scene, camera);
        }
    }

    window.addEventListener('DOMContentLoaded', init);
})();
