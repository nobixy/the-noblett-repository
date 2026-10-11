---
title: "12 — Resources"
id: "MOD12-RES"
type: "reference"
module: "12-math-for-engineering"
phase: "C"
order: 890
prerequisites: []
---

# 12 — Resources

*Pointers only. Study the units with these; the projects apply them.*

## Calculus
- **OpenStax *Calculus* Volumes 1–3** (openstax.org, free) — complete, with worked examples and answers to odd problems.
- **MIT 18.01SC Single Variable Calculus** (OCW) — problem sets with solutions and exams for the module-close test.
- **Numerical methods:** *Numerical Recipes* (Press et al.) chapters on integration and ODEs, as a reference.

## Linear algebra
- **Gilbert Strang, *Introduction to Linear Algebra*** (book) and **MIT 18.06SC** (OCW) — problem sets with solutions; its lectures fill the L3–L4 gaps listed under [Video course](#video-course).
- **Sheldon Axler, *Linear Algebra Done Right*** (free online) — for later, the proof-based view.

## Probability and statistics
- **Grinstead & Snell, *Introduction to Probability*** (free PDF).
- **Allen Downey, *Think Stats*** and ***Think Bayes*** (free) — computational, Python-first.
- **Seeing Theory** (seeing-theory.brown.edu) — beautiful interactive visualisations of distributions, the CLT, and intervals.
- **MIT 6.041 / 6.3700 Probabilistic Systems Analysis** (OCW) — problems with solutions.
- **Efron & Tibshirani, *An Introduction to the Bootstrap*** — the source, if you want depth.

## Signals
- **Steven W. Smith, *The Scientist and Engineer's Guide to Digital Signal Processing*** (free at dspguide.com) — practical and clear; chapters 8–12 (DFT, FFT) and 15–16 (moving-average and windowed filters).
- **phyphox** (phyphox.org) — the free phone-sensor app used in Motion Lab.

## Video course

*Companions, not replacements: your labs and projects are the course. Watch with the [V protocol](../study-protocols.md#v--watch-actively) (pause, predict, then blank-sheet [R]), take lectures and quizzes as second explanations, and build this module's own projects, not the course's assignments. How courses fit your sessions: [study-protocols § Using video courses](../study-protocols.md#using-video-courses).*

**Primary — Essence of Calculus and Essence of Linear Algebra**, 3Blue1Brown (Grant Sanderson). Free on YouTube: [Essence of Calculus](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr) · [Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) · [3blue1brown.com lessons](https://www.3blue1brown.com/lessons/essence-of-calculus/)
- **Why it fits:** this module is applied, computational math for someone who rebuilt arithmetic and algebra in Foundations. 3Blue1Brown gives the geometric *meaning* first (a derivative as a rate, a matrix as a transformation, an eigenvector as a direction that only stretches), which is what Motion Lab and Matrix Studio need before you code the numerics. Both series are short, famous for their clarity, and free. Two single videos from the same channel cover S1 and P2: [But what is the Fourier Transform? A visual introduction](https://www.youtube.com/watch?v=spUNpyF58BY) and [But what is the Central Limit Theorem?](https://www.youtube.com/watch?v=zeJD6dqJ5lo).

**Alternate — Harvard Stat 110: Probability**, Prof. Joe Blitzstein. Free on YouTube: [Probability Lecture Videos by Joe Blitzstein (Harvard)](https://www.youtube.com/playlist?list=PLLVplP8OIVc8EktkrD3Q8td0GmId7DjW0).
- **Why:** 3Blue1Brown has no probability course, and the P units are the largest gap. Stat 110 is one of the best-loved probability courses anywhere: story proofs, simulation-friendly intuition, and every distribution Chance Lab uses.

### Lecture-to-vault map

3Blue1Brown entries are chapter numbers; Stat 110 entries are lecture numbers.

| Unit · vault item | 3Blue1Brown (primary) | Stat 110 (alternate) |
| :-- | :-- | :-- |
| C1 Rates and derivatives · [Motion Lab](projects/motion-lab/spec.md) | Calculus ch. 1 The essence of calculus · ch. 2 The paradox of the derivative · ch. 3 Derivative formulas through geometry · ch. 4 Chain rule and product rule · ch. 5 Euler's number e · ch. 7 Limits | — |
| C2 Accumulation and integrals · Motion Lab | Calculus ch. 8 Integration and the fundamental theorem · ch. 9 What does area have to do with slope? | — |
| C3 Differential equations · Motion Lab | Calculus ch. 10 Higher order derivatives · ch. 11 Taylor series | — |
| L1 Vectors · [Matrix Studio](projects/matrix-studio/spec.md) | Linear Algebra ch. 1 Vectors · ch. 2 Linear combinations, span, and basis vectors · ch. 9 Dot products and duality | — |
| L2 Matrices as transformations · Matrix Studio | Linear Algebra ch. 3 Linear transformations and matrices · ch. 4 Matrix multiplication as composition · ch. 6 The determinant · ch. 7 Inverse matrices, column space and null space | — |
| L3 Linear systems and least squares · Matrix Studio | Linear Algebra ch. 7 Inverse matrices, column space and null space · ch. 13 Change of basis | — |
| L4 Eigenvectors and the SVD · Matrix Studio, Chance Lab | Linear Algebra ch. 14 Eigenvectors and eigenvalues · ch. 15 A quick trick for computing eigenvalues | Lectures 31–33 Markov Chains |
| P1 Random variables · [Chance Lab](projects/chance-lab/spec.md) | — | Lectures 1–8 (counting, conditional probability, random variables) · 11 Poisson · 12 Discrete vs. Continuous, the Uniform · 13 Normal · 16 Exponential |
| P2 Expectation and limits · Chance Lab | But what is the Central Limit Theorem? | Lectures 9–10 Expectation · 21 Covariance and Correlation · 29 Law of Large Numbers and Central Limit Theorem |
| P3 Inference · Chance Lab | — | — (see Gaps) |
| S1 Signals · [Lab 01 — Fourier by ear](labs/lab-01-fourier-by-ear.md) | But what is the Fourier Transform? A visual introduction | — |

**Gaps:**
- **C3:** neither pick teaches numerical ODE methods (Euler, RK4); use OpenStax and *Numerical Recipes* above.
- **L3 and L4:** for elimination, LU, least squares and the SVD, use MIT 18.06SC ([playlist](https://www.youtube.com/playlist?list=PL221E2BBF13BECF6C), [OCW](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/)): lectures 2 Elimination with Matrices, 4 Factorization into A = LU, 15 Projections onto Subspaces, 16 Projection Matrices and Least Squares, 21 Eigenvalues and Eigenvectors, 24 Markov Matrices, 29 Singular Value Decomposition.
- **P3:** for confidence intervals, the bootstrap and permutation tests, use *Think Stats* and Seeing Theory above.
