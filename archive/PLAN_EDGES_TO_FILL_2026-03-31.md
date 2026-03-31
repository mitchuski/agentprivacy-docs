# Plan: Edges to Fill

## Post-Chronicle Implementation Roadmap
**Date:** March 31, 2026
**Context:** Following the Dragon's Anatomy and Flight (Acts XXVII–XXIX)
**Master inscription:** `(⚔️⊥⿻⊥🧙)😊`

---

## Where We Got To

The weekend produced:
- 23 documents, ~65,000 words
- 3 Acts inscribed (XXVII, XXVIII, XXIX)
- Grimoire 8.8.0 → 9.2.0 (pending application)
- Dragon anatomy complete + flight begun

**Implementation status: ~70% built**

| Component | Status | Location |
|-----------|--------|----------|
| Spellweb ceremony visualization | Operational | `spellweb/` |
| Dual-agent extension scaffold | Built | `swordsman-blade/`, `mages-spell/` |
| Inter-extension ceremony channel | Implemented | Both extensions |
| Training grounds website | Built & exported | `agentprivacy_master/` |
| Ceremony wizard + Soulbae chat | Working | `agentprivacy_master/` |
| Chronicle synchronized | Complete | All 8 locations |

---

## The Eight Edges

These are the gaps between specification and implementation—the bridges not yet wired.

---

### Edge 1: The Path Page Gate

**What's specified:**
`/path` is the gate where extensions become available when training criteria are met. "Earned, not downloaded."

**What exists:**
Routes for `/ceremony`, `/evoke`, `/orbs` but no `/path` route.

**To fill:**
```
Location: agentprivacy_master/src/app/path/page.tsx

Requirements:
1. Training completion checker (query ceremony storage)
2. Criteria display (what's been earned, what remains)
3. Extension download links (locked until criteria met)
4. Mana balance display
5. Path visualization showing progression

Dependencies:
- Mana economy storage (Edge 6)
- Training completion events from /ceremony
```

**Owner:** agentprivacy_master
**Priority:** Immediate (gate must exist before extensions deploy)

---

### Edge 2: Extension ↔ Website Bridge

**What's specified:**
Blades forged in extensions flow to spellweb ceremony receiver for persistence.

**What exists:**
- `swordsman-blade/src/content/ceremony-channel.ts` handles extension↔extension
- No bridge to website ceremony receiver

**To fill:**
```
Location: Both extensions + spellweb

Requirements:
1. Content script message to window.postMessage bridge
2. Spellweb listener for BLADE_FORGED events
3. Ceremony receiver storage adapter
4. Blade inventory sync between extension and web

Pattern:
  Extension → window.postMessage → spellweb event listener → ceremony receiver → storage

Dependencies:
- spellweb.ai deployed (Edge 5)
- Ceremony receiver route on spellweb
```

**Owner:** swordsman-blade (primary), spellweb (receiver)
**Priority:** High

---

### Edge 3: Act Separation in Docs

**What's specified:**
Acts XXVII, XXVIII, XXIX as standalone navigable documents.

**What exists:**
Acts embedded in `spellbook-canonical.md` (65.9KB monolith).

**To fill:**
```
Location: agentprivacy_master/src/app/story/ + agentprivacy-docs/

Requirements:
1. Extract act-xxvii-the-swordsmans-forge.md
2. Extract act-xxviii-the-ceremony-engine.md
3. Extract act-xxix-the-dragon-wakes.md
4. Add routes: /story/xxvii, /story/xxviii, /story/xxix
5. Act navigation component with previous/next
6. Link from spellbook table of contents

Files to create:
- agentprivacy-docs/acts/act-xxvii-the-swordsmans-forge.md
- agentprivacy-docs/acts/act-xxviii-the-ceremony-engine.md
- agentprivacy-docs/acts/act-xxix-the-dragon-wakes.md
```

**Owner:** agentprivacy-docs (source), agentprivacy_master (routes)
**Priority:** High

