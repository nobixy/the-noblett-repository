---
title: "Specializations Hub"
type: hub
tags:
  - specialization
  - hub
  - curriculum
  - navigation
---

# Specializations Hub

> [!INFO] Specialization Architecture: Two Deep Beats Six Shallow
> In Years 4 & 5 (Part 3 of the curriculum), students select **two specialization tracks** from the 11 tracks below.
> Each specialization track consists of **two intensive graduate-level courses**, **three progressive hands-on laboratory sequences**, and **one comprehensive engineering capstone build deliverable**.
> Specializations allow students to transition from generalist computer engineering foundations to world-class mastery in specific classical or cutting-edge modern engineering disciplines.

> [!IMPORTANT] My Picks (decide at the end of Year 3, not before)
> - **Track A (Blocks 26, 28):** _undecided_
> - **Track B (Blocks 29, 31):** _undecided_
> - **Why these two:** _one paragraph, written when deciding_
>
> The other nine tracks are a catalog, not a to-do list. Reading them now is planning, not studying.

---

## 🧭 The 11 Specialization Tracks

The Noblett Repository divides its 11 specialization tracks into **Classical Core Tracks** (Tracks 1–6) and **Cutting-Edge Modern Paradigm Tracks** (Tracks 7–11).

```text
========================================================================================================
                                 THE COMPLETE 11-TRACK SPECIALIZATION CATALOG
========================================================================================================
CLASSICAL CORE SPECIALIZATIONS:                        CUTTING-EDGE MODERN PARADIGMS:
- Track 1: AI & Machine Learning                      - Track 7: TinyML and Edge AI
- Track 2: Systems & Performance                      - Track 8: Rust for Systems Engineering & Verification
- Track 3: Security & Cryptography                    - Track 9: HIL Virtualization, Digital Twins and CPS
- Track 4: Graphics & Vision                          - Track 10: Quantum Information & Computing
- Track 5: Programming Languages & Compilers          - Track 11: Autonomous Robotics & CPS
- Track 6: Computer Engineering (Deep Hardware)
========================================================================================================
```

---

### Classical Core Tracks (Tracks 1–6)

| Track | Focus & Core Courses | Key Build Deliverable |
| :--- | :--- | :--- |
| **[[Track 1 - AI and Machine Learning]]** | Statistical learning theory (Stanford CS229 / Bishop), deep learning systems (CMU 10-414 / CS231n), autograd engines, and attention mechanisms. | 125M-parameter autoregressive transformer trained from scratch with quantized C++ serving engine. |
| **[[Track 2 - Systems and Performance]]** | Performance engineering (MIT 6.172 / Leiserson), multiprocessor programming (Herlihy & Shavit), cache optimization, and database internals (CMU 15-721). | Lock-free, high-throughput LSM-tree storage engine with `io_uring` asynchronous I/O and ARIES recovery. |
| **[[Track 3 - Security and Cryptography]]** | Applied cryptography (Boneh & Shoup), systems security (MIT 6.1600/6.858), binary exploitation (ROP/Heap), and constant-time engineering. | End-to-end audited encrypted messaging protocol with Double Ratchet and post-quantum hybrid KEM (ML-KEM/Kyber). |
| **[[Track 4 - Graphics and Vision]]** | Foundations of graphics (GAMES101), physically based rendering (PBRT 4e), Monte Carlo light transport, and explicit GPU architectures (Vulkan). | Spectral volumetric Monte Carlo path tracer with Multiple Importance Sampling and AI neural denoising. |
| **[[Track 5 - Programming Languages and Compilers]]** | Type systems & operational semantics (Pierce TAPL), optimizing compilers (Cornell CS 6120), SSA construction, and register allocation. | End-to-end optimizing compiler targeting RISC-V with SSA optimizations and Coq/Lean mechanized type soundness proof. |
| **[[Track 6 - Computer Engineering]]** | Out-of-order superscalar architectures (Hennessy & Patterson), CMOS VLSI design (Weste & Harris), and silicon tapeout flows (OpenLane / SkyWater). | Tapeout-ready 32-bit RISC-V SoC with AXI interconnect, peripherals, and clean silicon DRC/LVS verification. |

---

### Cutting-Edge Modern Paradigm Tracks (Tracks 7–11)

