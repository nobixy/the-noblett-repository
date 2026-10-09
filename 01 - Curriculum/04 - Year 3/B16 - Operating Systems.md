---
block_id: "Block 16"
title: "Operating Systems (MIT 6.1810 & OSTEP)"
category: "core"
subject: "Computer Engineering"
term: "Year 3 Fall"
status: not-started
prerequisites:
  - "B09 - Computer Systems"
hours_estimate: 200
hours_actual: 0
primary_resource: "MIT 6.1810 (pdos.csail.mit.edu/6.1810) & Arpaci-Dusseau (OSTEP)"
milestone: "All xv6 labs pass make grade + minimal kernel boots on QEMU"
date_started: ""
date_completed: ""
tier: "Tier 1 - Core"
job_ready: 4 # job-ready path, phase 4 (DR-003)
aliases: ["Operating Systems"]
---

# Block 16 — Operating Systems (MIT 6.1810 & OSTEP)

[[00 - Start Here|Start Here]] / [[00 - Start Here#The Path|The Path]] / [[Systems Index|Systems Index]]

> [!INFO] Block Overview
> - **Term / Position:** Year 3 Fall
> - **Estimated Hours:** ~200 hrs
> - **Status:** `not-started`
> - **Primary Resource:** MIT 6.1810 (pdos.csail.mit.edu/6.1810) & Arpaci-Dusseau (OSTEP)
> - **Key Milestone:** All xv6 labs pass make grade + minimal kernel boots on QEMU

---

## 📚 Curriculum Tier: Tier 1 - Core
> **Tier 1 - Core**: Must complete before advancing.

## 🎯 Why This Block Matters
The kernel is the ultimate low-level abstraction manager: virtual memory, traps, scheduling, locks, and file systems.

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[B09 - Computer Systems|Computer Systems]]


## 📖 Primary Syllabus & Core Content
- [ ] Prep: Reread Ward, How Linux Works — all of it, fast
- [ ] OSTEP readings: Virtualization (CPU, memory), Concurrency (locks, condition variables, semaphores), Persistence (I/O, disks, filesystems)
- [ ] xv6 Kernel on RISC-V: Architecture, source code walkthrough
- [ ] Labs: util, syscall, page tables, traps, copy-on-write, networking, locks, file system, mmap

---

## 🛠️ Build Requirement
Complete every single MIT 6.1810 xv6 lab in `c` using `gcc`, debugged with `gdb`, tested via `make grade` on `qemu`. Then: write a freestanding bootable microkernel in `c` and `risc-v` assembly that boots on `qemu`, initializes SV39 page tables, configures UART and timer interrupts, and preemptively context switches between two isolated user-space processes.

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> All xv6 labs pass with full points on `make grade`, and your custom minimal kernel boots on QEMU and schedules two processes.

---

## 🔎 Verified Resources (DR-004, checked 2026-10-09)
**Verdict:** KEEP. `make grade` is a real autograder.
- **MIT 6.1810** (2025 labs): pdos.csail.mit.edu/6.1810/2025/schedule.html; OSTEP (free): ostep.org.

---

## 📝 Study Notes, Psets & Proofs

*Your atomic notes, problem-set proofs, and build notes go here — written by you, from a blank page.*

> [!TIP]- Check your work (only after your own blank-sheet attempt)
> `make grade` in every xv6 lab.

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- Berkeley CS162 (Pintos); Nanjing University OS (jyy); Tanenbaum, Modern Operating Systems; Love, Linux Kernel Development.

---

## ➡️ Next Steps
- **Topic Hub:** [[Systems Index|Systems Index]]
- **Milestone Checklist:** [[00 - Start Here#The Path|The Path]]
- **Sequential Block Navigation:**
  - Previous: [[B15 - Probability|Block 15 — Probability]] / [[B15a - Signals and Systems Bridge|Block 15a — Signals and Systems Bridge]]
  - Overview: [[00 - Start Here|Start Here]]
  - Next: [[B17 - Software Construction|Block 17 — Software Construction]]

- **Sequential Flow:** [[B15a - Signals and Systems Bridge|← Signals and Systems Bridge]] | [[00 - Start Here|Start Here]] | [[B17 - Software Construction|Software Construction →]]
