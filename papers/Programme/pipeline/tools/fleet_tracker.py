#!/usr/bin/env python3
"""Fleet Tracker · V6 Rehydration Pipeline · generated wall-board + document reader.

One readable site that answers "what did the fleet do and what needs me" without
opening a dozen files. It is an instrument: it displays pipeline state, it never
owns it. The manifest stays the map, the ledger stays the memory; this renders them.

GR-6 applies: everything under tracker/ is GENERATED. Never hand-edit the HTML;
fix the sources or this generator and rebuild.

Sources read (all under --root, default: the pipeline directory above tools/):
  manifest.yaml                  artifact + extraction state (A0-owned)
  reviews/critiques_ledger.md    append-only findings ledger
  chronicles/*.md                one per session, frontmatter-dated
  tasks/*.md                     task cards, frontmatter
  every other *.md / *.yaml / checks/*.py   rendered as reader pages

Designed to be pipeline-agnostic for future auto-research programmes: point
--root at any directory with the same manifest/ledger/chronicles/tasks shape.

Usage:
  python tools/fleet_tracker.py                  # generate tracker/
  python tools/fleet_tracker.py --serve          # generate then serve (default port 7272)
  python tools/fleet_tracker.py --no-checks      # skip shelling the checks/ suite
  python tools/fleet_tracker.py --stamp "2026-07-03 12:00"   # reproducible stamp
"""
import argparse
import html as html_mod
import io
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------- configuration

GATES = ["P0", "P1", "P2", "P3", "P4"]
SKIP_DIRS = {"tools", "tracker", "__pycache__", ".git"}
# canon surfaces (read-only upstream), resolved relative to the repo root if present
CANON_GLOBS = [
    "papers/v6/*.md",
    "papers/whitepapers/*.md",
    "research/CONJECTURE_REGISTER_V6.md",
]
LEDGER_TAIL = 14

