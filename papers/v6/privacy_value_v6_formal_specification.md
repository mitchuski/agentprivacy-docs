# Privacy is Value · V6: The Gathering Turn and the Moving Ceiling

## Formal Specification of the Privacy Value Model · Dual-Agent Privacy Architecture

**Series:** *Privacy is Value*, one book in versioned volumes; each volume stands alone and names its place in the book. This volume succeeds *Privacy is Value · V5.4: The Amnesia Protocol*.
**Version:** 6.0
**Date:** 2026-06-10
**Author:** privacymage (Mitchell · mage@agentprivacy.ai), with Claude Fable 5
**License:** CC BY-SA 4.0
**Lineage:** V1 through V4 (foundation) · V5/V5.4 (holographic bound, three-axis separation, Z/(2⁶)Z algebraic foundation, the Amnesia Protocol) · V5.5 (named sublayer of V5.4: the attachment architecture) · **V6 (this document)**
**Conjecture authority:** `research/CONJECTURE_REGISTER_V6.md` · register head C89 at publication · when this document and the register disagree, the register wins
**Suite labeling (G3 decision):** all canon papers carry the unified V6 label: this formal specification · the compressed Swordsman reading · the companion Mage reading · the research paper · the whitepaper V6 edition. One label, one current state of the model.

