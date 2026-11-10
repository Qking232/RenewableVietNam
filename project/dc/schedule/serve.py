#!/usr/bin/env python3
"""
Lightweight Local HTTP Server for DC36-T3 Hyperscale 36MW Datacenter 3D Evolution
"""
import os
import sys
import webbrowser
from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8088

def main():
    web_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(web_dir)
    server_address = ('127.0.0.1', PORT)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    url = f"http://127.0.0.1:{PORT}/index.html"
    print(f"DC36-T3 4D Digital Twin running at: {url}")
    print("Opening web browser...")
    webbrowser.open(url)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")

if __name__ == '__main__':
    main()
