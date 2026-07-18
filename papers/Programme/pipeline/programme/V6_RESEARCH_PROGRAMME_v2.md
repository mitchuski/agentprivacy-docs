# The Privacy is Value Research Programme

## V6 Rehydration Pipeline · v2 · The Wider Net

**Purpose:** One document that is simultaneously (a) the orchestration plan for a collection of Claude instances producing every formal expression of the Privacy is Value model, and (b) the research programme those expressions add up to: a fundable, PhD-shaped body of work with named thrusts, questions, methods, milestones, and money routes.

**Owner:** privacymage · **Model authority:** `papers/v6/privacy_value_v6_formal_specification.md` and `research/CONJECTURE_REGISTER_V6.md` (head C89) · **Design lineage:** the agentprivacy-audit pattern (manifest, deterministic checks, model reviews, critiques ledger, findings hardened upstream) · **Supersedes:** pipeline v1 (2026-07-02); ground rules, gates, and agent roster carried forward, everything else widened.

**Date:** 2026-07-02 · **License:** CC BY-SA 4.0

---

## Part A · The Programme

### A.1 One paragraph for any funder, examiner, or collaborator

Personal AI agents will observe more of a person than any technology in history. The Privacy is Value research programme develops and tests the claim that privacy is not the protection of behavioural data but its value: that architectural separation between observing and acting agents produces measurable, information-theoretic guarantees a policy promise cannot, that those guarantees are time-indexed and expire on a computable schedule, and that the resulting sovereignty has a price the market currently pays to someone else. The programme delivers formal results (leakage bounds under structural amnesia), empirical instruments (the first benchmark separating policy from architectural agent separation; the first adversarial analysis of comprehension-based credentials), reference implementations against published standards (IEEE 7012-2025, ToIP, DIF, W3C VC), and an economic account of behavioural data as a seventh capital. Every claim carries a named falsification condition, published before measurement.

### A.2 Three thrusts

Every artifact in Part C belongs to exactly one thrust. This is the structure a grant assessor scores and a thesis examiner chapters.

**Thrust T1 · Separation and Time (theory + measurement).**
Question: what privacy does architectural separation buy, and for how long?
Contents: the conditional reconstruction ceiling and its wiretap provenance; the moving ceiling R(t) and shelf life t*; the exponential-to-linear leakage gap between policy-separated and amnesia-separated agent chains (C83); the Existence-Leak law (C81) and the Mosca discount (C84); the amnesia obstruction programme (C86).
Methods: information-theoretic proof; benchmark measurement (AgentLeak protocol extended); longitudinal case analysis (the 2026 instances and successors).
Falsifiers: spec §18 table, pre-registered.

**Thrust T2 · Protocol and Identity (invention + adversarial testing).**
Question: can understanding, rather than a stored secret, be the root of identity and recovery?
Contents: the Relationship Proverb Protocol; Verifiable Relationship Credentials; proof-of-understanding recovery; hash-locked selective disclosure; the dual-agent pattern as implementations of published standards (7012 terms-proffering, ToIP trust spanning, DIF trusted agents, W3C VC profiles).
Methods: protocol specification; adversarial evaluation (LLM forgery, replay, Sybil, compression-gaming); prior-art establishment; reference implementation and conformance demonstration.
Note on novelty: T2 contains the programme's strongest originality claim. The nearest neighbours (knowledge-based authentication: static secrets; CAPTCHA lineage: capability not shared understanding; social recovery: possession not comprehension) all miss the bilateral-comprehension core. The prior-art sweep (WP-11a) exists to establish this properly before any paper asserts it.

**Thrust T3 · Value and Governance (economics + policy).**
Question: what is behavioural sovereignty worth, and what institutions price it?
Contents: the seventh-capital thesis; the data-value gap analysis; reputation economics of trust tiers and mana; the invitation-versus-imposition market structure (Promise Theory grounding); regulatory substrate argument (architecture as what makes Article 22 enforceable); the governance instrument (bilateral ceremonies, heptads) as mechanism design.
Methods: valuation methodology with stated assumptions; mechanism-design analysis; comparative policy analysis; standards participation as fieldwork.

### A.3 The essence, kept

