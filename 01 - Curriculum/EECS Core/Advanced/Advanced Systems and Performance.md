---
block_id: "Block 42"
track_id: "Track 2"
title: "Systems and Performance"
category: "advanced"
term: "Years 4 & 5"
status: not-started
prerequisites:
  - "C Fluency"
  - "Computer Systems"
  - "Computer Architecture"
  - "Operating Systems"
  - "Databases"
target_profile: "Systems Performance Engineer, Storage Engine Architect, High-Performance Infrastructure Developer"
aliases: [Track 2 - Systems and Performance, Track 2 - Performance Engineering and Storage Systems]
tier: "Tier 3 - Depth"
hours_estimate: 400
hours_actual: 0
---

# Track 2: Systems and Performance

> [!INFO] Track Overview
> - **Track ID:** Track 2
> - **Prerequisites:** [[C Fluency]], [[Computer Systems]], [[Computer Architecture]], [[Operating Systems]], [[Databases]]
> - **Target Profile:** Systems Performance Engineer, Storage Engine Architect, High-Performance Infrastructure Developer
> - **Structure:** Two core courses plus three progressive labs and one comprehensive capstone build deliverable.
> - **Curriculum Position:** Elective specialization block across Years 4 & 5 (*"Two deep beats six shallow"*).

---

## 🎯 Why This Track Matters

With the physical demise of Dennard scaling and the deceleration of Moore's Law, software can no longer rely on automatic hardware clock speed increases to deliver performance gains. Modern computing demands what Charles Leiserson terms "performance engineering at the top": extracting maximum efficiency from existing hardware through deep hardware-software co-design, cache-aware data layout, SIMD vectorization, lock-free concurrency, and asynchronous I/O pipelines.

This track equips students with the empirical and theoretical skills required to build ultra-low-latency, high-throughput systems infrastructure: storage engines, operating system internals, database kernels, and distributed backbones. Students learn to profile real hardware bottlenecks using hardware performance counters (PMUs) and eBPF kernel tracing, design concurrent data structures provably immune to data races and ABA hazards, and architect systems capable of saturating multi-gigabyte/sec PCIe NVMe buses and 100GbE networks.

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[C Fluency]]
- [[Computer Systems]]
- [[Computer Architecture]]
- [[Operating Systems]]
- [[Databases]]




## 📚 Core Courses

### Course 1: Software Systems Performance Engineering (MIT 6.172 Equivalent)

This course teaches students how to model, measure, and optimize software systems to extract peak operational efficiency from modern microprocessors.

#### Module 1: The Modern Microarchitectural Memory Hierarchy
- Hardware caches: L1i, L1d, unified L2, and shared L3 caches; cache associativity, cache line size ($64 \text{ bytes}$), write-back vs write-through policies.
- Spatial and temporal locality: matrix layouts, strided access penalties, cache-conscious matrix transposition and blocking algorithms.
- Hardware prefetchers: stream prefetchers, stride prefetchers, and software prefetch instructions (`_mm_prefetch`).
- False sharing: cache-line invalidation across multiple CPU cores; cache padding and alignment (`alignas(64)`).

#### Module 2: Compiler Optimizations, Vectorization & Assembly Analysis
- Understanding compiler optimizations: dead code elimination, loop unrolling, loop vectorization, function inlining, and profile-guided optimization (PGO).
- Assembly inspection: x86-64 calling conventions, register allocation pressure, and instruction-level parallelism (ILP).
- SIMD programming: Intel AVX-512, AVX2, and ARM NEON intrinsics; vector packing, masking, blending, and horizontal reduction operations.
- Branch prediction: static vs dynamic branch prediction (two-level adaptive predictors, TAGE); branches in inner loops and branchless programming patterns.

#### Module 3: Multicore Concurrency & Shared-Memory Multiprocessing
- Shared-memory parallel programming models: pthreads, OpenMP, and task-based work-stealing runtimes (Cilk).
- Critical section synchronization: mutexes, spinlocks with exponential backoff, reader-writer locks, and read-copy-update (RCU).
- Lock contention and Amdahl's Law vs Gustafson's Law: analytical modeling of parallel scalability limits.

#### Module 4: Instrumentation, Measurement & Dynamic Tracing
- Hardware Performance Monitoring Units (PMUs): measuring cache misses, branch mispredictions, stalled CPU cycles, and IPC (Instructions Per Cycle).
- Linux performance tools: `perf stat`, `perf record`, `perf report`, and generating flame graphs for call-stack latency attribution.
- Dynamic kernel and user-space tracing via Extended Berkeley Packet Filters (eBPF) using `bpftrace` and `bcc`.

#### Module 5: Roofline Performance Modeling & I/O Subsystems
- The Roofline Model: operational intensity (FLOPs/byte), memory bandwidth boundaries, and compute bounds.
- Memory-mapped files (`mmap`), page cache internals, direct I/O (`O_DIRECT`), and non-blocking asynchronous event loops.
- Linux `io_uring`: submission queue (SQ) and completion queue (CQ) ring buffers for zero-syscall I/O.

