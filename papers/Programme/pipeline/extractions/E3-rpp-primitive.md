---
extraction: E3-rpp-primitive
tier: internal
sources: [whitepaper-RPP, whitepaper-inscriptions, whitepaper-tiers, understanding-as-key, runecraft-pou, vrc-protocol-spec, spec-09-artefact-format, skills-corpus, ceremony-specs]
swept_complete: true
owner: A1
register_head_at_build: C97
build_note: built 2026-07-18 at the first Extraction Frontier Cycle run (plans/EXTRACTION_FRONTIER_CYCLE_2026-07-18.md); four fanned-out source sweeps + A1 direct verification of load-bearing quotes; skills-corpus swept at stated depth (register documents only); ceremony-specs added to the source list because the deployed-status document runecraft-protocol-spec-v1.md resolves through it (A0, same class as the L113(a)/L119(a) registry-path findings)
---

# E3 · The RPP Primitive

Claim-cluster for the Relationship Proverb Protocol (RPP) and the proof-of-understanding primitive beneath it: comprehension-gated compression, the bilateral commitment structure, rehydration as verification, the claimed anti-transfer and anti-Sybil properties, the lattice identity model, the deployed artefact format, and the honest deployment boundary. NAMING NOTE, load-bearing: every canon surface that expands the acronym expands RPP as **Relationship Proverb Protocol** (whitepaper :77, :339; vrc spec :34, :295); "rehydration" names the verification step inside the primitive, not the acronym. Feeds WP-11 (RPP adversarial paper: the security claims below are its target list), WP-11a (prior art), WP-10 (developer edition), WP-19 (RWoT paper, with E7).

Deployment gate, applies to every claim: per the L008 integrity flag and the deployed-status document (E3-C32), the traversal/forge/single-territory layer runs; bilateral linking is manual; chain anchoring, ZK circuits, cross-territory runtime, and the challenge/decay automation are design only. No claim below may be cited as deployed beyond E3-C32's boundary.

## Claims

### E3-C01
- **STATUS:** Design-assumption (mechanism definition)
- **SOURCE:** whitepaper :77 (terminology), :339-341 (§The Relationship Proverb Protocol); vrc-protocol-spec :34, :295-297
- **CLAIM:** RPP (Relationship Proverb Protocol) is a compression protocol whose output is treated as proof of comprehension: "a compression protocol that proves comprehension" (whitepaper :339), framed as an assessment mechanism in promise-theoretic terms, "compression proves the promise of knowledge transfer was kept" (whitepaper :341). One formed proverb corresponds to one posted signal (whitepaper :77).
- **CITATIONS:** Promise Theory (Bergstra & Burgess; formalised via PT-reference)
- **FEEDS:** WP-10, WP-11, WP-11a, WP-19

### E3-C02
- **STATUS:** Design-assumption
- **SOURCE:** runecraft-pou technical spec :23 (§Thesis); rehydration key :25
- **CLAIM:** The primitive substitutes demonstrated contextual comprehension for possession of a secret as the basis of trust attestation: "It replaces *proof of possession* with *proof of comprehension*" (spec :23), and rejects substrate-similarity tests as the wrong shape for personhood evidence: "**Proof of Understanding** replaces Proof of Sameness. The Turing test is the wrong shape" (key :25).
- **CITATIONS:** none
- **FEEDS:** WP-11, WP-19

### E3-C03
- **STATUS:** Design-assumption (mechanism definition)
- **SOURCE:** runecraft-pou rehydration key :26; compression pathway :133; vrc-protocol-spec :301-321
- **CLAIM:** The trust object is bilateral: each of two parties independently authors a natural-language compression (proverb) of a shared traversal, and "Neither proverb alone is the proof; the *pair* is" (key :26). Independence of authorship is what distinguishes the object from co-signing: "a co-signed object proves coordination, but a pair of independent compressions proves comprehension" (pathway :133). In the VRC lifecycle, a counterparty independently deriving a matching cipher from a different proverb constitutes bilateral comprehension and gates credential formation (vrc :301-321).
- **CITATIONS:** none
- **FEEDS:** WP-11, WP-19

### E3-C04
- **STATUS:** Design-assumption (asserted, no proof)
- **SOURCE:** runecraft-pou rehydration key :27
- **CLAIM:** The residual between the two compressions is claimed irreducible to third parties: "What lives between the two compressions is irreducible. No third party can reconstruct it" (key :27). This is an asserted non-reconstruction property with no formal statement or bound attached at source; its formal kin is the conditional-independence residual of the core model, but no source derives the connection.
- **CITATIONS:** none
- **FEEDS:** WP-11