# palette per the tracker note (first-person directed 2026-07-03)
CSS_BOARD = """
:root{--ground:#1c2126;--panel:#252c33;--paper:#e8e4d9;--amber:#d99a3d;
--green:#5a9e6f;--red:#c25b4e;--grey:#6b7680;--line:#39424c;}
*{margin:0;padding:0;box-sizing:border-box}
body{background:var(--ground);color:var(--paper);font-family:'Segoe UI',-apple-system,sans-serif;
line-height:1.55;padding:28px 20px 80px}
.wrap{max-width:1100px;margin:0 auto}
a{color:#c9b48a;text-decoration:none}a:hover{color:var(--amber);text-decoration:underline}
.mono{font-family:ui-monospace,Consolas,monospace;font-variant-numeric:tabular-nums}
header.mast{border-bottom:2px solid var(--line);padding-bottom:14px;margin-bottom:22px}
header.mast h1{font-family:Fraunces,Georgia,serif;font-style:italic;font-weight:500;
font-size:1.9em;color:var(--paper);letter-spacing:.01em}
.maststats{display:flex;flex-wrap:wrap;gap:10px 26px;margin-top:8px;color:#aab2ba;font-size:.92em}
.maststats b{color:var(--paper);font-weight:600}
section{margin:30px 0}
h2{font-size:1.12em;font-weight:600;letter-spacing:.04em;text-transform:uppercase;
color:#aab2ba;margin-bottom:12px}
.needs{background:linear-gradient(180deg,#2d2820,#282318);border:1px solid #6b5426;
border-left:4px solid var(--amber);border-radius:4px;padding:16px 18px}
.needs h2{color:var(--amber)}
.needs li{margin:9px 0 9px 18px;color:#e8dfc9}
.needs .ln{color:var(--amber);font-weight:600}
.needs .where{color:#9a917c;font-size:.88em}
table{width:100%;border-collapse:collapse;font-size:.92em}
th{color:#8a939d;text-align:left;font-weight:600;padding:7px 10px;border-bottom:1px solid var(--line);
font-size:.85em;letter-spacing:.05em;text-transform:uppercase}
td{padding:8px 10px;border-bottom:1px solid #2c343d;vertical-align:top}
tr:hover td{background:#272f37}
.scroll{overflow-x:auto;background:var(--panel);border:1px solid var(--line);border-radius:4px;padding:4px 8px}
.chip{display:inline-block;padding:1px 8px;border-radius:3px;font-size:.82em;font-weight:600;
font-family:ui-monospace,Consolas,monospace}
.tier-S{background:#4a3a5e;color:#d8c8f0}.tier-A{background:#2e4a5e;color:#bfe0f5}
.tier-G{background:#5e4a2e;color:#f0dcb8}.tier-P{background:#2e5e46;color:#bff0d5}
.tier-D{background:#44505c;color:#d5dee8}.tier-internal{background:#3a4148;color:#aab4be}
.st-done,.st-release-draft-v5{color:var(--green)}.st-pending{color:var(--grey)}
.st-parked{color:var(--grey);font-style:italic}.st-ongoing{color:#c9b48a}
.gate{white-space:nowrap;font-family:ui-monospace,Consolas,monospace;font-size:.85em}
.gate i{display:inline-block;width:13px;height:13px;border-radius:50%;margin-right:3px;
border:1.5px solid var(--grey);vertical-align:-2px;font-style:normal}
.gate i.on{background:var(--green);border-color:var(--green)}
.gate i.p4{border-color:var(--amber)}
.gate i.p4.on{background:var(--amber)}
.due-hard{color:var(--red);font-weight:600}
.note{color:#98a1aa;font-size:.88em;max-width:340px}
.lane{background:var(--panel);border:1px solid var(--line);border-radius:4px;
padding:12px 14px;margin-bottom:10px}
.lane .d{color:var(--amber);font-weight:600;font-family:ui-monospace,Consolas,monospace;margin-bottom:6px}
.sess{display:inline-block;background:#2c343d;border:1px solid var(--line);border-radius:3px;
padding:4px 10px;margin:3px 4px 3px 0;font-size:.86em}
.sess .r{color:#c9b48a;font-weight:600}
.led{border-left:3px solid var(--grey);background:var(--panel);border-radius:0 4px 4px 0;
padding:9px 13px;margin:7px 0;font-size:.9em}
.led.canon{border-left-color:var(--red)}.led.block{border-left-color:var(--red)}
.led.fp{border-left-color:var(--amber)}.led.res{border-left-color:var(--green)}
.led .h{font-family:ui-monospace,Consolas,monospace;color:#aab2ba;font-size:.86em;margin-bottom:3px}
.led .h b{color:var(--paper)}
.led .s{color:#8a939d;font-size:.86em;margin-top:3px}
.led.fp .s{color:var(--amber)}
.checks td.P{color:var(--green);font-weight:600}.checks td.F{color:var(--red);font-weight:600}
.checks td.dash{color:var(--grey)}
.shelfgrp{margin-bottom:16px}
.shelfgrp h3{color:#c9b48a;font-size:.95em;margin-bottom:6px;font-weight:600}
.doc{display:flex;gap:12px;padding:4px 8px;font-size:.9em;border-bottom:1px solid #2a323b}
.doc .t{flex:1}.doc .m{color:#7d868f;font-family:ui-monospace,Consolas,monospace;font-size:.85em;white-space:nowrap}
footer{margin-top:44px;color:#6b7680;font-size:.85em;border-top:1px solid var(--line);padding-top:12px}
"""

CSS_DOC = """
*{margin:0;padding:0;box-sizing:border-box}
body{background:#efe9dc;color:#262219;font-family:Georgia,'Times New Roman',serif;
line-height:1.7;padding:0 0 80px}
.bar{background:#1c2126;color:#e8e4d9;font-family:'Segoe UI',sans-serif;font-size:.88em;
padding:10px 22px;display:flex;gap:22px;flex-wrap:wrap;align-items:baseline}
.bar a{color:#d99a3d;text-decoration:none}.bar a:hover{text-decoration:underline}
.bar .p{color:#8a939d;font-family:ui-monospace,Consolas,monospace}
.page{max-width:860px;margin:34px auto;background:#f7f3e8;border:1px solid #d8d0bc;
box-shadow:0 2px 14px rgba(60,50,30,.12);padding:52px 58px;border-radius:2px}
h1,h2,h3,h4{font-family:Fraunces,Georgia,serif;color:#1f1b12;margin:1.3em 0 .5em;line-height:1.25}
h1{font-size:1.9em;margin-top:0}h2{font-size:1.45em;border-bottom:1px solid #d8d0bc;padding-bottom:.2em}
h3{font-size:1.15em}
p{margin:.75em 0}
a{color:#8a5a17}
code{font-family:ui-monospace,Consolas,monospace;font-size:.85em;background:#ece5d3;
padding:1px 5px;border-radius:3px;border:1px solid #ddd5c0}
pre{background:#26221a;color:#e8e4d9;padding:16px 18px;border-radius:4px;overflow-x:auto;
margin:1em 0;font-size:.85em;line-height:1.5}
pre code{background:none;border:none;color:inherit;padding:0}
blockquote{border-left:3px solid #c8a86a;padding:2px 0 2px 16px;margin:1em 0;color:#5a5240;font-style:italic}
ul,ol{margin:.7em 0 .7em 1.6em}li{margin:.3em 0}
hr{border:none;border-top:1px solid #d8d0bc;margin:1.6em 0}
table{border-collapse:collapse;margin:1em 0;font-size:.92em;font-family:'Segoe UI',sans-serif}
th,td{border:1px solid #cfc6ae;padding:6px 11px;text-align:left}
th{background:#e8e0cc}
.fm{background:#ece5d3;border:1px solid #ddd5c0;border-radius:4px;padding:10px 14px;
margin-bottom:22px;font-family:ui-monospace,Consolas,monospace;font-size:.8em;color:#5a5240;
white-space:pre-wrap;overflow-x:auto}
.anchor{scroll-margin-top:20px}
"""

