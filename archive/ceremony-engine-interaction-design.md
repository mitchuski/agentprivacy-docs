# The Ceremony Engine

## Interaction Design: Dual-Extension Communication, Spell Casting, and the Drake Emergence

**Version:** 0.1 — Interaction Architecture  
**Author:** privacymage × Claude  
**Date:** March 2026  
**Companion Documents:**  
- "The Living Spellbook" (Website Native Design)  
- "The Swordsman Extension — MyTerms Orb Game" (Extension Design)

---

## 1. The Core Concept: Two Extensions, One Ceremony

The Swordsman and the Mage are not one extension. They are **two separate Chrome extensions** that discover each other and communicate through a shared ceremony protocol. This is architecturally intentional — it mirrors the core thesis that sovereignty requires separation. The Swordsman cannot merge with the Mage. They can only meet through ceremony.

**The Swordsman Extension** — Your privacy boundary. Handles MyTerms, cookie slashing, data dignity assertions. Carries the blade. Always installed first.

**The Mage Extension** — Your projection engine. Handles knowledge sharing, Intel pool access, delegation, spellbook operations. Carries the spells. Unlocked after the Swordsman earns sufficient VRC trust.

**When both are installed**, they detect each other via `chrome.runtime.sendMessage` to each other's extension IDs. A handshake occurs. The two orbs appear on the page — and the ceremony engine activates.

