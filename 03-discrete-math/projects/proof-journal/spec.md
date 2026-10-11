---
title: "Project: Proof Journal"
id: "MOD03-PRJ-proof-journal"
type: "project"
module: "03-discrete-math"
phase: "B"
order: 560
prerequisites: []
artifact: "A journal of 25+ carefully written, reviewed, and revised proofs, with a one-page style guide"
deliverable: "The journal itself; two proofs explained out loud (recorded); a before/after reflection"
---

# Project: Proof Journal

| | |
| :-- | :-- |
| **Module** | 03 Discrete Math (runs through Units 2–8) |
| **You build** | A journal of proofs: each one written carefully, reviewed against a checklist, revised after a cooling-off period, and some explained out loud. By the end you have a personal reference of 25+ results you truly understand, and a style you've developed yourself |
| **Deliverable** | The journal, two recorded explanations, and a reflection |

---

## Why this matters

A proof is the most precise kind of writing there is: an argument with no gaps, where every word matters and every step is justified. Learning to write one trains exactly the skills of E08–E10 — topic sentences, old-before-new, defining terms, justifying claims — at maximum precision.

It's also how you'll know you *understand* something rather than recognise it. If you can prove that Euclid's algorithm is correct from a blank page, you understand it; if you can only follow someone else's proof, you don't yet. That's retrieval [R] and Feynman [F] in their strictest form.

And proofs connect straight to engineering: a loop invariant *is* a proof that your code works (Lab 02), and a design doc's "why this approach" section *is* an argument.

---

## The journal format

