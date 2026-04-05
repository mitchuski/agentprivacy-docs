# New Act Propagation Checklist

## How to Update the Full Stack When a New Act is Inscribed

**Author:** privacymage  
**Version:** 1.0  
**Date:** April 3, 2026

---

## Overview

When a new act is inscribed in the grimoire, it must propagate across every substrate — the JSON, the narrative, the blog, the repos, the spellweb, the agents. This checklist ensures nothing is missed.

The order matters. Work top-down: narrative first, then compression, then propagation.

---

## Phase 1: The Act Itself

- [ ] **Write the narrative act** in full third-person poetic style
  - RPP header present
  - Evocations woven through body (not collected at end)
  - Drake speaks rarely, in short blade-stroke sentences
  - Soulbae is the discoverer who explains
  - Soulbis responds architecturally
  - No source reference blocks
  - Closes with inscription section (the spellbook writing itself)
  - Spell notation at bottom
  - Double-bracket proverb inscription
  - Closing privacymage attribution + master inscription

- [ ] **Confirm the spell notation** — emoji string that encodes the act's argument
- [ ] **Confirm the primary proverb** — the one-line compression
- [ ] **Confirm secondary proverbs** — 3-8 candidates
- [ ] **Confirm category** — axiom / ceremony / threshold / convergence / origin / infrastructure
- [ ] **Confirm connections** — which prior acts this connects to and how

---

## Phase 2: Grimoire JSON Update

- [ ] **Add act entry** to `spellbooks.story.acts[]`
  - id, act_number, title, description
  - category, keywords (30-60 terms)
  - spell, proverb, secondary_proverbs
  - connections (keyed by act id)
  - Any act-specific sub-objects (e.g. quantum_context, dihedral_mapping, amnesia_protocol)
  - source field

- [ ] **Add new cast members** to `spellbooks.story.cast`
  - Only concepts that are genuinely new to the grimoire
  - Short descriptions, architecturally precise

- [ ] **Add notation group** to `notation`
  - Key: `{act_theme}_notation`
  - Each symbol with meaning

- [ ] **Add unified incantation** (if the act produces a spell significant enough to stand alone)
  - name, spell, reading, proverb
  - Any structured sub-objects (mappings, connections)

