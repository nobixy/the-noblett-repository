---
title: "M03 — Multiplication and Division"
id: "M03"
type: "lesson"
module: "00-foundations"
track: "math"
stage: "M03"
phase: "A"
order: 160
prerequisites: [M02]
---

# M03 — Multiplication and Division

**In this stage you will:** understand multiplication as groups, as area, and as scaling; learn the times tables with strategies instead of rote; see why the distributive law makes long multiplication work; do long division and know what each step means; and master remainders and **modulo**, one of the most-used operations in programming.

**Before you start:** M02 done.

---

## Diagnostic (cold, no calculator)

1. 7 × 8
2. 12 × 9
3. 34 × 27
4. 406 × 58
5. 7,452 ÷ 6
6. 3,927 ÷ 12 (give quotient and remainder)
7. 100 ÷ 7 (quotient and remainder)
8. What is the remainder when 23 is divided by 5?
9. Today is Monday. What day is it 100 days from now?
10. Convert 37 to binary.

<details>
<summary>Answers (diagnostic)</summary>

1. 56 · 2. 108 · 3. 918 · 4. 23,548 · 5. 1,242 · 6. 327 remainder 3 · 7. 14 remainder 2 · 8. 3 · 9. Wednesday (100 = 14 weeks + 2 days) · 10. 100101₂

All 10 right and fast: skim Parts 1–5, focus on Parts 6–7. If times-table facts (1–2) were slow, Part 3 is your priority.
</details>

---

## Why this matters

Multiplication and division are everywhere in engineering: bytes per second × seconds, pixels = width × height, items per page, how many packets a file needs. But two ideas from this stage matter far more than the arithmetic itself:

1. **The distributive law** — *a × (b + c) = a×b + a×c*. It's why long multiplication works, it's the core of algebra (M08), and it's how a CPU multiplies using only shifts and adds (Module 06).
2. **Remainders (modulo)** — *what's left over*. Clocks, days of the week, hash tables, ring buffers, checksums, cryptography, and "every Nth item" all run on it. In Python it's the `%` operator. You will use it in nearly every project from Module 01 on.

---

## Part 1 — What multiplication means

Three pictures of 3 × 4:

| Picture | Meaning |
| :-- | :-- |
| **Equal groups** | 3 bags with 4 apples each = 12 apples |
| **Area (array)** | a rectangle 3 rows by 4 columns has 12 squares |
| **Scaling** | 4 stretched to 3 times its length is 12 |

The **area picture** is the most powerful. Keep a mental image of a rectangle whenever you multiply.

### Properties, and why they're true

| Property | Rule | Why (in the area picture) |
| :-- | :-- | :-- |
| **Commutative** | a × b = b × a | Turn the 3-by-4 rectangle on its side: it's 4-by-3, same squares. |
| **Associative** | (a × b) × c = a × (b × c) | A box 2 × 3 × 4: count it as layers of 2×3 four times, or rows of 3×4 twice. Same box, same cubes. |
| **Identity** | a × 1 = a | One group of a is just a. |
| **Zero** | a × 0 = 0 | Zero groups of anything is nothing. |
| **Distributive** | a × (b + c) = a×b + a×c | Split a rectangle of width b + c into two rectangles of widths b and c. Total area = sum of the two areas. |

**The distributive law, drawn.** 7 × 13 = 7 × (10 + 3):

```
        10           3
   +-----------+-------+
 7 |  7×10=70  | 7×3=21|     total = 70 + 21 = 91
   +-----------+-------+
```

Every mental multiplication trick and the whole long-multiplication method are this picture.

---

## Part 2 — What division means

Two meanings of 12 ÷ 3:

- **Sharing** (how many in each group?): 12 cookies shared by 3 people → 4 each.
- **Measuring** (how many groups fit?): how many 3-metre pieces can you cut from a 12-metre cable? → 4 pieces.

Both give 4, but they're different questions. Measuring is the one that explains fraction division in M05, so keep it in mind.

**Division undoes multiplication:** 12 ÷ 3 = 4 because 4 × 3 = 12. Every division can be checked by multiplying back.

### Why you can't divide by zero

