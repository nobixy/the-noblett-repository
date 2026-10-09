---
block_id: "Track 8"
track_id: "Track 8"
title: "Rust for Systems Engineering and Formal Verification"
category: "specialization"
subject: "Specialization"
term: "Years 4 & 5"
status: not-started
prerequisites:
  - "B06 - C Fluency"
  - "B09 - Computer Systems"
  - "B16 - Operating Systems"
  - "B17 - Software Construction"
target_profile: "Systems Infrastructure Engineer, High-Assurance Rust Developer, Kernel Architect"
aliases: [Track 8 - Rust for Systems Engineering and Formal Verification, Track 8 - Rust Systems Engineering, "Rust for Systems Engineering"]
tier: "Tier 3 - Depth"
hours_estimate: 400
hours_actual: 0
optional: true # specialization track not yet chosen (DR-001)
primary_resource: "Advanced Rust Systems & Memory Safety Internals + Asynchronous Runtimes, Kernels & Formal Rust Verification"
milestone: "Bootable Multi-Core `no_std` Microkernel with Formally Verified Drivers"
date_started: ""
date_completed: ""
---

# Track 8 — Rust for Systems Engineering and Formal Verification

> [!INFO] Track Overview
> - **Track ID:** Track 8
> - **Prerequisites:** [[B06 - C Fluency|C Fluency]], [[B09 - Computer Systems|Computer Systems]], [[B16 - Operating Systems|Operating Systems]], [[B17 - Software Construction|Software Construction]]
> - **Target Profile:** Systems Infrastructure Engineer, High-Assurance Rust Developer, Kernel Architect
> - **Structure:** Two core courses plus three progressive labs and one comprehensive capstone build deliverable.
> - **Curriculum Position:** Elective specialization block across Years 4 & 5 (*"Two deep beats six shallow"*).

---

## 🎯 Why This Track Matters

For over fifty years, systems infrastructure, operating system kernels, databases, and network runtimes have been written almost exclusively in C and C++. However, empirical telemetry across major software vendors (Microsoft, Google, Apple) reveals that approximately 70% of all high-severity, exploitable vulnerabilities stem from memory safety bugs: use-after-free, double-free, out-of-bounds pointer arithmetic, and data races.

Rust revolutionizes systems programming by introducing a substructural (affine) type system that enforces compile-time ownership, single-writer mutable exclusivity, and strict lifetime boundaries without requiring a runtime garbage collector. However, mastering Rust for professional systems engineering requires moving beyond beginner syntax. True high-assurance systems work demands understanding the formal operational semantics of pointer provenance (Stacked Borrows / Tree Borrows), writing sound encapsulated `unsafe` blocks audited by Miri, implementing lock-free data structures compliant with the C++20/Rust memory models, building asynchronous execution reactors from scratch, and utilizing modern SMT-based deductive model checkers (Kani, Creusot) to mechanically prove software correctness.

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[B06 - C Fluency|C Fluency]]
- [[B09 - Computer Systems|Computer Systems]]
- [[B16 - Operating Systems|Operating Systems]]
- [[B17 - Software Construction|Software Construction]]




## 📚 Core Courses

### Course 1: Advanced Rust Systems & Memory Safety Internals

This course explores the deeper mechanics of the Rust type system, deep unsafe pointer invariants, memory layout control, and lock-free concurrency.

#### Module 1: Substructural Type Semantics & Advanced Lifetimes
- Mathematical foundations of affine type systems: linear vs affine logic; resources that can be consumed at most once.
- Subtyping and variance in Rust: covariance, contravariance, and invariance in generic parameters, lifetime bounds (`'a: 'b`), and raw pointer wrappers (`*const T`, `*mut T`, `NonNull<T>`).
- Higher-Ranked Trait Bounds (HRTBs): universal quantification over lifetimes using `for<'a> Trait<'a>`.
- Phantom types and marker traits: `PhantomData<T>`, `Send`, `Sync`, `Unpin`, and auto-trait mechanics.

