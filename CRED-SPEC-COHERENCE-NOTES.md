# Cred-spec coherence notes — first-person / DTG credential terminology

**What this is:** a coherence review of where agentprivacy-docs references DTG credential terminology, against
the **DTG Credentials Core Specification** (ToIP DTGWG, Working Draft v1.0,
<https://trustoverip.github.io/dtgwg-cred-spec/>), with ready-to-apply reconciliations. Prompted by reading
that spec as DTG ZKP Task Force co-chair.

**Governance / routing — READ FIRST.** The two richest targets live under `papers/`, which the V6 Rehydration
Pipeline (`papers/Programme/pipeline/CLAUDE.md`) declares **READ-ONLY canon**, and `E7-identity-vrc.md` is a
**generated extraction** ("generated artifacts are never hand-edited; fix inputs, rebuild"). So this doc does
**not** hand-edit any canon. Each gap below is routed:
- **Canon (`papers/…`)** → fix the *input source* and rebuild the extraction, or raise with role A0 / SOURCES.md;
  never a direct edit to the extraction or whitepaper.
- **Non-canon (`specs/`, `research/` letters)** → editable, but flagged here for your call given the gated
  private-repo rollout + FROZEN public `origin` ([[project_docs_publishing_flow]]). Nothing here is pushed.

Sibling map for the ZK side lives in `~/dtgwg-zkp-tf-mage/runtimes/CRED-SPEC-COHERENCE.md`.

---

## Gap 1 — five of six DTG credential acronyms are asserted but never defined  *(canon; route via pipeline)*

`papers/Programme/pipeline/extractions/E7-identity-vrc.md`, **E7-C26 (L199)** lists the set bare:
> "…a decentralised-trust-graph credential set of six credential types plus a relationship card (VRC among
> **VMC, VIC, VPC, VEC, VWC**, plus RCard)…"

Only VRC is expanded anywhere in the corpus. The other five never get an expansion (grep confirms zero hits for
any expansion form). **Reconciliation (cred-spec expansions):**

| Acronym | Cred-spec expansion | One-line role |
|---|---|---|
| VMC | **Verifiable Membership Credential** | membership in a VTC/VTN community |
| VIC | **Verifiable Invitation Credential** | authorises a prospective member to join |
| VPC | **Verifiable Persona Credential** | links a persona (P-DID) to a relationship |
| VEC | **Verifiable Endorsement Credential** | skills / reputation assertion on an edge |
| VWC | **Verifiable Witness Credential** | third-party attestation of a relationship (requires `taskContext`) |
| RCard | relationship card (**r-card**) | self-updating vCard analog carrying a VRC (planned DTG VDS) |

**Route:** add these expansions to the *source* the E7 extraction is built from (hearthold-build README /
tome-x), then rebuild — so the extraction stops asserting "six types" without defining five of them.

## Gap 2 — VRC concept drift: richer than the spec  *(NOT a defect — a contribution surface; flag only)*

The name is coherent everywhere (VRC = **Verifiable Relationship Credential**, incl.
`specs/vrc_promise_protocol_v3_3.md:1325`, `papers/whitepapers/swordsman_mage_whitepaper_v6_3.md:405`). But the
*concept* is broader than the spec's:
- Corpus: "Bilateral trust object proving **mutual comprehension**. **Promise bundle.**" (vrc_promise L1325);
  "VRCs are *promise bundles* — coordinated bilateral promises grouped for reuse" (whitepaper L411).
- Cred-spec: VRC is a bare **relationship attestation** (a signed edge; ZK proves possession + selective
  disclosure), with no economic/promise-theoretic semantics.

**Do not erase your richer definition to "match."** This is opportunity #9 in the ZKP-TF register: propose the
promise-bundle economics as an *extension the spec's minimal VRC schema can carry*. **Action:** add a one-line
reconciliation note where VRC is defined ("same acronym as the DTG cred-spec's VRC; agentprivacy extends it with
promise-theoretic / ERC-7812 economics") rather than a rewrite. Canon copies route via pipeline; the `specs/`
copy is directly editable if you approve.

## Gap 3 — four-DID taxonomy: mis-ordered and unexpanded  *(non-canon; `research/`)*

`research/privacymage-response-fpp-zkp-progress.md:103`:
> "The four-DID taxonomy **(R-DID, M-DID, P-DID, C-DID)** maps onto the pseudonym derivation…"

Order differs from the spec and the letters are never expanded (latent collision — an implied "Principal/Context"
reading would be wrong). **Reconciliation (cred-spec):** canonical order **R/M/C/P-DID** =
**R**elationship / **M**embership / **C**ommunity / **P**ersona DID. Suggested edit: "the four-DID taxonomy
(R-DID relationship, M-DID membership, C-DID community, P-DID persona)". Directly editable (non-canon) on your OK.

## Gap 4 — "First Person credential" conflates PHC and IDVC; IDVC absent entirely  *(mixed)*

"First Person credential" is used two ways in `research/privacymage-response-fpp-zkp-progress.md`:
- L23 as the personhood credential specifically: "two credential types: **personhood credentials (PHCs)**… and
  verifiable relationship credentials (VRCs)…" ✅ coheres.
- L27 as the whole sovereignty stack: "the next question the **First Person credential** must answer…" — loose.
- `grimoires/spellbook_v5_0_canonical.md:82` / `reference/GLOSSARY_MASTER_v4_0.md:2182` flatly equate
  👤✓ "First Person credential" = "Verified personhood."

The cred-spec now gives these **distinct** names: **PHC** (a governed VMC: real-human + one-per-person) and
**IDVC** (Identity Verification Credential — the identity-proofing input, e.g. Veriff/Jumio; *not* a DTG
subtype). **IDVC appears nowhere in the corpus** — a pure gap. **Reconciliation:** where "First Person
credential" means personhood, keep it tied to **PHC**; add at least a pointer to **IDVC** as the distinct
identity-proofing carrier so the two aren't collapsed. Glossary lives under `reference/` (check pipeline status
before editing); the letter is non-canon.

## Gap 5 — VTA load-bearing but unexpanded; VTC / VTN absent  *(mixed)*

`research/privacymage-response…:103` uses "each **VTA**", "the **VTA** separation theorem", "**OpenVTC**
infrastructure" without expansion; VTC/VTN never appear as standalone terms. **Reconciliation (cred-spec):**
- **VTA** = **Verifiable Trust Agent** (a DTG node's digital agent; local VTA on edge, cloud VTA on servers).
- **VTC** = **Verifiable Trust Community** (a DTG node, C-DID-identified).
- **VTN** = **Verifiable Trust Network** (a set of VTCs under a governance framework).
Add expansions at first use. (Note: our ZKP-TF README already aligns VTA capitalization to the spec.)

---

## Summary of routing

| Gap | Where | Kind | Route |
|---|---|---|---|
| 1 five acronyms | E7-C26 (canon) | definition-absent | fix input → rebuild extraction |
| 2 VRC drift | specs + canon | substantive (contribution) | reconciliation note, not rewrite; your call |
| 3 four-DID | research letter | cosmetic + correctness | direct edit on approval |
| 4 First-Person/PHC/IDVC | research + reference | conflation + gap | direct edit (letter) / pipeline (glossary) |
| 5 VTA/VTC/VTN | research letter | definition-absent | direct edit on approval |

**Nothing has been edited in the corpus.** Confirm which non-canon edits (Gaps 3–5 in `research/` + the `specs/`
note in Gap 2) you want applied, and how you want the canon gaps (1, and the canon side of 2/4) routed through
the pipeline. The spec-side expansions above are ready to drop in.
