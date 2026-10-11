---
title: "03 — Resources"
id: "MOD03-RES"
type: "reference"
module: "03-discrete-math"
phase: "B"
order: 570
prerequisites: []
---

# 03 — Resources

*Pointers only. The units and projects are the course.*

## Main texts (free)
- **Mathematics for Computer Science** — Eric Lehman, F. Thomson Leighton, Albert R. Meyer (MIT; free PDF). The main text for every unit.
- **Book of Proof** — Richard Hammack (free at richardhammack.github.io/BookOfProof). Gentler; answers to odd-numbered exercises. Start here when MCS feels steep.
- **How to Prove It** — Daniel Velleman (you own it). The best book on *how* to construct proofs; use it heavily in Units 1–2.

## Specific topics
- **SAT and DPLL** — Donald Knuth, *The Art of Computer Programming*, Vol. 4B ("Satisfiability") for the deep end; any lecture notes titled "DPLL algorithm" for the basics.
- **RSA and number theory** — Dan Boneh's "Cryptography I" course (free to audit) for the real-world side, *after* finishing Toy Cipher; Joseph Silverman, *A Friendly Introduction to Number Theory* (book) for more depth.
- **Probability puzzles** — the Monty Hall problem's history (search "Marilyn vos Savant Monty Hall") is a fascinating story of experts being wrong.

## Writing mathematics
- **Kevin Houston, *How to Think Like a Mathematician*** (book) — practical advice on reading and writing proofs.
- **LaTeX** — the *Overleaf* documentation ("Learn LaTeX in 30 minutes") if you want to typeset your journal.

## Video course

*Companions, not replacements: your labs and projects are the course. Watch with the [V protocol](../study-protocols.md#v--watch-actively) (pause, predict, then blank-sheet [R]), take lectures and quizzes as second explanations, and build this module's own projects, not the course's assignments. How courses fit your sessions: [study-protocols § Using video courses](../study-protocols.md#using-video-courses).*

**Primary — MIT 6.042J Mathematics for Computer Science**, MIT OpenCourseWare (Prof. Tom Leighton). Free.
- Lectures: [YouTube playlist](https://www.youtube.com/playlist?list=PLB7540DEDD482705B) · course page with problem sets, solutions and exams: [MIT OCW 6.042J](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/)
- **Why it fits:** the lecturer is a co-author of *Mathematics for Computer Science*, this module's main text, so the lectures follow the book you are already reading: proofs, induction, number theory and RSA, graphs, counting and probability. The OCW problem sets and past exams are the best extra practice for the unit checks and the module-close test.

**Alternate — Discrete Math (Full Course)**, Dr. Trefor Bazett (YouTube). Free: [playlist](https://www.youtube.com/playlist?list=PLHXZ9OQGMqxersk8fUxiUMSIx0DBqsKZS).
- **Why:** short, one-idea videos at a gentler level. Use them when a 6.042J lecture or an MCS section is too steep, especially in Units 1–2 (logic and proof), where Trefor Bazett starts from zero.

### Lecture-to-vault map

| Vault item | MIT 6.042J (primary) | Trefor Bazett (alternate; playlist positions) |
| :-- | :-- | :-- |
| U1 Logic · [Truth Engine](projects/truth-engine/spec.md) | Lecture 1 Introduction and Proofs | videos 10–30 (statements, truth tables, equivalence, conditionals, arguments, quantifiers) |
| U2 Proof · [Lab 01 — Proof writing](labs/lab-01-proof-writing-workshop.md) · [Proof Journal](projects/proof-journal/spec.md) | Lecture 1 Introduction and Proofs | videos 31–39 (definitions, direct proof, counterexamples, cases, contradiction, contrapositive) |
| U3 Induction · [Lab 02 — Invariants](labs/lab-02-invariants-and-program-correctness.md) | Lecture 2 Induction · Lecture 3 Strong Induction | videos 45–49 (induction, strong induction, recursive sequences) |
| U4 Sets, functions, relations | Lecture 11 Relations, Partial Orders, and Scheduling | videos 2–9 (sets, relations, functions) · 50–60 (set proofs, equivalence relations) |
| U5 Modular arithmetic and RSA · [Toy Cipher](projects/toy-cipher/spec.md) | Lecture 4 Number Theory I · Lecture 5 Number Theory II | videos 40–41 (quotient-remainder theorem and modular arithmetic; infinitely many primes) |
| U6 Counting · [Counting Verifier](projects/counting-verifier/spec.md) | Lecture 16 Counting Rules I · Lecture 17 Counting Rules II · Lectures 12–13 Sums | videos 64–70 (inclusion–exclusion, permutations, combinations) |
| U7 Graphs | Lecture 6 Graph Theory and Coloring · Lecture 7 Matching Problems · Lecture 8 Minimum Spanning Trees · Lecture 10 Graph Theory III | videos 81–84 (graph theory basics, degree, Euler paths) |
| U8 Discrete probability | Lecture 18 Probability Introduction · Lecture 19 Conditional Probability · Lecture 21 Random Variables · Lectures 22–23 Expectation | videos 61–63 and 71–77 (probability, conditional probability, Bayes' theorem) |

**Gaps:** SAT solving and DPLL (Truth Engine) are not in either course; use the DPLL pointers above.
