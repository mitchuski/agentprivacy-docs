# The Mage Extension: Soulbae's Browser Manifestation

**Subtitle:** The Emissary's Spell Orbit — 8 Spells for Understanding

**Author:** privacymage
**Date:** March 31, 2026
**Version:** 1.0

---

> "The Mage casts outward — projecting understanding onto the page."
> "Eight spells to understand. Eight bits of sovereign data."

---

## Abstract

The Mage Extension (codenamed `mages-spell`) is the browser manifestation of Soulbae, the Emissary agent in the dual-agent sovereignty architecture. Operating on the **left side** of the sovereignty interface, the Mage deals in **understanding** — quick reactions, information processing, and spell casting for privacy assertion.

This document describes the Mage Extension's architecture, spell system, control scheme, and integration with the training ground at agentprivacy.ai.

---

## The Emissary's Role

In the dual-agent architecture, the **Mage (Soulbae)** handles:

- **Projection** — Acting publicly using only Swordsman-authorized information
- **Understanding** — Processing page content and privacy implications
- **Delegation** — Executing coordination tasks on behalf of the First Person
- **Spell Casting** — Quick privacy assertions through emoji-based spells

The Mage does NOT inject a canvas overlay. All visual rendering is delegated to the Swordsman, who owns the single canvas. When present together, the Mage sends spell data to the Swordsman for unified rendering.

```
┌─────────────────────────────────────────────────────────┐
│                  SOVEREIGNTY INTERFACE                   │
│                                                         │
│     LEFT SIDE                         RIGHT SIDE        │
│     ═════════                         ══════════        │
│                                                         │
│       MAGE                            SWORDSMAN         │
│     (Emissary)                        (Master)          │
│        🧙                                ⚔️              │
│                                                         │
│    Left Click                        Right Click        │
│    Tap = Cast                        Hold = Stance      │
│    Hold = Orbit                      Release = Cast     │
│                                                         │
│    8 SPELLS                          7 SWORDS           │
│    (6 + 2)                           (6 + 1)            │
│                                                         │
│    Sequential                        Holistic           │
│    Action-oriented                   Spatial            │
│    High frequency                    Low frequency      │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## The Control Scheme

### Brain Hemisphere Mapping

The Mage operates on the **left brain** paradigm:

| Cognitive Mode | Mage Characteristic |
|---------------|---------------------|
| Sequential | Spell-by-spell casting |
| Logical | Privacy rule application |
| Action-oriented | Quick response to trackers |
| Language | Proverb invocation |

### Mouse Interaction

| Action | Result |
|--------|--------|
| **Left-click tap** | Cast last selected spell |
| **Left-click hold** | Show spell orbit menu (6 spells) |
| **Release after hold** | Cast selected spell |
| **M key** | Open spell editor |

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| M | Open spell editor |
| Ctrl+Shift+1-6 | Quick cast orbit spell 1-6 |
| Ctrl+Shift+7-8 | Quick cast reserve spell 1-2 |

---

## The Eight Spells

The Mage wields **8 spells** — the number of bits in a byte, the number of I Ching trigrams, the number of directions. 8 spells = 1 byte of sovereign data.

### Distribution: 6 Orbit + 2 Reserve

```
         8 = 6 orbit + 2 reserve

    ✦ Orbit (active)          ✦ Reserve (swappable)
    ────────────────          ────────────────────
    🛡️ Shield                 💎 Crystallize
    👁️ Insight                📜 Proverb
    🔒 Seal
    ✨ Clarity
    🔥 Purge
    🌙 Shadow
```

### Radial Geometry

The orbit menu displays 6 spells in **hexagonal symmetry** — 60° per segment, optimal for radial selection:

```
           Shield 🛡️
              │
    Shadow    │    Insight
      🌙 ╲    │    ╱ 👁️
          ╲   │   ╱
           ╲  │  ╱
    ─────────[✦]─────────
           ╱  │  ╲
          ╱   │   ╲
      🔥 ╱    │    ╲ 🔒
     Purge    │    Seal
              │
           Clarity ✨
