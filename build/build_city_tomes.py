#!/usr/bin/env python3
"""
Binds the City of Mages tomes (the Second Person Spellbook) into one volume and
renders the web PDF. Source of truth is the cityofmages repo's tomes/ tree; the
binder assembles by manifest order at build time, so edits to any act flow into
the next build. Emoji-dense narrative: web render only (the academic pipeline
blanks emoji by design and is wrong for this expression).
Outputs: pdfs/city/_assembled (md) and pdfs/city/ (render).
"""
import re
import subprocess
from pathlib import Path

BUILD_DIR = Path(__file__).resolve().parent
ROOT = BUILD_DIR.parent
CITY = ROOT.parent / "cityofmages" / "tomes"
OUT_DIR = ROOT / "pdfs" / "city"
OUT_MD = OUT_DIR / "_assembled"
NAME = "city_of_mages_bound_collection"
TITLE = "The City of Mages · the Second Person Spellbook · the Bound Collection"

PAGEBREAK = "\n\n<div style=\"page-break-before: always\"></div>\n\n"

# Tome order is canonical, not lexical (roman numerals sort wrong as strings).
TOMES = [
    ("tome-i-the-convergence", "TOME I · The Convergence"),
    ("tome-ii-the-lyapunov", "TOME II · The Lyapunov"),
    ("tome-iii-selenes-witness", "TOME III · Selene's Witness"),
    ("tome-iv-the-witnessing", "TOME IV · The Witnessing"),
    ("tome-v-the-crafting", "TOME V · The Crafting"),
    ("tome-vi-the-reply", "TOME VI · The Reply"),
    ("tome-vii-the-parallel", "TOME VII · The Parallel"),
    ("tome-viii-the-library", "TOME VIII · The Library"),
    ("tome-ix-the-horizon", "TOME IX · The Horizon"),
]

FRONT = f"""# {TITLE}

*Bound from the cityofmages repository's tomes/ tree. Each act is written in the
second person and carries its own frontmatter in the source: honesty labels,
conjecture lineage, cast, and status. Tome statuses (closed · open · open by
design) live in the City of Mages grimoire registry; this volume binds the
narrative bodies in canonical order and adds nothing.*

*The registry pin at binding: city_of_mages_grimoire v1.8.0
(`bafybeihx7zn3frj6gln4bw5k3pxqnxoyumj42x4ohsjrhmro6q5vndw3ei`). The conjecture
numbering authority is `agentprivacy-docs/research/CONJECTURE_REGISTER_V6.md`
(head C89); where an act and the register disagree, the register wins.*

(⚔️⊥⿻⊥🧙)😊
"""


def strip_frontmatter(text):
    if text.startswith("---"):
        m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
        if m:
            return text[m.end():]
    return text


def main():
    OUT_MD.mkdir(parents=True, exist_ok=True)

    pieces = [FRONT]
    act_count = 0
    for slug, title in TOMES:
        d = CITY / slug
        if not d.is_dir():
            print(f"MISSING tome dir (skipped): {slug}")
            continue
        acts = sorted(d.glob("[0-9][0-9]-*.md"))
        if not acts:
            print(f"NO acts in {slug} (skipped)")
            continue
        pieces.append(f"# {title}\n")
        for a in acts:
            pieces.append(strip_frontmatter(a.read_text(encoding="utf-8")))
            act_count += 1

    body = PAGEBREAK.join(pieces)
    md = OUT_MD / f"{NAME}.md"
    md.write_text(body, encoding="utf-8")
    print(f"assembled: {md} ({len(body):,} chars · {act_count} acts · {len(TOMES)} tomes)")

    html = OUT_MD / f"{NAME}.html"
    r = subprocess.run(
        ["pandoc", str(md), "-s", "-o", str(html),
         "--metadata", f"title={TITLE}", "-V", "lang=en"],
        capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        print("pandoc failed:", (r.stderr or "")[:300])
        return
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"file://{html}", wait_until="networkidle", timeout=120000)
        page.pdf(path=str(OUT_DIR / f"{NAME}.pdf"), format="A4",
                 margin={"top": "20mm", "bottom": "20mm", "left": "20mm", "right": "20mm"})
        browser.close()
    html.unlink()
    size = (OUT_DIR / f"{NAME}.pdf").stat().st_size
    print(f"-> pdfs/city/{NAME}.pdf ({size/1024/1024:.1f} MB)")


if __name__ == "__main__":
    main()
