---
title: "M10 — Geometry and Measurement"
id: "M10"
type: "lesson"
module: "00-foundations"
track: "math"
stage: "M10"
phase: "C"
order: 720
prerequisites: [M09]
---

# M10 — Geometry and Measurement

**In this stage you will:** measure and compute perimeter, area, and volume (and see why the formulas are true); work with angles and know why a triangle's angles add to 180°; prove and use the Pythagorean theorem; use similar shapes and scale drawings; meet trigonometry (sine and cosine) as the coordinates of a point on a circle; and move, scale, and rotate points on a grid — the basis of all computer graphics.

**Before you start:** M09 done. You're comfortable with coordinates and square roots (M07).

**Tools:** a ruler, a tape measure, a protractor (cheap, or a free phone app), graph paper. Calculator allowed for π, square roots, and trig.

---

## Diagnostic (cold)

1. Area and perimeter of a 7 × 4 rectangle.
2. Area of a triangle with base 10 and height 6.
3. Circumference and area of a circle with radius 5.
4. Volume of a 3 × 4 × 5 box.
5. Two angles of a triangle are 50° and 60°. What is the third?
6. A right triangle has legs 6 and 8. How long is the hypotenuse?
7. Distance between (1, 2) and (4, 6).
8. What do the interior angles of a hexagon add up to?
9. On a map with scale 1 : 50,000, two towns are 3 cm apart. How far apart are they really?
10. A right triangle has a 30° angle and a hypotenuse of 10. How long is the side opposite the 30° angle?

<details>
<summary>Answers (diagnostic)</summary>

1. 28; 22 · 2. 30 · 3. 10π ≈ 31.4; 25π ≈ 78.5 · 4. 60 · 5. 70° · 6. 10 · 7. 5 · 8. 720° · 9. 150,000 cm = 1.5 km · 10. 5
</details>

---

## Why this matters

Your browser engine (Module 10) is, at its heart, a geometry engine: every word, image, and box on a page is a rectangle with a position, a width, and a height, and **layout** is the job of computing those numbers. Every game, every map, every user interface does geometry. Circuit boards (Module 04) are drawn to scale. Signals (Module 12) are built from sine waves, which come straight out of Part 6 here.

And geometry is where proof was invented. Several of the "why" boxes in this stage are complete, short proofs — like Pythagoras, which you'll be able to prove with a drawing.

---

## Part 1 — Units and measuring

**Length:** mm, cm, m, km (metric — use this for engineering); inches, feet, miles (imperial; 1 inch = 2.54 cm exactly).
**Area** is measured in **square** units (cm², m²): how many 1×1 squares cover the shape.
**Volume** is measured in **cubic** units (cm³, m³): how many 1×1×1 cubes fill it. (1 litre = 1,000 cm³.)

**Converting area and volume units — the trap:** 1 m = 100 cm, but 1 m² = 100 × 100 = **10,000 cm²**, and 1 m³ = **1,000,000 cm³**. A square metre is a square 100 cm on each side. Use the conversion-factor method from M06, applied twice (area) or three times (volume).

**Measurement is never exact.** A ruler marked in mm gives readings to the nearest mm. Report measurements with the precision you actually have ("2.35 m", not "2.3517 m" from a tape measure).

---

## Part 2 — Perimeter and area

**Perimeter** = the distance around. Add up the sides.

