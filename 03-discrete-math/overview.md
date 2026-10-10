---
title: "03 — Discrete Math"
module: "03-discrete-math"
hours: 130
tags: [module, math, discrete]
---

# 03 — Discrete Math

**The mathematics of things you can count, list, and reason about step by step** — which is to say, the mathematics of computers. Logic, proof, induction, sets and functions, modular arithmetic, counting, graphs, and discrete probability. You learn it the way this curriculum learns everything: each idea feeds a build. You'll write a logic engine that solves puzzles, a toy public-key cipher (and break it), a counting verifier that checks formulas by brute force, and a proof journal in which you learn to write the most precise prose there is.

---

## Prerequisites

- Math **M08** (algebra) done; M09–M11 can run alongside this module.
- [02 Programming Fundamentals](../02-programming-fundamentals/overview.md) Lab 01 (recursion) done. (The rest of Module 02 can run in parallel.)
- English **E07+**. Proofs are writing: you'll use complex sentences (*if… then*, *because*, *suppose*) constantly.

## Objectives

By the end you will be able to:
1. Translate English statements into logic and back; build truth tables; recognise equivalent statements; negate statements with quantifiers correctly.
2. Write clear direct proofs, proofs by contrapositive, by contradiction, by cases, and by induction — and spot a broken proof.
3. Prove that a loop or recursive function is correct, using an invariant or induction.
4. Work with sets, functions, and relations, including one-to-one and onto functions.
5. Compute with modular arithmetic: inverses, fast powers, Fermat's little theorem — and explain why RSA works.
6. Count arrangements and selections, and use the pigeonhole principle and inclusion–exclusion.
7. Reason about graphs: degrees, paths, connectivity, trees.
8. Compute discrete probabilities and expected values, and explain the birthday paradox.

---

## The eight units

Each unit lists **what to learn**, **where to read** (free sources), **practice**, and which project uses it. Read in the order shown; projects start once their units are done.

**Free texts used below:**
- **MCS** = *Mathematics for Computer Science*, Lehman, Leighton & Meyer (MIT, free PDF; search the title). The main text.
- **BoP** = *Book of Proof*, Richard Hammack (free at richardhammack.github.io/BookOfProof). Gentler, with answers to odd-numbered exercises. Use it first when MCS feels too fast.
- **Velleman** = *How to Prove It* (you own it). Excellent for Units 1–2.

