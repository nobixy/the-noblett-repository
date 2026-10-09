---
block_id: "Track 6"
track_id: "Track 6"
title: "Computer Engineering"
category: "specialization"
subject: "Specialization"
term: "Years 4 & 5"
status: not-started
prerequisites:
  - "B04 - Nand2Tetris"
  - "B08 - Physics II"
  - "B08a - Circuits and Electronics Bridge"
  - "B09 - Computer Systems"
  - "B14 - Computer Architecture"
target_profile: "Computer Architecture Engineer, ASIC/VLSI Designer, FPGA Hardware Systems Engineer, Silicon Verification Specialist"
aliases: [Track 6 - Computer Engineering, Track 6 - Computer Engineering (Deep Hardware), "Advanced Computer Engineering"]
tier: "Tier 3 - Depth"
hours_estimate: 400
hours_actual: 0
optional: true # specialization track not yet chosen (DR-001)
primary_resource: "Advanced Computer Architecture & Memory Hierarchies (Hennessy & Patterson / Mutlu Equivalent) + VLSI Systems Design & Silicon Synthesis (Weste & Harris / OpenLane / SkyWater)"
milestone: "Tapeout-Ready 32-bit RISC-V SoC with AXI Bus, Peripherals, and Silicon DRC/LVS Verification"
date_started: ""
date_completed: ""
---

# Track 6 — Computer Engineering

> [!INFO] Track Overview
> - **Track ID:** Track 6
> - **Prerequisites:** [[B04 - Nand2Tetris|Nand2Tetris]], [[B08 - Physics II|Physics II]], [[B08a - Circuits and Electronics Bridge|Circuits and Electronics Bridge]], [[B09 - Computer Systems|Computer Systems]], [[B14 - Computer Architecture|Computer Architecture]]
> - **Target Profile:** Computer Architecture Engineer, ASIC/VLSI Designer, FPGA Hardware Systems Engineer, Silicon Verification Specialist
> - **Structure:** Two core courses plus three progressive labs and one comprehensive capstone build deliverable.
> - **Curriculum Position:** Elective specialization block across Years 4 & 5 (*"Two deep beats six shallow"*).

---

## 🎯 Why This Track Matters

Software cannot run without physical silicon. While high-level software abstractions provide the illusion of infinite memory and instantaneous instruction execution, every program ultimately executes on physical CMOS transistors switching billions of times per second while governed by Maxwell's electromagnetic equations, parasitic capacitances, thermal dissipation ceilings, and nanometer quantum tunneling effects.

This track takes students deep beneath the software abstraction layer into the physical and architectural science of modern microprocessors and application-specific integrated circuits (ASICs). Students master quantitative computer architecture (out-of-order execution, branch prediction, cache coherence protocols, memory controllers), digital logic synthesis using SystemVerilog, timing closure through Static Timing Analysis (STA), and open-source silicon manufacturing tapeout flows (OpenLane, SkyWater 130nm).

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[B04 - Nand2Tetris|Nand2Tetris]]
- [[B08 - Physics II|Physics II]]
- [[B08a - Circuits and Electronics Bridge|Circuits and Electronics Bridge]]
- [[B09 - Computer Systems|Computer Systems]]
- [[B14 - Computer Architecture|Computer Architecture]]




## 📚 Core Courses

### Course 1: Advanced Computer Architecture & Memory Hierarchies (Hennessy & Patterson / Mutlu Equivalent)

This course develops modern superscalar out-of-order execution microarchitectures, cache coherence, and DRAM memory subsystem dynamics.

#### Module 1: Pipelining Hazards, Branch Prediction & Instruction-Level Parallelism (ILP)
- Classic 5-stage RISC pipeline review: data hazards (RAW, WAR, WAW), structural hazards, and control hazards.
- Dynamic branch prediction: saturating 2-bit counters, correlating/two-level adaptive predictors, tournament predictors, and the TAGE (TAgged GEometric history length) predictor.
- Branch Target Buffers (BTB), Return Address Stacks (RAS), and speculative instruction fetching.
- Superscalar issue: wide fetching, decoding, and dispatching multiple instructions per clock cycle.

