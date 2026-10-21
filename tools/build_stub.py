"""Build the public agentprivacy-docs: a map of the ecosystem, and the published volumes kept at their old paths.

    python tools/build_stub.py

The research corpus moves to the private repository agentprivacy-research. This repository keeps the address public:
  1. every file the public sites and the IPFS volumes link to, copied from the PUBLIC projection (origin/main of
     ~/agentprivacy-docs), so nothing that was not already public is published here;
  2. a README rendered from the soul mage's census-gated export (~/soul_mage/exports/labs-harness.json): the surfaces,
     suites and ways in, each already public on agentprivacy.org. Lanes and their results are not carried.
Re-run after the soul mage re-exports, then review the diff before any push.
"""
import json, os, pathlib, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent.parent
HOME = pathlib.Path.home()
DOCS = HOME / "agentprivacy-docs"
REF = "origin/main"                     # the public projection: only bytes that are already public
EXPORT = HOME / "soul_mage" / "exports" / "labs-harness.json"
ORG = "https://agentprivacy.org"

# paths the live sites, the skills and the IPFS volumes link to (census of 2026-10-21) that exist on the public ref
KEEP = [
    "LICENSE.md",
    "archive/privacy_value_v5_formal_specification.md",
    "ceremonies",
    "papers/lineage/understanding_as_key_zypher_paper_v1.md",
    "papers/v5/privacy_is_value_v5.md",
    "papers/v5/pvm_v5_4_companion_guide.md",
    "papers/v6/privacy_value_v6_formal_specification.md",
    "pdfs/v5/privacy_value_v5_4_formal_specification.pdf",
    "pdfs/v5/pvm_v5_4_compressed.pdf",
    "pdfs/v6",
    "reference/64_blades_reference_sheet.md",
    "reference/IEEE_7012_QUICK_REFERENCE.md",
    "reference/PAPERS_INDEX.md",
    "research/CONJECTURE_REGISTER_V6.md",
    "research/pvm-v6-soil-and-the-programme-runtime-evolutions.md",
    "research/uor-atlas-utqc-overlap.md",
    "research/uor-atlas-utqc-v6-note.md",
    "specs/vrc_promise_protocol_v3_3.md",
    "papers/lineage/dualprivacy_researchpaper_v4_3.md",
]
# old root-level paths that public pages still link to (already 404 before the move): a pointer file, or for a PDF a copy
POINTERS = {
    "IEEE_7012_QUICK_REFERENCE.md": "reference/IEEE_7012_QUICK_REFERENCE.md",
    "privacy_is_value_v5.md": "papers/v5/privacy_is_value_v5.md",
    "privacy_value_v5_formal_specification.md": "archive/privacy_value_v5_formal_specification.md",
    "pvm_v5_4_companion_guide.md": "papers/v5/pvm_v5_4_companion_guide.md",
    "dualprivacy_researchpaper_v4_0.md": ("papers/lineage/dualprivacy_researchpaper_v4_3.md",
                                          "Version 4.0 is not kept here; the nearest kept version is 4.3."),
    "promise_theory_reference_v1_3.md": (None, "This reference is not kept in the public repository."),
    "pdfs/privacy_value_v5_4_formal_specification.pdf": "pdfs/v5/privacy_value_v5_4_formal_specification.pdf",
    "pdfs/pvm_v5_4_compressed.pdf": "pdfs/v5/pvm_v5_4_compressed.pdf",
}


def write_pointers():
    for old, target in POINTERS.items():
        target, note = target if isinstance(target, tuple) else (target, None)
        out = HERE / old
        out.parent.mkdir(parents=True, exist_ok=True)
        if old.endswith(".pdf"):
            out.write_bytes((HERE / target).read_bytes())   # a link to a PDF expects the PDF
            continue
        lines = ["# Moved", ""]
        if note:
            lines += [note, ""]
        if target:
            lines += [f"This file now lives at [{target}]({target}).", ""]
        out.write_text("\n".join(lines), encoding="utf-8", newline="\n")
