#!/usr/bin/env python3
"""Narrative reader for the V6 Gathering Arc (the moving-ceiling blogs).

A deliberately SEPARATE surface from the pipeline fleet-tracker at :7272 — this
board is the *narrative* being written for sync.soulbis.com (three public V6
essays + the arc spine), in a warm "letters" register so it never reads like the
graphite docs-research wall-board.

Canonical essay sources are the pipeline rehydrations (rehydrations/public/*),
so edits there feed WP-01/25/28 directly. Manifest status is read live, so the
board stays honest as the pipeline moves. Generated output lives in reader/ —
never hand-edit it; fix the .md sources or this generator and rebuild.

    python build_arc_reader.py            # build reader/
    python build_arc_reader.py --serve    # build + serve at :7373
"""
from __future__ import annotations
import argparse, html, http.server, re, socketserver
from pathlib import Path

HERE     = Path(__file__).resolve().parent                 # papers/Programme/blog
PIPELINE = HERE.parent / "pipeline"
PUBLIC   = PIPELINE / "rehydrations" / "public"
MANIFEST = PIPELINE / "manifest.yaml"
OUT      = HERE / "reader"
PORT     = 7373

# The arc, in publishing order. Sources are the canonical pipeline rehydrations.
SPINE = {
    "file": HERE / "ARC_the_gathering.md",
    "title": "The Gathering Arc",
    "tag": "arc",
    "hook": "The plan: V6 arriving in public, three ways — one clock, one counsel, one set of doors.",
}
POSTS = [
    {"tag": "post1", "wp": "WP-01", "src": PUBLIC / "the_moving_ceiling.md",
     "register": "formal", "day": "Day 1",
     "owns": "The argument — R(t), t*, the behavioural turn, rotate / outrun / forget, the pricing turn.",
     "hook": "Every static privacy guarantee has a shelf life. The first V6 result."},
    {"tag": "post2", "wp": "WP-25", "src": PUBLIC / "the_uncarved_date.md",
     "register": "City", "day": "Day 3–4",
     "owns": "The counsel — the three guilds' objections, the three counsels, Selene's line.",
     "hook": "A tale from the City of Mages. The formal companion to The Moving Ceiling."},
    {"tag": "post3", "wp": "WP-28", "src": PUBLIC / "competence_without_history.md",
     "register": "formal", "day": "Day 7–8",
     "owns": "The doors — the atlas, the skills, the game, the wiki; C83's leakage fold, first airing.",
     "hook": "The gathering turn has doors, entered by demonstrated understanding, not history."},
]
# Off-arc letters: in the publish-note system but outside the arc's ownership map.
LETTERS = [
    {"tag": "letter-fleet-cap", "src": PUBLIC / "letter_the_fleet_and_the_cap.md",
     "register": "letter", "day": "off-arc",
     "owns": "The process story — honesty enforced by architecture; the path record as the discovery.",
     "hook": "The runtime's first day. PUBLISH-AFTER-EPRINT fence holds on the formal result."},
]

# ------------------------------------------------------------- manifest -----
def manifest_status() -> dict:
    """Return {WP-xx: {status, gate, note}} parsed from the flow-map manifest."""
    out: dict[str, dict] = {}
    if not MANIFEST.exists():
        return out
    txt = MANIFEST.read_text(encoding="utf-8")
    for m in re.finditer(r"(WP-\d+):\s*\{(.*?)\}", txt, flags=re.S):
        wp, body = m.group(1), m.group(2)
        def field(k):
            fm = re.search(rf"{k}:\s*([^,}}]+)", body)
            return fm.group(1).strip() if fm else ""
        out[wp] = {"status": field("status"), "gate": field("gate"), "note": field("note")}
    return out

# ---------------------------------------------------------------- markdown ---
def _inline(s: str) -> str:
    s = html.escape(s, quote=False)
    codes: list[str] = []
    s = re.sub(r"`([^`]+)`", lambda m: (codes.append(m.group(1)), f"\x00{len(codes)-1}\x00")[1], s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)",
               lambda m: f'<a href="{html.escape(m.group(2),quote=True)}">{m.group(1)}</a>', s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*(?!\*)([^*]+)\*(?!\*)", r"<em>\1</em>", s)
    s = re.sub(r"\x00(\d+)\x00", lambda m: f"<code>{html.escape(codes[int(m.group(1))])}</code>", s)
    return s

