---
block_id: "Block 17"
title: "Computer Architecture & Digital Design"
category: "core"
term: "Year 2 Spring"
status: not-started
prerequisites:
  - "Computer Systems"
hours_estimate: 200
hours_actual: 0
primary_resource: "Onur Mutlu, DDCA (ETH Zürich) & Harris & Harris RISC-V Edition"
milestone: "Pipelined RISC-V core in Verilog runs compiled C program"
date_started: ""
date_completed: ""
tier: "Tier 2 - Support"
---

# Block 17 — Computer Architecture & Digital Design

[[00 - Dashboard|Dashboard]] / [[Checklist|Checklist]] / [[Hardware Index|Hardware Index]]

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
- [[Computer Systems]]


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
- **Topic Hub:** [[Hardware Index|Hardware Index]] | [[Checklist|Master Checklist]]
- **Sequential Flow:** [[Computer Systems|← Computer Systems]] | [[00 - Dashboard|Dashboard]] | [[Operating Systems|Operating Systems →]]
