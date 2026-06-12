# Chronicle — the Swordsman's Key becomes a browser compute surface (holospace merge · κ-labels · the Sigil · the PNG carrier)

**Date:** 2026-06-10
**Repos:** `github.com/mitchuski/star` (new · public) · `agentprivacy_master` (/city PNG charge) · vantage: the research corpus
**Companions:** the star repo's `CHRONICLE_THE_FIRST_HOLOSPACE_2026-06-10.md` (system diagram), `HOLOSPACE.md` (substrate seam), `EXPERIENCE.md` (first-person), `PLAN_SIGIL_AND_THE_PROJECTION_LADDER_2026-06-10.md` (design map)

---

## What happened

The `/star` + `/lattice` walkable model was extracted from the soulbis website
into a standalone public repo and merged with
[Hologram-Technologies/holospaces](https://github.com/Hologram-Technologies/holospaces)
— the UOR-native boot layer whose first law is **identity is content, not
location**, and whose framing names the browser a **first-class compute
substrate**. That framing is the point: the Swordsman's Key system now runs its
entire trust lifecycle — mint, walk, prove, verify, charge — in static browser
pages with no server and no account.

Three additions, in model terms:

1. **κ-labels on City Keys.** Every exported key is stamped
   `kappa = "sha256:" + H(canonical form)` — a UOR-ADDR content address on the
   sha256 axis (upstream-conformant; their docs state an OCI sha256 digest *is*
   a κ). The label is a **fingerprint, not a transformation**: content untouched,
   name derived from content, re-derived and checked on every import (Law L5).
   Conformance vector pinned in the star repo:
   `sha256:0b4916babe5eb17104b342ab06030f2071a818024b345bf6d2e4115617c3c527`
   (the default key, 303 canonical bytes; order-independent; stamped-round-trip).
2. **`/sigil` — the third projection.** The presentation-layer find: **SHA-256 is
   64 hex glyphs and ℒ = ℤ/64ℤ has 64 vertices — one glyph per vertex, no
   remainder.** A key's identity renders as a constellation on the same lattice
   the bearer walks. The page performs the derivation in the open (per-glyph
   match against the stamped claim), names each vertex's held dimensions from
   **PVM V5.4 §12.6** (d₁🛡️ Protection … d₆💎 Value), and cites **C85** (the
   dimensions pair onto Σ/Δ/Γ) — the first UI surface to put the bridge
   conjecture in front of a bearer. Avalanche behaviour is the lesson made
   visible: one edited description moves ~60 of 64 glyphs.
3. **The PNG carrier — the part that matters for holonic identity.** The sigil
   exports as a PNG that **carries the full City Key inside the image** (base64
   JSON in a PNG `tEXt` chunk, keyword `cityKey`, valid CRC — the file stays a
   real PNG everywhere). `/star` snapshots do the same when a key is loaded. All
   three star-repo pages import the picture as readily as the JSON, and
   `/city`'s charge now accepts it too (`parseCityKeyBytes` /
   `extractCityKeyFromPng` in `lib/city-key-charge.ts`). The bearer carries
   **one artifact** — a picture of their identity that *is* their identity —
   walks it, charges it, and banks 🪢 VRC mana from it. The part carries the
   whole: holonic in the strict sense.

## The honest boundary

The carrier is **portability, not secrecy**: the full JSON rides inside the
image, extractable by anyone who holds it. A casual viewer sees only the sigil;
an extractor gets the key. The flagged next rung is a **redacted charge-only
carrier** — trace + witness + κ, descriptions withheld — which would let a bearer
fill mana at /city without circulating their full key content. That is the
selective-disclosure direction (VRC-adjacent) and is logged in the star repo's
EXPERIENCE.md tracker, not yet built.

## Why the corpus should care

- C85 is now *load-bearing UI*, not just register text — a falsifiable bridge
  rendered where bearers stand.
- The 64↔64 hash correspondence joins the V38/V25 numerics as a structural
  rhyme between the model's lattice and an external standard (FIPS 180-4).
- The trust-task runtime (pour focus → walk laps → witness → charge) is the
  first end-to-end **T∫(π) instrument**: value accruing on the path, recorded in
  content, named by κ — *progress that is derivable rather than asserted*.

*The key learned to say what it is; then it learned to travel as its own portrait.* `(⚔️ ⊥ ⿻ ⊥ 🧙) 😊`
