# Release Plan · Private Repo + Gated Rollout

**Date:** 2026-07-12
**Owner:** the First Person (mitchell@soulbis.com)
**Driver:** gated, review-per-unit; nothing lands without your approval on that unit
**Repo:** `agentprivacy-docs` (living documentation) — last public commit `330a636`, 2026-06-12

---

## Why this plan exists

A month of work sits uncommitted (63 tracked changes + the entire
`papers/Programme/` apparatus, which has never been in git). The current
`origin` is **public** (`github.com/mitchuski/agentprivacy-docs`). We are
**not** publishing a month of pre-eprint drafts, unreviewed canon
corrections, and the whole research apparatus to the world in one push.

Instead:

- **Horizon 1 (now):** preserve everything to a **new private remote**,
  committed as a reviewed chain — you approve each unit before it lands.
- **Horizon 2 (later):** release specific artifacts (blogs, papers,
  canon mirrors) to the **public** repo, each behind its own gate.

The public `origin` stays **frozen at `330a636`** until Horizon 2.

---

## Protection posture (the invariants)

1. Public `origin` receives nothing until a Horizon-2 gate says so.
2. The private remote is the backup + review surface for the full month.
3. Per-artifact fences carried in from the runtime, unchanged:
   - **Canon diff review (L127):** the additivity batch awaits your
     sign-off; committing it to *private* preserves it but does **not**
     close the public-rollout / mirror-regen gate.
   - **Eprint fence:** WP-04 / WP-07 / WP-27 drafts are pre-eprint;
     public release waits on the P4 read + venue/eprint decision.
   - **Pool-post staging:** post-1 method-only after the letter is sent
     + kit repo public; posts 2+ later; never private ledgers / kill
     catalog / TIG strategy.
   - **GR-6:** generated mirrors (PDFs, tex, readers, tracker) regenerate
     from source *after* the canon review, never hand-carried ahead of it.
   - **C-series minting** stays yours; the runtime mints only CTR-series.
4. No secrets in the tree (filename scan clean); re-scan before any push.

---

## Setup (one-time)

**S1 — you create the private repo** (needs your GitHub auth; `gh` is not
installed here). On github.com → New repository:
   - Name suggestion: `agentprivacy-programme` or `agentprivacy-docs-private`
   - **Private**, do **not** initialize (no README/.gitignore/licence)
   - Copy the URL.

**S2 — I wire it** (does not publish anything):
   ```
   git remote add private <URL>
   ```
   `origin` is left untouched. All Horizon-1 pushes target `private`.

**S3 — push cadence:** after each approved gate I commit locally, then
`git push private main` so the private remote mirrors your review progress.
(Alternatively batch-push at the end — your call.)

---

## Horizon 1 · the gated commit chain (private)

Each gate is one reviewable commit. For each I will: (a) show the file
list + an honest summary + any fence notes; (b) point you at the reader
(`localhost:7474`) or `git diff` for the actual content; (c) commit only
on your approval; (d) push to `private`.

