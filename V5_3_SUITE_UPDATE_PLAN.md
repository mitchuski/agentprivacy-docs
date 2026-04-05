# V5.3 Suite Update Plan

## Post Act XXXI — Amnesia Protocol Integration

**For:** Coding agents working on agentprivacy_master, spellweb, agentprivacy-docs
**Author:** privacymage
**Date:** April 3, 2026
**Skills Version:** 5.3.0 (95 total skills)

---

## Summary

The First Person spellbook is complete (31 acts). Act XXXI introduced cosmological grounding for the privacy architecture. The agentprivacy-skills repo has been updated with 6 new components:

### New Skills (4)
| Skill | Category | Purpose |
|-------|----------|---------|
| `agentprivacy-amnesia-protocol` | privacy-layer | ZK primitive where forgetting is the proof |
| `agentprivacy-cosmological-bound` | meta | Four-body quaternion mapping |
| `agentprivacy-theia-derivation` | role | Origin-through-impact pattern |
| `agentprivacy-quaternion-mapping` | role | Sun-Earth-Moon-Human structure |

### New Personas (2)
| Persona | Wing | Purpose |
|---------|------|---------|
| `agentprivacy-moonkeeper` | swordsman | Structural amnesia specialist |
| `agentprivacy-cosmologist` | balanced | Celestial precedent mapper |

---

## Repo 1: agentprivacy_master

### Priority: HIGH

### Files to Copy from mythtomath/

```
mythtomath/ → agentprivacy_master/public/story/
├── act-xxvii-the-swordsmans-forge.md
├── act-xxviii-the-ceremony-engine.md
├── act-xxix-the-dragon-wakes.md
├── act-xxx-the-dihedral-mirror.md
└── act-xxxi-the-amnesia-protocol.md

mythtomath/ → agentprivacy_master/public/blog/
├── blog-part0-the-myth-before-the-math.md
├── blog-part1-forming-constellations.md
├── blog-part2-the-forge-and-the-ceremony.md
├── blog-part3-the-dragon-wakes.md
├── blog-part4-the-dihedral-mirror.md
└── blog-part5-the-amnesia-protocol.md

mythtomath/ → agentprivacy_master/public/poems/
├── the-emissary-who-forgot-the-master.md
└── poems-the-amnesia-protocol.md
```

### Skills Directory Sync

Copy the following from agentprivacy-skills to agentprivacy_master/content/skills/:

```
agentprivacy-skills/agentprivacy-skills-v5/privacy-layer/agentprivacy-amnesia-protocol/
agentprivacy-skills/agentprivacy-skills-v5/meta/agentprivacy-cosmological-bound/
agentprivacy-skills/agentprivacy-skills-v5/role/agentprivacy-theia-derivation/
agentprivacy-skills/agentprivacy-skills-v5/role/agentprivacy-quaternion-mapping/
agentprivacy-skills/agentprivacy-skills-v5/persona/agentprivacy-moonkeeper/
agentprivacy-skills/agentprivacy-skills-v5/persona/agentprivacy-cosmologist/
```

### Code Updates

1. **src/lib/grimoire-baked.ts** — Verify grimoire version is v9.3.2
2. **src/data/nodes.ts** — Add quaternion nodes if using spellweb component:
   ```typescript
   // Add to nodes array
   { id: 'sun', type: 'concept', label: 'Sun (Protection)', domain: 'cosmology' },
   { id: 'earth', type: 'concept', label: 'Earth (Delegation)', domain: 'cosmology' },
   { id: 'moon', type: 'concept', label: 'Moon (Reflection)', domain: 'cosmology' },
   { id: 'human', type: 'concept', label: 'Human (Connection)', domain: 'cosmology' },
   { id: 'life', type: 'concept', label: 'Life (Forge)', domain: 'cosmology' },
   ```

