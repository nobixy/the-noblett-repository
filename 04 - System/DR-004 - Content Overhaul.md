---
title: "DR-004: Content Overhaul"
type: decision-record
status: superseded
superseded_by: [DR-010, DR-011]
date: 2026-10-09
accepted: 2026-10-09
tags:
  - adr
  - decision-record
---

# DR-004: Content Overhaul

> [!WARNING] Superseded
> Superseded by [[DR-010 - Project-First Original Curriculum|DR-010]] and [[DR-011 - Sectioned Curriculum and Frontmatter Schema|DR-011]]. Kept as a historical record: its dates, hours, weeks, phases and links into `99 - Archive/` describe the v1 plan and are not current instructions.

*Uses the [[Decision Record]] template. Follows [[DR-003 - One Path Restructure|DR-003]]. Accepted and applied 2026-10-09. Checkpoint before the overhaul: git commit `c0451b3`.*

## Context
The goal: the strongest EECS education a part-time (~20 h/wk), budget-constrained self-learner can get, using the best free courses available in October 2026. Every block, elective and track was reviewed against MIT's current EECS degree charts (6-3 Computer Science and Engineering; 6-5 Electrical Engineering with Computing, which requires 6.1910, 6.2000 circuits and 6.3000 signals), Berkeley/Stanford/CMU courses, OSSU, teachyourselfcs.com and csdiy.wiki. Every URL named in the notes was checked on 2026-10-09.

What the review found:
1. **The EE half was optional.** Circuits, signals and differential equations sat outside the plan as "bridges", so the program was really CS with physics, not EECS.
2. **No machine learning or deep learning in the core.** ML was an optional elective; deep learning only lived in a track.
3. **GPUs and parallelism were optional** even though every fast system is now parallel.
4. **Redundancy:** SICP (Block 5) repeated CS61A (which is SICP in Python) and Block 12 (two interpreters).
5. **Tracks named no real courses.** Most tracks were module plans with invented course titles ("…Equivalent"); nothing to enroll in, no assignments, no autograder.
6. **Tracks outside EECS or overlapping:** Computational Biology and Advanced Pure Mathematics are other degrees; Rust, HIL/digital twins and formal verification overlapped Tracks 2, 9 and 5.
7. **Stale or wrong pointers:** "8.02SC" doesn't exist on OCW; Math for CS pointed at the 2015 offering; Missing Semester has a new 2026 edition; the 6.1040 root URL now 404s.

## Decision
**Added (3):**
- **Block 22a — Machine Learning** (Year 3; MIT 6.390 notes + MITx 6.036 Open Learning Library autograder + CS229 notes; 150 h).
- **Block 25a — Deep Learning** (Year 4; Karpathy *Zero to Hero*, CS231n assignments, Prince *UDL*; 160 h).
- **Track 11 — Signal Processing, Communications and Electromagnetics** (MIT 6.341, 6.011, 6.02, 6.450, 6.013, PySDR).

**Promoted to core (4):** Blocks 4a (Differential Equations), 8a (Circuits; now pointed at MIT 6.2000's current site + 6.002 OCW + MITx 6.002.1x), 15a (Signals; MIT 6.3000 current site + 6.003 OCW), and E4 Parallel Computing → **Block 23a** (Stanford CS149 public assignments incl. CUDA).

**Merged (5):** SICP → Block 1 (chapters 1–3 optional reading); E2 Intro ML → Block 22a; Rust (Track 8) → Track 2; HIL/Digital Twins (Track 9) → Track 9 Robotics; Formal Verification (Track 13) → Track 5.

**Cut (2):** Track 12 Computational Biology, Track 14 Advanced Pure Mathematics (outside EECS).

**Made optional (1):** Block 18 Real Analysis (neither MIT 6-3 nor 6-5 requires it; still available).

**Upgraded (26):** every remaining track (1–9) now has a 🌐 Real Courses section naming current free courses (CS229, CMU DLSys, CS336, MIT 6.172, CMU 15-721, Boneh–Shoup, MIT 6.5660, pwn.college, CS184, PBRT, Software Foundations, Cornell CS 6120, ETH architecture, MIT 6.205, MIT 6.5940, Modern Robotics, Underactuated, Quantum Country, IBM Quantum Learning, Stim) and `primary_resource` names them. Core upgrades: CS50x 2026 + `check50` (P4); Missing Semester 2026 (P5); 3Blue1Brown companions (Blocks 2, 11); Physics hours 100 → 130 each (Blocks 3, 8) and real 8.02 OCW links; MIT 6.1200J 2024 (Block 10); CSES autograded problems (Block 13); HDLBits + MIT 6.191 (Block 14); Software Construction trimmed and pointed at 6.102 readings + 6.005 psets (Block 17); CMU 15-445 public Gradescope (Block 21); MIT 18.404J Sipser videos (Block 24); MIT 6.5660 + pwn.college (E2 Security).

**Kept (24):** Phase −1, P1–P3, Nand2Tetris, C Fluency, Multivariable Calculus, CS:APP, Linear Algebra, Interpreters, Probability, xv6, CS144, Algorithms II, Statistics, 6.5840, Convex Optimization, Cryptopals, Capstone, Information Theory, E1 AI (CS188 autograders), Track 10 Full-Stack. Each now carries a 🔎 Verified Resources section with checked links, autograders, and a free alternative for anything paid (💲).

**Renumbering:** E3 → E2 (Security); E4 → Block 23a; Track 10 → 8 (Quantum), 11 → 9 (Robotics), 15 → 10 (Full-Stack); new Track 11. Every link, prerequisite and Sequential Flow was rewritten; cut and merged notes keep their full text in `99 - Archive/Cut Content/` (named `Cut - …`).

## Status
**Accepted**: 2026-10-09. **Superseded** by DR-010 and DR-011.

## Consequences
**Hours (planned, non-optional, Start Here query):** 5,125 → **5,805** (+150 4a, +160 8a, +160 15a, +150 22a, +160 25a, +140 23a, +60 physics; −120 SICP, −180 Real Analysis). Plus two tracks (800) = 6,605; plus habits (≈1,000–1,500, DR-001) = **≈7,600–8,100 h**, inside the ~8-year cap at 20 h/wk (≈8,320 h). The DR-001 cut order still applies if hours drop (Physics → Statistics → second track).

**Easier:** the program now covers the MIT 6-5 EE core and the modern CS core (ML, deep learning, parallel/GPU); every block and track points at a real course with an autograder, test suite or exam where one exists; everything named is free or has a free alternative.

**Harder / costs:** stage loads are uneven (Year 2 ≈ 1,390 h, Year 1 ≈ 1,300 h of blocks), so a "Year" is a stage, not a calendar year. The day-job weekly schedule in `Calendar.md` / how-i-study was **not** changed. Old numbers (Track 8–15, E3/E4, Block 5) in `99 - Archive` and DR-001–003 refer to the pre-DR-004 numbering. Paid items flagged 💲: CUDA GPU (free hosted GPU tier works), breadboard kit, FPGA board, SDR dongle, a few textbooks.

**Undo:** `git checkout -- . && git clean -fd` before committing, or revert the overhaul commit after.
