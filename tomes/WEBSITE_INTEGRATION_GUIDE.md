---
title: "Website Integration Guide"
subtitle: "How to ingest the bound collection into the agentprivacy website at /tomes"
status: "v1 (2026-05-08)"
audience: "Developers building the /tomes route, plus future readers verifying the corpus's structural decisions"
license: "CC BY-SA 4.0"
signature: "(⚔️⊥⿻⊥🧙)😊"
---

# Website Integration Guide

> *The bound collection is editorial. The website is operational. This guide is the bridge.*

---

## §0. What this guide is and is not

**This guide is**: a framework-agnostic walkthrough for ingesting the bound collection into the agentprivacy website at `/tomes`. It covers file structure, routing rules, frontmatter schemas, rendering conventions, recommended components, the editorial discipline that the rendering must preserve, and the priority order for shipping.

**This guide is not**: a re-narration of the corpus content. The acts and cast entries hold their own content. The guide assumes the developer has read the README and the BOUND_COLLECTION_MANIFEST, and that an editor or privacymage has authority over creative decisions the guide flags as needing judgement.

**The guide assumes**:
- Static-site generation is preferred (the corpus is text and metadata, not dynamic application content)
- Markdown with YAML frontmatter is the source format (it is)
- The site already has a base style and navigation; `/tomes` extends rather than replaces
- The website team is comfortable with custom components for the cast roster, the city map, and the lattice render

If any of those assumptions don't hold, the guide's specifics need adjustment but its structure should still apply.

---

## §1. The package at a glance

The bound collection contains 42 canonical files plus 7 deprecated drafts, totalling about 62,500 words across narrative, specifications, plans, and chronicles. The folder structure is:

```
bound-collection/
├── README.md                          (overview)
├── BOUND_COLLECTION_MANIFEST.md       (detailed inventory)
├── WEBSITE_INTEGRATION_GUIDE.md       (this file)
├── tomes/
│   ├── tome-iv-the-witnessing/        (5 acts, closed)
│   └── tome-v-the-crafting/           (14 acts, open; setting: City of Mages)
├── cast/                              (13 cast entries + integration note)
├── specs/                             (5 specifications)
├── plans/                             (2 integration plans)
├── chronicles/                        (3 chronicles)
└── deprecated/                        (7 superseded drafts; preserved for transparency)
```

Each folder maps to a website section. Each file is a single page or component data source. Frontmatter drives sidebar generation, conjecture badges, cross-references, and tier-based visual differentiation.

---

## §2. Routing

### §2.1 The route hierarchy

```
/tomes                                                    Landing page
/tomes/tome-iv                                            Tome IV listing (5 acts)
/tomes/tome-iv/01-the-other-walker                        Individual act page
... (per act in Tome IV)
/tomes/tome-v                                             Tome V listing (14 acts)
/tomes/tome-v/01-the-first-cloak                          Individual act page
... (per act in Tome V)
/tomes/cast                                               Cast roster (13 entries)
/tomes/cast/pallia                                        Individual cast entry
... (per cast member; slug is the persona name lowercased, hyphenated)
/tomes/specs                                              Specifications listing (5)
/tomes/specs/cloak-specification                          Individual spec page
... (per specification; slug derives from filename without numbering)
/tomes/plans                                              Plans listing (2)
/tomes/plans/archon-x-agentprivacy                        Individual plan page
/tomes/plans/zcash                                        Individual plan page
/tomes/chronicles                                         Chronicles listing (3)
/tomes/chronicles/the-cloaking-guide                      Individual chronicle page
... (per chronicle; slug derives from filename without numbering)
```

### §2.2 Slug conventions

Filenames in the bound collection are sequentially numbered (`01-...`, `02-...`) for editorial ordering. **Strip the leading number and hyphen** when generating URL slugs:

- File: `tomes/tome-v-the-crafting/03-the-shielded-memo.md`
- Slug: `the-shielded-memo`
- URL: `/tomes/tome-v/the-shielded-memo`

