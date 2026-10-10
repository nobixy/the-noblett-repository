---
title: "Project: Counting Verifier"
module: "03-discrete-math"
hours: 12
artifact: "count: a tool that checks counting formulas and probabilities three ways — brute-force enumeration, exact formula, and Monte Carlo simulation — plus a hash-collision experiment"
deliverable: "Lab report: the birthday paradox, predicted and measured + 3 bijective proofs in the Proof Journal"
---

# Project: Counting Verifier

| | |
| :-- | :-- |
| **Module** | 03 Discrete Math |
| **Time** | About 12 hours |
| **Prerequisites** | Units 4, 6, 8; M05 (fractions); Lab 01 of Module 02 (permutations by recursion) |
| **You build** | `count`, a test bench for counting and probability. Every formula you learn gets checked against a brute-force count of the actual objects, and every probability against both an exact fraction and a simulation. Then a real experiment: how soon do hash values collide? |
| **Deliverable** | A lab report and three proofs |

---

## Why this matters

Counting is where intuition fails most often. "How many ways…?" questions have answers that are easy to get *almost* right — off by a factor of 2 because order didn't matter, or by one case you counted twice. Professionals check counting arguments by **computing small cases by brute force**. That habit catches more errors than any amount of staring.

Probability is worse: the birthday paradox, Monty Hall, and conditional probability fool nearly everyone. Simulating them makes the truth undeniable — and then a proof makes it understood.

And counting is everywhere in computing: how many passwords, how many states, how many comparisons an algorithm makes (Module 05), and how soon a hash table starts colliding (also Module 05).

**Real-world analogs:** combinatorial test design, password-strength estimates, hash-collision analysis, simulation-based checks of probability models.

---

## Milestones

### Milestone 1 — The three-way checker

Build a small framework where each **claim** has three parts:

```python
Claim(
    name="choose 3 of n",
    formula=lambda n: comb(n, 3),                  # your formula (write your own comb!)
    enumerate=lambda n: combinations(range(n), 3), # the actual objects (itertools allowed here)
    sizes=range(0, 12),
)
```

