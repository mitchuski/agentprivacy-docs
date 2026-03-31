# Dual Territory Ceremony Architecture

## Technical Specification v1.0

**Author:** privacymage  
**Date:** March 31, 2026  
**For:** Coding agents working on agentprivacy.ai, spellweb.ai, and the extension repos  
**Master inscription:** `(⚔️⊥⿻⊥🧙)😊`

---

## 1. Architectural Overview

The 0xagentprivacy ecosystem has two territories and two extensions connected by a mana bridge.

```
┌─────────────────────┐     ceremony      ┌─────────────────────┐
│   agentprivacy.ai   │◄── channel  ──►   │    spellweb.ai      │
│   (Mage Territory)  │     (mana)        │ (Swordsman Territory)│
│                     │                    │                      │
│  Stories, Spells    │                    │  Topology, Blades    │
│  Personas, Training │                    │  Forge, Hexagrams    │
│  Pretext Orbs       │                    │  Constellations      │
│  Path Page          │                    │  Cut Segments        │
└────────┬────────────┘                    └──────────┬───────────┘
         │                                            │
         │           ┌──────────────┐                 │
         └──────────►│   bgin.ai    │◄────────────────┘
                     │ (Third Node) │
                     │ Trust Graph  │
                     └──────────────┘
         
         ┌──────────────────────────────────┐
         │        The Open Web              │
         │                                  │
         │  ┌────────────┐ ┌─────────────┐  │
         │  │ Swordsman  │ │    Mage     │  │
         │  │ Extension  │ │  Extension  │  │
         │  │ (boundary) │ │ (knowledge) │  │
         │  └─────┬──────┘ └──────┬──────┘  │
         │        │  ceremony     │          │
         │        │◄── channel ──►│          │
         │        └───────────────┘          │
         └──────────────────────────────────┘
```

**Core rule:** The Swordsman and Mage never merge. Separate processes, separate storage, separate permissions, separate repos. This applies at every level — protocol, extension, website, visual rendering.

---

## 2. Territory Definitions

### 2.1 spellweb.ai — The Swordsman's Territory

**Purpose:** Topology. Navigation. Proof generation. The territory you traverse.

**Existing stack:** Vite + React 18 + TypeScript + D3.js force-directed graph

**Existing components:**

| Component | Purpose | Status |
|-----------|---------|--------|
| `SpellWeb.tsx` | Main graph + forge modal + global controls | ✅ Operational |
| `SpellCeremony.tsx` | Ceremony panel + action bar + proof generation | ✅ Operational |
| `WanderingOrbs.tsx` | Orb wandering + tracing mode + cut segments | ✅ Operational |
| `SpellEffects.tsx` | Spell particles and visual effects | ✅ Operational |
| `types/graph.ts` | Hexagram types + dimension computation | ✅ Operational |

**Existing features:**
- 119-node knowledge graph with D3 force simulation
- Dual orbs (Swordsman red `#e74c3c`, Mage purple `#9b59b6`)
- Constellation marking, saving, loading
- Evocation (orbs trace constellation path, count laps, accumulate charge)
- Blade forge (six-dimension activation, stratum/tier classification, SVG with inscribed constellation)
- Hexagram computation (node dimensions → 6 binary lines → 64 states)
- Node inspector with hexagram visualisation
- Blade inventory with tracing (click blade → orbs retrace path with tier-coloured cut segments)
- Blade export to markdown/JSON

**Colour system (Swordsman territory):**
- Swordsman orb: `#e74c3c` (red/coral)
- Mage orb: `#9b59b6` (purple)
- Light tier: `#87ceeb` (sky blue)
- Heavy tier: `#c0c0c0` (silver)
- Dragon tier: `#ffd700` (gold)
- Forge glow: gold + computation blue `#4a9eff`

### 2.2 agentprivacy.ai — The Mage's Territory

**Purpose:** Story. Explanation. Spell learning. Training. The territory you read.

