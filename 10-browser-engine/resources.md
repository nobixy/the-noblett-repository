---
title: "10 — Resources"
id: "MOD10-RES"
type: "reference"
module: "10-browser-engine"
phase: "D"
order: 1300
prerequisites: []
---

# 10 — Resources

*Pointers only. Glimpse is the course.*

## Standards (primary sources)
- **HTML Living Standard** (html.spec.whatwg.org) — section 13.2 "Parsing HTML documents" (tokenization 13.2.5; tree construction 13.2.6), section 4 for element meanings.
- **CSS 2.2** (w3.org/TR/CSS22) — chapters 8 (box model), 9 (visual formatting model: block and inline formatting contexts, anonymous boxes), 10 (widths and heights, line height), 6 (cascade and inheritance, still the clearest short description).
- **Selectors Level 4** (w3.org/TR/selectors-4) — specificity.
- **CSS Syntax Level 3** (w3.org/TR/css-syntax-3) — tokenizing CSS.
- **WAI-ARIA and the Accessibility Tree** — MDN's "Accessibility tree" glossary entry and "ARIA roles" pages for your a11y dump.

## Explanations
- **MDN Web Docs** (developer.mozilla.org) — "How browsers work," "Introduction to the CSS basic box model," "Inline formatting context," "Specificity."
- **Tali Garsiel & Paul Irish, "How Browsers Work: Behind the scenes of modern web browsers"** (web.dev, free) — a classic overview of the pipeline.
- **Pavel Panchekha & Chris Harrelson, *Web Browser Engineering*** (browser.engineering, free) — a full book that builds a browser in Python. Use it only as a *second explanation after* you've built a milestone your own way; Glimpse's design and order are deliberately different.
- **Let's build a browser engine!** (Matt Brubeck's blog series, Rust) — a short, clear series on layout ideas.

## Tools
- **Firefox Developer Tools** — the inspector shows the DOM a real browser built, computed styles, and the box model for any element: your oracle for "what should this look like?"
- **html5lib** (Python, test-only witness) — a spec-compliant HTML parser.

## Video course

*Companions, not replacements: your labs and projects are the course. Watch with the [V protocol](../study-protocols.md#v--watch-actively) (pause, predict, then blank-sheet [R]), take lectures and quizzes as second explanations, and build this module's own projects, not the course's assignments. How courses fit your sessions: [study-protocols § Using video courses](../study-protocols.md#using-video-courses).*

**Primary — Chrome University**, Chrome for Developers (talks by Chrome engineers). Free on YouTube: [playlist](https://www.youtube.com/playlist?list=PLNYkxOF6rcICgS7eFJrGDhMBwWtdTgzpx).
- **Why it fits:** no university publishes a free lecture course on building a browser engine. *Web Browser Engineering*, the book this module follows most closely, has recorded lectures, but they are only available to instructors on request. These talks are the best free videos on how a real engine works inside, especially "Life of a pixel", which walks from HTML through DOM, style, layout and paint to display lists: the same pipeline as Glimpse's milestones. Watch the selected talks below, not the whole series (much of it is Chrome-specific).

**Alternate — CS50's Web Programming with Python and JavaScript (CS50W)**, Harvard (Brian Yu). Free: [course site with lecture videos](https://cs50.harvard.edu/web/).
- **Why:** the user's side of what Glimpse implements. Lecture 0 (HTML and CSS) shows the document tree, selectors and styling rules your tokenizer, tree builder and cascade must handle. Watch it before Milestone 1 if HTML and CSS are new to you.

### Lecture-to-vault map

Chrome University numbers are playlist positions.

| Vault item | Chrome University (primary) | CS50W (alternate) |
| :-- | :-- | :-- |
| [Lab 01 — Reading a web standard](labs/lab-01-reading-a-web-standard.md) | 1 The history of the web | Lecture 0 HTML and CSS |
| [Lab 02 — Text, Unicode and fonts](labs/lab-02-text-unicode-and-fonts.md) | — (see Gaps) | — |
| [Lab 03 — Drawing surfaces](labs/lab-03-drawing-surfaces.md) | 5 Life of a pixel (paint and display lists) | — |
| [Glimpse](projects/glimpse/spec.md): the big picture | 2 Anatomy of the browser 101 · 3 Anatomy of the browser 201 · 4 Life of a navigation | — |
| Glimpse: HTML tokenizer and tree | 5 Life of a pixel (parsing and the DOM) | Lecture 0 HTML and CSS (HTML and the DOM) |
| Glimpse: CSS cascade and specificity | 5 Life of a pixel (style) | Lecture 0 HTML and CSS (CSS) |
| Glimpse: box model, layout and paint | 5 Life of a pixel (layout, paint) | — |

**Gaps:** nothing here teaches text shaping, Unicode or fonts (Lab 02); use the written pointers above. A newer recording of "Life of a pixel" (BlinkOn) is on [YouTube](https://www.youtube.com/watch?v=K2QHdgAKP-s) if you want a second pass.
