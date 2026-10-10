---
title: "LM10: Worked Examples and Subgoal Labeling"
type: learning-method
method_id: LM10
evidence: "Strong for beginners"
project_hours: 3
counts_toward: "P4"
---

# LM10 — Worked Examples and Subgoal Labeling
*Deep dive + project ([[DR-009 - Learning Method Deep Dives|DR-009]]). Hub: [[LM00 - Learning Methods Hub|Learning Methods]] · Method in practice: [[how-i-study]] §1*

> [!NOTE] Evidence: **Strong for beginners**

## In plain words
When you're new to a topic, study fully worked solutions before solving problems alone. Label each chunk of the solution with its purpose (the subgoal), then solve a similar problem using only the labels.

## The evidence, honestly
Sweller & Cooper (1985): algebra beginners who studied worked examples learned faster and made fewer errors than beginners who solved the same problems unaided.
The benefit fades and can reverse as you gain skill (the expertise reversal effect, Kalyuga et al. 2003). Switch to problem solving once the examples feel easy.
Subgoal labels: Catrambone (1998); in programming, Margulieux, Guzdial & Catrambone (2012) found subgoal-labeled examples improved novices' performance on new tasks.

## Using it in EECS
- CS50 lecture code, Khan worked solutions and CLRS pseudocode are worked examples.
- Add labels like "read input", "guard the edge case", "update the invariant".

## Common mistakes
- Reading the example passively.
- Studying examples long after you no longer need them.
- Labels that just restate the code.

## 🔨 Project: Subgoal Annotator
Add `# SUBGOAL:` comments to 3 worked examples (CS50 lecture source or your own Week builds). Write a Python script that prints the subgoal outline of any .py or .c file. Then solve a similar problem using only the outline.
- **Done when:** the script outlines 3 files, and you solved 3 similar problems without looking at the original examples.
- **Time:** about 3 h, counted inside [[P4 - Programming On-Ramp|P4]]'s existing hours (replaces rewatching CS50 lectures; you annotate the lecture source code instead).
- **Level / when:** Beginner Python (file reading, string matching). In P4, with CS50.

## Sources
- Sweller & Cooper (1985), "The use of worked examples as a substitute for problem solving in learning algebra", *Cognition and Instruction* 2(1), 59–89.
- Kalyuga, Ayres, Chandler & Sweller (2003), "The expertise reversal effect", *Educational Psychologist* 38(1).
- Margulieux, Guzdial & Catrambone (2012), "Subgoal-labeled instructional material improves performance and transfer in learning to develop mobile applications", ICER '12.
