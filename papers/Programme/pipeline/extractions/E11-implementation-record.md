---
extraction: E11-implementation-record
tier: internal
sources: [kappa-impl, master-lib-impl, dual-extensions, spellweb-impl, star-holospace, skills-corpus, hearthold-build, g42-seal-ref]
swept_complete: true
owner: A1
register_head_at_build: C97
build_note: built 2026-07-18 at the fourth Extraction Frontier Cycle run; conformance-evidence for Part D; implemented-vs-specified stated per item (L008). Every code-behavior claim in this extraction was execution-verified or read-verified directly, not carried from a reader's assertion (the L157 rule; the E8-C14 refutation is why). g42-seal-ref and hearthold-build reused from E8/E6 sweeps; skills-corpus at stated depth (register documents only, per E3/E10 precedent)
---

# E11 · Implementation Record

Claim-cluster for what actually RUNS versus what is specified, across the model-in-code: the κ content-addressing implementations, the master library (City Key chain, charge/mana, proof packets, ed25519 identity), the two browser extensions, the spellweb engine, the star holospace, and the honest deployment boundary of each. This is the conformance-evidence extraction for Part D; every claim states implemented-vs-specified per the L008 discipline. Feeds WP-10 (developer edition), WP-06/WP-20/WP-23 (standards conformance matrix), WP-22 (ZK note).

Standing boundary for the whole file: "ZK" in the live system means SHA-256 commitments + Ed25519 signing + κ content-addressing (L008). There is real signing but, across the entire surveyed codebase, no signature VERIFICATION path — all live verification is content-hash re-derivation. That asymmetry is the single most load-bearing fact here (E11-C09).

## Claims

### E11-C01
- **STATUS:** Verified-record (reference implementation, runs client-side)
- **SOURCE:** kappa-impl sigil/index.html :251-258, star/index.html :597-604, lattice/index.html :350-357
- **CLAIM:** κ is derived identically across the three soulbis pages: κ = "sha256:" + hex(SHA-256(canonicalJSON(obj without kappa))), where canonicalJSON recursively sorts object keys, uses no whitespace, and serializes every primitive/string through JSON.stringify, converted to bytes by TextEncoder (UTF-8). Byte-for-byte identical code in all three files. The excluded field is only kappa (shallow delete on a spread copy); prior and all other fields are inside the preimage.
- **CITATIONS:** SHA-256; WebCrypto
- **FEEDS:** WP-10, WP-22

### E11-C02
- **STATUS:** Verified-record (string-encoding conformance, empirically tested)
- **SOURCE:** kappa-impl (JSON.stringify + TextEncoder path); cross-checked against g42-seal-ref canonical_serialise.py; direct byte-level test 2026-07-18 (L157)
- **CLAIM:** The canonical serializers emit raw UTF-8 for non-ASCII string content, NOT \uXXXX escapes — JSON.stringify escapes only quote, backslash, and control chars, then TextEncoder emits UTF-8. This was verified byte-identical to the Python reference (json.dumps ensure_ascii=False) over six vectors including accented Latin, CJK, an astral emoji, control chars, and em-dash. The only residual divergence is lone surrogates (invalid Unicode): JS escapes per ES2019 well-formed stringify, Python raises on encode. Conformance rule: keep payloads valid Unicode and the two implementations agree to the byte. This REFUTES the E8-C14 claimed divergence.
- **CITATIONS:** none
- **FEEDS:** WP-10, WP-22

### E11-C03
- **STATUS:** Verified-record (the L5 re-derivation law, implemented)
- **SOURCE:** kappa-impl sigil :400-404, star/lattice :605-609/:358-362; master-lib-impl city-key-charge.ts verifyCityKeyKappa :182-187
- **CLAIM:** Verification is re-derivation, never trust of the stored label (holospaces Law L5): on import the stamped kappa is re-derived from content and string-compared, mismatch flagged; a key carrying no kappa is not rejected but named ("it learns its name here"). A mismatch is intentionally NON-BLOCKING — κ is "a name, not an authority" (register C66). This is a genuine content-hash check, never signature verification.
- **CITATIONS:** none (register C66)
- **FEEDS:** WP-10, WP-22

