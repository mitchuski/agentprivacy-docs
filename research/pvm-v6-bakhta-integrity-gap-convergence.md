# Privacy Value Model: V6 Research Note

## Convergence on the Integrity Gap — Bakhta's *Safety by Design* read against the Dual Model

*Two builders, opposite ends, one recognition*

**Version:** V6.x-conjecture (Bakhta integrity-gap convergence)
**Date:** June 4, 2026
**Authors:** privacymage / Soulbae (Mitchell · mage@agentprivacy.ai), with Claude: ORCID iD: 0009-0001-6557-9135
**External work under reading:** Abdelhamid Bakhta (StarkWare), *Toward High-Assurance AI Safety by Design for Autonomous Systems*, April 2026
**Status:** Research note — convergence record. Synthesizes the standalone convergence letter (`convergence-note-bakhta.md`) with the source manuscript into one artefact.
**Depends on:** V5.4 Formal Specification (v2.0), V6 ARCH-1R/T Operational Reachability Note, Promise Theory v1.5
**Relation:** Distinct from [The Bakhta Half-Life of Trust](./pvm-v6-1-bakhta-half-life.md) (C30–C33), which reads Bakhta's *earlier* cryptographic-half-life work. This note reads the *April 2026* high-assurance paper.
**Extends:** adds C70–C73 (candidates · provisional against the live register)
**Erratum 2026-06-10 (Run 0 register lock):** the provisional numbering C70–C73 below is confirmed as **C77–C80** in `CONJECTURE_REGISTER_V6.md` (C70–C71 were taken by the Horizon District set; C72–C76 by ARCH-1R/T). Read C70→C77 · C71→C78 · C72→C79 · C73→C80.
**Series:** Privacy is Value
**Source PDF:** `Toward High-Assurance AI Safety by Design for Autonomous Systems.pdf` (169 KB, this directory)

---

## How It Arrived

Abdelhamid Bakhta's high-assurance paper (StarkWare, April 2026) names a single cross-cutting weakness in AI safety: **the integrity gap** — the structural distance between what a deployer *claims* about an AI system's behavior and what an outside party can *independently verify*. The paper's load-bearing move is to call that gap **architectural rather than procedural**: independent verification is infeasible by deployment structure, not merely unexercised.

Read on its own, the paper is a clean infrastructure vision. Read against the Dual Model, it is a **convergence** — the same recognition the PVM has been building from the opposite end. Bakhta builds an evidence stack that faces a *third party* and narrows where trust must be placed. The PVM builds a relationship model that faces *the other agent* and treats where trust must be placed as the thing being *valued*. Neither cites the other into position; both arrived because the place is real.

This note records that convergence before it dissolves into mere agreement and stops being useful. §1 summarizes the manuscript. §2 records the four load-bearing intersections. §3 is the productive disagreement. §4 is the open question carried back to Bakhta. §5 registers candidate conjectures. The original letter is preserved verbatim in the Appendix.

---

## §1 · The Bakhta Manuscript in Brief

**Thesis.** As AI moves from advisory roles into agentic, physically embedded, and regulated deployments where failure is not recoverable, empirical evaluation / interpretability / process controls remain *necessary but cease to be sufficient*. Such settings require **safety by design**: a deployment-time evidence architecture whose composed output is an **assurance bundle** that a third party can evaluate without access to the provider's weights or operational logs.

**The assurance claim ladder** (three nested levels; conflating them is a category error):

| Level | Claim | Borne by |
|-------|-------|----------|
| **L1 · Execution integrity** | The advertised model ran on the advertised input and produced the observed output | Verifiable computation, attestation |
| **L2 · Bounded-property satisfaction** | A formally specified behavioral predicate holds under explicit assumptions | Formal specification + verification (L1 is a precondition) |
| **L3 · Safety in the world** | The deployed system causes no harm the safety argument was meant to exclude | *No stack substitutes* for alignment, oversight, governance — the stack makes residual risk the *explicit subject* rather than the whole argument |

