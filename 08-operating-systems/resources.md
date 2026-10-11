---
title: "08 — Resources"
id: "MOD08-RES"
type: "reference"
module: "08-operating-systems"
phase: "D"
order: 1150
prerequisites: []
---

# 08 — Resources

*Pointers only. The projects are the course.*

## Operating systems
- **Remzi & Andrea Arpaci-Dusseau, *Operating Systems: Three Easy Pieces*** (ostep.org, free) — the best OS textbook to read alongside this module: scheduling (MLFQ, proportional share), concurrency (locks, condition variables), virtual memory (paging, TLBs), and persistence (file systems, journaling, crash consistency). Read the chapters matching each project. Its homework simulators are useful second explanations; your projects replace its programming assignments.
- **Kerrisk, *The Linux Programming Interface*** — threads, memory mapping, and file I/O chapters for Labs 01–02.

## RISC-V and Seedling
- **The RISC-V Instruction Set Manual, Volume II: Privileged Architecture** (riscv.org, free) — supervisor-mode CSRs (`sstatus`, `stvec`, `sepc`, `scause`, `stval`, `satp`, `sie`, `sip`), traps, and Sv39. Your primary reference.
- **The RISC-V SBI Specification** (github.com/riscv-non-isa/riscv-sbi-doc) — the TIME, SRST (system reset), and HSM extensions; the calling convention for `ecall` into firmware.
- **QEMU documentation:** "RISC-V 'virt' generic virtual platform" — the memory map and devices; the generic loader device.
- **"The RISC-V Reader"** (Patterson & Waterman, book) — a short, friendly tour of the ISA.
- **OSDev Wiki** (wiki.osdev.org) — practical articles on bootstrapping, linker scripts, and debugging kernels (mostly x86, but the ideas carry over).

## File systems and FUSE
- **libfuse** (github.com/libfuse/libfuse) — the `example/` folder and the `fuse.h` header comments document every operation.
- OSTEP chapters "File System Implementation" and "Crash Consistency: FSCK and Journaling".

## Concurrency
- **Allen Downey, *The Little Book of Semaphores*** (free) — puzzles that sharpen concurrency thinking.
- **ThreadSanitizer** documentation (clang.llvm.org/docs/ThreadSanitizer.html).

## Video course

*Companions, not replacements: your labs and projects are the course. Watch with the [V protocol](../study-protocols.md#v--watch-actively) (pause, predict, then blank-sheet [R]), take lectures and quizzes as second explanations, and build this module's own projects, not the course's assignments. How courses fit your sessions: [study-protocols § Using video courses](../study-protocols.md#using-video-courses).*

**Primary — MIT 6.S081 Operating System Engineering**, MIT PDOS (Robert Morris, Frans Kaashoek). Free.
- Lectures: each lecture's video is linked from the official [6.S081 lecture list](https://pdos.csail.mit.edu/6.S081/2020/schedule.html), next to the xv6 book chapter it goes with.
- **Why it fits:** 6.S081 teaches operating systems by reading and changing xv6, a small Unix kernel in C **for RISC-V**: traps, page tables (Sv39), system calls, interrupts, locks, scheduling and a logging file system. That is Seedling Kernel's exact stack, and Lab 03 already runs bare-metal RISC-V on QEMU.

**Alternate — Berkeley CS162 Operating Systems and Systems Programming**, UC Berkeley (Prof. John Kubiatowicz). Free: [YouTube playlist](https://www.youtube.com/playlist?list=PLF2K2xZjNEf97A_uBCwEl61sdxWVP7VWC) · [lecture page with slides](https://people.eecs.berkeley.edu/~kubitron/cs162/lectures.html).
- **Why:** a broader, concept-first course in the same order as OSTEP: threads, synchronization, scheduling, memory, file systems. Use it when 6.S081 assumes too much, and for Scheduler Arena, where it has more on scheduling policy.

### Lecture-to-vault map

6.S081 numbers are the LEC numbers on the official lecture list; CS162 numbers are lecture numbers.

| Vault item | MIT 6.S081 (primary) | Berkeley CS162 (alternate) |
| :-- | :-- | :-- |
| [Lab 01 — Threads and races](labs/lab-01-threads-and-races.md) | LEC 10 Multiprocessors and locking · LEC 13 sleep&wakeup | Lecture 3 Threads and Processes · Lectures 6–9 Synchronization |
| [Lab 02 — Virtual memory explorer](labs/lab-02-virtual-memory-explorer.md) | LEC 4 Page tables · LEC 8 Page faults | Lectures 13–17 Memory, address translation, caching and paging |
| [Lab 03 — Bare-metal RISC-V](labs/lab-03-bare-metal-riscv.md) | LEC 5 Calling conventions and stack frames RISC-V · LEC 6 Isolation & system call entry/exit | Lecture 2 Four Fundamental OS Concepts |
| [Scheduler Arena](projects/scheduler-arena/spec.md) | LEC 11 Thread switching | Lectures 10–12 Scheduling (12 includes deadlock) |
| [Tagfs](projects/tagfs/spec.md) (FUSE, journaling) | LEC 14 File systems · LEC 15 Crash recovery · LEC 16 File system performance and fast crash recovery | Lecture 4 Files and I/O · Lectures 19–21 File systems, reliability and transactions |
| [Seedling Kernel](projects/seedling-kernel/spec.md) | LEC 1 Introduction and examples · LEC 3 OS organization and system calls · LEC 4 Page tables · LEC 6 Isolation & system call entry/exit · LEC 9 Interrupts · LEC 11 Thread switching · LEC 14 File systems | Lecture 5 IPC, Pipes and Sockets |

**Note:** a YouTube playlist of 6.S081 exists, but it is a third-party re-upload; use the links on the official lecture list.
