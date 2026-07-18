#!/usr/bin/env python3
"""Library reader: renders EVERY programme doc (canon V6 papers, rehydrations,
extractions, reviews, chronicles, programme notes, observers, machinery) as its
own HTML page plus a wiki-style index. GR-6: generated, never hand-edited.

  python tools/build_library.py            # build reader/index.html + reader/docs/**
  python tools/build_library.py --serve    # build + serve at :7474

Output lands in the same reader/ dir the cycle reader uses, so a server
already running there picks the new pages up without a restart.
"""
import re, sys, html, pathlib

PIPELINE = pathlib.Path(__file__).resolve().parents[1]   # .../Programme/pipeline
PAPERS = PIPELINE.parents[1]                              # .../papers
OUT = PIPELINE / "reader"
PORT = 7474

# ---------------------------------------------------------------- groups ----
# (title, blurb, list of (papers-relative dir or file, recursive?))
GROUPS = [
    ("Canon · the V6 papers",
     "READ-ONLY to the runtime. The register these expressions rehydrate from.",
     [("v6", False)]),
    ("Rehydrations · the research expressions",
     "One register, many rooms: academic, grant, policy, public, standards.",
     [("Programme/pipeline/rehydrations", True)]),
    ("Extractions · claim inventories",
     "Tiered claim sets (S/A/G/P/D) that feed every rehydration.",
     [("Programme/pipeline/extractions", False)]),
    ("Reviews · the adversarial record",
     "Prior-art scans, persona reviews, the critiques ledger (append-only).",
     [("Programme/pipeline/reviews", True)]),
    ("Programme · direction and deadlines",
     "The autopath, runtime notes, deadline table.",
     [("Programme/pipeline/programme", False)]),
    ("Chronicles · the working record",
     "Per-seat chronicles. The long read stitches the cycle chronicles together.",
     [("Programme/pipeline/chronicles", False)]),
    ("Observers · the outside eye",
     "GPT-5.6 audit intake. Surfaces into papers only through chronicles (D2).",
     [("Programme/observers", False)]),
    ("Overlays · the poetic threads",
     "The Loomkeeper's lane: proverbs, protocols, spells, sci-fi concepts, woven and minted as understanding keys.",
     [("Programme/overlays", True)]),
    ("Machinery · rules, roles, tasks, templates",
     "How the runtime is allowed to move.",
     [("Programme/pipeline/GROUND_RULES.md", False),
      ("Programme/pipeline/README.md", False),
      ("Programme/pipeline/SOURCES.md", False),
      ("Programme/pipeline/CLAUDE.md", False),
      ("Programme/pipeline/manifest.yaml", False),
      ("Programme/pipeline/roles", False),
      ("Programme/pipeline/tasks", False),
      ("Programme/pipeline/templates", True)]),
]

