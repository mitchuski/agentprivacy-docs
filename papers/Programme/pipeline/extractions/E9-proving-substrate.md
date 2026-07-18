---
extraction: E9-proving-substrate
tier: internal
sources: [spec§15, spec§27, C81-C84, folding-citations, shor-mage-record, blade-forge-spec, aletheia-lethe-note, proof-packet-spec, kappa-impl, schrottenloher-note]
swept_complete: true
owner: A1
register_head_at_build: C96
build_note: built 2026-07-10 under the L008 standing fence (design vs deployment stated per claim); folding-citations resolved to spec §15.7 + v6-draft Part V §V.2 pending a SOURCES.md row (registry gap flagged to A0, the L113(a) class)
---

# E9 · The Proving Substrate

Claim-cluster for the proving substrate itself: what proof systems and folding schemes the canon specifies, the proof-packet and configuration-object wire formats, the ceremony proving-system design, the deployed cryptographic core (SHA-256 content addressing + Ed25519 signatures + the kappa label, the one deployed piece per L008), the proving-method practice record from the external circuit arena, the proof-medium/witness-substrate role pairing, and the dated-strength record of the 2026 ECDLP circuit reconstruction. Feeds WP-22 (zkproof-note, TIER-S; consumes E9 + E2) and WP-12 (existence-leak hunt, ongoing).

**Standing hazard, stated once and then per claim (L008):** the zero-knowledge proving substrate of this corpus is SPECIFIED, NOT IMPLEMENTED. The forge repository's `forge_circuits/`, `blades/`, `uor_mappings/` and `tests/` directories are README-plus-.gitkeep stubs (re-verified by direct inventory 2026-07-10). The operational cryptography across the deployed surfaces is SHA-256 content addressing, Ed25519 signatures, and the kappa (κ) content-address law. Every claim below carries an explicit design-vs-deployment statement.

**Ownership block (the E7 pattern, per L113):** the moving-ceiling and existence-leak LAWS are owned by E2 and E1; E9 owns the substrate they run on and never restates them as its own. Cross-references: C81 (Existence-Leak law, ~70%, Stage-2 open) is owned at **E2-C08**; C82 (Moving Ceiling, ~65%) at **E2-C03**; C83 (Compositional Leakage Amplification, ~55%) at **E1-C08**; C84 (Existence-Leak Discount / Mosca coupling, ~50%) at **E2-C09**; C92 (Tarski reading, ~70% capped at C81's base) at **E2-C14**; C93 (content-addressed liveness leak, ~55%) at **E2-C15**; the Zcash Orchard verified record at **E2-C05**; the withheld-result episode verified record (Babbush et al. primary attribution, the spacetime-volume metric discipline of L062(a)) at **E2-C07**; the complement-pair arithmetic and the phi-adjacency conjecture (C54) at **E1-C28/E1-C29**; the dual-runtime, two-extension, and dual-agent-harness separation designs at **E1-C36/E1-C37/E1-C38**; the C87 reading from the holospace side at **E7-C30** (which defers the folding literature here; E9-C13/E9-C14 discharge that deferral). Register wording and confidence for C81 to C84 were re-verified verbatim against `research/CONJECTURE_REGISTER_V6.md` at head C96 this build.

**Filter note for WP-22 (TIER-S) consumers, proposed (the L111(a) genre precedent, subject to A0 ruling at the WP-22 card):** design-status claims below are admissible at TIER-S as design descriptions with implementation status carried verbatim; the deployed-core claims (E9-C01, E9-C02, E9-C04, E9-C05 deployment half, E9-C06) are the conformance-grade material. Conjecture-status claims (E9-C12, E9-C13) and the E2-owned laws feed WP-22 as labelled open questions or via E2's own discipline only, never as claims.

**Depth per source (the L103 fence):**
- `spec§15` (formal spec §15.1 to §15.9): swept full. §15.3, §15.4, §15.7, §15.8 extracted; §15.1/§15.2/§15.5/§15.6 (ceremony cycle, trust ladder, phase notation, tier axes) noted and left to E8/E3 homes except where the SPECIFICATION.md counterpart is extracted here; §15.9 (C66 credential-versus-capability) left to E7's identity inventory.
- `spec§27` (temporal thread + §27.1): swept full; yields cross-references only (C84 owned at E2-C09; the HNDL cost backbone rides with that claim). No E9-numbered claim minted from §27.
- `C81-C84` (register rows, Bands VII/VIII): verified verbatim at head C96; ownership block above.
- `folding-citations`: resolved to spec §15.7 and research/privacy_value_v6_draft.md Part V §V.2 (the two carriers of the folding-scheme citation family). REGISTRY GAP: the slug has no SOURCES.md row; row proposed to A0.
- `shor-mage-record` (SHOR corpus): `papers/methodology_draft.md`, `claims_register.md`, `frontier.json`, `CASE_STUDY_2026-06-30_dual-agent-vs-ecdsafail.md`, `harness/swordsman_mage_pqc.mjs` header swept full; `notes/KILLED_LEVERS.md` and the research-notes series surveyed via the claims-register rows only (the per-kill detail is E10-method and WP-12 working material, not substrate claims). Attribution fence applied per claim.
- `blade-forge-spec` (FORGE): `zk_swordsman_blade_forge_v3_0.md` (body self-identifies as version 3.2; L049-class filename/body drift noted) and `SPECIFICATION.md` (body self-identifies as version 1.0.1, working draft) swept full; stub directories inventoried directly.
- `aletheia-lethe-note`: DOCS copy swept full (carries the 2026-06-09 reseat notice); FORGE copy not consulted (the E1 precedent).
- `proof-packet-spec` (MASTER): SPEC_proof_packets_and_tracing_v1.md v1.1 swept full including §14 amendments.
- `kappa-impl` (SOULBIS): `sigil/index.html` grounding legend and the κ/packet/Merkle code paths read directly; `star/index.html`, `lattice/index.html`, `scripts/verify-static.cjs` taken at the registry description plus the sigil page's shared-canon statement (deep per-page conformance is E11's territory). Survey depth stated; nothing below depends on the unread pages beyond the shared-canon assertion.
- `schrottenloher-note`: swept full at its dated strength (2026-06-02, Stage 1, n = 1), with the Run-0 erratum (its local "C40" reads C81) applied.

