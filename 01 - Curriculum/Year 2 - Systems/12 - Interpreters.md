---
block_id: "Block 12"
title: "Interpreters and Language Runtimes"
term: "Year 2 January Intensive"
status: not-started
hours_estimate: 130
hours_actual: 0
primary_resource: "Ball, Writing an Interpreter in Go & Nystrom, Crafting Interpreters (Part III)"
milestone: "clox bytecode VM with garbage collection passes book's full test suite"
date_started: ""
date_completed: ""
---

# Block 12 — Interpreters and Language Runtimes

> [!INFO] Block Overview
> - **Term / Position:** Year 2 January Intensive
> - **Estimated Hours:** ~130 hrs
> - **Status:** `not-started`
> - **Primary Resource:** Ball, Writing an Interpreter in Go & Nystrom, Crafting Interpreters (Part III)
> - **Key Milestone:** clox bytecode VM with garbage collection passes book's full test suite

---

## 🎯 Why This Block Matters
Build two complete programming language implementations — one tree-walking interpreter, one high-performance bytecode VM.

---

## 📖 Primary Syllabus & Core Content
- [ ] Thorsten Ball, Writing an Interpreter in Go: Lexing, Pratt parsing, AST evaluation, environment, closures
- [ ] Bob Nystrom, Crafting Interpreters Part III (C VM): Chunks of bytecode, virtual machine loop, value representation, hash tables, stack-based bytecode evaluation, closures, garbage collection (mark-sweep)

---

## 🛠️ Build Requirement
1. Build Monkey in Go (tree-walker). 2. Build `clox` in C (bytecode compiler and VM with GC). Bonus: Ball's Writing a Compiler in Go.

---

## 🏁 Done When
> [!IMPORTANT]
> `clox` passes the book's full test suite cleanly.

---

## 📝 Study Notes, Psets & Proofs
*(Atomic notes, problem set proofs, and project notes)*

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- Crafting Interpreters Part II (jlox); Ball, Writing a Compiler in Go.
