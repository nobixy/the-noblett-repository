---
title: "LM05: Interleaving"
type: learning-method
method_id: LM05
evidence: "Moderate"
project_hours: 3
counts_toward: "BM"
---

# LM05 — Interleaving
*Deep dive + project ([[DR-009 - Learning Method Deep Dives|DR-009]]). Hub: [[LM00 - Learning Methods Hub|Learning Methods]] · Method in practice: [[how-i-study]] §1*

> [!NOTE] Evidence: **Moderate**

## In plain words
Mix different kinds of problems in one session instead of doing 20 of the same kind in a row. You have to work out which method each problem needs.

## The evidence, honestly
Rohrer & Taylor (2007): students who practised math problem types mixed together scored far higher on a test a week later than students who practised them blocked by type, even though mixed practice felt harder and went worse during practice.
Kornell & Bjork (2008) found the same for learning to tell painters' styles apart.
Dunlosky et al. (2013): **moderate utility**. It helps most when the problem types look alike.

## Using it in EECS
- Mix Big-O questions, recursion traces, and "which data structure?" questions.
- In circuits, mix series, parallel and Thévenin problems.
- NeetCode's pattern lists are blocked by design, so once you know a few patterns, shuffle them.

## Common mistakes
- Interleaving topics you haven't learned yet. Learn each type once, then mix.
- Judging it by how practice feels. Judge it by the test a week later.

## 🔨 Project: Shuffle Drill: mixed-problem generator
In Scratch, or in Python with `random` and `input`, build a generator for 5 problem types: fraction addition, fraction division, negative multiplication, base conversion and prime factors. It mixes them in random order, checks your answers and reports accuracy per type.
- **Done when:** a 50-problem mixed session runs, it reports accuracy by type, and you did 3 sessions on different days.
- **Time:** about 3 h, counted inside [[BM - Bedrock Mathematics|BM]]'s existing hours (the Shuffle Drill replaces the Khan practice sets beyond the unit tests (the unit tests stay); the why-ladders for invert-and-multiply and negative × negative count as Build Requirement 2's Feynman explanations).
- **Level / when:** Beginner Python or Scratch. Week 4 (it extends the base-converter build); the Python version can wait until Week 10.

## Sources
- Rohrer & Taylor (2007), "The shuffling of mathematics problems improves learning", *Instructional Science* 35(6), 481–498.
- Kornell & Bjork (2008), "Learning concepts and categories: is spacing the 'enemy of induction'?", *Psychological Science* 19(6).
- Dunlosky et al. (2013).