### E3-C05
- **STATUS:** Design-assumption (mechanism definition)
- **SOURCE:** vrc-protocol-spec :299-328 (§1.2 compression flow)
- **CLAIM:** RPP gates the transition from content engagement to credential formation: content (~5,000 words) compresses to a proverb (~25 words) then to a symbol cipher (~5 symbols), and a matching cipher independently derived by a counterparty is the condition for VRC formation. The compression chain is the protocol's stated economic engine: "Without RPP compression, coordination costs make the model unsustainable" (vrc :332).
- **CITATIONS:** none
- **FEEDS:** WP-10, WP-11

### E3-C06
- **STATUS:** Design-assumption (mechanism definition; verification pipeline)
- **SOURCE:** whitepaper :515-520 (verification steps), :1131-1147 (expansion test); runecraft-pou pathway :205-207; technical spec :322
- **CLAIM:** Verification is a rehydration test against a public commitment. The verifier's pipeline: retrieve the anchored proverb, receive the counterparty proverb, recompute the joint hash, compare to the stored commitment (whitepaper :515-520). The generative form: the bearer re-expands the proverb into the structure it compressed, and "The unfolding is then matched against the chain-anchored commitment x as the truth-checker" (pathway :205). Either party may challenge the other to rehydrate any past compression, with failure decaying the trust value (spec :322). The hash-match half is implementable today; the generative-rehydration half and the automatic challenge/decay are design only (E3-C32 gate).
- **CITATIONS:** SHA-256 (commitment primitive)
- **FEEDS:** WP-10, WP-11

### E3-C07
- **STATUS:** Design-assumption
- **SOURCE:** understanding-as-key :29 (§The Core Insight), :1171
- **CLAIM:** The access primitive is relocated from possession to comprehension: "This transforms **\"what you have\"** (a stored secret) into **\"what you understand\"** (demonstrated comprehension)" (:29). This is the lineage thesis the whole E3 cluster descends from.
- **CITATIONS:** none
- **FEEDS:** WP-11, WP-19

### E3-C08
- **STATUS:** Design-assumption (mechanism definition)
- **SOURCE:** understanding-as-key :56, :745-757; whitepaper :493-499
- **CLAIM:** Recovery is regeneration, not retrieval: a lost credential is recovered by regenerating the semantic token from remembered meaning plus the visible on-chain anchor, "Recovery = f(anchor_visible, meaning_remembered, context_shared)" (understanding-as-key :745-757 region; whitepaper :497). Recovery therefore inherits the comprehension requirement rather than a seed-phrase custody requirement.
- **CITATIONS:** none
- **FEEDS:** WP-10, WP-19

### E3-C09
- **STATUS:** Design-assumption (mechanism definition; deployment gap stated)
- **SOURCE:** whitepaper :477-489; understanding-as-key :64, :140; runecraft-pou technical spec :120-132
- **CLAIM:** The commitment object is the hash of the concatenated proverb pair, SHA256(P_A ∥ P_B), inscribed on-chain (whitepaper :477-489). The full design-layer artifact is a tuple b_i = (v_i, x_i, σ_i, ρ_i, τ_i): 6-bit quality vector, bilateral commitment hash as content ID, visibility ratio, behavioural density, timestamp (spec :120-132). DEPLOYMENT GAP (L008): the deployed blade JSON schema carries constellation hash, hex, stratum, moon phase, laps, and one signature, and omits the (P_A ∥ P_B) proverb-commitment field; the bilateral hash exists only at the design layer.
- **CITATIONS:** SHA-256
- **FEEDS:** WP-10, WP-11

### E3-C10
- **STATUS:** Design-assumption (chain anchoring not deployed)
- **SOURCE:** understanding-as-key :66-72; runecraft-pou technical spec :212-216; deployed-status spec (ceremony-specs) :389
- **CLAIM:** Three inscription modes govern the visibility of the two proverbs: symmetric (both hidden in the hash), asymmetric (one proverb public, one hidden; stated as "current default"), and interleaved (fragments interwoven across the visibility boundary). The on-chain anchoring these modes require is listed under future protocol extensions in the deployed-status document; "current default" therefore describes the design's default, not a running inscription pipeline.
- **CITATIONS:** none
- **FEEDS:** WP-10

