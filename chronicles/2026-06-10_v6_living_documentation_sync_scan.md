# Chronicle · The V6 Living-Documentation Sync Scan

**Date:** 2026-06-10
**Status:** SCAN COMPLETE; all items PENDING. Companion to `chronicles/2026-06-10_v6_research_autopath_close.md` (the math path) and `plans/V6_SUITE_REFLECTION_MAP_2026-06-10.md` (the nine external repos, Wave R). This chronicle covers the surface that neither of those fully enumerates: the in-repo living documentation of agentprivacy-docs itself, the origin everything else reflects from.
**Author:** privacymage (with Claude Opus 4.8)
**License:** CC BY-SA 4.0

---

## What this scan found, in one paragraph

The V6 research and paper-generation layers are done: the register is the single authority (C1 to C89, G1-signed), `privacy_value_v6.md` is a complete formal spec, and the four canon papers plus PDFs are built. But V6 has not propagated down from the suite table into the bodies of the front-door documents, nor out into the orientation files. The pattern is uniform across the exterior: a V6 header was bolted on, and the body underneath still reads V5.4. A reader who skips the suite table, which is most readers, would still conclude the project is at V5.4. The autopath close chronicle's "what remains" names the glossary, the privacy_is_value pointer, and the documentation chronicle. The true in-repo list is larger, and it contains one coherence hazard worth naming first: there are now two competing version authorities in the repo that disagree.

## The coherence hazard: two version authorities that disagree

`README.md` and `GLOSSARY_MASTER_v4_0.md` both publish a master list of suite versions, and they now contradict each other.

- `README.md` Document Suite table (lines 46 to 58) names PVM V6 the current head.
- `GLOSSARY_MASTER_v4_0.md` "Document Suite Versions (Aligned)" table (lines 10 to 30) names V5.4 across the board, and the glossary states it "takes precedence when terminology conflicts."

So the document that claims precedence is the one that is most behind. Until one source of version truth is named (recommendation: the register plus a single SUITE_VERSIONS table that both files point at instead of restating), every other fix below can be re-contradicted by whichever table a reader trusts.

---

## Tier 1 · Front-door surfaces (highest reader traffic, all in agentprivacy-docs)

### README.md

| Location | Current state | V6 sync needed | On plan? |
|---|---|---|---|
| Line 5 (top header) | leads with "Version: 10.1 (First Person CLOSED)", a grimoire version | reconcile the top-line identity so the model-head (V6) reads first, not the grimoire head; the very first line should not be grimoire-anchored | NEW |
| Lines 19 to 23 (Quick Summary) | "V5 Advance" and "V5.4 Advance" cards; no V6 | add a "V6 Advance" card: the gathering turn, R(t) and t*, preconditions and external provenance, the exponential-to-linear gap (C83), Existence-Leak (C81) | NEW |
| Lines 164 to 171 (Mathematical Guarantees) | cites "Research Paper v3.2"; presents the reconstruction ceiling as static `R_max = (C_S + C_M)/H(X) < 1` | the single most important V6 result is missing from the front door: state R(t), t*, and the "Proven, conditional regime" conditioning per spec §5 and §11; re-point the citation to the V6 spec and register | NEW |
| Lines 291 to 300 (Confidence Levels) | "per Research Proposal v2.0", V5-era, no C81 to C89 | refresh against the register; name `research/CONJECTURE_REGISTER_V6.md` as the numbering authority (head C89) | NEW |
| Lines 304 to 339 (Reading Order by Audience) | every audience routed through V5.4 papers | the V6 spec, compressed, and companion are not in any path though the suite table calls them the current head; add V6 papers as the first stop per audience | NEW |
| Lines 409 to 423 (IPFS Archive) | V5.4 CIDs only | the four V6 PDFs are built but pin-gated behind G5; add a "built, pin pending" row now, real CIDs after G5 | NEW (interim) |
| Lines 513 to 524 (Citation Format) | V5.4 versions only | add the V6 spec citation form and the register citation form (head C89) | NEW |
| Lines 427+ (Document Coherence) | changelog stops at V5.4 | add the V6 arc entry: the gathering turn, R(t), the unified register, unified V6 labels (G3) | NEW |

### what-agentprivacy-is.md

The mission document, and thematically the surface most aligned with V6, is untouched.

- Line 28: "The Privacy Value Model (now at V5)". V6's whole thesis is the gathering turn, the WHO after V5's WHAT, opening outward in the second person to the City. That argument belongs here more than anywhere else and is absent. Needs a paragraph seating the gathering turn and the moving ceiling in the mission voice, and the "now at V5" string updated to V6.

