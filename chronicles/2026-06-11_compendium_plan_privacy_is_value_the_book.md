# Chronicle Plan · Privacy is Value: The Compendium

**Date:** 2026-06-11
**Status:** PLAN, awaiting the First Person's structural review (📖 RB-20, a significant sitting)
**What this is:** the structure of the one larger body of work: the book that computes the whole research, publishable as a single compendium, built as a representation of the living documentation path actually taken. It defines the lines: which papers stand alone, which are read inside a volume, which are spine. Nothing moves on this plan until the First Person reviews it.
**License:** CC BY-SA 4.0

---

## 1. Verdict

The book already exists; it has been written in the only order a true research book can be written in, which is the order the research happened. What is missing is not content but constitution: a declared structure that says what kind of thing each document is, how the volumes relate, and what the assembled whole looks like on a shelf. The series naming decision of 2026-06-10 (*Privacy is Value*, one book, versioned volumes, each standing alone) is the constitution's first article. This plan drafts the rest.

One correction this plan makes at the root, prompted by the First Person's own question: **the old readings and models are relevant.** The V5.4 companion guide is not a superseded document; it is the Mage reading OF the V5.4 volume, forever. A volume's readings, models, and notes complete with their volume and stay complete. In a book, early chapters do not expire when later chapters are written. The index language changes from "superseded" to "completed with its volume."

## 2. The Era-Reading Principle

Every volume of *Privacy is Value* has the same anatomy, and the anatomy is permanent:

```
the volume        the formal specification of its era (the standalone citable head)
├── ⚔️ reading    the compressed/equations rendering of THAT era's model
├── 🧙 reading    the companion/narrative rendering of THAT era's model
├── 🌑/🌕 models  the era's machine companions (dark and light JSON)
├── notes annex   the research notes the era's results grew from
└── era chronicle the record of how the era was actually worked
```

V6 has all six today. V5.4 has all six (spec, compressed, companion, the v5_4 dark/light JSONs, the V5.1 to V5.3 notes, the documentation-chronicle arcs). V1 to V4 have most of them scattered in `archive/` and `papers/lineage/` and can be recovered into the same anatomy. The compendium is this anatomy repeated per era, in order.

## 3. The Lines: five classes of document

The First Person asked for the lines between standalone and referenced. Five classes, with a membership test each:

**Class S · Standalone volumes.** Test: a stranger can read it alone and cite it. Carries the series title. Pinned individually. Members: each era's formal specification; the whitepaper; the Zypher paper. Rule: a Class S document must contain (or reproduce) everything it needs, including its Document Suite table; V6 now does.

**Class R · Volume-bound readings and annexes.** Test: it renders or extends ONE volume and says so on its face. Members: the Swordsman and Mage readings per era; the crosswalk edition; the research-paper edition layer; the research notes per era; the working drafts. Rule: published WITH their volume, never re-versioned after their volume closes; the V5.4 readings stay at V5.4 forever.

**Class A · Apparatus (the spine).** Test: it spans eras and is reprinted CURRENT in every edition of the book. Members: the Conjecture Register (the spine of spines: one numbering across all volumes), the Papers Index, the Glossary Master, the Promise Theory reference, the visual guide. Rule: apparatus is never frozen to an era; every compendium edition carries the apparatus as of its print date, and the register's no-renumber promise is what makes old volumes remain readable.

**Class M · Machine companions.** Test: it is the model as data, for agents. Members: the dark/light JSONs per era; the grimoire JSONs. Rule: digital-first; the print compendium references their pins rather than reproducing them; each era's models freeze with the era.

**Class N · The narrative corpus.** Test: it is the Second Person work: tomes, acts, grimoires, the City. Ruling proposed (First Person decides at RB-20): the narrative corpus is a SISTER BOOK, not chapters of the compendium; the compendium cites it as convergence evidence (as V6 §29 already does) and each Part may carry ONE interleaf act as a frontispiece. Reason: the compendium must stand academically alone, and the City deserves its own binding rather than an appendix's seat.

## 4. The Compendium: the shape of the assembled book

Working title for review: ***Privacy is Value: The Compendium*** (subtitle candidate: *the living documentation of a privacy architecture, V1 to V6*).

