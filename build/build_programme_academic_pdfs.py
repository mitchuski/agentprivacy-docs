#!/usr/bin/env python3
"""
Academic LaTeX/PDF exports for the V6 Rehydration Pipeline documents:
the tier-A papers, their supporting artefacts, the WP-14 literature-review
suite (combined into one document per run), and the autoresearch companion.

Pattern follows build_v6_academic_pdfs.py: pandoc md -> tex, fix-ups,
xelatex (two passes). Sources under papers/Programme/pipeline/ ·
PDFs to pdfs/programme/ · TeX to build/tex/programme/.
Requires pandoc and xelatex (MiKTeX) on PATH.

Frontmatter handling: the pipeline docs carry huge operational YAML blocks
(status lineage, extraction basis). Those are stripped; a clean title page
is generated from title/wp/tier/venue/date, with the operational status
line truncated into a small provenance note.
"""
import re
import subprocess
import sys
from pathlib import Path

BUILD_DIR = Path(__file__).resolve().parent
ROOT = BUILD_DIR.parent
PIPE = ROOT / "papers" / "Programme" / "pipeline"
ACAD = PIPE / "rehydrations" / "academic"
LITR = PIPE / "litreview"
PDFS = ROOT / "pdfs" / "programme"
TEX = BUILD_DIR / "tex" / "programme"
SRC = TEX / "src"

# Set to the author line you want on shareable/submission PDFs.
AUTHOR = "The Privacy-is-Value Research Programme"

# (source path, output basename, group) — group drives the viewer sections.
PAPERS = [
    (ACAD / "moving_ceiling_sok.md",            "WP-04_moving_ceiling_sok",       "paper"),
    (ACAD / "linear_cap_paper.md",              "WP-07_linear_cap",               "paper"),
    (ACAD / "rpp_adversarial.md",               "WP-11_rpp_adversarial",          "paper"),
    (ACAD / "weis_seventh_capital.md",          "WP-14_weis_seventh_capital",     "paper"),
    (ACAD / "conjecture_governance_method.md",  "WP-27_conjecture_governance",    "paper"),
    (ACAD / "rpp_adversarial_formalism.md",     "WP-11_formalism",                "support"),
    (ACAD / "rpp_adversarial_prereg.md",        "WP-11_prereg",                   "support"),
    (ACAD / "WP-11a_prior_art.md",              "WP-11a_prior_art",               "support"),
    (ACAD / "weis_prior_art_map.md",            "WP-14a_weis_prior_art_map",      "support"),
    (ACAD / "weis_valuation_methodology_v2_empirical.md", "WP-14_valuation_methodology_v2", "support"),
    (PIPE / "rehydrations" / "academic" / "autoresearch_companion.md", "PIPELINE_autoresearch_companion", "companion"),
    (PIPE / "chronicles" / "2026-08-17_veliz-normative-strand.md", "CHRONICLE_veliz_normative_strand", "companion"),
]

# Lit-review runs: each combines its files, in order, into one document.
LITREVIEW_RUNS = [
    ("LITREVIEW_run02", "WP-14 Literature Review — Adversarial Novelty Adjudication (Run 02)",
     ["RUN_MANIFEST.md", "gap_table.md", "contribution_claims.md",
      "ctr_candidates.md", "ctr_lr_02b_dp_stress.md", "bibliography.md"]),
    ("LITREVIEW_run03", "WP-14 Literature Review — Residue Stress Sweep (Run 03)",
     ["RUN_MANIFEST_03.md", "residue_verdicts_03.md", "bibliography_additions_03.md"]),
    ("LITREVIEW_run04", "WP-14 Literature Review — The Normative Strand (Run 04)",
     ["RUN_MANIFEST_04.md", "normative_strand_04.md", "bibliography_additions_04.md"]),
]

PANDOC_VARS = [
    "-V", "geometry:margin=27mm",
    "-V", "fontsize=11pt",
    "-V", "documentclass=article",
    # Cambria: full Greek/arrow/symbol coverage in prose (Latin Modern drops
    # ε, Φ, → etc. in text mode under xelatex); math in $...$ is unaffected.
    "-V", "mainfont=Cambria",
    "-V", "monofont=Consolas",
    "-V", "linkcolor=black",
    "-V", "urlcolor=blue",
    "-V", "colorlinks=true",
    "--pdf-engine=xelatex",  # ignored for -o .tex but harmless
]

FM_RE = re.compile(r"\A﻿?---\s*\n(.*?)\n---\s*\n", re.S)


def run(cmd, cwd=None, timeout=600):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True,
                          encoding="utf-8", errors="replace", timeout=timeout)


def parse_frontmatter(text):
    m = FM_RE.match(text)
    if not m:
        return {}, text
    fm, body = m.group(1), text[m.end():]
    meta = {}
    for line in fm.splitlines():
        km = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", line)
        if km:
            v = km.group(2).strip().strip('"').strip("'")
            meta[km.group(1).lower()] = v
    return meta, body


def first_h1(body):
    m = re.search(r"^#\s+(.+)$", body, re.M)
    return m.group(1).strip() if m else None


