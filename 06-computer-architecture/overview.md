---
title: "06 — Computer Architecture"
id: "MOD06"
type: "overview"
module: "06-computer-architecture"
phase: "C"
order: 900
prerequisites: [MOD04, MOD05, MOD01-PRJ-nib-machine, E10]
checkpoints: [MOD06-CLOSE]
tags: [module, architecture, hardware, compilers]
---

# 06 — Computer Architecture

**Design your own computer, build it from gates, and compile a language to it.** In this module you design **Kestrel**, a 16-bit processor: its instruction set, its emulator, its assembler, its calling convention, its memory-mapped screen and keyboard. Then you build its datapath out of the ALU and registers you made in Gatesmith and run the same programs on the hardware. Then you write **Ember**, a small programming language with an interpreter and a compiler that targets Kestrel. Finally you measure how memory caches make or break performance.

At the end, a program you wrote in your own language, compiled by your own compiler, runs on a processor you designed, built from gates you simulated. That is the whole stack, from logic to language, and it's yours.

---

## Prerequisites

- [04 Circuits and Digital Logic](../04-circuits-and-digital-logic/overview.md) — especially [Gatesmith](../04-circuits-and-digital-logic/projects/gatesmith/spec.md) (your ALU and register file).
- [05 DSA](../05-data-structures-and-algorithms/overview.md) (hash tables for symbol tables, trees for syntax, measurement).
- [Nib](../01-intro-cs-taste/projects/nib-machine/spec.md) (reread its spec and your code first: Kestrel is its big sibling).
- English **E10**: Kestrel's ISA reference is the most important technical document you'll have written so far.

## Objectives

By the end you will be able to:
1. Design an instruction set under constraints, and defend each decision with trade-offs.
2. Write a cycle-accurate emulator and a two-pass assembler with labels, directives, and macros.
3. Define and follow a calling convention (stack, return addresses, saved registers) and explain how function calls work in hardware.
4. Build a single-cycle and a multi-cycle datapath with a control unit, and explain the performance equation.
5. Explain pipelining and its hazards.
6. Write a lexer, a recursive-descent parser, a tree-walking interpreter, and a code generator for a small language.
7. Explain caches (hits, misses, locality, associativity, replacement) and predict program performance from memory access patterns.
8. Read real x86-64 or ARM machine code produced by a compiler.

## Sequence and time

| Order | Item | Concepts |
| :-- | :-- | :-- |
| 1 | [Lab 01 — Reading Real Machine Code](labs/lab-01-reading-real-machine-code.md) | compilers' output; registers; calls; Compiler Explorer |
| 2 | **[Kestrel ISA](projects/kestrel-isa/spec.md)** — ISA, emulator, assembler, conventions, I/O | instruction sets, encoding, addressing, flags, stacks, calls, memory-mapped I/O |
| 3 | [Lab 02 — A Tour of the Digital Simulator](labs/lab-02-digital-simulator-tour.md) | graphical simulation, RAM/ROM, splitters, loading hex |
| 4 | **[Kestrel Datapath](projects/kestrel-datapath/spec.md)** — the CPU in gates | datapath, control unit, single- vs multi-cycle, CPI, clock period |
| 5 | [Lab 03 — Pipelines and Hazards on Paper](labs/lab-03-pipelines-and-hazards.md) | pipelining, data and control hazards, forwarding, stalls, branch prediction |
| 6 | **[Ember Compiler](projects/ember-compiler/spec.md)** — a language for your CPU | lexing, parsing, ASTs, scopes, interpretation, code generation, calling conventions |
| 7 | **[Cache Simulator](projects/cache-sim/spec.md)** — memory performance | locality, cache organisation, replacement, traces, measurement |

Kestrel ISA must come first; Datapath and Ember can be done in either order (or interleaved, alternating hardware and compiler build sessions — but only one counts as your open build project at a time; see rule 2 in [Start Here](<../00 - Start Here.md>)); the Cache Simulator last.

## How the projects connect

```
                 Ember source (.em)
                        │  Ember compiler (lexer → parser → AST → codegen)
                        ▼
                 Kestrel assembly (.kasm)
                        │  Kestrel assembler (two passes)
                        ▼
                 Kestrel machine code (.khex)
              ┌─────────┴──────────┐
              ▼                    ▼
   Kestrel emulator (Python)   Kestrel datapath (gates, in Digital or Gatesmith)
              │                    │
              └── memory trace ──► Cache simulator
```

The **emulator is the reference**. The datapath must produce the same results, cycle by cycle where possible. The compiler's output must produce the same results as Ember's interpreter. Every arrow is a place where two independent implementations are compared — the most powerful testing idea in this curriculum.

## How the study methods run through this module

| Protocol | In this module |
| :-- | :-- |
| **R** | Blank-sheet the ISA table, the datapath diagram, the calling convention, and the compiler pipeline at each milestone. Milestone Checkpoints. Study Deck cards for encodings and the performance equation. |
| **F** | Recorded explanations: how a function call works in hardware; why pipelines stall; how a parser builds a tree; why caches work at all (locality). |
| **W** | The ISA design doc is a *long* why-ladder: every field width, every instruction kept or cut, every convention, defended against at least one alternative. |
| **S** | Subgoal labels for the fetch–decode–execute cycle, the assembler's passes, code generation for each kind of expression and statement. |
| **I** | Hardware and compiler work interleave; Study Deck sessions mix architecture with earlier modules. |
| **D** | CPU bugs are subtle (one wrong control bit). The emulator-vs-hardware comparison localises them; stuck notes for the rest. |
| **T** | The ISA reference manual; design docs; a lab report on caches; demos — including a final "whole stack" demo. |

## Connections

- **Back:** Nib (01), Gatesmith and Lab 03 (04), Module 02 (parsers: Worldfile, Truth Engine), Module 05 (hash tables for symbols; measurement), M07 (two's complement), [Magnitudes Field Guide](../00-foundations/math/projects/magnitudes-field-guide/spec.md) (memory latencies — now you'll see why).
- **Forward:** Module 07 (real machine code in C: pointers, the stack, the heap; your cache knowledge applied to real loops), Module 08 (your kernel runs on RISC-V, a real ISA you'll now find familiar; interrupts and privilege), Module 13 (the capstone's "down to the metal" option).

## Module close

1. **Cumulative retrieval [R]:** draw the Kestrel datapath; write the ISA table; walk a function call through the stack; draw the compiler pipeline; explain hits and misses with a diagram.
2. **The whole-stack demo [T]:** a short recording: an Ember program → compiled → assembled → running on the emulator **and** on the gate-level datapath, with the same output; then its cache behaviour.
3. **Reflection:** reread your Nib spec and code. Write half a page: what Nib taught you, and what Kestrel changed.
4. Tick the module in [Start Here](<../00 - Start Here.md>).

**Resources:** books, docs, and tools for this module are in [resources.md](resources.md) (pointers only — the projects are the course).

**Next:** [07 Systems Programming](../07-systems-programming/overview.md).