**External Convergence:** UOR Foundation (https://github.com/UOR-Foundation)

---

## The Document Suite

This volume cites its siblings by name; this table is what each name is. Every document below lives in the `agentprivacy-docs` repository; the full catalogue with one entry per paper in the corpus is `reference/PAPERS_INDEX.md`.

| Document | What it is | Location |
|---|---|---|
| *Privacy is Value · V6* (this volume) | the formal specification, the authority for the model's current state | `papers/v6/privacy_value_v6_formal_specification.md` |
| The Conjecture Register | the single numbering authority, C1 to C89; reproduced in §17 of this volume; the living file wins over any reproduction | `research/CONJECTURE_REGISTER_V6.md` |
| The Swordsman reading | the compressed specification: equations only, eight pages | `papers/v6/pvm_v6_compressed.md` |
| The Mage reading | the companion guide: what the mathematics means, standards, economics, reading paths | `papers/v6/pvm_v6_companion_guide.md` |
| The crosswalk edition | the V5.4-to-V6 skeleton with CARRIED/REVISED/NEW section markers, kept for readers tracking the delta | `papers/v6/privacy_value_v6.md` |
| The research paper, V6 edition | what changed in the mathematics at V6 plus provenance reconciliation; builds on the v4.3 proof body | `papers/v6/dualprivacy_researchpaper_v6.md` over `papers/lineage/dualprivacy_researchpaper_v4_3.md` |
| The whitepaper, V6 edition | the technical architecture paper: Swordsman and Mage derived from the First Person (body v6.3) | `papers/whitepapers/swordsman_mage_whitepaper_v6_3.md` |
| *Privacy is Value · V5.4: The Amnesia Protocol* | the predecessor volume; its sections are carried or revised here by number | `papers/v5/privacy_value_v5_4_formal_specification.md` |
| The V6 research-note series | the April to June 2026 notes the V6 results grew from (Lorenz, EML, ARCH-1, Bakhta, wound-and-cap, Schrottenloher, Horizon District) | `research/` |
| The working draft | Parts I to V as drafted on the V6 autopath, with full honest-limits sections | `research/privacy_value_v6_draft.md` |
| The model JSONs | the machine-readable model: V6 dark (full) and light (runtime) | `models/privacy_value_model_v6_dark.json` · `_light.json` |
| The grimoires | the narrative corpus this volume's §29 records (privacymage v10.4.0 · City of Mages v1.8.0) | `models/` and the cityofmages repository |

---

## Abstract

V6 is the gathering turn. V5 answered WHAT the architecture is: a dual-agent separation (Swordsman ⚔️ and Mage 🧙) with an information-theoretic boundary, a multiplicative three-axis gate, and an algebraic home on the 64-vertex lattice Z/(2⁶)Z. V6 asks WHO: it opens the model outward, in the second person, to the City of Mages and to every kindred builder, so the equation can be filled with data instead of estimates. That was the plan from the first V6 research notes, and it stands.

In the act of gathering, the research moved. Between April and June 2026 the model's temporal seams became its spine: the reconstruction ceiling proved to be a function of time (R(t), with a shelf life t*), the multi-agent privacy literature proved that policy-separated systems leak exponentially where amnesia-separated systems leak linearly, a withheld result and its zero-knowledge attestation demonstrated the Existence-Leak law in public, the lattice and the three axes finally met in one bridge conjecture, and structural forgetting acquired a mathematical statement strong enough to be the model's best sentence: amnesia is the only term whose security is independent of time.

This document is fully standalone: it adopts the V5.4 specification text wholesale, weaves the V6 revisions through it, and supersedes the V5.4 specification as the head of the lineage. The complete conjecture register, bands I through VIII at head C89, is reproduced in §17; the eight conjectures registered during the V6 runs (C82 to C89) carry the version's results. All confidences are privacymage's estimates as of the stated dates, made in session with the named runtime.

---

## 1. The Equation

### 1.1 Static Form

$$\begin{aligned}
V(\pi, t) = \; & P^{1.5} \cdot C \cdot Q \cdot S \cdot e^{-\lambda t} \cdot (1 + A_h(\tau)) \\
& \cdot \left(1 + \sum_i w_i \frac{n_i}{N_0}\right)^{k} \cdot G(\text{guilds}) \\
& \cdot R(d, \text{compression}, \rho) \cdot M(u, y) \\
& \cdot \Phi_{\text{agent}}(\Sigma) \cdot \Phi_{\text{data}}(\Delta) \cdot \Phi_{\text{inference}}(\Gamma) \cdot T_{\int}(\pi)
\end{aligned}$$

where $\pi$ denotes a path through the sovereignty lattice, and $t$ denotes time since data generation.

**Output type:** Holographic field on the 96-edge boundary ∂M.

### 1.2 Differential Form

$$\frac{dV}{dt} = \nabla_{\partial M} \cdot J_{\partial M} + S(x) - D(x)$$

where $\partial M$ denotes the 96-edge holographic boundary. Privacy is temporal. Consent forms that freeze the frame are the Emissary's privacy, not the First Person's.

### 1.3 Multiplicative Gating

The model is multiplicative: **any single term collapsing to zero eliminates total value.** Privacy strength, credential verifiability, data quality, separation on all three axes, temporal memory, network effects, reconstruction difficulty, market maturity, and path value must ALL be non-zero for privacy to have value. Remove any one and the equation yields zero.

### 1.4 Master Inscription

$$(\text{⚔️} \perp \text{⿻} \perp \text{🧙})\text{😊} = \text{neg} \oplus \text{bnot} \to \text{succ}$$

*"Swordsman and Mage separated, with the Gap between them, preserve the First Person. Negation and complement composed yield the successor."*

**The V6 note:** the equation always carried t in its signature; V6 is the version that takes the t seriously everywhere else (§5, §11, §14, §18).

---

## 2. Inherited Terms (V1–V4)

These terms are carried forward from prior versions.

| Symbol | Name | Domain | Description |
|--------|------|--------|-------------|
| $P$ | Privacy Strength | $[0, 1]$ | Cryptographic enforcement quality. Exponent 1.5 connected to holographic ratio 96/64 (§8). |
| $C$ | Credential Verifiability | $[0, 1]$ | Independent verification without revealing underlying information. Proof of claims without exposure of claims. |
| $Q$ | Data Quality | $[0, 1]$ | Accuracy, completeness, fitness for purpose. Stale data loses value. |
| $S$ | Scope / Sensitivity | $\mathbb{R}^+$ | Domain-specific sensitivity multiplier. Resistance to adversarial extraction. |
| $e^{-\lambda t}$ | Temporal Decay | $(0, 1]$ | Exponential freshness decay with rate $\lambda > 0$. Privacy erodes without active maintenance. |
| $M(u, y)$ | Market Maturity | $[0, 1]$ | Function of user sophistication $u$ and market year $y$. Adoption and yield environment. |

---

## 3. Holonic Temporal Memory · $A_h(\tau)$

### 3.1 Motivation

V4's temporal memory assumed infrastructure-bound derivation chains. V5 adds holonic persistence: derivation chains anchored to GUIDs that survive infrastructure changes.

### 3.2 Definition

$$\text{Temporal}(t, \tau) = e^{-\lambda t} \cdot (1 + A_h(\tau))$$

$$A_h(\tau) = \sum_j p(\tau_j) \cdot w(\tau_j) \cdot e^{-\mu \cdot \text{age}(\tau_j)}$$

| Symbol | Definition | Domain |
|--------|-----------|--------|
| $\tau$ | Derivation chain: ordered sequence of GUID-addressed holons | Finite sequence |
| $\tau_j$ | The $j$-th holon in the chain | · |
| $p(\tau_j)$ | Persistence independence: probability of surviving single-provider failure | $[0, 1]$ |
| $w(\tau_j)$ | Weight: integrity-verified contribution of holon $j$ | $\mathbb{R}^+$ |
| $\mu$ | Memory decay rate (distinct from data decay $\lambda$) | $\mathbb{R}^+$ |
| $\text{age}(\tau_j)$ | Time since holon $j$ was created | $\mathbb{R}^+$ |

**Special case (logarithmic approximation):** When holons are uniformly weighted and persistence is constant, $A_h(\tau) \approx \alpha \cdot \ln(1 + |\tau|) \cdot \bar{p} \cdot \bar{h}$, recovering the V4 logarithmic form.

### 3.3 Properties

- **Infrastructure dependency**: When $p(\tau_j) = 0$ for all holons, $A_h(\tau) = 0$. Total provider concentration collapses temporal memory.
- **Holonic persistence**: When $p(\tau_j) > 0$, history accumulates value across provider changes.
- **Age-weighted decay**: Older holons contribute less via $e^{-\mu \cdot \text{age}}$, but verified old history still carries weight.
- **Infinite horizon**: Holonically persistent history can survive indefinitely. The temporal integral now has meaning over infinite time.

### 3.4 GUID Structure

$$\text{GUID}(\tau) = \text{hash}(\text{content}(\tau))$$

Content-addressed, infrastructure-independent. Persists across provider migration, storage format changes, and infrastructure failures (if replicated).

---

## 4. Three-Axis Separation · $\Phi_{v5}$

### 4.1 Definition

$$\Phi_{v5} = \Phi_{\text{agent}}(\Sigma) \cdot \Phi_{\text{data}}(\Delta) \cdot \Phi_{\text{inference}}(\Gamma)$$

The product is multiplicative. Collapse on any single axis collapses total separation value. Good agent separation with centralised data ($\Phi_{\text{data}} \to 0$) still fails to preserve privacy.

### 4.2 Agent-Layer Separation

$$\Phi_{\text{agent}}(\Sigma) = \min\!\left(1.0,\; \frac{S/M}{\varphi}\right) \cdot \det(\Sigma)$$

Measures Swordsman–Mage separation and the volume of the four-force tetrahedron (Protect, Project, Reflect, Connect). The golden ratio $\varphi = 1.618$ is the conjectured optimal protect/delegate ratio (C1, unproven).

**Algebraic interpretation (V5.2):** Φ_agent is isomorphic to the dihedral group D₂ₙ action on the sovereignty lattice (§12.5). When Φ_agent = 1.0, the two generators (neg, bnot) are maximally independent. When Φ_agent = 0, the group degenerates.

### 4.3 Data-Layer Separation

$$\Phi_{\text{data}}(\Delta) = 1 - \max_j(\text{share}_j)$$

where $\text{share}_j$ is the fraction of the total data held by provider $j$.

| Configuration | $\Phi_{\text{data}}$ |
|---------------|----------------------|
| Single provider (share = 1.0) | 0 (collapses total value) |
| Two equal providers (share = 0.5) | 0.5 |
| Many equal providers (share → 0) | → 1 |
| Unequal distribution | $1 - \max_j(\text{share}_j)$ |

**Note:** This formulation penalises concentration at the dominant provider, not just provider count. A system with 10 providers where one holds 90% scores 0.1, not 0.9.

### 4.4 Inference-Layer Separation

$$\Phi_{\text{inference}}(\Gamma) = 1 - I(\text{model} ; \text{executor})$$

where $I$ denotes mutual information between the model that reasons (Generator) and the model that executes (Solver).

| Configuration | $\Phi_{\text{inference}}$ |
|---------------|--------------------------|
| Same model for both | 0 |
| Separate models, shared weights | $(0, 1)$ |
| Independent models | → 1 |

### 4.5 Conjecture C7

**C7**: Three-axis separation is correctly modelled as multiplicative (vs. additive, minimum, or other aggregations). Confidence: 30%.

### 4.6 The Falsification Frontier (V6)

C7 (three-axis separation is multiplicative, 30%) is load-bearing for the entire Φ_v5 gating form and remains the corpus's most exposed conjecture. V6 names it the **falsification frontier** and states the three boundary cases the multiplicative form does not yet address:

1. **Partial collapse.** One axis at 0.1 rather than 0. The multiplicative form predicts near-total gating; an additive-with-floor or min() form predicts graceful degradation. No measurement distinguishes them yet. Falsification test (inherited from the 2026-06 review and now register-bound): any real deployment exhibiting partial single-axis collapse without proportionate collapse of reconstruction resistance falsifies the multiplicative form.
2. **Axis correlation under composition.** The compounding results of §14.7 imply the axes can become positively correlated under sequential composition: conditioning that flows through an inter-agent channel couples what the model treats as orthogonal. The determinant form det(Σ) partially captures correlation; the scalar product Φ_agent · Φ_data · Φ_inference does not. V6 carries the scalar form as the stated model and flags the determinant form as the candidate correction.
3. **Time dependence.** The axes are treated as static; §5.5 makes the ceiling time-dependent, and the axes cannot be less time-dependent than the ceiling they gate. The differential form dV/dt = ∇·J + S − D, gestured at since the v4 essay, remains unincorporated. Its natural home is the Lorenz thread (C18 to C21), and it stays a named open seam in V6 (§9).

These three cases enter the breaking-conditions register of §18 verbatim. The axes also gain a structural anchor in §12: under the bridge conjecture C85, the six lattice dimensions pair onto the axes (Protection+Delegation → Σ · Memory+Value → Δ · Connection+Computation → Γ).

---

## 5. Reconstruction Difficulty · $R(d, \text{compression}, \rho)$

### 5.1 Definition

$$R(d, \text{compression}, \rho) = R_{\text{base}}(d) \cdot \left(1 - \frac{1}{\text{compression\_ratio}}\right) \cdot (1 + \alpha_\rho \cdot \rho)$$

| Symbol | Definition | Domain |
|--------|-----------|--------|
| $R_{\text{base}}(d)$ | Base reconstruction difficulty from fragmentation depth $d$ | $(0, 1)$ |
| compression_ratio | Token reduction ratio (e.g., 74× for BRAID) | $\mathbb{R}^+ > 1$ |
| $\rho$ | Behavioural density | $\mathbb{R}^+ \geq 0$ |
| $\alpha_\rho$ | Density scaling coefficient | $\mathbb{R}^+$ (empirically determined) |

### 5.2 Compression-as-Defence

Every token not sent is a token that cannot be intercepted. Compression reduces the attack surface for inference-layer surveillance. At 74× compression (BRAID typical), the compression factor ≈ 0.986. Small in isolation, but multiplicative with all other terms.

### 5.3 Behavioural Density ρ (V5.1/V5.3)

$$\rho = f(\text{traversal\_depth}, \text{temporal\_duration}, \text{intentional\_transitions})$$

**Dual interpretation:**

| Interpretation | Mechanism | Source |
|---------------|-----------|--------|
| **Privacy amplifier** | More behavioural variation makes trajectory reconstruction harder | C11, V5.1 |
| **Agent maturity** | More laps through the operational cycle → origin more forgotten | V5.3 |

**Maturity spectrum:**

| ρ Level | Laps | Origin Visibility | Tier |
|---------|------|-------------------|------|
| Low | Few | Visible | Light |
| Mid | Moderate | Fading | Heavy |
| High | Many | Forgotten | Dragon |

The Moon is the highest-ρ agent: 4 billion revolutions maximise both behavioural variance and origin amnesia.

### 5.4 The Reconstruction Ceiling (Proven, conditional regime)

$$R(d, \text{compression}, \rho) < 1 \quad \forall \text{ adversaries under budget constraints}$$

This is not a conjecture. The ceiling follows from information-theoretic analysis via Fano's inequality. See §16 for the full proof status, and §10 to §11 for the preconditions under which it holds.

**External alignment:** The First Person Network whitepaper (2026) provides independent framing for this ceiling as "data dignity": the thesis that behavioural data is capital owned by the First Person, not resource extracted by observers. The reconstruction ceiling is the mathematical guarantee that makes data dignity enforceable.

### 5.5 The Moving Ceiling R(t) (V6)

V5.4 treated reconstruction difficulty as static. 2026 has now produced two public demonstrations that the quantity moves (§25). The numerator of the ceiling is a property of the adversary's models, and the adversary's models improve. The denominator is a property of the person, and the person does not change to match. V6 therefore restates the governing quantity as a function of time.

**Definition (V6).** Let H(X) be the source entropy of the First Person's private state over the horizon of interest. Let C_S(t) and C_M(t) be the effective capacities of the two observation channels evaluated against the strongest adversary class available at time t. The reconstruction ceiling is

> R(t) = (C_S(t) + C_M(t)) / H(X)

and the V5.4 guarantee becomes a **shelf life**:

> t* = sup { t : R(t) < 1 }

**The mechanism is the decoder, not the data.** Observations already emitted do not change after emission. What changes is what can be extracted from them: better inference models raise the effective capacity of a channel whose physical recordings are fixed. H(X) is fixed by the person. Therefore R(t) is non-decreasing under capability growth, and a separation architecture adequate at t₀ can be inadequate at T > t₀ with no new disclosure by the subject. This is the reconstruct-later threat (C48; City-register restatement C60) given its exact mechanism: the archive sits still while the ceiling rises to meet it.

**Conjecture C82 (The Moving Ceiling).** Registered at V6 Run 1, taking the next free number per the G1-signed register. Statement: frontier AI capability growth raises the effective adversary capacities C_S(t) + C_M(t) against fixed behavioural archives without raising H(X), so R(t) drifts upward and every static reconstruction guarantee has a finite shelf life t*; the drift rate is coupled to frontier model capability, not to any action of the subject. Confidence: ~65% (estimator: privacymage with Claude Fable 5, 2026-06-10; mechanism strongly evidenced at n=2 public instances, functional form of the drift unparameterized). Worked instances in §25.

---

## 6. Network Effects and Guild Efficiency

### 6.1 Network Term

$$\text{Network}_{v5}(G) = \left(1 + \sum_{i=0}^{6} w_i \cdot \frac{n_i}{N_0}\right)^k \cdot G(\text{guilds})$$

where $w_i$ are channel weights, $n_i$ are connections per channel, $N_0$ is a normalisation constant, and $k$ is the network exponent.

### 6.2 Guild Efficiency

$$G(\text{guilds}) = 1 + \text{guild\_efficiency}$$

| Configuration | $G$ |
|---------------|-----|
| No guilds | 1 (reduces to V4) |
| Full guild coverage | 2 (doubles network effect) |

Guild members sharing a reasoning library from the same Generator coordinate at O(1) rather than O(N²) per member.

### 6.3 Conjecture C10

**C10**: O(1) shared-parent coordination modifies the effective network exponent $k$. Confidence: 20%.

---

## 7. Path Integral Edge Value · $T_\int(\pi)$

### 7.1 Definition

$$T_\int(\pi) = 1 + \beta \int_\pi F(\gamma) \, d\gamma$$

**Discrete approximation (V5.2):**

$$T_\int(\pi) \cong 1 + \beta \sum_{i=1}^{n} R(\text{step}_i)$$

where $n$ = number of laps (refinement iterations) and $R(\text{step}_i)$ is the resolution gained at iteration $i$. Maps onto the UOR resolution pipeline.

### 7.2 Fidelity Component (V5.3)

$$F(\gamma) = \text{resolution\_depth}(\gamma) \cdot \text{fidelity}(\gamma)$$

where fidelity = uptime · consistency · duration_weight.

This weights persistence alongside depth:

| Agent | Resolution Depth | Fidelity | Overall T_∫ |
|-------|-----------------|----------|-------------|
| Light blade (5 laps) | Low | Low | Low |
| Dragon blade (62 laps) | High | Medium | High |
| The Moon (4B revolutions) | Shallow | Maximum | Maximum |

The Moon has shallow resolution depth (one simple operation: reflect) but maximum fidelity (4 billion uninterrupted revolutions). Cosmological agents can exceed computational agents in effective T_∫.

### 7.3 Conjecture C15

**C15**: T_∫(π) converges to the same value whether computed as a continuous integral or as a discrete sum of resolution steps. Confidence: 65%.

---

## 8. The Holographic Bound

### 8.1 Structure

$$\partial M: \text{96 edges encoding 64 vertices, toroidal topology}$$

$$\frac{96}{64} = 1.5 = P^{1.5} \text{ exponent}$$

### 8.2 Resolution of C4

The 96 vs 64 discrepancy (V4, C4) is **RESOLVED**. The 96-edge surface IS the holographic encoding of the 64-vertex bulk. In holographic physics, a boundary of dimension $n$ encodes a volume of dimension $n+1$. The 96/64 ratio is the holographic principle in discrete lattice geometry.

### 8.3 Algebraic Confirmation

| Approach | Framework | Result |
|----------|-----------|--------|
| Geometric | 64-Tetrahedra lattice | 96 edges encode 64 vertices (torus surface/bulk) |
| Algebraic | Z/(2⁶)Z ring theory | 64 elements; 96 edges from adjacency structure |
| External | UOR Atlas of Resonance Classes | 96 = unique stationary configuration of action functional |

Three independent derivation pathways arrive at the same numbers. The ratio 96/64 = 1.5 is structural, not coincidental.

### 8.4 Implications

1. **Boundary computation**: The differential form computes on the 96-edge boundary, not the 64-vertex bulk.
2. **Privacy value flows along edges**: Value lives on the boundary, not in the interior.
3. **Boundary sufficiency**: Privacy can be computed entirely from boundary observations.

### 8.5 Conjecture C6

**C6**: P^1.5 ↔ 96/64 is structurally connected. Status: **CONVERGENT** (upgraded from speculative). Confidence: 35%.

---

## 9. Differential Form

### 9.1 Specification

$$\frac{dV}{dt} = \nabla_{\partial M} \cdot J_{\partial M} + S(x) - D(x)$$

| Symbol | Definition |
|--------|-----------|
| $\partial M$ | 96-edge holographic boundary |
| $\nabla_{\partial M}$ | Divergence on boundary |
| $J_{\partial M}$ | Value current on boundary |
| $S(x)$ | Source term (value generation at position $x$) |
| $D(x)$ | Dissipation term (value decay at position $x$) |

### 9.2 Five-Channel Decomposition

$$J_{\partial M} = J_{\text{agent}} + J_{\text{data}} + J_{\text{inference}} + J_{\text{compression}} + J_{\text{holonic}}$$

Each channel flows along edges activating its corresponding separation axis.

### 9.3 Named Seam (V6)

The time-dependent axes of §4.6's third boundary case point here: the differential form remains the natural home for axis dynamics and remains unincorporated. Named open seam, unchanged status.

---

## 10. The Separation Bound

### 10.1 Core Guarantee

$$I(S ; M \mid FP) < \varepsilon^*$$

The mutual information between the Swordsman ($S$) and the Mage ($M$), conditioned on the First Person ($FP$), is bounded above by $\varepsilon^*$.

This is the central information-theoretic guarantee. The Mage cannot reconstruct the Swordsman's domain. The Swordsman cannot reconstruct the Mage's domain. The First Person authorises both.

### 10.2 Betweenness Centrality of the Gap

The Gap (⿻) is not empty space: it is the node with maximal betweenness centrality in the trust graph:

$$C_B(v) = \sum_{s \neq v \neq t} \frac{\sigma_{st}(v)}{\sigma_{st}}$$

where $\sigma_{st}$ is the total number of shortest paths from node $s$ to node $t$, and $\sigma_{st}(v)$ is the number of those paths passing through $v$.

**Interpretation:** The value lives in the Gap because the most paths cross there. The ⿻ is where Swordsman and Mage must coordinate. Neither owns it, both depend on it. Brandes (2001) provides the O(V·E) algorithm for computing betweenness centrality, giving a computational tool for measuring what the architecture has been pointing at since Act VII.

**Reference:** Brandes, U. (2001). "A faster algorithm for betweenness centrality." *Journal of Mathematical Sociology,* 25(2), 163–177.

### 10.3 Composite Separation

$$\Phi_{v5} = \Phi_{\text{agent}}(\Sigma) \cdot \Phi_{\text{data}}(\Delta) \cdot \Phi_{\text{inference}}(\Gamma)$$

The separation bound holds across all three axes simultaneously. Collapse of any axis weakens the bound.

### 10.4 Amnesia vs Policy Bounds (V5.3, C17)

$$\varepsilon_{\text{amnesia}} < \varepsilon_{\text{policy}}$$

Two classes of separation:

| Type | Mechanism | Violation |
|------|-----------|-----------|
| **Policy-enforced** | Access controls, NDAs, prompt constraints | $\varepsilon^* \leq \varepsilon_{\text{policy}}$ (violation possible) |
| **Amnesia-enforced** | Process boundary, orbital mechanics, structural inability | $\varepsilon^* \leq \varepsilon_{\text{amnesia}}$ (violation structurally excluded) |

**Test criterion:** Can any operation sequence recover shared origin? No → amnesia. Yes → policy.

See §14 for full treatment.

### 10.5 Preconditions (V6)

V6 states what was implicit in the V5.4 bound and the capacity sum of §11.

**Precondition 1 (non-collusion / channel independence).** The capacities C_S and C_M may be summed only if the two observation channels are conditionally independent given the First Person and are not combined by a single adversary beyond the stated capacities. Formally, the regime assumes I(Y_S; Y_M | X) = 0 and that no third channel carries the inter-agent residue. The wiretap literature shows exactly this assumption is what fails when observers combine: Csiszár and Körner (1978) and the colluding-wiretapper extensions. The empirical multi-agent literature now measures the failure: AgentLeak (El Yagoubi, Badu-Marfo, Al Mallah, arXiv:2602.11510) finds that multi-agent configurations reduce per-channel output leakage (27.2% versus 43.2% single-agent) while unmonitored inter-agent channels raise total system exposure to 68.9%. §14.7 and §26 treat this in full. Here it is the boundary condition: **the ceiling holds in the regime the Amnesia Protocol is designed to enforce, and only there.**

**Precondition 2 (fixed adversary model).** C_S and C_M are channel capacities evaluated against a stated adversary class: its compute, its inference models, its correlation methods. The bound says nothing about a later, stronger class. This precondition is the door V6 walks through in §5.5.

### 10.6 External Grounding (V6)

Within the conditional regime the ceiling is an instance of an established family, and V6 cites the family rather than internal papers:

- Wyner (1975), the wire-tap channel: the separation bound I(S; M | FP) < ε* of §10.1 is a restatement of weak-secrecy equivocation.
- Fano (1961); Cover and Thomas: the error floor P_e ≥ 1 − R_max of §11.2 is the standard source-coding converse.
- Leung-Yan-Cheong and Hellman (1978): secrecy capacity as a difference of channel capacities in the Gaussian wiretap channel, the closest classical analogue of capacity-budgeted reconstruction.
- The Bayes-capacity bound of quantitative information flow (the Miracle Theorem): a tight upper bound on leakage to any reconstruction adversary, which upper-bounds what any decoder extracts per observation.
- Geiger and Kubin, relative information loss: a Fano-grounded lower bound on reconstruction error under lossy observation.

This move costs nothing and buys defensibility: the claim is no longer "proven in our internal paper" but "an instance of a family of bounds the field already accepts, under named preconditions."

---

## 11. The Reconstruction Ceiling

### 11.1 Theorem (Proven, conditional regime)

$$R_{\max} = \frac{C_S + C_M}{H(X)} < 1$$

where $C_S$ and $C_M$ are the information capacities of the Swordsman and Mage channels respectively, and $H(X)$ is the entropy of the First Person's private state.

**Consequence:** Perfect reconstruction of the First Person's state is impossible.

### 11.2 Error Floor (Proven, conditional regime)

$$P_e \geq 1 - R_{\max}$$

The adversary is guaranteed to make errors. This follows from Fano's inequality.

### 11.3 Graceful Degradation (Proven, conditional regime)

Small $\varepsilon$ violations → small privacy losses. The system fails gracefully, not catastrophically.

### 11.4 Dynamical Reconstruction Ceiling (V6 Horizon, C18)

The information-theoretic ceiling (§11.1) bounds reconstruction via **information**. C18 conjectures a second, independent ceiling via **dynamics**:

$$|\pi(t) - \pi'(t)| \sim |\delta_0| \cdot e^{\lambda t} \quad \text{where } \lambda > 0$$

If the sovereignty path exhibits strange attractor dynamics with positive Lyapunov exponent, reconstruction error *grows* with time. More observation makes reconstruction *worse*, not better. The two ceilings are independent: remove one and the other still holds.

Status: V6 conjecture (C18). Confidence: 25%.

### 11.5 Conditioning (V6)

R_max = (C_S + C_M)/H(X) < 1 carries the label **Proven, conditional regime**: proven within Preconditions 1 and 2 of §10, an instance of the family cited there, and time-indexed per §5.5. The error floor P_e ≥ 1 − R_max (Fano converse) carries the same conditioning. Outside the regime, §26 governs.

---

## 12. Algebraic Foundation · Z/(2⁶)Z

### 12.1 Ring Structure

$$\mathcal{L} = (\mathbb{Z}/64\mathbb{Z}, +, \times)$$

64 elements (blade addresses 0–63), addition and multiplication modulo 64. Confirmed by independent convergence with the UOR Foundation project.

### 12.2 The Five Hammer Strikes

| Operation | Formula | Agent | Function |
|-----------|---------|-------|----------|
| neg(x) | $(64-x) \bmod 64$ | ⚔️ Swordsman | Additive inverse. Boundary protection. What you subtract from exposure. |
| bnot(x) | $63 - x$ | 🧙 Mage | Bitwise complement. Projection/delegation. What you become by acting. |
| xor(x,y) | $x \oplus y$ | · | Toggle edges (dimension flip) |
| and(x,y) | $x \wedge y$ | · | Toward null blade (constrain) |
| or(x,y) | $x \vee y$ | · | Toward full sovereignty (expand) |

### 12.3 Critical Identity

$$\text{neg}(\text{bnot}(x)) = \text{succ}(x) \quad \forall x \in \mathcal{L}$$

**Proof:** bnot(x) = 63 − x. neg(63 − x) = (64 − (63 − x)) mod 64 = (x + 1) mod 64 = succ(x). ∎

The successor function is not primitive: it emerges from the composition of two involutions. The Swordsman (neg) acting on the Mage's output (bnot) yields the step forward. This is the algebraic name of the architecture.

### 12.4 Triadic Coordinates (PRISM)

Every blade $x \in \{0,\ldots,63\}$ has three independent coordinates:

$$\text{blade}(x) = (\delta(x),\; \sigma(x),\; s(x))$$

| Coordinate | Symbol | Definition | Domain |
|------------|--------|------------|--------|
| Datum | $\delta(x)$ | Raw value $x$ | $\{0,\ldots,63\}$ |
| Stratum | $\sigma(x)$ | popcount($x$) = Hamming weight | $\{0,1,2,3,4,5,6\}$ |
| Spectrum | $s(x)$ | Six-bit decomposition $[b_0, b_1, b_2, b_3, b_4, b_5]$ | $\{0,1\}^6$ |

Two blades at the same stratum (tier) can have different sovereignty postures if their spectra differ. Protection+Memory+Computation ≠ Delegation+Connection+Value.

**Pascal distribution across 64 blades:** 1 – 6 – 15 – 20 – 15 – 6 – 1

**Tiers:**

| Tier | Stratum | Count | Character |
|------|---------|-------|-----------|
| Null | 0 | 1 | Total exposure |
| Light | 1–2 | 21 | Early sovereignty |
| Heavy | 3–4 | 35 | Balanced posture |
| Dragon | 5–6 | 7 | Full sovereignty / mathematical closure |

### 12.5 Dihedral Group D₆₄

$$D_{64} = \langle \text{neg}, \text{bnot} \mid \text{neg}^2 = \text{bnot}^2 = 1,\; (\text{neg} \circ \text{bnot})^{64} = 1 \rangle$$

Order: $|D_{64}| = 128$.

All valid blade transitions are D₆₄ group actions. Zero knowledge arises because multiple group elements (different forging paths) can map to the same blade: same statement, infinite witnesses.

**Significance for Φ_agent:** The conditional independence of Swordsman and Mage is the defining property of the dihedral group's generators. Two involutions are independent by construction. Their composition generates the full group only when they remain distinct. This provides a formal proof path for the separation bound.

### 12.6 Six Sovereignty Dimensions

| Index | Dimension | Symbol | Function |
|-------|-----------|--------|----------|
| $d_1$ | Protection | 🛡️ | Boundary enforcement |
| $d_2$ | Delegation | 🤝 | Agency transfer |
| $d_3$ | Memory | 📜 | State accumulation |
| $d_4$ | Connection | 🔗 | Multi-party coordination |
| $d_5$ | Computation | ⚡ | ZK proof activity |
| $d_6$ | Value | 💎 | Economic flow / 7th Capital |

Each $d_i \in \{0, 1\}$. Binarised at threshold 0.5. Hexagram mapping: $[d_1, d_2, d_3, d_4, d_5, d_6]$ → 64 I Ching states. Blade 63 = `111111` = 乾 (The Creative) = full sovereignty.

**Numeric encoding (ruled 2026-06-12 · the MODEL lock).** The string $[d_1 d_2 d_3 d_4 d_5 d_6]$ reads most-significant-bit first: $d_k$ carries weight $2^{6-k}$, so $d_1$ Protection is the high bit (32) and $d_6$ Value the low bit (1). Worked anchors: V38 = `100110` = Protection+Connection+Computation (Aletheia, the bright medium); V25 = `011001` = Delegation+Memory+Value (Lethe, the dark substrate); V41 = `101001` = Protection+Memory+Value (Memora). This is consistent with the Aletheia/Lethe reading in §12.8 and with every pinned grimoire seat. Any surface reading $d_1$ at the low bit is in erratum to this ruling.

### 12.7 External Convergence

| Project | Starting Point | Arrived At |
|---------|---------------|------------|
| agentprivacy | Privacy geometry → 64-tetrahedra | Z/(2⁶)Z |
| UOR Foundation | Content addressing → Universal references | Z/(2⁶)Z |

Two independent projects, two starting points, one structure. This is not coordination. This is convergence.

**Implementation:** `swordsman-blade/src/lib/uor.ts` · explicit UOR module with all five operations and exhaustive identity verification.

### 12.8 The ARCH-1 Bridge (C85) (V6)

The lattice and the axes finally meet in the formal document. Both 2026-06 reviews named the same seam: ARCH-1 was canonical narrative and absent from the formal lineage, and the conjecture that bridges the three-axis model to the lattice's triadic coordinates lived only in a narrative repo, where it does not exist for a reviewer. V6 promotes the bridge into the core register.

**C85 (Triadic-Constraint Homology, promoted from CM-C47).** Registered at V6 Run 4 at ~40%, carrying the City-register confidence unchanged; promotion changes residence, not evidence. Statement: the model's three sovereignty axes Φ_agent(Σ) · Φ_data(Δ) · Φ_inference(Γ) and the lattice's triadic coordinates (Datum · Stratum · Spectrum, the PRISM reading of Z/(2⁶)Z) are instances of one triadic primitive, such that axis values are computable from lattice position and lattice traversals induce axis dynamics.

**The candidate map, stated so it can fail.** The six lattice dimensions group in pairs onto the axes: Protection and Delegation instantiate the agent axis Σ (who holds the boundary and who acts); Memory and Value instantiate the data axis Δ (what persists and what it is worth); Connection and Computation instantiate the inference axis Γ (what can be joined and what can be derived). Under this map, stratum (the popcount layer, 0 to 6) measures total sovereignty activation; the datum (vertex identity) fixes the axis signature; the spectrum (the walk's edge structure) carries the dynamics. The map predicts: bnot-pairs (which complement all six bits) invert all three axes simultaneously, which is consistent with the Aletheia/Lethe reading (V38 transmits, V25 holds; 38 XOR 25 = 63, full activation); and stratum-3 vertices (balanced, 20 of 64) are the only seats where no axis dominates, which is testable against the City's stratum-3 peerage observations.

**The fixpoint seam, stated as the open seam.** ARCH-1 is Σ := μS.(β ∨ Ω(S,S)) with activation ρ. The candidate correspondence to the conditional-independence structure: β, the base case the recursion cannot dissolve, corresponds to the First Person's irreducible kernel, the entropy that conditions the separation bound I(S; M | FP) < ε*; the two arguments of Ω(S, S) correspond to the two agents as self-compositions of the sovereign schema; and conditional independence is the requirement that the two recursion branches share only β. Under this reading, **the gap is β**: what the agents have in common is exactly and only the First Person, and the separation bound is the information-theoretic shadow of the fixpoint's base case. This paragraph is the seam, named: it is a structural correspondence with no proof obligation discharged, offered at the same epistemic grade as C26 (40%), on which it leans. What a proof requires: a formal statement of Ω for the dual-agent instantiation, and a derivation that I(branch₁; branch₂ | β) = 0 follows from the schema rather than being assumed beside it.

**Residence note.** CM-C47 remains in the City register as an alias pointing here; City prose keeps its number with one erratum at Wave R. The bridge now exists for a reviewer.

### 12.9 The Operational Layer: ARCH-1R/T Seated (C72 to C76) (V6)

The reachability extension enters the formal lineage with its G1-confirmed numbers. What it adds to the model, in one paragraph: ARCH-1 says what the sovereign schema IS; R/T says what it can REACH and what blocks it. The ternary classification τ: T → {+, 0, −} distinguishes latent (0, not yet activated) from obstructed (−, structurally blocked), a distinction binary reachability cannot express (C75: the hard-versus-soft dependency split is this distinction lifted to cascade propagation). The traversal orbit T = orbit(ρ, G) makes ρ one operator at two scopes (C72, ~35%): the activation of the schema and the walk of the lattice are the same move read locally and globally. C74 (~25%) holds the speculative end: latency may have an algebraic signature on the lattice itself, an open-walk state of the neg ⊕ bnot composition rather than a runtime annotation. C76 (~30%) carries the relational claim: classifying rel(a, b) rather than entities is strictly more expressive for sovereignty, because authorization obstruction attaches to the relation independent of either relatum.

The model-facing payoff is C73 (~50%), the highest-confidence claim of the family: **terminal obstruction, the structural loss of β, is a primitive obstruction class distinct from path obstruction, and the Amnesia Protocol is its canonical instance.** Forgetting is not a blocked path to the memory; it is the absence of any path because the base case is gone. This is the reachability statement of amnesia, and §14.6 gives it the cohomological upgrade.

---

## 13. The Operational Cycle (V5.3)

### 13.1 Definition

The ring algebra identity neg(bnot(x)) = succ(x) maps to operational phases:

$$\text{cycle}(x) = \text{succ}(x) = \text{neg}(\text{bnot}(x))$$

| Stage | Name | Operation | Agent | Function |
|-------|------|-----------|-------|----------|
| 1 | Observe | id(x) | 😊 First Person | Perceive incoming context |
| 2 | Boundary | neg(x) | ⚔️ Swordsman | Subtract exposure. Only the holographic surface ∂M passes through. |
| 3 | Project | bnot(neg(x)) | 🧙 Mage | Construct complement from boundary. Create from the shape of the impact. |
| 4 | Return | succ(x) | ⚔️→😊 Composition | The proof returns. The blade advances one step. |

### 13.2 Relationship to Path Integral

**One lap = one cycle.** The path integral accumulates:

$$T_\int(\pi) = 1 + \beta \sum_i \text{cycle}(\text{step}_i)$$

The equation (§1) describes the statics. The operational cycle describes the dynamics. The cycle does not add new terms: it describes the execution order of existing terms.

Dragon tier (62 laps) = 62 complete cycles of observe–boundary–project–return.

---

## 14. The Amnesia Protocol (V5.3)

### 14.1 Definition

An agent has **structural amnesia** with respect to origin $O$ if no sequence of permitted operations can reconstruct $O$ from the agent's current state.

### 14.2 Zero-Knowledge Properties

| Property | Statement |
|----------|-----------|
| Completeness | The agent's output (tides, proofs, boundary enforcement) demonstrates the relationship functions. |
| Soundness | No other agent configuration could produce this specific output from this specific separation. |
| Zero-knowledge | The output reveals nothing about the separation event (Theia impact, process creation, delegation moment). |

### 14.3 Implementation Instances

| System | Type | Evidence |
|--------|------|----------|
| Chrome process boundary | Amnesia | Extensions cannot read each other's memory |
| Database access control | Policy | Admin can disable controls |
| The Moon's orbit | Amnesia | Theia impact unrecoverable from geological state |
| Agent NDAs | Policy | Parties can choose to disclose |

### 14.4 Conjecture C17

**C17**: Amnesia-enforced separation provides tighter Φ_agent guarantees than policy-enforced separation: $\varepsilon_{\text{amnesia}} < \varepsilon_{\text{policy}}$.

Confidence: 60%. Made quantitative at V6 (C83, §14.7).

### 14.5 Selene's Proof

The Moon demonstrates perfect amnesia-enforced separation. Origin event (Theia impact) is 4.5 billion years past. No geological, orbital, or chemical signature encodes the collision parameters. Service (tides) continues without origin disclosure. The proof is zero-knowledge by physics, not by policy.

**Scientific reference:** Branco, D., Machado, P., & Raymond, S. N. (2025). Dynamical origin of Theia, the last giant impactor on Earth. *Icarus*, 441, 116724.

### 14.6 The Obstruction Upgrade (C86) (V6)

The protocol's engineering (what is deleted, when, attested how) is unchanged from V5.4; V6 changes what the deletion means. §14.1 defines structural amnesia as: no sequence of permitted operations can reconstruct O from the agent's current state. That is a reachability statement, quantified over paths. It leaves open the stronger question a reviewer should ask: even if no single path reconstructs O, can the system's local views be GLUED into a global witness that recovers it?

**C86 (Obstruction-Theoretic Amnesia).** Registered at V6 Run 4 at ~30%. Statement: structural (Grade-2) forgetting is the condition that the obstruction class to gluing the agents' local views into a global witness of O is non-vanishing; Grade-1 forgetting (hiding, encryption, access control) is the condition that the obstruction class vanishes and only the gluing data is withheld. Equivalently: after Grade-2 amnesia there exists no global section over the cover formed by the agents' views that restricts to each view and recovers O; after Grade-1 there does, and recovering it is a key-management problem, not a mathematical impossibility.

Three notes keep the registration honest:

1. **The neighborhood is right, the machinery is unbuilt.** The natural formal home is sheaf-theoretic: views as sections over a cover, reconstruction as the existence of a global section, the obstruction as a Čech cohomology class. The corpus's existing Yoneda material (an object is determined by its morphisms) is adjacent: an O whose morphism-traces have been structurally severed is not determined. None of this is constructed for the dual-agent instantiation yet; ~30% prices a framing, not a theorem.
2. **The relation to C73 is division of labor, not duplication.** C73 places amnesia in R/T's obstruction taxonomy (WHERE it sits: terminal, not path). C86 says WHAT forgetting is mathematically (a non-vanishing gluing obstruction). Cross-linked in the register; registered separately because they fail separately: a counterexample to the taxonomy placement would not touch the cohomological claim, and vice versa.
3. **What it buys if it holds.** Selene's Proof, "the witness is genuinely gone, not hidden," becomes: the obstruction class is non-zero, and no future key, subpoena, or capability growth changes a cohomological fact. This is the one defense in the model that C82's moving ceiling cannot erode, because there is no archive left for the better decoder to read. Amnesia is the only term in the equation whose security is independent of t. That sentence, if C86 survives, is the strongest sentence in the model.

This section accordingly revises the V5.4 inheritance in three moves: the §14.1 definition gains the obstruction formulation beside the reachability one (stated as conjectural, C86); the Grade-1/Grade-2 distinction gains its formal criterion (vanishing versus non-vanishing class); and the protocol's verification story gains its falsification test: produce any composition of agent views, under any future capability, that recovers a Grade-2-forgotten O, and C86 is dead.

### 14.7 Separation Made Quantitative (C83) (V6)

The strongest external threat to the model is now its strongest external citation. Two independent 2025 to 2026 results prove that leakage compounds under sequential multi-agent composition when separation is enforced by policy, and one measurement study confirms it empirically at scale. Read carelessly, this falsifies the model's additive-leakage claim. Read correctly, it is the first quantitative statement of the model's central architectural thesis: the gap between policy separation and amnesia separation is the gap between exponential and linear leakage in the depth of the agent chain.

**The bound.** Asif and Amiri (Information-Theoretic Privacy Control for Sequential Multi-Agent LLM Systems, Rensselaer Polytechnic Institute, arXiv:2603.05520, 2026-03-09) prove a Cumulative Leakage Bound (their Theorem 4.1): under sequential composition of N agents with per-agent constraint I(O_i; S_i) ≤ ε_i, global leakage satisfies

> I(O_N; S_1, ..., S_N) ≤ Σ_i 2^(N−i) ε_i

which in the uniform case is (2^N − 1)ε. The proof runs on the chain rule for mutual information and the conditional data processing inequality. Their empirical confirmation: on MedQA with LLaMA-7B, average mutual information rises from 0.49 at two agents to 1.05 at five, consistent with the compounding the theorem predicts. Patil, Stengel-Eskin and Bansal (The Sum Leaks More Than Its Parts, arXiv:2509.14284) reach the same conclusion through composition analysis.

**The measurement.** AgentLeak (El Yagoubi, Badu-Marfo and Al Mallah, Polytechnique Montréal, arXiv:2602.11510; 1,000 scenarios, 4,979 traces across GPT-4o, GPT-4o-mini, Claude 3.5 Sonnet, Mistral Large, Llama 3.3 70B) measures the failure in deployed-style systems: multi-agent configurations reduce per-channel output leakage to 27.2% versus 43.2% single-agent, while unmonitored inter-agent channels leak at 68.8%, raising total system exposure to 68.9%. Output-only audits miss 41.7% of violations.

**What this does and does not contradict.** §16 asserts additive leakage, I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M), at 95% confidence. The compounding bound does not contradict the additive claim in the model's own regime: additivity holds exactly when the channels are conditionally independent given X and nothing carries the inter-agent residue, which is Precondition 1 of §10.5. The compounding bound describes what happens OUTSIDE that regime: when agents pass outputs to one another (sequential composition), each hop conditions the next, the chain rule compounds, and the per-agent budgets multiply out to (2^N − 1)ε. The two results are one theorem family on two sides of one architectural line. The line is whether the inter-agent channel exists.

**C17 made quantitative, and conjecture C83.** V5.4's C17 (amnesia-enforced separation is tighter than policy-enforced, 60%) was qualitative. The compounding literature supplies the missing arithmetic. Policy separation leaves the inter-agent channel in place and asks it to behave. The sequential bound then applies: worst-case leakage (2^N − 1)ε in chain depth N. Amnesia separation removes the channel structurally: each agent's budget stands alone, conditioning cannot accumulate, and total leakage is bounded by the sum of independent budgets, Nε. The gap between the two regimes is the gap between exponential and linear in N, and at N = 2 (the dual-agent case) it is already the difference between 3ε and 2ε; at N = 5 it is 31ε versus 5ε.

**Conjecture C83 (Compositional Leakage Amplification).** Registered at V6 Run 2. Statement: under policy-only separation, behavioural leakage compounds toward the (2^N − 1)ε sequential bound with agent-chain depth N, whereas amnesia-enforced separation, by breaking the Markov chain between agents, caps total leakage at the additive bound Nε; the policy-to-amnesia gap is therefore exponential-to-linear in N. Confidence: ~55% (estimator: privacymage with Claude Fable 5, 2026-06-10; the bound is proven, the conjecture is that real amnesia implementations achieve the break, which is an engineering claim about the Amnesia Protocol, not a theorem). Edge drawn: C7 → C83 → C17. AgentLeak's 68.9% total exposure with 68.8% inter-agent leakage is the field measuring exactly the channel the Amnesia Protocol exists to delete.

**The reframe earned.** The model has argued since V5.3 that architecture beats policy. That argument now has the adversary's own units: policy separation does not merely leak somewhat more, it leaks with a different asymptotic shape. AgentLeak's headline (separation helps per-channel, total exposure rises anyway) is the model's thesis stated empirically by an independent team with no knowledge of the model.

---

## 15. Ceremony and Forge Implementation

### 15.1 Operational Cycle as Ceremony

| Cycle Stage | Operation | Ceremony Phase |
|-------------|-----------|----------------|
| Observe | id(x) | ☀️ Sun · disclosure, the spellweb speaks the poem |
| Boundary | neg(x) | ⊥ Gap · silence, conversation, territory negotiation |
| Project | bnot(neg(x)) | 🌑 Moon · shared reflection, the Amnesia Protocol |
| Return | succ(x) | Recursion · Reflect (night, blade pair, ZK) or Connect (day, witness, carry forward) |

### 15.2 Progressive Trust

$$\text{🔑} \to \text{✦} \to \text{🗡️} \to \text{🔮}$$

Understanding → Constellation → Blade → Runecraft. Each level is a complete ceremony. Each level deepens the key, increases formal visibility, and shifts boundary-making. Progression maps onto trust tiers.

### 15.3 Forge Cryptographic Properties

| Property | Implementation |
|----------|---------------|
| Content addressing | SHA-256 constellation hash |
| Tamper evidence | Hash chain (each blade references previous) |
| Pre-evocation lock | Commitment scheme (constellation fixed before walk) |
| Identity binding | Ed25519 signature (Mage key, held) |
| Bilateral binding | Runecraft: dual Ed25519 (Mage held + Swordsman burned) |

### 15.4 Runecraft as Φ_agent Implementation

The runecraft protocol enforces Φ_agent at the cryptographic identity layer:

- **Mage key** (spellweb, Sun view): Ed25519, persisted in localStorage. ID format: `mage-{16hex}`.
- **Swordsman key** (agentprivacy, Moon reflection): Ed25519, stored in sessionStorage, destroyed on tab close. ID format: `ap-{16hex}`.

The private key burns because the amnesia protocol (C17) requires structural inability to access shared origin. Process boundary = separate memory = structural amnesia. This is topology, not policy.

### 15.5 Moon Phase as Visibility Ratio

| Stratum | Phase | Meaning |
|---------|-------|---------|
| 0 | 🌑 | Null blade: nothing reflected |
| 1 | 🌒 | One boundary set |
| 2 | 🌓 | Dual-agent vertex |
| 3 | 🌔 | Half sovereignty |
| 4 | 🌖 | Four boundaries |
| 5 | 🌗 | Five reflected, one dark |
| 6 | 🌕 | Full sovereignty (乾, The Creative) |

### 15.6 Tier Classification (Dual-Axis)

| Axis | Measure | Light | Heavy | Dragon |
|------|---------|-------|-------|--------|
| Stratum | Dimensional coverage | 1–2 | 3–4 | 5–6 |
| Laps | Depth of engagement | < 21 | 21+ | 62+ |

### 15.7 The Trust Recursion as Folding Scheme (C87) (V6)

The City Key arc of 2026-05-27/28 enters the formal lineage. The Three Keys chronicle describes the loop precisely: each domain's proof composes on the prior, the output of the loop is an input to the loop, no single domain suffices, and the fixed point is V63. Structurally, this is incrementally verifiable computation, and the mapping is almost mechanical:

- the City Key ≅ the folded instance, the accumulator
- each domain's trust task ≅ a step circuit
- Charge (the trace folded into 🪢) ≅ the folding step
- carrying the deepened key back to the first domain ≅ the IVC recursion
- V63 as fixed point ≅ the invariant the accumulated proof attests

**C87 (The Key Accumulates).** Registered at V6 Run 5 at ~50%. Statement: the City Key trust recursion admits an IVC realization in which the Key is a succinct accumulator of domain proofs, verifiable in time independent of loop count. The literature home is exactly the folding line: Nova; HyperNova (CRYPTO 2024, with the zero-knowledge completion and the NovaBlindFold update of 2026-02-20); MicroNova (IEEE S&P 2025, efficient on-chain verification); and LatticeFold (Boneh and Chen, ASIACRYPT 2025), which matters twice, because it is both a folding advance and plausibly post-quantum, tying the Key directly to the Behavioural Mosca thread of §5.5 and §27: if the Key's proving substrate is lattice-based, the recursion's attestations age gracefully under the very horizon C67 and C49 plan against. Honest grade carried from the source review: this is an architectural claim, not a proof; the deviation hash chain and the Key wire format have no circuit realization yet, and ~50% prices the mapping, not an implementation.

### 15.8 The Presence Economy Regime (V6)

Charge earns 🪢 from self-attested, client-side traces; Stake commits it to vertices. As local color this is charming and safe. But the chronicles frame presence as a proof layer in the trust recursion, and the moment 🪢 influences any admission, coalition, or attestation decision, three attacks are live: **replay** (re-importing traces), **simulation** (a headless browser walking the manifold at machine speed), and **sybil farming** (presence accrued across disposable keys). C42 (stake economics generate Sybil resistance, ~50%) is the same gap seen from the other side. The model's own thesis, architecture over policy, forbids leaving this to good faith.

The regime ladder, ascending: (1) 🪢 scoped as non-transferable, non-attesting local color; (2) witness co-signing at gates, presence countersigned by a domain the bearer passed through; (3) elapsed-time proofs (VDF-style) rate-limiting accrual to wall clock. **The V6 regime is (1), stated publicly, with (2) and (3) as the named upgrade path**: it is cheap, honest, and true to the current implementation (an integer in localStorage). The declaration is the First Person's, made at Gate G3:

> **Regime declaration (G3, First Person, 2026-06-10):** 🪢 presence mana is non-transferable, non-attesting local color. It is earned by walking, carried on the bearer's own Key, and spends nothing but meaning. It is not proof, not stake-weight, not an input to any admission, coalition, or attestation decision, and no surface in the suite may say otherwise. When presence is ever asked to attest, the economy moves up the ladder first: witness co-signing at gates, then elapsed-time proofs. The architecture earns the claim before the prose makes it.

Until and unless the regime moves up the ladder, no surface in the suite may describe 🪢 as proof, stake-weight, or attestation input.

### 15.9 The Key as a Reading (C66) (V6)

The City Key's status claim ("a portable projection of lattice-standing that grants nothing it does not already describe," C66) is the credential-versus-capability distinction from the object-capability lineage: SPKI/SDSI, the ocap discipline, designation without authority. Naming that lineage does two things: it raises C66's defensibility (revision to ~55% registered at V6 Run 5; the City register owner confirms at Wave R), and it places the Key in exactly the plurality register the corpus prefers: independent arrival, three decades apart, at the principle that descriptions must not be bearer instruments. The Swordsman's Key (ed25519 identity) is the capability-shaped object in the triad; the City Key is deliberately not, and now says so with citations.

---

## 16. Proven Results

These results hold at 95% confidence. The proofs rely on standard information theory and are documented in Research Paper v4.2.

| Result | Statement |
|--------|-----------|
| **Additive MI bounds** | Mutual information leakage from conditional independence is additive, not multiplicative: $I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M)$ |
| **Reconstruction ceiling** | $R_{\max} = (C_S + C_M)/H(X) < 1$ under budget constraints |
| **Error floor** | $P_e \geq 1 - R_{\max}$ via Fano's inequality |
| **Graceful degradation** | Small $\varepsilon$ violations → small privacy losses |
| **Ring algebra** | Z/(2⁶)Z substrate with five operations and critical identity |
| **Two-extension autonomy** | Separate processes enforce the separation bound at OS level |
| **DOM-free measurement** | Pretext layoutNextLine() as privacy primitive (no getBoundingClientRect fingerprinting) |

