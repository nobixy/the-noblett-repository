---
title: "M08 — Algebra: Expressions and Equations"
id: "M08"
type: "lesson"
module: "00-foundations"
track: "math"
stage: "M08"
phase: "B"
order: 370
prerequisites: [M07]
---

# M08 — Algebra: Expressions and Equations

**In this stage you will:** use letters to stand for numbers; evaluate and simplify expressions; solve equations by keeping them balanced; rearrange formulas; solve inequalities (and know why the sign flips); and turn word problems into equations. Algebra is arithmetic with the numbers you don't know yet.

**Before you start:** M07 done. Negative numbers and order of operations are solid. Fractions (M05) are solid.

---

## Diagnostic (cold)

1. Evaluate 3x² − 2x + 5 when x = −2.
2. Simplify 4a + 3b − a + 5b.
3. Expand 3(2x − 5).
4. Solve 5x − 7 = 18.
5. Solve 3(x + 4) = 2x − 1.
6. Solve x/4 + 2 = 7.
7. Solve 2x − 3 < 9.
8. Solve −3x ≥ 12.
9. Rearrange d = rt to find t.
10. A number is doubled and then 7 is added. The result is 31. What is the number?

<details>
<summary>Answers (diagnostic)</summary>

1. 21 · 2. 3a + 8b · 3. 6x − 15 · 4. x = 5 · 5. x = −13 · 6. x = 20 · 7. x < 6 · 8. x ≤ −4 · 9. t = d/r · 10. 12
</details>

---

## Why this matters

Algebra is the tool for reasoning about quantities you don't know yet. It's how you answer engineering questions like:
- "How big can the file be if the transfer must finish in 10 seconds?"
- "At what number of users does plan B become cheaper than plan A?"
- "What resistor value gives this voltage?"

It's also the mental model behind programming. A **variable** in code and a variable in algebra are close cousins, and a **function** (M09) in code and in math are the same idea. But there's one important difference, and getting it straight now saves real confusion later (Part 1).

From here, math becomes the language of every later module: [03 Discrete Math](../../03-discrete-math/overview.md) starts after this stage.

---

## Part 1 — Variables and expressions

A **variable** is a letter that stands for a number: either an unknown we want to find, or a quantity that can change. *x*, *n*, *t* (time), *v* (voltage).

An **expression** is a combination of numbers, variables, and operations, with no equals sign: 3x² − 2x + 5.

- **Terms** are the parts joined by + or −: 3x², −2x, 5.
- The **coefficient** is the number in front of a variable: 3 in 3x², −2 in −2x.
- A **constant** is a term with no variable: 5.
- **Writing rules:** 3x means 3 × x. x² means x × x. 3x² means 3 × (x²), not (3x)².

### Algebra's `=` vs code's `=`

| | Algebra | Python |
| :-- | :-- | :-- |
| `x = 5` | a **statement**: x is equal to 5 (true or false) | an **instruction**: put 5 into the box called x |
| `x = x + 1` | a statement with **no solution** (no number equals itself plus 1) | an instruction: take x's value, add 1, put it back |
| equality test | `=` | `==` |

In algebra, `=` is a **claim that two things are equal**. In most programming languages, `=` is **assignment**. Keep the two apart and you'll never be confused by either.

### Evaluating (substituting a value)

**Subgoal labels [S]:**
1. **Replace** each variable with its value, **in brackets** (this protects negative signs).
2. **Compute** using the order of operations (M07).

*Worked example:* 3x² − 2x + 5 when x = −2
1. 3(−2)² − 2(−2) + 5
2. Exponent: (−2)² = 4 → 3·4 − 2(−2) + 5 → multiply: 12 + 4 + 5 → **21**

(Without the brackets, you might compute −2² = −4 and get it wrong. That's M07's trap.)

---

## Part 2 — Simplifying expressions

### Like terms

**Like terms** have exactly the same variable part: 4a and −a are like terms; 3b and 5b are like terms; 4a and 3b are not; x and x² are not.

**You can only combine like terms.** Add their coefficients:
> 4a + 3b − a + 5b = (4a − a) + (3b + 5b) = **3a + 8b**

> **[W] Why can't you combine 3a + 8b?** It's the same reason you can't add 3/4 + 8/5 without a common denominator (M05), or 3 metres + 8 seconds. *a* and *b* are different **units**. 3a means "3 of the thing called a." You can count a's together, and b's together, but not a's with b's.

### The distributive law, again

M03's rectangle, now with letters:
> 3(2x − 5) = 3·2x − 3·5 = **6x − 15**
> −2(x − 4) = −2x + 8 (the −2 multiplies both terms: −2 × −4 = +8)

