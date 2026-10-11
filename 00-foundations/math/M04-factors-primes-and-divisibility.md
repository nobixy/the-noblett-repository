---
title: "M04 — Factors, Primes, and Divisibility"
id: "M04"
type: "lesson"
module: "00-foundations"
track: "math"
stage: "M04"
phase: "A"
order: 170
prerequisites: [M03]
---

# M04 — Factors, Primes, and Divisibility

**In this stage you will:** find factors and multiples, use quick divisibility tests (and know why they work), understand prime numbers as the "atoms" of all whole numbers, factor any number into primes, prove there are infinitely many primes (your first real proof), and find greatest common divisors and least common multiples, including with Euclid's 2,300-year-old algorithm.

**Before you start:** M03 done. Times-table facts are fast. You know what `mod` means.

---

## Diagnostic (cold, no calculator)

1. List all the factors of 36.
2. Is 91 prime?
3. Write 360 as a product of primes.
4. Find the greatest common divisor of 48 and 180.
5. Find the least common multiple of 6 and 8.
6. Is 7,452 divisible by 3? By 9?
7. Is 1,000,001 divisible by 2?
8. List all primes less than 30.
9. Use any method to find the greatest common divisor of 1,071 and 462.
10. Two lights blink together now. One blinks every 12 seconds, the other every 18. When do they next blink together?

<details>
<summary>Answers (diagnostic)</summary>

1. 1, 2, 3, 4, 6, 9, 12, 18, 36 · 2. No: 91 = 7 × 13 · 3. 2 × 2 × 2 × 3 × 3 × 5 = 2³ × 3² × 5 · 4. 12 · 5. 24 · 6. Yes and yes (digits add to 18) · 7. No (it ends in 1, an odd digit) · 8. 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 · 9. 21 · 10. In 36 seconds
</details>

---

## Why this matters

Primes are the building blocks of whole numbers, the way chemical elements are the building blocks of matter. Every whole number bigger than 1 is built from primes in exactly one way.

This idea runs deep in computing:
- **Cryptography.** Multiplying two big primes is easy; splitting the product back into its primes is (as far as anyone knows) extremely hard. That one-way street protects nearly every secure connection on the internet. You'll build a toy version — and break it — in [Module 03](../../03-discrete-math/overview.md).
- **The greatest common divisor** simplifies fractions (M05), and Euclid's algorithm for it is one of the oldest algorithms still in daily use. It's the first algorithm in this curriculum whose *correctness* you'll prove.
- **Hash tables** often use prime sizes so that items spread evenly (Module 05).
- **Gears and schedules** line up at least common multiples, which matters in clocks, motors, and anything with cycles.

---

## Part 1 — Factors and multiples

If a × b = n (all whole numbers), then **a and b are factors of n**, and **n is a multiple of a and of b**.
> 3 × 4 = 12: 3 and 4 are factors of 12; 12 is a multiple of 3 and of 4.

"a is a factor of n" is the same as "n mod a = 0" and "a **divides** n" (written a | n).

**Picture:** the factors of n are exactly the side lengths of rectangles with area n. The rectangles with area 12 are 1×12, 2×6, and 3×4, so the factors of 12 are 1, 2, 3, 4, 6, 12.

### Finding all factors

**Subgoal labels [S]:**
1. **Start at 1** and test each number in order: does it divide n?
2. **Each time one does, write it and its partner** (n ÷ it) as a pair.
3. **Stop when the numbers meet or cross.** (That happens at the square root of n.)
4. **List** all the numbers from the pairs.

