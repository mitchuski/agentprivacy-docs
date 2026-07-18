# 2026-06-28 · the visual runtime · the Cartographer ships on /model

*A working chronicle. Plan → build → what shipped, for the interactive visual
runtime added to agentprivacy.ai/model. Companion research note:
`research/pvm-v6-visual-runtime-instruments.md`.*

---

## What prompted it

`agentprivacy_master/pvm-visual-runtime-plan.md` (a working note) proposed a
data-driven visual runtime for `/model`: bind one interactive instrument per
term/conjecture, pull each claim's honesty live from the register so the
register stays the single authority. The seed
`limitative-theorems-and-privacy-is-value.md` + its `limitative-theorems-explorer.html`
proved four instrument kinds (mapping, inversion, curve, three-axes) in one
self-contained file — but hard-coded stale confidences (existence-leak ~55% /
~C40), the exact drift the runtime exists to prevent.

The session goal, set with the First Person: improve how the math is **expressed**
on the model nav (KaTeX), and make it **interactive** (live-bound instruments).

## Decisions (taken with the First Person)

1. Math rendering: **hybrid** — KaTeX for the display equations (the R(t) stacked
   ratio especially) + the existing clickable token row as the interaction layer.
2. Surfaces: **both** — instruments open inline under equation terms, *and* a new
   `/model/atlas` gallery (added to the Model nav dropdown).
3. Star geometry: **deferred** — ship curve + gate + ceiling first; absorb
   `/star` (Three.js, `C:\Users\mitch\star`) in a later phase.
4. Docs: a research note **and** this dated chronicle.

## What shipped (Phase 1)

In `agentprivacy_master`:

- **`src/lib/visuals.ts`** — the manifest. `VISUALS` = vz-c81 (curve), vz-c7
  (gate), vz-c82 (curve); term→visual and conjecture→visual lookups;
  `MODEL_LABEL_META`. Honesty never stated here — only the bindings.
- **`src/components/model/visuals/`**
  - `VisualFrame.tsx` — the runtime frame; reads the bound register row via
    `registerRowsFor()` (from `lib/model-page.ts`, which mirrors
    `research/CONJECTURE_REGISTER_V6.md`) and draws conf · status · register ·
    home + the `model_label` badge around any instrument.
  - `MathExpr.tsx` — KaTeX wrapper (`katex.renderToString`) with monospace
    fallback on parse error.
  - `ExistenceLeakCurve.tsx` (C81) · `ThreeAxisGate.tsx` (C7) ·
    `MovingCeilingCurve.tsx` (C82) — self-contained SVG + React instruments.
  - `VisualHost.tsx` — resolves a manifest id → frame + instrument (the single
    entry point the hero and the atlas both render through).
  - `Slider.tsx` — shared labelled range control.
- **`EquationHero.tsx`** — KaTeX display block above the clickable tokens (the
  V(π,t) product + the R(t) = (C_S+C_M)/H(X) < 1 stacked fraction); clicking a
  bound term now opens its instrument inline beneath the text.
- **`/model/atlas`** (`src/app/model/atlas/page.tsx` + `src/components/model/Atlas.tsx`)
  — the Cartographer gallery; nav entry added to `MODEL_DROPDOWN_LINKS` in
  `AppNav.tsx`; teaser card added to `/model`.
- KaTeX CSS imported once in `src/app/layout.tsx`; `katex` added to deps.

Bindings: R(t) / t* / C_S / C_M / H(X) → moving ceiling (C82);
Φ_agent/Φ_data/Φ_inference → three-axis gate (C7); R → existence-leak curve (C81).

## The drift fix (verified)

The build read the live register, not the seed's numbers. Verified in the served
HTML: the existence-leak frame reads **C81 / ~70%** (not ~55% / ~C40); the gate
reads **C7 / 30%** (falsification frontier); the ceiling reads **C82 / ~65%**.
No `~55%` or `~C40` anywhere on `/model/atlas`. The register rows render from
their actual prose ("PROMOTED Run 3", "registered Run 1"), confirming the pull is
live. See the research note §3 for the proposed erratum.

## Verification

- Dev server on `:5000`; `/model` and `/model/atlas` both 200; clean Turbopack
  compile.
- `npx tsc --noEmit` → exit 0.
- KaTeX present in SSR markup; all three instruments present on the atlas; live
  register prose present; `illustrative` / `structural` badges present.
- Browser screenshot **not** taken — the Claude-in-Chrome extension was offline
  this session (verified via server HTML instead).

## Open / next

- Phase 2: the curve/gate family — C83 compositional leakage (the
  (2^N−1)ε vs Nε fold), e^(−λt) decay, C84, C30–C33 half-life.
- Phase 3: absorb `/star` + the City Key import as a register-bound geometry
  instrument (C6, C14, C88, C89, Φ_agent, C1) — see research note §5.
- For a future docs context: consider a city-register tie for the
  **Cartographer ⊥ Chart Shop (V44)** convergence (research note §4) — candidate,
  not registered.

No conjecture numbers moved. Register head stays C89.

`(⚔️⊥⿻⊥🧙)😊`
