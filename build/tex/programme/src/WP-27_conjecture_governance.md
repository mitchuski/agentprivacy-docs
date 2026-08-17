---
title: "Conjecture Governance: an Operating Method for Agent-Generated Research, with a Non-Delegable Completion Gate"
subtitle: "WP-27 · tier A · meta-research / research-methods venue · 2026-07-10 · status draft-v3"
author: "The Privacy-is-Value Research Programme"
date: "2026-07-10"
---

<!-- ============================================================
A2 HANDOFF NOTE (pipeline apparatus; REMOVE BEFORE ANY RELEASE)

Draft-v1, register translation from E10-method-record (31 claims,
widened 2026-07-10). Inline [E10-Cnn] markers are the claim trace
and are stripped at release together with this comment and the
trace map. No register C-identifiers appear in the body; claims
travel as [E10-Cnn] only.

FORMALISATION STUBS (four; ALL DISCHARGED at draft-v2, A3 pass
2026-07-10, each as a definition plus numbered invariants that
formalise the prose specification and nothing beyond it):
1. Section 3.2: gate ladder as a labelled transition system;
   non-delegability as an absence of transitions (Definition 2,
   I5-I6). DISCHARGED.
2. Section 3.3: ledger append-only invariant, enforcement stated
   as procedural, not cryptographic, exactly (Definition 3, I7-I9
   plus enforcement remark; the Section 5 contrast now points at
   the remark). DISCHARGED.
3. Section 3.4: production direction as a constraint on the
   derivation and citation relations (Definition 4, I10-I12);
   the dated qualification preserved as an explicit temporal
   index on the invariants. DISCHARGED.
4. Section 3.1: register numbering invariants (Definition 1,
   I1-I4). A3 RULING: stands alone, NOT folded into stub 2; the
   register's immutable object is the number-to-claim denotation
   map, not entry content (register prose, bands, and status are
   revised under governance), and the minting licence is an
   actor-licensing property akin to I5, not an append property.
   Folding would either overstate the register (content
   immutability it does not have) or weaken the ledger invariant.
   Reason recorded in the Section 3.1 remark and the A3 chronicle.
A3 RULING on the A2 open question (4.2 earned-twice table):
STAYS PROSE. A schematic convergence statement (the four rules as
elements of an intersection of independently generated rule sets)
would add notation without content and would push an observational
convergence toward a formal independence claim the record carries
only as reported observation (E10-C15: convergence, not derivation).
No notation was improvised beyond the prose specifications; the
Section 3 preamble states the design-invariant evidence class.

NOVELTY FENCE COMPLIANCE (reviews/WP-27_prior_art.md, binding):
contributions lead with N1 (the assembly), then N2-N4, each stated
no wider than the fence wording; S1-S6 are conceded in Section 5
family by family BEFORE any novelty is asserted, and each novelty
claim is presented at its nearest neighbour (Evans for N2, Cooper
and the human-in-the-loop line for N3, Lu et al. as the defining
anti-pattern for the non-delegable gate). The two UNVERIFIED items
(numbered-problem-list tradition; specific ELN records) are NOT
cited; both are named generically in Section 6 as unswept referee
risks, per the review's instruction.

CIRCUIT-WORKSHOP FENCE: the second instance appears at claim level
only (loop shape, the four convergent rules, the two cannot-decide
filings, the killed-levers rationale). No mechanisms, no resource
counts, no tier structure, no submission strategy. The fence is
stated in the body (Section 4.1) as reportable content.

STILL OPEN FOR DOWNSTREAM SEATS:
- A4: bibliography resolution (13 works verified at record in the
  prior-art review; Evans and Cooper are concept-level anchors and
  need an edition/page pin before P1, review limits section).
- A5/P1 risk list: the numbered-problem-list sweep (review
  precision note 4) is the named ambush; close before P1.
- A7: voice pass; this draft is A2 register translation, not final
  prose.
- Quotes from the operating record are carried verbatim inside
  quotation marks and attributed to the record generically (no
  internal file paths in the body); A9 verifies each against E10
  wording at the consistency station.

A4 ADDENDUM (citation station, 2026-07-10, per
tasks/WP-27_A4_2026-07-10.md): all 14 references verified at their
primary records this session (Crossref DOI API for the six walled
journal articles; arXiv abstracts for Lu et al. and Zhuge et al.;
rfc-editor.org for RFC 6962 and its obsoletion by RFC 9162; the COS
initiative page for the Registered Reports format and the
300-journal figure; archived scholarly record for Kelly and Weaver,
which has no DOI). Citation metadata edits only: Chambers pinned to
the Cortex editorial (49(3):609-610, 2013, doi:10.1016/j.cortex.2012.12.016);
Cooper pinned to Business Horizons 33(3):44-54, 1990,
doi:10.1016/0007-6813(90)90040-I, with Winning at New Products
(Addison-Wesley, 1986) as the book origin, and both in-text
"(Cooper)" instances year-pinned; Evans pinned to Addison-Wesley
Professional, 2003, first edition, ISBN 978-0-321-12521-7; Schuler
and Zeller's conference version given its DOI (10.1109/ICST.2011.32)
and the journal version its own title. The L102(b)/L104(c)
numbered-problem-list obligation is resolved at record: Hilbert,
"Mathematical problems", Bulletin of the AMS 8(10):437-479, 1902,
doi:10.1090/S0002-9904-1902-00923-3 (Crossref route; the AMS landing
page returns 403). Disposition: the body did not cite the tradition;
Section 6's unswept-neighbours paragraph now names the resolved
record and the reference is listed as its anchor; whether Section 3.1
or Section 5 should argue the numbering-as-prior-art comparison is
claim-shaped and is routed to A3/A2 via A0. Citation-role check
passed on every in-text citation; the one comparative import
re-checked at record is Schuler-Zeller's "more sensitive to oracle
weakness than mutation testing" (abstract wording: "even more
sensitive than mutation testing"). No claim was reworded; frontmatter
status stays draft-v2. prior_art rows reconciled the same session.

A3 ADDENDUM (revision 1, formal legs, 2026-07-10, per
tasks/WP-27_A3_revision_2026-07-10.md; L107 rulings govern):
- MAJOR-2 (WEAKEN ruling): I9 weakened to exactly E10-C05 content
  (STATUS as the designated mutable field of the fixed four-field
  form; corrections as entries per I8). The unextracted licensing
  clause and its status-history consequence are REMOVED, not
  defended; a closing clause states the record specifies no
  status-mutation semantics beyond the designation. No other
  passage leaned on the clause (swept).
- MINOR-1: the "Enforcement of I1 to I4" sentence split; the
  authority-lag episode now cited under I4 (with I2's
  registration-only rule), the visible-erratum episode cited under
  the register-wins rule as prose governance, explicitly not an
  invariant of Definition 1. No new invariant minted (E10-C12/C17
  state the rule as prose, not as a numbering invariant).
- MINOR-2: Definition 1 given a temporal origin at the register's
  consolidation gate, on Section 3.4's temporal-index pattern; I1's
  "whole history" now reads over the indexed history only.
- MINOR-5: I12's narrative-sourced channel narrowed to dated design
  status (recorded instances lie in the excluded earlier flow;
  in-scope candidate instances are agent-work residue). E10-C12
  marker added in Section 3.4; trace map line updated to match.
- MAJOR-3 SUPPORT: adoption clause (invariant subset I_A = {I1, I2,
  I4, I5, I6, I7, I8, I10, I11}, each checkable from an adopting
  team's own record; I3/I9/I12 excluded with reasons) and period
  clause (N full ladder transits, N fixed in advance, proposed
  default 3) drafted in the [A2: place in section 7] block at the
  end of Section 7. A2 consumes and deletes the block.
A2's anchors untouched (:310 MAJOR-1, the abstract, the Section 6
availability area, :320 MINOR-4, :122 MINOR-6). Frontmatter status
NOT bumped; the draft version bumps when A2's legs land.

