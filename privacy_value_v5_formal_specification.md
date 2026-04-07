# Privacy Value Model V5: Formal Specification

**Version:** 1.3 (V10.0.0 Grimoire aligned)
**Date:** April 7, 2026
**Author:** Mitchell Travers (privacymage)
**Status:** Working paper — peer review invited
**Companion to:** "Privacy is Value: From the Manifold Dragon to the Holographic Bound" (narrative version)
**External Convergence:** UOR Foundation (https://github.com/UOR-Foundation)

---

## Abstract

This document presents the formal mathematical specification of the Privacy Value Model V5 (PVM-V5). The model extends V4 by introducing three-axis separation (agent, data, inference), a holographic bound interpretation resolving the 96/64 correspondence, path integral edge value replacing additive sums, compression-as-defence modifier for reconstruction difficulty, holonic persistence for temporal memory, and guild efficiency for network scaling. V5's output type transitions from manifold-aware scalar to holographic field. The differential form now computes on the boundary manifold. New conjectures C6–C10 are introduced; C4 (96/64 discrepancy) is resolved; peer review recommendation 3.3 (UOR caveat) is superseded. Open questions and falsifiability conditions are explicitly stated.

---

## 1. The Equation

$$V(\pi, t) = P^{1.5} \cdot C \cdot Q \cdot S \cdot e^{-\lambda t} \cdot (1 + A_h(\tau)) \cdot \left(1 + \sum_i w_i \frac{n_i}{N_0}\right)^k \cdot G(\text{guilds}) \cdot R(d, \text{compression}) \cdot M(u, y) \cdot \Phi_{\text{agent}}(\Sigma) \cdot \Phi_{\text{data}}(\Delta) \cdot \Phi_{\text{inference}}(\Gamma) \cdot T_\int(\pi)$$

where $\pi$ denotes a path through the sovereignty lattice, $t$ denotes time since data generation, and the subscripts denote V5 modifications to prior terms.

**Differential form (V5):**

$$\frac{dV}{dt} = \nabla_{\partial M} \cdot J_{\partial M} + S(x) - D(x)$$

where $\partial M$ denotes the 96-edge holographic boundary and $\nabla_{\partial M}$ indicates divergence computed on that boundary.

The model remains **multiplicative**: any term collapsing to zero eliminates total value.

---

## 2. Inherited Terms (V1–V4)

These terms are carried forward with minor modifications noted.

| Symbol | Name | Domain | Description | V5 Change |
|--------|------|--------|-------------|-----------|
| $P$ | Privacy Strength | $[0, 1]$ | Cryptographic enforcement quality. Exponent 1.5 now connected to holographic ratio 96/64 (C6). | C6 connection |
| $C$ | Credential Verifiability | $[0, 1]$ | Independent verification without revealing underlying information. | None |
| $Q$ | Data Quality | $[0, 1]$ | Accuracy, completeness, fitness for purpose. | None |
| $S$ | Scope / Sensitivity | $\mathbb{R}^+$ | Domain-specific sensitivity multiplier. | None |
| $e^{-\lambda t}$ | Temporal Decay | $(0, 1]$ | Exponential freshness decay with rate $\lambda > 0$. | None |
| $M(u, y)$ | Market Maturity | $[0, 1]$ | Function of user sophistication and market year. | None |

---

## 2.5 UOR Algebraic Foundation (V5.4)

The sovereignty lattice is algebraically equivalent to the ring **Z/(2⁶)Z**. This grounding was confirmed by independent convergence with the UOR Foundation project.

### 2.5.1 Ring Structure

$$\mathcal{L} = (\mathbb{Z}/64\mathbb{Z}, +, \times)$$

Properties:
- **64 elements** (blade addresses 0-63)
- **Addition and multiplication** modulo 64
- **Five canonical operations** (hammer strikes)
- **Dihedral symmetry** D₆₄ (order 128)

### 2.5.2 The Five Hammer Strikes

| Operation | Formula | Category | Forge Meaning |
|-----------|---------|----------|---------------|
| neg(x) | (64-x) mod 64 | Unary involution | Counter-blow (inverts quality) |
| bnot(x) | 63 - x | Unary involution | Antipodal jump (mirror blade) |
| xor(x,y) | x ⊕ y | Binary symmetric | Toggle edges (dimension flip) |
| and(x,y) | x ∧ y | Binary contracting | Toward null blade (constrain) |
| or(x,y) | x ∨ y | Binary expanding | Toward full sovereignty (expand) |

### 2.5.3 Critical Identity

$$\text{neg}(\text{bnot}(x)) = \text{succ}(x) \quad \forall x \in \mathcal{L}$$

**Proof:** For all x ∈ {0,...,63}:
- bnot(x) = 63 - x
- neg(63 - x) = (64 - (63 - x)) mod 64 = (x + 1) mod 64 = succ(x) ∎

**Significance:** The successor function is not primitive — it emerges from the composition of two involutions. *"Deny the complement, and you advance."*

### 2.5.4 Triadic Coordinates

Every blade has three independent coordinates:

$$\text{blade}(x) = (\delta(x), \sigma(x), s(x))$$

| Coordinate | Symbol | Definition | Domain |
|------------|--------|------------|--------|
| datum | δ(x) | Raw value x | {0,...,63} |
| stratum | σ(x) | popcount(x) = Hamming weight | {0,1,2,3,4,5,6} |
| spectrum | s(x) | Six-bit decomposition [b₀,b₁,b₂,b₃,b₄,b₅] | {0,1}⁶ |

**Convergence with existing system:**
- datum = blade ID in the sovereignty lattice
- stratum = layer in Pascal's triangle (C(6,σ) distribution)
- spectrum = six sovereignty dimensions (d₁ Protection, d₂ Delegation, d₃ Memory, d₄ Connection, d₅ Computation, d₆ Value)

### 2.5.5 Dihedral Group D₆₄

The two involutions (neg, bnot) generate the dihedral group:

$$D_{64} = \langle \text{neg}, \text{bnot} \mid \text{neg}^2 = \text{bnot}^2 = 1, (\text{neg} \circ \text{bnot})^{64} = 1 \rangle$$

Order: |D₆₄| = 128

**Significance:** All valid blade transitions are D₆₄ group actions. Zero knowledge arises because multiple group elements (different forging paths) can map to the same blade — same statement, infinite witnesses.

### 2.5.6 External Convergence

The UOR Foundation (https://github.com/UOR-Foundation) independently developed this algebraic structure for universal object referencing:

| Project | Starting Point | Arrived At |
|---------|---------------|------------|
| agentprivacy | Privacy geometry → 64-tetrahedra | Z/(2⁶)Z |
| UOR Foundation | Content addressing → Universal references | Z/(2⁶)Z |

This independent arrival strengthens C6 (P^1.5 ↔ 96/64) and provides external validation that the 64-element structure is not arbitrary but emerges from the requirements of six-dimensional sovereignty.

**Implementation:** See `swordsman-blade/src/lib/uor.ts` for the explicit UOR module with all five operations and identity verification.

---

## 3. Modified Term: Holonic Temporal Memory — $A_h(\tau)$

### 3.1 V4 to V5 Change

V4's temporal memory assumed infrastructure-bound derivation chains. V5 adds holonic persistence: derivation chains anchored to GUIDs that survive infrastructure changes.

### 3.2 Definition

$$\text{Temporal}(t, \tau) = e^{-\lambda t} \cdot (1 + A_h(\tau))$$

$$A_h(\tau) = \alpha \cdot \ln(1 + |\tau|) \cdot h(\tau) \cdot p(\tau)$$

| Symbol | Definition | Domain |
|--------|-----------|--------|
| $\tau$ | Derivation chain: ordered sequence of state transitions | Finite sequence |
| $\lvert\tau\rvert$ | Length of derivation chain | $\mathbb{N}_0$ |
| $h(\tau)$ | Integrity fraction: proportion with valid ZK proofs | $[0, 1]$ |
| $p(\tau)$ | **Persistence independence**: fraction surviving single-provider failure | $[0, 1]$ |
| $\alpha$ | Scaling coefficient | $\mathbb{R}^+$ |

### 3.3 Properties

- **V4 reduction**: $p(\tau) = 1 \Rightarrow A_h(\tau) = A(\tau)$ (V4 form)
- **Infrastructure dependency**: $p(\tau) = 0$ (all history on one provider) $\Rightarrow A_h(\tau) = 0$
- **Holonic persistence**: When $p(\tau) > 0$, history accumulates value even across provider changes
- **Infinite horizon**: The $\int_0^\infty$ integral now has meaning — holonically persistent history can, in principle, survive indefinitely

### 3.4 GUID Structure

A holon is identified by a content-addressed GUID independent of storage location:

$$\text{GUID}(\tau) = \text{hash}(\text{content}(\tau))$$

The GUID persists across:
- Provider migration
- Storage format changes
- Infrastructure failures (if replicated)

---

## 4. New Term: Three-Axis Separation

### 4.1 V4 to V5 Change

V4 measured separation as a single 4×4 matrix $\Sigma$ over four forces (Protect, Project, Reflect, Connect). V5 recognises that separation operates on three orthogonal architectural axes.

### 4.2 Definition

$$\Phi_{v5} = \Phi_{\text{agent}}(\Sigma) \cdot \Phi_{\text{data}}(\Delta) \cdot \Phi_{\text{inference}}(\Gamma)$$

#### 4.2.1 Agent-Layer Separation

$$\Phi_{\text{agent}}(\Sigma) = \min\!\left(1.0,\; \frac{S/M}{\varphi}\right) \cdot \det(\Sigma)$$

This is V4's duality term unchanged. It measures Swordsman-Mage separation and the volume of the four-force tetrahedron.

#### 4.2.2 Data-Layer Separation

$$\Phi_{\text{data}}(\Delta) = 1 - \frac{1}{|\text{providers}(\Delta)|}$$

| Symbol | Definition | Domain |
|--------|-----------|--------|
| $\Delta$ | Data distribution descriptor | Set of providers |
| $\lvert\text{providers}(\Delta)\rvert$ | Number of independent storage providers | $\mathbb{N}^+$ |

Properties:
- Single provider: $\Phi_{\text{data}} = 0$ (collapses total value)
- Two providers: $\Phi_{\text{data}} = 0.5$
- Many providers: $\Phi_{\text{data}} \to 1$

#### 4.2.3 Inference-Layer Separation

$$\Phi_{\text{inference}}(\Gamma) = \text{separation}(\text{Generator}, \text{Solver})$$

| Symbol | Definition | Domain |
|--------|-----------|--------|
| $\Gamma$ | Inference architecture descriptor | — |
| Generator | Model that produces reasoning graphs | Agent |
| Solver | Model that executes reasoning graphs | Agent |

Properties:
- Same model for both: $\Phi_{\text{inference}} = 0$
- Separate models, shared weights: $\Phi_{\text{inference}} \in (0, 1)$
- Independent models: $\Phi_{\text{inference}} \to 1$

### 4.3 Multiplicativity

The three-axis product is multiplicative:

$$\Phi_{v5} = \Phi_{\text{agent}} \cdot \Phi_{\text{data}} \cdot \Phi_{\text{inference}}$$

**Consequence**: Collapse on any single axis collapses total separation value. This explains empirical observations that:
- Good agent separation with centralised data (Φ_data → 0) fails to preserve privacy
- Good data distribution with unified inference (Φ_inference → 0) fails to preserve privacy
- All three axes must be addressed simultaneously

### 4.4 Conjecture C7

**C7**: Three-axis separation is correctly modelled as multiplicative (vs. additive, minimum, or other aggregations).

Status: Supported by Act 24 analysis; requires empirical confirmation across diverse architectures.

---

## 5. Modified Term: Reconstruction Difficulty — $R(d, \text{compression})$

### 5.1 V4 to V5 Change

V4's reconstruction difficulty measured architectural resistance to adversarial reconstruction. V5 adds a compression modifier based on BRAID's demonstration that inference compression reduces attack surface.

### 5.2 Definition

$$R(d, \text{compression}) = R_{\text{base}}(d) \cdot \left(1 - \frac{1}{\text{compression\_ratio}}\right)$$

| Symbol | Definition | Domain |
|--------|-----------|--------|
| $R_{\text{base}}(d)$ | V4 reconstruction difficulty | $(0, 1)$ |
| compression_ratio | Token reduction ratio (e.g., 74× for BRAID) | $\mathbb{R}^+ > 1$ |

### 5.3 Properties

- **No compression** (ratio = 1): Factor becomes 0, multiplying to reduce R. This is conservative — uncompressed inference has maximal attack surface.
- **High compression** (ratio → ∞): Factor approaches 1, preserving $R_{\text{base}}$
- **BRAID typical** (ratio = 74): Factor ≈ 0.986

### 5.4 Conjecture C8

**C8**: BRAID-style compression reduces R_max in practice.

Status: Theoretically grounded (fewer tokens = smaller reconstruction surface); requires formal proof connecting compression ratio to information-theoretic bounds.

---

## 6. New Term: Guild Efficiency — $G(\text{guilds})$

### 6.1 Motivation

V4's network term assumed O(N²) coordination cost — each agent potentially interacting with every other. BRAID's shared-parent pattern demonstrates that agents sharing a reasoning library coordinate at O(1) cost per guild member.

### 6.2 Definition

$$\text{Network}_{v5}(G) = \left(1 + \sum_{i=0}^{6} w_i \cdot \frac{n_i}{N_0}\right)^k \cdot G(\text{guilds})$$

$$G(\text{guilds}) = 1 + \text{guild\_efficiency}$$

| Symbol | Definition | Domain |
|--------|-----------|--------|
| guild_efficiency | Fraction of network operating through shared-parent structures | $[0, 1]$ |

### 6.3 Properties

- **No guilds**: $G = 1$ (reduces to V4)
- **Full guild coverage**: $G = 2$ (doubles network effect)
- **Scaling**: Guild members coordinate at O(1) rather than O(N²)

### 6.4 Conjecture C10

**C10**: O(1) shared-parent coordination modifies the effective network exponent k.

Status: Structurally implied by BRAID architecture; requires calibration against empirical guild performance data.

---

## 7. Modified Term: Path Integral Edge Value — $T_\int(\pi)$

### 7.1 V4 to V5 Change

V4's edge value was an additive sum over edges, assuming independence:

$$T_{v4}(\pi) = 1 + \beta \sum_{e \in \pi} f(e) \cdot g(n_e)$$

V5 replaces this with a path integral that captures edge correlations:

$$T_\int(\pi) = 1 + \beta \int_\pi F(\gamma) \, d\gamma$$

### 7.2 Definition

| Symbol | Definition | Domain |
|--------|-----------|--------|
| $\pi$ | Path through sovereignty lattice | Continuous or discrete path |
| $\gamma$ | Path parameter | $[0, 1]$ |
| $F(\gamma)$ | Path density function | $\mathbb{R}^+$ |

The density function $F(\gamma)$ captures:
- **Verification checkpoints**: Some edges gate later traversal
- **Feedback loops**: Revisiting vertices with changed meaning
- **Non-local correlations**: Early choices affecting later value

### 7.3 Properties

- **V4 reduction**: When edges are independent, $\int_\pi F(\gamma) d\gamma = \sum_{e \in \pi} f(e) \cdot g(n_e)$
- **BRAID graphs**: Structured reasoning graphs naturally express as correlated paths
- **Generator-Solver split**: Generator proposes path; Solver executes; integral measures actual traversal

### 7.4 Conjecture Status Update

**C3** (V4: edge value additivity): **Challenged**. The path integral form better captures observed structure in BRAID reasoning graphs. The additive form is retained as a special case for uncorrelated paths.

---

## 8. The Holographic Bound

### 8.1 Resolution of C4

V4 flagged the 96 vs 64 discrepancy as an open question (C4): the UOR torus has 96 edges while the lattice has 64 vertices. This is now resolved.

**Resolution**: The 96-edge surface IS the holographic encoding of the 64-vertex bulk. In holographic physics, a boundary of dimension n encodes a volume of dimension n+1. The 96/64 ratio is not a discrepancy — it is the holographic principle expressing itself in discrete lattice geometry.

### 8.2 Implications

1. **Boundary computation**: The differential form $dV/dt = \nabla_{\partial M} \cdot J_{\partial M} + S(x) - D(x)$ now computes on the 96-edge boundary, not the 64-vertex bulk.

2. **Privacy value flows along edges**: Value lives on the boundary, not in the interior. This aligns with V4's insight that meaning lives in transitions.

3. **Boundary sufficiency**: Privacy can be computed entirely from boundary observations. The bulk is encoded by the surface.

### 8.3 Conjecture C6

**C6**: The ratio 96/64 = 1.5 is structurally connected to P^1.5 (the superlinear privacy exponent).

Status: Numerically coincident; no derivation from first principles. If true, the entire equation is an expression of the holographic principle applied to sovereignty architecture.

### 8.4 Conjecture C9

**C9**: The holographic boundary is sufficient for privacy value computation (boundary sufficiency).

Status: Implied by the holographic principle; requires discrete lattice verification.

### 8.5 UOR Caveat Update

V4 Peer Review Recommendation 3.3 (add UOR caveat to §8.2) is **no longer needed**. The holographic bound interpretation grounds the manifold structure independently of UOR's specific algebraic claims. UOR correspondence is now explained BY the holographic bound, not dependent on it.

### 8.6 Algebraic Confirmation (V5.4)

The holographic bound is now confirmed from both geometric and algebraic directions:

| Approach | Framework | Result |
|----------|-----------|--------|
| **Geometric** | 64-Tetrahedra lattice | 96 edges encode 64 vertices (torus surface/bulk) |
| **Algebraic** | Z/(2⁶)Z ring theory | 64 elements; 96 edges emerge from adjacency structure |

The UOR Foundation's independent derivation of the same 64-element structure provides external validation. The ratio 96/64 = 1.5 = P^1.5 is no longer numerically coincident — it emerges from the fundamental structure of six-dimensional sovereignty.

**Conjecture C6 Status:** UPGRADED from Speculative to **CONVERGENT**

The critical identity neg(bnot(x)) = succ(x) provides the algebraic mechanism: progression through the sovereignty lattice requires denying the complement. This is not metaphor — it is the group-theoretic structure of D₆₄ acting on Z/(2⁶)Z.

---

## 9. Differential Form

### 9.1 V5 Specification

$$\frac{dV}{dt} = \nabla_{\partial M} \cdot J_{\partial M} + S(x) - D(x)$$

| Symbol | Definition |
|--------|-----------|
| $\partial M$ | 96-edge holographic boundary |
| $\nabla_{\partial M}$ | Divergence on boundary |
| $J_{\partial M}$ | Value current on boundary |
| $S(x)$ | Source term (value generation at position x) |
| $D(x)$ | Dissipation term (value decay at position x) |

### 9.2 Five-Channel Decomposition

The value current decomposes into five channels corresponding to the five V5 modifications:

$$J_{\partial M} = J_{\text{agent}} + J_{\text{data}} + J_{\text{inference}} + J_{\text{compression}} + J_{\text{holonic}}$$

Each channel flows along edges that activate its corresponding separation axis.

---

## 10. Open Questions and Falsifiability

### 10.1 Conjecture Summary

| ID | Claim | V4 Status | V5.4 Status |
|----|-------|-----------|-------------|
| C1 | Golden ratio φ is optimal S/M ratio | Open | Open; BRAID provides empirical pathway |
| C2 | A(τ) should be logarithmic | Open | Strengthened by holonic persistence |
| C3 | Edge value is additive | Open | **Challenged** — path integral replaces |
| C4 | 96 vs 64 UOR discrepancy | Open | **RESOLVED** — holographic principle + algebraic |
| C5 | ~3,000× ZKP reduction | Speculative | Strengthened |
| C6 | P^1.5 ↔ 96/64 = 1.5 | — | **CONVERGENT** (↑ from Speculative) — UOR confirms |
| C7 | Three-axis separation is multiplicative | — | **NEW** — needs empirical confirmation |
| C8 | BRAID compression reduces R_max | — | **NEW** — needs formal proof |
| C9 | Holographic boundary sufficiency | — | **NEW** — needs lattice verification |
| C10 | O(1) shared-parent modifies k | — | **NEW** — needs calibration |
| C11 | Behavioural density ρ amplifies privacy | — | **NEW** (V5.1) — 55% confidence (↑ quantum context) |
| C12 | Hexagram encoding is structurally resonant | — | **ALGEBRAICALLY GROUNDED** — 60% (↑ spectrum = dimensions) |
| C13 | Bilateral Witness is verification primitive | — | **NEW** (V5.1) — 65% confidence (↑ quantum context) |
| C14 | Φ_agent ≅ D₂ₙ (dihedral group isomorphism) | — | **NEW** (V5.2/V5.4) — 75% confidence |
| C15 | T_∫(π) ≅ UOR resolution pipeline | — | **NEW** (V5.2/V5.4) — 65% confidence |
| C16 | Topological trust invariants (Betti numbers) | — | **NEW** (V5.2/V5.4) — Speculative 25% |

### 10.2 Measurement Gaps (Updated)

| ID | Term | V4 Gap | V5 Status |
|----|------|--------|-----------|
| M1 | $\sigma_{ij}$ (separation matrix) | No measurement for emergent forces | Three-axis operationalisation provides pathway; Φ_data and Φ_inference now measurable |
| M2 | $f(e)$ (edge weights) | No empirical data | BRAID provides first edge weight data via reasoning graphs |
| M3 | $\beta, \alpha$ (scaling coefficients) | Need calibration | Unchanged |
| M4 | Aggregation form | det(Σ) alternatives unclear | Three-axis product provides alternative to det(Σ) |

### 10.3 Breaking Conditions (Updated)

The model's core claims weaken or fail if:

1. ~~**UOR incompatibility**~~: **Resolved** — holographic bound explains independently
2. **Three-axis non-multiplicativity**: If agent separation compensates for data centralisation → multiplicative assumption breaks
3. **Compression increases attack surface**: If some compression methods increase rather than decrease reconstructability → compression-as-defence fails
4. **Holonic persistence fundamentally limited**: If content-addressing has inherent infrastructure dependency → persistence term is illusory
5. **Guild coordination scales with membership**: If shared-parent overhead grows with N → guild efficiency overstates network benefit

---

## 11. Structural Properties (Updated)

### 11.1 Multiplicative Gating

Unchanged from V4. Any single term at zero eliminates total value.

### 11.2 Manifold Interpretation (Updated)

V5's manifold interpretation differs from V4:

- **V4**: Value field on 64-vertex bulk with toroidal boundary
- **V5**: Value field computed on 96-edge boundary encoding 64-vertex bulk

The boundary IS the compute surface. The bulk is encoded, not directly measured.

### 11.3 Surveillance Gap as Topology (Updated)

V4's interpretation (accessible manifold volume) is refined:

- **V4**: Surveillance architectures access less manifold volume
- **V5**: Surveillance architectures have constrained boundaries; sovereignty architectures have expressive boundaries

The gap is now understood as boundary expressiveness, not bulk volume.

---

## 12. Version Lineage (Updated V5.4)

| Version | Date | Core Addition | Output Type |
|---------|------|---------------|-------------|
| V1 | 2024 | $P \cdot C \cdot Q \cdot S$ | Static scalar |
| V2 | Oct 2025 | $e^{-\lambda t}$, $(1 + n/N_0)^k$ | Dynamic scalar |
| V3 | Nov 2025 | $R(d)$, $M(u,y)$, $\Phi(S,M)$ | Agent-aware scalar |
| V3.1 | Jan 2026 | $\sigma(\text{⿻})^2$ | Architecture-gated scalar |
| V4 | Feb 2026 | $\Sigma$, $A(\tau)$, $T(\pi)$, $\Phi(\Sigma)$ | Manifold-aware scalar |
| V5 | Feb 2026 | Three-axis Φ, $A_h$, $T_\int$, R(compression), G(guilds), holographic bound | Holographic field |
| **V5.4** | **Mar 2026** | **UOR algebraic foundation, Z/(2⁶)Z, D₆₄, triadic coordinates, C14-C16** | **Algebraically grounded field** |

---

## 13. Notation Summary (Updated V5.4)

| Symbol | Meaning |
|--------|---------|
| $V(\pi, t)$ | Total privacy value for path $\pi$ at time $t$ |
| $P, C, Q, S$ | Privacy strength, credential verifiability, data quality, scope |
| $\lambda$ | Temporal decay rate |
| $\tau$ | Derivation chain (verified state transition history) |
| $A_h(\tau)$ | Holonic temporal memory accumulation |
| $p(\tau)$ | Persistence independence |
| $\Phi_{\text{agent}}$ | Agent-layer separation (Swordsman-Mage) |
| $\Phi_{\text{data}}$ | Data-layer separation (provider fragmentation) |
| $\Phi_{\text{inference}}$ | Inference-layer separation (Generator-Solver) |
| $G(\text{guilds})$ | Guild efficiency factor |
| $R(d, \text{compression})$ | Compression-modified reconstruction difficulty |
| $T_\int(\pi)$ | Path integral edge value (replaces additive $T(\pi)$) |
| $\partial M$ | 96-edge holographic boundary |
| GUID | Content-addressed identifier (holonic) |
| $\mathcal{L}$ | Sovereignty lattice = Z/(2⁶)Z (V5.4) |
| $\delta(x)$ | Datum — raw blade value (0-63) (V5.4) |
| $\sigma(x)$ | Stratum — Hamming weight / popcount (0-6) (V5.4) |
| $s(x)$ | Spectrum — six-bit decomposition [b₀...b₅] (V5.4) |
| neg, bnot | Unary involutions on $\mathcal{L}$ (V5.4) |
| xor, and, or | Binary operations on $\mathcal{L}$ (V5.4) |
| $D_{64}$ | Dihedral group generated by neg, bnot (order 128) (V5.4) |

---

## 14. Three Identity Layers

V5 formalises three identity layers emerging from the architecture:

| Layer | Identifier | Scope | Persistence |
|-------|-----------|-------|-------------|
| Data | GUID | Content-addressed holon | Infrastructure-independent |
| Relationship | VRC | Bilateral commitment | Relationship-scoped |
| Principal | DID | Sovereign identity | Self-sovereign |

The layers are orthogonal: a single principal (DID) can control multiple relationships (VRCs) across multiple data objects (GUIDs).

---

## References

- Travers, M. (2026). "Privacy is Value: From the Manifold Dragon to the Holographic Bound." *Soul Sync.*
- Travers, M. (2026). "Dual-Agent Privacy Architecture." Research Paper v4.2. *agentprivacy-docs.*
- Travers, M. (2026). "UOR × 64-Tetrahedra × ZK Mapping v2.2." *agentprivacy-docs.*
- Bergstra, J. & Burgess, M. (2019). *Promise Theory: Principles and Applications.*
- Susskind, L. (1995). "The World as a Hologram." *Journal of Mathematical Physics.* Holographic principle foundation.
- BRAID Framework (2026). Bounded Reasoning for Autonomous Inference and Decisions. Compression efficiency data.
- UOR Foundation (2026). "Universal Object Reference." https://github.com/UOR-Foundation — Independent Z/(2⁶)Z ring algebra convergence.

---

## Citation

```
Travers, M. (2026). "Privacy Value Model V5: Formal Specification."
Working paper. https://github.com/mitchuski/agentprivacy-docs
```

---

*This document presents the mathematics only. For narrative context, motivation, and the discovery process, see the companion piece: "Privacy is Value: From the Manifold Dragon to the Holographic Bound."*

*V5 axiom: "The boundary is always enough."*

*Peer review, critique, and falsification attempts are actively invited. Contact: mage@agentprivacy.ai*
