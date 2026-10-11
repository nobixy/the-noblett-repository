---
title: "Foundations: Math"
id: "FND-MA"
type: "overview"
module: "00-foundations"
track: "math"
phase: "A"
order: 130
prerequisites: []
checkpoints: [FND-MA-ASSESS]
tags: [module, foundations, math]
---

# Foundations: Math

*Part of [00 — Foundations](../overview.md).*

**From place value to logarithms.** This track rebuilds mathematics from whole numbers upward: place value, the four operations, factors and primes, fractions, decimals and percents, negative numbers and exponents, algebra, graphs and linear models, geometry, and finally exponential and logarithmic functions. After it, you continue with [03 Discrete Math](../../03-discrete-math/overview.md) and [12 Math for Engineering](../../12-math-for-engineering/overview.md) (calculus, linear algebra, probability).

It is written for an adult who wants to understand **why** each procedure works, not just memorise it. Every rule here comes with its reason. Every procedure comes with labelled steps. Every stage is connected to something you will build.

---

## Why this matters for an engineer

Math is the language systems are described in. But you don't need it as a pile of formulas. You need it as **a way of reasoning** you trust:

- **Place value and bases** are how computers store everything: binary, hexadecimal, memory addresses, colours, network addresses.
- **Division with remainder** is how hash tables, clocks, ring buffers, and checksums work (`%` in code).
- **Primes and the greatest common divisor** are the core of public-key cryptography.
- **Fractions, decimals, and ratios** are how you reason about speeds, bandwidth, error rates, and why `0.1 + 0.2` isn't exactly `0.3` on a computer.
- **Negative numbers and exponents** are how computers store signed numbers and how you size memory (powers of 2).
- **Algebra** is how you reason about any quantity you don't know yet, and how you model a system's behaviour.
- **Linear models** predict performance: a fixed cost plus a cost per item. Every network transfer time works this way.
- **Geometry** is layout (your browser engine), graphics, and signals.
- **Logarithms** are how you measure algorithm speed ("binary search takes log₂ n steps") and signal strength (decibels).

Math also trains the habit at the centre of engineering: **break a hard problem into steps, check each step, and know why each step is allowed.**

---

## What you will be able to do at the end

1. Compute with whole numbers, fractions, decimals, percents, and negative numbers accurately, by hand and mentally, and estimate to check any answer.
2. Convert between decimal, binary, and hexadecimal, and explain why the conversion works.
3. Factor numbers, find greatest common divisors with Euclid's algorithm, and explain why it works.
4. Use exponents, scientific notation, and the order of operations correctly.
5. Write and solve linear equations and inequalities, including from word problems.
6. Build a linear model from real data, graph it, and use it to predict; solve systems of two equations.
7. Use area, volume, angles, the Pythagorean theorem, and basic trigonometry on real objects and on screen coordinates.
8. Work with quadratic, exponential, and logarithmic functions, and explain what a logarithm *means*.
9. Explain the *why* behind every procedure above to another person.

---

## The eleven stages

