---
title: "Lab 01 — Reading a Web Standard"
module: "10-browser-engine"
hours: 8
---

# Lab 01 — Reading a Web Standard

**Goal:** learn to read huge technical standards *selectively* — the WHATWG HTML Standard and the CSS specifications — and turn what you read into precise, testable understanding: tokenizing by hand, computing specificity, and doing box-model arithmetic.

**Time:** about 8 hours, in three sessions.

---

## Session 1 — How to read a standard (2 hours)

The HTML Standard (html.spec.whatwg.org) is thousands of pages. Nobody reads it front to back. Engineers use it like a map: find the section you need, read it closely, and test your understanding.

**Use the three-pass method** ([LM13](<../../02 - Atlas/LM13 - Three-Pass Paper Reading.md>)), adapted:
1. **Pass 1 (15 min):** read the table of contents and section introductions for "Parsing HTML documents" (section 13.2). Write, in 5 sentences, what the parsing process consists of.
2. **Pass 2 (45 min):** read "Tokenization" (13.2.5) — the overview and the first ten states (data state, tag open, end tag open, tag name, before attribute name, attribute name, after attribute name, before attribute value, attribute value (double-quoted), and the comment states). Note how each state says exactly what to do with each next character.
3. **Pass 3 (only for what you'll implement):** later, during Glimpse Milestone 2.

**[W]:** why does the standard describe parsing as a state machine with explicit error-recovery for every malformed input, instead of saying "invalid HTML is an error"? (Hint: what did browsers do with the broken HTML of the 1990s web, and what would happen to old pages if a new browser refused them?)

---

## Session 2 — Tokenize and tree-build by hand (3 hours)

Using the states you read, tokenize these by hand into a list of tokens (start tag with attributes, end tag, character, comment, end-of-file) [S]:

1. `<p class="intro">Hi &amp; welcome</p>`
2. `<a href=page.html title='x y'>Go</a>`
3. `<ul><li>One<li>Two</ul>` (note the missing `</li>`)
4. `<!-- note --><br/>Text`

Then, for #3, build the **tree** the way a browser does: the HTML tree-construction rules close an open `<li>` when a new `<li>` starts. Look up that rule in section 13.2.6 ("The rules for parsing tokens in HTML content" → "in body" insertion mode → "A start tag whose tag name is 'li'"). Read just that rule closely.

Check your answers against a real browser: paste the snippet into a file, open it in Firefox, and use the inspector (F12) to see the tree it built.

---

## Session 3 — CSS by hand (3 hours)

### Specificity

Read CSS Selectors Level 3/4's "Calculating a selector's specificity." Specificity is a triple (ids, classes/attributes/pseudo-classes, type selectors), compared left to right.

Compute and order: `p`, `.note`, `#main`, `div p`, `div.note p`, `#main .note`, `ul li a`, `*`.

Then: given these rules and `<div id="main"><p class="note">Hi</p></div>`, what colour is the text?
```css
p { color: black; }
.note { color: blue; }
div p { color: green; }
#main p { color: red; }
```

<details>
<summary>Answers</summary>

Specificities: `*` (0,0,0) · `p` (0,0,1) · `div p` (0,0,2) · `ul li a` (0,0,3) · `.note` (0,1,0) · `div.note p` (0,1,2) · `#main` (1,0,0) · `#main .note` (1,1,0). The text is **red**: `#main p` is (1,0,1), the highest that matches.
</details>

### The box model

Read CSS 2.2 section 8 ("Box model") and 10.3.3 ("Block-level, non-replaced elements in normal flow") — the width equation:

> margin-left + border-left + padding-left + **width** + padding-right + border-right + margin-right = containing block width

Compute by hand:
1. Container 800 px; a `div` with `margin: 20px; padding: 10px; border: 2px solid;` and `width: auto`. What's its content width?
2. Same, with `width: 500px` and `margin-left: auto; margin-right: auto`. What are the margins? (This is how centring works.)
3. A block with `width: 50%` inside a 600 px container with `padding: 0 30px` on the container. What's the block's width?

<details>
<summary>Answers</summary>

1. 800 − 2×20 − 2×2 − 2×10 = **736 px**. 2. Remaining 800 − 500 − 2×2 − 2×10 = 276 → each margin **138 px**. 3. The containing block is the container's **content** box: 600 − 60 = 540, so 50% = **270 px**.
</details>

**Inheritance:** which properties inherit by default (e.g. `color`, `font-size`) and which don't (e.g. `margin`, `border`)? Find the "Inherited: yes/no" line in each property's definition. Make a flashcard for each property you'll implement.

---

## Done when

- [ ] Pass-1 summary written; the four snippets tokenized and #3 tree-built, checked in a browser.
- [ ] Specificity and box-model exercises done and checked.
- [ ] Inheritance flashcards for Glimpse's properties.

## Retrieval and reflection

1. **[R]:** the tokenizer's main states; specificity rules; the width equation.
2. **[F] (spoken, 2 min):** "Why are browsers so forgiving of broken HTML?"
