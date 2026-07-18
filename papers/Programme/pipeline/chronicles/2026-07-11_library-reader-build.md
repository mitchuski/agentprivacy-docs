---
date: 2026-07-11
role: A0 (instrument build at the first person's request, between cycles 13 and 14)
wps: []
extractions: []
register_head: C96
ledger_entries: []
companions: [2026-07-10_the-twelve-cycles.md, 2026-07-03_fleet-tracker-build.md]
---

# A0 session · the library reader: every programme document, one page each, one index

## Verdict

Built and serving. `tools/build_library.py` (stdlib only, on the
fleet-tracker precedent) renders all 229 programme documents to
individual HTML pages under `reader/docs/` and generates a wiki-style
`reader/index.html`: canon V6 papers (read-only upstream), the eleven
rehydrations with status chips drawn from their own frontmatter, the
extractions, the reviews and the critiques ledger, the programme notes
and deadlines, ninety-odd chronicles folded by date, the observer
intake docs, and the machinery (ground rules, manifest, roles, tasks,
templates). A live filter box searches title, path and status. The
twelve-cycles long read sits at the top as the catch-up entry point.
One server serves both surfaces at localhost:7474; because the output
directory is shared with the cycle reader, rebuilds appear without a
restart.

## Design decisions

- GR-6 throughout: the reader is generated, never hand-edited; the
  rebuild is one command (`python tools/build_library.py`); fixing a
  page means fixing its source document.
- Status chips truncate at the first clause: several frontmatter
  status fields are paragraph-length audit trails, which is correct
  for the file and wrong for an index.
- The observer documents appear in the library because this is the
  first person's own private reading surface. The D2 rule (observer
  material surfaces through chronicles only) governs what enters the
  papers, not what the first person may read.
- Markdown links to `.md` targets rewrite to their rendered pages; in
  practice the corpus references paths in backticks, so the index is
  the navigation surface, by observation rather than by design.

## Purpose (the first person's framing)

A local private space to read the whole programme and prompt back into
the runtime per document as magnification grows on each research
expression. The reading loop: the runtime writes, the library renders,
the first person reads at :7474 and returns rulings or magnification
requests, the next cycle carries them.

## Handoff

- **A0 (standing):** close-out now regenerates BOTH readers alongside
  the tracker (`build_library.py`, `build_cycle_reader.py`,
  `fleet_tracker.py`).
- **First person:** the index is at http://localhost:7474/ while the
  session server runs; the rebuild-and-serve command is
  `python tools/build_library.py --serve` from the pipeline directory.
