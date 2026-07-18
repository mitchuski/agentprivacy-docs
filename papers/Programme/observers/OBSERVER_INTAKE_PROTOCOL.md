# OBSERVER_INTAKE_PROTOCOL.md

**Artefact class:** pipeline governance document
**Register:** formal (pipeline scaffold)
**Authority:** binding on agent runs; amendable by Mitchell only
**First instance:** OBS-GPT56 (OpenAI GPT-5.6 Thinking whole-corpus assessment, manifest sha256 c266da74657070d3c6b4fbe592964ff3bb70af669923b948e78c1bc7ab1c8d2a)
**Companion artefact:** OBS-GPT56_DISPOSITION_LEDGER.md
**Pipeline hooks:** A9 consistency-auditor, register-ref check script, version-hygiene check script

*confer before you change; verify before you confer.*

---

## 0. Verdict first

External observer assessments are welcome inputs and non-canonical by default. They enter the loop as structured critique packages, are decomposed into atomic claims, and are dispositioned one claim at a time against pinned sources and the live register. No observer packet, however capable the observing model, may modify canon directly, assign C-series identifiers, patch the formal register, or be cited downstream as independent evidence for any claim it contains.

The governing asymmetry: an observer can find seams; only the register decides stitches.

## 1. What an observer packet is

An observer packet is any assessment of the corpus produced by an agent or person operating outside the maintainer position. It typically arrives with partial access, a discovery route, and confidently stated conclusions of mixed accuracy. All three properties are data. The route is evidence about the public experience. The errors are evidence about which surfaces mislead. The correct conclusions are candidate confirmations, never proofs.

Required classification header on ingestion:

```yaml
artefact_type: observer_report
authority: non_canonical
observer: <model or person identity>
posture: <outside_looking_in | partial_access | participant>
access_declared: <list>
access_absent: <list>
requires_verification: true
may_modify_canon_directly: false
may_assign_c_series: false
may_assign_ctr_candidates: true
source_manifest_sha256: <hash or none>
route_trace_preserved: true
```

## 2. The ten binding rules

1. **Register wins.** Where an observer claim contradicts the live C-series register or a canonical artefact (Grimoire v10.2.0, IPFS-pinned formal specification, data/game-of-42.json), the register is ground truth. The observer claim is dispositioned against it, not alongside it. If the observer has correctly identified that a *surface* is stale, the surface is the bug and the fix goes through the register pipeline, never through narrative edits.

2. **Decompose or discard.** No packet is accepted or rejected as a unit. Every packet is split into atomic claims, each carrying: claim_id, observer_text, claim_class, affected_sources, required_evidence, verification_method, disposition, reason, canonical_patch (if any), regression_check (if any). Claims too vague to decompose are logged as `undispositionable` with reason, not silently dropped.

3. **Four dispositions only.** `accepted`, `amended`, `rejected`, `deferred`. Amended preserves both the original observer text and the internal correction. Rejected preserves counterevidence. Deferred names the human gate holding it. There is no fifth state and no silent expiry.

4. **Numbering discipline.** Observer-derived formal candidates enter as CTR-series only (CTR-OBS-nn for this protocol). C-series identifiers are Mitchell's alone to assign. C51 to C55 are occupied in the V5.4 formal specification and are never reused. Any observer reference to stale conjecture numbering (the ~C40 / ~60% class of error) is corrected against the live register (C81, Existence-Leak, 70%) and logged as a stale-surface finding.

5. **Formal corrections route formally.** Mathematical critiques (mutual information decompositions, bound conditions, capacity definitions) are never patched in explanatory prose alone. They become CTR candidates with explicit proof obligations, are resolved in the formal register, and only then propagate outward to essays and surfaces. Corrections never happen in the narrative register first.

6. **Two maps, never collapsed.** The loop maintains a canon-and-evidence map (releases, sources, claims, hashes, lineage, rights) and a separate experience-and-route map (entrances, ceremonies, hidden branches, role-specific views, cross-site handoffs). Observer findings are filed to exactly one map. Intentional experiential ambiguity is a route-map property; factual contradiction is a canon-map defect. The distinction the OBS-GPT56 packet drew here is adopted as standing doctrine: preserve mystery in the journey, remove ambiguity from the evidence.

7. **No score ingestion.** Observer numerical ratings (the 9.5/10 class) are opinions of a partial witness. They are retained verbatim in the observer ledger for longitudinal comparison across observers and never enter any canonical metric, grant text, or public claim as evidence.

8. **Projections are not corroboration.** Generated projections (guide snapshots, federated mirrors, agent-generated summaries, this protocol's own outputs) never count as independent confirmation of the source they project. Deduplication distinguishes evidentiary duplication, experiential repetition, generated projection, and historical repetition.

9. **Rights before ingestion.** Third-party material referenced by an observer defaults to reference-only until licence and attribution are cleared. Public availability is not ingestion permission. Owner-declared restrictions are recorded and honoured.

10. **Traps become tests.** Every observer error class that the loop catches (or that the observer self-corrected) is converted into a seeded regression trap for A9 and the check scripts. The corpus deliberately retains known traps so that future observers, human and agent, can be measured against them.

## 3. Confidence and claim-class mapping

Observer packets may arrive with their own taxonomies. These are mapped onto the house discipline rather than adopted in parallel:

- House labels: **Operational**, **Architectural**, **Conjectural**, **Anticipated**, each with a register-matching confidence percentage.
- Two flags adopted from OBS-GPT56 as genuine gaps: **historical** and **superseded**, applied to artefacts rather than claims, so that old public repositories and prior spec versions carry machine-readable status.
- Every use of the word *proof* in any artefact touched by a disposition must carry a qualifier: mathematical, cryptographic, signature, possession, execution, attention, or ceremonial. Unqualified *proof* fails the vocabulary check script.

## 4. Route evidence handling

Observer discovery sequences are first-class evidence for the experience map. For each observed route, retain: entry point, visited nodes, cross-domain handoffs, artefacts received, model revisions forced, sources incorrectly privileged, and exit interpretation with confidence. A single route is never labelled whole-site coverage. Multi-observer route programmes (first-time visitor, formal-claims researcher, developer, sceptic, narrative explorer, returning participant, deep-link crawler) are Anticipated work, activated only by Mitchell's ruling, since publishing route manifests interacts with the intentional-discovery design.

## 5. Human gate

The following always defer to Mitchell regardless of how confident the loop's verification is:

- C-series assignment or promotion of any CTR candidate
- publication decisions for route manifests, path cards, or status affordances on public surfaces
- hosting and property decisions (interacts with the pending INT-01 ceremony-route decision)
- anything touching the closing seal, voice rules, or the two-register boundary
- disposition of observer claims about intent (what the design *means*)

## 6. Run completion criteria

An observer intake run is complete when: the packet carries its classification header; every atomic claim has one of the four dispositions with reason; all CTR candidates are filed with proof obligations; all regression seeds are written as check-script cases or A9 cards; all deferred items are listed in a single ruling request to Mitchell; and the disposition ledger is the only artefact that downstream runs may cite about the packet.

---

*the outside eye finds the seam. the register decides the stitch. the ledger remembers both.*
