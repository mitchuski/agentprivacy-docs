---
name: overlay-sweep
description: Sweep ONE overlay dimension (proverbs, protocols, spells/emoji strings, or sci-fi concepts) across the V6 research directory, producing an evidence-anchored inventory in the poetic register. Use when the Loomkeeper runs an overlay cycle or refreshes a single dimension after new formal work lands.
scope: papers/ (agentprivacy-docs), read-only; writes to overlays/sweeps/
---

# overlay-sweep

One dimension, the whole corpus, every item anchored.

## Corpus (the sweep list)

- `papers/v6/*.md` — the canon (5 files)
- `papers/Programme/pipeline/rehydrations/**` — the eleven expressions
- `papers/Programme/pipeline/extractions/*.md` — the claim inventories
- `papers/Programme/pipeline/GROUND_RULES.md`, `SOURCES.md`
- `papers/Programme/pipeline/programme/*.md` — direction + brief
- `papers/Programme/pipeline/chronicles/` — at minimum the synthesis
  long read + the A0 cycle chronicles (grep-first for the rest)
- `papers/Programme/observers/*.md`
- `papers/Programme/pipeline/reviews/critiques_ledger.md` — grep-only
  (200KB; census by pattern, read hits in window)

## Item form (every entry, no exceptions)

```
### <the item, verbatim or named>
- source: <file>:<line> (+ further sightings)
- formal twin: <the theorem / rule / claim / station it compresses,
  with its identifier (C-number, GR-number, L-number, WP, E-claim)
  when one exists>
- reading: 1-3 sentences, poetic register welcome
- threads: [P|R|S|F cross-references to items in other dimensions,
  by name — guesses allowed, marked (?)]
- casts forward: the direction this item points, one sentence, or "-"
```

## Dimension notes

- **OV-P proverbs:** hunt one-breath laws: chronicle verdict lines,
  GR-8-class mottos, coda sentences, observer doctrine ("finds seams /
  decides stitches" class). The test: would it survive alone on a wall.
- **OV-R protocols:** named repeatables: intake protocols, ceremony
  types, ladder stations, review disciplines, RESERVED/successor-
  criterion forms. Name what each governs and what invokes it.
- **OV-S spells & emoji strings:** seals, glyph strings, operators.
  Note WHERE they are banned (GR-4/GR-5 fence) as data, not defect:
  absence in the formal layer is the fence working. Decode each string
  element-wise; ⊥ is the load-bearing case (orthogonality, separation
  of duties, Swordsman⊥Mage) — trace it both registers.
- **OV-F sci-fi concepts:** the speculative furniture: amnesia gap,
  moving ceiling, existence leak, uncarved date, the concepts inside
  titles and essay frames. For each: the formal core it dramatises and
  the research it CASTS (what experiment/paper/protocol it implies).

## Discipline

- GR-9 binds: no anchor, no entry.
- Amplify, never strengthen: the reading may sing; the formal twin
  line must state only what the source states.
- Output: `overlays/sweeps/OV-<X>_<dimension>.md`, frontmatter with
  date, dimension, corpus coverage statement (RS-05 clause: name what
  you swept and at what depth), item count.
