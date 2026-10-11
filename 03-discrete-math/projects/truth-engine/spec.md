---
title: "Project: Truth Engine"
id: "MOD03-PRJ-truth-engine"
type: "project"
module: "03-discrete-math"
phase: "B"
order: 530
prerequisites: [MOD03-U1, MOD03-U3, MOD02-PRJ-worldfile]
artifact: "truth: a propositional-logic toolkit — parser, truth tables, equivalence checking, normal forms, brute-force and DPLL satisfiability, and puzzle solvers"
deliverable: "README + 2-page write-up of puzzle encodings and the brute-force vs DPLL measurements + short demo"
---

# Project: Truth Engine

| | |
| :-- | :-- |
| **Module** | 03 Discrete Math |
| **Prerequisites** | Unit 1 (logic), Unit 3 (induction); [Worldfile](../../../02-programming-fundamentals/projects/worldfile/spec.md)'s condition parser |
| **You build** | `truth`, a tool that reads logical formulas, prints truth tables, decides whether two formulas mean the same thing, converts formulas to standard forms, and solves **satisfiability** — "is there any way to make this true?" — first by trying everything, then with a much smarter algorithm. Then you use it to solve logic puzzles stated in English |
| **Deliverable** | README, a short write-up, and a demo |

---

## Why this matters

Unit 1 asks you to build truth tables and check equivalences by hand. This project makes the machine do it — and in building it, you'll understand the logic far better than drill alone could give you.

**Satisfiability (SAT)** is one of the most important problems in computer science. Trying every assignment takes 2ⁿ steps for n variables (M11: hopeless beyond about 30). Yet modern SAT solvers routinely handle millions of variables, and they're used to verify chips, check software, plan schedules, and solve puzzles. You'll implement the core idea behind them (DPLL, from 1962) and measure the difference yourself.

And Boolean logic **is** digital logic: the formulas you simplify here are the circuits you build in [Module 04](../../../04-circuits-and-digital-logic/overview.md).

**Real-world analogs:** SAT solvers (MiniSat, CaDiCaL), hardware verification, logic minimisers, type checkers and package-dependency resolvers (both often use SAT inside).

---

## The formula language

```
formula := iff
iff     := implies ("<->" implies)*
implies := or ("->" implies)?          # right-associative: a -> b -> c means a -> (b -> c)
or      := xor ("or" xor)*
xor     := and ("xor" and)*
and     := not ("and" not)*
not     := "not" not | atom
atom    := NAME | "T" | "F" | "(" formula ")"
```

Also accept the symbols `!` `&` `|` `^` for not/and/or/xor. Variable names are lowercase letters, digits, and `_`.

---

## Milestones

### Milestone 1 — Parse and print

1. Tokenizer and recursive-descent parser producing a tree (reuse and extend your Worldfile code: that's what it's for).
2. **Pretty printer** that writes a tree back as text with the **fewest brackets** needed for the precedence rules.
3. **Round-trip property test:** for 1,000 **randomly generated** formula trees (write a generator with a seeded RNG and a depth limit), `parse(pretty(tree)) == tree`.

**Done when:** the round-trip test passes; parse errors give the column and what was expected.

**[W]:** why is `->` right-associative? (Hint: what does "if a then (if b then c)" say, and how often do people mean "(if a then b) then c"?)

### Milestone 2 — Truth tables, classification, equivalence

1. `variables(f)` — sorted list of variable names.
2. `evaluate(f, assignment)` — recursive.
3. `truth table` — print every row (2ⁿ of them, in binary counting order: M01!) with a column for the result.
4. **Classify:** tautology (always true), contradiction (always false), or contingent.
5. **Equivalence:** f and g are equivalent iff `f <-> g` is a tautology. When they're not, print a **counterexample** assignment.

**Verify with Unit 1 laws:** write tests asserting that De Morgan's laws, distributivity, contrapositive (`p -> q` ≡ `not q -> not p`), and `p -> q` ≡ `not p or q` are tautologies — and that the **converse** is *not* equivalent (with the counterexample printed).

```
$ truth equiv "p -> q" "q -> p"
NOT equivalent. Counterexample: p=F, q=T  (left = T, right = F)
```

**Done when:** all law tests pass and the CLI works.

**Checkpoint:** [Milestone Checkpoint](<../../../04 - System/Milestone Checkpoint Template.md>). Feynman target: *why checking equivalence is the same as checking that an iff is a tautology*.

### Milestone 3 — Normal forms

1. **NNF** (negation normal form): push every `not` down to the variables, using De Morgan's laws and double negation, and rewriting `->`, `<->`, `xor` in terms of and/or/not.
2. **CNF** (conjunctive normal form): an AND of ORs of literals (a **literal** is a variable or its negation), by distributing `or` over `and`.
3. **Check every conversion** by equivalence (Milestone 2) on your random formulas — a differential test: your converter must never change the meaning.
4. **Measure the blow-up:** convert (a₁ and b₁) or (a₂ and b₂) or … or (aₖ and bₖ) to CNF for k = 1 to 12. Count the clauses. Predict the formula first [W]. (You should find 2ᵏ. Distribution can make formulas exponentially larger — a real problem real tools work around.)

**Done when:** conversions pass the equivalence check on 500 random formulas, and the blow-up table matches your prediction.

### Milestone 4 — Brute-force SAT and English puzzles

