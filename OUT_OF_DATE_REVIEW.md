# Out-of-Date Docs Review
## agentprivacy-docs repo — Jan 2026

Quick audit of what’s stale after the v1.3 / IEEE 7012 / Spellbook v5 push.

---

## 1. PDFs and .tex (binary/source assets)

| File | Status | Action |
|------|--------|--------|
| **dualprivacy_researchpaper_v3_5.pdf** | Stale — canonical is v3.6 (.md) | Regenerate from v3.6 (or from .tex if you add v3.6.tex); then remove v3_5.pdf or keep as “v3.5 archive” |
| **dualprivacy_researchpaper_v3_5.tex** | Stale | Add **dualprivacy_researchpaper_v3_6.tex** if you build PDF from LaTeX; remove or archive v3_5.tex |
| **swordsman_mage_whitepaper_v4_6.md** | Old — canonical is v4.8 | Remove or keep as archive (v4.6 is still in repo) |
| **swordsman_mage_whitepaper_v4_6.pdf** | Old | Remove or archive; add **v4_8.pdf** when generated |
| **swordsman_mage_whitepaper_v4_6.tex** | Old | Remove or archive; add **v4_8.tex** when you have it |
| **swordsman_mage_whitepaper_v4_7.pdf** | Stale — .md removed | Remove or archive |
| **swordsman_mage_whitepaper_v4_7.tex** | Stale | Remove or archive |

**Summary:** No PDF/tex for current **v3.6** (research) or **v4.8** (whitepaper). Old v3.5 and v4.6/v4.7 assets still present. Either regenerate current versions and add them, or remove/archive the old ones so the repo doesn’t imply they’re canonical.

---

## 2. Markdown cross-references to old versions

These files still cite old doc versions. Updating them avoids confusion.

| File | Old refs | Update to |
|------|----------|-----------|
| **vrc_promise_protocol_economic_architecture_v3_0.md** | Whitepaper v4.7, Research v3.5, Glossary v2.2 | v4.8, v3.6, v2.3 |
| **research_proposal_v1_4.md** | Research v3.5, Whitepaper v4.7, Spellbook v4.1.1 | v3.6, v4.8, v5.0 |
| **understanding_as_key_zypher_paper_v1.md** | Visual Guide v1.2, Research Proposal v1.2 | v1.3, v1.4 |
| **promise_theory_reference_v1_0.md** | Glossary v2.1→v2.2, README v1.1→v1.2 | v2.3, v1.3 |
| **swordsman_mage_whitepaper_v4_6.md** | Glossary v2.2 | If you keep this file, note it’s legacy; or remove |
| **GLOSSARY_MASTER_v2_3.md** | Internal refs “This Glossary v2.2”, “Whitepaper v4.4”, “Research Proposal v1.2” | v2.3, v4.8, v1.4 |
| **swordsman_mage_whitepaper_v4_8.md** | “Dual Privacy Architecture v3.5” (research) | v3.6 |

**COMMIT_DESCRIPTION_AND_REPO_COMPARISON.md** and **SPELLBOOK_STRUCTURE_OPTIONS.md** describe the Dec→Jan update; fine to leave as-is for history.

---

## 3. QUICK_START.md

The “Documents Available” list is outdated:

- Currently says: Whitepaper v4.3, Research v3.2, Spellbook v4.0.1, Tokenomics v2.0, Visual v1.1, Research Proposal v1.1, Glossary v2.0.
- Should align with current suite, e.g.: README, What Agentprivacy Is, Whitepaper v4.8, Research v3.6, Spellbook v5.0, Tokenomics v3.0 (VRC), Visual v1.3, Research Proposal v1.4, Glossary v2.3, IEEE 7012 Quick Ref, etc.

Update the list (and doc count “8” if needed) so it matches what’s actually in the repo and on the server.

---

## 4. server.py — doc list and README route

**DOCUMENTS** is hardcoded to filenames that **no longer exist** in the repo:

- `0xagentprivacy_README_v1_1.md` → use **README.md**
- `swordsman_mage_whitepaper_v4_4.pdf`, v4_4.md, v4_3.md → use **swordsman_mage_whitepaper_v4_8.md** (and v4_8.pdf if you add it)
- `spellbook_v4_0_1_canonical.md` → **spellbook_v5_0_canonical.md**
- `tokenomics_economic_architecture_v2.md` → **vrc_promise_protocol_economic_architecture_v3_0.md**
- `VISUAL_ARCHITECTURE_GUIDE_v1_1.md` → **VISUAL_ARCHITECTURE_GUIDE_v1_3.md**
- `GLOSSARY_MASTER_v2_1.md` → **GLOSSARY_MASTER_v2_3.md**
- `research_proposal_v1_2.md` → **research_proposal_v1_4.md**
- `dualprivacy_researchpaper_v3_3.md` → **dualprivacy_researchpaper_v3_6.md**

So the index at http://localhost:7000 would currently show only entries for files that don’t exist (or would 404). You should:

1. Replace **DOCUMENTS** with the current set of docs (README.md, what-agentprivacy-is.md, whitepaper v4.8, research v3.6, spellbook v5.0, VRC v3.0, visual v1.3, glossary v2.3, research proposal v1.4, IEEE 7012 quick ref, promise theory ref, etc.).
2. Change the README special route from `0xagentprivacy_README_v1_1.md` to **README.md**.

---

## 5. GIT_SETUP.md

Says “All 8 documentation markdown files” — update to the actual count and optionally list the main docs so it stays accurate.

---

## Suggested order of work

1. **server.py** — Update DOCUMENTS and README route so the local server index matches the repo and links work.
2. **QUICK_START.md** — Update document list and count.
3. **PDFs/tex** — Either add v3.6 and v4.8 outputs (and optionally v4_8.tex/v3_6.tex) or remove/archive old v3_5, v4_6, v4_7 assets.
4. **Cross-refs** — Sweep VRC tokenomics, research proposal, understanding_as_key, promise theory ref, glossary, whitepaper v4.8 for “v3.5 / v4.7 / v2.2 / v1.2 / v4.1.1” and point them to v3.6, v4.8, v2.3, v1.3, v5.0 as appropriate.
5. **GIT_SETUP.md** — Adjust doc count and list if you care about that file being current.

If you want, next step can be a concrete patch for **server.py** and **QUICK_START.md** (exact DOCUMENTS list and copy for the “Documents Available” section).
