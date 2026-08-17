# The Field Guide trust overlay — research fold

**What this is.** The durable research artifacts of the Field Guide × trust-graph work,
folded into the corpus 2026-08-17 from the working directory `~/field_guide_privacymage`
(built 2026-08-13 → 16 on the field machine; the working directory remains the build source
for the `fieldguide.localhost` wiki lane and the Pi-served copies — this folder is the
canonical, versioned home of the research substance).

**The occasion.** Max's ARWorld handoff (2026-08-15): the Hitchhikers Field Guide, a walking
AR client on OASIS, needed real one-hop trust to replace a hard-coded peer fixture. The
answer was the ToIP DTG lab's trust-graph-formation predicate (runtime 07), pointed at a
street — plus exactly four gates the physical world adds, and two findings that ran the
other way (the lab's personhood-gated formation runtime had never exercised the cred-spec's
conformant *pairwise* construction; a colleague's unrun acceptance checklist caught a leak
the leak test missed).

## Contents

| File | What it is |
|---|---|
| `COUNTER-SPEC-meet-and-overlay.md` | The reply to the handoff — the Meet rite, the disclosure model, the overlay rules — built as evidence, not argued as prose |
| `REFLECTION-MAP.md` | The ARWorld ↔ DTG-lab correspondence, row by row — **executed, not maintained**: `runtimes/reflection/test.mjs` fails if an anchor dies |
| `QUESTION-MAP.md` | All twenty questions in the ARWorld pack, each anchored to a property that runs |
| `NOTE-oasis-cred-spec-alignment.md` | The pairwise-construction correction, worked against the vendored cred-spec |
| `NOTE-zk-path-for-arworld.md` | What a ZK layer for the overlay would and would not buy |
| `runtimes/` | The evidence: eight suites, **124 properties** — run `cd runtimes && node verify.mjs` |

## Running the suites

Node + Python standard libraries only. The lab bridge needs the DTG lab checkout:

```
cd runtimes
DTG_LAB=~/dtgwg-cred-spec-main_mage node verify.mjs      # → ALL GREEN, 8 suites / 124 properties
```

Verified 2026-08-17 on the home machine (Windows, node v22): all green, with
`fixtures/vectors.json` sha256 byte-identical to the field machine's macOS run — the pack's
own determinism claim (`Rounding Is Not A Detail`) demonstrated across platforms. The
Windows portability patch (fileURLToPath / pathToFileURL, python3→python fallback) changed
path resolution only; suite content is untouched.

## What is deliberately NOT here

- **The ARWorld pack** (Max's handoff + discovery + trust-weighted-POI docs) — another
  author's working papers; they stay in the working directory and are served, attributed,
  from the team wiki (`fieldguide.localhost` → *The ARWorld Pack*, and the embassy-Pi
  copies). This corpus carries only the reply.
- **The wiki space itself** (22 pages + assets lane) — projection, not source; it lives in
  the farm (`~/.wiki/fieldguide.localhost/`) per the wiki-sync registry.
- **X11** — the lab-side filing of this work lives where it belongs:
  `~/dtgwg-cred-spec-main_mage/explorations/X11-field-guide-deployment.md`.

## Companions across the corpus

- Master chronicle: `agentprivacy_master/docs/chronicles/2026-08-17_field_guide_convergence.md`
- Family-B chronicle + release manifest: `../../chronicles/` (2026-08-17, both)
- Tome IX Act 10 (*The Predicate in the Street*, proposed): `cityofmages/tomes/tome-ix-the-horizon/`
- Spellweb: the Field Guide weave (`gateway-field-guide` + six ruling concepts)
