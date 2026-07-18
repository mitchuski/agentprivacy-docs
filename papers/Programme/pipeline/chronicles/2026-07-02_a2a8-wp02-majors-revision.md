---
date: 2026-07-02
role: A2+A8 (combined revision session)
wps: [WP-02]
extractions: [E1, E2]
register_head: C96
ledger_entries: []
---

# WP-02 · MAJOR-items revision · release-draft v5

## Verdict

Release-draft v5 of `rehydrations/policy/enforceable_by_architecture.md` is written and passes all four checks (tier_vocab, register_refs, figures_fence, versions). All four MAJOR weaknesses of A5 review 1 (weaknesses 2 to 5) are resolved; MINOR items 6, 9, 11 and 12 were fixed in passing; MINOR 10 is handled as a release checklist inside the apparatus comment; MINORs 7 and 8 are deliberately not resolved in the artifact (reasons below, one ledger entry proposed). The L042 guarantee wording of v4 was not reopened; the preconditions block, the capacity-deficit block and the section 5 hedge survive intact. No ledger appends were made and the manifest was not touched, per session overrides; entries and the status change are proposed through the final report to A0. The artifact is ready for A5 review 2.

## Path

The session ran as one combined A2+A8 seat: A2's register discipline (traceability, STATUS markers, GR-9) governing what may be said, A8's genre command governing how it reads to a supervisory-authority policy team.

The legal bridge (MAJOR 2) was treated as the load-bearing item because it dictated the thesis, the subtitle and the shape of section 1. The review's diagnosis was accepted in full: the v4 brief hung an architectural guarantee on Article 22, where nothing architectural lives, and ignored Articles 25 and 32, where everything architectural lives. Before writing a word, the relevant provisions were verified against the published GDPR text (2026-07-02): Article 25(1) (measures at the time of the determination of the means; state of the art; data-minimisation principle implemented in an effective manner), Article 32(1) and (2) (ongoing confidentiality of processing systems; unauthorised disclosure or access), Article 22(1) and (3) (the "solely" and "similarly significantly affects" thresholds; the safeguard triad), and Article 35(1), (3)(a) and (7)(d) (DPIA mandatory for systematic and extensive evaluation based on automated processing including profiling; measures envisaged as required content). The AI Act routing facts were verified the same day: Article 40 (harmonised standards, standardisation request, presumption of conformity), Article 43(2) (internal control under Annex VI for most Annex III categories), Article 74 including 74(8) (market surveillance; DPA designation for certain areas). The MCC-AI procurement templates (updated March 2025, non-binding, high-risk and non-high-risk variants) were verified against the Public Buyers Community publication record. Nothing legal was written from memory.

The bridge as now argued: Articles 25 and 32 are the legal home of the measure; Article 22 is the rights outcome. The brief states explicitly what the bound does not decide (the Article 22 thresholds contested for agentic systems) and states the narrower, defensible claim: the guarantee caps what the pipeline can reconstruct, and so constrains the profiling substrate on which an Article 22 decision and its Article 22(3) safeguards would operate. Article 35(7)(d) is named as where the declarations naturally live.

The dichotomy reframe (MAJOR 5) fell out of the same rewrite. The retired thesis sentence ("architecture is the substrate that makes Article 22 rights enforceable rather than nominal") implied that current supervisory enforcement is nominal, in a document addressed to supervisors. v5 frames three complementary enforcement layers (legal, policy, structural) distinguished by failure mode, not rank; the composition statement traces to E1-c27, whose extraction text carries it verbatim ("the layers compose ... rather than compete"). The new thesis places structural separation among the technical measures of Articles 25 and 32 whose guarantee, within declared conditions, holds by construction rather than by continued compliance.

