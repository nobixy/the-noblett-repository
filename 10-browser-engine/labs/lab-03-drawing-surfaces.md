---
title: "Lab 03 — Drawing Surfaces"
id: "MOD10-LAB03"
type: "lab"
module: "10-browser-engine"
phase: "D"
order: 1280
prerequisites: [MOD10-LAB02]
---

# Lab 03 — Drawing Surfaces

**Goal:** separate *what to draw* from *where it's drawn*, with a **display list** that three backends can paint: the terminal, an SVG file, and an interactive Tk window with scrolling.

**Sessions:** two.

---

## Session 1 — The display list

A **display list** is a flat list of simple drawing commands with absolute coordinates, produced by layout and consumed by painting:

```python
DrawRect(x=10, y=10, w=300, h=40, fill="#eef")
DrawText(x=20, y=18, text="Hello", font=("DejaVu Sans", 16, "bold"), color="#000")
DrawLine(x1=10, y1=50, x2=310, y2=50, color="#888", width=1)
```

Why a display list instead of drawing straight from the layout tree? [W]
- **Testing:** a display list printed as text is easy to compare against a golden file.
- **Several backends** from one layout.
- **Scrolling:** paint the same list with a vertical offset, skipping commands outside the visible area.

**Build `display.py`** with these command types (dataclasses) and three painters:
1. **SVG painter:** write an SVG file (`<rect>`, `<text>`, `<line>`; Floor Plan and Turtle taught you SVG). Open it in Firefox.
2. **Tk painter:** draw on a `Canvas`.
3. **Terminal painter:** map pixels to a character grid (e.g. 8 px per column, 16 px per row); draw text at the nearest cell; ignore rectangles or draw borders with box characters. Crude, but great for quick checks over SSH.

Test: a hand-made display list (a heading, two paragraphs, a coloured box) looks the same in SVG and Tk.

---

## Session 2 — Scrolling and hit-testing

1. **Scrolling:** a Tk window that paints a long display list with a `scroll_y` offset; mouse wheel and arrow keys change it; only commands intersecting the visible area are drawn (rectangle intersection — Floor Plan and Turtle stretch goal!). Measure painting time for a 10,000-command list with and without culling.
2. **Hit-testing:** on a mouse click at (x, y + scroll_y), find which display item contains the point (and later, which *link*). Return it and print it.
3. **Resizing:** when the window width changes, the display list must be rebuilt by layout (in Glimpse); for now, print the new width.

---

## Done when

- [ ] One display list painted identically by SVG and Tk, and readably by the terminal painter.
- [ ] Scrolling with culling (timing measured) and click hit-testing.

## Retrieval and reflection

1. **[R]:** why display lists; the three painters; culling; hit-testing.
2. **[W]:** what would change if the display list used coordinates relative to each parent instead of absolute ones?
