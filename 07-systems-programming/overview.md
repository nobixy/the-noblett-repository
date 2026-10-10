---
title: "07 — Systems Programming"
module: "07-systems-programming"
hours: 190
tags: [module, systems, c]
---

# 07 — Systems Programming

**C, memory, and the operating system's front door.** You learn C — the language most operating systems, databases, and network stacks are written in — and use it to build three serious tools: **Heapsmith**, your own `malloc` and `free`; **Burrow**, a full Unix shell with job control and scripting; and **Crate**, an archive format with checksums and compression that survives corruption. Along the way you master the tools systems programmers live in: `gdb`, `valgrind`, the sanitizers, `strace`, and `perf`.

After Module 06, you know what a stack frame and a load instruction are. Here, you'll see them from C — and you'll be the one who manages every byte.

---

## Prerequisites

- [06 Computer Architecture](../06-computer-architecture/overview.md) (stack frames, memory, caches).
- [05 DSA](../05-data-structures-and-algorithms/overview.md) (lists, hash tables, measurement — now with real memory).
- [Burrow Jr.](../01-intro-cs-taste/projects/shell-sketch/spec.md) (reread it: Burrow is its full-grown form).
- English E10 (design docs for every project).

## Objectives

By the end you will be able to:
1. Write correct, warning-free C: types, pointers, arrays, strings, structs, dynamic memory, multiple files, headers, and Makefiles.
2. Explain the memory layout of a running process (code, data, heap, stack) and what pointers really are.
3. Find memory bugs with `valgrind` and AddressSanitizer, and logic bugs with `gdb`.
4. Use system calls directly: files, processes, pipes, signals — and trace them with `strace`.
5. Implement a memory allocator and analyse its fragmentation and speed.
6. Implement a shell with pipelines, redirection, job control, and a small scripting language.
7. Design a binary file format with integrity checks, and make a program robust against corrupted input (fuzzing).
8. Measure real cache effects with `perf`.

## Sequence and time

| Order | Item | Hours | Concepts |
| :-- | :-- | --: | :-- |
| 1 | [Lab 01 — C for Python Programmers](labs/lab-01-c-for-python-programmers.md) | 20 | types, pointers, arrays, strings, structs, malloc/free, headers, make |
| 2 | [Lab 02 — Debugging Tools](labs/lab-02-debugging-tools.md) | 8 | gdb, valgrind, AddressSanitizer, UBSan, warnings as errors |
| 3 | [Lab 03 — System Calls and strace](labs/lab-03-system-calls-and-strace.md) | 8 | files, fds, fork/exec/wait, pipes, signals, errno |
| 4 | [Lab 04 — Measuring the Memory Hierarchy](labs/lab-04-measuring-the-memory-hierarchy.md) | 8 | perf, loop order, strides, cache sizes, array vs list in C |
| 5 | **[Heapsmith](projects/heapsmith/spec.md)** — a memory allocator | 50 | heap layout, free lists, splitting, coalescing, size classes, fragmentation, debugging features |
| 6 | **[Burrow](projects/burrow/spec.md)** — a Unix shell | 55 | processes, pipelines, redirection, process groups, job control, signals, a script language |
| 7 | **[Crate](projects/crate/spec.md)** — an archive format | 40 | binary formats, endianness, CRC32, compression, corruption recovery, fuzzing |
| | **Total** | **~190** | |

Labs 01–02 first (C fundamentals and tools are needed everywhere), then Lab 03 before Burrow, Lab 04 any time. Projects in any order; Heapsmith first is recommended because it makes pointers second nature.

## How the projects map to concepts

| Concept | Heapsmith | Burrow | Crate |
| :-- | :-- | :-- | :-- |
| Pointers and memory layout | everything | argument vectors, job tables | buffers, structs on disk |
| Data structures in C | free lists, size-class bins | job list, token lists, AST | directory table, hash table for compression |
| System calls | `mmap`/`sbrk` | `fork, execvp, waitpid, pipe, dup2, setpgid, tcsetpgrp, sigaction` | `open, read, write, lseek, fsync, rename` |
| Robustness | heap checker, canaries, double-free detection | signals and races | checksums, fuzzing, partial recovery |
| Testing | trace-driven tests and benchmarks | script-based test harness | fuzzing, corruption injection, round trips |

## How the study methods run through this module

| Protocol | In this module |
| :-- | :-- |
| **R** | Draw memory (stack, heap, pointers, structs with padding) from memory before each session. Milestone Checkpoints. Study Deck cards for C idioms, system calls, and their failure modes. |
| **F** | Recorded explanations: what a pointer is; how `free` knows a block's size; how job control hands the terminal to a process; how CRC detects errors. |
| **W** | Every allocator policy, every shell design choice, every file-format field, defended in a design doc with measurements. |
| **S** | Subgoal comments before every C function (they matter even more in C, where one wrong step corrupts memory). |
| **C** | Copywork this module: Rob Pike's "Notes on Programming in C" and Kernighan & Pike's prose — models of short, exact technical writing. |
| **I** | C practice problems mixed with earlier modules' algorithms re-written in C. |
| **D** | Memory bugs can be baffling. Valgrind first; then the 90-minute rule and a stuck note. |
| **T** | Design docs, a measurement report per project, demos. |

## Environment

`gcc` or `clang`, `make`, `gdb`, `valgrind`, `strace`, `ltrace`, `perf`. On Arch: `sudo pacman -S base-devel gdb valgrind strace ltrace perf`. Compile everything with:

```
-std=c17 -Wall -Wextra -Wpedantic -Werror -g
```

and test with `-fsanitize=address,undefined` builds as well. Linux is required for Burrow's job control details (WSL2 works; macOS mostly works with small differences in system calls, noted where relevant).

## Connections

- **Back:** Module 06 (stack frames, calling conventions, caches), Module 05 (data structures and measurement), Burrow Jr., Base Workshop's `minihex.py` (Crate's debugging tool), Tone Loom (binary formats, endianness).
- **Forward:** [08 Operating Systems](../08-operating-systems/overview.md) — your kernel's heap uses Heapsmith's ideas; Burrow's processes are what your scheduler schedules; Crate's `fsync` and atomic rename reappear in file systems and in [11 Databases](../11-databases/overview.md). [09 Networking](../09-networking/overview.md) — Lantern can be written in C with these skills.

## Module close

1. **Cumulative retrieval [R] (60 min):** a process's memory map; a block in your allocator with its header; the system calls for a pipeline with job control; Crate's file layout.
2. **Code review [T]:** pick 200 lines from one project and review them yourself a week later as a stranger (or ask someone): memory safety, error handling, clarity. Fix what you find.
3. **Update your [Terminal Field Notes](../00-foundations/english/projects/terminal-field-notes/spec.md)** with one entry correcting something you wrote back then about processes or memory.
4. Tick the module in [Start Here](<../00 - Start Here.md>).

**Next:** [08 Operating Systems](../08-operating-systems/overview.md).
