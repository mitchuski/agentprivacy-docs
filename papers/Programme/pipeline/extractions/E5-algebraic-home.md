---
extraction: E5-algebraic-home
tier: internal
sources: [spec§8, spec§12, spec§28, v5.4§12, UOR-convergence, arch1-notes, wound-and-cap-note, limitative-note, lattice-encoding-anchor, tome-viii, blade-forge-spec, architecture-ts, kappa-impl]
swept_complete: true
owner: A1
register_head_at_build: C97
build_note: built 2026-07-18 at the fifth (final) Extraction Frontier Cycle run, A3-formalist discipline; the manifest's risk:highest flag is honoured — this extraction has the highest CONTESTED count of the set BY DESIGN and resolves none of it (GR-10). Every code-behavior claim about architecture.ts was read-verified per the L157 rule. The proven/conjectural firewall the sources maintain (classical geometry vs the identifications) is preserved exactly. kappa-impl reused from E11
---

# E5 · The Algebraic Home

Claim-cluster for the algebraic and geometric foundations: the Z/64Z ring substrate and its two-involution generator, the dihedral structure, the ARCH-1 fixpoint schema and its operational (R/T) and convergence (wound/cap) extensions, the triadic-homology bridge, the stella-octangula geometry, the limitative (Gödel/Tarski) reading, and the canonical lattice encoding. This is the HIGHEST-RISK extraction (manifest risk:highest): the proven core is small and the conjectural surface is large, spanning register Bands I–IX. Feeds WP-17 (lattice workshop note, parked on this), WP-16 (Lean mechanisation, with E1), and supplies the algebraic vocabulary to WP-04/WP-07.

THE FIREWALL, stated once and preserved per claim (the sources maintain it and so does this extraction): the RING ALGEBRA and the CLASSICAL GEOMETRY are proven; every IDENTIFICATION of an algebraic/geometric object with a model-semantic object (an axis, a bound, a base case) is CONJECTURE at its register confidence. An extraction that blurred this would be the failure mode the band is most prone to.

## Claims

