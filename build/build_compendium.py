#!/usr/bin/env python3
"""
Assembles Privacy is Value: The Compendium from the manifests' order and renders
it: web PDF (MathJax + Playwright) always; academic PDF (xelatex) best-effort.
The assembly inherits the living corpus: edits to any member flow into the next
build. Outputs: compendium/_assembled/ (md) and pdfs/compendium/ (renders).
"""
import re
import subprocess
import sys
from pathlib import Path

BUILD_DIR = Path(__file__).resolve().parent
ROOT = BUILD_DIR.parent
OUT_MD = ROOT / "compendium" / "_assembled"
OUT_PDF = ROOT / "pdfs" / "compendium"
NAME = "privacy_is_value_compendium"
TITLE = "Privacy is Value: The Compendium"

PAGEBREAK = (
    "\n\n```{=latex}\n\\clearpage\n```\n"
    "<div style=\"page-break-before: always\"></div>\n\n"
)


def part(title, subtitle):
    return f"{PAGEBREAK}\n# {title}\n\n*{subtitle}*\n{PAGEBREAK}"


# (kind, payload): 'f' = file path relative to ROOT · 't' = generated text
SEQUENCE = [
    ("f", "compendium/00-front-matter/01-thesis.md"),
    ("f", "compendium/00-front-matter/02-how-to-read.md"),
    ("f", "compendium/00-front-matter/03-one-work-many-expressions.md"),

    ("t", part("PART I · The Equation Assembles", "V1 to V4 · 2025 to February 2026")),
    ("f", "compendium/part-i-the-equation-assembles/RETROSPECTIVE.md"),
    ("f", "papers/v4/privacy_value_v4_formal_specification.md"),
    ("f", "papers/lineage/dualprivacy_researchpaper_v4_3.md"),
    ("f", "papers/v4/privacy_is_value_v4.md"),

    ("t", part("PART II · The Amnesia Protocol", "V5 to V5.4 · February to May 2026")),
    ("f", "compendium/part-ii-the-amnesia-protocol/RETROSPECTIVE.md"),
    ("f", "papers/v5/privacy_value_v5_4_formal_specification.md"),
    ("f", "papers/v5/pvm_v5_4_compressed.md"),
    ("f", "papers/v5/pvm_v5_4_companion_guide.md"),
    ("f", "papers/v5/privacy_is_value_v5.md"),
    ("f", "research/privacy_value_v5_1_research_note.md"),
    ("f", "research/privacy_value_v5_2_research_note.md"),
    ("f", "research/privacy_value_v5_3_research_note.md"),
    ("f", "research/privacy_value_v5_2_canonical.md"),

    ("t", part("PART III · The Attachment", "V5.5, the sublayer · May 2026")),
    ("f", "compendium/part-iii-the-attachment/THE-SUBLAYER.md"),
    ("f", "reference/MAPPING_ADDITIONS_V5_5_2026-05-11.md"),

    ("t", part("PART IV · The Gathering Turn and the Moving Ceiling", "V6 · April to June 2026 · the current volume")),
    ("f", "compendium/part-iv-the-gathering-turn/RETROSPECTIVE.md"),
    ("f", "papers/v6/privacy_value_v6_formal_specification.md"),
    ("f", "papers/v6/pvm_v6_compressed.md"),
    ("f", "papers/v6/pvm_v6_companion_guide.md"),
    ("f", "papers/v6/dualprivacy_researchpaper_v6.md"),
    ("f", "papers/whitepapers/swordsman_mage_whitepaper_v6_3.md"),
    ("f", "papers/v6/privacy_value_v6.md"),
    ("f", "research/pvm-v6-lorenz-attractor.md"),
    ("f", "research/pvm-v6-eml-three-ceilings.md"),
    ("f", "research/pvm-v6-arch1-canonical-form.md"),
    ("f", "research/pvm-v6-1-bakhta-half-life.md"),
    ("f", "research/pvm-v6-convergence-wound-and-cap.md"),
    ("f", "research/v6_1_research_note.md"),
    ("f", "research/schrottenloher-ecdlp-v6-note.md"),
    ("f", "research/pvm-v6-arch1rt-operational-reachability.md"),
    ("f", "research/pvm-v6-bakhta-integrity-gap-convergence.md"),
    ("f", "research/2026-06-09_horizon_district_cryptographic_durability_note.md"),
    ("f", "research/aletheia-and-lethe.md"),
    ("f", "research/privacy_value_v6_horizon_note.md"),

    ("t", part("THE SPINE", "apparatus, current at build date")),
    ("f", "research/CONJECTURE_REGISTER_V6.md"),
    ("f", "reference/GLOSSARY_MASTER_v4_0.md"),
    ("f", "reference/promise_theory_reference_v1_4.md"),
    ("f", "reference/PAPERS_INDEX.md"),
    ("t", "## The consolidated bibliography\n\nThe V6 volume's §33 (Part IV) merges the V5.4 reference list verbatim with the V6 additions and is the book's consolidated bibliography; the V4-era references travel with their documents in Part I. A deduplicated re-set is a print-edition task, deferred by plan."),

    ("t", part("BACK MATTER", "the watermark, the concordances, the colophon")),
    ("f", "compendium/back-matter/honest-limits-ledger.md"),
    ("f", "compendium/back-matter/narrative-concordance.md"),
    ("f", "compendium/back-matter/chronicle-concordance.md"),
    ("f", "compendium/back-matter/colophon.md"),
]


