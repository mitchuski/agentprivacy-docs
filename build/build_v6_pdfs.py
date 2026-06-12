#!/usr/bin/env python3
"""
Web-pipeline PDFs for the V6 canon papers (full emoji fidelity, MathJax-typeset).
Layout: sources in papers/v6/ · PDFs to pdfs/v6/ · TeX to build/tex/v6/.
Run from anywhere: paths resolve relative to this script (repo_root/build/).
Requires pandoc, playwright + chromium.
"""
import subprocess
import sys
from pathlib import Path

BUILD_DIR = Path(__file__).resolve().parent
ROOT = BUILD_DIR.parent
PAPERS = ROOT / "papers"
PDFS = ROOT / "pdfs" / "v6"
TEX = BUILD_DIR / "tex" / "v6"

# Entries are paths relative to papers/ (without .md); output names use the basename.
DOCS = [
    ("v6/privacy_value_v6_formal_specification", "Privacy is Value · V6: The Gathering Turn and the Moving Ceiling — Formal Specification"),
    ("v6/privacy_value_v6", "Privacy is Value · V6: The Crosswalk Edition (V5.4 to V6)"),
    ("v6/pvm_v6_compressed", "Privacy is Value · V6: The Swordsman Reading — Compressed Specification"),
    ("v6/pvm_v6_companion_guide", "Privacy is Value · V6: The Mage Reading — Companion Guide"),
    ("v6/dualprivacy_researchpaper_v6", "Privacy is Value · V6: The Research Paper Edition"),
    ("whitepapers/swordsman_mage_whitepaper_v6_3", "Privacy is Value · V6: The Whitepaper — Swordsman and Mage: Dual Agents Derived from the First Person"),
]

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


def run(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        print(r.stderr or r.stdout, file=sys.stderr)
    return r.returncode


def main():
    PDFS.mkdir(parents=True, exist_ok=True)
    TEX.mkdir(parents=True, exist_ok=True)

    for base, title in DOCS:
        name = Path(base).name
        md = PAPERS / f"{base}.md"
        html = BUILD_DIR / f"{name}.html"
        pdf = PDFS / f"{name}.pdf"
        tex = TEX / f"{name}.tex"

        if not md.exists():
            print(f"Skip {md} (not found)")
            continue

        print(f"Building {name}...")

        if run(f'pandoc "{md}" -s -o "{html}" --mathjax --metadata title="{title}" -V lang=en') != 0:
            print(f"  pandoc html failed for {md}")
            continue
        content = html.read_text(encoding="utf-8")
        if "<head>" in content and HTML_HEAD not in content:
            content = content.replace("<head>", "<head>\n" + HTML_HEAD, 1)
        TABLE_FIX = '<style>table{display:table !important;border-collapse:collapse;width:100%}thead th,tbody td,tbody th{border:1px solid #333 !important;padding:8px 12px !important}thead th{background:#e8e8e8 !important}</style>'
        if "</head>" in content and "display:table !important" not in content:
            content = content.replace("</head>", TABLE_FIX + "\n</head>", 1)
        html.write_text(content, encoding="utf-8")

        try:
            from playwright.sync_api import sync_playwright
            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page()
                page.goto(f"file://{html}", wait_until="networkidle")
                # Wait for MathJax to finish typesetting (best effort).
                try:
                    page.wait_for_selector("mjx-container", timeout=20000)
                    page.wait_for_timeout(1500)
                except Exception:
                    pass
                page.pdf(path=str(pdf), format="A4", margin={"top": "20mm", "bottom": "20mm", "left": "20mm", "right": "20mm"})
                browser.close()
            print(f"  -> {pdf.relative_to(ROOT)}")
        except Exception as e:
            print(f"  Playwright PDF failed: {e}")

        if run(f'pandoc "{md}" -s -o "{tex}"') == 0:
            print(f"  -> {tex.relative_to(ROOT)}")

        if html.exists():
            html.unlink()

    print("Done.")


if __name__ == "__main__":
    main()
