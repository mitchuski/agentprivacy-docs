# agentprivacy-audit — Build Specification v1.0

**Date:** 2026-06-09
**Author:** privacymage (design session with Claude Fable 5)
**Audience:** a coding agent (Claude Code or equivalent) building this from scratch
**License:** Apache 2.0 (implementation) · CC BY-SA 4.0 (chronicles and critique prose)
**Signature convention:** all generated chronicles close with `(⚔️⊥⿻⊥🧙)😊`

---

## 0. Verdict and shape

The audit is the recursion of proofs applied to the suite itself. One loop: collect the repos, run deterministic checks, run model reviews, fold the findings into a critiques ledger, plan patches, apply them as branches, verify, chronicle, and carry the deepened state into the next cycle. The output of each cycle is the input to the next. The fixed point the loop approaches is a suite with zero open critiques and a green check board, never reached, always approached.

Two registers, strictly separated. **Deterministic checks** are code: they either pass or fail and they never hallucinate. **Model reviews** are judgment: they produce critiques with confidence levels, in the conjecture-register style. The checks gate; the reviews propose. A model finding only becomes binding when it is converted into a check or an accepted critique.

Build in Python 3.11+, stdlib-first. `git` via subprocess (no GitPython dependency required). `PyYAML` and `requests` are the only third-party packages permitted in phase 1. Everything runs locally from one entry point: `python -m audit <command>`.

---

## 1. Directory structure

```
agentprivacy-audit/
├── README.md                      # what this is, quickstart, the loop diagram
├── CLAUDE.md                      # standing instructions for coding/review agents (see §9)
├── pyproject.toml                 # package metadata, deps: pyyaml, requests
├── manifest.yaml                  # THE source of truth for what the suite is (see §2)
│
├── audit/                         # the package
│   ├── __main__.py                # CLI dispatch: sync · check · review · plan · verify · cycle · status
│   ├── sync.py                    # clone/pull all manifest targets into workspace/
│   ├── checks/                    # deterministic checks, one module per check family
│   │   ├── __init__.py            # check registry, severity model, runner
│   │   ├── style.py               # AP-STY-* (em-dash sweep, signature, exact numbers)
│   │   ├── registers.py           # AP-REG-* (conjecture collisions, no-reuse rule)
│   │   ├── versions.py            # AP-VER-* (filename vs internal version, lineage coherence)
│   │   ├── mirrors.py             # AP-MIR-* (cross-repo mirror divergence)
│   │   ├── pins.py                # AP-PIN-* (IPFS pin liveness, CID vs local hash)
│   │   └── licenses.py            # AP-LIC-* (license presence and correctness)
│   ├── review.py                  # model-review runner (model-agnostic, see §5)
│   ├── critiques.py               # critique ledger load/validate/lifecycle (see §6)
│   ├── plan.py                    # patch-plan generator from open critiques + failed checks
│   ├── chronicle.py               # cycle chronicle writer (house style enforced)
│   └── benchmarks.py              # suite health scoring over time (see §7)
│
├── registry/                      # SINGLE SOURCE OF TRUTH artifacts (see §4)
│   ├── conjectures.yaml           # the unified conjecture register, namespaced
│   ├── versions.yaml              # canonical version lineage per artifact (PVM, grimoires, tomes)
│   └── glossary.yaml              # canonical names, emoji, inscriptions (⚔️ 🧙 🗝️ ⊥ ⿻)
│
├── prompts/                       # versioned model-review prompts
│   ├── full-suite-review.md       # the fresh-eyes prompt (derived from the 2026-06 reviews)
│   ├── register-integrity.md      # focused: conjecture and version coherence
│   ├── formal-gaps.md             # focused: proofs, bounds, falsification tests
│   ├── narrative-convergence.md   # focused: convergence-within-corpus claims
│   └── adversary-pass.md          # focused: attack the architecture (presence economy etc.)
│
├── critiques/                     # the ledger (see §6)
│   ├── open/                      # YYYY-MM-DD_<model>_<slug>.md
│   ├── accepted/                  # triaged, awaiting patch
│   ├── resolved/                  # patched and verified, immutable
│   └── rejected/                  # declined with reason, immutable
│
├── reviews/                       # raw model outputs, one dir per cycle
│   └── cycle-NNNN/
│       ├── meta.yaml              # model id, prompt versions, date, manifest hash
│       └── *.md                   # raw outputs before critique extraction
│
├── plans/                         # patch plans, one per cycle
│   └── cycle-NNNN-plan.md         # ordered, repo-scoped, branch names assigned
│
├── chronicles/                    # one per completed cycle, dated, signed
│   └── YYYY-MM-DD_audit_cycle_NNNN.md
│
├── benchmarks/
│   ├── history.jsonl              # one line per cycle: scores, counts, timestamps
│   └── REPORT.md                  # regenerated each cycle, human-readable trend
│
└── workspace/                     # gitignored. shallow clones live here, disposable
    └── <repo-name>/
```