A2 ADDENDUM (revision 1, prose legs, 2026-07-10, per
tasks/WP-27_A2_revision_2026-07-10.md; L107 rulings govern; no A3
leg re-edited):
- MAJOR-1: the Section 4.4 catch reattributed, wording checked
  verbatim against E10-C24 ("Generation four, the pipeline's:
  deterministic checks proven non-vacuous"; "stood unnoticed in the
  corpus until this sweep"): generation four keeps the extraction's
  denotation and the 111/111 catch is attributed to the extraction
  sweep operating under the trace-or-delete discipline; [E10-C04]
  marker added. One further sentence records that the misattribution
  was itself found by the paper's own adversarial review station and
  corrected in this revision; it cites nothing beyond the revision's
  record and carries no extraction marker (trace map notes it).
- MAJOR-3: Section 7 restated consuming the A3 support block (block
  deleted): adoption criterion I_A = {I1,I2,I4,I5,I6,I7,I8,I10,I11}
  with the three exclusions reasoned in-text; period = N full ladder
  transits, N fixed in advance in the adopter's own register,
  proposed default N = 3 adopted at placement per the L108 routing
  (order-of-magnitude grounding stated in-text); criterion (i)
  restated as an observable with the counterfactual clause deleted;
  falsification stated severally (any single null falsifies the
  conjunctive hypothesis as stated) versus jointly (a triple null
  counts against the convergence grounding itself).
- MAJOR-4 (per the L107 ruling): one Section 6 paragraph, current
  fact only: the register's public surface is the one non-literature
  URL already carried; the ledger and chronicles are unpublished at
  draft time; release or editorial availability is reserved to the
  programme's principal, recorded as reserved, not promised; no
  availability commitment minted.
- MINOR-3: the abstract's two-instance evidence sentence now carries
  "within a single programme"; the N1 fence wording elsewhere is
  untouched.
- MINOR-4: strike option taken; "and a trace discipline enforced by
  deletion" removed from the Section 5 S2 residue sentence.
- MINOR-6: abstract "prevent history rewriting" replaced by "make
  history rewriting detectable", consistent with Section 1 and the
  Section 3.3 procedural-enforcement remark.
Frontmatter bumped to draft-v3. Trace map updated: Section 4.4 line
gains E10-C04 and a no-extraction-claim note for the revision-record
sentence; Section 6 line notes the availability paragraph; Section 7
line gains E10-C02/E10-C09 for the period grounding. The
nothing-exceeds-STATUS line re-verified true post-MAJOR-1 (wording
unchanged; the fix restores it). Next station: A0 targeted re-check
per the memo's five-leg successor criterion.
============================================================ -->

## Abstract

Agentic research pipelines can generate candidate results faster than any human can verify them. Existing governance instruments each address one failure mode: pre-registration fixes analysis plans, adversarial collaboration structures disagreement, assurance cases structure evidence, append-only logs make history rewriting detectable, and mutation testing exposes vacuous checks. This paper presents an assembled method for governing speculative technical research produced substantially by an agent fleet, as operated and recorded in a single research programme. The method has four components: a public register of numbered conjectures carrying estimator-attributed confidence bands and falsification conditions, which is the sole authority for claim status [E10-C12]; a gate ladder whose terminal completion gate is non-delegable, held by a human principal, and implemented as a literal machine state that no agent may mark, simulate, or summarise [E10-C02]; an append-only adversarial ledger with a fixed finding form, in which corrections to the record are themselves filed to the record [E10-C05]; and a two-register vocabulary discipline separating a formal register from a narrative register with a fixed production direction between them [E10-C01]. Each operating rule is stated with the defect class it was earned against, including the method's own failures: a false proposition reached completion-draft before adversarial review caught it, and vacuous check evidence stood in the record for two gates before an audit caught it [E10-C06][E10-C14]. The method is evidenced by its contemporaneous operating record across two independent instances within a single programme; the instances shared no code, seats, or artifacts, and four operating rules arrived independently in both [E10-C15]. To our knowledge, no prior work assembles these components as a governance method for agent-operated research; every component separately has strong prior art, which Section 5 concedes before any novelty is asserted. The transfer of the method beyond its two instances is stated as a hypothesis with a test, not as an established generality. A result against the method's own predictions is filed to its register with the same prominence as a confirmation, and this paper commits to that in writing.

## 1 Introduction: the verification gap

A research pipeline in which language-model agents draft, review, and revise technical artifacts has an asymmetry at its centre: generation is cheap and verification is not. The pipeline studied here produced full paper drafts, adversarial review memos, and revision cycles within single days [E10-C09]; no human principal can read at that rate, and a governance method that assumed contemporaneous human comprehension of every intermediate artifact would have failed silently here at the first backlog. The failure is not hypothetical in this record. A proposition that was false as stated reached completion-draft before an adversarial review seat constructed a counterexample by hand [E10-C09]; deterministic check scripts, invoked without file arguments, exited green having checked nothing, and multiple agents logged that green as evidence across two gates before a consistency audit caught it [E10-C06]. A method for this setting must assume that its own instruments will fail and must be structured to catch them.

The instruments that the meta-research and software-engineering literatures supply each govern one failure mode. Pre-registration and Registered Reports commit hypotheses and analysis plans before outcomes are observed (Chambers 2013; Nosek et al. 2018). Adversarial collaboration structures disagreement between rivals into a fair test (Kahneman and Klein 2009). Assurance cases trace claims to evidence (Kelly and Weaver 2004). Append-only transparency logs make history rewriting detectable (Laurie, Langley and Kasper 2013). Mutation testing and checked coverage expose test suites that execute code but verify nothing (DeMillo, Lipton and Sayward 1978; Schuler and Zeller 2011). Multi-agent research pipelines separate generator and evaluator roles (Lu et al. 2024; Zhuge et al. 2024). None of these, singly, is a governance method for a research programme whose drafting labour is agentic and whose claims are speculative conjectures rather than completed studies; and the most complete automation of the pipeline shape, the AI Scientist of Lu et al. (2024), automates precisely the step this paper's method refuses to automate, the final review.

This paper reports a method that was operated, not proposed: every rule below is evidenced by a contemporaneous operating record (an append-only ledger, frozen per-session chronicles, gate briefs with recorded human dispositions), and several rules exist only because a specific defect occurred and was caught [E10-C05][E10-C16][E10-C19]. The method's evidence class is therefore process-record: the record the method kept of itself, including its failures [E10-C16]. Section 2 states the four components and the operating rules with the defect classes they were earned against. Section 3 details each instrument. Section 4 presents the operating evidence, including a second, independent instance of the same discipline in a different domain [E10-C15]. Section 5 places the method against prior art and confines the novelty claims. Section 6 states limitations, including the record's own documented instrument failures. Section 7 states the transfer claim as a hypothesis with a test.

### 1.1 Contributions

The prior-art position is stated before the contributions are claimed: every component of this method has strong, nameable prior art, and Section 5 concedes it family by family. The contributions are the assembly and two inversions, plus a validation instrument; each is stated no wider than here.

1. **The assembly (Section 2).** A governance method combining a public register of numbered, confidence-banded, estimator-attributed conjectures [E10-C12], a gate ladder terminating in a non-delegable human completion gate [E10-C02][E10-C03], an append-only verdict-first adversarial ledger [E10-C05], and a two-register vocabulary discipline [E10-C01], operated by an agent fleet and instanced twice independently [E10-C15]. Each component separately is prior art; to our knowledge, no found work assembles them as a governance method for agent-operated speculative technical research.

2. **The two-register discipline as an inversion (Sections 3.4, 5).** Two vocabularies, formal and narrative, are maintained deliberately, with a fixed production direction (formal first; narrative harvested at a designated beat; "no emergence" a valid entry) and a structural mediation rule forbidding direct citation of the narrative register at formal tiers [E10-C01]. The near neighbour is the ubiquitous-language discipline of domain-driven design (Evans 2003), which drives toward one shared vocabulary; this method deliberately maintains two, with a one-way derivation direction. The inversion, not the idea of vocabulary discipline, is the claim.

3. **The non-delegable completion gate as a machine state (Sections 3.2, 5).** The terminal gate of the ladder is not a policy but a state: "awaiting completion-gate" is a literal state in the pipeline's manifest after which no agent touches the artifact, and the gate is never marked, simulated, summarised, or assumed by any agent; the same non-delegability covers publication and version control [E10-C02]. Stage-gate development processes (Cooper 1990) staff gates with human decision-makers, but nothing in that model forbids the executing system from recording the gate as passed; here the prohibition is structural. The machine-state non-delegability, not the gate ladder, is the claim.

4. **Cross-domain convergence as a validation instrument (Sections 4, 7).** Four operating rules (non-vacuous checkers [E10-C06], resume-verify-disk recovery [E10-C07], pre-registered verdict rules with "cannot decide" as an honoured outcome [E10-C08], and negative results at win-prominence [E10-C11]) arrived independently in two loops that shared no code, seats, or artifacts. The individual rules are prior art; offering their independent re-derivation in a second domain as the method's transfer evidence is, to our knowledge, unclaimed. The convergence is reported as observed, not as derivation proven [E10-C15].

Everything else in this paper is synthesis and is presented as such: the pre-registration posture (Chambers 2013; Nosek et al. 2018), the adversarial-review posture (Kahneman and Klein 2009; Mellers et al. 2014; Kelly and Weaver 2004), the multi-agent role separation (Lu et al. 2024; Zhuge et al. 2024), the append-only mechanism (Laurie et al. 2013), the negative-results norm (Scheel, Schijen and Lakens 2021), and the non-vacuous-checker principle (DeMillo et al. 1978; Schuler and Zeller 2011).

## 2 The Method

The method governs a research programme in which a fleet of language-model agent sessions ("seats") drafts, extracts, reviews, checks, and revises research artifacts, coordinated by an orchestrator seat, with a single human principal who owns completion, publication, and canon-level decisions [E10-C02][E10-C13]. The programme's claims are conjectures about a formal model, maintained publicly; the method's task is to let generation run at machine speed without letting any claim outrun its evidence.

### 2.1 The four components

**The conjecture register** [E10-C12]. One public file is the sole authority for conjecture numbers, confidence levels, and status. Numbers are identifiers, not ranks; a number once assigned is never reused, including numbers vacated by renumbering. New conjectures enter as unnumbered candidates and take the next free number only at registration, and registration is not an agent's act: when agent work produces conjecture-shaped residue, adoption is routed to the human principal as its own decision, explicitly distinguished from correction. Confidence bands are attributed to a named estimator and live at the claim's home document. When prose and register disagree, the register wins and the prose receives a visible erratum, never a silent edit.

**The gate ladder with a non-delegable completion gate** [E10-C02]. An artifact climbs a fixed ladder: draft; trace fidelity (every claim resolves to its extraction source); adversarial review survived; citations verified against published texts; deterministic consistency checks green; and finally the completion gate, a human read that no agent may mark, simulate, summarise, or assume. The runtime stops below the completion gate in every case; "awaiting completion-gate" is a literal machine state after which the runtime touches the artifact no further. The same non-delegability covers publication (seats prepare; the human posts) and version control (no commits or pushes from any agent session).

**The append-only adversarial ledger** [E10-C05]. Findings live in one append-only ledger with a fixed entry form: FINDING, EVIDENCE, PROPOSED, STATUS. Any seat may file; in practice a single orchestrator serialises all appends. Corrections to the record are filed in the record: when check evidence was found vacuous, the prior green claims were re-grounded on explicit re-runs and the correction itself was ledgered rather than papered over. The record's stated principle: "an audit trail that never admits error is evidence of nothing."

**The two-register discipline** [E10-C01]. One body of claims is maintained in two registers: a formal register using mathematical vocabulary exclusively, and a narrative register held upstream in the programme's narrative corpus. The production direction is fixed: formal first, narrative second; narrative is harvested from the formal work at a designated beat and never drives it, and a work cycle with no narrative emergence records "no emergence" as a valid entry. The mediation rule is structural rather than stylistic: the narrative corpus is never cited directly at formal tiers; an extraction layer restates, and formal artifacts cite the extraction.

### 2.2 Operating rules, each with the defect class it was earned against

The components are held together by operating rules. Stating a rule without its earning defect would misrepresent the method as designed rather than learned; the programme's own retrospectives record that the method was learned, not given [E10-C28]. Each rule follows with its defect class.

- **Trace or delete** [E10-C04]. Every claim in a formal artifact traces to a line in its extraction; every extraction line traces to a source in a closed registry; a claim that cannot be traced is deleted, not defended. Earned against: citation laundering around the registry. Enforcement instance: a policy brief's central operational test was deleted at re-trace because its only source was excluded by the artifact's tier filter; the distinction was re-anchored on two admissible claims, and restoration of the deleted test was fenced behind a register-process ruling rather than argued in place.

- **Checkers must be proven non-vacuous** [E10-C06]. A check with nothing to check must fail, not pass, and evidence-of-record lines must state the exact invocation. Earned against: the vacuous-green defect described in Section 1; the structural close is that an argument-less invocation of any check now exits with an error by design. The rule was earned a second time, independently, in the method's second instance (Section 4.2).

- **Interruption recovery is resume-verify-disk, never rebuild** [E10-C07]. An interrupted agent's work is on disk because output lands incrementally; what dies is the close-out. The same agent is resumed, made to verify the disk state, and forbidden from re-running anything. The complementary half, earned in the second instance: no decision-bearing verdict from an interrupted run is trusted without re-execution. Earned against: silent duplication and silent trust, respectively.

- **Verdict rules are pre-registered and never softened after the fact** [E10-C08]. Review findings state the exact passage and what would discharge the objection; severities are priced in advance (BLOCKING, MAJOR, MINOR) so routing needs no mid-flight judgement; the reviewer rules on its own successor, stating what re-examination suffices. In the second instance, probes declared their success and failure branches before running, and twice the honest answer "the instrument I pre-registered cannot decide this" was filed as such and never softened into a win. Earned against: post-hoc goalpost movement.

- **Negative results are filed at win-prominence** [E10-C11]. A result against the model's prediction goes to the register with the same prominence as a confirmation, and the path record applies the same rule to itself: reversals and dead ends are recorded at the same prominence as progress. The record's formulation: "a dead end named is a contribution; a dead end omitted is a defect." In the second instance the rule's compounding value was recorded: a killed-levers record kept at win-prominence is what made a closure statement over the whole search space possible, because only filed kills make the space enumerable.

- **Fix known findings before review** [E10-C10]. Findings already on the record are repaired before the adversarial review seat reads the artifact, so reviewer attention is not spent re-finding what the pipeline already knows. Earned against: the first paper loop, in which reviewer findings were spent on known defects; executed for the second paper as a dedicated pre-review card, after which the review returned zero blocking findings.

- **Seat discipline** [E10-C13]. Each agent session holds exactly one role for exactly one task card, boots through a fixed sequence (ground rules, role card, task card, then a statement of role, permitted writes, and definition of done), and refuses out-of-role fixes even when competent to make them. Where two seats must touch one artifact they are serialised explicitly. Shared mutable state has exactly one writer per contended file. Earned against: write collisions and competence-driven scope creep; the record shows an auditor seat that found a defect and fixed nothing, routing it to the owning role instead.

- **The named generative failure mode** [E10-C14]. The primary failure mode of a generative drafting agent, strengthening a claim to make prose flow, is named in every seat's boot file, held hostile by the review persona, and swept for mechanically at the final check station (explicit sweeps over counting claims, cross-references, and "X shows Y" assertions). The mode fired where predicted: a section preamble asserted blanket necessity where only three of five requirements had necessity constructions; the check station caught it by checking counting claims against the artifacts backing them. The stated design principle: make the honest form cheaper than the fluent form.

- **Corrections flow upstream, never launder downstream** [E10-C17]. Generated artifacts are never hand-edited; the input is fixed and the artifact rebuilt. Canon-level conflicts are escalated to the register process, not resolved by any seat. The record contains one defect traced through four instruments: an adversarial review found a bound asserted from preconditions that do not imply it; the artifact was fixed on the reviewer's decomposition; the same conflation was traced upstream into the extraction and the source specification and escalated rather than absorbed; the source correction executed only under explicit human approval with a complete before-and-after record; and the extraction was re-issued against the corrected source with a negative sweep for the same defect elsewhere.

## 3 The Instruments in Detail

Each instrument is described in prose and then fixed as a definition with numbered invariants (I1 to I12). The invariants are design invariants: they state what the method's specification contains and, where the property is an absence, what it omits by construction. Their evidence class is the process-record grade of Section 6: the governing documents that state each invariant and the practice instances that exercised it. None is asserted as an externally audited property of every operation, and each instrument's enforcement class is stated where it is weakest (the enforcement remarks of Sections 3.1 and 3.3).

### 3.1 Register mechanics

The register is one file whose authority is total within the programme: any surface that disagrees with it is, by rule, the surface in error [E10-C12]. Its numbering discipline was earned against a documented failure class: the programme's own planning record states that ad-hoc renumbering had failed twice before the register was consolidated, and concludes that only a single authority file ends the failure class [E10-C21]. The register was built by a dedicated run that resolved four collision clusters with written one-line dispositions confirmed at a signed human gate before any downstream document cited a number [E10-C12].

The dispositions themselves are written into the authority file, so the register carries the record of how it became authoritative [E10-C20]. Each disposition states its ground; where a disposition reverses a prior review's default it says so and why. External immutability constrains renumbering: numbers cited by pinned, externally distributed artifacts are never vacated, and duplicated claims are marked as aliases and retained precisely because pinned artifacts cite the alias numbers. The disposition table also preserves a completeness finding against the process's own prior reviews: intake found the collision set wider than either prior review had recorded, and the extra findings were dispositioned in the same table rather than handled off the record.

Register governance was exercised, not merely declared, in both directions. Downstream-running-ahead: two downstream surfaces carried conjecture numbers and a promotion ahead of the register, the inversion the discipline exists to prevent; a standing read-only survey instrument caught it, diagnosed it as "a lag to close, not a contradiction to arbitrate", drafted the full corrective register text, and routed the edit to the human principal without applying it [E10-C12][E10-C29]. Prose-running-behind: a research note cited a stale number for a claim the register had since settled; the correction was applied as a visible erratum, never a silent edit, under the stated boundary rule that prose conforming to an already-authoritative decision is the one class of fix needing no gate [E10-C17].

**Definition 1 (register).** Let K be the set of claims the programme maintains and index the register's successive states by t, with the origin of the index fixed at the register's consolidation point: t ranges over the states from the signed consolidation gate described above onward, so the earlier ad-hoc numbering practice, whose collisions that gate dispositioned, lies outside the indexed history, on the same temporal-index pattern as Section 3.4 [E10-C12][E10-C21]. The register at state t determines a partial function ρ_t from the positive integers to K, whose domain dom(ρ_t) is the set of assigned numbers, together with a finite set Cand_t of unnumbered candidates disjoint from the numbered claims [E10-C12].

The numbering discipline of the prose above is exactly the following four invariants [E10-C12][E10-C20].

- **I1 (single assignment).** For all states t, t′ and every number n: if ρ_t(n) and ρ_{t′}(n) are both defined, then ρ_t(n) = ρ_{t′}(n). Equivalently, the set of assignments ever made, taken over the register's whole indexed history (from the consolidation origin of Definition 1), is itself a partial function: a number denotes at most one claim, ever. I1 subsumes both identifier immutability (an assigned number never changes denotation) and no reuse (a number vacated by renumbering is never reassigned, since reassignment would give it a second claim).

- **I2 (monotone minting).** dom(ρ) is extended only at registration events, and a registration assigns the next free number, the least number never yet assigned. Numbering order is therefore registration order, and a number encodes identity, not rank. Candidates in Cand carry no number.

- **I3 (alias retention under external citation).** If a number n is cited by a pinned, externally distributed artifact, then n is never vacated: n ∈ dom(ρ_t) implies n ∈ dom(ρ_{t′}) for all t′ ≥ t. Where duplication is found, the externally cited number is retained and marked an alias of its twin rather than vacated [E10-C20].

- **I4 (human-licensed minting).** Every extension of dom(ρ) is an act of the human principal: the candidate-to-registered transition is the only number-minting event, and no agent action has an extension of dom(ρ) in its effect set. Agents produce and route candidates; they do not register them [E10-C12].

Enforcement of I1 to I4 is procedural, through the register process and its gates, as with the ledger invariant of Section 3.3. The operating record's enforcement instance for these invariants is the first episode above: downstream surfaces running ahead of the register were caught and routed to the human principal, not absorbed, which is I4's licensing boundary in use, together with I2's rule that only registration extends dom(ρ) [E10-C12][E10-C29]. The second episode enforces a different rule: the visible-erratum correction is an instance of the register-wins rule stated in the prose of this section, a rule of prose governance that Definition 1 does not contain [E10-C12][E10-C17]. Both are instances of an enforcement path in use, not a demonstration that no violation can occur.

**Remark (why the register invariants stand alone).** I1 and I2 resemble the ledger's append-only invariant (I7, Section 3.3), and I4 resembles the ladder's non-delegability invariant (I5, Section 3.2); the register nevertheless requires its own statement. The ledger's entries are immutable in content once appended; the register's entries are not: claim wording, confidence bands, and status are revised under the register process. What is immutable in the register is the denotation map ρ, the binding of number to claim, not the file's content. Folding the register into the ledger formalisation would therefore either assert a content immutability the register does not have, or weaken the ledger invariant to fit. The two disciplines share a posture, append rather than rewrite history and route the licensed act to the human, but they formalise different objects.

### 3.2 The gate ladder and the non-delegable completion gate

The ladder's lower gates are agent-run and deterministic where possible: trace fidelity is a spot-check against extraction lines; adversarial review is a persona seat with priced findings; citation verification resolves every reference at its primary record; consistency checks are scripts whose green is accepted only with the exact invocation on the record [E10-C02][E10-C06]. The terminal gate is different in kind, not merely in strictness. "Awaiting completion-gate" is a manifest state; on entering it the runtime's relationship to the artifact ends. No agent marks the gate, simulates the human read, or summarises the artifact in lieu of it. The prohibition extends to the two acts that would let an agent effectively complete work by other means: publication (seats prepare posts; the human posts) and version control (no commits or pushes from any agent session) [E10-C02].

The gate has two documented ancestors in the programme's pre-pipeline record [E10-C03]. First, chronicle gates: hard stops at which the runtime prepared a gate brief with designated blocks left open for the human principal's hand and ended its turn; a resuming runtime folded the human's writing back into the documents before any further run. Six such gates were run and signed. Second, a reading ledger: an append-only file of pointers to every piece of produced prose the human principal has not read in full, read to completion before any distribution act, under the rule "nothing publishes unread". The recorded rationale generalises the programme's own trust model to its process: "the proposer does not approve its own proposal."

The gate-brief instrument has a fixed form worth reporting because it makes partial human decisions well defined [E10-C19]: a status header naming the runs behind and ahead of the gate; a section stating what the runtime did and prepared; and designated decision blocks, one line per decision, confirm or override. An unmarked disposition is not confirmed, and the gate stays open. Items may be deferred with a named due point. A signature's scope is written out, including what it does not release (one recorded signature explicitly did not release distribution acts, which stayed on the human's per-repository trigger). Overrides are recorded verbatim and executed; one recorded override reversed the runtime's recommended structural default. Per-candidate verdicts use a closed vocabulary, and nothing binds without the word. The instrument also governs its own reopening: when a post-closure note minted register numbers eighteen days after the path closed, a further gate was opened for that act alone, on the stated ground that the standing rule is absolute [E10-C19][E10-C23].

