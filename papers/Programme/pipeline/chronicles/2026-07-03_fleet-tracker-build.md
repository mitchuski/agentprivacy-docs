---
date: 2026-07-03
role: A0 (tooling session, first-person directed; executes the fleet-tracker note of 2026-07-03)
wps: []
extractions: []
register_head: C96
ledger_entries: []
---

# A0 session · fleet tracker built and serving

## Verdict

The tracker planned in `programme/NOTE_FLEET_TRACKER_2026-07-03.md` is built and running. `tools/fleet_tracker.py` (stdlib only, per the note's architecture) reads the four sources — manifest, ledger, chronicle frontmatter, task frontmatter — plus every other pipeline document, and emits `tracker/`: a self-contained wall-board at `index.html` and a rendered reader page for all 93 documents, canon linked read-only. Serving at `http://localhost:7272` via `--serve`. The acceptance test named in the note passes: everything the day-of-three-cycles chronicle names is findable on the page — the six-item first-person queue (L011(g), L025, L044, L047, L048, WP-01's P4 read), the 28-WP artifact board with gate tracks, E1 at 40 claims and E2 at 15 on the extraction shelf, the C96/L055 masthead, the two-day session timeline, and the checks matrix.

## Path

Built to the note's page structure (masthead → needs-the-first-person → artifact board → extraction shelf → session timeline → ledger tail → checks → document shelf) and its design plan (graphite ground, lantern amber reserved for the needs-you block, tabular numerals, no motion). One deliberate extension at first-person direction: the document shelf renders *every* pipeline file as a human-readable page in a paper register — the reading surface for reviewing fleet output before anything transfers onward — since the session's purpose widened from "tracker" to "agent-tracking and human-readable view of all documents created". The generator takes `--root`, so any future auto-research programme with the same manifest/ledger/chronicles/tasks shape gets the same board unchanged.

The checks matrix shells the four checks per drafted artifact. It reports one FAIL: E1 against `check_versions`, which is the known L024-family tension (extractions fail the versions check precisely because they quote the canon faithfully), left visible rather than suppressed — the board renders state, it does not adjudicate it.

One parser defect found and fixed in-session: the manifest flow-map splitter did not treat parentheses as nesting, so a comma inside a note's parenthetical truncated WP-01's entry and dropped its "pending P4 read" flag from the queue. Fixed; the queue went from five items to the correct six. This is why the acceptance test was run against real state rather than a fixture.

## Reversals

- Fraunces is named first in the font stack but not embedded as a data-URI: embedding would balloon all 94 generated files for a masthead-only face. If the identity face matters on this surface, embed it in the generator later; the fallback (Georgia italic) holds the register meanwhile.
- The served build initially overwrote the index without the checks matrix (`--serve --no-checks`); regenerated with checks on. Operational lesson recorded: the close-out rebuild should run checks by default, and `--no-checks` is for fast iteration only.

## Handoff

- **First person:** the queue is on the board. Answers to the standing directional questions (L047/L048 diff approvals, WP-01 P4 read and the L025 wording call, L011(g) verification, L001/L002 disposition, and the suite-coherence pass ordering) form the next prompt; on those answers A0 cuts the next cycle's task cards.
- **A0 (next cycle):** rerun `python tools/fleet_tracker.py` at every close-out, same breath as the checks; README operations section now says so.
- **Future:** the approval → wiki-transfer flow the first person intends will sit downstream of the tracker's reader pages; nothing in the generator presumes it.
