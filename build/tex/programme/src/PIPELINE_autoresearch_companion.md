---
title: "How These Documents Were Made: a Role-Separated Agent Pipeline with a Non-Delegable Completion Gate, and its Adversarial Autoresearch Loops"
subtitle: "tier internal · 2026-08-17 · status draft-v1"
author: "The Privacy-is-Value Research Programme"
date: "2026-08-17"
---
## 1. What the reader is holding

The document set this companion accompanies was not written by a single author in a single sitting. It was produced by a pipeline of role-separated agent sessions operating under written ground rules, with every claim traced to an extraction line, every draft passed through adversarial review, and a final completion gate that no agent is permitted to mark. This companion explains that machinery: the roles, the gates, the checks, the memory surfaces, and the two adversarial literature-review runtimes whose outputs bound the novelty claims of the WEIS paper (WP-14).

The set comprises five tier-A academic artefacts and their supports:

| ID | Artefact | Venue target | State at 2026-08-17 |
|---|---|---|---|
| WP-04 | SoK: The Shelf Life of Privacy Guarantees | HotPETs / FC workshop | awaiting P4 (P0..P3 passed) |
| WP-07 | Sequential Composition of Leakage-Budgeted Agents | PoPETs | awaiting P4 (P0..P3 passed) |
| WP-11 | Compelled Comprehension (RPP adversarial paper) | SOUPS / FC | draft skeleton; prereg + formalism on file; results design-only |
| WP-14 | The Seventh Capital (WEIS paper) | WEIS 2027 | draft-v4; lit-review runs 02 and 03 bound to it |
| WP-27 | Conjecture Governance (the methods paper) | meta-research venue | draft-v3, awaiting P4 |

Supporting artefacts (prior-art scouts WP-11a and the WEIS prior-art map, the empirical valuation methodology, the WP-11 formalism and pre-registration) are internal-tier evidence substrates: they exist so that the tier-A papers never assert what a scout, a formalist, or a methodology rebuild has not first established.

## 2. The pipeline in one view

The V6 Rehydration Pipeline turns a research canon into audience-specific artefacts ("rehydrations") without letting any agent quietly strengthen a claim in transit. Its structural commitments:

1. **Extraction is upstream of everything.** Claim inventories E1..E11 are built from the canon by a dedicated extractor role. A rehydration may consume only claims that appear in an extraction; a claim that cannot be traced to an extraction line is deleted, not defended (GR-9, "trace or delete").
2. **One session, one role.** Fourteen role cards (A0..A13) each carry a mission, permitted reads and writes, a definition of done, and named failure modes. A session boots by reading the ground rules, its role card, and its task card, then states its permissions back before beginning.
3. **Tiered registers.** Every artefact declares a tier: S (standards), A (academic), G (grants), P (public), D (developer). Each tier has hard vocabulary and claim-strength constraints; at tier A, conjectures appear only as formally stated conjectures with proof obligations, and confidence percentages are banned (GR-2).
4. **Shared memory is append-only or single-writer.** The manifest (pipeline state) is writable by the orchestrator A0 alone. The critiques ledger is append-only and any role may write to it. Every session ends by writing a chronicle; a session without a chronicle is unfinished.
5. **The register is the sole authority** for conjecture numbering, confidence, and status (GR-1). Agents never promote a conjecture. If two canon surfaces disagree, the conflict is escalated to the ledger, never resolved locally (GR-10).

### 2.1 The roles

A0 orchestrator · A1 extractor · A2 register-translator · A3 formalist · A4 citation-verifier · A5 adversarial reviewer (with venue-typed sub-personae: crypto programme committee, regulator, grant assessor) · A6 benchmark engineer · A7 voice editor · A8 standards and policy writer · A9 consistency auditor · A10 prior-art scout · A11 mechaniser · A12 economist · A13 standards cartographer.

The separation is doing real work. The role that drafts (A2/A3) never verifies its own citations (A4), never reviews its own draft (A5), and never audits its own consistency (A9). The prior-art scout (A10) establishes novelty before any paper asserts it; the discipline is "novelty established before asserted".

### 2.2 The gates

Every artefact moves through five gates, and the manifest records the last gate passed:

