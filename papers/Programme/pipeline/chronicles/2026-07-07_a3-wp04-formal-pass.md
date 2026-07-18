---
date: 2026-07-07
role: A3
wps: [WP-04]
extractions: [E2]
register_head: C96
ledger_entries: []
---

# WP-04 formal pass: moving_ceiling_sok.md draft-v1 to draft-v2

**Verdict.** The formal pass is complete. `rehydrations/academic/moving_ceiling_sok.md` stands at draft-v2: every formal statement is now proved, cited, or labelled Conjecture with a proof obligation and its register identifier; no claim was widened past the novelty fence (reviews/WP-04_prior_art.md N1 to N7, S1 to S6); Definition 2 is sup-accurate with the monotonicity question surfaced and no first-crossing dependence; all three checks (register_refs, tier_vocab, figures_fence) PASS. The artifact is ready for the A0 spot-trace toward P0.

## Formal statements changed (one line each)

1. Proposition 1: restated with explicit hypotheses (finite alphabet, |X| >= 3, budgets against the declared class), split into (a) the capacity-sum bound as an inequality with its equality condition and (b) the exact Fano floor carrying the 1/H(X) term and the alphabet-entropy hypothesis; full proof supplied; recorded as a restated known-bound pair, with N2 confined to the decomposition reading.
2. The rounded floor P_e >= 1 - R_max is no longer asserted anywhere in WP-04; only the exact converse is, with an in-text precision note (see the precision finding below).
3. Definition 2: restated with domain (t >= t_0) and conventions (t* = infinity; t* undefined when the sub-unity set is empty); new Remark 1 states exactly what the supremum asserts (R(t) >= 1 for all t > t*) and does not assert (the interval up to t* is not certified), names the first-crossing quantity only to renounce dependence on it, and ties the monotonicity question to the Section 4 programme.
4. Section 4.1: new Definition 3 (decoder class as a gain-function family; effective capacity as a supremum over the class, under a stated compatibility requirement that bridges to Proposition 1); new Lemma 1 with proof (ordering hypothesis implies capacities monotone, R(t) non-decreasing, and sup equals first crossing); the empirical residue stated exactly per the N3 fence in three named items (ordering hypothesis as modelling assumption; the bit-valued functional as the exact missing step; instantiation absent in the literature), with the demotion clause retained.
5. Conjecture 1 (C82): content unchanged; one sentence added expressing the claim in Definition 3's terms; proof obligation and register identifier retained.
6. Conjecture 2 (C81): candidate probability model added (method variable M, cost functional c, feasibility indicator F_tau); the formal object-distinction sentence against Garg-Jain-Sahai added (witness leakage within one execution versus I(F_tau; M) across systems; neither bounds the other); the named missing step recorded: under the naive model the inequality is immediate (I(F_tau; M) = H(F_tau) > 0 for non-constant F_tau), so stated bare it is true and empty, and the proof obligation is an attestation class in which the claim is operationally non-vacuous.
7. Conjecture 3 (C93): the difficulty functional given an explicit symbol Delta_k(X) with its valuation named (expected search cost over the candidate space); the fixed-corroboration-model hypothesis made explicit in the statement; the steep-then-shallow profile left unasserted beyond monotonicity, as A2 had it.
8. Conjecture 4 (C84): axioms (D1) normalisation, (D2) monotonicity in specificity, (D3) domination by full disclosure supplied for the discount functional; the conjecture explicitly held at schema level until an elicitation or market study identifies a conforming D.
9. Section 6.4: formal-pass decision recorded in the text: both limitative framings (C90, C92) retained at related-work status only; no formal statement of either is made and neither is used by the formal apparatus.
10. Abstract, Sections 1, 1.1(2), 8, 9: "additive" wording tightened to the capacity-sum bound (the exact mathematical form is an inequality); "proof owed at the formal pass" removed; the conclusion's conjecture count corrected from three to four; the abstract's evidence attribution tightened (the existence-leak conjecture has one verified instance, not two; the two 2026 instances belong to the survey of the archival regime).
11. The single permitted public-spec URL placed once, as a footnote at Section 3.1, per the A0 provisional ruling L066(c).

## Path

