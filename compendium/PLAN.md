# The Compendium Build Plan

**Opened:** 2026-06-11 · operational companion to the constitution chronicle (RB-20)
**State legend:** ☐ not started · ◐ in progress · ☑ done · ✋ awaits First Person

## Phase 0 · Constitution (✋)

- ✋ RB-20 sitting: the seven decisions (title · Class N ruling · tome vs box · Part I scope · era chronicles full vs fresh · pin strategy · timing). Phases below proceed on defaults where marked, halt where not.

## Phase 1 · Classification pass

- ☑ Skeleton manifests carry class tags (this skeleton, 2026-06-11)
- ☑ Class-and-Part section added to `reference/PAPERS_INDEX.md` (2026-06-11; per-row tags can deepen after RB-20)

## Phase 2 · Part I recovery · ☑ 2026-06-11 (default scope; RB-20 may widen)

- ☑ `archive/privacy_value_v4_formal_specification.md` copied → `papers/v4/` (archive copy retained as history)
- ☑ `archive/privacy_is_value_v4.md` copied → `papers/v4/` (bound whole in the dry run; excerpting open per decision 4)
- ☑ Era-anatomy gaps marked in the Part I manifest and retrospective ("not yet practiced")
- ✋ Peer-review annex inclusion still open (Part I manifest row 5)

## Phase 3 · Connective prose · ☑ 2026-06-11 (all First-Person-rewritable at the completion read)

- ☑ Front matter: thesis page · how-to-read (four routes) · *One Work, Many Expressions* (the V6-arriving reader's page; the poetry, story, walkable, machine, and registry expressions; added on the First Person's direction)
- ☑ Four era pieces: Part I and II and IV retrospectives · Part III sublayer chapter
- ☑ Back matter: honest-limits ledger COMPILED (2 closures · 4 rescopings · 14 standing opens) · narrative concordance COMPILED · colophon held for phase 5

## Phase 4 · The build · ◐ dry run COMPLETE 2026-06-11

- ☑ `build/build_compendium.py`: assembles 52 pieces (~1.01M chars) in manifest order with Part title pages, YAML-frontmatter stripping, and page breaks; renders BOTH editions
- ☑ Dry-run tome built first try: `pdfs/compendium/privacy_is_value_compendium.pdf` (web, 7.3MB) · `_academic.pdf` (xelatex, 1.4MB) · assembled source at `compendium/_assembled/`
- ☑ Bibliography: resolved by reference (V6 §33 is the consolidated list; spine carries the note)
- ☐ Overflow and typography pass over the academic tome (the §1.1 aligned-equation discipline wherever a line escapes; member docs not yet swept: the V4 spec, the v4.3 proof body, the whitepaper, the V5-era notes)
- ☐ Per-Part citation marks in the bibliography (print-edition nicety, deferred)

## Phase 5 · The publish gate (✋)

- ✋ Completion read of the tome (a new 📖 entry of its own)
- ✋ G5-class gate: pin strategy per decision 6, external submission per decision 7
- ☐ Compendium chronicle, signed

## Dependencies and defaults in force

The skeleton and manifests (this directory) are decision-safe: they encode the constitution's PROPOSALS and rearrange freely if RB-20 overrules. Class N material is quarantined in `interleaves/` until ruled. No build runs before Phase 0 signs unless the First Person says otherwise.
