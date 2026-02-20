#!/usr/bin/env python3
"""
Build PDFs (with emoji support) and .tex from markdown for whitepaper, research paper, and VRC paper.
Uses: pandoc for md->html and md->tex; Playwright/Chromium for html->pdf (so emojis render).
Requires: pandoc on PATH, playwright + chromium (pip install playwright; python -m playwright install chromium).
"""
import os
import subprocess
import sys
from pathlib import Path

# Docs to build: (md_basename, title for HTML)
DOCS = [
    ("what-agentprivacy-is", "What Agentprivacy Is"),
    ("swordsman_mage_whitepaper_v4_8", "Swordsman and Mage Whitepaper v4.8"),
    ("dualprivacy_researchpaper_v3_6", "Dual Privacy Research Paper v3.6"),
    ("vrc_promise_protocol_economic_architecture_v3_0", "VRC Promise Protocol v3.0"),
]

# Minimal HTML style so PDF looks readable and emoji/symbols render
HTML_HEAD = """<meta charset="utf-8">
<style>
  body { font-family: 'Segoe UI', system-ui, sans-serif; line-height: 1.6; max-width: 800px; margin: 2em auto; padding: 0 1em; }
  pre, code { font-family: Consolas, monospace; background: #f4f4f4; padding: 0.2em 0.4em; border-radius: 3px; }
  pre { padding: 1em; overflow-x: auto; }
  table { border-collapse: collapse; width: 100%; }
  th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
  th { background: #f0f0f0; }
</style>
"""


def run(cmd, cwd=None):
    r = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        print(r.stderr or r.stdout, file=sys.stderr)
    return r.returncode


def main():
    root = Path(__file__).resolve().parent
    os.chdir(root)

    for base, title in DOCS:
        md = f"{base}.md"
        html = f"{base}.html"
        pdf = f"{base}.pdf"
        tex = f"{base}.tex"

        if not Path(md).exists():
            print(f"Skip {md} (not found)")
            continue

        print(f"Building {base}...")

        # 1. pandoc md -> html (standalone, UTF-8, with title)
        if run(f'pandoc "{md}" -s -o "{html}" --metadata title="{title}" -V lang=en') != 0:
            print(f"  pandoc html failed for {md}")
            continue
        # Inject styles: (1) after <head> for base typography, (2) before </head> override pandoc table styles so PDF tables render with borders
        with open(html, "r", encoding="utf-8") as f:
            content = f.read()
        if "<head>" in content and HTML_HEAD not in content:
            content = content.replace("<head>", "<head>\n" + HTML_HEAD, 1)
        TABLE_FIX = '<style>table{display:table !important;border-collapse:collapse;width:100%}thead th,tbody td,tbody th{border:1px solid #333 !important;padding:8px 12px !important}thead th{background:#e8e8e8 !important}</style>'
        if "</head>" in content and "display:table !important" not in content:
            content = content.replace("</head>", TABLE_FIX + "\n</head>", 1)
        with open(html, "w", encoding="utf-8") as f:
            f.write(content)

        # 2. html -> pdf via Playwright (emoji/symbols work)
        try:
            from playwright.sync_api import sync_playwright
            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page()
                page.goto(f"file://{root / html}", wait_until="networkidle")
                page.pdf(path=pdf, format="A4", margin={"top": "20mm", "bottom": "20mm", "left": "20mm", "right": "20mm"})
                browser.close()
            print(f"  -> {pdf}")
        except Exception as e:
            print(f"  Playwright PDF failed: {e}")

        # 3. pandoc md -> tex (for LaTeX source; emoji may show as missing in LaTeX build)
        if run(f'pandoc "{md}" -s -o "{tex}"') == 0:
            print(f"  -> {tex}")

        # Remove temporary HTML
        if Path(html).exists():
            Path(html).unlink()

    print("Done.")


if __name__ == "__main__":
    main()