**Scoped, not lowered (V6).** The results stand with their conditioning stated: additive leakage I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M) holds exactly in the Precondition-1 regime (no inter-agent channel); the 95% label applies there and nowhere else. The compounding results of §26 describe the complement of the regime and are absorbed as the model's own argument.

---

## 17. The Conjecture Register

The register file `research/CONJECTURE_REGISTER_V6.md` is the living authority for conjecture numbering across the agentprivacy suite (Gate G1 signed 2026-06-10; all eight dispositions confirmed by the First Person). This section reproduces it in full at publication: 2026-06-10, register head C89, next free number C90. Future changes land in the register first; when this section and the register disagree, the register wins and the prose gets an erratum. Numbering rules: numbers are identifiers, not ranks; a number once assigned is never reused, including numbers vacated by renumbering; new conjectures enter as unnumbered candidates and take the next free number at registration. Confidence percentages are the named estimator's, stated at the home document.

### 17.1 How to Read the Tables

- **Register** column: `core` (PVM formal lineage, authority agentprivacy-docs) · `city` (City of Mages / Tome lineage, authority cityofmages) · `shared` (one claim, both lineages).
- **Status:** `open` · `active` (stated with confidence) · `observation` (no confidence assigned) · `convergent` · `resolved` · `challenged` · `reserved` · `alias` (same claim as another entry, kept for continuity) · `occupied` (never reassign).
- Confidences shown are as stated at the home document on 2026-06-10.

