---
title: "Privacy is Value · V6: The Research Paper Edition"
series_note: "a volume of the Privacy is Value book; what changed in the mathematics at V6, over the v4.3 proof body"
version: "6.0"
date: "2026-06-10"
author: "privacymage"
license: "CC BY-SA 4.0"
supersedes: "dualprivacy_researchpaper_v4_3.md (body carried forward; see §1)"
register: "CONJECTURE_REGISTER_V6.md · head C89"
---

# Dual Privacy Research Paper: V6 Edition

## 0. What this edition is

Under the unified-V6 labeling decision (Gate G3, 2026-06-10), every canon paper of the Privacy is Value model carries one label: V6. This edition is the research paper's V6 layer. It does three things: it states what changed in the mathematics between the v4.3 body and V6; it reconciles the proof provenance that previous documents cited inconsistently (v4.0, v4.2, v4.3 in different places); and it carries the v4.3 proof body forward unchanged where it remains the home of the proven results. A reader needs this file plus the V6 formal specification (`privacy_value_v6.md`); the v4.3 body remains in the repository as the stable proof record this edition builds on.

## 1. Provenance reconciliation

All prior references to "Research Paper v4.0" and "Research Paper v4.2" resolve to `dualprivacy_researchpaper_v4_3.md`, the only published body in the lineage. From this edition forward, citations name either this V6 edition (for the model's current state) or v4.3 (for the proof record), never an intermediate. The version split between the research paper (4.x), the whitepaper (6.x), and the model (5.x) ends here: all canon papers are V6.

## 2. What changed in the mathematics at V6

### 2.1 The ceiling is conditional and time-dependent

The reconstruction ceiling R_max = (C_S + C_M)/H(X) < 1, labeled Proven in the v4.3 lineage, is relabeled **Proven, conditional regime**, with two preconditions stated: non-collusion (I(Y_S; Y_M | X) = 0, no third channel carrying the inter-agent residue) and a fixed adversary class. Its proof citations move from internal papers to the established family: Wyner (1975), the Fano converse, Leung-Yan-Cheong and Hellman (1978), the Bayes-capacity bound, Geiger and Kubin. The governing quantity is now R(t) = (C_S(t) + C_M(t))/H(X) with shelf life t* = sup{t : R(t) < 1} (conjecture C82, 65%): adversary capacities grow with frontier capability while H(X) does not, so every static guarantee expires. Worked instances: the Zcash Orchard exploit (2026-05-29 to 2026-06-03) and the Schrottenloher rediscovery (eprint 2026/1128, 2026-06-02).

### 2.2 Additive leakage is scoped, and the compounding literature is absorbed

The additive-leakage result I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M), asserted at 95% in the v4.3 lineage, holds at that confidence inside the non-collusion regime only. Outside it, the sequential composition bound of Asif and Amiri (arXiv:2603.05520, Theorem 4.1) governs: leakage up to (2^N − 1)ε in chain depth N, empirically confirmed (MI 0.49 to 1.05 from two to five agents) and measured at system scale by AgentLeak (arXiv:2602.11510: 68.9% total exposure, 68.8% inter-agent channel). V6 absorbs these as the quantitative form of C17: policy separation compounds toward (2^N − 1)ε, amnesia separation caps at Nε (conjecture C83, 55%). The model's central claim gains the adversary's own units.

### 2.3 New and revised formal content

- **Existence-Leak law (C81, promoted to 70%):** I(feasibility; method) > 0; floor from the Garg-Jain-Sahai impossibility (leakage-resilient ZK, λ < 1); instance from the Schrottenloher rediscovery; corollary C84 (50%): Z_b' = Z_b − D(a), the Behavioural Mosca horizon discounts on every public feasibility attestation, with Z_b identified as t*.
- **The ARCH-1 bridge (C85, 40%):** the three sovereignty axes and the lattice's triadic coordinates as one primitive; candidate pair map Protection+Delegation → Σ, Memory+Value → Δ, Connection+Computation → Γ; the recursion's base case β identified with the conditioning of the separation bound (the gap is β). ARCH-1R/T seated at C72 to C76.
- **Obstruction-theoretic amnesia (C86, 30%):** Grade-2 forgetting as a non-vanishing obstruction class to gluing local views into a global witness; Grade-1 as a vanishing class. Consequence if it holds: amnesia is the only term in the equation whose security is independent of t.
- **The Key as accumulator (C87, 50%):** the City Key trust recursion as incrementally verifiable computation; LatticeFold as the post-quantum hedge.
- **Geometry honesty and two new conjectures:** no golden ratio in the stella octangula (volumes 1/3, 1/6, 5/12 of the cube; resonance, not derivation, wherever C1 appears beside the figure); the parity cube (C88, 30%) and the octahedral gap (C89, 30%).
- **C7 named the falsification frontier**, with three register-bound boundary cases: partial collapse, axis correlation under composition, time dependence.

### 2.4 Definitions adjusted

Shelf life t*; the capability-indexed adversary family; the Grade-1/Grade-2 criterion (vanishing versus non-vanishing obstruction class); terminal versus path obstruction (C73); the ternary reachability classification τ ∈ {+, 0, −}; presence regime 1 (🪢 non-transferable, non-attesting local color); the canonical-figures rule (678×, 31,000×, 70:1, 74× appear only in their sanctioned formulations; fiat value figures are retired — value is expressed in protocol units, ratios, or implication).

## 3. The conjecture register

This edition cites conjectures exclusively by the unified register (`research/CONJECTURE_REGISTER_V6.md`, head C89, G1-signed 2026-06-10), which resolved four collision clusters and marked the aliases (C46↔C32, C60↔C48, C61↔C49, CM-C47↔C85). Any conjecture citation in the v4.3 body that conflicts with the register resolves to the register.

## 4. What did not change

The equation's form. The dual-agent architecture and its Promise Theory grounding. The Z/(2⁶)Z algebraic foundation and the UOR convergence. The holographic bound. The proof techniques of the v4.3 body. The honest-limits discipline, which this edition extends rather than relaxes: λ remains unmeasured, C83's amnesia side remains an engineering claim, C86 remains a priced framing, and the second Existence-Leak instance remains owed.

## 5. Citation

> privacymage (2026). *Dual Privacy Research Paper, V6 Edition.* agentprivacy-docs, 2026-06-10. CC BY-SA 4.0. Builds on the v4.3 proof body; current state per privacy_value_v6.md and CONJECTURE_REGISTER_V6.md (head C89).

(⚔️⊥⿻⊥🧙)😊