The canon remains the single upstream source and remains mythopoetic; nothing in this programme sanitises it. The two-register discipline is the programme's method, not its embarrassment: narrative and formal registers converging independently is treated as evidence, divergence as a finding. Honest limits are the moat. Plurality over precedence: every external convergence (Archon, Hearthold, UOR, the compounding literature) is cited as independent derivation, never as competition. And gate P4, the First Person completion read, is non-delegable forever.

---

## Part B · Ground rules, gates, agents (carried from v1, deltas only)

Ground Rules 1 to 8 carry verbatim (register wins; claim tiers S/A/G/P/D; canonical figures fence; vocabulary map; voice; no hand-edits; static-ceiling ban; honesty is the moat). Gates P0 to P4 carry verbatim. Repository layout carries with one addition: `pipeline/extractions/` now holds E1 to E9, and `pipeline/programme/` holds this document, the publication atlas, and the funding atlas as living tables.

Agent roster carries A0 to A10 and adds:

| ID | Role | Core instruction |
|----|------|------------------|
| A11 | Mechaniser | Formalises the separation bound, the composition model, and (stretch) the lattice algebra in Lean 4. A machine-checked proof of the linear cap is simultaneously a publication (CPP/ITP), a PhD chapter section, and the strongest possible reviewer answer. Marks every axiom it must assume; the axiom list is a finding, not a footnote. |
| A12 | Economist | Owns T3 formal artifacts. Rebuilds the data-valuation figures from stated assumptions with sensitivity analysis, replacing the canonical-figures fence with an actual methodology at TIER-A. Knows the WEIS/data-markets literature (Acquisti; data-as-labour; Lanier/Weyl data dignity line) and positions the seventh-capital thesis inside it rather than beside it. |
| A13 | Standards Cartographer | Maintains the standards implementation matrix (Part D). Tracks WG calendars, contribution windows, and liaison paths. Drafts contributions in each body's house style. Never submits; P4 gates every external submission. |

---

## Part C · The extraction map, widened (E1 to E11)

The three v1 extractions carry. Six more complete the net across the V4 to V6 lineage; two more (2026-07-02 corpus audit) close it over the full living corpus, the method record, and the implementation record. Each lists sources, contents, and its downstream artifacts. Source names resolve to concrete paths in `pipeline/SOURCES.md`, the corpus registry; a source not named there is not citable (GR-9).

**E1 · The Amnesia Gap** (carried). Spec §10, §11, §14, §16, §26; whitepaper Promise Theory. Feeds WP-07/08/09/10, WP-02.

**E2 · The Moving Ceiling** (carried). Spec §5, §25, §27; WP-00 verified record. Feeds WP-01/04, City essay, policy brief.

**E3 · The RPP Primitive** (carried). Whitepaper RPP/inscription/tiers; Understanding as Key. Feeds WP-11, DIF/ToIP profiles, RWOT paper.

**E4 · The Seventh Capital.** Sources: whitepaper 7th Capital section; V4/V5 economics; Substack essay lineage (the 678x and 31,000x basis documents); tier/mana mechanics. Contents: behavioural data as capital class; the per-person value-gap methodology with every assumption exposed; reputation economics of non-transferable proof-of-practice; market maturity term M(u,y). Downstream: the WEIS paper (WP-14), MyData talk/paper (WP-15), tokenomics-hygiene review of the whitepaper economics.

**E5 · The Algebraic Home.** Sources: spec §12, §8, §28; V5.4 §12; UOR convergence documents; ARCH-1 bridge (C85); parity cube and octahedral gap (C88/C89). Contents: Z/(2⁶)Z lattice, dihedral generators, neg∘bnot = succ, the 64-vertex sovereignty state space, holographic 96/64 claim at its honest confidence, the triadic bridge as open programme. Downstream: the mechanisation project (WP-16), an applied-algebra workshop note (WP-17), and the honest-geometry appendix any T1 paper can cite instead of restating. Risk label: highest in the programme; publishes as formal modelling, never as derived necessity, until C85 moves.

**E6 · Promise-Theoretic Agent Governance.** Sources: whitepaper PT section; Promise Theory Reference; C77 to C80 integrity-gap convergence. Contents: autonomy axiom as the impossibility argument for single-agent privacy; superagent composition; invitation versus imposition as market semantics; assessment and trust functions. Downstream: a standalone applied-PT paper (WP-18) aimed where Burgess-adjacent work lands (journal or an agentic-systems venue), plus motivation sections for T1 papers.