| Shape | Area | Why |
| :-- | :-- | :-- |
| Rectangle | length × width | rows of unit squares (M03's area model) |
| Parallelogram | base × height | cut the slanted end off and move it to the other side: it becomes a rectangle |
| Triangle | ½ × base × height | two copies of any triangle make a parallelogram |
| Circle | πr² | see below |

**Height** always means the **perpendicular** height (straight up, at a right angle to the base), not the slanted side.

### Circles and π

- **Radius** r: centre to edge. **Diameter** d = 2r.
- **Circumference** (perimeter) C = πd = 2πr.
- **π** (pi) ≈ 3.14159 is the ratio of *any* circle's circumference to its diameter. It's the same for every circle, which is remarkable. Measure it yourself: wrap a string around a round can, measure the string, divide by the can's diameter. You'll get about 3.1.
- **Area** A = πr². *Why:* cut a circle into many thin pizza slices and lay them alternately point-up and point-down. They form a shape close to a rectangle with height r and width half the circumference (πr). Area ≈ r × πr = πr². The thinner the slices, the closer it gets. (This "cut into tiny pieces" idea is the core of calculus, Module 12.)

### Composite shapes

Split into rectangles, triangles, and circles; add the areas (or subtract cut-outs).
> An L-shaped room: a 10 × 8 rectangle with a 4 × 3 corner cut out: 80 − 12 = **68**.

---

## Part 3 — Volume and scaling

| Solid | Volume |
| :-- | :-- |
| Box (rectangular prism) | length × width × height |
| Cylinder | πr² × h (area of the circle × height) |
| Any prism (same shape all the way up) | area of base × height |

**Surface area** of a box: add the areas of its 6 faces: 2(lw + lh + wh).

### The scaling law

Double the side of a cube from 2 to 4:
- length: ×2
- area of a face: 4 → 16, **×4** (= 2²)
- volume: 8 → 64, **×8** (= 2³)

**Scale lengths by k → areas scale by k², volumes by k³.** *Why:* area has two length directions, each scaled by k; volume has three.

This has real consequences: a chip shrunk to half the size in each direction has ¼ the area, so 4× as many fit on a wafer. A model scaled ×10 needs 1,000× the material.

---

## Part 4 — Angles

An **angle** measures a turn. A full turn is **360°**. (Why 360? An ancient choice — the Babylonians used base 60, and 360 has lots of factors: 2, 3, 4, 5, 6, 8, 9, 10, 12, … Mathematicians later also use **radians**, where a full turn is 2π — see Part 6.)

| Angle | Size |
| :-- | :-- |
| right angle | 90° (a quarter turn) |
| straight angle | 180° (a half turn) |
| acute | less than 90° |
| obtuse | between 90° and 180° |

**Angle facts:**
- Angles on a straight line add to **180°**.
- Angles around a point add to **360°**.
- When two lines cross, opposite angles are equal.

### Triangles add to 180°

> **[W] Why do a triangle's angles always add to 180°?**
> 1. Tear the three corners off a paper triangle and put them point to point. They always make a straight line: 180°. (Try it.)
> 2. The proof: draw a line through the top corner, parallel to the bottom side. The two angles at the bottom reappear at the top (angles made by a line crossing two parallel lines are equal). Now the three angles sit side by side along the straight line: 180°.

### Polygons and the turtle walk

Walk around any shape that doesn't cross itself (a **polygon**). At each corner you turn by the **exterior angle**. When you get back to the start, facing the same way, you've turned exactly **one full turn: 360°**.

- So for a regular polygon with n sides, each **turn** is 360° ÷ n. Square: 90°. Hexagon: 60°. Pentagon: 72°.
- Each **interior** angle is 180° − the turn. Regular pentagon: 180° − 72° = 108°.
- All interior angles together: **(n − 2) × 180°**. (Split the polygon into n − 2 triangles from one corner.) Hexagon: 4 × 180° = 720°.

You'll program exactly this in [Floor Plan and Turtle](projects/floor-plan-and-turtle/spec.md): a turtle that moves forward and turns draws any regular polygon using `turn = 360 / n`.

---

## Part 5 — The Pythagorean theorem

In a **right triangle**, the two sides that make the right angle are the **legs** (a, b); the longest side, opposite the right angle, is the **hypotenuse** (c).

> **a² + b² = c²**

*Example:* legs 6 and 8: c² = 36 + 64 = 100, so c = **10**.

> **[W] Why is it true? A proof by rearrangement** (draw it as you read).
> 1. Draw a big square with side a + b.
> 2. Place four copies of the right triangle inside it, one in each corner, so that their hypotenuses form a tilted square in the middle. That middle square has side c, so area **c²**.
> 3. Now rearrange the same four triangles inside the same big square differently: put them in pairs to form two rectangles (each a × b) in two corners. The space left over is two squares: one a × a and one b × b, total **a² + b²**.
> 4. Both arrangements use the same big square and the same four triangles, so the leftover areas are equal: **a² + b² = c²**. ∎

**Finding a leg:** if the hypotenuse is 17 and one leg is 8: b² = 17² − 8² = 289 − 64 = 225, so b = **15**.

**Testing for a right angle (the converse):** if a² + b² = c², the triangle *is* right-angled. Builders use 3-4-5: mark 3 m and 4 m along two walls; if the diagonal is exactly 5 m, the corner is square.

### Distance between two points

The distance between (x₁, y₁) and (x₂, y₂) is the hypotenuse of a right triangle with legs (x₂ − x₁) and (y₂ − y₁):

$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

*Example:* (1, 2) to (4, 6): legs 3 and 4, so d = **5**.

A 1920 × 1080 screen has a diagonal of √(1920² + 1080²) ≈ **2,203 pixels**. This formula is how a game checks if two objects are close enough to collide.

---

## Part 6 — Similar shapes and a first look at trigonometry

### Similar shapes

Two shapes are **similar** if one is a scaled copy of the other: same angles, all lengths multiplied by the same **scale factor**.
- A 3-4-5 triangle and a 9-12-15 triangle are similar (scale factor 3).
- **Scale drawings and maps:** a scale of 1 : 50 means 1 cm on paper = 50 cm in reality.
- **Shadows:** a 2 m pole casts a 3 m shadow; a tree at the same time casts an 18 m shadow. The triangles are similar (same sun angle), so the tree is 2 × (18 ÷ 3) = **12 m** tall.

### Sine, cosine, tangent

Because all right triangles with the same angle are similar, the **ratios** of their sides depend only on the angle. Those ratios have names. For an angle θ ("theta") in a right triangle:

| Ratio | Definition | Memory hook |
| :-- | :-- | :-- |
| sin θ | opposite ÷ hypotenuse | **SOH** |
| cos θ | adjacent ÷ hypotenuse | **CAH** |
| tan θ | opposite ÷ adjacent | **TOA** |

("Opposite" is the side across from θ; "adjacent" is the leg next to θ.)

*Worked example:* a 5 m ladder leans against a wall at 60° to the ground. How high does it reach?
1. Known: hypotenuse 5, angle 60°. Want: the side opposite the angle (the height).
2. Opposite and hypotenuse → sine. sin 60° = height ÷ 5.
3. height = 5 × sin 60° ≈ 5 × 0.866 = **4.33 m**.

**Values worth knowing:** sin 30° = cos 60° = 0.5; sin 45° = cos 45° ≈ 0.707; tan 45° = 1; sin 90° = 1; cos 90° = 0.

### The circle picture (the one that matters most for computing)

Put a circle of radius 1 at the origin. Start at the point (1, 0) and turn by angle θ counterclockwise. The point you reach is

> **(cos θ, sin θ)**

For a circle of radius r: **(r cos θ, r sin θ)**. So cos and sin simply tell you **where you are on a circle** after turning by θ. This is how computers draw circles, rotate images, aim game characters, and (in Module 12) describe every sound and radio wave as a point going round a circle.

**Radians:** computers usually measure angles in radians, where a full turn is 2π (about 6.283). 180° = π radians. In Python: `math.sin(math.radians(30))` → 0.5. Forgetting to convert degrees to radians is one of the most common graphics bugs.

---

## Part 7 — Moving shapes on a grid

Every computer graphic is points on a grid, moved by simple rules:

| Transformation | Rule | Example on (3, 1) |
| :-- | :-- | :-- |
| **Translate** (slide) by (a, b) | (x, y) → (x + a, y + b) | by (2, 5) → (5, 6) |
| **Scale** by k (from the origin) | (x, y) → (kx, ky) | by 2 → (6, 2) |
| **Reflect** in the y-axis | (x, y) → (−x, y) | (−3, 1) |
| **Rotate 90°** counterclockwise about the origin | (x, y) → (−y, x) | (−1, 3) |
| **Rotate by θ** about the origin | (x, y) → (x cos θ − y sin θ, x sin θ + y cos θ) | θ = 90° gives the row above |

**Check the 90° rule** with Part 6: (1, 0) at angle 0° rotates to (0, 1) at angle 90° ✓ — and the formula gives (−0, 1) ✓.

You don't need to memorise the general rotation formula now. In [Module 12](../../12-math-for-engineering/overview.md) you'll see it's a **matrix**, and that every transformation in this table is one. That's linear algebra, and it's how every graphics card works.

---

## Practice routine (4 sections)

| Section | Focus |
| :-- | :-- |
| 1 | Session 1: units, area/volume unit conversion · Session 2: perimeter and area with the "why" for each · Session 3: circles (measure π yourself) · Session 4: volume and scaling · Session 5: Practice Set 1, items 1–7 |
| 2 | Session 1: angle facts · Session 2: triangle 180° (tear the corners; write the proof) · Session 3: polygons and the turtle walk · Sessions 4–5: Pythagoras (draw the proof twice, from memory the second time) |
| 3 | Session 1: distance formula · Session 2: similar shapes and scale · Sessions 3–4: trig: SOH-CAH-TOA, then the circle picture · Session 5: transformations |
| 4 | Sessions 1–3: [Floor Plan and Turtle](projects/floor-plan-and-turtle/spec.md) · Session 4: Practice Set 1 rest + Set 2, Feynman · Session 5: self-check |

**Warm-up [R] (every session):** draw the Pythagoras rearrangement proof from memory. (By section 3, fluently and without looking.)

**Key why-questions [W]:**
1. Why is a triangle's area half of base × height?
2. Why do areas scale by k² and volumes by k³?
3. Why do a polygon's exterior turns add to 360°?
4. Why does a² + b² = c²? (Proof by rearrangement.)

**Feynman target [F]:** *"What do sine and cosine actually tell you?"* Use the circle picture. Briefly, with a sketch.

---

## Practice sets

### Practice Set 1 — Mixed (20 problems; calculator for π, roots, trig)

1. Perimeter of a square with side 7.5.
2. Area of a parallelogram with base 12 and height 5.
3. Area of an L-shape: a 10 × 8 rectangle with a 4 × 3 corner removed.
4. Circumference and area of a circle with diameter 14.
5. Volume of a cylinder with radius 3 and height 10.
6. A room is 4 m × 3.5 m × 2.5 m high. Floor area? Volume?
7. A cube's side doubles from 2 to 4. By what factor do one face's area and the volume grow?
8. Two angles on a straight line; one is 115°. The other?
9. A triangle has angles 90° and 35°. The third?
10. A regular pentagon: each turn (exterior angle)? Each interior angle?
11. Right triangle with legs 5 and 12: hypotenuse?
12. Hypotenuse 17, one leg 8: other leg?
13. Is a triangle with sides 7, 24, 25 right-angled? Show why.
14. Distance between (−2, 1) and (4, 9).
15. Diagonal of a 1920 × 1080 screen, in pixels.
16. A triangle has sides 3, 4, 5. A similar triangle's shortest side is 9. Its other sides?
17. A 2 m pole casts a 3 m shadow. A tree casts an 18 m shadow. How tall is the tree?
18. Give sin 30°, cos 60°, tan 45°.
19. A 5 m ladder makes 60° with the ground. How high up the wall does it reach?
20. Rotate (3, 1) by 90° counterclockwise about the origin.

<details>
<summary>Answers (Set 1)</summary>

1. 30 · 2. 60 · 3. 68 · 4. 14π ≈ 44.0; 49π ≈ 153.9 · 5. 90π ≈ 282.7 · 6. 14 m²; 35 m³ · 7. ×4; ×8 · 8. 65° · 9. 55° · 10. 72°; 108° · 11. 13 · 12. 15 · 13. Yes: 7² + 24² = 49 + 576 = 625 = 25² · 14. 10 · 15. ≈ 2,203 · 16. 12 and 15 · 17. 12 m · 18. 0.5, 0.5, 1 · 19. ≈ 4.33 m · 20. (−1, 3)
</details>

### Practice Set 2 — Think about it (4 problems)

1. A pizza with 12-inch diameter costs $10; a 16-inch one costs $16. Which is better value per square inch? (Use πr².)
2. Explain, using the turtle walk, why a regular hexagon's interior angles are each 120°.
3. In screen coordinates, y grows **downward**. If a turtle at (100, 100) "moves up" by 20 pixels, what are its new coordinates? How would the 90° rotation rule change?
4. A builder measures 3 m along one wall and 4 m along the other from a corner, and the diagonal between the marks is 5.1 m. Is the corner a right angle? Is it more or less than 90°?

<details>
<summary>Answers (Set 2)</summary>

1. 12-inch: area π(6²) ≈ 113.1 in² → about 11.3 in² per dollar. 16-inch: π(8²) ≈ 201.1 in² → about 12.6 in² per dollar. **The 16-inch is better value.** (Diameter grew by 4/3, area by (4/3)² ≈ 1.78, price by only 1.6.)
2. At each of 6 corners the turtle turns 360° ÷ 6 = 60°. The interior angle and the turn make a straight line: 180° − 60° = 120°.
3. (100, 80): "up" means y decreases. Because the y-axis is flipped, a rotation that looks counterclockwise on screen uses (x, y) → (y, −x) in screen coordinates — a classic source of graphics bugs. Always draw a test case.
4. Not quite: 3² + 4² = 25, but 5.1² = 26.01 > 25. The diagonal is too long, so the corner is a bit **more** than 90° (opening the angle stretches the diagonal).
</details>

---

## Watch, practise, and play

*Companions, not replacements: the lessons above come first. Use the [V protocol](../../study-protocols.md#v--watch-actively). Video course for this track: [math resources](resources.md#video-course).*

- **Watch:** Khan Academy: Geometry. Eddie Woo: Pythagoras proofs and trigonometry. GeoGebra (free) for constructions.
- **Practise:** Khan Academy geometry and right-triangle trigonometry exercises.
- **Play** ([puzzles and games](puzzles-and-games.md)): measure π with a can · Pythagoras in the room · shadow height · turtle art contest · tangrams

---

## Self-check (cold; calculator for π, roots, trig)

1. Area of the triangle with corners (0, 0), (6, 0), and (0, 4).
2. Area of a circle with radius 2.5.
3. Volume and surface area of a 2 × 3 × 4 box.
4. The interior angles of an octagon add up to? Each interior angle of a regular octagon?
5. Right triangle with legs 9 and 12: hypotenuse?
6. Distance between (1, −3) and (7, 5).
7. A turtle draws a regular hexagon. By how many degrees does it turn at each corner?
8. A ramp rises 1 m over 4 m of horizontal distance. How long is the ramp? What angle does it make with the ground? (Use tan⁻¹ on your calculator.)
9. Where is the point at angle 30° on a circle of radius 10 centred at the origin?
10. **[R] Blank sheet:** area formulas with their reasons; the scaling law; the triangle-sum proof; the turtle-walk 360° fact; the Pythagoras proof (drawn); SOH-CAH-TOA; the circle picture of sin and cos.

<details>
<summary>Answers (self-check)</summary>

1. 12 · 2. 6.25π ≈ 19.6 · 3. 24; 52 · 4. 1,080°; 135° · 5. 15 · 6. 10 · 7. 60° · 8. √17 ≈ 4.12 m; about 14.0° · 9. (10 cos 30°, 10 sin 30°) ≈ (8.66, 5)
</details>

## Done when

- [ ] Self-check ≥ 8/9 on items 1–9, blank sheet done.
- [ ] You can draw the Pythagoras proof from memory.
- [ ] Four why-questions answered; Feynman recording made.
- [ ] [Floor Plan and Turtle](projects/floor-plan-and-turtle/spec.md) complete.

**Next:** [M11 — Functions, Exponentials, and Logarithms](M11-functions-exponentials-and-logarithms.md).
