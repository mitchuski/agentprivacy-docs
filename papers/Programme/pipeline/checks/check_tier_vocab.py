#!/usr/bin/env python3
"""Tier vocabulary (GR-4/GR-5): mythopoetic terms and emoji banned at TIER-S/A;
em-dashes banned at TIER-P/G prose; confidence-band language banned at TIER-S/A."""
import re, sys
from _common import scan, tier_of, report, require_paths

MYTHOS = [r"\bSwordsman\b", r"\bMage\b(?!s? Reading)", r"City of Mages", r"\bFirst Person\b",
          r"Amnesia Protocol", r"\bSelene\b", r"\bgrimoire\b", r"\bspellbook\b"]
EMOJI = re.compile("[\U0001F300-\U0001FAFF\u2600-\u27BF\u2FFB]")
CONF = re.compile(r"(~\s*\d{1,3}\s*%|\bconfidence\b.{0,20}\d{1,3}\s*%|\d{1,3}\s*%\s*confidence)", re.I)

def main(paths):
    rc = 0
    for path in paths:
        p, text = scan(path)
        tier = tier_of(text)
        findings = []
        body = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)  # skip frontmatter
        if tier in ("S", "A"):
            for pat in MYTHOS:
                for m in re.finditer(pat, body):
                    line = body[:m.start()].count("\n") + 1
                    findings.append(f"{p.name}:~{line} mythopoetic term '{m.group(0)}' at TIER-{tier} (GR-4)")
            for m in EMOJI.finditer(body):
                line = body[:m.start()].count("\n") + 1
                findings.append(f"{p.name}:~{line} emoji at TIER-{tier} (GR-4)")
            for m in CONF.finditer(body):
                line = body[:m.start()].count("\n") + 1
                findings.append(f"{p.name}:~{line} confidence-band language at TIER-{tier} (GR-2)")
        if tier in ("P", "G"):
            for m in re.finditer("—", body):
                line = body[:m.start()].count("\n") + 1
                findings.append(f"{p.name}:~{line} em-dash at TIER-{tier} (GR-5)")
        rc |= report(findings, f"tier_vocab:{p.name}")
    return rc

if __name__ == "__main__":
    require_paths(sys.argv[1:], "tier_vocab")
    sys.exit(main(sys.argv[1:]))
