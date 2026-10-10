---
title: "Math Puzzles and Games"
track: math
tags: [math, puzzles, games, fun]
---

# Math Puzzles and Games

**Number games, tricks, puzzles, and challenges for each math stage — fun, but always with a reason.** Every trick has a "why does it work?" question [W]; answering it uses exactly the stage's idea. Use them as:
- **Warm-ups** (5 minutes before the morning lesson),
- **Fun Friday** (replace one practice set a week with two games from your stage — the [I] mixing still counts),
- **Social math** (most of these are better with a friend, a partner, or a kid),
- **Rewards** after a hard week.

Answers and explanations are in collapsible blocks. Try first.

---

## Daily-ish games (any stage)

### The 24 game
Draw four cards (A = 1, J/Q/K = 11/12/13, or just remove picture cards). Use each card's number exactly once with + − × ÷ and brackets to make **24**. Example: 4, 7, 8, 8 → (7 − 8 ÷ 8) × 4 = 24. Some sets are impossible. Hard one: **3, 3, 8, 8**.

<details><summary>Answer for 3, 3, 8, 8</summary>

8 ÷ (3 − 8 ÷ 3) = 8 ÷ (1/3) = 24. It needs fractions (M05)!
</details>

### Countdown numbers
Pick six numbers (from 1–10 plus some of 25, 50, 75, 100) and a random target from 101 to 999 (`shuf -i 101-999 -n 1`). In 3 minutes, get as close as you can using + − × ÷ with each number at most once. It's great for order of operations (M07) and mental math (M02–M03).

### Estimation first
Before *every* calculation this week, write a rough estimate. Score a point when your exact answer is within 10% of the estimate. Track your score. (This habit catches more errors than anything else.)

### Fermi questions (from M06 on)
Estimate with rough numbers and reasoning, not research. Then check online.
- How many piano tuners are in your city?
- How many litres of water do you drink in a year?
- How many keystrokes will you type during this whole curriculum?
- How many hairs are on your head?
- How many bytes are in all the photos on your phone? (Check your storage settings afterwards.)

The goal is the right **order of magnitude** (M07), not the exact number. Write your chain of estimates; [W] which step had the biggest uncertainty?

---

## M01–M02: Place value, bases, adding

### The binary mind-reading cards
Make six cards. Card 1 lists every number from 1 to 63 whose binary form has a 1 in the **ones** place (1, 3, 5, 7, …). Card 2: a 1 in the **twos** place (2, 3, 6, 7, 10, 11, …). Cards 3–6: the 4s, 8s, 16s, and 32s places. A friend picks a secret number from 1 to 63 and tells you which cards it's on. You add the **first number on each of those cards** and announce their number.

Make the cards with a short Python loop (after Lab 01) or by hand.

<details><summary>Why does it work? [W]</summary>

Each card's first number is a place value (1, 2, 4, 8, 16, 32). Being on a card means that bit is 1. Adding the place values of the 1-bits is converting binary to decimal (M01).
</details>

