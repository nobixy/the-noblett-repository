---
title: "Project: Heapsmith"
module: "07-systems-programming"
hours: 50
artifact: "libheapsmith: a malloc/free/realloc/calloc implementation in C that evolves from a bump allocator to segregated free lists with coalescing, mmap for large blocks, a heap checker, debug features, a heap visualiser, a real-program trace recorder, and LD_PRELOAD support"
deliverable: "Design doc + evaluation report (throughput and utilisation vs glibc, per version) + 5-minute demo with heap animations"
---

# Project: Heapsmith

| | |
| :-- | :-- |
| **Module** | 07 Systems Programming |
| **Time** | About 50 hours |
| **Prerequisites** | Labs 01–03 of this module; Module 05 (lists, size classes are like hash buckets, measurement) |
| **You build** | Your own memory allocator. It hands out and takes back blocks of memory from a region you get from the kernel, keeps track of free space with lists inside the free memory itself, merges neighbours, sorts requests into size classes, and grows by asking the kernel for more. You also build the tools to trust it: a trace format, a recorder that captures real programs' `malloc` calls, a heap checker, debug canaries, a picture of the heap, and finally the ability to run **real Linux programs on your allocator** |
| **Deliverable** | Design doc, evaluation report, and demo |

---

## Why this matters

Every program you've written in Python called `malloc` thousands of times without you knowing. Writing an allocator teaches pointers more deeply than anything else: you'll treat raw memory as headers, links, and payloads, and one wrong cast corrupts everything. It also teaches the core trade-off of systems design — **speed vs space** — in its purest form: a faster allocator usually wastes more memory, and you'll measure exactly how much.

Your kernel in Module 08 needs a heap, and you'll reuse these ideas there.

**Real-world analogs:** glibc's ptmalloc, jemalloc (FreeBSD, Firefox), tcmalloc (Google), mimalloc (Microsoft), kernel slab allocators.

---

## The interface

```c
void *hs_malloc(size_t size);
void  hs_free(void *ptr);
void *hs_realloc(void *ptr, size_t size);
void *hs_calloc(size_t n, size_t size);
int   hs_check(void);            // heap checker: 0 if all invariants hold, else prints problems
void  hs_dump(const char *path); // write a picture of the heap (Milestone 6)
```

