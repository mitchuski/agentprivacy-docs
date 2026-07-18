# V6 Rehydration Pipeline · Operations

How to run a collection of Claude instances against this directory. The programme this pipeline serves is `programme/V6_RESEARCH_PROGRAMME_v2.md`; this README is only the machinery.

## What lives where

```
pipeline/
  CLAUDE.md              agent boot file (Claude Code reads this automatically at repo/dir level)
  GROUND_RULES.md        GR-1..GR-10, binding every role
  manifest.yaml          pipeline state · A0-only writes
  roles/                 fourteen role cards (A0..A13), one per session
  extractions/           E1..E9 claim inventories · E2 is the built exemplar and gold standard
  rehydrations/          artifacts by audience: public/ policy/ grants/ academic/ standards/ developer/
  reviews/               critiques_ledger.md (append-only) + pc_reviews/
  checks/                four deterministic checks, runnable now (python3, stdlib only)
  templates/             extraction, task card, review, ledger entry formats
  tasks/                 task cards cut by A0 · WP-02_A2 and WP-07_A3 exist as exemplars
  programme/             the programme document, standards matrix, deadlines (A13)
```

## Booting a session

One session holds exactly one role. In Claude Code, from the repo root:

> You are running role **A3** in the V6 Rehydration Pipeline. Read `pipeline/GROUND_RULES.md`, then `pipeline/roles/A3-formalist.md`, then your task card `pipeline/tasks/WP-07_A3.md`. State your role, permitted reads/writes, and definition of done in three lines, then begin on branch `wp-07-linear-cap`.

That sentence is the whole protocol. The role card carries the mission, permissions, definition of done, and the role's named failure modes; the task card carries the WP-specific objective, inputs, outputs, and handoff. If a role has no task card, it asks A0 (i.e. you, or an A0 session) before inventing work.

## Running roles in parallel without collisions

- **One branch per WP** (`wp-NN-shortname`); extractions change only on main via A1.
- **manifest.yaml is A0's alone.** Every other role treats it as read-only truth; status changes are requested in the session summary and applied by A0.
- **The ledger is the only shared write surface** and it is append-only, so parallel sessions cannot conflict; entry IDs are taken as next-available at append time.
- **Extractions are upstream of everything:** if two WPs need the same new claim, it is added to the extraction (A1, main), never duplicated into two drafts.
- Recommended concurrency: one A0 session standing, two to three producer sessions (A2/A3/A6/A8/A12), one A5 session reviewing what producers finished last cycle, A9 weekly. More than five parallel sessions and the ledger review becomes the bottleneck; A0's decision list keeps you, the human, at three decisions or fewer per cycle.

## The gates, operationally

- **P0 extraction-fidelity:** A0 runs `check_register_refs.py` on the artifact + spot-traces three random claims to extraction lines.
- **P1 genre:** A5 review on file with no BLOCKING items.
- **P2 citation:** A4 verification note appended to the task card.
- **P3 consistency:** all four checks green: `python3 checks/check_register_refs.py <file>` etc. (A9 also runs suite-wide weekly.)
- **P4 completion read:** yours. No role marks it, simulates it, or proceeds past it. The manifest's `gate` field holds the last gate *passed*; anything at P3 is waiting on you.

## The checks (runnable now)

```
cd pipeline/checks
python3 check_register_refs.py  <files>   # C-number hygiene per tier · head C89
python3 check_figures_fence.py  <files>   # GR-3 canonical figures
python3 check_tier_vocab.py     <files>   # GR-4/GR-5: mythos/emoji at S/A · em-dashes at P/G
python3 check_versions.py       <files>   # retired citations · unconditioned ceilings · version fields
```

Tier is read from artifact frontmatter (`tier: S|A|G|P|D`). Non-zero exit = findings; every finding names file and line. Proven on first contact: run against the current whitepaper, `check_versions` finds the eight unconditioned static-ceiling passages and the 6.3 version field that ledger entry L003 records.

Keeping `HEAD = 89` in `check_register_refs.py` synchronised with `manifest.yaml`'s `register_head` is on A9's sweep list.

## The first real cycle (suggested)

1. **You (as A0):** commit this directory; open ledger L001-L003 decisions (two canon-level corrections, one hygiene batch).
2. **Session 1 (A1):** build E1 from the E2 exemplar's pattern; it unblocks WP-02, WP-07, WP-09.
3. **Session 2 (A2):** run task card WP-02_A2; the policy brief has the only hard date (2026-08-02).
4. **Session 3 (A9):** whitepaper hygiene pass to unblock WP-03.
5. **You (P4):** the two July essays are at P0 with drafts on file; they need your completion read, then they ship in the WP-01 → WP-25 order.

the manifest is the map. the ledger is the memory. the gates are the walls. p4 is the door only you hold.
