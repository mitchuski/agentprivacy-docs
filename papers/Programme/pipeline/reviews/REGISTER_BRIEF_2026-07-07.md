# Register Brief · 2026-07-07 · four items from the Fable runtime cycles (+1 added 2026-07-08)

**Prepared:** 2026-07-07, role A1 (Extractor), task card E1_E2_A1_maintenance_2026-07-07
**Status:** PROPOSAL ONLY · nothing in the register or the canon changes this session
**Register head observed:** C96
**Evidence base:** ledger L062, L063, L065, L066; rehydrations/academic/linear_cap_paper.md (WP-07 theory draft); rehydrations/academic/moving_ceiling_sok.md (WP-04 SoK draft); reviews/WP-04_prior_art.md; chronicle 2026-07-07_a8-submission-scaffold.md.

---

## Why this brief exists

Two cycle-3 drafts changed the epistemic shape of three register rows without touching a word of register text, and a bibliography verification surfaced a one-word canon defect. The standing rule is absolute: the proposer does not approve its own proposal, and no pipeline role marks P4. This brief therefore carries exact wording options, the evidence line for each, and what a P4 revert looks like, and stops there. The first person rules on all four items; every ruling is revertible at the P4 read.

---

## Item (a) · C83 · the proven side and the exponential side answer different adversaries

**Current row (verbatim, register Band VIII):**

> C83 | Compositional Leakage Amplification: policy-only separation compounds toward (2^N − 1)ε with chain depth; amnesia separation breaks the Markov chain and caps at Nε; the gap is exponential-to-linear | ~55% | active · registered Run 2, 2026-06-10 · edge C7 → C83 → C17 | core | privacy_value_v6_draft.md Part II §II.3

**Finding (L065(c)).** The WP-07 theory draft proves the Nε side as a conditional theorem (Theorem 5.1) against the *transcript adversary* (observes the full inter-agent transcript T), under conditional interface-inclusive budgets plus structural context erasure (requirements ER-1 to ER-5). The (2^N − 1)ε side is proven externally (arXiv:2603.05520 Thm 4.1, imported at WP-07 Theorem 4.1) against the *final-output adversary* (observes O_N only), under marginal output-only budgets. The row's implicit like-for-like comparison is not available as stated: WP-07 Proposition 4.3 exhibits a two-agent composition satisfying erasure with zero marginal budgets in which the transcript adversary recovers a context completely, so against the transcript adversary the policy side is not (2^N − 1)ε-bounded at all, and erasure alone caps nothing. What remains conjectural at ~55% is per-system conformance: that a real erasure implementation achieves the ER-1 to ER-5 discipline. This matches the extraction's existing fence (E1-C08: "the conjecture is that real amnesia implementations achieve the chain break, an engineering claim about the erasure protocol, not a theorem").

**PROPOSED · Option A (annotation, recommended).** Append to the C83 row's status column, confidence untouched:

> annotation 2026-07-07: the two bounds answer different adversary classes; the (2^N − 1)ε bound is proven against the final-output adversary under marginal output-only budgets (arXiv:2603.05520 Thm 4.1), the Nε cap is proven against the transcript adversary under conditional interface-inclusive budgets plus structural context erasure (WP-07 Theorem 5.1, conditional on ER-1 to ER-5); erasure alone caps nothing against the transcript adversary (WP-07 Prop 4.3); the conjectural residue at ~55% is per-system conformance to the erasure-and-budget discipline, not the mathematics.

**PROPOSED · Option B (row split).** C83 keeps its number and narrows to the conformance conjecture; the mathematical half is recorded as discharged-conditional with no new number (theorems do not take conjecture numbers). Statement column becomes:

> C83 | Compositional Leakage Amplification, conformance form: deployed erasure implementations achieve the ER-1 to ER-5 discipline under which total transcript leakage is capped at Nε (WP-07 Theorem 5.1); against the final-output adversary with marginal budgets the external bound is (2^N − 1)ε (arXiv:2603.05520 Thm 4.1); the two bounds answer different adversaries, and the mathematical half of the original row is discharged as a conditional theorem 2026-07-07 | ~55% | ...

**Evidence line:** rehydrations/academic/linear_cap_paper.md Definition 3.6 (adversary classes), Theorem 4.1, Proposition 4.3, Theorem 5.1, Remark 5.7; ledger L065(c); extraction E1-C08.

**P4 revert:** strike the annotation (Option A) or restore the single row verbatim as quoted above (Option B). No extraction change is needed in either direction; E1-C08 already carries the conformance reading and both drafts state their adversary classes in-text.

---

## Item (b) · C86 · first TIER-A carriage, register note

**Current row (verbatim, register Band VIII):**

> C86 | Obstruction-Theoretic Amnesia: Grade-2 forgetting = non-vanishing obstruction class to gluing local agent views into a global witness of O; Grade-1 = vanishing class with withheld gluing data; amnesia is the only term whose security is independent of t | ~30% | active · registered Run 4, 2026-06-10 · cross-linked C73 (taxonomy placement vs cohomological content) · falsification: any view-composition recovering Grade-2-forgotten O | core | privacy_value_v6_draft.md Part IV §IV.4

**Finding (L065).** The WP-07 draft carries C86 for the first time at TIER-A, as Conjecture 5.8 (obstruction-theoretic grade criterion), formally stated with three numbered proof obligations and the missing step named: obligation (i), construction of the site (a cover and topology on which the candidate Čech class lives, for at least the two-agent instantiation), is unstarted; the sheaf-theoretic vocabulary is imported, not constructed. The draft's theorem layer is independent of the conjecture, and the falsifier is restated in the paper's terms.

