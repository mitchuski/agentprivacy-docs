---
date: 2026-07-09
role: A3
wps: [WP-04]
extractions: []
register_head: C96
ledger_entries: []
---

# A3 · WP-04 pre-review fixes · legs (b) and (c) of L085

**Verdict.** Both legs of the task card landed in `rehydrations/academic/moving_ceiling_sok.md`, five edits total, nothing else touched. Leg (b): the stale two-unresolved-works framing narrowed to one unresolved work at all four sites (Section 2, Section 5.1, Section 8, References closing note); the MDPI Telecom item is now stated as resolved at its primary record (Kagai, Branch, But and Allen 2025, existing key `kagai2025harvest`), with its engagement explicitly reserved for the pre-submission literature pass (the L062(d) sweep), deciding nothing. Leg (c): Proposition 1's Attribution paragraph no longer cites Csiszár-Körner 1978 for a collusion-failure result the source does not state; the citation is kept for the lineage it does show (broadcast channels with confidential messages as the wiretap family's general single-eavesdropper form), and the failure of the summed bound under collusion is stated as elementary, anchored to the proof's own interaction identity and to Section 8's assumption-failure paragraph. Zero new citation keys. Four checks run non-vacuously with the explicit file list, exit 0 x4. Ledger entry proposed in the report to A0, not appended.

## Path

1. Boot per CLAUDE.md: GROUND_RULES, role card, task card, L085 (plus L062, L070, L082 for the finding lineage), the A4 verification note section 3 on `tasks/WP-04_A4.md`, and the five target passages of the draft.
2. Precedent read before wording: the WP-07 L079 fix in `linear_cap_paper.md` (Section 2 restatement and ER-1), where `csiszar1978broadcast` was re-anchored to the broadcast-with-confidential-messages lineage and superadditivity under collusion was stated as elementary with in-paper anchors. The SoK fix reuses that exact pattern, mapped to the SoK's own apparatus (the interaction identity in Proposition 1(a)'s proof; the Section 8 assumption-failure paragraph).
3. Leg (b) executed as factual narrowing only. Each of the four sites now says: one work resolved since the sweep and not yet engaged, one work still bibliographically unresolved and excluded from citation. The Section 8 threat sentence keeps the N7 fence's substance with both items still disclosed as referee risks and the narrowing-versus-N1-standing logic intact, reworded from "if either work resolves to" to "if either work proves on engagement to be", since resolution has occurred for one of them.
4. Leg (c) executed as one sentence-level restatement inside the Attribution paragraph; the proof, the proposition statement, and the precision note around it are untouched.

## Deliberations and reversals

- **Considered and declined: promoting Kagai et al. to a cited reference entry.** The key exists in pv_v6.bib, so a full References entry plus in-text citation was mechanically available. Declined: citing the work in the verified reference list would pre-empt the engagement decision that L085 and the task card explicitly reserve for the L062(d) referee-grade sweep. The chosen form records the resolution in the References closing note (with the existing bib key, so zero new keys) and names the work in prose at Sections 2 and 5.1 with a pointer to that note; the work remains outside the cited registry list.
- **Considered and declined: dropping Csiszár-Körner from the Attribution paragraph entirely.** The source genuinely belongs to the lineage the paragraph attributes part (a) to, and the paper's introduction already carries it as wiretap lineage; deletion would have weakened accurate attribution to fix an inaccurate one. The kept clause states only what the source shows.
- **Concurrency note.** The task card flagged a possible concurrent A4 seat on Section 5.2 and the References (Mosca-Piani retarget). Section 5.2 was not touched. No collision was observed at the References closing note; the edit applied cleanly against the file's current state.

## Checks

All four checks in `checks/` run WITH THE EXPLICIT FILE LIST (L082 discipline) over the draft, the task card, and this chronicle: `check_register_refs.py`, `check_tier_vocab.py`, `check_figures_fence.py`, `check_versions.py`. Results recorded in the session report; exit 0 x4, non-vacuous.

## Handoff

- **WP-04, single next action:** the A4 Mosca-Piani retarget (L085(a), sanctioned separately) is the remaining pre-P1 leg; on its landing, A5-pc seats with the A4 verification note on top, per L085(d).
- **Open question, not blocking:** whether the L062(d) sweep engages Kagai et al. substantively or records it as resolved-and-orthogonal; the draft's wording accommodates either outcome without further edits to these four sites.
- **Ledger:** proposed entry (L0nn) in the report to A0; nothing appended this session.
