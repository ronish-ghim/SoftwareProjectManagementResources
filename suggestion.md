# SPM Study Notes — Suggestions

## Content Gaps

### High Priority
- **Unit 5 — Add resource smoothing/balancing numerical examples**: Currently no worked examples for resource histogram analysis, leveling, or smoothing calculations. This is a calculation-heavy topic in the syllabus with zero numerical problems.

### Medium Priority
- **Unit 9 — Add diagrams/images**: Zero images despite covering baseline lifecycle, CM process flow, and version control concepts — even basic flowcharts would help.
- **Unit 8 — Add "types of testing" section**: Covers levels of testing (unit/integration/system/acceptance) but not types (black-box, white-box, gray-box) which the syllabus mentions.
- **`notes/img_desc.md` — Complete image tracking**: Currently only covers ch02 and ch03 partially. Chapters 1, 4, 5, 6, 7, 8, 9 have no entries.

### Low Priority
- **Unit 1 — Give "software product attributes" standalone treatment**: Attributes like invisibility, complexity, conformity, flexibility are covered implicitly but not as a dedicated section.
- **Unit 7 — Add "Conclusion" and "Further Exercises" sections**: Listed in the syllabus but not present as named sections in the notes.

---

## Viewer (`index.html`) Improvements

### Bugs
- ~~**Zoom causes layout clipping**: `transform: scale()` on `.markdown-body` doesn't change the element's actual layout box, causing overflow, clipping, and TOC/progress bar misalignment. Replace with `document.body.style.fontSize` scaling or CSS `zoom`.~~ ✅ Fixed — uses CSS `zoom` property.

### UX Enhancements
- ~~**Mobile TOC panel**: TOC panel (`#tocPanel`) is visible on small screens and overlaps main content. Should be hidden or collapsed on mobile.~~ ✅ Fixed — hidden at ≤1200px, main content margin adjusts.
- ~~**URL hash for headings**: Scrolling past headings doesn't update `location.hash`, making deep links to specific sections impossible. Use `history.replaceState()` on scroll.~~ ✅ Fixed — debounced scroll handler updates hash.
- ~~**Back-to-top button**: Long documents lack a quick way to scroll back up. Add a floating button.~~ ✅ Fixed — floating button appears after 500px scroll.
- ~~**Print stylesheet**: Printing the viewer produces unreadable output. Add `@media print` rules.~~ ✅ Fixed — hides chrome, adjusts layout.
- ~~**Image lazy loading**: Add `loading="lazy"` to `<img>` tags generated from markdown for faster initial page load.~~ ✅ Fixed — applied to all markdown images after render.
- **Scroll restoration**: Browser "Back" button doesn't restore scroll position within a note.

### Technical
- ~~**Use IntersectionObserver for TOC active tracking**: Current scroll event + `offsetTop` check is less performant. `IntersectionObserver` would be smoother.~~ ✅ Fixed — replaced with `IntersectionObserver`.
- ~~**Mermaid error visibility**: `suppressErrorRendering: true` + `.catch()` only logs to console with no user-visible feedback. Consider showing a small inline error message.~~ ✅ Fixed — red error box replaces failed diagram.
- **No offline fallback**: All JS libraries loaded from CDN. No internet = blank page. Consider a service worker or bundling critical dependencies.

---

## Documentation

- ~~**`AGENTS.md` — Update stale claim**: Says "Only one localStorage key used" but zoom persistence uses a second key `spm-zoom`.~~ ✅ Fixed.
- ~~**`AGENTS.md` — Remove duplicate line**: Line 44 was an exact duplicate of line 43 (`startOnLoad: false`).~~ ✅ Fixed.
- **`notes/img_desc.md` — Polish format**: Currently has fragmentary notes ("then next one is forward pass process"), mixed path separators (`\` vs `/`), and incomplete checkmarks.

---

## Image Assets

- **ch03 images 213–217, 220–224** — not documented in `img_desc.md` at all. Verify and add descriptions.
- **All chapters — verify image placement matches notes**: `img_desc.md` suggests some images are duplicates or unknown. A full audit would clean this up.

---

## Repository

- **Commit `.gitignore`**: Currently exists locally with `temp/` entry but is not tracked in git.
- **Clean up `temp/`**: Contains `gen_ppt.py` and `unit3_section4_5.pptx` — determine if these should be kept or removed.
