---
title: "Lab 02 — Invariants and Program Correctness"
module: "03-discrete-math"
hours: 6
---

# Lab 02 — Invariants and Program Correctness

**Goal:** prove that your own code is correct — loops with **invariants**, recursive functions with **induction** — and turn those proofs into `assert` checks that run while you test.

**Time:** about 6 hours, in three sessions. Do it during Unit 3.

---

## Session 1 — Induction, briefly (2 hours)

To prove a statement P(n) for every whole number n ≥ n₀:
1. **Base case:** prove P(n₀).
2. **Inductive step:** assume P(k) for some k ≥ n₀ (the **induction hypothesis**), and prove P(k + 1).

Then P holds for all n ≥ n₀: P(n₀) is true; so P(n₀ + 1) is; so P(n₀ + 2) is; and so on forever.

> **Claim.** For every n ≥ 1, 1 + 2 + … + n = n(n + 1)/2. (M11's Gauss formula.)
> **Proof.** By induction on n. *Base case (n = 1):* the left side is 1; the right side is 1·2/2 = 1. ✓
> *Inductive step:* assume 1 + … + k = k(k + 1)/2 for some k ≥ 1. Then 1 + … + k + (k + 1) = k(k + 1)/2 + (k + 1) (by the hypothesis) = (k + 1)(k/2 + 1) = (k + 1)(k + 2)/2, which is the formula for n = k + 1. ∎

**Strong induction:** in the inductive step, you may assume P is true for **all** values from n₀ up to k, not just k. Use it when the step to k + 1 needs a smaller case that isn't just k (e.g. "every integer > 1 is a product of primes": k + 1 is either prime, or it's a × b with both smaller — and the hypothesis covers both).

**Exercises:** prove by induction: (1) 1 + 2 + 4 + … + 2ⁿ⁻¹ = 2ⁿ − 1 (M11's binary sum); (2) n! > 2ⁿ for all n ≥ 4; (3) (strong) every integer n ≥ 2 is a product of primes.

**[W]:** Lab 01 of Module 02 said recursion and induction are the same idea. Now explain why: what plays the role of the base case, and what plays the role of the induction hypothesis, in a recursive function?

---

## Session 2 — Loop invariants (2 hours)

A **loop invariant** is a statement about the program's variables that is true **every time the loop is about to check its condition**. To prove a loop correct:

1. **Initialisation:** the invariant is true before the first iteration.
2. **Maintenance:** if it's true before an iteration, it's still true after.
3. **Termination:** the loop ends, and when it does, the invariant plus the exit condition give the result you want.

This is induction on the number of iterations.

**Example — summing a list:**

```python
def total(xs):
    s, i = 0, 0
    # Invariant: s == sum(xs[0:i])
    while i < len(xs):
        s += xs[i]
        i += 1
    return s
```
- *Initialisation:* i = 0, s = 0 = sum of no items ✓
- *Maintenance:* if s = sum(xs[0:i]) and we add xs[i] and then increase i, then s = sum(xs[0:i]) for the new i ✓
- *Termination:* i increases each time and stops at len(xs); then s = sum(xs[0:len(xs)]) = sum of everything ✓

**Example — Euclid's algorithm:**

```python
def gcd(a, b):
    # requires a >= 0, b >= 0, not both 0
    while b != 0:
        # Invariant: gcd(a, b) == gcd(original a, original b)
        a, b = b, a % b
    return a
```
- *Maintenance* is exactly M04's why-ladder: (a, b) and (b, a mod b) have the same common divisors.
- *Termination:* b is a non-negative integer that strictly decreases (a mod b < b), so it must reach 0.
- *At the end:* gcd(a, 0) = a.

### Invariants as executable checks

Turn each invariant into an `assert` at the top of the loop while testing:

```python
while i < len(xs):
    assert s == sum(xs[0:i])      # slow, but a powerful test
    ...
```

Run your tests with these on; remove (or guard) them for speed later. An invariant check that fails points straight to the iteration where things went wrong.

**Exercises:** state and prove the invariant, then add the assert, for: (1) your binary search from the [Growth and Halving Lab](../../00-foundations/math/projects/growth-and-halving-lab/spec.md) (invariant: *if the target is in the list, it's within `items[lo:hi]`*); (2) M03's repeated-division `to_binary`; (3) a loop that finds the maximum of a list.

---

## Session 3 — Proving recursive functions (2 hours)

For a recursive function, prove correctness by (strong) induction on the size of the input:
- **Base case:** the function's base case returns the right answer.
- **Inductive step:** assuming every recursive call (on a smaller input) returns the right answer, the function combines them correctly.

> **Claim.** `power(b, e)` (fast exponentiation from Module 02 Lab 01) returns bᵉ for every integer e ≥ 0.
> **Proof** by strong induction on e. *Base:* e = 0 returns 1 = b⁰. *Step:* assume `power(b, m)` = bᵐ for all m < e. If e is even, the function returns `power(b, e/2)²` = (b^(e/2))² = bᵉ (exponent law, M07). If e is odd, it returns b · `power(b, e − 1)` = b · bᵉ⁻¹ = bᵉ. Both calls use smaller exponents, so the hypothesis applies. ∎

**Exercises:** prove correct: (1) your recursive `reverse(s)`; (2) your recursive `to_binary(n)`; (3) **termination** of your Worldfile condition parser: argue that every recursive call consumes at least one token, so it can't recurse forever.

---

## Done when

- [ ] Three induction proofs, three loop-invariant proofs (with asserts added and tests passing), three recursive-function proofs — all in full sentences, added to your [Proof Journal](../projects/proof-journal/spec.md).

## Retrieval and reflection

1. **[R]:** the two parts of induction; the three parts of a loop-invariant proof; how to prove a recursive function correct.
2. **[F] (spoken, 2 min):** "What is a loop invariant?" using `total`.
3. **[W]:** a test checks some inputs; a proof covers all of them. Why do we still write tests for code we've proved correct? (Think: can the *code* differ from the algorithm you proved?)
