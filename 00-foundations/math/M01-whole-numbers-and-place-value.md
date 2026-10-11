---
title: "M01 — Whole Numbers and Place Value"
id: "M01"
type: "lesson"
module: "00-foundations"
track: "math"
stage: "M01"
phase: "A"
order: 140
prerequisites: []
---

# M01 — Whole Numbers and Place Value

**In this stage you will:** understand exactly how our number system works — digits, places, and zero — read and write large numbers, compare and round them, and then use the same idea to count in base 2 (binary), base 5, and base 16 (hexadecimal), the number systems computers use.

---

## Diagnostic (cold)

Do these on paper before reading anything. Check with the answers. If you get 9 or 10 right, skim Parts 1–4 and go straight to Part 5 (bases).

1. What does the 7 mean in 4,705?
2. Write 30,042 in expanded form (as a sum of each digit times its place).
3. Write in digits: two million, forty thousand, six.
4. Which is bigger: 98,999 or 100,001?
5. Round 4,682 to the nearest hundred.
6. Round 4,682 to the nearest thousand.
7. What number is 1 more than 3,999?
8. What is the binary number 1011 in ordinary (decimal) numbers?
9. Write 13 in binary.
10. What is the hexadecimal number 1F in decimal?

<details>
<summary>Answers (diagnostic)</summary>

1. 7 hundreds (700) · 2. 3×10,000 + 0×1,000 + 0×100 + 4×10 + 2×1 · 3. 2,040,006 · 4. 100,001 · 5. 4,700 · 6. 5,000 · 7. 4,000 · 8. 11 · 9. 1101 · 10. 31
</details>

---

## Why this matters

Place value is the single most important idea in arithmetic, and it is also how every computer stores every number, letter, colour, and instruction. The *only* difference between our numbers and a computer's is the number of digits: we use ten (0–9), a computer uses two (0 and 1). Same idea, different base.

Once you understand place value deeply:
- carrying and borrowing (M02) and long multiplication and division (M03) stop being tricks and become obvious;
- binary and hexadecimal stop being scary; you'll read `0xFF`, `#FF8800`, and `11111111` as easily as 255;
- in [01 Intro CS Taste](../../01-intro-cs-taste/overview.md), you'll build a tiny computer whose memory is a list of numbers between 0 and 255. That's 8 binary digits each, which you'll understand from this stage.

---

## Part 1 — Digits and places

We write every number with just ten symbols, the **digits** 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. How do ten symbols name infinitely many numbers? **Position.** A digit's value depends on *where* it is.

| Place | … | ten-thousands | thousands | hundreds | tens | ones |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Value of a 1 here | … | 10,000 | 1,000 | 100 | 10 | 1 |

**Each place is worth 10 times the place to its right.** Ten ones make a ten. Ten tens make a hundred. Ten hundreds make a thousand. This is the whole system.

So **4,705** means:

> 4 thousands + 7 hundreds + 0 tens + 5 ones
> = 4×1,000 + 7×100 + 0×10 + 5×1
> = 4,000 + 700 + 0 + 5

That way of writing it is called **expanded form**. It is the key that unlocks everything in this stage.

### Why zero matters

Without a symbol for "nothing in this place," you couldn't tell **305** from **35**. Zero is a **placeholder**: it holds a place open so the other digits stay in their right positions.

This sounds obvious, but it took humans thousands of years. Roman numerals had no zero and no place value (CCCV = 305: you add up the symbols), which made arithmetic with them miserable. Place value with zero came from India, reached Europe through Arabic mathematicians, and is why we call our digits Hindu-Arabic numerals. Lockhart's *Arithmetic* tells this story well, if you want more.