#### Module 2: The Unsafe Rust Operational Model & Pointer Provenance
- The formal definition of Undefined Behavior (UB) in Rust: data races, invalid memory access, unaligned pointers, and producing invalid primitive values.
- Operational semantics of pointer tracking: Stacked Borrows and Tree Borrows formal models.
- Interior mutability primitives: `UnsafeCell<T>`, `Cell<T>`, `RefCell<T>`, and why `UnsafeCell` is the sole compiler escape-hatch for shared mutation.
- Using Miri: dynamic UB detection, stacked borrows violations, memory leak analysis, and integer-to-pointer casting provenance tracking.

#### Module 3: Low-Level Memory Layout & Custom Allocators
- Memory layout guarantees: `repr(C)`, `repr(transparent)`, `repr(packed)`, and struct field reordering under `repr(Rust)`.
- The Rust Allocator API: `std::alloc::Allocator`, implementing slab allocators, fixed-size block allocators, and thread-local bump/arena allocators.
- Zero-copy deserialization: safe transmutation invariants, byte-slice casting using `zerocopy` and `bytemuck`.
- SIMD vectorization in Rust: portable SIMD (`std::simd`) and architecture-specific vendor intrinsics (`core::arch::x86_64`, `core::arch::aarch64`).

#### Module 4: Lock-Free Data Structures & Weak Memory Models
- The C++20 / Rust memory model: happens-before relationships, synchronized-with edges, and sequential consistency (`SeqCst`).
- Weak ordering: Acquire-Release semantics, Relaxed operations, and consume ordering subtleties.
- Hardware effects: store buffers, invalidation queues, cache line bouncing, and memory fences.
- Building lock-free primitives: Treiber stack, Michael-Scott queue, and tackling the ABA problem using tagged pointers and epoch-based memory reclamation (`crossbeam-epoch`).
- Concurrency testing: model checking multi-threaded interleavings via `loom`.

#### Module 5: Foreign Function Interface (FFI) & Cross-Language Hardening
- Safe FFI encapsulation: bridging Rust with C/C++ libraries without UB.
- Ownership and lifetime translation across language boundaries: raw pointers, opaque handles, and callback function pointers.
- Unwinding and panic safety across FFI: `extern "C-unwind"`, catch_unwind boundaries, and preventing undefined aborts.
- Automatic binding generation with `bindgen` and C-header synthesis with `cbindgen`.

---

### Course 2: Asynchronous Runtimes, Kernels & Formal Rust Verification

This course guides students through building bare-metal `no_std` kernels, low-level async reactors, and applying formal automated verification tools.

#### Module 1: The Asynchronous Execution Model from Scratch
- The `Future` trait: cooperative polling mechanics (`Poll<T>`, `Context`, `Waker`).
- State machine transformation: how the Rust compiler lowers `async/await` blocks into generator structs with internal discriminant states.
- The Pinning contract: `Pin<P<T>>`, structural pinning, preventing memory movements for self-referential generator structs, and sound `Drop` implementations.

#### Module 2: Designing an Async Runtime & Reactor
- Building the event loop reactor: interfacing with OS notification primitives (`epoll` on Linux, `kqueue` on macOS/BSD, and modern Linux `io_uring`).
- Waker implementation: constructing thread-safe custom vtables via `RawWaker` and `RawWakerVTable`.
- Multi-threaded work-stealing executors: Chase-Lev lock-free work-stealing deques, task scheduling heuristics, and cooperative yield points.

#### Module 3: Bare-Metal `no_std` Systems Programming
- Freestanding Rust development: `#![no_std]` and `#![no_main]`; custom panic handlers and stack unwinding stubs.
- Bootloader interfacing, ELF loading, and linker scripts.
- Memory management without OS support: paging tables (4-level / 5-level paging in x86-64), recursive page tables, physical frame allocators, and kernel heap initialization.
- Hardware exception handling: Interrupt Descriptor Table (IDT), Global Descriptor Table (GDT), and handling page faults safely.