**Subgoal labels [S] for simplifying:**
1. **Expand** all brackets (distributive law; watch the signs).
2. **Group** like terms.
3. **Combine** each group.

*Worked example:* 5(y − 2) − 3(y + 1)
1. 5y − 10 − 3y − 3 (the −3 multiplies both y and +1)
2. (5y − 3y) + (−10 − 3)
3. **2y − 13**

### Factoring out (the distributive law backwards)

> 12x + 18 = 6(2x + 3) (6 is the GCD of 12 and 18 — M04)

Check by expanding. You'll use factoring constantly in M11.

---

## Part 3 — Solving equations: the balance

An **equation** says two expressions are equal: 5x − 7 = 18. **Solving** means finding the value(s) of the variable that make it true.

**Picture a balance scale.** Both sides weigh the same. You may do anything you like, **as long as you do the same thing to both sides**, and the scale stays balanced.

**The goal:** get the variable alone on one side.
**The method:** undo what was done to the variable, in reverse order, using inverse operations (+ undoes −, × undoes ÷).

**Subgoal labels [S]:**
1. **Clear brackets** (expand) and **fractions** (multiply both sides by the common denominator).
2. **Collect** variable terms on one side and constants on the other (add or subtract the same thing on both sides).
3. **Combine** like terms on each side.
4. **Divide** both sides by the coefficient of the variable.
5. **Check** by substituting your answer into the **original** equation.

*Worked example:* **5x − 7 = 18**
2. Add 7 to both sides: 5x = 25.
4. Divide both sides by 5: **x = 5**.
5. Check: 5(5) − 7 = 18 ✓

*Worked example:* **3(x + 4) = 2x − 1**
1. Expand: 3x + 12 = 2x − 1.
2. Subtract 2x from both sides: x + 12 = −1. Subtract 12: x = −13.
5. Check: 3(−13 + 4) = 3(−9) = −27; 2(−13) − 1 = −27 ✓

*Worked example (fractions):* **x/2 + x/3 = 10**
1. Common denominator 6. Multiply **every term** on both sides by 6: 3x + 2x = 60.
3. 5x = 60. 4. **x = 12**. 5. Check: 6 + 4 = 10 ✓

> **[W] Why must you do the same thing to both sides?**
> 1. The equation is a claim that two quantities are equal.
> 2. If two quantities are equal and you do the same thing to both, the results are still equal (add 7 to two equal amounts → still equal).
> 3. Do something to one side only, and you've changed one quantity but not the other: the claim is no longer the same claim, and its solution changes.

### Special cases

- **No solution:** 2(x + 3) = 2x + 5 → 2x + 6 = 2x + 5 → 6 = 5. False for every x. The two sides are parallel lines that never meet (M09).
- **Every number is a solution:** 3(x − 1) = 3x − 3 → 0 = 0. True for every x. The two sides are the same expression.

---

## Part 4 — Formulas: solving for a different letter

A **formula** is an equation that connects several quantities. Rearranging it uses exactly the same balance moves; you just treat the other letters like numbers.

*Worked example:* **d = rt** (distance = rate × time). Solve for t.
- t is multiplied by r. Undo: divide both sides by r → **t = d/r**.

*Worked example:* **F = (9/5)C + 32** (Celsius to Fahrenheit). Solve for C.
- Subtract 32: F − 32 = (9/5)C.
- Multiply both sides by 5/9 (the reciprocal, M05): **C = (5/9)(F − 32)**.

*Worked example:* **v = u + at** (physics: final speed). Solve for a.
- Subtract u: v − u = at. Divide by t: **a = (v − u)/t**.

**Check a rearranged formula with numbers:** pick values that make the original true (C = 100 → F = 212) and see that your new formula gives them back ((5/9)(212 − 32) = (5/9)(180) = 100 ✓).

You'll rearrange formulas constantly in Module 04 (Ohm's law, V = IR) and Module 09 (transfer time = size/rate + delay).

---

## Part 5 — Inequalities

An **inequality** compares with <, >, ≤ (less than or equal), or ≥.
> 2x − 3 < 9 means "2x − 3 is less than 9."

Solve exactly like an equation, **with one extra rule:**

> **When you multiply or divide both sides by a negative number, flip the inequality sign.**

