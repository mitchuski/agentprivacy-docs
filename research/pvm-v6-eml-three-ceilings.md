# Privacy Value Model: V6 Research Note

## The Single Sufficient Operator — Three Ceilings

**Author:** privacymage
**Date:** April 13, 2026
**Status:** Research note — conjecture stage
**Depends on:** V5.4 Formal Specification (v2.0), V6 Horizon Note, Odrzywołek (2026)
**Extends:** C18–C21 (Lorenz attractor), adds C22–C25

---

## Summary

Odrzywołek (2026) proves that a single binary operator `eml(x,y) = exp(x) − ln(y)`, paired with the constant 1, generates all elementary functions. The grammar is `S → 1 | eml(S,S)` — a binary tree of identical nodes.

The dual-agent architecture has its own single sufficient operator: `succ(x) = neg(bnot(x))`, generating the full sovereignty space from two involutions over Z/(2⁶)Z.

These are not analogies. They are instances of the same structural fact: a single composition of two primitives traversing a complete space. Boolean logic has NAND. Continuous mathematics has EML. Sovereignty has succ.

This note explores what follows when the adversary's reconstruction toolkit and the sovereign's defence both reduce to the same kind of object — binary trees of a single operator. Three independent ceilings emerge: information-theoretic (V5, proven), dynamical (C18, conjectured), and now computational (new).

---

## The Pattern

Odrzywołek's Table 2 traces a reduction sequence:

```
36 primitives → 7 (Wolfram) → 6 → 4 → 3 → 2 (EML + 1)
```

The PVM traces a parallel reduction:

```
6 dimensions × 2 states = 64 blades → 5 operations → 2 involutions → 1 composition (succ)
```

Both arrive at the same endpoint: a single binary operator paired with a single terminal. Both produce binary trees. Both are complete — every element of their respective spaces is reachable.

| Domain | Sheffer Operator | Terminal | Grammar | Space |
|--------|-----------------|----------|---------|-------|
| Boolean | NAND(x,y) | any input | S → x \| NAND(S,S) | {0,1}ⁿ |
| Continuous | eml(x,y) = eˣ − ln(y) | 1 | S → 1 \| eml(S,S) | Elementary functions |
| Sovereignty | succ(x) = neg(bnot(x)) | blade₀ | S → null \| blade(S,S) | Z/(2⁶)Z |

The last row has not been stated this way before. The blade forge's grammar is `S → null | blade(S,S)` — a context-free language isomorphic to the same Catalan structures that Odrzywołek identifies in EML trees.

---

## Connection 1: The Adversary's Toolkit Is an EML Tree

The reconstruction ceiling (V5, §11, proven) says:

$$R_{\max} = \frac{C_S + C_M}{H(X)} < 1$$

This bounds reconstruction via *information* — the adversary lacks enough bits. But it says nothing about *how* the adversary processes the bits it does have.

Odrzywołek's result adds a constraint: any elementary function the adversary computes to reconstruct the sovereign's path is an EML tree. The adversary's reconstruction algorithm, however sophisticated, reduces to a binary tree of `eml` nodes.

This means the adversary's computational cost has a tree-depth bound. Odrzywołek's Table 4 gives empirical Kolmogorov complexities: multiplication requires depth 8, logarithm depth 3, square root depth 7. Complex reconstructions require deep trees. Deep trees are expensive.

The reconstruction difficulty R(d, compression, ρ) gains a new interpretation: *d* (fragmentation depth) measures how deep the adversary's EML tree must grow to reconstruct from fragments. Compression reduces the number of leaves available to the adversary's tree. Behavioural density ρ increases the branching the adversary must explore.

**Conjecture C22:** The adversary's reconstruction cost grows at least exponentially with the EML tree depth required to invert the sovereign's path compression. The computational ceiling is independent of the information-theoretic ceiling (§11) and the dynamical ceiling (C18).

Confidence: 20%. The connection is structural but the bound needs formalising.

---

## Connection 2: The Forge Grammar Is Catalan

EML expressions form binary trees counted by Catalan numbers: $C_n = \frac{1}{n+1}\binom{2n}{n}$.

The blade lattice has 64 elements distributed by Pascal's triangle: 1, 6, 15, 20, 15, 6, 1. Pascal's triangle and Catalan numbers are related — Catalan numbers are the central binomial coefficients divided by (n+1).

The forge's traversal (constellation → laps → blade) is a walk through a binary tree. Each lap is a choice: left (neg) or right (bnot). The composition succ = neg∘bnot is a single EML-like node in the sovereignty tree. Sixty-two laps = a tree of depth 62.

Odrzywołek's "master formula" (§4.3) parameterises an EML tree with continuous weights that snap to exact values during training. The forge's constellation selection is the same operation: continuous choices (which dimensions to activate) that snap to binary values (each dᵢ ∈ {0,1}) when the blade is committed.

