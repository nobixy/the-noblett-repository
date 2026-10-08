---
block_id: "Block 33"
title: "Interpreters and Language Runtimes"
category: "core"
term: "Year 2 January Intensive"
status: not-started
prerequisites:
  - "Software Construction"
  - "Computer Systems"
hours_estimate: 130
hours_actual: 0
primary_resource: "Ball, Writing an Interpreter in Go & Nystrom, Crafting Interpreters (Part III)"
milestone: "clox bytecode VM with garbage collection passes book's full test suite"
date_started: ""
date_completed: ""
tier: "Tier 1 - Core"
---

# Block 33 — Interpreters and Language Runtimes

[[00 - Dashboard|Dashboard]] / [[Checklist|Checklist]] / [[Languages Index|Languages Index]]

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
- [[Software Construction]]
- [[Computer Systems]]


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
- **Topic Hub:** [[Languages Index|Languages Index]] | [[Checklist|Master Checklist]]
- **Sequential Flow:** [[Computer Security|← Computer Security]] | [[00 - Dashboard|Dashboard]] | [[Theory of Computation|Theory of Computation →]]
