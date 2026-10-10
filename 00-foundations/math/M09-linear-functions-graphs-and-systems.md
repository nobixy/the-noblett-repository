---
title: "M09 — Linear Functions, Graphs, and Systems"
stage: M09
track: math
hours: 30
weeks: 4
---

# M09 — Linear Functions, Graphs, and Systems

**In this stage you will:** plot points, understand a function as an input-output machine (just like a function in code), work with straight-line functions — slope, intercept, y = mx + b — build linear models from real data and use them to predict, and solve two equations together to find where two lines meet.

**Time:** about 30 hours over 4 weeks.

**Before you start:** M08 done. You can solve equations and rearrange formulas.

**Tool:** Desmos (desmos.com/calculator) is encouraged from now on. Always sketch by hand first, then check in Desmos.

---

## Diagnostic (cold, 25 minutes)

1. Which quadrant is the point (3, −2) in?
2. If f(x) = 2x + 3, what is f(4)?
3. Find the slope of the line through (1, 2) and (4, 11).
4. What are the slope and y-intercept of y = −2x + 5?
5. Write the equation of the line with slope ½ and y-intercept 4.
6. Write the equation of the line through (2, 5) and (6, 13).
7. Solve together: y = 2x + 1 and y = −x + 7.
8. Solve together: x + y = 10 and x − y = 4.
9. Plan A costs $20 plus $5 per GB. Plan B costs $35 plus $2 per GB. For how many GB do they cost the same?
10. Is y = x² a linear function? Why or why not?

<details>
<summary>Answers (diagnostic)</summary>

1. Quadrant IV (right, down) · 2. 11 · 3. 3 · 4. slope −2, intercept 5 · 5. y = ½x + 4 · 6. y = 2x + 1 · 7. x = 2, y = 5 · 8. x = 7, y = 3 · 9. 5 GB · 10. No: its rate of change isn't constant (from 0 to 1 it rises 1; from 1 to 2 it rises 3), so its graph is a curve.
</details>

---

## Why this matters

A huge amount of engineering is **"a fixed cost plus a cost per unit."** Sending a file over a network: a fixed delay to get started, plus time per megabyte. A taxi: a base fare plus a price per kilometre. A program: startup time plus time per item. These are all **linear models**, and this stage teaches you to find them from measurements, read what their numbers mean, and predict with them.

You'll use exactly this skill in Module 05 (timing algorithms), Module 07 (measuring your allocator), and Module 09, where the time to send *n* bytes is roughly **latency + n ÷ bandwidth** — a straight line whose slope and intercept you'll measure on your own network.

And **functions** are the bridge to programming: a math function and a Python function are the same idea.

---

## Part 1 — The coordinate plane

Two number lines at right angles: the **x-axis** (horizontal) and the **y-axis** (vertical), crossing at the **origin** (0, 0). A point is written **(x, y)**: go x right (left if negative), then y up (down if negative).

```
            y
            ↑
   II       |       I
  (−, +)    |    (+, +)
  ──────────┼──────────→ x
   III      |       IV
  (−, −)    |    (+, −)
```

**Screen coordinates are different.** On computer screens (and in your browser engine in Module 10), the origin is usually the **top-left** corner and **y grows downward**. Same idea, flipped vertically. Always check which convention a system uses.

---

## Part 2 — Functions

A **function** is a rule that takes an input and gives exactly **one** output.

> **f(x) = 2x + 3** — "f of x equals 2x plus 3." Input 4: f(4) = 2(4) + 3 = 11.

The same thing in Python:

```python
def f(x):
    return 2 * x + 3

print(f(4))   # 11
```

Three ways to show a function:

| Table | Rule | Graph |
| :-- | :-- | :-- |
| x: 0, 1, 2, 3 → y: 3, 5, 7, 9 | y = 2x + 3 | points (0, 3), (1, 5), (2, 7), (3, 9) on a straight line |

Being able to move between the three is the main skill of this stage.

**"Exactly one output"** matters: f(4) can't be both 11 and 12. (A circle is not the graph of a function of x, because one x gives two y's.)

---

## Part 3 — Linear functions: slope and intercept

A function is **linear** when its output changes by the **same amount** every time the input goes up by 1. Its graph is a straight line.

### Slope

The **slope** m is the rate of change: how much y changes per one unit of x.

$$m = \frac{\text{rise}}{\text{run}} = \frac{\text{change in } y}{\text{change in } x} = \frac{y_2 - y_1}{x_2 - x_1}$$