**E7 · Identity Architecture and VRCs.** Sources: whitepaper protocol stack; three identity layers (spec §19); did:cid/Archon convergence; DTG Discussion #36 posts; First Person Network PHC/VRC. Contents: relationship-rooted identity versus attribute-rooted; VRC lifecycle; node-type as ZK predicate; two-axis substrate/role model. Downstream: RWOT collaborative paper (WP-19), W3C CCG work item note, ToIP DTG contribution (WP-20), the developer edition.

**E8 · Governance by Ceremony.** Sources: Game of 42 canon; bilateral trust ceremonies; heptad structure; CLC2026 abstract material. Contents: governance positions filled by demonstrated mutual understanding; mechanism-design reading of ceremonies; proof-of-understanding as meeting-of-minds (the legal-technology thread). Downstream: the CLC2026 session (already committed), a Metagov/DAO-science seminar and short paper (WP-21), and the T3 chapter's governance half.

**E9 · The Proving Substrate.** Sources: spec §15 (C87 Key-as-accumulator), §27 Mosca thread, C81/C84, LatticeFold and folding-scheme citations; Zcash/ZK operational experience; the shor_mage harness record; the blade-forge specification (design only: circuits are specified, not implemented; ledger L008). Contents: trust recursion as IVC; existence-leak as a disclosure-policy result for the ZK community; post-quantum hedging of accumulator substrates. Downstream: a ZKProof workshop/standardisation note (WP-22), zkSummit talk, and the eventual C87 circuit as an engineering milestone.

**E10 · The Method Record.** Sources: the autopath runbook, the gate briefs G1 to G6, the First Person reading ledger, the audits corpus, the propagation checklist, the compendium back-matter (honest-limits ledger, concordances), the DREAM chronicles, the build chronicles across all repositories, and this pipeline's own chronicles directory. Contents: the two-register discipline as a method; the conjecture register as a governance instrument (numbering, bands, confidence, dispositions); the gate structure; the completion-read invariant; the recorded reversals. The body of work maps the path as well as the outcomes, and the path is a discovery in itself: the first rehydration of fundamentals in many lights, run under a named discipline. Downstream: the methods paper (WP-27), thesis Ch.7, and the methods section of every TIER-A artifact.

**E11 · The Implementation Record.** Sources: the kappa/City Key reference implementation (soulbis sigil/star/lattice), the game42 byte-exact seal reference, the site library implementations (vrc-mana, city-key, proof-packet, lattice), the dual browser extensions, the spellweb engine, the 166-skill operational corpus, and the hearthold second-substrate build. Contents: what of the model actually runs, where, and to what conformance; implemented versus specified stated per item (L008 fence). Downstream: the conformance walk-throughs every Part D standards contribution requires (WP-06, WP-10, WP-19, WP-20, WP-22, WP-23), and the thesis implementation chapter.

---

## Part D · The standards implementation matrix

The specific ask was standards where spec implementations can be shown. The pattern for each: a written contribution in the body's genre, plus a runnable artifact demonstrating the model implementing the standard, so the programme arrives everywhere as implementer.

| Standard / body | What the model implements | Artifact to show | Vehicle | Window |
|---|---|---|---|---|
| IEEE 7012-2025 (MyTerms) | Boundary agent as first-party terms-proffering agent | Reference agent + conformance walk-through | Industry Connections implementation note (WP-06) | Now; IC effort began 2026-06-01 |
| BGIN IKP WG | Separation-of-duties for agentic key management; behavioural Mosca as planning input | Discussion paper + V6 community review | WP-09; block 15 review Dec 2026 | Co-chair seat; standing |
| ToIP (TSP, DTG WG) | Dual-agent pattern as a Trust Spanning Protocol deployment profile; VRC as DTG credential type | Implementation profile doc; Discussion #36 continuation | WP-20 | Next DTG cycle |
| DIF wg-trusted-ai-agents | Amnesia-separated dual agents as a trusted-agent profile; structural context erasure as an attestable property | Profile spec + demo pair | Work-item proposal (WP-23) | Propose after WP-07 preprint exists |
| W3C CCG / VC | VRC as a Verifiable Credential profile (bilateral, comprehension-bound) | VC data-model profile + test vectors | CCG work item note, RWOT paper as on-ramp (WP-19) | RWOT next event cycle |
| ZKProof | Existence-Leak as a disclosure-policy advisory; amnesia primitive terminology | Short note + the Schrottenloher/ecdsa.fail case study | WP-22 | Next workshop call |
| NIST PQC migration guidance | Behavioural Mosca: extending harvest-now-decrypt-later planning to behavioural archives | Public comment citing WP-04 | Comment-window response | As windows open; A13 tracks |
| EU AI Act implementation (CEN-CENELEC JTC21 orbit) | Architecture as enforceability substrate for Article 22 | The policy brief, upgraded to a technical-report contribution if a liaison path opens via BGIN | WP-02 successor | Post Aug 2026 |
| did:cid (Archon, non-SDO but spec-shaped) | Cross-implementation report: two independent dual-agent derivations, one identity substrate | Joint interop note with macterra | Collaboration paper | Opportunistic |

