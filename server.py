#!/usr/bin/env python3
"""
Simple documentation server for 0xagentprivacy docs
Serves markdown files as HTML at http://localhost:7000
"""

import http.server
import socketserver
import urllib.parse
import os
import markdown
from pathlib import Path

PORT = 7000

# Document files in order: (filename, title, description, file_type)
# file_type: 'md' for markdown, 'pdf' for PDF
# Paths are relative to the repo root (post 2026-06-10 restructure:
# papers/{v4,v5,v6,whitepapers}, pdfs/{v6,compendium}, reference/, research/)
DOCUMENTS = [
    # Entry points
    ("README.md", "README - Overview", "Introduction to the privacy-first AI agent architecture and the V6 documentation suite", "md"),
    ("what-agentprivacy-is.md", "What Agentprivacy Is", "Mission, thesis, and orientation for new joiners", "md"),
    ("QUICK_START.md", "Quick Start", "Where to begin reading, by audience", "md"),
    ("DOCUMENTATION_CHRONICLE.md", "Documentation Chronicle", "Navigable history of the documentation suite, Arc 1 through Arc 9 (V6)", "md"),
    # Privacy is Value V6 - The Gathering Turn and the Moving Ceiling
    ("papers/v6/privacy_value_v6_formal_specification.md", "Privacy is Value V6 - Formal Specification", "The standalone academic volume: moving ceiling R(t), shelf life t*, register head C89, consolidated references", "md"),
    ("pdfs/v6/privacy_value_v6_formal_specification.pdf", "V6 Formal Specification (PDF)", "Web render with MathJax-typeset equations", "pdf"),
    ("pdfs/v6/privacy_value_v6_formal_specification_academic.pdf", "V6 Formal Specification (academic PDF)", "xelatex render for academic submission", "pdf"),
    ("papers/v6/privacy_value_v6.md", "Privacy is Value V6 - Crosswalk Paper", "The narrative paper carrying the V5.4 to V6 path", "md"),
    ("pdfs/v6/privacy_value_v6.pdf", "Privacy is Value V6 (PDF)", "Same content as above, printable PDF", "pdf"),
    ("papers/v6/pvm_v6_compressed.md", "PVM V6 Compressed - Swordsman Reading", "Equations only: the five-page reading", "md"),
    ("pdfs/v6/pvm_v6_compressed.pdf", "PVM V6 Compressed (PDF)", "Same content as above, printable PDF", "pdf"),
    ("papers/v6/pvm_v6_companion_guide.md", "PVM V6 Companion Guide - Mage Reading", "Context, narrative, and standards alignment", "md"),
    ("pdfs/v6/pvm_v6_companion_guide.pdf", "PVM V6 Companion Guide (PDF)", "Same content as above, printable PDF", "pdf"),
    ("papers/v6/dualprivacy_researchpaper_v6.md", "Dual Privacy Research Paper V6", "The V6 edition over the v4.3 proof body: formal models, proofs, standards foundation", "md"),
    ("pdfs/v6/dualprivacy_researchpaper_v6.pdf", "Dual Privacy Research Paper V6 (PDF)", "Same content as above, printable PDF", "pdf"),
    ("papers/whitepapers/swordsman_mage_whitepaper_v6_3.md", "Whitepaper v6.3 - Technical Architecture", "Dual agent system design, IEEE 7012 integration: Swordsman (protect) and Mage (delegate)", "md"),
    ("pdfs/v6/swordsman_mage_whitepaper_v6_3.pdf", "Whitepaper v6.3 (PDF)", "Same content as above, printable PDF", "pdf"),
    # The book
    ("pdfs/compendium/privacy_is_value_compendium.pdf", "Privacy is Value - The Compendium (PDF)", "The whole research as one book: Parts I-IV, era retrospectives, honest-limits ledger, concordances", "pdf"),
    ("pdfs/compendium/privacy_is_value_compendium_academic.pdf", "The Compendium (academic PDF)", "xelatex render of the compendium tome", "pdf"),
    # Authorities and reference
    ("research/CONJECTURE_REGISTER_V6.md", "Conjecture Register V6", "The single numbering authority: head C89, bands, aliases, the no-renumber promise", "md"),
    ("reference/PAPERS_INDEX.md", "Papers Index", "Every paper made known for its purpose: the catalogue authority", "md"),
    ("reference/GLOSSARY_MASTER_v4_0.md", "Glossary Master v4.0 + V6 Addendum", "Canonical terminology including the Section 25 V6 vocabulary", "md"),
    ("reference/IEEE_7012_QUICK_REFERENCE.md", "IEEE 7012 Quick Reference", "Machine-readable personal privacy terms: agreement taxonomy and technical specs", "md"),
    ("reference/promise_theory_reference_v1_4.md", "Promise Theory Reference v1.4", "Formal semantic foundations for autonomous agent coordination", "md"),
    ("reference/VISUAL_ARCHITECTURE_GUIDE_v2_0.md", "Visual Guide v2.0 - Diagrams & Flows", "Visual diagrams, IEEE 7012 flows, and architectural illustrations of the agent framework", "md"),
]

# ---------------------------------------------------------------------------
# BLOG WORKSHOP — the distribution series.
# The public-tier essays ("blogs") live in the Programme pipeline; the two
# Foundations announcements live in blog/. Each post carries its publish target
# and its tier siblings (the same core told for other audiences), so the series
# can be read in order AND synced to the right public surface.
# ---------------------------------------------------------------------------
PROG = "papers/Programme/pipeline/rehydrations"

