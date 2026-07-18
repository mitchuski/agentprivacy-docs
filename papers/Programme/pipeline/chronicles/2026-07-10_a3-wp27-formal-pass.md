---
date: 2026-07-10
role: A3
wps: [WP-27]
extractions: [E10]
register_head: C96
ledger_entries: []
---

# A3 formal pass · WP-27 methods paper · draft-v2

**Verdict.** `rehydrations/academic/conjecture_governance_method.md` is at draft-v2. The four [A3: formalise] stubs are discharged as Definitions 1 to 4 with numbered invariants I1 to I12, each formalising exactly the prose specification the draft already carried and nothing beyond it. A theorem-discipline sweep reworded three sentences to observational strength and touched nothing else. All four deterministic checks PASS on the explicit path. One ledger entry is proposed to A0, not filed.

## Stub dispositions

1. **Gate ladder (Section 3.2, stub 1).** Definition 2: labelled transition system over the seven artifact states with actor set Ag ∪ {h}. Invariant I5 states non-delegability as an absence: the relation contains exactly one transition into complete, labelled h, and no agent-labelled transition into complete or out of awaiting-completion; complete is unreachable in the agent-only subsystem. I6 states the same absence for publication and version-control writes. The block states explicitly that the record's two awaiting-completion artifacts are instance evidence of operation under the invariant, not proof that no violation is possible.

2. **Ledger (Section 3.3, stub 2).** Definition 3: entry tuples with a content projection core(e) = (index, FINDING, EVIDENCE, PROPOSED). I7 append-only core (prefix-stable, indices strictly increasing, never reused); I8 corrections are entries referencing their target index; I9 STATUS as the only mutable projection, licensed by and referencing a later append. The enforcement remark states exactly that enforcement is procedural (single serialising writer), not cryptographic: no hash chain, no Merkle proof, no external witness, a violation of I7 not detectable from the ledger alone. The Section 5 transparency-log contrast now cites the remark instead of the stub (the one L102-adjacent touch was this forced consistency edit in Section 5's append-only paragraph; the novelty fence wording itself was not touched).

3. **Production direction (Section 3.4, stub 3).** Definition 4: disjoint unit sets (formal, extraction, narrative, external) with cite and der relations. I10 derivation edges formal-to-narrative only, empty harvest valid; I11 formal citations factor through the extraction layer, never terminate at narrative units; I12 the sole narrative-to-formal channel is candidate adoption through the human-licensed minting event I4. The dated qualification is preserved as an explicit temporal index paragraph: the invariants are asserted from the mid-2026 operating documents onward, the earlier narrative-first flow violates I10 as stated, the change is reported as method evolution, and the ledgered tension is referenced, not smoothed.

4. **Register numbering (Section 3.1, stub 4). RULING: stands alone, not folded into stub 2.** Definition 1: the register as a time-indexed partial function ρ from numbers to claims plus an unnumbered candidate set. I1 single assignment (subsumes identifier immutability and no-reuse: over the whole history a number denotes at most one claim); I2 monotone minting at the next free number, numbers as identifiers not ranks; I3 alias retention under external citation; I4 human-licensed minting (no agent action extends dom(ρ)). **Reason for the ruling:** the ledger and register invariants formalise different objects. The ledger's appended entries are content-immutable (I7); the register's entries are not, since claim wording, confidence bands, and status are revised under the register process. What is immutable in the register is the denotation map, the number-to-claim binding, not file content. Folding into the ledger formalisation would therefore either assert a content immutability the register does not have (a strengthening, the exact failure mode this task forbids) or weaken I7 to accommodate register revisions. Additionally, I4 is an actor-licensing property akin to the ladder's I5, not an append property; the kinship is real (shared posture: append rather than rewrite; route the licensed act to the human) and is recorded in a remark in Section 3.1 rather than by unification.

## Second ruling (A2's open question)

The Section 4.2 earned-twice evidence table **stays prose**; no schematic convergence statement was added. A formal statement (the four rules as elements of an intersection of two independently generated rule sets) would add notation without content and would push what E10-C15 carries as reported observation ("convergence, not derivation") toward a formal independence claim the record does not support. Recorded in the handoff comment in the artifact.

## Theorem-discipline sweep

Whole draft read against the rule: a sentence reading as a formal claim must be a defined invariant, carry its [E10-Cnn] basis, or be reworded to observational strength. Three rewordings:

1. Section 1: "any governance method that assumes contemporaneous human comprehension ... fails silently at the first backlog" (universal prediction) reworded to "a governance method that assumed ... would have failed silently here at the first backlog" (grounded in this record).
2. Section 4.4 opening: "The strongest operating evidence the record offers is reflexive" reworded to "A further class of operating evidence is reflexive". The unattributed superlative collided with Section 4.2, where the record's own assessment (quoted, attributed) names the convergence the strongest evidence the template carries; the paper must not out-rank its source's ranking.
3. Section 6: "defects that occur are caught by a later instrument" (present-universal, contradicted by the very next sentence) reworded to "in the recorded window, the defects that occurred were caught by a later instrument", keeping the existing "cannot show that all defects are caught" sentence as the governing limit.

Also added: a Section 3 preamble fixing the evidence class of all twelve invariants (design invariants at process-record grade; enforcement class stated where weakest). Checked and left standing: the Section 7 hypothesis keeps hypothesis shape (grounds, falsification condition, no generality assertion); counting claims (two papers, three same-day loops, at least five interruptions, six gates) all carry markers; the Section 3.5 continuity property is carried verbatim from E10-C18 with its marker. No marker was added or removed; no claim was widened.

## Frontmatter and apparatus

Status bumped to draft-v2; role, gate_target, and handoff lines updated (handoff to A4, bibliography resolution). The A2 handoff comment's stub list is marked discharged with both rulings recorded; the trace map's four stub lines and closing GR-9 note are updated to the discharged state with a sweep note.

## Checks (exact invocations, from pipeline/checks/)

- `python check_versions.py <explicit path>` PASS, exit 0
- `python check_register_refs.py <explicit path>` PASS, exit 0
- `python check_tier_vocab.py <explicit path>` PASS, exit 0
- `python check_figures_fence.py <explicit path>` PASS, exit 0

Explicit path in each: `C:/Users/mitch/agentprivacy-docs/papers/Programme/pipeline/rehydrations/academic/conjecture_governance_method.md`.

## Reversals

None. No formalisation attempt was abandoned mid-pass; the stub-4 fold-in option was evaluated and ruled out before writing, for the reason above. One near-miss worth recording: an early draft of I2 specified minting as "successor of the historical maximum", which would have over-specified the record's own phrase "next free number"; it was written instead as "the least number never yet assigned", which is the record's rule and no more.

## Handoff

- **WP-27, next action:** A0 to file the proposed ledger entry (returned in the A3 final report) and route per cycle plan; A4 bibliography resolution is the named next station (Evans and Cooper edition pins owed before review, per the artifact's own limits section).
- **Open question for the review seat (A5/P1):** whether the twelve invariants should be exercised by the adversarial persona against the enforcement episodes cited in Sections 3.1 and 4.4 (do the recorded episodes instantiate the invariant they are cited under). A3 believes they do; an adversarial read is the right instrument to confirm.
- **Blocked:** nothing blocked by this pass. The numbered-problem-list ambush (A5/P1 risk list) remains open and is untouched by this pass.