| Stage | Title | Core content | Project |
| :-- | :-- | :-- | :-- |
| [M01](M01-whole-numbers-and-place-value.md) | Whole numbers and place value | Digits, places, zero, big numbers, rounding, bases 2, 5, 16 | [Base Workshop](projects/base-workshop/spec.md) |
| [M02](M02-addition-and-subtraction.md) | Addition and subtraction | Meanings, properties, mental strategies, carrying and borrowing (and why), other bases, clock time | Base Workshop |
| [M03](M03-multiplication-and-division.md) | Multiplication and division | Area model, times tables, distributive law, long multiplication and division, remainders and modulo | [Prime Factory](projects/prime-factory/spec.md) starts |
| [M04](M04-factors-primes-and-divisibility.md) | Factors, primes, and divisibility | Divisibility tests, primes, factorisation, GCD (Euclid), LCM | Prime Factory |
| [M05](M05-fractions.md) | Fractions | Meaning, equivalence, comparing, all four operations (and why) | [Ratio Workshop](projects/ratio-workshop/spec.md) starts |
| [M06](M06-decimals-percents-and-ratios.md) | Decimals, percents, and ratios | Decimal place value, percent change, rates, unit conversion, why `0.1 + 0.2 ≠ 0.3` | Ratio Workshop |
| [M07](M07-negatives-exponents-and-order-of-operations.md) | Negatives, exponents, order of operations | Integers, why (−)×(−)=(+), powers, roots, scientific notation, bytes and powers of 2 | [Magnitudes Field Guide](projects/magnitudes-field-guide/spec.md) |
| [M08](M08-algebra-expressions-and-equations.md) | Algebra: expressions and equations | Variables, simplifying, solving equations and inequalities, formulas, word problems | [Fare Detective](projects/fare-detective/spec.md) starts |
| [M09](M09-linear-functions-graphs-and-systems.md) | Linear functions, graphs, and systems | Coordinates, functions, slope, linear models from data, systems of equations | Fare Detective |
| [M10](M10-geometry-and-measurement.md) | Geometry and measurement | Units, area, volume, angles, Pythagoras, similar shapes, intro trigonometry, screen coordinates | [Floor Plan and Turtle](projects/floor-plan-and-turtle/spec.md) |
| [M11](M11-functions-exponentials-and-logarithms.md) | Functions, exponentials, logarithms | Quadratics, exponential growth and decay, logarithms, sequences and sums | [Growth and Halving Lab](projects/growth-and-halving-lab/spec.md) |

### Pace

There is no schedule. Each stage's practice routine is written as numbered **sections** of five **math sessions** each (see [study-protocols § The session loop](../../study-protocols.md#the-session-loop)); do math sessions when you are freshest. **Go faster** when a stage's diagnostic (the first thing in each stage) shows you already know it: do the diagnostic, fix the misses, do the self-check, move on. **Go slower** when a self-check is under 80%. There is no prize for speed; there is a big prize for no gaps.

---

## How every stage is built

Each stage file has the same parts:

1. **Diagnostic** (cold): find out what you already know. Skip what you've mastered.
2. **Why it matters**: the connection to later builds.
3. **Learn**: explanations, each rule with its reason [W], each procedure with **worked examples whose steps are labelled** [S].
4. **Practice sets**: always **mixed** [I], with answers in collapsible blocks. Do them on paper first; check after.
5. **Why-ladders** [W] and a **Feynman target** [F] for the stage's central idea.
6. **Self-check**: a cold test at the end of the stage. **Done when** ≥ 80%.

### The math session

| Step | What | Protocol |
| :-- | :-- | :-- |
| 1 | **Warm-up recall:** from memory, write the last session's procedure as labelled steps and do one example | [R] [S] |
| 2 | **Learn:** the session's part of the stage; cover each worked example and redo it from the labels only | [S] |
| 3 | **Practice:** the session's mixed set, on paper, no calculator unless the stage says so | [I] |
| 4 | **Check and log:** mark answers; every miss goes in your math error log (below) | [R] |
| 5 | **Why:** one why-ladder on the session's main rule | [W] |

**Session 5 of every section:** a cumulative mixed set: 10 problems from this section, 5 from earlier stages (spacing [I]) — or, once per section, **Fun Session**: two games or puzzles from [your stage](puzzles-and-games.md).
**Section Review:** redo two old problems cold, one from your error log.

**Minimum session:** 10 mixed problems from earlier stages and your flashcards. That counts.

### The math error log

Like the spelling log, but for math. Keep `~/workbench/math/math-errors.tsv`:

```
date	stage	problem	my_answer	right_answer	type	fix
YYYY-MM-DD	M05	3/4 + 1/6	4/10	11/12	concept	added tops and bottoms; need a common unit first (W-ladder in M05)
YYYY-MM-DD	M03	7 × 8	54	56	fact	7×8=56: "5,6,7,8" → 56 = 7×8
```

