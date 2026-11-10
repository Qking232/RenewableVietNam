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

        // Default to Completed Operational Campus Reality
        currentTimestamp = schedule.max_timestamp;
        return updateState(currentTimestamp);
    };

    window.DC36_TIMELINE.setCampusMode = function(mode) {
        if (!schedule) return null;
        if (mode === 'reality') {
            currentTimestamp = schedule.max_timestamp;
        } else if (mode === 'construction') {
            currentTimestamp = schedule.min_timestamp;
        }
        return updateState(currentTimestamp);
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
                    if (child.isMesh && child.material) {
                        if (!child.material.isMeshPhysicalMaterial && !child.userData.isGlass) {
                            child.material.transparent = true;
                            child.material.opacity = 0.18;
                            child.material.depthWrite = false;
                        }
                    }
                });
            }
        } else {
            if (roof) roof.visible = true;
            if (facadeGroup) {
                facadeGroup.traverse(child => {
                    if (child.isMesh && child.material) {
                        if (!child.material.isMeshPhysicalMaterial && !child.userData.isGlass) {
                            child.material.transparent = false;
                            child.material.opacity = 1.0;
                            child.material.depthWrite = true;
                        }
                    }
                });
            }
        }
    }

    // Helper: Compute fractional progress [0.0, 1.0] for any target P6 activity
    function getTaskFrac(code, curTime) {
        if (!schedule || !schedule.activities) return 0;
        const act = schedule.activities.find(a => a.code === code);
        if (!act) return 0;
        if (curTime < act.startTimestamp) return 0;
        if (curTime >= act.finishTimestamp) return 1;
        const span = act.finishTimestamp - act.startTimestamp;
        if (span <= 0) return 1;
        return Math.max(0, Math.min(1, (curTime - act.startTimestamp) / span));
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

        // =========================================================================
        // HIGH-PRECISION 4D CONSTRUCTION SEQUENCE KINEMATICS (PRIMAVERA P6 DCMA-14)
        // =========================================================================
        if (models) {
            const tau_piling = getTaskFrac('A4120', currentTimestamp);
            const tau_raft   = getTaskFrac('A4140', currentTimestamp);
            const tau_cols   = getTaskFrac('A4210', currentTimestamp);
            const tau_slab1  = getTaskFrac('A4220', currentTimestamp);
            const tau_slab2  = getTaskFrac('A4230', currentTimestamp);
            const tau_truss  = getTaskFrac('A4240', currentTimestamp);
            const tau_facade = getTaskFrac('A4310', currentTimestamp);
            const tau_roof   = getTaskFrac('A4320', currentTimestamp);
            const tau_sub    = getTaskFrac('A5110', currentTimestamp);
            const tau_chw    = getTaskFrac('A5310', currentTimestamp);
            const tau_gens   = getTaskFrac('A5220', currentTimestamp);
            const tau_racks  = getTaskFrac('A5470', currentTimestamp);
            const tau_heat   = getTaskFrac('A6420', currentTimestamp);

            // ---------------------------------------------------------------------
            // 1. Phase 1: Sequential Bored Piling & Rig Kinematics (A4120)
            // ---------------------------------------------------------------------
            const p1 = models.p1_piling;
            if (p1 && p1.userData) {
                p1.visible = (activePhase >= 1);
                const piles = p1.userData.piles || [];
                const totalPiles = piles.length; // 160 clusters
                const rig = p1.userData.rig;

                if (tau_piling <= 0) {
                    piles.forEach(p => { if (p.group) p.group.visible = false; });
                    if (rig) rig.visible = false;
                } else if (tau_piling >= 1.0) {
                    piles.forEach(p => {
                        if (p.group) {
                            p.group.visible = true;
                            p.group.position.y = 0;
                        }
                    });
                    if (rig) {
                        rig.visible = (activePhase < 4);
                        rig.position.set(-36, 0, 20);
                    }
                } else {
                    const activeIdx = Math.floor(tau_piling * totalPiles);
                    const subFrac = (tau_piling * totalPiles) - activeIdx;

                    for (let i = 0; i < totalPiles; i++) {
                        const p = piles[i];
                        if (!p || !p.group) continue;
                        if (i < activeIdx) {
                            p.group.visible = true;
                            p.group.position.y = 0;
                        } else if (i === activeIdx) {
                            p.group.visible = true;
                            // Active pile driving downwards into the earth
                            p.group.position.y = (1.0 - subFrac) * 5.0;
                        } else {
                            p.group.visible = false;
                        }
                    }

                    if (rig && activeIdx < totalPiles) {
                        rig.visible = true;
                        const curP = piles[activeIdx];
                        rig.position.set(curP.x, 0, curP.z + 3.2);
                        if (rig.userData && rig.userData.auger) {
                            rig.userData.auger.rotation.y = (Date.now() * 0.02) % (Math.PI * 2);
                        }
                    }
                }
            }

            // ---------------------------------------------------------------------
            // 2. Phase 2: Directional Raft Slab Pour & Plinths Casting (A4140)
            // ---------------------------------------------------------------------
            const p2 = models.p2_foundation;
            if (p2 && p2.userData) {
                if (tau_raft <= 0 && activePhase < 2) {
                    p2.visible = false;
                } else if (tau_raft >= 1.0 || activePhase > 2) {
                    p2.visible = true;
                    if (p2.userData.raft) {
                        p2.userData.raft.scale.set(1, 1, 1);
                        p2.userData.raft.position.set(5, 0.9, 0);
                    }
                    if (p2.userData.genPlinths) p2.userData.genPlinths.visible = true;
                    if (p2.userData.subPlinths) p2.userData.subPlinths.forEach(sp => sp.visible = true);
                } else {
                    p2.visible = true;
                    // Directional West-to-East progressive concrete casting
                    const growthX = Math.max(0.005, tau_raft);
                    if (p2.userData.raft) {
                        p2.userData.raft.scale.set(growthX, 1, 1);
                        p2.userData.raft.position.x = 5 - (90 * (1.0 - growthX)) / 2;
                    }
                    if (p2.userData.genPlinths) p2.userData.genPlinths.visible = (tau_raft > 0.35);
                    if (p2.userData.subPlinths) {
                        p2.userData.subPlinths.forEach((sp, idx) => {
                            sp.visible = (tau_raft > 0.55 + idx * 0.2);
                        });
                    }
                }
            }

            // ---------------------------------------------------------------------
            // 3. Phase 3: Vertical Column Extrusion & Slabs Casting (A4210, A4220, A4230)
            // ---------------------------------------------------------------------
            const p3 = models.p3_superstructure;
            if (p3 && p3.userData) {
                if (tau_cols <= 0 && activePhase < 3) {
                    p3.visible = false;
                } else {
                    p3.visible = true;
                    const cols = p3.userData.columns || [];

                    // Columns Vertical Extrusion (A4210)
                    if (tau_cols >= 1.0 || activePhase > 3) {
                        cols.forEach(c => {
                            if (c.mesh) {
                                c.mesh.visible = true;
                                c.mesh.scale.set(1, 1, 1);
                                c.mesh.position.y = c.baseY;
                            }
                        });
                        if (p3.userData.walls) {
                            p3.userData.walls.forEach(w => {
                                w.visible = true;
                                w.scale.set(1, 1, 1);
                                w.position.y = 7.3;
                            });
                        }
                    } else if (tau_cols > 0) {
                        const colScaleY = Math.max(0.005, tau_cols);
                        cols.forEach(c => {
                            if (c.mesh) {
                                c.mesh.visible = true;
                                c.mesh.scale.set(1, colScaleY, 1);
                                c.mesh.position.y = 1.8 + (10.5 * colScaleY) / 2;
                            }
                        });
                        if (p3.userData.walls) {
                            p3.userData.walls.forEach(w => {
                                w.visible = true;
                                w.scale.set(1, colScaleY, 1);
                                w.position.y = 1.8 + (11 * colScaleY) / 2;
                            });
                        }
                    }

                    // Level 1 Slab Directional Pour (A4220)
                    if (p3.userData.slabL1) {
                        if (tau_slab1 <= 0 && activePhase < 3) {
                            p3.userData.slabL1.visible = false;
                        } else if (tau_slab1 >= 1.0 || activePhase > 3) {
                            p3.userData.slabL1.visible = true;
                            p3.userData.slabL1.scale.set(1, 1, 1);
                            p3.userData.slabL1.position.x = 5;
                        } else if (tau_slab1 > 0) {
                            p3.userData.slabL1.visible = true;
                            const s1 = Math.max(0.005, tau_slab1);
                            p3.userData.slabL1.scale.set(s1, 1, 1);
                            p3.userData.slabL1.position.x = 5 - (89 * (1.0 - s1)) / 2;
                        }
                    }

                    // Level 2 Slab Directional Pour (A4230)
                    if (p3.userData.slabL2) {
                        if (tau_slab2 <= 0 && activePhase < 3) {
                            p3.userData.slabL2.visible = false;
                        } else if (tau_slab2 >= 1.0 || activePhase > 3) {
                            p3.userData.slabL2.visible = true;
                            p3.userData.slabL2.scale.set(1, 1, 1);
                            p3.userData.slabL2.position.x = 5;
                        } else if (tau_slab2 > 0) {
                            p3.userData.slabL2.visible = true;
                            const s2 = Math.max(0.005, tau_slab2);
                            p3.userData.slabL2.scale.set(s2, 1, 1);
                            p3.userData.slabL2.position.x = 5 - (89 * (1.0 - s2)) / 2;
                        }
                    }
                }
            }

            // ---------------------------------------------------------------------
            // 4. Phase 4: Roof Steel Trusses & Perimeter Envelope (A4240, A4310, A4320)
            // ---------------------------------------------------------------------
            const p4 = models.p4_envelope;
            if (p4 && p4.userData) {
                if (tau_truss <= 0 && tau_facade <= 0 && tau_roof <= 0 && activePhase < 4) {
                    p4.visible = false;
                } else {
                    p4.visible = true;

                    // Roof Trusses Lowering from Rigging Cable (A4240)
                    const trusses = p4.userData.trusses || [];
                    if (p4.userData.roofSteel) {
                        if (tau_truss <= 0 && activePhase < 4) {
                            p4.userData.roofSteel.visible = false;
                            if (p4.userData.gantry) p4.userData.gantry.visible = false;
                        } else if (tau_truss >= 1.0 || activePhase > 4) {
                            p4.userData.roofSteel.visible = true;
                            trusses.forEach(t => {
                                if (t.mesh) {
                                    t.mesh.visible = true;
                                    t.mesh.position.y = t.targetY;
                                }
                            });
                            if (p4.userData.gantry) p4.userData.gantry.visible = true;
                        } else {
                            p4.userData.roofSteel.visible = true;
                            const trussCount = trusses.length; // 9
                            for (let i = 0; i < trussCount; i++) {
                                const t = trusses[i];
                                if (!t || !t.mesh) continue;
                                const slot = i / trussCount;
                                const nextSlot = (i + 1) / trussCount;
                                if (tau_truss >= nextSlot) {
                                    t.mesh.visible = true;
                                    t.mesh.position.y = t.targetY;
                                } else if (tau_truss >= slot) {
                                    const tFrac = (tau_truss - slot) / (nextSlot - slot);
                                    t.mesh.visible = true;
                                    // Smooth descent from sky rigging height
                                    t.mesh.position.y = t.targetY + (1.0 - tFrac) * 25.0;
                                } else {
                                    t.mesh.visible = false;
                                }
                            }
                            if (p4.userData.gantry) p4.userData.gantry.visible = (tau_truss > 0.85);
                        }
                    }

                    // Precast Architectural Facade Enclosure (A4310)
                    if (p4.userData.facadeGroup && p4.userData.facade) {
                        const f = p4.userData.facade;
                        if (tau_facade <= 0 && activePhase < 4) {
                            p4.userData.facadeGroup.visible = false;
                        } else if (tau_facade >= 1.0 || activePhase > 4) {
                            p4.userData.facadeGroup.visible = true;
                            if (f.south) { f.south.visible = true; f.south.position.y = 10.3; }
                            if (f.west)  { f.west.visible = true; f.west.position.y = 10.3; }
                            if (f.north) { f.north.visible = true; f.north.position.y = 10.3; }
                            if (f.east)  { f.east.visible = true; f.east.position.y = 10.3; }
                            if (f.lobby) f.lobby.visible = true;
                            if (f.dock)  f.dock.visible = true;
                            if (f.accent) f.accent.visible = true;
                        } else {
                            p4.userData.facadeGroup.visible = true;
                            // South Wall (0.00 - 0.25)
                            if (f.south) {
                                f.south.visible = (tau_facade > 0);
                                const sFrac = Math.min(1.0, tau_facade / 0.25);
                                f.south.position.y = 10.3 + (1.0 - sFrac) * 18.0;
                            }
                            // West Wall (0.25 - 0.50)
                            if (f.west) {
                                f.west.visible = (tau_facade > 0.25);
                                const wFrac = Math.max(0, Math.min(1.0, (tau_facade - 0.25) / 0.25));
                                f.west.position.y = 10.3 + (1.0 - wFrac) * 18.0;
                            }
                            // North Wall (0.50 - 0.75)
                            if (f.north) {
                                f.north.visible = (tau_facade > 0.50);
                                const nFrac = Math.max(0, Math.min(1.0, (tau_facade - 0.50) / 0.25));
                                f.north.position.y = 10.3 + (1.0 - nFrac) * 18.0;
                            }
                            // East Wall, Corporate Lobby & Loading Dock (0.75 - 1.00)
                            if (f.east) {
                                f.east.visible = (tau_facade > 0.75);
                                const eFrac = Math.max(0, Math.min(1.0, (tau_facade - 0.75) / 0.25));
                                f.east.position.y = 10.3 + (1.0 - eFrac) * 18.0;
                            }
                            if (f.lobby) f.lobby.visible = (tau_facade > 0.85);
                            if (f.dock)  f.dock.visible = (tau_facade > 0.85);
                            if (f.accent) f.accent.visible = (tau_facade > 0.92);
                        }
                    }

                    // TPO Roof Waterproof Membrane Roll-Out (A4320)
                    if (p4.userData.roof) {
                        if (tau_roof <= 0 && activePhase < 4) {
                            p4.userData.roof.visible = false;
                        } else if (tau_roof >= 1.0 || activePhase > 4) {
                            p4.userData.roof.visible = true;
                            p4.userData.roof.scale.set(1, 1, 1);
                            p4.userData.roof.position.z = 0;
                        } else {
                            p4.userData.roof.visible = true;
                            const rz = Math.max(0.005, tau_roof);
                            p4.userData.roof.scale.set(1, 1, rz);
                            p4.userData.roof.position.z = 0 - (60.5 * (1.0 - rz)) / 2;
                        }
                    }

                    applyCutawayState();
                }
            }

            // ---------------------------------------------------------------------
            // 5. Phase 5: Heavy MEP Rigging & Equipment Placement (A5110, A5220, A5310)
            // ---------------------------------------------------------------------
            const p5 = models.p5_mep;
            if (p5 && p5.userData) {
                if (tau_sub <= 0 && tau_chw <= 0 && tau_gens <= 0 && activePhase < 5) {
                    p5.visible = false;
                } else {
                    p5.visible = true;

                    // 110kV Transformers Placement (A5110)
                    if (p5.userData.substation) {
                        p5.userData.substation.visible = (tau_sub > 0 || activePhase >= 5);
                        const trans = p5.userData.transformers || [];
                        trans.forEach(tr => {
                            if (!tr.group) return;
                            if (tau_sub <= 0 && activePhase < 5) {
                                tr.group.visible = false;
                            } else if (tau_sub >= 1.0 || activePhase > 5) {
                                tr.group.visible = true;
                                tr.group.position.y = tr.targetY;
                            } else {
                                tr.group.visible = true;
                                tr.group.position.y = tr.targetY + (1.0 - tau_sub) * 16.0;
                            }
                        });
                    }

                    // Standby Generator Farm Sequential Rigging (A5220)
                    const gensets = p5.userData.gensets || [];
                    const genCount = gensets.length; // 16
                    if (tau_gens <= 0 && activePhase < 5) {
                        gensets.forEach(g => { if (g.group) g.group.visible = false; });
                    } else if (tau_gens >= 1.0 || activePhase > 5) {
                        gensets.forEach(g => {
                            if (g.group) {
                                g.group.visible = true;
                                g.group.position.y = g.targetY;
                            }
                        });
                    } else {
                        for (let i = 0; i < genCount; i++) {
                            const g = gensets[i];
                            if (!g || !g.group) continue;
                            const slot = i / genCount;
                            const nextSlot = (i + 1) / genCount;
                            if (tau_gens >= nextSlot) {
                                g.group.visible = true;
                                g.group.position.y = g.targetY;
                            } else if (tau_gens >= slot) {
                                const gFrac = (tau_gens - slot) / (nextSlot - slot);
                                g.group.visible = true;
                                g.group.position.y = g.targetY + (1.0 - gFrac) * 12.0;
                            } else {
                                g.group.visible = false;
                            }
                        }
                    }

                    // Centrifugal Chillers & Cooling Towers (A5310, A5330)
                    const chillers = p5.userData.chillers || [];
                    chillers.forEach(ch => {
                        if (!ch.group) return;
                        if (tau_chw <= 0 && activePhase < 5) {
                            ch.group.visible = false;
                        } else if (tau_chw >= 1.0 || activePhase > 5) {
                            ch.group.visible = true;
                            ch.group.position.y = ch.targetY;
                        } else {
                            ch.group.visible = true;
                            ch.group.position.y = ch.targetY + (1.0 - tau_chw) * 12.0;
                        }
                    });
                    if (p5.userData.coolingTowers) {
                        p5.userData.coolingTowers.visible = (tau_chw > 0.4 || activePhase >= 5);
                    }
                }
            }

            // ---------------------------------------------------------------------
            // 6. Phase 6: White Space Fit-Out & Pod Deployment (A5470)
            // ---------------------------------------------------------------------
            const p6 = models.p6_whitespace;
            if (p6 && p6.userData) {
                if (activePhase < 6) {
                    p6.visible = false;
                } else {
                    p6.visible = true;
                    if (p6.userData.raisedFloor) p6.userData.raisedFloor.visible = true;
                    if (p6.userData.upsRoom) p6.userData.upsRoom.visible = true;

                    // 1,200 High-Density Server Racks Population (336 in model)
                    const racks = p6.userData.racks || [];
                    const rackTotal = racks.length;
                    if (activePhase > 6) {
                        racks.forEach(r => r.visible = true);
                    } else {
                        const activeCount = Math.floor(tau_racks * rackTotal);
                        for (let i = 0; i < rackTotal; i++) {
                            racks[i].visible = (i < activeCount);
                        }
                    }
                }
            }

            // ---------------------------------------------------------------------
            // 7. Phase 7: Testing & Commissioning Load Banks (A6420)
            // ---------------------------------------------------------------------
            const p7 = models.p7_loadbanks;
            if (p7 && p7.userData) {
                p7.visible = (activePhase === 7);
                if (activePhase === 7 && p7.userData.pulseRing) {
                    p7.userData.pulseRing.rotation.z += 0.015;
                }
            }
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