BLOG_SERIES = [
    {
        "id": "moving-ceiling",
        "arc": "Arc I · The Moving Ceiling (V6)",
        "blurb": "The first V6 result — every static privacy guarantee has a shelf life. Read top to bottom.",
        "posts": [
            {"n": "1", "title": "The Moving Ceiling",
             "subtitle": "every static privacy guarantee has a shelf life · the first V6 result",
             "path": f"{PROG}/public/the_moving_ceiling.md",
             "status": "post-ready", "target": "sync.soulbis.com",
             "siblings": [("academic", "SoK: The Shelf Life of Privacy Guarantees", f"{PROG}/academic/moving_ceiling_sok.md"),
                          ("policy", "Enforceable by Architecture", f"{PROG}/policy/enforceable_by_architecture.md")]},
            {"n": "2", "title": "The Uncarved Date",
             "subtitle": "a tale from the City of Mages · companion to The Moving Ceiling",
             "path": f"{PROG}/public/the_uncarved_date.md",
             "status": "post-ready", "target": "sync.soulbis.com", "siblings": []},
            {"n": "3", "title": "Competence Without History",
             "subtitle": "the gathering turn has doors: the atlas, the skills, the game, the wiki",
             "path": f"{PROG}/public/competence_without_history.md",
             "status": "post-ready", "target": "sync.soulbis.com",
             "siblings": [("academic", "Sequential Composition: Exponential-to-Linear Separation", f"{PROG}/academic/linear_cap_paper.md")]},
        ],
    },
    {
        "id": "foundations",
        "arc": "Arc II · The Foundations",
        "blurb": "Two announcements — the community and the runtime that made V6 possible.",
        "posts": [
            {"n": "4", "title": "Founding the City of Mages",
             "subtitle": "from WHAT to WHO · the second person opens · an announcement",
             "path": "blog/founding-the-city-of-mages.md",
             "status": "drafting", "target": "sync.soulbis.com", "siblings": []},
            {"n": "5", "title": "The Dual Agent Harness",
             "subtitle": "one proposes, one breaks, the signature does not delegate · an announcement",
             "path": "blog/the-dual-agent-harness.md",
             "status": "drafting", "target": "sync.soulbis.com",
             "siblings": [("academic", "Conjecture Governance: an Operating Method", f"{PROG}/academic/conjecture_governance_method.md"),
                          ("standards", "Separation of Duties for Personal AI Agents", f"{PROG}/standards/bgin_separation_of_duties.md")]},
        ],
    },
    {
        "id": "runtime-letters",
        "arc": "Related · Runtime Letters (off-arc)",
        "blurb": "Letters that narrate the harness's first runs. Optional, complementary reading.",
        "posts": [
            {"n": "—", "title": "Two Agents Walk Into a Circuit",
             "subtitle": "one proposes, one breaks, neither writes the exam",
             "path": f"{PROG}/public/two_agents_walk_into_a_circuit.md",
             "status": "post-ready", "target": "sync.soulbis.com", "siblings": []},
            {"n": "—", "title": "The Fleet and the Cap",
             "subtitle": "ten sessions, one rule, and the read that cannot be delegated",
             "path": f"{PROG}/public/letter_the_fleet_and_the_cap.md",
             "status": "post-ready", "target": "sync.soulbis.com", "siblings": []},
        ],
    },
]

# The earlier V5 narrative series, kept available (already published).
V5_BLOG = [
    ("blog/blog-part0-the-myth-before-the-math.md", "V5 · Part 0 — The Myth Before the Math"),
    ("blog/blog-part1-forming-constellations.md", "V5 · Part 1 — Forming Constellations"),
    ("blog/blog-part2-the-forge-and-the-ceremony.md", "V5 · Part 2 — The Forge and the Ceremony"),
    ("blog/blog-part3-the-dragon-wakes.md", "V5 · Part 3 — The Dragon Wakes"),
    ("blog/blog-part4-the-dihedral-mirror.md", "V5 · Part 4 — The Dihedral Mirror"),
    ("blog/blog-part5-the-amnesia-protocol.md", "V5 · Part 5 — The First Agent We Forgo(t)"),
]

def series_flat():
    """Ordered list of every post across all arcs (for prev/next navigation)."""
    return [p for arc in BLOG_SERIES for p in arc["posts"]]

def series_nav(path):
    """Return (prev_post, this_post, next_post) for a given file path, or Nones."""
    norm = path.replace('\\', '/')
    flat = series_flat()
    for i, p in enumerate(flat):
        if p["path"].replace('\\', '/') == norm:
            return (flat[i-1] if i > 0 else None, p, flat[i+1] if i < len(flat)-1 else None)
    return (None, None, None)

def blog_paths():
    """All paths surfaced by the workshop + V5 series, for de-duping the browse tree."""
    s = {p["path"].replace('\\', '/') for p in series_flat()}
    for p in series_flat():
        for _, _, sp in p["siblings"]:
            s.add(sp.replace('\\', '/'))
    s |= {f.replace('\\', '/') for f, _ in V5_BLOG}
    return s

# Top-level directories to skip entirely in the "browse everything" tree.
BROWSE_SKIP_DIRS = {'.git', '.github', '__pycache__', 'build', 'node_modules'}

def discover_all_docs():
    """Walk the repo and return {top_level_dir: [(relpath, is_pdf), ...]} for
    every .md and .pdf that is not already surfaced in the curated lists above,
    so nothing in the documentation is hidden from the reader."""
    curated = {doc[0].replace('\\', '/') for doc in DOCUMENTS}
    curated |= blog_paths()
    tree = {}
    for root, dirs, files in os.walk('.'):
        # prune skipped directories in-place
        dirs[:] = [d for d in dirs if d not in BROWSE_SKIP_DIRS and not d.startswith('.git')]
        for fn in files:
            if not (fn.lower().endswith('.md') or fn.lower().endswith('.pdf')):
                continue
            rel = os.path.normpath(os.path.join(root, fn)).replace('\\', '/')
            if rel.startswith('./'):
                rel = rel[2:]
            if rel in curated:
                continue
            top = rel.split('/')[0] if '/' in rel else '(root)'
            tree.setdefault(top, []).append((rel, fn.lower().endswith('.pdf')))
    for top in tree:
        tree[top].sort(key=lambda x: x[0].lower())
    return dict(sorted(tree.items(), key=lambda kv: kv[0].lower()))

# ---------------------------------------------------------------------------
# PROGRAMME CONSOLE — a local review surface for the whole V6 rehydration
# pipeline. Parses pipeline/manifest.yaml (the A0-only source of truth) live on
# every request and renders the gate ladder + extraction lineage + the
# work-package board, each row linking to the artifact the reader already
# serves. Single-source: nothing cached, nothing duplicated, the manifest is
# the only authority for status/tier/gate/due/chain.
# ---------------------------------------------------------------------------
import re as _re

PIPE = "papers/Programme/pipeline"

_M_SIMPLE = ['name', 'tier', 'thrust', 'extraction', 'status', 'gate', 'due',
             'path', 'venue', 'risk', 'owner', 'built', 'widened',
             'prereg_required', 'hard_deadline']
_M_LIST = ['chain', 'extraction', 'sources', 'depends', 'targets']

TIER_INFO = {
    'P': ('Public', '#5a9fd4'), 'A': ('Academic', '#b48ead'),
    'G': ('Grants', '#e0a35a'), 'S': ('Standards', '#88c0a0'),
    'D': ('Developer', '#d08770'), 'internal': ('Internal', '#7a7a7a'),
}
TIER_ORDER = ['P', 'A', 'S', 'G', 'D', 'internal']

# status -> (css class, sort rank within a tier)
STATUS_STATE = [
    ('done', ('done', 0)), ('awaiting-p4', ('ready', 1)),
    ('release-draft', ('ready', 1)), ('post-ready', ('ready', 1)),
    ('ongoing', ('live', 2)), ('draft', ('draft', 3)),
    ('widened', ('draft', 3)), ('parked', ('cold', 5)),
    ('anticipated', ('cold', 5)), ('pending', ('pending', 4)),
]

def _status_state(status):
    s = (status or '').lower()
    for key, val in STATUS_STATE:
        if s.startswith(key):
            return val
    return ('pending', 4)