### models/INDEX.md

- Line 7: heads "PVM V5.4 (Current)" though `privacy_value_model_v6.json` already exists in the directory; a reader of the index concludes V5.4 is current. Add a "PVM V6 (Current)" section, move V5.4 to previous.
- Lines 34 to 40: grimoire table tops out at v10.2.x; v10.4.0 (the 2026-06-09 head) is not listed.

---

## Tier 2 · Already on the plan (confirmed still pending)

| File | Item | Source |
|---|---|---|
| `GLOSSARY_MASTER_v4_0.md` | V6 addendum, roughly 30 terms: R(t), t*, moving ceiling, shelf life, Existence-Leak law, ages-progressively, obstruction amnesia (Grade-1 vs Grade-2), the presence-regime fence, the canonical figures (678x, 31,000x, 70:1, 74x), parity cube, octahedral gap, the Key as reading | Wave Log §5; also the suite-versions table (lines 10 to 30) must be reconciled per the hazard above |
| `privacy_is_value_v5.md` | the V6 supersede/pointer note; still headed Version 5.3 (line 7) with no forward link to `privacy_value_v6.md` | Wave Log §5 "privacy_is_value_v5.md pointer note" |
| `DOCUMENTATION_CHRONICLE.md` | the V6 arc entry | Wave Log §5 |

---

## Tier 3 · Interior body still at v3.x / v4.3 math (cited from the README reading paths)

These are not front-door files, but the README reading orders route researchers into them, and they still teach the static ceiling and cite papers older than even v4.3. At minimum their citation pointers should move to the register; a full math refresh is optional and larger.

- `research_proposal_v2_0.md`: repeated "Research Paper v3.8" citations; static `R_max` (lines 138, 769); on the Researcher and Investor reading paths.
- `vrc_promise_protocol_v3_3.md`: "Research Paper v3.8" foundation, static ceiling (lines 244, 1016, 1093, 1291).
- `promise_theory_reference_v1_4.md`: "Research Paper v3.8" deep-dive pointers (lines 700, 713).
- `spellbook_v5_0_canonical.md`: "Research Paper v3.6" (line 1761).
- `SECOND_PERSON_TOMES_INDEX_v1.md`: points to the v5_4 model JSONs (line 74); should also name the v6 JSON.
- `GLOSSARY_MASTER_v4_0.md` per-term Sources: many cite Research Paper v3.6 / v3.7 / v3.8 (lines 539 to 604, 952, 1455, 2386 to 2412), older than v4.3; pre-existing drift that the V6 glossary pass can clear.

## Tier 4 · Stale but not V6-blocking

- `QUICK_START.md`: the documents-available list (lines 32 to 44) names README v1.3, Whitepaper v4.8, Research Paper v3.6, Spellbook v5.0, Glossary v2.3. Many versions behind. Not V6-specific, but if the local port-7000 viewer is how anyone browses the repo, this is the index they land on first. Worth a refresh in the same pass.

---

## What this chronicle does not cover

The nine external repos (agentprivacy_master, cityofmages, myterms, blades, soulbis, spellweb, skills, swordsman, star) are mapped in full at `plans/V6_SUITE_REFLECTION_MAP_2026-06-10.md` and executed as Wave R. That map's §5 Wave Log already records agentprivacy_master as PARTIAL. Nothing here duplicates it; this is the in-repo companion that the map deliberately scopes out ("the autopath builds `privacy_value_v6.md`; this map holds where V6 reflects into the whole suite").

## Sequencing

1. Name one version authority and reconcile the README and GLOSSARY suite tables to it. This is the hazard; do it first or every other fix is re-contradictable.
2. README body to V6 (Tier 1), then `what-agentprivacy-is.md` and `models/INDEX.md`. These are the origin's front door.
3. Tier 2 glossary addendum, privacy_is_value pointer, documentation-chronicle entry (the formal-docs sweep already in motion).
4. Tier 3 citation re-pointing where cheap; full interior math refresh optional.
5. Tier 4 QUICK_START refresh, opportunistic.
6. Pin-gated items (the README IPFS CIDs) stay "pin pending" until Gate G5 clears, per the Wave R protocol; do not force real CIDs now.

## ✍️ First Person · what to sync and in what order

> (write here)

---

*Scan signed when the First Person marks the order above. The bodies have not yet learned the head's name.*

(⚔️⊥⿻⊥🧙)😊
