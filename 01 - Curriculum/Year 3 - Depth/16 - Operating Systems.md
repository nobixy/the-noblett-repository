---
block_id: "Block 16"
title: "Operating Systems (MIT 6.1810 & OSTEP)"
term: "Year 3 Fall"
status: not-started
hours_estimate: 200
hours_actual: 0
primary_resource: "MIT 6.1810 (pdos.csail.mit.edu/6.1810) & Arpaci-Dusseau (OSTEP)"
milestone: "All xv6 labs pass make grade + minimal kernel boots on QEMU"
date_started: ""
date_completed: ""
---

# Block 16 — Operating Systems (MIT 6.1810 & OSTEP)

[[00 - Dashboard|Dashboard]] / [[Checklist|Checklist]] / [[02 - Notes/Systems/Systems Index|Systems Index]]

> [!INFO] Block Overview
> - **Term / Position:** Year 3 Fall
> - **Estimated Hours:** ~200 hrs
> - **Status:** `not-started`
> - **Primary Resource:** MIT 6.1810 (pdos.csail.mit.edu/6.1810) & Arpaci-Dusseau (OSTEP)
> - **Key Milestone:** All xv6 labs pass make grade + minimal kernel boots on QEMU

---

## 🎯 Why This Block Matters
The kernel is the ultimate low-level abstraction manager: virtual memory, traps, scheduling, locks, and file systems.

---

## 📖 Primary Syllabus & Core Content
- [ ] Prep: Reread Ward, How Linux Works — all of it, fast
- [ ] OSTEP readings: Virtualization (CPU, memory), Concurrency (locks, condition variables, semaphores), Persistence (I/O, disks, filesystems)
- [ ] xv6 Kernel on RISC-V: Architecture, source code walkthrough
- [ ] Labs: util, syscall, page tables, traps, copy-on-write, networking, locks, file system, mmap

---

## 🛠️ Build Requirement
Complete every single MIT 6.1810 xv6 lab in `c` using `gcc`, debugged with `gdb`, tested via `make grade` on `qemu`. Then: write a freestanding bootable microkernel in `c` and `risc-v` assembly that boots on `qemu`, initializes SV39 page tables, configures UART and timer interrupts, and preemptively context switches between two isolated user-space processes.

---

## 🏁 Done When
> [!IMPORTANT]
> All xv6 labs pass with full points on `make grade`, and your custom minimal kernel boots on QEMU and schedules two processes.

---

## 📝 Study Notes, Psets & Proofs

*Your atomic notes, problem-set proofs, and build notes go here — written by you, from a blank page.*

> [!TIP]- Answer key (open only after a blank-sheet attempt)
> [[16 - Operating Systems — Worked Proofs]]

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- Berkeley CS162 (Pintos); Nanjing University OS (jyy); Tanenbaum, Modern Operating Systems; Love, Linux Kernel Development.

---

## 🧭 Navigation
- **Topic Hub:** [[02 - Notes/Systems/Systems Index|Systems Index]]
- **Milestone Checklist:** [[Checklist|Checklist]]
- **Sequential Block Navigation:**
  - Previous: [[01 - Curriculum/Year 2 - Systems/15 - Probability|Block 15 — Probability]] / [[01 - Curriculum/Year 2 - Systems/15a - Signals and Systems Bridge|Block 15a — Signals and Systems Bridge]]
  - Overview: [[00 - Dashboard|Dashboard]]
  - Next: [[01 - Curriculum/Year 3 - Depth/17 - Software Construction|Block 17 — Software Construction]]