`count check` runs every claim for every size and reports mismatches. Write your **own** `factorial`, `perm(n, k)`, and `comb(n, k)` (don't use `math.comb` except as a test witness).

**Claims to include (at least 12):** n!; P(n, k); C(n, k); subsets of an n-set (2ⁿ); strings of length k over an alphabet of size a (aᵏ); binary strings of length n with exactly k ones (C(n, k) — why the same?); passwords of length 8 using lowercase letters and digits with **at least one digit** (total minus all-letters); multisets / **stars and bars** (ways to put k identical balls into n boxes: C(n + k − 1, k)); lattice paths (Module 02's `paths(r, c)` = C(r + c, r)); handshakes (C(n, 2)); anagrams of `MISSISSIPPI`-style words (multinomial); one claim that is **deliberately wrong** to prove the checker catches it.

**Done when:** all claims pass except the planted wrong one, which is reported clearly.

**[W]:** for every claim, write the one-sentence reason the formula is right (the "why" behind the count) next to it in code comments.

### Milestone 2 — Bijections: counting by matching

A **bijection** (Unit 4) is a perfect one-to-one matching between two sets. If you can match every object of one kind with exactly one of another, the two counts are equal — no formula needed.

For each identity: (a) check it with the three-way checker; (b) write the bijection as **code** that converts one kind of object into the other, and test that it's one-to-one and onto for small n; (c) write the proof in your [Proof Journal](../proof-journal/spec.md).

1. C(n, k) = C(n, n − k). (*Matching:* choosing k items to take = choosing n − k items to leave.)
2. Subsets of {1, …, n} ↔ binary strings of length n. (M01: a subset *is* a binary number!)
3. Pascal's identity: C(n, k) = C(n − 1, k − 1) + C(n − 1, k). (*Split by whether item n is chosen.*)

**Done when:** three bijections coded and tested, three proofs written.

### Milestone 3 — Inclusion–exclusion and derangements

A **derangement** is a shuffle where **nothing** stays in its place (e.g. a secret-gift exchange where nobody draws their own name).

1. Count derangements of n items by brute force for n ≤ 10.
2. Derive the inclusion–exclusion formula: D(n) = n! (1 − 1/1! + 1/2! − 1/3! + … ± 1/n!). Check it against brute force.
3. Compute D(n)/n! for n = 1 … 12. What number does it approach? (Compare with 1/e ≈ 0.3679.)

**Done when:** formula matches brute force; the limit observed and stated.

### Milestone 4 — Probability, three ways

For each problem: compute the **exact** probability as a `Fraction` (M05!) by enumerating the sample space; **simulate** 100,000 trials (seeded); and state the answer to yourself *before* computing [W].

1. **Two dice:** P(sum = 7); P(at least one six).
2. **Monty Hall:** three doors, one prize. You pick a door; the host, who knows where the prize is, opens another door with no prize; you may switch. P(win if you switch)? (Write your gut answer first. Many people — including professional mathematicians — got this wrong when it was first published.)
3. **Conditional probability:** a test for a rare condition (1 in 1,000) is 99% accurate both ways. If you test positive, what's the chance you have it? (Enumerate a population of 100,000.)
4. **Expected fixed points:** in a random shuffle of n cards, how many cards stay in place, on average? Simulate for n = 5, 10, 52. Then prove the answer with **linearity of expectation** (Unit 8) in two lines.
5. **Birthday paradox:** how many people are needed before two share a birthday with probability over 50%? Exact (product formula), simulated, and compared.

**Done when:** all five, each with exact, simulated, and your prior guess recorded.

**Checkpoint:** [Milestone Checkpoint](<../../../04 - System/Milestone Checkpoint Template.md>). Feynman target: *Monty Hall* — explain why switching wins, in plain words, without formulas. (Hint: imagine 100 doors.)

### Milestone 5 — The hash-collision experiment

A **hash function** maps data to a number in a fixed range. Hash tables (Module 05) depend on different items getting different numbers — but with N possible values, collisions start much sooner than N items. How soon?

1. Make a small hash: take `hashlib.sha256` of a string and keep only the first **16 bits** (N = 65,536 possible values).
2. **Predict** with the birthday approximation: the first collision is expected after about √(πN/2) items (≈ 321 for N = 65,536). Also compute the exact 50% point from your Milestone 4 birthday formula with 65,536 "days."
3. **Measure:** hash `"item0"`, `"item1"`, … until the first collision. Repeat 1,000 times (with different prefixes). Record the average and the distribution (a text histogram).
4. Repeat for 8, 12, 20, and 24 bits. How does the first-collision point grow with the number of bits? (M11: it's about 2^(bits/2).) What does that mean for a 128-bit or 256-bit hash?

**Done when:** predictions vs measurements for five hash sizes, and the 2^(bits/2) rule confirmed.

---

## Testing guidance

- The whole project *is* testing: brute force is the oracle for every formula.
- **Seeds** for every simulation, and enough trials that random error is small (with 100,000 trials, simulated probabilities are typically within about ±0.003 of the truth).
- **Exact fractions** for exact answers — never floats.

## Common pitfalls

- **Order matters or doesn't?** The most common counting error. Ask it out loud before every formula.
- **Enumerating something too big:** 12! is 479 million. Keep brute-force sizes small; let formulas handle big n.
- **Simulation bugs that agree with wrong intuition:** e.g. a Monty Hall simulation where the host opens a random door (sometimes revealing the prize). Re-read the problem; model it exactly.

## Communication deliverable

1. **Lab report** ([template](<../../../04 - System/Lab Report Template.md>), E10 level): *"How many items before a hash collides?"* — prediction from the birthday bound, measurements for five sizes, the 2^(bits/2) rule, and one paragraph on what it means for hash tables and for security.
2. **Three bijective proofs** in the Proof Journal (Milestone 2).
3. Optional: a 3-minute spoken Monty Hall explanation (great Feynman practice).

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Before each milestone, write the relevant formulas and their reasons from memory |
| **F** | Monty Hall; why collisions come early |
| **W** | Reasons in comments for every claim; gut guesses recorded before computing |
| **S** | Count → formula → reason, the same three steps every time |
| **I** | Counting, sets, and probability mixed in every milestone |
| **T** | Report and proofs |

## Stretch goals

- **Generating functions:** count ways to make change for a dollar with coins of 1, 5, 10, 25, by multiplying polynomials. Verify by brute force.
- **Catalan numbers:** count balanced bracket strings of length 2n by brute force; find the formula; find the bijection with lattice paths that stay above the diagonal.
- **Random graph experiment:** how many random edges until a graph on n vertices becomes connected? (A preview of Module 05's graph algorithms.)

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Checker and claims | 12+ claims with reasons; planted error caught | 8+ claims | Few |
| Bijections | Three coded, tested, and proved | Two | One |
| Inclusion–exclusion | Formula derived and verified; limit stated | Verified | Missing |
| Probability | Five problems, exact + simulated + prior guess | Four | Fewer |
| Hash experiment | Five sizes, prediction vs measurement, rule stated | Three sizes | Missing |
| Communication | Report clear; proofs complete | One | Neither |

**Done when:** every area at least 2.

## Connections

- **Back:** M05 (fractions), M11 (growth), Module 02 (recursion, permutations), Units 4, 6, 8.
- **Forward:** Module 05 (hash tables, counting comparisons, probabilistic analysis), Module 09 (probability of packet loss and checksums missing errors), Module 12 (probability and statistics in depth).

> **Originality note:** the three-way checking framework and experiment design were written for this curriculum.