Late contributions follow a patch protocol rather than bypassing the ladder [E10-C23]: a contribution arriving after a path has closed runs as an appended run with its own write-point gate, because it mints register numbers and the proposer does not approve its own proposal. The patch partitions its actions by gate-dependency: applied immediately are only mechanical pieces and prose conforming to already-authoritative decisions; number minting and every cross-link into locked artifacts are staged behind the gate, so a locked artifact never cites an unminted number. Epistemic accounting is kept separate from framing gain: one recorded patch strengthened the framing of an existing conjecture while its confidence stayed flat, with the reason recorded (a theoretical reframing is not the empirical second instance the claim's own promotion bar requires).

**Definition 2 (gate ladder).** Let Q = {draft, trace-checked, review-survived, citations-verified, checks-green, awaiting-completion, complete} be the artifact states and let the actor set be Ag ∪ {h}, where Ag is the set of agent roles and h the human principal. The ladder is a labelled transition system over Q whose transitions are triples (q, a, q′): actor a moves the artifact from state q to state q′, subject to that gate's evidence guard as stated in the prose above (trace spot-check; review survival against priced findings; citation resolution; checks green with the exact invocation on the record). The forward transitions up to and including entry into awaiting-completion are agent-labelled, as are regress transitions (a review verdict returning an artifact to revision); regress does not affect the invariants below [E10-C02].

The non-delegability of the prose above is exactly the following two invariants [E10-C02].

- **I5 (terminal transition licensed to the human alone).** The transition relation contains exactly one transition into complete, namely (awaiting-completion, h, complete), and contains no transition (q, a, complete) with a ∈ Ag and no transition (awaiting-completion, a, q′) with a ∈ Ag. Consequently: every path from draft to complete passes through awaiting-completion and leaves it only by the human principal's act, and complete is unreachable in the agent-only subsystem obtained by deleting the transitions labelled h. The invariant holds by construction, as an absence: there is no agent-callable transition to guard, disable, or audit, because the relation contains none.

- **I6 (extended non-delegability).** The same absence is stated for two actions outside the ladder: publication and version-control writes (commits and pushes) carry the label h only, and the agent action set contains neither; agent seats prepare, the human acts [E10-C02].

I5 and I6 are properties of the transition relation as the governing documents specify it. What the operating record adds is instance evidence: two artifacts driven to awaiting-completion with no agent transition beyond it (Section 4.1) [E10-C02]. That is evidence of operation under the invariant, not a proof that no violation is possible; the enforcement class is procedural here as elsewhere (Section 3.3).

### 3.3 Ledger discipline and the path record

The ledger's fixed form (FINDING, EVIDENCE, PROPOSED, STATUS) and single serialising writer are described in Section 2.1 [E10-C05]. Its division of labour with the other record instruments is itself a rule: the ledger holds findings, the manifest holds state, and the chronicles hold sequence and reasoning; duplication is forbidden and cross-reference is by entry identifier [E10-C05][E10-C16].

The chronicle instrument makes the path record contemporaneous and self-aware [E10-C16]: every agent session writes exactly one chronicle, verdict-first, with reversals recorded at the same prominence as progress and a handoff block naming open questions and the single next action per work package touched; "a session without a chronicle is unfinished." The instrument is self-referential by design: the programme claims its governance method is reusable, and the record's stated ground for the chronicle discipline is that this claim needs evidence, "and the evidence is this directory", written "as if a methods examiner will read it, because one will."

Two rules fix the record's evidential value. The contemporaneity rule [E10-C27]: chronicles freeze with their dates and are never revised, "which is what makes them evidence"; retrospectives are distillations, and where a chronicle and a retrospective disagree, the chronicle wins, "because it was there". A concordance instrument operationalises this by mapping every retrospective claim about an era to the contemporaneous records in which the era was worked, so distillations are auditable against their sources by construction. The honest-limits rule [E10-C26]: a cross-era ledger of the work's own limitations is compiled only from each era's own limitation sections, "so it cannot flatter"; every entry is marked closed (with the closer named and dated), rescoped, or standing open, and the summary counts them; method failures are entries at the same grade as mathematical opens. Its closing invariant binds the whole artifact set: nothing in the limits ledger is hidden elsewhere in the corpus, and nothing elsewhere in the corpus is softer than the limits ledger.

**Definition 3 (ledger).** The ledger at state t is a finite sequence L_t = (e_1, ..., e_n(t)) of entries, each entry e_i a tuple (i, F_i, E_i, P_i, S_i) of its index and the four fixed fields (FINDING, EVIDENCE, PROPOSED, STATUS). Write core(e_i) = (i, F_i, E_i, P_i) for the entry's content projection [E10-C05].

The append-only discipline of the prose above is exactly the following three invariants [E10-C05].

- **I7 (append-only core).** For states t ≤ t′: n(t) ≤ n(t′), and core(e_i) is identical in L_t and L_{t′} for every i ≤ n(t). Entries are appended in strictly increasing index order and are never edited or removed once appended; indices are never reused, so the entries are totally ordered by index across the ledger's whole history.

- **I8 (corrections are entries).** A correction to the record is itself an entry: if e_j corrects or amends e_i, then j > i and e_j names index i in its fields. The record's history is therefore recoverable from the appended sequence alone; nothing is repaired by rewriting.

- **I9 (status as the designated mutable field).** Of the four fixed fields of an appended entry, S_i is the designated mutable field: it alone may change after append, the core projection core(e_i) being immutable per I7. Corrections to the record are themselves filed as entries per I8; the record specifies no status-mutation semantics beyond this designation.

**Enforcement remark (procedural, not cryptographic).** I7 to I9 are enforced procedurally: a single serialising writer, the orchestrator seat, performs every append, and other seats propose entries rather than writing them [E10-C05]. There is no hash chain, no Merkle consistency proof, and no external witness; a violation of I7 would not be detectable from the ledger alone. The invariants' evidential force therefore rests on the writer discipline and on the surrounding record that cites entries by identifier under the contemporaneity rule above [E10-C27], not on a verification algorithm. This is precisely the difference Section 5 draws against transparency-log mechanisms, in which the append-only property is cryptographically auditable by any third party; the two enforcement classes must not be conflated, and this paper does not conflate them.

### 3.4 The two-register discipline

The formal register uses mathematical vocabulary exclusively, under a fixed translation map from the narrative register's terms to formal ones; the narrative register is held upstream in the programme's narrative corpus and appears in no formal artifact [E10-C01]. Between them sits an extraction layer: formal artifacts cite extractions; extractions restate and trace to sources in a closed registry; the narrative corpus is never cited directly at a formal tier. The direction of production is fixed: formal first, narrative harvested afterwards at a designated beat, with "no emergence" recorded as a valid outcome of a cycle, so the absence of narrative yield never pressures the formal work to produce it.

The discipline is stated as checkable by the reader in the programme's public-facing corpus [E10-C01]: one conjecture register spans every expression; the derivation direction is one-way; a narrative unit that instances a conjecture cites it; and a figure that merely resonates is marked resonance, not derivation.

One dating qualification is carried here because the record requires it [E10-C01]. The fixed formal-first direction is evidenced from the programme's mid-2026 operating documents onward; an earlier process document records a flow in which a narrative unit preceded its research note and could introduce register candidates. The programme's retrospectives read this as method evolution (the method was learned, not given [E10-C28]); this paper reports the direction rule with its dated scope rather than as a timeless property, and the tension between the dated record and one undated later statement of the rule is filed in the programme's ledger, not smoothed here [E10-C25].

**Definition 4 (registers and mediation graph).** Let Φ be the set of formal artifacts, X the set of extraction units, and Nar the set of narrative units, pairwise disjoint, and let Ext be the external literature. Over these units the record's discipline determines two directed relations: cite (u cites v as a source) and der (v is produced from u; the production direction) [E10-C01].

The production discipline of the prose above is exactly the following three invariants [E10-C01].

- **I10 (derivation direction).** Every derivation edge between the registers runs from the formal side to the narrative side: der contains edges from Φ into Nar (narrative harvested from the formal work at the designated beat) and no edge from Nar into Φ. A cycle with no harvest records "no emergence"; the empty harvest is a valid value of the relation, not a failure of it.

- **I11 (citation mediation).** For every formal artifact f ∈ Φ, the sources of f satisfy cite(f) ⊆ X ∪ Ext; in particular cite(f) ∩ Nar = ∅. No formal artifact cites a narrative unit directly; extractions restate and trace to sources in the closed registry, so every path from a formal artifact to the narrative corpus factors through the extraction layer.

- **I12 (the one narrative-to-formal channel).** Narrative-to-formal influence is confined to candidate adoption: a narrative unit, like any non-formal source of conjecture-shaped residue (Section 3.1), may give rise to an unnumbered candidate, and a candidate enters the formal register only through the human-licensed minting event of invariant I4 [E10-C12]. The channel's evidence is dated: the record's instances of a narrative unit introducing candidates lie in the earlier flow that the temporal index below excludes, and the candidate instances on the record within the invariants' dated scope arise from agent work, not narrative units [E10-C01][E10-C12][E10-C25]. Within that scope the narrative-sourced case therefore stands at design status, licensed by the candidate-adoption rule, which admits candidates from any non-formal source, and not yet exercised. Composing I10 to I12: the only path from Nar into the formal register passes through the candidate set and the human principal; no agent-mediated path exists.

**Temporal index (the dated qualification, preserved).** I10 to I12 carry the dated scope stated in the paragraph above: they are design invariants of the method as operated from the programme's mid-2026 operating documents onward [E10-C01]. The earlier recorded flow, in which a narrative unit could precede its research note and introduce register candidates, violates I10 as stated; the record reads the change as the point at which the direction was fixed, method evolution rather than timeless property [E10-C25][E10-C28]. This paper asserts the invariants from that dated point and not earlier, and the residual tension with one undated later statement of the rule remains filed in the programme's ledger, not smoothed here (Section 6).

### 3.5 Auxiliary instruments

Five further instruments recur in the record and are reported for completeness, since the method's operation depends on them.

**Resumable driving documents** [E10-C18]. A fresh agent session with no memory resumes the whole programme by reading one driving document top to bottom and executing the first item whose status is not done; the document carries its own state table, run log, and exit criteria, and is updated at every close beat. The property extends to supersession: a superseded plan's own header records that it is superseded and names the operative driver, so the stale and the live document each state which is which. Jointly with resume-verify-disk recovery [E10-C07], this makes continuity a property of the artifact set rather than of any session's memory.

**Dated, verdict-first plans that hold what is not theirs to decide** [E10-C21]. Plans carry their own status including supersession, subordinate writing to reconciliation (nothing downstream numbers anything until the register consolidation closes), carry a priority collapse so partial execution has a defined order, and keep a standing section of open decisions held for the human principal.

**Origin-first reflection** [E10-C22]. While a research path runs, no agent edits any repository outside the origin; outward-reflecting changes are accumulated as one-line entries in a reflection ledger and executed after the path closes and its gate signs, as one focused pass per target in declared impact order, with per-pass checks and a wave log that records outcomes honestly at target granularity, including partial completion with the remainder itemised and skips with reasons.

**Read-only standing surveys** [E10-C29]. A per-repository daily survey reads the estate and changes nothing but itself: current state, a coverage table, prioritised suggestions with reasons, and uncertainties with the inference method stated. Its discipline extends the gate rules to reconnaissance: proposals are drafted to application readiness and explicitly not applied ("the proposer does not approve its own proposal"); actions reserved to the human are listed as such; and carried-forward items are marked stale-still when a prior suggestion was not applied, so non-execution is visible rather than silently re-proposed.

**Built, never hand-edited, structured data** [E10-C30]. Where the narrative register carries structured data releases, each version is a structured-delta patch merged by a dedicated idempotent script that publishes its own verification block (counts, presence checks, validity, integrity) in the release chronicle; byte-identical copies are verified before any external pin, superseded pins are kept as lineage, and the pin itself is the human's manual step. This rule too was earned by failure: one version's prose merged while its structural sections were never applied; the next version was built on the incomplete head and inherited the divergence; the human principal's read caught it; and the repair shipped as a dedicated reconciliation release with the root cause traced and stated.

## 4 Evidence from Operation

### 4.1 The two instances

The method's primary instance is the paper pipeline itself: research artifacts driven up the gate ladder under adversarial review before a human commits to them. Within the recorded operating window, two papers were driven to the awaiting-completion state under the full ladder, each with every gate on the record [E10-C02]; the same window contains the enforcement instances cited throughout Sections 2 and 3.

The second instance is a workshop in a different domain: blind optimisation of a compiled constraint system under a held-out verification gate, recorded in the programme's corpus as the second instance of the same trust-gated loop template [E10-C15]. This paper carries the second instance at claim level only, under the instance's own integrity fence: its mechanisms, resource counts, internal tier structure, and submission strategy are withheld from this record and form no part of any claim here. What is carried is the loop shape, the four operating rules of Section 4.2, two pre-registered probes whose honest outcome was "cannot decide", and the killed-levers rationale of Section 2.2. The two instances shared no code, no seats, and no artifacts [E10-C15].

### 4.2 Rules earned twice

Four operating rules arrived independently in both instances, in different forms. The record's own assessment is quoted for exactly what it claims and no more: "Two domains, one discipline, convergent rules", a convergence the record names the strongest evidence the template carries [E10-C15]. This paper reports the convergence as observed, not as derivation proven.

- **Non-vacuous checkers** [E10-C06]. Pipeline: the vacuous-green defect and its structural close (Section 1; Section 2.2). Workshop: certificate checkers were unit-tested against deliberately corrupted inputs before their pass was believed, on the stated ground that a verification pass reporting success on zero items is suspect.

- **No trust in interrupted-run state without verification** [E10-C07]. Pipeline: at least five interruption events were recovered by resuming the same agent against verified disk state, with nothing rebuilt, including one review memo that survived a mid-close-out kill complete to its last finding. Workshop: an assay found its own prior verdict on disk from an interrupted run and refused to trust it, re-executing every decision-bearing number. Jointly the rule's full form: trust the disk for work products after verification; trust no decision-bearing verdict without re-execution.

- **Pre-registered verdict rules, with "cannot decide" honoured** [E10-C08]. Pipeline: both paper review loops closed by a targeted re-check against the review memo's own pre-stated successor criterion, each saving a full second review. Workshop: probes declared success and failure branches before running; twice the pre-registered instrument could not decide, and the filing said so.

- **Negative results at win-prominence** [E10-C11]. Pipeline: the rule is standing in the chronicle format (a mandatory reversals section) and exercised; one seat chronicle records a failed re-derivation as part of the evidence of record. Workshop: the killed-levers record at win-prominence is what made a closure statement over the search space possible at all.

### 4.3 The same-day revision loop

The pipeline's recurring unit of review work is a same-day loop [E10-C09]: an adversarial persona review returns a major-revision verdict with priced findings; findings are routed by competence (mathematical legs to the formalist seat, prose legs to the translator seat), serialised on the one file with an explicit handoff; the orchestrator runs a targeted re-check against the reviewer's pre-stated successor criterion; and a clean re-check constitutes review-gate evidence with no second full review. Three instances closed same-day in the recorded window: one with a single major self-contradiction plus four minor findings; one with one blocking finding (a proposition false as stated, with a hand-built counterexample and a named fix) plus four major and eight minor; one with zero blocking, four major, and five minor findings, the zero-blocking outcome following the fix-known-findings-before-review rule of Section 2.2 [E10-C09][E10-C10]. In each case the artifact's mathematical core had survived independent re-derivation at the review seat, which is what confined the loop to statement and prose legs [E10-C09].

### 4.4 The method catching its own instruments

A further class of operating evidence is reflexive: the method's instruments failed, and the method caught them. Two episodes already reported above are gathered here with a third, deliberately, because a methods paper that reported only its instrument's successes would fail this method's own honesty rule [E10-C26]. First, the vacuous-check episode: green check evidence stood in the record for two gates; the consistency station caught it; one seat disclosed its own vacuous history unprompted; the correction was ledgered and the defect closed structurally [E10-C06]. Second, the strengthening episode: the named generative failure mode fired where predicted and was caught by a mechanical sweep of counting claims [E10-C14]. Third, the instrument-generation record [E10-C24]: the programme's coherence instruments evolved through four named generations (hand-ticked propagation checklists; review-only audits with priority tiers, together with per-document convergence studies and coherence reports with honest gap tables; a recorded verdict that coherence by hand had stopped scaling, with a deterministic audit-tool build specification whose acceptance test was reproducing known findings; deterministic checks proven non-vacuous), and the record preserves each generation's failure rather than its self-report. The first generation's terminal artifact asserts, in its completion summary, one hundred and eleven of one hundred and eleven items complete, while its own body still carries items marked not started, with unticked boxes; a companion document repeats the completion claim. The contradiction stood unnoticed in the corpus until the present extraction sweep found it; it is filed in the programme's ledger, the completion figure is treated as unreliable, and the finding is reported here as content: what caught the first generation's overclaim was not a later generation of the coherence instrument, whose fourth generation is the deterministic checks proven non-vacuous, but the extraction sweep behind this paper, operating under the trace-or-delete discipline of Section 2.2 [E10-C24][E10-C04]. An earlier draft of this paragraph itself misattributed that catch to the fourth-generation instrument, an instance of the named strengthening failure mode of Section 2.2 firing inside the paper that names it; the paper's own adversarial review station found the misattribution, and this revision corrects it on the revision's own record.

The record also retrospects its own method at the honesty grade it applies to results [E10-C28]: the earliest era's retrospective keeps its "not yet practiced" cells; a middle era's retrospective keeps the era's reach distinct from its grasp and records a numbering failure as part of the path; and the latest era's retrospective closes with its standing opens. One further discipline observation from the record bears on this paper's own novelty posture: the programme's rule, learned at an external convergence event, is that independent arrival at the same structure is evidence of structure and never a priority claim [E10-C28]. Section 5 applies that rule to this method.

## 5 Related Work

The concessions come first; every component of this method has strong prior art, and the paper's novelty claims survive only at the assembly and inversion level stated in Section 1.1.

**Pre-registration and Registered Reports.** Peer review of protocols before data collection, with in-principle acceptance independent of outcome, is established practice (Chambers 2013, at over three hundred journals); the preregistration revolution distinguishes prediction from postdiction by committing hypotheses and analysis decisions to a public record before outcomes are observed (Nosek et al. 2018). The numbered public problem list is itself far older prior art: Hilbert's 1900 list, cited here at its Bulletin translation (Hilbert 1902), established the numbered register of open problems as an organising instrument for a research community, and this method's register numbering is synthesis of that tradition. The pre-registration posture of this method's verdict rules [E10-C08] and the register-before-result posture of its conjecture register [E10-C12] are synthesis of this line. What neither line contains, so far as the sweep found: a standing register of live conjectures carrying estimator-attributed confidence bands and falsification conditions, governed continuously across a programme; severity-priced findings as advance contracts; and a reviewer ruling on its own successor criterion with a machine-run re-check against it.

**Adversarial collaboration, calibration, assurance cases.** Structured good-faith adversarial testing between rivals is canonical (Kahneman and Klein 2009); calibrated probability-banded forecasting with team deliberation is established (Mellers et al. 2014); structured claim-evidence-argument decomposition with every leaf tracing to evidence is the assurance-case discipline (Kelly and Weaver 2004). This method's adversarial review seat [E10-C09][E10-C14] and trace-or-delete rule [E10-C04] are synthesis of this family. What the family does not contain: a standing adversarial seat re-instantiated per artifact inside an agent fleet.

**Multi-agent research pipelines and agentic review.** The AI Scientist automates the full pipeline from idea to paper, including a simulated automated peer review reported at near-human score agreement (Lu et al. 2024); Agent-as-a-Judge evaluates agent systems with agentic evaluators, approaching human-evaluation baselines (Zhuge et al. 2024). The fleet shape and role separation of this method [E10-C13] are synthesis of this family, and the family is also the sharpest contrast available: the AI Scientist automates the final review, which is exactly what this method's completion gate forbids [E10-C02]. Agentic judging is the delegated gate the method structurally refuses; the differentiator is non-delegability, not role separation.

**Append-only logs.** Certificate Transparency defines a publicly auditable, append-only log whose append-only property is enforced by Merkle-tree consistency proofs, making equivocation efficiently detectable (Laurie, Langley and Kasper 2013). The append-only property of this method's ledger [E10-C05] is synthesis of this mechanism family, with an explicit difference in enforcement: the critiques ledger's invariant is procedural (one serialising writer; corrections filed as entries), not cryptographic, and Section 3.3's enforcement remark says exactly this. Electronic laboratory notebook practice provides tamper-evident chronology for research records generally; no specific record from that literature is adopted here (Section 6).

**Negative-results norms.** Registered Reports demonstrably surface null and negative findings: the positive-result rate falls from ninety-six percent in the standard literature to forty-four percent under the format (Scheel, Schijen and Lakens 2021). The win-prominence rule [E10-C11] is synthesis of this norm. What the norm's literature does not contain: the rule applied reflexively to a research path's own dead ends, with the resulting enumerability of the searched space used to license closure statements.

**Non-vacuous checks.** Mutation testing requires a test suite to detect seeded faults (DeMillo, Lipton and Sayward 1978); checked coverage detects tests that execute code but never check the result, and is reported as more sensitive to oracle weakness than mutation testing (Schuler and Zeller 2011). The non-vacuous-checker rule [E10-C06] is a generalisation of exactly this principle from unit-test oracles to research-process checkers, with the failure hard-wired as an exit code and with the self-caught vacuous-green audit of Section 4.4 as its operating instance.

**The two inversion anchors.** Domain-driven design cultivates a single ubiquitous language shared by domain experts and developers within a bounded context (Evans 2003); this method deliberately maintains two registers with a fixed one-way production direction and a no-direct-citation fence between them [E10-C01], and the claim is confined to that inversion. Stage-gate development staffs go/kill gates between stages with human gatekeepers (Cooper 1990); those gates are managerial resource decisions, and nothing in the model forbids the executing system from recording a gate as passed; this method's terminal gate is an epistemic completion gate reserved from the automation that prepares it, as a machine state [E10-C02], and the claim is confined to that inversion.

With the concessions stated, the novelty ledger of Section 1.1 can be re-read at its intended width: the assembly (N1 in the fence's numbering), the two inversions (N2, N3), and convergence-as-validation (N4). No found work assembles a confidence-banded conjecture register, a gate ladder with a machine-state non-delegable human completion gate, an append-only adversarial ledger, and a two-register vocabulary discipline into one governance method for agent-operated research; the claim carries a "to our knowledge" qualifier and is falsified by a single counterexample, which the register process would file at the prominence this method requires [E10-C11].

## 6 Limitations

**Two instances, one team.** The method has operated in exactly two instances, both within one programme, sharing the same human principal and the same governing documents' authorship. The convergence evidence of Section 4.2 is therefore evidence of transfer across domains, not across teams or institutions; the transfer claim is confined to Section 7's hypothesis and nothing here should be read as established generality [E10-C15].

**Process-record evidence class.** Every operating claim in this paper is evidenced by the programme's own contemporaneous record. The record is structured against self-flattery (append-only ledger [E10-C05]; frozen chronicles with the contemporaneity rule [E10-C27]; a limits ledger compiled only from each era's own limitation sections [E10-C26]), but it remains self-report by a single organisation, and no external audit of the record has been performed.

**Availability of the record.** The register, the ledger, and the chronicles are the evidence base of every operating claim above, so their availability status belongs in this section. At the time of this draft, the conjecture register has a public surface at the programme's specification page, the one non-literature URL this paper carries (References); the adversarial ledger and the per-session chronicles are unpublished. Whether and in what form they become available, for external audit or otherwise, is a decision reserved to the programme's principal, under the same non-delegability that covers publication (Section 3.2); that decision is recorded here as reserved, not promised, and this paper makes no availability commitment on the principal's behalf.

**The method does not guarantee correctness, and its record proves it.** A false proposition reached completion-draft before adversarial review caught it; vacuous check evidence stood in the record for two gates before an audit caught it [E10-C06]. The method's claim is narrower than correctness: in the recorded window, the defects that occurred were caught by a later instrument and filed at full prominence, and each catch produced a structural close. The record cannot show that all defects are caught; by construction it can only show which were.

**A documented unreliability in the method's own ancestry.** The first-generation coherence instrument's completion claim (one hundred and eleven items, asserted complete) is contradicted by its own body and is treated as unreliable throughout this paper; the finding is reported in Section 4.4 as content, not softened [E10-C24]. Readers should treat all first-generation completion figures in the programme's early record accordingly.

**A dated qualification on the two-register direction.** The fixed formal-first production direction is evidenced from the programme's mid-2026 documents onward; an earlier process document records a narrative-first flow. The tension between the dated record and one undated later statement of the rule is filed in the programme's ledger and reported in Section 3.4; the direction rule should be read with its dated scope [E10-C01][E10-C25].

**Unswept neighbours.** The prior-art sweep behind Section 5 was web-only, English-only, and single-session. Of its three named referee risks, one is now anchored at record and two remain open: the long tradition of numbered open-problem lists in mathematics, which anticipates register numbering (though not, so far as the sweep found, confidence-banded, estimator-attributed conjectures inside an active agent-run governance loop), has been resolved at its primary record (Hilbert 1902, the *Bulletin of the American Mathematical Society* translation of the 1900 problem list) and the comparison is argued in Section 5, with the numbering itself conceded to the tradition; electronic laboratory notebook and timestamped-record literature was surveyed as background without a primary record adopted; and the philosophy-of-science framing of confidence-banded conjectures was left unswept. The two inversion anchors (Evans; Cooper) are pinned at edition and record (Evans 2003, first edition; Cooper 1990 at its journal record).

**Withheld detail in the second instance.** The second instance is carried at claim level only, under its own integrity fence (Section 4.1). A reader cannot independently verify the workshop half of the earned-twice claims from this paper; the fence is reported rather than hidden, and the pipeline half of each claim stands on the primary instance's record alone [E10-C15].

Per the programme's standing rule, a result against this method's predictions, including a failed replication of the transfer hypothesis below, is filed to the register with the same prominence as a confirmation; this paper commits to that in writing.

## 7 The Transfer Hypothesis

The method's reusability beyond its two instances is an open, testable question, and this paper states it as such rather than claiming it.

**Hypothesis (transfer).** A research loop in a new domain, operated by a different team, that adopts the four components of Section 2.1 and operates them as specified below will, within its first sustained operating period as defined below, (i) record at least one vacuity observable, defined as either a vacuity finding filed against one of its own checkers or a checker failing a deliberately corrupted input at its adoption test; (ii) file at least one pre-registered verdict as "cannot decide" without softening; and (iii) produce a negative-results record complete enough to license at least one closure statement over a searched space. The hypothesis is grounded in the observed independent arrival of exactly these behaviours in two loops that shared no code, seats, or artifacts [E10-C15][E10-C06][E10-C08][E10-C11].

**Adoption criterion (operating the components as specified).** An adopting loop operates the components of Section 2.1 as specified if and only if its own operating record satisfies the invariant subset I_A = {I1, I2, I4, I5, I6, I7, I8, I10, I11}, each checkable from the adopting team's record alone: I1 and I2 from the register file's history (every number denotes one claim across all states; every minting event assigns the least never-assigned number); I4 from the recorded act of the human principal at every extension of dom(ρ); I5 and I6 from the loop's governing documents containing no agent-labelled transition into the complete state, from every completed artifact's terminal transition carrying the human principal's recorded act, and from the absence of agent-authored publication or version-control writes on the record; I7 and I8 from every ledger state extending its predecessor by appended entries only, with core projections unchanged and every correcting entry naming the index it corrects; and I10 and I11 from derivation edges running only from the formal side to the narrative side and from no formal artifact's source list containing a narrative unit. Three invariants are deliberately excluded from I_A. I3 is excluded because its antecedent, external citation of a number by a pinned artifact, may never fire within a new loop's first period; a vacuously satisfied conditional cannot evidence adoption. I9 is excluded because its check is the same history diff that checks I7 and I8, so it adds no independent observable. I12 is excluded because it is a composition of I4 with I10 and I11, not an independent check.

**Period (the first sustained operating period).** The first sustained operating period of an adopting loop is the interval ending with its Nth full ladder transit, where a full ladder transit is one artifact driven from draft through every agent-run gate into the awaiting-completion state, and N is fixed in advance of the test in the adopting loop's own register, per the pre-registration posture of Section 2.2; fixing N in advance is what removes insufficient operation as a retrospective escape. The proposed default is N = 3, and its grounding is stated at its true strength: the primary instance's recorded window (two artifacts driven to awaiting-completion and three same-day review loops [E10-C02][E10-C09]) grounds the order of magnitude, not the constant. Predictions (i) to (iii) are evaluated over that interval.

**Falsification and null semantics.** The hypothesis is conjunctive, so it is falsifiable severally: a null on any one of (i) to (iii), in a loop that satisfies the adoption criterion over its pre-registered period, falsifies the hypothesis as stated, and the surviving criteria then bound at most a weaker successor hypothesis, which would be filed as such. A joint null on all three would count further, against the grounding itself: it would exhibit a loop operating the same components without any of the behaviours whose independent arrival in two instances grounded the prediction [E10-C15]. Either outcome is filed at the same prominence as a confirmation, per the standing rule this paper has already committed to in writing (Section 6).

The evidence for the hypothesis is the convergence of Section 4.2 and nothing stronger: two instances, one team, one shared discipline-author. What would move the claim from hypothesis toward result is stated by the method's own promotion bar: an empirical second instance outside the originating team [E10-C23]. The instruments this paper describes are, by their own construction, the reporting apparatus such a test would need: a register to hold the hypothesis, a ladder to gate the report, a ledger to file the outcome either way, and a record kept as if a methods examiner will read it, because one will [E10-C16].

## References

All references verified at a primary record (Crossref DOI metadata, arXiv abstract, RFC record, archived scholarly record, publisher page, or initiative page) in the prior-art sweep preceding this draft and re-verified at the citation station, 2026-07-10. Evans and Cooper carry edition and record pins; the Kelly and Weaver workshop paper has no DOI and is verified at its archived scholarly record.

- Chambers, C. D. "Registered Reports: A new publishing initiative at *Cortex*." *Cortex* 49(3):609-610, 2013. doi:10.1016/j.cortex.2012.12.016. Format and adoption described at the Center for Open Science Registered Reports initiative page (cos.io), which records over three hundred journals offering the format.
- Cooper, R. G. "Stage-Gate Systems: A New Tool for Managing New Products." *Business Horizons* 33(3):44-54, 1990. doi:10.1016/0007-6813(90)90040-I. The underlying staged go/kill process is developed in Cooper, R. G., *Winning at New Products*, Addison-Wesley, 1986.
- DeMillo, R. A., Lipton, R. J., Sayward, F. G. "Hints on Test Data Selection: Help for the Practicing Programmer." *Computer* 11(4):34-41, 1978. doi:10.1109/C-M.1978.218136.
- Evans, E. *Domain-Driven Design: Tackling Complexity in the Heart of Software.* Addison-Wesley Professional, 2003 (first edition; ISBN 978-0-321-12521-7). Ubiquitous language and bounded context.
- Hilbert, D. "Mathematical problems." *Bulletin of the American Mathematical Society* 8(10):437-479, 1902. doi:10.1090/S0002-9904-1902-00923-3. The Bulletin's English translation of the 1900 Paris problem list; anchor for the numbered-problem-list tradition named in Section 6.
- Kahneman, D., Klein, G. "Conditions for intuitive expertise: A failure to disagree." *American Psychologist* 64(6):515-526, 2009. doi:10.1037/a0016755.
- Kelly, T. P., Weaver, R. A. "The Goal Structuring Notation: A Safety Argument Notation." Proc. DSN 2004 Workshop on Assurance Cases, 2004.
- Laurie, B., Langley, A., Kasper, E. "Certificate Transparency." RFC 6962, IETF, June 2013 (obsoleted by RFC 9162).
- Lu, C., Lu, C., Lange, R. T., Foerster, J., Clune, J., Ha, D. "The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery." arXiv:2408.06292, 2024.
- Mellers, B., Ungar, L., Baron, J., et al. "Psychological Strategies for Winning a Geopolitical Forecasting Tournament." *Psychological Science* 25(5):1106-1115, 2014. doi:10.1177/0956797614524255.
- Nosek, B. A., Ebersole, C. R., DeHaven, A. C., Mellor, D. T. "The preregistration revolution." *PNAS* 115(11):2600-2606, 2018. doi:10.1073/pnas.1708274114.
- Scheel, A. M., Schijen, M. R. M. J., Lakens, D. "An Excess of Positive Results: Comparing the Standard Psychology Literature With Registered Reports." *Advances in Methods and Practices in Psychological Science* 4(2), 2021. doi:10.1177/25152459211007467.
- Schuler, D., Zeller, A. "Assessing Oracle Quality with Checked Coverage." Proc. IEEE ICST 2011, pp. 90-99, doi:10.1109/ICST.2011.32; journal version, "Checked coverage: an indicator for oracle quality", *Software Testing, Verification and Reliability* 23(7):531-551, 2013, doi:10.1002/stvr.1497.
- Zhuge, M., Zhao, C., Ashley, D., Wang, W., Khizbullin, D., et al. "Agent-as-a-Judge: Evaluate Agents with Agents." arXiv:2410.10934, 2024.

The research programme whose governance record this paper reports maintains its public specification at https://agentprivacy.ai/model. This is the only non-literature URL this paper carries, per its claim discipline.

---

### Trace map (pipeline apparatus; stripped at release with the inline markers)

Every claim-bearing passage carries an inline [E10-Cnn] marker; this map records consumption per section, with STATUS as carried in the extraction (two admitted values: Method-rule (process-record); Process-observational (process-record)). Nothing in this draft exceeds its extraction STATUS: no rule is asserted as optimal, complete, or sufficient; earned-twice claims carry both earning events; the circuit-workshop instance appears at claim level only per its integrity fence; quotes are verbatim from E10's carried wording.

- Abstract: E10-C01, E10-C02, E10-C05, E10-C12 (Method-rule); E10-C06, E10-C14, E10-C15 (Process-observational). The commitment sentence is a GR-8 obligation, not a claim.
- Section 1: E10-C05, E10-C16, E10-C19 (Method-rule); E10-C06, E10-C09 (Process-observational). The false-proposition and vacuous-green episodes are carried from the extraction's anti-strengthening fence and E10-C06/E10-C09 wording.
- Section 1.1: N1-N4 per the binding novelty fence, each stated no wider than the fence wording; markers E10-C01, E10-C02, E10-C03, E10-C05, E10-C12 (Method-rule); E10-C06, E10-C07, E10-C08, E10-C11, E10-C15 (Process-observational).
- Section 2.1: E10-C01, E10-C02, E10-C05, E10-C12, E10-C13 (Method-rule).
- Section 2.2: E10-C04, E10-C10, E10-C13, E10-C14, E10-C17 (Method-rule); E10-C06, E10-C07, E10-C08, E10-C11 (Process-observational); E10-C28 (Process-observational; "learned, not given").
- Section 3.1: E10-C12, E10-C20, E10-C21 (Method-rule); E10-C29 (Method-rule; the survey instrument as catcher); E10-C17 (Method-rule; erratum instance). Stub 4 DISCHARGED at draft-v2 (Definition 1, I1 to I4; A3 ruled it stands alone rather than folding into Section 3.3, remark in place).
- Section 3.2: E10-C02, E10-C03, E10-C19, E10-C23 (Method-rule); E10-C06 (Process-observational, invocation-on-record wording). Stub 1 DISCHARGED at draft-v2 (Definition 2, I5 and I6; non-delegability as an absence of transitions).
- Section 3.3: E10-C05, E10-C16, E10-C26, E10-C27 (Method-rule). Stub 2 DISCHARGED at draft-v2 (Definition 3, I7 to I9; the enforcement remark states the procedural class exactly, and the Section 5 contrast now cites it).
- Section 3.4: E10-C01 (Method-rule, including the dating addendum, carried with its dated scope); E10-C25 (Method-rule; consumed ONLY for its dating-note evidence, see below); E10-C28 (Process-observational); E10-C12 (Method-rule; the candidate-adoption routing cited at I12, added at revision 1). Stub 3 DISCHARGED at draft-v2 (Definition 4, I10 to I12; the dated qualification preserved as an explicit temporal index; I12's narrative-sourced case narrowed to dated design status at revision 1, L107 MINOR-5).
- Section 3.5: E10-C07, E10-C18, E10-C21, E10-C22, E10-C29, E10-C30 (Method-rule).
- Section 4.1: E10-C02 (Method-rule; two papers to awaiting-completion); E10-C15 (Process-observational; instance description and fence statement).
- Section 4.2: E10-C06, E10-C07, E10-C08, E10-C11, E10-C15 (Process-observational; both earning events per claim; the workshop halves at claim level only).
- Section 4.3: E10-C09 (Process-observational; three instances with finding counts as extracted); E10-C10 (Method-rule).
- Section 4.4: E10-C06, E10-C14, E10-C24, E10-C28 (Process-observational except E10-C14 Method-rule); E10-C26 (Method-rule; the honesty ground for gathering failures); E10-C04 (Method-rule; the trace-or-delete discipline under which the extraction sweep caught the 111/111 overclaim, reattributed at revision 1, L107 MAJOR-1). The unreliable completion figure is reported as unreliable, per the extraction's Contested item 1. The revision-record sentence (the misattribution found by this paper's own review station and corrected) carries no extraction claim; it reports this draft's own revision history (the L107 record), on the abstract-commitment-sentence pattern.
- Section 5: external literature per reviews/WP-27_prior_art.md (S1-S6 conceded family by family; N1-N4 confined); E10 markers where the method's side of each comparison is stated: E10-C01, E10-C02, E10-C04, E10-C05, E10-C12, E10-C13 (Method-rule); E10-C06, E10-C08, E10-C09, E10-C11, E10-C14 (Process-observational).
- Section 6: E10-C01, E10-C05, E10-C25, E10-C26, E10-C27 (Method-rule); E10-C06, E10-C15, E10-C24 (Process-observational). The unswept-neighbour paragraph carries no extraction claim; it restates the prior-art review's own limits section (UNVERIFIED items not cited, per instruction). The availability paragraph (revision 1, L107 MAJOR-4 ruling) carries no extraction claim: it states current fact about this pipeline's own record and records the release decision as reserved to the programme's principal, not promised.
- Section 7: E10-C15 with E10-C06, E10-C08, E10-C11 (Process-observational; hypothesis grounded on the convergence claim only); E10-C16, E10-C23 (Method-rule; the promotion bar and the reporting apparatus); E10-C02, E10-C09 (Process-observational per E10-C09, Method-rule per E10-C02; the period clause's grounding, stated in-text as order of magnitude, not the constant; revision 1, L107 MAJOR-3). The adoption criterion and null semantics reference Definitions 1 to 4's invariants and the hypothesis's own logical form; they mint no new claim.

**Consumed (30 of 31):** E10-C01 through E10-C24, E10-C26 through E10-C30 fully; E10-C25 partially, for its dating-note evidence only (the pre-autopath production order and the tension routing). E10-C25's main content, the substrate-by-substrate propagation checklist and version-bump semantics, is a release-logistics discipline orthogonal to the four governance components and is not presented as part of the method.

**Not consumed (1 of 31), and why:** E10-C31 (skill-to-vertex discipline): term-level traceability of an operational skills corpus to the formal model is an instance-specific inventory discipline, not a component of the governance method; its one-authority pattern is already carried by E10-C12 and its provenance-honesty pattern by E10-C26/E10-C27. Consuming it would widen the paper's method claim beyond the four components the task card fixes.

**Claims needed but absent from E10, not invented (GR-9):** none. Where the paper wanted a formal statement (four sites), draft-v2 supplies a definition with numbered invariants that formalise the prose specification and nothing beyond it (Definitions 1 to 4, invariants I1 to I12; every invariant is a design invariant at process-record grade, per the Section 3 preamble); where it wanted transfer generality, Section 7 states a hypothesis instead. A3 sweep note (draft-v2): three sentences were reworded to observational strength (Section 1 backlog sentence; Section 4.4 opening, whose superlative collided with the attributed superlative of Section 4.2; Section 6 catch claim, from present-universal to recorded-window); no marker was added or removed, and no claim was widened.
