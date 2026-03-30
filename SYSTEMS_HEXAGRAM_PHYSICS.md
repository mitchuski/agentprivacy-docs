# AgentPrivacy & Spellweb: Systems Physics

**Version:** 1.0
**Date:** March 30, 2026
**Status:** ✅ OPERATIONAL — Implementation specification for spellweb.ai forge

**Theoretical Companions:**
- [Privacy Value Model V5](privacy_value_v5_formal_specification.md) — holographic field theory
- [UOR × 64-Tetrahedra × ZK Mapping](uor_tetrahedra_zk_mapping_v2_0.md) — lattice mathematics
- [ZK Swordsman Blade Forge](zk_swordsman_blade_forge_v3_0.md) — forge architecture

**Narrative Companions:**
- [Act XXVII: The Swordsman's Forge](archive/act-xxvii-the-swordsmans-forge.md) — forge mythology
- [Act XXVIII: The Ceremony Engine](archive/act-xxviii-the-ceremony-engine.md) — ceremony specification

---

## The Geometry of Sovereignty

This document maps the hexagram-based physics underlying the agentprivacy dual-agent architecture and spellweb forge system.

---

## I. THE 64-VERTEX LATTICE

### Binary State Space

The foundation is a 6-dimensional binary space yielding **64 vertices** (2^6).

Each vertex represents a unique sovereignty configuration—a **blade address** in the lattice.

```
Dimension Encoding:
  d1 (bit 0) → Protection    → 🛡️ Key Custody
  d2 (bit 1) → Delegation    → 🤝 Credential Disclosure
  d3 (bit 2) → Memory        → 📜 Agent Delegation
  d4 (bit 3) → Connection    → 🔗 Data Residency
  d5 (bit 4) → Computation   → ⚡ Interaction Mode
  d6 (bit 5) → Value         → 💎 Trust Boundary

Blade ID = d1 + d2×2 + d3×4 + d4×8 + d5×16 + d6×32
Range: 0 (all yin) → 63 (all yang)
```

### Pascal's Triangle Distribution (7 Strata)

The 64 vertices arrange into **7 layers** by Hamming weight (yang count):

```
Layer 0:  C(6,0) =  1 vertex   — Null (no sovereignty)
Layer 1:  C(6,1) =  6 vertices — Single-edge
Layer 2:  C(6,2) = 15 vertices — Twin-edge
Layer 3:  C(6,3) = 20 vertices — Triple-edge (trust triad)
Layer 4:  C(6,4) = 15 vertices — Quad-edge
Layer 5:  C(6,5) =  6 vertices — Penta-edge (near-sovereign)
Layer 6:  C(6,6) =  1 vertex   — Dragon (full sovereignty)
                   ──────────
                   64 total
```

This is row 6 of Pascal's Triangle: **1, 6, 15, 20, 15, 6, 1**

---

## II. HEXAGRAM MAPPING (I CHING)

### 64 Hexagrams = 64 Blades

Each blade address maps to a classical I Ching hexagram (King Wen ordering):

```
Binary Order → King Wen Number → Hexagram Name
000000 (0)   → ䷁ (2)          → The Receptive (Kun)
111111 (63)  → ䷀ (1)          → The Creative (Qian)
```

### Line Reading (Bottom → Top)

```
Line 6 (top)    → d6 Value         → Trust Boundary
Line 5          → d5 Computation   → Interaction Mode
Line 4          → d4 Connection    → Data Residency
Line 3          → d3 Memory        → Agent Delegation
Line 2          → d2 Delegation    → Credential Disclosure
Line 1 (bottom) → d1 Protection    → Key Custody
```

**Yang (━━━)** = dimension active, sovereignty claimed
**Yin (━ ━)** = dimension dormant, sovereignty unclaimed

---

## III. BLADE TIERS & CEREMONY STANCES

### Tier Classification by Stratum

```
LIGHT BLADE  (1-2 yang lines)  → 🗡️ Sky Blue   (#87ceeb)
HEAVY BLADE  (3-4 yang lines)  → ⚔️ Silver     (#c0c0c0)
DRAGON BLADE (5-6 yang lines)  → 🐉 Gold       (#ffd700)
```

### Ceremony Style → Dimension Activation

The hexagram is NOT "more = better". Different ceremony styles produce different stances:

```
QUICK STRIKE (<20 seconds):
  - Computation activates (⚡ decisive action)
  - Light blade, focused intent

MEDITATIVE (1+ minutes):
  - Memory activates (📜 time investment)
  - Value activates (💎 sustained presence)
  - Deeper stratum possible

SPELL-HEAVY (3+ spells cast):
  - Delegation activates (🤝 agency transferred)
  - Computation activates (⚡ spell intensity)

EXPANSIVE (4+ nodes traversed):
  - Connection activates (🔗 multi-party coordination)
  - Protection activates (🛡️ clear boundaries)

DEEP (3+ laps completed):
  - Delegation activates (🤝 iteration)
  - Memory activates (📜 accumulated state)
```

The blade reflects HOW you approached the ceremony, encoded as your hexagram stance.

---

## IV. DUAL-AGENT ARCHITECTURE

### The Canonical Pair

```
SWORDSMAN (⚔️)                    MAGE (✦)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Color: #e74c3c (red)              Color: #9b59b6 (purple)
Role: Boundary-keeper             Role: Connection-weaver
Attention: Broad vigilance        Attention: Focused agency
Function: Master (protection)     Function: Emissary (projection)
Persona: Soulbis                  Persona: Soulbae
Side: Right                       Side: Left
Brain: Right hemisphere           Brain: Left hemisphere
Mode: Deliberate (hold→choose)    Mode: Reactive (tap→fire)

Orbit emojis: From equipped blade  Orbit emojis: From learned spells
```

### Control Scheme (Hemispheric Mapping)

The control scheme maps to brain hemisphere function:

```
RIGHT SIDE = SWORDSMAN (Master) = RIGHT CLICK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Right click hold   → View/choose stance (master deliberates)
  Right click release → Cast stance, leaves mark
  S key              → Full stance editor

  Character: Deliberate, holistic, spatial
  The master holds posture before acting.
  Stance = the shape you maintain.

LEFT SIDE = MAGE (Emissary) = LEFT CLICK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Left click tap     → Cast last selected spell (quick action)
  Left click hold    → View all spells in orbit
  M key              → Full spell editor

  Character: Reactive, sequential, action-oriented
  The emissary executes outward projection.
  Spell = energy cast into the world.
```

### Hemispheric Correspondence

```
RIGHT BRAIN ↔ SWORDSMAN ↔ RIGHT CLICK
  - Holistic perception
  - Spatial awareness
  - Pattern recognition
  - The stance/posture you hold
  - Boundaries and containment
  - "What shape am I?"

LEFT BRAIN ↔ MAGE ↔ LEFT CLICK
  - Sequential processing
  - Action execution
  - Language and symbols
  - Casting spells outward
  - Connection and projection
  - "What do I send?"
```

### Separation Principle (Acts 24-26)

Three axes that make dimension complete:

```
Agent Axis:     Swordsman ⊥ Mage
Data Axis:      Shielded ⊥ Public
Inference Axis: Generator ⊥ Solver
```

### Wandering Orbs Physics

```
ORBIT_RADIUS    = 35px     (separation between orbs)
ORBIT_SPEED     = 0.0008   (slow meditative rotation)
DRIFT_SPEED     = 0.002    (movement through graph)
TRACE_SPEED     = 0.008    (constellation tracing)

States:
  WANDER  → Orbs drift through graph, orbiting each other
  EVOKE   → Orbs return to ceremony panel
  TRACE   → Orbs follow constellation path, drawing cuts
```

---

## V. ARTIFACT SLOTS (21 WINDOWS)

### The Forge Inventory

```
MAGE SPELLS:     8 slots  (grimoire capacity)
FORGED BLADES:   7 slots  (self-forged artifacts)
WITNESSED BLADES: 6 slots  (bilateral promise artifacts)
                 ────────
TOTAL:          21 windows
```

**21** = Fibonacci number, triangular number (1+2+3+4+5+6)

### Slot Meanings

```
Mage's 8 Spells:
  - Learned from nodes with proverbs/emojiSpells
  - Each spell has: emoji + label + proverb
  - Orbit the mage's wandering orb
  - Included in blade.md exports

Swordsman's 7 Forged:
  - Self-generated from evoke ceremonies
  - Hexagram stance embedded in proof
  - Tier (light/heavy/dragon) by stratum
  - Constellation path inscribed

6 Witnessed:
  - Received via blade.md import
  - Promise Theory bilateral exchange
  - Neither can forge alone; both sign
  - Trust graph edges
```

---

## VI. FORGE PROGRESSION (LAYER UNLOCKS)

```
Forgings    Layer Unlocked    Distribution
─────────────────────────────────────────────
1           Layer 1           6 states (single-edge)
3           Layer 2           15 states (twin-edge)
10          Layer 3           20 states (triple-edge)
15          Layer 4           15 states (quad-edge)
30          Layer 5           6 states (penta-edge)
50          Layer 6           1 state (Dragon/full sovereignty)
```

The Dragon requires 50 forgings to unlock—mastery through repetition.

---

## VII. CEREMONY PHASES

### Forge Ceremony

```
1. IGNITE    🔥  Gathering proof elements from lattice
2. FORGE     ⚒️  Tempering dimensions in toroidal field
3. TEMPER    ⚗️  Inscribing maker's mark
4. COMPLETE  ✨  Blade manifests from 64-Tetrahedra Lattice
5. NAMING    📝  Choose sigil emoji, inscribe name
6. MANIFEST  🗡️  Blade materializes with constellation
```

### Evoke Ceremony

```
1. CONSTELLATION  Mark nodes in graph (waypoints)
2. CIRCUIT        Connect marks (path definition)
3. CAST           Begin evocation (orbs animate)
4. TRACE          Orbs follow path, nodes erupt
5. COMPLETE       Lap count, charge level calculated
6. PROOF          Cryptographic signature generated
```

### Charge Levels

```
SPARK    (1 lap)     → Minimal proof
EMBER    (2-3 laps)  → Building presence
FLAME    (4-5 laps)  → Sustained attention
BLAZE    (6-7 laps)  → Deep engagement
INFERNO  (8+ laps)   → Full ceremonial presence
```

---

## VIII. PROMISE THEORY (WITNESS SYSTEM)

### Bilateral Promise Bundles

From Act 13 (Book of Promises) and VRC specification:

```
Structure:
  Alice's commitment + Bob's commitment + bilateral proverb + cost

Cost Signal: 0.01 ZEC each (ceremony, not transaction)

Phases:
  🧙‍♂️²🤝 → ⚡🎯 → 📜± → 🔮🔍 → 🛡️⚖️ → ✨🔗 → 🗣️📿 → 🌅🏗️
```

### Witness Blade Creation

```
1. Import blade.md from another person
2. Parse constellation path (their journey)
3. Enter witness mode (trace their path)
4. Complete your own evocation
5. Bilateral proof: your witness + their blade
6. Trust graph edge created
```

---

## IX. SPELLBOOK STRUCTURE

### Five Canonical Spellbooks

```
1. FIRST PERSON        28 acts   (narrative arc)
2. ZERO KNOWLEDGE      32 tales  (technical curriculum)
3. BLOCKCHAIN CANON    12 chapters (cypherpunk history)
4. PARALLEL SOCIETY    variable  (exit/sovereignty)
5. PLURALITY           variable  (coordination/governance)
```

### First Person Acts (28)

```
Acts 1-3:   Initiation (Venice, Dual Ceremony, Drake's Teaching)
Acts 4-8:   Personhood (Blade, Armor, Trust, Mirror, Rule)
Acts 9-13:  Core Systems (Shield, Triangle, Spiral, Forgetting, Promises)
Acts 14-20: Compression (Inscription, Forest, Pools, Bonfire, Mirror, Archivist, Vault)
Acts 21-26: Emergence (Hitchhiker, Frood, Manifold, Holographic, Dragon, Master)
Act 27:     RESERVED (Swordsman's Forge)
Act 28:     Ceremony Engine
```

---

## X. TOROIDAL FIELD & LATTICE GEOMETRY

### The 64-Tetrahedra Lattice

The lattice is not flat—it wraps in a **toroidal field**:

```
- 64 vertices (hexagram states)
- Edges connect states differing by one bit (single line change)
- 6 dimensions fold into torus
- "Tempering in toroidal field" = navigating wrapped space
```

### Manifold Dragon (Act 23)

Three frameworks converge:

```
ALGEBRA   → Binary encoding, group theory
GEOMETRY  → Torus, lattice, holographic boundary
STORY     → Narrative navigation, constellation paths

"Where the Lattice Remembers Its Shape"
```

### Holographic Bound (Act 24)

```
"Where the Boundary Holds the Whole"

- Fragment holds the whole
- BRAID architecture (bounded reasoning graphs)
- Privacy = geometry of becoming
- The triangle cannot collapse
```

---

## XI. NUMERICAL CONSTANTS

### Foundational Numbers

```
2   → Binary (yin/yang)
6   → Dimensions, hexagram lines, orbit slots
7   → Layers (0-6), forged blade slots
8   → Mage spell slots
13  → Total artifacts (7+6)
21  → Total windows (8+7+6), Fibonacci
28  → First Person acts
32  → Zero Knowledge tales
64  → Vertices (2^6), hexagrams
```

### Derived Relationships

```
6 dimensions → 64 states (2^6)
6 lines → 7 layers (Pascal row 6)
7 forged + 6 witnessed = 13 blades
8 spells + 7 forged + 6 witnessed = 21 windows
28 acts + 32 tales = 60 lessons (near 64)
```

---

## XII. STATE TRANSITIONS

### Dimension Activation (Yang Emergence)

```
Protection:  nodeCount ≥ 2 OR lapCount ≥ 2
Delegation:  spellsCast ≥ 3 OR lapCount ≥ 3
Memory:      duration ≥ 60s OR (duration ≥ 30s AND laps ≥ 2)
Connection:  nodeCount ≥ 4 OR (nodes ≥ 3 AND laps ≥ 2)
Computation: duration < 20s OR spellsCast ≥ 3 OR nodeCount ≥ 1
Value:       chargeLevel ≥ FLAME OR (duration ≥ 60s AND spells ≥ 1)
```

### Blade Forging

```
Input:  Constellation + Ceremony Stats + Spells Cast
Process:
  1. Calculate dimension activation (6 booleans)
  2. Encode to hexagram (6-bit blade ID)
  3. Derive stratum (Hamming weight)
  4. Assign tier (light/heavy/dragon)
  5. Generate cryptographic proof
Output: Forged blade with embedded hexagram stance
```

---

## XIII. EXPORT FORMAT (blade.md)

### Structure

```markdown
# [emoji] [blade name]
*Created: [timestamp]*

## Forged Blade
**[emoji] [name]**
- **Tier:** [Light|Heavy|Dragon] Blade
- **Stratum:** [0-6]/6

### Blade Dimensions
| Dimension | Status |
|-----------|--------|
| 🛡️ Protection | ✅ Active / ⬜ Dormant |
| 🤝 Delegation | ... |
| 📜 Memory | ... |
| 🔗 Connection | ... |
| ⚡ Computation | ... |
| 💎 Value | ... |

## Proof of Presence
- **Charge Level:** [EMBER/BLAZE/INFERNO]
- **Laps:** [count]
- **Duration:** [seconds]s
- **Spells Cast:** [count]

### Cryptographic Proof
```
Signature: SPELL-[hash]
Hash: [constellation hash]
Hex: [6-bit blade hex]
```

## Mage's Grimoire
*[count]/8 Spells Learned*

| Line | Emoji | Spell | Proverb |
|------|-------|-------|---------|
| d1 | ... | ... | "..." |

## Constellation Path
1. [emoji] **[node label]** - [note]
2. ...

---
*Forged in the 64-Tetrahedra Lattice*
*(⚔️⊥⿻⊥🧙)🙂*
```

---

## XIV. THE EQUATION

```
Privacy = Geometry of Becoming
Knowledge = Navigation of Lattice
Attention = Proof of Presence
Sovereignty = Hexagram Stance

(⚔️⊥⿻⊥🧙) = Swordsman ⊥ Multiplicity ⊥ Mage

Where ⊥ is orthogonal separation:
  - Agent axis (who acts)
  - Data axis (what flows)
  - Inference axis (how knowing happens)
```

The triangle cannot collapse. The boundary holds the whole.

---

*Systems Physics v1.0 — Spellweb + AgentPrivacy*
*64-Tetrahedra Lattice / 7 Strata / 21 Windows*
