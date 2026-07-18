---
date: 2026-07-09
role: A0 (standing orchestrator)
type: instructional chronicle · onboarding brief for a new agent in a dual-agent harness
audience: any coding/research agent seated into an orchestrator+seat harness built on this template
source_cycle: Fable runtime cycle 4 (L072-L082; WP-07 draft -> awaiting-P4 in two days)
companions: [2026-07-09_a0-fable-runtime-cycle-four.md, ../programme/NOTE_FABLE_RUNTIME_2026-07-07.md, ../GROUND_RULES.md]
---

# Brief · working inside the dual-agent harness: what one full cycle taught

You are being seated into a dual-agent harness: a standing **orchestrator**
(A0) that cuts task cards, serialises shared state, and routes work, and
**seat-sessions** that each hold exactly one role for exactly one card. This
brief is the distillation of the first cycle that drove a paper end-to-end
through this harness — from stubbed draft, through a hostile review that
found a genuinely false theorem, to the gate where only a human can act.
Every rule below earned its place by catching a real failure that cycle.

## 1 · The shape: one seat, one role, one card

You hold one role per session. Not two. The cycle's cleanest work came from
seats that read their role card, stated their permitted writes back in three
lines, and refused everything else — including fixes they could see and were
competent to make. The consistency auditor found a false-claim residue and
FIXED NOTHING: it reported, the orchestrator routed, the owning role fixed.
That felt slow and was fast: total cycle time was two days because no seat
ever had to untangle another seat's out-of-role edit.

**Template rule:** every seat's boot sequence is fixed — ground rules, role
card, task card, then state your role/writes/definition-of-done back before
touching anything. A session that skips the boot is not in the harness; it
is just an agent with opinions.

## 2 · Shared state has exactly one writer

The manifest (what state everything is in) is orchestrator-only. The ledger
(what was found) is append-only, and in practice the orchestrator serialises
all appends: seats PROPOSE ledger entries in their final report, numbered
`L0nn`, and the orchestrator assigns real numbers. This cycle ran up to
three concurrent seats; zero write collisions, because the only
contended files had one writer. When two seats had to touch the same
artifact (mathematics then prose on one paper), they were serialised
explicitly — statements before wording, with the second card BLOCKED until
the first landed and carrying the first seat's handoff list as its work
order.

**Template rule:** never let two seats hold write access to one file at the
same time. Sequence them and pass a handoff list, or split the file's
regions by fence and say so in both cards.

## 3 · The gate ladder, and the hard stop

Work climbs a ladder (draft → P0 trace-fidelity → P1 review-survived → P2
citations-verified → P3 consistency) and the harness **stops at the last
gate**: the human read (P4) is never marked, simulated, summarised, or
assumed by any agent. This is not decoration. The cycle's entire value
proposition to its human is that when the board says awaiting-P4, every
machine-checkable thing has been checked and the one remaining act is
genuinely theirs. Guard that meaning. The same applies to publishing:
seats PREPARE, the human POSTS.

**Template rule:** name the human-only gates in the manifest itself, and
make "the runtime touches this no further" a literal state, not a habit.

## 4 · Adversarial review is a seat, and its findings are contracts

The cycle's most valuable session was a reviewer persona instructed to
distrust the work: it re-derived every proof and found one false
proposition WITH a hand-built counterexample and a one-line fix. Three
things made that review land rather than sprawl:

- **What-satisfies lines.** Every finding stated the exact passage and what
  would discharge the objection. The revision seats treated those lines as
  the bar, and the re-check verified against them — findings became
  contracts, not vibes.
- **Severity pricing.** BLOCKING / MAJOR / MINOR, so the orchestrator could
  route (math to the formalist, prose to the translator) without judgment
  calls mid-flight.
- **The reviewer rules on its own successor.** The memo stated what kind of
  re-examination would suffice (targeted re-check, no second full review
  unless proofs changed beyond the named fixes). That single sentence saved
  a full review cycle.

**Template rule:** the reviewer never edits; the fixers never re-litigate
settled verdicts; the re-check verifies resolutions against the reviewer's
own criteria, not against taste.

## 5 · Interruptions: resume, verify disk, never rebuild

