---
title: "Project: Growth and Halving Lab"
track: math
stages: "M11"
hours: 14
artifact: "Paper experiments; search.py and growth.py with measured tables and log-scale plots"
deliverable: "Lab report: how fast do different algorithms grow, and does log₂ n really describe binary search?"
---

# Project: Growth and Halving Lab

| | |
| :-- | :-- |
| **When** | M11, week 5 |
| **Time** | About 14 hours |
| **You build** | Experiments — on paper, with coins, and in code — that test the growth laws of M11 against reality: binary search vs linear search, n² vs 2ⁿ, halving processes |
| **Deliverable** | A lab report with log-scale plots |

---

## Why this matters

M11 told you that binary search takes about log₂ n steps, that comparing every pair takes about n²/2, and that 2ⁿ explodes. This lab makes you **check**. You'll count steps, time code, and plot the results — and you'll see the curves from M11 appear in your own data.

This is the bridge into [Module 05](../../../../05-data-structures-and-algorithms/overview.md), where every data structure you build gets this kind of analysis. Engineers who measure growth instead of guessing it make far better design decisions.

**Real-world analogs:** benchmarking, algorithm analysis, performance regression testing, capacity planning.

---

## Milestones

### Milestone 1 — Paper and coin experiments

1. **The guessing game.** With a friend (or a random number generator you don't look at), play "guess my number" for ranges 1–10, 1–100, 1–1,000, using the halving strategy. Play each range 3 times. Record the number of guesses. Compare with ⌈log₂ n⌉.
2. **Coin halving.** Start with 64 coins (or any 50+). Flip all of them; remove every coin that lands heads. Repeat with the survivors until none are left. Record the survivors each round. Do it 3 times. On average, how many rounds does it take? Compare with log₂ 64 = 6. Why isn't it exactly 6 every time?
3. **The chessboard.** One grain of rice on the first square, two on the second, four on the third… How many grains on the 64th square? On the whole board? (Use the binary sum from M11.) At about 25 mg per grain, how many tonnes is that? Write it in scientific notation.

**Done when:** three tables and the chessboard answer.

<details>
<summary>Check (chessboard)</summary>

Square 64: 2⁶³ ≈ 9.2 × 10¹⁸ grains. Whole board: 2⁶⁴ − 1 ≈ 1.8 × 10¹⁹ grains. At 25 mg = 2.5 × 10⁻⁵ kg each: ≈ 4.6 × 10¹⁴ kg ≈ 4.6 × 10¹¹ tonnes — hundreds of times the world's yearly rice harvest.
</details>

### Milestone 2 — `search.py`: count the steps

Write two functions that search a **sorted** list for a target and **return the number of comparisons** they made:
- `linear_search(items, target)` — check each item from the start.
- `binary_search(items, target)` — check the middle; throw away the half that can't contain the target; repeat.

**Experiment:** for n = 10, 100, 1,000, …, 1,000,000 (sorted lists `list(range(n))`), search for 100 random targets each, and record the **average** and **maximum** comparisons for both methods.

**Compare:** put log₂ n and n/2 next to your measured averages in the table. How close are they?

**Tests:** both functions find every element of a small list; both report "not found" correctly for a missing target; binary search on a 1-element and a 0-element list doesn't crash.

**Done when:** the table is complete and the comparison is written in two or three sentences.

**Checkpoint:** [Milestone Checkpoint](<../../../../04 - System/Milestone Checkpoint Template.md>). Feynman target: explain why binary search *needs* a sorted list. Why-ladder target: *why is the maximum for binary search ⌈log₂(n + 1)⌉ and not log₂ n exactly?*

### Milestone 3 — `growth.py`: time three kinds of growth

Write three functions and time them for growing n:
1. **Linear:** sum a list of n numbers.
2. **Quadratic:** count how many pairs (i, j) with i < j in a list of n random numbers have a sum divisible by 7. (Use two nested loops on purpose — M11 Part 5 says this is about n²/2 checks.)
3. **Exponential:** count how many **subsets** of a list of n small numbers add up to exactly 50 (try every subset — there are 2ⁿ).

**Experiment:**
- For each function, find the n where one run takes about **1 second** on your machine. (Double n until it's over a second.)
- Check the **doubling rule:** when n doubles, the linear time should roughly double, the quadratic time should roughly **quadruple**, and the exponential time should roughly **square** (adding just one item doubles it). Record the ratios you measure.

**Plot** time vs n for all three on **one log-scale plot** (y-axis in powers of 10; by hand on graph paper, or with `matplotlib` using `plt.yscale("log")`). On a log scale, what shape does each curve make?

**Done when:** the 1-second table, the doubling-ratio table, and the plot are done.

### Milestone 4 — Predict, then test

Use your measurements to make **three predictions** before running anything:
1. How long will the quadratic function take for n = 4 × (your 1-second n)?
2. How long would the exponential function take for n = (your 1-second n) + 10? + 30? (Use scientific notation; compare the second to your lifetime.)
3. How many comparisons will binary search need for a list of 1 billion items?

Write each prediction with its reasoning. Then test the first one (and the third, if you have the memory — otherwise reason about it). Record the percent error.

**Done when:** three written predictions, at least one tested, with percent error.

---

## Common pitfalls

- **Timing tiny operations:** repeat them and divide (see Magnitudes Field Guide).
- **Including setup time:** build the list *before* starting the timer.
- **Sorted vs unsorted:** binary search on an unsorted list gives wrong answers silently. Assert the list is sorted in your tests.
- **Midpoint bugs:** binary search has famous off-by-one traps (`lo <= hi` vs `lo < hi`, `mid + 1` vs `mid`). Test small lists of size 0, 1, 2, and 3 exhaustively: every target present and absent.
- **Exponential runs that never end:** start small (n = 10) and add one at a time.

## Communication deliverable

**Lab report** ([template](<../../../../04 - System/Lab Report Template.md>), E08–E09 level, 1–2 pages): *"Do real programs grow the way M11 says?"* Include your search table, the 1-second table, the doubling ratios, the log-scale plot, and your Milestone 4 predictions and results. End with one practical rule for choosing algorithms.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Write the growth table from M11 from memory before Milestone 3 |
| **F** | Why binary search needs sorting |
| **W** | ⌈log₂(n + 1)⌉; why the coin experiment isn't exactly 6 |
| **S** | Binary search as subgoal comments: *pick middle → compare → discard half → repeat → stop* |
| **I** | Paper, coins, and code; three growth types side by side |
| **T** | The lab report |

## Stretch goals

- **Interpolation search:** guess the position by proportion (like opening a dictionary near "S" for "snake"). Count its comparisons on evenly spaced data. Then on very uneven data.
- **Smarter subsets:** can you make the subset-sum counter faster for small target values? (Search "subset sum dynamic programming." You'll study this idea in Module 05.)
- **Fit the exponent:** on a log-log plot (both axes log), a function n^k is a straight line with slope k. Measure the slope of your quadratic function's line. Is it close to 2?

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Paper experiments | All three, compared with theory | Two | One |
| Search | Correct, tested edge cases, table vs log₂ n | Works | Bugs |
| Growth | 1-second table, doubling ratios, log plot | Partial | Missing |
| Predictions | Written first, tested, percent error | Written, untested | Missing |
| Lab report | Clear, honest, practical rule | Complete | Missing |

**Done when:** every area at least 2.

## Connections

- **Back:** M07 (powers, scientific notation), M11 (everything); [Prime Factory](../prime-factory/spec.md) (your first timing experiments).
- **Forward:** Module 05 (every data structure and algorithm), Module 11 (why database indexes are B+trees with log-time lookups).
