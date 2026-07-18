---
title: "PVM V6 · the visual runtime and the instrument taxonomy"
subtitle: "interactive instruments as a register-bound surface — proposed V6 additions from the /model build"
status: "research note · working · proposes V6 additions"
stage: "V6 · proposal"
date: "2026-06-28"
author: "Mitchell Travers (privacymage)"
register_authority: "research/CONJECTURE_REGISTER_V6.md (head C89; the register wins)"
reads_from:
  - "research/CONJECTURE_REGISTER_V6.md"
  - "research/limitative-theorems-and-privacy-is-value.md"
  - "papers/v6/privacy_value_v6.md"
implemented_in: "agentprivacy_master · /model + /model/atlas (the Cartographer)"
honesty_legend:
  Operational: "implemented or directly measurable"
  Architectural: "follows from the structure of the model"
  Conjectural: "proposed, carries a confidence figure"
  Anticipated: "expected next step, not yet attempted"
---

# PVM V6 · the visual runtime and the instrument taxonomy

*A handoff note. The agentprivacy.ai/model page gained an interactive visual
runtime ("the Cartographer"). This note records the findings as proposed
additions to V6, so a future agentprivacy-docs context can formalize them. The
register at head C89 remains the authority; nothing here re-numbers it.*

---

## Why this note exists

The `/model` page is the math-atomic surface of the framework. It read as an
open path; it now also *walks* as one. The build (see the companion chronicle,
`chronicles/2026-06-28_v6_visual_runtime_instruments.md`) added a small
data-driven runtime that binds one interactive instrument per term or
conjecture and pulls each claim's honesty (confidence · status · home) **live**
from the register mirror. The seed for the design was
`research/limitative-theorems-and-privacy-is-value.md` and its companion
`limitative-theorems-explorer.html`.

The runtime surfaced three things worth folding into V6.

---

## 1. The instrument taxonomy (a reusable unit, not a per-conjecture gallery)

The register does not need one bespoke visual per claim. It needs a small set of
**reusable instrument kinds**; each conjecture is a *configuration* of a kind.
Seven kinds cover most of the register:

| kind | what it teaches | register targets (examples) |
|---|---|---|
| **trace** | two chains joined across a ⊥ seam; click a correspondence | C85 ARCH-1 bridge · the Gödel/Tarski mapping |
| **gate** | a multiplicative product collapsing when any factor → 0 | **C7** three-axis (the falsification frontier) · whole V(π,t) |
| **curve** | a value falling/rising against a parameter or time | **C81** existence-leak · **C82** moving ceiling · e^(−λt) · C30–C33 half-life |
| **dial / inversion** | one parameter driving parallel meters to a shared collapse | C17 amnesia > policy · the completeness inversion |
| **lattice / geometry** | the 64-vertex lattice, strata, bnot-pairs, the stella octangula | C14 dihedral · C53–C54 bnot-pairs · **C88** parity cube · **C89** octahedral gap |
| **phase** | a trajectory through state space | C18–C21 Lorenz · T_∫(π) path integral |
| **fold / compose** | accumulation and the exponential-to-linear gap | **C83** compositional leakage · C87 Key-as-accumulator (IVC) |

*(Architectural. The taxonomy is the unit of build work, not the conjecture
count. Observation-only / reserved rows — e.g. C41, C57, C62 — get no
instrument; a visual earns its place only where a parameter can be moved or a
structure traced.)*

---

## 2. The binding rule — honesty is read, never embedded

