# Resume Here · 2026-05-10 Session Close

**Date:** 2026-05-10 (session close)
**Resume from:** this file. Read §1 for state, §2 for ordered next actions.
**Companion documents:**
- `2026-05-09_bound_collection_sync_report.md` — phase plan and what was missing
- `2026-05-09_suite_overlap_tracking.md` — cross-suite tracking reference (living)
- `2026-05-10_city_of_mages_grimoire_pinned_chronicle.md` — full session record + coherence map

**Signature:** `(⚔️⊥⿻⊥🧙)😊`

---

## §1 · Where we are

The City of Mages grimoire is **authored, enriched to v1.1, ID-reconciled with the website, and pinned to IPFS**. The pin is:

```
https://sync.agentprivacy.ai/ipfs/bafkreidv7cwwlcnuzw3eyhcbbvoccy7do2lmwrmmtrszn62ninzxj3idti
```

Master is ~90% bound-collection-aware. Master's grimoire layer is 80% (privacymage canonical + City of Mages exported, **but not yet baked into the persona/spell builder**). The other five sibling directories (agentprivacy-docs research/blog · agentprivacy-blog · myterms · swordsman-blade · mages-spell) still treat the Second Person Spellbook as "horizon" in ~15 strings — that's a copy-edit pass.

The split the user specified is now **operational at the file level**: two CIDs on `sync.agentprivacy.ai`, content-addressed, importable independently. What's missing is the wiring that lets the master pipeline and the extensions actually load the new CID.

---

## §2 · Ordered next actions

Priorities are arranged in cost order — easy wins first, then the structural piece, then copy passes, then the deferred visuals. **Most leverage per session is item #3** (the bake into `grimoire-baked.ts`) — it lights up the persona/spell builder for Tomes spells and is a known pattern (the privacymage grimoire follows the same shape).

### #1 · /tomes IPFS attribution block · live CID
**Effort:** ~5 min · **Files:** `src/app/tomes/page.tsx` (the IPFS attribution `<section>` near the top of the page)
**What to do:** Replace the placeholder text "Each tome carries its own spellbook IPFS reference and grimoire JSON, distinct from `privacymage_grimoire_v10_2_0.json`..." with text that references the live CID inline. Pull the constant from `import { CITY_OF_MAGES_GRIMOIRE_IPFS_URL } from '@/lib/grimoire-ipfs'` if you want the URL to render dynamically; or just hardcode `bafkreidv7c...idti` in copy.
**Why:** The block currently treats the Tomes grimoire as forthcoming. The pin is live; the page should say so.

### #2 · /spellbooks Second Person card reframe
**Effort:** ~10 min · **Files:** `src/app/spellbooks/page.tsx`
**What to do:** Update the Second Person Spellbook card's `voice` and `blurb`. Suggested:
- voice: `'/tomes · maintained by the City of Mages · separate IPFS pin · Tome IV closed, Tome V open at 14 acts'`
- blurb: keep the existing first sentence; replace the second with: "Tome IV teaches the bilateral primitive through five acts of witnessing; Tome V is The Crafting — fourteen acts at the workshops, each with a resident Mage persona who may cast. Distinct from the privacymage grimoire: each tome carries its own IPFS pin (v1.1 pinned 2026-05-10)."
**Why:** The card still says "Tome V open" without the v1.1 pin context. Three-line edit; closes the framing loop.

