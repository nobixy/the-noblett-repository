---
title: "Project: Pico Thermostat"
id: "MOD04-PRJ-pico-thermostat"
type: "project"
module: "04-circuits-and-digital-logic"
phase: "B"
order: 650
prerequisites: [MOD04-LAB04]
artifact: "A working temperature controller: a TMP36 sensor and a small resistor heater switched by a transistor from a Pico, with on/off, hysteresis, and proportional control — all logged and compared"
deliverable: "Lab report comparing control strategies with plots + short demo + updated thermostat explainer"
---

# Project: Pico Thermostat

| | |
| :-- | :-- |
| **Module** | 04 Circuits and Digital Logic |
| **Prerequisites** | Labs 01–04; [Explain-a-System](../../../00-foundations/english/projects/explain-a-system/spec.md) explainer 1 (reread it now) |
| **You build** | A real feedback controller. A Pico reads a temperature sensor taped to a small resistor "heater," switches the heater with a transistor, and tries to hold a target temperature. You measure how the system heats and cools, then compare three control strategies with logged data |
| **Deliverable** | A lab report, a demo, and a rewritten thermostat explainer |

> ⚠️ **Safety.** The heater is a 47 Ω, **1 W-rated** resistor on 5 V (about 0.53 W). It gets warm to hot — that's the point — so: rated resistor only (never a ¼ W one), mount it on the breadboard in open air, keep it away from paper and fabric, don't touch it while it's on, and never leave it running unattended. Your control code must include a **hard limit**: if the sensor reads above 60 °C, or the reading is missing or impossible, turn the heater off.

---

## Why this matters

Your first explainer described a thermostat in words. Now you build one and discover what words left out: sensors are noisy, heat takes time to spread (so the temperature keeps rising after you switch off), and the simplest rule — "on below the target, off above it" — makes the heater switch on and off constantly.

