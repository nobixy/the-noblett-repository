---
block_id: "P4"
stage: "01 - Phase 0 Prerequisites"
title: "Programming On-Ramp"
category: "core"
subject: "Computer Science"
term: "Phase 0 (0–5 mo)"
status: not-started
prerequisites: []
hours_estimate: 145
hours_actual: 0
primary_resource: "Harvard CS50x 2026"
milestone: "Valgrind-clean 300-line C program, Hash Table & BST from scratch"
date_started: ""
date_completed: ""
tier: "Tier 2 - Support"
job_ready: 1 # job-ready path, phase 1 (DR-003)
aliases: ["Programming On-Ramp"]
---

# P4 — Programming On-Ramp

> [!INFO] Block Overview
> - **Term / Position:** Phase 0
> - **Estimated Hours:** ~145 hrs
> - **Status:** `not-started`
> - **Primary Course:** Harvard CS50x (`cs50.harvard.edu/x`) & John Guttag, *Introduction to Computation and Programming Using Python* (MIT 6.100A/B)

---

## 📚 Curriculum Tier: Tier 2 - Support
> **Tier 2 - Support**: Strongly recommended for full understanding.

## 🎯 Why This Block Matters
Before diving into Berkeley CS61A, you need fundamental operational competence with memory, pointers, data structures, and debugging.

---

## 🧪 Cold Exit Test (Can Skip Course if Passed)
*Test:*
- [ ] Write a 300-line C program with manual memory management that is 100% `valgrind`-clean.
- [ ] Implement a hash table and a binary search tree (BST) from scratch with complete insertion, search, and free routines.
*(Can pass → skip to P5!)*

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- *None. This is a foundational block.*


## 📖 Primary Syllabus
- [ ] Harvard CS50x (2026 edition):
  - [ ] Week 0: Scratch
  - [ ] Week 1: C
  - [ ] Week 2: Arrays
  - [ ] Week 3: Algorithms
  - [ ] Week 4: Memory (Pointers, Heap vs Stack)
  - [ ] Week 5: Data Structures (Linked lists, Tries, Hash tables)
  - [ ] Week 6: Python
  - [ ] Week 7: SQL
  - [ ] Artificial Intelligence (lecture between Weeks 7 and 8)
  - [ ] Week 8: HTML, CSS, JavaScript
  - [ ] Week 9: Flask
  - [ ] Week 10: The End (final project)
  - [ ] Every problem set and the final project. (The 2026 edition has no separate labs.)

---

## 🛠️ Build Requirement
Implement a 300-line modular data structure library in `c` (hash table with separate chaining and a self-balancing binary search tree), compiled with `gcc` / `clang` using `-Wall -Wextra -Werror`, debugged with `gdb`, and rigorously verified with 0 memory leaks and 0 errors under `valgrind`.

---

## 🧠 Learning-Method Projects (DR-009, 2026-10-10)
- [[LM10 - Worked Examples and Subgoal Labeling|LM10 Worked Examples and Subgoal Labeling]]: Subgoal Annotator (~3 h)
- **Hours:** inside this block's existing hours; replaces rewatching CS50 lectures; you annotate the lecture source code instead.

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> The cold exit test passes cleanly under `valgrind`.

---

## 🎮 NeetCode Pro Sprint, Daily Code Streak and Fun Builds (DR-006, 2026-10-09)
> [!IMPORTANT] Your NeetCode Pro access ends **Feb 6, 2027**
> Use it now, in Phase −1/0. +20 h on this block (offset by trimming P2 and Block 17).

**Before Feb 6, 2027 (≈17 weeks; about 20 min a day, plus one longer session a week):**
1. *Python for Beginners* (NeetCode Pro, interactive). Do it before CS50x Week 6 so Python feels familiar.
2. *Python for Coding Interviews* (NeetCode Pro).
3. *Algorithms & Data Structures for Beginners* (NeetCode Pro, ≈25 h): lessons Arrays → Linked Lists → Recursion → Sorting → Binary Search → Trees → Hashing at least. This previews Block 13.
4. **NeetCode 150** (neetcode.io/roadmap), easy problems in Arrays & Hashing, Two Pointers, Stack, Binary Search, Linked List, as your **🎮 Daily Code Streak**: one problem a day, logged in [[log]].
- Download nothing you're not allowed to. Keep your own notes and solutions in your repo so they outlive the subscription.

**After Feb 6, 2027 (free fallback):** the neetcode.io roadmap and practice lists, NeetCode's free YouTube solutions (youtube.com/@NeetCode), and LeetCode's free problem set. Keep the streak going with Exercism (exercism.org, free, mentored), Codewars (codewars.com) or Project Euler.

**Advent of Code (Dec 1–25, 2026)** (adventofcode.com, free): do the puzzles in Python as the streak during December.

**Coursera Plus alternatives** (included as of 2026-10-09): *Programming for Everybody (Getting Started with Python)* and *Python Data Structures* (University of Michigan). Use them as the failover if CS50x Week 1 (C) is a wall: do them first, then return to CS50x.

**Fun build:** make your **CS50x final project a small game**. Options:
- **LÖVE** (love2d.org, free, Lua)
- **Godot** (godotengine.org, free)
- **p5.js** with The Coding Train videos (p5js.org, thecodingtrain.com, free)
- **PICO-8** 💲 $14.99 (lexaloffle.com)

Optional after P4: CS50's *Introduction to Game Development* (cs50.harvard.edu/games, free) or *Introduction to Game Design* (Coursera Plus).

---

## 🔎 Verified Resources (DR-004, checked 2026-10-09)
**Verdict:** UPGRADE. Pointed at the current offering and its autograder.
- **CS50x 2026** (free, certificate free): cs50.harvard.edu/x/2026/. Problem sets are autograded with `check50` and submitted with `submit50` — use them as the *Check your work* step.

---

## 📝 Study Notes, Psets & Proofs

*Your atomic notes, problem-set proofs, and build notes go here — written by you, from a blank page.*

> [!TIP]- Check your work (only after your own blank-sheet attempt)
> CS50's `check50` autograder on every problem set, then `valgrind` for the exit test.

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- King, *C Programming: A Modern Approach, 2nd ed.*
- University of Helsinki, *Python Programming MOOC*

---

## ➡️ Next Steps
*Why does the next subject come next?*
- Next block: [[P5 - Tooling|P5 — Tooling]]

- **Sequential Flow:** [[P3 - Math Prerequisites|← Math Prerequisites]] | [[00 - Start Here|Start Here]] | [[P5 - Tooling|Tooling →]]
