---
date: 2026-07-10
role: A3/A1 hybrid (canon-batch execution seat, cycle 12, L047 pattern, per L125)
wps: [WP-03]
extractions: [E1]
register_head: C96
ledger_entries: []
---

# Canon additivity batch · CTR-OBS-01 execution (L125)

Verdict first. The CTR-OBS-01 correction landed at every V6-era EXACT site named in the verified inventory (reviews/CTR-OBS-01_verification_and_inventory.md, Part 2.3), plus the two ruled pipeline legs: the E1-C04 re-issue on the L044 pattern and the grant_edition.md one-line inheritance fix. The exact-additivity wording is replaced everywhere by the subadditive truth: under Precondition 1, I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M) − I(Y_S; Y_M), hence at most the sum, with equality if and only if the two outputs are also marginally independent. The pvm_v6_compressed.md display at :112 additionally had its pre-L044 conflation repaired (preconditions give the bound and the floor; the strict bound needs the declared capacity-deficit condition). The V5.4 specification's :634 site was NOT edited; the artefact received a non-invasive superseded-status flag (HTML comment at the document head) per the OBS-GPT56-017 convention. The capacity-deficit "holds exactly when C_S + C_M < H(X)" clause class was fenced out of the fix at every site and is unchanged everywhere. Backups of all seven touched files were taken to archive/canon-backups-2026-07-10/ before any edit. Checks: no new findings anywhere; all failures verified pre-existing by running the same check against the pre-edit backups. First-person diff review is reserved on landing per L125; this chronicle is that review's surface.

Sequence: backups first; then the canon sites in inventory order; then the E1-C04 re-issue (canon-first ordering per the L044 pattern); then the WP-03 inheritance sentence (sequenced after the re-issue so the trace stays exact); then checks; then this chronicle.

## Before and after, every site

Repo root: C:\Users\mitch\agentprivacy-docs. Line anchors are the inventory's; each site was re-located by content before editing.

### Site 1 · papers/v6/privacy_value_v6_formal_specification.md, §14.7 (inventory :679)

BEFORE:

> §16 asserts additive leakage, I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M), at 95% confidence. The compounding bound does not contradict the additive claim in the model's own regime: additivity holds exactly when the channels are conditionally independent given X and nothing carries the inter-agent residue, which is Precondition 1 of §10.5.

AFTER:

> §16 asserts the additive leakage bound, I(X; Y_S, Y_M) ≤ I(X; Y_S) + I(X; Y_M), at 95% confidence. The compounding bound does not contradict the additive bound in the model's own regime: when the channels are conditionally independent given X and nothing carries the inter-agent residue, which is Precondition 1 of §10.5, the joint leakage satisfies I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M) − I(Y_S; Y_M), hence is at most the sum, with equality if and only if the two outputs are also marginally independent (I(Y_S; Y_M) = 0); every ceiling and floor statement uses only the at-most direction, which the redundancy term only tightens.

The rest of the paragraph (the OUTSIDE-the-regime compounding description) is unchanged.

### Site 2 · papers/v6/privacy_value_v6_formal_specification.md, §16 table row (inventory :778)

BEFORE:

> | **Additive MI bounds** | Mutual information leakage from conditional independence is additive, not multiplicative: $I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M)$ |

AFTER:

> | **Additive MI bounds** | Under conditional independence (Precondition 1), mutual information leakage is at most additive, not multiplicative: $I(X; Y_S, Y_M) \leq I(X; Y_S) + I(X; Y_M)$, with equality iff additionally $I(Y_S; Y_M) = 0$ |

The adjacent Reconstruction ceiling row (which carries the L044 decomposition and the deficit condition) is unchanged.

### Site 3 · papers/v6/privacy_value_v6_formal_specification.md, §16 "Scoped, not lowered" (inventory :786)

BEFORE:

> **Scoped, not lowered (V6).** The results stand with their conditioning stated: additive leakage I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M) holds exactly in the Precondition-1 regime (no inter-agent channel); the 95% label applies there and nowhere else.

AFTER:

> **Scoped, not lowered (V6).** The results stand with their conditioning stated: in the Precondition-1 regime (no inter-agent channel) the joint leakage satisfies I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M) − I(Y_S; Y_M), hence is at most the sum of the marginal leakages, with equality if and only if the two outputs are also marginally independent (I(Y_S; Y_M) = 0); the 95% label applies to the at-most bound there and nowhere else.

