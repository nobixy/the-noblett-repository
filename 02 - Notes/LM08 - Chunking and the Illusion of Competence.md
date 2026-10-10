---
title: "LM08: Chunking and the Illusion of Competence"
type: learning-method
method_id: LM08
evidence: "Strong (chunking); strong (illusions of competence)"
project_hours: 3
counts_toward: "BM"
---

# LM08 — Chunking and the Illusion of Competence
*Deep dive + project ([[DR-009 - Learning Method Deep Dives|DR-009]]). Hub: [[LM00 - Learning Methods Hub|Learning Methods]] · Method in practice: [[how-i-study]] §1*

> [!NOTE] Evidence: **Strong (chunking); strong (illusions of competence)**

## In plain words
**Chunking:** practice until a group of steps becomes one unit you can use without thinking, the way a chess master sees a position, not 32 pieces.

**Illusion of competence:** feeling that you know something because it looks familiar on the page. The fix is to test yourself and compare your confidence with your score.

## The evidence, honestly
Chunking is one of the best-established findings about expertise: Chase & Simon (1973) on chess masters, building on Miller (1956).
Koriat & Bjork (2005): learners overrate how well they will remember material whose answer is visible while they study it.
Oakley's *Learning How to Learn* (Week 2) teaches both; the research behind them is solid.

## Using it in EECS
- "Swap two variables", "two-pointer scan", "voltage divider" and "read–modify–write" are chunks.
- Drill each one until you recognize it on sight.
- Predict before every quiz and compare.

## Common mistakes
- Judging readiness by how familiar the page feels.
- Building chunks from examples you never practised yourself.

## 🔨 Project: Calibration Tracker
Before each Khan quiz or NeetCode problem, write your predicted score or "will I solve it: yes/no". Afterwards, log predicted vs actual in a CSV. Plot it with a few lines of Python (matplotlib), or use a spreadsheet chart.
- **Done when:** 20 predictions are logged, the chart shows whether you are over- or under-confident, and you wrote one sentence on what you'll change.
- **Time:** about 3 h, counted inside [[BM - Bedrock Mathematics|BM]]'s existing hours (the Shuffle Drill replaces the Khan practice sets beyond the unit tests (the unit tests stay); the why-ladders for invert-and-multiply and negative × negative count as Build Requirement 2's Feynman explanations).
- **Level / when:** Beginner Python or a spreadsheet. Week 10, with the prime sieve.

## Sources
- Miller (1956), "The magical number seven, plus or minus two", *Psychological Review* 63(2).
- Chase & Simon (1973), "Perception in chess", *Cognitive Psychology* 4(1).
- Koriat & Bjork (2005), "Illusions of competence in monitoring one's knowledge during study", *Journal of Experimental Psychology: Learning, Memory, and Cognition* 31(2).
