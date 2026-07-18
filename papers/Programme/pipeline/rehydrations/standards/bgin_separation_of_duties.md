---
wp: WP-09
tier: S
artifact: discussion-paper
title: Separation of Duties for Personal AI Agents
status: release-draft-v3 (P1 marked at L120; chain complete, the runtime touches this WP only in sweeps; frontmatter levelled by A0 at the cycle-13 sweep, L128/F2)
role: A2+A8
date: 2026-07-10
change_note: v3 (A2, 2026-07-10) revision 1 per the L118 review (A5 memo, 0 BLOCKING / 3 MAJOR / 5 MINOR) under the three A0 rulings; MAJOR-1 legibility edit inside the section 2 guarantee passage (Y_S/Y_M defined at first use, one plain-language reading sentence, nothing weakened, all four GR-7 elements intact); MAJOR-2 per ruling 2 (active attribution of the implementation record to the proposer's own design documents; availability sentence in reserved form, no commitment minted); MAJOR-3 per ruling 1 (section 2 sentence + deliverable 2 clause on who estimates H(X) and over what scope; OQ-1 wording unchanged); MINORs 1-4 per the memo's what-satisfies lines; MINOR-5 per ruling 3 (offering clause struck, OQ-5 unchanged); claim spine, eight open questions and four deliverables otherwise unchanged (L111). Prior v2 (A8, 2026-07-10): venue-grounding expansion per the WP-09 A8 card
gate_target: P1 marked (L120; the L118 successor-criterion re-check passed; remaining acts = first-person Block #15: authorship + interests, availability form, submission decision)
handoff: the first person (venue 2026-10-15/16)
venue: BGIN Block #15, 2026-10-15/16, Washington D.C. (L061; re-verified live at bgin-global.org/events 2026-07-10)
extraction_basis: E1 claims c01, c02, c04 (proven-conditional), c09, c10, c11, c27 (empirical-external), c06, c36, c37, c38 (design-status, consumed as design descriptions per the task card); conjecture-status claims c07, c08, c19, c22, c31, c32 appear only as explicitly labelled open questions in section 4; e1-c17 and e1-c18 excluded (interpretive grounding, per the L031 precedent)
due_external: 2026-10-15
---

# Separation of Duties for Personal AI Agents

## Structural Separation for Agentic Key Custody, Transaction Authority and Identity Credentials · Discussion Paper Proposing a Work Item

<!-- ============================================================
A2 HANDOFF NOTE (pipeline apparatus; REMOVE BEFORE ANY RELEASE)

Draft-v3 (A2, 2026-07-10): revision 1, the L118 station. All nine
findings of the A5 review (memo on the A5 task card) resolved
under the three A0 rulings recorded at L118. Narrowing directions
only; no claim strengthened; every edited sentence re-checked
against its e1 row's STATUS. Per leg:
- MAJOR-1 (section 2 guarantee passage): Y_S and Y_M defined at
  first use (the two agents' respective observations of the data
  subject); one plain-language reading sentence added inside the
  same passage (the two channels jointly convey at most an R_max
  fraction of the private state's information; success
  probability at most R_max, which restates the error floor and
  adds no claim). The passage remains one passage; the
  preconditions, the declarable deficit condition, the R(t)
  time-indexing and the incomplete-as-stated rule are untouched.
  A0 spot-trace of the passage expected next.
- MAJOR-2 (implementation record, ruling 2): the record is
  attributed actively as the proposer's own design documents;
  the availability sentence is added in RESERVED form only
  (addressed at release alongside the author block and statement
  of interests; the L107(2) principle: no commitment minted by
  the runtime, the first person decides the form at release);
  the three implementation statuses stay verbatim.
- MAJOR-3 (ruling 1): one sentence after the section 2 guarantee
  passage and one clause in deliverable 2 state that who
  estimates H(X), and over what scope of private state, is part
  of what the work item's evaluation guidance must specify, as a
  work-item question. OQ-1 wording unchanged.
- MINOR-1: "the two territories" -> "the two storage contexts";
  "proposing seat / checking seat" -> "proposing role / checking
  role".
- MINOR-2: the record's lead harmonised to the section 6
  rendering (one layer deployed as described, one specified with
  code not written at its specification version, one built
  instance at the workflow layer).
- MINOR-3: the EU-acquis sentence reworded to a genuine scope
  statement (a mapping task the work item could take up, not
  this paper's claim).
- MINOR-4: "cannot express" -> "does not express" (:211 area).
- MINOR-5 (ruling 3): "Offered as a candidate planning input for
  key-management practice" struck from OQ-5; the OQ itself
  unchanged.
Untouched, per the card's out-of-scope line: venue facts (A8's,
verified), the OQ set and deliverable set beyond the ruled
touches, canon, manifest, ledger, extractions.

Draft-v2 (A8, 2026-07-10): the venue-grounding expansion, per the
WP-09 A8 card. The claim spine, the eight open questions and the
four deliverables are unchanged (L111: reframe only, never add,
remove or promote). The GR-7-complete guarantee passage in section
2 is byte-identical to v1. All lowercase claim markers are
untouched. Every addition is a venue fact or a verified external
reference; per-item provenance below.

VERIFICATION RECORD (A8, all fetched 2026-07-10):
(1) Block #15: 2026-10-15/16, Washington D.C. Verified live at
    bgin-global.org (home announcement) and bgin-global.org/events
    ("Block #15 Meeting", October 15-16, 2026, Washington, D.C.).
    Agrees with the L061 correction.
(2) Working group name and remit: the live working-group registry
    (bgin-global.org/activities/working-groups) styles the group
    "IAM, Key Management and Privacy (IKP) Working Group" (active),
    remit: "guidance and good practice documents" describing
    identity (including keys) and access management for access to
    crypto-currency exchange; identity (including keys) and access
    management using Blockchain/DLT for online resource access;
    and privacy considerations for those systems. NOTE: the task
    card's gloss "Identity, Key Management and Privacy" is not the
    site's current form; the site's "IAM, ..." form is used
    throughout this draft. The group's document forum styles it
    "IAM, Key Management & Privacy (IKP)".
(3) Document class: study report, with BGIN SR numbering. Verified
    at the Wallet Governance, Policy and Key Management Study
    Report page (bgin.discourse.group/t/wallet-governance-policy-
    and-key-management-study-report/492: "BGIN SR 00**", working
    draft, IKP WG). "Discussion paper" remains this paper's
    self-description of genre only: no published BGIN taxonomy
    naming that class was verifiable, so no such taxonomy is
    asserted (the deadlines-registry line "discussion papers per
    WG process" is the pipeline's own record, not a published
    venue fact).
(4) In-genre exemplars: (a) Wallet Governance, Policy and Key
    Management Study Report (IKP WG, working draft, SR series),
    verified at its forum page as in (3); (b) "Study Report:
    Zero-Knowledge Proofs (ZKPs) - Technology and Applications",
    listed as published in the IKP WG document-forum category
    (bgin.discourse.group/c/working-group-s/ikp-wg/8). The same
    category listing verifies current IKP drafting and discussion
    activity: proof-of-personhood draft report (with a
    dual-agent-systems discussion topic), crypto-agility and
    PQC-migration draft report, privacy-enhanced authentication
    and key management draft report, accountable wallet, and
    agentic-framework material.
(5) IEEE 7012: verified at standards.ieee.org/ieee/7012/7192/:
    "IEEE Standard for Machine Readable Personal Privacy Terms",
    active standard, approved by the IEEE SA Standards Board
    2025-11-04, published 2026-01-20.
(6) ToIP: verified at trustoverip.github.io/tswg-tsp-specification:
    "Trust Spanning Protocol (TSP) Specification", status "vs1.0
    Experimental Implementor's Draft Rev 2", stated as the
    spanning-layer protocol of the ToIP technology architecture.
(7) DIF: verified at identity.foundation (working-group listing)
    and identity.foundation/working-groups/trusted-agents.html:
    "Trusted AI Agents Working Group", scope "defining an
    opinionated, interoperable stack to enable trustworthy,
    privacy-preserving, and secure AI agents"; named work items:
    Delegated Authority Report, Delegated Authority Threat Model,
    Governance of Delegated Authority Report, and a protocol
    reference implementation (KYA-OS) for delegation and
    cryptographic agent identity.

KEPT GENERIC, with reasons (the station's named failure mode is
inventing process detail):
- BGIN's work-item adoption and approval procedure: no published
  procedure was located; section 4 asks for a session and leaves
  the adoption decision and drafting mechanics to the working
  group's usual practice, unspecified.
- Editorial and review process, document numbering beyond the SR
  series, and any co-chair or seat particulars: not verifiable at
  a public page; omitted (author-block material at release).
FETCH DEAD-ENDS (recorded per the card): bgin-global.org/news/
ikp-webinar (IKP agentic-framework webinar item surfaced in
search) returned 404; papers.ssrn.com abstract 4449592 (soulbound
tokens study report, IKP WG) returned 403. Neither is cited; the
agentic-framework and dual-agent-systems facts used in section 3
rest on the working-group category listing in (4) only.

WHAT CHANGED AT V2, structurally: Purpose gains a one-sentence
routing to the IKP WG and Block #15; section 3 gains a
venue-routing paragraph (remit verbatim-adjacent, current slate,
continuity sentence marked synthesis); section 4 heading text
reframed to the adoptable shape (scope statement unchanged;
deliverables carry document classes; open questions carried as
the proposed study agenda; a proposed-first-session paragraph
added); section 5 lead adjusted for the venue-continuity
paragraph, BGIN exemplar paragraph added, and the three external
paragraphs grounded (IEEE status and dates; TSP name, status and
layer; DIF working-group name and work items). References updated
to match. RELEASE CHECKLIST below unchanged; the "verified
2026-07-10" datelines in body markers strip with the markers.

Draft-v1 (A2, 2026-07-10), for the A8 standards-expansion station.

GENRE. This is a discussion paper proposing a work item, not a
policy brief. The register is consensus-seeking and problem-framing-
first: the paper states a problem class with the field's evidence,
offers one candidate architectural pattern with its full
conditioning, argues venue fit, and hands the community a scoped
work item whose open questions are explicitly labelled. It imposes
no obligations on addressees; WP-02's recommendation machinery is
deliberately absent. Venue mechanics (working-group routing,
document class, review process) are stated generically per the task
card's out-of-scope line; A8 grounds them.

CONSUMPTION RULINGS TO SURFACE TO A0 (proposed ledger entry
returned with this draft; not appended, ledger out of scope for
this card):
(1) Design-status admission. The task card's spine names e1-c06,
    e1-c36, e1-c37, e1-c38 (design-status) for sections 2 and 3.
    E1's TIER-S filter note (the L031 reconciliation) reads as an
    exhaustive allow-list built for WP-02 (proven-conditional core
    plus the empirical-external rows "only"), and the FEEDS lines
    of those four claims do not name WP-09. The card governs this
    draft; every design-status claim is consumed as a design
    description, never as a guarantee, with implementation status
    carried verbatim (specified-not-built, one-built-instance).
    The tension between card and filter note is flagged, not
    resolved here.
(2) Off-FEEDS open questions. OQ-2 and OQ-3 trace to e1-c08 and
    e1-c07, whose FEEDS name the theory and benchmark stations,
    not WP-09. They are consumed as labelled open questions only,
    under the card's rule that conjecture-status claims may appear
    only as open questions. Flagged with (1).
(3) Exclusions. e1-c17 and e1-c18 (design-assumption, semantic
    grounding and interpretation) FEED WP-09 but are excluded:
    the L031 ruling on e1-c17 records that this tier admits no
    interpretive grounding, and the same reasoning covers e1-c18.
    The verified-record 2026 instances are E2 material and are not
    reached (GR-9: the extraction basis is E1); section 3's stakes
    argument is framed as this paper's synthesis instead.

CLAIM-SOURCE MAP, per section. Identifiers lowercase per L014 so
the register-reference check stays clean at this tier; they are
the extraction's claims. STATUS travels inline in square brackets;
no sentence may be strengthened beyond its carried STATUS.

- Purpose: synthesis of sections 1, 2 and 4; the classification
  distinction traces to e1-c04 (channel existence) and e1-c27
  (the policy-side instance); the exposure statement to e1-c10.
- Section 1 (problem statement): e1-c09, e1-c10, e1-c11, e1-c27
  [Empirical-external] carry the landscape, the measurements and
  the vendor instance; e1-c04 [Proven-conditional] carries the
  channel-existence distinction. The blockchain-context scoping
  sentence is this paper's framing, marked as such. The
  operation-sequence classification test appears in section 2 as
  a design definition from e1-c06 per the task card; note WP-02
  is fenced from that test at its tier pending a register-process
  ruling (its apparatus, v4). This draft's use is card-directed
  and design-labelled; see consumption ruling (1).
- Section 2 (candidate pattern): e1-c06 [Design] for the
  definition, grades and classification test; e1-c01, e1-c02,
  e1-c04 [Proven-conditional] for the conditioned guarantee, one
  passage, GR-7 complete (preconditions + capacity-deficit
  condition + R(t) time-indexing in-passage); external grounding
  family cited from e1-c01/e1-c02 CITATIONS lines (e1-c05 not
  consumed; its FEEDS do not name WP-09).
- Section 3 (venue fit): stakes argument is synthesis, marked;
  implementation record e1-c36, e1-c37, e1-c38 [Design] with
  implementation status stated verbatim from the extraction.
- Section 4 (proposed work item): deliverables synthesise
  sections 1 to 3; open questions OQ-1 to OQ-8 trace as marked
  inline (OQ-1 to the declarable-fact framing of e1-c02 and the
  stated absence of methodology; OQ-2 e1-c08; OQ-3 e1-c07; OQ-4
  e1-c06's own open-criterion statement; OQ-5 e1-c31; OQ-6
  e1-c32; OQ-7 e1-c22; OQ-8 e1-c19). Every OQ is labelled open;
  none is asserted.
- Section 5 (adjacent work): external standards facts plus this
  paper's synthesis, marked sentence by sentence. No pipeline
  document is cited (zero canon-internal citations at this tier).
- Section 6 (limits): GR-8 obligation, proportionate to tier.

RELEASE CHECKLIST: at release, strip (a) this comment, (b) the
YAML frontmatter, (c) all inline square-bracket claim markers;
then add an author/institution block, a statement of interests,
and the venue's document header per A8's expansion; and resolve
the availability of the section 3 design documents to the working
group (the form is the first person's decision at release, per
L118 ruling 2 and the L107(2) principle; until then the body
sentence stays in reserved form and mints no commitment).
============================================================ -->

---

### Purpose and proposed action

This paper proposes a work item: a separation-of-duties profile for personal AI agents that hold, or sit adjacent to, key custody, transaction authority or identity credentials. It states the problem class with the field's published measurements, describes one candidate architectural pattern together with the full conditions under which its guarantee is proven, and lists the questions a work item would need to resolve. The community is asked to review the problem framing, correct or extend the evidence base, and decide whether the work item should be taken up. [Synthesis; the load-bearing claims are carried in sections 1 and 2.] The proposal is addressed to the IAM, Key Management and Privacy (IKP) Working Group, whose remit covers identity (including keys) and access management and privacy considerations for blockchain systems, with first discussion proposed for the Block #15 meeting, Washington D.C., 15 to 16 October 2026. [Venue facts, verified 2026-07-10 at bgin-global.org]

The distinction the work item would make precise is the one current documentation does not express: between policy-enforced separation, where an inter-agent channel exists and its use is prohibited, and structural separation, where the channel is absent by construction. [e1-c04: Proven-conditional, channel-existence distinction] Current agent deployments implement the former almost exclusively, and published measurement locates the exposure precisely on the unmonitored inter-agent channels that policy permits to exist. [e1-c10, e1-c11: Empirical-external]

### 1 · Problem statement: personal AI agents meet blockchain and identity infrastructure

The problem, stated first: separation of duties between AI agents is today enforced by instructions, and instructed separation measurably leaks where the instructions do not reach.

Agentic AI deployments interpose delegated software agents between the person and the systems acting on their data; each additional agent adds observation and communication channels. [e1-c09, e1-c11: Empirical-external] In blockchain and identity contexts, those channels sit next to signing keys, transaction construction and credential presentation; the measurements below are domain-general, and this paper's contribution is to bring them to the venue where those particular assets are governed. [Scoping sentence: this paper's framing.]

The multi-agent privacy field arrived at separation-of-duties independently and repeatedly across 2025 and 2026: privacy-leakage benchmarking of multi-agent pipelines, contextual-integrity reasoning lines, and maker-checker and supervisor-worker orchestration patterns. All of these enforce the separation with prompt-level or training-level controls; none enforces it architecturally. [e1-c11: Empirical-external]

The measured consequence: in a benchmark of 1,000 scenarios and 4,979 execution traces across five frontier models, multi-agent configurations reduced per-channel output leakage to 27.2% against 43.2% for a single agent, while unmonitored inter-agent channels leaked at 68.8%, raising total system exposure to 68.9%; audits confined to system outputs missed 41.7% of violations. [e1-c10: Empirical-external] A second line of work proves that under sequential composition of N agents, each individually bounded by a per-agent leakage constraint, global leakage compounds toward a bound exponential in the chain depth, and measures average mutual information rising from 0.49 at two agents to 1.05 at five. [e1-c09: Empirical-external; the compounding bound is proven in the cited work] The unmonitored inter-agent channel is where the exposure concentrates.

A recently released vendor governance toolkit provides one documented instance of the policy-enforced class, with decentralised identifiers, an inter-agent trust protocol, policy interception and trust scoring: its own documentation records that the policy engine and the agents run in the same process and the same trust boundary, with container isolation recommended but external to the toolkit's enforcement. Violation of the separation remains possible though prohibited. [e1-c27: Empirical-external, vendor documentation] The same source records that the two layers compose rather than compete: policy governance can run above structural separation. [e1-c27] Nothing in this paper argues against policy-level governance; the argument is that documentation should be able to say which of the two classes a deployment is in, because their failure modes differ.

### 2 · One candidate pattern: two-agent separation with structural context erasure

For one deployment pattern there is a proven, conditional result. Its preconditions and its single declarable capacity condition are stated here in full, because the guarantee is empty without them, and because a work item that standardised the declaration discipline would be useful even to deployments that never adopt this particular pattern.

The pattern, as a design definition: two agents with disjoint duties, a boundary agent S facing external counterparties and a delegation agent M acting on the data subject's behalf, with structural context erasure between agent invocations, so that neither agent accumulates the other's view. Separation of this kind is classified by reachability, not by rule: if some sequence of permitted operations can reconstruct the shared origin from an agent's current state, the separation is policy-enforced; if no such sequence exists, it is structurally enforced. The design further distinguishes two grades of erasure: hiding, where the material is recoverable with the right keys (encryption, access control), and forgetting, where the design leaves no recovery path. [e1-c06: design definition; a formal criterion for the grade distinction is not settled and appears as open question OQ-4]

The conditioned guarantee, in one passage. Let H(X) be the entropy of the data subject's private state, let Y_S and Y_M be the two agents' respective observations of the data subject, let C_S and C_M be the information capacities of the corresponding observation channels, and write R_max = (C_S + C_M)/H(X). Under Precondition 1 (non-collusion: the two observation channels are conditionally independent given the data subject, formally I(Y_S; Y_M | X) = 0, and no third channel carries the inter-agent residue) and Precondition 2 (fixed adversary class: the capacities are evaluated against a stated adversary class, its compute, its inference models, its correlation methods), two structural facts are proven: the leakage of the two channels is additive rather than compounding, and the reconstruction error floor P_e >= 1 - R_max holds. In plain terms, the two channels can jointly convey at most an R_max fraction of the private state's information, so an adversary of the stated class reconstructs that state with success probability at most R_max. [e1-c01, e1-c02, e1-c04: Proven-conditional] When, additionally, the capacity-deficit condition C_S + C_M < H(X) holds, a declarable numerical fact about a given system and adversary class rather than a consequence of the architecture, then R_max < 1 and reconstruction of the private state is bounded away from certainty against the stated class, by the error floor above. The preconditions do not by themselves place R_max below one. The capacities are time-indexed: writing R(t) for the ratio evaluated against the strongest adversary class available at time t, it is the deficit condition, not the preconditions, that erodes as stronger classes arrive, and the bound says nothing about a later, stronger class. A separation or non-reconstructability claim that omits its preconditions, its declared deficit, its adversary class or its date is therefore incomplete as stated. [e1-c02: Proven-conditional, with the time-indexing carried in the claim]

The declaration has an entropy side as well as a capacities side: who estimates H(X), and over what scope of private state that entropy is taken, is part of what the proposed work item's evaluation guidance must specify, and it stands under the same absence of a standardised methodology that OQ-1 in section 4 records for the capacities. [Work-item question, stated as a work-item question; this paper's framing, no claim carried]

