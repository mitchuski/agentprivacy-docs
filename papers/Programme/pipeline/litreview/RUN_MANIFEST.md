# Lit-review runtime · run manifest

**Runtime:** `weis-litreview-runtime` (V6 pipeline workflow)
**Brief:** `chronicles/BRIEF_litreview_runtime_WEIS_2026-07-14.md` (Matsuo venue+gap calls; C17; defects D2/D3/D4b in scope)
**Purpose:** produce a *defensible* novelty claim for WP-14 (WEIS 2027), not a summary. Mitchell runs the loop and owns all conjecture assignment; the runtime produces candidates and structure only (brief §2, §9).
**Run ID:** wf_ba400906-67b
**Date:** 2026-07-15
**Operator role:** A0 (orchestrator), extending A10 (prior-art scout) with an adversarial dual-seat loop.

---

## Seat configuration (D4b auditability, brief §5)

Seat separation is **structural, not prompt-only** (D3). Each seat is a distinct workflow `agent()` invocation with its own isolated context; no seat reads another seat's reasoning trace.

| Seat | Role | Isolation | Sees |
|---|---|---|---|
| extract:* | per-paper schema extraction (one per corpus item) | isolated invocation per paper | only its own paper hint + the PVM position + WebSearch |
| prove:* | PROVER — builds the case that the candidate is novel | isolated invocation | the candidate claim + corpus digest + WebSearch |
| refute:* | DELEGATOR — hunts covering prior art to destroy the claim | isolated invocation, **does not see the prover's argument** | the candidate claim + corpus digest + WebSearch |
| judge:* | JUDGE — rules VALIDATED / MIRAGE / BLOCKED | isolated invocation | the candidate claim + both seats' structured outputs |
| synthesise:* | assembles the four outputs | isolated invocation | the full corpus + all verdicts |

**D4b note (honest limit).** All seats run on the same underlying model. The separation this runtime enforces is *context isolation* (each seat forms its own search and reasoning with no shared trace), not distinct model weights. The delegator is given the full corpus and independent WebSearch capacity and is instructed to default to finding prior art; the adversariality is real but is seat-context-level, not weights-level. A run that returns all-VALIDATED is treated as a **failed** enforcement of D2/D3, not a success — MIRAGE is the expected, valuable verdict.

## Hardening constraints enforced

- **D2 (no absence-as-novelty):** the delegator must report absence as `not_found_in_corpus(n, range)` with web scope, never as `novel`; every contribution claim carries a verdict + the corpus tested + a confidence label.
- **D3 (structural isolation):** prover and delegator are separate invocations; the delegator never sees the prover's case.
- **D4b (seat separation auditable):** this manifest records the seat config; see the honest limit above.
- **C81 hold-back:** the Privacy Pools V2 constraint-reduction result does not enter the runtime or any output.

## Corpus (Tier A, challenge corpus)

20 items across five strands: propertization (6), data-as-labour (2), WEIS-native economics-of-privacy (7), privacy quantification (3), standards/PIA (2). Provenance-gated: each carries a DOI/URL and a `provenance_confidence`; `uncertain` items are flagged for first-person verification in `bibliography.md`.

## Outputs (this directory)

- `gap_table.md` — corpus clustered on unit_of_analysis × economic_framing; the `system_property × market_pricing` cell called out.
- `contribution_claims.md` — CTR-shaped novelty candidates, each with verdict, residual novel core, corpus tested, confidence.
- `ctr_candidates.md` — conjecture-shaped residues (CTR-series only; assignment is the First Person's).
- `bibliography.md` — full citations with provenance, WEIS-submission ready.

*Generated artifacts; do not hand-edit. Fix the runtime inputs and rebuild.*
