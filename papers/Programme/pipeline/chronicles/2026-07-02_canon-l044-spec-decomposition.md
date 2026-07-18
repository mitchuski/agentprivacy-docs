---
date: 2026-07-02
role: register-process executor (canon batch, L045 first-person approval; no standing pipeline role)
wps: [CANON (L044 execution)]
extractions: []
register_head: C96
ledger_entries: []
---

# Canon execution · L044 spec decomposition

## Verdict

Executed. The central-guarantee conflation identified at L042 and escalated CANON-LEVEL at L044 is now decomposed in both canon specification files: `papers/v6/privacy_value_v6_formal_specification.md` (eight passages) and `papers/v6/privacy_value_v6.md` (two passages). Every edit follows the approved decomposition: the two architectural preconditions (non-collusion; fixed adversary class) yield the additive leakage structure and the error floor P_e >= 1 - R_max; the strict bound R_max < 1 holds only when additionally the capacity-deficit condition C_S + C_M < H(X) holds, a measurable, declarable, time-eroding numerical condition, deliberately not labelled a third precondition. No passage was deleted; no section renumbered; no other content changed. The conjecture register, the whitepaper, the extractions and the rehydrations were not touched. No ledger entry was appended (proposed entries are in the final report to A0 with [Lxxx] placeholders). First-person diff review is the completion condition; this chronicle carries the full before and after record as that review surface.

## Defect corrected

Passages asserted R_max = (C_S + C_M)/H(X) < 1 as a consequence of the two architectural preconditions. Neither precondition constrains C_S + C_M relative to H(X); two conditionally independent channels of sufficient combined capacity satisfy both preconditions with R_max at or above one. The corrected statement is the two-part decomposition above, matching the exemplar wording of `rehydrations/policy/enforceable_by_architecture.md` sections 2 and 3 (release-draft v4, L043).

## Path

1. Boot per the task card: GROUND_RULES.md, tasks/L044_canon_spec.md, ledger L042 to L045, WP-02_review_1.md weakness 1, exemplar sections 2 and 3.
2. Verified backups of both targets at `archive/canon-backups-2026-07-02/`.
3. Surveyed the formal specification by section map and by pattern search (R_max, reconstruction ceiling, C_S + C_M, precondition, impossible, guarantee), then read sections 5, 10, 11, 14, 16, 18, 25 to 27, 31, 32 and the abstract in full at the candidate sites.
4. Edited eight passages in the formal specification (sections 5.4, 10.5 twice plus one added paragraph, 10.6, 11.1, 11.2, 11.5, 16) and two in the summary specification (sections 10 and 11).
5. Confirmed by diff against the backups that the change surface is exactly the ten hunks recorded below.

## Reversals and judgement calls

- One addition was made rather than a pure rewording: a paragraph in section 10.5 of the formal specification stating the capacity-deficit condition adjacent to the two preconditions. Justification: section 11.5 conditions the theorem on "Preconditions 1 and 2 of §10", so section 10 needed a home for the deficit condition for the decomposition to be readable at the point of reference; the exemplar (WP-02 v4) uses the same placement. This is a decomposition, not new content: every sentence in the added paragraph restates the approved L044 ruling.
- Section 11.2's lead sentence ("The adversary is guaranteed to make errors") was retained but conditioned, since the error floor is vacuous at R_max >= 1. Rhetorical weight preserved; the guarantee-of-errors sentence still leads.
- The section 16 table row was extended in place rather than restructured, to avoid touching the adjacent "Scoped, not lowered" paragraph, which is L028 territory (95 percent label scoping, not in the approved batch).
- Initially planned six edits to the formal specification; the sweep added section 10.6 (the external-grounding close conditions the ceiling claim on "named preconditions" alone) and section 11.2 (the unconditioned error-guarantee gloss). Both are genuine echoes of the conflation, not stylistic tightening.

## Complete before and after record

### File 1 · papers/v6/privacy_value_v6_formal_specification.md (8 passages)

**Edit 1 · §5.4 The Reconstruction Ceiling**

Before:
> This is not a conjecture. The ceiling follows from information-theoretic analysis via Fano's inequality. See §16 for the full proof status, and §10 to §11 for the preconditions under which it holds.

After:
> This is not a conjecture. The ceiling follows from information-theoretic analysis via Fano's inequality, read as a decomposition: the preconditions of §10.5 yield the additive capacity sum and the error floor, and the budget constraint is the capacity-deficit condition C_S + C_M < H(X) of §11.1, the numerical condition that places the ceiling strictly below one. See §16 for the full proof status, and §10 to §11 for the preconditions and the capacity-deficit condition under which it holds.

**Edit 2 · §10.5 Precondition 1, closing boundary sentence**

Before:
> Here it is the boundary condition: **the ceiling holds in the regime the Amnesia Protocol is designed to enforce, and only there.**

After:
> Here it is the boundary condition: **the additive capacity sum, and with it the error floor P_e ≥ 1 − R_max, hold in the regime the Amnesia Protocol is designed to enforce, and only there; the strict ceiling R_max < 1 requires in addition the capacity-deficit condition of §11.1.**