## Claims

### E9-C01
- **STATUS:** Design-assumption (deployment inventory; verified by direct inspection 2026-07-02 at L008, re-verified 2026-07-10)
- **SOURCE:** kappa-impl; blade-forge-spec (stub inventory); spec §15.3; L008 standing fence
- **CLAIM:** The deployed cryptographic core of the corpus is exactly three primitives: SHA-256 content addressing (constellation hashes, class and instance proofs, the κ label), Ed25519 signatures (identity binding, held and burned keypairs), and the κ content-address law over canonical JSON. No zero-knowledge proof system is deployed anywhere in the corpus: the forge repository's circuit directories are empty stubs, and every surface that names ZK behaviour realises it either as a hash commitment (prove-that-not-what) or as a design document. Deployment status: the three primitives run on the SOULBIS pages, the MASTER libraries, and the runecraft protocol; the ZK layer is design only.
- **CITATIONS:** FIPS 180-4 (SHA-256); RFC 8032 (Ed25519); direct inventory of `zk blades forge/forge_circuits/` et al.
- **FEEDS:** WP-22 (conformance-grade), WP-12

### E9-C02
- **STATUS:** Design-assumption (deployed as described; reference implementation running)
- **SOURCE:** kappa-impl (sigil/index.html grounding legend + code); proof-packet-spec §6, §14.2
- **CLAIM:** The κ label law (Law L5): κ = "sha256:" + SHA-256 over the canonical JSON form of the object, where canonicalisation sorts keys recursively, emits no whitespace, encodes UTF-8, drops undefined fields, preserves array order, and excludes exactly one field, the label field itself (κ for keys, `proof` for packets; one canon parameterised by the excluded field). The label is never trusted from the carrier: it is re-derived from content on every import ("never trusted, always re-derived"). The exported PNG carries the full key as base64 JSON in a PNG tEXt chunk (keyword `cityKey`) with κ stamped; import re-derives κ from the carried content. Deployment status: deployed on the sigil, star, and lattice pages and the packet verifier; the same code path verifies City Keys and proof packets. Adjacency note for WP-12: a deployed, deduplicating content-address law is precisely the design surface of the liveness-leak conjecture C93, owned at E2-C15; E9 supplies the deployed instance surface, not the law.
- **CITATIONS:** none external (reference implementation; SHA-256 as at E9-C01); PNG tEXt per ISO/IEC 15948.
- **FEEDS:** WP-22 (conformance-grade), WP-12 (instance surface for E2-C15)

### E9-C03
- **STATUS:** Design-assumption (deployed at spec v1.1; phases 1 to 9 built, phase 10 not built)
- **SOURCE:** proof-packet-spec §2 to §5, §8, §14.4
- **CLAIM:** The proof-packet format is a two-layer model: a class proof (SHA-256 of the static artefact descriptor, rolled up to a `district_root`) and an instance proof packet (SHA-256 of the bearer's actual traced action under the same Law-L5 rule). A packet's canonical form includes `anchoredTo` (the class proof) and `districtRoot`, so an instance commits to the class it claims to instantiate and cannot claim a class it does not anchor to. The packet's privacy behaviour (`payloadMode`) is a pure function of the artefact's declared witness type, not a UI choice: sealed (commitment only, raw content never stored), revealed (public body), refractive (declared public facet plus sealed remainder), composed (Merkle composition of child packet proofs), relational (accruing bond). Ordered `ceremonyTrace` phase evidence makes the steps provable, not just the label. Deployment status: phases 1 to 9 built and regression-reviewed across three instances (master, spellweb, star) at v1.1 (2026-06-12); the interop phase (10) is not built.
- **CITATIONS:** none external (design and build record in source).
- **FEEDS:** WP-22, WP-12

### E9-C04
- **STATUS:** Design-assumption (deployed; normative rule with published conformance vector)
- **SOURCE:** proof-packet-spec §14.1; kappa-impl (packetsDigest)
- **CLAIM:** The packets digest carried on a key (`packets.root`) is a Merkle root computed as: leaves = the packets' full proof strings sorted lexicographically (order-independent, matching the κ canon's insertion-order independence); node = "sha256:" + SHA-256 over the UTF-8 bytes of left + "|" + right; odd node promoted unchanged; root = the single survivor; a single packet's digest is its own proof. A published conformance vector (three named leaves yielding root sha256:07f20f689c8bef2d8a9a2a71d94e7014ea8398cc603b0ff72dadba5c517983d1) is reproduced independently by the consuming pages. Deployment status: deployed (reference implementation `proof-packet-digest.ts`; independent verification on the SOULBIS pages).
- **CITATIONS:** Merkle 1987 (hash trees) as the construction family; the conformance vector is source-internal and machine-checkable.
- **FEEDS:** WP-22 (conformance-grade)