#### Module 2: Dynamic Scheduling & Out-of-Order Execution
- Tomasulo's algorithm: reservation stations, common data bus (CDB), and eliminating WAR/WAW false dependencies via register renaming.
- The Reorder Buffer (ROB): maintaining precise exception architecture and speculative state retirement.
- Unified physical register file architectures (R10k style) vs explicit ROB architectures.
- Memory disambiguation: load-store queues (LSQ), store-to-load forwarding, and speculative memory execution.

#### Module 3: Multiprocessor Cache Coherence & Memory Consistency
- The cache coherence problem: write-invalidate vs write-update protocols.
- Snooping protocols: MSI, MESI (Illinois protocol), and MOESI state machines.
- Scalable directory-based cache coherence for many-core processors.
- Memory consistency models: Sequential Consistency (SC), Total Store Order (TSO), Weak Ordering, and Release Consistency; memory barrier instructions (`sfence`, `lfence`, `mfence`).

#### Module 4: DRAM Subsystem Architecture & Memory Controllers
- Physical DRAM organization: channels, dual in-line memory modules (DIMMs), ranks, chips, banks, rows, and columns.
- DRAM timing constraints: $t_{\text{RCD}}$ (row-to-column delay), $t_{\text{RP}}$ (row precharge), $t_{\text{CAS}}$ (column access strobe), and $t_{\text{RAS}}$ (row active time).
- Memory controller scheduling algorithms: First-Ready First-Come-First-Served (FR-FCFS), bank parallelism, and row-buffer hit optimization.
- DRAM refresh overhead and Rowhammer vulnerability physics.

#### Module 5: Domain-Specific Accelerators & Spatial Computing
- Taxonomy of accelerators: SIMD vectors vs GPUs vs Systolic Arrays.
- Systolic array architecture: processing element (PE) datapath, weight-stationary vs output-stationary dataflows for tensor multiplication (Google TPU v1-v4).
- Interconnection networks (NoC): 2D mesh, torus, crossbar switches, virtual channels, and wormhole routing.

---

### Course 2: VLSI Systems Design & Silicon Synthesis (Weste & Harris / OpenLane / SkyWater)

This course covers transistor-level CMOS physics, digital cell library design, SystemVerilog RTL synthesis, Static Timing Analysis, and physical ASIC tapeout.

#### Module 1: MOS Transistor Physics & CMOS Inverter Dynamics
- MOSFET operation: cut-off, linear/triode, and saturation regions; Shockley square-law model vs velocity saturation in nanometer regimes.
- Static CMOS inverter: transfer characteristics (VTC), switching threshold $V_{\text{th}}$, and noise margins ($NM_H, NM_L$).
- Dynamic behavior: parasitic capacitances ($C_{gd}, C_{gs}, C_{db}, C_{sb}$), RC delay modeling, and Elmore delay calculations.
- The Method of Logical Effort: sizing transistor chains for minimal path delay ($D = N F^{1/N} + P$).

#### Module 2: Static & Dynamic CMOS Combinational Logic Design
- Complementary CMOS logic networks: pull-up networks (pMOS) and pull-down networks (nMOS).
- Pass-transistor logic and transmission gates: charge sharing, threshold drops, and restoring buffers.
- Dynamic logic: precharge and evaluation phases, domino logic, and charge leakage mitigation via keeper transistors.
- Sequential circuit elements: latches vs flip-flops, master-slave D flip-flops, setup time ($t_{\text{setup}}$), hold time ($t_{\text{hold}}$), and clock-to-Q delay ($t_{\text{cq}}$).