The compounding measurements of section 1 and the additive guarantee above do not contradict each other: they are one theorem family on the two sides of one architectural line, and the line is whether the inter-agent channel exists. The measured 68.8% inter-agent leakage is a measurement of the channel whose absence defines the Precondition-1 regime. [e1-c04, e1-c10]

None of this is a private theorem. Within its conditional regime the result is an instance of a family the information-theory literature has accepted for decades: wire-tap channel equivocation (Wyner, 1975), the source-coding converse (Fano, 1961; Cover and Thomas, 2006), secrecy capacity as a difference of channel capacities (Leung-Yan-Cheong and Hellman, 1978), and the colluding-observer failure mode that makes Precondition 1 load-bearing (Csiszar and Korner, 1978). [Citations carried on e1-c01 and e1-c02] What is proposed as new is not the mathematics but the deployment pattern that makes the preconditions hold inside an agentic AI system by construction, and the documentation discipline that makes the conditions declarable and reviewable.

### 3 · Why this problem class belongs at this venue

Venue fit, stated first: key custody, transaction authority and identity credentials are where an accumulating or compromised agent's observations carry the most consequence, and the question this paper raises, whether a claimed separation is structural or policy-enforced, is a classification and documentation question of exactly the kind standards processes exist to settle.

The routing, in the venue's own terms: BGIN's IAM, Key Management and Privacy (IKP) Working Group states its remit as guidance and good practice documents on identity (including keys) and access management for access to crypto-currency exchanges, on identity and access management using blockchain or DLT for online resource access, and on privacy considerations for those systems. [Venue fact, verified 2026-07-10 at bgin-global.org/activities/working-groups] The working group's current slate already sits adjacent to this proposal: its wallet-governance study report treats wallets as governance and identity instruments and classifies wallet types by security, privacy and usability, and its current drafting and discussion activity includes proof of personhood (with a dual-agent-systems discussion thread), crypto agility and post-quantum migration, privacy-enhanced authentication and key management, and agentic-framework material. [Venue facts, verified 2026-07-10 at the working group's document forum, bgin.discourse.group] A separation-of-duties profile for personal AI agents extends that slate rather than departing from it. [Synthesis]