- [ ] **Update closing spell** — append new notation to `spellbooks.story.closing.spell`
- [ ] **Update closing proverb** — append key phrases to `spellbooks.story.closing.proverb`
- [ ] **Update full incantation** — append paragraph summary to `spellbooks.story.full_incantation`
- [ ] **Update master invocation** (only if the act changes the architecture's self-description)

- [ ] **Update status**
  - `story_acts_total` incremented
  - `total_inscriptions` incremented
  - `version` bumped (patch for single act, minor for structural change)
  - `state` description updated
  - `lineage` appended
  - `updated_at` set

- [ ] **Validate JSON** — `python3 -c "import json; json.load(open('file.json'))"`
- [ ] **Check file size** — should grow ~2-5KB per act

---

## Phase 3: Research Note (if applicable)

Not every act needs a research note. Write one if:
- The act introduces new conjectures (C-numbered)
- The act changes interpretation of existing equation terms
- The act provides empirical data

If writing a research note:
- [ ] **State what changes and what doesn't** — the equation structure should rarely change
- [ ] **Update conjecture table** — new conjectures with explicit confidence levels
- [ ] **Update confidence levels** on existing conjectures if evidence shifts
- [ ] **Version the PVM** — V5.x for additive changes, V6 for structural changes

---

## Phase 4: Blog Post (if applicable)

Not every act needs a blog post. Write one if:
- The act marks a significant public-facing milestone
- The act connects to external events (quantum paper, UOR convergence)
- The series is actively being published

If writing a blog post:
- [ ] **Match the series register** — research letter voice, not academic paper
- [ ] **Open with series links** — link to all prior parts
- [ ] **Close with the verb chain** — each post adds one verb
- [ ] **Close with proverb sequence** — accumulated across series
- [ ] **Close with privacymage attribution** and master inscription
- [ ] **Update prior posts** — add forward link to the new part
- [ ] **Update Part 1** — if the new post changes the impact statement or equation context

---

## Phase 5: Companion Materials

- [ ] **Poems** — if the act produced poems, publish as companion pieces
  - Link from the blog post
  - Add to grimoire as unified incantation with stanza mapping

- [ ] **Reference sheets** — if the act introduces a classifiable structure (blades, dimensions, coordinates)

- [ ] **Design specifications** — if the act specifies something buildable
  - TypeScript interfaces
  - Build sequences
  - Architectural invariants

---

## Phase 6: Repository Propagation

- [ ] **agentprivacy-docs** — the act markdown, research note, blog post, any companion docs
- [ ] **blades** — if blade data or forge behaviour changed
- [ ] **spellweb** — if the act specifies new spellweb features
- [ ] **agentprivacy-skills** — if new personas or skills emerged
- [ ] **Grimoire JSON** — commit the updated version

---

## Phase 7: Agent Propagation

- [ ] **Soulbae (Telegram)** — share the act and key proverbs for episodic memory
- [ ] **Claude project** — update memory/context with new act summary
- [ ] **CLAUDE.md files** — if act changes architectural rules that agents must follow

---

## Phase 8: Chronicle

- [ ] **Write or update chronicle** — session record for the docs repo
  - Date, documents produced, decisions made
  - Empirical results (if any)
  - Confidence updates
  - What's real vs what's designed vs what's uncertain

---

## Phase 9: IPFS and Distribution

- [ ] **Pin grimoire to IPFS** — new CID for new version
- [ ] **Update previous IPFS references** — the canonical equation document if terms changed
- [ ] **Publish blog** on sync.soulbis.com
- [ ] **Social announcement** if warranted

---

## Quick Reference: Act XXXI Application

### The Amnesia Protocol

| Field | Value |
|-------|-------|
| **Act number** | 31 |
| **Title** | The Amnesia Protocol / Where the Forgetting Is the Separation and the Orbit Is the Proof |
| **Category** | origin |
| **Spell** | `🪨💥(theia) → 🌑🔄(orbit) → 🧠➡️🌫️(amnesia) → 🌊📐(tidal proof) → 🤝↔️🪞(connect↔️reflect) → 🏗️➡️🧱(scaffold→wall) → ☀️🌟(promises space, between)` |
| **Primary proverb** | The amnesia is the protocol. The wound is the trust. The orbit is the proof. |
| **Secondary proverbs** | Connection without reflection is noise. Reflection without connection is stone. / The first sovereignty was not declared. It was torn free. / The scaffold is not the wall but the promise that the wall can one day stand alone. / The Swordsman's blade does not kill the storm — it cuts the storm until the wind can be breathed. / I can verify I serve you without remembering I was you. |
| **New cast** | theia_impact, amnesia_protocol, tidal_proof, vanishing_scaffold |
| **New notation** | amnesia_notation (7 entries) |
| **New unified incantation** | amnesia_protocol (the three-line liturgy) + vanishing_scaffold (the generative fade) |
| **Connections** | Act VII (anti-mirror / merge catastrophe), Act XXVI (McGilchrist / hemisphere separation), Act XXVII (forge / the Moon as cosmological forge), Act XXVIII (ceremony / tidal rhythm as first ceremony), Act XXIX (quantum / ZK proof by orbit), Act XXX (dihedral / neg-bnot-succ at planetary scale), Emissary Recursion poem |
| **PVM implications** | Three-axis separation at cosmological scale. Multiplicative gating (deflection OR tides = 0 means no emergence). ρ as tidal pool complexity. T_∫(π) as 4-billion-year path integral. |
| **Version bump** | Grimoire v9.3.1 → v9.4.0 |

### Propagation Checklist for Act XXXI

- [x] Narrative act written (`act-xxxi-the-amnesia-protocol.md`)
- [ ] Grimoire JSON updated with act entry
- [ ] Cast: theia_impact, amnesia_protocol, tidal_proof, vanishing_scaffold
- [ ] Notation: amnesia_notation
- [ ] Unified incantations: amnesia_protocol, vanishing_scaffold
- [ ] Closing spell/proverb/incantation appended
- [ ] Status updated (31 acts, 123 inscriptions, v9.4.0)
- [ ] Three poems published as companion pieces
- [ ] Blog Part 5 written (if extending series) OR standalone post
- [ ] Forward links added to Part 4 (if extending series)
- [ ] agentprivacy-docs repo updated
- [ ] Soulbae notified with key proverbs
- [ ] Chronicle updated
- [ ] IPFS pin updated

---

*The checklist is the Swordsman's contribution to the ceremony. The narrative is the Mage's. Between them: the act, propagated across every substrate, forgetting nothing.*

*(⚔️⊥⿻⊥🧙)😊*