### E9-C05
- **STATUS:** Design-assumption (deployed lineage mechanism; the accumulator reading is Conjecture-C87, owned at E9-C13)
- **SOURCE:** kappa-impl (prior field); spec §15.7
- **CLAIM:** Key lineage is a hash chain: an evolved key export stamps `prior` = the κ of the key it grew from; an unchanged re-export keeps both `prior` and κ unchanged (lineage marks evolution, not circulation). Design-vs-deployment split stated exactly: the deployed object is a hash CHAIN of content addresses; the succinct-ACCUMULATOR reading of that chain (verification time independent of chain length) is conjecture C87 and has no circuit realisation. The deployed chain is compatible with, but is not, an incrementally verifiable computation.
- **CITATIONS:** none external (deployed mechanism); folding literature at E9-C14.
- **FEEDS:** WP-22

### E9-C06
- **STATUS:** Design-assumption (deployed at spec date; the erasure-grade design is owned at E1-C36)
- **SOURCE:** spec §15.3, §15.4
- **CLAIM:** The forge cryptographic property table maps five properties to deployed primitives: content addressing = SHA-256 constellation hash; tamper evidence = hash chain (each configuration object references the previous); pre-evocation lock = commitment scheme (constellation fixed before the walk); identity binding = Ed25519 signature (delegation-agent key, persisted in localStorage); bilateral binding = dual Ed25519 (delegation-agent key held + boundary-agent key generated per ceremony in sessionStorage and destroyed at session close). The key destruction enforces the structural-erasure requirement at the identity layer (the C17 linkage and the storage-grade design are E1-C36's claim; E9 carries only the primitive inventory). Deployment status: deployed per the runecraft protocol record; no ZK primitive appears in the table.
- **CITATIONS:** RFC 8032; commitment usage is hash-based (E9-C01 primitives).
- **FEEDS:** WP-22 (conformance-grade)

### E9-C07
- **STATUS:** Design-assumption (specified, not built: phase 10 of the packet spec)
- **SOURCE:** proof-packet-spec §12, §14.4
- **CLAIM:** The designed standards projection of the packet format: a pure function emitting a W3C VC Data Model 2.0 object from a packet (issuer = bearer did:key; credentialSchema = the class proof; proof type chosen by payloadMode: a ZK/BBS+ selective-disclosure proof for sealed/refractive, a data-integrity signature for revealed), plus a ToIP trust-registry export rooted at `district_root`. This is the ONLY place the corpus specifies a concrete external ZK proof family (BBS+ selective disclosure), and it is explicitly unbuilt: v1.1 records "remaining: phase 10 interop only". Deployment status: design only; the native hash-commitment packet is the deployed object.
- **CITATIONS:** W3C VC Data Model 2.0; BBS+ signature scheme (IRTF CFRG draft lineage); ToIP Trust Registry Protocol; trusttasks.org.
- **FEEDS:** WP-22

### E9-C08
- **STATUS:** Design-assumption (design only; SPECIFIED NOT IMPLEMENTED, L008)
- **SOURCE:** blade-forge-spec (v3 document §1, §8; forge_circuits README)
- **CLAIM:** The forge design thesis: the 64-vertex lattice (2^6 configurations on Z/(2^6)Z with the five-operation signature neg, bnot, xor, and, or) is itself the constraint system of the intended proving substrate. Specifically: the tetrahedral adjacency matrix is the constraint system "the R1CS or PlonK circuit, expressed geometrically"; each vertex is a gate whose fan-in/fan-out is fixed by the geometry; a proof is computed on the 96-edge boundary rather than in the 64-vertex bulk. The circuit families named for the implementation are Plonkish, Halo2, and Plonky2 ("per-circuit implementation files (Halo2 / Plonky2 / custom) belong here when authored"). Deployment status: NO circuit is authored; the directories are stubs by direct inventory; the document's OPERATIONAL header refers to the lattice/graph interface layer running on the public site, not to any proving system. Design vs deployment could not be further apart on this claim and both halves are stated.
- **CITATIONS:** Groth16/R1CS lineage and PlonK (Gabizon, Williamson, Ciobotaru, ePrint 2019/953) for the named constraint-system families; Halo2 (Zcash) and Plonky2 (Polygon Zero) as named toolchains.
- **FEEDS:** WP-22, WP-12

### E9-C09
- **STATUS:** Design-assumption (format deployed at the hash+signature layer; the witness layer design only, L008)
- **SOURCE:** blade-forge-spec (SPECIFICATION.md §3, §8)
- **CLAIM:** The configuration-object wire format ("blade"): { id: SPELL-{hash}-{stratum}; hex 0x00 to 0x3F; stratum = Hamming weight 0 to 6; spectrum = six booleans; phase; hash = SHA-256 of constellation; signature = Ed25519 commitment }. Validity is checked by six deterministic rules (range, popcount consistency, spectrum decomposition, phase mapping, hash, signature against the forge public key). The "forging" is DEFINED as a zero-knowledge witness proving derivation-path existence without revealing the path ("same blade, infinite forgings = zero knowledge"). Design-vs-deployment split: the object format and its six checks run on the deployed pages using only E9-C01 primitives; the forging-as-ZK-witness layer has no realisation, and the deployed derivation evidence is a content-addressed certificate (hash), which hides nothing from whoever holds it. The zero-knowledge property of the format is aspiration priced at the design tier, not a deployed property.
- **CITATIONS:** none external beyond E9-C01 primitives.
- **FEEDS:** WP-22, WP-12

### E9-C10
- **STATUS:** Design-assumption (disclosure-encoding design; deployed as a display convention)
- **SOURCE:** blade-forge-spec (SPECIFICATION.md §4); spec §15.5
- **CLAIM:** The visibility notation encodes posture, not content: a configuration's stratum (0 to 6) maps to a seven-step phase scale, showing WHICH dimensions are active without showing WHAT content activated them. A full-stratum object proves "all six dimensions active" without revealing which nodes or interactions produced the configuration. This is a selective-disclosure DESIGN at the granularity of dimension counts; it carries no cryptographic hiding beyond not-storing (the deployed packets' sealed mode, E9-C03). Deployment status: the display convention is live; no cryptographic binding between phase and hidden content exists.
- **CITATIONS:** none external.
- **FEEDS:** WP-22

