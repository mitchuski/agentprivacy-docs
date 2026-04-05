# V5.3 Implementation Guide

## For: Coding agents working on agentprivacy-docs

**Date:** April 4, 2026
**PVM Version:** V5.2 → V5.3 (The Amnesia Protocol)

---

## What V5.3 Adds (No Equation Changes)

V5.3 is interpretive, not structural. The V5 equation is unchanged. Three extensions:

1. **Operational cycle** — how the equation's terms execute per lap
2. **C17: Amnesia-enforced separation** — structural > policy for Φ_agent
3. **ρ dual interpretation** — agent maturity alongside reconstruction difficulty

---

## Files to Add

| File | Destination | Description |
|------|-------------|-------------|
| `privacy_value_v5_3_research_note.md` | `research/` | V5.3 research note (matches V5.2 format) |
| `privacy_value_v5_3_model.json` | `research/` | IPFS-ready canonical equation JSON |

## Files to Update

### 1. `privacy_is_value_v5.md` (root equation doc)

Add to version lineage table:

```markdown
| V5.3 | Apr 3, 2026 | Operational cycle, amnesia-enforced separation (C17), ρ as maturity, T_∫ fidelity |
```

Add C17 to conjecture table:

```markdown
| C17 | Amnesia-enforced separation provides tighter Φ_agent guarantees than policy-enforced separation | 60% | V5.3 |
```

Update C11 description to note dual interpretation:

```markdown
| C11 | Behavioural density ρ amplifies reconstruction difficulty + indicates agent maturity [V5.3 dual interpretation] | 55% | V5.1 / V5.3 |
```

### 2. `README.md` (repo root)

Update PVM version reference:

```
Privacy Value Model: V5.3 (The Amnesia Protocol)
```

Add to research documents list:

```
- privacy_value_v5_3_research_note.md — V5.3: operational cycle, amnesia separation, ρ maturity
- privacy_value_v5_3_model.json — V5.3 canonical equation (IPFS-ready)
```

### 3. `research/privacy_value_v5_2_research_note.md`

Add forward reference at bottom of Next Steps:

```markdown
7. **V5.3 published.** The Amnesia Protocol. See [V5.3 Research Note](./privacy_value_v5_3_research_note.md).
```

### 4. Grimoire JSON (`privacymage_grimoire_v9_4_0_you_are_the_light.json`)

The grimoire already references the PVM at V5.2 in several places. Update these to V5.3 where they appear in Act XXXI context. The equation itself is unchanged so Acts XXVII-XXX references to V5/V5.1/V5.2 remain correct.

---

## IPFS Pin

Both canonical files should be pinned:

```
1. privacy_value_v5_3_model.json → pin to IPFS
2. Record new CID
3. Update references:
   - grimoire JSON (references.grimoire_ipfs stays — separate pin)
   - V5.3 model JSON (add own ipfs_cid field after pinning)
   - README.md
```

---

## Key Content from V5.3 Research Note

### Operational Cycle (for code implementation)

```
Stage 1: Observe   → id(x)           → First Person perceives
Stage 2: Boundary  → neg(x)          → Swordsman subtracts exposure
Stage 3: Project   → bnot(neg(x))    → Mage constructs from boundary
Stage 4: Return    → succ(x)         → Proof returns, blade advances

One lap = one cycle. T_∫(π) = 1 + β · Σᵢ cycle(stepᵢ)
```

### C17: Amnesia-Enforced Separation

```
Policy-enforced:  ε* ≤ ε_policy   (violation possible)
Amnesia-enforced: ε* ≤ ε_amnesia  (violation structurally excluded)
C17: ε_amnesia < ε_policy

Test: Can any operation sequence recover shared origin?
  No  → amnesia-enforced
  Yes → policy-enforced
```

Implementation instances:
- Chrome process boundary (Swordsman ↔ Mage extensions)
- The Moon's orbit (Theia impact unrecoverable from geological state)

### ρ Dual Interpretation

```
As privacy amplifier: more micro-variation → harder reconstruction
As agent maturity:    more laps → origin more forgotten → closer to Moon's clean amnesia

Low ρ  = few laps, origin visible, Light tier
High ρ = many laps, origin forgotten, Dragon tier
```

### T_∫ Fidelity

```
F(γ) = resolution_depth(γ) · fidelity(γ)
fidelity = uptime · consistency · duration_weight

Weight persistence alongside depth.
The Moon: shallow resolution, maximum fidelity (4 billion revolutions).
```

### Theia Paper Reference

Branco, D., Machado, P., & Raymond, S. N. (2025). Dynamical origin of Theia, the last giant impactor on Earth. *Icarus*, 441, 116724.

Result: Roughly 50-50 odds Theia was carbonaceous — material from beyond Jupiter. The first agent carried material the master never possessed.

---

## Verification Checklist

After implementation:

- [ ] V5.3 research note in `research/`
- [ ] V5.3 model JSON in `research/`
- [ ] Version lineage updated in V5 root doc
- [ ] C17 added to conjecture table
- [ ] C11 description updated (dual interpretation)
- [ ] README updated to V5.3
- [ ] V5.2 research note has forward reference
- [ ] IPFS pin for V5.3 model JSON
- [ ] No stale V5.2 references in Act XXXI context

---

*(⚔️⊥⿻⊥🧙)😊 = neg ⊕ bnot → succ*