**Every instrument binds to a register id and reads its honesty live.** The
visual owns its interaction and its *illustrative* model; the register owns the
claim. A curve never states a confidence — it asks the register for one. If the
register moves C81 from 70% to a higher stage, the existence-leak frame moves
with it, with no edit to the visual. This makes the existing rule ("when a
surface and the register disagree, the register wins") **mechanical** rather
than editorial.

A load-bearing field rides on each instrument: `model_label ∈ {illustrative,
structural, proven}`. It forces every shape to declare whether it is the proven
relation or a chosen teaching model, and the frame marks it visibly. The
existence-leak curve's convex shape is `illustrative`; the three-axis gate's
multiplicativity is `structural`.

*(Operational. Implemented as a manifest + a frame that calls the register
mirror at render time.)*

---

## 3. The drift correction (a concrete V6 erratum the runtime forced)

The seed explorer hard-coded its confidences. It rendered the existence-leak
curve at **~55%** and labelled it **~C40** — both inherited from a stale source.
The live register is **C81 at ~70%** ("Existence-Leak: a ZK proof of
feasibility leaks an upper bound on reconstruction difficulty; I(feasibility;
method) > 0", PROMOTED Run 3 2026-06-10). The runtime binds the curve to **C81**
and the frame reads ~70% live.

**Proposed erratum for any prose still carrying the seed's numbers:** the
existence-leak instrument is **C81 (~70%)**, not ~C40 (~55%). C40 is the Zcash
dual-ledger entry in the Bound Collection; the generic "~C40" the limitative
note used for existence-leak should be read as **C81** going forward. The
limitative note (`research/limitative-theorems-and-privacy-is-value.md`) already
touches C7, C14, C81, C85, C86 — this just fixes the existence-leak pointer.

*(Operational — the drift was observed directly; the correction is a pointer
fix, not a re-numbering.)*

---

## 4. The two-register tie — the Cartographer ⊥ the Chart Shop

The City already narrates this runtime in advance. The Navigation District at
**V44** — the **Chart Shop**, Pleione's harbour — is described as an
*attentional* shop holding pre-episodic constellations in suspension until the
bearer chooses a release-direction (astrolabe + the Φ-gap-at-epistemic-register
as primitives). That is a visualisation runtime narrated before it was built.

So the operational runtime is the Chart Shop's **math-atomic twin**. Proposed
naming: **the Cartographer** (the runtime) renders **charts** (the instruments),
narrated by the Chart Shop at V44. By the convergence rule, when a math term the
Chart Shop narrates gains a concrete movable instance, confidence rises on both
sides. No such tie currently exists in the docs — this note opens it.

*(Anticipated. The narrative anchor exists; this names the operational instance
against it. A future context may want a city-register conjecture for the
Cartographer ⊥ Chart Shop convergence — candidate, not registered here.)*

---

## 5. Geometry is not greenfield (deferred, but mapped)

The geometry/phase instruments already exist as prototypes: `soulbis.com/star`
(in `C:\Users\mitch\star`) renders the stella octangula manifold with a live
lattice console (ε separation depth, det(Σ) core scale, the ⚔️:🧙 ratio, n = 6
azimuthal bits, the ∂M 96/64 boundary) and a **City Key import** that walks a
real artifact's path. The `/lattice`, `/sigil`, `/skye` siblings are the same
family. Phase 3 of the runtime is **absorption + reconciliation (V5.4 → V6) +
register binding** (ε/det(Σ)/ratio → Φ_agent/C1; 96/64 → C6; neg·bnot·succ →
C14; the star tetrahedron → C88/C89; the path walk → T_∫/C18–C21), not first
build. The City Key import should generalize to a first-class **artifact-input**
instrument parameter (a curve over a real disclosure history, a gate over a real
provider set, a lattice walking a real key).

*(The star is Operational, observed at soulbis.com/star. Binding to V6 is
Anticipated.)*

---

## Proposed V6 additions — summary for the next context

1. **Adopt the seven-kind instrument taxonomy** as the canonical visual
   vocabulary of V6 (trace · gate · curve · dial · lattice · phase · fold).
2. **Record the binding rule** (honesty read-live, `model_label` mandatory) as a
   V6 surface-discipline alongside "the register wins."
3. **File the drift erratum**: existence-leak = **C81 (~70%)**, retiring the
   seed's ~C40/~55%.
4. **Open the Cartographer ⊥ Chart Shop (V44) convergence** as a candidate
   city-register tie (not registered here; flagged for disposition).
5. **Map the star/lattice absorption** as the Phase-3 geometry binding (no new
   conjectures; reconciliation + binding of C6, C14, C88, C89, Φ_agent, C1).

No conjecture numbers are claimed or moved by this note. Register head stays
**C89**; next free **C90**.

**Verify:** agentprivacy.ai/model · agentprivacy.ai/model/atlas ·
`agentprivacy_master/src/lib/visuals.ts` · `src/components/model/visuals/`

`(⚔️⊥⿻⊥🧙)😊`