### E9-C11
- **STATUS:** Design-assumption (speculative, source-labelled ~25%; design only, L008)
- **SOURCE:** blade-forge-spec (v3 document §3, §11)
- **CLAIM:** The intended hardness source of the forge design: toroidal boundary conditions create unbounded cyclic path multiplicity between any two vertices, so a verifier can check a configuration's properties while witness extraction (which of infinitely many derivations produced it) is claimed infeasible. The source's own honest assessment prices this at ~25% ("whether the toroidal topology creates sufficient computational hardness for practical ZK security parameters"). E9 carries the design claim at exactly that strength: an unproven hardness assumption with no security reduction, no parameter set, and no implementation. The related boundary-sufficiency claim is register conjecture C9 (25%), whose one measured instance is negative at the emitted level (E9-C20).
- **CITATIONS:** none external (no reduction exists to cite).
- **FEEDS:** WP-22 (as labelled open question only), WP-12

### E9-C12
- **STATUS:** Conjecture linkage record (register numbers verbatim; the fence claim of this extraction)
- **SOURCE:** blade-forge-spec (v3 document register note 2026-06-10 + §12); register rows C1 to C10
- **CLAIM:** The forge document's conjecture table resolves to the live register per its own 2026-06-10 register note, and the register wording governs (GR-1): C5 (~3,000x ZKP reduction) is resolved-strengthened; C6 (the 96/64 edge-vertex ratio matching the superlinear exponent is structural) 35%, convergent; C7 (three-axis separation is multiplicative) 30%, the V6 falsification frontier, owned at E1-C16; C8 (compression reduces the reconstruction bound R_max; the compression-ratio figure of the source is GR-3-fenced and not repeated here) 45%, active; C9 (holographic boundary sufficiency) 25%, active, with the E9-C20 negative instance; C10 (O(1) shared-parent modifies the network exponent) 20%, active. The document's known deltas are carried: its Existence-Leak references read C81; CM-C47 promoted to C85; C67 to C71 are the Horizon set. No document-local number is citable in place of the register row.
- **CITATIONS:** none external (register hygiene claim).
- **FEEDS:** WP-22 (fence), WP-12 (fence)

