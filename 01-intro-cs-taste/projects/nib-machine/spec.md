---
title: "Project 1: Nib, a Tiny Computer"
module: "01-intro-cs-taste"
hours: 18
artifact: "nib.py (emulator), nasm.py (assembler), six Nib programs, a live memory viewer"
deliverable: "README + 8–10 sentence explanation of fetch–decode–execute + 4-minute recorded demo"
---

# Project 1: Nib, a Tiny Computer

| | |
| :-- | :-- |
| **Module** | 01 Intro CS Taste |
| **Time** | About 18 hours (3–4 Saturdays) |
| **Prerequisites** | Labs 00–02; Math M01–M02 (bases, binary addition); English E01+ |
| **You build** | An emulator for **Nib**, an 8-bit computer with 256 bytes of memory and 16 instructions; six programs for it, first in raw hex and then with a tiny assembler you write; and a live viewer that shows the machine's memory changing as it runs |
| **Deliverable** | README, a short written explanation, and a recorded demo |

---

## Why this matters

Every program you've ever run — a browser, a game, Python itself — is, at the bottom, a list of numbers in memory that a processor reads one at a time and obeys. That's the most important idea in computer architecture, and this project makes it concrete. You'll *be* the processor on paper first, then build one in software, then write programs for it as raw numbers, and finally build a tool (an assembler) that turns readable text into those numbers.

When you reach [Module 06](../../../06-computer-architecture/overview.md), you'll design a much bigger CPU, write its emulator and assembler, and then build it out of logic gates. Nib is the small, real version of that.

**Real-world analogs:** CPU emulators (like the ones that run old game consoles on a PC), the instruction-set manuals of real processors, assemblers.

---

## The Nib machine

Read this section slowly, twice. Then close it and try to write the instruction table from memory [R].

### State

| Part | Size | Meaning |
| :-- | :-- | :-- |
| **Memory** | 256 bytes, addresses 0x00–0xFF | Holds both the program and its data. Each byte is a number 0–255. |
| **A** (accumulator) | 1 byte | The one working register. Almost every instruction reads or writes A. |
| **PC** (program counter) | 1 byte | The address of the next instruction. |
| **Z** (zero flag) | 1 bit | Set to 1 when A becomes 0; set to 0 when A becomes anything else. |
| **C** (carry flag) | 1 bit | Set by arithmetic: 1 if an addition went past 255 or a subtraction went below 0. |
| **Output** | text | Characters and numbers the program prints. |
| **Input** | a queue of bytes | Characters the program can read (from the user or a file). |

At start: all registers and flags are 0. The program is loaded into memory starting at address 0x00. Memory not covered by the program is 0.

### Instructions

Every instruction is **exactly 2 bytes**: the **opcode** (which instruction), then the **operand** (a number the instruction uses). The opcode must be 0x00–0x0F; any other value is an **illegal instruction**, and the machine stops with an error.

`mem[x]` means "the byte at address x." All arithmetic is **modulo 256** (M03): results wrap around like an 8-digit binary odometer (M01).

| Opcode | Name | Operand | Effect | Flags |
| :-- | :-- | :-- | :-- | :-- |
| `00` | **HALT** | (ignored) | Stop the machine. | — |
| `01` | **LOAD** | address | A ← mem[address] | Z |
| `02` | **LOADI** | value | A ← value | Z |
| `03` | **STORE** | address | mem[address] ← A | — |
| `04` | **ADD** | address | A ← (A + mem[address]) mod 256 | Z, C |
| `05` | **SUB** | address | A ← (A − mem[address]) mod 256 | Z, C |
| `06` | **ADDI** | value | A ← (A + value) mod 256 | Z, C |
| `07` | **SUBI** | value | A ← (A − value) mod 256 | Z, C |
| `08` | **JMP** | address | PC ← address | — |
| `09` | **JZ** | address | if Z = 1: PC ← address | — |
| `0A` | **JNZ** | address | if Z = 0: PC ← address | — |
| `0B` | **JC** | address | if C = 1: PC ← address | — |
| `0C` | **OUT** | mode | mode 0: print A as a character (ASCII). mode 1: print A as a decimal number. Any other mode: illegal. | — |
| `0D` | **IN** | (ignored) | A ← next byte from the input queue, or 0 if the queue is empty | Z |
| `0E` | **LOADX** | address | A ← mem[mem[address]] (the byte at address holds a *pointer*: the address to read from) | Z |
| `0F` | **STOREX** | address | mem[mem[address]] ← A | — |