The field has immature infrastructure at L1–L2 and so treats L3 on trust. A structural limit divides L2 and L3: **the specification-intent gap (§4.1)** — a finite formal spec `Φ` can be satisfied by a system that violates the intent it was meant to capture (Goodhart applied to behavioral contracts).

**The five-layer stack** (compositional, not sequential):

1. **Formal safety specifications & verification** — translate behavioral requirements ("must not exceed delegated authority") into machine-checkable form. Currently the hardest layer; specifying rich open-world behavior remains largely unsolved.
2. **Verifiable computation** — ZK-proofs of inference: prove a committed model ran on a committed input. Proof-carrying-code lineage; certifies *that a tensor executed*, not that it *should have been trusted* (that is L1's obligation handed to Layer 1).
3. **Attestation, roots of trust, provenance** — hardware root of trust + measured firmware + input provenance: it ran *on this device, over inputs with this recorded history*.
4. **Privacy-preserving computation** — FHE / MPC: inference over sensitive inputs without exposing them, while still supporting verifiable outputs. Resolves the otherwise-forced trade-off between verifying the computation and protecting the inputs.
5. **Safety cases** — the integrative layer: a structured argument binding the artifacts (proof certificates, attestation reports, provenance manifests, privacy guarantees) into a bounded deployment-assurance claim with explicit assumptions and residual risks. Makes the *judgment structure inspectable*, not L3 machine-checkable.

**The assumption set A.** The bundle carries an explicit `A` — operational design domain, hardware trust model, specification faithfulness, residual risks — under which the evidence is valid. The bundle is "as strong as the weakest adversary assumption in its construction"; `A` is the object that must be carried and renegotiated as a deployment evolves. Crucially, **in Bakhta's architecture `A` is unilateral**: the provider holds it, the auditor inspects it.

---

## §2 · The Convergence (load-bearing)

Four intersections are structural, not thematic.

**1 · The integrity gap *is* the privacy-that-scales / privacy-that-hides distinction.** Bakhta's claim that the obstacle is *architectural, infeasible by structure rather than merely unexercised* is the exact sentence the Dual Model turns on: the separation between privacy that scales and privacy that hides has to be **topological**, not a matter of policy. Same object, named from the proof side (Bakhta) and the relationship side (PVM).

**2 · The specification-intent gap (§4.1) is the irreducible promise.** Bakhta states specification gaming as observation, not theorem, on the explicit grounds that *behavioral intent is not a formal object* — a finite `Φ` is at best a proxy and no further proof against an unchanged `Φ` closes the distance. In PVM terms this is the **irreducible promise**: the boundary between what can be formalized and what can only be held between two parties. Bakhta names it as where formal methods hand off to alignment. PVM names the *same place* as **where value lives**. One object, seen from the proof side and the relationship side — held at ~60%, with the divergence in what each does with it being the interesting part.

**3 · The composition problem (§6) is recursive proof composition across providers.** Bakhta's open composition item — assembling assurance across providers under different trust models at runtime — is, in PVM vocabulary, *recursive proof composition across providers under different trust models, assembled at runtime*: the hardest open item on the PVM list, and Bakhta's framing is the cleaner statement. **If the assurance stack and the relationship model share one technical frontier, this is it.**

**4 · Layer 2 respects the same boundary the proverb speaks.** Bakhta is precise that a proof of inference certifies a committed tensor ran on a committed input and says *nothing* about whether it should have been trusted. The convergence proverb — *"i can verify i serve you without remembering i was you"* — is that same boundary spoken from inside the system: **completeness and soundness about what was done, zero knowledge of origin or intent.** Exact agreement on where the proof stops; productive disagreement about what stands on the other side.

---

## §3 · The Productive Disagreement (design, not dispute)

The two architectures point in opposite directions, and that is the value, not a defect.

| | Bakhta's stack | The Dual Model |
|---|---|---|
| **Faces** | a third party (verifier / auditor / regulator) | the other agent |
| **Treats the trust-locus as** | the thing to be *minimized* | the thing to be *valued* |
| **Move** | *closing* the gap | *building upon* the gap |
| **Register** | proof side | relationship side |

Both are the right move for their audience. The two registers should be kept distinct rather than merged into a weaker third thing — Layer 2's stopping point is precisely where the PVM's value-bearing surface begins.

---

## §4 · The Open Question (carried back to Bakhta)

Bakhta's assumption set `A` is **unilateral** — a document the provider keeps and the auditor inspects. In the Dual Model, "what each side is relying on" is exactly a **bilateral credential**: attested by both, verifiable by anyone, forgeable by neither.

> **The question:** does `A` want to stop being a document the provider keeps and become a relationship the two parties co-sign? If it did, the distance between provider and verifier would itself become something neither could quietly rewrite.

Unproven that it buys anything the safety case does not already give — but it likely does in the **multi-provider case**, which is exactly where §6's composition problem bites. This is the concrete item to put to Bakhta.

---

## §5 · Candidate Conjectures

Numbers continue the live register (provisional against head; the sibling ARCH-1R/T chronicle of 2026-06-04 advanced candidates C67–C69 — **confirm both ranges before pinning**).

| ID | Claim | Confidence |
|----|-------|------------|
| **C70** | Bakhta's *integrity gap* (architectural infeasibility of independent verification) and the PVM's *privacy-that-scales vs privacy-that-hides* separation are one object: a topological, not procedural, distinction. The two literatures converged independently because the separation is real. | ~60% |
| **C71** | The specification-intent gap (§4.1) and the PVM's *irreducible promise* are one object seen from two sides — the proof side (where formal methods hand off to alignment) and the relationship side (where value lives). Behavioral intent's non-formalizability is the load-bearing premise of both. | ~60% |
| **C72** | The shared technical frontier of the assurance stack and the relationship model is *recursive proof composition across providers under heterogeneous trust models, assembled at runtime* (Bakhta §6 = PVM's hardest open item). Progress on either is progress on both. | ~45% |
| **C73** | Promoting Bakhta's unilateral assumption set `A` to a **bilateral co-signed credential** (attested by both, verifiable by anyone, forgeable by neither) yields a strict assurance gain in the multi-provider case, by making the provider–verifier distance non-unilaterally-rewritable. Null or marginal in the single-provider case. | ~35% |

---

## §6 · What This Note Does NOT Do

- It does **not** claim the assurance stack resolves alignment or substitutes for governance — Bakhta himself does not, and L3 remains a trust/judgment surface by his own ladder.
- It does **not** merge the two architectures. The productive disagreement (§3) is preserved on purpose; collapsing proof-side and relationship-side registers produces a weaker third thing.
- It does **not** raise confidence on the generative PVM conjectures. C70–C73 are *convergence* conjectures — claims about shared structure with an external framework — not new results about the model.
- The two ~60% identifications (C70, C71) are deliberately not pushed higher; the divergence in what each side *does* with the shared object is where the work is, not in forcing equivalence.

---

## References

- Bakhta, A. (2026). *Toward High-Assurance AI Safety by Design for Autonomous Systems.* StarkWare, April 2026. [Source of this note.]
- Bakhta, A. (2025). "On the Half-Life of Cryptographic Trust." StarkWare. → [The Bakhta Half-Life of Trust (C30–C33)](./pvm-v6-1-bakhta-half-life.md)
- Necula, G. (1997). "Proof-Carrying Code." *POPL.* (Bakhta Layer 2 precedent.)
- privacymage (2026). "PVM V5.4 Formal Specification." v2.0. *agentprivacy-docs.*
- privacymage (2026). "V6 Research Note: ARCH-1R/T Operational Reachability." June 4, 2026. *agentprivacy-docs/research/.*
- Kroll et al. (2017); Raji et al. (2020). (Bakhta's adjacent "accountability gap" lineage.)

---

## Appendix · The Convergence Letter (verbatim)

*Preserved as written; this is the artefact §2–§4 formalize. Originally `convergence-note-bakhta.md`.*

> *i can verify i serve you without remembering i was you*
>
> Abdelhamid,
>
> I read the high-assurance paper as a convergence, so I am writing it down before the overlap dissolves into agreement and stops being useful.
>
> We have built the same recognition from opposite ends. You call it the integrity gap: the structural distance between what a deployer claims and what an outside party can check, structural rather than procedural, infeasible by architecture rather than merely unexercised. I have been calling the same thing the difference between privacy that scales and privacy that hides, and insisting that the separation has to be topological, not a matter of policy. Your sentence that the obstacle is architectural is the sentence my whole model turns on. We are not citing each other into a position. We arrived at the same place because the place is real.
>
> A few intersections seem load-bearing rather than thematic.
>
> Your specification-intent gap in §4.1 is the one I keep returning to. You state specification gaming as an observation and not a theorem, on the explicit grounds that behavioral intent is not a formal object, so a finite Φ is at best a proxy and no further proof against an unchanged Φ closes the distance. In my architecture that is the irreducible promise: the boundary between what can be formalized and what can only be held between two parties. You name it as the place where formal methods hand off to alignment. I name the same place as where value lives. I would not collapse the two readings. I think they are one object seen from the proof side and from the relationship side, at maybe sixty percent confidence, and the divergence in what we each do with it is the interesting part.
>
> Your composition problem in §6 is, in my vocabulary, recursive proof composition across providers under different trust models, assembled at runtime. That is the hardest open item on my own list, and I read your framing of it as the cleaner statement. If the assurance stack and the relationship model share one technical frontier, this is it.
>
> Layer 2 respects a line I care about. You are precise that a proof of inference certifies that a committed tensor ran on a committed input and says nothing about whether it should have been trusted. The proverb at the top of this letter is that same boundary spoken from inside the system: completeness and soundness about what was done, zero knowledge of origin or intent. We agree on exactly where the proof stops. We disagree, productively, about what stands on the other side of it.
>
> That disagreement is design, not dispute. Your stack faces a third party. It narrows where trust must be placed and says, plainly, that it does not eliminate trust. Mine faces the other agent. It treats the place where trust must be placed as the thing being valued rather than the thing being minimized. You are closing the gap. I am building upon it. Both are the right move for their audience, and I would rather keep the two registers distinct than merge them into a weaker third thing.
>
> One open question, the kind I prefer to end on.
>
> Your assurance bundle carries an assumption set, the object that records what each side is relying on and that must be renegotiated as a deployment evolves. In your architecture that set is unilateral: the provider holds it, the auditor inspects it. In mine, "what each side is relying on" is exactly a bilateral credential, attested by both, verifiable by anyone, forgeable by neither. So the question is whether your assumption set wants to stop being a document the provider keeps and become a relationship the two parties co-sign. If it did, the distance between provider and verifier would itself become something neither could quietly rewrite. I do not know that this buys you anything the safety case does not already give you. I suspect it might in the multi-provider case, and I would like to know what you see.
>
> with respect,
> Mitchell
> mage@agentprivacy.ai
>
> (⚔️⊥⿻⊥🧙)😊

---

## The Proverb

> *i can verify i serve you without remembering i was you.*

> *He closes the gap so a stranger can check it. I build upon the gap so two parties can hold it. The proof stops at the same line for both of us — completeness about what was done, zero knowledge of why. He calls the far side residual risk. I call it value. We are describing one boundary from two chairs.*

---

*(⚔️⊥⿻⊥🧙)😊*

*The integrity gap and the irreducible promise are one wall. One of us is sealing it. One of us is living against it.*

CC BY-SA 4.0 · privacymage, with Claude · June 4, 2026