def strip_first_h1(body):
    return re.sub(r"^#\s+.+\n", "", body, count=1, flags=re.M)


def yaml_quote(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def prepare(md_path, name):
    """Strip operational frontmatter, emit clean pandoc source."""
    text = md_path.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)
    title = meta.get("title") or first_h1(body) or md_path.stem.replace("_", " ")
    if first_h1(body) and (meta.get("title") is None or
                           first_h1(body).lower()[:40] == title.lower()[:40]):
        body = strip_first_h1(body)
    bits = []
    for key, label in (("wp", None), ("tier", "tier"), ("venue", None),
                       ("venue_target", None), ("venue-target", None),
                       ("date", None), ("status", "status")):
        v = meta.get(key)
        if not v:
            continue
        if key == "status":
            v = v.split("(")[0].strip()[:60]
        bits.append(f"{label + ' ' if label else ''}{v}")
    subtitle = " · ".join(dict.fromkeys(bits))  # dedupe, keep order
    fm = ["---", f"title: {yaml_quote(title)}"]
    if subtitle:
        fm.append(f"subtitle: {yaml_quote(subtitle)}")
    fm += [f"author: {yaml_quote(AUTHOR)}",
           f"date: {yaml_quote(meta.get('date', ''))}", "---", ""]
    out = SRC / f"{name}.md"
    out.write_text("\n".join(fm) + body, encoding="utf-8")
    return out, title, meta


def prepare_litreview(name, title, files):
    parts = []
    date = ""
    for fn in files:
        p = LITR / fn
        if not p.exists():
            continue
        meta, body = parse_frontmatter(p.read_text(encoding="utf-8"))
        date = meta.get("date", date)
        parts.append(body.strip())
    if not parts:
        return None, None, None
    fm = ["---", f"title: {yaml_quote(title)}",
          f"author: {yaml_quote(AUTHOR)}", f"date: {yaml_quote(date)}", "---", ""]
    out = SRC / f"{name}.md"
    out.write_text("\n".join(fm) + "\n\n\\newpage\n\n".join(parts), encoding="utf-8")
    return out, title, {"date": date}


def fix_tex(tex):
    tex = re.sub(r"_\\int\b", r"_{\\int}", tex)
    return tex


def build_pdf(src_md, name):
    tex = TEX / f"{name}.tex"
    r = run(["pandoc", str(src_md), "-s", "-o", str(tex), *PANDOC_VARS])
    if r.returncode != 0:
        print(f"  pandoc failed: {r.stderr[:400]}")
        return None
    tex.write_text(fix_tex(tex.read_text(encoding="utf-8")), encoding="utf-8")
    for i in (1, 2):
        r = run(["xelatex", "-interaction=nonstopmode",
                 f"-output-directory={TEX}", f"-jobname={name}", str(tex)],
                cwd=str(TEX))
        if not (TEX / f"{name}.pdf").exists():
            tail = "\n".join((r.stdout or "").splitlines()[-12:])
            print(f"  xelatex pass {i} produced no PDF:\n{tail}")
            return None
    srcpdf, dst = TEX / f"{name}.pdf", PDFS / f"{name}.pdf"
    try:
        from pypdf import PdfReader
        pages = str(len(PdfReader(srcpdf).pages))
    except Exception:
        pages = ""
    try:
        if dst.exists():
            dst.unlink()
        srcpdf.replace(dst)
    except PermissionError:
        print(f"  NOTE: {dst.name} locked; fresh copy left in build/tex/programme/")
    for ext in (".aux", ".log", ".out", ".toc"):
        p = TEX / f"{name}{ext}"
        if p.exists():
            p.unlink()
    return pages


def main():
    for d in (PDFS, TEX, SRC):
        d.mkdir(parents=True, exist_ok=True)
    manifest, failures = [], []

    jobs = []
    for md, name, group in PAPERS:
        if not md.exists():
            print(f"Skip {md.name} (not found)")
            continue
        jobs.append((prepare(md, name), name, group, md))
    for name, title, files in LITREVIEW_RUNS:
        prep = prepare_litreview(name, title, files)
        if prep[0] is not None:
            jobs.append((prep, name, "litreview", LITR))

    for (src_md, title, meta), name, group, origin in jobs:
        print(f"Building {name} ...")
        pages = build_pdf(src_md, name)
        if pages is None:
            failures.append(name)
            continue
        print(f"  -> pdfs/programme/{name}.pdf ({pages} pages)")
        manifest.append({
            "name": name, "title": title, "group": group,
            "pages": pages, "date": (meta or {}).get("date", ""),
            "wp": (meta or {}).get("wp", ""),
            "venue": (meta or {}).get("venue") or (meta or {}).get("venue_target")
                     or (meta or {}).get("venue-target") or "",
            "status": ((meta or {}).get("status", "").split("(")[0].strip()[:80]),
        })

    import json
    (PDFS / "manifest.json").write_text(
        json.dumps(manifest, indent=1), encoding="utf-8")
    if failures:
        print(f"FAILED: {', '.join(failures)}")
        sys.exit(1)
    print(f"Done. {len(manifest)} PDFs -> pdfs/programme/")


if __name__ == "__main__":
    main()