- **P0 extraction fidelity.** A0 spot-traces random claims in the draft back to extraction lines and runs the register-reference check.
- **P1 genre.** An A5 adversarial review appropriate to the venue is on file with no BLOCKING items outstanding.
- **P2 citation.** A4 has verified every external citation against a primary or near-primary record; unverifiable citations are marked, never silently kept.
- **P3 consistency.** Four deterministic checks pass: register-reference hygiene, canonical-figures fence, tier vocabulary, and version/retired-claim hygiene. These are ordinary Python scripts; a non-zero exit names file and line.
- **P4 completion read.** The First Person (the human principal) reads the artefact and decides. No agent marks P4, simulates it, or proceeds past it. Everything in the table above sitting at "awaiting P4" is waiting at that door.

The gate that matters most is the one the machine cannot pass. P4 is non-delegable by construction: the pipeline's own boot file instructs every agent that P4 "cannot be simulated, summarised, or assumed". This is the pipeline's answer to the central hazard of agent-generated research, which is not fabrication but fluent overstatement.

### 2.3 The review loop, concretely

The typical cycle for a tier-A paper, reconstructed from the ledger and chronicles of WP-07 (the PoPETs theory paper):

1. A3 builds the mathematical core (the cap theorem proven under explicit hypotheses; necessity both ways; tightness).
2. A4 verifies the bibliography (60 entries, zero failures) and one import-fidelity defect is fixed.
3. A2 completes the prose sections around the formal core.
4. A5, seated as a crypto programme-committee reviewer, returns MAJOR REVISION: 1 BLOCKING, 4 MAJOR, 8 MINOR findings; the core survives independent re-derivation.
5. A3 repairs the mathematical legs the same day (one proposition gains missing hypotheses; one reviewer suggestion is adopted as a new proposition); A2 revises the prose legs (eleven-item re-alignment of abstract and framing sections to the revised core).
6. A0 re-checks the specific findings and passes P1; A9's check suite passes P3 after a one-sentence fix.
7. The artefact is stamped "awaiting P4" and the runtime touches it no further.

Later, a first-person direction added an erosion leg (background side-information; the cap survives conditioning while the floor erodes), which itself went through a fresh A9 audit and a targeted A5 adversarial review before returning to awaiting-P4. Nothing ships because it is finished; it ships because a named person read it.

## 3. The autoresearch loops

Two kinds of automated research run inside the programme. Both are structured so that the automation cannot flatter the position it serves.

### 3.1 The fleet cycles

Day-to-day production runs as "fleet cycles": a standing A0 session cuts task cards; two or three producer sessions (A2/A3/A6/A8/A12) work one work-package branch each; one A5 session reviews what producers finished the previous cycle; A9 sweeps weekly. The chronicles directory records roughly a hundred such sessions across July 2026, including three-cycle days. Concurrency is bounded deliberately: beyond about five parallel sessions the ledger review becomes the bottleneck, and the design target is that the human principal faces three decisions or fewer per cycle.

### 3.2 The literature-review runtime (run 02, 2026-07-15)

The WEIS paper needed a defensible novelty claim, not a summary. The runtime that produced it (run ID wf_ba400906-67b) enforced three disciplines:

- **D2, no absence-as-novelty.** A gap in the corpus is reported as `not_found_in_corpus(n, scope)`, never as "no prior work does X". Every contribution claim carries a verdict, the corpus tested, and a confidence label.
- **D3, structural isolation.** The prover seat (argues the claim is novel) and the refuter seat (hunts covering prior art) are separate agent invocations with separate contexts; the refuter never sees the prover's argument.
- **D4b, auditable seat separation, honestly limited.** All seats run on the same model weights; the separation is context isolation, not weight diversity. The run manifest states this limit rather than hiding it, and adopts the operating rule that an all-VALIDATED result is treated as a failed enforcement of the adversarial discipline, not a success.

Run 02 tested five novelty candidates against a 20-item corpus plus each seat's independent web scope. The verdict spread was 0 VALIDATED / 5 MIRAGE / 0 BLOCKED: every headline claim was anticipated by named prior art, and what survived in each case was a narrower residual core (for the strongest: pricing a finite, adversary-relative, time-drifting reconstruction bound held as inalienable subject-owned capital, with the value gap decomposed as market-position rent). The gap table's load-bearing empty cell, {system property x market pricing}, was itself adjudicated a corpus-selection artefact once the differential-privacy-markets strand was admitted. The paper's contribution was rewritten to the conjunction of the surviving residues. The all-MIRAGE spread is the evidence the search was adversarial rather than confirmatory.

### 3.3 The residue stress sweep (run 03, 2026-08-17)