def md_to_html(text: str) -> str:
    out, lines, i = [], text.splitlines(), 0
    while i < len(lines):
        ln = lines[i]
        if not ln.strip():
            i += 1; continue
        if ln.startswith("```"):
            i += 1; buf = []
            while i < len(lines) and not lines[i].startswith("```"):
                buf.append(html.escape(lines[i])); i += 1
            i += 1; out.append("<pre><code>" + "\n".join(buf) + "</code></pre>"); continue
        m = re.match(r"(#{1,6})\s+(.*)", ln)
        if m:
            lvl = len(m.group(1)); out.append(f"<h{lvl}>{_inline(m.group(2))}</h{lvl}>"); i += 1; continue
        if re.match(r"^\s*([-*_])\s*\1\s*\1[\s\1]*$", ln):
            out.append("<hr>"); i += 1; continue
        if ln.startswith(">"):
            buf = []
            while i < len(lines) and lines[i].startswith(">"):
                buf.append(_inline(lines[i].lstrip(">").strip())); i += 1
            out.append("<blockquote>" + "<br>".join(buf) + "</blockquote>"); continue
        if re.match(r"^\s*[-*]\s+", ln):
            buf = []
            while i < len(lines) and re.match(r"^\s*[-*]\s+", lines[i]):
                buf.append("<li>" + _inline(re.sub(r"^\s*[-*]\s+","",lines[i])) + "</li>"); i += 1
            out.append("<ul>" + "".join(buf) + "</ul>"); continue
        if re.match(r"^\s*\d+\.\s+", ln):
            buf = []
            while i < len(lines) and re.match(r"^\s*\d+\.\s+", lines[i]):
                buf.append("<li>" + _inline(re.sub(r"^\s*\d+\.\s+","",lines[i])) + "</li>"); i += 1
            out.append("<ol>" + "".join(buf) + "</ol>"); continue
        buf = []
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#{1,6}\s|>|```|\s*[-*]\s|\s*\d+\.\s)", lines[i]) \
              and not re.match(r"^\s*([-*_])\s*\1\s*\1", lines[i]):
            buf.append(_inline(lines[i].strip())); i += 1
        out.append("<p>" + "<br>".join(buf) + "</p>")
    return "\n".join(out)

# ------------------------------------------------------------------ parse ----
def frontmatter(raw: str) -> tuple[dict, str]:
    m = re.match(r"^---\n(.*?)\n---\n", raw, flags=re.S)
    if not m:
        return {}, raw
    fm = {}
    for line in m.group(1).splitlines():
        km = re.match(r'\s*([\w-]+):\s*(.*)', line)
        if km:
            fm[km.group(1)] = km.group(2).strip().strip('"')
    return fm, raw[m.end():]