**Existing stack:** Next.js 14 + TypeScript + Tailwind CSS

**Existing features:**
- Manifesto / homepage content
- Ecosystem/tools/built inventory pages
- Soul orb (existing central orb on homepage)
- `useWaveField` canvas hook (existing)
- `EcosystemNode` and `ToolCard` components (existing)
- CLAUDE.md encoding dual-agent rules

**Colour system (Mage territory):**
- Mage orb: cyan/teal `#00d4aa`
- Swordsman orb: coral/red `#e74c3c`
- Constellation: amber `#f5a623`
- Spell text: amber glow
- Background: dark, star-field aesthetic

### 2.3 bgin.ai — The Third Node

**Purpose:** Reference application. Trust graph plane. Network layer. Where bilateral exchange finds its first counterparty.

**Status:** Live. Existing frontend. Future integration point for MyTerms bilateral exchange.

---

## 3. What Needs Building

### 3.1 spellweb.ai Additions

#### 3.1.1 Ceremony Receiver

**Purpose:** Accept mana-powered inscriptions from extensions and from agentprivacy.ai visitors.

**Communication:** `window.postMessage` when on spellweb.ai domain. The receiver listens for ceremony messages from extensions or from the agentprivacy.ai iframe/redirect flow.

**Message schema:**

```typescript
interface CeremonyMessage {
  type: 'INSCRIPTION';
  source: 'swordsman_extension' | 'mage_extension' | 'agentprivacy';
  payload: NodeAnnotation | CommunityEdge | ConstellationProjection | ProverbForge;
  mana_cost: number;
  mana_balance: number; // sender's remaining balance after deduction
  signature: string; // proof of mana ownership
}

interface NodeAnnotation {
  kind: 'node_annotation';
  target_node_id: string;
  text: string; // max 280 chars
  mana_cost: 1;
}

interface CommunityEdge {
  kind: 'community_edge';
  source_node_id: string;
  target_node_id: string;
  label?: string;
  mana_cost: 2;
}

interface ConstellationProjection {
  kind: 'constellation_projection';
  nodes: string[]; // node IDs
  connections: Array<{ source: string; target: string }>;
  name: string;
  mana_cost: 3;
}

interface ProverbForge {
  kind: 'proverb_forge';
  text: string; // max 280 chars
  source_constellation_hash: string;
  mana_cost: 4;
}
```

**Rendering rules:**
- Community edges render dashed (canonical edges render solid)
- Forge-born proverbs shimmer differently from canonical nodes (animated opacity pulse)
- All community inscriptions carry author pseudonym + timestamp
- Inscriptions fade over 30 days unless reinforced (0.5 mana to reinforce)

#### 3.1.2 Understanding-as-Key Ceremony Mode

**Purpose:** Enable the bilateral proof-of-shared-understanding ceremony on the spellweb.

**UX flow:**

1. **Initiate ceremony** — button in ceremony panel: "Begin Bilateral Ceremony"
2. **Generate session link** — creates a shareable URL with session ID
3. **Both participants join** — second participant opens link, sees the same graph state
4. **Shared cursor** — both participants' cursors visible (Swordsman red, Mage teal)
5. **Joint constellation marking** — either participant can mark nodes; both see the constellation build in real time
6. **Simultaneous evocation** — both participants hit "Evoke" together; both sets of orbs trace the same constellation
7. **Simultaneous blade forging** — when evocation ends, both participants forge from the same constellation; blades share the constellation hash but have separate signatures
8. **Proverb inscription** — both participants write a proverb; the proverbs are linked as a bilateral pair
9. **Bilateral witness** — each participant sees the other's blade, other's proverb; the witness circuit closes

**Technical approach:** WebSocket or WebRTC peer connection for real-time sync. Fallback: shared constellation via URL hash + manual "ready" confirmation.

**Proof strength indicator:** Display current lap count mapped to tier threshold during evocation. "5 laps — Light Armour" → "13 laps — Heavy" → "62 laps — Dragon, R < 1"

