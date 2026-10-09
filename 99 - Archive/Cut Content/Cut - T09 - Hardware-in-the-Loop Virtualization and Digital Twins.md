---
block_id: "Track 9"
track_id: "Track 9"
title: "Hardware-in-the-Loop Virtualization, Digital Twins and CPS"
category: "specialization"
subject: "Specialization"
term: "Years 4 & 5"
status: not-started
prerequisites:
  - "B08 - Physics II"
  - "B08a - Circuits and Electronics Bridge"
  - "B09 - Computer Systems"
  - "B14 - Computer Architecture"
  - "B16 - Operating Systems"
  - "T06 - Advanced Computer Engineering"
target_profile: "HIL Simulation Engineer, Cyber-Physical Systems Architect, Automotive/Avionics Safety Engineer"
aliases: [Track 9 - Hardware-in-the-Loop Virtualization, Digital Twins and CPS, Track 9 - HIL Virtualization and CPS, "Hardware-in-the-Loop Virtualization and Digital Twins"]
tier: "Tier 3 - Depth"
hours_estimate: 400
hours_actual: 0
optional: true # specialization track not yet chosen (DR-001)
primary_resource: "Real-Time Systems, Hypervisors & Plant Modeling + Hardware-in-the-Loop Testbeds, Emulation & Fault Injection"
milestone: "Complete Hardware-in-the-Loop (HIL) Testbed for Autonomous Drone Flight Controller"
date_started: ""
date_completed: ""
cut: "DR-004 (2026-10-09): Merged into Track 9 (Autonomous Robotics and Control): HIL testing and digital twins are how CPS and robots are validated."
---
> [!WARNING] Removed from the curriculum by [[DR-004 - Content Overhaul|DR-004]] (2026-10-09)
> Merged into Track 9 (Autonomous Robotics and Control): HIL testing and digital twins are how CPS and robots are validated.


# Track 9 — Hardware-in-the-Loop Virtualization, Digital Twins and CPS

> [!INFO] Track Overview
> - **Track ID:** Track 9
> - **Prerequisites:** [[B08 - Physics II|Physics II]], [[B08a - Circuits and Electronics Bridge|Circuits and Electronics Bridge]], [[B09 - Computer Systems|Computer Systems]], [[B14 - Computer Architecture|Computer Architecture]], [[B16 - Operating Systems|Operating Systems]], [[T06 - Advanced Computer Engineering|Advanced Computer Engineering]]
> - **Target Profile:** HIL Simulation Engineer, Cyber-Physical Systems Architect, Automotive/Avionics Safety Engineer
> - **Structure:** Two core courses plus three progressive labs and one comprehensive capstone build deliverable.
> - **Curriculum Position:** Elective specialization block across Years 4 & 5 (*"Two deep beats six shallow"*).

---

## 🎯 Why This Track Matters

Cyber-Physical Systems (CPS)—including autonomous vehicle fleets, commercial fly-by-wire avionics, nuclear power grid controllers, and surgical robotics—operate at the critical boundary where software algorithms interface with continuous, non-linear physical dynamics. In these safety-critical systems, software bugs, timing jitter, or unexpected environmental perturbations do not merely result in program crashes; they cause catastrophic physical destruction and loss of human life.

Validating safety-critical control firmware against ISO 26262 (ASIL-D) or DO-178C (DAL-A) standards cannot be performed solely on physical prototypes due to destructive risk, cost, and impossibility of edge-case physical reproducibility. Instead, modern mission-critical engineering relies on deterministic Hardware-in-the-Loop (HIL) virtualization: running real embedded electronic control units (ECUs) in hard real-time lockstep with mathematical digital twin plant simulations, emulated multi-core SoCs (via QEMU/Renode), simulated bus networks (CAN-FD, FlexRay, TSN), and automated fault injection engines. Mastering this discipline bridges embedded Linux kernel real-time tuning, numerical physics integration, bus protocol engineering, and formal hybrid system reachability verification.

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[B08 - Physics II|Physics II]]
- [[B08a - Circuits and Electronics Bridge|Circuits and Electronics Bridge]]
- [[B09 - Computer Systems|Computer Systems]]
- [[B14 - Computer Architecture|Computer Architecture]]
- [[B16 - Operating Systems|Operating Systems]]
- [[T06 - Advanced Computer Engineering|Advanced Computer Engineering]]




## 📚 Core Courses

