---
block_id: "Block 23a"
title: "Parallel Computing (Stanford CS149)"
category: "core"
subject: "Computer Science"
term: "Year 4 Fall"
status: not-started
prerequisites:
  - "B14 - Computer Architecture"
  - "B16 - Operating Systems"
hours_estimate: 140
hours_actual: 0
primary_resource: "Stanford CS149 Parallel Computing (public assignments on GitHub)"
milestone: "CS149 assignments 1–3 done: SIMD/multi-core speedups, task-graph thread pool, CUDA renderer correct and fast"
date_started: ""
date_completed: ""
tier: "Tier 1 - Core"
aliases: ["Parallel Computing", "E4 - Parallel Computing"]
---

# Block 23a — Parallel Computing (Stanford CS149)

[[00 - Start Here|Start Here]] / [[00 - Start Here#The Path|The Path]] / [[Systems Index|Systems Index]]

> [!INFO] Block Overview
> - **Term / Position:** Year 4 Fall
> - **Estimated Hours:** ~140 hrs
> - **Status:** `not-started`
> - **Primary Resource:** Stanford CS149 Parallel Computing (public assignments on GitHub)
> - **Key Milestone:** CS149 assignments 1–3 done: SIMD/multi-core speedups, task-graph thread pool, CUDA renderer correct and fast
> - **Added by:** [[DR-004 - Content Overhaul|DR-004]] (2026-10-09)

---

## 📚 Curriculum Tier: Tier 1 - Core

## 🎯 Why This Block Matters
Single-core performance stopped scaling years ago. Everything fast today — servers, phones, GPUs, ML training — is parallel. This block was the optional E4 elective; [[DR-004 - Content Overhaul|DR-004]] makes it core because GPUs and multi-core are now the default machine, and because Block 25a (Deep Learning) needs it.

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[B14 - Computer Architecture|Computer Architecture]]
- [[B16 - Operating Systems|Operating Systems]]

---

## 📖 Primary Syllabus & Core Content
- [ ] Parallel programming models: SIMD, multi-core threads, tasks, data-parallel
- [ ] Performance analysis: work, span, speedup, memory-bandwidth bounds
- [ ] Cache coherence and memory consistency
- [ ] Synchronization, locks, lock-free techniques
- [ ] GPU architecture and CUDA programming
- [ ] Domain-specific parallelism (graphs, deep-learning kernels)

---

## 🛠️ Build Requirement
Stanford CS149 assignments from the public `stanford-cs149` GitHub repositories: asst1 (ISPC/SIMD and multi-core speedups), asst2 (task-graph scheduling with your own thread pool), asst3 (CUDA circle renderer). Optional: the `cs149gpt` attention-kernel assignment. Run each on your own Linux machine; profile with `perf` and NVIDIA Nsight.

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> Each assignment's reference checker reports correct output; your speedups are within the ranges the handouts call good; your thread pool passes ThreadSanitizer with zero reports.

---

## 🔎 Verified Resources (DR-004, checked 2026-10-09)
- **Stanford CS149** (Fall 2025 site, lecture slides): gfxcourses.stanford.edu/cs149/fall25; assignments: github.com/stanford-cs149 (asst1, asst2, asst3, intro_to_cuda, cs149gpt).
- 💲 CUDA work needs an NVIDIA GPU. Free alternative: a free hosted GPU notebook tier (e.g. Google Colab) for asst3 and the CUDA tutorial; asst1–2 run on any multi-core CPU.
- Free companion text: *Dive Into Systems* chapters on parallelism (diveintosystems.org).

---

## 📝 Study Notes, Psets & Proofs

*Your atomic notes, problem-set proofs, and build notes go here — written by you, from a blank page.*

> [!TIP]- Check your work (only after your own blank-sheet attempt)
> The checkers and reference timings shipped with each assignment; ThreadSanitizer; `perf`.

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- CMU 15-418/618 Parallel Computer Architecture and Programming (same lineage); Herlihy & Shavit, *The Art of Multiprocessor Programming* 💲.

---

## ➡️ Next Steps
- **Topic Hub:** [[Systems Index|Systems Index]] | [[00 - Start Here#The Path|The Path]]
- **Sequential Flow:** [[B23 - Distributed Systems|← Distributed Systems]] | [[00 - Start Here|Start Here]] | [[B24 - Theory of Computation|Theory of Computation →]]