### E9-C13
- **STATUS:** Conjecture-C87 (register confidence ~50%; architectural claim, no circuit exists)
- **SOURCE:** spec §15.7; v6-draft Part V §V.2; register Band VIII
- **CLAIM:** The Key Accumulates (C87): the City Key trust recursion admits an IVC (incrementally verifiable computation) realisation in which the Key is a succinct accumulator of domain proofs, verifiable in time independent of loop count. The mapping as specified: the Key = the folded instance (accumulator); each domain's trust task = a step circuit; the Charge trace = the folding step; carrying the deepened key back to the first domain = the IVC recursion; the fixed point V63 = the invariant the accumulated proof attests. Honest grade carried verbatim: "this is an architectural claim, not a proof; the deviation hash chain and the Key wire format have no circuit realization yet, and ~50% prices the mapping, not an implementation". Deployment status: the deployed object is the E9-C05 hash chain; nothing folds. Cross-reference: E7-C30 holds C87's holospace-side reading and defers the folding literature to this extraction (discharged at E9-C14).
- **CITATIONS:** folding literature at E9-C14 (the register row's named home).
- **FEEDS:** WP-22 (as labelled open question only)

### E9-C14
- **STATUS:** Design-assumption (citation-family identification; all citations externally resolvable)
- **SOURCE:** spec §15.7; v6-draft Part V §V.2 (the folding-citations carriers)
- **CLAIM:** The folding-scheme literature the canon names as C87's home, exactly: Nova (Kothapalli, Setty, Tzialla); HyperNova (CRYPTO 2024, "with the zero-knowledge completion and the NovaBlindFold update of 2026-02-20"); MicroNova (IEEE S&P 2025, efficient on-chain verification); LatticeFold (Boneh and Chen, ASIACRYPT 2025). The canon's stated reason LatticeFold matters twice: it is both a folding advance and plausibly post-quantum, so a lattice-based proving substrate would let the recursion's attestations age gracefully under the horizon that C67 and C49 plan against (the migration-planning laws themselves are owned at E1-C31 and the E2 temporal thread). No folding scheme is implemented anywhere in the corpus (L008); the family is cited as the design's literature home, not as evidence of capability.
- **CITATIONS:** Nova (CRYPTO 2022, ePrint 2021/370); HyperNova (CRYPTO 2024, ePrint 2023/573); MicroNova (IEEE S&P 2025); LatticeFold (Boneh-Chen, ASIACRYPT 2025, ePrint 2024/257); NovaBlindFold update 2026-02-20 as carried in canon (external resolution to be confirmed at the WP-22 A4 station).
- **FEEDS:** WP-22

### E9-C15
- **STATUS:** Empirical-external (dated-strength record: 2026-06-02 note, Stage 1, n = 1)
- **SOURCE:** schrottenloher-note (full), with the Run-0 erratum applied (its local candidate number reads C81)
- **CLAIM:** The reconstruction record at its dated strength: Schrottenloher (Inria Rennes, single-authored, arXiv:2606.02235, 2026-06-01/02) reconstructs in the open, with runnable code, the ECDLP point-addition circuits whose gate and qubit counts Babbush et al. (arXiv:2603.28846) had attested by zero-knowledge proof without disclosure roughly three months earlier. Reconstructed strength: about 1.5% more qubits and 6.5 to 10% fewer Toffoli gates on the point-addition circuit than the withheld benchmark. The engine: a two-pass split of the extended Euclidean algorithm (a plain Euclidean stage records branch choices as a packed garbage bit-vector; a separate Bezout reconstruction replays those bits), folding modular inversion and an in-place multiplication into one structure with space cost ~4.36n qubits at the reconstruction step; a second instance-specific gain from secp256k1's pseudo-Mersenne prime (2^256 minus 2^32 minus 977), which turns reduction into erase-the-top-bit plus small additions. Trajectory as tabulated at the note's date (full Shor on secp256k1, space-optimised, LOGICAL counts): Litinski 2023 ~2,400 qubits / 2^27.57 Toffoli; Babbush et al. 2026: 1,191 / 2^26.27; Schrottenloher 2026: 1,208 / 2^26.11. The note's honest framing carried verbatim: fault-tolerant execution still demands millions of physical qubits; "Z is decremented, not collapsed". Citation discipline for the same author's prior line: Chevignard-Fouque-Schrottenloher is CRYPTO 2025, not 2024 (the L070(3) sweep correction; any E9 consumer citing the CFS qubit-reduction paper carries that venue). The episode's verified-record framing, primary attribution, and metric discipline are owned at E2-C07; this claim is the substrate-level detail at the note's dated strength.
- **CITATIONS:** arXiv:2606.02235 / ePrint 2026/1128 (the reconstruction); arXiv:2603.28846 / ePrint 2026/625 (the withheld-result primary record); Litinski 2023 (arXiv:2306.08585) for the prior benchmark; Chevignard, Fouque, Schrottenloher, CRYPTO 2025 (venue per L070(3)) when the prior qubit-reduction line is cited.
- **FEEDS:** WP-22, WP-12

### E9-C16
- **STATUS:** Design-assumption (architectural corollary of C81; the law itself is owned at E2-C08)
- **SOURCE:** schrottenloher-note (the disclosure fork and corollary)
- **CLAIM:** The witness-existence asymmetry, the substrate reading of the existence-leak law: a zero-knowledge proof cannot hide a coordinate it is constructed to certify, and ZK-as-disclosure-control therefore behaves differently for capability claims than for instance claims. The withheld-methods proof hid a witness that still existed (the circuit), and a witness that exists under a published existence claim is reconstructible from that claim as a seed (demonstrated within one quarter, E9-C15). By contrast, structural context erasure hides the witness because the witness is gone: zero-memory is stronger than zero-knowledge for exactly this reason, since there is nothing left to reconstruct (the erasure grades and the archive-term claim are owned at E1-C06/E1-C12 and E2-C11). Scope fence carried from the register: the law concerns capability attestations; instance attestations (e.g. a transaction proof) are out of scope. This claim supplies WP-22's central design distinction: what a proving substrate can withhold (method) versus what it constitutionally cannot (feasibility).
- **CITATIONS:** Garg, Jain and Sahai (leakage-resilient ZK impossibility) ride with E2-C08; the instance record is E9-C15/E2-C07.
- **FEEDS:** WP-22, WP-12

### E9-C17
- **STATUS:** Design-assumption (role assignment at the proof-medium layer; the register-held generalisation is C53, ~70%, shared register)
- **SOURCE:** aletheia-lethe-note (DOCS copy, post-reseat)
- **CLAIM:** The proving-role pairing: the corpus assigns the two halves of one zero-knowledge architecture to the complement pair of lattice seats 38 and 25 (exact bitwise complements; arithmetic owned at E1-C28). Seat 38 (Protection, Connection, Computation active) carries the transmission-medium role: the non-interactive proof transform, identified in-source with Fiat-Shamir (the oracle that answers without speaking; carries yes/no without carrying which). Seat 25 (Delegation, Memory, Value active) carries the holding-substrate role: witness-unretrievability as covenant (witnesses held by their irretrievability; the forgetting is the proof). Equal stratum (both Hamming weight 3) is read as the algebraic signature that the medium and the substrate are peers, neither reducible to the other; the pair occupies at the proof-medium layer the same involution relationship (bnot) that the agent layer assigns to the boundary and delegation agents. Register status: the generalisation "every bnot-pair on the lattice has a mythological reading" is C53 (~70%, occupied, never reassign); the phi-adjacency of the pair's disclosure ratios is C54, owned at E1-C29. Deployment status: interpretive design reading; the only deployed correlates are the E9-C01 primitives. Mythological names stay upstream (GR-4).
- **CITATIONS:** Fiat and Shamir 1986 (protocol identification only).
- **FEEDS:** WP-22

### E9-C18
- **STATUS:** Empirical-external (external arena record; frontier snapshot flagged unsynced in source)
- **SOURCE:** shor-mage-record (frontier.json DS-1; methodology_draft §0 to §2; case study)
- **CLAIM:** The one place the corpus records a LIVE proving substrate in production use is external: the ecdsa.fail arena (operated under Eigen Labs; Layr Labs is the GitHub organisation name, per the L070(3) sweep). Its substrate facts: score = peak qubits x average-executed Toffoli; the held-out gate is 9,024 Fiat-Shamir witnesses hashed from the candidate's own operation stream and reseeded per candidate, so the proposer structurally cannot tune to them; the arena adopted the published ZK verifier of the withheld-result episode as its automatic scoring filter (the verified-record framing of that reuse is owned at E2-C07). Frontier snapshot at 2026-06-30 as pinned in the source's single-source-of-truth file: best score 1,571,592,960 = 1,364,230 (average-executed Toffoli, stated to two decimal places in source) x 1,152 (peak qubits); the file's own `synced: false` flag is carried, so the figure is citable only as the dated snapshot, not as current. Published baselines in the same file: best published single-add ~2.7e9 (about 1.72x worse than the live island score, with the source's caveat that low published numbers use approximate, non-density-neutral arithmetic); honest density-neutral floor 3.0e9 to 3.2e9. Attribution fence per the standing record: the arena, the vendored circuit toolchains, and the SOTA circuit are OTHERS' work; nothing in this claim is the programme's contribution.
- **CITATIONS:** the ecdsa.fail challenge repository and leaderboard (external, resolvable); frontier.json as the dated on-disk snapshot.
- **FEEDS:** WP-22, WP-12