*Worked example:* **−3x ≥ 12**
- Divide both sides by −3 **and flip**: **x ≤ −4**.
- Check with a number: x = −5 → −3(−5) = 15 ≥ 12 ✓. x = 0 → 0 ≥ 12 ✗ ✓ (0 is not ≤ −4, so it shouldn't work).

> **[W] Why flip?**
> 1. 2 < 5 is true. Multiply both by −1: −2 and −5. But −2 > −5 (−2 is further right).
> 2. Multiplying by −1 **mirrors** the number line around 0: everything that was on the right is now on the left. The order reverses.
> 3. So the inequality sign has to reverse too, or the statement becomes false.

**Answers are ranges**, drawn on the number line: x < 6 is an open circle at 6 with an arrow going left; x ≤ −4 is a filled circle at −4 (filled because −4 itself counts) with an arrow going left.

**Engineering use:** constraints. "The packet must be at most 1,500 bytes." "The response must arrive in under 200 ms." Every limit is an inequality.

---

## Part 6 — Word problems into algebra

**Translating phrases:**

| Words | Algebra |
| :-- | :-- |
| a number | x (choose a clear letter) |
| 5 more than x · x increased by 5 | x + 5 |
| 5 less than x | x − 5 (careful: not 5 − x) |
| twice x · double x | 2x |
| half of x | x/2 |
| the product of x and y | xy |
| x is at most 10 | x ≤ 10 |
| x is at least 10 | x ≥ 10 |
| is · gives · results in | = |

**Subgoal labels [S] (Pólya, specialised for algebra):**
1. **Understand:** what's unknown? **Define a variable in words**, with units: "Let t = number of texts."
2. **Plan:** write an equation that says the same thing as the problem.
3. **Carry out:** solve.
4. **Look back:** check in the **original words** (not just the equation); answer in a full sentence with units.

*Worked example:* A phone plan costs $15 per month plus $0.10 per text. One month's bill is $23.50. How many texts were sent?
1. Let t = number of texts sent.
2. 15 + 0.10t = 23.50
3. 0.10t = 8.50 → t = 85
4. Check: $15 + 85 × $0.10 = $15 + $8.50 = $23.50 ✓. **85 texts were sent.**

*Worked example:* A rectangle's length is 5 cm more than its width. Its perimeter is 46 cm. Find its dimensions.
1. Let w = width in cm. Then length = w + 5.
2. Perimeter = 2 × (length + width): 2(w + 5 + w) = 46.
3. 2(2w + 5) = 46 → 4w + 10 = 46 → 4w = 36 → w = 9.
4. Width 9 cm, length 14 cm. Check: 2(9 + 14) = 46 ✓

---

## Practice routine (5 sections)

| Section | Focus |
| :-- | :-- |
| 1 | Session 1: variables, terms, `=` vs assignment · Session 2: evaluating with brackets · Sessions 3–4: like terms and expanding · Session 5: factoring out + Practice Set 1, items 1–5 |
| 2 | Sessions 1–2: one- and two-step equations · Sessions 3–4: variables on both sides, brackets · Session 5: fractions in equations |
| 3 | Session 1: special cases · Sessions 2–3: rearranging formulas · Session 4: inequalities and the flip · Session 5: Practice Set 1, items 6–18 |
| 4 | Sessions 1–4: word problems (two per session, all four Pólya steps written) · Session 5: Practice Set 1 rest + Set 2 |
| 5 | Sessions 1–3: [Fare Detective](projects/fare-detective/spec.md) Milestones 1–2 · Session 4: Feynman · Session 5: self-check |

**Warm-up [R] (every session):** write the five equation-solving subgoal labels from memory, then solve one equation and check it.

**Key why-questions [W]:**
1. Why can you only combine like terms?
2. Why must you do the same thing to both sides?
3. Why does the inequality flip when you multiply by a negative?
4. Why does `x = x + 1` make sense in Python but not in algebra?

**Feynman target [F]:** *"What does it mean to solve an equation?"* Use the balance scale. Then explain why checking your answer in the original equation is not optional.

---

## Practice sets

### Practice Set 1 — Mixed (20 problems)

1. Evaluate 2a − 3b when a = 4 and b = −1.
2. Evaluate (x − 3)² when x = −2.
3. Simplify 7x − 3 + 2x + 10.
4. Simplify 5(y − 2) − 3(y + 1).
5. Factor 12x + 18.
6. x + 9 = 4
7. 7x = −42
8. 4x + 5 = 33
9. 3x − 8 = x + 6
10. 2(3x − 1) = 4x + 10
11. x/3 − 1 = 5
12. (2x + 1)/5 = 3
13. x/2 + x/3 = 10
14. 5 − 2x = 11
15. 3x + 2 > 14
16. 7 − x ≤ 3
17. Solve A = lw for w.
18. Solve F = (9/5)C + 32 for C.
19. A phone plan is $15/month plus $0.10 per text. The bill is $23.50. How many texts? (All four steps.)
20. A rectangle's length is 5 more than its width; its perimeter is 46. Find both. (All four steps.)

<details>
<summary>Answers (Set 1)</summary>

1. 11 · 2. 25 · 3. 9x + 7 · 4. 2y − 13 · 5. 6(2x + 3) · 6. x = −5 · 7. x = −6 · 8. x = 7 · 9. x = 7 · 10. x = 6 · 11. x = 18 · 12. x = 7 · 13. x = 12 · 14. x = −3 · 15. x > 4 · 16. x ≥ 4 · 17. w = A/l · 18. C = (5/9)(F − 32) · 19. 85 texts · 20. width 9, length 14
</details>

### Practice Set 2 — Think about it (5 problems)

1. Explain why `x = x + 1` is a normal line of Python but an equation with no solution in algebra.
2. Using 2 < 5, show with numbers why multiplying both sides by −1 needs the sign flipped.
3. A student solved 2(x + 3) = 14 like this: 2x + 3 = 14, so x = 5.5. Find the error, fix it, and check your answer.
4. Solve 2(x + 3) = 2x + 5. What happens? What does it mean?
5. Solve 3(x − 1) = 3x − 3. What happens? What does it mean?

<details>
<summary>Answers (Set 2)</summary>

1. In Python, `=` assigns: compute x + 1 and store it in x. In algebra, `=` claims equality, and no number equals itself plus 1 (subtracting x from both sides gives 0 = 1).
2. −2 vs −5: −2 is to the right of −5, so −2 > −5. The order reversed.
3. The 2 must multiply both terms in the bracket: 2x + 6 = 14 → 2x = 8 → x = 4. Check: 2(4 + 3) = 14 ✓
4. 2x + 6 = 2x + 5 → 6 = 5, false: **no solution**. No value of x makes the two sides equal.
5. 3x − 3 = 3x − 3 → 0 = 0, always true: **every number is a solution**. The two sides are the same expression written two ways.
</details>

---

## Watch, practise, and play

*Companions, not replacements: the lessons above come first. Use the [V protocol](../../study-protocols.md#v--watch-actively). Video course for this track: [math resources](resources.md#video-course).*

- **Watch:** Khan Academy: Algebra 1, expressions, equations, inequalities. *Algebra: Elementary to Advanced* (Johns Hopkins, Coursera), course 1. *Introduction to Mathematical Thinking* (Stanford, Coursera) for a taste of proof.
- **Practise:** Khan Academy Algebra 1; Alcumus algebra.
- **Play** ([puzzles and games](puzzles-and-games.md)): think of a number (then invent your own trick) · balance puzzles

---

## Self-check (cold)

1. Evaluate −x² + 4x when x = −3.
2. Simplify 3(2a − b) − 2(a − 4b).
3. Solve 6x − 9 = 2x + 15.
4. Solve 4(x − 2) − 3 = 2(x + 1) + 7.
5. Solve (x − 4)/3 = (x + 2)/5.
6. Solve −2x + 5 > 13.
7. Rearrange v = u + at to find a.
8. A 600 MB download has 120 MB done and continues at 8 MB/s. How many more seconds until it finishes? (Define a variable; all four steps.)
9. Three consecutive whole numbers add up to 84. Find them.
10. **[R] Blank sheet:** `=` in algebra vs code; like terms and why; the five equation subgoals; the inequality flip and why; the word-problem steps.

<details>
<summary>Answers (self-check)</summary>

1. −21 · 2. 4a + 5b · 3. x = 6 · 4. x = 10 · 5. x = 13 · 6. x < −4 · 7. a = (v − u)/t · 8. Let t = seconds remaining: 120 + 8t = 600 → t = 60 seconds · 9. Let n = the first number: n + (n + 1) + (n + 2) = 84 → 3n + 3 = 84 → n = 27: **27, 28, 29**
</details>

## Done when

- [ ] Self-check ≥ 8/9 on items 1–9, blank sheet done.
- [ ] Every equation you solved this stage was checked by substitution (look at your work: is there a check line?).
- [ ] Four why-questions answered; Feynman recording made.
- [ ] [Fare Detective](projects/fare-detective/spec.md) Milestones 1–2 done.

**Next:** [M09 — Linear Functions, Graphs, and Systems](M09-linear-functions-graphs-and-systems.md). You can also now start [03 Discrete Math](../../03-discrete-math/overview.md) alongside M09–M11.
