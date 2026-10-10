---
title: "M02 — Addition and Subtraction"
stage: M02
track: math
hours: 20
weeks: 3
---

# M02 — Addition and Subtraction

**In this stage you will:** understand what adding and subtracting really mean, use their properties to calculate in your head, learn exactly why carrying and borrowing work, add in binary, hex, and clock time, and solve word problems with a four-step method.

**Time:** about 20 hours over 3 weeks.

**Before you start:** M01 done. You can write any number in expanded form.

---

## Diagnostic (cold, 15 minutes, no calculator)

1. 47 + 38
2. 503 − 278
3. 6,005 − 1,987
4. 2,486 + 7,519
5. Estimate 4,912 + 3,107 to the nearest thousand.
6. 1011₂ + 0110₂ (answer in binary)
7. 2 hours 45 minutes + 1 hour 30 minutes
8. What number plus 356 makes 1,000?
9. 9,000 − 1
10. Is a − b always equal to b − a? Give an example.

<details>
<summary>Answers (diagnostic)</summary>

1. 85 · 2. 225 · 3. 4,018 · 4. 10,005 · 5. about 8,000 · 6. 10001₂ · 7. 4 hours 15 minutes · 8. 644 · 9. 8,999 · 10. No. 5 − 3 = 2, but 3 − 5 = −2 (or "can't be done" with whole numbers).

9–10 right: skim Parts 1–5 and spend your time on Parts 6–8.
</details>

---

## Why this matters

You've added and subtracted all your life. This stage is about doing it **reliably** and **knowing why it works**, because the same mechanics run inside every computer. The carry in column addition is exactly the carry signal you'll wire between logic gates when you build an adder in Module 04, and that adder is the heart of the CPU you'll design in Module 06. Binary subtraction with borrowing leads straight to how computers store negative numbers (M07).

Mental strategies matter too. Engineers estimate constantly: "Is this 3 MB or 300 MB? Will it fit?" Fast, rough, correct-ish arithmetic in your head catches mistakes before they cost hours.

---

## Part 1 — What addition and subtraction mean

**Addition** has two everyday meanings:
- **Combining:** 3 apples and 4 apples make 7 apples.
- **Moving right on the number line:** start at 3, move 4 steps right, land on 7.

**Subtraction** has three:
- **Taking away:** 7 apples, eat 4, 3 are left.
- **Difference (distance):** how far is it from 4 to 7 on the number line? 3.
- **Missing part:** 4 plus what makes 7? 3.

**Subtraction undoes addition.** If 4 + 3 = 7, then 7 − 3 = 4 and 7 − 4 = 3. This is called being **inverse** operations. It gives you a free check for every subtraction: add the answer back.

> 503 − 278 = 225? Check: 225 + 278 = 503 ✓

---

## Part 2 — Properties of addition (and why they're true)