| Unit | Title | Key ideas | Read | Hours | Project |
| :-- | :-- | :-- | :-- | --: | :-- |
| U1 | Logic | propositions; and/or/not/implies/iff; truth tables; De Morgan; contrapositive vs converse; ∀ and ∃ and their negations | BoP ch. 2; Velleman ch. 1–2 | 10 | [Truth Engine](projects/truth-engine/spec.md) |
| U2 | Proof | direct; contrapositive; contradiction; cases; counterexamples; writing proofs | BoP ch. 4–6; MCS ch. 1 | 12 | [Proof Journal](projects/proof-journal/spec.md) starts |
| U3 | Induction and invariants | weak and strong induction; recursive definitions; loop invariants; correctness of recursive programs | BoP ch. 10; MCS ch. 5–6 | 10 | Proof Journal; [Lab 02](labs/lab-02-invariants-and-program-correctness.md) |
| U4 | Sets, functions, relations | set operations, power sets, Cartesian products; one-to-one/onto/bijections; equivalence relations; partial orders | BoP ch. 1, 11–12; MCS ch. 4 | 10 | Counting Verifier |
| U5 | Modular arithmetic | congruences; GCD and Bézout via extended Euclid; inverses; fast powers; Fermat; RSA | BoP ch. 7 (and ch. 5's divisibility); MCS ch. 9 | 14 | [Toy Cipher](projects/toy-cipher/spec.md) |
| U6 | Counting | sum and product rules; permutations; combinations; binomial theorem; pigeonhole; inclusion–exclusion; stars and bars | BoP ch. 3; MCS ch. 15 | 12 | [Counting Verifier](projects/counting-verifier/spec.md) |
| U7 | Graphs | vertices, edges, degree; handshake lemma; paths and connectivity; trees; bipartite graphs; Euler walks | MCS ch. 12–13 | 8 | Proof Journal; (algorithms in Module 05) |
| U8 | Discrete probability | sample spaces; events; conditional probability; independence; expectation and linearity; birthday paradox | MCS ch. 17–19 | 10 | Counting Verifier |
| | **Units total** | | | **~86** | |

### Projects and labs

| Item | Hours | Uses |
| :-- | --: | :-- |
| [Lab 01 — Proof Writing Workshop](labs/lab-01-proof-writing-workshop.md) | 6 | U2 |
| [Lab 02 — Invariants and Program Correctness](labs/lab-02-invariants-and-program-correctness.md) | 6 | U3 |
| [Truth Engine](projects/truth-engine/spec.md) | 18 | U1, U3 |
| [Toy Cipher](projects/toy-cipher/spec.md) | 16 | U5 |
| [Counting Verifier](projects/counting-verifier/spec.md) | 12 | U4, U6, U8 |
| [Proof Journal](projects/proof-journal/spec.md) | runs through the module (inside unit hours) | U2–U7 |

**Total:** about 130–145 hours. At 10 hours a week (mornings, replacing finished foundation math), about 14 weeks.

---

## How to study each unit

Discrete math is learned by **doing problems and writing proofs**, not by reading. For every unit:

1. **Preview (15 min):** skim the unit's reading — headings, definitions, and the statements of theorems only.
2. **Worked examples with subgoal labels [S] (60–90 min):** for each worked example in the reading, cover the solution and label its steps by *purpose* ("assume the opposite", "use the definition of even", "reach a contradiction"). Your labels become the method.
3. **Problems (bulk of the time) [I]:** do problems from BoP (odd-numbered have answers) and MCS. **Mix units** once you have two or more: each session, at least a third of the problems come from earlier units.
4. **Why-ladders [W]** on every definition: *why is it defined this way? what example would break if it weren't?* (E.g. why is 1 not prime — you did this in M04; why is "if P then Q" true when P is false?)
5. **Blank-sheet recall [R] (15 min) after each session:** definitions, theorem statements, and one proof outline from memory.
6. **Feynman [F] once per unit:** the unit's central idea in plain words, spoken.
7. **Flashcards [I]:** every definition and theorem statement goes into [Study Deck](../02-programming-fundamentals/projects/study-deck/spec.md). Definitions must be recalled **exactly** — in discrete math, the precise wording *is* the meaning.

**Stuck on a proof [D]:** proofs are where diffuse mode pays off most. Work 25 minutes, write a stuck note (what you're trying to show; what you know; what you've tried), walk away, come back tomorrow. Many proofs crack on the second day.

### Communication: the most precise writing you'll ever do

A proof is an argument (E10) with no gaps. Every proof you write follows the [Proof Journal](projects/proof-journal/spec.md) style rules: state what you'll prove, say which method, define every variable, justify every step, and end by saying what you've shown. Writing proofs will sharpen all your other technical writing.

---

## Connections

- **Back:** M04 (primes, GCD, Euclid — you'll now *prove* what you used), M07 (two's complement is arithmetic mod 2ⁿ), M11 (sums and growth; induction proves the formulas); [Prime Factory](../00-foundations/math/projects/prime-factory/spec.md) (reused in Toy Cipher); [Worldfile](../02-programming-fundamentals/projects/worldfile/spec.md) (its condition language becomes Truth Engine's parser).
- **Alongside:** [04 Circuits and Digital Logic](../04-circuits-and-digital-logic/overview.md) — Boolean logic *is* digital logic. Truth Engine's simplifier and Module 04's gate circuits are the same mathematics.
- **Forward:** [05 DSA](../05-data-structures-and-algorithms/overview.md) (graphs, recursion, correctness proofs, counting for analysis, probability for hashing); Module 09 (checksums, modular arithmetic, probability of loss); Module 11 (sets and relations are the foundation of relational databases).

---

## Module close

1. **Cumulative retrieval [R] (60 min, closed book):** every definition from U1–U8 on paper, then the statement and proof outline of five theorems of your choice. Check; flashcard every miss.
2. **Timed problem set (2 hours):** 12 unseen problems mixed across all units (take them from MCS's end-of-chapter problems you haven't done, or from an MIT 6.1200 problem set or exam on OCW). Grade yourself honestly with the solutions. Target: 70%+. Below that, revisit your weakest unit for a week.
3. **Proof Journal review:** reread your first and your latest proof. Write half a page on how your proof writing changed.
4. Tick the module in [Start Here](<../00 - Start Here.md>).

**Next:** [05 Data Structures and Algorithms](../05-data-structures-and-algorithms/overview.md) (after Module 04, or alongside its later labs).