Inputs read in order: task card; A2 draft-v1 with its handoff work list; E2 (including the 2026-07-07 maintenance touch: E2-C07 re-issue, E2-C12 annotation); reviews/WP-04_prior_art.md; ledger L054, L062, L065, L066; corrected spec sections 5, 10, 11 (read-only, for the decomposition's exact form); WP-07 linear_cap_paper.md section 3 (read-only, for notation).

The session was interrupted twice (a session limit during boot, then a server error mid-edit); after the second interruption the on-disk state was re-verified line by line before continuing, and all earlier edits were found intact. The E2 maintenance touch landed mid-session: Section 5.8 already conformed to the re-issued E2-C07 (Babbush et al. attribution; the tenfold figure carries its spacetime-volume metric in the claim text), and arXiv:2509.14284 remains uncited, consistent with its verification-in-flight annotation. No draft change was needed for either.

## Reversals

1. Conjecture 2: the first instinct was to prove the inequality as a lemma under the candidate model, since F_tau non-constant and a function of M gives I(F_tau; M) = H(F_tau) > 0 immediately. Reversed: promoting that to a result would trivialise the law (true and empty) and would amount to widening by emptying the claim of content. The triviality is instead named in the statement as the missing step, and the proof obligation is restated in the operational form (quantified search-cost reduction for a stated attestation class). A dead end that became the sharpest sentence in the section.
2. Notation collision D(a) versus D(X) inside Section 6: first considered renaming the discount functional, reversed because Z_b' = Z_b - D(a) is the fenced N5 form and the extraction's own formula (E2-C09); the difficulty functional was renamed to Delta_k(X) instead, with the renaming declared in the conjecture's text.
3. Section 4: A2's draft offered demotion to a discussion paragraph as the fallback and the pass briefly weighed taking it (the full QIF grounding cannot be finished inside one paper). Reversed to the middle path the N3 fence actually permits: grounding at definition level plus the one provable lemma, with the residue named exactly and the demotion clause kept live inside the paper.

## Precision finding (proposed ledger entry, A0 to append)

**Proposed entry 1 (SUITE, precision, same class as L065(e)).** Spec section 11.2 and E2-C01 quote the error floor in the rounded form P_e >= 1 - R_max. The exact Fano converse yields P_e >= (H(X) - C_S - C_M - 1)/log(|X| - 1), which gives 1 - R_max - 1/H(X) only under an alphabet-entropy hypothesis; the rounded form is not exactly implied. WP-07 flagged the same point at L065(e); WP-04 now likewise asserts only the exact form. No canon contradiction is claimed (the rounded form reads as a large-H(X) simplification); proposal: the register process consider a one-line precision annotation at spec 11.2, and A1 consider annotating E2-C01's floor wording at next E2 touch. Extraction wording was left untouched here per GR-9 (the claim trace quotes the canon).

**Proposed entry 2 (WP-04/WP-07, L054-adjacent).** WP-04's Definition 2 plus Remark 1 now state the supremum reading exactly, and Lemma 1 shows sup and first crossing coincide under the ordered-family hypothesis; this executes, at rehydration level, the E2-C04 route that L054's PROPOSED line contemplated, while the canon-level refinement of spec section 5 stays with the register process (L054 remains open). Related flag: WP-07 Remark 3.4 glosses t* = sup{t : R(t) < 1} with no sup-semantics caveat and thus inherits the L054 question; propose a one-line remark at WP-07's next touch.

**Proposed entry 3 (WP-04, notation register).** Deliberate cross-paper divergence, flagged not harmonised: WP-07 treats C_S, C_M as declared budgets (ER-5/ER-6); WP-04 defines them as class-relative effective capacities (Definition 3's supremum). Same symbols, different definitional route; WP-07's ER-6 already defers the ordered-family formalisation to the WP-04 side. To be reconciled editorially (a cross-reference sentence in each) when both papers approach release; no mathematical conflict, since WP-04's compatibility requirement makes its capacities usable exactly where WP-07 uses budgets.

**Proposed entry 4 (WP-04, status).** A3 formal pass complete at draft-v2; all A2 work-list items discharged or explicitly carried (UNVERIFIED items still uncited, bib additions still with A4/A8); checks register_refs, tier_vocab, figures_fence all PASS on 2026-07-07; next gate action is the A0 spot-trace for P0.

## Checks

Run on 2026-07-07 against draft-v2, from `pipeline/checks/`: register_refs PASS, tier_vocab PASS, figures_fence PASS. Register identifiers present (C81, C82, C84, C86, C90, C92, C93, C18 to C21) are all at or below head C96 and none carries a percentage band; no sanctioned-figure or fiat pattern appears; no canon vocabulary appears in the artifact body.

## Handoff

- **WP-04, single next action:** A0 spot-trace for P0 on draft-v2. The artifact's apparatus header carries the formal-changes list, the notation flags against WP-07, and the A2 work-list discharge record.
- **Open questions:** (a) whether the register process adopts the precision annotation at spec 11.2 (proposed entry 1); (b) L054 remains open at canon level, with the rehydration-side treatment now in place; (c) Definition 3's compatibility-requirement witness (the bit-valued functional) is the exact missing step of the Section 4 programme and a candidate future work item for A3 beyond this card's scope.
- **Blocked items:** none for this pass. Bibliography additions (~36 entries, L066(b)) and the referee-grade everlasting-privacy sweep (L062(d)) block P1, not P0, and sit with A4/A8.
