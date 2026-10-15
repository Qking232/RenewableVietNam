#!/usr/bin/env python3
"""
Custom Local Development Server for RenewableVietNam
Features:
- CORS headers enabled for all local requests
- Proper MIME type mappings (.mjs, .json, .geojson, .kml, .svg, etc.)
- Cache-Control: no-store / no-cache for instant live file reflection
- Automatic port fallback if 8000 is occupied
"""

import http.server
import socketserver
import os
import sys

PORT = 8000
MAX_PORT_ATTEMPTS = 10
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

class CustomDevHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT_DIR, **kwargs)

    def end_headers(self):
        # Enable CORS for local cross-origin development & map tiles/APIs
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS, HEAD")
        self.send_header("Access-Control-Allow-Headers", "*")
        # Prevent aggressive browser caching during active development
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

# Register extra MIME types
CustomDevHandler.extensions_map.update({
    ".mjs": "application/javascript",
    ".js": "application/javascript",
    ".json": "application/json",
    ".geojson": "application/geo+json",
    ".kml": "application/vnd.google-earth.kml+xml",
    ".svg": "image/svg+xml",
    ".wasm": "application/wasm",
    ".yaml": "text/yaml",
    ".yml": "text/yaml",
})

def run_server():
    global PORT
    for attempt in range(MAX_PORT_ATTEMPTS):
        try:
            with socketserver.TCPServer(("", PORT), CustomDevHandler) as httpd:
                print(f"============================================================")
                print(f"🚀 RenewableVietNam Local Server is running!")
                print(f"📂 Root Directory: {ROOT_DIR}")
                print(f"🌐 Local URL:     http://localhost:{PORT}/")
                print(f"⚡ EV Charging:   http://localhost:{PORT}/evcharging/")
                print(f"⚡ Rev 0.10:      http://localhost:{PORT}/evcharging/index_rev0.10.html")
                print(f"🌿 ProjectEnergy: http://localhost:{PORT}/projectenergy/")
                print(f"============================================================")
                sys.stdout.flush()
                httpd.serve_forever()
        except OSError as e:
            if "Address already in use" in str(e) or e.errno == 10048 or e.errno == 98:
                print(f"Port {PORT} is busy, trying port {PORT + 1}...")
                PORT += 1
            else:
                raise e

if __name__ == "__main__":
    run_server()
