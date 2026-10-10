---
title: "M07 — Negatives, Exponents, and Order of Operations"
stage: M07
track: math
hours: 30
weeks: 4
---

# M07 — Negatives, Exponents, and Order of Operations

**In this stage you will:** work with negative numbers and know *why* a negative times a negative is positive; use exponents, their laws, and the reasons behind them (including why anything to the power 0 is 1); use square roots and scientific notation; apply the order of operations without traps; and see how computers store negative numbers using nothing but the odometer from M01.

**Time:** about 30 hours over 4 weeks.

**Before you start:** M06 done.

---

## Diagnostic (cold, 20 minutes, no calculator)

1. −7 + 4
2. 3 − 9
3. −5 − (−8)
4. (−6) × (−4)
5. −36 ÷ 9
6. 2¹⁰
7. 5⁰
8. 10⁻³ as a decimal
9. 3 + 4 × 2²
10. What is (−3)²? What is −3²?

<details>
<summary>Answers (diagnostic)</summary>

1. −3 · 2. −6 · 3. 3 · 4. 24 · 5. −4 · 6. 1,024 · 7. 1 · 8. 0.001 · 9. 19 · 10. 9 and −9 (the exponent applies before the minus sign unless there are brackets)
</details>

---

## Why this matters

**Negative numbers** are everywhere in engineering: temperatures, voltages below ground, debts, positions left of an origin, a signal swinging below zero, the change in a value. And computers have to store them using only 0s and 1s — with no minus sign available. The trick they use (Part 7) is one of the most elegant ideas in computing, and you'll build it into hardware in Module 06.

**Exponents** are how engineers talk about size. Memory comes in powers of 2 (a 32-bit address can reach 2³² bytes). Physics and electronics use powers of 10 (a nanosecond is 10⁻⁹ seconds). Algorithms are measured with exponents (n² steps vs 2ⁿ steps — the difference between "fast" and "never finishes"). After this stage, you'll be able to estimate any of these in your head.

**Order of operations** matters because code follows it exactly. A formula typed into a program with one misplaced bracket gives a wrong answer with no error message.

---

## Part 1 — Negative numbers on the number line

Extend the number line to the left of 0: …, −3, −2, −1, 0, 1, 2, 3, … These are the **integers**.

- **−5** is 5 steps **left** of 0. **5** and **−5** are **opposites**: same distance from 0, opposite sides.
- The **absolute value** |−5| = 5 is the distance from 0, ignoring direction.
- **Further left is smaller:** −5 < −2 (−5 °C is colder than −2 °C). The trap: "5 is bigger than 2, so −5 is bigger than −2." No.

### Adding and subtracting

Think of **adding as moving**: adding a positive moves right; adding a negative moves left.

> −7 + 4: start at −7, move 4 right → **−3**
> −8 + (−6): start at −8, move 6 left → **−14**

**Subtracting is adding the opposite:** a − b = a + (−b).

> 3 − 9 = 3 + (−9) → start at 3, move 9 left → **−6**
> −5 − (−8) = −5 + 8 → **3**

> **[W] Why does subtracting a negative move right?**
> 1. Subtraction answers "what do I add to b to get a?" (M02: the missing-part meaning).
> 2. −5 − (−8) asks: what do I add to −8 to get −5? From −8 to −5 is 3 steps right. So the answer is **+3**.
> 3. Real life: your bank shows −$8 (you owe $8). The bank cancels (removes) that −$8 debt. Removing a debt makes you $8 better off. Taking away a negative is the same as adding a positive.

**Shortcut rules** (use after you understand the moves):

| Situation | Rule | Example |
| :-- | :-- | :-- |
| Same signs | add the sizes, keep the sign | −8 + (−6) = −14 |
| Different signs | subtract the smaller size from the larger, take the sign of the larger size | −12 + 5 = −7 |
| Subtracting | change to adding the opposite, then use the rules above | 6 − (−11) = 6 + 11 = 17 |

---

## Part 2 — Multiplying and dividing negatives

