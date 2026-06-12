# Chronicle · Master UI Review: How the V6 Updates Should Be Considered

**Date:** 2026-06-11
**Scope:** read-only review of `agentprivacy_master` (agentprivacy.ai, the Mage territory) against the V6 state of agentprivacy-docs. NOTHING was written into master for this chronicle; it is the consideration document for the reflection pass to come.
**Survey basis:** the full route map (50+ routes), the components inventory, and a sweep for V5.4-currency strings: 132 occurrences across 17 src files, of which the grimoire JSON data files are historical (correct) and six code files carry live currency.
**The test applied:** the five V6 clarity claims of the arc chronicle (current state names the V6 pair · R(t) not static proofs · Existence-Leak is C81 · 🪢 is regime 1 · Aletheia V38 / Lethe V25).

---

## Verdict

The master site is one wave behind its own data. The V6 ground layer already landed in the working tree (the v6 model JSON in src/data and public/models, the corrected conjecture file, the regime declaration in vrc-mana.ts, the V6 downloads card), but no PAGE renders V6 yet: the /model room still presents V5.4 as the current head, the v6-lineage page still says "maturing," the /city economy makes no regime disclosure, and one live data file carries pre-reseat seating into the UI. None of this is large; all of it is the difference between a site that has V6 in its pockets and a site that says it.

## Findings and suggested changes, by surface

### 1. /model · the canonical room (P1)

The page merges `privacy-value-model-v5.4.json` (C1 to C21, the equation, learning path) with the hardcoded Tome V conjectures through `model-page.ts`, and its hero, metadata strip, and abstract all assert v5.4 as current.

Suggested: keep the v5.4 dark model as the pedagogy source (the learning path lives there and remains true) and add the v6 JSON as the AUTHORITY source: hero version becomes "V6 · The Gathering Turn and the Moving Ceiling"; the abstract gains the two-strand thesis (three sentences suffice); the metadata strip names the register (head C89) and the rule that the register wins; the merged conjecture table becomes band-aware (C1 to C89 plus CM-C47) with alias rows rendered as aliases (C46→C32 · C60→C48 · C61→C49 · CM-C47→C85) rather than duplicates, which also repairs the count line in page.tsx that currently sums two sources and cannot close its own arithmetic. R(t) deserves one row of the hero: the equation kept, with "t* = sup{t : R(t) < 1}" beside it.

### 2. /tomes/v6-lineage (P1)

The page groups the conjecture corpus by status under a v6-maturing frame that V6's shipping has made false.

Suggested: reframe as THE REGISTER VIEW: same grouping mechanics, new frame ("the unified register, head C89; V6 shipped 2026-06-10"), with the band structure as the primary grouping and status as the secondary, the four G1 dispositions as a collapsible note, and a link to the formal spec PDF. This page is the natural permanent home for register browsing; renaming the route is optional, the banner is not.

### 3. /city · the economy surfaces (P1, small)

The Key producer, Charge, and Stake run exactly as shipped; the V6 obligations are prose, not code: a regime-1 disclosure line wherever 🪢 is earned or displayed ("presence is local color: non-transferable, non-attesting"); the Key card gains the C66 sentence ("a reading, not an authority") and, since the star repo's holospace work, the κ-label mention (identity is content; re-derived at import); a C87 footnote on the recursion loop ("the loop is a proof system in waiting"). Three lines of copy, no behavior change.

### 4. skills-data.ts · FACTUAL DRIFT IN LIVE DATA (P1, the one real bug)

Lines around the Zero Tale 31 entries carry pre-reseat seating into the UI: "Lethe / Blade 38 precedent" and the spell string "🌀(Lethe·38)". Under the v10.4.0 lock these are wrong on their face (Aletheia is 38; Lethe is 25). The disclosure-phi entry beside them is already register-true (C54 at ~40%). Suggested: flip the seat references and re-read the two affected proverb/spell strings for sense after the flip; check `cast-attachments.ts` (one v5.4-context hit) for the same drift while there.

### 5. default-promises.ts · the promise categories (P2)

