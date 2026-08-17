#!/usr/bin/env python3
"""FC'27 anonymized LNCS fit-check render of WP-04 (moving-ceiling SoK).

Produces pdfs/programme/WP-04_FC27_anon.pdf in llncs format (FC'27 SoK
track: 20 pp + references/appendices) with the anonymization + apparatus
transforms applied mechanically:
  - frontmatter stripped (build pipeline standard)
  - author = "Anonymous Submission to FC 2027"; no provenance subtitle
  - extraction/traceability markers stripped: [E2-C02], [S1], [N3 residue], ...
  - WP-number self-references neutralised in prose
This is a FIT-CHECK draft. The submission itself rides P4 and the plan file
pipeline/submissions/FC27_WP-04_plan.md.
"""
import re
import sys
from pathlib import Path

BUILD_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BUILD_DIR))
from build_programme_academic_pdfs import (  # noqa: E402
    ACAD, PDFS, TEX, SRC, FM_RE, run, fix_tex, yaml_quote)

NAME = "WP-04_FC27_anon"
MD = ACAD / "moving_ceiling_sok.md"

MARKER = re.compile(
    r"\s*\[(?:E\d+-C\d+[^\]]*|S\d+[^\]]*|N\d+[^\]]*|bib:[^\]]*|A4[^\]]*)\]")


def main():
    for d in (PDFS, TEX, SRC):
        d.mkdir(parents=True, exist_ok=True)
    text = MD.read_text(encoding="utf-8")
    m = FM_RE.match(text)
    body = text[m.end():] if m else text
    body = re.sub(r"^#\s+.+\n", "", body, count=1, flags=re.M)
    body = MARKER.sub("", body)
    body = body.replace("WP-07", "the companion theory paper")
    body = body.replace("WP-04", "this paper")
    body = body.replace(
        "## References (verified registry; bib status per canonical pv_v6.bib)",
        "## References")

    fm = ["---",
          'title: "SoK: The Shelf Life of Privacy Guarantees"',
          f"author: {yaml_quote('Anonymous Submission to FC 2027')}",
          "---", ""]
    src = SRC / f"{NAME}.md"
    src.write_text("\n".join(fm) + body, encoding="utf-8")

    tex = TEX / f"{NAME}.tex"
    r = run(["pandoc", str(src), "-s", "-o", str(tex),
             "-V", "documentclass=llncs",
             "-V", "mainfont=Cambria",
             "-V", "linkcolor=black", "-V", "urlcolor=black",
             "--pdf-engine=xelatex"])
    if r.returncode != 0:
        print("pandoc failed:", r.stderr[:500])
        sys.exit(1)
    t = fix_tex(tex.read_text(encoding="utf-8"))
    # llncs supplies its own page geometry/headers; pandoc's default template
    # is compatible, but \institute is expected by \maketitle.
    t = t.replace("\\author{Anonymous Submission to FC 2027}",
                  "\\author{Anonymous Submission to FC 2027}\n"
                  "\\institute{Anonymized for review}")
    tex.write_text(t, encoding="utf-8")

    for i in (1, 2):
        r = run(["xelatex", "-interaction=nonstopmode",
                 f"-output-directory={TEX}", f"-jobname={NAME}", str(tex)],
                cwd=str(TEX))
        if not (TEX / f"{NAME}.pdf").exists():
            print(f"xelatex pass {i} produced no PDF:")
            print("\n".join((r.stdout or "").splitlines()[-15:]))
            sys.exit(1)

    srcpdf, dst = TEX / f"{NAME}.pdf", PDFS / f"{NAME}.pdf"
    from pypdf import PdfReader
    pages = len(PdfReader(srcpdf).pages)
    if dst.exists():
        dst.unlink()
    srcpdf.replace(dst)
    for ext in (".aux", ".log", ".out", ".toc"):
        p = TEX / f"{NAME}{ext}"
        if p.exists():
            p.unlink()
    print(f"-> pdfs/programme/{NAME}.pdf ({pages} pages; "
          f"FC'27 SoK budget = 20 + refs/appendices)")


if __name__ == "__main__":
    main()