### Count to 31 on one hand
Each finger is a bit: thumb = 1, index = 2, middle = 4, ring = 8, little = 16. Count from 0 to 31 out loud. Then count to 1,023 using both hands. (You'll know binary in your fingers forever.)

### Hex speed round
A friend (or `python3 -c "import random; print(random.randint(0,255))"`) gives a number; say it in hex within 5 seconds. Then the reverse. Track your time per answer.

### Make 100
Using the digits 1–9 **in order**, with + and − between some of them, make 100. (For example, 123 − 45 − 67 + 89 = 100.) Find three different ways.

### Odometer bets (M02)
On a car trip or a bus ride, predict how many kilometres until the odometer shows a "palindrome" (like 12321). Then check.

---

## M03–M04: Multiply, divide, primes

### The missing digit trick
A friend writes any number with 4+ digits, scrambles its digits into a new number, and subtracts the smaller from the larger. They circle one non-zero digit of the answer and tell you the **other** digits. You name the circled digit.

<details><summary>How and why [W]</summary>

Add the digits they tell you. The missing digit is whatever brings the total up to the next multiple of 9 (if the total is already a multiple of 9, the missing digit is 9). Why: a number and its scrambled version have the same digit sum, so they have the same remainder mod 9 (M04's digit-sum test). Their difference is therefore a multiple of 9, so its digits add up to a multiple of 9.
</details>

### 1089
Take a three-digit number whose first and last digits differ by at least 2 (e.g. 732). Reverse it (237). Subtract the smaller from the larger (495). Reverse that (594) and add (495 + 594). The answer is always **1089**. [W] Why? (Hint: write the number as 100a + 10b + c and do the algebra once you reach M08. For now, test ten numbers.)

### Kaprekar's mystery (6174)
Take a four-digit number with at least two different digits. Arrange its digits in descending order and in ascending order; subtract. Repeat with the result. You'll reach **6174** in at most 7 steps, and then it repeats forever. Try five starting numbers. (After Lab 01, write a program that checks all 4-digit numbers and finds the one that takes the most steps.)

### Prime race
Two players take turns naming primes in order (2, 3, 5, 7, 11, …). The first to say a composite number or freeze for 5 seconds loses. How far can you get alone? (The primes below 100 are flashcard material for M04.)

### Factor-pair rectangles
Draw every rectangle you can with 24 unit squares. Then 36, then 37. [W] Why does 37 give only one? What kind of number gives an odd number of rectangles? (Squares! M04 Practice Set 1, #18.)

### Times-table bingo
Make a 5 × 5 bingo card of products (like 42, 56, 63). Call out random facts ("7 × 8") and mark the products. Fast and very effective for the M03 "hard core" facts.

---

## M05–M06: Fractions, decimals, percents

### Fraction war (card game)
Each player draws two cards and makes a fraction (the smaller card on top). The bigger fraction wins both pairs. Say *why* it's bigger out loud (common denominator, benchmark ½, or cross-multiplying — M05 Part 3).

### Unit-fraction puzzles
Write 1 as a sum of **different** unit fractions (fractions with 1 on top): 1 = 1/2 + 1/3 + 1/6. Find another way with four fractions. (Ancient Egyptian scribes wrote all fractions this way.)

### Percent shopping game
From a real shop's sale page, compute the real price of five items with different discounts — in your head, using the 10% / 5% / 1% trick (M06). Then check. Bonus: find a "buy 3 for the price of 2" deal and convert it into a percent discount.

### Recipe remix
Halve, triple, or scale a real recipe to feed 7 (Ratio Workshop Milestone 1) and **cook it**. Edible maths.

### The 0.1 + 0.2 bet (M06, after Lab 01)
Bet a friend that a computer can't add 0.1 and 0.2. Open Python and show them. Then explain why (M06 Part 7).

---

## M07: Negatives and powers

### Rice on the chessboard
One grain on the first square, doubling each square. Estimate on paper (powers of 2, the 2¹⁰ ≈ 10³ bridge) how many grains on square 64. Then compute it exactly in Python.

### Paper folding to the Moon
A sheet of paper is about 0.1 mm thick. How many folds until it's taller than you? Taller than a mountain? Reaches the Moon (384,000 km)? Estimate with powers of 2, then calculate.

### Temperature swings
Look up today's highs and lows for five cities on different continents. Compute every difference (including negative numbers). Which pair has the biggest swing?

### Two's complement odometer game (after M07 Part 7)
Write 4-bit numbers on cards (0000–1111). Shuffle. Draw two and add them on paper in 4 bits. Say the signed answer. Did it overflow?

---

## M08–M09: Algebra and graphs

### Think of a number
"Think of a number. Double it. Add 10. Halve it. Subtract the number you first thought of. Your answer is 5." Write it as algebra (n → 2n → 2n + 10 → n + 5 → 5) [W]. Then **invent your own trick** with a different answer, and try it on someone.

### Balance puzzles
Draw two-pan scales with shapes (2 squares + 1 circle = 3 circles + 4 kg…) and solve for each shape's weight. Then write each puzzle as an equation (M08's balance idea).

### Desmos challenges (desmos.com)
- **Desmos art:** draw a face, a house, or your initials using at least 15 equations, with domain restrictions like `{0 < x < 3}`. Label what each equation does.
- **Desmos classroom activities** (search "Desmos Marbleslides lines" and "Desmos Polygraph lines"): free, game-like activities about slopes and intercepts.

### Who catches whom?
Write five "race" puzzles from real life (your walking speed vs a bus with a head start). Solve each with a system of equations, and also by graphing in Desmos (M09).

---

## M10: Geometry

### Measure π with a can
Wrap a string around three round objects, measure, and divide by each one's diameter. Average your results. How close to 3.14159 did you get? What were your error sources (M06)?

### Pythagoras in the room
Check whether the corners of your room, your table, and your phone are true right angles, using the 3-4-5 rule (M10 Part 5).

### Shadow height
Measure your shadow and your height, then a tree's shadow, at the same time of day. Compute the tree's height with similar triangles.

### Turtle art contest
Using Python's `turtle` (after Lab 01), draw the most beautiful pattern you can with a single loop of `forward` and `left`. Then explain the angle you chose (360 ÷ n, or a star's angle).

### Tangrams
Make a set of seven tangram pieces from card (instructions are easy to find). Make ten shapes. [W] Why do all the shapes have the same area?

---

## M11: Growth, logs, sums

### Guess my number
Play "guess my number from 1 to 1,000" with someone (higher/lower). With the best strategy, how many guesses do you ever need? (10, because 2¹⁰ = 1,024. That's log₂.)

### Tower of Hanoi
Use coins of different sizes. Move the stack from one place to another, one coin at a time, never putting a bigger coin on a smaller one. Count the moves for 3, 4, and 5 coins. Find the pattern (2ⁿ − 1 — M11's binary sum!) and explain it recursively (Module 02 Lab 01).

### Pascal's triangle art
Write Pascal's triangle to 16 rows. Shade every **odd** number. What picture appears? (Search "Sierpinski triangle" afterwards.) Then, after Lab 01, print 64 rows in Python with `#` for odd numbers.

### Decibel detective
Use a free sound-meter app on your phone. Measure five places (quiet room, street, kitchen with a blender…). How many times more sound **power** is the loudest than the quietest? (Every 10 dB is ×10.)

### Doubling-time race
Compound interest at 7% a year: how many years to double your money? Try the "rule of 72" (72 ÷ 7 ≈ 10.3 years) and check it with logarithms. Why does the rule of 72 work? [W]

---

## Online puzzle platforms

| Platform | Use from | Why it's fun |
| :-- | :-- | :-- |
| **Alcumus** (artofproblemsolving.com/alcumus) | M04 | Adaptive problems with full solutions; topics from prealgebra up |
| **Khan Academy "Mastery challenges"** | M01 | Short mixed quizzes that level up your skills |
| **Project Euler** (projecteuler.net) | after Lab 01 + M04 | Math puzzles you solve with code. Problems 1, 2, 3, 5, 6, 7 fit the foundations perfectly. Don't share solutions online (the site asks this) |
| **Brilliant** (brilliant.org) | any | 💲 Interactive courses (math, logic, CS). Optional; the free tier has daily problems |
| **NRICH** (nrich.maths.org) | any | Free rich puzzles from the University of Cambridge, sorted by level |
| **Desmos** (desmos.com) | M08 | Graphing art and game-like classroom activities |

---

## Math in the wild (a weekly challenge)

Once a week, find one real thing that uses this stage's math. Photograph it and write three sentences: what it is, what math it uses, and one calculation with it. Examples: a "30% off" sign (M06), a ratio on a bag of fertiliser (M05), a slope sign on a hill (M09), a phone screen's resolution (M06/M10), a population growth headline (M11). Keep them in `~/workbench/math/in-the-wild/`. By the end of the track, you'll have 40 examples of math you *use*.
