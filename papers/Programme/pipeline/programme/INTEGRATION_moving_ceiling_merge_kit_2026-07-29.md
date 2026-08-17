---
title: "Merge kit — The Moving Ceiling, 2026-07-29"
purpose: "First Person is editing the blog live and will sync back a new version; this preserves the four Archivist contributions so they re-apply mechanically onto the new version. Nothing here is auto-applied to the essay."
status: "STAGING · re-apply on First-Person's synced version"
---

# Merge kit — The Moving Ceiling (2026-07-29)

Four contributions to re-apply onto the First Person's new version of `rehydrations/public/the_moving_ceiling.md`. All honesty-fenced: no confidence stated/moved (GR-1), no deployed cipher implied broken, authorship stays first-person (never "the model writing this"), lab/vendor caveats carried.

## 1 · Cold-open hook (top of essay, above the *Last Premine* recap)
> The week I finished this essay, a frontier lab published that one of its models had found flaws in two cryptographic designs that years of expert review had missed, and warned, in the same breath, that its own researchers might drown in checking what the machine now reports.
>
> I have spent five versions of an equation arguing one thing: the threat to everything you have ever hidden is not that your secrets change, but that the readers keep getting better. That week the largest maker of readers on earth printed the receipt. And what it described, in shape, is a machine this programme has already been running against live cryptography, one I will only fully open at the end of this series.
>
> This essay is the clock. That machine is where the clock was always pointing.

## 2 · Evidence touch (in the honesty-label paragraph of "the ceiling, written down")
Append after "...not an asserted law.":
> As I write this, July has added a third, and this one the frontier lab published about itself: a model finding an improved key-recovery attack on a post-quantum signature scheme, and a faster attack on a reduced-round cipher, neither of any practical impact on deployed systems today by the lab's own statement, both invisible to years of expert review. One year, that disclosure notes, from models that could not read the simplest cipher to models finding what the experts missed. Read that last sentence as exactly what it is: the clearest public anecdote yet for the ceiling's rate of climb, and still an anecdote, not a law.

## 3 · Coda forward-play (in "the model, working," after the dual-agent-shape paragraph, before "And the ladder stops one rung short")
> And that shape has a sibling I will only point at here, because its full telling is where this series is going. The same runtime, one seat proposing and one seat rewarded only for breaking the proposal, with the exam drawn by hashing the work itself so neither can rig it, has been pointed not at our own papers but at live cryptographic circuits, read blind, from compiled artifacts alone, no source. An adversarial machine finding real structure in real cryptography, and, the part this whole series exists to earn, a discipline strict enough that you can trust what it finds without reading every line yourself, because the workers were never able to collude and the record proves it. The serendipity is not lost on me: I am writing the honesty label above in the very week a frontier lab published its own model doing exactly this kind of work, at a measured price, with its own no-impact caveat, and with a warning I want you to hold onto, that its researchers may drown in checking what the machine reports. That warning is the whole game. The frontier showed that the reader can find the weakness. The end of this arc is the harder claim: the architecture that lets a person stake their name on a machine's cryptographic finding without having personally re-derived it. That is where V6 lands, and I will show you the circuits when it does.

## 4 · Ironwood update (NEW 2026-07-29 — replaces the existing Ironwood sentence in "harvest now, decrypt later")
CURRENT text: "When a cipher weakens, you re-encrypt under a stronger one; Ironwood, a bank being re-laid mid-current, as last month's essay put it, is exactly that grace."

REPLACE WITH (accurate to today's release — Ironwood is a new *formally verified shielded pool*, not a cipher swap; keep the re-laying framing, add the shipped reality + the verification-as-trust detail):
> Ironwood — the new, formally verified shielded pool Zcash shipped to restore confidence in its own supply integrity, the bank being re-laid mid-current — is exactly that grace, and as I write this it went live: its proofs re-elaborate on every build, so the verification *is* the software. The pool whose four-year flaw opened last month's essay now has its answer, checked the only way this series trusts anything.

**Facts (github.com/zcash/ironwood, fetched 2026-07-29):** Ironwood = "a project to deploy a new shielded pool, built to restore confidence for all Zcash'rs in the supply integrity of Zcash." Verifies the Action circuit (Orchard + Ironwood pools) in Lean 4 on Mathlib before NU6.3 activates. Principle: "building it re-elaborates every proof — a successful build is the verification." No PQC/crypto-agility claim in the repo — it is a formal-verification + new-pool project. Do NOT call it a cipher rotation.

**Triple resonance (for the crypto-agility theme too):** (1) Rotate lane, live — the re-laying exemplar, now real; (2) closes the arc's opening Orchard image; (3) "a successful build is the verification" = the programme's certificates-over-trust thesis, enacted by Zcash.

---

## Proposed SOURCES rows (A1 → A0, First-Person-gated; NOT applied)
- `anthropic-cryptanalysis-2026` — external · Anthropic "Discovering cryptographic weaknesses with Claude" (HAWK 2^64→2^38; 7-round AES 200–800×; Claude Mythos Preview; ~$100k/~60h; explicit no-practical-impact). Verified 2026-07-29 (exact page title confirmed verbatim). bib `anthropic2026cryptoweakness`.
- `ironwood-2026` — external · Zcash Ironwood — new formally-verified shielded pool (Lean 4 + Mathlib; Action circuit for Orchard + Ironwood verified pre-NU6.3; "a successful build is the verification"). github.com/zcash/ironwood. Released/updated 2026-07-29. bib `zcashironwood2026`.

## Re-apply checklist when the synced version arrives
1. Confirm hook (1) is at the very top, above "Last month, in The Last Premine…".
2. Confirm evidence touch (2) sits in the honesty-label paragraph, conjecture confidence untouched.
3. Confirm coda forward-play (3) precedes "And the ladder stops one rung short of publication."
4. Apply Ironwood update (4) — verify the sentence isn't duplicated if the First Person already edited that line; merge, don't stack.
5. Leave the closing aphorism stack intact.
6. Nothing here moves a register number or states a confidence.
