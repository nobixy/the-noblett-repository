---
title: "Project: Kestrel Datapath"
module: "06-computer-architecture"
hours: 55
artifact: "The Kestrel-16 CPU built from gates in Digital (or Gatesmith): ALU16, register file, single-cycle datapath and control unit, then a multi-cycle version — running the same machine code as your emulator, verified against it"
deliverable: "Design doc with datapath diagram and control table + performance report (single- vs multi-cycle) + 5-minute demo"
---

# Project: Kestrel Datapath

| | |
| :-- | :-- |
| **Module** | 06 Computer Architecture |
| **Time** | About 55 hours |
| **Prerequisites** | [Kestrel ISA](../kestrel-isa/spec.md) (manual and emulator done); [Gatesmith](../../../04-circuits-and-digital-logic/projects/gatesmith/spec.md); [Lab 02](../../labs/lab-02-digital-simulator-tour.md) |
| **You build** | The Kestrel processor as a circuit: a 16-bit ALU, an 8-register file, the datapath connecting them to memory, and a control unit that decodes instructions into control signals. First a **single-cycle** version (every instruction in one clock tick), then a **multi-cycle** version (one memory, a control state machine). Both run your real Kestrel programs, and both are checked against your emulator |
| **Deliverable** | Design doc, performance report, and demo |

---

## Why this matters

Your emulator says *what* each instruction does. The datapath is *how*: wires, multiplexers, registers, and a control unit setting dozens of signals every cycle. This is the moment the whole curriculum's hardware thread pays off — the gates from Lab 03, the ALU and register file from Gatesmith, the FSM design method from Crosswalk — all assembled into a working CPU.

You'll also learn the **performance equation** that governs every processor ever built:

$$\text{time} = \text{instructions} \times \text{cycles per instruction (CPI)} \times \text{clock period}$$

Single-cycle and multi-cycle designs trade these three factors against each other, and you'll measure the trade with your own programs.

**Real-world analogs:** every CPU's microarchitecture; textbook MIPS/RISC-V datapaths; FPGA soft cores.

---

## Tool choice

**Recommended: Digital** (by H. Neemann; free; Lab 02). It's graphical, has RAM/ROM components that load hex files, a terminal component, test-case tables, and can export Verilog for an FPGA later.

**Alternative: Gatesmith** (your own simulator), extended with a 16-bit RAM primitive. Harder, but you keep everything in text and can generate traces directly. Choose one and say why in your design doc [W].

Either way: build **hierarchically**. Every block is its own component with its own tests before it's used.

---

## Milestones

### Milestone 1 — Design doc and the building blocks

1. **Design doc v1** (4–6 pages): the datapath diagram (draw it by hand first, then cleanly), the list of control signals with their meanings, the **control table** (one row per opcode/function, one column per control signal), the clock and memory organisation, and what you'll measure.
2. **ALU16:** widen your ALU8 (chain two 8-bit adders through the carry, or rebuild at 16 bits). Flags exactly as the manual says. **Test** against a Python reference model: random vectors (all 2³² operand pairs is too many; use 100,000 random plus hand-picked edge cases per op).
3. **RegFile8x16:** 8 registers × 16 bits, two read ports, one write port, **r0 always reads 0** and ignores writes. Test.
4. **Sign extenders** for imm6 and imm9; the LUI combiner.

**Done when:** each block passes its tests in isolation.

**Checkpoint:** [Milestone Checkpoint](<../../../04 - System/Milestone Checkpoint Template.md>). Retrieval target: draw the datapath from memory, with every multiplexer labelled.

### Milestone 2 — Single-cycle datapath, a subset

A **single-cycle** CPU does fetch, decode, execute, memory, and write-back all within one clock period.

1. Use **separate instruction memory (ROM) and data memory (RAM)** for now. [W] Why does a single-cycle design need two memories (or a memory with two ports)?
2. **Subset first:** ALU (R-type), ADDI, LDI, LUI, BR, SYS HALT.
3. **Control unit:** combinational logic from the opcode (and cond/flags) to control signals — implement it straight from your control table (a ROM lookup is a legitimate and simple way to build it: the opcode is the address, the control word is the data [W]).
4. **PC logic:** PC + 1, or the branch target, chosen by a multiplexer driven by the branch condition evaluated from the flags.
5. Load a small program (assembled by `kasm.py`) into the ROM and run it. Watch registers change.

**Done when:** a program using only the subset (e.g. counting to 10 in a register and halting) gives the same final registers as the emulator.

### Milestone 3 — The full instruction set and devices

1. Add LD and ST (data memory address from ALU result; write-enable from control), JAL and JALR (link value PC + 1 to the register file; target selection).
2. **Memory-mapped TTY:** decode address 0xFF00 so a store sends a character to Digital's Terminal component instead of RAM. (Keyboard input and the framebuffer are stretch goals in hardware.)
3. Run `lib.kasm`'s `puts` printing "HELLO, KESTREL", and the recursive `fib(10)` printing 55.

**Done when:** both programs produce correct output on the hardware.

### Milestone 4 — Verification against the emulator

Your emulator is the reference. Make the comparison systematic:

1. Add to your emulator a mode that writes a **commit trace**: for every instruction, the PC, and any register or memory write (`PC=0012 r3←0x0007`).
2. Get the same trace from the hardware: in Digital, generate **test-case tables** from the emulator trace (expected register values after each clock), or add probes and export; in Gatesmith, emit the trace directly.
3. Run **every program** from Kestrel ISA Milestones 4–6 (where the hardware supports the devices) and compare traces. The first differing line points straight at the bug.
4. **Plant a bug** in the control table (flip one bit) and confirm the comparison catches it and points near it.

**Done when:** all supported programs match the emulator line for line.

**Checkpoint:** Milestone Checkpoint. Why-ladder target: *why compare full traces instead of only final output?*

### Milestone 5 — Timing and the multi-cycle design

1. **Critical path of the single-cycle design:** estimate it using gate delays (Gatesmith's timing analysis; or count gate levels along the slowest path — usually PC → instruction memory → register read → ALU → data memory → register write). The **clock period** must be at least this long, for **every** instruction, even quick ones. [W] Why is that wasteful?
2. **Multi-cycle design:** one memory for instructions and data; instructions take several shorter cycles (e.g. FETCH, DECODE, EXECUTE, MEMORY, WRITEBACK), skipping steps they don't need. The **control unit becomes an FSM** (Crosswalk's design method: states → diagram → table → encoding → logic). Add the internal registers it needs (instruction register, memory data register, ALU output register).
3. Count **cycles per instruction** for each instruction class and the new, shorter clock period.
4. **The performance equation on real programs:** take the instruction mix of your Life or Snake program (count instruction classes with the emulator) and compute the total time for single-cycle vs multi-cycle. Which wins for your program? Would it change for a program with more loads and stores?

**Done when:** the multi-cycle CPU passes the same trace comparisons, and the performance comparison table is done.

---

## Testing guidance

- **Unit tests for every block**, then **trace comparison** for whole programs. Never debug the whole CPU before its parts pass alone.
- **One control-table source:** generate the control ROM contents (or logic) from a single table file used in your design doc too, so they can't drift apart.
- Keep a set of tiny **directed test programs**, one per instruction, each ending with registers in a known state.

## Common pitfalls

- **Write-before-read timing** in the register file: a register written in a cycle must not corrupt that cycle's reads in a single-cycle design. Know exactly when your register file writes (on the clock edge, after the reads settle).
- **Sign-extension wires** crossed (bit order!). Gatesmith's rule: bit 0 is least significant, everywhere.
- **Branch offset relative to the wrong PC** (PC vs PC + 1): must match the manual.
- **r0** written by mistake in hardware: the register file must ignore it.
- **Huge, flat schematics:** build components; a CPU drawn as one giant diagram is impossible to debug.

## Communication deliverable

1. **Design doc** v1 → v2: datapath diagrams for both designs, the control table, the multi-cycle FSM diagram, and the verification method.
2. **Performance report** (2 pages, E10): critical-path estimates, CPI per instruction class, the performance equation applied to two of your programs, and a recommendation. Include one paragraph on what pipelining (Lab 03) would change.
3. **Demo (5 minutes):** the CPU running `fib` with the terminal printing, a trace comparison catching a planted bug, and the performance table.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | The datapath drawn from memory before Milestones 2 and 5 |
| **F** | The performance equation; how a control unit "decides" |
| **W** | Two memories; control ROM; full-trace comparison; wasted time in single-cycle |
| **S** | Control table rows as subgoals for each instruction; the FSM design method |
| **I** | Hardware design interleaved with Ember compiler work (if you're doing both) |
| **D** | One-bit control bugs: trace diff first, then a stuck note, then a break |
| **T** | Design doc, report, demo |

## Stretch goals

- **Keyboard and framebuffer in hardware:** memory-map Digital's keyboard and LED-matrix components; run Snake on your gates.
- **Pipeline:** a 5-stage pipeline with forwarding and a load-use stall (Lab 03 on paper first). Measure CPI with and without forwarding.
- **FPGA:** export Verilog from Digital and run Kestrel on a low-cost FPGA board (the open-source Yosys/nextpnr toolchain supports several boards around $15–30). Seeing your CPU print "HELLO" on real silicon is unforgettable.
- **Interrupts** in hardware (pairs with the Kestrel ISA stretch goal).

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Blocks | ALU16, RegFile, extenders, each tested alone | Most | Untested |
| Single-cycle | Full ISA + TTY; `puts` and `fib` correct | Subset | Partial |
| Verification | Trace comparison on all programs; planted bug caught | Final-output checks | None |
| Multi-cycle | FSM control; passes trace comparison | Partially working | Missing |
| Performance | Critical path, CPI, equation on two programs | Partial | Missing |
| Communication | Doc, report, demo | Two | One |

**Done when:** every area at least 2; Verification at 3.

## Connections

- **Back:** Lab 03 of Module 04 (real gates), Gatesmith (ALU, register file, timing), Crosswalk (FSM control), Kestrel ISA (the specification).
- **Forward:** Lab 03 (pipelines), the [Cache Simulator](../cache-sim/spec.md) (why memory is the bottleneck), Module 08 (a real CPU's privilege levels and interrupts), the capstone's "down to the metal" option.

> **Originality note:** the Kestrel datapath, its verification-by-trace plan, and the milestones were designed for this curriculum around your own ISA.