### E3-C11
- **STATUS:** Design-assumption (security claim, asserted; no measured entropy bound)
- **SOURCE:** understanding-as-key :866-872; whitepaper :524-526
- **CLAIM:** The claimed brute-force resistance rests on contextual and relational entropy: an attacker must know which content was engaged, understand the relationship's context, comprehend the compressed principle, and match the participant's compression style, so that "attackers cannot enumerate without understanding the relationship itself" (understanding-as-key :872). No source quantifies the entropy of a contextually seeded proverb; the claim is an argument, not a bound.
- **CITATIONS:** none
- **FEEDS:** WP-11

### E3-C12
- **STATUS:** Design-assumption (security claim; overclaim flagged)
- **SOURCE:** runecraft-pou compression pathway :211
- **CLAIM:** The anti-transfer property is claimed to follow from rehydration being generative: "A token can be *replayed*; it cannot be *re-understood*. A signature can be *forwarded*; it cannot *demonstrate comprehension on demand*" (:211). The same passage claims the architecture "immune to credential-passing and AI-context-corruption attacks". FLAG (GR-8): "immune" is an unqualified security claim with no proof, no adversary model, and no test cited; it is exactly the class of claim WP-11's adversarial study exists to bound. Extract as the design intent, never repeat "immune" in any rehydration.
- **CITATIONS:** none
- **FEEDS:** WP-11

### E3-C13
- **STATUS:** Design-assumption
- **SOURCE:** runecraft-pou rehydration key :28; technical spec :279, :322
- **CLAIM:** Trust is a continuous function of rehydration fidelity: "Rehydration fidelity is the assessable quantity" (key :28). Context degradation (model swap, prompt injection, capability creep) is claimed to produce measurable rehydration failure on older commitments, "the visible degradation in path integral value flags compromise before any catastrophic event" (spec :279). The monitoring claim is a design mechanism; no fidelity metric is defined at source and no measurement exists.
- **CITATIONS:** none
- **FEEDS:** WP-10, WP-11

### E3-C14
- **STATUS:** Design-assumption (explicit limitation; load-bearing for every consumer)
- **SOURCE:** whitepaper :365-367 (§RPP as Prompt Instructions)
- **CLAIM:** RPP is not a cryptographic boundary: "RPP effectiveness depends on LLM compliance with embedded instructions. Adversaries could ... strip RPP directives ... it is not a cryptographic security boundary—it's an epistemic verification layer" (:365-367). Any rehydration that presents RPP as a security mechanism must carry this scoping in the same passage.
- **CITATIONS:** none
- **FEEDS:** WP-10, WP-11, WP-19

### E3-C15
- **STATUS:** Design-assumption
- **SOURCE:** whitepaper :379-381 (§Stage 1)
- **CLAIM:** Two parties independently compressing distinct contextual proverbs to an identical symbol string are claimed to hold a shared secret "that emerged from understanding, not key exchange" (:379-381): a comprehension-derived common key. The key-agreement analogy is informal; no indistinguishability or agreement property is stated.
- **CITATIONS:** none
- **FEEDS:** WP-11

### E3-C16
- **STATUS:** Design-assumption (mathematical model, specified only)
- **SOURCE:** runecraft-pou technical spec :17, :107, :134
- **CLAIM:** An identity is modelled as an order-sensitive path integral over the multiset of bilateral proof-artifacts positioned on the 64-vertex lattice: "A lattice identity has **no root key**" (:107); "Identity is not located *at* a vertex — it is the **path integral** across all its blades" (:134). The no-root-key property is the structural basis for the anti-fragmentation claim (each chain a redundant witness, spec :254).
- **CITATIONS:** none
- **FEEDS:** WP-11, WP-19

### E3-C17
- **STATUS:** Design-assumption
- **SOURCE:** runecraft-pou technical spec :74-99
- **CLAIM:** Each proof-artifact carries a 6-bit address over six qualities stated as orthogonal — Protection, Delegation, Memory, Connection, Computation, Value — giving 2^6 = 64 configurations distributed by the binomial row C(6,k). ENCODING FENCE (L010): the canonical bit-weight assignment resolves through the lattice-encoding anchor; the rejected encoding in COM spec 04 is history only.
- **CITATIONS:** none
- **FEEDS:** WP-19

