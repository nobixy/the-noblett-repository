---
title: "Lab 02 — Text, Unicode, and Fonts"
id: "MOD10-LAB02"
type: "lab"
module: "10-browser-engine"
phase: "D"
order: 1270
prerequisites: [MOD10-LAB01]
---

# Lab 02 — Text, Unicode, and Fonts

**Goal:** understand text the way a rendering engine must: characters vs bytes, UTF-8 encoding by hand, what a font's metrics are, and how to measure and break lines of proportional text.

**Sessions:** three.

---

## Session 1 — Unicode and UTF-8

- **Unicode** assigns every character a number, its **code point**: `A` = U+0041, `é` = U+00E9, `€` = U+20AC, `😀` = U+1F600.
- **UTF-8** encodes code points as 1 to 4 bytes:

| Code point range | Bytes | Pattern |
| :-- | :-- | :-- |
| U+0000–U+007F | 1 | `0xxxxxxx` (ASCII is unchanged) |
| U+0080–U+07FF | 2 | `110xxxxx 10xxxxxx` |
| U+0800–U+FFFF | 3 | `1110xxxx 10xxxxxx 10xxxxxx` |
| U+10000–U+10FFFF | 4 | `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx` |

**Exercises (by hand, then check with Python's `"€".encode("utf-8").hex()`):**
1. Encode `é` (U+00E9) and `€` (U+20AC) in UTF-8 (M01 binary skills!).
2. Decode the bytes `e2 82 ac` and `f0 9f 98 80`.
3. Write `utf8_decode(data: bytes) -> list[int]` yourself, with errors for invalid sequences (a continuation byte without a lead byte; a truncated sequence; an "overlong" encoding). Test against Python's decoder on random valid strings and on fuzzed bytes (Python's `errors="strict"` must agree on what's invalid).

**[W]:** why is UTF-8 designed so ASCII bytes never appear inside a multi-byte character? (Think about a parser looking for `<` in a page.)

**Beyond code points:** what users see as one character can be several code points (`é` can also be `e` + U+0301 combining accent; flags and some emoji are sequences). Look up "grapheme cluster." Glimpse will treat code points as characters — note this as a known limitation.

---

## Session 2 — Font metrics

A font gives each character (glyph) an **advance width** (how far to move after drawing it), and the font has an **ascent** (height above the baseline) and **descent** (below). Line height is usually ascent + descent + some gap.

Using Tkinter (it's in Python's standard library; Lab 00's `tk` package):

```python
import tkinter as tk, tkinter.font as tkfont
root = tk.Tk()
f = tkfont.Font(family="DejaVu Sans", size=16)   # use a font you have: tkfont.families()
print(f.measure("Hello"), f.metrics())            # width in pixels; ascent, descent, linespace
```

1. Measure "iiiii" vs "WWWWW" vs "Hello world" in a proportional font and in a monospace font.
2. Is `measure("ab") == measure("a") + measure("b")`? Try "AV" and "To" (kerning — many systems apply it). Glimpse will measure whole words, which handles this.
3. Measure the same word at sizes 8–48. Is width proportional to size?

---

## Session 3 — Lines by hand, on a canvas

Draw a paragraph on a Tk `Canvas`, wrapped to a width of 400 px, in a proportional font:
1. Split into words; measure each word and the width of a space.
2. Greedy line breaking (Pagelet's algorithm, now with pixel widths): add words while they fit; then start a new line.
3. Each line's **baseline** y = previous baseline + line height; draw each word at (x, baseline − ascent) with `create_text(..., anchor="nw")`.
4. Now mix styles: one bold word and one larger word in the middle of the paragraph. Each line's height must fit its **tallest** word, and words should share a **baseline** (align them by ascent). Get it right on paper first [S].

This is exactly the core of Glimpse's inline layout.

---

## Done when

- [ ] UTF-8 exercises and your decoder (tested and fuzzed).
- [ ] Metrics measurements recorded.
- [ ] A wrapped mixed-style paragraph drawn correctly on a canvas.

## Retrieval and reflection

1. **[R]:** the UTF-8 table; code point vs byte vs grapheme; ascent, descent, advance; baseline alignment.
2. **[F] (spoken):** "Why can't a browser just count characters to know how wide a line is?"