Keep the journal as Markdown files in `~/workbench/03-proofs/` (one file per unit, or one per proof). Math notation: Markdown with `$…$` LaTeX works in Obsidian, VS Code previews, and GitHub. (Optional: learn real LaTeX and typeset the final versions. It's the standard for mathematical writing.)

Each entry:

```markdown
## P07 — Euclid's algorithm computes the GCD
*Unit 3 · Method: loop invariant · Written 2027-02-03 · Revised 2027-02-10*

**Claim.** For integers a ≥ 0, b ≥ 0, not both zero, the loop … returns gcd(a, b).

**Scratch** (how I found it — keep this messy and honest):
- tried examples (1071, 462) …
- stuck on why the remainder keeps common divisors; wrote stuck note; next session: "anything dividing a and b divides a − qb" …

**Proof.** …  ∎

**Review checklist:** claim ✓ · method ✓ · variables ✓ · steps justified ✓ · all cases ✓ · conclusion ✓
**What I learned:** …
```

The **scratch** section matters: it's where you record the search — the examples, the dead ends, the stuck notes. Mathematicians' real work looks like this; the clean proof is just the final draft.

---

## The required proofs

At least **25**, including these 20 (add your own for the rest). The unit each belongs to is shown; write each one *during* that unit.

| # | Unit | Claim |
| :-- | :-- | :-- |
| P01 | U2 | The product of two odd integers is odd. |
| P02 | U2 | For all integers n: if n² is even, then n is even. (contrapositive) |
| P03 | U2 | √2 is irrational. (contradiction) |
| P04 | U2 | There are infinitely many primes. (Euclid — you've seen it in M04; now write it yourself, from memory) |
| P05 | U2 | For every integer n, n³ − n is divisible by 3. (cases) |
| P06 | U3 | 1 + 2 + … + n = n(n + 1)/2. (induction) |
| P07 | U3 | Euclid's algorithm computes the GCD. (loop invariant + termination) |
| P08 | U3 | Every integer n ≥ 2 is a product of primes. (strong induction) |
| P09 | U3 | Fast exponentiation computes bᵉ. (strong induction on e) |
| P10 | U4 | The composition of two one-to-one functions is one-to-one. |
| P11 | U4 | A set with n elements has 2ⁿ subsets. (induction, or the bijection with binary strings) |
| P12 | U4 | "a ≡ b (mod m)" is an equivalence relation. |
| P13 | U5 | a has an inverse mod m if and only if gcd(a, m) = 1. (both directions) |
| P14 | U5 | Fermat's little theorem. |
| P15 | U5 | RSA decrypts correctly (for gcd(m, n) = 1). |
| P16 | U6 | C(n, k) = C(n, n − k), by a bijection. |
| P17 | U6 | Pascal's identity, by splitting on one element. |
| P18 | U6 | Among any 5 points inside a 2 × 2 square, two are at distance at most √2. (pigeonhole: cut into four 1 × 1 squares) |
| P19 | U7 | In any graph, the sum of all vertex degrees is twice the number of edges (the handshake lemma); so the number of odd-degree vertices is even. |
| P20 | U7 | A tree with n vertices has exactly n − 1 edges. (induction: remove a leaf) |

Plus at least five of your own choosing: from MCS or BoP exercises, from Lab 02, or about your own code (the Worldfile parser always terminates; DPLL's unit propagation preserves satisfiability; Study Deck's Leitner replay is deterministic).

---

## The process for each proof

1. **Understand the claim [S]:** restate it in your own words. Identify the hypothesis and conclusion. Write the definitions involved, exactly.
2. **Explore:** try examples. Try to break it. Draw pictures. (Scratch section.)
3. **Choose a method:** direct, contrapositive, contradiction, cases, induction, bijection. Say why [W].
4. **Draft the proof** in full sentences following the [Lab 01 style rules](../../labs/lab-01-proof-writing-workshop.md).
5. **Cool off [D]:** until a later session.
6. **Review with the checklist.** Is every step justified? Is every case covered? Is every variable introduced?
7. **Revise.** Keep the old version (git keeps it anyway); write one sentence on what you changed.
8. **Recall later [R]:** at least one section later, close the journal and rewrite the proof from a blank page. Compare. Mark P-entries you could reproduce with ★.

**Stuck [D]:** write the stuck note in the scratch section, walk away, return. If stuck after three sessions, read *only the first line* of a published proof (the method), and try again. Read the whole published proof only after a fourth attempt — then close it and write your own version in the next session.

---

## Milestones

| Milestone | After | Done when |
| :-- | :-- | :-- |
| **1** | end of U2 | P01–P05 written, reviewed, revised; your first **style guide** draft (one page: the rules you've found matter most) |
| **2** | end of U3 | P06–P09 done; P04 rewritten from memory at least one section later |
| **3** | end of U5 | P10–P15 done (P13–P15 shared with [Toy Cipher](../toy-cipher/spec.md)) |
| **4** | end of U7 | P16–P20 and your five extra proofs done |
| **5** | module close | ★ recall test on 10 random proofs; two recordings; reflection |

### Recordings [F] [T]

Choose two proofs (one short, one long). Record yourself explaining each **from a blank page or whiteboard**, as if teaching a friend: what the claim says, why it's believable, the key idea, then the steps. Keep each one short. Listen back. Note one improvement.

### Getting feedback

- A study partner who's also learning proofs is ideal: swap two proofs per section and review each other with the checklist.
- Online communities that check proofs are helpful (for example, Math StackExchange's "proof-verification" tag). Post **your** proof and ask a specific question ("Is my induction step justified?"). Follow the community's rules.
- An AI assistant can review a *finished* proof for gaps (README rules: treat comments as questions; don't let it write proofs for you).

---

## Common pitfalls

- **Proof by example** ("it works for 1, 2, 3").
- **Proving the converse** instead of the claim.
- **Using what you're trying to prove** (circular reasoning).
- **"Clearly"** hiding the hard step.
- **Induction without using the hypothesis** — if your inductive step never uses P(k), something's wrong.
- **Skipping the scratch work** and copying the textbook's clean proof. That's recognition, not understanding.

## Communication deliverable

- The journal (25+ proofs) with the style guide at the front.
- Two recordings.
- **Reflection (half a page, at module close):** reread P01 and your latest proof. What changed in how you write? Which style rules matter most? Which proof are you proudest of, and why?

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Section-later rewrites from a blank page; ★ recall test |
| **F** | Recorded explanations |
| **W** | Choosing a method and saying why; every definition questioned |
| **S** | Templates from Lab 01 as subgoal labels |
| **I** | Proofs from different units interleaved in recall tests |
| **D** | Stuck notes in scratch sections; cooling-off before review |
| **C** | Copywork during this module: short proofs from BoP (the clean ones) — rebuild them from hint notes, then diff |
| **T** | Reviews, recordings, reflection |

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Coverage | 25+ proofs including all 20 required | 20 | Fewer |
| Correctness | All reviewed; errors found and fixed | Mostly correct | Gaps |
| Style | Follows your style guide; full sentences; no "clearly" | Mostly | Symbol soup |
| Process | Scratch sections honest; revisions recorded | Some | Clean copies only |
| Recall | ★ on 8+ of 10 random proofs | 5+ | Fewer |
| Communication | Two clear recordings; thoughtful reflection | One | Neither |

**Done when:** every area at least 2; Correctness and Recall at 3.

## Connections

- **Back:** M04's proof that there are infinitely many primes; Lab 01 and Lab 02 of this module.
- **Forward:** Module 05 (proofs of algorithm correctness and running time), Module 11 (why recovery works), and every design doc's "alternatives" section.
