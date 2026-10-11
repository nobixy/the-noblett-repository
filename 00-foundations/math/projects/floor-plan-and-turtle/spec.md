---
title: "Project: Floor Plan and Turtle"
id: "FND-MA-PRJ-floor-plan-and-turtle"
type: "project"
module: "00-foundations"
track: "math"
phase: "C"
order: 740
prerequisites: [M09, MOD01-LAB01]
stages: "M10"
artifact: "A measured scale drawing of a room; turtle/SVG programs that draw it from data, draw geometric art, and lay out boxes in rows like a browser"
deliverable: "short demo + half-page explanation of the closure check and the row-layout algorithm"
---

# Project: Floor Plan and Turtle

| | |
| :-- | :-- |
| **You build** | A measured floor plan of a real room (paper), then programs that draw it from a data file and check it closes up, geometric art from angles, and a tiny layout engine that places boxes in rows — the core idea of a browser's layout |
| **Deliverable** | A short demo and a half-page explanation |

---

## Why this matters

You'll measure something real, turn it into numbers, and turn the numbers back into a picture — and you'll check your work with geometry instead of trusting your eyes.

The last milestone is a sneak preview of [Module 10](../../../../10-browser-engine/overview.md): a browser lays out words and images as **boxes in rows**, wrapping to a new line when a row is full. You'll write the simplest version of that algorithm here, with nothing but addition, comparison, and coordinates. When you build your browser engine, this will be familiar.

**Real-world analogs:** CAD and floor-plan software, turtle graphics (a classic way to teach geometry with code), SVG graphics on the web, text layout in browsers and word processors.

---

## Tools

- Tape measure, graph paper, ruler, protractor.
- **Python's built-in `turtle` module** (needs Tk: on Arch, `sudo pacman -S tk`). If it won't run on your setup, write **SVG files** instead: SVG is a simple text format for drawings that any browser opens. A line from (10, 10) to (100, 50) is `<line x1="10" y1="10" x2="100" y2="50" stroke="black"/>`. Milestones 3–4 ask for SVG output anyway, so you'll learn it either way.

---

## Milestones

### Milestone 1 — Measure and draw (paper)

**Do:**
1. Pick a room. Measure every wall, door, and window to the nearest centimetre. Measure both **diagonals** of the floor.
2. **Check the corners:** for a rectangular room, both diagonals should equal √(length² + width²) (M10 Part 5). Compute the expected diagonal and compare with your measurements. Is your room truly rectangular? By how much is it off?
3. Draw the room on graph paper at **1 : 50** (1 cm on paper = 50 cm real). Include doors and windows.
4. Compute: floor area (m²), wall area to paint (walls minus doors and windows), room volume (m³), and how many litres of paint you'd need for two coats (look up a typical coverage, around 10 m² per litre).

**Done when:** drawing done; corner check written up; four computed quantities with units.

**[W]:** If the two diagonals are different lengths, what does that tell you about the room's shape?

### Milestone 2 — Draw it from data, and check it closes

Write the room as a **path**: a list of moves for a turtle that walks around the walls.

```
# room.txt — distance (cm) and the turn (degrees, left) after each wall
412  90
356  90
412  90
356  90
```

Write `plan.py` that:
1. reads the file;
2. draws the path (turtle, or SVG with a scale factor);
3. **computes where the turtle ends up**, using trigonometry: each move of distance d at heading θ changes the position by (d cos θ, d sin θ) (M10 Part 6 — remember to convert degrees to radians);
4. runs a **closure check**: the total turn should be 360°, and the end point should be back at the start. Print the **closure error** (the distance from end to start, by Pythagoras) in cm.

**Then:** enter your *measured* room (not the ideal one) and see how big your closure error is. Real measurements never close perfectly. Is your error bigger than your measuring precision would explain?

**Done when:** a perfect rectangle gives closure error ≈ 0 (floating-point tiny, M06), and your real room's error is reported and explained in one or two sentences.

**Checkpoint:** [Milestone Checkpoint](<../../../../04 - System/Milestone Checkpoint Template.md>). Feynman target: explain why (d cos θ, d sin θ) is the change in position for a move of length d at angle θ. Use the circle picture.

### Milestone 3 — Geometry art (SVG)

