---
date: 2026-07-09
role: A9
wps: [WP-04, WP-07, WP-13, WP-27]
extractions: [E1, E2, E10]
register_head: C96
ledger_entries: []   # entry proposed to A0 in the seat report, not appended (per card)
---

# A9 session · weekly consistency sweep, cycle 6 · three hardening items independently verified

## Verdict

The suite is green: all four deterministic checks pass on all eight files of the explicit sweep list (the two academic drafts, the policy brief, the three public drafts, the refreshed prior-art review, and the new E10 method-record extraction), 32 check cells, exit 0 across the board, non-vacuous. All three hardening items are VERIFIED independently at this seat: L082(c), each of the four checks invoked with no arguments exits 2 with the loud refusal, none exits 0; L091(d), check_versions passes on WP-04_prior_art.md with the "or <1450" trigger text still present in the file (now line 64 after the A10 refresh), and a synthetic probe carrying an unconditioned "R < 1" paragraph still fails with exactly one GR-7 finding, so the catch is not weakened; L093(b), the A10 refresh landed (header refresh note at prior_art:13) and the three spot-checked rows agree with the A4-verified record in every particular (Chevignard venue CRYPTO 2025 with pages and DOI at :62; ecdsa.fail operator Eigen Labs with the Layr Labs explanation at :67; Kagai row with the full Crossref author list, DOI, and the AUTHORS UNVERIFIED residue cleared at :27). Cross-document consistency post-churn holds: the WP-04/WP-07 notation divergence remains deliberate and confined to notation per L069(c), disclosed in WP-04's own apparatus at :117; every trace marker in both papers resolves (WP-07's consumed set matches its extraction_basis and its five non-basis E1 markers all sit in the recorded-exclusions block; WP-04 consumes exactly E2-C01..C15); register head triple-agrees at C96 (register :5, manifest :4, check HEAD constant). E10 enters the sweep clean: frontmatter well-formed at a recognised tier, claims E10-C01..C18 monotone with no gaps, every FEEDS line resolves to WP-27 (manifest :56, pending), and no tier breach since canon vocabulary is permitted upstream at tier internal. Last cycle's finding 1 is confirmed addressed (WP-07 extraction_basis now lists c12). Two minor non-blocking findings, both in apparatus surfaces owned by A0, are filed below and fixed by no one at this seat. The known E1-versus-check_versions tension (operative entry L033) is not in this cycle's explicit list; its standing state was recorded out of band and is unchanged (same three findings at :42/:119/:259). Nothing was fixed; one proposed ledger entry returns to A0.

## Scope and constraints

Session constraints from A0: fix nothing; canon read-only; both TIER-A papers at awaiting-P4, read-only; manifest, critiques_ledger append, and tracker untouched; no git. The concurrently drafted rehydrations/grants/grant_edition.md is out of this sweep by instruction and was not read; only its ledger entry (L097) was read in the ledger pass. The GR-7 probe used a scratch file outside the pipeline tree and was deleted after use.

## Check matrix (run of record)

Run from `checks/` with the explicit eight-file list; python, one invocation per check.

| File | register_refs | tier_vocab | figures_fence | versions |
|---|---|---|---|---|
| rehydrations/academic/moving_ceiling_sok.md | PASS | PASS | PASS | PASS |
| rehydrations/academic/linear_cap_paper.md | PASS | PASS | PASS | PASS |
| rehydrations/policy/enforceable_by_architecture.md | PASS | PASS | PASS | PASS |
| rehydrations/public/the_moving_ceiling.md | PASS | PASS | PASS | PASS |
| rehydrations/public/the_uncarved_date.md | PASS | PASS | PASS | PASS |
| rehydrations/public/competence_without_history.md | PASS | PASS | PASS | PASS |
| reviews/WP-04_prior_art.md | PASS | PASS | PASS | PASS |
| extractions/E10-method-record.md | PASS | PASS | PASS | PASS |

Exit codes 0, 0, 0, 0. Supplementary invocations: the four argv-less runs (exit 2 each, refusal on stderr); check_versions on the synthetic probe (exit 1, one finding, gr7_probe.md:7); check_versions on E1-amnesia-gap.md for the tension registry (exit 1, three findings, :42/:119/:259, unchanged from cycle 5).

