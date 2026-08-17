#!/usr/bin/env python3
"""Serve the Programme Academic Reader locally.

Serves the repo root so the viewer (pdfs/programme/index.html) can link
PDFs, generated .tex, and markdown sources. `/` redirects to the reader.

    python build/serve_programme.py          # http://localhost:7300
    python build/serve_programme.py 7301     # alternate port
"""
import http.server
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 7300


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=str(ROOT), **kw)

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            self.send_response(302)
            self.send_header("Location", "/pdfs/programme/index.html")
            self.end_headers()
            return
        try:
            super().do_GET()
        except (ConnectionAbortedError, ConnectionResetError, BrokenPipeError):
            pass  # browser aborted mid-stream (PDF viewer does this); harmless

    def log_message(self, fmt, *args):
        pass


if __name__ == "__main__":
    # ThreadingHTTPServer: a stalled or aborted PDF stream must not block
    # every other request (the single-threaded TCPServer did exactly that).
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    httpd.daemon_threads = True
    print(f"Programme Academic Reader: http://localhost:{PORT}/")
    httpd.serve_forever()