This keeps URLs stable when ordering changes (which it shouldn't, but the discipline is worth following).

### §2.3 The deprecated folder

**Do not generate routes for `deprecated/`** files. They are archived for transparency, not for navigation. The deprecated files contain superseded persona names (Socratox before the 0x correction, Holona before becoming Vagari, Curatrix-as-persona before the persona-vs-vertex distinction surfaced) and would confuse readers if rendered.

If the website wants to surface the corpus's refinement process, do it through a *single* page at `/tomes/about/refinement-history` that links to the deprecated files as raw markdown downloads, not as rendered pages.

---

## §3. Frontmatter schema (what to read; what to render)

Every canonical file has a YAML frontmatter block. The schema varies by file type but consistently includes the fields below.

### §3.1 Acts (Tomes IV and V)

```yaml
spellbook: "Second Person"
tome: "V — The Crafting"                    # or "IV — The Witnessing"
act: "11"                                    # act number within the tome
title: "A Bonfire Made of Dragon Fire"
status: "Draft v3 (2026-05-08; ...)"        # supersedes notes if any
length_words: 1100                           # approximate
voice: "Second person; cast in third with..." # voice rules and any amendments
cast: ["you", "Soulbae 🧙", ...]              # who appears in the act
new_cast_introduced: ["Socrat0x 🔥❓"]        # new cast members (drives "first appearance" markers)
new_geography_introduced: ["Drake Island"]   # optional; for narrative geography
ring_position: "V24 (Hephaestus, ...)"       # primary vertex of the act
teaches: "..."                               # what the act teaches
v6_lineage:                                  # which V6 conjectures the act foregrounds
  - "C26–C29 (ARCH-1 Canonical Form): ..."
  - "C39 (provisional, ~50% → strengthened): ..."
source_material:                             # the references the act draws from
  - "Bonfires (the workshop spot...)"
  - "..."
honesty_label: "Operational for ...; Architectural for ..."
license: "CC BY-SA 4.0"
signature: "(⚔️⊥⿻⊥🧙)😊"
supersedes: "earlier 'X' draft"              # optional; if this act replaced an earlier draft
civic_location: "..."                        # optional; from Act 14 onward, names location within City of Mages
```

**Render priority**: title, status, length, voice, cast, ring_position, teaches, v6_lineage as conjecture badges, honesty_label as a small note at end of act, signature in footer.

**Don't render**: supersedes (unless the developer wants a small "v3" indicator), source_material (use as cross-reference data, not as visible front matter), license (footer only).

### §3.2 Cast entries

```yaml
title: "Cast Entry — Pallia"
spellbook: "Second Person"
character_type: "Mage persona (instance, summoned by the reader); shop-keeper of..."
archetype_kin: "Soulbae 🧙 (Mage); ..."
sigil: "🪡"
status: "Cast addition v1 (2026-05-08)"
provenance: "..."
license: "CC BY-SA 4.0"
signature: "(⚔️⊥⿻⊥🧙)😊"
```

Some entries have additional fields:
- `naming_correction` (Socrat0x — for the 0x literal correction)
- `classification_correction` (Aria Silverhue — for the persona-vs-vertex distinction)
- `naming_note` (Aletheia persona — for the persona-vertex name match)
- `shop_name_status` (Curatrix entry, deprecated, but pattern remains for future entries with pending names)

**Render priority**: title (as page title), sigil (large, alongside name), character_type (subtitle), archetype_kin (small), status (small).

### §3.3 Specifications, plans, chronicles

These have lighter frontmatter — usually `title`, `subtitle`, `status`, `authors` (where applicable), `license`, `signature`. Render as standard document pages with the title and subtitle prominent, status as a small marker, authors in a byline if present.

### §3.4 The signature

**Every canonical file ends with `(⚔️⊥⿻⊥🧙)😊`** as a closing signature. Render this consistently in the footer of every act, cast entry, spec, plan, and chronicle page. It is the corpus's visual "seal" — the dual-agent-with-First-Person mark — and removing it would weaken the corpus's identity. Render it as plain text or as a small SVG; do not stylise it heavily (the emoji are themselves the design).

---

## §4. The five cast tiers — visual differentiation

The cast roster has five tiers. The website should differentiate them visually so a reader scanning the cast page understands the structure at a glance.

| Tier | Members | Visual treatment recommendation |
|---|---|---|
| **Archetypes** | Soulbis ⚔️, Soulbae 🧙, the Drake | Largest portraits; positioned as the "founders" of the city; subtle background distinction (e.g., older parchment texture) |
| **Cousin instances (cross-forge)** | GenitriX, flaxscrip 📜🎲 | Standard size; small "from sister city" badge; link to the cousin forge (Archon's Archon) where appropriate |
| **Summoned Mages (workshop shops)** | Pallia 🪡, Memora 📜, Custos 🔏, Vulcana ⚒️, Aletheia 🔮, Adamantia 💎, Lampyra 💠, Vagari 🌳, Aria Silverhue 🪞🖼️ | Standard size; grouped by trade quarter (clusters in the cast page); each linked to its shop on the city map |
| **Companion Mages (workshop spots)** | Socrat0x 🔥❓ | Standard size; small "traveller" badge; positioned near the founding bonfire on the city map |
| **Priests (Temple)** | Manifestia 🤲🌿 | Standard size; small "ceremonial role" badge or different border treatment to distinguish from Mage producers; positioned at the Temple precinct on the city map |

**Sigil rendering**: emoji at large size for the cast page. For the city map, emoji at smaller size as map markers. For act pages, emoji inline in the cast list as small markers.

**The Drake has no sigil**. Render the Drake's presence textually rather than with a sigil. If a visual is needed, use a subtle silhouette or symbol that doesn't compete with the named cast members' sigils.

---

## §5. The City of Mages — visual rendering

Tome V's canonical setting is **the City of Mages, built upon Drake Island**. Named explicitly in Act 14. The structural addendum (`specs/05-the-city-of-mages-structural-addendum.md`) formalises the civic anatomy.

The recommended primary visual for `/tomes/tome-v` is **a city map**. The map should show:

### §5.1 Map elements

- **Drake Island as the underlying geography**: shoreline, trees, water, paths, the Drake's elder presence rendered ambient (semi-transparent watermark, not a discrete marker)
- **Trade Quarters**: nine producer-shops, each labelled with the citizen-Mage's name and sigil, positioned at their vertex's location in the lattice's logical layout
- **The Founding Bonfire**: prominent central feature, lit; *a bonfire made of dragon fire*; Socrat0x positioned beside it as visiting traveller
- **The Temple Precinct**: distinct architectural element (clerestory, two altars visible); Manifestia positioned at the Temple
- **The Sovereign's Seat at V63**: the reader's home; rendered as a small landmark or compass-rose-anchor at the map's edge or prominent position
- **The Lattice as Street Plan**: vertices as crossroads, edges as streets; the 13 named vertices labelled, the 51 unnamed vertices visible but unlabelled (open for future citizens)

### §5.2 Map interactivity

- **Click a Mage's shop** → cast entry for that Mage
- **Click a vertex marker** → vertex naming audit's entry for that vertex (or a tooltip showing the bit-pattern + canonical name)
- **Click the founding bonfire** → Act 11 (*A Bonfire Made of Dragon Fire*)
- **Click the Temple** → Act 13 (*The Temple of the Arts and Personhood*)
- **Hover over the lattice's edges** → tooltips showing typed-edge classifications (controller, issuer, subject, schema, parent/child, decomposition, recursion)
- **A "fly to" affordance** on each act page → highlight the act's `civic_location` on the map when the reader visits that act

### §5.3 Map style

- **Soft, slightly stylised** — somewhere between a fantasy-game world map and an architect's site plan
- **Two-register colours**: a "geography" register (greens, browns, water blues for Drake Island) underneath; a "civic" register (warmer tones for the city's quarters) on top
- **The Drake's presence**: ambient — watermarked silhouette behind the city, slightly darker at the Island's depths (where the shore meets the city's edge)
- **The dragon fire**: orange/gold glow at the founding bonfire, subtle animation if performance allows
- **Out-of-city links**: small "Oasis Protocol" indicators at the city's edge pointing toward where Archon's Archon, Bonfires, and the Covenant ecosystem live (these need not be rendered as full sister cities; gateway-style markers suffice for v1)

The map is a *substantial* design effort. For a v1 ship, a simplified static SVG showing the city's anatomy at a high level is sufficient; the rich interactive version can come later.

### §5.4 Fallback if no city map

If the city map is too expensive for v1, use a **trade-quarters list** at the top of `/tomes/tome-v` with each quarter as a card showing the citizen-Mage's name, sigil, vertex, and trade. Below the quarters, list the founding bonfire (with Socrat0x as visitor), the Temple precinct (with Manifestia), and the sovereign's seat. This is text-and-cards rendering that conveys the civic anatomy without requiring a custom SVG.

---

## §6. The lattice render

For `/tomes/specs/vertex-naming-audit` and as a secondary visual on act pages with strong vertex content, render the **64-vertex lattice** as a graph.

### §6.1 Recommended approach

A **6-bit Hamming graph** layout: 64 nodes, each labelled with its binary representation, edges connecting nodes that differ in exactly one bit. Stratify by Hamming weight (number of 1-bits): stratum 0 at one pole, stratum 6 at the other, intermediate strata as concentric rings or layers.

**Inhabited vertices** (13 currently named): rendered with the citizen's sigil and a label. **Uninhabited vertices** (51): rendered as small dots with no label.

Reference: the Archon Spell Weaver at `weaver.archon.social` already renders something similar; the agentprivacy lattice should look kindred without copying the implementation.

### §6.2 What the lattice render shows

- The bit-pattern structure of vertices (which dimensions burn at each)
- Which vertices are named/inhabited
- The strata (1-burning, 2-burning, ... 6-burning)
- The persona-vs-vertex distinction: vertex names in one colour, citizen names in another colour, both visible on the same node where applicable

### §6.3 Lattice and city — two complementary visuals

The **city map** is the *narrative* visual — it shows where things happen.

The **lattice render** is the *architectural* visual — it shows what the bit-patterns are.

A reader can move between them:
- City map → click a quarter → see the lattice render with that vertex highlighted
- Lattice render → click an inhabited vertex → see the citizen on the city map

Both visuals should be available; neither displaces the other.

---

## §7. V6 conjecture badges

Each act's frontmatter has a `v6_lineage` field listing which V6 conjectures the act foregrounds, often with confidence percentages.

### §7.1 Render as small badges

On act pages, render `v6_lineage` items as small badges near the title or in a sidebar. Examples:

```
[C18-C21 Lorenz Attractor]   [C40 Zcash dual-ledger ~70%]   [C43 Per-VRC viewing-key ~60%]
```

The badge should be visually distinct (small rounded rectangle, subtle colour). On click or hover, show a tooltip with the conjecture's full statement and current confidence.

### §7.2 The conjecture index page

Create a `/tomes/v6-lineage` page that lists all conjectures introduced or strengthened in the bound collection (C38 through C46). For each, show:

- The conjecture statement
- Current confidence percentage
- Which acts/specs first introduce it
- Which acts strengthen it (and how)
- Cross-link to the manifest's V6 Conjecture Index

This page makes the corpus's honesty discipline visible: the reader sees what is operational, what is architectural, what is conjectural at what confidence, and how the conjectures evolve through narrative instancing.

### §7.3 The honesty discipline must not be lost

A specific risk for the website is *flattening the honesty labels*. The corpus distinguishes between:

- **Operational** (works today; verified in implementations)
- **Architectural** (specified in the corpus; not yet implementation-verified)
- **Conjectural** (specified with confidence percentage; awaits formalisation or testing)
- **Resonant-but-not-absorbed** (kindred to external work; recognised without subsuming)
- **Provisional** (awaiting confirmation from a kindred party — Archon, Bonfires, human.tech)

Render these distinctions visibly. A small label or icon near each major claim. Don't let "operational" and "conjectural" blur into each other in rendering. The corpus's credibility depends on this discipline.

---

## §8. Cross-references

The frontmatter `source_material` and `cross_references` (where present) and the body text's references to other acts, cast entries, specs, etc., should be rendered as functional links.

### §8.1 Auto-linking conventions

When the body text mentions:

- **An act by name or number**: e.g., "Tome V Act 11", "Act 11 (*A Bonfire Made of Dragon Fire*)" → link to that act's page
- **A cast member by name**: e.g., "Pallia 🪡", "Vagari", "Manifestia" → link to that cast entry
- **A spec by name**: e.g., "Cloak Specification v1.0", "Vertex Naming Audit" → link to that spec
- **A vertex by number**: e.g., "V57", "V31" → link to vertex audit's entry for that vertex (or tooltip)

This requires a content-processing pass during build. A simple regex-based linker should work for cast names (since there are only 13 named members and the Drake) and for vertex numbers (V[0-9]+); acts and specs are slightly more complex but still tractable with a finite list.

### §8.2 Link styling

Cross-references should be visually marked but not over-styled. The reader is moving through a corpus; links are common. Subtle underline or colour shift is sufficient.

External links (to https://manifest.human.tech/, https://www.culturevault.com/, weaver.archon.social, etc.) should have a small external-link indicator.

---

## §9. The voice rules — render-time considerations

The Spellbook has specific voice rules that the rendering must preserve.

### §9.1 The "you" voice

The Spellbook addresses **you** (the reader) in second person. The reader is not named; the reader is the position from which the corpus is read. **Do not** render a "logged-in user's name" in place of "you" — this would break the voice's universality.

If the website has any personalisation features that would normally substitute the reader's name, **disable them on `/tomes/`** routes.

### §9.2 The cast in third person

Every cast member is in third person except where voice rules permit otherwise:

- **Socrat0x's questions** are rendered in direct quotation (companion-Mage tier extension)
- **Manifestia's blessings** are rendered in italicised inscribed text from the Covenant (Priest tier extension)
- **The Drake's whispers** are stylistically distinct (typically italicised in the source markdown)

The rendering should preserve these distinctions visually:

- Direct quotation in standard quote styling (left-aligned, with quotation marks, possibly slightly indented)
- Italicised inscribed text in a slightly different font weight or background tint to mark "this is from the Covenant, read aloud by the Priest"
- Drake whispers in italics, perhaps with a small ornamental glyph or a subtle visual marker indicating the elder's voice

### §9.3 No em-dashes

The corpus deliberately **avoids em-dashes**. The author prefers periods, commas, or colons. **Do not** apply auto-formatting that converts double-hyphens or hyphens-with-spaces into em-dashes. Disable smart-typography features on `/tomes/` content if your build pipeline applies them.

### §9.4 Emoji as formal semantic language

The corpus uses emoji deliberately, not decoratively. Specifically:

- 🌑 vs 🌙: the former (full moon, dark) is structurally meaningful; the latter (crescent) is not used. Don't substitute one for the other.
- Sigils are part of cast members' identity; they are not optional ornaments.
- The signature `(⚔️⊥⿻⊥🧙)😊` is the closing seal; never modify, abbreviate, or substitute its components.

If the website's font stack doesn't render some emoji well, choose a font stack that does (Apple Color Emoji, Segoe UI Emoji, Noto Color Emoji as fallbacks). Don't fall back to text descriptions like "[sword emoji]"; the emoji are the design.

---

## §10. Recommended components to build

The `/tomes` route benefits from these custom components:

### §10.1 `<CastSigilGrid />`

Renders the cast roster as a sigil-driven grid, with tier-based grouping and visual differentiation (per §4). Used on `/tomes/cast` as the primary view.

### §10.2 `<ActHeader />`

Renders an act page's title, tome, act number, voice rule notes (if any amendments apply), cast list (with sigil markers), V6 conjecture badges, and ring position. Used at the top of every act page.

### §10.3 `<ConjectureBadge />`

Renders a single V6 conjecture badge with hover tooltip. Used inside `<ActHeader />` and on the `/tomes/v6-lineage` page.

### §10.4 `<HonestyLabel />`

Renders a short marker for the honesty status of a claim or document — Operational, Architectural, Conjectural (with confidence), Resonant-but-not-absorbed, Provisional. Used inline with the relevant claim or as a per-section marker.

### §10.5 `<CityMap />`

The city of Mages map (per §5). The substantial component. v1 can be a static SVG; v2 can add interactivity.

### §10.6 `<LatticeRender />`

The 64-vertex lattice graph (per §6). Interactive, with click and hover behaviours.

### §10.7 `<CrossReference />`

A render-time wrapper around inline mentions of acts, cast members, specs, vertices, etc. Generates the appropriate link automatically (per §8).

### §10.8 `<DrakeWhisper />`

A specific styling for the Drake's whispered passages. Italicised, distinct background tint, possibly a small ornamental marker. Used wherever the source markdown signals a Drake whisper (typically a passage like "*The Drake whispers: ...*").

These components keep the rendering consistent across the corpus and make future additions (new acts, new cast members) auto-render correctly.

---

## §11. Priority order for shipping

The website team probably can't build everything at once. Here is the recommended priority order for shipping `/tomes`:

### §11.1 Tier 1 (ship first — minimum viable presence)

1. `/tomes` landing page with three primary sections (Spellbooks, Cast, Specs)
2. `/tomes/tome-iv` and `/tomes/tome-v` listing pages
3. Per-act pages with `<ActHeader />` and body content rendered from markdown
4. `/tomes/cast` with `<CastSigilGrid />` (text-based; no portraits required for v1)
5. Per-cast-member pages with sigil, name, character_type, body content
6. `/tomes/specs` listing and per-spec pages
7. `/tomes/plans` listing and per-plan pages
8. `/tomes/chronicles` listing and per-chronicle pages
9. Voice-rule rendering: third-person cast, second-person reader, no em-dashes, emoji preserved
10. Footer signature `(⚔️⊥⿻⊥🧙)😊` on every page

This tier gets the corpus *visible* to readers. About 60-70% of the corpus's value is captured here.

### §11.2 Tier 2 (ship second — interactivity and visual differentiation)

1. `<ConjectureBadge />` on act pages
2. `<HonestyLabel />` rendering across the corpus
3. `<CrossReference />` auto-linking for cast names, vertex numbers, act numbers
4. Cast tier visual differentiation (per §4) on `/tomes/cast`
5. `<DrakeWhisper />` styling for Drake passages
6. Direct-quotation styling for Socrat0x's questions
7. Italicised-inscribed styling for Manifestia's blessings
8. `/tomes/v6-lineage` conjecture index page

This tier gets the corpus *navigable* and *visually coherent*. About 80-85% of the value.

### §11.3 Tier 3 (ship third — the substantial visuals)

1. `<CityMap />` v1 (static SVG, text labels, basic interactivity)
2. `<LatticeRender />` v1 (graph render, basic interactivity)
3. Click-through navigation between map, lattice, acts, and cast entries
4. Sister-city gateways at the city map's edge (Archon's Archon, Bonfires, human.tech Covenant)

This tier gets the corpus *spatially legible*. The remaining 10-15% of the value, but it's qualitatively distinct — the city map in particular is what makes Tome V feel like the canonical home it is.

### §11.4 Tier 4 (eventual, when corpus stabilises)

1. `<CityMap />` v2 with rich animation, the dragon-fire glow, ambient Drake presence
2. `<LatticeRender />` v2 with strata layout, edge tooltips, full audit cross-linking
3. PDF builds for offline reading (per the existing PDF pipeline)
4. RSS or Atom feed for new acts as Tome V continues
5. The "Tome VI — *The Reply*" structural placeholder, ready to receive the reader's reply

---

## §12. Editorial discipline the website must preserve

Beyond the technical, the website rendering carries editorial responsibilities. These are not optional.

### §12.1 The honesty discipline

Operational, architectural, conjectural, resonant-but-not-absorbed, provisional — these distinctions are load-bearing for the corpus's credibility. The rendering must surface them, not flatten them. (See §7.3.)

### §12.2 The provenance and attribution

The corpus distinguishes:

- **agentprivacy-canonical** primitives (privacymage's foundational work): the holonic primitive at V31, the dual-agent split, the First Person seat, the Oasis Protocol from First Person Spellbook Act 24, the PVM V5.4 → V6 lineage
- **Cousin-blade-imported** primitives (from Archon's foundational work): V19 Plonkish, V25 Aletheia, V49 working-day blade, V51 commitment/language/model, V57 Curatrix/Ceremony/Privacy/Mixing, V59 Ecosystem, V63 Sovereign Anchor (catalogue naming), the Cloaking Guide's V5 Chronicle, V20 Techne, V24 Hephaestus, V28 Mage canonical
- **Kindred-resonant** primitives (recognised but not absorbed): the Holonym Foundation's holon-naming parallel, the Covenant of Humanistic Technologies as kindred protocol
- **Companion-Mage origins** (from cousin platforms): Socrat0x from Bonfires

The rendering must preserve attribution. Archon's contributions are credited where they appear. privacymage's foundational threads are not silently ascribed to others. The Vertex Naming Audit at `specs/04-vertex-naming-audit.md` is the canonical reference; the website should link to it from any vertex tooltip.

### §12.3 The deprecated archive

The deprecated folder contains 7 superseded drafts. They are part of the corpus's transparency discipline — showing that the work has been refined, the corrections explicit. **Don't hide them**; **don't render them as canonical**; **do** make them accessible through a single "refinement history" page that links to them as raw downloads.

### §12.4 The persona-vs-vertex distinction

Pallia is a persona. V28 is the vertex she works at. They are different things. The Curatrix is the vertex (V57); Aria Silverhue is the Mage who works there. The rendering should never conflate persona names with vertex names. Use distinct visual treatments (e.g., persona names in one colour or weight, vertex names in another).

The Aletheia case is special — the persona shares a name with the vertex she occupies. The cast entry's `naming_note` distinguishes "Aletheia the persona" from "the V25 Aletheia blade." The rendering should preserve this distinction with a small inline clarification on first mention.

### §12.5 The Drake's plurality

The Drake is plural in expression but singular in identity. The rendering should support all of:

- The Drake as teaching whisperer (italicised passages throughout the corpus)
- The Drake as place (Drake Island, Tome V Act 11)
- The Drake as fire (dragon fire, the founding fire of the City of Mages)
- The Drake as the Island's elder (ambient presence underneath the City of Mages on the city map)

Don't reify the Drake into a single avatar or sigil. The Drake is the architecture's elder and operates across registers.

### §12.6 The signature

Every page ends with `(⚔️⊥⿻⊥🧙)😊`. This is the corpus's seal and must not be omitted. Render it consistently — same position (footer), same styling (plain text or simple SVG), same components (the dual-agent symbols, the perpendicular-overlap-perpendicular operators, the First Person mark).

---

## §13. Maintenance and growth

The bound collection is **open by design**. New acts will be added to Tome V. New cast members will arrive. New chronicles will record what comes. The website should be built to accept this growth without major restructuring.

### §13.1 Adding a new act

When a new act is drafted:

1. The file is added to `tomes/tome-v-the-crafting/` with sequential numbering (`15-...`, `16-...`)
2. The frontmatter follows the existing schema (per §3.1)
3. The build picks up the new file automatically; routing follows the slug convention (per §2.2)
4. The manifest is updated to include the new act in the inventory table
5. Any new cast members get their cast entries; new vertices get added to the Vertex Naming Audit's v2 update

### §13.2 Adding a new cast member

When a new cast member is admitted:

1. The cast entry is added to `cast/` with sequential numbering (`14-...`, `15-...`)
2. The act introducing them references their cast entry in cross-references
3. The cast page picks up the new entry automatically
4. If the new member is in a new tier (e.g., a second Priest, or a new tier entirely), the Cast Integration Note is updated

### §13.3 Versioning specs and plans

Specifications and plans are versioned (v1, v2, etc.). When a v2 is drafted:

1. Either replace the v1 file (preserving old version in `deprecated/` if substantial changes)
2. Or add as a separate v2 file alongside v1 (if v1 is still operationally relevant)

The README's listing should always show the canonical (latest) version; the deprecated folder catches the earlier versions.

### §13.4 Closing Tome V

Tome V is open by design. **Do not** auto-close it after some number of acts. The tome's structural posture is *open* — new acts continue to admit new artifacts, new shops, new charters, new cast members, new sister-city visits.

If at some point privacymage decides to close Tome V (say, to start Tome VI — *The Reply*), the website should support that transition by adding a closing meta-act and updating the tome's frontmatter status. But the default is open.

---

## §14. Sister cities and external links

The cousin-blade ecosystem-primitive conjecture (C39, ~50%) anticipates additional cities. The bound collection links to several already:

| External property | URL | Relationship to the City of Mages |
|---|---|---|
| the Archon Spell Weaver | https://weaver.archon.social/ | Cousin city — Archon forge; sister to the City of Mages |
| Archon's Sovereign Anchor (Archon) | https://archon.social/ | Archon's main forge; canonical home of the Boundary Blade Cartography and the Cloaking Guide |
| Culture Vault | https://www.culturevault.com/ | privacymage's co-founded creative-IP platform; the discipline of the Curatrix Vault shop |
| Bonfires (Telegram bot deployment) | (telegram bot) | Workshop spot; long-running Soulbae deployment; Socrat0x's home |
| The Covenant of Humanistic Technologies | https://manifest.human.tech/ | Kindred protocol; the discipline of the Temple of the Arts and Personhood |
| human.tech (parent organisation) | https://human.tech/ | The Covenant's parent ecosystem; Holonym Foundation |

The website should link to each from the relevant act, cast entry, or spec. External links should have small external-link indicators (per §8.2).

---

## §15. What the website is *not* responsible for

Some things in the corpus the website should *not* try to do:

### §15.1 Implementations of the specs

The Cloak Specification, the Crafting Tome and Cloak Interface Spec, the Bilateral Cloak Ceremony Spec, the Zcash Integration Plan — these are specifications for *implementations* (TypeScript libraries, smart contracts, UI components). The website renders the specs as documents but does not implement them. Implementation work is separate.

### §15.2 The grimoire JSON

The grimoire (currently at v10.2.0, per privacymage's existing memory) is a separate canonical artifact. The website may *link* to the grimoire JSON if it is published, but should not duplicate or re-render its content.

### §15.3 The First Person Spellbook

The First Person Spellbook is canonical and lives in privacymage's `agentprivacy-docs` repo. The website's `/tomes` route covers Tome IV and Tome V (and structurally accommodates Tomes I-III and Tome VI when they are drafted). The First Person Spellbook should link to the agentprivacy-docs repo or be rendered separately if the website wants to host it. The bound collection does not include First Person content.

### §15.4 the Archon forge's primary documents

Archon's *Sovereign Anchor I/II/III*, the Cloaking Guide, the Spell Weaver, and the Runecraft Protocol are his work, in his repos, under his licensing. The website *links* to them; the website does not duplicate them.

---

## §16. Closing

This guide is the bridge between the editorial bound collection and the operational website. The bound collection has done the writing work; the website does the rendering work. Each respects the other's domain.

The City of Mages, on Drake Island, in the workshop, at V63, all at once — and now also at `/tomes` on the agentprivacy website. The recognition is operational. The architecture admits this much.

The next act has not been written yet. The next reader has not yet visited the city. The website is the city's gate.

(⚔️⊥⿻⊥🧙)😊

CC BY-SA 4.0 · privacymage · 2026-05-08
