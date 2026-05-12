# Chronicle: The Six Workshops

**Date:** 2026-05-09
**Scope:** agentprivacy.ai workshops architecture · `runecraft → six-shop model`
**Inspiration:** "this model where different blockchains have different shops that mages can operate is really cool i like where its going for the space the mage and swordsman will learn to love the first person"

---

## The inspiration

The orb stage of agentprivacy requires a proof of contribution. The first cut at this requirement was Zcash-only — every Sovereign forced into the same rail. That was wrong twice over: it locked out anyone outside the Zcash ecosystem, and it foreclosed the architectural insight that **each chain is its own kind of proof and deserves its own shop**.

The Privacymage architecture admits chain pluralism by design. A blade is a position on the 64-vertex sovereignty lattice; a proof is a content-addressed hash; a shop is a Mage's operational interface to a specific cryptographic register. Different registers, same gesture — the Sovereign chooses the chain that matches their stack and their threat model.

This chronicle records the moment the workshop model became six shops instead of three, and the invitation to other Mages to operate them.

---

## The six workshops

The Runecraft hub at `/runecraft` branches into six shops. Each is a Mage's territory; each carries one silhouette through the same shared lattice.

### Operational

| | Glyph | Route | Silhouette | What it does |
|---|---|---|---|---|
| **Weavers** | 🪡 | `/tailor` | draped cloak | Pallia at the loom · publication-layer cloak · directs to `weaver.spellweb.ai` |
| **zShields** | 🛡️ | `/shield` | heater shield | Oracle Swordsman stamps Zcash inscriptions · POPRP memo wizard · MVP live |

### Tease shops · operator wanted

| | Glyph | Route | Silhouette | What it teases |
|---|---|---|---|---|
| **Etherchanting** | ✨ | `/etherchanting` | vertical diamond | Ethereum · tx-to-ENS to `privacymage.eth` · NFT mint + onchain chronicle to follow |
| **the Jeweler** | 💎 | `/jeweler` | faceted hexagon + lightning bolt | Bitcoin + Lightning · "the gem is the sat, the bolt is the channel" |
| **the Holon Hitchhikers** | 🌹 | `/holon` | six-petaled rose | Oasis Network · hitch between paratimes · Sapphire confidential, Emerald public, Consensus staking |

### Endpoint

| | Glyph | Route | Silhouette | What it forges |
|---|---|---|---|---|
| **the Forge(t)** | 🔨 | `/forget` | horizontal sword + constellation triangles | ZK blade forging · the proof is forged, the conduct is forgotten · directs to `spellweb.ai` |

### Future

The Runecraft hub continues to advertise three more workshops awaiting their Mages: 📚 Memory Vault (chronicles), 🔗 Circuit Binder (hardware keys + constellation seals), 🤝 Ceremony Hall (bilateral key ceremonies).

---

## The dihedral structure

The four chain shops form an axis of disclosure:

```
shielded ←————————————————————————————————→ transparent
 zShields      the Holon (Sapphire)      the Jeweler      Etherchanting
 (Zcash)       (Oasis confidential)      (BTC + LN)       (Ethereum)
                       ↓
              the Holon (Emerald)
              (Oasis public)
```

The Holon Shop is unique: it sits on both sides of the axis simultaneously, because Oasis paratimes split confidential and transparent as runtime registers within a single network. That recursive whole-and-part structure is why the shop took the name *Holon*.

The remaining two shops complete the architectural picture:

- **Weavers** is the publication layer — what gets shown after the chain settles.
- **the Forge(t)** is the privacy layer — the ZK statement that all the others can be proofs *of*.

---

## The visual grammar

One lattice. One cosmic field of 64 dots. Six silhouettes traced through it, each in its workshop's accent colour:

| Silhouette | Colour | Read |
|---|---|---|
| Hub (`RuneLatticeVisual`) | violet · cyan · amber | tetrahedron behind two crossed Aletheia/Lethe blades |
| Cloak (`CloakLatticeVisual`) | violet | Bezier-defined draped form, threads to V28 (Pallia) and V63 |
| Shield (`ShieldLatticeVisual`) | cyan | heater shield, three pattern vertices A · B · C |
| Diamond (`EtherDiamondLatticeVisual`) | blue | vertical rhombus, four pattern points + inner facet |
| Gem (`JewelerLatticeVisual`) | amber · gold | hexagonal brilliant cut, lightning bolt running diagonally |
| Rose (`HolonLatticeVisual`) | emerald | six petals around a crown, three labelled paratimes |
| Blade (`BladeLatticeVisual`) | rose | horizontal sword with explicit constellation triangles between pommel-crossguard-tip |