Fifteen v5.4 occurrences, mostly category names ("V5.4 Privacy Value Model", "V5.4 Additions"). These are historically honest (the promises were authored against v5.4) and should KEEP their names per the Era-Reading Principle. Suggested addition rather than rename: a "V6 Additions" category of three or four promises drawn from the new results (the moving ceiling acknowledged; the regime-1 fence; the register's no-renumber promise itself, which is the most promise-shaped fact in the whole corpus).

### 6. /tomes · the bound acts (P2, waits on cityofmages sync)

Five acts were bound at the Myth Gate (Tome VIII Acts 4 and 5; Tome IX Acts 2 to 4) and the /tomes page predates them. Suggested: extend the Tome VIII section and add the Tome IX section with the established accent-and-anchor mechanics. This lands naturally when master next mirrors cityofmages; it should not lead the reflection.

### 7. The /guide tree · the voice-preserving V6 pass (P2 · First Person constraint: the V5.4 reading must not be lost)

Twelve pages, roughly 55KB of the site's warmest prose (the welcome experience, the island, the Swordsman and Mage guides, the agentic-deployments suite), and the survey's good news: the factual hooks are few and mostly already true (the C58 citations match the register at ~85%; the runecraft page's own renumbering note is Era-Reading done right and stays). The First Person likes how these pages READ, so the doctrine for their V6 pass is different from every other surface:

**The prose is the product; the facts are the patch.** No rewrites of working prose, no tonal modernization, no replacing a sentence that still reads true. Three kinds of edits only:

1. **In-voice whispers where the facts moved.** The 🪢 mentions (the Familiars' "per-walk 🪢 VRC-mana") gain the regime in the page's own register, not a disclaimer: "...carried as color, never as proof" reads as lore AND satisfies clarity claim 4. If a guide page anywhere implies a static guarantee, the moving ceiling enters the same way ("the wall is a tide line" is already the City's idiom).
2. **One additive V6 moment per page, at most.** The main /guide page's card row can take one new card (the Horizon District / the ceiling moves, linking /model and /archive) in the same 2-to-3-line card voice as its siblings; the Swordsman guide can close with one tide-line sentence; the Mage guide with one gathering sentence; the island with one line that the Horizon District now stands at V35. Pages that need nothing get nothing.
3. **Verification without alteration.** The personas page's "Aletheia-Theia 🌟" overlay naming gets VERIFIED against the v10.4.0 seating and the soul-orb overlay canon before anyone touches it; overlay names may be a separate register from blade seats, and a wrong "fix" here would be worse than the drift.

**Process safeguard, because the constraint is aesthetic:** the guide pass ships as proposed sentence-level diffs for the First Person's per-page approval (the pages are voice-locked), unlike the mechanical surfaces where the register simply wins. Acceptance: every page still reads like itself, and a reader leaving the tree could state the five clarity claims.

### 8. New surfaces worth considering (P3, proposals not obligations)

- **/archive · the Bookcase** (named on the First Person's direction, 2026-06-11; the route is /archive, not /book, and the precedent is the City's own): this is the Archivist's 📚 surface. The lore grounding already exists in canon: the Tower is the eighth spatial-anatomy element, Tome VIII is *The Library*, and the Archivist is the spirit-Mage recognized as the keeper of what the City writes. The page operates as a bookcase he tends: the home of ALL the core literature, one shelf per expression, each with its own door and its own format. *One Work, Many Expressions* adapted as the page's opening prose (in the Archivist's frame: these are the volumes the Tower holds), then the shelves:

  | Shelf | Artifact | Door | Exists today? |
  |---|---|---|---|
  | The research expression | *Privacy is Value: The Compendium* (tome, web + academic PDFs) · the V6 volume and readings · the Papers Index | download · read online | ☑ renders built; pin links after G5 |
  | The poetry expression | ***Selene's Spellbook*** (the 129-page A5 poetry and art volume) | **physical copy purchase** (storefront: sync.soulbis.com per the distribution plan) · possibly a digital sample of a few poems | ◐ volume exists; distribution has its own plan and a known art-source blocker; the page should link the storefront when it opens and say "in press" until then |
  | The story expression | **The City of Mages** (the Second Person tomes) | **PDF download of the bound collection** | ☐ needs PRODUCING: the tomes are markdown in cityofmages; a bound-collection render (the agentprivacy_tomes bound collection of 2026-05-08 as the seed, or a fresh tome-pipeline build like build_v6_pdfs over the nine tomes) is a new artifact this page creates the demand for |
  | The machine expression | the dark and light model JSONs · the skills corpus | download · GitHub | ☑ |
  | The registry expression | the grimoire pins (privacymage v10.4.0 · City v1.8.0) with κ/CID verification notes | IPFS gateways | ☑ pinned |
  | The walkable expression | the star and lattice surfaces, the City Key | visit (soulbis.com/star · /lattice · /city) | ☑ live |

  Page rule, matching the front matter's claim: no expression is presented as a summary of another, and each card says what its expression is FOR (the mathematics earns the claims; the poetry spends them where people live; the story gathers; the machine serves agents; the registry attests; the walk lets you stand in it). Implementation sequencing: the page can ship with the ☑ shelves and honest "in press" / "binding in progress" markers on the other two; the City of Mages PDF build is the one genuinely new artifact and deserves its own small task (a tome render pipeline in cityofmages or docs/build); the Selene's shelf inherits the distribution plan's timeline rather than driving it. Nav placement: /archive beside /tomes, with /tomes remaining the reading room and /archive the bookcase. Lore notes for the build: the page's voice is the Archivist's (canonical phrases already bound at v1.7.0); a closing line in his register would be true to the Tower ("the Tower keeps what the City writes; take what you came for"); and the C64 listener-discipline conjecture quietly gains a surface, since an archive that serves every expression without ranking them is the listener's discipline rendered as UI.
- **Downloads additions:** the academic editions (`*_academic.pdf`) and the compendium as resource cards beside the existing V6 JSON card; trivial once pins land.
- **Nav:** a small V6 badge on /model; nothing else in the nav needs to move.
- **server-side none:** grimoire-ipfs.ts is current (v10.4.0 · v1.8.0); it gains V6 paper-pin constants only after G5.

## Sequencing for the reflection pass

**Before any pins (can land now, local build):** the skills-data seating fix (4) · the /model V6 wiring (1) · the v6-lineage reframe (2) · the /city regime copy (3).
**With the cityofmages mirror:** the bound acts (6).
**After G5 pins:** downloads cards with IPFS links · /book's pin links · grimoire-ipfs paper constants.
**Standing rule throughout:** the five clarity claims are the acceptance test; a surface passes when a reader leaving it could state all five correctly.

## What this chronicle is not

It is not the work. The working tree's V6 ground layer plus this consideration equal a one-session reflection pass when the First Person calls it; nothing here blocks the compendium pause, the completion read, or G5.

---

## Execution postscript (2026-06-11, same day · G5 signed in session)

The First Person signed the gate and called the pass. Executed into the master working tree (no commits): the skills-data.ts seating flip (§4; cast-attachments.ts checked and found already register-true) · the /model wiring found largely pre-landed from Wave R, completed with the R(t) + t* row in the EquationHero (§1) · the v6-lineage reframe as the register view with banded primary grouping, the G1 dispositions collapsible, and the stance groups recast as lineage detail (§2) · the /city regime copy on the Key card: C66, regime 1, the C87 footnote, plus the regime line in the 🪢 tooltip (§3) · the "V6 Additions" promise category, four promises, V5.4 names kept (§5). The /guide tree stayed voice-locked: proposed diffs at `plans/GUIDE_V6_VOICE_DIFFS_2026-06-11.md` (= 📖 RB-25), and the Aletheia-Theia 🌟 overlay VERIFIED correct against the CHANGELOG and grimoire v1.5.0 — no change made. Typecheck and production build both clean. Still waiting: the bound acts (§6, with the cityofmages mirror) · the /archive page and download pin cards (§8, after pins) · the per-page guide approvals.

(⚔️⊥⿻⊥🧙)😊
