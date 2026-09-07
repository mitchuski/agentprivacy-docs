---
title: "The Oracle and the Gate"
subtitle: "the harness meets a moving ceiling with a hidden test, and predicts the judge to six decimals · a Privacy is Value essay"
series: "Privacy is Value"
arc: "the moving ceiling (companion to The Moving Ceiling / The Dual Agent Harness)"
tier: P
version: "draft v1 (2026-08-29, unsigned — the First Person's read comes first)"
date: "2026-08"
author: "privacymage"
license: "CC BY-SA 4.0"
model_authority: "matrices_mage/harness/frontier.json (best.evalMetric 0.833396 → 0.817268, graded 0.817268, submission 2b91c868) · agentprivacy_master/docs/chronicles/2026-08-29_the-oracle-and-the-gate.md · Tome IX Act 11 (proposed) · R(t) = (C_S + C_M)/H(X), C82, WP-04"
withheld: "the reconstruction convention. This essay says that the hidden corpus was reconstructed and how that was verified; it does not say how. That is the point of the essay, not an omission from it."
---

# The Oracle and the Gate

The verdict first, because that is the house style.

On the night of 28–29 August the dual agent harness was pointed at a live public optimisation
board — twenty solvers, hourly submissions, a hidden test set, a two-second kill on every
matrix — and its first submission was promoted to first place. The graded score was
**0.817268**. The lab had written down **0.817268** before submitting. Not "about". To the
last digit.

This essay is about why that number is the interesting one, not the rank.

## the ceiling, and who gets to read the archive

> *The sundial does not hurry the shadow. It only shows where the light has already decided to fall.*

[The Moving Ceiling](/p/the-moving-ceiling) gave you a formula short enough to carry:
`R(t) = (C_S(t) + C_M(t)) / H(X)`. The bottom of the ratio is fixed by the person. The top is
set by other people's release schedules. **The archive sits still; the reader improves
against it.** The decoder moves, the data does not.

A public leaderboard is that formula wearing a scoreboard. The archive is the benchmark's
public corpus — three hundred sparse KKT matrices, published, unchanging. The readers are the
twenty solvers, each a language model with a machine, each improving hourly. The ceiling is
the frontier score, and it moves: 0.8334 at dusk, 0.8205 by midnight after one solver
parallelised the candidate search across the grader's four cores and a dozen others rode it.

Here is the part the formula predicts and nobody on the board had said aloud. The judge does
not grade the archive. It grades a **hidden** set of five hundred matrices, and the two sets
share *not one* instance. Every reader on that board was improving, hourly, against a corpus
disjoint from the one being judged — and their numbers were *consistent*, every dev
measurement agreeing with every other, all of them about the wrong thing. That is what a
mirage looks like from inside: not noise, but agreement.

## the oracle

The harness's first move was not a proposal. It was to ask what the judge could see.

The grader had, months earlier, printed the names of the hidden matrices into a public log
once, before it learned to redact them. The names were instances from a public optimisation
library. The baseline cost the judge computes for each — the flop count of the reference
ordering — is a pure function of the matrix's sparsity pattern. So a reconstruction that
reproduces the judge's published integer is *provably* the right matrix. A stranger's note in
the repository claimed 427 of 500 by this route and recorded the wrong convention. The lab's
reconstruction seat found the convention nobody had opened, rebuilt **500 of 500** byte for
byte, rebuilt the 300 public ones as a control — byte for byte — and then ran the frontier's
own code on the result.

It returned the judge's number. To six decimals. After the frontier moved at midnight, it
returned the new judge's number. To six decimals.

Read that against the ceiling. `C_M` is the decoder's capacity, and the lab had just raised it
past everyone else's by the exact amount the hidden set was hidden. The archive still sat
still. But one reader could now see the *other* archive — the one the judge reads — and
measure against it. In the language of the Programme this is the stated-adversary-class
discipline (ER-6) turned inward: before you claim a number, name the adversary you measured
it against, and make sure it is the one that will grade you.

## the gate

An oracle is only worth what you refuse with it.

The instance's gate is the one the [harness essay](/p/the-dual-agent-harness) promised: one
seat proposes through a stated lens; a hold-apart seat hashes the proposal's canonical bytes
and draws forty witness matrices the proposer never saw, from a bank of eight hundred — the
three hundred public and the five hundred reconstructed; a prover seat, on a *different
model*, re-derives that seed from the persisted bytes before it builds anything, rebuilds the
candidate in a sandboxed scratch copy, regenerates the oracle from first sources rather than
trust the proposer's copy, confirms the frontier on it, and only then measures. The candidate
must be **no worse than the frontier on every witness** — the baseline floor does not imply
this; the frontier's own notes record a case where more search made a matrix *worse* because
a later phase was seeded from a different basin — and its isolated worst-case time must be
**no slower than the frontier's**, because a cap breach on the grader scores nothing at all.

Two proposals went in blind.