---

### Course 2: Multiprocessor Programming & Advanced Database Storage (Herlihy & Shavit / CMU 15-721)

This course dives into lock-free concurrent algorithm design, memory consistency models, and the internal architecture of high-performance database engines.

#### Module 1: Concurrent Synchronization & Hardware Memory Models
- Sequential consistency, x86 Total Store Order (TSO), and ARM/RISC-V relaxed memory models.
- Atomic read-modify-write operations: Compare-And-Swap (CAS), Fetch-And-Add (FAA), Test-And-Set (TAS).
- Progress conditions: wait-free, lock-free, obstruction-free, and starvation-free guarantees.
- Linearizability: establishing verification linearization points for concurrent data structures.

#### Module 2: Lock-Free Data Structures & Memory Reclamation
- The ABA problem: hazard pointers, tagged reference counters, and epoch-based reclamation (EBR).
- Lock-free stacks (Treiber stack) and queues (Michael-Scott queue).
- Lock-free search structures: Harris's linked list, concurrent skip lists, and split-ordered hash tables.
- Hardware Transactional Memory (Intel TSX, ARM TME): transactional aborts, fallbacks, and lock elision.

#### Module 3: Database Storage Internals & Indexing Structures
- Write-optimized storage: Log-Structured Merge-trees (LSM-trees), compaction algorithms (size-tiered vs leveled), and Bloom filter tuning.
- Read-optimized indexing: cache-conscious B+-trees, Masstree, and latch-free Bw-trees using epoch managers and mapping tables.
- Variable-length key compression and prefix truncation.

#### Module 4: Logging, Recovery & Transaction Protocols
- Write-Ahead Logging (WAL) and the ARIES recovery method: physiological logging, Compensation Log Records (CLRs), and the Analysis-Redo-Undo phases.
- Concurrency control algorithms: Two-Phase Locking (2PL), Timestamp Ordering (T/O), and Multi-Version Concurrency Control (MVCC) with vacuuming strategies.
- Optimistic Concurrency Control (OCC) and TicToc timestamp-based validation.

#### Module 5: Query Execution Engines & Vectorized Processing
- Volcano iterator model vs block-oriented processing.
- Vectorized query execution (Moneydb/X100 paradigm): cache-friendly column-store processing and SIMD-accelerated filter evaluations.
- Just-In-Time (JIT) query compilation using LLVM: compiling SQL queries into native machine instructions to eliminate virtual dispatch.

---

## 📑 Seminal Papers & Advanced Textbooks

