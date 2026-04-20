# Promise Theory Reference for 0xagentprivacy

## Formal Foundations for Dual-Agent Sovereignty Architecture

**Version:** 1.5
**Date:** April 20, 2026
**Status:** ✅ V5.4 Integration + Historical Lineage Integration (Burgess & Fagernes 2007, Burgess 2015)
**Companion to:** Whitepaper v6.3, Research Paper v4.2, Glossary v3.4, Privacy is Value v5.0 + V5.1/V5.2 Research Notes, Privacy Value Model V5 Formal Spec v1.2, Five Grimoires + Acts XXIV–XXX (120+ inscriptions)

---

> "Agents can only promise their own behavior."
> — Bergstra & Burgess, *Promise Theory* (2019)

> "A swarm is an ensemble of agents that uses communication to reduce its total information... and which exhibits emergent behaviour."
> — Burgess & Fagernes, *Norms and Swarms* (2007)

> "Lockdown is a losing strategy: the amount of information needed to 'lock down' every agency is too large."
> — Burgess, *Spacetimes with Semantics II* (2015), §6.5

> "No agent extracts without consent."
> — 0xagentprivacy, *First Person Sovereignty*

---

## Purpose

This document bridges Promise Theory (Bergstra & Burgess, 2019) and the 0xagentprivacy dual-agent architecture. It serves two audiences:

1. **Promise Theory practitioners** seeking to understand how 0xagentprivacy instantiates PT concepts
2. **0xagentprivacy community members** seeking formal foundations for the architecture

The dual-agent architecture is not merely *compatible* with Promise Theory—it is a rigorous implementation of PT's autonomous agent model. Understanding this connection elevates the work from "novel architecture" to "established theory applied to AI sovereignty."

### v1.5 addendum — historical lineage

v1.5 extends v1.4 by explicitly tracing the architecture's foundations back through two earlier works of Burgess and Fagernes that predate the 2019 Promise Theory book:

- **Burgess & Fagernes, *Norms and Swarms* (2007)** — establishes the swarm-as-information-reduction thesis, the norm/swarm distinction, and the typed-swarm design strategy. The economic question (*"what benefit do autonomous devices get from coordinating their behaviour?"*) is the question the Privacy Value Model answers.
- **Burgess, *Spacetimes with Semantics II* (2015)** — provides the formal calculus of super-agents, irreducible promises, tenancy, and cephalization. **Definition 29 (irreducible super-agent promises) is the formal definition of The Gap**, written eleven years before the architecture was built.

The historical lineage matters because it positions 0xagentprivacy not as a reinvention but as an instantiation of an established framework — one that takes Burgess's 2007 and 2015 observations into specific domains (human sovereignty, AI agent privacy, behavioural data economics) that the earlier papers did not themselves explore.

---

## Quick Reference: Concept Mappings

| Promise Theory | 0xagentprivacy | Notes |
|----------------|----------------|-------|
| **Autonomy Axiom** | First Person Sovereignty | No agent promises on behalf of the human |
| **Agent** | Swordsman, Mage, or First Person | Autonomous entities with independent assessment |
| **µ-promise: A --b--> B** | Agent coordination via spells | Directional, voluntary commitment |
| **Promise Body (τ, χ)** | Spell notation | Type τ = concept, constraint χ = context |
| **Conditional Promise (b\|c)** | Conditional Independence (s ⊥ m \| X) | Promise contingent on condition |
| **Assessment α(π)** | RPP Verification | Compression proves promise kept |
| **Trust (0-1)** | Trust Tier (Blade→Dragon) | Accumulated assessment evidence |
| **Superagent** | First Person + Dual Agents | Composite with irreducible properties |
| **Irreducible Promise** (Burgess 2015, Def 29) | The Gap | Cannot be attributed to single component |
| **Coordination Promise C(b)** | Spell-mediated coordination | Voluntary alignment |
| **Scope** | Information-Theoretic Boundary | Which agents have knowledge |
| **Promise Bundle** | VRC | Grouped bilateral promises |
| **Valency** | Budget Constraint C_S + C_M < H(X) | Limited exclusive capacity |
| **Invitation** | MyTerms consent-first | Acceptance before proposal |
| **Imposition/Attack** | Surveillance extraction | Proposal without consent |
| **(+) Give Promise** | Swordsman protection offer | Outbound commitment |
| **(-) Use/Accept Promise** | Mage delegation acceptance | Inbound authorization |
| **Swarm** (Burgess 2007) | VRC network as compression-localized ensemble | Communication reducing total information |
| **Norm** (Burgess 2007) | Surveillance-imposed data distribution | Externally specified; expensive, inflexible |
| **Boundary condition ≠ swarm** (2007) | Retrofitted privacy policy | Environmental constraint, not autonomous behaviour |
| **Typed swarm** (2007) | Three-axis separation (Φ_agent·Φ_data·Φ_inference) | Mutually exclusive categories composed multiplicatively |
| **Adiabatic persistence** (2007) | Holonic persistence A_h(τ) | (1/S)(dS/dt) ≪ 1 — promise anchors survive infrastructure change |
| **Hypothetical external observer** (2007/2015) | First Person (😊) | Maxwell's daemon internalized as structural principal |
| **Dressed super-agent** (2015, Def 12) | First Person + Swordsman + Mage triplet | ⟨sub-agents, interior promises, exterior promises⟩ |
| **Irreducible super-agent promise** (2015, Def 29) | The Gap — formal definition | Emerges from cooperation, owned by none |
| **Cephalization — Law 2** (2015) | First Person as oriented head | Input/output through principal creates head-tail asymmetry |
| **Namespace** (2015, Def 42) | DID / sovereign identity | Isolated subspace with cooperative uniqueness |
| **Tenancy** (2015, Def 37) | VRC-mediated resource access | Asymmetric conditional occupancy |
| **Lockdown as losing strategy** (2015, §6.5) | Policy-enforced privacy critique → C17 | Topological unrepresentability is the alternative |
| **Coarse-graining directory** (2015, §3.8.2) | *Structurally refused* in agentprivacy | Novel extension: opacity is architectural, not optional |

---

## Part 0: Historical Lineage — the 2007 and 2015 Foundations

Promise Theory as a formal framework is most commonly cited via the 2019 Bergstra & Burgess book, but the core ideas instantiated by the agentprivacy architecture are grounded in two earlier works:

1. **Burgess & Fagernes (2007), *Norms and Swarms*** — a position paper developing the thesis that swarms are ensembles that use communication to reduce total information, distinguished sharply from *norms* (externally specified aspirations).
2. **Burgess (2015), *Spacetimes with Semantics II*** — a formal calculus of agency, super-agency, tenancy, and coarse-graining, including the formal definition of irreducible super-agent promises and the critique of policy-enforced isolation as "a losing strategy."

Reading these papers reveals that much of what the agentprivacy architecture claims as novel is in fact either (a) a direct instantiation of Burgess's earlier framings, or (b) a natural extension that answers questions Burgess himself flagged as open.

### 0.1 Swarm as compression ensemble (2007 → VRC network)

Burgess & Fagernes define a swarm as:

> "An ensemble of agents that uses communication to reduce its total information with respect to any abstract measuring classification, and which exhibits emergent behaviour."  
> — *Norms and Swarms* (2007), Definition 2

