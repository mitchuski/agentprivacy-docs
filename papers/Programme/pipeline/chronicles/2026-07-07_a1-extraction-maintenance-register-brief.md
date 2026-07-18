---
date: 2026-07-07
role: A1
wps: [WP-04, WP-07]
extractions: [E1, E2]
register_head: C96
ledger_entries: []  # four entries proposed below; A0 serialises appends this cycle
---

# A1 · Extraction maintenance and the register brief

## Verdict

The cycle 1-2 extraction queue is discharged and the register brief is filed. Three edits: E2-C07 re-issued with its primary attribution (Babbush et al., arXiv:2603.28846 / ePrint 2026/625) and the ~10x stated as a spacetime-volume figure in the claim text (L062(a)); E2-C12's citation of arXiv:2509.14284 annotated verification in flight (L066(a) fallback; the A4 verdict had not landed); E1-C40's FEEDS rerouted from WP-07 to the WP-04 §6 related-work shelf, WP-16 retained, claim text untouched (L065(d)). check_register_refs PASS on both extractions after editing. reviews/REGISTER_BRIEF_2026-07-07.md carries four items in the gate-brief form (C83 adversary-distinction annotation or split; C86 TIER-A carriage note; C82 cross-reference; the v4.3 publisher diff), each with proposed wording, an evidence line, and its P4 revert. Nothing in the register or the canon changed this session.

## Path

Boot per CLAUDE.md; ledger read L061 to L067 in full before touching anything, per the task card's instruction to read the driving entries first.

**E2-C07.** The A10 prior-art sweep (L062) had withdrawn the only literature contest of the ~10x figure precisely because the primary record confirms it as spacetime volume; the edit therefore does two things at once: names the primary record in the claim and the CITATIONS line, and binds the figure to its metric so no downstream repetition can drop it. The episode keeps its spec §25 name (Schrottenloher instance) because downstream trace lines key on it; the attribution correction lives inside the claim, not in a renaming.

**E2-C12.** The card offered two branches: resolve per the A4 verdict on arXiv:2509.14284 if landed, else annotate. reviews/ holds no A4 verdict file and no same-day A4 chronicle exists; A0 confirmed mid-session that the verdict has not landed. The fallback branch was taken: the citation is annotated verification in flight with both ledger pointers (L066(a), and L065(a) which flagged the same paper independently from the WP-07 side) and a not-citable-downstream fence. No guess was made about the paper's status.

**E1-C40.** The reroute changes flow, not content: WP-07's theory draft excluded the C91 reading as not statable at TIER-A without an unclaimed reduction, so the FEEDS expectation pointing there was stale. FEEDS now names WP-04 (limitative/related-work shelf, §6 related-work status at most) and WP-16. Claim text, confidence, edges, and the Band IX fence are untouched.

**Register brief.** Form taken from chronicles/gates/ in the docs corpus (G6 is the nearest exemplar: proposals tabled unnumbered, first-person write-lines, revert stated). Item (a) offers two wording options and recommends the annotation over the split, because the split would rewrite a row the annotation can qualify, and the smaller move is easier to revert. Items (b) and (c) propose notes with no status or confidence change. Item (d) records the one-word diff L063 names, plus a scope note that the same attribution recurs at three further canon sites (v6 formal spec lines 1371 and 1429; v5.4 spec line 961) so a single ruling can cover all four if the first person wishes; the proposal itself stays at L063's scope.

## Reversals

- The session was terminated by a session limit early in the first run; nothing had reached disk. The run restarted from the boot sequence, re-read both extractions from disk before editing, and confirmed with A0 that the A4 verdict on arXiv:2509.14284 remained outstanding. No divergence between the two runs' intended edits was found on re-derivation.
- E1-C09 also cites arXiv:2509.14284, as a load-bearing citation for the Patil et al. composition-analysis sentence. Annotating it was considered and NOT done: the task card names E2-C12 only, and the card's discipline is execute exactly. The site is flagged in both sweep records and in proposed ledger entry (2) below so the A4 verdict resolves both sites in one pass.
- Renaming the E2-C07 episode from "Schrottenloher instance" to an attribution-first label was considered and rejected; downstream artifacts (WP-04 SoK markers, WP-01) trace to the episode name, and the correction belongs inside the claim.

## Proposed ledger entries (A0 serialises; wording ready to paste)

