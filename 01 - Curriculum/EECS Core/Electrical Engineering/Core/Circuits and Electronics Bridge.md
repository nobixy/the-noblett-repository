---
block_id: "Block 39"
title: "Circuits and Electronics Bridge (MIT 6.2000)"
category: "core"
term: "Year 1 Spring"
status: not-started
prerequisites:
  - "Physics II"
  - "Differential Equations Bridge"
optional: true # computer-engineering path; excluded from the hour budget
hours_estimate: 160
hours_actual: 0
primary_resource: "Anant Agarwal & Jeffrey Lang, Foundations of Analog and Digital Electronic Circuits & MIT 6.002 / 6.2000 OCW"
milestone: "All 10 problem sets solved; SPICE simulation & physical breadboard of active multi-stage audio pre-amp/filter complete; MIT 6.002 final exam passed ≥80%"
date_started: ""
date_completed: ""
tier: "Tier 2 - Support"
---

# Block 39 — Circuits and Electronics Bridge (MIT 6.2000)

[[00 - Dashboard|Dashboard]] / [[Checklist|Checklist]] / [[Hardware Index|Hardware Index]]

> [!NOTE] Optional — computer-engineering path
> Not required for MIT 6-3 (the [6-3 degree chart](https://catalog.mit.edu/degree-charts/computer-science-engineering-course-6-3/) doesn't require 6.2000). The source program adds 6.002 circuits only for the full computer-engineering degree. It sits outside the hour budget. [[Advanced Computer Engineering|Track 6]] and [[Hardware-in-the-Loop Virtualization and Digital Twins|Track 9]] list it as a prerequisite.

> [!INFO] Block Overview
> - **Term / Position:** Year 1 Spring (Co-requisite with [[Physics II]], preceding [[Computer Systems]] and [[Computer Architecture]])
> - **Estimated Hours:** ~160 hrs
> - **Status:** `not-started`
> - **Primary Resource:** Anant Agarwal & Jeffrey Lang, *Foundations of Analog and Digital Electronic Circuits* (Morgan Kaufmann) & MIT 6.002 / 6.2000 *Circuits and Electronics*
> - **Key Milestone:** All 10 problem sets solved; SPICE simulation & physical breadboard of active multi-stage audio pre-amp/filter complete; MIT 6.002 final exam passed ≥80%

---

## 📚 Curriculum Tier: Tier 2 - Support
> **Tier 2 - Support**: Strongly recommended for full understanding.

## 🎯 Why This Block Matters

Computation does not occur in an ethereal realm of pure mathematical logic; it is physically instantiated in non-linear analog silicon devices governed by electrodynamics. 

In [[Nand2Tetris]], digital logic gates (NAND, AND, OR, NOT) are treated as idealized axioms where discrete voltages represent pure $0$ and $1$. While this abstraction enables computer architecture, it leaves software engineers blind to the underlying physical reality:
1. **The Lumped Circuit Abstraction:** How Maxwell's partial differential equations from [[Physics II]] collapse into discrete algebraic laws (Kirchhoff's Current Law and Kirchhoff's Voltage Law) under the lumped matter discipline ($d \ll \lambda = c/f$).
2. **The Transistor as a Physical Switch:** Real MOSFET transistors are not instantaneous binary switches; they possess parasitic capacitances, channel resistances, threshold voltages, and finite charge-carrier transit times that dictate clock speeds, power dissipation, and race conditions.
3. **Signal Conditioning & The Analog-Digital Interface:** Real-world signals (audio, radio frequencies, biomedical voltages, sensor telemetry) are continuous analog waveforms that must be amplified, filtered, and buffered using operational amplifiers before digital systems can sample them.
4. **Energy, Power & Thermal Physics:** Modern processor architectures are constrained not by logic gate counts, but by thermal dissipation ($P = f C V_{DD}^2 + V_{DD} I_{leakage}$) and parasitic inductive/capacitive ringing on power rails.

Mastering this bridge ensures that your understanding of computer systems ([[Computer Systems]], [[Computer Architecture]]) is anchored in physical law.

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[Physics II]]
- [[Differential Equations Bridge]]


## 📖 Primary Syllabus & Core Content

The curriculum follows the canonical text by Agarwal & Lang, synchronized with MIT 6.002 / 6.2000 lectures.

### Phase 1: Lumped Circuit Abstraction & Resistive Networks
- [ ] **Module 01: The Lumped Matter Discipline & Circuit Laws**
  - Maxwell's equations to lumped circuit abstraction: constraint $\frac{\partial \mathbf{B}}{\partial t} = 0$ outside elements and $\frac{\partial q}{\partial t} = 0$ inside elements.
  - Kirchhoff's Current Law (KCL) and charge conservation at nodes.
  - Kirchhoff's Voltage Law (KVL) and path-independence of electric potential in conservative fields.
  - Associated variables convention (passive sign convention).
  - Ideal circuit elements: linear resistors, independent voltage sources, independent current sources.
- [ ] **Module 02: Systematic Network Analysis Methods**
  - Node-voltage method: formulation of independent node equations, conductance matrices, handling floating voltage sources via supernodes.
  - Mesh-current method: loop equations, handling current sources via supermeshes.
  - Linearity, superposition principle, and linear circuit solvers.
  - Thevenin and Norton theorem equivalents: open-circuit voltage $V_{th}$, short-circuit current $I_{sc}$, equivalent resistance $R_{th} = V_{th} / I_{sc}$.
  - Maximum power transfer theorem: $R_L = R_{th}$ proof via calculus.

### Phase 2: Non-Linear Circuits & The MOSFET Switch
- [ ] **Module 03: Non-Linear Elements & Small-Signal Modeling**
  - Non-linear element constitutive equations: semiconductor p-n junction diodes ($i = I_S(e^{v / V_T} - 1)$).
  - Analytical vs graphical load-line analysis.
  - Piecewise linear modeling: ideal diode model, offset voltage model ($0.7\text{ V}$).
  - Incremental small-signal analysis: Taylor series expansion around a DC operating point (Q-point), dynamic incremental resistance $r_d = \left(\left.\frac{di}{dv}\right|_{V_Q}\right)^{-1}$.
- [ ] **Module 04: MOSFET Transistors & Digital Inverters**
  - MOSFET physical structure: Source, Drain, Gate, Substrate/Body; NMOS and PMOS.
  - Threshold voltage $V_{th}$, inversion layer formation, pinch-off phenomenon.
  - Switch model of the MOSFET (S model): off for $v_{GS} < V_{th}$, ideal short for $v_{GS} \ge V_{th}$.
  - Switch-Resistor model (SR model): drain-to-source on-resistance $R_{ON}$.
  - Digital abstraction & static discipline: $V_{IL}, V_{IH}, V_{OL}, V_{OH}$, noise margins $NM_L = V_{IL} - V_{OL}$ and $NM_H = V_{OH} - V_{IH}$.
  - The NMOS inverter with pull-up resistor; Voltage Transfer Characteristic (VTC).
  - CMOS inverter architecture: complementary PMOS pull-up and NMOS pull-down networks; rail-to-rail swing, zero static power dissipation.
  - Logic gate synthesis in CMOS: NAND, NOR, compound logic gates (AOI/OAI).

### Phase 3: Energy Storage & Transient Dynamics
- [ ] **Module 05: Capacitors, Inductors & First-Order Systems**
  - Capacitor constitutive law: $i(t) = C \frac{dv(t)}{dt}$; energy stored $E_C = \frac{1}{2} C v^2$.
  - Inductor constitutive law: $v(t) = L \frac{di(t)}{dt}$; energy stored $E_L = \frac{1}{2} L i^2$.
  - Continuity conditions: capacitor voltage $v_C(t)$ and inductor current $i_L(t)$ cannot change instantaneously.
  - First-order RC and RL circuits: homogeneous differential equations, natural response, zero-input response.
  - Step response & zero-state response: complete solution $x(t) = x(\infty) + [x(0^+) - x(\infty)]e^{-t/\tau}$.
  - Time constants: $\tau = RC$ for capacitive networks, $\tau = L/R$ for inductive networks.
  - Propagation delay in digital gates: $t_{pd} \approx 0.69 R_{ON} C_L$; dynamic energy dissipation per switching cycle $E = C_L V_{DD}^2$.
- [ ] **Module 06: Second-Order RLC Circuits & Dynamic Stability**
  - Series and parallel RLC network state equations; second-order linear differential equations.
  - Characteristic equation: $s^2 + 2\alpha s + \omega_0^2 = 0$.
  - Undamped natural frequency $\omega_0 = \frac{1}{\sqrt{LC}}$ and attenuation factor $\alpha$.
  - Damping ratio $\zeta = \alpha / \omega_0$; Quality factor $Q = \frac{\omega_0}{2\alpha}$.
  - Detailed classification of dynamic behavior:
    - Overdamped ($\zeta > 1$): two distinct negative real roots, sluggish exponential return.
    - Critically damped ($\zeta = 1$): repeated real roots, fastest return to equilibrium without overshoot.
    - Underdamped ($\zeta < 1$): complex conjugate roots, damped sinusoidal oscillations with ringing frequency $\omega_d = \omega_0 \sqrt{1 - \zeta^2}$.
    - Undamped ($\zeta = 0$): pure imaginary roots, sustained sinusoidal oscillation.

### Phase 4: AC Frequency Domain, Phasors & Operational Amplifiers
- [ ] **Module 07: Sinusoidal Steady State & Phasor Analysis**
  - Complex exponential drive $v(t) = \text{Re}\{V e^{j\omega t}\}$; Euler's relation.
  - Phasor transform: transforming linear differential equations into complex algebraic equations.
  - Complex impedance and admittance: $Z_R = R$, $Z_C = \frac{1}{j\omega C} = -\frac{j}{\omega C}$, $Z_L = j\omega L$.
  - AC circuit analysis using node-voltage, Thevenin/Norton, and impedance combinations.
  - AC power: instantaneous power, real (active) power $P = \frac{1}{2} V_m I_m \cos(\theta)$, reactive power $Q$, apparent power $S$, power factor.
- [ ] **Module 08: Frequency Response & Filters**
  - System transfer function $H(j\omega) = \frac{V_{out}(j\omega)}{V_{in}(j\omega)}$.
  - Magnitude $|H(j\omega)|$ in decibels ($\text{dB} = 20 \log_{10} |H|$) and phase response $\angle H(j\omega)$.
  - Asymptotic Bode magnitude and phase plots; break frequencies, poles, and zeros.
  - Passive filter topologies: first-order RC low-pass and high-pass filters; cutoff frequency $\omega_c = 1/(RC)$.
  - Second-order RLC band-pass and notch (band-stop) filters; center frequency, bandwidth $BW = \omega_0 / Q$.
- [ ] **Module 09: Operational Amplifiers (Op-Amps)**
  - Differential amplifier model, open-loop gain $A_{OL} \to \infty$, input impedance $R_{in} \to \infty$, output impedance $R_{out} \to 0$.
  - Negative feedback and the Virtual Short principle: golden rules $V_+ = V_-$, $I_+ = I_- = 0$.
  - Fundamental op-amp configurations:
    - Inverting amplifier: $G = -R_f / R_{in}$.
    - Non-inverting amplifier: $G = 1 + R_f / R_1$.
    - Voltage follower / buffer: $G = 1$, impedance matching.
    - Summing amplifier and Difference amplifier.
    - Instrumentation amplifier (3-op-amp topology) and Common-Mode Rejection Ratio (CMRR).
    - Op-amp integrators and differentiators.
  - Real-world non-idealities: finite open-loop gain, input offset voltage, bias currents, slew rate limits, Gain-Bandwidth Product (GBWP).
- [ ] **Module 10: Active Filters & Continuous MOSFET Amplifiers**
  - Active filter design: Sallen-Key second-order low-pass and high-pass filter topologies; Butterworth (maximally flat passband) polynomial poles.
  - MOSFET small-signal amplifier: saturation region physics ($v_{DS} \ge v_{GS} - V_{th}$); square-law equation $i_D = \frac{1}{2} \mu_n C_{ox} \frac{W}{L} (v_{GS} - V_{th})^2 (1 + \lambda v_{DS})$.
  - Small-signal parameters: transconductance $g_m = \sqrt{2 \mu_n C_{ox} \frac{W}{L} I_D}$, output resistance $r_o = 1 / (\lambda I_D)$.
  - Common-source amplifier topology: DC biasing, AC coupling capacitors, small-signal AC gain $A_v = -g_m (R_D \parallel r_o)$, input and output impedances.

---

## 🛠️ Build Requirement

### The Deliverable: Dual-Stage Active Audio Pre-Amplifier and 4th-Order Butterworth Filter
You must design, simulate in SPICE (LTspice or ngspice), and physically breadboard (or test with virtual bench instrumentation) an analog signal conditioning pipeline:

1. **Stage 1 (Discrete Small-Signal Preamplifier):**
  - Implement a discrete N-channel MOSFET (2N7000 or BS170) common-source preamplifier.
  - Establish stable Q-point biasing using a resistive voltage divider with source degeneration.
  - Achieve mid-band AC voltage gain $\ge 20\text{ dB}$ ($10\times$ voltage gain) for small-signal audio inputs ($10\text{ mV}_\text{RMS}$).
2. **Stage 2 (Active 4th-Order Band-Pass Filter):**
  - Implement a dual-op-amp (TL072, NE5532, or LM358) active 4th-order Sallen-Key Butterworth band-pass filter passing the standard voice telephony band ($300\text{ Hz} - 3.4\text{ kHz}$).
  - Low-pass section: 2nd-order Sallen-Key with cutoff $f_H = 3.4\text{ kHz}$ ($Q = 0.707$).
  - High-pass section: 2nd-order Sallen-Key with cutoff $f_L = 300\text{ Hz}$ ($Q = 0.707$).
  - Out-of-band attenuation must achieve $-40\text{ dB/decade}$ on both skirts.
3. **Stage 3 (Low-Impedance Output Buffer):**
  - Rail-to-rail op-amp voltage follower or push-pull complementary stage driving a $32\,\Omega$ headphone load or line-in input without clipping.
4. **Verification & Testing Artifacts:**
  - Write SPICE netlist `.cir` or schematic `.asc` file.
  - Execute an AC sweep simulation (`.ac dec 100 10 100k`) plotting magnitude and phase Bode response.
  - Execute a transient simulation (`.tran 0 10m 0 1u`) testing step response and THD under $1\text{ kHz}$ sine wave input.
  - Deliver a formal measurement report comparing simulated vs measured cutoff frequencies, passband gain, and THD.

---

## 🏁 Mastery Criteria & Assessments

> [!IMPORTANT]
> A block is done when this condition is true. Not before.
- [ ] All 10 MIT 6.002 problem sets solved with full derivations.
- [ ] Complete SPICE simulation netlist executes cleanly in LTspice or ngspice, verifying $\ge 20\text{ dB}$ gain and $-40\text{ dB/decade}$ filter rolloff.
- [ ] Physical breadboard (or hardware bench simulator) successfully amplifies a real audio signal or function generator sweep without noticeable distortion ($< 1\%$ THD).
- [ ] MIT 6.002 / 6.2000 Final Examination completed under strict exam conditions (closed-book, 3 hours) scoring $\ge 80\%$.

---

## 📝 Study Notes, Psets & Proofs

*Your atomic notes, problem-set proofs, and build notes go here — written by you, from a blank page.*

> [!TIP]- Check your work (only after your own blank-sheet attempt)
> OCW's 6.002 (Spring 2007) posts no solutions. Your SPICE run and breadboard measurements are the check: they match your analysis or they don't.

---

## 🔄 Appendix A Alternatives (Failover)

*Only consult if primary genuinely isn't working after two honest weeks:*
- **Textbooks:**
  - Paul Horowitz & Winfield Hill, *The Art of Electronics*, 3rd ed., Cambridge University Press. (The supreme empirical bible for circuit intuition, layout, and benchcraft).
  - Adel S. Sedra & Kenneth C. Smith, *Microelectronic Circuits*, 8th ed., Oxford University Press. (The worldwide academic standard for transistor-level microelectronics).
- **Online Courses:**
  - Berkeley EECS 16A & 16B: *Designing Information Devices and Systems I & II* (eecs16a.org / eecs16b.org).
  - Coursera / Georgia Tech: *Linear Circuits* (Bonnie Ferri).

---

## ➡️ Next Steps
- **Topic Hub:** [[Hardware Index|Hardware Index]] | [[Checklist|Master Checklist]]
- **Sequential Flow:** [[Physics II|← Physics II]] | [[00 - Dashboard|Dashboard]] | [[Computer Systems|Computer Systems →]]