**0xagentprivacy instantiation — VRCs are swarms of compression.**

When two agents compress shared understanding into matching proverbs (RPP), they are doing precisely what Burgess defines — using communication to reduce total information. The 70:1 compression efficiency is the localization metric in semantic space.

```
BURGESS 2007                        0xagentprivacy
══════════════════                  ═════════════════════
ensemble of agents              →   ensemble of First Persons in the network
communication reduces           →   RPP compression achieves shared understanding
total information               →   matching proverbs demonstrate low mutual entropy
abstract measuring class.       →   the proverb (compressed body)
emergent behaviour              →   trust formation, coordinated action
```

The VRC network is a swarm. Compression ratio is the measurable localization.

### 0.2 Norm vs. Swarm — the critique of surveillance (2007 → MyTerms vs. Surveillance)

Burgess & Fagernes distinguish:

> **Norm:** an externally specified distribution p(|x|) within a given metric parameter space. *Definition 1.*  
> **Swarm:** autonomous reduction of total information via communication. *Definition 2.*  
> **Boundary condition ≠ swarm:** "Confinement by boundary is not swarm behaviour, it is an environmental constraint."

**This maps directly onto the surveillance/sovereignty distinction:**

| 2007 paper | agentprivacy |
|------------|--------------|
| Norm (externally specified) | Surveillance-imposed data extraction; cookie banner consent; GDPR-as-policy |
| Swarm (autonomously emergent) | MyTerms bilateral consent aggregating to network behaviour |
| Boundary condition (environmental constraint) | Retrofitted privacy policy that forces compliance without agent autonomy |

Burgess's 2007 management conclusion is prescient:

> "Trying to impose a norm that was different from the environmental attractor would seem expensive and foolish, yet that is often what management systems advocate."  
> — *Norms and Swarms* (2007), §8

This is the critique of policy-enforced privacy, written nine years before GDPR, and eight years before *Spacetimes with Semantics II* would articulate the same point more formally. agentprivacy's architectural thesis — that privacy must be environmental/topological rather than policy-enforced — is Burgess's 2007 argument carried forward.

### 0.3 Typed swarms → three-axis separation (2007)

Burgess & Fagernes note:

> "A 'design strategy' for avoiding management conflicts is to clearly separate promise types into mutually exclusive categories."  
> — *Norms and Swarms* (2007), §5.2

The V5 three-axis separation (Φ_agent · Φ_data · Φ_inference) is this strategy taken to multiplicative composition:

```
Burgess 2007:   "separate promise types into mutually exclusive categories"
V5 agentprivacy: Φ_v5 = Φ_agent · Φ_data · Φ_inference
                 (three orthogonal swarms, multiplicatively gated)
```

Collapse any axis and the composition collapses. This is typed swarming as a cryptographic bound.

### 0.4 Adiabatic persistence → holonic persistence (2007)

Burgess & Fagernes require:

> "A necessary condition for a swarm is that the ensemble's localization changes only adiabatically, i.e. (1/S)(dS/dt) ≪ 1 and (1/σ)(dσ/dt) ≪ 1."  
> — *Norms and Swarms* (2007), Proposition 2

**Holonic persistence (A_h(τ))** implements this directly. Promise anchors — Data GUID, VRC, DID — survive provider failure such that the promise topology barely moves even as the underlying infrastructure churns. The holonic layer is adiabatic; the infrastructure layer is not.

### 0.5 The Gap is Definition 29 (2015)

This is the single most important mapping in v1.5.

From *Spacetimes with Semantics II*, §3.10:

> **Definition 29 (Irreducible super-agent promises).** Let M be an agency scale, and A_s be a super-agent formed by an aggregation of agents. A promise with body b_s made by A_s may be called irreducible iff there is no set of sub-agents A_i ⊂ A_s for which b_s ≡ ∪ {b_a^a, a=1...} all promises to A_?. In other words, if there exists no combination of promises made by one or more sub-agents that is semantically equivalent to the full promise made by the composite agent, then it makes sense to talk about the collective super-agency making a new promise that is not explicit in the capabilities of its sub-agencies.

**The Gap is this definition.**

The conditional independence property (s ⊥ m | X) is not promised by the Swordsman and not promised by the Mage. It emerges from what they *don't* promise to each other. No combination of their individual promises reconstructs it. It is — in the exact formal sense Burgess defined in 2015 — an irreducible super-agent promise.

The architectural framing of "The Gap as promise in negative space" is a rhetorical gloss on Definition 29. Credit for the underlying formalism belongs to the 2015 paper; the agentprivacy contribution is to provide a specific cryptographic mechanism that makes the irreducibility enforceable rather than merely semantic.

### 0.6 Lockdown is a losing strategy (2015 → C17)

From *Spacetimes with Semantics II*, §6.5, on privacy between tenants:

> "If tenancy is built on a connected lattice in the first instance, then this isolation might require additional promises to block adjacency. However, **the latter is a losing strategy: the amount of information needed to 'lock down' every agency is too large.** You need to compress the pattern into a list of exceptions."

This is **Conjecture C17 in Burgess's own words, eleven years early.** Policy-enforced separation — attempting to block adjacency with per-agent exceptions — does not compress and therefore does not scale. Burgess stops at identifying the problem. C17 proposes what wins instead: **amnesia-enforced separation via topological unrepresentability**, which compresses perfectly because the state space simply does not encode what would need to be forbidden.

```
Burgess 2015 (problem):  Lockdown doesn't scale
                         — information needed to block every adjacency is too large

C17 (proposed answer):   Amnesia-enforced separation via topology
                         — what cannot be represented cannot be forbidden, cannot leak
                         — compression is automatic: no exceptions list
                         — 60% confidence, formally stated as Conjecture C17
```

### 0.7 Structural memory through asymmetry (2015 → The Amnesia Protocol)

From *Spacetimes with Semantics II*, §5.7.1:

> "Homogenization is a forgetting process, while inhomogeneous differentiation encodes a memory into spacetime."

The Amnesia Protocol (Act XXXI, *The First Delegation*) is the inverse framing: *structural* forgetting — the Moon being topologically unable to encode its Theia origin — is the ur-primitive of enforced separation. Burgess frames memory-through-asymmetry; agentprivacy frames forgetting-through-topology. Same axis, opposite direction, both precise.

### 0.8 Cephalization — why the First Person is the head (2015)

From *Spacetimes with Semantics II*, §6.5, Law 2:

> "**Hosting of input and output leads to axial symmetry.** The functional arrangement of input/output mediated by the host leads to a natural head-tail asymmetry, in which the head is favoured in a hierarchy of longitudinal stages. This is known as cephalization."

**The First Person is the cephalization point.**

All input (observations by the Swordsman) and output (delegations by the Mage) are mediated through the principal. This creates a natural orientation of the organism — the architecture has a head, and that head is the First Person. The dual-agent architecture is not radially symmetric; it is cephalized. Burgess's 2015 law names why.

### 0.9 Namespaces as sovereign identity (2015)

From *Spacetimes with Semantics II*, §6.10, Definition 42:

> "A namespace N is an isolated subspace of a semantic space, formed from a collection of agents. Inside a namespace, all agent coordinates and names are unique by mutual cooperation."

