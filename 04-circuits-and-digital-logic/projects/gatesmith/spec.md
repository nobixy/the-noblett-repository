---
title: "Project: Gatesmith"
id: "MOD04-PRJ-gatesmith"
type: "project"
module: "04-circuits-and-digital-logic"
phase: "B"
order: 630
prerequisites: [MOD04-LAB03, MOD02]
artifact: "gatesmith: a gate-level logic simulator with its own netlist language, hierarchy, buses, flip-flops, test vectors, VCD waveforms, and timing analysis — plus a chip library up to an 8-bit ALU and a register file"
deliverable: "README + netlist language reference + timing lab report + short demo"
---

# Project: Gatesmith

| | |
| :-- | :-- |
| **Module** | 04 Circuits and Digital Logic |
| **Prerequisites** | Lab 03 (gates, adders, flip-flops on real chips); Module 02 (parsers, recursion, testing); [Truth Engine](../../../03-discrete-math/projects/truth-engine/spec.md) helpful |
| **You build** | `gatesmith`, a simulator for digital circuits described in a text **netlist** language you implement. It checks circuits against test vectors, writes waveforms you can view in GTKWave, and measures how long signals take to settle. With it you design a library of chips, from multiplexers to an 8-bit ALU with flags and a register file — the parts of the CPU you'll design in Module 06 |
| **Deliverable** | README, a language reference, a lab report on timing, and a demo |

---

## Why this matters

On the breadboard, a 2-bit adder took an afternoon and a dozen wires. A CPU has millions of gates. Engineers design them in **hardware description languages** and test them in **simulators** long before any chip is made. Here you build both the language and the simulator, and then use them to design real circuits.

You'll learn three ideas that run through all of computer engineering:
1. **Hierarchy:** a full adder is made of half adders; an 8-bit adder of full adders; an ALU of adders and multiplexers. Design each level once, test it, and reuse it.
2. **Combinational vs sequential logic:** circuits whose outputs depend only on current inputs, vs circuits with memory (flip-flops) that change on clock edges.
3. **Timing:** gates aren't instant. The slowest path through a circuit (the **critical path**) sets how fast its clock can tick.

**Real-world analogs:** Verilog/VHDL with simulators like Icarus Verilog and Verilator; logic-synthesis timing reports; GTKWave.

---

## The netlist language (starting point)

```
# halfadder.gs
chip HalfAdder(a, b) -> (sum, carry)
  sum   = XOR(a, b)
  carry = AND(a, b)
end

chip FullAdder(a, b, cin) -> (sum, cout)
  s1, c1  = HalfAdder(a, b)
  sum, c2 = HalfAdder(s1, cin)
  cout    = OR(c1, c2)
end

chip Add8(a[8], b[8], cin) -> (s[8], cout)
  wire c[9]
  c[0] = BUF(cin)
  for i in 0..7
    s[i], c[i+1] = FullAdder(a[i], b[i], c[i])
  end
  cout = BUF(c[8])
end
```

