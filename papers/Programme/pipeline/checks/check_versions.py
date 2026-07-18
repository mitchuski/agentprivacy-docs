#!/usr/bin/env python3
"""Version hygiene (GR-7 + retired citations): flags retired research-paper citations,
unconditioned static-ceiling statements, and header/metadata version fields for reconciliation."""
import re, sys
from _common import scan, report, require_paths

# L024: pattern tolerates markdown emphasis and a colon, e.g. "**Research Paper:** v4.2".
RETIRED = [r"Research Paper\**:?\**\s*v4\.[02]", r"researchpaper_v4_0", r"researchpaper_v4_2"]
# RS-03 arm (L122(b)): the GR-7 retired sentence family, unconditional — no window rescue.
RETIRED_SENTENCES = [r"guarantee[s]?\s+that\s+adversar(?:y|ies)\s+cannot\s+reconstruct"]
# RS-01 arm (L122(b)): historical artefacts referenced without a status qualifier.
# Seed list; grows from SOURCES.md historical/superseded flags at future maintenance touches.
HISTORICAL = [r"agentprivacy-spellbook"]
HIST_RESCUE = re.compile(r"historical|superseded|archived|provenance|no longer|former|retired", re.I)
# L091(d): the R<1 arm is case-sensitive, word-bounded, and refuses digit runs
# (the "or <1450" class of false positive); the ceiling arm stays case-insensitive.
STATIC_PATTERNS = [re.compile(r"\bR\s*(?:_max)?\s*<\s*1(?!\d)"),
                   re.compile(r"reconstruction ceiling", re.I)]
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
        for pat in RETIRED_SENTENCES:
            for m in re.finditer(pat, text, re.I):
                line = text[:m.start()].count("\n") + 1
                findings.append(f"{p.name}:{line} retired sentence family (GR-7/RS-03) '{m.group(0)}'")
        for pat in HISTORICAL:
            for m in re.finditer(pat, text):
                line = text[:m.start()].count("\n") + 1
                # paragraph window rescue: a status qualifier in the same paragraph clears it (RS-01)
                start = text.rfind("\n\n", 0, m.start()) + 1
                end = text.find("\n\n", m.end());  end = len(text) if end == -1 else end
                if not HIST_RESCUE.search(text[start:end]):
                    findings.append(f"{p.name}:{line} historical artefact referenced without status qualifier (RS-01) '{m.group(0)}'")
        seen_static_lines = set()  # L024: dedupe static-ceiling findings per line
        for pat in STATIC_PATTERNS:
            for m in pat.finditer(text):
                line_no = text[:m.start()].count("\n") + 1
                if line_no in seen_static_lines:
                    continue
                # window: same paragraph (blank-line delimited)
                start = text.rfind("\n\n", 0, m.start()) + 1
                end = text.find("\n\n", m.end());  end = len(text) if end == -1 else end
                if not COND.search(text[start:end]):
                    seen_static_lines.add(line_no)
                    findings.append(f"{p.name}:{line_no} static-ceiling statement without conditioning in paragraph (GR-7)")
        for m in re.finditer(r"^\s*\**\s*[Vv]ersion:?\**\s*[|:]?\s*([0-9][0-9.]*)", text, re.M):
            line = text[:m.start()].count("\n") + 1
            findings.append(f"{p.name}:{line} version field '{m.group(1)}' — reconcile against PAPERS_INDEX")
        rc |= report(findings, f"versions:{p.name}")
    return rc

if __name__ == "__main__":
    require_paths(sys.argv[1:], "versions")
    sys.exit(main(sys.argv[1:]))
