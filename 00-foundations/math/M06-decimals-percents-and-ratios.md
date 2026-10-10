---
title: "M06 — Decimals, Percents, and Ratios"
stage: M06
track: math
hours: 30
weeks: 4
---

# M06 — Decimals, Percents, and Ratios

**In this stage you will:** extend place value to the right of the decimal point, compute with decimals and know where the point goes and why, convert between fractions, decimals, and percents, handle percent change correctly (including the traps), work with ratios and rates, convert units like an engineer, and finally understand why computers say `0.1 + 0.2` is not `0.3`.

**Time:** about 30 hours over 4 weeks.

**Before you start:** M05 done. You can do all four fraction operations and explain invert-and-multiply.

---

## Diagnostic (cold, 25 minutes, no calculator)

1. Which is bigger: 0.45 or 0.5?
2. 3.07 + 12.6
3. 4.2 × 0.15
4. 7.2 ÷ 0.09
5. Write 3/8 as a decimal.
6. Write 0.35 as a fraction in simplest form.
7. What is 15% of 240?
8. 45 is what percent of 60?
9. A price rises from $80 to $92. What is the percent increase?
10. A connection is 100 megabits per second. At most, how many megabytes per second is that?

<details>
<summary>Answers (diagnostic)</summary>

1. 0.5 · 2. 15.67 · 3. 0.63 · 4. 80 · 5. 0.375 · 6. 7/20 · 7. 36 · 8. 75% · 9. 15% · 10. 12.5 MB/s (8 bits per byte)
</details>

---

## Why this matters

Engineering numbers are rarely whole: 3.3 volts, 0.5 milliseconds, 99.9% uptime, a 2.4 GHz radio, a 1.5× speedup. And they always have **units**. Getting the decimal point, the percent, or the unit wrong by one step means an answer that's off by 10×, 100×, or 8× (bits vs bytes) — the most common class of real engineering mistakes.

This stage gives you three habits:
1. **Know where the decimal point goes, and why.**
2. **Treat percents as fractions, not as magic.** Most percent mistakes come from forgetting *percent of what*.
3. **Carry units through every calculation** so the units themselves check your work.

You'll use all three constantly in [Module 09](../../09-networking/overview.md), where every transfer time, throughput, and loss rate is a decimal, a percent, or a rate.

---

## Part 1 — Decimal place value

Place value (M01) continues to the right of the ones place. Each place is still **one tenth of the place to its left**:

| hundreds | tens | ones | **.** | tenths | hundredths | thousandths |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 100 | 10 | 1 | . | 1/10 | 1/100 | 1/1000 |

**3.407** = 3 ones + 4 tenths + 0 hundredths + 7 thousandths = 3 + 4/10 + 7/1000 = **3 407/1000**.

The decimal point just marks where the ones place is. That's all it does.

### Comparing decimals

