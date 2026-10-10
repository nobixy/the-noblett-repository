---
block_id: "Block 9a"
title: "Maker Lab 2: Embedded C on Microcontrollers (RP2350 / ESP32)"
category: "core"
subject: "Computer Engineering"
term: "Year 2 Fall (after Computer Systems)"
status: not-started
prerequisites:
  - "B06 - C Fluency"
  - "B09 - Computer Systems"
  - "B08b - Maker Lab 1 - Electronics Bench"
hours_estimate: 80
hours_actual: 0
primary_resource: "Raspberry Pi Pico 2 C SDK + ESP-IDF (FreeRTOS) docs + Valvano's UT Austin embedded materials (free)"
milestone: "Propeller see-saw holds a setpoint within ±3° under disturbance, using your own IMU driver and a fixed-rate PID loop"
date_started: ""
date_completed: ""
tier: "Tier 1 - Core"
---

# Block 9a — Maker Lab 2: Embedded C on Microcontrollers (RP2350 / ESP32)

[[00 - Start Here|Start Here]] / [[00 - Start Here#The Path|The Path]] / [[Hardware Index|Hardware Index]]

> [!INFO] Block Overview
> - **Term / Position:** Year 2 Fall (after Computer Systems)
> - **Estimated Hours:** ~80 hrs
> - **Status:** `not-started`
> - **Primary Resource:** Raspberry Pi Pico 2 C SDK + ESP-IDF (FreeRTOS) docs + Valvano's UT Austin embedded materials (free)
> - **Key Milestone:** Propeller see-saw holds a setpoint within ±3° under disturbance, using your own IMU driver and a fixed-rate PID loop
> - **Added by:** [[DR-005 - Capstone and Maker Thread|DR-005]] (2026-10-09)

---

## 📚 Curriculum Tier: Tier 1 - Core

## 🎯 Why This Block Matters
A drone is a microcontroller running a fast control loop on noisy sensors. This lab moves you from Arduino libraries to your own drivers: registers, interrupts, timers, buses, an RTOS, and motors. It is the embedded half of 'my software and hardware skill will need to be perfected'. **Sim first, then buy:** every lab below starts in a free simulator; buy parts only once the simulated version works.

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[B06 - C Fluency|C Fluency]]
- [[B09 - Computer Systems|Computer Systems]]
- [[B08b - Maker Lab 1 - Electronics Bench|Maker Lab 1]]

---

## 📖 Primary Syllabus & Core Content
- [ ] Memory-mapped I/O and registers; reading the RP2350 and ESP32 datasheets; clocks and the build/flash/debug cycle (SWD debugging with a second Pico as a probe).
- [ ] GPIO, interrupts and ISRs (latency, what is safe inside an ISR), hardware timers and PWM, ADC, DMA.
- [ ] Buses from the datasheet: UART, I2C and SPI drivers written by you, checked on the logic analyzer.
- [ ] FreeRTOS (as used by ESP-IDF): tasks, queues, priorities, watchdog; fixed-rate control loops and jitter measurement.
- [ ] Sensors: IMU (accelerometer + gyro), time-of-flight range sensor, barometer; sensor fusion with a complementary filter.
- [ ] Actuators: brushed DC via H-bridge, hobby servos, brushless motors and ESC protocols (PWM, DShot overview).
- [ ] Control: discrete PID, anti-windup, sample-rate choice, step-response tuning with logged data (ties to Differential Equations and Signals).
- [ ] Wireless first contact: ESP-NOW peer-to-peer messages between two ESP32 boards (feeds Block 19a mesh work).

---

## 🛠️ Build Requirement
Simulate in Wokwi first (it runs ESP32 and Pico code), then build:
1. **Your own IMU driver** over I2C or SPI (no vendor library), verified against a logic-analyzer capture.
2. **Propeller see-saw:** a motor + propeller on a pivoting arm; complementary filter + PID at ≥250 Hz holds a commanded angle; telemetry streamed over UART or ESP-NOW and plotted.
3. **Measured numbers:** ISR latency, loop jitter, and a step response (overshoot, settling time) in your notes.

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> The see-saw holds ±3° under a finger push and returns within 1 s; your driver matches the datasheet's timing on the analyzer; you can explain anti-windup and why the loop rate matters.

---

## 🔎 Verified Resources (DR-005, checked 2026-10-09)
- Raspberry Pi microcontroller docs and Pico C/C++ SDK (free): raspberrypi.com/documentation/microcontrollers/.
- ESP-IDF Programming Guide (free): docs.espressif.com/projects/esp-idf/en/stable/esp32/ (ESP-NOW: …/api-reference/network/esp_now.html).
- Jonathan Valvano, UT Austin embedded systems materials (free): users.ece.utexas.edu/~valvano/.
- Interrupt blog by Memfault (free, excellent firmware practice): interrupt.memfault.com.
- Wokwi simulator (free): wokwi.com.
- 💲 Elecia White, *Making Embedded Systems*, 2nd ed. (library copy works).
- **Kit (💲, approx. Oct 2026):** Pico 2 $5 (Pico 2 W $7), one or two ESP32-S3 dev boards ≈$10 each, IMU breakout ≈$5–10, ToF sensor ≈$5–10, small motor driver (DRV8833/TB6612) ≈$5, coreless motors + props + servo ≈$10–15. Total ≈$50–70.

---

## 📝 Study Notes, Psets & Proofs

*Your atomic notes, problem-set proofs, and build notes go here — written by you, from a blank page.*

> [!TIP]- Check your work (only after your own blank-sheet attempt)
> Logged step responses and analyzer traces are the check; compare your PID tuning against a simulation of the same plant from Block 4a.

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- Zephyr RTOS docs (free): docs.zephyrproject.org/latest/ if you prefer a vendor-neutral RTOS.
- Embedded Rust (the Embedded Rust Book) once the C versions work.

---

## ➡️ Next Steps
- **Topic Hub:** [[Hardware Index|Hardware Index]] | [[00 - Start Here#The Path|The Path]]
- **Sequential Flow:** [[B09 - Computer Systems|← Computer Systems]] | [[00 - Start Here|Start Here]] | [[B10 - Math for CS|Math for CS →]]
