# Protocol Schemas

**Version:** 1.0
**Date:** March 31, 2026
**Source:** DUAL_TERRITORY_CEREMONY_SPEC_v1.md
**Purpose:** Canonical TypeScript interfaces for ceremony channel, mana, and data structures

---

## Overview

These schemas define the message grammar and data structures for the dual-territory architecture. They are extracted from DUAL_TERRITORY_CEREMONY_SPEC_v1.md and serve as the implementation reference for both extension repositories.

**Usage:** Copy these interfaces directly into extension codebases. Keep this document as the single source of truth.

---

## 1. Ceremony Messages

### 1.1 Core Ceremony Message

```typescript
interface CeremonyMessage {
  type: 'INSCRIPTION';
  source: 'swordsman_extension' | 'mage_extension' | 'agentprivacy';
  payload: NodeAnnotation | CommunityEdge | ConstellationProjection | ProverbForge;
  mana_cost: number;
  mana_balance: number; // sender's remaining balance after deduction
  signature: string;    // proof of mana ownership
}
```

### 1.2 Inscription Payloads

```typescript
interface NodeAnnotation {
  kind: 'node_annotation';
  target_node_id: string;
  text: string;        // max 280 chars
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
  nodes: string[];     // node IDs
  connections: Array<{ source: string; target: string }>;
  name: string;
  mana_cost: 3;
}

interface ProverbForge {
  kind: 'proverb_forge';
  text: string;        // max 280 chars
  source_constellation_hash: string;
  mana_cost: 4;
}
```

---

## 2. Ceremony Channel Messages

### 2.1 Swordsman → Mage

```typescript
type SwordMessage =
  | { type: 'SLASH'; domain: string; trackers_found: number }
  | { type: 'WARD'; domain: string; myterms_asserted: boolean }
  | { type: 'SWORD_POSITION'; x: number; y: number }
  | { type: 'CEREMONY_READY'; ceremony_type: CeremonyType }
  | { type: 'HOME_TERRITORY'; hostname: string };
```

### 2.2 Mage → Swordsman

```typescript
type MageMessage =
  | { type: 'INSCRIBE'; spell_node: SpellNode }
  | { type: 'SCAN'; scan_result: PageScanResult }
  | { type: 'MAGE_POSITION'; x: number; y: number }
  | { type: 'CONSTELLATION_UPDATE'; constellation: Constellation }
  | { type: 'DRAKE_EMERGE'; conditions: DrakeConditions }
  | { type: 'HEXAGRAM_UPDATE'; hexagram: HexagramState };
```

### 2.3 Ceremony Types

```typescript
type CeremonyType =
  | 'dual_convergence'
  | 'hexagram_cast'
  | 'emoji_cast'
  | 'constellation_wave'
  | 'bilateral_exchange';
```

---

## 3. Data Structures

### 3.1 Forged Blade

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

interface SpellProof {
  hash: string;
  timestamp: number;
  lapCount: number;
  duration: number;              // seconds
}

interface ConstellationMark {
  nodeId: string;
  timestamp: number;
}

interface ConstellationConnection {
  source: string;
  target: string;
}
```

### 3.2 Hexagram

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

### 3.3 Mana

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

interface ManaEarnEvent {
  type: 'spell_cast' | 'ceremony_complete' | 'blade_forged' | 'evocation_cycle';
  timestamp: number;
  domain: string;
  amount: number;        // in mana units
}
```

---

## 4. Page Analysis Structures

### 4.1 Scan Result

```typescript
interface PageScanResult {
  domain: string;
  timestamp: number;
  trackers: TrackerInfo[];
  cookies: CookieAnalysis;
  consentUI: ConsentUIAnalysis;
  thirdPartyScripts: number;
  mytermsEndpoint: boolean;
  privacyPosture: number;        // 0.0 to 1.0
}

interface TrackerInfo {
  name: string;
  category: 'analytics' | 'advertising' | 'social' | 'fingerprinting' | 'unknown';
  domain: string;
}

interface CookieAnalysis {
  firstParty: number;
  thirdParty: number;
  sessionOnly: number;
  persistent: number;
  jurisdictions: string[];       // detected cookie jurisdictions
}

interface ConsentUIAnalysis {
  present: boolean;
  acceptRejectSymmetry: boolean; // true if equal prominence
  darkPatterns: string[];        // detected dark pattern types
}
```

