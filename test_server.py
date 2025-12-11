yep#!/usr/bin/env python3
"""Quick test to verify server can start"""
import http.server
import socketserver
import sys

PORT = 7000

# Fix Windows encoding
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # Suppress default logging

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Server running at http://localhost:{PORT}")
        print(f"Press Ctrl+C to stop")
        httpd.serve_forever()
except OSError as e:
    if "Address already in use" in str(e) or "Only one usage" in str(e):
        print(f"Port {PORT} is already in use. Server may already be running!")
        print(f"Open http://localhost:{PORT} in your browser")
    else:
        print(f"Error: {e}")
except KeyboardInterrupt:
    print("\nServer stopped")

