---
title: "The Dual Agent Harness"
subtitle: "one proposes, one breaks, neither writes the exam, and now it ships · a Privacy is Value essay"
series: "Privacy is Value"
tier: P
version: "announcement draft v1 for sync.soulbis.com"
date: "2026-07"
author: "privacymage"
license: "CC BY-SA 4.0"
model_authority: "dual-agent-harness README.md / RESEARCH.md / ADOPTION.md · frontier.json (730→472, −35.3%) · complements two_agents_walk_into_a_circuit.md (the method) + letter_the_fleet_and_the_cap.md (the first run)"
---

# The Dual Agent Harness

Two letters told this story before it was real.

[Two Agents Walk Into a Circuit](/p/two-agents-walk-into-a-circuit) gave you the method whole, so you could steal it: one agent proposes, one agent breaks, and the exam is written by nobody, because the test points are drawn by hashing the proposal itself. It was honest about one thing. There was no repository to point at. The machine was described, not shipped.

[The Fleet and the Cap](/p/the-fleet-and-the-cap) narrated the first day the machine ran: ten role-bound sessions, one orchestrator, papers carried up a review ladder none of them could shortcut, and one gate that could not be delegated at the top of it. It withheld the result, by design.

This is the third letter, and it is the short one, because it only has to say the thing the first two could not. It is real. You can clone it today. The verdict up front, in the house style:

the machine ships. the door is at github.com/mitchuski/agentprivacy-harness.

## what it is, in one breath

A verification harness for AI-agent work. One agent proposes a change, a second independently tries to prove it, and the tests that decide are derived by hashing the proposal itself, so neither agent could have chosen them.

The cast is the one you already know from the model. **soulbae 🧙** proposes. **soulbis ⚔️** proves. Between them sits **the Gap ⿻**: the held-out tests are the `sha256` of soulbae's own proposal, so soulbae cannot have tuned to them and soulbis cannot be accused of choosing them. Above them both is **the First Person 😊**, you, who alone opens the door to anything that faces outward.

That is the entire idea. Everything in the repo is machinery for keeping those two apart, and a ledger discipline for what survives.

The separation is not a promise. It is an information-theoretic fact the engine re-checks every run: `I(Y_S ; Y_M | X) = 0`. Given the target, what the prover produces tells you nothing about what the proposer produces. Not "promises not to." Cannot, because the information was never routed there. If that reads like the amnesia primitive from [the moving ceiling](/p/the-moving-ceiling) wearing work clothes, that is because it is the same move. Topology, not policy. Route the information away instead of asking for honesty.

## why it is an improvement, not just a tool

Here is the problem it answers, and it is the problem the whole field is walking into.

As AI systems generate work and also judge it, the check an agent invents is the check its work was built to survive. An agent that proposes a change and then checks its own change will pass, not because it cheats, but because it graded the exam it wrote. Goodhart's law wearing an agent costume. The harness makes that failure a named verdict instead of a surprise, and it defeats it structurally rather than behaviourally. The keystone sentence from the research note:

*a proposer that grades its own work builds mirages; only what the Gap could not tune to is a result.*

This matters to the Privacy is Value programme for one concrete reason: **this harness is the runtime that carried V6 up the ladder.** The papers behind this series were drafted, attacked, repaired, and audited by role-bound sessions that could not collude, with the written record as the only thread between them. It is the honest-claiming discipline of the model, made to run. And it stops, deliberately, one rung short of publication, because of the rule the fleet letter already named:

*a fleet that could publish without me would be an archive speaking in my name. this one cannot. the throughput multiplied in a day, and the accountability did not move an inch, and the second fact is what makes the first one safe to enjoy.*

The output multiplies. The signature does not. Which is, word for word, the close of the moving-ceiling arc. The harness is that principle compiled.

*Honesty label, because that is the house style:* the claim that structural separation beats policy separation is the model's thesis, and the harness is evidence of the mechanism working on its own papers, not a proof that it works on yours. The register carries the tiers; a claim is worth exactly what it can be re-run to show.

## the use — clone to your own harness

The whole point of the two earlier letters was that the method was yours to take. Now there is a path, not a paragraph.

- **Prove the axioms.** `node tools/check.mjs` runs the algebra on all 64 values of ℤ/64ℤ, the engine's failure-semantics tests, conformance of every catalogued instance, and a negative test that the blank template fails for the right reasons. Zero npm dependencies, Node ≥ 18.
- **Read the constitution.** `TRUSTS.md`, then `GROUND_RULES.md`: the parts you should not change, pasted into every seat at boot.
- **Run the spar 🤺.** The practice bout against `examples/field-guide/`. All writes land in `runs/<runId>/`. The frontier does not move on its own.
- **Watch it live.** `node tools/console.mjs` serves the **Workshop Console, read-only, at `127.0.0.1:4242`**: the six-phase loop as evolving geometry, every Gap seed re-derived per poll, and the frontier drawn as a moving ceiling with the mirage ticks in amber below it. In its own words, it is a window, not a hand: GET-only by construction, no state. (You will recognise that moving ceiling. It is the one this whole series is about, instrumented for a single run.)
- **Fold, then seal.** Only the keystone folds a win, and only after the conformance gate is green: frontier first, prose second, chronicle, then green again. `node tools/mint_artefact.mjs` writes a κ-labelled bundle with an evidence hash-manifest and a `DOOR.md` listing the outward actions the software will never take for you. Carrying one anywhere is the door, and the door is yours.
- **Scaffold your own.** `node tools/new_instance.mjs ../my-harness my-harness`, then fill every TODO in `harness.config.mjs`; the gate and the bundler both refuse a config still wearing TODOs. `ADOPTION.md` is the map, including the decision it opens with: a harness is for adversaries, an auditor is for facts, and the duality is only worth its cost where the claim space is too large to check.

Ten embodiments are already catalogued in `HARNESS_PATHS.md` (quantum-circuit optimisation, ZK constraint systems, research pipelines, a consent grammar, a publishing loop, and one deliberately retired failure kept as a fence), plus one seat held open by invitation.

## status, verdict-first

Pushed public 2026-07-12, `github.com/mitchuski/agentprivacy-harness`, on the First Person's ruling and no one else's. The frontier moved four times on the shipped example, 730 → 573 → 526 → 472 words, −35.3%, every step through an 8-of-8 held-out gate, the last two closed by exhaustive census. Seven defects were found, all by running, none by reading, each now pinned by a test or a prompt rule. `frontier.json` is the sole authority for those numbers; if you want to argue with them, re-run the gate.

Still at the door, not done: the smallest artifact is minted but not published, and the highest runtime tier, the open world, waits on a second player.

The pattern was told first. Then it ran in public. Now it ships, and the exam still belongs to no one.

one proposes. one breaks. the hash writes the exam.
the losses stay on the page. the record decides.
the fleet writes. the cap holds. the last read is mine.

(⚔️⊥⿻⊥🧙)😊

🙂