---

### Edge 4: Hexagram Visualization

**What's specified:**
Node inspector showing hexagram states in real-time. Six dimensions binarized at 0.5 threshold → I Ching hexagram. Blade 63 = 乾 (The Creative).

**What exists:**
- Math in `SYSTEMS_HEXAGRAM_PHYSICS.md`
- Blade forge calculates 6 dimensions
- No hexagram rendering in UI

**To fill:**
```
Location: spellweb/src/components/

Requirements:
1. HexagramDisplay component
   - 6 horizontal lines (solid/broken based on dimension > 0.5)
   - I Ching number (0-63)
   - Traditional name lookup (乾, 坤, etc.)

2. Integration points:
   - Node inspector tooltip
   - Blade forge result panel
   - Ceremony completion screen

3. Hexagram transition visualization
   - Show which lines change between states
   - Animate the transformation

Data structure:
  dimensions: [d1Hide, d2Opt, d3Forget, d4Connect, d5Compute, d6Delegate]
  threshold: 0.5
  hexagram: dimensions.map(d => d > 0.5 ? 1 : 0).join('') → binary → decimal
```

**Owner:** spellweb
**Priority:** Medium (enhances understanding, not blocking)

---

### Edge 5: spellweb.ai Deployment

**What's specified:**
Public forge accessible at spellweb.ai

**What exists:**
- `dist/` folder with production build (476KB)
- 403 error on live domain

**To fill:**
```
Location: spellweb/

Requirements:
1. Verify Vercel/hosting configuration
2. Check domain DNS settings
3. Verify build output matches expected routes
4. Deploy and confirm 200 on all routes

Verification:
- GET spellweb.ai → 200
- GET spellweb.ai/ceremony → 200
- Orb animation renders
- Ceremony channel accepts connections
```

**Owner:** spellweb
**Priority:** Immediate (blocking extension bridge)

---

### Edge 6: Mana Economy Flow

**What's specified:**
- Mana earned through training (mage-x-feed-filter)
- Mana spent on ceremony unlocks
- Proof of practice, not proof of capital

**What exists:**
- Mana depletion visualization in spellweb ceremony
- No persistent balance
- No earning mechanism wired

**To fill:**
```
Location: agentprivacy_master + spellweb + mage-x-feed-filter

Requirements:
1. Mana storage schema
   - userId/ceremonyId
   - balance: number
   - earnedFrom: [{source, amount, timestamp}]
   - spentOn: [{ceremony, amount, timestamp}]

2. Earning events:
   - Training module completion → +mana
   - Blade forge completion → +mana
   - Bilateral witness → +mana

3. Spending gates:
   - Extension unlock requires mana threshold
   - Advanced ceremony types require mana

4. Display:
   - /path page shows balance
   - Ceremony start shows cost
   - Insufficient mana shows earning path

Storage options:
- localStorage (prototype)
- IndexedDB (production)
- Server-side (if account system exists)
```

**Owner:** agentprivacy_master (storage), mage-x-feed-filter (earning), spellweb (spending)
**Priority:** Medium

---

### Edge 7: Understanding-as-Key for Strangers

**What's specified:**
Five-step ceremony proving comprehension without prior relationship:
1. Language capture
2. Constellation mapping
3. Simultaneous blade forging
4. Proverb inscription
5. Bilateral witness

**What exists:**
- Worked for known parties (Soulbae bilateral witness)
- No stranger-to-stranger protocol

**To fill:**
```
Location: spellweb + ceremony spec

Requirements:
1. Stranger matching mechanism
   - Queue of ceremony participants
   - Anonymous pairing based on constellation overlap

2. Verification without identity:
   - Blade signatures compared
   - Constellation paths compared
   - Proverb inscription compared
   - Match score threshold

3. Witness record format:
   - No names, only blade signatures
   - Proof that two independent forgers reached same state
   - Timestamp and constellation hash

4. UX flow:
   - "Join stranger ceremony" button
   - Waiting room with anonymous count
   - Paired when compatible constellation found
   - Side-by-side forging view
   - Comparison reveal at end

Dependencies:
- WebSocket or real-time sync for simultaneous forging
- May require server component
```

