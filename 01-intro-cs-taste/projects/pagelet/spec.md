---
title: "Project 4: Pagelet, a Page Viewer"
id: "MOD01-PRJ-pagelet"
type: "project"
module: "01-intro-cs-taste"
phase: "A"
order: 290
prerequisites: [MOD01-LAB02, M02, E03]
artifact: "pagelet.py: a terminal document viewer with its own markup language, word wrapping, numbered links, history, and a hand-written HTTP client; a 5-page site you wrote"
deliverable: "README + Pagelet markup reference + short demo browsing your own site"
---

# Project 4: Pagelet, a Page Viewer

| | |
| :-- | :-- |
| **Module** | 01 Intro CS Taste |
| **Prerequisites** | Labs 00–02; Math M01–M02; English E03+ (you write a small website) |
| **You build** | A text-mode browser for a small markup language of your own. It fetches pages over HTTP using a request you write by hand, parses the markup into blocks, wraps text to fit the terminal, numbers the links, and lets you follow them and go back. You also write a small website to browse with it |
| **Deliverable** | README, a one-page reference for your markup language, and a demo |

---

## Why this matters

A web browser does four things: it **fetches** a document over the network, **parses** the text into a structure, **lays out** that structure to fit the screen, and **renders** it — then repeats when you click a link. Real browsers are some of the most complex programs ever written. But the four steps are simple at their core, and you can build all four in a handful of build sessions.

That's Pagelet. In [Module 10](../../../10-browser-engine/overview.md), you'll build a real document browser with an HTML-subset parser, a style system, and box layout. You'll recognise every stage, because you'll have built the small, real version first.

You also write the website you browse. That's English practice with a purpose: a reader (you, later) will navigate it.

**Real-world analogs:** text browsers like `lynx` and `w3m`, Markdown renderers, `less`, documentation viewers.

---

## The Pagelet markup language (PML), v1

Files end in `.pml`. A page is a list of **blocks**, separated by blank lines or recognised by their first characters:

| You write | Block | Rendered as |
| :-- | :-- | :-- |
| `= Title` | heading level 1 | UPPERCASE, underlined with `=` |
| `== Section` | heading level 2 | as written, underlined with `-` |
| ordinary lines | paragraph (consecutive lines join into one) | wrapped to the screen width |
| `- item` | list item (consecutive items form one list) | `•` with a hanging indent when wrapped |
| `> text` | quote | indented by 4 with `│ ` in front, wrapped |
| a line with only ` ```
= Nib Notes

My tiny computer has {16 instructions|isa.pml} and 256 bytes of memory.
This page explains how I tested it.

== What I learned
- The PC moves before the instruction runs.
- {Pointers|pointers.pml} are just addresses stored in memory.

> Write the trace on paper first.
``` ` | preformatted block | shown exactly, never wrapped (long lines cut with `→`) |

**Inline links**, anywhere in a paragraph, list item, or quote: `{label|target}`.
- `{the next page|next.pml}` renders as `the next page[3]` if it's the third link on the page.
- Targets can be a relative path (`next.pml`, `../index.pml`) or a full URL (`http://localhost:8000/about.pml`).
- A literal `{` is written `{{`.

Example page:

```
= Nib Notes

My tiny computer has {16 instructions|isa.pml} and 256 bytes of memory.
This page explains how I tested it.

== What I learned
- The PC moves before the instruction runs.
- {Pointers|pointers.pml} are just addresses stored in memory.

> Write the trace on paper first.
```

You may extend PML (for example `*emphasis*`), but **document every extension** in your reference page and explain why you added it.

---

## Milestones

### Milestone 1 — Parse and render a local file

**Build** `pagelet.py` with two clearly separated stages:

1. **`parse(text) -> list of blocks`.** Each block is a small dictionary, e.g. `{"kind": "para", "text": "My tiny computer has {16 instructions|isa.pml} …"}` or `{"kind": "heading", "level": 2, "text": "What I learned"}`. Don't think about the screen at all in this stage.
2. **`render(blocks, width) -> list of lines`.** Turn blocks into the exact lines to print, wrapping to `width` (default: your terminal width from `shutil.get_terminal_size()`, capped at 80).