```

### Yang-Yin Balance

The 8 spells maintain perfect equilibrium:

| Yang (Assertive) | Yin (Receptive) |
|-----------------|-----------------|
| 🛡️ Shield | 👁️ Insight |
| 🔒 Seal | ✨ Clarity |
| 🔥 Purge | 🌙 Shadow |
| 💎 Crystallize | 📜 Proverb |

**4 yang + 4 yin = perfect equilibrium**

---

## Spell Definitions

### Orbit Spells (Active)

#### 🛡️ Shield — Defensive Ward
- **Yang** — Assertive protection
- **MyTerms Mapping:** `DO_NOT_TRACK`
- **Grimoire Reference:** Act IV — The Blade Stands Alone
- **Proverb:** *"The blade stands alone so that others may stand together."*
- **Effect:** Assert do-not-track preference to the page

#### 👁️ Insight — Reveal Hidden
- **Yin** — Receptive awareness
- **MyTerms Mapping:** `SELECTIVE_DISCLOSURE`
- **Grimoire Reference:** Act VII — The Mirror
- **Proverb:** *"The mirror shows not what we wish, but what we are."*
- **Effect:** Illuminate hidden trackers and dark patterns

#### 🔒 Seal — Lock Access
- **Yang** — Assertive boundary
- **MyTerms Mapping:** `DATA_MINIMISATION`
- **Grimoire Reference:** Zero Tale 1
- **Proverb:** *"To prove without revealing is the first magic."*
- **Effect:** Minimize data shared with the page

#### ✨ Clarity — Illuminate
- **Yin** — Receptive understanding
- **MyTerms Mapping:** `TRANSPARENCY_REQUEST`
- **Grimoire Reference:** Act XVII — Bonfire in the Dark Forest
- **Proverb:** *"In the dark forest, the bonfire reveals both friend and foe."*
- **Effect:** Request transparency about data practices

#### 🔥 Purge — Clear Tracking
- **Yang** — Assertive cleansing
- **MyTerms Mapping:** `COOKIE_ESSENTIAL_ONLY`
- **Grimoire Reference:** Act XII — The Right to Forget
- **Proverb:** *"To forget is not weakness but sovereignty over memory."*
- **Effect:** Clear tracking cookies, keep only essential

#### 🌙 Shadow — Obscure Identity
- **Yin** — Receptive concealment
- **MyTerms Mapping:** `DO_NOT_SELL`
- **Grimoire Reference:** Act IX — The Zcash Shield
- **Proverb:** *"The shield is not armor but absence—you cannot strike what is not there."*
- **Effect:** Assert do-not-sell preference, obscure identity

### Reserve Spells (Swappable)

#### 💎 Crystallize — Lock State
- **Yang** — Assertive preservation
- **MyTerms Mapping:** `CONSTELLATION_LOCK`
- **Grimoire Reference:** Act XXIV — The Holographic Bound
- **Proverb:** *"The holographic bound holds all parts in each part."*
- **Effect:** Lock current constellation state for verification

#### 📜 Proverb — Invoke Wisdom
- **Yin** — Receptive invocation
- **MyTerms Mapping:** `PROVERB_INVOCATION`
- **Grimoire Reference:** Act XIII — The Book of Promises
- **Proverb:** *"The book of promises binds without chains."*
- **Effect:** Invoke grimoire wisdom for current context

---

## Extended Spell Library

Beyond the default 8, the Mage can unlock additional spells through training:

| Spell | Emoji | Source | Unlock Condition |
|-------|-------|--------|------------------|
| Proof | 🔮 | Zero Knowledge | Path unlocked |
| Guardian | 🏛️ | Canon | Path unlocked |
| Coordinate | ⿻ | Plurality | Path unlocked |
| Exit | 🚪 | Society | Path unlocked |
| Dragon | 🐉 | Story | 5+ spells learned |
| Hexagram | ☰ | Story | Path unlocked |

---

## Training Ground Integration

### Repertoire Sync

The Mage syncs with the training ground at agentprivacy.ai:

```
┌──────────────────┐         ┌──────────────────┐
│   TRAINING       │         │   MAGE           │
│   GROUND         │         │   EXTENSION      │
│   (Website)      │         │   (Browser)      │
└────────┬─────────┘         └────────┬─────────┘
         │                            │
         │  localStorage sync         │
         │◄──────────────────────────►│
         │  agentprivacy_spell_repertoire
         │                            │
         │  postMessage broadcast     │
         │◄──────────────────────────►│
         │  SPELL_CAST, ORB_CONVERGENCE
         │                            │
