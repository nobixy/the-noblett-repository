---
block_id: "Block 14"
title: "Computer Architecture & Digital Design"
term: "Year 2 Spring"
status: not-started
hours_estimate: 200
hours_actual: 0
primary_resource: "Onur Mutlu, DDCA (ETH Zürich) & Harris & Harris RISC-V Edition"
milestone: "Pipelined RISC-V core in Verilog runs compiled C program"
date_started: ""
date_completed: ""
---

# Block 14 — Computer Architecture & Digital Design

> [!INFO] Block Overview
> - **Term / Position:** Year 2 Spring
> - **Estimated Hours:** ~200 hrs
> - **Status:** `not-started`
> - **Primary Resource:** Onur Mutlu, DDCA (ETH Zürich) & Harris & Harris RISC-V Edition
> - **Key Milestone:** Pipelined RISC-V core in Verilog runs compiled C program

---

## 🎯 Why This Block Matters
How the CPU actually executes instructions at the gate and pipeline level. The foundation for hardware systems engineering.

---

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

## 🏁 Done When
> [!IMPORTANT]
> Your hardware CPU executes a real C program compiled with `riscv64-unknown-elf-gcc`.

---

## 📝 Study Notes, Psets & Proofs
*(Atomic notes, problem set proofs, and project notes)*

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- MIT 6.1910 / 6.004 (OCW); Berkeley CS61C Project 3; Patterson & Hennessy, Computer Organization and Design RISC-V.
