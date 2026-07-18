# NOTE · Fleet Tracker · runtime fleet result tracking artefact

Status: PLANNED 2026-07-03 (first-person directed at the close of the three-cycle day; build deferred to 2026-07-03+ by the first person). Nothing built yet.

## What it is

One readable page that answers "what did the fleet do and what needs me" without opening a dozen files. The audience is the first person at the start and end of a fleet day; the page's single job is to surface the decision queue and the state of every artifact at a glance, with the detail one click down. It is an instrument in the atlas sense: it displays pipeline state, it never owns it. The manifest stays the map, the ledger stays the memory; the tracker renders them.

## Architecture (recommended)

A small deterministic generator, not a live app:

- `pipeline/tools/fleet_tracker.py` (stdlib only, like the checks) reads four sources: `manifest.yaml`, `reviews/critiques_ledger.md`, `chronicles/*.md` frontmatter, `tasks/*.md` frontmatter.
- Emits `pipeline/FLEET_TRACKER.html`, fully self-contained (inline CSS, no external requests, so the same file works as a Claude Artifact, a local file, or later a gatehouse-gated page on the guide).
- GR-6 applies: the HTML is generated, never hand-edited; fix the generator or the sources.
- Rebuild moment: A0 runs it at every cycle close-out, same breath as the checks. Optionally a `--stamp` arg takes the datetime (generators should not mint their own timestamps if the artefact is diffed).
- Parsing contract: manifest lines are single-line YAML flow maps (parse with a small regex walker, not a YAML dep); ledger entries are `[Lnnn][SCOPE][TIER][DATE][ROLE]` headers with FINDING/EVIDENCE/PROPOSED/STATUS lines; chronicle frontmatter carries date/role/wps/ledger_entries. All three formats are already stable across L001-L055 and 20+ chronicles.

Alternative considered and parked: a live Next.js route on agentprivacy_master reading the repo. Wrong layer for now; the pipeline is a local workshop and its tracker should work air-gapped. Revisit if the pipeline itself ever publishes.

## Page structure (scanned, not read; summary before detail)

1. **Masthead**: register head · ledger head (L055) · last rebuild stamp · counts (sessions today, entries filed, checks green/red).
2. **Needs the First Person** (the top block, always): the decision queue derived from ledger entries with `STATUS: open(first-person...)` or `open(pending first-person...)` plus any WP at gate P3 (waiting on P4). Each item: one sentence, its L-number, the file it lives in. This block is the page's reason to exist.
3. **Artifact board**: one row per WP from the manifest: name · tier chip · status · gate as a five-stop track (P0-P4, filled to last-passed, P4 visually distinct because only the first person marks it) · due (hard deadlines flagged) · next actor · note. Sort: hard deadlines first, then gate-descending.
4. **Extraction shelf**: E1-E11 with status, claim counts, head-at-build, re-sweep flags.
5. **Cycle timeline**: one lane per cycle, sessions as blocks (role · wp · verdict word from the chronicle), the day's shape visible.
6. **Ledger tail**: last N entries, colour-striped by severity class (CANON-LEVEL / BLOCKING / P-tier / resolved), each linking to its ledger anchor.
7. **Checks matrix**: check × artifact grid from the latest A0 run (the generator can shell the four checks itself, or read a results file the close-out writes).

## Design plan (so the build starts warm)

Subject-grounded, not templated: the pipeline's own vocabulary is walls, gates, ledgers, lanterns; the tracker should read like the workshop's wall-board, not a SaaS dashboard.

- **Palette**: graphite ground `#1c2126`; panel `#252c33`; ledger-paper text `#e8e4d9`; lantern amber accent `#d99a3d` (used once per view: the needs-you block); semantic separately: gate-green `#5a9e6f`, blocked-red `#c25b4e`, pending-grey `#6b7680`. Neutrals biased warm toward the amber, not pure grey.
- **Type**: Fraunces (data-URI @font-face, italic for the masthead only) to match the agentprivacy identity; body/UI: system stack (Segoe UI/-apple-system); data: `ui-monospace` with `font-variant-numeric: tabular-nums` everywhere digits column up (gates, counts, L-numbers, dates).
- **Layout**: single column, max ~1100px; the needs-you block full-width at top in the amber treatment; board and shelf as tables inside `overflow-x: auto` containers; timeline as a horizontal flex of lanes. No hero, no emoji section markers, no rounded-card-with-accent-rail; chips and gate-tracks carry the state.
- **Motion**: none beyond hover states; this is a wall-board.

## Not in scope (recorded so it stays out)

Editing state from the page; live agent telemetry; publishing before the pipeline itself is committed to git; any canon content beyond titles and L-numbers (the tracker is internal tier; formal register; no canon vocabulary leaks).

## Build checklist for tomorrow

1. Write `tools/fleet_tracker.py`, parse the four sources, emit the seven blocks.
2. Run against today's real state (L055, 28 WPs, 11 extractions, 3 cycles) as the fixture; the day-of-three-cycles chronicle is the acceptance test: everything it names should be findable on the page.
3. A0 adds the rebuild to the close-out loop and notes it in the README's operations section.
4. Optional same-day: render once as a Claude Artifact to check the self-contained file stands alone.