*(The `date` column is just when you logged the miss — record metadata, like a journal entry's date. It does not schedule anything.)*

**Error types:** `fact` (a times-table or basic fact), `careless` (copied wrong, sign dropped), `procedure` (a step missing or out of order), `concept` (didn't understand why), `reading` (misread the question).

At each Section Review, count the types. `concept` errors need a why-ladder and a Feynman pass. `procedure` errors need subgoal labels. `careless` errors need a checking habit (estimate first; check by the inverse operation). `fact` errors need flashcards.

### Calculator and computer policy

- **M01–M07:** no calculator for practice sets. Use one only to check, *after* you have an answer by hand. The point is fluency and number sense.
- **M08–M11:** a calculator is allowed for messy arithmetic once you can do the stage's procedures by hand.
- **Projects:** use Python freely (after [01 Lab 01](../../01-intro-cs-taste/labs/lab-01-python-first-steps.md)). Many projects ask you to *check* your hand work with code: the code is a second witness, not a replacement.
- **Desmos** (desmos.com/calculator, free) is encouraged from M08 on for graphing.

---

## How the study methods run through this track

| Protocol | How it shows up in math |
| :-- | :-- |
| **R** Blank-sheet retrieval | Every session's warm-up: write a procedure from memory as labelled steps and do one example. Each section: blank-sheet the stage's main ideas. Cold diagnostics and self-checks. |
| **F** Feynman pass | Each stage has one central idea to explain in plain words (e.g. "why we carry," "why invert and multiply works," "what a logarithm is"). Spoken once per section. |
| **W** Why-ladder | Every rule and every step: "Why is this allowed? What would break without it?" Each stage lists its key why-questions. |
| **S** Subgoal labels | Every worked example has labelled steps. You cover the example and redo it from the labels alone. Your labels become flashcards. |
| **I** Interleave and space | Every practice set is mixed. Session-5 cumulative sets bring back earlier stages. Flashcards for facts and procedures on the flashcard spacing schedule ([I], part of the technique). |
| **D** Diffuse break | A hard problem gets three honest attempts, then a stuck note and a walk. Come back with the note only. |
| **T** Teach-back and write-up | Each project has a short written report or a recorded explanation, sized to your English stage. |
| **Pólya** | Word problems use Pólya's four steps: *understand → plan → carry out → look back* ([LM14](<../../02 - Atlas/LM14 - Pólya's Problem Solving.md>)). |

---

## Projects in this track

Small, real, and each connected to later builds. Milestones before [01 Lab 01](../../01-intro-cs-taste/labs/lab-01-python-first-steps.md) are paper-and-pencil; later milestones add short Python programs.

| Project | Stages | What you make | Connects to |
| :-- | :-- | :-- | :-- |
| [Base Workshop](projects/base-workshop/spec.md) | M01–M02 | A paper counting board in bases 2, 5, 10, 16; then a converter and an "odometer" simulator in Python | Binary and hex everywhere (04, 06, 07) |
| [Prime Factory](projects/prime-factory/spec.md) | M03–M04 | A hand sieve, factor trees, Euclid by hand; then a sieve, factoriser, and GCD program with tests | Toy cipher (03), hashing (05) |
| [Ratio Workshop](projects/ratio-workshop/spec.md) | M05–M06 | Recipe scaler, screen and aspect-ratio calculator, download-time estimator | Units and rates in networking (09) |
| [Magnitudes Field Guide](projects/magnitudes-field-guide/spec.md) | M07 | A poster and a short guide to the sizes and speeds inside a computer, from nanoseconds to terabytes | Performance thinking everywhere |
| [Fare Detective](projects/fare-detective/spec.md) | M08–M09 | Linear models of real prices from real data, with predictions and break-even points | Performance models (07, 09) |
| [Floor Plan and Turtle](projects/floor-plan-and-turtle/spec.md) | M10 | A scale floor plan of a room, then a Python turtle program that draws it and geometric art | Layout in the browser engine (10), graphics |
| [Growth and Halving Lab](projects/growth-and-halving-lab/spec.md) | M11 | Experiments on doubling and halving, including timing your own search programs | Algorithm analysis (05) |

---

## Video course