| | Example | Result |
| :-- | :-- | :-- |
| positive × positive | 3 × 4 | positive (12) |
| positive × negative | 3 × (−4) | negative (−12): three debts of $4 = owing $12 |
| negative × positive | (−3) × 4 | negative (−12): commutative |
| **negative × negative** | (−3) × (−4) | **positive (12)** — why? |

### Why is negative × negative positive? Two arguments

**1. The pattern argument.** Watch what happens as the first number goes down by 1:

| | |
| :-- | :-- |
| 3 × (−4) = −12 | |
| 2 × (−4) = −8 | (went up by 4) |
| 1 × (−4) = −4 | (up by 4) |
| 0 × (−4) = 0 | (up by 4) |
| (−1) × (−4) = **4** | (the pattern continues: up by 4) |
| (−2) × (−4) = **8** | |

Each step down in the first number *adds* 4 to the answer. For the pattern to continue past 0, negative × negative must be positive.

**2. The distributive-law proof.** (This is the airtight one. It's in your old bedrock note, too.)
1. 1 + (−1) = 0, so (−1) × (1 + (−1)) = (−1) × 0 = **0**.
2. Use the distributive law (M03) on the left side: (−1) × 1 + (−1) × (−1) = 0.
3. (−1) × 1 = −1, so: −1 + (−1) × (−1) = 0.
4. The only number that adds to −1 to make 0 is **+1**. So **(−1) × (−1) = 1**. ∎

**Why this matters [W]:** the rule isn't an arbitrary convention. If (−1) × (−1) were anything other than 1, the distributive law would break — and the distributive law is what makes all of algebra work. Math chose to keep the distributive law, and the sign rule came with it.

**Sign rules** (same for division, since division undoes multiplication):
- Same signs → positive. Different signs → negative.
- With several factors: **count the negatives**. Even count → positive; odd count → negative. (−2)(−3)(−4) = **−24** (three negatives).

---

## Part 3 — Exponents

An **exponent** says how many times to multiply a number (the **base**) by itself:
> 2⁵ = 2 × 2 × 2 × 2 × 2 = 32. Say "2 to the 5th" or "2 to the power 5."

In code: `2 ** 5` in Python; `pow(2, 5)`. (Not `2 ^ 5`: in Python and C, `^` means something else — XOR, Module 04.)

### Two tables to know by heart (flashcards)

| n | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 16 | 20 | 30 | 32 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 2ⁿ | 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 | 512 | 1,024 | 65,536 | ≈1 million | ≈1 billion | ≈4.3 billion |

| n | −9 | −6 | −3 | 0 | 3 | 6 | 9 | 12 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 10ⁿ | nano | micro | milli | 1 | kilo (thousand) | mega (million) | giga (billion) | tera (trillion) |

**The key bridge: 2¹⁰ = 1,024 ≈ 10³.** So 2²⁰ ≈ 10⁶, 2³⁰ ≈ 10⁹, 2⁴⁰ ≈ 10¹². Every power-of-2 estimate in computing uses this.

### The laws of exponents (and why)

| Law | Example | Why (count the factors) |
| :-- | :-- | :-- |
| aᵐ × aⁿ = aᵐ⁺ⁿ | 2³ × 2⁴ = 2⁷ | (2·2·2) × (2·2·2·2): 3 twos then 4 more = 7 twos |
| aᵐ ÷ aⁿ = aᵐ⁻ⁿ | 10⁸ ÷ 10⁵ = 10³ | 8 tens on top, 5 cancel with the 5 on the bottom, 3 remain |
| (aᵐ)ⁿ = aᵐⁿ | (2³)² = 2⁶ | two groups of three twos = six twos |
| (ab)ⁿ = aⁿbⁿ | (2·5)³ = 2³·5³ | rearrange the factors (commutative law) |

### Zero and negative exponents

**Why is 2⁰ = 1?** Follow the pattern, dividing by 2 each step:

> 2³ = 8 → 2² = 4 → 2¹ = 2 → 2⁰ = **1** → 2⁻¹ = **½** → 2⁻² = **¼** → 2⁻³ = **⅛**

Also from the division law: 2³ ÷ 2³ = 2³⁻³ = 2⁰, and 8 ÷ 8 = 1. So 2⁰ must be 1 for the law to keep working.

**Negative exponents mean "one over":** a⁻ⁿ = 1/aⁿ. 10⁻³ = 1/1,000 = 0.001 (milli). 2⁻³ = 1/8.

### The minus-sign trap

- **(−3)² = (−3) × (−3) = 9.** The brackets put the minus inside.
- **−3² = −(3²) = −9.** Without brackets, the exponent goes first, then the minus.
- Python agrees: `(-3)**2` is `9`, `-3**2` is `-9`.

---

## Part 4 — Square roots

The **square root** √n is the number that, multiplied by itself, gives n. √144 = 12 because 12 × 12 = 144. (The name comes from squares: a square of area 144 has side 12.)

**Perfect squares to know:** 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225.

**Estimating:** √50 is between √49 = 7 and √64 = 8, close to 7 (since 50 is just above 49): about **7.07**.

Square roots appear in Pythagoras (M10), distances on screens, the "stop at √n" rule for factors (M04), and the root-mean-square voltage of household electricity (Module 04).

---

## Part 5 — Scientific notation

Very big and very small numbers are written as **a × 10ⁿ**, with 1 ≤ a < 10.

| Number | Scientific notation | In code |
| :-- | :-- | :-- |
| 300,000,000 m/s (speed of light) | 3 × 10⁸ | `3e8` |
| 0.000000001 s (1 nanosecond) | 1 × 10⁻⁹ | `1e-9` |
| 602,000,000,000,000,000,000,000 | 6.02 × 10²³ | `6.02e23` |

**Multiplying:** multiply the fronts, add the exponents, then fix the front if needed.
> (3 × 10⁸) × (2 × 10⁻³) = 6 × 10⁵
> (4 × 10⁶) × (5 × 10⁻⁹) = 20 × 10⁻³ = **2 × 10⁻²** (fix: 20 = 2 × 10¹)

**Why it's useful:** you can multiply huge numbers in your head, and you can see the **order of magnitude** (the power of 10) at a glance. "Is this 10⁶ or 10⁹?" is often the only question that matters. The [Magnitudes Field Guide](projects/magnitudes-field-guide/spec.md) project is entirely about this.

---

## Part 6 — Order of operations

**Why do we need a rule?** 3 + 4 × 2 could mean (3 + 4) × 2 = 14 or 3 + (4 × 2) = 11. Everyone has to agree, or written math (and code) is ambiguous. The agreed order:

1. **Brackets** (innermost first)
2. **Exponents** (and roots)
3. **Multiplication and division**, **left to right**
4. **Addition and subtraction**, **left to right**

**Subgoal labels [S]:**
1. Find the **innermost brackets**; work inside them using steps 2–4. Repeat until no brackets remain.
2. Do all **exponents**.
3. Sweep **left to right** doing × and ÷ as you meet them.
4. Sweep **left to right** doing + and − as you meet them.

*Worked example:* **20 − 3 × (4 + 2)² ÷ 9**
1. Brackets: 4 + 2 = 6 → 20 − 3 × 6² ÷ 9
2. Exponents: 6² = 36 → 20 − 3 × 36 ÷ 9
3. × and ÷ left to right: 3 × 36 = 108; 108 ÷ 9 = 12 → 20 − 12
4. **8**

**The traps:**
- **"PEMDAS" makes people think multiplication comes before division.** It doesn't. They're equal, done left to right: 8 ÷ 2 × 4 = 4 × 4 = **16** (not 8 ÷ 8 = 1).
- **Same for + and −:** 10 − 3 + 2 = 7 + 2 = **9** (not 10 − 5).
- **When in doubt in code, add brackets.** They cost nothing and remove all doubt for the next reader. (A fact about Python: `2 ** 3 ** 2` is `2 ** 9 = 512`, because stacked powers go right to left. Brackets make this obvious: `2 ** (3 ** 2)`.)

---

## Part 7 — How computers store negative numbers

A computer stores a number in a fixed number of bits, like an odometer with a fixed number of wheels (M01). There's no place for a minus sign. So how does it store −1?

**Run the odometer backwards.** A 4-digit decimal odometer at 0000, rolled back one step, shows **9999**. In a world with only four digits, 9999 behaves like −1: add 1 to it and you get 0000 (the carry falls off the end).

Binary works the same way. A **4-bit** counter at 0000, minus 1, shows **1111**. So we *decide* that 1111 means −1, 1110 means −2, and so on:

| Bits | 0111 | 0110 | … | 0001 | 0000 | 1111 | 1110 | … | 1001 | 1000 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Value | 7 | 6 | … | 1 | 0 | −1 | −2 | … | −7 | −8 |

This is called **two's complement**. With 4 bits, it covers −8 to 7. With 8 bits, −128 to 127. With 32 bits, about −2.1 billion to +2.1 billion.

**Why it's brilliant:** the computer uses the **same adding circuit** for positive and negative numbers. Try 3 + (−3) = 0011 + 1101:

```
   0011
 + 1101
 ------
  10000   → keep 4 bits → 0000 = 0 ✓
```

The carry falls off the end and the answer is exactly right. That's modular arithmetic (M03): 4-bit numbers live on a ring of 16, and −3 and 13 are the *same place* on that ring (13 mod 16 = 13, −3 mod 16 = 13).

**Quick rules:**
- The leftmost bit is 1 for negative numbers (the **sign bit**).
- To negate a number: flip every bit, then add 1. (5 = 0101 → flip 1010 → +1 → 1011 = −5.)
- **Overflow:** in 8 bits, 127 + 1 = 10000000 = **−128**. The odometer rolled over the top. This is a real bug class in C, Rust, and hardware, and you'll meet it in Modules 06–07.

> **[W] Why does "flip and add 1" give the negative?** Flipping every bit of n gives 1111 − n (each 0 becomes 1 and each 1 becomes 0; 0101 + 1010 = 1111). 1111 is 15, which is −1 on the 4-bit ring. So flipping gives −1 − n. Adding 1 gives −n. ∎

You'll build a circuit that does exactly this in Module 04 and use it to make your CPU subtract in Module 06.

---

## Practice routine (4 weeks)

| Week | Focus |
| :-- | :-- |
| 1 | Mon: number line, opposites, absolute value · Tue–Wed: adding and subtracting (moves first, then rules) · Thu: multiply/divide signs, both arguments · Fri: Practice Set 1, items 1–11 |
| 2 | Mon: exponent meaning and the two tables · Tue: laws with the factor-counting reasons · Wed: zero and negative exponents · Thu: square roots · Fri: Practice Set 1, items 12–19 |
| 3 | Mon: scientific notation · Tue–Wed: order of operations (20 problems, mixed) · Thu: two's complement · Fri: Practice Set 1 rest + Set 2 |
| 4 | Mon–Wed: [Magnitudes Field Guide](projects/magnitudes-field-guide/spec.md) · Thu: Feynman · Fri: self-check |

**Daily warm-up [R]:** powers of 2 from 2⁰ to 2¹⁰ and the 10ⁿ prefixes, from memory; then one order-of-operations problem.

**Key why-questions [W]:**
1. Why does subtracting a negative make a number bigger?
2. Why is (−1) × (−1) = 1? (The distributive-law proof, all four steps.)
3. Why is a⁰ = 1?
4. Why does 0011 + 1101 = 0000 in 4 bits mean 3 + (−3) = 0?

**Feynman target [F]:** *"Why is a negative times a negative positive?"* Explain it twice: once with the pattern, once with the distributive law. Record both. Which one would convince a skeptical friend?

---

## Practice sets

### Practice Set 1 — Mixed (24 problems, no calculator)

1. −12 + 5 · 2. −8 + (−6) · 3. 7 − 15 · 4. −4 − 9 · 5. 6 − (−11) · 6. −20 − (−5)
7. (−7) × 6 · 8. (−9) × (−8) · 9. (−2) × (−3) × (−4) · 10. 48 ÷ (−6) · 11. |−15| − |8|
12. 2⁷ · 13. 3⁴ · 14. (−2)⁵ · 15. 2³ × 2⁴ (as a power, then a number) · 16. 10⁸ ÷ 10⁵ · 17. (2³)² · 18. 4⁻¹ and 2⁻³
19. √144, and estimate √50 to one decimal place
20. (6.02 × 10²³) × 2, in scientific notation
21. (3 × 10⁸) × (2 × 10⁻³)
22. 20 − 3 × (4 + 2)² ÷ 9
23. 8 ÷ 2 × 4
24. In 4-bit two's complement, what number is 1110? What range of numbers can 4 bits hold?

<details>
<summary>Answers (Set 1)</summary>

1. −7 · 2. −14 · 3. −8 · 4. −13 · 5. 17 · 6. −15 · 7. −42 · 8. 72 · 9. −24 · 10. −8 · 11. 7 · 12. 128 · 13. 81 · 14. −32 · 15. 2⁷ = 128 · 16. 10³ = 1,000 · 17. 2⁶ = 64 · 18. ¼ and ⅛ · 19. 12; about 7.1 · 20. 1.204 × 10²⁴ · 21. 6 × 10⁵ · 22. 8 · 23. 16 · 24. −2; −8 to 7
</details>

### Practice Set 2 — Think about it (5 problems)

1. How many different values can a 16-bit number hold? A 32-bit number? (Use the table and the 2¹⁰ ≈ 10³ bridge to estimate, then give the exact value.)
2. The temperature goes from −12 °C to 7 °C. By how much did it rise? Write it as a subtraction.
3. Use 2¹⁰ ≈ 10³ to estimate 2⁴⁰. What is a "terabyte" in powers of 2, roughly?
4. In 8-bit two's complement, what is 01111111 + 1? Why is this called overflow?
5. Negate 6 in 4-bit two's complement using "flip and add 1." Check by adding your answer to 0110.

<details>
<summary>Answers (Set 2)</summary>

1. 2¹⁶ = **65,536**. 2³² ≈ 4 × 10⁹; exactly **4,294,967,296**.
2. 7 − (−12) = 7 + 12 = **19 °C**.
3. 2⁴⁰ = (2¹⁰)⁴ ≈ (10³)⁴ = 10¹² (exactly 1,099,511,627,776). A terabyte is about 2⁴⁰ bytes (exactly 2⁴⁰ is a tebibyte, TiB).
4. 10000000 = **−128**. 127 + 1 should be 128, but 8-bit two's complement only goes up to 127; the result "rolled over" into the negative range.
5. 6 = 0110 → flip → 1001 → +1 → **1010** (= −6). Check: 0110 + 1010 = 10000 → keep 4 bits → 0000 ✓
</details>

---

## Self-check (cold, 30 minutes, no calculator)

1. −15 + 9 − (−4)
2. (−3)³
3. −2⁴
4. 5 × 10⁻² as a decimal
5. (4 × 10⁶) × (5 × 10⁻⁹), in scientific notation
6. 2⁵ × 2⁻²
7. 18 − 2 × (3 − 5)²
8. (−12 ÷ 4) − (−2)(−5)
9. What is the smallest number of bits that can give 1,000 different values?
10. In 4-bit two's complement, add 0011 and 1101. What does the result show?
11. **[R] Blank sheet (10 min):** adding/subtracting negatives with the "moves" picture; both arguments for (−)×(−) = (+); the exponent laws with reasons; why a⁰ = 1; order of operations with the two traps; two's complement and "flip and add 1."

<details>
<summary>Answers (self-check)</summary>

1. −2 · 2. −27 · 3. −16 · 4. 0.05 · 5. 2 × 10⁻² · 6. 2³ = 8 · 7. 10 · 8. −13 · 9. 10 bits (2¹⁰ = 1,024; 2⁹ = 512 is too few) · 10. 10000 → 0000: 3 + (−3) = 0, with the carry falling off the end
</details>

## Done when

- [ ] Self-check ≥ 9/10 on items 1–10, blank sheet done.
- [ ] Powers of 2 to 2¹⁰ and the SI prefixes instant from memory.
- [ ] Four why-questions answered; Feynman recordings made.
- [ ] [Magnitudes Field Guide](projects/magnitudes-field-guide/spec.md) complete.

**Next:** [M08 — Algebra: Expressions and Equations](M08-algebra-expressions-and-equations.md). Also: you now have everything [03 Discrete Math](../../03-discrete-math/overview.md) needs except algebra; it starts after M08.
