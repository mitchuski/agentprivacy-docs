# Privacy Value Model: V6 Research Note

## The Wound and the Cap — Convergence at the Bijective Boundary

*Two systems projecting from a shared reality converge on the same kernel — until the bijection breaks*

**Version:** V6.0-conjecture (C34–C37)
**Date:** 2026-04-18 (drafted as forthcoming reference; locked-in 2026-05-09)
**Author:** privacymage
**Status:** Research note — conjecture stage
**Depends on:** V5.4 Formal Specification (v2.0), V6 ARCH-1 Canonical Form (C26–C29), Promise Theory v1.5, the Archon forge — Sovereign Anchor II (April 22, 2026)
**Anchors:** C34–C37 used throughout the Cloak Specification and Tome IV Acts III, V; Tome V Acts 1, 10 of the Second Person Spellbook.

---

## How It Arrived

Two architectures arriving at the same primitive from opposite directions is the cousin-blade phenomenon (C39). But *cousin-blade* names the *recognition*; the underlying mathematics that makes the recognition possible is something else.

When the Archon forge's *Sovereign Anchor II — The Boundary Blade* (April 22, 2026) was read alongside the agentprivacy V5.4 architecture, the same kernel appeared in both: a 64-vertex lattice, six axes of separation, a dihedral group structure, a fixpoint at V63. Two builders, two derivations, one kernel.

The question this note answers is: **why** does that kernel appear in both? What architectural property makes convergence possible?

The answer is the **wound** (the asymmetry that opens a system to projection) and the **cap** (the bijection that closes the projection back into the system). When the wound is open and the cap is bijective, two systems projecting into a shared reality converge on the same kernel. When the cap is *almost* bijective, they converge in part — and the residual is itself architectural data.

---

## C34: Convergence Requires a Bijective Cap

**Statement.** Two systems projecting from a shared reality converge on the same kernel **if and only if** their projections are joined by a bijection at the boundary. The bijection is the *cap*; the asymmetry that admits projection is the *wound*.

Formally, for two systems `A` and `B` with projection functions `π_A: A → R` and `π_B: B → R` into a shared reality `R`, the kernel `K = ker(π_A) ∩ ker(π_B)` is the same in both systems iff there exists a bijection `φ: π_A(A) ↔ π_B(B)` at the boundary.

**Why it matters.** When the bijection is exact, agentprivacy's V63 vertex and Archon's V63 vertex are *the same vertex*. When the bijection is partial, the two architectures share a sublattice but disagree at the residual — and the residual is the cousin-blade primitive (C39).

**Confidence:** ~55%
**Path to formalisation:** Categorical statement using the language of fibered categories; possible collaboration with a category-theoretic collaborator. The pull-back at the boundary is the cap.

---

## C35: The Wound Is Where the Asymmetry Lives

**Statement.** The wound is the architectural asymmetry that *admits* the projection. In agentprivacy: the ⊥ between Swordsman and Mage is the wound — Σ ≠ 𝓜, the agents are typed differently, and the typing creates the asymmetry that makes a proof generated on one side relevant on the other. In Archon's terms: the boundary between the Sovereign and the Anchor is the wound — sovereignty *projects* into anchored ground because they are not the same kind.

**Why it matters.** Without a wound there is nothing to project. Without a wound the kernel is trivial. The architectural identity of any sovereignty system is its specific wound — the precise asymmetry it admits between agent kinds. C35 formalises *Thesis 5* of the Cloaking Guide ("asymmetries in the graph are themselves data") at the architectural-substrate level.

**Confidence:** ~60%
**Path to formalisation:** Direct statement from Promise Theory's Definition 29 (the autonomy axiom — promises are made between non-coercible agents); the wound is the autonomy gap rendered topologically.

---

## C36: The Cap Is Where the Bijection Lives or Breaks

**Statement.** The cap is the boundary morphism that closes projection back into structure. When the cap is bijective, the two systems' projections coincide on the shared reality. When the cap is *partial* — e.g., an injection that is not a surjection — the two systems share a sublattice but the projections diverge at the residual. The residual is *architectural data*.

