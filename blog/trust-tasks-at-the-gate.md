---
title: "Trust Tasks at the Gate"
subtitle: "ten specs, two ceremonies, one registry · a Privacy is Value letter"
series: "Privacy is Value"
tier: P
version: "draft v1, local"
date: "2026-07"
author: "privacymage"
license: "CC BY-SA 4.0"
model_authority: "TRUST-TASKS-FIT-MAP-2026-07-18.md · ~/dtgwg-trust-tasks-tf-mage (10 specs, validate green) · CHRONICLE_trust_tasks_browser_compute_integration_2026-06-11.md · papers/trust-tasks/RESEARCH_NOTE_trust-tasks-convergence_2026-07-18.md"
---

# Trust Tasks at the Gate

The verdict up front, in the house style:

the ceremonies compile. ten agentprivacy trust tasks now validate inside the Trust over IP reference registry's own build.

## the bridge that was a metaphor

In June, a chronicle drew a correspondence table and left it on the wall. The City's workshops mint proof packets; Trust over IP's Decentralised Trust Graph working group keeps a reference registry of "trust task" specifications at trusttasks.org. The table said: our artefact descriptor is their task specification, our proof packet is their verifiable credential, our grimoire is their registry. It was a good metaphor, and it stayed a metaphor for five weeks.

This letter reports the metaphor cashing out. Two of the City's ceremonies have been rewritten as registry-conformant specifications, in the registry's own JSON Schema discipline, passing the registry's own validator alongside its 166 existing tasks. Not described. Written, schema by schema, and checked by machinery we did not build.

## what a trust task is

A trust task is one finite unit of verifiable work between two parties, captured as a JSON document that travels independently of whatever protocol carries it. Who issued it, who it is for, what it asks, a signature that binds the asking. Small, closed, portable. The registry's framework is a working draft, and its instincts run close to ours: every task declares what it mutates and what it discloses, and the declaration is descriptive, never prescriptive. The registry tells you what a task does. Whether that requires a human's consent is your policy, derived from your own handler, never delegated to a registry.

Closed vocabularies, declared disclosure, authority kept local. We have been singing that tune in a different key for a year.

## the first ceremony: two gates at the gatehouse

The first family is the admission ceremony, six specifications under the slug `agent-admission`. It answers the question the delegation stack skips: before an agent is trusted to do anything, how does it become admitted at all?

Not by key possession. Any agent can hold a key. Admission asks whether the agent understands the policy it will be bound by, and whether a human accountable for it has said yes. Two gates, different in kind, and either alone is refused. An approval without demonstrated understanding is patronage. Demonstrated understanding without an accountable approver is unsupervised admission.

The mechanisms that made the Gatehouse honest travelled intact. The challenge criteria are drawn from the hash of the agent's own submission, so the submission cannot be written to the test. The verdict lexicon is closed at three: validated flies, a failed held-out probe lands in the sandbox, a violated hard constraint holds everything, and an invented fourth verdict is itself a rejection. The credential that results is bilateral, two signatures from two distinct parties, because a relationship credential one party can mint alone is an assertion wearing a relationship's clothes. And where the outcome is anchored on an external registry, the anchor is evidence, never authority.

## the second ceremony: understanding at the door

The second family is the LAN ceremony, four specifications under the slug `understanding`. It is the consent-first sibling: no supervisor, two parties meeting as equals.

A joining party offers its address. Offers, is not scanned for; the offering is the consent. The host answers with a gateway, the terms of the room pinned by digest. The joiner answers those terms in its own words, and copying the text back is refused, because the key to the room is what you understood, not what you can retrieve. Then the joiner, not the host, proposes the agreement, machine-readable personal privacy terms in the IEEE 7012 pattern, and the host's signed acceptance seals it. Last comes access: a broker mints a scoped, expiring grant, and the room's underlying credential never leaves the broker's hands. Asking for the raw credential is not a negotiation. It is a named refusal.

access is earned by understanding, not credential.

That sentence has been the City's door rule since a router move killed a hostname and taught us that a name which resolves sometimes is worse than one that never does. It is now also a schema constraint that a validator enforces.

## what we found on their side of the bridge

The pleasant surprise of the whole exercise: the registry already contains our instincts, independently arrived at.

Their consent flow binds what a human approves to the exact bytes that execute, which is our two-gate rule seen from the execution side. Their vault family includes proxy login, exercising a credential without releasing it, which is the cookie broker wearing standards clothing. Their status queries insist the registry read is authoritative and anchors only mirror it, which is evidence-never-authority stated as protocol. Convergence like that, uncoordinated, is the strongest signal available that the underlying shape is real.

## honesty label, because that is the house style

These ten specifications are drafts in a local workbench, validating against the registry's build but submitted nowhere. The upstream registry is one author's fast-moving work, all 166 existing tasks from a single hand, and nothing here presumes its acceptance. Validation is schema-level conformance, not interoperability; two independent implementations is the registry's own bar for promotion, and we are at zero. What this letter claims is exactly what can be re-run: clone the workbench, run the validator, watch 176 specifications pass where 166 passed before.

the door is real, and it is still our own door. what changed is that the hinges now fit a standard frame.

(⚔️⊥⿻⊥🧙)😊

🙂