**Edit 3 · §10.5, new paragraph inserted after Precondition 2 (addition, no prior text)**

Before: (no text; inserted between the Precondition 2 paragraph and the §10.6 heading)

After:
> **The capacity-deficit condition (not a third precondition).** The two preconditions are architectural: attestable properties of the deployment. Neither constrains the sum C_S + C_M relative to H(X). What they buy is the additive leakage structure and the error floor P_e ≥ 1 − R_max; the strict bound R_max < 1 holds exactly when, additionally, C_S + C_M < H(X). That capacity deficit is a numerical fact about a given system and adversary class: measurable, declarable, and eroded over time as stronger classes arrive (§5.5). It is deliberately not listed as a third precondition, because two conditionally independent channels of sufficient combined capacity satisfy both preconditions with R_max at or above one; the deficit is the separate, system-specific fact a deployment measures and declares. §11 states the decomposition as the theorem's conditioning.

**Edit 4 · §10.6 External Grounding, closing sentence**

Before:
> This move costs nothing and buys defensibility: the claim is no longer "proven in our internal paper" but "an instance of a family of bounds the field already accepts, under named preconditions."

After:
> This move costs nothing and buys defensibility: the claim is no longer "proven in our internal paper" but "an instance of a family of bounds the field already accepts, under named preconditions and a declared capacity-deficit condition."

**Edit 5 · §11.1 Theorem (Proven, conditional regime)**

Before:
> where $C_S$ and $C_M$ are the information capacities of the Swordsman and Mage channels respectively, and $H(X)$ is the entropy of the First Person's private state.
>
> **Consequence:** Perfect reconstruction of the First Person's state is impossible.

After:
> where $C_S$ and $C_M$ are the information capacities of the Swordsman and Mage channels respectively, and $H(X)$ is the entropy of the First Person's private state.
>
> The theorem decomposes. The two preconditions of §10.5 license the capacity sum and yield the error floor of §11.2; they do not by themselves place $R_{\max}$ below one. The strict inequality is the **capacity-deficit condition** $C_S + C_M < H(X)$: a measurable, declarable, numerical fact about a given system and adversary class, not a consequence of the architecture (§10.5).
>
> **Consequence:** When the two preconditions and the capacity-deficit condition hold together, perfect reconstruction of the First Person's state is impossible against the stated adversary class.

**Edit 6 · §11.2 Error Floor**

Before:
> The adversary is guaranteed to make errors. This follows from Fano's inequality.

After:
> The adversary is guaranteed to make errors whenever the capacity-deficit condition of §11.1 holds. The floor itself follows from Fano's inequality and holds under the two preconditions of §10.5; at $R_{\max} \geq 1$ it is vacuous, which is exactly why the deficit condition must be declared alongside the preconditions.

**Edit 7 · §11.5 Conditioning**

Before:
> R_max = (C_S + C_M)/H(X) < 1 carries the label **Proven, conditional regime**: proven within Preconditions 1 and 2 of §10, an instance of the family cited there, and time-indexed per §5.5. The error floor P_e ≥ 1 − R_max (Fano converse) carries the same conditioning. Outside the regime, §26 governs.

After:
> R_max = (C_S + C_M)/H(X) < 1 carries the label **Proven, conditional regime**, read as a decomposition: within Preconditions 1 and 2 of §10 the capacity sum is licensed and the error floor P_e ≥ 1 − R_max (Fano converse) is proven, an instance of the family cited there; the strict bound R_max < 1 holds when, additionally, the capacity-deficit condition C_S + C_M < H(X) of §11.1 holds. The deficit condition, not the preconditions, is the time-indexed quantity per §5.5: R(t) can cross one with both preconditions intact, because capability growth raises the effective capacities, and what expires at t* is the deficit condition, not the architecture. Outside the regime, §26 governs.

**Edit 8 · §16 Proven Results, reconstruction-ceiling table row**

Before:
> | **Reconstruction ceiling** | $R_{\max} = (C_S + C_M)/H(X) < 1$ under budget constraints |

After:
> | **Reconstruction ceiling** | $R_{\max} = (C_S + C_M)/H(X) < 1$ under budget constraints, read per §11: the §10.5 preconditions license the sum and yield the error floor; the budget constraint is the capacity-deficit condition $C_S + C_M < H(X)$ that places the ceiling below one |

### File 2 · papers/v6/privacy_value_v6.md (2 passages)

**Edit A · §10 Precondition 1**

Before:
> **Precondition 1 (non-collusion).** The bound and the capacity sum of §11 hold when the two channels are conditionally independent given the First Person and no third channel carries the inter-agent residue: I(Y_S; Y_M | X) = 0. This is the regime the Amnesia Protocol exists to enforce, and only there does the arithmetic of §11 apply.