#### Module 3: SystemVerilog RTL Design & Hardware Verification
- Synthesizable SystemVerilog: procedural blocks (`always_ff`, `always_comb`), non-blocking (`<=`) vs blocking (`=`) assignments.
- Finite State Machine (FSM) modeling: Mealy vs Moore state machines, one-hot vs binary state encoding.
- Verification methodology: SystemVerilog Assertions (SVA) for formal property checking; testbench generation with Cocotb (Python) and UVM fundamentals.
- Open-source logic simulation: Verilator cycle-accurate simulation and Icarus Verilog.

#### Module 4: Synthesis, Static Timing Analysis (STA) & Clock Trees
- Logic synthesis: translating RTL into gate-level netlists using Yosys and target standard cell libraries (SkyWater 130nm / FreePDK45).
- Static Timing Analysis (STA): timing paths, arrival times, required times, slack analysis, and fixing setup/hold timing violations.
- Clock Tree Synthesis (CTS): clock skew, jitter, H-tree distributions, and clock mesh networks.

#### Module 5: Physical ASIC Layout & Tapeout Verification
- The physical design flow: floorplanning, power grid distribution (VDD/VSS rings and stripes), cell placement, and global/detailed routing.
- Physical verification: Design Rule Checking (DRC) for geometric silicon manufacturing constraints; Layout Versus Schematic (LVS) electrical network extraction.
- Open-source tapeout tooling: OpenLane automated RTL-to-GDSII flow; participating in Tiny Tapeout or Efabless multi-project wafer (MPW) runs.

---

## 📑 Seminal Papers & Advanced Textbooks

