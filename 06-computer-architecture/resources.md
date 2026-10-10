---
title: "06 — Resources"
module: "06-computer-architecture"
---

# 06 — Resources

*Pointers only. Your ISA manual, emulator, datapath, and compiler are the course.*

## Architecture
- **Harris & Harris, *Digital Design and Computer Architecture: RISC-V Edition*** (book) — chapters 6 (architecture), 7 (microarchitecture: single-cycle, multi-cycle, pipelined datapaths), and 8 (memory systems and caches). The best companion for this module.
- **Patterson & Hennessy, *Computer Organization and Design: RISC-V Edition*** (book) — the classic; chapters 2, 4, 5.
- **The RISC-V Instruction Set Manual, Volume I: Unprivileged** (riscv.org, free) — a beautifully reasoned real ISA manual. Its commentary boxes explain *why* each design choice was made; read them before writing your own rationale section. (Also excellent Level 4 copywork.)
- **ETH Zürich, Digital Design and Computer Architecture** (Onur Mutlu's lectures, YouTube, free) — deep lectures on pipelining, caches, and memory.

## Tools
- **Digital** (github.com/hneemann/Digital) — documentation is built into the program (*Help*).
- **Compiler Explorer** (godbolt.org).
- **Valgrind's Lackey and Cachegrind** — valgrind.org documentation.

## Compilers (Ember)
- **Robert Nystrom, *Crafting Interpreters*** (craftinginterpreters.com, free) — Part II (a tree-walking interpreter) is the perfect second explanation for Ember Milestones 2–3. Part III builds a bytecode VM; skim it for ideas, don't copy its design.
- **Niklaus Wirth, *Compiler Construction*** (free PDF from ETH) — a short, complete book on recursive-descent compilers for a small language; chapters 1–9.
- **Abdulaziz Ghuloum, "An Incremental Approach to Compiler Construction"** (paper, free) — the idea of growing a compiler one feature at a time, always working.

## Caches
- **Ulrich Drepper, "What Every Programmer Should Know About Memory"** (free PDF) — long and detailed; read sections 3 (caches) and 6 (what programmers can do) after the Cache Simulator.

## Video and course companions
Free YouTube series and Coursera/edX/MIT OCW courses for this module are listed in [courses-and-videos.md](../courses-and-videos.md#modules-0113). Use them with the [V protocol](../study-protocols.md#v--watch-actively): lectures and quizzes as second explanations; this module's own projects, not the courses' assignments.