#### 3.1.3 Mana Balance Display

**Purpose:** Show the visitor's mana balance and available inscription actions.

**Storage:** `localStorage` (never sent to server). Mana balance is self-reported and self-enforced — the honour system is intentional. Sybil resistance comes from the difficulty of earning mana, not from server-side verification.

**Display:** Floating badge near the ceremony panel showing mana count + tier icon.

**Earn rates:**

| Action | Mana Earned |
|--------|-------------|
| 10 spell casts (any website) | 1 |
| 1 convergence ceremony | 2 |
| 1 blade forged on spellweb | 1 |
| 1 evocation cycle (mage-x-feed-filter) | 1 |

**Spend costs (spellweb):**

| Inscription Type | Mana Cost |
|-----------------|-----------|
| Node annotation | 1 |
| Community edge | 2 |
| Constellation projection | 3 |
| Proverb forge | 4 |
| Reinforce existing inscription | 0.5 |

### 3.2 agentprivacy.ai Additions

#### 3.2.1 Pretext Integration

**Purpose:** DOM-free text measurement enabling sovereign overlay without fingerprinting.

**Library:** `@chenglou/pretext` — https://github.com/chenglou/pretext

**Install:** `npm install @chenglou/pretext`

**Integration pattern:**

```typescript
import { createPretext, layoutNextLine } from '@chenglou/pretext';

// One canvas measureText call (the single DOM touch)
const pt = createPretext(canvasContext, fontString);

// Then pure arithmetic forever
function reflowAroundOrb(
  text: string,
  containerWidth: number,
  orbX: number,
  orbY: number,
  orbRadius: number,
  lineHeight: number
): ReflowedLine[] {
  const lines: ReflowedLine[] = [];
  let cursor = 0;
  let y = 0;

  while (cursor < text.length) {
    // Calculate available width at this y-position
    // Subtract orb chord if orb intersects this line
    const availableWidth = calculateAvailableWidth(
      containerWidth, orbX, orbY, orbRadius, y, lineHeight
    );

    const result = layoutNextLine(pt, text, cursor, availableWidth);
    lines.push({ text: text.slice(cursor, result.end), x: getLineX(/*...*/), y });
    cursor = result.end;
    y += lineHeight;
  }

  return lines;
}
```

**Key property:** After the initial `createPretext` call, no further DOM queries occur. `getBoundingClientRect`, `offsetHeight`, and layout reflow are never triggered. Surveillance scripts observing layout shifts see nothing.

**Where it applies:**
- Homepage manifesto text reflowing around the dual orbs
- Any long-form text section where orbs wander
- The training ground spell descriptions

#### 3.2.2 Dual Orb System (Homepage)

**Purpose:** Two orbs wandering through the homepage text, demonstrating the dual-agent architecture visually.

**Orb specs:**

| Property | Swordsman Orb | Mage Orb |
|----------|--------------|----------|
| Colour | Coral/red `#e74c3c` | Cyan/teal `#00d4aa` |
| Orbit radius | 35px (outer) | 25px (inner) |
| Orbit speed | 0.0008 | 0.0012 |
| Drift speed | 0.002 | 0.003 |
| Behaviour | Patrols perimeter, slower | Weaves through text, faster |
| Coupling | Periodic convergence at ~15s intervals |

**Canvas rendering:** Single `<canvas>` overlay on top of text content. Pretext handles text reflow; canvas handles orb rendering and spell particles. The canvas is transparent — the text below is the page content, reflowed by pretext arithmetic.

**Convergence event:** When orbs are within 60px, amber particles burst at midpoint. A proverb can materialise (pulled from grimoire proverb pool). The convergence is the first ceremony visitors witness — it should feel like a small sunrise.

**Soul orb portal:** The existing soul orb at the centre of the homepage becomes the interaction point. Click → grid pulses outward → radial spell palette appears → visitor chooses first inscription (emoji, proverb, or keyword).