def parse(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    fm, body = frontmatter(raw)
    title = fm.get("title") or next((l[2:].strip() for l in body.splitlines() if l.startswith("# ")), path.stem)
    words = len(re.findall(r"\w+", body))
    return {"title": title, "subtitle": fm.get("subtitle", ""), "version": fm.get("version", ""),
            "words": words, "mins": max(1, round(words / 220)), "html": md_to_html(body),
            "rel": path}

# --------------------------------------------------------------- template ----
CSS = """
:root{--ink:#2b2420;--ink-soft:#6b5f54;--parch:#f7f1e6;--card:#fffdf8;--rule:#e4d9c6;
  --accent:#a8712d;--accent-soft:#c9975422;--gold:#3f9e4a;--shadow:0 1px 3px #2b241612;}
@media (prefers-color-scheme:dark){:root{--ink:#ece3d4;--ink-soft:#a99d8b;--parch:#1c1815;
  --card:#252017;--rule:#3a3128;--accent:#d8a35a;--accent-soft:#d8a35a1c;--gold:#5cc169;--shadow:0 1px 3px #0006;}}
:root[data-theme=light]{--ink:#2b2420;--ink-soft:#6b5f54;--parch:#f7f1e6;--card:#fffdf8;--rule:#e4d9c6;--accent:#a8712d;--accent-soft:#c9975422;--gold:#3f9e4a;--shadow:0 1px 3px #2b241612;}
:root[data-theme=dark]{--ink:#ece3d4;--ink-soft:#a99d8b;--parch:#1c1815;--card:#252017;--rule:#3a3128;--accent:#d8a35a;--accent-soft:#d8a35a1c;--gold:#5cc169;--shadow:0 1px 3px #0006;}
*{box-sizing:border-box}
body{margin:0;background:var(--parch);color:var(--ink);font:17px/1.7 Georgia,'Iowan Old Style',Cambria,serif;-webkit-font-smoothing:antialiased}
a{color:var(--accent);text-decoration:none} a:hover{text-decoration:underline}
.wrap{max-width:44rem;margin:0 auto;padding:2.4rem 1.3rem 6rem}
.masthead{border-bottom:2px solid var(--rule);padding-bottom:1.3rem}
.kicker{font:600 12px/1 ui-sans-serif,system-ui,sans-serif;letter-spacing:.16em;text-transform:uppercase;color:var(--accent)}
.masthead h1{font-size:2rem;margin:.5rem 0 .3rem;letter-spacing:-.01em}
.masthead p{margin:.2rem 0 0;color:var(--ink-soft);font-style:italic}
.crossnav{font:500 13px/1 ui-sans-serif,system-ui,sans-serif;margin-top:1rem}
.crossnav a{display:inline-block;padding:.35rem .7rem;border:1px solid var(--rule);border-radius:99px;color:var(--ink-soft)}
.spine{background:var(--accent-soft);border:1px dashed var(--accent);border-radius:12px;padding:1rem 1.2rem;margin:1.3rem 0}
.spine .row{display:flex;align-items:baseline;gap:.6rem}
.spine h2{font-size:1.15rem;margin:0;flex:1} .spine .hook{color:var(--ink-soft);margin:.3rem 0 0;font-style:italic}
.spine a.open{font:600 12px/1 ui-sans-serif,system-ui,sans-serif;color:var(--accent)}
.card{display:block;background:var(--card);border:1px solid var(--rule);border-radius:12px;
  padding:1.15rem 1.3rem;margin:1rem 0;box-shadow:var(--shadow);transition:transform .12s,border-color .12s}
.card:hover{transform:translateY(-2px);border-color:var(--accent);text-decoration:none}
.card.gated{border-left:4px solid var(--accent)}
.card .row{display:flex;align-items:baseline;gap:.6rem;margin-bottom:.25rem;flex-wrap:wrap}
.num{font:700 12px/1 ui-sans-serif,system-ui,sans-serif;color:var(--accent);background:var(--accent-soft);padding:.3rem .5rem;border-radius:6px;white-space:nowrap}
.card h2{font-size:1.28rem;margin:0;color:var(--ink);flex:1;min-width:60%}
.owns{margin:.35rem 0 .2rem} .owns b{color:var(--ink)}
.hook{color:var(--ink-soft);margin:.15rem 0 .7rem;font-style:italic}
.meta{font:500 12.5px/1 ui-sans-serif,system-ui,sans-serif;color:var(--ink-soft);display:flex;gap:.85rem;flex-wrap:wrap;align-items:center}
.chip{padding:.22rem .5rem;border-radius:99px;font-weight:600;font-size:11.5px;letter-spacing:.03em;border:1px solid var(--rule)}
.chip.gate{color:var(--accent);background:var(--accent-soft);border-color:var(--accent)}
.chip.reg{color:var(--ink-soft)} .chip.day{color:var(--ink-soft)}
.p4{color:var(--accent);font-weight:600}
.file{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:11px}
.reader h1{font-size:1.9rem;line-height:1.2;margin:.2rem 0 .3rem}
.reader .sub{color:var(--ink-soft);font-style:italic;margin:0 0 1.4rem}
.reader h2{font-size:1.4rem;margin:2.2rem 0 .6rem;border-bottom:1px solid var(--rule);padding-bottom:.3rem}
.reader h3{font-size:1.15rem;margin:1.7rem 0 .5rem}
.reader p{margin:.9rem 0} .reader hr{border:0;border-top:1px solid var(--rule);margin:2rem 0}
.reader blockquote{margin:1.2rem 0;padding:.4rem 0 .4rem 1.1rem;border-left:3px solid var(--accent);color:var(--ink-soft);font-style:italic}
.reader code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.9em;background:var(--accent-soft);padding:.1em .35em;border-radius:4px}
.reader pre{background:var(--card);border:1px solid var(--rule);border-radius:8px;padding:1rem;overflow-x:auto} .reader pre code{background:none;padding:0}
.reader ul,.reader ol{padding-left:1.4rem} .reader li{margin:.3rem 0}
.pagenav{display:flex;justify-content:space-between;gap:1rem;margin-top:3rem;padding-top:1.4rem;border-top:2px solid var(--rule);font:500 14px/1.4 ui-sans-serif,system-ui,sans-serif}
.pagenav a{max-width:45%} .pagenav .next{text-align:right;margin-left:auto}
.pagenav small{display:block;color:var(--ink-soft);font-size:11px;text-transform:uppercase;letter-spacing:.08em}
.back{font:500 13px/1 ui-sans-serif,system-ui,sans-serif;color:var(--ink-soft);margin-bottom:1.2rem;display:inline-block}
.themebtn{position:fixed;top:1rem;right:1rem;background:var(--card);border:1px solid var(--rule);color:var(--ink-soft);border-radius:99px;padding:.4rem .8rem;cursor:pointer;font:500 12px/1 ui-sans-serif,system-ui,sans-serif}
"""
THEME_JS = "(function(){var r=document.documentElement,b=document.getElementById('t');function cur(){return r.getAttribute('data-theme')||(matchMedia('(prefers-color-scheme:dark)').matches?'dark':'light')}b.onclick=function(){r.setAttribute('data-theme',cur()==='dark'?'light':'dark')}})();"

def page(title, inner):
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title>
<style>{CSS}</style></head><body><button class="themebtn" id="t">◐ theme</button>
<div class="wrap">{inner}</div><script>{THEME_JS}</script></body></html>"""

def build(stamp: str) -> int:
    OUT.mkdir(exist_ok=True)
    mani = manifest_status()
    spine = parse(SPINE["file"])
    posts = [{**p, **parse(p["src"]), "st": mani.get(p["wp"], {})} for p in POSTS]

    # index
    cards = []
    for k, p in enumerate(posts, 1):
        st = p["st"]
        gated = "pending P4" in (st.get("note", "")).lower()
        gate_chip = f'<span class="chip gate">{html.escape(st.get("gate","?"))} · {html.escape(st.get("status","?"))}</span>'
        p4 = '<span class="p4">◆ ship-ready — awaiting your P4 read</span>' if gated else ""
        cards.append(f"""<a class="card{' gated' if gated else ''}" href="{p['tag']}.html">
  <div class="row"><span class="num">Post {k} · {p['wp']}</span><h2>{html.escape(p['title'])}</h2></div>
  <div class="owns"><b>Owns:</b> {html.escape(p['owns'])}</div>
  <div class="hook">{html.escape(p['hook'])}</div>
  <div class="meta">{gate_chip}
    <span class="chip reg">{html.escape(p['register'])} register</span>
    <span class="chip day">{html.escape(p['day'])}</span>
    <span>{p['words']:,} words · ~{p['mins']} min</span>{p4}</div>
  <div class="meta" style="margin-top:.5rem"><span class="file">{p['src'].relative_to(PIPELINE.parent).as_posix()}</span></div>
</a>""")

    letters = [{**l, **parse(l["src"])} for l in LETTERS if l["src"].exists()]
    letter_cards = []
    for l in letters:
        letter_cards.append(f"""<a class="card" href="{l['tag']}.html" style="border-style:dashed">
  <div class="row"><span class="num">Letter · off-arc</span><h2>{html.escape(l['title'])}</h2></div>
  <div class="owns"><b>Owns:</b> {html.escape(l['owns'])}</div>
  <div class="hook">{html.escape(l['hook'])}</div>
  <div class="meta"><span class="chip reg">{html.escape(l['register'])} register</span>
    <span class="chip gate">P0 · awaiting P4</span>
    <span>{l['words']:,} words · ~{l['mins']} min</span></div>
  <div class="meta" style="margin-top:.5rem"><span class="file">{l['src'].relative_to(PIPELINE.parent).as_posix()}</span></div>
</a>""")
    letters_section = ""
    if letters:
        letters_section = ('<div class="kicker" style="margin-top:2rem">Letters · off-arc · publish-note system</div>'
                           + "".join(letter_cards))

    total = sum(p["words"] for p in posts)
    inner = f"""<div class="masthead">
  <div class="kicker">Narrative · the moving-ceiling blogs · for sync.soulbis.com</div>
  <h1>The Gathering Arc — V6</h1>
  <p>One clock, one counsel, one set of doors. V6 arriving in public, three ways.</p>
  <div class="crossnav"><a href="http://localhost:7272">← docs-research board (fleet tracker)</a></div>
</div>
<div class="spine">
  <div class="row"><h2>{html.escape(spine['title'])} <span style="font-weight:400;color:var(--ink-soft)">· the arc spine</span></h2>
  <a class="open" href="arc.html">read the plan →</a></div>
  <div class="hook">{html.escape(SPINE['hook'])}</div>
</div>
<div class="meta" style="margin:1.2rem 0 .3rem">
  <span>3 posts</span><span>{total:,} words</span><span>publishes across ~1 week</span><span>built {html.escape(stamp)}</span>
</div>
{''.join(cards)}
{letters_section}"""
    (OUT / "index.html").write_text(page("The Gathering Arc — V6 narrative", inner), encoding="utf-8")

    # letter reader pages (back-link only, no prev/next chain)
    for l in letters:
        inner_l = f"""<a class="back" href="index.html">← the arc</a>
<div class="meta" style="margin-bottom:1.1rem">
  <span class="num">Letter · off-arc</span>
  <span class="chip gate">P0 · awaiting P4</span>
  <span class="chip reg">{html.escape(l['register'])} register</span>
  <span>{l['words']:,} words · ~{l['mins']} min</span>
  <span class="file">{l['src'].relative_to(PIPELINE.parent).as_posix()}</span>
</div>
<article class="reader"><h1>{html.escape(l['title'])}</h1>
{f'<p class="sub">{html.escape(l["subtitle"])}</p>' if l['subtitle'] else ''}{l['html']}</article>"""
        (OUT / f"{l['tag']}.html").write_text(page(l["title"], inner_l), encoding="utf-8")

    # spine reader
    sp = f"""<a class="back" href="index.html">← the arc</a>
<article class="reader"><h1>{html.escape(spine['title'])}</h1>{spine['html']}</article>"""
    (OUT / "arc.html").write_text(page(spine["title"], sp), encoding="utf-8")

    # post readers
    for k, p in enumerate(posts):
        prev = posts[k-1] if k > 0 else None
        nxt  = posts[k+1] if k < len(posts)-1 else None
        pv = f'<a class="prev" href="{prev["tag"]}.html"><small>← previous</small>{html.escape(prev["title"])}</a>' if prev else '<a class="prev" href="arc.html"><small>← the arc</small>The Gathering Arc</a>'
        nx = f'<a class="next" href="{nxt["tag"]}.html"><small>next →</small>{html.escape(nxt["title"])}</a>' if nxt else ""
        st = p["st"]
        inner = f"""<a class="back" href="index.html">← the arc</a>
<div class="meta" style="margin-bottom:1.1rem">
  <span class="num">Post {k+1} · {p['wp']}</span>
  <span class="chip gate">{html.escape(st.get('gate','?'))} · {html.escape(st.get('status','?'))}</span>
  <span class="chip reg">{html.escape(p['register'])} register</span>
  <span>{p['words']:,} words · ~{p['mins']} min</span>
  <span class="file">{p['src'].relative_to(PIPELINE.parent).as_posix()}</span>
</div>
<article class="reader"><h1>{html.escape(p['title'])}</h1>
{f'<p class="sub">{html.escape(p["subtitle"])}</p>' if p['subtitle'] else ''}{p['html']}</article>
<nav class="pagenav">{pv}{nx}</nav>"""
        (OUT / f"{p['tag']}.html").write_text(page(p["title"], inner), encoding="utf-8")

    print(f"built {OUT/'index.html'} · arc spine + {len(posts)} posts · {total:,} words")
    return len(posts)

def serve():
    OUT.mkdir(exist_ok=True)
    class H(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *a, **k): super().__init__(*a, directory=str(OUT), **k)
        def log_message(self, *a): pass
    with socketserver.TCPServer(("127.0.0.1", PORT), H) as srv:
        print(f"serving gathering-arc reader at http://localhost:{PORT}  (ctrl-c to stop)")
        srv.serve_forever()

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--serve", action="store_true")
    ap.add_argument("--stamp", default="now")
    a = ap.parse_args()
    build(a.stamp)
    if a.serve:
        serve()