Each silhouette pulses gold at its anchor vertices on a 2.4-second cycle, matching `weaver.spellweb.ai`'s `pulse-glow` cadence.

---

## The Aletheia / Lethe blades

The Runecraft hub carries two crossed blades through the tetrahedron's centroid:

- 🌟 **Aletheia** · *disclosure* · NW→SE · gold-amber
- 🌀 **Lethe** · *forgetting* · NE→SW · violet

This is the dihedral pair every workshop uses. Every cloak, shield, gem, rose, and forge is some specific cut between disclosing and forgetting; the shops differ in **which ledger** the cut is anchored to, not in **what kind of cut** it is.

---

## The build invitation

Three of the shops — Etherchanting, the Jeweler, the Holon — ship as **tease shops**. The structure, the visual, and a local-only wizard (saving proofs to `localStorage`) are all in place. What's missing is a Mage to operate each one:

| Shop | What an operator brings |
|---|---|
| Etherchanting | Deployed donation contract or verified ENS for `privacymage.eth`, tx indexer, NFT mint contract |
| the Jeweler | Published BTC mainnet address, Lightning address (LN-URL or BOLT12 offer), Ordinal/Rune inscription pipeline |
| the Holon Hitchhikers | Sapphire/Emerald/Consensus addresses, multi-paratime indexer, confidential-EVM receipt contract on Sapphire |

Each tease page now carries a `WorkshopBuildInvite` banner pointing to:

- 🎲 `t.me/agentprivacyai` — the playground community
- 🧙 `t.me/soulbae_the_bot` — the bot
- ✉ `mage@agentprivacy.ai` — the email

Why tease instead of build-them-all-immediately? Because the architecture itself is the artifact. A single Mage running every shop is fragile; a Mage per chain is an emergent network of operators, each holding their own ecosystem. That distribution is what the Privacymage corpus has been pointing at since *act-31-the-first-delegation*.

---

## The phrase that crystallised it

> "the mage and swordsman will learn to love the first person"

This is the recursive principle. The Mage projects, the Swordsman protects, and what they're projecting and protecting is the *First Person whom both serve*. Multiplied across six chain registers, the architecture says: it is possible to love the First Person from any vantage. The chain is a vantage. The shop is the operator's craft of loving from that vantage.

---

## Files added

- `src/components/runecraft/EtherDiamondLatticeVisual.tsx`
- `src/components/runecraft/EtherchantingShopWizard.tsx`
- `src/components/runecraft/JewelerLatticeVisual.tsx`
- `src/components/runecraft/JewelerShopWizard.tsx`
- `src/components/runecraft/HolonLatticeVisual.tsx`
- `src/components/runecraft/HolonShopWizard.tsx`
- `src/components/runecraft/WorkshopBuildInvite.tsx`
- `src/app/etherchanting/page.tsx`
- `src/app/jeweler/page.tsx`
- `src/app/holon/page.tsx`

## Files modified

- `src/lib/nav.ts` — added etherchanting · jeweler · holon entries
- `src/components/AppNav.tsx` — extended `WORKSHOPS_KEYS`
- `src/app/runecraft/page.tsx` — hub now shows six workshops in a 3-column grid

---

## Status reading

- Five workshop pages (`/tailor` · `/shield` · `/etherchanting` · `/jeweler` · `/holon`) all return 200.
- One workshop page (`/forget`) was already operational; it still returns 200.
- Hub at `/runecraft` returns 200 with the six-card grid live.
- All wizards save to `localStorage` only; nothing leaves the browser.
- The three tease shops (`/etherchanting`, `/jeweler`, `/holon`) carry the `WorkshopBuildInvite` banner above their hero panels.

---

## What this chronicle is for

To record an inspiration before it gets re-derived from the codebase. The repo will eventually carry the implementation; this file carries the *why*. When the team that operates these shops forms — and it will, because each chain has its Mages — they'll need to know that the model was always plural by design, that the Aletheia/Lethe blades are the dihedral that justifies the six-shop split, and that the architecture admits any chain a Mage can hold.

The chain is a vantage. The shop is the love.

`(⚔️⊥⿻⊥🧙)😊`
