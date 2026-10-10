---
title: "Lab 02 — Capacitors and the 555 Clock"
module: "04-circuits-and-digital-logic"
hours: 10
type: maker-lab
---

# Lab 02 — Capacitors and the 555 Clock

**Goal:** see an exponential curve in a real circuit, measure a time constant, and build a **clock** — the steady tick that every digital system marches to.

**Time:** about 10 hours, in three sessions.

**Deliverable:** a lab report: *"Does an RC circuit charge the way the formula says?"* plus a working ~1 Hz blinker.

---

## Session 1 — The capacitor (simulator + bench, 4 hours)

### What a capacitor does

A **capacitor** stores charge on two plates separated by an insulator. Its **capacitance** C (farads, F; you'll use microfarads, µF = 10⁻⁶ F, and nanofarads, nF = 10⁻⁹ F — M07) says how much charge it stores per volt.

Key behaviours:
- The voltage across a capacitor **can't jump instantly**; it changes as charge flows in or out.
- Charging through a resistor, the voltage rises fast at first, then slower and slower as it approaches the supply voltage.

### The RC charging curve

Charging a capacitor C through a resistor R from a supply V₀, starting empty:

$$V_C(t) = V_0 \left(1 - e^{-t/RC}\right)$$

The product **τ = RC** (Greek "tau") is the **time constant**, in seconds when R is in ohms and C in farads.
- After 1τ: the capacitor reaches 1 − e⁻¹ ≈ **63.2%** of V₀.
- After 5τ: ≈ **99.3%** — "fully charged" for practical purposes.

*Example:* R = 100 kΩ, C = 100 µF → τ = 100,000 × 0.0001 = **10 s**. On a 5 V supply it reaches about 3.16 V after 10 s.

> **[W] Why does it slow down?** The current through the resistor is (V₀ − V_C)/R (Ohm's law across the resistor). As V_C rises, the voltage left across the resistor shrinks, so the current shrinks, so charging slows. The rate of change is proportional to the distance from the target — and that is exactly what produces an exponential (M11; you'll see why in Module 12's calculus). The same shape appears in the thermostat's heating curve and in your Study Deck forgetting model.

**Discharging** through R: V_C(t) = V_start × e^(−t/RC). After 1τ it's down to 36.8%.

### Simulate (Falstad)

Build: switch, 5 V, 100 kΩ, 100 µF. Watch the scope trace as it charges. Read the voltage at t = τ, 2τ, 3τ. Then discharge it.

### Measure on the bench

**Safety:** electrolytic capacitors have polarity — the stripe marks the **negative** leg. Never reverse it. Use a capacitor rated above your supply voltage (6.3 V or more).

1. Build the 100 kΩ + 100 µF circuit with a pushbutton (or just a wire you connect) to start charging, and a second resistor + button to discharge it.
2. Discharge fully (short its legs through a 100 Ω resistor for a few seconds).
3. Start charging and **read the meter every 5 seconds for 60 seconds**. Use your phone's stopwatch or a video of the meter and a clock (video is easier: you can read it frame by frame).
4. Record the table. Plot V against t (by hand or with Python/matplotlib).
5. **Fit τ from your data:** find the time where V reaches 63.2% of the final value. Compare with RC from the nominal values.
6. **Linearise [W]:** plot ln(1 − V/V₀) against t. If the formula is right, this is a straight line through 0 with slope −1/τ (M11: the logarithm undoes the exponential). Fit the slope (M09) and get τ again.

**Electrolytic capacitors often have ±20% tolerance.** Is your measured τ within that?

---

## Session 2 — The 555 timer: a clock (3 hours)

The **NE555** is one of the most-made chips in history. In **astable** mode it switches its output between high and low forever, by repeatedly charging and discharging a capacitor between ⅓ and ⅔ of the supply voltage.

Frequency (from the datasheet):

$$f \approx \frac{1.44}{(R_1 + 2R_2)\,C}$$

*Example:* R₁ = 1 kΩ, R₂ = 68 kΩ, C = 10 µF → f ≈ 1.44/(137,000 × 0.00001) ≈ **1.05 Hz** — about one tick per second.

1. **Read the NE555 datasheet** (search "NE555 datasheet" — Texas Instruments publishes one). Find the pinout diagram and the astable circuit. Datasheets are dense; read the first page, the pinout, and the astable section only. This is a real engineering skill: extracting what you need from a long technical document (Level 4 copywork material, too).
2. Build the astable circuit with an LED (+ 330 Ω) on the output. Count blinks for 60 seconds. Compare with the formula.
3. Change C to 1 µF. Predict, then measure. (Too fast to count? Use your meter's frequency mode if it has one, or a logic analyser, or a phone video in slow motion.)
4. Add a 100 nF capacitor between the CONTROL pin (5) and ground and between the supply and ground near the chip (a **decoupling capacitor**). [W] Look up why digital chips need decoupling capacitors, and write one sentence.

**Keep this 1 Hz circuit built.** It's the clock for Lab 03's counter.

---

## Session 3 — Report (3 hours)

**Lab report** ([template](<../../04 - System/Lab Report Template.md>)): *"Does an RC circuit charge the way the formula predicts?"* Include: the predicted curve, your measured table and plot, τ found two ways (63% point and the log-linear fit), comparison with nominal RC and the tolerance, and the 555's predicted vs measured frequency at two capacitor values. Discuss error sources: tolerance, reading the meter at the right moment, leakage current in electrolytic capacitors, the meter's own input resistance (does a 10 MΩ meter input matter in a 100 kΩ circuit?).

---

## Done when

- [ ] Charging curve measured, plotted, and τ fitted two ways.
- [ ] The 555 blinks at ~1 Hz, and you've measured a second frequency.
- [ ] Lab report done.

## Retrieval and reflection

1. **[R]:** the charging formula; what τ means; 63% and 5τ; why charging slows; the 555 formula; what a decoupling capacitor is for.
2. **[F] (spoken, 2 min):** "Why does a capacitor charge quickly at first and slowly later?"
3. **[W]:** where else have you seen "the rate of change is proportional to the distance from the target"? (Study Deck's forgetting curve; M11's halving; the thermostat coming up.)

**Next:** [Lab 03 — Logic Chips on a Breadboard](lab-03-logic-chips-on-a-breadboard.md).
