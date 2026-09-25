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
Complete every single MIT 6.1810 xv6 lab, graded with `make grade`. Then: write a minimal bootable kernel from scratch that boots on QEMU and context switches between two user processes.

---

## 🏁 Done When
> [!IMPORTANT]
> All xv6 labs pass with full points on `make grade`, and your custom minimal kernel boots on QEMU and schedules two processes.

---

## 📝 Study Notes, Psets & Proofs
*(Atomic notes, problem set proofs, and project notes)*

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- Berkeley CS162 (Pintos); Nanjing University OS (jyy); Tanenbaum, Modern Operating Systems; Love, Linux Kernel Development.