Write `art.py` producing SVG files:
1. **Regular polygons:** `polygon(n, side)` using turn = 360° ÷ n. Draw n = 3 to 12 in a row.
2. **Star polygons:** connect every k-th point of n points on a circle (points at (r cos θ, r sin θ)). Try n = 5, k = 2 (a pentagram), n = 7, k = 3, n = 12, k = 5. Which (n, k) pairs draw a single connected star, and which break into separate shapes? (Hint: GCD(n, k) — M04!)
3. **A clock face:** 12 hour marks and 60 minute marks using cos and sin, plus hands showing the current time.
4. One piece of your own design.

**Done when:** four SVG files that open in your browser, and a one-sentence answer to the star question.

### Milestone 4 — Boxes in rows: a tiny layout engine

This is the core of how a browser lays out text and inline images.

**Input:** a container width, and a list of boxes (width × height), like words of different lengths:

```
# boxes.txt  — first line: container width; then one box per line: width height
300
60 20
45 20
120 20
80 30
100 20
40 20
```

**Algorithm (write it as subgoal comments first [S]):**
1. Start at x = 0, y = 0, with an empty current row.
2. For each box: if x + box width (+ a gap of 5) would exceed the container width, **start a new row**: x = 0, y = y + (height of the tallest box in the previous row) + gap.
3. Place the box at (x, y). Move x right by the box width + gap. Remember the row's tallest height.
4. Output every box's position, and draw them (SVG): the container outline, each box as a rectangle with its number inside.

**Then extend:**
- **Alignment:** an option to centre each row, or right-align it (you need to know a row's total width before placing it — what does that change in the algorithm?).
- **Baseline:** in each row, align boxes along their **bottom** edges instead of their tops.

**Tests:** for the example above with width 300, gap 5, top-aligned, write the expected (x, y) of every box **by hand first**, then check the program matches.

**Done when:** the program matches your hand answer; both extensions work; SVG output looks right.

**Checkpoint:** Milestone Checkpoint. Why-ladder target: *why does right-alignment need two passes over each row, while left-alignment needs only one?*

---

## Common pitfalls

- **Degrees vs radians.** `math.cos(90)` is cos of 90 *radians*. Use `math.radians`.
- **Screen y grows downward** (M09, M10). In SVG, y = 0 is the top. Your floor plan will appear upside down unless you flip it. Decide and document.
- **Accumulating heading as floats.** After 1,000 small turns, rounding errors add up. Keep the heading as an integer number of degrees when the input is whole numbers.
- **Off-by-one gaps:** do you put a gap after the last box in a row? Decide, write it down, test it.
- **A box wider than the container:** what should happen? (Browsers let it overflow.) Decide and handle it.

## Communication deliverable

1. **short demo:** show the paper plan, then `plan.py` drawing it and reporting closure error, then the star art, then the layout engine with alignment.
2. **Half-page explanation** (E08–E09 level): how the closure check works, and how the row-layout algorithm decides when to wrap. Include one small diagram.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Write the Pythagoras proof and the circle picture from memory before Milestone 2 |
| **F** | Why (d cos θ, d sin θ) |
| **W** | Unequal diagonals; one pass vs two passes; GCD and stars |
| **S** | Layout algorithm as subgoal comments |
| **T** | Demo and explanation |

## Stretch goals

- **Floor plan with furniture:** add furniture as rectangles and check that nothing overlaps (rectangle intersection: a classic test you'll reuse in graphics and layout).
- **Justify:** stretch the gaps in each row (except the last) so rows exactly fill the width, like justified text.
- **Line breaking with words:** read a paragraph of text, treat each word as a box of width = number of letters × 8, and lay it out. You've just built the start of a text renderer.

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Measuring | Precise; corner check done and interpreted | Measured, no check | Rough |
| Closure | Correct trig; error reported and explained | Draws, no closure check | Missing |
| Art | All four SVGs; star question answered with GCD | Three | Fewer |
| Layout | Matches hand answers; both extensions | Basic rows | Missing |
| Communication | Demo and explanation clear | One | Neither |

**Done when:** every area at least 2; Layout at 3.

## Connections

- **Back:** M04 (GCD in star polygons), M06 (scale, units), M09 (coordinates), M10 (everything).
- **Forward:** Module 10 (block and inline layout), Module 12 (rotation as a matrix), and any graphics work you do later.