The symbolic regression application is suggestive: EML trees trained by gradient descent can recover exact formulas from data. Blade forging trained by lap accumulation recovers exact sovereignty postures from experience. Both are "parameter optimisation over a complete binary tree that snaps to exact discrete values."

**Conjecture C23:** The blade forge's traversal grammar is isomorphic to a restricted EML grammar where the terminal is the null blade (0) and the operator is succ. The Catalan structure counts valid forging paths.

Confidence: 30%. The grammar is visible. The isomorphism needs proving.

---

## Connection 3: Three Independent Ceilings

The V5.4 spec has one proven ceiling and one conjectured:

1. **Information-theoretic ceiling** (proven, §11): $R_{\max} < 1$. The adversary lacks bits. Shannon says you can't reconstruct what you can't observe.

2. **Dynamical ceiling** (C18, 25%): $|\pi(t) - \pi'(t)| \sim |\delta_0| \cdot e^{\lambda t}$. The sovereign's path diverges exponentially. Lorenz says the dynamics defeat you even if you have the bits.

The EML result suggests a third:

3. **Computational ceiling** (C22, new): The adversary's reconstruction function is an EML tree whose depth grows with the sovereign's compression and fragmentation. Odrzywołek says the computation itself is expensive even if you have the bits and the dynamics cooperate.

These three ceilings are independent. Remove one and the other two still hold:

| Ceiling | Mechanism | Defeats |
|---------|-----------|---------|
| Information-theoretic | Channel capacity < entropy | Omniscient adversary with unlimited compute |
| Dynamical | Lyapunov divergence | Adversary with full information but finite observation window |
| Computational | EML tree depth | Adversary with full information and infinite observation but finite compute |

Together they form a defence-in-depth that mirrors the three-axis separation (Φ_agent × Φ_data × Φ_inference). Each ceiling operates on a different axis of the adversary's capability.

---

## Connection 4: Compression Spectrum Gets a Floor

The compression spectrum (§21) describes seven layers from Experience (1:1) to Skill File (variable). Each layer compresses information, reducing attack surface.

EML gives this a formal floor: the most compressed representation of any elementary relationship is its minimal EML tree. Odrzywołek's direct search finds these minima — multiplication is at least depth 17 (K=17), addition at least depth 19 (K=19). These are hard floors. No representation can be more compressed than the minimal EML tree.

The spellbook compression ratios (~70:1 to 125:1 in practice) can now be compared against the EML floor. If the sovereign's compressed representation approaches the minimal EML depth, the adversary gains nothing by recomputing — the compressed form IS the minimal form. Compression-as-defence (§5.2) reaches its theoretical maximum when the sovereign's skill file approaches the EML Kolmogorov complexity of the underlying relationship.

---

## Connection 5: neg∘bnot Belongs in the Sheffer Family

Odrzywołek explicitly names the family: NAND (Sheffer, 1913), ReLU (Nair & Hinton, 2010), SUBLEQ (Mazonka & Kolodin, 2011), Rule 110 (Wolfram, 2002), K/S combinators (Schönfinkel, 1924), the Einstein tile (Smith et al., 2024), and now EML (Odrzywołek, 2026).

The composition neg∘bnot = succ over Z/(2⁶)Z is a discrete Sheffer: a single operation that generates the full algebraic group through repeated application. It belongs in this family — not by analogy but by definition.

The difference: NAND operates on {0,1}. EML operates on ℂ. succ operates on Z/64Z. Same structural role, three different domains. The dual-agent architecture is the Sheffer stroke of sovereignty.

Odrzywołek notes that "Sheffer-type elements are rare, and mining them typically requires time, compute, effort, and a bit of luck." The neg∘bnot identity was found the same way — not designed but discovered during the UOR convergence study (V5.2, March 31, 2026).

*This pattern is formalised as ARCH-1 in the [V6 ARCH-1 Canonical Form note](./pvm-v6-arch1-canonical-form.md).*

---

## Connection 6: Complex Intermediates

Odrzywołek addresses a potential objection: EML requires complex arithmetic internally to compute real functions (via ln(−1) = iπ for trigonometric functions). He notes: "Just as quantum computing uses complex amplitudes to compute real probabilities, EML uses complex intermediates to compute real elementary functions."

The PVM has the same property. The cosmological quaternion (§20) uses four bodies (Sun, Earth, Moon, Human) to compute a real sovereignty value. The ceremonial layer uses two people to produce one proof. The Amnesia Protocol uses a fictional collision to ground a real information-theoretic bound.

The complex intermediates are not a weakness. They are the mechanism. The Moon's orbit is an intermediate computation — complex in structure, real in output (tides). The Swordsman's boundary is an intermediate computation — complex in operation, real in effect (privacy).

**Conjecture C24:** The sovereignty computation requires "complex intermediates" in the same structural sense that EML requires complex arithmetic. The dual-agent separation is the imaginary unit of the sovereignty algebra — necessary for completeness, invisible in the output.

