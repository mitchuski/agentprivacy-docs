# Convergence Note: Compiled AI and the agentprivacy Architecture

**Subtitle:** One axis, not three.

**Author:** Mitchell Travers (privacymage)
**Status:** Research note v1 (convergence analysis). Filed under V6 development as a path taken, not a load-bearing result.
**Date:** 2026-05-20
**License:** CC BY-SA 4.0 + Apache 2.0
**Subject paper:** Trooskens, Karlsberg, Sharma, De Brouwer, Van Puyvelde, Young, Thickstun, Alterovitz, De Brouwer. *Compiled AI: Deterministic Code Generation for LLM-Based Workflow Automation.* arXiv:2604.05150v1 [cs.SE], April 2026. (XY.AI Labs; Stanford University School of Medicine; Cornell; Brigham and Women's / Harvard Medical School.)

> independent builders arriving at the same primitive is plurality, not coincidence.
> the question is never who got there first. it is which axis they were standing on.

---

## Verdict

Compiled AI converges hard on one axis of the Privacy Value Model and is silent on the other two. It is inference-layer separation Φ_inference(Γ) driven to its limit, reached from the reliability-and-audit direction rather than the sovereignty direction. Measured against

```
Φ_v5 = Φ_agent(Σ) · Φ_data(Δ) · Φ_inference(Γ)
```

it scores high on one factor and near-zero on the rest, so by the multiplicative law (C7) it is a reliability architecture, not a privacy architecture. Read it as a candidate Solver-side substrate, not as an alternative to the dual-agent stack.

## The paper in one breath

Compiled AI defines a workflow system by three properties: the model runs once at generation time and never at transaction time; deployed workflows execute as static code with zero further model calls; and every artifact passes a four-stage validation pipeline (security, syntax, execution, accuracy) before deployment. An LLM is confined to generating narrow business-logic functions inside pre-validated templates, which compile into deterministic Temporal activities. The motivating asymmetry: enterprise workflows need intelligence to design but not to execute repeatedly.

## The three convergences

### Convergence 1. One-time invocation plus zero-token execution maps to Φ_inference(Γ) → 1

This is the cleanest correspondence in the paper. The LLM is the Generator at compile time; the deterministic activity is the Solver at runtime; the model is removed from the execution loop entirely. That is the same Generator-Solver split BRAID uses, here pushed to the strong limit: the model is provably absent from the runtime path, so Φ_inference → 1 by construction rather than by degree. They arrive via the DSPy and LLM+P lineage; agentprivacy arrives via BRAID and the inference axis. Same primitive, two on-ramps.

### Convergence 2. Topological security maps to architecture over policy (the C17 lineage)

Their security argument is purely structural. Prompt-injection surface shrinks because there is nowhere at runtime for an injected instruction to land, not because a rule forbids it. This is "scales vs hide": separation enforced by where the model can run, not by promise. It is independent empirical support for the meta-principle that topology beats policy, the claim Burgess §6.5 anticipated and the architecture carries as C17. The model exiting the loop is the same move as the Gap being load-bearing: the property holds because of where the boundary sits, not because anyone agreed to honour it.

### Convergence 3. Validation-as-requirement maps to compliance by construction (with the IEEE 7012 caveat)

Their fourth design principle encodes regulatory constraints (HIPAA, PCI-DSS, SOC 2) directly in templates so generated code inherits compliance by default. That is compliance-by-construction, and it is exactly the operator-side compliance the IEEE 7012 integration plan v2 already separates from the full architecture. Compliance is not the agentprivacy stack. Their HIPAA-in-the-template is the Σ axis read from the operator's chair, not the bilateral first-person term that MyTerms / IEEE 7012 places on the data subject's side. The convergence is real; the caveat is the entire reason the Second Person Spellbook exists.

### Adjacent: bounded agentic invocation maps to constrained delegation

Appendix A's "Safety Sandwich" fences a probabilistic extraction step between input validation and deterministic logic, governed by schema, fallback, and human escalation. That is the Mage's bounded delegation: the delegated act is real but boundary-bounded. The structure matches cleanly. The missing piece is whose delegation it is.

## The false friends

Two places where the vocabulary matches and the structure does not. Naming them is the honest part.

**Dual LLM is not Master and Emissary.** The paper's Dual LLM pattern separates a privileged instance from a quarantined one to contain prompt injection (Willison-style isolation). There is no `I(S;M|FP) < ε*` bound, no First Person both instances serve, and no right→left→right return cycle. It isolates to defend; it does not separate to generate sovereignty. The resemblance is surface only and the telos is opposite: defence against an attacker, not preservation of a principal.

**Zero-token execution is not the Amnesia Protocol.** Both forget the reasoning at runtime, but by inverse means. Selene forgets so that nothing can be reconstructed; the proof is valid because the witness is gone. The code foundry "forgets" by writing everything down: every decision traces to a line of code, fully auditable. That is the Emissary's mode, total disclosure, the opposite of forgetting-as-proof. Same word, opposite physics.

## The orthogonality verdict

By the multiplicative law this is decisive.

| Axis | What it measures | Compiled AI | Reading |
|---|---|---|---|
| Φ_agent(Σ) | Swordsman/Mage separation serving a principal | undefined | no First Person; the two instances serve the operator |
| Φ_data(Δ) | provider fragmentation | → 0 | centralised infrastructure, single-provider activities |
| Φ_inference(Γ) | Generator/Solver separation | → 1 | model absent from the runtime path |

One strong factor times two near-zero factors collapses the product, so Φ_v5 → 0. The value Compiled AI creates accrues to the operator: determinism, audit readiness, a 57× token reduction at 1,000 transactions, a shrunk attack surface. None of it accrues to the data subject. There is no behavioural capital, no bilateral term, no VRC, no ZKP, no decentralisation. This is not a criticism of the paper; it solves the operator's problem and solves it well. It is a placement. Compiled AI is the Emissary's reliability discipline, not the Master's sovereignty layer.

## Synthesis: what to do with it

Read Compiled AI not as a competitor but as a candidate execution layer for the Solver half of the Mage. If the Mage's delegated work should run deterministically and auditably, the code foundry is a credible discipline for compiling that delegation into static, testable artifacts. agentprivacy is then what you wrap around it:

- name the First Person the workflow serves (restores Φ_agent)
- fragment the substrate across providers (restores Φ_data)
- bind the workflow to a first-person term rather than an operator policy (restores the bilateral A(τ) and closes the IEEE 7012 gap)

Compiled AI hands you a clean Φ_inference → 1. The architecture is what makes that determinism serve sovereignty rather than the enterprise.

One structural note worth keeping. Compiled AI is an Emissary-only architecture: the analytic mode compiles, the artifact freezes time into snapshots and runs, and nothing returns to broad attention. No right-hemispheric return, no First Person in the loop. That is precisely why it works for invoice extraction and precisely why it cannot be a sovereignty layer on its own. The return is what agentprivacy adds.

## Candidate conjectures (provisional labels, pending canonical assignment)

Provisional `CA-i` labels are used to avoid colliding with the canonical C-series; promotion and renumbering are the author's call.

- **CA-1 (near-certain, ~90%, definitional).** Compiled AI instantiates the strong limit Φ_inference → 1, because the model is absent from the runtime path by construction.
- **CA-2 (~80%, interpretive).** Topological removal of the model from the runtime path is the same enforcement primitive as "scales vs hide"; Compiled AI is independent empirical support for the C17 lineage.
- **CA-3 (conditional on C7, ~85%).** A single strong axis with Φ_data → 0 and Φ_agent undefined yields Φ_v5 → 0; high reliability therefore implies no sovereignty value. Compiled AI is a clean worked example of axis collapse.
- **CA-4 (engineering hypothesis, ~55%).** The code foundry can serve as the Solver-side execution layer for a Mage's bounded delegation, with Φ_agent and Φ_data supplied externally. Not yet built; falsifiable by attempting the integration.

## Honest limits

This note is architectural, not a replication of their benchmarks. CA-2's "same primitive" claim is interpretive: their security gain is partly measured (injection-detection figures carry stated methodology caveats, including canary recall that reflects simulation rather than production) and partly structural; only the structural part is the convergence. The Φ_data → 0 reading assumes their stated deployment target (centralised Temporal infrastructure); a future variant that fragments the substrate would lift Φ_data and change the mapping. The note treats the paper as a fixed design point, yet their own future-work directions (natural-language specification, automatic decomposition) could move it. Finally, the absence of Φ_agent is a property of the use case (operator workflow automation), not a flaw the authors should have addressed; they were never solving for a principal.

## References

- Trooskens et al., *Compiled AI: Deterministic Code Generation for LLM-Based Workflow Automation*, arXiv:2604.05150v1, April 2026.
- Privacy Value Model V5.4: three-axis separation Φ_v5 = Φ_agent · Φ_data · Φ_inference; C7 multiplicative composition.
- agentprivacy three-axis separation skill (Φ_inference as the Generator-Solver split from BRAID).
- McGilchrist, *The Master and His Emissary*: the right→left→right return cycle; the Emissary's mode as explicit, abstract, time-frozen.
- Burgess, "Spacetimes with Semantics II" / "Norms and Swarms": the C17 lineage, topology over policy.
- IEEE 7012-2025 (MyTerms) integration plan v2: operator-side compliance versus the bilateral first-person term.

---

## Appendix A: Letter to XY.AI Labs (draft)

Dear Geert and colleagues,

I read *Compiled AI* with real recognition. You reached, from the reliability and healthcare-audit direction, a primitive that some of us reached from the privacy and sovereignty direction: take the model out of the execution loop, compile intelligence once, then run deterministic code. In the architecture I work on (agentprivacy / the dual-agent sovereignty model), that is the inference-layer separation Φ_inference, and your compiled paradigm is the strong limit of it, Φ_inference → 1, the model provably absent from the runtime path. Two different on-ramps, one primitive. I take that as plurality rather than coincidence, and I am noting the convergence rather than any precedence.

What struck me most is that your security argument is topological, not policy-based. The injection surface shrinks because there is nowhere at runtime for an instruction to land, not because a rule forbids it. That is the same claim I build everything on: separation enforced by where computation can happen beats separation enforced by promise. Your paper is the cleanest production-systems evidence for it I have seen.

Where our work diverges is by design, not disagreement. Compiled AI optimises for the operator: determinism, auditability, cost at scale. The architecture I work on adds two further axes, agent separation and data fragmentation, so that the same determinism serves a principal (a "first person") rather than the enterprise. In that framing your code foundry reads as a strong candidate substrate for the Solver half of a bounded delegation, with the sovereignty layer wrapped around it.

A genuine question, if you are open to it: have you considered the compiled artifact as the execution layer for delegation that a data subject authorises, rather than only workflows an operator specifies? I would value a conversation, and I am happy to share the three-axis framing in full.

With respect for the work,

Mitchell Travers (privacymage)
BGIN Identity, Key Management & Privacy WG · First Person Network
agentprivacy.ai · mage@agentprivacy.ai

---

**Verify:** [agentprivacy.ai](https://agentprivacy.ai) · [sync.soulbis.com](https://sync.soulbis.com) · [github.com/mitchuski/agentprivacy-docs](https://github.com/mitchuski/agentprivacy-docs)

*(⚔️⊥⿻⊥🧙)😊*
