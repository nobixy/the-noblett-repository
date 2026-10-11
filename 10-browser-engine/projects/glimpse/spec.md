---
title: "Project: Glimpse"
id: "MOD10-PRJ-glimpse"
type: "project"
module: "10-browser-engine"
phase: "D"
order: 1290
prerequisites: [MOD10-LAB03, MOD01-PRJ-pagelet, MOD09-PRJ-lantern]
artifact: "Glimpse: a document browser in Python — HTTP/1.1 client with cache, HTML tokenizer and tree builder with error recovery, a CSS subset with cascade and inheritance, block and inline layout, a display list painted to terminal, SVG, and an interactive window, navigation and history, an outline, an accessibility tree, and reader mode"
deliverable: "Design doc (grown per milestone) + SUPPORTED.md (the exact subset) + test report (golden display lists, invariants, differential parsing) + short demo"
---

# Project: Glimpse

| | |
| :-- | :-- |
| **Module** | 10 Browser Engine |
| **Prerequisites** | Labs 01–03 of this module; Pagelet; Lantern (serves your test corpus); Module 05 (trees) |
| **Language** | Python (standard library; `ssl` and `zlib` allowed; `html5lib` allowed **only in tests**, as a second witness) |
| **You build** | **Glimpse**, a browser for documents: articles, documentation, blogs, your own notes. No JavaScript, no floats, no flexbox — but real HTML parsing with error recovery, a real cascade, real block-and-inline layout with mixed fonts, links, history, caching, and three output backends. You'll browse your own vault (as HTML from Lantern) and simple real websites with it |
| **Deliverable** | Growing design doc, a supported-subset reference, a test report, and a demo |

---

## Why this matters

A browser engine is the largest piece of software most people use daily, and its core ideas — parsing untrusted text into trees, cascading rules, laying out boxes, painting from a display list — appear everywhere: document editors, e-book readers, UI toolkits, PDF generators, game UI. Building one, even a document-only one, is a tour of almost everything you've learned: state machines, recursion, trees, hash maps, geometry, networking, caching, and testing.

The scope is chosen on purpose: a **document** browser — the web as it was meant for reading — which is achievable alone, and genuinely useful.

**Real-world analogs:** Gecko, Blink, WebKit; text browsers like Lynx and w3m; e-book renderers; reader modes.

> **Originality:** Glimpse's scope (document-first, three paint backends, outline and accessibility tree, reader mode), architecture, milestones, and test strategy were designed for this curriculum. It is not a chapter-by-chapter reimplementation of any browser-engineering book; if you read one, read it as a second explanation after you've built the matching milestone yourself.

---

## The supported subset (write the exact version in `SUPPORTED.md`)

- **HTML elements:** structure (`html head body title meta link style`), text blocks (`p h1–h6 blockquote pre hr br div section article header footer nav main aside`), lists (`ul ol li dl dt dd`), inline (`a em strong i b code span small sub sup`), `img` (alt text always; images in the stretch goal), `table` as simple blocks (stretch: real tables), unknown elements as inline.
- **CSS:** selectors — type, `.class`, `#id`, `*`, descendant (`a b`), child (`a > b`), grouped (`a, b`); specificity; `!important` (decide); sources — your user-agent stylesheet, `<style>`, `<link rel="stylesheet">`, `style=""` attributes.
- **CSS properties:** `display` (block, inline, list-item, none), `margin`, `padding`, `border-width`, `border-style` (solid), `border-color`, `width`, `max-width`, `color`, `background-color`, `font-size` (px, em, %), `font-weight`, `font-style`, `font-family` (map a few generic families to installed fonts), `line-height`, `text-align` (left, center, right), `text-decoration: underline`, `white-space: pre`, `list-style-type` (disc, decimal, none).
- **Out of scope:** JavaScript, floats, positioning, flexbox, grid, forms (stretch: GET forms), animations.

---

## Milestones