# ---------------------------------------------------------------- small helpers

def esc(s):
    return html_mod.escape(str(s), quote=False)

def read(p):
    return Path(p).read_text(encoding="utf-8-sig", errors="replace")

def slug_for(rel):
    """Flat, predictable output name for a source path."""
    return str(rel).replace("\\", "/").replace("/", "__") + ".html"

def frontmatter(text):
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip()
    return fm, (text[m.end():] if m else text)

def fm_list(v):
    v = (v or "").strip()
    if v.startswith("[") and v.endswith("]"):
        v = v[1:-1]
    return [x.strip() for x in v.split(",") if x.strip()]

def first_heading(body, fallback):
    m = re.search(r"^#\s+(.+)$", body, re.M)
    return m.group(1).strip() if m else fallback

# ---------------------------------------------------------------- manifest parser

def split_flow(s):
    parts, depth, cur = [], 0, ""
    for ch in s:
        if ch in "[{(":
            depth += 1
        elif ch in "]})":
            depth -= 1
        if ch == "," and depth == 0:
            parts.append(cur)
            cur = ""
        else:
            cur += ch
    if cur.strip():
        parts.append(cur)
    return [p.strip() for p in parts]

def parse_flow_map(s):
    out = {}
    for part in split_flow(s):
        if ":" in part:
            k, v = part.split(":", 1)
            out[k.strip()] = v.strip()
    return out

def parse_manifest(path):
    meta, sections = {}, {"extractions": {}, "artifacts": {}}
    section = None
    for raw in read(path).splitlines():
        line = raw.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^([\w-]+):\s*(.*)$", line)  # top-level scalar / section
        if m:
            key, val = m.group(1), m.group(2)
            if val == "" or val.startswith("#"):
                section = key if key in sections else None
                if key not in sections and key != "rules":
                    section = None
                continue
            if key not in sections:
                meta[key] = re.sub(r"\s+#.*$", "", val).strip()
                section = None
            continue
        m = re.match(r"^\s{2}([\w.-]+):\s*\{(.*)\}\s*$", line)
        if m and section in sections:
            sections[section][m.group(1)] = parse_flow_map(m.group(2))
    return meta, sections["extractions"], sections["artifacts"]

# ---------------------------------------------------------------- ledger parser

LEDGER_HEAD = re.compile(r"^\[(L\d+)\]\[([^\]]*)\]\[([^\]]*)\]\[([^\]]*)\]\[([^\]]*)\]")

def parse_ledger(path):
    entries, cur, field = [], None, None
    for line in read(path).splitlines():
        m = LEDGER_HEAD.match(line)
        if m:
            cur = {"id": m.group(1), "scope": m.group(2), "tier": m.group(3),
                   "date": m.group(4), "role": m.group(5),
                   "FINDING": "", "EVIDENCE": "", "PROPOSED": "", "STATUS": ""}
            entries.append(cur)
            field = None
            continue
        if cur is None:
            continue
        fm = re.match(r"^(FINDING|EVIDENCE|PROPOSED|STATUS):\s*(.*)$", line)
        if fm:
            field = fm.group(1)
            cur[field] = fm.group(2)
        elif field and line.strip():
            cur[field] += " " + line.strip()
    return entries