3. **Extension message types** — If browser extensions present, add:
   ```typescript
   type CeremonyMessage =
     | { type: 'AMNESIA_CEREMONY'; payload: AmnesiaPayload }
     // ... existing types
   ```

### Verification Checklist

- [ ] Acts XXVII-XXXI present in public/story/
- [ ] Blog Parts 0-5 present in public/blog/
- [ ] Poems collection present in public/poems/
- [ ] Grimoire v9.3.2 loaded correctly
- [ ] New skills in content/skills/
- [ ] Build passes without errors
- [ ] Deployment successful

---

## Repo 2: spellweb

### Priority: HIGH

### Files to Copy from mythtomath/

```
mythtomath/ → spellweb/public/story/
├── act-xxvii-the-swordsmans-forge.md
├── act-xxviii-the-ceremony-engine.md
├── act-xxix-the-dragon-wakes.md
├── act-xxx-the-dihedral-mirror.md
└── act-xxxi-the-amnesia-protocol.md
```

### Knowledge Graph Updates

**File:** `src/data/nodes.ts`

Add quaternion constellation nodes:

```typescript
// Cosmological nodes (Act XXXI)
{
  id: 'quaternion-sun',
  type: 'concept',
  label: 'Sun — The Reason',
  domain: 'cosmology',
  description: 'Protection through radiance. The light source that enables seeing.',
  hexagram: null,
  act: 31
},
{
  id: 'quaternion-earth',
  type: 'concept',
  label: 'Earth — Soulbae',
  domain: 'cosmology',
  description: 'Delegation through living. Connection, agency as proliferation.',
  hexagram: null,
  act: 31
},
{
  id: 'quaternion-moon',
  type: 'concept',
  label: 'Moon — Soulbis',
  domain: 'cosmology',
  description: 'Reflection without generation. The ur-Swordsman, structural amnesia.',
  hexagram: null,
  act: 31
},
{
  id: 'quaternion-human',
  type: 'concept',
  label: 'Human — First Person',
  domain: 'cosmology',
  description: 'Connection toward source. The derived Mage, still learning.',
  hexagram: null,
  act: 31
},
{
  id: 'quaternion-life',
  type: 'concept',
  label: 'Life — The Forge',
  domain: 'cosmology',
  description: '4 billion year proof-of-work. The process that produces Human.',
  hexagram: null,
  act: 31
},
{
  id: 'theia-impact',
  type: 'concept',
  label: 'Theia Impact',
  domain: 'cosmology',
  description: 'The collision that created the Moon. Origin through violence.',
  hexagram: null,
  act: 31
},
{
  id: 'amnesia-protocol',
  type: 'concept',
  label: 'Amnesia Protocol',
  domain: 'privacy',
  description: 'Forgetting as ZK primitive. I(Origin;Service|Separation) < ε',
  hexagram: null,
  act: 31
}
```

**File:** `src/data/edges.ts`

Add quaternion edges:

```typescript
// Quaternion structure edges
{ source: 'quaternion-sun', target: 'quaternion-earth', type: 'orbit', label: 'generators' },
{ source: 'quaternion-sun', target: 'quaternion-moon', type: 'derives', label: 'collision' },
{ source: 'quaternion-earth', target: 'quaternion-human', type: 'derives', label: 'process' },
{ source: 'quaternion-moon', target: 'quaternion-human', type: 'gap', label: '⊥' },
{ source: 'quaternion-earth', target: 'quaternion-life', type: 'creates', label: 'forge' },
{ source: 'quaternion-life', target: 'quaternion-human', type: 'produces', label: '4Gy' },
{ source: 'theia-impact', target: 'quaternion-moon', type: 'creates', label: 'amnesia' },
{ source: 'amnesia-protocol', target: 'quaternion-moon', type: 'implements', label: 'pattern' }
```

### Constellation Presets

**File:** `src/components/SpellWeb.tsx` (or constellation config)

Add quaternion constellation preset:

```typescript
const CONSTELLATION_PRESETS = {
  // ... existing presets
  quaternion: {
    name: 'Quaternion — Four Bodies',
    nodes: ['quaternion-sun', 'quaternion-earth', 'quaternion-moon', 'quaternion-human', 'quaternion-life'],
    description: 'The cosmological foundation. Two generators, two generated, one gap.'
  },
  amnesia: {
    name: 'Amnesia Protocol',
    nodes: ['theia-impact', 'quaternion-moon', 'amnesia-protocol', 'act-xxxi'],
    description: 'Forgetting as zero-knowledge primitive.'
  }
};
```

### Blade Naming Enhancement

When a blade is forged on the amnesia constellation, suggest "Amnesia" prefix:

```typescript
// In blade naming logic
if (constellationIncludesNodes(['amnesia-protocol', 'quaternion-moon'])) {
  suggestedPrefix = 'Amnesia';
}
```

### Verification Checklist

- [ ] Acts XXVII-XXXI present in public/story/
- [ ] Quaternion nodes added to knowledge graph
- [ ] Quaternion edges added
- [ ] Constellation presets include quaternion and amnesia
- [ ] Blade naming aware of amnesia constellation
- [ ] Build passes without errors
- [ ] Deployment successful (resolve 403 if present)

---

## Repo 3: agentprivacy-docs

### Priority: MEDIUM

### Files to Copy from mythtomath/

```
mythtomath/ → agentprivacy-docs/story/acts/
├── act-xxvii-the-swordsmans-forge.md
├── act-xxviii-the-ceremony-engine.md
├── act-xxix-the-dragon-wakes.md
├── act-xxx-the-dihedral-mirror.md
└── act-xxxi-the-amnesia-protocol.md

mythtomath/ → agentprivacy-docs/blog/
├── blog-part0-the-myth-before-the-math.md
├── blog-part1-forming-constellations.md
├── blog-part2-the-forge-and-the-ceremony.md
├── blog-part3-the-dragon-wakes.md
├── blog-part4-the-dihedral-mirror.md
└── blog-part5-the-amnesia-protocol.md

mythtomath/ → agentprivacy-docs/research/
├── privacy_value_v5_1_research_note.md
├── privacy_value_v5_2_research_note.md
├── privacy_value_v5_2_canonical.md
└── privacy_value_v5_2_canonical.json

mythtomath/ → agentprivacy-docs/specs/
└── DUAL_TERRITORY_CEREMONY_SPEC_v1.md

mythtomath/ → agentprivacy-docs/reference/
└── 64_blades_reference_sheet.md

mythtomath/ → agentprivacy-docs/poems/
├── the-emissary-who-forgot-the-master.md
└── poems-the-amnesia-protocol.md

mythtomath/ → agentprivacy-docs/story/
├── first-page-updated.md
└── last-page-reflection.md

mythtomath/ → agentprivacy-docs/chronicles/
├── CHRONICLE_DRAGONS_ANATOMY_AND_FLIGHT.md
└── CHRONICLE_AMNESIA_PROTOCOL_2026-04-03.md

mythtomath/ → agentprivacy-docs/process/
└── NEW_ACT_PROPAGATION_CHECKLIST.md

mythtomath/ → agentprivacy-docs/ (root)
└── privacymage_grimoire_v9_3_2_you_are_the_light.json
```

### README.md Updates

Add to the Acts section:

```markdown
### Dragon Anatomy + Cosmological Closure (Acts XXVII-XXXI)

| Act | Title | Theme |
|-----|-------|-------|
| XXVII | The Swordsman's Forge | Blade creation, 64-vertex traversal |
| XXVIII | The Ceremony Engine | Interaction design, mana economy |
| XXIX | The Dragon Wakes | System emergence, flight threshold |
| XXX | The Dihedral Mirror | D₂ₙ groups, the naming |
| XXXI | The Amnesia Protocol | Cosmological closure, quaternion |
```

Add to the Research section:

