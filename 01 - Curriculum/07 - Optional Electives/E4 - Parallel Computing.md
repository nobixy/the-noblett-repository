---
block_id: "E4"
title: "Parallel Computing"
category: "elective"
subject: "Computer Science"
term: "Year 3 Spring"
status: not-started
prerequisites:
  - "B14 - Computer Architecture"
  - "B16 - Operating Systems"
hours_estimate: 140
hours_actual: 0
primary_resource: "Stanford CS149"
milestone: "Write a high-performance CUDA kernel and lock-free thread pool"
date_started: ""
date_completed: ""
tier: "Tier 3 - Depth"
optional: true # optional elective, outside the ordered Path (DR-002)
aliases: ["Parallel Computing"]
---

# E4 — Parallel Computing

[[00 - Start Here|Start Here]] / [[00 - Start Here#The Path|The Path]] / [[Systems Index|Systems Index]]

> [!INFO] Block Overview
> - **Term / Position:** Year 3 Spring
> - **Estimated Hours:** ~140 hrs
> - **Status:** `not-started`
> - **Primary Resource:** Stanford CS149: Parallel Computing
> - **Key Milestone:** Write a high-performance CUDA kernel and lock-free thread pool

## 📚 Curriculum Tier: Tier 3 - Depth
> **Tier 3 - Depth**: Optional deep dive for specialized mastery.

## 🎯 Why This Block Matters
Moore's Law for single-core performance is dead. Modern systems rely on explicit parallelism across multi-core CPUs, GPUs, and SIMD execution. You must learn to write concurrent, lock-free, high-throughput code.

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[B14 - Computer Architecture|Computer Architecture]]
- [[B16 - Operating Systems|Operating Systems]]

## 📖 Primary Syllabus & Core Content
- [ ] Concurrency vs Parallelism
- [ ] Memory Consistency Models and Cache Coherence
- [ ] SIMD Vectorization
- [ ] GPU Architecture & CUDA Programming
- [ ] Lock-free Data Structures & Synchronization Primitives
- [ ] Message Passing & MPI

## 🛠️ Build Requirement
Complete the core assignments from Stanford CS149, including optimizing a fractal renderer using SIMD intrinsics, writing a multi-threaded web server task queue, and implementing an image processing kernel in CUDA.

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> Your parallel implementation achieves a measurable speedup scaling almost linearly with thread count, and passes ThreadSanitizer with zero race conditions.

## 📝 Study Notes, Psets & Proofs

*Your atomic notes, problem-set proofs, and build notes go here — written by you, from a blank page.*

> [!TIP]- Check your work
> Benchmark your multi-threaded and GPU implementations against single-threaded baselines using `perf` and NVIDIA Nsight.

## ➡️ Next Steps
- **Topic Hub:** [[Systems Index|Systems Index]] | [[00 - Start Here#The Path|The Path]]
- **Sequential Flow:** *Optional elective (E1–E4), outside the ordered [[00 - Start Here#The Path|Path]]; start once the prerequisites above are done.* | [[00 - Start Here|Start Here]]
