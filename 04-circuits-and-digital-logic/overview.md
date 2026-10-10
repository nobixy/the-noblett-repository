---
title: "04 — Circuits and Digital Logic"
module: "04-circuits-and-digital-logic"
hours: 150
tags: [module, ee, maker, logic]
---

# 04 — Circuits and Digital Logic

**From electrons to adders.** You measure real voltages and currents on a breadboard, light LEDs with resistors you calculated, time circuits with capacitors, wire logic chips into an adder that really adds, and program a microcontroller to run a traffic light and a thermostat. Alongside the hardware, you write **Gatesmith**, your own logic simulator, and build an 8-bit ALU in it — the arithmetic heart of the CPU you'll design in Module 06.

This module is where the bottom of the computer stops being abstract. After it, "a CPU is made of switches" is something you've *done*, not something you've read.

---

## Prerequisites

- Math **M08+** (Ohm's law is a formula to rearrange; RC charging is an exponential, explained in Lab 02 and M11).
- [03 Discrete Math](../03-discrete-math/overview.md) **Unit 1** (logic). The rest of Module 03 can run alongside.
- [02 Programming Fundamentals](../02-programming-fundamentals/overview.md) done (Gatesmith is a substantial Python program).
- English **E07+** (lab reports are the main deliverable here).

## Objectives

By the end you will be able to:
1. Use a multimeter safely to measure voltage, current, and resistance; apply Ohm's law, series and parallel rules, and voltage dividers; size a resistor for an LED.
2. Explain and measure how a capacitor charges (an exponential), and build a timer clock.
3. Read a chip's datasheet and pinout; wire logic gates; build adders and counters from real chips.
4. Use a transistor as a switch controlled by a microcontroller.
5. Program a Raspberry Pi Pico: digital I/O, debouncing, analog input, PWM, and logging.
6. Design a finite-state machine, encode it in bits, and implement it in logic and in code.
7. Build a gate-level logic simulator with hierarchy, clocked storage, test vectors, and timing analysis — and use it to design an ALU.
8. Write a clear lab report with measurements, predictions, and error analysis.

## Safety (read first)

- **Low voltage only.** Everything here runs on 5 V or less from USB or small batteries. **Never** work on mains (wall) electricity. Never open a power supply.
- **Short circuits** across a battery heat wires and batteries fast. If anything gets hot or smells, disconnect power immediately.
- **Measure current with the meter in series and the probe in the "A" or "mA" socket**; measuring *voltage* with the probe still in the current socket shorts the circuit and can blow the meter's fuse. Move the probe back every time.
- **Electrolytic capacitors have a polarity.** Reversed, they can fail violently. The stripe marks the negative leg.
- **Resistors that heat things** (Pico Thermostat) must be rated for the power you put through them; the spec tells you how to check.

## Hardware: shopping list (about $60–90 total)

| Item | Why | Approx. |
| :-- | :-- | :-- |
| 2 × full-size breadboards (830 points) + jumper wire kit | everything | $12 |
| Digital multimeter (auto-ranging is easiest) | every lab | $15–25 |
| Resistor kit (E12 values, 10 Ω – 1 MΩ) | Labs 01–04 | $8 |
| LEDs (red, yellow, green; 20+), pushbuttons (10), 10 kΩ potentiometer | Labs 01–04 | $6 |
| Capacitors: 100 nF ceramic (10), 10 µF, 100 µF, 470 µF electrolytic | Lab 02 | $5 |
| 2 × NE555 timer | Lab 02 | $2 |
| 74HC-series chips: 74HC00 (NAND), 74HC04 (NOT), 74HC08 (AND), 74HC32 (OR), 74HC86 (XOR), 74HC74 (D flip-flop), 74HC161 (4-bit counter) | Lab 03 | $8 |
| Raspberry Pi Pico **H** (pre-soldered headers) + USB cable | Lab 04, projects | $6 |
| 2N2222 (or PN2222) NPN transistors, a few; 1 W resistors: 47 Ω and 100 Ω; a TMP36 analog temperature sensor | Pico Thermostat | $5 |
| Passive piezo buzzer | Lab 04 (play your Tone Loom songs!) | $1 |
| 5 V breadboard power module (USB) *or* a 4 × AA battery pack | Labs 01–03 | $4 |
| *Optional:* 8-channel USB logic analyser (~$10) + free PulseView software | seeing signals over time | $10 |

**Simulator-first rule:** every hardware lab starts in a free simulator, so you can learn before parts arrive — and so money is never a blocker:
- **Falstad Circuit Simulator** (falstad.com/circuit, in the browser) — analog circuits, animated current flow.
- **Wokwi** (wokwi.com) — simulates the Pico with MicroPython, plus LEDs, buttons, and sensors.
- **Digital** (by H. Neemann; free, Java; `digital` in the AUR) or **Logisim Evolution** — gate-level simulation with a GUI (used again in Module 06).

## Sequence and time

| Order | Item | Hours | Concepts |
| :-- | :-- | --: | :-- |
| 1 | [Lab 01 — Meter, Ohm's Law, LEDs](labs/lab-01-meter-ohms-law-and-leds.md) | 10 | voltage, current, resistance; series/parallel; dividers; LED resistors; power |
| 2 | [Lab 02 — Capacitors and the 555 Clock](labs/lab-02-capacitors-and-the-555-clock.md) | 10 | RC charging (exponential), time constant, astable timer, clock signals |
| 3 | [Lab 03 — Logic Chips on a Breadboard](labs/lab-03-logic-chips-on-a-breadboard.md) | 14 | datasheets; gates; pull-down resistors; half/full adders; counters; bouncing |
| 4 | [Lab 04 — Pico and MicroPython](labs/lab-04-pico-and-micropython.md) | 12 | GPIO, debouncing in software, ADC, PWM, serial logging |
| 5 | **[Project: Gatesmith](projects/gatesmith/spec.md)** | 50 | logic simulation, netlists, hierarchy, flip-flops, test vectors, timing, ALU design |
| 6 | **[Project: Crosswalk Controller](projects/crosswalk-controller/spec.md)** | 26 | finite-state machines, state encoding, next-state logic, timing, testing scenarios |
| 7 | **[Project: Pico Thermostat](projects/pico-thermostat/spec.md)** | 28 | sensing, calibration, transistor switching, feedback control, hysteresis, data logging |
| | **Total** | **~150** | |

Labs 01–04 in order. Start Gatesmith after Lab 03 (it's software, so it fits weekday evenings while hardware waits for Saturdays). Crosswalk after Gatesmith's flip-flop milestone and Lab 04. Pico Thermostat last.

## How the projects map to concepts — and to later modules

| Concept | Where you meet it | Later |
| :-- | :-- | :-- |
| Boolean algebra = gates | Lab 03, Gatesmith, Truth Engine | Module 06 control logic |
| Adders, carries, overflow | Lab 03, Gatesmith ALU | Kestrel's ALU and flags (06) |
| Clocks and flip-flops | Lab 02, Lab 03, Gatesmith | Registers, pipelines (06) |
| State machines | Crosswalk | Protocol state machines (09: Courier), parsers (10), the CPU control unit (06) |
| Feedback control | Pico Thermostat | Retransmission timers and flow control (09) are feedback loops too |
| Exponential RC curves | Lab 02, Thermostat | Signals (12) |

## How the study methods run through this module

| Protocol | In this module |
| :-- | :-- |
| **R** | Before each lab: draw the circuit from memory and predict every reading. After: blank sheet of the laws used. Milestone Checkpoints in every project. |
| **F** | Explain voltage, current, and resistance without the water analogy, then with it — and say where the analogy breaks. Explain a flip-flop "remembering." Spoken weekly. |
| **W** | Why pull-down resistors? Why does NAND alone suffice? Why does a ripple adder get slower as it gets wider? Why hysteresis? Each lab and spec lists more. |
| **S** | Lab procedures as labelled steps; the FSM design method (states → diagram → table → encoding → logic) as subgoals. |
| **I** | Hardware and simulation alternate; labs mix analog and digital; Study Deck cards for laws, pinouts, and gate tables. |
| **D** | Hardware bugs are physical: a loose wire, a reversed chip. When stuck, stop, write a stuck note, and re-wire from scratch the next day — it's often faster than debugging. |
| **T** | **Lab reports** are the main deliverable (E08–E10 level). Each project also has a recorded demo with the real hardware. |

## Connections

- **Back:** [Explain-a-System](../00-foundations/english/projects/explain-a-system/spec.md) explainers 1 (thermostat) and 3 (calculator adding) — reread them before starting; [Nib](../01-intro-cs-taste/projects/nib-machine/spec.md) (now you build its hardware ideas); M02 (carries), M07 (two's complement), M11 (exponentials); [Truth Engine](../03-discrete-math/projects/truth-engine/spec.md) (simplifying logic).
- **Forward:** [06 Computer Architecture](../06-computer-architecture/overview.md) — Gatesmith's ALU and register file become parts of the Kestrel datapath. [13 Capstone](../13-capstone/overview.md) — the embedded option builds on the Pico.

## Module close

1. **Cumulative retrieval [R] (45 min):** Ohm's law, series/parallel, dividers, the RC time constant, the 555 formula, every gate's truth table, the full adder, a D flip-flop's behaviour, the FSM design steps.
2. **Rebuild from memory:** wire a full adder from 74HC chips with no notes, and test all 8 input rows.
3. **Update your [Explain-a-System](../00-foundations/english/projects/explain-a-system/spec.md) explainers 1 and 3** from scratch. Compare with the originals: what do you understand now that you didn't?
4. Tick the module in [Start Here](<../00 - Start Here.md>).

**Next:** [05 Data Structures and Algorithms](../05-data-structures-and-algorithms/overview.md), then [06 Computer Architecture](../06-computer-architecture/overview.md).
