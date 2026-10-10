---
title: "Lab 02 — Sorting Workshop"
module: "05-data-structures-and-algorithms"
hours: 12
---

# Lab 02 — Sorting Workshop

**Goal:** implement five sorting algorithms, test them ruthlessly, race them, and understand why no comparison sort can beat about n log₂ n comparisons.

**Time:** about 12 hours, in four sessions.

**Deliverable:** a lab report: *"Which sort wins, when?"*

---

## Session 1 — Simple sorts and a test harness (3 hours)

### The test harness first

All sorts must pass the same tests. Write `test_sorts.py` with a **parametrised fixture** over the sort functions (Module 02 Lab 02), and test:
- empty list; one item; two items both orders;
- already sorted; reverse sorted; all equal; many duplicates;
- 1,000 random lists of random lengths (seeded), compared with `sorted()` — the **second witness**;
- **stability** (for the stable sorts): sort records `(key, original_index)` by key only; equal keys must keep their original order.
- the input list is not modified (decide: do your sorts return a new list, or sort in place? Be consistent and test it).

### Insertion sort

**Invariant** (Module 03 Lab 02): before processing item i, `xs[0:i]` is sorted. Each step takes item i and shifts it left past every larger item.

Write it with the invariant as an `assert` in test mode. Count comparisons. Best case (already sorted): about n. Worst (reversed): about n²/2. [W] Why is insertion sort excellent on *nearly sorted* data?

---

## Session 2 — Divide and conquer (3 hours)

### Merge sort

**Subgoal labels [S]:**
1. If the list has 0 or 1 items, it's sorted (base case).
2. Split it in half.
3. Sort each half (recursively — the leap of faith).
4. **Merge** the two sorted halves: repeatedly take the smaller front item.

**Why n log n:** there are log₂ n levels of splitting, and each level does about n work merging. Draw the recursion tree for n = 8 [R].

**Merge** is a two-pointer algorithm you'll reuse in Vault Search (merging sorted lists of document IDs). Write it carefully and test it alone. Merge sort is **stable** if, on ties, you take from the left half first.

### Quicksort

1. Choose a **pivot**.
2. **Partition:** rearrange so everything smaller than the pivot is to its left, larger to its right.
3. Recursively sort the two sides.

Average O(n log n), worst O(n²) — when pivots are always the smallest or largest (e.g. "first element as pivot" on already-sorted input). Implement with (a) first-element pivot and (b) **random** pivot. Feed both a sorted list of 5,000 items and observe (a) hit Python's recursion limit or crawl. [W] Why does a random pivot fix this for every input? (It doesn't make the worst case impossible, just astronomically unlikely — Module 03 Unit 8.)

---

## Session 3 — Heaps and counting (3 hours)

### Heap sort (and the binary heap)

A **binary min-heap** is a complete binary tree stored in an array, where each parent ≤ its children. Index tricks: children of i are 2i + 1 and 2i + 2; parent is (i − 1) // 2.

Implement `heap_push` (add at the end, **sift up**) and `heap_pop` (move the last item to the root, **sift down**), both O(log n). Heap sort: push everything, pop everything. You'll reuse this heap as the priority queue in Route Planner — make it a proper class with tests. (Not stable. [W] Why not?)

### Counting sort: breaking the n log n "barrier"

If keys are small integers (say 0–255), count how many of each, then output them in order: O(n + k) for k possible keys, **no comparisons at all**. Implement it, stable version (prefix sums of counts give each key's starting position).

**[W]** How does counting sort get around the n log n lower bound below? (The bound only applies to sorts that learn about order by *comparing*.)

---

## Session 4 — The lower bound and the race (3 hours)

### Why comparison sorts need about n log₂ n comparisons

A comparison sort must be able to produce every one of the **n!** possible orderings (Module 03 Unit 6). Each comparison has two outcomes, so k comparisons can distinguish at most 2ᵏ cases. To distinguish n! cases you need 2ᵏ ≥ n!, so k ≥ log₂(n!) ≈ n log₂ n − 1.44n. Compute log₂(n!) for n = 10, 100, 1,000 and compare with your merge sort's comparison counts. Write this argument in your Proof Journal.

### The race

Using `bench.py` (Lab 01): time all five sorts plus Python's built-in `sorted` (Timsort, implemented in C) on random, sorted, reversed, and "nearly sorted" (sorted, then 1% of items swapped) inputs, for n from 1,000 up to where each takes 10 seconds. Also count comparisons for the comparison sorts.

**Predict first** [R], then measure. Plot time vs n (log-log) per input type.

### Lab report

*"Which sort wins, when?"* — tables, plots, the comparison counts vs log₂(n!), and recommendations. Explain why `sorted` beats all of yours (C vs Python, and Timsort's trick of finding already-sorted runs).

---

## Done when

- [ ] Five sorts pass the full harness (stability tested for the stable ones).
- [ ] `MinHeap` class with tests (you'll reuse it).
- [ ] Lower-bound argument written; race done; report written.

## Retrieval and reflection

1. **[R]:** each sort's idea, invariant, best/worst/average cost, stability, and when to use it; the lower-bound argument.
2. **[F] (spoken, 2 min):** "Why does merge sort take n log n time?" with the recursion tree.
3. **Flashcards:** the heap index formulas; each sort's costs with reasons.

**Next:** [Lab 03 — Stacks, Queues, and Lists](lab-03-stacks-queues-and-lists.md).