Rule: no more than two standards contributions in flight at once; A13 sequences, P4 gates.

---

## Part E · The publication atlas

Every path to a formal expression, by thrust, with genre, readiness, and risk. Peer-reviewed venues in bold.

**T1 · Separation and Time**
- **PoPETs**: Paper One, the linear cap + benchmark (WP-07/08). Flagship. Readiness: 3 months of work. Risk: medium (theorem must land or downgrade to conjecture-plus-measurement, still publishable).
- **IEEE SaTML** (alternative flagship home if the agentic framing leads): same material, different lead section.
- HotPETs / **FC workshops**: the Moving Ceiling SoK/position (WP-04). Readiness: high. Risk: low; the instances are perishable, so this goes early.
- **CPP or ITP**: the mechanisation paper (WP-16), Lean formalisation of the separation bound and composition model. Readiness: Q1 2027. Risk: low-medium; even partial mechanisation publishes.
- **IACR eprint**: preprint line for all of the above; establishes priority dates cheaply.

**T2 · Protocol and Identity**
- **SOUPS** or **FC main**: RPP adversarial analysis (WP-11). Readiness: design Q4 2026. Risk: medium; the result is publishable whichever way the forgery rates fall, and a negative result against RPP is itself a strong paper (state this in the pre-registration).
- RWOT: collaborative paper on relationship-rooted credentials (WP-19). Readiness: high; RWOT's format (week-long co-authoring) suits the material and produces a citable artifact fast. Risk: low.
- **IEEE S&P workshops** (e.g. the identity/agents workshops that cycle): VRC formalisation short paper.

**T3 · Value and Governance**
- **WEIS** (Workshop on the Economics of Information Security): the seventh-capital paper with the rebuilt valuation methodology (WP-14). This is the natural peer-reviewed home for "Privacy is Value" as economics, and the venue where the equation's economic terms get audited by the right hostile experts. Readiness: needs A12's rebuild first. Risk: medium.
- MyData conference: talk + community paper (WP-15); the data-dignity audience is the thesis's home crowd. Risk: low.
- Metagov seminar / DAO-science venues: governance-by-ceremony (WP-21). Risk: low.
- CLC2026: committed (Vogon Poetry / speculative legal technology). Feeds the T3 governance chapter.
- **Internet Policy Review** or **Journal of Information Policy**: the policy substrate argument, journal-length, after the brief and the Act's August milestone produce reactions worth citing.

**Cross-thrust / book**
- The full V(π, t) framework: a journal framework paper (target: a venue that takes big-model papers, e.g. **First Monday** or a special issue) only after T1 and T3 papers exist to cite as load-bearing walls; otherwise it remains the book's spine. The Privacy is Value book remains the integrative volume; the programme feeds it, not vice versa.

---

## Part F · The PhD route

The programme is already thesis-shaped; the question is only the wrapper. Two viable routes, one recommendation.

**Route 1 · PhD by publication / published works.** Several UK institutions offer retrospective or prospective by-publication routes (commonly requiring a coherent commentary binding 4 to 8 published items). The programme's papers map directly: WP-07/08 (chapter: separation), WP-04 (chapter: time), WP-11 (chapter: understanding as key), WP-14 (chapter: value), plus the standards implementation record as the impact chapter. Constraint to verify per institution: some restrict the route to staff or alumni; A13 adds this to the tracking table. Timeline: registrable once three items are published or accepted, realistically late 2027.