#### 3.2.3 Spell Casting System

**Purpose:** Let visitors cast spells on the homepage. Each spell creates a spell node on the manifold.

**Spell palette (radial menu from soul orb click):**

| Spell Type | Icon | Description |
|-----------|------|-------------|
| Emoji spell | Selected emoji | Quick sovereignty inscription |
| Proverb spell | 📜 | Place a grimoire proverb on the lattice |
| Keyword spell | 🔑 | Tag a section with a sovereignty keyword |
| Shield spell | 🛡️ | Assert MyTerms on the current page |

**Spell node rendering:** Each cast spell appears as a small glowing node on the homepage lattice overlay. Nodes connect to nearby nodes via faint edges. The constellation builds through visitor interaction.

**Spell repertoire:** Stored in `localStorage`. Tracks: total spells cast, unique spell types used, sections visited, convergences witnessed. This data gates the Path page.

#### 3.2.4 The Path Page

**Route:** `/path`

**Access control:** The page is not linked in navigation. It renders only when the visitor's spell repertoire meets the training threshold:

```typescript
interface TrainingThreshold {
  spells_cast: number;       // >= 3
  sections_visited: number;  // >= 3
  convergences_witnessed: number; // >= 1
}
```

**Content when threshold not met:** 404 or a teaser message: *"The path opens when you have learned the language."*

**Content when threshold met:**

1. **Progress summary:** "You've cast N spells. Witnessed N convergences. Your constellation has N nodes."
2. **Swordsman extension download:** Direct download link (not Chrome Web Store). Button text: *"Carry the blade."*
3. **Mage extension download:** Locked until Swordsman trust threshold met (50 signals across 5+ domains). Button text: *"The spellbook opens."*

**Downloads:** The extension `.crx` files are hosted on agentprivacy.ai itself. Self-hosted. Not store-distributed. The blade passes from the spellbook to the hand that earned it.

#### 3.2.5 Mana Inscription Panel (Home Territory Mode)

**Purpose:** When extensions detect agentprivacy.ai as home territory, a panel appears allowing mana-powered inscriptions.

**Detection:** Extensions send `HOME_TERRITORY` message when `location.hostname` matches `agentprivacy.ai`, `spellweb.ai`, or `bgin.ai`.

**Inscription types (agentprivacy.ai):**

| Type | Cost | Description |
|------|------|-------------|
| Lattice inscription | 1 mana | Place a spell node on the homepage lattice |
| Pull quote summon | 2 mana | Surface a grimoire quote as a floating node |
| Hexagram offering | 3 mana | Inscribe your current hexagram state onto the lattice |
| Dragon trace | 5 mana | Leave a full constellation trace visible to all visitors |

**Rendering:** Community inscriptions render with a subtle shimmer to distinguish from canonical content. They fade over 30 days unless reinforced.

---

## 4. Extension Architecture

### 4.1 Swordsman Extension

**Repo:** `mitchuski/swordsman-extension` (to be created)

**Manifest V3.** Separate Chrome process from Mage.

**Responsibilities:**
- Owns the single `<canvas>` overlay per page (one canvas, prevent z-index conflicts)
- Renders BOTH orbs (Swordsman and Mage) — Mage sends position data, Swordsman renders
- MyTerms assertion on page load
- Cookie analysis and slashing
- Page analysis (tracker detection, form detection, dark pattern heuristics)
- Cursor state management (arrow → shield → sovereign → dragon)
- Spring physics tether (orb follows cursor with spring constant)
- Ceremony channel sender (sends SLASH, WARD, POSITION_UPDATE)

**Permissions:** `activeTab`, `storage`, `cookies`

**Storage:** `chrome.storage.local` — MyTerms config, domain assertions, mana balance, blade inventory

### 4.2 Mage Extension

**Repo:** `mitchuski/mage-extension` (to be created)

