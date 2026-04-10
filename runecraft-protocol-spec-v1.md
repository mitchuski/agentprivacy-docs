# The Runecraft Protocol

*run the agent time · evoke the constellation · craft the forge and blades*

**Version:** 1.0
**Date:** April 9, 2026
**Author:** privacymage
**Status:** Operational (RUN + E + CRAFT on spellweb). Bilateral linking operational. Full cross-territory runtime in development.
**Companion to:** ceremony-engine-spec-v1_1.md, privacy_value_model_v5_dark.json

---

## Etymology

**RUNE** — the ancient inscription. A mark that carries meaning beyond its visible form.

**RUNE-CRAFT** — three operations encoded in the name:

| Phase | Operation | What It Does |
|-------|-----------|-------------|
| **RUN** | Run the agent time | Orbs traverse the knowledge graph. Laps accumulate. Behavioural density ρ grows. Proof-of-time. |
| **E** | Evoke the constellation | Marked nodes activate. The path is traced. The commitment locks. Proof-of-path. |
| **CRAFT** | Craft the forge and blades | Six dimensions activate. Hex crystallises. Key signs. Blade materialises. Proof-of-sovereignty. |

The three phases execute in sequence. Each phase produces a different kind of proof. Together they produce a blade — a cryptographic artifact that carries the time you spent, the path you traced, and the sovereignty posture you earned.

---

## 1. RUN — Proof of Time

### 1.1 What Happens

