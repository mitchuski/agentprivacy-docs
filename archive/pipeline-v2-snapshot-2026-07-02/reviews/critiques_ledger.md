# Critiques Ledger · append-only · any role may append · format per templates/ledger_entry_format.md

[L001][SUITE][CANON-LEVEL][2026-07-02][A4-equivalent]
FINDING: spec §25 states "ZEC fell roughly 27 to 33% in 24 hours"; public record shows ZEC rose post-fork (≈$544 on 06-02 → ≈$624 peak 06-04) then fell ≈50% over 06-04/05, confounded by a prominent institutional exit.
EVIDENCE: BitMEX Research timeline 2026-06; contemporaneous coverage (WP-00 search record).
PROPOSED: register-process correction to spec §25; suite-wide prohibition on the canon figure (encoded at E2-C06).
STATUS: open

[L002][SUITE][CANON-LEVEL][2026-07-02][A4-equivalent]
FINDING: spec §25's Schrottenloher account omits three public-record enrichments that strengthen C81/C82: (a) Gidney held the core technique ~1 year under publication restriction; (b) ecdsa.fail reused the published ZK verifier as its scoring filter; (c) the open challenge subsequently exceeded the withheld benchmark. Also: Orchard non-exploitation is cryptographically unprovable, a stronger detail than the canon carries.
EVIDENCE: eprint 2026/1128; Gidney post 2026-06; ecdsa.fail leaderboard; Zcash Foundation post.
PROPOSED: enrichment of spec §25 via register process; already usable downstream via Verified-record claims E2-C05/C07.
STATUS: open

[L003][SUITE][P3][2026-07-02][A9-equivalent]
FINDING: whitepaper version hygiene: header 6.3 vs document-metadata 6.2; header date April 7 with June 10 edition note; metadata cites Research Paper v4.2, retired by research-paper V6 §1.
EVIDENCE: swordsman_mage_whitepaper_v6_3.md front matter and Document Metadata section.
PROPOSED: single reconciliation pass against PAPERS_INDEX; blocks WP-03.
STATUS: open

[L004][WP-01][P0][2026-07-02][A7-equivalent]
FINDING: essay draft v1/v2 retold Orchard and Schrottenloher stories already published in "The Last Premine" (2026-06-12), violating the overlap check.
EVIDENCE: sync.soulbis.com/p/privacy-is-value-the-last-premine.
PROPOSED: rewritten as sequel (draft v3): one-paragraph recap linking to the branch; new territory only. A7 overlap check now names compared posts explicitly (role card updated).
STATUS: resolved(2026-07-02, session, draft v3 + WP-25 v2 reframed to defer messengers to the Horizon chronicle)

[L005][SUITE][P3][2026-07-02][A9-equivalent]
FINDING: register head moved C89 -> C93 (C92 Tarski axis-reading, Run 8 2026-06-28, per agentprivacy.ai/model/atlas live surface); pipeline manifest, check_register_refs HEAD, and WP-01 frontmatter carried the stale head.
EVIDENCE: atlas page footer "Conjecture authority lives in the register at head C93"; C81 instrument note citing C92.
PROPOSED: bumped manifest register_head, check HEAD constant, WP-01 frontmatter to C93 (done this entry). Standing A9 sweep item confirmed necessary. E2 extraction retains register_head_at_build: C89 as an accurate historical record; A1 to verify no C90-C93 content affects E2 claims on next sweep.
STATUS: resolved(2026-07-02, session, synchronised to C93)
