---
title: "Project: Motion Lab"
id: "MOD12-PRJ-motion-lab"
type: "project"
module: "12-math-for-engineering"
phase: "C"
order: 870
prerequisites: [MOD12-C1, MOD12-C2, MOD12-C3]
units: "C1, C2, C3"
artifact: "Numerical calculus tools tested against exact answers; your phone's accelerometer data integrated into velocity and position; ODE solvers (Euler, RK4) compared on a spring, a pendulum, and your RC circuit"
deliverable: "Lab report: what numerical calculus gets right, gets wrong, and why (with error plots)"
---

# Project: Motion Lab

| | |
| :-- | :-- |
| **Module** | 12 Math for Engineering (Units C1–C3) |
| **You build** | A small numerical-calculus toolkit — derivatives, integrals, root finding, and differential-equation solvers — tested against exact answers, and then pointed at real data: your phone's motion sensors, and your own Module 04 circuit measurements |
| **Deliverable** | A lab report with error plots |

---

## Why this matters

Calculus is the mathematics of change: speed is the rate of change of position; position is the accumulation of speed. Computers do calculus **numerically**, with small steps — and small steps have errors that can grow, shrink, or explode depending on the method. Engineers who simulate anything (circuits, robots, weather, games) must understand those errors. Here you'll see them on your own data.

---

## Milestones

### Milestone 1 — Derivatives (Unit C1)

1. `derivative(f, x, h)` by **forward difference** (f(x+h) − f(x))/h and **central difference** (f(x+h) − f(x−h))/(2h).
2. For f = sin, exp, and x³ at a few points, plot the error against h for h = 10⁻¹ … 10⁻¹⁵ on log-log axes. You'll see the error **fall** (slope 1 for forward, 2 for central — read the slopes off, Module 05 Lab 01) and then **rise** again for tiny h. [W] Why does it rise? (M06 Part 7: floating-point rounding — subtracting two nearly equal numbers loses digits.) Find the best h for each method and explain it.
3. **Newton's method** for roots: x ← x − f(x)/f′(x). Find √2 (root of x² − 2) to 15 digits, counting iterations; watch the number of correct digits roughly **double** each step. Find a function where Newton's method fails (diverges or cycles) and explain why with a sketch.

### Milestone 2 — Integrals (Unit C2)

1. Left Riemann sums, the **trapezoid** rule, and **Simpson's** rule.
2. For ∫₀^π sin x dx (= 2 exactly) and ∫₀¹ e^x dx, plot error against the number of steps (log-log). Confirm the slopes (≈ −1, −2, −4) and explain them in words [F].
3. The **fundamental theorem** check: numerically integrate a derivative and compare with the original function's change.

### Milestone 3 — Your phone's motion (Units C1–C2 on real data)

**phyphox** (a free app from RWTH Aachen University, for Android and iOS) records your phone's accelerometer and exports CSV.
1. Record: the phone lying still (30 s); then slid along a table in a straight line about 1 m and stopped; then dropped onto a cushion from a measured height (carefully, onto something soft!).
2. **Integrate** acceleration to velocity, and velocity to position (trapezoid rule), for the slide. Compare the computed distance with the measured 1 m. It will be wrong — often badly. [W] Why? (A tiny constant error in acceleration integrates to a velocity error that grows linearly and a position error that grows **quadratically**: **drift**. Show it with the "still" recording, which should integrate to zero.)
3. Fix what you can: subtract the bias measured while still; reset velocity to zero when you know the phone is stopped (a trick used in real foot-mounted navigation). Report how close you get.
4. **The drop:** from the free-fall segment (acceleration magnitude near 0 in the phone's frame), measure the fall time and compute the height with h = ½gt². Compare with your measured height.

### Milestone 4 — Differential equations (Unit C3)

1. **Euler's method** and **RK4** for dy/dt = f(t, y).
2. **Exponential decay** dy/dt = −y/τ: compare both methods with the exact e^{−t/τ} for several step sizes (error plots; slopes 1 and 4).
3. **Your RC circuit** from Module 04 Lab 02: dV/dt = (V₀ − V)/RC. Simulate with your measured R and C; overlay your measured charging data. Then fit τ by least squares on the model (Matrix Studio's least squares, or `numpy.polyfit` on the linearised log form).
4. **The spring** (harmonic oscillator) x″ = −ω²x as a system of two first-order equations. Run Euler and RK4 for 100 periods; plot the **energy** ½v² + ½ω²x² over time. Euler's energy **grows** (the spring gains energy from nowhere); RK4's barely changes. Then try the **semi-implicit (symplectic) Euler** method (update v first, then x using the new v): its energy stays bounded even with large steps. [W] Why does such a tiny change matter so much? (Read about symplectic integrators after answering.)
5. **The pendulum** θ″ = −(g/L) sin θ: compare with the small-angle approximation for amplitudes of 5°, 30°, and 90°. When does the approximation fail?

---

## Communication deliverable

**Lab report** (3–4 pages, E10): error-vs-step plots with slopes for derivatives, integrals, and ODE methods; the phone-motion story (drift and its fixes); the RC fit vs Module 04's measurement; the energy plots and your explanation; three practical rules for numerical calculus.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Derive the central-difference and trapezoid error orders from a blank page (Taylor series — look it up in OpenStax Vol. 2 ch. 6) |
| **F** | Drift; why RK4 is better; why the best h isn't the smallest |
| **W** | Rounding vs truncation error; symplectic Euler; small-angle failure |
| **S** | Method steps as subgoal comments; error analysis as labelled steps |
| **T** | The report |

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Derivatives and Newton | Error plots with both regimes explained; Newton failure shown | Plots only | Missing |
| Integrals | Three rules, slopes confirmed and explained | Two | One |
| Phone data | Drift shown and partly fixed; drop height computed | Integrated only | Missing |
| ODEs | Euler/RK4/symplectic, RC fit, energy plots, pendulum | Most | Few |
| Report | Clear, with rules of thumb | Complete | Missing |

**Done when:** every area at least 2.

## Connections

- **Back:** M06 (floating point), M11 (exponentials, logs), Module 04 Lab 02 and Pico Thermostat (RC and heating curves), Module 05 Lab 01 (log-log slopes).
- **Forward:** robotics, control, and simulation tracks; any physics in your capstone.

> **Originality note:** these experiments were designed for this curriculum.