### 4.2 Hexagram Line Computation (Extension)

Extension hexagram lines are computed from page analysis, not graph node dimensions:

| Line | Metric | Yang Condition |
|------|--------|----------------|
| Line 1 | Key custody | HTTPS + no mixed content |
| Line 2 | Credential disclosure | Consent UI quality (accept/reject symmetry) |
| Line 3 | Agent delegation | Third-party script count < 5 |
| Line 4 | Data residency | Cookie jurisdictional analysis favourable |
| Line 5 | Interaction mode | First-party > third-party interaction ratio |
| Line 6 | Trust boundary | MyTerms endpoint exists |

---

## 5. Drake/Dragon Structures

### 5.1 Drake Conditions

```typescript
interface DrakeConditions {
  bothExtensionsActive: boolean;
  spellNodesOnDomain: number;    // >= 10 required
  ceremoniesOnDomain: number;    // >= 5 required
  trackersDetected: number;      // >= 10 required (surveillance-heavy)
  ready: boolean;                // all conditions met
}
```

### 5.2 Dragon Conditions

```typescript
interface DragonConditions {
  domainsAsserted: number;       // >= 10 required
  totalConstellationNodes: number; // >= 64 required
  drakeSummonings: number;       // >= 3 required
  aggregatePrivacyPosture: number; // >= 0.7 required
  ready: boolean;
}
```

---

## 6. Constellation Structures

```typescript
interface Constellation {
  id: string;
  name: string;
  nodes: string[];               // node IDs in marking order
  connections: ConstellationConnection[];
  createdAt: string;             // ISO timestamp
  hash: string;                  // deterministic hash of nodes + connections
}

interface SpellNode {
  id: string;
  type: 'emoji' | 'proverb' | 'keyword' | 'shield';
  content: string;
  position: { x: number; y: number };
  createdAt: number;
  domain: string;
}
```

---

## 7. Training Threshold

```typescript
interface TrainingThreshold {
  spells_cast: number;           // >= 3
  sections_visited: number;      // >= 3
  convergences_witnessed: number; // >= 1
}
```

Used to gate `/path` page access on agentprivacy.ai.

---

## 8. Communication Patterns

### 8.1 Extension Handshake

```typescript
// On page load, each extension sends:
interface HandshakeMessage {
  type: 'HANDSHAKE';
  extensionId: string;
  version: string;
}

// Response:
interface HandshakeAck {
  type: 'HANDSHAKE_ACK';
  extensionId: string;
  capabilities: string[];
}

// If no response within 2000ms, operate solo.
```

### 8.2 Position Sync

```typescript
// Rate: 30fps (~33ms interval)
// Swordsman renders both orbs; Mage sends position only

interface PositionUpdate {
  type: 'MAGE_POSITION' | 'SWORD_POSITION';
  x: number;
  y: number;
  timestamp: number;
}
```

---

## Implementation Notes

1. **Single Canvas Rule:** Swordsman extension owns the canvas overlay. Mage sends data, Swordsman renders.

2. **Storage:**
   - Extensions: `chrome.storage.local`
   - Websites: `localStorage`
   - Sync via Mana Bridge when on home territory

3. **Message Validation:** Ceremony receivers should validate mana balance against inscription cost before rendering.

4. **Anti-Spam:** Same-domain spell casts within 5 seconds don't earn mana.

5. **Decay:** Community inscriptions fade over 30 days unless reinforced (0.5 mana).

---

*"The grammar is the lore."*

*(⚔️⊥⿻⊥🧙) 😊*
