---
block_id: "Block 4"
title: "From NAND to Tetris (Hardware & Software Hierarchy)"
category: "core"
term: "Year 1 January Intensive"
status: not-started
prerequisites:
  - "CS61A"
hours_estimate: 150
hours_actual: 0
primary_resource: "nand2tetris.org & The Elements of Computing Systems, 2nd ed."
milestone: "A Jack program you wrote runs on the CPU you built"
date_started: ""
date_completed: ""
tier: "Tier 1 - Core"
---

# Block 4 — From NAND to Tetris (Hardware & Software Hierarchy)

[[00 - Dashboard|Dashboard]] / [[Checklist|Checklist]] / [[Hardware Index|Hardware Index]]

> [!INFO] Block Overview
> - **Term / Position:** Year 1 January Intensive
> - **Estimated Hours:** ~150 hrs
> - **Status:** `not-started`
> - **Primary Resource:** nand2tetris.org & The Elements of Computing Systems, 2nd ed.
> - **Key Milestone:** A Jack program you wrote runs on the CPU you built

---

## 📚 Curriculum Tier: Tier 1 - Core
> **Tier 1 - Core**: Must complete before advancing.

## 🎯 Why This Block Matters
Build a whole computer, from elementary logic gates to a running high-level game, in one month. De-mystifies the entire computer abstraction stack.

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[CS61A]]


## 📖 Primary Syllabus & Core Content
- [ ] December Prep: Read hardware half of Justice, How Computers Really Work
- [ ] Project 1: Boolean Logic (Nand to basic gates, Mux, Dmux)
- [ ] Project 2: Boolean Arithmetic (Half Adder, Full Adder, ALU)
- [ ] Project 3: Sequential Logic (DFF, Bit, Register, RAM, Program Counter)
- [ ] Project 4: Machine Language (Hack assembly programming)
- [ ] Project 5: Computer Architecture (Memory, CPU, Hack platform)
- [ ] Project 6: Assembler (Assembly to binary translation)
- [ ] Projects 7-8: Virtual Machine (Stack arithmetic and branching/function call VM)
- [ ] Projects 9-11: High-Level Language & Compiler (Jack language, lexer, parser, code generator)
- [ ] Project 12: Operating System (Memory management, math, graphics, string/array OS library)

---

## 🛠️ Build Requirement
Complete all twelve Nand2Tetris projects using the Hardware Simulator, `python` (or `c` / `rust`) for the software suite, and Hack `assembly` in `jack`:
1. **Hardware Suite (Projects 1–5)**: Design chips in HDL: logic gates → 16-bit ALU → registers & RAM → Hack CPU → complete computer architecture, verified with hardware test scripts.
2. **Software Suite (Projects 6–8)**: Implement Hack assembler, two-tier virtual machine translator, and runtime stack in `python` or `c`.
3. **Compiler & OS (Projects 9–12)**: Implement full syntax analyzer and code generator for the `jack` language, and write the complete Hack standard library OS.
4. **Toolchain & Verification**: Automated regression testing in `bash`, version-controlled with `git`.

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> A non-trivial Jack program you wrote runs successfully on the CPU and architecture you built.

---

## 📝 Study Notes, Psets & Proofs

*Your atomic notes, problem-set proofs, and build notes go here — written by you, from a blank page.*

> [!TIP]- Check your work (only after your own blank-sheet attempt)
> The `.tst`/`.cmp` test scripts that ship with each project. A chip or program is done when its script passes.

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- No real substitute. Do it.

---

## ➡️ Next Steps
- **Topic Hub:** [[Hardware Index|Hardware Index]] | [[Checklist|Master Checklist]]
- **Sequential Flow:** [[Physics I|← 03 - Physics I]] | [[00 - Dashboard|Dashboard]] | [[Differential Equations Bridge|04a - Differential Equations Bridge (optional) →]]