- **Primary:** **Khan Academy math** — [Arithmetic](https://www.khanacademy.org/math/arithmetic) → [Pre-algebra](https://www.khanacademy.org/math/pre-algebra) → [Algebra 1](https://www.khanacademy.org/math/algebra) → [High school geometry](https://www.khanacademy.org/math/geometry) → [Algebra 2](https://www.khanacademy.org/math/algebra2). Short videos with auto-checked practice and unit tests, covering M01–M11.
- **Alternate:** **Math Antics** — [YouTube channel](https://www.youtube.com/@mathantics) · [mathantics.com](https://www.mathantics.com/). Slower and friendlier, strongest in M01–M07; no logarithms.
- **Which lectures go with which lab and project:** the map in [resources](<resources.md#lesson-to-vault-map>). Watch with the [V protocol](../../study-protocols.md#v--watch-actively) and [use courses as companions](../../study-protocols.md#using-video-courses).

---

## Fun, videos, and courses

- **[Puzzles and games](puzzles-and-games.md):** number tricks (with the *why*), card and dice games, Fermi questions, Desmos challenges, and online puzzle platforms — sorted by stage. Use them for warm-ups and the **Fun Session** in each section.
- **Video course:** see [above](#video-course). Every stage file also has a short **Watch, practise, and play** section with extra videos for that stage.
- **[The first sections](../first-sections.md):** the plan for the start (Sections 1–12).

## Free resources (pointers only)

- **OpenStax** (openstax.org, free textbooks): *Prealgebra 2e* (M01–M07), *Elementary Algebra 2e* (M08–M09), *Intermediate Algebra 2e* and *College Algebra 2e* (M10–M11). Use for extra practice problems with answers.
- **Khan Academy** (khanacademy.org): use the **unit tests** as extra cold checks, not as the main path.
- **Paul Lockhart, *Arithmetic*** (owned): a beautiful companion for M01–M05 on *why* arithmetic works. A few pages, when you feel like it.
- **3Blue1Brown** (youtube, 3blue1brown.com): visual intuition, especially for M11 and later.
- **Desmos** (desmos.com/calculator): graphing from M08.

---

## Connections

- **Before:** nothing. This is the start.
- **Alongside:** [English foundations](../english/overview.md) in English sessions. [01 Intro CS Taste](../../01-intro-cs-taste/overview.md) starts after M01.
- **After:** [03 Discrete Math](../../03-discrete-math/overview.md) (logic, proof, counting, modular arithmetic) after M08. [12 Math for Engineering](../../12-math-for-engineering/overview.md) (calculus, linear algebra, probability) after M11.

| Later need | Comes from |
| :-- | :-- |
| Binary and hex in CPUs, memory dumps, colours | M01–M02 |
| `%` and integer division in hashing, ring buffers, checksums | M03 |
| Cryptography (Module 03) | M04 |
| Bandwidth, throughput, unit conversions | M06 |
| Signed integers, bit widths, memory sizes | M07 |
| Modelling performance, solving for unknowns | M08–M09 |
| Layout boxes, graphics coordinates | M10 |
| Algorithm speed (log n, n², 2ⁿ) | M11 |

---

## Track assessment

When you finish M11, take this cold, in one sitting (checkpoint id `FND-MA-ASSESS`; no calculator for part 1):

1. **Arithmetic (no calculator, 30 problems):** mixed whole numbers, fractions, decimals, percents, negatives, exponents, order of operations. Target: **27/30**.
2. **Algebra (10 problems):** equations, inequalities, a system, a word problem.
3. **Model:** given 6 data points from a real price list, build a linear model, graph it, and predict a 7th.
4. **Geometry and functions (6 problems):** area, Pythagoras, one trig problem, one exponential, one logarithm, one sum.
5. **Explain (written, 300 words):** pick any two of — why carrying works, why invert-and-multiply works, why (−1)×(−1)=1, what log₂(1024) means — and explain them for a beginner.

Use OpenStax chapter reviews or Khan unit tests to assemble parts 1, 2, and 4 (choose problems you haven't seen; mix them yourself).

**Done when:** part 1 ≥ 27/30 and parts 2–5 complete with at most 3 total errors. If not, note the weakest stage, work through its practice sets again, and retake that part.