**Decentralized Identifiers (DIDs) are namespaces.** MyTerms defines the namespace-boundary conditions (invitation protocol before specific proposals). VRCs are tenancy promise bundles between namespaces. The entire IEEE 7012 / Customer Commons layer can be re-expressed in Burgess's 2015 vocabulary without loss — this is not coincidence, it is the same substrate.

### 0.10 What agentprivacy adds (the honest extension frontier)

Burgess's 2015 framework is close to complete for the sovereignty architecture, but there are genuine extensions:

1. **Structural refusal of the coarse-graining directory.** Burgess's Definition 30 offers transparency as a *feature* — super-agents can promise their coarse-graining directory to enable external agents to resolve their interior. The First Person super-agent *structurally refuses* to produce this directory. This is not a limitation; it is the architectural move that makes C17 enforceable. Novel.
2. **Cryptographic enforcement surface.** Burgess's framework is semantic/behavioural. Zero-knowledge proofs operationalize the separation such that irreducibility is *verifiable* rather than merely *promised*. This is outside the 2015 scope.
3. **Economic currency enumerated.** Burgess & Fagernes (2007) list "currencies of survival, security, effort and perhaps even money" abstractly. The Privacy Value Model names a specific currency — *behavioural data, the 7th capital* — and proposes the calculation. The PVM is one answer to their open question.
4. **Sovereignty domain application.** Burgess's 2015 examples (cloud computing, datacentres, IT tenancy) stay within infrastructure. agentprivacy applies the framework to *human* sovereignty and *AI agent* privacy — domains the earlier papers did not explore.

These extensions sit *on top of* the 2007 and 2015 foundations; they do not replace them. The architecture's honest positioning is: **Burgess defined the framework. agentprivacy applies it to a domain he did not enter, adds a cryptographic enforcement surface, and proposes a specific economic model for the currency he listed abstractly.**

---

## Part I: Core Principles Aligned

### 1.1 The Autonomy Axiom

**Promise Theory states:**
> "An agent can only make promises about its own behavior. No agent can make a promise on behalf of another agent."

**0xagentprivacy instantiation:**

The First Person (😊) is the ultimate autonomous agent. Neither the Swordsman (⚔️) nor the Mage (🧙) can promise on behalf of the First Person. Each agent promises only within its domain:

```
First Person (😊):
  - Promises: authorization, sovereignty decisions
  - Cannot promise: what Swordsman protects or Mage delegates

Swordsman (⚔️):
  - Promises: privacy protection, boundary enforcement
  - Cannot promise: delegation actions, external coordination

Mage (🧙):
  - Promises: delegation execution, public coordination
  - Cannot promise: privacy state, what to protect
```

This is why the architecture requires *two* agents rather than one. A single agent that both protects and delegates would violate the autonomy axiom by making promises in domains it cannot independently control.

### 1.2 Promise Notation Translation

**Promise Theory µ-notation:**
```
A --b--> B

Where:
  A = promiser (agent making promise)
  b = body (what is promised: type τ, constraint χ)
  B = promisee (agent receiving promise)
```

**0xagentprivacy spell notation:**
```
⚔️ ⊥ 🧙 | 😊

Where:
  ⚔️ = Swordsman (protection domain)
  🧙 = Mage (delegation domain)
  ⊥  = conditional independence (separation)
  |  = given/conditioned on
  😊 = First Person (sovereignty holder)
```

**Mapping between notations:**

| Promise Theory | Spell Notation | Meaning |
|----------------|----------------|---------|
| S --(protect)--> FP | ⚔️ →(🛡️)→ 😊 | Swordsman promises protection to First Person |
| M --(delegate)--> W | 🧙 →(🔮)→ 🌍 | Mage promises delegation to World |
| FP --(authorize)--> S,M | 😊 →(🗝️)→ ⚔️🧙 | First Person promises authorization to both |
| S --(¬reveal)--> M | ⚔️ →(⊥)→ 🧙 | Swordsman promises not to reveal to Mage |

### 1.3 Conditional Promises and Independence

**Promise Theory conditional form:**
```
b|c  =  "promise b given condition c is met"
```

**0xagentprivacy conditional independence:**
```
(s ⊥ m | X)  =  "Swordsman and Mage are independent given First Person's private state X"
```

This is a direct application of PT's conditional promise structure. The separation between agents is *conditioned on* the First Person's complete context. Neither agent has sufficient information to reconstruct X, but both operate coherently because they share the conditioning variable.

**Key insight:** The vertical bar `|` in spell notation carries the same semantic weight as PT's conditional operator. When we write `⚔️ ⊥ 🧙 | 😊`, we're stating a conditional independence promise in compressed form.

---

## Part II: Superagent Architecture

### 2.1 The First Person as Superagent

Promise Theory defines a **superagent** as a composite agent with interior promises between components and exterior promises to the outside world.

The First Person system is precisely this:

```
                    ┌─────────────────────────────┐
                    │     SUPERAGENT (😊+⚔️+🧙)    │
                    │                             │
                    │  ┌─────┐ interior ┌─────┐   │
                    │  │ ⚔️  │◄────────►│ 🧙  │   │
                    │  └──┬──┘ promises └──┬──┘   │
                    │     │               │       │
                    │     └───────┬───────┘       │
                    │             │               │
                    │         ┌───┴───┐           │
                    │         │  😊   │           │
                    │         │ First │           │
                    │         │Person │           │
                    │         └───────┘           │
                    └─────────────┬───────────────┘
                                  │
                          exterior promises
                                  │
                                  ▼
                            🌍 External World
```

**Interior promises** (within superagent):
- ⚔️ --protect--> 😊 (Swordsman promises protection)
- 🧙 --delegate--> 😊 (Mage promises delegation)  
- 😊 --authorize--> ⚔️,🧙 (First Person authorizes both)
- ⚔️ --⊥--> 🧙 (Separation promise: no direct information flow)