**Flag rules, exactly:**
- **Z** is updated by every instruction that writes A (LOAD, LOADI, ADD, SUB, ADDI, SUBI, IN, LOADX): Z = 1 if the new A is 0, else Z = 0. Other instructions leave Z unchanged.
- **C** is updated only by ADD, SUB, ADDI, SUBI. For additions: C = 1 if the true sum was greater than 255. For subtractions: C = 1 if the true result was less than 0 (a "borrow"). Other instructions leave C unchanged.

### The fetch–decode–execute cycle

The machine repeats these steps until HALT or an error:

1. **Fetch:** read the opcode at mem[PC] and the operand at mem[PC + 1].
2. **Advance:** PC ← (PC + 2) mod 256. (Before executing! So a jump simply overwrites PC.)
3. **Decode:** look up which instruction the opcode means. Illegal → stop with an error that shows the PC and the byte.
4. **Execute:** do the instruction's effect and update the flags.

### Program file format (`.nib`)

A plain text file of hex bytes:

```
# hi.nib — prints "HI"
02 48   # LOADI 'H'
0C 00   # OUT char
02 49   # LOADI 'I'
0C 00   # OUT char
00 00   # HALT
```

- Bytes are two hex digits, separated by spaces or newlines. Uppercase or lowercase.
- `#` starts a comment that runs to the end of the line.
- `@20` (an `@` followed by hex) sets the address where the following bytes go. Without it, bytes start at 0x00.

---

## Milestones

### Milestone 0 — Be the computer (paper, 1–2 hours)

Before writing any code, run a program **by hand**. Draw a table with columns: step, PC, instruction, A, Z, C, mem[0x20], output.

Trace this program completely:

```
# countdown.nib
02 03   # 00: LOADI 3
03 20   # 02: STORE 0x20
06 30   # 04: ADDI 0x30      (0x30 is the character '0')
0C 00   # 06: OUT char
01 20   # 08: LOAD 0x20
07 01   # 0A: SUBI 1
03 20   # 0C: STORE 0x20
0A 04   # 0E: JNZ 0x04
00 00   # 10: HALT
```

Questions: what does it print? How many instructions run in total (count HALT)? What are A, Z, and mem[0x20] at the end? Why does it jump back to 0x04 and not to 0x00?

<details>
<summary>Answer key (open after tracing)</summary>

It prints **321**. 21 instructions run: 2 before the loop, 6 per pass × 3 passes, plus HALT. At the end A = 0, Z = 1, C = 0, mem[0x20] = 0. It jumps to 0x04 because the setup (LOADI 3, STORE) should happen only once; the loop body starts at ADDI.

The first few rows:

| step | PC (before) | instruction | A | Z | C | mem[20] | output |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 00 | LOADI 3 | 03 | 0 | 0 | 00 | |
| 2 | 02 | STORE 20 | 03 | 0 | 0 | 03 | |
| 3 | 04 | ADDI 30 | 33 | 0 | 0 | 03 | |
| 4 | 06 | OUT 0 | 33 | 0 | 0 | 03 | 3 |
| 5 | 08 | LOAD 20 | 03 | 0 | 0 | 03 | 3 |
| 6 | 0A | SUBI 1 | 02 | 0 | 0 | 03 | 3 |
| 7 | 0C | STORE 20 | 02 | 0 | 0 | 02 | 3 |
| 8 | 0E | JNZ 04 | 02 | 0 | 0 | 02 | 3 |
</details>

**Done when:** your trace matches the key, and you can say in one sentence what the PC is for.

**Checkpoint:** [Milestone Checkpoint](<../../../04 - System/Milestone Checkpoint Template.md>). Feynman target: *the fetch–decode–execute cycle*, explained with your paper trace.

### Milestone 1 — The emulator core

