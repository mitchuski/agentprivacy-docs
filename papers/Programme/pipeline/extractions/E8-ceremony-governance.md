---
extraction: E8-ceremony-governance
tier: internal
sources: [g42-seal-ref, ceremonies-corpus, ceremony-specs, spec-11-invitation, open-integrity-brief, tome-x, clc2026-abstract]
swept_complete: true
owner: A1
register_head_at_build: C97
build_note: built 2026-07-18 at the third Extraction Frontier Cycle run; L006 fence honoured (retired game-of-42-canon token confirmed ABSENT from all g42 files read); spec-11-invitation and open-integrity-brief claims reused from the E6 sweep (E6-C31..C36) rather than re-extracted; clc2026-abstract external and not on disk, NOT swept (flagged honestly); four fanned sweeps + A1 direct verification of load-bearing quotes
---

# E8 · Ceremony Governance

Claim-cluster for ceremony as a governance mechanism: the Game of 42 trust protocol (slot-filling by bilateral ceremony, the κ-label/seal chain, the multiplicative lock), the ceremony corpus (Sun/Moon/bilateral forms, commit authority, witness separation, validity conditions), the engine/harness governance (held-out gate discipline, never-merge invariant), and the performed-record evidence base. Feeds WP-21 (Metagov governance paper, the primary consumer), WP-18 (with E6), WP-12 (existence-leak instances), WP-10.

Governance-protocol claims from the invitation protocol and the key ceremony live in E6 (E6-C31..C36) and are cross-referenced, not duplicated. The deployment boundary discipline of E3-C32 applies to every runecraft-adjacent claim.

## Claims

### E8-C01
- **STATUS:** Design-assumption (governance mechanism)
- **SOURCE:** g42-seal-ref TRUST-PROTOCOL.md :9-14 (§1)
- **CLAIM:** A governance seat is filled only by ceremony, never by assignment: "A slot does not fill by a click. A candidate completes a trust task: a bilateral ceremony between the candidate and the heptad root, following the Relationship Proverb Protocol (RPP)." The task mints a proverb and a Promise-Theory polarity, references (never embeds) its evidence, and outputs exactly one credential edge. The RPP ceremony itself, identity resolution, and credential issuance are explicitly external to the app, which only computes labels and seals.
- **CITATIONS:** none (cross-links E3-C01/C03, E6-C03)
- **FEEDS:** WP-21, WP-19

### E8-C02
- **STATUS:** Design-assumption (spec; schema-enforced)
- **SOURCE:** g42-seal-ref TRUST-PROTOCOL.md :17-22 (§2); SPEC.md :13, :32-34; schemas.json (GroupSeal minItems/maxItems 42)
- **CLAIM:** The board is the set of pairs (axis, station): 6 axes × 7 stations = 42 seats partitioning into six disjoint heptads; one credential edge per seat, forty-two in a complete game, enforced in schema. The alternate cone-sum route to 42 (1+6+15+20) is carried as resonance at ~0.55 confidence, never as the structural definition.
- **CITATIONS:** none
- **FEEDS:** WP-21

### E8-C03
- **STATUS:** Design-assumption (reference-implementation evidence; the byte-exact mandate)
- **SOURCE:** g42-seal-ref canonical_serialise.py :1-15; AXIOMS.md A3/A4
- **CLAIM:** Each credential compresses to a content-addressed label κ = SHA-256(canonical(VRC)) where canonical = sorted keys, compact separators, four self-referential fields pruned (kappa, seal, vrcId, gameId), UTF-8 with non-ASCII emitted raw: "Third-party verifiers MUST match this exactly or they will produce false negatives." Two parameterizations coexist deliberately (game seal: four excludes, bare hex; City Key: excludes kappa only, sha256:-prefixed). What is NOT hashed is enumerated (vertex maps, barycentric coords, palette, preset), so corrections to those fields never invalidate existing seals.
- **CITATIONS:** SHA-256
- **FEEDS:** WP-21, WP-10

