---
title: "DR-008: Project-First Start and Projects Ladder"
type: decision-record
status: accepted
date: 2026-10-10
accepted: 2026-10-10
tags:
  - adr
  - decision-record
---

# DR-008: Project-First Start and Projects Ladder

*Uses the [[Decision Record]] template. Follows [[DR-007 - Repo Cleanup|DR-007]]. Accepted and applied 2026-10-10. Checkpoint before this change: git commit `f6f26ef`.*

## Context
"Make more projects, I learn best by doing projects. Then make it easier for me to start right now: it just has me reading two books out the gate and I still find that boring. So until I build that muscle, feed in some fun stuff along the way."

Phase −1 opened with Lockhart's *Arithmetic* and Huddleston & Pullum / Williams, and four Year 1 blocks (2, 3, 7, 8) had problem sets but no build. The hour cap leaves ~15 h of margin (DR-006), so nothing could be added, only swapped.

## Decision
- **Day 1 is a build.** A [[00 - Start Here#🚀 Week 1 — Do This Today|Week 1: do this today]] checklist at the top of Start Here: Scratch game, Wokwi Pico blink, Desmos art, Bandit, nandgame, a weekly review, and the daily code streak.
- **Starter Sprint (Weeks 1–12):** one fun build a week, each with a done-when line, counted inside B0, BM, BW, P1, P2, P4 and P5 ([[Projects Ladder]]). All free; three optional paid extras are marked 💲.
- **Books become companions:**
  - Lockhart: 10–15 min/day from Week 5, finished by the end of P3.
  - Williams *Style*: from Week 5.
  - Huddleston & Pullum: lookups only.
  - *A Mind for Numbers*: alongside the course.
  - *Make It Stick* and Adler Part 2: moved to Year 1 Companion Reading.
- **Reading Ramp** ([[how-i-study#2a. Reading Ramp|how-i-study §2a]]), stated explicitly:
  - Weeks 1–4: 0–15 min/day, optional.
  - Weeks 5–8: 15–20 min.
  - Weeks 9–12: 20–30 min.
  - Phase 0: up to 45 min.
  - Year 1 on: what the block assigns, build first.
  - If reading feels like a wall two days running, drop back one row for a week.
- **Every block has a build:**
  - New project builds in [[B02 - Calculus I|Block 2]] (calculus toy lab), [[B03 - Physics I|Block 3]] (2D physics sandbox + phyphox), [[B07 - Multivariable Calculus|Block 7]] (3D field explorer) and [[B08 - Physics II|Block 8]] (E&M simulator + electromagnet).
  - [[P3 - Math Prerequisites|P3]] gets a truth-table toolkit; [[P1 - Learning How to Learn|P1]] a flashcard app; [[P2 - Reading, Thinking, and Writing|P2]] a build write-up in place of the book synopsis.
  - Every other block already had one.
  - The [[Block Note Template]] now requires a Project Build section.
- **Weekly mini-build** (≤2 h, Saturday) for the whole program, with ideas per year ([[how-i-study#2b. Weekly Mini-Build|how-i-study §2b]]).
- **[[Projects Ladder]]:** one note linking every build in order: the Starter Sprint, every block on The Path with its done-when line, the track capstones, and Block 30.

Checked 2026-10-10:
- Raspberry Pi Pico 2: $5 (Pico 2 W: $7).
- The Wokwi free plan simulates the Pico in MicroPython; projects on the free plan are public.
- phyphox is a free app from RWTH Aachen.
- Steam prices from DR-006.

## Consequences
**Hours:** unchanged, **6,005 h** core. Every build replaces reading, recitation write-ups or practice sets inside its block. The total stays ≈7,805–8,305 h with ~15 h of margin.

**Flags:**
- B0, BM and BW mastery still needs the Khan unit tests, 10 days of copywork, and the explanations.
- Lockhart now has to be finished by the end of P3 instead of in BM.
- [[Calendar]] still says the current focus is reading BM and BW. It's your file, so it wasn't edited: swap in the Week 1 checklist if you want.
- The day-job weekly schedule was not changed.

**Undo:** `git checkout -- . && git clean -fd` (back to `f6f26ef`).