### E11-C04
- **STATUS:** Verified-record (the one published golden conformance vector)
- **SOURCE:** kappa-impl sigil :259-273; master-lib-impl proof-packet-digest.ts :18-22
- **CLAIM:** The single explicit byte-exact test vector in the corpus is the packets Merkle root: three leaves SHA-256(utf8 "packet-alpha"/"packet-beta"/"packet-gamma"), sorted, paired as SHA-256(left+"|"+right) with odd promotion, yield root sha256:07f20f689c8bef2d8a9a2a71d94e7014ea8398cc603b0ff72dadba5c517983d1. The same vector appears in both the soulbis sigil page and the master library — a genuine cross-implementation golden value. Note: the star sigil doc cites a DIFFERENT κ conformance vector (sha256:0b4916...) for the key itself; the two are different objects (key-κ vs packets-root), not a conflict.
- **CITATIONS:** SHA-256
- **FEEDS:** WP-10, WP-22

### E11-C05
- **STATUS:** Verified-record (the City Key chain as built)
- **SOURCE:** master-lib-impl city-key.ts buildCityKey :293-348, canonicalCityKeyJSON :356-366, deriveCityKeyKappa :373-381
- **CLAIM:** The City Key is really constructed from achievement state (achievements → lit vertices → sparse descriptions + focus → optional κ seal) and κ-fingerprinted over the same custom canonical serializer as the soulbis pages, written to a downloadable JSON with κ re-derived over the actual bytes. IMPORTANT: there is NO "VRC → κ" numeric transform and NO signature — VRC mana is carried and charged separately and does not enter the exported key's κ preimage at build time. Byte-exactness against the soulbis pages is a stated requirement; the reference cited in-code is the star repo, NOT game42 (no game42 reference exists anywhere in master src).
- **CITATIONS:** none
- **FEEDS:** WP-10, WP-20

### E11-C06
- **STATUS:** CONTESTED (drift risk: one serializer, four hand-copies)
- **SOURCE:** master-lib-impl city-key.ts, proof-packet.ts, proof-packet-digest.ts, chart-reading.ts (each re-implements the canonical serializer)
- **CLAIM:** Four independent master-library modules each re-implement the SAME custom canonical serializer (recursive key-sort, no whitespace, self-field deleted, undefined dropped, SHA-256, sha256:+hex) by duplication, not by importing a shared function. They agree today, but nothing enforces agreement — a byte-level conformance risk internal to one repo, the same class as the E8-C03 two-parameterization split. A shared module or a golden-vector test across all four would close it. Ledger entry filed; the refactor is a code disposition.
- **CITATIONS:** none
- **FEEDS:** WP-10

### E11-C07
- **STATUS:** Verified-record (real accounting ledger)
- **SOURCE:** master-lib-impl city-key-charge.ts chargeCityKey :219-282; vrc-mana.ts :41-72; vrc-allocation.ts :48-93
- **CLAIM:** The charge/mana accounting is a real deduplicated ledger state machine: three charge kinds each dedup'd by an id (generate = max(1,floor(laps)) + tour bonus; charge = sum floor(spent) + completion bonus; cast = flat 3 per new chart κ), accruing into a single monotonic VRC-mana counter, with a vertex-keyed staking pool (commit clamps to free balance, withdraw preserves monotonicity). Real arithmetic in localStorage. Honesty note carried at source: presence mana is declared non-transferable, non-attesting LOCAL COLOR (PVM V6 §15, G3-signed) — a real value explicitly NOT an attestation input.
- **CITATIONS:** none
- **FEEDS:** WP-10

