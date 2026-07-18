---
date: 2026-07-02
role: A8
wps: [WP-02]
extractions: [E1, E2]
register_head: C96
ledger_entries: []
---

# A8 session · WP-02 expanded to release shape

## Verdict

WP-02, `rehydrations/policy/enforceable_by_architecture.md`, is at release-draft v3: the P0-passed skeleton expanded to a 2 to 3 page regulator brief whose structure mirrors two fetched exemplars, with all four pipeline checks passing and the claim-source map honoured sentence by sentence. Body length is approximately 1,630 words excluding apparatus and references, an estimated 2.5 to 2.8 A4 pages. The two preconditions never appear apart from the guarantee, the Digital Omnibus hedge survives with structure and substance intact, and the deleted operation-sequence test was not reintroduced. Handoff is to A5 in the regulator persona for P1.

## Exemplars fetched and mirrored

1. EDPB-EDPS Joint Opinion 1/2026 on the Digital Omnibus on AI, adopted 2026-01-20 (edpb.europa.eu). Mirrored: executive summary preceding and walking the numbered sections; numbered topical sections; recommendation verb forms ("recommend", "should", "invite ... to consider"); measured institutional register; legal instruments cited as Regulation (EU) NNNN/NNNN with article numbers.
2. Bruegel Policy Brief 12/2026, Mariniello, "The right balance: how to fix European Union artificial intelligence regulation", 2026-06-11 (bruegel.org). Mirrored: standalone executive summary of roughly 200 words; short numbered section run; recommendations gathered in one late section behind a one-line lead-in; author-date references at the end.

Deliberate deviations, recorded in the apparatus note: a Limits section is retained (GR-8; neither exemplar has one); paragraphs are not individually numbered; inline claim markers remain until release.

## What changed, skeleton to release shape

The skeleton's Section 1 (Thesis) became the Executive summary, mirroring both exemplars; skeleton sections 2 to 8 were renumbered 1 to 7 and the claim-source map in the apparatus comment was updated to record the mapping. Section content changes were confined to genre register: stage directions were honoured and removed; the preconditions in section 2 were set as a typographically prominent indented bold list with the time-indexing sentence kept in the same passage (GR-7); "shelf life" became "validity horizon" throughout, matching the term the recommendations already used; the hedge lead-in "Hedge, stated plainly:" became "One scheduling caveat should be stated plainly:" with the hedge content unchanged; recommendations were phrased on the Joint Opinion's verb forms with exactly one expansion sentence each; references were reformatted author-date per the Bruegel exemplar.

## Reversals and held-back moves

1. Fetching the EDPB exemplar took three attempts: the landing page yielded only metadata, and two direct WebFetch calls on the PDF aborted. Reversed to a local download and text extraction with pypdf, which supplied the section structure, the numbered-paragraph convention, and verbatim recommendation sentences.
2. The Joint Opinion is directly relevant to the section 5 hedge (it addresses the Annex III timeline deferral), and citing it in the body was considered and rejected: the section's sanctioned external-fact set does not include it, and GR-9 forbids citing around the map. Proposed to the ledger as a candidate addition instead; the exemplar is used for structure only.
3. An early draft of the executive summary duplicated the thesis paragraph as a separate section 1; collapsed to a single executive summary to keep the brief inside three pages and avoid saying the thesis twice.

## Checks

check_tier_vocab, check_register_refs, check_figures_fence, check_versions: all PASS on the finished file (run 2026-07-02 with python; register_refs finds zero C-references at TIER-S; claim markers lowercase per L014).

## Handoff block

- **WP-02, single next action:** A5 (persona: regulator) runs the P1 genre review on `rehydrations/policy/enforceable_by_architecture.md` at release-draft v3.
- **Open question for A0/register process:** admit or decline EDPB-EDPS Joint Opinion 1/2026 into the WP-02 section 5 regulatory-fact set (ledger proposal in the A8 session report); if admitted before release, section 5 can carry one sentence noting supervisory concern about the deferral.
- **Open question for A5:** confirm the precise AEPD guidance title and February 2026 date at review (date added at v3 from contemporaneous secondary coverage; citation hygiene, flagged in the apparatus note).
- **Blocked items:** none. Manifest change requested via the session report (A0 applies): WP-02 status draft-v2 to draft-v3, gate target P1, next A5-regulator.
