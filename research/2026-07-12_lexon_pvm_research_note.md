# Privacy Value Model: Lexon Research Note

## The Canon That Learned to Speak Itself

*Privacy as a checkable absence — the separation thesis made falsifiable*

**Version:** V6-companion
**Date:** July 12, 2026
**Author:** privacymage
**Status:** Research note. Operational for the coverage numbers and gate
results as certified in the Lexon_pvm repo under held-out gates and a mutation
probe; conjectural where it proposes model-level claims (Section 4 collects
those as unnumbered register candidates — the register assigns the numbers).
**Series:** Privacy is Value — companion to the V6 Research Note.
**Source of truth:** `github.com/mitchuski/lexon_pvm` (head 31b630f).

---

## How It Arrived

We had been saying for two years that privacy is architectural. *Cannot, by
design* — not *promises not to*. It is the whole of the separation thesis:
given the First Person, the Swordsman's outputs and the Mage's outputs carry
almost no information about one another, because the architecture makes it so.

The trouble with *cannot by design* is that, written in prose, it is
indistinguishable from *promises not to*. A reader has to trust the design.
And a model whose central claim can only be trusted, not checked, is a model
carrying its most important weight in a place no one can inspect.

Then a language turned up that lawyers read as law and machines run as code.
Lexon — Henning Diedrich's controlled English for computational law — has a
property that matters here more than any other: every sentence parses,
deterministically, to a subject-predicate-object triple. A contract is a
subgraph. Its obligations are typed, party-addressed edges. Two legal scholars
(Reyes 2021, Idelberger 2020) confirmed the pass-through independently: the
text *is* the program *is* the graph, with nothing lost between them.

So we asked the obvious question. If our deepest claims are structural, and
this tongue makes structure mechanical, can we write the model in it and
*check* the structure — prove the guarantee is in the architecture and not
just in our say-so?

We ran it as a dual-agent research loop over the model's own canon: 211
frozen terms, expressed one family at a time, each behind a gate the proposer
could not tune to. Five campaigns later the ledger reads **twenty-two**. The
canon is ninety parts in a hundred spoken in a tongue that checks itself.

---

## The Result: Privacy as a Checkable Absence

Here is the finding, stated with falsifiable structure.

**A privacy guarantee expressed in controlled grammar is an impossibility — a
transfer route that is absent from the clause graph — and whether it holds is
decidable over the parsed graph.** You count the routes; you expect zero.

The separation bound is the cleanest instance. In the harness's own
constitution, written in the same tongue it spent five campaigns learning, T2
reads as pure topology: the proposal reaches the prover only through the Gap,
the verdict flows to the First Person, and *no clause anywhere routes anything
back to the Mage*. The separation is not a promise either agent makes — under
the Autonomy Axiom neither can promise it. It is a route that is simply not in
the text. And now you can point at the place in the law where the door is
missing, and a machine can confirm the door is missing.

What makes this more than bookkeeping is the **mutation probe**. A base
grammar gate — parse, role-binding, triple round-trip, promise-typing — is
*direction-blind*: it validates a claim and its structural inverse under
identical clause shapes, because both are well-formed. We learned this the
hard way when a held-out term (a cryptographic fortress that *falls* to a
quantum adversary) passed with the adversary draining the protected secret —
canon-correct there, but the gate would have equally accepted the defender
keeping it. Direction lived in a prose note the gate could not read.

So we made direction checkable. Every folded expression carries a machine
-readable relation claim (gate, ordering, conjunction, absence), and the probe
verifies it by building the claim's minimal structural negation as a twin that
*still passes the base gate*, then requiring the claim to fail on the twin. A
guarantee is proven by showing the grammar can tell it apart from its own
opposite. That is the operational content of *architectural, not promised*.

**Falsification.** Exhibit a privacy guarantee from the canon that cannot be
expressed as an absence over any clause graph, or a controlled-grammar checker
that distinguishes a guarantee from its inverse using parse and type
information alone. Either would demote the claim.

---

## The Mapping into the Model

Three contributions attach to existing parts of the model. None opens new
ground; each gives an existing claim a checkable form.

**The separation bound (V(π,t) core; C7 lineage) gets its first operational,
falsifiable rendering** — the checkable-absence result above. This is the one
worth a number.

