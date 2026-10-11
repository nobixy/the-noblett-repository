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

## Video and course companions
Free YouTube series and Coursera/edX/MIT OCW courses for this module are listed in [courses-and-videos.md](../courses-and-videos.md#modules-0113). Use them with the [V protocol](../study-protocols.md#v--watch-actively): lectures and quizzes as second explanations; this module's own projects, not the courses' assignments.
