---
title: "10 — Browser Engine"
id: "MOD10"
type: "overview"
module: "10-browser-engine"
phase: "D"
order: 1250
prerequisites: [MOD09, MOD05, MOD02, MOD06-PRJ-ember-compiler, M10, FND-MA-PRJ-floor-plan-and-turtle, E10]
checkpoints: [MOD10-CLOSE]
tags: [module, browser, parsing, layout]
---

# 10 — Browser Engine

**Turn bytes from the network into a page you can read and click.** You'll build **Glimpse**, a document browser for a useful subset of the web: it fetches pages over HTTP (and HTTPS) with your own client, tokenizes and parses HTML into a tree with real-world error recovery, parses a subset of CSS and computes styles with the cascade and inheritance, lays out block and inline boxes with line breaking, and paints the result to three different backends — the terminal, SVG files, and an interactive window with scrolling, links, and history. It also produces an outline and an accessibility tree, and has a reader mode.

Pagelet (Module 01) did fetch → parse → lay out → render for your own tiny markup. Glimpse does it for HTML and CSS, the way real engines are structured.

---

## Prerequisites

- [09 Networking](../09-networking/overview.md) (HTTP, Lantern to serve your test pages).
- [05 DSA](../05-data-structures-and-algorithms/overview.md) (trees, hash maps), [02](../02-programming-fundamentals/overview.md) (parsers), [06 Ember](../06-computer-architecture/projects/ember-compiler/spec.md) (a full front end).
- Math [M10](../00-foundations/math/M10-geometry-and-measurement.md) (coordinates, boxes) — and [Floor Plan and Turtle](../00-foundations/math/projects/floor-plan-and-turtle/spec.md)'s row layout.
- English E10.

## Objectives

By the end you will be able to:
1. Read a large web standard selectively and turn part of it into code.
2. Implement an HTML tokenizer as a state machine and a tree builder with error recovery.
3. Parse CSS, match selectors, compute specificity, and resolve the cascade and inheritance.
4. Implement the CSS box model, block layout, and inline layout with line breaking and mixed styles.
5. Separate layout from painting with a display list, and paint to several backends.
6. Implement navigation: URL resolution, history, link hit-testing, scrolling, and an HTTP cache.
7. Test a rendering engine with golden display lists, layout invariants, and differential parsing.

## Sequence and time

| Order | Item | Concepts |
| :-- | :-- | :-- |
| 1 | [Lab 01 — Reading a Web Standard](labs/lab-01-reading-a-web-standard.md) | three-pass reading of specs; tokenization; the box model; specificity by hand |
| 2 | [Lab 02 — Text, Unicode, and Fonts](labs/lab-02-text-unicode-and-fonts.md) | code points, UTF-8, font metrics, line breaking |
| 3 | [Lab 03 — Drawing Surfaces](labs/lab-03-drawing-surfaces.md) | Tk canvas, SVG, coordinates, display lists, scrolling |
| 4 | **[Glimpse](projects/glimpse/spec.md)** | the whole engine, in eight milestones |

## The engine's pipeline

```
URL ──► fetch (HTTP client, cache) ──► bytes ──► decode (UTF-8) ──► tokenize (FSM) ──► tree builder ──► DOM tree
                                                                                                         │
             user agent stylesheet + <style> + <link> + style="" ──► CSS parser ──► rules ──► cascade ──► styled tree
                                                                                                         │
                                                         layout (block + inline, line breaking) ──► layout tree
                                                                                                         │
                                                                      paint ──► display list ──► terminal / SVG / window
```

Every arrow is a separately testable stage — the parse/render split from Pagelet, grown up.

## How the study methods run through this module

| Protocol | In this module |
| :-- | :-- |
| **R** | Draw the pipeline, the box model, and the tokenizer's main states from memory. Study Deck cards for specificity rules, box-model arithmetic, and inheritance. |
| **F** | Recorded explanations: how `<p>Hello <b>world</b></p>` becomes pixels; why inline layout is harder than block layout. |
| **W** | Each subset decision in the design doc ("why no floats?", "why this error-recovery rule?"), defended. |
| **S** | Subgoal labels for each tokenizer state transition, the cascade, and the line-breaking algorithm. |
| **I** | Parsing, styling, geometry, and networking interleaved. |
| **C** | Copywork from the specs themselves (the WHATWG HTML standard's introductory sections are precise, readable prose). |
| **D** | Layout bugs are visual: render to SVG, compare, sleep on it. |
| **T** | Design doc (grown per milestone), a "supported subset" reference, a test report, and a demo browsing real pages. |

## Video course

- **Primary:** **Chrome University**, selected talks (Chrome for Developers) — [YouTube playlist](https://www.youtube.com/playlist?list=PLNYkxOF6rcICgS7eFJrGDhMBwWtdTgzpx); start with "Life of a pixel".
- **Alternate:** **CS50's Web Programming with Python and JavaScript (CS50W)**, Lecture 0 HTML and CSS (Harvard) — [course site](https://cs50.harvard.edu/web/).
- **Which lectures go with which lab and project:** the map in [resources](<resources.md#lecture-to-vault-map>). Watch with the [V protocol](../study-protocols.md#v--watch-actively) and [use courses as companions](../study-protocols.md#using-video-courses).

---

## Connections

- **Back:** Pagelet (the four stages), Lantern (serves your test corpus), Floor Plan and Turtle (boxes in rows), Worldfile/Ember (parsers), Crosswalk (FSMs), Edit Buffer (text structures), Vault Search (Glimpse can search pages it has visited).
- **Forward:** [13 Capstone](../13-capstone/overview.md) — Glimpse fetching pages over Courier from Lantern, backed by your database.

## Module close

1. **Cumulative retrieval [R]:** the whole pipeline, with one example traced through every stage on paper.
2. **Rewrite [Explain-a-System](../00-foundations/english/projects/explain-a-system/spec.md) explainer 4** a second time, now from the browser's side.
3. **Showcase [T]:** a short demo browsing your vault (served by Lantern as HTML) and two real, simple websites.
4. Tick the module in [Start Here](<../00 - Start Here.md>).

**Resources:** books, docs, and tools for this module are in [resources.md](resources.md) (pointers only — the projects are the course).

**Next:** [11 Databases](../11-databases/overview.md) (if not already done), then [13 Capstone](../13-capstone/overview.md).