*Worked example:* **factors of 36**
- 1 × 36 · 2 × 18 · 3 × 12 · 4 × 9 · (5 doesn't divide) · 6 × 6 ← the numbers met. Stop.
- **1, 2, 3, 4, 6, 9, 12, 18, 36.**

> **[W] Why can you stop at the square root?** Factors come in pairs (a × b = n). If both were bigger than the square root, their product would be bigger than n. So in every pair, one of them is at most the square root. Once you've tested up to it, you've found every pair. (This is also why the computer programs in [Prime Factory](projects/prime-factory/spec.md) only need to check up to √n. It turns a slow program into a fast one.)

---

## Part 2 — Divisibility tests

Quick ways to tell if a number divides another without dividing.

| Divides by | Test | Example | Why it works |
| :-- | :-- | :-- | :-- |
| **2** | last digit is even (0, 2, 4, 6, 8) | 1,234 ✓ | 10 is a multiple of 2, so every place except the ones is a multiple of 2. Only the ones digit matters. |
| **5** | last digit 0 or 5 | 7,365 ✓ | Same reason: 10 is a multiple of 5. |
| **10** | last digit 0 | 4,560 ✓ | |
| **4** | last two digits form a multiple of 4 | 3,716 (16) ✓ | 100 is a multiple of 4, so only the last two digits matter. |
| **8** | last three digits form a multiple of 8 | 5,128 (128) ✓ | 1,000 is a multiple of 8. |
| **3** | digits add up to a multiple of 3 | 7,452: 7+4+5+2 = 18 ✓ | see below |
| **9** | digits add up to a multiple of 9 | 7,452: 18 ✓ | see below |
| **6** | passes both the 2 test and the 3 test | 2,358 ✓ | 6 = 2 × 3, and 2 and 3 share no factors. |

> **[W] Why does the digit-sum test work for 9 (and 3)?**
> 1. Each place value is one more than a multiple of 9: 10 = 9 + 1, 100 = 99 + 1, 1,000 = 999 + 1.
> 2. So 7,452 = 7×1,000 + 4×100 + 5×10 + 2 = 7×(999 + 1) + 4×(99 + 1) + 5×(9 + 1) + 2 = (a multiple of 9) + (7 + 4 + 5 + 2).
> 3. So 7,452 and its digit sum (18) have the **same remainder mod 9**. If the digit sum divides by 9, so does the number. Since 9 is a multiple of 3, the same argument works for 3.
>
> This is your first taste of **modular arithmetic**, the main subject of Module 03. Reread this box when you get there.

---

## Part 3 — Prime numbers

A **prime** is a whole number greater than 1 whose only factors are 1 and itself.
- **Primes:** 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, …
- A number greater than 1 that isn't prime is **composite**: 4, 6, 8, 9, 10, 12, …
- **1 is neither.** (Why? See the why-ladder in Part 4.)
- **2 is the only even prime.** Every other even number has 2 as a factor.

There are **25 primes below 100**. Learn the ones below 50 by heart (15 of them).

### Is it prime? (testing one number)

**Subgoal labels [S]:**
1. **Find the square root** roughly (√91 is a bit more than 9, since 9 × 9 = 81 and 10 × 10 = 100).
2. **Test each prime up to that root:** 2, 3, 5, 7.
3. **If none divides it, it's prime.** If one does, it's composite.

*Worked example:* **Is 91 prime?** √91 ≈ 9.5. Test 2 (no, odd), 3 (9 + 1 = 10, no), 5 (no), 7: 91 ÷ 7 = 13 ✓. **Composite: 7 × 13.**

(Why only *primes* up to the root, not every number? Because if 4 divided it, 2 would too, and you already tested 2.)

### The Sieve of Eratosthenes (finding all primes up to N)

An ancient Greek method, still the basis of fast prime-finding programs.

**Subgoal labels [S]:**
1. **Write all numbers from 2 to N** in a grid.
2. **Circle the first number not crossed out** (it's prime).
3. **Cross out all its multiples**, starting from its square (smaller multiples are already crossed out).
4. **Repeat** from step 2 until the next circled number's square is bigger than N.
5. **Everything not crossed out is prime.**

You'll do this by hand on a 1–200 grid in [Prime Factory](projects/prime-factory/spec.md) Milestone 1, then program it.

---

## Part 4 — Prime factorisation

Every whole number greater than 1 can be written as a product of primes. This is its **prime factorisation**.

### Factor tree

**Subgoal labels [S]:**
1. **Split** the number into any two factors (use a divisibility test to find one).
2. **Keep splitting** each composite branch.
3. **Stop** at primes (circle them).
4. **Collect** the circled primes, smallest first, and use exponents for repeats.

*Worked example:* **360**

```
          360
         /   \
       10     36
      /  \   /  \
     2    5  6    6
            / \  / \
           2  3 2   3
```

Primes: 2, 5, 2, 3, 2, 3 → sorted: 2 × 2 × 2 × 3 × 3 × 5 = **2³ × 3² × 5**.

(The small raised number is an **exponent**: 2³ means 2 × 2 × 2. You'll study these properly in M07.)

### Ladder division (often faster)

Divide by the smallest prime that works, over and over:

```
2 | 360
2 | 180
2 |  90
3 |  45
3 |  15
5 |   5
  |   1
```

Same answer: 2³ × 3² × 5.

### The Fundamental Theorem of Arithmetic

> **Every whole number greater than 1 has exactly one prime factorisation** (apart from the order of the factors).

No matter how you split 360 in the factor tree — 10 × 36, or 2 × 180, or 8 × 45 — you always end up with three 2s, two 3s, and one 5. This is why primes are like atoms: each number has a unique "chemical formula."

> **[W] Why isn't 1 a prime?**
> 1. If 1 were prime, then 6 = 2 × 3 = 1 × 2 × 3 = 1 × 1 × 2 × 3 = …
> 2. Factorisations would no longer be unique: you could add as many 1s as you like.
> 3. The theorem above is far too useful to lose, so mathematicians define primes to exclude 1. **Definitions are choices, made to keep the important theorems true and simple.** That's a deep idea about how math (and good software design) works.

---

## Part 5 — There are infinitely many primes (a proof)

Primes get rarer as numbers grow. Do they ever stop? Euclid answered this around 300 BC, with an argument you can follow completely. It's your first proof in this curriculum; read it slowly.

**Claim:** there is no largest prime.

**Proof:**
1. Suppose, for the sake of argument, that there *is* a complete, finite list of all the primes: p₁, p₂, …, pₖ.
2. Multiply them all together and add 1. Call the result **Q**: Q = (p₁ × p₂ × … × pₖ) + 1.
3. Divide Q by any prime on the list. It leaves a **remainder of 1** (because Q is one more than a multiple of that prime). So **no prime on the list divides Q**.
4. But Q is bigger than 1, so it has a prime factorisation (Part 4). Its prime factors must be primes that are **not on the list**.
5. So the list was not complete after all. This works for *any* finite list, so no finite list can contain all the primes. **There are infinitely many.** ∎

*Example of step 3:* if the "list" were 2, 3, 5, then Q = 30 + 1 = 31, which leaves remainder 1 when divided by 2, 3, or 5. (31 happens to be a new prime itself. Q isn't always prime: with 2, 3, 5, 7, 11, 13, Q = 30,031 = 59 × 509 — but 59 and 509 are new primes, not on the list.)

**[F] Feynman target for this stage:** explain this proof to a friend, out loud, without notes. If you can do it, you understand the key moves of proof by contradiction, which you'll use all through Module 03.

---

## Part 6 — Greatest common divisor (GCD)

The **GCD** of two numbers is the biggest number that divides both. GCD(48, 180) = 12.

**Uses:** simplifying fractions (48/180 = 4/15 by dividing both by 12); cutting things into the largest equal pieces; checking whether two numbers share any factor (GCD = 1 means they're **coprime**, which matters in cryptography).

### Method 1 — Prime factorisations

1. Factorise both: 48 = 2⁴ × 3; 180 = 2² × 3² × 5.
2. Take each prime they **share**, with the **smaller** exponent: 2² and 3¹.
3. Multiply: 4 × 3 = **12**.

### Method 2 — Euclid's algorithm (best for big numbers)

**Subgoal labels [S]:**
1. **Divide the bigger number by the smaller** and find the remainder.
2. **Replace** the pair with (smaller number, remainder).
3. **Repeat** until the remainder is 0.
4. **The last non-zero remainder is the GCD.** (Equivalently, the divisor at the step where you got 0.)

*Worked example:* **GCD(1,071, 462)**

| Step | Divide | Remainder |
| :-- | :-- | :-- |
| 1 | 1,071 ÷ 462 = 2, since 2 × 462 = 924 | 1,071 − 924 = **147** |
| 2 | 462 ÷ 147 = 3, since 3 × 147 = 441 | 462 − 441 = **21** |
| 3 | 147 ÷ 21 = 7 exactly | **0** |

**GCD = 21.** Check: 1,071 = 21 × 51 and 462 = 21 × 22 ✓

> **[W] Why does Euclid's algorithm work?**
> 1. Any number that divides both a and b also divides a − b. (If a = 21 × 51 and b = 21 × 22, then a − b = 21 × 29.)
> 2. Subtracting b as many times as possible leaves a mod b. So any common divisor of a and b also divides a mod b. And the other way round: anything dividing b and a mod b also divides a (since a = some multiple of b + a mod b).
> 3. So the pairs (a, b) and (b, a mod b) have **exactly the same common divisors**, and so the same GCD. Each step keeps the GCD the same while making the numbers smaller. When the remainder hits 0, the pair is (g, 0), and GCD(g, 0) = g.
>
> This is a complete argument that the algorithm is correct. In Module 03 you'll write it as a formal proof.

---

## Part 7 — Least common multiple (LCM)

The **LCM** of two numbers is the smallest number that is a multiple of both. LCM(6, 8) = 24.

**Uses:** common denominators for adding fractions (M05); when cycles line up again (gears, schedules, blinking lights).

**Method 1 — list multiples:** 6, 12, 18, **24**, … and 8, 16, **24** → 24. Fine for small numbers.

**Method 2 — prime factorisations:** take every prime that appears in either, with the **larger** exponent.
> 6 = 2 × 3; 8 = 2³ → 2³ × 3 = **24**.

**Method 3 — from the GCD:** LCM(a, b) = a × b ÷ GCD(a, b).
> LCM(12, 18) = 216 ÷ 6 = **36**.

*Worked example (cycles):* two lights blink together now; one every 12 seconds, one every 18. They next blink together at LCM(12, 18) = **36 seconds**.

---

## Practice routine (3 sections)

| Section | Focus |
| :-- | :-- |
| 1 | Session 1: factors and the √n stop · Session 2: divisibility tests (and why) · Session 3: primes and testing · Session 4: sieve 1–100 by hand · Session 5: Practice Set 1, items 1–9 |
| 2 | Sessions 1–2: factor trees and ladders · Session 3: the infinitely-many-primes proof (read, then rewrite from memory [R]) · Session 4: GCD both methods · Session 5: Prime Factory Milestone 2 |
| 3 | Session 1: LCM · Session 2: applications · Session 3: Practice Set 1 rest + Set 2 · Session 4: Feynman (the proof, out loud) · Session 5: self-check |

**Warm-up [R] (every session):** Euclid's algorithm subgoal labels from memory, then one GCD.
**Flashcards:** primes below 50; divisibility tests with their reasons.

**Key why-questions [W]:**
1. Why can you stop testing factors at √n?
2. Why does the digit-sum test work for 9?
3. Why isn't 1 prime?
4. Why does Euclid's algorithm give the GCD?

---

## Practice sets

### Practice Set 1 — Mixed (20 problems, no calculator)

1. List all factors of 48.
2. List all factors of 97.
3. Is 2,358 divisible by 3? by 9? by 4? by 6?
4. Is 51 prime?
5. Is 101 prime?
6. Prime factorisation of 84.
7. Prime factorisation of 1,001.
8. Prime factorisation of 256.
9. Prime factorisation of 990.
10. GCD(24, 36)
11. GCD(35, 64)
12. GCD(252, 198) by Euclid's algorithm (show each step).
13. LCM(4, 6)
14. LCM(12, 15)
15. LCM(9, 10)
16. A 12-tooth gear drives an 18-tooth gear. Mark a tooth on each where they touch. After how many turns of each gear do the marks meet again?
17. You want to cut a 48 cm × 30 cm board into identical squares, as large as possible, with no waste. How big is each square, and how many squares are there?
18. Find a number with exactly 3 factors. What kind of number has exactly 3 factors?
19. How many primes are there between 1 and 50?
20. Bus A leaves every 15 minutes, bus B every 20 minutes. Both leave at 9:00. When do they next leave together?

<details>
<summary>Answers (Set 1)</summary>

1. 1, 2, 3, 4, 6, 8, 12, 16, 24, 48 · 2. 1, 97 (prime) · 3. Yes (digit sum 18); yes; no (58 isn't a multiple of 4); yes (even and divisible by 3) · 4. No: 3 × 17 · 5. Yes (not divisible by 2, 3, 5, or 7; √101 ≈ 10) · 6. 2² × 3 × 7 · 7. 7 × 11 × 13 · 8. 2⁸ · 9. 2 × 3² × 5 × 11 · 10. 12 · 11. 1 (coprime) · 12. 252 mod 198 = 54; 198 mod 54 = 36; 54 mod 36 = 18; 36 mod 18 = 0 → **18** · 13. 12 · 14. 60 · 15. 90 · 16. LCM(12, 18) = 36 teeth: the small gear turns 3 times, the big gear 2 times · 17. GCD(48, 30) = 6 cm squares; 8 × 5 = 40 squares · 18. 4 (factors 1, 2, 4); squares of primes (4, 9, 25, 49, …) have exactly 3 factors · 19. 15 · 20. LCM(15, 20) = 60 minutes → 10:00
</details>

### Practice Set 2 — Think about it (4 problems)

1. Explain why every prime greater than 3 is either one more or one less than a multiple of 6. (Hint: what are the possible remainders mod 6, and which ones can't be prime?)
2. A friend says "2 × 3 × 5 × 7 × 11 × 13 + 1 = 30,031 is prime, because Euclid's proof says so." Are they right? What *does* the proof say about 30,031?
3. Why is GCD(a, b) × LCM(a, b) = a × b? Try it with 12 and 18, then explain using prime factorisations (smaller exponent + larger exponent = both exponents).
4. Why might a hash table with 100 buckets spread the keys 0, 10, 20, 30, … badly, while one with 101 buckets spreads them well? (Use mod.)

<details>
<summary>Answers (Set 2)</summary>

1. Every number is 6k, 6k+1, 6k+2, 6k+3, 6k+4, or 6k+5. 6k, 6k+2, 6k+4 are even; 6k+3 is divisible by 3. So a prime bigger than 3 must be 6k+1 or 6k+5 (= 6(k+1) − 1).
2. Wrong: 30,031 = 59 × 509. The proof only says Q has prime factors that aren't on the list (59 and 509 aren't). It doesn't say Q is prime.
3. 12 = 2² × 3, 18 = 2 × 3². GCD takes 2¹ × 3¹ (smaller exponents), LCM takes 2² × 3² (larger). Together they use every exponent from both numbers exactly once: 2³ × 3³ = 216 = 12 × 18. ✓
4. With 100 buckets, keys that are multiples of 10 land only in buckets 0, 10, 20, …, 90 (key mod 100): just 10 of the 100 buckets get used. With 101 buckets, since 101 is prime and shares no factor with 10, the keys 0, 10, 20, … spread over all the buckets.
</details>

---

## Watch, practise, and play

*Companions, not replacements: the lessons above come first. Use the [V protocol](../../study-protocols.md#v--watch-actively). Video course for this track: [math resources](resources.md#video-course).*

- **Watch:** Khan Academy: Pre-algebra, factors and multiples. Numberphile: prime-number videos. Eddie Woo (YouTube): classroom explanations.
- **Practise:** Alcumus (artofproblemsolving.com, free): prealgebra number theory.
- **Play** ([puzzles and games](puzzles-and-games.md)): prime race · factor-pair rectangles · Kaprekar's 6174

---

## Self-check (cold, no calculator)

1. List all factors of 60.
2. Prime factorisation of 1,260.
3. Is 221 prime?
4. Is 7,365 divisible by 3? by 5? by 9?
5. GCD(1,071, 462) by Euclid's algorithm, from memory.
6. LCM(14, 21)
7. In two sentences, explain why 1 is not prime.
8. In three sentences, explain why the digit-sum test for 9 works.
9. **[R] Blank sheet:** write Euclid's proof that there are infinitely many primes, from memory. Then compare with Part 5.

<details>
<summary>Answers (self-check)</summary>

1. 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60 · 2. 2² × 3² × 5 × 7 · 3. No: 13 × 17 · 4. Yes (digit sum 21); yes (ends in 5); no (21 isn't a multiple of 9) · 5. 21 · 6. 42
</details>

## Done when

- [ ] Self-check ≥ 5/6 on items 1–6; items 7–9 written and checked.
- [ ] You can explain the infinitely-many-primes proof out loud without notes.
- [ ] Four why-questions answered in writing.
- [ ] [Prime Factory](projects/prime-factory/spec.md) Milestones 1–2 done (Milestones 3–4 can wait for Python).

**Next:** [M05 — Fractions](M05-fractions.md).