| Property | Rule | Example | Why it's true |
| :-- | :-- | :-- | :-- |
| **Commutative** (order doesn't matter) | a + b = b + a | 8 + 5 = 5 + 8 | Combining two piles gives the same total whichever you pick up first. |
| **Associative** (grouping doesn't matter) | (a + b) + c = a + (b + c) | (7 + 6) + 4 = 7 + (6 + 4) | Three piles become one pile; the order you merge them doesn't change what's in it. |
| **Identity** (adding zero) | a + 0 = a | 9 + 0 = 9 | Adding nothing changes nothing. |

**Subtraction has none of the first two.** 7 − 4 ≠ 4 − 7, and (10 − 5) − 2 = 3 but 10 − (5 − 2) = 7. *Why?* Because subtraction has a direction: you start from one specific number and remove from it. Swapping which number you start from changes the problem.

**Why care?** These properties are what let you rearrange sums to make them easy. 7 + 6 + 4 is hard-ish; 7 + (6 + 4) = 7 + 10 = 17 is easy. Every mental trick below is one of these properties in disguise.

---

## Part 3 — Mental strategies

Try each one on paper first, then in your head.

| Strategy | How | Example |
| :-- | :-- | :-- |
| **Make a ten** | Split one number to fill the other up to a ten | 8 + 5 = 8 + 2 + 3 = 10 + 3 = 13 |
| **Split by place** | Add tens and ones separately | 47 + 38 = (40 + 30) + (7 + 8) = 70 + 15 = 85 |
| **Compensate** | Round one number, then fix | 49 + 26 = 50 + 26 − 1 = 75 |
| **Count up** (subtraction) | Jump from the smaller number to the bigger in easy steps | 1,000 − 356: 356 → 400 is 44; 400 → 1,000 is 600; total **644** |
| **Same difference** (subtraction) | Add the same amount to both numbers; the distance between them doesn't change | 503 − 278 = 505 − 280 = **225** |

> **[W] Why does "same difference" work?** Subtraction can mean *distance on the number line*. If you slide both numbers 2 steps to the right, the distance between them is the same. 503 and 278 are exactly as far apart as 505 and 280.

---

## Part 4 — Column addition and why carrying works

For bigger numbers, use columns.

**Subgoal labels [S]:**
1. **Line up the places:** ones under ones, tens under tens.
2. **Add the ones column.**
3. **If the column total is 10 or more, write its ones digit and carry the ten** to the next column as a 1.
4. **Move left; add that column including any carry.** Repeat.
5. **Write any final carry** at the far left.
6. **Check** with an estimate.

*Worked example:* **2,486 + 7,519**

```
   ¹ ¹ ¹        ← carries
   2 4 8 6
 + 7 5 1 9
 ---------
 1 0 0 0 5
```

- Ones: 6 + 9 = 15 → write **5**, carry 1.
- Tens: 8 + 1 + (carry 1) = 10 → write **0**, carry 1.
- Hundreds: 4 + 5 + 1 = 10 → write **0**, carry 1.
- Thousands: 2 + 7 + 1 = 10 → write **0**, carry 1.
- Final carry: **1**. Answer **10,005**. Estimate: 2,500 + 7,500 = 10,000 ✓

> **[W] Why does carrying work?**
> 1. When the ones column adds up to 15, that's 15 ones.
> 2. 15 ones = 1 ten + 5 ones (that's just M01: regroup ten of a place into one of the next).
> 3. The ones place can only hold one digit, so the 5 stays and the 1 ten moves to the tens column, where it belongs. **Carrying is regrouping.** Nothing magic. And in binary, the same thing happens, but at 2 instead of 10.

---

## Part 5 — Column subtraction and why borrowing works

**Subgoal labels [S]:**
1. **Line up the places.** Bigger number on top.
2. **Start at the ones.** If the top digit is big enough, subtract.
3. **If the top digit is too small, borrow:** take 1 from the next place to the left (it goes down by 1) and add 10 to this place.
4. **If the next place is 0, keep going left** until you find a non-zero digit; borrow from it, and every 0 you passed becomes 9.
5. **Subtract each column.**
6. **Check** by adding the answer to the bottom number.

*Worked example:* **6,005 − 1,987** (the "zeros" case)

```
   5 9 9 15    ← after borrowing
   6 0 0  5
 − 1 9 8  7
 ----------
   4 0 1  8
```

- Ones: 5 − 7 won't work. Next places are 0 and 0. Go all the way to the 6 thousands.
- Borrow: 6 thousands → 5 thousands, and the 1 thousand you took becomes 10 hundreds. Take 1 of those hundreds → 9 hundreds, giving 10 tens. Take 1 ten → 9 tens, giving 10 ones. Ones become 5 + 10 = 15.
- Now: 15 − 7 = **8**; 9 − 8 = **1**; 9 − 9 = **0**; 5 − 1 = **4**. Answer **4,018**.
- Check: 4,018 + 1,987 = 6,005 ✓

> **[W] Why does borrowing work?** 6,005 is still 6,005 after you rewrite it as 5 thousands + 9 hundreds + 9 tens + 15 ones (check: 5,000 + 900 + 90 + 15 = 6,005). You didn't change the number; you changed how it's grouped, so every column has enough to subtract. **Borrowing is regrouping in reverse.**

**The most common error:** subtracting the smaller digit from the bigger one in each column, no matter which is on top. 600 − 247 done that way gives 447 (wrong; the answer is 353). The check by addition catches it instantly: 447 + 247 = 694 ≠ 600.

---

## Part 6 — Adding in other bases

The column method works in **every** base. The only change: **carry when a column reaches the base**, not 10.

### Binary (carry at 2)

The facts: 0 + 0 = 0 · 0 + 1 = 1 · 1 + 1 = **10₂** (write 0, carry 1) · 1 + 1 + 1 = **11₂** (write 1, carry 1).

*Worked example:* **1011₂ + 0110₂** (11 + 6)

```
  ¹ ¹ ¹
    1 0 1 1
  + 0 1 1 0
  ---------
  1 0 0 0 1
```

- 1 + 0 = 1. 1 + 1 = 10 → 0, carry 1. 0 + 1 + 1 = 10 → 0, carry 1. 1 + 0 + 1 = 10 → 0, carry 1. Final carry 1.
- **10001₂** = 17 ✓ (11 + 6 = 17)

This is exactly what the adder circuit you build in Module 04 does, one column at a time.

### Hexadecimal (carry at 16)

*Worked example:* **3A₁₆ + 15₁₆**
- Ones: A + 5 = 10 + 5 = 15 = **F** (no carry, since 15 < 16).
- Sixteens: 3 + 1 = **4**.
- **4F₁₆** (check: 58 + 21 = 79 = 4×16 + 15 ✓)

*Worked example:* **9₁₆ + 8₁₆** = 17 = one 16 + one 1 = **11₁₆**.

### Clock time (carry at 60, then at 24 or 12)

*Worked example:* **2:45 + 1:30**
- Minutes: 45 + 30 = 75. 75 ≥ 60, so write 75 − 60 = **15**, carry 1 hour.
- Hours: 2 + 1 + 1 = **4**. Answer **4:15**.

*Subtracting time:* **10:20 − 3:45**. Minutes: 20 − 45 won't work; borrow 1 hour = 60 minutes → 80 − 45 = **35**. Hours: 9 − 3 = **6**. Answer **6:35**.

Clocks also roll over: 23:40 + 0:35 on a 24-hour clock = 24:15 → **00:15** (the next day). That rollover is the odometer from M01 again, and it's the "remainder" idea you'll formalise in M03.

---

## Part 7 — Word problems with Pólya's four steps

George Pólya's method (see [LM14](<../../02 - Atlas/LM14 - Pólya's Problem Solving.md>)) works on every word problem you'll ever meet, including engineering ones.

1. **Understand.** What do you know? What do you want? Underline numbers and units. Restate the question in your own words.
2. **Plan.** Which operation, and *why*? (Combining → add. Difference, remaining, how much more → subtract.) Draw a bar or a number line if unsure.
3. **Carry out.** Calculate carefully.
4. **Look back.** Is the answer the right size (estimate)? Does it have units? Does it answer the actual question?

*Worked example:* A download is 4,700 MB. So far 2,950 MB have arrived. How much is left?
1. Know: total 4,700 MB, done 2,950 MB. Want: remaining.
2. "Remaining" = total − done → subtract.
3. 4,700 − 2,950: count up: 2,950 → 3,000 is 50; 3,000 → 4,700 is 1,700; total **1,750 MB**.
4. Estimate: 4,700 − 3,000 ≈ 1,700 ✓. Units: MB ✓. Answers "how much is left" ✓.

---

## Practice routine (3 weeks)

| Week | Focus |
| :-- | :-- |
| 1 | Mon: meanings and inverse · Tue: properties (write the "why" for each) · Wed–Thu: mental strategies (20 problems/day in your head, then check on paper) · Fri: Practice Set 1, items 1–10 |
| 2 | Mon: column addition · Tue–Wed: column subtraction, especially with zeros · Thu: binary and hex addition · Fri: Practice Set 1, all |
| 3 | Mon: clock time · Tue: word problems with Pólya · Wed: Base Workshop Milestone 3 · Thu: Practice Set 2 + Feynman · Fri: self-check |

**Daily warm-up [R]:** write the subgoal labels for column subtraction from memory, then do one problem with zeros in the top number.
**Mental-math minute:** every day, 10 two-digit additions and subtractions in your head, timed. Log the time. It falls fast.

**Key why-questions [W]:**
1. Why does carrying work? (Answer it for base 10 and base 2.)
2. Why does borrowing across zeros turn the zeros into 9s (in base 10) and into 1s (in binary)?
3. Why isn't subtraction commutative?
4. Why does "same difference" work?

**Feynman target [F]:** *"Why do we carry?"* Explain to a friend with coins or bundles of sticks, no jargon. Record it (2 minutes).

---

## Practice sets

### Practice Set 1 — Mixed (20 problems, no calculator)

1. 58 + 67
2. 300 − 146
3. 4,729 + 3,586
4. 7,002 − 3,458
5. 12,345 + 67,890
6. 10,000 − 2,763
7. 999 + 999 (do it in your head)
8. 8,001 − 7,999 (in your head)
9. 49 + 37 (in your head, by compensation)
10. 1,000 − 463 (in your head, by counting up)
11. 1101₂ + 0111₂
12. 1111₂ + 1₂
13. 1000₂ − 0001₂
14. 3A₁₆ + 15₁₆
15. FF₁₆ + 1₁₆
16. 1:50 + 0:45
17. 10:20 − 3:45
18. 2,750 + ___ = 5,000
19. A download is 4,700 MB; 2,950 MB are done. How much is left? (Use Pólya; write all four steps.)
20. You have $1,240. You spend $385 and $97, then earn $450. How much do you have now?

<details>
<summary>Answers (Set 1)</summary>

1. 125 · 2. 154 · 3. 8,315 · 4. 3,544 · 5. 80,235 · 6. 7,237 · 7. 1,998 (1,000 + 1,000 − 2) · 8. 2 (they're 2 apart on the number line) · 9. 86 (50 + 37 − 1) · 10. 537 · 11. 10100₂ (13 + 7 = 20) · 12. 10000₂ · 13. 0111₂ (8 − 1 = 7) · 14. 4F₁₆ · 15. 100₁₆ · 16. 2:35 · 17. 6:35 · 18. 2,250 · 19. 1,750 MB · 20. $1,208
</details>

### Practice Set 2 — Think about it (5 problems)

1. Explain why 503 − 278 gives the same answer as 505 − 280.
2. A student wrote 600 − 247 = 447. What did they do wrong? How would checking by addition have caught it?
3. In binary, what is 1 + 1 + 1? Why do you need this fact when adding two binary numbers?
4. An 8-bit counter shows 11111111. What does it show after adding 1? What happened to the carry?
5. Your train leaves at 22:50 and takes 2 hours 25 minutes. When does it arrive (24-hour clock)?

<details>
<summary>Answers (Set 2)</summary>

1. Both numbers moved 2 steps right on the number line, so the distance between them didn't change.
2. In each column they subtracted the smaller digit from the larger (7 − 0, 4 − 0, 6 − 2) instead of borrowing. Check: 447 + 247 = 694, not 600. Correct answer: 353.
3. 1 + 1 + 1 = 11₂ (three = one 2 and one 1). You need it because a column can contain two 1-digits *plus* a carry from the column to the right.
4. 00000000. The carry out of the leftmost bit has no place to go and is lost: **overflow** (M01's odometer).
5. 22:50 + 2:25: minutes 50 + 25 = 75 → 15, carry 1 hour; hours 22 + 2 + 1 = 25 → 25 − 24 = 1. Arrives at **01:15** the next day.
</details>

---

## Self-check (cold, 30 minutes, no calculator)

1. 6,284 + 3,759
2. 5,000 − 2,371
3. 40,305 − 18,768
4. 2,999 + 4,002 (in your head)
5. Estimate 7,912 − 3,089, then compute it exactly.
6. 10110₂ + 01011₂ (answer in binary, then check in decimal)
7. 2F₁₆ + 2F₁₆
8. 23:40 + 0:35 on a 24-hour clock
9. A game save file is 1,250 MB. Your drive has 3,100 MB free. After saving two copies, how much is free? (Pólya, all four steps.)
10. **[R] Blank sheet (10 min):** the meanings of addition and subtraction, the three properties with reasons, the subgoal labels for carrying and borrowing, and how other bases change the method.

<details>
<summary>Answers (self-check)</summary>

1. 10,043 · 2. 2,629 · 3. 21,537 · 4. 7,001 · 5. about 4,800 (7,900 − 3,100); exactly 4,823 · 6. 100001₂ = 33 (22 + 11 ✓) · 7. 5E₁₆ (47 + 47 = 94) · 8. 00:15 · 9. 3,100 − 2×1,250 = 3,100 − 2,500 = 600 MB (look back: 600 is less than one more copy, so a third copy wouldn't fit — useful to know)
</details>

## Done when

- [ ] Self-check ≥ 8/9 on items 1–9, and the blank sheet done.
- [ ] Mental-math minute: 10 problems in under 60 seconds with no errors.
- [ ] Four why-questions answered in writing; Feynman recording made.
- [ ] [Base Workshop](projects/base-workshop/spec.md) Milestone 3 done.

**Next:** [M03 — Multiplication and Division](M03-multiplication-and-division.md).
