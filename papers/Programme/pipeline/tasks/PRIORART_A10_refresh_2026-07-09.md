---
role: A10
runtime: fable
branch: none (convention suspended)
gate_target: prior_art rows reconciled with A4-verified metadata (L093(b))
due: 2026-07-09
---

# Task card · WP-04 prior-art row refresh · role A10 (Prior-Art Scout)

**Objective:** `reviews/WP-04_prior_art.md` was built at cycle 1 (L062). Since
then the A4 citation stations verified every reference at its primary record
(L070, L085) and corrected several metadata items in the drafts. The prior-art
document's rows were never brought back in line (A9's P3 observation, L093(b)).
Reconcile the rows against the A4-verified metadata. This is a metadata
refresh, NOT a re-sweep: no new works enter, no verdicts change, the novelty
ledger N1-N7/S1-S6 is untouched.

**Known stale items (from the record; verify each before editing):**
1. Chevignard-Fouque-Schrottenloher venue: the record is CRYPTO **2025**
   (cycle-3 sweep correction; see chronicle 2026-07-07_a4-wp07-citation-pass.md
   and the L070 entry).
2. ecdsa.fail attribution: **Eigen Labs** (same sweep correction).
3. Mosca-Piani timeline report: the sharpest-shift claim sits in the **2025
   edition** (GRI 2026-03-09), verified at the L085/L087 legs — if a prior_art
   row cites the 2024 report for that claim, retarget the row's wording.
4. Kagai, Branch, But & Allen 2025 (Telecom 6(4):100): read referee-grade and
   ENGAGED at L091; the row already carries the N7 annotation — verify the
   row's metadata (authors via Crossref, publisher PDF route) agrees with the
   L091 record and mark the formerly-unresolved status as resolved if any
   residue of it remains in the row.

**Method:** read `tasks/WP-04_A4.md` (the verification note + addenda) and the
A4 chronicles of 2026-07-07/09 as the source of verified metadata; diff each
prior_art row against them; edit rows in place; leave a dated refresh note in
the document's header block recording what changed and on whose verification.

**Checks:** run the four `checks/` scripts on the edited file with the explicit
path (argv-less runs now exit 2 by design; a versions FAIL on this file would
be a regression — the :62 false positive was fixed this cycle, A0 on record).

**Out of scope:** new prior-art search; the SoK draft; canon; manifest; ledger
(return the proposed entry to A0); tracker.

**Definition of done:** rows reconciled with per-row provenance; check run
recorded; chronicle per `chronicles/README.md`; proposed ledger entry returned
to A0.