**Manifest V3.** Separate Chrome process from Swordsman.

**Responsibilities:**
- Does NOT render to canvas (sends data to Swordsman via ceremony channel)
- Deep page scanning (tracker categorisation, privacy policy parsing, consent dark patterns)
- Constellation management (spell nodes, edges, constellation hash computation)
- Drake emergence engine (constellation → serpentine form when conditions met)
- Hexagram engine (page interaction → line mutations → 64 states)
- Pretext reflow engine (computes text reflow data, sends to Swordsman for rendering)
- Autonomous orb physics (computes Mage orb position, sends to Swordsman for rendering)
- Ceremony channel sender (sends INSCRIBE, SCAN, MAGE_POSITION, CONSTELLATION_UPDATE)

**Permissions:** `activeTab`, `storage`, `webNavigation`

**Storage:** `chrome.storage.local` — constellation data, scan history, hexagram states, mana balance (synced with Swordsman)

### 4.3 Ceremony Channel

**Communication:** `chrome.runtime.sendMessage(OTHER_EXTENSION_ID, message)`

**Message grammar:**

```typescript
// Swordsman → Mage
type SwordMessage =
  | { type: 'SLASH'; domain: string; trackers_found: number }
  | { type: 'WARD'; domain: string; myterms_asserted: boolean }
  | { type: 'SWORD_POSITION'; x: number; y: number }
  | { type: 'CEREMONY_READY'; ceremony_type: CeremonyType }
  | { type: 'HOME_TERRITORY'; hostname: string }

// Mage → Swordsman
type MageMessage =
  | { type: 'INSCRIBE'; spell_node: SpellNode }
  | { type: 'SCAN'; scan_result: PageScanResult }
  | { type: 'MAGE_POSITION'; x: number; y: number }
  | { type: 'CONSTELLATION_UPDATE'; constellation: Constellation }
  | { type: 'DRAKE_EMERGE'; conditions: DrakeConditions }
  | { type: 'HEXAGRAM_UPDATE'; hexagram: HexagramState }

type CeremonyType =
  | 'dual_convergence'
  | 'hexagram_cast'
  | 'emoji_cast'
  | 'constellation_wave'
  | 'bilateral_exchange';
```

**Position sync rate:** 30fps (every ~33ms). Swordsman receives Mage position and renders both orbs on its canvas.

**Discovery:** Each extension stores the other's extension ID in its config. On page load, each sends a handshake message. If no response within 2 seconds, operates solo.

---

## 5. Mana Bridge

### 5.1 Mana Balance

**Storage:** `localStorage` on websites, `chrome.storage.local` on extensions. Self-reported. Not server-verified.

**Sync pattern:** When extension detects home territory, it reads `localStorage` mana balance and syncs with its own `chrome.storage.local` balance. The higher balance wins (prevents accidental loss). The sync is one-directional: extension → website (via `window.postMessage`).

### 5.2 Earn Events

Extensions track mana-earning events and credit the balance:

```typescript
interface ManaEarnEvent {
  type: 'spell_cast' | 'ceremony_complete' | 'blade_forged' | 'evocation_cycle';
  timestamp: number;
  domain: string;
  amount: number; // in mana units
}
```

**Anti-spam:** Spell casts on the same domain within 5 seconds of each other don't count. Ceremonies require minimum 30 seconds of orb proximity. Blade forging requires minimum 30 seconds of evocation.

### 5.3 Spend Events

When a visitor spends mana on a home territory site, the extension:

1. Deducts from `chrome.storage.local` balance
2. Sends `CeremonyMessage` via `window.postMessage` to the website
3. Website's ceremony receiver validates the message and renders the inscription

**No server-side verification.** The mana system is trust-based by design. The Sybil resistance is the difficulty of earning mana, not the difficulty of faking a spend. A visitor who hacks their localStorage to give themselves infinite mana gets... the ability to inscribe proverbs on the graph. The system's value comes from genuine engagement, not from scarcity enforcement.