Feedback control is everywhere in engineering: cruise control, drones (the old v1 plan's capstone), power supplies, network congestion control (Module 09: your transport protocol slows down when it detects loss — a feedback loop). This project gives you the core intuitions with your own hands and your own data.

**Real-world analogs:** home thermostats, 3D-printer hot-ends, sous-vide cookers, PID controllers.

---

## The hardware

```
5V (VBUS, pin 40) ── 47 Ω 1 W resistor (heater) ──┐
                                                    │ collector
GP16 ── 1 kΩ ──────────────────────────────── base  2N2222
                                                    │ emitter
GND ────────────────────────────────────────────────┘

TMP36: +Vs → 3V3 (pin 36), GND → GND, Vout → GP26 (ADC0); its flat face taped against the heater resistor
```

**Check the transistor math first [S]** (Lab 01 skills):
1. Heater current when fully on: I_C ≈ (5 V − V_CE(sat) ≈ 0.2 V) / 47 Ω ≈ **102 mA**.
2. Base current: I_B ≈ (3.3 V − 0.7 V) / 1 kΩ ≈ **2.6 mA** — safe for a GPIO pin.
3. For the transistor to switch fully on (**saturate**), I_B × β must exceed I_C with margin. A 2N2222's β is around 100 at this current; 2.6 mA × 100 = 260 mA ≫ 102 mA ✓.
4. Heater power: P = I²R ≈ 0.102² × 47 ≈ **0.49 W** — under the 1 W rating ✓. Transistor power when saturated: V_CE × I_C ≈ 0.2 × 0.102 ≈ 0.02 W ✓.

Measure the real I_C, V_CE, and the heater voltage, and compare with your predictions.

**TMP36:** output voltage = 0.5 V + 0.01 V per °C. So T(°C) = (V − 0.5) × 100.

---

## Milestones

### Milestone 1 — Read and trust the sensor

1. Read the TMP36 through the ADC; convert to °C.
2. **Noise:** log 600 readings over 60 seconds with the heater off. Compute the mean and the spread (the standard deviation — Python's `statistics.stdev`; Module 12 explains it fully). Plot a histogram.
3. **Averaging:** average N readings per sample for N = 1, 4, 16, 64. How does the spread change? (Module 12: it should shrink roughly like 1/√N. Does it?)
4. **Calibration:** compare with a reference thermometer (a kitchen or room thermometer) at room temperature. Record the offset and apply it. Compare with the Pico's internal sensor (Lab 04) too: why might they disagree? [W]

**Done when:** you have a calibrated reading with known noise, and a chosen N with a reason.

### Milestone 2 — Characterise the plant

The thing being controlled is called the **plant**. Before controlling it, measure how it behaves.

1. **Step response:** start at room temperature, turn the heater fully on, and log temperature every second for 15 minutes. Then turn it off and log the cooling for 15 minutes.
2. Plot both. They should look like Lab 02's capacitor curves: heating approaches a maximum exponentially; cooling decays toward room temperature.
3. **Fit the model** T(t) = T_room + ΔT_max(1 − e^(−t/τ)) to the heating curve: find ΔT_max (the final rise) and τ (the time to reach 63% of it) — the same methods as Lab 02, including the log-linear fit.
4. **Delay:** how long after switching on does the reading start to rise? That **dead time** comes from heat slowly spreading from the resistor to the sensor. It will matter a lot in Milestone 3.

**Done when:** τ, ΔT_max, and the dead time are measured, with plots.

**Checkpoint:** [Milestone Checkpoint](<../../../04 - System/Milestone Checkpoint Template.md>). Feynman target: *why heating a resistor looks exactly like charging a capacitor*. (Heat flow is proportional to temperature difference, as current is proportional to voltage difference.)

### Milestone 3 — On/off control, with and without hysteresis

Choose a **setpoint** about two-thirds of the way up your measured ΔT_max above room temperature (e.g. room + 10 °C if ΔT_max is 15 °C).

1. **Plain on/off:** heater on if T < setpoint, off otherwise, checked every second. Run 20 minutes. Log temperature and heater state.
   - Measure: the temperature **ripple** (max − min after settling) and the **switching rate** (heater changes per minute).
   - Noise near the setpoint causes rapid on/off **chatter**. Do you see it?
2. **With hysteresis:** on if T < setpoint − h, off if T > setpoint + h, otherwise **keep the current state**. Try h = 0.25, 0.5, and 1.0 °C. [W] Why does "keep the current state" in the middle band require the controller to have memory? (It's a two-state FSM — Crosswalk again.)
3. Fill the table: h vs ripple vs switches per minute. Explain the trade-off.
4. **Overshoot:** even with hysteresis, the temperature goes above setpoint + h after the heater switches off. Why? (Dead time and stored heat: Milestone 2.)

**Done when:** the table for four settings, with plots.

### Milestone 4 — Proportional control with PWM

Instead of fully on or off, set the heater's **power** in proportion to the error:

```
error = setpoint − T
duty  = clamp(Kp × error, 0, 1)      # 0 = off, 1 = fully on
```

Use PWM at a low frequency (e.g. 2 Hz is fine for a heater — [W] why can a heater use such a slow PWM when an LED needed 1 kHz?).

1. Try Kp = 0.1, 0.3, 1.0 (per °C). Log 20 minutes each.
2. Measure ripple, overshoot, and the **steady-state error** — proportional control usually settles *below* the setpoint. [W] Why? (At the setpoint, error = 0, so duty = 0 — but the plant needs some power to stay warm.)
3. **Stretch — PI control:** add an **integral** term that accumulates error over time: duty = Kp × error + Ki × Σ(error × Δt). It removes steady-state error. Watch out for **windup** (the sum growing huge while the heater is maxed out) and clamp it.

**Done when:** three Kp runs analysed, the steady-state error explained.

### Milestone 5 — Logging, plotting, safety

1. All runs stream CSV to your computer (Lab 04) and are plotted with the same script.
2. **Safety tests:** unplug the sensor's signal wire during a run (or force an impossible reading in software): the heater must switch off within 2 seconds. Test the 60 °C limit by temporarily setting it lower (e.g. room + 5 °C). Log both events.

**Done when:** both safety behaviours demonstrated and logged.

---

## Testing guidance

- **Test the controller logic on the PC first:** write the control functions so they can run against a **simulated plant** (your fitted model from Milestone 2, plus random noise) on your computer. Same code, fake plant, fake clock — then run it on the Pico. If they disagree a lot, your model is missing something (probably dead time); add it.
- **Safety logic gets its own tests** (impossible readings, missing readings, over-limit).

## Common pitfalls

- **Wrong transistor pins.** 2N2222 pinouts differ between packages and makers; check your datasheet (E-B-C or C-B-E).
- **No common ground** between the 5 V heater circuit and the Pico: they share GND here, so it's fine — but if you ever use a separate supply, connect the grounds.
- **Sensor not touching the heater:** tape it firmly; poor contact means long dead time.
- **Changing two settings at once:** change one parameter per run, or you can't tell what caused what (lab report rule).
- **Running tests back-to-back without cooling:** start every run from room temperature, or record the starting temperature.

## Communication deliverable

1. **Lab report** (2–3 pages, [template](<../../../04 - System/Lab Report Template.md>), E10 level): *"How do on/off, hysteresis, and proportional control compare for a small heater?"* With the plant model, the tables, the plots, and a recommendation.
2. **Demo:** the hardware, a live run, a plot, and a safety cut-off.
3. **Rewrite your [thermostat explainer](../../../00-foundations/english/projects/explain-a-system/spec.md)** from scratch, without looking at the old one. Then compare: what does the new one say that the old one couldn't?

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Before Milestone 1, write the transistor checks and the TMP36 formula from memory |
| **F** | Heater ≈ capacitor; why hysteresis needs memory |
| **W** | Sensor disagreement; overshoot; slow PWM; steady-state error |
| **S** | Transistor sizing steps; the plant-characterisation steps |
| **I** | Analog (heat, sensors) and digital (FSM, PWM) ideas together |
| **D** | Control tuning is fiddly; one change per run; stuck notes |
| **T** | Report, demo, rewritten explainer |

## Stretch goals

- **PI or PID control** with anti-windup, and a comparison against Milestone 4.
- **Auto-tuning:** estimate good Kp and Ki from your Milestone 2 model automatically.
- **Wi-Fi (Pico W):** serve the live temperature as a tiny web page (a preview of Module 09's Lantern server).

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Hardware | Predicted and measured currents agree; safe build | Works | Unsafe or unmeasured |
| Sensor | Noise, averaging, calibration all quantified | Calibrated | Raw readings |
| Plant model | τ, ΔT_max, dead time from data, two fitting methods | One method | Missing |
| Control | On/off, three hysteresis bands, three Kp values, analysed | Two strategies | One |
| Safety | Missing-sensor and over-limit cut-offs demonstrated | One | None |
| Communication | Report, demo, rewritten explainer | Two | One |

**Done when:** every area at least 2; Safety at 3.

## Connections

- **Back:** Lab 01 (Ohm's law, power), Lab 02 (exponential curves), Lab 04 (ADC, PWM, logging), Crosswalk (the hysteresis controller is an FSM), M11 (exponentials and logs).
- **Forward:** Module 09 (congestion control is feedback control), Module 12 (calculus describes these curves exactly; statistics makes the noise analysis rigorous), Module 13 (the embedded capstone option).

> **Originality note:** the hardware design, experiments, and milestone plan were written for this curriculum.
