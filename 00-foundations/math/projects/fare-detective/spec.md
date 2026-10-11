---
title: "Project: Fare Detective"
id: "FND-MA-PRJ-fare-detective"
type: "project"
module: "00-foundations"
track: "math"
phase: "B"
order: 410
prerequisites: [M07]
stages: "M08–M09"
artifact: "A notebook of real pricing formulas and solved questions; fitted linear models from collected data; fare.py"
deliverable: "A one-page recommendation: which plan should I choose, and when does that change?"
---

# Project: Fare Detective

| | |
| :-- | :-- |
| **You build** | You investigate real prices — taxi fares, phone plans, electricity, cloud storage, shipping — write them as algebra, uncover hidden pricing rules from data, and build a tool that fits models and finds break-even points |
| **Deliverable** | A one-page recommendation with a trade-off table and a graph |

---

## Why this matters

Most prices in the world are **a fixed part plus a rate**: a base fare plus a price per kilometre; a monthly fee plus a price per gigabyte. So is almost every performance number in computing: **start-up cost plus cost per item**. If you can find the fixed part and the rate from data, you can predict, compare, and decide.

This project trains the exact skill you'll use in [Module 09](../../../../09-networking/overview.md) to measure your network's latency and bandwidth, and in Modules 05 and 07 to model how your programs' running time grows. Here, the data is about money, which makes it easy to care about.

**Real-world analogs:** pricing pages, cost calculators, capacity planning, performance modelling ("time = latency + size ÷ bandwidth").

---

## Milestones

### Milestone 1 — Pricing rules as algebra (M08)

**Do:** find **five** published pricing rules from public sources (company websites, your city's official taxi tariff, your electricity supplier's published tariff). Good candidates:
- a taxi or ride-share fare rule (base + per km + per minute)
- two mobile phone or data plans
- an electricity tariff (daily standing charge + price per kWh)
- a cloud storage price (per GB per month, maybe with a free tier)
- a parcel shipping price by weight

For each:
1. **Define variables in words, with units** (M08 Part 6): "Let k = trip distance in km."
2. **Write the formula:** C = 3.50 + 2.25k.
3. **Note anything non-linear:** free tiers, minimum charges, price steps (tiers). Write these as separate rules: "If g ≤ 15, C = 10; otherwise C = 10 + 4(g − 15)."

> **Privacy rule:** use published prices and made-up usage, not your real bills or accounts. Your workbench is yours, but keep personal financial data out of anything you might share (README rule).

**Done when:** five rules written as formulas with defined variables and units.

### Milestone 2 — Ten questions (M08)

Write and answer **ten** questions using your formulas, all four Pólya steps written out, with at least:
- 3 "what does it cost for…" (evaluate)
- 3 "how much can I use for $X?" (solve an equation)
- 2 "what's the most I can use and stay under $X?" (solve an inequality)
- 2 rearranged formulas (e.g. solve your taxi formula for k)

**Done when:** ten solved questions, each checked in the original words.

**Checkpoint:** [Milestone Checkpoint](<../../../../04 - System/Milestone Checkpoint Template.md>). Why-ladder target: *in "C = 3.50 + 2.25k", what does each number mean, and what would change in the world if each one doubled?*

### Milestone 3 — Uncover hidden rules (M09)

Now the detective part: **find a pricing rule nobody told you.** Choose two sources where you can get (input, price) pairs but not the formula:
- a fare estimator on a ride-share or taxi website (try 6+ distances);
- a shipping calculator (try 6+ weights);
- a cloud pricing calculator;
- or a dataset you make: time how long `cp` takes to copy files of 6+ sizes (`dd if=/dev/urandom of=f bs=1M count=N`, then `time cp f g`). This one is "price in seconds" — and it's a direct preview of Module 09.

For each source, follow M09's model-building subgoals:
1. Collect at least 6 points. Record them in a CSV file (`x,y` per line).
2. Plot by hand on graph paper, then in Desmos.
3. Does it look linear? If there's a bend or a jump, find where.
4. Fit a line (from two well-chosen points). State m and b **with units and meaning**.
5. Compute the residual for every point.
6. Predict one new point, *then* check it against the source.