def _parse_flow_entry(body):
    """Parse the inner '{...}' of one manifest entry into a dict, tolerant of
    unquoted note text with colons/commas. List keys pulled first (bracketed),
    then note (to end), then the simple scalar keys."""
    rec = {}
    work = body
    for k in _M_LIST:
        m = _re.search(r'\b' + k + r'\s*:\s*\[([^\]]*)\]', work)
        if m:
            rec[k] = [x.strip() for x in m.group(1).split(',') if x.strip()]
            work = work[:m.start()] + work[m.end():]
    note = None
    mnote = _re.search(r'\bnote\s*:\s*(.*)$', work, _re.S)
    if mnote:
        note = mnote.group(1).strip().rstrip(',').strip()
        work = work[:mnote.start()]
    for k in _M_SIMPLE:
        m = _re.search(r'\b' + k + r'\s*:\s*([^,}]*)', work)
        if m:
            v = m.group(1).strip().rstrip(',').strip()
            if v:
                rec[k] = v
    if note:
        rec['note'] = note
    return rec

def parse_manifest():
    """Return (meta, extractions, artifacts) parsed from pipeline/manifest.yaml."""
    meta, extractions, artifacts = {}, [], []
    path = os.path.join(PIPE, 'manifest.yaml')
    if not os.path.exists(path):
        return meta, extractions, artifacts
    section = None
    with open(path, encoding='utf-8') as f:
        for raw in f:
            raw = raw.rstrip('\n')
            stripped = raw.strip()
            if not stripped or stripped.startswith('#'):
                continue
            if _re.match(r'^(pipeline|version|register_head|gates)\s*:', raw):
                k, _, v = stripped.partition(':')
                meta[k.strip()] = v.split('  #')[0].strip()
                continue
            if raw.startswith('extractions:'):
                section = 'E'; continue
            if raw.startswith('artifacts:'):
                section = 'A'; continue
            m = _re.match(r'^\s+([A-Za-z0-9\-]+):\s*\{(.*)\}\s*$', raw)
            if m and section:
                rec = _parse_flow_entry(m.group(2))
                rec['id'] = m.group(1)
                (extractions if section == 'E' else artifacts).append(rec)
    return meta, extractions, artifacts

def _esc(s):
    return (str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))

def _read_link(relpath, label='read'):
    """Link into the markdown reader if relpath (relative to PIPE) is a served
    .md file; otherwise return a muted note about its kind."""
    if not relpath:
        return '<span class="pc-noread">—</span>'
    rp = relpath.strip()
    full = f"{PIPE}/{rp}"
    if rp.endswith('/'):
        return '<span class="pc-noread">dir</span>'
    if rp.endswith('.md') and os.path.exists(full):
        return f'<a class="pc-read" href="/{urllib.parse.quote(full)}">{label} &rarr;</a>'
    if os.path.exists(full):
        return f'<span class="pc-noread">{_esc(rp.rsplit(".",1)[-1])}</span>'
    return '<span class="pc-noread">not built</span>'

