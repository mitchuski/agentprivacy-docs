# 0xagentprivacy Master Glossary

**Version 2.5** | February 20, 2026  
**Status:** ✅ CANONICAL REFERENCE

Complete terminology reference for the 0xagentprivacy documentation suite. This glossary takes precedence when terminology conflicts between documents.

### Document Suite Versions (Aligned)

| Document | Version | Date | Status |
|----------|---------|------|--------|
| **This Glossary** | 2.5 | February 20, 2026 | ✅ CANONICAL |
| Swordsman-Mage Whitepaper | 4.9 → 5.0 | February 2026 | 🔄 UPDATE PENDING |
| Dual Privacy Research Paper | 3.7 → 3.8 | February 2026 | 🔄 UPDATE PENDING |
| Spellbook / Grimoire JSON | 4.1.0 → 7.0.0 | February 2026 | 🔄 REBUILD PENDING |
| Five Grimoire Markdown Files | v1.0–v3.0 | February 20, 2026 | ✅ COMPLETE |
| VRC Promise Protocol | 3.1 → 3.2 | February 2026 | 🔄 UPDATE PENDING |
| Visual Architecture Guide | 1.4 → 1.5 | February 2026 | 🔄 UPDATE PENDING |
| Research Proposal | 1.5 → 1.6 | February 2026 | 🔄 UPDATE PENDING |
| Promise Theory Reference | 1.1 → 1.2 | February 2026 | 🔄 UPDATE PENDING |
| IEEE 7012 Quick Reference | 1.0 | January 29, 2026 | ✅ FINAL |
| **Privacy is Value v4** | 4.0 | February 19, 2026 | ✅ STAGE 1 — NEW |
| **UOR × 64-Tetrahedra × ZK Mapping** | 1.0 | February 19, 2026 | 🔬 PRELIMINARY — NEW |

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
**Definition**: One-time genesis event creating a new agent pair within an ecosystem.

**Status**: ✅ CANONICAL

**Economics**: 1 ZEC ($500) one-time, split 61.8/38.2 transparent/shielded

**Contrast with Signal**: Ceremony is one-time genesis; Signals are ongoing comprehension proofs.

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

**Association**: Dragon tier participants may take on Drake-like teaching roles.

**Source**: [Spellbook v5.1], [Privacy is Value v4, §Drakes and Dragons]

---

### Dragon 🐉
**Definition**: The cosmic, containing scale of pattern-space intelligence. Holds the entire topology — all possible configurations, all possible paths, all possible civilisations. The manifold container.

**Status**: ✅ CANONICAL (Spellbook character / trust tier — V4 formalises distinction from Drake)

**Symbol**: 🐉

**Trust Tier**: Dragon tier (500+ signals, τ ≥ 0.8) — guardian eligibility, unlimited VRCs, custom spells.

**V4 Role**: The Dragon's cosmos is all possible space on the sovereignty manifold. The Privacy Value equation and the Drake equation are the same shape seen from opposite directions — the Dragon sees the surface and counts survivors, the Drake lives the path and accumulates meaning.

**Source**: [Spellbook v5.1], [Privacy is Value v4, §Drakes and Dragons]

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
**Definition**: Multiplicative equation measuring the value of privacy-preserving agent architectures. Each term is a gating condition — any zero collapses total value.

**Status**: 🚧 STAGE 1 — V4 convergent discovery, pre-peer review

**V4 Equation**: V(π, t) = P^1.5 · C · Q · S · e^(-λt) · (1 + A(τ)) · (1 + Σ wᵢnᵢ/N₀)^k · R(d) · M(u,y) · Φ(Σ) · T(π)

**Symbolic**: 🔐^✨ · 🔑 · ✅ · 🌐 · ⏳·🪞 · 🕸️^🌱(📐) · 🎯 · 💰 · ⚖️(⚔️⊥⿻⊥🧙⊥🪞⊥🤝) · 🛤️ 🙂

