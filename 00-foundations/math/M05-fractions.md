---
title: "M05 — Fractions"
stage: M05
track: math
hours: 35
weeks: 5
---

# M05 — Fractions

**In this stage you will:** understand what a fraction *is* (four ways), make equivalent fractions and simplify them, compare fractions, and add, subtract, multiply, and divide them, knowing exactly why each procedure works. "Invert and multiply" will stop being a magic spell.

**Time:** about 35 hours over 5 weeks. This is the stage most adults find hardest, and the one that unlocks everything after it. Take your time.

**Before you start:** M04 done. You can find a GCD and an LCM quickly.

---

## Diagnostic (cold, 25 minutes, no calculator)

1. Simplify 18/24.
2. Which is bigger: 5/8 or 3/5?
3. 2/3 + 1/4
4. 5/6 − 1/4
5. 3/4 × 2/9
6. 3/4 ÷ 3/8
7. 2½ × 1⅓
8. What is 3/5 of 40?
9. Write 17/5 as a mixed number.
10. How many ¼-cup scoops are in 3 cups?

<details>
<summary>Answers (diagnostic)</summary>

1. 3/4 · 2. 5/8 (25/40 vs 24/40) · 3. 11/12 · 4. 7/12 · 5. 1/6 · 6. 2 · 7. 3⅓ (= 10/3) · 8. 24 · 9. 3⅖ · 10. 12

All correct *and* you can explain why 6 works: skim to Part 7 and the practice sets.
</details>

---

## Why this matters

Fractions are where most people's math confidence breaks, because they were taught as rules without reasons. "Find a common denominator." "Invert and multiply." "Cross-multiply." Rules without reasons are easy to mix up and impossible to rebuild when forgotten.

This stage rebuilds fractions from their meaning, so every rule becomes something you can work out again on a blank page.

Fractions matter later because:
- every **rate** (bytes per second, pixels per inch, errors per thousand packets) is a fraction;
- **probability** (Module 03, 12) is fractions;
- **algebra** (M08) does to letters exactly what this stage does to numbers;
- computers represent fractions in **binary**, which is why `0.1 + 0.2` gives `0.30000000000000004` in Python. You'll understand why by the end of M06, starting from Part 9 here.

---

## Part 1 — What a fraction is

The fraction **a/b** (say "a over b") has four meanings. They are all the same number, seen from different sides.

| Meaning | 3/4 is… |
| :-- | :-- |
| **Parts of a whole** | Cut a whole into 4 equal pieces; take 3 of them. |
| **Division** | 3 ÷ 4. Share 3 pizzas among 4 people: each gets 3/4 of a pizza. |
| **A point on the number line** | Split the gap from 0 to 1 into 4 equal steps; 3/4 is 3 steps from 0. |
| **A ratio** (M06) | 3 for every 4. |

**The parts:**
- The bottom number, the **denominator**, says **what size the pieces are** (quarters, eighths, thirds). It *names* the unit.
- The top number, the **numerator**, says **how many** of those pieces you have. It *counts*.

This one idea — **the denominator is a unit, the numerator counts units** — explains almost every rule in this stage. Underline it.

**Fractions bigger than 1:** 7/4 means seven quarters. That's one whole (4 quarters) plus 3 quarters: **1¾**. A fraction with top ≥ bottom is called **improper**; 1¾ is a **mixed number**.

**Converting:**
- Improper → mixed: divide. 17/5: 17 ÷ 5 = 3 remainder 2 → **3⅖**.
- Mixed → improper: whole × bottom + top. 3⅖ = (3 × 5 + 2)/5 = **17/5**.

---

## Part 2 — Equivalent fractions

**1/2 = 2/4 = 3/6 = 4/8.** Why? Cut each half into 2 smaller pieces: you have 2 pieces, each a quarter. Same amount, smaller pieces, more of them.

**Rule:** multiplying (or dividing) the top **and** the bottom by the same number gives an equal fraction.

