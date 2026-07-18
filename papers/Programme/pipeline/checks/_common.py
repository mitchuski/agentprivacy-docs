"""Shared helpers for pipeline checks."""
import re, sys, pathlib

def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip().strip('"')
    return fm

def tier_of(text):
    t = frontmatter(text).get("tier", "").upper()
    return t if t in ("S", "A", "G", "P", "D", "INTERNAL") else None

def scan(path):
    p = pathlib.Path(path)
    return p, p.read_text(encoding="utf-8", errors="replace")

def require_paths(paths, name="check"):
    """L082(c): an argv-less invocation must fail loudly, never pass vacuously."""
    if not paths:
        print(f"[{name}] ERROR · no input files given; a pathless run proves nothing (L082)",
              file=sys.stderr)
        sys.exit(2)

def report(findings, name):
    if findings:
        print(f"[{name}] FAIL · {len(findings)} finding(s)")
        for f in findings:
            print("  -", f)
        return 1
    print(f"[{name}] PASS")
    return 0