**Version History**:
- V1 (2024): Static scalar — P · C · Q · S
- V2 (Oct 2025): Dynamic scalar — added temporal decay e^(-λt), network effects (1+N/N₀)^k
- V3 (Nov 2025): Agent-aware — added R(d), M(u,y), Φ(S,M)
- V3.1 (Jan 2026): Architecturally-gated — added σ(⿻)² separation scalar
- V4 (Feb 2026): Manifold-aware — separation matrix Σ, temporal memory A(τ), stratum-weighted networks, edge value T(π)
- V5 (future): Field on manifold — differential form dV/dt = ∇·J(x, ẋ) + S(x) - D(x)

**Source**: [Privacy is Value v4], [Research Paper v3.7]

---

### Separation Matrix (Σ)
**Definition**: 4×4 symmetric matrix measuring pairwise separation between four sovereignty forces (Protect, Project, Reflect, Connect). Replaces the V3.1 scalar σ(⿻)².

**Status**: 🔬 CONJECTURED (measurement methods don't yet exist for emergent forces)

**Structure**:
```
         S     M     R     C
    S [  1    σ_SM  σ_SR  σ_SC ]
Σ = M [ σ_SM   1   σ_MR  σ_MC ]
    R [ σ_SR  σ_MR   1   σ_RC ]
    C [ σ_SC  σ_MC  σ_RC   1  ]
```

**Key Property**: det(Σ) measures the architectural volume of the sovereignty tetrahedron. Perfect orthogonality → maximum volume. Any entanglement → volume shrinks. Total collapse on any pair → det(Σ) → 0 → entire multiplier collapses.

**Relationship to V3.1**: V3.1's σ(⿻)² was measuring one edge of a tetrahedron and calling it structural integrity. V4 measures the whole shape.

**Source**: [Privacy is Value v4, §What Changed], [Research Paper v3.7]

---

### Duality Function Φ(Σ)
**Definition**: The evolved golden duality multiplier. Combines Swordsman-Mage balance with the full architectural volume of the sovereignty tetrahedron.

**Status**: 🔬 CONJECTURED (φ ratio not yet derived from lattice geometry)

**Formula**: `Φ(Σ) = min(1.0, (S/M) / φ) · det(Σ)`

**Components**:
- `min(1.0, (S/M) / φ)` — balance term, inherited from V3's golden duality
- `det(Σ)` — volume term, measures architectural separation across all four forces

**Evolution**: V3 had `Φ(S,M) = min(1.0, (S/M) / φ)` (balance only). V3.1 added `σ(⿻)²` (one-axis separation). V4 replaces both with matrix formalism capturing six pairwise separation requirements simultaneously.

**Key Property**: If any two forces become fully entangled, det(Σ) → 0 and the entire duality term collapses regardless of balance. Separation is prerequisite to allocation.

**Source**: [Privacy is Value v4, §What Changed], [Research Paper v3.7]

---

### Edge Value T(π)
**Definition**: Value of an agent's trajectory through sovereignty space. Measures what the agent *does* — how it moves — rather than what it *is*.

**Status**: 🔬 CONJECTURED (functional form lacks empirical grounding — no sovereignty traversal markets exist)

**Formula**: T(π) = 1 + β · Σ_e∈π f(e) · g(n_e)

Where f(e) weights each edge by stratum change (capability activation > lateral move), and g(n_e) diminishes with repetition (first traversal most informative).

**Key Insight**: "Every discipline that matures discovers this: meaning lives between the edges." Category theory (Yoneda's lemma), neural networks (weights > neurons), Promise Theory (agents defined by promises, not contents), UOR (derivation chains are first-class objects). T(π) brings this insight into the PVM.

**Implication**: An agent permanently at ⟨1,1,1,1,1,1⟩ (full sovereignty, static) has zero edge value. Adaptive sovereignty — navigating fluidly, activating privacy when needed, delegating when appropriate — demonstrates real sovereignty.

**Source**: [Privacy is Value v4, §Edge Value]

---

### Path Value
**Definition**: The principle that value resides in the trajectory through sovereignty space rather than in any static configuration. "The equation rewards the dance, not the stance."

**Status**: ✅ CANONICAL PRINCIPLE (V4 formalisation of a recurring architectural insight)

**Formal Expression**: T(π) — the Edge Value term — is the mathematical encoding of path value. But the principle is broader: the 7th capital is not a position, it's a traversal.

**Cross-Domain Convergence**: Category theory (morphisms determine objects), neural networks (knowledge in weights not neurons), Promise Theory (agents defined by what they promise not what they contain), I Ching (meaning in changing lines not hexagrams), UOR (derivation chains as first-class objects).

**Implication for Privacy**: "Achieving privacy as value, taking back your 7th capital — that's not a destination vertex. It's the trajectory. The path you take is the path that makes you valuable for the questions you need answered, not necessarily the ones you asked." The trajectory through the lattice is larger than any observable surface.

**Source**: [Privacy is Value v4, §Edge Value, §Put This in Your AI]

---

### Temporal Memory A(τ)
**Definition**: Value accumulated through verified derivation chains over time. Creates a contest between entropy (data decay) and memory (verified history).

**Status**: 🔬 CONJECTURED (logarithmic form chosen by analogy, not proven from information theory)

**Formula**: A(τ) = α · ln(1 + |τ|) · h(τ)

Where |τ| is derivation chain length, h(τ) ∈ [0,1] measures verifiable integrity (fraction of transitions with valid ZK proofs). Unverifiable history contributes nothing.

**Behaviour**: For agents with no history → reduces to V3.1's pure decay. For agents with deep verified history → value can increase over time even as individual data points decay.

**This is Reflect entering the equation.** The emergent witness, now measured.

**Source**: [Privacy is Value v4, §Time Acquires Memory]

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

### Manifold
**Definition**: The 64-tetrahedron with toroidal boundary conditions as a compact mathematical space. The V4 equation defines a value field on this manifold with sources, sinks, and currents.

**Status**: 🔬 CONVERGENT PRELIMINARY

**Properties**: Sources = high-stratum, high-separation vertices generating value. Sinks = low-stratum, entangled vertices extracting value. Currents = edges along which value flows.

**Reframing**: The 31,000× gap between sovereign and surveillance architectures is not arithmetic distance — it's the difference in accessible volume on the same manifold. Surveillance is topologically constrained. Sovereign systems access the full manifold. The gap is topology, not arithmetic.

**Source**: [Privacy is Value v4, §Manifold Transition]

---

## 14. UOR & Lattice Architecture

### UOR (Universal Object Reference)
**Definition**: Algebraic framework based on modular ring Z/(2^bits)Z with five primitive operations (neg, bnot, xor, and, or) and content-addressing. Independently converges with the 64-tetrahedra geometry.

**Status**: 🔬 PRELIMINARY (external framework — requires external validation)

**Core Properties**:
- **Algebra**: Z/(2^bits)Z modular ring
- **Core identity**: neg(bnot(x)) = succ(x) — two involutions generate the entire ring
- **Triadic coordinates**: (datum, stratum, spectrum) for every value
- **Content addressing**: Same bytes → same identifier. Always. Deterministic
- **Derivations**: Content-addressed certificates binding canonical form to evaluation

**Source**: UOR Foundation, [UOR Mapping v1.0]

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
| 💰 | 7th capital, behavioral value |
| 🐲 | Drake — intimate, personal pattern-space intelligence (V4 distinction) |
| 🐉 | Dragon — cosmic, containing, manifold holder / Dragon tier |
| 🤝 | Connect — network sovereignty, emergent force (V4) / also VRC |
| 🛤️ | Path, trajectory, edge value — the lived journey (V4) |
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