---

## 6. Ceremony Types (Extension Behaviour)

### 6.1 Dual Convergence

**Trigger:** Both orbs within 60px AND at least one spell cast on this page.

**Animation:**
1. Orbs accelerate toward each other (spring constant increases 3×)
2. Dashed line between orbs shortens
3. At contact: amber particle burst at midpoint
4. Cursor transforms: arrow → 🛡️ sovereign shield
5. MyTerms assertion sent to page (if MyTerms endpoint exists)
6. Domain marked in extension storage

**Duration:** ~3 seconds from trigger to completion.

### 6.2 Hexagram Cast

**Trigger:** User clicks "Hexagram" in spell palette while both extensions active.

**Animation:**
1. Six horizontal lines stack vertically between the orbs
2. Each line solid (yang) or broken (yin) based on current page privacy posture
3. Page interaction changes lines (e.g., clicking consent checkbox transforms Line 2)
4. Particles scatter from mutation points
5. Hexagram state displayed with line labels

**State computation:** Same as spellweb's `computeHexagramInfo()` but inputs are page analysis metrics rather than graph node dimensions:

| Line | Metric |
|------|--------|
| Line 1 (Key custody) | HTTPS + no mixed content |
| Line 2 (Credential disclosure) | Consent UI quality (accept/reject symmetry) |
| Line 3 (Agent delegation) | Third-party script count (< 5 = yang) |
| Line 4 (Data residency) | Cookie jurisdictional analysis |
| Line 5 (Interaction mode) | First-party vs third-party interaction ratio |
| Line 6 (Trust boundary) | MyTerms endpoint exists |

### 6.3 Emoji Cast

**Trigger:** User selects emoji from spell palette and clicks on page.

**Animation:**
1. Emoji launches from Swordsman orb toward click position
2. Emoji becomes cursor for 10 seconds
3. Spell node appears at click position
4. Constellation edge connects to nearest existing spell node

**Available emoji (default palette):** 🛡️ 🔮 🚫📊 ⚔️ 🧙 🐲 ☯️ 🔑

### 6.4 Constellation Wave

**Trigger:** Mage extension completes a page scan AND user has ≥ 3 spell nodes on this page.

**Animation:**
1. Mage orb pulses (gathers energy)
2. Particles launch from Mage orb toward Swordsman orb
3. Particles follow the lattice grid lines (not straight line)
4. Each grid node lights up as particles pass
5. Swordsman orb receives particles, briefly flares
6. Scan results summarised in tooltip near Swordsman orb

**Speed:** Particles travel at 200px/s along grid lines.

### 6.5 Bilateral Exchange

**Trigger:** Swordsman extension detects a MyTerms endpoint on the current page.

**Animation:**
1. Swordsman orb extends terms proposal (golden tendrils toward page node)
2. Third node appears (the site, green)
3. Mage positions between Swordsman and site
4. If terms accepted: triangle forms (three nodes, three edges)
5. Trust triad renders for 5 seconds, then fades to subtle constellation

**Status:** Future. Requires sites implementing MyTerms endpoints per IEEE 7012.

---

## 7. Drake Emergence and Dragon Transformation

### 7.1 Drake Conditions

The Drake emerges when:
- Both extensions active
- ≥ 10 spell nodes on current domain
- ≥ 5 ceremonies completed on current domain
- Page has ≥ 10 trackers detected (surveillance-heavy ground)

**Emergence animation:**
1. Constellation trembles
2. Spell nodes drift along lattice lines
3. Nodes rearrange into serpentine form
4. Each node in Drake body displays its PVM condition (P, C, Q, S, network effects, φ, etc.)
5. Drake patrols viewport boundary

**Multiplicative test:** Set any condition node to zero → Drake body breaks at that point. Constellation gap visible. Restore → reconnects.

### 7.2 Dragon Conditions