#### Module 4: Hardware Driver Architecture & Type-State Patterns
- Memory-Mapped I/O (MMIO) and Port I/O: volatile memory access (`core::ptr::read_volatile`, `write_volatile`).
- The type-state pattern: encoding hardware peripheral states into the Rust type system (e.g. `Pin<Input>`, `Pin<Output>`, `Uart<Uninitialized>`, `Uart<Configured>`) to make illegal hardware configurations unrepresentable at compile time.
- Writing asynchronous drivers: VirtIO network and block device drivers over memory-mapped rings.

#### Module 5: Deductive Verification & Model Checking for Rust
- SAT/SMT-based bounded model checking with the Kani Rust Model Checker.
- Specifying formal function contracts, pre-conditions, post-conditions, and loop invariants using harness assertions.
- Deductive functional verification with Creusot and Why3: translating Rust programs into pure logic specifications.
- Formally proving absence of panics, absence of arithmetic overflow, and functional equivalence against reference mathematical specifications.

---

## 📑 Seminal Papers & Advanced Textbooks

- **Jung, R., Jourdan, J.-H., Krebbers, R., & Dreyer, D. (2017).** *RustBelt: Securing the Foundations of the Rust Programming Language*. Proceedings of the ACM on Programming Languages (POPL 2018), 2(Article 66), 1–34 (ACM SIGPLAN Distinguished Paper Award).
- **Jung, R., Dang, H.-H., Kang, J., & Dreyer, D. (2020).** *Stacked Borrows: An Operational Model for Rust's Pointer Tracking*. Proceedings of the ACM on Programming Languages (POPL 2020), 4(Article 41), 1–32.
- **Levy, A., Andersen, M. P., Campbell, B., Culler, D., Dutta, P., Ghena, B., Kempke, P., & Pannuto, P. (2017).** *Multiprogramming a 64kB Computer Safely and Efficiently*. Proceedings of the 26th ACM Symposium on Operating Systems Principles (SOSP '17), 42–57.
- **Denis, X., Jourdan, J.-H., & Marché, C. (2022).** *Creusot: a Foundry for the Deductive Verification of Rust Programs*. Formal Methods and Software Engineering (ICFEM 2022), LNCS 13607, 90–106.
- **Gjengset, J. (2021).** *Rust for Rustaceans: Idiomatic Programming for Experienced Developers*. No Starch Press.

---

## 🛠️ Progressive Labs

### Lab 1: Sound Lock-Free Queue Verified by Miri and Loom
- **Objective:** Implement the Michael-Scott lock-free concurrent queue in Rust using atomic pointers (`AtomicPtr`), `UnsafeCell`, and epoch-based memory reclamation.
- **Deliverables:**
  - Rust crate providing an unbounded multi-producer multi-consumer (MPMC) lock-free FIFO queue.
  - Comprehensive stress test suite and Miri verification harness.
- **Acceptance Criteria:**
  - The implementation must execute under `cargo miri test` with zero undefined behavior diagnostics, zero memory leaks, and complete adherence to Stacked Borrows rules.
  - The queue must be verified under `loom` across all permitted thread interleavings up to 4 concurrent threads without deadlocks or atomicity violations.

### Lab 2: Mini-Tokio Asynchronous Runtime with io_uring
- **Objective:** Construct an asynchronous runtime from first principles supporting asynchronous TCP sockets powered by Linux `io_uring`.
- **Deliverables:**
  - Custom async reactor submitting submission queue entries (SQEs) and polling completion queue entries (CQEs) without syscall overhead.
  - Multi-threaded task scheduler implementing work-stealing across worker threads with cooperative yield semantics.
- **Acceptance Criteria:**
  - The runtime must successfully execute an asynchronous HTTP/TCP echo server benchmarking at least $150,000 \text{ req/sec}$ on localhost.
  - Average round-trip task scheduling latency must remain $< 25 \, \mu\text{s}$, achieving within 20% throughput of production Tokio on identical workloads.

### Lab 3: Deductive Verification with Kani Rust Model Checker
- **Objective:** Implement a complex unsafe intrusive doubly-linked list or circular ring-buffer and formally prove its memory safety and functional correctness using Kani.
- **Deliverables:**
  - Rust source containing the data structure and formal Kani verification harnesses with symbolic inputs.
  - Mathematical contract specifications (`kani::assume`, `kani::assert`) proving invariant preservation across all mutating operations.
- **Acceptance Criteria:**
  - Automated proof check runs `cargo kani` and succeeds with 0 counterexamples across all symbolic memory interactions up to a bound of $k = 32$.
  - Formal claims verify total absence of null-pointer dereferences, pointer misalignment, integer overflow, and out-of-bounds array access.

---

## 🏆 Capstone Build Deliverable

### Bootable Multi-Core `no_std` Microkernel with Formally Verified Drivers

A freestanding, crash-resilient, multi-core operating system kernel written in 100% `#![no_std]` Rust for x86-64 or RISC-V targets running inside QEMU.

```text
+-----------------------------------------------------------------------------------+
|                        VERIFIED RUST MICROKERNEL (no_std)                         |
|                                                                                   |
|  [ User Ring 3 Process ]        [ User Ring 3 Process ]                           |
|            |                               |                                      |
|  ----------+-------------------------------+------------------------------------  |
|            v                               v                                      |
|  [ Syscall Fast-Path ]          [ Preemptive Work-Stealing Scheduler ]            |
|            |                               |                                      |
|  [ Multi-Level Paging ]         [ Slab Heap Allocator ]                           |
|            |                               |                                      |
|  [ Kani-Verified VirtIO Block Driver ]  [ Async Serial UART / APIC Timer ]       |
+-----------------------------------------------------------------------------------+
```

#### System Architecture & Specifications
1. **Kernel Core:** Multi-core SMP initialization, 4-level virtual memory paging manager with identity mapping and kernel/user space isolation, frame allocator, and slab allocator.
2. **Process Subsystem:** Preemptive priority-based context switcher using APIC timer interrupts, saving and restoring thread execution contexts with minimal latency.
3. **Verified Drivers:** VirtIO block storage driver and asynchronous UART driver whose state machines and ring-buffer interactions are formally verified with Kani.

#### Verification & Acceptance Criteria
- **Linting & Hygiene:** Zero compiler warnings under `cargo clippy --pedantic -- -D warnings`, verified via CI pipeline.
- **Stress Testing & Concurrency:** Must execute continuous stress testing inside QEMU running 10,000 process context switches, preemptive interrupts, and concurrent filesystem reads with zero panic, zero memory leaks, and zero kernel deadlock.
- **Formal Verification:** All internal unsafe pointer operations within the kernel's scheduler queues and memory frame allocators must pass formal proof checks via Kani.
- **Test Commands:**
  ```bash
  # Check strict clippy compliance
  cargo clippy --all-targets -- -D warnings
  # Run Miri on host-compatible components
  cargo miri test --lib
  # Run Kani model checker on verified drivers
  cargo kani --harness verify_virtio_ring
  # Boot and execute automated kernel test suite in QEMU
  cargo test --target x86_64-unknown-none
  qemu-system-x86_64 -kernel target/x86_64-unknown-none/debug/kernel -serial stdio -display none
  ```

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> Assessment criteria go here.

## ➡️ Next Steps & Degree Pathway
- **Curriculum Hub:** [[Specialization Branches|Specializations Hub]]
- **Degree Assignment:**
  - If chosen as **Primary Specialization (Track A)**: Course 1 binds to [[Specialization Branches|Block 26 - Specialization A1]] and Course 2 binds to [[Specialization Branches|Block 28 - Specialization A2]].
  - If chosen as **Secondary Specialization (Track B)**: Course 1 binds to [[Specialization Branches|Block 29 - Specialization B1]] and Course 2 binds to [[Specialization Branches|Block 31 - Specialization B2]].
- **Curriculum Roadmap:** [[00 - Start Here|Start Here]] / [[00 - Start Here#The Path|The Path]]

- **Sequential Flow:** [[T02 - Advanced Systems and Performance|← Advanced Systems and Performance]] | [[00 - Start Here|Start Here]] | [[T13 - Systems Formal Verification|Systems Formal Verification →]]
