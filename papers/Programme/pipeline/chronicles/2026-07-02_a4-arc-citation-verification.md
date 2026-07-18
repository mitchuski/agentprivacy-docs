---
date: 2026-07-02
role: A4
wps: [WP-01, WP-28]
extractions: [E2]
register_head: C96
ledger_entries: []
---

# A4 citation verification of the gathering-arc essays (WP-01, WP-28)

## Verdict

Both essays pass citation verification. Every external citation and checkable world-claim in `rehydrations/public/the_moving_ceiling.md` (draft v3) and `rehydrations/public/competence_without_history.md` (draft v2) resolves against primary sources on the live web. Zero citation-metadata edits were required; zero unresolved citations remain. Both standing liveness questions close affirmatively: guide.agentprivacy.ai is live (HTTP 200, serving "The Guide" federation index), and agentprivacy.ai/model/atlas publicly serves the leakage-fold instrument exactly as WP-28 describes it (draggable per-hop leakage, chain depth N on the x-axis, (2^N - 1)e against Ne, conf ~55%, edge C7 -> C83 -> C17, register head C96). Three ledger entries are proposed to A0 (not appended, per session override); none blocks publication. `check_tier_vocab.py` and `check_register_refs.py` pass on both artifacts.

## Path

The session booted per `GROUND_RULES.md`, the A4 role card, both task cards, and `CLAUDE.md`, then read the two essays and enumerated every external citation and checkable world-claim: six reader-facing URLs shared across the essays, the Substack back-reference, the Orchard incident claims, the withheld-quantum-result claims, the Mosca inequality attribution, the multi-agent leakage literature claims, and the Ward Cunningham attribution.

First reversal, recorded with prominence. The initial verification round used the sandboxed web-fetch tool, which returned HTTP 403 for every target except the Substack, including eprint.iacr.org, a site that is certainly public. The early reading that the agentprivacy.ai family might be down was wrong; the 403s were bot filtering of the fetch tool, not site state. All liveness verification was redone with direct HTTP requests carrying a browser user agent, which returned 200 for all six URLs, and content verification proceeded by inspection of the returned HTML rather than trusting any status code alone.

The Orchard claims verified against the Zcash Foundation post (zfnd.org, Zebra emergency soft fork and NU6.2 activation) plus corroborating coverage: bug present since Orchard's May 2022 launch, found 2026-05-29 by Taylor Hornby via an AI-assisted audit using a frontier model released the previous day, soft fork 2026-06-02, NU6.2 2026-06-03, public disclosure 2026-06-04. "Four years" and "within a day" both hold.

The withheld-result claims verified against three primaries: Babbush et al. (arXiv 2603.28846, whitepaper dated 2026-04-17, circuits withheld behind a zero-knowledge proof), Schrottenloher's reconstruction (eprint 2026/1128, received 2026-06-01, approved 2026-06-04, also arXiv 2606.02235), and Gidney's same-day post acknowledging roughly a year of withholding. The interval from existence claim to reconstruction is about six and a half weeks; the essay's "about two months" is a fair essay-register statement, not a contradiction. One factual note for the canon: eprint 2026/1128 is single-authored (Andre Schrottenloher); pipeline surfaces that say "Schrottenloher et al." are wrong, though neither essay names authors, so no edit arose.

Second reversal. The working hypothesis for WP-28's "(2^N - 1)e" claim was that the essay might be attributing the canon's own structural claim to the literature, since the atlas itself calls the exponent "the structural claim (edge C7 -> C83 -> C17)". That hypothesis was wrong: the bound exists verbatim in the literature as Theorem 4.1 of arXiv 2603.05520 (Information-Theoretic Privacy Control for Sequential Multi-Agent LLM Systems), whose cumulative leakage bound reduces to (2^N - 1)e in the uniform case. A residual nuance survives: the bound is proven, and amplification is empirically evidenced, but the label "the exponential side is measured in the literature" slightly overstates its epistemic status; this is proposed to A0 rather than edited, since honesty labels are out of A4 scope. The companion claim about the "big measurement study" verified against AgentLeak (arXiv 2602.11510): inter-agent messages leak at 68.8% against 27.2% for final outputs, with output-only audits missing 41.7% of violations.

The atlas verification went beyond status codes: the served HTML contains the moving-ceiling instrument (draggable frontier growth rate g, shelf life t*, conf ~65%, registered Run 1, 2026-06-10, caption "evidence of mechanism, not of rate" verbatim) and the fold instrument (per-hop leakage slider 0.01 to 0.2, chain depth N axis, policy-only (2^N - 1)e against amnesia Ne, conf ~55%, registered Run 2, 2026-06-10). Both match their essay descriptions including the percentages, which the essays state as register-derived and the public surface confirms.

One tension found and not resolved, per GR-10: the live guide.agentprivacy.ai self-describes as "the static snapshot; the living wiki runs locally for workshops & governance", while WP-28's fourth door says "the register gets worked there in public". The site is live and forkable, so the citation resolves; the working-in-public claim is ahead of the deployed surface. Proposed as a CANON-LEVEL ledger entry for the register process.

The Mosca inequality attribution verified against eprint 2015/1075 (Michele Mosca). The Ward Cunningham federated-wiki lineage verified against the public record. The Substack back-reference verified live (published 2026-06-12, correct title and author). agentprivacy.ai/spells and 42.agentprivacy.ai both verified live with on-topic content. The first-person lines flagged in L025/L026 were not touched.

No git operations were performed, no ledger appends were made, and the manifest was not written, per session overrides. Verification notes are on file under `## Verification note` in `tasks/WP-01_A4.md` and `tasks/WP-28_A4.md`.

## Handoff

- **Open questions:** whether A0/A7 amend WP-28's "measured in the literature" phrasing to reflect bound-plus-evidence; whether the guide.agentprivacy.ai working-in-public tension is accepted as a known deployment gap or reworded upstream; whether any canon surface using "Schrottenloher et al." for eprint 2026/1128 needs correction.
- **Blocked items:** none. Nothing found blocks publication of either essay.
- **WP-01 next action:** A0 marks gate P2 (verification note on file, checks pass).
- **WP-28 next action:** A0 marks gate P2 (verification note on file, checks pass) and adjudicates the two proposed WP-28 ledger entries.