(1) [E2][P0][2026-07-07][A1]
FINDING: L062(a) executed. E2-C07 re-issued: withheld-result announcement attributed to its primary record, Babbush et al. arXiv:2603.28846 / ePrint 2026/625, in claim and CITATIONS; the ~10x stated as a spacetime-volume figure carrying its metric wherever repeated; episode name retained per spec §25. check_register_refs PASS.
EVIDENCE: extractions/E2-moving-ceiling.md E2-C07 + sweep record; reviews/WP-04_prior_art.md; chronicle 2026-07-07_a1-extraction-maintenance-register-brief.md.
PROPOSED: closes the E2-enrichment leg of L062; downstream repetitions of the figure (WP-01, WP-04, WP-22, WP-12) carry the metric at next touch.
STATUS: for A0 to mark.

(2) [E2][P0][2026-07-07][A1]
FINDING: L066(a), A1 leg. E2-C12's CITATIONS line annotates arXiv:2509.14284 verification in flight (A4 verdict pending); not citable downstream until resolved. Same-citation site E1-C09 (load-bearing for the Patil et al. sentence) flagged, deliberately not edited (outside card scope); it takes the same resolution when the verdict lands.
EVIDENCE: extractions/E2-moving-ceiling.md E2-C12; extractions/E1-amnesia-gap.md E1-C09 + sweep records.
PROPOSED: A4 verdict resolves both sites in one pass; A1 executes at next touch.
STATUS: open pending A4.

(3) [E1][P0][2026-07-07][A1]
FINDING: L065(d) executed. E1-C40 FEEDS rerouted: WP-07 removed (theory draft excluded the C91 reading as not TIER-A statable without an unclaimed reduction); WP-04 limitative/related-work shelf (§6 related-work status at most) and WP-16 named. Claim text, register confidence, edges, Band IX fence unchanged.
EVIDENCE: extractions/E1-amnesia-gap.md E1-C40 + sweep record; L065(d).
PROPOSED: closes L065(d); the WP-04 seat notes the shelf feed at its next formal pass.
STATUS: for A0 to mark.

(4) [REGISTER][CANON-LEVEL][2026-07-07][A1]
FINDING: register brief filed at reviews/REGISTER_BRIEF_2026-07-07.md, gate-brief form, four items: (a) C83 adversary-distinction annotation or row split, exact wording options, annotation recommended; (b) C86 first-TIER-A-carriage note, no confidence change; (c) C82 cross-reference note, no status change; (d) v4.3 publisher one-word diff per L063(a), with a scope note listing three further canon sites carrying the same attribution. Each item states its evidence line and P4 revert. PROPOSAL ONLY; register and canon untouched this session.
EVIDENCE: reviews/REGISTER_BRIEF_2026-07-07.md.
PROPOSED: A0 places the brief on the first-person queue (tracker); discharges the register-adjacent legs L065(c) and the canon leg of L063 into a rulable form.
STATUS: open awaiting first-person ruling.

## Handoff

- **Open question:** none for A1; all four brief items await the first person, and the E2-C12 / E1-C09 citation state awaits A4.
- **Blocked:** E1-C09 edit (same-citation site) blocked on the A4 verdict on arXiv:2509.14284, by design.
- **WP-04:** next action for the A3 formal pass: consume E1-C40 at §6 related-work status at most; trace lines to E2-C07 may shift by a citation (primary record now named).
- **WP-07:** next action for A2/A4 on the stubs: no trace change needed for the E1-C40 removal (the draft already excluded it); E2-C07's enriched citation is available if §6 wants the instance.
- **A0:** serialise the four proposed ledger entries; place the register brief on the first-person queue; note both extractions' frontmatter maintenance lines.

## Addendum · same session, A0 micro-task

The A4 verdict landed after the main run closed: arXiv:2509.14284 VERIFIED (Patil, Stengel-Eskin and Bansal, preprint 2025-09-16), and E2-C12's CITATIONS line confirmed correct against spec §26 (ledger L070(2)). Per the one-pass staging recorded in the reversals above, the verification-in-flight annotation on E2-C12 was cleared and replaced with the verified state, E1-C09's same-citation flag was discharged with the same enrichment, both cite-as-preprint, and both sweep records and frontmatter notes were updated to record the resolution; claim texts unchanged. check_register_refs re-run after the edits: E1 PASS, E2 PASS. This addendum supersedes the handoff's blocked item (E1-C09, now resolved) and the open citation state in proposed ledger entry (2), whose STATUS A0 may serialise as resolved by L070(2); the citation is citable downstream as a preprint in both extractions.
