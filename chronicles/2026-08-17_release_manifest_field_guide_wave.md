# 2026-08-17 · RELEASE MANIFEST — The Field Guide Convergence Wave

**Status:** the single cross-repo handoff for the field_guide_privacymage convergence
(2026-08-13 → 17: two field days on the Mac + the merge home). Work from this file alone to
commit and push. Precedent: the 2026-05-28 City Key release manifest. Companion narrative:
`agentprivacy_master/docs/chronicles/2026-08-17_field_guide_convergence.md` (master, unsigned).

**Wave version:** `convergence-2026-08-17` · guide federation **14 hosts / 13 sister sites**
(fieldguide seated) · dtg KB at **X11** · spellweb graph **+9 nodes / +17 edges** (atlas 811).

**Verification (run on THIS machine, 2026-08-17):** `field_guide_privacymage/runtimes/`
`node verify.mjs` → **ALL GREEN — 8 suites, 124 properties** (meet-overlay 54/54 · fixtures
8/8 · consumer-py 15/15 byte-exact · lab-bridge 10/10 against `~/dtgwg-cred-spec-main_mage` ·
acceptance 13/13 · open-questions 13/13 · questions 5/5 · reflection 6/6), `vectors.json`
sha256 `8a2637fb…5e062dd` — **byte-identical to the field machine's run**: pack determinism
held across macOS → Windows, which is the rounding chapter's own claim, now demonstrated on
itself. Federation audit: fieldguide 23pp / 0 broken / 0 leaks / 0 orphans; dtg 92pp / 0
broken (2 leak hits = the two manifested chronicles, known false positives).

---

## Per-repo inventory (in push order)

### 1. `~/field_guide_privacymage` — **WORKING DIRECTORY, stays git-less (ruled 2026-08-17)**
The First Person's ruling: the field guide is a working directory that folds into the whole —
the canonical repos (master · cityofmages · spellweb · docs) receive the updates; the
directory itself is not versioned. It remains the build source for the wiki lane
(`fieldguide.localhost` + the Pi pushes) and keeps Max's ARWorld pack (another author's
papers — never folded into the corpus, only served with attribution).
- **This wave (in the working dir):** Windows portability patch — `runtimes/verify.mjs`,
  `fixtures/test.mjs`, `questions/test.mjs`, `reflection/test.mjs` (fileURLToPath, not
  URL.pathname), `lab-bridge/test.mjs` (pathToFileURL for the ESM import), python3→python
  fallback. Suite CONTENT untouched; 124/124 green after. `wiki/assets-staging/` mirror
  deliberately NOT patched (published, digest-checked evidence of the field state).
- **The fold (durable substance → repos):** counter-spec + reflection map + question map +
  both NOTEs + the full `runtimes/` (post-patch) copied to
  `agentprivacy-docs/research/fieldguide/` with a provenance README — verify re-run there:
  ALL GREEN 124/124, same vectors sha. Chronicle → master; act → cityofmages; weave →
  spellweb; X11 → the lab. Nothing durable now lives only in the working dir.
- **Mitch:** nothing to push here.

### 2. `~/dtgwg-cred-spec-main_mage` (private · main @ e40e7f4 · dirty 4)
- **This wave:** `explorations/X11-field-guide-deployment.md` (byte-copy from the field
  machine, hash-verified), `explorations/README.md` (fifth-wave table row for X11),
  `tools/build-kb.mjs` (SOURCES rows for X10 + X11 — X10 had never been manifested),
  and the pre-existing `INTEGRATION-MAP.md` modification (identical on both machines).
- **Mitch:** commit + push (private remote). After push, the Mac-side copy pulls and its
  untracked X11 becomes redundant (delete there, don't re-add).

### 3. `~/agentprivacy_master` (main @ 36580fd · dirty 30)
- **This wave:** `docs/chronicles/2026-08-17_field_guide_convergence.md` (master chronicle —
  **read + sign before it reflects anywhere public**), nested
  `agentprivacy-skills/…/wikis/agentprivacy-wiki-sync/SKILL.md` (fieldguide row + bijection
  rule + dtg row correction; friend-secret redaction preserved).
- **Backlog riding along (pre-wave, listed for completeness):** six DTG-arc master
  chronicles 07-16 → 08-14 (untracked; already reflected publicly through the 08-14 G.1
  rite), wiki-sync/wiki-watch skill dirs, model/UI edits (`src/…`), CODEX, grimoire v10.4
  JSONs, `.bak` file (suggest dropping the `.bak` from the commit).
- **Mitch:** commit + push; agentprivacy.ai deploy if the UI edits are meant to ship.

### 4. `~/cityofmages` (main @ 269c4fd · dirty 7)
- **This wave:** `tomes/tome-ix-the-horizon/10-the-predicate-in-the-street.md` —
  **PROPOSED, unbound.** Binding is yours: edit `status:` + signature, then commit.
  After binding, rebuild tomes site (`node build-tomes.js` + `add-family` + `audit`) so
  Act 10 federates; I have deliberately not federated the unbound draft.
- **Backlog:** DREAM-2026-08-12, spec 09 + runecraft edits (06-09 arc).
- **Mitch:** bind (or reject) Act 10 → commit + push.

### 5. `~/spellweb` (main @ f0c7369 · dirty 9)
- **This wave:** `src/data/nodes.ts` + `edges.ts` — the Field Guide weave (9 nodes,
  17 edges; all endpoints verified; chronicle node auto-seals from atlas).
- **Backlog:** presets.ts, grimoire v10.4 JSON, DREAM-2026-07-16 / 08-12, hexagram blog.
- **Mitch:** commit + push; spellweb prod redeploy is manual as usual.

### 6. `~/agentprivacy-docs` (main @ 26df900 · dirty 29+)
- **This wave:** `research/fieldguide/` — **the fold**: README + counter-spec + reflection
  map + question map + 2 NOTEs + `runtimes/` (8 suites / 124 properties, green in place);
  `chronicles/2026-08-17_field_guide_convergence_merge.md` (family-B),
  `chronicles/INDEX.md` (new 2026-08 Field Guide section), and THIS manifest.
- **Backlog:** programme pipeline lane (litreview run 03, rehydrations, build scripts,
  08-12 chronicle) — the `the-moving-ceiling (1).md` stray looks like a duplicate download;
  suggest deleting rather than committing.
- **Mitch:** commit + push (private/main per the H1 publishing flow; public origin frozen).

### 7. `~/dtgwg-zkp-tf-mage` (main @ b37d52f · dirty 1)
- No wave changes. The untracked call-companion HTML (identical on both machines) is
  yours to commit or leave.

### 8. Not repos / no action needed to push
- `~/.wiki` farm: fieldguide.localhost live (23pp) · dtg.localhost rewired (92pp, stale
  slug-drift copies moved to `~/.wiki/recycle/`, nothing deleted) · guide hub + family +
  audit + extras rebuilt · new tool `skill-fedwiki/wire-dtg-kb.js` (the now-scripted dtg
  wire step). Local serve only; the public guide snapshot/Gatehouse deploy is a separate
  op if wanted.
- `E:\mouseaugust` (the Mac home): read-only this wave; nothing written. After repo pushes,
  the Mac side pulls rather than re-copying.

## Known-pending (deliberate, not forgotten)
- Reply to Max: written into the corpus, **unsent** — your act.
- Tailnet exposure of fieldguide.localhost (would be hole 8086 + `_tailnet_proxy.js` row).
- Erosion applied to the trust edge itself + edge unmake — the counter-spec's own named gap.
- An independent (not-this-author) consumer of lab runtime 07 — still the standing ask.
