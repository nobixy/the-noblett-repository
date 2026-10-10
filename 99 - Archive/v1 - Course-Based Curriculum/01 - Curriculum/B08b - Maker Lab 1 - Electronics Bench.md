---
block_id: "Block 8b"
stage: "02 - Year 1"
title: "Maker Lab 1: Electronics Bench, Soldering and Arduino"
category: "core"
subject: "Electrical Engineering"
term: "Year 1 Spring (after Circuits)"
status: not-started
prerequisites:
  - "B08a - Circuits and Electronics Bridge"
hours_estimate: 40
hours_actual: 0
primary_resource: "SparkFun and Adafruit Learn tutorials + Arduino docs (free); Wokwi and Falstad simulators first"
milestone: "Soldered kit works; Arduino sensor logger runs 1 hour unattended; MOSFET motor driver with flyback diode built and measured"
date_started: ""
date_completed: ""
tier: "Tier 1 - Core"
---

# Block 8b — Maker Lab 1: Electronics Bench, Soldering and Arduino

[[00 - Start Here|Start Here]] / [[00 - Start Here#The Path|The Path]] / [[Hardware Index|Hardware Index]]

> [!INFO] Block Overview
> - **Term / Position:** Year 1 Spring (after Circuits)
> - **Estimated Hours:** ~40 hrs
> - **Status:** `not-started`
> - **Primary Resource:** SparkFun and Adafruit Learn tutorials + Arduino docs (free); Wokwi and Falstad simulators first
> - **Key Milestone:** Soldered kit works; Arduino sensor logger runs 1 hour unattended; MOSFET motor driver with flyback diode built and measured
> - **Added by:** [[DR-005 - Capstone and Maker Thread|DR-005]] (2026-10-09)

---

## 📚 Curriculum Tier: Tier 1 - Core

## 🎯 Why This Block Matters
The first of five Maker Labs (the hands-on thread that runs beside the theory, added for the drone-swarm capstone). Circuits taught you why; this lab teaches your hands: a multimeter, a breadboard, a soldering iron, and a microcontroller. Every later lab and the capstone hardware depend on these habits. **Sim first, then buy:** every lab below starts in a free simulator; buy parts only once the simulated version works.

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[B08a - Circuits and Electronics Bridge|Circuits and Electronics Bridge]]

---

## 📖 Primary Syllabus & Core Content
- [ ] Bench safety: iron safety, ventilation and flux fumes, ESD, first look at LiPo battery safety.
- [ ] Multimeter: voltage, current, resistance, continuity, diode test. Read a datasheet's absolute-maximum table.
- [ ] Breadboard prototyping: LEDs and current-limiting resistors, voltage dividers, pull-up/pull-down resistors, switch debouncing (RC + software).
- [ ] Transistors as switches: BJT and logic-level MOSFET low-side switch, flyback diode for inductive loads.
- [ ] Power: linear regulators, decoupling capacitors, ground loops, why 3.3 V vs 5 V logic matters (level shifting).
- [ ] Soldering: through-hole, desoldering with wick and pump, wire stripping and crimping, heat-shrink; inspect joints against the SparkFun checklist.
- [ ] Arduino: GPIO, analogRead (ADC), PWM, Serial; reading a sensor library's source, then replacing it with your own code.
- [ ] Debug tools: a cheap USB logic analyzer with sigrok PulseView to watch UART/I2C on the wire.

---

## 🛠️ Build Requirement
Build each one in Wokwi or Falstad first, then on the bench:
1. **Solder a through-hole kit** (any small kit) and pass your own joint-inspection checklist.
2. **Sensor logger:** Arduino (or Pico 2 in Arduino mode) reads an IMU or temperature sensor and logs to serial with a hardware + software debounced button.
3. **Motor driver:** a DC motor driven from PWM via a logic-level MOSFET with a flyback diode; measure current with the multimeter and capture the PWM with the logic analyzer.

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> All three builds work and are photographed in your notes; the logger runs 1 hour unattended; from a blank page you can explain a pull-up resistor, a flyback diode and decoupling capacitors.

---

## 🔎 Verified Resources (DR-005, checked 2026-10-09)
- SparkFun tutorials (free): learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering, …/how-to-use-a-breadboard, …/how-to-use-a-multimeter.
- Adafruit Learn (free): learn.adafruit.com. Arduino docs (free): docs.arduino.cc.
- Simulators (free): wokwi.com (Arduino, ESP32, Pico); falstad.com/circuit.
- sigrok PulseView (free logic-analyzer software): sigrok.org/wiki/PulseView.
- 💲 Charles Platt, *Make: Electronics* (library copy works).
- **Kit (💲, cheapest path, approx. Oct 2026):** breadboard + jumpers + parts assortment ≈$20–35; basic multimeter ≈$20–30; Pine64 Pinecil soldering iron $25.99 (pine64.com) + solder, flux, wick ≈$15; 8-channel USB logic analyzer clone ≈$10–15; Raspberry Pi Pico 2 $5 or an Arduino Uno-compatible clone. Total ≈$95–125. Free alternative: Wokwi for everything except soldering; a library makerspace often lends irons and meters.

---

## 📝 Study Notes, Psets & Proofs

*Your atomic notes, problem-set proofs, and build notes go here — written by you, from a blank page.*

> [!TIP]- Check your work (only after your own blank-sheet attempt)
> The circuit works on the bench and matches your simulation; the logic analyzer trace matches what your code meant to send.

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- Paul Scherz & Simon Monk, *Practical Electronics for Inventors* 💲 (library).
- Ben Eater's breadboard videos (YouTube, free).

---

## ➡️ Next Steps
- **Topic Hub:** [[Hardware Index|Hardware Index]] | [[00 - Start Here#The Path|The Path]]
- **Sequential Flow:** [[B08a - Circuits and Electronics Bridge|← Circuits and Electronics Bridge]] | [[00 - Start Here|Start Here]] | [[B09 - Computer Systems|Computer Systems →]]