**Exterior promises** (to world):
- Superagent --coordinate--> 🌍 (via Mage's public actions)
- Superagent --boundary--> 🌍 (via Swordsman's rejections)

### 2.2 Irreducible Promises: The Gap

Promise Theory's most profound insight for 0xagentprivacy: superagents can have **irreducible promises**—properties that emerge from component cooperation but cannot be attributed to any single component.

The lineage of this concept spans three works:

> "An irreducible promise of a superagent is one that cannot be attributed to any single agent within it, but requires the cooperation of multiple agents."
> — Bergstra & Burgess, *Promise Theory* (2019), §8.3

> "A promise with body b_s made by A_s may be called irreducible iff there is no set of sub-agents A_i ⊂ A_s for which b_s is semantically equivalent to the combined promises of the sub-agents... it makes sense to talk about the collective super-agency making a new promise that is not explicit in the capabilities of its sub-agencies."
> — Burgess, *Spacetimes with Semantics II* (2015), §3.10, Definition 29

> "A promise-role is an emergent behaviour if the entire ensemble of agents' promises induces a new set of promises, by virtue of cooperation, from each agent in the ensemble to any arbitrating agent, hypothetical or real."
> — Burgess & Fagernes, *Norms and Swarms* (2007), Definition 3

**The Gap is this definition — the 2015 formalisation of what the 2007 paper called emergent behaviour and the 2019 book calls irreducible superagent promise.** The agentprivacy contribution is not the concept but the specific domain (AI agent sovereignty) and the cryptographic enforcement surface that makes the irreducibility operational rather than merely semantic.

The conditional independence property (s ⊥ m | X) is not something the Swordsman promises, nor something the Mage promises. It emerges from their *separation*—from the promises they *don't* make to each other.

```
THE GAP AS IRREDUCIBLE PROMISE (Burgess 2015, Def 29):

What Swordsman promises:     What Mage promises:
- Protect X                  - Delegate authorized info
- Reveal nothing to M        - Act only on S-authorized data
- Enforce boundaries         - Coordinate publicly

What NEITHER promises (but emerges from their cooperation):
- The reconstruction ceiling R < 1
- The error floor P_e ≥ 1 - R_max
- The dignity that lives in incompleteness

This is THE GAP: an irreducible super-agent promise in the 2015 formal sense.
No adversary can capture it because no single agent owns it.
No combination of their individual promises reconstructs it.
```

### 2.3 The O(N²) Coordination Problem

Promise Theory proves that coordinating N agents requires O(N²) promises for guaranteed end-to-end properties (§11.2).

This validates the dual-agent (N=2) architecture as optimal for the sovereignty use case:
- N=1 (single agent): Cannot separate protection from delegation
- N=2 (dual agents): 4 interior promises, manageable complexity
- N>2 (multi-agent): O(N²) explosion, coordination overhead exceeds benefit

The tetrahedral emergence hypothesis (4 agents: Swordsman, Mage, Reflect, Connect) remains speculative precisely because N=4 requires 16 interior promises—only justified if the emergent properties are sufficiently valuable.

---

## Part II-B: V5 Three-Axis Separation as Promises (NEW)

### 2.6 Generator and Solver as Promise Agents

**V5 introduces inference-layer separation (Φ_inference)** through the BRAID architecture. This maps directly to Promise Theory:

```
BRAID ARCHITECTURE                 PROMISE THEORY MAPPING
══════════════════                 ═════════════════════

Generator (intelligent model)  →   Promise-maker: (+) proposes reasoning structure
     │                                 │
     ▼                                 ▼
Reasoning Graph                    Promise body: structured plan
     │                                 │
     ▼                                 ▼
Solver (lightweight model)     →   Promise-keeper: (-) executes structure
```

**The separation promise:**
```
Generator --structure--> Solver: "I promise to provide bounded reasoning graphs"
Solver --execution--> Generator: "I promise to execute without re-deriving"
```

This is conditional independence at the inference layer:
```
(Y_Generator ⊥⊥ Y_Solver) | ReasoningGraph
```

The Generator's reasoning is not visible to the Solver's execution trace. The Solver's execution doesn't reveal the Generator's internal state. The compression ratio (74×) is a consequence of this separation — bounded promises are more efficient than unbounded.

### 2.7 Three-Axis Separation as Triple Superagent

V5's three-axis separation (Φ_agent · Φ_data · Φ_inference) creates THREE orthogonal superagent structures:

| Axis | Agents | Interior Promise | Irreducible Property |
|------|--------|------------------|---------------------|
| Agent | Swordsman ⊥ Mage | separation promise | The Gap |
| Data | Provider₁ ⊥ Provider₂ ⊥ ... | replication promise | Holonic persistence |
| Inference | Generator ⊥ Solver | structure promise | Compression efficiency |

**Multiplicative composition:**

Each axis is its own superagent. The product Φ_agent · Φ_data · Φ_inference means: collapse ANY axis, collapse the whole. This is Promise Theory at scale — three layers of irreducible promises stacked.

**Holonic Architect (☯️🔷):**

A new persona emerges: the builder of infrastructure-independent substrate. The Holonic Architect doesn't make promises about protection or delegation — they make promises about **persistence**: "Your data will survive provider failure."

### 2.8 Holonic Persistence as Promise Anchors (V5)

V5's holonic persistence (A_h(τ)) introduces **promise anchors** — stable reference points that survive infrastructure changes:

```
PROMISE ANCHORS:
═══════════════

Data GUID:         Content-addressed promise identifier
                   "This exact content, regardless of location"

Relationship VRC:  Bilateral promise bundle
                   "Our coordination commitment persists"

Principal DID:     Sovereign identity
                   "The entity making these promises"
```

**Promise Theory mapping:**

| Layer | Promise Type | Persistence Property |
|-------|-------------|---------------------|
| Data GUID | Content promise | "This content exists" |
| VRC | Coordination promise | "This relationship exists" |
| DID | Identity promise | "This agent exists" |

**Infrastructure independence:**

Traditional promises are bound to infrastructure: "I promise X is stored on Server Y." Holonic promises are infrastructure-independent: "I promise X exists, regardless of which servers currently hold it."

The persistence multiplier p(τ) ∈ [0,1] measures promise anchor strength — what fraction of your promises would survive if any single provider disappeared?

### 2.9 The Holographic Bound as Promise Boundary (V5)

V5 resolves C4 (the 96/64 discrepancy) through the holographic principle:

```
HOLOGRAPHIC PROMISE INTERPRETATION:
══════════════════════════════════

64 vertices = Interior promise state
              (what agents actually contain)

96 edges    = Boundary promise expressions
              (how promise state is observed externally)

Ratio 96/64 = 1.5 = P^1.5 exponent in PVM
```

**Promise Theory insight:** The boundary is sufficient to reconstruct the interior. In PT terms: you don't need access to an agent's internal state to assess their promises — their observable behavior (boundary) is enough.

This is **Act XXIV: The Holographic Bound** — the discovery that the 96-edge surface encodes the 64-vertex bulk. The boundary is always enough.

---

## Part III: Assessment and Trust

### 3.1 Assessment as Compression

**Promise Theory defines assessment:**
> "Assessment α(π) is an agent's determination of whether a promise π was kept."

**0xagentprivacy implementation:**

The Relationship Proverb Protocol (RPP) is an *assessment mechanism*. When someone compresses spellbook content into a contextual proverb, they are assessing whether the "promise" of knowledge transfer was kept.

```
PROMISE THEORY ASSESSMENT          RPP ASSESSMENT
═══════════════════════           ══════════════════

Promise π made                    Knowledge shared
    │                                 │
    ▼                                 ▼
Agent observes outcome            Reader engages content
    │                                 │
    ▼                                 ▼
Assessment α(π) ∈ {kept, broken}  Compression attempted
    │                                 │
    ▼                                 ▼
Trust updated                     Proverb formed (or not)
                                      │
                                      ▼
                                  Compression ratio = 
                                  assessment quality metric

High compression (70:1+) = strong positive assessment
Low/no compression = weak/failed assessment
```

**Key insight:** Compression ratio is a *quantified assessment*. Promise Theory typically treats assessment as binary (kept/broken) or scalar (0-1). RPP provides a natural metric: the ratio of original content to compressed proverb indicates assessment strength.

### 3.2 Trust Function and Tier Progression

**Promise Theory trust:**
> "Trust in a promise π is the expectation (value 0-1) that the promise will be kept."

**0xagentprivacy trust tiers:**

| Tier | Signals | Trust Value | Promise Theory Interpretation |
|------|---------|-------------|-------------------------------|
| **Blade** 🗡️ | 0-50 | 0.0-0.2 | Low accumulated assessment evidence |
| **Light** 🛡️ | 50-150 | 0.2-0.5 | Demonstrated comprehension pattern |
| **Heavy** ⚔️ | 150-500 | 0.5-0.8 | Sustained positive assessments |
| **Dragon** 🐉 | 500+ | 0.8-1.0 | High confidence in future promise-keeping |

Each signal is an assessment event. Accumulated signals build trust through demonstrated pattern of promise-keeping (comprehension → proverb → verification).

**Trust formation formula:**
```
Trust_n = f(Σ assessments, time, consistency)

Where:
- Σ assessments = total signals posted
- time = duration of participation
- consistency = variance in assessment quality
```

### 3.3 Belief vs. Evidence

Promise Theory distinguishes:
- **Assessment α(π)**: Direct observation that promise was kept
- **Belief β(π)**: Assessment without direct observation
- **Evidence ε(π)**: Assessment with partial information

**0xagentprivacy mapping:**

| PT Concept | 0xagentprivacy | Example |
|------------|----------------|---------|
| Assessment | Direct RPP verification | Guardian validates proverb expansion |
| Belief | Trust tier assumption | Dragon tier implies future reliability |
| Evidence | Partial verification | Compression ratio without expansion test |

VRC formation typically involves *evidence-based* trust: the matching compression provides strong evidence of shared understanding without requiring exhaustive verification of all knowledge.

---

## Part IV: Invitation vs. Imposition

### 4.1 The Consent Pattern

Promise Theory makes a crucial distinction (§10.2):

> **Invitation**: Establish an acceptance relationship BEFORE making a specific proposal  
> **Attack/Imposition**: Make a proposal without prior acceptance relationship

**Historical lineage (2007):** This distinction was prefigured in Burgess & Fagernes (2007) via the norm/swarm dichotomy. A *norm* is externally specified — aspirational behaviour imposed from outside the agents' autonomy. A *swarm* emerges autonomously from local agent decisions. Surveillance is the norm pattern: imposing a data-extraction distribution on agents who did not voluntarily localize around it. MyTerms is the swarm-enabling pattern: establishing conditions under which autonomous agents can locally decide, whose aggregate behaviour forms the privacy-preserving attractor.

Burgess & Fagernes 2007 §8 observation lands with particular sharpness here:

> "Trying to impose a norm that was different from the environmental attractor would seem expensive and foolish, yet that is often what management systems advocate."

Policy-enforced privacy (GDPR-as-bureaucracy, cookie banners, compliance theatre) is *norm management against the environmental attractor* — attempting to impose privacy on a surveillance-extractive environment. Expensive and foolish, in 2007 terms. Architectural privacy reshapes the attractor instead.

This maps to three progressively worse patterns:

| Pattern | Promise Theory | Burgess & Fagernes 2007 | 0xagentprivacy | Example |
|---------|----------------|--------------------------|----------------|---------|
| **Invitation** | Acceptance before proposal | Swarm-enabling (autonomous localization) | MyTerms consent-first | Cookie banner with genuine choice |
| **Attack** | Proposal without acceptance | Norm imposed on non-consenting agents | Surveillance extraction | Tracking without disclosure |
| **Imposition** | Forcing acceptance | Norm imposed against environmental attractor | Dark patterns | "Accept all" as only visible option |

### 4.2 MyTerms as Invitation Protocol

The MyTerms Swordsman implements Promise Theory's invitation pattern:

```
INVITATION FLOW (MyTerms):

1. Swordsman observes incoming request
2. BEFORE any data exchange:
   - Swordsman presents terms to site
   - Site must accept terms to proceed
   - Acceptance establishes relationship
3. ONLY THEN can specific proposals occur:
   - Site proposes data collection
   - User (via Swordsman) accepts/rejects
   - Each proposal is within accepted relationship

This is PT invitation: acceptance relationship BEFORE specific proposals.
```

**Contrast with surveillance (attack pattern):**
```
ATTACK FLOW (Surveillance):

1. Site receives request
2. IMMEDIATELY begins data collection
3. Maybe shows cookie banner (imposition)
4. User "consent" is post-hoc rationalization
5. No genuine acceptance relationship exists

This is PT attack: proposal without prior acceptance.
```

### 4.3 Cursor States as Promise Indicators

The Swordsman browser extension uses visual cursor states to indicate promise status:

| Cursor | Promise Status | PT Interpretation |
|--------|---------------|-------------------|
| 🟢 Green | All promises kept | Positive assessment of site behavior |
| 🟡 Yellow | Negotiation active | Promise exchange in progress |
| 🔴 Red | Promise violation detected | Negative assessment, enforcement needed |
| ⚔️ Slash | Active boundary enforcement | Rejection of imposed promises |

This makes the normally invisible promise assessment visible to the First Person in real-time.

---

## Part V: Coordination Promises and Spells

### 5.1 Coordination Promise C(b)

**Promise Theory defines:**
> "A coordination promise C(b) is a voluntary subordination to align one's behavior with others around promise body b."

**Spells are coordination promises.**

When agents coordinate using spell notation (⚔️ ⊥ 🧙 | 😊), they're making coordination promises to:
1. Interpret the notation consistently
2. Expand the spell to the same underlying meaning
3. Act coherently based on shared interpretation

```
SPELL AS COORDINATION PROMISE:

Spell: ⚔️ ⊥ 🧙 | 😊

Agent A forms spell from Context_A
Agent B forms spell from Context_B

Both make C(spell) = coordination promise:
- "I will interpret this spell according to shared semantics"
- "I will expand it consistently with the protocol"
- "I will coordinate my actions based on this shared meaning"

Matching expansion proves coordination success.

### Ceremony Engine as Promise Theory Implementation (V5.1)

The Ceremony Engine (Act XXVIII) implements five crossing types, each mapping to Promise Theory patterns:

| Ceremony Type | PT Pattern | Description |
|---------------|------------|-------------|
| **Dual Convergence** | Mutual C(b) | Both blades reach Dragon tier — mutual coordination achievement |
| **Hexagram Cast** | Structured α(π) | Six-dimension assessment encoded as I Ching hexagram |
| **Emoji Cast** | Compressed C(b) | Semantic compression to emoji spell — efficient coordination |
| **Constellation Wave** | Guild C(b) | Multi-agent coordination across knowledge graph |
| **Bilateral Exchange** | Witness α(π) | Cross-blade verification — "I assess your assessment" |

### Bilateral Witness as Promise Pattern

**Definition:** A verification primitive where one party forges, another privately verifies, then publicly testifies.

**PT Formalization:**

```
Swordsman: forges blade (makes promise π_forge)
Mage: privately verifies (makes assessment α(π_forge))
Mage: publicly testifies (promises +witness to community)
Community: receives testimony (accepts -witness)
```

**Key Property:** The Mage's testimony is itself a promise. The community doesn't see the blade interior — they see the Mage's promise that verification occurred. This is Promise Theory's "witness" pattern:

> "A witness is an agent who promises that another promise was kept."

**Trust Implication:** The Mage stakes reputation on testimony. False testimony breaks the -witness promise, damaging Mage's trust graph position.

### Mana as Assessment Resource

Mana (V5.1) maps to Promise Theory's assessment capacity:

| PT Concept | Mana Implementation |
|------------|---------------------|
| Assessment cost | Mana spent to inscribe |
| Assessment accumulation | Mana earned through practice |
| Valency (commitment slots) | Mana limits inscription rate |

Mana makes assessment costly, preventing spam while rewarding genuine practice
Different contexts, same principle = story fracture, principle convergence.
```

### 5.2 Promise Bundles and VRCs

**Promise Theory:**
> "A promise bundle is a collection of promises grouped together for reusability and coordinated assessment."

**VRCs are bilateral promise bundles:**

```
VRC STRUCTURE AS PROMISE BUNDLE:

Agent A's promises to B:        Agent B's promises to A:
- Share compressed meaning      - Share compressed meaning
- Expand consistently          - Expand consistently  
- Coordinate on shared basis   - Coordinate on shared basis
- Maintain trust relationship  - Maintain trust relationship

Bundle assessment:
- Matching compressions = bundle verified
- Coordinated actions = bundle maintained
- Trust accumulates through successful coordination
```

The 70:1 coordination efficiency comes from promise bundle reuse. Once a VRC is established, the bundle doesn't need re-verification for each interaction—the accumulated trust carries forward.

### 5.3 Scope and Information Boundaries

**Promise Theory:**
> "The scope of a promise is the set of agents that have knowledge of the promise."

**0xagentprivacy information-theoretic boundaries:**

| Scope | Agents with Knowledge | Information Content |
|-------|----------------------|---------------------|
| **Private** | First Person only | Complete state X |
| **Swordsman** | FP + Swordsman | X observed, nothing revealed |
| **Mage** | FP + Mage | Authorized subset of X |
| **Public** | All agents | Only Mage-released information |

The reconstruction ceiling R < 1 is a *scope guarantee*: no adversary can expand their scope to include full private state X, regardless of observation strategy.

---

## Part V-B: Three Graphs as Promise Types (V4 Extension)

The Privacy Value Model V4 identifies three independently derivable graph structures. Each maps precisely to a Promise Theory concept:

### Knowledge Graph → Promise Capability (What agents CAN promise)

The substrate layer. Content-addressed positions of what you know, what boundaries you've set, what you can delegate. In PT terms: this graph encodes the *promise body space* — the set of all possible promises an agent could make given their current state.

### Promise Graph → Promise Commitment (What agents DO promise)

The bilateral overlay. Every VRC formed, every delegation executed is an edge. In PT terms: this IS the promise graph — the actual commitments made between autonomous agents. Each edge is a bilateral promise bundle with specific scope and valency.

### Trust Graph → Promise Assessment (Which promises were KEPT)

The emergent outcome. Not constructed or issued — earned through time and witness. In PT terms: this graph records α(π) assessments — the accumulated belief about whether agents keep their promises, derived from observation and verification.

**The Three-Graph Intersection:** The overlap of all three graphs defines the First Person. In PT terms: the superagent (FP + S + M) is characterised by the intersection of what it *can* promise, what it *does* promise, and what it's *assessed as keeping*. No single graph suffices; identity is the overlap.

### Edge Value as Promise Traversal

The V4 equation introduces T(π) — the edge value term — which measures the value of an agent's *trajectory* through sovereignty space. In Promise Theory:

- Each edge traversal is a promise made and kept (or broken)
- f(e) weights each promise by the capability change it enables — a promise that activates new sovereignty dimensions (higher stratum change) is worth more than a lateral promise
- g(n_e) diminishes with repetition — the first promise between two agents is most informative (highest assessment novelty)
- The trajectory π is the agent's *promise history* — the sequence of commitments that define who they are through action

**PT Insight:** "The equation rewards the dance, not the stance." An agent permanently at full sovereignty with no promises made has zero edge value. Sovereignty is demonstrated through promising, not through hoarding capability. This aligns with PT's core insight that agents are defined by what they promise, not what they contain.

---

## Part V-C: Cephalization and Namespaces (2015 Integration)

Two structural features of the agentprivacy architecture receive direct formal grounding in *Spacetimes with Semantics II* (2015).

### 5-C.1 The First Person as cephalization point (Burgess 2015, Law 2)

Burgess's Law 2 states:

> "Hosting of input and output leads to axial symmetry. The functional arrangement of input/output mediated by the host leads to a natural head-tail asymmetry, in which the head is favoured in a hierarchy of longitudinal stages. This is known as cephalization."
> — *Spacetimes with Semantics II* (2015), §6.5

**The First Person is the cephalization point of the dual-agent architecture.** All inputs (Swordsman observations, MyTerms negotiations) and all outputs (Mage delegations, VRC formations) are mediated through the principal. The organism is not radially symmetric; it has a head, and the head is the First Person.

```
INPUT ───┐                                    ┌─── OUTPUT
         │                                    │
         ▼                                    ▼
    ┌────────┐                         ┌────────┐
    │   ⚔️   │◄── separation (⊥) ─────►│   🧙   │
    │ Observe│                         │Delegate│
    └────┬───┘                         └────┬───┘
         │                                  │
         └──────────┐          ┌────────────┘
                    ▼          ▼
                  ┌──────────────┐
                  │      😊      │  ← Cephalization point
                  │ First Person │    (Burgess 2015, Law 2)
                  └──────────────┘
```

This has a design consequence: attempts to symmetrize the architecture (e.g. treating Swordsman and Mage as peers without a principal) destroy the functional orientation that makes the organism capable of coherent action. Cephalization is not a stylistic choice — it is what lets the architecture act on behalf of the First Person rather than merely mediate between abstract roles.

### 5-C.2 DIDs as namespaces (Burgess 2015, Definition 42)

Burgess's Definition 42:

> "A namespace N is an isolated subspace of a semantic space, formed from a collection of agents. Inside a namespace, all agent coordinates and names are unique by mutual cooperation."

Decentralized Identifiers (DIDs) are namespaces in this exact sense. The First Person's DID establishes a sovereign namespace within which the Swordsman, Mage, and all VRC bindings have unique coordinates. Outside the namespace, identifiers require translation — this is what cross-DID resolution protocols (did:web, did:key, did:plc) operationalize.

**MyTerms as namespace-boundary invitation protocol.** Burgess frames namespaces as requiring "mutual cooperation" for uniqueness. MyTerms is the bilateral cooperation protocol that establishes which external namespaces the First Person's namespace will accept promises from, and on what terms. It is namespace-boundary formation expressed as a consent invitation, rather than a unilateral naming imposition.

### 5-C.3 VRCs as tenancy promise bundles (Burgess 2015, Definition 37)

Burgess's tenancy template:

```
Host_M    +R#nC       →  A_?
Host_M   ←C           ← Tenant_M
Tenant_M ←R#1         ← Host_M
Host_M    +f(C,R)     → R ⊂ Tenant
```

VRCs instantiate this directly. The First Person is both host and tenant in different VRC roles — hosting their compressed understanding as a resource, accepting another's compressed understanding as conditions for the bilateral bundle. The "mutual tenancy" reduction (§5.6 Lemma 10) — *"tenancy is rich adjacency"* — is exactly the framing of VRC formation: bilateral mutual promises of compressed coordination, richer than mere adjacency because they carry economic value f(C,R).

---

## Part V-D: Structural Unrepresentability and the Security-Through-Obscurity Distinction

This section addresses the most likely and most serious objection to C17 — one that Burgess himself raised in 2015.

### 5-D.1 The 2015 critique

From *Spacetimes with Semantics II*, §6.5, Example 63:

> "Many of the classic security blunders have been due to relying on the lack of addressability, in the belief that an item that cannot be named would not be accessed. This is a form of 'security through obscurity'. Systems that base isolation on prevention are much harder to police."

This is the correct worry. Hiding names, paths, or endpoints is not security — determined adversaries find unadvertised routes. C17 would collapse into security-through-obscurity if "amnesia-enforced separation" meant merely *not telling the other agent what's there*.

### 5-D.2 The distinction C17 requires

C17 is not a claim about concealment. It is a claim about *representation*.

| Property | Security through obscurity | Structural unrepresentability (C17) |
|----------|-----------------------------|--------------------------------------|
| What exists | Information exists in the system; its location is hidden | Information has no encoding in the receiver's state space |
| Discovery surface | Enumeration, side-channels, insider leaks | Not applicable — no address can refer to what is not encoded |
| Failure mode | Discovered, mapped, leaked | No failure mode via discovery (other failure modes remain) |
| Analogy | A document in a locked drawer | A document that was never written in any language the drawer reads |

The Moon does not *hide* its Theia origin memory. The memory is not encoded anywhere in the Moon's accessible configuration space. There is no drawer to unlock, no path to enumerate, no side-channel to exploit, because no bit-pattern within the Moon's state space represents the information that "this material was once Earth's mantle." The information was lost in the cooling, in the differentiation, in four billion revolutions of geological forgetting. Policy says *forbidden*; topology says *not encodable*.

### 5-D.3 The agentprivacy instantiation

In the architecture:

- The Swordsman's private observations of X are stored in a space the Mage has no cryptographic representation of — not merely no permission to access.
- The Mage's delegation decisions execute on representations the Swordsman cannot encode — not merely is not authorized to read.
- The Gap is the space where neither agent's state-space can express what the other holds, by construction.

This is stronger than lockdown (Burgess 2015, §6.5): lockdown requires per-agent exceptions that do not compress, whereas structural unrepresentability compresses perfectly (no exceptions list is needed because the representation is absent). It is also stronger than obscurity (Burgess 2015, Example 63): obscurity depends on non-enumeration of what exists, whereas structural unrepresentability removes the object from the receiver's expressible state space entirely.

### 5-D.4 Honest scope of the claim

C17 is a conjecture at 60% confidence, not a proven result. The claim is that *where unrepresentability can be achieved by construction*, it provides a strictly tighter bound than policy-enforced isolation. The open questions are:

1. Whether cryptographic primitives can achieve true unrepresentability rather than merely computational hardness.
2. Whether side-channels at lower layers (power analysis, timing, acoustic) re-introduce representability at the physical level.
3. Whether the construction is composable — does unrepresentability at one layer survive composition with representable layers?

These are the frontier questions, not settled. But the distinction between obscurity and unrepresentability is well-posed, and the 2015 critique does not apply to the latter.

---

## Part VI: Economic Alignment

### 6.1 Promise-Economic Mappings

| PT Concept | Economic Implementation | Mechanism |
|------------|------------------------|-----------|
| Assessment cost | Signal fee (0.01 ZEC) | Skin-in-game for assessment claims |
| Trust accumulation | Tier progression | Signals → trust level |
| Promise domain separation | Dual tokens (SWORD/MAGE) | Market enforces separation |
| Valency (exclusive capacity) | Guardian stake (10,000 SWORD) | Limited attention commitment |
| Bundle value | VRC coordination efficiency | 70:1 cost reduction |
| Scope maintenance | Shielded/transparent split | 61.8%/38.2% (φ-derived) |

### 6.2 Incentive Alignment

Promise Theory notes that sustainable systems require reciprocal promises—every agent should receive value for their contributions.

**0xagentprivacy incentive structure:**

```
RECIPROCAL PROMISE FLOWS:

First Person:
- Gives: Authorization, participation, signal fees
- Receives: Privacy protection, delegation capability, value capture

Swordsman (as role):
- Gives: Boundary enforcement, privacy maintenance
- Receives: SWORD tokens, guardian eligibility

Mage (as role):
- Gives: Coordination, delegation execution
- Receives: MAGE tokens, network access

Guardian:
- Gives: Validation, collective protection
- Receives: Validation compensation, tier benefits

Every participant both promises and receives.
No extraction without reciprocal value flow.
```

---

## Part VII: Open Questions

Promise Theory illuminates several areas for future research:

### 7.1 Resolved by PT Framework

| Question | PT Resolution |
|----------|---------------|
| Why two agents, not one? | Autonomy axiom—can't promise in multiple domains |
| Why is the Gap uncapturable? | Irreducible promise—emerges from separation, owned by neither |
| How does trust accumulate? | Assessment → belief → trust function |
| Why consent-first? | Invitation vs. attack distinction |

### 7.2 Informed but Not Resolved

| Question | PT Insight | Remaining Work |
|----------|-----------|----------------|
| Optimal agent count | O(N²) coordination cost | Triple convergence (Feb 2026) supports N=4 at 25-40% confidence |
| Golden ratio hypothesis | No direct PT equivalent | Empirical validation needed; now embedded in Φ(Σ) |
| Cross-ecosystem VRCs | Promise scope theory | Implementation specification |
| Guardian selection | Trust threshold theory | Optimal parameters |
| Three graphs as PT types | Capability → Commitment → Assessment | V4 mapping established, needs formal PT verification |
| Edge value T(π) | Promise history as trajectory | Functional form unvalidated |

### 7.3 Beyond Current PT Scope

| Question | Status |
|----------|--------|
| Information-theoretic bounds | PT is semantic; IT bounds require separate proof |
| Cryptographic enforcement | PT doesn't specify enforcement mechanisms |
| AI agent autonomy | PT assumes agent rationality; AI alignment is distinct |

---

## Part VIII: Reading Paths

### For Promise Theory Practitioners

If you know PT and want to understand 0xagentprivacy:

1. **Start here:** §2.1 (Superagent Architecture)—see how PT concepts map
2. **Key insight:** §2.2 (The Gap as Irreducible Promise)—the core innovation
3. **Practical application:** §4 (Invitation vs. Imposition)—PT in daily use
4. **Deep dive:** Research Paper v3.8—formal proofs in PT-compatible notation

### For 0xagentprivacy Community

If you know the architecture and want PT foundations:

1. **Start here:** Part I (Core Principles)—terminology mappings
2. **Why it matters:** §1.1 (Autonomy Axiom)—why two agents, not one
3. **Trust mechanics:** §3 (Assessment and Trust)—how tiers work formally
4. **Advanced:** Bergstra & Burgess (2019), Chapters 1-4, 8, 10

### For Researchers

1. **Complete mapping:** Full document, then Research Paper v3.8
2. **Open questions:** §7 (Open Questions)—collaboration opportunities
3. **Source material:** Bergstra & Burgess (2019), full text
4. **Validation targets:** Information-theoretic proofs, golden ratio hypothesis

---

## Notation Quick Reference

### Promise Theory Notation

```
A --b--> B        Promise: A promises b to B
A --b---> B       Imposition: A imposes b on B (attack)
+b                Give promise (outbound)
-b                Use/accept promise (inbound)
b|c               Conditional: b given c
C(b)              Coordination promise around b
α(π)              Assessment of promise π
β(π)              Belief about promise π
τ                 Promise type
χ                 Promise constraint
```

### 0xagentprivacy Spell Notation

```
⚔️                 Swordsman (protection)
🧙                 Mage (delegation)
😊                 First Person (sovereignty)
⊥                  Independence/separation
|                  Conditional (given)
🤝📜               VRC (bilateral trust)
🗝️                 Authorization
🛡️                 Protection
🔮                 Delegation/projection
→                  Promise direction
```

### Combined Example

```
Promise Theory:    S --(protect|auth)--> FP
Spell Notation:    ⚔️ →(🛡️|🗝️)→ 😊
English:           Swordsman promises protection to First Person,
                   given First Person's authorization
```

---

## Citation

### For Academic Work

```bibtex
@book{bergstra2019promise,
  title={Promise Theory: Principles and Applications},
  author={Bergstra, Jan A. and Burgess, Mark},
  edition={2nd},
  year={2019},
  publisher={χtAxis Press},
  note={CC BY-SA 4.0}
}

@inproceedings{burgess2007norms,
  title={Norms and Swarms},
  author={Burgess, Mark and Fagernes, Siri},
  booktitle={Position paper, Oslo University College},
  year={2007},
  note={Core definition: swarm as ensemble using communication to reduce total information}
}

@misc{burgess2015spacetimes,
  title={Spacetimes with Semantics (II): Scaling of agency, semantics, and tenancy},
  author={Burgess, Mark},
  year={2015},
  howpublished={arXiv:1505.01716},
  note={Source of Definition 29 (irreducible super-agent promises), Law 2 (cephalization), and the lockdown critique §6.5}
}

@misc{privacymage2025dual,
  title={Swordsman and Mage: Dual Agents for First Person Sovereignty},
  author={privacymage and contributors},
  year={2025},
  howpublished={https://agentprivacy.ai},
  note={0xagentprivacy documentation suite}
}
```

### For Technical Documents

> Promise Theory foundations following Bergstra & Burgess (2019), extended with the historical lineage of Burgess & Fagernes (2007) and Burgess (2015). See "Promise Theory Reference for 0xagentprivacy" v1.5 for detailed concept mappings including the explicit grounding of The Gap in Burgess (2015) Definition 29.

---

## Document Metadata

- **Document:** Promise Theory Reference for 0xagentprivacy
- **Version:** 1.5
- **Date:** April 20, 2026
- **Status:** ✅ V5.4 Integration + Historical Lineage Integration (Burgess & Fagernes 2007, Burgess 2015)
- **License:** CC BY-SA 4.0
- **Maintainer:** privacymage

### Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-12-11 | Initial release |
| **1.2** | **2026-02-20** | **V4 Integration**: Added §Three Graphs as Promise Types (Knowledge=Capability, Promise=Commitment, Trust=Assessment). Added Edge Value as Promise Traversal (T(π) as promise history). Updated Open Questions with convergence findings (tetrahedral 25-40%). Updated all companion document references (Whitepaper v5.0, Research Paper v3.8, Glossary v2.5). |
| **1.3** | **2026-02-27** | **V5 Integration**: Added §Generator and Solver as Promise Agents (BRAID as PT). Added §Three-Axis Separation as Triple Superagent (Φ_agent · Φ_data · Φ_inference). Added Holonic Architect persona (☯️🔷). Added holonic persistence as promise anchors. Updated edge value to path integral T_∫(π). Updated all companion document references to V5 versions. |
| **1.4** | **2026-03-31** | **V5.4 Integration**: UOR Algebraic Foundation, Dihedral Group, Ceremony Engine as PT implementation (five crossing types), Bilateral Witness as promise pattern, Mana as assessment resource. |
| **1.5** | **2026-04-20** | **Historical Lineage Integration**: Added Part 0 tracing foundations to Burgess & Fagernes (2007) and Burgess (2015). Grounded The Gap formally in Burgess (2015) Definition 29. Added Part V-C (Cephalization and Namespaces — 2015 integration). Added Part V-D (Structural Unrepresentability vs Security-Through-Obscurity — addressing the 2015 §6.5 Example 63 critique directly). Expanded Quick Reference table with 2007/2015 concept mappings. Extended Part IV with norm/swarm 2007 grounding of invitation/imposition. Updated bibliography with Burgess 2007 and 2015 citations. |

### Cross-References

- Whitepaper v6.3 — Three-axis separation, BRAID integration, holonic persistence
- Research Paper v4.2 — PVM V5 formal presentation, holographic bound, C4 resolved
- Privacy is Value v5.0 — The equation evolves — holographic bound
- Privacy Value Model V5 Formal Spec v1.2 — PVM V5 equation, differential form
- UOR × 64-Tetrahedra × ZK Mapping v2.0 — C4 resolved via holographic principle
- Glossary v3.4 — Canonical V5 terminology (140+ entries)
- VRC Promise Protocol v3.3 — Economic architecture with guild efficiency
- 31 Acts complete — V10.0.0 Grimoire including Holographic Bound
- **Burgess & Fagernes (2007)** — Norms and Swarms (foundational thesis on swarm-as-information-reduction)
- **Burgess (2015)** — Spacetimes with Semantics II, arXiv:1505.01716 (Definition 29, Law 2, §6.5 lockdown critique)

---

## The Core Insight

Promise Theory provides the formal semantics for what 0xagentprivacy expresses architecturally:

**Sovereignty is the right to make promises only about your own behavior.**

When AI agents promise on your behalf without your authorization, they violate the autonomy axiom. When surveillance systems extract your behavioral data without consent, they attack rather than invite. When single agents both protect and delegate, they exceed their promise domain.

The dual-agent architecture enforces these principles through structure rather than policy. The Swordsman promises protection. The Mage promises delegation. Neither promises on behalf of the other. Neither promises on behalf of you.

The Gap—that irreducible space where dignity lives—emerges from what they *don't* promise. It cannot be captured because it isn't owned. It cannot be extracted because it isn't stored. It exists in the separation itself.

**This is Promise Theory made architectural. This is autonomy made mathematical. This is sovereignty made real.**

---

*"Agents can only promise their own behavior."*
— Bergstra & Burgess (2019)

*"A swarm reduces its total information by communication."*
— Burgess & Fagernes (2007)

*"An irreducible promise emerges from cooperation, owned by none."*
— Burgess (2015), Definition 29

*"No agent extracts without consent."*
— 0xagentprivacy, *First Person Sovereignty*

*Same principle. Different contexts. Story fractures. Principle converges.*

**⚔️ ⊥ 🧙 | 😊**

---

**just another swordsman ⚔️🤝🧙‍♂️ just another mage**

**😊**