**Line up the decimal points**, then compare from the left like whole numbers (add zeros at the end if that helps; they don't change the value).

> 0.45 vs 0.5 → 0.45 vs 0.50 → 50 hundredths > 45 hundredths → **0.5 is bigger**.

**The trap:** "0.45 has more digits, so it's bigger." No: more digits to the *right* of the point means smaller pieces, not a bigger number.

### Rounding decimals

Same subgoals as M01: find the place, look one to the right, 5 or more rounds up, drop the rest.
> 3.14159 to two decimal places (hundredths): look at the thousandths digit (1) → keep → **3.14**.
> 2.996 to two decimal places: thousandths is 6 → round up 2.99 → **3.00** (keep the zeros to show the precision).

---

## Part 2 — Decimals and fractions

### Decimal → fraction

Read the place value, then simplify.
> 0.35 = 35/100 = **7/20** (÷5) · 0.125 = 125/1000 = **1/8** (÷125) · 0.407 = **407/1000**

### Fraction → decimal

A fraction is a division (M05 Part 1). Divide the top by the bottom, adding zeros after the point as needed.
> 3/8 = 3 ÷ 8 = 3.000 ÷ 8 = **0.375**
> 2/3 = 2 ÷ 3 = 0.666… = **0.6̄** (the bar means "repeats forever")

**Which fractions give exact (terminating) decimals?** Only those whose denominator, in simplest form, has **no prime factors except 2 and 5**. 3/8 (8 = 2³) ✓. 7/20 (20 = 2² × 5) ✓. 1/3 ✗. 1/7 ✗.

> **[W] Why only 2 and 5?** A terminating decimal is a fraction over 10, 100, 1,000, … and 10 = 2 × 5. You can only rewrite a/b over a power of 10 if b's prime factors all appear in 10. (Hold this thought for Part 7, where base 2 makes the same rule much stricter.)

**Benchmarks to know by heart (flashcards):**

| Fraction | 1/2 | 1/4 | 3/4 | 1/5 | 1/8 | 1/3 | 2/3 | 1/10 | 1/100 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Decimal | 0.5 | 0.25 | 0.75 | 0.2 | 0.125 | 0.333… | 0.666… | 0.1 | 0.01 |
| Percent | 50% | 25% | 75% | 20% | 12.5% | 33.3…% | 66.6…% | 10% | 1% |

---

## Part 3 — Computing with decimals

### Adding and subtracting: line up the points

```
   3.07
+ 12.60      ← write the missing zero so the places line up
 ------
  15.67
```

*Why:* you can only add tenths to tenths and hundredths to hundredths (same idea as common denominators in M05).

### Multiplying: count the decimal places

**Subgoal labels [S]:**
1. **Ignore the points** and multiply as whole numbers.
2. **Count** the total number of digits after the point in both numbers.
3. **Place the point** so the answer has that many digits after it.
4. **Estimate** to check.

*Worked example:* **4.2 × 0.15**
1. 42 × 15 = 630.
2. 4.2 has 1 decimal place, 0.15 has 2 → 3 total.
3. 0.630 → **0.63**.
4. Estimate: 4 × 0.15 = 0.6 ✓

> **[W] Why count the places?** 4.2 = 42/10 and 0.15 = 15/100. So 4.2 × 0.15 = (42 × 15)/(10 × 100) = 630/1000. Tenths times hundredths gives thousandths. The "count the places" rule is fraction multiplication in disguise.

### Dividing: make the divisor whole

**Subgoal labels [S]:**
1. **Move the divisor's point** right until it's a whole number. Count the moves.
2. **Move the dividend's point the same number of places** (add zeros if needed).
3. **Divide** as usual, putting the answer's point straight above the dividend's point.
4. **Estimate** to check.

*Worked example:* **7.2 ÷ 0.09**
1. 0.09 → 9: two moves.
2. 7.2 → 720.
3. 720 ÷ 9 = **80**.
4. Check: 80 × 0.09 = 7.2 ✓. (Dividing by something less than 1 gives a bigger answer — M05.)

> **[W] Why can you move both points?** Moving both points two places right multiplies both numbers by 100. M05 Part 6: a division doesn't change if you multiply both parts by the same amount. 7.2 ÷ 0.09 = 720 ÷ 9.

### × and ÷ by 10, 100, 1,000

Multiplying by 10 moves the point one place **right** (every digit is worth 10× more). Dividing by 10 moves it one place **left**.
> 3.47 × 100 = 347 · 3.47 ÷ 100 = 0.0347

---

## Part 4 — Percents

**Percent** means **per hundred**. 35% = 35/100 = 0.35. That's it: a percent is a fraction with denominator 100.

**Converting:**
- Percent → decimal: ÷ 100 (move the point two left). 4.5% = 0.045.
- Decimal → percent: × 100 (move two right). 0.045 = 4.5%.
- Fraction → percent: to decimal, then × 100. 7/20 = 0.35 = 35%.

### The three basic percent questions

All three are the same equation: **part = percent × whole**. Just find which piece is missing.

| Question | Example | Calculation |
| :-- | :-- | :-- |
| Find the **part** | What is 15% of 240? | 0.15 × 240 = **36** |
| Find the **percent** | 45 is what % of 60? | 45 ÷ 60 = 0.75 = **75%** |
| Find the **whole** | 36 is 15% of what? | 36 ÷ 0.15 = **240** |

**Mental tricks:** 10% = move the point one left (10% of 240 = 24). 5% = half of 10% (12). 1% = move two left (2.4). So 15% = 24 + 12 = 36.

### Percent change

**Subgoal labels [S]:**
1. **Find the change** (new − old). Positive = increase, negative = decrease.
2. **Divide by the OLD value** (the starting point).
3. **Convert to a percent.**

*Worked example:* $80 → $92. Change = 12. 12 ÷ 80 = 0.15 = **15% increase**.

### The percent traps (every one of these causes real mistakes)

1. **"Percent of what?"** A 20% discount followed by a 20% markup does **not** get you back where you started: $100 → $80 → $96. The second 20% is of a smaller number.
2. **Reverse percent.** After a 20% discount the price is $64. The original was **not** $64 + 20% of 64. It was $64 ÷ 0.80 = **$80**. (The $64 is 80% of the original.)
3. **Successive changes multiply, they don't add.** +10% then −10%: 50,000 × 1.10 × 0.90 = **49,500**, not 50,000.
4. **Percent vs percentage points.** An error rate going from 2% to 3% is an increase of **1 percentage point**, but a **50% increase** in the error rate. Both are true; say which one you mean.

> **[W] Why divide by the old value in percent change?** Because "percent change" answers "how big is the change *compared to where we started*?" A $12 increase is huge on an $8 item (150%) and tiny on an $8,000 one (0.15%). The old value is the reference.

---

## Part 5 — Ratios, rates, and proportions

A **ratio** compares two amounts: 18 boys to 24 girls is **18 : 24**, which simplifies (÷ 6) to **3 : 4**. Ratios simplify like fractions.

**Part-to-part vs part-to-whole:** the ratio of boys to girls is 3 : 4, but the **fraction** of the group that is boys is 3/(3 + 4) = **3/7**. Mixing these up is a common error.

A **rate** is a ratio with different units: 120 km per 2 hours, 50 megabits per second. A **unit rate** is "per one": 120 km / 2 h = **60 km/h**.

### Proportions

A **proportion** says two ratios are equal: 3/4 = x/20. Solve by scaling (4 × 5 = 20, so x = 3 × 5 = 15) or by cross-multiplying (3 × 20 = 4 × x → x = 15).

*Splitting in a ratio:* split 64 in the ratio 3 : 5. Total parts = 8. One part = 64 ÷ 8 = 8. So **24 and 40**.

---

## Part 6 — Units and conversions

### Metric prefixes

| Prefix | Symbol | Means | Example |
| :-- | :-- | :-- | :-- |
| giga | G | 1,000,000,000 (10⁹) | 2.4 GHz |
| mega | M | 1,000,000 (10⁶) | 50 Mbps |
| kilo | k | 1,000 (10³) | 5 km |
| (none) | | 1 | 1 m |
| milli | m | 1/1,000 (10⁻³) | 3 ms |
| micro | µ | 1/1,000,000 (10⁻⁶) | 10 µs |
| nano | n | 1/1,000,000,000 (10⁻⁹) | 1 ns |

(The powers-of-ten notation 10⁶ is explained in M07.)

### Converting with "fractions equal to 1"

The safest way to convert units: multiply by a fraction whose top and bottom are **equal amounts in different units**. It equals 1, so it doesn't change the quantity, only the units. Units cancel like numbers.

*Worked example:* **72 km/h → m/s**

$$72\ \frac{\text{km}}{\text{h}} \times \frac{1000\ \text{m}}{1\ \text{km}} \times \frac{1\ \text{h}}{3600\ \text{s}} = \frac{72 \times 1000}{3600}\ \frac{\text{m}}{\text{s}} = 20\ \frac{\text{m}}{\text{s}}$$

km cancels with km, h with h; m/s is left. **If the units don't cancel to what you want, the setup is wrong** — before you've done any arithmetic. This is called **dimensional analysis**, and it's one of the most powerful checking tools in engineering.

### Computer units: two traps

1. **Bits vs bytes.** 1 byte = 8 bits. Network speeds are in **bits** per second (lowercase b: Mbps, Mb/s). File sizes are in **bytes** (uppercase B: MB). A 100 Mbps connection moves at most 100 ÷ 8 = **12.5 MB per second**.
2. **1,000 vs 1,024.** Storage makers use kilo = 1,000 (a 500 GB drive is 500,000,000,000 bytes). Operating systems often count in powers of 2: 1 **KiB** (kibibyte) = 1,024 bytes, 1 MiB = 1,024 KiB, 1 GiB = 1,024 MiB. That's why a "500 GB" drive shows up as about **466 GiB**. Neither is wrong; know which one you're looking at.

---

## Part 7 — Why `0.1 + 0.2` isn't `0.3` on a computer

Open Python and type `0.1 + 0.2`. You'll get `0.30000000000000004`. This is not a bug in Python. It's arithmetic, and you now know enough to understand it.

**Why-ladder [W]:**
1. **Computers store numbers in binary.** Fractions use binary places: halves, quarters, eighths, … (M05 Part 9).
2. **A fraction terminates in binary only if its denominator is a power of 2** (same logic as Part 2, but base 2's only prime factor is 2).
3. **1/10 has a factor of 5 in its denominator.** So in binary, 0.1 is a repeating fraction: 0.0001100110011…₂ forever.
4. **Computers keep only a fixed number of binary digits** (usually 53 significant bits for Python's `float`). So 0.1 is stored as a number *very slightly* different from 1/10. Same for 0.2 and 0.3.
5. **The tiny errors don't cancel out perfectly**, so 0.1 + 0.2 lands one tiny step away from the stored value of 0.3.

**Engineering rules that follow:**
- **Never test floats with `==`.** Test whether they're close: `abs(a - b) < 1e-9`, or Python's `math.isclose(a, b)`.
- **Never store money in floats.** Store whole cents as integers (`1999` for $19.99), or use Python's `decimal` module.
- **Expect tiny errors** in any long float calculation, and know they can grow. You'll meet this again in [Module 12](../../12-math-for-engineering/overview.md) (numerical methods) and Module 06 (how floats are built from bits).

---

## Practice routine (4 weeks)

| Week | Focus |
| :-- | :-- |
| 1 | Mon: decimal place value and comparing · Tue: rounding · Wed–Thu: decimal ↔ fraction, benchmarks · Fri: add/subtract decimals |
| 2 | Mon–Tue: multiply and divide decimals (with the why) · Wed–Thu: percents, the three questions · Fri: Practice Set 1, items 1–15 |
| 3 | Mon: percent change · Tue: the four traps · Wed: ratios and proportions · Thu: units and conversion factors · Fri: Practice Set 1 rest + Set 2 |
| 4 | Mon–Tue: [Ratio Workshop](projects/ratio-workshop/spec.md) Milestones 2–3 · Wed: the `0.1 + 0.2` why-ladder, written · Thu: Feynman · Fri: self-check |

**Daily warm-up [R]:** the benchmark table from memory, and one unit conversion with full unit cancellation.

**Key why-questions [W]:**
1. Why do you count decimal places when multiplying?
2. Why does moving both points work in division?
3. Why does percent change divide by the old value?
4. Why can 1/8 be stored exactly in binary but 1/10 can't?

**Feynman target [F]:** *"Why is a 50% off sale followed by a 50% price rise not back to the original price?"* Plain words, one example, 90 seconds out loud. Then: *"Why does Python say 0.1 + 0.2 isn't 0.3?"*

---

## Practice sets

### Practice Set 1 — Mixed (20 problems, no calculator)

1. Write 0.407 as a fraction.
2. Order from smallest to largest: 0.6, 0.06, 0.66, 0.606.
3. Round 3.14159 to two decimal places.
4. 12.5 − 3.75
5. 0.3 × 0.4
6. 2.5 × 1.2
7. 9.6 ÷ 0.3
8. 1.44 ÷ 1.2
9. 5/16 as a decimal
10. 2/3 as a decimal
11. 0.125 as a fraction
12. 7/20 as a percent
13. 0.045 as a percent
14. 18% of 350
15. 27 is what percent of 36?
16. A $120 item is 25% off. New price?
17. After a 20% discount, an item costs $64. What was the original price?
18. A town of 50,000 grows by 10%, then shrinks by 10%. What is the population now?
19. A group has 18 boys and 24 girls. Write the boys-to-girls ratio in simplest form. What fraction of the group is boys?
20. Convert 72 km/h to m/s, showing the unit cancellation.

<details>
<summary>Answers (Set 1)</summary>

1. 407/1000 · 2. 0.06, 0.6, 0.606, 0.66 · 3. 3.14 · 4. 8.75 · 5. 0.12 · 6. 3 · 7. 32 · 8. 1.2 · 9. 0.3125 · 10. 0.666… (0.6̄) · 11. 1/8 · 12. 35% · 13. 4.5% · 14. 63 · 15. 75% · 16. $90 · 17. $80 · 18. 49,500 · 19. 3 : 4; 3/7 · 20. 20 m/s
</details>

### Practice Set 2 — Engineering numbers (6 problems; calculator allowed after you set up the units)

1. At best, how many seconds does it take to download a 2 GB file over a 50 Mbps connection? (Use 1 GB = 1,000 MB.)
2. A drive is sold as "500 GB." How many GiB is that? (1 GiB = 2³⁰ = 1,073,741,824 bytes.)
3. A server takes 3 ms to handle one request, one at a time. At most how many requests per second can it handle?
4. 3 of 12,000 packets arrive corrupted. Write the error rate as a percent and as "per million."
5. A battery holds 3,000 mAh. A device draws 250 mA. How many hours will it run (ideally)?
6. Explain in 3–4 sentences why `0.1 + 0.2 == 0.3` is `False` in Python, and what you should write instead.

<details>
<summary>Answers (Set 2)</summary>

1. 2 GB = 2,000 MB = 16,000 Mb; 16,000 Mb ÷ 50 Mb/s = **320 s** (about 5⅓ minutes). Real downloads are slower; Module 09 explains why.
2. 500,000,000,000 ÷ 1,073,741,824 ≈ **465.7 GiB**.
3. 1 s = 1,000 ms; 1,000 ÷ 3 ≈ **333** requests per second.
4. 3 ÷ 12,000 = 0.00025 = **0.025%** = **250 per million**.
5. 3,000 mAh ÷ 250 mA = **12 hours** (mA cancels, h remains).
6. Python stores floats in binary, and 0.1, 0.2, and 0.3 all have repeating binary forms, so each is stored as a tiny bit off. The errors don't cancel exactly. Write `math.isclose(0.1 + 0.2, 0.3)` or `abs((0.1 + 0.2) - 0.3) < 1e-9`.
</details>

---

## Watch, practise, and play

*Companions, not replacements: the lessons above come first. Use the [V protocol](../../study-protocols.md#v--watch-actively). Full list: [courses-and-videos.md](../../courses-and-videos.md#foundations-math).*

- **Watch:** Math Antics: decimals and percents. Khan Academy: decimals, percents, ratios and rates. Computerphile: 'Floating Point Numbers'.
- **Practise:** Khan Academy ratios and percents practice.
- **Play** ([puzzles and games](puzzles-and-games.md)): the percent shopping game · recipe remix · the 0.1 + 0.2 bet · Fermi questions

---

## Self-check (cold, 35 minutes; no calculator for 1–8)

1. 6.08 − 2.9
2. 0.25 × 0.8
3. 4.5 ÷ 0.15
4. 7/8 as a decimal and as a percent
5. 35% of 80
6. A price goes from $45 to $54. Percent increase?
7. A total including 15% tax is $69. What was the price before tax?
8. Split 64 in the ratio 3 : 5.
9. A 4K video frame is 3,840 × 2,160 pixels, with 3 bytes per pixel. How many bytes is one uncompressed frame? At 60 frames per second, about how many MB per second? (Calculator allowed.)
10. **[R] Blank sheet (10 min):** decimal place value; the multiply and divide rules with their reasons; the three percent questions; the four percent traps; unit conversion with fractions equal to 1; the `0.1 + 0.2` why-ladder.

<details>
<summary>Answers (self-check)</summary>

1. 3.18 · 2. 0.2 · 3. 30 · 4. 0.875; 87.5% · 5. 28 · 6. 20% · 7. $60 ($69 ÷ 1.15) · 8. 24 and 40 · 9. 24,883,200 bytes per frame (about 24.9 MB); × 60 ≈ 1,493 MB/s, about 1.5 GB per second. (That's why video is compressed.)
</details>

## Done when

- [ ] Self-check ≥ 8/9 on items 1–9, blank sheet done.
- [ ] The four why-questions answered; both Feynman targets recorded.
- [ ] [Ratio Workshop](projects/ratio-workshop/spec.md) complete.

**Next:** [M07 — Negatives, Exponents, and Order of Operations](M07-negatives-exponents-and-order-of-operations.md).
