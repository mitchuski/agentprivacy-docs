---
date: 2026-07-08
role: A5
wps: [WP-07]
extractions: []
register_head: C96
ledger_entries: [L077]
---

# A5 seat session · WP-07 adversarial review 1 (PoPETs crypto/IT-theory persona)

## Verdict

WP-07's `rehydrations/academic/linear_cap_paper.md` (completion-draft-v1) received its first adversarial review at the crypto-pc seat: **MAJOR REVISION. 1 BLOCKING, 4 MAJOR, 8 MINOR. No desk-reject grounds. Not P1 evidence this cycle.** The memo is on `tasks/WP-07_A5.md` under "## Review memo", verdict-first, all thirteen findings numbered, severity-tagged and passage-anchored, each with the fix that would satisfy the objection. Serialised by A0 as L077.

The BLOCKING item is a genuine mathematical error, the only false statement found in the paper: Proposition 4.2 fails under the generality its own section preamble declares ("carried state permitted"), because the proof's conditional-Markov step silently assumes no carried state and an unstated freshness hypothesis on N_i. The review supplies an explicit two-invocation counterexample inside the stated model (fresh junk emitted as O_1, rho_1 = S_1, O_2 = rho_1; every stated hypothesis holds at eps = 0 while L_2 = H(S_1) > 0) and the one-line hypothesis fix that restores the proposition, whose proof is otherwise correct. The following "even without erasure" sentence inherits the same gap and the memo shows it false by the same construction.

The four MAJORs: (1) the headline exponential-to-linear "separation" compares two upper bounds, with no attainability result for the geometric regime and with eps parameters of different operational strength on the two sides; (2) ER-6's time-indexed budgets are ill-typed against Shannon mutual information and Corollary 5.4's expiry narrative needs the certified-bound reading stated; (3) ER-1's literal wording already excludes the carried-state channel, making Proposition 5.5's hypothesis set self-contradictory on a literal reading; (4) the abstract's "auditable" overclaims for ER-5, whose conformance is an unaddressed MI-estimation problem.

## Re-derivation scope

The review read proofs rather than sampled them. Re-derived in full at this seat: Theorems 3.1, 3.2, 3.3 (correct; one estimator-range nit, MINOR-2); Proposition 4.2 (false as stated, counterexample constructed; proof verified correct under the repaired hypotheses); Proposition 4.3 (correct, and the paper's strongest asset: an infinite separation at budget zero); Theorem 5.1 (correct; Steps 1 to 3 checked including the conditional-independence lemma in Step 2 and the exact exchange identity in Step 3); Corollary 5.2 (reduction verified, ER-3's joint form carries it); Corollary 5.4 (follows, one-bit threshold slippage against ER-7, MINOR-1); Proposition 5.5 (construction correct; ER-1 wording collision, MAJOR-3); Proposition 5.6 (correct). The Theorem 4.1 import was checked against the A4 verification note only, per the card: it now carries both source hypotheses, and the ORTHOGONAL verdict was treated as settled and not re-litigated.

## Path and turning points

Boot per card sequence: ground rules, role card, task card, A4 verification note in full, then the paper in full. The card's five attack surfaces plus the two L075 surfaces were each priced explicitly; the memo carries an "answers to the card's attack surfaces" section mapping every surface to a finding or to a clean verdict. Findings that cleared: Theorem 5.1's hypotheses are non-circular (ER-5 is local, the theorem's content is exactly the global-to-local distance); the adversary framing does not overclaim; no unconditional-ceiling drift was found in A2's fresh sections, which was hunted for specifically.

Turning point of the session: the BLOCKING finding emerged not from section 5 (the expected attack surface) but from section 4, by testing the section preamble's "full generality" declaration against Proposition 4.2's proof steps. The lesson for the pipeline record: the theory core's P0 status covered trace fidelity, not proof soundness against the surrounding section's declared model, and the two can diverge.

Reversals: none. One scoping decision recorded rather than reversed: MINOR-4 (section 1's "hypotheses are individually load-bearing" overstates two-of-five necessity coverage) was priced MINOR rather than MAJOR because the abstract and section 5.2 state the coverage precisely; the memo supplies a cheap ER-4 necessity construction should the authors prefer to strengthen rather than weaken.

## Session interruption note

The session was killed by the session limit during close-out, after the memo and the card's frontmatter status update had landed on disk and before this chronicle was written. A0 verified the memo complete on disk (all thirteen findings through the final recommendation) and serialised the ledger entry as L077; this chronicle was written on resume under A0's instruction not to re-run the review. Nothing was rebuilt.

## Handoff

- **Open questions:** whether the geometric regime's attainability (MAJOR-1 prong (a)) is resolvable by citation from the Asif-Amiri source or requires an in-model construction; which of the two sanctioned resolutions of MAJOR-4 (soften "auditable" versus section 6 owning the estimation gap) the revision takes, noting the memo recommends the second.
- **Blocked:** WP-07's P1 gate is paused at the review station pending the revision loop; a targeted re-check of BLOCKING-1 and MAJOR-1 to MAJOR-4 suffices after revision, no second full review needed unless the revision touches proofs beyond the named fixes.
- **Next action per WP touched:**
  - **WP-07 to A3 (statement legs):** BLOCKING-1 (Proposition 4.2 hypotheses plus the "even without erasure" sentence), MAJOR-2 (ER-6/Corollary 5.4 semantics of eps_i(t)), MAJOR-3 (ER-1 rewording), MINOR-1 (threshold reconciliation), MINOR-2 (Fano estimator range), MINOR-3 (Definition 3.7 "Equivalently"), MINOR-7 (Conjecture 5.8 restyle or fixed candidate site), MINOR-8 (Definition 3.8 closure informality note).
  - **WP-07 to A2 (wording legs):** MAJOR-1 (abstract "admits exponential amplification", sections 1/7 "bounded only by", the Remark 5.7 like-with-like fence; statement-side coordination with A3 if an attainability construction is adopted), MAJOR-4 (abstract "auditable" plus the section 6 estimation paragraph), MINOR-4 (section 1 necessity-coverage sentence), MINOR-5 (DP contrast sharpening), MINOR-6 (csiszar1978broadcast role).