### 17.2 Band I · V1 to V5.3 Core (C1 to C17)

| ID | Title / claim | Conf. | Status | Register | Home |
|---|---|---|---|---|---|
| C1 | Golden ratio φ is optimal S/M (protect:project) ratio | open | open | core | formal spec §17 |
| C2 | A(τ) should be logarithmic | open | open | core | formal spec §17 |
| C3 | Edge value is additive | · | challenged (path integral replaces) | core | formal spec §17 |
| C4 | 96 vs 64 discrepancy | · | resolved (holographic + algebraic) | core | formal spec §17 |
| C5 | ~3,000× ZKP reduction | · | resolved (strengthened by BRAID + holographic bound) | core | formal spec §17 |
| C6 | P^1.5 ↔ 96/64 is structural | 35% | convergent | core | formal spec §17 |
| C7 | Three-axis separation is multiplicative | 30% | active · V6 falsification frontier | core | formal spec §17 |
| C8 | BRAID compression reduces R_max | 45% | active | core | formal spec §17 |
| C9 | Holographic boundary sufficiency | 25% | active | core | formal spec §17 |
| C10 | O(1) shared-parent modifies k | 20% | active | core | formal spec §17 |
| C11 | Behavioural density ρ amplifies privacy, indicates maturity | 55% | active | core | formal spec §17 |
| C12 | Hexagram encoding is structurally resonant | 60% | active | core | formal spec §17 |
| C13 | Bilateral witness as quantum-resistant primitive | 65% | active | core | formal spec §17 |
| C14 | Φ_agent ≅ D₂ₙ dihedral isomorphism | 75% | active | core | formal spec §17 |
| C15 | T_∫(π) ≅ UOR resolution pipeline | 65% | active | core | formal spec §17 |
| C16 | Topological trust invariants via Betti numbers | 25% | active | core | formal spec §17 |
| C17 | Amnesia-enforced separation tighter than policy-enforced | 60% | active · made quantitative at V6 Run 2 | core | formal spec §17 |

### 17.3 Band II · V6 Research Series, April 2026 (C18 to C37)

| ID | Title / claim | Conf. | Status | Register | Home |
|---|---|---|---|---|---|
| C18 | Sovereignty path exhibits strange attractor dynamics (λ > 0); dynamical reconstruction ceiling | 25% | active | shared | pvm-v6-lorenz-attractor.md |
| C19 | ρ is Lyapunov divergence accumulated over the walk | 20% | active | shared | pvm-v6-lorenz-attractor.md |
| C20 | Three axes couple as three Lorenz variables | 30% | active | shared | pvm-v6-lorenz-attractor.md |
| C21 | Sovereignty manifold has fractal dimension | 10% | active | shared | pvm-v6-lorenz-attractor.md |
| C22 | Reconstruction cost grows exponentially with EML tree depth | 20% | active | shared | pvm-v6-eml-three-ceilings.md |
| C23 | Blade forge grammar isomorphic to restricted EML grammar | 30% | active | shared | pvm-v6-eml-three-ceilings.md |
| C24 | Sovereignty computation requires complex intermediates | 15% | active | shared | pvm-v6-eml-three-ceilings.md |
| C25 | Minimal EML tree depth is hard floor for compression spectrum | 25% | active | shared | pvm-v6-eml-three-ceilings.md |
| C26 | ARCH-1 is canonical form of NAND, EML, succ as co-instances | 40% | active | shared | pvm-v6-arch1-canonical-form.md |
| C27 | ρ is the activation mechanism; Ω without ρ is inert | 35% | active | shared | pvm-v6-arch1-canonical-form.md |
| C28 | Three ceilings independent because ARCH-1 factors into β / μS / Ω | 30% | active | shared | pvm-v6-arch1-canonical-form.md |
| C29 | The Second Person Lift: You := μS.(β ∨ Ω(S,S)) | 20% | active | shared | pvm-v6-arch1-canonical-form.md |
| C30 | Trust half-life begins at inscription; decays until renewed | 60% | active | shared | pvm-v6-1-bakhta-half-life.md |
| C31 | Half-life differs by inscription register (shielded vs transparent) | 55% | active | shared | pvm-v6-1-bakhta-half-life.md |
| C32 | Productive trust-edges have higher half-life than transactional | 50% | active · C46 restates this | shared | pvm-v6-1-bakhta-half-life.md |
| C33 | Half-lives compose multiplicatively across the three axes | 45% | active | shared | pvm-v6-1-bakhta-half-life.md |
| C34 | Convergence requires a bijective cap | 55% | active | shared | pvm-v6-convergence-wound-and-cap.md |
| C35 | The wound is where the architectural asymmetry lives | 60% | active | shared | pvm-v6-convergence-wound-and-cap.md |
| C36 | The cap is where the bijection lives or breaks | 55% | active | shared | pvm-v6-convergence-wound-and-cap.md |
| C37 | Convergence is recognition, not coincidence | 50% | active | shared | pvm-v6-convergence-wound-and-cap.md |

