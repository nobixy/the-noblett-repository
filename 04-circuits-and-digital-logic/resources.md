---
title: "04 — Resources"
id: "MOD04-RES"
type: "reference"
module: "04-circuits-and-digital-logic"
phase: "B"
order: 660
prerequisites: []
---

# 04 — Resources

*Pointers only. The labs and projects are the course.*

## Circuits (Labs 01–02)
- **All About Circuits** (allaboutcircuits.com, free textbook) — Volume I (DC) chapters 1–6 and the capacitor chapter. Clear second explanations.
- **Paul Horowitz & Winfield Hill, *The Art of Electronics*** (book) — the classic reference. Use the index; don't read it straight through. Its "Learning the Art of Electronics" companion is lab-based and friendlier.
- **Falstad Circuit Simulator** (falstad.com/circuit) — its built-in examples menu is a course in itself.

## Digital logic (Lab 03, Gatesmith)
- **Charles Petzold, *Code*** (2nd ed.) — the relay-and-switch story of gates, adders, and memory. Read the logic chapters alongside Lab 03.
- **Harris & Harris, *Digital Design and Computer Architecture*** (book; RISC-V edition) — chapters 1–3 for combinational and sequential logic; chapter 5 for adders including carry-lookahead. Also used in Module 06.
- **Datasheets** — Texas Instruments and Nexperia publish free datasheets for the NE555 and every 74HC chip. Read the first page, the pinout, and the function table.
- **GTKWave** (gtkwave.sourceforge.net) and the **VCD format** description in the IEEE 1364 (Verilog) standard summaries found online.

## Microcontrollers (Lab 04, projects)
- **MicroPython documentation for the RP2** (docs.micropython.org, "Quick reference for the RP2") — pins, ADC, PWM, timers.
- **Raspberry Pi Pico documentation** (raspberrypi.com/documentation) — pinout diagram (print it!), RP2040 datasheet (the temperature sensor formula is in the ADC section).
- **Wokwi** (wokwi.com) — Pico simulator with MicroPython.

## Control (Pico Thermostat)
- **Brian Douglas, "Understanding PID Control"** (MATLAB Tech Talks) — this module's alternate video course; see [Video course](#video-course).
- **Karl Åström & Richard Murray, *Feedback Systems*** (free online) — the rigorous version, for later.

## Video course

*Companions, not replacements: your labs and projects are the course. Watch with the [V protocol](../study-protocols.md#v--watch-actively) (pause, predict, then blank-sheet [R]), take lectures and quizzes as second explanations, and build this module's own projects, not the course's assignments. How courses fit your sessions: [study-protocols § Using video courses](../study-protocols.md#using-video-courses).*

**Primary — Building an 8-bit breadboard computer**, Ben Eater (YouTube). Free: [playlist](https://www.youtube.com/playlist?list=PLowKtXNTBypGqImE405J2565dvjafglHU) · kit and schematics: [eater.net/8bit](https://eater.net/8bit).
- **Why it fits:** it is the same kind of work this module asks for: real 555 timers, 74-series chips and LEDs on a breadboard, explained wire by wire. The clock, latch, flip-flop, counter and adder videos match Labs 02–03, and the later control-logic videos are the bridge to Module 06.

**Alternate — Understanding PID Control**, MATLAB Tech Talks (Brian Douglas). Free: [series page](https://www.mathworks.com/videos/series/understanding-pid-control.html) · part 1 on YouTube: [What Is PID Control?](https://www.youtube.com/watch?v=wkfEZmsQqiA).
- **Why:** the primary never touches feedback control, and the Pico Thermostat is a PID controller. This short series explains P, I and D, anti-windup, derivative filtering and tuning with almost no math.

### Lecture-to-vault map

Ben Eater numbers are positions in the playlist.

| Vault item | Ben Eater 8-bit (primary) | Understanding PID Control (alternate) |
| :-- | :-- | :-- |
| [Lab 01 — Meter, Ohm's law and LEDs](labs/lab-01-meter-ohms-law-and-leds.md) | — (see Gaps) | — |
| [Lab 02 — Capacitors and the 555 clock](labs/lab-02-capacitors-and-the-555-clock.md) | videos 2–5 (555 timer in astable, monostable and bistable mode; clock logic) | — |
| [Lab 03 — Logic chips on a breadboard](labs/lab-03-logic-chips-on-a-breadboard.md) | videos 6–8 (SR latch, D latch, D flip-flop) · 9–13 (bus, tri-state, registers) · 24–27 (JK flip-flops, binary counter) | — |
| [Gatesmith](projects/gatesmith/spec.md) (logic simulator) | videos 14–18 (two's complement, the ALU) · 6–8 (latches and flip-flops to simulate) | — |
| [Crosswalk Controller](projects/crosswalk-controller/spec.md) | videos 24–29 (counters, program counter) · 30–33 (7-segment decoder, EEPROM as logic) | — |
| [Lab 04 — Pico and MicroPython](labs/lab-04-pico-and-micropython.md) | — (see Gaps) | — |
| [Pico Thermostat](projects/pico-thermostat/spec.md) (PID) | — | Part 1 What Is PID Control? · Part 2 Anti-windup · Part 3 Expanding Beyond a Simple Derivative · Part 4 A PID Tuning Guide |

**Gaps:** no free video course matched Lab 01 (meter, Ohm's law, LEDs) and Lab 04 (Pico, MicroPython) well. For Lab 01, Khan Academy's [Introduction to circuits and Ohm's law](https://www.youtube.com/watch?v=F_vLWkkOETI) is a good single video. For Lab 04, use the MicroPython and Pico documentation above.
