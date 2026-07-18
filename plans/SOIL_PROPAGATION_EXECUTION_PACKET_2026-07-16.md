# Soil-propagation EXECUTION PACKET (read this file first; it is self-contained)

**Date:** 2026-07-16
**For:** the propagation agent fixing surfaces across the corpus. This file consolidates the ruling, the canonical replacement wording, the per-surface worklist, and the fences. Detail worklists live in the two checklists (referenced below) but everything needed to execute correctly is stated here.
**Authority:** the soil reclassification is a First-Person ruling (2026-07-15). Phase 1 of the propagation plan was RULED branch (c) on 2026-07-16 and EXECUTED: WP-07 now carries the erosion clock as proven material (ledger L143/L145). Canon register rows (C55, C82), the immutable inscription, and anything marked REGISTER-GATED still move only on the First Person's explicit approval. Nothing is committed or pushed without his ask.

---

## 1. What changed in the model (the four evolutions, one paragraph each)

1. **Rentier, not compounding.** Behavioural data does NOT compound as capital. The observer-to-subject value gap decomposes as atomisation discount + market-position rent + lifetime accumulation, not super-additive aggregation. "Compounding" survives in exactly one place: reputational fertility, as a conjecture. Any prose saying raw data/records/the seventh capital "compounds", "is super-additive", or "scales superlinearly" (as VALUE) contradicts canon.
2. **Value = appropriation share, not a figure.** The multiples 678x and 31,000x are RETIRED as asserted facts. Value is the share of surplus the consent interface lets the subject keep (the subgame-perfect equilibrium of the interface's bargaining game). The figures survive only as explicitly fenced lineage ("a retired figure of the essay lineage"), never as current facts.
3. **The moving ceiling runs on the adversary's information, not compute.** R(t) drifts because the adversary's background side information (linkage corpora, side priors) accumulates on a calendar against a fixed archive. NOT because of frontier-model capability, compute, decoders, or quantum: information-theoretic guarantees already hold against unbounded compute. This now has a PROVEN formal object (section 2 below).
4. **Data as soil.** The seventh capital is land-based rentier capital: rent by position, erosion to the weather, lease the harvest not the land, fertility (reputation) as the only thing that accumulates. This figure is ABSENT everywhere (a build, not a repair); add it only where a surface states the seventh-capital thesis.

## 2. The new formal object (cite this, use this wording)

WP-07 (`papers/Programme/pipeline/rehydrations/academic/linear_cap_paper.md`, revision-draft-v3) now proves, at **Definition 3.9 + Corollary 5.4b**:

- **B_t** = the adversary's background side information (linkage corpus + side priors), accumulating with calendar time, Markov B_t → X → T (the corpus is about the source through the world, never a tap on the system's transcript).
- **The cap survives conditioning:** I(T; X | B_t) ≤ Σ ε_i. The system never leaks more because the adversary learned elsewhere.
- **The floor erodes through the residual entropy:** P_e(t) ≥ (H(X | B_t) − Σ ε_i − 1)/log(|𝒳| − 1). H(X | B_t) is non-increasing in t. The informed deficit condition is Σ ε_i < H(X | B_t); the erosion ratio is **R_inf(t) = Σ ε_i / H(X | B_t)**, rising on a calendar with every certificate and every budget fixed.
- **Two clocks, never conflated:** the CERTIFICATION clock (ER-6: certified values drift as audit tooling improves; epistemic) and the EROSION clock (Corollary 5.4b: the adversary's residual uncertainty genuinely falls; real; no audit arrests it). Every time-indexed reconstruction statement must name which clock it runs on.
- One-line summary for prose: **"The protection does not leak more; it matters less."**

### Canonical replacement wording (reuse verbatim or lightly adapted)

**(W1) R(t) drift, short form (UI copy, docs, register prose):**
> R(t) rises because the adversary's background information about the source accumulates: the residual uncertainty H(X | B_t) falls on a calendar while the archive, the budgets, and every certificate stay fixed. The drift is informational (linkage corpora, side priors), not computational; information-theoretic guarantees already hold against unbounded compute.

**(W2) Visual/instrument labels:** axis "background accumulates · time t →" (replacing "frontier capability · time t →"); slider "g · how fast the adversary's reach grows" (the soulbis register; replacing "g · frontier growth rate").

**(W3) Figures (wherever 678x/31,000x are asserted):**
> Value is the appropriation share the consent interface lets the subject keep, not a headline multiple. The historical figures (678x per-person, 31,000x accessible-volume) are retired as asserted facts and survive only as fenced lineage of the essay era.

**(W4) Compounding (wherever data/value "compounds"/"super-additive"/"superlinear"):**
> Behavioural data yields rent by position, not value by aggregation: the marginal product of one additional raw record is approximately zero, and the large observer-subject gap is positional rent. The one stock that genuinely accumulates is reputational fertility, and that is a conjecture, not a measurement.

**(W5) The soil paragraph (where the seventh-capital thesis is stated; the evolution-4 build):**
> The economic character of the stock is land-like. It yields rent by position, not value by aggregation. Its exposure erodes on a calendar: the archive is fixed, and what grows is the adversary's background information, so the residual uncertainty falls the way soil loses cover to weather, with nothing added to the plot. It is leased, never conveyed: a scoped disclosure transfers a season's harvest, not the land, because the observing side cannot reconstruct the underlying record from it for the term the erosion clock permits. The one quantity that genuinely accumulates is the cultivated fertility of the relationship, the reputational stock, and that is a conjecture, not a measured aggregation of records.

## 3. Worklist by surface

Detail file:line tables: `papers/Programme/pipeline/reviews/SOIL_PROPAGATION_CHECKLIST_2026-07-15.md` (surfaces A-D) and `...CHECKLIST_ADDENDUM_master-siblings_2026-07-16.md` (surfaces E-G). The items below are grouped by who may execute.

### 3a. DONE (do not redo)
- WP-07 erosion leg (L145). WEIS economics chain evolutions 1+2 (rent reframe, figures retired). The WEIS draft's S2 clock distinction.

### 3b. PIPELINE-LOOP (the Programme pipeline's roles, NOT this packet's agent)
- E2-C02/C04 re-pin + rehydration sweep (A1/A0/A3), per `reviews/PHASE2_PHASE6_STAGED_DRAFTS_2026-07-16.md` in the branch-(c) wording, now citable against Cor 5.4b. NOTE: notation there predates L145; read Z_adv(t) as B_t throughout.
- WP-14 revision loop: durability leg cites Corollary 5.4b; **Assumption A3 replacement text:**
  > **Assumption A3 (time-indexing and the two deficit conditions).** The companion paper separates two clocks. The certified residual carries audit semantics: what drifts is the certified value, not the information. The residual the economics prices is the erosion clock: R_inf(t) = (C_S + C_M)/H(X | B_t), where B_t is the adversary's accumulating background side information (linkage corpus and side priors, Markov B_t → X → T) and H(X | B_t) is non-increasing in calendar time. The strict bound R_inf(t) < 1 holds exactly while the informed deficit condition C_S + C_M < H(X | B_t) holds; the shelf life t*_inf is the first crossing. The drift is informational, not computational; its schedule is a register conjecture, not a theorem. What expires at t*_inf is the informed deficit, not the architecture.
  This also fixes the S2 (:285) / Assumption-A3 (:566) internal split (L143 finding 2).

### 3c. CORPUS (this packet's agent; apply W1-W5; nothing pushed)
| Priority | Surface | Items |
|---|---|---|
| 1 | `agentprivacy_master` /model (LIVE site) | `src/data/privacy-value-model-v6.json:24` (W1) and `:89-90` canonical_figures (W3); `src/app/model/page.tsx:141-142` (W1); `src/components/model/visuals/MovingCeilingCurve.tsx:13-14/49/109` (W1+W2); `src/lib/visuals.ts:96/99/101` (W1) |
| 2 | master skills/economics | `agentprivacy-skills/.../agentprivacy-sovereignty-economics/SKILL.md:7/99/105` (W3+W4); `src/lib/skills-data.ts:46` (W3); `.../agentprivacy-story-diffusion/SKILL.md:96` (W4); `docs/skills/persona/agentprivacy-soulbis/SKILL.md:116` (W4, decouple P^1.5 from returns) |
| 3 | `myterms` | `A_privacy_is_value_equation.md:107` (W3); `E_sustainability_model.md:15` (W3) and `:65` (W4) |
| 4 | `dual-agent-harness` | `universe/ERRATA.md:29-32` + `universe/FLEET.md:187` (W1; note ERRATA presents itself as the authoritative correction, so it MUST move with the C82 register row; if the row has not moved yet, add a dated note rather than rewriting the quoted register text) |
| 5 | `agentprivacy-CODEX.md:428/532` | W3+W4 |
| 6 | soulbis website | NO fixes needed (cleanest surface); optional W1 sentence in the ceiling tooltip to name the informational mechanism explicitly |

### 3d. REGISTER-GATED (First-Person approval required per item; prepare diffs only)
- Register row **C82** re-wording (staged in `PHASE2_PHASE6_STAGED_DRAFTS_2026-07-16.md`) and its mirror `agentprivacy_master/src/data/conjecture-register-v6-mirror.json:704` (mirror moves only after the row).
- Register row **C55** character change to soil/rentier + whitepaper §§565-577/1529-1583 + spec §5.5/§10.5/§25/§30 + Tome III Act 9 + Tome IX tide-line driver + grimoire C55 + spellweb nodes (parent checklist B/C/D tables; W4+W5 are the wording base).
- Figure disposition batch: whitepaper:577/1581, v4:219, spec §30 fence, spellweb axiom + legacy graph, master's ~15 versioned grimoire JSON `"economic"` fields, archived grimoire in swordsman-blade/mages-spell (W3; versioned/archived files may be lineage-fenced rather than edited, his call).
- The immutable spellweb inscription `public/data/inscriptions.json:1` ("7th capital compounds"): SUPERSEDE with a new inscription, never patch.
- Canonical grimoire spell `💎(7th capital) → 📈(compounds)` in master AND spellweb: move together so the two canonical homes do not diverge.

## 4. Fences (do not touch; these are false positives)

- **P^1.5 "superlinear"** = privacy-PROTECTION strength axis, not data-value compounding. Keep.
- **C83 "(2^N − 1)ε compounding"** = multi-agent LEAKAGE composition, not value. Keep.
- **Existence-leak "super-additively from correlated systems"** = adversary leakage geometry. Keep.
- **Seventh-capital LABELS** ("behavioural data as the 7th capital") with no compounding/figure claim. Keep.
- **"Sovereignty compounds" / "derivation chains compound logarithmically"** = separation/reputation-adjacent; the second is the closest kin of the surviving reputational-fertility conjecture; flag for the First Person, do not rewrite silently.
- The grant edition's open-hypothesis framing of R(t) drift: already the safest wording. Keep.
- Never introduce "moving ceiling"/City vocabulary INTO tier-A/S pipeline artifacts (GR-4), and never state R < 1 without preconditions + time index in the same passage (GR-7).

## 5. Verification recipe (after edits)

Grep each touched repo, expect ZERO hits outside fenced-lineage/fence-listed contexts:
- `frontier capability|frontier capacity|frontier growth` near `R(t)`/ceiling material
- `678|31,000|31000` asserted as fact (W3 contexts convert them to fenced lineage; the fence text itself may name them)
- `compound` within 3 lines of `capital|data|value` (check against the fence list above)
Then: the two clocks are never merged (no sentence says certificates and corpus growth are the same drift), and every R(t) statement names its clock.

## 6. Standing rules

Nothing committed or pushed without the First Person's explicit ask (LIVE sites /model and soulbis additionally carry a deploy step). Register rows and canon dispositions are his (GR-10). Generated pipeline artifacts are never hand-edited (GR-6): if an item traces to a pipeline extraction, route it to 3b instead of editing output. When done, chronicle what moved.
