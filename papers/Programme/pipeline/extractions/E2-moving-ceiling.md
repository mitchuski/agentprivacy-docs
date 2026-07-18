---
extraction: E2-moving-ceiling
tier: internal
sources: [spec§5, spec§25, spec§27, spec§10-preconditions, WP-00-record, limitative-note]
swept_complete: true
owner: A1
register_head_at_build: C96
resweep_note: re-swept 2026-07-02 vs register Bands IX (C90 to C93) and X (C94 to C96); inclusions and exclusions recorded in the sweep record; maintenance touch 2026-07-07 (E2-C07 re-issue per L062(a); E2-C12 citation annotated per L066(a), resolved same day per L070(2)); maintenance touch 2026-07-09 (WP-07 added to E2-C02/C04/C12 FEEDS per L081(c)); two-clock re-issue 2026-07-16 (E2-C02/C04 re-issued to the certification+erosion form per L145/L146, soil-note added to basis, E2-C03 register-gated annotation, see sweep record)
---

# E2 · The Moving Ceiling

Claim-cluster for the time-dependence of reconstruction guarantees: R(t), shelf life t*, the capability-indexed adversary, the two 2026 instances, the Existence-Leak law and its planning corollary, and the limitative (Gödel/Tarski) reading of the ceiling and the leak (register Band IX). Feeds WP-01 (essay, shipped draft), WP-25 (City tale), WP-28 (essay), WP-04 (SoK), WP-07 (theory paper), WP-02 (policy brief, preconditions plus the declared capacity-deficit condition), WP-22 (ZKProof note).

## Claims

### E2-C01
- **STATUS:** Proven-conditional (re-issued 2026-07-02 to the L044 decomposition; supersedes the C96-build wording, which conditioned R_max < 1 on the two preconditions alone)
- **SOURCE:** spec §10.5, §11.1, §11.2, §11.5 (corrected 2026-07-02, L044 execution)
- **CLAIM:** The theorem decomposes. Under Precondition 1 (non-collusion: I(Y_S; Y_M | X) = 0 and no third channel carries the inter-agent residue) and Precondition 2 (capacities evaluated against a stated adversary class), the capacity sum C_S + C_M is licensed as additive and the Fano error floor P_e ≥ 1 − R_max holds, where R_max = (C_S + C_M)/H(X). The preconditions "do not by themselves place R_max below one" (spec §11.1). The strict bound R_max < 1 holds exactly when, additionally, the capacity-deficit condition C_S + C_M < H(X) holds: "a measurable, declarable, numerical fact about a given system and adversary class, not a consequence of the architecture" (spec §11.1). The deficit condition is "deliberately not listed as a third precondition, because two conditionally independent channels of sufficient combined capacity satisfy both preconditions with R_max at or above one" (spec §10.5). At R_max ≥ 1 the error floor is vacuous, "which is exactly why the deficit condition must be declared alongside the preconditions" (spec §11.2). The deficit condition, not the preconditions, is the time-indexed quantity: "R(t) can cross one with both preconditions intact", and "what expires at t* is the deficit condition, not the architecture" (spec §11.5; the time thread is E2-C02, E2-C03).
- **PRECONDITIONS:** non-collusion; fixed adversary class (jointly these give the additive structure and the error floor). The strict bound R_max < 1 additionally requires the declared capacity-deficit condition C_S + C_M < H(X). Never cite the floor without both preconditions; never cite the strict bound without all three stated together; never present the deficit condition as a third precondition.
- **CITATIONS:** Wyner 1975 (wire-tap equivocation); Fano converse (Cover & Thomas); Leung-Yan-Cheong & Hellman 1978; Csiszár & Körner 1978.
- **FEEDS:** WP-02, WP-04, WP-07