**Subgoal labels [S] for slope from two points:**
1. **Label** the points (x₁, y₁) and (x₂, y₂).
2. **Subtract** the y's (second minus first).
3. **Subtract** the x's **in the same order**.
4. **Divide.** Simplify.
5. **Sense-check:** line goes up left-to-right → positive slope; down → negative.

*Worked example:* slope through (1, 2) and (4, 11): (11 − 2)/(4 − 1) = 9/3 = **3**. Up 3 for every 1 to the right.

| Slope | Line |
| :-- | :-- |
| positive | rises left to right |
| negative | falls left to right |
| 0 | horizontal (y never changes) |
| undefined (run = 0) | vertical (not a function of x) |

### Intercept

The **y-intercept** b is where the line crosses the y-axis: the output when x = 0. It's the **starting value**.

### Slope-intercept form: y = mx + b

> **y = mx + b** — m is the slope, b is the y-intercept.

**Graphing y = mx + b by hand:**
1. Plot (0, b).
2. From there, go **run 1, rise m** (or for a fraction like ⅔: run 3, rise 2). Plot.
3. Repeat once more, then draw the line through the points.

**Finding the equation from two points — subgoal labels [S]:**
1. **Slope** m from the two points.
2. **Substitute** m and one point (x, y) into y = mx + b.
3. **Solve** for b.
4. **Write** y = mx + b.
5. **Check** with the other point.

*Worked example:* line through (2, 5) and (6, 13).
1. m = (13 − 5)/(6 − 2) = 8/4 = 2.
2. 5 = 2(2) + b.
3. b = 1.
4. **y = 2x + 1.**
5. Check (6, 13): 2(6) + 1 = 13 ✓

**Other forms:** an equation like 2x + 3y = 12 is also a line. Solve for y (M08) to get slope-intercept form: 3y = −2x + 12 → **y = −⅔x + 4**.

**Parallel lines** have the same slope (and different intercepts). They never meet.

> **[W] Why is the graph of y = mx + b a straight line?** Because every step of 1 in x adds exactly m to y. Equal steps across, equal steps up, every time: that's what "straight" means. If the step up changed (as in y = x²), the line would bend.

---

## Part 4 — Linear models from real data

A **model** is a simple function that describes real measurements well enough to predict.

**The meaning of m and b in a model:**
- **b** = the **fixed part**: the value when the input is 0 (base fare, startup time, latency).
- **m** = the **rate**: how much the output grows per unit of input, **with units** (dollars per km, seconds per MB).

**Subgoal labels [S] for building a linear model:**
1. **Plot the data** (by hand or Desmos). Does it look roughly like a line? If not, stop: a line is the wrong model.
2. **Pick two points** far apart that sit on the trend (or draw a line by eye through the middle of the points and read two points off it).
3. **Compute m and b** (Part 3), **with units**.
4. **Interpret** m and b in words.
5. **Check** against the other data points. How far off is each? (These differences are called **residuals**.)
6. **Predict**, and say how much you trust the prediction.

*Worked example:* you time three file transfers on your network:

| Size (MB) | 10 | 50 | 100 |
| :-- | :-- | :-- | :-- |
| Time (s) | 1.2 | 4.4 | 8.4 |

1. Plotted: very close to a line.
2. Use (10, 1.2) and (100, 8.4).
3. m = (8.4 − 1.2)/(100 − 10) = 7.2/90 = **0.08 s per MB**. b: 1.2 = 0.08(10) + b → b = **0.4 s**. Model: **T = 0.08·size + 0.4**.
4. **Interpretation:** every transfer has a fixed 0.4 s start-up delay (the **latency**), plus 0.08 s per MB. 0.08 s per MB means 1 ÷ 0.08 = **12.5 MB/s** (the **bandwidth**).
5. Check (50, 4.4): 0.08(50) + 0.4 = 4.4 ✓ (residual 0).
6. Predict 250 MB: 0.08(250) + 0.4 = **20.4 s**.

**Interpolating vs extrapolating:** predicting *inside* your data range (e.g. 70 MB) is usually safe. Predicting *far outside* it (e.g. 50,000 MB) assumes the pattern continues, which it may not (disks fill, caches run out, connections time out). Always say which you're doing.

