---
extraction: E2-moving-ceiling
tier: internal
sources: [spec§5, spec§25, spec§27, spec§10-preconditions, WP-00-record]
swept_complete: true
owner: A1
register_head_at_build: C89
---

# E2 · The Moving Ceiling

Claim-cluster for the time-dependence of reconstruction guarantees: R(t), shelf life t*, the capability-indexed adversary, the two 2026 instances, the Existence-Leak law and its planning corollary. Feeds WP-01 (essay, shipped draft), WP-25 (City tale), WP-04 (SoK), WP-02 (policy brief, preconditions only), WP-22 (ZKProof note).

## Claims

### E2-C01
- **STATUS:** Proven-conditional
- **SOURCE:** spec §10, §11
- **CLAIM:** R_max = (C_S + C_M)/H(X) < 1 and the Fano error floor P_e ≥ 1 − R_max hold under Precondition 1 (non-collusion: I(Y_S; Y_M | X) = 0 and no third channel carries the inter-agent residue) and Precondition 2 (capacities evaluated against a stated adversary class).
- **PRECONDITIONS:** non-collusion; fixed adversary class. Never cite this claim without both.
- **CITATIONS:** Wyner 1975 (wire-tap equivocation); Fano converse (Cover & Thomas); Leung-Yan-Cheong & Hellman 1978; Csiszár & Körner 1978.
- **FEEDS:** WP-02, WP-04, WP-07

### E2-C02
- **STATUS:** Design-assumption (definition, not claim)
- **SOURCE:** spec §5
- **CLAIM:** R(t) = (C_S(t) + C_M(t))/H(X), where H(X) is fixed by the source and C_S(t), C_M(t) are effective capacities against the strongest adversary class available at time t. Shelf life t* = sup{t : R(t) < 1}.
- **CITATIONS:** none (definitional)
- **FEEDS:** WP-01, WP-04, WP-02

### E2-C03
- **STATUS:** Conjecture-C82 (register confidence ~65%)
- **SOURCE:** spec §5
- **CLAIM:** Frontier capability growth raises C_S(t) + C_M(t) against fixed archives without raising H(X); R(t) drifts upward; the drift is coupled to frontier-model release, not to any action of the subject.
- **CITATIONS:** instances at E2-C05, E2-C07
- **FEEDS:** WP-01, WP-04

### E2-C04
- **STATUS:** Design-assumption (formalisation obligation for A3)
- **SOURCE:** spec §5 (implicit); WP-04 task
- **CLAIM:** The "adversary class at time t" requires formalisation as an ordered family of decoder classes {D_t} with D_t ⊆ D_t' for t ≤ t'; monotonicity of R(t) follows from the ordering, empirical content is the rate.
- **CITATIONS:** to be grounded by A3 in the QIF/Bayes-capacity literature.
- **FEEDS:** WP-04

### E2-C05
- **STATUS:** Verified-record (WP-00)
- **SOURCE:** spec §25, corrected and enriched per public record
- **CLAIM:** Zcash Orchard instance: soundness flaw (missing constraint in variable-base scalar multiplication, halo2_gadgets) present since Orchard activation May 2022; multiple prior audits including with earlier AI models did not find it; found 2026-05-29 by Taylor Hornby (Shielded Labs audit) using Claude Opus 4.8 released 2026-05-28; PoC counterfeiting demonstrated in local testing; emergency soft fork 2026-06-02 (block 3,363,426); NU6.2 hard fork 2026-06-03 (block 3,364,600); no evidence of exploitation, and, because of Orchard's privacy properties, non-exploitation cannot be cryptographically proven.
- **CITATIONS:** Zcash Foundation, "Zebra 4.5.3 and 5.0.0: Emergency Soft Fork and NU6.2 Activation" (zfnd.org, 2026-06); BlockSec incident analysis (2026-06).
- **FEEDS:** WP-01, WP-04, WP-22

### E2-C06
- **STATUS:** CONTESTED (canon-level; ledger L001)
- **SOURCE:** spec §25 ("ZEC fell roughly 27 to 33% in 24 hours")
- **CLAIM:** The canon's price-action figure does not match public record: ZEC rose on the fork (≈$544 on 06-02 to ≈$624 peak 06-04), then fell ≈50% over 06-04/06-05, confounded by a prominent institutional exit. No artifact uses the canon figure; artifacts either omit price action or state the verified sequence.
- **CITATIONS:** BitMEX Research timeline (2026-06); contemporaneous market coverage.
- **FEEDS:** all (as a prohibition)

### E2-C07
- **STATUS:** Verified-record (WP-00)
- **SOURCE:** spec §25, enriched per public record
- **CLAIM:** Schrottenloher instance: Google Quantum AI published (2026-03-31) a ~10x Shor resource improvement for secp256k1, withholding methods behind a zero-knowledge proof of existence; André Schrottenloher (Inria/Univ Rennes) published an independent reconstruction ~two months later (eprint 2026/1128, 2026-06-01/02); Craig Gidney disclosed the same day he had held the core technique ~a year under publication restriction; the ecdsa.fail open challenge, using the published ZK verifier as its automatic scoring filter, subsequently exceeded the withheld benchmark.
- **CITATIONS:** eprint.iacr.org/2026/1128; Gidney blog post 2026-06; ecdsa.fail leaderboard record.
- **FEEDS:** WP-01, WP-04, WP-22, WP-12

### E2-C08
- **STATUS:** Conjecture-C81 (register confidence 70%; Stage-2 hold pending second instance outside cryptography)
- **SOURCE:** spec §25
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
- **CITATIONS:** arXiv:2603.05520; arXiv:2602.11510; arXiv:2509.14284.
- **FEEDS:** WP-04 (context), E1 (primary home)

## Contested items
E2-C06 → ledger L001 (CANON-LEVEL, spec §25 price figure).

## Sweep record
spec §5/§25/§27/§10: swept 2026-07-02, A1-equivalent (session), full. WP-00 record: incorporated 2026-07-02. Enrichments beyond canon (Gidney year, ecdsa.fail verifier reuse, non-provability of Orchard exploitation): ledger L002 as canon-level enrichment candidates.