- **Hennessy, J. L., & Patterson, D. A. (2017).** *Computer Architecture: A Quantitative Approach, 6th Edition*. Morgan Kaufmann.
- **Mutlu, O., & Subramanian, L. (2014).** *Research Problems and Opportunities in Memory Systems*. Supercomputing Frontiers and Innovations, 1(3), 19–55.
- **Weste, N. H., & Harris, D. (2015).** *CMOS VLSI Design: A Circuits and Systems Perspective, 4th Edition*. Pearson.
- **Horowitz, P., & Hill, W. (2015).** *The Art of Electronics, 3rd Edition*. Cambridge University Press.
- **Jouppi, N. P. et al. (2017).** *In-Datacenter Performance Analysis of a Tensor Processing Unit*. Proceedings of the 44th Annual International Symposium on Computer Architecture (ISCA '17), 1–12.

---

## 🛠️ Progressive Labs

### Lab 1: Out-of-Order Execution Core with Tomasulo's Algorithm in SystemVerilog
- **Objective:** Design and simulate a synthesizable 2-wide out-of-order execution core with reservation stations, register renaming, and a Reorder Buffer in SystemVerilog.
- **Deliverables:**
  - SystemVerilog RTL modules implementing issue, execution, writeback, and retirement logic.
  - Cycle-accurate simulation testbench running under Verilator executing compiled C benchmarks.
- **Acceptance Criteria:**
  - Successfully resolves WAR and WAW register hazards via register renaming with zero simulation deadlocks.
  - The core must achieve an Instructions Per Cycle (IPC) $\ge 1.4$ on tight loop dependency benchmarks, passing 10,000 randomized arithmetic instruction fuzzing tests.

### Lab 2: Multi-Level MESI Cache Coherence Protocol in gem5
- **Objective:** Implement and evaluate a multi-core MESI directory cache coherence protocol in the gem5 simulator using the Ruby memory subsystem.
- **Deliverables:**
  - SLICC (Specification Language for Implementing Cache Coherence) state machine files defining transitions, invalidations, and writeback responses.
  - Benchmarking configuration evaluating multi-threaded memory access patterns across 8 CPU cores.
- **Acceptance Criteria:**
  - Protocol state transitions verify 100% adherence to single-writer multiple-reader coherence invariants with zero deadlocks or livelocks.
  - Automated gem5 Ruby test suite completes across parallel stress workloads with 0 assertion failures.

### Lab 3: ASIC Standard Cell Layout and Timing Closure via OpenLane Flow
- **Objective:** Take a synthesizable 32-bit pipelined ALU or cryptographic AES accelerator from SystemVerilog RTL through the complete open-source OpenLane ASIC flow down to tapeout-ready GDSII silicon layout on the SkyWater 130nm process node.
- **Deliverables:**
  - Synthesis, floorplanning, placement, clock-tree synthesis, and routing configuration scripts.
  - Final GDSII layout file, Static Timing Analysis (STA) timing reports, and power dissipation estimates.
- **Acceptance Criteria:**
  - Zero setup timing violations and zero hold timing violations at a target clock frequency of $100 \text{ MHz}$ under worst-case corner analysis.
  - Layout passes 100% Design Rule Checking (DRC) and Layout Versus Schematic (LVS) verification with zero manufacturing violations via Magic and Netgen.

---

## 🏆 Capstone Build Deliverable

### Tapeout-Ready 32-bit RISC-V SoC with AXI Bus, Peripherals, and Silicon DRC/LVS Verification

A complete, production-grade 32-bit RISC-V System-on-Chip (SoC) designed in SystemVerilog, verified through extensive testbenches, and hardened into a physical silicon tapeout deliverable for manufacturing via Tiny Tapeout or Efabless SkyWater 130nm MPW.

```text
+-----------------------------------------------------------------------------------+
|                        TAPEOUT-READY RISC-V SOC ASIC                              |
|                                                                                   |
|  +--------------------------------+       +------------------------------------+  |
|  | RV32I Pipelined CPU Core       | <===> | Memory Controller & SRAM (8 KB)    |  |
|  | (5-Stage, BPU, Timer Interrupt)|       +------------------------------------+  |
|  +--------------------------------+                          ^                    |
|                 ^                                            |                    |
|                 |                                            v                    |
|  ===============+================== AXI4-Lite Crossbar ======+==================  |
|                 |                          |                         |            |
|                 v                          v                         v            |
|       +-------------------+      +-------------------+      +-------------------+ |
|       | UART Controller   |      | GPIO Controller   |      | SPI Flash Master  | |
|       +-------------------+      +-------------------+      +-------------------+ |
+-----------------------------------------------------------------------------------+
```

#### System Architecture & Specifications
1. **Processor Core:** 32-bit RISC-V (RV32I / RV32E) pipelined CPU core supporting user and machine execution modes, hardware timer, and vectored interrupt controller.
2. **On-Chip Interconnect & Memory:** AXI4-Lite or Wishbone crossbar matrix connecting the CPU to 8 KB of on-chip single-cycle SRAM and memory-mapped peripheral registers.
3. **Integrated Peripherals:** Full-duplex 115200-baud UART transceiver, configurable GPIO controller, hardware PWM timers, and SPI master interface for external flash booting.
4. **Physical Implementation:** Hardened into physical GDSII layout using the open-source SkyWater 130nm PDK and OpenLane flow, fully routed within standard cell rows and bonded to physical I/O pad rings.

#### Verification & Acceptance Criteria
- **RTL & Software Verification:** The SoC must boot freestanding C firmware from simulated SPI flash memory, execute string printing over UART, and compute arithmetic benchmarks inside a Cocotb / Verilator testbench with 100% test pass.
- **Physical Silicon DRC & LVS Clean:** The generated GDSII layout must achieve zero DRC errors in Magic and zero LVS discrepancies in Netgen, with positive setup and hold timing slack ($\ge +0.5 \text{ ns}$) under all PVT (Process, Voltage, Temperature) corners.
- **Test Commands:**
  ```bash
  # Run complete RTL testbench and firmware execution in Verilator
  make sim_soc
  # Run Cocotb Python verification test suite
  pytest tests/test_soc_cocotb.py -v
  # Execute automated OpenLane RTL-to-GDSII flow
  flow.tcl -design my_riscv_soc -tag tapeout_run
  # Run physical verification checks
  make verify_drc_lvs
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

- **Sequential Flow:** [[T04 - Advanced Graphics and Vision|← Advanced Graphics and Vision]] | [[00 - Start Here|Start Here]] | [[T07 - TinyML and Edge AI|TinyML and Edge AI →]]