### Course 1: Real-Time Systems, Hypervisors & Plant Modeling

This course covers scheduling theory, Linux real-time patch internals, multi-core virtualization, and continuous dynamical plant equations.

#### Module 1: Hard Real-Time Scheduling Theory & Analysis
- Classical scheduling algorithms: Rate-Monotonic Scheduling (RMS), Earliest Deadline First (EDF), and Least Laxity First (LLF).
- Schedulability tests: Liu & Layland utilization bounds ($\sum U_i \le n(2^{1/n}-1)$); exact Response Time Analysis (RTA).
- Resource sharing and synchronization: unbounded priority inversion, Priority Inheritance Protocol (PIP), and Priority Ceiling Protocol (PCP).
- Schedulability under multiprocessor partitioned vs global scheduling.

#### Module 2: Deterministic OS & Linux PREEMPT_RT Architecture
- Linux kernel latency sources: non-preemptible spinlocks, interrupt service routines (ISRs), page faults, and timer tick granularity.
- PREEMPT_RT patch internals: threadification of interrupt handlers, converting spinlocks into sleeping rt-mutexes, high-resolution timers (`hrtimer`).
- Low-latency configuration: CPU core isolation (`isolcpus`), memory pinning (`mlockall`), IRQ CPU affinity masking, and Intel CAT (Cache Allocation Technology) to eliminate noisy neighbor cache thrashing.

#### Module 3: Continuous & Hybrid Dynamical Plant Modeling
- State-space representation of physical systems:
  $$\dot{x}(t) = A x(t) + B u(t), \quad y(t) = C x(t) + D u(t)$$
- Modeling non-linear physics: aerodynamics (6-DOF flight equations), brushless DC motors (electromechanical torque balance), and hydraulic actuators.
- Real-time numerical integration: Runge-Kutta 4th Order (RK4) and symplectic integrators; trade-offs between step-size stability and compute budget.
- Hybrid automata: discrete mode switches (e.g. gear changes, friction stiction, impact dynamics) governed by guard conditions.

#### Module 4: Embedded Type-1 Hypervisors & Hardware Virtualization
- Architectural partitioning: ARM TrustZone, Intel VT-x, and RISC-V H-extension.
- Open-source embedded real-time hypervisors: Jailhouse (static cell-based partitioning), Xen-ARM, and ACRN.
- Zero-overcommit memory and core allocation: ensuring hard real-time guests execute without virtualization-induced exit latency.

#### Module 5: Automotive & Avionics Deterministic Bus Protocols
- Controller Area Network (CAN 2.0B & CAN-FD): non-destructive bitwise arbitration, CRC polynomials, bit-stuffing, and bus-off error recovery.
- FlexRay and ARINC 429: static time-triggered slots and deterministic message scheduling.
- Time-Sensitive Networking (TSN / IEEE 802.1Qbv): credit-based and time-aware traffic shapers for deterministic Ethernet in industrial CPS.

---

### Course 2: Hardware-in-the-Loop Testbeds, Emulation & Fault Injection

This course focuses on practical co-simulation architectures, peripheral emulation in QEMU and Renode, physical-electrical signal bridging, automated fault injection, and formal safety verification.

#### Module 1: Co-Simulation Architecture & Time Synchronization
- Master-slave co-simulation paradigms; lockstep synchronization between simulated virtual time and wall-clock hardware time.
- The Functional Mock-up Interface (FMI 2.0 / 3.0) standard: Functional Mock-up Units for Model Exchange (FMU-ME) vs Co-Simulation (FMU-CS).
- Mitigating extrapolation errors and algebraic loops in distributed real-time simulations.

#### Module 2: Full-System Peripheral Emulation in QEMU & Renode
- Architecture of Renode and QEMU: event-driven processor and peripheral modeling.
- Writing custom peripherals in C / C# / Python: modeling memory-mapped registers, FIFO buffers, interrupt lines, and DMA handshakes.
- Connecting simulated firmware to host networks via virtual CAN (vcan) and TAP interfaces.

#### Module 3: Physical Signal Conditioning & Hardware Interfacing
- Mixed-signal I/O bridging: Digital-to-Analog Converters (DAC), Analog-to-Digital Converters (ADC), and PWM signal decoders.
- Electrical level shifting, galvanic isolation (optoisolators/digital isolators), and physical CAN transceiver interfacing.
- FPGA-based real-time I/O coprocessors for sub-microsecond physical sensor synthesis.