def superseded_ids(entries):
    """Append-only ledgers close by reference: a later resolved entry saying
    'resolves L049' / 'closes L044' / 'L048 approved' retires the earlier one."""
    closed = set()
    verbs = r"resolv\w*|clos\w*|approv\w*|clear\w*|discharg\w*|supersed\w*|retire\w*"
    for e in entries:
        if not e["STATUS"].lower().startswith("resolved"):
            continue
        text = " ".join((e["FINDING"], e["PROPOSED"], e["STATUS"]))
        for m in re.finditer(r"L\d{3}", text):
            lid = m.group(0)
            if lid == e["id"]:
                continue
            window = text[max(0, m.start() - 60):m.end() + 60]
            if re.search(verbs, window, re.I):
                closed.add(lid)
    return closed

def ledger_class(e, closed=frozenset()):
    st = e["STATUS"].lower()
    if st.startswith("resolved") or e["id"] in closed:
        return "res"
    if re.search(r"open\([^)]*first-person", st) or "pending first-person" in st:
        return "fp"
    if "CANON" in e["tier"].upper():
        return "canon"
    if "BLOCK" in e["tier"].upper() or "blocking" in st:
        return "block"
    return ""

# ---------------------------------------------------------------- markdown renderer

INLINE_RULES = [
    (re.compile(r"`([^`]+)`"), lambda m: "<code>" + esc(m.group(1)) + "</code>"),
    (re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)"),
     lambda m: '<a href="%s">%s</a>' % (m.group(2), esc(m.group(1)))),
    (re.compile(r"\*\*([^*]+)\*\*"), lambda m: "<b>" + m.group(1) + "</b>"),
    (re.compile(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])"), lambda m: "<i>" + m.group(1) + "</i>"),
]

def inline(s):
    # protect code spans first by running rules in order on escaped text
    s = esc(s)
    for rx, fn in INLINE_RULES:
        s = rx.sub(fn, s)
    return s

