---
date: 2026-07-02
role: register-process executor (canon batch, first-person approval per L045)
wps: [WP-03]
extractions: []
register_head: C96
ledger_entries: []
---

# Canon whitepaper batch · L015 to L023 executed

**Verdict: all eight items executed.** `papers/whitepapers/swordsman_mage_whitepaper_v6_3.md` now agrees with `reference/PAPERS_INDEX.md` on version, research-paper pointer and companion references; the six static-ceiling passages carry in-passage GR-7 conditioning (non-collusion, stated adversary class, R(t) time-indexing) with the L044 decomposition applied at the one passage asserting R_max < 1 from architecture alone; the retired sentence family does not survive; the GR-3 figures are in sanctioned formulations or removed. check_versions moved from 8 findings to 1 (the residual is the checker's unconditional header version-field flag; the field now agrees with PAPERS_INDEX). check_figures_fence moved from 12 findings to 9 (the fence flags every occurrence by design; all residuals are sanctioned-form or explained below). No ledger appends, no git operations, no other file touched. Backup untouched at `archive/canon-backups-2026-07-02/`.

## Path

Boot per the pipeline CLAUDE.md: GROUND_RULES, task card `tasks/L003_canon_whitepaper.md`, ledger entries L015 to L024 and L043 to L045, PAPERS_INDEX whitepaper and research-paper entries. Baseline checks run before any edit: check_versions 8 findings, check_figures_fence 12. The exemplar decomposition wording was taken from `rehydrations/policy/enforceable_by_architecture.md` sections 2 and 3 (the L042/L043 restatement): preconditions give additive structure plus the error floor P_e >= 1 - R_max; the strict bound R_max < 1 requires additionally the measurable capacity-deficit condition C_S + C_M < H(X); the deficit is time-indexed and what expires at t* is the deficit condition, not the architecture.

Items 1, 2, 4, 5 were mechanical. Item 3 repointed both retired research-paper identities (metadata v4.2 and body "Dual Privacy Architecture v3.5") to the PAPERS_INDEX pointer `papers/v6/dualprivacy_researchpaper_v6.md`, naming the v4.3 proof body as its base. Item 7 conditioned each of the six passages in place, keeping the jigsaw rhetoric of the :891 section intact; the strict-bound decomposition was applied there. Item 8 kept the figure where the sanctioned formulation fitted the sentence (:208, :577, :1119, :1300, :1851) and removed it where it did not (:264, :325, :403).

## Finding: the VRC spec's internal version contradicts its filename

Item 6 ruled: glob `specs/` for a v3_4 file, revert to v3.3 if absent. No v3_4 file exists; the citation was reverted to v3.3 as ruled, with the disk path cited. But `specs/vrc_promise_protocol_v3_3.md` line 5 reads "**Version 3.4 - V5.1 Forge Integration + Dual Territory Edition**": the document self-identifies as 3.4 under a v3_3 filename, and its content does carry the dual-territory and mana material the whitepaper's descriptor names. The whitepaper's original "v3.4" citation was therefore arguably faithful to the document and unfaithful only to the filename and to SOURCES.md/PAPERS_INDEX (both say v3.3). Executed as ruled; escalated in the final report as a proposed CANON-LEVEL ledger entry per GR-10. The register process should either rename the file and registry rows to v3.4 or correct the spec's internal header; until then the citation matches the registry side.

## Reversals and judgement calls

1. The :891 heading contains the phrase "Reconstruction Ceiling" and a heading is its own paragraph under the checker's blank-line window; conditioning cannot live in prose beside it. Resolved by renaming the heading to "The Reconstruction Ceiling R(t): Information-Theoretic Privacy", which is also the honest V6 name for the object. Not a workaround of the checker: the time index belongs in the name.
2. "Nonexistent in the adversary's information space" (:907) was kept, amended to "that adversary's", binding it to the stated class in the preceding conditioned sentence rather than deleting a load-bearing rhetorical beat.
3. The 6.2 Version History row is backfilled with an explicit "change record not retained" note rather than an invented change list; no new claims.
4. Item 8 at :1851: the dollar pair $10 to $0.14 restates the 70:1 ratio, so removing the figure while keeping the dollars would have hidden, not removed, the claim. The row was instead aligned to the sanctioned formulation and the dollar pair marked indicative.

## Residuals, explained

- check_versions :7 "version field '6.3', reconcile against PAPERS_INDEX": the checker flags every version field unconditionally; the field agrees with PAPERS_INDEX ("body v6.3, V6 edition by note").
- check_figures_fence residuals: :577 (31,000x, sanctioned accessible-volume formulation), :208, :1119, :1300, :1851 (70:1, all now tied to the spellbook-corpus compression-ratio formulation), :599 (74x, conforming per L023), :1863 twice ($47k and $52k, now marked indicative). :1867 is a false positive of the fence regex: "$50k-$500k/year" for ecosystem operators matches the \$5[0-2]k pattern but is not the canonical $47k to $52k figure; not listed in L023; left unedited.
- Out-of-scope observations, not edited, for the register process to weigh: :555 "privacy emerges from mathematical impossibility rather than corporate promises" is an unconditioned impossibility claim outside the six ruled passages and outside the retired family verbatim; :1931 cites Glossary v3.4 where PAPERS_INDEX's reference shelf lists Glossary Master v4.0; body references to Promise Theory Reference v1.0 at :117, :281 and :1759 are historical title strings and were left with the metadata row bumped to v1.5 per L019's scope.

## Handoff

- **WP-03:** batch executed; single next action: first-person diff review of the before/after list in the final report, then A0 clears the WP-03 L003-decision blocker and updates the manifest.
- **Open question (register process):** the VRC spec filename/internal-version contradiction (proposed CANON-LEVEL entry in the final report); the :555 impossibility sentence and the Glossary v3.4 citation as candidate follow-ups.
- **Blocked:** nothing. No ledger appends made from this session; proposed entries travel in the final report.
