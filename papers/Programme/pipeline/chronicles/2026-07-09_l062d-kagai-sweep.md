---
date: 2026-07-09
role: A3 (with A10-grade source reading, one seat, per the L062(d) card)
wps: [WP-04]
extractions: [E2]
register_head: C96
ledger_entries: []   # entry proposed to A0 in the seat report, not appended (per card)
---

# L062(d) referee-grade sweep: Kagai et al. 2025 read and ENGAGED; the four process-narration passages rewritten; SoK at draft-v4

**Verdict first.** Kagai, Branch, But and Allen 2025 ("Harvest-Now, Decrypt-Later: A Temporal Cybersecurity Risk in the Quantum Transition", Telecom 6(4):100, doi:10.3390/telecom6040100) was read referee-grade at its primary record and is ENGAGED in `rehydrations/academic/moving_ceiling_sok.md`, as an instance of the archival regime inside the existing HNDL family (section 5.1), not as an eighth family. The A10 sweep row's characterisation is confirmed in every checked particular: the paper is a genuine lifetime-versus-horizon formalisation whose load-bearing quantities are declared or projected inputs, with no ratio against source entropy, no derived shelf life, and no adversary-class ordering. The four process-narration passages (sections 2, 5.1, 8, References closing note) now read as ordinary related-work prose. N1, N3 and N7 stand as worded. This closes L088 MAJOR-4 and the Kagai leg of L062(d); the SoK is at draft-v4, awaiting the A0 targeted re-check per L088(b).

## The read (route and evidence)

Route, documented per the card: `doi.org/10.3390/telecom6040100` redirects to `mdpi.com/2673-4001/6/4/100`, which returns 403 to non-browser fetchers, including with a browser user agent; the browser extension seat was unavailable this session. Crossref (`api.crossref.org/works/10.3390/telecom6040100`) supplied verified metadata: authors Francis Kagai, Philip Branch, Jason But (Swinburne, Electrical/Robotics/Biomedical Engineering), Rebecca Allen (Swinburne, Physics and Astronomy); published 2025-12-18. Semantic Scholar's record pointed to the versioned MDPI PDF (also 403), but the publisher's asset host serves the full PDF without the bot wall: `mdpi-res.com/d_attachment/telecom/telecom-06-00100/article_deploy/telecom-06-00100.pdf` (23 pages, CC BY). Full text extracted and read.

The card's three questions, answered on the text:

(a) **Time-indexed guarantee formalisation?** Partially, and of a different kind. The paper formalises a time-indexed compromise probability, its Eq. (2): "R(t) = Pr{Ha(t) >= Ld}", "where Ha(t) represents the adversary's decryption capability at time t, and Ld denotes the required confidentiality lifetime". Adversary capability is hardware-parameterised: Eq. (4) gives "Tbreak(n, t) = alpha n^3 log2(n) ECC(t)/Q(t)" with Q(t) the logical qubits available at t. Nothing is derived from a disclosing architecture: Ld comes from "regulatory requirements, industry standards, and operational practices" (section 4.3) and the horizon is adopted from forecasts ("The adversarial horizon Ha(tmig) = 19 years is selected as a conservative baseline based on current quantum resource estimates"). Note the symbol collision: their R(t) is a probability, the SoK's R(t) a capacity-to-entropy ratio. A referee reading both papers hits this immediately; the SoK now discloses it in section 5.1.

