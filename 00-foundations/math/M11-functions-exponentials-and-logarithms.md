---
title: "M11 — Functions, Exponentials, and Logarithms"
stage: M11
track: math
hours: 35
weeks: 5
---

# M11 — Functions, Exponentials, and Logarithms

**In this stage you will:** work with quadratic functions (and derive the quadratic formula yourself), understand exponential growth and decay, learn what a logarithm *means* (it's a question, not a mystery), add up long sequences with two famous tricks, and compare how fast different functions grow — which is exactly how programmers judge whether an algorithm is fast.

**Time:** about 35 hours over 5 weeks.

**Before you start:** M10 done. Exponent laws (M07) and equations (M08) are solid.

---

## Diagnostic (cold, 25 minutes; calculator allowed for 3)

1. Solve x² − 5x + 6 = 0.
2. Expand (x + 3)(x − 2).
3. Solve 2x² + 3x − 2 = 0.
4. A population of 1,000 doubles every 3 years. How big is it after 12 years?
5. log₂ 64
6. log₁₀ 1,000,000
7. log₂ 1
8. 1 + 2 + 3 + … + 100
9. 1 + 2 + 4 + 8 + … + 512
10. You guess a secret number from 1 to 1,000,000; after each guess you're told "higher" or "lower." At most how many guesses do you need with the best strategy?

<details>
<summary>Answers (diagnostic)</summary>

1. x = 2 or x = 3 · 2. x² + x − 6 · 3. x = ½ or x = −2 · 4. 16,000 (4 doublings) · 5. 6 · 6. 6 · 7. 0 · 8. 5,050 · 9. 1,023 · 10. 20 (2²⁰ ≈ 1,000,000)
</details>

---

## Why this matters

This stage is about **how fast things grow**, and that is the central question of algorithm design.

| If an algorithm takes… | then for 1,000,000 items it takes about… |
| :-- | :-- |
| log₂ n steps | 20 steps |
| n steps | 1,000,000 steps |
| n² steps | 1,000,000,000,000 steps |
| 2ⁿ steps | more steps than there are atoms in the universe |

Every one of those functions is in this stage. When you analyse your search engine in Module 05, your route planner, or your database index in Module 11, you'll be using exactly these ideas: binary search is log₂ n; comparing every pair is about n²/2; trying every subset is 2ⁿ.

Exponentials and logarithms are also how engineers handle huge ranges: decibels for signal strength in networking and electronics, half-lives, interest, the growth of anything that compounds.

---

## Part 1 — Quadratics

A **quadratic** function has an x² term: f(x) = ax² + bx + c (with a ≠ 0). Its graph is a **parabola**: a U shape (opening up if a > 0, down if a < 0). Throw a ball, and its height over time is a quadratic.

### Expanding and factoring

**Expanding** two brackets uses the distributive law twice (M03's area model, one more time):

```
         x      +3
     +-------+------+
  x  |  x²   |  3x  |
     +-------+------+
 −2  | −2x   |  −6  |
     +-------+------+
(x + 3)(x − 2) = x² + 3x − 2x − 6 = x² + x − 6
```

**Factoring** goes backwards. For x² + bx + c, find two numbers that **multiply to c** and **add to b**.
> x² + 7x + 12: multiply to 12, add to 7 → 3 and 4 → **(x + 3)(x + 4)**.
> x² − 9 (a "difference of squares"): **(x − 3)(x + 3)**.

### Solving by factoring

**Subgoal labels [S]:**
1. **Rearrange** so one side is 0: ax² + bx + c = 0.
2. **Factor** the left side.
3. **Set each factor to 0** and solve.
4. **Check** each answer in the original.

> **[W] Why does step 3 work?** If two numbers multiply to 0, at least one of them must be 0. (No two non-zero numbers multiply to 0.) So (x − 2)(x − 3) = 0 means x − 2 = 0 or x − 3 = 0.

### The quadratic formula

Not every quadratic factors nicely. This formula always works:

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

**Deriving it yourself (completing the square).** Do this once slowly; it's the best why-ladder in the stage.
1. Start: ax² + bx + c = 0. Divide by a: x² + (b/a)x + c/a = 0.
2. Move the constant: x² + (b/a)x = −c/a.
3. **Complete the square:** (x + b/(2a))² = x² + (b/a)x + b²/(4a²). So add b²/(4a²) to both sides: (x + b/(2a))² = b²/(4a²) − c/a = (b² − 4ac)/(4a²).
4. Take the square root of both sides (± because both a positive and a negative number square to the same thing): x + b/(2a) = ±√(b² − 4ac) / (2a).
5. Subtract b/(2a): **x = (−b ± √(b² − 4ac)) / (2a)**. ∎

The part under the root, **b² − 4ac**, is the **discriminant**:
- positive → two solutions (the parabola crosses the x-axis twice)
- zero → one solution (it touches once)
- negative → no real solutions (it never reaches the x-axis)

*Worked example:* 2x² + 3x − 2 = 0. a = 2, b = 3, c = −2. Discriminant 9 + 16 = 25. x = (−3 ± 5)/4 → **x = ½ or x = −2**.

### Where quadratics show up in computing

**Comparing every pair.** n people each shake hands with every other person: n(n − 1)/2 handshakes. 20 people → 190. 1,000 → 499,500. An algorithm that compares every pair of items does about n²/2 work: fine for 1,000 items, painful for 1,000,000 (Module 05).

---

## Part 2 — Exponential growth and decay

**Linear** growth adds the same amount each step: 100, 110, 120, 130…
**Exponential** growth **multiplies** by the same amount each step: 100, 110, 121, 133.1… (×1.1 each time).

$$f(x) = a \cdot b^x$$

- a = starting value; b = growth factor per step; x = number of steps.
- b > 1: growth. 0 < b < 1: decay.

| Situation | Function |
| :-- | :-- |
| 1,000 people, doubling every 3 years, after t years | 1,000 × 2^(t/3) |
| $1,000 at 5% interest per year, compounded yearly, after n years | 1,000 × 1.05ⁿ |
| 80 mg of a drug, halving every 6 hours, after h hours | 80 × (½)^(h/6) |

*Worked example:* $1,000 at 5% for 3 years: 1,000 × 1.05³ = 1,000 × 1.157625 ≈ **$1,157.63**. (Not $1,150: each year's interest earns interest. That's M06's "successive percents multiply" trap, now as a formula.)

**The key fact:** exponential growth eventually beats **any** polynomial. 2ⁿ vs n²: at n = 10, 1,024 vs 100; at n = 20, about a million vs 400; at n = 100, 2¹⁰⁰ ≈ 10³⁰ vs 10,000. An algorithm that takes 2ⁿ steps is useless for large n no matter how fast your computer is.

> **[W] Why does doubling get so big so fast?** Fold a sheet of paper (0.1 mm thick) in half 42 times (you physically can't, but imagine it): 0.1 mm × 2⁴² ≈ 440,000 km, more than the distance to the Moon. Each doubling adds *as much as everything before it combined*: 1 + 2 + 4 + 8 = 15, and the next step is 16. (Part 5 proves this.)

---

## Part 3 — Logarithms: the question behind the exponent

A **logarithm** answers a question:

> **log₂ 64 = ?** means **"2 to what power is 64?"** Answer: 6, because 2⁶ = 64.

$$\log_b x = y \quad \text{means} \quad b^y = x$$

That's all a logarithm is: **the exponent you need**. The log undoes the exponential, the way subtraction undoes addition.

### The two most useful readings

- **log₂ n = "how many times can I halve n before I reach 1?"** (or "how many doublings from 1 to n?"). log₂ 1,024 = 10. log₂ 1,000,000 ≈ 20.
  - **Binary search:** halving the search range each guess finds one item among n in about log₂ n steps. That's why the guessing game takes 20 guesses for a million numbers.
  - **Bits needed:** to give n things different binary numbers, you need ⌈log₂ n⌉ bits (⌈ ⌉ means "round up"). 5,000 values → log₂ 5,000 ≈ 12.3 → **13 bits**. (M07, Practice Set 2, revisited.)
- **log₁₀ n ≈ "how many digits n has, minus 1"** (for whole numbers). log₁₀ 1,000,000 = 6, and 1,000,000 has 7 digits. log₁₀ 50 ≈ 1.7, between 1 (10) and 2 (100).

### Values to know

| | log₂ | log₁₀ |
| :-- | :-- | :-- |
| 1 | 0 | 0 |
| 2 / 10 | 1 | 1 |
| 1,024 / 1,000 | 10 | 3 |
| ≈ 10⁶ | ≈ 20 | 6 |
| ≈ 10⁹ | ≈ 30 | 9 |
| ½ / 0.1 | −1 | −1 |

### The laws of logarithms (and why)

Each law is an exponent law (M07) read backwards:

| Log law | Comes from | Example |
| :-- | :-- | :-- |
| log(xy) = log x + log y | bᵐ × bⁿ = bᵐ⁺ⁿ (multiplying adds exponents) | log₂(8 × 32) = 3 + 5 = 8 |
| log(x/y) = log x − log y | bᵐ ÷ bⁿ = bᵐ⁻ⁿ | log₁₀(1,000/10) = 3 − 1 = 2 |
| log(xⁿ) = n log x | (bᵐ)ⁿ = bᵐⁿ | log₂(4⁵) = 5 × 2 = 10 |
| log_b 1 = 0 | b⁰ = 1 | |
| change of base: log_b x = log x / log b | | log₂ 1,000 = log₁₀ 1,000 / log₁₀ 2 ≈ 3 / 0.301 ≈ 9.97 |

**In Python:** `math.log2(x)`, `math.log10(x)`, `math.log(x, base)`.

### Log scales and decibels

When values range over many powers of 10 (sound, signal strength, earthquakes), we use a **log scale**: equal steps mean equal *multiplications*.

**Decibels (dB)** compare two powers: dB = 10 × log₁₀(P₁/P₂).
- 10× the power = **+10 dB**. 1,000× = **+30 dB**. Half the power ≈ **−3 dB**.
- Your Wi-Fi signal strength (Module 09) is shown in dBm: −30 dBm is excellent, −70 dBm is weak, −90 dBm is barely usable. Each −10 dB is ten times less power.

---

## Part 4 — Sequences

A **sequence** is an ordered list of numbers.

- **Arithmetic:** add the same **difference** d each time: 3, 7, 11, 15, … (d = 4). The nth term is a + (n − 1)d. It's a linear function (M09) of n.
- **Geometric:** multiply by the same **ratio** r each time: 3, 6, 12, 24, … (r = 2). The nth term is a·rⁿ⁻¹. It's an exponential function of n.

---

## Part 5 — Sums: two famous tricks

### Trick 1: Gauss's pairing (arithmetic sums)

The story goes that young Carl Friedrich Gauss was told to add 1 + 2 + … + 100 and answered in seconds.

> Write the sum forwards and backwards:
> 1 + 2 + 3 + … + 100
> 100 + 99 + 98 + … + 1
> Each column adds to 101. There are 100 columns. So **twice** the sum is 100 × 101, and the sum is **5,050**.

**In general:** 1 + 2 + … + n = **n(n + 1)/2**. For any arithmetic sum: (number of terms) × (first + last) / 2.

*Worked example:* 3 + 7 + 11 + … + 39. Number of terms: (39 − 3)/4 + 1 = 10. Sum = 10 × (3 + 39)/2 = **210**.

**Why this matters:** a loop like this does 1 + 2 + … + n units of work:

```python
for i in range(n):
    for j in range(i):
        do_something()
```

That's n(n − 1)/2 calls: about n²/2. You'll use this exact count in Module 05.

### Trick 2: the binary sum (geometric sums)

$$1 + 2 + 4 + \dots + 2^{n-1} = 2^n - 1$$

*Why — two ways:*
1. **In binary**, 1 + 2 + 4 + … + 2ⁿ⁻¹ is the number 111…1 (n ones). Add 1, and it carries all the way: 1000…0 = 2ⁿ (M02's carry chain). So the sum is 2ⁿ − 1. With 8 bits: 11111111₂ = 255 = 2⁸ − 1.
2. **Algebra:** let S = 1 + 2 + … + 2ⁿ⁻¹. Then 2S = 2 + 4 + … + 2ⁿ. Subtract: 2S − S = 2ⁿ − 1 (everything else cancels). So **S = 2ⁿ − 1**.

**General geometric sum:** a + ar + … + arⁿ⁻¹ = **a(rⁿ − 1)/(r − 1)**. Example: 1 + 3 + 9 + … + 3⁵ = (3⁶ − 1)/2 = **364**.

**Why this matters:** "each doubling adds as much as everything before" (Part 2). It's also why a dynamic array that doubles its size when full does only about 2n copying work in total for n insertions — you'll prove and use this in Module 05.

### Summation notation

$$\sum_{i=1}^{n} i = 1 + 2 + \dots + n$$

Read: "the sum, for i from 1 to n, of i." It's a `for` loop in math clothes:

```python
total = 0
for i in range(1, n + 1):
    total += i
```

---

## Part 6 — Comparing growth

Put it all together. For each function, how big at n = 10, 1,000, and 1,000,000?

| Function | n = 10 | n = 1,000 | n = 1,000,000 | Example algorithm (Module 05) |
| :-- | --: | --: | --: | :-- |
| 1 (constant) | 1 | 1 | 1 | look up an array item by index |
| log₂ n | ≈ 3.3 | ≈ 10 | ≈ 20 | binary search |
| n | 10 | 1,000 | 1,000,000 | scan a list once |
| n log₂ n | ≈ 33 | ≈ 10,000 | ≈ 20,000,000 | good sorting |
| n² | 100 | 1,000,000 | 10¹² | compare every pair |
| 2ⁿ | 1,024 | ≈ 10³⁰¹ | (unimaginable) | try every subset |

At a billion simple steps per second: n² at n = 1,000,000 takes about 17 minutes; n log n takes 0.02 seconds. **Choosing the algorithm matters more than buying a faster computer.** This table is the reason [Module 05](../../05-data-structures-and-algorithms/overview.md) exists.

---

## Practice routine (5 weeks)

| Week | Focus |
| :-- | :-- |
| 1 | Mon: expanding (area model) · Tue: factoring · Wed: solving by factoring (and why) · Thu: derive the quadratic formula, slowly, twice · Fri: Practice Set 1, items 1–10 |
| 2 | Mon–Tue: exponential growth and decay · Wed: compound interest and the successive-percent trap · Thu: exponential vs polynomial (make the table yourself) · Fri: Practice Set 1, items 11–12 |
| 3 | Mon–Tue: logarithms as questions; the two readings · Wed: log laws from exponent laws · Thu: decibels and bits · Fri: Practice Set 1, items 13–19 |
| 4 | Mon: sequences · Tue: Gauss's pairing · Wed: the binary sum, both proofs · Thu: summation notation as loops · Fri: Practice Set 1 rest + Set 2 |
| 5 | Mon–Wed: [Growth and Halving Lab](projects/growth-and-halving-lab/spec.md) · Thu: Feynman · Fri: self-check, then the [track assessment](overview.md#track-assessment) next week |

**Daily warm-up [R]:** write the definition of a logarithm, three log facts, and one growth comparison from memory.

**Key why-questions [W]:**
1. Why does "product = 0" let you split a factored equation?
2. Why does completing the square lead to the quadratic formula? (All five steps.)
3. Why does log(xy) = log x + log y?
4. Why does 1 + 2 + 4 + … + 2ⁿ⁻¹ = 2ⁿ − 1? (Both proofs.)

**Feynman target [F]:** *"What is a logarithm?"* No formulas allowed for the first minute. Use halving and the guessing game. Then explain why binary search is fast.

---

## Practice sets

### Practice Set 1 — Mixed (22 problems; calculator allowed for 7, 11, and to check)

1. Expand (x − 4)(x + 4).
2. Expand (2x + 1)².
3. Factor x² + 7x + 12.
4. Factor x² − 9.
5. Solve x² + 7x + 12 = 0.
6. Solve x² = 2x + 15.
7. Solve x² − 4x + 1 = 0 with the formula. Give exact and decimal answers.
8. How many real solutions does x² + 2x + 5 = 0 have? How do you know without solving?
9. A ball's height is h = −5t² + 20t metres after t seconds. When does it land? What's its greatest height (hint: halfway between the landing times)?
10. How many handshakes happen when 20 people each shake hands once with everyone else?
11. $1,000 at 5% per year, compounded yearly. Value after 3 years?
12. A drug's amount halves every 6 hours. Starting from 80 mg, how much is left after 24 hours?
13. Solve 3ˣ = 81.
14. log₂ 1,024
15. log₁₀ 0.001
16. log₃ 81
17. log₂(8 × 32) using a log law.
18. How many bits do you need to give 5,000 items different numbers?
19. A signal's power increases 1,000-fold. How many decibels is that?
20. 1 + 2 + 3 + … + 50
21. 3 + 7 + 11 + … + 39
22. 1 + 3 + 9 + … + 3⁵

<details>
<summary>Answers (Set 1)</summary>

1. x² − 16 · 2. 4x² + 4x + 1 · 3. (x + 3)(x + 4) · 4. (x − 3)(x + 3) · 5. x = −3 or −4 · 6. x = 5 or −3 · 7. x = 2 ± √3 ≈ 3.732 or 0.268 · 8. None: the discriminant 4 − 20 = −16 is negative · 9. Lands at t = 4 s (and starts at t = 0); greatest height at t = 2: −20 + 40 = 20 m · 10. 190 · 11. ≈ $1,157.63 · 12. 5 mg (4 halvings) · 13. x = 4 · 14. 10 · 15. −3 · 16. 4 · 17. 3 + 5 = 8 · 18. 13 (2¹² = 4,096 is too few; 2¹³ = 8,192) · 19. 30 dB · 20. 1,275 · 21. 210 · 22. 364
</details>

### Practice Set 2 — Think about it (4 problems)

1. Algorithm A takes n² steps. Algorithm B takes 100n steps. Which is faster for n = 50? For n = 1,000? At what n are they equal?
2. A dynamic array starts with room for 1 item and doubles its room whenever it's full, copying everything over. After inserting 1,024 items, how many copies were made in total (from all the doublings)? Use the binary sum.
3. Explain, with the halving picture, why log₂ of a number between 512 and 1,024 is between 9 and 10.
4. A friend says "a 3 dB increase doubles the volume you hear." What does +3 dB double, exactly? (Hint: 10 × log₁₀ 2 ≈ 3.)

<details>
<summary>Answers (Set 2)</summary>

1. n = 50: A = 2,500, B = 5,000 → **A** is faster. n = 1,000: A = 1,000,000, B = 100,000 → **B** is faster. Equal when n² = 100n → **n = 100**. For big inputs, the lower growth rate always wins eventually.
2. Doublings happen at sizes 1, 2, 4, …, 512, copying that many items each time: 1 + 2 + 4 + … + 512 = 2¹⁰ − 1 = **1,023 copies**. That's less than 1 copy per item on average.
3. 512 = 2⁹ and 1,024 = 2¹⁰. A number between them needs more than 9 halvings but fewer than 10 to reach 1.
4. +3 dB doubles the **power** (since 10 log₁₀ 2 ≈ 3). Human hearing doesn't perceive double power as double loudness (that takes about +10 dB). "Doubling" depends on what you measure.
</details>

---

## Self-check (cold, 35 minutes; calculator for 2 and 5)

1. Factor and solve x² − x − 12 = 0.
2. Solve 3x² − 2x − 1 = 0 with the quadratic formula.
3. 50 bacteria double every 20 minutes. How many after 2 hours?
4. log₂ 4,096
5. Between which two whole numbers is log₁₀ 50? Then find it with a calculator.
6. How many steps does binary search need, at most, for 1,000,000 sorted items?
7. 1 + 2 + … + 1,000
8. 1 + 2 + 4 + … + 2¹⁵
9. Compare n² and 2ⁿ at n = 10 and at n = 20.
10. **[R] Blank sheet (15 min):** expanding and factoring; the quadratic formula derivation; exponential vs linear growth; the definition of a logarithm with both readings; the log laws with reasons; Gauss's pairing; the binary sum with both proofs; the growth table.

<details>
<summary>Answers (self-check)</summary>

1. (x − 4)(x + 3) = 0 → x = 4 or x = −3 · 2. x = (2 ± √16)/6 → x = 1 or x = −⅓ · 3. 6 doublings: 50 × 64 = 3,200 · 4. 12 · 5. Between 1 and 2; ≈ 1.699 · 6. 20 · 7. 500,500 · 8. 2¹⁶ − 1 = 65,535 · 9. n = 10: 100 vs 1,024; n = 20: 400 vs 1,048,576
</details>

## Done when

- [ ] Self-check ≥ 8/9 on items 1–9, blank sheet done.
- [ ] You can derive the quadratic formula on a blank page.
- [ ] Four why-questions answered; Feynman recording made.
- [ ] [Growth and Halving Lab](projects/growth-and-halving-lab/spec.md) complete.
- [ ] The math [track assessment](overview.md#track-assessment) passed.

**Next:** [12 Math for Engineering](../../12-math-for-engineering/overview.md) (calculus, linear algebra, probability) when the build modules call for it, and [03 Discrete Math](../../03-discrete-math/overview.md) if you haven't finished it. Math stays a daily habit: 20–30 minutes of mixed review from your error log and old practice sets on weekday mornings.