1. `sat(f)` — try all 2ⁿ assignments; return a satisfying one, or `None`.
2. **Puzzles from English** (this is the Unit 1 translation skill — and E07's *if/unless/only if* precision). For each, define variables, translate every sentence into a formula, AND them together, and let `sat` find the answer. Then check whether the answer is **unique** (add the negation of the found answer and run again).
   - **Knights and knaves:** on an island, knights always tell the truth, knaves always lie. *A says: "B is a knave." B says: "A and I are both knights."* What are A and B? (Variable `a` = "A is a knight." A's statement is true iff A is a knight: `a <-> not b`.) Write three puzzles of your own too.
   - **Scheduling:** five study sessions (math, English, build, review, rest) into five slots, with rules like "build is not first", "review comes right after build", "rest is not next to math." (One variable per (session, slot) pair; constraints in CNF-ish form.)
3. **Timing:** how many variables can brute force handle in 10 seconds? Measure for n = 10, 15, 20, 22, 24. Plot. (M11: what curve is it?)

**Done when:** all puzzles solved with uniqueness checked, and the timing table done.

### Milestone 5 — DPLL

The **DPLL algorithm** (Davis, Putnam, Logemann, Loveland, 1962) searches assignments cleverly, working on CNF:

**Subgoal labels [S]:**
```
# DPLL(clauses, assignment):
# 1. Simplify: remove clauses already satisfied; remove false literals from the rest
# 2. If no clauses remain → SAT (return the assignment)
# 3. If any clause is empty → this branch fails (return None)
# 4. Unit propagation: if a clause has exactly one literal, that literal MUST be true — set it, go to 1
# 5. (Optional) Pure literals: a variable that appears with only one sign can be set to make it true
# 6. Choose an unassigned variable; try it True (recurse); if that fails, try False (recurse)
```

It's recursive (Module 02 Lab 01) and you'll prove it correct in your [Proof Journal](../proof-journal/spec.md) (sketch: each step keeps satisfiability unchanged).

**Hard tests:**
- **4×4 Sudoku** (digits 1–4, rows, columns, and 2×2 boxes each contain each digit once): 64 variables `x_r_c_d` = "cell (r, c) holds d." Brute force needs 2⁶⁴ tries — impossible. DPLL should solve it in well under a second.
- **8 queens:** place 8 queens on a chessboard so none attack each other (64 variables).
- **Pigeonhole:** "n + 1 pigeons in n holes, each pigeon in some hole, no two in the same hole" is **unsatisfiable** (Unit 6!). Time DPLL proving it for n = 4 … 9. It gets slow fast — even smart solvers struggle with this family. Why might that be? [W]

**Second witness (optional):** write your CNF in the standard DIMACS format and run a real solver (`minisat`, available in most package managers). Do the answers agree?

**Done when:** Sudoku and 8 queens solved by DPLL; the brute-force vs DPLL comparison and the pigeonhole timing table are done.

**Checkpoint:** Milestone Checkpoint. Why-ladder target: *why does unit propagation never throw away a solution?*

---

## Testing guidance

- **Random formulas + truth tables** are your oracle: any transformation must preserve equivalence; any SAT answer must actually satisfy the formula (check it!); any UNSAT answer on small formulas must agree with brute force.
- **Seeded generators** so failures can be replayed.
- **Small cases by hand** first (Unit 1 exercises are perfect fixtures).

## Common pitfalls

- **Precedence bugs** in the parser. Round-trip testing catches most.
- **Exponential memory:** don't build the whole truth table in memory for 25 variables; stream rows.
- **Mutating shared clause lists** in DPLL recursion: copy, or undo changes on backtrack.
- **Trusting a SAT answer without checking it.** Always evaluate the formula under the returned assignment.

## Communication deliverable

1. **README:** every command, the formula language, and examples.
2. **Write-up (2 pages, E09–E10 level):** how you encoded Sudoku and the scheduling puzzle (one example clause of each kind, explained in English); the brute-force vs DPLL table; the pigeonhole result and your explanation.
3. **Demo:** an equivalence check with a counterexample, a knights-and-knaves puzzle from English to answer, and DPLL solving Sudoku.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Before Milestone 3, write De Morgan, distributivity, and the implication rewrite from memory |
| **F** | Equivalence = tautology of iff; how DPLL prunes |
| **W** | Right-associative `->`; CNF blow-up; unit propagation safety; pigeonhole hardness |
| **S** | DPLL subgoals; the puzzle-encoding steps (variables → sentences → formulas → AND) |
| **I** | Unit 1 problems are interleaved with building; puzzles mix logic and counting |
| **T** | README, write-up, demo |

## Stretch goals

- **Tseitin encoding:** convert to CNF *without* exponential blow-up by introducing new variables. Measure the difference on Milestone 3's family.
- **Clause learning:** read about CDCL (conflict-driven clause learning, the idea behind modern solvers) and add a simple version.
- **Circuit checker:** describe a half adder and full adder as formulas, and prove (by equivalence checking) that your Module 04 gate designs compute the right functions.

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Parser and printer | Full grammar, minimal brackets, random round-trip | Works | Precedence bugs |
| Tables and equivalence | Classification, counterexamples, Unit 1 laws tested | Most | Missing |
| Normal forms | NNF and CNF, differentially tested, blow-up measured | One form | Missing |
| Brute force and puzzles | Puzzles from English, uniqueness checked, timing table | Some puzzles | Missing |
| DPLL | Sudoku, 8 queens, pigeonhole timing; answers verified | Small cases | Missing |
| Communication | README, write-up, demo | Most | Few |

**Done when:** every area at least 2; DPLL at 3.

## Connections

- **Back:** Unit 1, Unit 3; Worldfile's parser; M01 (binary counting enumerates assignments); M11 (2ⁿ growth).
- **Forward:** Module 04 (Boolean algebra = gates; simplification = fewer chips); Module 05 (backtracking search; exponential vs polynomial algorithms).

> **Originality note:** the milestone structure, puzzle set, and measurement tasks were designed for this curriculum. DPLL and the DIMACS format are classic published methods, used here as components.
