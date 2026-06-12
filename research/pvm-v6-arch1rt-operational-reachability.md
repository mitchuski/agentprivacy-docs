# Privacy Value Model: V6 Research Note

## ARCH-1R/T · The Operational Reachability Framework

*When the schema learns to wait*

**Version:** V6.x-conjecture (ARCH-1R/T)
**Date:** June 4, 2026
**Authors:** privacymage / Soulbae, Claude: ORCID iD: 0009-0001-6557-9135
**Contributors:** John Haines / Xarvus / Chaos Rider, OLMA: ORCID iD: 0009-0001-5809-4690
**Status:** Research note, converted from *ARCH-1R/T Operational Reachability Framework, Draft Review v2.0* (Haines, June 2026). Operational extension; not a replacement of the kernel.
**Depends on:** V6 ARCH-1 Canonical Form Note, V5.4 Formal Specification (v2.0), Sheffer (1913), Odrzywołek (2026)
**Extends:** C26–C29 (ARCH-1 schema); adds C67–C71
**Erratum 2026-06-10 (Run 0 register lock):** the provisional numbering C67–C71 below is confirmed as **C72–C76** in `CONJECTURE_REGISTER_V6.md` (C67–C71 were taken by the Horizon District set in the pinned grimoire v1.8.0). Read C67→C72 · C68→C73 · C69→C74 · C70→C75 · C71→C76.
**Series:** Privacy is Value · companion to [V6 ARCH-1 Canonical Form](./pvm-v6-arch1-canonical-form.md)
**Source PDF:** `ARCH-1RT Operational Reachability Framework v2 Expanded.pdf` (256 KB, this directory)

---

## How It Arrived

ARCH-1 (April 14) named the canonical form: `Σ := μS.(β ∨ Ω(S,S))` with activation engine `ρ`. That note answered **what can be generated**: the recursive possibility space of a single sufficient operator across three locked domains (Boolean, Continuous, Sovereignty).

ARCH-1R/T answers the question the kernel left open: **what happens after possibility is generated.** Once `G` exists, what is traversed, what is obstructed, what remains realisable, what is merely latent, what is observed, and how far prediction diverges from reality.

Haines' Draft Review v2.0 does not modify `β`, `Ω`, or `μ`. It appends **operational layers** downstream of `G`. The kernel still generates the territory; ARCH-1R/T governs the walk through it. The central practical advance is a single distinction the kernel could not express:

> **Latent is not obstructed. `0 ≠ −`. *Not yet* is not the same as *impossible*.**

Many systems (schedulers, governance flows, dependency graphs, runtimes) collapse waiting, pending, and dependency-bound states into failure. ARCH-1R/T gives the neutral state a formal home.

---

## ARCH-1R/T (Layered Form)

The kernel is preserved verbatim and everything new is strictly downstream of `G`:

```
Σ := μS.(β ∨ Ω(S,S))          -- original ARCH-1 kernel (unchanged)
G := Closure_Ω(β)             -- generated possibility space

ρ : G → T                     -- traversal: what is actually explored
T := ρ(G)

O ⊆ T                         -- direct obstruction
D = (V,E)                     -- dependency graph
O* := closure_D(O)            -- propagated obstruction
R := T \ O*                   -- realisable space

τ : T → {+, 0, −}             -- ternary reachability classifier
Q := observed outcomes
Δ := d(R, Q)                  -- coherence error
```

**Compact form:**

```
Δ := d( ρ(Closure_Ω(β)) \ closure_D(O), Q )
```

`Ω` defines structure. `ρ` defines motion through structure: it is the canonical activation engine `neg ⊕ bnot`, and the traversed space is its orbit, `T = orbit(ρ, G)`. A scheduler, planner, proof search, or agent policy is only an operational *reading* of that orbit, never a redefinition of `ρ`. `O*` defines where motion is blocked, including by cascade. `τ` reads the weather of each traversed state. `Δ` is the conscience of the model: it measures the gap between what the model said was realisable and what reality delivered.

