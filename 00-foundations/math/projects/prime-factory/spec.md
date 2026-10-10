---
title: "Project: Prime Factory"
track: math
stages: "M03–M04, then after 01 Lab 01"
hours: 16
artifact: "A hand sieve to 200 and factor sheets; primes.py with tests; timing experiments; a toy 'lock' you try to break"
deliverable: "A one-page lab report: how hard is factoring as numbers grow?"
---

# Project: Prime Factory

| | |
| :-- | :-- |
| **When** | Milestones 1–2 during M03–M04 (paper). Milestones 3–5 after [01 Lab 01](../../../../01-intro-cs-taste/labs/lab-01-python-first-steps.md). |
| **Time** | About 16 hours |
| **You build** | A prime toolkit by hand and then in code; experiments that show why some algorithms are fast and others are slow; and a toy "lock" based on multiplying primes, which you then try to pick |
| **Deliverable** | A one-page lab report |

---

## Why this matters

You'll discover two things that sit at the heart of computer science:

1. **The same problem can be solved by algorithms of wildly different speed.** Testing whether a number is prime by trying every divisor up to n is slow; stopping at √n is dramatically faster; the sieve is faster still for many numbers at once. You'll measure the difference yourself.
2. **Some problems are easy one way and hard the other way.** Multiplying two primes takes a computer microseconds. Splitting the product back into its primes gets harder very quickly as the numbers grow. That one-way street is what keeps your bank connection private. In [Module 03](../../../../03-discrete-math/overview.md) you'll build a toy public-key cipher on top of this project, and break it.

**Real-world analogs:** prime generation in cryptographic libraries, factoring challenges, sieve-based algorithms in number theory software.

---

## Milestones

### Milestone 1 — The hand sieve (M03, week 4)