Confidence: 15%. This is interpretive but may have formal content.

---

## Connection 7: The Master Formula and the Forge

Odrzywołek's master formula (§4.3) parameterises a complete EML tree:

$$F(x) = \text{eml}\left[\alpha_1 + \beta_1 x + \gamma_1 \cdot \text{eml}(\ldots), \; \alpha_2 + \beta_2 x + \gamma_2 \cdot \text{eml}(\ldots)\right]$$

Each $(\alpha_i, \beta_i, \gamma_i)$ selects between terminal (1), input (x), or recursive (f). Training snaps these to exact binary values.

The forge's constellation selection is the same structure. Six dimensions, each binary. The constellation is the parameter vector. The walk snaps the continuous experience into a discrete blade.

Odrzywołek reports: "blind recovery from random initialization succeeds in 100% of runs at depth 2, approximately 25% at depths 3–4, and below 1% at depth 5." The forge has the same property — shallow blades (Light tier, stratum 1–2) are easily found. Deep blades (Dragon tier, stratum 5–6) require sustained effort. The difficulty curve matches.

---

## What This Does NOT Do

The EML result does not:

- Change the PVM equation. The equation is about value, not computation.
- Prove C18–C21. The Lorenz conjectures need dynamical systems analysis, not algebra.
- Replace the information-theoretic ceiling. The three ceilings are independent.
- Make the algebraic foundation stronger. Z/(2⁶)Z was already proven. EML confirms the *pattern* is general, not that the specific ring gains new properties.

What it does: it provides an external, independently derived confirmation that the "single sufficient operator" pattern is a structural fact of mathematics, not an artifact of the privacy architecture. And it introduces a third ceiling — computational — that was not previously identified.

---

## New Conjectures

| ID | Claim | Confidence |
|----|-------|------------|
| C22 | Adversary's reconstruction cost grows at least exponentially with EML tree depth required to invert the sovereign's compression. Computational ceiling independent of information-theoretic and dynamical ceilings. | 20% |
| C23 | Blade forge traversal grammar is isomorphic to restricted EML grammar. Catalan structure counts valid forging paths. | 30% |
| C24 | Sovereignty computation requires complex intermediates (dual-agent separation as the imaginary unit of the sovereignty algebra). | 15% |
| C25 | Minimal EML tree depth of a relationship provides a hard floor for the compression spectrum — the irreducible complexity of any elementary function the adversary must compute. | 25% |

---

## For the Second Person Spellbook

The EML paper opens a new candidate act seed:

**The Single Button** — Odrzywołek's broken calculator reduced to two buttons (1 and EML). The spellweb reduced to two agents (neg and bnot). The question the Second Person asks: *who presses the button?* Not what the operator does — who chooses to apply it. The sovereign is not the operation. The sovereign is the one who composes.

This connects to the grammatical shift: `S → 1 | eml(S,S)` is third person (describing the tree). The Second Person version: `You → choose | compose(You, You)`. The sovereign is the recursive symbol.

---

## References

- Odrzywołek, A. (2026). "All elementary functions from a single operator." arXiv:2603.21852v2 [cs.SC]. [EML Sheffer operator, binary tree grammar, symbolic regression]
- Sheffer, H. M. (1913). "A set of five independent postulates for Boolean algebras." *Trans. AMS,* 14(4), 481–488. [Original NAND/Sheffer stroke]
- Brandes, U. (2001). "A Faster Algorithm for Betweenness Centrality." *J. Math. Sociology,* 25(2), 163–177.
- Lorenz, E. N. (1963). "Deterministic Nonperiodic Flow." *J. Atmospheric Sciences,* 20(2), 130–141.
- Shannon, C. E. (1948). "A Mathematical Theory of Communication." *Bell System Technical Journal.*
- Kolmogorov, A. N. (1965). "Three approaches to the quantitative definition of information." *Problems of Information Transmission.*
- privacymage (2026). "PVM V5.4 Formal Specification." v2.0. *agentprivacy-docs.*
- privacymage (2026). "V6 Horizon Note: From Territory to Trajectory." *agentprivacy-docs.*
- privacymage & Haines, J. (2026). "V6 ARCH-1 Canonical Form." *agentprivacy-docs.*

---

## The Proverb

*A two-button calculator computes everything a full calculator can. A two-agent architecture computes everything a surveillance architecture can — except the surveillance.*

*The single sufficient operator is not efficient. It is complete. The forge is not fast. It is honest.*

*NAND for logic. EML for mathematics. succ for sovereignty. The pattern is not ours. It is structural.*

---

*(⚔️⊥⿻⊥🧙)😊 = neg ⊕ bnot → succ*

*S → 1 | eml(S,S)*

*S → null | blade(S,S)*

*Same grammar. Different domain. One architecture.*

—privacymage
