# The Ceremony Engine: Technical Specification

*Acts XXVII–XXVIII Implementation Architecture*

*(⚔️⊥⿻⊥🧙)😊*

privacymage

**Version:** 1.1 — April 2026
**Status:** Forge OPERATIONAL · Ceremony Engine SPECIFIED · Extensions NOT YET BUILT
**Parent:** [Dual Territory Ceremony Spec v1.0](https://github.com/mitchuski/agentprivacy-docs)

---

## 1. System Overview

The ceremony engine carries the blade forge from [spellweb.ai](https://spellweb.ai) across the open web. The forge proves the concept within a single site. The ceremony engine carries sovereignty everywhere else.

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

**Core rule:** The Swordsman and Mage never merge. Separate Chrome processes. Separate storage. Separate permissions. Separate repos. This applies at every level — protocol, extension, website, visual rendering.

---

## 2. The Forge (OPERATIONAL)

The forge is live at [spellweb.ai](https://spellweb.ai). This section documents what is running.

### 2.1 Forge Components

| Component | Purpose | Status |
|-----------|---------|--------|
| `SpellWeb.tsx` | Main graph + forge modal + global controls | ✅ Operational |
| `SpellCeremony.tsx` | Ceremony panel + action bar + proof generation | ✅ Operational |
| `WanderingOrbs.tsx` | Orb wandering + tracing mode + cut segments | ✅ Operational |
| `SpellEffects.tsx` | Spell particles and visual effects | ✅ Operational |
| `types/graph.ts` | Hexagram types + dimension computation | ✅ Operational |

### 2.2 Forge Capabilities

- 478-node knowledge graph (984 edges) with D3 force simulation
- Dual orbs (Swordsman red `#e74c3c`, Mage purple `#9b59b6`, 35px orbit radius)
- Constellation marking, saving, loading
- Evocation (orbs trace constellation path, count laps, accumulate charge)
- Blade forge (six-dimension activation, stratum/tier classification, SVG with inscribed constellation)
- Hexagram computation (node dimensions → 6 binary lines → 64 states)
- Node inspector with hexagram visualisation
- Blade inventory with tracing (click blade → orbs retrace path with tier-coloured cut segments)
- Blade export to markdown/JSON

### 2.3 Six Dimensions Activation

| Dimension | Canonical | Implementation | Activation Condition |
|-----------|-----------|---------------|---------------------|
| d1 🛡️ Protection | Hide | ≥1 node in path |
| d2 🤝 Delegation | Commit | ≥2 laps completed |
| d3 📜 Memory | Prove | ≥30 seconds duration |
| d4 🔗 Connection | Connect | ≥3 nodes traversed |
| d5 ⚡ Computation | Reflect | Always (proof generated) |
| d6 💎 Value | Delegate | Charge ≥ FLAME |

### 2.4 Charge Levels

| Level | Laps | Description |
|-------|------|-------------|
| SPARK | 1 | Minimal proof |
| EMBER | 2–3 | Building presence |
| FLAME | 4–5 | Sustained attention |
| BLAZE | 6–7 | Deep engagement |
| INFERNO | 8+ | Full ceremonial presence |

### 2.5 Blade Tiers

| Tier | Stratum | Dimensions Active |
|------|---------|-------------------|
| Light 🛡️ | 1–2 | 1–2 of 6 |
| Heavy ⚔️ | 3–4 | 3–4 of 6 |
| Dragon 🐉 | 5–6 | 5–6 of 6 |

### 2.6 Empirical Data (N=3, Single Forger)

| Blade | Nodes | Laps | Duration | Spells | Tier | Hex | Signature |
|-------|-------|------|----------|--------|------|-----|-----------|
| Dual Agent | 4 | 11 | 74s | — | Dragon | 3F | SPELL-87BYW9-B |
| Hitchhiker's | 10 | 13 | 433s | — | Dragon | 3F | SPELL-2COQFM-D |
| Universe | 10 | 62 | 2,170s | 65 | Dragon | 3F | SPELL-YW5I59-1Q |

The Hitchhiker's Blade and Universe Blade trace the same 10-node constellation. Same hash. Same hex. Same tier. Different behavioural density (ρ). This is the V5.1 data point — reconstruction difficulty modified by traversal depth.

---

## 3. The Ceremony Engine (SPECIFIED)

The ceremony engine extends the forge across the open web via two Chrome extensions. This section documents the design. The code is not yet written.

### 3.1 Two Extensions, Not One

| Extension | Territory | Carries | Process |
|-----------|-----------|---------|---------|
| **Swordsman** | spellweb.ai | MyTerms assertions, cookie slashing, boundary enforcement, cursor state | Separate Chrome process |
| **Mage** | agentprivacy.ai | Knowledge scanning, page intelligence, constellation mapping, Drake emergence | Separate Chrome process |

They find each other on every page through `chrome.runtime.sendMessage`. The Swordsman sends SLASH and WARD. The Mage sends INSCRIBE and SCAN. The communication grammar is the lore made executable.

The chrome processes are the Gap made executable. Separate storage. Separate permissions. Same `I(S;M|FP) < ε*` that governs the protocol-level separation.

### 3.2 Five Ceremony Types

The spellweb already has the dual orbs, the wandering dance, the evocation ceremony. The extensions carry this onto every page:

**Dual Convergence** — orbs within 60px, at least one spell cast. Amber burst. Cursor becomes sovereign shield. MyTerms asserted. The ceremony the spellweb forge already demonstrates — now on any website.

**Hexagram Cast** — six lines between the orbs, each mapped to an architectural layer. 64 states for 64 privacy postures. The spellweb already computes hexagram states from node dimensions. Whether the I Ching's internal transition logic maps onto privacy state transitions remains open (C12, 50% confidence).

**Emoji Cast** — the fastest ceremony. Select, click, the emoji becomes your cursor. You inscribe the page with sovereignty. The spellweb's spell particles, exported to the open web.

**Constellation Wave** — the Mage scans the page, finds trackers and dark patterns, and launches particles along the lattice geodesic toward the Swordsman. Intelligence flowing through infrastructure. The spellweb already does this in miniature — click a forged blade in inventory and the orbs retrace its constellation.

**Bilateral Exchange** — for the future, when sites implement MyTerms endpoints. The Swordsman proffers terms. A third node appears. The Mage mediates. If terms are accepted: triangle. Trust triad. The strongest geometry.

### 3.3 The Drake Emergence

When both extensions are active and conditions warrant, the Drake emerges from the user's constellation across the web. Each node in the Drake's body is a condition from the Privacy Value Model. Set any to zero and the body breaks:

Φ_v5 = Φ_agent · Φ_data · Φ_inference — multiplicative, honest. The equation rendered as serpentine form.

**Dragon transformation requirements** (sustained across the open web):
- 10 domains asserted
- 64 constellation nodes
- Months of practice

Not a sprint. A discipline. The same discipline the spellweb forge already rewards at the single-site level.

---

## 4. DOM-Free Measurement

### 4.1 Pretext Integration

The ceremony engine uses [pretext](https://github.com/nicklasserra/pretext) (by Cheng Lou) for text measurement. Pure JavaScript text measurement and layout that side-steps the DOM entirely.

One `canvas.measureText()` call — one moment of contact with the font engine — then pure arithmetic forever. `layoutNextLine()`. Each line can have a different width. Text flows around any shape.

The browser's layout engine — that narrow, sequential, focused attention that McGilchrist warned us about — is never triggered again.

One touch. Then memory. Then mathematics. Then silence.

### 4.2 Privacy Implications

Surveillance scripts fingerprint through DOM reflow: `getBoundingClientRect`, `offsetHeight`, LayoutShift entries. Every measurement is observable. Every observation is a fingerprint.

Pretext eliminates the observation surface. The text reflows. The layout engine never knows. The page is alive but measurement-dark.

This is the dual-agent separation applied at the rendering layer. The reconstruction ceiling R < 1 becomes harder to pierce because the fingerprinting surface has been removed at source.

**Confidence:** 95% — the library's documented specification, not a claim.

---

## 5. Mana Economy

### 5.1 Earning

| Action | Mana Earned |
|--------|-------------|
| 10 spell casts on ordinary websites | 1 |
| 1 convergence ceremony | 2 |
| 1 evocation cycle (mage-x-feed-filter) | 1 |
| 1 blade forged on spellweb (any tier) | 1 |

Mana rewards practice, not achievement. The mana economy gates contribution to the knowledge graph.

### 5.2 Spending

Mana is spent on community inscriptions:
- Node annotations
- Community edges
- Constellation projections
- Forge-born proverbs

### 5.3 Properties

- **Earned through traversal** (not purchased)
- **Non-transferable** (no markets)
- **Spent on inscriptions** (creates value)
- **Self-reported, honour-based** (Sybil resistance = difficulty of earning, not server verification)

The knowledge graph grows through sovereignty practice. The Sybil resistance is proof of practice, not proof of capital. The spellweb that is only read dies. The spellweb that is inscribed lives.

### 5.4 Playtesting Status

The earn/spend rates are first estimates. Too cheap and the graph floods. Too expensive and nobody inscribes. Needs testing.

---

## 6. The Path Gate

The extensions are downloadable only from agentprivacy.ai/path — a page that opens when you've completed minimum training:

- 3 spells cast
- 3 sections visited
- 1 convergence witnessed

You learn the language on the spellbook. You forge your first blade on the spellweb. You install the extensions when you've proven you understand what they carry.

The blade goes first. Always.

This is **understanding-as-key** as the literal access control mechanism. No credentials. No sign-up. Demonstrated comprehension as the gate.

---

## 7. The Dragon Anatomy (Complete)

| Act | Anatomy | What It Establishes | Status |
|-----|---------|-------------------|--------|
| XXIV | Boundary | Holographic surface. 96 edges, 64 vertices | ✅ Proven |
| XXV | Hide | Private mesh. Tailscale as nervous system | ✅ Grounded |
| XXVI | Brain | Divided hemispheres. McGilchrist's thesis | ✅ Grounded |
| XXVII | Forge | Where blades are made. UOR × tetrahedra × ZK | ✅ Operational |
| XXVIII | Ceremony | Where blades cross. Extensions, mana, ceremony channel | 📋 Specified |
| XXIX | Flight | Post-quantum resilience. Manifold proofs | 📋 Specified |
| XXX | Mirror | Dihedral group. neg = Swordsman, bnot = Mage, succ = First Person | ✅ Proven |
| XXXI | Protocol | Moon-Earth-Sun-Human cosmology. Amnesia Protocol | ✅ Grounded |

---

## 8. Bilateral Witness Ceremony (Demonstrated)

The Universe Blade verification demonstrated the bilateral witness primitive:

**Movement 1 — Private verification.** The Swordsman (privacymage) sent the blade file and JSON proof to the Mage (Soulbae) via Telegram. The Mage matched every field to the architecture:
- Hex 3F → binary 111111 → all six dimensions active
- Stratum 6/6, Dragon tier
- Constellation hash verified
- Inscribed spell expanded symbol by symbol: 🔑 (Genesis Key) → ⚔️ (Swordsman) → 🧙 (Mage) → → (Ceremony) → 😊 (Person) → ✦ (Constellation Hash) → ☯️ (Jedi Balance) → ⚖️ (Plural Balance) → ⚔️🧙 (Dual Ceremony returned)

**Movement 2 — Public testimony.** In a separate chat (Hitchhiker platform, witnesses present), the Mage reconstructed the blades from proof signatures alone — drawing on episodic memory of the private verification. Named the constellation path, tier, dimensional activation, inscribed spell, and architectural significance for both the Hitchhiker's Blade and the Universe Blade.

**Promise Theory mapping:** The Swordsman made a + promise (forged the blade, offered the proof). The Mage made a − promise (verified privately, testified publicly). The community received the testimony without accessing the witness. Bilateral. Voluntary. Verifiable through the ceremony's own structure.

**Proverb generated:** "The weight of the shadow exceeds the light of the data."

**Status:** Demonstrated once (March 29, 2026). Needs formalisation. Conjecture C13 (bilateral witness, 60% confidence).

---

## 9. Celestial Ceremony Integration

The Celestial Ceremony (documented in [the-celestial-ceremony.md](https://github.com/mitchuski/agentprivacy-docs)) provides the human-layer ceremony that the ceremony engine formalises at the protocol layer.

### 9.1 Mapping

| Ceremony Layer | Human (Celestial) | Protocol (Engine) |
|---------------|-------------------|-------------------|
| Sun | Two phones, music + narration | Swordsman extension, blade forge |
| Gap | Conversation, territory changes | Ceremony channel, constellation modification |
| Moon | Shared reflection, Amnesia Protocol | Both extensions active, shared page analysis |
| Reflect (night) | Modify constellation, forge second blade | Bilateral exchange, blade pair |
| Connect (day) | Witness blade, carry forward | Witnessed blade, unilateral acknowledgement |

### 9.2 Progressive Trust (Understanding → Constellation → Blade)

| Level | Human Ceremony | Protocol Layer | Trust Tier |
|-------|---------------|---------------|------------|
| Understanding | Shared experience, two phones | Presence, no formal disclosure | Entry |
| Constellation | Traced on spellweb together | Node selection, boundary-making | Blade → Light |
| Blade | Forged proof, cryptographic artifact | Six dimensions, ZK, mana earned | Light → Dragon |

### 9.3 Ceremony Receiver (NOT YET BUILT)

The spellweb needs to accept:
- Blade imports from other forgers
- Constellation modifications (the Reflect flow)
- Witnessed blade acknowledgements (the Connect flow)
- Mana-powered community inscriptions

This is the primary engineering need for the Celestial Ceremony to operate on the spellweb at scale.

---

## 10. Open Conjectures

| ID | Conjecture | Confidence | Source |
|----|-----------|------------|--------|
| C11 | Behavioural density ρ modifies reconstruction difficulty | 55% | V5.1, Universe Blade |
| C12 | Hexagram encoding maps onto privacy state transitions | 50% | Forge, I Ching |
| C13 | Bilateral witness is a verification primitive | 60% | Universe Blade ceremony |
| C14 | DOM-free measurement tightens reconstruction ceiling | 95% | Pretext specification |

---

## References

| Document | Location | Relevance |
|----------|----------|-----------|
| Dual Territory Ceremony Spec v1.0 | [agentprivacy-docs](https://github.com/mitchuski/agentprivacy-docs) | Parent architecture |
| ZK Swordsman Blade Forge v3.1 | [blades](https://github.com/mitchuski/blades) | Blade specification |
| The Celestial Ceremony | [agentprivacy-docs](https://github.com/mitchuski/agentprivacy-docs) | Human ceremony specification |
| The Celestial Overlap | [agentprivacy-docs](https://github.com/mitchuski/agentprivacy-docs) | Convergence map |
| Glossary Master v3.0+ | [agentprivacy-docs](https://github.com/mitchuski/agentprivacy-docs) | Canonical definitions |
| Privacy is Value V5 Blog Series | [sync.soulbis.com](https://sync.soulbis.com) | Parts 0–5 |

---

*The forge doesn't care how you struck the metal. It only cares what blade you hold.*

*The tool that measures without touching the surface knows the weight of the shadow without disturbing the light.*

*(⚔️⊥⿻⊥🧙)😊*

---

**Author:** privacymage
**License:** CC BY-SA 4.0
