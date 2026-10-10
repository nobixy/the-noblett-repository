---
block_id: "Block 14"
stage: "03 - Year 2"
title: "Computer Architecture & Digital Design"
category: "core"
subject: "Computer Engineering"
term: "Year 2 Spring"
status: not-started
prerequisites:
  - "B09 - Computer Systems"
hours_estimate: 200
hours_actual: 0
primary_resource: "Onur Mutlu, DDCA (ETH Zürich) & Harris & Harris RISC-V Edition"
milestone: "Pipelined RISC-V core in Verilog runs compiled C program"
date_started: ""
date_completed: ""
tier: "Tier 2 - Support"
job_ready: 3 # job-ready path, phase 3 (DR-003)
aliases: ["Computer Architecture"]
---

# Block 14 — Computer Architecture & Digital Design

[[00 - Start Here|Start Here]] / [[00 - Start Here#The Path|The Path]] / [[Hardware Index|Hardware Index]]

> [!INFO] Block Overview
> - **Term / Position:** Year 2 Spring
> - **Estimated Hours:** ~200 hrs
> - **Status:** `not-started`
> - **Primary Resource:** Onur Mutlu, DDCA (ETH Zürich) & Harris & Harris RISC-V Edition
> - **Key Milestone:** Pipelined RISC-V core in Verilog runs compiled C program

---

## 📚 Curriculum Tier: Tier 2 - Support
> **Tier 2 - Support**: Strongly recommended for full understanding.

## 🎯 Why This Block Matters
How the CPU actually executes instructions at the gate and pipeline level. The foundation for hardware systems engineering.

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[B09 - Computer Systems|Computer Systems]]


## 📖 Primary Syllabus & Core Content
- [ ] Combinational and sequential logic design in SystemVerilog/Verilog
- [ ] RISC-V ISA specification and instruction encoding
- [ ] Single-cycle and multi-cycle microarchitectures
- [ ] Pipelining: Hazards, stalls, data forwarding, branch prediction
- [ ] Memory systems: Caches (direct mapped, set-associative), replacement policies, write buffers
- [ ] Virtual memory hardware and TLBs
- [ ] I/O and peripheral bus protocols

---

## 🛠️ Build Requirement
Build a 5-stage pipelined RISC-V processor core in Verilog with hazard detection and forwarding. Simulate with Verilator, then run on an FPGA board (Digilent Arty A7 or iCEBreaker).

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> Your hardware CPU executes a real C program compiled with `riscv64-unknown-elf-gcc`.

---

## 🔎 Verified Resources (DR-004, checked 2026-10-09)
**Verdict:** UPGRADE. Added autograded Verilog practice and the current MIT course.
- **HDLBits** (free, autograded Verilog exercises): hdlbits.01xz.net — finish it before the RISC-V core.
- ETH DDCA (Mutlu, free lectures): safari.ethz.ch/digitaltechnik/; **MIT 6.191** current site (Fall 2026): 6191.mit.edu/fall26.
- Free toolchain: Verilator (veripool.org/verilator), YosysHQ oss-cad-suite.
- 💲 FPGA board; free alternative: run the core in Verilator only.

---

## 📝 Study Notes, Psets & Proofs

*Your atomic notes, problem-set proofs, and build notes go here — written by you, from a blank page.*

> [!TIP]- Check your work (only after your own blank-sheet attempt)
> Your own testbenches under Verilator, then the *Done when* test: a C program compiled with riscv64-gcc runs correctly on your core.

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- MIT 6.1910 / 6.004 (OCW, Ward & Halstead *Computation Structures*); Berkeley CS61C Project 3; Patterson & Hennessy, Computer Organization and Design RISC-V.

---

## ➡️ Next Steps
- **Topic Hub:** [[Hardware Index|Hardware Index]] | [[00 - Start Here#The Path|The Path]]
- **Sequential Flow:** [[B13 - Algorithms I|← Algorithms I]] | [[00 - Start Here|Start Here]] | [[B15 - Probability|Probability →]]