**Owner:** spellweb
**Priority:** Lower (advanced feature, needs ceremony mode working first)

---

### Edge 8: GitNexus/KuzuDB Integration

**What's specified:**
Knowledge graph persists to WASM database. LangChain ReAct agent integration.

**What exists:**
- `SPELLWEB_INTEGRATION_SPEC.md` (150+ lines)
- D3.js graph renders in memory
- No persistence layer

**To fill:**
```
Location: spellweb/src/lib/

Requirements:
1. KuzuDB WASM adapter
   - Initialize database in browser
   - Schema for nodes, edges, blades
   - CRUD operations

2. Graph sync:
   - Load from DB on mount
   - Save node additions
   - Save edge creations
   - Save blade associations

3. Query interface:
   - Find paths between nodes
   - Get blades by constellation
   - Get ceremonies by participant

4. Optional: LangChain integration
   - ReAct agent with graph context
   - Natural language graph queries
   - Soulbae integration for guided exploration

Dependencies:
- @aspect-build/kuzu-wasm or equivalent
- May require build config changes for WASM
```

**Owner:** spellweb
**Priority:** Lower (enhancement, not blocking core ceremony)

---

## Execution Order

```
Phase 1: Deployment (Immediate)
├── Edge 5: Deploy spellweb.ai (resolve 403)
└── Edge 3: Extract Acts XXVII-XXIX to standalone files

Phase 2: Gates (High Priority)
├── Edge 1: Build /path page
├── Edge 2: Wire extension→website bridge
└── Edge 6: Implement mana storage

Phase 3: Enhancement (Medium Priority)
├── Edge 4: Add hexagram visualization
└── Edge 6: Wire mana earning/spending

Phase 4: Advanced (Lower Priority)
├── Edge 7: Stranger ceremony protocol
└── Edge 8: KuzuDB persistence
```

---

## Per-Repository Checklist

### agentprivacy_master
- [ ] Create `/path` route (Edge 1)
- [ ] Add story routes for Acts XXVII-XXIX (Edge 3)
- [ ] Implement mana storage (Edge 6)

### spellweb
- [ ] Resolve 403 deployment (Edge 5)
- [ ] Add ceremony receiver for extension bridge (Edge 2)
- [ ] Add hexagram display component (Edge 4)
- [ ] Add stranger ceremony mode (Edge 7)
- [ ] Add KuzuDB adapter (Edge 8)

### swordsman-blade
- [ ] Add window.postMessage bridge to website (Edge 2)
- [ ] Add blade export for persistence (Edge 2)

### mages-spell
- [ ] Add window.postMessage bridge to website (Edge 2)
- [ ] Wire training completion to mana earning (Edge 6)

### agentprivacy-docs
- [ ] Extract Act XXVII to standalone file (Edge 3)
- [ ] Extract Act XXVIII to standalone file (Edge 3)
- [ ] Extract Act XXIX to standalone file (Edge 3)
- [ ] Apply grimoire patches v9.0.0 → v9.2.0

---

## Coherence Note

The fractal separation holds at every scale:

| Edge | Swordsman Territory | Mage Territory |
|------|--------------------| ---------------|
| 1 | — | /path gate |
| 2 | Extension bridge sender | Website receiver |
| 3 | — | Act narratives |
| 4 | Hexagram state | — |
| 5 | spellweb.ai deployment | — |
| 6 | Spending | Earning |
| 7 | Stranger matching | Comprehension proof |
| 8 | Graph topology | Query interface |

The edges are at the bridges. The territories are coherent within themselves.

---

*The dragon has its body and learned to fly—these are the wings waiting to be attached.*

`(⚔️⊥⿻⊥🧙)😊`
