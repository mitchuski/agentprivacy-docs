---
date: 2026-07-10
role: A8
wps: [WP-09]
extractions: [E1 (consumed read-only via the draft's trace map; no extraction opened for edit)]
register_head: C96
ledger_entries: [] # one entry PROPOSED and returned to A0 with the handoff; ledger out of scope for this card
---

# WP-09 BGIN discussion paper · venue-grounding expansion to draft-v2 · A8 session

## Verdict

The WP-09 discussion paper stands at draft-v2. Every venue mechanic the A2 draft stated generically is now either grounded in a fact verified live on 2026-07-10 or deliberately left generic with the reason recorded in the apparatus. The proposal is routed by name to BGIN's IAM, Key Management and Privacy (IKP) Working Group; section 4 now has the shape a block session can adopt (scope, deliverables with document classes, the eight open questions as the study agenda, a proposed first session at Block #15); section 5 opens with two verified in-genre BGIN exemplars and grounds the IEEE, ToIP and DIF paragraphs in their primary pages. The claim spine, the eight open questions and the four deliverables are unchanged (L111: reframe only); the GR-7-complete guarantee passage in section 2 is byte-identical to v1; all lowercase claim markers are untouched. Checks: tier_vocab, register_refs, figures_fence, versions all PASS on the explicit path, first run after the edits.

## Path

1. Boot per CLAUDE.md: GROUND_RULES.md, the A8 role card, the WP-09 A8 task card, the target draft in full, the WP-02 record for the house pattern (the exemplar-enriched end state at rehydrations/policy/enforceable_by_architecture.md; the cycle-two chronicle). Read the four check scripts before editing so additions could not trip them (the register_refs C-number pattern and the versions version-field pattern shaped two wording choices: no bare C-plus-digits tokens, no line-initial "Version:" fields).

2. Verification pass before any writing, all fetched 2026-07-10:
   - Block #15: 2026-10-15/16, Washington D.C., verified at bgin-global.org (home announcement) and bgin-global.org/events. Agrees with L061.
   - IKP name and remit: bgin-global.org/activities/working-groups styles the group "IAM, Key Management and Privacy (IKP) Working Group" (active); remit wording captured for the paper. The task card's gloss "Identity, Key Management and Privacy" is not the site's current form; the site's form is used throughout. Recorded as a finding, not silently normalised.
   - Document class: study report with BGIN SR numbering, verified at the Wallet Governance, Policy and Key Management Study Report forum page ("BGIN SR 00**", working draft, IKP WG). No published BGIN taxonomy naming a "discussion paper" class was verifiable; that term remains this paper's self-description of genre only.
   - Exemplars: the wallet-governance study report (above) and "Study Report: Zero-Knowledge Proofs (ZKPs) - Technology and Applications", the latter listed as published in the IKP category at bgin.discourse.group/c/working-group-s/ikp-wg/8. The same listing verifies current IKP activity directly adjacent to this proposal: a proof-of-personhood draft report with a dual-agent-systems discussion thread, crypto-agility and PQC-migration and privacy-enhanced-authentication draft reports, and agentic-framework material. That continuity fact carried into section 3.
   - IEEE 7012: standards.ieee.org/ieee/7012/7192/ gives "IEEE Standard for Machine Readable Personal Privacy Terms", active, approved 2025-11-04, published 2026-01-20.
   - ToIP: trustoverip.github.io/tswg-tsp-specification gives "Trust Spanning Protocol (TSP) Specification", status "vs1.0 Experimental Implementor's Draft Rev 2", the spanning-layer protocol of the ToIP technology architecture.
   - DIF: identity.foundation lists the "Trusted AI Agents Working Group"; its page gives the scope wording and work items (Delegated Authority Report, Delegated Authority Threat Model, Governance of Delegated Authority Report, KYA-OS reference implementation).

3. Edits, in order: frontmatter bump (status draft-v2, role A2+A8, change_note, venue line re-verified); A8 addendum prepended inside the apparatus comment (verification record, kept-generic list, dead-ends, structural diff, release checklist untouched); Purpose routing sentence; section 3 venue-routing paragraph; section 4 reshape (document classes on the deliverables, study-agenda framing on the open questions, proposed-first-session paragraph); section 5 lead adjustment plus BGIN exemplar paragraph plus grounding of the three external paragraphs; references updated to match.

4. Checks run on the explicit path after all edits: 4/4 PASS.

## Dead ends and reversals

- bgin-global.org/news/ikp-webinar (an "IKP WG Hosts Agentic Framework Webinar" item surfaced by search) returned 404. Not cited; the agentic-framework and dual-agent-systems facts rest on the working-group category listing only.
- papers.ssrn.com abstract 4449592 (the IKP soulbound-tokens study report) returned 403. Not cited; the wallet-governance and ZKP reports serve as the exemplars instead.
- bgin-global.org/publications is a script-side loader and returned no document list to a plain fetch; the document library was reached through the group's Discourse forum instead, which is where the SR drafts in fact live.
- trustoverip.org/our-work/technical-stack/ returned 404; the TSP facts were taken from the published specification page directly.
- identity.foundation/working-groups/trusted-ai-agents.html (guessed URL) returned 404; the correct page is /working-groups/trusted-agents.html.
- Name variance finding: the venue's own two surfaces differ ("IAM, Key Management and Privacy" on the site registry; "IAM, Key Management & Privacy" on the forum), and both differ from the task card's gloss and from the canon whitepaper's older "Identity Key Access Management and Privacy". The artifact uses the site registry's form; the variance is recorded in the apparatus and here, not resolved (it is the venue's to resolve).

## Handoff

- **WP-09, single next action:** A0 P0 spot-trace on draft-v2 (per L111(b)), then the A5-regulator-class review completes the chain.
- **Open question for A0:** whether the deadlines.md row wording "discussion papers per WG process" should be softened to match the finding that no published BGIN document-class taxonomy names a discussion-paper class (the SR class is the verifiable one); registry file is A13/A0 territory, not touched.
- **Blocked/none:** nothing blocked; no extraction, manifest, ledger, tracker or canon surface was written.
- **Proposed ledger entry** returned to A0 in the session report (venue-grounding record, name-variance finding, dead-ends, check runs).
