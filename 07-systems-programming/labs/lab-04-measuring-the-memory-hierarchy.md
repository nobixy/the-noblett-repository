---
title: "Lab 04 — Measuring the Memory Hierarchy"
id: "MOD07-LAB04"
type: "lab"
module: "07-systems-programming"
phase: "C"
order: 1030
prerequisites: [MOD07-LAB03]
---

# Lab 04 — Measuring the Memory Hierarchy

**Goal:** see the caches you simulated in Module 06 on your real machine, with C and `perf`: loop order, strides, working-set size, and array vs linked list.

**Sessions:** three.

**Deliverable:** a lab report comparing your measurements with your Cache Simulator's predictions.

---

## Session 1 — Timing C properly

- Use `clock_gettime(CLOCK_MONOTONIC, &ts)` for wall-clock timing in nanoseconds.
- Compile benchmarks with optimisation (`-O2`), but make sure the compiler can't delete the work: use the result (print a checksum) or the compiler will optimise the loop away. [W] Check with Compiler Explorer (Module 06 Lab 01) that your loop is still there.
- Repeat each measurement 5–10 times; report the **median**.
- Note your CPU's cache sizes (`lscpu`, or your [Magnitudes Field Guide](../../00-foundations/math/projects/magnitudes-field-guide/spec.md)).

---

## Session 2 — Four experiments

Predict each result first (using your Cache Simulator if you can), then measure.

1. **Loop order:** sum a 4096 × 4096 `int` matrix row by row (`a[i][j]`, inner loop over j) and column by column (inner loop over i). Report time and the ratio.
2. **Stride:** sum every k-th element of a 64 MiB array for k = 1, 2, 4, …, 64 (always doing the same number of additions by looping more times for small k — or report time per element touched). Where does the time per element jump, and why does it jump at that k? (Block size!)
3. **Working set:** repeatedly walk arrays of size 4 KiB, 8 KiB, … up to 256 MiB (many passes each), reporting time per access. Plot on a log scale. You should see **steps** at your L1, L2, and L3 sizes — your Magnitudes Field Guide's stretch goal, now clearly visible in C.
4. **Array vs linked list:** sum 10 million ints stored (a) in an array, (b) in a linked list whose nodes were allocated in order, (c) in a linked list whose nodes were **shuffled** in memory (allocate an array of nodes, then link them in a random order). Report time per element. This answers Module 05 Lab 03's question for real.

---

## Session 3 — perf

`perf stat` counts hardware events using the CPU's own counters:

```bash
perf stat -e cycles,instructions,cache-references,cache-misses,L1-dcache-load-misses ./loop_order row
perf stat -e cycles,instructions,cache-references,cache-misses,L1-dcache-load-misses ./loop_order col
```

(If perf reports "permission denied", see `perf_event_paranoid` in `man perf_event_open`; on your own machine, `sudo sysctl kernel.perf_event_paranoid=1` is a common setting.)

- **IPC** (instructions per cycle) = instructions ÷ cycles. Which version has the higher IPC? Why?
- Compare L1 miss counts between the two loop orders with your Cache Simulator's prediction for the same access pattern (scaled to your real cache). How close is the model?

---

## Lab report

*"Does my real machine behave like my cache model?"* — the four experiments with predictions and results, the working-set plot with cache sizes marked, the perf counters, and three rules for cache-friendly C.

## Done when

- [ ] Four experiments measured (medians, with checksums printed so nothing is optimised away).
- [ ] perf counters for at least two experiments.
- [ ] Lab report written.

## Retrieval and reflection

1. **[R]:** why row order beats column order; what stride does; what a working-set plot shows; IPC.
2. **[W]:** your Module 05 benchmarks were in Python. Would the array-vs-list gap be bigger or smaller there? Why?