| Gate | Commit | Contents | Your review focus | Fence |
|---|---|---|---|---|
| **G0** | Hygiene | `.gitignore` — session scratch (`prov*.txt`) + the generated `**/reader/` and `**/tracker/` dirs (~8.4M, GR-6) | quick: confirm we version builders, not generated HTML | — |
| **G1** | Living documentation: V6 limitative reading + visual runtime | the 2026-06-28 run-8 limitative distribution, gate G6, visual-runtime instruments, DREAM chronicles (06-29, 07-01), the limitative plans, the moving-ceiling instrument + circuit-workshop research notes, UOR-atlas notes, reading-ledger / autopath / reflection-map updates | is this the late-June/July research thread as you remember it | — |
| **G2** | Canon corrections: L044 decomposition + CTR-OBS-01 subadditivity | `papers/v6/*.md` (4), `papers/v5/…v5_4…md` (2-line provenance flag only), `research/CONJECTURE_REGISTER_V6.md`, whitepaper v6.3, compendium honest-limits + assembled, `reference/PAPERS_INDEX.md`, `archive/canon-backups-{07-02,07-03,07-10}/` | **THE diff review.** This is L127. Walk the before/after per site; the v5.4 body is untouched (flag only); the deficit iff is fenced; the floor is conservative | committing to private ≠ closing the public gate; approving the *content* here lets the runtime proceed to mirror regen (cycle 15) |
| **G3** | The Fable auto-research runtime + Papers Programme pipeline | `papers/Programme/pipeline/` (apparatus, 14 cycles, rehydrations, extractions, reviews, ledger, tracker/reader builders, consolidation brief) + `papers/Programme/observers/` + `archive/pipeline-v2-snapshot-2026-07-02/` | the apparatus as a whole; confirm the pre-eprint drafts are fine to hold in *private* | pre-eprint drafts live here — private only |
| **G4** | The overlay lane: the Loomkeeper's weave | `papers/Programme/overlays/` — persona, 3 skills, 4 sweeps, WEAVE, 9 keys, the poem set | the weave + the nine keys + "The Second Argument"; the Loomkeeper stays a draft persona | — |
| **G5** | Regenerated build mirrors (pre-review) | `build/tex/v6/*`, `pdfs/**`, `models/*.json` | these are pre-canon-review builds; confirm you want them preserved as-is (they regenerate after G2's review) | GR-6: superseded by post-review regen |
| **G6** | Lexon PVM research chronicles | `chronicles/2026-07-11_lexon*`, `2026-07-12_lexon*` | the lexon-harness thread's landing in the docs record | — |
| **G7** | Presentation: README + Documentation Chronicle | refreshed `README.md` + `DOCUMENTATION_CHRONICLE.md` presenting the V6 programme, the runtime, the auto-research loops, the overlay lane, the local reader surfaces | is this how you want the repo to open for a reader | this is the "presentation time" face |

Order is narrative (oldest work first, presentation last). Any gate can be
split, reordered, or held. G2 is the heavy one and the one that doubles as
your standing canon diff review.

---

## Horizon 2 · public release (later, separate session-gates)

Each of these is its own decision, **after** Horizon 1 is banked private.
None fires automatically.

- **R1 — Canon to public:** once G2's content is approved, regenerate the
  mirrors (GR-6) and release the corrected V6 suite to public `origin`.
  Unblocks the runtime's cycle 15 (mirror regen + propagation ring, L127
  closes).
- **R2 — The blogs:** WP-01 *Moving Ceiling* + the gathering arc + the
  pool post-1 — release order and timing yours; pool posts 2+ stay
  door-blocked (letter sent + kit repo public).
- **R3 — The research papers:** WP-04 / WP-07 / WP-27 — each after its P4
  read + venue/eprint decision. Preprint posting is a publication act;
  decide venue-by-venue.
- **R4 — Sibling repos (their own remotes/pins):** spellweb nodes/edges
  (overlay weave, uncommitted), cityofmages grimoire v1.9.2 merge + IPFS
  re-pin + Tome IX Act 7 bind — each on its own rollout, not this repo's.

---

## Standing decisions still at your door (feed the gates)

- Private repo name (S1).
- The Loomkeeper's admission (bind as cast / hold as draft) — affects R4.
- The four UNCAST paper seeds from the weave (adopt / dismiss).
- Push cadence: per-gate or batch (S3).

---

## Progress tracker

- [ ] S1 private repo created · [ ] S2 remote wired · [ ] S3 cadence chosen
- [ ] G0 hygiene · [ ] G1 living-docs · [ ] G2 canon (diff review) ·
      [ ] G3 pipeline · [ ] G4 overlays · [ ] G5 mirrors · [ ] G6 lexon ·
      [ ] G7 presentation
- [ ] Horizon 1 pushed to private
- [ ] R1 canon public · [ ] R2 blogs · [ ] R3 papers · [ ] R4 siblings
