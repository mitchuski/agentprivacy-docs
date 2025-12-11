# Understanding as Key
## A Paper on Privacy-Preserving Trust Through Demonstrated Comprehension

*From the Signal to Sanctuary implementation at Zypherpunk Hack 2025*

**Version:** 1.0  
**Date:** December 1, 2025  
**Author:** privacymage / 0xagentprivacy  
**Status:** Living Document

**Document Alignment**: 
- [Whitepaper v4.4, §4.3 Private Proverb Inscription]
- [Spellbook v4.0.2-canonical, Part VI: The Recovery, Act 12: The Forgetting]
- [Tokenomics v2.1, §2.1 RPP as Economic Foundation]
- [Research Paper v3.2, §5 Reconstruction Ceiling]
- [Visual Architecture Guide v1.2]
- [Glossary v2.1]

**Whitepaper Integration**: This lite paper expands on the Private Proverb Inscription mechanism introduced in Whitepaper §4.3. It should be read as a companion specification, suitable for inclusion as **Appendix D** or as a standalone protocol document in the documentation suite.

---

> *"Your relationships become your backup. Meaning becomes your key."*

---

## The Core Insight

This transforms **"what you have"** (a stored secret) into **"what you understand"** (demonstrated comprehension).

The proverb piggybacks on natural human relational memory rather than fighting against cognitive architecture.

```
Traditional Authentication:          Proverb-Based Trust:
                                     
"What you have"                      "What you understand"
├── Seed phrases                     ├── Demonstrated comprehension
├── Private keys                     ├── Relational memory
├── Hardware tokens                  ├── Contextual meaning
├── Stored secrets                   ├── Bilateral understanding
│                                    │
└── Fights human memory              └── Works WITH human memory
    (random strings)                     (meaningful proverbs)
```

**Why this matters for adoption:**

Humans are terrible at remembering random strings. We lose seed phrases, forget passwords, misplace hardware tokens. The entire security industry is built on fighting against how human memory actually works.

But humans are excellent at remembering:
- Relationships and their contexts
- Meaningful phrases and their origins  
- Shared experiences and derived insights
- Stories and their lessons

The proverb protocol **aligns cryptographic security with cognitive architecture**. Recovery becomes a function of understanding, not recall of arbitrary data.

*This may have unlocked the adoption curve.*

---

## Overview

The Relationship Proverb Protocol (RPP) creates bilateral trust through demonstrated understanding. But how that understanding is committed onchain determines the privacy properties, recovery paths, and disclosure controls available to participants.

This document describes **three inscription paths**—symmetric, asymmetric, and interleaved—each serving different trust and recovery needs. The **Signal to Sanctuary** project at Zypherpunk Hack 2025 represents the first production implementation of these primitives on Zcash.

**Path 1 - Symmetric:** Both proverbs hidden in a single commitment hash. Maximum privacy, but recovery requires both parties.

**Path 2 - Asymmetric (Current Default):** The First Person's proverb is published visibly in the transparent pool inscription. The Sanctuary's response proverb remains hidden, committed only in the hash. This enables understanding-based recovery while keeping the bilateral relationship verifiable.

**Path 3 - Interleaved:** Proverbs fragment—first half of one combined with second half of the other across the visibility boundary. Neither party fully exposed, neither fully hidden. Mutual recovery.

---

## Table of Contents