Run 02's residues became the claims to defend, so run 03 (run ID wf_af6caf5a-745, run this date) stresses them. Configuration: five sweep seats search independent modalities (WEIS and economics-of-privacy venues; formal preprints; legal and standards scholarship; data-as-labour and data-union literature; shelf-life and erosion literature) with a 2023-2026 window; five refuter seats, one per residue, each instructed to default to finding coverage, receiving the sweep digest but no prover argument (D3 preserved); one judge seat rules SURVIVES / NARROWED / COVERED per residue and assembles the bibliography additions. D2 phrasing is mandatory in every absence report. Outputs land beside run 02's as generated artefacts (run manifest, residue verdicts, bibliography additions) and are never hand-edited.

The run returned 1 COVERED / 4 NARROWED / 0 SURVIVES across the five residues, from 76 sweep items and 74 proposed bibliography additions. The discipline held in both directions: nothing was rubber-stamped (no residue survived unmodified), and the adjudication did not merely repeat run 02 (the Phi/R assessment-unit residue, already flagged thin, was ruled outright COVERED by named governance instruments and is recommended for retirement into its neighbours; the strongest surviving residue is the identification of the measured WTA/WTP floor and the IEEE 7012 proposer inversion as two evaluations of one structural share function, for which the refuter found no game-theoretic treatment anywhere). The judge's restated residuals, the covering art, and the per-residue absence reports are in the run-03 verdict artefact; all of it awaits first-person adjudication before anything changes in WP-14.

### 3.4 The directed strand sweep (run 04, 2026-08-17)

The loop also admits first-person direction. When the human principal identified a missing pole in WP-14's related work (the anti-commodification position: personal data should not be for sale at all, anchored contemporarily by Carissa Véliz and classically by Radin's market-inalienability), run 04 (run ID wf_23f4f7ad-527) swept that strand deliberately: four sweep seats (market-inalienability theory; the Véliz corpus and its reception; collective and group privacy with externality economics; formal precedents for pricing alongside inalienable data), two targeted refuter seats on the joins the new strand exposes, and a judge returning a positioning map, threat verdicts, and per-paper citation placements. Both tested legs returned NARROWED: the priced-quantity-with-non-transferred-records join is already occupied by differential-privacy query pricing, and the pooling remedy is anticipated inside the social-data-externality line itself; the surviving claims were restated accordingly and the concessions written into the paper in the same pass. The strand entered the paper as a fourth standing objection answered by partial vindication rather than rebuttal, which is the honest shape: the architecture agrees with the pole about the stock and disagrees about scoped disclosure.

The sequence 02-then-03-then-04 is the loop this companion exists to name: claim, adversarial adjudication, residue, re-adjudication of the residue on a widened and time-advanced corpus, and directed expansion when a human identifies a blind spot. Each pass either narrows the claim or raises the earned confidence in what remains, and the direction of travel is one-way: claims only ever get narrower under the loop, which is what distinguishes it from a citation search run to decorate a fixed conclusion.

## 4. What the method does and does not guarantee

In keeping with the programme's honesty rule (GR-8), the limits:

- **Same-weights adversariality.** Every seat in the lit-review runtime runs on the same underlying model. Context isolation demonstrably produces disconfirming verdicts (the all-MIRAGE spread), but it is not equivalent to review by cognitively independent experts, and correlated blind spots survive it.
- **Web scope is not the field.** Refuter searches are bounded by what web search surfaces in-session. The runs report their scope; they cannot report what the scope missed. Citation verification (A4) and first-person reading remain the backstop.
- **Checks catch form, reviews catch genre; neither catches truth.** The deterministic checks enforce hygiene (numbering, fences, vocabulary, versions). A5 reviews enforce venue standards. The mathematical cores are re-derived in review, but formal verification (the A11 mechaniser lane) has not yet been run over the tier-A theorems.
- **P4 is a bottleneck by design.** Every tier-A artefact in the table is stopped at the same gate, and the queue at that gate is the cost of making completion non-delegable. The pipeline accepts this cost explicitly.
- **This companion is itself pipeline output.** It was drafted by an agent session at first-person commission, describes the machinery from its own records (ground rules, manifest, ledger, chronicles, run manifests), and carries the same obligation: nothing in it should be read as having passed P4 until the First Person has read it.

## 5. Reading order

For a reader new to the set: this companion first; then WP-27 for the method stated to methods-venue standard; then WP-04 (the SoK) for the field map; then WP-07 (the theory paper) for the formal core; then WP-14 with its literature-review runs 02 and 03 for the economics; then WP-11 with its formalism and pre-registration for the protocol-facing leg. The prior-art artefacts (WP-11a, the WEIS map) are best read beside the papers they fence.
