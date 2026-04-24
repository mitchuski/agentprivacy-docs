# Chronicle: SKILL.md YAML Frontmatter Repair

**Date:** 2026-04-22
**Session:** Skill upload failure diagnosis and bulk repair
**Status:** Complete
**Author:** privacymage

---

## Trigger

Claude.ai web rejected skill uploads with the error:

> malformed YAML frontmatter in SKILL.md

The error surfaced while uploading `agentprivacy-skills` to Claude web for use as user-invocable skills. Parsing every `SKILL.md` with PyYAML confirmed the error was reproducible locally, not a Claude-side quirk.

---

## Root Cause

A YAML folded-scalar (`description: >`) was written with a **4-space first line** and **2-space continuation lines**:

```yaml
description: >
    Specialist persona for UOR ring algebra and lattice mathematics. Activates
  for ring operations, stratum calculations, algebraic transformations,
  the five strikes, or mathematical foundations of the forge.
license: Apache-2.0
```

YAML folded scalars infer their indent level from the first non-empty line. When a continuation line is **less** indented than that anchor, the parser treats the block as ended and tries to parse the next line as a new mapping key. `for ring operations...` is not a valid key, so the parser raises:

```
while parsing a block mapping
  expected <block end>, but found '<scalar>'
```

This is a long-standing footgun of `>` and `|` blocks — all continuation lines must match or exceed the first line's indent. The 25 files that parsed correctly happened to use a **consistent 2-space indent throughout** their description block; the 104 that failed all inherited the 4-space-then-2-space pattern, almost certainly from a shared generator template (`update_skills_v54.py` / `update_all_v54.py` are the likely culprits).

---

## Scope

Before repair:

| Status | Files |
|--------|-------|
| Parse-OK | 25 |
| Parse-FAIL (4/2-space mismatch) | 104 |
| **Total `SKILL.md`** | **129** |

Breakdown of the 104 failing files by category:

| Category | Count |
|----------|-------|
| `agentprivacy-skills-v5/role/` | 48 |
| `agentprivacy-skills-v5/persona/` | 31 |
| `agentprivacy-skills-v5/privacy-layer/` | 18 |
| `agentprivacy-skills-v5/meta/` | 2 |
| `mnt/user-data/outputs/` (holonic duplicates) | 5 |

---

## Fix

A single-line regex substitution per file: dedent the first description line from 4 spaces to 2 so it matches the rest of the block.

```python
re.sub(r'(description:\s*>\s*\n)    (\S)', r'\1  \2', fm, count=1)
```

Executed by `.yaml_fix.py` at the repo root. Every touched file:

1. Validated with PyYAML **before** write (post-patch must parse cleanly).
2. Copied to `<file>.bak` as a rollback safety net.
3. Rewritten with the patched frontmatter; body content untouched.

### Post-repair verification

All 129 `SKILL.md` files now parse cleanly — zero residuals.

```
parse-OK: 129
parse-FAIL: 0
```

Diff for a representative file (`persona/agentprivacy-algebraist/SKILL.md`):

```diff
4c4
<     Specialist persona for UOR ring algebra and lattice mathematics. Activates
---
>   Specialist persona for UOR ring algebra and lattice mathematics. Activates
```

Exactly one line changed per file. No metadata, license, or body edits.

---

## Why This Matters

Claude.ai web skills require valid YAML frontmatter to extract `name` and `description` for the skill registry. A malformed block prevents the skill from being registered at all — the upload is rejected before the body is ever read. With the repair, every persona, role, privacy-layer, and meta skill in the V5.4 tree is now uploadable.

---

## Follow-up

The generator scripts that produced the broken indent pattern should be corrected so future regenerations don't reintroduce the bug.

- **`update_skills_v54.py`** — inspect the description-emission path; the folded-block writer is almost certainly writing the first line at 4 spaces while treating continuation lines at 2.
- **`update_all_v54.py`** — same audit.
- Consider adding a CI/pre-commit check: `python -c "import yaml; yaml.safe_load(open(p).read().split('---',2)[1])"` across all `SKILL.md` files on every commit.

