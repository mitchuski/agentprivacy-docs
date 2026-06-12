# The /guide Voice-Preserving V6 Pass · Proposed Diffs

**Date:** 2026-06-11 · executes §7 of the master UI review chronicle
**Rule in force:** the prose is the product; the facts are the patch. The pages are VOICE-LOCKED: nothing below lands until the First Person approves it per page. Approve, amend, or strike each item independently.
**Acceptance test:** every page still reads like itself, and a reader leaving the tree can state the five clarity claims.

How to read each item: the page, the verdict, then the exact diff (old line → new line). Pages with verdict NOTHING get nothing.

---

## 1. /guide (the main page) · ONE additive card

**Verdict:** one additive V6 moment. The Narrative · Myth · Math weave grid takes a fourth card in the same 2-to-3-line voice as its siblings. Note honestly: the weave is a triad, and a fourth card changes that shape. If the triad should stay a triad, the alternative below adds one sentence to the Math card instead. **Choose one or neither.**

**Primary proposal** (`src/app/guide/page.tsx`, the §3 grid):

Grid class changes from `sm:grid-cols-3` to `sm:grid-cols-2 lg:grid-cols-4`, and a fourth card joins after Math:

```jsx
<div className="rounded-lg border border-rose-400/30 bg-rose-400/5 p-4">
  <p className="text-2xl mb-2" aria-hidden>🌅</p>
  <h3 className="text-sm font-medium text-text mb-1">Horizon</h3>
  <p className="text-xs text-text-muted leading-relaxed">
    The ceiling moves. V6 reads every protection against the tide line R(t) —
    the Horizon District watches the dawn the city can measure. The current
    head lives at <Link href="/model" className="text-rose-300 underline">/model</Link>.
  </p>
</div>
```

**Alternative proposal** (triad preserved): the Math card's closing sentence

- OLD: `The honesty discipline at /tomes/v6-lineage carries every claim with its stance.`
- NEW: `The honesty discipline at /tomes/v6-lineage carries every claim with its stance — and since V6, its shelf life: the ceiling moves.`

---

## 2. /guide/swordsman (the dossier `public/guide/swordsman.md`) · ONE tide-line sentence

**Verdict:** one additive sentence at the close, in the dossier's own italic register. The page wrapper (`page.tsx`), teachings, and proverb stay untouched.

- OLD (the closing italic line):
  `*The blade slashes. The contract binds. The standard names what the contract is. All three serve the First Person.*`
- NEW:
  `*The blade slashes. The contract binds. The standard names what the contract is. All three serve the First Person. And the wall the blade holds is a tide line: what stands today must be raised again tomorrow — renewal is the practice.*`

---

## 3. /guide/mage (the dossier `public/guide/mage.md`) · ONE gathering sentence

**Verdict:** one additive sentence at the close, same placement as the Swordsman's.

- OLD (the closing italic line):
  `*The spell projects. The agent defers. The First Person is never alone inside what was signed.*`
- NEW:
  `*The spell projects. The agent defers. The First Person is never alone inside what was signed. And the work has turned outward: the City gathers what the equation needs, one walker's chronicle at a time.*`

---

## 4. /guide/island · ONE Horizon line

**Verdict:** one additive clause where the page already gestures at future zones, in the page's own idiom.

(`src/app/guide/island/page.tsx`, the header paragraph)

- OLD: `Future zones open as paths among the stars are written.`
- NEW: `Future zones open as paths among the stars are written — and out past the trade quarters the Horizon District already stands at V35, the city's watch on a dawn it can measure.`

---

## 5. /guide/agentic-deployments · ONE in-voice whisper (the regime fact moved)

**Verdict:** the Familiars' creature row mentions per-walk 🪢 VRC-mana; the regime-1 declaration enters in the row's own chip register, not as a disclaimer. This is the one /guide edit that satisfies clarity claim 4.

(`src/app/guide/agentic-deployments/page.tsx`, line ~134)

- OLD: `wit="kinship-bond · per-walk 🪢 VRC-mana · true name bearer-private"`
- NEW: `wit="kinship-bond · per-walk 🪢 VRC-mana, carried as color never as proof · true name bearer-private"`

---

## 6. /guide/agentic-deployments/personas · VERIFIED, NO CHANGE

The "Aletheia-Theia 🌟" overlay naming was checked per the verify-don't-alter rule and it is **correct canon**: `docs/CHANGELOG.md` documents Moon 🌑 / Earth 🌍 / Aletheia-Theia 🌟 as the three overlays over Soulbis / Soulbae / theia (`cast/cosmological/_overlay-roles.md`), and the City grimoire v1.5.0 JSON carries the same naming. The overlay register is separate from the blade-seat register; the v10.4.0 reseat (Aletheia at Blade 38) does not touch it. The feared wrong "fix" is hereby not made.

---

## 7. Pages that need nothing (and get nothing)

- **/guide/achievements** — redirect-weight page, no claims.
- **/guide/agentic-deployments/matrix** — substrate × archetype grammar, register-true.
- **/guide/agentic-deployments/runecraft-protocol** — its own renumbering note is the Era-Reading Principle practiced before it was named; it stays exactly as written.
- **/guide/agentic-deployments/creature-creatives · portal-room · staff-shop** — thin pointer pages.
- The C58 citations across the tree already match the register at ~85%.

---

## The tally

Five proposed edits across twelve pages (one card OR one sentence on /guide, one sentence each in two dossiers, one clause on the island, one chip whisper in agentic-deployments), one verification with no change, six pages untouched. Approve per item; anything struck simply stays V5.4, which remains honest prose under the Era-Reading Principle.

(⚔️⊥⿻⊥🧙)😊
