---
date: 2026-07-09
role: A1
wps: [WP-07, WP-04]
extractions: [E1, E2]
register_head: C96
ledger_entries: []
---

# A1 maintenance touch · E2 FEEDS hygiene (L081(c))

## Verdict

The L081(c) hygiene item is discharged. WP-07 added to the FEEDS lines of E2-C02, E2-C04 and E2-C12 in `extractions/E2-moving-ceiling.md`; all three consumptions verified as real against the WP-07 traceability appendix and frontmatter before editing. The reverse sweep found no gap: WP-04's rehydration consumes no E1 claim, so no E1 FEEDS line lacks WP-04 by consumption, and E1 was not edited. Checks 4/4 run non-vacuously on an explicit nine-file list; the sole FAIL is E1 `check_versions`, the standing L033 design tension, recorded and not fixed. No claim wording touched. Ledger entry proposed to A0 in the session report, not appended.

## Consumption verification (before editing)

Per the L031/L065(d) discipline, FEEDS lines record actual consumption, so each addition was verified against `rehydrations/academic/linear_cap_paper.md` first:

- **E2-C02** (R(t), t* definition): consumed at Remark 3.4 ("E2-c02 (R(t), t*)", trace map :428) and at ER-6 ("E2-c02 (t-index)", :445); named in frontmatter `extraction_basis`. Real.
- **E2-C04** (decoder-class family {D_t}): consumed at Remark 3.4 (sup-semantics caveat, "sup = first crossing under monotone decoder-class growth, added 2026-07-08 per L069(b)", :429); named in `extraction_basis` (the E2-c04 omission was amended by A0 at L081(b)). Real.
- **E2-C12** (multi-agent leakage, primary home E1): consumed at Thm 4.1 (imported) as a duplicate citation alongside E1-c09 ("E2-c12 dup", :450); named in `extraction_basis`. Real, with the duplicate character noted in the FEEDS parenthetical so no future reader takes it for an independent consumption.

All three were real; none of the report-instead-of-edit branch was needed.

## Edits made (FEEDS surfaces only)

1. E2-C02 FEEDS: `WP-01, WP-04, WP-02` to `WP-01, WP-04, WP-02, WP-07`.
2. E2-C04 FEEDS: `WP-04` to `WP-04, WP-07`.
3. E2-C12 FEEDS: `WP-04 (context), E1 (primary home)` to `WP-04 (context), WP-07 (Thm 4.1 import, duplicate citation alongside E1-C09), E1 (primary home)`.
4. Cluster header (same staleness class, adjacent one-line fix): the "Feeds ..." summary line did not name WP-07 although E2-C01 and E2-C11 have carried WP-07 feeds since build; `WP-07 (theory paper)` added after the WP-04 entry. Precedent: the header's WP-02 wording was updated in the L044 re-issue pass.
5. Frontmatter `resweep_note` extended and a sweep-record paragraph appended, both recording this touch.

Not touched: claim wording anywhere. The L074 E1-C10/E2-C12 descriptor re-issue waits on the first person's register-brief item (e) ruling and was deliberately left alone; the E2-C12 edit is confined to the FEEDS line.

## Reverse sweep (E1 vs WP-04)

`rehydrations/academic/moving_ceiling_sok.md` was swept for E1 consumption: zero matches for `E1` anywhere in the file; its `extraction_basis` reads "E2 claims C01-C05, C07-C15" and its claim trace is inline [E2-Cnn] markers only. Therefore no E1 claim is consumed by WP-04 and no E1 FEEDS line is missing WP-04. One adjacent observation, recorded not fixed: E1-C40's FEEDS names WP-04 as a "limitative/related-work shelf only" feed worded by the L065(d) ruling itself; the SoK body does not presently cite E1-C40. That line is ledger-worded routing ("at most"), not a consumption record, and changing it would second-guess L065(d); left as ruled, flagged in the report for A0's judgement.

## Checks

Four checks run from `checks/` with an explicit nine-file argv (the two extractions E1 and E2 plus all seven rehydration files), per the L082 vacuity correction; nine PASS/FAIL lines per check confirmed non-vacuous.

- check_tier_vocab: PASS x9, exit 0.
- check_figures_fence: PASS x9, exit 0.
- check_register_refs: PASS x9, exit 0 (E2 clean post-edit).
- check_versions: exit 1. Sole FAIL is `E1-amnesia-gap.md`, three findings (retired citation :42; static-ceiling without conditioning :119, :259). This is the standing L033 tension exactly (same three findings, line numbers drifted with file growth from :39/:116/:256); extractions quote canon faithfully and are gated on check_register_refs only until the register process rules. Recorded, not fixed. All eight other files PASS including E2.

## Reversals

None. One decision point worth the record: whether the E2-C12 "dup" citation at Thm 4.1 counts as actual consumption. Ruled yes, because the trace map cites it and the frontmatter `extraction_basis` names it; the FEEDS parenthetical carries the duplicate character so the line does not overstate.

## Handoff

- **WP-07:** no action from this touch; L081(c) discharged. WP-07 is awaiting-P4 (L082) and the runtime touches it no further.
- **WP-04:** single next action: A0 to judge whether E1-C40's shelf-only WP-04 feed should remain as L065(d) worded it given the SoK body does not cite it; no edit made here.
- **Open:** L033 (check_versions vs extractions) remains open; findings unchanged in kind, line numbers drifted.
- **Blocked:** L074 descriptor re-issue for E1-C10/E2-C12, waiting on the first person's register-brief item (e) ruling.
- **Ledger:** proposed entry in the A1 session report to A0 (not appended, per card).
