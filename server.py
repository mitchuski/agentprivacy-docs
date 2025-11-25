#!/usr/bin/env python3
"""
Simple documentation server for 0xagentprivacy docs
Serves markdown files as HTML at http://localhost:7000
"""

import http.server
import socketserver
import urllib.parse
import os
import markdown
from pathlib import Path

PORT = 7000

# Document files in order
DOCUMENTS = [
    ("0xagentprivacy_README.md", "README - Overview"),
    ("swordsman_mage_whitepaper_v4_3.md", "Whitepaper v4.3 - Technical Architecture"),
    ("dualprivacy_researchpaper_v3_2.md", "Research Paper v3.2 - Mathematical Foundations"),
    ("spellbook_v4_0_1_canonical.md", "Spellbook v4.0.1 - Narrative Framework"),
    ("tokenomics_economic_architecture_v2.md", "Tokenomics v2.0 - Economic Architecture"),
    ("VISUAL_ARCHITECTURE_GUIDE_v1_1.md", "Visual Guide v1.1 - Diagrams & Flows"),
    ("research_proposal_v1_1.md", "Research Proposal v1.1 - Collaboration Invitation"),
    ("GLOSSARY_MASTER_v2.md", "Glossary v2.0 - Canonical Terminology"),
]

class DocsHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path.strip('/')
        
        # Serve index page
        if path == '' or path == 'index.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(self.generate_index().encode('utf-8'))
            return
        
        # Serve markdown files as HTML
        if path.endswith('.md') or any(path == doc[0] for doc in DOCUMENTS):
            # Find the actual file
            filename = path
            if not filename.endswith('.md'):
                filename = next((doc[0] for doc in DOCUMENTS if path == doc[0]), None)
            
            if filename and os.path.exists(filename):
                self.send_response(200)
                self.send_header('Content-type', 'text/html; charset=utf-8')
                self.end_headers()
                
                # Read and convert markdown to HTML
                with open(filename, 'r', encoding='utf-8') as f:
                    md_content = f.read()
                
                html = self.markdown_to_html(md_content, filename)
                self.wfile.write(html.encode('utf-8'))
                return
        
        # Default: try to serve file
        return super().do_GET()
    
    def generate_index(self):
        html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>0xagentprivacy Documentation Suite</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #f5f5f5;
            padding: 20px;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
            margin-bottom: 10px;
            font-size: 2.5em;
        }
        .subtitle {
            color: #7f8c8d;
            margin-bottom: 30px;
            font-size: 1.2em;
        }
        .docs-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }
        .doc-card {
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            padding: 20px;
            transition: all 0.3s ease;
            background: #fafafa;
        }
        .doc-card:hover {
            border-color: #3498db;
            box-shadow: 0 4px 12px rgba(52, 152, 219, 0.2);
            transform: translateY(-2px);
        }
        .doc-card h2 {
            color: #2c3e50;
            margin-bottom: 10px;
            font-size: 1.3em;
        }
        .doc-card a {
            display: inline-block;
            margin-top: 15px;
            padding: 10px 20px;
            background: #3498db;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            transition: background 0.3s;
        }
        .doc-card a:hover {
            background: #2980b9;
        }
        .status {
            display: inline-block;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 0.85em;
            margin-left: 10px;
        }
        .status.complete { background: #2ecc71; color: white; }
        .info {
            background: #ecf0f1;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 30px;
            border-left: 4px solid #3498db;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>⚔️🧙 0xagentprivacy Documentation Suite</h1>
        <p class="subtitle">Privacy-First AI Agent Architecture for Human Sovereignty</p>
        
        <div class="info">
            <strong>📚 Complete Documentation Suite</strong><br>
            All documents are available for review. Click any document to read it in full.
        </div>
        
        <div class="docs-grid">
"""
        
        for filename, title in DOCUMENTS:
            doc_path = filename
            html += f"""
            <div class="doc-card">
                <h2>{title}</h2>
                <p>Click to read the full document</p>
                <a href="/{doc_path}">Read Document →</a>
            </div>
"""
        
        html += """
        </div>
        
        <div style="margin-top: 40px; padding-top: 20px; border-top: 2px solid #e0e0e0; color: #7f8c8d; text-align: center;">
            <p>Server running on <strong>http://localhost:7000</strong></p>
            <p>All documents served as HTML with syntax highlighting</p>
        </div>
    </div>
</body>
</html>"""
        return html
    
    def markdown_to_html(self, md_content, filename):
        # Convert markdown to HTML
        md = markdown.Markdown(extensions=['extra', 'codehilite', 'tables', 'fenced_code'])
        html_content = md.convert(md_content)
        
        # Wrap in full HTML document
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{filename} - 0xagentprivacy Docs</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.8;
            color: #333;
            background: #f5f5f5;
            padding: 20px;
        }}
        .container {{
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        .back-link {{
            display: inline-block;
            margin-bottom: 20px;
            padding: 10px 20px;
            background: #3498db;
            color: white;
            text-decoration: none;
            border-radius: 5px;
        }}
        .back-link:hover {{
            background: #2980b9;
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: #2c3e50;
            margin-top: 30px;
            margin-bottom: 15px;
        }}
        h1 {{ font-size: 2.5em; border-bottom: 3px solid #3498db; padding-bottom: 10px; }}
        h2 {{ font-size: 2em; border-bottom: 2px solid #e0e0e0; padding-bottom: 8px; }}
        h3 {{ font-size: 1.5em; }}
        p {{ margin-bottom: 15px; }}
        code {{
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
        }}
        pre {{
            background: #2c3e50;
            color: #ecf0f1;
            padding: 20px;
            border-radius: 5px;
            overflow-x: auto;
            margin: 20px 0;
        }}
        pre code {{
            background: transparent;
            padding: 0;
            color: inherit;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }}
        th {{
            background: #3498db;
            color: white;
        }}
        tr:nth-child(even) {{
            background: #f9f9f9;
        }}
        blockquote {{
            border-left: 4px solid #3498db;
            padding-left: 20px;
            margin: 20px 0;
            color: #555;
            font-style: italic;
        }}
        a {{
            color: #3498db;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        ul, ol {{
            margin-left: 30px;
            margin-bottom: 15px;
        }}
        li {{
            margin-bottom: 8px;
        }}
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
    <script>hljs.highlightAll();</script>
</head>
<body>
    <div class="container">
        <a href="/" class="back-link">← Back to Index</a>
        {html_content}
        <div style="margin-top: 40px; padding-top: 20px; border-top: 2px solid #e0e0e0;">
            <a href="/" class="back-link">← Back to Index</a>
        </div>
    </div>
</body>
</html>"""
        return html

if __name__ == "__main__":
    handler = DocsHandler
    
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"🚀 Documentation server running at http://localhost:{PORT}")
        print(f"📚 Serving {len(DOCUMENTS)} documents")
        print(f"📖 Open http://localhost:{PORT} in your browser")
        print(f"⏹️  Press Ctrl+C to stop")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n👋 Server stopped")

