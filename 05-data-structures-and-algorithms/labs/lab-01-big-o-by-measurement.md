---
title: "Lab 01 — Big-O by Measurement"
module: "05-data-structures-and-algorithms"
hours: 10
---

# Lab 01 — Big-O by Measurement

**Goal:** understand big-O notation as a precise statement about growth — and never trust one without measuring it. You'll also build a dynamic array and *prove* (and measure) why appending to it is cheap on average.

**Time:** about 10 hours, in three sessions.

**Deliverable:** a short lab report: *"Growth strategies for dynamic arrays."*

---

## Session 1 — The notation (3 hours)

### Counting steps, then ignoring the details

To compare algorithms independent of machine speed, count **basic steps** (comparisons, additions, memory reads) as a function of the input size n. Then keep only the part that dominates for large n.

| Steps | Dominant part | Big-O |
| :-- | :-- | :-- |
| 3n + 7 | 3n | O(n) |
| n²/2 + 5n | n²/2 | O(n²) |
| 4 log₂ n + 10 | log n | O(log n) |
| 2ⁿ + n³ | 2ⁿ | O(2ⁿ) |

**Definitions** (Module 03 precision):
- f(n) = **O(g(n))** if there are constants c > 0 and n₀ such that f(n) ≤ c·g(n) for all n ≥ n₀. ("f grows **no faster** than g.")
- f(n) = **Ω(g(n))** if f(n) ≥ c·g(n) for all n ≥ n₀. ("No slower.")
- f(n) = **Θ(g(n))** if both. ("Same growth.")

**[W] Why drop constants?** Because constants depend on the machine, the language, and the compiler, while the growth shape doesn't. A 100× faster computer makes an O(n²) algorithm 100× faster — but doubling n still makes it 4× slower. For large enough n, growth always wins (M11 Part 6).

**[W] When do constants matter?** For small n, and when two algorithms have the same growth. Insertion sort (O(n²)) beats merge sort (O(n log n)) on lists of 10 items — that's why real sorting libraries switch to insertion sort for small pieces.

### Best, worst, average

Linear search for a target: best case 1 comparison (it's first), worst case n (last or missing), average about n/2. Always say **which case** you mean. Worst case is the usual default, because it's a guarantee.

### Practice [S]

For each function, count steps as a formula, then give big-O. Then explain your count with labels ("outer loop runs n times; inner loop runs i times; total 1 + 2 + … + n").

```python
def f1(xs):
    return xs[0] + xs[-1]

def f2(xs):
    t = 0
    for x in xs: t += x
    return t

def f3(xs):
    n = len(xs); c = 0
    for i in range(n):
        for j in range(i + 1, n):
            if xs[i] == xs[j]: c += 1
    return c

def f4(n):
    c = 0
    while n > 1:
        n //= 2; c += 1
    return c

def f5(xs):
    for x in xs:
        if x in xs[:10]:     # careful: what does this cost?
            print(x)
```

<details>
<summary>Answers</summary>

f1: O(1). f2: O(n). f3: n(n − 1)/2 comparisons (M11's Gauss sum) → O(n²). f4: about log₂ n halvings → O(log n). f5: `xs[:10]` makes a 10-item copy and `in` scans it: ≤ 10 steps per item, a constant → O(n). (Hidden costs like slicing are a classic trap.)
</details>

---

## Session 2 — Measure it (3 hours)

### Log-log plots reveal the exponent

If time T(n) ≈ c · nᵏ, then log T = log c + k · log n — a **straight line** on a plot with both axes logarithmic, with **slope k** (M11: the log turns powers into multiplication). So:
1. Time a function at n = 1,000; 2,000; 4,000; … (doubling).
2. Plot log(time) against log(n).
3. Fit the slope (M09, using two far-apart points, or least squares from Module 12 later).

Slope ≈ 1 → linear. ≈ 2 → quadratic. A curve that bends upward → something worse (or a cache effect — Module 06).

Also use the **doubling ratio**: T(2n)/T(n) ≈ 2 for O(n), ≈ 4 for O(n²), ≈ 2 + a bit for O(n log n), ≈ 1 + a bit for O(log n).

### Build `bench.py`, a reusable benchmarking helper

```python
def bench(fn, make_input, sizes, repeats=5):
    """Time fn on inputs of each size; return [(n, median_seconds)]."""
    # 1. For each n: build the input BEFORE timing
    # 2. Time `repeats` runs with time.perf_counter(); keep the median (robust to hiccups)
    # 3. Return the table
```

Plus `loglog_slope(table)` and `doubling_ratios(table)`. You'll reuse this in every project in this module.

**Measure** f2, f3, f4, and Python's `sorted`, `list.append`, `x in list`, `x in set`, and `list.insert(0, x)`. Predict each slope **before** measuring [R]. Which surprised you? (`list.insert(0, x)` is O(n) — every element shifts. Why? Session 3 explains.)

---

## Session 3 — The dynamic array and amortised cost (4 hours)

A Python `list` is a **dynamic array**: elements sit side by side in one block of memory, so `xs[i]` is instant (O(1): jump straight to position i). But the block has a fixed **capacity**. When it's full, the list must allocate a bigger block and **copy everything over**.

### Build `DynArray`

Using a fixed-size underlying store (simulate one with `[None] * capacity` and never call `append` on it), implement: `append`, `get(i)`, `set(i, v)`, `pop()`, `__len__`, and a **copy counter** that counts every element copied during growth.

Two growth strategies:
- **Add a constant:** when full, grow capacity by 10.
- **Double:** when full, double the capacity.

### Measure and prove

1. Append n = 1,000 … 1,000,000 items with each strategy. Record total copies.
2. **Prediction for doubling:** the copies are 1 + 2 + 4 + … + (the last capacity) < 2n (M11's binary sum!). So the **average** cost per append is less than 2 copies — O(1) **amortised**, even though one append occasionally costs n.
3. **Prediction for +10:** copies are 10 + 20 + 30 + … ≈ n²/20. So the average per append grows with n: O(n) amortised.
4. Plot total copies against n on a log-log plot. Slopes ≈ 1 and ≈ 2.

**Write the proof** (Proof Journal style) that doubling gives fewer than 2n total copies for n appends.

**[W] Why not triple?** Or grow by 1.5×? (Many real implementations use about 1.125–1.5×.) What's the trade-off? (Hint: wasted space.)

### Lab report

*"How does the growth strategy of a dynamic array affect the cost of appending?"* — predictions, the two copy-count curves, the log-log slopes, the proof, and the space-vs-time trade-off.

---

## Done when

- [ ] Session 1 practice done and checked.
- [ ] `bench.py` works; at least eight functions measured with predictions recorded first.
- [ ] `DynArray` with both strategies; copy counts match the predictions; report written.

## Retrieval and reflection

1. **[R]:** O, Ω, Θ definitions; why drop constants and when they still matter; the log-log slope method; amortised cost of doubling with its proof.
2. **[F] (spoken, 2 min):** "Why is appending to a Python list fast, even though it sometimes copies everything?"
3. **Flashcards:** each Python operation's cost **with its reason**.

**Next:** [Lab 02 — Sorting Workshop](lab-02-sorting-workshop.md).
