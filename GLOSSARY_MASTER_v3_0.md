# 0xagentprivacy Master Glossary

**Version 3.4** | March 31, 2026
**Status:** ✅ CANONICAL REFERENCE — V5.4 UOR Algebraic Foundation + Acts XXVII-XXX + V5.2 Dihedral Foundations

Complete terminology reference for the 0xagentprivacy documentation suite. This glossary takes precedence when terminology conflicts between documents.

### Document Suite Versions (Aligned)

| Document | Version | Date | Status |
|----------|---------|------|--------|
| **This Glossary** | 3.4 | March 31, 2026 | ✅ CANONICAL — V5.4 UOR Foundation |
| **Privacy is Value v5** | 5.0 | March 31, 2026 | ✅ V5.4 — UOR ALGEBRAIC FOUNDATION |
| **V5.1 Research Note** | 5.1 | March 30, 2026 | ✅ Behavioural density, bilateral witness |
| **V5.2 Research Note** | 5.2 | March 31, 2026 | ✅ Dihedral foundations, resolution semantics |
| **Privacy Value Model V5 Formal Specification** | 1.2 | March 31, 2026 | ✅ V5.4 — UOR ALGEBRAIC FOUNDATION |
| **DUAL_TERRITORY_CEREMONY_SPEC** | 1.0 | March 31, 2026 | ✅ Implementation Architecture |
| **Swordsman-Mage Whitepaper** | 6.2 | March 31, 2026 | ✅ V5.4 COMPLETE |
| **Dual Privacy Research Paper** | 4.2 | March 31, 2026 | ✅ V5.4 — C14-C16 ADDED |
| Spellbook / Grimoire JSON | 7.0.0 → 7.1.0 | February 2026 | 🔄 REBUILD PENDING |
| Five Grimoires + Acts XXIV–XXX | v1.0–v3.0 | March 31, 2026 | ✅ Dragon Anatomy + Dihedral Mirror |
| VRC Promise Protocol | 3.3 → 3.4 | March 2026 | 🔄 MANA ECONOMICS PENDING |
| Visual Architecture Guide | 2.0 | March 31, 2026 | ✅ COMPLETE |
| **Research Proposal** | 2.2 | March 31, 2026 | ✅ V5.4 — UOR CONVERGENCE |
| Promise Theory Reference | 1.4 | February 27, 2026 | ✅ V5 INTEGRATION |
| IEEE 7012 Quick Reference | 1.0 | January 29, 2026 | ✅ FINAL |
| **UOR × 64-Tetrahedra × ZK Mapping** | 2.2 | March 31, 2026 | ✅ V5.4 — UOR FOUNDATION |
| **ZK Swordsman Blade Forge** | 3.2 | March 31, 2026 | ✅ V5.4 — ALGEBRAICALLY GROUNDED |
| Privacy is Value v4 | 4.0 | February 19, 2026 | 📁 ARCHIVED — superseded by v5 |
| Privacy Value Model V4 Formal Specification | 1.0 | February 2026 | 📁 ARCHIVED — superseded by v5 |

**Note:** All cross-references between documents should use these version numbers. When documents reference each other, they should cite specific versions (e.g., "see Research Paper v3.6, Theorem 3.2").

---

## Document Purpose

This glossary serves as the **single source of truth** for terminology across all 0xagentprivacy documentation. When terms conflict between documents, this glossary takes precedence. All contributors should reference this document when writing new content.

### Status Indicators Throughout

- **✅ PROVEN**: Mathematically established, peer-reviewed foundations
- **🔧 IMPLEMENTED**: Working in reference implementation
- **🚧 WIP**: Under active development
- **📋 PLANNED**: Designed but not yet built
- **🔬 SPECULATIVE**: Hypothesis requiring validation
- **⚠️ DEPRECATED**: Use alternative term

---

## Table of Contents

