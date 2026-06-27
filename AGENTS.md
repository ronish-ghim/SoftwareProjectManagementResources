# SPM Study Notes — Agent Guide

Study material repo for CSC415 (Software Project Management), BSc CSIT 7th Sem, TU.
Markdown notes + HTML SPA viewer. No build system, no package.json, no tests.

## Quick start
- Open `index.html` in a browser — no server needed, all JS from CDN
- Viewer: marked + KaTeX + highlight.js + Mermaid; fetches `.md` via `fetch()`

## Repository structure
```
Root             syllabus.md, cheatsheet.md, study_guide.md — exam prep
                 index.html — SPA viewer
                 AGENTS.md, img_desc.md — agent/image tracking (not part of notes)
notes/           unit_01*.md .. unit_09*.md — primary note content
notes/old_notes/ — stale copies of same 9 units (do not use)
notes/assets/    — chapter-named subdirs (ch03/, etc.) with JPEG images
Class_notes/     — 9 lecture PDFs (do not modify)
ref/             — reference PDFs (Z-table, interest tables)
```

## Viewer conventions (`index.html`)
- Notes registered with group assignments (1-4) in `notes` array (line ~610)
- Supplements (`syllabus.md`, `cheatsheet.md`, `study_guide.md`) in `supplements` array
- refTools (`ztable`, `interest`) bypass markdown fetch — rendered inline via JS functions
- Hash routing: `#unit_01_*.md` loads note; `#syllabus.md` loads supplement; `#` returns to welcome
- Pipe suffix: `#file.md|N` scrolls to heading nearest line N; `#file.md|heading-id` scrolls to that heading
- Bare heading IDs (`#heading-id`) auto-resolve: heading map built on first miss from cached content, loads correct file and scrolls
- `basePath = 'notes/'`; supplements fetched from root (no prefix); refTools intercepted before fetch
- External links (`http://`/`https://`) open in `_blank` with `noopener`
- `.md` links within content are intercepted, path-stripped, and routed via `location.hash`
- All other links (anchor `#heading-id`, etc.) pass through normally

## Image references
- Notes reference images as `assets/chXX/ch03_img_XXX.jpeg`; viewer rewrites `assets/` → `notes/assets/` at render time
- Chapter 3 has 16 images (209–224)
- `notes/img_desc.md` tracks image descriptions (private, not loaded by viewer)

## Math rendering
- KaTeX with auto-render
- Placeholder system (`\uFFFC`) protects math from marked parsing and protects currency `$` from KaTeX

## Mermaid diagrams
- Diagrams in ` ```mermaid ` fenced blocks
- `startOnLoad: false` — viewer manually calls `mermaid.run()` after content load
- `mermaid.run()` must be called per-node (`.forEach(...)`) with `.catch()` — one failing diagram shouldn't block others
- Node labels with parentheses cause parse errors; avoid them in diagrams

## Theme & persistence
- Dark mode toggle, persisted in localStorage key `spm-theme` (default `light`)
- Zoom level persisted in a second localStorage key `spm-zoom`

## Search
- Exact substring match (case-insensitive), NOT fuzzy
- Searches all 12 markdown files (9 notes + 3 supplements) via cached `fetchContent()`
- Max 3 matches per file with 2-line context snippets; `"+N more"` note after 3rd
- Triggered on input >= 2 chars, debounced at 300ms

## Code blocks
- highlight.js for syntax highlighting
- Copy button injected into every `<pre>` block (Clipboard API)
- Keyboard: `/` focuses search, `Escape` clears search

## Other features
- TOC auto-generated from `<h2>`/`<h3>` elements
- Reading progress bar (fixed top bar, scroll-based width)
- Mermaid version: `mermaid@11` from jsDelivr
- marked version: 12.0.1

## Sidebar (collapsible at all sizes)
- Hamburger menu (`#menuBtn`) toggles `body.sidebar-closed` — works at all screen sizes
- Desktop (>820px): sidebar slides in/out; no overlay; link clicks keep sidebar open
- Mobile (≤820px): sidebar starts closed (`sidebar-closed` set on page load); overlay + body scroll lock; link clicks auto-close
- CSS transition `0.2s ease` on `.sidebar`; main content margin adjusts with `.main { margin-left }`

## Constraints
- Do not modify `Class_notes/` PDFs or `ref/` PDFs
- `notes/old_notes/` — stale backups; do not reference
- `.gitignore` exists locally as `temp/` (not yet committed)