**PROPOSED register note.** Append to the C86 row's status column, no status or confidence change:

> note 2026-07-07: first TIER-A carriage as WP-07 Conjecture 5.8, with proof obligations (i) site/cover construction for the two-agent instantiation (unstarted; the named missing step), (ii) the recoverability-with-keys ↔ vanishing-class correspondence, (iii) a computable invariant in one non-trivial instance; confidence unchanged at ~30%; nothing in WP-07's theorems depends on it.

**Evidence line:** rehydrations/academic/linear_cap_paper.md §5.3 (Conjecture 5.8; "The missing step, named"; falsifier); ledger L065; extraction E1-C12 ("~30% prices a framing, not a theorem").

**P4 revert:** delete the note; the row returns verbatim.

---

## Item (c) · C82 · cross-reference note only, no status change

**Current row (verbatim, register Band VIII):**

> C82 | The Moving Ceiling: frontier capability growth raises C_S(t) + C_M(t) against fixed archives without raising H(X); R(t) drifts upward and every static reconstruction guarantee has a finite shelf life t* | ~65% | active · registered Run 1, 2026-06-10 | core | privacy_value_v6_draft.md Part I §I.3

**Finding (L066).** The WP-04 SoK draft carries the drift as "Conjecture 1 (capability-coupled drift; programme register C82, moderate confidence, mechanism unestablished)", with the proof obligation stated in-text: a formalised coupling model and at least one measured capability series showing capacity increase attributable to model release against a fixed archive; the two verified 2026 instances are named as a single year's cluster, not a series. The paper separates the erosion observation (shared with the HNDL, everlasting-privacy and re-identification corpora; not conjectural) from the coupling claim, which is C82 proper. No status change is proposed; this item records the cross-reference so the register and its first TIER-A surface point at each other.

**PROPOSED cross-reference note.** Append to the C82 row's status column:

> cross-reference 2026-07-07: carried at TIER-A as WP-04 Conjecture 1 (capability-coupled drift), proof obligation a formalised coupling model plus a measured capability series; the erosion observation is separated from the coupling claim in that carriage; no status or confidence change.

**Evidence line:** rehydrations/academic/moving_ceiling_sok.md §4.2 (Conjecture 1); extraction E2-C03; ledger L066.

**P4 revert:** delete the note; the row returns verbatim.

---

## Item (d) · v4.3 publisher correction · one-word canon diff

**Finding (L063(a)).** The v4.3 research paper's References item 1 attributes the Bergstra and Burgess Promise Theory book to O'Reilly Media. The public record shows it independently published (2nd edition 2019, ISBN 978-1696578554; 1st edition CreateSpace, 2014). The A8 submission scaffold's bibliography already carries the verified publisher; the canon file is untouched pending this ruling.

**Before** (papers/lineage/dualprivacy_researchpaper_v4_3.md:1730):

> 1. Bergstra, J.A. & Burgess, M. (2019). Promise Theory: Principles and Applications. O'Reilly Media.

**After (PROPOSED):**

> 1. Bergstra, J.A. & Burgess, M. (2019). Promise Theory: Principles and Applications. Independently published.

**Scope note, for one-stroke ruling if desired.** The same attribution recurs on three further canon surfaces outside L063's naming: papers/v6/privacy_value_v6_formal_specification.md:1371 and :1429, and papers/v5/privacy_value_v5_4_formal_specification.md:961. L063 names only v4.3; whether the identical one-word correction extends to the v5.4 and v6 surfaces is the first person's call, flagged here so a single ruling can cover all four sites. (Extraction E1-C17 cites the book without a publisher field; no extraction change is needed under any ruling.)

**Evidence line:** ledger L063(a); chronicle 2026-07-07_a8-submission-scaffold.md; templates/submission/references/pv_v6.bib (verified entry with the publisher note).

**P4 revert:** restore "O'Reilly Media." at each corrected site.

---

## Item (e) · spec model-descriptor · one-phrase canon diff x2 (added 2026-07-08, L074)

The A9 weekly sweep found the AgentLeak model descriptor divergent across the
suite. The verified fact (L070(2), against the published benchmark): the five
evaluated models are GPT-4o, GPT-4o-mini, Claude 3.5 Sonnet, Mistral Large and
Llama 3.3 70B — production models, not uniformly frontier models. The spec
carries "five frontier models" at formal-spec :1161 and :1406 while its own
:677 names the five. WP-07 already carries the verified wording ("five
production LLMs", Def 3.6); WP-04, E1-C10 and E2-C12 carry the spec's wording
faithfully.

**Proposed:** the two spec occurrences read "five production LLMs" (same class
as the item-(d) one-word diff and the L039 single-author sweep: a factual
descriptor corrected to the verified source). On the ruling, A1 re-issues
E1-C10/E2-C12 wording and WP-04's occurrence aligns at its A4 citation
station. Declining leaves the descriptor divergence standing with WP-07 alone
on the verified side.

## First Person writes

*(Confirm or override, one line each. The next runtime folds the ruling back verbatim; the register and canon change only after, and only per, these lines.)*

- **Item (a) C83:** Option A annotation as worded / Option B split as worded / row unchanged / own wording:
- **Item (b) C86 note:** accept as worded / decline / own wording:
- **Item (c) C82 cross-reference:** accept as worded / decline / own wording:
- **Item (d) v4.3 publisher:** correct v4.3 only / correct all four sites / decline:
- **Item (e) spec model-descriptor:** correct both spec occurrences / decline:

---

the register moves only by the first person's hand; this page only asks.