Write `nib.py` with:
- a way to **load** a `.nib` file into a 256-byte memory (a list of 256 ints);
- a `step()` that does one fetch–decode–execute cycle;
- a `run(max_steps=100_000)` that steps until HALT, an error, or the step limit (so an infinite loop can't freeze your terminal);
- a command line: `python3 nib.py run program.nib` prints the program's output, then a one-line summary (`halted after 21 steps`).
- **trace mode:** `python3 nib.py trace program.nib` prints one line per step:

```
step   1  PC=00  02 03  LOADI 03   A=03 Z=0 C=0
step   2  PC=02  03 20  STORE 20   A=03 Z=0 C=0
```

**Design suggestion** (yours may differ; write down why if it does [W]): keep the machine state in a class (`class Nib:` with attributes `mem`, `a`, `pc`, `z`, `c`, `halted`, `output`, `inp`), and decode with a dictionary from opcode to a method.

**Subgoal labels [S]** for `step()`:

```python
# 1. Fetch opcode and operand at PC
# 2. Advance PC by 2, wrapping at 256
# 3. Decode: find the instruction, or raise an error for an illegal opcode
# 4. Execute: change A, memory, PC, output, or input as the instruction says
# 5. Update Z and C exactly as the flag rules say
```

**Done when:** `hi.nib` prints `HI` and `countdown.nib` prints `321` in 21 steps, and the trace matches your paper trace.

### Milestone 2 — Tests

`test_nib.py` with at least one test per instruction, plus:
- **Wraparound:** LOADI 255, ADDI 1 → A = 0, Z = 1, C = 1. LOADI 0, SUBI 1 → A = 255, Z = 0, C = 1.
- **Flags left alone:** STORE, JMP, and OUT don't change Z or C.
- **Illegal opcode:** a program containing byte `10` as an opcode stops with an error mentioning the PC.
- **PC wraparound:** a JMP to 0xFE executes the instruction at 0xFE–0xFF, then continues at 0x00.
- **Step limit:** an infinite loop (`08 00` — JMP 0) stops at the limit with a clear message.
- **Input:** IN with an empty queue gives 0 and Z = 1.

**Done when:** all pass.

### Milestone 3 — Program it in raw hex

Write these programs **in hex, by hand**, with a comment on every line. Put data (counters, strings) at addresses like 0x80 and up, using `@80`. Test each one with your emulator.

1. `initials.nib` — print your initials and a newline (character 10).
2. `count9.nib` — print `9876543210` and a newline.
3. `add.nib` — add the two numbers stored at 0x80 and 0x81 and print the result in decimal (OUT 1). Try 200 + 100: what prints, and is C set? Why?
4. `multiply.nib` — multiply the numbers at 0x80 and 0x81 by repeated addition; store the result at 0x82 and print it. Make sure 0 × anything works.
5. `hello.nib` — print a string stored at 0x90 (bytes ending with a 0 byte) using **LOADX** and a pointer at 0x8F that you move forward one byte at a time. Stop at the 0 byte (JZ).

**Done when:** all five work and are committed. Note how painful it is to compute jump addresses by hand, especially when you insert an instruction. That pain is the reason Milestone 4 exists.

**Checkpoint:** Milestone Checkpoint. Why-ladder targets:
- *Why does Nib need LOADX at all? Could you print a string without it?* (Hint: you could make a program that changes its own LOAD instruction's operand. Why might that be a dangerous idea?)
- *Why does a JMP into the middle of your data usually cause an "illegal instruction" error, and why is that a good thing?*

### Milestone 4 — `nasm.py`, a tiny assembler

Writing hex by hand is slow and error-prone. An **assembler** translates readable text into machine code.

**Input format** (`.nasm`):

```
; hello.nasm — print a string with a pointer
        LOADI msg       ; A = the ADDRESS of msg (a label used as a value)
        STORE ptr
loop:   LOADX ptr       ; A = mem[mem[ptr]]
        JZ done
        OUT 0
        LOAD ptr
        ADDI 1
        STORE ptr
        JMP loop
done:   HALT
ptr:    .byte 0
msg:    .string "HELLO, NIB"
```

**Rules:**
- One instruction or directive per line. `;` starts a comment.
- A **label** is a name followed by `:` at the start of a line; it means "the address of whatever comes next."
- Operands can be: a decimal number (`72`), hex (`0x48`), a character in single quotes (`'H'`), or a label (`loop`). HALT and IN may omit the operand (it becomes 0).
- Directives: `.byte n` puts one byte; `.string "text"` puts the characters followed by a 0 byte; `.org 0x80` moves the current address.
- Output: a `.nib` file your emulator can run, with comments showing the address and the original source line.

**How it works — two passes [S]:**
1. **Pass 1:** go through the lines, keeping a running address. Record each label's address in a dictionary. (You can't emit `JMP loop` yet if `loop` comes later — that's why you need this pass.)
2. **Pass 2:** go through again and emit bytes, now that every label's address is known.

**Errors must be helpful** (E09): unknown instruction, unknown label, number out of range (0–255), duplicate label — each with the line number and the line's text.

**Tests:** assemble each of your Milestone 3 programs rewritten in `.nasm`; the emulator must give the same output as your hand-written hex versions. Also test every error message.

**Done when:** all five programs assemble and run; errors are clear.

**Checkpoint:** Milestone Checkpoint. Why-ladder target: *why does the assembler need two passes?* (Contrast: what would a one-pass assembler have to do instead?)

### Milestone 5 — The live memory viewer

Add `python3 nib.py watch program.nib`: show memory as a 16 × 16 grid of hex bytes, with the PC's two bytes highlighted (use reverse video: `"\x1b[7m"` before and `"\x1b[0m"` after), the registers and flags beside it, and the output so far below. Advance one step each time you press Enter (or automatically every 0.2 s with `--speed`).

```
     0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F
00  02 15 03 14 0E 14 09 12 0C 00 01 14 06 01 03 14      A=4C Z=0 C=0
10  08 04 00 00 17 48 45 4C 4C 4F 2C 20 4E 49 42 00      PC=06
20  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00      out: HE
```

Watch `hello.nasm` run. Assembled, `done` is at 0x12, `ptr` at 0x14, and the string starts at 0x15. You'll see the pointer byte at 0x14 count up — 15, 16, 17, … — one step per character. That's what "a pointer" means, and you'll never forget it.

**Done when:** the viewer works and you've recorded 30 seconds of it running.

---

## Testing guidance (summary)

- **Paper first:** for any new program, trace the first 10 steps by hand, then compare with `trace`.
- **One test per instruction**, plus the edge cases in Milestone 2.
- **Round trip:** hand-written hex and assembled `.nasm` must produce identical memory images.
- **Regression tests** for every bug you fix (Lab 02).

## Common pitfalls

- **Advancing the PC after executing** instead of before. Then every jump lands 2 bytes off.
- **Forgetting `mod 256`** — A becomes 256 and Python happily keeps it.
- **Updating Z on STORE.** STORE doesn't change A, so it must not change Z.
- **Confusing an address with the value at that address.** `LOADI 0x20` puts the number 0x20 in A; `LOAD 0x20` puts *what's stored at* 0x20 in A. This confusion is the most common bug in real assembly programming. Say the difference out loud until it's automatic.
- **Data in the path of the code.** If your program runs into your data bytes, the machine executes them as instructions. Always end code with HALT and put data after it.

## Communication deliverable

Sized for E02–E05:
1. **README.md:** what Nib is, how to run the emulator, trace, watch, and the assembler, with one example of each command.
2. **"How Nib runs a program" (8–10 sentences):** the fetch–decode–execute cycle, in simple, correct sentences, using `countdown.nib` as the example. Short and correct beats long.
3. **Demo (4 minutes, recorded):** show `hello.nasm`, assemble it, run it in the viewer, and explain what the pointer is doing. End with the bug that took you longest.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Before Milestone 1, write the instruction table from memory. Before Milestone 4, write the two-pass idea from memory. |
| **F** | Fetch–decode–execute (Milestone 0); the pointer (Milestone 5) |
| **W** | LOADX vs self-modifying code; illegal opcodes as a safety net; two passes; class design choices |
| **S** | Subgoal comments for `step()` and for each assembler pass |
| **I** | Programs alternate arithmetic, loops, and memory/pointer work |
| **D** | Hex-by-hand bugs are maddening: stuck notes and breaks |
| **T** | README, explanation, demo |

## Stretch goals

- **Comparison:** write a program that reads characters with IN and prints them in uppercase (subtract 32 only for 'a'–'z': use SUB and the C flag to test "less than").
- **A stack:** reserve 0xF0–0xFF as a stack and use STOREX/LOADX with a stack pointer to implement a simple subroutine call and return. What instruction would you *add* to Nib to make this easier?
- **Breakpoints:** `watch` stops automatically when the PC reaches a chosen address.
- **Disassembler:** `nib.py dis program.nib` turns bytes back into readable instructions. Can it tell code from data? (It can't, always. Why not?)
- **Nib-to-Nib:** write a Nib program that copies itself to another part of memory and jumps there.

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Emulator | All 16 instructions and flag rules exact; trace and step limit | Works for the sample programs | Bugs in flags or PC |
| Tests | Every instruction and every listed edge case | Most | Few |
| Hex programs | All five, commented, working | Four | Fewer |
| Assembler | Two passes, labels, directives, helpful errors, round-trip tests | Works without good errors | Missing |
| Viewer | Live grid with PC highlight | Static dump | Missing |
| Communication | Clear README, explanation, and demo | Two of three | One or none |

**Done when:** every area at least 2; Emulator and Tests at 3.

## Connections

- **Back:** M01 (hex, bytes), M02 (binary addition, carry, overflow), M03 (mod 256); [Base Workshop](../../../00-foundations/math/projects/base-workshop/spec.md) (`minihex.py`, ASCII).
- **Forward:** [04](../../../04-circuits-and-digital-logic/overview.md) — you'll build the adder and the flag logic out of gates. [06](../../../06-computer-architecture/overview.md) — you'll design a 16-bit machine with many registers, a stack, subroutine calls, and memory-mapped I/O, write its emulator and assembler, and build its datapath in a logic simulator.

> **Originality note:** Nib's 16-instruction, 2-byte, accumulator-plus-pointer design and these milestones were written for this curriculum. It is deliberately different from teaching machines like the Little Man Computer (decimal mailboxes) or Hack (Nand2Tetris).
