---
block_id: "Block 27"
title: "Parallel Computing"
category: "core"
term: "Year 3 Spring"
status: not-started
prerequisites:
  - "Computer Architecture"
  - "Operating Systems"
hours_estimate: 140
hours_actual: 0
primary_resource: "Stanford CS149"
milestone: "Write a high-performance CUDA kernel and lock-free thread pool"
date_started: ""
date_completed: ""
tier: "Tier 1 - Core"
---

# Block 27 — Parallel Computing

[[00 - Dashboard|Dashboard]] / [[Checklist|Checklist]] / [[Systems Index|Systems Index]]

> [!INFO] Block Overview
> - **Term / Position:** Year 3 Spring
> - **Estimated Hours:** ~140 hrs
> - **Status:** `not-started`
> - **Primary Resource:** Stanford CS149: Parallel Computing
> - **Key Milestone:** Write a high-performance CUDA kernel and lock-free thread pool

## 📚 Curriculum Tier: Tier 1 - Core
> **Tier 1 - Core**: Must complete before advancing.

## 🎯 Why This Block Matters
Moore's Law for single-core performance is dead. Modern systems rely on explicit parallelism across multi-core CPUs, GPUs, and SIMD execution. You must learn to write concurrent, lock-free, high-throughput code.

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[Computer Architecture]]
- [[Operating Systems]]

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
- **Topic Hub:** [[Systems Index|Systems Index]] | [[Checklist|Master Checklist]]
- **Sequential Flow:** [[Software Construction|← Software Construction]] | [[00 - Dashboard|Dashboard]] | [[Distributed Systems|Distributed Systems →]]
