# 0xagentprivacy Master Glossary

**Version 2.2** | December 11, 2025  
**Status:** ✅ CANONICAL REFERENCE

Complete terminology reference for the 0xagentprivacy documentation suite. This glossary takes precedence when terminology conflicts between documents.

### Document Suite Versions (Aligned)

| Document | Version | Date | Status |
|----------|---------|------|--------|
| **This Glossary** | 2.2 | December 11, 2025 | ✅ CANONICAL |
| Swordsman-Mage Whitepaper | 4.4 | November 29, 2025 | ✅ FINAL |
| Dual Privacy Research Paper | 3.2 | November 25, 2025 | ✅ FINAL |
| Spellbook | 4.0.1-canonical | November 25, 2025 | ✅ FINAL |
| Tokenomics Economic Architecture | 2.0 | November 25, 2025 | ✅ FINAL |
| Visual Architecture Guide | 1.1 | November 25, 2025 | ✅ FINAL |
| Research Proposal | 1.2 | November 25, 2025 | ✅ FINAL |
| **Promise Theory Reference** | 1.0 | December 11, 2025 | ✅ NEW |

**Note:** All cross-references between documents should use these version numbers. When documents reference each other, they should cite specific versions (e.g., "see Research Paper v3.2, Theorem 3.2").

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
3. [Promise Theory Foundations](#3-promise-theory-foundations) ← **NEW**
4. [Information Theory & Privacy](#4-information-theory--privacy)
5. [Cryptographic Primitives](#5-cryptographic-primitives)
6. [Trust Mechanics](#6-trust-mechanics)
7. [Economic System](#7-economic-system)
8. [Protocol Standards](#8-protocol-standards)
9. [Compression & Encoding](#9-compression--encoding)
10. [Spellbook & Narrative](#10-spellbook--narrative)
11. [Topology & Structure](#11-topology--structure)
12. [Symbolic Notation](#12-symbolic-notation)
13. [Abbreviations & Acronyms](#13-abbreviations--acronyms)
14. [Forbidden Terms](#14-forbidden-terms)
15. [Cross-Document Reference](#15-cross-document-reference)

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
**Definition**: Behavioral data as a form of personal wealth, distinct from the traditional six capitals (financial, manufactured, intellectual, natural, social, human).

**Status**: ✅ CANONICAL

**Origin**: Extends Jane Gleeson-White's work on capital forms to encompass digital behavioral sovereignty.

**Problem Statement**: Currently extracted by surveillance capitalism without consent or compensation, treating behavioral data as minable resource rather than personal property.

**Solution Architecture**: Dual-agent separation that keeps 7th capital under First Person control while enabling value-creating coordination.

**Economic Thesis**: Privacy-first architectures generate orders of magnitude more value than surveillance alternatives through trust-enabled network effects.

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

**Spell Notation**: The vertical bar | carries the same semantic weight: ⚔️ ⊥ 🧙 | 😊 states conditional independence in compressed form.

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

**0xagentprivacy Application**: Spells are coordination promises. When agents coordinate using spell notation (⚔️ ⊥ 🧙 | 😊), they make coordination promises to:
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

**Source**: Research Paper v3.2, Theorem 3.2

---

### Error Floor (P_e)
**Definition**: The minimum probability that an adversary makes at least one reconstruction error.

**Status**: ✅ PROVEN (Theorem 3.3)

**Formula**: P_e ≥ 1 - R_max

**Interpretation**: Adversaries are mathematically guaranteed to make errors when R_max < 1. This is not a feature that might fail—it's a theorem.

**Source**: Research Paper v3.2, Theorem 3.3

---

### Separation Theorem
**Definition**: Information leakage from dual agents is additive, not multiplicative.

**Status**: ✅ PROVEN (Theorem 3.1)

**Formula**: I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M) when (Y_S ⊥ Y_M) | X

**Promise Theory Alignment**: This is the mathematical consequence of the autonomy axiom applied to dual agents—each agent's promises are independent, so their information contributions add rather than multiply.

**Implication**: Adversary gains no synergy from observing both agents. Two sources of partial information don't combine into complete information.

**Source**: Research Paper v3.2, Theorem 3.1

---

### Budget Constraint
**Definition**: The limit on total information leakage across both agents.

**Status**: ✅ CANONICAL

**Formula**: C_S + C_M < H(X)

**Promise Theory Alignment**: This is a valency constraint—limited exclusive promise capacity prevents total revelation.

**Implementation**: Enforced through architectural separation, not policy. The separation itself creates the constraint.

**Source**: Research Paper v3.2, §3.2

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

**Source**: Whitepaper v4.4, §VRC Formation

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
**Definition**: Mathematical constant (~1.618) appearing in the 61.8/38.2 transparent/shielded split.

**Status**: 🔬 SPECULATIVE (empirical validation needed)

**Application**: 
- Fee split: 61.8% transparent / 38.2% shielded (= 1/φ ratio)
- Budget hypothesis: Optimal C_M/C_S may converge to φ

**Source**: Tokenomics v2.0, Research Paper v3.2

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

### MyTerms (IEEE 7012)
**Definition**: Framework for bilateral privacy agreements where First Persons set terms and services must accept.

**Status**: 🔧 IMPLEMENTED

**Promise Theory Alignment**: Implements the invitation pattern. Acceptance relationship established BEFORE specific proposals.

**Swordsman Implementation**: MyTerms Swordsman presents terms to sites, enforces acceptance before data exchange.

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

## 9. Compression & Encoding

### Spell
**Definition**: Compressed symbolic representation of complex concepts using emoji-based semantic notation.

**Status**: ✅ CANONICAL

**Promise Theory Alignment**: Spells are coordination promises. Using spell notation = promising to interpret it according to shared semantics.

**Compression Ratio**: 70:1 to 125:1 (concept density vs. expanded explanation)

**Example**: ⚔️ ⊥ 🧙 | 😊 = "Swordsman and Mage are conditionally independent given the First Person"

---

### Master Inscription
**Definition**: The foundational spell encoding the core architectural principle.

**Status**: ✅ CANONICAL

**Form**: ⚔️ ⊥ 🧙 | 😊

**Meaning**: "Separation between Swordsman and Mage preserves the First Person"

**Promise Theory Reading**: "The irreducible promise of conditional independence, given First Person authorization"

---

### Story Fracture, Principle Convergence
**Definition**: The phenomenon where different contexts produce different narratives that nonetheless converge on the same underlying principles.

**Status**: ✅ CANONICAL

**Application**: Two people reading the same spellbook form different proverbs (story fracture) but the same spell notation (principle convergence). This proves genuine comprehension vs. surface copying.

**VRC Formation**: Matching convergence despite fractured stories = proof of bilateral understanding.

---

## 10. Spellbook & Narrative

### Spellbook
**Definition**: Source material for learning, structured as 13 Acts, plus 30 tales in Zero Spellbook.

**Status**: ✅ CANONICAL

**Promise Theory Alignment**: The spellbook is a promise body—content being offered. RPP assessment determines if the promise (knowledge transfer) was kept.

**Structure**:
- Acts 1-13: Progressive narrative (Act 13: The Book of Promise integrates Promise Theory)
- Zero Spellbook: 30 foundational tales

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

### Drake
**Definition**: Pattern-teaching entity in the Spellbook narrative. Teaches through relationship rather than instruction.

**Status**: ✅ CANONICAL (Spellbook context)

**Association**: Dragon tier participants may take on Drake-like teaching roles.

---

## 11. Topology & Structure

### Yggdrasil
**Definition**: The substrate of infinite possibility—the space from which all specific configurations emerge.

**Status**: ✅ CANONICAL (Spellbook topology)

**Symbol**: 🌳

**Role**: Represents pre-measurement potential. Swordsman's measurement collapses Yggdrasil into specific reality.

---

### Tetrahedral Emergence
**Definition**: Hypothesis that the dual-agent gap generates two additional emergent properties (Reflect and Connect), creating a four-property sovereignty architecture.

**Status**: 🔬 SPECULATIVE (5% confidence)

**Components**:
- Swordsman (⚔️): Protection
- Mage (🧙): Delegation
- Reflect (🪞): Temporal memory (emergent)
- Connect (🕸️): Network effects (emergent)

**Promise Theory Consideration**: Would require N=4 agents with O(16) interior promises. Only justified if emergent properties provide sufficient value.

---

## 12. Symbolic Notation

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

### State & Value
| Symbol | Meaning |
|--------|---------|
| 🌀 | Spiral, golden ratio, balanced sovereignty |
| 🪞 | Mirror, reconstruction, observation |
| 💰 | 7th capital, behavioral value |
| 🐉 | Dragon tier, elite status |
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

## 13. Abbreviations & Acronyms

### Core Protocol
| Abbrev | Full Term |
|--------|-----------|
| RPP | Relationship Proverb Protocol |
| VRC | Verifiable Relationship Credential |
| ZKP | Zero-Knowledge Proof |
| TSP | Trust Spanning Protocol |
| PT | Promise Theory |

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

## 14. Forbidden Terms

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

## 15. Cross-Document Reference

### Primary Documents (Aligned Versions)

| Document | Version | Focus | Key Terms |
|----------|---------|-------|-----------|
| **This Glossary** | 2.2 | Terminology standardization | All canonical definitions |
| **Promise Theory Reference** | 1.0 | PT foundations | Autonomy, Assessment, Superagent, Irreducible |
| **Whitepaper** | 4.4 | Architecture, RPP, practical systems | Dual Agents, Separation, VRC, Chronicles, MyTerms |
| **Research Paper** | 3.2 | Mathematical foundations, proofs | Theorems 3.1-3.4, Reconstruction Ceiling, Error Floor |
| **Tokenomics** | 2.0 | Economic architecture | SWORD, MAGE, Ceremony, Signal, Guardian, 61.8/38.2 Split |
| **Spellbook** | 4.0.1-canonical | Narrative, symbolic system | Soulbis, Soulbae, Acts, Tales, Spells |
| **Visual Guide** | 1.1 | Diagrams, flows | Status indicators, architecture diagrams |
| **Research Proposal** | 1.2 | Collaboration invitation | Confidence levels, validation needs |

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
| Reconstruction Ceiling | Research Paper v3.2 §3.2 | Whitepaper v4.4, Tokenomics v2.0 |
| VRC Formation | Whitepaper v4.4 | Spellbook v4.0.1, Tokenomics v2.0 |
| 61.8/38.2 Split | Tokenomics v2.0 | This Glossary v2.2 |
| Guardian | Tokenomics v2.0 | Whitepaper v4.4 |
| Spells | Spellbook v4.0.1 | Whitepaper v4.4, Visual Guide v1.1 |
| Trust Tiers | Tokenomics v2.0 | Whitepaper v4.4, This Glossary v2.2 |
| Tetrahedral | Whitepaper v4.4 | Research Proposal v1.2 |
| Golden Ratio | Research Paper v3.2 | Tokenomics v2.0 |
| Ceremony vs Signal | This Glossary v2.2 | Tokenomics v2.0 |
| **Promise Theory Foundations** | Promise Theory Ref v1.0 | This Glossary v2.2, Whitepaper v4.4 |
| **Autonomy Axiom** | Promise Theory Ref v1.0 | This Glossary v2.2 |
| **Irreducible Promise** | Promise Theory Ref v1.0 | This Glossary v2.2 |
| **Assessment** | Promise Theory Ref v1.0 | This Glossary v2.2 |

### Citation Format

When referencing across documents, use:
- `[Whitepaper v4.4, §Section]`
- `[Research Paper v3.2, Theorem 3.2]`
- `[Glossary v2.2, Term Name]`
- `[Spellbook v4.0.1, Act N]`
- `[Promise Theory Ref v1.0, §Section]`
- `[Bergstra & Burgess (2019), §Chapter.Section]`

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Nov 20, 2025 | Initial comprehensive glossary |
| 2.0 | Nov 25, 2025 | Major expansion: ZKP terms, protocol standards, status indicators, cross-references, topology section, compression ratios |
| 2.1 | Nov 25, 2025 | Coherence update: Aligned all cross-document version references |
| **2.2** | **Dec 11, 2025** | **Promise Theory integration: Added §3 Promise Theory Foundations, PT alignments throughout existing terms, Superagent definition, notation extensions, new cross-references** |

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