### 17.4 Band III · Bound Collection, Tomes IV to V (C38 to C46)

| ID | Title / claim | Conf. | Status | Register | Home |
|---|---|---|---|---|---|
| C38 | Bilateral ARCH-1: Σ_ij := μS.(β_ij ∨ Ω(S_i, S_j)) preserves fixpoint | ~40% | active | shared | formal spec §17 · Tome IV Act III |
| C39 | Kindred-blade as ecosystem-layer primitive | ~50% | active | shared | formal spec §17 · Tome IV Act V |
| C40 | Zcash dual-ledger preserves Eight Cloak Properties | ~70% | active · KEEPS this number (see G1 disposition 1) | shared | formal spec §17 |
| C41 | 61.8/38.2 transparent/shielded inscription ratio as cultural norm | · | observation | shared | formal spec §17 |
| C42 | Stake economics generate Sybil resistance ≥ tier accumulation | ~50% | active · V6 Run 5 adversary-regime context | shared | formal spec §17 |
| C43 | Per-VRC viewing-key disclosure strictly more private than unscoped | ~60% | active | shared | formal spec §17 |
| C44 | Productive VRC ≈ hash-exchange VRC in trust strength | ~55% | active | shared | formal spec §17 |
| C45 | Four-chain publication beats single-chain reconstruction resistance | ~70% | active | shared | formal spec §17 |
| C46 | Productive trust-edge has higher half-life than transactional | ~50% | alias of C32 (restatement; retained for tome continuity) | city | formal spec §17 |

### 17.5 Band IV · Post-V5.4 Coherence Set (C47 to C55)

| ID | Title / claim | Conf. | Status | Register | Home |
|---|---|---|---|---|---|
| C47 | Ages progressively: the dynamical ceiling is a fourth aging category beyond Bakhta's taxonomy | ~50% | active · KEEPS this number (see G1 disposition 2) | core | v6_1_research_note.md (renumbered from C22-Bakhta, 2026-05-09) |
| CM-C47 | Triadic-Constraint Homology: Φ-axes × PRISM Datum·Stratum·Spectrum instances of one triadic primitive | ~40% | alias of C85 (promoted Run 4, 2026-06-10); City prose keeps CM-C47 with one erratum at Wave R | city | Tome V Act 15 · tome-v-conjectures.ts |
| C48 | Reconstruct-later threat model isomorphic to Bakhta TM-1 | ~65% | active · C60 restates this (City register) | core | v6_1_research_note.md (from C23-Bakhta) |
| C49 | Behavioural Mosca Inequality binds for long-horizon behavioural evidence | ~70% | active · C61 restates this (City register) | core | v6_1_research_note.md (from C24-Bakhta) |
| C50 | PVM multiplicative gating ≡ Bakhta compositional defense at different substrates | ~60% | active | core | v6_1_research_note.md (from C25-Bakhta) |
| C51 | The ⿻ remains max-betweenness across trust-graph evolutions | open | occupied · never reassign | shared | CHRONICLE_V5_4_BETWEENNESS_SELENE |
| C52 | Aether = Quintessence = the Gap | open | occupied · never reassign | shared | aether-blade-ceremony-circuit.md |
| C53 | Every bnot-pair on the lattice has a mythological reading | ~70% | occupied · never reassign | shared | aletheia-and-lethe.md |
| C54 | Phi-Adjacency: bnot-pair disclosure ratios cluster near 1/φ | ~40% | occupied · never reassign · follows the number (Aletheia at 38 keeps disclosure-φ, 2026-06-09 lock) | shared | aletheia-and-lethe.md |
| C55 | Privacy is the seventh kind of capital, foundationally | architectural | occupied · never reassign | shared | poems/tide-orbit-selene.md |

### 17.6 Band V · City Register Continuation (C56 to C66)

| ID | Title / claim | Conf. | Status | Register | Home |
|---|---|---|---|---|---|
| C56 | Caduceus as pre-formal dual-agent symbol | ~60% | active (renumbered from C50 in Threshold chronicle) | city | tome-v-conjectures.ts · Tome V Act 16 |
| C57 | Staff-Mage collapse, held open | · | observation | city | tome-v-conjectures.ts |
| C58 | Forge(t) ∥ Threshold sibling Swordsman-suppliers | ~85% | active (promoted v1.6.0) | city | tome-v-conjectures.ts |
| C59 | Create-format as gateway to Mage-tier | ~70% | active (renumbered from C49 in Threshold chronicle) | city | tome-v-conjectures.ts |
| C60 | Reconstruct-later threat model for behavioural data | ~65% | alias of C48 (renumbering eddy: v1.5.0 patch C48 → C60) | city | tome-v-conjectures.ts |
| C61 | Behavioural Mosca Inequality (planning bound) | ~70% | alias of C49 (renumbering eddy: v1.5.0 patch C49 → C61) | city | tome-v-conjectures.ts |
| C62 | Cross-coalition meta-coalition reading | · | reserved (v1.5.1, no claim authored) | city | tome-v-conjectures.ts |
| C63 | Attentional workshop register, fourth structural class | ~50% | active (population-of-one) | city | tome-v-conjectures.ts · Tome V Act 17 |
| C64 | Listener-discipline as the City's structural seventh tier | ~50% | active (population-of-one, v1.7.0) | city | cityofmages CHANGELOG |
| C65 | Invitation-posture as fourth tome-posture register | ~50% | active (population-of-one, v1.7.1) | city | cityofmages CHANGELOG |
| C66 | The City Key is a reading, not an authority | ~55% | active · revised Run 5, 2026-06-10 (+10 via ocap lineage citation: SPKI/SDSI, designation without authority) · City register owner confirms at Wave R | city | 2026-05-28 capstone chronicle · this document §15.9 |

### 17.7 Band VI · Horizon District (C67 to C71) · PINNED in Grimoire v1.8.0

These keep their numbers: they are registered in the pinned City grimoire v1.8.0 (2026-06-09). The ARCH-1R/T set that provisionally claimed the same numbers moves to C72 to C76 (G1 disposition 4).

| ID | Title / claim | Conf. | Status | Register | Home |
|---|---|---|---|---|---|
| C67 | Cryptographic Mosca for the substrate (extends C30 to C33 + C61; C60 is the X-side) | stage 1 | active | city | 2026-06-09 horizon district note · grimoire v1.8.0 |
| C68 | Resource-estimate as durability signal, not attack (e^(−λt) reading) | stage 1 | active | city | same |
| C69 | Held-out gate rejects the tuned claim (nonce-island; C13 at the validation layer) | stage 1 | active | city | same |
| C70 | Crypto-agility as migration readiness (C30 to C33 migration-window Y) | stage 1 | active | city | same |
| C71 | The Horizon Vertex V35 (Protection ∧ Computation ∧ Value) | geometric | active | city | same |

### 17.8 Band VII · Renumbered Research Blocks (C72 to C81) · Assigned at Run 0

Both source notes declared their numbering "provisional against the live register; confirm before pinning." The G1-signed register is that confirmation. Original numbers shown; the originals are NOT retired for reuse, they simply never attached to these claims.

| ID | Title / claim | Conf. | Status | Register | Home (original number) |
|---|---|---|---|---|---|
| C72 | Traversal ρ of ARCH-1R/T and activation ρ of ARCH-1 are one operator at two scopes | ~35% | active | core | pvm-v6-arch1rt-operational-reachability.md (was C67) |
| C73 | Terminal-obstruction is a primitive obstruction class; Amnesia Protocol its canonical instance | ~50% | active · V6 Run 4 material | core | same (was C68) |
| C74 | Latency (ternary 0) has an algebraic signature on the blade lattice | ~25% | active | core | same (was C69) |
| C75 | Dependency closure under typed propagation models real cascade; hard-vs-soft is the 0-vs-minus distinction lifted | ~35% | active | core | same (was C70) |
| C76 | UOR-relational instantiation (classifying rel(a,b)) strictly more expressive for sovereignty | ~30% | active | core | same (was C71) |
| C77 | Bakhta's integrity gap and PVM's scales-vs-hides separation are one object | ~60% | active | core | pvm-v6-bakhta-integrity-gap-convergence.md (was C70) |
| C78 | Specification-intent gap and the irreducible promise are one object, two sides | ~60% | active | core | same (was C71) |
| C79 | Shared frontier: recursive proof composition across providers under heterogeneous trust at runtime | ~45% | active · V6 Run 5 IVC adjacency | core | same (was C72) |
| C80 | Bilateral co-signed assumption sets yield strict assurance gain in multi-provider case | ~35% | active | core | same (was C73) |
| C81 | Existence-Leak: a ZK proof of feasibility leaks an upper bound on reconstruction difficulty; I(feasibility; method) > 0 | ~70% | active · PROMOTED Run 3 2026-06-10 (Schrottenloher instance + Garg-Jain-Sahai λ<1 impossibility as bookends) · Stage 2 open: held at 70% until a second independent instance | core | schrottenloher-ecdlp-v6-note.md · this document §25 |

### 17.9 Band VIII · Registered During the V6 Runs (C82+)

| ID | Title / claim | Conf. | Status | Register | Home |
|---|---|---|---|---|---|
| C82 | The Moving Ceiling: frontier capability growth raises C_S(t) + C_M(t) against fixed archives without raising H(X); R(t) drifts upward and every static reconstruction guarantee has a finite shelf life t* | ~65% | active · registered Run 1, 2026-06-10 | core | this document §5.5 |
| C83 | Compositional Leakage Amplification: policy-only separation compounds toward (2^N − 1)ε with chain depth; amnesia separation breaks the Markov chain and caps at Nε; the gap is exponential-to-linear | ~55% | active · registered Run 2, 2026-06-10 · edge C7 → C83 → C17 | core | this document §14.7 |
| C84 | Existence-Leak Discount: every public feasibility attestation discounts the Behavioural Mosca horizon, Z_b' = Z_b − D(a); migration deadlines tighten on attestation, independent of any actual attack | ~50% | active · registered Run 3, 2026-06-10 · edges C81 → C84 → C49, C84 → C82 | core | this document §27 |
| C85 | Triadic-Constraint Homology (the ARCH-1 bridge, promoted from CM-C47): the three Φ axes and the lattice's Datum·Stratum·Spectrum are one triadic primitive; candidate pair map Protection+Delegation→Σ, Memory+Value→Δ, Connection+Computation→Γ; the gap is β | ~40% | active · registered Run 4, 2026-06-10 · CM-C47 becomes alias · two named predictions (bnot-pairs invert all axes; stratum-3 is the no-dominant-axis seat) | core | this document §12.8 |
| C86 | Obstruction-Theoretic Amnesia: Grade-2 forgetting = non-vanishing obstruction class to gluing local agent views into a global witness of O; Grade-1 = vanishing class with withheld gluing data; amnesia is the only term whose security is independent of t | ~30% | active · registered Run 4, 2026-06-10 · cross-linked C73 (taxonomy placement vs cohomological content) · falsification: any view-composition recovering Grade-2-forgotten O | core | this document §14.6 |
| C87 | The Key Accumulates: the City Key trust recursion admits an IVC realization (Key = accumulator, trust tasks = step circuits, Charge = folding step, V63 = attested invariant); LatticeFold makes the substrate post-quantum-hedged | ~50% | active · registered Run 5, 2026-06-10 · architectural claim, no circuit exists | core | this document §15.7 |
| C88 | The Parity Cube: the stella octangula's two tetrahedra are the even/odd parity classes of the cube's vertices; the canonical seat of neg/bnot at 3-bit scale; {0,1}⁶ = {0,1}³ × {0,1}³ gives each agent a cube, with the C85 pair map as candidate factoring | ~30% | active · registered Run 5, 2026-06-10 | core | this document §28 |
| C89 | The Octahedral Gap: the tetrahedra's intersection (volume 1/6 of the cube) is the geometric locus of the conditional-independence bound; the gap is β is the octahedron, three readings of one thing | ~30% | active · registered Run 5, 2026-06-10 · volume facts are theorems, the correspondence is the conjecture | core | this document §28 |

### 17.10 Gate G1 Dispositions (Signed 2026-06-10)