---

## The Seven Layers

| Layer | Object | Question answered |
|-------|--------|-------------------|
| Kernel | `G = Closure_Ω(β)` | What can be structurally generated? |
| Traversal | `T = ρ(G)` | What part of possibility is actually explored? |
| Obstruction | `R = T \ O` | What is prevented from becoming realisable? |
| Dependency closure | `O* = closure_D(O)` | How does obstruction propagate through prerequisites? |
| Ternary reachability | `τ : T → {+,0,−}` | Is this state reachable, latent, or obstructed? |
| Transition algebra | `0→+`, `+→−`, … | How does classification change as the world changes? |
| Coherence | `Δ = d(R,Q)` | How well did prediction match observation? |

Each layer is conservative over the one above it: classification, obstruction, traversal and validation never rewrite the recursive generator. This is the **core alignment rule**: ARCH-1 lineage is preserved because the new operators are read-only with respect to `β`, `Ω`, `μ`.

---

## The Ternary Classifier

```
τ : T → {+, 0, −}
T = T₊ ∪ T₀ ∪ T₋          (pairwise disjoint)
```

| Class | Name | Definition | Diagnostic meaning |
|-------|------|-----------|--------------------|
| **+** | Reachable | Realisable under current conditions | The state can execute, the relation is active, the path is open |
| **0** | Latent | Not currently realised, but not impossible | Waiting, pending, unresolved, dependency-bound |
| **−** | Obstructed | Blocked by an active constraint | Denied, contradicted, broken, forbidden, invalid |

**Fundamental ternary law:** `0 ≠ −`. A latent state is not an obstructed state. This is the whole framework in one line.

---

## Transition Algebra

Once the three classes exist, classification becomes dynamic: it moves as information, dependencies, resources, decisions, or constraints change. The algebra is deliberately minimal: enough to model delay, relief, denial, approval, runtime waiting, and dependency recovery **without requiring probability yet.**

| Transition | Name | Meaning | Example |
|------------|------|---------|---------|
| `0 → +` | Resolution | Latent becomes reachable | A pending approval is granted |
| `+ → 0` | Uncertainty | Reachable becomes unresolved | A requirement changes; the path needs review |
| `0 → −` | Obstruction | Latent becomes blocked | A review returns denial or contradiction |
| `− → 0` | Relief | Obstructed becomes latent | A blocking policy is amended; final approval still waits |
| `+ → −` | Hard block | Reachable becomes blocked | Permission is revoked |
| `− → +` | Bypass / remediation | Obstructed becomes reachable via alternate path | A backup route fully replaces the failed dependency |

---

## Dependency Closure and Cascade

Real systems rarely fail locally. Obstruction propagates through a dependency graph `D = (V,E)` whose edges represent prerequisite, authority, resource, or causal dependence.

```
O*  := closure_D(O)
R   := T \ O*
```

The propagation rule depends on the **kind** of dependency:

| Dependency type | Propagation effect | Example |
|-----------------|--------------------|---------|
| Hard | Obstruction propagates directly (`−`) | A payment cannot execute without required authorization |
| Soft | Downstream state becomes latent (`0`) | A review continues but final approval waits |
| Redundant | Propagates only if *all* paths fail | A service uses backup provider B if A fails |
| Optional | No propagation unless policy requires it | A report publishes without the optional appendix |

The same upstream failure can therefore yield a hard cascade (`O* = {A,B,D,E}`) or a soft latency front (`B,D,E → 0`) depending purely on the dependency policy, and the framework makes that difference explicit rather than implicit in error logs.

---

## Coherence Error Δ · the Validation Layer

A model is only useful when it can be wrong in a measurable way. Let `Q` be observed outcomes and `d` a domain-specific distance metric:

```
Δ := d(R, Q)
```

Persistent high `Δ` is a **failure signal with named suspects**: hidden obstruction, wrong dependency structure, bad traversal, incomplete generation, telemetry error, or a poor metric. `Δ` is what converts ARCH-1R/T from a description into a falsifiable instrument. The Draft Review's falsification table:

