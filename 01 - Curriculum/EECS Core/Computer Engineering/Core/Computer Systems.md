---
block_id: "Block 16"
title: "Computer Systems: A Programmer's Perspective (CS:APP)"
category: "core"
term: "Year 2 Fall"
status: not-started
prerequisites:
  - "C Fluency"
  - "Nand2Tetris"
hours_estimate: 200
hours_actual: 0
primary_resource: "Bryant & O'Hallaron, CS:APP, 3e & CMU 15-213 Lectures"
milestone: "All 7 CS:APP labs pass; malloc lab score ≥90; objdump decoded cold"
date_started: ""
date_completed: ""
tier: "Tier 1 - Core"
---

# Block 16 — Computer Systems: A Programmer's Perspective (CS:APP)

[[00 - Dashboard|Dashboard]] / [[Checklist|Checklist]] / [[Systems Index|Systems Index]]

> [!INFO] Block Overview
> - **Term / Position:** Year 2 Fall
> - **Estimated Hours:** ~200 hrs
> - **Status:** `not-started`
> - **Primary Resource:** Bryant & O'Hallaron, CS:APP, 3e & CMU 15-213 Lectures
> - **Key Milestone:** All 7 CS:APP labs pass; malloc lab score ≥90; objdump decoded cold

---

## 📚 Curriculum Tier: Tier 1 - Core
> **Tier 1 - Core**: Must complete before advancing.

## 🎯 Why This Block Matters
The single highest-payoff course in CS. Explains everything between your high-level program and raw physical hardware.

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[C Fluency]]
- [[Nand2Tetris]]


## 📖 Primary Syllabus & Core Content
- [ ] Ch 1: A Tour of Computer Systems
- [ ] Ch 2: Representing and Manipulating Information (bit-level operations, integer/floating-point representation)
- [ ] Ch 3: Machine-Level Representation of Programs (x86-64 assembly, loops, stack frames, buffer overflows)
- [ ] Ch 4: Processor Architecture (Y86-64 pipeline)
- [ ] Ch 5: Optimizing Program Performance (instruction-level parallelism, branch prediction, profiling)
- [ ] Ch 6: The Memory Hierarchy (SRAM, DRAM, locality, cache memories)
- [ ] Ch 7: Linking (relocation, symbol resolution, dynamic shared libraries)
- [ ] Ch 8: Exceptional Control Flow (signals, processes, non-local jumps)
- [ ] Ch 9: Virtual Memory (paging, address translation, dynamic memory allocation)
- [ ] Ch 10: System-Level I/O (Unix I/O, file descriptors)
- [ ] Ch 11: Network Programming (client-server architecture, sockets)
- [ ] Ch 12: Concurrent Programming (processes, I/O multiplexing, threads, synchronization, race conditions)

---

## 🛠️ Build Requirement
Complete all seven canonical CMU 15-213 (CS:APP) systems labs in `c` on `linux` using `gcc`, `gdb`, `make`, `valgrind`, and `x86` `assembly`:
1. **Data Lab & Bomb Lab**: Bitwise manipulation in `c`, reverse engineering binary bombs in `gdb` via disassembled `x86` `assembly`.
2. **Attack Lab**: Stack smashing buffer overflows and Return-Oriented Programming (ROP) gadget chains.
3. **Cache Lab**: Matrix transpose cache simulator and cache-miss minimization in `c`.
4. **Shell Lab & Malloc Lab**: Unix shell with job control and signals, dynamic memory allocator with segregated free lists passing `valgrind` tests with $\ge 90$ throughput/utilization score.
5. **Proxy Lab**: Multi-threaded concurrent caching HTTP web proxy with POSIX threads and robust socket I/O.

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> All seven labs pass cleanly; Malloc Lab scores ≥ 90 on space utilization and throughput; you read objdump output without flinching.

---

## 📝 Study Notes, Psets & Proofs

*Your atomic notes, problem-set proofs, and build notes go here — written by you, from a blank page.*

> [!TIP]- Check your work (only after your own blank-sheet attempt)
> The grading drivers and traces that ship with each self-study lab ([csapp.cs.cmu.edu/3e/labs.html](https://csapp.cs.cmu.edu/3e/labs.html)).

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- Berkeley CS61C (cs61c.org); Dive Into Systems (free online).

---

## ➡️ Next Steps
- **Topic Hub:** [[Systems Index|Systems Index]] | [[Checklist|Master Checklist]]
- **Sequential Flow:** [[Linear Algebra|← Linear Algebra]] | [[00 - Dashboard|Dashboard]] | [[Computer Architecture|Computer Architecture →]]