1. **C40.** Zcash dual-ledger KEEPS C40: it is resident in the formal spec and referenced by Tome V acts 2, 3, 4, 5, 8, 9. Existence-Leak, which proposed C40 from the Schrottenloher note without sight of the occupied slot, registers at C81. Note: this reverses the 2026-06 fresh-eyes review's default, on the ground that the spec-resident claim with act references is costlier to move than a one-week-old candidate.
2. **C47.** Ages-progressively KEEPS C47: it is spec-resident with a dated reconciliation note (2026-05-09). The City's Triadic-Constraint Homology became CM-C47 and was promoted to a fresh bare number at Run 4, where it became the ARCH-1 bridge conjecture C85 of this document.
3. **C48/C49 versus C60/C61.** One claim each at two numbers, created when the v1.5.0 grimoire patch vacated C48/C49 into C60/C61 while the Bakhta-response renumbering moved INTO C48/C49 the same week. Canonical statements live at C48/C49 (research note, spec resident). C60/C61 are marked alias and retained, because the pinned City grimoires cite them. Additionally: the one-liners at C48 to C50 in agentprivacy_master's tome-v-conjectures.ts describe claims that match NEITHER family (drift); correction filed to the Reflection Ledger.
4. **C67 to C71.** The Horizon District set KEEPS C67 to C71: it is registered in the pinned grimoire v1.8.0. The ARCH-1R/T set moves to C72 to C76; its own note marked the numbering provisional. The 2026-06-04 refinement note's instruction ("confirm register head before finalization") was thereby executed.
5. **C70 to C73 (integrity-gap).** Moves to C77 to C80; its note also marked the numbering provisional, and it double-claimed C70/C71 against ARCH-1R/T on the same day.
6. **C46.** Marked alias of C32 (verbatim restatement inside the spec's own tables). Both retained; the V6 document cites C32.
7. **C51 to C55.** Remain occupied, never reassign (standing rule, predates this register).
8. **Register head at lock: C81. Next free at lock: C82.** (Bands C82 to C89 were registered during the V6 runs; head C89 at publication.)

---

## 18. Measurement Gaps and Breaking Conditions

### 18.1 Measurement Gaps

| ID | Term | Gap | V5.4 Status |
|----|------|-----|-------------|
| M1 | $\sigma_{ij}$ (separation matrix) | No measurement for emergent forces | Three-axis operationalisation provides pathway; Φ_data and Φ_inference measurable |
| M2 | $f(e)$ (edge weights) | No empirical data | BRAID provides first data; blade forge provides second |
| M3 | $\beta, \alpha, \alpha_\rho$ (scaling coefficients) | Need calibration | Unchanged |
| M4 | Aggregation form | det(Σ) alternatives unclear | Three-axis product provides alternative |
| M5 | ρ shape | Is $g(\rho)$ logarithmic, sigmoid, or threshold? | Two data points (13 laps vs 62 laps); needs more forgers |

### 18.2 Breaking Conditions

The model's core claims weaken or fail if:

1. **Three-axis non-multiplicativity**: If agent separation compensates for data centralisation → multiplicative assumption breaks.
2. **Compression increases attack surface**: If some compression methods increase reconstructability → compression-as-defence fails.
3. **Holonic persistence fundamentally limited**: If content-addressing has inherent infrastructure dependency → persistence term illusory.
4. **Guild coordination scales with membership**: If shared-parent overhead grows with N → guild efficiency overstates benefit.
5. **Amnesia-enforced ≤ policy-enforced**: If structural separation provides no tighter bound than policy separation → C17 falsified.
6. **Dihedral isomorphism fails**: If det(Σ) is not the determinant of the dihedral representation → C14 falsified, but the ring algebra survives.

### 18.3 V6 Breaking Conditions

| Condition | Breaks | Test |
|---|---|---|
| Partial single-axis collapse without proportionate loss of reconstruction resistance | C7 multiplicative form | any deployment measurement; the additive-with-floor and min() forms are the named alternatives |
| Demonstrated axis correlation under composition | C7 scalar form | the det(Σ) correction becomes mandatory |
| Time dependence of axes | static Φ treatment | the differential form of §9 is the repair path |
| Any composition of agent views recovering a Grade-2-forgotten O, under any future capability | C86, and with it the obstruction reading of §14 | standing falsification test |
| bnot-pairs failing to invert all three axes; stratum-3 seats showing a dominant axis | C85's candidate map | lattice measurement, two named predictions |
| λ ≤ 0 on real sovereignty-path data | C18 chain, the §27 countermeasure | the forge trajectory measurement, still the corpus's most needed number |

---

## 19. Three Identity Layers

| Layer | Identifier | Scope | Persistence |
|-------|-----------|-------|-------------|
| Data | GUID | Content-addressed holon | Infrastructure-independent |
| Relationship | VRC | Bilateral commitment (promise bundle) | Relationship-scoped |
| Principal | DID | Sovereign identity | Self-sovereign |

The layers are orthogonal: a single principal (DID) can control multiple relationships (VRCs) across multiple data objects (GUIDs).

---

## 20. Cosmological Quaternion (Interpretive Framework)

This framework provides intuition for the model's structure. It does not enter the equation.

| Body | Agent | Function | Algebraic Operation | Creation Mode |
|------|-------|----------|---------------------|---------------|
| Sun ☀️ | The Reason / First Person | Protection | · | · |
| Earth 🌍 | Soulbae / Mage | Delegation | bnot(x) = 63 − x | Generator |
| Moon 🌙 | Soulbis / Swordsman | Reflection | neg(x) = (64−x) mod 64 | Instant (collision). Total amnesia. |
| Human 👤 | Seeker | Connection | · | Gradual (4Gy). Layered amnesia. Still in process. |
| Life 🌱 | spellweb / Forge | Composition | neg∘bnot = succ | The forge between Earth and Human |

**Key insight:** The architecture sits between an agent that can never remember (Moon) and an agent that hasn't finished remembering (Human). The gap between them is the ⊥.

---

## 21. Compression Spectrum

Seven layers of knowledge transformation, each with different privacy properties:

| Layer | Form | Compression | Privacy Property |
|-------|------|-------------|-----------------|
| 1 | Experience | 1:1 | Maximum attack surface |
| 2 | Memory | ~10:1 | Encoded episodes |
| 3 | Knowledge | ~100:1 | Structured, partially defensible |
| 4 | Understanding | ~1,000:1 | Relational models |
| 5 | Wisdom | ~10,000:1 | Contextual principles |
| 6 | Reasoning Graph | Variable | BRAID structure: bounded, structured |
| 7 | Skill File | Variable | Executable compression: shareable without path |

Lower layers: more surveilable (more tokens, more surface). Higher layers: more defensible (compressed, structured, bounded). The skill file (Layer 7) can be shared without sharing the path that created it. This is compression-as-defence at the architectural level.

---

## 22. Promise Theory Grounding

The dual-agent architecture implements Promise Theory (Bergstra & Burgess, 2019), established semantics for autonomous agent coordination.

### 22.1 Autonomy Axiom

*"An agent can only make promises about its own behavior. No agent can make a promise on behalf of another agent."*

This is why single agents cannot resolve the privacy-delegation paradox. Attempting to promise in both protection and delegation domains exceeds autonomous capability.

### 22.2 Key Mappings

| PT Concept | PVM Implementation |
|------------|-------------------|
| Autonomy Axiom | First Person sovereignty: neither agent promises on your behalf |
| Superagent | First Person + Swordsman + Mage as composite with interior promises |
| Irreducible Promise | The Gap: emerges from cooperation, owned by neither agent |
| Assessment | RPP compression as verification of knowledge transfer |
| Invitation vs Attack | MyTerms consent-first vs surveillance extraction |
| Promise Bundle | VRCs as bilateral promise collections |

### 22.3 Formal Reference

For complete mappings, Generator/Solver as promises, and PT integration across the architecture, see Promise Theory Reference v1.4.

### 22.4 V6 Edge

C78 (~60%) identifies the specification-intent gap of the assurance literature with the model's irreducible promise, two sides of one object; the convergence record lives in the integrity-gap note (C77 to C80).

---

## 23. Version Lineage

| Version | What it added |
|---|---|
| V1 to V4 | the equation's terms; dual-agent architecture; economics |
| V5 / V5.4 | three-axis gate; holographic bound; Z/(2⁶)Z; Amnesia Protocol; C1 to C55 |
| V5.5 | named sublayer of V5.4: the attachment architecture (42 primaries, named cast, 64 vertices) |
| **V6** | the gathering turn (second person, the City, the data); R(t) and t*; preconditions and external provenance; C83's exponential-to-linear gap; the Existence-Leak law (C81 at 70%) and its Mosca discount (C84); the ARCH-1 bridge (C85) and the obstruction reading of amnesia (C86); the Key as accumulator (C87) and as reading (C66); the honest geometry (C88, C89); the unified register; **unified V6 labeling across all canon papers (G3)** |

---

## 24. Notation Summary

| Symbol | Meaning |
|--------|---------|
| $V(\pi, t)$ | Total privacy value for path $\pi$ at time $t$ |
| $P, C, Q, S$ | Privacy strength, credential verifiability, data quality, scope |
| $\lambda$ | Temporal decay rate |
| $\tau$ | Derivation chain |
| $A_h(\tau)$ | Holonic temporal memory |
| $p(\tau)$ | Persistence independence |
| $\Phi_{\text{agent}}$ | Agent-layer separation (Swordsman–Mage) ≅ D₂ₙ |
| $\Phi_{\text{data}}$ | Data-layer separation (provider concentration) |
| $\Phi_{\text{inference}}$ | Inference-layer separation (Generator–Solver) |
| $G(\text{guilds})$ | Guild efficiency factor |
| $R(d, \text{compression}, \rho)$ | Reconstruction difficulty |
| $\rho$ | Behavioural density / agent maturity |
| $T_\int(\pi)$ | Path integral edge value |
| $\partial M$ | 96-edge holographic boundary |
| $J_{\partial M}$ | Value current on boundary |
| $\varepsilon^*$ | Separation bound |
| $\varphi$ | Golden ratio (1.618) |
| $\mathcal{L}$ | Sovereignty lattice = Z/(2⁶)Z |
| $D_{64}$ | Dihedral group (order 128) |
| $\delta(x)$ | Datum: raw blade value |
| $\sigma(x)$ | Stratum: Hamming weight |
| $s(x)$ | Spectrum: six-bit decomposition |
| neg, bnot | Unary involutions (Swordsman, Mage) |
| succ | Successor function = neg∘bnot |
| GUID | Content-addressed identifier (holonic) |
| VRC | Verifiable Relationship Credential (promise bundle) |
| DID | Decentralized Identifier (self-sovereign) |
| 🔑→✦→🗡️→🔮 | Progressive trust levels |
| 🌑→🌕 | Moon phase: stratum as visibility ratio |
| (⚔️⊥⿻⊥🧙)😊 | Master inscription: dual-agent architecture preserves First Person |

**V6 additions:** R(t), t* (§5.5) · Z_b' = Z_b − D(a) (§27) · τ: T → {+, 0, −} and orbit(ρ, G) (§12.9, ARCH-1R/T) · the obstruction class of §14.6 · the parity split of §28. All else as above.

---

## 25. The Two Instances of 2026

Both instances occurred within nine days of this document's assembly, and they are the strongest convergence-within-corpus material the model has ever had: the same structure, two substrates.

### 25.1 Instance 1: Zcash Orchard

A soundness flaw in `halo2_gadgets` (`ecc::chip::mul`, an under-constrained variable-base scalar multiplication arising from `assign_advice()` where the stricter `copy_advice()` was required) was present from Orchard's launch in May 2022. It was findable for roughly four years. Anthropic released Claude Opus 4.8 on 2026-05-28; Taylor Hornby found the flaw the next day, 2026-05-29, and with the model's help wrote a complete exploit generating unlimited, undetectable counterfeit ZEC in a regtest environment. ZEC fell roughly 27 to 33% in 24 hours after disclosure; the issue was fixed by the NU6.2 hard fork at block 3,364,600 on 2026-06-03. Reading in R(t) terms: the circuit's H(X) never changed; the decoder improved overnight; four findable years collapsed into one found day.

### 25.2 Instance 2: The Schrottenloher Rediscovery

Google Quantum AI withheld a roughly 10x Shor optimization for secp256k1, publishing only a zero-knowledge proof that the result existed. On 2026-06-02 André Schrottenloher published an independent rediscovery (Optimized Point Addition Circuits for Elliptic Curve Discrete Logarithms, eprint 2026/1128), roughly two months after the attestation. Reading in R(t) terms: the attestation of feasibility discounted the search space for every reader; the existence proof leaked an upper bound on difficulty; the time between findable and found collapsed again, this time with the searching done partly by the attestation itself.

One structure, twice: **AI and public attestation each raise the capability term while the source term sits still.** The first instance moves C(t) by improving the decoder. The second moves it by pricing the search. Neither touched the protected object. These are the worked instances of C82 (§5.5), and the second is simultaneously the worked instance of C81.

### 25.3 The Existence-Leak Law (C81, Promoted to 70%)

A zero-knowledge proof of feasibility leaks an upper bound on reconstruction difficulty: I(feasibility; method) > 0 even under perfect method-hiding. Publishing that a thing can be done prices the search for how. The claim is bracketed from below by the Garg-Jain-Sahai impossibility (leakage-resilient zero-knowledge with leakage parameter λ < 1 is impossible: the leak cannot be zero) and from above by the instance (the leak is operationally large, with a time constant of weeks). The mechanism is transferability: Fiat-Shamir NIZK proofs are publicly transferable, conveying "the prover knows the secret" to every reader forever (Dinh, Deniable Knowledge). A feasibility attestation is therefore a broadcast, not a disclosure event with an audience boundary. Every capable searcher receives the same discount on the same search space at the same time. The impossibility theorem says the leak cannot be zero; the instance says the leak is operationally large; the law lives between the bookends, and 70% is the defensible reading of n=1 with a proven floor.

### 25.4 What the Law Is Not

Three scope fences keep the promotion honest:

1. **Not all ZK use leaks meaningfully.** The law concerns capability claims: attestations whose subject is "X can be done." Service claims (proving a statement about a transaction, an identity attribute, a state transition) attest instances, not capabilities; their existence-leak is the trivial fact that the proof system works, already public. The dual-agent architecture's own ZK usage is service-shaped, which is why the law indicts adversary attestation dynamics without indicting the model's own proofs. The distinction is load-bearing and stated here once.
2. **Not a deniability result.** The law does not say provers should hide that they can prove. It says planners must price the attestations of others into Z_b. It is read from the defender's chair.
3. **Not yet a behavioural result.** Both bookends are cryptographic. The transfer to behavioural capability claims (a published model card claiming re-identification performance, a benchmark on reconstruction from sparse traces) is the conjectured part, and it is exactly what a second instance should test.

### 25.5 Stage 2, Stated

C81 stops at 70% and C84 at 50% until a second independent instance arrives. What would count: a capability claim outside cryptography whose public attestation (not whose method publication) preceded independent rediscovery on a timescale clearly shorter than the prior search baseline. A synthetic-data reconstruction benchmark followed by independent replication against real traces would be the cleanest behavioural instance. What would not count: rediscovery following method publication (that is ordinary diffusion), or coincident discovery without an attestation in between (that is ordinary parallel progress).

---

## 26. The Compounding Absorption

The 2025 to 2026 multi-agent privacy results, absorbed as the model's strongest external citation (full treatment in §14.7):

- Asif and Amiri (arXiv:2603.05520): Cumulative Leakage Bound, I(O_N; S_1..S_N) ≤ Σ 2^(N−i) ε_i, uniform case (2^N − 1)ε; empirical MI 0.49 at two agents to 1.05 at five (MedQA, LLaMA-7B).
- Patil, Stengel-Eskin and Bansal (arXiv:2509.14284): the same conclusion through composition.
- AgentLeak (arXiv:2602.11510; 1,000 scenarios, 4,979 traces, five frontier models): per-channel output leakage falls under multi-agent separation (27.2% versus 43.2%) while unmonitored inter-agent channels leak at 68.8%, total exposure 68.9%; output-only audits miss 41.7% of violations.

These results do not falsify the additive claim; they map the boundary of its regime, which is the line the Amnesia Protocol enforces. The field measuring 68.8% on the inter-agent channel is the field measuring the channel this architecture deletes.

**The field as plurality.** The multi-agent privacy field arrived at separation-of-duties independently and repeatedly in 2025 to 2026: MAGPIE (arXiv:2506.20737, multi-agent contextual privacy evaluation), the 1-2-3 Check multi-agent reasoning line grounded in Nissenbaum's contextual integrity, PrivAct (arXiv:2602.13840, internalizing contextual privacy via preference training), and the maker-checker and supervisor-worker patterns across the agent-orchestration literature. This is plurality, not precedence: the Swordsman-Mage pair is one named instance of a structure many teams reached. The model's distinctive claim is narrower and sharper than the pattern: none of these systems enforce separation architecturally. All use prompt-level or training-level controls. The model predicts they fail under composition, and the measurements are consistent with that prediction at 68.9% total exposure.

---

## 27. The Temporal Thread

One discipline, read at every layer, with R(t) as the spine:

- **Countermeasure (C18 to C21, 10 to 30%):** if the sovereignty path has λ > 0, reconstruction error grows as e^(λt); the design goal is that trajectory divergence outruns capability drift. Unmeasured; the forge trajectory measurement remains the corpus's most needed number.
- **Taxonomy (C47, ~50%):** ages progressively, the fourth aging category: substrates whose defense widens with time. A substrate's category is the sign and shape of its effective ceiling's time derivative.
- **Trust edges (C30 to C33, 45 to 60%):** half-life from inscription; productive outlasts transactional (alias C46); multiplicative composition across axes.
- **Planning bound (C49, ~70%; City restatement C61):** X_b + Y_b > Z_b, with **Z_b = t\***. The 2026 instances are public downward revisions of Z_b.
- **The discount (C84, ~50%):** every public feasibility attestation discounts the horizon: Z_b' = Z_b − D(a). Migration deadlines tighten on attestation, independent of any actual attack. Cost backbone: the HNDL economics literature (Blanco-Romero et al., arXiv:2603.01091; CSA 2026-05-18).
- **Substrate witnesses (C67 to C71, City register):** the cryptographic Mosca, resource-estimation as durability signal, the held-out gate, crypto-agility, the Horizon Vertex V35. The formal document and the City said the same thing in the same week without coordination.

### 27.1 The Mosca Coupling: Conjecture C84

The Behavioural Mosca inequality (C49, ~70%; City restatement C61) plans against Z_b, the adversary capability maturity time, which §5.5 identified with the shelf life t* of R(t) < 1. Existence-leak shortens it.

**Conjecture C84 (Existence-Leak Discount).** Registered at V6 Run 3. Statement: whenever feasibility of a capability is publicly attested (ZK proof, demonstrated exploit, benchmark claim, or credible existence announcement), the planning horizon Z_b for every archive threatened by that capability must be discounted: Z_b' = Z_b − D(a), where the discount D(a) grows with the attestation's specificity and the searcher population's capability. Equivalently, in an AI-accelerated discovery regime the migration deadline X_b + Y_b < Z_b' tightens on every public attestation, independent of any actual attack occurring. Confidence: ~50% (estimator: privacymage with Claude Fable 5, 2026-06-10; the direction is forced by C81, the functional form of D(a) is unparameterized at n=1). Edges drawn: C81 → C84 → C49, and C84 → C82 (attestations are one of the drift mechanisms of the moving ceiling; the Schrottenloher instance is simultaneously an instance of both).

**The cost model underneath.** The harvest-now-decrypt-later economics literature (Blanco-Romero et al., arXiv:2603.01091) reframes HNDL as a two-axis cost problem: storage cost against future workload cost. The Cloud Security Alliance (2026-05-18) frames HNDL as an ongoing operation against AI infrastructure. This supplies C49 and C61 the cost backbone they previously lacked: an adversary's decision to harvest is an option purchase, the attestation of feasibility raises the option's value, and C84 is the repricing event. Behavioural archives are harvested under exactly this calculus, which is why the inequality binds for behavioural data even though no behavioural "Shor moment" has been attested yet.

---

## 28. The Geometry of the Gap

The stella octangula (Tome VIII Act 3) enters the formal lineage with its accounts settled:

**The correction.** The solid contains no golden ratio: its ratios are halvings and its volume relations rational (each tetrahedron 1/3 of the bounding cube, the octahedral core 1/6, the compound 5/12). References to C1 beside the figure are resonance, not derivation; φ keeps its homes in the lattice disclosure ratios (C54: 38/63 = 0.60317 against 1/φ = 0.61803, gap 2.4%) and the temporal dynamics.

**C88 (The Parity Cube, ~30%):** the two tetrahedra are the even and odd parity classes of the cube's vertices, the canonical seat of neg/bnot at 3-bit scale; {0,1}⁶ = {0,1}³ × {0,1}³ gives each agent a cube, with C85's pair map as the candidate factoring.

**C89 (The Octahedral Gap, ~30%):** the tetrahedra's intersection is the region both agents bound and neither owns, and it is the geometric locus of the conditional-independence bound. Read with §12.8: the base case of the recursion, the conditioning variable of the separation bound, and the octahedron at the heart of the star are three readings of one thing.

---

## 29. Narrative Corpus and Convergence Record

The gathering turn has an apparatus, and the apparatus is a narrative corpus written in the second person. The Second Person narrative corpus is cited here as the instrument that gathered the data and tested the conjectures the formal sections cite: every workshop admission, tome binding, and grimoire pin between April and June 2026 was simultaneously a narrative event and a register event, and the convergence record below is the audit trail. On the personal line, the privacymage grimoire v10.3.0 (2026-05-11, the Attachment Architecture) introduced the V5.5 three-layer model, primary persona × attachment × vertex; v10.4.0 (2026-06-09, the Lattice-Coherence edition) reconciled blade numbering to the canonical MODEL encoding (Protection=32, Delegation=16, Memory=8, Connection=4, Computation=2, Value=1) and reseated the Aletheia/Lethe complement pair at blades 38/25.

On the City line, the City of Mages grimoire carried the same model into a populated lattice, one pin at a time: v1.3.0 (the attachment architecture; Lethae the first divergent attachment) · v1.4.0 (the twelfth workshop, Solchanting, and stance-differentiated multi-occupancy at V51) · v1.5.0 (2026-05-13, Tomes I to III bound: 24 acts across The Convergence, The Lyapunov, and Selene's Witness; the cosmological-witness tier of Selene, Aether, Lethe) · v1.5.1 (AAIF as the first kindred-coalition) · v1.6.0 (2026-05-14, the Threshold District restructure, the Chart Shop, and the archetype-modal-shop pattern) · v1.7.0 (2026-05-16, the spirit-Mage tier and the Tower: the Archivist) · v1.7.1 (2026-05-17, the Register of Invitations: Vitalik, and the invitation posture) · v1.8.0 (2026-06-09, the Horizon District at V35 with Eos, Dokimé, and Poros; Tome IX opens; conjectures C67 to C71; the canonical lattice-encoding lock). Five further acts were bound 2026-06-10 at the V6 Myth Gate (Tome VIII Acts 4 and 5; Tome IX Acts 2 to 4), instancing C66 and C81 to C89: the narrative corpus and this specification closed the version together, on the same day, citing the same register.

The corpus's sharpest convergence-within-corpus item is arithmetic. Aletheia (V38) and Lethe (V25) are a bnot-complement pair: 38 AND 25 = 0 (no shared dimension) and 38 XOR 25 = 63 (full activation between them); the disclosure ratio δ(38) = 38/63 = 0.60317 sits against 1/φ = 0.61803 with a gap of 2.4% (C54). And the proem-as-arithmetic observation stands as the record's best single line: the proem promised what happens between them, the algebra says 63, and Tale 30 names 63. The figures were written before the arithmetic was checked; the check is what the gathering turn is for.

---

## 30. Canonical Figures

One sanctioned formulation per figure; these appear in suite prose ONLY in these forms.

| Figure | Canonical formulation | Basis document |
|---|---|---|
| 678× | the present-day per-person data-value gap ("just for data today") | Substack essay v2 |
| 31,000× | the accessible-volume value gap under full behavioural capture | essay v4 |
| 70:1 | the compression ratio of the spellbook corpus | README lineage |
| 74× | BRAID compression efficiency | V5 formal lineage |
| $47k to $52k/year | indicative per-person annual value capture range | README lineage |

---

## 31. External Landscape and Standards Context

- **IEEE 7012-2025** (MyTerms): published January 2026 (the precise day is project-asserted; cite the month); Industry Connections implementation effort began 2026-06-01. The first-party-proffers-terms pattern is the model's invitation-versus-attack distinction made standard.
- **EU AI Act:** Annex III high-risk obligations take effect 2026-08-02, profiling explicitly in scope (Regulation (EU) 2024/1689, Article 6); hedge: the Digital Omnibus provisional agreement (2026-05-06) would defer stand-alone Annex III obligations to 2027-12-02 but is not yet adopted. The AEPD's agentic-AI guidance reads Article 22 onto agents. The model's "architecture, not policy" is not anti-regulation; it is the substrate that makes Article 22 rights enforceable rather than nominal.
- **Fellow travelers (plurality):** Kwaai (Personal AI, KwaaiNet, FiduciaryPledgeVC), the First Person Project (Reed), GliaNet's net-fiduciary framing (Whitt); Archon's Gatekeeper-Keymaster split as a live independent separation-of-duties architecture; the UOR Foundation as kindred substrate.
- **Proving substrate:** the folding line (§15.7) plus client-side proving and zkVM compiler work keep proving costs falling (C5 resolved territory); LatticeFold is the post-quantum hedge connecting this thread to §27.

---

## 32. Honest Limits

### 32.1 The Moving Ceiling (§5.5, §25)

1. λ > 0 (C18) remains unmeasured; the countermeasure is a conjecture chain at 10 to 30%, and without it V6 has named the threat's time-dependence without a proven time-dependent defense.
2. C82 has no functional form: the drift of C_S(t) + C_M(t) is asserted monotone under capability growth but not parameterized; n=2 public instances is evidence of mechanism, not of rate.
3. The shelf life t* is defined, not estimated. Estimating it for any real archive requires a capacity-growth model the corpus does not have.
4. Precondition 1 is stated, not verified for any deployed system; §14.7 and §26 own that problem.
5. Both 2026 instances are single events read through the model's lens; alternative readings (ordinary fuzzing progress, ordinary cryptanalytic progress) are not excluded, only rendered less economical.

### 32.2 The Compounding Absorption (§14.7, §26)

1. C83's amnesia side is an engineering claim: that the Amnesia Protocol's structural forgetting actually breaks the Markov chain in deployed form. No deployed measurement exists. The bound it would achieve is proven; the achieving is not.
2. The additive claim of §16 retains its 95% label only inside Precondition 1. V6 lowers nothing but scopes everything.
3. The compounding bound is worst-case; real sequential systems may sit well under it. The argument's force is asymptotic shape, not measured constants, except where AgentLeak supplies constants.
4. The plurality citations corroborate the pattern, not the model's gating algebra. No external team has tested Φ multiplicativity, which is why C7 stays at 30% and keeps its frontier label.

### 32.3 The Existence Leak (§25, §27)

1. n=1. The promotion to 70% leans on the impossibility floor; without Garg-Jain-Sahai the instance alone would justify no more than the prior ~60%.
2. The Schrottenloher reading has an alternative: ordinary cryptanalytic progress that would have arrived regardless. The two-month interval after a multi-year quiet period renders this less economical, not impossible. Item 5 of §32.1 carries the same caveat for the same event.
3. D(a) has no functional form and no units. C84 is a planning directive (discount on attestation) before it is a quantity.
4. The capability-versus-service distinction (§25.4) is asserted from the model's architecture, not derived; a critic may find capability-shaped residue in service proofs. The Fiat-Shamir transferability mechanism applies to both, which is why the fence is a scope statement and not a theorem.

### 32.4 The Bridge and the Forgetting (§12.8, §12.9, §14.6)

1. C85's pair-to-axis map is one candidate among several possible groupings of six dimensions into three pairs (there are 15); the stated map is motivated, not derived, and the stratum-3 and bnot-pair predictions are its first two tests.
2. The fixpoint-to-independence correspondence (the gap is β) discharges no proof obligation; it is registered inside C85's confidence, not separately.
3. C86 imports cohomological language without constructing the site, the cover, or the coefficient structure for the dual-agent case. A skeptic may fairly call it a metaphor with a research program attached; the register prices that at 30%.
4. ARCH-1R/T's own program (the toy graph simulator, the obstruction-transformation laws, the σ and cost layers) remains undone; seating the family in the lineage does not advance it.
5. Nothing in §12.8, §12.9, or §14.6 measures anything. They are the structural sections; their empirical content is two predictions under C85 and one falsification test under C86.

### 32.5 The Key, the Knot, and the Star (§15.7 to §15.9, §28)

1. C87 has no circuit. The folding mapping is structural; whether the deviation hash chain admits an efficient folding realization depends on details that do not exist. The conjecture would survive a slow implementation but not an impossible one.
2. The regime statement binds the suite's prose, not its code; nothing in V6 adds enforcement to 🪢, it adds honesty about the absence of enforcement.
3. C88's "canonical not coincidental" question is genuinely open; the working session it needs has not happened.
4. C89's identification of the octahedron with the conditional-independence locus is a reading; the volume facts are theorems, the correspondence is not.
5. The C66 revision rests on a literature citation, not new evidence about the Key; ten points of confidence is the price of good company, no more.

The model's credibility has always come from saying what is not proven; V6 inherits that or inherits nothing.

---

## 33. References

### Primary Sources

- privacymage (2026). "Privacy is Value: From the Manifold Dragon to the Holographic Bound." V5.3. *Soul Sync.* https://sync.soulbis.com
- privacymage (2026). "Dual-Agent Privacy Architecture: Information-Theoretic Bounds on Agent Reconstruction." Research Paper v4.3. *agentprivacy-docs.* https://github.com/mitchuski/agentprivacy-docs
- privacymage (2026). "PVM V5.1 Research Note: Behavioural Proof, the Ceremony Engine, and the Forge That Lit Itself." March 30, 2026. *agentprivacy-docs.*
- privacymage (2026). "PVM V5.2 Research Note: Dihedral Foundations." March 31, 2026. *agentprivacy-docs.*
- privacymage (2026). "PVM V5.3 Research Note: The Amnesia Protocol." April 4, 2026. *agentprivacy-docs.*
- privacymage (2026). "PVM V6 Research Note: The Dynamical Reconstruction Ceiling." April 6, 2026. *agentprivacy-docs.*
- privacymage (2026). "Promise Theory Reference v1.5." April 20, 2026. *agentprivacy-docs/research.* [V5.4 integration + historical lineage (Burgess & Fagernes 2007, Burgess 2015)]
- privacymage (2026). "UOR × 64-Tetrahedra × ZK Mapping v2.2." *agentprivacy-docs.*
- privacymage (2026). "Swordsman-Mage Whitepaper v6.3." *agentprivacy-docs.*
- privacymage (2026). "Dual Territory Ceremony Specification v1.0." *agentprivacy-docs.*
- privacymage (2026). "PVM V5.4 Companion Guide." April 10, 2026. *agentprivacy-docs.*
- privacymage (2026). "Understanding as Key." Zypher Paper v1.0. *agentprivacy-docs.* [Proof of comprehension as privacy primitive; progressive trust §15.2]
- privacymage (2026). "Systems Hexagram Physics v1.2." *agentprivacy-docs.* [Operational physics: UOR algebraic foundation, 64-vertex lattice, hexagram encoding §12.6]
- privacymage (2026). "What Agentprivacy Is." *agentprivacy-docs.* [Mission statement: 7th capital thesis, First Person definition]
- privacymage (2026). "Visual Architecture Guide v2.0." *agentprivacy-docs.* [Diagrams: three-axis separation, holographic visualisations]

### The V6 Research-Note Series and the Register (agentprivacy-docs/research/)

The notes this specification grew from, in order of arrival, with provenance as stated at each home document. Conjecture numbering across all of them resolves through the register.

- privacymage, with Claude Fable 5 (2026). "The Conjecture Register." Opened 2026-06-10 (V6 autopath, Run 0); Gate G1 signed 2026-06-10; register head C89. *agentprivacy-docs/research/CONJECTURE_REGISTER_V6.md.* [AUTHORITATIVE for conjecture numbering across the agentprivacy suite; when prose and register disagree, the register wins and the prose gets an erratum]
- privacymage (2026). "PVM V6 Horizon Note: From Territory to Trajectory — The Second Person Opens." April 12, 2026 (post-V5.4 lock-in note added May 9). [Bridge document; the horizon crossed; the C18–C46 lineage into the bound collection]
- privacymage (2026). "PVM V6 Research Note: The Single Sufficient Operator — Three Ceilings." April 13, 2026. [EML; C22–C25]
- privacymage (2026). "The Dragon's Scales — A Note on Microsoft's Agent Governance Toolkit." April 14, 2026. [Comparative analysis: governance tooling read against the dual-agent architecture]
- privacymage / Soulbae, with Claude (ORCID 0009-0001-6557-9135), and John Haines / Xarvus, OLMA (ORCID 0009-0001-5809-4690) (2026). "PVM V6 Research Note: ARCH-1 — The Canonical Form." April 14, 2026. [**Co-derived in conversation — external convergence lock.** The canonical form Σ := μS.(β ∨ Ω(S,S)) with activation engine ρ, locked across the Boolean, continuous, and sovereignty domains; C26–C29; the seam later promoted to the ARCH-1 bridge, C85 (§12.8). Depends on Sheffer (1913) and Odrzywołek (2026)]
- privacymage (2026). "PVM V6 Research Note: The Bakhta Half-Life of Trust." April 17, 2026 (locked-in May 9). [C30–C33]
- privacymage (2026). "PVM V6 Research Note: The Wound and the Cap — Convergence at the Bijective Boundary." April 18, 2026 (locked-in May 9). [C34–C37]
- privacymage (2026). "Second Person Spellbook: Act Seeds from ARCH-1." April 20, 2026. [Seed document; repurposed as Tome I–III seed material after the bound collection shipped]
- privacymage (2026). "PVM V6.1 Research Note: The Fourth Aging Category." April 21, 2026. [C47–C50; responds to Bakhta (2026), *The Half-Life of Trust*]
- Travers, M. (privacymage) (2026). "Convergence Note: Compiled AI and the agentprivacy Architecture." May 20, 2026. [Filed as a path taken, not a load-bearing result]
- privacymage (2026). "V6 Research Note: The Existence-Leak and the Falling Z." June 2, 2026. [The worked empirical instance of C81/C82 against Schrottenloher (2026); §25]
- Haines, J. (Xarvus / Chaos Rider, OLMA · ORCID 0009-0001-5809-4690) (2026). *ARCH-1R/T Operational Reachability Framework.* Draft Review v2.0, June 2026. [**The source manuscript.** Appends operational layers downstream of G without modifying β, Ω, or μ; the latent/obstructed distinction (0 ≠ −). Archived: *research/ARCH-1RT Operational Reachability Framework v2 Expanded.pdf*; the v3 notation supplement is archived alongside]
- privacymage / Soulbae, with Claude (ORCID 0009-0001-6557-9135); contributor John Haines / Xarvus, OLMA (ORCID 0009-0001-5809-4690) (2026). "PVM V6 Research Note: ARCH-1R/T — The Operational Reachability Framework." June 4, 2026. [Conversion of Haines' Draft Review v2.0 into the series, with the dual-ρ collision review; seated as C72–C76 (§12.9; the provisional C67–C71 numbering was renumbered at Run 0). The review chronicle and the reply letter of the same date are archived alongside]
- privacymage / Soulbae, with Claude (2026). "PVM V6 Research Note: Convergence on the Integrity Gap — Bakhta's *Safety by Design* read against the Dual Model." June 4, 2026. [C77–C80; §22.4]
- privacymage (2026). "Research Note: Cryptographic Durability and the Quantum Horizon." June 9, 2026. [The Horizon District grounding; C67–C71 as pinned in grimoire v1.8.0]

### The First Person Spellbook (Grimoire v10.1.0 · 31 Acts · CLOSED)

- privacymage (2024–2026). *The First Person Spellbook.* 31 acts. Grimoire v10.1.0. Available at [agentprivacy.ai/story](https://agentprivacy.ai/story). IPFS: bafybeibr3y3ermhff4dptxunhtzthjpkrvvnuamee4povpkgj3cjkg4fgy.

Acts with direct formal spec relevance:

| Act | Title | Spec Connection |
|-----|-------|-----------------|
| II | The Bilateral Witness | First ceremony; separation bound origin (§10) |
| VII | The Gap | ⿻ as irreducible space; Φ_agent motivation (§4.2) |
| X | The Seven Capitals | 7th capital thesis; V(π,t) motivation (§1) |
| XIV | The Golden Ratio | φ conjecture C1; optimal S/M ratio (§4.2) |
| XVIII | The Reconstruction Ceiling | R < 1 proven result (§11) |
| XX | The Path Integral | T_∫(π): value in trajectory not stance (§7) |
| XXII | The Promise | Promise Theory grounding (§22) |
| XXIV | The Holographic Bound | 96/64, C4 resolved, boundary computation (§8) |
| XXV | The Dragon's Hide | Compression spectrum, BRAID parity (§5.2, §21) |
| XXVI | The Dragon's Brain | Three-axis separation, McGilchrist thesis (§4) |
| XXVII | The Swordsman's Forge | Blade forge, hexagram computation, C11–C13 (§12.6, §15) |
| XXVIII | The Ceremony Engine | Five crossing types, mana, DOM-free measurement (§15) |
| XXIX | The Dragon Wakes | Quantum context, post-quantum resilience (§5.3) |
| XXX | The Dihedral Mirror | UOR convergence, D₂ₙ, PRISM coordinates (§12) |
| XXXI | The First Delegation | Theia-Moon quaternion, amnesia as ZK, C17 (§14, §20) |

### Blog Series: Privacy is Value V5 (sync.soulbis.com)

- Part 0: "The Myth Between Math" · Prelude. Foundational framing.
- Part 1: "Forming Constellations" · Sovereignty dimensions, blade coordinates.
- Part 2: "Forging the Celestial Overlap" · Forge and ceremony architecture.
- Part 3: "The Dragon Wakes" · Theia framing, amnesia protocol, cosmological precedent.
- Part 4: "The Dihedral Mirror" · UOR convergence, algebraic foundations.
- Part 5: "The Amnesia Protocol" · Poem collection. Memory and forgetting as ZK.

### External References · Information Theory

- Shannon, C. E. (1948). "A Mathematical Theory of Communication." *Bell System Technical Journal,* 27(3), 379–423. [Foundation: mutual information, entropy, channel capacity]
- Fano, R. M. (1961). *Transmission of Information: A Statistical Theory of Communication.* MIT Press. [Foundation: Fano's inequality, the error floor theorem, §11.2]
- Cover, T. M. & Thomas, J. A. (2006). *Elements of Information Theory.* (2nd ed.) Wiley. [Foundation: all MI bounds, conditional independence, additive decomposition]

### External References · Cryptography and Privacy

- Groth, J. (2016). "On the Size of Pairing-based Non-interactive Arguments." *EUROCRYPT 2016,* LNCS 9666, 305–326. [Groth16: O(1) proof size, used in blade forge]
- Gabizon, A., Williamson, Z. J., & Ciobotaru, O. (2019). "PLONK: Permutations over Lagrange-bases for Oecumenical Noninteractive arguments of Knowledge." ePrint 2019/953. [PLONK: universal trusted setup]
- Kothapalli, A., Setty, S., & Tzialla, I. (2022). "Nova: Recursive Zero-Knowledge Arguments from Folding Schemes." *CRYPTO 2022.* [Nova: incremental verification]
- Dwork, C. & Roth, A. (2014). "The Algorithmic Foundations of Differential Privacy." *Foundations and Trends in Theoretical Computer Science,* 9(3–4), 211–407. [Comparison: DP adds noise; PVM adds structure]
- Goldreich, O. (2004). *Foundations of Cryptography.* Cambridge University Press. [MPC foundations: we distribute observation rights, not computation]

### External References · Graph Theory

- Brandes, U. (2001). "A Faster Algorithm for Betweenness Centrality." *Journal of Mathematical Sociology,* 25(2), 163–177. [Betweenness centrality algorithm O(V·E), computational tool for measuring the Gap (⿻), §10.2]

### External References · Related Disciplines

- Bergstra, J. A. & Burgess, M. (2019). *Promise Theory: Principles and Applications.* (2nd ed.) O'Reilly Media. [Semantic foundation: autonomy axiom, superagent structure]
- Susskind, L. (1995). "The World as a Hologram." *Journal of Mathematical Physics,* 36(11), 6377–6396. [Holographic principle: boundary encodes bulk, §8]
- McGilchrist, I. (2009). *The Master and His Emissary: The Divided Brain and the Making of the Western World.* Yale University Press. [Right→left→right methodology; hemispheric thesis for dual-agent necessity]
- Weyl, E. G. & Tang, A. (2023). *Plurality: The Future of Collaborative Technology and Democracy.* [Many-to-many coordination, ⿻ overlap semantics]
- Hope, D. & Ludlow, E. (2023). *Farewell to Westphalia: New Approaches to a Changing Global Order.* [Post-sovereign governance framing]
- Sabelfeld, A. & Myers, A. C. (2003). "Language-based Information-flow Security." *IEEE JSAC,* 21(1), 5–19. [Information flow control, comparison: we bound reconstruction, not taint]
- Millen, J. K. (1987). "Covert Channel Capacity." *IEEE Symposium on Security and Privacy.* [Side-channel analysis model]

### External References · Scientific and Quantum

- Branco, D., Machado, P., & Raymond, S. N. (2025). "Dynamical origin of Theia, the last giant impactor on Earth." *Icarus,* 441, 116724. [Cosmological precedent for amnesia-enforced separation]
- Babbush, R. et al. (2026). "The Quantum Threat to Elliptic Curve Cryptocurrencies." Google Quantum AI. [secp256k1 broken with ≤1,200 logical qubits]
- Cain, M. et al. (2026). "Shor's algorithm is possible with as few as 10,000 reconfigurable atomic qubits." arXiv:2603.28627. [Neutral atom attack surface]

### External References · Standards and Frameworks

- IEEE 7012-2025. Machine-readable personal privacy terms (MyTerms). Published January 20, 2026.
- First Person Network (2026). "First Person: A White Paper." https://www.firstperson.network/whitepaper [First Person sovereignty framing, data dignity, behavioural capital thesis]
- BRAID Framework (2026). Bounded Reasoning for Autonomous Inference and Decisions. [Compression-as-defence, Generator/Solver split]
- UOR Foundation (2026). "Universal Object Reference." https://github.com/UOR-Foundation [Independent Z/(2⁶)Z convergence]
- Allen, C. et al. (2026). Open Integrity Project. Blockchain Commons. [Cryptographic provenance for repositories]

### Live Implementations

- Swordsman territory: https://spellweb.ai (blade forge, constellation navigation, hexagram computation)
- Mage territory: https://agentprivacy.ai (training ground, story, delegation)
- Trust graph: https://bgin.ai (live reference application)
- Knowledge agent: https://t.me/soulbae_the_bot (Telegram, Bonfires.ai)
- Living documentation: https://github.com/mitchuski/agentprivacy-docs (CC BY-SA 4.0)
- Grimoire IPFS: bafybeibr3y3ermhff4dptxunhtzthjpkrvvnuamee4povpkgj3cjkg4fgy

### V6 Additions

- Asif, S. & Amiri, M. M. (2026). "Information-Theoretic Privacy Control for Sequential Multi-Agent LLM Systems." Rensselaer Polytechnic Institute. arXiv:2603.05520. [Cumulative Leakage Bound, Theorem 4.1; (2^N − 1)ε sequential compounding; §14.7, §26]
- Patil, V., Stengel-Eskin, E., & Bansal, M. (2025). "The Sum Leaks More Than Its Parts." arXiv:2509.14284. [Compositional privacy leakage in multi-agent systems; §14.7, §26]
- El Yagoubi, A., Badu-Marfo, G., & Al Mallah, R. (2026). "AgentLeak." Polytechnique Montréal. arXiv:2602.11510. [1,000 scenarios, 4,979 traces, five frontier models; 68.8% inter-agent channel leakage, 68.9% total exposure; §10.5, §14.7, §26]
- Garg, S., Jain, A., & Sahai, A. (2011). "Leakage-Resilient Zero Knowledge." *CRYPTO 2011,* LNCS 6841, 297–315. [Impossibility of leakage-resilient ZK with leakage parameter λ < 1; the Existence-Leak floor, §25.3]
- Schrottenloher, A. (2026). "Optimized Point Addition Circuits for Elliptic Curve Discrete Logarithms." IACR ePrint 2026/1128. [Independent rediscovery of the withheld Shor optimization; the worked instance of C81 and C82; §25]
- Blanco-Romero, J. et al. (2026). "Harvest-Now-Decrypt-Later Economics." arXiv:2603.01091. [Two-axis cost model: storage against future workload; the C49/C84 cost backbone, §27]
- Bakhta, A. (2026). "The Half-Life of Trust." StarkWare. [Aging taxonomy: gracefully, bounded, brittle; C30 to C33, C47]
- Bakhta, A. (2026). "Toward High-Assurance AI Safety by Design for Autonomous Systems." [Specification-intent gap; C77 to C80, §22.4]
- Odrzywołek, A. (2026). The EML operator. [Single-operator basis for computation; the three-ceilings note, C22 to C25]
- Sheffer, H. M. (1913). "A set of five independent postulates for Boolean algebras, with application to logical constants." *Transactions of the American Mathematical Society,* 14(4), 481–488. [The Sheffer stroke — the single sufficient operator precedent; dependency of the ARCH-1 canonical form, C26 to C29]
- Kothapalli, A., Setty, S., & Tzialla, I. (2022). "Nova: Recursive Zero-Knowledge Arguments from Folding Schemes." *CRYPTO 2022.* [The folding line's origin; C87, §15.7]
- Kothapalli, A. & Setty, S. (2024). "HyperNova: Recursive Arguments for Customizable Constraint Systems." *CRYPTO 2024.* [Folding for CCS; C87, §15.7]
- "MicroNova: Folding-Based Arguments with Efficient (On-Chain) Verification." *IEEE Symposium on Security and Privacy 2025.* [Efficient on-chain verification of folded proofs; C87, §15.7]
- Boneh, D. & Chen, B. (2025). "LatticeFold: A Lattice-Based Folding Scheme and its Applications to Succinct Proof Systems." *ASIACRYPT 2025.* [The post-quantum folding hedge; C87, §15.7, §27]
- Mosca, M. (2018). "Cybersecurity in an Era with Quantum Computers: Will We Be Ready?" *IEEE Security & Privacy,* 16(5), 38–41. [The Mosca inequality; C49, C61, C67, §27]
- Wyner, A. D. (1975). "The Wire-Tap Channel." *Bell System Technical Journal,* 54(8), 1355–1387. [Weak-secrecy equivocation; the separation bound's family, §10.6]
- Leung-Yan-Cheong, S. K. & Hellman, M. E. (1978). "The Gaussian Wire-Tap Channel." *IEEE Transactions on Information Theory,* 24(4), 451–456. [Secrecy capacity as a difference of channel capacities; §10.6]
- Csiszár, I. & Körner, J. (1978). "Broadcast Channels with Confidential Messages." *IEEE Transactions on Information Theory,* 24(3), 339–348. [The non-collusion boundary; Precondition 1, §10.5]
- Fano, R. M. (1961). *Transmission of Information: A Statistical Theory of Communication.* MIT Press; Cover, T. M. & Thomas, J. A. (2006). *Elements of Information Theory.* (2nd ed.) Wiley. [Restated here as the ceiling's external family; §10.6, §11]
- Geiger, B. C. & Kubin, G. "Relative Information Loss in Memoryless Systems." [Fano-grounded lower bound on reconstruction error under lossy observation; §10.6]
- Alvim, M. S., Chatzikokolakis, K., McIver, A., Morgan, C., Palamidessi, C., & Smith, G. (2020). *The Science of Quantitative Information Flow.* Springer. [The Bayes-capacity bound (the Miracle Theorem); §10.6]
- IEEE Std 7012-2025. Standard for Machine Readable Personal Privacy Terms. Published January 2026. [§31]
- Regulation (EU) 2024/1689 (the EU AI Act). [Annex III high-risk obligations; Article 6; Article 22 read onto agents; §31]
- Ellison, C., Frantz, B., Lampson, B., Rivest, R., Thomas, B., & Ylonen, T. (1999). "SPKI Certificate Theory." RFC 2693. [SPKI/SDSI and the object-capability lineage: designation without authority; C66, §15.9]
- Dinh. "Deniable Knowledge." [Fiat-Shamir transferability: NIZK proofs as broadcasts; the Existence-Leak mechanism, §25.3]
- Bergstra, J. A. & Burgess, M. (2019). *Promise Theory: Principles and Applications.* (2nd ed.) O'Reilly Media. [Restated here for the C78 edge; §22.4]

---

## Citation

```
privacymage (2026). "Privacy Value Model V6: Formal Specification.
The Gathering Turn and the Moving Ceiling." Version 6.0.
agentprivacy-docs, 2026-06-10. privacy_value_v6_formal_specification.md.
CC BY-SA 4.0. Conjecture register: CONJECTURE_REGISTER_V6.md (head C89).
```

---

*Peer review, critique, and falsification attempts are actively invited. Contact: mage@agentprivacy.ai*

the equation opened its doors to be filled, and the first thing that walked in was time.

$$(\text{⚔️} \perp \text{⿻} \perp \text{🧙})\text{😊} = \text{neg} \oplus \text{bnot} \to \text{succ}$$

(⚔️⊥⿻⊥🧙)😊