**Do:**
1. On graph paper, write the numbers 1 to 200 in rows of **6** (1–6, 7–12, …).
2. Run the Sieve of Eratosthenes (M04 Part 3) by hand. Use a different colour for the multiples of 2, 3, 5, 7, 11, and 13.
3. **Notice:** in rows of 6, the primes (after 2 and 3) all fall in just two columns. Which two? Write a sentence explaining why, using remainders mod 6 (you'll prove this in M04 Practice Set 2).
4. **Why did you stop at 13?** Write the reason (M04: √200 ≈ 14.1).

**Done when:** your list of primes under 200 is complete (there are **46**), and both "why" sentences are written.

### Milestone 2 — The factor sheets (M04)

**Do:**
1. **Factor trees** for 20 numbers of your choice between 100 and 2,000. At least 5 should have a repeated prime factor (like 2³). Write each factorisation with exponents. Check by multiplying back.
2. **Euclid by hand:** GCD of 10 pairs using the labelled steps from M04 Part 6. Include (1,071, 462), two pairs that are coprime (GCD 1), and two consecutive Fibonacci numbers (e.g. 89 and 55: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, …). Count the steps for each pair.
3. **LCMs** of 5 pairs, using GCD: lcm = a × b ÷ gcd.
4. **Gear puzzle:** cut two paper circles, mark 12 teeth on one and 18 on the other. Mark a starting tooth on each. "Turn" them (count teeth) and confirm the marks meet again at LCM(12, 18) = 36 teeth.

**Done when:** all checked; you've noticed something about the Fibonacci pairs' step counts (write it down — it's a real result, see stretch goals).

**Checkpoint:** [Milestone Checkpoint](<../../../../04 - System/Milestone Checkpoint Template.md>). Feynman target: explain why Euclid's algorithm works (M04's why-ladder), out loud, with one of your own examples.

### Milestone 3 — `primes.py` (after 01 Lab 01)

Write these functions:

```python
def is_prime_slow(n: int) -> bool:   # try every d from 2 to n - 1
def is_prime(n: int) -> bool:        # try d from 2 while d * d <= n
def sieve(limit: int) -> list[int]:  # all primes <= limit, Sieve of Eratosthenes
def factorize(n: int) -> list[int]:  # prime factors in order, with repeats: 360 -> [2, 2, 2, 3, 3, 5]
def gcd(a: int, b: int) -> int:      # Euclid's algorithm (a loop, not math.gcd)
def lcm(a: int, b: int) -> int:
```

**Rules:** handle the edge cases on purpose and document them: is 0 prime? 1? negative numbers? What should `factorize(1)` return? (Decide, write the decision in a comment, and test it [W].)

**Tests** (`test_primes.py`):
- `sieve(200)` has exactly 46 primes and matches your hand list.
- For every n from 2 to 10,000: `is_prime(n) == is_prime_slow(n)` (for n up to, say, 2,000 if the slow one is too slow — that slowness is a finding; note it).
- For every n from 2 to 10,000: the product of `factorize(n)` equals n, and every factor passes `is_prime`.
- `gcd` matches `math.gcd` on 1,000 random pairs; `gcd(a, 0) == a`.
- `lcm(a, b) * gcd(a, b) == a * b` on random pairs.

**Done when:** all tests pass.

### Milestone 4 — Speed experiments

Measure, don't guess. Use `time.perf_counter()` around each call.

1. **Three ways to find all primes below N.** For N = 1,000, 10,000, 100,000 (and 1,000,000 where it finishes within a minute): time (a) `is_prime_slow` on every number, (b) `is_prime` on every number, (c) `sieve(N)`.
   - Put the results in a table. Before measuring, write a **prediction with a reason** for each [lab report step 2].
   - For each method: when N grows 10×, how much does the time grow? (About 10×? 30×? 100×?)
2. **Euclid's step count:** count the loop steps of `gcd` for consecutive Fibonacci numbers up to the 40th. Plot (or tabulate) steps against the size of the numbers. What kind of growth is it?

**Done when:** both tables filled in, with predictions written before the measurements.

### Milestone 5 — The toy lock

This is a tiny model of how public-key cryptography protects data.

1. **Make a lock:** pick two primes p and q (use `sieve` or `is_prime` on random numbers). Compute **n = p × q**. Publish n; keep p and q secret.
2. **Pick it:** write `crack(n)` that finds p and q using your `factorize` (trial division).
3. **Race:** for primes of 3, 4, 5, 6, 7, and 8 digits each, make a lock and time how long `crack` takes. (Stop when a single crack takes over 5 minutes; note where.) Also time how long the multiplication p × q took.
4. **Estimate:** using the growth you see, estimate how long trial division would take for primes with 20 digits. With 300 digits (the size real systems use)? Use scientific notation (M07) and compare with the age of the universe (about 4 × 10¹⁷ seconds).

**Done when:** the race table and the estimates are done.

**Checkpoint:** Milestone Checkpoint. Why-ladder target: *why is multiplying easy but factoring hard?* Go three levels deep.

---

## Common pitfalls

- **`d * d <= n`, not `d < n ** 0.5`.** Floating-point square roots can be slightly off for large n (M06 Part 7). Integer multiplication is exact.
- **Forgetting the last factor:** after dividing out all small factors, if what's left is greater than 1, it's prime and must be included.
- **Sieve memory:** a list of a million booleans is fine; a hundred million may not be. Note where your machine struggles.
- **Timing too-fast code:** if a call takes microseconds, time 1,000 calls and divide.
- **Testing slow code at big sizes:** keep `is_prime_slow` tests small, or your test suite takes forever.

## Communication deliverable

**Lab report** (one page, [Lab Report Template](<../../../../04 - System/Lab Report Template.md>), sized for E06–E08): *"How does the time to find primes, and to crack a toy lock, grow as the numbers get bigger?"* Include your Milestone 4 table, your Milestone 5 race table, your predictions, and two sentences on why this matters for internet security.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Write the sieve and Euclid subgoals from memory before coding |
| **F** | Euclid's correctness, out loud |
| **W** | Edge-case decisions (is 1 prime?), "why rows of 6," "why factoring is hard" |
| **S** | Subgoal comments in every function |
| **I** | Factor sheets mix trees, GCDs, LCMs, and gears |
| **T** | The lab report |

## Stretch goals

- **Lamé's theorem:** you probably found that consecutive Fibonacci numbers make Euclid's algorithm take the most steps for their size. That's a known theorem (1844). Read about it and connect it to your plot.
- **Prime counting:** count primes below 10, 100, …, 10⁷. Compare with N ÷ ln N (after M11; `math.log` is ln). How close is it?
- **A faster cracker:** read about Pollard's rho method and implement it. How much further can you crack in 5 minutes?

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Hand work | Sieve to 200 correct, factor sheets checked, patterns explained | Mostly correct | Incomplete |
| Code and tests | All tests pass; edge cases decided and documented | Most tests | Failing |
| Experiments | Predictions before measurements; growth rates stated | Measured, no predictions | Missing |
| Toy lock | Race table and estimates in scientific notation | Partial | Missing |
| Lab report | Clear, with tables and a conclusion | Complete | Missing |

**Done when:** every area at least 2; Code and Experiments at 3.

## Connections

- **Back:** M03 (division, mod), M04 (everything).
- **Forward:** Module 03's [toy cipher project](../../../../03-discrete-math/projects/toy-cipher/spec.md) reuses `gcd`, `is_prime`, and `crack`; Module 05 (algorithm speed, hashing with primes); M11 (growth rates explain your Milestone 4 tables).
