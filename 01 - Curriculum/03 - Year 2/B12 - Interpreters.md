---
block_id: "Block 12"
title: "Interpreters and Language Runtimes"
category: "core"
subject: "Computer Science"
term: "Year 2 January Intensive"
status: not-started
prerequisites:
  - "B06 - C Fluency"
  - "B09 - Computer Systems"
hours_estimate: 130
hours_actual: 0
primary_resource: "Ball, Writing an Interpreter in Go & Nystrom, Crafting Interpreters (Part III)"
milestone: "clox bytecode VM with garbage collection passes book's full test suite"
date_started: ""
date_completed: ""
tier: "Tier 1 - Core"
job_ready: 4 # job-ready path, phase 4 (DR-003)
aliases: ["Interpreters"]
---

# Block 12 — Interpreters and Language Runtimes

[[00 - Start Here|Start Here]] / [[00 - Start Here#The Path|The Path]] / [[Languages Index|Languages Index]]

> [!INFO] Block Overview
> - **Term / Position:** Year 2 January Intensive
> - **Estimated Hours:** ~130 hrs
> - **Status:** `not-started`
> - **Primary Resource:** Ball, Writing an Interpreter in Go & Nystrom, Crafting Interpreters (Part III)
> - **Key Milestone:** clox bytecode VM with garbage collection passes book's full test suite

---

## 📚 Curriculum Tier: Tier 1 - Core
> **Tier 1 - Core**: Must complete before advancing.

## 🎯 Why This Block Matters
Build two complete programming language implementations — one tree-walking interpreter, one high-performance bytecode VM.

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[B06 - C Fluency|C Fluency]]
- [[B09 - Computer Systems|Computer Systems]]


## 📖 Primary Syllabus & Core Content
- [ ] Thorsten Ball, Writing an Interpreter in Go: Lexing, Pratt parsing, AST evaluation, environment, closures
- [ ] Bob Nystrom, Crafting Interpreters Part III (C VM): Chunks of bytecode, virtual machine loop, value representation, hash tables, stack-based bytecode evaluation, closures, garbage collection (mark-sweep)

---

## 🛠️ Build Requirement
1. Build Monkey in Go (tree-walker). 2. Build `clox` in C (bytecode compiler and VM with GC). Bonus: Ball's Writing a Compiler in Go.

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> `clox` passes the book's full test suite cleanly.

---

## 🔎 Verified Resources (DR-004, checked 2026-10-09)
**Verdict:** KEEP.
- *Crafting Interpreters* (free online): craftinginterpreters.com — its test suite is the autograder. 💲 Ball's Go books (interpreterbook.com); free alternative: Crafting Interpreters Part II (jlox).

---

## 📝 Study Notes, Psets & Proofs

*Your atomic notes, problem-set proofs, and build notes go here — written by you, from a blank page.*

> [!TIP]- Check your work (only after your own blank-sheet attempt)
> Ball's tests for Monkey; the `test/` suite in the Crafting Interpreters repo for clox (*Done when*).

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- Crafting Interpreters Part II (jlox); Ball, Writing a Compiler in Go.

---

## ➡️ Next Steps
- **Topic Hub:** [[Languages Index|Languages Index]] | [[00 - Start Here#The Path|The Path]]
- **Sequential Flow:** [[B11 - Linear Algebra|← Linear Algebra]] | [[00 - Start Here|Start Here]] | [[B13 - Algorithms I|Algorithms I →]]
