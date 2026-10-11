---
title: "Project: Cache Simulator"
id: "MOD06-PRJ-cache-sim"
type: "project"
module: "06-computer-architecture"
phase: "C"
order: 970
prerequisites: [MOD06-PRJ-kestrel-isa, FND-MA-PRJ-magnitudes-field-guide, MOD05-LAB01]
artifact: "cachesim: a trace-driven cache simulator (direct-mapped to fully associative, LRU/FIFO/random, write policies, miss classification), trace generators, and a set of experiments on your own programs and real Linux programs"
deliverable: "Lab report: what makes memory access fast? (with plots) + short demo"
---

# Project: Cache Simulator

| | |
| :-- | :-- |
| **Module** | 06 Computer Architecture |
| **Prerequisites** | [Kestrel ISA](../kestrel-isa/spec.md) emulator; [Magnitudes Field Guide](../../../00-foundations/math/projects/magnitudes-field-guide/spec.md); Module 05 Lab 01 (measurement) |
| **You build** | A simulator that replays a list of memory addresses (a **trace**) through a model of a CPU cache and reports hits, misses, and why each miss happened. You generate traces from your Kestrel programs and from real programs on your Linux machine, and run experiments that explain why some code is ten times faster than other code that does the same work |
| **Deliverable** | A lab report with plots, and a demo |

---

## Why this matters

Your Magnitudes Field Guide showed that main memory is about a hundred times slower than the CPU. Yet programs run fast — because of **caches**: small, fast memories that keep copies of recently used data close to the processor. Whether your program is fast often depends less on how many instructions it runs and more on how well it uses the cache.

That's why an array beats a linked list (Module 05 Lab 03's open question), why the order of nested loops over a 2D array can change speed by 10×, and why database engines (Module 11) are designed around blocks. In this project you build the model that explains all of it, and test it on real programs.

**Real-world analogs:** CPU L1/L2/L3 caches; Cachegrind (a real cache simulator in Valgrind); disk page caches; CDN caches.

---

## Background