- **Primitive gates** (built in, each with a configurable delay, default 1 time unit): `NOT, BUF, AND, OR, NAND, NOR, XOR, XNOR` (2 inputs each, except NOT/BUF), constants `0` and `1`, and `DFF(d) -> q` (positive-edge-triggered D flip-flop on the global clock `clk`).
- A **chip** has named inputs and outputs; **buses** are written `name[width]`, bits indexed `name[i]` (bit 0 = least significant), and slices `name[3:0]`.
- **Internal wires** are declared with `wire` (or created by assignment).
- `for i in a..b ... end` repeats lines with `i` substituted (an **unrolled** loop: it generates gates; it doesn't "run").
- Every wire must have exactly **one driver**. Two drivers → error; no driver → error. Combinational loops (a gate's output feeding back to its own input without passing through a DFF) → error, with the loop listed.

You may change the syntax; document every change in `NETLIST.md`.

### Test vectors

```
# FullAdder.tv
a b cin | sum cout
0 0 0   | 0   0
0 0 1   | 1   0
...
1 1 1   | 1   1
```

Buses can be written in hex: `a[8]=0x3C`. For sequential chips, each row is one clock cycle: inputs are applied, the clock rises, outputs are checked.

---

## Milestones

### Milestone 1 — Combinational simulation of primitives and flat chips

1. **Parser** for chips without buses or loops; errors with file:line:column (Module 02 Worldfile standard).
2. **Elaboration:** turn a chip into a flat **graph** of primitive gates and wires.
3. **Validation:** exactly one driver per wire; unused inputs warned; **combinational loops** found by depth-first search for cycles (Module 05 preview), reported as a list of wire names.
4. **Levelised evaluation:** sort gates in **topological order** (every gate after the gates that feed it), then evaluate once in that order.
5. **Truth-table runner:** `gatesmith table halfadder.gs HalfAdder` prints all input rows. `gatesmith test FullAdder.tv` checks vectors.

**Tests:** half adder and full adder against their vectors; each error type triggered by a small bad netlist.

**Done when:** your Lab 03 full adder, written as a netlist, passes all 8 vectors.

**Checkpoint:** [Milestone Checkpoint](<../../../04 - System/Milestone Checkpoint Template.md>). Why-ladder target: *why does topological order guarantee every gate's inputs are ready when you evaluate it, and why can't a combinational loop be ordered?*

### Milestone 2 — Hierarchy, buses, and the NAND challenge

1. Buses, indexing, slicing, `for` loops.
2. **Library chips** (each with a `.tv` test file; generate big vector files with a Python script that computes expected outputs — a **reference model**):
   - `Mux2` (1-bit), `Mux2x8` (8-bit, 2 inputs), `Mux4x8` (8-bit, 4 inputs)
   - `Decoder3` (3 inputs → 8 one-hot outputs)
   - `Add8` (ripple carry), `Inc8` (add 1), `Neg8` (two's complement negate: invert and add 1 — M07!)
   - `Eq8` (are two bytes equal?), `IsZero8`
3. **The NAND challenge:** NAND alone can build every other gate. Build `NotN, AndN, OrN, XorN` using only NAND, and prove each equals the built-in gate by **exhaustive equivalence** (`gatesmith equiv`). Then rebuild `FullAdder` from NAND-only gates and count its gates. [W] Why do chip makers care that one gate type is enough?

**Done when:** every library chip passes its vectors; the NAND versions are proven equivalent.

### Milestone 3 — The ALU

Design `ALU8`, an 8-bit arithmetic logic unit. **This ALU is the one your Kestrel CPU will use in Module 06**, so design it carefully and document it.

**Interface:** `ALU8(a[8], b[8], op[3]) -> (y[8], z, c, n, v)`

| op | Operation | y | Notes |
| :-- | :-- | :-- | :-- |
| 000 | ADD | a + b | c = carry out |
| 001 | SUB | a − b | computed as a + (NOT b) + 1; c = carry out of that addition (so **c = 1 means no borrow**) |
| 010 | AND | a AND b (bitwise) | c = 0 |
| 011 | OR | a OR b | c = 0 |
| 100 | XOR | a XOR b | c = 0 |
| 101 | PASSB | b | c = 0 (useful for "load" instructions) |
| 110 | SHL | a shifted left 1 | c = the bit shifted out (a[7]) |
| 111 | SHR | a shifted right 1 (logical) | c = the bit shifted out (a[0]) |

**Flags:** **z** = 1 if y = 0; **n** = y[7] (the sign bit in two's complement); **v** = signed overflow for ADD and SUB (the operands' signs make the result's sign impossible — e.g. positive + positive = negative), 0 otherwise.

**[W] Compare with Nib:** in Nib, C = 1 meant "a borrow happened." Here, C = 1 means "no borrow." Both conventions exist in real processors (x86 uses the first, ARM the second). Why might hardware designers prefer the second? (Hint: what does the adder produce for free when computing a + NOT b + 1?)

**Design approach [S]:** compute every operation's result in parallel (an adder for ADD/SUB with a mux choosing b or NOT b and the carry-in; AND/OR/XOR gate rows; shift wiring), then a **multiplexer** selects y by op. Flags from y and the adder.

**Verification:** a Python **reference model** of the ALU; generate test vectors for **all** 65,536 (a, b) pairs × 8 ops (524,288 rows — your simulator should handle it; if it's slow, that's a finding to optimise). Also hand-checked edge cases: 0x7F + 0x01 (v = 1), 0x80 − 0x01 (v = 1), 0x00 − 0x01 (c = 0, y = 0xFF), shifts of 0x81.

**Done when:** all 524,288 vectors pass.

**Checkpoint:** Milestone Checkpoint. Feynman target: *how the same adder does both addition and subtraction*.

### Milestone 4 — Sequential logic and waveforms

1. **DFF semantics:** all DFFs sample their inputs on the rising edge of `clk`, then all update together. (Simulate as: compute all next values first, then commit — or two different DFFs reading each other will give wrong answers. [W] Why?)
2. **Chips:** `Reg8(d[8], load) -> (q[8])` (loads d on the clock edge only when load = 1, otherwise keeps its value — a mux in front of 8 DFFs); `Counter8(reset, load, inc, d[8]) -> (q[8])`; `RegFile4x8(waddr[2], wdata[8], we, raddr1[2], raddr2[2]) -> (r1[8], r2[8])` — four 8-bit registers, one write port, two read ports (exactly what a CPU needs to read two operands at once).
3. **VCD output:** `gatesmith run Counter8.gs --cycles 20 --vcd out.vcd` writes a **Value Change Dump** file. Open it in **GTKWave** (free; `gtkwave` package) and look at your counter's waveforms. The VCD format is a short, documented text format — read its description and implement the subset you need (header, variable declarations, timestamps, value changes).

**Done when:** sequential vector tests pass for all three chips, and you've viewed a VCD of the counter and the register file in GTKWave.

### Milestone 5 — Timing: critical paths and glitches

1. **Event-driven simulation mode:** keep a priority queue of future events (time, wire, new value) ordered by time — a min-heap (`heapq`; Module 05 will have you build your own). When a gate's input changes, schedule its output change after its delay. Run until no events remain. Record the time each output **settles**.
2. **Critical path:** for `Add8`, find the worst-case input change (hint: 0xFF + 0x00 → 0xFF + 0x01 makes the carry ripple all the way) and measure the settling time. Then do it for 16- and 32-bit ripple adders. Plot settling time against width. (What growth is it — M11?)
3. **Glitches:** in event-driven mode, watch an output momentarily take a **wrong** value before settling (a **glitch**). Find one in your ALU's z flag and capture it in a VCD. [W] Why don't glitches matter in a clocked design, as long as the clock is slow enough?
4. **Carry-lookahead:** design a 4-bit carry-lookahead block (carries computed from "generate" g = a AND b and "propagate" p = a XOR b signals in parallel rather than rippling) and build `AddCLA16` from four blocks. Compare its settling time and gate count with a 16-bit ripple adder. **Faster costs more gates** — a real engineering trade-off.

**Done when:** the timing table (widths × designs) and a glitch VCD exist.

---

## Testing guidance

- **Reference models in Python** generate expected outputs; the simulator must match them exactly. Exhaustive where possible (≤ 2²⁰ input combinations), random sampling beyond.
- **Error fixtures** for every netlist error.
- **Levelised vs event-driven must agree** on final (settled) values — a differential test between your two simulation modes.

## Common pitfalls

- **Bit order:** decide once that bit 0 is the least significant, and use it everywhere — netlists, test vectors, hex parsing, VCD.
- **DFFs updating one at a time** instead of all together.
- **Slow simulation of the full ALU test:** precompute the topological order once per chip, not per vector. Represent wire values in a flat list indexed by integers, not dictionaries keyed by strings, if speed matters.
- **Uninitialised flip-flops:** decide what value DFFs start with (0 is simplest; real hardware is unpredictable — so real designs have a reset input). Document it.

## Communication deliverable

1. **README:** commands, the chip library, how to run all tests.
2. **`NETLIST.md`:** the complete language reference.
3. **Lab report** (E10 level): *"How does adder design affect speed and size?"* — ripple vs carry-lookahead, widths 8–32, settling times and gate counts, the glitch observation, and your conclusion.
4. **Demo:** a netlist, a failing vector and its fix, the ALU passing all tests, a counter in GTKWave, and the timing plot.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Before Milestone 3, draw the full adder and the ALU block diagram from memory |
| **F** | One adder doing add and subtract; why critical paths limit clock speed |
| **W** | Topological order; NAND universality; carry convention; simultaneous DFF update; glitches; speed vs gates |
| **S** | ALU design steps: compute all results → select by op → flags |
| **I** | Hardware lab (Lab 03) and simulator work alternate |
| **T** | README, reference, report, demo |

## Stretch goals

- **Netlist from Truth Engine:** convert a simplified formula into a Gatesmith chip automatically.
- **Export to Digital or Logisim:** write a converter so your chips can be opened in a graphical simulator (useful in Module 06).
- **A multiplier:** an 8×8 → 16-bit array multiplier from adders. Count its gates and critical path.
- **Verilog:** learn enough Verilog to write `ALU8` and simulate it with Icarus Verilog; compare the experience with your own tool.

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Language and parser | Buses, slices, loops, precise errors, all validation | Most | Fragile |
| Simulation | Levelised + event-driven, agreeing; loops detected | Levelised only | Wrong results |
| Library | All chips with vectors; NAND challenge proven | Most | Few |
| ALU | All 524,288 vectors pass; flags exact | Edge cases fail | Missing |
| Sequential | DFF semantics right; Reg8, Counter8, RegFile; VCD in GTKWave | Two chips | Missing |
| Timing | Ripple vs CLA table; glitch captured | Ripple only | Missing |
| Communication | README, NETLIST.md, report, demo | Most | Few |

**Done when:** every area at least 2; Simulation and ALU at 3.

## Connections

- **Back:** Lab 03 (real gates and adders), M02 (carries), M07 (two's complement, overflow), Truth Engine (equivalence), Nib (flags, from the software side).
- **Forward:** [Module 06 Kestrel](../../../06-computer-architecture/projects/kestrel-datapath/spec.md) — your ALU8 and RegFile4x8 (widened to 16 bits) become the core of the datapath; the timing analysis decides your clock period.

> **Originality note:** the netlist language, chip library, ALU specification, and milestone plan were designed for this curriculum. Building every gate from NAND is a classic idea used in many places; here it is one optional milestone inside a different project — you write the simulator itself, its timing engine, and its waveform output.
