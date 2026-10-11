---
title: "Lab 01 — Proof Writing Workshop"
id: "MOD03-LAB01"
type: "lab"
module: "03-discrete-math"
phase: "B"
order: 510
prerequisites: []
---

# Lab 01 — Proof Writing Workshop

**Goal:** learn the five basic proof methods as templates with labelled steps, the style rules that make a proof readable, and the common errors that make one wrong.

**Sessions:** three. Do it during Unit 2.

---

## Session 1 — What a proof is

A **proof** is an argument that a statement is true in **every** case, where each step follows from definitions, earlier results, or previous steps. Checking examples is not a proof (examples show *some* cases; a proof covers *all*). But examples are how you *find* a proof — always try several first.

### The anatomy of a proof

1. **The claim**, stated precisely.
2. **The method** ("We prove the contrapositive." / "Suppose, for contradiction, that…").
3. **Setup:** introduce every variable and say what it is ("Let n be an even integer. Then n = 2k for some integer k.").
4. **The chain of steps**, each with its reason.
5. **The conclusion**: say what you have shown, and mark the end (∎).

### Style rules (use them in every proof you write)

1. **Full sentences.** Symbols are words inside sentences, not replacements for them. ("Since n = 2k, we have n² = 4k² = 2(2k²).")
2. **Define every variable before using it**, and say where it comes from ("for some integer k").
3. **Justify every step** that isn't plain algebra ("by the definition of odd", "by Lemma 1", "by the induction hypothesis").
4. **Never write "clearly" or "obviously."** If it's clear, one short sentence will show it. If you can't write that sentence, it isn't clear.
5. **Say where you're going.** Readers follow a proof better when they know the plan (E09: signposting).
6. **Use the definitions.** Most early proofs are: write out the definitions, then do algebra. "n is even" means "n = 2k for some integer k." Write it out.

### Template 1 — Direct proof

To prove **"if P, then Q"**: assume P; derive Q.

> **Claim.** The sum of two even integers is even.
> **Proof.** *[Setup]* Let a and b be even integers. *[Definitions]* By the definition of even, a = 2j and b = 2k for some integers j and k. *[Algebra]* Then a + b = 2j + 2k = 2(j + k). *[Conclude]* Since j + k is an integer, a + b is even by definition. ∎

**Subgoal labels:** assume the hypothesis → unpack definitions → algebra → repack into the definition of the conclusion.

**Exercises:** prove directly: (1) the product of two odd integers is odd; (2) if a divides b and b divides c, then a divides c; (3) the square of an odd integer is one more than a multiple of 8. (*Hint for 3:* write the odd number as 2k + 1 and use that k(k + 1) is always even. Why is it?)

---

## Session 2 — Contrapositive, contradiction, cases

### Template 2 — Proof by contrapositive

"If P then Q" is logically equivalent to "if not Q then not P" (Unit 1: check with a truth table). Sometimes the second is easier.

> **Claim.** For any integer n, if n² is even, then n is even.
> **Proof.** We prove the contrapositive: if n is odd, then n² is odd. Let n be odd; then n = 2k + 1 for some integer k. So n² = 4k² + 4k + 1 = 2(2k² + 2k) + 1, which is odd by definition. Since the contrapositive is true, so is the original statement. ∎

**When to use it:** when the conclusion ("n is even") is easier to *assume the negation of* than to reach directly.

> **Don't confuse the contrapositive with the converse.** The converse of "if P then Q" is "if Q then P," and it is **not** equivalent. "If it's a square, it's a rectangle" is true; its converse, "if it's a rectangle, it's a square," is false.

### Template 3 — Proof by contradiction

To prove S: assume **not S**, and derive something impossible.