def strip_frontmatter(text):
    if text.startswith("---"):
        m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
        if m:
            tm = re.search(r'^title:\s*"?(.*?)"?\s*$', m.group(1), re.MULTILINE)
            lead = f"*{tm.group(1)}*\n\n" if tm else ""
            return lead + text[m.end():]
    return text


def run(cmd, cwd=None, timeout=1800):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True,
                          encoding="utf-8", errors="replace", timeout=timeout)


def main():
    OUT_MD.mkdir(parents=True, exist_ok=True)
    OUT_PDF.mkdir(parents=True, exist_ok=True)

    pieces, missing = [], []
    for kind, payload in SEQUENCE:
        if kind == "t":
            pieces.append(payload)
            continue
        p = ROOT / payload
        if not p.exists():
            missing.append(payload)
            continue
        pieces.append(strip_frontmatter(p.read_text(encoding="utf-8")))
    body = PAGEBREAK.join(pieces)
    md = OUT_MD / f"{NAME}.md"
    md.write_text(body, encoding="utf-8")
    print(f"assembled: {md.relative_to(ROOT)} ({len(body):,} chars, {len(pieces)} pieces)")
    if missing:
        print("MISSING (skipped): " + ", ".join(missing))

    # Web render
    html = OUT_MD / f"{NAME}.html"
    r = run(["pandoc", str(md), "-s", "-o", str(html), "--mathjax",
             "--metadata", f"title={TITLE}", "-V", "lang=en"])
    if r.returncode != 0:
        print("pandoc html failed:", (r.stderr or "")[:300])
    else:
        try:
            from playwright.sync_api import sync_playwright
            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page()
                page.goto(f"file://{html}", wait_until="networkidle", timeout=120000)
                try:
                    page.wait_for_selector("mjx-container", timeout=30000)
                    page.wait_for_timeout(5000)
                except Exception:
                    pass
                page.pdf(path=str(OUT_PDF / f"{NAME}.pdf"), format="A4",
                         margin={"top": "20mm", "bottom": "20mm", "left": "20mm", "right": "20mm"})
                browser.close()
            print(f"-> pdfs/compendium/{NAME}.pdf")
        except Exception as e:
            print(f"Playwright PDF failed: {e}")
        finally:
            if html.exists():
                html.unlink()

    # Academic render, best effort
    tex = OUT_MD / f"{NAME}_academic.tex"
    r = run(["pandoc", str(md), "-s", "-o", str(tex),
             "-V", "geometry:margin=25mm", "-V", "fontsize=10pt",
             "-V", "documentclass=report", "-V", "linkcolor=black", "-V", "urlcolor=blue",
             "--metadata", f"title={TITLE}"])
    if r.returncode != 0:
        print("pandoc tex failed:", (r.stderr or "")[:300])
        sys.exit(0)
    t = tex.read_text(encoding="utf-8")
    t = re.sub(r"_\\int\b", r"_{\\int}", t)
    tex.write_text(t, encoding="utf-8")
    ok = True
    for i in (1, 2):
        r = run(["xelatex", "-interaction=nonstopmode",
                 f"-output-directory={OUT_MD}", f"-jobname={NAME}_academic",
                 str(tex)], cwd=str(OUT_MD))
        if not (OUT_MD / f"{NAME}_academic.pdf").exists():
            ok = False
            print(f"xelatex pass {i} produced no PDF; tail:")
            print("\n".join((r.stdout or "").splitlines()[-10:]))
            break
    if ok:
        pages = ""
        log = OUT_MD / f"{NAME}_academic.log"
        if log.exists():
            m = re.search(r"Output written on .*\((\d+) pages?",
                          log.read_text(encoding="utf-8", errors="replace"))
            if m:
                pages = f" ({m.group(1)} pages)"
        (OUT_MD / f"{NAME}_academic.pdf").replace(OUT_PDF / f"{NAME}_academic.pdf")
        print(f"-> pdfs/compendium/{NAME}_academic.pdf{pages}")
    for ext in (".aux", ".log", ".out", ".toc"):
        p = OUT_MD / f"{NAME}_academic{ext}"
        if p.exists():
            p.unlink()
    print("Done.")


if __name__ == "__main__":
    main()
