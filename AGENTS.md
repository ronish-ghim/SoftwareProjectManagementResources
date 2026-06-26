# SPM Study Notes — Agent Guide

This is a **study material repository** for CSC415 (Software Project Management), BSc CSIT 7th Sem, Tribhuvan University. It contains markdown notes, lecture PDFs, and an HTML viewer.

## Quick start
- Open `index.html` in a browser to browse notes (no server needed — all JS from CDN)
- Viewer is a JS SPA: fetches `.md` files via `fetch()`, renders with marked+KaTeX+highlight.js

## Repository structure
```
Root           syllabus.md, cheatsheet.md, study_guide.md — exam prep
               index.html — SPA viewer
notes/         unit_01*.md .. unit_09*.md — primary note content
notes/old_notes/   — stale copies of same 9 units (out of date)
notes/assets/      — images referenced by notes
Class_notes/       — 9 lecture PDFs (Chapter_1*.pdf .. Chapter_9*.pdf)
ref/               — reference PDFs (Z-table, interest tables)
```

## Viewer conventions (`index.html`)
- Notes are registered with group assignments (1-4) in the `notes` array (line ~632)
- Supplements (`syllabus.md`, `cheatsheet.md`, `study_guide.md`) registered in `supplements` array
- Hash routing: `#unit_01_*.md` loads a note; `#` returns to welcome page
- Search queries all 9 notes + 3 supplements (fuzzy line-level, 3 matches max per file)

## Key facts
- **No build system, no package.json, no tests, no CI/CD, no `.gitignore`**
- Notes reference images via `notes/assets/` prefix; viewer rewrites them at render time
- Ref PDFs can be linked from notes — they live in `ref/`
- Unit note filenames follow: `unit_XX_<topic>.md`
- `cheatsheet.md` contains all formulas (PW, FW, AW, IRR, BCR, CPM, PERT, EVM)
- `study_guide.md` contains exam strategy and numerical walkthroughs

## Constraints
- Do not modify `Class_notes/` PDFs or `ref/` PDFs
