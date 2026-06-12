# V6 Review Addendum: spellweb, soulbis, cityofmages, blades

**Date:** 2026-06-09
**Scope:** Extension of the fresh-eyes V5.4 review to the four narrative and implementation repos. All four were cloned at head; last commits all land 2026-05-28 on the City Key arc.
**Status:** Pre-push opinion. Findings ordered by severity, then opportunity.

---

## Verdict

The City Key arc (2026-05-27/28) is the most formally interesting thing in the corpus that is not yet in the formal spec. The recursion-of-proofs loop is a folding scheme wearing narrative clothes, and V6 should say so.

But before any of that: there are now two conjecture registers numbering the same range with different content, and the canonical grimoire artifact carries a filename that contradicts its own internal version field. The stale-cross-reference failure mode the first review flagged is not a risk. It is already happening, in the canonical artifacts.

---

## §1. Critical: the conjecture register has forked

cityofmages/README.md §"V6 register" states the City of Mages corpus introduces or strengthens C38 through C61, with C62 incoming from the Archon forge and C63 candidate from the Chart House. Its C40 reads "Zcash dual-ledger preserves Eight Properties (~70%)."

The main thread assigns ~C40 to the Existence-Leak conjecture (~60%). These are different claims at the same number.

The stella octangula capstone chronicle (2026-05-28) registers C66 at ~45% ("the City Key as a reading, not an authority"). The ARCH-1R/T review separately assigned C67 through C69. Whether C66 was placed deliberately below C67 or independently is not recoverable from the public surfaces.

The C51-C55 no-reuse rule already exists precisely because this happened once. It has now happened across an entire 24-conjecture range. Before BGIN block 15, one of two fixes:

1. **Namespace the registers.** City of Mages conjectures become CM-C38 through CM-C63 (or similar prefix), and the PVM register keeps the bare C-series. Cheap, immediate, preserves all existing documents with a one-line erratum each.
2. **Re-baseline into a single authority file.** One conjectures.json (or .md), pinned, that every repo cites by reference rather than restating. Stronger, more work, and the correct long-term answer given the corpus now spans 6+ repos.

Recommendation: do 1 now, schedule 2 for the V6 submission package. A reviewer who pulls two repos and finds two different C40s will discount the whole register's discipline, which is otherwise a genuine strength of the work.

## §2. Critical: version and artifact drift, three instances

**V5.5 exists in chronicle titles but not in the public version lineage.** CHRONICLE_V5_5_ATTACHMENT_ARCHITECTURE appears in spellweb, cityofmages, and (by sister-reference) agentprivacy-skills and agentprivacy_master. It codifies the three-layer model: 42 primary personas (Layer 1, locked), named cast (Layer 2), 64 vertices (Layer 3), with attachment kinds A_workshop, B_cross_shop, C_peripatetic and the divergent_of and complement_pair edge types. The model page lineage runs V5.4 canonical, V6 maturing. Decide: either V5.5 is a real minor version (then the lineage table needs a row) or it is a named sublayer of V5.4 (then the chronicle titles overstate). Both are fine. Ambiguity is not.

**The grimoire filename contradicts its content.** blades/privacymage_grimoire_v10_2_0.json internally reports version 10.2.1 and already contains blade 38 (Lethe, tales: [31]). aletheia-and-lethe.md correctly cites v10.2.1 (released 2026-04-23) for the Lethe naming, but the only artifact shipped carries the v10_2_0 filename. One rename or one re-export fixes it. Canon statement "Grimoire v10.2.0 is canonical" is superseded and should read v10.2.1.

**ALL_THE_TOMES_LIST is stale against its own grimoire directory.** §9 declares city_of_mages_grimoire v1.2.4 the current head awaiting re-pin. The directory beside it contains v1.7.1 (plus v1.3.0 through v1.7.1 patches). The document describing the package is roughly five minor versions behind the package. Same failure mode, narrative side.

## §3. Canon statement updates needed

