---
title: "06 — Resources"
id: "MOD06-RES"
type: "reference"
module: "06-computer-architecture"
phase: "C"
order: 980
prerequisites: []
---

# 06 — Resources

*Pointers only. Your ISA manual, emulator, datapath, and compiler are the course.*

## Architecture
- **Harris & Harris, *Digital Design and Computer Architecture: RISC-V Edition*** (book) — chapters 6 (architecture), 7 (microarchitecture: single-cycle, multi-cycle, pipelined datapaths), and 8 (memory systems and caches). The best companion for this module.
- **Patterson & Hennessy, *Computer Organization and Design: RISC-V Edition*** (book) — the classic; chapters 2, 4, 5.
- **The RISC-V Instruction Set Manual, Volume I: Unprivileged** (riscv.org, free) — a beautifully reasoned real ISA manual. Its commentary boxes explain *why* each design choice was made; read them before writing your own rationale section. (Also excellent Level 4 copywork.)

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

## Video course

*Companions, not replacements: your labs and projects are the course. Watch with the [V protocol](../study-protocols.md#v--watch-actively) (pause, predict, then blank-sheet [R]), take lectures and quizzes as second explanations, and build this module's own projects, not the course's assignments. How courses fit your sessions: [study-protocols § Using video courses](../study-protocols.md#using-video-courses).*

**Primary — Digital Design and Computer Architecture**, ETH Zürich (Prof. Onur Mutlu). Free on YouTube: [lecture playlist](https://www.youtube.com/playlist?list=PL5Q2soXY2Zi-EImKxYYY1SZuGiOAOBKaf) · all of Mutlu's courses: [lecture videos page](https://people.inf.ethz.ch/omutlu/lecture-videos.html).
- **Why it fits:** the course uses Harris & Harris, *Digital Design and Computer Architecture*, this module's main companion, and walks the same path as your projects: instruction set architecture, single-cycle and multi-cycle microarchitecture, pipelining and hazards, then memory hierarchy and caches. It is deep and complete; watch the lectures that match your current project, not the whole course.

**Alternate — Building an 8-bit breadboard computer**, Ben Eater (YouTube). Free: [playlist](https://www.youtube.com/playlist?list=PLowKtXNTBypGqImE405J2565dvjafglHU).
- **Why:** the gentle version of a datapath and control unit, built from real chips. The control-logic and microcode videos are the clearest free explanation of how instructions become control signals, exactly the step in Kestrel Datapath.

### Lecture-to-vault map

| Vault item | ETH DDCA, Mutlu (primary) | Ben Eater 8-bit (alternate; playlist positions) |
| :-- | :-- | :-- |
| [Lab 01 — Reading real machine code](labs/lab-01-reading-real-machine-code.md) | Lecture 9b Assembly Programming | — |
| [Lab 02 — Digital simulator tour](labs/lab-02-digital-simulator-tour.md) | Lecture 2 Combinational Logic I · Lecture 3 Combinational Logic II · Lecture 4 Sequential Logic Design | videos 6–13 (latches, flip-flops, bus, registers) |
| [Lab 03 — Pipelines and hazards](labs/lab-03-pipelines-and-hazards.md) | Lecture 12 Pipelining · Lecture 13 Pipelined Processor Design: Data & Control Dependence Handling | — |
| [Kestrel ISA](projects/kestrel-isa/spec.md) (ISA, emulator, assembler) | Lecture 7 Von Neumann Model & Instruction Set Architectures · Lecture 8 Instruction Set Architectures II · Lecture 9 ISA and Microarchitecture (Tradeoffs) | videos 40–44 (microcode, more instructions, flags, conditional jumps) |
| [Kestrel Datapath](projects/kestrel-datapath/spec.md) (CPU in gates) | Lecture 10 Microarchitecture Fundamentals and Design · Lecture 11 Multi-Cycle Microarchitecture Design | videos 28–29 (program counter) · 35–38 (CPU control logic) |
| [Cache Simulator](projects/cache-sim/spec.md) | Lecture 21 Memory Organization & Technology · Lecture 22 Memory Hierarchy and Caches · Lecture 23 Cache Design and Management | — |
| [Ember Compiler](projects/ember-compiler/spec.md) | — (see Gaps) | — |

**Gaps:** neither course teaches compilers. For Ember, *Crafting Interpreters* (above) stays the second explanation. Nand to Tetris Part II (Coursera) covers a compiler, but it is now a Coursera subscription course: only a preview is free. ([DR-010](<../04 - System/DR-010 - Project-First Original Curriculum.md>) already replaced its projects with Kestrel and Ember.)
