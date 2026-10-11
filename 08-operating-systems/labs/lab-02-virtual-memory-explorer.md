---
title: "Lab 02 — Virtual Memory Explorer"
id: "MOD08-LAB02"
type: "lab"
module: "08-operating-systems"
phase: "D"
order: 1100
prerequisites: [MOD08-LAB01]
---

# Lab 02 — Virtual Memory Explorer

**Goal:** observe virtual memory on your real Linux machine — the layout of a process, address randomisation, lazy allocation, page faults, memory-mapped files, and copy-on-write after `fork` — so that when you implement page tables in Seedling, you know what they're for.

**Sessions:** three.

**Deliverable:** a short lab report with your measurements.

---

## Session 1 — The address space

Every process sees its own **virtual address space**: addresses that the hardware translates (using **page tables** set up by the kernel) into **physical** memory addresses. Two processes can use the same virtual address for different physical memory.

1. Write `layout.c` that prints the address of: a function (code), a global initialised variable, a global uninitialised variable, a `malloc`'d block (small and large), a local variable, and `argv`. Then it prints its own `/proc/self/maps` (open the file and copy it to stdout).
2. Match every printed address to a line of `/proc/self/maps`: which region is it in, and what are that region's permissions (`r-xp`, `rw-p`, …)?
3. Run it three times. The addresses change: **ASLR** (address space layout randomisation). [W] Why would an operating system deliberately randomise addresses? (Search "ASLR exploit mitigation" after answering.)
4. Draw the address space: code at the bottom, then data, heap growing up, shared libraries, stack at the top growing down [R].

---

## Session 2 — Laziness and page faults

Memory is managed in **pages** (4 KiB on most systems: `getconf PAGESIZE`). The kernel often doesn't give you physical memory when you ask — only when you first **touch** each page. Touching an unbacked page causes a **page fault**, which the kernel handles by finding a physical page and mapping it in.

Measure with `getrusage(RUSAGE_SELF, &ru)` → `ru.ru_minflt` (minor faults: no disk needed) and `ru.ru_majflt` (major faults: had to read from disk).

1. **Lazy allocation:** `malloc` 1 GiB (with `mmap` it's lazy for sure: `mmap(NULL, 1<<30, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0)`). Check `ru_minflt` before and after. Then write one byte in every 4 KiB page. Faults now? How many? (Predict: 1 GiB ÷ 4 KiB = 262,144.) Watch the process's memory (RSS) in `top` or `/proc/self/status` as you touch pages.
2. **Fault cost:** time touching the 1 GiB the first time vs a second pass. Divide the difference by the number of faults: the cost of one page fault in microseconds. Compare with your Magnitudes Field Guide.
3. **Memory-mapped files:** `mmap` a large file (a few hundred MB — make one with `dd`) read-only and sum its bytes. Count major faults on a cold read (drop caches first: `sync; echo 3 | sudo tee /proc/sys/vm/drop_caches` — on your own machine only) vs a warm read.

---

## Session 3 — Copy-on-write

After `fork`, the child has a "copy" of the parent's memory — but copying gigabytes on every fork would be slow. Instead, both processes share the same physical pages, marked **read-only**; when either one **writes** a page, a page fault happens and the kernel copies just that page: **copy-on-write** (COW).

1. Parent touches 256 MiB (so the pages exist). Then `fork`.
2. In the child, measure minor faults before and after **reading** all 256 MiB (prediction: almost none). Then **writing** one byte per page (prediction: one fault per page — 65,536).
3. Time `fork` itself for a parent using 10 MiB, 100 MiB, and 1 GiB. Does fork time grow with memory? (A little: page tables must still be copied.)

**[W]:** why does copy-on-write make `fork` + `exec` (Burrow's pattern) cheap, even for a big shell process?

---

## Lab report

*"What does my Linux machine actually do when I ask for memory?"* — the annotated address-space drawing, lazy-allocation fault counts, the cost of one page fault, cold vs warm mmap reads, and the COW measurements.

## Done when

- [ ] Address-space drawing with real addresses; ASLR observed.
- [ ] Fault counts and per-fault cost measured; mmap cold vs warm.
- [ ] COW measurements; report written.

## Retrieval and reflection

1. **[R]:** virtual vs physical; page; page fault (minor/major); what `mmap` does lazily; copy-on-write.
2. **[F] (spoken):** "Why can two programs use the same address without interfering?"
