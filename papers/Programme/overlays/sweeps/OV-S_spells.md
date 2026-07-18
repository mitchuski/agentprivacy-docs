---
date: 2026-07-11
dimension: spells-and-emoji-strings
run: overlay-run-1
coverage: >
  Swept (RS-05 clause): Programme/pipeline/GROUND_RULES.md read in full;
  all 5 papers/v6/*.md by symbol grep (⊥ ⚔ 🧙 ⿻ κ 🪢 😊 🙂, seal/sigil,
  R(t), R_max, H(X), I(X;·), Nε, t*, V(π,t)) with hit windows read;
  checks/check_tier_vocab.py read in full; chronicles/ swept by glyph grep
  (2026-07-10_the-twelve-cycles.md returned ZERO glyph hits; A7/A9 cycle
  chronicles read at hit windows); observers/*.md by grep with the 96/64
  and RS windows read; rehydrations/public/*.md by glyph grep, all seals
  sighted; reviews/OBSERVER_REGRESSION_SEEDS.md RS-07 read in window;
  reviews/critiques_ledger.md GREP-ONLY (⊥ seal sigil emoji κ glyph) with
  the two hit windows read. Hunted and NOT found in this corpus: T∫ tracer
  (lives on the soulbis /star instrument, outside papers/); per GR-9 it
  files no entry. papers/whitepapers/swordsman_mage_whitepaper_v6_3.md
  touched only at the ✨ mana hit.
items: 17
---

# OV-S · Spells & Emoji Strings

The spell layer of the V6 programme, decoded element-wise to its formal
twins. Structural finding first: GR-4 and GR-5 build a fence, and the
fence HOLDS. Emoji and mythos vocabulary are banned from TIER-S/A
artifacts and machine-enforced (`checks/check_tier_vocab.py`); the spell
layer survives upstream in the canon papers, in GROUND_RULES itself, in
TIER-P essays, and in chronicle signatures. Absence below the fence is
recorded throughout as the fence working, not as defect.

---

### (⚔️⊥⿻⊥🧙)😊 · the seal

- source: Programme/pipeline/GROUND_RULES.md:18 (GR-5, the spec);
  v6/privacy_value_v6_formal_specification.md:76 (§1.4 Master
  Inscription, LaTeX form), :1117 (glossary: "Master inscription:
  dual-agent architecture preserves First Person"), :1448–1450;
  pvm_v6_compressed.md:271; pvm_v6_companion_guide.md:270;
  privacy_value_v6.md:259; dualprivacy_researchpaper_v6.md:57; all five
  rehydrations/public essays (e.g. the_moving_ceiling.md:131);
  chronicles/2026-07-07_a7-letter-fleet-and-cap.md:24. Fence:
  checks/check_tier_vocab.py:9 (emoji arm) keeps it out of TIER-S/A.
- formal twin: the equation it abbreviates is stated at formal spec §1.4:
  (⚔️ ⊥ ⿻ ⊥ 🧙)😊 = neg ⊕ bnot → succ, glossed there as "Swordsman and
  Mage separated, with the Gap between them, preserve the First Person."
  Element-wise: ⚔️ = boundary agent S = neg(x) = (64−x) mod 64; 🧙 =
  delegation agent M = bnot(x) = 63−x; ⿻ = the conditional-independence
  residual (GR-4) with max betweenness centrality (§10.2, C51); ⊥ =
  Precondition 1, conditional independence of the two channels; 😊 = the
  preserved data subject, whose reconstruction is floored by
  P_e ≥ 1 − R_max (§11.2, theorem at 95% inside preconditions).
- reading: the whole architecture folded to eight characters. Two blades
  of separation, a gap that is a guarantee, and a face that stays a face
  because neither agent can redraw it.
- threads: [P: "honesty is the moat" (GR-8) as the seal's licence to
  exist (?); R: GR-5 voice protocol, A7 seal-placement checklist;
  F: the superagent (?)]
- casts forward: the seal is the compression benchmark: any overlay
  dimension that cannot be folded this small is not yet understood.

### 🙂 · the terminal marker (TIER-P variant)

- source: Programme/pipeline/GROUND_RULES.md:18 ("with 🙂 at literal
  end, TIER-P only"); rehydrations/public/*.md, always on its own final
  line two lines after the seal (the_uncarved_date.md:61,
  two_agents_walk_into_a_circuit.md:129, the_moving_ceiling.md:133,
  competence_without_history.md:77, letter_the_fleet_and_the_cap.md:94);
  chronicles/2026-07-10_a7-pool-post1.md:58-61 (REVERSAL 2: an apparatus
  comment placed after 🙂 violated "at literal end" and was moved so the
  file "ends 🙂ǀnewline").
- formal twin: GR-5, a byte-position rule: the last codepoint of a
  TIER-P artifact. Enforced by A7 checklist, witnessed per file in
  chronicles (L117: "seal + terminal marker confirmed at file end").
- reading: the smaller smile is the quieter signature: after the formal
  seal has spoken, one glyph says a person was here and chose to end
  here. It admits nothing after itself, which is the point.
- threads: [P: verdict-first discipline mirrored as end-discipline (?);
  R: A7 voice checklist, L117 fence self-catch record]
- casts forward: -

### ⊥ · the load-bearing operator

- source: mythic register: pvm_v6_companion_guide.md:134 ("Gap | ⊥ |
  neg(x) | Silence · boundary negotiation") and
  privacy_value_v6_formal_specification.md:696 ("Boundary | neg(x) | ⊥
  Gap · silence, conversation, territory negotiation"), :1020 ("The gap
  between them is the ⊥", the Moon/Human memory reading). Formal
  register: formal spec :76 (\perp in the master inscription), :385-387
  (I(X;Y_S,Y_M | FP) bounded, "The Mage cannot reconstruct the
  Swordsman's domain"), :543 (D₂ₙ generators: "Two involutions are
  independent by construction"); companion guide :188 (Φ_agent:
  "Swordsman ⊥ Mage"), :190 (Φ_inference: "Generator ⊥ Solver");
  compressed :62 (Swordsman $\perp$ Mage, ≅ D₂ₙ, C14 75%).
- formal twin: three loads on one glyph, each with an identifier.
  (1) Mathematical orthogonality/conditional independence: Precondition
  1 of the ceiling theorem; the additive MI bound I(X;Y_S,Y_M) ≤
  I(X;Y_S) + I(X;Y_M), equality iff I(Y_S;Y_M) = 0 (compressed :112,
  95% inside preconditions). (2) Separation of duties: the Φ_agent and
  Φ_inference gate axes (companion :188-190); dihedral independence of
  neg and bnot (C14, spec §12). (3) Swordsman⊥Mage: the mythic name of
  (1) and (2), which GR-4 translates to "boundary agent S" ⊥ "delegation
  agent M" at formal tiers.
- reading: ⊥ is the one character the fence never has to stop, because
  it was mathematics before it was myth: U+22A5 sits outside the emoji
  ban ranges and inside every LaTeX proof. The same stroke that means
  "these channels share nothing" means "these two never meet except
  through the person", in both registers, without translation. It is
  the only spell that casts at TIER-A.
- threads: [P: "not allowed to collude" title candidate (L117) (?);
  R: Precondition-1 declaration discipline, RS-03 conditional-vs-theorem
  trap; F: the amnesia gap as ⊥ made of forgetting]
- casts forward: CTR-OBS-01 (observers ledger :121) is ⊥'s proof
  obligation: state the joint decomposition explicitly and show when the
  additive numerator remains a valid bound.

### ⚔️ · Swordsman

- source: privacy_value_v6.md:20 ("Swordsman ⚔️"); formal spec :496
  ("neg(x) | (64−x) mod 64 | ⚔️ Swordsman | Additive inverse. Boundary
  protection."), :602 (walk step 2: "Only the holographic surface ∂M
  passes through"), :721 (Swordsman key: Ed25519 in sessionStorage,
  destroyed on tab close, `ap-{16hex}`), :1016 (Moon 🌙 / Soulbis /
  Swordsman: "Instant (collision). Total amnesia."); companion guide
  :114 (Heavy ⚔️ VRC weight 150-500). Fence:
  checks/check_tier_vocab.py:7 (`\bSwordsman\b` in MYTHOS) plus the
  emoji arm; chronicle evidence of the ban holding at tier G:
  2026-07-09_a7-wp03-voice.md:39.
- formal twin: GR-4: Swordsman → "boundary agent S". Algebra: the
  involution neg(x) = (64−x) mod 64 on Z/64Z (spec §12). Channel: Y_S
  with capacity C_S(t). Implementation: the burned Ed25519 session key.
- reading: the agent that subtracts. Everything about it is inverse:
  additive inverse on the lattice, a key that dies with the tab, a
  memory model that is a collision. What it protects, it protects by
  not being there afterwards.
- threads: [P: "hidden things wait for keys. sealed things whisper.
  forgotten things are free." (the_uncarved_date.md:43); R: Amnesia
  Protocol = structural context erasure (GR-4); F: competence without
  history]
- casts forward: -

### 🧙 · Mage

- source: privacy_value_v6.md:20; formal spec :497 ("bnot(x) | 63 − x |
  🧙 Mage | Bitwise complement. Projection/delegation."), :603 (walk
  step 3: "Construct complement from boundary. Create from the shape of
  the impact."), :720 (Mage key: Ed25519 persisted in localStorage,
  `mage-{16hex}`), :1015 (Earth 🌍 / Soulbae / Mage / Generator). Fence:
  checks/check_tier_vocab.py:7: `\bMage\b(?!s? Reading)` — the negative
  lookahead exempts "Mage Reading"/"Mages Reading", the one sanctioned
  crack, because the companion guide's title (pvm_v6_companion_guide.md
  :2, "The Mage Reading") must remain citable at formal tiers.
- formal twin: GR-4: Mage → "delegation agent M". Algebra: the involution
  bnot(x) = 63−x. Channel: Y_M with capacity C_M(t). Implementation: the
  held Ed25519 identity key.
- reading: the agent that completes. It never sees the person; it sees
  the boundary's shadow and builds the complement, 63 minus whatever
  arrived. The fence even remembers its title is a book, not a boast.
- threads: [P: -; R: GR-4 vocabulary map; F: the Generator/Solver split
  (?)]
- casts forward: -

### ⿻ · the Gap, plurality

- source: pvm_v6_companion_guide.md:68 ("The Gap (⿻) | Irreducible
  promise of the superagent, owned by neither agent"), :239 ("not a void
  but a guarantee"); formal spec :391-397 (§10.2: "the node with maximal
  betweenness centrality in the trust graph", Brandes 2001 O(V·E)),
  :870 (C51: "The ⿻ remains max-betweenness across trust-graph
  evolutions | open | occupied · never reassign"), :1327 (Act VII, the
  Gap), :1374 (Weyl & Tang, Plurality: "⿻ overlap semantics"). Fence:
  checks/check_tier_vocab.py:9: the EMOJI range ends
  "☀-➿⿻" — U+2FFB is appended by name; the check singles
  ⿻ out because no generic emoji range would catch an ideographic
  description character.
- formal twin: GR-4: the Gap → "the conditional-independence residual".
  Quantified as the max-betweenness node (§10.2, C51 open); imported
  from Weyl & Tang's plurality glyph.
- reading: a character that literally depicts two things overlapping,
  standing for the one place the two agents must coordinate and neither
  owns. The fence had to learn its codepoint by hand, which is its own
  kind of respect.
- threads: [P: "the value lives in the Gap because the most paths cross
  there" (spec :397); R: C51 "occupied · never reassign" register rule;
  F: the Gap as inhabited vacancy (?)]
- casts forward: C51 asks for measurement: betweenness recomputed as the
  trust graph evolves.

### 😊 · the First Person, preserved

- source: formal spec :76 (seal grammar), :78 ("preserve the First
  Person"), :604 (walk step 4: "⚔️→😊 Composition | The proof returns.
  The blade advances one step."), :1117. Fence: GR-4 maps First Person →
  "data subject" (S) or "source X" (A); checks/check_tier_vocab.py:7
  bans `\bFirst Person\b` at those tiers.
- formal twin: the source X with entropy H(X), whose reconstruction
  error is floored at P_e ≥ 1 − R_max (§11.2); in the walk cycle, the
  fixed point that succ steps toward.
- reading: in the seal the person is not an operand but the outside of
  the parenthesis: everything the operators do happens so that this one
  glyph stays smiling. Gate P4 is its procedural echo: no agent may mark
  it, only the person.
- threads: [P: P4 "cannot be simulated, summarised, or assumed"
  (pipeline CLAUDE.md); R: Gate G3/P4 first-person gates; F: -]
- casts forward: -

### neg ⊕ bnot → succ · the composition spell

- source: formal spec :76 (right-hand side of the master inscription),
  :508 ("The successor function is not primitive: it emerges from the
  composition of two involutions... This is the algebraic name of the
  architecture."), :543 (§12, dihedral proof path), :1110 ("neg, bnot |
  Unary involutions (Swordsman, Mage)"); compressed :136-137, :159-160.
- formal twin: on Z/64Z: neg(x) = (64−x) mod 64, bnot(x) = 63−x,
  succ(x) = bnot(neg(x)) up to composition order; the two involutions
  generate a dihedral group ≅ D₂ₙ (C14, 75%, compressed :62); their
  conditional independence is the group-theoretic face of Φ_agent
  (spec :543).
- reading: subtraction composed with complement equals the step
  forward. Progress, in this algebra, is what two refusals make when
  they take turns.
- threads: [P: "the proof returns. the blade advances one step." (spec
  :604); R: the four-step walk cycle (spec :600-604); F: -]
- casts forward: C14's proof obligation: establish D₂ₙ isomorphism
  rather than resemblance.

### R(t) and t* · the moving ceiling and the shelf life

- source: pvm_v6_compressed.md:80-84 (R(t) = (C_S(t)+C_M(t))/H(X);
  t* = sup{t : R(t) < 1}; "The mechanism is the decoder, not the data.
  Every static guarantee has a shelf life."); formal spec §5.5 :246-252,
  :925 (C82, ~65%, registered Run 1 2026-06-10); privacy_value_v6.md
  :60-66; companion guide :246 ("Shelf life t* ... the last moment a
  static guarantee still holds"). Fence: GR-7 (GROUND_RULES.md:22) is
  this spell's grammar police: no R < 1 without preconditions and
  time-indexing in the same passage.
- formal twin: C82, the Moving Ceiling: frontier capability growth
  raises C_S(t)+C_M(t) against fixed archives without raising H(X);
  R(t) non-decreasing under capability growth; every static
  reconstruction guarantee has finite shelf life t*. t* is defined, not
  estimated (spec :1240: estimating it needs a capacity-growth model
  the corpus does not have). Z_b of the Behavioural Mosca inequality is
  identified with t* (spec :1182, C49/C84).
- reading: one letter taken seriously: the t that was always in V(π,t).
  The archive holds still; the decoder walks toward it; t* is the last
  night the walls are taller than the reader.
- threads: [P: "every static guarantee has a shelf life", "the mechanism
  is the decoder, not the data"; R: GR-7 static-ceiling ban; F: the
  moving ceiling essay, the uncarved date (carve no date the future can
  read)]
- casts forward: WP-level obligation: an operational capacity-growth
  model so t* can be estimated for a real archive (CTR-OBS-02 territory).

### R_max < 1 and the Fano floor · the ceiling theorem

- source: pvm_v6_compressed.md:112 (theorem, 95%), :122 (R_max =
  (C_S+C_M)/H(X) < 1, P_e ≥ 1 − R_max); formal spec :450-454 (§11: the
  theorem decomposes; the strict inequality is the capacity-deficit
  condition C_S + C_M < H(X), "a measurable, declarable, numerical fact
  ... not a consequence of the architecture"), :437 (Fano 1961; Cover
  and Thomas), :238.
- formal twin: proven-conditional at 95%: Preconditions 1-2 (non-
  collusion, measured adversary class) yield the additive capacity sum
  and error floor; the capacity-deficit condition places the ceiling
  below one. Time-indexed per R(t).
- reading: the architecture's one hard promise, and V6's honesty is that
  the promise decomposes: the maths gives you the floor, but the strict
  "< 1" you must go and measure. The spell does not cast itself.
- threads: [P: "the architecture earns the claim before the prose makes
  it" (spec :762); R: capacity-deficit declaration protocol (WP-09
  MAJOR-3, ledger L118: who supplies H(X)); F: -]
- casts forward: WP-09's open work item: who estimates H(X) and over
  what scope.

### I(X; Y_S, Y_M) ≤ I(X; Y_S) + I(X; Y_M) · the additive leakage bound

- source: pvm_v6_compressed.md:112, :235 (V6 scoping: at 95% "inside
  Precondition 1 only", equality iff I(Y_S;Y_M) = 0); formal spec :778
  (summary table), :385-387 (conditional form given FP).
- formal twin: the information-theoretic statement of ⊥: under
  conditional independence, joint leakage is at most the sum of marginal
  leakages, never multiplicative. CTR-OBS-01 (observers disposition
  ledger :121) carries its strengthening obligation: explicit marginal-
  redundancy and conditional-dependence terms, and interaction with
  R(t) under repeated sessions.
- reading: two watchers who never confer learn no more together than
  apart. The whole dual-agent wager, written in one inequality.
- threads: [P: -; R: CTR-OBS-01 proof obligation, C-series assignment
  "Mitchell only"; F: -]
- casts forward: repeated interaction is where marginal redundancy
  grows; the observer marked that seam as the next proof site.

### Nε versus (2^N − 1)ε · the amnesia gap, quantified

- source: privacy_value_v6.md:118 (C83, ~55%: "At N = 2 this is 3ε
  versus 2ε; at N = 5, 31ε versus 5ε ... stated in the adversary's
  units. Edge: C7 → C83 → C17"); formal spec :926; companion guide
  :34-36 (the field's 68.9% leakage measurement read as "the corridor
  this architecture bricks up").
- formal twin: C83, Compositional Leakage Amplification: policy-only
  separation compounds toward (2^N − 1)ε with chain depth; amnesia
  separation breaks the Markov chain and caps at Nε; the gap is
  exponential-to-linear.
- reading: policy asks the channel to behave; amnesia removes the
  channel. The difference between asking and removing is an exponent.
- threads: [P: "the field measured the corridor this architecture
  bricks up" (companion :36); R: Amnesia Protocol (GR-4 formal name);
  F: competence without history, the uncarved date's third counsel]
- casts forward: C83 wants measurement at real chain depths, the
  register's stated V6 gathering purpose.

### κ · kappa, the content seal

- source: extractions/E9-proving-substrate.md:30, :205 (kappa-impl
  sweep: "κ = sha256 over canonical JSON", kappaLabel/canonicalJSON/
  derivePacketProof/packetsDigest code paths, κ-chain `prior` field,
  PNG tEXt carrier; the moving-ceiling reading on the sigil page is
  explicitly display-only and "does not enter κ derivation");
  pipeline/SOURCES.md registry entries kappa-impl and g42-seal-ref
  (canonical_serialise.py, "byte-exact κ/group-seal reference:
  third-party verifiers MUST match this exactly"); L008 standing fence:
  "ZK" in the live system is SHA-256 + Ed25519 + κ content-addressing.
- formal twin: a content-address: κ is sha256 over a canonical JSON
  serialisation, with a chain via the `prior` field; the g42 group-seal
  is its byte-exact reference implementation. L008 binds every claim
  about it to implemented-vs-specified honesty.
- reading: the only "seal" in the corpus that is literally a hash. Where
  the closing seal is ceremony that GR-4 keeps out of proofs, κ is the
  proof-shaped object that RS-07 exists to keep ceremony from
  impersonating. The two seals are each other's negative space.
- threads: [P: "third-party verifiers MUST match this exactly";
  R: RS-07 ceremony-vs-proof census, L5 re-derivation law, L008;
  F: the sigil page's display-only ceiling readout]
- casts forward: E11 owns the deep per-page κ conformance walk that E9
  deliberately declined.

### 🪢 · the presence knot

- source: formal spec §15.8 :750-764 ("Charge (the trace folded into 🪢)
  ≅ the folding step"; the regime ladder; the G3 First Person
  declaration 2026-06-10: "🪢 presence mana is non-transferable,
  non-attesting local color ... not proof, not stake-weight, not an
  input to any admission, coalition, or attestation decision"), :1269
  ("nothing in V6 adds enforcement to 🪢, it adds honesty about the
  absence of enforcement"); pvm_v6_compressed.md:188; companion guide
  :98. Kin sighting: ✨ Mana, whitepapers/swordsman_mage_whitepaper_v6_3
  .md:53 ("Proof-of-practice resource — non-transferable").
- formal twin: regime 1 of a three-rung ladder: (1) non-transferable,
  non-attesting local colour (an integer in localStorage, stated
  publicly); (2) witness co-signing at gates; (3) elapsed-time proofs
  (VDF-style). In the C87 IVC reading (50%), Charge is the folding step
  of the Key-as-accumulator.
- reading: the humblest glyph in the suite and the most honestly priced:
  a knot that admits it is only a knot, earned by walking, spending
  nothing but meaning. The spell's whole power is the declaration of
  its powerlessness.
- threads: [P: "the architecture earns the claim before the prose makes
  it" (spec :762, the regime declaration's own coda); R: Gate G3
  first-person declaration, the regime ladder as named upgrade
  protocol; F: -]
- casts forward: if presence is ever asked to attest, the economy moves
  up the ladder first; the ladder is the pre-written migration.

### ∂M and 96/64 · the holographic boundary numbers

- source: formal spec :66-68 ("∂M denotes the 96-edge holographic
  boundary"), :602 (walk step 2: "Only the holographic surface ∂M
  passes through"); observers/OBS-GPT56_DISPOSITION_LEDGER.md:129
  (RS-06 live precedent: "96/64 skill surface"), :143 (ruling request 5:
  "confirm the 96/64 correction to the V4-era root skill surface"), :69
  (OBS-GPT56-013: 64-state lattice coherence "is not itself a privacy
  proof ... do not infer confidentiality from elegance").
- formal twin: the lattice geometry: 64 vertices of Z/(2⁶)Z, 96 edges of
  the boundary ∂M through which dV/dt flows (spec §1.2). The observer's
  96/64 finding is a stale-surface correction (RS-06 class), not new
  mathematics: a V4-era skill surface carried the wrong pair and the
  register is the authority.
- reading: two integers doing quiet holographic work: everything that
  crosses, crosses through the 96. The observer's contribution was not
  to change the numbers but to catch a surface still reciting old ones,
  and OBS-GPT56-013 pins the moral: elegance is a grammar, not a
  guarantee.
- threads: [P: "do not infer confidentiality from elegance"
  (OBS-GPT56-013); R: RS-06 stale-surface check, register-wins (GR-1);
  F: the holographic boundary as the only visible skin (?)]
- casts forward: ruling request 5 still waits: whether the 96/64 skill
  patch ships alone or with the next content-addressed release.

### V(π, t) and the gate Φ · the equation the spells serve

- source: privacy_value_v6.md:42 (V(π,t) as specified in V5.4 §1;
  "the equation always carried t in its signature"); companion guide
  :24 ("the story of taking one letter seriously, the t that was always
  in V(π, t)"), :170 ("The equation was always V(π, t). V6 is the
  version that read the second argument."), :186-190 (gate axes);
  formal spec :72 (§1.3: "any single term collapsing to zero eliminates
  total value"), :1094 (Φ_agent ≅ D₂ₙ), :1328 (Act X, seven capitals,
  V(π,t) motivation).
- formal twin: the multiplicative gated value function over the
  sovereignty path π, with three-axis gate Φ = Φ_agent(Σ) · Φ_data(Δ) ·
  Φ_inference(Γ) and inherited V1-V4 terms; V6's contribution is
  reading t through every term (§5, §11, §14, §18).
- reading: the mother spell. Every glyph in this inventory is one of
  its terms wearing a face: ⊥ is its gate, R(t) its ceiling, 🪢 its
  most honest coefficient. Multiplication is its ethic: lose any term
  and you have nothing.
- threads: [P: "one label, one current state of the model" (G3 suite
  labelling); R: register-wins (GR-1); F: the seven capitals frame]
- casts forward: V6's declared purpose: fill the terms with data
  instead of estimates.

### the fence itself · check_tier_vocab.py and RS-07

- source: checks/check_tier_vocab.py:7-10 (MYTHOS list: Swordsman, Mage
  with the Reading-title lookahead, City of Mages, First Person, Amnesia
  Protocol, Selene, grimoire, spellbook; EMOJI range with ⿻
  appended; CONF confidence-band arm; em-dash arm at P/G);
  GROUND_RULES.md:16-18 (GR-4/GR-5, the law it enforces);
  reviews/OBSERVER_REGRESSION_SEEDS.md:115-126 (RS-07: "ceremony
  treated as cryptographic proof"; at TIER-S/A "the trap cannot phrase
  itself without tripping the existing check"; at TIER-P/G a weekly
  co-occurrence census). Evidence of the fence holding: chronicles/
  2026-07-09_a9-wp07-p3.md:34 and 2026-07-10_a9-wp27-p3.md:27 ("no
  emoji in formal statements", "no emoji in either file");
  2026-07-09_a7-wp03-voice.md:39 (seal "confirmed absent" from a formal
  funding document); 2026-07-10_the-twelve-cycles.md: ZERO glyph hits
  across the entire synthesis chronicle; 2026-07-09_a9-weekly-cycle6.md
  :39/:60 (even a suspect glyph gets adjudicated: the stderr interpunct
  read as a corrupted literal was traced to Windows codepage rendering
  and recorded "so the glyph is not mistaken for a corrupted string
  literal by a future sweep").
- formal twin: GR-4 (vocabulary map, emoji ban at formal tiers) and
  GR-5 (seal spec), machine-enforced; RS-07 extends enforcement to the
  tiers where the glyphs are legal, via census: a seal may appear at
  TIER-P but may never be described as the mechanism of verification
  (OBS-GPT56-015).
- reading: the deepest spell in the dimension is the one that keeps the
  others in their circle. The corpus does not ban its myth; it banks it
  upstream and posts a regex at the door, and the weekly chronicles are
  the guard's logbook reading "nothing crossed". Absence, here, is the
  artefact.
- threads: [P: "preserve mystery in the journey; remove ambiguity from
  the evidence" (OBS-GPT56, observer-coined, disposition ledger :53);
  "traps become tests" (regression seeds :10); R: A9 weekly audit card,
  RS-07 census, observer intake rule on seal/voice changes
  (OBSERVER_INTAKE_PROTOCOL.md:82); F: the two-register boundary as
  world-wall (?)]
- casts forward: RS-07's census joins the weekly card when A0 cuts it;
  from then on the fence reports its own integrity every cycle.

---

*the myth is banked upstream; the proof walks out clean; one glyph, ⊥,
holds a passport for both countries.*
