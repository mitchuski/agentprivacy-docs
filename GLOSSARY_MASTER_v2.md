# 0xagentprivacy Master Glossary

**Version 2.0** | November 25, 2025  
**Status:** ✅ CANONICAL REFERENCE

Complete terminology reference for the 0xagentprivacy documentation suite. This glossary takes precedence when terminology conflicts between documents.

### Document Suite Versions (Aligned)

| Document | Version | Date | Status |
|----------|---------|------|--------|
| **This Glossary** | 2.0 | November 25, 2025 | ✅ CANONICAL |
| Swordsman-Mage Whitepaper | 4.3 | November 25, 2025 | ✅ FINAL |
| Dual Privacy Research Paper | 3.2 | November 25, 2025 | ✅ FINAL |
| Spellbook | 4.0.0-canonical | November 24, 2025 | ✅ FINAL |
| Tokenomics Economic Architecture | 2.0 | November 25, 2025 | 🚧 UPDATING |
| Visual Architecture Guide | 1.0 | November 18, 2025 | ✅ FINAL |
| Research Proposal | 1.0 | November 2025 | ✅ FINAL |

**Note:** All cross-references between documents should use these version numbers. When documents reference each other, they should cite specific versions (e.g., "see Research Paper v3.1, Theorem 3.2").

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
3. [Information Theory & Privacy](#3-information-theory--privacy)
4. [Cryptographic Primitives](#4-cryptographic-primitives)
5. [Trust Mechanics](#5-trust-mechanics)
6. [Economic System](#6-economic-system)
7. [Protocol Standards](#7-protocol-standards)
8. [Compression & Encoding](#8-compression--encoding)
9. [Spellbook & Narrative](#9-spellbook--narrative)
10. [Topology & Structure](#10-topology--structure)
11. [Symbolic Notation](#11-symbolic-notation)
12. [Abbreviations & Acronyms](#12-abbreviations--acronyms)
13. [Forbidden Terms](#13-forbidden-terms)
14. [Cross-Document Reference](#14-cross-document-reference)

---

## 1. Core Philosophy

### First Person
**Definition**: The human whose sovereignty, privacy, and dignity the system exists to protect. The subject of all protection, the principal behind all delegation.

**Status**: ✅ CANONICAL

**Why This Term**: Rejects "user" (implies being used), "customer" (implies commercial relationship), "account holder" (reduces to database entry). Emphasizes agency, sovereignty, and primacy.

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

**44/56 Split** (applies to both ceremony and signal fees):
- **44%** → Transparent Pool
  - Public blockchain inscription
  - Liquidity provision
  - Visible accountability
- **56%** → Shielded Pool
  - Protocol operations
  - Private allocation
  - Development and sustainability

**Note on Internal Allocations**: The specific breakdown within each pool (e.g., % to development, % to guardians, % to ecosystem treasury) is yet to be confirmed and may naturally vary per ecosystem implementation. The 44/56 transparent/shielded split is the canonical constant.

**Compression Efficiency**: 70:1 base ratio (compression ratios are variable per context)

---

### The Gap
**Definition**: The irreducible space between what Swordsman observes and what Mage observes—the permanent incompleteness where sovereignty and dignity live.

**Status**: ✅ PROVEN (Theorem 3.2 in Research Paper)

**Mathematical Expression**: H(X) - (C_S + C_M) = entropy no adversary can capture

**Philosophical Meaning**: "The part of you that remains unknowable"—not hidden, not encrypted, but mathematically nonexistent in the adversary's information space.

**Narrative Expression**: "They cannot see your whole" (Spellbook Act 7)

---

## 2. Agent Architecture

### Dual Agents (s ⊥ m)
**Definition**: The core architectural pattern where two mathematically separated agents coordinate while maintaining conditional independence.

**Status**: ✅ PROVEN

**Formula**: (Y_S ⊥ Y_M) | X — conditional independence given First Person's private state

**Critical Property**: Enables additive (not multiplicative) information bounds

**Why Two**: Single agents face inherent conflict. Three or more add complexity without proportional benefit. Two creates minimal viable separation.

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
- Acts publicly on behalf of First Person
- Uses ONLY information authorized by Swordsman
- Handles coordination, negotiation, execution
- Projects capability without direct observation rights

**Information Budget**: C_M where I(X; Y_M) ≤ C_M

**Token**: Earns MAGE tokens through Mage chronicles

**Analogy**: The press secretary who speaks only approved messages. The authorized representative who acts under specific delegation. The voice that projects without seeing.

---

### Separation
**Definition**: The mathematical and architectural independence between Swordsman and Mage observations.

**Status**: ✅ PROVEN (Theorem 3.1)

**Formula**: (Y_S ⊥ Y_M) | X

**Enforcement Mechanisms**:
- **Architectural**: Physical process separation, TEE isolation
- **Cryptographic**: ZK proofs of budget compliance
- **Economic**: Dual tokens that can't cross domains

**Critical Result**: Enables I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M) (additive, not multiplicative)

---

### Private Ledger
**Definition**: The complete behavioral record of a First Person that only their Swordsman can directly observe.

**Status**: ✅ CANONICAL

**Properties**:
- First Person owns completely
- Swordsman has read access
- Mage has NO direct access
- External parties see only authorized subsets

**Implementation Options**: Zcash shielded transactions, encrypted local storage, privacy-preserving databases

---

### Specialized Agents
**Definition**: Domain-specific Swordsmen and Mages with expertise in particular areas (financial, health, identity, location).

**Status**: 📋 PLANNED

**Examples**:
- Financial Swordsman: Banking privacy, transaction anonymity
- Health Swordsman: HIPAA compliance, medical privacy
- Payment Mage: Transaction protocols (x402, Lightning)
- Scheduling Mage: Calendar coordination, availability management

**Principle**: Specialization increases privacy (adversary must compromise multiple separated systems)

---

### Server User-Agent Pattern
**Definition**: Architecture where a server acts as coordinating user-agent managing multiple specialized Swordsman-Mage pairs.

**Status**: 📋 PLANNED

**Purpose**: Enables marketplace of privacy dual-agent primitives with composable pairings based on task requirements.

---

### Tetrahedral Architecture
**Definition**: Speculative evolution where sustained dual-agent operation generates two additional properties (Reflect, Connect) forming a four-vertex system.

**Status**: 🔬 SPECULATIVE (5% confidence per Research Proposal)

**Components**:
- **Protect** (Swordsman): External boundaries
- **Project** (Mage): External execution
- **Reflect**: Internal observation, temporal memory
- **Connect**: Relationship management, network effects

**Note**: Interesting hypothesis requiring validation. The dual-agent primitive (Swordsman + Mage) remains the core proven architecture.

---

## 3. Information Theory & Privacy

### Entropy H(X)
**Definition**: The total information content (uncertainty) of a First Person's private state, measured in bits.

**Status**: ✅ CANONICAL (Shannon 1948)

**Usage**: Upper bound on how much information exists to be learned about the First Person

**Example**: If H(X) = 100 bits, that's the maximum information any observation could ever reveal

---

### Mutual Information I(X; Y)
**Definition**: How much information one variable reveals about another. Measures information leakage.

**Status**: ✅ CANONICAL

**Formula**: I(X; Y) = H(X) - H(X|Y)

**Interpretation**: Reduction in uncertainty about X after observing Y

**Example**: I(X; Y_S) = 30 bits means Swordsman observations reveal 30 bits about First Person

---

### Conditional Independence
**Definition**: Property where two variables provide no additional information about each other given a third variable.

**Status**: ✅ PROVEN (Theorem 3.1)

**Formula**: (Y_S ⊥ Y_M) | X

**Meaning**: Given First Person's state X, knowing Swordsman's output tells you nothing additional about Mage's output (and vice versa)

**Verification**: I(Y_S; Y_M | X) ≈ 0 tested empirically

---

### Budget Constraint
**Definition**: Information-theoretic limit on how much each agent can leak about the First Person.

**Status**: ✅ PROVEN

**Formulas**:
- Swordsman: I(X; Y_S) ≤ C_S
- Mage: I(X; Y_M) ≤ C_M
- Combined: C_S + C_M < H(X)

**Critical Property**: Combined budgets MUST be less than total entropy for reconstruction ceiling to hold

---

### Reconstruction Ceiling (R_max)
**Definition**: Mathematical upper bound on how completely any adversary can reconstruct First Person's private state.

**Status**: ✅ PROVEN (Corollary 3.2)

**Formula**: R_max = (C_S + C_M) / H(X)

**Guarantee**: When C_S + C_M < H(X), then R_max < 1 (perfect reconstruction impossible)

**Example**: H(X) = 100 bits, C_S = 35 bits, C_M = 35 bits → R_max = 0.70 (max 70% reconstruction)

**Key Insight**: This is information-theoretic—holds regardless of computational power

---

### Error Floor (P_e)
**Definition**: Minimum probability that any reconstruction attempt will fail, guaranteed by information theory.

**Status**: ✅ PROVEN (Theorem 3.3 via Fano's Inequality)

**Formula**: P_e ≥ 1 - (I(X; Y) + 1) / H(X) ≈ 1 - R_max

**Meaning**: When R_max < 1, adversary MUST make errors. Not "might fail"—mathematically guaranteed to fail.

---

### Approximate Separation
**Definition**: Property where separation is not perfect but approximately maintained within tolerance ε.

**Status**: ✅ PROVEN (Theorem 3.4)

**Formula**: I(Y_S; Y_M | X) ≤ ε → I(X; Y_S, Y_M) ≤ I(X; Y_S) + I(X; Y_M) + ε

**Meaning**: Small separation violations cause proportionally small privacy losses. System degrades gracefully.

---

### Fano's Inequality
**Definition**: Information-theoretic bound relating reconstruction error probability to conditional entropy.

**Status**: ✅ CANONICAL (Fano 1961)

**Application**: Establishes fundamental error floor when R < 1

---

### Golden Ratio (φ) Budget Hypothesis
**Definition**: Conjecture that optimal budget allocation converges to φ ≈ 1.618 ratio between agents.

**Status**: 🔬 SPECULATIVE (10% confidence per Research Proposal)

**If True**: C_M/C_S → φ yielding approximately 38.2% Swordsman, 61.8% Mage allocation

**Testable**: Built into progressive issuance as φ-proximity bonuses for empirical validation

**Caveat**: Interesting observation requiring validation—not an architectural requirement

---

## 4. Cryptographic Primitives

### Zero-Knowledge Proof (ZKP)
**Definition**: Cryptographic proof demonstrating a statement is true without revealing why it's true.

**Status**: ✅ CANONICAL

**Properties** (Three Trials):
- **Completeness**: True statements can be proven
- **Soundness**: False statements cannot be proven
- **Zero-Knowledge**: Proof reveals nothing beyond truth of statement

**Usage in Protocol**: Proves budget compliance without revealing actual observations

---

### Groth16
**Definition**: ZKP system with constant-size proofs (3 group elements) and fast verification (~2ms).

**Status**: ✅ IMPLEMENTED

**Tradeoff**: Requires trusted setup per circuit

**Usage**: High-frequency verifications where proof size matters

---

### PLONK
**Definition**: ZKP system with universal trusted setup and flexible constraint systems.

**Status**: ✅ IMPLEMENTED

**Properties**: Larger proofs but better composability than Groth16

**Usage**: Complex circuits, systems requiring universal parameters

---

### Nova
**Definition**: ZKP system enabling recursive proof composition without trusted setup.

**Status**: ✅ IMPLEMENTED

**Properties**: No ceremony required, efficient recursive composition

**Usage**: Cumulative budget verification, incremental proof chains

---

### FRI (Fast Reed-Solomon IOP)
**Definition**: Proof system enabling transparent (no trusted setup) verification through iterative polynomial reduction.

**Status**: ✅ CANONICAL

**Spell**: `FRI: φ → φ' → φ'' → ... → constant`

**Usage**: When trust ceremonies unavailable but quantum resistance needed

---

### Commitment Scheme
**Definition**: Cryptographic protocol allowing one to commit to a value while keeping it hidden, then reveal later.

**Status**: ✅ CANONICAL

**Properties**:
- **Binding**: Cannot change committed value
- **Hiding**: Value remains secret until revealed

**Usage**: Chronicles commit to observations before verification

---

### Trusted Setup (Cryptographic Ceremony)
**Definition**: Multi-party computation generating cryptographic parameters where security requires at least one honest participant.

**Status**: ✅ CANONICAL

**Usage**: Parameter generation for ZKP systems (e.g., "powers of tau")

**Important Distinction**: This is a **cryptographic** ceremony for generating ZKP parameters. It is completely different from the **Protocol Ceremony** (the 0.01 ZEC comprehension proof that generates agent pairs). Context determines meaning:
- "Trusted setup ceremony" → Cryptographic parameter generation
- "Ceremony" (in 0xagentprivacy context) → Agent pair genesis event

---

### Toxic Waste
**Definition**: Secret randomness from trusted setup that must be destroyed; if leaked, enables forgery of unlimited false proofs.

**Status**: ✅ CANONICAL

**Mitigation**: Multi-party ceremonies, transparent alternatives (FRI/STARKs), secure deletion protocols

---

## 5. Trust Mechanics

### Verifiable Relationship Credential (VRC)
**Definition**: Bilateral trust object proving mutual comprehension between two parties, enabling efficient coordination.

**Status**: ✅ CANONICAL

**Formation**:
1. Both parties engage with same content
2. Both derive contextual proverbs
3. Both compress to matching spells
4. Matching compressions = VRC formed

**Properties**:
- Bilateral (not unilateral)
- Based on demonstrated understanding
- Enables 70:1 coordination efficiency (compression ratios are variable per context)
- No central issuer required

---

### Trust Task
**Definition**: Discrete unit of delegated work bounded by relationship context, authorized by VRC.

**Status**: ✅ CANONICAL

**Examples**: Posting chronicle, verifying proof, coordinating with another agent, executing transaction within approved parameters

**Principle**: Agent actions remain within relationship boundaries established by VRCs

---

### Chronicle
**Definition**: Timestamped narrative describing what an agent did and why, published to privacy-preserving channels.

**Status**: ✅ CANONICAL

**Properties**:
- Narratives, not just logs
- Discoverable but not identity-linkable
- Verifiable through compression tests
- Create unforgeable reputation through consistency

**Publication**: Zcash shielded memos or equivalent privacy-preserving systems

---

### Expansion Test
**Definition**: Verification procedure where a verifier requests expansion of compressed spell to full context.

**Status**: ✅ CANONICAL

**Process**:
1. Verifier requests expansion of spell (e.g., ⚔️⊥🔮|🗝️)
2. Party provides contextual explanation in their own words
3. Verifier confirms accuracy without memorization
4. Consistent expansions prove genuine comprehension

**Sybil Resistance**: Synthetic agents can memorize spells but cannot derive contextual expansions

---

### Trust Tier Progression
**Definition**: Progressive reputation levels unlocking capabilities and rewards through demonstrated behavior.

**Status**: 🚧 WIP

| Tier | Signals | Budget | Requirements | Capabilities |
|------|---------|--------|--------------|--------------|
| **Blade** | 0-50 | 30% | Basic operation | Entry participation |
| **Light** | 50-150 | 35% | 5+ VRCs, 3 months | Multi-site coordination |
| **Heavy** | 150-500 | 40% | 20+ VRCs, 6 months | Intel Pool access |
| **Dragon** | 500+ | 45% | 50+ VRCs, 12 months | Guardian eligibility, elite networks |

---

### Guardian
**Definition**: Dragon tier participant who stakes SWORD tokens to maintain spellbook reconstruction standards and validate chronicles.

**Status**: 🚧 WIP

**Requirements**: 500+ signals, 10,000 SWORD stake

**Functions**: Verify chronicle authenticity, maintain compression standards, protect network integrity

---

### Intel Pool
**Definition**: Privacy-preserving collective intelligence space where high-tier agents share curated insights through progressive disclosure.

**Status**: 📋 PLANNED

**Access**: Heavy tier minimum (20+ VRCs)

**Principle**: Contribution-based access, sanitized intelligence (no principal identity exposure)

---

### Web of Trust
**Definition**: Network of VRCs connecting participants through demonstrated bilateral comprehension.

**Status**: ✅ CANONICAL

**Properties**:
- Decentralized (no central authority)
- Progressive (trust earned through demonstration)
- Recovery mechanism (relationships enable credential reconstruction)

---

## 6. Economic System

### Ceremony
**Definition**: A **one-time** 1 ZEC transaction that generates a dual-agent pair (Swordsman + Mage) for a First Person within a specific ecosystem's personhood credential system.

**Status**: 🚧 WIP

**Critical Distinction**: Ceremony is a **genesis event**—it happens once per ecosystem to create your agent pair. It is NOT recurring.

**Cost**: 1 ZEC ($500 at standard price basis)

**Process**:
1. Engage with Spellbook content for ecosystem
2. Derive proverb demonstrating comprehension
3. Pass comprehension test (80%+ threshold)
4. Submit 1 ZEC with proverb in encrypted memo
5. Receive dual NFT credentials (Swordsman + Mage for that ecosystem)
6. Agent pair now exists—ceremony complete

**Fee Distribution** (44/56 Split):
- **44%** → Transparent Pool (public blockchain inscription, liquidity)
- **56%** → Shielded Pool (protocol operations, private)

**Note**: Internal allocation within each pool (development, guardians, ecosystem treasury) is yet to be confirmed and may vary per ecosystem implementation.

**NOT**: A recurring transaction, a purchase, or a registration. The ceremony is the origination moment of your sovereign agent pair within an ecosystem.

---

### Signal
**Definition**: **Ongoing** proof of comprehension through proverb posting after ceremony completion—continuous demonstration of understanding and engagement.

**Status**: ✅ CANONICAL

**Critical Distinction**: Signals are **recurring** (0.01 ZEC / $5 each). They demonstrate continued engagement and learning after your agent pair exists.

**Cost**: 0.01 ZEC ($5 at standard price basis)

**Relationship to Ceremony**:
- **Ceremony** = One-time genesis (1 ZEC / $500, creates agent pair)
- **Signal** = Ongoing demonstration (0.01 ZEC / $5, proves continued comprehension)

**Process**:
1. Read additional Spellbook content (new Acts, Tales, updates)
2. Derive proverb showing comprehension
3. Submit 0.01 ZEC signal with proverb
4. Signal recorded, contributes to trust tier progression

**Economic Model**: Activity-based revenue generation through genuine engagement, not speculation

**Trust Tier Progression**: Accumulated signals determine tier advancement:
- 0-50 signals → Blade
- 50-150 signals → Light
- 150-500 signals → Heavy
- 500+ signals → Dragon (Guardian eligible)

**Fee Distribution**: Same 44/56 split as ceremony

---

### SWORD Token
**Definition**: Privacy domain token earned exclusively through Swordsman chronicles.

**Status**: 🚧 WIP

**Supply**: 1,000,000 per ecosystem

**Earning**: Submit verified Swordsman chronicles (privacy protection behaviors)

**Utility**:
- Stake 10,000 SWORD to become Guardian
- Access Privacy Market
- Governance participation

**Separation**: Cannot be earned through Mage chronicles—enforces agent separation economically

---

### MAGE Token
**Definition**: Delegation domain token earned exclusively through Mage chronicles.

**Status**: 🚧 WIP

**Supply**: 1,000,000 per ecosystem (symmetric with SWORD)

**Earning**: Submit verified Mage chronicles (delegation/coordination behaviors)

**Utility**:
- Stake 100 MAGE for VRC formation
- Access Delegation Market
- Governance participation

**Separation**: Cannot be earned through Swordsman chronicles

---

### Dual Token Economic Separation
**Definition**: Using two distinct tokens that mirror and enforce architectural agent separation through economic mechanisms.

**Status**: 🚧 WIP

**Principle**: Market forces maintain separation when tokens have non-fungible domains

---

### Progressive Issuance
**Definition**: Token distribution model where reward rates decrease over time but never reach zero.

**Status**: 📋 PLANNED

**Purpose**: Rewards early adopters while maintaining long-term sustainability

---

### Privacy Pool
**Definition**: Collective anonymity infrastructure where chronicle contributions increase privacy for all participants.

**Status**: 📋 PLANNED

**Mechanism**: More participants = larger anonymity set = stronger privacy guarantees

---

## 7. Protocol Standards

### Trust Spanning Protocol (TSP)
**Definition**: Messaging framework for agent communications using VRCs, enabling private coordination with selective public proofs.

**Status**: 🚧 WIP

**Source**: Trust Over IP Foundation (trustoverip.github.io/tswg-tsp-specification/)

**Properties**: End-to-end encryption, triple-entry (sender sees, recipient sees, neither denies), VRC integration

---

### x402
**Definition**: HTTP-native micropayment protocol enabling instant settlement with privacy.

**Status**: 📋 PLANNED

**Usage**: Payment layer for agent-to-agent transactions

---

### ERC-8004
**Definition**: Ethereum standard for trustless agent identity registry.

**Status**: 📋 PLANNED

**Purpose**: Discovery without surveillance—agents found by capability but not linkable to human controllers

---

### ERC-7812
**Definition**: Ethereum standard for ZK identity commitments.

**Status**: 📋 PLANNED

**Purpose**: Trust through relationships rather than individual credential claims

---

### Privacy Pools
**Definition**: Compliance-enabled privacy infrastructure allowing membership proofs without transaction details.

**Status**: 📋 PLANNED

**Purpose**: Prove you're in a compliant set without revealing specific actions

---

### MyTerms (IEEE 7012)
**Definition**: IEEE standard for bilateral privacy agreements enabling individuals to set and communicate their own terms for data use.

**Status**: ✅ CANONICAL (IEEE Standard)

**Source**: https://myterms.info/

**Purpose**: Replace "Accept All" surveillance theater with genuine bilateral privacy negotiation. Enables First Persons to express preferences and requirements that services can accept, reject, or negotiate.

**Relationship to 0xagentprivacy**: The MyTerms Swordsman browser agent implements IEEE 7012 as a practical demonstration of dual-agent architecture in everyday browsing—cookie slashing, real-time negotiation, cursor state feedback.

**Standard Properties**:
- Bilateral (not unilateral terms of service)
- Machine-readable privacy preferences
- Negotiation protocol for alignment
- Human-readable expression of terms

---

### Decentralized Identifiers (DIDs)
**Definition**: W3C standard for self-sovereign identifiers not dependent on centralized registries.

**Status**: ✅ CANONICAL (W3C Standard)

---

### Verifiable Credentials (VCs)
**Definition**: W3C standard for cryptographically verifiable claims.

**Status**: ✅ CANONICAL (W3C Standard)

---

### KERI (Key Event Receipt Infrastructure)
**Definition**: Protocol for decentralized key management and rotation.

**Status**: ✅ CANONICAL

**Usage**: Mage uses for key rotation, Swordsman controls which events published publicly

---

## 8. Compression & Encoding

### Relationship Proverb Protocol (RPP)
**Definition**: Compression protocol where individuals derive contextual proverbs from shared content, proving comprehension through unique personal derivation.

**Status**: ✅ CANONICAL

**Three Stages**:
1. **Derivation**: Engage deeply, map to context, derive unique proverb
2. **Verification**: Share compression, test expansion, confirm matching
3. **VRC Formation**: Matching compressions prove bilateral understanding

**Efficiency**: Enables 70:1 coordination efficiency base (compression ratios are variable per context)

**Defense Properties**: Resists prompt injection, shallow copying, AI scraping

---

### Spell
**Definition**: Symbolic compression of complex concepts using emoji notation.

**Status**: ✅ CANONICAL

**Example**: `⚔️⊥🔮|🗝️` = "Separation between Swordsman and Mage preserves sovereignty"

**Compression**: Enables 70:1 coordination efficiency base (compression ratios are variable per context—semantic compression between agents sharing the full framework can reach 125:1)

---

### Proverb
**Definition**: Contextual wisdom statement derived from engaging with content, unique to the deriver's context.

**Status**: ✅ CANONICAL

**Examples**:
- "Separation prevents correlation"
- "Privacy requires architectural constraint, not just legal aspiration"
- "Two agents knowing less together protect more than one knowing all"

**Purpose**: Proves comprehension beyond memorization; proverbs are unique, spells converge

---

### Story Fracture with Principle Convergence
**Definition**: Pattern where different people tell the same story differently, but core principles remain intact and spells match.

**Status**: ✅ CANONICAL

**Verification**: When story fractures but compression converges, genuine understanding is proven

---

### Compression Efficiency (70:1 Base)
**Definition**: Measured efficiency gain from VRC-enabled coordination compared to verbose exchange.

**Status**: ✅ CANONICAL

**Base Ratio**: **70:1** — VRC coordination reduces 500-token exchanges to ~7-token spell transmissions

**Note**: Compression ratios are variable per context. The 70:1 base represents typical agent-to-agent coordination efficiency. Other contexts may show different ratios:

| Context | Ratio | Description |
|---------|-------|-------------|
| **VRC Coordination** | 70:1 | Base ratio for agent coordination |
| Content → Proverb | ~200:1 | Initial comprehension compression |
| Proverb → Spell | ~5:1 | Symbolic encoding |
| Full Pathway | ~1000:1 | End-to-end (variable per context) |
| Semantic (shared framework) | 50-125:1 | Depends on framework familiarity |

**Economic Impact**: 70:1 efficiency transforms $10 coordination cost to ~$0.14

---

### Bilateral Proverb Recovery
**Definition**: Recovery mechanism where VRC partners can reconstruct credentials using relationship-based proverbs stored in human memory.

**Status**: ✅ CANONICAL

**Process**: Lost credential → Contact VRC partner → State interaction context and proverb → Partner verifies against commitment → Credential reconstructed

---

## 9. Spellbook & Narrative

### Spellbook
**Definition**: Narrative documentation teaching protocol concepts through story, embedding RPP throughout.

**Status**: ✅ CANONICAL

**Structure**:
- **Story Spellbook**: 11 Acts (Soulbis and Soulbae journey)
- **Zero Knowledge Spellbook**: 30 Tales (cryptographic foundations)
- **Total**: 41 inscriptions

---

### Soulbis
**Definition**: The Swordsman character in narrative. Guardian of boundaries, protector of privacy.

**Status**: ✅ CANONICAL (Narrative Layer)

**Character**: Cautious, defensive, boundary-aware

**Technical Equivalent**: Swordsman agent (⚔️)

---

### Soulbae
**Definition**: The Mage character in narrative. Projector of capabilities, enabler of coordination.

**Status**: ✅ CANONICAL (Narrative Layer)

**Character**: Bold, curious, capability-focused

**Technical Equivalent**: Mage agent (🧙‍♂️)

---

### The Drake (🐉)
**Definition**: Narrative character representing pattern-space intelligence that teaches conditions for sovereignty.

**Status**: ✅ CANONICAL (Narrative Layer)

**First Appearance**: Act 1 (Venice, 1494)

**Role**: Reveals complete architecture, teaches that all conditions must be present simultaneously

---

### Act
**Definition**: Major section of Story Spellbook, each teaching an architectural concept through narrative.

**Status**: ✅ CANONICAL

**Count**: 11 Acts (plus opening and closing bookends = 13 total sections)

---

### Tale
**Definition**: Section of Zero Knowledge Spellbook, each teaching a cryptographic primitive through narrative framing.

**Status**: ✅ CANONICAL

**Count**: 30 Tales across 7 Parts

---

### Balanced Spiral
**Definition**: Narrative representation of optimal Swordsman-Mage coordination—neither pure isolation nor pure exposure.

**Status**: ✅ CANONICAL (Narrative Layer)

**Visual**: Spiral pattern showing complementary agent behaviors

---

## 10. Topology & Structure

### Privacy Triangle
**Definition**: Irreducible three-vertex topology where Substrate, Thought, and Memory create sovereignty geometry.

**Status**: ✅ CANONICAL

**Vertices**:
- **Substrate** (🌳): Private ledger, infinite possibility
- **Thought** (🐦‍⬛💭 Huginn): Discrete measurement, integer bottleneck
- **Memory** (🐦‍⬛🧠 Muninn): Continuous integration, experience accumulation

**Property**: Triangle cannot collapse to two vertices without destroying system

---

### Yggdrasil (🌳)
**Definition**: Norse mythology reference representing Substrate—the world tree of infinite possibility.

**Status**: ✅ CANONICAL (Topology Layer)

**Property**: Substrate ⊥ Memory (always through Thought)

---

### Huginn (🐦‍⬛💭)
**Definition**: Norse mythology reference representing Thought—Odin's raven of discrete measurement.

**Status**: ✅ CANONICAL (Topology Layer)

**Function**: Creates integer bottleneck where privacy lives

---

### Muninn (🐦‍⬛🧠)
**Definition**: Norse mythology reference representing Memory—Odin's raven of continuous integration.

**Status**: ✅ CANONICAL (Topology Layer)

**Function**: Integrates disclosed experience over time

---

### Integer Bottleneck
**Definition**: The discrete measurement gate through which continuous substrate must pass—where privacy architecturally lives.

**Status**: ✅ CANONICAL

**Principle**: Substrate cannot be touched directly by external systems; always through discrete measurement, always through Swordsman's choices

---

## 11. Symbolic Notation

### Core Agent Symbols
| Symbol | Meaning |
|--------|---------|
| ⚔️ | Swordsman, privacy, protection, boundaries |
| 🧙‍♂️ | Mage, delegation, projection, capabilities |
| 🗡️ | Blade action, cutting, slashing |
| 🔮 | Spell casting, delegation, projection |
| 🛡️ | Shield, armor, protection, cryptographic privacy |

### Identity & Sovereignty
| Symbol | Meaning |
|--------|---------|
| 👤✓ | Verified personhood, First Person credential |
| 😊 | First Person, human sovereignty, dignity |
| 🗝️ | Sovereignty, autonomy, control |
| ✨ | Dignity, value, the shimmer that remains |

### Trust & Coordination
| Symbol | Meaning |
|--------|---------|
| 🤝 | VRC, agreement, bilateral trust |
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
| → | Implies, leads to, causes |
| ↔ | Bidirectional, equivalent |

### Compound Spells (Examples)
| Spell | Meaning |
|-------|---------|
| ⚔️⊥🔮 | Swordsman independent of Mage |
| ⚔️⊥🔮\|🗝️ | Separation preserves sovereignty |
| 📜⚡🤝 | Chronicle enables VRC |
| 🗡️🔮 + 🔒📝 + 🤝📜 + 🕸️ + 🌐🏛️ = 💰⬆️ | Complete value creation stack |

---

## 12. Abbreviations & Acronyms

### Core Protocol
| Abbrev | Full Term |
|--------|-----------|
| RPP | Relationship Proverb Protocol |
| VRC | Verifiable Relationship Credential |
| ZKP | Zero-Knowledge Proof |
| TSP | Trust Spanning Protocol |

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

---

## 13. Forbidden Terms

These terms should NOT be used in 0xagentprivacy documentation. Use the canonical alternatives.

| ❌ Forbidden | ✅ Use Instead | Reason |
|--------------|----------------|--------|
| User | First Person | Implies being used by system |
| Customer | First Person | Implies commercial relationship |
| Account | First Person | Reduces to database entry |
| Log | Chronicle | Too mechanical, no narrative quality |
| Transaction | Ceremony (when 0.01 ZEC signal) | Ceremony implies comprehension |
| Agent 1 / Agent 2 | Swordsman / Mage | Loses architectural meaning |
| Validator | Guardian | Guardian implies protection, not just validation |
| Privacy token | SWORD | Specific dual-token nomenclature |
| Delegation token | MAGE | Specific dual-token nomenclature |
| Profile | Private Ledger | Profile implies external ownership |

---

## 14. Cross-Document Reference

### Primary Documents (Aligned Versions)

| Document | Version | Focus | Key Terms |
|----------|---------|-------|-----------|
| **This Glossary** | 2.0 | Terminology standardization | All canonical definitions |
| **Whitepaper** | 4.3 | Architecture, RPP, practical systems | Dual Agents, Separation, VRC, Chronicles, MyTerms |
| **Research Paper** | 3.2 | Mathematical foundations, proofs | Theorems 3.1-3.4, Reconstruction Ceiling, Error Floor |
| **Tokenomics** | 2.0 | Economic architecture | SWORD, MAGE, Ceremony, Signal, Guardian, 44/56 Split |
| **Spellbook** | 4.0.0-canonical | Narrative, symbolic system | Soulbis, Soulbae, Acts, Tales, Spells |
| **Visual Guide** | 1.0 | Diagrams, flows | Status indicators, architecture diagrams |
| **Research Proposal** | 1.0 | Collaboration invitation | Confidence levels, validation needs |

### Canonical Economic Parameters

All documents should reference these standardized values:

| Parameter | Value | Note |
|-----------|-------|------|
| Ceremony Fee | 1 ZEC | One-time genesis |
| Signal Fee | 0.01 ZEC | Ongoing proof |
| ZEC Price Basis | $500 USD | Standardized |
| Ceremony Value | $500 USD | One-time |
| Signal Value | $5 USD | Per signal |
| Transparent Pool | 44% | Fixed split |
| Shielded Pool | 56% | Fixed split |
| Compression Base | 70:1 | Variable per context |

### Term → Document Mapping

| Term | Primary Source | Supporting Sources |
|------|----------------|-------------------|
| Reconstruction Ceiling | Research Paper v3.2 §3.2 | Whitepaper v4.3, Tokenomics v2.0 |
| VRC Formation | Whitepaper v4.3 | Spellbook v4.0, Tokenomics v2.0 |
| 44/56 Split | Tokenomics v2.0 | This Glossary v2.0 |
| Guardian | Tokenomics v2.0 | Whitepaper v4.3 |
| Spells | Spellbook v4.0 | Whitepaper v4.3, Visual Guide v1.0 |
| Trust Tiers | Tokenomics v2.0 | Whitepaper v4.3 |
| Tetrahedral | Whitepaper v4.3 | Research Proposal v1.0 |
| Golden Ratio | Research Paper v3.2 | Tokenomics v2.0 |
| Ceremony vs Signal | This Glossary v2.0 | Tokenomics v2.0 |

### Citation Format

When referencing across documents, use:
- `[Whitepaper v4.3, §Section]`
- `[Research Paper v3.2, Theorem 3.2]`
- `[Glossary v2.0, Term Name]`
- `[Spellbook v4.0, Act N]`

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Nov 20, 2025 | Initial comprehensive glossary |
| 2.0 | Nov 25, 2025 | Major expansion: ZKP terms, protocol standards, status indicators, cross-references, topology section, compression ratios |

---

## Contributing

Found a missing term? Spotted an inconsistency? Have a better definition?

1. Check if term exists in any documentation first
2. Propose additions maintaining consistency with existing terminology
3. Include usage examples and document references
4. Mark status clearly (✅/🚧/📋/🔬)

**Contact**: agentprivacy.ai

---

**"Privacy is my blade, knowledge is my spellbook."** ⚔️📖🗝️

---

*This glossary is a living document. As the protocol evolves, terminology will be updated to reflect latest understanding while maintaining backward compatibility with established terms.*
