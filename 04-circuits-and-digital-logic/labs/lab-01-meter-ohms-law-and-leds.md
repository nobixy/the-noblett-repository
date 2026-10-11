---
title: "Lab 01 — Meter, Ohm's Law, and LEDs"
id: "MOD04-LAB01"
type: "lab"
module: "04-circuits-and-digital-logic"
phase: "B"
order: 590
prerequisites: []
kind: "maker"
---

# Lab 01 — Meter, Ohm's Law, and LEDs

**Goal:** understand voltage, current, and resistance well enough to predict a circuit's behaviour *before* you build it — then measure it and explain the difference.

**Sessions:** four (two in the simulator, two on the bench).

**Deliverable:** a lab report: *"How well does Ohm's law predict my real circuits?"*

**Safety:** 5 V or less only. Read the [module safety notes](../overview.md#safety-read-first) first.

---

## Session 1 — The three quantities (simulator)
### What they are

- **Voltage (V, volts)** is the "push": the difference in electrical energy per unit of charge between two points. Voltage is always *between* two points. "The voltage at this pin" means "between this pin and ground (0 V)."
- **Current (I, amperes, A)** is the flow: how much charge passes a point per second. 1 mA = 0.001 A.
- **Resistance (R, ohms, Ω)** is how much a component opposes flow.

**Ohm's law** connects them, for a resistor:

$$V = I \times R$$

Rearrange it (M08) to get the other two: I = V/R, R = V/I. *Example:* 5 V across a 1 kΩ resistor drives I = 5/1,000 = 0.005 A = **5 mA**.

**Power (P, watts, W)** is energy per second, turned into heat in a resistor: P = V × I = I²R = V²/R. Every resistor has a power rating (common ones: ¼ W). Exceed it and it overheats.

### The water analogy, and where it breaks [F] [W]

People often explain circuits with water in pipes: voltage = pressure, current = flow rate, resistance = a narrow pipe. It helps for Ohm's law and series/parallel. It **breaks** in important places: water pipes can leak but wires don't "leak" current; a pipe stays full without a pump, but a circuit with no closed loop carries no current at all; and the analogy says nothing about electric and magnetic fields (how energy really travels). Use it as a crutch, and know where it'll fail you.

### Series and parallel

- **Series** (one after another, one path): the **same current** flows through each; the voltages add up; resistances add: R = R₁ + R₂.
- **Parallel** (side by side, several paths): the **same voltage** is across each; the currents add up; resistances combine as 1/R = 1/R₁ + 1/R₂. (Two equal resistors in parallel give half the resistance.)

> **[W] Why do parallel resistances combine "upside down"?** Adding a parallel path gives the current *another way through*, so total resistance goes **down**. Conductance (1/R, "how easily current flows") is what adds.

### Simulate it (Falstad, falstad.com/circuit)

Build each circuit, and **predict every number before you look** [R]:
1. 5 V battery + 1 kΩ resistor. Predict I.
2. 5 V + 1 kΩ and 2.2 kΩ in series. Predict I and the voltage across each.
3. 5 V + 1 kΩ and 1 kΩ in parallel. Predict each current and the total.
4. 5 V + 1 kΩ and 2.2 kΩ in parallel.

<details>
<summary>Predictions (check after)</summary>

1. 5 mA · 2. R = 3.2 kΩ → I ≈ 1.56 mA; V₁ ≈ 1.56 V, V₂ ≈ 3.44 V (they add to 5 V) · 3. 5 mA each, 10 mA total (R = 500 Ω) · 4. 5 mA and ≈ 2.27 mA, total ≈ 7.27 mA (R ≈ 687.5 Ω)
</details>

---

## Session 2 — The voltage divider and the LED (simulator)
### Voltage divider

Two resistors in series between a supply and ground. The voltage at the middle is

$$V_{out} = V_{in} \times \frac{R_2}{R_1 + R_2}$$

where R₂ is the resistor between the middle and ground. *Why:* the current is V_in/(R₁ + R₂) (series), and V_out = I × R₂ (Ohm's law). Derive it yourself on paper [S] before using it.

*Examples:* 10 kΩ / 10 kΩ from 5 V → **2.5 V**. R₁ = 10 kΩ, R₂ = 4.7 kΩ → 5 × 4.7/14.7 ≈ **1.60 V**.

**Dividers are everywhere:** a potentiometer is an adjustable divider; many sensors are a resistor whose value changes with light or temperature, read as a divider by a microcontroller (Lab 04).

### The LED and its resistor

An **LED** (light-emitting diode) lets current flow in **one direction only** (long leg = anode = +), and drops a nearly fixed **forward voltage** V_f across itself when lit (red ≈ 2.0 V, green and blue ≈ 2.0–3.2 V; check your datasheet). It does **not** limit its own current: connect it straight to 5 V and it burns out. So you put a resistor in series.

**Subgoal labels [S] for sizing an LED resistor:**
1. Look up V_f and the desired current I (10 mA is bright and safe for most small LEDs).
2. The resistor gets the rest of the voltage: V_R = V_supply − V_f.
3. R = V_R / I.
4. Pick the nearest standard value **above** it (from your E12 kit: 100, 120, 150, 180, 220, 270, 330, 390, 470, 560, 680, 820…).
5. Recompute the actual current, and the resistor's power P = I²R; check it's under the rating.

*Worked example:* red LED (V_f = 2.0 V) on 5 V at 10 mA → V_R = 3.0 V → R = 300 Ω → choose **330 Ω** → I = 3.0/330 ≈ **9.1 mA** → P = 0.0091² × 330 ≈ **27 mW** (fine for ¼ W).

Simulate an LED circuit in Falstad. Then try it *without* the resistor and watch the simulated current.

---

## Session 3 — On the bench

### Know your breadboard and meter

- **Breadboard:** each group of 5 holes in a short row is connected; the long rails along the edges are connected along their length (on some boards, each long rail is split in the middle — check with your meter's continuity beep).
- **Meter:**
  - **Voltage:** black probe in COM, red in V. Dial to V (DC). Touch the two points *across* a component (in parallel with it).
  - **Resistance:** same sockets; dial to Ω; **only on unpowered components** (take resistors out, or disconnect power).
  - **Current:** red probe moved to **mA** (or A). Break the circuit and put the meter **in series**, so the current flows through it. **Move the probe back to V afterwards** (see safety).
  - **Continuity:** beeps when two points are connected. Your best friend for finding broken wires.

### Measurements

For each circuit: draw it, **predict** every reading, build it, measure, and record predicted vs measured in a table.

1. **Measure 5 resistors** with the meter. Compare with the colour bands. Real resistors have a **tolerance** (often ±5% or ±1%). Are yours within it?
2. **Measure your supply voltage.** Is it exactly 5.00 V? (Probably not. Use the *measured* value in later predictions.)
3. **Series circuit:** 1 kΩ + 2.2 kΩ on your supply. Measure the voltage across each and the current.
4. **Divider:** 10 kΩ + 4.7 kΩ. Measure V_out. Now **load** it: put a 4.7 kΩ resistor from V_out to ground (in parallel with R₂). Predict the new V_out first. [W] Why did it change? What does this mean for using a divider to "power" something?
5. **LED:** red LED + 330 Ω. Measure the current, the voltage across the LED (V_f), and across the resistor. Try 1 kΩ and 150 Ω: how does brightness relate to current?
6. **Potentiometer:** wire it as a divider; measure V_out at five positions.

<details>
<summary>Prediction for step 4 (loaded divider)</summary>

Loading puts 4.7 kΩ ∥ 4.7 kΩ = 2.35 kΩ at the bottom. V_out = 5 × 2.35/(10 + 2.35) ≈ **0.95 V** (down from 1.60 V). A divider only gives the voltage you calculated if almost no current is drawn from its middle. That's why dividers are used for *signals*, not for powering things.
</details>

---

## Session 4 — Analysis and report

### Sources of error

For each mismatch between prediction and measurement, ask [W]:
- **Component tolerance:** a "1 kΩ" ±5% resistor can be 950–1,050 Ω.
- **Supply voltage:** not exactly 5 V, and it may sag under load.
- **The meter itself:** in current mode it adds a little resistance (the "burden"); in voltage mode it draws a tiny current. Usually small, but measurable on high resistances.
- **LED forward voltage** depends on current and on the individual LED.
- **Contact resistance** in breadboards and wires.

Re-predict using measured resistor values and measured supply voltage. How much closer does it get?

### Write the lab report

Use the [Lab Report Template](<../../04 - System/Lab Report Template.md>). **Question:** *"How accurately does Ohm's law, with nominal component values, predict my circuits — and what explains the differences?"* Include the circuit diagrams, the predicted-vs-measured tables (with percent error, M06), the loaded-divider result, and the re-prediction with measured values.

---

## Done when

- [ ] All six bench circuits measured, with predictions recorded *before* measuring.
- [ ] Lab report written and revised with the E08 checklist.
- [ ] You can size an LED resistor from memory [R].

## Retrieval and reflection

1. **[R] Blank sheet:** Ohm's law in three forms; power; series and parallel rules; the divider formula and its derivation; LED resistor subgoals; how to measure V, I, and R safely.
2. **[F] (spoken):** "What is voltage?" — first without any analogy, then with water, then where water fails.
3. **Flashcards:** E12 values; the formulas; the meter safety rule.

**Next:** [Lab 02 — Capacitors and the 555 Clock](lab-02-capacitors-and-the-555-clock.md).