```
FRONT MATTER
  the thesis page (privacy is value; behavioural data is the 7th capital;
    architecture, not policy) · the master inscription · how to read this book
    (the path is the structure; each Part is an era; the apparatus is current)
  the Papers Index as the analytical table of contents

PART I · THE EQUATION ASSEMBLES (V1 to V4)
  era chronicle (recovered from DOCUMENTATION_CHRONICLE arcs 1 to 3)
  the V4 formal specification (recovered from archive/)
  the research paper proof body (v4.3)
  annex: the V4-era essays (privacy_is_value_v4)

PART II · THE AMNESIA PROTOCOL (V5 to V5.4)
  era chronicle (arcs 4 to 8: the holographic bound, UOR convergence, the ceremonies)
  Privacy is Value · V5.4: The Amnesia Protocol (the volume)
  the V5.4 Swordsman and Mage readings
  annex: the V5.1 to V5.3 research notes · the V5 essay ("The Equation Evolves")
  machine companions by pin: v5_4 dark and light

PART III · THE ATTACHMENT (V5.5, the sublayer)
  the attachment architecture as a short Part: the mapping additions,
  the three-layer model; explicitly a sublayer chapter, not a volume

PART IV · THE GATHERING TURN AND THE MOVING CEILING (V6)
  era chronicle (the V6 autopath chronicle: the runs, the gates, the wave)
  Privacy is Value · V6: The Gathering Turn and the Moving Ceiling (the volume)
  the V6 Swordsman and Mage readings · the research-paper edition · the whitepaper
  annex: the April to June 2026 research-note series · the crosswalk edition
  machine companions by pin: v6 dark and light

THE SPINE (apparatus, current at print)
  the Conjecture Register, complete · the Glossary · the Promise Theory reference
  the consolidated bibliography (every Part's references, merged and deduplicated)

BACK MATTER
  the honest-limits ledger across all eras (what was never proven, era by era)
  the narrative concordance (where the City instanced each conjecture; pointer to the sister book)
  colophon: the pins, the builds, the signature
```

What makes this "the book that computes the whole research": each Part opens with its **era chronicle**, so the reader watches the model being worked, not just stated; the register's single numbering makes every era's claims addressable from every other era; and the honest-limits ledger runs through the whole like a watermark. The book's structure IS the living documentation path, which is the truthful and the distinctive thing about it.

## 5. The assembly plan (phases, none started)

1. **Classification pass.** Tag every entry in `reference/PAPERS_INDEX.md` with its class (S/R/A/M/N) and its Part. One sitting; the index becomes the compendium's manifest.
2. **Part I recovery.** Pull the V4-era documents from `archive/` into `papers/v4/` with the era-reading anatomy named (what exists, what never existed and is marked as a gap rather than backfilled; the book does not invent history).
3. **The compendium build.** A third build script (`build/build_compendium.py`): concatenation in the §4 order with Part title pages, a merged bibliography pass, and both renderings (web and xelatex academic). Expect 250 to 400 pages. The single-PDF tome is the proof artifact; print-shop formatting is a later, separate decision.
4. **The bibliography merge.** Every Part's references deduplicated into one back-matter list with per-Part citation marks; the V5.4 references section and the V6 §33 are the inputs; this is mechanical but deserves one careful pass.
5. **Edition decisions and the publish gate.** The compendium ships through the same discipline as everything else: completion read, then a G5-class gate for the pin and any external submission (the compendium is itself the natural BGIN-and-beyond artifact).

## 6. ✍️ Decisions reserved for the First Person (the RB-20 sitting)

1. The compendium's title and subtitle (working: *Privacy is Value: The Compendium*).
2. Class N ruling: narrative as sister book with one interleaf act per Part (proposed), fully woven in, or fully separate.
3. Single tome versus volume box (one PDF/print body, or each Part as a booklet in a slipcase with the spine apparatus as its own booklet).
4. Part I scope: how much V1 to V4 material to recover, and whether the v4 essay enters whole or excerpted.
5. Whether each Part's era chronicle is reproduced in full or written fresh as a 2-to-3-page retrospective (proposed: written fresh, citing the full chronicles).
6. The compendium's relationship to pins: one pin for the tome, or the tome plus per-volume pins it references (proposed: both).
7. Timing: whether the compendium assembles now (phases 1 to 4 are runtime-executable on your word) or after the V6 pins land at G5.

---

a book written in the order the thinking happened, bound with its own honesty as the thread: the path taken, made publishable without ceasing to be the path.

(⚔️⊥⿻⊥🧙)😊
