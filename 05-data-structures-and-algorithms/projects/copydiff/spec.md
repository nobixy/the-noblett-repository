---
title: "Project: Copydiff"
module: "05-data-structures-and-algorithms"
hours: 35
artifact: "copydiff: a word-level diff tool for Franklin copywork — LCS by dynamic programming, Myers' diff, edit-distance classification of spelling vs word changes, reports, and integration with your spelling log"
deliverable: "Design doc (v2 from E10, updated after build) + accuracy report against your hand diffs + 4-minute demo"
---

# Project: Copydiff

| | |
| :-- | :-- |
| **Module** | 05 Data Structures and Algorithms |
| **Time** | About 35 hours |
| **Prerequisites** | Labs 01–03 of this module; your [First Design Doc](../../../00-foundations/english/projects/first-design-doc/spec.md) v2 for Copydiff (if you skipped it, write a design doc now, using that spec's Milestones 1–2) |
| **You build** | The tool that automates step 6 of Franklin copywork: given the original passage and your rebuild, it lines them up word by word, shows what you dropped, added, or changed, separates **spelling** mistakes from **word-choice** differences, counts punctuation differences, logs the numbers over time, and feeds new misspellings into your spelling log |
| **Deliverable** | Your design doc (updated after building), an accuracy report, and a demo |

---

## Why this matters

You've done copywork diffs by hand for months; you know exactly what a good comparison looks like. Now you build it, and in doing so you meet **dynamic programming** — one of the most powerful ideas in algorithms — in its most famous form: finding the **longest common subsequence** of two sequences. The same algorithm family powers `diff`, `git`, spell checkers ("did you mean…?"), DNA sequence alignment, and plagiarism detectors.

You also experience the full engineering loop for the first time: design doc *before* (written in E10), build, measure against goals, and update the doc with what you learned.

**Real-world analogs:** `diff`, `git diff --word-diff`, code review tools, Levenshtein-based spell suggestion.

---

## Before you start: compare designs

Reread your design doc v2. Then read this spec. Where they differ, decide which approach to take **and write the decision** (one short paragraph each) in a new section of your doc: "Changes after reading the build spec." Neither is automatically right. This is how real teams reconcile a design with new information.

---

## Milestones

### Milestone 1 — Tokens

1. **Tokenise** each text into a list of tokens: words (letters, digits, apostrophes inside words like *don't*), and each punctuation mark as its own token. Keep each token's position in the original text (for highlighting later).
2. **Normalisation options:** case-insensitive comparison (on by default), punctuation on/off, curly vs straight quotes treated as equal.
3. **Tests:** contractions, hyphenated words (decide: one token or three? [W]), numbers, empty input, multiple spaces and line breaks.

**Done when:** tokenisation of five of your real copywork passages looks right to you, and tests pass.

### Milestone 2 — LCS by dynamic programming

The **longest common subsequence** (LCS) of two token lists is the longest list of tokens that appears in both **in the same order** (not necessarily next to each other). Tokens in the LCS are "kept"; tokens only in the original were **deleted** (you dropped them); tokens only in your rebuild were **inserted**.

**The recurrence** (Module 03 induction thinking): let L[i][j] be the LCS length of the first i tokens of A and the first j of B.
- L[0][j] = L[i][0] = 0
- If A[i−1] == B[j−1]: L[i][j] = L[i−1][j−1] + 1
- Otherwise: L[i][j] = max(L[i−1][j], L[i][j−1])

**Subgoal labels [S]:**
1. Fill the table row by row (each cell needs only cells above, left, and diagonal — already filled).
2. **Backtrack** from L[n][m] to recover the actual edit script: diagonal moves on matches = KEEP; up = DELETE; left = INSERT.
3. Merge consecutive operations into runs for display.

**Do one by hand first:** A = "the cat sat on the mat", B = "the cat sat on a mat". Fill the 7 × 7 table on paper; backtrack. [R]

**Tests:**
- On tiny random inputs (lengths ≤ 8, small vocabulary), check your LCS length against a **brute-force** search over all subsequences (Module 03 counting tells you why this only works for tiny inputs).
- The edit script, applied to A, produces B exactly (a **round-trip** test: apply KEEPs and INSERTs, skip DELETEs).

**Measure:** time and memory for passages of 100, 1,000, and 10,000 tokens. The table is n × m: what happens to memory at 10,000? (M11/Lab 01.)

**Done when:** brute-force and round-trip tests pass, and the measurement table is done.

**Checkpoint:** [Milestone Checkpoint](<../../../04 - System/Milestone Checkpoint Template.md>). Feynman target: *why the LCS table can be filled cell by cell* (overlapping subproblems; Module 02's memoised `paths` was the same idea). Why-ladder target: *why does "max of up and left" give the right answer when the tokens differ?*

### Milestone 3 — Myers' diff

The LCS table always costs n × m time and memory, even when the texts are almost identical — which, for good copywork, they are. **Myers' algorithm** (Eugene Myers, 1986; used in `git`) finds a shortest edit script in **O((n + m) · D)** time, where D is the number of differences. When D is small, that's nearly linear.

The idea: explore edit paths in order of how many edits they use (0 edits, 1 edit, 2…), following free diagonal "snakes" of matching tokens as far as they go. Read the algorithm's description (the original paper, "An O(ND) Difference Algorithm and Its Variations," is readable; many blog posts walk through it with pictures). Then implement the basic forward version with trace recording for backtracking.

**Tests:** for 1,000 random pairs, Myers' edit script has the **same number of edits** as the LCS method (n + m − 2·LCS). Round-trip tests as before.

**Measure:** Myers vs LCS table on (a) your passages, (b) a 10,000-token essay vs a copy with 20 random edits, (c) two unrelated 2,000-token texts. When does each win? Plot.

**Done when:** tests pass; the comparison table shows where Myers helps and where it doesn't.

### Milestone 4 — Spelling vs word change

A DELETE followed by an INSERT at the same place is a **substitution**: you wrote a different token. Was it a misspelling (*seperate* for *separate*) or a different word (*quick* for *fast*)?

1. **Pair up** adjacent delete/insert runs of equal length into substitutions.
2. **Levenshtein edit distance** between the two words: the minimum number of single-letter insertions, deletions, and substitutions to turn one into the other. Another DP table (letters instead of tokens) — implement it yourself.
3. **Classify:** a substitution is a **spelling** error if the distance is small relative to the word's length (e.g. distance ≤ max(1, length ÷ 4)) — tune this threshold **using your own hand diffs** as ground truth, and justify the final choice [W]. Also: if the rebuild word is in a dictionary (`/usr/share/dict/words`, or a word list you download), it's probably a *word choice*, even if close (*form* vs *from*). Decide how to combine the two signals.
4. Punctuation tokens get their own category.

**Output counts:** words kept, dropped, added, word changes, spelling errors, punctuation differences — matching the metrics your design doc promised.

**Done when:** classification runs on your passages, with a confusion table against your hand judgements.

### Milestone 5 — Reports and integration

1. **Terminal output:** the rebuild with colours — kept (plain), dropped (red, struck through or in `[-…-]`), added (green `{+…+}`), spelling errors (yellow, with the correct word).
2. **HTML report** with the same colouring, for keeping (open in a browser).
3. **Copywork log:** append a row per run to `copywork-log.tsv` (date, passage name, level, each count). `copydiff trend` shows a 30-day chart of spelling errors and word changes per 100 words.
4. **Spelling Engine integration:** offer to append new spelling errors to `spelling-log.tsv` (with tag `copywork`), skipping words already there.

**Done when:** you've used Copydiff for every copywork session for two weeks.

### Milestone 6 — Accuracy against your goals

Your design doc listed testable goals (e.g. "spelling-error count matches my hand count within ±1 on 8 of 10 passages"). Test them:
1. Take 10 passages you diffed **by hand** in the past (your copywork template's section 4).
2. Run Copydiff on each. Compare its counts with yours.
3. For every disagreement, decide who was right — you or the tool — and why.

**Done when:** an accuracy table and a decision for every disagreement.

---

## Testing guidance

- **Brute force for tiny inputs**, **round trips** for every edit script, **two algorithms that must agree** on edit counts.
- **Real data** (your passages) for classification, with your own judgements as the oracle.
- Keep a `fixtures/` folder of tricky passages: repeated words, moved sentences, a dropped line.

## Common pitfalls

- **Recursion depth in backtracking:** iterate instead (Lab 03).
- **Memory blow-up of the full table** for long texts: that's why Myers exists (and why the LCS method can be done keeping only two rows if you only need the length).
- **Moved sentences:** diff sees a moved sentence as a delete plus an insert far away. That's a known limit of diff; detect "same sentence elsewhere" as a stretch goal, and say so in the doc.
- **Over-tuning the spelling threshold** to 10 passages. Hold out 3 passages you don't tune on, and test on them last.

## Communication deliverable

1. **Design doc:** v2 from E10 + "Changes after reading the build spec" + section 8 "After the build" (what changed, what surprised you, what you'd do differently).
2. **Accuracy report** (1–2 pages): goals vs results, the confusion table, the threshold decision, the LCS vs Myers measurements.
3. **Demo (4 minutes):** a real copywork session from rebuild to diff to logged trend.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Fill the LCS table by hand from memory before coding; write the Levenshtein recurrence from memory |
| **F** | Why the DP table works; how Myers saves work |
| **W** | Hyphen tokens; the threshold; dictionary signal; LCS vs Myers trade-offs |
| **S** | DP subgoals; classification pipeline |
| **C** | You are building copywork's own tool — and using it every session |
| **T** | Design doc lifecycle, report, demo |

## Stretch goals

- **Linear-space LCS** (Hirschberg's algorithm): the edit script in O(n + m) memory.
- **Moved-block detection:** recognise a dropped sentence that reappears elsewhere.
- **Sentence-level view:** align sentences first, then words within sentences — faster and more readable.
- **Patience diff** (used as an option in git): read about it and compare outputs on real text.

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Tokens | All options; tricky cases decided and tested | Basic | Fragile |
| LCS | Hand table; brute-force and round-trip tests; measured | Works | Wrong scripts |
| Myers | Agrees with LCS on 1,000 pairs; comparison plotted | Works | Missing |
| Classification | Levenshtein yours; threshold justified; held-out test | Works | Guesswork |
| Integration | Two weeks of real use; logs and trend; spelling log fed | Some use | None |
| Communication | Doc lifecycle complete; accuracy report; demo | Most | Few |

**Done when:** every area at least 2; LCS and Integration at 3.

## Connections

- **Back:** E10 (the design doc), all your copywork, [Spelling Engine](../../../00-foundations/english/projects/spelling-engine/spec.md) (now fed automatically), Module 02 Lab 01 (memoisation), Module 03 (induction, counting).
- **Forward:** Edit Buffer (diffing two versions of a buffer), Module 11 (comparing database states), and any time you read `git diff` — you'll know what's underneath.

> **Originality note:** Copydiff's purpose, classification design, and milestone plan were written for this curriculum. LCS, Levenshtein distance, and Myers' algorithm are classic published algorithms used here as components.
