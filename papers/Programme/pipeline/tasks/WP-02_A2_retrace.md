---
wp: WP-02
role: A2
tier: S
extraction: E1 (now built, 2026-07-02) + E2
branch: none (branch convention suspended; untracked tree)
gate_target: P0 (A0 runs it after this re-trace)
due: 2026-07
---

# Task card · WP-02 re-trace · role A2

**Objective:** Replace the six `[E1-trace-pending]` markers in the WP-02 skeleton with real traces to the built E1, so A0 can run P0.
**Inputs:** `rehydrations/policy/enforceable_by_architecture.md` (draft v1); `extractions/E1-amnesia-gap.md` (39 claims, head C96; its top note names the Proven-conditional core E1-C01 to E1-C05); GROUND_RULES.md (TIER-S constraints unchanged).
**Output:** the same file, markers resolved; the A8 handoff note's section-to-source map updated to cite E1 claim IDs (lowercase form per L014: E1-c01 etc.).
**Definition of done:**
- every `[E1-trace-pending]` marker replaced by an explicit claim ID trace or, if E1 carries no matching claim, the sentence is deleted per GR-9 (trace or delete, never defend);
- no claim strengthened in the rewrite; STATUS discipline of the cited E1 claims respected (Proven-conditional core only for load-bearing statements; conjecture-tied claims may not appear at TIER-S in any form);
- all four checks pass; ledger clean or filed; A0 notified.
**Out of scope:** new sections; new claims; touching E1; touching the manifest.
**Handoff:** A0 (P0 run: register check + three-claim spot-trace), then A8 per the original card.