(In [Module 12](../../12-math-for-engineering/overview.md) you'll learn **least squares**, the standard way to fit the best line through many points. For now, two good points are enough.)

---

## Part 5 — Systems of two equations

Two lines usually cross at **one point**. That point satisfies **both** equations. Finding it is called **solving a system**.

**Why it's useful:** "when do two plans cost the same?" (the **break-even** point), "when does the slower runner catch up?", "what mix of two things gives this total?"

### Method 1 — Graph it

Graph both lines; read off where they cross. Good for seeing; imprecise for exact answers. Use Desmos to check.

### Method 2 — Substitution

**Subgoal labels [S]:**
1. **Solve one equation** for one variable (pick the easiest).
2. **Substitute** that expression into the **other** equation.
3. **Solve** the resulting one-variable equation.
4. **Back-substitute** to find the other variable.
5. **Check** in **both** original equations.

*Worked example:* y = 2x + 1 and y = −x + 7.
1. Already solved for y.
2. 2x + 1 = −x + 7.
3. 3x = 6 → x = 2.
4. y = 2(2) + 1 = 5.
5. Check the second: −2 + 7 = 5 ✓. **(2, 5).**

### Method 3 — Elimination

**Subgoal labels [S]:**
1. **Line up** both equations as ax + by = c.
2. **Multiply** one or both equations so that one variable has **opposite** coefficients.
3. **Add** the equations: that variable disappears.
4. **Solve**, then back-substitute.
5. **Check** in both.

*Worked example:* 3x + 2y = 16 and x + 4y = 12.
2. Multiply the second equation by −3 so the x's become opposites: −3x − 12y = −36.
3. Add it to the first: (3x + 2y) + (−3x − 12y) = 16 + (−36) → −10y = −20.
4. y = 2. Back-substitute into x + 4y = 12: x + 8 = 12 → x = 4.
5. Check: 3(4) + 2(2) = 16 ✓; 4 + 4(2) = 12 ✓. **(4, 2).**

*Worked example (break-even):* Plan A: $20 + $5/GB. Plan B: $35 + $2/GB. Let g = GB used.
- A = 20 + 5g, B = 35 + 2g. Same cost when 20 + 5g = 35 + 2g → 3g = 15 → **g = 5 GB**.
- Below 5 GB, A is cheaper (lower start); above 5 GB, B is cheaper (lower slope). The intercepts decide who wins at first; the slopes decide who wins in the end.

### When there's no single answer

- **Parallel lines** (same slope, different intercept): **no solution**. Elimination gives something like 0 = 4.
- **The same line twice**: **infinitely many solutions**. Elimination gives 0 = 0.

(That's M08's special cases, now with pictures.)

---

## Practice routine (4 weeks)

| Week | Focus |
| :-- | :-- |
| 1 | Mon: coordinate plane and screen coordinates · Tue: functions as machines (write 3 as Python functions) · Wed–Thu: slope · Fri: y = mx + b, graphing by hand |
| 2 | Mon–Tue: equation from two points; other forms · Wed: parallel lines · Thu–Fri: Practice Set 1, items 1–11 |
| 3 | Mon–Tue: linear models from data (do the worked example, then one of your own: time how long `seq 1 N > /dev/null` takes for five values of N) · Wed–Thu: systems, all three methods · Fri: Practice Set 1 rest |
| 4 | Mon–Wed: [Fare Detective](projects/fare-detective/spec.md) Milestones 3–4 · Thu: Practice Set 2 + Feynman · Fri: self-check |

**Daily warm-up [R]:** the "equation from two points" subgoal labels from memory, then one problem.

**Key why-questions [W]:**
1. Why is the graph of y = mx + b straight?
2. Why does the point where two lines cross solve both equations?
3. In a cost model, which number decides who's cheaper for small usage, and which decides for large usage? Why?
4. Why is extrapolating riskier than interpolating?

**Feynman target [F]:** *"What do the slope and intercept of a model tell you?"* Use the file-transfer example. 2 minutes, out loud, with a sketch.

---

## Practice sets

### Practice Set 1 — Mixed (18 problems)

1. f(x) = −3x + 7. Find f(−2), f(0), and f(5).
2. Make a table for y = 4x − 1 for x = −1, 0, 1, 2, 3.
3. Slope through (−2, 3) and (4, 6).
4. Slope through (1, 5) and (3, −1).
5. Slope through (2, 4) and (7, 4). What does the line look like?
6. Equation of the line with slope −3 and y-intercept 2.
7. Equation of the line through (1, 1) and (3, 7).
8. Equation of the line through (−2, 1) and (2, 9).
9. Equation of the line parallel to y = 4x − 3 through (1, 6).
10. Rewrite 2x + 3y = 12 in slope-intercept form.
11. Where does y = 2x − 8 cross the x-axis?
12. Solve: y = 3x − 4 and y = x + 2.
13. Solve: 2x + y = 11 and x − y = 1.
14. Solve: 3x + 2y = 16 and x + 4y = 12.
15. Solve: y = 2x + 1 and y = 2x − 3. Explain the result.
16. A taxi charges $3.50 plus $2.25 per km. Write the cost function. What does a 12 km trip cost? How far can you go for $26?
17. File transfers: (10 MB, 1.2 s), (50 MB, 4.4 s), (100 MB, 8.4 s). Build the model, interpret m and b (give the bandwidth in MB/s), and predict 250 MB.
18. Gym A: $40 to join + $25/month. Gym B: $10 to join + $30/month. When do they cost the same? After how many months is A cheaper?

<details>
<summary>Answers (Set 1)</summary>

1. 13, 7, −8 · 2. −5, −1, 3, 7, 11 · 3. ½ · 4. −3 · 5. 0; horizontal · 6. y = −3x + 2 · 7. y = 3x − 2 · 8. y = 2x + 5 · 9. y = 4x + 2 · 10. y = −⅔x + 4 · 11. x = 4 (set y = 0) · 12. (3, 5) · 13. (4, 3) · 14. (4, 2) · 15. No solution: same slope, different intercepts, so the lines are parallel · 16. C = 3.50 + 2.25k; $30.50; 10 km · 17. T = 0.08·size + 0.4; 0.4 s latency, 0.08 s/MB (12.5 MB/s); 20.4 s · 18. Equal at 6 months ($190 each); A is cheaper from month 7 on
</details>

### Practice Set 2 — Think about it (4 problems)

1. A function machine gives f(1) = 5, f(2) = 8, f(3) = 11. Is it linear? Find the rule. Write it as a Python function.
2. Your measurements of a program's run time are: 1,000 items → 0.05 s; 10,000 → 0.5 s; 100,000 → 5 s; 1,000,000 → 70 s. Is a linear model good for all of this data? What might be happening at the largest size?
3. Two lines have the same slope and the same intercept. How many solutions does the system have? Why?
4. Why can't a vertical line be written as y = mx + b?

<details>
<summary>Answers (Set 2)</summary>

1. Yes: each step adds 3. f(x) = 3x + 2. `def f(x): return 3 * x + 2`.
2. The first three fit a line through 0 with slope 0.00005 s/item, which predicts 50 s for 1,000,000 items, but it took 70 s. The pattern bends at large sizes: perhaps the data no longer fits in fast memory (cache), so each item gets slower. Extrapolation from small sizes would have been wrong. (You'll see exactly this effect in Module 06.)
3. Infinitely many: they're the same line, so every point on it is on both.
4. A vertical line has the same x for every y (like x = 3). Its "run" is 0, so the slope would need division by zero, which is undefined. And it isn't a function of x (one x has many y's).
</details>

---

## Watch, practise, and play

*Companions, not replacements: the lessons above come first. Use the [V protocol](../../study-protocols.md#v--watch-actively). Full list: [courses-and-videos.md](../../courses-and-videos.md#foundations-math).*

- **Watch:** Khan Academy: Algebra 1, linear equations, graphs, and systems. *Algebra: Elementary to Advanced* (Coursera), courses 1–2.
- **Practise:** Desmos (free) classroom activities on slopes and intercepts.
- **Play** ([puzzles and games](puzzles-and-games.md)): Desmos art · who catches whom?

---

## Self-check (cold, 35 minutes)

1. If f(x) = 5 − 2x, find f(−3).
2. Find the slope through (−1, −4) and (3, 8).
3. Find the equation of that line.
4. Find the slope and y-intercept of 4x − 2y = 6.
5. Solve: y = −x + 9 and y = 2x − 3.
6. Solve: 5x − 2y = 4 and 3x + 2y = 12.
7. Print shop A charges $12 setup plus $0.08 per page. Shop B charges $5 setup plus $0.15 per page. At how many pages do they cost the same? Which is cheaper for 500 pages?
8. Data: (2, 9) and (5, 18). Build the linear model and predict the value at x = 10.
9. **[R] Blank sheet (10 min):** what a function is; slope formula with meaning; y = mx + b; the model-building subgoals with what m and b mean; substitution and elimination subgoals; the three outcomes for a system.

<details>
<summary>Answers (self-check)</summary>

1. 11 · 2. 3 · 3. y = 3x − 1 · 4. y = 2x − 3: slope 2, intercept −3 · 5. (4, 5) · 6. (2, 3) · 7. 100 pages; for 500 pages, A costs $52 and B costs $80, so A is cheaper · 8. y = 3x + 3; 33
</details>

## Done when

- [ ] Self-check ≥ 7/8 on items 1–8, blank sheet done.
- [ ] You built one linear model from your own measurements (week 3 timing task).
- [ ] Four why-questions answered; Feynman recording made.
- [ ] [Fare Detective](projects/fare-detective/spec.md) complete.

**Next:** [M10 — Geometry and Measurement](M10-geometry-and-measurement.md).
