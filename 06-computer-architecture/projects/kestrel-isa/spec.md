---
title: "Project: Kestrel ISA"
id: "MOD06-PRJ-kestrel-isa"
type: "project"
module: "06-computer-architecture"
phase: "C"
order: 940
prerequisites: [MOD01-PRJ-nib-machine, MOD04-PRJ-gatesmith, MOD06-LAB01]
artifact: "The Kestrel-16 instruction set reference manual; kestrel.py (cycle-counting emulator with devices); kasm.py (two-pass assembler with pseudo-instructions); a runtime library in assembly; a game running on the framebuffer"
deliverable: "ISA Reference Manual (your most important document so far) + test report + short demo of the game"
---

# Project: Kestrel ISA

| | |
| :-- | :-- |
| **Module** | 06 Computer Architecture |
| **Prerequisites** | [Nib](../../../01-intro-cs-taste/projects/nib-machine/spec.md); [Gatesmith](../../../04-circuits-and-digital-logic/projects/gatesmith/spec.md)'s ALU8; Lab 01 of this module |
| **You build** | **Kestrel-16**, a 16-bit computer you design. You write its instruction set reference manual, a cycle-counting emulator with a terminal, keyboard, timer, and a small pixel screen, an assembler with labels and pseudo-instructions, a calling convention with a stack, a runtime library (printing, multiplication, division) in assembly — and finally a game that runs on it |
| **Deliverable** | The ISA Reference Manual, a test report, and a demo |

---

## Why this matters

Nib had one register, 256 bytes, and no way to call a function. Real processors have many registers, large memories, a stack, function calls, and devices. Designing an instruction set teaches you what a processor *must* offer software, and what every choice costs in hardware. It's one of the best design exercises in all of computer science: every bit in a 16-bit instruction is precious, so every decision is a trade-off you must defend.

You'll do it the way real ISAs are done: with a written **reference manual** first, a **reference emulator** that defines correct behaviour, and an **assembler** — and then (in the next projects) with hardware and a compiler that must both obey the manual.

**Real-world analogs:** the RISC-V, ARM, and x86 architecture manuals; emulators like QEMU; assemblers like `as`.

---

## The constraints (must be satisfied)

Your design may differ from the baseline below in any way, but it **must** satisfy these:

1. **16-bit words** and **16-bit instructions**. (An optional second word for a large immediate is allowed — if you add one, defend it.)
2. **At least 8 general registers.**
3. The **arithmetic operations of your Gatesmith ALU** (ADD, SUB, AND, OR, XOR, PASSB, SHL, SHR) widened to 16 bits, setting Z, C, N, V with the **same conventions** (C = carry out; for SUB, C = 1 means no borrow).
4. **Load and store** with base register + offset addressing.
5. **A way to load any 16-bit constant** into a register (in at most two instructions).
6. **Conditional branches** that can test equality and both **unsigned** and **signed** less-than.
7. **Function call and return**, including calls through a register (function pointers).
8. **A stack** (by convention or by dedicated instructions).
9. **Memory-mapped devices:** a terminal (output), a keyboard (input), a cycle counter, and a pixel framebuffer (at least 64 × 32, 1 bit per pixel).
10. **HALT**, and a defined behaviour for **illegal instructions**.
11. At least **one opcode reserved** for future extension.

---

## The baseline design (a starting point you may change)

### Registers

`r0`–`r7`, 16 bits each. **`r0` always reads as 0**; writes to it are discarded (this makes MOV, CMP, NOP, and RET possible without extra opcodes). Flags Z, C, N, V. PC (16 bits).

### Memory

**Word-addressed:** 65,536 words of 16 bits (addresses 0x0000–0xFFFF). Each address holds one 16-bit word.

| Range | Use |
| :-- | :-- |
| 0x0000–0xDFFF | RAM. Programs load at 0x0000. The stack starts at 0xDFFF and grows down. |
| 0xE000–0xE07F | Framebuffer: 64 × 32 pixels, 1 bit each; each word holds 16 pixels of one row, bit 15 = leftmost (4 words per row × 32 rows = 128 words) |
| 0xFF00 | TTY_OUT — writing a value prints its low 8 bits as an ASCII character |
| 0xFF01 | TTY_IN — reading gives the next keyboard byte, or 0 if none (non-blocking) |
| 0xFF02 | CYCLES_LO — low 16 bits of the cycle counter (read-only) |
| 0xFF03 | CYCLES_HI — high 16 bits |
| 0xFF04 | FB_FLUSH — writing any value tells the emulator to redraw the screen |

### Encoding

Bits [15:12] are the **opcode**. `sext(x)` means sign-extend to 16 bits (M07).