The closing sentence on §26 absorption is unchanged.

### Site 4 · papers/v6/privacy_value_v6.md, §16 (inventory :132)

BEFORE:

> The V5.4 results stand with their conditioning stated. In particular, additive leakage I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M) holds exactly in the Precondition-1 regime (no inter-agent channel); the 95% label applies there and nowhere else.

AFTER:

> The V5.4 results stand with their conditioning stated. In particular, in the Precondition-1 regime (no inter-agent channel) the joint leakage satisfies I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M) − I(Y_S; Y_M), hence is at most the sum of the marginal leakages, with equality if and only if the two outputs are also marginally independent (I(Y_S; Y_M) = 0); the 95% label applies to the at-most bound there and nowhere else.

### Site 5 · papers/v6/dualprivacy_researchpaper_v6.md, §2.2 (inventory :30)

BEFORE:

> The additive-leakage result I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M), asserted at 95% in the v4.3 lineage, holds at that confidence inside the non-collusion regime only.

AFTER:

> The additive-leakage result, asserted as the equality I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M) at 95% in the v4.3 lineage, is scoped and corrected: inside the non-collusion regime the joint leakage satisfies I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M) − I(Y_S; Y_M), hence is at most the sum, with equality if and only if the two outputs are also marginally independent, and the 95% label applies to the at-most bound there only.

The sentence keeps the v4.3 lineage attribution as history (the lineage did assert the equality) and states the corrected form as the live claim.

### Site 6 · papers/v6/pvm_v6_compressed.md, separation-bound display (inventory :112; double defect)

BEFORE:

> **Theorem (95%):** Conditional independence $\implies$ additive MI bound $\implies R_{\max} < 1$.

AFTER:

> **Theorem (95%):** Preconditions 1 and 2 $\implies$ the additive MI bound $I(X; Y_S, Y_M) \leq I(X; Y_S) + I(X; Y_M)$ (equality iff additionally $I(Y_S; Y_M) = 0$) and the Fano floor $P_e \geq 1 - R_{\max}$; the strict bound $R_{\max} < 1$ holds exactly when, additionally, the declared capacity-deficit condition $C_S + C_M < H(X)$ holds.

Two defects repaired in one display: (a) the CTR-OBS-01 exact-additivity wording, and (b) the pre-L044 conflation, in which conditional independence alone was displayed as implying R_max < 1. The repaired display follows the L044 decomposition (preconditions give the additive bound and the floor; the strict bound needs the declared capacity-deficit condition in the same passage). The "holds exactly when" in the AFTER text is the capacity-deficit definitional iff, which is the fenced clause class, deliberately present and correct.

### Site 7 · papers/v6/pvm_v6_compressed.md, "Proven Results · scoped" (inventory :235)

BEFORE:

> V6 scoping: Additive leakage $I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M)$ at 95% **inside Precondition 1 only**.

AFTER:

> V6 scoping: Additive leakage bound $I(X; Y_S, Y_M) \leq I(X; Y_S) + I(X; Y_M)$, equality iff additionally $I(Y_S; Y_M) = 0$, at 95% **inside Precondition 1 only**.

The remainder of the line (separation bound and ceiling status; worked drift instances) is unchanged.

### Site 8 · papers/v5/privacy_value_v5_4_formal_specification.md (inventory :634) · FLAGGED, NOT EDITED

The §16 table row at :634 is untouched (superseded artefact; the inventory and L125 both direct a flag, not an edit). The artefact received a non-invasive HTML comment at the document head (renders as nothing) per the historical/superseded flag convention (OBS-GPT56-017):

BEFORE: (no artefact-status flag; file began at the title line)

AFTER (inserted above the title):

> &lt;!-- artefact-status: superseded (historical/superseded flag convention, OBS-GPT56-017; applied 2026-07-10 per CTR-OBS-01 / L125). This V5.4 volume is succeeded by the V6 formal specification (papers/v6/privacy_value_v6_formal_specification.md), which carries the corrected wording. Known pre-correction wording preserved unedited in this artefact: the §16 "Additive MI bounds" table row states exact additivity; the corrected subadditive form (at most the sum, equality iff additionally I(Y_S; Y_M) = 0) lives in the V6 specification §16. This artefact is a historical record and is not edited. --&gt;

### Site 9 · pipeline extractions/E1-amnesia-gap.md, E1-C04 re-issue (L044 pattern)

BEFORE:

