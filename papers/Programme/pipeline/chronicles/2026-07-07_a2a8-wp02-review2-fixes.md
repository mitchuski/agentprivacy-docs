---
date: 2026-07-07
role: A2+A8 (combined revision seat)
wps: [WP-02]
extractions: []
register_head: C96
ledger_entries: []
---

# WP-02 review-2 fixes · A2+A8 revision seat

## Verdict

All five review-2 findings (reviews/WP-02_A5_review2.md, serialised at L064) are resolved at their cited sentences in `rehydrations/policy/enforceable_by_architecture.md`; nothing the review did not cite was reworded in the brief body. The artifact is bumped to release-draft-v6 with a change note in the frontmatter. check_figures_fence PASS, check_register_refs PASS, check_tier_vocab PASS. All body claim markers and the four [per E1-cNN] reference tags are intact; the release strip remains a separate card. Every edit moved in the weaker-claim direction. Handoff to A0 for the targeted re-check of the five findings only (L064(b): no third full review).

## The five fixes, before and after

**1 · MAJOR, measurement vocabulary (fence OPEN per L064(a)).** Three sentences reworded to the declaration frame of section 2.1; the L042 decomposition itself untouched; the no-standardised-methodology caveat lives once, in 2.1, and is not repeated.

- Executive summary: "under stated and auditable preconditions together with one measurable capacity condition" → "... together with one declarable capacity condition".
- Section 2 body: "a capacity-deficit condition that is measurable and declarable for a given system and adversary class" → "a capacity-deficit condition that is declarable for a given system and adversary class".
- Conditions block: heading "**Capacity-deficit condition (measurable and declarable).**" → "**Capacity-deficit condition (declarable).**"; closing clause "it is the quantity a deployer measures and declares" → "it is the quantity a deployer declares and attests; section 2.1 states how the declaration is checked" (a pointer to where the caveat lives, not a repetition of it).

**2 · MINOR 1, t* glosses sup-accurate.** Three glosses reworded so none takes the first-crossing reading; no dependence on E2-c04 introduced (L054 stays open at the register process).

- Section 3: "the horizon up to which the stated guarantee, with its stated adversary class, remains in force" → "the latest time at which the stated guarantee, with its stated adversary class, is still in force".
- Section 3: "R(t) can pass one, with both preconditions intact, once C_S(t) + C_M(t) reaches H(X)" → "... at any time at which C_S(t) + C_M(t) reaches H(X)".
- Recommendation 3: "the horizon t* within which the evaluation is claimed to hold" → "the horizon t* to which the evaluation is claimed to hold".

**3 · MINOR 2, Article 35(3)(a).** Decision-effects element restored with the review's one-clause fix: "... including profiling, and on which decisions with legal or similarly significant effects are based, a data protection impact assessment is already mandatory (Article 35(3)(a))". The review also noted the personal-aspects element in passing; the task card scopes the fix to the decision-effects element and that is all that was added.

**4 · MINOR 3, IEEE 7012 appositive.** The sentence was split. The external fact keeps its marker: "Separately, IEEE 7012-2025 standardises machine-readable personal privacy terms. [Regulatory and standards facts, external-citable]". The capability claim now stands in the brief's own voice, weakened from "can" to "could", under its own marker: "In this brief's reading, such machine-readable terms are a contractual layer a structurally separated agent could sign and honour. [Synthesis; this brief's reading, not a statement of the standard]".

**5 · MINOR 4, stale apparatus note.** The v4 handoff paragraph's claim that the E2-c01 conflation "is carried in the extraction wording of E2-c01 itself ... so it is escalated CANON-LEVEL" is rewritten to the post-resolution state: escalated at v4 (L042/L044), since resolved by the spec correction (L047), first-person approval (L056(1)) and the extraction re-issue with E1-c02 tightened (L052); extraction layer and brief now agree. This clears the standing L052 refresh flag ("A2/A8 refresh at next touch").

## Version and apparatus

- Frontmatter: status → release-draft-v6; date → 2026-07-07; one-line change_note added; gate_target → targeted re-check per L064(b); handoff → A0.
- A v6 paragraph was added at the head of the strip-at-release handoff comment recording the five fixes and, for the re-checker, noting that the v5 claim-source map line "the guarantee wording is UNTOUCHED (L042 stands)" describes v5 and is superseded by the L064(a) rewording. This is apparatus maintenance, not body rewording; leaving it absent would have reproduced exactly the stale-apparatus defect of finding 5.

## Reversals and near-misses

1. **Self-inflicted check failure, caught and fixed.** The first draft of the new apparatus text used uppercase claim identifiers (E2-C04, E2-C01, E1-C02), which check_register_refs reads as register references C4/C1/C2 at TIER-S (three FAIL findings). The L014 lowercase convention exists precisely for this; identifiers lowercased, check returned to PASS. Recorded because the failure mode (apparatus prose re-introducing register-shaped tokens) will recur at every apparatus touch.
2. **One "measurable and declarable" deliberately left in place.** The v4 historical paragraph of the strip-at-release apparatus still reads "a measurable and declarable capacity-deficit condition". It is a contemporaneous record of what v4 did, quoting L042's own prescribed wording; review 2 cited only the three body sentences, the card forbids rewording uncited sentences, and the paragraph strips at release. Left intact and flagged here so the re-checker does not read it as a missed occurrence.
3. **No other reversals.** No fix required weakening beyond what the review prescribed, and no fix tempted a strengthening.

## Checks (run 2026-07-07, after edits)

- check_figures_fence.py on the artifact: PASS (note: the checks are vacuous when run without file arguments; the first argless run returned exit 0 having scanned nothing, and was rerun properly).
- check_register_refs.py: PASS (after the lowercase correction recorded above).
- check_tier_vocab.py: PASS.
- Manual grep for dollar/fiat patterns and 678x / 31,000x / 70:1 / 74x: no matches.
- Marker inventory: 14 body claim markers across 12 lines plus 4 [per E1-cNN] reference-list tags, unchanged; the strip happens at release, not now.

## Proposed ledger entries (A0 to append; this seat does not write the ledger this session)

- L064 status advance: revision executed at release-draft-v6, all five findings resolved at their cited sentences; ready for the targeted re-check per L064(b).
- L052 minor flag closure: the stale E2-c01 apparatus note in WP-02 is refreshed (finding 5); the "A2/A8 refresh at next touch" item can be marked done.

## Handoff

- **Open questions:** none from this seat. The interim t* wording stands until L054 resolves at the register process; if L054 adopts the E2-C04 formalisation, the section 3 glosses may be restored to first-crossing wording under a new card.
- **Blocked items:** none. The release-strip card should not run until the targeted re-check passes.
- **Next action per WP touched:** WP-02 → A0 routes the targeted re-check of the five findings only (no third full review, per L064(b)); on pass, cut the release-strip card against the checklist in the apparatus comment.