CSS = """
:root{--ink:#1a1d21;--soft:#5a6470;--line:#e3ddd2;--bg:#faf7f1;--acc:#7a5c2e;--chip:#efe9dd}
@media(prefers-color-scheme:dark){:root{--ink:#e8e4dc;--soft:#9aa3ad;--line:#3a3f45;--bg:#17191c;--acc:#c9a86a;--chip:#26292e}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);
font:18px/1.7 Georgia,'Times New Roman',serif}
.wrap{max-width:50rem;margin:0 auto;padding:3rem 1.4rem 8rem}
h1{font-size:1.9rem;line-height:1.2;margin:2.5rem 0 .6rem}
h2{font-size:1.3rem;margin:2.6rem 0 .8rem;border-bottom:1px solid var(--line);padding-bottom:.4rem}
h3{font-size:1.05rem;margin:1.8rem 0 .5rem}h4{font-size:1rem;margin:1.5rem 0 .4rem}
p{margin:0 0 1.15rem}hr{border:0;border-top:1px solid var(--line);margin:2.6rem 0}
em{color:var(--soft)}strong{color:var(--acc)}
a{color:var(--acc)}a:hover{text-decoration:underline}
code{font:.85em ui-monospace,Consolas,monospace;background:var(--chip);
padding:.08em .35em;border-radius:4px}
pre{font:14px/1.55 ui-monospace,Consolas,monospace;background:var(--chip);
border:1px solid var(--line);border-radius:8px;padding:.9rem 1.1rem;overflow-x:auto}
pre code{background:none;padding:0}
blockquote{margin:0 0 1.15rem;padding:.1rem 0 .1rem 1.1rem;border-left:3px solid var(--acc);color:var(--soft)}
table{border-collapse:collapse;margin:0 0 1.25rem;font-size:.88em;display:block;overflow-x:auto}
th,td{border:1px solid var(--line);padding:.35rem .7rem;text-align:left;vertical-align:top}
th{background:var(--chip)}
.meta{font:13px/1.6 ui-monospace,Consolas,monospace;color:var(--soft);
border:1px solid var(--line);border-radius:8px;padding:.7rem 1rem;margin:1.2rem 0 2rem;
overflow-x:auto;white-space:pre-wrap}
.crumb{font:14px ui-monospace,Consolas,monospace;color:var(--soft)}
.crumb a{color:var(--acc);text-decoration:none}
ul,ol{margin:0 0 1.15rem;padding-left:1.4rem}li{margin:.28rem 0}
.chip{display:inline-block;font:11px ui-monospace,Consolas,monospace;background:var(--chip);
border:1px solid var(--line);border-radius:99px;padding:.05rem .55rem;margin-left:.5rem;color:var(--soft)}
.blurb{color:var(--soft);font-style:italic;margin-top:-.3rem}
.small{color:var(--soft);font-size:.85rem}
.idx li{margin:.4rem 0}
#q{width:100%;font:16px Georgia,serif;padding:.55rem .8rem;border:1px solid var(--line);
border-radius:8px;background:var(--bg);color:var(--ink);margin:1.2rem 0}
.hero{border:1px solid var(--line);border-radius:10px;padding:1rem 1.3rem;margin:1.6rem 0;background:var(--chip)}
details{margin:.6rem 0}summary{cursor:pointer;color:var(--acc)}
"""

FILTER_JS = """
document.getElementById('q').addEventListener('input',function(){
  var q=this.value.toLowerCase();
  document.querySelectorAll('.idx li').forEach(function(li){
    li.style.display=li.textContent.toLowerCase().includes(q)?'':'none';});
  document.querySelectorAll('.group').forEach(function(g){
    var any=[].some.call(g.querySelectorAll('.idx li'),function(li){return li.style.display!=='none';});
    g.style.display=any?'':'none';
    if(q) g.querySelectorAll('details').forEach(function(d){d.open=true;});
  });
});
"""

# ------------------------------------------------------------- rendering ----
def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

def parse_front(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}, "", text
    fm = {}
    for line in m.group(1).splitlines():
        km = re.match(r"^([A-Za-z0-9_-]+):\s*(.+?)\s*$", line)
        if km:
            fm[km.group(1).lower()] = km.group(2).strip("'\"")
    return fm, m.group(1), text[m.end():]

def inline(s, rel_to_root=""):
    s = html.escape(s, quote=False)
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*\*(.+?)\*\*\*", r"<strong><em>\1</em></strong>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
    def link(m):
        label, target = m.group(1), m.group(2)
        if target.startswith(("http://", "https://", "#")):
            return '<a href="%s">%s</a>' % (target, label)
        base = target.split("#")[0]
        frag = target[len(base):]
        if base.endswith((".md", ".yaml", ".yml", ".py", ".txt")):
            return '<a href="%s%s.html%s">%s</a>' % (rel_to_root, base, frag, label)
        return '<a href="%s">%s</a>' % (target, label)
    s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, s)
    return s