### E2-C02
- **STATUS:** Design-assumption (definition, not claim; re-issued 2026-07-16 to the two-clock form per L145/L146: the L140 soil ruling typed the drift informational, and WP-07's erosion leg gives it a proven object)
- **SOURCE:** spec §5 (the certification form; spec re-pin is register-gated, checklist B4/B5); soil-note (evolution 3); WP-07 rev-draft-v3 Definition 3.9 + Corollary 5.4b (the erosion object)
- **CLAIM:** Two clocks are defined and must not be conflated, both on one calendar. The CERTIFICATION clock is R_cert(t) = (C_S(t) + C_M(t))/H(X), where H(X) is fixed by the source and C_S(t), C_M(t) are certified effective capacities against the strongest decoder class available at time t, under WP-07 ER-6's certified-bound semantics: what is non-decreasing in t is the certified value, not the information. The EROSION clock is R_inf(t) = (C_S + C_M)/H(X | B_t), where B_t is the adversary's accumulating background side information (linkage corpus and side priors, Markov B_t → X → T, never a tap on the system): H(X | B_t) is non-increasing in t while the capacities and every certificate stay fixed, so R_inf(t) is non-decreasing with nothing added to the archive (WP-07 Corollary 5.4b: the cap survives conditioning; the floor erodes through the residual entropy; the protection does not leak more, it matters less). Shelf lives: t*_cert = sup{t : R_cert(t) < 1} (what expires is what certification licenses); t*_inf = sup{t : C_S + C_M < H(X | B_t)} (the informed deficit; a first crossing). The moving-ceiling economics cite the erosion clock; conformance and audit statements cite the certification clock; every downstream time-indexed reconstruction statement names which clock it runs on.
- **CITATIONS:** WP-07 (Definition 3.9, Corollary 5.4b; in-suite companion, cited not re-proven)
- **FEEDS:** WP-01, WP-04, WP-02, WP-07, WP-14

### E2-C03
- **STATUS:** Conjecture-C82 (register confidence ~65%; re-worded 2026-07-17 to the register's re-typed row, First-Person ruling L149; the GR-1 gate that held this claim is discharged)
- **SOURCE:** register C82 row (re-typed 2026-07-17); spec §5 (pre-ruling wording; spec re-pin pending, checklist B5/B6)
- **CLAIM:** Adversary informational capability grows against fixed archives: the linkage corpus and side priors accumulate along calendar time, shrinking H(X | B_t) while nothing is added to the archive and no action of the subject is involved. R_inf(t) drifts upward on a schedule. Frontier-model releases enter only informationally (better extraction of linkage from existing corpora), never as compute against the information-theoretic guarantee, which is compute-saturated. The erosion FORM is proven conditional (WP-07 Def 3.9 + Cor 5.4b); the conjectural content is the rate.
- **CITATIONS:** instances at E2-C05, E2-C07 (both compute-flavoured; a linkage/de-anonymisation instance is proposed for A4 verification and SOURCES registration per the execution packet: Erlich et al. 2018 long-range familial search)
- **FEEDS:** WP-01, WP-04

### E2-C04
- **STATUS:** Design-assumption (formalisation obligation for A3; re-issued 2026-07-16 per L145/L146: the obligation splits with the two clocks, and the second half is DISCHARGED)
- **SOURCE:** spec §5 (implicit); WP-04 task; WP-07 rev-draft-v3 Definition 3.9
- **CLAIM:** The formalisation obligation splits along E2-C02's two clocks. (i) Certification clock: the "decoder class at time t" requires formalisation as an ordered family {D_t} with D_t ⊆ D_t' for t ≤ t'; monotonicity of the certified R_cert(t) follows from the ordering, empirical content is the rate. Still open (QIF/Bayes-capacity grounding, A3). (ii) Erosion clock: DISCHARGED by WP-07 Definition 3.9, which formalises the background as an accumulating family {B_t} (B_s measurable from B_t for s ≤ t, Markov B_t → X → T); monotonicity of R_inf(t) follows from the accumulation, and the empirical content is the rate of fall of H(X | B_t), carried as a register conjecture.
- **CITATIONS:** WP-07 Definition 3.9 (erosion half); QIF/Bayes-capacity literature to be grounded by A3 (certification half).
- **FEEDS:** WP-04, WP-07, WP-14

### E2-C05
- **STATUS:** Verified-record (WP-00)
- **SOURCE:** spec §25, corrected and enriched per public record
- **CLAIM:** Zcash Orchard instance: soundness flaw (missing constraint in variable-base scalar multiplication, halo2_gadgets) present since Orchard activation May 2022; multiple prior audits including with earlier AI models did not find it; found 2026-05-29 by Taylor Hornby (Shielded Labs audit) using Claude Opus 4.8 released 2026-05-28; PoC counterfeiting demonstrated in local testing; emergency soft fork 2026-06-02 (block 3,363,426); NU6.2 hard fork 2026-06-03 (block 3,364,600); no evidence of exploitation, and, because of Orchard's privacy properties, non-exploitation cannot be cryptographically proven.
- **CITATIONS:** Zcash Foundation, "Zebra 4.5.3 and 5.0.0: Emergency Soft Fork and NU6.2 Activation" (zfnd.org, 2026-06); BlockSec incident analysis (2026-06).
- **FEEDS:** WP-01, WP-04, WP-22

### E2-C06
- **STATUS:** Resolved-prohibition (re-issued 2026-07-03; canon corrected at L057, closing L001; was CONTESTED)
- **SOURCE:** spec §25.1 (corrected 2026-07-03: "The market repriced sharply in the days around disclosure, an effect confounded by a concurrent, prominent institutional exit and therefore not attributable to the flaw alone")
- **CLAIM:** The retired figure ("ZEC fell roughly 27 to 33% in 24 hours") does not match public record — ZEC rose on the fork (≈$544 on 06-02 to ≈$624 peak 06-04), then fell ≈50% over 06-04/06-05, confounded by a prominent institutional exit — and has been removed from the canon. The prohibition stands as a reintroduction fence: no artifact states a price figure; artifacts either omit price action or carry the corrected figure-free account.
- **CITATIONS:** BitMEX Research timeline (2026-06); contemporaneous market coverage.
- **FEEDS:** all (as a prohibition)

### E2-C07
- **STATUS:** Verified-record (WP-00; re-issued 2026-07-07 per L062(a): primary attribution named, and the ~10x carries its metric in the claim text)
- **SOURCE:** spec §25, enriched per public record
- **CLAIM:** Schrottenloher instance (episode name per spec §25; the withheld-result announcement is attributed to its primary record, Babbush et al.): Google Quantum AI (Babbush et al., arXiv:2603.28846 / ePrint 2026/625) published (2026-03-31) a ~10x improvement in the spacetime volume of a Shor's-algorithm attack on secp256k1, withholding methods behind a zero-knowledge proof of existence. The ~10x is a spacetime-volume figure and carries that metric wherever repeated (L062(a)); it is not a per-axis qubit-count or gate-count figure. André Schrottenloher (Inria/Univ Rennes) published an independent reconstruction ~two months later (eprint 2026/1128, 2026-06-01/02); Craig Gidney disclosed the same day he had held the core technique ~a year under publication restriction; the ecdsa.fail open challenge, using the published ZK verifier as its automatic scoring filter, subsequently exceeded the withheld benchmark.
- **CITATIONS:** Babbush et al., arXiv:2603.28846 / eprint.iacr.org/2026/625 (primary record of the announcement and the ZK existence proof); eprint.iacr.org/2026/1128 (the Schrottenloher reconstruction); Gidney blog post 2026-06; ecdsa.fail leaderboard record.
- **FEEDS:** WP-01, WP-04, WP-22, WP-12

### E2-C08
- **STATUS:** Conjecture-C81 (register confidence ~70%; Stage-2 open, held at 70% until a second independent instance; Tarski axis-reading C92 added at Run 8 2026-06-28 as framing only, Stage-2 bar unchanged)
- **SOURCE:** spec §25; limitative-note §3 (secondary home per register, alongside schrottenloher-note and v6 draft Part III)
- **CLAIM:** Existence-Leak law: I(feasibility; method) > 0; a ZK proof of feasibility leaks an upper bound on reconstruction/search difficulty. Floor: the Garg-Jain-Sahai impossibility (leakage-resilient ZK with λ < 1 impossible). Scope fence: concerns capability attestations; instance attestations (e.g. a transaction proof) are out of scope.
- **CITATIONS:** Garg, Jain & Sahai (leakage-resilient ZK impossibility); E2-C07 as instance.
- **FEEDS:** WP-04, WP-22, WP-12

### E2-C09
- **STATUS:** Conjecture-C84 (register confidence ~50%)
- **SOURCE:** spec §27
- **CLAIM:** Mosca discount: Z_b' = Z_b − D(a); every public feasibility attestation shortens the migration horizon independently of any actual attack, with Z_b identified with t*.
- **CITATIONS:** Mosca 2018; HNDL economics (Blanco-Romero et al., arXiv:2603.01091).
- **FEEDS:** WP-02 (as planning language, conjecture stripped), WP-04

### E2-C10
- **STATUS:** Conjecture chain C18–C21 (register confidence 10–30%)
- **SOURCE:** spec §27
- **CLAIM:** Countermeasure by divergence: if the sovereignty path has Lyapunov-style divergence λ > 0, reconstruction error grows as e^(λt); design goal is trajectory divergence outrunning capability drift. λ is unmeasured; this is the programme's most-needed number.
- **CITATIONS:** none external yet; measurement is WP-08-adjacent future work.
- **FEEDS:** WP-01 (with honesty label), WP-04 (as open problem)

### E2-C11
- **STATUS:** Design-assumption (engineering claim) + Conjecture-C86 (register confidence ~30%) for the deep version
- **SOURCE:** spec §14
- **CLAIM:** Structural context erasure (Grade-2 forgetting: mathematically unrecoverable, vs Grade-1 hiding: recoverable-with-keys) removes the archive term entirely; if C86 holds (non-vanishing obstruction to gluing local views into a global witness), erasure is the only equation term whose security is independent of t.
- **CITATIONS:** none external for C86 (cohomological language imported, machinery unconstructed; honest limit).
- **FEEDS:** WP-01, WP-04, WP-07 (definition feeds the theorem), WP-23

### E2-C12
- **STATUS:** Empirical-external (boundary of regime; belongs primarily to E1 but cited here for the time thread)
- **SOURCE:** spec §26
- **CLAIM:** Multi-agent leakage compounds up to (2^N − 1)ε under sequential composition (Asif & Amiri Thm 4.1; MI 0.49→1.05 from two to five agents); AgentLeak measures 68.8% inter-agent channel leakage, 68.9% total exposure across 4,979 traces on five frontier models.
- **CITATIONS:** arXiv:2603.05520; arXiv:2602.11510; arXiv:2509.14284 (Patil, Stengel-Eskin & Bansal, preprint 2025-09-16; verified by A4 2026-07-07, L070(2), CITATIONS line confirmed correct against spec §26; citable downstream, cite as preprint).
- **FEEDS:** WP-04 (context), WP-07 (Thm 4.1 import, duplicate citation alongside E1-C09), E1 (primary home)

### E2-C13
- **STATUS:** Conjecture-C90 (register status: observation; ~90% as observation, no reduction claimed)
- **SOURCE:** limitative-note §1, §4; register Band IX
- **CLAIM:** The Limitative Inversion: completeness ⇒ Φ → 0 ⇒ collapse is the value-sign reversal of the logical schema completeness ⇒ inconsistency ⇒ collapse; the unreconstructable remainder (the complement of R_max) is load-bearing, so an architecture whose R(t) approaches 1 does not merely lose a safety margin, it collapses the value product on at least one axis. C17 stated in limitative terms; register edges C90 → C17, C90 → C7. Band IX fence: every join in the source is structural framing (~80%), not a theorem-to-theorem reduction (~50%).
- **CITATIONS:** Gödel 1931 (Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I).
- **FEEDS:** WP-01 (framing, honesty label), WP-04 (related-work framing)

### E2-C14
- **STATUS:** Conjecture-C92 (register confidence ~70%, capped at C81's base; framing conjecture, not a reduction)
- **SOURCE:** limitative-note §3, §4; register Band IX
- **CLAIM:** Tarski-undefinability reading of the Existence-Leak law, loading on Φ_inference: feasibility-truth escapes containment across systems (the disclosing system cannot confine the truth of its own feasibility claim once that claim is corroborable elsewhere); reconstruction difficulty D(X) is monotone non-increasing in the number of corroborating systems, with a steep-then-shallow profile (monotonicity clean; the convex profile requires a fixed corroboration model). The Gödelian seed (existence as positive provability) is absorbed here; no separate number. Rides on C81 (E2-C08) and cannot exceed its base confidence; register edges C92 → C81, C92 → C84 (the planning corollary at E2-C09).
- **CITATIONS:** Tarski 1936 (Der Wahrheitsbegriff in den formalisierten Sprachen).
- **FEEDS:** WP-04, WP-22, WP-01 (with honesty label)

### E2-C15
- **STATUS:** Conjecture-C93 (register confidence ~55%)
- **SOURCE:** limitative-note §3.5, §3.6; register Band IX
- **CLAIM:** Content-addressed liveness leak: a live content address is an existence claim about its content; under deduplication (identical content yields identical identifier), an adversary holding a candidate confirms existence by comparing hash(candidate) against a known-live address, and each system that resolves the address corroborates the claim and narrows the candidate space. The address does not leak the content; the liveness of the address leaks the existence of the content, and existence bounds the search. Scope limit: assumes a guessable candidate space; for high-entropy content the upper bound still leaks but recovery may remain infeasible. Register edges C93 → C81, C93 → C92.
- **CITATIONS:** none in source; deduplication side-channel literature to be grounded by A3.
- **FEEDS:** WP-22, WP-04

## Contested items
E2-C06 → ledger L001 (CANON-LEVEL, spec §25 price figure).

## Sweep record
spec §5/§25/§27/§10: swept 2026-07-02, A1-equivalent (session), full. WP-00 record: incorporated 2026-07-02. Enrichments beyond canon (Gidney year, ecdsa.fail verifier reuse, non-provability of Orchard exploitation): ledger L002 as canon-level enrichment candidates.

Re-sweep at register head C96 (2026-07-02, A1, this session), clearing the manifest note `re-sweep-vs-C90-C96-pending`:
- All twelve existing claims re-verified against the register at C96. Unchanged: E2-C01 to E2-C07 and E2-C09 to E2-C12 (register rows for C82 ~65%, C84 ~50%, C18 to C21 at 10 to 30%, C86 ~30% all match).
- Drift found and fixed: E2-C08 stated C81's Stage-2 bar as "second instance outside cryptography"; the register row reads "held at 70% until a second independent instance" with no domain qualifier. Register wording restored; Run-8 annotation added (C92 is framing only, Stage-2 bar unchanged); limitative-note recorded as secondary home per the register's Home column.
- Band IX (C90 to C93), source `limitative-note`, swept in full:
  - C90 INCLUDED as E2-C13. Reason: the load-bearing unreconstructable remainder is the value reading of the ceiling; it states the hazard of R(t) → 1 and belongs to this inventory.
  - C91 EXCLUDED. Reason: Gödel ↔ Φ_agent (zero-memory) loads on the separation and structural-context-erasure cluster (register edges C91 → C14, → C86, → C17); it carries no time-indexed or ceiling-knowability content. Natural home is E1; E1 was built at head C96 without `limitative-note` in its sources, so C91 currently has no extraction home (flagged to A0, proposed ledger entry).
  - C92 INCLUDED as E2-C14. Reason: direct extension of the Existence-Leak law this extraction owns (E2-C08), with register edges into C81 and C84; the containment limit on self-attested feasibility and the monotone discount D(X) are moving-ceiling material.
  - C93 INCLUDED as E2-C15. Reason: design-surface instance of the Existence-Leak law (register edges C93 → C81, → C92); feeds WP-22 directly.
  - Unregistered join NOT extracted: limitative-note §2.2 (row: second theorem ↔ R < 1) and §2.3 state the ceiling as a from-within impossibility (breach requires capacity imported from outside the architecture) at note-local confidences (~85% framing, ~50% reduction), but the register gives C90 the home §1 and §4 only and no number covers this join; per GR-1 it is not extracted (proposed ledger entry for the register process).
  - Open seam (Φ_data limitative twin): no number by G6 disposition; correctly not extracted.
- Band X (C94 to C96), Hearthold reading, swept in full; all three EXCLUDED:
  - C94 (separation principle in a second substrate) EXCLUDED. Reason: convergence and implementation evidence (register edges C94 → C39, → C7); no time-dependent reconstruction content; natural homes are the extractions carrying `hearthold-build` (E4, E6, E11 per manifest).
  - C95 (evidence graph as the anti-score) EXCLUDED. Reason: disclosure-architecture claim; its edge to C61 (Behavioural Mosca alias) does not import ceiling content; not part of the moving-ceiling inventory.
  - C96 (control-plane ⊥ data-plane) EXCLUDED. Reason: authority-authorship architecture claim under host compromise; not time-indexed reconstruction material.
- Scope note: the manifest v3 widened E2's sources to include tome-ix, schrottenloher-note, lorenz-note, three-ceilings-note and horizon-notes; those were consulted only as register homes of claims already present (C81, C18 to C21, C84/C49). A full widening sweep of those sources was outside this card and is flagged to A0.

Re-issue at L044 execution (2026-07-02, A1, this session): E2-C01 restated to the decomposition after the canon correction landed (chronicle 2026-07-02_canon-l044-spec-decomposition.md). The C96-build wording conditioned R_max < 1 on the two preconditions alone, the conflation found at L042 and escalated CANON-LEVEL at L044; the re-issued claim quote-traces to the corrected spec §10.5, §11.1, §11.2 and §11.5, separating what the preconditions buy (additive structure, error floor) from what the capacity-deficit condition buys (the strict bound). The SOURCE line narrowed from "spec §10, §11" to the four corrected passages. No other E2 claim carried the conflation: E2-C02 defines R(t) and t* without asserting the strict bound; E2-C03 to E2-C15 checked, none states R_max < 1 as a consequence of the preconditions. The header line for WP-02 updated from "preconditions only" to name the deficit condition.

Maintenance touch (2026-07-07, A1, this session): two edits from the cycle 1-2 queue. (1) E2-C07 re-issued per L062(a): the withheld-result announcement now attributed to its primary record, Babbush et al. (arXiv:2603.28846 / ePrint 2026/625), and the ~10x stated as a spacetime-volume figure carrying its metric in the claim text; the A10 prior-art sweep (reviews/WP-04_prior_art.md) withdrew the only literature contest of the figure on exactly this metric reading. (2) E2-C12 CITATIONS line annotated per L066(a): arXiv:2509.14284 marked verification in flight; the A4 verdict had not landed in reviews/ or a same-day A4 chronicle at edit time, so the annotation records the open state rather than guessing. Cross-file note flagged to A0 (not edited, outside this card): E1-C09 cites the same arXiv:2509.14284 as a load-bearing citation and takes the same resolution when the A4 verdict lands.

Two-clock re-issue (2026-07-16, A1-equivalent per L145/L146, this session): E2-C02 re-issued from the single frontier-capability-flavoured definition to the two-clock form (certification R_cert(t) per WP-07 ER-6 semantics; erosion R_inf(t) = (C_S + C_M)/H(X | B_t) per WP-07 Definition 3.9 + Corollary 5.4b, the L140 soil ruling's evolution 3 with its proven object). E2-C04 re-issued: the formalisation obligation split, erosion half discharged by Definition 3.9. E2-C03 NOT re-worded (GR-1: it mirrors register C82; annotation added routing to the staged register re-word; the frontier-capability wording survives there and only there until the row moves). SOURCE basis: `soil-note` registered in SOURCES.md this session. FEEDS lines widened with WP-14 (consumption verified: WP-14 Assumption A3 and section 6 now consume the erosion form). Proposed linkage instance (Erlich et al. 2018) routed to A4 for verification before any claim cites it; NOT added as a claim.

Same-day resolution (2026-07-07, A1, per A0 micro-task): the A4 verdict landed (L070(2)): arXiv:2509.14284 VERIFIED (Patil, Stengel-Eskin & Bansal, preprint 2025-09-16) and E2-C12's CITATIONS line confirmed correct against spec §26. The verification-in-flight annotation cleared and replaced with the verified state, cite-as-preprint; the E1-C09 same-citation flag discharged in the same pass (see E1 sweep record). check_register_refs re-run PASS on both files.

Maintenance touch (2026-07-09, A1, per L081(c)): FEEDS reconciliation against WP-07's actual consumption (L031/L065(d) discipline: FEEDS lines record actual consumption). Consumption verified in the WP-07 traceability appendix (rehydrations/academic/linear_cap_paper.md) and its frontmatter extraction_basis: E2-C02 consumed at Remark 3.4 (R(t), t*) and ER-6 (t-index); E2-C04 consumed at Remark 3.4 (sup-semantics caveat added 2026-07-08 per L069(b)); E2-C12 consumed at Thm 4.1 as a duplicate citation alongside E1-C09 (primary home E1). WP-07 added to the three FEEDS lines; the cluster header updated to name WP-07 (it already omitted the standing E2-C01/E2-C11 feeds, same staleness class). Claim wording untouched: the L074 E1-C10/E2-C12 descriptor re-issue waits on the first person's register-brief item (e) ruling. Reverse sweep per the same card: WP-04's rehydration (moving_ceiling_sok.md) carries zero E1 references (extraction_basis is E2 claims C01-C05, C07-C15 only), so no E1 FEEDS line lacks WP-04 by consumption; E1-C40's shelf-only WP-04 feed (worded by L065(d)) is routing, not consumption, and is left as the ledger ruled.