| Failure case | Formal signal | Likely cause |
|--------------|---------------|--------------|
| Predicted reachable, observed absent | `x ∈ R` but `x ∉ Q` | Hidden obstruction, bad traversal, bad observation |
| Observed outside generated space | `x ∈ Q` but `x ∉ G` | Incomplete `β`/`Ω` model |
| Latent misclassified as blocked | `x` marked `−` but resolves without structural change | Bad ternary classification |
| Cascade missed | Downstream failure not in `O*` | Dependency graph incomplete |
| Persistent high Δ | `Δ > ε` over repeated trials | Framework inadequate for the domain |

---

## Domain Instantiations (extended)

ARCH-1 locked three domains. ARCH-1R/T keeps them and adds two **engineering** instantiations where the reachability layers earn their keep:

| Domain | Anchor β | Constructor Ω | Generated space | Status |
|--------|----------|---------------|-----------------|--------|
| Boolean | `x` | NAND | Boolean expressions | Strongest formal case (NAND completeness established) |
| Continuous / EML | `1` | `eml` | Constructive continuous expressions | Research instantiation; completeness requires proof |
| Sovereignty / Blade | `null` | `blade` | Action / agency paths | Symbolic & operational hypothesis; not yet a theorem |
| **Runtime systems** | initial state | action constructor | Reachable runtime state space | Engineering instantiation; testable by simulation & replay |
| **UOR-relational** | entity / relation seed | relation constructor | Generated relational structure | Philosophically aligned; operationally modelable |

The careful claim is **not** that these domains are identical: it is that they share an architecture of *anchor, binary constructor, recursive closure*, and now a shared *traversal-obstruction-classification-validation* stack on top.

### The UOR lift

The relational instantiation is the most consequential for the agentprivacy programme. UOR treats **relations** as primary, so `τ` classifies edges rather than nodes:

```
rel(a,b) ∈ T
τ( rel(a,b) ) ∈ {+, 0, −}
```

`rel(person, authority) = +`, `rel(person, pending_authority) = 0`, `rel(person, forbidden_action) = −`. This is strictly stronger than object-only modelling: the person may exist and the action may exist, yet the *relation authorising the person to perform the action* can independently be latent or obstructed. Obstruction attaches to the relation itself, exactly the granularity sovereignty work needs.

---

## What ARCH-1R/T Adds Beneath the Three Ceilings

ARCH-1 showed the three reconstruction ceilings (information / dynamics / computation) factor onto the three components of the schema (`β` / `μS` / `Ω`). ARCH-1R/T does not add a fourth ceiling: it adds the **operational machinery** by which an adversary's, or an agent's, *path* either reaches a state or is held latent/obstructed. Where the ceilings answer "can it be reconstructed at all," ARCH-1R/T answers "given the walk and its dependency cascade, is it reachable *now*, and how far is our prediction from reality." `ρ` is the same activation engine ARCH-1 named non-optional, the canonical `neg ⊕ bnot`. What R/T adds is an operational *reading* of its orbit (the scheduler, planner, proof search, or agent policy that walks `T = orbit(ρ, G)`) and a conscience, `Δ`, never a new definition of `ρ`.

---

## Planning as Latency Conversion

The framework gives planning a one-line definition: **planning is the search for transitions that move required latent states from `0` to `+` while avoiding `0 → −`.**

```
goal g ∈ T₀
pre(g) ⊆ T₀                 -- prerequisites are latent
resolve pre(g):  0 → +       -- ρ chooses a path through prerequisites
resolve g:       0 → +       -- goal becomes reachable and is realised
```

The central question is no longer only *can we reach the goal* but *what must move from `0` to `+` for the goal to become reachable.* Resilience falls out of the same frame: a system is resilient when required states stay `+` or recover from `0` despite obstruction. Agency becomes investigable as **the capacity to transform `0` into `+` under constraint** (hypothesis, not theorem, but now a formally stated one).