def md_to_html(text, rel_to_root=""):
    out, para, mode = [], [], None   # mode: None | 'ul' | 'ol' | 'code' | 'table' | 'quote'
    table_rows = []
    def flush_para():
        nonlocal para
        if para:
            out.append("<p>%s</p>" % inline(" ".join(para), rel_to_root)); para = []
    def close_list():
        nonlocal mode
        if mode in ("ul", "ol"):
            out.append("</%s>" % mode); mode = None
        elif mode == "quote":
            out.append("</blockquote>"); mode = None
    def flush_table():
        nonlocal mode, table_rows
        if mode == "table":
            body = []
            for i, cells in enumerate(table_rows):
                tag = "th" if i == 0 else "td"
                body.append("<tr>%s</tr>" % "".join(
                    "<%s>%s</%s>" % (tag, inline(c, rel_to_root), tag) for c in cells))
            out.append("<table>%s</table>" % "".join(body))
            table_rows, mode = [], None
    for raw in text.splitlines():
        ls = raw.strip()
        if mode == "code":
            if ls.startswith("```"):
                out.append("</code></pre>"); mode = None
            else:
                out.append(html.escape(raw))
            continue
        if ls.startswith("```"):
            flush_para(); close_list(); flush_table()
            out.append("<pre><code>"); mode = "code"; continue
        if ls.startswith("|") and ls.endswith("|"):
            flush_para(); close_list()
            cells = [c.strip() for c in ls.strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
                continue  # separator row
            if mode != "table":
                mode = "table"
            table_rows.append(cells); continue
        flush_table()
        if ls.startswith(">"):
            flush_para()
            if mode != "quote":
                close_list(); out.append("<blockquote>"); mode = "quote"
            out.append("<p>%s</p>" % inline(ls.lstrip("> ").strip(), rel_to_root)); continue
        if mode == "quote" and ls:
            out.append("<p>%s</p>" % inline(ls, rel_to_root)); continue
        m_ul = re.match(r"^[-*]\s+(.*)$", ls)
        m_ol = re.match(r"^\d+[.)]\s+(.*)$", ls)
        if m_ul or m_ol:
            flush_para()
            want = "ul" if m_ul else "ol"
            if mode != want:
                close_list(); out.append("<%s>" % want); mode = want
            out.append("<li>%s</li>" % inline((m_ul or m_ol).group(1), rel_to_root)); continue
        if mode in ("ul", "ol") and ls:
            out.append("<li style='list-style:none'>%s</li>" % inline(ls, rel_to_root)); continue
        close_list()
        if not ls:
            flush_para(); continue
        if re.fullmatch(r"-{3,}|\*{3,}|_{3,}", ls):
            flush_para(); out.append("<hr>"); continue
        hm = re.match(r"^(#{1,4})\s+(.*)$", ls)
        if hm:
            flush_para()
            lvl = len(hm.group(1))
            out.append('<h%d id="%s">%s</h%d>' % (lvl, slugify(hm.group(2)),
                       inline(hm.group(2), rel_to_root), lvl))
            continue
        para.append(ls)
    flush_para(); close_list(); flush_table()
    if mode == "code":
        out.append("</code></pre>")
    return "\n".join(out)

def page(title, body, depth):
    root = "../" * depth
    return ("<!doctype html>\n"
            '<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">\n'
            "<title>%s</title>\n<style>%s</style>\n"
            '<div class="wrap"><p class="crumb"><a href="%sindex.html">&larr; library index</a>'
            ' &middot; <a href="%scycles.html">the long read</a></p>\n%s\n'
            '<hr><p class="small">generated by tools/build_library.py &middot; GR-6: never hand-edit</p></div>'
            % (html.escape(title), CSS, root, root, body))

# ----------------------------------------------------------------- build ----
def collect(entry, recursive):
    p = PAPERS / entry
    if p.is_file():
        return [p]
    if not p.is_dir():
        return []
    pat = "**/*" if recursive else "*"
    exts = (".md", ".yaml", ".yml", ".json")
    return sorted(f for f in p.glob(pat) if f.is_file() and f.suffix in exts)

def doc_title(path, fm, body_text):
    if fm.get("title"):
        return fm["title"]
    m = re.search(r"^#\s+(.+)$", body_text, re.M)
    if m:
        return re.sub(r"[*`]", "", m.group(1)).strip()
    return path.stem.replace("_", " ").replace("-", " ")

def build():
    (OUT / "docs").mkdir(parents=True, exist_ok=True)
    index_groups, built = [], 0
    for gtitle, gblurb, entries in GROUPS:
        items = []
        for entry, recursive in entries:
            for f in collect(entry, recursive):
                rel = f.relative_to(PAPERS)
                out_rel = pathlib.Path("docs") / rel.parent / (rel.name + ".html")
                depth = len(out_rel.parts) - 1
                text = f.read_text(encoding="utf-8", errors="replace")
                if f.suffix in (".yaml", ".yml", ".json"):
                    fm, body_text = {}, text
                    body = "<h1>%s</h1><pre><code>%s</code></pre>" % (
                        html.escape(f.name), html.escape(text))
                    title = f.name
                else:
                    fm, fm_raw, body_text = parse_front(text)
                    title = doc_title(f, fm, body_text)
                    meta = ('<div class="meta">%s</div>' % html.escape(fm_raw)) if fm_raw else ""
                    body = ('<p class="small">%s &middot; %d words</p>%s%s'
                            % (html.escape(str(rel)), len(body_text.split()), meta,
                               md_to_html(body_text, "../" * (depth - 1))))
                dest = OUT / out_rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(page(title, body, depth), encoding="utf-8")
                built += 1
                status = fm.get("status", "")
                words = len(body_text.split())
                items.append((title, str(out_rel).replace("\\", "/"), status, words, str(rel)))
        index_groups.append((gtitle, gblurb, items))
    write_index(index_groups)
    print("built reader/index.html + %d doc pages" % built)

def li(title, href, status, words, rel):
    short = re.split(r"[(;]", status)[0].strip()[:40] if status else ""
    chip = ('<span class="chip">%s</span>' % html.escape(short)) if short else ""
    return ('<li><a href="%s">%s</a>%s <span class="small">&middot; %s w &middot; %s</span></li>'
            % (href, html.escape(title), chip, f"{words:,}", html.escape(rel)))

def write_index(index_groups):
    parts = ['<!doctype html>',
             '<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">',
             "<title>V6 Research Programme · library</title>",
             "<style>%s</style>" % CSS, '<div class="wrap">',
             "<h1>The V6 Research Programme</h1>",
             '<p class="blurb">every doc in the pipeline, one page each. local, private, generated.</p>',
             '<div class="hero"><strong><a href="cycles.html">The Twelve Cycles</a></strong> '
             '— the long-read synthesis of the runtime, with all cycle chronicles appended. '
             'Start here if you are catching up.</div>',
             '<input id="q" type="search" placeholder="filter the library… (title, path, status)">']
    for gtitle, gblurb, items in index_groups:
        if not items:
            continue
        parts.append('<div class="group"><h2>%s <span class="small">(%d)</span></h2>'
                     '<p class="blurb">%s</p>' % (html.escape(gtitle), len(items), html.escape(gblurb)))
        # big groups fold: chronicles by date, machinery by kind
        if gtitle.startswith("Chronicles"):
            bydate = {}
            for it in items:
                d = re.match(r"(\d{4}-\d{2}-\d{2})", pathlib.Path(it[4]).name)
                bydate.setdefault(d.group(1) if d else "undated", []).append(it)
            for d in sorted(bydate, reverse=True):
                parts.append('<details><summary>%s (%d)</summary><ul class="idx">%s</ul></details>'
                             % (d, len(bydate[d]), "".join(li(*it) for it in bydate[d])))
        elif gtitle.startswith("Machinery"):
            bykind = {}
            for it in items:
                kind = pathlib.Path(it[4]).parts
                key = kind[2] if len(kind) > 3 else "root"
                bykind.setdefault(key, []).append(it)
            order = ["root", "roles", "tasks", "templates"]
            for k in sorted(bykind, key=lambda x: order.index(x) if x in order else 99):
                label = {"root": "ground rules · sources · manifest"}.get(k, k)
                openattr = " open" if k == "root" else ""
                parts.append('<details%s><summary>%s (%d)</summary><ul class="idx">%s</ul></details>'
                             % (openattr, html.escape(label), len(bykind[k]),
                                "".join(li(*it) for it in bykind[k])))
        else:
            parts.append('<ul class="idx">%s</ul>' % "".join(li(*it) for it in items))
        parts.append("</div>")
    parts.append('<hr><p class="small">generated by tools/build_library.py &middot; '
                 'rebuild: <code>python tools/build_library.py</code> &middot; GR-6: never hand-edit</p>'
                 "</div><script>%s</script>" % FILTER_JS)
    (OUT / "index.html").write_text("\n".join(parts), encoding="utf-8")

if __name__ == "__main__":
    build()
    if "--serve" in sys.argv:
        import http.server, functools as ft
        handler = ft.partial(http.server.SimpleHTTPRequestHandler, directory=str(OUT))
        print(f"serving http://localhost:{PORT}/  (Ctrl-C to stop)")
        http.server.ThreadingHTTPServer(("127.0.0.1", PORT), handler).serve_forever()