### E9-C19
- **STATUS:** Design-assumption (one built instance, run once on CPU; NO validated score improvement; the generative claim is gated and UNRUN)
- **SOURCE:** shor-mage-record (methodology_draft CTR-2, CTR-4, §6 to §8; claims_register CR-1 to CR-11; case study; harness header)
- **CLAIM:** The proving-method instance: the dual-agent harness (design owned at E1-C38) was run against the ecdsa.fail arena, transposing the arena's held-out Fiat-Shamir gate into the architecture's non-collusion precondition: because the 9,024 witnesses are hashed from the proposer's own operation stream, the proposer is structurally denied the witness derivation, which realises I(Y_S; Y_M | X) = 0 at workflow level (the identity is spec §10.5 Precondition 1; the source's register attribution of it is drifted, see E9-C21). What the run produced, attribution split per claim: (a) OTHERS' work: the measured circuit is the community's vendored SOTA, reproduced (0/0/0 at the E9-C18 frontier score), never improved, never credited to the programme. (b) The programme's method layer, run: the referee killed all eight proposed levers cheaply on CPU (the typed kill discipline, ~92% source confidence, CR-1, accepted); the cheap analytical pre-filter (CR-5, ~90%, accepted); the three-axis exhaustion measurement (every single-move frontier lever measured dead; a beat requires a coordinated structural package). (c) The programme's method layer, UNRUN: the generative claim that the decomposed architecture finds validated structural cuts a flat agent would not (CR-2, ceiling unknown, gated on an equal-budget two-arm falsification that requires a Linux + NVIDIA GPU surface and has not run). The honest envelope carried verbatim: methodology and negative results, not a frontier advance; no validated score improvement is attributable to the harness.
- **CITATIONS:** RCI (arXiv:2407.07064); SkillOpt (arXiv:2605.23904) as the conceded prior-art mechanisms; the arena as at E9-C18.
- **FEEDS:** WP-22 (as method context, design status verbatim), WP-12