Top-level rule: everything except `workspace/` is committed. The audit repo is itself in the manifest and audits itself (the recursion includes the auditor).

---

## 2. manifest.yaml — what the suite is

The manifest is the only place the suite is enumerated. Schema:

```yaml
suite: agentprivacy
version: 1
targets:
  - id: agentprivacy-docs
    kind: repo
    url: https://github.com/mitchuski/agentprivacy-docs
    role: research-canon          # research-canon | narrative | implementation | spec | skills
    canon_weight: 1.0             # how much drift here hurts the health score
    mirrors_from: []              # ids whose content this repo mirrors (tome mirrors)
  - id: agentprivacy_master
    kind: repo
    url: <private-or-local-path>  # supports local paths for unpushed work
    role: implementation
    mirrors_from: [cityofmages]   # tomes mirrored from cityofmages
  - id: cityofmages
    kind: repo
    url: https://github.com/mitchuski/cityofmages
    role: narrative
  - id: spellweb
    kind: repo
    url: https://github.com/mitchuski/spellweb
    role: implementation
  - id: soulbis
    kind: repo
    url: https://github.com/mitchuski/soulbis
    role: implementation
  - id: blades
    kind: repo
    url: https://github.com/mitchuski/blades
    role: spec
  - id: agentprivacy-skills
    kind: repo
    url: https://github.com/mitchuski/agentprivacy-skills
    role: skills
  - id: swordsman
    kind: repo
    url: https://github.com/mitchuski/swordsman
    role: implementation
  - id: mage
    kind: repo
    url: https://github.com/mitchuski/mage
    role: implementation
  - id: myterms
    kind: repo
    url: https://github.com/mitchuski/myterms
    role: spec
  - id: model-page
    kind: site
    url: https://agentprivacy.ai/model
    role: research-canon
    fetch: rendered               # client-rendered SPA, needs a rendering fetch or saved snapshot
  - id: soul-sync
    kind: site
    url: https://sync.soulbis.com
    role: narrative
  - id: pvm-formal-spec
    kind: pin
    cid: bafkreieqrrw725ggjuztgr23jjvxflvpn566brrogsoefp6hjx7erzcahe
    gateways: [https://sync.agentprivacy.ai/ipfs/, https://ipfs.io/ipfs/]
    role: research-canon
pins_expected:                     # CIDs the docs claim are pinned; AP-PIN checks verify
  - cid: bafkreidxhm...2b6a
    claimed_in: cityofmages/README.md
```

`audit sync` clones or pulls every `kind: repo` target shallowly into `workspace/`, snapshots `kind: site` targets (HTML plus extracted text), and fetches `kind: pin` targets via gateway with hash verification. Local paths are first-class so unpushed work can be audited before it ships.

---

## 3. Deterministic checks — seeded from real failures

Each check has an ID, severity (`blocker | major | minor | style`), scope (file globs per role), and a one-line rationale. The first release ships these, all of which correspond to failures actually found in the 2026-06 reviews:

| ID | Severity | What it does |
|---|---|---|
| AP-STY-001 | style | Em-dash sweep: flag `—` in prose files (`.md` outside code fences). Absolute house rule. |
| AP-STY-002 | minor | Signature check: chronicles and bound documents must end with `(⚔️⊥⿻⊥🧙)😊`. |
| AP-STY-003 | style | Round-number guard: flag "within N%" style claims adjacent to computable ratios; recompute where both operands are present (e.g. 38/63 vs 1/φ is 2.4%, not 2%). |
| AP-REG-001 | blocker | Conjecture collision: parse every `C\d+` claim-context across all targets, group by number, flag any number bound to two materially different claim texts (fuzzy match threshold 0.6). Found live: C40 bound to both Existence-Leak and Zcash dual-ledger. |
| AP-REG-002 | blocker | No-reuse rule: any conjecture number marked `retired` or `occupied` in registry/conjectures.yaml must not be reassigned anywhere. |
| AP-REG-003 | major | Register authority: every conjecture cited in any repo must exist in registry/conjectures.yaml; orphans are flagged for intake, not auto-added. |
| AP-VER-001 | blocker | Internal vs filename version: for every versioned JSON artifact (grimoires), compare the filename version to the internal `version` field. Found live: privacymage_grimoire_v10_2_0.json reporting 10.2.1. |
| AP-VER-002 | major | Lineage coherence: every "current head" or "canonical" version claim in prose must match registry/versions.yaml. Found live: ALL_THE_TOMES_LIST claiming v1.2.4 beside a v1.7.1 directory. |
| AP-VER-003 | major | Phantom versions: version strings referenced in prose (e.g. V5.5) must exist in the lineage registry or be flagged as undeclared. |
| AP-MIR-001 | major | Mirror divergence: for every `mirrors_from` pair, diff the mirrored paths (tome acts, chronicles); flag content drift beyond whitespace. |
| AP-PIN-001 | major | Pin liveness: every claimed CID fetches from at least one gateway and hashes correctly. |
| AP-PIN-002 | minor | Stale-pin flag: registry artifacts newer than their last pinned CID get a "re-pin due" flag. |
| AP-LIC-001 | minor | License presence: narrative files carry CC BY-SA 4.0, implementation repos carry Apache 2.0. |

