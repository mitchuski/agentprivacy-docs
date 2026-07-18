---
date: 2026-07-08
role: A3
wps: [WP-07]
extractions: [E1, E2]
register_head: C96
ledger_entries: []   # proposed entry text delivered to A0 in the session report; A0 assigns the number
---

# A3 micro-fix: sup-semantics caveat added to Remark 3.4 (WP-07)

## Verdict

Executed. The L069(b) defect in `rehydrations/academic/linear_cap_paper.md` is closed: Remark 3.4's gloss of t* now carries the sup-semantics caveat, stating that t* = sup{t : R(t) < 1} is not in general a first crossing and naming the monotonicity condition under which the expiry reading is exact, in the wording discipline Corollary 5.4 already uses ("With budgets ε_i(t) non-decreasing in t"). Two sentences added; no new claims, no new notation, no new citations. The traceability appendix's Remark 3.4 line now records E2-c04. All four checks exit 0. Nothing else in the theory core changed. No ledger append (per session sanction, the proposed entry text goes to A0 for numbering); no manifest touch; no git action.

## The change, quoted

Before (Remark 3.4, the affected passage):

> ... R(t) can cross one with every structural requirement intact, and what expires at t* is the deficit condition, not the architecture. Treating channel capacity as a time-indexed quantity has precedent ...

After:

> ... R(t) can cross one with every structural requirement intact, and what expires at t* is the deficit condition, not the architecture. The supremum is not in general a first crossing: R(t) may cross one and return, in which case t* marks the last time the deficit condition holds, not the first time it fails. When C_S(t) + C_M(t) is non-decreasing in t (the regime of ER-6's growing decoder class, and the hypothesis under which Corollary 5.4 below states the composed shelf life), R(t) is non-decreasing, the supremum coincides with the first crossing, and the expiry reading is exact. Treating channel capacity as a time-indexed quantity has precedent ...

Trace map addition (traceability appendix, Remark 3.4 row): `E2-c04 (sup-semantics caveat: sup = first crossing under monotone decoder-class growth, added 2026-07-08 per L069(b))` inserted between the E1-c02 mapping and the Gopala-Lai-El Gamal note.

## Path and reasoning

1. Read L069(b) in the ledger, GROUND_RULES.md, the A3 role card, extraction claims E1-C02 and E2-C04, Remark 3.4 with its surrounding section 3 text, ER-6/ER-7, and Corollary 5.4.
2. The defect is exactly as filed: the remark defined t* as a supremum and then spoke of expiry ("what expires at t*") without the hypothesis that makes the expiry reading exact. Corollary 5.4 already carries the hypothesis explicitly for the composed form (budgets non-decreasing in t); the remark's base form did not.
3. The fix route is E2-C04 (ordering of decoder classes implies monotonicity implies sup = first crossing), the same route WP-04's Definition 3 + Lemma 1 discharge formally per L069. At this remark's level of formality the route is stated as a condition, not re-proved: the formal development is companion work, exactly as ER-6's parenthetical already says.
4. Wording chosen to reuse only existing notation (R(t), C_S(t), C_M(t), t*, ER-6, Corollary 5.4) and Corollary 5.4's "non-decreasing in t" formulation. Forward references to ER-6 and Corollary 5.4 are already the remark's practice ("ER-1 below", "ER-6 below").
5. Trace map: judged that the caveat's extraction basis is E2-c04, which was absent from the Remark 3.4 row; added the one mapping line per the session sanction.

## Reversals

None. One candidate action considered and declined: updating the frontmatter `status` line, which reads "theory core sections 3-5 unchanged at P0 per L072" and is now stale by exactly this sanctioned touch. That line is state-description, A0's to amend alongside the ledger entry; flagged in the session report rather than edited here (a one-remark touch does not self-describe in the frontmatter).

## Checks

- `checks/check_register_refs.py` exit 0
- `checks/check_tier_vocab.py` exit 0
- `checks/check_figures_fence.py` exit 0
- `checks/check_versions.py` exit 0

## Handoff

- **WP-07, next action:** A5-crypto-pc reads the draft (gate target P1). The draft is otherwise as A2 and A4 left it; abstract, sections 1-2 and 6-7 are A2's and untouched.
- **Open item for A0:** assign the ledger number to the proposed entry (delivered in the session report); amend the frontmatter status line's "theory core sections 3-5 unchanged at P0 per L072" to record this sanctioned one-remark touch; L069(b) can then close.
- **Blocked:** nothing.
