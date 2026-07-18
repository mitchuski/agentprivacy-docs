---
date: 2026-07-09
role: A10
wps: [WP-04]
extractions: []
register_head: C96
ledger_entries: []   # entry proposed to A0 in the seat report, not appended (per card)
---

# A10 prior-art row refresh: WP-04_prior_art.md reconciled with the A4-verified metadata (L093(b))

**Verdict first.** All rows of `reviews/WP-04_prior_art.md` are now reconciled with the A4-verified metadata of the citation stations (L070, L085 and addenda on tasks/WP-04_A4.md) and the L091 referee-grade read. Thirteen rows edited, metadata only: four corrections of wrong or retargeted metadata (Chevignard-Fouque-Schrottenloher CRYPTO 2024 to CRYPTO 2025 with pages and DOI, section 5; ecdsa.fail operator Layr Labs to Eigen Labs, section 5; the Mosca-Piani row retargeted so the sharpest-shift claim sits with the 2025 edition cited directly, section 2; Haines et al. author order to Haines, Mosaheb, Mueller, Pryvalov, section 7), two resolutions of unverified residues (Kagai, Branch, But, Allen entered on the Telecom row with the AUTHORS UNVERIFIED flag cleared and the L091 engagement recorded, section 1; FEDS 2025-093 authors Mascelli and Rodden entered with DOI, section 1), and seven verified-bib enrichments (full author lists for Erlich 2018 and Jain 2023; page or volume completions for Garg, Moran, Roetteler, Erlich, Rocher, Unruh, Haines). A dated refresh note stands in the header block; the sweep-count postscript carries a dated update rather than a rewritten history. No re-sweep, no work added or removed, no verdict or relation changed, novelty ledger N1-N7/S1-S6 untouched, the A3 annotation beneath N7 untouched. Four checks run with the explicit file path, PASS x4, non-vacuous; the former check_versions :62 false positive (L091(d)) confirmed fixed on this file. Ledger entry proposed in the report to A0; this seat appended nothing.

## Stations

1. **Boot.** CLAUDE.md, GROUND_RULES.md, role card A10, task card PRIORART_A10_refresh_2026-07-09. Scope confirmed: metadata refresh only, per the A9 P3 observation L093(b).

2. **Source assembly.** Verified metadata taken exclusively from the on-disk record: the A4 verification note and both addenda (tasks/WP-04_A4.md), chronicles 2026-07-07_a4-wp07-citation-pass.md and 2026-07-09_a4-wp04-citation-pass.md, the L062(d) sweep chronicle 2026-07-09_l062d-kagai-sweep.md, the ledger entries L085 through L093, and pv_v6.bib's verified entries (each carries its A4 verification comment). No web fetch was made or needed; every edited datum traces to one of these records.

3. **Diff and edit.** Each row diffed against the record. The four known stale items on the card all verified stale and corrected. Two further wrong-or-caveated items found in the diff and corrected on the same authority (Haines author order, an L070 correction the card's inputs section names; the FEDS row's author-list caveat, resolved by the Crossref DOI record at the A4 station). The A4 record's seven page-range and author-list enrichments applied where the rows lacked them, each read off the corresponding pv_v6.bib entry. Rows edited carry a short provenance clause where the change corrects an error or clears a flag; pure enrichments carry none.

4. **Mosca-Piani retarget judgement.** The row already attributed the sharpest 10-year shift to the 2025 edition in its result column while citing only the 2024 report; per the card's item 3 and the L085(a) retarget executed in the draft, the citation cell now names both editions with their edition and survey particulars (2024 sixth edition, 32 experts; 2025 seventh edition, 26 experts, GRI page posted 2026-03-09) and the result column states which edition carries which claim, mirroring the retargeted draft sentence.

5. **Header and postscript.** Dated refresh note added beneath the title recording every change class and its verification authority; frontmatter status line extended. The sweep-count postscript was not rewritten: the original statement stands and a dated update beneath it records the Telecom resolution, the count at 41, and the L091 ancillary finding confining the unread-neighbour risk to the one ResearchGate preprint.

6. **Checks.** From `checks/`, all four scripts run with the explicit path `../reviews/WP-04_prior_art.md`: versions PASS, register_refs PASS, tier_vocab PASS, figures_fence PASS, exit 0 x4, non-vacuous (L082 discipline). check_versions PASS confirms the :62 "r <1450" false positive fixed this cycle, as the card anticipated; a FAIL would have been a regression and none occurred.

## Reversals and judgement calls recorded

- **Enrichment scope widened, deliberately.** The card names four stale items; the method line instructs a full diff. The diff surfaced the Haines order and FEDS caveat (wrong or caveated, clearly in scope) and the seven bib enrichments (incomplete, not wrong). Decision: apply the enrichments too, because the task's objective is reconciliation with the A4-verified metadata and each enrichment is read off a verified bib entry; recorded here so A0 can reverse the widening if it exceeds the intended diff.
- **Postscript handling.** First instinct was to rewrite the sweep-count sentence in place; rejected as rewriting the 2026-07-07 record. A dated update block appended instead, matching the annotation pattern A3 used beneath N7.
- **Left alone on purpose:** the section 1 ResearchGate row (still UNVERIFIED, correctly); the Babbush row's "posted 2026-03-30/31" (A4 finding 4 rules either reading defensible and the sweep's wording is the carried form); the Naether row (title form consistent with the bib record); every verdict, relation and unclaimed column; N1-N7, S1-S6, and the A3 annotation.
- **No row unreconcilable.** Every datum needed was present in the on-disk record; nothing was guessed.

## Handoff

- **WP-04, single next action:** A0 receives the seat report with the proposed ledger entry (this closes the L093(b) weekly-sweep item for the prior-art rows); WP-04 itself remains awaiting-P4 and was not touched.
- **Open question:** whether A0 ratifies the enrichment-scope widening (reversal 1) or trims the seven enrichment edits back; either reading of the card is defensible.
- **Blocked:** nothing. No canon, manifest, tracker, ledger, or draft touch; no git commands; no web fetches.