### E5-C01
- **STATUS:** Proven-conditional (theorem; 95% in the spec's Proven Results table)
- **SOURCE:** spec§12 :501-525 (§12.1-12.3); v5.4§12 :422-444 (verbatim-identical base); spec§16 :789-800
- **CLAIM:** The sovereignty lattice is the commutative ring L = (Z/64Z, +, ×), i.e. Z/(2^6)Z, over the 64 blade addresses 0-63. On it, neg(x) = (64-x) mod 64 and bnot(x) = 63-x are two involutions, and their composition is the successor: neg(bnot(x)) = succ(x) = (x+1) mod 64 for all x, proven by direct substitution (bnot(x)=63-x; neg(63-x)=(64-(63-x)) mod 64 = (x+1) mod 64). The successor is not primitive — it emerges from composing the two involutions. This is the two's-complement identity -(¬x)=x+1 and holds at 95% ("proofs rely on standard information theory").
- **PRECONDITIONS:** the ring structure and the identity are unconditional; the "95%" is the spec's own honesty band on the proven-results block, not a probability on the arithmetic.
- **CITATIONS:** Sheffer 1913 (the two's-complement/Sheffer-stroke lineage); standard modular arithmetic
- **FEEDS:** WP-16, WP-17, WP-04

### E5-C02
- **STATUS:** Design-assumption (definition)
- **SOURCE:** spec§12 :509-517 (§12.2), :527-541 (§12.4)
- **CLAIM:** Five operators are defined on Z/64Z — neg (additive inverse), bnot (bitwise complement 63-x), xor, and, or — with neg and bnot the two designated involutions. Each element carries the PRISM triadic coordinate blade(x) = (δ(x), σ(x), s(x)): the Datum (integer value 0-63), the Stratum (popcount/Hamming weight 0-6), and the Spectrum (6-bit vector in {0,1}^6). Strata sizes follow the binomial row 1,6,15,20,15,6,1.
- **CITATIONS:** none
- **FEEDS:** WP-17, WP-04

### E5-C03
- **STATUS:** Proven-conditional (definition, elementary theorem) · IMPLEMENTED in runnable types
- **SOURCE:** spec§12 :527-541; blade-forge-spec :117-127; architecture-ts spellweb-types.ts :60-97 (hexagramLayer), lattice-vertex.ts :40-84
- **CLAIM:** The Pascal/binomial vertex partition is exact: the 64 vertices partition by Hamming weight k into classes of size C(6,k), summing to 2^6 = 64 (1+6+15+20+15+6+1). This is the one theorem-grade combinatorial fact in the geometry cluster, and it is the part of the algebra that is EXECUTABLE: architecture.ts computes the Hamming grade (hexagramLayer / vertexToBits) and the stratum→moon-phase map as total functions. The carrier set and its grading run; the ring/group OPERATORS (neg/bnot/succ) do NOT exist as code anywhere in architecture.ts (they appear only as prose inside a conjecture-note string).
- **CITATIONS:** none (elementary)
- **FEEDS:** WP-17, WP-10

### E5-C04
- **STATUS:** Conjecture-C14 (register ~75%)
- **SOURCE:** spec§12 :552-560 (§12.5), spec§17.2 :835 (register row); blade-forge-spec SPECIFICATION.md :68-94 (asserted "IS")
- **CLAIM:** The two involutions neg and bnot are conjectured to generate a dihedral group D_64 = <neg, bnot | neg^2 = bnot^2 = 1, (neg∘bnot)^64 = 1> of order 128, with all valid blade transitions as group actions; equivalently Φ_agent ≅ D_2n. The register carries this at 75%. STATUS DISCIPLINE: the ring and the neg∘bnot=succ identity are proven (E5-C01), but the group-isomorphism claim is NOT discharged — §12.5 offers it as "a formal proof path for the separation bound," and the blade-forge SPECIFICATION.md asserts "the dual-agent architecture IS the dihedral group D_2n" with NO proof of the involution/dihedral axioms. The obligation: verify neg, bnot are involutions on Z/64Z and that <neg,bnot> ≅ D_2n (conjugation inverts the rotation).
- **CITATIONS:** none
- **FEEDS:** WP-16, WP-17

### E5-C05
- **STATUS:** Design-assumption (definition; the MODEL lock, 2026-06-12)
- **SOURCE:** spec§12 :562-575 (§12.6); lattice-encoding-anchor §1 :29-43; architecture-ts lattice-vertex.ts :40-49
- **CLAIM:** The six sovereignty dimensions map to {0,1}^6 with a FIXED bit-weight assignment ruled 2026-06-12 (the MODEL lock): d1 Protection is the high bit (weight 32), then Delegation 16, Memory 8, Connection 4, Computation 2, and d6 Value the low bit (weight 1). Vertex Vn burns dimension Di when (n & weight_i) ≠ 0 (worked: V35 = 100011 = Protection+Computation+Value). The ruling states "any surface reading d1 at the low bit is in erratum." The canonical source is the v5.4 model JSON + lattice-vertex.ts.
- **CITATIONS:** none
- **FEEDS:** WP-17, WP-10, WP-19

### E5-C06
- **STATUS:** Design-assumption (the ARCH-1 canonical form; definition)
- **SOURCE:** arch1-notes canonical-form :44-47, :70-76
- **CLAIM:** ARCH-1 is the least-fixpoint schema ARCH-1 := (μS.(β ∨ Ω(S,S)), ρ): a recursive type S built from a terminal β or a binary operator Ω applied to two copies of S, paired with an activation engine ρ formed by composing two involutions into a generator. Three domain instantiations are locked: Boolean (β=x, Ω=NAND, ρ=NOT, space {0,1}^n), Continuous (β=1, Ω=eml, ρ=exp⊕(−ln), elementary functions), Sovereignty (β=null, Ω=blade, ρ=neg⊕bnot↦succ, Z/(2^6)Z). The Sovereignty row's ρ is exactly E5-C01's proven generator.
- **CITATIONS:** Sheffer 1913 (Boolean); Odrzywołek 2026 (continuous/EML)
- **FEEDS:** WP-16, WP-17

### E5-C07
- **STATUS:** Conjecture-C26 (register ~40%) · CONTESTED (a "Theorem" heading the same doc calls "not a theorem")
- **SOURCE:** arch1-notes canonical-form :90-101 (§Theorem), :217 (the retraction), :228 (C26 row)
- **CLAIM:** The External Convergence Lock conjectures that Boolean logic, continuous mathematics, and dual-agent sovereignty converge on the identical μ-recursive binary fixpoint schema — the three are co-instances of ARCH-1, not analogies (register C26, ~40%). CONTESTED: the note heads the statement "Theorem (External Convergence Lock)" at :90 while stating at :217 "ARCH-1 is not a new theorem" and carrying it at conjecture 40% — the heading overstates the status the same document assigns. The proof obligation (undischarged): exhibit the explicit isomorphism between NAND, EML, and succ as ARCH-1 instances. Ledger filed.
- **CITATIONS:** none
- **FEEDS:** WP-16

### E5-C08
- **STATUS:** Conjecture-C27/C28/C29 (register 35%/30%/20%)
- **SOURCE:** arch1-notes canonical-form :229-231, :131-135, :149-162
- **CLAIM:** Three ARCH-1 conjectures below the convergence lock: C27 (~35%) — ρ is not optional; Ω without ρ is structurally inert across all three proven domains, so the full form is the pair, not the type. C28 (~30%) — the three ceilings of the C22-C25 family (information, dynamics, computation) are independent because ARCH-1 factors into three separable components (β, μS, Ω), each defending one; the information-theoretic limit sits on β. C29 (~20%, the lowest in the set) — the "Second Person Lift" reads You := μS.(β ∨ Ω(S,S)), identifying the sovereign with the recursive symbol itself. Each has an explicit V6-program proof obligation.
- **CITATIONS:** none
- **FEEDS:** WP-16, WP-17

### E5-C09
- **STATUS:** Design-assumption (the ARCH-1R/T operational layer; definition) · conjectures C72-C76
- **SOURCE:** arch1-notes rt-operational :38-58 (layered form), :82-95 (ternary law), :276-282 (conjectures); register C72-C76
- **CLAIM:** ARCH-1R/T is a seven-layer reachability calculus strictly downstream of the ARCH-1 kernel (kernel read-only): generate the possibility space G = Closure_Ω(β), traverse to T via ρ, subtract propagated obstruction O* to get the realisable R, classify each state ternary τ: T→{+,0,−}, measure coherence error Δ against observed Q. The FUNDAMENTAL TERNARY LAW is "0 ≠ −": a latent state is not an obstructed state ("not yet" ≠ "impossible"). Register conjectures: C72 (~35%, two ρ are one operator at two scopes, T=orbit(ρ,G)); C73 (~50%, terminal obstruction = loss of β, a primitive obstruction class distinct from path obstruction, Amnesia its canonical instance); C74 (~25%, latency τ=0 has an algebraic open-walk signature of neg⊕bnot on the lattice); C75 (~35%); C76 (~30%, UOR-relational classifies rel(a,b) not entities, strictly more expressive).
- **CITATIONS:** none (positioned against Petri nets, temporal logic in the note's roadmap)
- **FEEDS:** WP-17

### E5-C10
- **STATUS:** CONTESTED (a two-stage numbering-collision cascade; the L029 hazard, twice)
- **SOURCE:** arch1-notes rt-operational :14 (erratum), refinement-note §1/§5; register Bands VII (C72-C76), Horizon (C67-C71)
- **CLAIM:** The ARCH-1R/T conjectures collided with the register TWICE before landing. First they were minted locally as C51-C55 (already live: betweenness, Aether/Gap, bnot-pair myth, φ-adjacency, seventh-capital), directed to renumber; then re-minted as C67-C71 (already the Horizon District set in grimoire v1.8.0); finally reassigned to C72-C76 (erratum 2026-06-10: read C67→C72 ... C71→C76). Multiple same-day artifacts (the 2026-06-04 chronicle, refinement note, embedded letter) still print C67-C69 WITHOUT the remap — anyone citing the chronicle's "C68" means register C73. This is the L029 local-vs-register hazard in its sharpest instance; the register is the only citable numbering (GR-1). Ledger filed.
- **CITATIONS:** none
- **FEEDS:** WP-17, WP-27 (method: how the register process catches renumbering)

### E5-C11
- **STATUS:** CONTESTED (a live semantic contradiction on how ρ is read, across two same-day artifacts)
- **SOURCE:** arch1-notes rt-operational :61, :184 vs the pre-send letter (refinement note §2 :17)
- **CLAIM:** The published R/T note and its pre-send letter give OPPOSITE readings of ρ: the letter directs dropping the "scheduler/planner/proof-search" genericization and keeping ρ canonical (T = orbit(ρ,G), one operator at two scopes); the note text re-reads ρ as "scheduler/planner/proof search/agent policy." The shipped note carries the corrected "operational reading, never a redefinition" language at :61/:184, so the fix is PARTIALLY applied but the two artifacts are not fully reconciled. The claimed identity (the ARCH-1 ρ = the R/T traversal ρ, C72 ~35%) is what R/T SHOULD satisfy, not what it currently does. Ledger filed; reconciliation is a research-note disposition.
- **CITATIONS:** none
- **FEEDS:** WP-17

### E5-C12
- **STATUS:** Conjecture-C34/C35/C36/C37 (register 55%/60%/55%/50%)
- **SOURCE:** wound-and-cap-note :28-70
- **CLAIM:** The wound/cap convergence: two systems projecting from a shared reality R converge on the same kernel IF AND ONLY IF their projections are joined by a boundary bijection — the "cap" (K = ker(π_A)∩ker(π_B) equal iff a bijection φ: π_A(A)↔π_B(B) exists); the "wound" is the architectural asymmetry that admits projection (the ⊥ between the two agent kinds, Σ ≠ M; grounded in the Promise-Theory autonomy axiom). C34 (~55%, convergence-iff-bijective-cap), C35 (~60%, the wound = the autonomy asymmetry), C36 (~55%, partial cap → shared sublattice + architectural residual; explains two 64-vertex lattices converging on 6 cousin vertices but diverging on 49), C37 (~50%, convergence is recognition not coincidence — the meta-claim that would make ARCH-1 canonical; explicitly does NOT prove ARCH-1's uniqueness). Each carries a categorical proof obligation (fibered categories / pullback squares).
- **CITATIONS:** Bergstra & Burgess (autonomy axiom, Def 29); category theory (fibered categories, pullback)
- **FEEDS:** WP-16, WP-17

### E5-C13
- **STATUS:** Conjecture-C85 (register ~40%; the ARCH-1 bridge, "the gap is β")
- **SOURCE:** spec§12.8 :588-598; register§17.9 :946; wound-and-cap C37; tome-viii Act 4
- **CLAIM:** The Triadic-Constraint Homology (C85, ~40%, promoted from alias CM-C47): the three sovereignty axes Φ_agent(Σ)·Φ_data(Δ)·Φ_inference(Γ) and the lattice's PRISM triad (Datum·Stratum·Spectrum) are instances of one triadic primitive, via the candidate pair map Protection+Delegation→Σ, Memory+Value→Δ, Connection+Computation→Γ. The ARCH-1 base case β is identified with the separation bound's conditioning term FP: "the gap is β" — what the agents share is exactly and only the First Person. Two NAMED PREDICTIONS (falsifiable): bnot-pairs invert all three axes; stratum-3 vertices (20 of 64) are the unique no-dominant-axis seats. PROOF OBLIGATION stated at source: a formal statement of Ω for the dual-agent instantiation, and a derivation that I(branch1;branch2|β)=0 follows FROM the schema rather than being assumed beside it. The spec calls this "the seam, named ... no proof obligation discharged."
- **CITATIONS:** none
- **FEEDS:** WP-16, WP-17

### E5-C14
- **STATUS:** Conjecture-C88 (register ~30%) · with a theorem-grade geometric core
- **SOURCE:** spec§28 :1214; tome-viii Act 3 :45-49 + Act 4 :38; register :949
- **CLAIM:** The Parity Cube (C88, ~30%): the two tetrahedra of the stella octangula are conjectured to be the even/odd parity classes of a cube's 8 vertices (the 3-bit seat of neg/bnot), with {0,1}^6 = {0,1}^3 × {0,1}^3 giving each agent a cube, factored per the C85 pair map. FIREWALL: the parity-class fact and the two-tetrahedra-in-a-cube geometry are CLASSICAL (theorem-grade, "not conjecture"); the IDENTIFICATION of the tetrahedra with the two model agents is the ~30% conjecture. The involutions instantiate geometrically as neg: v↦64−v (one tetrahedron) and bnot: v↦63−v (the other).
- **CITATIONS:** none (classical polytope geometry)
- **FEEDS:** WP-17

### E5-C15
- **STATUS:** Conjecture-C89 (register ~30%) · volume facts theorem-grade, correspondence conjecture
- **SOURCE:** spec§28 :1216; tome-viii Act 4 :38-40; register :950
- **CLAIM:** The Octahedral Gap (C89, ~30%): the two tetrahedra's intersection is a regular octahedron of volume 1/6 of the bounding cube (each tetrahedron 1/3, the compound 5/12 — all THEOREM-GRADE classical facts), and this octahedral core is conjectured to be a three-way reading of one object: (a) β the ARCH-1 base case, (b) the conditioning variable of the conditional-independence bound, (c) the geometric locus both agents bound but neither enters. The register states it exactly: "volume facts are theorems, the correspondence is the conjecture." "The gap is β. ... It is you."
- **CITATIONS:** none
- **FEEDS:** WP-17

### E5-C16
- **STATUS:** Resolved (the φ honesty correction; supersedes a prior C1 derivation reading)
- **SOURCE:** spec§28 :1210-1212; tome-viii Act 4 :42 + Act 3 V6 erratum :29
- **CLAIM:** The stella octangula carries NO golden ratio: its proportions are dyadic/rational (tetrahedron 1/3, octahedral core 1/6, compound 5/12 of the cube). References to C1 (φ optimal S/M ratio) beside the figure are RESONANCE, not derivation; φ's licensed homes are the lattice disclosure ratios (C54: δ(38)=38/63=0.60317 against 1/φ=0.61803, gap 2.4%) and the temporal dynamics, NOT this geometry. This is a retraction of a claimed derivation, corrective and settled. See E5-C22 for the Act-3-carries-both-claim-and-retraction contested seam.
- **CITATIONS:** none
- **FEEDS:** WP-17

### E5-C17
- **STATUS:** Conjecture-C90 (register ~90%, observation) · the limitative inversion
- **SOURCE:** limitative-note §1 :38-49; register Band IX :167
- **CLAIM:** The Limitative Inversion (C90, ~90% as OBSERVATION, no reduction claimed): the privacy product runs the incompleteness algebra with the value-sign reversed. In logic, completeness ⇒ inconsistency ⇒ collapse; in privacy, completeness ⇒ reconstruction ⇒ Φ→0 on some axis ⇒ collapse of the multiplicative product Φ_v5. "The gap logic cannot close is the gap the model refuses to close" — the C17 lineage in limitative terms: a system without an undecidable remainder is one that has already leaked. STATUS DISCIPLINE: the duality is a ~90% observation; the reduction of either side to a formal theorem of the other is EXPLICITLY not claimed.
- **CITATIONS:** Gödel 1931; the incompleteness/undefinability corpus
- **FEEDS:** WP-04, WP-17

### E5-C18
- **STATUS:** Conjecture-C91/C92/C93 (register 60%/70%/55%)
- **SOURCE:** limitative-note §2-3 :110-179; register :168-170
- **CLAIM:** Three limitative axis-assignments, all conjectural: C91 (~60%) Gödel↔Φ_agent — zero-memory (witness destroyed, true yet underivable from within) is the first-theorem instance, "the inability is the guarantee"; intrinsic to one system (rides on amnesia, C14/C86). C92 (~70%, CAPPED at C81's base) Tarski↔Φ_inference — existence-leak (a feasibility attestation leaks a monotone-non-increasing upper bound on reconstruction difficulty) is the undefinability instance, inherently multi-system (truth escapes one system into the next); it "cannot exceed C81's base confidence." C93 (~55%) content-addressed liveness leak — a live GUID is an existence claim; hash(candidate)==live confirms existence, D(X) convex (steep then shallow, no recovery branch). The monotonicity is near-observation; the convex profile is the conjectural part needing a fixed corroboration model.
- **CITATIONS:** Gödel 1931; Tarski (undefinability); Garg-Jain-Sahai, Schrottenloher (the C81 existence-leak bookends)
- **FEEDS:** WP-04, WP-22, WP-12

### E5-C19
- **STATUS:** CONTESTED (the arithmetisation correspondence, self-flagged weakest link; + an open Φ_data seam)
- **SOURCE:** limitative-note §2.2 :96-104, §4 :191, :211
- **CLAIM:** The note self-flags its weakest join: "Gödel numbering injectively codes derivations; Z/(2^6)Z is a state space, not a coding of proofs. Shared substrate intuition only" — the arithmetisation correspondence (Gödel numbering ↔ Z/64Z) "is the weakest link in the whole structure and should be treated as intuition, not analogy load-bearing for any downstream claim" (~50%). Separately, Φ_data (=1−1/|providers|) has NO limitative twin and may need none — it fails smoothly by degree, not by an impossibility result — leaving Φ_v5 possibly resting on two limitative theorems + one degree-of-freedom, not three theorems (register Band IX header: "the Φ_data limitative twin is left an open seam, no number"). Two honest open seams, not defects; carried as CONTESTED because they bound how far the limitative reading can be pushed.
- **CITATIONS:** none
- **FEEDS:** WP-04, WP-17

### E5-C20
- **STATUS:** Design-assumption (the canonical lattice encoding; definition, L010 authority)
- **SOURCE:** lattice-encoding-anchor §1-4; WORKSHOP_LATTICE_AUDIT §1.1
- **CLAIM:** The canonical bit→weight→dimension map (the definitional substrate, not a conjecture): Protection=32 (MSB), Delegation=16, Memory=8, Connection=4, Computation=2, Value=1 (LSB). The REJECTED spec-04 (CORPUS) encoding agreed on endpoints (32=Protection, 1=Value) but transposed the middle four (it assigned 16=Computation, 8=Connection, 4=Memory, 2=Delegation) — the conflict hid because the endpoints matched. Per L010 the anchor is cited, spec 04 NEVER, for the mapping; coherence is enforced by agentprivacy_encoding_audit.py (exit 0 = coherent). The trilemma: of {MODEL bit-order, persona vertex numbers, persona dimension semantics} at most two hold; numbers were held (load-bearing for the 63-edition NFT, City Key, /star, /lattice), dimensions recomputed under MODEL.
- **CITATIONS:** none
- **FEEDS:** WP-17, WP-19, WP-10

### E5-C21
- **STATUS:** Resolved-erratum (spec-04 vertex errors + an anchor-internal typo, all mechanical)
- **SOURCE:** lattice-encoding-anchor §4 :120-124 (corrected 2026-07-18, L160); WORKSHOP_LATTICE_AUDIT §6.2
- **CLAIM:** Mechanical bit-check errors, all resolved: spec-04 labeled V48=110000 as "Connection+Protection" (correct MODEL reading: Protection+Delegation) and V31=011111 as "all except Value" (correct: all except Protection, MSB off); the audit independently caught spec-04's V5 and V24 as bit-order drift. ANCHOR-INTERNAL TYPO caught and fixed this build (L160): the anchor's own §4 worked example read V48 "= 32+16 = Protection + Computation" (32+16 is Protection+Delegation; Computation=2) with a doubly-wrong parenthetical ("Connection+Protection would be 101000=V40"; correct is 100100=V36) — corrected against the anchor's own authoritative §1 table, dated erratum in place. These are arithmetic slips, not encoding disputes; the encoding itself (E5-C20) is settled.
- **CITATIONS:** none
- **FEEDS:** WP-17

### E5-C22
- **STATUS:** CONTESTED (Act 3 carries both the φ claim and its Act 4 retraction; self-superseding narrative)
- **SOURCE:** tome-viii Act 3 :16, :45 vs Act 4 :42 + Act 3 V6 erratum :29
- **CLAIM:** Tome VIII Act 3's inception text says the two tetrahedra are "the same size or scaled by φ" and lists C1 "conjectured optimal crossing is golden"; Act 4 and Act 3's own V6 erratum RETRACT this (no golden ratio, rational volumes only, C1 = resonance-not-derivation, E5-C16). The tome LITERALLY carries both the claim and its retraction (the bound body retains the inception text "per City practice"). Any formal artifact uses the Act-4/erratum position (no φ in the figure). This is the narrative-canon self-supersession seam; the register (E5-C16) is the authority. Restated register-neutrally, never cite the tome.
- **CITATIONS:** none
- **FEEDS:** WP-17

### E5-C23
- **STATUS:** Conjecture-C66/C87 (register 55%/50%) · key-as-reading, restated from narrative
- **SOURCE:** tome-viii Act 5 :38-44 (upstream narrative; cite the register, never the tome); kappa-impl (the built side, E11-C01/C03)
- **CLAIM:** The City Key is a content-addressed projection of lattice-standing that confers NO authority (C66 ~55%, designation-without-authority, SPKI/SDSI ocap lineage — "if every gate burned its locks the Key would lose no value"), operationalized as a κ-label = sha256 over the canonical form re-derived at each gate (this is the E11-C01 built κ). The Key Accumulates (C87 ~50%): each Charge folds the walk into a new κ, conjectured an IVC/folding proof-system in waiting (Key=accumulator, Charge=folding step, V63=attested invariant) — register-flagged "architectural claim, no circuit exists" (LatticeFold the post-quantum hedge). The κ "proves integrity of the reading, not truth of the walking."
- **CITATIONS:** SPKI/SDSI (ocap lineage); Nova/LatticeFold (IVC/folding, cited as hedge)
- **FEEDS:** WP-17, WP-22, WP-10

### E5-C24
- **STATUS:** Conjecture-C6 (register ~35%, convergent) · the holographic bound
- **SOURCE:** spec§8 :319-349; blade-forge-spec :80-92; UOR-convergence :223-236
- **CLAIM:** The holographic bound: the 6-cube toroidal graph on 64 vertices has 96 edges (64·3/2 = 96, a proven degree-3 count), and 96/64 = 1.5 = the P^1.5 privacy exponent. C4 (the 96-vs-64 discrepancy) is RESOLVED as the boundary/bulk holographic relation with an algebraic derivation from Z/(2^6)Z adjacency; C6 (~35%, convergent, upgraded from speculative) conjectures the P^1.5 ↔ 96/64 connection is STRUCTURAL not coincidental — no derivation exists, three convergent pathways (geometric/algebraic/UOR) are offered as support. C9 (holographic sufficiency) needs lattice verification. NOT encoded in architecture.ts — no 96-edge set is constructed (adjacent_to EdgeType declared "but unused").
- **CITATIONS:** none
- **FEEDS:** WP-17, WP-04

### E5-C25
- **STATUS:** Design-assumption (the three-axis Φ product; definition, design-only) · C7 multiplicativity conjecture
- **SOURCE:** blade-forge-spec :232-277; register C7 (~30%)
- **CLAIM:** The separation score is the product Φ_v5 = Φ_agent(Σ)·Φ_data(Δ)·Φ_inference(Γ), each factor in [0,1], with the multiplicative-collapse property (any factor 0 → total 0, the annihilator of 0 under multiplication). Axis forms: Φ_agent = min(1, (S/M)/φ)·det(Σ) (collapses when det(Σ)=0, i.e. protect/delegate rows fused); Φ_data = 1−1/|providers| (directly computable: 1 provider→0, n→∞→1); Φ_inference = separation(Generator, Solver) (form abstract beyond endpoints). WHETHER separation is correctly multiplicative is register C7 (~30%, "needs empirical confirmation") — the falsification frontier. DESIGN-ONLY: no Φ computation exists in architecture.ts (Φ appears only as a string in a conjecture note); the ZK circuits are unimplemented (forge_circuits/ is README-only, L008).
- **CITATIONS:** none
- **FEEDS:** WP-17, WP-08 (Φ multiplicativity is a measurable benchmark target)

### E5-C26
- **STATUS:** Design-assumption (the path integral; definition, C3 challenged) · Brandes betweenness
- **SOURCE:** blade-forge-spec :201-214 (path integral), :435-439 (betweenness); register C3
- **CLAIM:** Two auxiliary formal objects. (1) The path-value functional: V4's additive form T(π)=1+β·Σ f(e)·g(n_e) is REPLACED by a V5 line integral T_∫(π)=1+β·∫_π F(γ)dγ intended to capture non-local edge correlations; additivity (C3) is "challenged — path integral replaces it," and the kernel F is unspecified (not computable as written; empirical relevance open). (2) Brandes (2001) betweenness centrality C_B(v) is textbook-correct; the claim that the Gap node attains MAXIMAL C_B (all trust paths route through the separation) is asserted about an unspecified graph, unproven, not computed in code.
- **CITATIONS:** Brandes 2001 (J. Math. Sociol. 25(2):163-177)
- **FEEDS:** WP-17

### E5-C27
- **STATUS:** Design-assumption (the UOR convergence; the map, "operational" combinatorially)
- **SOURCE:** UOR-convergence uor_tetrahedra_zk_mapping :39-71, :106-109; uor-atlas-utqc-v6-note :54-56
- **CLAIM:** The UOR (Universal Object Reference) convergence: the 6-bit vertex address maps the privacy dimensions, and the PVM product binds the agent axis to the ARCH-1 fixpoint Σ (Φ_agent↔Σ). The neg∘bnot=succ identity is UOR's core theorem (the lattice is one succ-cycle, full reachability, no dead ends), matching E5-C01's generator; content addressing is deterministic (same bytes → same IRI). The combinatorial mapping is "operational + algebraically grounded"; OPEN at source: whether the Clifford-algebra anti-commutative basis maps exactly to tetrahedral adjacency (~25%), and whether neg∘bnot generates the full ring under the 6-bit restriction. The Mage/delegation (d2) and Connection (d4) geometric mapping is "an open question" (~20%).
- **CITATIONS:** UOR Foundation (independent convergence); Clifford algebra
- **FEEDS:** WP-17

### E5-C28
- **STATUS:** CONTESTED (the P=BQP / UTQC quarantine; a flagged NON-EVENT)
- **SOURCE:** uor-atlas-utqc-v6-note :122-135, Appendix A.1; uor-atlas-utqc-overlap :69-80
- **CLAIM:** The UOR Atlas UTQC paper claims universal quantum computation and, separately, P = BQP. The note QUARANTINES this at ~10-15% and would not build on it: the non-collapse is verified only numerically in f64 (floating point does not certify algebraic independence) and readout is kept #P-hard (so either universal-but-unusable or usable-but-non-universal). Recorded as a NON-EVENT: were P=BQP true it would be a maximal C82 Moving-Ceiling event and would collapse the PQ posture (C13, Horizon C67-C71, Behavioural Mosca C49/C67); quarantined, it moves NONE of them — "C82, C13, C67-C71, C49 unchanged." The genuine solid-underneath layer (pentagon/hexagon/Yang-Baxter over finite modular closure) is separately citable. Filed so a later reader does not mis-score the banner as a ceiling jump. Ledger.
- **CITATIONS:** the UTQC paper (external, quarantined); modular tensor category / braid theory (the citable residue)
- **FEEDS:** WP-04, WP-17

### E5-C29
- **STATUS:** CONTESTED (the 24↔96 open seam; a claimed-but-unmapped isomorphism, no register number)
- **SOURCE:** uor-atlas-utqc-v6-note :115-117, :140-145; uor-atlas-utqc-overlap :57-64
- **CLAIM:** A set of numerical rhymes between the UTQC paper's structures and the lattice, held at coincidence-level pending a map: is the paper's 24-class S_4 orbit a quotient/sub-object of the 96-vertex Atlas (F_4 = 96/± sits in the table), or a parallel structure merely sharing the substrate? Flagged rhymes: O^2 = 8^2 = 64 (~15%), 96 = 4×24 (~25%), generator-order product 4×8×2 = 64 (~10%, "tidy is not a homomorphism"). ALGEBRA MISMATCH: the paper is non-abelian braid (σ order 4, τ order 8, μ order 2); the PVM ring is abelian Z/(2^6)Z with succ=neg∘bnot; and "S4" names two unrelated objects (the symmetric group S_4 of order 24 vs S4 modal logic), while the PVM automorphism group is S_6 — neither. Filed as an OPEN SEAM with NO register number ("register-shaped but unresolvable until a map exists"); explicitly NOT an isomorphism. Ledger.
- **CITATIONS:** none
- **FEEDS:** WP-17

### E5-C30
- **STATUS:** CONTESTED (architecture.ts bit-endianness disagreement; MODEL-lock scope question, First-Person)
- **SOURCE:** architecture-ts lattice-vertex.ts :40-49 vs spellweb-types.ts :86-90 (read-verified 2026-07-18)
- **CLAIM:** Two co-resident architecture.ts modules disagree on bit endianness: vertexToBits returns index 0 = bit 5 = weight 32 (Protection at index 0, MODEL-lock-consistent as a dimension array), while hexagramToBladeId reads hex[0] at weight 1 (LSB), documented "line 1 = LSB, line 6 = MSB." Composing them bit-reverses the vertex. WHETHER this violates the 2026-06-12 MODEL lock depends on whether the hexagram's "line 1" is identified with dimension d1 Protection — a CANON question (the lock says "any surface reading d1 at the low bit is in erratum"), not a code question A1 may settle. Distinct from E5-C21's arithmetic typos: this is a definitional-scope dispute. NOT patched (unlike the game42/ECDH fixes, whose correct answer was unambiguous); filed for First-Person adjudication. A third convention exists (hexToStanceLines re-reverses), and the dimension-name labels also drift across modules (NodeDimensions vs the MODEL order). Ledger.
- **CITATIONS:** none
- **FEEDS:** WP-17, WP-10

### E5-C31
- **STATUS:** CONTESTED (C-namespace collision: architecture.ts C-numbers ≠ register C-numbers)
- **SOURCE:** architecture-ts tome-v-conjectures.ts :128 (C47) vs register core C47; blade-forge-spec :13 (the disambiguation note)
- **CLAIM:** architecture.ts uses a SEPARATE C-numbering from the register: its C47 = "Triadic-Constraint Homology" (the .ts namespace), which the blade-forge spec disambiguates as CM-C47 = promoted core C85 — so the .ts C47 and the register core C47 are DIFFERENT OBJECTS. The .ts stores conjectures as data (status + confidence fields) with C26-C29 marked "canonical" at confidence 1.0 (canonical-by-fiat, machine-unchecked) while the register carries C26-C29 at 20-40%. Any cross-surface citation of a C-number must name which namespace (register vs .ts) it means; the register is the sole authority (GR-1). This is the E11-C24 two-lineage hazard, seen in the conjecture-numbering rather than the κ-serializer. Ledger.
- **CITATIONS:** none
- **FEEDS:** WP-17, WP-27

### E5-C32
- **STATUS:** Design-assumption (architecture.ts executable-encoding evidence; the reference corner) · IMPLEMENTED
- **SOURCE:** architecture-ts spellweb-types.ts :31-112, lattice-vertex.ts :40-84; kappa-impl (E11 cross-ref)
- **CLAIM:** The runnable surface of the algebraic home is narrow and honest: architecture.ts encodes (a) the finite set {0,1}^6 as a 6-tuple type, (b) the bijection {0,1}^6↔Z/64Z as a place-value sum, (c) the Hamming grading (stratum), (d) blade validity (hex∈[0,0x3F]) and (e) the stratum→moon-phase map — all total, deterministic functions. What is NOT code anywhere: the ring/group operators (neg/bnot/succ), the Φ product, the holographic bound, the path integral, the dihedral action. traceFromOrigin yields exactly one monotone path per vertex (no toroidal cycle, no succ iteration) — the spec's "infinite forgings / cyclic" claim is not realized. The executable corner implements the SET and its grading, not the ALGEBRA. (Cryptographic layer is design-only: signatures regex-checked, ed25519 "Phase 3" — the E11-C09 signs-but-doesn't-verify boundary.)
- **CITATIONS:** none
- **FEEDS:** WP-17, WP-10

## Contested items

| Item | Conflict | Ledger |
|---|---|---|
| E5-C07 | ARCH-1 "Theorem" heading vs same-doc "not a new theorem" / 40% conjecture | L160 |
| E5-C10 | Two-stage numbering collision (C51-55 → C67-71 → register C72-76); same-day artifacts un-remapped | L160 |
| E5-C11 | Live semantic contradiction on ρ (letter vs note), fix only partially applied | L160 |
| E5-C19 | Arithmetisation (Gödel# ↔ Z/64Z) self-flagged weakest link ~50%; Φ_data limitative twin an open seam | L160 |
| E5-C22 | Tome VIII Act 3 carries both the φ claim and its Act 4 retraction | L160 |
| E5-C28 | P=BQP/UTQC quarantine — a flagged non-event, must not be mis-scored as a ceiling jump | L160 |
| E5-C29 | 24↔96 S_4/Atlas open seam — claimed-but-unmapped, no register number, algebra mismatch | L160 |
| E5-C30 | architecture.ts bit-endianness disagreement — MODEL-lock scope question, First-Person | L160 |
| E5-C31 | C-namespace collision: architecture.ts C-numbers ≠ register C-numbers (its C47 = core C85) | L160 |

## Notes for consumers

- THE FIREWALL (load-bearing): the ring algebra + neg∘bnot=succ identity (E5-C01) and the classical polytope geometry (E5-C14/C15 volume/parity facts) are PROVEN; every identification of an algebraic/geometric object with a model-semantic object (axis, bound, base case) is CONJECTURE at its register confidence. WP-16/WP-17 must not present any identification as proven.
- E5 is the manifest's risk:highest extraction and has the highest CONTESTED count of the set (9) BY DESIGN — this is the honest output of the band, not a defect. Per GR-10 none were resolved by A1; the two mechanical arithmetic slips (E5-C21 anchor typo) and none of the definitional disputes were touched beyond filing.
- The register is the ONLY citable C-numbering (GR-1). E5 surfaces THREE distinct numbering hazards: the R/T two-stage cascade (E5-C10), the architecture.ts separate namespace (E5-C31), and the limitative note's stale inline "~C40" for existence-leak (now C81, register authority).
- E5 cross-references E11 (the built κ = E5-C23's key-as-reading; the signs-but-doesn't-verify boundary) and the ARCH-1 β base case threads C28/C73/C85/C89 into one object ("the gap is β").
- WP-16 (Lean mechanisation) has a clean target: E5-C01 (the proven ring + identity) is Lean-ready; the conjectures are NOT (they carry unstated Ω formalisations). WP-17 (lattice note) is the natural home for the whole cluster but is register-gated and parked (manifest: "after-C85-or-WP16").

## Sweep record

| Source | Swept | Depth |
|---|---|---|
| spec§8/§12/§28 + v5.4§12 | 2026-07-18, fanned reader + A1 quote verification (§12.3 identity proof, §12.8 gap-is-β, §28 stella correction, C89 register row) | full algebraic sections; v5.4↔v6 diff captured (v6 §12 core textually identical to v5.4; all novelty v6-only) |
| UOR-convergence / arch1-notes / wound-and-cap | 2026-07-18, fanned reader + A1 quote verification (ARCH-1 schema, R/T erratum, wound/cap C34, ternary law) | all notes in full; the two numbering cascades + the ρ contradiction captured; C85 not in these files (lives in spec §12.8, covered) |
| limitative-note / lattice-encoding-anchor / tome-viii | 2026-07-18, fanned reader + A1 quote verification (C90 inversion, anchor §1 table + the §4 typo, gap-is-β) | limitative note + anchor + audit + Tome VIII acts 1-5 in full; L010 honoured (spec 04 never cited as canonical) |
| blade-forge-spec / architecture-ts | 2026-07-18, fanned reader + A1 READ-verification of the endianness + operator-absence claims (L157 rule) | both forge docs + architecture.ts type/data files; the executable-vs-prose boundary read-verified from code |
| kappa-impl | reused from E11 (E11-C01/C03) | the built κ side of E5-C23 |