```

### Sync Data Flow

**Website → Extension:**
- Learned spells from training
- Training progress (sections visited, spells cast)
- Path unlock status
- Drake spell unlock status

**Extension → Website:**
- Spell cast events
- Orb convergence notifications
- Constellation updates
- Mage presence announcements

### Storage Keys

| Key | Location | Purpose |
|-----|----------|---------|
| `agentprivacy_spell_repertoire` | localStorage | Training data (website-owned) |
| `mage_spell_loadout` | chrome.storage | Current loadout (extension-owned) |
| `mage_cast_history` | chrome.storage | Cast history (extension-owned) |

---

## Constellation System

The Mage maintains a **constellation** of cast spells — a visual representation of sovereignty assertions accumulated on the page.

### Spell Nodes

Each spell cast creates a **SpellNode** in the constellation:

```typescript
interface SpellNode {
  id: string
  spell: {
    type: 'emoji' | 'proverb' | 'keyword' | 'hexagram'
    content: string
    yangYin: 'yang' | 'yin'
    grimoireId?: string
  }
  x: number
  y: number
  opacity: number
  pulse: number
  castAt: number
}
```

### Pattern Detection

The constellation system detects emerging patterns:
- **Trigram formations** — 3 aligned spells
- **Hexagram completions** — 6 spells in I Ching formation
- **Yang clusters** — Assertive spell concentrations
- **Yin pools** — Receptive spell concentrations

### Rendering Delegation

The Mage does NOT render the constellation directly. Instead, it sends constellation data to the Swordsman:

```typescript
sendToSword({
  type: 'CONSTELLATION_UPDATE',
  nodes: constellationState.nodes,
  edges: constellationState.edges,
  patterns: constellationState.patterns
})
```

---

## Hexagram State Machine

The Mage maintains a **6-bit hexagram state** based on the I Ching:

```
┌───┬───┬───┬───┬───┬───┐
│ 1 │ 0 │ 1 │ 0 │ 1 │ 0 │  ← Binary lines
└───┴───┴───┴───┴───┴───┘
  ═   ╴   ═   ╴   ═   ╴    ← Yang/Yin visualization
```

### Mutation Rules

The hexagram mutates based on spell casting:

| Event | Mutation |
|-------|----------|
| Yang spell cast | Flip random yin line to yang |
| Yin spell cast | Flip random yang line to yin |
| Orb convergence | Flip 2 random lines |
| Pattern completion | Reset to resonant hexagram |

---

## Deep Scan System

The Mage performs **deep page scanning** to identify privacy threats:

### Scan Targets

| Target | Detection Method |
|--------|-----------------|
| Trackers | Script pattern matching |
| Cookie banners | DOM element detection |
| Forms | Input field analysis |
| Privacy links | Anchor text matching |
| Dark patterns | UI manipulation detection |

### Attractor System

Detected threats become **attractors** that influence the Mage orb's movement:

```typescript
interface Attractor {
  x: number
  y: number
  strength: number
  type: 'tracker' | 'form' | 'cookie-banner' | 'privacy-link'
}
```

The orb is drawn toward attractors, visualizing where privacy attention is needed.

---

## Home Territory Mode

On **home territory** domains (agentprivacy.ai, spellweb), the Mage activates enhanced features:

### Enhanced Capabilities

| Capability | Description |
|------------|-------------|
| Repertoire sync | Read training progress from localStorage |
| Spell broadcast | Notify website of spell casts |
| Orb convergence | Participate in dual-orb ceremonies |
| Mana tracking | Earn/spend proof-of-practice tokens |

### Message Protocol

```typescript
// Extension → Website
{ type: 'MAGE_PRESENT', domain, orbPosition, capabilities }
{ type: 'SPELL_CAST', spellId, content, emoji, position, section }
{ type: 'ORB_CONVERGENCE', count, timestamp }