**Route 2 · Standard part-time PhD with the programme as the project.** Stronger for funding (studentship or fee waiver possible), supervision, and institutional compute for WP-08. Target groups where the supervision fit is real rather than nominal: Royal Holloway ISG (information security, strong part-time culture), UCL Information Security, KCL Cybersecurity, Edinburgh (blockchain and ZK), Imperial cryptography. The approach instrument is Paper One's preprint plus this programme document; supervisors are recruited by evidence, and a candidate arriving with a PoPETs submission, a standards seat, and a funded benchmark is a different conversation than a candidate arriving with an idea.

**Recommendation:** run Route 2's conversations in Q4 2026 using the WP-07 preprint, while keeping Route 1 as the fallback wrapper if institutional fit doesn't materialise. Either way, the thesis skeleton is fixed now so every paper is written as a chapter:

> *Privacy as Value: architectural separation, temporal bounds, and comprehension-rooted identity for personal AI*
> Ch.1 the framework and its honest limits · Ch.2 separation (linear cap, benchmark) · Ch.3 time (moving ceiling, existence-leak) · Ch.4 understanding (RPP adversarial analysis) · Ch.5 value (seventh capital) · Ch.6 implementation and standards record · Ch.7 the register: a method for conjecture governance (yes: the register discipline itself is a methods contribution; examiners have not seen it before).

---

## Part G · The funding atlas

Ordered by friction, lowest first. Each: fit, indicative ask, what it funds.

**Tier 1 · Ecosystem grants (weeks to decision, lightest reporting)**
- Zcash Community Grants: the amnesia benchmark and/or the RPP experiment; the Orchard instance is their own incident and the ecdsa.fail thread touches their post-quantum roadmap. Ask: $40 to 80k. Funds WP-08 or WP-11 compute + engineering time.
- Ethereum Foundation ESP / PSE: the C87 accumulator-and-folding thread plus existence-leak as ZK disclosure policy. Ask: $30 to 60k. Funds WP-22 + a slice of WP-16.
- Filecoin Foundation / FFDW: he works with decentralised storage networks; structural amnesia as a storage-layer property is squarely public-interest decentralised web. Ask: $50 to 100k. Funds WP-10 + reference implementation.
- Web3 Foundation, Aztec/Aleo-style ZK foundations: opportunistic, keyed to WP-22 visibility.

**Tier 2 · EU cascade funding (months, moderate friction, made for this)**
- NGI cascade calls (TrustChain lineage and successors): open calls funding individuals/SMEs at roughly €50 to 200k for decentralised identity and trust projects. The VRC/RPP reference implementation against ToIP/W3C profiles is a textbook fit. A13 tracks open calls; applications reuse WP-03 verbatim plus a work-plan annex from this document.