### Milestone 1 — Design doc, test corpus, and the fetcher

1. **Design doc v1** (5 pages): the pipeline diagram, the data structures (DOM node, style, layout box, display item), the subset, testing strategy (golden display lists, invariants, differential parsing), and the milestones.
2. **Test corpus:** 20+ small HTML pages you write, each targeting a feature (headings, nested lists, inline styles, broken markup, long words, `pre`, entities, …). Serve them with Lantern. Also choose 5 real, simple, text-heavy websites to aim for (documentation pages, a plain blog, Wikipedia's mobile pages are surprisingly simple — check what renders).
3. **HTTP client** (upgrade Pagelet's): HTTP/1.1 with `Host`, keep-alive connection reuse per host, `Content-Length` and **chunked** decoding, redirects (≤ 5), `gzip` decoding (`zlib`), HTTPS via `ssl.create_default_context()` (certificate checks on — never turn them off [W]), and `file://` URLs.
4. **Cache:** in memory (and optionally on disk), honouring `Cache-Control: max-age`, `no-store`, and revalidating with `ETag` / `If-None-Match` and `Last-Modified` / `If-Modified-Since` (Lantern answers 304!).

**Done when:** `glimpse fetch URL` prints the decoded body for your corpus, HTTPS sites, a redirect, and a chunked response; cache hits and 304 revalidations are logged.

### Milestone 2 — The HTML tokenizer

A state machine following the HTML Standard's tokenization section for your subset: data, tag open, end tag open, tag name, attribute states (unquoted, single- and double-quoted values), self-closing start tag, markup declaration (comments, `<!DOCTYPE>` simplified), and **character references** (`&amp;`, `&lt;`, `&gt;`, `&quot;`, `&nbsp;`, `&#123;`, `&#x1F600;`, and a small named table). `<script>` and `<style>` contents are raw text until the matching end tag.

Every state transition corresponds to a sentence in the standard; cite the section in a comment [S].

**Tests:** a table of 40+ inputs → expected token lists, including malformed ones (unclosed attributes, `<` in text, `</>`, attributes without values, uppercase tags).

**Checkpoint:** [Milestone Checkpoint](<../../../04 - System/Milestone Checkpoint Template.md>). Retrieval target: draw the tag-and-attribute part of the state machine from memory.

### Milestone 3 — The tree builder

Turn tokens into a **DOM tree** (nodes: element with tag and attributes, text, comment) with the standard's main error-recovery behaviours for your subset:
- implied `html`, `head`, `body`;
- elements that belong in `head` (`title`, `meta`, `link`, `style`) placed there;
- **void elements** (`br`, `hr`, `img`, `meta`, `link`) never have children;
- auto-closing: a new `<p>` closes an open `p`; `<li>` closes an open `li`; block elements close an open `p`; `</p>` without an open `p` inserts an empty one (yes, browsers do that);
- mismatched end tags: close up to the matching open element if it's in scope, else ignore;
- text in `pre` preserved; whitespace-only text between blocks handled consistently (decide where to collapse — tokenizer, tree builder, or layout [W]).

**Differential testing:** parse every corpus page with your parser and with `html5lib` (test only), serialise both trees to a simple text form, and compare. Differences must be either fixed or listed in `SUPPORTED.md` as known deviations.

**Done when:** your corpus parses identically to html5lib except for documented deviations.

### Milestone 4 — CSS: parsing, matching, cascade, inheritance

1. **CSS tokenizer and parser** for your subset: rules, selector lists, declarations, comments; skip unknown at-rules and unknown properties gracefully (browsers ignore what they don't understand — [W] why is that essential for the web to evolve?).
2. **Selector matching** against DOM nodes (right-to-left matching for descendant selectors: start from the element and walk up — [W] why right-to-left?).
3. **Cascade:** for each element and property, the winning declaration by origin (user-agent < author; `style=""` highest among author), specificity, then source order.
4. **Inheritance** for inherited properties; **initial values** for the rest; **computed values** (resolve `em` and `%` font sizes against the parent).
5. **Your user-agent stylesheet** (`ua.css`): sensible defaults for every element (headings sizes, margins, list indentation, `pre` monospace, links blue and underlined). Write it yourself; it's also a nice test of your parser.
6. `glimpse styles URL` prints the DOM with each element's computed styles.

**Tests:** specificity tables (Lab 01), cascade cases, inheritance chains, `em` compounding (nested `font-size: 1.2em`).

### Milestone 5 — Block layout

1. **Layout tree:** a box per element with `display ≠ none`; **anonymous block boxes** wrap inline content that sits next to blocks (look up "anonymous block boxes" in CSS 2.2 §9.2.1.1).
2. **Block layout:** width from the width equation (Lab 01: `auto` widths, `max-width`, centring with auto margins); vertical stacking; height from content; padding and borders. (Vertical margin collapsing is a stretch goal — note it in `SUPPORTED.md`.)
3. **Paint:** backgrounds, borders, and (for now) each text node as one unwrapped line, into the display list; SVG backend.

**Layout invariants** (checked in tests on every corpus page):
- every child's border box lies within its parent's content box horizontally (for normal flow without overflow);
- block siblings don't overlap vertically and appear in document order;
- every box's width equals the width equation's result.

### Milestone 6 — Inline layout

The heart of the engine (Lab 02 Session 3, made general):
1. Walk inline content (text and inline elements, nested) **as a sequence of styled word pieces**; measure each with Tk font metrics for its computed font.
2. **Line breaking:** greedy, breaking at spaces; a word longer than the line goes on its own line (or is broken — decide); `<br>` forces a break; `white-space: pre` keeps line breaks and spaces and never wraps.
3. **Line boxes:** each line's height fits its tallest piece; pieces share a **baseline**; `line-height` sets the minimum spacing.
4. `text-align` per line; `text-decoration: underline` as a line under each piece; list markers (bullets, numbers) placed in the margin.
5. Inline element **borders and backgrounds** spanning several lines (stretch: they're tricky — note if skipped).

**Golden display lists:** for each corpus page at width 600 px, a text dump of the display list, reviewed by eye once, then committed (Module 02 golden-file rules). Any change shows up as a diff you review.

**Checkpoint:** Milestone Checkpoint. Feynman target: *how `<p>Hello <b>big</b> world</p>` becomes positioned words on two lines at a narrow width*.

### Milestone 7 — The browser

1. **Window backend** (Tk): paints the display list; scrolling with culling (Lab 03); **re-layout on resize**.
2. **Links:** hit-testing maps a click to the innermost `<a>` (keep a back-pointer from display items to layout boxes to DOM nodes); resolve `href` against the base URL; navigate.
3. **History** (Pagelet's two stacks), **address bar**, **reload** (bypassing the cache), **status line** (URL under the mouse).
4. **Fragment links** (`#section`): scroll to the element with that id.
5. **Terminal backend** for `glimpse --text URL` (great for SSH and for quick checks).

**Done when:** you can browse your corpus and your 5 target real sites by clicking, going back and forward, and resizing.

### Milestone 8 — Outline, accessibility tree, reader mode, and performance

1. **Outline:** a sidebar (or `--outline` text output) of the page's headings, clickable.
2. **Accessibility tree dump:** `glimpse --a11y URL` prints a tree of roles and names (headings with levels, links with their text, lists with item counts, images with alt text, landmarks like `nav` and `main`) — the structure a screen reader would use. Check your corpus pages: are headings in order? Do images have alt text? (Report problems like a linter.)
3. **Reader mode:** a toggle that re-renders `main` or `article` content (or the largest text block — choose a heuristic and justify it) with a clean reading stylesheet (comfortable `max-width`, larger type, high contrast).
4. **Performance:** time each pipeline stage for a large page (e.g. a long documentation page or a 5,000-paragraph generated one). Find the slowest stage with `cProfile` and speed it up (caching font measurements is often the big win). Report before and after.

---

## Testing guidance

- **Stage by stage:** tokenizer tables, tree comparisons with html5lib, cascade cases, layout invariants, golden display lists, and end-to-end navigation scripts.
- **Visual check:** keep a page `corpus/index.html` that links every test page; browse them all after any change, side by side with Firefox (expect differences; document the important ones).
- **Fuzz** the tokenizer and tree builder with random and mutated HTML: no crashes, always a tree.

## Common pitfalls

- **Whitespace handling** — the classic source of extra or missing spaces. Decide one place where collapsing happens.
- **Mixing layout and paint** — keep layout pure (boxes and positions) and paint separate (display list).
- **Re-measuring the same words** thousands of times — cache by (word, font).
- **Absolute vs relative coordinates** confusion — compute absolute positions in one pass and say so in the design doc.
- **Scope creep** — floats and tables are tempting rabbit holes. Finish the core first.

## Communication deliverable

1. **Design doc** — one section per milestone, with diagrams of each stage and every subset decision justified.
2. **`SUPPORTED.md`** — the exact subset (elements, selectors, properties), known deviations from real browsers, and the reason for each.
3. **Test report** (2–3 pages): tokenizer tables, html5lib agreement, invariants, golden lists, fuzzing, and performance before/after.
4. **Demo:** browse your vault (served as HTML by Lantern), a real documentation site, reader mode, the accessibility dump, and a resize reflowing text.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Before each milestone: the relevant stage drawn from memory (states, cascade order, width equation, line box) |
| **F** | Bytes → pixels for one paragraph; why inline layout is hard |
| **W** | Certificate checks; whitespace decisions; ignoring unknown CSS; right-to-left matching; reader-mode heuristic |
| **S** | Spec sections cited per state and rule |
| **C** | Copywork from the HTML Standard's introduction and CSS 2.2's box-model chapter |
| **D** | Visual bugs: render to SVG, compare, write a stuck note |
| **T** | Design doc, subset reference, test report, demo |

## Stretch goals

- **Images:** decode PNG yourself (it's zlib-compressed scanlines with filters — a satisfying parser) or with Pillow, and lay out `img` as inline replaced boxes with `width`/`height`.
- **Vertical margin collapsing** and **simple tables**.
- **GET forms** (text inputs and a submit button) — enough to use a search page.
- **Search inside pages** with Vault Search's index over your browsing history.
- **Print to PDF-like pages:** paginate the display list into fixed-height pages (SVG per page).

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Networking | Keep-alive, chunked, gzip, HTTPS with verification, redirects, cache with revalidation | Basics | HTTP/1.0 only |
| HTML parsing | Spec-cited tokenizer; tree builder matches html5lib on corpus (deviations documented); fuzzed | Mostly | Fragile |
| CSS | Parser, matching, cascade, inheritance, computed values, own UA sheet | Most | Partial |
| Layout | Block + inline with mixed styles, baselines, alignment, lists, pre; invariants hold | Block only | Broken |
| Browser | Window, scrolling, links, history, fragments, resize, terminal mode | Most | Static |
| Extras | Outline, a11y dump, reader mode, profiling with speed-up | Two | One |
| Communication | Doc, SUPPORTED.md, test report, demo | Most | Few |

**Done when:** every area at least 2; HTML parsing and Layout at 3.

## Connections

- **Back:** Pagelet (the first browser you built), Lantern (your server), Floor Plan and Turtle (rows of boxes), Edit Buffer and Lab 02 (text), Worldfile/Truth Engine/Ember (parsers), Crosswalk (FSMs), Vault Search (caching ideas, search).
- **Forward:** [13 Capstone](../../../13-capstone/overview.md) — Glimpse as the front end of your own stack.
