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

## Video and course companions
Free YouTube series and Coursera/edX/MIT OCW courses for this module are listed in [courses-and-videos.md](../courses-and-videos.md#modules-0113). Use them with the [V protocol](../study-protocols.md#v--watch-actively): lectures and quizzes as second explanations; this module's own projects, not the courses' assignments.