- Memory is divided into **blocks** (also called **lines**), e.g. 16 words or 64 bytes. The cache holds whole blocks.
- An address splits into **tag | index | offset**: the offset picks a word within the block; the index picks a **set** in the cache; the tag says which block of memory is stored there.
- **Direct-mapped:** each set holds 1 block. **N-way set associative:** each set holds N blocks. **Fully associative:** one set holds everything.
- **Hit:** the block is in the cache. **Miss:** it isn't; fetch it (and perhaps evict another block — chosen by the **replacement policy**: LRU, FIFO, random).
- **Writes:** **write-back** (update the cache; write to memory only when the block is evicted, if it's "dirty") vs **write-through** (always also write memory); **write-allocate** or not (does a write miss bring the block into the cache?).
- **The 3 C's of misses:** **compulsory** (first touch ever — would miss even with an infinite cache), **capacity** (would miss even in a fully associative cache of the same size), **conflict** (only because of limited associativity).
- **Average memory access time:** AMAT = hit time + miss rate × miss penalty.

**[W] Why do caches work at all?** Programs show **locality**: they reuse recent data (**temporal**) and touch nearby addresses (**spatial**). If programs accessed memory randomly, caches would barely help.

---

## Milestones

### Milestone 1 — Trace formats and generators

1. **Kestrel traces:** add a mode to your emulator that writes every memory access: `I 0012` (instruction fetch), `R e003` (data read), `W 0101` (data write) — hex word addresses.
2. **Real Linux traces:** Valgrind's **Lackey** tool records every memory access of a real program: `valgrind --tool=lackey --trace-mem=yes ls > /dev/null 2> trace.txt` (lines like ` L 04222cac,8`). Write a reader for this format (byte addresses with sizes). Keep traces short (a few million lines).
3. **Synthetic generator** (Python): traces for patterns you design — sequential array scan, strided scan (every k-th element), random access, linked-list walk (nodes scattered in memory), and 2D matrix traversal in row-major vs column-major order.

**Done when:** you have at least six traces of different kinds.

### Milestone 2 — The simulator

`cachesim` with parameters: total size, block size, associativity (1, 2, 4, …, fully), replacement (LRU, FIFO, random with seed), write policy (write-back + write-allocate, or write-through + no-write-allocate), and address unit (word or byte).

**Subgoal labels [S] for one access:**
```
# 1. Split the address into tag, set index, block offset (shifts and masks — power-of-two sizes)
# 2. Look in that set for a block with this tag
# 3. Hit: update LRU/FIFO state; on write, mark dirty (write-back) or count a memory write (write-through)
# 4. Miss: choose a victim in the set (empty way first, then by policy); if dirty, count a write-back;
#    load the new block; update policy state
# 5. Classify the miss (Milestone 3)
```

**Output:** accesses, hits, misses, miss rate, write-backs, AMAT for given hit time and penalty.

**Tests:** tiny hand-traced cases (draw the cache on paper for a 10-access trace with 2 sets × 2 ways and predict every hit/miss [R]); LRU vs FIFO on a trace where they differ (construct one!); a fully associative cache with LRU must equal a single-set cache with N ways; sequential scan miss rate = 1 ÷ (words per block) once warm.

**Done when:** hand-traced tests pass.

### Milestone 3 — Classify the misses

For each miss, decide its C:
- **Compulsory:** this block has never been accessed before (keep a set of all blocks ever seen).
- **Capacity:** it would also miss in a **fully associative LRU cache of the same total size** (run that cache alongside).
- **Conflict:** otherwise.

**Done when:** every run reports the 3C breakdown, and for a direct-mapped cache on a trace designed to thrash two addresses that map to the same set, conflict misses dominate.

**Checkpoint:** [Milestone Checkpoint](<../../../04 - System/Milestone Checkpoint Template.md>). Feynman target: *the three kinds of misses, with one example each*.

### Milestone 4 — Experiments

For each experiment, **predict first** (in a table), then run, then explain:

1. **Matrix traversal:** a 256 × 256 matrix summed row by row vs column by column, in a 4 KiB, 64-byte-block cache. (Then: write the same two loops in Python with a large list of lists, time them, and see whether the real machine agrees — and why Python may blur the effect. Module 07 repeats this in C, where the effect is dramatic.)
2. **Array vs linked list** walk of 100,000 elements — answer Module 05 Lab 03's open question with numbers.
3. **Block-size sweep:** fixed cache size, block sizes 4 to 256 bytes on three traces. Why does the miss rate first fall, then rise?
4. **Associativity sweep:** 1, 2, 4, 8 ways, fully associative, on all traces. Where do conflict misses disappear?
5. **Replacement policies:** LRU vs FIFO vs random. When does it matter?
6. **Your Kestrel programs:** Life and the Ember-compiled Life. Instruction-fetch miss rate vs data miss rate. Would a split instruction/data cache help?
7. **A real program** (from Lackey): miss rate vs cache size from 1 KiB to 1 MiB. Plot on a log scale. Is there a **working-set** size where the curve flattens?

**Done when:** all seven experiments have predictions, results, and explanations.

### Milestone 5 — Two levels (stretch-sized but recommended)

Add an L2 cache behind L1. Report global and local miss rates and the combined AMAT. Use realistic latencies from your Magnitudes Field Guide.

---

## Testing guidance

- **Hand-traced tiny cases** are the gold standard; draw them.
- **Equivalences** between configurations (fully associative = 1 set) as tests.
- **Determinism:** random replacement uses a seed.

## Common pitfalls

- **Word vs byte addresses** between Kestrel traces and Lackey traces.
- **Accesses that cross a block boundary** (Lackey's sizes): decide how to count them (usually: touch both blocks).
- **LRU bookkeeping bugs:** update recency on hits, not just misses.
- **Too-long traces:** sample or shorten; your simulator in Python handles a few million accesses in reasonable time.

## Communication deliverable

1. **Lab report** (3 pages, E10): *"What makes memory access fast?"* — the seven experiments with predictions, plots (log scales where appropriate), the 3C breakdowns, and five practical rules for writing cache-friendly code.
2. **Demo:** the hand-traced example animated (print the cache after each access), then the matrix experiment.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Address splitting and the access steps from memory before coding |
| **F** | The 3 C's; locality |
| **W** | Why caches work; why block size has a sweet spot; LRU vs FIFO |
| **S** | Access-handling subgoals |
| **I** | Hardware model, your programs, and real programs together |
| **T** | Report and demo |

## Stretch goals

- **Prefetching:** on a miss to block b, also fetch b + 1. Which traces benefit?
- **Cachegrind comparison:** run `valgrind --tool=cachegrind` on the same real program and compare its miss rates with yours for the same configuration.
- **Kestrel with a cache:** add the cache model *inside* the emulator so memory accesses cost cycles, and report the new CPI for your programs.

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Traces | Kestrel, Lackey, and 5 synthetic patterns | Some | One |
| Simulator | All parameters; hand-traced tests; equivalence tests | Most | Bugs |
| 3C classification | Correct and demonstrated on a thrash trace | Partial | Missing |
| Experiments | Seven, with predictions and explanations | Five | Fewer |
| Communication | Report with five rules; demo | One | Neither |

**Done when:** every area at least 2; Simulator at 3.

## Connections

- **Back:** Magnitudes Field Guide (latencies), Module 05 (arrays vs lists; measurement), Kestrel (traces).
- **Forward:** Module 07 (cache effects measured in real C with `perf`), Module 08 (page caches and TLBs: the same idea for virtual memory), Module 11 (buffer pools: the same idea for disk pages).

> **Originality note:** the experiments, trace sources, and milestones were written for this curriculum.