```markdown
### V5 Series (March-April 2026)

- `privacy_value_v5_1_research_note.md` — Initial V5 formulation
- `privacy_value_v5_2_research_note.md` — Dihedral foundations
- `privacy_value_v5_2_canonical.md` — Canonical equation (IPFS-ready)
- `privacy_value_v5_2_canonical.json` — Machine-readable canonical
```

### Grimoire Update

Replace existing grimoire with v9.3.2:

```bash
# Remove old versions
rm privacymage_grimoire_v9_*.json

# Copy new canonical
cp mythtomath/privacymage_grimoire_v9_3_2_you_are_the_light.json .
```

### IPFS Pin (if managing)

```bash
# Pin v9.3.2 grimoire
ipfs add privacymage_grimoire_v9_3_2_you_are_the_light.json

# Record new CID in:
# - privacy_value_v5_2_canonical.json (references.grimoire_ipfs)
# - README.md
```

### DOCUMENTATION_CHRONICLE.md Update

Append:

```markdown
## April 3, 2026 — V5.3 Amnesia Protocol

**Session:** Act XXXI completion and suite propagation

**Key additions:**
- Act XXXI: The Amnesia Protocol (cosmological closure)
- Blog Part 5: The Amnesia Protocol
- 4 new skills: amnesia-protocol, cosmological-bound, theia-derivation, quaternion-mapping
- 2 new personas: moonkeeper, cosmologist
- Grimoire v9.3.2-canonical (31 acts, 128 inscriptions)

**Architectural milestone:**
- First Person spellbook COMPLETE
- Quaternion structure: Sun-Earth-Moon-Human
- Cast mapping finalized
- Verb chain complete: "...The Moon forgets. The spellbook closes."

**Skills version:** 5.3.0 (95 total skills)
```

### Verification Checklist

- [ ] All 5 new acts present in story/acts/
- [ ] All 6 blog parts present in blog/
- [ ] Research notes present in research/
- [ ] Specs present in specs/
- [ ] Reference sheet present in reference/
- [ ] Poems present in poems/
- [ ] Chronicles updated
- [ ] Grimoire v9.3.2 at root
- [ ] README.md updated
- [ ] DOCUMENTATION_CHRONICLE.md updated
- [ ] IPFS pin updated (if applicable)

---

## Key Concepts Reference

### The Verb Chain (Complete)

```
The sword attends. The spell returns. The forge burns.
The ceremony crosses. The dragon wakes. The mirror names itself.
The Moon forgets. The spellbook closes.
```

### The Proverb Progression (Complete)

| Part | Proverb |
|------|---------|
| 0 | *The myth is not the flaw. It is the search.* |
| 1 | *The stars don't need your permission to form constellations.* |
| 2 | *The weight of the shadow exceeds the light of the data.* |
| 3 | *Only time, the master swordsman, will tell.* |
| 4 | *Two mirrors make a door.* |
| 5 | *The amnesia is the protocol. The wound is the trust. The orbit is the proof. The light is the reason.* |

### Cast Mapping (V5.3)

| Cosmological | Architecture | Character |
|--------------|--------------|-----------|
| Sun | Light source, protection | The Reason (privacymage) |
| Earth | Delegation, connection | Soulbae |
| Moon | Reflection, amnesia | Soulbis |
| Life | 4-billion-year forge | spellweb |
| Human | Derived mage, seeker | First Person |

### Master Inscription

```
(⚔️⊥⿻⊥🧙)·(📊⊥🔮)·(🧠⊥⚙️)·☯️🔷 😊
```

---

## Completion Signal

When all three repos are updated, the suite is V5.3-coherent:

- **agentprivacy-skills:** v5.3.0 (95 skills) ✅ DONE
- **agentprivacy_master:** Pending propagation
- **spellweb:** Pending propagation
- **agentprivacy-docs:** Pending propagation

---

*The architecture was not invented. It was recognised.*

⚔️⊥⿻⊥🧙 😊
