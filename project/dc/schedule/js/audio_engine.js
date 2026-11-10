// Procedural Web Audio API Sound Synthesizer for DC36-T3 Hyperscale Datacenter
// Zero External Audio Files - 100% Mathematical Audio Synthesis

(function() {
    window.DC36_AUDIO = {};

    let ctx = null;
    let masterGain = null;
    let isMuted = true;
    let isInitialized = false;

    // Subsystem Sound Generators
    let transformerNodes = null;
    let chillerNodes = null;
    let serverFanNodes = null;
    let generatorNodes = null;

    function initAudioContext() {
        if (isInitialized) return;
        const AudioCtx = window.AudioContext || window.webkitAudioContext;
        if (!AudioCtx) return;

        ctx = new AudioCtx();
        masterGain = ctx.createGain();
        masterGain.gain.setValueAtTime(0.0, ctx.currentTime);
        masterGain.connect(ctx.destination);

        // 1. Substation Transformer 50Hz AC Magnetostriction Hum
        transformerNodes = setupTransformerHum();

        // 2. Chiller Centrifugal Compressor & Turbine Drone
        chillerNodes = setupChillerDrone();

        // 3. Server Room White Space Airflow Pink Noise (EC Fans)
        serverFanNodes = setupServerRoomFans();

        // 4. Standby Diesel Generator Heavy Engine Rumble
        generatorNodes = setupGeneratorRumble();

        isInitialized = true;
    }

    // 1. Substation 50Hz Transformer Hum (50Hz + 100Hz + 150Hz)
    function setupTransformerHum() {
        const gain = ctx.createGain();
        gain.gain.setValueAtTime(0.0, ctx.currentTime);
        gain.connect(masterGain);

        // Fundamental 50 Hz sine wave
        const osc1 = ctx.createOscillator();
        osc1.type = 'sine';
        osc1.frequency.setValueAtTime(50, ctx.currentTime);
        const g1 = ctx.createGain();
        g1.gain.setValueAtTime(0.35, ctx.currentTime);
        osc1.connect(g1);
        g1.connect(gain);
        osc1.start();

        // 100 Hz harmonic
        const osc2 = ctx.createOscillator();
        osc2.type = 'sine';
        osc2.frequency.setValueAtTime(100, ctx.currentTime);
        const g2 = ctx.createGain();
        g2.gain.setValueAtTime(0.2, ctx.currentTime);
        osc2.connect(g2);
        g2.connect(gain);
        osc2.start();

        // 150 Hz harmonic
        const osc3 = ctx.createOscillator();
        osc3.type = 'triangle';
        osc3.frequency.setValueAtTime(150, ctx.currentTime);
        const g3 = ctx.createGain();
        g3.gain.setValueAtTime(0.08, ctx.currentTime);
        osc3.connect(g3);
        g3.connect(gain);
        osc3.start();

        return { gain };
    }

    // 2. Chiller Centrifugal Compressor Drone
    function setupChillerDrone() {
        const gain = ctx.createGain();
        gain.gain.setValueAtTime(0.0, ctx.currentTime);
        gain.connect(masterGain);

        const osc = ctx.createOscillator();
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(84, ctx.currentTime);

        const filter = ctx.createBiquadFilter();
        filter.type = 'lowpass';
        filter.frequency.setValueAtTime(280, ctx.currentTime);
        filter.Q.setValueAtTime(3.0, ctx.currentTime);

        osc.connect(filter);
        filter.connect(gain);
        osc.start();

        return { gain, filter };
    }

    // 3. Server Room Pink Noise (EC Fans across 72 CRAH units & 1,200 Racks)
    function setupServerRoomFans() {
        const gain = ctx.createGain();
        gain.gain.setValueAtTime(0.0, ctx.currentTime);
        gain.connect(masterGain);

        // Generate 3 seconds of pink noise buffer
        const bufferSize = ctx.sampleRate * 3;
        const buffer = ctx.createBuffer(1, bufferSize, ctx.sampleRate);
        const data = buffer.getChannelData(0);

        let b0 = 0, b1 = 0, b2 = 0, b3 = 0, b4 = 0, b5 = 0, b6 = 0;
        for (let i = 0; i < bufferSize; i++) {
            const white = Math.random() * 2 - 1;
            b0 = 0.99886 * b0 + white * 0.0555179;
            b1 = 0.99332 * b1 + white * 0.0750759;
            b2 = 0.96900 * b2 + white * 0.1538520;
            b3 = 0.86650 * b3 + white * 0.3104856;
            b4 = 0.55000 * b4 + white * 0.5329522;
            b5 = -0.7616 * b5 - white * 0.0168980;
            data[i] = (b0 + b1 + b2 + b3 + b4 + b5 + b6 + white * 0.5362) * 0.06;
            b6 = white * 0.115926;
        }

        const noiseSource = ctx.createBufferSource();
        noiseSource.buffer = buffer;
        noiseSource.loop = true;

        // Bandpass filter centered at 850 Hz to simulate HVAC duct air rush
        const filter = ctx.createBiquadFilter();
        filter.type = 'bandpass';
        filter.frequency.setValueAtTime(750, ctx.currentTime);
        filter.Q.setValueAtTime(1.2, ctx.currentTime);

        noiseSource.connect(filter);
        filter.connect(gain);
        noiseSource.start();

        return { gain, filter };
    }

    // 4. Standby Generator Heavy Diesel Engine Rumble
    function setupGeneratorRumble() {
        const gain = ctx.createGain();
        gain.gain.setValueAtTime(0.0, ctx.currentTime);
        gain.connect(masterGain);

        const osc = ctx.createOscillator();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(26, ctx.currentTime);

        const filter = ctx.createBiquadFilter();
        filter.type = 'lowpass';
        filter.frequency.setValueAtTime(160, ctx.currentTime);
        filter.Q.setValueAtTime(4.0, ctx.currentTime);

        osc.connect(filter);
        filter.connect(gain);
        osc.start();

        return { gain };
    }

    // High Voltage Circuit Breaker / Switchgear Snap Sound
    window.DC36_AUDIO.playSwitchgearClick = function() {
        if (!ctx || isMuted) return;
        const now = ctx.currentTime;
        const osc = ctx.createOscillator();
        const clickGain = ctx.createGain();
        osc.type = 'square';
        osc.frequency.setValueAtTime(800, now);
        osc.frequency.exponentialRampToValueAtTime(80, now + 0.06);

        clickGain.gain.setValueAtTime(0.6, now);
        clickGain.gain.exponentialRampToValueAtTime(0.001, now + 0.08);

        osc.connect(clickGain);
        clickGain.connect(masterGain);
        osc.start(now);
        osc.stop(now + 0.08);
    };

    // Toggle Master Audio Mute
    window.DC36_AUDIO.toggleMute = function() {
        initAudioContext();
        if (ctx.state === 'suspended') {
            ctx.resume();
        }

        isMuted = !isMuted;
        const targetVol = isMuted ? 0.0 : 0.65;
        if (masterGain) {
            masterGain.gain.setTargetAtTime(targetVol, ctx.currentTime, 0.08);
        }
        return isMuted;
    };

    window.DC36_AUDIO.isMuted = function() {
        return isMuted;
    };

    // Dynamically adjust audio mix based on construction phase & equipment state
    window.DC36_AUDIO.updateState = function(phase, isBlackoutRunning) {
        if (!ctx || !isInitialized) return;
        const now = ctx.currentTime;

        if (isBlackoutRunning) {
            // During blackout test: Utility drops, 16 diesel generators roar at 100%
            if (transformerNodes) transformerNodes.gain.gain.setTargetAtTime(0.0, now, 0.1);
            if (generatorNodes) generatorNodes.gain.gain.setTargetAtTime(0.85, now, 0.2);
            if (serverFanNodes) serverFanNodes.gain.gain.setTargetAtTime(0.3, now, 0.2);
            if (chillerNodes) chillerNodes.gain.gain.setTargetAtTime(0.0, now, 0.1);
            return;
        }

        // Normal Phased Progression
        if (phase >= 5) {
            // Substation active
            if (transformerNodes) transformerNodes.gain.gain.setTargetAtTime(0.3, now, 0.2);
            // Chillers active
            if (chillerNodes) chillerNodes.gain.gain.setTargetAtTime(0.25, now, 0.2);
        } else {
            if (transformerNodes) transformerNodes.gain.gain.setTargetAtTime(0.0, now, 0.2);
            if (chillerNodes) chillerNodes.gain.gain.setTargetAtTime(0.0, now, 0.2);
        }

        if (phase >= 6) {
            // Server room CRAH & racks active
            if (serverFanNodes) serverFanNodes.gain.gain.setTargetAtTime(0.4, now, 0.2);
        } else {
            if (serverFanNodes) serverFanNodes.gain.gain.setTargetAtTime(0.0, now, 0.2);
        }

        if (phase === 7) {
            // Commissioning Load tests: generators running at testing load
            if (generatorNodes) generatorNodes.gain.gain.setTargetAtTime(0.45, now, 0.2);
        } else {
            if (generatorNodes) generatorNodes.gain.gain.setTargetAtTime(0.0, now, 0.2);
        }
    };
})();
