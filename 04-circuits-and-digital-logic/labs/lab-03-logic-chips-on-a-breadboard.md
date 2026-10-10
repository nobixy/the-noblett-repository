---
title: "Lab 03 — Logic Chips on a Breadboard"
module: "04-circuits-and-digital-logic"
hours: 14
type: maker-lab
---

# Lab 03 — Logic Chips on a Breadboard

**Goal:** turn logic into hardware. Verify gate truth tables with switches and LEDs, build a half adder and a full adder that really add, drive a binary counter from your 555 clock, and discover switch bounce.

**Time:** about 14 hours, in four sessions.

**Deliverable:** a working 2-bit adder on the breadboard, a counting display, and a short lab report on switch bounce.

---

## Session 1 — Gates and datasheets (3 hours)

### 74HC chips

The **74HC** family is a long-lived standard set of logic chips. Each chip holds several gates. Every chip needs power: **pin 14 to +5 V, pin 7 to ground** for the 14-pin chips used here (check each datasheet — always). The **notch** or dot on the chip marks pin 1; pins count anticlockwise from there, viewed from the top.

| Chip | Contents |
| :-- | :-- |
| 74HC00 | four 2-input NAND gates |
| 74HC04 | six NOT gates (inverters) |
| 74HC08 | four 2-input AND gates |
| 74HC32 | four 2-input OR gates |
| 74HC86 | four 2-input XOR gates |
| 74HC74 | two D flip-flops |
| 74HC161 | a 4-bit synchronous counter |

**High and low:** for 74HC at 5 V, roughly: above 3.5 V reads as **1**, below 1.5 V reads as **0**. In between is undefined — avoid it.

### Never leave an input floating

An input connected to nothing **floats**: it picks up noise and reads randomly as 0 or 1. Every input must be tied to a definite level. For a switch input, use a **pull-down resistor** (10 kΩ to ground): the input reads 0 until the switch connects it to +5 V. [W] Why a resistor and not a plain wire to ground? (What happens when the switch then connects +5 V straight to ground?)

### Verify truth tables

For each of AND, OR, XOR, NAND, NOT: wire one gate with two switch inputs (each with a pull-down) and an LED (+ 330 Ω) on the output. Go through all input combinations and record the table. Compare with Module 03 Unit 1.

**Unused inputs:** tie unused gate inputs on each chip to ground. (Floating unused inputs on CMOS chips can make them draw extra current and misbehave.)

---

## Session 2 — Adders (4 hours)

### Half adder

Adding two bits a + b (M02): the sum bit is 1 when exactly one is 1; the carry is 1 when both are 1.

| a | b | carry | sum |
| :-- | :-- | :-- | :-- |
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 0 |

So **sum = a XOR b** and **carry = a AND b**. One 74HC86 gate and one 74HC08 gate. Build it; test all four rows.

### Full adder

To add multi-bit numbers, each column also adds a **carry in** from the column to its right (M02 Part 6). A **full adder** adds three bits a, b, c_in:
- **sum** = a XOR b XOR c_in
- **c_out** = (a AND b) OR (c_in AND (a XOR b))

It's two half adders and an OR gate. Draw it first. Then **check it with Truth Engine:** is `(a and b) or (c and (a xor b))` equivalent to "at least two of a, b, c are 1"? (It should be — [W] why does that make sense for a carry?)

Build the full adder and test all **8** rows.

### 2-bit adder

Chain two full adders: the carry out of bit 0 feeds the carry in of bit 1 (for bit 0, tie carry in to ground). Inputs: four switches (a₁a₀ and b₁b₀). Outputs: three LEDs (carry, s₁, s₀). Test all 16 combinations, checking against M02 binary addition. You've built the core of a computer's arithmetic.

> **[W] Why is this called a "ripple-carry" adder, and why does it get slower as it gets wider?** The top bit can't know its answer until the carry has rippled through every bit below it. Each gate takes a few nanoseconds; a 64-bit ripple adder waits for 64 stages. You'll measure this in Gatesmith and see the faster alternative (carry-lookahead).

---

## Session 3 — Clocks, flip-flops, counting (4 hours)

### The D flip-flop: one bit of memory

A **D flip-flop** (74HC74) copies its D input to its Q output **at the moment the clock rises** (goes from 0 to 1), and holds that value until the next rising edge — no matter what D does in between. It **remembers** one bit. Registers, counters, and every memory in a CPU are built from this idea.

Build: D from a switch (with pull-down), clock from your 555 (Lab 02), Q to an LED. Change D quickly between ticks: the LED only changes on the tick. Tie the flip-flop's preset and clear pins high (check the datasheet; they're active-low).

### A binary counter

The **74HC161** counts in binary on each rising clock edge. Wire its clock to the 555, its four outputs (Q₀–Q₃) to four LEDs, and set its control pins so it counts (datasheet: tie the enable pins high, the load and clear pins high). Watch it count 0000 → 1111 → 0000 at one step per second (M01's odometer, in silicon).

### Switch bounce

Now replace the 555 clock with a **pushbutton** (with a pull-down). Press it once. Does the counter go up by exactly 1?

Often it jumps by 2, 3, or more. Mechanical switch contacts **bounce**: they make and break contact several times over a few milliseconds before settling. The counter sees every bounce as a clock edge.

**Experiment:** press 20 times, recording how many counts each press made. (If you have a logic analyser, capture a press and *see* the bounces.)

**Fixes** (try one): an RC filter on the button (a resistor and a capacitor — Lab 02 — smoothing the edges) feeding a Schmitt-trigger input (74HC14, if you have one), or do it in software on the Pico (Lab 04).

---

## Session 4 — Report and tidy-up (3 hours)

**Short lab report:** *"How often does my pushbutton bounce, and does an RC filter fix it?"* — your 20-press table, before and after.

**Photograph** each built circuit and draw clean schematics of the full adder and counter for your notes.

---

## Done when

- [ ] Five truth tables verified on hardware.
- [ ] Full adder and 2-bit adder pass all rows.
- [ ] The counter counts from the 555; bounce measured and one fix tried.
- [ ] Report written; schematics drawn.

## Retrieval and reflection

1. **[R] Blank sheet (15 min):** the full adder's equations and schematic; why inputs need pull-downs; what a D flip-flop does; what bounce is.
2. **[F] (spoken, 2 min):** "How does a pile of switches add two numbers?" Then compare with your [Explain-a-System](../../00-foundations/english/projects/explain-a-system/spec.md) explainer 3.
3. **Flashcards:** pin 7/14 rule; the half- and full-adder equations; HC logic levels.

**Next:** [Lab 04 — Pico and MicroPython](lab-04-pico-and-micropython.md).
