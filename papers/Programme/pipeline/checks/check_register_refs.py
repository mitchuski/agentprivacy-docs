#!/usr/bin/env python3
"""C-number hygiene: no reference above register head; TIER-S must contain zero C-refs;
TIER-A C-refs must not carry percentage bands. Lists all refs for reconciliation."""
import re, sys
from _common import scan, tier_of, report, require_paths

HEAD = 97  # keep in sync with manifest register_head (bumped C96->C97 per L150, sync applied at the E3 build L153)

def main(paths):
    rc = 0
    for path in paths:
        p, text = scan(path)
        tier = tier_of(text)
        findings = []
        # match conjecture refs like C82, C82-C89, but not e.g. hex or C_S
        for m in re.finditer(r"\bC(\d{1,3})\b(?!_)", text):
            n = int(m.group(1))
            line = text[:m.start()].count("\n") + 1
            if n > HEAD:
                findings.append(f"{p.name}:{line} C{n} exceeds register head C{HEAD}")
            if tier == "S":
                findings.append(f"{p.name}:{line} C{n} present in TIER-S artifact (GR-2)")
            if tier == "A":
                ctx = text[m.start():m.start()+80]
                if re.search(r"\d{1,3}\s*%", ctx):
                    findings.append(f"{p.name}:{line} C{n} carries a %-band in TIER-A (GR-2)")
        rc |= report(findings, f"register_refs:{p.name}")
    return rc

if __name__ == "__main__":
    require_paths(sys.argv[1:], "register_refs")
    sys.exit(main(sys.argv[1:]))