The stakes argument, which is this paper's synthesis and not a measured claim: three properties of this domain raise the cost of agent-side accumulation. Settlement is irreversible, so an agent that can be steered into signing cannot be un-steered by remedy after the fact. Keys and credentials rotate at a cost, and some bindings do not rotate at all, so what an agent's accumulated context reveals about them stays revealed. And public-ledger data persists indefinitely, so whatever an agent leaks toward reconstruction remains available to every future adversary class, which is precisely the time-indexed erosion that the R(t) framing of section 2 makes explicit. [Synthesis; the time-indexing itself is carried at e1-c02]

There is an implementation record for the pattern of section 2, and it consists of the proposer's own design documents, cited here at their honest status: one layer deployed as described, one specified with code not written at its specification version, and one built instance at the workflow layer; none is an evaluated system. Its role in this paper is to show the pattern is implementable, not that it is validated. [e1-c36, e1-c37, e1-c38: Design] Availability of the design documents to the working group is addressed at release, alongside the author block and statement of interests. [Reserved form per the release checklist; no availability commitment is minted by this draft]

- A dual-runtime browser design instantiates the two erasure grades in storage: the delegation agent's signing keypair is generated once and persists across sessions, while the boundary agent's keypair is generated per ceremony and destroyed at session close. The erasure is structural (storage destruction), not instructed (policy). The binding between the two storage contexts is a manual export and import carried by the data subject; no automated inter-agent channel exists, which enforces the Precondition-1 regime by construction at this layer. Deployed as described at its specification date. [e1-c36: Design]
- A two-process design places the two agents in separate browser extension processes with separate storage and separate permissions, communicating only over an explicit message channel, a process-level instance of the separation bound. Per its own specification, the design is specified and the two-extension code is not written at specification v1.1. [e1-c37: Design]
- A workflow-level harness operationalises the same discipline for agent teams: the proposing role cannot tune to the held-out material the checking role will draw on, realising the non-collusion condition as a mechanism rather than an assumption. One instance built at the specification date. [e1-c38: Design]

