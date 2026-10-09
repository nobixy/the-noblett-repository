---
title: "Projects & Builds Hub"
type: hub
tags:
  - hub
  - navigation
  - projects
---

# Projects & Builds Hub
*Per Rule 2: A block is done when the Done when line is true. Not before.*

[[00 - Dashboard|Dashboard]] / [[Checklist|Checklist]]

---

> [!TIP]
> Use [[Project Build Spec Template|Project Build Spec Template]] to specify architectures, representation invariants, and test plans for every major build. All software artifacts must be version-controlled under Git and tested with rigorous developer toolchains.

---

## 🏗️ Core Curriculum Course Builds

The core degree requirements mandate completing tangible, production-grade software and hardware artifacts for each course block. Builds are developed using standard system toolchains including `gcc`, `clang`, `rust`, `cargo`, `gdb`, `valgrind`, `qemu`, `verilog`, `renode`, and `pytest`.

- [ ] **Phase 0 On-Ramp:** [[Programming On-Ramp|Phase 0 Programming]]: Valgrind-clean 300-line C program, hash table (separate chaining), and binary search tree from scratch. Verified with `gcc`, `valgrind`, and `gdb`.
- [ ] **Block 01:** [[CS61A|01 - CS61A]]: Scheme Interpreter with tail-call optimization, user-defined macros, and lexical scoping implemented in Python and verified via `pytest`.
- [ ] **Block 02:** [[Calculus I|02 - Calculus I]]: Numerical differentiation engine, adaptive Simpson's rule and Riemann sum integrator, and Taylor series polynomial approximator implemented in Python and C, verified with `pytest`.
- [ ] **Block 03:** [[Physics I|03 - Physics I]]: Classical kinematics, 2D/3D rigid-body collision simulator, and symplectic numerical integrator (Verlet/leapfrog) in C++ verified with unit tests.
- [ ] **Block 04:** [[Nand2Tetris|04 - Nand2Tetris]]: Complete hardware-to-software computing stack: 16-bit Hack CPU and ALU in the Nand2Tetris HDL, assembler, stack-based VM translator, Jack compiler, and minimal OS running an interactive graphics demo.
- [ ] **Block 05:** [[SICP|05 - SICP]]: Metacircular Evaluator, Amb non-deterministic evaluator, and Lazy Stream Evaluator in Scheme/Racket.
- [ ] **Block 06:** [[C Fluency|06 - C Fluency]]: Reusable systems data structures in ANSI C: dynamic array vector, arena string allocator, hash map, and a POSIX-compliant `ls -laR` utility. Verified leak-free with `valgrind` and `clang` AddressSanitizer.
- [ ] **Block 07:** [[Multivariable Calculus|07 - Multivariable Calculus]]: Vector calculus numerical gradient descent, Hessian matrix computation, and 3D contour surface visualizer in Python with `numpy` and `matplotlib`.
- [ ] **Block 08:** [[Physics II|08 - Physics II]]: Finite-difference time-domain (FDTD) electromagnetic field simulation and Maxwell's equations solver in Python and C++.
- [ ] **Block 09:** [[Computer Systems|09 - Computer Systems]]: Complete CMU CS:APP laboratory suite (Data Lab, Defusing Binary Bomb with `gdb`, Attack Lab ROP exploits, Cache Lab simulator, UNIX Shell with job control, `malloc` segregated-free-list dynamic allocator, and concurrent multi-threaded HTTP proxy).
- [ ] **Block 10:** [[Math for CS|10 - Math for CS]]: Automated DPLL Boolean SAT solver, graph coloring engine, and number-theoretic algorithms (RSA, Miller-Rabin) in Python, with formal inductive proofs formalized in Lean.
- [ ] **Block 11:** [[Linear Algebra|11 - Linear Algebra]]: High-performance matrix numerical library from scratch: LU decomposition with partial pivoting, Gram-Schmidt orthogonalization, QR decomposition, and power method for eigenspaces. Verified with `pytest`.
- [ ] **Block 12:** [[Interpreters|12 - Interpreters]]: Tree-walking interpreter for the Monkey programming language in Go, plus `clox` bytecode virtual machine with mark-sweep garbage collection in ANSI C.
- [ ] **Block 13:** [[Algorithms I|13 - Algorithms I]]: Self-balancing AVL and Red-Black trees, binary heaps, and Dijkstra shortest-path finder implemented from scratch in C and Python, verified with `pytest` unit tests and `valgrind` memory checking.
- [ ] **Block 14:** [[Computer Architecture|14 - Computer Architecture]]: 5-stage pipelined RV32I RISC-V processor in Verilog with hazard detection, forwarding unit, dynamic 2-bit branch predictor, and unified direct-mapped cache. Tested in Verilator and FPGA emulation.
- [ ] **Block 15:** [[Probability|15 - Probability]]: Monte Carlo simulation suite, discrete/continuous Markov chain steady-state solver, and random walk martingale path estimator in Python with `numpy` and `scipy`.
- [ ] **Block 16:** [[Operating Systems|16 - Operating Systems]]: Complete MIT 6.1810 xv6 RISC-V lab curriculum (system calls, copy-on-write page faults, user-level thread scheduler, lock-free memory buffer, crash-consistent logging file system) and minimal freestanding kernel booting in `qemu`.
- [ ] **Block 17:** [[Software Construction|17 - Software Construction]]: Production compiler intermediate representation and optimizer with formal representation invariants, abstract data types (ADTs), and automated WCAG 2.1 AA developer inspection interface.
- [ ] **Block 18:** [[Real Analysis|18 - Real Analysis]]: Arbitrary-precision epsilon-delta convergence verifier, metric space topology explorer, and continuous nowhere-differentiable function visualizer in Python and Rust, with theorems mechanized in Lean.
- [ ] **Block 19:** [[Networking|19 - Networking]]: Stanford CS144 TCP/IP stack from scratch in modern C++: TCP receiver, TCP sender, connection state machine, sliding-window flow control, and IP router. Tested against real network packet captures with `clang` and `gdb`.
- [ ] **Block 20:** [[Algorithms II|20 - Algorithms II]]: Edmonds-Karp and Dinic's blocking network flow algorithms, Primal-Dual Simplex solver, and spectral graph partitioner in C++ and Python, verified with `pytest` on DIMACS benchmarks.
- [ ] **Block 21:** [[Databases|21 - Databases]]: CMU 15-445 BusTub relational DBMS engine in C++: buffer pool manager, extendible hash index, B+ tree index, Volcano execution engine, and multi-version concurrency control (MVCC).
- [ ] **Block 22:** [[Statistics|22 - Statistics]]: High-dimensional MLE numerical optimizer, Likelihood Ratio and Wald hypothesis testing suite, and Hamiltonian Monte Carlo (HMC) / Metropolis-Hastings MCMC sampler in Python with `numpy`, `scipy`, and `pytest`.
- [ ] **Block 23:** [[Distributed Systems|23 - Distributed Systems]]: MIT 6.5840 distributed systems labs in Go: MapReduce execution framework, Raft replicated consensus protocol (leader election, log replication, snapshotting), and fault-tolerant sharded key-value service.
- [ ] **Block 24:** [[Theory of Computation|24 - Theory of Computation]]: Deterministic and non-deterministic Turing machine simulators, generalized DFA minimization engine, and Boolean 3-SAT verifier/reduction engine in Python, with computability lemmas formalized in Lean.
- [ ] **Block 25:** [[Convex Optimization|25 - Convex Optimization]]: Portfolio optimization and trajectory planner formulated in CVXPY / SciPy with manual derivation and implementation of KKT optimality conditions.
- [ ] **Block 26:** [[05 - Specialization Branches|26 - Specialization A1]]: Primary Specialization Foundational Systems Build in Rust, C++, or Python: core algorithmic substrate, runtime environment integration, and concurrency race detection verified with `pytest` or `cargo test`.
- [ ] **Block 27:** [[Intensive Cryptopals|27 - Intensive Cryptopals or TLA+]]: Complete solution of all 8 Cryptopals crypto challenges (AES-CBC padding oracles, ECB byte-at-a-time, RSA signature forgery, Diffie-Hellman MITM) OR formal TLA+ specification and model-checking bug reproduction of Raft/Paxos.
- [ ] **Block 28:** [[05 - Specialization Branches|28 - Specialization A2]]: Primary Specialization Advanced Systems Engine in Rust, C++, or Python: standalone high-performance system artifact, quantitative throughput/latency benchmarking, and formal invariant test harness with `valgrind` or sanitizers.
- [ ] **Block 29:** [[05 - Specialization Branches|29 - Specialization B1]]: Secondary Specialization Applied Domain Pipeline in Rust, C++, or Python: domain component implementation, automated bit-exact verification with `pytest` or `cargo test`, and system resource profiling with `valgrind`.
- [ ] **Block 30:** [[Magnum Opus Capstone|30 - Capstone]]: Master's Engineering Capstone: 10,000+ line production systems codebase, seminal research paper replication, or physical ASIC tapeout meeting formal usability and empirical performance metrics.
- [ ] **Block 31:** [[05 - Specialization Branches|31 - Specialization B2]]: Secondary Specialization Scaled Infrastructure Engine in Rust, C++, or Python: advanced domain module, automated regression harness in `pytest` or `cargo test`, and quantitative profiling integrated into Year 5 Capstone.
- [ ] **Block 32:** [[Information Theory|32 - Information Theory]]: Shannon-Fano, Huffman, and Lempel-Ziv-Welch (LZW) universal compression and decompression utility with channel capacity simulation.