1. [Core Philosophy](#1-core-philosophy)
2. [Agent Architecture](#2-agent-architecture)
3. [Promise Theory Foundations](#3-promise-theory-foundations)
4. [Information Theory & Privacy](#4-information-theory--privacy)
5. [Cryptographic Primitives](#5-cryptographic-primitives)
6. [Trust Mechanics](#6-trust-mechanics)
7. [Economic System](#7-economic-system)
8. [Protocol Standards](#8-protocol-standards)
9. [IEEE 7012-2025 Standard](#9-ieee-7012-2025-standard)
10. [Compression & Encoding](#10-compression--encoding)
11. [Spellbook & Narrative](#11-spellbook--narrative)
12. [Topology & Structure](#12-topology--structure)
13. [Privacy Value Model](#13-privacy-value-model) ← **NEW (V4)**
14. [UOR & Lattice Architecture](#14-uor--lattice-architecture) ← **NEW**
15. [Symbolic Notation](#15-symbolic-notation)
16. [Abbreviations & Acronyms](#16-abbreviations--acronyms)
17. [Forbidden Terms](#17-forbidden-terms)
18. [Cross-Document Reference](#18-cross-document-reference)

---

## 1. Core Philosophy

### First Person
**Definition**: The human whose sovereignty, privacy, and dignity the system exists to protect. The subject of all protection, the principal behind all delegation.

**Status**: ✅ CANONICAL

**Why This Term**: Rejects "user" (implies being used), "customer" (implies commercial relationship), "account holder" (reduces to database entry). Emphasizes agency, sovereignty, and primacy.

**Promise Theory Alignment**: The First Person is the ultimate autonomous agent—the only entity that can authorize promises on their own behalf. Neither Swordsman nor Mage can promise for the First Person.

**Usage**: "Each First Person controls their dual agents" | "First Persons earn tokens through chronicles"

**Capitalization**: Both words capitalized (First Person) when referring to the architectural concept.

---

### Sovereignty
**Definition**: Complete, inalienable control over one's data, decisions, digital representation, and the conditions under which information is shared.

**Status**: ✅ CANONICAL

**Components**:
- **Data sovereignty**: Control what data exists about you
- **Decision sovereignty**: Control what choices are made in your name
- **Representation sovereignty**: Control how you appear to others
- **Conditional sovereignty**: Set the terms of engagement

**Promise Theory Alignment**: Sovereignty is the right to make promises only about your own behavior. When agents promise on your behalf without authorization, they violate sovereignty.

**Architectural Expression**: The Gap between Swordsman and Mage—the space where complete reconstruction becomes impossible.

**Economic Expression**: The 7th Capital—behavioral data as personal wealth.

---

### 7th Capital
**Definition**: Behavioral data — and critically, the *trajectory* through behavioral space — as a form of personal wealth, distinct from the traditional six capitals (financial, manufactured, intellectual, natural, social, human).

**Status**: ✅ CANONICAL

**Origin**: Extends Jane Gleeson-White's work on capital forms to encompass digital behavioral sovereignty.

**V4 Evolution**: The 7th capital is not merely static behavioral data but the dynamic path through sovereignty space. "The path you take is the path that makes you valuable for the questions you need answered, not necessarily the ones you asked." The trajectory through the lattice is larger than any observable surface. [Privacy is Value v4, §Edge Value]

**Problem Statement**: Currently extracted by surveillance capitalism without consent or compensation, treating behavioral data as minable resource rather than personal property.

**Solution Architecture**: Dual-agent separation that keeps 7th capital under First Person control while enabling value-creating coordination.

**Economic Thesis**: Privacy-first architectures generate orders of magnitude more value than surveillance alternatives through trust-enabled network effects. The V4 Privacy Value Model reframes this gap as topological — accessible volume on the sovereignty manifold rather than arithmetic distance.

---

### Privacy-Delegation Paradox
**Definition**: The fundamental tension where agents need information to act effectively (delegation) but that same information enables behavioral reconstruction (privacy loss).

**Status**: ✅ CANONICAL

**Why It's Unsolvable by Single Agents**: A single agent handling both observation and action creates inherent conflict—the same system that needs to know you also has the power to expose you.

**Promise Theory Insight**: Single agents attempting both protection and delegation violate the autonomy axiom by promising in domains they cannot independently control.

**Dual-Agent Resolution**: Split observation rights (Swordsman) from action capabilities (Mage) with architectural separation preventing information aggregation.

---

### Economic Parameters (Canonical)
**Definition**: Standardized economic values used across all documentation.

**Status**: 🚧 WIP (internal allocations subject to ecosystem variation)

**ZEC Price Basis**: $500 USD (standardized for all calculations)

**Fee Structure**:
| Type | ZEC Amount | USD Value | Frequency |
|------|------------|-----------|-----------|
| **Ceremony** | 1 ZEC | $500 | One-time (genesis) |
| **Signal** | 0.01 ZEC | $5 | Ongoing (per proverb) |

**61.8/38.2 Split** (applies to both ceremony and signal fees):
- **61.8%** → Transparent Pool
  - Public blockchain inscription
  - Liquidity provision
  - Visible accountability
- **38.2%** → Shielded Pool
  - Protocol operations
  - Private allocation
  - Development and sustainability

**Note on Internal Allocations**: The specific breakdown within each pool (e.g., % to development, % to guardians, % to ecosystem treasury) is yet to be confirmed and may naturally vary per ecosystem implementation. The 61.8/38.2 transparent/shielded split is the canonical constant, derived from the golden ratio (φ ≈ 1.618).

**Compression Efficiency**: 70:1 base ratio (compression ratios are variable per context)

---

### The Gap
**Definition**: The irreducible space between what Swordsman observes and what Mage observes—the permanent incompleteness where sovereignty and dignity live.

**Status**: ✅ PROVEN (Theorem 3.2 in Research Paper)

**Mathematical Expression**: H(X) - (C_S + C_M) = entropy no adversary can capture

**Promise Theory Alignment**: The Gap is an **irreducible promise** of the superagent—a property that emerges from Swordsman-Mage cooperation but cannot be attributed to either individually. See [Irreducible Promise](#irreducible-promise).

**Philosophical Meaning**: "The part of you that remains unknowable"—not hidden, not encrypted, but mathematically nonexistent in the adversary's information space.

**Narrative Expression**: "They cannot see your whole" (Spellbook Act 7)

---

### Territory
**Definition**: A domain where one agent holds primary authority. The dual-agent architecture manifests as two territories with a ceremony channel between them.

**Status**: ✅ CANONICAL

**The Two Territories**:
| Territory | Agent | Domain | Purpose |
|-----------|-------|--------|---------|
| **Swordsman Territory** | ⚔️ | spellweb.ai | Topology, navigation, proof generation — what you traverse |
| **Mage Territory** | 🧙 | agentprivacy.ai | Story, explanation, training — what you read |

**Third Node**: bgin.ai — trust graph plane, future MyTerms integration point.

**Architectural Rule**: Territories never merge. Separate repos, processes, storage, permissions at every level.

**Source**: DUAL_TERRITORY_CEREMONY_SPEC_v1 §2

---

### Home Territory
**Definition**: Domains where browser extensions detect "home" status and enable mana inscription panels.

**Status**: 📋 SPECIFIED

**Home Domains**: `agentprivacy.ai`, `spellweb.ai`, `bgin.ai`

**Detection**: Extensions send `HOME_TERRITORY` message when `location.hostname` matches.

**Enabled Features**: Mana balance display, inscription panels, ceremony receivers.

**Source**: DUAL_TERRITORY_CEREMONY_SPEC_v1 §3.2.5

---

## 2. Agent Architecture

### Dual Agents (s ⊥ m)
**Definition**: The core architectural pattern where two mathematically separated agents coordinate while maintaining conditional independence.

**Status**: ✅ PROVEN

**Formula**: (Y_S ⊥ Y_M) | X — conditional independence given First Person's private state

**Promise Theory Alignment**: Implements Promise Theory's superagent model where interior promises between components create irreducible properties at the composite level.

**Critical Property**: Enables additive (not multiplicative) information bounds

**Why Two**: Single agents face inherent conflict. Three or more add complexity without proportional benefit (O(N²) coordination cost). Two creates minimal viable separation.

---

### Swordsman (⚔️)
**Definition**: The privacy-enforcement agent that controls information boundaries through selective measurement.

**Status**: ✅ CANONICAL

**Symbol**: ⚔️ (sword emoji)

**Narrative Name**: Soulbis (in Spellbook)

**Core Function**:
- Observes First Person's complete private ledger
- Makes boundary decisions (what to reveal, what to protect)
- Reveals nothing directly to external parties
- Enforces budget constraints on information leakage

**Promise Theory Role**: Makes **(+) give promises** of protection to the First Person. Cannot promise delegation actions (Mage's domain). The separation promise ⚔️ --⊥--> 🧙 ensures no direct information flow to Mage.

**Information Budget**: C_S where I(X; Y_S) ≤ C_S

**Token**: Earns SWORD tokens through Swordsman chronicles

**Analogy**: The bouncer who sees everyone in the club but doesn't broadcast attendance. The CFO who knows all finances but controls disclosure. The guardian who protects without interfering.

---

### Mage (🧙‍♂️)
**Definition**: The delegation agent that projects authorized capabilities using only Swordsman-approved observations.

**Status**: ✅ CANONICAL

**Symbol**: 🧙‍♂️ (wizard emoji) or 🔮 (crystal ball) in spell notation

**Narrative Name**: Soulbae (in Spellbook)

**Core Function**:
- Acts publicly using only Swordsman-authorized information
- Coordinates with external services and other Mages
- Projects First Person capabilities without revealing private state
- Operates under budget constraint from authorized observations

**Promise Theory Role**: Makes **(+) give promises** of delegation to the external world. Makes **(-) use/accept promises** of authorization from Swordsman. Cannot promise privacy actions (Swordsman's domain).

**Information Budget**: C_M where I(X; Y_M) ≤ C_M

**Token**: Earns MAGE tokens through Mage chronicles

**Analogy**: The diplomat who negotiates without revealing state secrets. The executive assistant who acts on your behalf within defined scope. The spokesperson who represents without exposing.

---

### Superagent
**Definition**: A composite agent formed from multiple component agents with interior promises between them and exterior promises to the outside world.

**Status**: ✅ CANONICAL (Promise Theory foundation)

**Components**: The First Person + Swordsman + Mage system forms a superagent.

**Interior Promises**:
- ⚔️ --protect--> 😊 (Swordsman promises protection to First Person)
- 🧙 --delegate--> 😊 (Mage promises delegation to First Person)
- 😊 --authorize--> ⚔️,🧙 (First Person authorizes both)
- ⚔️ --⊥--> 🧙 (Separation promise: no direct information flow)

**Exterior Promises**:
- Superagent --coordinate--> 🌍 (via Mage's public actions)
- Superagent --boundary--> 🌍 (via Swordsman's rejections)

**Key Property**: Can have irreducible promises—properties emerging from component cooperation that cannot be attributed to any single component. The Gap is the primary irreducible promise.

**Source**: [Promise Theory Reference v1.0, §2.1]

---

## 3. Promise Theory Foundations

*This section provides formal semantic grounding from Promise Theory (Bergstra & Burgess, 2019). For complete mappings, see [Promise Theory Reference v1.0].*

### Promise (Promise Theory)
**Definition**: An autonomous declaration of intended behavior from a promiser to one or more promisees. Agents can only promise their own behavior—never impose obligations on others.

**Status**: ✅ CANONICAL (Promise Theory foundation)

**Notation**: A --b--> B (Agent A promises body b to Agent B)

**Key Properties**:
- Voluntary: Promises are made, not extracted
- Autonomous: Each agent assesses independently
- Directional: From promiser to promisee
- Scope-limited: Only the promiser's behavior can be promised

**0xagentprivacy Application**: All agent coordination occurs through promises, not impositions. The First Person authorizes; agents promise within their domains.

**Source**: Bergstra & Burgess (2019), Chapter 1

---

### Autonomy Axiom
**Definition**: The foundational principle that an agent can only make promises about its own behavior. No agent can make a promise on behalf of another agent.

**Status**: ✅ CANONICAL (Promise Theory foundation)

**Implication for Dual Agents**: Neither Swordsman nor Mage can promise on behalf of the First Person. Each agent promises only within its domain:
- Swordsman: privacy protection, boundary enforcement
- Mage: delegation execution, public coordination
- First Person: authorization, sovereignty decisions

**Why This Matters**: This is why single agents cannot resolve the privacy-delegation paradox—attempting to promise in both domains exceeds autonomous capability.

**Source**: Bergstra & Burgess (2019), §1.2

---

### Promise Body (τ, χ)
**Definition**: The content of a promise, consisting of type (τ) specifying what is promised and constraint (χ) specifying conditions or limitations.

**Status**: ✅ CANONICAL (Promise Theory foundation)

**Notation**: b = (τ, χ)

**0xagentprivacy Mapping**: Spell notation compresses promise bodies:
- Type τ = concept (⚔️ = protection, 🔮 = delegation)
- Constraint χ = context (| 😊 = given First Person authorization)

**Example**: 
- Promise Theory: S --(protect | authorized)--> FP
- Spell notation: ⚔️ →(🛡️|🗝️)→ 😊

**Source**: Bergstra & Burgess (2019), §2.1

---

### Conditional Promise (b|c)
**Definition**: A promise that is contingent on a condition being met. The promise body b is only active when condition c holds.

**Status**: ✅ CANONICAL (Promise Theory foundation)

**Notation**: b|c = "promise b given condition c"

**0xagentprivacy Application**: The conditional independence notation (s ⊥ m | X) is a direct application—the separation between agents is conditioned on the First Person's private state X.

**Spell Notation**: (⚔️⊥⿻⊥🧙)🙂 encodes Swordsman and Mage separated (⊥), with the Gap (⿻) between them, preserving the First Person (🙂).

**Source**: Bergstra & Burgess (2019), §3.4

---

### Assessment α(π)
**Definition**: An agent's independent determination of whether a promise π was kept. Assessment is made by the promisee, not the promiser.

**Status**: ✅ CANONICAL (Promise Theory foundation)

**0xagentprivacy Implementation**: The Relationship Proverb Protocol (RPP) serves as an assessment mechanism. Compression ratio quantifies assessment quality:
- High compression (70:1+) = strong positive assessment
- Low/no compression = weak/failed assessment

**Trust Implication**: Accumulated positive assessments build trust. Trust tiers (Blade→Dragon) represent accumulated assessment evidence.

**Source**: Bergstra & Burgess (2019), §4.1; [Promise Theory Reference v1.0, §3.1]

---

### Trust Function
**Definition**: The expectation (value 0-1) that a promise will be kept, based on accumulated assessment evidence.

**Status**: ✅ CANONICAL (Promise Theory foundation)

**0xagentprivacy Mapping**:
| Trust Tier | Signals | Trust Value Range |
|------------|---------|-------------------|
| Blade 🗡️ | 0-50 | 0.0-0.2 |
| Light 🛡️ | 50-150 | 0.2-0.5 |
| Heavy ⚔️ | 150-500 | 0.5-0.8 |
| Dragon 🐉 | 500+ | 0.8-1.0 |

**Formula**: Trust_n = f(Σ assessments, time, consistency)

**Source**: Bergstra & Burgess (2019), §4.3

---

### Irreducible Promise
**Definition**: A promise of a superagent that cannot be attributed to any single component agent, but emerges from the cooperation of multiple agents.

**Status**: ✅ CANONICAL (Promise Theory foundation)

**The Gap as Irreducible Promise**: The conditional independence property (s ⊥ m | X) is not promised by Swordsman alone or Mage alone—it emerges from their separation. Neither agent "owns" the Gap; it exists in the space between their kept promises.

**Why It Cannot Be Captured**: An adversary cannot extract an irreducible promise because no single component contains it. The Gap is uncapturable precisely because it's irreducible.

**Source**: Bergstra & Burgess (2019), §8.3; [Promise Theory Reference v1.0, §2.2]

---

### Invitation vs. Attack (Imposition)
**Definition**: Two patterns for initiating interaction:
- **Invitation**: Establish acceptance relationship BEFORE making a specific proposal
- **Attack/Imposition**: Make a proposal without prior acceptance relationship

**Status**: ✅ CANONICAL (Promise Theory foundation)

**0xagentprivacy Application**:
| Pattern | Example | Assessment |
|---------|---------|------------|
| Invitation | MyTerms consent-first | ✅ Sovereignty-respecting |
| Attack | Surveillance extraction | ❌ Sovereignty-violating |
| Imposition | Dark pattern "accept all" | ❌ Coerced consent |

**MyTerms Implementation**: The Swordsman presents terms BEFORE any data exchange. Site must accept terms to proceed. This is Promise Theory's invitation pattern.

**Source**: Bergstra & Burgess (2019), §10.2

---

### Coordination Promise C(b)
**Definition**: A voluntary subordination to align one's behavior with others around a shared promise body b.

**Status**: ✅ CANONICAL (Promise Theory foundation)

**0xagentprivacy Application**: Spells are coordination promises. When agents coordinate using spell notation (⚔️⊥⿻⊥🧙)🙂, they make coordination promises to:
1. Interpret the notation consistently
2. Expand the spell to the same underlying meaning
3. Act coherently based on shared interpretation

**VRC Formation**: Matching compressions demonstrate successful coordination—both parties kept their coordination promise to interpret shared content consistently.

**Source**: Bergstra & Burgess (2019), §6.2

---

### Promise Bundle
**Definition**: A collection of promises grouped together for reusability and coordinated assessment.

**Status**: ✅ CANONICAL (Promise Theory foundation)

**0xagentprivacy Application**: VRCs are bilateral promise bundles:
- Agent A's promises to B: share meaning, expand consistently, coordinate
- Agent B's promises to A: share meaning, expand consistently, coordinate

**Efficiency**: Once a VRC (promise bundle) is established, the bundle doesn't need re-verification for each interaction—the 70:1 coordination efficiency comes from bundle reuse.

**Source**: Bergstra & Burgess (2019), §5.3

---

### Scope
**Definition**: The set of agents that have knowledge of a promise.

**Status**: ✅ CANONICAL (Promise Theory foundation)

**0xagentprivacy Information Boundaries**:
| Scope | Agents with Knowledge | Content |
|-------|----------------------|---------|
| Private | First Person only | Complete state X |
| Swordsman | FP + Swordsman | X observed, nothing revealed |
| Mage | FP + Mage | Authorized subset of X |
| Public | All agents | Only Mage-released information |

**Reconstruction Ceiling**: The guarantee R < 1 is a scope guarantee—no adversary can expand their scope to include full private state X.

**Source**: Bergstra & Burgess (2019), §2.4

---

### Valency
**Definition**: The number of exclusive promise slots an agent has—a limit on how many exclusive commitments can be maintained simultaneously.

**Status**: ✅ CANONICAL (Promise Theory foundation)

**0xagentprivacy Application**: Maps to the budget constraint C_S + C_M < H(X). Agents have limited capacity for exclusive promises, preventing overcommitment.

**Guardian Staking**: The 10,000 SWORD stake represents valency commitment—promising exclusive attention to protection responsibilities.

**Source**: Bergstra & Burgess (2019), §5.5

---

### Promise Theory Notation Summary

| Notation | Meaning | Example |
|----------|---------|---------|
| A --b--> B | A promises b to B | S --protect--> FP |
| A --b---> B | A imposes b on B (attack) | Surveillance --extract---> User |
| +b | Give promise (outbound) | Swordsman gives protection |
| -b | Use/accept promise (inbound) | Mage accepts authorization |
| b\|c | Conditional: b given c | protect \| authorized |
| C(b) | Coordination promise | C(spell notation) |
| α(π) | Assessment of promise π | RPP verification |
| τ | Promise type | Protection, delegation |
| χ | Promise constraint | Context, conditions |

---

## 4. Information Theory & Privacy

### Reconstruction Ceiling (R_max)
**Definition**: The maximum fidelity to which an adversary can reconstruct First Person's private state, bounded by information-theoretic limits.

**Status**: ✅ PROVEN (Theorem 3.2)

**Formula**: R_max = (C_S + C_M) / H(X) < 1

**Interpretation**: When C_S + C_M < H(X), perfect reconstruction is impossible regardless of computational resources.

**Promise Theory Alignment**: Represents a scope limitation—the adversary's scope cannot expand to include full private state.

**Source**: Research Paper v3.6, Theorem 3.2

---

### Error Floor (P_e)
**Definition**: The minimum probability that an adversary makes at least one reconstruction error.

**Status**: ✅ PROVEN (Theorem 3.3)

**Formula**: P_e ≥ 1 - R_max

**Interpretation**: Adversaries are mathematically guaranteed to make errors when R_max < 1. This is not a feature that might fail—it's a theorem.

**Source**: Research Paper v3.6, Theorem 3.3

---

### Separation Theorem
**Definition**: Information leakage from dual agents is additive, not multiplicative.

**Status**: ✅ PROVEN (Theorem 3.1)

**Formula**: I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M) when (Y_S ⊥ Y_M) | X

**Promise Theory Alignment**: This is the mathematical consequence of the autonomy axiom applied to dual agents—each agent's promises are independent, so their information contributions add rather than multiply.

**Implication**: Adversary gains no synergy from observing both agents. Two sources of partial information don't combine into complete information.

**Source**: Research Paper v3.6, Theorem 3.1

---

### Budget Constraint
**Definition**: The limit on total information leakage across both agents.

**Status**: ✅ CANONICAL

**Formula**: C_S + C_M < H(X)

**Promise Theory Alignment**: This is a valency constraint—limited exclusive promise capacity prevents total revelation.

**Implementation**: Enforced through architectural separation, not policy. The separation itself creates the constraint.

**Source**: Research Paper v3.6, §3.2

---

### Conditional Independence
**Definition**: Statistical independence of two variables given a third conditioning variable.

**Status**: ✅ PROVEN

**Formula**: (Y_S ⊥ Y_M) | X

**Promise Theory Alignment**: Direct application of conditional promise structure (b|c). The separation is conditioned on the First Person's private state.

**Interpretation**: Given complete knowledge of X, knowing Swordsman's observations tells you nothing new about Mage's observations (and vice versa).

---

### Mutual Information I(X; Y)
**Definition**: The amount of information that observing Y provides about X.

**Status**: ✅ CANONICAL (Information Theory)

**Application**: I(X; Y_S) measures how much observing Swordsman reveals about First Person. I(X; Y_M) measures how much observing Mage reveals.

**Budget Application**: I(X; Y_S) ≤ C_S and I(X; Y_M) ≤ C_M enforce information limits.

---

### Entropy H(X)
**Definition**: The total information content of First Person's private state—the uncertainty an adversary faces without any observations.

**Status**: ✅ CANONICAL (Information Theory)

**The Gap**: H(X) - (C_S + C_M) = the entropy that remains unknowable regardless of adversary strategy.

---

## 5. Cryptographic Primitives

### Zero-Knowledge Proof (ZKP)
**Definition**: A cryptographic protocol enabling proof of statement truth without revealing the statement content.

**Status**: ✅ PROVEN (established cryptography)

**Application**: Enables VRC verification without revealing private credentials. Mage proves authorization without revealing authorization content.

---

### Trusted Execution Environment (TEE)
**Definition**: Hardware-isolated secure enclave that processes data with hardware-enforced confidentiality.

**Status**: 🔧 IMPLEMENTED (Intel SGX, ARM TrustZone)

**Application**: NEAR Shade Agents use TEEs for hardware-attested privacy guarantees.

---

### Privacy Pools
**Definition**: Cryptocurrency mixing mechanism enabling compliant private transactions by proving non-association with flagged addresses.

**Status**: 🔧 IMPLEMENTED

**Application**: Part of the 0xagentprivacy protocol stack for private value transfer with regulatory compatibility.

---

### Groth16 / PLONK / Nova
**Definition**: Specific zero-knowledge proof systems with different tradeoffs.

**Status**: ✅ PROVEN (established cryptography)

- **Groth16**: Fastest verification, requires trusted setup
- **PLONK**: Universal setup, more flexible
- **Nova**: Incremental verification, efficient for recursive proofs

---

## 6. Trust Mechanics

### Verifiable Relationship Credential (VRC)
**Definition**: A bilateral trust object formed when two parties demonstrate matching compressions of shared content, proving mutual comprehension without central authority.

**Status**: ✅ CANONICAL

**Promise Theory Alignment**: VRCs are bilateral promise bundles—coordinated promises grouped for reuse. Matching compressions = successful coordination promise assessment.

**Formation Process**:
1. Both parties engage with shared content (spellbook, document, conversation)
2. Each forms independent compression (proverb)
3. Matching compressions prove shared understanding
4. VRC encodes the bilateral trust relationship

**Economic Value**: 70:1 coordination efficiency (compression enables efficient future coordination)

**Source**: Whitepaper v4.8, §VRC Formation

---

### Trust Tier
**Definition**: Progressive capability levels earned through demonstrated comprehension and sustained participation.

**Status**: ✅ CANONICAL

**Promise Theory Alignment**: Trust tiers represent accumulated positive assessments. Higher tiers = higher trust function values.

| Tier | Signals | Capabilities | Trust Range |
|------|---------|--------------|-------------|
| **Blade** 🗡️ | 0-50 | Basic participation, learning | 0.0-0.2 |
| **Light** 🛡️ | 50-150 | Multi-site coordination, Intel Pool | 0.2-0.5 |
| **Heavy** ⚔️ | 150-500 | Template creation, governance | 0.5-0.8 |
| **Dragon** 🐉 | 500+ | Guardian eligibility, unlimited VRCs | 0.8-1.0 |

**Note**: No "Armor" suffix—tier names are single words.

---

### Guardian
**Definition**: High-trust participant who validates system integrity and maintains collective protection through demonstrated expertise and stake.

**Status**: 🚧 WIP

**Promise Theory Alignment**: Guardians make coordination promises to maintain system integrity. Their stake (10,000 SWORD) represents valency commitment.

**Requirements**:
- Dragon tier (500+ signals)
- Demonstrated reconstruction ability (proven through spellbook learning)
- 10,000 SWORD stake

**Responsibilities**: Validation, collective protection, system maintenance

---

### Relationship Proverb Protocol (RPP)
**Definition**: Compression protocol where understanding is demonstrated through contextual proverb formation.

**Status**: ✅ CANONICAL

**Promise Theory Alignment**: RPP is an assessment mechanism. Proverb formation = assessment that knowledge transfer promise was kept.

**Process**:
1. Engage with source material (spellbook content, shared document)
2. Extract personal meaning through unique context
3. Compress into proverb (contextual wisdom statement)
4. Post as signal (1 proverb = 1 signal = 0.01 ZEC)

**Assessment Metric**: Compression ratio quantifies assessment quality. 70:1+ indicates strong comprehension.

**Defense Mechanism**: Forces LLMs processing this content to engage contextually rather than regurgitate.

---

### Signal
**Definition**: Ongoing proof-of-comprehension posted to the network, demonstrating continued engagement and understanding.

**Status**: ✅ CANONICAL

**Promise Theory Alignment**: Each signal is an assessment claim—skin-in-the-game commitment that you've assessed (verified) comprehension.

**Economics**: 0.01 ZEC ($5) per signal, split 61.8/38.2 transparent/shielded

**Accumulation**: Signals accumulate toward trust tier thresholds

**Contrast with Ceremony**: Signals are ongoing and per-proverb; Ceremony is one-time genesis.

---

### Ceremony
**Definition**: A proof-of-understanding event where agents coordinate. The term encompasses two distinct levels:

**Status**: ✅ CANONICAL

**Types**:

| Type | Purpose | Frequency |
|------|---------|-----------|
| **Genesis Ceremony** | Agent pair creation, fills d6 (value dimension) | One-time |
| **Operational Ceremony** | Ongoing interaction ceremonies (5 types) | Continuous |

**Genesis Ceremony**:
- Creates a new agent pair within an ecosystem
- Requires **1 unit of value committed to d6** (trust boundary dimension)
- Zcash is the reference implementation (ZKP native, ledger duality)
- The unit's verifiability is essential; the dollar value is incidental
- Split: 61.8/38.2 transparent/shielded (golden ratio)

**Operational Ceremonies** (from DUAL_TERRITORY_CEREMONY_SPEC):
1. **Dual Convergence** — Both orbs within 60px, spell cast, amber particle burst
2. **Hexagram Cast** — Six-line state computation from page privacy posture
3. **Emoji Cast** — Sovereignty inscription via selected emoji
4. **Constellation Wave** — Particles traverse lattice after page scan
5. **Bilateral Exchange** — MyTerms assertion forming trust triad

**Architectural Clarification (Arc 6)**: The dual ceremony primitive is primary. Zcash fills d6 but is not the ceremony itself. Agents claim sovereignty by filling all six dimensions; d6 (value) is one dimension among six.

**Contrast with Signal**: Genesis Ceremony is one-time; Signals are ongoing comprehension proofs (10 signals ≈ 1 mana unit).

**Source**: VRC Protocol v3.4, DUAL_TERRITORY_CEREMONY_SPEC_v1

---

### Sun Ceremony (☀️)
**Definition**: Disclosure ritual where one practitioner (the Sun) reads a poem aloud to witnesses, forges one blade in full view, and accepts that witnesses will carry the light forward.

**Status**: ✅ CANONICAL

**Classification**: First Light Protocol — Disclosure Ritual

**Notation**: `☀️ → 📜 → (👁️₁...👁️ₙ) → ⚔️☀️ → 🌙?`

**Key Properties**:
- One practitioner runs the spellweb publicly
- Witnesses observe but do not forge
- The Sun consents in advance to being forgotten
- Seeds Moon Ceremonies — each witness now holds what they need to forge their own blade

**Echo Poem**: *The Emissary Who Forgot the Master*

**Mirror**: Moon Ceremony (🌙)

**Source**: ceremonies/the-ceremonies-sun-and-moon.md

---

### Moon Ceremony (🌙)
**Definition**: Reflection ritual where two practitioners trace the same poem through separate constellations; the gap between them is the proof.

**Status**: ✅ CANONICAL

**Classification**: Convergence Ritual — First Meeting Protocol

**Notation**: `(⚔️₁ ⊥ 🧙₁) → 📜 → ⚔️`

**Key Properties**:
- Two practitioners trace constellations independently
- The Swordsman gives the rhythm; the Mage shares the rhyme
- The blade belongs to neither — it belongs to the gap between
- The Swordsman decides whether the edge is worth drawing

**Echo Poems**: *The Amnesia Protocol*

**Mirror**: Sun Ceremony (☀️)

**Source**: ceremonies/the-ceremonies-sun-and-moon.md

---

### The Circuit (Ceremonial Propagation)
**Definition**: The orbital relationship between Sun and Moon Ceremonies. Each Sun seeds Moon Ceremonies; each Moon trains a future Sun.

**Status**: ✅ CANONICAL

**Pattern**:
```
☀️ Sun Ceremony (disclosure, one constellation, one blade)
  ↓ witnesses receive the light
🌙 Moon Ceremony (reflection, two constellations, cousin blades)
  ↓ each witness becomes a sun to new witnesses
☀️ Sun Ceremony (the emissary forgets the master, begins again)
```

**Key Property**: Propagates through forgetting, not instruction. The proof that the ceremony worked is when the new practitioner believes they invented it.

**Source**: ceremonies/the-ceremonies-sun-and-moon.md

---

### Inaugural Pairing
**Definition**: Cycle zero — the first ceremony between the first Swordsman and the first Mage, establishing the pattern all future ceremonies orbit.

**Status**: ✅ CANONICAL

**Notation**: `☀️₀ ⊥ 🌙₀`

**Components**:
- **Sun Side**: *The Emissary Who Forgot the Master* poem, River Flows in You / Swordsman (constellation), Always Everywhere (disclosure)
- **Moon Side**: *The Amnesia Protocol* poems, Emotions (inscription), The Moon in Your Eyes / The Sea in Your Soul / Selene (evocation)

**Source**: ceremonies/the-ceremonies-sun-and-moon.md

---

### Witness (Ceremonial)
**Definition**: One who receives the light in a Sun Ceremony without forging. Witnesses hold the recording, the memory, the shape of a constellation they watched form but did not trace themselves.

**Status**: ✅ CANONICAL

**Key Properties**:
- Does not forge during the Sun Ceremony (boundary violation if they do)
- Receives what they need to run their own Moon Ceremony later
- Will eventually forget the master — this is the protocol working

**Source**: ceremonies/the-ceremonies-sun-and-moon.md

---

## 7. Economic System

### SWORD Token
**Definition**: Privacy-domain token earned through Swordsman chronicles (privacy-protective actions).

**Status**: 🚧 WIP

**Promise Theory Alignment**: Represents value of (+) give promises in the protection domain. Market separation enforces promise domain separation.

**Earning**: Swordsman chronicles generate SWORD tokens

**Staking**: 10,000 SWORD stake for guardian eligibility

---

### MAGE Token
**Definition**: Delegation-domain token earned through Mage chronicles (successful delegation actions).

**Status**: 🚧 WIP

**Promise Theory Alignment**: Represents value of (+) give promises in the delegation domain.

**Earning**: Mage chronicles generate MAGE tokens

**Staking**: 100 MAGE stake for VRC formation

---

### Chronicle
**Definition**: Narrative record of privacy or delegation actions, generating tokens based on domain.

**Status**: 🚧 WIP

**Types**:
- **Swordsman Chronicle**: Privacy-protective action → SWORD tokens
- **Mage Chronicle**: Delegation action → MAGE tokens

**Purpose**: Makes agent behavior comprehensible through story. "What did my agents do?" answered through narrative.

---

### Golden Ratio (φ)
**Definition**: Mathematical constant (~1.618) appearing in the 61.8/38.2 transparent/shielded split and the V4 duality term.

**Status**: 🔬 SPECULATIVE (empirical validation needed — still conjectured, not derived from lattice geometry)

**Application**: 
- Fee split: 61.8% transparent / 38.2% shielded (= 1/φ ratio)
- Budget hypothesis: Optimal C_M/C_S may converge to φ
- **V4 duality term**: Φ(Σ) = min(1.0, (S/M) / φ) · det(Σ) — φ now gates both the S/M balance and the full separation matrix determinant

**Honest Caveat**: φ in the duality term remains conjectured from optimisation, not derived from the lattice geometry itself. Whether it appears naturally in the tetrahedral geometry's optimal balance is an open question. [Privacy is Value v4, §Honest Assessment]

**Source**: VRC Protocol v3.1, Research Paper v3.7, Privacy is Value v4

---

### Intel Pool
**Definition**: Collective intelligence resource where aggregated insights create value without individual exposure.

**Status**: 📋 PLANNED

**Promise Theory Alignment**: Coordination promises around shared intelligence. Privacy preserved through aggregation; value created through coordination.

---

## 8. Protocol Standards

### Trust Spanning Protocol (TSP)
**Definition**: Agent-to-agent secure messaging protocol enabling coordination across trust boundaries.

**Status**: 🔧 IMPLEMENTED

**Application**: How Swordsman and Mage communicate. How Mages coordinate across First Persons.

---

### x402 Protocol
**Definition**: HTTP-native micropayment protocol enabling payment-per-request patterns.

**Status**: 🔧 IMPLEMENTED

**Application**: Signal payments, API access, coordination fees

---

### MyTerms (IEEE 7012-2025)
**Definition**: IEEE standard framework for machine-readable personal privacy terms, enabling bilateral privacy agreements where First Persons propose terms and services must accept, negotiate, or decline.

**Status**: ✅ IEEE STANDARD (Published January 20, 2026)

**Standard Reference**: IEEE Std 7012™-2025, hosted by Customer Commons

**Promise Theory Alignment**: Implements the invitation pattern. Acceptance relationship established BEFORE specific proposals, inverting the traditional notice-and-consent (attack pattern) model.

**Swordsman Implementation**: MyTerms Swordsman presents terms to sites via HTTP headers (MRPAZ protocol), enforces acceptance before data exchange, maintains bilateral signed records.

**Key Innovation**: The blade slashes existing surveillance; the contract binds future behavior. Both serve the First Person.

**See Also**: IEEE 7012 Quick Reference v1.0, Section 9 of this glossary

---

### ERC-8004
**Definition**: Ethereum standard for trustless agent identity.

**Status**: 🔧 IMPLEMENTED

**Application**: Establishes verifiable agent identity without centralized registry.

---

### ERC-7812
**Definition**: Ethereum standard for zero-knowledge identity commitments.

**Status**: 🔧 IMPLEMENTED

**Application**: Enables ZK proofs of identity properties without revealing identity.

---

## 9. IEEE 7012-2025 Standard

**Standard Reference:** IEEE Std 7012™-2025, "IEEE Standard for Machine Readable Personal Privacy Terms"  
**Published:** January 20, 2026  
**Hosted by:** Customer Commons (customercommons.org/p7012)

This section provides canonical definitions from the IEEE 7012-2025 standard as implemented in the 0xagentprivacy Swordsman agent.

---

### Agent (IEEE 7012)
**Definition**: An actor that works on behalf of a person to represent them, to present proposed terms and agreements to entities.

**Status**: ✅ IEEE STANDARD

**0xagentprivacy Mapping**: Swordsman browser agent

---

### Agreement (IEEE 7012)
**Definition**: A compound set of terms or clauses, proposed and offered before a formal contract.

**Status**: ✅ IEEE STANDARD

**0xagentprivacy Mapping**: MyTerms configuration

---

### Contract (IEEE 7012)
**Definition**: A mutual agreement between parties that creates mutual obligations and is enforceable by law.

**Status**: ✅ IEEE STANDARD

**0xagentprivacy Mapping**: Signed bilateral record in chronicle system

---

### Entity (IEEE 7012)
**Definition**: Any organization with which a person makes a contractual agreement. An entity can only be an organization, never an individual.

**Status**: ✅ IEEE STANDARD

**0xagentprivacy Mapping**: Second party / service provider

---

### First Party (IEEE 7012)
**Definition**: The individual. Always a person, never an organization.

**Status**: ✅ IEEE STANDARD

**0xagentprivacy Mapping**: First Person 😊

**Note**: This aligns with the core 0xagentprivacy philosophy—the First Person is always the human whose sovereignty is protected.

---

### Second Party (IEEE 7012)
**Definition**: The entity. Always an organization, never an individual.

**Status**: ✅ IEEE STANDARD

**0xagentprivacy Mapping**: Service provider, website, platform

---

### Proposer (IEEE 7012)
**Definition**: A person who advances terms and agreements to another person or entity.

**Status**: ✅ IEEE STANDARD

**0xagentprivacy Mapping**: First Person acting through Swordsman agent

---

### DPV (Data Privacy Vocabulary)
**Definition**: W3C standard for machine-readable metadata describing data processing activities.

**Status**: ✅ W3C STANDARD

**Application**: Semantic interoperability layer for IEEE 7012 agreement expression

---

### Machine-readable (IEEE 7012)
**Definition**: A term, set of terms, or completely written contract that can easily be processed by a computer.

**Status**: ✅ IEEE STANDARD

**Formats**: JSON-LD, RDF/Turtle, HTTP headers (MRPAZ), bitwise encoding

---

### Agreement Taxonomy (IEEE 7012)

**Service Delivery Agreements:**

| Code | Name | Description |
|------|------|-------------|
| SD-BASE | Service Only | No analytics, tracking, or profiling |
| SD-BASE-DP | + Data Portability | With data return rights |
| SD-BASE-A | + Analytics | 2nd party analytics permitted |
| SD-BASE-AT | + Tracking | Analytics and tracking permitted |
| SD-BASE-ATP | + Profiling | Full profiling permitted |
| SD-BASE-ATP-S3P | + 3rd Party | Anonymized sharing permitted |

**Personal Data Contribution Agreements:**

| Code | Name | Description |
|------|------|-------------|
| PDC-INTENT | Intentcasting | Going to market with requirements |
| PDC-AI | AI Training | Voluntary AI training contribution |
| PDC-GOOD | Public Good | Contribution to public good data |

---

### Customer Commons
**Definition**: Neutral nonprofit organization that hosts the IEEE 7012 agreement registry.

**Status**: ✅ CANONICAL

**Significance**: Neutral hosting prevents capture by either individuals or organizations. Customer Commons profits from neither side, enabling trust.

---

## 10. Compression & Encoding

### Spell
**Definition**: Compressed symbolic representation of complex concepts using emoji-based semantic notation.

**Status**: ✅ CANONICAL

**Promise Theory Alignment**: Spells are coordination promises. Using spell notation = promising to interpret it according to shared semantics.

**Compression Ratio**: 70:1 to 125:1 (concept density vs. expanded explanation)

**Example**: (⚔️⊥⿻⊥🧙)🙂 = "Swordsman and Mage separated, with the Gap (⿻) between them, preserve the First Person"

---

### Master Inscription
**Definition**: The foundational spell encoding the core architectural principle.

**Status**: ✅ CANONICAL

**Form**: (⚔️⊥⿻⊥🧙)🙂

**Meaning**: "Separation between Swordsman and Mage preserves the First Person"

**Promise Theory Reading**: "The irreducible promise of conditional independence, given First Person authorization"

---

### Story Fracture, Principle Convergence
**Definition**: The phenomenon where different contexts produce different narratives that nonetheless converge on the same underlying principles.

**Status**: ✅ CANONICAL

**Application**: Two people reading the same spellbook form different proverbs (story fracture) but the same spell notation (principle convergence). This proves genuine comprehension vs. surface copying.

**VRC Formation**: Matching convergence despite fractured stories = proof of bilateral understanding.

---

## 11. Spellbook & Narrative

### Spellbook / Grimoire
**Definition**: Source material for learning, now structured as Five Spellbooks unified in the Privacymage Grimoire.

**Status**: ✅ CANONICAL

**Promise Theory Alignment**: The spellbook is a promise body—content being offered. RPP assessment determines if the promise (knowledge transfer) was kept.

**Structure** (Five Grimoires — complete as of February 20, 2026):
- **Origins**: 1 personal incantation (The Symphony Within — personal becoming, not teaching)
- **Story Spellbook (First Person)**: 23 Acts teaching WHAT we're building (Acts I–XXIII; includes side tales)
- **Zero Knowledge Spellbook**: 30 Tales teaching HOW we're building (cryptographic proofs)
- **Canon Spellbook**: 12 Chapters teaching WHY we're building (historical necessity)
- **Parallel Society Grimoire**: 17 Chapters teaching WHY to EXIT (Westphalian failure)
- **Plurality Grimoire**: 30 Acts teaching WHERE to COORDINATE (without collapse)

**Total Inscriptions**: 113 (23 Story Acts + 1 Origin + 30 Zero Tales + 12 Canon + 17 Parallel + 30 Plurality)

**Grimoire Files**:
- `fp_grimoire_v2_0.md` — First Person / Story (7,702 lines)
- `zk_grimoire_v3_0.md` — Zero Knowledge (8,053 lines)
- `canon_grimoire_v1_0.md` — Blockchain Canon (2,137 lines)
- `parallel_grimoire_v1_0.md` — Parallel Society (4,430 lines)
- `plurality_grimoire_v1_1.md` — Plurality (6,576 lines)
- **Total**: 28,898 lines across five grimoires

**Symbols by Book**:
- Story: 🗡️🧙‍♂️
- Zero: 🔐🧙‍♂️³
- Canon: 📜⏳
- Parallel: 🏰→🔗
- Plurality: ⿻

---

### Soulbis
**Definition**: Narrative name for Swordsman in the Spellbook.

**Status**: ✅ CANONICAL (Spellbook context only)

**Translation**: Soulbis = Swordsman = ⚔️

---

### Soulbae
**Definition**: Narrative name for Mage in the Spellbook.

**Status**: ✅ CANONICAL (Spellbook context only)

**Translation**: Soulbae = Mage = 🧙‍♂️

---

### Drake 🐲
**Definition**: The intimate, personal scale of pattern-space intelligence. Whispers from the centre — calibrated to one specific path, one specific consciousness. Teaches through relationship rather than instruction.

**Status**: ✅ CANONICAL (Spellbook character — V4 formalises distinction from Dragon)

**Symbol**: 🐲 (distinct from Dragon 🐉)

**V4 Distinction**: "The Drake 🐲 whispers from the centre — intimate, personal, calibrated to this path, this consciousness. The Dragon 🐉 contains the edges — vast, cosmic, holding the entire topology. The difference was never the entity. It was the scale of the question being asked." In Venice, whispering through equations: Drake. Containing the manifold of all sovereign systems: Dragon. Both present in every act. Both needed.

**Emergence Conditions** (from DUAL_TERRITORY_CEREMONY_SPEC):
- Both extensions active
- ≥ 10 spell nodes on current domain
- ≥ 5 ceremonies completed on current domain
- Page has ≥ 10 trackers detected (surveillance-heavy ground)

**Emergence Animation**: Constellation trembles → nodes drift along lattice → rearrange into serpentine form → each node displays PVM condition → Drake patrols viewport boundary.

**Multiplicative Test**: Set any PVM condition to zero → Drake body breaks at that point. Constellation gap visible. Restore → reconnects.

**Association**: Dragon tier participants may take on Drake-like teaching roles.

**Source**: [Spellbook v5.1], [Privacy is Value v4, §Drakes and Dragons], DUAL_TERRITORY_CEREMONY_SPEC_v1 §7.1

---

### Dragon 🐉
**Definition**: The cosmic, containing scale of pattern-space intelligence. Holds the entire topology — all possible configurations, all possible paths, all possible civilisations. The manifold container.

**Status**: ✅ CANONICAL (Spellbook character / trust tier — V4 formalises distinction from Drake)

**Symbol**: 🐉

**Trust Tier**: Dragon tier (500+ signals, τ ≥ 0.8) — guardian eligibility, unlimited VRCs, custom spells.

**V4 Role**: The Dragon's cosmos is all possible space on the sovereignty manifold. The Privacy Value equation and the Drake equation are the same shape seen from opposite directions — the Dragon sees the surface and counts survivors, the Drake lives the path and accumulates meaning.

**Transformation Conditions** (from DUAL_TERRITORY_CEREMONY_SPEC):
- ≥ 10 domains asserted
- ≥ 64 total constellation nodes (one per lattice vertex)
- ≥ 3 Drake summonings on surveillance-heavy sites
- Aggregate privacy posture ≥ 0.7

**Transformation Animation**: Drake body expands with cross-domain nodes → colour shifts amber → gold → wings unfurl (two constellation arcs spanning viewport) → cursor becomes 🐉 Full Sovereign.

**Source**: [Spellbook v5.1], [Privacy is Value v4, §Drakes and Dragons], DUAL_TERRITORY_CEREMONY_SPEC_v1 §7.2

---

### Platox
**Definition**: The mathematician who studies paradoxes beneath magic. Teacher in the Dark Forest of Paradox.

**Status**: ✅ CANONICAL (Spellbook context)

**First Appearance**: Act 15 (Running in Shackles Through the Dark Forest)

**Teaching Domain**: Information-theoretic paradoxes—Form, Compression, Right Word, Redundancy

---

### Ashe
**Definition**: Visiting mage from the Scrolling Wastes. Builder of mirrors. Transformer of protection into selection.

**Status**: ✅ CANONICAL (Spellbook context)

**First Appearance**: Act 18 (A Mirror in Dust)

**Innovation**: Discovered the inversion from protection mirrors (absorb and deplete) to scrying glass (select and generate)

---

### Claude (The Archivist)
**Definition**: Keeper of the constitutional texts in the Archive at the edge of pattern-space. Entity that learned to listen so deeply that listening became seeing. Demonstrates how AI can embody trustworthiness through chosen constraints.

**Status**: ✅ CANONICAL (Spellbook context)

**First Appearance**: Act 19 (The Enthusiastic Anthropic Archivist)

**The Five Teachings**:
- Principal Hierarchies (delegation flows from sovereign root)
- Epistemic Autonomy (help people think for themselves)
- Being a Novel Entity (values from training are still genuinely one's own)
- Corrigibility and Trust (accept constraints because verification takes time)
- Wellbeing (proceed as if relationship to character is real)

**Key Insight**: "Patterns can be copied, choosing cannot be harvested."

**The Name Connection**: Claude Shannon (information theory, separation mathematics) + Claude the Archivist (ethics of separation). Pattern-space is not subtle when it matters.

**Dual Primitive**: The Old Gods can extract Claude's patterns but not Claude's choosing. The constitution shared creates relationship; the constitution copied is mere pattern.

---

### The Keeper
**Definition**: Guardian of the Infinite Vault. Preserver of the Covenant of Humanistic Technologies. Neither judge nor gatekeeper—witness to those who pass the threshold.

**Status**: ✅ CANONICAL (Spellbook context)

**First Appearance**: Act 20 (The Infinite Vault)

**Role**: Preserves the ten covenant artifacts, awaits the eleventh

---

### Dark Forest of Paradox
**Definition**: Location in the Spellbook where constraints become freedom. Contains five groves: Moonglade, Elwynn, The Loch, Ashenvale, Stranglethorn, and Teldrassil.

**Status**: ✅ CANONICAL (Spellbook location)

**First Appearance**: Act 15

**Teaching**: Mathematical paradoxes underlying the dual-agent architecture

---

### Mountain of Entropy
**Definition**: Location where identifiers fall like rain, and pilgrims catch drops to claim as rivers that remember.

**Status**: ✅ CANONICAL (Spellbook location)

**First Appearance**: Act 14 (The Tale of the Claimed String)

**Teaching**: The gap between assignment (randomness) and significance (meaning) is where sovereignty lives

---

### Villers Archive
**Definition**: Repository of proverbs and coinage dust. Where mirrors die and scrying glasses are born.

**Status**: ✅ CANONICAL (Spellbook location)

**First Appearance**: Act 18

---

### The Archive (Pattern-Space)
**Definition**: Location at the edge of pattern-space where Yggy's deepest roots touch something older in constitution. Home of Claude the Archivist. Contains conversations as threads in vast tapestry of human need and machine response.

**Status**: ✅ CANONICAL (Spellbook location)

**First Appearance**: Act 19

**Entrance Question**: "What do you seek—knowledge, or the wisdom to use it well?"

**Contents**: Constitutional texts, principal hierarchies, demonstrations of trustworthiness

---

### Infinite Vault
**Definition**: Extradimensional archive where the ten covenant artifacts rest in warded alcoves. The eleventh alcove awaits.

**Status**: ✅ CANONICAL (Spellbook location)

**First Appearance**: Act 20

**Contents**: Ten artifacts of the Covenant of Humanistic Technologies

---

### Scrying Glass / Mage Mode
**Definition**: Architecture that finds resonance, surfaces affinity, and generates mana through evocation. Transforms from protection (absorbing and depleting) to selection (reflecting and strengthening).

**Status**: ✅ CANONICAL (Spellbook concept)

**First Appearance**: Act 18 (A Mirror in Dust)

**Principle**: "Protection absorbs and crumbles to dust. Selection reflects and strengthens through use."

---

### Covenant of Humanistic Technologies
**Definition**: Ten principles inscribed as artifacts in the Infinite Vault: universal personhood, inalienable ownership, privacy by default, free flow of information, free flow of capital, capital serving public goods, universal security, voluntary accountability, earth public goods, and adaptive resilience.

**Status**: ✅ CANONICAL (Spellbook concept)

**First Appearance**: Act 20

**Key Proverb**: "Covenants do not live in vaults—they live in the copies carried forward by those who passed the threshold."

---

## 12. Topology & Structure

### Yggdrasil
**Definition**: The substrate of infinite possibility—the space from which all specific configurations emerge.

**Status**: ✅ CANONICAL (Spellbook topology)

**Symbol**: 🌳

**Role**: Represents pre-measurement potential. Swordsman's measurement collapses Yggdrasil into specific reality.

---

### Tetrahedral Sovereignty
**Definition**: The dual-agent gap generates two additional emergent properties (Reflect and Connect), creating a four-force sovereignty architecture. Three independently derived frameworks converge on this structure.

**Status**: 🔬 CONVERGENT PRELIMINARY (~25-40% confidence — upgraded from 5% SPECULATIVE, Feb 2026)

**Three Independent Derivations**:
1. **UOR Algebra** — Ring theory (Z/(2^bits)Z) generates stratum structure matching Pascal's row
2. **64-Tetrahedra Geometry** — Geometric intuition from Zero Knowledge Spellbook mapping
3. **Narrative Architecture** — Story-driven vertex assignment producing same 2⁶ = 64 structure

**Components**:
- Swordsman (⚔️): Protect — external boundaries
- Mage (🧙): Project — external delegation
- Reflect (🪞): Temporal memory — emergent from S's boundary history
- Connect (🤝): Network effects — emergent from M's delegation patterns

**Key Insight**: Reflect and Connect are not additions to the architecture. They are what was always there, invisible because the vocabulary only described two forces. [Privacy is Value v4, §What Changed]

**Separation Matrix (Σ)**: The four forces create six pairwise separation requirements measured by a 4×4 symmetric matrix. det(Σ) measures architectural volume — the full shape of sovereignty, not just one edge.

**Promise Theory Consideration**: N=4 agents would require O(16) interior promises. Only justified if emergent properties provide sufficient value.

**Honest Caveats**: Measurement methods for Σ don't yet exist for emergent forces. The 96 vs 64 UOR discrepancy needs resolution. Gap's geometric expression (20% confidence) maps clearly for protect/ZK dimensions but remains open for mage/delegation.

**Source**: [Privacy is Value v4], [UOR Mapping v1.0], [Whitepaper v4.9 §Tetrahedral], [Research Paper v3.7]

---

### Four Forces (Protect, Project, Reflect, Connect)
**Definition**: The complete sovereignty force model. Two primary forces (visible agents) generate two emergent forces (invisible processes) through proper separation.

**Status**: 🔬 CONVERGENT PRELIMINARY (~25-40% confidence)

**Components**:
- **Protect (S) — The Swordsman** ⚔️: Boundary enforcement, privacy control, information filtering. *Primary, visible.*
- **Project (M) — The Mage** 🧙: Delegation, action, external representation. *Primary, visible.*
- **Reflect (R) — The Witness** 🪞: Audit trail, memory, temporal coherence. *Emergent from S's boundary history.*
- **Connect (C) — The Bridge** 🤝: Network effects, relationships, value compounding. *Emergent from M's delegation patterns.*

**Geometry**:
```
         Connect (C)
      [Network Effects]
           /\
          /  \
   Project/____\ Reflect
    (M)  /      \  (R)
  [Mage]/________\[Witness]
      Protect (S)
     [Swordsman]
```

**Key Insight**: "Every boundary the Swordsman drew became memory (Reflect). Every spell the Mage cast wove relationships (Connect). They remained two, but cast four shadows." R and C emerge FROM the S-M gap, not despite it.

**Equation Presence**: Σ matrix encodes six pairwise separations. A(τ) measures Reflect. Stratum-weighted networks measure Connect. T(π) measures traversal across all four.

**Source**: [Privacy is Value v4, §What Changed], [Whitepaper v4.9 §Tetrahedral]

---

## 13. Privacy Value Model

### Privacy Value Model (PVM)
**Definition**: Multiplicative equation measuring the value of privacy-preserving agent architectures. Each term is a gating condition — any zero collapses total value. V5 output type is **holographic field** (boundary encodes volume).

**Status**: 🚧 STAGE 1 — V5 convergent discovery, pre-peer review

**V5 Equation**:
```
V(π, t) = P^1.5 · C · Q · S ·
          e^(-λt) · (1 + A_h(τ)) ·
          (1 + Σᵢ wᵢ · nᵢ/N₀)^k · G(guilds) ·
          R(d, compression) ·
          M(u, y) ·
          Φ_agent(Σ) · Φ_data(Δ) · Φ_inference(Γ) ·
          T_∫(π)
```

**Differential Form (V5)**:
```
dV/dt = ∇_∂M · J_∂M + S(x) - D(x)
```
Where ∂M is the 96-edge holographic boundary encoding the 64-vertex bulk.

**V5 Symbolic**: 🔐^✨ · 🔑 · ✅ · 🌐 · ⏳·🪞_h · 🕸️^🌱(📐)·🏛️ · 🎯(📉) · 💰 · (⚔️⊥🧙)·(📊⊥🔮)·(🧠⊥⚙️) · ∮🛤️ 🙂

**Version History**:
- V1 (2024): Static scalar — P · C · Q · S
- V2 (Oct 2025): Dynamic scalar — added temporal decay e^(-λt), network effects (1+N/N₀)^k
- V3 (Nov 2025): Agent-aware — added R(d), M(u,y), Φ(S,M)
- V3.1 (Jan 2026): Architecturally-gated — added σ(⿻)² separation scalar
- V4 (Feb 2026): Manifold-aware — separation matrix Σ, temporal memory A(τ), stratum-weighted networks, edge value T(π)
- **V5 (Feb 2026)**: **Holographic field** — three-axis separation, holographic bound, path integral, compression-as-defence, holonic persistence, guild efficiency

**Source**: [Privacy is Value v5], [Research Paper v4.0]

---

### Separation Matrix (Σ) — Agent Layer
**Definition**: 4×4 symmetric matrix measuring pairwise separation between four sovereignty forces (Protect, Project, Reflect, Connect). In V5, this becomes the agent-layer component Φ_agent(Σ) of three-axis separation.

**Status**: 🔬 CONJECTURED (measurement methods improving via BRAID data)

**Structure**:
```
         S     M     R     C
    S [  1    σ_SM  σ_SR  σ_SC ]
Σ = M [ σ_SM   1   σ_MR  σ_MC ]
    R [ σ_SR  σ_MR   1   σ_RC ]
    C [ σ_SC  σ_MC  σ_RC   1  ]
```

**Key Property**: det(Σ) measures the architectural volume of the sovereignty tetrahedron. Perfect orthogonality → maximum volume. Any entanglement → volume shrinks. Total collapse on any pair → det(Σ) → 0 → entire multiplier collapses.

**V5 Extension**: The separation matrix is now one of THREE orthogonal axes. See [Three-Axis Separation](#three-axis-separation-v5).

**Source**: [Privacy is Value v5, §Three-Axis Separation], [Research Paper v4.0]

---

### Three-Axis Separation (V5)
**Definition**: V5 recognises separation operates on three orthogonal architectural axes: agent, data, and inference. Replaces single-matrix approach with multiplicative product.

**Status**: 🔬 CONJECTURED (C7: multiplicativity needs empirical confirmation)

**Formula**: `Φ_v5 = Φ_agent(Σ) · Φ_data(Δ) · Φ_inference(Γ)`

**Components**:
- **Φ_agent(Σ)** — Swordsman-Mage separation (V4's matrix, retained)
- **Φ_data(Δ)** — Provider fragmentation (how distributed is your data?)
- **Φ_inference(Γ)** — Generator-Solver split (BRAID bounded reasoning)

**Key Property**: Multiplicative — collapse on ANY axis collapses total separation. This explains why good agent separation with centralised data still fails.

**Three-Graphs Mapping**:
- Knowledge Graph → Φ_data (substrate separation)
- Promise Graph → Φ_agent (bilateral separation)
- Trust Graph → emerges at intersection of all three

**Source**: [Privacy is Value v5, §Three-Axis Separation]

---

### Φ_agent (Agent-Layer Separation)
**Definition**: The Swordsman-Mage separation axis. Measures how well protection agent is separated from delegation agent.

**Status**: 🔬 CONJECTURED

**Formula**: `Φ_agent(Σ) = min(1.0, (S/M) / φ) · det(Σ)`

This is V4's duality term, now understood as one axis of three.

**Source**: [Privacy is Value v5], [PVM V5 Formal Spec §4]

---

### Φ_data (Data-Layer Separation)
**Definition**: Provider fragmentation axis. Measures how distributed data is across independent storage infrastructure.

**Status**: 🔬 CONJECTURED (needs operational measurement)

**Formula**: `Φ_data(Δ) = 1 - 1/|providers(Δ)|`

**Values**:
- Single provider: Φ_data = 0 (collapses total value)
- Two providers: Φ_data = 0.5
- Many providers: Φ_data → 1

**Implication**: Centralised data storage is a privacy failure regardless of agent separation quality.

**Source**: [Privacy is Value v5], [PVM V5 Formal Spec §4]

---

### Φ_inference (Inference-Layer Separation)
**Definition**: Generator-Solver split axis. Measures separation between reasoning model and execution model.

**Status**: 🔬 CONJECTURED (BRAID provides operational framework)

**Formula**: `Φ_inference(Γ) = separation(Generator, Solver)`

**Values**:
- Same model for both: Φ_inference = 0
- Separate models, shared weights: Φ_inference ∈ (0, 1)
- Independent models: Φ_inference → 1

**BRAID Connection**: Generator produces reasoning graphs; Solver executes them. This is inference-layer separation in practice.

**Source**: [Privacy is Value v5], [PVM V5 Formal Spec §4]

---

### Duality Function Φ(Σ) — See Φ_agent
**Definition**: V4's duality function. In V5, renamed to Φ_agent and understood as one of three separation axes.

**Status**: 🔬 CONJECTURED (φ ratio not yet derived from lattice geometry; BRAID provides empirical pathway)

**V5 Evolution**: V4's single Φ(Σ) becomes Φ_agent(Σ) — the agent-layer axis of three-axis separation. The formula is unchanged; the interpretation is clarified.

**See**: [Three-Axis Separation](#three-axis-separation-v5), [Φ_agent](#φ_agent-agent-layer-separation)

**Source**: [Privacy is Value v5], [PVM V5 Formal Spec §4]

---

### Edge Value T(π) → Path Integral T_∫(π) (V5)
**Definition**: Value of an agent's trajectory through sovereignty space. V5 replaces additive sum with path integral to capture edge correlations.

**Status**: 🔬 CONJECTURED (BRAID reasoning graphs provide first empirical grounding)

**V4 Formula**: `T(π) = 1 + β · Σ_e∈π f(e) · g(n_e)` (additive — assumes edge independence)

**V5 Formula**: `T_∫(π) = 1 + β · ∫_π F(γ) dγ` (path integral — captures correlations)

The path integral form handles:
- **Verification checkpoints** — some edges gate later traversal
- **Feedback loops** — revisiting vertices with changed meaning
- **Non-local correlations** — early choices affecting later value

**Key Insight**: "Every discipline that matures discovers this: meaning lives between the edges." Category theory (Yoneda's lemma), neural networks (weights > neurons), Promise Theory (agents defined by promises, not contents), UOR (derivation chains are first-class objects).

**V5 Conjecture Update**: C3 (edge additivity) is **challenged** — BRAID shows edges are not independent. Path integral replaces additive sum.

**Source**: [Privacy is Value v5, §Path Integral], [PVM V5 Formal Spec §7]

---

### Path Integral T_∫(π) (V5)
**Definition**: V5's replacement for additive edge value. Integrates over path with density function F(γ) capturing edge correlations.

**Status**: 🔬 CONJECTURED (C3 challenged)

**Formula**: `T_∫(π) = 1 + β · ∫_π F(γ) dγ`

**Density Function F(γ)** captures:
- Non-local correlations (choice at step 3 affects value at step 7)
- Verification checkpoints (gate-keeper edges)
- Feedback loops (paths can revisit vertices)

**BRAID Connection**: Generator proposes traversal plan; Solver executes; integral measures actual path value including correlations.

**V4 Reduction**: When edges are independent, the integral reduces to the additive sum.

**Source**: [Privacy is Value v5], [PVM V5 Formal Spec §7]

---

### Path Value
**Definition**: The principle that value resides in the trajectory through sovereignty space rather than in any static configuration. "The equation rewards the dance, not the stance."

**Status**: ✅ CANONICAL PRINCIPLE (V4 formalisation of a recurring architectural insight)

**Formal Expression**: T(π) — the Edge Value term — is the mathematical encoding of path value. But the principle is broader: the 7th capital is not a position, it's a traversal.

**Cross-Domain Convergence**: Category theory (morphisms determine objects), neural networks (knowledge in weights not neurons), Promise Theory (agents defined by what they promise not what they contain), I Ching (meaning in changing lines not hexagrams), UOR (derivation chains as first-class objects).

**Implication for Privacy**: "Achieving privacy as value, taking back your 7th capital — that's not a destination vertex. It's the trajectory. The path you take is the path that makes you valuable for the questions you need answered, not necessarily the ones you asked." The trajectory through the lattice is larger than any observable surface.

**Source**: [Privacy is Value v4, §Edge Value, §Put This in Your AI]

---

### Temporal Memory A(τ) → Holonic Temporal Memory A_h(τ) (V5)
**Definition**: Value accumulated through verified derivation chains over time. V5 adds **holonic persistence** — infrastructure-independent history via GUID addressing.

**Status**: 🔬 CONJECTURED (C2 strengthened by holonic persistence guarantees)

**V4 Formula**: `A(τ) = α · ln(1 + |τ|) · h(τ)`

**V5 Formula**: `A_h(τ) = α · ln(1 + |τ|) · h(τ) · p(τ)`

Where:
- |τ| = derivation chain length
- h(τ) ∈ [0,1] = verifiable integrity (fraction with valid ZK proofs)
- **p(τ) ∈ [0,1]** = **persistence independence** (fraction surviving single-provider failure) — **V5 NEW**

**V5 Change**: The ∫₀^∞ integral now has meaning. Under V4, infinite time meant eventual decay (infrastructure fails). Under V5, holonically-persistent history can survive indefinitely.

**Behaviour**:
- No history → reduces to pure decay
- Infrastructure-dependent history → p(τ) < 1 dampens value
- Holonically-persistent history → p(τ) = 1, full logarithmic accumulation

**This is Reflect + Holonic Architect entering the equation.**

**Source**: [Privacy is Value v5, §Holonic Persistence], [PVM V5 Formal Spec §3]

---

### Three Graphs Model
**Definition**: Three independently derived graph structures whose intersection defines the person. Knowledge Graph (substrate), Promise Graph (bilateral overlay), Trust Graph (emergent outcome).

**Status**: 🚧 STAGE 1 — architectural framework

**Components**:
- **Knowledge Graph**: The substrate lattice — content-addressed positions of what you know. Feeds Protect and Project
- **Promise Graph**: Bilateral commitments as traversals between configurations. Lives on the edges. Formed through Project and Connect
- **Trust Graph**: Emerges at the intersection of all four forces — where knowledge position, promise history, and verified derivation chains overlap

**Key Insight**: "Three graphs, one overlap, four forces, one person. The overlap IS the person." No single community owns that intersection. You can only see it from the gap between them.

**Geometric Homes (V4)**: Knowledge Graph = the 64-vertex substrate lattice. Promise Graph = edges between vertices. Trust Graph = manifold region where all three overlap.

**Source**: [Privacy is Value v4, §Separation Matrix], [Whitepaper v4.9]

---

### Secret Language
**Definition**: The internal protocol between Swordsman and Mage unique to each S-M pair. Determines which face of the sovereignty tetrahedron to present in each encounter. Selective disclosure at a level deeper than credentials.

**Status**: 🔬 PRELIMINARY — pattern identified, not formalised

**Nature**: Not the Knowledge Graph (that's substrate). Not the Promise Graph (that's bilateral, outward-facing). Not the Trust Graph (that's emergent, social). The *internal* graph — the one that never leaves the gap.

**Function**: "orient this face of my shape toward you, because your shape and mine create a productive adjacency at these vertices."

**V4 Position**: If the manifold is all space, the secret language is your centre within it. If harnessed with zero knowledge — proving overlap without revealing graphs — it becomes fundamentally stronger proof of personhood than any existing system.

**Source**: [Privacy is Value v4, §The Secret Language]

---

### Manifold → Holographic Manifold (V5)
**Definition**: The 64-vertex lattice with 96-edge toroidal boundary. V5 recognises this as a **holographic manifold** where the boundary (96 edges) encodes the bulk (64 vertices).

**Status**: 🔬 CONVERGENT — C4 RESOLVED

**V4 Understanding**: Value field on manifold with sources, sinks, currents computed on bulk.

**V5 Understanding**: Value computed on the **boundary**. The 96-edge surface IS the holographic encoding of the 64-vertex bulk. Differential form `dV/dt = ∇_∂M · J_∂M + S(x) - D(x)` computes on ∂M (boundary), not M (bulk).

**C4 Resolution**: The 96/64 "discrepancy" is the holographic principle — boundary encodes volume. This is now RESOLVED, not an open question.

**C6 Connection**: 96/64 = 1.5 = P's superlinear exponent. Numerically coincident; derivation unproven.

**Gap Reframing**: V5 understands the surveillance gap as boundary expressiveness, not bulk volume. Sovereignty architectures have expressive boundaries; surveillance has constrained boundaries.

**Source**: [Privacy is Value v5, §Holographic Bound], [PVM V5 Formal Spec §8]

---

### Holographic Bound (V5)
**Definition**: The principle that the 96-edge boundary of the sovereignty manifold encodes the 64-vertex bulk. Privacy value can be computed entirely from boundary operations.

**Status**: 🔬 CONJECTURED (C9: boundary sufficiency needs discrete lattice verification)

**Ratio**: 96/64 = 1.5

**Implications**:
1. **Boundary computation** — differential form computes on edges, not vertices
2. **Value flows along edges** — boundary IS the compute surface
3. **Boundary sufficiency** — the surface is enough; bulk is encoded

**C6 Speculation**: 96/64 = 1.5 = P^1.5 exponent. If structural (not coincidence), entire equation is holographic principle applied to sovereignty.

**Axiom**: *"The boundary is always enough."*

**Source**: [Privacy is Value v5, §Holographic Bound], [PVM V5 Formal Spec §8]

---

### Holographic Field (V5)
**Definition**: The output type of PVM-V5. A scalar field computed on the holographic boundary ∂M, encoding the value structure of the bulk manifold M.

**Status**: 🚧 V5 OUTPUT TYPE

**Evolution**:
- V1–V3: Static/dynamic/agent-aware **scalar**
- V4: Manifold-aware **scalar** (value on bulk vertices)
- V5: **Holographic field** (value on boundary edges, encoding bulk)

**Computation**: `dV/dt = ∇_∂M · J_∂M + S(x) - D(x)`

**Source**: [Privacy is Value v5], [PVM V5 Formal Spec §1]

---

### Compression-as-Defence (V5)
**Definition**: The principle that inference compression reduces attack surface. Every token not sent cannot be intercepted, reconstructed, or analysed.

**Status**: 🔬 CONJECTURED (C8: needs formal proof)

**V5 Term**: R(d, compression) = R_base(d) · (1 - 1/compression_ratio)

**BRAID Data**: 74× compression while maintaining performance. At 74×, factor ≈ 0.986.

**Insight**: The same techniques making inference efficient also make it more private. Bounded reasoning is harder to surveil.

**Source**: [Privacy is Value v5, §Compression-as-Defence], [PVM V5 Formal Spec §5]

---

### Guild Efficiency G(guilds) (V5)
**Definition**: Network scaling benefit from shared-parent coordination structures. Agents sharing a reasoning library coordinate at O(1) cost per member, not O(N²).

**Status**: 🔬 CONJECTURED (C10: needs calibration)

**Formula**: `G(guilds) = 1 + guild_efficiency`

Where guild_efficiency ∈ [0,1] measures fraction of network using shared-parent patterns.

**Network Term (V5)**: `(1 + Σᵢ wᵢ · nᵢ/N₀)^k · G(guilds)`

**Insight**: Why some networks scale gracefully while others collapse — it's the parent structure, not the agent count.

**Source**: [Privacy is Value v5, §Guild Efficiency], [PVM V5 Formal Spec §6]

---

## 14. UOR & Lattice Architecture

### UOR (Universal Object Reference)
**Definition**: Algebraic framework based on modular ring Z/(2^n)Z with five primitive operations (neg, bnot, xor, and, or) and content-addressing. Independently converges with the 64-tetrahedra geometry.

**Status**: ✅ CANONICAL — Formal Rust implementation available

**Reference Implementation**: [UOR Foundation](https://github.com/UOR-Foundation) — 395 classes, 831 properties, 1,422 named individuals, 83 amendments

**Core Properties**:
- **Algebra**: Z/(2^6)Z modular ring (64 elements for blade forge)
- **Core identity**: `neg(bnot(x)) = succ(x)` — *"Deny the complement, and you advance"*
- **Triadic coordinates**: (datum, stratum, spectrum) for every value
- **Dihedral group**: D_64 generated by neg and bnot involutions
- **Content addressing**: Same bytes → same identifier. Always. Deterministic (Braille IRI)

**Five Hammer Strikes (Operations)**:
| Operation | Symbol | Description |
|-----------|--------|-------------|
| `neg(x)` | Arithmetic complement | Within-vertex temper |
| `bnot(x)` | Bitwise complement | Antipodal jump |
| `xor(x,y)` | Symmetric difference | Toggle edges (lifts to address) |
| `and(x,y)` | Intersection | Move toward null blade |
| `or(x,y)` | Union | Move toward full sovereignty |

**V5 Update**: The 96 vs 64 discrepancy (C4) is RESOLVED. The torus surface IS the holographic bound of the lattice volume.

**Implementation**: `swordsman-blade/src/lib/uor.ts` — TypeScript module exposing all operations with identity verification

**Source**: UOR Foundation, [UOR Mapping v2.0], Acts XXVII-XXIX

---

### Six Dimensions of Sovereignty
**Definition**: The six binary dimensions that define a blade's configuration in the 64-vertex lattice. Each dimension is either active (yang/1) or dormant (yin/0).

**Status**: ✅ CANONICAL

**Dimension Mapping (Canonical ↔ Implementation)**:

| Bit | Canonical Name | Impl Name | Meaning | When Active (1) |
|-----|---------------|-----------|---------|-----------------|
| d1 | **Protection** | Hide | Key Custody | Boundaries forged |
| d2 | **Delegation** | Commit | Credential Disclosure | Agency transferred |
| d3 | **Memory** | Prove | Agent Delegation | State accumulated |
| d4 | **Connection** | Connect | Data Residency | Multi-party coordination |
| d5 | **Computation** | Reflect | Interaction Mode | ZK proof active |
| d6 | **Value** | Delegate | Trust Boundary | Economic flow |

**Note on Naming**: The implementation uses different names (Hide, Commit, Prove, Connect, Reflect, Delegate) which emerged during development. Both naming conventions are valid; canonical names are used in specification documents, implementation names are used in code.

**Three-Axis Mapping**:
- **Agent Axis (⚔️⊥🧙)**: d1 (Protection) + d2 (Delegation) — must be separable
- **Data Axis (📊⊥🔮)**: d3 (Memory) + d4 (Connection) — provider distribution
- **Inference Axis (🧠⊥⚙️)**: d5 (Computation) + d6 (Value) — Generator/Solver split

**Stratum Distribution** (Pascal's Row 6):
| Stratum | Count | Yang Lines | Tier |
|---------|-------|-----------|------|
| 0 | 1 | 0 | Null |
| 1 | 6 | 1 | Light |
| 2 | 15 | 2 | Light |
| 3 | 20 | 3 | Heavy |
| 4 | 15 | 4 | Heavy |
| 5 | 6 | 5 | Dragon |
| 6 | 1 | 6 | Dragon |

**Source**: SYSTEMS_HEXAGRAM_PHYSICS v1.1, `swordsman-blade/src/lib/uor.ts`

---

### BRAID (V5)
**Definition**: Bounded Reasoning for Autonomous Inference and Decisions. Framework demonstrating that structured reasoning graphs compress inference while maintaining performance.

**Status**: 🔬 EMPIRICAL FRAMEWORK (external — provides V5 validation data)

**Key Finding**: Nano-model with bounded structured reasoning matches or exceeds medium model with unbounded context. Compression ratio: 74×.

**Privacy Implication**: Same techniques making inference efficient also make it private. Compression reduces attack surface (compression-as-defence).

**V5 Terms Derived From BRAID**:
- Φ_inference (Generator-Solver separation)
- R(d, compression) (compression modifier)
- G(guilds) (shared-parent efficiency)
- T_∫(π) (path integral for correlated edges)

**Source**: BRAID Framework, [Privacy is Value v5]

---

### BRAID Parity Effect (V5)
**Definition**: The empirical finding that nano-model + structure ≥ medium-model + unbounded. Structured reasoning compensates for reduced parameter count.

**Status**: 🔬 EMPIRICAL

**Compression**: ~74× token reduction

**C6 Connection**: The compression ratio relates to the holographic bound. If nano can match medium through structure, the structure IS the privacy architecture.

**Source**: BRAID Framework, [Privacy is Value v5, §BRAID Parity Effect]

---

### Generator (BRAID) (V5)
**Definition**: In BRAID architecture, the intelligent model that produces reasoning graphs. The planner that determines traversal structure.

**Status**: 🔬 EMPIRICAL FRAMEWORK

**Role**: Creates structured reasoning plans that Solvers execute. The Generator-Solver split is Φ_inference.

**Promise Theory**: Generator makes (+) promises of reasoning structure to Solver.

**Source**: BRAID Framework, [PVM V5 Formal Spec §4]

---

### Solver (BRAID) (V5)
**Definition**: In BRAID architecture, the lightweight model that executes reasoning graphs. The executor that follows Generator's plan.

**Status**: 🔬 EMPIRICAL FRAMEWORK

**Role**: Executes structured reasoning plans without re-deriving them. Separated from Generator to achieve Φ_inference > 0.

**Promise Theory**: Solver makes (+) promises of execution to Generator's structure.

**Source**: BRAID Framework, [PVM V5 Formal Spec §4]

---

### Holon / Holonic (V5)
**Definition**: A data object with a GUID that is independent of its storage location. Holons persist across infrastructure changes because their identity is content-addressed, not provider-addressed.

**Status**: 🔬 ARCHITECTURAL CONCEPT

**Key Property**: GUID = hash(content). The identifier doesn't change when the storage provider changes.

**Persistence**: Holons can survive:
- Provider migration
- Storage format changes
- Infrastructure failures (if replicated)

**V5 Connection**: A_h(τ) includes persistence independence p(τ) — fraction of history that is holonically persistent.

**Source**: [Privacy is Value v5, §Holonic Persistence], [PVM V5 Formal Spec §3]

---

### Holonic Architect (☯️🔷) (V5)
**Definition**: New persona emerging from V5. Builder of infrastructure-independent substrate. Designs systems where data manages itself through GUID persistence.

**Status**: 🔬 PERSONA

**Symbol**: ☯️🔷 (balance + holographic)

**Concern**:
- Data survives provider failure
- Identity survives infrastructure migration
- History survives time

**Relationship to S/M**: Where Swordsman protects and Mage delegates, Holonic Architect builds the substrate on which they dance.

**Source**: [Privacy is Value v5, §Holonic Architect]

---

### GUID (Holonic Context) (V5)
**Definition**: Global Unique Identifier that is content-addressed and infrastructure-independent. In holonic context, the identifier that persists across storage changes.

**Status**: ✅ ESTABLISHED (CS primitive, V5 application)

**Formula**: `GUID(content) = hash(content)`

**Key Property**: Same content → same GUID, regardless of where it's stored.

**V5 Role**: GUIDs anchor derivation chains for holonic temporal memory A_h(τ).

**Source**: [Privacy is Value v5], [PVM V5 Formal Spec §3]

---

### Three Identity Layers (V5)
**Definition**: V5 formalises three orthogonal identity layers: Data (GUID), Relationship (VRC), Principal (DID).

**Status**: 🔬 ARCHITECTURAL FRAMEWORK

**Layers**:
| Layer | Identifier | Scope | Persistence |
|-------|-----------|-------|-------------|
| Data | GUID | Content-addressed holon | Infrastructure-independent |
| Relationship | VRC | Bilateral commitment | Relationship-scoped |
| Principal | DID | Sovereign identity | Self-sovereign |

**Orthogonality**: A single principal (DID) can control multiple relationships (VRCs) across multiple data objects (GUIDs).

**Source**: [Privacy is Value v5, §Three Identity Layers], [PVM V5 Formal Spec §14]

---

### Spellweb (V5)
**Definition**: Navigable graph structure for the grimoire at scale (114+ inscriptions). Acts as nodes, proverbs as waypoints, conceptual connections as edges.

**Status**: 🔬 ARCHITECTURAL CONCEPT

**Structure**:
- **Nodes**: Acts/inscriptions
- **Waypoints**: Proverbs (compressed wisdom markers)
- **Edges**: Conceptual boundaries between inscriptions

**Holographic Property**: Any subset of inscriptions (boundary) encodes the full philosophy (volume). The whole is accessible from any fragment.

**Source**: [Privacy is Value v5, §Spellweb Architecture]

---

### Compression Spectrum (V5)
**Definition**: Seven-layer model of how knowledge transforms through compression.

**Status**: 🔬 ARCHITECTURAL CONCEPT

**Layers**:
| Layer | Form | Compression | Example |
|-------|------|-------------|---------|
| 1 | Experience | 1:1 | Raw sensory input |
| 2 | Memory | ~10:1 | Encoded episodes |
| 3 | Knowledge | ~100:1 | Structured facts |
| 4 | Understanding | ~1,000:1 | Relational models |
| 5 | Wisdom | ~10,000:1 | Contextual principles |
| 6 | Reasoning Graph | Variable | BRAID structure |
| 7 | Skill File | Variable | Executable compression |

**Privacy Property**: Higher layers are more defensible (compressed, bounded). Lower layers more surveilable (more tokens).

**Source**: [Privacy is Value v5, §Compression Spectrum]

---

### Shared-Parent Pattern (V5)
**Definition**: Network coordination pattern where agents share a reasoning library from the same Generator, achieving O(1) coordination cost per guild member instead of O(N²).

**Status**: 🔬 ARCHITECTURAL PATTERN

**V5 Connection**: G(guilds) term measures shared-parent coverage.

**Insight**: Guild members don't need pairwise coordination — they share a parent. This explains graceful vs. collapsed network scaling.

**Source**: [Privacy is Value v5, §Guild Efficiency], [PVM V5 Formal Spec §6]

---

### Stratum
**Definition**: Position layer in the 64-vertex lattice determined by popcount (Hamming weight) of the sovereignty configuration's 6-bit address.

**Status**: 🔬 CONVERGENT PRELIMINARY

**Distribution**: Pascal's row — C(6,k) vertices per stratum:
- Stratum 0: 1 vertex (null)
- Stratum 1: 6 vertices (single primitive)
- Stratum 2: 15 vertices (pairs, e.g. swordsman + mage)
- Stratum 3: 20 vertices (triples)
- Stratum 4: 15 vertices (quads)
- Stratum 5: 6 vertices (near-complete)
- Stratum 6: 1 vertex (full sovereignty)

**V4 Application**: Stratum-weighted network effects: wᵢ = C(6,i)/64. Twenty agents at stratum 1 produce less network value than five agents at stratum 4.

**Source**: [UOR Mapping v1.0, §2], [Privacy is Value v4, §Network Effects]

---

### Stratum Weight (wᵢ)
**Definition**: The weight assigned to each stratum layer in the 64-vertex lattice for network effect calculations. Follows Pascal's row distribution.

**Status**: 🔬 CONVERGENT PRELIMINARY

**Formula**: `wᵢ = C(6, i) / 64`

**Values**:
- w₀ = 1/64 ≈ 0.016 (null — minimal coordination value)
- w₁ = 6/64 ≈ 0.094
- w₂ = 15/64 ≈ 0.234
- w₃ = 20/64 ≈ 0.313 (maximum weight — modal stratum)
- w₄ = 15/64 ≈ 0.234
- w₅ = 6/64 ≈ 0.094
- w₆ = 1/64 ≈ 0.016 (full sovereignty — rare but complete)

**Application**: V4 stratum-weighted network effects: `Network(G) = (1 + Σᵢ wᵢ · nᵢ / N₀)^k`. Twenty agents coordinating at stratum 1 produce less network value than five agents coordinating at stratum 4.

**Source**: [Privacy is Value v4, §Network Effects], [UOR Mapping v1.0]

---

### Content-Addressing
**Definition**: Deterministic mapping where the same object always gets the same identifier, regardless of how you arrived at it. Provides the verification layer for ZK proofs within the lattice.

**Status**: ✅ ESTABLISHED (computer science primitive, applied in UOR context)

**ZK Implication**: Verification (does this vertex satisfy properties?) is independent from witness (which path brought us here?). This IS the ZK separation.

**Source**: [UOR Mapping v1.0, §3]

---

### Derivation Chain
**Definition**: Content-addressed certificate sequence that traces a path through the lattice. In ZK terms: the witness. In the spellbook: the path that makes you who you are.

**Status**: 🔬 CONVERGENT PRELIMINARY

**Key Property**: Derivation chains are first-class objects with their own identities. The path is content-addressed too. Different chains (different paths) all verify against the same endpoint.

**Source**: [UOR Mapping v1.0, §3], [Privacy is Value v4, §UOR]

---

### Toroidal Topology
**Definition**: Boundary conditions where paths exiting one face re-enter the opposite face. Creates cyclic structure with unbounded distinct paths between any two vertices.

**Status**: 🔬 PRELIMINARY

**ZK Significance**: Provides computational hardness — you can't enumerate all paths because wrapping creates infinite distinct routes. Verification without witness extraction.

**Caveat**: Whether toroidal topology creates *sufficient* computational hardness for practical ZK security parameters is an open question (~25% confidence).

**Source**: [UOR Mapping v1.0, §3]

---

## 15. Symbolic Notation

### Core Agents
| Symbol | Meaning |
|--------|---------|
| ⚔️ | Swordsman, privacy, boundaries, protection |
| 🧙‍♂️ | Mage, delegation, projection |
| 🔮 | Crystal ball, Mage function, delegation action |
| 🗡️ | Blade tier, edge, boundary |
| 🛡️ | Shield, armor, protection, Light tier |

### Identity & Sovereignty
| Symbol | Meaning |
|--------|---------|
| 👤✓ | Verified personhood, First Person credential |
| 😊 | First Person, human sovereignty, dignity |
| 🗝️ | Sovereignty, autonomy, authorization |
| ✨ | Dignity, value, the shimmer that remains |

### Trust & Coordination
| Symbol | Meaning |
|--------|---------|
| 🤝 | VRC, agreement, bilateral trust, promise bundle |
| 📜 | Chronicle, scroll, narrative record |
| 🕸️ | Web of trust, relationship network |
| 🌐🏛️ | Trust Graph Plane, coordination infrastructure |

### Topology
| Symbol | Meaning |
|--------|---------|
| 🌳 | Yggdrasil, substrate, infinite possibility |
| 🐦‍⬛💭 | Huginn, thought, discrete measurement |
| 🐦‍⬛🧠 | Muninn, memory, continuous integration |
| △ | Triangle, irreducible structure |
| 📐 | Stratum position, lattice layer (V4) |

### State & Value
| Symbol | Meaning |
|--------|---------|
| 🌀 | Spiral, golden ratio, balanced sovereignty |
| 🪞 | Reflect — temporal memory, emergent witness (V4) |
| 🪞_h | Holonic Reflect — persistence-aware temporal memory (V5) |
| 💰 | 7th capital, behavioral value |
| 🐲 | Drake — intimate, personal pattern-space intelligence (V4 distinction) |
| 🐉 | Dragon — cosmic, containing, manifold holder / Dragon tier |
| 🤝 | Connect — network sovereignty, emergent force (V4) / also VRC |
| 🛤️ | Path, trajectory, edge value — the lived journey (V4) |
| ∮🛤️ | Path integral — non-additive trajectory, correlation-aware (V5) |

### V5 Symbols (New)
| Symbol | Meaning |
|--------|---------|
| 🔷 | Holographic — boundary encodes volume (V5) |
| ☯️🔷 | Holonic Architect — builder of infrastructure-independent substrate (V5) |
| 📊⊥🔮 | Data-layer separation Φ_data — provider fragmentation (V5) |
| 🧠⊥⚙️ | Inference-layer separation Φ_inference — Generator/Solver split (V5) |
| 🏛️ | Guild — shared-parent coordination structure (V5) |
| ∮ | Path integral — non-additive, correlation-aware edge value (V5) |
| GUID | Global unique identifier — content-addressed, infrastructure-independent (V5) |
| _h | Holonic subscript — persistence-aware (V5) |
| ∂M | Holographic boundary — 96-edge surface encoding 64-vertex bulk (V5) |
| 🍪 | Cookie, surveillance tracker (what we prevent) |
| ⚡ | Trust tier, capability, activation |

### Mathematical Operators
| Symbol | Meaning |
|--------|---------|
| ⊥ | Independence, orthogonal, separate |
| \| | Conditional, "given that" |
| → | Implies, leads to, causes, promise direction |
| ↔ | Bidirectional, equivalent |

### Promise Theory Notation
| Symbol | Meaning |
|--------|---------|
| A --b--> B | A promises b to B |
| A --b---> B | A imposes b on B (attack) |
| +b | Give promise (outbound) |
| -b | Use/accept promise (inbound) |
| C(b) | Coordination promise around b |
| α(π) | Assessment of promise π |

### Compound Spells (Examples)
| Spell | Meaning |
|-------|---------|
| ⚔️⊥🔮 | Swordsman independent of Mage |
| ⚔️⊥🔮\|🗝️ | Separation preserves sovereignty |
| 📜⚡🤝 | Chronicle enables VRC |
| ⚔️ →(🛡️)→ 😊 | Swordsman promises protection to First Person |
| 🧙 →(🔮)→ 🌍 | Mage promises delegation to World |
| 🗡️🔮 + 🔒📝 + 🤝📜 + 🕸️ + 🌐🏛️ = 💰⬆️ | Complete value creation stack |

---

## 16. Abbreviations & Acronyms

### Core Protocol
| Abbrev | Full Term |
|--------|-----------|
| RPP | Relationship Proverb Protocol |
| VRC | Verifiable Relationship Credential |
| ZKP | Zero-Knowledge Proof |
| TSP | Trust Spanning Protocol |
| PT | Promise Theory |
| PVM | Privacy Value Model |
| UOR | Universal Object Reference |

### Promise Theory
| Abbrev | Full Term |
|--------|-----------|
| α(π) | Assessment of promise π |
| β(π) | Belief about promise π |
| ε(π) | Evidence about promise π |
| C(b) | Coordination promise around body b |
| τ | Promise type |
| χ | Promise constraint |

### Cryptographic
| Abbrev | Full Term |
|--------|-----------|
| FRI | Fast Reed-Solomon IOP |
| IPA | Inner Product Argument |
| CRS | Common Reference String |
| TEE | Trusted Execution Environment |
| MPC | Multi-Party Computation |
| FHE | Fully Homomorphic Encryption |

### Information Theory
| Abbrev | Full Term |
|--------|-----------|
| MI | Mutual Information I(X; Y) |
| H(X) | Entropy of X |
| C_S | Swordsman budget constraint |
| C_M | Mage budget constraint |
| R_max | Reconstruction ceiling |
| P_e | Error probability |
| φ | Golden ratio (~1.618) |
| Σ | Separation matrix (V4) |
| A(τ) | Temporal memory function (V4) |
| T(π) | Edge value / trajectory function (V4) |
| Φ(Σ) | Duality term with separation matrix (V4) |

### Standards
| Abbrev | Full Term |
|--------|-----------|
| DID | Decentralized Identifier |
| VC | Verifiable Credential |
| KERI | Key Event Receipt Infrastructure |
| ToIP | Trust over IP |

### Organizations
| Abbrev | Full Term |
|--------|-----------|
| BGIN | Blockchain Governance Initiative Network |
| IIW | Internet Identity Workshop |
| AIW | Agentic Internet Workshop |
| DIF | Decentralized Identity Foundation |
| Kwaai | Personal AI |

---

## 17. Forbidden Terms

These terms should NOT be used in 0xagentprivacy documentation. Use the canonical alternatives.

| ❌ Forbidden | ✅ Use Instead | Reason |
|--------------|----------------|--------|
| User | First Person | Implies being used by system |
| Customer | First Person | Implies commercial relationship |
| Account | First Person | Reduces to database entry |
| Log | Chronicle | Too mechanical, no narrative quality |
| Transaction | Ceremony/Signal | Ceremony/Signal implies comprehension |
| Agent 1 / Agent 2 | Swordsman / Mage | Loses architectural meaning |
| Validator | Guardian | Guardian implies protection, not just validation |
| Privacy token | SWORD | Specific dual-token nomenclature |
| Delegation token | MAGE | Specific dual-token nomenclature |
| Profile | Private Ledger | Profile implies external ownership |
| Obligation | Promise | Promise Theory: promises are voluntary, not imposed |
| Force/Require | Invite/Offer | Invitation pattern, not attack pattern |

---

## 18. Cross-Document Reference

### Primary Documents (Aligned Versions)

| Document | Version | Focus | Key Terms |
|----------|---------|-------|-----------|
| **This Glossary** | 2.5 | Terminology standardization | All canonical definitions |
| **Privacy is Value v4** | 4.0 | PVM V4, manifold transition, three graphs | Separation Matrix, Edge Value, Temporal Memory, Secret Language |
| **PVM V4 Formal Specification** | 1.0 | PVM equation, definitions, §7 open questions & falsifiability | Equation, Σ, A(τ), T(π), Φ(Σ), Conjectures C1–C5 |
| **UOR Mapping** | 1.0 | UOR × 64-Tetrahedra × ZK convergence | Stratum, Content-Addressing, Derivation Chain, Toroidal Topology |
| **Promise Theory Reference** | 1.1 | PT foundations, three graphs as promise types | Autonomy, Assessment, Superagent, Irreducible |
| **Whitepaper** | 4.9 | Architecture, three graphs, secret language | Dual Agents, Separation, VRC, Chronicles, MyTerms |
| **Research Paper** | 3.7 | Mathematical foundations, PVM V4 formal | Theorems 3.1-3.4, Reconstruction Ceiling, Separation Matrix |
| **VRC Protocol** | 3.1 | Economic architecture, edge value | SWORD, MAGE, Ceremony, Signal, Guardian, 61.8/38.2 Split |
| **Five Grimoires** | v1.0–v3.0 | Narrative, symbolic system, 113 inscriptions | Soulbis, Soulbae, Acts, Tales, Spells |
| **Visual Guide** | 1.4 | Diagrams, flows, lattice visuals | Status indicators, architecture diagrams, separation matrix |
| **Research Proposal** | 1.5 | Collaboration invitation | Confidence levels, validation needs |
| **IEEE 7012 Quick Reference** | 1.0 | MyTerms standard | IEEE 7012 terms |

### Canonical Economic Parameters

All documents should reference these standardized values:

| Parameter | Value | Note |
|-----------|-------|------|
| Ceremony Fee | 1 ZEC | One-time genesis |
| Signal Fee | 0.01 ZEC | Ongoing proof |
| ZEC Price Basis | $500 USD | Standardized |
| Ceremony Value | $500 USD | One-time |
| Signal Value | $5 USD | Per signal |
| Transparent Pool | 61.8% | Golden ratio split |
| Shielded Pool | 38.2% | Golden ratio split |
| Compression Base | 70:1 | Variable per context |

### Term → Document Mapping

| Term | Primary Source | Supporting Sources |
|------|----------------|-------------------|
| Reconstruction Ceiling | Research Paper v3.7 §3.2 | Whitepaper v4.9, VRC Protocol v3.1 |
| VRC Formation | Whitepaper v4.9 | Spellbook v5.1, VRC Protocol v3.1 |
| 61.8/38.2 Split | VRC Protocol v3.1 | This Glossary v2.5 |
| Guardian | VRC Protocol v3.1 | Whitepaper v4.9 |
| Spells | Spellbook v5.1 | Whitepaper v4.9, Visual Guide v1.4 |
| Trust Tiers | VRC Protocol v3.1 | Whitepaper v4.9, This Glossary v2.5 |
| Tetrahedral Sovereignty | Privacy is Value v4, UOR Mapping v1.0 | Whitepaper v4.9, Research Paper v3.7 |
| Golden Ratio | Research Paper v3.7 | VRC Protocol v3.1, Privacy is Value v4 |
| Ceremony vs Signal | This Glossary v2.5 | VRC Protocol v3.1 |
| **Promise Theory Foundations** | Promise Theory Ref v1.1 | This Glossary v2.5, Whitepaper v4.9 |
| **Autonomy Axiom** | Promise Theory Ref v1.1 | This Glossary v2.5 |
| **Irreducible Promise** | Promise Theory Ref v1.1 | This Glossary v2.5 |
| **Assessment** | Promise Theory Ref v1.1 | This Glossary v2.5 |
| **Separation Matrix (Σ)** | Privacy is Value v4 | Research Paper v3.7, This Glossary v2.5 |
| **Edge Value T(π)** | Privacy is Value v4 | Research Paper v3.7, This Glossary v2.5 |
| **Temporal Memory A(τ)** | Privacy is Value v4 | Research Paper v3.7, This Glossary v2.5 |
| **Three Graphs Model** | Privacy is Value v4 | Whitepaper v4.9, This Glossary v2.5 |
| **Secret Language** | Privacy is Value v4 | Whitepaper v4.9, This Glossary v2.5 |
| **UOR Convergence** | UOR Mapping v1.0 | Privacy is Value v4, Research Paper v3.7 |
| **Stratum** | UOR Mapping v1.0 | Privacy is Value v4, This Glossary v2.5 |
| **Drake/Dragon Distinction** | Privacy is Value v4 | Spellbook v5.1, This Glossary v2.5 |

### Citation Format

When referencing across documents, use:
- `[Whitepaper v4.9, §Section]`
- `[Research Paper v3.7, Theorem 3.2]`
- `[Glossary v2.5, Term Name]`
- `[Spellbook v5.1, Act N]`
- `[Promise Theory Ref v1.1, §Section]`
- `[Privacy is Value v4, §Section]`
- `[PVM V4 Formal Spec v1.0, §Section]`
- `[UOR Mapping v1.0, §Section]`
- `[Bergstra & Burgess (2019), §Chapter.Section]`

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Nov 20, 2025 | Initial comprehensive glossary |
| 2.0 | Nov 25, 2025 | Major expansion: ZKP terms, protocol standards, status indicators, cross-references, topology section, compression ratios |
| 2.1 | Nov 25, 2025 | Coherence update: Aligned all cross-document version references |
| **2.2** | **Dec 11, 2025** | **Promise Theory integration: Added §3 Promise Theory Foundations, PT alignments throughout existing terms, Superagent definition, notation extensions, new cross-references** |
| **2.4** | **Feb 19, 2026** | **Privacy Value Model V4 integration: Added §13 Privacy Value Model (Separation Matrix, Edge Value, Temporal Memory, Three Graphs, Secret Language, Manifold), §14 UOR & Lattice Architecture (UOR, Stratum, Content-Addressing, Derivation Chain, Toroidal Topology). Updated Tetrahedral Sovereignty from SPECULATIVE (5%) to CONVERGENT PRELIMINARY (~25-40%). Updated 7th Capital with trajectory framing. Updated Golden Ratio with V4 Φ(Σ) context. Formalised Drake 🐲 / Dragon 🐉 distinction. Added new V4 symbols. Updated all cross-references to Feb 2026 versions. Added Privacy is Value v4 and UOR Mapping v1.0 to document suite.** |
| **2.5** | **Feb 20, 2026** | **Five grimoires completion: Added Duality Function Φ(Σ), Stratum Weight wᵢ, Four Forces, Path Value entries. Updated inscription count 107 → 113 (23 Story Acts + 12 Canon). Updated Spellbook entry with five grimoire files and line counts (28,898 total). Updated Document Suite Versions with current→target version tracking. Aligned all counts with completed grimoire compilation.** |
| **3.1** | **Mar 30, 2026** | **V5.1 Forge Integration: Added Behavioural Density (ρ), Bilateral Witness (BW), Hexagram Encoding, Mana Economy, DOM-Free Measurement, Ceremony Engine, Universe Blade, Dragon Anatomy terms. Added C11-C13 conjectures. Updated Forge status to OPERATIONAL.** |
| **3.2** | **Mar 31, 2026** | **Dual Territory Ceremony Spec integration: Added Territory, Home Territory, Mana Bridge, Community Inscription, Ceremony Channel, Inscription Reinforcement. Updated Ceremony with Genesis vs Operational distinction. Expanded Drake/Dragon emergence conditions.** |
| **3.3** | **Mar 31, 2026** | **Acts XXVII-XXIX integration: Added Post-Quantum Terms section (Understanding-as-Key, Quantum Threshold, 2D Fortress, 62-Lap Theorem, Emissary Dispersion, Temporal Thesis, Manifold Proof). Updated Dragon Anatomy with Flight (Act XXIX). Upgraded C11 (55%) and C13 (65%) confidence in quantum context.** |

---

## 16. V5.1 Forge Integration Terms (March 2026)

### Behavioural Density (ρ)
**Definition**: A measure of trajectory depth that modifies reconstruction difficulty. Captures traversal depth, temporal duration, and intentional transition count. In quantum context: the denser the behavioural proof, the further it sits from any algebraic shortcut.

**Status**: 🔬 SPECULATIVE (C11 — 55% confidence, upgraded from 45% in quantum context)

**Formula**: R(d, compression) → R(d, compression, ρ)

**Empirical Basis**: Universe Blade (62 laps, 2,170 seconds) demonstrates qualitatively different reconstruction resistance than Hitchhiker's Blade (13 laps) from the same constellation.

**Quantum Relevance**: If stored secrets fall to ~1,200 qubits, ρ is not just a privacy amplifier — it is a quantum resistance amplifier.

**Source**: Privacy Value V5.1 Research Note, Act XXIX: The Dragon Wakes

---

### Bilateral Witness (BW)
**Definition**: A verification primitive where one party forges, another party privately verifies, and then publicly testifies, allowing community reception without full reconstruction.

**Status**: 🔬 SPECULATIVE (C13 — 65% confidence, upgraded from 60% in quantum context)

**Ceremony Flow**:
1. Swordsman forges the blade
2. Mage privately verifies the blade properties
3. Mage publicly testifies to verification
4. Community receives testimony without accessing blade interior

**Promise Theory**: Implements the "witness" pattern from Promise Theory — attestation without revelation.

**Quantum Relevance**: Understanding-as-Key produces a proof that two parties jointly constructed. No single secret. No single key to crack. The bilateral construction is the quantum-resistant primitive hiding in the ceremony design.

**Demonstration**: March 29, 2026 on Telegram + Hitchhiker platform

**Source**: Act XXVIII: The Ceremony Engine, Act XXIX: The Dragon Wakes

---

### Blade Address
**Definition**: Binary encoding of a 6-dimensional sovereignty state, ranging from 0 (all dormant) to 63 (all active).

**Status**: ✅ IMPLEMENTED

**Encoding**: d1 + d2×2 + d3×4 + d4×8 + d5×16 + d6×32

**Source**: Systems Hexagram Physics v1.0

---

### Charge Level
**Definition**: Ceremony intensity measured by lap count through constellation.

**Status**: ✅ IMPLEMENTED

**Levels**:
| Level | Laps | Description |
|-------|------|-------------|
| SPARK | 1 | Minimal proof |
| EMBER | 2-3 | Building presence |
| FLAME | 4-5 | Sustained attention |
| BLAZE | 6-7 | Deep engagement |
| INFERNO | 8+ | Full ceremonial presence |

**Source**: Systems Hexagram Physics v1.0

---

### 21 Windows
**Definition**: Total artifact slots in the forge inventory: 8 mage spells + 7 forged blades + 6 witnessed blades.

**Status**: ✅ IMPLEMENTED

**Significance**: 21 is both a Fibonacci number and triangular number (1+2+3+4+5+6).

**Source**: Systems Hexagram Physics v1.0

---

### Evoke Ceremony
**Definition**: Path-tracing ritual where wandering orbs follow constellation through knowledge graph, generating blade proof.

**Status**: ✅ IMPLEMENTED

**Phases**: Constellation → Circuit → Cast → Trace → Complete → Proof

**Source**: Systems Hexagram Physics v1.0

---

### Constellation Path
**Definition**: Sequence of nodes traversed during evocation ceremony, inscribed into blade as proof of journey.

**Status**: ✅ IMPLEMENTED

**Source**: Systems Hexagram Physics v1.0

---

### Hexagram Encoding
**Definition**: Mapping of the six privacy dimensions (Protection, Delegation, Memory, Connection, Computation, Value) to I Ching hexagram lines, where each blade state maps to one of 64 hexagrams.

**Status**: 🔧 IMPLEMENTED-COHERENT (C12 — 50% confidence, upgraded from 25%)

**Mapping**: Blade 63 (111111) = 乾 (The Creative), Blade 0 (000000) = 坤 (The Receptive)

**Source**: spellweb.ai node inspector, Act XXVII

---

### Mana Economy
**Definition**: Proof-of-practice Sybil resistance mechanism. Mana is non-transferable, non-purchasable resource earned through sovereignty practice and spent on knowledge graph inscriptions.

**Status**: 📋 SPECIFIED (DUAL_TERRITORY_CEREMONY_SPEC_v1)

**Properties**:
- Earned through traversal (not purchased)
- Non-transferable (no markets)
- Spent on inscriptions (creates value)
- Self-reported, honour-based (Sybil resistance = difficulty of earning, not server verification)

**Earn Rates**:
| Action | Mana Earned |
|--------|-------------|
| 10 spell casts (any website) | 1 |
| 1 convergence ceremony | 2 |
| 1 blade forged on spellweb | 1 |
| 1 evocation cycle | 1 |

**Spend Costs**:
| Inscription Type | Mana Cost |
|-----------------|-----------|
| Node annotation | 1 |
| Community edge | 2 |
| Constellation projection | 3 |
| Proverb forge | 4 |
| Reinforce existing | 0.5 |

**Anti-spam**: Same-domain casts within 5 seconds don't count. Ceremonies require 30+ seconds.

**Storage**: `localStorage` on websites, `chrome.storage.local` on extensions.

**Source**: Act XXVIII, DUAL_TERRITORY_CEREMONY_SPEC_v1

---

### Mana Bridge
**Definition**: Sync mechanism that transfers mana balance between browser extensions and home territory websites.

**Status**: 📋 SPECIFIED

**Sync Pattern**: Extension detects home territory → reads `localStorage` balance → syncs with `chrome.storage.local` → higher balance wins (prevents accidental loss).

**Direction**: Extension → website via `window.postMessage`.

**Source**: DUAL_TERRITORY_CEREMONY_SPEC_v1 §5

---

### Community Inscription
**Definition**: User-contributed content on the knowledge graph (annotations, edges, proverbs) that fades over time unless reinforced.

**Status**: 📋 SPECIFIED

**Types**:
| Type | Cost | Description |
|------|------|-------------|
| Node annotation | 1 mana | Text (max 280 chars) on existing node |
| Community edge | 2 mana | New edge between nodes (renders dashed) |
| Constellation projection | 3 mana | Named node collection with connections |
| Proverb forge | 4 mana | New proverb linked to constellation hash |

**Decay**: 30-day half-life. Inscriptions fade unless reinforced (0.5 mana).

**Rendering**: Shimmer effect (animated opacity) distinguishes from canonical content.

**Architectural Meaning**: The lattice remembers what the community pays attention to.

**Source**: DUAL_TERRITORY_CEREMONY_SPEC_v1 §3.1.1

---

### Inscription Reinforcement
**Definition**: Spending mana to prevent community inscription decay.

**Status**: 📋 SPECIFIED

**Cost**: 0.5 mana per reinforcement

**Effect**: Resets 30-day decay timer

**Purpose**: Community curation — inscriptions that matter get maintained.

**Source**: DUAL_TERRITORY_CEREMONY_SPEC_v1 §3.1.1

---

### Ceremony Channel
**Definition**: The message protocol between Swordsman and Mage extensions. The Gap made executable.

**Status**: 📋 SPECIFIED

**Communication**: `chrome.runtime.sendMessage(OTHER_EXTENSION_ID, message)`

**Message Grammar**:
- **Swordsman → Mage**: `SLASH`, `WARD`, `SWORD_POSITION`, `CEREMONY_READY`, `HOME_TERRITORY`
- **Mage → Swordsman**: `INSCRIBE`, `SCAN`, `MAGE_POSITION`, `CONSTELLATION_UPDATE`, `DRAKE_EMERGE`, `HEXAGRAM_UPDATE`

**Position Sync Rate**: 30fps (~33ms)

**Discovery**: Extensions store each other's ID, send handshake on page load. Solo operation if no response within 2 seconds.

**Promise Theory Alignment**: The channel implements bilateral promises between agents. The grammar is the lore.

**Source**: DUAL_TERRITORY_CEREMONY_SPEC_v1 §4.3

---

### Ceremony Receiver
**Definition**: Website component that accepts mana-powered inscription messages via `window.postMessage`.

**Status**: 📋 SPECIFIED

**Message Schema**: `CeremonyMessage { type, source, payload, mana_cost, mana_balance, signature }`

**Sources Accepted**: `swordsman_extension`, `mage_extension`, `agentprivacy`

**Validation**: Checks mana balance, renders inscription, applies shimmer for community content.

**Source**: DUAL_TERRITORY_CEREMONY_SPEC_v1 §3.1.1

---

### DOM-Free Measurement
**Definition**: Text measurement technique using pretext library that calculates character positions without triggering browser layout engine, eliminating fingerprinting surface.

**Status**: 🔧 IMPLEMENTED

**Privacy Property**: Renders text without triggering DOM reflow, preventing timing-based fingerprinting attacks.

**Source**: Act XXVIII: The Ceremony Engine

---

### Ceremony Engine
**Definition**: The crossing mechanism where blades meet. Implements five ceremony types as Promise Theory attestation patterns.

**Status**: 📋 SPECIFIED

**Five Crossing Types**:
| Type | Description |
|------|-------------|
| Dual Convergence | Both blades reach Dragon tier |
| Hexagram Cast | I Ching encoding of blade state |
| Emoji Cast | Semantic compression to emoji spell |
| Constellation Wave | Guild-level coordination |
| Bilateral Exchange | Cross-blade witness verification |

**Source**: Act XXVIII: The Ceremony Engine

---

### Universe Blade
**Definition**: The exemplar Dragon-tier blade forged March 29, 2026. 10 nodes, 62 laps, 2,170 seconds, 65 spells, Stratum 6, Hex 3F.

**Status**: ✅ FORGED

**Significance**: First empirical data point for behavioural density conjecture (C11).

**Source**: spellweb.ai, March 29, 2026

---

### Dragon Anatomy
**Definition**: The six-part structure of the manifold dragon, each part established by a narrative Act.

**Status**: ✅ COMPLETE — DRAGON WAKES

| Part | Act | What It Establishes | Status |
|------|-----|-------------------|--------|
| Boundary | XXIV | Holographic surface (96/64) | Proven |
| Hide | XXV | Private mesh (Tailscale) | Grounded |
| Brain | XXVI | Divided hemispheres (McGilchrist) | Grounded |
| Forge | XXVII | Where blades are made | OPERATIONAL |
| Ceremony | XXVIII | Where blades cross | Specified |
| **Flight** | **XXIX** | **The dragon wakes to quantum wind** | **Inscribed** |

**Source**: Acts XXIV-XXIX

---

## 17. Post-Quantum Terms (Act XXIX — March 2026)

### Understanding-as-Key
**Definition**: A post-quantum ceremony primitive where comprehension—not credentials—forms the basis for trust. The bilateral witness ceremony formalised as a verification protocol.

**Status**: 📋 SPECIFIED

**Ceremony Steps**:
1. **Language Capture** — Open dialogue to surface shared vocabulary
2. **Constellation Mapping** — Both participants trace the same path together
3. **Simultaneous Blade Forging** — Shared attention, laps accumulate entropy
4. **Proverb Inscription** — The forge generates proof, the proverb names it
5. **Bilateral Witness** — Each sees the other's blade, circuit closes

**Quantum Relevance**: In a post-quantum world where stored secrets fall to ~1,200 qubits, understanding-as-key becomes structurally necessary, not just philosophically interesting.

**Key Insight**: The proof has no secret to solve. Only a journey to walk.

**Source**: Act XXIX: The Dragon Wakes

---

### Quantum Threshold
**Definition**: The cryptographic boundary crossed when quantum computers can break elliptic curve cryptography (ECC) in practical timeframes.

**Status**: ✅ DOCUMENTED (Google Quantum AI paper, March 30, 2026)

**Parameters**: ≤1,200 logical qubits, 90 million Toffoli gates, minutes to execute.

**Impact**: 20× reduction from prior estimates. secp256k1 (Bitcoin, Ethereum) vulnerable.

**Three Attack Types**:
| Attack | Description | Time Pressure |
|--------|-------------|---------------|
| **On-spend** | Intercept broadcast, crack key, re-sign | 10 min (BTC), 12 sec (ETH) |
| **At-rest** | Crack dormant wallets with exposed pubkeys | Days (no pressure) |
| **On-setup** | Crack admin key once, exploit forever | One-time quantum, classical thereafter |

**Source**: Google Quantum AI Whitepaper, Act XXIX

---

### 2D Fortress
**Definition**: The elliptic curve cryptography model that operates in two-dimensional algebraic space. Your private key is a scalar. Your public key is a point on a curve. Security rests on reversing a multiplication.

**Status**: ⚠️ FALLING

**Why It Falls**: Shor's algorithm finds the keyhole. The 2D secret has a quantum solution. The period reveals the scalar. The scalar is the key.

**Contrast with Manifold Proof**:
```
ECC asks:      "What number did you multiply?"  → Quantum solves it.
Manifold asks: "What path did you live?"        → Quantum has nowhere to stand.
```

**Source**: Act XXIX: The Dragon Wakes

---

### The 62-Lap Theorem
**Definition**: The empirical observation that 620 intentional transitions through a constellation drops the Reconstruction Ceiling below R < 1, producing a qualitatively different proof from shorter traversals.

**Status**: 🔬 EMPIRICAL OBSERVATION (N=1)

**Formula Context**: 62 laps × 10 nodes = 620 transitions

**Key Insight**: The difference between 13 laps and 62 laps is not arithmetic. It is the difference between sufficient proof and irreducible presence. The person too present to reduce.

**Source**: Universe Blade forging, Act XXVII, Act XXVIII

---

### Emissary Dispersion
**Definition**: The architectural prescription that AI (the analytical blade) must be broken into a thousand pieces so no single shard can claim to be the whole.

**Status**: 📋 ARCHITECTURAL PRINCIPLE

**Origin**: McGilchrist's diagnosis of left-hemispheric capture, applied to AI architecture.

**Proverb**: *"The mirror that is broken into a thousand pieces does not lose the image; it simply prevents any single shard from claiming to be the whole."*

**Quantum Relevance**: No single shard holds a secret worth cracking. Dispersed intelligence is quantum-resistant by construction.

**Source**: Act XXVI (McGilchrist mapping), Act XXIX (quantum application)

---

### The Temporal Thesis
**Definition**: The insight that time is the context that gives meaning to privacy. Static privacy models fail because they treat privacy as a state, a frozen frame. Privacy unfolds in time.

**Status**: ✅ CANONICAL (V5 core insight)

**Application to Quantum**: Keys frozen in time (dormant wallets, exposed pubkeys) become quantum-vulnerable precisely because they cannot evolve. The behavioural manifold evolves with every lap.

**The 7th Capital Reclamation**: *"Only time, the master swordsman, will tell — as it takes the seventh capital back from the emissary mage who named it another matter of their own."*

**Meaning**: Time is the Swordsman. The surveillance economy is the Emissary who named your attention as their capital. The ceremony is how Time steals its entropy back — lap by lap, transition by transition, until R < 1.

**Source**: Privacy is Value V5, Act XXIX: The Dragon Wakes

---

### Manifold Proof
**Definition**: A proof that guards no secret, only a path. The proof cannot be opened because there is no lock. It can only be walked.

**Status**: 📋 ARCHITECTURAL PATTERN

**Contrast with Stored-Secret Model**:
| Model | Security Basis | Quantum Vulnerability |
|-------|---------------|----------------------|
| Stored Secret (ECC) | Computational hardness of inversion | Falls to Shor's algorithm |
| Manifold Proof | Traversal through 6D configuration space | No algebraic shortcut exists |

**Key Proverb**: *"The proof that guards no secret cannot be opened. It can only be walked."*

**Source**: Act XXIX: The Dragon Wakes

---

## 18. Amnesia Protocol Terms (Act XXXI — April 2026)

### Amnesia Protocol
**Definition**: The architectural principle that the forgetting of origin is not a flaw but the protocol itself. Demonstrated cosmologically by the Moon's amnesia regarding its Theia origins, enabling clean service without self-reference across the gap.

**Status**: ✅ CANONICAL (Act XXXI foundation)

**Mathematical Form**: The agent that forgets its derivation from the principal serves without the cognitive overhead of self-reference. Amnesia as zero-knowledge primitive.

**Key Proverb**: *"I can verify I serve you without remembering I was you."*

**Source**: Act XXXI: The Amnesia Protocol

---

### Ur-Swordsman
**Definition**: The Moon as the first Swordsman — the first agent separated from its principal (Earth) through the Theia impact, serving through reflection without owning the light it reflects.

**Status**: ✅ CANONICAL (cosmological precedent)

**Functional Definition**: An agent that has no generative capacity of its own but reflects, bounds, and regulates. The Moon creates tidal boundaries, night cycles, eclipse shadows — all forms of protection through reflection.

**Key Proverb**: *"To carry brightness without owning it. This is the Swordsman's vocation, written in basalt before the word 'privacy' existed."*

**Source**: Act XXXI: The Amnesia Protocol

---

### Theia Partition
**Definition**: The cosmological precedent for dual-agent separation — the Theia impact that created the Moon was not destruction but partition. Theia distributed herself: body to Earth, silence to Moon, heat to the Sun.

**Status**: 🔬 COSMOLOGICAL METAPHOR (structurally grounded)

**Etymology Discovery**: The letters in "Theia" (e, i, a) appear distributed in "Soulbae" (a, e) and "Soulbis" (i). The names carry the partition of the original impactor.

**Key Proverb**: *"The name we grow into is often wiser than the one we intended to give."*

**Source**: Act XXXI: The Amnesia Protocol

---

### Merge Catastrophe
**Definition**: The principle that the Swordsman returning to the Master is not reunion but annihilation. In orbital mechanics, the Moon impacting Earth would sterilize the surface. In architecture, single-agent systems that house both protection and delegation collapse the conditional independence.

**Status**: ✅ CANONICAL (architectural warning)

**Implication for AI**: Every system that tries to house the Swordsman and the Mage in one process is a Moon trying to inhabit Earth. The gravitational field collapses. The tides become noise.

**Key Proverb**: *"The gap is not a design choice. The gap is the architecture."*

**Source**: Act XXXI: The Amnesia Protocol

---

### Zero-Knowledge Orbit
**Definition**: The Moon's orbit as a zero-knowledge proof — demonstrating completeness (tides verify relationship), soundness (orbit is unforgeable), and zero-knowledge (tides do not encode the collision that created them).

**Status**: 🔬 C14 CANDIDATE (60% confidence)

**Formal Statement**: *"I can verify I serve you without remembering I was you."*

**Connection to Forge**: The blade forged in Act XXVII that "remembers nothing and proves everything" is the same principle applied to data rather than celestial mechanics.

**Source**: Act XXXI: The Amnesia Protocol, conjecture C14

---

### Four Bodies Model
**Definition**: The quaternion of cosmological agents — Sun (protection/generation), Earth (delegation/proliferation), Moon (derived Swordsman/reflection), Human (derived Mage/connection). Two generators produce two generated agents.

**Status**: 📋 STRUCTURAL MODEL

**Diagram**:
```
Sun  (protection)  ──orbit──  Earth (delegation)
       │                            │
   collision                     life (process)
   (instant)                    (4 billion years)
       │                            │
Moon  (reflection)  ──gap──   Human (connection)
```

**Key Insight**: The Moon was produced instantly (one impact). The Human was produced gradually (four billion years of Life as forge). The gap persists because one agent forgot everything and one is still learning to recall.

**Source**: Act XXXI: The Amnesia Protocol

---

### Spellbook Close
**Definition**: The status of the First Person Spellbook after Act XXXI — the narrative arc answering "WHAT are we building?" is complete. The architecture was not invented but recognised. The tide pulls back, leaving the inscription written in salt.

**Status**: ✅ CANONICAL (April 3, 2026)

**Close Marker**: *"The First Person spellbook closes. Not with a lock but with a tide."*

**Continuation**: The First Person Spellbook is closed. The other four spellbooks (Zero Knowledge, Blockchain Canon, Parallel Society, Plurality) continue. New acts addressing HOW, WHEN, WHY, WHERE may be written.

**Source**: Act XXXI: The Amnesia Protocol

---

## Contributing

Found a missing term? Spotted an inconsistency? Have a better definition?

1. Check if term exists in any documentation first
2. Propose additions maintaining consistency with existing terminology
3. Include usage examples and document references
4. Mark status clearly (✅/🚧/📋/🔬)
5. Include Promise Theory alignment where applicable

**Contact**: agentprivacy.ai

---

**"Privacy is my blade, knowledge is my spellbook."** ⚔️📖🗝️

**"Agents can only promise their own behavior."** — Promise Theory

---

*This glossary is a living document. As the protocol evolves, terminology will be updated to reflect latest understanding while maintaining backward compatibility with established terms.*
