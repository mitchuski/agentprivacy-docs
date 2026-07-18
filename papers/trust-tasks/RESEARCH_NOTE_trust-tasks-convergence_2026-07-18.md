---
title: "Trust-task convergence: agentprivacy ceremonies as ToIP Trust Tasks"
tier: D
status: research note, local, v1
date: 2026-07-18
author: privacymage (with the First Person)
sources:
  - "~/dtgwg-cred-spec-main_mage/TRUST-TASKS-FIT-MAP-2026-07-18.md (observation record)"
  - "~/dtgwg-trust-tasks-tf-mage (workbench: clone of trustoverip/dtgwg-trust-tasks-tf @894fcc6 + 10 new specs)"
  - "docs/experience/CHRONICLE_trust_tasks_browser_compute_integration_2026-06-11.md (the original correspondence)"
  - "~/dtgwg-cred-spec-main_mage/SPEC-DRAFT-proof-of-understanding-trust-task.md (LAN ceremony promotion)"
  - "~/dtgwg-cred-spec-main_mage/explorations/X3-trust-task-composition.md (bundle profiles, credential/artifact wall)"
reproduction: "cd ~/dtgwg-trust-tasks-tf-mage && npm run validate  →  'Validated 176 specs, indexed 34 shared schemas' (baseline repo: 166/33)"
---

# Trust-task convergence: agentprivacy ceremonies as ToIP Trust Tasks

**Tier note.** This is a TIER-D artefact: architecture and integration surfaces.
Conjectural material appears only as clearly marked design assumptions (§5).

## 1. Object of study

Whether the agentprivacy trust-task constructions (the KY-A admission ceremony and
the LAN proof-of-understanding ceremony) can be expressed, without loss of their
load-bearing rules, inside the Trust Over IP DTGWG *Trust Tasks* framework
(trusttasks.org, framework SPEC.md v0.2 working draft), using only the framework's
own conventions.

Result: **yes, at schema level.** Ten specifications across two new families
(`agent-admission/*` x6, `understanding/*` x4) validate in the registry's own
build alongside its 166 existing tasks. Every named rejection of the source
ceremonies survives as either a schema constraint or a namespaced error code.

## 2. The registry, observed

Conventions found upstream that are worth adopting suite-wide, independent of any
submission:

1. **Descriptive, never prescriptive, effect axes.** Every task declares
   `sideEffects` (none / mutating / destructive) and `exposure` (discloses
   none / metadata / secret, plus `actsAsSubject`), and the framework forbids
   deriving consent policy from the declaration: consumers derive the
   authoritative class from the handler they invoke. Registry metadata renders;
   executing code decides. This cleanly separates the catalogue's honesty from
   the consumer's sovereignty.
2. **Closed vocabularies as schemas, not conventions.** The category taxonomy is
   a JSON Schema enum; adding a category is a deliberate schema change. Same
   instinct as our closed verdict lexicon, applied to classification drift.
3. **The envelope discipline.** `id / type / payload / issuer / recipient /
   threadId / proof`, request and response linked by `threadId`, errors always a
   distinct error type, payload schemas closed (`additionalProperties: false`).
   Audience binding: a proof without an in-band recipient is invalid unless the
   spec opts out as bearer.
4. **Two-implementation promotion bar.** draft → candidate requires two
   interoperable implementations; candidate → standard requires 90 days without
   breaking change. Maturity is earned by interop, not prose.

## 3. The mapping

| agentprivacy construction | Registry expression | Load-bearing rule preserved as |
|---|---|---|
| KY-A submission + witness draw | `agent-admission/apply` 0.1 | draw derived from sha256 of canonical submission; `WitnessDraw` shared schema; auditor re-derivable |
| Understanding challenge (h(τ) gate) | `agent-admission/respond` 0.1 | `copyNotComprehension` error code; published thresholds in response |
| Supervisor approval (human gate) | `agent-admission/approve` 0.1 | `supervisorIsAgent` refusal; one decision per application; deny is terminal |
| Bilateral VRC issuance (two gates) | `agent-admission/issue` 0.1 | five ordered rules in Conformance; `gates` array `minItems=maxItems=2`, distinct kinds; closed `Verdict` enum (validated / failedHeldOut / blocked); `tierScopeMismatch` |
| Revocation + ERC-8004 mirroring | `agent-admission/revoke` 0.1 | `sideEffects: destructive`; mirror mandatory, reason text never mirrored |
| Relying-party read | `agent-admission/status` 0.1 | anchors are evidence, this read is authority |
| LAN ceremony: consent-first offer | `understanding/offer` 0.1 | offered-never-scanned as a MUST; `nameResolvesSometimes` = refusal, not retry |
| Gateway reading + comprehension | `understanding/exchange` 0.1 | gateway pinned by digest; own-words rule |
| MyTerms / IEEE 7012 seal | `understanding/seal` 0.1 | joiner proposes from roster; `selfIssuedSeal` refused; content-addressed witness record |
| Cookie-broker graduated access | `understanding/grant` 0.1 | `exposure.discloses: secret` with rationale; `rawCredentialRequested` always refused |

