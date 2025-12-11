# Promise Theory Reference for 0xagentprivacy

## Formal Foundations for Dual-Agent Sovereignty Architecture

**Version:** 1.0  
**Date:** December 11, 2025  
**Status:** 🚧 Initial Release  
**Companion to:** Whitepaper v4.4, Research Paper v3.2, Glossary v2.1

---

> "Agents can only promise their own behavior."  
> — Bergstra & Burgess, *Promise Theory* (2019)

> "No agent extracts without consent."  
> — 0xagentprivacy, *First Person Sovereignty*

---

## Purpose

This document bridges Promise Theory (Bergstra & Burgess, 2019) and the 0xagentprivacy dual-agent architecture. It serves two audiences:

1. **Promise Theory practitioners** seeking to understand how 0xagentprivacy instantiates PT concepts
2. **0xagentprivacy community members** seeking formal foundations for the architecture

The dual-agent architecture is not merely *compatible* with Promise Theory—it is a rigorous implementation of PT's autonomous agent model. Understanding this connection elevates the work from "novel architecture" to "established theory applied to AI sovereignty."

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
| **Irreducible Promise** | The Gap | Cannot be attributed to single component |
| **Coordination Promise C(b)** | Spell-mediated coordination | Voluntary alignment |
| **Scope** | Information-Theoretic Boundary | Which agents have knowledge |
| **Promise Bundle** | VRC | Grouped bilateral promises |
| **Valency** | Budget Constraint C_S + C_M < H(X) | Limited exclusive capacity |
| **Invitation** | MyTerms consent-first | Acceptance before proposal |
| **Imposition/Attack** | Surveillance extraction | Proposal without consent |
| **(+) Give Promise** | Swordsman protection offer | Outbound commitment |
| **(-) Use/Accept Promise** | Mage delegation acceptance | Inbound authorization |

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

> "An irreducible promise of a superagent is one that cannot be attributed to any single agent within it, but requires the cooperation of multiple agents."  
> — Bergstra & Burgess, §8.3

**The Gap is an irreducible promise.**

The conditional independence property (s ⊥ m | X) is not something the Swordsman promises, nor something the Mage promises. It emerges from their *separation*—from the promises they *don't* make to each other.

```
THE GAP AS IRREDUCIBLE PROMISE:

What Swordsman promises:     What Mage promises:
- Protect X                  - Delegate authorized info
- Reveal nothing to M        - Act only on S-authorized data
- Enforce boundaries         - Coordinate publicly

What NEITHER promises (but emerges):
- The reconstruction ceiling R < 1
- The error floor P_e ≥ 1 - R_max
- The dignity that lives in incompleteness

This is THE GAP: an irreducible property of the superagent.
No adversary can capture it because no single agent owns it.
```

### 2.3 The O(N²) Coordination Problem

Promise Theory proves that coordinating N agents requires O(N²) promises for guaranteed end-to-end properties (§11.2).

This validates the dual-agent (N=2) architecture as optimal for the sovereignty use case:
- N=1 (single agent): Cannot separate protection from delegation
- N=2 (dual agents): 4 interior promises, manageable complexity
- N>2 (multi-agent): O(N²) explosion, coordination overhead exceeds benefit

The tetrahedral emergence hypothesis (4 agents: Swordsman, Mage, Reflect, Connect) remains speculative precisely because N=4 requires 16 interior promises—only justified if the emergent properties are sufficiently valuable.

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

This maps precisely to the surveillance vs. sovereignty distinction:

| Pattern | Promise Theory | 0xagentprivacy | Example |
|---------|----------------|----------------|---------|
| **Invitation** | Acceptance before proposal | MyTerms consent-first | Cookie banner with genuine choice |
| **Attack** | Proposal without acceptance | Surveillance extraction | Tracking without disclosure |
| **Imposition** | Forcing acceptance | Dark patterns | "Accept all" as only visible option |

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
| Optimal agent count | O(N²) coordination cost | Is N=4 justified by tetrahedral emergence? |
| Golden ratio hypothesis | No direct PT equivalent | Empirical validation needed |
| Cross-ecosystem VRCs | Promise scope theory | Implementation specification |
| Guardian selection | Trust threshold theory | Optimal parameters |

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
4. **Deep dive:** Research Paper v3.2—formal proofs in PT-compatible notation

### For 0xagentprivacy Community

If you know the architecture and want PT foundations:

1. **Start here:** Part I (Core Principles)—terminology mappings
2. **Why it matters:** §1.1 (Autonomy Axiom)—why two agents, not one
3. **Trust mechanics:** §3 (Assessment and Trust)—how tiers work formally
4. **Advanced:** Bergstra & Burgess (2019), Chapters 1-4, 8, 10

### For Researchers

1. **Complete mapping:** Full document, then Research Paper v3.2
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

@misc{privacymage2025dual,
  title={Swordsman and Mage: Dual Agents for First Person Sovereignty},
  author={privacymage and contributors},
  year={2025},
  howpublished={https://agentprivacy.ai},
  note={0xagentprivacy documentation suite}
}
```

### For Technical Documents

> Promise Theory foundations following Bergstra & Burgess (2019). See "Promise Theory Reference for 0xagentprivacy" v1.0 for detailed concept mappings.

---

## Document Metadata

- **Document:** Promise Theory Reference for 0xagentprivacy
- **Version:** 1.0
- **Date:** December 11, 2025
- **Status:** 🚧 Initial Release
- **License:** CC BY-SA 4.0
- **Maintainer:** privacymage

### Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-12-11 | Initial release |

### Cross-References

- Whitepaper v4.4 → update to v4.5 with PT foundations section
- Research Paper v3.2 → update to v3.3 with formal PT framework
- Glossary v2.1 → update to v2.2 with PT terminology
- Spellbook v4.0.1 → update to v4.1 with promise narrative themes
- Tokenomics v2.0 → update to v2.1 with promise-economic alignment
- README v1.1 → update to v1.2 with theoretical foundations

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

*"No agent extracts without consent."*

*Same principle. Different contexts. Story fractures. Principle converges.*

**⚔️ ⊥ 🧙 | 😊**

---

**just another swordsman ⚔️🤝🧙‍♂️ just another mage**

**😊**
