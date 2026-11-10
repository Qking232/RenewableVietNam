// 4D Timeline Engine & Construction State Machine for DC36-T3 Hyperscale Datacenter
(function() {
    window.DC36_TIMELINE = {};

    let schedule = null;
    let models = null;
    let particles = null;

    let currentTimestamp = 0;
    let isPlaying = false;
    let playbackSpeed = 2.0; // 1 day per X seconds
    let lastAnimTime = 0;
    let cutawayEnabled = false;
    let cfdEnabled = false;

    window.DC36_TIMELINE.init = function(schedData, modelRefs, particleRefs) {
        schedule = schedData;
        models = modelRefs;
        particles = particleRefs;

        currentTimestamp = schedule.min_timestamp;
        updateState(currentTimestamp);
    };

    window.DC36_TIMELINE.setCutaway = function(enabled) {
        cutawayEnabled = enabled;
        applyCutawayState();
    };

    window.DC36_TIMELINE.setCFD = function(enabled) {
        cfdEnabled = enabled;
        if (particles && particles.cfd) {
            particles.cfd.points.visible = cfdEnabled;
        }
    };

    function applyCutawayState() {
        if (!models || !models.p4_envelope) return;
        const facadeGroup = models.p4_envelope.getObjectByName("BuildingFacade");
        const roof = models.p4_envelope.getObjectByName("RoofMembrane");

        if (cutawayEnabled) {
            if (roof) roof.visible = false;
            if (facadeGroup) {
                facadeGroup.traverse(child => {
                    if (child.isMesh) {
                        child.material.transparent = true;
                        child.material.opacity = 0.18;
                        child.material.depthWrite = false;
                    }
                });
            }
        } else {
            if (roof) roof.visible = true;
            if (facadeGroup) {
                facadeGroup.traverse(child => {
                    if (child.isMesh) {
                        child.material.transparent = false;
                        child.material.opacity = 1.0;
                        child.material.depthWrite = true;
                    }
                });
            }
        }
    }

    function updateState(timestamp) {
        currentTimestamp = Math.max(schedule.min_timestamp, Math.min(schedule.max_timestamp, timestamp));
        const totalSpan = schedule.max_timestamp - schedule.min_timestamp;
        const currentProgress = (currentTimestamp - schedule.min_timestamp) / totalSpan;

        let activeTasks = [];
        let completedTasks = 0;
        let activePhase = 1;

        // Evaluate all P6 activities against current timestamp
        schedule.activities.forEach(act => {
            if (currentTimestamp >= act.finishTimestamp) {
                completedTasks++;
            } else if (currentTimestamp >= act.startTimestamp && currentTimestamp < act.finishTimestamp) {
                activeTasks.push(act);
            }
        });

        // Determine active Phase (1 to 8)
        for (let i = 0; i < schedule.phases.length; i++) {
            const p = schedule.phases[i];
            const pStart = new Date(p.start_date).getTime();
            const pFinish = new Date(p.finish_date).getTime();
            if (currentTimestamp >= pStart) {
                activePhase = p.id;
            }
        }

        // Metrics Computation
        // 1. Concrete Poured m3 (0 -> 24,000 m3 across Phases 1-4)
        let concreteM3 = 0;
        if (activePhase === 1) concreteM3 = Math.floor(currentProgress * 5000);
        else if (activePhase === 2) concreteM3 = 5000 + Math.floor((currentProgress - 0.2) * 20000);
        else if (activePhase === 3) concreteM3 = 14000 + Math.floor((currentProgress - 0.35) * 30000);
        else concreteM3 = 24000;
        concreteM3 = Math.max(0, Math.min(24000, concreteM3));

        // 2. MW Capacity (0 MW until Phase 7 Cx, reaching 36MW at COD)
        let activeMW = 0;
        if (activePhase === 7) {
            const p7 = schedule.phases[6];
            const p7Start = new Date(p7.start_date).getTime();
            const p7End = new Date(p7.finish_date).getTime();
            const frac = Math.max(0, Math.min(1, (currentTimestamp - p7Start) / (p7End - p7Start)));
            activeMW = (frac * 36).toFixed(1);
        } else if (activePhase >= 8) {
            activeMW = "36.0";
        }

        // 3. Server Racks Deployed (0 -> 1,200 during Phase 6)
        let racksDeployed = 0;
        if (activePhase === 6) {
            const p6 = schedule.phases[5];
            const p6Start = new Date(p6.start_date).getTime();
            const p6End = new Date(p6.finish_date).getTime();
            const frac = Math.max(0, Math.min(1, (currentTimestamp - p6Start) / (p6End - p6Start)));
            racksDeployed = Math.floor(frac * 1200);
        } else if (activePhase >= 7) {
            racksDeployed = 1200;
        }

        // 4. Target PUE
        let currentPUE = "--";
        if (activePhase === 7) currentPUE = "1.32";
        else if (activePhase >= 8) currentPUE = "1.22";

        // Update 3D Geometry Visibilities & Transforms
        if (models) {
            // Phase 1: Groundwork & Piles
            models.p1_piling.visible = (activePhase >= 1);
            if (activePhase >= 4) {
                // Dim down piling rigs once superstructure is in place
                const rig = models.p1_piling.children[2];
                if (rig) rig.visible = false;
            } else {
                const rig = models.p1_piling.children[2];
                if (rig) rig.visible = true;
            }

            // Phase 2: Raft Slab
            models.p2_foundation.visible = (activePhase >= 2);

            // Phase 3: Superstructure
            models.p3_superstructure.visible = (activePhase >= 3);

            // Phase 4: Roof & Envelope
            models.p4_envelope.visible = (activePhase >= 4);
            applyCutawayState();

            // Phase 5: Heavy MEP
            models.p5_mep.visible = (activePhase >= 5);

            // Phase 6: White Space Fit-Out
            models.p6_whitespace.visible = (activePhase >= 6);

            // Phase 7: Load Banks (visible only during testing Phase 7)
            models.p7_loadbanks.visible = (activePhase === 7);
        }

        // Update Particle Systems & VFX
        if (particles) {
            // Cooling tower plumes visible in Phase 5 to 8
            particles.steam.points.visible = (activePhase >= 5);
            // Generator smoke active during Cx load tests (Phase 7)
            particles.smoke.points.visible = (activePhase === 7);
            // CFD airflow
            if (cfdEnabled) {
                particles.cfd.points.visible = (activePhase >= 6);
            }
        }

        // Update Server Rack LED States (Amber in Phase 7 testing, Cyan/Green in Phase 8 COD)
        if (window.DC36_SERVER_LEDS && window.DC36_SERVER_LEDS.length > 0) {
            const isTest = (activePhase === 7);
            const isLive = (activePhase >= 8);
            window.DC36_SERVER_LEDS.forEach((led, idx) => {
                if (isLive) {
                    led.visible = true;
                    // Blinking operational pattern
                    const flash = Math.sin(Date.now() * 0.005 + idx) > 0.1;
                    led.material.color.setHex(flash ? 0x00e5ff : 0x00ff88);
                    led.material.emissive.setHex(flash ? 0x00e5ff : 0x00ff88);
                } else if (isTest) {
                    led.visible = true;
                    led.material.color.setHex(0xffaa00);
                    led.material.emissive.setHex(0xffaa00);
                } else {
                    led.visible = false;
                }
            });
        }

        // Return telemetry state for UI HUD
        const curDate = new Date(currentTimestamp);
        const dateStr = curDate.toISOString().split('T')[0];
        const elapsedDays = Math.floor((currentTimestamp - schedule.min_timestamp) / (1000 * 3600 * 24));

        return {
            timestamp: currentTimestamp,
            dateString: dateStr,
            progressPercent: (currentProgress * 100).toFixed(1),
            elapsedDays,
            totalDays: schedule.total_calendar_days,
            activePhase,
            phaseName: schedule.phases[activePhase - 1].name,
            activeTasks,
            completedCount: completedTasks,
            totalActivities: schedule.total_activities,
            concreteM3,
            activeMW,
            racksDeployed,
            currentPUE
        };
    }

    window.DC36_TIMELINE.updateToTime = function(timestamp) {
        return updateState(timestamp);
    };

    window.DC36_TIMELINE.updateToProgress = function(fraction) {
        const totalSpan = schedule.max_timestamp - schedule.min_timestamp;
        const target = schedule.min_timestamp + fraction * totalSpan;
        return updateState(target);
    };

    window.DC36_TIMELINE.togglePlay = function() {
        if (!schedule) return false;
        // Auto-loop to start if user clicks play at or near 100% completion
        if (currentTimestamp >= schedule.max_timestamp - 100) {
            currentTimestamp = schedule.min_timestamp;
            updateState(currentTimestamp);
        }
        isPlaying = !isPlaying;
        lastAnimTime = performance.now();
        return isPlaying;
    };

    window.DC36_TIMELINE.isPlaying = function() {
        return isPlaying;
    };

    window.DC36_TIMELINE.setSpeed = function(speedMultiplier) {
        playbackSpeed = speedMultiplier;
    };

    window.DC36_TIMELINE.jumpToMilestone = function(taskCode) {
        const act = schedule.activities.find(a => a.code === taskCode);
        if (act) {
            return updateState(act.finishTimestamp || act.startTimestamp);
        }
        return updateState(currentTimestamp);
    };

    window.DC36_TIMELINE.tick = function(now) {
        if (!isPlaying) return null;
        if (!lastAnimTime) lastAnimTime = now;
        const dt = (now - lastAnimTime) / 1000;
        lastAnimTime = now;

        // Speed: 1.0 means ~60 seconds to traverse entire 1001 days project
        const totalSpan = schedule.max_timestamp - schedule.min_timestamp;
        const advanceMs = (dt / 50) * totalSpan * playbackSpeed;
        
        currentTimestamp += advanceMs;
        let finished = false;
        if (currentTimestamp >= schedule.max_timestamp) {
            currentTimestamp = schedule.max_timestamp;
            isPlaying = false;
            finished = true;
        }

        const state = updateState(currentTimestamp);
        if (state) state.playbackFinished = finished;
        return state;
    };
})();