### Preamble
- [The Core Insight](#the-core-insight) — From "what you have" to "what you understand"

### Part I: The Three Paths
1. [The Three Paths](#the-three-paths) — Overview diagram
2. [Path 1: Symmetric Inscription](#path-1-symmetric-inscription-maximum-privacy) — Maximum privacy
3. [Path 2: Asymmetric Inscription](#path-2-asymmetric-inscription-current-signal-to-sanctuary-default) — Current default
4. [Path 3: Interleaved Inscription](#path-3-interleaved-inscription-fragmented-commitment) — Fragmented commitment

### Part II: Visibility as Meaning
5. [Visibility as Relationship Style](#visibility-as-relationship-style) — The spectrum of disclosure
6. [The Visibility Ratio: φ-Derived Experiments](#the-visibility-ratio-φ-derived-experiments) — Golden ratio configurations

### Part III: VRC Ceremonies
7. [VRC Key Ceremonies Without Losing Privacy](#vrc-key-ceremonies-without-losing-privacy) — Privacy-preserving ceremonies
8. [Social Recovery Through Understanding](#social-recovery-through-understanding) — Meaning-based recovery
9. [Selective Disclosure](#selective-disclosure) — Controlling revelation

### Part IV: Security & Implementation
10. [Entropy and Security](#entropy-and-security) — Why proverbs aren't guessable
11. [Trust Tier Integration](#trust-tier-integration) — Progressive path recommendations
12. [Signal to Sanctuary: First Implementation](#signal-to-sanctuary-first-implementation) — Zcash production system
13. [Proverbiogenesis Connection](#proverbiogenesis-connection) — Becoming weather
14. [Implementation Notes](#implementation-notes) — Memo formats & endpoints

### Part V: Integration
15. [The Big Picture](#the-big-picture) — Summary
16. [Further Reading](#further-reading) — Cross-references
17. [Document Series](#document-series) — Full suite

---

## The Three Paths

```
                         PROVERB INSCRIPTION
                                │
           ┌────────────────────┼────────────────────┐
           │                    │                    │
           ▼                    ▼                    ▼
    ┌─────────────┐      ┌─────────────┐      ┌─────────────┐
    │  SYMMETRIC  │      │ ASYMMETRIC  │      │ INTERLEAVED │
    │  (Private)  │      │  (Public)   │      │ (Fragmented)│
    │             │      │             │      │             │
    │ 🔒📝 ↔ 🔒📝 │      │ 🔓📝 → 🔒🗝️ │      │ 🔓½📝 ↔ 🔒½🗝️│
    └─────────────┘      └─────────────┘      └─────────────┘
           │                    │                    │
    Both proverbs        FP visible,          Half each in
    hidden in hash       Sanctuary hidden     hash, half visible
           │                    │                    │
    Maximum privacy      Social recovery      Mutual recovery
    Minimum recovery     FP disclosure        Neither controls
```

---

## Path 1: Symmetric Inscription (Maximum Privacy)

**Notation:** `🔒📝 ↔ 🔒📝`

**Structure:**
```
hash(P_first_person ∥ P_sanctuary) → onchain
```

Both proverbs contribute equally to a single hash. Neither is distinguishable onchain. The commitment exists, but observers cannot determine:
- Which party initiated
- What either proverb contains
- Who the counterparties are

**Properties:**

| Property | Value |
|----------|-------|
| **First Person Privacy** | ✅ Complete |
| **Sanctuary Privacy** | ✅ Complete |
| **Recovery Path** | ❌ Requires both parties |
| **Selective Disclosure** | ❌ All-or-nothing |
| **Verification** | Requires both proverbs |

**Use Cases:**
- Maximum privacy relationships
- Blade-tier trust (early relationship)
- Situations where recovery is less critical than opacity
- When First Person wants no public trace of their understanding

---

## Path 2: Asymmetric Inscription (Current Signal to Sanctuary Default)

**Notation:** `🔓📝 → 🔒🗝️`

**Structure:**
```
P_first_person → onchain (visible in transparent pool)
hash(P_first_person ∥ P_sanctuary) → commitment
```

The First Person's proverb appears in cleartext onchain. The Sanctuary's response proverb remains private—committed in the hash but never published. The First Person accepts visibility in exchange for recovery properties.

**Properties:**

| Property | Value |
|----------|-------|
| **First Person Privacy** | ❌ Proverb visible onchain |
| **Sanctuary Privacy** | ✅ Response hidden in hash |
| **Recovery Path** | ✅ Through understanding |
| **Selective Disclosure** | ✅ First Person controls proof |
| **Verification** | FP proverb visible, Sanctuary proves relationship |

**Current Signal to Sanctuary Implementation:**

```
First Person → Oracle:
  [rpp-v1]
  [act-5-golden-split]
  [timestamp]
  [First Person's proverb]        ← Published in transparent pool

Oracle → First Person (shielded):
  [vrc-callback-v1]
  [Sanctuary's proverb response]  ← Hidden, only FP receives
  [re: act-5-golden-split]
  
Transparent Pool Inscription:
  First Person's proverb (visible)
  + hash(FP_proverb ∥ Sanctuary_proverb) (commitment)
```

**Use Cases:**
- Social recovery based on understanding
- Progressive trust relationships (Light, Heavy, Dragon tiers)
- Situations where recovery outweighs First Person opacity
- Building verifiable proof of engagement with spellbook content

---

## Path 3: Interleaved Inscription (Fragmented Commitment)

**Notation:** `🔓½📝 ↔ 🔒½🗝️`

**Structure:**
```
visible: P_fp[n/2:n] ∥ P_sanctuary[0:n/2]      (FP's ending + Sanctuary's beginning)
hidden:  hash(P_fp[0:n/2] ∥ P_sanctuary[n/2:n]) (FP's beginning + Sanctuary's ending)
```

The proverbs themselves fragment and **interweave**. Your ending with their beginning visible. Your beginning with their ending hidden. Neither party fully exposed, neither fully hidden.

**Visual:**
```
First Person's Proverb:    [===HIDDEN===][==VISIBLE==]
                                  ↘            ↙
                              INTERWEAVE
                                  ↗            ↖
Sanctuary's Proverb:       [==VISIBLE==][===HIDDEN===]

Visible onchain:  "...gates I choose" + "The mage who..."
Hidden in hash:   "Seventh capital flows through..." + "...receives guards as their own"
```

**Properties:**

| Property | Value |
|----------|-------|
| **First Person Privacy** | ⚖️ Partial (second half visible) |
| **Sanctuary Privacy** | ⚖️ Partial (first half visible) |
| **Recovery Path** | ✅ Requires understanding from BOTH |
| **Selective Disclosure** | ⚖️ Mutual—neither controls alone |
| **Verification** | Requires reconstruction from both halves |

**Why This Interweave Direction:**

The visible portion shows:
- How the First Person **concluded** their understanding
- How the Sanctuary **began** their response

The hidden portion protects:
- How the First Person **arrived** at their understanding
- How the Sanctuary **completed** their response

This creates a cryptographic "handshake"—you see where one ends and the other begins, but not the full journey of either.

**Why This Matters:**

Neither party can unilaterally prove or hide the relationship. Recovery requires:
1. First Person reconstructs their hidden beginning
2. Sanctuary reconstructs their hidden ending
3. Both halves combine to verify the commitment

This creates **mutual skin in the game**—the relationship is truly bilateral at the cryptographic level, not just the semantic level.

**φ-Derived Fragmentation:**
```
Instead of 50/50 split:

First Person:  [==38.2% HIDDEN==][===61.8% VISIBLE===]
Sanctuary:     [===61.8% VISIBLE===][==38.2% HIDDEN==]

Or inverted:

First Person:  [===61.8% HIDDEN===][==38.2% VISIBLE==]
Sanctuary:     [==38.2% VISIBLE==][===61.8% HIDDEN===]

The golden ratio governs the fragment boundary itself.
The direction of the φ-split signals relationship emphasis.
```

**Use Cases:**
- High-trust bilateral relationships (Heavy/Dragon tier)
- Situations requiring mutual recovery guarantees
- When neither party should have disclosure advantage
- Experimental: testing whether φ-split fragments have different properties than 50/50

---

## Visibility as Relationship Style

The amount you reveal isn't just a technical parameter—it's a **signal about the relationship itself**. The cryptographic commitment structure becomes semantic.

### The Spectrum

```
VISIBILITY SPECTRUM AS RELATIONSHIP STYLE
                           
0%        25%       38.2%      50%       61.8%      75%       100%
│          │          │         │          │          │          │
▼          ▼          ▼         ▼          ▼          ▼          ▼
┌──────────┬──────────┬─────────┬──────────┬──────────┬──────────┐
│ DISCRETE │ RESERVED │ BALANCED│ MUTUAL   │ OPEN     │ DECLARED │
│          │          │   (φ⁻¹) │          │   (φ)    │          │
└──────────┴──────────┴─────────┴──────────┴──────────┴──────────┘
     │          │          │         │          │          │
  Private    Guarded    Golden    Equal     Golden    Public
  affair     intimacy   privacy   exposure  openness  commitment
```

### Relationship Archetypes

| Visibility | Style | Signal | Recovery |
|------------|-------|--------|----------|
| **0%** (Symmetric) | Discrete | "This exists, but that's all you'll know" | Requires both parties |
| **~25%** | Reserved | "A hint of what we share" | Partial context, both needed |
| **38.2%** (φ⁻¹) | Balanced Privacy | "Privacy-first, but verifiable" | Meaning-recoverable with effort |
| **50%** | Mutual | "We're equally exposed" | Either party can begin recovery |
| **61.8%** (φ) | Balanced Openness | "Openness-first, but protected" | Understanding-recoverable |
| **~75%** | Declared | "Mostly visible commitment" | Easy recovery, minimal hidden |
| **100%** (Asymmetric) | Public | "My understanding is on record" | Full FP recovery from context |

### What You Signal

**0% Visible (Symmetric)**
```
"Our relationship is no one's business but ours."

Style: Discrete affair. Early courtship. Sensitive collaboration.
Signal: Maximum privacy. Neither reveals without the other.
Recovery: Both must participate. No unilateral proof.
```

**38.2% Visible (φ-Complement)**
```
"I value privacy, but I'm willing to be found."

Style: Guarded intimacy. Professional trust. Careful disclosure.
Signal: Privacy-weighted golden ratio. Recovery possible, not easy.
Recovery: Requires genuine understanding to reconstruct the hidden 61.8%.
```

**50% Visible (Interleaved Equal)**
```
"We share equally in exposure and protection."

Style: Mutual vulnerability. Partnership. Balanced power.
Signal: Neither has disclosure advantage. True bilateral.
Recovery: Either party's understanding can seed reconstruction.
```

**61.8% Visible (φ-Ratio)**
```
"I lean toward openness, but keep something sacred."

Style: Open relationship. Public collaboration. Visible trust.
Signal: Openness-weighted golden ratio. Easy to verify, hard to fake.
Recovery: Context-rich. The visible 61.8% provides strong recovery anchor.
```

**100% Visible (Asymmetric)**
```
"My commitment is public record. Yours remains protected."

Style: Declared allegiance. Public endorsement. One-way visibility.
Signal: First Person accepts full exposure. Sanctuary stays hidden.
Recovery: FP proverb always available. Sanctuary controls verification.
```

### The Golden Ratio Sweet Spots

The φ-derived points (38.2% and 61.8%) represent **natural equilibria**:

```
38.2% Visible (Privacy-Weighted):
├── 38.2% revealed → enough for recovery anchor
├── 61.8% hidden → enough for meaningful privacy
└── Optimal for: sensitive relationships, early trust, careful disclosure

61.8% Visible (Openness-Weighted):
├── 61.8% revealed → rich recovery context
├── 38.2% hidden → sacred core preserved
└── Optimal for: public collaborations, mature trust, verifiable commitment
```

**Hypothesis:** These φ-derived points may represent attractors—relationship styles that naturally stabilize at golden ratio visibility because they balance competing needs optimally.

### Choosing Your Style

```
ASK YOURSELF:

1. How much do I want observers to know about this relationship?
   0% ←──────────────────────────────────────────→ 100%
   Nothing                                    Everything

2. How important is unilateral recovery?
   0% ←──────────────────────────────────────────→ 100%
   Both needed                              Either can recover

3. Who should control disclosure?
   Symmetric ←────── Interleaved ──────→ Asymmetric
   Mutual control    Shared control       One party visible

4. What does this visibility level say about us?
   Discrete ←─────────────────────────────→ Declared
   Secret allies                          Public partners

YOUR VISIBILITY RATIO = f(privacy_need, recovery_need, power_balance, signal_intent)
```

### Progression Over Time

Relationships may evolve through visibility styles:

```
RELATIONSHIP LIFECYCLE:

Early:     0% → 25%      "Getting to know you, staying discrete"
Building:  25% → 38.2%   "Trust growing, still guarded"
Maturing:  38.2% → 50%   "Balanced mutual exposure"
Deepening: 50% → 61.8%   "Comfortable being seen together"
Committed: 61.8% → 100%  "Public declaration of relationship"

Each signal updates the onchain record.
History of visibility changes itself becomes meaningful.
```

### Notation Extension

Building on the emoji system:

| Visibility | Notation | Meaning |
|------------|----------|---------|
| 0% | `🔒📝 ↔ 🔒📝` | Symmetric, fully hidden |
| 25% | `🔒¾📝 ↔ 🔓¼🗝️` | Quarter visible |
| 38.2% | `🔒φ⁻¹📝 ↔ 🔓φ⁻¹🗝️` | Golden privacy |
| 50% | `🔓½📝 ↔ 🔒½🗝️` | Equal interleave |
| 61.8% | `🔓φ📝 ↔ 🔒φ🗝️` | Golden openness |
| 75% | `🔓¾📝 ↔ 🔒¼🗝️` | Three-quarter visible |
| 100% | `🔓📝 → 🔒🗝️` | Asymmetric, FP visible |

---

## The Visibility Ratio: φ-Derived Experiments

The choice between paths isn't just binary or ternary. The **golden ratio** (φ ≈ 1.618) that governs the transparent/shielded fee split may also govern visibility experiments across all three paths.

### Experimental Design Space

```
                    VISIBILITY SPECTRUM
                           
    Symmetric              Interleaved              Asymmetric
    (100% hidden)          (50/50 or φ)             (100% FP visible)
         │                      │                         │
         ├──────────────────────┼─────────────────────────┤
         │                      │                         │
         │     38.2%      ↔    50%    ↔     61.8%         │
         │   symmetric      interleaved    asymmetric     │
         │                      │                         │
         └──────────────────────┴─────────────────────────┘
                                │
                         φ-derived splits
```

### Potential Configurations

**Configuration A: Ecosystem-Level Split**
```
Of all inscriptions in an ecosystem:
├── 38.2% → Symmetric (both hidden)
├── 23.6% → Interleaved (mutual fragments)
└── 38.2% → Asymmetric (First Person visible)

Or simplified:
├── 61.8% → Asymmetric (recovery-enabled)
└── 38.2% → Symmetric (maximum privacy)

First Persons choose at signal time.
Ecosystem tracks aggregate ratio.
```

**Configuration B: Fragment-Level Split (Interleaved Path)**
```
Within the interleaved path itself:
├── 61.8% of First Person's proverb → visible
├── 38.2% of First Person's proverb → in hash
├── 38.2% of Sanctuary's proverb → visible  
└── 61.8% of Sanctuary's proverb → in hash

Golden ratio governs the fragment boundary.
```

**Configuration C: Temporal/Trust Tier Progression**
```
Trust tier progression:
├── Blade (early): 100% symmetric (maximum privacy while building trust)
├── Light: Asymmetric (recovery becomes option)
├── Heavy: Interleaved (mutual skin in game)
└── Dragon: Choice (earned the right to decide)
```

### Why φ?

The golden ratio appears throughout the architecture:
- 61.8% transparent / 38.2% shielded (fee distribution) [Tokenomics v2.1, §2.1]
- φ-proximity bonuses in progressive issuance [Tokenomics v2.1, §6]
- Conjectured optimal Swordsman/Mage budget allocation [Research Paper v3.2, §7]

Extending φ to visibility ratios maintains architectural coherence. The same mathematical harmony that balances economic flows may balance privacy/recovery tradeoffs.

**Status:** 🔬 EXPLORATORY — These ratios are experimental hypotheses, not proven optima. Signal to Sanctuary provides the infrastructure to test them.

---

## VRC Key Ceremonies Without Losing Privacy

Traditional key ceremonies require visible coordination—participants must reveal themselves to establish shared secrets. The proverb inscription paths enable **privacy-preserving VRC ceremonies** where relationships form without surveillance.

### The Problem with Traditional Ceremonies

```
Traditional Key Ceremony:
├── Participants must identify themselves
├── Coordination is visible to observers
├── Key material links to identities
├── Recovery requires centralized backup or m-of-n schemes
└── The ceremony itself creates a surveillance record
```

### Proverb-Based Ceremony Architecture

The visibility spectrum enables ceremonies where **understanding replaces identity**:

```
Proverb Ceremony (1 ZEC) [Tokenomics v2.1, §1.3]:
├── No identity disclosure required
├── Coordination through shared content engagement
├── Key material derived from bilateral proverbs
├── Recovery through meaning, not seed phrases
└── The ceremony creates only a commitment hash (or partial visibility by choice)
```

### Ceremony Types by Visibility

| Ceremony Type | Visibility | Use Case | Privacy Level |
|---------------|------------|----------|---------------|
| **Shadow Ceremony** | 0% (Symmetric) | Covert partnerships, sensitive alliances | Maximum |
| **Guarded Ceremony** | 38.2% | Professional relationships, early trust | High |
| **Balanced Ceremony** | 50% (Interleaved) | Partnerships, mutual accountability | Mutual |
| **Open Ceremony** | 61.8% | Public collaborations, verifiable trust | Moderate |
| **Declared Ceremony** | 100% (Asymmetric) | Public commitments, on-record relationships | Minimal (FP visible) |

### The Shadow Ceremony (Maximum Privacy)

For relationships that must remain invisible:

```
┌─────────────────────────────────────────┐
│         SHADOW CEREMONY (0%)            │
│                                         │
│ Both parties engage with same tale      │
│ Each derives proverb independently      │
│ Proverbs exchanged through private      │
│   channel (shielded memo, encrypted)    │
│                                         │
│ Onchain record:                         │
│   hash(P_fp ∥ P_sanctuary) only         │
│                                         │
│ Result:                                 │
│ • Relationship exists (hash proves)     │
│ • No party identifiable from chain      │
│ • Recovery requires both proverbs       │
│ • Perfect forward secrecy               │
└─────────────────────────────────────────┘
```

**Use Cases:**
- Whistleblower protection
- Sensitive collaborations
- Early-stage negotiations
- Relationships in hostile environments

### The Declared Ceremony (Verifiable Commitment)

For relationships meant to be seen:

```
┌─────────────────────────────────────────┐
│       DECLARED CEREMONY (100%)          │
│                                         │
│ First Person's proverb published        │
│ Sanctuary's response in hash            │
│                                         │
│ Onchain record:                         │
│   P_fp (visible)                        │
│   + hash(P_fp ∥ P_sanctuary)            │
│                                         │
│ Result:                                 │
│ • FP's understanding on record          │
│ • Sanctuary controls verification       │
│ • FP can always prove engagement        │
│ • Recovery from visible context         │
└─────────────────────────────────────────┘
```

**Use Cases:**
- Public endorsements
- Credential issuance
- Community membership
- On-record commitments

### The Interleaved Ceremony (Mutual Binding)

For relationships requiring balanced exposure:

```
┌─────────────────────────────────────────┐
│      INTERLEAVED CEREMONY (50%)         │
│                                         │
│ Each proverb fragments                  │
│ Halves interweave across visibility     │
│                                         │
│ Onchain record:                         │
│   P_fp[end] ∥ P_sanctuary[begin]        │
│   + hash(P_fp[begin] ∥ P_sanctuary[end])│
│                                         │
│ Result:                                 │
│ • Cryptographic handshake visible       │
│ • Neither fully exposed                 │
│ • Mutual recovery possible              │
│ • True bilateral commitment             │
└─────────────────────────────────────────┘
```

**Use Cases:**
- Business partnerships
- Mutual agreements
- Collaborative projects
- Balanced power relationships

### Key Derivation from Proverbs

The ceremony produces **relationship-specific keys** derived from bilateral understanding:

```
Key Derivation [Research Paper v3.2, §4]:

ceremony_key = KDF(
    hash(P_fp ∥ P_sanctuary),
    tale_id,
    timestamp,
    visibility_ratio
)

Properties:
├── Deterministic: Same inputs → same key
├── Bilateral: Requires both proverbs
├── Contextual: Bound to specific tale/time
├── Recoverable: Understanding regenerates proverbs → regenerates key
└── Private: Key never appears onchain, only commitment hash
```

### Ceremony Progression (Trust Ladder)

Relationships may evolve through ceremony types:

```
CEREMONY LIFECYCLE:

Signal Phase (0.01 ZEC each):
├── Multiple signals build trust tier [Tokenomics v2.1, §5]
├── Blade → Light → Heavy → Dragon progression
└── Each signal demonstrates continued understanding

Ceremony Phase (1 ZEC):
├── Formal bilateral commitment
├── VRC established with chosen visibility
├── Key material derived for future coordination
└── Relationship anchored on-chain

Evolution Phase:
├── May re-ceremony at different visibility
├── History of ceremonies becomes trust signal
├── Progressive revelation as trust deepens
└── Or progressive privacy as relationship matures
```

### Connection to Dual-Agent Architecture

The ceremony visibility maps to Swordsman/Mage separation [Whitepaper v4.4, §2]:

```
Visibility Level → Agent Emphasis

0% (Shadow):     Pure Swordsman domain
                 Maximum protection, minimum delegation
                 
50% (Interleaved): Balanced separation
                   Both agents equally involved
                   
100% (Declared):   Mage-enabled recovery
                   Delegation capability preserved
                   
The visibility ratio IS the privacy/delegation tradeoff
made concrete in cryptographic structure.
```

### Privacy Guarantees Preserved

Regardless of visibility level, core guarantees hold [Research Paper v3.2, §5]:

```
For ALL ceremony types:

I(Observer; Both_Full_Proverbs) < I(Visible_Portion)
R_max < 1 (reconstruction ceiling maintained)
s ⊥ m | X (conditional independence preserved)

Even 100% visibility only reveals First Person's proverb.
The bilateral relationship requires Sanctuary's response.
The ceremony NEVER exposes both complete proverbs publicly.
```

---

## Social Recovery Through Understanding

The asymmetric inscription path enables a fundamentally different recovery model:

### Traditional Recovery
```
Lost seed phrase → Total loss
Centralized backup → Single point of failure
Social recovery (m-of-n) → Coordination overhead
```

### Understanding-Based Recovery
```
Lost proverb → Regenerate through meaning
Recovery = f(anchor_visible, meaning_remembered, context_shared)
```

**Why This Works:**

The proverb isn't a random string. It emerged from:
- Your engagement with specific content
- Your personal context and understanding
- The relationship's shared meaning
- The compression process itself

The same cognitive process that generated the original proverb can regenerate it. The onchain inscription provides context. Your memory of understanding provides the key.

### Recovery Scenarios

**Scenario A: First Person Verification**
```
┌─────────────────────────────────────────┐
│ First Person wants to prove engagement  │
└────────────────────┬────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────┐
│ Their proverb already visible onchain   │
│ (proof of understanding exists)         │
└────────────────────┬────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────┐
│ Request Sanctuary to provide response   │
│ for full bilateral verification         │
└────────────────────┬────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────┐
│ hash(P_first_person ∥ P_sanctuary)      │
│ matches commitment → VRC verified       │
└─────────────────────────────────────────┘
```

**Scenario B: Sanctuary Response Recovery**
```
┌─────────────────────────────────────────┐
│ Sanctuary loses local response record   │
└────────────────────┬────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────┐
│ Retrieves P_first_person from onchain   │
│ (visible, provides context)             │
└────────────────────┬────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────┐
│ Reconstructs relationship meaning       │
│ • What tale was signaled?               │
│ • What response did I derive?           │
│ • What callback did I send?             │
└────────────────────┬────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────┐
│ Regenerates response from understanding │
│ (cognitive reconstruction)              │
└────────────────────┬────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────┐
│ Verifies: hash(P_fp ∥ P_regenerated)    │
│ matches stored commitment               │
└─────────────────────────────────────────┘
```

---

## Selective Disclosure

The asymmetric inscription creates a disclosure asymmetry:

**What Observers See:**
- First Person's proverbs (their understanding visible)
- Commitment hashes exist
- Relationship count is visible

**What Observers Cannot See:**
- The Sanctuary's response proverbs
- The bilateral verification details
- Which commitments map to which Sanctuary responses

**Sanctuary Controls:**
- When to verify a First Person's claim (timing)
- To whom to reveal relationship (audience)
- Which relationships to acknowledge (selection)

### Verification Protocol

```
1. Verifier retrieves P_first_person from onchain inscription (visible)
2. Sanctuary provides P_sanctuary (hidden response)
3. Verifier computes hash(P_first_person ∥ P_sanctuary)
4. Match against stored commitment → relationship verified
```

The First Person need not be present or available. The onchain record serves as their persistent proof of understanding. The Sanctuary holds the completing response that verifies the bilateral relationship.

---

## Entropy and Security

**Common Concern:** "Aren't proverbs guessable?"

**Reality:** Proverbs aren't random strings, but they're not low-entropy either.

Proverb derivation incorporates **contextual entropy** from:
- The specific tale/content engaged with
- The timing of the interaction
- The participant's unique LLM memory patterns
- The relationship's shared chronicles
- Personal interpretation and compression style

An attacker would need to:
1. Know which content was engaged with
2. Understand the relationship's context
3. Comprehend the principle being compressed
4. Match the participant's compression style

**Brute force resistance:** The combination of contextual specificity and semantic compression creates sufficient entropy that attackers cannot enumerate without understanding the relationship itself. They must not only guess words but comprehend the relationship's meaning.

---

## Trust Tier Integration

The three paths map naturally to progressive trust:

| Tier | Recommended Path | Rationale |
|------|------------------|-----------|
| 🗡️ **Blade** (0-50) | Symmetric (🔒📝 ↔ 🔒📝) | Maximum privacy while trust builds |
| 🛡️ **Light** (50-150) | Asymmetric (🔓📝 → 🔒🗝️) | Recovery becomes valuable |
| ⚔️ **Heavy** (150-500) | Interleaved (🔓½📝 ↔ 🔒½🗝️) | Mutual commitment, shared risk |
| 🐉 **Dragon** (500+) | Multiple overlapping | Redundant recovery networks, all paths |

**Dragon Tier Pattern:**

```
Dragon participants may create inscriptions across all three paths,
forming redundant recovery meshes:

Recovery_paths = Σ(symmetric) + Σ(asymmetric) + Σ(interleaved)

Mix of paths creates:
- Symmetric: relationships requiring maximum discretion
- Asymmetric: relationships where FP visibility acceptable
- Interleaved: high-trust bilateral commitments

The portfolio of inscription types itself becomes a trust signal.
```

---

## Signal to Sanctuary: First Implementation

**Zypherpunk Hack 2025** produced the first production implementation of these primitives on Zcash.

**Repository:** [github.com/mitchuski/agentprivacy-zypher](https://github.com/mitchuski/agentprivacy-zypher) — Complete implementation with Zcash integration, Nillion TEE, NEAR Cloud AI, and IPFS spellbook storage.

### Architecture

```
┌─────────────────────────────────────────┐
│         First Person Journey            │
│                                         │
│ 📖 Read tale at agentprivacy.ai/story   │
│ 🔮 (Optional) Chat with Soulbae         │
│ ✍️ Form proverb from understanding      │
│ 📋 Copy formatted memo                  │
└────────────────────┬────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────┐
│         Zashi Wallet (Swordsman)        │
│                                         │
│ • Paste memo with proverb               │
│ • Set signal amount (0.01 ZEC)          │
│ • Send z→z shielded transaction         │
│                                         │
│ Wallet IS the Swordsman—controls        │
│ transaction, verifies privacy           │
└────────────────────┬────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────┐
│         Oracle (Viewing Key Only)       │
│                                         │
│ • Decrypts memo (views proverb)         │
│ • Fetches canonical from IPFS           │
│   ipfs://bafkreigopjrfwjsz56oft7nmv26q2oddq6j4fexj27zjirzgkdeogm2myq │
│ • AI verifies semantic match            │
│ • NEVER sees amount/address/timing      │
│ • Triggers golden split on verification │
└────────────────────┬────────────────────┘
                     │
        ┌────────────┴────────────┐
        │                         │
        ▼                         ▼
┌───────────────┐         ┌───────────────┐
│  61.8%        │         │  38.2%        │
│  Transparent  │         │  Shielded     │
│               │         │               │
│  Inscription  │         │  Protocol     │
│  with proverb │         │  operations   │
└───────────────┘         └───────────────┘
        │
        ▼
┌─────────────────────────────────────────┐
│         VRC Callback                    │
│                                         │
│ Oracle sends response proverb           │
│ to First Person's z-address             │
│                                         │
│ Bilateral VRC established:              │
│ hash(FP_proverb ∥ Oracle_proverb)       │
└─────────────────────────────────────────┘
```

### Key Separation

Signal to Sanctuary demonstrates cryptographic dual-agent architecture:

```
Viewing Key (Mage's sight):
├── Can read memo contents
├── Can verify proverbs
├── Cannot spend funds
└── Cannot sign transactions

Signing Key (Swordsman's action):
├── Can execute golden split
├── Can create inscriptions
├── Only acts upon verified signal
└── Never sees unverified content

THE GAP:
The agent that sees cannot act.
The agent that acts only does so upon verified signal.
Mathematical separation, not policy-based trust.
```

### All Three Paths Available

Signal to Sanctuary supports all inscription types:

**Asymmetric (Current Default):**
```
[rpp-v1]
[act-id]
[timestamp]
[proverb]
→ First Person proverb visible, Sanctuary response hidden
→ Recovery + selective disclosure enabled
```

**Symmetric (Maximum Privacy):**
```
[rpp-v1-symmetric]
[act-id]
[timestamp]
[proverb]
→ Both proverbs hidden in commitment hash
→ Maximum privacy, requires both parties for verification
```

**Interleaved (Mutual Commitment):**
```
[rpp-v1-interleaved]
[act-id]
[timestamp]
[proverb]
[split-ratio]
→ Half each visible, half each in hash
→ Neither controls disclosure alone, mutual recovery
```

---

## Proverbiogenesis Connection

Both inscription paths participate in **proverbiogenesis**—the process by which statements transform from someone's words to everyone's truth [Spellbook v4.0.2, Act 12].

### The Five Phases

```
🌱 Induction    → Stimulus (the privacy problem felt)
⚒️ Coinage      → Formula crystallized ("Privacy is value")
📡 Exposure     → Propagating agent (spellbook, inscriptions)
🌊 Dissemination→ Mixed diffusion (parallel adoption)
🌫️🏛️ Reference Loss → The forgetting (becomes weather)
```

### Inscriptions as Exposure

Every proverb inscription—symmetric or asymmetric—serves as an **exposure mechanism**:
- Each inscription propagates the principle
- Parallel inscriptions create mixed diffusion
- Accumulating inscriptions build proverbial currency
- Eventually: "Of course data is sovereign" becomes obvious

**The paradox of victory:** If privacy primitives succeed, no one will remember they were built. If they fail, no one will remember they could have been.

*We're not building monuments. We're building weather.*

---

## Implementation Notes

### Memo Format

**Asymmetric (Current Default):**
```
[rpp-v1]
[tale-id]
[timestamp]
[proverb]

Example:
[rpp-v1]
[act-5-golden-split]
[1699564800123]
[Seventh capital flows through gates I choose]

Result: First Person's proverb visible in transparent pool inscription
        Sanctuary's response hidden in VRC callback + commitment hash
```

**Symmetric (Maximum Privacy Option):**
```
[rpp-v1-symmetric]
[tale-id]
[timestamp]
[proverb]

Example:
[rpp-v1-symmetric]
[act-5-golden-split]
[1699564800123]
[Seventh capital flows through gates I choose]

Result: Only hash(FP_proverb ∥ Sanctuary_proverb) published
        Neither proverb visible onchain
```

**Interleaved (Mutual Commitment):**
```
[rpp-v1-interleaved]
[tale-id]
[timestamp]
[proverb]
[split-ratio] (optional: default 50, or 618 for φ)

Example:
[rpp-v1-interleaved]
[act-5-golden-split]
[1699564800123]
[Seventh capital flows through gates I choose]
[618]

Result: 
  visible: FP_proverb[0:61.8%] ∥ Sanctuary_proverb[38.2%:100%]
  hidden:  hash(FP_proverb[61.8%:100%] ∥ Sanctuary_proverb[0:38.2%])
```

### Verification Endpoints

```
POST /verify/symmetric
{
  "proverb_fp": "...",
  "proverb_sanctuary": "...",
  "commitment": "..."
}
→ { "verified": true/false }

POST /verify/asymmetric
{
  "proverb_fp": "...",           // visible onchain
  "proverb_sanctuary": "...",    // provided by Sanctuary for verification
  "commitment": "..."
}
→ { "verified": true/false }

POST /verify/interleaved
{
  "proverb_fp": "...",           // full proverb (half visible, half hidden)
  "proverb_sanctuary": "...",    // full proverb (half hidden, half visible)
  "commitment": "...",
  "split_ratio": 0.618           // fragment boundary
}
→ { "verified": true/false, "fragments_match": true/false }
```

### Golden Ratio Visibility Tracking (Future)

```
POST /signal
{
  "memo": "...",
  "path": "asymmetric" | "symmetric" | "interleaved",
  "split_ratio": 0.5 | 0.618     // for interleaved only
}

GET /ecosystem/inscription-distribution
→ { 
    "symmetric": 0.382,
    "asymmetric": 0.382,
    "interleaved": 0.236,
    "total_signals": 1000,
    "avg_interleaved_split": 0.618
  }
```

---

## The Big Picture

Three paths. Five ceremony types. One paradigm shift.

**The shift:** From "what you have" to "what you understand."

All inscription types:
- Create bilateral trust from understanding
- Enable VRC formation without identity disclosure
- Participate in proverbiogenesis [Spellbook v4.0.2, Act 12]
- Contribute to privacy infrastructure
- Preserve reconstruction ceiling guarantees [Research Paper v3.2, §5]
- **Work WITH human cognitive architecture, not against it**

The choice between them reflects fundamental tradeoffs:
- **Symmetric:** Maximum privacy, requires both parties for recovery
- **Asymmetric:** First Person visibility, understanding-based recovery
- **Interleaved:** Mutual fragments, neither controls alone, shared recovery

The visibility ratio chosen at ceremony time **is itself a signal**—it declares the relationship style as cryptographic structure. Privacy-first or openness-first. Guarded or declared. Mutual or asymmetric.

The golden ratio may govern not just fee distribution but visibility ratios and fragment boundaries—an experimental hypothesis that Signal to Sanctuary provides infrastructure to test.

**Key Innovation:** VRC ceremonies without surveillance. Your understanding becomes your key. Your relationships become your backup. The ceremony creates commitment without creating a surveillance record.

**The Adoption Unlock:** By aligning cryptographic primitives with how human memory actually works—relational, contextual, meaningful—we may have found the path to mainstream adoption of privacy-preserving trust.

Signal to Sanctuary proves all three paths work on Zcash today.

The window is 2-3 years before surveillance architectures lock in [Spellbook v4.0.2, Act 12]. Every inscription—symmetric, asymmetric, or interleaved—is a vote for which future becomes inevitable.

---

## Further Reading

### Core Documentation Suite

| Document | Version | Relevant Sections |
|----------|---------|-------------------|
| **Swordsman/Mage Whitepaper** | v4.4 | §4.3 Private Proverb Inscription, §2 Dual-Agent Architecture |
| **Dual Privacy Research Paper** | v3.2 | §5 Reconstruction Ceiling, §4 Key Derivation, §7 Golden Ratio Hypothesis |
| **First Person Spellbook** | v4.0.2 | Part VI: The Recovery, Act 12: The Forgetting/Proverbiogenesis |
| **VRC Protocol: Tokenomics** | v2.1 | §1.3 Ceremony vs Signal, §2.1 RPP Foundation, §5 Trust Tiers |
| **Visual Architecture Guide** | v1.2 | VRC Formation Process, Information Flow Topology |
| **Glossary** | v2.1 | VRC, RPP, First Person, Ceremony, Signal definitions |

### Signal to Sanctuary Implementation

**Repository:** [github.com/mitchuski/agentprivacy-zypher](https://github.com/mitchuski/agentprivacy-zypher)

| Document | Purpose |
|----------|---------|
| **PROJECT_OVERVIEW.md** | Architecture & bounty alignment |
| **HOW_IT_WORKS.md** | Technical flow & code paths |
| **README.md** | Quick start & dual-agent model |
| **QUICKSTART.md** | 30-minute deployment guide |

### Related Concepts

| Concept | Document Reference |
|---------|-------------------|
| Reconstruction Ceiling (R < 1) | Research Paper v3.2, §5 |
| Conditional Independence (s ⊥ m \| X) | Whitepaper v4.4, §2.1 |
| Golden Ratio Economics | Tokenomics v2.1, §2.1 |
| Trust Tier Progression | Tokenomics v2.1, §5; Glossary v2.1 |
| Proverbiogenesis | Spellbook v4.0.2, Act 12 |
| Threshold Recovery | Spellbook v4.0.2, Part VI |

### Living Documentation

- [github.com/mitchuski/agentprivacy-zypher](https://github.com/mitchuski/agentprivacy-zypher) — Signal to Sanctuary implementation repository
- [github.com/mitchuski/agentprivacy-docs](https://github.com/mitchuski/agentprivacy-docs) — Documentation repository
- [agentprivacy.ai/story](https://agentprivacy.ai/story) — The Spellbook (narrative framework)
- [agentprivacy.ai](https://agentprivacy.ai) — Project home

### Suggested Whitepaper Integration

This document is designed to integrate with **Whitepaper v4.4** as:

**Option A: Appendix D — Proverb Inscription Paths**
- Full document as appendix
- Cross-referenced from §4.3 Private Proverb Inscription
- Maintains standalone readability

**Option B: Expanded §4.4 — Inscription Path Specification**
- Core concepts integrated into main body
- Ceremony section as §4.5
- Visibility spectrum as §4.6

**Option C: Companion Document**
- Standalone in documentation suite
- Referenced from Whitepaper, Tokenomics, and Spellbook
- Current format preserved

---

## Document Series

This lite paper is part of the complete 0xagentprivacy documentation suite:

1. **Swordsman/Mage Whitepaper v4.4** — Dual-agent architecture, RPP protocol, separation primitives
2. **Dual Privacy Research Paper v3.2** — Mathematical proofs, information-theoretic bounds, ZK protocols
3. **The Spellbook v4.0.2-canonical** — Narrative compression, symbolic language, trust game, recovery architecture
4. **VRC Protocol: Economic Architecture v2.1** — Tokenomics, sustainability, deployment
5. **Visual Architecture Guide v1.2** — Diagrams, flows, conceptual maps
6. **Understanding as Key v1.0** (this document) — Visibility spectrum, ceremony types, cognitive alignment
7. **Research Proposal v1.2** — Collaboration invitation, validation needs
8. **Glossary Master v2.1** — Canonical terminology reference

**First Implementation:** Signal to Sanctuary (Zypherpunk Hack 2025)

---

*"The proverb is the spell. The inscription is the commitment. The bilateral exchange is the relationship."*

### The Paradigm Shift
```
FROM: "What you have" (stored secrets fighting human memory)
TO:   "What you understand" (demonstrated comprehension working WITH memory)
```

### Paths
**Symmetric:** 🔒📝 ↔ 🔒📝 — Both hidden, maximum privacy  
**Asymmetric:** 🔓📝 → 🔒🗝️ — First Person reveals, Sanctuary hidden, recovery enabled  
**Interleaved:** 🔓½📝 ↔ 🔒½🗝️ — Half each visible, half each hidden, mutual recovery

### Ceremonies
**Shadow:** 0% visible — Covert commitment  
**Guarded:** 38.2% visible — Privacy-weighted golden ratio  
**Balanced:** 50% visible — Mutual exposure  
**Open:** 61.8% visible — Openness-weighted golden ratio  
**Declared:** 100% visible — Public record

### The Formula
```
VRC = f(proverbs, visibility_ratio, ceremony_type)
Recovery = f(understanding, context, meaning)
Privacy = f(what_you_choose_to_reveal)
Adoption = f(alignment_with_cognitive_architecture)
```

**⚔️ ⊥ 🧙‍♂️ | 😊**

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | December 1, 2025 | Initial release: Three paths (symmetric, asymmetric, interleaved), visibility as relationship style, VRC ceremony types, φ-derived experiments, cognitive architecture alignment |

---

**License:** CC BY-SA 4.0  
**Author:** Privacymage / 0xagentprivacy  
**Implementation:** Signal to Sanctuary (Zypherpunk Hack 2025)  
**Implementation Repository:** [github.com/mitchuski/agentprivacy-zypher](https://github.com/mitchuski/agentprivacy-zypher)  
**Documentation Repository:** [github.com/mitchuski/agentprivacy-docs](https://github.com/mitchuski/agentprivacy-docs)

---

**Understanding is the new key. Privacy is Value. Take back the 7th Capital.** 📖🔮
