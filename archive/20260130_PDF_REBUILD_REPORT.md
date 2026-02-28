# PDF and .tex Rebuild Report
## agentprivacy-docs — January 30, 2026

---

## What Was Done

### 1. Build pipeline (emoji-capable PDFs)
- **Pandoc** used for: `md → html` and `md → tex`.
- **Playwright + Chromium** used for: `html → pdf` so **emojis and Unicode symbols** (⚔️, 🧙, ⊥, etc.) render correctly in the PDFs.
- **Script:** `build_pdfs.py` in the repo root. Run: `python build_pdfs.py` (requires `pandoc` on PATH and `pip install playwright` + `python -m playwright install chromium`).

### 2. New .tex and .pdf generated from markdown

| Source (.md) | Output (.tex) | Output (.pdf) |
|--------------|--------------|---------------|
| swordsman_mage_whitepaper_v4_8.md | swordsman_mage_whitepaper_v4_8.tex | swordsman_mage_whitepaper_v4_8.pdf |
| dualprivacy_researchpaper_v3_6.md | dualprivacy_researchpaper_v3_6.tex | dualprivacy_researchpaper_v3_6.pdf |
| vrc_promise_protocol_economic_architecture_v3_0.md | vrc_promise_protocol_economic_architecture_v3_0.tex | vrc_promise_protocol_economic_architecture_v3_0.pdf |

- **.tex:** `pandoc <file>.md -s -o <file>.tex`.
- **.pdf:** `pandoc <file>.md -s -o <file>.html` then Playwright Chromium prints HTML to PDF (A4, 20mm margins). Emojis and symbols render via browser engine.

### 3. Old PDF and .tex files removed

| Removed |
|---------|
| dualprivacy_researchpaper_v3_5.pdf |
| dualprivacy_researchpaper_v3_5.tex |
| swordsman_mage_whitepaper_v4_6.md |
| swordsman_mage_whitepaper_v4_6.pdf |
| swordsman_mage_whitepaper_v4_6.tex |
| swordsman_mage_whitepaper_v4_7.pdf |
| swordsman_mage_whitepaper_v4_7.tex |

- The legacy whitepaper v4.6 .md was also removed so the repo has a single current whitepaper (v4.8).

### 4. Server index updated
- **server.py** DOCUMENTS list now includes the three new PDFs so they appear on the index at http://localhost:7000 (Whitepaper v4.8 PDF, Research Paper v3.6 PDF, VRC Promise Protocol v3.0 PDF).

---

## Font / Unicode notes

- PDFs are built via **Playwright/Chromium** (HTML → PDF), so system/browser fonts and emoji (⚔️, 🧙, 😊, ⊥, etc.) render correctly.
- The **.tex** files are from Pandoc; building those with pdflatex/xelatex may still show missing-character for emoji unless you add an emoji font in a custom template. Use build_pdfs.py for PDFs with full emoji support.

---

## Repo state after rebuild

- **Whitepaper:** v4.8 only (.md, .tex, .pdf).
- **Research paper:** v3.6 only (.md, .tex, .pdf).
- **VRC paper:** v3.0 (.md, .tex, .pdf).
- No remaining v3.5, v4.6, or v4.7 PDF/tex in the repo.
