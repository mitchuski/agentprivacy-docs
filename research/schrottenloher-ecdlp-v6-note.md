# V6 Research Note — The Existence-Leak and the Falling Z

**Date:** 2 June 2026
**Object:** Schrottenloher, *Optimized Point Addition Circuits for Elliptic Curve Discrete Logarithms*, arXiv:2606.02235v1 (1 June 2026)
**Lineage anchor:** C30–C33 (Bakhta / *Half-Life of Trust* / Behavioral Mosca Inequality)
**Candidate seed:** one new conjecture proposed below, numbering deferred
**Status:** Stage 1, pre-peer-review, worked empirical example
**Erratum 2026-06-10 (Run 0 register lock):** the candidate proposed below as "C40" is registered as **C81** in `CONJECTURE_REGISTER_V6.md`; C40 was already occupied by Zcash dual-ledger (formal spec §17.2.1). Read every "C40 (Existence-Leak)" in this note as C81.

> i can prove i broke you without showing you how

the inverse of Selene's Proof, and the reason this note exists.

## Verdict

A reproducible, open-source quantum attack on secp256k1 lands as a clean downward revision of the Z trajectory in the Behavioral Mosca Inequality, not as a new attack class. It touches nothing in the PQ stack: ML-KEM and ML-DSA are lattice schemes outside Shor's discrete-log reach, and the isogeny line died by a different cause. The value of the object is twofold. First, it is the most concrete decrement to date of the time-to-feasibility term for the curve that secures the behavioral-capital ledgers. Second, the manner of its arrival exposes a leakage channel in zero-knowledge disclosure control that the architecture has not yet named, and which contrasts sharply with the amnesia primitive at the base of the Zero Spellbook.

## The object

Schrottenloher (Inria Rennes) reconstructs, in the open and with runnable code, the elliptic-curve discrete-log circuits that Babbush et al. announced roughly three months earlier (arXiv:2603.28846) but declined to publish. Babbush's group improved the logical circuits by a factor of two to three over Litinski's 2023 benchmark and then withheld the circuits, attesting their gate and qubit counts by a zero-knowledge proof rather than by disclosure, on stated concern over medium-term attack feasibility. Schrottenloher reproduces comparable numbers from first principles: about 1.5% more qubits and 6.5 to 10% fewer Toffoli gates on the point-addition circuit.

The engine is a two-pass split of the extended Euclidean algorithm. A plain Euclidean stage records its branch choices as a packed garbage bit-vector; a separate Bézout reconstruction replays those bits. Separating the input side from the coefficient side folds modular inversion and an in-place multiplication into one structure, and the space cost collapses onto that reconstruction step at roughly 4.36n qubits. A second, instance-specific gain comes from secp256k1's prime being pseudo-Mersenne, 2^256 minus (2^32 plus 977), so reduction stops being subtraction of a 256-bit constant and becomes erase-the-top-bit, add-a-small-f. The curve is faster to attack because it was chosen to be fast to use.

The trajectory, full Shor on secp256k1, space-optimized:

| Source | Logical qubits | Toffoli gates |
|---|---|---|
| Litinski 2023 | ~2x (≈2,400) | 2^27.57 |
| Babbush et al. 2026 | 1,191 | 2^26.27 |
| Schrottenloher 2026 | 1,208 | 2^26.11 |

Honest framing for the lineage: these are logical counts. Fault-tolerant execution still demands error correction and therefore millions of physical qubits. Z is decremented, not collapsed.

## Where it slots: C30–C33

The Behavioral Mosca Inequality holds that exposure begins when X_b plus Y_b exceeds Z_b, where X_b is the required confidentiality lifetime of behavioral capital, Y_b is the migration time for behavioral-data infrastructure to post-quantum primitives, and Z_b is the time until the attack is operationally feasible. This paper is a measured reduction in the resource-cost component of the Z_b trajectory for the one curve that signs on-chain identity, reputation, and credential rails. In the temporal-dynamics term e^{-lambda t} (1 + A(tau)), a fall in Z_b registers as a rise in the effective decay rate lambda for every configuration secured by secp256k1: the threat landscape against that primitive is now moving faster, by a published and reproducible margin, which is precisely the condition under which the decay function says stale configurations are catastrophically undervalued.

This is a worked example feeding C30–C33. It is not a new conjecture in that cluster, and it does not change any proven bound. It does what *Half-Life of Trust* predicts a primitive's aging should do: it ages progressively, and now there is a number attached to the slope.

## The disclosure fork: a candidate conjecture

The interesting structure is not the circuit. It is that a zero-knowledge proof intended as a disclosure control leaked the only quantity whose secrecy would have mattered. A proof that an attack is feasible at cost kappa is an upper bound on the difficulty of building that attack, and an upper bound on difficulty is a search-space compression for any third party. Babbush's proof hid the method and broadcast the feasibility; the feasibility was sufficient for independent reconstruction within a quarter.

State it for the record.

**Candidate conjecture (Existence-Leak). Confidence ~60%, Stage 1, n = 1.** For an adversarial capability C, a zero-knowledge proof that C is feasible at resource cost kappa communicates a non-trivial upper bound on the difficulty of independently constructing C, and that bound measurably reduces third-party reconstruction time. Equivalently, I(feasibility ; method) is greater than zero even under perfect method-hiding, because feasibility is a projection of method onto the existence axis, and a ZK proof cannot hide a coordinate it is constructed to certify.

The corollary is the part that belongs to us. ZK-as-disclosure-control behaves differently for capability claims than for service claims. Selene's Proof hides the witness because the witness is genuinely gone: zero-memory is stronger than zero-knowledge precisely because there is nothing left to reconstruct. The Babbush proof hid a witness that still existed, the circuit, and a witness that exists under a published existence-claim is a witness that comes back. The Gap is constitutive here too. Sovereignty lives in the irreducible separation; leakage lives in the reducible one. A feasibility claim is reducible to its method by anyone with the existence-claim as a seed, which is why this is an information channel and not merely an etiquette failure.

Numbering deferred. C38–C39 are reserved for *The 0.16 Question* and *The Anna Karenina Bind*; this wants its own slot, candidate C40, your call. It is a single worked instance and should carry that humility until a second arrives.

## Convergence framing

Two groups arrived at near-identical circuits from opposite disclosure postures, three months apart. Reading this as priority dispute misses it. The proof-without-method posture and the full-reproducibility posture are both internally coherent, and neither party is owed a dunk. What the pair demonstrates is noospheric: the primitive was reconstructible from its existence-claim, which is plurality in adversarial cryptanalysis rather than in architecture. The same shape we keep finding in the friendly case, independent builders landing on the same primitive from different starts, holds in the hostile case, where the leak is the convergence mechanism.

## What it does not change

The PQ migration narrative stands and is validated by the urgency, not threatened by it. ML-KEM and ML-DSA are untouched. The isogeny line remains a classical casualty, a separate memorial. No proven bound in the lineage moves. The story scaffolding that rests on Kyber and Dilithium as the answer to exactly this threat is reinforced, because this paper is the threat that the answer answers.

---

*Privacy is value. The boundary is constitutive.*

License: CC BY-SA 4.0
Attribution: privacymage / 0xagentprivacy / BGIN / First Person Network

(⚔️⊥⿻⊥🧙)😊