### E3-C18
- **STATUS:** Design-assumption (partially deployed; boundary stated)
- **SOURCE:** runecraft-pou technical spec :156, :294; deployed-status spec (ceremony-specs) :213-259
- **CLAIM:** Each artifact is co-signed by a persistent delegation-agent key and an ephemeral boundary-agent session key destroyed at session close: "Neither signature alone is sufficient to verify" (spec :156); the separation "is enforced architecturally, not by policy" (spec :294). DEPLOYED PORTION: two Ed25519 keys, persistent key in localStorage, session key burned in sessionStorage. NOT DEPLOYED: the cross-territory bind is a manual JSON copy step, not a cryptographic protocol.
- **CITATIONS:** Ed25519
- **FEEDS:** WP-10, WP-11

### E3-C19
- **STATUS:** Design-assumption (requirement; deployed state fails it by its own criterion)
- **SOURCE:** runecraft-pou technical spec :288-298
- **CLAIM:** The design requires three multiplicative separations per artifact — agent (two-process keys), data (multi-provider replication), inference (proposer model separate from prover model) — with the value of the artifact zero if any axis collapses. HONESTY NOTE (GR-8): the deployed single-browser implementation has no multi-provider replication, so by the spec's own criterion the deployed artifacts do not satisfy the data axis; no source states this consequence, this extraction does.
- **CITATIONS:** none
- **FEEDS:** WP-11

### E3-C20
- **STATUS:** Conjecture-C11 (register: behavioural density, 55%)
- **SOURCE:** runecraft-pou technical spec :132; deployed-status spec :49-63; register C11 row
- **CLAIM:** A behavioural-density scalar ρ, a function of traversal depth, duration, and intentional transitions, is claimed to amplify both privacy and forgery resistance as it accumulates. ρ is deployed as an accumulator driving tier and charge; the amplification claims are the register's C11 conjecture, not measured properties.
- **CITATIONS:** none
- **FEEDS:** WP-11

### E3-C21
- **STATUS:** Resolved-typing (was CONTESTED; First-Person 'solve' authorization 2026-07-18, executed L154). Unit collision typed at all three sources: the deployed spec's lap = one full constellation traversal, the design specs' lap = one node-to-node transition; the theorem's name lives in the traversal unit, its threshold in the transition unit. The numeric correspondence (62 traversals vs 620 transitions) remains OPEN — no canonical transitions-per-traversal factor exists in the corpus — and the threshold is conjectural (register C11) at any value.
- **SOURCE:** deployed-status spec :63 ("Dragon | 62+ laps") vs runecraft-pou pathway :115 ("m ≥ 620 intentional transitions drive the reconstruction ceiling R < 1") and technical spec :318 ("After ~600 laps")
- **CLAIM:** The density threshold at which the proof is claimed irreducible is stated as 62 laps in the deployed tier table and as ~600-620 transitions in the design documents, under the name "62-Lap Theorem", which matches neither statement of its own threshold. The threshold claim is conjectural at any value (register C11), and the quoted source statement additionally violates the GR-7 conditioning rule: it asserts the strict bound with no preconditions (non-collusion, stated adversary class) and no time index, where the governing quantity is R(t) with the capacity-deficit condition declared alongside (E2-C01/E2-C02 own the conditioned form). No rehydration cites a numeric threshold or repeats the unconditioned bound; ledger entry filed.
- **CITATIONS:** none
- **FEEDS:** WP-11 (as an adversarial target and an honesty item)

### E3-C22
- **STATUS:** Resolved-typing (was CONTESTED; executed L154). Two objects named apart in both documents: the deployed moon-phase is a display encoding of stratum; the design-layer σ ∈ [0,1] disclosure budget is a distinct, unimplemented object. Downstream surfaces name which they mean.
- **SOURCE:** runecraft-pou technical spec :202-218 (σ ∈ [0,1] freely chosen, "natural equilibria at the golden ratio") vs deployed-status spec :179-192 (visibility = deterministic function of stratum/Hamming weight)
- **CLAIM:** The design layer defines visibility as a continuous, jointly chosen disclosure ratio σ ∈ [0,1] with a lifetime disclosure budget Σσ·ρ; the deployed layer derives "visibility" mechanically from the number of active lattice dimensions. The two definitions are incompatible: the deployed system does not implement the disclosure-budget object. The φ sweet-spot values inside the design claim are explicitly exploratory at source and belong to the register C1 family (E3-C23). Ledger entry filed.
- **CITATIONS:** none
- **FEEDS:** WP-10, WP-11