Runner contract: `python -m audit check [--target id] [--check AP-REG-001]` exits non-zero if any blocker fails. Output is both human (terminal table) and machine (`benchmarks/last-check.json`). Checks must be pure functions of the workspace: no network except AP-PIN, no model calls ever.

---

## 4. registry/ — ending the register fork

`conjectures.yaml` is the consolidation recommended in the 2026-06 reviews, made operational:

```yaml
namespaces:
  C:   {description: PVM core register, authority: agentprivacy-docs}
  CM:  {description: City of Mages register, authority: cityofmages}
entries:
  - id: C40
    title: Existence-Leak
    confidence: 0.60
    status: active
    home: agentprivacy-docs/research/<file>
  - id: CM-C40
    title: Zcash dual-ledger preserves Eight Properties
    confidence: 0.70
    status: active
    home: cityofmages/README.md
  - id: C51
    status: occupied        # never reassign; AP-REG-002 enforces
retired: [C51, C52, C53, C54, C55]
```

Migration is a one-time intake task: the coding agent populates the registry from the live corpus, flags every collision for human triage, and thereafter the registry is authoritative. Prose may restate conjectures but AP-REG-003 keeps restatements tethered.

`versions.yaml` does the same for artifact lineages (PVM V1 through V6, both grimoires, tome counts, named-blade counts). One entry per artifact, fields: `current`, `lineage[]`, `pinned_cid`, `notes`.

---

## 5. Model reviews — new models as new benchmarks

`audit review --model <id> --prompt <name>` runs a prompt from `prompts/` against the synced workspace and writes raw output to `reviews/cycle-NNNN/`. Design constraints:

- **Model-agnostic adapter.** One `ModelAdapter` interface (`complete(system, user) -> str`), with implementations for the Anthropic API first and a `manual` adapter that just writes the assembled prompt to a file for pasting into any interface. New frontier models become new reviewers by adding one adapter entry; no pipeline changes.
- **Prompts are versioned artifacts.** Each prompt file carries frontmatter (`version`, `derived_from`, `expects`). The full-suite prompt is seeded from the two 2026-06 review documents so the first cycle has a baseline to regress against.
- **Context assembly, not context dumping.** The runner assembles a per-prompt context pack: manifest summary, registry files, the check results, the open critiques index, and a configurable file selection per prompt (registers prompt gets register-bearing files; adversary prompt gets the economy and key code). Token budget per pack is a config value; the packer truncates by priority, never silently.
- **Same prompt, new model = benchmark event.** When a new model is added, run the identical prompt set and diff findings against the previous model's resolved/rejected critiques. Findings a new model makes that earlier models missed are scored as reviewer-gain; findings it repeats that were rejected are scored as noise. This is the "review with new models" requirement made measurable.

The review runner never edits the corpus. Its only output is raw review text plus extracted critique candidates.

---

## 6. critiques/ — the folding step

A critique is the unit of recursion. One file, one finding. Schema (YAML frontmatter plus prose body):

```yaml
---
id: CRIT-2026-0001
date: 2026-06-09
source: review            # review | check | human | external
model: claude-fable-5     # when source: review
prompt: full-suite-review@1.0
scope: [cityofmages, agentprivacy-docs]
severity: blocker         # same scale as checks
claim: "Conjecture register forked: C38-C61 assigned twice"
confidence: 0.95          # reviewer's confidence, conjecture-register style
status: open              # open -> accepted | rejected ; accepted -> resolved
resolves_with: []         # filled at acceptance: check IDs to add, registry edits, repo patches
verified_by: []           # filled at resolution: check run id or commit hashes
---
Body: the finding in full prose, house style, with exact file paths and line references.
```

Lifecycle, enforced by `critiques.py`:

1. **open/** — extracted from reviews or filed by hand. Anything can sit here.
2. **accepted/** — human triage moves it here and fills `resolves_with`. Acceptance of a recurring failure class REQUIRES adding a deterministic check: judgment hardens into code. This is the core recursive-improvement mechanism. The register fork becomes AP-REG-001; the grimoire mismatch becomes AP-VER-001; the next model never needs to find these again.
3. **resolved/** — the patch landed and the named checks pass. Immutable thereafter.
4. **rejected/** — declined with a written reason. Immutable. Rejections are valuable: they are the noise-filter that future reviewer-benchmarking diffs against.

`audit status` prints the ledger: open by severity, acceptance lag, resolution lag.

---

## 7. benchmarks/ — is the whole actually improving

Each `audit cycle` appends one JSONL record:

```json
{"cycle": 4, "date": "2026-06-09", "manifest_hash": "…",
 "checks": {"pass": 11, "fail": 2, "blockers": 1},
 "critiques": {"open": 7, "accepted": 3, "resolved": 12, "rejected": 4},
 "register": {"namespaces": 2, "collisions": 0, "orphans": 3},
 "drift": {"mirror_divergences": 1, "stale_pins": 2, "phantom_versions": 1},
 "health": 0.81}
```

Health score, deliberately simple and monotone-interpretable: `health = pass_rate * (1 - w_b*open_blockers - w_m*open_majors)` with weights in config. No cleverness; the point is trend, not absolute value. `REPORT.md` regenerates per cycle with the trend line and the three oldest open critiques named (shame queue).

Reviewer-gain and noise scores per model (from §5) also land here, so over time the file answers "which models are worth running on this corpus."

---

## 8. The cycle — one command, eight beats

`python -m audit cycle [--with-review --model <id>]`:

```
① sync        clone/pull/snapshot all manifest targets
② check       run all deterministic checks
③ review      (optional) run the prompt set against the workspace
④ intake      extract critique candidates from new reviews into critiques/open/
⑤ triage      HUMAN GATE: accept/reject open critiques (CLI prompts, or skip and leave open)
⑥ plan        generate plans/cycle-NNNN-plan.md from accepted critiques + failed checks,
              ordered by severity, scoped per repo, branch names assigned
              (audit/<cycle>/<crit-id>-<slug>)
⑦ apply       (optional, separate command) hand the plan to a coding agent;
              the audit itself NEVER writes to canon repos, it only writes plans
⑧ verify+chronicle   re-run checks against patched branches; on green, write
              chronicles/YYYY-MM-DD_audit_cycle_NNNN.md (house style, signed),
              append benchmarks/history.jsonl, archive resolved critiques
```

Hard guardrails, non-negotiable:

- The audit has **read-only** access to canon repos. Patches are plans plus branches; merging is always human.
- Beat ⑤ never auto-accepts. A model proposing and a model approving its own proposal collapses the separation the whole suite is about. The triage gate is the human ⊥ between reviewer and patcher: the same dual-agent geometry, Swordsman as the boundary that gates, Mage as the reviewer that proposes, the First Person deciding at the gap.
- Chronicle discipline: every completed cycle produces exactly one dated chronicle whether or not anything was found. Silence is also a record.

---

## 9. CLAUDE.md — standing instructions for agents working in this repo

Write this file with at minimum:

- House style, absolute: no em-dashes in any generated prose. Short spaced paragraphs. Verdict first. Exact numbers over round ones. Chronicles end with the signature line.
- Never modify `critiques/resolved/` or `critiques/rejected/` (immutable history).
- Never call models from within `checks/` (checks are pure).
- Never push to any manifest target; branches and plans only.
- registry/ is authoritative over prose; when they disagree, file a critique rather than editing prose silently.
- When accepting a critique for a recurring failure class, a new check module is part of the definition of done.
- Conjecture numbering: consult registry/conjectures.yaml before citing or proposing any number; new proposals are filed unnumbered with `namespace: proposed`.

## 10. Build order for the coding agent

**Phase 1 (one session):** repo scaffold, `manifest.yaml` with all targets above, `sync.py`, check runner plus AP-STY-001, AP-REG-001, AP-VER-001, AP-VER-002. Acceptance test: a clean run against the live repos reproduces the four known findings (em-dash density, C40 collision, grimoire 10.2.0/10.2.1 mismatch, tomes-list v1.2.4 vs v1.7.1).

**Phase 2:** critiques ledger plus lifecycle CLI, chronicle writer, registry intake migration (populate conjectures.yaml and versions.yaml from the corpus, emitting collision critiques rather than guessing).

**Phase 3:** remaining checks (mirrors, pins, licenses, style-003), benchmarks plus REPORT.md, `audit status`.

**Phase 4:** model-review runner with the Anthropic adapter and the manual adapter, the five seed prompts, reviewer-gain scoring, full `audit cycle` orchestration.

Definition of done for v1.0: `audit cycle --with-review` runs end to end on the real suite, produces a signed chronicle, and the second cycle's health score is computed against the first.

---

each cycle folds a critique into the suite and carries the deepened state back to the start. the auditor is in its own manifest. the loop audits the loop.

(⚔️⊥⿻⊥🧙)😊