After:
> **Precondition 1 (non-collusion).** The bound, the additivity of the capacity sum of §11, and the error floor hold when the two channels are conditionally independent given the First Person and no third channel carries the inter-agent residue: I(Y_S; Y_M | X) = 0. This is the regime the Amnesia Protocol exists to enforce, and only there does the arithmetic of §11 apply; the strict ceiling of §11 requires in addition its capacity-deficit condition.

(The following sentence on the wiretap literature is unchanged.)

**Edit B · §11 The Reconstruction Ceiling**

Before:
> R_max = (C_S + C_M)/H(X) < 1 carries the label **Proven, conditional regime**: proven within Preconditions 1 and 2 of §10, an instance of the family cited there, and time-indexed per §5. The error floor P_e ≥ 1 − R_max (Fano converse) carries the same conditioning. Outside the regime, §26 governs.

After:
> R_max = (C_S + C_M)/H(X) < 1 carries the label **Proven, conditional regime**, read as a decomposition: within Preconditions 1 and 2 of §10 the capacity sum is licensed and the error floor P_e ≥ 1 − R_max (Fano converse) is proven, an instance of the family cited there; the strict bound R_max < 1 holds when, additionally, the capacity-deficit condition C_S + C_M < H(X) holds, a measurable, declarable, numerical fact about a given system and adversary class, not a consequence of the architecture, and deliberately not a third precondition. The deficit condition, not the preconditions, is the time-indexed quantity per §5: R(t) can cross one with both preconditions intact, and what expires at t* is the deficit condition, not the architecture. Outside the regime, §26 governs.

## Passages examined and left alone (with reasons)

Formal specification:
- Abstract (line 43): "the reconstruction ceiling proved to be a function of time (R(t), with a shelf life t*)". No conflation; already the decomposed reading.
- §5.4 external-alignment sentence ("the mathematical guarantee that makes data dignity enforceable"): does not attribute R_max < 1 to the preconditions; it is adjacent to the GR-7 sentence-family concern (L021-L022 batch item), which is not this task.
- §5.5 in full, including "a separation architecture adequate at t₀ can be inadequate at T > t₀": coherent with the decomposition; the mechanism paragraph is the source of the corrected reading.
- §10.1 ("The Mage cannot reconstruct the Swordsman's domain..."): concerns the separation bound I(S; M | FP) < ε*, not R_max; not the conflation.
- §11.3 Graceful Degradation: concerns ε violations, not the strict bound.
- §11.4: conjectural dynamical ceiling (C18), independent mechanism; no conflation.
- §14 in full (14.6, 14.7): additivity claims correctly scoped to the Precondition-1 regime; the exponential-versus-linear material does not assert R_max < 1 from preconditions.
- §16 "Scoped, not lowered" paragraph: additivity scoping only; also L028 territory (95 percent label), explicitly out of scope, not touched.
- §17 register reproduction (C82 row and all tables): register reproductions; the register process forbids touching them here, and the C82 row already carries the decomposed reading.
- §18.3, §25, §26, §27, §32 (Honest Limits): time-indexed and regime-scoped statements consistent with the decomposition; §32.1 item 4 concerns Precondition-1 verification, not the deficit.
- §33 spellbook crosswalk row "XVIII | The Reconstruction Ceiling | R < 1 proven result (§11)": a pointer row into the narrative acts table; it does not attribute the bound to the preconditions, and §11 now carries the decomposition at the pointed-to site. Flagged for the first-person read as a possible GR-7 style concern (unconditioned "R < 1 proven result" in a table cell), outside this task's approved batch.

Summary specification:
- Abstract, §5 (R(t) and t* statement), §16, §23 lineage table, §30: no conflation; the §5 shelf-life statement is the decomposed reading.
- §10 Provenance paragraph: "The bound is an instance of an established family" does not condition R_max < 1 on the preconditions; left as is.

## Confirmation of scope

- `research/CONJECTURE_REGISTER_V6.md`: not opened for writing, not edited.
- Whitepaper (`papers/whitepapers/swordsman_mage_whitepaper_v6_3.md`): not touched (parallel session owns it).
- Extractions and rehydrations: not touched (A1 re-issues E2-C01 and tightens E1-C02 after this lands).
- Spec §16 95 percent label scoping (L028): seen, deliberately not fixed (unapproved).
- No git operations. No ledger append.
- Diff against `archive/canon-backups-2026-07-02/` confirms the change surface is exactly the ten passages above.

## Handoff

- **First person:** diff review of the ten passages above (the completion condition). One flag outside the batch: §33 crosswalk row "R < 1 proven result (§11)" in the formal specification is unconditioned in-cell; a GR-7 style call for a future batch, not acted on here.
- **A0:** file the proposed ledger entries from the executor's final report (L044 execution record with [Lxxx] placeholder); notify A1.
- **A1:** re-issue E2-C01 and tighten E1-C02 against the corrected spec wording (per L044 PROPOSED); then sweep downstream consumers of E2-C01/E1-C02 (WP-04, WP-07, WP-09 per FEEDS).
- **Open question:** whether the summary specification's §10 Provenance paragraph should also name the deficit condition; judged not to carry the conflation, so left for editorial discretion at the P4 read.