### E11-C08
- **STATUS:** Verified-record (proof packets: sealed = commitment only, real privacy behavior)
- **SOURCE:** master-lib-impl proof-packet.ts buildProofPacket :241-288, WITNESS_MODE :120-144, canonicalPacketJSON :157-169; spellweb-impl proofPackets.ts :53-94
- **CLAIM:** Proof packets are content-addressed with a witness-derived privacy mode (a pure function of witness type, explicit 20-witness map, default sealed): sealed and refractive modes store ONLY a SHA-256 commitment of the content — raw content never enters the packet (real privacy behavior, not a stub); the L5 re-derivation self-verifies. The spellweb ingester dedupes on the content-addressed proof string and does type-shape validation only (no cryptographic check), consistent with the format-spec Phase-3 deferral. CAVEAT (deployment boundary): when crypto.subtle is unavailable (non-secure context), proof/commitment become empty strings — structurally real, cryptographically empty.
- **CITATIONS:** SHA-256
- **FEEDS:** WP-10, WP-22, WP-23

### E11-C09
- **STATUS:** Verified-record (the load-bearing asymmetry: signing exists, verification does not)
- **SOURCE:** master-lib-impl ceremony/keygen.ts generateKeyPair/signMessage :27-42, ceremony/storage.ts :127-128; grep-confirmed absence of ed.verify across master src; dual-extensions swordsman signSpell :287+ (placeholder)
- **CLAIM:** The live system has REAL ed25519 keygen and signing (@noble/ed25519: randomSecretKey, getPublicKeyAsync, signAsync), with the private key burned to sessionStorage and the public key persisted — but NO ed25519 signature VERIFICATION path exists anywhere in the surveyed codebase (grep-confirmed). All "verification" in the live site is content-hash re-derivation (κ, packet proof), never signature checking. The Drake Orb badge "signature" is an explicit non-cryptographic content hash (Phase 1). The extension signSpell returns the literal "placeholder_signature" with a TODO, and receivers never verify. Deployment boundary quotes present in source: "Phase 1: hash-only ... Phase 3 will upgrade to real ed25519".
- **CITATIONS:** Ed25519 (@noble/ed25519)
- **FEEDS:** WP-10, WP-20, WP-23

