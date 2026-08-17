# 2026-08-12 · Ceremony as Trust Task — the Verification Registry Goes Live

**Status:** session record (family-B root chronicle, non-pipeline). Companion records:
agentprivacy_master `docs/chronicles/2026-08-11_the-registry-opens.md` +
`2026-08-12_both-faces-on-the-table.md` (framework voice), spellweb `chronicles/DREAM-2026-08-12.md`
(KG voice), cityofmages `chronicles/DREAM-2026-08-12.md` (City ledger). Nothing in this corpus was
edited; this chronicle and its INDEX row are the only additions, uncommitted.

## What happened (2026-08-11 → 08-12, DTG ZKP TF lane)

1. **X10 — ceremony-as-trust-task** (`~/dtgwg-cred-spec-main_mage/explorations/X10-...md`): the
   answer to "can agent runtimes be entropy for trusted setup?" is a boundary rule — **agents
   orchestrate entropy; they are never the entropy** (an agent's context window is a §19 logged
   observer; a secret transiting it is compromised by construction). Three lanes: L1 verification
   registry (live), L2 universal BN254 phase-1 (proposed), L3 per-circuit phase-2 structurally gated
   behind the §25 construction-selection gate (`phase2-gate-closed` throw + property test).

2. **Verification registry LIVE** at https://mitchuski.github.io/dtgwg-zkp-mage/ — public,
   digest-checked records of independent circuit rebuilds (three Groth16/BN254 circuits: nullifier
   membership 11,523 constraints · dual issuer 10,717 · guardian threshold 16,078). Lab total:
   **18 suites / 178 properties, all green** (new 18th suite `ceremony-orchestrator`, 8/8).

3. **Empirical refutation before publication**: the lab's "byte-identical artifacts" claim was
   falsified by its own acceptance machinery — compiled circuits (r1cs/wasm) reproduce byte-exactly;
   the setup chain (ptau/zkeys/vkey) is machine-local (snarkjs mixes CSPRNG into every contribution).
   Acceptance model shipped corrected: circuit digests required, setup chain advisory, the
   volunteer's own green suites carry the proving-system claim.

4. **The pseudonymous seat**: `seat-7f` (admission-gated, name withheld) holds two registry rows —
   twelve advisory divergences (cold clone) and zero (pinned build) — with a disclosure note that
   both ran on maintainer hardware as demonstration. Admission and identity separable, enacted on
   the public artifact. Open question surfaced: the informative platform fields (CPU/OS) are a
   correlator for pseudonymous seats — X4's observable-event minimisation applied to the registry's
   own records.

5. **Cross-TF convergence**: RAHP's pressure test of the Core Credentials draft
   (trustoverip/dtgwg-rahp-tf#8) asks the lab's governing question in prose — *what can be built
   that is cryptographically valid but still unsafe?* Its finding 5 (ZKP constructions lack defined
   inputs/statements/verification algorithms) is addressed to the ZKP TF; the lab is the
   answer-shape. Item-map: finding 3 ↔ X6 erosion clocks; 6/9 ↔ A7 + PR-DEL; 7 ↔ A6 narrow
   nullifier; 2 ↔ VWC + transcript binding.

## Disposition

Public pushes (`7681990` → `450f8e9`, registry + entries 0000–0005) were made in the lab's own lane
by explicit ask. Upstream posts (Show & Tell + Discussion #10 comment, staged in the research root,
git-excluded) are Mitch's to make under the position protocol. This corpus: chronicle + INDEX row
only, uncommitted, canon untouched.