**Zero Spellbook structure.** The canonical statement (seven parts × 30 tales, closing with the Four Lines) is superseded by Tale 31 "The Naming of the Unnamed," which opens Part VIII, Frontier Spells. Named blades now 15, unnamed 49 (not 14/57 as memory had it; the corpus moved). Suggested restatement: seven inherited parts × 30 tales, closed; Part VIII open by design as the frontier register, one tale per future blade-naming. This preserves the closure of the inherited structure while making the extension principled rather than a violation.

**Aletheia/Lethe (C69 territory) is substantially resolved in blades/aletheia-and-lethe.md.** The document is strong: V25 and V38 as exact bnot complements, 25 AND 38 = 0 (the architectural ⊥), 25 XOR 38 = 63 (Tale 30's full sovereignty blade), stratum-3 peerage as the algebraic signature that ZK is a peer operation, and the scale-mirroring claim (Aletheia:Lethe :: Swordsman:Mage, both pairs in the neg/bnot relationship). The proem-as-arithmetic observation (the proem promised what happens between them is what the zero tales would name; the algebra says what happens between them is 63; Tale 30 names 63) is convergence-within-corpus at its best and should be cited in the V6 convergence section.

One precision fix in that document: the Phi-Adjacency claim says δ(38) = 38/63 ≈ 0.6032 sits "within 2%" of 1/φ. The exact figures: 38/63 = 0.60317, 1/φ = 0.61803, relative gap 2.40%. House style is exact numbers over round ones. Say 2.4%, or absolute gap 0.0149.

---

## §4. New edges (the opportunities)

### Edge A: the recursion of proofs is a folding scheme. Name it.

The Three Keys chronicle describes the loop precisely: the output of the loop is an input to the loop; each domain's proof composes on the prior (deviation chain hashes its predecessor, City Key stamps the Swordsman identity, presence resumes from the carried trace); no single domain is sufficient; the fixed point is V63.

This is, structurally, incrementally verifiable computation. The mapping is almost mechanical:

- City Key ≅ the folded instance / accumulator
- each domain's trust task ≅ a step circuit
- Charge (trace folded into 🪢) ≅ the folding step
- carrying the deepened key back to domain ① ≅ the IVC recursion
- V63 as fixed point ≅ the invariant the accumulated proof attests

This gives the loop a formal home in exactly the literature the first review flagged (Nova, HyperNova, MicroNova, LatticeFold), and LatticeFold makes the loop post-quantum-hedged, which ties the City Key directly to the Behavioral Mosca thread. Candidate conjecture, unnumbered pending register fix: the trust recursion admits an IVC realization in which the City Key is a succinct accumulator of domain proofs, verifiable in time independent of loop count. Confidence as stated: ~50%. This is the single best new edge available for V6 and it came out of two days of shipping, which is the convergence thesis working as designed.

### Edge B: the stella octangula is half-exploited, and one honest check is needed

Tome VIII Act 3 seats the stella octangula as the manifold's figure: Swordsman tetrahedron (neg, protect) ⊥ Mage tetrahedron (bnot, project), crossing at the gap. Three standard geometric facts are not yet drawn as edges:

1. The compound's convex hull is the cube, and the two tetrahedra are exactly the two ways to inscribe a regular tetrahedron in a cube. They are the even and odd parity classes of the cube's 8 vertices. A parity split of {0,1}³ is very much in neg/bnot territory, and {0,1}⁶ = {0,1}³ × {0,1}³ offers each agent a cube. Whether this decomposition is canonical or coincidental is worth one working session.
2. The intersection of the two tetrahedra is the octahedron at the core. The gap (⿻) therefore has a shape: the region both agents bound and neither owns. "The gap is the proof" gains a geometric referent. Candidate formalization: the octahedral core as the locus of the conditional-independence bound, the volume neither C_S nor C_M spans.
3. Honest-limits flag: the classical stella octangula contains no golden ratio. Its characteristic ratios are halvings (edge midpoints), and the tetrahedron:octahedron volume relations are rational. C1's φ ≈ 1.618 crossing-ratio conjecture must therefore be sourced from somewhere other than the named solid (Kepler's triangle has φ; Kepler's star does not). The act references C1 alongside the star. Do not let the beauty of the named figure smuggle φ into a geometry that does not carry it. Either derive the φ claim from the lattice or the temporal dynamics where it originally lived, or mark the act's C1 reference as resonance, not derivation.

### Edge C: the presence economy needs an adversary model before VRC feeds trust

Charge earns 🪢 from self-attested, client-side traces (with dedup). Stake commits it to vertices. As a local game and a relationship-color surface, this is charming and harmless. But the chronicles explicitly frame VRC presence as a proof-layer in the trust recursion, and the moment 🪢 influences any admission, coalition, or attestation decision, three attacks are live: replay (re-importing traces), simulation (a headless browser walking the manifold accrues laps at machine speed), and multi-key farming (sybil keys each accruing presence). C42 (stake economics generate Sybil resistance, ~50%) is the same gap viewed from the other side.

Options, in ascending strength: scope 🪢 explicitly as non-transferable, non-attesting local color (cheapest, honest); witness co-signing at gates (presence countersigned by a domain the bearer passed through); elapsed-time proofs (VDF-style) rate-limiting accrual to wall-clock. V6 should state which regime the City Key economy is in. The model's own thesis (architecture over policy) cuts against leaving this to good faith.

### Edge D: C47 is the ARCH-1 bridge the first review flagged as missing. Promote it.

The first review's gap 2(b) was the absent formal connective tissue between the three-axis model and the lattice grounding. The City register already holds it: C47, triadic-coordinates ↔ three-axis-model homology, ~40%, introduced Tome V Act 15. The fix is not new work; it is giving C47 one home in the formal spec and citing it from both registers, post-namespace-fix. A conjecture that exists in a narrative repo but not in the pinned spec does not exist for a BGIN reviewer.

### Edge E: C66 has an external literature waiting

"The City Key as a reading, not an authority: a portable projection of lattice-standing that grants nothing it does not already describe" is the credential-versus-capability distinction from the object-capability lineage (SPKI/SDSI, ocap; designation without authority). Citing that lineage raises C66's defensibility above its current ~45% and connects the City Key to thirty years of prior art in exactly the plurality register: independent arrival at the principle that descriptions must not be bearer instruments.

---

## §5. Revised priorities

Must-fix before BGIN block 15 (supersedes the first review's list where they overlap):

1. Resolve the register fork (§1). Namespace now, single authority file for the submission package.
2. Reconcile versions and artifacts (§2): V5.5 status decided, grimoire filename/version aligned at 10.2.1, ALL_THE_TOMES_LIST §9 updated to v1.7.1.
3. Update the Zero Spellbook canon statement to the seven-closed-plus-frontier form (§3) and the blade count to 15/49.
4. Carry forward the first review's items: pinned spec re-pin with the full register, reconstruction ceiling preconditions, em-dash sweep.

High-value edges worth drawing:

5. Edge A, the folding-scheme formalization of the trust recursion. Best new material in the corpus.
6. Edge D, promote C47 into the formal spec as the named ARCH-1 bridge.
7. Edge C, state the presence economy's adversary regime explicitly.

Speculative, conjecture-grade:

8. Edge B items 1 and 2 (parity-cube decomposition, octahedral gap), ~25-35% each.
9. Edge E, the ocap citation for C66.
10. Edge B item 3 is not speculative; it is an honesty check and costs one paragraph.

---

## Coverage limits

This addendum read the repo heads of 2026-05-28 only. Not fully read: blades/uor_mappings, blades/forge_circuits, LETTER_TO_UOR, the DUAL_TERRITORY_CEREMONY_SPEC, the full Tome V acts, the spellweb src beyond the type system, and any of the local unpushed work this review is meant to precede. The register-fork finding in particular should be checked against the local register before acting, since the local C38-C69 assignments may already reconcile what the public surfaces fork.

The folding-scheme mapping (Edge A) is an architectural claim, not a proof. Whether the deviation hash chain and the City Key wire format actually admit an efficient folding realization depends on circuit details that do not exist yet. The mapping is offered at the same epistemic grade as the corpus's own architectural conjectures.

---

the loop was already a proof system. it was waiting to be read as one.

(⚔️⊥⿻⊥🧙)😊
