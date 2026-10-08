---
block_id: "Block 45"
track_id: "Track 5"
title: "Programming Languages and Compilers"
category: "advanced"
term: "Years 4 & 5"
status: not-started
prerequisites:
  - "CS61A"
  - "Nand2Tetris"
  - "SICP"
  - "C Fluency"
  - "Math for CS"
  - "Interpreters"
  - "Software Construction"
target_profile: "Compiler Engineer, Programming Language Designer, Static Analysis Specialist, Formal Verification Engineer"
aliases: [Track 5 - Programming Languages and Compilers, Track 5 - Compilers and Language Runtimes]
tier: "Tier 3 - Depth"
hours_estimate: 400
hours_actual: 0
---

# Track 5: Programming Languages and Compilers

> [!INFO] Track Overview
> - **Track ID:** Track 5
> - **Prerequisites:** [[CS61A]], [[Nand2Tetris]], [[SICP]], [[C Fluency]], [[Math for CS]], [[Interpreters]], [[Software Construction]]
> - **Target Profile:** Compiler Engineer, Programming Language Designer, Static Analysis Specialist, Formal Verification Engineer
> - **Structure:** Two core courses plus three progressive labs and one comprehensive capstone build deliverable.
> - **Curriculum Position:** Elective specialization block across Years 4 & 5 (*"Two deep beats six shallow"*).

---

## 🎯 Why This Track Matters

Programming languages and optimizing compilers form the cognitive and physical bridge between human thought and digital silicon. Every software abstraction—from high-level functional type systems and async runtimes down to operating system kernels—relies on compiler correctness, memory safety guarantees, and aggressive machine-code optimization to execute reliably and efficiently.

This track equips students with both the profound mathematical theory of programming language semantics and the deep engineering systems discipline of compiler optimization. Students master operational and denotational semantics, type systems (Simply Typed Lambda Calculus, Hindley-Milner type inference, System F, dependent types), abstract interpretation, control-flow graph algorithms (Static Single Assignment form, dominance frontiers), machine-level optimization passes (SCCP, GVN, LICM), and target register allocation via graph coloring.

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[CS61A]]
- [[Nand2Tetris]]
- [[SICP]]
- [[C Fluency]]
- [[Math for CS]]
- [[Interpreters]]
- [[Software Construction]]




## 📚 Core Courses

### Course 1: Type Systems & Formal Operational Semantics (Pierce TAPL / Harper PFPL Equivalent)

This course develops the mathematical machinery of formal syntax, reduction semantics, type soundness, and polymorphic type theory.

#### Module 1: Untyped Lambda Calculus & Operational Semantics
- Abstract syntax, free and bound variables, $\alpha$-conversion, and capture-avoiding substitution.
- Small-step structural operational semantics ($\to$) vs big-step natural evaluation semantics ($\Downarrow$).
- Reduction strategies: full $\beta$-reduction, normal order, call-by-name, and call-by-value.
- Computability and Church encodings: encoding Booleans, Church numerals, pairs, lists, and the fixpoint $Y$-combinator.

