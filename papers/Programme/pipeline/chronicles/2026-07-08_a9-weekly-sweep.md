---
date: 2026-07-08
role: A9
wps: [WP-04, WP-07, WP-13]
extractions: [E1, E2]
register_head: C96
ledger_entries: []
---

# A9 session · weekly consistency sweep · academic drafts enter the suite

## Verdict

The suite is green with two minor findings and one known tension. The two academic drafts (moving_ceiling_sok.md at draft-v2, linear_cap_paper.md at draft-v1) entered the weekly sweep for the first time and both pass all four deterministic checks. The four checks pass on all seven rehydrations and on E2; E1 fails check_versions with exactly the three findings of the standing L033 tension (extractions quote the canon faithfully, including its retired citations and unconditioned conjecture statements), recorded and not fixed. Theorem numbering is internally consistent in both drafts; every trace marker in both trace maps resolves to an existing claim in E1 (C01 to C40) or E2 (C01 to C15); the WP-04/WP-07 notation divergence remains confined to notation per L069(c). Register head triple-agrees at C96 (register, manifest, check HEAD). The two findings: WP-07's frontmatter extraction_basis omits E1-c12, which its trace map uses for Definition 3.8 and Conjecture 5.8; and the AgentLeak model descriptor diverges across surfaces ("five production LLMs" in WP-07 per the L070 verified record, "five frontier models" in WP-04, both extractions, and the canon spec itself, making the root CANON-LEVEL). Nothing was fixed; two proposed ledger entries were returned to A0. WP-07's stub sections 0-2 and 6-7 were in flight with A2 and excluded from audit; no check failure traced to an in-flight edit.

## Scope and constraints

Session overrides from A0: fix nothing; canon read-only; manifest A0-only; no ledger append (A0 serialises; proposed entries in the report); no git operations; no tracker regeneration (GR-6). Audit scope for linear_cap_paper.md was its theory core (sections 3 to 5), frontmatter, and trace map only, since A2 may concurrently be filling the stubbed sections (abstract, 1-2, 6-7); at read time (file mtime 2026-07-08 22:39) the stubs were still stubs, so A2's fills had not landed during this sweep.

## Path