- 12 ÷ 3 = 4 because 4 × 3 = 12.
- 12 ÷ 0 = ? would need ? × 0 = 12. But anything × 0 = 0. **No number works.**
- 0 ÷ 0 = ? would need ? × 0 = 0. **Every number works.** So there's no single answer.

Either way, "÷ 0" has no meaningful answer, so we call it **undefined**. (In Python, `12 / 0` raises `ZeroDivisionError`. Now you know why the language refuses.)

But **0 ÷ 12 = 0**, because 0 × 12 = 0. Sharing nothing among 12 people gives each nothing.

---

## Part 3 — Times tables, with strategies

You need the facts up to 12 × 12 in your memory, instantly. Not because calculators don't exist, but because without them every other skill (fractions, factoring, algebra, estimation) becomes slow and error-prone.

**The good news:** there are far fewer facts to learn than the 144 in the table.
- Commutativity halves it (7 × 8 = 8 × 7).
- ×0, ×1, ×2, ×10 are easy.
- Most of the rest have a strategy:

| Facts | Strategy | Example |
| :-- | :-- | :-- |
| ×2 | double | 2 × 8 = 16 |
| ×4 | double, then double again | 4 × 7 = 14 → 28 |
| ×8 | double three times | 8 × 6 = 12 → 24 → 48 |
| ×5 | half of ×10 | 5 × 7 = 70 ÷ 2 = 35 |
| ×9 | ×10 minus one group | 9 × 7 = 70 − 7 = 63 |
| ×3 | ×2 plus one group | 3 × 8 = 16 + 8 = 24 |
| ×6 | ×5 plus one group | 6 × 7 = 35 + 7 = 42 |
| ×11 (up to 9) | repeat the digit | 11 × 7 = 77 |
| ×12 | ×10 plus ×2 | 12 × 7 = 70 + 14 = 84 |
| squares | learn as a list | 6×6=36, 7×7=49, 8×8=64, 9×9=81, 11×11=121, 12×12=144 |

**The hard core** (learn as flashcards): 6×7=42, 6×8=48, 7×7=49, 7×8=56, 8×8=64, 6×9=54, 7×9=63, 8×9=72. Hook for 7 × 8: "**5, 6, 7, 8**" → 56 = 7 × 8.

**Practice:** the strategies first, slowly, for one section. Then flashcards on the 1-3-7-21 spacing schedule. Then a 1-minute timed sheet every session of 30 mixed facts. Target: 30 in 60 seconds, no errors.

> **[W] Why do the strategies work?** Every one is the distributive law. 9 × 7 = (10 − 1) × 7 = 70 − 7. 6 × 7 = (5 + 1) × 7 = 35 + 7. Write three more in this form.

---

## Part 4 — Multiplying by 10, 100, and by 2 in binary

**× 10** shifts every digit one place left and puts a 0 in the ones place: 37 × 10 = 370. *Why?* Every digit's place is now worth 10× more (M01).
**× 100** shifts two places: 37 × 100 = 3,700.
**× 20** = × 2 × 10: 37 × 20 = 74 × 10 = 740.

**In binary, × 2 shifts left one place:** 1011₂ × 2 = 10110₂. Computers do "multiply by 2" this way, and call it a **left shift** (`<<` in Python and C: `11 << 1` is 22).

---

## Part 5 — Long multiplication

### Area model first (to understand)

*Worked example:* **34 × 27**

```
          30         4
     +---------+--------+
  20 | 20×30   | 20×4   |      600 +  80
     |  = 600  |  = 80  |
     +---------+--------+
   7 | 7×30    | 7×4    |      210 +  28
     |  = 210  |  = 28  |
     +---------+--------+
                                total = 600 + 80 + 210 + 28 = 918
```

Split each number by place, multiply every pair, add the pieces. That's the distributive law applied twice.

### The standard method (to be fast)

**Subgoal labels [S]:**
1. **Write the longer number on top**, places lined up.
2. **Multiply the top number by the bottom's ones digit.** Write the result (carrying as you go).
3. **Multiply the top number by the bottom's tens digit.** Because it's tens, **start one place to the left** (write a 0 in the ones place first).
4. **Continue for each digit**, one more place left each time.
5. **Add** the rows.
6. **Check** with an estimate.