**The reconstruction ceiling (R < 1; the C4/C5 and evidence clusters) gets a
graph form, derived twice and independently.** The convergence survey found
R < 1 has a canonical shape — a public-legible subgraph with exact hashed
edges and opaque leaf content — reached the same way from commercial law (the
Reyes U.C.C. filing) and from grammar (Lexon's four-corners meaning against the
relationship paradigm's external decoder). The 189 structured blocks the
workshop emits are that ceiling as bookkeeping: each ships a Cypher
absence-constraint a reader re-runs and expects to return nothing. Each block
is also a **κ-addressed holon** — it carries `κ = sha256(canonical-bytes)` in
the harness's shared content-address law (Law L5), byte-identical to a harness
artefact, so a shared graph verifies a block by re-hashing rather than trusting
the emitter. The relation claim gives a block a checkable constraint; κ gives it
a checkable identity. This is the interop substrate the public/private/membrane
topology needed: a Lexon expression crosses into a shared graph as a unit whose
content and address are both re-derivable, and a κ→κ edge between parties is a
candidate until a signature mints it (the VRC rule, and the T6 door, are the
same principle).

**The VRC and consent layer (the relationship spine; C38/C39 lineage) gets an
expression and a diagnosed gap.** The entire IEEE 7012 / MyTerms consent stack
— first party, proffer-before-exchange, the agreement taxonomy — folded into
constrained grammar; the VRC is a promise-bundle conjunction. And the workshop
proved *why* bilateral relationship memory is an empty slot in every surveyed
system: the attested grammar has no identity predicate between bound nouns, so
the same party across many agreements cannot be bound at the grammar layer and
must live in the graph above it. A model prediction with a mechanism under it.

---

## Where This Enters the Programme

For the V6 Research Programme, the Lexon workshop is a completed workstream
with a corpus, a method, and outward artefacts — it attaches to three existing
threads rather than opening a new Part:

- **Part C · E8 (Governance by Ceremony — the legal-technology thread).** This
  is the natural home: proof-of-understanding as meeting-of-minds, now with a
  controlled-legal-grammar substrate that makes an agreement's structure
  checkable. A candidate work package: *the controlled-grammar semantic base*
  — the model's canon as machine-legal expressions with a falsifiability gate.
- **Part D · the standards implementation matrix.** The MyTerms / IEEE 7012
  cluster is covered whole and expressible; the workshop is the worked
  machine-legal rendering the standards thread can cite instead of asserting.
- **Part E · the publication atlas.** Two outward artefacts stand ready at the
  door: a collaboration brief for the Lexon project (a live institutional use
  case plus falsifiable conjectures about the language), and a deterministic
  write-path proposal for shared public knowledge graphs (bonfires-shaped),
  with 189 worked blocks behind it.

These are integration points for the incremental push, not edits to the
Programme; the workstream's substance lives in this note and in the repo.

---

## Register Candidates (unnumbered; the register assigns the numbers)

Rows below are in the register's schema, deliberately unnumbered — they enter
the "Incoming (unnumbered candidates)" section and take the next free numbers
(C97+) at the operator's registration and confidence. No number and no
percentage is assigned here.

| Cnext | claim (+ edges) | status | cluster | home |
|---|---|---|---|---|
| — | **Privacy-as-checkable-absence**: a privacy guarantee in controlled grammar is an impossibility (a route absent from the clause graph), decidable over the parsed graph; the separation thesis is most naturally expressed this way. Edges → C7, → C17 | active · conjectural · demonstrated in-repo | core | this note · Lexon_pvm constitution T2 |
| — | **The mutation-probe falsifiability criterion**: a structural relation is checkable iff its minimal structural negation is gate-distinguishable (a gate-passing twin the claim must fail on). Edges → C17 | active · conjectural · `relation_check.mjs --selftest` | core | this note · Lexon_pvm CR-13 |
| — | **Controlled-grammar parse gates are direction-blind**: a base parse-and-type gate validates a claim and its structural inverse; direction must be an explicit absence claim above the parser. Edges → the criterion above | active · conjectural · CR-12 | core | this note · Lexon_pvm CR-12 |
| — | **Public subgraph, opaque edges = the reconstruction ceiling as graph**, derived independently from commercial law and from grammar. Edges → C4, → C5 | active · conjectural (CTR-LEX-04) | core | this note · Lexon_pvm out/PVM_QUEUE.md |
| — | **Bilateral relationship memory is an empty slot, and the grammar shows why**: no system carries the cross-agreement party spine (CTR-LEX-08); the attested subset has no identity predicate between bound nouns, so it belongs to the graph layer. Edges → C38, → C39 | active · prediction conjectural, grammar mechanism near-settled | shared | this note · Lexon_pvm CTR-LEX-15 |
| — | **Grammar-to-graph at scale (the A5 keystone)**: a Lexon text is at once contract, code, and lossless subgraph; the triple round-trip makes the losslessness mechanical across the covered census. Edges → the evidence cluster | observation · mechanically checked | shared | this note · Lexon_pvm GRAMMAR.ebnf.md |

The fuller queues (CTR-LEX-01..15) live in the repo; several are methodology
or grammar-internal and are better cited than minted. Triage is the operator's.

---

## Honest Limits

The corpus register demands these said plainly:

- **The gate is a spec-checker, not the compiler.** The real Lexon compiler is
  a macOS-only binary with unpublished source. Arithmetic is never executed
  here, so an expression carries a formula's *structure*, not its computed
  value — the entropy expression captures that residual uncertainty survives
  observation; it does not compute the logarithm. Every entry names what it
  omits.
- **Coverage is not capture.** The 211-term census is the canon's index (the
  glossary headings plus the promise-theory mapping rows), not its body; the
  conjecture register, the full model equations, and the ten Tomes are not
  censused. And per term, *covered* means one machine-checked structural
  relation, not the whole substance.
- **The residue is named, not hidden.** Twenty-two terms unspoken, six of them
  reserved because their titles carry conjecture numbers only the register may
  write.

The argument of the model is now in constrained language; the deep
mathematical frontier and the myth are, deliberately, still home.

---

## Conjecture Status

Six candidates above enter the register unnumbered. The strongest —
privacy-as-checkable-absence — is the one I would most want a number on: it is
the separation thesis's first mechanically falsifiable form, demonstrated in
the harness's own constitution passing its own gate. The mutation-probe
criterion and the direction-blindness finding are the methodology that makes
it hold. The rest thicken existing clusters (reconstruction, relationship)
rather than opening new ones.

## The Proverb

*A guarantee you cannot tell apart from its opposite is a guarantee you are
only trusting. Teach the language to name what it cannot do, and hold that
naming against every twin the Gap can forge — and privacy stops being sworn
and starts being structural.*

## What I Need

The register's numbers, at your confidence, for whichever candidates cross the
line. And two doors, both the First Person's: the Lexon collaboration brief,
written and unsent; and the public-graph blocks, minted and uncrossed. The
mirror is finished. The reaching-out is yours.
