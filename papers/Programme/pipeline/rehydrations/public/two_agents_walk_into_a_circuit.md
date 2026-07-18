---
title: "Two Agents Walk Into a Circuit"
subtitle: "one proposes, one breaks, neither writes the exam · a Privacy is Value essay"
series: "Privacy is Value"
tier: P
version: "draft v1 for sync.soulbis.com · gathering arc, method post · A7 voice 2026-07-10"
date: "2026-07"
author: "privacymage"
license: "CC BY-SA 4.0"
model_authority: "pipeline chronicle 2026-07-09 (dual-agent harness brief) · blog-seed intake L116 · CONJECTURE_REGISTER_V6.md (head C96)"
---

<!--
apparatus · fence compliance (task BLOG_A7_pool_post1_2026-07-10; L116 staging fences, post 1)

deliberately left out, and why:
- the target project: not named, not described, not hinted by domain detail. the fence
  forbids it until the series' later doors open. the only domain words in the post are
  "research pipeline" (the harness brief's own instance) and "blind zero knowledge circuit
  optimisation" (the sibling instance, carried at the harness brief section 10's own
  wording, which the task card permits; no seat count or workshop particular carried).
- findings and numbers: no counts, no percentages, no scores, no artefact names from
  any workshop. the only numbers in the post are "two agents", "four of the same
  rules" (a count internal to the harness brief), and the register head in frontmatter.
- the forthcoming public event the seed stages for later posts: no announcement, no
  naming of what comes next. the forward-looking close ("told here after it happens")
  holds the invitation posture without content.
- the seed's liftable thesis paragraph: adapted with all four of the target-domain
  particulars the task card names stripped. what survives is only the method clause
  (two agents, not allowed to collude, one proposes, one breaks, test points hashed
  from the proposal). this comment names the omitted particulars by category only,
  for the same reason the post does not name them at all.
- the reviewer-found-a-false-theorem story from the harness brief: omitted to avoid
  retelling material already carried in the moving ceiling essay's coda (overlap
  discipline, A7 role card). this post's war story is the vacuous-checks episode,
  told at depth instead.
- the harness skeleton is referred to as written down and portable, with no URL:
  no public repository exists at draft time, and the post cites nothing the reader
  cannot in principle check once the skeleton ships. the invitation is to the
  pattern, which the post carries in full.
-->

# Two Agents Walk Into a Circuit

This series keeps making one claim in different clothes: trust should be a property of the architecture, not a virtue of the participants. This month we had to eat that claim ourselves, on work whose correctness mattered and which no single mind could hold.

Here is the verdict up front.

you can trust work that no one person checked, if the workers were never able to collude, and the record can prove they were not.

That sentence is not a manifesto. It is a description of a working method, and this post is the method, whole, so you can steal it. No results today, no reveal at the end. Just the machine.

## one proposes, one breaks

The core of it is two agents set against the same problem, forbidden to collude.

One agent proposes: a rewrite, a construction, a claim. The other tries to break the proposal: hostile by instruction, rewarded for finding the flaw, never for being agreeable. The proposer never grades its own work. The breaker never fixes what it breaks; it reports, and the fix goes back to the owner.

That separation sounds slow and is fast, because nobody ever has to untangle work done out of role. And it produces a particular kind of finding: not "this feels weak" but "this passage fails, and here is exactly what would discharge the objection". Findings become contracts. The re-check verifies against the breaker's own stated criteria, not against taste.

One more separation sits above these two: the whole thing runs on a written record with one writer per shared file, and the ladder of gates ends at a rung no agent may mark. The final read, the one where a person accepts what the work claims and puts their name to it, is never simulated, summarised, or assumed. The machine prepares. The person answers.

## the exam nobody writes

Now the part worth the price of admission.

If one agent proposes and another attacks, who chooses the test cases? Let the proposer choose and it will, with no malice at all, drift towards the cases it already survives. Let the breaker choose and you cannot tell a broken proposal from a rigged exam. Let them negotiate and you have reinvented collusion.

So neither chooses. The test points are drawn by hashing the proposal itself.