## Hardening verification (independent, this seat)

1. **L082(c) argv-less guard: VERIFIED.** All four entrypoints call `require_paths` (checks/_common.py:22-27); invoked with no arguments, each printed `ERROR · no input files given; a pathless run proves nothing (L082)` to stderr and exited 2. None exited 0. The console rendered the interpunct as a replacement glyph under the Windows codepage; the byte in source is the interpunct, not a defect.
2. **L091(d) \bR\b STATIC split: VERIFIED, both arms.** The R-arm in check_versions.py:11 is word-bounded, case-sensitive, and refuses digit runs (`(?!\d)`); the ceiling arm stays case-insensitive. Positive arm: check_versions on reviews/WP-04_prior_art.md PASSes while the former false-positive trigger "or <1450" remains in the file at :64 (line drift from the card's :62 is the A10 refresh, verified benign). Negative arm: a synthetic probe file (scratchpad, outside the tree, deleted after) containing an unconditioned "R < 1" paragraph FAILed with exactly one GR-7 finding at the offending line and no finding on the control paragraph.
3. **L093(b) prior-art refresh landed: VERIFIED.** Dated A10 refresh note present in the header block (prior_art:13). Spot-checks against the A4 record (tasks/WP-04_A4.md; chronicles 2026-07-07_a4-wp07-citation-pass.md and 2026-07-09_a4-wp04-citation-pass.md): Chevignard-Fouque-Schrottenloher row (:62) carries CRYPTO 2025, pp. 384-415, doi:10.1007/978-3-032-01878-6_13 with the correction provenance, agreeing with the DBLP/Crossref record; ecdsa.fail row (:67) carries Eigen Labs with Layr Labs identified as the same company's GitHub organisation, agreeing with the site self-description record; Kagai row (:27) carries the full author list (Kagai, Branch, But, Allen), Telecom 6(4):100, the DOI, and the RESOLVED clause clearing the original AUTHORS UNVERIFIED flag with the L070(3)/L091 provenance. The sweep-count postscript update (:145) records the count at 41 with the sole UNVERIFIED item confined to the ResearchGate preprint, matching the L091 ancillary finding. The A3 annotation beneath N7 (:130) stands unedited as L095 requires.

## Path

1. Boot per CLAUDE.md: ground rules, role card, task card. Ledger read to head (L097); L095 confirms A0's application of the hardening fixes and names this seat's verification as the closing condition; L096 registers E10; L097 records the concurrent WP-03 draft, which stayed out of this sweep.
2. Register head verified before any check ran: register :5 (C96, next free C97), manifest :4 (C96), check_register_refs.py:7 (HEAD = 96). Triple agreement.
3. The four checks over the explicit eight-file list, then the three hardening verifications, in that order (matrix and verdicts above).
4. Cross-document pass. Trace markers enumerated mechanically from both papers: WP-07 consumes E1 c01-c06, c08-c10, c12 and E2 c01/c02/c04/c11/c12, matching its extraction_basis (:11-15) exactly; its remaining E1 markers (c36/c37 lineage acknowledgement :443; c40, c07/c13-c26/c30-c35, c39 exclusions :492-499) are recorded decisions in the trace appendix, not silent consumption. WP-04 consumes E2-C01..C15 exactly, C06 as prohibition per its extraction_basis (:12). All markers resolve against E1's forty claims and E2's fifteen.
5. Notation divergence per L069(c): still notation-only and now self-documenting; WP-04's apparatus block (:117) states the C_S/C_M split (WP-07 declared budgets ER-5/ER-6; WP-04 class-relative effective capacities, Definition 3). R(t) = (C_S(t) + C_M(t))/H(X) and t* = sup{t : R(t) < 1} are character-identical across both papers (WP-07 :170; WP-04 :158/:164/:232), and both carry the decomposition discipline (preconditions license additivity and the floor; the declared deficit licenses the strict bound; the deficit expires) in-passage, satisfying GR-7 wherever the strict bound appears.
6. E10 first-sweep. Frontmatter keys complete and well-formed; `tier: internal` is a recognised tier_of value so the checks classify it correctly; claim headers E10-C01 through E10-C18 monotone, no gaps or duplicates; all 18 FEEDS lines name WP-27, which exists in the manifest (:56, status pending, extraction E10); the manifest E10 row (:24, drafted per L096) mirrors the file's coverage statement; SOURCES.md §2 designates process-record as primary for E10 exclusively, and the file's sources list matches the manifest assignment. The in-file STATUS-vocabulary deviation is already ruled ADMITTED for E10 only at L096 serialisation; nothing for this seat to file.
7. Known-tension registry: E1 is not on this cycle's explicit list, so the tension does not appear in the run of record. Recorded out of band for the registry: check_versions on E1 still fails with the same three findings at the same lines as cycle 5 (:42 retired citation; :119/:259 static-ceiling in faithful canon quotes). Operative entry L033 (the card's historical "L024" label was resolved to L033 by last cycle's chronicle); unchanged, not fixed.
8. Cycle-5 finding follow-through: finding 1 (WP-07 extraction_basis omitted E1-c12) is addressed, c12 now listed at linear_cap_paper.md:13. Finding 2 (AgentLeak model descriptor, CANON-LEVEL) rides with the register brief per the L097 rider; not re-filed.
9. Finding F1 (minor, apparatus): WP-07 frontmatter sits two stations behind the manifest. linear_cap_paper.md:6 ends "P3 station L081 ... awaiting A9 re-run", :9-10 carry gate_target/handoff "A9 P3 re-run, then the P4 owner", while manifest :35 has held awaiting-P4 since L082 (2026-07-09). This is exactly the staleness class A0 amended on WP-04 at L093 same-session; WP-07's P3 predates that amendment convention and was never brought level. Non-blocking: the manifest owns state, and the runtime may not touch an awaiting-P4 artifact, so the fix, if any, is A0's to sanction. This also answers half of last cycle's open question: A0 amended WP-04's fields at L093, implying frontmatter does follow gate marks, which makes WP-07's the inconsistent surface.
10. Finding F2 (minor, cosmetic): manifest.yaml note fields for both papers carry duplicated trailing deadline clauses ("FC workshops deadline 2026-09-01" twice at :32; the PoPETs Issue 2/Issue 3 clause twice at :35). A0-only file; recorded, not touched.

## Reversals and dead ends

1. None in the check runs: the argv-less discipline held from the first invocation (the explicit file list was assembled before any check ran, so no vacuous first pass occurred this cycle).
2. The card's item 5 names the tension "L024"; carried as shorthand per last cycle's resolution, the operative entry is L033. Not re-litigated.
3. The stderr refusal glyph was momentarily suspect (replacement character in console output); resolved by reading _common.py, the source byte is the interpunct and the rendering is Windows codepage behaviour. Recorded so the glyph is not mistaken for a corrupted string literal by a future sweep.

## Handoff

- **WP-13 (standing sweep):** suite green, 32/32 cells. The three hardening items are verified at this seat; per L095 PROPOSED (b), L082(c) and L091(d) can close, and per PROPOSED (a) the prior-art staleness item leaves the weekly sweep list, all on A0's serialisation of this report. Next A9 run sweeps the grant edition (WP-03 draft-v1, out of scope this cycle) once its chain reaches the P3 station, and picks up the E10 widening pass if the cycle-7 card lands.
- **WP-07:** finding F1 (stale frontmatter status/gate_target/handoff versus manifest awaiting-P4) to A0 for a ruling on whether an awaiting-P4 artifact's pipeline-apparatus frontmatter may be levelled; no runtime action otherwise possible.
- **WP-04:** no findings; the prior-art review is reconciled and green.
- **WP-27/E10:** first sweep clean; nothing owed until the widening pass.
- **A0 housekeeping:** finding F2 (duplicated deadline clauses in manifest notes :32/:35) at A0's convenience.
- No git operations; nothing committed, staged, or pushed. The GR-7 probe scratch file was created outside the pipeline tree and deleted. No file outside chronicles/ was written in the pipeline tree.
