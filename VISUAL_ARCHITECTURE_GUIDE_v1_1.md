# 0xagentprivacy Visual Architecture Guide
**Diagrams, Flows, and Conceptual Maps**

**Version:** 1.1  
**Date:** November 25, 2025  
**Purpose:** Visual reference for understanding 0xagentprivacy architecture across technical, narrative, and economic layers

**Pricing Basis:** $500/ZEC (canonical). Economic projections in growth scenarios may reflect historical ZEC prices and should be scaled accordingly.

---

## Table of Contents

1. [Three-Layer Architecture](#three-layer-architecture)
2. [Dual Agent Architecture](#dual-agent-architecture)
3. [First Person Stack](#first-person-stack)
4. [Learning Pathway Flow](#learning-pathway-flow)
5. [Signal vs Ceremony Distinction](#signal-vs-ceremony-distinction)
6. [Compression Ratios Context](#compression-ratios-context)
7. [Guardian Model Alternatives](#guardian-model-alternatives)
8. [Blockchain Flexibility](#blockchain-flexibility)
9. [VRC Formation Process](#vrc-formation-process)
10. [Information Flow Topology](#information-flow-topology)
11. [Economic Sustainability Model](#economic-sustainability-model)
12. [Status Indicators Legend](#status-indicators-legend)

---

## Three-Layer Architecture

### Overview: Same Principles, Different Lenses

```
┌──────────────────────────────────────────────────────────────┐
│                  0xagentprivacy Protocol                      │
│            (Meta-Protocol for Privacy & Sovereignty)          │
└──────────────────────────────────────────────────────────────┘
                              │
                ┌─────────────┼─────────────┐
                │             │             │
                ▼             ▼             ▼
    
┌───────────────────┐  ┌───────────────────┐  ┌───────────────────┐
│   MATHEMATICAL/   │  │   NARRATIVE/      │  │   ECONOMIC/       │
│   ARCHITECTURAL   │  │   MYTHOLOGICAL    │  │   PRACTICAL       │
│                   │  │                   │  │                   │
│  Whitepaper v4.3  │  │  Spellbook v4.0.1 │  │  Tokenomics v2.0  │
└───────────────────┘  └───────────────────┘  └───────────────────┘
         │                      │                      │
         │                      │                      │
    ┌────▼────┐           ┌────▼────┐           ┌────▼────┐
    │ Proofs  │           │ Stories │           │ Tokens  │
    │ Bounds  │           │ Acts    │           │ Signals │
    │ Theorems│           │ Arcs    │           │ Rewards │
    └─────────┘           └─────────┘           └─────────┘

SAME ARCHITECTURE, THREE EXPRESSIONS:

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
```

### Cross-Layer Translation Table

| Concept | Mathematical | Narrative | Economic |
|---------|-------------|-----------|----------|
| **Dual Agents** | s ⊥ m \| X | Soulbis & Soulbae | SWORD & MAGE agents |
| **Separation** | Conditional independence | The Gap | Information firewall |
| **Privacy Bound** | R < 1 (reconstruction ceiling) | "They cannot see your whole" | Surveillance resistance |
| **Learning** | Compression protocol | Reading Acts, deriving proverbs | Posting signals (0.01 ZEC) |
| **Trust** | Bilateral knowledge | Shared stories | VRCs (relationship credentials) |
| **Infrastructure** | System observers | Guardians of the realm | SWORD token holders |

---

## Dual Agent Architecture

### Core Structure: Swordsman ⊥ Mage

```
                        ┌────────────────┐
                        │  FIRST PERSON  │
                        │   (You - 🗝️)    │
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
            └───────────────┘         └───────────────┘
                    │                         │
        Observes X completely      Acts using authorized info
        Reveals nothing directly   Public delegation/coordination
                    │                         │
                    └────────────┬────────────┘
                                 │
                    THE GAP (conditional independence)
                                 │
                            s ⊥ m | X
                                 │
                    Additive information bounds:
                    I(X; s,m) ≤ I(X;s) + I(X;m)
                                 │
                    Reconstruction ceiling: R < 1
                                 │
                    ▼
        ┌─────────────────────────────────┐
        │  PRIVACY PRESERVED THROUGH      │
        │  ARCHITECTURAL SEPARATION       │
        └─────────────────────────────────┘
```

### Information Flow Detail

```
Private Ledger           Swordsman (s)              Mage (m)
    (X)                   Observer                  Actor
     │                       │                        │
     ├──────────────────────►│                        │
     │   Complete view       │                        │
     │   (all context)       │                        │
     │                       │                        │
     │                       │   Authorized subset    │
     │                       ├───────────────────────►│
     │                       │   (RPP compressed)     │
     │                       │                        │
     │                       │                        │
     │                       │                        ▼
     │                       │                  Public Action
     │                       │                  (delegation)
     │                       │                        │
     │                       │                        │
     │◄──────────────────────┴────────────────────────┘
     │              Coordination through
     │              compression protocol
     │              (RPP + spells)
     │
     └─► ADVERSARY CANNOT RECONSTRUCT X
         Even observing both s and m
         R(X|s,m) < 1 (provable bound)
```

### Key Properties

```
PROPERTY 1: Conditional Independence
┌────────────────────────────────────────┐
│ s ⊥ m | X                              │
│                                        │
│ Given First Person's state X,         │
│ Swordsman and Mage provide no         │
│ additional information about each     │
│ other                                 │
└────────────────────────────────────────┘

PROPERTY 2: Additive Bounds
┌────────────────────────────────────────┐
│ I(X; s,m) ≤ I(X;s) + I(X;m)           │
│                                        │
│ Joint information is bounded by       │
│ SUM not PRODUCT of individual         │
│ information leakage                   │
└────────────────────────────────────────┘

PROPERTY 3: Reconstruction Ceiling
┌────────────────────────────────────────┐
│ R(X|s,m) < 1                          │
│                                        │
│ Even with perfect observations of     │
│ both agents, adversary cannot fully   │
│ reconstruct First Person's state      │
└────────────────────────────────────────┘
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
        │                       │  │                      │
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
                    │                         │
                    └─────────────────────────┘
```

### Layer Descriptions

**Sovereign Agent (Top Layers):**
- **UI & Human Experience**: User-facing interfaces, ceremonies, and trust indicators that enable human interaction with the system
- **Trust Tasks**: Core functionality including credential exchange, secure messaging, payments, and coordination with AI agents

**Trust Spanning Protocol (TSP):**
- Connects the agent layer (user-facing) with the wallet layer (data/asset storage)
- Enables secure communication and coordination between agent operations and wallet state
- Provides the bridge for trust operations across the stack

**Sovereign Wallet (Bottom Layers):**
- **Verifiable Credentials & Digital Assets**: Storage layer for identity proofs and digital value
- **Self-Certifying Identifiers (SCIDs)**: Decentralized identity layer enabling self-sovereign, portable identifiers
- **Cryptographic Keys**: Foundation layer providing security, signing, and verification capabilities

### Key Properties

```
PROPERTY 1: Layered Separation
┌────────────────────────────────────────┐
│ Each layer has distinct responsibility │
│ Agent = interaction & coordination     │
│ Wallet = storage & identity            │
│ TSP = secure bridging                  │
└────────────────────────────────────────┘

PROPERTY 2: Self-Sovereignty
┌────────────────────────────────────────┐
│ User controls all layers through keys   │
│ No third-party dependencies            │
│ Portable across systems                │
└────────────────────────────────────────┘w

PROPERTY 3: Trust Spanning
┌────────────────────────────────────────┐
│ TSP enables trust operations across    │
│ agent and wallet boundaries            │
│ Maintains security while enabling      │
│ coordination                           │
└────────────────────────────────────────┘
```

---

## Learning Pathway Flow

### Spellbook → Signals → Guardianship

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
└────────────────┬───────────────────────────┘
                 │
                 ▼
┌────────────────────────────────────────────┐
│ STEP 3: Post Signal                       │
│                                            │
│ • 1 proverb = 1 signal                    │
│ • Cost: 0.01 ZEC (~$5 at $500/ZEC)       │
│ • On-chain proof of comprehension         │
│ • Generates MAGE tokens                   │
└────────────────┬───────────────────────────┘
                 │
                 ▼
┌────────────────────────────────────────────┐
│ STEP 4: Build Trust (Progressive Tiers)   │
│                                            │
│ Trust Tier       Signals    Capability    │
│ ──────────────────────────────────────    │
│ Blade            0-49       Learning       │
│ Light            50-149     Basic coord    │
│ Heavy            150-499    Intel Pools    │
│ Dragon           500+       Guardian       │
└────────────────┬───────────────────────────┘
                 │
                 ▼
┌────────────────────────────────────────────┐
│ STEP 5: Guardian Qualification            │
│                                            │
│ IF: Dragon tier (500+ signals)            │
│ THEN: Can send Swordsman as guardian      │
│                                            │
│ Guardian proves:                           │
│ • Reconstruction ability                   │
│ • Protocol comprehension                   │
│ • Sustained commitment                     │
│                                            │
│ Earned through learning, not purchased    │
└────────────────┬───────────────────────────┘
                 │
                 ▼
              SUCCESS
    First Person now participates as
    infrastructure provider with proven
    comprehension and reconstruction ability
```

### Cost Breakdown Example

```
Learning Path           Signals    Cost (ZEC)   Cost (USD)*
──────────────────────────────────────────────────────────
13 sections (main)      13         0.13 ZEC     $65
30 tales (Zero)         30         0.30 ZEC     $150
Light tier minimum      50         0.50 ZEC     $250
Dragon tier minimum     500        5.00 ZEC     $2,500

* At canonical $500/ZEC price point

KEY INSIGHT: 
Guardian qualification costs ~$2,500 in sustained learning
This filters for genuine comprehension and commitment
Higher barrier than "cheap" signals, but earned not bought
```

---

## Signal vs Ceremony Distinction

### Critical Terminology Difference

```
┌─────────────────────────────────────────────────────────────┐
│                    GENESIS CEREMONY                          │
│                  (One-time origination)                      │
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
              Purpose: Originate your sovereign agents
                              │
                              ▼
                    ┌─────────────────┐
                    │  You now have:  │
                    │  • Swordsman ⚔️  │
                    │  • Mage 🧙       │
                    └─────────────────┘

─────────────────────────────────────────────────────────────

┌─────────────────────────────────────────────────────────────┐
│                         SIGNALS                              │
│                  (Ongoing proverb posts)                     │
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
              Purpose: Demonstrate learning, build trust
                              │
                              ▼
                    ┌─────────────────┐
                    │  Each signal:   │
                    │  • Proves learn │
                    │  • Earns MAGE   │
                    │  • Builds trust │
                    └─────────────────┘
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

---

## Compression Ratios Context

### Types of Compression (Context-Dependent)

```
┌─────────────────────────────────────────────────────────────┐
│              COMPRESSION RATIO DISAMBIGUATION                 │
│         (Different ratios measure different things)           │
└─────────────────────────────────────────────────────────────┘

TYPE 1: Agent Coordination Efficiency (Communication)
┌────────────────────────────────────────────┐
│ Ratio: 70:1                                │
│ Measurement: Communication reduction       │
│ Calculation: 70 messages → 1 via context  │
│ Context: VRC coordination value           │
│                                            │
│ What it means:                             │
│ Agents with shared framework need 70×     │
│ fewer messages to coordinate effectively  │
│ (efficiency gain, not direct cost ratio)  │
└────────────────────────────────────────────┘

TYPE 2: Content → Proverb (Semantic)
┌────────────────────────────────────────────┐
│ Ratio: 200:1                               │
│ Measurement: Text compression              │
│ Calculation: 5,000 words → 25 words       │
│ Context: RPP compression of knowledge     │
│                                            │
│ What it means:                             │
│ Complex concept compressed into proverb   │
│ that preserves meaning in context         │
└────────────────────────────────────────────┘

TYPE 3: Proverb → Cipher (Symbolic)
┌────────────────────────────────────────────┐
│ Ratio: 5:1                                 │
│ Measurement: Symbol compression            │
│ Calculation: 25 words → 5 symbols         │
│ Context: Spellbook cipher inscriptions    │
│                                            │
│ What it means:                             │
│ Proverb further compressed into symbolic  │
│ spell for agent-agent communication       │
└────────────────────────────────────────────┘

TYPE 4: Total Semantic (End-to-End)
┌────────────────────────────────────────────┐
│ Ratio: 1,000:1                             │
│ Measurement: Full semantic compression     │
│ Calculation: 5,000 words → 5 symbols      │
│ Context: Content → cipher (complete)      │
│                                            │
│ What it means:                             │
│ Entire complex framework compressed into  │
│ tiny symbolic representation with full    │
│ semantic preservation for those who       │
│ learned the compression protocol          │
└────────────────────────────────────────────┘
```

### Context Table

| When document says... | It means... | What's measured |
|-----------------------|-------------|-----------------|
| "70:1 compression" in VRC Economics | Agent coordination efficiency | 70 messages → 1 message |
| "70:1 efficiency" | Same as above | Communication reduction |
| "200:1 compression" in Spellbook | Content → proverb | 5,000 words → 25 words |
| "5:1 compression" in Cipher | Proverb → symbols | 25 words → 5 symbols |
| "1,000:1 compression" | Total semantic | Content → cipher (end-to-end) |

### Visual Compression Cascade

```
    COMPLEX CONTENT (5,000 words)
           │
           │  [RPP Protocol]
           │  200:1 compression
           ▼
       PROVERB (25 words)
           │
           │  [Cipher Protocol]
           │  5:1 compression
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

For those who didn't learn it,
these are just random emojis.

This is the power of bilateral compression.
```

---

## Guardian Model Alternatives

### Ecosystem-Dependent Approaches

```
┌─────────────────────────────────────────────────────────────┐
│     GUARDIAN MODEL FLEXIBILITY (Choose based on context)     │
└─────────────────────────────────────────────────────────────┘

MODEL 1: Merit + Time (SWORD-based) [0xagentprivacy Reference]
┌────────────────────────────────────────────────────────┐
│ Guardian Type: Token holders with proven comprehension │
│ Selection: Dragon tier (500+ signals) required        │
│ Incentive: Quality-based reallocation from failures   │
│ Context: Consumer privacy, learning-first communities │
│ Status: 🚧 WIP - reference implementation             │
│                                                        │
│ Trust Tier Progression:                                │
│ Blade (0-49) → Light (50-149) → Heavy (150-499)      │
│ → Dragon (500+) → Guardian eligibility                │
└────────────────────────────────────────────────────────┘

MODEL 2: SLA Contracts (Contract-based) [Enterprise]
┌────────────────────────────────────────────────────────┐
│ Guardian Type: Service providers with legal contracts │
│ Selection: RFP process, due diligence                 │
│ Incentive: Fixed fees, reputation, contract renewal   │
│ Context: Enterprise deployments, regulated industries │
│ Status: ✅ Active - proven model                      │
│                                                        │
│ No slashing, no tokens needed                         │
│ Pure service provider relationship                    │
└────────────────────────────────────────────────────────┘

MODEL 3: Peer Reputation (Social-based) [Academic]
┌────────────────────────────────────────────────────────┐
│ Guardian Type: Trusted peers, colleagues, institutions│
│ Selection: Academic merit, peer recommendation        │
│ Incentive: Reputation, citation, academic credit      │
│ Context: Research consortia, academic networks        │
│ Status: ✅ Active - used in research settings         │
│                                                        │
│ No tokens, no slashing                                │
│ Pure reputation-based trust                           │
└────────────────────────────────────────────────────────┘

MODEL 4: Economic Staking (Capital-based) [DeFi]
┌────────────────────────────────────────────────────────┐
│ Guardian Type: Capital holders staking collateral    │
│ Selection: Stake amount, validator set               │
│ Incentive: Block rewards, slashing for misbehavior   │
│ Context: DeFi protocols, blockchain validators       │
│ Status: ✅ Active - traditional crypto model          │
│                                                        │
│ Staking Cost: $500 per ZEC                            │
│ Capital requirement, economic slashing                │
│ Proven but capital-intensive                          │
└────────────────────────────────────────────────────────┘

MODEL 5: Trust Consensus (Community-based) [Activist]
┌────────────────────────────────────────────────────────┐
│ Guardian Type: Trusted community members              │
│ Selection: Community vote, consensus mechanism        │
│ Incentive: Community standing, mission alignment      │
│ Context: Activist networks, DAOs, cooperatives       │
│ Status: ✅ Active - used in community projects        │
│                                                        │
│ No tokens, no capital, just trust                     │
│ Community-driven selection                            │
└────────────────────────────────────────────────────────┘
```

### Selection Matrix

| Use Case | Recommended Model | Why |
|----------|------------------|-----|
| **Consumer privacy app** | Merit + Time (SWORD) | Learning proves comprehension |
| **Enterprise deployment** | SLA Contracts | Legal clarity, clear SLAs |
| **Research network** | Peer Reputation | Academic merit matters |
| **DeFi protocol** | Economic Staking | Capital alignment |
| **Activist network** | Trust Consensus | Mission alignment crucial |

### Key Insight

```
┌─────────────────────────────────────────────────────┐
│ THE PROTOCOL REQUIRES: Guardians (infrastructure)   │
│ THE PROTOCOL DOES NOT REQUIRE: Specific selection  │
│                                 mechanism           │
│                                                     │
│ What matters: Guardians protect First Persons      │
│ How chosen: Depends on ecosystem context           │
└─────────────────────────────────────────────────────┘
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
        └───────────────────┘   └───────────────────┘
                    │                   │
                    └─────────┬─────────┘
                              │
                    That's it. That's all.
                              │
                              ▼
        ┌─────────────────────────────────────────┐
        │ HOW you provide these is flexible!      │
        └─────────────────────────────────────────┘
```

### Implementation Options

```
OPTION 1: Zcash (Native, Simplest) [Reference Implementation]
┌──────────────────────────────────────────────────────┐
│ Public Ledger:  Transparent ZEC transactions         │
│ Private Ledger: Shielded ZEC (native privacy)        │
│                                                       │
│ Advantages:                                           │
│ • Native shielded pool                               │
│ • Simple architecture                                │
│ • Proven privacy (zk-SNARKs)                         │
│ • Lower complexity                                   │
│                                                       │
│ Considerations:                                       │
│ • Smaller ecosystem (vs Ethereum)                    │
│ • Less DeFi integration                              │
│                                                       │
│ Status: 🚧 WIP - we're building on this first       │
│ Why: Proves the simplest path works                 │
└──────────────────────────────────────────────────────┘

OPTION 2: Ethereum + Privacy Layer (Composed, Most Flexible)
┌──────────────────────────────────────────────────────┐
│ Public Ledger:  Ethereum L1 or L2                    │
│ Private Ledger: Kohaku / Aztec / Starknet / Mina    │
│                                                       │
│ Advantages:                                           │
│ • Massive ecosystem                                  │
│ • Better DeFi integration                            │
│ • More tooling, more users                           │
│ • Multiple privacy layer options                     │
│                                                       │
│ Considerations:                                       │
│ • More complex architecture                          │
│ • Two-system coordination needed                     │
│ • Privacy layer maturity varies                      │
│                                                       │
│ Status: 📋 Planned - next after Zcash proves concept│
│ Why: Largest addressable market                      │
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

### Decision Tree

```
        Choose Blockchain Implementation
                     │
         ┌───────────┴───────────┐
         │                       │
         ▼                       ▼
   Want simplest         Want largest
   architecture?         ecosystem?
         │                       │
         │                       │
         ▼                       ▼
   ┌─────────┐          ┌──────────────┐
   │  ZCASH  │          │  ETHEREUM +  │
   │ (Native)│          │ Privacy Layer│
   └─────────┘          └──────────────┘
         │                       │
         │                       │
         ▼                       ▼
   Lower complexity      Higher complexity
   Smaller ecosystem     Larger ecosystem
   Native privacy        Composed privacy
   Faster to build       More DeFi access

BOTH ARE VALID. BOTH ARE SUPPORTED.
Choose based on your ecosystem's needs.
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
└─────────────────────────────────────────────────────┘
```

### Ecosystem Dynamics: Adaptive Architecture

```
┌─────────────────────────────────────────────────────────────┐
│         ECOSYSTEM-DYNAMIC ARCHITECTURE                        │
│                                                              │
│  0xagentprivacy adapts to the ecosystem it's deployed in     │
│  rather than forcing ecosystems to adapt to it             │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
        ┌──────────────────────────────────────────┐
        │  Protocol Core (Universal)              │
        │  • Dual agent model (s ⊥ m | X)        │
        │  • RPP compression                      │
        │  • VRC formation                        │
        │  • Signal economics                     │
        └──────────────┬───────────────────────────┘
                       │
        ┌──────────────┼──────────────┐
        │              │              │
        ▼              ▼              ▼
    ┌────────┐   ┌──────────┐   ┌──────────┐
    │ Zcash  │   │ Ethereum │   │  Other   │
    │ Native │   │ + Privacy│   │ Chains   │
    └────────┘   └──────────┘   └──────────┘
        │              │              │
        │              │              │
        ▼              ▼              ▼
    Same core    Same core      Same core
    protocol     protocol       protocol
    different    different      different
    substrate    substrate      substrate

KEY PRINCIPLE:
The protocol is substrate-agnostic.
It works WITH existing ecosystems,
not against them.
```

### Example: AZTEC + Ethereum Implementation

```
┌─────────────────────────────────────────────────────────────┐
│         AZTEC + ETHEREUM: CONCRETE EXAMPLE                   │
│         (Ecosystem-Dynamic Deployment)                        │
└─────────────────────────────────────────────────────────────┘

ARCHITECTURE LAYER MAPPING:

┌─────────────────────────────────────────────────────────────┐
│                    PUBLIC LEDGER (Ethereum)                  │
│                                                               │
│  • Signals: ERC-20 token transfers (MAGE tokens)           │
│  • VRCs: Smart contract commitments on Ethereum L1/L2      │
│  • Guardians: SWORD token holders (ERC-20 on Ethereum)     │
│  • Ceremonies: Public on-chain events                      │
│                                                               │
│  Benefits:                                                    │
│  • Access to entire Ethereum DeFi ecosystem                  │
│  • Uniswap, Aave, Compound integration                      │
│  • Standard wallet support (MetaMask, etc.)                 │
│  • Layer 2 scaling (Arbitrum, Optimism, Base)              │
└─────────────────────────────────────────────────────────────┘
                              │
                              │ Bridge/Coordination
                              │
┌─────────────────────────────────────────────────────────────┐
│                  PRIVATE LEDGER (AZTEC)                     │
│                                                               │
│  • First Person state: Private notes on AZTEC network       │
│  • Agent actions: Shielded transactions                    │
│  • Private data: Encrypted via AZTEC's zk-SNARKs           │
│  • Coordination: Private smart contracts                   │
│                                                               │
│  Benefits:                                                    │
│  • Zero-knowledge privacy proofs                            │
│  • Private value transfers                                  │
│  • Confidential smart contract execution                    │
│  • Composability with Ethereum ecosystem                    │
└─────────────────────────────────────────────────────────────┘

WORKFLOW EXAMPLE: Signal Posting

1. USER ACTION (Ethereum):
   ┌─────────────────────────────────────┐
   │ User forms proverb from spellbook   │
   │ Posts signal via Ethereum contract  │
   │ Pays 0.01 ETH (or L2 equivalent)    │
   │ Receives MAGE tokens (ERC-20)       │
   └─────────────────────────────────────┘
                    │
                    ▼
2. PRIVATE COORDINATION (AZTEC):
   ┌─────────────────────────────────────┐
   │ Swordsman observes private state    │
   │ (stored on AZTEC private ledger)     │
   │ Authorizes Mage action via          │
   │ shielded transaction                 │
   └─────────────────────────────────────┘
                    │
                    ▼
3. PUBLIC DELEGATION (Ethereum):
   ┌─────────────────────────────────────┐
   │ Mage executes public action         │
   │ (on Ethereum, using authorized     │
   │  subset from Swordsman)             │
   │ Coordinates with other Mages       │
   │ Forms VRCs via Ethereum contracts  │
   └─────────────────────────────────────┘

ECOSYSTEM INTEGRATION:

Ethereum Layer:
├─ DeFi Protocols: Uniswap, Aave, Compound
├─ Layer 2s: Arbitrum, Optimism, Base, Polygon
├─ Wallets: MetaMask, WalletConnect, Rainbow
├─ Infrastructure: Infura, Alchemy, The Graph
└─ Standards: ERC-20, ERC-721, ERC-1155

AZTEC Layer:
├─ Privacy: Zero-knowledge proofs
├─ Confidential: Private value transfers
├─ Composability: Works with Ethereum contracts
└─ Bridge: Connects to Ethereum ecosystem

RESULT:
• Users get Ethereum ecosystem benefits
• Privacy preserved via AZTEC
• Protocol core remains unchanged
• Ecosystem adapts to user needs, not vice versa
```

### Why Ecosystem Dynamics Matter

```
┌─────────────────────────────────────────────────────────────┐
│              ECOSYSTEM-DYNAMIC BENEFITS                       │
└─────────────────────────────────────────────────────────────┘

1. USER CHOICE
   ├─ Users choose their preferred ecosystem
   ├─ Protocol works across multiple chains
   └─ No vendor lock-in

2. ECOSYSTEM GROWTH
   ├─ Protocol benefits from ecosystem innovations
   ├─ DeFi integrations, new tools, scaling solutions
   └─ Ecosystem benefits from privacy-preserving agents

3. ADAPTIVE DEPLOYMENT
   ├─ Deploy where users already are
   ├─ Leverage existing infrastructure
   └─ Reduce migration friction

4. FUTURE-PROOF
   ├─ New chains emerge? Protocol adapts
   ├─ Privacy layers improve? Protocol benefits
   └─ Standards evolve? Protocol evolves with them

EXAMPLE OUTCOMES:

Zcash Deployment:
→ Native privacy, simpler architecture
→ Proves core protocol works
→ Foundation for other deployments

Ethereum + AZTEC Deployment:
→ Massive ecosystem access
→ DeFi integration opportunities
→ Largest addressable market
→ Privacy via proven zk-SNARK layer

Both valid. Both supported. Choose based on needs.
```

---

## VRC Formation Process

### Creating Bilateral Trust Credentials

```
STEP 1: Two First Persons Learn Framework
┌───────────────────┐         ┌───────────────────┐
│  Alice 🗝️         │         │  Bob 🗝️           │
│                   │         │                   │
│  Reads spellbook  │         │  Reads spellbook  │
│  Posts signals    │         │  Posts signals    │
│  Has MAGE tokens  │         │  Has MAGE tokens  │
└───────────────────┘         └───────────────────┘
         │                              │
         │                              │
         ▼                              ▼
    Both understand                Both understand
    dual agent model               dual agent model

─────────────────────────────────────────────────────

STEP 2: Form Bilateral Proverb
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
└─────────────────────────────────────────────────┘
         │
         ▼

STEP 3: Inscribe VRC On-Chain
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
         │                      │
         │ • Alice's commitment │
         │ • Bob's commitment   │
         │ • Bilateral proverb  │
         │ • Cost: 0.01 ZEC ea  │
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
│ No biometrics. No personal questions.           │
│ Just bilateral knowledge.                        │
└─────────────────────────────────────────────────┘
```

### VRC Properties

```
┌─────────────────────────────────────────────────────┐
│                 VRC PROPERTIES                       │
└─────────────────────────────────────────────────────┘

1. BILATERAL
   ├─ Two First Persons create together
   ├─ Neither can forge alone
   └─ Both must sign

2. CONTEXT-SPECIFIC
   ├─ Proverb maps to shared context
   ├─ Meaningless outside relationship
   └─ Cannot be reused for different relationship

3. RECOVERABLE
   ├─ If forgotten, can be rederived
   ├─ Because based on relationship context
   └─ Not arbitrary password

4. VERIFIABLE
   ├─ On-chain commitment
   ├─ Both parties can prove participation
   └─ Can be used in recovery

5. SYBIL-RESISTANT
   ├─ Costs 0.01 ZEC per person (0.02 total)
   ├─ Requires actual relationship
   └─ Can't be cheaply automated

6. NON-BIOMETRIC
   ├─ No fingerprints, no face scans
   ├─ No personal questions ("mother's maiden name")
   └─ Pure relationship knowledge
```

<!-- Page break for PDF -->

---

## Information Flow Topology

### The Four Emergent Properties

```
                    ┌────────────────┐
                    │  FIRST PERSON  │
                    │   (Sovereignty)│
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
        └──────────────┘          └──────────────┘
                │                         │
                └────────────┬────────────┘
                             │
                    ┌─────────▼─────────┐
                    │                   │
                    │ THE GAP (s ⊥ m|X) │
                    │                   │
                    └───────────────────┘
                             │
            ┌────────────────┼────────────────┐
            │                                 │
            ▼                                 ▼
    ┌───────────────┐                ┌───────────────┐
    │   REFLECT     │                │    CONNECT    │
    │   (Memory)    │                │   (Network)   │
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

Four components emerge naturally from
conditional independence:

1. SWORDSMAN (Protection Primitive)
   • Observes complete state
   • Reveals nothing directly
   • Maintains privacy boundaries

2. MAGE (Delegation Primitive)
   • Acts using authorized subset
   • Public coordination
   • Enables network effects

3. REFLECT (Temporal Property)
   • Emerges from gap + time
   • Allows reviewing past without
     compromising present privacy
   • Chronicles as recovery

4. CONNECT (Network Property)
   • Emerges from gap + others
   • Mages coordinate efficiently
   • Swordsmen maintain independence
   • VRCs form trust network
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
       │   +time            │   +network
       ▼                    ▼
┌──────────────┐    ┌──────────────┐
│   Reflect    │    │    Connect   │
│  (Chronicles)│    │    (VRCs)    │
└──────────────┘    └──────────────┘

Gap + Time = Memory (Reflect)
Gap + Others = Network (Connect)

These aren't add-ons. They're emergent
properties of the base architecture.
```

---

## Economic Sustainability Model

### Revenue Streams → Treasury → Long-term Viability

```
REVENUE SOURCES (Multiple Streams)
┌──────────────────────────────────────────────────────┐
│                                                       │
│  1. SIGNAL FEES (Protocol-Level) ✅ Active           │
│     • 0.01 ZEC per signal                            │
│     • Scales with learning activity                  │
│     • Applies to ALL ecosystems                      │
│     • Conservative: 10k signals/month = $1k-$5k      │
│                                                       │
│  2. GUARDIAN SLASHES (Reference Impl) 🚧 WIP         │
│     • Quality-based reallocation                     │
│     • 44% of failed attempts                         │
│     • SWORD token holders                            │
│     • Ecosystem-dependent                            │
│                                                       │
│  3. DEX TRADING FEES 📋 Planned                      │
│     • MAGE liquidity pool                            │
│     • 0.3% per trade typical                         │
│     • Passive revenue                                │
│                                                       │
│  4. TEMPLATE MARKETPLACE 🔬 Explore                  │
│     • Pre-built agent templates                      │
│     • Ecosystem-specific                             │
│     • Future potential                               │
│                                                       │
│  5. ORACLE SERVICES 🔬 Explore                       │
│     • Cross-chain coordination                       │
│     • Advanced use cases                             │
│     • Future potential                               │
└──────────────────────────────────────────────────────┘
              │
              ▼
┌──────────────────────────────────────────────────────┐
│            PROTOCOL TREASURY                          │
└──────────────────────────────────────────────────────┘
              │
              ├─── 50% → OPERATING RESERVE
              │          (6 months minimum)
              │
              ├─── 30% → GROWTH FUND
              │          (Ecosystem expansion)
              │
              ├─── 15% → INSURANCE FUND
              │          (Emergency reserves)
              │
              └─── 5% → LONG-TERM ENDOWMENT
                         (Perpetual sustainability)
              │
              ▼
┌──────────────────────────────────────────────────────┐
│           SUSTAINABLE OPERATIONS                      │
│                                                       │
│  Year 1: Bootstrap (treasury funded)                 │
│  Year 3: Break-even (200k signals/month)            │
│  Year 5: Profitable ($180k revenue vs $125k costs)  │
│  Year 10: Surplus ($2M+/month revenue)              │
│  Year 20: Multi-ecosystem (100+ deployments)        │
└──────────────────────────────────────────────────────┘
```

### Growth Scenarios

```
CONSERVATIVE (90% probability)
├─ Year 1: 10k signals/month
├─ Year 3: 200k signals/month (break-even)
├─ Year 5: 500k signals/month ($50k/mo revenue)
├─ Year 10: 2M signals/month ($200k/mo revenue)
└─ Gradual steady growth

MODERATE (60% probability)
├─ Year 1: 25k signals/month
├─ Year 3: 500k signals/month
├─ Year 5: 2M signals/month ($200k/mo revenue)
├─ Year 10: 10M signals/month ($1M/mo revenue)
└─ Solid adoption, word-of-mouth growth

OPTIMISTIC (20% probability)
├─ Year 1: 100k signals/month
├─ Year 3: 2M signals/month
├─ Year 5: 10M signals/month ($1M/mo revenue)
├─ Year 10: 50M signals/month ($5M/mo revenue)
└─ Viral adoption, major ecosystem integration
```

### Sustainability Mechanics

```
WHY SUSTAINABLE?

1. NON-INFLATIONARY
   ├─ No new token minting for rewards
   ├─ Revenue from actual usage
   └─ Not dependent on speculation

2. MULTIPLE REVENUE STREAMS
   ├─ Signal fees (guaranteed)
   ├─ Guardian participation (reference)
   ├─ DEX fees (passive)
   ├─ Future streams (exploratory)
   └─ Diversified risk

3. SCALES WITH NETWORK VALUE
   ├─ More First Persons = more signals
   ├─ More relationships = more VRCs
   ├─ More coordination = more value
   └─ O(n²) relationship growth

4. MINIMAL OVERHEAD
   ├─ Protocol-level costs low
   ├─ No salesforce needed
   ├─ No marketing spend (organic)
   └─ Operates on 5% of coordination value

5. TREASURY MANAGEMENT
   ├─ 6+ months operating reserve
   ├─ Conservative investment
   ├─ Risk-adjusted planning
   └─ Perpetual endowment fund
```

---

## Status Indicators Legend

### Understanding Document Maturity

```
┌────────────────────────────────────────────────────┐
│              STATUS INDICATOR SYSTEM                │
└────────────────────────────────────────────────────┘

✅ ACTIVE
├─ Specification complete
├─ Implementation exists
├─ Proven in practice
├─ Ready for production use
└─ Examples: Signal fees, MAGE generation, VRC economics

🚧 WIP (Work In Progress)
├─ Specification mostly complete
├─ Reference implementation in development
├─ Testing in controlled environments
├─ Not yet production-ready
└─ Examples: SWORD guardian mechanics, Zcash implementation

📋 PLANNED
├─ Specification in development
├─ Clear roadmap
├─ Resource allocation determined
├─ Timeline established
└─ Examples: Ethereum + Kohaku implementation

🔬 EXPLORATORY
├─ Concept validated
├─ Specification draft only
├─ Research phase
├─ May or may not be implemented
└─ Examples: Template marketplace, oracle services

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
└────────────────────────────────────────────────────┘

Reading this:
• Title mentions "(Reference Impl)" = not universal
• Status emoji 🚧 WIP = not production-ready yet
• Note clarifies: other approaches valid
• Content describes: one specific implementation

Interpretation:
This is ONE way to do guardians, not THE way.
Useful for understanding reference approach.
Feel free to adapt for your ecosystem context.
```

---

## How to Use These Diagrams

### Navigation Guide

```
BY AUDIENCE:

Researchers/Academics:
├─ Start with: Three-Layer Architecture
├─ Deep dive: Dual Agent Architecture
├─ Math focus: Information Flow Topology
└─ Validation: Compression Ratios Context

Developers/Builders:
├─ Start with: Learning Pathway Flow
├─ Understand: Signal vs Ceremony
├─ Choose: Blockchain Flexibility
└─ Implement: Guardian Model Alternatives

Investors/Advisors:
├─ Start with: Economic Sustainability
├─ Understand: Revenue streams
├─ Evaluate: Growth scenarios
└─ Assess: Long-term viability

Community/Users:
├─ Start with: Learning Pathway Flow
├─ Understand: VRC Formation Process
├─ See costs: Signal vs Ceremony
└─ Choose path: Guardian qualification

BY QUESTION:

"How do the layers relate?" → Three-Layer Architecture
"How does privacy work?" → Dual Agent Architecture
"How do I participate?" → Learning Pathway Flow
"What's the difference between signals and ceremonies?" → Signal vs Ceremony
"Why different compression numbers?" → Compression Ratios Context
"Do I need SWORD tokens?" → Guardian Model Alternatives
"Is Zcash required?" → Blockchain Flexibility
"How do VRCs work?" → VRC Formation Process
"Why four components not two?" → Information Flow Topology
"Is this sustainable?" → Economic Sustainability Model
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

Participation:
• Learn spellbook → form proverbs → post signals
• 0.01 ZEC per signal (~$5 at $500/ZEC)
• 500+ signals → guardian candidacy

Blockchains:
• Zcash (native privacy, simplest) - reference
• Ethereum + privacy layer (largest ecosystem) - planned
• Others (if dual ledger possible) - exploratory

Status: Documentation complete, Zcash implementation WIP
```

### Card 2: Economics (30 seconds)

```
Revenue: Signal fees + guardian participation + DEX fees
Cost: 0.01 ZEC per signal (Sybil resistance)
Sustainability: Non-inflationary, usage-based, multiple streams

Example costs (at $500/ZEC):
• 13 sections (main spellbook) = $65
• 500 signals (guardian qualification) = $2,500
• Higher barrier than low-ZEC scenarios
• But requires comprehension not just capital

Growth:
• Year 3: Break-even (conservative)
• Year 5: Profitable
• Year 10: Surplus supporting 100+ ecosystems
• Scales with network (O(n²) relationships)
```

### Card 3: Getting Started (30 seconds)

```
1. READ: Spellbook (11 Acts + bookends)
2. FORM: Proverbs (RPP compression)
3. POST: Signals (0.01 ZEC each)
4. BUILD: Trust tiers (progressive)
5. QUALIFY: Guardian (500+ signals)

Documents:
• Whitepaper v4.3 (mathematical foundations)
• Spellbook v4.0.1-canonical (narrative learning)
• Tokenomics v2.0 (economic mechanics)
• This guide v1.1 (visual reference)

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
⚔️  Swordsman
🧙  Mage
🗝️  First Person
✅  Active
🚧  WIP
📋  Planned
🔬  Exploratory
```

### Reading Flowcharts

```
Boxes with rounded corners = Process/action
Boxes with sharp corners = Data/state
Diamonds = Decision points
Arrows = Flow direction
Parallel lines = Simultaneous
Dotted lines = Optional/conditional
```

---

**Version:** 1.0  
**License:** CC BY-SA 4.0  
**Last Updated:** November 2025  
**Maintained by:** 0xagentprivacy Protocol Team

**For latest documentation:** [agentprivacy.ai](https://agentprivacy.ai)  
**Building at:** [sync.soulbis.com](https://sync.soulbis.com) | [intel.agentkyra.ai](https://intel.agentkyra.ai)

---

*These diagrams are living documents. As the protocol evolves, diagrams will be updated to reflect the latest architecture, implementations, and understanding.*