**Done when:** two models, each with a plot, residuals, an interpretation, and one tested prediction.

### Milestone 4 — `fare.py` (M09)

A command-line tool:
- `python3 fare.py fit data.csv` reads the points, fits a line through the first and last points **and** through the pair of points that gives the smallest total absolute residual (try every pair — a small brute-force search), and prints both models with their total residuals. (You'll learn the standard best-fit method, least squares, in Module 12.)
- `python3 fare.py plot data.csv` draws the points and the line as an ASCII chart in the terminal (or with `matplotlib` if you have it).
- `python3 fare.py compare "20 + 5x" "35 + 2x"` finds the break-even point of two linear plans by solving the system, and says which plan is cheaper below and above it.

**Rules:** parse the plan expressions in the simple form `"b + m x"` only (don't build a general expression parser — that's Module 02's skill). Use `Fraction` to avoid float surprises in break-even points.

**Tests:** for each command, at least two cases you solved by hand in M09's practice sets (e.g. the gym and print-shop problems).

**Done when:** all three commands work on your Milestone 3 data, and tests pass.

### Milestone 5 — The recommendation (M09)

Pick one real decision (two phone plans, two cloud storage providers, two ways to get to work). Write a **one-page recommendation**:
- the question, in one sentence;
- both cost models (formulas, with units);
- a graph of both lines with the break-even point marked;
- a trade-off table (E10 style, simplified): cost at low, medium, and high use, plus one non-cost criterion;
- your recommendation, **and what would change it** ("If my data use rises above 5 GB per month, plan B becomes cheaper").

**Done when:** the page is written, with the graph.

---

## Common pitfalls

- **Units on the slope.** "2.25" is not a slope; "$2.25 per km" is.
- **Ignoring tiers.** Many prices have free allowances or steps. A straight line through tiered data gives a wrong model. Look at the plot first.
- **Extrapolating wildly.** Your 1–20 km fare model may not hold for a 300 km trip (many fares change for long trips). Say so.
- **Choosing two points that are close together.** Small measurement errors give a big slope error. Use points far apart.
- **Treating the `cp` timing as exact.** Run each size three times; use the median. Caching (Magnitudes Field Guide) will affect repeated runs.

## Communication deliverable

The **one-page recommendation** (E08–E10 level): clear question, models, graph, trade-off table, recommendation, and the condition that would change it.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Before Milestone 3, write the model-building subgoals from memory |
| **F** | Explain m and b of your `cp` model to a friend: what is the computer doing during the "fixed" part? |
| **W** | What each number means; why two far-apart points |
| **S** | Pólya steps written for every question in Milestone 2 |
| **I** | Questions mix evaluate, solve, inequality, rearrange |
| **T** | The recommendation |

## Stretch goals

- **Least squares now:** look up the least-squares formulas for slope and intercept, implement them, and compare with your brute-force fit.
- **Piecewise models:** handle tiered pricing in `fare.py` with a list of (threshold, rate) pairs.
- **Three plans:** find the cheapest plan for every usage level when there are three or more plans (hint: the answer is a set of intervals).

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Formulas | Five rules, variables defined with units, tiers handled | Most | Few |
| Questions | Ten, all Pólya steps, all checked | Most | Few |
| Models from data | Plots, residuals, interpretations, tested predictions | Partial | Missing |
| `fare.py` | Three commands, tests from hand-worked problems | Two commands | Missing |
| Recommendation | Graph, table, clear trigger condition | Complete | Missing |

**Done when:** every area at least 2.

## Connections

- **Back:** M06 (rates, units), M08 (equations, inequalities, formulas), M09 (models, systems).
- **Forward:** Module 05 (timing algorithms), Module 07 (measuring your allocator and archive tool), Module 09 (latency + size ÷ bandwidth on your real network), Module 12 (least squares).
