# 2026-07-18 · E8 built · the Extraction Frontier Cycle, run 3

**Verdict first.** E8-ceremony-governance is drafted: 41 claims at head C97, four checks pass, manifest updated, ledger L156. The frontier stands at **9 of 11 built** (E5 and E11 remain). WP-21 is unblocked. Six conflicts were found; two were resolved same-day where the fact was already settled, and one is a genuine latent bug in a byte-exact reference implementation.

## What this extraction established

- **Ceremony as governance, end to end:** seats fill only by bilateral ceremony (never by fiat), identity is membership-in-the-sealed-shape, the multiplicative lock (no partial seal), commit authority split at the moment of creation (only the boundary agent draws the edge), witnesses hold the recordings while participants hold the artifact, and refusal is a valid outcome, not a failure.
- **A real evidence base, honestly bounded:** four performed records (the 03-29 bilateral witness ceremony, the N=3 forge base, the honest-Sun blade, and the 07-18 RPP inscription — the last with a self-referential provenance note since this pipeline produced it), plus the cross-implementation seal byte-match as the one end-to-end exercise of the byte-exact mandate.
- **The L006 fence held:** the retired token appears nowhere in the g42 sources.

## The finds

1. **A latent hash divergence in the byte-exact repo (E8-C14):** the Python reference emits raw UTF-8; the "faithful port" escapes non-ASCII. Any non-ASCII proverb would hash differently across the two — precisely the false negative the reference exists to prevent. Guard comment placed in `hash.js`; the encoder fix changes hash behavior and is the First Person's call.
2. **Prose exclude-set corrected (E8-C13):** TRUST-PROTOCOL named two pruned fields where code and AXIOMS carry four. Fixed, with the correction noted in-line.
3. **The one-word-two-metrics disease is systemic:** tier-by-stratum vs tier-by-laps is the *third* instance of the class (after E3's lap-units and tier-ladders). A class-level vocabulary ruling is requested instead of a third local patch.
4. Also filed: the `succ` referent drift (principal vs validated result), the 478-vs-119 graph snapshots both claiming "Operational", the flagship blade's three irreconciled forge dates, and the Pretext library's two candidate repo URLs (A4).

## Handoff

- **First Person:** four small dispositions — the hash.js encoder (fix to match the reference, or constrain payloads ASCII-only in schema); the class-level tier/lap vocabulary ruling; the succ referent; the blade-date reconciliation. Plus the standing three from run 2 (E6-C06 modal seam, E6-C36 delegation grammars, the hearthold fork). All diffs uncommitted, now spanning five repos (agentprivacy-docs, cityofmages, agentprivacy_master, game42, and the E3-run touches).
- **Runtime, next:** E11 implementation-record (cycle run 4), then E5 with A3 seated — that completes the frontier. WP-21's chain can start any session.
- **Future touch:** diff the two ceremony-engine-spec copies (FORGE copy ~2.3KB larger, unverified delta).