> - **STATUS:** Proven-conditional
> - **SOURCE:** spec §16, §14.7
> - **CLAIM:** Additive mutual-information leakage: I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M) holds exactly when the two observation channels are conditionally independent given X and nothing carries the inter-agent residue (Precondition 1). The 95% label of spec §16 applies in that regime and nowhere else. The compounding results (E1-C09, E1-C10) describe the complement of the regime and do not contradict the additive claim; the two are one theorem family on two sides of one architectural line, the line being whether the inter-agent channel exists.
> - **PRECONDITIONS:** Precondition 1 (no inter-agent channel).
> - **CITATIONS:** chain rule for mutual information (Cover & Thomas); scoping stated in spec §16 "Scoped, not lowered".

AFTER:

> - **STATUS:** Proven-conditional (re-issued 2026-07-10 per CTR-OBS-01, L125)
> - **SOURCE:** spec §16, §14.7 (corrected 2026-07-10, CTR-OBS-01/L125 execution)
> - **CLAIM:** Additive mutual-information leakage bound: under Precondition 1 (the two observation channels conditionally independent given X and nothing carrying the inter-agent residue), the joint leakage satisfies I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M) − I(Y_S; Y_M), hence is at most I(X; Y_S) + I(X; Y_M), with equality if and only if additionally the two outputs are marginally independent (I(Y_S; Y_M) = 0). Every downstream ceiling and floor statement uses only the at-most direction, which the redundancy term only tightens. The 95% label of spec §16 applies to the at-most bound in that regime and nowhere else. The compounding results (E1-C09, E1-C10) describe the complement of the regime and do not contradict the bound; the two are one theorem family on two sides of one architectural line, the line being whether the inter-agent channel exists.
> - **PRECONDITIONS:** Precondition 1 (no inter-agent channel); equality additionally requires marginal independence of the outputs.
> - **CITATIONS:** chain rule for mutual information and the interaction identity (Cover & Thomas); scoping stated in spec §16 "Scoped, not lowered" (corrected wording).

FEEDS unchanged (WP-02, WP-07, WP-08, WP-09). Two apparatus additions on the L044 precedent: the frontmatter resweep_note gained "CTR-OBS-01 re-issue pass 2026-07-10 (E1-C04 corrected to the subadditive bound with equality condition, per L125)", and the sweep record gained a CTR-OBS-01 re-issue entry recording that no other E1 claim carried the exact wording (E1-C02 and E1-C08 are BOUND class per the inventory) and that E1-C02's deficit-condition iff is fenced out.

### Site 10 · pipeline rehydrations/grants/grant_edition.md, section 2 (inventory :133)

BEFORE:

> Within Precondition 1, additive mutual-information leakage, I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M), holds exactly when the two observation channels are conditionally independent given X; the compounding results of section 3 describe the complement of this regime and do not contradict it.

AFTER:

> Within Precondition 1, mutual-information leakage is at most additive, I(X; Y_S, Y_M) <= I(X; Y_S) + I(X; Y_M), with equality if and only if the two outputs are also marginally independent; the compounding results of section 3 describe the complement of this regime and do not contradict it.

One sentence only; the [E1-C04: Proven-conditional] marker and every neighbouring sentence unchanged; the artifact stays at P1 (release-draft-v3). The touch is recorded in the apparatus comment block (which is stripped at release), noting the sequencing after the E1-C04 re-issue and the deficit-condition fence in the same section. The section-2 paragraph above it, "The strict bound R_max < 1 holds exactly when, additionally, the capacity-deficit condition C_S + C_M < H(X) holds", is the fenced definitional iff and is untouched.

## The fence, verified

Every "holds exactly when" attached to the capacity-deficit condition C_S + C_M < H(X) is a genuine definitional iff (inventory class iii) and was left intact: spec §10.5 (the capacity-deficit paragraph), spec §16 Reconstruction ceiling row, grant_edition section 2, E1-C02, and the repaired pvm_v6_compressed :112 display, which now carries the clause correctly. No instance of that clause class was modified anywhere in this batch.

## Deliberately not touched, with reasons