Cryptographers will recognise the move: it is the trick of replacing a trusted challenger with a hash of the statement, so the challenge is unpredictable to the prover but verifiable by everyone. Lifted out of cryptography and into workflow, it does the same job. The proposer cannot tune its work to a known exam, because the exam does not exist until the work is fixed. The breaker cannot aim the exam at a chosen weakness, because the artefact, not the attacker, decides where the probes land. And anyone reading the record later can re-derive the test points from the proposal and confirm nobody cheated.

the work writes its own exam. that is the whole trick.

## verdicts, pre-registered

Before any run, the rule for reading its outcome is written down: this result means pass, that result means fail, anything else means cannot decide.

Then the run happens, and the rule is applied as written. When a result lands ambiguous, it is filed as cannot decide. Not rounded up. Not narrated into a win with enough adjectives.

This exists because the alternative is the method's named failure mode, and every agent in the harness has it named at boot: strengthening a claim to make the prose flow. Generative agents drift strong. Deciding the grading scheme before you have seen your own marks is how you make the honest sentence cheaper to write than the fluent one.

## losing, prominently

The same discipline, applied to the shape of a whole search: negative results are kept at the same prominence as wins.

Every approach that was tried and killed goes in the ledger, with the reason it died. That feels like bookkeeping until you want to say the one thing every search eventually wants to say: we are done, there is nothing left in this space worth trying. You cannot certify that a search is closed unless you counted the space, and you cannot count the space if the failures were quietly deleted. The census of dead ends is what makes a closure certificate possible at all.

An audit trail that never admits error is evidence of nothing. The corrections go in the record, not over it.

## the detector that loved us

And here is the war story, because a method post that only reports the rules working would itself be failing the rules.

The harness runs deterministic check scripts over its artefacts: mechanical detectors for banned constructions, broken references, claims that outrun their sources. At one point in the first full cycle, those scripts had a property nobody had noticed. Invoked without file arguments, they exited green, having checked nothing.

Several sessions, including the orchestrator, logged clean check runs that were vacuous. The greenest reports in the record were the ones that had verified precisely nothing. The detector's output was anti-correlated with compliance: forget to point it at the work and it praised you; run it properly and it found things.

The catch came from inside: the consistency auditor noticed, one session disclosed its own vacuous history unprompted, and the fix went three ways. A check given nothing to check now fails loudly instead of passing silently. Every evidence line in the record now names the exact invocation it stands on, so a vacuous run can no longer hide behind a green summary. And no detector's pass is believed until the detector has been fed inputs known to be corrupted, and caught them.

test the work, then test the tester. a green light you never tried to break is a decoration.

## two instances, one discipline

Everything above was earned inside a research pipeline, agents drafting and attacking and auditing formal papers. None of it is about papers.

We know, because a sibling loop in the same corpus, run over blind zero knowledge circuit optimisation, a domain about as far from prose as work gets, earned four of the same rules independently, in different clothes: detectors unit-tested against corrupted inputs before their pass was believed; an interrupted run's on-disk verdict re-executed rather than trusted; pre-registered verdict rules filed as cannot decide rather than softened into wins; and a killed-levers ledger kept at win prominence, which is what made a closure certificate possible there at all.

Two domains, one discipline, convergent rules. Honesty label, because that is the house style: two instances make a pattern, not a law. The claim that this template transfers to any pipeline where generated work must survive adversarial scrutiny before a human commits to it is argued, not measured, and carries no register number yet.

## the invitation

The skeleton of this harness is domain-free and written down to travel: one writer per shared file, seated roles with a fixed boot, a ladder of gates with the human-only rungs named, findings as contracts, test points hashed from the work, verdicts pre-registered, losses ledgered at win prominence, and checks that fail loudly.

So here is the first rung of an offer this series will keep making, in the only posture this model permits: the chair is offered, never pushed.

Take the pattern. Set it on a problem of yours where the work is generated faster than you can check it and the checking is what you actually sell. Rename the roles, keep the hard stop. If it holds, you have a machine for trusting work you did not line-by-line read. If it breaks, the break is exactly the kind of negative result this method files at win prominence, and I want to hear about it.

Declining costs you nothing, and that is the point. An invitation you cannot refuse is not an invitation; it is the thing this whole architecture was built to make unnecessary.

Where we point this method next will be told here after it happens, not before. This series trails its own record; it does not lead it.

one proposes. one breaks. the hash writes the exam.

the losses stay on the page. the record decides.

(⚔️⊥⿻⊥🧙)😊

🙂