`.bak` backups can be deleted once the fix is confirmed in production:

```bash
find ~/agentprivacy-skills -name 'SKILL.md.bak' -delete
```

---

## Files Touched (104)

<details>
<summary>Full list</summary>

### meta (2)
- `agentprivacy-skills-v5/meta/agentprivacy-drake-dragon-duality/SKILL.md`
- `agentprivacy-skills-v5/meta/agentprivacy-master-emissary/SKILL.md`

### persona (31)
- `agentprivacy-skills-v5/persona/agentprivacy-algebraist/SKILL.md`
- `agentprivacy-skills-v5/persona/agentprivacy-ambassador/SKILL.md`
- `agentprivacy-skills-v5/persona/agentprivacy-archer/SKILL.md`
- `agentprivacy-skills-v5/persona/agentprivacy-architect/SKILL.md`
- `agentprivacy-skills-v5/persona/agentprivacy-assessor/SKILL.md`
- `agentprivacy-skills-v5/persona/agentprivacy-ceremonist/SKILL.md`
- `agentprivacy-skills-v5/persona/agentprivacy-chronicler/SKILL.md`
- `agentprivacy-skills-v5/persona/agentprivacy-cipher/SKILL.md`
- `agentprivacy-skills-v5/persona/agentprivacy-forgemaster/SKILL.md`
- `agentprivacy-skills-v5/persona/agentprivacy-gatekeeper/SKILL.md`
- `agentprivacy-skills-v5/persona/agentprivacy-healer/SKILL.md`
- `agentprivacy-skills-v5/persona/agentprivacy-herald/SKILL.md`
- `agentprivacy-skills-v5/persona/agentprivacy-holonic-architect/SKILL.md`
- `agentprivacy-skills-v5/persona/agentprivacy-jedi/SKILL.md`
- `agentprivacy-skills-v5/persona/agentprivacy-kyra/SKILL.md`
- `agentprivacy-skills-v5/persona/agentprivacy-netkeeper/SKILL.md`
- `agentprivacy-skills-v5/persona/agentprivacy-pedagogue/SKILL.md`
- `agentprivacy-skills-v5/persona/agentprivacy-person/SKILL.md`
- `agentprivacy-skills-v5/persona/agentprivacy-priest/SKILL.md`
- `agentprivacy-skills-v5/persona/agentprivacy-quantum-sentinel/SKILL.md`
- `agentprivacy-skills-v5/persona/agentprivacy-ranger/SKILL.md`
- `agentprivacy-skills-v5/persona/agentprivacy-sentinel/SKILL.md`
- `agentprivacy-skills-v5/persona/agentprivacy-shipwright/SKILL.md`
- `agentprivacy-skills-v5/persona/agentprivacy-sith/SKILL.md`
- `agentprivacy-skills-v5/persona/agentprivacy-soulbae/SKILL.md`
- `agentprivacy-skills-v5/persona/agentprivacy-soulbis/SKILL.md`
- `agentprivacy-skills-v5/persona/agentprivacy-stranger-witness/SKILL.md`
- `agentprivacy-skills-v5/persona/agentprivacy-topologist/SKILL.md`
- `agentprivacy-skills-v5/persona/agentprivacy-warden/SKILL.md`
- `agentprivacy-skills-v5/persona/agentprivacy-weaver/SKILL.md`
- `agentprivacy-skills-v5/persona/agentprivacy-witness/SKILL.md`