### E9-C20
- **STATUS:** Empirical-external (programme-run measurement on an external vendored circuit; a result AGAINST the model's prediction, filed at full prominence per GR-8)
- **SOURCE:** shor-mage-record (claims_register CR-9; EX-1 probe record; methodology_draft §5)
- **CLAIM:** The one worked instance of register conjecture C9 (holographic boundary sufficiency, 25%) at the proving-substrate level is NEGATIVE at the emitted-circuit level: the disclosure-frontier probe (EX-1, 2026-07-01) ran a global taint pass over the vendored SOTA point-addition circuit and found 8 of 1,446,685 paid AND gates classicalisable (0.0006%), an UPPER bound, and those eight coincide with the constant-propagation pass's already-banked removals. Net exploitable surplus approximately zero; the Toffoli factor of this circuit is irreducible by classicalisation, and the source downgraded its local claim to REFUTED-at-emitted-level (CR-9 closed). Attribution: the measurement is the programme's method layer; the circuit measured is others' vendored work. Register note: the register row C9 stands at 25% pending the register process; this claim records the instance, not a register move (GR-1).
- **CITATIONS:** none external beyond the arena record (the probe is on-disk practice record: EX1_disclosure_frontier_probe.md).
- **FEEDS:** WP-12, WP-22 (as the honesty exhibit for boundary-sufficiency claims)

### E9-C21
- **STATUS:** CONTESTED (source register-drift; register wording governs per GR-1; filed to A0 for the ledger)
- **SOURCE:** shor-mage-record (methodology_draft CTR-2; claims_register register-drift note CH-4; harness header) against register rows C82/C83 and spec §10.5
- **CLAIM:** The shor-mage practice record carries a register drift its own drift-check note (CH-4: "verify against the live register... flag any that moved") asks to be flagged, and this claim is that flag: (a) methodology_draft CTR-2 and the claims-register annotation attribute the non-collusion identity I(Y_S; Y_M | X) = 0 to "C83"; the live register's C83 is Compositional Leakage Amplification (the (2^N - 1)-epsilon versus N-epsilon gap, owned at E1-C08), and the identity is Precondition 1 of spec §10.5, not a numbered conjecture. The harness header, by contrast, carries C83 correctly (compounding under collusion). (b) The same surfaces gloss C82 as "the dual-agent ceiling R(t)", and the harness header states the ratio bound in its pre-L044 static form without the capacity-deficit decomposition; the register's C82 is the drift law (owned at E2-C03), and the decomposition discipline is E2-C01's. Effect on use: no E9 or downstream claim may cite the shor-mage record's register numbers; the substrate facts of E9-C18 to E9-C20 are unaffected because none of them rests on the drifted attributions. Resolution path: the register process or the source repo's own pre-submission drift check; not resolved here.
- **CITATIONS:** none external (register hygiene finding).
- **FEEDS:** WP-22 (as a citation fence), WP-12

### E9-C22
- **STATUS:** Design-assumption (declared regime; first-person declaration binding suite prose)
- **SOURCE:** spec §15.8; v6-draft Part V §V.3
- **CLAIM:** The presence-economy regime declaration bounds what the deployed substrate may claim to prove: presence mana earned from self-attested client-side traces is declared (Gate G3, First Person, 2026-06-10) to be non-transferable, non-attesting local colour: "not proof, not stake-weight, not an input to any admission, coalition, or attestation decision, and no surface in the suite may say otherwise". The named attack surface if it were treated as proof: replay (re-imported traces), simulation (a headless browser walking at machine speed), sybil farming (presence across disposable keys); C42 (stake economics generate Sybil resistance, ~50%) is the same gap from the other side. The named upgrade ladder before presence may ever attest: (2) witness co-signing at gates, then (3) elapsed-time proofs (VDF-style) rate-limiting accrual to wall clock. Deployment status: regime (1) is the deployed truth (an integer in localStorage); the ladder rungs are design only. This is the corpus's cleanest worked example of the L008 discipline applied prospectively: the architecture earns the claim before the prose makes it.
- **CITATIONS:** Boneh, Bonneau, Bunz, Fisch 2018 (verifiable delay functions) for the named rung-3 primitive family.
- **FEEDS:** WP-22

## Contested items

- **E9-C21** tagged CONTESTED: shor-mage practice-record register drift (C83 misattribution of the non-collusion identity; loose C82 gloss; pre-L044 static form in the harness header). Not canon-versus-canon (GR-1 resolves it: the register governs and the source's own drift-check anticipated the flag), so filed as a source-integrity finding, not CANON-LEVEL; proposed ledger entry returned to A0 with this build.
- **Registry gap (not a claim):** the manifest E9 source slug `folding-citations` has no SOURCES.md row (the L113(a) class). Resolved this build to spec §15.7 + v6-draft Part V §V.2; row proposed to A0.
- **L049-class version drift (not a claim):** `zk_swordsman_blade_forge_v3_0.md` self-identifies in body as version 3.2; SPECIFICATION.md self-identifies as version 1.0.1 working draft. Cited here by filename per the registry; the L049 precedent (registry follows the document body) applies if a consumer needs the version.

## Sweep record

- spec §15 (formal spec §15.1 to §15.9): swept 2026-07-10, A1 (this session), full. Extracted: §15.3/§15.4 (E9-C06), §15.7 (E9-C13/E9-C14), §15.8 (E9-C22). Excluded with reasons: §15.1/§15.2 (ceremony cycle, trust ladder: E8/E3 territory), §15.5/§15.6 (phase notation extracted via the SPECIFICATION.md counterpart at E9-C10; tier axes are E3 material), §15.9 (C66 credential-versus-capability: identity inventory, E7's manifest home).
- spec §27 (+ §27.1): swept 2026-07-10, A1, full. No E9 claim minted: C84 and the temporal thread are owned at E2-C09 and the E2 cluster; the HNDL cost backbone (Blanco-Romero et al., arXiv:2603.01091; CSA 2026-05-18) rides with E2-C09's citations. Recorded as swept to close the source list honestly.
- C81-C84 (register Bands VII/VIII): rows read verbatim 2026-07-10 at head C96; wording and confidences carried into the ownership block; C87's row (Band VIII) read for E9-C13. No drift found between spec §15.7 and the register row for C87, nor between spec §27.1 and the register row for C84.
- folding-citations: resolved 2026-07-10 to spec §15.7 and research/privacy_value_v6_draft.md Part V §V.2 (both read in full for the citation family); E7-C30's deferral of the folding literature to this source is discharged (E9-C14). Registry gap flagged (no SOURCES.md row); proposed row: "`folding-citations` — external · the folding-scheme citation family carried at spec §15.7 and v6-draft Part V §V.2: Nova; HyperNova (CRYPTO 2024 + NovaBlindFold 2026-02-20); MicroNova (IEEE S&P 2025); LatticeFold (Boneh-Chen, ASIACRYPT 2025); citations resolve externally, the carriers are canon."
- shor-mage-record: swept 2026-07-10, A1, at the stated depth: methodology_draft.md, claims_register.md, frontier.json, CASE_STUDY_2026-06-30, harness/swordsman_mage_pqc.mjs header in full; KILLED_LEVERS.md and research-notes surveyed via the claims-register rows (per-kill detail is E10/WP-12 working material). Attribution fence applied per claim (E9-C18 to E9-C20). Register drift found and tagged CONTESTED (E9-C21). The case-study convergence observation (the free/paid boundary of the Z/64Z algebra naming the arena's cost law) noted as an unregistered candidate the source itself proposes for the register; NOT extracted per GR-1 (no number covers it; the register process owns candidate intake).
- blade-forge-spec: swept 2026-07-10, A1, full (both documents); forge_circuits/, blades/, uor_mappings/, tests/ inventoried directly (README + .gitkeep only), re-confirming L008. The v3 document's OPERATIONAL header read against the inventory and split per claim (E9-C08/E9-C09). The GR-3-fenced compression figure in its §5 not repeated anywhere in this extraction; C8 carried figure-free (E9-C12).
- aletheia-lethe-note: swept 2026-07-10, A1, full (DOCS copy, post-reseat). E9 extracted the proving-role pairing only (E9-C17); the complement arithmetic and phi-adjacency stay at E1-C28/E1-C29 (no duplication).
- proof-packet-spec: swept 2026-07-10, A1, full including §14 amendments (E9-C03/E9-C04/E9-C07). The built-versus-unbuilt line taken from the spec's own execution-status statements (phases 1 to 9 built; phase 10 interop only remaining).
- kappa-impl: swept 2026-07-10, A1, at survey depth: sigil/index.html read directly (grounding legend, kappaLabel/canonicalJSON/derivePacketProof/packetsDigest code paths, the prior-field lineage note, the tEXt carrier, and the explicitly display-only moving-ceiling reading, which does not enter κ derivation); star/lattice/verify-static taken at the registry description plus the sigil page's shared-canon statement. Deep per-page conformance deliberately left to E11 (its manifest home).
- schrottenloher-note: swept 2026-07-10, A1, full, at dated strength (2026-06-02; Stage 1, n = 1), Run-0 erratum applied (local candidate number reads C81). The C81 law and its register life stay at E2-C08; E9 extracted the substrate detail (E9-C15) and the architectural corollary (E9-C16). CFS venue discipline (CRYPTO 2025, L070(3)) recorded on E9-C15's citations.