### 4 · The proposed work item

Proposal, stated first: a separation-of-duties profile for personal AI agents in blockchain and identity contexts, delivering terminology, a classification method, a documentation profile and a maintained open-questions register.

**Scope.** Personal AI agents that hold keys, construct or authorise transactions, or present identity credentials on behalf of a person; the separation properties claimed between such agents; and the documentation by which those claims are made reviewable.

**Candidate deliverables**, offered for community revision, with the document class each would take in the working group's series (the study-report class is the group's published class; the guidance class follows the remit's own "guidance and good practice documents" wording):

1. **Terminology and classification** (study report). Definitions of policy-enforced versus structural separation in terms of channel existence, with a channel-inventory method: enumerate every communication channel between agents and every shared surface that could carry the inter-agent residue (shared processes and memory, shared storage, logging and observability pipelines, orchestration state, vendor telemetry), and classify the deployment by what the inventory shows rather than by what policy prohibits. [Derives from sections 1 and 2; e1-c04, e1-c27, e1-c06]
2. **Documentation profile** (guidance document). A profile under which any separation or non-reconstructability claim names its non-collusion precondition, its stated adversary class, its declared capacity-deficit condition C_S + C_M < H(X), and the date and adversary class to which the declaration is indexed; who estimates the entropy term H(X), and over what scope of private state, is part of what the evaluation guidance of deliverable 3 must specify. [Derives from section 2; e1-c01, e1-c02; the entropy clause is a work-item question, no claim carried]
3. **Evaluation guidance** (good practice document) for wallet, agent and identity vendors: what a reviewer can check today (that the declarations are present, that the channel inventory supports the conditional-independence claim, that the declared arithmetic is consistent) and what cannot yet be checked for want of a measurement methodology (whether a declared capacity is well-founded; see OQ-1). [Derives from section 2; scope of checkability stated as recommended practice]
4. **An open-questions register**, seeded with the list below and maintained as the work item's research agenda, a natural fit for the working group's document forum, where its draft reports are already developed in the open. [Venue fact on the forum's use, verified 2026-07-10; the register proposal itself derives from sections 1 to 3]

**Open questions, offered as the work item's study agenda.** Every item below is an open question. None is asserted by this paper. Several originate as unproven conjectures in the research programme that produced the pattern of section 2; they are offered to the work item as questions precisely because they are unresolved, and a negative answer to any of them would be a result worth publishing through the same work item.

- **OQ-1 · Measurement methodology.** No standardised methodology exists for measuring observation-channel capacities against machine-learning adversary classes; until one exists, the capacity-deficit condition of section 2 is declarable but not independently checkable. What should such a methodology measure, and which body should standardise it? [The declarable-fact framing traces to e1-c02; the absence of a methodology is a stated absence, not a conjecture]
- **OQ-2 · The chain break.** The compounding bound of section 1 is proven for sequentially composed agents under policy-only separation. [e1-c09] Whether deployed structural-erasure implementations in fact break the inter-agent chain and cap total leakage at additive growth is an engineering question about erasure protocols, not a theorem, and it is open. [Open question; conjecture-status at source, e1-c08]
- **OQ-3 · The quantitative gap.** Is structurally enforced separation measurably tighter than policy-enforced separation on matched workloads, and by how much? [Open question; conjecture-status at source, e1-c07]
- **OQ-4 · The grade criterion.** What formal criterion separates recoverable hiding from unrecoverable forgetting (the two grades of section 2), such that a reviewer could assign a grade from design documentation? [Open per the design definition's own statement, e1-c06]
- **OQ-5 · A planning inequality for behavioural data.** Cryptographic migration planning uses the inequality that migration time plus required secrecy lifetime must not exceed adversary maturity time (Mosca, 2018). Does a behavioural analogue hold for agentic systems, such that migration to structurally separated substrates must complete before observation capability matures enough to reconstruct traces recorded today? [Open question; conjecture-status at source, e1-c31]
- **OQ-6 · Record-now-reconstruct-later.** Is the threat model for behavioural data recorded under today's adversary and reconstructed under tomorrow's structurally isomorphic to harvest-now-decrypt-later for cryptographic material, tightly enough that the mitigation discipline transfers? [Open question; conjecture-status at source, e1-c32]
- **OQ-7 · Bilateral attestation.** Does promoting a provider-held assumption set, inspected by an auditor, to a bilateral co-signed credential, attested by both parties and verifiable by anyone, yield a strict assurance gain in the multi-provider case? [Open question; conjecture-status at source, e1-c22]
- **OQ-8 · Convergence with the assurance literature.** Are the AI-assurance literature's integrity gap (the architectural infeasibility of independent verification) and this paper's structural-versus-policy distinction two views of one object, such that the two communities can share results rather than duplicate them? [Open question; conjecture-status at source, e1-c19]

**Proposed first session.** A session of the IKP Working Group is requested at the Block #15 meeting, Washington D.C., 15 to 16 October 2026, to review and correct the problem framing and evidence base of sections 1 and 2, to decide whether the work item is taken up and under which document class, and, if it is taken up, to seed the open-questions register with the study agenda above as the session amends it. Written comment in advance of the session can proceed at the working group's document forum, where this paper would be posted. The adoption decision is the working group's; no process beyond a session request is assumed here. [Venue particulars verified 2026-07-10 at bgin-global.org/events; the session content derives from sections 1 to 4]

### 5 · Relationship to adjacent work

Position, stated first: the proposed work item reads as continuous with the working group's own document series inside the venue, and should coordinate with, not duplicate, three adjacent efforts outside it; each connection below is this paper's synthesis unless marked as a statement of the cited document.

Within the venue's own series: the IKP Working Group's Wallet Governance, Policy and Key Management Study Report (a working draft in the group's study-report series) treats wallets as governance and identity instruments and classifies wallet types by their security, privacy and usability properties, and the group has published Study Report: Zero-Knowledge Proofs (ZKPs) - Technology and Applications. [Venue facts, verified 2026-07-10 at the working group's document forum] The present proposal supplies a document that series does not yet contain: a classification of the separation properties between the agents that operate such wallets and credentials. [Synthesis]

IEEE Std 7012-2025, IEEE Standard for Machine Readable Personal Privacy Terms, approved by the IEEE SA Standards Board in November 2025 and published in January 2026, standardises machine-readable personal privacy terms proffered on the individual's behalf. [External standards facts, verified 2026-07-10 at the IEEE SA standard page] In this paper's reading, a boundary agent of the section 2 pattern is a natural candidate for the first-party terms-proffering role that standard contemplates, and the documentation profile of section 4 would give such an agent's separation claims a reviewable form. [Synthesis; this paper's reading, not a statement of the standard]

The Trust over IP technology architecture places a single spanning-layer protocol at its core: the Trust Spanning Protocol (TSP) Specification, an experimental implementor's draft at the time of writing, defines how endpoints with public-key-based identifiers exchange authentic and, where required, confidential messages across trust domains. [External standards facts, verified 2026-07-10 at the published specification page] The two-agent pattern of section 2 is a candidate deployment profile at that layer: two agents in one person's service, deliberately held in separate trust domains. [Synthesis]

The Decentralized Identity Foundation's Trusted AI Agents Working Group states its scope as an interoperable stack for trustworthy, privacy-preserving and secure AI agents, with current work items on delegated authority (a report, a threat model and a governance report) and a protocol reference implementation for agent delegation and cryptographic agent identity. [External facts, verified 2026-07-10 at the working group's page] Together with related agentic-credential work across that community, these efforts address which agent may present what, and under whose authority. [External landscape fact, stated generically beyond the named working group] The present proposal is complementary: it addresses what an agent can accumulate, and whether the separation between agents is structural or instructed. [Synthesis]