#### Module 4: Automated Fault Injection & Functional Safety Certification
- Hardware fault injection: voltage brownout injection, clock glitching, physical open/short circuit simulation.
- Software-implemented fault injection (SWIFI): register bit flips, memory corruption, frame drop, frame delay, and corrupted CRC payloads.
- Developing safety cases according to ISO 26262 (ASIL-D) and DO-178C (DAL-A): fault detection time interval (FDTI) and safe-state transitions.

#### Module 5: Reachability Analysis & Safety Envelopes
- Formal methods for continuous and hybrid systems: set-based reachability analysis using zonotopes, support functions, and interval arithmetic.
- Reachability engines: SpaceEx, Flow*, and dReach.
- Computing safe invariant tubes: mathematically proving that under all permitted sensor noises and disturbances, the physical state never enters the unsafe region.

---

## 📑 Seminal Papers & Advanced Textbooks

- **Sha, L., Rajkumar, R., & Lehoczky, J. P. (1990).** *Priority Inheritance Protocols: An Approach to Designing High-Performance Real-Time Systems*. IEEE Transactions on Computers, 39(9), 1175–1185.
- **Alur, R., Courcoubetis, C., Henzinger, T. A., & Ho, P.-H. (1993).** *Hybrid Automata: An Algorithmic Approach to the Specification and Verification of Hybrid Systems*. Hybrid Systems, Lecture Notes in Computer Science (LNCS 736), 209–229.
- **Cucinotta, T., Anastasi, G. F., & Abeni, L. (2009).** *Real-Time Virtualization on Multi-Core Architectures*. IEEE Transactions on Industrial Informatics, 5(4), 433–443.
- **Lee, E. A., & Seshia, S. A. (2017).** *Introduction to Embedded Systems: A Cyber-Physical Systems Approach, 2nd Edition*. MIT Press.
- **Buttazzo, G. C. (2011).** *Hard Real-Time Computing Systems: Predictable Scheduling Algorithms and Applications, 3rd Edition*. Springer.
- **Alur, R. (2015).** *Principles of Cyber-Physical Systems*. MIT Press.

---

## 🛠️ Progressive Labs

### Lab 1: PREEMPT_RT Linux Kernel Tuning & Jitter Benchmarking
- **Objective:** Configure, patch, and deploy a real-time Linux PREEMPT_RT kernel on an embedded target or x86 host, eliminating all latency outliers under extreme load.
- **Deliverables:**
  - Automated deployment script for kernel compilation with `CONFIG_PREEMPT_RT=y`, CPU isolation, and core affinity configurations.
  - Verification harness executing `cyclictest` under synthetic workload generation via `stress-ng`.
- **Acceptance Criteria:**
  - The real-time kernel must run continuous `cyclictest` for 24 hours under 100% CPU and I/O stress (`stress-ng --cpu 8 --io 4 --vm 2`) with maximum worst-case jitter $\le 15 \, \mu\text{s}$.
  - Zero dropped timer interrupts or scheduling deadline misses across the entire benchmarking run.

### Lab 2: Emulated CAN-FD Controller and Co-Simulation in Renode
- **Objective:** Write a custom peripheral model for an emulated CAN-FD controller in Renode and co-simulate it with compiled Zephyr RTOS firmware.
- **Deliverables:**
  - C# Renode peripheral plugin implementing register maps, FIFO buffers, and frame transmission for CAN-FD.
  - Integration script connecting the virtual Renode peripheral to a Linux SocketCAN interface (`vcan0`).
- **Acceptance Criteria:**
  - The virtual controller must transmit and receive $10,000$ CAN-FD frames at $5 \text{ Mbps}$ simulated data rate without frame corruption or loss.
  - Simulated bus timing and message sequences must match physical CAN-FD bus logic analyzer captures with 100% bit parity.

### Lab 3: SpaceEx Reachability Analysis of Inverted Pendulum Safety Tube
- **Objective:** Construct a hybrid automaton model of an inverted pendulum system controlled by a digital sampled-data microcontroller with actuation delay, and formally compute its forward reachable set.
- **Deliverables:**
  - SpaceEx model file (`.xml`) specifying continuous dynamics, discrete controller sampling transitions, and sensor noise bounds.
  - Python visualization script generating phase-plane reachability tubes.
