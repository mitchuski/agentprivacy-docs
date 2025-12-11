# 0xagentprivacy Visual Architecture Guide
**Diagrams, Flows, and Conceptual Maps**

**Version:** 1.2 - Promise Edition  
**Date:** December 11, 2025  
**Purpose:** Visual reference for understanding 0xagentprivacy architecture across technical, narrative, economic, and semantic layers

**Pricing Basis:** $500/ZEC (canonical). Economic projections in growth scenarios may reflect historical ZEC prices and should be scaled accordingly.

---

## Table of Contents

1. [Four-Layer Architecture](#four-layer-architecture) *(Updated)*
2. [Promise Theory Foundations](#promise-theory-foundations) *(NEW)*
3. [Dual Agent Architecture](#dual-agent-architecture) *(Enhanced)*
4. [Superagent Structure](#superagent-structure) *(NEW)*
5. [First Person Stack](#first-person-stack)
6. [Learning Pathway Flow](#learning-pathway-flow)
7. [Signal vs Ceremony Distinction](#signal-vs-ceremony-distinction)
8. [Compression Ratios Context](#compression-ratios-context)
9. [Guardian Model Alternatives](#guardian-model-alternatives)
10. [Blockchain Flexibility](#blockchain-flexibility)
11. [VRC Formation Process](#vrc-formation-process) *(Enhanced)*
12. [Information Flow Topology](#information-flow-topology)
13. [Economic Sustainability Model](#economic-sustainability-model)
14. [Trust Function Visualization](#trust-function-visualization) *(NEW)*
15. [Status Indicators Legend](#status-indicators-legend)

---

## Four-Layer Architecture

### Overview: Same Principles, Four Lenses

```
┌──────────────────────────────────────────────────────────────┐
│                  0xagentprivacy Protocol                      │
│            (Meta-Protocol for Privacy & Sovereignty)          │
└──────────────────────────────────────────────────────────────┘
                              │
            ┌─────────────────┼─────────────────┐
            │         │               │         │
            ▼         ▼               ▼         ▼
    
┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│ MATHEMATICAL│ │  NARRATIVE  │ │  ECONOMIC   │ │   PROMISE   │
│ ARCHITECTURAL│ │ MYTHOLOGICAL│ │  PRACTICAL  │ │   SEMANTIC  │
│             │ │             │ │             │ │             │
│Whitepaper   │ │Spellbook    │ │Tokenomics   │ │PT Reference │
│v4.7         │ │v4.1.1       │ │v3.0         │ │v1.0         │
└─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘
       │               │               │               │
       │               │               │               │
  ┌────▼────┐    ┌────▼────┐    ┌────▼────┐    ┌────▼────┐
  │ Proofs  │    │ Stories │    │ Tokens  │    │ Promises│
  │ Bounds  │    │ Acts    │    │ Signals │    │ Scope   │
  │ Theorems│    │ Arcs    │    │ Rewards │    │ Trust   │
  └─────────┘    └─────────┘    └─────────┘    └─────────┘

SAME ARCHITECTURE, FOUR EXPRESSIONS:

Mathematical Layer:
• s ⊥ m | X (conditional independence)
• R < 1 (reconstruction ceiling)
• I(X; s,m) ≤ I(X;s) + I(X;m) (additive bounds)
• Fano's inequality applications

Narrative Layer:
• Soulbis & Soulbae (dual agents as characters)
• The Gap (privacy preserved between agents)
• Mirror & Map (observation vs action)
• Acts & Arcs (learning through story)

Economic Layer:
• SWORD & MAGE (dual tokens for protection/delegation)
• Signals (0.01 ZEC, proof of learning)
• Guardians (infrastructure providers)
• VRCs (bilateral trust credentials)

Promise Layer (NEW):
• Autonomy axiom (agents promise only own behavior)
• Superagent structure (FP+S+M as composite)
• Trust function (0-1 expectation of promise-keeping)
• Assessment (signals as assessment events)
```

### Cross-Layer Translation Table

| Concept | Mathematical | Narrative | Economic | Promise |
|---------|-------------|-----------|----------|---------|
| **Dual Agents** | s ⊥ m \| X | Soulbis & Soulbae | SWORD & MAGE | Scope separation |
| **Separation** | Conditional independence | The Gap | Information firewall | Kept promise |
| **Privacy Bound** | R < 1 (reconstruction ceiling) | "They cannot see your whole" | Surveillance resistance | Irreducible promise |
| **Learning** | Compression protocol | Reading Acts, deriving proverbs | Posting signals (0.01 ZEC) | Assessment events |
| **Trust** | Bilateral knowledge | Shared stories | VRCs (relationship credentials) | Trust function τ(0-1) |
| **Infrastructure** | System observers | Guardians of the realm | SWORD token holders | Promise-keepers |
| **Coordination** | Mutual information | Spells | VRC efficiency | Coordination promises |
| **Budget** | C_S + C_M < H(X) | Capacity limits | Token allocation | Valency constraint |

---

## Promise Theory Foundations

### The Autonomy Axiom (Visual)

```
┌─────────────────────────────────────────────────────────────┐
│             THE AUTONOMY AXIOM VISUALIZED                    │
│     "Agents can only promise their own behavior"             │
└─────────────────────────────────────────────────────────────┘

WHAT AGENTS CAN PROMISE:

    ⚔️ Swordsman                   🧙 Mage
    ┌─────────────────┐           ┌─────────────────┐
    │ ✓ "I will not   │           │ ✓ "I will act   │
    │   reveal X"     │           │   on authorized │
    │                 │           │   info only"    │
    │ ✓ "I will       │           │                 │
    │   maintain      │           │ ✓ "I will       │
    │   boundaries"   │           │   coordinate    │
    │                 │           │   efficiently"  │
    └─────────────────┘           └─────────────────┘
           │                              │
           │         OWN BEHAVIOR         │
           └──────────────┬───────────────┘
                          │
                          ✓ VALID PROMISES

WHAT AGENTS CANNOT PROMISE:

    ❌ Single Agent Attempting Both:
    ┌─────────────────────────────────────┐
    │ "I will protect privacy AND         │
    │  enable full delegation"            │
    │                                     │
    │  This requires promising outcomes   │
    │  that depend on external actors:    │
    │  • Users must trust                 │
    │  • Services must cooperate          │
    │  • Networks must function           │
    │                                     │
    │  IMPOSSIBLE: Cannot promise         │
    │  another's behavior                 │
    └─────────────────────────────────────┘
                    │
                    ❌ FORMAL VIOLATION

WHY DUAL AGENTS ARE NECESSARY:

┌─────────────────────────────────────────────────────────────┐
│  Single Agent: Promises outcome requiring cooperation       │
│  ┌─────────┐                                                │
│  │  Agent  │──→ "I'll protect AND delegate" ──→ ❌ INVALID │
│  └─────────┘    (outcome, not behavior)                     │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  Dual Agents: Each promises only own behavior               │
│  ┌─────────┐                                                │
│  │Swordsman│──→ "I'll protect" ──────────────→ ✓ VALID    │
│  └─────────┘    (own behavior)                              │
│  ┌─────────┐                                                │
│  │  Mage   │──→ "I'll delegate" ─────────────→ ✓ VALID    │
│  └─────────┘    (own behavior)                              │
│                                                              │
│  TOGETHER: Privacy + Delegation achieved                    │
│            through architectural separation                  │
└─────────────────────────────────────────────────────────────┘
```

### Promise Types in 0xagentprivacy

```
┌─────────────────────────────────────────────────────────────┐
│              PROMISE TYPE CLASSIFICATION                     │
└─────────────────────────────────────────────────────────────┘

TYPE 1: Give Promises (+)
┌────────────────────────────────────────┐
│ "I will provide X to you"              │
│                                        │
│ Examples:                              │
│ • Swordsman (+) protection → FP        │
│ • Mage (+) delegation → FP             │
│ • Guardian (+) validation → network    │
│ • First Person (+) authorization → S,M │
└────────────────────────────────────────┘

TYPE 2: Accept Promises (-)
┌────────────────────────────────────────┐
│ "I will accept/use what you provide"   │
│                                        │
│ Examples:                              │
│ • Swordsman (-) accepts authorization  │
│ • Mage (-) accepts authorized info     │
│ • Network (-) accepts chronicles       │
│ • VRC partner (-) accepts verification │
└────────────────────────────────────────┘

TYPE 3: Coordination Promises C(b)
┌────────────────────────────────────────┐
│ "I will voluntarily subordinate my     │
│  behavior to external authority b"     │
│                                        │
│ Examples:                              │
│ • Spell = C(protocol_rules)            │
│ • VRC = C(bilateral_agreement)         │
│ • Guardian = C(compression_standards)  │
│                                        │
│ NOTE: Subordination is VOLUNTARY       │
│       Agent can always revoke          │
└────────────────────────────────────────┘

TYPE 4: The Irreducible Promise
┌────────────────────────────────────────┐
│ "A property that exists only in the    │
│  relationship between agents"          │
│                                        │
│ The Gap (⊥) is irreducible:           │
│ • Cannot be attributed to Swordsman    │
│ • Cannot be attributed to Mage         │
│ • Exists in their maintained separation│
│ • Requires all three (FP+S+M) to exist │
│                                        │
│ R_max < 1 IS the irreducible promise   │
└────────────────────────────────────────┘
```

---

## Dual Agent Architecture

### Core Structure: Swordsman ⊥ Mage (Promise-Theoretic View)

```
                        ┌────────────────┐
                        │  FIRST PERSON  │
                        │   (You - 😊)    │
                        │   (Authorizer)  │
                        └────────┬───────┘
                                 │
                    Private State X (complete context)
                                 │
                    ┌────────────┼────────────┐
                    │                         │
                    ▼                         ▼
            ┌───────────────┐         ┌───────────────┐
            │  SWORDSMAN ⚔️  │         │    MAGE 🧙    │
            │   (Protect)   │         │  (Delegate)   │
            │               │         │               │
            │ PROMISES:     │         │ PROMISES:     │
            │ • Protection  │         │ • Delegation  │
            │ • Boundary    │         │ • Coordination│
            │ • Non-reveal  │         │ • Efficiency  │
            └───────────────┘         └───────────────┘
                    │                         │
        Observes X completely      Acts using authorized info
        Reveals nothing directly   Public delegation/coordination
                    │                         │
                    │         ⊥               │
                    │    (SEPARATION          │
                    │     PROMISE)            │
                    └────────────┬────────────┘
                                 │
                    THE GAP (Irreducible Promise)
                                 │
                            s ⊥ m | X
                                 │
                    Additive information bounds:
                    I(X; s,m) ≤ I(X;s) + I(X;m)
                                 │
                    Reconstruction ceiling: R < 1
                                 │
                    ▼
        ┌─────────────────────────────────────┐
        │  PRIVACY PRESERVED THROUGH          │
        │  KEPT SEPARATION PROMISE            │
        │                                     │
        │  Each agent keeps its own promises. │
        │  The gap emerges from maintained    │
        │  separation, not external force.    │
        └─────────────────────────────────────┘
```

### Interior Promises (Superagent View)

```
┌─────────────────────────────────────────────────────────────┐
│         INTERIOR PROMISES WITHIN SUPERAGENT                  │
│         (First Person + Swordsman + Mage)                   │
└─────────────────────────────────────────────────────────────┘

                         😊 First Person
                        /│\
           authorize   / │ \   authorize
          ┌──────────/  │  \──────────┐
          │            │              │
          ▼            │              ▼
     ⚔️ Swordsman      │         🧙 Mage
          │            │              │
          │            │              │
  protect │            │              │ delegate
          │            │              │
          ▼            │              ▼
         😊 ◄──────────┘──────────► 😊


PROMISE FLOW DIAGRAM:

    ⚔️ ─── protect ───► 😊     (S promises protection to FP)
    🧙 ─── delegate ──► 😊     (M promises delegation to FP)
    😊 ─── authorize ─► ⚔️🧙   (FP authorizes both agents)
    ⚔️ ─── ⊥ ────────► 🧙     (S promises separation from M)

CRITICAL: The separation promise (⊥) is interior to the superagent.
          It cannot be observed from outside.
          It must be maintained by architectural constraint.

EXTERIOR PROMISES (to world):

    ┌─────────────────────────────────────┐
    │          SUPERAGENT (FP+S+M)        │
    │                                     │
    │  ──── coordinate ──────► 🌍         │
    │       (via Mage)                    │
    │                                     │
    │  ──── boundary ────────► 🌍         │
    │       (via Swordsman)               │
    └─────────────────────────────────────┘
```

### Key Properties (Promise-Theoretic Framing)

```
PROPERTY 1: Conditional Independence (Separation Promise)
┌────────────────────────────────────────┐
│ s ⊥ m | X                              │
│                                        │
│ Promise Theory: Non-overlapping scopes │
│ Swordsman observes protection scope    │
│ Mage observes delegation scope         │
│ Neither promises the other's behavior  │
│                                        │
│ The separation is a KEPT PROMISE       │
└────────────────────────────────────────┘

PROPERTY 2: Additive Bounds (Scope Limits)
┌────────────────────────────────────────┐
│ I(X; s,m) ≤ I(X;s) + I(X;m)           │
│                                        │
│ Promise Theory: Valency constraints    │
│ Each agent has limited promise capacity│
│ Joint capacity is SUM not PRODUCT      │
│ Architectural enforcement of limits    │
└────────────────────────────────────────┘

PROPERTY 3: Reconstruction Ceiling (Irreducible Promise)
┌────────────────────────────────────────┐
│ R(X|s,m) < 1                          │
│                                        │
│ Promise Theory: Irreducible property   │
│ Exists only in relationship between    │
│ Swordsman, Mage, and First Person     │
│ Cannot be captured by compromising one │
│                                        │
│ The Gap IS the irreducible promise     │
└────────────────────────────────────────┘
```

---

## Superagent Structure

### The Composite Agent Model

```
┌─────────────────────────────────────────────────────────────┐
│               SUPERAGENT ARCHITECTURE                        │
│     First Person + Swordsman + Mage = Composite Agent       │
└─────────────────────────────────────────────────────────────┘

EXTERIOR VIEW (What the world sees):

    ┌─────────────────────────────────────────┐
    │                                         │
    │            SUPERAGENT                   │
    │                                         │
    │   Appears as single coherent agent      │
    │   Coordinates externally                │
    │   Maintains boundaries                  │
    │                                         │
    └─────────────────────────────────────────┘
                      │
                      ▼
              Exterior Promises:
              • Coordinate with others
              • Maintain privacy boundaries
              • Keep commitments to VRC partners


INTERIOR VIEW (What's actually happening):

    ┌─────────────────────────────────────────┐
    │             SUPERAGENT                   │
    │                                         │
    │    ┌────────────────────────────────┐   │
    │    │      😊 First Person           │   │
    │    │      (Authorization)           │   │
    │    └────────────┬───────────────────┘   │
    │                 │                       │
    │    ┌────────────┼────────────┐          │
    │    │            │            │          │
    │    ▼            ▼            ▼          │
    │  ┌─────┐      ┌───┐      ┌─────┐        │
    │  │ ⚔️  │──⊥───│   │──────│ 🧙  │        │
    │  │ S   │      │   │      │ M   │        │
    │  └─────┘      └───┘      └─────┘        │
    │    │         THE GAP        │           │
    │    │      (Irreducible)     │           │
    │    └────────────┬───────────┘           │
    │                 │                       │
    │         Interior Promises:              │
    │         • S protects FP                 │
    │         • M delegates for FP            │
    │         • S ⊥ M (separation kept)       │
    │         • FP authorizes both            │
    │                                         │
    └─────────────────────────────────────────┘


WHY SUPERAGENT MATTERS:

1. ADVERSARY SEES EXTERIOR ONLY
   ┌─────────────────────────────────────┐
   │ Adversary observes superagent       │
   │ Cannot see interior promises        │
   │ Cannot distinguish S from M         │
   │ Cannot observe Gap directly         │
   └─────────────────────────────────────┘

2. COMPROMISE REQUIRES ALL THREE
   ┌─────────────────────────────────────┐
   │ Compromise S alone → Learn C_S bits │
   │ Compromise M alone → Learn C_M bits │
   │ Compromise FP alone → No agent keys │
   │                                     │
   │ Full reconstruction requires ALL:   │
   │ FP + S + M cooperating              │
   │                                     │
   │ The Gap exists in their cooperation │
   │ No single compromise captures it    │
   └─────────────────────────────────────┘

3. IRREDUCIBLE PROMISE LOCATION
   ┌─────────────────────────────────────┐
   │ R_max < 1 is not in S               │
   │ R_max < 1 is not in M               │
   │ R_max < 1 is not in FP              │
   │                                     │
   │ R_max < 1 is IN THE RELATIONSHIP    │
   │ It exists BETWEEN the components    │
   │ It requires maintained separation   │
   │                                     │
   │ This is the "shimmer of dignity"    │
   └─────────────────────────────────────┘
```

---

## First Person Stack

### Sovereign Agent and Wallet Architecture

```
                    ┌─────────────────────────────────────┐
                    │     SOVEREIGN AGENT                 │
                    └─────────────────────────────────────┘
                                 │
                    ┌────────────┴────────────┐
                    │                         │
                    ▼                         ▼
        ┌──────────────────────┐  ┌──────────────────────┐
        │ UI & Human Experience │  │    Trust Tasks       │
        │                       │  │                      │
        │ • QR codes            │  │ • Credential exchange│
        │ • Ceremonies          │  │ • TRQP              │
        │ • Trust marks         │  │ • Secure messaging   │
        │                       │  │ • Payments/value    │
        │                       │  │ • Federated social  │
        │                       │  │ • AI agents         │
        └──────────────────────┘  └──────────────────────┘
                    │                         │
                    └────────────┬────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │                         │
                    │ Trust Spanning Protocol │
                    │        (TSP)            │
                    │                         │
                    │  Bridges agent and      │
                    │  wallet layers          │
                    │  (Coordination promises)│
                    │                         │
                    └────────────┬────────────┘
                                 │
                    ┌────────────┴────────────┐
                    │                         │
                    ▼                         ▼
        ┌──────────────────────┐  ┌──────────────────────┐
        │ Verifiable Credentials │  │   Digital Assets      │
        │                       │  │                      │
        │ • Identity proofs     │  │ • Tokens             │
        │ • Attestations        │  │ • NFTs               │
        │ • Claims              │  │ • Value storage      │
        │ (Promise bundles)     │  │ (Commitment stakes)  │
        └──────────────────────┘  └──────────────────────┘
                    │                         │
                    └────────────┬────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │                         │
                    │ Self-Certifying         │
                    │ Identifiers (SCIDs)     │
                    │                         │
                    │ • Decentralized identity │
                    │ • Self-sovereign        │
                    │ • Portable              │
                    │ (Autonomy foundation)   │
                    │                         │
                    └────────────┬────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │                         │
                    │  Cryptographic Keys    │
                    │                         │
                    │ • Private keys         │
                    │ • Public keys          │
                    │ • Key derivation       │
                    │ • Signing/verification │
                    │                         │
                    │  (Foundation Layer)    │
                    │  (Promise-keeping      │
                    │   enforcement)         │
                    │                         │
                    └─────────────────────────┘
```

### Layer Descriptions (Promise-Theoretic)

**Sovereign Agent (Top Layers):**
- **UI & Human Experience**: User-facing interfaces for making and accepting promises
- **Trust Tasks**: Core functionality for promise exchange, coordination, and verification

**Trust Spanning Protocol (TSP):**
- Connects agent layer (promise-making) with wallet layer (commitment storage)
- Implements coordination promises C(b) across the stack

**Sovereign Wallet (Bottom Layers):**
- **Verifiable Credentials & Digital Assets**: Storage for promise bundles and commitment stakes
- **Self-Certifying Identifiers (SCIDs)**: Foundation for autonomy axiom compliance
- **Cryptographic Keys**: Enforcement layer for promise-keeping (ZK proofs transform "trust me" to "verify me")

---

## Learning Pathway Flow

### Spellbook → Signals → Guardianship (Assessment Journey)

```
START: First Person wants to participate in 0xagentprivacy
  │
  ▼
┌────────────────────────────────────────────┐
│ STEP 1: Read Spellbook                     │
│                                            │
│ Options:                                   │
│ • 11 Acts + bookends (13 sections)        │
│ • 30 tales (Zero Spellbook)               │
│ • Boundary spells (practical)             │
│ • Integration guides                       │
│                                            │
│ PT: Understanding before promising         │
└────────────────┬───────────────────────────┘
                 │
                 ▼
┌────────────────────────────────────────────┐
│ STEP 2: Form a Proverb (RPP)             │
│                                            │
│ Read content → compress into proverb      │
│ • Maps content to YOUR context            │
│ • Proves comprehension                    │
│ • Creates unique expression               │
│                                            │
│ Example:                                   │
│ "My privacy blade guards what my          │
│  delegation spell cannot reveal"          │
│                                            │
│ PT: Assessment of knowledge transfer      │
└────────────────┬───────────────────────────┘
                 │
                 ▼
┌────────────────────────────────────────────┐
│ STEP 3: Post Signal (Assessment Payment)  │
│                                            │
│ • 1 proverb = 1 signal                    │
│ • Cost: 0.01 ZEC (~$5 at $500/ZEC)       │
│ • On-chain proof of comprehension         │
│ • Generates MAGE tokens                   │
│                                            │
│ PT: Signal = Assessment α(π)              │
│     Skin-in-game proves genuine assessment│
└────────────────┬───────────────────────────┘
                 │
                 ▼
┌────────────────────────────────────────────┐
│ STEP 4: Build Trust (Trust Function τ)    │
│                                            │
│ Trust Tier  Signals  Trust τ  Capability  │
│ ─────────────────────────────────────────  │
│ Blade       0-49     0.0-0.2  Learning     │
│ Light       50-149   0.2-0.5  Basic coord  │
│ Heavy       150-499  0.5-0.8  Intel Pools  │
│ Dragon      500+     0.8-1.0  Guardian     │
│                                            │
│ PT: Each signal = assessment event        │
│     Trust τ = accumulated evidence        │
└────────────────┬───────────────────────────┘
                 │
                 ▼
┌────────────────────────────────────────────┐
│ STEP 5: Guardian Qualification            │
│                                            │
│ IF: Dragon tier (500+ signals, τ ≥ 0.8)  │
│ THEN: Can become Guardian                 │
│                                            │
│ Guardian proves:                           │
│ • Reconstruction ability                   │
│ • Protocol comprehension                   │
│ • Sustained commitment                     │
│                                            │
│ Earned through learning, not purchased    │
│                                            │
│ PT: Guardian = Professional promise-keeper │
│     Stake = Commitment to coordination    │
│     Slashing = Penalty for violation      │
└────────────────┬───────────────────────────┘
                 │
                 ▼
              SUCCESS
    First Person now participates as
    infrastructure provider (promise-keeper)
    with proven comprehension and 
    demonstrated commitment history
```

### Cost Breakdown Example

```
Learning Path           Signals    Cost (ZEC)   Cost (USD)*  Trust τ
──────────────────────────────────────────────────────────────────────
13 sections (main)      13         0.13 ZEC     $65          ~0.05
30 tales (Zero)         30         0.30 ZEC     $150         ~0.12
Light tier minimum      50         0.50 ZEC     $250         0.20
Dragon tier minimum     500        5.00 ZEC     $2,500       0.80

* At canonical $500/ZEC price point

KEY INSIGHT: 
Guardian qualification costs ~$2,500 in sustained learning (assessments)
This filters for genuine comprehension and commitment history
Higher barrier than "cheap" signals, but earned through demonstrated
promise-keeping, not purchased with capital alone
```

---

## Signal vs Ceremony Distinction

### Critical Terminology Difference

```
┌─────────────────────────────────────────────────────────────┐
│                    GENESIS CEREMONY                          │
│                  (Genesis Promise)                           │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │  Cost: 1 ZEC    │
                    │  Frequency: Once│
                    │  Requires:      │
                    │  Personhood     │
                    │  Credential     │
                    └─────────────────┘
                              │
                              ▼
              Creates: Dual agent pair (Swordsman & Mage)
              Generates: Initial SWORD + MAGE tokens
              Purpose: Genesis promise to maintain separation
                              │
                              ▼
                    ┌─────────────────┐
                    │  You now have:  │
                    │  • Swordsman ⚔️  │
                    │  • Mage 🧙       │
                    │  (Superagent)   │
                    └─────────────────┘

              PT: Ceremony = commitment to architectural separation
                  First Person promises to authorize both agents
                  Agents promise to maintain independence

─────────────────────────────────────────────────────────────

┌─────────────────────────────────────────────────────────────┐
│                         SIGNALS                              │
│                  (Assessment Payments)                       │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │  Cost: 0.01 ZEC │
                    │  Frequency: Many│
                    └─────────────────┘
                              │
                              ▼
              Activity: Post proverbs proving comprehension
              Generates: MAGE tokens (continuous)
              Purpose: Assessment events building trust τ
                              │
                              ▼
                    ┌─────────────────┐
                    │  Each signal:   │
                    │  • Proves learn │
                    │  • Earns MAGE   │
                    │  • Builds τ     │
                    │  (Assessment)   │
                    └─────────────────┘

              PT: Signal = Assessment α(π) with skin-in-game
                  Each signal = evidence of promise-keeping capability
```

### Comparison Table

| Aspect | Genesis Ceremony | Signal |
|--------|-----------------|--------|
| **Frequency** | Once per First Person | Continuous (many) |
| **Cost** | 1 ZEC (requires personhood credential) | 0.01 ZEC each |
| **Purpose** | Create agent pair | Prove comprehension |
| **Output** | SWORD + MAGE tokens | MAGE tokens only |
| **What it proves** | Intent to participate | Understanding of protocol |
| **Analogy** | Birth certificate | Report cards |
| **Required for** | Having agents | Guardian qualification |
| **PT Role** | Genesis promise (commitment to separation) | Assessment event α(π) |

---

## Compression Ratios Context

### Types of Compression (Context-Dependent)

```
┌─────────────────────────────────────────────────────────────┐
│              COMPRESSION RATIO DISAMBIGUATION                 │
│         (Different ratios measure different things)           │
└─────────────────────────────────────────────────────────────┘

TYPE 1: Agent Coordination Efficiency (Communication)
┌────────────────────────────────────────┐
│ Ratio: 70:1                            │
│ Measurement: Communication reduction   │
│ Calculation: 70 messages → 1 via VRC  │
│ Context: Promise bundle reuse         │
│                                        │
│ PT Insight:                            │
│ VRC is a promise bundle—once formed,  │
│ the bundle doesn't need re-verification│
│ for each coordination                  │
└────────────────────────────────────────┘

TYPE 2: Content → Proverb (Semantic)
┌────────────────────────────────────────┐
│ Ratio: 200:1                           │
│ Measurement: Text compression          │
│ Calculation: 5,000 words → 25 words   │
│ Context: RPP compression of knowledge │
│                                        │
│ PT Insight:                            │
│ Compression ratio is quantified       │
│ assessment α(π)—high compression      │
│ indicates genuine comprehension       │
└────────────────────────────────────────┘

TYPE 3: Proverb → Cipher (Symbolic)
┌────────────────────────────────────────┐
│ Ratio: 5:1                             │
│ Measurement: Symbol compression        │
│ Calculation: 25 words → 5 symbols     │
│ Context: Coordination promise notation│
│                                        │
│ PT Insight:                            │
│ Spells are coordination promises C(b) │
│ in compressed symbolic form           │
└────────────────────────────────────────┘

TYPE 4: Total Semantic (End-to-End)
┌────────────────────────────────────────┐
│ Ratio: 1,000:1                         │
│ Measurement: Full semantic compression │
│ Calculation: 5,000 words → 5 symbols  │
│ Context: Content → cipher (complete)  │
│                                        │
│ PT Insight:                            │
│ Total compression enables efficient   │
│ promise coordination—agents who share │
│ framework can coordinate with minimal │
│ overhead                               │
└────────────────────────────────────────┘
```

### Visual Compression Cascade

```
    COMPLEX CONTENT (5,000 words)
           │
           │  [RPP Protocol]
           │  200:1 compression
           │  Assessment: α(learning)
           ▼
       PROVERB (25 words)
           │
           │  [Cipher Protocol]
           │  5:1 compression
           │  Coordination promise form
           ▼
       CIPHER (5 symbols)
           │
           │  TOTAL: 1,000:1
           ▼
    ⚔️🧙🗝️✨🤝 (Complete framework)

For those who learned the protocol,
these 5 symbols contain the entire
5,000-word framework with perfect
semantic reconstruction.

PT: Matching compression = mutual assessment
    Both parties keep knowledge transfer promise
    VRC forms from demonstrated comprehension

For those who didn't learn it,
these are just random emojis.

This is the power of bilateral promise bundles.
```

---

## Guardian Model Alternatives

### Ecosystem-Dependent Approaches (Promise-Keeper Models)

```
┌─────────────────────────────────────────────────────────────┐
│   GUARDIAN MODEL FLEXIBILITY (Promise-Keeper Selection)      │
└─────────────────────────────────────────────────────────────┘

MODEL 1: Merit + Time (SWORD-based) [0xagentprivacy Reference]
┌────────────────────────────────────────────────────────────┐
│ Guardian Type: Token holders with proven comprehension     │
│ Selection: Dragon tier (500+ signals, τ ≥ 0.8) required   │
│ Incentive: Quality-based reallocation from failures       │
│ Context: Consumer privacy, learning-first communities     │
│ Status: 🚧 WIP - reference implementation                 │
│                                                            │
│ PT: Promise-keeping verified through accumulated          │
│     assessment history (signals) and stake (SWORD)        │
│     Slashing = penalty for promise violation              │
│                                                            │
│ Trust Tier Progression:                                    │
│ Blade (τ<0.2) → Light (τ<0.5) → Heavy (τ<0.8)            │
│ → Dragon (τ≥0.8) → Guardian eligibility                   │
└────────────────────────────────────────────────────────────┘

MODEL 2: SLA Contracts (Contract-based) [Enterprise]
┌────────────────────────────────────────────────────────────┐
│ Guardian Type: Service providers with legal contracts     │
│ Selection: RFP process, due diligence                     │
│ Incentive: Fixed fees, reputation, contract renewal       │
│ Context: Enterprise deployments, regulated industries     │
│ Status: ✅ Active - proven model                          │
│                                                            │
│ PT: Legal contract is externalized promise                │
│     Court system provides promise enforcement             │
│     No slashing, no tokens needed                         │
└────────────────────────────────────────────────────────────┘

MODEL 3: Peer Reputation (Social-based) [Academic]
┌────────────────────────────────────────────────────────────┐
│ Guardian Type: Trusted peers, colleagues, institutions    │
│ Selection: Academic merit, peer recommendation            │
│ Incentive: Reputation, citation, academic credit          │
│ Context: Research consortia, academic networks            │
│ Status: ✅ Active - used in research settings             │
│                                                            │
│ PT: Reputation is accumulated trust τ over time           │
│     Social enforcement of promise-keeping                 │
│     No tokens, no slashing—pure trust function            │
└────────────────────────────────────────────────────────────┘

MODEL 4: Economic Staking (Capital-based) [DeFi]
┌────────────────────────────────────────────────────────────┐
│ Guardian Type: Capital holders staking collateral         │
│ Selection: Stake amount, validator set                    │
│ Incentive: Block rewards, slashing for misbehavior        │
│ Context: DeFi protocols, blockchain validators            │
│ Status: ✅ Active - traditional crypto model              │
│                                                            │
│ PT: Capital stake = commitment to promise                 │
│     Slashing = economic penalty for violation             │
│     Incentive compatibility through economics             │
└────────────────────────────────────────────────────────────┘

MODEL 5: Trust Consensus (Community-based) [Activist]
┌────────────────────────────────────────────────────────────┐
│ Guardian Type: Trusted community members                  │
│ Selection: Community vote, consensus mechanism            │
│ Incentive: Community standing, mission alignment          │
│ Context: Activist networks, DAOs, cooperatives            │
│ Status: ✅ Active - used in community projects            │
│                                                            │
│ PT: Community assessment of promise-keeping history       │
│     Social coordination promise C(community)              │
│     No tokens, no capital—trust from demonstrated action  │
└────────────────────────────────────────────────────────────┘
```

### Selection Matrix

| Use Case | Recommended Model | Why (PT Rationale) |
|----------|------------------|-----|
| **Consumer privacy app** | Merit + Time (SWORD) | Learning proves assessment capability |
| **Enterprise deployment** | SLA Contracts | Legal promises, clear enforcement |
| **Research network** | Peer Reputation | Trust function through academic merit |
| **DeFi protocol** | Economic Staking | Capital commitment, incentive compatibility |
| **Activist network** | Trust Consensus | Mission alignment as coordination promise |

### Key Insight

```
┌─────────────────────────────────────────────────────────────┐
│ THE PROTOCOL REQUIRES: Guardians (promise-keepers)          │
│ THE PROTOCOL DOES NOT REQUIRE: Specific selection mechanism │
│                                                             │
│ What matters: Guardians keep their promises to network      │
│ How chosen: Depends on ecosystem context                    │
│                                                             │
│ PT Insight: All models implement promise-keeping incentives │
│             through different mechanisms (stake, contract,  │
│             reputation, capital, community)                 │
└─────────────────────────────────────────────────────────────┘
```

---

## Blockchain Flexibility

### Meta-Protocol vs Implementation

```
┌─────────────────────────────────────────────────────────────┐
│              META-PROTOCOL REQUIREMENTS                      │
│         (What 0xagentprivacy actually needs)                │
└─────────────────────────────────────────────────────────────┘
                              │
                    ┌─────────┴─────────┐
                    │                   │
                    ▼                   ▼
        ┌───────────────────┐   ┌───────────────────┐
        │  PUBLIC LEDGER    │   │  PRIVATE LEDGER   │
        │                   │   │                   │
        │  • Signals        │   │  • First Person   │
        │  • VRCs           │   │    state X        │
        │  • Guardians      │   │  • Agent actions  │
        │  • Ceremonies     │   │  • Private data   │
        │                   │   │                   │
        │ (Visible promises)│   │ (Interior state)  │
        └───────────────────┘   └───────────────────┘
                    │                   │
                    └─────────┬─────────┘
                              │
                    That's it. That's all.
                              │
                              ▼
        ┌─────────────────────────────────────────┐
        │ HOW you provide these is flexible!      │
        │                                         │
        │ PT: Dual ledger enables separation      │
        │     promise to be architecturally       │
        │     enforced, not just claimed          │
        └─────────────────────────────────────────┘
```

### Implementation Options

```
OPTION 1: Zcash (Native, Simplest) [Reference Implementation]
┌──────────────────────────────────────────────────────┐
│ Public Ledger:  Transparent ZEC transactions         │
│ Private Ledger: Shielded ZEC (native privacy)        │
│                                                       │
│ PT Advantages:                                        │
│ • Native separation promise enforcement             │
│ • Dual ledger is architectural, not composed        │
│ • Simple promise verification                       │
│                                                       │
│ Status: 🚧 WIP - we're building on this first       │
└──────────────────────────────────────────────────────┘

OPTION 2: Ethereum + Privacy Layer (Composed, Most Flexible)
┌──────────────────────────────────────────────────────┐
│ Public Ledger:  Ethereum L1 or L2                    │
│ Private Ledger: Kohaku / Aztec / Starknet / Mina    │
│                                                       │
│ PT Advantages:                                        │
│ • Largest ecosystem for coordination promises       │
│ • Multiple privacy layer options for separation     │
│ • More tooling for promise verification             │
│                                                       │
│ Status: 📋 Planned - next after Zcash proves concept│
└──────────────────────────────────────────────────────┘

OPTION 3: Other Chains (Future)
┌──────────────────────────────────────────────────────┐
│ • Mina Protocol (smallest blockchain)                │
│ • Aleo (privacy-first L1)                            │
│ • Secret Network (private smart contracts)           │
│ • Namada (shielded asset hub)                        │
│                                                       │
│ Status: 🔬 Exploratory - if dual ledger possible    │
└──────────────────────────────────────────────────────┘
```

### Key Insight

```
┌─────────────────────────────────────────────────────┐
│ 0xagentprivacy is a META-PROTOCOL                   │
│                                                     │
│ It specifies WHAT you need (dual ledger)           │
│ NOT HOW you provide it (blockchain choice)         │
│                                                     │
│ Zcash first = simplest proof of concept            │
│ Ethereum next = largest ecosystem access           │
│ Others possible = wherever dual ledger achievable  │
│                                                     │
│ PT: The separation promise can be kept on any      │
│     substrate that provides dual ledger capability │
└─────────────────────────────────────────────────────┘
```

---

## VRC Formation Process

### Creating Bilateral Promise Bundles

```
STEP 1: Two First Persons Learn Framework
┌───────────────────┐         ┌───────────────────┐
│  Alice 😊         │         │  Bob 😊           │
│                   │         │                   │
│  Reads spellbook  │         │  Reads spellbook  │
│  Posts signals    │         │  Posts signals    │
│  Has MAGE tokens  │         │  Has MAGE tokens  │
│  (Assessments)    │         │  (Assessments)    │
└───────────────────┘         └───────────────────┘
         │                              │
         │                              │
         ▼                              ▼
    Both understand                Both understand
    dual agent model               dual agent model
    (Can keep knowledge            (Can keep knowledge
     transfer promise)              transfer promise)

─────────────────────────────────────────────────────

STEP 2: Form Bilateral Proverb (Mutual Assessment)
┌─────────────────────────────────────────────────┐
│ Alice and Bob co-create proverb that maps       │
│ to THEIR shared context:                        │
│                                                  │
│ "Our guardians watch what our agents cannot     │
│  reveal between us"                             │
│                                                  │
│ This proverb is:                                 │
│ • Unique to their relationship                  │
│ • Meaningless to outsiders                      │
│ • Verifiable by each other                      │
│ • Recoverable if one forgets                    │
│                                                  │
│ PT: Bilateral assessment α(relationship)        │
│     Matching compression = mutual assessment    │
└─────────────────────────────────────────────────┘
         │
         ▼

STEP 3: Inscribe VRC On-Chain (Promise Bundle Creation)
┌───────────────────┐         ┌───────────────────┐
│  Alice ⚔️🧙        │         │  Bob ⚔️🧙          │
└───────────────────┘         └───────────────────┘
         │                              │
         │      Create VRC              │
         └──────────┬──────────────────┘
                    │
                    ▼
         ┌──────────────────────┐
         │   VRC (On-chain)     │
         │   (Promise Bundle)   │
         │                      │
         │ • Alice's commitment │
         │ • Bob's commitment   │
         │ • Bilateral proverb  │
         │ • Cost: 0.01 ZEC ea  │
         │                      │
         │ PT: Bundle of mutual │
         │     promises that    │
         │     can be verified  │
         │     but not forged   │
         └──────────────────────┘
                    │
                    ▼

STEP 4: VRC Becomes Recovery Mechanism
┌─────────────────────────────────────────────────┐
│ IF: Alice loses her keys                         │
│ THEN: Bob can help verify Alice's identity       │
│       using their bilateral proverb              │
│                                                  │
│ How it works:                                    │
│ 1. Alice claims: "I'm Alice, I lost my keys"    │
│ 2. Bob asks: "What's our proverb?"              │
│ 3. Alice forms correct proverb from context     │
│ 4. Bob verifies: "Yes, that's Alice"            │
│ 5. Recovery proceeds (with multiple VRCs)       │
│                                                  │
│ PT: Recovery through demonstrated promise-       │
│     keeping (expanding the cipher correctly)     │
│                                                  │
│ No biometrics. No personal questions.           │
│ Just bilateral promise verification.            │
└─────────────────────────────────────────────────┘
```

### VRC Properties (Promise Bundle Characteristics)

```
┌─────────────────────────────────────────────────────┐
│                 VRC PROPERTIES                       │
│              (Promise Bundle Features)               │
└─────────────────────────────────────────────────────┘

1. BILATERAL (Mutual Promises)
   ├─ Two First Persons create together
   ├─ Neither can forge alone
   └─ Both must sign

2. CONTEXT-SPECIFIC (Scoped Promises)
   ├─ Proverb maps to shared context
   ├─ Meaningless outside relationship
   └─ Cannot be reused for different relationship

3. RECOVERABLE (Promise Reconstruction)
   ├─ If forgotten, can be rederived
   ├─ Because based on relationship context
   └─ Not arbitrary password

4. VERIFIABLE (Assessment Evidence)
   ├─ On-chain commitment
   ├─ Both parties can prove participation
   └─ Can be used in recovery

5. SYBIL-RESISTANT (Commitment Cost)
   ├─ Costs 0.01 ZEC per person (0.02 total)
   ├─ Requires actual relationship
   └─ Can't be cheaply automated

6. NON-BIOMETRIC (Pure Promise)
   ├─ No fingerprints, no face scans
   ├─ No personal questions ("mother's maiden name")
   └─ Pure bilateral promise verification

PT INSIGHT: VRC is a promise bundle that enables 70:1
coordination efficiency because once mutual assessment
is verified, the bundle can be reused without re-
verification for each coordination.
```

---

## Information Flow Topology

### The Four Emergent Properties

```
                    ┌────────────────┐
                    │  FIRST PERSON  │
                    │   (Sovereignty)│
                    │   (Authorizer) │
                    └────────┬───────┘
                             │
                    Private State X
                             │
                ┌────────────┼────────────┐
                │                         │
                ▼                         ▼
        ┌──────────────┐          ┌──────────────┐
        │ SWORDSMAN ⚔️  │          │   MAGE 🧙     │
        │  (Privacy)   │          │ (Delegation) │
        │  (Protector) │          │ (Coordinator)│
        └──────────────┘          └──────────────┘
                │                         │
                └────────────┬────────────┘
                             │
                    ┌─────────▼─────────┐
                    │                   │
                    │ THE GAP (s ⊥ m|X) │
                    │ (Irreducible      │
                    │  Promise)         │
                    │                   │
                    └───────────────────┘
                             │
            ┌────────────────┼────────────────┐
            │                                 │
            ▼                                 ▼
    ┌───────────────┐                ┌───────────────┐
    │   REFLECT     │                │    CONNECT    │
    │   (Memory)    │                │   (Network)   │
    │   (Temporal)  │                │   (Social)    │
    └───────────────┘                └───────────────┘

TETRAHEDRAL SOVEREIGNTY:
    
         First Person (Apex)
              /│\
             / │ \
            /  │  \
           /   │   \
    Swordsman  │    Mage
          \    │    /
           \   │   /
            \  │  /
             \ │ /
         The Gap (Base)
         (Irreducible Promise)

Four components emerge naturally from
conditional independence:

1. SWORDSMAN (Protection Primitive)
   • Observes complete state
   • Reveals nothing directly
   • Maintains privacy boundaries
   • PT: Promises protection to First Person

2. MAGE (Delegation Primitive)
   • Acts using authorized subset
   • Public coordination
   • Enables network effects
   • PT: Promises delegation for First Person

3. REFLECT (Temporal Property)
   • Emerges from gap + time
   • Allows reviewing past without
     compromising present privacy
   • Chronicles as recovery
   • PT: Memory of kept promises

4. CONNECT (Network Property)
   • Emerges from gap + others
   • Mages coordinate efficiently
   • Swordsmen maintain independence
   • VRCs form trust network
   • PT: Network of promise bundles
```

### Why Four, Not Two?

```
NAIVE: Just two agents is enough
┌──────────────┐    ┌──────────────┐
│  Swordsman   │    │     Mage     │
└──────────────┘    └──────────────┘
       │                    │
       └──────────┬─────────┘
                  │
            Privacy + Delegation
                DONE

REALITY: The gap between them creates two more
┌──────────────┐    ┌──────────────┐
│  Swordsman   │    │     Mage     │
└──────────────┘    └──────────────┘
       │                    │
       │    THE GAP         │
       │  (Irreducible      │
       │   Promise)         │
       │       │            │
       └───────┼────────────┘
               │
    ┌──────────┼──────────┐
    │                     │
    ▼                     ▼
┌──────────┐        ┌──────────┐
│ REFLECT  │        │ CONNECT  │
│ (Time)   │        │ (Others) │
└──────────┘        └──────────┘

PT INSIGHT:
The gap (⊥) is not emptiness—it's an irreducible promise.
This promise, when combined with time, creates REFLECT.
This promise, when combined with others, creates CONNECT.

The tetrahedral structure has O(16) interior promises
between its four components. This complexity is justified
only because the emergent value (sovereignty preserved
through maintained separation) exceeds the coordination
cost of the additional promises.
```

---

## Economic Sustainability Model

### Revenue Streams (Promise-Economic Flows)

```
┌─────────────────────────────────────────────────────────────┐
│              REVENUE STREAMS (Promise-Economic)              │
└─────────────────────────────────────────────────────────────┘

PRIMARY: Signal Fees (Assessment Payments)
┌────────────────────────────────────────┐
│ • 0.01 ZEC per signal                  │
│ • Sybil resistance (skin-in-game)      │
│ • Scales with participation            │
│ • Recurring (continuous assessment)    │
│                                        │
│ PT: Signals are assessment payments    │
│     Each signal = demonstrated         │
│     comprehension commitment           │
└────────────────────────────────────────┘

SECONDARY: Chronicle Rewards (Promise-Keeping Compensation)
┌────────────────────────────────────────┐
│ • SWORD for privacy chronicles         │
│ • MAGE for delegation chronicles       │
│ • Guardian validation rewards          │
│ • Progressive issuance                 │
│                                        │
│ PT: Tokens reward demonstrated         │
│     promise-keeping behavior           │
└────────────────────────────────────────┘

TERTIARY: VRC Economics (Promise Bundle Value)
┌────────────────────────────────────────┐
│ • Formation fees (0.01 ZEC each)       │
│ • 70:1 coordination efficiency         │
│ • Network effects (O(n²) VRCs)        │
│ • Cross-ecosystem treaties             │
│                                        │
│ PT: VRC value from promise bundle      │
│     reuse—one-time assessment,         │
│     unlimited coordination             │
└────────────────────────────────────────┘
```

### Sustainability Timeline

```
┌─────────────────────────────────────────────────────────────┐
│                   SUSTAINABILITY PATH                        │
└─────────────────────────────────────────────────────────────┘

Phase 1: Foundation (Year 1)
┌────────────────────────────────────────┐
│ • Grant-funded + signal revenue        │
│ • 15,000-50,000 signals/month          │
│ • Building promise-keeper network      │
│ • Grants: 60%, Signals: 40%            │
└────────────────────────────────────────┘
                    │
                    ▼
Phase 2: Growth (Year 2)
┌────────────────────────────────────────┐
│ • Approaching break-even               │
│ • 30,000-80,000 signals/month          │
│ • Multiple ecosystems                  │
│ • Grants: 20%, Signals: 80%            │
└────────────────────────────────────────┘
                    │
                    ▼
Phase 3: Sustainability (Year 3+)
┌────────────────────────────────────────┐
│ • Self-sustaining                      │
│ • 50,000-100,000+ signals/month        │
│ • Surplus for ecosystem grants         │
│ • Grants: 0%, Signals: 100%+           │
│                                        │
│ PT: Promise network becomes self-      │
│     reinforcing—value creation         │
│     exceeds coordination cost          │
└────────────────────────────────────────┘
```

### Break-Even Analysis

```
Monthly Costs: $125,000
├─ Development: $85,000
├─ Infrastructure: $25,000
└─ Operations: $15,000

Break-Even Signals: ~65,500/month
├─ Revenue per signal: $5.00
├─ Shielded pool (38.2%): $1.91/signal for operations
├─ Required: $125,000 / $1.91 ≈ 65,445 signals
└─ Active First Persons: ~21,815 (at 3 signals/month)

PT INSIGHT:
Signal-based funding = assessment-based sustainability
Protocol funded by demonstrated comprehension,
not speculation or extraction
```

---

## Trust Function Visualization

### Trust τ as Accumulated Assessment

```
┌─────────────────────────────────────────────────────────────┐
│              TRUST FUNCTION VISUALIZATION                    │
│         τ: [0,1] expectation of promise-keeping             │
└─────────────────────────────────────────────────────────────┘

TRUST ACCUMULATION CURVE:

Trust τ
    │
1.0 │                                    ┌─────── Dragon ────
    │                               ____/
0.8 │                          ____/
    │                     ____/           Guardian eligible
0.7 │                ____/
    │           ____/
0.5 │      ____/                          ┌─────── Heavy ────
    │  ___/                          Intel Pools access
0.3 │ /
    │/                                    ┌─────── Light ────
0.2 │                                Basic coordination
    │
0.0 │────────────────────────────────────┴─────── Blade ────
    └─────────────────────────────────────────────────────────
    0     50    100    150    200    300    400    500+ signals

TIER DEFINITIONS:

┌─────────┬──────────┬───────────┬─────────────────────────────┐
│  Tier   │ Signals  │  Trust τ  │  Capability                 │
├─────────┼──────────┼───────────┼─────────────────────────────┤
│ Blade 🗡️│  0-49    │  0.0-0.2  │  Learning, basic access     │
│ Light 🛡️│  50-149  │  0.2-0.5  │  Basic coordination, VRCs   │
│ Heavy ⚔️│ 150-499  │  0.5-0.8  │  Intel Pools, governance    │
│ Dragon🐉│  500+    │  0.8-1.0  │  Guardian, proposals        │
└─────────┴──────────┴───────────┴─────────────────────────────┘

PT INSIGHT:
• Each signal = assessment event α(π)
• Positive assessment → incremental trust increase
• Trust τ = accumulated evidence of promise-keeping
• Higher τ → greater capability access
• Guardian eligibility requires τ ≥ 0.8

WHY THIS WORKS:
┌────────────────────────────────────────┐
│ Trust cannot be purchased directly     │
│ Trust must be EARNED through:          │
│ • Sustained assessment payments        │
│ • Demonstrated comprehension           │
│ • Accumulated evidence over time       │
│                                        │
│ This creates natural Sybil resistance: │
│ • 500 signals = ~$2,500 + TIME         │
│ • Cannot be rushed                     │
│ • Cannot be faked                      │
│ • Proves genuine engagement            │
└────────────────────────────────────────┘
```

### Trust in VRC Formation

```
VRC TRUST REQUIREMENTS:

                    Alice (τ_A)              Bob (τ_B)
                         │                       │
                         │    VRC Formation      │
                         └──────────┬────────────┘
                                    │
                                    ▼
                         ┌──────────────────┐
                         │  Minimum τ for   │
                         │  VRC Formation:  │
                         │                  │
                         │  τ_A ≥ 0.2 AND   │
                         │  τ_B ≥ 0.2       │
                         │  (Light tier+)   │
                         └──────────────────┘

TRUST TRANSFER IN VRCs:

┌─────────────────────────────────────────────────────────────┐
│ VRC trust is NOT τ_A + τ_B                                  │
│ VRC trust is MIN(τ_A, τ_B) with bilateral verification     │
│                                                              │
│ Why: Both parties must keep their promises                  │
│      VRC is only as strong as weakest promise-keeper        │
│                                                              │
│ Example:                                                     │
│ • Alice (τ = 0.7) + Bob (τ = 0.5) → VRC trust ≈ 0.5        │
│ • High-trust Alice cannot "transfer" trust to low-trust Bob │
│ • Both must demonstrate promise-keeping independently       │
└─────────────────────────────────────────────────────────────┘
```

---

## Status Indicators Legend

### Component Status Meanings

```
✅ ACTIVE (Production-Ready)
├─ Specification complete
├─ Implementation tested
├─ Deployed and functioning
├─ Can be relied upon
└─ Promise-keeping verified in production

🚧 WIP (Work In Progress)
├─ Specification mostly complete
├─ Reference implementation in development
├─ Testing in controlled environments
├─ Not yet production-ready
└─ Promise verification mechanisms in development

📋 PLANNED
├─ Specification in development
├─ Clear roadmap
├─ Resource allocation determined
├─ Timeline established
└─ Promise structure designed, not yet implemented

🔬 EXPLORATORY
├─ Concept validated
├─ Specification draft only
├─ Research phase
├─ May or may not be implemented
└─ Promise structure theoretical

⚠️ DEPRECATED
├─ No longer recommended
├─ Being phased out
├─ Migration path available
└─ Use newer approach instead

❌ NOT SUPPORTED
├─ Explicitly not part of protocol
├─ Will not be implemented
└─ Use alternatives
```

### How to Read Document Status

```
Example Document Section:

┌────────────────────────────────────────────────────┐
│ 4.2 Guardian Slash Revenue (Reference Impl) 🚧 WIP│
│                                                     │
│ NOTE: This section describes guardian slash        │
│ revenue from the 0xagentprivacy reference          │
│ implementation using SWORD tokens (WIP). Other     │
│ ecosystems may use different guardian models       │
│ with different or no slash revenue.                │
│                                                     │
│ [Content describes SWORD-based slashing...]        │
│                                                     │
│ PT: Slashing = economic penalty for promise        │
│     violation, creating incentive compatibility    │
└────────────────────────────────────────────────────┘

Reading this:
• Title mentions "(Reference Impl)" = not universal
• Status emoji 🚧 WIP = not production-ready yet
• Note clarifies: other approaches valid
• Content describes: one specific implementation
• PT annotation: explains promise-theoretic rationale

Interpretation:
This is ONE way to do guardians (promise-keepers), not THE way.
Useful for understanding reference approach.
Feel free to adapt for your ecosystem context.
```

---

## How to Use These Diagrams

### Navigation Guide

```
BY AUDIENCE:

Researchers/Academics:
├─ Start with: Four-Layer Architecture
├─ Deep dive: Promise Theory Foundations
├─ Math focus: Dual Agent Architecture
├─ Theory: Superagent Structure
└─ Validation: Trust Function Visualization

Developers/Builders:
├─ Start with: Learning Pathway Flow
├─ Understand: Signal vs Ceremony
├─ Choose: Blockchain Flexibility
├─ Implement: Guardian Model Alternatives
└─ Reference: VRC Formation Process

Investors/Advisors:
├─ Start with: Economic Sustainability
├─ Understand: Revenue streams
├─ Evaluate: Trust Function (user retention)
└─ Assess: Long-term viability

Community/Users:
├─ Start with: Learning Pathway Flow
├─ Understand: VRC Formation Process
├─ See costs: Signal vs Ceremony
└─ Choose path: Guardian qualification

Promise Theory Practitioners (NEW):
├─ Start with: Promise Theory Foundations
├─ Deep dive: Superagent Structure
├─ Apply: Trust Function Visualization
├─ Reference: Cross-Layer Translation Table
└─ Compare: Guardian Model Alternatives

BY QUESTION:

"How do the layers relate?" → Four-Layer Architecture
"What is Promise Theory's role?" → Promise Theory Foundations (NEW)
"How does privacy work?" → Dual Agent Architecture
"What is the superagent?" → Superagent Structure (NEW)
"How do I participate?" → Learning Pathway Flow
"What's the difference between signals and ceremonies?" → Signal vs Ceremony
"Why different compression numbers?" → Compression Ratios Context
"Do I need SWORD tokens?" → Guardian Model Alternatives
"Is Zcash required?" → Blockchain Flexibility
"How do VRCs work?" → VRC Formation Process
"Why four components not two?" → Information Flow Topology
"Is this sustainable?" → Economic Sustainability Model
"How does trust accumulate?" → Trust Function Visualization (NEW)
"What does ✅ vs 🚧 mean?" → Status Indicators Legend
```

---

## Quick Reference Cards

### Card 1: Core Architecture (30 seconds)

```
0xagentprivacy = Privacy-first agent coordination

Architecture:
• Dual agents (Swordsman ⚔️ protects, Mage 🧙 delegates)
• Conditional independence (s ⊥ m | X)
• The Gap preserves privacy (R < 1)
• Four emergent components (protect, delegate, reflect, connect)

Promise Theory:
• Agents promise only own behavior (autonomy axiom)
• Separation is a kept promise (irreducible)
• Trust τ from accumulated assessments
• VRCs are bilateral promise bundles

Participation:
• Learn spellbook → form proverbs → post signals
• 0.01 ZEC per signal (~$5 at $500/ZEC)
• 500+ signals (τ ≥ 0.8) → guardian candidacy

Status: Documentation complete, Zcash implementation WIP
```

### Card 2: Promise Theory (30 seconds)

```
Promise Theory = Formal semantics for autonomous systems

Core Principles:
• Autonomy axiom: Agents promise only own behavior
• Superagent: FP+S+M as composite with interior promises
• Irreducible promise: Gap exists in relationship, not components
• Assessment α(π): Signals as promise verification events
• Trust function τ: 0-1 expectation of promise-keeping

Why It Matters:
• Single-agent systems FORMALLY VIOLATE autonomy axiom
• Dual-agent separation is mathematically necessary
• Economic incentives must be promise-compatible
• Trust earned through demonstrated promise-keeping

Application:
• Swordsman promises protection (own behavior)
• Mage promises delegation (own behavior)
• Separation promise exists between them
• Guardian = professional promise-keeper
```

### Card 3: Economics (30 seconds)

```
Revenue: Signal fees + chronicle rewards + VRC value
Cost: 0.01 ZEC per signal (assessment payment)
Sustainability: Non-inflationary, assessment-based, multiple streams

Trust Tiers (Trust Function τ):
• Blade (0-49 signals, τ < 0.2): Learning
• Light (50-149 signals, τ < 0.5): Basic coordination
• Heavy (150-499 signals, τ < 0.8): Intel Pools
• Dragon (500+ signals, τ ≥ 0.8): Guardian eligible

Example costs (at $500/ZEC):
• 13 sections (main spellbook) = $65 (τ ≈ 0.05)
• 500 signals (guardian qualification) = $2,500 (τ ≥ 0.8)

Growth:
• Year 3: Self-sustaining
• Scales with network (O(n²) VRC relationships)
• Promise-keeping creates value → value sustains network
```

### Card 4: Getting Started (30 seconds)

```
1. READ: Spellbook (13 Acts)
2. FORM: Proverbs (RPP compression)
3. POST: Signals (0.01 ZEC each) → Assessment events
4. BUILD: Trust tiers (progressive τ accumulation)
5. QUALIFY: Guardian (500+ signals, τ ≥ 0.8)

Documents:
• Whitepaper v4.7 (mathematical + PT foundations)
• Spellbook v4.1.1 (narrative learning)
• Research Paper v3.5 (proofs + PT grounding)
• Tokenomics v3.0 (promise-economic alignment)
• Promise Theory Reference v1.0 (formal semantics)
• This guide v1.2 (visual reference)

All at: agentprivacy.ai
Building at: sync.soulbis.com | intel.agentkyra.ai
```

---

## Appendix: Diagram Format Notes

### ASCII Art Conventions

```
Box Drawing:
┌─┐  │  ├─┤  ┬  ┴  ┼  ─  │

Arrows:
→  ←  ↑  ↓  ↔  ▼  ▲  ◄  ►

Relationships:
├─  Parent-child
└─  Last child
│   Continuation
─   Horizontal connection

Emojis:
⚔️  Swordsman (protection promise)
🧙  Mage (delegation promise)
😊  First Person (authorizer)
🗡️  Blade tier
🛡️  Light tier
⚔️  Heavy tier
🐉  Dragon tier
✅  Active
🚧  WIP
📋  Planned
🔬  Exploratory
⊥   Separation promise
```

### Reading Flowcharts

```
Boxes with rounded corners = Process/action
Boxes with sharp corners = Data/state
Diamonds = Decision points
Arrows = Flow direction
Parallel lines = Simultaneous
Dotted lines = Optional/conditional
⊥ symbol = Separation promise (maintained independence)
```

---

**Version:** 1.2 - Promise Edition  
**License:** CC BY-SA 4.0  
**Last Updated:** December 11, 2025  
**Maintained by:** 0xagentprivacy Protocol Team

**Companion Documents:**
- Whitepaper v4.7 (Mathematical + Promise Theory foundations)
- Research Paper v3.5 (Proofs + PT grounding)
- Spellbook v4.1.1 (Narrative learning)
- Tokenomics v3.0 (Promise-economic alignment)
- Promise Theory Reference v1.0 (Formal semantics)
- Glossary v2.2 (Canonical terminology + PT section)

**For latest documentation:** [agentprivacy.ai](https://agentprivacy.ai)  
**Building at:** [sync.soulbis.com](https://sync.soulbis.com) | [intel.agentkyra.ai](https://intel.agentkyra.ai)

---

*These diagrams are living documents. As the protocol evolves, diagrams will be updated to reflect the latest architecture, implementations, and understanding.*

**"Agents can only promise their own behavior—the diagrams show how."**