| Op | Name | Format (bits 11…0) | Meaning | Flags |
| :-- | :-- | :-- | :-- | :-- |
| 0x0 | **ALU** | rd[11:9] ra[8:6] rb[5:3] fn[2:0] | rd ← ra *fn* rb (fn = Gatesmith ALU op: ADD 0, SUB 1, AND 2, OR 3, XOR 4, PASSB 5, SHL 6, SHR 7; shifts use ra and ignore rb) | ZCNV |
| 0x1 | **ADDI** | rd ra imm6[5:0] | rd ← ra + sext(imm6) | ZCNV |
| 0x2 | **LDI** | rd imm9[8:0] | rd ← sext(imm9) | — |
| 0x3 | **LUI** | rd imm8[7:0] (bit 8 unused) | rd ← (imm8 << 8) OR (rd AND 0x00FF) | — |
| 0x4 | **LD** | rd ra imm6 | rd ← mem[ra + sext(imm6)] | — |
| 0x5 | **ST** | rs ra imm6 | mem[ra + sext(imm6)] ← rs (the first register field is the source) | — |
| 0x6 | **BR** | cond[11:9] off9[8:0] | if cond: PC ← PC + 1 + sext(off9) | — |
| 0x7 | **JAL** | rd off9 | rd ← PC + 1; PC ← PC + 1 + sext(off9) | — |
| 0x8 | **JALR** | rd ra imm6 | t ← ra + sext(imm6); rd ← PC + 1; PC ← t | — |
| 0x9–0xE | *reserved* | | illegal for now — yours to design (see Milestone 4's stretch) | |
| 0xF | **SYS** | code[11:0] | 0 = HALT; others illegal for now | — |

**Branch conditions** (`cond`): 0 AL (always), 1 EQ (Z), 2 NE (!Z), 3 HS (C: unsigned ≥), 4 LO (!C: unsigned <), 5 LT (N ≠ V: signed <), 6 GE (N = V: signed ≥), 7 MI (N).

**Pseudo-instructions** (the assembler expands them):

| Pseudo | Expands to |
| :-- | :-- |
| `MOV rd, ra` | `ALU rd, ra, r0, ADD` (rd ← ra + 0) |
| `CMP ra, rb` | `ALU r0, ra, rb, SUB` (flags only; result discarded into r0) |
| `NOP` | `ALU r0, r0, r0, ADD` |
| `LI rd, value` | `LDI rd, lo(value)` then `LUI rd, hi(value)` (or just `LDI` if the value fits in 9 signed bits) |
| `CALL label` | `JAL r6, label` (if within range; otherwise `LI r5, label` + `JALR r6, r5, 0`) |
| `RET` | `JALR r0, r6, 0` |
| `PUSH rs` | `ADDI r7, r7, -1` then `ST rs, r7, 0` |
| `POP rd` | `LD rd, r7, 0` then `ADDI r7, r7, 1` |
| `HALT` | `SYS 0` |

### Calling convention (baseline)

| Register | Role | Saved by |
| :-- | :-- | :-- |
| r0 | zero | — |
| r1–r3 | arguments; r1 also holds the return value | caller (if it needs them after the call) |
| r4 | temporary / frame pointer (your choice — document it) | callee |
| r5 | scratch for long calls | caller |
| r6 | link register (return address) | callee, if it calls others |
| r7 | stack pointer | — |

> **Why does LDI's 9-bit immediate plus LUI cover every constant?** LDI with 0–255 sets the low byte (and zeros or sign-fills the high byte); LUI then overwrites the high byte and keeps the low byte. Work through `LI r1, 0xBEEF` and `LI r1, -1` by hand [S]. Then decide if you'd design it differently.

---

## Milestones

### Milestone 1 — The ISA Reference Manual, v1

Before any code, write `KESTREL.md` — the **reference manual**. It must be possible for someone else to write an emulator from it alone. Sections:

1. **Overview** (one paragraph) and design goals.
2. **Programmer's model:** registers, flags, memory, memory map.
3. **Instruction formats** (bit diagrams) and **every instruction**: syntax, encoding, operation in pseudocode, flags, one example with its hex encoding.
4. **Condition codes.**
5. **Illegal instructions** and HALT.
6. **Assembly language syntax**, pseudo-instructions.
7. **Calling convention** and stack layout, with a diagram of a stack frame.
8. **Devices.**
9. **Design rationale [W]:** at least **eight** decisions, each with the alternative you rejected and why. Suggested: r0 as zero vs a ninth general register; word vs byte addressing (what does byte addressing cost in encoding bits and in hardware?); flags vs compare-and-branch-in-one-instruction (RISC-V's choice); PC-relative vs absolute branches; immediate field sizes; how many registers (8 vs 16 — what would it cost in bits per instruction?); which opcodes you reserved; the link-register convention vs pushing the return address automatically.

**Done when:** the manual is complete and has had a cooling-off review [D] with the E08 checklist. (A peer review is even better.)

**Checkpoint:** [Milestone Checkpoint](<../../../04 - System/Milestone Checkpoint Template.md>). Retrieval target: write the encoding table from memory.

### Milestone 2 — The emulator

`kestrel.py`:
- Load `.khex` files (hex words, `#` comments, `@addr` directives — Nib's format, widened).
- **Fetch–decode–execute** exactly as the manual says (it's the reference: if the code and the manual disagree, fix one and record which).
- **Devices** through a memory-access function: `read(addr)` and `write(addr, value)` check the memory map.
- **Cycle counting:** 1 cycle per instruction for now (the datapath project will refine this).
- `run`, `trace` (one line per instruction: PC, encoding, disassembly, changed registers and memory), step limit, and clear errors for illegal instructions (with PC and encoding).
- A **disassembler** (needed for trace).

**Tests (`test_kestrel.py`):** at least two per instruction (from the manual's examples); every branch condition with flags set both ways; sign extension at the limits (imm6 = −32 and 31; off9 = −256 and 255); r0 writes discarded; JAL/JALR link values; device reads and writes; PC wrap-around at 0xFFFF.

**Done when:** all tests pass.

### Milestone 3 — The assembler

`kasm.py`, two passes (Nib's design, grown up):
- Labels; `.org`, `.word v1, v2, …`, `.string "text"` (one character per word, ending with 0 — or packed two per word; decide [W]), `.equ NAME value`, `.space n`.
- **Expressions** in operands: numbers (decimal, `0x`, `0b`, `'c'`), labels, `+`, `-`, and `lo(x)`, `hi(x)`.
- All pseudo-instructions, including **`LI`'s one-or-two-instruction choice** — which changes code size, which changes label addresses. [W] Why does this complicate a two-pass assembler, and how do you solve it? (Hint: decide the size in pass 1 conservatively, or iterate until sizes stop changing.)
- **Range checking** with clear errors: "branch to `loop` is 300 words away; BR reaches ±256 — use JMP via LI + JALR" (E09-quality messages).
- A **listing file**: address, encoding, source line.

**Tests:** every instruction assembled and disassembled back (round trip); every error message; a 200-line program assembles identically twice.

**Done when:** tests pass and your Milestone 4 library assembles.

### Milestone 4 — The runtime library and the stack

Write in Kestrel assembly (`lib.kasm`), following the calling convention:
- `putc` (r1 = char), `puts` (r1 = address of a 0-terminated string), `getc` (non-blocking; returns 0 if none).
- `mul` (r1 × r2 → r1) by **shift-and-add** (the binary version of long multiplication, M03).
- `udiv` and `umod` by **shift-and-subtract** (binary long division, M03).
- `print_udec` and `print_dec` (signed: M07) using `udiv`/`umod` by 10.
- `memcpy`, `memset`.

**Prove the stack works:** a recursive `fact(n)` and a recursive `fib(n)` in assembly, which save the link register and their arguments on the stack. Run `fib(15)`; check the result (610) and count cycles.

**Tests:** an assembly test harness: for each routine, a small test program that calls it with known inputs and prints results; the Python test compares the output with expected values (golden files). Test `mul` and `udiv` against Python on 1,000 random pairs (generate the test program automatically).

**Done when:** all routines pass and recursion works.

**Checkpoint:** Milestone Checkpoint. Feynman target: *what happens, step by step, in registers and on the stack, when `fib(3)` calls `fib(2)` and returns*. Draw the stack at its deepest point [R].

**Stretch (design):** use a reserved opcode for something that would make your library smaller or faster (hardware `PUSH`/`POP`, a multiply instruction, a shift-by-n). Update the manual with the rationale, implement it in the emulator and assembler, and **measure** the difference in cycles and code size. This is how real ISAs evolve: by measuring what programs actually do.

### Milestone 5 — Devices, and the screen

1. **Terminal and keyboard:** TTY_OUT prints; TTY_IN reads keys without blocking (on Linux, put the terminal in raw mode with `termios`/`tty` and restore it on exit — always, even after an error).
2. **Framebuffer:** on FB_FLUSH, draw the 64 × 32 pixels in the terminal (Unicode half blocks `▀ ▄ █` show two pixel rows per text row, so 64 × 16 characters), or in a window (pygame or Tkinter), or as a PPM image file per frame.
3. **Cycle counter** readable as two words.
4. **Speed:** how many Kestrel instructions per second does your emulator run? (Module 05 measurement.) If it's too slow for a game, profile it (`python -m cProfile`) and speed up the hot loop (decode tables instead of if-chains, local variables, avoiding objects per instruction).

**Done when:** a test program draws a moving pixel that you steer with the keyboard.

### Milestone 6 — A real program

Write **one** of these in Kestrel assembly (about 200–500 lines):
- **Conway's Game of Life** on the 64 × 32 framebuffer, wrapping at the edges (`%` — or, since 64 and 32 are powers of 2, a bitwise AND: why does that work? [W]), with a glider and a few random seeds.
- **Snake** with keyboard control, growing tail (a ring buffer! Module 05 Lab 03), and score printed to the terminal.

Measure instructions per frame (using the cycle counter). Find the hottest loop (instrument the emulator to count executions per address — a **profiler** for your own CPU) and optimise it. Report before and after.

**Done when:** the game runs, and you have before/after numbers for one optimisation.

---

## Testing guidance

- **The manual is the specification**; every test cites the manual section it checks.
- **Golden programs** (expected terminal output) for everything above the instruction level.
- **Generated tests** (random operands, compared with Python) for arithmetic routines.
- Keep every program you write as a regression test: it will run again on the datapath and as compiler output.

## Common pitfalls

- **Sign extension bugs** in immediates — the most common emulator bug. Test the boundaries.
- **PC + 1 vs PC:** branches and JAL are relative to the *next* instruction in the baseline. Be consistent everywhere (manual, emulator, assembler).
- **Writing r0** must not change it — including through LD and JAL.
- **Forgetting to save r6** in a function that calls another: the return address is overwritten, and RET jumps to the wrong place (usually an infinite loop).
- **Raw terminal mode** left on after a crash: always restore it in a `finally` block.
- **Word vs byte thinking:** strings take one word per character in the baseline. Count accordingly.

## Communication deliverable

1. **`KESTREL.md` — the ISA Reference Manual** (v1 at Milestone 1, final at the end with a change history). This is graded as a technical document: complete, precise, consistent, and readable. Aim for the quality of the real manuals you sampled in copywork Level 4.
2. **Test report** (1 page): what is tested, how, and coverage per instruction.
3. **Demo:** the manual's structure, the assembler's listing, `fib` in the trace, and the game running.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Encoding table from memory; the stack at `fib`'s deepest point |
| **F** | Function calls in hardware; how LDI + LUI build constants |
| **W** | Eight design rationales in the manual; packed strings; two-pass sizing; power-of-two wrap-around |
| **S** | Fetch–decode–execute; assembler passes; shift-and-add/subtract |
| **I** | Hardware thinking, assembly programming, and tooling alternate |
| **C** | Copywork during this project: passages from a real ISA manual (the RISC-V unprivileged spec's introduction is excellent prose) |
| **T** | The manual, test report, demo |

## Stretch goals

- **Interrupts:** a timer device that interrupts the CPU every N cycles; a vector address, saved PC, and a return-from-interrupt instruction. (This is exactly what your kernel in Module 08 will rely on.)
- **Byte addressing:** redesign for byte addresses with 8-bit loads and stores; compare code size and complexity.
- **A monitor program:** a tiny command-line program *running on Kestrel* that lets you inspect and edit memory and jump to addresses.

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Manual | Complete, precise, 8+ rationales, someone else could build from it | Mostly complete | Gaps |
| Emulator | Matches manual exactly; trace; devices; tests for every instruction and edge | Works | Edge bugs |
| Assembler | Two passes, expressions, all pseudos, range errors, listing, round trips | Works | Fragile |
| Library and stack | All routines; recursion; generated tests | Most | Few |
| Devices and game | Keyboard, framebuffer, a working game, profiled and optimised | Game runs | Missing |
| Communication | Manual + test report + demo | Two | One |

**Done when:** every area at least 2; Manual and Emulator at 3.

## Connections

- **Back:** Nib (everything, grown up), Gatesmith (the ALU and its flag conventions), M03 (long multiplication and division in binary), M07 (sign extension, two's complement), Module 05 (ring buffers, profiling).
- **Forward:** [Kestrel Datapath](../kestrel-datapath/spec.md) (this manual is the hardware's specification), [Ember Compiler](../ember-compiler/spec.md) (this calling convention is the compiler's target), [Cache Simulator](../cache-sim/spec.md) (this emulator produces memory traces), Module 08 (interrupts and privilege on RISC-V).

> **Originality note:** the Kestrel constraints, baseline encoding, memory map, and milestones were designed for this curriculum. They deliberately differ from teaching ISAs such as Hack (Nand2Tetris) and LC-3, and from RISC-V, while teaching the same ideas.