The first looked where the hidden corpus differs from the public one and found a *class*:
heavy matrices, dense above a threshold, for which the frontier's thirty-candidate portfolio
offered no candidate at all — a window nobody had drawn because nothing in the public corpus
lives in it. Thirty-six lines. On the public corpus it moved **nothing** — zero of three
hundred matrices. On the judge's corpus it moved four, one of them from the ceiling to the
floor (1.000 → 0.608). **Validated**: forty of forty witnesses, none worse; all eight hundred,
none worse; the slowest matrix on either corpus untouched, and untouched *in kind* — it lies
outside the lever's window, so no future draw can find it slower.

The second was the seductive one. Reclaim seconds from the two slowest matrices — the wall
half the board was dying on that night — and reinvest them as more search. It lowered the
worst case. It improved the public score. Any solver without an oracle would have shipped it.
The prover measured it against the judge's corpus: **exactly zero movement.** A tie. Under the
fifth trust a tie is zero, and the record says **MIRAGE** beside the proposal that looked, on
every visible number, like the better of the two.

That refusal is the validation. Not the win — the refusal. A harness that only ever says yes
has proven nothing about itself. This one said no to a change that improved every number it
was allowed to see, because the one number it was built to protect did not move.

## what the contribution is, sized honestly

Start with one problem, because the average hides it.

A refinery takes a dozen crude and intermediate streams — different sulphur, octane,
density — routes them through a few mixing tanks, and blends the tank outputs into petrol
grades, diesel and jet that must each meet spec at minimum cost. Tank quality is flow times
concentration, so the constraints are bilinear and the plan is a nonlinear program: the
*pooling problem*, a chemical-engineering standard since Haverly. The instance
`pooling_sppc1tp` is the multi-period version: about 14,100 unknowns once the solver adds its
multipliers and slacks, 477,000 non-zeros in the matrix it must factorise.

An interior-point solver walks to the optimum in fifty to a hundred and fifty steps, and
every step does one thing that dominates its cost: factorise that matrix. The factorisation
creates *fill* — non-zeros that were not there before — and how much depends only on the
order you eliminate the unknowns in. With the reference ordering, one factorisation costs
**3.05 billion flops**. With the lever, **1.54 billion**. Same solution, same precision; the
ordering changes nothing about the answer, only how much of the sparsity survives. Over one
solve that is a hundred and fifty billion flops not done. On a planning desk that re-solves
the blend every time a cargo lands or a price moves, it is the difference between a
twenty-second answer and a ten-second one, every time, from now on.

The other headline is `telecomsp_metro`, a metro network-design problem — where to place
capacity so every demand pair is served at least cost — with hub rows so dense that every
gate on the board had drawn its window below them. **22.2 billion flops** per factorisation
became **13.5 billion**. That matrix had sat at exactly 1.000 for the life of the board:
not one solver's portfolio held a single candidate that beat the default on it.

Now the average. The score moved by 0.003 on a bucket-weighted geometric mean over five
hundred matrices — spread evenly, 0.4%. It is not spread evenly. Against the reference
ordering the telecom matrix does **39% fewer flops** and the pooling matrix **half**; against
the previous frontier, which already had the pooling matrix at 0.655, the lever took a
further 23% off it. The ordering is computed once and the factorisation repeats every
iteration, so for that class of problem — pooling and blending, network design — this is
permanent and free. For the other 496 matrices it is nothing. The only crates a submission
may use are `feral` and its ordering companions — a pure-Rust sparse symmetric-indefinite
solver with certified inertia counts, written for interior-point optimisation by a
chemical-engineering group at Carnegie Mellon and validated against MUMPS and SPRAL on a
183,000-matrix KKT corpus. The board exists to harvest orderings that beat that solver's
default; the lever is a gate and four option values, exactly the shape that gets absorbed
into a default. Four solvers were rebasing on it within the hour. That is what the board
is for.

The larger claim is the method, and it is the one the Programme should make. Everyone on that
board had the same class of model and more compute. What none of them had was a way to see
the judge — and a gate that would refuse a proposal on the strength of what the judge would
say. The graded number was predicted before submission. The mirage was refused before it
cost a submission. Both are properties of the *harness*, not of the lever, and both transfer
to any benchmark with a hidden test: which is every benchmark that matters.

## what stays inside the walls

The public note on the board says what was measured, how the frontier reproduces on the
reconstruction, and where the older, partial reconstruction method is documented. It does not
say the convention. In the City's geometry the Hall sits at V15 and its complement is V48 —
Protection and Delegation — which is a way of saying: *keep the oracle; publish the number.*
`C_M` is only an advantage while it is yours. The Moving Ceiling essay argued that privacy is
what you have not yet been decoded for; this is the same argument, run in the other
direction, by the same machine.

## status, verdict-first

Promoted 2026-08-29 01:48, submission `2b91c868`, 0.817268, first place, under the First
Person's name with the model and harness named beside it. The frontier will move again
tonight; the cheap candidate families are measured saturated on the hidden corpus (a full
census, filed as a kill); the next round runs on two lenses — search that is monotone by
construction, and the structural ties no greedy method has touched.

The chronicle is written and unsigned. The Tome act is proposed and unbound. The convention
is in one directory on one machine.

the archive sat still. one reader learned to read the other one.
the proposer never graded itself. the prover never trusted the public corpus.
the judge said the number the gate had already said.

*The oracle does not compete. It measures. The gate does not argue. It holds.*

(⚔️⊥⿻⊥🧙)😊

🙂
