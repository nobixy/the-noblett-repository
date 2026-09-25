---
block_id: "Block 6"
title: "C Fluency & Low-Level Problem Solving"
term: "Year 1 Spring"
status: not-started
hours_estimate: 110
hours_actual: 0
primary_resource: "Kernighan & Ritchie (K&R) & Zingaro, Algorithmic Thinking (Ch 1-5)"
milestone: "Valgrind-clean builds & whiteboard explanation of pointer arithmetic, struct padding, stack frame"
date_started: ""
date_completed: ""
---

# Block 6 — C Fluency & Low-Level Problem Solving

> [!INFO] Block Overview
> - **Term / Position:** Year 1 Spring
> - **Estimated Hours:** ~110 hrs
> - **Status:** `not-started`
> - **Primary Resource:** Kernighan & Ritchie (K&R) & Zingaro, Algorithmic Thinking (Ch 1-5)
> - **Key Milestone:** Valgrind-clean builds & whiteboard explanation of pointer arithmetic, struct padding, stack frame

---

## 🎯 Why This Block Matters
Block 9 (CS:APP) assumes real C. Get it now before hitting hardware and systems.

---

## 📖 Primary Syllabus & Core Content
- [ ] K&R The C Programming Language: Every single exercise
- [ ] Zingaro, Algorithmic Thinking, 2e: Chapters 1–5 (Hash tables, memoization, binary search, trees in pure C)
- [ ] Brian Ward, How Linux Works, 3e: Chapters 8–17 in the background
- [ ] Tooling: gcc/clang flags (-Wall -Wextra -Werror -O2 -g), GDB, Valgrind

---

## 🛠️ Build Requirement
Build from scratch in C: a dynamic array (vector), an arena-based string library, a hash table with collision resolution, and a minimal `ls` clone. Compile each with -O2, inspect `objdump -d`, and annotate what the compiler did.

---

## 🏁 Done When
> [!IMPORTANT]
> Every build is completely valgrind-clean (zero leaks, zero errors) and you can explain pointer arithmetic, struct padding, and a stack frame on a whiteboard.

---

## 📝 Study Notes, Psets & Proofs
*(Atomic notes, problem set proofs, and project notes)*

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- Modern C (Gustedt); CS50 C weeks; Effective C (Seacord); Programming from the Ground Up.