The Dragon transformation requires (checked across all domain assertions):
- ≥ 10 domains asserted
- ≥ 64 total constellation nodes (one per lattice vertex)
- ≥ 3 Drake summonings on surveillance-heavy sites
- Aggregate privacy posture ≥ 0.7

**Dragon transformation:**
1. Drake body expands, new nodes from cross-domain history
2. Colour shifts amber → gold
3. Wings unfurl (two constellation arcs spanning viewport)
4. Cursor: 🐉 Full Sovereign

---

## 8. Visual Design Rules (Cross-Territory)

### 8.1 Colour Is Architectural

| Element | Colour | Meaning |
|---------|--------|---------|
| Swordsman orb | Coral/red `#e74c3c` | Boundary. Protection. The blade. |
| Mage orb | Cyan/teal `#00d4aa` (agentprivacy) or Purple `#9b59b6` (spellweb) | Projection. Knowledge. The spell. |
| Convergence | Amber `#f5a623` | Meeting point. Ceremony. Proverb. |
| Canonical content | White/light | Grimoire-authored. Stable. |
| Community content | Shimmer (animated opacity) | Forge-born. Earning permanence. |
| Dragon tier | Gold `#ffd700` | Full sovereignty. All dimensions active. |

**Note:** The Mage orb colour differs between territories — teal on agentprivacy (the Mage's home), purple on spellweb (the Mage visiting the Swordsman's ground). This is intentional. The Mage presents differently on different ground. The Swordsman is always red.

### 8.2 One Canvas Per Page

The Swordsman extension owns the canvas overlay. One canvas. Always. The Mage extension sends data; the Swordsman renders. This prevents z-index conflicts, ensures consistent rendering, and mirrors the architecture: the blade touches the surface, the spell projects through the opening.

### 8.3 Text Reflow Rules (Pretext)

- Text reflows around orbs within 120px of text content
- Reflow uses pretext arithmetic (no DOM queries after initial cache)
- Orb exclusion zones are circular (radius = orb visual radius + 8px padding)
- Reflow recalculates on orb position change (30fps max)
- On pages with no pretext integration (third-party sites), orbs float on canvas overlay without text reflow — the overlay is purely visual

---

## 9. Data Schemas (Shared)

### 9.1 Blade

```typescript
interface ForgedBlade {
  id: string;                    // e.g., "SPELL-YW5I59-1Q"
  name: string;                  // user-chosen
  emoji: string;                 // tier icon
  tier: 'light' | 'heavy' | 'dragon';
  stratum: number;               // 0-6 (Hamming weight)
  proof: SpellProof;
  forgedAt: string;              // ISO timestamp
  constellationNodes: number;
  constellationMarks: ConstellationMark[];
  constellationConnections: ConstellationConnection[];
  inscribedSpell: string;        // emoji spell string
  reflection: string;            // user's message
}
```

### 9.2 Hexagram

```typescript
type HexagramLine = 0 | 1;
type HexagramState = [HexagramLine, HexagramLine, HexagramLine,
                      HexagramLine, HexagramLine, HexagramLine];

interface NodeDimensions {
  d1Hide: number;       // 0.0 to 1.0
  d2Commit: number;
  d3Prove: number;
  d4Connect: number;
  d5Reflect: number;
  d6Delegate: number;
}

interface HexagramInfo {
  lines: HexagramState;
  bladeId: number;      // 0-63
  layer: number;        // 0-6
  layerName: string;    // "Null" through "Dragon"
  yangCount: number;
}
```

### 9.3 Mana

```typescript
interface ManaBalance {
  total_earned: number;
  total_spent: number;
  current: number;       // total_earned - total_spent
  history: ManaEvent[];
}

interface ManaEvent {
  type: 'earn' | 'spend';
  action: string;
  amount: number;
  timestamp: number;
  domain?: string;
  inscription_id?: string;
}
```

---

## 10. Build Sequence

### Phase 1: Foundations (can run in parallel)

