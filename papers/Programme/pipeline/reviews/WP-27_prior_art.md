---
wp: WP-27 (methods-paper-conjecture-governance)
artifact: prior-art review (pre-draft novelty map)
role: A10
date: 2026-07-10
tier: A (discipline applied; this is an internal review, not the WP-27 draft)
inputs: [GROUND_RULES.md, CLAUDE.md, extractions/E10-method-record.md, tasks/WP-27_A10_2026-07-10.md, reviews/WP-04_prior_art.md, live web]
status: complete; feeds the WP-27 A2/A3 draft seats (cycle 7)
register_head_at_build: C96
---

# WP-27 · Prior-art sweep and novelty map (the method paper)

**Verdict first.** Every component of the programme's research-governance
method has strong, nameable prior art, and the paper must say so before it is
told so. Pre-registration and registered reports (Chambers; Nosek et al.) own
the analysis-plan-before-data posture; adversarial collaboration (Kahneman and
Klein) and forecasting-tournament calibration (Mellers, Tetlock et al.) own
red-team review with priced disagreement; assurance-case notation (Kelly and
Weaver, GSN) owns structured claim-evidence argument; multi-agent research
pipelines with role separation and agentic peer review (Lu et al., the AI
Scientist; Zhuge et al., Agent-as-a-Judge) own the agent-fleet-with-seats
shape; append-only cryptographically tamper-evident public logs (Laurie,
Langley and Kasper, Certificate Transparency) own the append-only ledger
mechanism; mutation testing (DeMillo, Lipton and Sayward) and checked coverage
(Schuler and Zeller) own the "your checks may check nothing" discipline; and
Domain-Driven Design's ubiquitous language (Evans) and the Stage-Gate model
(Cooper) are the near neighbours the paper's two most distinctive moves invert.
What no found work assembles is the **combination**: a public conjecture
register of numbered, confidence-banded, estimator-attributed conjectures, a
gate ladder terminating in a non-delegable human completion gate that the agent
runtime may not mark or simulate, an append-only verdict-first adversarial
ledger, and a two-register vocabulary discipline with a fixed production
direction, all operated by an agent fleet and earned independently in two
domains. The defensible novelty is the assembly and the two inversions (the
two-register fence and the non-delegable machine-state gate), never any single
instrument. No swept work contradicts an E10 claim; one contrast (the AI
Scientist's automated final review) is the anti-pattern E10-C02 defines itself
against and is filed as a precision note, not a CONTESTED tag.

Method: family-by-family web search with primary-record verification. Every row
below was resolved to a live record (publisher page, Crossref DOI metadata,
arXiv abstract, RFC, or archived scholarly record) this session, except items
explicitly marked UNVERIFIED. Publisher landing pages that block automated
fetch (PNAS 403, APA PsycNet JS shell) were verified through the Crossref DOI
record instead, noted per row. Field order per work: citation · one-line result
· relation to E10 claims · what remains unclaimed. No canon citations; external
literature only.

---

## 1 · Pre-registration, registered reports, analysis-plan-before-data

| Citation | One-line result | Relation to E10 | Unclaimed |
|---|---|---|---|
| C. D. Chambers, Registered Reports format, launched at *Cortex* (2013); format described at the Center for Open Science, "Registered Reports" initiative page (cos.io), stating peer review of the protocol before data collection and in-principle acceptance regardless of outcome; over 300 journals now offer the format. VERIFIED at the COS initiative page (cos.io/initiatives/registered-reports); Chambers listed as chair of the Registered Reports Steering Committee, Cardiff University. A4 station pin (2026-07-10): C. D. Chambers, "Registered Reports: A new publishing initiative at *Cortex*", *Cortex* 49(3):609-610 (2013), doi:10.1016/j.cortex.2012.12.016, VERIFIED via Crossref. | Peer review of the plan before results exist, with acceptance guaranteed independent of whether data support the hypothesis. | Direct ancestor of E10-C08 (pre-registered verdict rules) and the register-before-result posture of E10-C12. | The RR unit is a single study's protocol reviewed once by a journal; it is not a standing, numbered, confidence-banded register of live conjectures governed continuously across a programme, nor is it operated by an agent fleet. |
| B. A. Nosek, C. R. Ebersole, A. C. DeHaven, D. T. Mellor, "The preregistration revolution", *PNAS* 115(11):2600-2606 (2018), doi:10.1073/pnas.1708274114. VERIFIED via Crossref DOI metadata (publisher page returned 403). | Distinguishes prediction from postdiction by committing hypotheses and analysis decisions to a public record before observing outcomes. | Ancestor of E10-C08 (verdict rules fixed in advance, never softened after the fact) and E10-C12 (a register as the sole authority for status). | Preregistration fixes a study's analysis plan; it does not price severities in advance (BLOCKING/MAJOR/MINOR), rule on its own successor criterion, or bind an automated review loop. The "what-satisfies-as-contract" mechanism of E10-C08 has no counterpart. |
| A. M. Scheel, M. R. M. J. Schijen, D. Lakens, "An Excess of Positive Results: Comparing the Standard Psychology Literature With Registered Reports", *Advances in Methods and Practices in Psychological Science* 4(2) (2021), doi:10.1177/25152459211007467. VERIFIED via Crossref. | 96% positive results in the standard literature versus 44% in Registered Reports: the format demonstrably surfaces null and negative findings. | Empirical anchor for E10-C11 (negative results at win-prominence) and for E10-C08's claim that a pre-committed verdict rule changes what gets reported. Cross-listed to family 5. | Measures publication outcomes across a corpus; offers no per-session record instrument and no "dead end named is a contribution" norm applied to a research path's own chronicle. |

## 2 · Adversarial collaboration, red-team review, assurance cases

| Citation | One-line result | Relation to E10 | Unclaimed |
|---|---|---|---|
| D. Kahneman, G. Klein, "Conditions for intuitive expertise: A failure to disagree", *American Psychologist* 64(6):515-526 (2009), doi:10.1037/a0016755. VERIFIED via Crossref DOI metadata (APA PsycNet landing is a JS shell). | The canonical adversarial-collaboration write-up: rivals jointly design a fair test, articulate each other's positions in good faith, and publish the residual disagreement. | Ancestor of E10-C09 (the adversarial-review loop) and E10-C14 (the review persona held hostile to the strengthening failure mode). | A two-party good-faith collaboration between named human rivals; not a standing adversarial *seat* re-instantiated per artifact with priced findings and a machine-run re-check against the reviewer's own successor criterion. |
| B. Mellers, L. Ungar, J. Baron, J. Ramos, B. Gurcay, K. Fincher, S. E. Scott, D. Moore, P. Atanasov, S. A. Swift, T. Murray, E. Stone, P. E. Tetlock, "Psychological Strategies for Winning a Geopolitical Forecasting Tournament", *Psychological Science* 25(5):1106-1115 (2014), doi:10.1177/0956797614524255. VERIFIED via Crossref. | Good Judgment Project: calibrated, probability-banded forecasts with training and team deliberation beat control conditions and (elsewhere in the programme) professional analysts. | Ancestor of the confidence-band discipline behind E10-C12 (percentages are the named estimator's) and of the calibration ethos behind E10-C08. | Calibration is over event probabilities scored against outcomes; the register's bands are estimator-attributed confidences on standing conjectures, not tournament forecasts, and are never softened post hoc rather than Brier-scored. |
| T. P. Kelly, R. A. Weaver, "The Goal Structuring Notation - A Safety Argument Notation", Proc. Dependable Systems and Networks (DSN) 2004 Workshop on Assurance Cases (2004). VERIFIED at scholarly record (Semantic Scholar paper record + author-hosted PDF); workshop paper, no DOI. | Structured decomposition of a top claim into subgoals, strategies, and supporting evidence, with every leaf tracing to evidence: the assurance-case discipline. | Structural precedent for E10's trace-or-delete (E10-C04) and gate-brief argument structure (E10-C02/C03): claims trace to evidence or they do not stand. | GSN structures a static safety argument for a system; it is not a live research-governance loop, has no non-delegable completion gate reserved from an automation, and no two-register vocabulary fence. |

## 3 · Multi-agent research pipelines with role separation; agentic review

| Citation | One-line result | Relation to E10 | Unclaimed |
|---|---|---|---|
| C. Lu, C. Lu, R. T. Lange, J. Foerster, J. Clune, D. Ha, "The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery", arXiv:2408.06292 (Sakana AI, 2024). VERIFIED at arXiv abstract. | End-to-end automated pipeline: idea generation, code, experiments, figures, full paper, and a *simulated automated peer review* reported at near-human score agreement. | The closest published relative of the agent-fleet shape behind E10-C13 (seat discipline) and E10-C02, and the sharpest contrast: it *automates the final review*, which is exactly what E10-C02's non-delegable P4 forbids. | Role separation here is functional pipeline staging inside one automated system; it has no human completion gate the runtime may not cross, no append-only adversarial ledger, and no two-register discipline. The differentiator is non-delegability, not role separation. |
| M. Zhuge, C. Zhao, D. Ashley, W. Wang, D. Khizbullin, et al., "Agent-as-a-Judge: Evaluate Agents with Agents", arXiv:2410.10934 (2024). VERIFIED at arXiv abstract. | Agentic evaluators give step-by-step, tool-augmented judgement of other agent systems, outperforming LLM-as-a-Judge and matching a human-evaluation baseline on the DevAI benchmark. | Prior art for machine-run review with role separation (E10-C09's reviewer seat, E10-C13). | The judge is itself an agent issuing the verdict; E10-C02 reserves the *final* verdict (P4) for a human and forbids any agent from marking, simulating, or summarising it. Agentic judging is the delegated gate the method structurally refuses. |

## 4 · Append-only, tamper-evident research-process ledgers

| Citation | One-line result | Relation to E10 | Unclaimed |
|---|---|---|---|
| B. Laurie, A. Langley, E. Kasper, "Certificate Transparency", RFC 6962 (IETF, June 2013; obsoleted by RFC 9162). VERIFIED at rfc-editor.org. | A publicly auditable, append-only log whose append-only property is enforced by Merkle-tree consistency proofs; any attempt to show different histories to different observers is efficiently detectable. | The strongest mechanism precedent for E10-C05 (findings in one append-only ledger) and E10-C17 (corrections filed in the record, never laundered). | CT logs immutable certificate events with cryptographic non-equivocation; the critiques ledger is an append-only record of *research findings and their resolutions* with a fixed FINDING/EVIDENCE/PROPOSED/STATUS form, enforced socially by one serialising orchestrator, not by Merkle proofs. The mechanism is prior art; the application to adversarial research findings is not the RFC's object. |
| Tamper-evident electronic lab notebook (ELN) practice and blockchain-timestamped lab-record proposals (general body of work; representative: tamper-evident notebook and blockchain-timestamp audit-log literature surveyed this session, no single primary record adopted). BACKGROUND ONLY, not adopted as a verified row. | ELNs and timestamped notebooks provide chronology, authorship, and tamper evidence for research records. | Context for E10-C16 (the chronicle instrument as a contemporaneous record) and E10-C05. | ELNs record experimental steps for IP/compliance; none found is a per-session, verdict-first, reversal-at-win-prominence path record written "as if a methods examiner will read it". Do not cite a specific ELN paper until one is resolved at record. |

## 5 · Negative-results publication norms (the win-prominence rule)

| Citation | One-line result | Relation to E10 | Unclaimed |
|---|---|---|---|
| A. M. Scheel, M. R. M. J. Schijen, D. Lakens (2021), as in family 1. VERIFIED. | Registered Reports cut the positive-result rate from 96% to 44%: a structural norm that surfaces negatives. | Empirical support for E10-C11 (negative results filed at the same prominence as confirmations) and GR-8. | Demonstrates the effect across a literature; does not apply the norm reflexively to a research path's own dead ends (E10-C11's second move: "a dead end named is a contribution"). |
| The Registered Reports in-principle-acceptance mechanism (Chambers; Nosek et al., as in family 1) and dedicated null-result venues (Journal of Negative Results and successors; PLOS Biology values-based null-results initiative, 2025). Chambers/Nosek VERIFIED; the null-result-venue landscape confirmed at search level, individual venue records NOT separately fetched. | Publication commitment before outcomes is the field's standard instrument for defeating the file-drawer effect. | Ancestor of E10-C11's standing rule (a result against prediction goes to the register with a confirmation's prominence). | These are journal-level acceptance policies; the programme's rule is an internal ledger/chronicle norm enabling closure statements over an enumerated space of killed levers (E10-C11's circuit-workshop half), which is unclaimed. |

## 6 · Verification discipline for automated checks (non-vacuous checkers)

| Citation | One-line result | Relation to E10 | Unclaimed |
|---|---|---|---|
| R. A. DeMillo, R. J. Lipton, F. G. Sayward, "Hints on Test Data Selection: Help for the Practicing Programmer", *Computer* 11(4):34-41 (1978), doi:10.1109/C-M.1978.218136. VERIFIED via Crossref. | Origin of mutation testing: seed faults and require the test suite to detect them, measuring whether tests can catch changes rather than merely execute code. | Ancestor of E10-C06 (checkers proven non-vacuous) and the circuit-workshop half (certificate checkers unit-tested against deliberately corrupted inputs). | Mutation testing scores an existing suite against seeded faults; E10-C06 is an operational guard on a *deterministic check itself* (an argv-less invocation must exit non-zero, not pass having checked nothing), plus a two-domain convergence claim. |
| D. Schuler, A. Zeller, "Assessing Oracle Quality with Checked Coverage", Proc. IEEE ICST 2011, pp. 90-99, doi:10.1109/ICST.2011.32; journal version "Checked coverage: an indicator for oracle quality", *Software Testing, Verification and Reliability* 23(7):531-551 (2013), doi:10.1002/stvr.1497. VERIFIED at CISPA/Semantic Scholar record + Crossref (both DOIs; conference DOI added at the A4 station, 2026-07-10). | Checked coverage: the dynamic slice of executed statements that actually influence an oracle, detecting tests that run code but never check the result; reported more sensitive to oracle weakness than mutation testing. | The precise published neighbour of E10-C06/E10-C14: a check that executes but verifies nothing is worthless, and the discipline is to detect exactly that. | Schuler-Zeller diagnose weak oracles in a unit-test suite; the programme generalises the same principle to research-process checkers and hard-wires the failure as an exit code, and pairs it with the "vacuous green stood in the record for two gates" self-audit (L082). The generalisation and the self-catching instance are unclaimed. |

## 7 · Anchoring the combination: the two inversions

| Citation | One-line result | Relation to E10 | Unclaimed |
|---|---|---|---|
| E. Evans, *Domain-Driven Design: Tackling Complexity in the Heart of Software* (Addison-Wesley Professional, 2003; first edition, ISBN 978-0-321-12521-7): ubiquitous language and bounded context. VERIFIED at concept level in the sweep; edition pinned at the publisher record (InformIT/Pearson) at the A4 station, 2026-07-10. | A single shared vocabulary is cultivated so domain experts and developers speak one language inside a bounded context. | The near neighbour of E10-C01's two-register discipline, and its inversion: DDD drives *toward one* shared vocabulary; E10-C01 deliberately *maintains two* registers (formal and narrative) with a fixed production direction (math first, myth second) and a no-direct-citation mediation fence between them. | No DDD construct fixes a production direction between two registers or forbids citing one register at the other's tier. The deliberate two-register split with a one-way mediation rule is unclaimed. |
| R. G. Cooper, "Stage-Gate Systems: A New Tool for Managing New Products", *Business Horizons* 33(3):44-54 (1990), doi:10.1016/0007-6813(90)90040-I; the underlying staged go/kill process developed in *Winning at New Products* (Addison-Wesley, 1986): staged development with go/kill gates staffed by human gatekeepers. VERIFIED at concept level in the sweep; record pinned via Crossref at the A4 station, 2026-07-10. | Gates are human go/kill/hold/recycle investment decisions between development stages. | The near neighbour of E10's gate ladder (E10-C02/C03), and its inversion: Stage-Gate gates are *managerial resource* decisions; E10's terminal gate (P4) is an *epistemic completion* gate reserved from the automation, a literal machine state ("awaiting-P4") the runtime may not cross, mark, or simulate. | Stage-Gate gatekeepers approve spend and progression; nothing in the model forbids the executing system from recording the gate as passed. The non-delegability-as-machine-state is unclaimed. |

---

## Precision notes for A0 (no CONTESTED items raised)

Nothing swept contradicts an E10 claim; GR-10 is not triggered. Four notes,
proposed as ledger entries in my chronicle:

1. **The AI Scientist contrast (E10-C02).** Lu et al. (2024) run a *simulated
   automated peer review* as the pipeline's evaluation stage. This is not a
   contradiction of E10-C02 but its defining anti-pattern: the method reserves
   the final review (P4) for a human precisely to refuse the automated final
   gate the AI Scientist embraces. WP-27 should cite this work and state the
   contrast explicitly; it is the sharpest way to make the non-delegable gate
   legible to a machine-learning readership.

2. **Two-register framing (E10-C01).** Evans's ubiquitous language is the
   neighbour a software-literate referee will raise. The novelty is confined to
   the *two-register* split with a fixed production direction and a
   no-cross-citation fence; present it as the inversion of ubiquitous language,
   not as an unrelated idea, or the paper invites the ambush.

3. **Gate framing (E10-C02/C03).** Cooper's Stage-Gate and the human-in-the-loop
   literature are the neighbours for the gate ladder. Confine the novelty to
   non-delegability-as-machine-state; a gate ladder per se is not new.

4. **Numbered conjecture/problem lists (E10-C12).** Numbered standing-problem
   registers with status are a long tradition (Hilbert's problems; the Clay
   Millennium Problems; the Erdos problems list). These were confirmed at
   search level only and are NOT adopted as verified rows this session; a
   referee-grade sweep should resolve at least one at record before P1 and
   frame the *numbering* as prior art, reserving novelty for
   confidence-banded, estimator-attributed conjectures inside an active
   agent-run governance loop. Flagged UNVERIFIED-at-record for this specific
   comparison. **A4 station resolution (2026-07-10): RESOLVED at record.**
   D. Hilbert, "Mathematical problems", *Bulletin of the American Mathematical
   Society* 8(10):437-479 (1902), doi:10.1090/S0002-9904-1902-00923-3 (the
   Bulletin's English translation of the 1900 Paris problem list), VERIFIED
   via the Crossref DOI record (the AMS landing page returns 403; Crossref
   route per the house pattern, L102). The WP-27 draft's Section 6 now names
   the resolved record and lists the reference as the tradition's anchor;
   whether Section 3.1 or Section 5 argues the numbering-as-prior-art
   comparison in the body remains with the drafting seats (routed A4 to
   A3/A2 via A0). The Clay Millennium and Erdos lists remain at search
   level, uncited.

---

## Novelty ledger

Direction (stated honestly per the task card): the likely novel core is the
**combination**, not any component. The N-numbers are therefore narrow and few;
the S-numbers are broad and are where most of E10 sits.

### Assertions defensible as NEW (state each no wider than written here)

- **N1 (traces to the E10 cluster; the paper's own framing claim).** The
  assembly: a public register of numbered, confidence-banded,
  estimator-attributed conjectures (E10-C12) + a gate ladder terminating in a
  non-delegable human completion gate (E10-C02/C03) + an append-only
  verdict-first adversarial ledger (E10-C05) + a two-register vocabulary
  discipline (E10-C01), operated by an agent fleet and instanced twice
  independently (E10-C15). Each component has strong prior art (families 1-6);
  no found work assembles them as a governance method for agent-run speculative
  technical research. Keep a "to our knowledge" qualifier; present the assembly
  as the contribution.

- **N2 (traces to E10-C01).** The two-register discipline: two vocabularies
  (formal and narrative) maintained deliberately, with a fixed production
  direction (formal first, narrative harvested at a designated beat, "no
  emergence" a valid entry) and a structural mediation rule forbidding direct
  citation of the narrative register at formal tiers. Evans's ubiquitous
  language is the neighbour and the inversion (it unifies to one language). The
  inversion is unclaimed. Present narrowly, as an inversion of a known idea.

- **N3 (traces to E10-C02/C03).** The non-delegable completion gate as a literal
  machine state: "awaiting-P4" is a runtime state after which no agent touches
  the artifact, and P4 is never marked, simulated, summarised, or assumed by any
  agent, with the same non-delegability covering publication and version
  control. Stage-Gate go/kill gates and human-in-the-loop supervision are
  neighbours but are managerial or supervisory, not an epistemic final gate
  reserved *from the automation that prepares it*. Present narrowly.

- **N4 (traces to E10-C15).** Cross-domain convergence as a validation
  instrument: four sub-rules (non-vacuous checkers E10-C06, resume-verify-disk
  E10-C07, pre-registered "cannot decide" verdicts E10-C08, negative-results
  at win-prominence E10-C11) arriving independently in two loops that shared no
  code, seats, or artifacts, offered as the evidence the template transfers.
  The individual rules are prior art (families 1-6); using their independent
  re-derivation in a second domain as the method's transfer evidence is
  unclaimed. Present as convergence observed, not as derivation proven (the E10
  fence).

### Assertions that must be framed as SYNTHESIS (not new)

- **S1 (E10-C08, E10-C12).** Pre-registering hypotheses and verdict rules before
  outcomes belongs to pre-registration and Registered Reports (Chambers 2013;
  Nosek et al. 2018). New residue: severity-priced findings as advance contracts
  and the reviewer ruling on its own successor criterion. Frame the
  pre-registration posture as synthesis.

- **S2 (E10-C09, E10-C14).** Adversarial, good-faith red-team review with agreed
  fair tests belongs to adversarial collaboration (Kahneman-Klein 2009), to
  calibrated forecasting tournaments (Mellers et al. 2014), and to assurance
  cases (Kelly-Weaver 2004). New residue: a standing adversarial *seat*
  re-instantiated per artifact with a machine-run re-check. Frame the
  adversarial-review posture as synthesis.

- **S3 (E10-C02, E10-C13).** Multi-agent research pipelines with role separation
  and agentic peer review belong to the AI Scientist (Lu et al. 2024) and
  Agent-as-a-Judge (Zhuge et al. 2024). New residue: the non-delegable final
  gate (N3), not the role separation. Frame seat discipline as synthesis; lead
  with the contrast, not the resemblance.

- **S4 (E10-C05, E10-C17).** Append-only, tamper-evident logs belong to
  Certificate Transparency (Laurie et al. 2013) and ELN practice. New residue:
  the fixed-form adversarial FINDING/EVIDENCE/PROPOSED/STATUS record with
  corrections filed in the record. Frame the append-only property as synthesis.

- **S5 (E10-C11).** Norms that surface null and negative results belong to
  Registered Reports and null-result venues; the effect is measured by Scheel
  et al. (2021). New residue: the norm applied reflexively to a research path's
  own dead ends, enabling closure statements over an enumerated killed-lever
  space. Frame the negative-results norm as synthesis.

- **S6 (E10-C06, E10-C14).** "Your automated checks may verify nothing" belongs
  to mutation testing (DeMillo et al. 1978) and checked coverage
  (Schuler-Zeller 2011/2013). New residue: the operational guard (argv-less
  exit-non-zero) and the self-caught vacuous-green audit. Frame the
  non-vacuous-checker principle as synthesis.

### Sweep count

Verified works and records: 13 primary records (11 literature/standard records
resolved at Crossref DOI, arXiv, RFC, or archived scholarly record: Chambers
via COS, Nosek et al., Scheel et al., Kahneman-Klein, Mellers et al.,
Kelly-Weaver, Lu et al., Zhuge et al., Laurie et al. RFC 6962, DeMillo et al.,
Schuler-Zeller; plus 2 concept-level canonical texts adopted as inversion
anchors: Evans DDD, Cooper Stage-Gate). Items carried as UNVERIFIED-at-record:
the numbered-problem-list comparison of precision note 4 (Hilbert/Clay/Erdos,
confirmed at search level only, not adopted as rows) and the specific
ELN/blockchain-notebook row of family 4 (kept as BACKGROUND, no single record
adopted). Neither may be cited in a WP-27 draft until resolved at record.

A4 station addendum (2026-07-10): four records added or pinned at the
citation station: Chambers's *Cortex* editorial (Crossref,
doi:10.1016/j.cortex.2012.12.016), Cooper's *Business Horizons* 1990 article
(Crossref, doi:10.1016/0007-6813(90)90040-I, with *Winning at New Products*,
Addison-Wesley, 1986, as the book origin), Evans's publisher record
(InformIT/Pearson, first edition, ISBN 978-0-321-12521-7), and the Hilbert
1902 Bulletin translation (Crossref, doi:10.1090/S0002-9904-1902-00923-3).
Both concept-level anchors are thereby converted to pinned records and the
numbered-problem-list item of precision note 4 is resolved at record: 14
works now verified at a primary record (the original 11 literature/standard
records, Evans, Cooper, Hilbert), plus the COS initiative page as the
adoption record. The ELN/blockchain-notebook item of family 4 remains
BACKGROUND, unresolved at record, and uncited.

### Limits of this sweep

Web-only, English-only, one session. The two inversion anchors (Evans, Cooper)
were cited at concept level from canonical texts, not fetched at a page record;
a referee-grade pass should pin an edition/page before P1 (discharged: both
pinned at the A4 station, 2026-07-10; see the addendum above). The
numbered-conjecture-register tradition (precision note 4) is the most likely
un-swept ambush and should be closed first (closed at record at the A4
station, 2026-07-10: Hilbert 1902; the body-framing decision remains with
the drafting seats). The philosophy-of-science framing
of confidence-banded conjectures (Popper, corroboration) was touched at search
level and left unswept per scope; if WP-27 leans on falsification language, add
a Popper/Lakatos pass. No disclosure-economics or ELN-record pass was run.
