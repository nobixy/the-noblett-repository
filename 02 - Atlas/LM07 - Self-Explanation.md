---
title: "LM07: Self-Explanation"
type: learning-method
method_id: LM07
evidence: "Moderate to strong"
---

# LM07 — Self-Explanation
*Deep dive + project ([[DR-009 - Learning Method Deep Dives|DR-009]]). Hub: [[LM00 - Learning Methods Hub|Learning Methods]] · Method in practice: [[how-i-study]] §1*

> [!NOTE] Evidence: **Moderate to strong**

## In plain words
While working through a solution or a worked example, explain to yourself, step by step, why each step is there.

## The evidence, honestly
Chi et al. (1989): the physics students who learned most from worked examples were the ones who explained each step to themselves.
Bisra et al. (2018), a meta-analysis of 64 reports: prompting learners to self-explain gave g ≈ 0.55.
Dunlosky et al. (2013): **moderate utility** (it costs time).

## Using it in EECS
- Before you run code, write a comment on each line saying why it's there.
- Talk aloud while debugging (rubber-duck debugging is the same idea).
- When reading a proof, write the justification for each line in the margin.

## Common mistakes
- Paraphrasing what a line does ("increments i") instead of why it's there ("move past the element we just placed").

## 🔨 Project: Narrated Solutions
For 5 easy practice problems (NeetCode, or Module 05's problem practice), write a why-comment on every line before running the code. Record one solve talking aloud (phone audio).
- **Done when:** 5 commented solutions are in your repo, plus a short note on which bugs the explanations caught before running.
- **Level:** Beginner Python.
- **Fits with:** No separate protocol code; it overlaps with **S** (subgoal labels) and **W** (why-ladders).

## Sources
- Chi, Bassok, Lewis, Reimann & Glaser (1989), "Self-explanations: how students study and use examples in learning to solve problems", *Cognitive Science* 13(2).
- Bisra et al. (2018), *Educational Psychology Review* 30.