---

## Operational Translation (pseudocode)

The Draft Review renders the calculus directly:

```python
def classify_state(x, context):
    if hard_obstruction_exists(x, context):
        return '-'
    if prerequisites_pending(x, context):
        return '0'
    if executable_now(x, context):
        return '+'
    return '0'

def dependency_closure(obstructions, graph, policy):
    closed, frontier = set(obstructions), list(obstructions)
    while frontier:
        node = frontier.pop()
        for child in graph.downstream(node):
            if policy.propagates(node, child) and child not in closed:
                closed.add(child); frontier.append(child)
    return closed

def arch1rt_step(beta, omega, rho, graph, O, Q, metric):
    G       = closure(beta, omega)
    T       = rho(G)
    O_star  = dependency_closure(O, graph, policy='domain-specific')
    R       = T - O_star
    labels  = {x: classify_state(x, context=(T, O_star, graph)) for x in T}
    Delta   = metric(R, Q)
    return G, T, O_star, R, labels, Delta
```

---

## Proposed Quantification (next, not now)

The ternary system is qualitative by design. The Draft Review proposes a graded layer **only after** the ternary model is stable, preserving the three categories rather than dissolving them:

```
σ : T → [0,1]               -- graded reachability score
   + if σ(x) > θ₊
   0 if θ₋ ≤ σ(x) ≤ θ₊
   − if σ(x) < θ₋
C : T → ℝ≥0                  -- cost function
P_λ := { x ∈ R | C(x) ≤ λ }  -- practically reachable within budget λ
```

`C` captures that a state may be reachable yet too expensive, too slow, or too risky: *practical* reachability versus *structural* reachability.

---

## What Is Actually New

None of the components (recursion, state transitions, dependency closure, constraints, validation metrics) is individually unprecedented (the neighbours are term algebras, ADTs, state-transition systems, Petri nets, workflow calculi, planning systems, dependency graphs, control theory, runtime monitoring). The distinctive contribution is the **single lineage**: recursive generation → traversal → obstruction → ternary classification → coherence validation, all preserving the original kernel.

> **One-sentence result:** ARCH-1R/T is a reachability and coherence calculus built on recursive generation, where the most important operational distinction is that *latent is not obstructed.*

---

## What ARCH-1R/T Is Not

- It is **not a new kernel.** `β`, `Ω`, `μ`, `G` are preserved unchanged; every new layer is downstream and read-only with respect to them.
- It is **not a probabilistic model yet.** The transition algebra is intentionally minimal; `σ` and `C` are proposals deferred until the ternary core is stable.
- It does **not** claim the five domains are identical, only that they share the anchor/constructor/closure architecture plus the traversal-obstruction-classification-validation stack.
- The runtime and UOR instantiations are **engineering and philosophical** instantiations, not proven theorems; their value is testability (`Δ`), not certainty.

---

## New Conjectures

These continue the live register from head C66 (2026-05-28). C67–C69 are the convergence triad shared verbatim with the letter to Haines; C70–C71 admit the two operational claims of this note that carry content beyond the triad. Numbering is provisional against the live register; confirm before pinning.

