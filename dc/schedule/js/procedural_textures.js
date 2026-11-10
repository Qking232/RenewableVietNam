// Procedural PBR Texture Synthesizer for DC36-T3 Hyperscale Datacenter
// Zero External Image Assets - 100% Procedural Canvas Generation

(function() {
    window.DC36_TEXTURES = {};

    // 1. Concrete PBR Surface (Aggregate Noise, Micro-Cracks, Expansion Seams)
    function generateConcreteTexture() {
        const canvas = document.createElement('canvas');
        canvas.width = 512;
        canvas.height = 512;
        const ctx = canvas.getContext('2d');

        // Base Concrete Slate
        ctx.fillStyle = '#838a92';
        ctx.fillRect(0, 0, 512, 512);

        // Multi-Scale Aggregate Noise
        const imgData = ctx.getImageData(0, 0, 512, 512);
        const data = imgData.data;
        for (let i = 0; i < data.length; i += 4) {
            const noise = (Math.random() - 0.5) * 36;
            data[i] = Math.min(255, Math.max(0, data[i] + noise));
            data[i+1] = Math.min(255, Math.max(0, data[i+1] + noise));
            data[i+2] = Math.min(255, Math.max(0, data[i+2] + noise));
        }
        ctx.putImageData(imgData, 0, 0);

        // Expansion Joint Seams
        ctx.strokeStyle = '#4b5259';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(256, 0); ctx.lineTo(256, 512);
        ctx.moveTo(0, 256); ctx.lineTo(512, 256);
        ctx.stroke();

        const tex = new THREE.CanvasTexture(canvas);
        tex.wrapS = THREE.RepeatWrapping;
        tex.wrapT = THREE.RepeatWrapping;
        tex.repeat.set(8, 6);
        return tex;
    }

    // 2. Brushed Industrial Stainless Steel / Aluminum
    function generateBrushedMetalTexture() {
        const canvas = document.createElement('canvas');
        canvas.width = 512;
        canvas.height = 512;
        const ctx = canvas.getContext('2d');

        ctx.fillStyle = '#9aa1a8';
        ctx.fillRect(0, 0, 512, 512);

        // Anisotropic Horizontal Brushed Scratches
        for (let y = 0; y < 512; y++) {
            const alpha = 0.05 + Math.random() * 0.12;
            const shade = Math.random() > 0.5 ? 255 : 30;
            ctx.fillStyle = `rgba(${shade},${shade},${shade},${alpha})`;
            ctx.fillRect(0, y, 512, 1);
        }

        const tex = new THREE.CanvasTexture(canvas);
        tex.wrapS = THREE.RepeatWrapping;
        tex.wrapT = THREE.RepeatWrapping;
        return tex;
    }

    // 3. Hexagonal Perforated Server Door Ventilation Mesh
    function generateHexMeshTexture() {
        const canvas = document.createElement('canvas');
        canvas.width = 256;
        canvas.height = 256;
        const ctx = canvas.getContext('2d');

        ctx.fillStyle = '#111317';
        ctx.fillRect(0, 0, 256, 256);

        const r = 6;
        const hexWidth = r * Math.sqrt(3);
        const hexHeight = r * 2;

        ctx.fillStyle = '#050608';
        for (let y = 0; y < 256 + hexHeight; y += hexHeight * 0.75) {
            const rowOffset = (Math.floor(y / (hexHeight * 0.75)) % 2 === 0) ? 0 : hexWidth / 2;
            for (let x = 0; x < 256 + hexWidth; x += hexWidth) {
                drawHexagon(ctx, x + rowOffset, y, r - 1.5);
            }
        }

        const tex = new THREE.CanvasTexture(canvas);
        tex.wrapS = THREE.RepeatWrapping;
        tex.wrapT = THREE.RepeatWrapping;
        tex.repeat.set(4, 8);
        return tex;
    }

    function drawHexagon(ctx, cx, cy, radius) {
        ctx.beginPath();
        for (let i = 0; i < 6; i++) {
            const angle = (i * Math.PI) / 3;
            const x = cx + radius * Math.cos(angle);
            const y = cy + radius * Math.sin(angle);
            if (i === 0) ctx.moveTo(x, y);
            else ctx.lineTo(x, y);
        }
        ctx.closePath();
        ctx.fill();
    }

    // 4. Industrial Safety Hazard Chevron Stripes (Yellow / Black 45-degree)
    function generateHazardStripes() {
        const canvas = document.createElement('canvas');
        canvas.width = 256;
        canvas.height = 256;
        const ctx = canvas.getContext('2d');

        ctx.fillStyle = '#f59e0b'; // OSHA Safety Amber
        ctx.fillRect(0, 0, 256, 256);

        ctx.fillStyle = '#18181b'; // Matte Black
        const stripeWidth = 32;
        for (let x = -256; x < 512; x += stripeWidth * 2) {
            ctx.beginPath();
            ctx.moveTo(x, 0);
            ctx.lineTo(x + stripeWidth, 0);
            ctx.lineTo(x + stripeWidth + 256, 256);
            ctx.lineTo(x + 256, 256);
            ctx.closePath();
            ctx.fill();
        }

        const tex = new THREE.CanvasTexture(canvas);
        tex.wrapS = THREE.RepeatWrapping;
        tex.wrapT = THREE.RepeatWrapping;
        return tex;
    }

    // 5. High-Density Server Blade PCB Traces
    function generatePCBTexture() {
        const canvas = document.createElement('canvas');
        canvas.width = 256;
        canvas.height = 256;
        const ctx = canvas.getContext('2d');

        ctx.fillStyle = '#062016'; // Deep Solder Mask Green
        ctx.fillRect(0, 0, 256, 256);

        ctx.strokeStyle = '#22c55e'; // Green Copper Trace
        ctx.lineWidth = 1.5;
        for (let i = 0; i < 24; i++) {
            ctx.beginPath();
            const startY = i * 11;
            ctx.moveTo(0, startY);
            ctx.lineTo(80 + (i % 5) * 20, startY);
            ctx.lineTo(120 + (i % 5) * 20, startY + 20);
            ctx.lineTo(256, startY + 20);
            ctx.stroke();
        }

        // Gold Pins
        ctx.fillStyle = '#eab308';
        for (let x = 10; x < 250; x += 15) {
            ctx.fillRect(x, 240, 8, 16);
        }

        const tex = new THREE.CanvasTexture(canvas);
        tex.wrapS = THREE.RepeatWrapping;
        tex.wrapT = THREE.RepeatWrapping;
        return tex;
    }

    // 6. Volumetric Cloud Particle Sprite for Cooling Towers
    function generatePlumeSprite() {
        const canvas = document.createElement('canvas');
        canvas.width = 128;
        canvas.height = 128;
        const ctx = canvas.getContext('2d');

        const grad = ctx.createRadialGradient(64, 64, 4, 64, 64, 60);
        grad.addColorStop(0, 'rgba(255, 255, 255, 0.85)');
        grad.addColorStop(0.35, 'rgba(215, 240, 255, 0.45)');
        grad.addColorStop(0.7, 'rgba(190, 225, 255, 0.15)');
        grad.addColorStop(1, 'rgba(255, 255, 255, 0.0)');

        ctx.fillStyle = grad;
        ctx.fillRect(0, 0, 128, 128);

        return new THREE.CanvasTexture(canvas);
    }

    window.DC36_TEXTURES.init = function() {
        return {
            concrete: generateConcreteTexture(),
            brushedMetal: generateBrushedMetalTexture(),
            hexMesh: generateHexMeshTexture(),
            hazardStripes: generateHazardStripes(),
            pcb: generatePCBTexture(),
            plumeSprite: generatePlumeSprite()
        };
    };
})();