**Word wrapping** — the core layout algorithm (it's the same idea as the boxes-in-rows engine in [Floor Plan and Turtle](../../../00-foundations/math/projects/floor-plan-and-turtle/spec.md)):

```python
# 1. Split the text into words
# 2. Start an empty line
# 3. For each word: if adding it (plus a space) would exceed the width, finish the line and start a new one
# 4. Add the word to the current line
# 5. Finish the last line
# (A single word longer than the width goes on its own line, cut with a hyphen — decide and document.)
```

For now, render links as their label only.

`python3 pagelet.py page.pml` prints the page.

**Tests:**
- `parse` gives the right block kinds for the example page.
- After `render`, **no line is longer than `width`**, for widths 20, 40, 60, 80, on a page with long paragraphs. (Write this as a loop over widths.)
- Rendering keeps **every word, in order** (join the wrapped lines back into words and compare).
- Preformatted blocks are unchanged.

**Done when:** the example page renders correctly at four widths and all tests pass.

**Checkpoint:** [Milestone Checkpoint](<../../../04 - System/Milestone Checkpoint Template.md>). Why-ladder target: *why keep parsing and rendering as separate stages?* (Think: what if you later want to render the same page to HTML, or to a narrower screen?)

### Milestone 2 — Links, navigation, and history

**Build:**
- Number every link on the page in order: render as `label[n]`.
- After printing a page, show a prompt: `pagelet [page.pml] > `.
- Commands:
  - a number → follow that link
  - `b` → back; `f` → forward
  - `l` → list all links with their targets
  - `g <target>` → go to a path or URL
  - `r` → reload; `q` → quit
- **History with two stacks:** going to a new page pushes the current page onto the *back* stack and clears the *forward* stack; `b` pops from back and pushes onto forward; `f` does the reverse. (This is exactly how real browser history works.)
- **Relative targets** are resolved against the current page's location: from `notes/nib.pml`, the target `isa.pml` means `notes/isa.pml`, and `../index.pml` means `index.pml`. Use `urllib.parse.urljoin` (it works for file paths written as `file:///…` URLs too) — and test it.
- Long pages: if the page has more lines than the terminal, show one screenful at a time (Enter for more).

**Tests:** the history stacks (a sequence of go/back/forward operations gives the expected current page); relative resolution (five cases including `../`).

**Done when:** you can browse a folder of linked `.pml` files, go back and forward, and every test passes.

### Milestone 3 — Fetch over HTTP, by hand

Now pages come from a web server. Serve a folder of `.pml` files with Python's built-in server:

```bash
cd ~/workbench/01-pagelet/site
python3 -m http.server 8000
```

**Build an HTTP client with a raw socket** — no `urllib.request`, no `requests`. You'll write the request text yourself:

```python
request = (
    f"GET {path} HTTP/1.0\r\n"
    f"Host: {host}\r\n"
    f"User-Agent: Pagelet/0.1\r\n"
    f"\r\n"
)
```

**Subgoal labels [S]:**
```python
# 1. Split the URL into host, port (default 80), and path (urllib.parse.urlsplit is fine)
# 2. Open a TCP socket to (host, port); send the request bytes
# 3. Read until the server closes the connection (HTTP/1.0 closes after one response)
# 4. Split headers from body at the first b"\r\n\r\n"
# 5. Parse the status line ("HTTP/1.0 200 OK") into version, code, reason
# 6. Parse header lines into a dictionary (lowercase the names)
# 7. Handle the code: 200 → the body is the page; 301/302 → follow the Location header (at most 5 times);
#    404 and others → show a friendly error page made in PML
# 8. Decode the body as UTF-8
```

**Experiment:** run `nc -l 8001` (netcat listening), then point Pagelet at `http://localhost:8001/hello.pml`. Netcat shows you the exact request bytes Pagelet sent. Then type a response by hand into netcat:

```
HTTP/1.0 200 OK
Content-Type: text/plain

= Hello from netcat
```

and press `Ctrl+D`. Pagelet should render it. You just played the part of a web server.

**Tests:** the response parser on canned byte strings (a 200, a 404, a 301 with `Location`, headers with mixed case, a body containing `\r\n\r\n` inside it — only the *first* one separates headers from body).

**Done when:** Pagelet browses your site over HTTP, follows a redirect, shows a friendly 404, and the netcat experiment worked.

**Checkpoint:** Milestone Checkpoint. Feynman target: *what happens between "type an address" and "see the page"*, using your own code as the map. (Compare with your [Explain-a-System](../../../00-foundations/english/projects/explain-a-system/spec.md) explainer 4 if you've written it.)

### Milestone 4 — Write the site

Write a small website in PML: **at least 5 pages**, linked to each other, about your learning so far. Suggested pages:
- `index.pml` — what this site is, with links to everything
- one page per Module 01 project: what it does, one thing you learned, one picture in a preformatted block (ASCII diagram)
- `methods.pml` — which study method helps you most and why

**Writing rules:** your current English stage applies. Short, correct sentences. Run the spell checker on the finished pages and log every caught word. Every page links back to `index.pml`.

**Done when:** 5+ pages, all links work (write a tiny **link checker**: fetch every page, follow every link, report any 404 — a useful tool and a good test).

---

## Common pitfalls

- **`\n` vs `\r\n`:** HTTP uses `\r\n` line endings. Your request must too; parse headers by splitting on `\r\n`.
- **Reading only once:** `recv` can return part of the response. Loop until it returns `b""`.
- **Decoding before splitting:** split bytes at `b"\r\n\r\n"` first, then decode. Headers are ASCII; the body might not be.
- **Links inside preformatted blocks:** they should *not* become links. Decide and test.
- **Width off-by-one:** a line of exactly `width` characters is allowed; `width + 1` isn't. Test the boundary.
- **Unclosed `{`:** a page with `{broken` must not crash Pagelet. Render it as plain text and maybe warn.

## Communication deliverable

Sized for E03–E06:
1. **README.md:** how to run Pagelet (local files and HTTP), all the commands, and how to run the tests.
2. **`PML.md`:** the markup reference: every block kind and the link syntax, each with an example. (This is your first *language specification*. Precise and complete beats long.)
3. **Demo:** browse your own site over HTTP: follow links, go back and forward, hit a 404, show the netcat experiment.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Before Milestone 3, write the HTTP request format and the response parsing steps from memory |
| **F** | Address → page, end to end |
| **W** | Separate parse and render; two stacks for history; first `\r\n\r\n` only |
| **S** | Word-wrap and HTTP subgoal comments |
| **I** | Parsing, layout, and networking interleaved across milestones |
| **C** | Your site's pages are writing practice; copywork passages during this project can come from good documentation pages |
| **T** | README, `PML.md`, demo, and the site itself |

## Stretch goals

- **Emphasis:** `*word*` rendered in bold with ANSI codes (`\x1b[1m … \x1b[0m`). Careful: escape codes have zero display width, so wrapping must not count them.
- **Justified text:** spread the spaces so every line except the last is exactly `width` characters.
- **A cache:** keep fetched pages in a dictionary; `r` forces a refetch. Show `(cached)` in the prompt.
- **HTML-lite:** treat `<h1>`, `<p>`, and `<a href>` in `.html` files as their PML equivalents. You've started Module 10.
- **Search:** `/word` highlights matches on the current page.

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Parse/render | Separate stages; all block kinds; width and word-order tests | Works, few tests | Mixed together, buggy wrap |
| Navigation | Links, two-stack history, relative resolution, paging, tested | Links and back | Missing |
| HTTP | Raw-socket client; 200/301/404; parser tests; netcat experiment | 200 only | Uses a library |
| Site | 5+ pages, link checker passes, clean writing | 5 pages | Fewer |
| Communication | README, PML.md, demo all clear | Two | One or none |

**Done when:** every area at least 2; Parse/render and HTTP at 3.

## Connections

- **Back:** [Lab 01](../../labs/lab-01-python-first-steps.md) (strings, lists, dicts, files), Relay (sockets, buffering), Floor Plan and Turtle (boxes in rows).
- **Forward:** [10 Browser Engine](../../../10-browser-engine/overview.md) — **Glimpse**, a real document browser: a tokenizer and tree-builder for an HTML subset, a small style system, block and inline box layout, and a rendered window. [09](../../../09-networking/overview.md) — **Lantern**, the HTTP server on the other side of the wire.

> **Originality note:** the PML markup language, Pagelet's design, and these milestones were written for this curriculum. They're intentionally different from existing small-browser books and protocols.