> **[W] Why must you do the same to top and bottom?**
> 1. Multiplying the bottom by 3 cuts every piece into 3 smaller pieces, so each piece is ⅓ the size.
> 2. To keep the same amount, you need 3 times as many of the smaller pieces: multiply the top by 3.
> 3. Do only one, and the amount changes. (2/3 → 2/9 is a much smaller amount: same count, smaller pieces.)

### Simplifying

To write a fraction in **simplest form**, divide top and bottom by their GCD (M04).

*Worked example:* **84/126**
1. GCD(84, 126) = 42 (Euclid: 126 mod 84 = 42; 84 mod 42 = 0).
2. 84 ÷ 42 = 2, 126 ÷ 42 = 3 → **2/3**.

(If you don't see the GCD right away, divide by any common factor and repeat: 84/126 → ÷2 → 42/63 → ÷21 → 2/3.)

---

## Part 3 — Comparing fractions

| Situation | Method | Example |
| :-- | :-- | :-- |
| Same denominator | Compare numerators (same-size pieces; more is more) | 5/8 > 3/8 |
| Same numerator | The smaller denominator is bigger (fewer pieces → each is bigger) | 3/5 > 3/8 |
| Different both ways | Rewrite with a common denominator | 5/8 vs 3/5 → 25/40 vs 24/40 → 5/8 is bigger |
| Quick check | Compare to a benchmark like ½ or 1 | 4/9 < ½ < 5/8 |

**Cross-multiplication shortcut:** to compare a/b and c/d, compare a × d with c × b. For 5/8 vs 3/5: 5 × 5 = 25 vs 3 × 8 = 24, so 5/8 is bigger. *Why it works:* a × d and c × b are exactly the numerators you'd get using the common denominator b × d. It's the common-denominator method without writing the denominator.

---

## Part 4 — Adding and subtracting

**You can only add things measured in the same unit.** 2 metres + 3 centimetres is not 5 of anything. The denominator is the unit, so:

**Subgoal labels [S]:**
1. **Make the units the same:** find a common denominator (the LCM of the denominators is the smallest one).
2. **Rewrite each fraction** with that denominator (multiply top and bottom by the same number).
3. **Add or subtract the numerators** (you're counting pieces of the same size). Keep the denominator.
4. **Simplify**, and convert to a mixed number if helpful.

*Worked example:* **3/4 + 1/6**
1. LCM(4, 6) = 12.
2. 3/4 = 9/12; 1/6 = 2/12.
3. 9/12 + 2/12 = **11/12**.
4. Already simple.

*Worked example (mixed numbers):* **2⅓ − 1¾**
1. Convert to improper: 7/3 − 7/4.
2. LCM(3, 4) = 12: 28/12 − 21/12.
3. = **7/12**.

> **The classic error:** 1/2 + 1/3 = 2/5 (adding tops and bottoms). Look back [Pólya step 4]: 2/5 is *less* than 1/2, but we added something positive to 1/2. Impossible. The right answer is 3/6 + 2/6 = **5/6**. Estimating catches this error every time.

> **[W] Why don't we add the denominators?** Because the denominator isn't a count; it's the size of the pieces. Adding two quarter-pieces gives two quarters (2/4), not two eighths. Adding the bottoms would mean the pieces somehow got smaller by being put together.

---

## Part 5 — Multiplying

**"Of" means multiply.** ½ of 8 is 4 = ½ × 8. ⅔ of ¾ is ⅔ × ¾.

**Rule:** multiply tops, multiply bottoms: (a/b) × (c/d) = (a × c)/(b × d).

**Why — the area model.** Draw a square of side 1. Shade ¾ of it with vertical lines (4 columns, shade 3). Now shade ⅔ of it with horizontal lines (3 rows, shade 2). The square is cut into 4 × 3 = **12** small pieces (that's the new denominator). The overlap — ⅔ of the ¾ — is 3 × 2 = **6** pieces. So ⅔ × ¾ = 6/12 = **½**.

```
     ┌────┬────┬────┬────┐
     │▓▓▓▓│▓▓▓▓│▓▓▓▓│    │   ▓ = overlap (2/3 of 3/4)
     ├────┼────┼────┼────┤
     │▓▓▓▓│▓▓▓▓│▓▓▓▓│    │   6 of 12 pieces
     ├────┼────┼────┼────┤
     │░░░░│░░░░│░░░░│    │   ░ = 3/4 only
     └────┴────┴────┴────┘
```

**Subgoal labels [S]:**
1. **Convert** mixed numbers to improper fractions. (Whole numbers: n = n/1.)
2. **Cancel** any factor shared by a top and a bottom (even diagonally) — this keeps numbers small.
3. **Multiply** tops; multiply bottoms.
4. **Simplify**; convert back to mixed if helpful.

*Worked example:* **7/12 × 18/35**
1. Already fractions.
2. Cancel 7 with 35 (÷7 → 1 and 5). Cancel 18 with 12 (÷6 → 3 and 2). Now: 1/2 × 3/5.
3. = **3/10**.

*Worked example:* **2¼ × 1⅓** = 9/4 × 4/3 → cancel 4s and 9/3 → 3/1 × 1/1 = **3**.

**Notice:** multiplying by a fraction **less than 1** makes things **smaller** (½ × 8 = 4). "Multiplication makes bigger" is only true for numbers above 1.

---

## Part 6 — Dividing (and why "invert and multiply" works)

Go back to the **measuring** meaning of division from M03: *a ÷ b asks "how many b's fit into a?"*

- 3 ÷ ¼: how many quarter-cups fit in 3 cups? Each cup holds 4 quarters, so 3 cups hold **12**. And notice: 3 × 4 = 12. Dividing by ¼ is the same as multiplying by 4.
- ¾ ÷ ⅛: how many eighths fit in three-quarters? ¾ = 6/8, so **6**. And ¾ × 8 = 6.

**Method 1 — common denominator (shows the meaning):**
Write both with the same denominator; then the question is just "how many of these pieces fit into those pieces?"
> ¾ ÷ ⅙ = 9/12 ÷ 2/12 = "how many 2-twelfths fit in 9-twelfths?" = 9 ÷ 2 = **9/2** = 4½.

**Method 2 — invert and multiply (fast):**
> (a/b) ÷ (c/d) = (a/b) × (d/c)

**Subgoal labels [S]:**
1. **Convert** mixed numbers to improper fractions.
2. **Keep** the first fraction.
3. **Flip** the second fraction (swap its top and bottom; this is called its **reciprocal**).
4. **Multiply** (cancelling first).
5. **Look back:** is the size sensible? Dividing by something less than 1 should give a *bigger* answer.

*Worked example:* **3½ ÷ 1¾**
1. 7/2 ÷ 7/4. 2–3. 7/2 × 4/7. 4. Cancel 7s; 4/2 = **2**. 5. Does 1¾ fit into 3½ twice? 1¾ + 1¾ = 3½ ✓

> **[W] Why does invert-and-multiply work?** (The why-ladder from [study-protocols](../../study-protocols.md#w--why-ladder).)
> 1. A division doesn't change if you multiply both numbers by the same thing. (12 ÷ 3 = 24 ÷ 6 = 4: twice as much stuff, pieces twice as big, same count.)
> 2. So multiply both parts of (a/b) ÷ (c/d) by d/c: you get (a/b × d/c) ÷ (c/d × d/c).
> 3. But c/d × d/c = 1. So it's (a/b × d/c) ÷ 1, which is just **a/b × d/c**. The "invert" makes the divisor become 1, and dividing by 1 does nothing.
>
> And the meaning: dividing by ⅛ asks how many eighths fit; there are 8 in every whole, so multiply by 8.

---

## Part 7 — Fractions of quantities, and word problems

**"Fraction of an amount"** = multiply. ⅗ of 40 = ⅗ × 40 = 120/5 = **24**. (Or: 40 ÷ 5 = 8 per fifth, × 3 = 24.)

**Which operation?** [Pólya step 2]

| The problem says… | Operation |
| :-- | :-- |
| "a fraction **of**" | × |
| "**how many** ___ fit / can you make" | ÷ |
| "**combined**, total" | + |
| "how much **more**, how much **left**" | − |
| "**each** gets" (sharing) | ÷ |
| "**scale** a recipe by" | × |

*Worked example:* A cable is 7½ m long. How many ¾-m pieces can you cut?
1. Understand: total 7½ m, piece ¾ m, want number of pieces. 2. "How many fit" → ÷. 3. 15/2 ÷ 3/4 = 15/2 × 4/3 = 60/6 = **10 pieces**. 4. Look back: ¾ m is less than 1 m, so we expect more than 7 pieces ✓.

---

## Part 8 — Fractions in Python

Python can do exact fraction arithmetic. After [01 Lab 01](../../01-intro-cs-taste/labs/lab-01-python-first-steps.md), try:

```python
from fractions import Fraction as F
print(F(3, 4) + F(1, 6))     # 11/12
print(F(7, 2) / F(7, 4))     # 2
print(F(84, 126))            # 2/3  (simplifies automatically)
```

Use this to **check** your hand answers, never to replace them. (In [Ratio Workshop](projects/ratio-workshop/spec.md) you'll use it in a real program.)

---

## Part 9 — A preview: fractions in binary

In base 10, places to the right of the point are tenths, hundredths, thousandths (M06). In **binary**, they are **halves, quarters, eighths, sixteenths**:

| Binary | Value |
| :-- | :-- |
| 0.1₂ | ½ |
| 0.01₂ | ¼ |
| 0.11₂ | ½ + ¼ = ¾ |
| 0.001₂ | ⅛ |
| 0.101₂ | ½ + ⅛ = ⅝ |

So fractions whose denominator is a power of 2 have short, exact binary forms. But **⅓** can't be written exactly in binary (just as it can't in decimal: 0.333…). Neither can **1/10**! That surprising fact is the root of the famous `0.1 + 0.2 != 0.3` puzzle you'll solve in M06.

---

## Practice routine (5 weeks)

| Week | Focus |
| :-- | :-- |
| 1 | Mon: four meanings (draw each for 3/4, 2/5, 7/4) · Tue: improper and mixed · Wed–Thu: equivalent fractions and simplifying · Fri: comparing |
| 2 | Mon–Wed: adding and subtracting (with drawings first, then the procedure) · Thu: mixed numbers · Fri: Practice Set 1, items 1–9 |
| 3 | Mon–Tue: multiplying (area model by hand for 5 problems before using the rule) · Wed–Fri: dividing: measuring meaning, both methods, the why-ladder |
| 4 | Mon: fractions of amounts · Tue–Wed: word problems · Thu–Fri: Practice Set 1 rest + Set 2 |
| 5 | Mon–Tue: [Ratio Workshop](projects/ratio-workshop/spec.md) Milestone 1 · Wed: Feynman pass · Thu: blank sheet + error-log review · Fri: self-check |

**Daily warm-up [R]:** pick one operation (rotate daily). Write its subgoal labels from memory and its *why* in one sentence. Do one problem.

**Key why-questions [W]:**
1. Why must you do the same to the top and bottom to get an equivalent fraction?
2. Why do you need a common denominator to add, but not to multiply?
3. Why does multiplying by ½ make a number smaller?
4. Why does invert-and-multiply work? (All three rungs.)

**Feynman target [F]:** *"Why does dividing by ⅓ triple a number?"* Explain it with measuring cups, out loud, in 2 minutes. Then explain invert-and-multiply in plain words.

**Interleaving warning [I]:** the most common fraction errors come from using the right procedure on the wrong operation (adding denominators, finding a common denominator to multiply). That's why every practice set mixes all four operations. Before each problem, **name the operation and its first step** before writing anything.

---

## Practice sets

### Practice Set 1 — Mixed (20 problems, no calculator)

1. Simplify 45/60.
2. Simplify 84/126.
3. 3/7 = ?/35
4. Order from smallest to largest: 2/3, 5/8, 3/4, 7/12.
5. 1/2 + 1/3
6. 3/8 + 5/12
7. 7/10 − 1/4
8. 3¼ + 2⅔
9. 4 − 1⅝
10. 2/5 × 3/4
11. 6 × 5/8
12. 7/12 × 18/35
13. 2¼ × 1⅓
14. 5 ÷ ⅓
15. ¾ ÷ ⅛
16. ⅔ ÷ 4/9
17. 3½ ÷ 1¾
18. ⅜ of 64
19. A recipe needs ⅔ cup of sugar. You make 1½ batches. How much sugar?
20. A cable is 7½ m long. How many ¾-m pieces can you cut from it?

<details>
<summary>Answers (Set 1)</summary>

1. 3/4 · 2. 2/3 · 3. 15 · 4. 7/12, 5/8, 2/3, 3/4 (common denominator 24: 14, 15, 16, 18) · 5. 5/6 · 6. 19/24 · 7. 9/20 · 8. 5 11/12 (= 71/12) · 9. 2⅜ (= 19/8) · 10. 3/10 · 11. 3¾ (= 15/4) · 12. 3/10 · 13. 3 · 14. 15 · 15. 6 · 16. 3/2 = 1½ · 17. 2 · 18. 24 · 19. 1 cup · 20. 10
</details>

### Practice Set 2 — Think about it (5 problems)

1. Draw a picture showing why 2/3 = 4/6.
2. A student wrote 1/2 + 1/3 = 2/5. Explain, using estimation, why this must be wrong. Then explain what they misunderstood about the denominator.
3. Explain why ¾ ÷ ⅛ = 6 using only the "how many fit" meaning. No rules.
4. Why does multiplying a number by a fraction less than 1 make it smaller? Use the area model or "of."
5. What is 0.1₂ as a fraction? 0.11₂? 0.111₂? Can ⅓ be written as a binary fraction with a finite number of digits? Why or why not?

<details>
<summary>Answers (Set 2)</summary>

1. Draw a bar cut into 3 equal parts, shade 2. Now cut every part in half: 6 parts, 4 shaded. Same shaded area.
2. 2/5 is less than 1/2, but adding 1/3 to 1/2 should make it bigger. They treated the denominators as counts and added them; but denominators are piece sizes, and pieces don't shrink when you combine them.
3. ¾ is the same as 6/8, six eighth-pieces. So 6 eighths fit into ¾.
4. "½ × 8" means "half of 8": you take part of 8, so you get less than 8. In the area model, multiplying by a fraction less than 1 keeps only part of the rectangle.
5. ½; ¾; ⅞. No: ⅓ would need a denominator that's a power of 2, and no power of 2 is a multiple of 3, so the binary digits repeat forever (0.010101…₂). This is exactly why computers can't store some simple fractions exactly.
</details>

---

## Self-check (cold, 35 minutes, no calculator)

1. Simplify 72/90.
2. Which is bigger: 7/9 or 4/5? Show how you know.
3. 5/6 + 3/8
4. 4⅓ − 2¾
5. 8/15 × 5/12
6. 5/6 ÷ 5/12
7. 2⅔ ÷ 4
8. A phone battery is ¾ full. You use ⅓ of a full charge. What fraction of a full charge is left?
9. A movie is 2¼ hours long. You watched ⅗ of it. How many minutes did you watch?
10. **[R] Blank sheet (10 min):** the four meanings of a fraction; what the denominator and numerator do; the subgoal labels for all four operations; the why-ladder for invert-and-multiply.

<details>
<summary>Answers (self-check)</summary>

1. 4/5 · 2. 4/5 (cross-multiply: 7 × 5 = 35 vs 4 × 9 = 36) · 3. 29/24 = 1 5/24 · 4. 19/12 = 1 7/12 · 5. 2/9 · 6. 2 · 7. 2/3 · 8. 5/12 · 9. 2¼ hours = 135 minutes; ⅗ × 135 = 81 minutes
</details>

## Done when

- [ ] Self-check ≥ 8/9 on items 1–9, blank sheet done.
- [ ] Four why-questions answered; invert-and-multiply explained out loud.
- [ ] Your error log shows no repeated "concept" errors on fractions in the last week.
- [ ] [Ratio Workshop](projects/ratio-workshop/spec.md) Milestone 1 done.

**Next:** [M06 — Decimals, Percents, and Ratios](M06-decimals-percents-and-ratios.md).