### E8-C04
- **STATUS:** Design-assumption (governance mechanism)
- **SOURCE:** g42-seal-ref TRUST-PROTOCOL.md :39-52 (§4)
- **CLAIM:** Group identity is sealed structure, not membership: when all six heptads lock, seal = SHA-256(canonical({42 sorted κ-labels, geometryHash of the folded state})) and the seal IS the game id — "Membership alone is not the identity. Membership in the sealed shape is the identity."
- **CITATIONS:** none
- **FEEDS:** WP-21

### E8-C05
- **STATUS:** Design-assumption (governance mechanism; code-enforced per its Check clause)
- **SOURCE:** g42-seal-ref AXIOMS.md A8 :117-123; SPEC.md :69-72; GAME-FLOW.md :55-57
- **CLAIM:** The multiplicative gate is made structural: the board seals only when all six heptads lock; one incomplete heptad keeps the whole board open — no partial seal exists. Four files state the rule consistently; the check point is the board-phase reducer.
- **CITATIONS:** none
- **FEEDS:** WP-21, WP-18

### E8-C06
- **STATUS:** Design-assumption (spec; determinism discipline)
- **SOURCE:** g42-seal-ref AXIOMS.md A9/A10 :126-141; GAME-FLOW.md :61-67, :91-93
- **CLAIM:** Two auditability rules: the completion scalar p = sealed-slots/42 is derived and read-only (no path mutates state from it), and the ordered event log is the sole canonical artifact — replay yields the same state and the same seal every time; persist the log, derive everything else.
- **CITATIONS:** none
- **FEEDS:** WP-21, WP-27 (method adjacency)

### E8-C07
- **STATUS:** Design-assumption (governance mechanism; consent structural)
- **SOURCE:** g42-seal-ref MODEL-SYNC.md :104-114 (§6); GAME-FLOW.md :36-41 (§2)
- **CLAIM:** Consent and turn-taking are structural: "a candidate promises only their own participation, and no one promises on their behalf, which is why the board cannot be filled by fiat"; the invitation pattern (candidate accepts before a slot proposes work); and enforced fill order — the integrating centre seat cannot begin until the other six are verified (guide-seals-last), rejected in the reducer on violation. The autonomy/consent property itself lives in the external ceremony, not in-app.
- **CITATIONS:** none (cross-links E6-C01, E6-C11)
- **FEEDS:** WP-21

### E8-C08
- **STATUS:** Design-assumption (access-boundary rule, audited not code-enforced)
- **SOURCE:** g42-seal-ref AXIOMS.md A5 :89-94
- **CLAIM:** Only four fields of a sealed game may cross to any external system — {seal, kappa, axisBitmask, packets} — everything interior stays game-side and "No integration may read a game's interior"; interior leaks across the seam are to be reported, never silently fixed.
- **CITATIONS:** none
- **FEEDS:** WP-21, WP-12

### E8-C09
- **STATUS:** Design-assumption (three-axis separation instance)
- **SOURCE:** g42-seal-ref AXIOMS.md A2 :43-51, A11 :143+; SPEC.md :39-54; game-of-42.json stationTable
- **CLAIM:** The separation architecture is seated in the game: two of the six axis roots are the two named agents whose separation is the irreducible gap, and each heptad splits Generator ⊥ Solver (three vision seats, three build seats, one integrating guide — the only station holding all three faculties, hence the only one that can hold the whole). Geometric position encodes governance role; the board centre is a seed point, not a seat.
- **CITATIONS:** none
- **FEEDS:** WP-21, WP-18