> **Claim.** √2 is irrational (it can't be written as a fraction a/b of integers).
> **Proof.** Suppose, for contradiction, that √2 = a/b for integers a and b, with b ≠ 0 and the fraction in lowest terms (M05: we can always simplify). Squaring, 2 = a²/b², so a² = 2b². So a² is even, and by the previous claim, a is even: a = 2c for some integer c. Then 4c² = 2b², so b² = 2c², so b² is even, and so b is even. But then a and b are both even, so a/b was not in lowest terms — a contradiction. So √2 is irrational. ∎

You've already seen one: Euclid's proof of infinitely many primes (M04 Part 5).

**Subgoal labels:** assume the opposite → follow consequences → reach something that contradicts an assumption or a known fact → conclude.

### Template 4 — Proof by cases

Split into cases that cover **every** possibility, and prove each.

> **Claim.** For every integer n, n² + n is even.
> **Proof.** Either n is even or n is odd. *Case 1:* n = 2k. Then n² + n = 4k² + 2k = 2(2k² + k), even. *Case 2:* n = 2k + 1. Then n² + n = (4k² + 4k + 1) + (2k + 1) = 4k² + 6k + 2 = 2(2k² + 3k + 1), even. In every case n² + n is even. ∎

### Template 5 — Disproof by counterexample

To show "for all x, P(x)" is **false**, one example where P fails is enough.

> **Claim (false).** Every odd number greater than 1 is prime. **Counterexample:** 9 is odd and greater than 1, but 9 = 3 × 3. ∎

**Exercises:** (1) contrapositive: if n² is odd, then n is odd; (2) contradiction: there is no largest even integer; (3) cases: for any integer n, n³ − n is divisible by 3 (cases: n mod 3 = 0, 1, 2 — M03!); (4) find a counterexample: "if a divides bc, then a divides b or a divides c."

---

## Session 3 — Finding errors, and review

### Broken proofs

Each "proof" below is wrong. Find the error and explain it in one or two sentences.

1. *"Claim: the sum of two odd integers is odd. Proof: 3 + 5 = 8… wait, let me try 1 + 1 = 2."* (What does a correct attempt teach you about the claim?)
2. *"Claim: if n² is even then n is even. Proof: let n be even; then n = 2k and n² = 4k², which is even. ∎"*
3. *"Claim: for all integers x, if x² = 4 then x = 2. Proof: x² = 4, so x = √4 = 2. ∎"*
4. *"Claim: every integer greater than 1 is a product of primes. Proof: 6 = 2 × 3, 12 = 2 × 2 × 3, 35 = 5 × 7. It works for all of these, so it's true. ∎"*
5. *"Claim: 1 = 2. Proof: let a = b. Then a² = ab, so a² − b² = ab − b², so (a + b)(a − b) = b(a − b), so a + b = b, so 2b = b, so 2 = 1. ∎"*

<details>
<summary>Answers</summary>

1. The claim is false (1 + 1 = 2 is even); a single counterexample disproves it. Testing is how you discover that.
2. It proves the **converse** (even → square even), not the claim (square even → even).
3. x = −2 also satisfies x² = 4. The step "x = √4" ignores the negative root. The claim is false.
4. Examples aren't a proof; a proof must cover every integer. (The claim is true — proved by strong induction in Unit 3.)
5. Dividing by (a − b), which is 0 since a = b. Division by zero (M03) hides inside algebra.
</details>

### Peer review (or self-review in a later session)

Review a proof using these questions (your future Proof Journal rubric):
- Is the claim stated exactly?
- Is the method announced?
- Is every variable introduced with its type and origin?
- Is every non-algebra step justified?
- Does every case get covered?
- Would a classmate who knows the definitions but not the proof be convinced?

---

## Done when

- [ ] All exercises written in full sentences, following the style rules.
- [ ] All five broken proofs diagnosed.
- [ ] The five templates on flashcards (their subgoal labels), and you can recall them blank-sheet [R].

## Retrieval and reflection

1. **[R]:** the five templates' labels, the six style rules, and the difference between contrapositive and converse.
2. **[F] (spoken):** "What is proof by contradiction?" using √2.
3. **[W]:** why is "if P then Q" true when P is false? (Hint: "If you score 90%, I'll buy you dinner." You scored 70% and I didn't buy dinner. Did I break my promise?)

**Next:** start the [Proof Journal](../projects/proof-journal/spec.md).
