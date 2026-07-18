# Plan: update the display & distribution surfaces (master · skills · atlas · cred-spec · guide)

**Date:** 2026-07-16
**Serves:** propagating the July model evolutions (soil ruling L140, R(t) clock narrowing L139, WP-14, public harness) and the DTG Credentials Core Spec into the outward surfaces, and shipping one guide deploy that carries all of it.
**Companion plan:** `SOIL_PROPAGATION_PLAN_2026-07-16.md` — the canon-inward plan. **This plan never executes that plan's register-gated phases; it consumes their outcomes.** Where a lane below touches the same object (C55 wording, R(t) phrasing), the gate is inherited from there.
**Evidence base:** 2026-07-16 four-surface audit (master display drift ×9, skills-v5 diff, guide pipeline map, cred-spec integration map at `~/dtgwg-cred-spec-main_mage/INTEGRATION-MAP.md`).

**What this plan is not:** authority to commit or push. Every lane produces reviewed working-tree edits; commits, pushes, and the wrangler deploy are Mitch's (P4 never marked).

---

## Gates

| Gate | What it is | Blocks |
|---|---|---|
| **G-P1** | First-Person (b)-vs-(c) ruling on WP-07's R(t) (soil plan Phase 1; memo staged) | every R(t)-*erosion/clock* phrasing item: A5, A7, C2 |
| **G-REG** | Phase-3 register disposition of C55 (soil/rentier character-change) + soil conjecture registration (C97+) | exact wording of A1/A2/A8, C1; the new register head in A4/C3 |
| **G-DOCS** | Mitch approval of the routed Gap 1–5 edits (`CRED-SPEC-COHERENCE-NOTES.md`) | Lane D |
| **G-M** | Mitch review → commit/push per repo; wrangler deploy | Lane F ship |

**Not gated (start immediately):** harness publicity (A3), WP-14 listing (A6), VRC re-anchor (A10), skills back-port (Lane B), atlas register-head bump + DTG enrichment (C3/C4), ZKP-TF upstream (Lane E). The *fact* of the soil ruling is adopted (L140), so A1/A2/A8/C1 can be **drafted now against the ruling doc** and finalized to the Phase-3 wording when G-REG opens.