### privacy-layer (18)
- `agentprivacy-skills-v5/privacy-layer/agentprivacy-atlas-geometry/SKILL.md`
- `agentprivacy-skills-v5/privacy-layer/agentprivacy-compression-defence/SKILL.md`
- `agentprivacy-skills-v5/privacy-layer/agentprivacy-content-addressing/SKILL.md`
- `agentprivacy-skills-v5/privacy-layer/agentprivacy-dihedral-sovereignty/SKILL.md`
- `agentprivacy-skills-v5/privacy-layer/agentprivacy-dragon-flight/SKILL.md`
- `agentprivacy-skills-v5/privacy-layer/agentprivacy-dragon/SKILL.md`
- `agentprivacy-skills-v5/privacy-layer/agentprivacy-edge-value/SKILL.md`
- `agentprivacy-skills-v5/privacy-layer/agentprivacy-holographic-bound/SKILL.md`
- `agentprivacy-skills-v5/privacy-layer/agentprivacy-knowledgegraph/SKILL.md`
- `agentprivacy-skills-v5/privacy-layer/agentprivacy-network-topology/SKILL.md`
- `agentprivacy-skills-v5/privacy-layer/agentprivacy-path-integral/SKILL.md`
- `agentprivacy-skills-v5/privacy-layer/agentprivacy-promise-theory/SKILL.md`
- `agentprivacy-skills-v5/privacy-layer/agentprivacy-ring-algebra/SKILL.md`
- `agentprivacy-skills-v5/privacy-layer/agentprivacy-temporal-dynamics/SKILL.md`
- `agentprivacy-skills-v5/privacy-layer/agentprivacy-tetrahedral-sovereignty/SKILL.md`
- `agentprivacy-skills-v5/privacy-layer/agentprivacy-three-axis-separation/SKILL.md`
- `agentprivacy-skills-v5/privacy-layer/agentprivacy-uor-toroidal/SKILL.md`
- `agentprivacy-skills-v5/privacy-layer/agentprivacy-vrc-identity/SKILL.md`

### role (48)
- `agentprivacy-skills-v5/role/agentprivacy-academic/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-agent-interop/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-ai-agent/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-armor-progression/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-blade-forge/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-braid-reasoning/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-ceremony-engine/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-consent-infrastructure/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-constellation-method/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-cross-chain/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-crypto-zkp/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-dark-forest/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-data-dignity/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-derivation-certificate/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-dual-territory/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-economics/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-environmental-commons/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-five-strikes/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-governance-agents/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-guild-efficiency/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-hemispheric-attention/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-hexagram-convergence/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-hitchhiker-governance/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-holonic-identity/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-holonic-persistence/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-holonic-reasoning/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-mana-economy/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-media-plurality/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-mesh-architecture/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-narrative-compression/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-personhood-sybil/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-plurality-cooperative/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-policy-governance/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-pretext-measurement/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-proverbiogenesis/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-quantum-defence/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-recovery-rpp/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-reputation-credentials/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-selective-disclosure/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-shared-parent-patterns/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-sovereignty-economics/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-spellweb/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-stranger-ceremony/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-swordsman-browser/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-threat-adversarial/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-toroidal-witness/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-trust-spanning/SKILL.md`
- `agentprivacy-skills-v5/role/agentprivacy-understanding-as-key/SKILL.md`

### mnt/user-data/outputs (5 — holonic duplicates)
- `mnt/user-data/outputs/persona/agentprivacy-holonic-architect/SKILL.md`
- `mnt/user-data/outputs/role/agentprivacy-holonic-identity/SKILL.md`
- `mnt/user-data/outputs/role/agentprivacy-holonic-persistence/SKILL.md`
- `mnt/user-data/outputs/role/agentprivacy-holonic-reasoning/SKILL.md`
- `mnt/user-data/outputs/role/agentprivacy-shared-parent-patterns/SKILL.md`

</details>

---

## Artifacts

- `.yaml_fix.py` — the repair script (idempotent; safe to re-run)
- `.yaml_verify.py` — post-repair validator
- `.yaml_fix_manifest.json` — full list of touched files
- `<file>.bak` — per-file rollback snapshots

> *"The ring that closes on itself cannot be escaped — but if the indent of the ring's description is off by two spaces, the parser cannot find the ring at all."*