> **[W] Why-ladder: why is each place worth ten times the one before?**
> 1. Because we group in tens: when we have ten of something, we bundle them into one of the next size.
> 2. Why tens? Because we have ten fingers. Many cultures counted on fingers, so ten was the natural bundle size.
> 3. Does it have to be ten? No. Any number of two or more works. The Babylonians used sixty (that's why there are 60 minutes in an hour). Computers use two. **The rule "each place is worth *base* times the one before" works for any base.** Hold on to this; it's Part 5.

---

## Part 2 — Big numbers

For big numbers, we group digits in **threes from the right**, with commas: **5,300,020**. Each group has a name:

| Group | billions | millions | thousands | (ones) |
| :-- | :-- | :-- | :-- | :-- |
| Example | 3 | 041 | 500 | 207 |

**3,041,500,207** = *three billion, forty-one million, five hundred thousand, two hundred seven.*

**Reading a big number:**
1. Split into groups of three from the right.
2. Read each group as a number from 0 to 999.
3. Say the group's name after it (billion, million, thousand). Skip groups that are 000.

**Writing a big number from words:**
1. Write a group for each name you hear, with three digits each.
2. Fill groups you didn't hear with 000; pad short groups with leading zeros (forty-one → 041).
3. Remove leading zeros from the very first group only.

*Example:* "two million, forty thousand, six" → millions: 2 · thousands: 040 · ones: 006 → **2,040,006**.

(Code note: computers don't use the commas. In Python you write `2040006` or `2_040_006`.)

---

## Part 3 — Comparing and ordering

**To compare two whole numbers:**
1. **More digits = bigger** (as long as neither starts with zeros). 100,001 (6 digits) > 98,999 (5 digits).
2. **Same number of digits:** compare from the left. The first place where they differ decides it. 4,**7**05 > 4,**6**99 because 7 hundreds > 6 hundreds.

> **[W] Why does rule 2 work?** Because the leftmost place is worth more than *all* the places to its right put together. 1 hundred (100) is more than 9 tens + 9 ones (99). So once the left digits differ, nothing to the right can change the answer.

---

## Part 4 — The number line, rounding, and estimating

Picture the whole numbers as evenly spaced points on a line: 0, 1, 2, 3, … going right forever. Bigger numbers are further right.

**Rounding** replaces a number with the nearest "round" number at some place, to make it easier to work with.

**Subgoal labels [S] for rounding:**
1. **Find the rounding place** (e.g. hundreds).
2. **Look at the digit just to its right.**
3. **If it's 5 or more, round up:** add 1 to the rounding place. **If it's 4 or less, keep** the rounding place.
4. **Replace every digit to the right with 0.**

*Worked example:* round **4,682** to the nearest hundred.
1. Rounding place: hundreds → the **6**.
2. Digit to its right: **8**.
3. 8 ≥ 5, so round up: 6 → 7.
4. Zeros after: **4,700**.

*Worked example (with a carry):* round **649,999** to the nearest thousand.
1. Thousands digit: **9** (in 64**9**,999).
2. Next digit: **9**.
3. Round up: 9 + 1 = 10 — so write 0 and carry 1 into the ten-thousands: 64 → 65.
4. **650,000**.

> **[W] Why "5 or more rounds up"?** 4,682 is between 4,600 and 4,700. It's 82 away from 4,600 and 18 away from 4,700, so 4,700 is nearer. The digit after the rounding place tells you which half of the gap you're in. Exactly halfway (like 4,650) is a tie; "round up" is just the usual convention. (Computers sometimes use other tie rules; you'll see why in M06.)

**Estimating** = rounding first, then doing the arithmetic, to get a quick approximate answer. You'll use it constantly to **check** exact answers: if your exact answer is far from the estimate, something's wrong.

---

## Part 5 — Other bases

Here is the big idea from Part 1's why-ladder: **place value works with any base.** In base *b*, there are *b* digits (0 to *b*−1), and each place is worth *b* times the place to its right.

### Base 5 (count on one hand)

Digits: 0, 1, 2, 3, 4. Places: 1, 5, 25, 125, 625, …

Count: 1, 2, 3, 4, **10** (one five, zero ones), 11, 12, 13, 14, **20**, … 44, **100** (one twenty-five).

We write the base as a small number after: **243₅** means 2×25 + 4×5 + 3×1 = 50 + 20 + 3 = **73**.

### Base 2 — binary

Digits: **0, 1**. Places: 1, 2, 4, 8, 16, 32, 64, 128, 256, …(each one doubles).

| Decimal | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Binary | 0 | 1 | 10 | 11 | 100 | 101 | 110 | 111 | 1000 | 1001 | 1010 |

A binary digit is called a **bit**. Eight bits make a **byte**. A byte can hold the numbers 00000000 to 11111111, which is 0 to 255. (That's 256 different values: remember this number; you'll see it constantly.)

**Why do computers use binary?** Because it's easy to build reliable switches with two states: on/off, high voltage/low voltage, charged/uncharged. Telling ten voltage levels apart reliably is much harder. You'll build these switches into adders in Module 04.

In code, binary numbers are written with `0b` in front: `0b1011` is 11.

### Base 16 — hexadecimal ("hex")

Digits: 0–9, then **A=10, B=11, C=12, D=13, E=14, F=15**. Places: 1, 16, 256, 4,096, 65,536, …

In code, hex is written with `0x` in front: `0x1F` = 1×16 + 15×1 = **31**.

**Why do programmers use hex?** Because **one hex digit is exactly four bits** (16 = 2×2×2×2). So a byte (8 bits) is exactly **two** hex digits, and long binary numbers become short and readable:

> 1010 1111₂ → split into groups of four → 1010 = A, 1111 = F → **AF₁₆** (= 175)

You've seen hex already: web colours like `#FF8800` are three bytes (red FF = 255, green 88 = 136, blue 00 = 0). Memory addresses, error codes, and network addresses are often in hex.

| Binary | Hex | Decimal | | Binary | Hex | Decimal |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 0000 | 0 | 0 | | 1000 | 8 | 8 |
| 0001 | 1 | 1 | | 1001 | 9 | 9 |
| 0010 | 2 | 2 | | 1010 | A | 10 |
| 0011 | 3 | 3 | | 1011 | B | 11 |
| 0100 | 4 | 4 | | 1100 | C | 12 |
| 0101 | 5 | 5 | | 1101 | D | 13 |
| 0110 | 6 | 6 | | 1110 | E | 14 |
| 0111 | 7 | 7 | | 1111 | F | 15 |

Learn this table by heart (flashcards). It pays off for the rest of your career.

### Converting any base → decimal

**Subgoal labels [S]:**
1. **Write the place values** above the digits, starting with 1 on the right, multiplying by the base each step left.
2. **Multiply** each digit by its place value.
3. **Add** the results.

*Worked example:* **110010₂** → decimal.
1. Places (right to left): 1, 2, 4, 8, 16, 32 → over the digits: 32 16 8 4 2 1 / 1 1 0 0 1 0
2. Multiply: 32×1, 16×1, 8×0, 4×0, 2×1, 1×0 → 32, 16, 0, 0, 2, 0
3. Add: 32 + 16 + 2 = **50**.

*Worked example:* **3E8₁₆** → decimal.
1. Places: 256, 16, 1.
2. 3×256 = 768; E is 14, 14×16 = 224; 8×1 = 8.
3. 768 + 224 + 8 = **1,000**.

### Converting decimal → any base ("largest place that fits")

**Subgoal labels [S]:**
1. **List the place values** of the target base up to the first one bigger than your number.
2. **Starting from the largest place that fits**, ask: how many of this place fit into what's left? Write that digit. Subtract.
3. **Move to the next place right.** Repeat until you reach the ones place. (Places where nothing fits get a 0.)
4. **Check** by converting back.

*Worked example:* **200** → binary.
1. Places: 1, 2, 4, 8, 16, 32, 64, 128 (256 is too big).
2. 128 fits once → **1**, left 72. 64 fits once → **1**, left 8. 32 doesn't fit → **0**. 16 → **0**. 8 fits → **1**, left 0. 4 → **0**. 2 → **0**. 1 → **0**.
3. Read the digits: **11001000₂**.
4. Check: 128 + 64 + 8 = 200 ✓.

*Worked example:* **38** → base 5.
1. Places: 1, 5, 25 (125 too big).
2. 25 fits once → **1**, left 13. 5 fits twice → **2**, left 3. 1 fits three times → **3**.
3. **123₅**. 4. Check: 25 + 10 + 3 = 38 ✓.

(In M03 you'll learn a second method using division, which is how computers do it.)

### Counting and rollover: the odometer

A car's odometer counts in base 10 with a fixed number of digits. When a digit passes 9, it rolls over to 0 and pushes 1 into the next place: 0199 → 0200. When *all* the digits are 9 and you add 1, it rolls over to all zeros: 9999 → 0000. The extra 1 has nowhere to go and is lost.

Binary counts the same way, but rolls over at 1: 0111 → 1000. A 4-bit counter goes 1111 → 0000.

This "nowhere to go" is called **overflow**, and it is a real source of computer bugs (and of some famous disasters). Computers store numbers in a fixed number of bits, exactly like an odometer with a fixed number of wheels. You'll meet it again in M07 (negative numbers in fixed width) and Module 06.

---

## Practice routine (3 sections)

| Section | Focus |
| :-- | :-- |
| 1 | Session 1: places and expanded form · Session 2: zero and big numbers · Session 3: comparing · Session 4: rounding · Session 5: Practice Set 1 (items 1–5) + cumulative |
| 2 | Session 1: base 5 by hand (use coins: 5 pennies = a nickel, 5 nickels = a "quarter-plus") · Session 2: binary counting 0–32 out loud · Session 3: binary ↔ decimal · Session 4: hex and the binary-hex table · Session 5: Practice Set 1 (all) |
| 3 | Sessions 1–2: [Base Workshop](projects/base-workshop/spec.md) Milestones 1–2 · Session 3: Practice Set 2 · Session 4: Feynman pass · Session 5: self-check |

**Warm-up [R] (every session):** write the place values for bases 10, 2, and 16 from memory (up to five places), and convert one random number.
**Flashcards:** the 16-row binary/hex table, powers of 2 up to 2¹⁰ = 1,024.

**Key why-questions [W]** (answer each in writing during the stage):
1. Why is each place worth *base* times the one to its right?
2. Why does one hex digit correspond to exactly four bits?
3. Why is the biggest 8-bit number 255 and not 256?
4. Why does adding 1 to 0111₂ give 1000₂? (Answer it the same way you'd explain 0999 + 1 = 1000.)

**Feynman target [F]:** *"What does the position of a digit mean, and why do we need zero?"* Explain it in plain words in under 200 words, then out loud, briefly, without using the words "place value." Then explain how binary is the same idea.

---

## Practice sets

### Practice Set 1 — Mixed (20 problems)

1. What is the value of the digit 6 in 360,512?
2. Write 7,093 in expanded form.
3. Write in digits: five million, three hundred thousand, twenty.
4. Order from smallest to largest: 10,010; 1,100; 10,100; 1,010.
5. Round 38,451 to the nearest thousand, then to the nearest ten thousand.
6. Convert 110010₂ to decimal.
7. Convert 200 to binary.
8. Convert 2A₁₆ to decimal.
9. Convert 243₅ to decimal.
10. Convert 38 to base 5.
11. Convert 10101111₂ to hex, then to decimal.
12. Convert C3₁₆ to binary, then to decimal.
13. Convert 100 to hex.
14. What binary number comes right after 1111₂?
15. What hex number comes right after 9FF₁₆?
16. A 4-digit odometer reads 9998. What does it read after 3 more kilometres?
17. Convert 3E8₁₆ to decimal.
18. How many different numbers can you write with 3 decimal digits (including leading zeros)? With 8 binary digits?
19. Round 86,400 (the number of seconds in a day) to the nearest ten thousand.
20. What is the largest number you can write with 4 binary digits? With 2 hex digits? (Answer in decimal.)

<details>
<summary>Answers (Set 1)</summary>

1. 60,000 · 2. 7×1,000 + 0×100 + 9×10 + 3×1 · 3. 5,300,020 · 4. 1,010; 1,100; 10,010; 10,100 · 5. 38,000; 40,000 · 6. 50 · 7. 11001000₂ · 8. 42 · 9. 73 · 10. 123₅ · 11. AF₁₆; 175 · 12. 11000011₂; 195 · 13. 64₁₆ · 14. 10000₂ (sixteen) · 15. A00₁₆ · 16. 0001 (9999, then 0000 — overflow — then 0001) · 17. 1,000 · 18. 1,000 (000 to 999); 256 (00000000 to 11111111) · 19. 90,000 · 20. 15; 255
</details>

### Practice Set 2 — Think about it (5 problems)

1. In base 10, multiplying by 10 adds a 0 on the right (37 → 370). What happens in binary when you add a 0 on the right of 1011₂? What did that do to the number's value? Why?
2. A web colour is `#1E90FF`. Write the red, green, and blue values in decimal.
3. Without converting to decimal, which is bigger: 10011₂ or 1111₂? Why?
4. You want to give every person on Earth (about 8 billion) a different number in binary. About how many bits do you need? (Hint: 2¹⁰ is about a thousand. So 2²⁰ is about a million, 2³⁰ about a billion.)
5. Base 60 is still used for time. Write 2 hours, 5 minutes, 30 seconds as a number of seconds. What are the "place values" of hours, minutes, and seconds?

<details>
<summary>Answers (Set 2)</summary>

1. 1011₂ → 10110₂. 11 → 22: it doubled. Adding a 0 shifts every digit one place left, and each place is worth 2× the one to its right, so every digit's value doubles. (In base 10, it multiplies by 10 for the same reason.) Computers use this as a fast "multiply by 2" called a **left shift**.
2. 1E = 30, 90 = 144, FF = 255.
3. 10011₂: it has more digits (5 vs 4), and neither starts with 0. (It's 19; the other is 15.)
4. 2³⁰ ≈ 1 billion, so 2³³ ≈ 8 billion: about **33 bits**. (Exactly: 2³³ = 8,589,934,592, just enough.)
5. 2×3,600 + 5×60 + 30 = 7,200 + 300 + 30 = **7,530** seconds. Place values: seconds = 1, minutes = 60, hours = 3,600 (= 60×60).
</details>

---

## Watch, practise, and play

*Companions, not replacements: the lessons above come first. Use the [V protocol](../../study-protocols.md#v--watch-actively). Video course for this track: [math resources](resources.md#video-course).*

- **Watch:** Math Antics (YouTube): 'Place Value'. Crash Course Computer Science: the episode on representing numbers and letters with binary. Khan Academy: Arithmetic, place value.
- **Practise:** Khan Academy place-value and rounding exercises (auto-checked, so good for mixed review [I]).
- **Play** ([puzzles and games](puzzles-and-games.md)): binary mind-reading cards · count to 31 on one hand · hex speed round · make 100

---

## Self-check (end of section 3, cold)

1. Write 5,020,301 in words and in expanded form.
2. Round 649,999 to the nearest thousand.
3. Convert 1100100₂ to decimal.
4. Convert 77 to binary. Check your answer.
5. Convert BEEF₁₆ to decimal.
6. Convert 255 to hex.
7. Convert 1000₅ to decimal.
8. What is 01111111₂ + 1? Answer in binary and decimal.
9. How many bits are in two hex digits? What is that amount called?
10. Explain in two sentences why `0x10` equals 16.
11. **[R] Blank sheet:** write everything you know about place value and bases. Then check against this file.

<details>
<summary>Answers (self-check)</summary>

1. Five million, twenty thousand, three hundred one. 5×1,000,000 + 0×100,000 + 2×10,000 + 0×1,000 + 3×100 + 0×10 + 1×1
2. 650,000
3. 100
4. 1001101₂ (64 + 8 + 4 + 1 = 77 ✓)
5. 48,879 (11×4,096 + 14×256 + 14×16 + 15 = 45,056 + 3,584 + 224 + 15)
6. FF₁₆
7. 125
8. 10000000₂ = 128
9. 8 bits = one byte
10. In hex, the second place from the right is worth 16. `0x10` means one 16 and zero ones, which is 16.
</details>

## Done when

- [ ] Self-check ≥ 8/10 on items 1–10, and the blank sheet done.
- [ ] Binary/hex table and powers of 2 up to 1,024 on flashcards, and you can recite them.
- [ ] Four why-questions answered in writing.
- [ ] Feynman pass done (written and spoken).
- [ ] [Base Workshop](projects/base-workshop/spec.md) Milestones 1–2 done.

**Next:** [M02 — Addition and Subtraction](M02-addition-and-subtraction.md).