**Requirements** (same as the C standard's `malloc`): returned pointers are aligned to **16 bytes**; `hs_malloc(0)` returns NULL or a unique pointer (decide); `hs_free(NULL)` does nothing; `hs_realloc(NULL, n)` = `hs_malloc(n)`; `hs_realloc(p, 0)` frees (decide and document); `hs_calloc` checks `n × size` for overflow.

Get memory from the kernel with **`mmap`** (anonymous, private), in big chunks (e.g. 1 MiB "arenas"). Don't call the system `malloc` from inside your allocator.

---

## The trace format and driver

```
# trace: a = allocate, f = free, r = realloc; ids name blocks
a 0 24
a 1 4096
r 0 100
f 1
f 0
```

The **driver** (`hsdrive trace.txt --impl v3`):
- replays a trace, writing a unique byte pattern into each block's payload and **checking it's intact** before each free/realloc (this catches allocators that hand out overlapping blocks);
- checks alignment and that no two live blocks overlap (keep the live blocks in a sorted structure — Module 05);
- calls `hs_check()` every N operations in check mode;
- reports **throughput** (operations per second) and **peak utilisation** = (peak total live payload bytes) ÷ (peak total bytes obtained from the kernel).

**Trace sources:**
1. **Synthetic generators** (Python): random sizes; many tiny objects; a few huge ones; "phases" (allocate 100,000 blocks, free every other one, then allocate bigger ones — a fragmentation stress test); realloc-heavy (growing buffers).
2. **Real programs** (Milestone 7's recorder).

---

## Milestones

### Milestone 1 — Design doc, driver, and a bump allocator

1. **Design doc v1** (4–6 pages): the block layout (header, payload, footer — draw it to the byte), the heap invariants you'll check, the planned versions, the metrics and goals (e.g. "v4 within 2× of glibc's throughput and ≥ 80% utilisation on the phase trace"), and alternatives.
2. **v0 — bump allocator:** keep a pointer to the next free byte; `malloc` rounds up and moves it; `free` does nothing. Absurdly fast; terrible utilisation. It's your baseline.
3. The driver and three synthetic traces.

**Done when:** the driver runs v0 on all traces with correct payload checks.

### Milestone 2 — v1: implicit free list, boundary tags, coalescing

Every block has a **header** (size and an "allocated" bit — sizes are multiples of 16, so the low 4 bits are free for flags [W]) and a **footer** (a copy of the header at the end).

```
| header: size|alloc | payload … | footer: size|alloc |
```

- **Find:** walk all blocks from the start (the "implicit list") and take the **first** free block big enough (**first fit**).
- **Split** it if the remainder is big enough to be a block on its own.
- **Free:** mark it free; then **coalesce** immediately with the previous and next blocks if they're free. The footer of the previous block tells you where it starts — that's why footers exist.
- **Grow:** when nothing fits, get another arena with `mmap` and add it.

**Heap checker `hs_check`:** walk every block and verify: sizes are multiples of 16 and within the arena; header equals footer; **no two adjacent free blocks** (coalescing invariant); every payload is aligned; the walk ends exactly at the arena's end.

**Subgoal labels [S]** for `free`:
```c
// 1. Find the header from the payload pointer
// 2. Mark the block free (header and footer)
// 3. If the next block is free: merge (new size = sum), update the new footer
// 4. If the previous block is free: merge into it (read its footer to find it)
// 5. (Debug) run hs_check
```

**Done when:** all traces pass with `hs_check` after every operation.

**Checkpoint:** [Milestone Checkpoint](<../../../04 - System/Milestone Checkpoint Template.md>). Retrieval target: draw three adjacent blocks before and after a coalescing free, with every header and footer value. Feynman target: *how `free` knows how big a block is*.

### Milestone 3 — v2: explicit free list

Walking every block (including allocated ones) is slow. Store **next/prev pointers inside free blocks' payloads** (free payloads are unused, so it costs nothing) to form a doubly linked list of only the free blocks.

- Insertion policy: **LIFO** (push freed blocks at the front) vs **address-ordered** (keep the list sorted by address). Implement both; measure throughput and utilisation on all traces. [W] Why does address order often fragment less?
- Fit policy: first fit vs **best fit** (smallest block that fits). Measure.

**Done when:** a measured comparison table of four combinations.

### Milestone 4 — v3: segregated size classes and big blocks

1. **Segregated lists:** an array of free lists by size class (e.g. 16, 32, 48, 64, 80–128, 129–256, …, powers of two above that). `malloc` looks in the right class first, then larger ones. Small requests become nearly O(1).
2. **Big blocks:** requests above a threshold (e.g. 128 KiB) get their **own `mmap`**, and `free` returns them with `munmap`. [W] Why does this help utilisation? What does each `mmap` cost? (Measure with `strace -c`.)

**Done when:** v3 beats v2's throughput on every trace, with utilisation reported.

### Milestone 5 — realloc and calloc done well

- **In-place realloc:** shrink by splitting; grow by absorbing the next block if it's free and big enough; only otherwise allocate-copy-free.
- **calloc** with overflow check, and zeroing (can you skip zeroing for fresh `mmap` memory? It's already zero. Measure.)
- Test on the realloc-heavy trace: how often did growth happen in place?

### Milestone 6 — Debug mode and the heap picture

Compile-time `HS_DEBUG`:
1. **Canaries:** a known 8-byte pattern before and after every payload; check on free (and in `hs_check`). Report "heap overflow detected in block allocated at trace op 1,234."
2. **Double-free and invalid-free detection:** a magic number in the header of allocated blocks; freeing a block without it is reported, not obeyed.
3. **Leak report at exit:** `atexit` handler listing blocks never freed.

**Heap picture `hs_dump`:** write a **PPM image** (Lab 01 Session 8's binary-writing skills; PPM is a trivially simple image format: a short text header then RGB bytes) with one pixel per 16 bytes of heap: headers dark grey, allocated payload blue, free green, canaries red, padding yellow. Dump every 1,000 operations during the phase trace, and turn them into an animation (`ffmpeg -framerate 10 -i heap_%04d.ppm heap.mp4`, optional). **Watch fragmentation happen.**

### Milestone 7 — Real programs

1. **Recorder:** a shared library `librecord.so` that wraps `malloc`, `free`, `realloc`, `calloc` (find the real ones with `dlsym(RTLD_NEXT, "malloc")`) and writes each call to a trace file. Run it with `LD_PRELOAD=./librecord.so ls -la /usr/bin` and similar. **Pitfalls [W]:** `dlsym` and `fprintf` may themselves call `malloc` — guard against re-entry with a flag, write with `write()` into a static buffer, and handle the very first `calloc` from `dlsym` with a small static buffer. Read about this before starting; it's a famous puzzle.
2. **Loader:** build Heapsmith as `libheapsmith.so` exporting `malloc`/`free`/`realloc`/`calloc` and run real programs on it: `LD_PRELOAD=./libheapsmith.so ls`, `… python3 -c "print(sum(range(10**6)))"`, `… gcc --version`. Programs with threads need a lock: add a global `pthread_mutex_t` around every operation (and note the cost).

**Done when:** three real programs run correctly on your allocator, and three real traces are recorded.

### Milestone 8 — Evaluation

Run every version (v0–v3, plus v2's variants) and **glibc's malloc** (through the same driver, compiled against the system allocator) on every trace. Report throughput and peak utilisation in two tables and one scatter plot (utilisation vs throughput, one point per version per trace).

**Done when:** the tables and plot are done and you can name the best version for each kind of trace.

---

## Testing guidance

- **The driver's payload checks** catch overlap and corruption; `hs_check` catches broken structure; run both in check mode on every trace.
- **ASan can't see inside your allocator** (it only tracks the system's malloc), so your own checks matter. Do run the driver itself under ASan/Valgrind to catch bugs in the *driver*.
- **Random traces with a seed**, shrinking failures to minimal traces (Module 05), saved as regression tests.

## Common pitfalls

- **Pointer arithmetic in the wrong units:** do block arithmetic on `char *` (bytes), then cast. Write tiny inline helpers (`header_of(payload)`, `next_block(b)`, `footer_of(b)`) and test them alone.
- **Forgetting to update the footer** after a split or merge — the checker finds it.
- **Free-list pointers left dangling** after a merge removed a block from the list.
- **Alignment of headers:** with 16-byte alignment and an 8-byte header, payloads must start at 16-byte boundaries; work out the layout on paper first.
- **Recording traces with a recorder that mallocs** — infinite recursion.

## Communication deliverable

1. **Design doc** v1 → v2 (with block diagrams to the byte and every policy decision justified by measurements).
2. **Evaluation report** (2–3 pages): the tables and scatter plot, the fragmentation animation's story in words, the real-program results, and your recommendation.
3. **Demo (5 minutes):** the heap animation on the phase trace, `ls` running on your allocator, and the scatter plot.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Block layouts and free-list states drawn from memory before each milestone |
| **F** | How `free` knows the size; why fragmentation happens |
| **W** | Flag bits in sizes; LIFO vs address order; mmap threshold; recorder re-entrancy; every policy chosen by data |
| **S** | Subgoals for malloc, free, split, coalesce |
| **D** | Corrupted heaps are maddening: the checker narrows it down; then a stuck note |
| **T** | Design doc, report, demo |

## Stretch goals

- **Thread caches:** per-thread free lists for small sizes (like tcmalloc) and measure with a multithreaded trace.
- **A slab allocator** for one fixed size, as kernels use.
- **Your kernel's heap:** port v3 (minus mmap) to Module 08's Seedling kernel.

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Driver and traces | Payload/overlap checks; 5 synthetic + 3 real traces | Synthetic only | Weak checks |
| Correctness | v1–v3 pass all traces with `hs_check` every op | Most | Corruption |
| Policies | Explicit list variants and size classes measured | Some | Untested |
| Debug and visualisation | Canaries, double-free, leaks, heap pictures | Two | One |
| Real programs | Recorder and LD_PRELOAD loader on 3 programs | One | None |
| Evaluation | Full tables + scatter vs glibc | Partial | Missing |
| Communication | Doc, report, demo | Two | One |

**Done when:** every area at least 2; Correctness at 3.

## Connections

- **Back:** Lab 01 (pointers, structs, bits), Module 05 (free lists are linked lists; size classes are bucketed like hash tables; amortisation), Module 06 (alignment and caches).
- **Forward:** Module 08 (kernel heap; virtual memory explains what `mmap` really does), Module 11 (buffer pools and page layouts reuse header/footer thinking).

> **Originality note:** Heapsmith's trace format, recorder/loader tooling, visualiser, debug features, and evaluation plan were designed for this curriculum. It deliberately differs from university malloc labs (no provided driver, traces, or scoring scripts).
