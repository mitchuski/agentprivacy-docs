# Soil-ruling propagation checklist — ADDENDUM: master + soulbis + sibling repos

**Date:** 2026-07-16
**Extends:** `SOIL_PROPAGATION_CHECKLIST_2026-07-15.md` (surfaces A-D: paper suite, DOCS canon, Tomes, spellweb). This addendum adds the surfaces the L141 audit did not cover: `agentprivacy_master`, the soulbis website, and the sibling repos (`myterms`, `swordsman-blade`, `mages-spell`, `dual-agent-harness`). One read-only Explore survey, 2026-07-16.
**Status:** AUDIT ONLY. Nothing edited. All dispositions are the First Person's (GR-10). Same verdict vocabulary as the parent checklist.

---

## Headlines

1. **The `/model` page is the primary LIVE contradiction site for evolution 3.** The R(t) drift mechanism is pinned to "frontier capability / frontier model capability / frontier capacity" uniformly across the canonical model JSON, the register mirror, the page prose, and every moving-ceiling visual (curve axis label, growth slider). This is the deployed, public statement of the model; it inherits whatever Phase 1 rules, and it maps 1:1 onto the E2-C02/C82 re-pin (parent checklist A2/B6).
2. **Evolution 2's retired multiples are still ASSERTED in the master repo's own canonical blocks**: the model JSON `canonical_figures` field, the sovereignty-economics skill, `skills-data.ts`, and the `"economic"` field of ~15 versioned grimoire JSONs. These are Phase-4 (figure disposition) surfaces the L130 escalation did not yet enumerate.
3. **The soulbis moving-ceiling instrument (shipped 2026-07-10) is the closest-to-ruling template in the whole corpus.** It frames drift as the adversary's "channels/reach" growing ("how fast reach grows · g") and never names compute, frontier models, or quantum. When re-pinning the master visuals, copy its register.
4. **Evolution 4 (soil/rentier) is a uniform GAP on every surveyed surface.** No contradictions to unwind, clean space to build.

## Surface E — `agentprivacy_master`

