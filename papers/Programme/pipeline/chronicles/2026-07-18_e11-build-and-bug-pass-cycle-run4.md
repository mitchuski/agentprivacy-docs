# 2026-07-18 · E11 built · bug pass · the Extraction Frontier Cycle, run 4

**Verdict first.** E11-implementation-record is drafted: 25 claims at head C97, four checks pass. The frontier now stands at **10 of 11 built** — only E5 (algebraic-home) remains. Along the way the bug queue was worked: one real bug fixed (the ECDH handshake, both extensions), one earlier "bug" refuted (E8-C14), and every code-behavior claim in the extraction was execution- or read-verified before it landed.

## The Part-D headline

The live system **signs but does not verify**. Real ed25519 signing exists (private key burned to sessionStorage); no ed25519 signature-verification path exists anywhere in the surveyed codebase. All live verification is content-hash re-derivation (κ, packet proof). The corpus carries this boundary honestly in its own comments ("Phase 1: hash-only ... Phase 3 will upgrade"). That one sentence is the conformance truth WP-20/WP-23 must state exactly.

## The bug pass (L157 + L158)

- **E8-C14 REFUTED (L157):** the claimed non-ASCII hash divergence between game42's Python reference and its JS port does not exist — direct byte-level test over six vectors showed them identical (both raw UTF-8). The warning comment I had placed in a reference implementation was itself the defect. Minted a method rule now in the cycle plan: sweep claims about *code behavior* get executed, not just quoted. The E11 κ sweep independently confirmed the same fact.
- **Real bug FIXED (L158):** the ECDH handshake round-trip was structurally broken in both extensions — the responder acknowledged without returning its public key, so the shared secret was never derived on either side. Both `KEY_EXCHANGE` handlers now derive the secret and return their public JWK. The fix completes the handshake; the derived key is still unused (plaintext channel) — a separate deployment gap recorded, not silently expanded.
- **Settled from code:** E8-C38 (478-vs-119 graph — both stale; live is 807/1738), the fog-of-war retirement (code retained and inert, retired by data de-population — the E8-C35 phrasing corrected at both spec copies), the three ceremony-engine-spec variants mapped.

## Two new contested (code/spec dispositions, not register)

- **E11-C06:** one canonical serializer hand-copied into four master modules; agreement unenforced — a drift risk wanting a shared module or golden-vector test.
- **E11-C15:** SPELLWEB_INTEGRATION_SPEC_v2 is wholesale non-conformant to the live Vite/D3 build; its "must not modify" list names files that don't exist. Retire or rewrite.

## Handoff

- **First Person:** the ECDH fix is applied (both extensions, uncommitted). The queue's hash.js item is DROPPED (refuted). No blocking rulings from this run — the signing-stub / placeholder-ID / unused-secret / additive-leakage-measurement items are pre-ship deployment gaps E11 records, not defects needing a call. Optional Phase-3 builds if wanted: consume the shared secret to encrypt the channel; implement signSpell + receiver verify. Standing queue from earlier runs unchanged (E6-C06 modal seam gates WP-18; the tier/lap vocabulary class ruling; the succ referent; the delegation grammars; the hearthold fork).
- **Runtime, next — the last frontier build:** E5 (algebraic-home) with A3 (formalist) seated. It is flagged highest-risk; expect many CONTESTED items and do not force resolution. After E5 the frontier flips to maintenance (widening sweeps + the weekly coherence loop = WP-13).
- **Unlocked:** WP-10 has its full chain (E1+E3+E11); WP-20/WP-23 gain the conformance matrix; WP-08 gains E11-C17 (additive leakage) as a measurable benchmark target.
- Diffs now span six repos (agentprivacy-docs, cityofmages, agentprivacy_master, game42, swordsman-blade, mages-spell), all uncommitted.