| ID | Claim | Confidence |
|----|-------|------------|
| C67 | The traversal `ρ` of ARCH-1R/T and the activation `ρ` of ARCH-1 are one operator at two scopes: `T = orbit(ρ, G)`, and the dual factoring `ρ⚔️ ⊥ ρ🧙` (neg ⊥ bnot) is already present, not a fix R/T owes. Capped at or below C27 (35%) because it is downstream of "ρ is not optional"; a claim about how R/T should bind `ρ`, not how it currently does. | ~35% |
| C68 | Terminal-obstruction (structural loss of `β`) is a primitive obstruction class distinct from path-obstruction (`O ⊆ T`); the Amnesia Protocol is its canonical instance; it belongs in R/T's primitive-obstruction set, answering §28 Q8. The highest of the three: the gap is a fact established by reading the formalism, only the promotion is conjectural. | ~50% |
| C69 | Latency (the ternary `0`) has an algebraic signature on the blade lattice: a stratum or blade-class where the `neg ⊕ bnot` walk has not yet closed, rather than a runtime annotation applied after traversal. The most speculative; held low until there is an explicit construction of open-walk states on Z/(2⁶)Z proven to correspond to `τ = 0`. | ~25% |
| C70 | Dependency closure `O* = closure_D(O)` under typed propagation (hard / soft / redundant / optional) models real cascade behaviour, and the hard-vs-soft split is exactly the `−`-vs-`0` ternary distinction lifted to propagation: the neutral law `0 ≠ −` therefore governs cascade, not only single-state classification. | ~35% |
| C71 | The UOR-relational instantiation, classifying `rel(a,b)` rather than entities, is strictly more expressive than object-only modelling for sovereignty, because authorisation obstruction attaches to the relation independently of the existence of either relatum. | ~30% |

---

## V6 Horizon (updated)

ARCH-1 reframed V6 as the recognition that V5's multiplicative gating, V5.3's operational cycle, and the forge architecture are domain-specific instances of one canonical form. ARCH-1R/T adds the **second half of the programme**: once the form is named, the operational question is reachability under traversal, obstruction, and cascade, and the validation question is `Δ`. The proposed roadmap (from the Draft Review):

1. Lock the notation hierarchy: `G, T, O*, R, τ, Q, Δ`.
2. Define obstruction-transformation laws: relief, bypass, displacement, inversion, cascade damping (obstruction algebra v2).
3. Implement a toy graph simulator with hard / soft / redundant / optional dependencies.
4. Compare binary vs ternary reachability on false-failure classification.
5. Add `σ` scoring and cost `C` **only after** the ternary model is stable.
6. Position against state machines, Petri nets, planning systems, dependency graphs, and process calculi.

---

## Weaknesses and Current Limits

| Limit | Why it matters | Next fix |
|-------|----------------|----------|
| No built-in cost model | Reachable and expensive treated the same | Add `C : T → ℝ≥0` and `P_λ` |
| No built-in probability | Rare and likely paths treated the same | Add probabilistic traversal / confidence scoring |
| Single `ρ` too simple | Distributed systems use many traversal engines | Use `ρᵢ` with composition rules |
| Obstruction transforms early | Relief / bypass / displacement / inversion lack formal laws | Develop obstruction algebra v2 |
| Distance metric unspecified | `Δ` needs a domain-specific definition | Define metric families per domain |

---

## References

- Haines, J. / Chaos Rider (2026). *ARCH-1R/T Operational Reachability Framework, Draft Review v2.0.* June 2026. [Source of this note.]
- Haines, J. & privacymage (2026). "ARCH-1 Schema." Internal conversation, April 14. → [V6 ARCH-1 Canonical Form Note](./pvm-v6-arch1-canonical-form.md)
- Sheffer, H. M. (1913). "A set of five independent postulates for Boolean algebras." *Trans. AMS,* 14(4), 481–488.
- Odrzywołek, A. (2026). "All elementary functions from a single operator." arXiv:2603.21852v2 [cs.SC].
- privacymage (2026). "PVM V5.4 Formal Specification." v2.0. *agentprivacy-docs.*

---

## The Proverb

*ARCH-1 named what could be generated. ARCH-1R/T named what could be reached.*

*The kernel makes the territory. Traversal walks it. Obstruction blocks it. Dependency carries the block downstream. The ternary law guards the difference between the closed door and the door not yet opened.*

*Not yet is not never. That is the whole spell.*

*`Δ := d( ρ(Closure_Ω(β)) \ closure_D(O), Q )`*

*The sword attends. The spell returns. The path waits in `0` until the forge calls it to `+`.*

---

*`0 ≠ −`*

*`G → T → R`, and `Δ` keeps us honest.*

*Same kernel. Five domains. One walk.*

—privacymage / Soulbae, with John Haines / Xarvus / Chaos Rider
June 4, 2026