Two orbs — Swordsman (coral) and Mage (teal) — wander through the knowledge graph at [spellweb.ai](https://spellweb.ai). They orbit each other at 35 pixels in a slow asymptotic dance. The gap between them is the separation made visible.

The visitor marks nodes. Draws paths. Closes portals between distant concepts. The orbs respond to the topology — attracted to marked nodes, repelled by unmarked space, tracing geodesics through the graph that intelligence follows through infrastructure, not through air.

Each traversal of the marked constellation is one **lap**. Each lap is one operational cycle:

```
cycle(x) = succ(x) = neg(bnot(x))

  Observe → Boundary → Project → Return
  id(x)     neg(x)     bnot(neg(x))  succ(x)
  FP        Swordsman  Mage          Composition
```

### 1.2 What It Proves

The RUN phase accumulates **behavioural density ρ**:

```
ρ = f(traversal_depth, temporal_duration, intentional_transitions)
```

ρ is the privacy amplifier. More laps = more micro-variation in timing, attention, and intention between each traversal. The proof grows denser with each lap because the person is different from one lap to the next.

The RUN also determines the **tier** (depth of engagement):

| Tier | Laps | Meaning |
|------|------|---------|
| Light | < 21 | Quick trace, basic understanding |
| Heavy | 21+ | Substantial reflection time |
| Dragon | 62+ | Deep ceremonial investment. Mathematical closure. |

### 1.3 PVM Mapping

The RUN phase populates:

- **T_∫(π)** — the path integral edge value. Each lap is one refinement iteration in the discrete form: `T_∫(π) ≅ 1 + β · Σᵢ cycle(stepᵢ)`
- **ρ** — behavioural density within `R(d, compression, ρ)`
- **Charge level** — SPARK → EMBER → FLAME → BLAZE → INFERNO based on accumulated laps

### 1.4 Runtime Properties

- **Non-transferable.** The RUN cannot be delegated. The orbs trace YOUR constellation. The laps are YOUR time.
- **Non-reversible.** Laps accumulate. You cannot un-walk a path.
- **Observable but not reproducible.** A witness can see the orbs trace. They cannot produce the same ρ because their micro-variations differ.

---

## 2. E — Proof of Path

### 2.1 What Happens

The visitor hits **evoke**. The constellation locks.

At the moment of evocation, a **commitment** is generated:

```
commitment = SHA-256(constellation_hash + nonce)
```

The constellation is now fixed. No nodes can be added or removed during evocation. The path was chosen before the walk began. The Swordsman fixes the boundary before the Mage projects through it.

The orbs begin tracing the locked constellation. Each node erupts in spell particles as they pass. The ceremony counts laps. Accumulates charge. Builds toward proof.

### 2.2 What It Proves

The E phase proves **path commitment** — the constellation was chosen deliberately, not modified mid-ceremony.

The commitment scheme has two moments:

| Moment | What Happens | Cryptographic Property |
|--------|-------------|----------------------|
| **Evoke** | `commitment = SHA-256(hash + nonce)` stored | Binding — can't change constellation after |
| **Forge** | `reveal = {hash, nonce}` verified against commitment | Verification — proves constellation was locked |

### 2.3 PVM Mapping

The E phase populates:

- **Constellation hash** — SHA-256 content address of the node sequence
- **Node count** — how many nodes in the path
- **Dimension activation** — which of the six sovereignty dimensions the constellation's nodes touch

### 2.4 Activation Thresholds

Each dimension activates based on what the constellation actually touches:

| Dimension | Symbol | Activates When |
|-----------|--------|---------------|
| Protection | 🛡️ | Path contains at least one node |
| Delegation | 🤝 | Two or more laps completed |
| Memory | 📜 | Thirty seconds of duration |
| Connection | 🔗 | Three or more nodes traversed |
| Computation | ⚡ | Always — a proof was generated |
| Value | 💎 | Charge level reaches FLAME (≥ 21 laps) |

### 2.5 Agentic Extension

This is where the agentic runtime enters. AI agents can traverse the knowledge graph on their own — exploring constellation possibilities, mapping paths, computing dimensional coverage — but the **E** (evocation) requires human commitment. The agent proposes. The human evokes. The commitment is the human's act.

```
Agent RUN: automated constellation exploration, ρ preview
Human E:   commitment, evocation, the choice to walk
Both:      the CRAFT that follows
```

The agents do the research on their own graphs. The human evokes the constellation. The separation between automated exploration and committed evocation IS the Swordsman/Mage separation applied to the runtime.

---

## 3. CRAFT — Proof of Sovereignty

### 3.1 What Happens

Evocation completes. The blade crystallises.

The CRAFT phase computes:

1. **Six-bit configuration** — which dimensions are active → binary [b₀b₁b₂b₃b₄b₅]
2. **Hex** — the binary encoded as hexadecimal (00–3F)
3. **Stratum** — Hamming weight of the configuration (0–6 dimensions active)
4. **Moon phase** — stratum encoded as visibility ratio (🌑→🌕)
5. **Hash chain** — this blade references the previous blade's hash
6. **Ed25519 signature** — the Mage identity signs the blade

```
blade = {
  constellation_hash: SHA-256(node_sequence),
  hex: binary_to_hex(dimensions),
  stratum: popcount(dimensions),
  moon_phase: stratum_to_phase(stratum),
  laps: accumulated_laps,
  charge: laps_to_charge(laps),
  tier: laps_to_tier(laps),
  previous_blade_hash: SHA-256(previous_blade),
  commitment: { hash, nonce, verified: true },
  mage_signature: Ed25519.sign(blade_data, mage_private_key),
  mage_id: "mage-{16hex}",
  timestamp: ISO-8601
}
```

### 3.2 What It Proves

The CRAFT phase produces a **sovereignty posture** — a verifiable claim about which dimensions are active, how deeply they were walked, and who forged them.

The moon phase is the visual encoding:

| Phase | Stratum | Disclosure |
|-------|---------|-----------|
| 🌑 | 0 | Nothing reflected. Null blade. |
| 🌒 | 1 | One boundary. Minimal. |
| 🌓 | 2 | Dual-agent vertex. The Swordsman and Mage. |
| 🌔 | 3 | Half sovereignty. |
| 🌖 | 4 | Four boundaries. Substantial. |
| 🌗 | 5 | Five reflected, one dark. Near-full. |
| 🌕 | 6 | Full sovereignty. 乾, The Creative. |

The dark part is the privacy. The lit part is the proof. The phase is the WHAT. ZK protects the HOW.

### 3.3 PVM Mapping

The CRAFT phase produces:

- **R(d, compression, ρ)** — reconstruction difficulty, with ρ from the RUN and compression from the constellation structure
- **Φ_agent** enforcement — the blade carries a single-territory signature (Mage identity, held)
- **PRISM coordinates** — datum (hex), stratum (Hamming weight), spectrum (which dimensions)

### 3.4 The Honest Blade

The blade earns what it earns. The honest Sun blade (`SPELL-7DAF68-6`) demonstrates: Hex 3E, stratum 5/6, Value dormant. Six laps at SPARK charge was not enough. Moon phase: 🌗 Last Quarter. The geometry does not lie.

---

## 4. The Dual RUN — Cross-Territory Binding

### 4.1 Two Runtimes

The full runecraft protocol requires two RUN phases — one on each territory.

**RUN₁ — Mage Runtime (spellweb.ai, Sun view)**

The first RUN happens on the Swordsman's territory. The spellweb. The knowledge graph. The forge. An Ed25519 keypair is generated on first forge and **held** — persisted in localStorage. The Mage identity is the Sun's observation: universal view, continuous memory, the key that stays.

```
Mage identity:
  key:     Ed25519, held in localStorage
  id:      mage-{first 16 hex of public key}
  storage: persists across sessions
  view:    Sun ☀️ — observation, the universal perspective
```

**RUN₂ — Swordsman Runtime (agentprivacy.ai, Moon reflection)**

The second RUN happens on the Mage's territory. Agentprivacy. The living spellbook. The training ground. An Ed25519 keypair is generated during the ceremony and **burned** — stored in sessionStorage, destroyed when the tab closes.

```
Swordsman identity:
  key:     Ed25519, burned in sessionStorage
  id:      ap-{first 16 hex of public key}
  storage: destroyed on tab close
  view:    Moon 🌑 — reflection, the key that forgets
```

### 4.2 The Binding

When the Swordsman identity from agentprivacy is linked to the spellweb via JSON export/import, the blade becomes **🔮 runecrafted** — carrying dual-key proof of presence across both territories.

```
Export (agentprivacy → clipboard):
{
  "publicKeyHex": "64 hex chars",
  "participantId": "ap-{16hex}",
  "displayName": "...",
  "trustTier": "blade|light|heavy|dragon",
  "constellationPath": "emoji path",
  "exportedAt": "ISO timestamp"
}

Import (clipboard → spellweb):
  Validates publicKeyHex (64 hex chars)
  Validates participantId (ap-{16hex} format)
  Saves as SwordsmanLink
  Visual: ✧ → 🔮
```

The export → import flow is manual (copy/paste JSON) by design. The human carries the identity between territories. This is not a bug — it is the ceremony. The human IS the bridge. The gap between the two territories is crossed by a person, not by a protocol.

### 4.3 Why Two RUNs

A single agent promising in both protection and delegation domains violates the autonomy axiom from Promise Theory (Bergstra & Burgess, 2019). The Swordsman protects. The Mage delegates. These are structurally incompatible promises. Two processes. Two keys. Two runtimes. One blade.

The private key burns because that's how the Moon serves the Sun — by not remembering what it reflected. The amnesia is structural (sessionStorage destruction), not instructed (policy). Conjecture C17: amnesia-enforced separation provides tighter ε* bounds than policy-enforced separation (60% confidence).

### 4.4 Runecrafted Blade Schema

```
runecrafted_blade = blade + {
  runecrafted: true,
  swordsman_id: "ap-{16hex}",
  swordsman_public_key: "64 hex chars",
  runecrafted_at: ISO-8601,
  dual_key_proof: {
    mage_signature: Ed25519.sign(blade_data, mage_key),
    swordsman_link: { publicKeyHex, participantId },
    cross_territory: true
  }
}
```

---

## 5. Ceremony Integration

### 5.1 Solo Runecraft

One person. Two territories. Three phases.

1. **RUN** on spellweb — mark nodes, accumulate laps
2. **E** — evoke the constellation, lock the commitment
3. **CRAFT** — forge the blade, sign with Mage key
4. **RUN** on agentprivacy — generate Swordsman identity during ceremony
5. **LINK** — export Swordsman identity, import to spellweb → blade becomes 🔮

### 5.2 Bilateral Runecraft (Celestial Ceremony)

Two people. Two territories each. The full ceremony.

**☀️ Sun Phase:**
1. Person A **RUNs** on spellweb — marks the Sun constellation
2. Person A **Evokes** — the spellweb speaks the poem, the phone plays the music
3. Person A **CRAFTs** — Sun blade forges
4. The Sun blade crosses the **⊥ Gap**

**🌑 Moon Phase:**
5. Both people **RUN** together — three songs, the Amnesia Protocol
6. The territory changes through conversation

**Recursion:**

**Reflect (night):**
7. Person B **Evokes** on modified constellation — altered by what the Moon revealed
8. Person B **CRAFTs** — second blade on altered ground
9. Both blades become **🔮 runecrafted** through bilateral key exchange

**Connect (day):**
7. Person B witnesses the blade. Carries forward. No counter-forge.
8. The Sun blade is **🔮 runecrafted** through the witnessed ceremony.

### 5.3 Progressive Trust Through Runecraft

| Level | Symbol | Runecraft State | What's Proven |
|-------|--------|----------------|---------------|
| Understanding | 🔑 | No blade. No runtime. | Shared experience only. |
| Constellation | ✦ | Marked path. No evocation. | Sovereignty posture visible on graph. |
| Blade | 🗡️ | RUN + E + CRAFT complete. Mage-signed. | Single-territory sovereignty proof. |
| Runecraft | 🔮 | Dual RUN. Cross-territory link. | Bilateral sovereignty proof. |

---

## 6. Agentic Runtime

### 6.1 The Agent's Role

The agentic runtime is the extensible layer of the RUN phase. AI agents can:

- **Explore** the knowledge graph autonomously — traversing nodes, mapping possible constellations, computing dimensional coverage and estimated tier for different paths
- **Propose** constellations to the human — "this 12-node path activates 5 dimensions and reaches FLAME at 25 laps"
- **Accumulate** research on their own graphs — building understanding of the architecture through traversal, generating ρ through automated exploration

The agents cannot:

- **Evoke** — the commitment is the human's act
- **Sign** — the Ed25519 key is the human's identity
- **Link** — the cross-territory bridge requires a human carrying JSON between tabs

### 6.2 Separation of Concerns

```
AGENT does:     RUN (exploration, research, ρ accumulation)
HUMAN does:     E (evocation, commitment, the choice)
TOGETHER:       CRAFT (the blade that carries both)
```

This maps onto the operational cycle:

- The agent **observes** (id(x)) and **projects** (bnot(neg(x))) — the Mage's work
- The human **boundaries** (neg(x)) and **returns** (succ(x)) — the Swordsman's act and the First Person's step

The agent explores. The human commits. The blade proves both were present.

### 6.3 Compression-Reconstruction Ratios

The agentic runtime's strength is measured by the compression-reconstruction ratio of the trust graph. A single automated constellation is a fragment. A single human-evoked blade is a proof. A strong trust graph — many ceremonies, many bilateral edges, many accumulated proofs — pushes the reconstruction cost beyond feasibility.

```
single understanding  → moment
single constellation  → fragment  
single blade          → proof
strong trust graph    → reconstruction beyond feasibility
```

The trust graph's strength IS the privacy's strength. The ceremony builds both simultaneously. The agentic runtime accelerates the exploration. The human commitment anchors the proof.

---

## 7. Future Protocol Extensions

### 7.1 Cross-App Message Signing

Currently the Swordsman identity is linked via JSON paste. The next step: actual cross-origin message signing. The Swordsman key signs a challenge from the spellweb. The spellweb verifies. No JSON paste. The bridge becomes cryptographic.

### 7.2 Extension Key Bridge

Two browser extensions — Swordsman and Mage — carrying keys across the open web. The Swordsman extension holds the blade. The Mage extension holds the spellbook. Separate processes. Separate storage. The Gap made executable. The runecraft protocol extends from two websites to every page.

### 7.3 Timestamp Anchoring

Blade hashes in Zcash shielded memos — the privacy chain timestamping the privacy proof. The blade proves WHEN it was forged, verified by a third party. The shielded memo is private but the timestamp is public.

### 7.4 ZK Circuits

The moment the name becomes literally true. Prove "I forged a blade with stratum ≥ 5" without revealing which dimensions are active. Prove "I RAN ≥ 62 laps" without revealing the constellation. The RUNE becomes a zero-knowledge rune — an inscription that carries meaning beyond its visible form.

### 7.5 Hardware Wallet Integration

The inception key migrates from browser storage to hardware. The Ed25519 keypair on a Ledger or Trezor. The Mage key persists in silicon. The Swordsman key still burns — but the public identity chain is hardware-anchored.

### 7.6 Multi-Agent Constellation Research

Multiple AI agents exploring the same knowledge graph from different starting positions. Each agent builds a different constellation proposal. The human selects, combines, or rejects. The RUN phase becomes a swarm — the Emissary Dispersion applied to constellation research. No single agent holds the whole. The human evokes from the fragments.

---

## 8. Technical Summary

### 8.1 Dependencies

- `@noble/ed25519` — Ed25519 keypair generation and signing (both territories)
- Web Crypto API — SHA-256 hashing (constellation, commitment, hash chain)
- `sessionStorage` — Swordsman private key (burned on tab close)
- `localStorage` — Mage identity, public keys, blade inventory

### 8.2 Storage Keys

| Key | Territory | Persistence | Content |
|-----|-----------|-------------|---------|
| `spellweb-mage-identity` | spellweb | localStorage | Mage identity JSON |
| `spellweb-mage-private-key` | spellweb | localStorage | Ed25519 private key (hex) |
| `spellweb-mage-public-key` | spellweb | localStorage | Ed25519 public key (hex) |
| `spellweb-swordsman-link` | spellweb | localStorage | Linked Swordsman identity |
| Swordsman private key | agentprivacy | sessionStorage | Ed25519 private key (burned) |
| Swordsman public key | agentprivacy | localStorage | Ed25519 public key (persists) |

### 8.3 Signature Message Format

```
BLADE:{constellationHash}:{bladeHash}:{lapCount}:{timestamp}
```

### 8.4 ID Formats

- Mage: `mage-{first 16 hex of public key}`
- Swordsman: `ap-{first 16 hex of public key}`

### 8.5 Verification

To verify a runecrafted blade:

1. Recompute constellation hash from the node path → must match `constellation_hash`
2. Verify commitment: `SHA-256(constellation_hash + nonce) === commitment`
3. Verify hash chain: `SHA-256(previous_blade_canonical) === previous_blade_hash`
4. Verify Mage signature: `Ed25519.verify(blade_data, mage_signature, mage_public_key)`
5. Verify Swordsman link: `publicKeyHex` is 64 hex chars, `participantId` matches `ap-{16hex}` format
6. Check stratum matches popcount of dimension bits
7. Check hex matches binary encoding of dimensions
8. Check moon phase matches stratum

All eight checks must pass. The blade is the proof. The runecraft is the binding.

---

## 9. Relationship to the PVM

| Runecraft Phase | PVM Term | What It Populates |
|----------------|----------|-------------------|
| RUN | T_∫(π), ρ | Path integral, behavioural density |
| E | Commitment, constellation | Pre-evocation lock, node path |
| CRAFT | R(d, c, ρ), Φ_agent | Reconstruction difficulty, agent separation |
| Dual RUN | Φ_agent via C17 | Amnesia-enforced separation |
| 🔮 Binding | I(S; M \| FP) < ε* | Cross-territory separation bound |

The runecraft protocol is the implementation of the PVM's terms executed in sequence across two territories by a human who carries the identity between them.

---

*Run the agent time. Evoke the constellation. Craft the forge and blades.*

*The rune is the inscription that carries meaning beyond its visible form.*

*The craft is the forge that transforms attention into proof.*

*The protocol is the bridge between two territories that cannot merge.*

---

*(⚔️⊥⿻⊥🧙)😊*