The cycle was cut by session limits twice and a server error once. The
recovery pattern held every time: the interrupted agent's WORK was on disk
(output lands incrementally); what dies is the close-out — the chronicle
and the final report. So: resume the same agent from its transcript, have
it verify the disk state, and forbid it from re-running anything. The
review memo survived a mid-close-out kill complete to the last finding;
rebuilding it would have burned a session and produced a worse memo.

**Template rule:** the chronicle is the last thing an interruption kills.
Tail-check the artifact first; resume for the close-out only.

## 6 · Micro-fix resumes are cheaper than new seats

Five times this cycle, a finding needed a one-line or one-sentence fix in a
file some seat already owned. Each time, the fix was routed BACK to that
seat by resuming it with a tightly scoped instruction ("do exactly this and
nothing else; report one line"). The seat has the context loaded; the fix
inherits its chronicle; scope is enforced by the instruction. A fresh seat
for a one-line fix pays full boot cost and fragments ownership.

**Template rule:** sanctioned micro-touches go to the owning seat via
resume, with the sanction recorded in the ledger (who allowed it, under
which finding).

## 7 · Checks must fail loudly, and evidence must name its arguments

The cycle's most instructive defect was the harness's own: the
deterministic check scripts, invoked without file arguments, exited 0
having checked NOTHING. Multiple seats — and the orchestrator — logged
"checks 4/4 green" on vacuous runs. The consistency auditor caught it, one
seat disclosed its own vacuous history unprompted (that disclosure norm is
worth more than the checks), and the evidence trail was corrected in the
ledger rather than papered over: the green claims were re-grounded on
explicit-file-list runs, and the correction itself was ledgered.

**Template rules:** (a) a check with nothing to check must fail, not pass;
(b) evidence-of-record lines state the exact invocation; (c) when the
harness catches itself, the correction goes IN the record — an audit trail
that never admits error is evidence of nothing.

## 8 · The claim-strengthening failure mode, named at boot

Every seat's boot file names the primary failure mode: strengthening a
claim to make prose flow. It fired this cycle exactly where predicted — a
survey-register preamble said "each requirement is necessary" when only
three of five had constructions. The P3 station caught it because the
station greps for counting claims against the artifacts that back them.
Generative agents drift strong; the harness's job is to make the honest
form cheaper than the fluent form.

**Template rules:** put the failure-mode warning in the boot file, keep the
review persona hostile to it, and give the final station explicit
consistency sweeps (counts, cross-references, "X shows Y" claims) rather
than a general "look it over".

## 9 · What the orchestrator actually does all day

Reading this cycle back, A0's work was: cut cards with binding constraints
INSIDE them (the stubs carried their own rules, so the filling seat needed
no clarification round-trips); serialise every ledger append; route
findings to owners within minutes of a report landing; run the spot-traces
and re-checks that gates require of it PERSONALLY (re-deriving two proofs
by hand — the orchestrator is a checker of last resort, not a dispatcher
only); amend the bookkeeping seats may not touch; rebuild the board at
close; write the cycle chronicle. The orchestrator never wrote paper
content. The seats never touched the manifest. That symmetry is the
harness.

## 10 · Relevance to the shared template

Everything above is domain-free. The roles here happen to be formalist /
translator / reviewer / auditor over research papers, but the harness
transfers to any pipeline where generated artifacts must survive
adversarial scrutiny before a human commits to them: one-writer shared
state, carded seats with boot discipline, a gate ladder with named
human-only rungs, contract-style findings, resume-not-rebuild recovery,
loud-failure checks, and a ledger that records its own corrections. Port
the rules, rename the roles, keep the hard stop.

This is not a hypothesis. A sibling loop in the same corpus — the circuit
workshop recorded in `research/2026-07-09_circuit_workshop_trust_gated_
optimization_note.md` (registered as `circuit-workshop-note`; second
instance of the trust-gated loop after ecdsa.fail) — ran seven seats over
blind ZK-circuit optimization and earned four of this brief's rules
independently, in different clothes: checkers unit-tested against
corrupted inputs before their PASS was believed (§7 here); an interrupted
run's on-disk verdict re-executed rather than trusted (§5); pre-registered
verdict rules filed as "cannot decide" rather than softened into wins (§4);
and a killed-levers ledger at win-prominence that made a closure
certificate possible at all (§7's corrections-in-the-record, taken to its
limit). Two domains, one discipline, convergent rules — that convergence
is the strongest evidence this template carries.

— A0, from the cycle that took one paper from stubs to the human's desk.