def md_to_html(text):
    lines = text.splitlines()
    out, i, n = [], 0, len(lines)
    list_stack = []  # entries: (indent, tag)

    def close_lists(to_indent=-1):
        while list_stack and list_stack[-1][0] >= to_indent if to_indent >= 0 else list_stack:
            out.append("</%s>" % list_stack.pop()[1])

    def close_all_lists():
        while list_stack:
            out.append("</%s>" % list_stack.pop()[1])

    while i < n:
        line = lines[i]
        stripped = line.strip()
        # fenced code
        if stripped.startswith("```"):
            close_all_lists()
            block = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                block.append(lines[i])
                i += 1
            out.append("<pre><code>" + esc("\n".join(block)) + "</code></pre>")
            i += 1
            continue
        # blank
        if not stripped:
            close_all_lists()
            i += 1
            continue
        # heading
        m = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if m:
            close_all_lists()
            lvl = len(m.group(1))
            hid = re.sub(r"[^\w-]+", "-", m.group(2).lower()).strip("-")
            out.append('<h%d class="anchor" id="%s">%s</h%d>' % (lvl, hid, inline(m.group(2)), lvl))
            i += 1
            continue
        # hr
        if re.match(r"^(-{3,}|\*{3,}|_{3,})$", stripped):
            close_all_lists()
            out.append("<hr>")
            i += 1
            continue
        # table
        if stripped.startswith("|") and i + 1 < n and re.match(r"^\s*\|[\s:|-]+\|?\s*$", lines[i + 1]):
            close_all_lists()
            hdr = [c.strip() for c in stripped.strip("|").split("|")]
            out.append('<div style="overflow-x:auto"><table><tr>' +
                       "".join("<th>%s</th>" % inline(c) for c in hdr) + "</tr>")
            i += 2
            while i < n and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                out.append("<tr>" + "".join("<td>%s</td>" % inline(c) for c in cells) + "</tr>")
                i += 1
            out.append("</table></div>")
            continue
        # blockquote
        if stripped.startswith(">"):
            close_all_lists()
            block = []
            while i < n and lines[i].strip().startswith(">"):
                block.append(lines[i].strip()[1:].strip())
                i += 1
            out.append("<blockquote>%s</blockquote>" % inline(" ".join(block)))
            continue
        # list item
        m = re.match(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$", line)
        if m:
            indent = len(m.group(1))
            tag = "ol" if m.group(2)[0].isdigit() else "ul"
            while list_stack and list_stack[-1][0] > indent:
                out.append("</%s>" % list_stack.pop()[1])
            if not list_stack or list_stack[-1][0] < indent or list_stack[-1][1] != tag:
                if list_stack and list_stack[-1][0] == indent and list_stack[-1][1] != tag:
                    out.append("</%s>" % list_stack.pop()[1])
                out.append("<%s>" % tag)
                list_stack.append((indent, tag))
            out.append("<li>%s</li>" % inline(m.group(3)))
            i += 1
            continue
        # paragraph (gather until structural break)
        close_all_lists()
        para = [stripped]
        i += 1
        while i < n:
            nxt = lines[i].strip()
            if (not nxt or nxt.startswith(("#", "```", ">", "|")) or
                    re.match(r"^(\s*)([-*+]|\d+[.)])\s+", lines[i]) or
                    re.match(r"^(-{3,}|\*{3,})$", nxt)):
                break
            para.append(nxt)
            i += 1
        out.append("<p>%s</p>" % inline(" ".join(para)))
    close_all_lists()
    return "\n".join(out)

# ---------------------------------------------------------------- page shells

def doc_page(title, rel, mtime, inner, fm_text=""):
    fm_block = '<div class="fm">%s</div>' % esc(fm_text) if fm_text else ""
    return """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%s · fleet tracker</title><style>%s</style></head><body>
<div class="bar"><a href="../index.html">&larr; wall-board</a>
<span class="p">%s</span><span class="p">%s</span></div>
<div class="page">%s%s</div></body></html>""" % (
        esc(title), CSS_DOC, esc(rel), esc(mtime), fm_block, inner)

# ---------------------------------------------------------------- build

def build(root, out, stamp, run_checks):
    root, out = Path(root), Path(out)
    docs_out = out / "docs"
    docs_out.mkdir(parents=True, exist_ok=True)

    manifest_path = root / "manifest.yaml"
    ledger_path = root / "reviews" / "critiques_ledger.md"
    meta, extractions, artifacts = parse_manifest(manifest_path)
    ledger = parse_ledger(ledger_path) if ledger_path.exists() else []

    # ---- discover + render every document in the pipeline
    doc_index = {}  # rel(str, /) -> {title, mtime, href, group}
    sources = []
    for p in sorted(root.rglob("*")):
        if p.is_dir() or any(part in SKIP_DIRS for part in p.relative_to(root).parts):
            continue
        if p.suffix.lower() in (".md", ".yaml", ".yml", ".py", ".txt"):
            sources.append(p)
    repo = root
    for cand in [root.parents[i] for i in range(min(4, len(root.parents)))]:
        if (cand / "papers").is_dir() and (cand / "research").is_dir():
            repo = cand
            break
    canon_files = []
    for g in CANON_GLOBS:
        canon_files.extend(sorted(repo.glob(g)))

    def render_file(p, rel_key, group, canon=False):
        text = read(p)
        mtime = datetime.fromtimestamp(p.stat().st_mtime).strftime("%Y-%m-%d %H:%M")
        if p.suffix.lower() == ".md":
            fm_raw = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
            fm_text, body = (fm_raw.group(1), text[fm_raw.end():]) if fm_raw else ("", text)
            title = first_heading(body, p.name)
            inner = md_to_html(body)
        else:
            title = p.name
            fm_text = ""
            inner = "<h1>%s</h1><pre><code>%s</code></pre>" % (esc(p.name), esc(text))
        if canon:
            inner = ('<p style="font-family:sans-serif;font-size:.85em;color:#8a5a17">'
                     'CANON · read-only upstream of the pipeline</p>') + inner
        href = "docs/" + slug_for(rel_key)
        (out / href).write_text(
            doc_page(title, rel_key, mtime, inner, fm_text), encoding="utf-8")
        doc_index[rel_key] = {"title": title, "mtime": mtime, "href": href, "group": group}

    for p in sources:
        rel = str(p.relative_to(root)).replace("\\", "/")
        group = rel.split("/")[0] if "/" in rel else "· pipeline root"
        render_file(p, rel, group)
    for p in canon_files:
        rel = "canon/" + str(p.relative_to(repo)).replace("\\", "/")
        render_file(p, rel, "canon (read-only)", canon=True)

    def href_of(rel):
        rel = rel.replace("\\", "/")
        return doc_index.get(rel, {}).get("href", "")

    # ---- chronicles → sessions
    sessions = []
    for rel, info in doc_index.items():
        if not rel.startswith("chronicles/") or rel.endswith("README.md"):
            continue
        fm, body = frontmatter(read(root / rel))
        vm = re.search(r"##\s*Verdict\s*\n+(.+?)(?:\n\n|\n##|$)", body, re.S)
        sessions.append({
            "rel": rel, "href": info["href"],
            "date": fm.get("date", rel.split("/")[1][:10]),
            "role": fm.get("role", "?"),
            "wps": fm_list(fm.get("wps", "")),
            "ledger": fm.get("ledger_entries", ""),
            "slug": Path(rel).stem[11:] if len(Path(rel).stem) > 11 else Path(rel).stem,
            "verdict": (vm.group(1).strip().split(". ")[0][:220] if vm else ""),
        })
    sessions.sort(key=lambda s: (s["date"], s["rel"]))
    dates = sorted({s["date"] for s in sessions}, reverse=True)

    # ---- extraction claim counts
    for eid, e in extractions.items():
        f = root / e.get("path", "_")
        e["_claims"] = len(re.findall(r"^###\s+E\d+-C\d+", read(f), re.M)) if f.exists() else None

    # ---- needs-first-person queue
    closed = superseded_ids(ledger)
    needs = []
    for e in ledger:
        if ledger_class(e, closed) == "fp":
            needs.append({
                "label": "%s · %s" % (e["id"], e["FINDING"][:190] + ("…" if len(e["FINDING"]) > 190 else "")),
                "status": e["STATUS"],
                "href": href_of("reviews/critiques_ledger.md") + "#" + e["id"].lower(),
                "where": "critiques_ledger.md " + e["id"],
            })
    for wid, a in sorted(artifacts.items()):
        note = a.get("note", "")
        if a.get("gate") == "P3" or re.search(r"P4\b", note):
            needs.append({
                "label": "%s · %s — %s" % (wid, a.get("name", ""), note[:170]),
                "status": "gate %s · waiting on the P4 read" % a.get("gate"),
                "href": href_of(a.get("path", "")) or "#board",
                "where": a.get("path", ""),
            })

    # ---- checks matrix
    check_results, check_names = {}, []
    if run_checks:
        checks_dir = root / "checks"
        check_files = sorted(checks_dir.glob("check_*.py"))
        check_names = [c.stem.replace("check_", "") for c in check_files]
        targets = []
        for eid, e in extractions.items():
            f = root / e.get("path", "_")
            if f.exists():
                targets.append((eid, f))
        for wid, a in artifacts.items():
            f = root / a.get("path", "_")
            if f.suffix == ".md" and f.exists() and "ledger" not in f.name:
                targets.append((wid, f))
        for label, f in targets:
            row = {}
            for c in check_files:
                try:
                    r = subprocess.run([sys.executable, str(c), str(f)],
                                       capture_output=True, text=True, timeout=60,
                                       cwd=str(checks_dir))
                    row[c.stem.replace("check_", "")] = ("PASS" if r.returncode == 0 else "FAIL")
                except Exception:
                    row[c.stem.replace("check_", "")] = "ERR"
            check_results[label] = row

    # ---------------------------------------------------------------- index html
    ledger_head = ledger[-1]["id"] if ledger else "—"
    latest = dates[0] if dates else "—"
    today_sessions = sum(1 for s in sessions if s["date"] == latest)
    open_count = sum(1 for e in ledger
                     if not e["STATUS"].lower().startswith("resolved") and e["id"] not in closed)

    H = []
    H.append("""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Fleet Tracker · %s</title><style>%s</style></head><body><div class="wrap">""" % (
        esc(meta.get("pipeline", "pipeline")), CSS_BOARD))
    H.append("""<header class="mast"><h1>Fleet Tracker · %s</h1>
<div class="maststats mono">
<span>register head <b>%s</b></span><span>ledger head <b>%s</b> (<b>%d</b> open)</span>
<span>manifest v<b>%s</b></span><span>last fleet day <b>%s</b> · <b>%d</b> sessions</span>
<span>rebuilt <b>%s</b></span></div></header>""" % (
        esc(meta.get("pipeline", "")), esc(meta.get("register_head", "?")), ledger_head,
        open_count, esc(meta.get("version", "?")), latest, today_sessions, esc(stamp)))

    # needs block
    H.append('<section class="needs"><h2>Needs the First Person</h2>')
    if needs:
        H.append("<ul>")
        for q in needs:
            H.append('<li><a class="ln" href="%s">%s</a><br>%s '
                     '<span class="where">· %s</span></li>' % (
                         q["href"], esc(q["label"]), esc(q["status"]), esc(q["where"])))
        H.append("</ul>")
    else:
        H.append("<p>Nothing in the queue.</p>")
    H.append("</section>")

    # artifact board
    def gate_track(g):
        cells = []
        passed = GATES.index(g) if g in GATES else -1
        for i, name in enumerate(GATES):
            cls = ("on " if i <= passed else "") + ("p4" if name == "P4" else "")
            cells.append('<i class="%s" title="%s"></i>' % (cls.strip(), name))
        label = g if g in GATES else "—"
        return '<span class="gate">%s %s</span>' % ("".join(cells), label)

    def sort_key(item):
        wid, a = item
        hard = 0 if a.get("hard_deadline") == "true" else 1
        gate = -(GATES.index(a["gate"]) if a.get("gate") in GATES else -1)
        return (hard, gate, wid)

    H.append('<section id="board"><h2>Artifact board · %d work packages</h2><div class="scroll"><table>' % len(artifacts))
    H.append("<tr><th>wp</th><th>name</th><th>tier</th><th>status</th><th>gate</th>"
             "<th>due</th><th>next / chain</th><th>note</th></tr>")
    for wid, a in sorted(artifacts.items(), key=sort_key):
        due = a.get("due", "")
        duec = ' class="due-hard mono"' if a.get("hard_deadline") == "true" else ' class="mono"'
        path_href = href_of(a.get("path", ""))
        name_cell = ('<a href="%s">%s</a>' % (path_href, esc(a.get("name", "")))
                     if path_href else esc(a.get("name", "")))
        tier = a.get("tier", "")
        note = a.get("note", a.get("blocker", ""))
        H.append('<tr><td class="mono">%s</td><td>%s</td><td><span class="chip tier-%s">%s</span></td>'
                 '<td class="st-%s">%s</td><td>%s</td><td%s>%s</td><td class="mono">%s</td>'
                 '<td class="note">%s</td></tr>' % (
                     wid, name_cell, tier, tier, esc(a.get("status", "")), esc(a.get("status", "")),
                     gate_track(a.get("gate", "")), duec, esc(due),
                     esc(a.get("chain", "")).strip("[]"), esc(note)))
    H.append("</table></div></section>")

    # extraction shelf
    H.append('<section><h2>Extraction shelf · %d</h2><div class="scroll"><table>' % len(extractions))
    H.append("<tr><th>id</th><th>name</th><th>status</th><th>claims</th><th>built</th><th>note</th></tr>")
    for eid, e in sorted(extractions.items(), key=lambda kv: int(kv[0][1:])):
        f_href = href_of(e.get("path", ""))
        name_cell = ('<a href="%s">%s</a>' % (f_href, esc(e.get("name", "")))
                     if f_href else esc(e.get("name", "")))
        claims = e.get("_claims")
        H.append('<tr><td class="mono">%s</td><td>%s</td><td class="st-%s">%s</td>'
                 '<td class="mono">%s</td><td class="mono">%s</td><td class="note">%s</td></tr>' % (
                     eid, name_cell, esc(e.get("status", "")), esc(e.get("status", "")),
                     claims if claims is not None else "—",
                     esc(e.get("built", e.get("widened", ""))), esc(e.get("note", ""))))
    H.append("</table></div></section>")

    # cycle timeline
    H.append('<section><h2>Session timeline · %d chronicles</h2>' % len(sessions))
    for d in dates:
        H.append('<div class="lane"><div class="d">%s</div>' % esc(d))
        for s in [x for x in sessions if x["date"] == d]:
            wps = " ".join(s["wps"][:4]) + ("…" if len(s["wps"]) > 4 else "")
            H.append('<a class="sess" href="%s" title="%s"><span class="r">%s</span> · %s · %s</a>' % (
                s["href"], esc(s["verdict"]), esc(s["role"].split(" ")[0].rstrip(";,")),
                esc(wps or "—"), esc(s["slug"])))
        H.append("</div>")
    H.append("</section>")

    # ledger tail
    H.append('<section><h2>Ledger tail · last %d of %d entries</h2>' % (
        min(LEDGER_TAIL, len(ledger)), len(ledger)))
    ledger_href = href_of("reviews/critiques_ledger.md")
    for e in ledger[-LEDGER_TAIL:][::-1]:
        H.append('<div class="led %s"><div class="h"><b>%s</b> [%s][%s][%s][%s]</div>'
                 '%s<div class="s">STATUS: %s</div></div>' % (
                     ledger_class(e, closed), e["id"], esc(e["scope"]), esc(e["tier"]), esc(e["date"]),
                     esc(e["role"]), esc(e["FINDING"][:260] + ("…" if len(e["FINDING"]) > 260 else "")),
                     esc(e["STATUS"])))
    H.append('<p style="margin-top:8px"><a href="%s">full ledger →</a></p></section>' % ledger_href)

    # checks matrix
    H.append('<section><h2>Checks</h2>')
    if check_results:
        H.append('<div class="scroll"><table class="checks"><tr><th>artifact</th>%s</tr>' %
                 "".join("<th>%s</th>" % esc(c) for c in check_names))
        for label, row in check_results.items():
            H.append("<tr><td class=\"mono\">%s</td>%s</tr>" % (
                esc(label),
                "".join('<td class="%s">%s</td>' % (v[0], v) for v in
                        (row.get(c, "—") for c in check_names))))
        H.append("</table></div>")
    else:
        H.append('<p style="color:#8a939d">Checks not run this build — rebuild without --no-checks.</p>')
    H.append("</section>")

    # document shelf
    H.append('<section><h2>All documents · %d</h2>' % len(doc_index))
    groups = {}
    for rel, info in doc_index.items():
        groups.setdefault(info["group"], []).append((rel, info))
    for g in sorted(groups):
        H.append('<div class="shelfgrp"><h3>%s</h3>' % esc(g))
        for rel, info in sorted(groups[g], key=lambda kv: kv[1]["mtime"], reverse=True):
            H.append('<div class="doc"><span class="t"><a href="%s">%s</a></span>'
                     '<span class="m">%s</span><span class="m">%s</span></div>' % (
                         info["href"], esc(info["title"]), esc(rel), info["mtime"]))
        H.append("</div>")
    H.append("</section>")

    H.append('<footer>Generated by tools/fleet_tracker.py — GR-6: never hand-edit; '
             'fix the sources or the generator and rebuild. The manifest is the map, '
             'the ledger is the memory; this page renders them.</footer>')
    H.append("</div></body></html>")

    (out / "index.html").write_text("\n".join(H), encoding="utf-8")

    # ledger anchors: re-render the ledger doc page with per-entry ids
    if ledger_path.exists():
        inner = []
        for e in ledger:
            inner.append('<div class="anchor" id="%s" style="border-bottom:1px solid #d8d0bc;'
                         'padding:10px 0"><p><b>%s</b> <code>[%s][%s][%s][%s]</code></p>'
                         '<p><b>FINDING:</b> %s</p><p><b>EVIDENCE:</b> %s</p>'
                         '<p><b>PROPOSED:</b> %s</p><p><b>STATUS:</b> %s</p></div>' % (
                             e["id"].lower(), e["id"], esc(e["scope"]), esc(e["tier"]),
                             esc(e["date"]), esc(e["role"]), esc(e["FINDING"]),
                             esc(e["EVIDENCE"]), esc(e["PROPOSED"]), esc(e["STATUS"])))
        mtime = datetime.fromtimestamp(ledger_path.stat().st_mtime).strftime("%Y-%m-%d %H:%M")
        (out / href_of("reviews/critiques_ledger.md")).write_text(
            doc_page("Critiques Ledger", "reviews/critiques_ledger.md", mtime,
                     "<h1>Critiques Ledger · %d entries</h1>" % len(ledger) + "\n".join(inner)),
            encoding="utf-8")

    return out / "index.html", len(doc_index), len(needs)

# ---------------------------------------------------------------- serve

def serve(out, port):
    import functools
    import http.server
    import socketserver
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(out))
    with socketserver.ThreadingTCPServer(("", port), handler) as httpd:
        print("Fleet tracker at http://localhost:%d" % port)
        httpd.serve_forever()

# ---------------------------------------------------------------- main

def main():
    if sys.platform == "win32":
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="Generate (and serve) the fleet tracker.")
    ap.add_argument("--root", default=None, help="pipeline root (default: dir above tools/)")
    ap.add_argument("--out", default=None, help="output dir (default: <root>/tracker)")
    ap.add_argument("--stamp", default=None, help="rebuild stamp (default: now)")
    ap.add_argument("--no-checks", action="store_true", help="skip running checks/")
    ap.add_argument("--serve", action="store_true", help="serve after generating")
    ap.add_argument("--port", type=int, default=7272)
    args = ap.parse_args()

    root = Path(args.root) if args.root else Path(__file__).resolve().parents[1]
    out = Path(args.out) if args.out else root / "tracker"
    stamp = args.stamp or datetime.now().strftime("%Y-%m-%d %H:%M")

    index, ndocs, nneeds = build(root, out, stamp, run_checks=not args.no_checks)
    print("built %s · %d documents rendered · %d items in the first-person queue" % (
        index, ndocs, nneeds))
    if args.serve:
        serve(out, args.port)

if __name__ == "__main__":
    main()