---

## 🌉 Optional Bridge Course Builds (computer-engineering path)

Not required for 6-3 and outside the hour budget. Build these only if you take the bridge blocks. Each line below follows its block's own Build section.

- [ ] **Block 04a:** [[Differential Equations Bridge|04a - Differential Equations Bridge]]: Numerical ODE integration engine (RK4 and adaptive RKF45) with a phase-portrait and chaos visualizer; the Van der Pol limit cycle demonstrated.
- [ ] **Block 08a:** [[Circuits and Electronics Bridge|08a - Circuits and Electronics Bridge]]: Dual-stage active audio pre-amplifier and 4th-order Sallen-Key Butterworth band-pass filter, simulated in SPICE, then built on a breadboard.
- [ ] **Block 15a:** [[Signals and Systems Bridge|15a - Signals and Systems Bridge]]: Zero-dependency DSP engine in C or Rust: radix-2 FFT/IFFT, FFT convolution, and a WAV-file audio filter.

---

## 🚀 Specialization Track Capstone Builds

The 11 advanced graduate tracks culminate in substantial capstone engineering projects documented in the [[05 - Specialization Branches|Specializations Hub]]:

- [ ] **Track 1 (AI & Machine Learning):** [[Deep AI and Machine Learning|Track 1 Capstone]]: Autograd Engine & Transformer Pipeline (`needle` / `micrograd`), CUDA FlashAttention kernels, and Ring AllReduce distributed training benchmarked with `pytest`.
- [ ] **Track 2 (Systems & Performance):** [[Advanced Systems and Performance|Track 2 Capstone]]: High-Throughput Storage Engine (`nebula-lsm`) in C++20 with lock-free skip list MemTable, Linux `io_uring` direct I/O, and leveled SSTable compaction compiled with `clang` and debugged with `gdb`.
- [ ] **Track 3 (Security & Cryptography):** [[Advanced Security and Cryptography|Track 3 Capstone]]: Post-Quantum Encrypted Messaging Engine (`ironclad`) in Rust implementing Signal Double Ratchet with NIST FIPS 203 ML-KEM-768, built with `cargo` and tested for constant-time properties.
- [ ] **Track 4 (Graphics & Vision):** [[Advanced Graphics and Vision|Track 4 Capstone]]: Physically Based Spectral Path Tracer (`lumina-pt`) in C++ with Multiple Importance Sampling, BVH spatial acceleration, and Intel OIDN neural denoising.
- [ ] **Track 5 (Programming Languages & Compilers):** [[Advanced Programming Languages and Compilers|Track 5 Capstone]]: Optimizing SSA Compiler (`velox-cc`) with dominance frontiers, Chaitin-Briggs graph coloring register allocation, RV32IM backend tested in `qemu`, and mechanized Lean 4 / Coq type soundness proofs.
- [ ] **Track 6 (Computer Engineering):** [[Advanced Computer Engineering|Track 6 Capstone]]: Hardened 32-bit RISC-V SoC (`apex-soc`) with Wishbone interconnect, UART, and SPI peripherals written in Verilog, simulated with Verilator and Cocotb, and hardened to GDSII layout via OpenLane SkyWater 130nm PDK.
- [ ] **Track 7 (TinyML & Edge AI):** [[TinyML and Edge AI|Track 7 Capstone]]: Edge Wake-Word Detection System (`edge-vision`) executing INT8 quantized inference on ARM Cortex-M microcontrollers via CMSIS-NN SIMD vectorization, tested in `qemu` and `renode`.
- [ ] **Track 8 (Rust Systems & Formal Verification):** [[Rust for Systems Engineering|Track 8 Capstone]]: Formally Verified Preemptive SMP Microkernel (`aegis-os`) in Rust with 4-level paging and verified VirtIO drivers built with `cargo` and verified using Kani model checking.
- [ ] **Track 9 (Hardware-in-the-Loop & CPS):** [[Hardware-in-the-Loop Virtualization and Digital Twins|Track 9 Capstone]]: Real-Time Hardware-in-the-Loop Testbed (`aero-twin`) simulating 6-DOF flight dynamics and CAN-FD communication orchestrated in `renode` and QEMU.
- [ ] **Track 10 (Quantum Information & Computing):** [[Quantum Information and Computing|Track 10 Capstone]]: Variational Quantum Eigensolver (VQE) & Circuit Compiler (`q-compile`) with A* SWAP routing on heavy-hex coupling graphs and ZNE error mitigation tested via `pytest`.
- [ ] **Track 11 (Autonomous Robotics & CPS):** [[Autonomous Robotics|Track 11 Capstone]]: Autonomous Indoor Navigation Stack (`drone-nav`) in ROS 2 with 3D LiDAR odometry, Informed RRT*, and real-time Model Predictive Control (MPC).

---

## 🧭 Navigation
- **Curriculum Overview:** [[00 - Dashboard|Dashboard]]
- **Milestone Checklist:** [[Checklist|Checklist]]
- **Specializations Catalog:** [[05 - Specialization Branches|Specializations Hub]]