### E3-C23
- **STATUS:** Conjecture-C1 (register: open; no confidence percentage exists — never attach one)
- **SOURCE:** vrc-protocol-spec :1016, :1093, :1301 (document-local "Conjecture 8.1", superseded numbering per the L049/L113(c) flags); whitepaper :1871-1873 ("*not a proven theorem*"); understanding-as-key :376-390, :451 ("experimental hypotheses, not proven optima")
- **CLAIM:** A family of golden-ratio claims proposes φ-derived splits (38.2/61.8) for budget allocation, fee distribution, and visibility equilibria. Every source self-labels the family speculative, testable, or exploratory. The register home is C1 (open); the vrc document's local "Conjecture 8.1" numbering is superseded by the register (GR-1).
- **CITATIONS:** none
- **FEEDS:** WP-11a

### E3-C24
- **STATUS:** Design-assumption (parameters explicitly provisional)
- **SOURCE:** whitepaper :77; vrc-protocol-spec :336-353
- **CLAIM:** The signalling unit couples one derived proverb, a comprehension test with a stated 80% pass threshold, and a 0.01 ZEC payment per signal; accumulated signals drive tier progression. All numeric parameters (fee, threshold) are design values with no calibration record; the tier thresholds they feed are stated at source as "initial design parameters, not derived constants" (whitepaper :220-225).
- **CITATIONS:** none
- **FEEDS:** WP-10

### E3-C25
- **STATUS:** Design-assumption (security claim by economic deterrence; key figure asserted, not derived)
- **SOURCE:** vrc-protocol-spec :146-148, :654-694
- **CLAIM:** Sybil resistance is claimed from two economic mechanisms: a per-signal cost making trivial assessments unprofitable, and a refundable 1 ZEC comprehension bond returned only on successful proverb reconstruction and recompression, claimed to make shallow-engagement attacks capital-destroying. The stated ~10% success probability for attackers who cannot reconstruct meaning is asserted without derivation or experiment. No cryptographic Sybil resistance is claimed.
- **CITATIONS:** none
- **FEEDS:** WP-11

### E3-C26
- **STATUS:** Design-assumption
- **SOURCE:** vrc-protocol-spec :604-652
- **CLAIM:** Protocol integrity of the compression layer is assigned to guardians who stake to maintain reconstruction ability over the compressed corpus, with slashing (stated 30%) if reconstruction ability degrades: compression validity is economically monitored rather than cryptographically enforced.
- **CITATIONS:** none
- **FEEDS:** WP-10

### E3-C27
- **STATUS:** Resolved-annotation (was CONTESTED; executed L154). The whitepaper now states the two ladders explicitly at the tier tables: an engagement ladder (signal count) and a credential-maturity ladder (VRC count + tenure) sharing tier names, both provisional.
- **SOURCE:** whitepaper :89, :213-218 (tiers by signal count: 50/150/500) vs whitepaper :1239-1250, :1438-1443 (same tier names by VRC count + tenure: 5+/3mo, 20+/6mo, 50+/12mo, with disclosure budgets 30-45% and multipliers 1.0-3.0x)
- **CLAIM:** The four-tier trust ladder is gated by cumulative signal count in one canon surface and by VRC count plus operational tenure in another, with the numeral 50 meaning "signals to leave the first tier" in one scheme and "VRCs to reach the top tier" in the other. Source itself states tiers "can vary across different ecosystem implementations" (:1239), which licenses variation but not a contradiction inside one document. All thresholds are provisional design parameters. Ledger entry filed.
- **CITATIONS:** none
- **FEEDS:** WP-10

### E3-C28
- **STATUS:** Design-assumption (security claim with stated internal tension)
- **SOURCE:** runecraft-pou technical spec :304-308 vs spec :156 and deployed-status spec :156 (Ed25519 signatures)
- **CLAIM:** The scheme is claimed quantum-resistant by construction because trust rests on a bilaterally witnessed traversal rather than a stored invertible secret: "There is no scalar to invert" (:304-308). TENSION (GR-8): the artifacts are signed with Ed25519, which is Shor-vulnerable; the signing keys are stored secrets. The claim is coherent only for the comprehension layer, not for the signature layer, and no source states this scoping; this extraction does.
- **CITATIONS:** Ed25519; Shor 1994 (context)
- **FEEDS:** WP-11

