---
artefact: brief.coding-agent
subject: "Literature-review runtime, oriented to WEIS"
date: 2026-07-14
author: privacymage
register: standards
status: internal
target: coding agent (agentprivacy-harness)
repo: github.com/mitchuski/agentprivacy-harness
source: BGIN_MATSUO_RESEARCH_2026-07-14_clean.md
register_refs: [C17, C81]
defects_in_scope: [D2, D3, D4b]
---

# Brief: build the literature-review runtime

**Objective: extend the existing dual-agent harness into a literature-review runtime that Mitchell can run against the privacy-impact-assessment corpus and the WEIS back catalogue, and whose output is a defensible novelty claim for a WEIS submission, not a summary. You are building the instrument. Mitchell runs the loop.**

*a literature review that only finds agreement has not been run against an adversary.*

---

## 1. Why this exists (context you must not re-derive)

Matsuo, reviewing the work on 2026-07-14, made two calls that define this task.

First, **venue.** The economic contribution belongs at WEIS (Workshop on the Economics of Information Security), not a crypto or ML venue. Everything the runtime extracts is scored against one question: does it help state the *economic* novelty of privacy-as-value.

Second, **the gap.** He asked "what is new" four times and got an answer about why the work matters, not what is new. The field's unit of analysis is **privacy impact to a named subject** (the ISO / PIA tradition). PVM's unit of analysis is a **property of a system**. The runtime's job is to map that boundary precisely enough that the contribution claim survives a programme committee.

This is C17 restated for a literature task: the novelty is architectural and economic, not another privacy metric competing on the subject-impact axis.

---

## 2. What you are building

A runtime configuration on top of the current harness, not a new harness. Deliverables:

1. A corpus loader and a per-paper extraction pass with a fixed schema (Section 4).
2. A dual-agent review loop configured for the hardening constraints in Section 5.
3. Output templates: a gap table, a contribution-claim candidate set, a CTR candidate set, and a bibliography with provenance.
4. Check scripts that fail the run if the hardening constraints are violated.

Mitchell executes the loop and owns all conjecture assignment. You produce candidates and structure, never rulings.

---

## 3. Corpus (inputs)

Two tiers, loaded separately, never merged in the store.

**Tier A, the challenge corpus (what the field already claims):**
- ISO/IEC 29100 (privacy framework)
- ISO/IEC 29134 (privacy impact assessment)
- the privacy-quantification literature: differential privacy, k-anonymity / l-diversity / t-closeness, quantitative information flow, multi-party-computation privacy models
- WEIS back catalogue, filtered to papers pricing privacy or security as an economic quantity

**Tier B, the position corpus (what PVM claims):**
- PVM V5.4 formal specification (the canonical pinned artefact)
- the privacy-is-value root document

Loader requirement: every item carries `source`, `retrieved`, `doi_or_url`, and a `tier`. No item enters the run without provenance. Missing provenance is a hard fail, not a warning.

---

## 4. Per-paper extraction schema

For every Tier A item, both seats extract the same fields independently. The fields are chosen to answer Matsuo's four re-asks mechanically.

```yaml
paper_id: <stable slug>
unit_of_analysis: subject_impact | system_property | both | unclear
dimensionality: single_scalar | multi_dimensional | relational
economic_framing: none | cost_model | incentive_model | market_pricing
adversary_model: explicit | implicit | absent
failure_mode_on_missing_axis: <how, if at all, the metric behaves when one input is zero>
novelty_claim: <the paper's own one-sentence contribution, quoted <=15 words or paraphrased>
overlap_with_pvm: <where it agrees>
divergence_from_pvm: <where it does not>
citation: <full>
```

The two fields that carry the WEIS argument are `unit_of_analysis` and `economic_framing`. The runtime's central finding, if the thesis holds, is that the corpus clusters on `subject_impact` and `cost_model`, and that `system_property` combined with `market_pricing` is sparse or empty. That sparse cell is the contribution. If it is not sparse, the thesis is weaker than assumed and Mitchell needs to know that before February, not after.

