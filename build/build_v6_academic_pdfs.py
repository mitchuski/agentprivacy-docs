#!/usr/bin/env python3
"""
Academic-style exports for the V6 canon papers: pandoc md -> tex, fix-ups,
xelatex (two passes) -> pdfs/v6/<base>_academic.pdf. Proper LaTeX math.
Layout: sources in papers/v6/ · PDFs to pdfs/v6/ · TeX to build/tex/v6/.
Emoji render blank in this edition by design; the web pipeline carries them.
Requires pandoc and xelatex (MiKTeX) on PATH.
"""
import re
import subprocess
import sys
from pathlib import Path

BUILD_DIR = Path(__file__).resolve().parent
ROOT = BUILD_DIR.parent
PAPERS = ROOT / "papers"
PDFS = ROOT / "pdfs" / "v6"
TEX = BUILD_DIR / "tex" / "v6"

# Paths relative to papers/ (without .md); output names use the basename.
DOCS = [
    "v6/privacy_value_v6_formal_specification",
    "v6/privacy_value_v6",
    "v6/pvm_v6_compressed",
    "v6/pvm_v6_companion_guide",
    "v6/dualprivacy_researchpaper_v6",
    "whitepapers/swordsman_mage_whitepaper_v6_3",
]

PANDOC_VARS = [
    "-V", "geometry:margin=25mm",
    "-V", "fontsize=11pt",
    "-V", "documentclass=article",
    "-V", "linkcolor=black",
    "-V", "urlcolor=blue",
]


def run(cmd, cwd=None, timeout=600):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True,
                          encoding="utf-8", errors="replace", timeout=timeout)


def fix_tex(tex: str) -> str:
    # Subscript \int needs braces under xelatex (the V5.4-lineage T_\int form).
    return re.sub(r"_\\int\b", r"_{\\int}", tex)


def main():
    PDFS.mkdir(parents=True, exist_ok=True)
    TEX.mkdir(parents=True, exist_ok=True)
    failures = []

    for base in DOCS:
        name = Path(base).name
        md = PAPERS / f"{base}.md"
        tex = TEX / f"{name}_academic.tex"
        if not md.exists():
            print(f"Skip {md} (not found)")
            continue
        print(f"Building {name}_academic ...")

        r = run(["pandoc", str(md), "-s", "-o", str(tex), *PANDOC_VARS])
        if r.returncode != 0:
            print(f"  pandoc tex failed: {r.stderr[:400]}")
            failures.append(base)
            continue

        tex.write_text(fix_tex(tex.read_text(encoding="utf-8")), encoding="utf-8")

        ok = True
        for i in (1, 2):
            r = run(["xelatex", "-interaction=nonstopmode",
                     f"-output-directory={TEX}",
                     f"-jobname={name}_academic", str(tex)], cwd=str(TEX))
            if not (TEX / f"{name}_academic.pdf").exists():
                ok = False
                tail = "\n".join((r.stdout or "").splitlines()[-12:])
                print(f"  xelatex pass {i} produced no PDF:\n{tail}")
                failures.append(base)
                break
        if ok:
            src = TEX / f"{name}_academic.pdf"
            dst = PDFS / f"{name}_academic.pdf"
            pages = ""
            log = TEX / f"{name}_academic.log"
            if log.exists():
                m = re.search(r"Output written on .*\((\d+) pages?", log.read_text(encoding="utf-8", errors="replace"))
                if m:
                    pages = f" ({m.group(1)} pages)"
            try:
                if dst.exists():
                    dst.unlink()
                src.replace(dst)
                print(f"  -> pdfs/v6/{name}_academic.pdf{pages}")
            except PermissionError:
                print(f"  NOTE: {dst.name} locked (open in a reader); fresh copy at build/tex/v6/{src.name}{pages}")

        for ext in (".aux", ".log", ".out", ".toc"):
            p = TEX / f"{name}_academic{ext}"
            if p.exists():
                p.unlink()

    if failures:
        print(f"FAILED: {', '.join(failures)}")
        sys.exit(1)
    print("Done.")


if __name__ == "__main__":
    main()