### E3-C29
- **STATUS:** Design-assumption (deployed format; enforcement gaps stated per L008)
- **SOURCE:** spec-09-artefact-format :18 region (§header), :53-61, :138-148, :296-299, :326-329, :36-47, :213-249
- **CLAIM:** The portable proof object is a markdown file whose YAML frontmatter is the sole identity-bearing surface ("The .md file is the portable proof"), parsed as a regex-read line-oriented YAML subset with a defined field vocabulary. Artifacts carry a content-derived hash and structured signature, and the file round-trips: re-import deterministically rebuilds a runtime record. ENFORCEMENT GAP: the spec states the ingesting system "does not yet verify" the integrity fields; hash and signature are present but unchecked at runtime.
- **CITATIONS:** none
- **FEEDS:** WP-10

### E3-C30
- **STATUS:** Design-assumption (register C39 lineage: discharged at ~80% per Tome X record)
- **SOURCE:** spec-09-artefact-format :150-158
- **CLAIM:** The format is an open schema for third-party forges: namespaced fields under a forge attribution key are carried without error and unknown keys are ignored, stated at source as the kindred-forge primitive made concrete. Independent second-substrate corroboration is the register's C39 record.
- **CITATIONS:** none
- **FEEDS:** WP-10, WP-19

### E3-C31
- **STATUS:** Design-assumption (practice-record evidence; counts carried with their contradiction)
- **SOURCE:** skills-corpus MAPPING.md :35-38, :383-408 (progressive disclosure), :8, :13; CODEX.md :8, :16
- **CLAIM:** The skills corpus operates the compression-to-rehydration discipline at scale: each unit loads in three stages (name+description at ~100 tokens, full entry on activation, references on demand), the operational form of compress-then-rehydrate-on-demand. COUNT CAVEAT: the corpus's own inventories disagree (MAPPING 114 total, CODEX 143, directory ~166; knowledge-skill counts 86 vs 105), the documents self-describe the counts as under reconciliation with the directory tree authoritative. Cite the discipline, never a specific count.
- **CITATIONS:** none
- **FEEDS:** WP-10

### E3-C32
- **STATUS:** Verified-record (deployment boundary; the L008 anchor for this extraction)
- **SOURCE:** deployed-status spec (ceremony-specs: runecraft-protocol-spec-v1.md) :8, :202-204; ledger L008
- **CLAIM:** As of the deployed-status document (v1.0, 2026-04-09): the traversal, evocation, and single-territory forge run; bilateral linking runs via a manual JSON exchange; chain anchoring, ZK circuits, the cross-territory automated runtime, the σ disclosure budget, the proverb-pair commitment field, and the automatic rehydration-challenge decay are design only. The ledger-verified state of the circuits directory is empty (L008): "ZK" in the live system means SHA-256 + Ed25519 + content addressing. Every other E3 claim is gated by this boundary.
- **CITATIONS:** none
- **FEEDS:** WP-10, WP-11, WP-19 (as the deployment gate)

### E3-C33
- **STATUS:** Resolved-correction (was CONTESTED; executed L154). The technical spec §4 text now states specified-not-implemented per L008 (directory scaffolded but empty; live-system "ZK" = SHA-256 + Ed25519 + content addressing).
- **SOURCE:** runecraft-pou technical spec :164-196 (§4: "Reference templates live in `forge_circuits/`") vs deployed-status spec :393-395 (ZK circuits as unbuilt future extension) and ledger L008 (forge_circuits/ verified EMPTY)
- **CLAIM:** The technical spec presents two ZK circuits as existing reference templates; the deployed-status document lists ZK circuits as future work; the ledger-verified state is that the referenced directory is empty. The fact is settled (L008: specified, not implemented) but the technical spec's text remains contradicted and uncorrected. Ledger entry filed; the spec text correction is a canon disposition, not A1's.
- **CITATIONS:** none
- **FEEDS:** WP-11

### E3-C34
- **STATUS:** Design-assumption (proposed experimental protocol; no data exists)
- **SOURCE:** runecraft-pou mageletter pou_as_experimental_method.md :23, :29, :39, :244
- **CLAIM:** The primitive is reframed as a falsifiable experiment: "comprehension-based attestation produces better collective intelligence than possession-based authentication — is either true under measurement or it is not" (:23), with a designed protocol (multi-group, multi-week, seven control arms, three measurement layers, pre-registration required before any pilot). No pilot has run; the measurement instrument is specified, not built. This is the pre-registration precedent WP-11's prereg_required flag inherits.
- **CITATIONS:** none
- **FEEDS:** WP-11