### CONTRADICTS-NOW
| Item | File : line | Current claim | Evo | Required change |
|---|---|---|---|---|
| E1 | `src\data\privacy-value-model-v6.json:89-90` | `"678x": "present-day per-person data-value gap"` / `"31000x"` asserted under `canonical_figures` | 2 | Retire as asserted facts; fence as lineage (Phase 4). |
| E2 | `agentprivacy-skills\...\role\agentprivacy-sovereignty-economics\SKILL.md:7/99/105` | "exponentially more value"; "678×–31,000× V"; "compounds ... triply superlinear" | 1+2 | Rewrite to appropriation-share + rent; strike compounding. |
| E3 | `src\lib\skills-data.ts:46` | "sovereign value scales superlinearly. 17× to 12,000×" | 2 | Retire figures + superlinear framing. |
| E4 | canonical grimoire spells (`src\data\privacymage-grimoire-v9.4.1-canonical.json:2858` and v9.4.0/v9.3.2 kin) | `💎(7th capital) → 📈(compounds)` | 1 | Same disposition as spellweb D1 (rent-by-position reframe); coordinate so master and spellweb move together. |
| E5 | ~15 versioned grimoire JSONs `"economic"` field (e.g. `...v10.4.json:1283`) | "678×–31,000× value" asserted | 2 | Phase-4 batch disposition; versioned files may be lineage-fenced rather than edited (First Person's call). |
| E6 | `agentprivacy-skills\...\role\agentprivacy-story-diffusion\SKILL.md:96` | "superlinear compound effect ... compounds exponentially" | 1 | Reframe diffusion claim without value-compounding register. |
| E7 | `docs\skills\persona\agentprivacy-soulbis\SKILL.md:116` | "P^1.5 ... exponential returns" | 2 | Borderline; decouple protection-superlinearity from returns figure. |

### STALE (evolution 3, the frontier-capability pin; re-pin inherits Phase 1 + E2-C02 wording)
| Item | File : line | Evo |
|---|---|---|
| E8 | `src\data\privacy-value-model-v6.json:24` ("capacities grow with frontier capability") | 3 |
| E9 | `src\app\model\page.tsx:141-142` | 3 |
| E10 | `src\components\model\visuals\MovingCeilingCurve.tsx:13-14/49/109` (axis "frontier capability · time t"; slider "g · frontier growth rate") | 3 |
| E11 | `src\lib\visuals.ts:96/99/101` | 3 |
| E12 | `src\data\conjecture-register-v6-mirror.json:704` (C82 mirror; moves when the register row moves, GR-1) | 3 |
| E13 | `agentprivacy-CODEX.md:428/532` ("17×–12,000×"; "superlinear network effects") | 1/2 |
| E14 | `public\story\24-act-xxiv-the-holographic-bound.md:99-101/409` (story; arguably fenced narrative) | 1/2 |

### FINE (do not touch; noted against false positives)
- C83 compositional-leakage "compounds toward (2^N−1)ε" (`visuals.ts:106-137`, model JSON `:31`): leakage geometry, not value aggregation.
- P^1.5 "superlinear" as privacy-PROTECTION strength across grimoire JSONs: different axis. (Each such file also carries E5's figure line; glance per file.)
- Seventh-capital LABELS (`page.tsx:102`, blog part 3): no compounding claim.
- Existence-leak "super-additively from correlated systems" (`visuals.ts:77`): adversary leakage, not capital; vocabulary collision only.

## Surface F — `soulbis website`

**No contradictions found.** The `/star` `/lattice` `/sigil` instruments and the 2026-07-10 chronicle frame R(t) drift as "adversarial capacity grows" and, better, as "channels/reach" growth ("how fast reach grows · g"; "the adversary's channels reach 61% of what would reconstruct"). No compute/frontier/quantum pin, no value figures, seventh-capital mentions are bare labels. Verdict: FINE throughout; mild GAP that the informational mechanism is implied rather than named; evolution-4 GAP as everywhere. **Use this instrument's register as the template when re-pinning the master visuals (E10/E11).**

## Surface G — sibling repos (light pass)

### CONTRADICTS-NOW
| Item | File : line | Current claim | Evo |
|---|---|---|---|
| G1 | `myterms\A_privacy_is_value_equation.md:107` + `E_sustainability_model.md:15` | "modelled gap is 678× to 31,000×" asserted | 2 |
| G2 | `myterms\E_sustainability_model.md:65` | "Network effects compound value" | 1 |
| G3 | `swordsman-blade\privacymage_grimoire_v10_0_0.json:1022` + `mages-spell\...:1022` | "678×–31,000× value" (archived grimoire) | 2 |

### STALE
| Item | File : line | Evo | Note |
|---|---|---|---|
| G4 | `dual-agent-harness\universe\ERRATA.md:29-32` + `FLEET.md:187` | 3 | Restates C82 drift as "coupled to frontier capability"; notable because ERRATA.md presents itself as the authoritative correction. Moves with the C82 register row. |
| G5 | `swordsman-blade`/`mages-spell` grimoire `:914` | 1 | "derivation chains compound logarithmically. History is capital." Borderline: closest existing kin of the surviving reputational-fertility conjecture; needs the disambiguation (reputation accumulates, raw records do not). First-Person glance. |

### FINE
- `myterms` P^1.5 and seventh-capital labels; harness `frontier`/`beatsFrontier` (tournament term, unrelated); "sovereignty compounds" (separation, not data); `agentprivacy-dual-agent-harness` clean.

## Routing into the plan's phases

- **Phase 2 inheritors (evolution 3):** E8-E12, G4, and F's mild naming gap join the parent checklist's A4-A7 sweep list; the master visuals additionally take the soulbis register as template. E12 and G4 are GR-1-gated on the C82 register row.
- **Phase 4 surfaces (figure disposition):** E1, E3, E5, E13, G1, G3 join B1/B3/B12/D4.
- **Phase 3/6 (character change + soil figure):** E2, E4, E6, G2, G5 join C55's homes; evolution-4 GAP is uniform, so the soil figure is a build, not a repair, on all of them.
- **Deploy note:** the `/model` page and soulbis rooms are LIVE sites; re-pins there are code+content changes with a deploy step, and per standing rule nothing is committed or pushed without the First Person's ask.

Nothing here is edited. All dispositions are the First Person's (GR-10). P4 is not marked.