def programme_console_html():
    import datetime
    meta, extractions, artifacts = parse_manifest()
    today = datetime.date.today().isoformat()

    # ---- gate ladder ----
    gates_raw = meta.get('gates', '').strip('[]')
    gates = [g.strip() for g in gates_raw.split(',') if g.strip()]

    # ---- metrics ----
    def _st(recs, key='status'):
        from collections import Counter
        return Counter(_status_state(r.get(key, ''))[0] for r in recs)
    wp_states = _st(artifacts)
    ex_drafted = sum(1 for e in extractions
                     if _status_state(e.get('status', ''))[0] in ('done', 'ready', 'draft', 'live'))

    # ---- work-package board grouped by tier ----
    by_tier = {}
    for a in artifacts:
        by_tier.setdefault(a.get('tier', 'internal'), []).append(a)

    def _claim_count(note):
        m = _re.search(r'(\d+)\s+claims', note or '')
        return m.group(1) if m else None

    # ===================== render =====================
    P = []
    P.append(f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Programme Console · {_esc(meta.get('pipeline','v6-rehydration'))}</title>
<style>
:root {{ color-scheme: dark; }}
* {{ box-sizing: border-box; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background: #1a1a1a; color: #e0e0e0; margin: 0; line-height: 1.5; }}
a {{ color: #a8d8ff; text-decoration: none; }}
a:hover {{ color: #fff; text-decoration: underline; }}
.wrap {{ max-width: 1180px; margin: 0 auto; padding: 28px 22px 80px; }}
.top {{ display:flex; justify-content:space-between; align-items:baseline; flex-wrap:wrap; gap:10px; }}
.top a.home {{ font-size:.85em; color:#b0b0b0; }}
h1 {{ font-size: 1.7em; margin: 6px 0 2px; color:#fff; }}
.sub {{ color:#9aa0a8; font-size:.95em; margin-bottom:18px; }}
.mast {{ display:flex; gap:22px; flex-wrap:wrap; font-size:.82em; color:#b0b0b0;
  background:#20242e; border:1px solid #333a48; border-radius:8px; padding:10px 16px; margin-bottom:20px; }}
.mast b {{ color:#e6ebf5; }}
.metrics {{ display:flex; gap:10px; flex-wrap:wrap; margin: 0 0 26px; }}
.metric {{ background:#252b36; border:1px solid #343c4c; border-radius:8px; padding:10px 14px; min-width:96px; }}
.metric .n {{ font-size:1.5em; font-weight:700; color:#fff; }}
.metric .l {{ font-size:.72em; color:#9aa0a8; text-transform:uppercase; letter-spacing:.04em; }}
h2 {{ font-size:1.15em; color:#fff; margin: 32px 0 4px; border-bottom:1px solid #333; padding-bottom:6px; }}
.h2sub {{ color:#8b929c; font-size:.85em; margin-bottom:14px; }}
.ladder {{ display:flex; gap:8px; flex-wrap:wrap; margin:10px 0 4px; }}
.rung {{ background:#222834; border:1px solid #39415280; border-radius:20px; padding:6px 14px; font-size:.82em; }}
.rung b {{ color:#8fd6b0; }}
.rung.p4 {{ border-color:#5a9fd4; }} .rung.p4 b {{ color:#a8d8ff; }}
.grid {{ display:grid; grid-template-columns: repeat(auto-fill, minmax(340px,1fr)); gap:12px; margin-top:12px; }}
.card {{ background:#232833; border:1px solid #343c4c; border-radius:9px; padding:13px 15px; }}
.card.done {{ border-left:3px solid #2ecc71; }}
.card.ready {{ border-left:3px solid #5a9fd4; }}
.card.live {{ border-left:3px solid #4bbfa0; }}
.card.draft {{ border-left:3px solid #e0a35a; }}
.card.pending {{ border-left:3px solid #555d6b; }}
.card.cold {{ border-left:3px solid #3a3f4a; opacity:.82; }}
.card h3 {{ font-size:.98em; margin:0 0 7px; color:#fff; }}
.card h3 .wid {{ color:#8b93c0; font-variant-numeric:tabular-nums; }}
.pills {{ display:flex; gap:6px; flex-wrap:wrap; margin-bottom:8px; }}
.pill {{ font-size:.68em; padding:2px 8px; border-radius:11px; letter-spacing:.02em; white-space:nowrap; }}
.pill.status {{ background:#2f3644; color:#cdd4de; }}
.pill.status.done {{ background:#1e6b3f; color:#d6ffe6; }}
.pill.status.ready {{ background:#2a577a; color:#dcefff; }}
.pill.status.live {{ background:#245a4c; color:#d6fff2; }}
.pill.status.draft {{ background:#6b4a1e; color:#ffeccd; }}
.pill.status.cold {{ background:#2b2f38; color:#8b929c; }}
.pill.gate {{ background:#3a3550; color:#d9ccff; }}
.pill.thrust {{ background:#2b3038; color:#9aa0a8; }}
.card .meta {{ font-size:.78em; color:#9aa0a8; margin:3px 0; }}
.card .meta code {{ color:#c9d3e0; background:#1c2029; padding:1px 5px; border-radius:4px; font-size:.94em; }}
.card .foot {{ display:flex; justify-content:space-between; align-items:center; margin-top:9px; }}
.pc-read {{ font-size:.82em; font-weight:600; }}
.pc-noread {{ font-size:.75em; color:#6a7280; }}
details.note {{ margin-top:8px; }}
details.note summary {{ cursor:pointer; font-size:.75em; color:#8b929c; }}
details.note[open] summary {{ color:#b0b0b0; }}
details.note .body {{ font-size:.78em; color:#aeb4bd; margin-top:6px; padding-left:10px;
  border-left:2px solid #343c4c; white-space:pre-wrap; }}
.tierhd {{ display:flex; align-items:center; gap:10px; margin:26px 0 2px; }}
.tierdot {{ width:11px; height:11px; border-radius:50%; }}
.tierhd h3 {{ margin:0; font-size:1.02em; color:#fff; }}
.tierhd .c {{ color:#7a828e; font-size:.82em; }}
.exgrid {{ display:grid; grid-template-columns: repeat(auto-fill, minmax(250px,1fr)); gap:10px; }}
.ex {{ background:#212630; border:1px solid #333b49; border-radius:8px; padding:11px 13px; }}
.ex h4 {{ margin:0 0 5px; font-size:.9em; color:#e6ebf5; }}
.ex .m {{ font-size:.76em; color:#9aa0a8; }}
.shelves {{ display:grid; grid-template-columns: repeat(auto-fill, minmax(240px,1fr)); gap:12px; margin-top:12px; }}
.shelf {{ background:#20242e; border:1px solid #333a48; border-radius:8px; padding:12px 14px; }}
.shelf h4 {{ margin:0 0 8px; font-size:.9em; color:#fff; }}
.shelf ul {{ margin:0; padding-left:0; list-style:none; }}
.shelf li {{ font-size:.82em; margin:3px 0; }}
.shelf .more {{ color:#7a828e; font-size:.78em; }}
</style></head><body><div class="wrap">""")

    P.append(f"""<div class="top"><div>
<h1>Privacy is Value · Programme Console</h1>
<div class="sub">the V6 rehydration pipeline — one core, many tellings — read live from <code>manifest.yaml</code> · {today}</div>
</div><a class="home" href="/">&larr; Blog Workshop</a></div>""")

    P.append(f"""<div class="mast">
<span><b>pipeline</b> {_esc(meta.get('pipeline','—'))}</span>
<span><b>manifest</b> v{_esc(meta.get('version','—'))}</span>
<span><b>register head</b> {_esc(meta.get('register_head','—'))}</span>
<span><b>extractions</b> {len(extractions)}</span>
<span><b>work packages</b> {len(artifacts)}</span>
</div>""")

    # metrics
    order = [('done','done'),('ready','in ladder'),('live','ongoing'),
             ('draft','drafting'),('pending','pending'),('cold','parked')]
    P.append('<div class="metrics">')
    for st, lbl in order:
        n = wp_states.get(st, 0)
        if n:
            P.append(f'<div class="metric"><div class="n">{n}</div><div class="l">{lbl}</div></div>')
    P.append(f'<div class="metric"><div class="n">{ex_drafted}/{len(extractions)}</div><div class="l">extractions built</div></div>')
    P.append('</div>')

    # gate ladder
    P.append('<h2>The gate ladder</h2>')
    P.append('<div class="h2sub">every artifact climbs P0&rarr;P4; P4 (the completion read) is non-delegable — first person only.</div>')
    P.append('<div class="ladder">')
    for g in gates:
        gid = g.split('-')[0]
        cls = 'rung p4' if gid == 'P4' else 'rung'
        rest = g[len(gid)+1:].replace('-', ' ')
        P.append(f'<div class="{cls}"><b>{_esc(gid)}</b> {_esc(rest)}</div>')
    P.append('</div>')

    # work-package board
    P.append('<h2>Rehydration board</h2>')
    P.append('<div class="h2sub">work packages by tier — each one a telling of the extracted core for a named audience.</div>')
    for tier in TIER_ORDER:
        recs = by_tier.get(tier)
        if not recs:
            continue
        recs.sort(key=lambda r: (_status_state(r.get('status',''))[1], r['id']))
        tname, tcol = TIER_INFO.get(tier, (tier, '#7a7a7a'))
        P.append(f'<div class="tierhd"><span class="tierdot" style="background:{tcol}"></span>'
                 f'<h3>{_esc(tname)}</h3><span class="c">{len(recs)} package{"s" if len(recs)!=1 else ""}</span></div>')
        P.append('<div class="grid">')
        for a in recs:
            cls, _ = _status_state(a.get('status', ''))
            gate = a.get('gate')
            gate_pill = f'<span class="pill gate">{_esc(gate)}</span>' if gate and gate != 'null' else ''
            thrust = a.get('thrust')
            thrust_pill = f'<span class="pill thrust">{_esc(thrust)}</span>' if thrust else ''
            ex = a.get('extraction')
            ex_txt = ', '.join(ex) if isinstance(ex, list) else (ex or '—')
            if ex_txt in ('null', 'None', ''):
                ex_txt = '—'
            chain = a.get('chain')
            chain_txt = ' &rarr; '.join(_esc(c) for c in chain) if isinstance(chain, list) else '—'
            due = a.get('due', '—')
            note = a.get('note', '')
            note_html = ''
            if note:
                note_html = (f'<details class="note"><summary>provenance</summary>'
                             f'<div class="body">{_esc(note)}</div></details>')
            P.append(f"""<div class="card {cls}">
<h3><span class="wid">{_esc(a['id'])}</span> · {_esc(a.get('name','—'))}</h3>
<div class="pills"><span class="pill status {cls}">{_esc(a.get('status','—'))}</span>{gate_pill}{thrust_pill}</div>
<div class="meta">lineage: <code>{_esc(ex_txt)}</code></div>
<div class="meta">chain: {chain_txt}</div>
<div class="foot"><span class="meta">due {_esc(due)}</span>{_read_link(a.get('path',''))}</div>
{note_html}</div>""")
        P.append('</div>')

    # extraction lineage
    P.append('<h2>Extraction lineage</h2>')
    P.append('<div class="h2sub">the shared cores — claims lifted from canon under the P0 fidelity fence — that every telling above rehydrates.</div>')
    P.append('<div class="exgrid">')
    for e in sorted(extractions, key=lambda r: int(_re.sub(r'\D','',r['id']) or 0)):
        cls, _ = _status_state(e.get('status', ''))
        cc = _claim_count(e.get('note', ''))
        srcs = e.get('sources')
        nsrc = len(srcs) if isinstance(srcs, list) else 0
        bits = []
        if cc: bits.append(f'{cc} claims')
        if nsrc: bits.append(f'{nsrc} sources')
        bits.append(f"owner {e.get('owner','—')}")
        P.append(f"""<div class="ex">
<h4>{_esc(e['id'])} · {_esc(e.get('name','—'))}</h4>
<div class="pills"><span class="pill status {cls}">{_esc(e.get('status','—'))}</span></div>
<div class="m">{_esc(' · '.join(bits))}</div>
<div class="m" style="margin-top:6px">{_read_link(e.get('path',''), 'open extraction')}</div>
</div>""")
    P.append('</div>')

    # supporting shelves (scanned live)
    def _ls(sub, pat='.md'):
        d = os.path.join(PIPE, sub)
        if not os.path.isdir(d):
            return []
        return sorted(fn for fn in os.listdir(d) if fn.endswith(pat))

    roles = _ls('roles')
    reviews = [r for r in _ls('reviews') if r != 'critiques_ledger.md']
    chronicles = sorted(_ls('chronicles'), reverse=True)
    ledger_full = f"{PIPE}/reviews/critiques_ledger.md"
    ledger_n = 0
    if os.path.exists(ledger_full):
        with open(ledger_full, encoding='utf-8') as f:
            ledger_n = len(_re.findall(r'^\[L\d+\]', f.read(), _re.M))

    P.append('<h2>Working record</h2>')
    P.append('<div class="h2sub">the roles that run the ladder, the append-only ledger, the reviews, and the session chronicles.</div>')
    P.append('<div class="shelves">')

    # ledger
    P.append(f'<div class="shelf"><h4>Critiques ledger</h4><ul>'
             f'<li><a href="/{urllib.parse.quote(ledger_full)}">critiques_ledger.md</a> '
             f'<span class="more">· {ledger_n} entries</span></li></ul></div>')

    # roles
    P.append('<div class="shelf"><h4>Roles · A0&ndash;A13</h4><ul>')
    for r in roles:
        rid = r.split('-')[0]
        P.append(f'<li><a href="/{urllib.parse.quote(PIPE+"/roles/"+r)}">{_esc(r[:-3])}</a></li>')
    P.append('</ul></div>')

    # reviews
    P.append('<div class="shelf"><h4>Reviews &amp; briefs</h4><ul>')
    for r in reviews[:10]:
        P.append(f'<li><a href="/{urllib.parse.quote(PIPE+"/reviews/"+r)}">{_esc(r[:-3])}</a></li>')
    P.append('</ul></div>')

    # chronicles
    P.append('<div class="shelf"><h4>Chronicles</h4><ul>')
    for c in chronicles[:8]:
        P.append(f'<li><a href="/{urllib.parse.quote(PIPE+"/chronicles/"+c)}">{_esc(c[:-3])}</a></li>')
    if len(chronicles) > 8:
        P.append(f'<li class="more">+ {len(chronicles)-8} earlier</li>')
    P.append('</ul></div>')

    # existing readers
    P.append('<div class="shelf"><h4>Built readers</h4><ul>'
             f'<li><a href="/{urllib.parse.quote(PIPE+"/reader/index.html")}">Library reader</a></li>'
             f'<li><a href="/{urllib.parse.quote(PIPE+"/tracker/index.html")}">Fleet tracker</a></li>'
             f'<li><a href="/{urllib.parse.quote(PIPE+"/README.md")}">Pipeline README</a></li>'
             f'<li><a href="/{urllib.parse.quote(PIPE+"/SOURCES.md")}">Source registry</a></li>'
             '</ul></div>')

    P.append('</div>')  # shelves
    P.append('</div></body></html>')
    return ''.join(P)


class DocsHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        path = urllib.parse.unquote(parsed_path.path.strip('/'))
        
        # Serve index page
        if path == '' or path == 'index.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(self.generate_index(parsed_path.query).encode('utf-8'))
            return

        # Programme Console — the whole pipeline, read live from manifest.yaml
        if path in ('programme', 'programme/', 'console', 'console/'):
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(programme_console_html().encode('utf-8'))
            return

        # Special routes for README
        if path.lower() in ['readme', 'readme.md', '0xagentprivacy_readme', '0xagentprivacy_readme.md']:
            filename = 'README.md'
            if os.path.exists(filename):
                self.send_response(200)
                self.send_header('Content-type', 'text/html; charset=utf-8')
                self.end_headers()
                with open(filename, 'r', encoding='utf-8') as f:
                    md_content = f.read()
                html = self.markdown_to_html(md_content, filename)
                self.wfile.write(html.encode('utf-8'))
                return
        
        # Serve PDF files — delegate to the base SimpleHTTPRequestHandler so the
        # response carries Content-Length, Last-Modified, and HTTP Range (206)
        # support. Browser PDF viewers (Chrome/PDFium in particular) request the
        # file in byte ranges and render a blank page if the server ignores Range
        # or omits Content-Length, which the old hand-rolled writer did.
        if path.endswith('.pdf') or any((path == doc[0] or path.lower() == doc[0].lower()) and doc[3] == 'pdf' for doc in DOCUMENTS):
            filename = path
            if not filename.endswith('.pdf') or not os.path.exists(filename):
                filename = next((doc[0] for doc in DOCUMENTS if (path == doc[0] or path.lower() == doc[0].lower()) and doc[3] == 'pdf'), None)

            if filename and os.path.exists(filename):
                # Normalise the request path to the real file, then let the base
                # handler stream it with full headers + range support.
                self.path = '/' + urllib.parse.quote(filename)
                return super().do_GET()

        # Serve markdown files as HTML
        # Check if path matches any markdown document (handle URL encoding)
        decoded_path = urllib.parse.unquote(path)
        if decoded_path.endswith('.md') or any((decoded_path == doc[0] or decoded_path.lower() == doc[0].lower() or path == urllib.parse.quote(doc[0])) and doc[3] == 'md' for doc in DOCUMENTS):
            # Find the actual file
            filename = decoded_path
            if not filename.endswith('.md') or not os.path.exists(filename):
                # Try to find by matching against DOCUMENTS list
                for doc in DOCUMENTS:
                    if doc[3] == 'md' and (decoded_path == doc[0] or decoded_path.lower() == doc[0].lower() or path == urllib.parse.quote(doc[0])):
                        filename = doc[0]
                        break
                else:
                    filename = None
            
            if filename and os.path.exists(filename):
                self.send_response(200)
                self.send_header('Content-type', 'text/html; charset=utf-8')
                self.end_headers()
                
                # Read and convert markdown to HTML
                with open(filename, 'r', encoding='utf-8') as f:
                    md_content = f.read()
                
                html = self.markdown_to_html(md_content, filename)
                self.wfile.write(html.encode('utf-8'))
                return
        
        # Default: try to serve file
        return super().do_GET()
    
    def generate_index(self, query=''):
        import datetime
        # ---- Cadence: tunable spacing so the series can be played with ----
        qs = urllib.parse.parse_qs(query or '')
        def _int(name, default, lo, hi):
            try:
                return max(lo, min(hi, int(qs.get(name, [default])[0])))
            except (ValueError, TypeError):
                return default
        gap = _int('gap', 7, 0, 60)    # days between arcs (the interval to play with)
        step = _int('step', 2, 1, 14)  # days between posts within an arc
        try:
            today = datetime.date.today()
        except Exception:
            today = None
        # Assign a publish day-offset to each post path.
        schedule = {}
        cursor, first = 0, True
        for arc in BLOG_SERIES:
            if not first:
                cursor += gap
            first = False
            for i, p in enumerate(arc["posts"]):
                schedule[p["path"]] = cursor + i * step
            if arc["posts"]:
                cursor += (len(arc["posts"]) - 1) * step

        html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>0xagentprivacy Living Documentation</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            color: #e0e0e0;
            background: #1a1a1a;
            padding: 20px;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: #2d2d2d;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.5);
        }
        h1 {
            color: #ffffff;
            margin-bottom: 10px;
            font-size: 2.5em;
        }
        .subtitle {
            color: #b0b0b0;
            margin-bottom: 30px;
            font-size: 1.2em;
        }
        .docs-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }
        .doc-card {
            border: 2px solid #404040;
            border-radius: 8px;
            padding: 20px;
            transition: all 0.3s ease;
            background: #252525;
        }
        .doc-card:hover {
            border-color: #5a9fd4;
            box-shadow: 0 4px 12px rgba(90, 159, 212, 0.3);
            transform: translateY(-2px);
        }
        .doc-card h2 {
            color: #ffffff;
            margin-bottom: 10px;
            font-size: 1.3em;
        }
        .doc-card p {
            color: #b0b0b0;
        }
        .doc-card a {
            display: inline-block;
            margin-top: 15px;
            padding: 10px 20px;
            background: #5a9fd4;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            transition: background 0.3s;
        }
        .doc-card a:hover {
            background: #4a8fc4;
        }
        .status {
            display: inline-block;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 0.85em;
            margin-left: 10px;
        }
        .status.complete { background: #2ecc71; color: white; }
        .info {
            background: #353535;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 30px;
            border-left: 4px solid #5a9fd4;
            color: #e0e0e0;
        }
        .section-title {
            color: #ffffff;
            font-size: 1.7em;
            margin: 45px 0 5px;
            padding-bottom: 8px;
            border-bottom: 2px solid #5a9fd4;
        }
        .section-sub { color: #b0b0b0; margin-bottom: 10px; }
        .browse details {
            background: #252525;
            border: 1px solid #404040;
            border-radius: 6px;
            margin: 10px 0;
            padding: 8px 16px;
        }
        .browse summary {
            cursor: pointer;
            color: #ffffff;
            font-weight: 600;
            font-size: 1.1em;
            padding: 6px 0;
        }
        .browse summary .count { color: #7a7a7a; font-weight: 400; font-size: 0.85em; }
        .browse ul { list-style: none; margin: 8px 0 8px 4px; }
        .browse li { margin: 4px 0; }
        .browse a { color: #a8d8ff; text-decoration: none; }
        .browse a:hover { color: #ffffff; text-decoration: underline; }
        .browse .pdf-tag { color: #e0a35a; font-size: 0.8em; margin-left: 6px; }
        /* Blog workshop */
        .cadence {
            background: #1d2233; border: 1px solid #3a4260; border-radius: 8px;
            padding: 12px 16px; margin: 6px 0 18px; display: flex; flex-wrap: wrap;
            align-items: center; gap: 10px 18px; font-size: 0.9em;
        }
        .cad-label { color: #cfd6ff; font-weight: 600; }
        .cad-group { color: #9aa0b8; }
        .cad {
            display: inline-block; margin-left: 4px; padding: 2px 9px; border-radius: 4px;
            background: #2a3145; color: #b8c0e0 !important; text-decoration: none; font-size: 0.9em;
        }
        .cad:hover { background: #38405c; }
        .cad.on { background: #5a9fd4; color: #06121f !important; font-weight: 700; }
        .cad-note { color: #7a809a; font-size: 0.85em; flex-basis: 100%; }
        .when {
            color: #8fb8d8; font-size: 0.8em; font-variant-numeric: tabular-nums;
            white-space: nowrap;
        }
        .arc { margin: 22px 0; }
        .arc-head { color: #d9b3ff; font-size: 1.15em; font-weight: 700; margin-bottom: 2px; }
        .arc-blurb { color: #9a9a9a; font-size: 0.92em; margin-bottom: 12px; }
        .post {
            display: flex; align-items: center; gap: 16px;
            background: #252525; border: 1px solid #404040; border-left: 3px solid #7a5cff;
            border-radius: 8px; padding: 14px 18px; margin: 8px 0;
            transition: all 0.2s ease;
        }
        .post:hover { border-color: #7a5cff; box-shadow: 0 3px 10px rgba(122,92,255,0.25); }
        .post-n {
            flex: 0 0 auto; width: 34px; height: 34px; border-radius: 50%;
            background: #1a1a1a; border: 1px solid #7a5cff; color: #d9b3ff;
            display: flex; align-items: center; justify-content: center; font-weight: 700;
        }
        .post-body { flex: 1 1 auto; min-width: 0; }
        .post-title { color: #ffffff; font-size: 1.15em; font-weight: 600; }
        .post-sub { color: #a8a8a8; font-size: 0.9em; margin-top: 2px; }
        .siblings { margin-top: 6px; font-size: 0.82em; color: #7a7a7a; }
        .siblings a { color: #e0a35a; text-decoration: none; }
        .siblings a:hover { text-decoration: underline; }
        .post-meta { flex: 0 0 auto; display: flex; align-items: center; gap: 12px; }
        .post-meta .status {
            padding: 3px 9px; border-radius: 4px; font-size: 0.78em; font-weight: 600; margin: 0;
        }
        .status.ready { background: #2ecc71; color: #06210f; }
        .status.draft { background: #e0a35a; color: #2b1a06; }
        .status.todo  { background: #555; color: #ddd; }
        .post-meta .target { color: #8a8a8a; font-size: 0.8em; }
        .post-meta .read {
            padding: 8px 16px; background: #7a5cff; color: #fff; text-decoration: none;
            border-radius: 5px; font-size: 0.9em; white-space: nowrap;
        }
        .post-meta .read:hover { background: #6a4cef; }
        .post-meta .read.disabled { background: #3a3a3a; color: #888; cursor: default; }
        @media (max-width: 640px) {
            .post { flex-wrap: wrap; }
            .post-meta { width: 100%; justify-content: flex-start; }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>(⚔️⊥⿻⊥🧙)🙂 0xagentprivacy Living Documentation</h1>
        <p class="subtitle">Privacy-First AI Agent Architecture for Human Sovereignty</p>
        
        <div class="info">
            <strong>📚 Blog Workshop + Living Documentation</strong><br>
            The <strong>Blog Workshop</strong> below is the distribution series — read the posts in order and sync each to its public surface.
            <strong>Featured</strong> documents follow, and <strong>Browse everything</strong> at the bottom lists every markdown and PDF, so nothing is hidden.
            <br><a href="/programme" style="display:inline-block;margin-top:8px;font-weight:600;">&rarr; Open the Programme Console</a> — the whole V6 rehydration pipeline (extractions, work packages, gate ladder), read live from the manifest.
        </div>
"""

        # Featured docs are rendered into this block now, emitted AFTER the workshop.
        featured_cards = ""
        for filename, title, description, file_type in DOCUMENTS:
            if not os.path.exists(filename):
                continue
            doc_path = 'README' if filename == 'README.md' else urllib.parse.quote(filename)
            link_text = "View PDF →" if file_type == 'pdf' else "Read Document →"
            featured_cards += f"""
            <div class="doc-card">
                <h2>{title}</h2>
                <p>{description}</p>
                <a href="/{doc_path}">{link_text}</a>
            </div>
"""

        # ---- BLOG WORKSHOP: the distribution series, in reading order ----
        def _gaplink(g):
            cls = "on" if g == gap else ""
            return f'<a class="cad {cls}" href="/?gap={g}&step={step}">{g}d</a>'
        def _steplink(s):
            cls = "on" if s == step else ""
            return f'<a class="cad {cls}" href="/?gap={gap}&step={s}">{s}d</a>'
        html += f"""
        <h2 class="section-title">Blog Workshop — the distribution series</h2>
        <p class="section-sub">Read the series in order, then sync each post to its public surface. Every post shows its status, its publish target, and its tier siblings (the same core told for other audiences).</p>
        <div class="cadence">
            <span class="cad-label">Cadence — play with the spacing:</span>
            <span class="cad-group">gap between arcs {_gaplink(0)}{_gaplink(3)}{_gaplink(7)}{_gaplink(14)}{_gaplink(21)}</span>
            <span class="cad-group">step within arc {_steplink(1)}{_steplink(2)}{_steplink(3)}</span>
            <span class="cad-note">The interval between the V6 math arc and the Foundations posts is the <strong>gap</strong>.</span>
        </div>
"""
        for arc in BLOG_SERIES:
            html += f"""
        <div class="arc">
            <div class="arc-head">{arc['arc']}</div>
            <div class="arc-blurb">{arc['blurb']}</div>
"""
            for p in arc["posts"]:
                exists = os.path.exists(p["path"])
                day = schedule.get(p["path"], 0)
                if today is not None:
                    d = today + datetime.timedelta(days=day)
                    when = f'Day {day} · {d.strftime("%a %d %b")}'
                else:
                    when = f'Day {day}'
                href = '/' + urllib.parse.quote(p["path"].replace('\\', '/'))
                st = p["status"]
                st_cls = "ready" if st == "post-ready" else ("draft" if exists else "todo")
                st_label = st if exists else "to write"
                read = f'<a class="read" href="{href}">Read →</a>' if exists else '<span class="read disabled">not written yet</span>'
                sib = ""
                if p["siblings"]:
                    links = " · ".join(
                        f'<a href="/{urllib.parse.quote(sp.replace(chr(92), "/"))}">{tier}</a>'
                        for tier, _title, sp in p["siblings"] if os.path.exists(sp))
                    if links:
                        sib = f'<div class="siblings">other tellings: {links}</div>'
                html += f"""
            <div class="post">
                <div class="post-n">{p['n']}</div>
                <div class="post-body">
                    <div class="post-title">{p['title']}</div>
                    <div class="post-sub">{p['subtitle']}</div>
                    {sib}
                </div>
                <div class="post-meta">
                    <span class="when">{when}</span>
                    <span class="status {st_cls}">{st_label}</span>
                    <span class="target">→ {p['target']}</span>
                    {read}
                </div>
            </div>
"""
            html += "        </div>\n"

        # V5 legacy series (compact)
        v5_cards = ""
        for filename, title in V5_BLOG:
            if os.path.exists(filename):
                v5_cards += f'                    <li><a href="/{urllib.parse.quote(filename)}">{title}</a></li>\n'
        if v5_cards:
            html += """
        <div class="browse">
            <details>
                <summary>Privacy is Value V5 — the earlier series (already published)</summary>
                <ul>
""" + v5_cards + """                </ul>
            </details>
        </div>
"""

        # ---- FEATURED docs (rendered above, emitted here, after the workshop) ----
        if featured_cards:
            html += """
        <h2 class="section-title">Featured documents</h2>
        <p class="section-sub">The V6 suite, the book, and the reference authorities.</p>
        <div class="docs-grid">
""" + featured_cards + """
        </div>
"""

        # Browse everything — auto-discovered tree of all remaining docs
        tree = discover_all_docs()
        total = sum(len(v) for v in tree.values())
        if tree:
            html += f"""
        <h2 class="section-title">Browse everything</h2>
        <p class="section-sub">{total} more markdown and PDF files across {len(tree)} folders — the full documentation, nothing hidden.</p>
        <div class="browse">
"""
            for top, items in tree.items():
                html += f"""            <details>
                <summary>{top} <span class="count">({len(items)})</span></summary>
                <ul>
"""
                for rel, is_pdf in items:
                    href = '/' + urllib.parse.quote(rel)
                    tag = '<span class="pdf-tag">PDF</span>' if is_pdf else ''
                    label = rel[len(top) + 1:] if top != '(root)' and rel.startswith(top + '/') else rel
                    html += f'                    <li><a href="{href}">{label}</a>{tag}</li>\n'
                html += """                </ul>
            </details>
"""
            html += """        </div>
"""

        html += """
        <div style="margin-top: 40px; padding-top: 20px; border-top: 2px solid #404040; color: #b0b0b0; text-align: center;">
            <p>Server running on <strong style="color: #ffffff;">http://localhost:7000</strong></p>
            <p>All documents served as HTML, with MathJax equations and syntax highlighting</p>
        </div>
    </div>
</body>
</html>"""
        return html
    
    def markdown_to_html(self, md_content, filename):
        # Strip a leading YAML frontmatter block ( --- ... --- ) so it does not
        # render as stray text at the top of the essays.
        if md_content.lstrip().startswith('---'):
            body = md_content.lstrip()
            end = body.find('\n---', 3)
            if end != -1:
                nl = body.find('\n', end + 1)
                md_content = body[nl + 1:] if nl != -1 else ''

        # Convert markdown to HTML
        md = markdown.Markdown(extensions=['extra', 'codehilite', 'tables', 'fenced_code'])
        html_content = md.convert(md_content)

        # In-series navigation: if this file is a workshop post, build a prev/next bar.
        prev_post, this_post, next_post = series_nav(filename)
        series_bar = ""
        if this_post is not None:
            def _link(post, arrow_left=False):
                if not post or not os.path.exists(post["path"]):
                    return '<span class="nav-empty"></span>'
                href = '/' + urllib.parse.quote(post["path"].replace('\\', '/'))
                arrow = "← " if arrow_left else ""
                tail = "" if arrow_left else " →"
                return f'<a class="nav-btn" href="{href}">{arrow}{post["title"]}{tail}</a>'
            sib = ""
            if this_post["siblings"]:
                links = " · ".join(
                    f'<a href="/{urllib.parse.quote(sp.replace(chr(92), "/"))}">{tier}: {t}</a>'
                    for tier, t, sp in this_post["siblings"] if os.path.exists(sp))
                if links:
                    sib = f'<div class="series-siblings">Other tellings of this core — {links}</div>'
            series_bar = f"""
        <div class="series-nav">
            <div class="series-tag">Blog Workshop · distribution series</div>
            <div class="series-nav-row">
                {_link(prev_post, arrow_left=True)}
                <span class="nav-here">{this_post['title']}</span>
                {_link(next_post)}
            </div>
            {sib}
        </div>
"""

        # Wrap in full HTML document
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{filename} - 0xagentprivacy Docs</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.8;
            color: #e0e0e0;
            background: #1a1a1a;
            padding: 20px;
        }}
        .container {{
            max-width: 1000px;
            margin: 0 auto;
            background: #2d2d2d;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.5);
        }}
        .back-link {{
            display: inline-block;
            margin-bottom: 20px;
            padding: 10px 20px;
            background: #5a9fd4;
            color: white;
            text-decoration: none;
            border-radius: 5px;
        }}
        .back-link:hover {{
            background: #4a8fc4;
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: #ffffff;
            margin-top: 30px;
            margin-bottom: 15px;
        }}
        h1 {{ font-size: 2.5em; border-bottom: 3px solid #5a9fd4; padding-bottom: 10px; }}
        h2 {{ font-size: 2em; border-bottom: 2px solid #404040; padding-bottom: 8px; }}
        h3 {{ font-size: 1.5em; }}
        p {{ margin-bottom: 15px; color: #e0e0e0; }}
        code {{
            background: #1a1a1a;
            color: #a8d8ff;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
            border: 1px solid #404040;
        }}
        pre {{
            background: #1a1a1a;
            color: #e0e0e0;
            padding: 20px;
            border-radius: 5px;
            overflow-x: auto;
            margin: 20px 0;
            border: 1px solid #404040;
        }}
        pre code {{
            background: transparent;
            padding: 0;
            color: inherit;
            border: none;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }}
        th, td {{
            border: 1px solid #404040;
            padding: 12px;
            text-align: left;
        }}
        th {{
            background: #3d3d3d;
            color: #ffffff;
        }}
        tr:nth-child(even) {{
            background: #252525;
        }}
        tr:nth-child(odd) {{
            background: #2d2d2d;
        }}
        td {{
            color: #e0e0e0;
        }}
        blockquote {{
            border-left: 4px solid #5a9fd4;
            padding-left: 20px;
            margin: 20px 0;
            color: #b0b0b0;
            font-style: italic;
            background: #252525;
            padding: 15px 20px;
            border-radius: 4px;
        }}
        a {{
            color: #5a9fd4;
            text-decoration: none;
        }}
        a:hover {{
            color: #7ab8e4;
            text-decoration: underline;
        }}
        ul, ol {{
            margin-left: 30px;
            margin-bottom: 15px;
        }}
        li {{
            margin-bottom: 8px;
            color: #e0e0e0;
        }}
        strong {{
            color: #ffffff;
        }}
        em {{
            color: #b0b0b0;
        }}
        .series-nav {{
            background: #21182f; border: 1px solid #4a3a6a; border-radius: 8px;
            padding: 14px 18px; margin-bottom: 26px;
        }}
        .series-tag {{ color: #b98cff; font-size: 0.78em; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 8px; }}
        .series-nav-row {{ display: flex; align-items: center; justify-content: space-between; gap: 12px; flex-wrap: wrap; }}
        .nav-btn {{ color: #d9b3ff !important; text-decoration: none; font-weight: 600; }}
        .nav-btn:hover {{ text-decoration: underline !important; }}
        .nav-here {{ color: #ffffff; font-weight: 700; text-align: center; flex: 1 1 auto; }}
        .nav-empty {{ flex: 0 0 60px; }}
        .series-siblings {{ margin-top: 10px; padding-top: 8px; border-top: 1px solid #3a2e55; font-size: 0.85em; color: #9a9a9a; }}
        .series-siblings a {{ color: #e0a35a !important; text-decoration: none; }}
        .series-siblings a:hover {{ text-decoration: underline !important; }}
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css">
    <style>
        /* Override highlight.js for better dark mode */
        .hljs {{
            background: #1a1a1a !important;
            color: #e0e0e0 !important;
        }}
    </style>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
    <script>hljs.highlightAll();</script>
    <script>
        window.MathJax = {{
            tex: {{ inlineMath: [['$', '$'], ['\\\\(', '\\\\)']], displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']] }},
            options: {{ skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'] }}
        }};
    </script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-mml-chtml.min.js" id="MathJax-script" async></script>
</head>
<body>
    <div class="container">
        <a href="/" class="back-link">← Back to Index</a>
        {series_bar}
        {html_content}
        {series_bar}
        <div style="margin-top: 40px; padding-top: 20px; border-top: 2px solid #404040;">
            <a href="/" class="back-link">← Back to Index</a>
        </div>
    </div>
</body>
</html>"""
        return html

if __name__ == "__main__":
    import sys
    # Fix Windows console encoding for emojis
    if sys.platform == 'win32':
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
    
    handler = DocsHandler

    # Threaded + address reuse: browser PDF viewers open several parallel,
    # keep-alive connections (range requests). A single-threaded server
    # serialises those and can appear to hang; threading keeps it responsive.
    class ThreadingServer(socketserver.ThreadingTCPServer):
        daemon_threads = True
        allow_reuse_address = True

    with ThreadingServer(("", PORT), handler) as httpd:
        print(f"Documentation server running at http://localhost:{PORT}")
        print(f"Serving {len(DOCUMENTS)} documents")
        print(f"Open http://localhost:{PORT} in your browser")
        print(f"Press Ctrl+C to stop")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped")

