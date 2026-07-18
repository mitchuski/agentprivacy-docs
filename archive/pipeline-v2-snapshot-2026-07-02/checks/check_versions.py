#!/usr/bin/env python3
"""Version hygiene (GR-7 + retired citations): flags retired research-paper citations,
unconditioned static-ceiling statements, and header/metadata version fields for reconciliation."""
import re, sys
from _common import scan, report

RETIRED = [r"Research Paper v4\.0", r"Research Paper v4\.2", r"researchpaper_v4_0", r"researchpaper_v4_2"]
STATIC = re.compile(r"R\s*(?:_max)?\s*<\s*1|reconstruction ceiling", re.I)
COND = re.compile(r"precondition|conditional|non-collusion|R\(t\)|adversary class", re.I)

def main(paths):
    rc = 0
    for path in paths:
        p, text = scan(path)
        findings = []
        for pat in RETIRED:
            for m in re.finditer(pat, text):
                line = text[:m.start()].count("\n") + 1
                findings.append(f"{p.name}:{line} retired citation '{m.group(0)}'")
        for m in STATIC.finditer(text):
            line_no = text[:m.start()].count("\n") + 1
            # window: same paragraph (blank-line delimited)
            start = text.rfind("\n\n", 0, m.start()) + 1
            end = text.find("\n\n", m.end());  end = len(text) if end == -1 else end
            if not COND.search(text[start:end]):
                findings.append(f"{p.name}:{line_no} static-ceiling statement without conditioning in paragraph (GR-7)")
        for m in re.finditer(r"^\s*\**\s*[Vv]ersion:?\**\s*[|:]?\s*([0-9][0-9.]*)", text, re.M):
            line = text[:m.start()].count("\n") + 1
            findings.append(f"{p.name}:{line} version field '{m.group(1)}' — reconcile against PAPERS_INDEX")
        rc |= report(findings, f"versions:{p.name}")
    return rc

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
