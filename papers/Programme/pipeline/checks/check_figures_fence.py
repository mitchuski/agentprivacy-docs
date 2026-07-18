#!/usr/bin/env python3
"""Canonical figures fence (GR-3): flags 678x, 31,000x, 70:1, 74x, $47k-52k.
TIER-A/S: any occurrence fails. Other tiers: reported for sanctioned-form review."""
import re, sys
from _common import scan, tier_of, report, require_paths

PATTERNS = [
    (r"\b678\s*[x×]", "678x"),
    (r"\b31[,.]?000\s*[x×]", "31,000x"),
    (r"\b70\s*:\s*1\b", "70:1"),
    (r"\b74\s*[x×]", "74x"),
    (r"\$4[7-9]k|\$5[0-2]k", "$47-52k"),
]

def main(paths):
    rc = 0
    for path in paths:
        p, text = scan(path)
        tier = tier_of(text)
        findings = []
        for pat, name in PATTERNS:
            for m in re.finditer(pat, text, re.I):
                line = text[:m.start()].count("\n") + 1
                if tier in ("S", "A"):
                    findings.append(f"{p.name}:{line} canonical figure {name} in TIER-{tier} (GR-3: not at all)")
                else:
                    findings.append(f"{p.name}:{line} canonical figure {name} — verify sanctioned formulation")
        rc |= report(findings, f"figures_fence:{p.name}")
    return rc

if __name__ == "__main__":
    require_paths(sys.argv[1:], "figures_fence")
    sys.exit(main(sys.argv[1:]))