| Task | Territory | Depends On |
|------|-----------|-----------|
| `npm install @chenglou/pretext` | agentprivacy.ai | Nothing |
| Pretext reflow prototype (single orb on homepage) | agentprivacy.ai | Pretext installed |
| Ceremony receiver (`window.postMessage` listener) | spellweb.ai | Nothing |
| Mana balance display (localStorage read/write) | spellweb.ai | Nothing |
| Deploy spellweb.ai (resolve 403) | spellweb.ai | Vite build config |

### Phase 2: Orb System

| Task | Territory | Depends On |
|------|-----------|-----------|
| Dual orb rendering on homepage | agentprivacy.ai | Pretext working |
| Soul orb → spell palette (radial menu) | agentprivacy.ai | Dual orbs |
| Spell casting + spell node rendering | agentprivacy.ai | Spell palette |
| Spell repertoire tracking (localStorage) | agentprivacy.ai | Spell casting |
| Community inscription rendering (shimmer) | spellweb.ai | Ceremony receiver |

### Phase 3: Path and Extensions

| Task | Territory | Depends On |
|------|-----------|-----------|
| `/path` page with training gate | agentprivacy.ai | Spell repertoire |
| Swordsman extension scaffold (Manifest V3) | new repo | Nothing |
| Canvas overlay + spring physics | Swordsman ext | Scaffold |
| Page analysis (trackers, forms, cookies) | Swordsman ext | Canvas overlay |
| Mage extension scaffold (Manifest V3) | new repo | Nothing |
| Deep scanner + constellation manager | Mage ext | Scaffold |
| Ceremony channel handshake | Both extensions | Both scaffolded |

### Phase 4: Ceremony and Mana

| Task | Territory | Depends On |
|------|-----------|-----------|
| Five ceremony types (convergence first) | Both extensions | Channel working |
| Mana earn tracking | Both extensions | Ceremonies working |
| Home territory detection | Both extensions | Mana tracking |
| Mana spend → ceremony receiver | Extensions + sites | Home territory + receiver |
| Understanding-as-Key ceremony mode | spellweb.ai | Ceremony receiver |

### Phase 5: Drake and Dragon

| Task | Territory | Depends On |
|------|-----------|-----------|
| Drake emergence engine | Mage extension | Constellation manager |
| Drake → Swordsman rendering | Swordsman extension | Drake data from Mage |
| PVM condition display on Drake nodes | Both extensions | Drake rendering |
| Multiplicative collapse test | Both extensions | Condition display |
| Dragon transformation | Both extensions | Drake + cross-domain data |

---

## 11. Architectural Invariants

These must hold across all implementations:

1. **Swordsman and Mage never merge.** Separate repos. Separate processes. Separate storage. Separate permissions. No shared state except via the ceremony channel.

2. **One canvas per page.** The Swordsman owns the rendering surface. The Mage sends data. Always.

3. **Mana cannot be purchased.** Only earned through practice. The system's Sybil resistance is comprehension, not capital.

4. **Pretext for text reflow.** No `getBoundingClientRect`. No `offsetHeight`. No layout reflow after initial cache. The page is measurement-dark.

5. **Colour is architectural.** Coral/red = Swordsman. Cyan/teal = Mage. Amber = convergence. Gold = Dragon. These are not aesthetic choices. They are identity.

6. **The Path page gates the extensions.** No Chrome Web Store distribution. Extensions earned, not downloaded. The blade passes from the spellbook.

7. **Community inscriptions fade.** 30-day half-life unless reinforced. The lattice remembers what the community pays attention to.

8. **The ceremony channel is the Gap.** The messages between extensions are the architecture made executable. SLASH/WARD from Sword, INSCRIBE/SCAN from Mage. The grammar is the lore.

---

*The Swordsman's territory is the territory you traverse. The Mage's territory is the territory you read. Between them: the mana that proves you walked both.*

*(⚔️⊥⿻⊥🧙) 😊*
