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

# Document files in order: (filename, title, description, file_type)
# file_type: 'md' for markdown, 'pdf' for PDF
DOCUMENTS = [
    ("0xagentprivacy_README_v1_1.md", "README v1.1 - Overview", "Complete introduction to the privacy-first AI agent architecture and documentation suite", "md"),
    ("swordsman_mage_whitepaper_v4_4.pdf", "Whitepaper v4.4 - Technical Architecture (PDF)", "Dual agent system design: Swordsman (protect) and Mage (delegate) - LaTeX PDF version", "pdf"),
    ("swordsman_mage_whitepaper_v4_4.md", "Whitepaper v4.4 - Technical Architecture", "Dual agent system design: Swordsman (protect) and Mage (delegate) - Markdown version", "md"),
    ("swordsman_mage_whitepaper_v4_3.md", "Whitepaper v4.3 - Technical Architecture", "Dual agent system design: Swordsman (protect) and Mage (delegate)", "md"),
    ("spellbook_v4_0_1_canonical.md", "Spellbook v4.0.1 - Narrative Framework", "Symbolic language, trust game mechanics, and recovery architecture for sovereign agency", "md"),
    ("tokenomics_economic_architecture_v2.md", "Tokenomics v2.0 - Economic Architecture", "Economic models, incentive structures, and dignity-based tokenomics for agent ecosystems", "md"),
    ("VISUAL_ARCHITECTURE_GUIDE_v1_1.md", "Visual Guide v1.1 - Diagrams & Flows", "Visual diagrams, system flows, and architectural illustrations of the agent framework", "md"),
    ("GLOSSARY_MASTER_v2_1.md", "Glossary v2.1 - Canonical Terminology", "Comprehensive glossary of terms, concepts, and definitions used across all documentation", "md"),
    ("research_proposal_v1_2.md", "Research Proposal v1.2 - Collaboration Invitation", "Research collaboration framework and invitation for academic and industry partnerships", "md"),
    ("dualprivacy_researchpaper_v3_3.md", "Research Paper v3.3 - Mathematical Foundations", "Formal mathematical models, proofs, and theoretical foundations of dual privacy mechanisms", "md"),
]

class DocsHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        path = urllib.parse.unquote(parsed_path.path.strip('/'))
        
        # Serve index page
        if path == '' or path == 'index.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(self.generate_index().encode('utf-8'))
            return
        
        # Special routes for README
        if path.lower() in ['readme', 'readme.md', '0xagentprivacy_readme', '0xagentprivacy_readme.md']:
            filename = '0xagentprivacy_README_v1_1.md'
            if os.path.exists(filename):
                self.send_response(200)
                self.send_header('Content-type', 'text/html; charset=utf-8')
                self.end_headers()
                with open(filename, 'r', encoding='utf-8') as f:
                    md_content = f.read()
                html = self.markdown_to_html(md_content, filename)
                self.wfile.write(html.encode('utf-8'))
                return
        
        # Serve PDF files
        if path.endswith('.pdf') or any((path == doc[0] or path.lower() == doc[0].lower()) and doc[3] == 'pdf' for doc in DOCUMENTS):
            filename = path
            if not filename.endswith('.pdf'):
                filename = next((doc[0] for doc in DOCUMENTS if (path == doc[0] or path.lower() == doc[0].lower()) and doc[3] == 'pdf'), None)
            
            if filename and os.path.exists(filename):
                self.send_response(200)
                self.send_header('Content-type', 'application/pdf')
                self.send_header('Content-Disposition', f'inline; filename="{filename}"')
                self.end_headers()
                
                # Read and serve PDF file
                with open(filename, 'rb') as f:
                    self.wfile.write(f.read())
                return
        
        # Serve markdown files as HTML
        # Check if path matches any markdown document (handle URL encoding)
        decoded_path = urllib.parse.unquote(path)
        if decoded_path.endswith('.md') or any((decoded_path == doc[0] or decoded_path.lower() == doc[0].lower() or path == urllib.parse.quote(doc[0])) and doc[3] == 'md' for doc in DOCUMENTS):
            # Find the actual file
            filename = decoded_path
            if not filename.endswith('.md') or not os.path.exists(filename):
                # Try to find by matching against DOCUMENTS list
                for doc in DOCUMENTS:
                    if doc[3] == 'md' and (decoded_path == doc[0] or decoded_path.lower() == doc[0].lower() or path == urllib.parse.quote(doc[0])):
                        filename = doc[0]
                        break
                else:
                    filename = None
            
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
    <title>0xagentprivacy Living Documentation</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            color: #e0e0e0;
            background: #1a1a1a;
            padding: 20px;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: #2d2d2d;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.5);
        }
        h1 {
            color: #ffffff;
            margin-bottom: 10px;
            font-size: 2.5em;
        }
        .subtitle {
            color: #b0b0b0;
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
            border: 2px solid #404040;
            border-radius: 8px;
            padding: 20px;
            transition: all 0.3s ease;
            background: #252525;
        }
        .doc-card:hover {
            border-color: #5a9fd4;
            box-shadow: 0 4px 12px rgba(90, 159, 212, 0.3);
            transform: translateY(-2px);
        }
        .doc-card h2 {
            color: #ffffff;
            margin-bottom: 10px;
            font-size: 1.3em;
        }
        .doc-card p {
            color: #b0b0b0;
        }
        .doc-card a {
            display: inline-block;
            margin-top: 15px;
            padding: 10px 20px;
            background: #5a9fd4;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            transition: background 0.3s;
        }
        .doc-card a:hover {
            background: #4a8fc4;
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
            background: #353535;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 30px;
            border-left: 4px solid #5a9fd4;
            color: #e0e0e0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>(⚔️⊥🧙)🙂 0xagentprivacy Living Documentation</h1>
        <p class="subtitle">Privacy-First AI Agent Architecture for Human Sovereignty</p>
        
        <div class="info">
            <strong>📚 Living Documentation</strong><br>
            All documents are available for review. Click any document to read it in full.
        </div>
        
        <div class="docs-grid">
"""
        
        for filename, title, description, file_type in DOCUMENTS:
            # Only show files that exist
            if not os.path.exists(filename):
                continue
                
            # Use simpler path for README
            if filename == '0xagentprivacy_README_v1_1.md':
                doc_path = 'README'
            else:
                doc_path = urllib.parse.quote(filename)
            
            # Different link text for PDFs
            link_text = "View PDF →" if file_type == 'pdf' else "Read Document →"
            
            html += f"""
            <div class="doc-card">
                <h2>{title}</h2>
                <p>{description}</p>
                <a href="/{doc_path}">{link_text}</a>
            </div>
"""
        
        html += """
        </div>
        
        <div style="margin-top: 40px; padding-top: 20px; border-top: 2px solid #404040; color: #b0b0b0; text-align: center;">
            <p>Server running on <strong style="color: #ffffff;">http://localhost:7000</strong></p>
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
            color: #e0e0e0;
            background: #1a1a1a;
            padding: 20px;
        }}
        .container {{
            max-width: 1000px;
            margin: 0 auto;
            background: #2d2d2d;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.5);
        }}
        .back-link {{
            display: inline-block;
            margin-bottom: 20px;
            padding: 10px 20px;
            background: #5a9fd4;
            color: white;
            text-decoration: none;
            border-radius: 5px;
        }}
        .back-link:hover {{
            background: #4a8fc4;
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: #ffffff;
            margin-top: 30px;
            margin-bottom: 15px;
        }}
        h1 {{ font-size: 2.5em; border-bottom: 3px solid #5a9fd4; padding-bottom: 10px; }}
        h2 {{ font-size: 2em; border-bottom: 2px solid #404040; padding-bottom: 8px; }}
        h3 {{ font-size: 1.5em; }}
        p {{ margin-bottom: 15px; color: #e0e0e0; }}
        code {{
            background: #1a1a1a;
            color: #a8d8ff;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
            border: 1px solid #404040;
        }}
        pre {{
            background: #1a1a1a;
            color: #e0e0e0;
            padding: 20px;
            border-radius: 5px;
            overflow-x: auto;
            margin: 20px 0;
            border: 1px solid #404040;
        }}
        pre code {{
            background: transparent;
            padding: 0;
            color: inherit;
            border: none;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }}
        th, td {{
            border: 1px solid #404040;
            padding: 12px;
            text-align: left;
        }}
        th {{
            background: #3d3d3d;
            color: #ffffff;
        }}
        tr:nth-child(even) {{
            background: #252525;
        }}
        tr:nth-child(odd) {{
            background: #2d2d2d;
        }}
        td {{
            color: #e0e0e0;
        }}
        blockquote {{
            border-left: 4px solid #5a9fd4;
            padding-left: 20px;
            margin: 20px 0;
            color: #b0b0b0;
            font-style: italic;
            background: #252525;
            padding: 15px 20px;
            border-radius: 4px;
        }}
        a {{
            color: #5a9fd4;
            text-decoration: none;
        }}
        a:hover {{
            color: #7ab8e4;
            text-decoration: underline;
        }}
        ul, ol {{
            margin-left: 30px;
            margin-bottom: 15px;
        }}
        li {{
            margin-bottom: 8px;
            color: #e0e0e0;
        }}
        strong {{
            color: #ffffff;
        }}
        em {{
            color: #b0b0b0;
        }}
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css">
    <style>
        /* Override highlight.js for better dark mode */
        .hljs {{
            background: #1a1a1a !important;
            color: #e0e0e0 !important;
        }}
    </style>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
    <script>hljs.highlightAll();</script>
</head>
<body>
    <div class="container">
        <a href="/" class="back-link">← Back to Index</a>
        {html_content}
        <div style="margin-top: 40px; padding-top: 20px; border-top: 2px solid #404040;">
            <a href="/" class="back-link">← Back to Index</a>
        </div>
    </div>
</body>
</html>"""
        return html

if __name__ == "__main__":
    import sys
    # Fix Windows console encoding for emojis
    if sys.platform == 'win32':
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
    
    handler = DocsHandler
    
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"Documentation server running at http://localhost:{PORT}")
        print(f"Serving {len(DOCUMENTS)} documents")
        print(f"Open http://localhost:{PORT} in your browser")
        print(f"Press Ctrl+C to stop")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped")