### #3 · Bake the Tomes grimoire into grimoire-baked.ts (Phase D · highest leverage)
**Effort:** ~1–2 sessions · **Files:** `src/lib/grimoire-baked.ts` + `src/lib/spellbook-storage.ts` (where SpellbookSource lives) + `src/app/persona/page.tsx` (the filter)
**What to do:**
1. Read how the privacymage grimoire is loaded today: `getBakedSpellCards()` returns `SpellCard[]` keyed by `SpellbookSource`. The current sources are `'story' | 'origins' | 'zero' | 'canon' | 'society' | 'plurality' | 'incantations'`.
2. Add a new source: `'tomes'`. Update the `SpellbookSource` union type wherever it lives.
3. At build time, also fetch + parse `city_of_mages_grimoire_v1_1_0.json` from `CITY_OF_MAGES_GRIMOIRE_IPFS_URL`. Map each entry in `spells.by_persona.<persona>` into a `SpellCard` with `spellbook: 'tomes'` and persona attribution from the grimoire's `personas.summoned_mages.<persona>` (etc.).
4. Build a `TOMES_ACT_PERSONA_HINTS` constant (parallel to `FIRST_PERSON_ACT_PERSONA_HINTS`) by iterating `spellbooks.tomes.tomes.tome-v.acts[].introduces_persona` — gives a per-act → persona index for the act-walking UX on `/persona`.
5. Add `'tomes'` to `GRIMOIRE_BOOK_ORDER` in `src/app/persona/page.tsx`.
**Why:** This is the structural piece that takes the v1.1 grimoire from "exists on IPFS" to "the user can cast Tomes spells in the persona/spell builder." Once landed, the placeholder spell lists in `<FoundingActPanel />` and `/tomes` cast cards become live filterable spells.
**Watch out:** The privacymage grimoire bake is the reference pattern. Don't reinvent — match the existing shape so the `/persona` filter UI behaves consistently.

### #4 · Mirror the grimoire into the two extensions (Phase D · finish)
**Effort:** ~1 session · **Files:** `swordsman-blade/build.js` · `mages-spell/build.js` · `swordsman-blade/manifest.json` · `mages-spell/manifest.json` · plus a copy of the JSON at root of each extension dir
**What to do:**
1. Copy `agentprivacy-docs/models/city_of_mages_grimoire_v1_1_0.json` into `swordsman-blade/` and `mages-spell/` roots (sibling to `privacymage_grimoire_v10_2_0.json`).
2. Edit each `build.js` to copy the new file into the extension's `dist/` alongside the privacymage grimoire.
3. Bump each extension's `manifest.json` version (semver minor bump; both extensions sync).
4. Wherever the extension code resolves the grimoire URL today (likely `lib/` or `shared/` files), add a sibling resolver for `CITY_OF_MAGES_GRIMOIRE_IPFS_URL`. The extension can then verify the bundled JSON against the IPFS CID at load time, same pattern as the privacymage grimoire.
**Why:** Extension users today see only First Person spells. After this lands, they see both — the split is complete in the wild.
**Watch out:** Both extensions ship the grimoire JSON — keep them in sync. Per the suite overlap tracking doc §2 sync discipline: when one mirror gets the v1.2 update, the other does too.