- **Leiserson, C. E., Thompson, N. C., Emer, J. S., Kuszmaul, B. C., Lampson, B. W., Sanchez, D., & Schardl, T. B. (2020).** *There's plenty of room at the Top: What will drive computer performance after Moore's law?* Science, 368(6495), Article eaam9744.
- **Herlihy, M., & Moss, J. E. B. (1993).** *Transactional Memory: Architectural Support for Lock-Free Data Structures*. Proceedings of the 20th Annual International Symposium on Computer Architecture (ISCA '93), 289–300.
- **Pavlo, A., Angulo, G., Arulraj, J., Lin, H., Lin, J., Menon, P., Mowry, T. C., Peschel, R., Quah, L., Schoenbach, R., Tang, B., & Zhang, J. (2017).** *Self-Driving Database Management Systems*. Proceedings of the 8th Biennial Conference on Innovative Data Systems Research (CIDR '17).
- **Gregg, B. (2020).** *Systems Performance: Enterprise and the Cloud, 2nd Edition*. Addison-Wesley Professional.
- **Herlihy, M., Shavit, N., Luchangco, V., & Spear, M. (2020).** *The Art of Multiprocessor Programming, 2nd Edition*. Morgan Kaufmann.

---

## 🛠️ Progressive Labs

### Lab 1: Cache-Conscious Matrix Transposition and AVX-512 SIMD Vectorization
- **Objective:** Optimize out-of-place and in-place dense square matrix transposition ($N = 16384$) in C/C++ to saturate physical hardware memory bandwidth.
- **Deliverables:**
  - Implementation benchmarking naive row/column loops, recursive cache-oblivious tiling, and explicit AVX-512 vector register intrinsics.
  - Flame graphs and cache-miss metrics generated via Linux `perf`.
- **Acceptance Criteria:**
  - The vectorized implementation must achieve $\ge 85\%$ of STREAM benchmark memory bandwidth saturation on the host test machine.
  - Cache profiling confirms $> 4.0\times$ speedup and $> 90\%$ reduction in L1/L2 cache misses compared to naive non-tiled loops.

### Lab 2: Lock-Free Skip List with Epoch-Based Reclamation in C++
- **Objective:** Construct a concurrent, lock-free skip list supporting atomic inserts, lookups, and deletions under arbitrary concurrent thread contention.
- **Deliverables:**
  - Modern C++ implementation using atomic operations (`std::atomic<T>`) and an epoch-based memory reclamation manager.
  - Multi-threaded stress test harness simulating read-heavy ($90\%$ read, $10\%$ write) and write-heavy ($50\%$ read, $50\%$ write) workloads.
- **Acceptance Criteria:**
  - Zero memory leaks, zero segmentation faults, and zero data races verified under ThreadSanitizer (`clang++ -fsanitize=thread`).
  - Total lookup throughput across 16 threads must scale linearly and benchmark $> 1,500,000 \text{ operations/sec}$.

### Lab 3: High-Throughput Write-Ahead Logging (WAL) & ARIES Crash Recovery
- **Objective:** Implement a crash-recovery subsystem implementing ARIES physiological logging, group commits, and compensation log records (CLRs).
- **Deliverables:**
  - C++ logging module with background buffer flushers and checkpointing.
  - Recovery manager executing Analysis, Redo, and Undo passes over simulated crashed log files.
- **Acceptance Criteria:**
  - Automated fault injection harness terminates the process with `kill -9` at 50 randomized execution intervals during active transaction commits.
  - Recovery manager successfully restores the database state with 100% committed transaction persistence and zero phantom records.

---

## 🏆 Capstone Build Deliverable

### Production-Grade High-Performance Storage Engine or Kernel/DB Upstream Contribution

An industrial-grade, persistent key-value storage engine engineered in C++ or Rust featuring lock-free concurrency, LSM-tree architecture, and asynchronous NVMe I/O via `io_uring`.

```text
+-----------------------------------------------------------------------------------+
|                        HIGH-PERFORMANCE STORAGE ENGINE                            |
|                                                                                   |
|  [ Concurrent Client Threads ] ---> [ Lock-Free Skip-List MemTable ]              |
|                                                     |                             |
|                                                     v                             |
|  [ Append-Only WAL (io_uring) ] <--- [ Group Commit Coordinator ]                 |
|                                                     |                             |
|                                                     v                             |
|  [ Leveled SSTable Compaction ] <--- [ Background Flush Worker Thread ]           |
|                 |                                                                 |
|                 v                                                                 |
|  [ Direct I/O (O_DIRECT) ] ---------> [ NVMe Block Storage ]                      |
+-----------------------------------------------------------------------------------+
```

#### System Architecture & Specifications
1. **MemTable & Concurrency:** Multi-threaded concurrent lock-free skip list MemTable using epoch-based memory reclamation, supporting non-blocking concurrent writes.
2. **Write-Ahead Logging (WAL):** High-throughput append-only log with group commit batching and direct disk write submissions via Linux `io_uring`.
3. **SSTable Storage & Compaction:** Immutable sorted-string tables (SSTables) with two-level block indexing, fractional cascading, and dynamic Bloom filters; multi-threaded leveled background compaction.
4. **Alternative Capstone Track:** Submit and merge an upstream performance optimization patch to the Linux Kernel, PostgreSQL, or LLVM.

#### Verification & Acceptance Criteria
- **Throughput & Latency:** The storage engine must sustain $> 500,000 \text{ write ops/sec}$ and $> 800,000 \text{ read ops/sec}$ on random 1KB keys/values, with p99 tail latency strictly $< 100 \, \mu\text{s}$.
- **Recovery Integrity:** Must pass a 1,000-iteration randomized crash-injection test suite without a single lost committed transaction or unhandled memory corruptions.
- **Test Commands:**
  ```bash
  # Compile with ThreadSanitizer and AddressSanitizer
  cmake -B build -DCMAKE_BUILD_TYPE=RelWithDebInfo -DENABLE_SANITIZERS=ON && cmake --build build
  # Run full unit and concurrency tests
  ./build/tests/storage_concurrency_test
  # Run benchmark load generator under io_uring
  ./build/benchmarks/db_bench --benchmarks="fillrandom,readrandom" --threads=16 --num=10000000
  ```

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> Assessment criteria go here.

## ➡️ Next Steps & Degree Pathway
- **Curriculum Hub:** [[Specializations Hub|Specializations Hub]]
- **Degree Assignment:**
  - If chosen as **Primary Specialization (Track A)**: Course 1 binds to [[Specialization A1|Block 26 - Specialization A1]] and Course 2 binds to [[Specialization A2|Block 28 - Specialization A2]].
  - If chosen as **Secondary Specialization (Track B)**: Course 1 binds to [[Specialization B1|Block 29 - Specialization B1]] and Course 2 binds to [[Specialization B2|Block 31 - Specialization B2]].
- **Curriculum Roadmap:** [[00 - Dashboard|Dashboard]] / [[Checklist|Checklist]]

- **Sequential Flow:** [[Differential Equations Bridge|← Differential Equations Bridge]] | [[00 - Dashboard|Dashboard]] | [[Rust for Systems Engineering|Rust for Systems Engineering →]]