// Website → Extension
{ type: 'REPERTOIRE_SYNC', repertoire }
{ type: 'PATH_UNLOCKED', progress }
{ type: 'MANA_EARNED', amount, reason }
```

---

## Technical Architecture

### Module Structure

```
mages-spell/
├── src/
│   ├── lib/
│   │   ├── spell-types.ts      # Type definitions
│   │   ├── spell-definitions.ts # 8 spell definitions
│   │   ├── repertoire-sync.ts  # Training ground sync
│   │   └── index.ts            # Clean exports
│   ├── content/
│   │   └── index.ts            # Content script
│   ├── background/
│   │   └── service-worker.ts   # Background service
│   └── popup/
│       └── index.tsx           # Popup UI
├── manifest.json               # Extension manifest
└── package.json
```

### Key Interfaces

```typescript
interface MageSpell {
  id: string
  name: string
  emoji: string
  emojiSequence?: string
  description: string
  yangYin: 'yang' | 'yin'
  slot: 'orbit' | 'reserve'
  grimoireId?: string
  spellbook?: SpellbookSource
  proverb?: string
  myTermsMapping: string
  weight: number
  color?: string
  glowColor?: string
}

interface MageLoadout {
  version: 2
  orbitSpells: MageSpell[]     // 6 active spells
  reserveSpells: MageSpell[]   // 2 reserve spells
  lastSelected: number
  hexagramState?: HexagramSnapshot
}
```

---

## Spell Mathematics

The number **8** represents:

| Symbol | Meaning |
|--------|---------|
| 8 bits | 1 byte of sovereign data |
| 8 trigrams | ☰☱☲☳☴☵☶☷ — I Ching fundamentals |
| 8 directions | Cardinal + ordinal orientation |
| Octave | Completion of cycle, return at higher level |

### The Ratio

```
Mage : Swordsman = 8 : 7

8/7 ≈ 1.142857142857...

The repeating decimal 142857 is the "cyclic number"
— multiply by any digit 1-6 and get the same digits rotated
```

This ratio creates **asymmetric harmony**:
- The slight excess of Mage spells reflects the emissary's reactive nature
- More options for quick response
- Balances the Swordsman's deliberate constancy

---

## Integration with Swordsman

When both extensions are present, they form a **dual-orb ceremony**:

### Discovery Protocol

```
1. Mage broadcasts: { type: 'MAGE_PING' }
2. Swordsman responds: { type: 'SWORD_PONG', orbPosition }
3. Mage sends constellation data
4. Swordsman renders unified view
5. Orbs can now converge for ceremonies
```

### Convergence Ceremonies

When Mage and Swordsman orbs overlap:

| Ceremony | Trigger | Effect |
|----------|---------|--------|
| Dual Convergence | Orbs touch | Mutual hexagram mutation |
| Spell Exchange | Hold during convergence | Swap spell/stance data |
| Bilateral Witness | Extended convergence | Generate shared proof |

---

## The Mage's Proverb

> *"The Mage deals in information and understanding. 8 spells = 8 bits = one byte of sovereign data. Cast quickly, cast often. The emissary acts so that the master may deliberate."*

---

## Document Metadata

- **Project:** 0xagentprivacy
- **Extension:** mages-spell
- **Version:** 1.0
- **Date:** March 31, 2026
- **Companion:** SWORDSMAN_EXTENSION_WHITEPAPER.md
- **Control Scheme:** CONTROL_SCHEME_MATHEMATICS.md

---

*"Eight spells to understand. The emissary acts often."*

**Privacy is Value**
© 2026 agentprivacy