> **EXECUTION STATUS 2026-07-17 (display agent, G-REG wave):** DONE against the ruled rows — master V6 JSON `register_head` C97 + Band XI soil-reading entry; model-downloads blurb → C97; A2 abstract refined to the ruled clauses (rent by position · appropriation share · leased never conveyed · C55/C97); A9 lore docs re-typed; spellweb conj-c55 re-typed to the ruled character, conj-c82 aligned to the re-typed row verbatim-adapted, **conj-c97 MINTED** (+ edges C97→C55, C97→C82), 7th-capital cluster (con-7thcapital, dragon-vertex, seventh-capital-reclaimed, act-tome-iii-9, presets ×2) soil pass, doc node head → C97; harness ERRATA quote moved to the re-typed row (dated note updated). Inscription: STANDS-AS-HISTORY respected — untouched. Register head line in `research/CONJECTURE_REGISTER_V6.md:5` synced C96→C97 (mechanical bookkeeping; Band XI + L150 authority). **BLOCKED once: `scripts/mirror-conjecture-register.mjs` denied by the permission classifier → G-M item for Mitch (one command).** Versioned grimoire JSON economic/proverb fields + canonical grimoire spell 💎→📈 remain First-Person dispositions. tsc clean ×2, JSON valid; second train run same day.
>
> **EXECUTION STATUS 2026-07-16 (display agent):** ungated wave DONE (A3/A6/A10/B1-B3/C3/C4). **G-P1 wave DONE**: A5, A7, C2 + packet §3c corpus rows 1-5 applied (V6 JSON thesis/statement/figures, model page W1 + two-clocks, MovingCeilingCurve W1+W2, visuals.ts, EquationHero ×3 — a residual the packet's worklist missed, found by the §5 grep — sovereignty-economics/story-diffusion/soulbis SKILLs W3+W4, myterms ×3, harness ERRATA dated-note + FLEET W1, CODEX ×2). Register-gated holdouts correctly untouched: C82 mirror row :704, versioned grimoire proverbs/economic fields, inscription. **Mitch chose: apply A1/A2 soil drafts now** (landing "held ground pays rent" + model abstract land/share/erosion-clock; A8 = keep) **+ one train now**. tsc clean master+spellweb; V6 JSON valid. Train running: resync → snapshot → gate → verify; commits + deploy = Mitch.
>
> **GATE STATUS 2026-07-16 (from the soil-plan side, ledger L145): G-P1 is OPEN.** The First Person ruled **branch (c)** and it is executed: WP-07 now proves the erosion clock (Definition 3.9 + Corollary 5.4b; corpus variable **B_t**, erosion ratio **R_inf(t) = Σε_i / H(X | B_t)**; "the protection does not leak more, it matters less"; certification clock and erosion clock separated, never merged). Items A5, A7, C2 are unblocked. **Canonical replacement wording + full corpus worklist + fences: `plans/SOIL_PROPAGATION_EXECUTION_PACKET_2026-07-16.md` (read it before phrasing any R(t) item; W1/W2 are the drop-in strings for A5/A7, and the c82 clock narrowing for C2 must name the calendar/informational clock and cite Cor 5.4b, not compute).** G-REG remains closed.
>
> **GATE STATUS 2026-07-17 (from the soil-plan side, ledger L149): G-REG is OPEN for C82, C55, and the figure disposition.** The First Person ruled: C82 re-word agreed (register row re-typed 2026-07-17, quote it exactly); C55 = land/soil rentier character (register row carries the full ruled wording); the multiples 678x/31,000x are retired as asserted facts suite-wide (fenced lineage only). **The inscription is ruled STANDS-AS-HISTORY: mint nothing, supersede nothing, treat as a pre-ruling historical record.** Finalize A1/A2/A8/A9/C1 against the register rows in `research/CONJECTURE_REGISTER_V6.md`; regenerate the mirror via `scripts/mirror-conjecture-register.mjs` Harness ERRATA/FLEET re-words also released. **UPDATE (L150): the bridge conjecture is MINTED as C97, Band XI (Structural Inalienability by Non-Reconstruction, edges C97 → C55 / C97 → C82); register head is now C97** — use C97 in the C3 atlas head bump and regenerate the mirror; a spellweb `conj-c97` node is in scope for C1's register pass.

---

## Lane A — agentprivacy_master display (`~/agentprivacy_master`)

Ordered by severity from the audit:

| # | File:line | Change | Gate |
|---|---|---|---|
| A1 | `src/app/page.tsx:274` | "The 7th capital compounds." → rentier reading: does **not** compound; value accrues as a **share** (bargaining position), compounding scoped to reputational fertility only | draft now; finalize at G-REG |
| A2 | `src/app/model/page.tsx:102` | "behavioural data as the 7th capital" → Data-as-Soil: land-based rentier capital, value-as-share, R(t) as informational-erosion clock, structural-inalienability = info-sec fusion; cite `research/pvm-v6-soil-and-the-programme-runtime-evolutions.md` | draft now; finalize at G-REG |
| A3 | `src/app/guide/the-dual-agent-harness/page.tsx:405-414, 277-301, 462-479` | Replace "being prepared for sharing" with live repo link (github.com/mitchuski/agentprivacy-harness) + workshop console; add runtime 01 (nullifier) and runtime 07 (trust-graph-formation) with their cred-spec anchors | none |
| A4 | `src/data/privacy-value-model-v6.json:22-73` + `src/data/conjecture-register-v6-mirror.json` | Add soil conjecture, advance `register_head` past C96 — **regenerate via `scripts/mirror-conjecture-register.mjs`**, never hand-edit the mirror | G-REG |
| A5 | `src/app/model/page.tsx:152` + `src/data/privacy-value-model-v6.json:12` | Reconcile "amnesia is the only term whose security is independent of t" with the WEIS overclaim removal; narrow R(t) language to the informational-capability clock | **G-P1** |
| A6 | `src/lib/model-downloads.ts:67-115` | Add WP-14 (WEIS 2027, seventh capital) to the papers list; fix hard-coded "register to C96" blurb | none (blurb final at G-REG) |
| A7 | `src/components/model/visuals/MovingCeilingCurve.tsx:11-16,118` | Annotate R(t) as informational-capability clock; optional soil erosion-clock reading | **G-P1** |
| A8 | `src/app/page.tsx:708` | "Take back the 7th Capital" hero → align with rentier framing | draft now; finalize at G-REG |
| A9 | `docs/CITYOFMAGES_README.md:435`, `docs/ALL_THE_TOMES_LIST.md:102` | C55 lore descriptions → soil ruling (low priority) | G-REG |
| A10 | `src/app/model/page.tsx:255` | Re-anchor "delegation = signed relational edge (the VRC)" from KAPPA_HOLON to the DTG Credentials Core Spec; name the pairwise construction | none |
| A11 | `docs/chronicles/2026-07-16_trust-graph-formation-dream-cycle.md` | Untracked chronicle — include in the commit set | G-M |

## Lane B — skills (`~/agentprivacy_master/agentprivacy-skills/agentprivacy-skills-v5` — the nested copy; the wiki builder hard-codes this path)

| # | Change |
|---|---|
| B1 | Back-port `~/.claude/skills/agentprivacy-wiki-sync` → `wikis/agentprivacy-wiki-sync/` (the one missing skill; write/publish twin of agentprivacy-wiki-watch). Register in `.claude-plugin/plugin.json` if the manifest enumerates |
| B2 | `privacy-layer/agentprivacy-vrc-identity/SKILL.md` — update ToIP section + open problem #5 with the DTG spec's two ZK constructions + PHC/IDVC split; same pass on `persona/agentprivacy-ambassador/SKILL.md` |
| B3 | Housekeeping: remove `agentprivacy-uor-toroidal/SKILL.md.bak-2026-07-10`; commit the untracked `wikis/agentprivacy-wiki-watch/` |
| B4 | **Candidates only, not this cycle:** carve workshop-console, lexon, and V6 research-loop skills out of the skill bodies they're buried in — register as a follow-up quest |
| B5 | Do NOT touch stale `~/agentprivacy-skills` (superseded shell); optionally add a SUPERSEDED marker |

## Lane C — spellweb → atlas (`~/spellweb`)

| # | Change | Gate |
|---|---|---|
| C1 | `src/data/nodes.ts:1654` (conj-c55) + `:1756` (act-tome-iii-9) + `con-7thcapital:247` + `con-dragon-vertex:443` + `seventh-capital-reclaimed` + `presets.ts:76,231,412` — soil/rentier free-text specialisation. **nodes.ts:1654/1756 are soil-plan Phase-3 surfaces (register-gated): stage as proposal diffs, First Person disposes** | G-REG |
| C2 | c82 node — add the clock narrowing (informational-capability erosion, calendar-adversary) | **G-P1** |
| C3 | `privacy-value-model-v6` document node — "Register head C93" → current head (C96 now; C97+ after registration) | none now; re-bump at G-REG |
| C4 | DTG node/page enrichment — cite the DTG Credentials Core Spec, name pairwise + community-anchored ZK constructions (page already has the six types + thin-credential-fat-registry) | none |
| C5 | Optional: mint VMC/VTC/PHC/IDVC concept nodes + tag `con-vrc`/`proto-vrc`/`con-three-layer-identity`/`skill-trust-graph-formation` with cred-spec anchors | none |
| C6 | `chronicles/DREAM-2026-07-16.md` — untracked; include in commit set | G-M |

## Lane D — agentprivacy-docs gaps (gated: G-DOCS; respect papers/ read-only + frozen origin)

**Ownership note (2026-07-16):** a separate agent session is building on the agentprivacy-docs work to make the research executable. **Lane D routes to that agent** — this plan's executor does not edit agentprivacy-docs content (this plans/ file and INDEX row excepted) and coordinates through `CRED-SPEC-COHERENCE-NOTES.md`. Avoid concurrent edits to the same files.

| # | Change |
|---|---|
| D1 | `research/privacymage-response-fpp-zkp-progress.md` — Gaps 3/4/5 (R/M/C/P-DID order + expansion at L103; First-Person→PHC + IDVC pointer at L23/L27; VTA/VTC/VTN expansion). Non-canon, directly editable on approval |
| D2 | Gap 1 — fix E7 input source (hearthold-build README / tome-x) so E7-C26 defines VMC/VIC/VPC/VEC/VWC; rebuild extraction via pipeline. Never hand-edit `extractions/E7-identity-vrc.md` |
| D3 | Gap 2 — one-line "same acronym; agentprivacy extends with promise-theoretic economics (O9)" note in `specs/vrc_promise_protocol_v3_3.md` + whitepaper (whitepaper = canon → route via register) |
| D4 | Gap 4 — `reference/GLOSSARY_MASTER_v4_0.md` PHC/IDVC split (glossary via pipeline) |

## Lane E — ZKP-TF / cred-spec (`~/dtgwg-zkp-tf-mage`, `~/dtgwg-cred-spec-main_mage`)

| # | Change |
|---|---|
| E1 | Commit the pending 2-line README coherence edit (VTA capitalization + cred-spec normative link) — the only tracked dirty file; the only thing that goes upstream this cycle (G-M) |
| E2 | Open E1–E7 strawman edits as upstream PR/issues from `STRAWMAN-COHERENCE-EDITS.md` (TF process) |
| E3 | Build track: circom port of runtime 01 (Poseidon nullifier + Merkle membership) = O2 + O4 primitive; then VWC witness seat |
| E4 | `~/dtgwg-cred-spec-main_mage` = working root; keep `INTEGRATION-MAP.md` updated as lanes land |

## Lane F — the deploy train (after A, B, C and any approved D land)

```
cd ~/.wiki/skill-fedwiki
node resync.js                       # full federation: skill, guide, research, atlas, tomes, grimoire, harness, library
cd ~/agentprivacy.guide
node tools/snapshot.mjs              # ~/.wiki → site/
node tools/gate.mjs                  # MANDATORY post-snapshot
node flow/run.mjs verify             # must PASS
node flow/sync-manifest.mjs
# G-M: git commit/push or npx wrangler deploy  (Mitch)
```

Notes:
- This train also carries the **already-stranded** Jul-13 skill-site rebuild (232 modified files uncommitted in agentprivacy.guide) and master's Jul-14 conjecture-mirror commit that never reached `/research/`.
- `harness.localhost` is IN the public snapshot — harness page edits go public with this deploy.
- Verify live spot-checks after deploy: `/` hero (no "compounds"), `/model` (soil + clock), `/guide/the-dual-agent-harness` (repo link), `/skill/agentprivacy-wiki-sync` (new page), `/atlas` C55 + register head, gates still open.

---

## Execution order

1. **Now (ungated):** A3, A6, A10, A11 · B1–B3 · C3, C4 (+C5 if wanted) · E1 staged, E4. Draft A1/A2/A8 + C1 as proposals against the ruling doc.
2. **On G-REG (Phase-3 disposition):** finalize A1/A2/A8/A9, run A4 mirror regen, apply C1 disposition, re-bump C3.
3. **On G-P1 ((b)-vs-(c) ruling):** A5, A7, C2 in the ruled wording.
4. **On G-DOCS:** D1–D4 via their stated routes.
5. **Lane F once the wave above is in the working trees; ship at G-M.** If G-P1/G-REG lag, Lane F can ship a first train with the ungated wave (harness publicity + skills + WP-14 + cred-spec anchors) and a second train after the rulings — Mitch's call on one train vs two.

## Standing rules

- Pipeline artifacts: fix inputs and rebuild, never hand-patch generated output (E7, conjecture mirror, wiki pages).
- Canon dispositions are First-Person/register (GR-10); this plan stages diffs, it does not rule.
- Nothing committed or pushed by roles; the deploy is Mitch's.
- On execution, chronicle per repo (PLAN → EXECUTION → CHRONICLE).