CIDS = [  # IPFS pins of the April 2026 volumes, each re-derivable from the pinned file's bytes
    ("bafkreiamwa6sukmeb4binexmmjlszbljnx6wk3iv6p4lgjusv5urhwyera", "PVM V5.4 formal specification (PDF)"),
    ("bafkreiavy3zpepoicyejrc7kgeam4mhbo7w56cdaniueiok3b2q43eyqla", "PVM V5.4 companion guide (PDF)"),
    ("bafkreifknnwrrga2rlnbfumcsplzvp4x7ayitfpjpq7k7oh4lck4msk5si", "PVM V5.4 compressed (PDF)"),
    ("bafkreicl677c52ayuw7i2cpxcc2534fuv4ehd7gbsc55ozotpbsuk3qqtu", "The grimoire v10.0.0 (JSON), 2026-04-07"),
]
# names not yet released: kept in a file outside this public repository, one per line; the build refuses without it
FORBIDDEN_FILE = HOME / ".agentprivacy" / "unreleased_names.txt"
FORBIDDEN = [l.strip().lower() for l in FORBIDDEN_FILE.read_text(encoding="utf-8").splitlines() if l.strip()] if FORBIDDEN_FILE.exists() else None


def git(*args):
    return subprocess.run(["git", "-C", str(DOCS), *args], check=True, capture_output=True).stdout


def copy_public():
    n = 0
    for path in KEEP:
        kind = git("cat-file", "-t", f"{REF}:{path}").decode().strip()
        files = ([f for f in git("ls-tree", "-r", "-z", "--name-only", REF, path).decode("utf-8").split("\0") if f]
                 if kind == "tree" else [path])   # -z: raw names (the ceremony folders carry emoji)
        for f in files:
            out = HERE / f
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_bytes(git("cat-file", "blob", f"{REF}:{f}"))
            n += 1
    return n


def absolute(href):
    return href if href.startswith("http") else ORG + href


def readme(d):
    L = ["# agentprivacy-docs", "",
         "The map of the agentprivacy ecosystem: where each part lives, what it does, and how to come in. "
         "The research corpus that used to be published here is now kept in a private repository; this repository keeps "
         "the published volumes at the paths that sites, skills and the IPFS-pinned specifications link to.", "",
         "## Where things live", "", "| Surface | What it is |", "|---|---|"]
    for s in d["surface"]:
        L.append(f"| [{s['label']}]({absolute(s['href'])}) | {s['text']} |")
    L += ["", "## What runs across it", "", "| Suite | What it does |", "|---|---|"]
    for s in d["suite"]:
        links = " ".join(f"[{l['label']}]({absolute(l['href'])})" for l in s.get("links", []) if l.get("href"))
        L.append(f"| {s['name']} | {s['does']}{(' ' + links) if links else ''} |")
    L += ["", "## Ways in", ""]
    for s in sorted(d["door"], key=lambda x: x.get("step", "")):
        L.append(f"- **[{s['name']}]({absolute(s['href'])})**: {s['text']}")
    L += ["", "## The published volumes", "",
          "The Privacy Value Model's April 2026 volumes are pinned to IPFS; each CID re-derives from the file's bytes.", "",
          "| CID | File |", "|---|---|"]
    L += [f"| `{c}` | {name} |" for c, name in CIDS]
    L += ["", "The volumes and references that public pages link to are kept here at their original paths: `papers/v5/`, "
          "`papers/v6/`, `pdfs/v5/`, `pdfs/v6/`, `ceremonies/`, `reference/`, `research/` and `specs/`.", "",
          "## Licence", "", "See [LICENSE.md](LICENSE.md).", "",
          "---", "",
          f"*The map above is rendered from the soul mage's census-gated record ({d['generated']}, "
          f"`{d.get('κ', d.get('kappa', ''))}`) by `tools/build_stub.py`; every line in it traces to a record already "
          "public on agentprivacy.org.*", ""]
    text = "\n".join(L)
    low = text.lower()
    hit = [w for w in FORBIDDEN if w in low]
    if hit:
        sys.exit(f"refused: the README would carry {hit}")
    return text


def main():
    if FORBIDDEN is None:
        sys.exit(f"refused: {FORBIDDEN_FILE} is missing (the list of names not yet released)")
    d = json.loads(EXPORT.read_text(encoding="utf-8"))
    n = copy_public()
    write_pointers()
    (HERE / "README.md").write_text(readme(d), encoding="utf-8", newline="\n")
    print(f"copied {n} public files from {REF}; README rendered from {EXPORT.name} ({d['generated']})")


if __name__ == "__main__":
    main()