*Worked example:* **406 × 58**

```
        4 0 6
      ×   5 8
      -------
      3 2 4 8      ← 406 × 8
  + 2 0 3 0 0      ← 406 × 50  (406 × 5, shifted one place: the 0 is "×10")
  -----------
    2 3 5 4 8
```

Estimate: 400 × 60 = 24,000 ✓ (close to 23,548).

> **[W] Why shift the second row left?** Because the 5 in 58 is really 50. 406 × 50 = 406 × 5 × 10, and × 10 shifts left. The standard method is the area model with the zeros written as a shift.

---

## Part 6 — Long division

Long division looks like a ritual. It's actually **measuring, one place at a time**: "How many 6s fit into 7,452?" answered thousands first, then hundreds, then tens, then ones.

**Subgoal labels [S]:**
1. **Look at the leftmost part** of the number that is at least as big as the divisor.
2. **Divide:** how many times does the divisor fit? Write that digit above.
3. **Multiply** that digit by the divisor; write it below.
4. **Subtract** to find what's left over at this place.
5. **Bring down** the next digit and repeat from step 2.
6. **When no digits remain,** what's left is the remainder.
7. **Check:** quotient × divisor + remainder = original number.

*Worked example:* **7,452 ÷ 6**

```
       1 2 4 2
     ---------
  6 ) 7 4 5 2
      6           ← 6 fits into 7 once (1 thousand groups of 6)
      -
      1 4         ← 1 left, bring down 4 → 14
      1 2         ← 6 fits twice in 14
      ---
        2 5       ← 2 left, bring down 5 → 25
        2 4       ← 6 fits 4 times
        ---
          1 2     ← 1 left, bring down 2 → 12
          1 2     ← 6 fits twice
          ---
            0     ← remainder 0
```

**1,242.** Check: 1,242 × 6 = 7,452 ✓

*What each step means:* "6 into 7" really means "6 into 7 **thousand**": 1 thousand groups of 6 use up 6,000, leaving 1,452. "6 into 14" means "6 into 14 **hundred**": 2 hundred groups, and so on. The ritual is just doing it place by place.

*Worked example with a remainder:* **3,927 ÷ 12**
- 12 into 39 → 3 (36), left 3, bring down 2 → 32.
- 12 into 32 → 2 (24), left 8, bring down 7 → 87.
- 12 into 87 → 7 (84), left **3**.
- **327 remainder 3.** Check: 327 × 12 + 3 = 3,924 + 3 = 3,927 ✓

---

## Part 7 — Remainders and modulo

When a division doesn't come out even, the **remainder** is what's left. The operation that gives just the remainder is called **modulo** (or "mod"):

> 23 ÷ 5 = 4 remainder 3, so **23 mod 5 = 3**.

The remainder is always **less than the divisor**: mod 5 results are always 0, 1, 2, 3, or 4.