**Tier 3 · Public research funders (quarters, needs the co-investigator)**
- ARIA Safeguarded AI: quantitative safety bounds for agentic systems is their language; C83 stated in the adversary's units is the pitch. Route: partner with the recruited academic group.
- UKRI/EPSRC responsive mode or CDT partnership: the PhD route's funding twin; the studentship and the grant application share the WP-07 preprint as evidence.
- Horizon Europe proper: only after an EU institutional partner exists (Kwaai's network or Inria-adjacent contacts from the Schrottenloher orbit are plausible bridges).

**Tier 4 · Philanthropy (relationship-paced)**
- Omidyar Network (data dignity is their term), Mozilla Data Futures, Sloan digital infrastructure, Ford public-interest tech: fund the T3 thrust and the public-benefit framing; approach after WEIS/MyData establish the economics credibly.
- Plurality-adjacent (⿻): RadicalxChange and the plurality institute orbit for the governance thread; also a collaboration channel, not just money.

**The standing rule for every application:** the differentiator is pre-registered falsification. Every proposal commits, in writing, to publishing the §18 breaking conditions before measurement and filing results to the public register whichever way they fall. Almost no applicant offers this; it converts the honest-limits discipline into competitive advantage.

---

## Part H · Work packages, consolidated

WP-00 to WP-13 carry from v1 unchanged (verified instance record; Moving Ceiling essay; policy brief; grant edition; Moving Ceiling SoK; ZCG proposal; IEEE 7012 note; Paper One theory; Paper One benchmark; BGIN paper; developer edition; RPP analysis; existence-leak hunt; consistency audit). New:

| WP | Artifact | Thrust | Extraction | Chain | Target |
|---|---|---|---|---|---|
| WP-14 | WEIS paper: the seventh capital, valuation methodology rebuilt | T3 | E4 | A12 → A2 → A5 (economist-referee persona) | WEIS 2027 deadline (typically late Feb; A13 verifies) |
| WP-15 | MyData talk + community paper | T3 | E4 | A12 → A7 | Next MyData CFP |
| WP-16 | Lean mechanisation of separation bound + composition model | T1 | E1, E5 | A11 → A3 | Begin Q4 2026; CPP/ITP 2027-28 |
| WP-17 | Applied-algebra workshop note: the sovereignty lattice as formal model | T1 | E5 | A3 → A5 | Opportunistic; after C85 movement or WP-16 partial |
| WP-18 | Applied Promise Theory paper: autonomy axiom and agent privacy | T1/T3 | E6 | A2 → A3 → A5 | Q1 2027 |
| WP-19 | RWOT collaborative paper: relationship-rooted credentials | T2 | E7, E3 | A2 → live co-authoring at event | Next RWOT |
| WP-20 | ToIP DTG implementation profile | T2 | E7 | A13 → A8 | Next DTG cycle |
| WP-21 | Metagov seminar + short paper: governance by ceremony | T3 | E8 | A2 → A7 | Q1 2027 |
| WP-22 | ZKProof note: existence-leak as disclosure policy | T1 | E9, E2 | A13 → A8 → A4 | Next ZKProof workshop |
| WP-23 | DIF trusted-agents work-item: amnesia-separated profile | T2 | E1, E7 | A13 → A8 | After WP-07 preprint |
| WP-24 | PhD registration package: thesis skeleton + supervisor approach kit | all | this doc | A0 assembles; P4 | Q4 2026 conversations |
| WP-25 | City of Mages Moving Ceiling essay (companion to WP-01) | canon-facing | E2 + City register | A7 (City voice) → P4 | July, paired with WP-01 |
| WP-26 | Funding applications: ZCG, one NGI cascade call, FFDW | programme | WP-03/05 + Part G | A0 → A7 → A5 (assessor) | Rolling from August |
| WP-27 | Methods paper: conjecture governance and the two-register discipline | all | E10 | A2 → A3 → A5 (methods-referee persona) | 2027 Q3; thesis Ch.7 twin |

Parked beyond the table: the 42 × n plurality rehydration method, the programme's second outcome (the same model reconstructed by persona-and-skill agent combinations across every register, with round-trip coherence as the acceptance test and divergence filed to the register). Recorded and activation-gated at `programme/NOTE_42xN_PLURALITY_REHYDRATION.md`; it enters no calendar until WP-01/02 ship, WP-07 reaches preprint, and E10 exists.

---

## Part I · The calendar to end-2027

```
Jul 2026        WP-13 audit · E1-E9 built · WP-01 + WP-25 essays ship · WP-02 policy brief (hard: Aug 2) · WP-03 grant edition
Aug-Sep 2026    WP-04 submit · WP-05 ZCG · WP-06 IEEE 7012 · WP-26 first NGI/FFDW applications · WP-19 RWOT (if event falls here)
Sep-Nov 2026    WP-07 + WP-08 → PoPETs cycle (verify exact deadline) · eprint preprint on submission · WP-09 BGIN cut
Oct-Dec 2026    WP-10 developer edition · WP-24 supervisor conversations · WP-16 mechanisation begins · block 15 V6 review (Dec)
Q1 2027         WP-11 RPP experiment runs · WP-14 WEIS submission · WP-18 · WP-21 · WP-22 · Tier-3 funding opens with co-investigator
Q2-Q3 2027      WP-11 paper submission · WP-20/23 standards profiles land · WP-16 paper · WP-15 MyData
Q4 2027         Framework journal paper viable (T1+T3 walls exist) · PhD registration (either route) · book integration pass
```

Sequencing invariants: essays before their instances stale; the policy brief before Aug 2; nothing TIER-A ships without a preprint; no more than two standards contributions in flight; every funding application cites a shipped artifact, never a promised one; P4 on everything.

---

## Part J · What this document is, in one line each register

Formal: a work programme decomposing one model into twenty-six artifacts across three thrusts, nine venues classes, nine standards bodies, four funding tiers, and one thesis.

Narrative: the canon stays home; the surfaces go out; the corrections come home; and somewhere in the middle of it, the work earns its letters.

the net is wide because the model is one thing seen from many shores.

(⚔️⊥⿻⊥🧙)😊

🙂