The tier/scope machinery (det(Σ) and the stratum, in harness vocabulary) crosses
the boundary as an opaque `TierGrant`: an integer tier plus a resolvable
`scopeFunction` reference. The derivation stays ours; the registry carries only
that scope is derived from a published function, never negotiated.

## 4. Convergence findings

Independent constructions on both sides arrived at the same shapes. Four
correspondences, none coordinated:

1. **Their `task-consent/*` ↔ our two-gate rule.** Their delegated-execution
   design binds what a human approves to the exact payload that executes
   (salted, type-bound digest; effects from dry-running the real handler). Our
   admission ceremony binds who may execute at all to a human approval plus
   demonstrated understanding. Same closure, either side of the delegation
   boundary; an admission tier is a natural input to their `policy/evaluate`.
2. **Their `vault/proxy-login` ↔ our cookie broker.** Exercise a credential
   without releasing it. `understanding/grant` states the same custody line at
   ceremony time and names the refusal (`rawCredentialRequested`).
3. **Their TRQP `registry/authorization` ↔ our status read.** Point-in-time
   authoritative reads with the registry as authority and caches distrusted.
4. **Their descriptive effect axes ↔ our credential/artifact wall.** Both keep
   the catalogue descriptive and the reliance decision local. The wall (a proof
   show never constitutes completion evidence) is proposed in the companion
   design note as a candidate third axis, *evidence class*: what a successful
   response may be relied on to establish, and for how long.

## 5. Design assumptions (marked)

- **A1.** The two-gate rule generalises beyond the regulator posture: we assume
  any admission scheme collapsing approval and understanding into one gate loses
  the meaning of both. Evidence: the source ceremony's reference auditor
  (14/14 properties); not yet tested against a second implementation.
- **A2.** The witness-draw mechanism is portable to the peer posture
  (`understanding/exchange` notes it as optional). Untested there.
- **A3.** An opaque tier plus published scope function is enough interop; a
  shared tier vocabulary is not needed. This is the thinnest-possible-interface
  bet and may be wrong for cross-authority tier comparison.
- **A4.** The IEEE 7012 seal can be pinned by a single digest over three
  registers (plain, legal, machine-readable). If registers version
  independently, the pinning needs a digest per register.

## 6. Limits

- Schema-level conformance only. No second implementation, no interop run, no
  upstream review. The registry's own promotion bar (two interoperable
  implementations) is not met and is not claimed.
- The upstream framework is a v0.2 working draft by a single author; its
  conventions may move under these specs.
- The Gatehouse engine itself remains fenced by its own ruling; the specs
  re-express its ceremony and cite none of its code.
- Nothing in this note has been submitted, published, or circulated. All
  artefacts are local and uncommitted.

## 7. Artefact locations

- Specs + design notes: `~/dtgwg-trust-tasks-tf-mage` under `specs/agent-admission/`,
  `specs/understanding/`, `docs/design-notes/` (untracked; tree otherwise clean).
- Observation record: `~/dtgwg-cred-spec-main_mage/TRUST-TASKS-FIT-MAP-2026-07-18.md`.
- LAN ceremony promotion: `~/dtgwg-cred-spec-main_mage/SPEC-DRAFT-proof-of-understanding-trust-task.md`.
- Public telling: `blog/trust-tasks-at-the-gate.md` (this suite).

## 8. Open questions

1. Registry authority for bundle profiles (context authority, Trust Task TF, or
   shared body): interlocks with the ZKP-side X3 programme.
2. Whether *evidence class* merits a framework axis or stays per-spec prose.
3. Witness-draw portability to the peer posture (A2).
4. Tier vocabulary across gate authorities (A3).
5. Whether `understanding/seal`'s witness record wants a registered shared
   schema, given the same shape recurs in the admission ledger head.