Addressees and instruments (MAJOR 3): section 6 now opens with a routing paragraph stating why routing matters (internal control, not third-party assessment, is the default for Annex III; market surveillance is the post-market checkpoint; procurement binds where conformity assessment does not reach), and each of the four recommendations names who acts and through what: the European standardisation organisations under the Article 40 request and procurement officers via MCC-AI (recommendation 1); harmonised-standards documentation requirements plus guidance to notified bodies and market surveillance authorities, with the Article 40 request commissioning the missing methodology (recommendation 2); market surveillance authorities and DPAs in Article 35(7)(d) DPIA practice (recommendation 3); DPAs and the EDPB reading Article 32(1)(d) interpretively (recommendation 4).

Verification methodology (MAJOR 4): new subsection 2.1 separates design facts from declared quantities. Precondition 1 is attested by a design-time channel inventory (shared processes and memory, storage, logging and observability pipelines, orchestration state, vendor telemetry) audited as technical documentation; C_S, C_M and H(X) are declarations whose presence, named adversary class, arithmetic consistency and inventory support an assessor can check, and whose well-foundedness no assessor can currently check because no standardised capacity-measurement methodology exists. The subsection says so in terms and routes the methodology gap to recommendation 2. Nothing exceeds E1's empirical-external rows: the section 1 measurements are explicitly characterised as the field's measurements of realised leakage, not a capacity-attestation method.

## Reversals and declined moves

- The v3/v4 thesis sentence was retired, not defended. The apparatus comment had marked it "the reusable thesis sentence retained"; review 1 showed it was the artifact's rhetorical defect, and it is gone. Recorded as a reversal of a v3 editorial decision.
- MINOR 7 (t* defined as sup rather than first crossing, ill-behaved unless R(t) is monotone) was NOT fixed in the artifact. The sup-definition is the extraction's own wording (E2-c02, sourced to spec section 5); changing it in a rehydration would launder a definitional correction (GR-6/GR-9) and would also reopen the section 3 guarantee-adjacent wording the task card fences. A ledger entry is proposed instead, routing the refinement to the register process (the E2-c04 formalisation obligation, ordered decoder classes with inclusion, would make R(t) monotone and dissolve the issue).
- MINOR 8 (Precondition 1 not attestable as written) was addressed only as far as extraction support reaches: the formal clause I(Y_S; Y_M | X) = 0, carried in E1-c01's own precondition statement, was added parenthetically to the precondition block, and subsection 2.1 names the inventory surfaces an audit must cover. A full operational test for "residue" does not exist in E1 at TIER-S admissibility and was not invented.
- Considered and declined: adding a fifth recommendation for the measurement methodology. Folded into recommendation 2 instead, keeping the four-recommendation shape the exemplars support.
- Considered and declined: citing the EDPB-EDPS Joint Opinion 1/2026 in the body. It remains apparatus-only (exemplar); the v3 decision not to add it to section 5's sanctioned fact set stands.
- Genre deviation recorded: the v3 rule "one bold lead sentence plus exactly one expansion sentence" per recommendation is relaxed at v5 to accommodate addressee-and-instrument naming; recorded in the apparatus comment.

## Checks

All four checks run with `python` on the finished file, all PASS: tier_vocab, register_refs (zero C-references at TIER-S), figures_fence, versions (no unconditioned static-ceiling statements; every R_max < 1 passage carries its conditioning).

## Handoff

- **WP-02, single next action:** A0 to record draft-v4 to release-draft-v5 in the manifest and hand to A5 for review 2 (full re-review at v5). Due 2026-07-20 per the task card.
- **Open questions:** (1) proposed ledger entry on the t* sup-versus-first-crossing definitional refinement (register process; touches spec section 5 and E2-c02); (2) whether the register process wants an operational "residue" test admissible at TIER-S (would resolve the remainder of review MINOR 8 at a later revision); (3) at release, the checklist in the apparatus comment (strip apparatus, add author/institution and statement of interests) answers review MINOR 10 and needs an owner.
- **Blocked items:** none. No git operations performed; no ledger appends; manifest untouched, all per session overrides.
