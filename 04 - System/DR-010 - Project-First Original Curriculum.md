---
title: "DR-010: Project-First Original Curriculum"
type: decision-record
status: accepted
amended_by: [DR-011]
date: 2026-10-10
accepted: 2026-10-10
tags:
  - adr
  - decision-record
---

# DR-010: Project-First Original Curriculum

> [!NOTE] Amended by [[DR-011 - Sectioned Curriculum and Frontmatter Schema|DR-011]]
> DR-011 removed all time estimates (the hours, "Week 1" and pace figures below are historical), added the frontmatter schema, and settled the ordering rules. The rest of this record still stands.

*Uses the [[Decision Record]] template. Follows [[DR-009 - Learning Method Deep Dives|DR-009]]. Accepted and applied 2026-10-10. Checkpoint before this change: git commit `bf48336` (the Obsidian auto-backup commits after it already contain parts of this change).*

## Context

The v1 plan (DR-001 to DR-009) was built around famous courses: CS61A, Nand2Tetris, CS144, MIT 6.S081/xv6, CMU 15-213 and 15-445, CS50. Progress was meant to be measured by those courses' projects and autograders. Three problems:

1. **Foundations weren't truly foundational.** BM and BW started from Lockhart's *Arithmetic* and Huddleston & Pullum. For an adult who describes their English as "super bad (can barely spell)" and is restarting math from arithmetic, the bottom rungs were missing: spelling, parts of speech, the simple sentence; place value, the four operations, fractions.
2. **The builds were other people's.** Project-first learning needs projects designed for a self-learner on their own machine, with clear milestones, tests the learner writes, and success criteria they can check alone — not course starter code and autograders.
3. **The study methods were described, but not wired in.** how-i-study.md explained the methods well, but most blocks didn't say *where* in the work to use them.

The journal (2026-09-25 to 2026-10-06) also shows a pattern of setup without starting: the plan was too big to begin.

## Decision

1. **Rebuild the curriculum** as numbered module folders (`00-foundations/` … `13-capstone/`), each with `overview.md`, `labs/`, `projects/<name>/spec.md`, and `resources.md`.
2. **Foundations from absolute basics:**
   - **English E01–E10:** spelling baseline and high-frequency words → spelling rules → word parts and confusables → parts of speech → the simple sentence and verbs → punctuation → joining ideas → paragraphs and clarity → technical description and instructions → argument and design docs. Six projects (Spelling Engine, Machine Manual, Terminal Field Notes, Explain-a-System, Bug Report Gauntlet, First Design Doc).
   - **Math M01–M11:** place value and bases → addition/subtraction → multiplication/division and modulo → factors and primes → fractions → decimals, percents, ratios → negatives, exponents, order of operations → algebra → linear functions and systems → geometry → functions, exponentials, logarithms. Seven projects. Every stage has a diagnostic, worked examples with subgoal labels, mixed practice with answers (checked in Python), why-ladders, and a self-check.
3. **An early CS taste module (01):** Python labs plus four small, real systems — Nib (a tiny computer), Relay (talking programs with reliability over a lossy link), Burrow Jr. (a mini shell), Pagelet (a page viewer) — each a preview of a full-size later build.
4. **Original projects only.** Every project spec is an original design: Kestrel ISA, datapath, and the Ember compiler instead of Nand2Tetris; Courier (CP/1) instead of CS144's labs; Seedling (RISC-V, from scratch) instead of xv6 labs; Heapsmith, Burrow, Crate instead of 15-213 labs; Stratum instead of BusTub; Glimpse instead of a chapter-by-chapter browser book. Courses appear only in `resources.md` as second explanations, never as assignments.
5. **Study methods as exact routines:** [study-protocols.md](../study-protocols.md) defines R (retrieval), F (Feynman), W (why-ladder), S (subgoal labels), I (interleave and space), C (Franklin copywork), D (diffuse break), T (teach-back and write-up). Every stage and project uses them by code, and every project milestone ends with a Milestone Checkpoint (R + F + W).
6. **Communication in every project,** sized to the English stage: spoken demos and short notes early; lab reports from Module 03–04; full design docs from Module 05 (whose first project, Copydiff, is built from the design doc written in E10).
7. **New templates:** Milestone Checkpoint, Design Doc, Lab Report, Demo Script.
8. **Archive v1:** `01 - Curriculum/`, Projects Ladder, and Projects Hub moved to `99 - Archive/v1 - Course-Based Curriculum/` (not deleted; links still resolve). Its advanced tracks and the drone-swarm capstone remain available after the core, by a future Decision Record.
9. **Start Here rewritten** as a dashboard: a concrete Week 1 and a checklist of every stage, lab, and project. **README rewritten.** how-i-study.md §2a, §2b, §3, §4, §6 updated.

## Status

Accepted.

## Consequences

- **Easier:** starting (Week 1 is seven small, specific days); knowing what to do next; knowing when something is done (every item has a "done when" list and a rubric); connecting early work to later systems (every spec has a Connections section).
- **Harder:** no external autograders — correctness rests on the tests I write, including differential tests, crash tests, and fuzzing, which each spec requires. No course certificates.
- **Scope:** the core is about 2,900 hours (≈ 3 years at 20 h/week), down from the v1 program's ≈ 7,800–8,300 h, because physics, several advanced theory blocks, and the specialisation tracks moved to "after the core."
- **Not verified by execution:** the RISC-V bare-metal code in Module 08 Lab 03 was written from the specifications but not run (the toolchain wasn't installed when this DR was written). Run it early and fix anything that doesn't boot.
- **Review date:** at the next how-i-study revision (2027-03-25), check: are the foundations' paces realistic? Are the deliverable sizes right for the English stage reached?
