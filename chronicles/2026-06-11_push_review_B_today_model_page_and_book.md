# Push Review B · Today (2026-06-11) — the Model-Page Wiring, the Book, and the Pins Question

**Date:** 2026-06-11
**Purpose:** describe the 2026-06-11 work, in progress, separately from the pre-today arc (Review A). Smaller and still moving.
**License:** CC BY-SA 4.0

---

## 1. The model page wiring (agentprivacy_master) — IN PROGRESS

The task underway: make the `/model` page render from the V6 JSON instead of the V5.4 JSON.

**What the page actually does, and why pins are NOT the blocker.** The page reads a **local JSON file imported at build time**, not IPFS:

> `src/lib/model-page.ts:16` — `import pvmJson from '@/data/privacy-value-model-v5.4.json';`

The V6 JSON already exists in the repo (`src/data/privacy-value-model-v6.json` and `public/models/privacy-value-model-v6.json`, generated 2026-06-10 from the register). The page just is not importing it yet. So the fix is a code change, not an infrastructure step:

1. Point the import at `privacy-value-model-v6.json` (and reconcile the merge layer in `model-page.ts`, which currently merges the v5.4 dark model with the hardcoded Tome-V conjectures; the v6 JSON should become the source so page and register cannot fork).
2. Update the lineage line to V6, the conjecture range/count from the register (head C89), and the hero/abstract per the V6 thesis.
3. Refresh the `v6-lineage` grouping and the `model-downloads` V6 entry (already partly landed pre-today).

**The pins answer, directly: no, you do not need pins to make the page render the correct JSON.** The grimoire CIDs in `src/lib/grimoire-ipfs.ts` (v10.4.0 = `bafybeicvbong…stsm`) are served as *links and a verify-the-bytes story* on the page; they are not the data source for the conjecture rendering. IPFS pins matter for two separate things, both later and both not blocking the page:
- the **citable artifact CIDs** (the README IPFS table, the downloadable grimoire/paper bytes), and
- the **V6 document re-pin**, which the reflection map deliberately schedules **last**, after the reflection gate (G5), alongside the grimoire bumps and the deploy.

So if the page is rendering V5.4 content, the cause is the `model-page.ts` import line still pointing at the v5.4 JSON, not a missing pin. Swap the import; the page renders V6 from the local file with no network step.

## 2. agentprivacy-docs — files touched today

- `chronicles/2026-06-11_compendium_plan_privacy_is_value_the_book.md` — a new plan: *Privacy is Value: The Book*, a compendium of the corpus.
- `reference/PAPERS_INDEX.md` — papers index (new or refreshed).
- `plans/V6_FIRST_PERSON_READING_LEDGER.md` — reading-ledger update (the completion-read gate for the V6 suite).
- `README.md` — continued V6 body alignment.
- These two review chronicles (A and B).

## 3. Status

The model-page wiring is the live task; nothing in master is saved for it yet. The book compendium plan is new scope, not part of the V6 push. Treat Review B as the smaller, in-flight follow-on to the Review A arc: push A's coordinated arc first (docs then master), and let the master model-page import flip ride in master's commit so the page goes V6 the moment master is pushed.

---

## The short version for the push

- **Review A** = the V6 suite + the MODEL-coherence reseat + the coherence cleanup (everything through 2026-06-10). Review once, push as a coordinated arc, docs first.
- **Review B (today)** = flip the model-page import to the v6 JSON (one line plus the merge-layer reconcile), the book plan, the papers index and ledger touch-ups. **No pins required for the page**; the V6 re-pin is a separate, later, gated step.

(⚔️⊥⿻⊥🧙)😊