(b) **Lifetime-versus-horizon distinction?** Yes, explicitly and centrally. Eq. (1): "Compromise occurs if Ld > Ha", with "Ld denotes the required confidentiality lifetime of protected data ... while Ha represents the adversary's decryption horizon". Sectoral exposure is the arithmetic residue, Eq. (6): "W = max(0, Ld − Ha(tmig))". This is the comparison form (Mosca's form): both quantities are inputs, neither is computed from channel capacities. It confirms exactly what section 8 of the SoK had conditionally priced: a lifetime-versus-horizon formalisation with declared inputs narrows nothing that N1 claims.

(c) **Systematisable content for the trichotomy?** Yes, as an instance, not a family. The model is the archival regime: fixed harvested ciphertext, adversary capability growing (their contribution 1 claims "the first formal model of the harvest-now, decrypt-later (HNDL) adversary", specified by collection capability, deferred decryption power and temporal horizon). The adversary is indexed by a single scalar horizon under optimistic/median/pessimistic scenario curves (FS-ISAC-style), not by an ordered family of decoder classes; monotone capability growth is assumed in the curves, never stated as a hypothesis or derived. So the work slots into section 5.1 beside Blanco-Romero et al. and sharpens the family's boundary against Definition 2 and the section 4 programme.

**Engagement decision: ENGAGE.** Grounds in one line: the paper is the closest published formalisation to Definition 2's purpose and instantiates the family the SoK's section 5.1 surveys, so the unification claim requires it inside the systematisation, and its declared-inputs structure is precisely the contrast that carries N1.

## Changes executed (four sites plus apparatus; revision 1's eleven sites untouched)

1. **Section 2 (corpus paragraph).** Before: two-work resolution history ("has since been resolved ... not yet engaged here"). After: forty-one resolved works stated as method, Kagai named as engaged in 5.1, the single unresolved preprint excluded and flagged. No process narration.
2. **Section 5.1 (second paragraph).** Before: "resolved but not yet engaged, engagement reserved for the pre-submission literature pass". After: a full engagement paragraph placing Kagai against Definition 2 (their Eq. (1)/(2)/(6) content in prose, the R(t) symbol collision disclosed, the declared-versus-derived contrast stated, no-class-ordering stated), tagged [N1 residue][N3 residue]; the unresolved preprint kept as the one open referee risk.
3. **Section 8 (external validity).** Before: two works as conditional referee risks ("if either work proves on engagement ..."). After: Kagai stated as read and positioned (lifetime-versus-horizon formalisation, quantum-transition-specific, declared/projected inputs; N1 stands; contribution 4's cross-domain claim unreached); the unresolved preprint remains the open risk with the conditional now attached to it alone.
4. **References closing note.** The Kagai entry moved into the reference list proper (alphabetical, existing key kagai2025harvest, zero bib changes); the "resolved since the sweep, not yet cited or engaged" note deleted; the unresolved-preprint note retained.
5. **Apparatus.** Frontmatter to draft-v4 with role line updated; an L062(d) sweep block appended to the A3 handoff comment. `reviews/WP-04_prior_art.md`: a dated annotation added beneath A10's N7 row (row itself unedited) recording the verdict, the confirmed particulars, and the ancillary finding below.

**No claim strengthened, in either direction.** The engagement paragraph asserts about Kagai only what the text shows (each particular quote-backed above); the paper's formalisation claim is reported as its own ("presents itself as the first formal model"); nothing was added to diminish it, and the SoK's own claims were not widened by the read (N7's wording was already quantum-transition-fenced by A10).

## Reversals and dead ends

1. **Fetch route.** WebFetch on the DOI and article page failed (403), curl with browser UA failed (403), the versioned PDF URL from Semantic Scholar failed (403), the browser extension was disconnected. The working route was the publisher's asset host (mdpi-res.com), found on the fourth attempt. Recorded so the next MDPI fetch starts there.
2. **Section 2 recount.** A first drafting kept "forty works ... during the sweep" plus a separate Kagai history sentence; rejected as still process narration. The count restated as forty-one resolved works, which absorbs Kagai without a story.
3. **Considered and declined: an eighth family.** The paper's temporal-risk framing does not organise multiple literatures and adds no regime outside the trichotomy; a new section-5 family would have inflated the work to justify the engagement (the exact failure mode the card fences).

## Checks (non-vacuous, explicit file list per L082)

Run on `rehydrations/academic/moving_ceiling_sok.md` and `reviews/WP-04_prior_art.md`: register_refs PASS x2, tier_vocab PASS x2, figures_fence PASS x2, check_versions PASS on the SoK and FAIL on WP-04_prior_art.md:62. The FAIL is a pre-existing checker false positive, verified present on the file with this session's annotation removed: the STATIC pattern `R\s*(?:_max)?\s*<\s*1` matches the substring "r <1450" inside A10's Babbush row text "(or <1450 / <70M)", a logical-qubit count, not a ceiling statement. Not fixed here (the row is A10's and the checker is out of card scope); recorded for the ledger and for the L082(c) hardening list (a word boundary `\bR\b` on the pattern kills this class). The SoK, the artifact this card edits, is exit 0 x4.

## Ancillary finding (reported, no action taken)

The remaining UNVERIFIED item's reported content (the ResearchGate preprint "reported to formalise the vulnerability condition Ld > Ha") is precisely the condition Kagai et al. publish as Eq. (1). The unread-neighbour class of referee risk is therefore now confined to one unresolved preprint whose reported contribution is already read and positioned in a published venue. No claim is made that the two works are related; the observation only reprices the residual risk.

## Handoff

- **WP-04, single next action:** A0 targeted re-check per L088(b) over the four MAJOR sites, five MINOR sites, and these four passages; clean = P1 evidence (L080 precedent). The draft accommodates no further Kagai action.
- **Open question for A0:** the A3 handoff comment's STILL OPEN list retains the everlasting-privacy/long-term-confidentiality families leg of L062(d) as unstruck; if the A5 review and the L085 A4 pass are ruled to have discharged it, strike it at the re-check, otherwise it needs its own seat before P1.
- **Blocked/none.** No canon touch, no manifest touch, no ledger append, zero new citation keys, no commits.
- **Proposed ledger entry** (text in the seat report to A0): L062(d) Kagai leg + L088 MAJOR-4 closure, with the check_versions false-positive finding and the mdpi-res.com fetch route recorded.
