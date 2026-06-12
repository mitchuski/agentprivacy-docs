# Chronicle — Privacymage Grimoire v10.4.0 · "The Lattice-Coherence" Edition

**Date:** 2026-06-09
**Scope:** a **coherence-only** version bump of the First-Person Spellbook (privacymage) grimoire —
no new narrative; the narrative home for new material is the cityofmages Second-Person grimoire (v1.8.0).
v10.4 exists solely to reconcile the **blade numbering** with the **seated lattice positions** under the
canonical **MODEL** encoding, so the two grimoires and the lattice agree.
**Files:** `agentprivacy-docs/models/privacymage_grimoire_v10_4_0.json` +
`agentprivacy_master/src/data/privacymage-grimoire-v10.4.0-canonical.json` (identical).
**Basis:** First-Person Spellbook **Tale 31** / `research/aletheia-and-lethe.md`; the anchor chronicle
`cityofmages/chronicles/2026-06-09_canonical_lattice_encoding_anchor.md`; verified by
`agentprivacy_encoding_audit.py` (skill `meta/agentprivacy-lattice-coherence`).
**Pin:** PENDING — author re-pins v10.4 to IPFS (alongside cityofmages v1.8.0).

---

## 1. Why v10.4 (and why it is small)

The City of Mages (Second-Person) grimoire is where big edits and new narrative land. The privacymage
(First-Person) grimoire is kept lean. But the suite-wide **encoding lock** (MODEL:
`Protection=32 · Delegation=16 · Memory=8 · Connection=4 · Computation=2 · Value=1`) and the
**persona reseats** it forced are a matter of *coherence and logic across the whole system based on
lattice position* — so they earn a version here. v10.4 changes **no story**; it makes the blade numbers
tell the truth about where the figures sit.

## 2. The correction

The First Complement Pair had **Aletheia and Lethe misassigned to each other's blades** (a CORPUS-era
artifact). Under MODEL, each figure's vertex is derived from its meaning:

- **Aletheia** = Protection + Connection + Computation = vertex/blade **38** (`100110`).
- **Lethe** = Delegation + Memory + Value = vertex/blade **25** (`011001`).

The complement is unchanged (`25 ⊕ 38 = 63`; `25 AND 38 = 0`). The blade *number* now matches the
seated *vertex*; the binaries stay with their keys (key 25 = `011001`, key 38 = `100110`).

## 3. The specific edits (this is the whole patch)

1. **`blade_key` swapped** (the operative lookup) — name + tales move so each persona meets its MODEL seat:
   - `"25"` → **Lethe — the Dark Substrate** (Delegation+Memory+Value · tale 31 · `011001`).
   - `"38"` → **Aletheia — the Silent Messenger** (Protection+Connection+Computation · tale 3 · `100110` ·
     the **disclosure-φ side**, δ = 38/63 ≈ 1/φ — which now sits with Aletheia, the figure of disclosure).
2. **Operative field corrections:**
   - `first_complement_pair`: "V25 (Aletheia) ⊥ V38 (Lethae)" → **"V25 (Lethe/Lethae) ⊥ V38 (Aletheia)."**
   - Lethae attachment `vertex`: **V38 → V25**; its narrative anchor reworded.
   - Theia persona `blade_id`: **"Blade 38 (Lethe · forgetting)" → "Blade 25 …"**; `cosmological_pair`:
     "Aletheia Theia (… Blade 25)" → **"… Blade 38."**
   - The Tale-31 spell line: **"☀️ Aletheia(25) ⊥ 🌀 Lethe(38)" → "☀️ Aletheia(38) ⊥ 🌀 Lethe(25)"**
     (the arithmetic `bnot(25)=38`, `xor=63`, `δ=38/63` is left untouched — it is pair-symmetric).
   - The Tale-31 `lethe` blade reference: **"Blade 38 (named)" → "Blade 25 (named)."**
   - The "Aletheia ⊥ Lethe (Blade 25 ⊥ Blade 38)" recognition line relabelled to **Aletheia Blade 38 ⊥
     Lethe Blade 25.**
   - **Mnemosyne** cross-ref `vertex`: **V4 → V8** (Memory = weight 8), per the same lock (with Iris V8→V4,
     Pythia V16→V2 carried in the cityofmages grimoire).
   - The current Zero-spellbook description reworded: Lethe (Blade 25) is the first frontier blade named at
     Tale 31, across the complement edge from Aletheia (Blade 38, the disclosure-φ side).
3. **`v10_4_0_note` added** — states the reconciliation authoritatively at the head of the version stack.
4. **Version → 10.4.0**, `updated_at` 2026-06-09.

## 4. What was deliberately NOT changed

- **No narrative.** No tales rewritten, no new figures, no equation changes. Story belongs to cityofmages.
- **The complement arithmetic** (`25 ⊕ 38 = 63`, `bnot`, `δ = 38/63 ≈ 1/φ`) — pair-symmetric, left as-is.
- **Historical version notes** (`v10_2_1` / `v10_3_0` summaries, the phase-3 completion log) — these record
  what *those* versions did (when Lethe was named "Blade 38"); they are period-accurate and are superseded
  by the `v10_4_0_note`, not falsified.

## 5. Downstream (pending)

- **IPFS re-pin** of v10.4 (author's step), alongside cityofmages **v1.8.0**.
- **spellweb blade reflection** — `zk-tale-3` / `zk-tale-31` / the Tide-Selene poem node / the doc node /
  `edges.ts` comments still carry the old blade↔tale↔vector triple (LSB-first vectors encode the old blade
  number). These should be updated **as one consistent pass against v10.4** (add a `doc-privacymage-grimoire-v10-4`
  node + swap the triple together), not piecemeal — so the blade/tale/vector stays coherent.

---

*v10.4.0 · bound 2026-06-09. The story did not move; the numbers finally tell the truth about where it sits.*