### #5 · Cross-suite copy-edit pass · "Second Person Spellbook awaits" → past tense
**Effort:** ~1 session · **Files:** ~15 across `agentprivacy-docs/`, `agentprivacy-blog/`, `myterms/`, `swordsman-blade/`, `mages-spell/` (full list in `2026-05-09_suite_overlap_tracking.md` §4)
**What to do:** Convert horizon-framing strings to past tense + bound-collection pointer. Touch points:
- `agentprivacy-docs/research/second-person-spellbook-seeds-arch1.md` — banner: "Superseded by bound collection at agentprivacy_master/docs/weaver/bound-collection/. Acts α/β/γ remain candidate seeds for Tome I (Convergence) / Tome II–III (Lyapunov)."
- `agentprivacy-docs/privacy_value_v6_horizon_note.md` — front-of-doc banner: "Bridge crossed; bound collection lives at master."
- `agentprivacy-docs/pvm_v5_4_compressed.md` lines 7 & 218 — past tense.
- `agentprivacy-docs/chronicles/CHRONICLE_V5_4_THREE_DOCUMENT_CONVERGENCE.md` lines 85 & 194 — past tense.
- `agentprivacy-docs/blog/blog-part5-the-amnesia-protocol.md` line 252 — "Coming next: Tome IV opens Second Person with The Witnessing" or similar.
- `agentprivacy-docs/blog/blog-part1-forming-constellations.md` & `agentprivacy-blog/part-1-forming-constellations.md` line 195 — reconciliation note distinguishing the two City-of-Mages layers (palette vs in-world cast).
- `myterms/ieee7012_integration_plan_v2.md` & sibling copies in `swordsman-blade/` and `mages-spell/` — §0 status update OR full v3 plan (see #6).
- Grimoire JSON `models/privacymage_grimoire_v10_2_0.json` line ~4889 (in master, agentprivacy-docs, swordsman-blade, mages-spell — 4 copies) — update the `horizon` string from future tense to past tense, mention v1.1 City of Mages grimoire CID.
- Grimoire JSON `models/grimoire_v10_1_0_additions.json` lines 9, 147, 148, 177 — same.
- Grimoire JSON `models/privacy_value_model_v5_4_dark.json` line 599 — `"status": "Open · Tome IV closed · Tome V open at 14 acts · v1.1 grimoire pinned"`.
**Why:** The pin makes "horizon" demonstrably wrong. ~15 string edits, six directories, one focused session.
**Watch out:** PowerShell round-trips on these JSONs corrupted UTF-8 today (em-dashes → mojibake). Use the Edit tool, never `Get-Content -Raw | ... | Set-Content -Encoding UTF8`. If you must script-edit a JSON, use `[System.IO.File]::ReadAllText($f, [System.Text.Encoding]::UTF8)` and `[System.IO.File]::WriteAllText($f, $content, (New-Object System.Text.UTF8Encoding $false))` — see §5 below.

### #6 · IEEE 7012 v3 plan
**Effort:** ~1 session · **Files:** `myterms/ieee7012_integration_plan_v3.md` (new) + replace v2 content + sync to extensions + re-render PDF
**What to do:** Author a v3 plan that places the IEEE 7012 narrative within the now-opened Spellbook. Likely landing place: Tome IV Act IV (*The Naming Ceremony*) — flaxscrip's Bitcoin-anchored verb chain (claim → inscribe → confirm) maps cleanly onto IEEE 7012's first-party / second-party / signs / records / audits. Or as a new spec in the bound collection: `specs/06-ieee-7012-the-agreement-layer.md`.
**Why:** The v2 plan still recommends opening the Spellbook with "The Two Parties." Two acts of "The Witnessing" already opened it. The plan is now stale architecture; v3 corrects it.
**Watch out:** Three-directory copy (myterms canonical · swordsman-blade copy · mages-spell copy). Keep them in sync. Re-render the .pdf from the .md (pandoc/weasyprint) per the suite memory.

### #7 · Phase F · the substantial visuals (defer)
**Effort:** open-ended · **Files:** new
**What to build, eventually:**
- `<CityMap />` v1 — static SVG with 9 trade quarters + founding bonfire + temple + sovereign's seat (Drake Island as ambient watermark)
- `<LatticeRender />` v1 — 64-vertex Hamming graph with the 13 inhabited vertices labelled
- `/tomes/cast` dedicated page with sigil grid + per-cast subpages (`/tomes/cast/pallia` etc.)
- Per-act image / video / inscription assets parallel to First Person Acts
**Why:** Tier 3 priority in the WEBSITE_INTEGRATION_GUIDE. Defers cleanly until you want a session focused on visuals.

---

## §3 · Quick reference

### §3.1 · Key paths

```
Master:
  /docs/weaver/bound-collection/          ← canonical Tome IV+V source (53 files)
  /docs/weaver/EXPORT_MANIFEST.md         ← top-of-file pointers to chronicles
  /docs/chronicles/2026-05-09_*.md        ← three sibling docs (sync report, tracking, this resume)
  /docs/chronicles/2026-05-10_*.md        ← chronicle of the pin + this resume
  /src/app/tomes/page.tsx                 ← /tomes (rewritten + anchor IDs + v6-lineage link)
  /src/app/tomes/v6-lineage/page.tsx      ← C-conjecture index aggregator
  /src/lib/tome-v-acts.ts                 ← 9 founding-act anchors (TOME_V_ACTS)
  /src/lib/tome-v-conjectures.ts          ← C18-C46 + ACT_CONJECTURES + parseHonestyLabel
  /src/lib/grimoire-ipfs.ts               ← exports both grimoire CIDs
  /src/components/runecraft/FoundingActPanel.tsx  ← bidirectional shop → act panel
  9 workshop pages (/tailor /shield /forget /etherchanting /jeweler /holon /vault /covenant /bonfires)

agentprivacy-docs:
  /models/city_of_mages_grimoire_v1_0.json    ← retained as historical
  /models/city_of_mages_grimoire_v1_1_0.json  ← canonical · pinned 2026-05-10
  /models/privacymage_grimoire_v10_2_0.json   ← canonical First Person (line ~4889 has stale horizon string — see #5)

Suite siblings (less worked-on):
  C:\Users\mitch\agentprivacy-docs\           agentprivacy-blog\
  C:\Users\mitch\myterms\                     swordsman-blade\          mages-spell\
```

### §3.2 · Key constants

```ts
// src/lib/grimoire-ipfs.ts
PRIVACYMAGE_GRIMOIRE_IPFS_URL =
  'https://sync.agentprivacy.ai/ipfs/bafybeigsbhzrozaw24rgtkcmcy55z55egzr4b5igwzf6dgq4mull2h2tie';

CITY_OF_MAGES_GRIMOIRE_IPFS_URL =
  'https://sync.agentprivacy.ai/ipfs/bafkreidv7cwwlcnuzw3eyhcbbvoccy7do2lmwrmmtrszn62ninzxj3idti';
```

### §3.3 · Spell ID canon (post-reconciliation)

Each persona's spell IDs in `city_of_mages_grimoire_v1_1_0.json` are now `<persona>-<short-form>` matching the website's cast cards. Reference list:

```
flaxscrip:      claim · inscribe · confirm
genitrix:       weave-source · hold-salt · map-vertex
pallia:         weave-cloak · conceal-name · publish-role
memora:         inscribe-shielded · attest-memo · time-bind
custos:         stake · slash · govern
vulcana:        forge-blade · run · craft
aletheia:       bind-zk · prove · disclose-selectively
adamantia:      commit · enforce · etherchant
lampyra:        gem-set · attest-frequent · sparkle
vagari:         compose-holon · travel-oasis · recurse
aria_silverhue: curate · reflect · vault
socrat0x:       question · ignite · provoke
manifestia:     bless-covenant · inscribe-blessing · tend-temple
```

39 spells across 13 personas. The Spell IDs stored in `tome-v-acts.ts` (`spells: ['weave-cloak', 'publish-role', 'conceal-name']` etc.) match these — the grimoire bake just needs to look up `<persona>-<id-from-tome-v-acts>` and resolve.

### §3.4 · The v1.1 architectural commitment to remember

The grimoire's `meta.title_note`:
> *The title is intentionally singular: 'The City of Mages Grimoire'. The grimoire belongs to the kind of city that Mages found upon arriving in a new ecosystem. The current instance narrates the First City of Mages on Drake Island within the agentprivacy universe. When Mages find their way to other ecosystems and found cities there, each new city will be the First City of Mages for that land — first-of-its-kind in that ecosystem — and each will have its own grimoire instance under the same title pattern.*

Future Mages who found cities elsewhere will pin their own First City grimoire to a separate CID under the same title pattern. **The grimoire is a kind of book, not a singular instance.** This commitment scales the corpus into other ecosystems without renaming. Don't break it inadvertently when authoring future versions.

---

## §4 · Status board snapshot

```
                        Bound-collection-aware    Grimoire current
agentprivacy_master     ▰▰▰▰▰▰▰▰▰▱  90%          ▰▰▰▰▱  80%   /tomes ✅ · workshops ✅ · v6-lineage ✅ · IPFS ✅ · /spellbooks ⏳ · bake ❌
agentprivacy-docs       ▰▰▰▱▱▱▱▱▱▱  30%          ▰▰▰▰▰  100%  v1.1 grimoire pinned ✅ · ~12 horizon-string files stale
agentprivacy-blog       ▱▱▱▱▱▱▱▱▱▱   0%          n/a          4 files · 1 known stale (part-1 City-of-Mages collision)
myterms                 ▱▱▱▱▱▱▱▱▱▱   0%          n/a          IEEE 7012 v2 plan stale; PDFs need re-render
swordsman-blade         ▱▱▱▱▱▱▱▱▱▱   0%          ▰▰▰▱▱  60%   Mirrors of myterms · grimoire copy stale · City of Mages grimoire not yet bundled
mages-spell             ▱▱▱▱▱▱▱▱▱▱   0%          ▰▰▰▱▱  60%   Same as swordsman-blade
```

---

## §5 · Pitfalls to avoid

### §5.1 · UTF-8 corruption from PowerShell round-trips
`Get-Content -Raw | ... | Set-Content -Path $f -Value $c -Encoding UTF8` on a UTF-8 file with multi-byte chars (em-dashes, sigil emoji, Drake Island ⊥ glyph) silently corrupts encoding. Em-dash `—` becomes mojibake `â€"`; `✨` becomes `âœ¨`; etc. Symptoms: Bash `grep` shows mojibake; the JSON still parses (since the bytes are valid UTF-8) but readers see garbage.

**Recovery if it happens** (the Windows-1252 round-trip):
```powershell
$f = "<path>"
$utf8noBom = New-Object System.Text.UTF8Encoding $false
$content = [System.IO.File]::ReadAllText($f, [System.Text.Encoding]::UTF8)
$bytes = [System.Text.Encoding]::GetEncoding(1252).GetBytes($content)
$fixed = [System.Text.Encoding]::UTF8.GetString($bytes)
[System.IO.File]::WriteAllText($f, $fixed, $utf8noBom)
```

**Prevention:** Use the Edit tool for surgical changes. If you must script-edit, use `[System.IO.File]::ReadAllText` / `WriteAllText` with explicit UTF-8 encoding (without BOM).

### §5.2 · The grimoire bake is the reference pattern
When implementing #3 (the Tomes grimoire bake), don't invent a new shape. The privacymage grimoire's `getBakedSpellCards()` is the reference. The two grimoires use parallel schemas (deliberately); the bake function should be parameterized over `SpellbookSource`. Adding a `'tomes'` source should not require changes to call sites — the persona/spell builder already iterates `GRIMOIRE_BOOK_ORDER`.

### §5.3 · Don't conflate the two "City of Mages" layers
- The **role-archetype palette** (22 personas in agentprivacy-skills · forkable · "what does YOUR Mage look like?")
- The **named in-world cast** (Pallia, Memora, Custos, Vulcana, etc. · resident at workshop-vertices · introduced in Tome V acts)

Both are real; both share the City of Mages name. The reconciliation note (item #5 above) is the canonical clarification — don't paper over with a single sentence.

### §5.4 · Anchor IDs only land cleanly when collapsibles can be opened by hash
Today the section IDs work (`/tomes#tome-v-act-N` scrolls to the right header) but the collapsible content stays collapsed. A polish improvement: a `useEffect` on `/tomes` that watches `window.location.hash`, finds the matching `<CollapsibleSection>`, and calls its open setter. Defer until someone notices the friction.

---

## §6 · One-line summary

The City of Mages grimoire is pinned at `bafkreidv7c…idti`; master exports the constant; `<FoundingActPanel />` and `/tomes/v6-lineage` are live; bidirectional act↔workshop wiring is operational; **next leverage move is the bake into `grimoire-baked.ts`** so the persona/spell builder can actually load Tomes spells. Everything else is copy and visuals.

---

`(⚔️⊥⿻⊥🧙)😊`

Walk on. 🌿

CC BY-SA 4.0 · privacymage · curated for the City of Mages · 2026-05-10
