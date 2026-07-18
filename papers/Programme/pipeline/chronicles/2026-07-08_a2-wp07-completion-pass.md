---
date: 2026-07-08
role: A2
wps: [WP-07]
extractions: [E1]
register_head: C96
ledger_entries: []
---

# WP-07 completion pass: the paper is whole, and nothing was strengthened to make it so

## Verdict

`rehydrations/academic/linear_cap_paper.md` is complete: abstract, section 1 (introduction), section 2 (related work), section 6 (threats to validity) and section 7 (conclusion) are filled; all five stub markers are gone; the theory core (sections 3 to 5, gate P0 per L072) is untouched to the character. The frontmatter status line now reads completion-draft-v1. All four deterministic checks pass (register_refs, tier_vocab, figures_fence, versions; exit 0 each). The draft is ready for A5-crypto-pc with A4's verification note on top, per the task card's handoff.

The binding constraints were honoured as written. The abstract presents the central result as a decomposition: the structural requirements license additive accounting and the Fano floor; the strict sub-unity reconstruction bound additionally requires the declared capacity-deficit condition, named as a numerical fact about a system-adversary pair at a stated time and as the component that expires. No earlier abstract was inherited. The introduction is built on exactly the three stub hooks (exponential-to-linear gap; Proposition 4.3 as the formal counterpart of measured inter-agent-channel leakage; the two necessity propositions). Related work covers exactly the stub's citation list; zero new citations were introduced; every key used already resolves in `templates/submission/references/pv_v6.bib` (60 verified entries, A4/L070). Zero confidence percentages anywhere in the new prose. No canon vocabulary.

## What was written, and where honesty governed flow

- **Abstract.** One paragraph, decomposition-first, closing on the expiry of the deficit condition. No numeric figures, no citations. The temptation resisted: "guarantee" language for the cap; the cap is stated as a conditional theorem under auditable requirements.
- **Section 1.** Seven paragraphs plus a five-item contribution list plus organisation. The paraphrase of the imported Theorem 4.1 carries both source hypotheses (the Markov structure and the mutual independence of the sensitive variables) inside the sentence, so the introduction cannot recreate the import-fidelity defect A4 found and A3 fixed (L070(1)). The AgentLeak measurements are stated qualitatively ("dominant share", "substantial fraction") with an explicit pointer to Definition 3.6 for exact figures, so the numbers live in one place and cannot drift. An honesty paragraph states in the introduction itself that every result is conditional, that conformance is per-instance and answered for no system, and that adverse results are reported with equal prominence (GR-8's in-writing obligation, carried in both section 1 and section 6).
- **Section 2.** Seven lead-in-bolded paragraphs matching the stub list in order. The Asif-Amiri positioning follows A4's ORTHOGONAL verdict verbatim in substance: the hypothesis sets of their Theorem 4.1 and our Proposition 4.2 are formally incomparable, neither implying the other, and neither result claims the other's hypotheses. The differential-privacy paragraph explicitly disclaims any DP implication of the ER-5 budgets (different adversaries, different neighbouring relations); the language-based information-flow paragraph explicitly disclaims replacing static enforcement. Both disclaimers cost flow and were kept.
- **Section 6.** Six bolded paragraphs expanding the section 5.4 seed list into prose: conditionality and per-instance conformance; the passive adversary model; leakage versus reconstruction with the deficit's expiry and the GR-7 sentence discipline; import fidelity (traces to the A4 note); statement precision (alphabet-entropy hypothesis, inequality form); the reporting commitment.
- **Section 7.** Three paragraphs: the separation restated at proved strength only; the decomposition discipline as the recommended form for deployed-system guarantees; three open items (per-instance conformance measurement, Conjecture 5.8 with its unstarted first step, active adversaries and side channels). The Conjecture 5.8 time-status sentence is a conditional restatement of section 5.3's own preamble, not an upgrade.
- The PoPETs feasibility read in the apparatus note was treated as decision material and restated nowhere in paper content, per the card.

## Reversals and decisions recorded

- **Section 5.4 was left untouched despite its own grant.** Its parenthetical says "A2 may reframe prose", but this session's instruction declares sections 3 to 5 READ-ONLY at P0. Resolved toward the stricter rule: 5.4 stands as written and section 6 is a prose expansion beside it. The resulting partial duplication is deliberate and resolves at A8 port time, where 5.4 seeds the 06_threats_to_validity template section; flagged in the traceability addendum and the handoff.
- **Section 6 heading kept as "Threats to validity".** The task card calls the section "discussion"; the file's heading and the template mapping (06_threats_to_validity) say otherwise. The heading stayed; the content is the discussion the card asks for, seeded by 5.4.
- **Exact measurement figures excluded from the new sections.** First drafting instinct was to repeat the AgentLeak percentages in the introduction for force. Reversed: qualitative statement plus pointer to Definition 3.6, so the verified figures exist at one audited site only.
- **Two apparatus syncs a step beyond the card's letter, disclosed:** (1) the References section's "(related work stub)" annotations on `millen1987covert`, `sabelfeld2003language`, `dwork2014algorithmic` were stale once section 2 existed and now read "(section 2)"; (2) an A2 traceability addendum was appended inside the existing strip-at-release apparatus comment (GR-9 obligation for the new sections), below and without touching A3's entries.
- **L069(b) could not be discharged this session and is not silently absorbed.** That entry flags Remark 3.4's t* gloss as lacking the sup-semantics caveat "for WP-07's next touch". This was WP-07's next touch, but Remark 3.4 is theory-core text and READ-ONLY to this role at P0. The new sections avoid restating any t* gloss (section 6 references t*_lin only through Corollary 5.4, where the sup form is explicit). The fix belongs to A3 or to an A0-sanctioned core touch; carried in the handoff.

## Findings

- No missing references: every key the stubs required already resolves in pv_v6.bib. Nothing for the chronicle on that head beyond confirmation.
- No tension found between the new prose and the theory core; the one candidate tension (t* gloss, above) is pre-existing and ledgered at L069(b).
- For A3, nothing requiring action beyond L069(b); for A5-crypto-pc, suggested additional attack surface: whether section 2's differential-privacy contrast is drawn tightly enough, and whether the abstract's "auditable" adjective for ER-1 to ER-5 is adequately supported by Remark 5.7's per-requirement audit list (the intent is "testable per instance", which section 6 states).

## Checks

register_refs PASS, tier_vocab PASS, figures_fence PASS, versions PASS on `rehydrations/academic/linear_cap_paper.md`, all exit 0, run 2026-07-08 after the final edit.

## Handoff

- **WP-07, single next action:** A5-crypto-pc review of the completed draft with A4's verification note (tasks/WP-07_A4.md) on top, per L072(b).
- **Open:** L069(b), the Remark 3.4 t* sup-semantics caveat, needs an A3 or A0-sanctioned core touch; the section 5.4 / section 6 duplication resolves at A8 port time (no action before port); venue decision (PoPETs issue 2 versus 3) remains with the first person, decision material in the draft's apparatus note.
- **Blocked:** nothing.

## Addendum (same seat, A0 micro-fix resume, L073)

The frontmatter extraction_basis list omitted E1-c12, which the traceability appendix uses for Definition 3.8 / Conjecture 5.8; c12 added to the E1 list in the existing format, no other edit, theory core untouched. All four checks re-run after the fix: PASS, exit 0 x4.
