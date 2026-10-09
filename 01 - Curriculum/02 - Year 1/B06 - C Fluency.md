---
block_id: "Block 6"
title: "C Fluency & Low-Level Problem Solving"
category: "core"
subject: "Computer Science"
term: "Year 1 Spring"
status: not-started
prerequisites:
  - "B01 - CS61A"
hours_estimate: 110
hours_actual: 0
primary_resource: "Kernighan & Ritchie (K&R) & Zingaro, Algorithmic Thinking (Ch 1-5)"
milestone: "Valgrind-clean builds & whiteboard explanation of pointer arithmetic, struct padding, stack frame"
date_started: ""
date_completed: ""
tier: "Tier 1 - Core"
job_ready: 3 # job-ready path, phase 3 (DR-003)
aliases: ["C Fluency"]
---

# Block 6 — C Fluency & Low-Level Problem Solving

[[00 - Start Here|Start Here]] / [[00 - Start Here#The Path|The Path]] / [[Languages Index|Languages Index]]

> [!INFO] Block Overview
> - **Term / Position:** Year 1 Spring
> - **Estimated Hours:** ~110 hrs
> - **Status:** `not-started`
> - **Primary Resource:** Kernighan & Ritchie (K&R) & Zingaro, Algorithmic Thinking (Ch 1-5)
> - **Key Milestone:** Valgrind-clean builds & whiteboard explanation of pointer arithmetic, struct padding, stack frame

---

## 📚 Curriculum Tier: Tier 1 - Core
> **Tier 1 - Core**: Must complete before advancing.

## 🎯 Why This Block Matters
Block 9 (CS:APP) assumes real C. Get it now before hitting hardware and systems.

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[B01 - CS61A|CS61A]]


## 📖 Primary Syllabus & Core Content
- [ ] K&R The C Programming Language: Every single exercise
- [ ] Zingaro, Algorithmic Thinking, 2e: Chapters 1–5 (Hash tables, memoization, binary search, trees in pure C)
- [ ] Brian Ward, How Linux Works, 3e: Chapters 8–17 in the background
- [ ] Tooling: gcc/clang flags (-Wall -Wextra -Werror -O2 -g), GDB, Valgrind

---

## 🛠️ Build Requirement
Build from scratch in C: a dynamic array (vector), an arena-based string library, a hash table with collision resolution, and a minimal `ls` clone. Compile each with -O2, inspect `objdump -d`, and annotate what the compiler did.

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> Every build is completely valgrind-clean (zero leaks, zero errors) and you can explain pointer arithmetic, struct padding, and a stack frame on a whiteboard.

---

## 📝 Study Notes, Psets & Proofs

*Your atomic notes, problem-set proofs, and build notes go here — written by you, from a blank page.*

> [!TIP]- Check your work (only after your own blank-sheet attempt)
> `valgrind` and your own tests. For K&R exercises, Tondo & Gimpel's *The C Answer Book* has worked solutions.

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- Modern C (Gustedt); CS50 C weeks; Effective C (Seacord); Programming from the Ground Up.

---

## ➡️ Next Steps
- **Topic Hub:** [[Languages Index|Languages Index]] | [[00 - Start Here#The Path|The Path]]
- **Sequential Flow:** [[B05 - SICP|← SICP]] | [[00 - Start Here|Start Here]] | [[B07 - Multivariable Calculus|Multivariable Calculus →]]