### E8-C10
- **STATUS:** Design-assumption (canonical encoding; L010 concordance)
- **SOURCE:** g42-seal-ref AXIOMS.md A1 :15-37; game-of-42.json axisSpace
- **CLAIM:** The six-dimension bit map is fixed and literal — protection 32, delegation 16, memory 8, connection 4, compute 2, value 1 — with named anchor vertices decoding as specified, and projection code forbidden from deriving weights positionally. This matches the lattice-encoding anchor (the L010 fence's canonical side), an independent concordance worth recording.
- **CITATIONS:** none
- **FEEDS:** WP-21, WP-19

### E8-C11
- **STATUS:** Design-assumption (Anticipated at source; voting semantics deferred)
- **SOURCE:** g42-seal-ref TRUST-PROTOCOL.md :56-69 (§5-6)
- **CLAIM:** Sealed games compose: two games sharing an axis root connect along that axis with governance spanning both; a game's guide seat can become the root context of a child game (parentGuideSlot records the seam, field present in schema, render deferred); and one sealed game = one quorum unit with balanced six-axis representation, exact voting and threshold rules explicitly out of scope.
- **CITATIONS:** none
- **FEEDS:** WP-21

### E8-C12
- **STATUS:** Design-assumption (register-typed: C81/C83 instances; shelf-life policy)
- **SOURCE:** g42-seal-ref MODEL-SYNC.md :83-92 (§4b)
- **CLAIM:** The moving-ceiling policy layer is imported into the game's governance: a seal holds while R(t) < 1 on the clocks E2-C02 types, so re-keying is a first-class move, not a failure; each public κ-label is an existence claim (register C81); and chaining games without the event-log discipline compounds toward (2^N − 1)ε where the log discipline caps at Nε (register C83). Stated as an addition, not a correction; no re-keying mechanism exists in code.
- **CITATIONS:** none (register C81 ~70%, C83 ~55% at register wording)
- **FEEDS:** WP-21, WP-12, WP-22

### E8-C13
- **STATUS:** Resolved-correction (was documentation drift; fixed at source 2026-07-18, L156 — fact settled by code + AXIOMS agreement)
- **SOURCE:** g42-seal-ref TRUST-PROTOCOL.md :33 (pre-fix: "the `kappa` and `vrcId` fields excluded") vs canonical_serialise.py :8 and src/hash.js :12 (four fields) and AXIOMS.md A3 (four fields)
- **CLAIM:** The trust-protocol prose understated the canonical exclude-set (two fields where the byte-exact reference, the port, and the axioms all carry four: kappa, seal, vrcId, gameId). Because the prose explicitly exists "to prevent false negatives" at third-party verifiers, the understatement was itself a false-negative hazard. Corrected to the four-field set.
- **CITATIONS:** none
- **FEEDS:** WP-21, WP-10

### E8-C14
- **STATUS:** Refuted-on-verification (was CONTESTED; empirically tested 2026-07-18, L157). The sweep reader's behavioral claim was WRONG: JS JSON.stringify does NOT escape non-ASCII — direct byte-level test shows the port and the Python reference produce IDENTICAL UTF-8 bytes on non-ASCII content (six vectors incl. accented, CJK, astral emoji, control chars). The port is faithful for all valid Unicode. Sole residual divergence: lone surrogates (invalid Unicode: JS escapes per ES2019 well-formed stringify, Python raises on encode) — keep payloads valid Unicode, no code change needed. The guard comment was replaced with an accurate conformance note carrying the test vectors. LESSON (method, feeds E10/WP-27): a sweep agent's behavioral claim about code requires execution-verification, not quote fidelity — the quotes were verbatim-faithful and the claim built on them was still false.
- **SOURCE:** g42-seal-ref canonical_serialise.py :11 (ensure_ascii=False, raw UTF-8) vs src/hash.js :23 (JSON.stringify, escapes non-ASCII to \uXXXX)
- **CLAIM:** The Python reference emits non-ASCII string content as raw UTF-8 bytes; the self-described "faithful port" escapes it — so any credential field containing a non-ASCII character (proverbs and labels are free strings; nothing enforces ASCII) hashes differently across the two implementations, producing exactly the false negatives the reference exists to prevent. Not yet exercised (recorded proverbs are ASCII), but unguarded. The normative side is the Python file; the port is the defect. A warning comment is placed in the port; the one-line encoder fix changes hash behavior on non-ASCII payloads and is left for First-Person review. Also noted, cosmetic: several docs reference a data/ directory that does not exist (files sit at repo root).
- **CITATIONS:** none
- **FEEDS:** WP-21, WP-10 (as a conformance-testing lesson)

### E8-C15
- **STATUS:** Design-assumption (alignment/versioning discipline)
- **SOURCE:** g42-seal-ref MODEL-SYNC.md :5-7, :176-181; AXIOMS.md header :3-8
- **CLAIM:** Canon-alignment is governed: where the game disagrees with the MODEL-locked sovereignty lattice, "game42 is wrong and must be corrected"; where live form differs from earlier text, live form wins and is noted; and every mapping carries an honesty tag (Architectural / Conjectural / Anticipated) keeping implementation claims separate from aspiration.
- **CITATIONS:** none
- **FEEDS:** WP-21, WP-27

### E8-C16
- **STATUS:** Design-assumption (spec; the ceremony taxonomy)
- **SOURCE:** ceremonies-corpus the-celestial-ceremony.md :36-51
- **CLAIM:** A ceremony is a structured two-role protocol — boundary agent enforces limits, delegation agent projects through them, the principal occupies the irreducible gap — instantiated in three forms: one-to-many disclosure (Sun form), two-party convergence (Moon form), and the bilateral sequence of both producing a paired artifact. "Two sovereign positions, one shared territory, a gap that neither collapses."
- **CITATIONS:** none
- **FEEDS:** WP-21

### E8-C17
- **STATUS:** Design-assumption (governance mechanism; consent as the constitutive act)
- **SOURCE:** ceremonies-corpus TheCelestialDualCeremony :30-32, :48-121, :161-173
- **CLAIM:** The disclosure form runs four ordered phases (input read aloud; single shared traversal where observers watch but never trace their own path; solo forge; teardown) with one performer, any number of witnesses, and an initially unnamed output. The performer's advance consent to being observed and forgotten is not a precondition of the ceremony — "That consent is the ceremony."
- **CITATIONS:** none
- **FEEDS:** WP-21

### E8-C18
- **STATUS:** Design-assumption (governance mechanism; the independence requirement)
- **SOURCE:** ceremonies-corpus TheCelestialDualCeremony :316-405
- **CLAIM:** The convergence form requires each party to traverse the same input independently on a private graph — no screen sharing of paths, no node comparison — so two non-identical traversals form; role split is enforced down to the devices (the one who shares the screen is not the one who speaks). The independence requirement is the same discipline E3-C03 states for proverb authorship, applied to traversal.
- **CITATIONS:** none (cross-links E3-C03)
- **FEEDS:** WP-21

### E8-C19
- **STATUS:** Design-assumption (governance invariant, effectively MUST)
- **SOURCE:** ceremonies-corpus TheCelestialDualCeremony :394-404 (§VI)
- **CLAIM:** Commit authority is split as a hard rule: the produced artifact "enters the graph only if the Swordsman draws the edge" — only the boundary agent may commit, only the delegation agent may generate, and neither may act in the other's domain. "Boundary enforcement at the moment of creation: the one who protects decides what crosses."
- **CITATIONS:** none
- **FEEDS:** WP-21, WP-18

### E8-C20
- **STATUS:** Design-assumption (validity semantics)
- **SOURCE:** ceremonies-corpus TheCelestialDualCeremony :422-430
- **CLAIM:** Validity is defined by failure modes: identical outputs = one party deferred (a sovereignty violation, invalid); zero constellation overlap = the input was transmitted, not shared (connection failure, invalid); an uncommitted artifact = sovereign refusal, explicitly NOT a failure. Refusal-as-valid-outcome is a governance primitive of the corpus (kin to E6-C33's contested-entry path).
- **CITATIONS:** none
- **FEEDS:** WP-21

### E8-C21
- **STATUS:** Design-assumption (role separation)
- **SOURCE:** ceremonies-corpus celestial-key-ceremony-guide.md :266-272
- **CLAIM:** Witness and participant are formally separated evidence-holders: witnesses watch and record (photos, video, audio); participants do not record themselves — "The ceremony produces blades, not recordings. The recordings belong to the witnesses" — and witness recordings form their own attestable sequence.
- **CITATIONS:** none (cross-links E6-C19, the PT witness promise)
- **FEEDS:** WP-21

### E8-C22
- **STATUS:** Design-assumption (staged-disclosure ladder)
- **SOURCE:** ceremonies-corpus the-celestial-ceremony.md :62-79
- **CLAIM:** Trust stages in three tiers of increasing formalisation — shared experience (the key held between two bodies), constellation (the inclusion/exclusion choice IS the boundary act), forged artifact (permanent, proving more while revealing less). The proves-more-reveals-less inversion at the top tier is the corpus's staged-disclosure thesis.
- **CITATIONS:** none
- **FEEDS:** WP-21, WP-10

### E8-C23
- **STATUS:** Design-assumption (load-bearing display encoding)
- **SOURCE:** ceremonies-corpus moon-phase-notation.md :19-27, :49-55
- **CLAIM:** The moon-phase glyph is protocol content, not decoration: phase maps to stratum (count of active dimensions 0-6, derived from the artifact's hex), disclosing the sovereignty posture-count while content stays concealed — "The moon phase shows the sovereignty posture... It does NOT show the content." Consistent with the E3-C22 resolution (stratum display, not the σ budget).
- **CITATIONS:** none
- **FEEDS:** WP-21, WP-10

### E8-C24
- **STATUS:** Design-assumption (deployed-forge behavior table)
- **SOURCE:** ceremonies-corpus ceremony-engine-spec-v1_1.md §2.3-2.5 :82-107
- **CLAIM:** The deployed forge gates each of six binary dimensions on a measurable traversal condition (node count, lap count, duration, spell count), yielding stratum 0-6, a five-level charge scale, and a tier classification. This is running behavior on the single-site forge (the E3-C32 boundary: the forge runs; the cross-web engine does not).
- **CITATIONS:** none
- **FEEDS:** WP-21, WP-10

### E8-C25
- **STATUS:** Verified-record (practice evidence, small-N honestly stated)
- **SOURCE:** ceremonies-corpus ceremony-engine-spec-v1_1.md §2.6 :109-117; moon-phase-notation.md :99-101
- **CLAIM:** The forge's empirical base is N=3 artifacts by a single operator with recorded metrics (two sharing an identical constellation but differing behavioural density — the sole empirical support for the density conjecture, register C11), plus the "honest Sun blade" (five of six dimensions active, the sixth honestly dormant — cited as evidence the forge does not over-award). Small-N, single-forger: practice-record, never statistical evidence.
- **CITATIONS:** none
- **FEEDS:** WP-21, WP-11

### E8-C26
- **STATUS:** Verified-record (one performed instance; register C13 ~60%)
- **SOURCE:** ceremonies-corpus ceremony-engine-spec-v1_1.md §8 :256-272
- **CLAIM:** The bilateral witness ceremony was performed once (2026-03-29, named parties, Telegram + public channel): private field-verification of the artifact, then public reconstruction from proof signatures before witnesses — a (+) promise (forge and offer proof) answered by a (−) promise (verify privately, testify publicly). Logged at source as demonstrated-once, needs formalisation, register C13.
- **CITATIONS:** none (cross-links E6-C19)
- **FEEDS:** WP-21, WP-19

### E8-C27
- **STATUS:** Verified-record (performed 2026-07-18; provenance note: produced by this pipeline's own session)
- **SOURCE:** ceremonies-corpus rpp_inscription_2026-07-18_the-frontier-pair.md
- **CLAIM:** The Relationship Proverb Protocol was performed bilaterally and transparently logged (dated, named parties, both proverbs in clear, SHA-256 pair commitment, re-derivation convention stated), with the E3-C14 scoping carried in the record itself ("the epistemic verification layer, not a cryptographic security boundary"). PROVENANCE: this record was produced by the extraction programme's own session on the build day of E3 — it is the corpus's newest practice-record and is self-referential evidence; cite it as an instance of the protocol, never as independent corroboration of it.
- **CITATIONS:** none
- **FEEDS:** WP-21, WP-11 (as a worked instance)

### E8-C28
- **STATUS:** Design-assumption (the root two-party protocol)
- **SOURCE:** ceremonies-corpus TheCelestialDualCeremony :442-549
- **CLAIM:** The root two-party protocol runs disclosure and reflection in one session on two physically co-present devices, with the proof defined as the intersection of four independent signals (sound, understanding, constellation, text) — "No one who wasn't present can reconstruct it." An asserted co-presence-entropy argument, kin to E3-C11, with the same status: argument, not bound.
- **CITATIONS:** none
- **FEEDS:** WP-21, WP-11

### E8-C29
- **STATUS:** Design-assumption (the never-merge invariant + self-declared build state)
- **SOURCE:** ceremony-specs DUAL_TERRITORY :47, :787; ceremony-engine-spec :50, :134, :10
- **CLAIM:** The engine's non-negotiable invariant: the two agents never merge — separate processes, storage, permissions, repositories, at every level — formalised as I(S;M|FP) < ε* with the inter-agent channel as the gap made executable. The corpus stratifies its own build state explicitly: forge OPERATIONAL, ceremony engine SPECIFIED, extensions NOT YET BUILT.
- **CITATIONS:** none
- **FEEDS:** WP-21, WP-18, WP-10

### E8-C30
- **STATUS:** Design-assumption (harness governance; the held-out gate discipline)
- **SOURCE:** ceremony-specs DUAL_AGENT_HARNESS :33-44, :60-69, :195-200
- **CLAIM:** The dual-agent harness formalises ceremony as research governance: the proposer reduces/conceals, the prover commits only what survives a held-out gate enforcing I(Y_S;Y_M|X)=0 (the proposer cannot tune to the prover's witnesses), and "a proposer that grades itself builds mirages." Normative rules: every harness declares its gap or is rejected at review; the engine core is generic and never special-cased; sources of truth are referenced, never duplicated; "only the Gate makes a claim true."
- **CITATIONS:** none (register C82/C83 conditioning carried at source)
- **FEEDS:** WP-21, WP-27, WP-18

### E8-C31
- **STATUS:** Design-assumption (deployed-partial; un-tuneable gate instances)
- **SOURCE:** ceremony-specs DUAL_AGENT_HARNESS :162-179
- **CLAIM:** The built harness instance enforces its gap by structure: the delegation agent cannot render (the boundary agent owns the canvas), cannot lower the earned-unlock lattice, cannot mint agreement identifiers (external registry), and must produce outputs hashing to the recorded state; bilateral records are immutable and auditor-disputable. Partial deployment honestly stated at source (mock pass; real-bus wiring pending; loop single-round, not held-apart).
- **CITATIONS:** none
- **FEEDS:** WP-21, WP-10

### E8-C32
- **STATUS:** Design-assumption (access governance; comprehension-gated)
- **SOURCE:** ceremony-specs DUAL_TERRITORY :316-338; ceremony-engine :226-237; DUAL_TERRITORY :200, :464-470, :791
- **CLAIM:** Cross-territory access is gated by demonstrated comprehension, not credentials ("understanding-as-key as the literal access control mechanism. No credentials. No sign-up"), and the contribution-credit system is deliberately honour-based and client-side — no server verification, resistance grounded in the cost of earning through practice, credit non-purchasable and non-transferable, with earn/spend rates explicitly untested first estimates.
- **CITATIONS:** none (cross-links E3-C07; kin of the vrc mana claim in E3's economics cluster)
- **FEEDS:** WP-21, WP-10

### E8-C33
- **STATUS:** Design-assumption (inter-agent protocol grammar)
- **SOURCE:** ceremony-specs DUAL_TERRITORY :401-435 (§4.3)
- **CLAIM:** The inter-agent channel is a fixed message grammar partitioned by sender (boundary agent: slash/ward/position/ceremony-ready/home-territory; delegation agent: inscribe/scan/position/constellation/drake/hexagram) with a two-second handshake timeout after which each agent operates solo — the only permitted shared-state path, and it degrades to independence, never to merger.
- **CITATIONS:** none
- **FEEDS:** WP-21, WP-10

### E8-C34
- **STATUS:** Design-assumption (measurement-darkness mechanism; provenance flag attached)
- **SOURCE:** ceremony-specs ceremony-engine :168-183; DUAL_TERRITORY :271, :293, :793
- **CLAIM:** The "reads the page without the page knowing" mechanism is concrete: one canvas.measureText() call caches font metrics, then all layout is pure arithmetic — no getBoundingClientRect, no offsetHeight, no reflow after initial cache (stated as a MUST-NOT invariant) — so layout-observing surveillance sees nothing. PROVENANCE FLAG: the two specs cite different repository URLs for the load-bearing library (chenglou/pretext vs nicklasserra/pretext); A4-verify before any external citation.
- **CITATIONS:** Pretext library (URL unresolved between two candidates; A4)
- **FEEDS:** WP-21, WP-10

### E8-C35
- **STATUS:** Design-assumption (service-ceremony conformance contract)
- **SOURCE:** ceremony-specs 03-bilateral-cloak-ceremony-spec.md :28-31, :110-151, :178-188, :238-241, :296-307
- **CLAIM:** The bilateral service ceremony (commission → verify → weave → deliver) is a conformance contract: the weaving agent MUST verify artifact references, proverb-hash, and signatures before work; the proof file MUST carry the principal's anchor signature; verification failure obliges refund (≤5% withheld) within 24 hours; a conforming implementation must provide ten capabilities including an audit log and an honesty UI surfacing per-beat conformance to both parties. Credentials bind to the wearer's anchor without the weaver learning it; the output includes the trust edge itself. Draft, not operationally instanced.
- **CITATIONS:** none
- **FEEDS:** WP-21, WP-10

### E8-C36
- **STATUS:** CONTESTED (third instance of the tier-metric collision class)
- **SOURCE:** ceremonies-corpus ceremony-engine-spec §2.5 :102-107 (tier by stratum/dimension-count) vs celestial-key-ceremony-guide :108 (tier by lap count: Light <21, Heavy 21+, Dragon 62+)
- **CLAIM:** "Tier" is defined by two non-equivalent metrics — dimension-count in the engine spec, lap-count in the ceremony guide — so one artifact can classify differently by document. This is the THIRD instance of one word carrying two metrics (after E3-C21 lap-units and E3-C27 tier-ladders); the class is systemic and deserves a single vocabulary ruling rather than another local note. Ledger entry filed.
- **CITATIONS:** none
- **FEEDS:** WP-21, WP-10

### E8-C37
- **STATUS:** CONTESTED (semantic drift in the core algebra's interpretation)
- **SOURCE:** ceremony-engine-spec :251 ("succ = First Person") vs DUAL_AGENT_HARNESS :39-40 ("succ = the validated result. It emerges only from the two held apart")
- **CLAIM:** The same algebraic term succ in the identity neg(bnot(x)) = succ(x) is bound to the principal in one canon surface and to the validated output in another. The two readings may be intentional polysemy (what emerges from the two held apart, named at two registers), but no surface states that, and the identity is verified in running code whose meaning downstream artifacts will cite. First-Person disposition requested. Ledger entry filed.
- **CITATIONS:** none
- **FEEDS:** WP-21, WP-18

### E8-C38
- **STATUS:** CONTESTED (running-state and requirements drift between the two engine specs)
- **SOURCE:** DUAL_TERRITORY :70 (478-node graph, 984 edges, "Operational") vs ceremony-engine :70 (119-node graph, "Operational"); DUAL_TERRITORY :614-620 vs ceremony-engine :156-161 (Dragon requirements: four quantified criteria vs three loose ones)
- **CLAIM:** The two specs claim different sizes for the same live graph while both asserting operational status (likely dated snapshots, unannotated), and state materially different Dragon-transformation requirements (the territory spec adds ≥3 summonings on surveillance-heavy sites and aggregate posture ≥0.7). Neither Dragon gate is deployed. The graph-size figures need dating; the requirement sets need a governing document named. Ledger entry filed.
- **CITATIONS:** none
- **FEEDS:** WP-21, WP-10

### E8-C39
- **STATUS:** CONTESTED (practice-record date integrity)
- **SOURCE:** the-celestial-ceremony.md :268 (Universe blade forged March 30) vs ceremony-engine :272 (witness ceremony of the same blade March 29) vs celestial-ceremony-blade-pathway.md :141 (inaugural ceremony blades April 7) vs act XXIX :105 ("the day before the paper dropped")
- **CLAIM:** The flagship artifact's production date is stated three absolute ways plus one relative anchor, and the documents do not reconcile whether the late-March forge and the April 7 "inaugural ceremony blades" are one event or two. Dates in practice-records are evidence; E8's performed-record claims (E8-C25/C26) cite the per-document dates and this row carries the conflict. Ledger entry filed; reconciliation is a record-keeping disposition, not a wording fix.
- **CITATIONS:** none
- **FEEDS:** WP-21

### E8-C40
- **STATUS:** Design-assumption (governance-of-register practice, narrative form)
- **SOURCE:** tome-x Act 2 :16, :62 (restated register-neutrally; formal artifacts cite the register, never the tome)
- **CLAIM:** The register discipline is practiced by the corpus's own narrative layer: the second-substrate chronicle explicitly "mints no new conjecture", deepens C94-C96 without re-scoring or renumbering, and defers any promotion or new number to the register authority — governance-of-canon behaving as specified (E6-C31's conditions, observed in practice).
- **CITATIONS:** none (cross-links E6-C31, E6-C38..C41 for the hearthold governance content itself)
- **FEEDS:** WP-21, WP-27

### E8-C41
- **STATUS:** Verified-record (cross-implementation byte-match; the seal chain exercised end-to-end)
- **SOURCE:** tome-x Act 1 :66-68 (restated; formal pointer = the g42 demo record for-the-city-of-mages.md and the served surface)
- **CLAIM:** A real governance board was seated on the 42-seat structure (officers on the six axes, every seat and edge a signed credential, including a reciprocal human-AI credential pair), and its VRC → κ → seal chain was computed independently by a second implementation against the City's canon and "matched to the byte" — the one end-to-end exercise of E8-C03/C04's byte-exact mandate on record, cross-implementation. The E8-C14 verification strengthens this evidence: the two encoders are byte-identical for all valid Unicode (L157), so the byte-match generalises beyond the ASCII payloads exercised.
- **CITATIONS:** external cousin build (attribution fence as E6-C38)
- **FEEDS:** WP-21, WP-20

## Contested items

| Item | Conflict | Ledger |
|---|---|---|
| E8-C13 | Trust-protocol prose exclude-set (2 fields) vs code+AXIOMS (4) | L156 · RESOLVED-CORRECTION same-day (code was authoritative) |
| E8-C14 | Claimed byte-divergence reference-vs-port on non-ASCII | L156 filed · L157 REFUTED by direct byte-level test (port faithful for all valid Unicode; lone-surrogate residual noted) |
| E8-C36 | Tier by stratum vs tier by laps — third instance of the one-word-two-metrics class | L156 · vocabulary ruling requested (class-level, not local) |
| E8-C37 | succ = principal vs succ = validated result | L156 · First-Person disposition |
| E8-C38 | 478-vs-119 node graph both "Operational"; Dragon requirements differ | L156 · date the snapshots, name the governing doc |
| E8-C39 | Flagship blade date: Mar 29 / Mar 30 / Apr 7 unreconciled | L156 · record-keeping disposition |

## Sweep record

| Source | Swept | Depth |
|---|---|---|
| g42-seal-ref | 2026-07-18, fanned reader + A1 quote verification (canonical_serialise.py :8-15, hash.js :12/:20-24, TRUST :9-14/:33, AXIOMS A8) | SPEC, AXIOMS, TRUST-PROTOCOL, GEOMETRY, MODEL-SYNC, GAME-FLOW, canonical_serialise.py, schemas.json, game-of-42.json, src/hash.js; retired token confirmed absent |
| ceremonies-corpus | 2026-07-18, fanned reader | STATED DEPTH: 9 of 17 DOCS files read fully + 8 skimmed; 4 of 18 FORGE files read fully, rest matched as duplicates; the Dir-2 ceremony-engine-spec copy is ~2.3KB larger than Dir-1 and was NOT diffed (possible spec delta, unverified — future touch) |
| ceremony-specs | 2026-07-18, fanned reader + A1 quote verification (DUAL_TERRITORY :47/:70, HARNESS :39-44, engine :70/:251) | four specs in full; runecraft-protocol-spec skipped (E3 sweep covers it) |
| spec-11-invitation / open-integrity-brief | reused from the E6 sweep (E6-C31..C36) | not re-swept |
| tome-x | 2026-07-18, fanned reader + A1 quote verification (Act 1 :16/:62, Act 2 :48-50) | both acts; restated register-neutrally, never cited downstream |
| clc2026-abstract | NOT swept | external, not on disk (registry flag stands); cite the submitted abstract by reference if a claim ever needs it — no E8 claim does |
