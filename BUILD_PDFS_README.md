# Building PDFs (with emoji support)

PDFs and `.tex` for the whitepaper, research paper, and VRC paper are built from the markdown sources so that **emojis and Unicode symbols** (⚔️, 🧙, ⊥, etc.) render correctly.

## Quick build

```bash
python build_pdfs.py
```

## Requirements

- **Pandoc** on PATH ([pandoc.org](https://pandoc.org) or `winget install JohnMacFarlane.Pandoc`)
- **Playwright + Chromium** for HTML→PDF (emoji-capable):
  ```bash
  pip install playwright
  python -m playwright install chromium
  ```

## What the script does

1. **Pandoc** converts each `.md` → standalone HTML (with UTF-8 and a minimal style).
2. **Playwright/Chromium** opens the HTML and prints to PDF (A4, 20mm margins). Emojis and symbols render via the browser engine.
3. **Pandoc** converts each `.md` → `.tex` for LaTeX source.

## Outputs

| Source | Outputs |
|--------|--------|
| swordsman_mage_whitepaper_v4_8.md | .tex, .pdf |
| dualprivacy_researchpaper_v3_6.md | .tex, .pdf |
| vrc_promise_protocol_economic_architecture_v3_0.md | .tex, .pdf |

See **PDF_REBUILD_REPORT.md** for full details.