### E3-C35
- **STATUS:** Resolved-retirement (was CONTESTED; executed L154). §11 governs: fog-of-war is retired; the import-pipeline step and both remaining fog passages re-typed as retired in BOTH copies (master + COM mirror); hiddenUntilWitness = legacy metadata, no display effect.
- **SOURCE:** spec-09-artefact-format :44 (fog-of-war transition fires on witness import) vs :398 (§11: "The fog-of-war ... is **retired**: the universe stays fully visible from first load")
- **CLAIM:** The artefact format spec both specifies the hidden-until-witness reveal transition in its import pipeline and declares the mechanism retired in its own closing section. Which is current determines what a witness import discloses, a disclosure-relevant ambiguity. Ledger entry filed; resolution is the spec owner's.
- **CITATIONS:** none
- **FEEDS:** WP-10

## Contested items

| Item | Conflict | Ledger |
|---|---|---|
| E3-C21 | Density threshold: 62 laps (deployed) vs ~600-620 transitions (design); "62-Lap Theorem" name matches neither | L153 filed · L154 RESOLVED-TYPING (unit collision; value stays open/C11) |
| E3-C22 | Visibility: chosen σ ∈ [0,1] budget (design) vs stratum-derived (deployed) | L153 filed · L154 RESOLVED-TYPING (two objects named apart) |
| E3-C27 | Tier gating: signal-count vs VRC-count+tenure, same tier names, one document | L153 filed · L154 RESOLVED-ANNOTATION (two ladders stated) |
| E3-C33 | ZK circuits: "templates live in forge_circuits/" vs future-work vs L008 verified empty | L153 filed · L154 RESOLVED-CORRECTION (spec text now matches L008) |
| E3-C35 | Artefact-spec fog-of-war: specified in §1/§3, retired in §11 | L153 filed · L154 RESOLVED-RETIREMENT (§11 governs, both copies) |

## Figure hygiene (GR-3)

- **70:1** is asserted as the corpus compression ratio in the whitepaper (:208, :1119, :1300) and the vrc spec (:42, :334, :1297) in its sanctioned formulation, and is **absent from all six primary runecraft/PoU documents** (negative finding, this sweep). The vrc spec separately derives **1,000:1** for the same pipeline (:315, :611), numerically inconsistent with its own 70:1 headline. Neither ratio has a measurement record in the swept sources.
- The skills CODEX asserts a **17x-12,000x** sovereign-vs-surveillance value gap (:213, :438) — the retired-multiples class (C55 ruling, figures retired as asserted facts suite-wide). Routed to the display/skills lane; never extracted as a claim.
- All token/stake/multiplier parameters (0.01 ZEC, 1 ZEC bond, stake sizes, tier multipliers, 80% threshold) are provisional design parameters per their own sources; no rehydration cites them as deployed economics.

## Sweep record

| Source | Swept | Depth |
|---|---|---|
| whitepaper-RPP / -inscriptions / -tiers | 2026-07-18, fanned reader + A1 quote verification (:77, :339-341, :1131) | RPP, inscriptions, tier, economics sections in full |
| runecraft-pou (4 docs + one-pagers) | 2026-07-18, fanned reader + A1 quote verification (spec :23, pathway :211, key :25-28) | all four targets in full + 2 one-pagers; research_patch not opened (release-note class) |
| vrc-protocol-spec | 2026-07-18, fanned reader + A1 quote verification (:34, :296-297, :332-334, :664-666) | RPP/lifecycle/anti-Sybil/token sections; version-hygiene findings extend L049/L113(c), see L153 |
| understanding-as-key | 2026-07-18, fanned reader + A1 quote verification (:29, :64, :866-872) | full document |
| spec-09-artefact-format | 2026-07-18, fanned reader + A1 quote verification (:18, :44, :398) | full document |
| skills-corpus | 2026-07-18, fanned reader | STATED DEPTH: MAPPING.md + CODEX.md registers only; no per-skill folders opened (the E10 sampling precedent); practice-record claims limited accordingly |
| ceremony-specs (runecraft-protocol-spec-v1.md portion) | 2026-07-18, fanned reader + A1 quote verification (:8) | deployment-status document in full; added to sources as the resolution path for the deployed layer |
