---
title: "08 — Operating Systems"
id: "MOD08"
type: "overview"
module: "08-operating-systems"
phase: "D"
order: 1080
prerequisites: [MOD07, MOD06, MOD05, E10]
checkpoints: [MOD08-CLOSE]
tags: [module, os, kernel]
---

# 08 — Operating Systems

**Write the program that runs all the other programs.** You'll simulate and compare CPU schedulers, build a file system that runs on your real Linux machine through FUSE, and then write **Seedling**: a small operating-system kernel for a real processor architecture (64-bit RISC-V), booting in an emulator. Seedling prints to a serial console, handles interrupts and timer ticks, manages physical memory and page tables, switches between threads, runs user programs in a protected mode, offers system calls, reads files from a ramdisk, and runs a tiny shell — all code you wrote.

---

## Prerequisites

- [07 Systems Programming](../07-systems-programming/overview.md) (C, pointers, system calls, Heapsmith, Burrow).
- [06 Computer Architecture](../06-computer-architecture/overview.md) (registers, traps, calling conventions; Kestrel makes RISC-V feel familiar).
- [05 DSA](../05-data-structures-and-algorithms/overview.md) (queues, heaps, trees).
- English E10.

## Objectives

By the end you will be able to:
1. Explain and compare scheduling policies with metrics, and connect them to Linux's real scheduler.
2. Write correct concurrent code with threads, locks, and condition variables, and find races with ThreadSanitizer.
3. Explain virtual memory — address spaces, page tables, page faults, copy-on-write — and observe it on Linux.
4. Implement a file system with directories, metadata, and crash safety, and mount it on Linux.
5. Boot a kernel on RISC-V; handle traps, interrupts, and exceptions; manage physical pages and Sv39 page tables.
6. Implement threads, context switches, and preemptive scheduling in a kernel.
7. Run user programs in user mode and serve their system calls.
8. Test a kernel automatically, and debug it with GDB.

## Sequence and time

| Order | Item | Concepts |
| :-- | :-- | :-- |
| 1 | [Lab 01 — Threads and Races](labs/lab-01-threads-and-races.md) | pthreads, races, mutexes, condition variables, deadlock, TSan |
| 2 | **[Scheduler Arena](projects/scheduler-arena/spec.md)** | scheduling policies, metrics, fairness, Linux CFS reality check |
| 3 | [Lab 02 — Virtual Memory Explorer](labs/lab-02-virtual-memory-explorer.md) | address spaces, /proc maps, page faults, mmap, copy-on-write |
| 4 | **[Tagfs](projects/tagfs/spec.md)** — a FUSE file system | inodes and directories, FUSE operations, journaling, crash safety |
| 5 | [Lab 03 — Bare-Metal RISC-V](labs/lab-03-bare-metal-riscv.md) | cross-compiling, linker scripts, QEMU virt, OpenSBI, UART, GDB |
| 6 | **[Seedling Kernel](projects/seedling-kernel/spec.md)** | boot, traps, timer, page allocator, threads, context switch, Sv39, user mode, syscalls, ramdisk FS, a shell |

Seedling is long; its milestones are designed so that each one ends with a kernel that boots and does something new. Expect to hit at least one bug that lasts several sections. That's normal for kernels — the [D] protocol is your friend.

## How the projects map to concepts

| Concept | Where |
| :-- | :-- |
| Scheduling | Scheduler Arena (simulation), Seedling M4 (real) |
| Concurrency | Lab 01, Seedling's spinlocks and interrupt masking, Tagfs's request handling |
| Virtual memory | Lab 02 (observed), Seedling M5 (implemented) |
| File systems | Tagfs (on Linux), Seedling M7 (in your kernel) |
| Protection | Seedling M6 (user mode, system calls) |
| Crash consistency | Tagfs's journal (and Module 11's write-ahead log) |

## How the study methods run through this module

| Protocol | In this module |
| :-- | :-- |
| **R** | Draw the trap path, a page-table walk, a context switch, and an inode layout from memory before each milestone. Study Deck cards for CSR names, PTE bits, and syscall numbers. |
| **F** | Recorded explanations: what happens on a timer interrupt; how a page table turns a virtual address into a physical one; how a crash-safe file system stays consistent. |
| **W** | Every kernel design choice in the Seedling design doc, defended; every scheduler policy's trade-off measured. |
| **S** | Subgoal labels for trap entry/exit, context switch, page-table walk, syscall dispatch. |
| **D** | Kernel bugs freeze everything with no error message. The flight recorder (Seedling M2), GDB, and the stuck-note habit are essential; never debug a kernel past three honest attempts without writing a stuck note and stepping away. |
| **I** | Labs and projects alternate between user-level Linux experiments and kernel code. |
| **T** | Design docs, a lab report for the Scheduler Arena, a file-system specification, and a kernel walkthrough demo. |

## Environment

- Linux (or WSL2). `fuse3` (and its development headers) for Tagfs.
- **RISC-V toolchain and emulator:** on Arch, `sudo pacman -S riscv64-elf-gcc riscv64-elf-binutils riscv64-elf-gdb qemu-system-riscv` (package names differ elsewhere: look for a `riscv64-unknown-elf` or `riscv64-linux-gnu` cross-compiler, and `qemu-system-misc` on Debian/Ubuntu).
- ThreadSanitizer comes with gcc and clang (`-fsanitize=thread`).

## Connections

- **Back:** Burrow (processes and signals from the user side), Heapsmith (the kernel heap), Crate (on-disk formats, fsync), Kestrel (traps and interrupts stretch goal; the idea of privileged state), Crosswalk (thread states are an FSM), Module 05 (queues, heaps, trees).
- **Forward:** [09 Networking](../09-networking/overview.md) (the kernel's network stack is what your sockets talk to; Courier lives in user space on top of UDP), [11 Databases](../11-databases/overview.md) (buffer pools, logs, and crash recovery), [13 Capstone](../13-capstone/overview.md) (the "down to the metal" option extends Seedling).

## Module close

1. **Cumulative retrieval [R]:** from a timer interrupt firing to a different user process running, every step, on one page.
2. **Kernel walkthrough [T]:** a short recorded tour of Seedling's source, file by file, for a programmer who has never seen it.
3. **Update your [Explain-a-System](../00-foundations/english/projects/explain-a-system/spec.md) explainer 2** (a key press) from scratch. You now know what an interrupt, a driver, and a kernel actually are.
4. Tick the module in [Start Here](<../00 - Start Here.md>).

**Resources:** books, docs, and tools for this module are in [resources.md](resources.md) (pointers only — the projects are the course).

**Next:** [09 Networking](../09-networking/overview.md).