---

## 5. Hardening constraints that are load-bearing here

This is a novelty search, so the failure mode is not a bad summary, it is a false claim of newness. Three defects from the taxonomy apply directly and the run must be configured against them.

**D2, statistical overclaiming.** The runtime must never emit "no prior work does X" from absence of evidence in the corpus. Absence is reported as `not_found_in_corpus(n papers, date range)`, never as `novel`. A novelty claim is only ever a candidate, tagged with the corpus it was checked against and a confidence label. Overclaiming novelty is the single thing Matsuo was testing for.

**D3, prompt-only isolation.** Seat separation must be structural, not a prompt instruction. The prover seat (builds the case that PVM is novel) and the delegator seat (builds the case that it is not, that prior art already covers it) must not share context. If your configuration achieves separation by prompt alone, the run is invalid and the check script must fail it.

**D4b, same-model zero-separation.** If both seats run the same model with the same weights, seat separation collapses and the adversarial review is theatre. Configure distinct seats such that the delegator has genuine independent capacity to find prior art the prover missed. Record the seat configuration in the run manifest so separation is auditable.

Verdict lexicon is preserved: each novelty candidate resolves to VALIDATED (survived the delegator's prior-art search), MIRAGE (the delegator found covering prior art), or BLOCKED (insufficient corpus to decide). MIRAGE is the valuable verdict here. A run that returns all VALIDATED has almost certainly failed D2, not succeeded.

---

## 6. Outputs

Four files, standards register throughout, UK spelling, no em-dashes, confidence labels on every speculative line.

1. `gap_table.md`, the corpus clustered on the schema fields, with the `system_property` x `market_pricing` cell called out.
2. `contribution_claims.md`, three to five one-sentence novelty candidates, each with its verdict, the corpus it was tested against, and a confidence percentage. The current best candidate to seed the run:
   > privacy impact assessment measures impact to a named subject after the fact by survey; PVM bounds it in advance architecturally, where R is a per-subject reconstruction bound and Phi is the system property that gates R. (confidence 70%)
3. `ctr_candidates.md`, proposed conjectures in CTR-series form only. Never C-series. Assignment is Mitchell's.
4. `bibliography.md`, full citations with provenance, ready for the WEIS submission.

---

## 7. Hold-back (C81, existence-leak discipline)

The Privacy Pools V2 constraint-reduction result does not enter this runtime and does not appear in any output. It is unverified, it is a feasibility disclosure, and publishing it leaks an upper bound on difficulty independent of method-hiding (C81, ~70%). If the loop surfaces it from Mitchell's own notes, quarantine it and flag it, do not fold it into the WEIS argument. That result travels on its own reproduction track, not this one.

Equally: the runtime states novelty candidates, it does not state that a novel result exists. "A theorem-shaped result survived the review" is itself an existence-leak against the work and must be pulled back to the specific, checked claim.

---

## 8. Acceptance criteria

The build is done when:

- a run against a seeded five-paper subset produces a populated gap table with no missing-provenance entries
- at least one novelty candidate returns MIRAGE on the seed set (proves the delegator seat is actually adversarial; if nothing can be knocked down, D2/D3/D4b are not really enforced)
- the check scripts fail a deliberately mis-configured run: prompt-only isolation, same-model seats, and an absence-as-novelty claim must each trip a script
- every output file carries a pipeline header block and passes the register and version-hygiene checks
- no output references the Privacy Pools result

---

## 9. Out of scope

Do not touch the model itself, the PVM axioms, or the verdict lexicon. Do not attempt the formal literature review's conclusions: the runtime structures the evidence, Mitchell writes the review and owns every claim of novelty. Do not assign conjecture IDs. Do not draft the WEIS paper.

---

*build the instrument so the delegator can win; a review Mitchell cannot lose is one he did not run.*