Whether regulatory conformity language under the EU acquis raises the same structural-versus-policy classification question for high-risk AI documentation is a mapping task the work item could take up, not a claim this paper makes; this paper's scope is confined to blockchain and identity contexts. [Scope statement only; no claim carried]

### 6 · Limits

This paper claims less than it might, deliberately. The guarantee of section 2 is conditional twice over: outside its two preconditions it makes no statement, and within them the strict bound holds only while the declared capacity deficit holds; the preconditions are exactly what fails when observers collude or channels are combined, and the deficit is exactly what erodes as stronger adversary classes arrive, which is why every declaration is indexed to an adversary class and a date. No rate of erosion is asserted for any system. The empirical measurements of section 1 are the field's, made on policy-composed systems; no measurement of the section 2 pattern itself exists, and producing one is what OQ-2 and OQ-3 ask. The implementation record of section 3 is design-status: one layer deployed as described, one specified with code not written at its specification version, one built instance at the workflow layer; none has been independently evaluated. The stakes argument of section 3 and every connection drawn in section 5 are this paper's synthesis. All eight open questions are open, and this paper asserts none of them. Findings against the pattern, should the work item produce them, are results of the work item and will be reported with the same prominence as findings for it.

---

### References (external only; final venue formatting at release)

- Asif and Amiri (2026). Sequential-composition leakage bound and measurements. arXiv:2603.05520. [per e1-c09]
- Patil, Stengel-Eskin and Bansal (2025). Composition analysis. arXiv:2509.14284 (preprint). [per e1-c09]
- El Yagoubi, Badu-Marfo and Al Mallah (2026). AgentLeak inter-agent channel measurement. arXiv:2602.11510. [per e1-c10]
- Multi-agent privacy landscape: MAGPIE, arXiv:2506.20737; PrivAct, arXiv:2602.13840. [per e1-c11]
- Microsoft (2026). Agent Governance Toolkit documentation. github.com/microsoft/agent-governance-toolkit. [per e1-c27]
- Wyner, A. D. (1975). 'The wire-tap channel', Bell System Technical Journal.
- Fano, R. M. (1961). Transmission of Information; Cover, T. M. and Thomas, J. A. (2006). Elements of Information Theory.
- Leung-Yan-Cheong, S. K. and Hellman, M. E. (1978). 'The Gaussian wire-tap channel'.
- Csiszar, I. and Korner, J. (1978). 'Broadcast channels with confidential messages'.
- Mosca, M. (2018). 'Cybersecurity in an era with quantum computers: will we be ready?'. [per open question OQ-5]
- Bakhta, A. (2025). On the Half-Life of Cryptographic Trust. StarkWare. [per open questions OQ-6]
- Bakhta, A. (2026). Toward High-Assurance AI Safety by Design for Autonomous Systems. StarkWare. [per open questions OQ-7, OQ-8]
- BGIN, IAM, Key Management and Privacy (IKP) Working Group: working-group registry at bgin-global.org/activities/working-groups; Block #15 meeting particulars at bgin-global.org/events.
- BGIN IKP Working Group, Wallet Governance, Policy and Key Management Study Report (working draft, SR series). bgin.discourse.group/t/wallet-governance-policy-and-key-management-study-report/492.
- BGIN IKP Working Group, Study Report: Zero-Knowledge Proofs (ZKPs) - Technology and Applications. Per the working-group document forum, bgin.discourse.group/c/working-group-s/ikp-wg/8.
- IEEE Std 7012-2025, IEEE Standard for Machine Readable Personal Privacy Terms (approved 2025-11-04; published 2026-01-20). standards.ieee.org/ieee/7012/7192.
- Trust over IP Foundation, Trust Spanning Protocol (TSP) Specification (experimental implementor's draft). trustoverip.github.io/tswg-tsp-specification.
- Decentralized Identity Foundation, Trusted AI Agents Working Group. identity.foundation/working-groups/trusted-agents.html.