- **Acceptance Criteria:**
  - Automated formal reachability proof check verifying that for all initial angle perturbations within $\theta_0 \in [-0.2, 0.2] \text{ rad}$, the cart position never violates safety boundaries ($|x(t)| \le 1.0 \text{ m}$).
  - Safety claims mathematically validated with zero intersection with the designated unsafe state set.

---

## 🏆 Capstone Build Deliverable

### Complete Hardware-in-the-Loop (HIL) Testbed for Autonomous Drone Flight Controller

An end-to-end, closed-loop cyber-physical HIL simulation testbed connecting a physical microcontroller running flight firmware to a real-time aerodynamic digital twin.

```text
+-----------------------------------------------------------------------------------+
|                           HIL CLOSED-LOOP TESTBED                                 |
|                                                                                   |
|  [ PREEMPT_RT Host ]                                  [ Physical Target MCU ]     |
|  +------------------------------+                     +------------------------+  |
|  | 6-DOF Aerodynamic Simulator  | -- SPI / CAN (IMU) -> | Pixhawk / STM32F7      |  |
|  | (1 kHz RK4 Integration)      | <- PWM (Motors) ----  | Real-Time Flight Logic |  |
|  +------------------------------+                     +------------------------+  |
|                 |                                                  |              |
|                 v                                                  v              |
|  [ Fault Injection Controller ] -----------------------> [ Functional Safety Log] |
+-----------------------------------------------------------------------------------+
```

#### System Architecture & Specifications
1. **Target Hardware Controller:** Physical ARM Cortex-M7 microcontroller (e.g. STM32F7 or Pixhawk 4) running production flight control firmware (PX4 or ArduPilot).
2. **Plant Simulation Engine:** High-fidelity 6-DOF non-linear rigid-body aerodynamic simulator executing at $1 \, \text{kHz}$ on a Linux PREEMPT_RT host computer.
3. **Signal Interface:** Synthesized IMU sensor data (accelerometer, gyroscope, barometer) streamed over physical high-speed SPI/CAN buses into the MCU; motor PWM control signals sampled via timer input captures and fed back into the physics model in hard closed loop.
4. **Fault Injection Harness:** Automated fault generator introducing physical sensor freezing, gyro drift, actuator degradation, and dropped bus frames.

#### Verification & Acceptance Criteria
- **Timing & Determinism:** The closed-loop simulation loop must execute deterministically at $1.0 \text{ kHz} \pm 1\%$, with round-trip sensor-to-actuator communication jitter $< 20 \, \mu\text{s}$.
- **Mission Execution:** The flight controller must successfully complete a 10-minute automated autonomous waypoint navigation mission with zero loss of control and positional deviation $< 0.5 \text{ m}$.
- **Fault Recovery & Safety:** Under simulated sudden rotor degradation (50% thrust drop) and gyro sensor freeze, the system must detect the anomaly and transition into a fail-safe emergency land state within $< 200 \text{ ms}$, satisfying functional safety requirements.
- **Test Commands:**
  ```bash
  # Check host real-time latency
  sudo cyclictest -p 99 -i 1000 -l 100000 -m
  # Launch the HIL real-time physics engine and bridge
  ./bin/hil_drone_sim --config configs/quadrotor_6dof.json --bus can0 --rate 1000
  # Execute automated automated fault injection test suite
  python3 scripts/run_hil_fault_injection.py --suite iso26262_asil_d
  ```

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> Assessment criteria go here.

## ➡️ Next Steps & Degree Pathway
- **Curriculum Hub:** [[Specialization Branches|Specializations Hub]]
- **Degree Assignment:**
  - If chosen as **Primary Specialization (Track A)**: Course 1 binds to [[Specialization Branches|Block 26 - Specialization A1]] and Course 2 binds to [[Specialization Branches|Block 28 - Specialization A2]].
  - If chosen as **Secondary Specialization (Track B)**: Course 1 binds to [[Specialization Branches|Block 29 - Specialization B1]] and Course 2 binds to [[Specialization Branches|Block 31 - Specialization B2]].
- **Curriculum Roadmap:** [[00 - Start Here|Start Here]] / [[00 - Start Here#The Path|The Path]]

- **Sequential Flow:** [[T09 - Autonomous Robotics|← Autonomous Robotics]] | [[00 - Start Here|Start Here]] | [[T03 - Advanced Security and Cryptography|Advanced Security and Cryptography →]]