**In Python:**
- `23 // 5` → `4` (integer division: how many whole fives)
- `23 % 5` → `3` (modulo: what's left)
- `divmod(23, 5)` → `(4, 3)` (both)

### Modulo is cycling

Modulo is **counting around a circle**. The numbers 0 to *n*−1 are arranged in a ring; mod *n* tells you where you land.

| Problem | Ring size | Calculation |
| :-- | :-- | :-- |
| What day is it 100 days after Monday? | 7 | 100 mod 7 = 2 → two days after Monday → **Wednesday** |
| What time is it 30 hours after 08:00? | 24 | (8 + 30) mod 24 = 38 mod 24 = **14:00** |
| Is 1,234 even? | 2 | 1,234 mod 2 = 0 → **even** |
| A ring buffer has 8 slots. After 29 writes (starting at slot 0), where is the next write? | 8 | 29 mod 8 = **5** |
| An LED blinks every 3rd tick. Is tick 51 a blink? | 3 | 51 mod 3 = 0 → **yes** |

That's the odometer and the clock from M01–M02, now with a name. You'll use `%` constantly: a **hash table** (Module 05) puts an item in bucket `hash % number_of_buckets`; a **ring buffer** (Module 07) wraps its index with `% size`; **checksums** and **cryptography** (Module 03) are built on modular arithmetic.

### Decimal → any base, by repeated division

M01 promised a second method. This is how computers do it.

**Subgoal labels [S]:**
1. **Divide** the number by the base. **The remainder is the next digit, starting from the right.**
2. **Replace** the number with the quotient.
3. **Repeat** until the quotient is 0.
4. **Read the remainders from last to first** (bottom to top).

*Worked example:* **37 → binary**

| Step | Divide | Quotient | Remainder |
| :-- | :-- | :-- | :-- |
| 1 | 37 ÷ 2 | 18 | **1** |
| 2 | 18 ÷ 2 | 9 | **0** |
| 3 | 9 ÷ 2 | 4 | **1** |
| 4 | 4 ÷ 2 | 2 | **0** |
| 5 | 2 ÷ 2 | 1 | **0** |
| 6 | 1 ÷ 2 | 0 | **1** |

Read bottom to top: **100101₂**. Check: 32 + 4 + 1 = 37 ✓

> **[W] Why does this work?**
> 1. The ones digit of any number in base *b* is the number mod *b*. (In base 10: 37 mod 10 = 7, the ones digit. In base 2: 37 mod 2 = 1, the last bit.)
> 2. Why? Because every other place is a multiple of *b*, so it divides evenly; only the ones digit is left over.
> 3. Dividing by *b* (and throwing away the remainder) shifts every digit one place right, so the next digit becomes the new ones digit. Repeat, and you peel off the digits one at a time, right to left.

---

## Practice routine (4 sections)

| Section | Focus |
| :-- | :-- |
| 1 | Session 1: meanings and properties · Session 2: distributive law with rectangles · Sessions 3–5: times-table strategies (one strategy group per session), start flashcards |
| 2 | Sessions 1–2: ×10, ×100, shifts · Sessions 3–4: area model, then standard long multiplication · Session 5: Practice Set 1, items 1–9 |
| 3 | Session 1: division meanings, division by zero · Sessions 2–4: long division · Session 5: Practice Set 1, items 10–14 + cumulative |
| 4 | Sessions 1–2: modulo and cycles · Session 3: base conversion by division · Session 4: Practice Set 1 rest + Set 2 · Session 5: self-check |

**Every session:**
- **Warm-up [R]:** the long-division subgoal labels from memory, then one problem.
- **Facts minute:** 30 mixed times-table facts in 60 seconds (paper or flashcards). Log the score.
- **Prime Factory:** start [Milestone 1](projects/prime-factory/spec.md) in section 4.

**Key why-questions [W]:**
1. Why does the distributive law hold? (Draw it.)
2. Why do we shift each row left in long multiplication?
3. Why can't we divide by zero? Why is 0 ÷ 5 fine?
4. Why does repeated division by 2 give the binary digits?

**Feynman target [F]:** *"What is modulo, and where does it show up in real life?"* Five examples, no jargon, out loud.

---

## Practice sets

### Practice Set 1 — Mixed (20 problems, no calculator)

1. 6 × 7 · 2. 8 × 9 · 3. 12 × 12 · 4. 25 × 4 · 5. 48 × 5 (by halving 480)
6. 99 × 7 (distributive: 100 × 7 − 7) · 7. 23 × 45 · 8. 312 × 24 · 9. 1,205 × 37
10. 864 ÷ 4 · 11. 945 ÷ 7 · 12. 5,040 ÷ 12 · 13. 1,000 ÷ 8 · 14. 2,023 ÷ 9 (quotient and remainder)
15. 50 mod 7 · 16. 1,000 mod 16
17. Convert 45 to binary by repeated division.
18. Convert 200 to hex by repeated division.
19. A day has 1,440 minutes. How many full 25-minute study blocks fit in a day? How many minutes are left?
20. A ring buffer has 8 slots, numbered 0–7. Writing starts at slot 0 and moves one slot each write, wrapping around. After 29 writes, which slot is next?

<details>
<summary>Answers (Set 1)</summary>

1. 42 · 2. 72 · 3. 144 · 4. 100 · 5. 240 · 6. 693 · 7. 1,035 · 8. 7,488 · 9. 44,585 · 10. 216 · 11. 135 · 12. 420 · 13. 125 · 14. 224 remainder 7 · 15. 1 · 16. 8 · 17. 101101₂ · 18. C8₁₆ (200 ÷ 16 = 12 r 8; 12 ÷ 16 = 0 r 12 = C) · 19. 57 blocks, 15 minutes left · 20. slot 5 (29 mod 8)
</details>

### Practice Set 2 — Think about it (5 problems)

1. Use the distributive law to find 7 × 98 in your head. Write the steps.
2. Draw 13 × 6 as a rectangle split into two parts. Explain how the drawing shows the distributive law.
3. Explain, without the word "undefined," why 5 ÷ 0 has no answer but 0 ÷ 5 = 0.
4. Why is the last digit of a decimal number equal to the number mod 10? What does the last bit of a binary number tell you about the number?
5. A 3-hour lab starts at 11:00. Using mod 12, what time does it end on a 12-hour clock? (Careful: 12-hour clocks show 12, not 0. How would you handle that?)

<details>
<summary>Answers (Set 2)</summary>

1. 7 × 98 = 7 × (100 − 2) = 700 − 14 = 686.
2. 13 × 6 = (10 + 3) × 6: one 10-by-6 rectangle (60) next to a 3-by-6 rectangle (18). Together they are the 13-by-6 rectangle: 60 + 18 = 78.
3. 5 ÷ 0 asks "what times 0 is 5?" — nothing works, because anything times 0 is 0. 0 ÷ 5 asks "what times 5 is 0?" — 0 works.
4. Every place except the ones place is a multiple of 10, so dividing by 10 leaves only the ones digit as remainder. The last bit is the number mod 2: 0 means even, 1 means odd.
5. (11 + 3) mod 12 = 14 mod 12 = 2 → 2:00. The 12-hour clock problem: 12:00 would come out as 0 mod 12. A common fix is to compute mod 12 and then show 0 as 12. (Programs that display 12-hour time do exactly this. It's a classic bug when forgotten.)
</details>

---

## Watch, practise, and play

*Companions, not replacements: the lessons above come first. Use the [V protocol](../../study-protocols.md#v--watch-actively). Full list: [courses-and-videos.md](../../courses-and-videos.md#foundations-math).*

- **Watch:** Math Antics: multiplication and long division. Khan Academy: multiplication and division. Numberphile (YouTube): a fun video on remainders or divisibility.
- **Practise:** Khan Academy multiplication and division practice; times-table flashcards.
- **Play** ([puzzles and games](puzzles-and-games.md)): times-table bingo · the 24 game · the missing-digit trick · 1089

---

## Self-check (cold, no calculator)

1. 9 × 7, 11 × 12, 6 × 8, 7 × 7 (all from memory)
2. 57 × 86
3. 2,304 × 15
4. 6,384 ÷ 8
5. 9,876 ÷ 24 (quotient and remainder; check it)
6. 125 mod 12
7. Convert 99 to binary by repeated division.
8. Convert 255 to hex by repeated division.
9. Three printers each print 45 pages per minute. How many minutes to print 2,700 pages? (Pólya.)
10. **[R] Blank sheet:** meanings of × and ÷, the five properties with reasons, long multiplication and long division as subgoal labels, what modulo means with three examples.

<details>
<summary>Answers (self-check)</summary>

1. 63, 132, 48, 49 · 2. 4,902 · 3. 34,560 · 4. 798 · 5. 411 remainder 12 (411 × 24 + 12 = 9,864 + 12 = 9,876 ✓) · 6. 5 · 7. 1100011₂ · 8. FF₁₆ · 9. 3 × 45 = 135 pages per minute; 2,700 ÷ 135 = 20 minutes
</details>

## Done when

- [ ] Self-check ≥ 8/9 on items 1–9, blank sheet done.
- [ ] Facts minute: 30 facts in 60 seconds, no errors, three sessions in a row.
- [ ] Four why-questions answered; Feynman recording made.
- [ ] [Prime Factory](projects/prime-factory/spec.md) Milestone 1 done.

**Next:** [M04 — Factors, Primes, and Divisibility](M04-factors-primes-and-divisibility.md).