| Track | Focus & Core Courses | Key Build Deliverable |
| :--- | :--- | :--- |
| **[[Track 7 - TinyML and Edge AI]]** | Efficient deep learning (MIT 6.5940), mathematical quantization (INT8/FP4), CMSIS-NN SIMD vectorization, and zero-allocation memory arenas. | Bare-metal real-time keyword spotting and vision anomaly detection on ARM Cortex-M / RISC-V microcontroller (< 50 mW). |
| **[[Track 8 - Rust for Systems Engineering and Formal Verification]]** | Substructural affine types, deep `unsafe` pointer provenance (Stacked Borrows), lock-free data structures, `no_std` kernels, and Kani model checking. | Bootable multi-core `no_std` microkernel with preemptive scheduler and formally verified VirtIO drivers. |
| **[[Track 9 - Hardware-in-the-Loop Virtualization, Digital Twins and CPS]]** | Hard real-time Linux (PREEMPT_RT), 6-DOF physical plant simulation, CAN-FD / TSN bus protocols, and SpaceEx reachability analysis. | Real-time Hardware-in-the-Loop (HIL) testbed for autonomous drone flight controller with automated fault injection. |
| **[[Track 10 - Quantum Information and Computing]]** | Linear algebraic quantum mechanics, universal circuit synthesis, Shor/Grover algorithms, topological surface codes, and VQE for NISQ systems. | End-to-end quantum compiler, SWAP topology router, and Variational Quantum Eigensolver (VQE) converging to chemical accuracy. |
| **[[Track 11 - Autonomous Robotics and Cyber-Physical Systems]]** | Probabilistic state estimation (EKF/UKF on $SE(3)$), graph-based SLAM (GTSAM), non-linear Model Predictive Control (MPC), and ROS 2 middleware. | Autonomous indoor navigation, frontier exploration, and dynamic obstacle avoidance robot stack in ROS 2 / Gazebo. |
| **[[Track 12 - Computational Biology and Bioinformatics]]** | Algorithms for genome assembly (De Bruijn graphs), HMMs for sequence alignment, and biological data science (CMU 02-251, MIT 6.8700). | De novo genome assembler and PyTorch-based single-cell RNA-seq transcription factor binding site predictor. |
| **[[Track 13 - Systems Formal Verification]]** | State-machine model checking (TLA+/TLC), relational modeling (Alloy), and rigorous proof of safety/liveness in distributed consensus. | Formal TLA+ specification and exhaustive TLC verification of a custom Byzantine Fault Tolerant distributed protocol. |
| **[[Track 14 - Advanced Pure Mathematics]]** | Abstract Algebra (Dummit & Foote), Point-Set & Algebraic Topology (Munkres), and Differential Geometry / Manifolds (Tu). | LaTeX portfolio containing mathematician-grade proofs for core theorems bridging Galois Theory, Topology, and Lie Algebras. |

---

## 🎯 Recommended High-Impact Track Pairings

To maximize career specialization depth and cross-disciplinary synergy, students are encouraged to pair tracks according to their post-graduation aspirations:

1. **The Modern Ultra-Systems & Cloud Architect:**
  - **Combination:** [[Track 2 - Systems and Performance]] + [[Track 8 - Rust for Systems Engineering and Formal Verification]]
  - **Synergy:** Combines raw Linux kernel and database internals with memory-safe, formally verified concurrent systems in Rust.
2. **The Autonomous Cyber-Physical & Robotics Pioneer:**
  - **Combination:** [[Track 7 - TinyML and Edge AI]] + [[Track 11 - Autonomous Robotics and Cyber-Physical Systems]]
  - **Synergy:** Unites on-device micro-watt intelligence with real-time probabilistic SLAM and Model Predictive Control.
3. **The Embedded Hardware & Safety-Critical Engineer:**
  - **Combination:** [[Track 6 - Computer Engineering]] + [[Track 9 - Hardware-in-the-Loop Virtualization, Digital Twins and CPS]]
  - **Synergy:** Bridges custom ASIC/FPGA digital design with deterministic HIL virtualization and ISO 26262 functional safety testing.
4. **The High-Assurance Cryptography & Formal Logic Specialist:**
  - **Combination:** [[Track 3 - Security and Cryptography]] + [[Track 10 - Quantum Information and Computing]] (or [[Track 5 - Programming Languages and Compilers]])
  - **Synergy:** Integrates post-quantum lattice cryptography with deep quantum computational algorithms and mechanized formal proofs.
5. **The Next-Generation AI & Accelerator Architect:**
  - **Combination:** [[Track 1 - AI and Machine Learning]] + [[Track 7 - TinyML and Edge AI]] (or [[Track 6 - Computer Engineering]])
  - **Synergy:** Connects high-level generative deep architectures with bare-metal silicon accelerators and quantization mathematics.

---

## 📐 Extra Math for Specializations

Specialization tracks demand mathematical maturity far beyond standard undergraduate calculus and linear algebra. The following authoritative mathematical reference texts support the respective tracks:

- **Measure-Theoretic Probability & Stochastic Processes (Tracks 1, 7, 10, 11):**
  - Rick Durrett, *Probability: Theory and Examples, 5th Edition*, Cambridge University Press.
  - David Williams, *Probability with Martingales*, Cambridge University Press.
- **Convex Analysis & Non-Smooth Optimization (Tracks 1, 2, 7, 11):**
  - Stephen Boyd & Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press.
  - R. Tyrrell Rockafellar, *Convex Analysis*, Princeton University Press.
- **Abstract Algebra & Number Theory (Tracks 3, 5, 10):**
  - David S. Dummit & Richard M. Foote, *Abstract Algebra, 3rd Edition*, John Wiley & Sons.
  - Kenneth Ireland & Michael Rosen, *A Classical Introduction to Modern Number Theory, 2nd Edition*, Springer GTM.
- **Category Theory, Type Theory & Logic (Tracks 5, 8, 10):**
  - Saunders Mac Lane, *Categories for the Working Mathematician, 2nd Edition*, Springer GTM.
  - Steve Awodey, *Category Theory, 2nd Edition*, Oxford University Press.
  - Benjamin C. Pierce, *Types and Programming Languages*, MIT Press.
- **Differential Geometry & Lie Groups for Robotics (Tracks 4, 11):**
  - Timothy D. Barfoot, *State Estimation for Robotics: A Matrix Lie Group Approach*, Cambridge University Press.
  - John M. Lee, *Introduction to Smooth Manifolds, 2nd Edition*, Springer GTM.
- **Spectral Graph Theory & Randomized Algorithms (Tracks 1, 2, 3, 5):**
  - Daniel A. Spielman, *Spectral and Algebraic Graph Theory*, Yale University Lecture Monograph.
  - Michael Mitzenmacher & Eli Upfal, *Probability and Computing: Randomization and Probabilistic Techniques in Algorithms and Data Analysis*, Cambridge University Press.