### E11-C10
- **STATUS:** Verified-record (canonical lattice encoding, L010-concordant)
- **SOURCE:** master-lib-impl lattice-vertex.ts :12-19, :40-54; proof-packet-digest.ts :119-120
- **CLAIM:** The 6-cube vertex codec is implemented as POSITIONAL binary, not a lookup table: bit(5-i) for dimension i, so Protection = bit 5 = weight 32 down to Value = bit 0 = weight 1, via (vertex >> (5-i)) & 1. Two independent modules assert the same "MODEL lock, unified 2026-06-12" convention. This matches the g42 AXIOMS A1 map (E8-C10) and the lattice-encoding anchor (the L010 fence's canonical side) — a three-way implementation concordance on the encoding.
- **CITATIONS:** none
- **FEEDS:** WP-10, WP-19

### E11-C11
- **STATUS:** Verified-record (the spellweb forge runtime, live counts)
- **SOURCE:** spellweb-impl src/data/nodes.ts (807 node literals), edges.ts (1738 source entries), forge.ts :40-227, SpellCeremony.tsx :842-846
- **CLAIM:** The live spellweb graph is 807 nodes / 1738 edges (imported from the TS data files; the 4-array edge split is a TS compiler workaround, not a data-model split), NOT the 478 or 119 figures the ceremony specs cite (those are stale/dated snapshots) and NOT the dead 16-node public/spellweb/nodes.json. The forge runtime is real and pure-functional: a lap is counted on the orb's geometric return to the start node (not a timer); charge is a Fibonacci-threshold function of lap count (spark/ember 13/flame 21/inferno 38/dragon 62); the six dimension bits are gated by PER-DIMENSION constants (the "30s AND laps>=2" condition applies ONLY to the memory bit); tier from laps (62 dragon / 21 heavy / else light); stratum = Hamming weight; hex = 6-bit pack, protection MSB. This settles E8-C38's 478-vs-119 (both stale) and confirms the E8-C36 tier-metric collision at the code level (tier IS lap-count here, stratum is the dimension-count — two real quantities the docs conflate under one word).
- **CITATIONS:** none
- **FEEDS:** WP-10

### E11-C12
- **STATUS:** Verified-record (blade hash chain + commit-reveal, local append log)
- **SOURCE:** spellweb-impl forge.ts blade chain :71-124, commitment :126-150
- **CLAIM:** Forged blades form a SHA-256 hash chain in localStorage (each blade hashes canonical JSON including the previous hash), and a real commit-reveal exists (16-byte random nonce, commitment = SHA-256(constellationHash+nonce), verify by recompute, locked at evoke start). But the chain is a local append log, NOT a re-verified ledger — chain integrity is not checked on import.
- **CITATIONS:** SHA-256
- **FEEDS:** WP-10, WP-22

### E11-C13
- **STATUS:** Verified-record (import is trust-on-ingest; the Phase-3 boundary, confirmed from code)
- **SOURCE:** spellweb-impl SpellWeb.tsx import :2556-2706 (commitmentVerified:true "Trust the import"), workshop-provenance.ts regex parse :45-139
- **CLAIM:** The artefact .md import path parses frontmatter and body by hand-rolled per-key REGEX (no YAML parser, no schema validation) and constructs a proof trusted unconditionally: commitmentVerified is hard-set true, no signature/hash recomputation, bladeHash faked from the constellation hash. blade_signature/blade_hash are EMITTED on export but IGNORED on import. This exactly confirms the format-spec §8 statement "cryptographic verification ... Phase 3" from the code side — the honest deployment boundary of the witness-import feature.
- **CITATIONS:** none
- **FEEDS:** WP-10, WP-23

### E11-C14
- **STATUS:** Verified-record (fog-of-war: retired by data, code retained and inert)
- **SOURCE:** spellweb-impl graph.ts :302-307, SpellWeb.tsx :1032-1033, :1218-1231
- **CLAIM:** The fog-of-war mechanism (hiddenUntilWitness field, silhouette render, witnessedShops localStorage) is NOT removed from code — it is dormant because no canonical node currently carries the tag (retired for cast/universe 2026-05-11, "reserved for future secret-lore nodes"). Retirement was executed by de-populating the data, not deleting the runtime. This corrects the E8-C35 resolution's "legacy metadata, no display effect" phrasing (the code path is live-but-inert, not absent); the artefact-spec notes are updated to say so (L158).
- **CITATIONS:** none
- **FEEDS:** WP-10

### E11-C15
- **STATUS:** CONTESTED (a whole spec superseded, its "must not modify" targets nonexistent)
- **SOURCE:** spellweb-impl docs/SPELLWEB_INTEGRATION_SPEC_v2.md vs package.json + src/main.tsx + src/components/SpellWeb.tsx
- **CLAIM:** SPELLWEB_INTEGRATION_SPEC_v2 prescribes a Next.js app-router / dual-route (/spellweb + /nexus) / react-force-graph / JSON-loader / GitNexus-pipeline architecture; the running app is a single-page Vite + React + raw-D3 build centred on one component, and NONE of the spec's named files exist (its "Files That Must Not Be Modified" list points at files absent from the tree). The spec has no RFC-2119 MUSTs (its normative force is prose). Recorded as non-conformant-to-build; a spec disposition (retire or rewrite), not a code fix. Ledger entry filed.
- **CITATIONS:** none
- **FEEDS:** WP-10

### E11-C16
- **STATUS:** Verified-record (two built extensions; real channel, real role split)
- **SOURCE:** dual-extensions DUAL_EXTENSION_ARCHITECTURE.md :37-46, ceremony-channel.ts :136-294, both dist/ trees
- **CLAIM:** Two Chrome MV3 extensions really exist and are built (swordsman-blade v0.3.1, mages-spell v1.2.1): the boundary agent asserts terms and owns the blade/MyTerms path, the delegation agent scans and builds constellations. The cross-extension channel is a real plaintext chrome.runtime.sendMessage handshake (SWORD_PRESENT → MAGE_ACKNOWLEDGE) plus a 30fps position sync and ceremony verbs. The message vocabulary in the shipping channel matches AETHER.md, NOT the stale DUAL_EXTENSION_ARCHITECTURE.md verb list (a doc-vs-code drift, the arch doc stamped v1.0.0 has drifted from the shipping code).
- **CITATIONS:** none
- **FEEDS:** WP-10

### E11-C17
- **STATUS:** Design-assumption (the additive-leakage GUARANTEE is prose, unmeasured; GR-8 honesty item)
- **SOURCE:** dual-extensions DUAL_EXTENSION_ARCHITECTURE.md :41
- **CLAIM:** The extension architecture states "Information Theoretic Guarantee: I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M)" but NO code measures, estimates, or enforces it, and the identity holds only if the two channels are independent given X — which the implementation does not establish (the extensions share chrome.storage, the same repertoire, and exchange messages, which couples them). Flagged (GR-8): a "guarantee" that is an unmeasured architectural assertion, the honesty item of the extension pair. Note the same doc set declares the Σ/Δ/Γ axis product MULTIPLICATIVE while this leakage claim is ADDITIVE — two composition models side by side, neither instrumented.
- **CITATIONS:** none (the additive-leakage claim's formal home is the E1/WP-07 cluster; here it is the UNMEASURED-in-code record)
- **FEEDS:** WP-10, WP-08 (benchmark: this is a thing a benchmark could actually measure)

### E11-C18
- **STATUS:** Design-assumption (crypto specified, handshake was broken then fixed, still unused)
- **SOURCE:** dual-extensions swordsman/mage background/index.ts performKeyExchange + KEY_EXCHANGE handler (fixed 2026-07-18, L158)
- **CLAIM:** The ECDH-P256 → AES-GCM-256 handshake code exists in both extensions but shipped BROKEN: the responder replied acknowledge-only with no public key, so the shared secret was never derived on either side. Fixed 2026-07-18 (both handlers now return their public JWK and derive the secret). The fix makes the handshake complete but NOT used — the derived key is still never consumed (no encrypt/decrypt anywhere; the channel is plaintext). Signing is likewise stubbed (signSpell returns "placeholder_signature", receivers never verify) and the extension IDs are placeholders (cross-extension messaging cannot resolve until Web Store publishing). These are pre-ship deployment gaps the docs flag, recorded here as the extension pair's boundary, not defects to patch further.
- **CITATIONS:** ECDH P-256; AES-GCM
- **FEEDS:** WP-10, WP-23

### E11-C19
- **STATUS:** Verified-record (the aether sync discipline, verified in-sync)
- **SOURCE:** dual-extensions AETHER.md :354-360; whole-tree diff run 2026-07-18
- **CLAIM:** The shared types/data/meaning contract is kept byte-identical between the sibling extension repos by manual discipline ("diff -rq ... if this prints anything the aether is broken"). Verified currently in-sync: the three shared docs and shared/types are byte-identical across the two repos, diff clean. This is a real, testable governance discipline (the E6-C19 witness-promise idea applied to source), currently holding. The only legitimate divergences are manifest identity and src/ layout.
- **CITATIONS:** none
- **FEEDS:** WP-10, WP-27

### E11-C20
- **STATUS:** Verified-record (the sigil PNG carrier + κ-avalanche, runs)
- **SOURCE:** star-holospace HOW_THE_SIGIL_WORKS.md :24-113; kappa-impl sigil PNG :293-323, buildGrid8 :509-512
- **CLAIM:** The PNG tEXt carrier is fully implemented and runs client-side: the full City Key JSON is base64'd into a PNG tEXt chunk (keyword cityKey, hand-computed CRC-32, inserted before IEND), leaving a valid PNG; on import the κ is re-derived (never trusted). The sigil light is content-derived: 64 SHA-256 hex glyphs map one-per-vertex, each nibble (0-15) setting vertex brightness — one edited description re-lights ~60 of 64 vertices (the avalanche is SHA-256 diffusion). Palette and geometry are chosen/expressive; light is derived. Honest boundary stated in-code: "portability, not secrecy — the full JSON is extractable from the image."
- **CITATIONS:** SHA-256; PNG tEXt; CRC-32
- **FEEDS:** WP-10, WP-22

### E11-C21
- **STATUS:** Verified-record (DH-PSI common ground, built with a documented deviation)
- **SOURCE:** star-holospace CHRONICLE_ECDH_PSI_HANDOFF :1-24, :98-108; skye/index.html :358-395
- **CLAIM:** A two-party private-set-intersection handoff is built and running on /skye: each bearer blinds their touched-vertex set with a secret scalar, two files cross, only the intersection and set sizes are learned. It DEVIATES deliberately from its own §3 proposal: instead of Curve25519/ristretto255 via a vendored library, it uses the RFC 3526 2048-bit MODP group (id 14), hash-to-QR by squaring, 256-bit short exponents, Fisher-Yates shuffle, secret in sessionStorage per exchange. The round-3 artifact is "a report, not a proof — the κ-commitment ZK layer remains the v3 rung" (the honest boundary; the acceptance-check pass is the chronicle's assertion, not independently re-run).
- **CITATIONS:** RFC 3526 (modp2048); Diffie-Hellman PSI
- **FEEDS:** WP-10, WP-22, WP-19

### E11-C22
- **STATUS:** Design-assumption (holospace provisioning blocked; the key round-trip is what runs)
- **SOURCE:** star-holospace HOLOSPACE.md :1-39, :104-129; CONCEPT_COMPRESSION_REHYDRATION_DUAL_AGENTS.md :36-137
- **CLAIM:** The key compression → rehydration round-trip is built (import re-derives κ and rebuilds palette/geometry/lit across all four pages; boundary agent gets stance/tier/lit, delegation agent gets descriptions/focus/trace — the dual-agent re-equip). But the holospace PROVISIONING (κ-addressed devcontainer, IPFS pin, .holo artifact) is explicitly NOT built — blocked on a third-party operator key; the concept doc's stations are self-marked incomplete. The "reconstitutes as two agents, never as a profile of the person" is the design intent, the round-trip is the running part.
- **CITATIONS:** none
- **FEEDS:** WP-10, WP-19

### E11-C23
- **STATUS:** Verified-record (the site's model-in-code is real state, not display scaffolding — with named exceptions)
- **SOURCE:** master-lib-impl promises/ (types :9-72, storage :13-59), trust/tiers.ts :9-18, chart-reading.ts :120-188; model-page.ts :278-322 and grimoire-ipfs.ts (the scaffolding exceptions)
- **CLAIM:** Most master-library protocol objects are real local state, not typing scaffolding: the promise ledger (real add/update/delete lifecycle, spell→constellation emoji extraction, single-device — no signing or cross-agent exchange), the trust-tier function (real threshold scoring: completedPromises*3 + studiedActs → blade/light/heavy/dragon, over self-reported local counters — real scoring on unverified inputs), the chart-reading κ + proof-packet projection. The EXCEPTIONS, explicitly display/typing scaffolding: model-page.ts (static merge/sort of baked conjecture JSONs; the authoritative register is mirror-generated offline from agentprivacy-docs, cite-never-edit) and grimoire-ipfs.ts (const IPFS pin pointers, no fetching). The spellweb builder is real geometry (96 hypercube edges, popcount rows) driving visualization.
- **CITATIONS:** none
- **FEEDS:** WP-10, WP-20

### E11-C24
- **STATUS:** Verified-record (the conformance-authority chain points at star, never game42)
- **SOURCE:** master-lib-impl city-key.ts :353-355 and grep across master src; kappa-impl (soulbis = the star pages)
- **CLAIM:** The stated byte-exact conformance authority for κ across the master library is the star repo (github.com/mitchuski/star, HOLOSPACE.md, HOW_THE_SIGIL_WORKS.md §7, swordsmans-key.interop.md) — cited repeatedly in comments. There is NO game42 reference anywhere in master src. So two byte-exact κ reference lineages coexist in the corpus: the soulbis/star κ (excludes kappa only, sha256:-prefixed) and the game42 seal (excludes four fields, bare hex) — the E8-C03 two-parameterization fact, seen from the implementation side. Any cross-lineage κ comparison must state which parameterization it uses.
- **CITATIONS:** none
- **FEEDS:** WP-10, WP-20

### E11-C25
- **STATUS:** Verified-record (the aggregate honest-boundary ledger; the Part-D headline)
- **SOURCE:** master-lib-impl in-source Phase markers (types.ts :51-52, storage.ts :127, spellbook-storage.ts :395, first-artifacts.ts :1034, districts.ts :196, city-key.ts :155); the per-claim boundaries above
- **CLAIM:** The corpus carries its deployment boundary honestly in-source, and the aggregate is the Part-D conformance statement: real and running = κ content-addressing (four surfaces, byte-tested), commit-reveal, proof-packet sealing, ed25519 SIGNING, the charge/mana ledger, the forge runtime, the extension channel, DH-PSI, the key round-trip; specified/stubbed/blocked = ed25519 VERIFICATION (absent everywhere), the additive-leakage guarantee (unmeasured), spell signing (placeholder), the extension shared secret (now derivable but unused), holospace provisioning (blocked on operator key), measured-geometry producers, DID fields ("WILL BE FILLED"), and the κ-commitment ZK rung. The one-sentence Part-D truth: the system content-addresses and signs, but does not yet verify signatures or measure its information-theoretic claims — and it says so in its own comments.
- **CITATIONS:** none
- **FEEDS:** WP-10, WP-20, WP-23, WP-08

## Contested items

| Item | Conflict | Ledger |
|---|---|---|
| E11-C06 | One canonical serializer hand-copied into four master modules; agreement unenforced | L158 · shared-module/golden-test refactor = code disposition |
| E11-C15 | SPELLWEB_INTEGRATION_SPEC_v2 wholesale non-conformant to the live Vite/D3 build; its "must not modify" targets do not exist | L158 · retire-or-rewrite the spec = disposition |

## Notes for consumers

- The load-bearing Part-D fact (E11-C09/C25): real signing, no signature verification anywhere; all live verification is κ re-derivation. Any conformance/standards artifact (WP-20/WP-23) must state this exactly.
- E11 SETTLES two prior contested items from other extractions: E8-C14 (encoding divergence REFUTED, E11-C02) and E8-C38 (478-vs-119 both stale; live = 807/1738, E11-C11).
- Two byte-exact κ lineages coexist (star/soulbis vs game42) with different exclude-sets and label formats (E11-C24); never compare across them without naming the parameterization.
- crypto.subtle-unavailable (non-secure context) degrades κ/proof/commitment to empty strings across the board — a uniform deployment caveat.

## Sweep record

| Source | Swept | Depth |
|---|---|---|
| kappa-impl | 2026-07-18, fanned reader + direct byte-level encoding test (L157) + code read of the fixed surfaces | sigil/star/lattice index.html + verify-static.cjs in full; string-encoding empirically tested |
| master-lib-impl | 2026-07-18, fanned reader (survey depth, headers/exports/key functions) | 14 module groups surveyed; ed.verify absence grep-confirmed; game42-absence grep-confirmed |
| dual-extensions | 2026-07-18, fanned reader + A1 direct read-verification of the ECDH/signing/ID claims before the fix | both repos' shared docs + background/ceremony-channel; diff -rq confirmed in-sync; the KEY_EXCHANGE bug read-verified and fixed |
| spellweb-impl | 2026-07-18, fanned reader (live TS data counts verified against the arrays) | nodes.ts/edges.ts counts, forge.ts, import path, fog code — all read-verified; 807/1738 counted |
| star-holospace | 2026-07-18, fanned reader | sigil/skye code + HOLOSPACE/CONCEPT/HOW_THE_SIGIL docs + the two chronicles |
| skills-corpus | reused from E3/E10 sweeps (register documents only) | stated depth: no per-skill folders; the progressive-disclosure discipline is the practice-record |
| hearthold-build / g42-seal-ref | reused from E6/E8 sweeps | the second-substrate and seal-reference implementation facts cross-referenced, not re-swept |