1. Boot per CLAUDE.md: ground rules, role card, task card. Ledger read in full; head at L072.
2. First check invocation was a no-op (the checks take explicit file paths; zero files scanned, exit 0). Re-run correctly over the nine-file suite: all seven rehydrations/*.md plus both extractions. Recorded as a reversal so the empty first run is not mistaken for evidence.
3. Deterministic checks, run of record (python, checks/ as cwd): check_register_refs exit 0 (9/9 PASS); check_tier_vocab exit 0 (9/9 PASS); check_figures_fence exit 0 (9/9 PASS); check_versions exit 1, sole failure E1-amnesia-gap.md with 3 findings (:42 retired citation "Research Paper v4.2"; :119 and :259 static-ceiling without in-paragraph conditioning). All seven rehydrations, including both academic drafts, pass 4/4.
4. Known-tension registry: the E1 versions failure is the standing extraction-versus-check tension filed at L033 (the task card's L024 reference; L024 itself was the check-pattern defect, resolved at L032). Line drift from the 2026-07-02 run (:39/:116/:256 to :42/:119/:259) matches the E1 frontmatter and maintenance-note growth of 2026-07-07; same three findings, same class (faithful quotes: E1-C03's CITATIONS line quoting spec §16; E1-C14 and the ceilings-independence claim carrying "reconstruction ceiling" in conjecture wording). Recorded, not fixed.
5. Register head: research/CONJECTURE_REGISTER_V6.md line 5 (C96, next free C97), manifest register_head (C96), check_register_refs.py HEAD (96). Triple agreement; no drift.
6. WP-07 theory core: numbering sequence 3.1-3.8, 4.1-4.3, 5.1-5.8 sequential and internally consistent; all internal cross-references (ER-1 to ER-7, propositions cited from Remark 5.7 and section 5.4) resolve. The L070 import-fidelity fix is present (Theorem 4.1 carries both source hypotheses). Trace map: every cited E1/E2 claim ID exists; exclusions (E1-c40 per L065(d), E1-c07/c13-c26/c30-c35, E1-c39) are recorded decisions, consistent with the extraction FEEDS state after the 2026-07-07 A1 touch.
7. Finding 1: frontmatter extraction_basis lists E1 c01-c06, c08-c10 and E2 c01/c02/c11/c12, but the trace map uses E1-c12 (Conjecture-C86) for Definition 3.8 and Conjecture 5.8. E1-C12 exists and FEEDS WP-07, so the trace resolves; the frontmatter list is the incomplete surface. Present since A3's draft-v1, not an in-flight artefact.
8. WP-04: numbering (Proposition 1, Definition 2, Remark 1, Definition 3, Lemma 1, Conjectures 1-4) consistent; the absent "Definition 1" is a documented A8 port-time renumbering note, not a defect. All 15 E2 claims consumed at their extraction status; E2-C06 appears as prohibition only, no price figure anywhere; conjecture confidences carried qualitatively (TIER-A discipline held). Cross-references into WP-07 (Theorem 3.2, Remark 3.4, Definition 3.8) all name real objects.
9. Notation divergence per L069(c): verified still notation-only. C_S/C_M as declared budgets (WP-07 ER-5/ER-6) versus class-relative effective capacities (WP-04 Definition 3); R(t) and t* formulas identical; Fano floor in the exact form with the alphabet-entropy hypothesis in both; the decomposition discipline (preconditions license additivity and floor; declared deficit licenses the strict bound; the deficit expires) word-consistent across both drafts. WP-07's ER-6 defers the ordered-family formalisation to WP-04's section 4, so the two definitional routes are complementary, not conflicting. The absent sup-semantics caveat at WP-07 Remark 3.4 is the already-filed L069(b) flag riding with WP-07's next touch; not re-filed.
10. Finding 2: AgentLeak model descriptor. L070(2)/L072 established the verified wording "production LLMs" and WP-07 Definition 3.6 carries it. WP-04 section 5.9 says "five frontier models"; E1-C10 and E2-C12 say the same; and the canon spec carries "five frontier models" at :1161 and :1406 while its own :677 names the five models (GPT-4o, GPT-4o-mini, Claude 3.5 Sonnet, Mistral Large, Llama 3.3 70B). The extractions are faithful to the canon, so the root is CANON-LEVEL (GR-10) with rehydration and extraction legs following the ruling.
11. Status coherence: WP-04 manifest (draft-v2, gate P0) = frontmatter (draft-v2) = tracker board (draft-v2, P0). WP-07 manifest (draft-v1, gate P0 marked 2026-07-08 22:31) = frontmatter (sections-3-5-draft-v1, compatible); tracker board shows draft-v1 with gate blank, stale by one gate because the board was built 2026-07-07 22:27, before the P0 mark. Expected staleness; A0 rebuilds at cycle close per GR-6; recorded as-is, not filed. Process observation, not a finding: both drafts' frontmatter gate_target/handoff lines reflect their producing session and now sit one station behind the manifest (WP-04's "handoff: A0 spot-trace" discharged at L069; WP-07's "handoff: A5-crypto-pc" while the manifest routes A2 first); the manifest owns state, so no defect, but A0 may wish to rule whether handoff lines update at gate marks.

## Reversals and dead ends

1. The first check run passed vacuously (no file arguments); caught by the absence of PASS lines and re-run over the enumerated suite. The second run is the run of record.
2. An initial reading took the E1 versions failure as matching the task card's "L024 tension" label at face value; the ledger shows L024 was the pattern defect (resolved at L032) and the standing extraction tension is L033. The card's label is recorded as shorthand; the operative entry is L033.

## Handoff

- **WP-13 (standing sweep):** suite green apart from the two minor findings and the standing L033 tension. Next A9 run re-verifies the WP-07 frontmatter after A2's fills land, and sweeps A2's completed sections 0-2/6-7 for the first time.
- **WP-07:** finding 1 (extraction_basis omits E1-c12) to A3, or to A2 in passing during the in-flight fill, at A0's routing. L069(b) sup-semantics caveat still open, rides with the same touch.
- **WP-04:** finding 2's rehydration leg (section 5.9 "frontier models" to the verified descriptor) lands naturally at the A4 citation station, already the manifest's next action.
- **Canon:** finding 2's root (spec :1161/:1406 "five frontier models" against the verified record and the spec's own :677 model list) is a register-process item; extraction legs (E1-C10, E2-C12) follow the ruling via A1.
- Open question for A0: whether draft frontmatter handoff lines should be updated at gate marks or remain producer-session records; either is workable, but the convention is currently implicit.
- No git operations; nothing committed, staged, or pushed. No file outside chronicles/ was written.