- The three awaiting-P4 papers (WP-07, WP-04, WP-27): conformant per L123; hard stop; not opened for writing.
- WP-09, the policy brief (WP-02), all register files, research/CONJECTURE_REGISTER_V6.md: outside the seat's sanction; BOUND-class sites there need nothing per the inventory.
- Spec §10.5 (inventory :426) and privacy_value_v6.md :88: BOUND-leaning ambiguous, fix marked optional in the inventory, and the :430 paragraph carries the fenced deficit iff; minimal-touch discipline held, left unchanged.
- papers/whitepapers/swordsman_mage_whitepaper_v6_3.md :747, COM hearthold/README.md, V5.4-era root skill surfaces, tracker/docs mirrors: canon-adjacent ring; per L123/L125 these ride the standing first-person propagation pass and mirror regeneration (GR-6), not this seat.
- pvm_v6_companion_guide.md: not named in the inventory's EXACT table; not opened.
- No git command was run anywhere (standing rule; diff review is the first person's on landing).

## Reversals

None. One judgement call to surface for the diff review: at Site 5 (dualprivacy) the corrected sentence keeps the v4.3 lineage's equality assertion as attributed history ("asserted as the equality ... in the v4.3 lineage") rather than deleting it, because the sentence's function in §2.2 is to describe what V6 does to the inherited result; the live claim is the at-most bound. If the first person prefers the lineage mention gone, the sentence reduces cleanly.

## Backup manifest

All copies taken to archive/canon-backups-2026-07-10/ BEFORE any edit:

1. privacy_value_v6_formal_specification.md (130,788 bytes)
2. privacy_value_v6.md (26,254 bytes)
3. dualprivacy_researchpaper_v6.md (6,580 bytes)
4. pvm_v6_compressed.md (15,709 bytes)
5. privacy_value_v5_4_formal_specification.md (56,631 bytes)
6. E1-amnesia-gap.md (39,869 bytes)
7. grant_edition.md (44,183 bytes)

## Check record

Pipeline files, all four checks with explicit paths:

- E1-amnesia-gap.md: figures_fence PASS · register_refs PASS · tier_vocab PASS · versions FAIL with 3 findings (:44 retired citation Research Paper v4.2; :121 and :261 GR-7 static-ceiling in paragraph). All three verified PRE-EXISTING: the identical finding set, same lines, reproduces on the pre-edit backup (the known L033-class FAIL). No new findings.
- grant_edition.md: figures_fence PASS · register_refs PASS · tier_vocab PASS · versions PASS.

Canon files, check_versions.py each, with the pre-edit backup run as the pre-existence control:

- privacy_value_v6_formal_specification.md: FAIL, 8 findings (retired v4.2 citation :774; six GR-7 paragraph findings; version-field reconcile :6). Identical set on the backup. Pre-existing, recorded not fixed.
- privacy_value_v6.md: FAIL, 1 finding (version-field reconcile :4). Identical on backup. Pre-existing.
- dualprivacy_researchpaper_v6.md: FAIL, 2 findings (retired v4.0 and v4.2 citations :20). Identical on backup. Pre-existing.
- pvm_v6_compressed.md: FAIL, 1 finding (GR-7 paragraph :76). Identical on backup. Pre-existing.
- privacy_value_v5_4_formal_specification.md: FAIL, 14 findings (retired citation; eleven GR-7 instances; two version-field reconciles). Identical set on the backup with every line anchor shifted by exactly +2, the two lines of the inserted head flag. Pre-existing; consistent with the artefact's superseded status, which the new flag now declares.

Net check delta of the batch: zero new findings on any file.

## Handoff

- WP-03 (grant_edition): one-sentence inheritance fix landed; artifact remains at P1, chain complete. Next action: none for the runtime; first-person diff review on landing (L125).
- E1: E1-C04 re-issued; downstream consumers (WP-02, WP-07, WP-08, WP-09) already carry BOUND-class wording per the inventory and need no re-issue. Next action: A9's next weekly sweep confirms no consumer drift.
- Canon: seven edits across four V6 files landed; V5.4 spec flagged superseded, not edited. Next action: first-person diff review against archive/canon-backups-2026-07-10/; then mirror regeneration (tracker/docs HTML) per GR-6 rides the standing item.
- Open question for the first person: whether the two optional BOUND-leaning sites (spec §10.5 "the additive capacity sum ... hold", privacy_value_v6.md :88) should take the one-word hygiene tightening on a future ruled card; left untouched here by the inventory's own classification.
- Blocked/none: C-series minting for CTR-OBS-01/02 remains the first person's and was not exercised (protocol rule 4).
- Proposed ledger entry returned to A0 in the seat's final message for serialisation (ledger is append-only; A0 serialises this batch per L125).
