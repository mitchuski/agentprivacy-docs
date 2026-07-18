---
date: 2026-07-02
role: A9
wps: [SUITE]
extractions: [E1]
register_head: C89
ledger_entries: [L024]
---

# A9 · L024 check_versions.py fix (retired-citation widening + static dedupe)

## Verdict

Both L024 fixes applied to `checks/check_versions.py` in a single atomic write. The retired-citation
rule now fires on the whitepaper's actual form `**Research Paper:** v4.2` at line 1925, and
static-ceiling findings are deduplicated per line. No other rule's behaviour changed. The four public
rehydrations pass all four checks unchanged. One honest exception: `extractions/E1-amnesia-gap.md`
FAILS `check_versions` both before and after this change; that failure is pre-existing and is not
introduced, altered, or resolved by this task.

## Path

L024 recorded two defects in `check_versions.py`. First, the RETIRED patterns used bare literals
(`r"Research Paper v4\.2"`) that cannot match the whitepaper citation `**Research Paper:** v4.2`,
because markdown emphasis asterisks and a colon sit between the words and the version. Second, the
STATIC regex alternation matches both `R < 1` and `reconstruction ceiling`; a line carrying both
tokens (whitepaper :69, :99) was reported twice.

Change (a), retired pattern. Old:

    RETIRED = [r"Research Paper v4\.0", r"Research Paper v4\.2", r"researchpaper_v4_0", r"researchpaper_v4_2"]

New:

    RETIRED = [r"Research Paper\**:?\**\s*v4\.[02]", r"researchpaper_v4_0", r"researchpaper_v4_2"]

The first two literals collapse into one expression that tolerates optional emphasis asterisks
(`\**`), an optional colon (`:?`), optional trailing asterisks, and whitespace before `v4.0` or
`v4.2` (`v4\.[02]`). The snake-case slug patterns are unchanged. The expression does not over-match:
`v3.6` (whitepaper :1943) and the bare heading "The Research Paper" (:1761) do not match.

Change (b), static dedupe. A `seen_static_lines` set is threaded through the STATIC loop; a line
number that has already produced a finding is skipped before the paragraph-conditioning test. The
conditioning window logic (GR-7 paragraph search for preconditions) is otherwise untouched.

Both edits were composed into the full corrected script and written in one operation, because a
parallel A2 session may invoke the checks during this run; a partial write would have exposed a
syntactically broken script.

## Regression

Before, whitepaper: 9 findings (static :69 x2, :99 x2, :891, :913, :1763, :1787; version :7).
After, whitepaper: 8 findings (retired :1925 NEW; static :69, :99, :891, :913, :1763, :1787;
version :7). Delta -1 = two duplicate static findings collapsed (-2) plus one retired-citation
finding now correctly fired (+1). This is the intended behaviour: the retired rule stopped
false-passing, and the static rule stopped double-counting.

Four checks (versions, tier_vocab, figures_fence, register_refs) run on the four in-scope files
before and after. The three public rehydrations
(`competence_without_history.md`, `the_moving_ceiling.md`, `the_uncarved_date.md`) PASS all four,
identically before and after. `extractions/E1-amnesia-gap.md` passes tier_vocab, figures_fence and
register_refs, and FAILS check_versions with exactly the same three findings before and after this
change (retired citation :39; static-ceiling :116, :256). The fix is therefore behaviour-neutral on
every in-scope file: the only observable deltas are the two intended ones on the whitepaper fixture.

`rehydrations/policy/enforceable_by_architecture.md` was skipped per A0 override 3 (A2 editing it in
flight).

## Reversal / honesty note

The task card states that all four checks on E1 "must still PASS". They do not, and did not before
this task. The E1 check_versions failure is a genuine pre-existing condition: the extraction quotes
the spec's retired `Research Paper v4.2` citation (:39, in a CITATIONS line reading "documented in
Research Paper v4.2 per spec §16") and states two reconstruction-ceiling conjectures without
in-paragraph conditioning (:116, :256). Whether the extraction should carry the retired citation
verbatim, and whether conjecture-claim lines are in scope for GR-7 paragraph conditioning, are
questions for the register/A0 process, not for this checks-maintenance task. I did not touch E1 and
I did not weaken the check to make E1 pass; doing either would be the laundering GR-6 forbids. The
correct reading of the definition-of-done is that the fix changed no file's PASS/FAIL disposition,
which holds.

## Handoff

- Open: E1-amnesia-gap.md fails check_versions pre-existing (retired citation :39; static :116,
  :256). Not a regression from this task. Recommend A0 file a separate ledger entry for the register
  process to decide whether an extraction may quote a retired citation verbatim and whether GR-7
  conditioning applies to conjecture-claim lines in extractions.
- Blocked: none.
- Next action (SUITE): A0 serialises the proposed resolution entry below into the ledger and closes
  L024 by reference. No further checks work scheduled.