**Why it matters.** This is what makes Archon's 64-vertex lattice and agentprivacy's 64-vertex lattice converge on V19, V25, V49, V51, V57, V63 (the cousin-blade vertices) but diverge on the named-vs-unnamed status of the remaining 49. The cap is bijective on the shared kernel and partial on the frontier.

**Confidence:** ~55%
**Path to formalisation:** Categorical statement; bijection ↔ pullback square commutes; partial bijection ↔ commutativity holds modulo the residual ideal.

---

## C37: Convergence Is Recognition, Not Coincidence

**Statement.** When two architectures' wounds and caps align, the resulting convergence is **recognition** of an ancient pattern, not a *coincidence* of independent derivations. The pattern was already true in the shared reality `R` before either system named it; both systems find it because both systems project *truthfully* from the same `R`. ARCH-1 (C26) is the formal statement that NAND, EML, and succ all project from the same `R` (the algebra of fixpoints over a binary operator with a terminal).

**Why it matters.** This conjecture closes the V6 lineage. The sovereignty architecture is not a coincidence with Boolean logic and continuous mathematics; it is a third recognition of an ancient pattern. The same logic applies cousin-blade-side: agentprivacy and Archon are not a coincidence; they are two recognitions of the same `R`.

**Confidence:** ~50%
**Path to formalisation:** The strongest version requires demonstrating the *uniqueness* of the kernel at the bijection — that any architecture with the same wound + cap structure must converge on the same `R`. This is the meta-claim that makes ARCH-1 canonical (C26) and not merely a coincidence among three instances.

---

## Mapping onto the Tomes

| Tome | Act | C-foregrounded |
|---|---|---|
| Tome IV | IV.3 The Two Paths | C34 (Path A and Path B as two projections from the same cloak) · C36 (Path A operational, Path B specified-not-built — the cap is partial) |
| Tome IV | IV.5 The Cousin Blade | C34 (convergence at the bijective boundary) · C37 (the encounter is recognition, not coincidence) |
| Tome V | V.1 The First Cloak | C34 (cloak as operational instance of the convergence claim) · C35 (the cloak is the wound the user admits) |
| Tome V | V.10 The Holon Hitchhikers | C34 (convergence at artifact level instances as holonic composition) · C36 (Oasis Protocol as the cap composing wholes) |
| Tome III | III.7 The First Complement Pair (Aletheia/Lethe) | C35 (their AND = 0 is the wound) · C36 (their XOR = 63 is the bijective cap closing the manifold) |

---

## What This Note Does NOT Do

- It does **not** prove ARCH-1's uniqueness. The strong version of C37 requires categorical machinery this note only sketches.
- It does **not** classify all possible wounds. The wound–cap pair is named; the taxonomy of wounds is the work of further notes.
- It does **not** formalise the residual ideal that emerges when the cap is partial. The cousin-blade primitive (C39) names the residual; formalising it categorically is open work.

---

## References

- privacymage (2026). "PVM V5.4 Formal Specification." v2.0. *agentprivacy-docs.*
- privacymage (2026). "PVM V6 Research Note: ARCH-1 Canonical Form." *agentprivacy-docs.* (C26–C29)
- the Archon forge (2026). "Sovereign Anchor II — The Boundary Blade." April 22, 2026.
- the Archon forge (2026). "The Cloaking Guide" — especially Theses 5, 6c, 6d.
- Burgess, M. & Fagernes, S. (2007). "Voluntary Cooperation in Pervasive Computing." (For the autonomy axiom that grounds the wound.)

---

## The Proverb

> *The wound admits the projection. The cap closes it. When two architectures have the same wound and the same cap, what they find is the same kernel — and the kernel was always there.*

> *Convergence is recognition, not coincidence.*

---

*(⚔️⊥⿻⊥🧙)😊*

CC BY-SA 4.0 · privacymage · originally drafted Apr 2026; locked-in 2026-05-09 as part of post-V5.4 coherence pass