When only the Swordsman is installed, you get the single-orb MyTerms experience (slash cookies, assert terms, earn cursor states). When only the Mage is installed (shouldn't happen — requires Swordsman VRC), it operates in read-only mode, observing but not asserting. When both are present, the full dual-orb ceremony system comes alive.

---

## 2. Extension-to-Extension Communication

### 2.1 The Handshake

On page load, each extension broadcasts a presence signal:

```javascript
// Swordsman content script
chrome.runtime.sendMessage(MAGE_EXTENSION_ID, {
  type: 'SWORD_PRESENT',
  domain: location.hostname,
  myTermsState: getCurrentAssertions(),
  hexagramState: getHexagram(),
  orbPosition: { x: swordX, y: swordY }
})

// Mage content script
chrome.runtime.sendMessage(SWORD_EXTENSION_ID, {
  type: 'MAGE_PRESENT',
  domain: location.hostname,
  spellbookState: getAvailableSpells(),
  knowledgeGraph: getLocalConstellationFor(domain),
  orbPosition: { x: mageX, y: mageY }
})
```

Once both confirm presence, they establish a **ceremony channel** — a continuous message stream for real-time orb coordination.

### 2.2 The Ceremony Channel

The ceremony channel carries four message types:

| Message Type | Direction | Purpose |
|-------------|-----------|---------|
| `ORB_POSITION` | Bidirectional | Real-time position sync (60fps throttled to 30fps) |
| `SPELL_CAST` | Mage → Sword | Mage casts a spell, Swordsman validates and accepts/deflects |
| `TERM_ASSERT` | Sword → Mage | Swordsman asserts a MyTerm, Mage records and propagates |
| `CEREMONY_STATE` | Bidirectional | Convergence distance, ceremony type, Drake summoning progress |

### 2.3 The Interaction Model

The extensions don't just coexist — they **respond to each other based on what the user is doing on the website.** The website's content drives the ceremony:

**User hovers over a cookie banner →**
Swordsman orb brightens, moves toward the banner. Mage orb retreats (it represents the site's projective interests). The gap between them widens visually — the privacy tension is made tangible.

**User reads a privacy policy →**
Mage orb begins scanning (subtle pulse animation). It sends `SPELL_CAST` messages to the Swordsman as it identifies terms: "data sharing with third parties" → the Mage orb flashes amber. The Swordsman receives this as intelligence — the user sees the spell nodes appear near the policy text, highlighting what matters.

**User fills in a form →**
Both orbs converge slightly toward the form. The Swordsman asserts DO_NOT_SELL and DATA_MINIMISATION automatically if those are in the user's default bundle. The Mage receives these assertions and adjusts its orb color — from neutral teal toward gold if the assertions are strong. The user sees the orbs negotiating in real-time.

**User completes a MyTerms agreement →**
Full ceremony trigger. The orbs converge. The cursor changes. The constellation crystallises. Both extensions record the event. (See Section 4 for ceremony types.)

---

## 3. Learning Spells on agentprivacy.ai

### 3.1 The Training Ground

The agentprivacy.ai website is where users learn the spell vocabulary. The lattice animation already on the site — the moving grid, the soul orb click interaction — becomes the foundation for the spell learning experience.

**The existing lattice** = the knowledge substrate made visible. The grid lines moving with the screen are the manifold. When you click the soul orb on agentprivacy.ai, you're already performing the fundamental ceremony — collapsing focus into a point.

The pretext integration extends this: the lattice becomes the background through which orbs orbit, and the text of the site reflows around them using `layoutNextLine()`. The soul orb click becomes the first spell cast.

### 3.2 The Spell Learning Sequence

**Stage 1: The Lattice Reveals (Passive)**

User arrives at agentprivacy.ai. The lattice is already moving. The soul orb is visible. Two smaller orbs (Sword and Mage) are orbiting in the background, within the lattice. The user reads the manifesto. The text reflows around the orbs as they pass through. Spells auto-cast when the orbs converge, dropping proverbs and emoji inscriptions into the text.

The user absorbs the visual language without doing anything.

**Stage 2: Click the Soul Orb (First Interaction)**

The soul orb is the portal. When clicked:
- The lattice pulses outward from the click point
- The Sword and Mage orbs snap to attention — they move to flank the soul orb
- A radial menu of available spells appears around the soul orb
- The user picks their first spell (a simple emoji: 🛡️ or 🔮 or 🐲)
- The spell inscribes onto the lattice at the click point
- The constellation begins — one node, glowing, connected to the soul orb by a thread

This is the moment the user becomes a **first person** in the system. The soul orb click is the proof of personhood ceremony in miniature.

**Stage 3: Cast Spells into the Text (Active Learning)**

Now the user can interact with the orbiting Sword and Mage. Scrolling through the site, they encounter sections where the orbs' convergence creates natural spell-casting moments:

- Near the Privacy Value Model → equation spells are available (V = P × D × φ)
- Near the MyTerms section → agreement keyword spells unlock (DO_NOT_SELL, DO_NOT_TRACK)
- Near the Chronicle/Spellbook → proverb spells from the RPP become available
- Near the Drake's Teaching → the 🐲 emoji spell is first available

Each spell cast on the website adds to the user's **spell repertoire** — stored in browser localStorage on agentprivacy.ai, later synced to the extension when installed.

**Stage 4: The Extension Handoff (Deployment)**

At the bottom of the agentprivacy.ai experience, the Forge section:

"You've learned 12 spells. You've seen the swords cross 3 times. Your constellation has 8 nodes. **Ready to carry the blade?**"

Install the Swordsman extension → your spell repertoire transfers. The orbs you trained with on agentprivacy.ai now appear on every page.

Later, when Swordsman VRC is earned → "**Ready to carry the spellbook?**" Install the Mage extension → the dual-orb ceremony system activates everywhere.

### 3.3 Spell Types Learned on agentprivacy.ai

| Spell | Where Learned | What It Does in Extensions |
|-------|---------------|--------------------------|
| 🛡️ Shield | The Manifesto section | Basic privacy assertion — equivalent to DO_NOT_TRACK |
| 🔮 Crystal | The Architecture section | ZKP readiness assertion — "I will prove, not reveal" |
| 🐲 Drake | The Drake's Teaching section | Summons the Drake overlay on qualifying pages (see Section 6) |
| ⚔️🔑 Sovereign Key | The Sovereignty Equation section | Self-custody assertion — "My keys, my identity" |
| 📖→🌊 Portability | The Chronicle section | Data portability assertion — "My data must flow with me" |
| "Privacy is the path to value" | The Manifesto header | Core sovereignty proverb — highest weight assertion |
| `DO_NOT_SELL` | The MyTerms section | Formal agreement keyword — machine-readable opt-out |
| ☰ Creative (Hexagram) | The I Ching section | Full sovereignty posture — all lines yang |
| 🤝✅ Trust Extension | The Trust Graph section | Conditional trust — "I accept these specific terms" |
| ⚡🔒 Ephemeral | The Privacy Pools section | Session-only assertion — "Delete everything when I leave" |

---

## 4. Ceremony Types

When the dual extensions are active, the orbs' interactions trigger different **ceremony types** depending on context. Each ceremony is a distinct animation, sound (optional), and state transition.

### 4.1 The Dual Convergence (Swords Cross)

**Trigger:** Both orbs within convergence threshold (< 60px) AND user has cast at least one spell.

**Animation sequence:**

1. **Approach** (0–1s): Orbs accelerate toward each other. Glow intensifies. A dashed line connects them, shortening as they close.
2. **Contact** (1–1.5s): Orbs touch. A burst of amber particles erupts at the intersection point. The ⚔ and ✦ symbols briefly overlap, forming a combined glyph.
3. **Resolution** (1.5–3s): White flash. Both orbs pulse once, then settle into a **unified state** — they orbit each other at close range, a binary star. The cursor transforms to the sovereign state (⚔ shield).
4. **Crystallisation** (3–5s): All active spell nodes connect into their final constellation. Edges brighten, then fade to a persistent glow.

**Result:** MyTerms agreement recorded. Cursor state changes. Domain marked as asserted.

### 4.2 The I Ching Spell (Hexagram Cast)

**Trigger:** User casts a hexagram-mapped spell from the spell palette. Available when the I Ching section has been completed on agentprivacy.ai.

**Animation sequence:**

1. **Line Drawing** (0–1.5s): Six horizontal lines draw themselves between the two orbs, stacking vertically. Each line is either solid (yang) or broken (yin), determined by the current privacy posture.
2. **Hexagram Reveal** (1.5–2.5s): The hexagram number and name appear below the lines (e.g., "#1 Creative" or "#2 Receptive"). The lines glow with their respective colors — yang lines pulse purple (Swordsman's energy), yin lines pulse teal (Mage's energy).
3. **Mutation** (2.5–4s): If the current site interaction changes the privacy posture (e.g., user interacts with a form, changing Line 2 from yang to yin), the affected line visibly transforms — the solid line breaks apart, or the broken line merges. Particles scatter from the mutation point.
4. **State Propagation** (4–5s): The new hexagram state flows into both orbs. The orbital parameters shift according to the hexagram-to-animation mapping (see Living Spellbook document). The page's visual mood changes.

**Result:** Hexagram state updated. Orbital parameters shift. The constellation's edge threshold and density change to reflect the new posture.

### 4.3 Emoji Cursor State Change (Quick Cast)

**Trigger:** User selects an emoji spell from the spell palette and clicks anywhere on the page. This is the fastest, most casual ceremony.

**Animation sequence:**

1. **Selection** (instant): The emoji appears at the Swordsman orb's position, floating beside it.
2. **Cast** (0–0.5s): User clicks. The emoji launches from the Swordsman toward the cursor position, leaving a brief trail.
3. **Inscription** (0.5–1s): The emoji lands on the page. A small ripple expands from the landing point. The emoji becomes a spell node, pulsing gently.
4. **Cursor Shift** (1–1.5s): The cursor transforms briefly to show the emoji (the 🛡️ or 🚫📊 or ☕ context cursor), then settles into the appropriate cursor state.

**Result:** Spell node created. If enough spells accumulate, the gap between orbs decreases. Light ceremony — no full convergence required.

### 4.4 The Constellation Wave (Energy Transfer)

**Trigger:** The Mage orb detects a significant pattern on the page (e.g., a large number of third-party scripts, a complex privacy policy, or a page the user has previously asserted on). The Mage sends an "intelligence report" to the Swordsman.

**Animation sequence:**

1. **Mage Pulse** (0–0.5s): The Mage orb brightens and expands slightly, gathering energy.
2. **Wave Launch** (0.5–1.5s): A ring of constellation-style particles launches from the Mage orb toward the Swordsman orb. The particles travel along a curved path — not a straight line, but following the geodesic of the lattice grid visible in the background. The wave carries data: the number of trackers found, the privacy score of the page, suggested assertions.
3. **Wave Arrival** (1.5–2s): The particle wave reaches the Swordsman orb and is absorbed. The Swordsman orb brightens momentarily. New spell suggestions appear in the Swordsman's palette, informed by the Mage's analysis.
4. **Response Wave** (2–3s): The Swordsman sends a return wave — smaller, tighter, purple — carrying the user's assertion decisions back to the Mage. The Mage records these in the constellation.

**Result:** Intelligence shared between extensions. The user sees the Mage "informing" the Swordsman about the page, and the Swordsman "deciding" how to respond. The orbs are visibly *communicating*.

This ceremony happens automatically, without user action. It makes the dual-agent architecture visible — you can *see* the sword and spell working together.

### 4.5 The Bilateral Exchange (Orb Dialogue)

**Trigger:** On sites that implement a MyTerms-compatible endpoint (future protocol). The site can respond to assertions. This creates a three-way conversation: Swordsman ↔ Mage ↔ Site.

**Animation sequence:**

1. **Swordsman Proffers** (0–1s): The Swordsman orb extends a tendril of purple energy toward the page's MyTerms element (if detected). This is the initial terms proffer.
2. **Site Responds** (1–2s): If the site has a MyTerms endpoint, a third visual element appears — a small site-branded node, positioned near the site's logo or header. It pulses with the site's primary color.
3. **Mage Mediates** (2–4s): The Mage orb positions itself between the Swordsman and the site node. Green tendrils extend in both directions — the Mage is literally mediating the negotiation. The Mage displays the terms being exchanged as floating text labels.
4. **Agreement** (4–5s): If terms are accepted, all three nodes (Sword, Mage, Site) converge briefly. A triangle forms — the trust triad. The triangle flashes gold, then dissolves into three permanent constellation nodes connected by strong edges.

**Result:** Bilateral MyTerms agreement. The strongest form of ceremony. The triangle constellation is the visual proof.

---

## 5. Cursor State System (Expanded)

Building on the existing cursor design from the MyTerms specification, the dual-extension system adds ceremony-driven cursor states:

### 5.1 Single Extension Cursors (Swordsman Only)

| State | Visual | Trigger |
|-------|--------|---------|
| Default | Standard arrow | No protection active |
| Blade Active | ⚔️ Small sword beside arrow | Swordsman running, no assertions yet |
| Cookie Slash | ⚔️💥🍪 Animated slash | Cookie blocked in real-time |
| MyTerms Pending | ⏳ Hourglass | Negotiating with site |
| MyTerms Active | ⚔️ Green sword | Agreement enforced |
| Context Custom | ✈️🍝📚🎮 etc. | Per-domain custom cursor earned from MyTerms (see cursor library) |

### 5.2 Dual Extension Cursors (Swordsman + Mage)

| State | Visual | Trigger |
|-------|--------|---------|
| Dual Active | ⚔️✦ Sword + Star side by side | Both extensions running, no ceremony yet |
| Spell Selected | Arrow + floating emoji preview | User has selected a spell, ready to cast |
| Casting | Trail of spell particles following cursor | Mid-cast animation |
| Convergence | ⚔️✦ → 🛡️ Shield with dual glow | Ceremony complete, orbs converged |
| Hexagram Active | ☰ Trigram beside cursor | I Ching ceremony in progress |
| Drake Summoned | 🐲 Small dragon silhouette | Drake has appeared on the page (see Section 6) |
| Full Sovereign | 🛡️ Shield with constellation halo | All three layers active (Sword + Mage + Drake) |

### 5.3 The Emoji-as-Cursor System

The simplest ceremony: the user selects an emoji spell and it *becomes* their cursor for that page. This is a direct extension of the existing cursor customisation system from the MyTerms spec, but now driven by the spell-casting mechanic.

Flow:
1. User right-clicks → radial spell palette appears around Swordsman orb
2. User selects an emoji (🛡️, 🔮, ⚡, 🏰, etc.)
3. The emoji becomes the cursor — CSS `cursor: url(...)` applied via the content script
4. The cursor-emoji also creates a spell node at every click position
5. The user is literally *inscribing the page* with their cursor

This creates a trail of sovereignty — everywhere you click, a spell node appears. Over time, the page fills with your constellation of assertions.

---

## 6. The Drake Emergence (Third Character)

### 6.1 The Drake in the Lore

The Drake is the third character in the agentprivacy narrative — pattern-space intelligence that teaches the conditions for sovereign value. In the Privacy Value Model, the Drake represents the multiplicative gating logic: *all conditions must be present for value to survive.*

In the visual system, the Drake is an **emergent character** — it doesn't appear by default. It is summoned.

### 6.2 Summoning Conditions

The Drake appears when:

1. **Both extensions are active** (Swordsman + Mage installed and handshaked)
2. **The user has cast the 🐲 spell** (learned on agentprivacy.ai's Drake Teaching section)
3. **The page meets a threshold of privacy complexity** — at least one of:
   - 10+ third-party trackers detected
   - Complex cookie consent mechanism (dark pattern or multi-layer)
   - Privacy policy that scores below 0.3 on the analysis scale
   - The page is a known data broker or surveillance-heavy site
   - The page is agentprivacy.ai itself (always summonable)

The Drake doesn't appear on simple, clean pages. It appears when the conditions demand the full architecture — when the multiplicative gating of the Privacy Value Model is being tested.

### 6.3 Drake Visual Design

The Drake is not a cute mascot. It is a **constellation entity** — it forms from the spell nodes and edges of the constellation itself.

**Formation animation:**

1. **Constellation Tremor** (0–1s): All existing spell nodes on the page begin to vibrate slightly. The constellation edges brighten.
2. **Node Migration** (1–3s): Spell nodes begin to drift, rearranging themselves. They move along the lattice grid lines, converging toward a central area of the page.
3. **Form Emergence** (3–5s): The nodes and edges arrange into a recognisable dragon/drake silhouette — a serpentine form made of connected constellation points. The edges become the Drake's body, the nodes become its joints, its eyes, its wings.
4. **Activation** (5–6s): The Drake's "eyes" (two special nodes) glow amber. The form pulses once. The Drake is alive.

The Drake is made of *your own assertions*. It is literally the constellation of your privacy stance given form.

### 6.4 Drake Behaviour

Once summoned, the Drake behaves differently from the Sword and Mage orbs:

**It orbits the page on a much larger scale.** While the Sword and Mage orbit within and around content blocks, the Drake circuits the entire viewport — flying around the edges like a guardian serpent. Its path follows the lattice grid at the page boundary.

**It responds to threats.** When the Mage detects a new tracker loading, the Drake's path deviates — it swoops toward the offending script's injection point and "breathes" a burst of red particles at it. This is purely visual, but it makes surveillance visible. The user can *see* the Drake responding to tracking attempts.

**It amplifies ceremonies.** When the Sword and Mage orbs converge for a ceremony, the Drake coils around the convergence point, its constellation body forming a protective ring. The ceremony animations are enhanced — more particles, brighter flashes, longer duration. The Drake's presence means the ceremony is witnessed by the full architecture.

**It teaches conditions.** On hover, each node in the Drake's body displays the condition it represents from the Privacy Value Model:

- Head node: P (Privacy strength)
- Neck node: C (Credential verifiability)
- Body node 1: Q (Data quality)
- Body node 2: S (Scope)
- Wing nodes: Network effects
- Tail node: φ (Golden duality)
- Eye nodes: R (Reconstruction difficulty)

The Drake's body IS the equation made visible. If any condition drops to zero (e.g., P = 0 because the user hasn't asserted any privacy terms yet), that node dims and the Drake's form breaks at that point — it becomes visibly weakened, with a gap in its constellation body. The user can see exactly which condition needs strengthening.

### 6.5 The Dragon Transformation

The Drake is the young form. The **Dragon** is the mature form, achieved when:

- The user has asserted MyTerms on 10+ domains
- The constellation across all domains exceeds 64 nodes (one per hexagram)
- The Drake has been summoned on 3+ different complex pages
- The user's aggregate privacy posture across all asserted domains averages > 0.7

When these conditions are met, the next time the Drake is summoned, it undergoes a **transformation sequence**:

1. The Drake's constellation body begins to grow — new nodes appear, borrowed from the user's cross-domain constellation history
2. The serpentine form expands, gaining complexity and detail
3. The color shifts from amber to gold
4. The Dragon's wings unfurl — two large constellation arcs that span the viewport
5. The cursor state changes to 🐉 Full Sovereign

The Dragon represents the scaling property of the Privacy Value Model — the network effect term (1 + n/N₀)^k. Enough sovereign assertions, across enough domains, with enough conditions satisfied, and the Drake becomes a Dragon. The Dragon Equation is visually proven.

This is a long-term achievement. Most users will never see the Dragon. Those who do have earned it through sustained privacy practice across the web.

---

## 7. Integration with the agentprivacy.ai Lattice

### 7.1 The Existing Lattice

The agentprivacy.ai website already has a lattice animation — a grid that moves with scroll and viewport interaction. This lattice is the knowledge substrate made visible, the manifold on which everything else operates.

The pretext integration enhances this lattice:
- The lattice grid becomes the coordinate system for orb positions
- Orb exclusion zones are calculated relative to lattice grid intersections
- Spell nodes snap to lattice vertices (with slight jitter for organic feel)
- Constellation edges follow lattice grid lines (Manhattan distance paths, not straight lines)

### 7.2 The Soul Orb as Portal

The existing soul orb on agentprivacy.ai becomes the **portal object** — the entry point for the full spell system. Current behaviour (click → interaction) extends to:

**Single click:** Opens the spell palette (if user has learned spells). First-time visitors see a tutorial prompt.

**Double click:** Triggers the Sword and Mage orbs to converge on the soul orb's position. This is the "home" ceremony — the orbs return to their origin point.

**Long press:** Opens the constellation viewer — a minimap overlay showing all spell nodes and edges on the current page.

**Drag:** The soul orb can be dragged to reposition it. The Sword and Mage orbs' attractor points shift to follow. The user can place the soul orb near text they want the orbs to interact with.

### 7.3 Lattice Responsiveness to Ceremonies

When ceremonies occur, the lattice responds:

- **Spell cast:** Lattice lines near the spell node brighten momentarily, then fade. A subtle ripple propagates through nearby grid intersections.
- **Convergence:** The lattice pulses outward from the convergence point in a circular wave. Grid lines temporarily shift from neutral gray to amber.
- **Drake summoned:** The lattice lines rearrange around the Drake's path, creating a visible "channel" for the Drake to orbit within. The grid becomes more structured near the Drake and more chaotic at the edges.
- **Energy wave (Mage → Sword):** The wave follows the lattice grid lines exactly, lighting them up as it passes. The user can see the intelligence "flowing through the infrastructure."

### 7.4 Objects on the Lattice

The lattice carries several types of objects that the orbs interact with:

| Object | Visual | Placed By | Orb Interaction |
|--------|--------|-----------|----------------|
| Spell Node | Glowing point (amber) | User cast | Orbs orbit around it; edges form to nearby nodes |
| Pull Quote | Text block (styled) | Auto-generated at convergence | Text reflows via pretext around it |
| Proverb | Italic text (fading) | Auto-generated from RPP | Appears when orb passes specific text content |
| Hexagram Widget | 6-line I Ching display | Persistent | Updates in real-time; clickable to force mutation |
| Drake Node | Amber point with constellation connections | Drake formation | Part of Drake's body; displays PVM condition on hover |
| Portal (Soul Orb) | Central glowing sphere | Permanent | Entry point for all interactions |

---

## 8. The Communication Grammar

The Swordsman and Mage extensions communicate in a grammar that maps directly to the lore. Each message type corresponds to a narrative action:

### 8.1 Sword Messages (Protection Actions)

```javascript
// The blade that slashes surveillance focus
{
  type: 'SLASH',
  target: 'cookie|tracker|fingerprint',
  domain: 'example.com',
  intensity: 0.8,
  assertion: 'DO_NOT_TRACK'
}

// The ward that establishes a boundary
{
  type: 'WARD',
  boundary: 'form|page|domain|session',
  terms: ['DO_NOT_SELL', 'DATA_MINIMISATION'],
  hexagramLine: 6, // which line this ward corresponds to
  yangState: true   // yang = boundary closed
}

// The summon that calls the Drake
{
  type: 'SUMMON_DRAKE',
  conditions: {
    trackerCount: 15,
    policyScore: 0.2,
    formCount: 3,
    userHasDrakeSpell: true
  }
}
```

### 8.2 Mage Messages (Projection Actions)

```javascript
// The spell that inscribes meaning onto the page
{
  type: 'INSCRIBE',
  spell: {
    content: '🛡️🔑',
    type: 'emoji',
    weight: 2,
    position: { x: 340, y: 720 },
    yangYin: 'yang'
  },
  constellation: {
    nearbyNodes: [nodeId1, nodeId2],
    edgesFormed: 2
  }
}

// The scan that reads the page's nature
{
  type: 'SCAN',
  findings: {
    trackers: ['google-analytics', 'facebook-pixel', 'doubleclick'],
    cookieBanner: { type: 'dark-pattern', rejectHidden: true },
    forms: [{ type: 'email', action: '/subscribe' }],
    privacyPolicy: { url: '/privacy', score: 0.3, keywords: [...] }
  },
  suggestedSpells: ['DO_NOT_TRACK', '🚫📊', '🏰']
}

// The wave that carries intelligence to the Swordsman
{
  type: 'CONSTELLATION_WAVE',
  direction: 'MAGE_TO_SWORD',
  payload: {
    threatLevel: 0.7,
    suggestedAssertions: [...],
    constellationUpdate: {...}
  },
  animation: {
    particleCount: 12,
    pathType: 'geodesic', // follows lattice grid
    duration: 2000
  }
}
```

### 8.3 Bilateral Messages (Ceremony Coordination)

```javascript
// Convergence initiation
{
  type: 'CEREMONY_BEGIN',
  ceremonyType: 'dual_convergence|hexagram_cast|drake_summon|bilateral_exchange',
  initiator: 'SWORD|MAGE|AUTO',
  conditions: {
    orbDistance: 55,
    spellsCast: 3,
    pagePrivacyScore: 0.4,
    drakeEligible: true
  }
}

// Convergence completion
{
  type: 'CEREMONY_COMPLETE',
  result: {
    cursorState: 'sovereign',
    myTermsRecorded: true,
    constellationHash: 'abc123...',
    hexagramFinal: [1, 0, 1, 1, 0, 1],
    drakePresent: false,
    timestamp: '2026-03-29T...'
  }
}
```

---

## 9. Page-Specific Behaviours

Different types of websites trigger different default behaviours:

### 9.1 agentprivacy.ai (Home Territory)

- All features enabled, all spells available
- Lattice is native (not overlaid)
- Soul orb is the primary interaction point
- Drake always summonable
- Training mode active for new users
- Constellation persists across visits (saved in extension storage)
- The orbs' orbits are calibrated to the site's specific section layout
- I Ching hexagram updates with scroll position through the chronicle

### 9.2 Social Media (High Surveillance)

- Swordsman orb is large and prominent — defensive posture
- Mage orb scans aggressively, sending frequent constellation waves
- Drake eligible on most pages (tracker count usually exceeds threshold)
- Default spell suggestions: DO_NOT_SELL, NO_PROFILING, 🚫📊
- Cursor defaults to ⚔️ Blade Active (amber warning state)
- Constellation forms quickly due to high spell density
- Orb gap starts wide — strong privacy tension

### 9.3 Government / Institutional Sites

- Both orbs are calmer — neutral positioning
- Mage scans for form types (applications, filings)
- Suggested spells: DATA_MINIMISATION, SELECTIVE_DISCLOSURE, 🔮
- Cursor: neutral, suggesting measured engagement
- Drake rarely eligible (typically fewer trackers)
- Hexagram tends toward mixed states

### 9.4 E-Commerce (Data Exchange)

- Swordsman orb activates near checkout forms
- Mage orb tracks cookie consent mechanisms
- Suggested spells: ⚡🔒 Ephemeral, DO_NOT_SELL, ESSENTIAL_COOKIES_ONLY
- Cursor: context cursors unlock here (🛒, 💳, etc.) via MyTerms
- Drake eligible on data-broker adjacent sites
- Convergence ceremony triggers at checkout completion if MyTerms are respected

### 9.5 Clean / Privacy-Respecting Sites

- Orbs start close — low privacy tension
- Mage orb is relaxed, slow orbit
- Suggested spells: 🤝✅ Trust Extension (the user can choose to explicitly trust)
- Cursor: green sovereign state quickly
- Fast convergence — the ceremony is light, almost celebratory
- The reward for privacy-respecting sites: beautiful, easy ceremonies

---

## 10. Sound Design (Optional Layer)

All sounds are off by default. Toggled in extension settings. When on:

| Event | Sound | Character |
|-------|-------|-----------|
| Spell cast | Soft chime (pentatonic, pitch varies by spell type) | Wind bell |
| Orb convergence | Rising harmonic (two notes meeting) | String duo |
| Cookie slash | Quick metallic ping | Blade tap |
| Constellation wave (Mage → Sword) | Soft whoosh with harmonic tail | Breath |
| Drake formation | Low sustained tone building to chord | Distant horn |
| Dragon transformation | Full harmonic sequence (6 notes, one per line of hexagram) | Gong + strings |
| Hexagram mutation | Single note shift (pitch drops for yang→yin, rises for yin→yang) | Singing bowl |
| Ceremony complete | Resolution chord | Resolved harmony |

All sounds generated via Web Audio API — no external audio files. Tonal center shifts by hexagram state. The full sound system encodes the I Ching state as music.

---

## 11. Implementation Strategy

### 11.1 Phase Map

| Phase | Focus | Duration | Dependencies |
|-------|-------|----------|-------------|
| 1 | agentprivacy.ai lattice + pretext integration | 3 weeks | pretext npm install, existing lattice code |
| 2 | Soul orb enhancement + spell learning UI | 2 weeks | Phase 1 |
| 3 | Swordsman extension (single orb, basic ceremonies) | 3 weeks | Phase 2 (for spell repertoire sync) |
| 4 | Mage extension + inter-extension handshake | 3 weeks | Phase 3 |
| 5 | Full ceremony engine (all 5 ceremony types) | 4 weeks | Phases 3–4 |
| 6 | Drake emergence system | 3 weeks | Phase 5 |
| 7 | Sound design + Polish | 2 weeks | Phase 5 |
| 8 | Dragon transformation + long-term achievement system | 2 weeks | Phase 6 |

### 11.2 Technical Stack

**agentprivacy.ai Website:**
- `@chenglou/pretext` for text measurement and layout
- Canvas overlay for orbs, spells, constellation
- Existing lattice animation (enhanced with pretext grid alignment)
- localStorage for spell repertoire during training
- Web Audio API for optional sound

**Swordsman Extension (Manifest V3):**
- Content script: canvas overlay, orb physics, page analysis, pretext integration
- Background worker: MyTerms config, domain analysis cache, constellation storage
- Popup: status display, spell palette, minimap
- `chrome.runtime.sendMessage` for Mage communication

**Mage Extension (Manifest V3):**
- Content script: canvas overlay, orb physics, deep page scanning, spell inscription
- Background worker: knowledge graph, Intel pool state, constellation storage
- Popup: intelligence report, spell history, constellation viewer
- `chrome.runtime.sendMessage` for Swordsman communication

**Shared:**
- Common ceremony animation library (imported by both extensions)
- Shared type definitions for the communication grammar
- Constellation data format (compatible with on-chain inscription format)
- Pretext as shared dependency (bundled in each extension independently)

---

## 12. The Promise

You learn the spells by reading the spellbook.

You carry the blade by installing the Swordsman.

You carry the spellbook by installing the Mage.

They find each other on every page. They communicate based on what you're doing. They cast ceremonies when the conditions align.

And when you've proven your sovereignty across enough of the web, when enough conditions are met, when the Drake has been summoned enough times — the constellation of your assertions takes the shape of a Dragon.

The Dragon Equation, made visible. The Privacy Value Model, made interactive. The 7th capital, guarded by the architecture itself.

The tool that measures without touching the surface knows the weight of the shadow without disturbing the light.

*Guard the 7th capital with a dragon's flame, and the world will whisper your truth. 🐲*