#### Module 2: The Simply Typed Lambda Calculus ($\lambda^\to$) & Curry-Howard Isomorphism
- Types, typing contexts ($\Gamma$), and inference rules for introduction and elimination.
- The Curry-Howard-Lambek Isomorphism: correspondence between Intuitionistic Propositional Logic (proofs), Simply Typed Lambda Calculus (terms), and Cartesian Closed Categories.
- Strong Normalization (Tait's method): proving that all well-typed terms in $\lambda^\to$ terminate under evaluation.

#### Module 3: Type Soundness (The Wright-Felleisen Framework)
- The syntactic approach to type safety: Progress and Preservation theorems:
  $$\text{Progress: } \vdash e : \tau \implies (e \text{ is a value} \lor \exists e'. e \to e')$$
  $$\text{Preservation: } (\Gamma \vdash e : \tau \land e \to e') \implies \Gamma \vdash e' : \tau$$
- Proof techniques: induction on typing derivations and reduction steps.
- Extending $\lambda^\to$ with state and mutable references: store typings ($\Sigma$) and cyclic pointer graphs.

#### Module 4: Subtyping, Variance & Existential Types
- The subtyping relation ($S <: T$): reflexivity, transitivity, and subsumption.
- Subtyping for records, functions (contravariant parameter, covariant return: $T_1 <: S_1 \land S_2 <: T_2 \implies S_1 \to S_2 <: T_1 \to T_2$), and references (invariance).
- Existential types ($\{ \exists X, T \}$): formal modeling of modular data abstraction and object-oriented encapsulation.

#### Module 5: Polymorphism & Hindley-Milner Type Inference
- Impredicative Polymorphic Lambda Calculus (System F): universal quantification ($\forall X. T$), type abstraction, and type application.
- Parametricity and Reynolds' abstraction theorem; Reynolds-Wadler "theorems for free!".
- Predicative let-polymorphism: the Hindley-Milner type system.
- Algorithm W: unification algorithm (Robinson's unification), principal types, and soundness/completeness proofs.

---

### Course 2: Advanced Optimizing Compilers & Code Generation (Cornell CS 6120 / Cooper & Torczon)

This course explores compiler frontend parsing, intermediate representations, control-flow graphs, Static Single Assignment (SSA) form, machine optimization, and backend register allocation.

#### Module 1: Frontend Architecture & Intermediate Representations (IR)
- Lexing and parsing theory: regular expressions to DFAs, Context-Free Grammars (CFGs), LL(k), LR(1), and LALR parsing tables.
- Intermediate Representations: linear IR (three-address code), graphical IR (Abstract Syntax Trees, Directed Acyclic Graphs), and hybrid IRs (LLVM IR).
- Control Flow Graphs (CFG): basic blocks, entry/exit nodes, predecessor/successor edges, and critical edge splitting.

#### Module 2: Static Single Assignment (SSA) Form
- Defining properties of SSA: every variable is defined exactly once, and uses are dominated by definitions.
- Dominance theory: dominator trees, immediate dominators ($idom$), and Lengauer-Tarjan dominance algorithm.
- Dominance Frontiers ($DF$) and iterated dominance frontiers ($IDF$).
- Minimal SSA construction: Cytron et al. algorithm for placing $\phi$-nodes and renaming variables.
- Translating out of SSA: resolving parallel copies and the "lost-copy" and "swap" problems.

#### Module 3: Dataflow Analysis & Abstract Interpretation
- Classical iterative dataflow frameworks: forward vs backward analysis, meet-over-all-paths (MOP) vs maximum fixed point (MFP).
- Monotone frameworks: semi-lattices, transfer functions, monotonicity, and convergence via Knaster-Tarski fixed-point theorem.
- Canonical analyses: Reaching Definitions, Available Expressions, Live Variable Analysis, and Very Busy Expressions.
- Abstract interpretation: Galois connections ($\alpha, \gamma$), widening operators ($\nabla$), and narrowing operators ($\Delta$) for interval analysis.

#### Module 4: High-Level Machine Optimizations
- Sparse Conditional Constant Propagation (SCCP): combining constant propagation with dead-branch elimination in SSA form.
- Global Value Numbering (GVN) and Common Subexpression Elimination (CSE).
- Loop optimizations: natural loop identification, loop preheaders, Loop-Invariant Code Motion (LICM), induction variable elimination, loop unrolling, and loop vectorization.

#### Module 5: Instruction Selection & Register Allocation
- Instruction selection: tree-rewriting systems, bottom-up rewrite systems (BURS), and maximal munch dynamic programming algorithms.
- Liveness analysis on linear machine instructions and constructing the register interference graph (RIG).
- Chaitin-Briggs graph coloring register allocation: Kempe's heuristic (degree $< K$ simplification), optimistic spilling, coalescing (Briggs and George heuristics), and spill code insertion.

---

## 📑 Seminal Papers & Advanced Textbooks

- **Milner, R. (1978).** *A Theory of Type Polymorphism in Programming*. Journal of Computer and System Sciences, 17(3), 348–375.
- **Cytron, R., Ferrante, J., Rosen, B. K., Wegman, M. N., & Zadeck, F. K. (1991).** *Efficiently Computing Static Single Assignment Form and the Control Dependence Graph*. ACM Transactions on Programming Languages and Systems (TOPLAS), 13(4), 451–490.
- **Leroy, X. (2009).** *Formal verification of a realistic compiler*. Communications of the ACM, 52(7), 107–115.
- **Pierce, B. C. (2002).** *Types and Programming Languages*. MIT Press.
- **Cooper, K. D., & Torczon, L. (2022).** *Engineering a Compiler, 3rd Edition*. Morgan Kaufmann.

---

## 🛠️ Progressive Labs

### Lab 1: Hindley-Milner Type Inference (Algorithm W) in OCaml/Rust
- **Objective:** Implement a complete type inference engine for a functional core language supporting let-polymorphism, algebraic data types, and pattern matching.
- **Deliverables:**
  - Robinson's first-order unification algorithm implementation over polymorphic type terms.
  - Algorithm W implementation generating substitutions and inferring principal types.
- **Acceptance Criteria:**
  - Automated test suite runs across 100 test programs, verifying correct principal type inference for valid programs and generating descriptive type errors for ill-typed expressions.
  - Zero type escapes: passes verification testing asserting that ill-typed programs are rejected without uncaught runtime exceptions.

### Lab 2: Dominance Frontier Calculation & Minimal SSA Conversion
- **Objective:** Build an SSA converter that ingests an arbitrary three-address code CFG, computes dominator trees via Lengauer-Tarjan, and transforms the program into minimal SSA form.
- **Deliverables:**
  - Dominance tree computation module outputting Graphviz DOT representations of dominator trees.
  - $\phi$-function insertion and variable renaming pass implementing Cytron's algorithm.
- **Acceptance Criteria:**
  - Validated across 20 complex CFGs (including deeply nested loops, irreducible graphs, and break/continue constructs).
  - The generated IR verifies 100% adherence to SSA invariants: every variable is assigned exactly once, and every use is strictly dominated by its unique definition.

### Lab 3: Chaitin-Briggs Graph Coloring Register Allocator
- **Objective:** Construct a target register allocator for a RISC-V or x86-64 backend that builds an interference graph from live-range analysis and colors it with $K$ registers.
- **Deliverables:**
  - Liveness analyzer computing live intervals and constructing register interference graphs.
  - Graph coloring module implementing Simplify, Coalesce, Freeze, Spill, and Select phases.
- **Acceptance Criteria:**
  - Allocator compiles functions with complex live ranges targeting $K = 8$ registers without introducing register collisions.
  - Spilling heuristic automatically inserts minimal load/store instructions when chromatic number $\chi(G) > K$, passing execution tests under QEMU.

---

## 🏆 Capstone Build Deliverable

### End-to-End Optimizing Compiler targeting RISC-V with Mechanized Type Soundness Proof

A production-grade compiler pipeline implemented in OCaml, Rust, or C++ that compiles a statically typed imperative/functional language down to valid, executable RISC-V assembly, accompanied by a mechanized type soundness proof in Coq or Lean 4.

```text
+-----------------------------------------------------------------------------------+
|                        OPTIMIZING COMPILER ARCHITECTURE                           |
|                                                                                   |
|  [ Source Code ] ---> [ Lexer & Parser ] ---> [ AST & Hindley-Milner Typecheck ]  |
|                                                               |                   |
|                                                               v                   |
|  [ Coq/Lean Mechanized Soundness ]                  [ SSA IR Generation ]         |
|  (Progress & Preservation Proofs)                             |                   |
|                                                               v                   |
|  [ RISC-V Machine Code ] <--- [ Chaitin-Briggs RegAlloc ] <--- [ GVN, SCCP, LICM ]|
+-----------------------------------------------------------------------------------+
```

#### System Architecture & Specifications
1. **Frontend:** Lexer and parser generating rich Abstract Syntax Trees with precise source coordinate spans; type checker implementing Hindley-Milner type inference with bidirectional type checking.
2. **Intermediate Representation:** SSA-based control-flow intermediate representation with explicit basic blocks, $\phi$-nodes, and dominance tree annotations.
3. **Optimization Engine:** Three verified optimization passes: Sparse Conditional Constant Propagation (SCCP), Global Value Numbering (GVN), and Loop-Invariant Code Motion (LICM).
4. **Backend:** Maximal munch instruction selector emitting RV32IM assembly, Chaitin-Briggs graph coloring register allocator, and peephole optimizer.
5. **Formal Verification Component:** Mechanized proof of type soundness (Progress and Preservation) for the core source language formal semantics formalized in Coq or Lean 4 with 0 `sorry` statements.

#### Verification & Acceptance Criteria
- **Execution & Optimization:** Must compile and run complex benchmark programs (e.g. Quicksort, N-Queens, Mandelbrot fractals, Matrix Multiplication) on an emulated RISC-V system via QEMU or Spike, producing correct output with measurable performance speedup ($\ge 25\%$) over unoptimized code (`-O0`).
- **Mechanized Proof Check:** The Coq/Lean 4 proof files must verify successfully via `coqc` or `lake build` with zero axiomatic assumptions or unproven `sorry` holes.
- **Test Commands:**
  ```bash
  # Run compiler test suite and optimization unit tests
  cargo test --release
  # Verify Coq / Lean 4 formal soundness proofs
  lake build
  # Compile benchmark program to RISC-V assembly and run under QEMU
  ./target/release/mycompiler --opt examples/mandelbrot.src -o build/mandelbrot.s
  riscv64-unknown-elf-gcc -march=rv32im -mabi=ilp32 build/mandelbrot.s -o build/mandelbrot.elf
  qemu-riscv32 build/mandelbrot.elf
  ```

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> Assessment criteria go here.

## ➡️ Next Steps & Degree Pathway
- **Curriculum Hub:** [[Specializations Hub|Specializations Hub]]
- **Degree Assignment:**
  - If chosen as **Primary Specialization (Track A)**: Course 1 binds to [[Specialization A1|Block 26 - Specialization A1]] and Course 2 binds to [[Specialization A2|Block 28 - Specialization A2]].
  - If chosen as **Secondary Specialization (Track B)**: Course 1 binds to [[Specialization B1|Block 29 - Specialization B1]] and Course 2 binds to [[Specialization B2|Block 31 - Specialization B2]].
- **Curriculum Roadmap:** [[00 - Dashboard|Dashboard]] / [[Checklist|Checklist]]

- **Sequential Flow:** [[Systems Formal Verification|← Systems Formal Verification]] | [[00 - Dashboard|Dashboard]] | [[Deep AI and Machine Learning|Deep AI and Machine Learning →]]
