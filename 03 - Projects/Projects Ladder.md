---
title: "Projects Ladder"
type: hub
tags:
  - hub
  - projects
---

# Projects Ladder
*Every build in the program, in order, each with a done-when line ([[DR-008 - Project-First Start and Projects Ladder|DR-008]]). I learn best by building, so this is the main way through the program; The Path in [[00 - Start Here|Start Here]] is the checklist and [[Projects Hub]] has the long specs.*

**Rules**
1. Every block has at least one build with a done-when line. Reading supports the build; it doesn't come first.
2. One mini-build a week (≤2 h, usually Saturday), logged in [[log]] ([[how-i-study#2b. Weekly Mini-Build|how-i-study §2b]]).
3. Reading ramps up slowly: [[how-i-study#2a. Reading Ramp|Reading Ramp]].
4. Hours: all of this fits inside the existing block hours (6,005 h core). Builds replace reading or write-up time; nothing was added.

---

## 🪜 Starter Sprint (Weeks 1–12)
*One fun build a week while the study habit forms. Week 1 is broken into days on [[00 - Start Here#🚀 Week 1 — Do This Today|Start Here]]. Alongside it, every day: the 🎮 Daily Code Streak (NeetCode *Python for Beginners*, then easy NeetCode 150 problems; NeetCode Pro ends Feb 6, 2027, then the free neetcode.io roadmap, Exercism or Codewars).*

| Week | Build | Counts toward | Done when | Cost |
| :-- | :--- | :--- | :--- | :--- |
| 1 | Scratch quiz game: 10 questions about anything you like, with a score | [[B0 - The Deep Learner's Toolkit\|B0]] | someone else plays it start to finish | free (scratch.mit.edu, no install) |
| 2 | Blink a Raspberry Pi Pico in the Wokwi simulator, then make it flash SOS and time your reaction to a button | [[B0 - The Deep Learner's Toolkit\|B0]] | SOS blinks correctly and the reaction timer prints milliseconds | free (wokwi.com/pi-pico); a real Pico 2 is 💲 $5, optional |
| 3 | Desmos art: draw a picture using only lines, parabolas and restricted domains | [[BM - Bedrock Mathematics\|BM]] | the picture uses 15+ equations and you can say what each one does | free (desmos.com/calculator) |
| 4 | Scratch base converter + fraction visualizer | [[BM - Bedrock Mathematics\|BM]] | converts 0–255 between decimal, binary and hex both ways, and draws any a/b as a bar | free |
| 5 | nandgame: build NAND → half adder → full adder → multi-bit adder | [[BM - Bedrock Mathematics\|BM]] | the adder levels pass and you wrote a 1-page Feynman note: why binary adds like decimal | free (nandgame.com); Turing Complete is 💲 $19.99, optional |
| 6 | Twine branching story where every choice is a clean sentence | [[BW - Bedrock English and Grammar\|BW]] | 1,500 words, 3 endings, and a friend played it | free (twinery.org) |
| 7 | Python sentence machine: random sentences from the 4 core sentence patterns | [[BW - Bedrock English and Grammar\|BW]] | it prints 20 grammatical sentences and you can mark subject, verb and object in each | free |
| 8 | OverTheWire Bandit, levels 0–10, in your own terminal | [[P5 - Tooling\|P5]] | you reached level 10 and wrote one line per level on the command that cracked it | free (overthewire.org) |
| 9 | Python flashcard app with Leitner boxes for your first 20 study cards | [[P1 - Learning How to Learn\|P1]] | it schedules all 20 cards and you used it 7 days in a row | free |
| 10 | Python prime sieve + factor-tree printer | [[BM - Bedrock Mathematics\|BM]] | it factors every number up to 1,000 and a test checks each factorization multiplies back | free |
| 11 | Puzzle week: 5 Human Resource Machine levels, or 5 Project Euler problems, each with Pólya's four steps written out | [[P2 - Reading, Thinking, and Writing\|P2]] | 5 solved, 5 write-ups | Project Euler is free (projecteuler.net); Human Resource Machine is 💲 $14.99, optional |
| 12 | Pong or Breakout clone in p5.js or LÖVE | [[P4 - Programming On-Ramp\|P4]] | playable with a score, and someone beat your high score | free (p5js.org, love2d.org) |

---

## 🏗️ The Ladder (every block on The Path)
*Done-when lines come from The Path; the Phase −1/0 and Blocks 2, 3, 7 and 8 builds are new in DR-008.*

### Phase -1: Bedrock Foundations (The Ground Floor)

| # | Block | Build / done when |
| :-- | :--- | :--- |
| 1 | [[B0 - The Deep Learner's Toolkit\|B0]] | Scratch quiz game played by someone else; Pico SOS + reaction timer in Wokwi. |
| 2 | [[BM - Bedrock Mathematics\|BM]] | Desmos art, base converter, nandgame adders, prime sieve all work; Khan unit tests passed. |
| 3 | [[BW - Bedrock English and Grammar\|BW]] | Twine story played by a friend; sentence machine; 10 days of copywork. |

### Phase 0: Prerequisites (0–5 months)

| # | Block | Build / done when |
| :-- | :--- | :--- |
| 4 | [[P1 - Learning How to Learn\|P1]] | Flashcard app used 7 days; study system written in how-i-study; 20 cards. |
| 5 | [[P2 - Reading, Thinking, and Writing\|P2]] | Build write-up, 3-pass paper read, 5 Pólya puzzles, 14 days of 500 words. |
| 6 | [[P3 - Math Prerequisites\|P3]] | Truth-table and set toolkit agrees with your hand answers; cold test passed. |
| 7 | [[P4 - Programming On-Ramp\|P4]] | 300-line valgrind-clean C program; hash table & BST from scratch. |
| 8 | [[P5 - Tooling\|P5]] | [[log]] has 14 consecutive daily entries & headless Linux mastery. |

### Year 1: Learn to Program. Learn to Prove.

| # | Block | Build / done when |
| :-- | :--- | :--- |
| 9 | [[B01 - CS61A\|Block 1]] | Scheme interpreter project + one extension the course doesn't ask for (e.g. tail calls); past final ≥70%. |
| 10 | [[B02 - Calculus I\|Block 2]] | Calculus toy lab: the integrators match the exact answers to 10 of the 18.01 integrals within 1e-6, the error plot shows Simpson's 4th-order slope, and Newton's method finds √2 to 12 digits. |
| 11 | [[B03 - Physics I\|Block 3]] | 2D physics sandbox: total energy drifts under 1% over 10,000 steps, momentum is conserved in collisions to 1e-9, and your phyphox pendulum gives g within 2%. |
| 12 | [[B04 - Nand2Tetris\|Block 4]] | A Jack program you wrote runs on the CPU you built. |
| 13 | [[B04a - Differential Equations Bridge\|Block 4a]] | Construct adaptive RK4/RKF45 chaos simulator; 18.03 final passed. |
| 14 | [[B06 - C Fluency\|Block 6]] | Vector, arena string library, hash table and an `ls` clone in C, valgrind-clean, with `objdump` annotated. |
| 15 | [[B07 - Multivariable Calculus\|Block 7]] | 3D field explorer: gradient descent finds the minima of three 18.02 functions and matches your Lagrange-multiplier answers, and numerical flux equals the numerical divergence integral within 1% for two fields. |
| 16 | [[B08 - Physics II\|Block 8]] | E&M field simulator + electromagnet: the simulated point charge and dipole match Coulomb's law within 1%, a numerical Gauss's-law check passes, and the measured field rises in proportion to current. |
| 17 | [[B08a - Circuits and Electronics Bridge\|Block 8a]] | Design & test 4th-order Sallen-Key Butterworth filter in SPICE & breadboard. |
| 18 | [[B08b - Maker Lab 1 - Electronics Bench\|Block 8b]] | Soldered kit, sensor logger, MOSFET motor driver all work. |

### Year 2: The Systems Year

| # | Block | Build / done when |
| :-- | :--- | :--- |
| 19 | [[B09 - Computer Systems\|Block 9]] | All 7 labs pass; malloc lab score ≥90. |
| 20 | [[B09a - Maker Lab 2 - Embedded C\|Block 9a]] | Own IMU driver; propeller see-saw holds ±3° with PID. |
| 21 | [[B10 - Math for CS\|Block 10]] | RSA, Miller–Rabin and modular exponentiation in Python with tests; 6.042 final passed. |
| 22 | [[B11 - Linear Algebra\|Block 11]] | LU, Gram–Schmidt, Householder QR and the power method in NumPy, benchmarked against SciPy; 18.06 final passed. |
| 23 | [[B12 - Interpreters\|Block 12]] | clox passes book's full test suite. |
| 24 | [[B13 - Algorithms I\|Block 13]] | Every core data structure and algorithm implemented and fuzz-tested; 6.006 final passed; Codeforces ≥1200. |
| 25 | [[B14 - Computer Architecture\|Block 14]] | Pipelined RISC-V core runs compiled C program. |
| 26 | [[B15 - Probability\|Block 15]] | Monte Carlo suite and Markov-chain steady-state solver in Python; final passed. |
| 27 | [[B15a - Signals and Systems Bridge\|Block 15a]] | Implement real-time audio FFT DSP filterbank in C or Rust. |
| 28 | [[B15b - Maker Lab 3 - CAD and 3D Printing\|Block 15b]] | Enclosure, IMU damper mount, prop guard fit by revision 3. |

### Year 3: Depth

| # | Block | Build / done when |
| :-- | :--- | :--- |
| 29 | [[B16 - Operating Systems\|Block 16]] | All xv6 labs pass make grade + minimal bootable kernel. |
| 30 | [[B16a - Maker Lab 4 - Raspberry Pi and Embedded Linux\|Block 16a]] | Companion computer survives 50 power cycles + 1 h UART fuzzing. |
| 31 | [[B17 - Software Construction\|Block 17]] | Rebuilt clox/Monkey under spec, rep invariants, AF. |
| 32 | [[B18 - Real Analysis\|Block 18]] | Prove Bolzano–Weierstrass, EVT, uniform-continuity from definitions unaided. *(optional)* |
| 33 | [[B19 - Networking\|Block 19]] | All 8 labs pass; TCP stack fetches real web page. |
| 34 | [[B19a - Wireless, Mesh and Network Science\|Block 19a]] | Consensus on a real mesh matches the λ2 prediction within 2x. |
| 35 | [[B20 - Algorithms II\|Block 20]] | Max-flow (Edmonds–Karp, Dinic) and a simplex solver, benchmarked on DIMACS graphs; 6.046 final passed; Codeforces ≥1600. |
| 36 | [[B21 - Databases\|Block 21]] | All four BusTub projects pass Gradescope; DDIA read cover to cover. *(optional)* |
| 37 | [[B21a - Maker Lab 5 - PCB Design\|Block 21a]] | Own 2-layer MCU + IMU board passes DRC and brings up. |
| 38 | [[B22 - Statistics\|Block 22]] | Real dataset MLE, CI, hypothesis tests, MCMC Bayesian inference. |
| 39 | [[B22a - Machine Learning\|Block 22a]] | All OLL exercises pass; regression, classifiers, a neural net and k-means built from scratch in NumPy. |

### Year 4: Advanced Core and Specializations

| # | Block | Build / done when |
| :-- | :--- | :--- |
| 40 | [[B23 - Distributed Systems\|Block 23]] | All labs pass 500 consecutive runs under `go test -race`. |
| 41 | [[B23a - Parallel Computing\|Block 23a]] | Assignments 1–3 correct and fast; thread pool clean under ThreadSanitizer. |
| 42 | [[B24 - Theory of Computation\|Block 24]] | 18.404J final passed; prove NP-completeness and undecidability by reduction. *(optional)* |
| 43 | [[B24a - Applied Cryptography and Protocol Security\|Block 24a]] | Crypto I done; secure swarm link fails closed under replay/tamper. |
| 44 | [[B25 - Convex Optimization\|Block 25]] | EE364A homework 1–8 done; CVXPY project + manual KKT. |
| 45 | [[B25a - Deep Learning\|Block 25a]] | Autograd engine + GPT from scratch; CS231n assignments 1–3 pass their checks. |
| 46 | [[Specialization Branches\|Block 26]] | Your chosen track's course project (see the track note). |
| 47 | [[B27 - Intensive Cryptopals\|Block 27]] | Sets 1–6 solved with tests; 7–8 stretch. |
| 48 | [[B27a - Drone Lab - Flight Stack, ROS 2 and SITL\|Block 27a]] | 10/10 SITL missions (3 vehicles); one micro-drone flies indoors; failsafes logged. |
| 49 | [[Specialization Branches\|Block 28]] | Your chosen track's course project (see the track note). |
| 50 | [[Specialization Branches\|Block 29]] | Your chosen track's course project (see the track note). |
| 51 | [[Employability Portfolio and Review\|Employability Portfolio]] | Due by end of Year 4: three public projects, resume, outside review ([[DR-001 - Program Scope, Phases, and Timeline\|DR-001]]). *(optional)* |

### Year 5: The MEng Year

| # | Block | Build / done when |
| :-- | :--- | :--- |
| 52 | [[B30 - Magnum Opus Capstone\|Block 30]] | Milestones M0–M6 (+ M2b digital twin) met. |
| 53 | [[Specialization Branches\|Block 31]] | Your chosen track's course project (see the track note). |
| 54 | [[B32 - Information Theory\|Block 32]] | Derive Shannon entropy, channel capacity, Huffman/Arithmetic encoders, and LDPC codes. |

### Optional Electives (E1–E2)

| # | Block | Build / done when |
| :-- | :--- | :--- |
| 55 | [[E1 - Artificial Intelligence\|E1]] | CS188 Pacman agents with A*, alpha-beta and Q-learning all pass. *(optional)* |
| 56 | [[E2 - Computer Security\|E2]] | The six public 6.1600 labs done. *(optional)* |

---

## 🚀 Specialization Track Capstones

| Track | Capstone build |
| :--- | :--- |
| [[T01 - Deep AI and Machine Learning\|T01]] | Production-Grade Autoregressive Transformer Training & Quantized Serving Engine |
| [[T02 - Advanced Systems and Performance\|T02]] | Production-Grade High-Performance Storage Engine or Kernel/DB Upstream Contribution |
| [[T03 - Advanced Security and Cryptography\|T03]] | End-to-End Audited Encrypted Messaging Protocol with Post-Quantum Hybrid KEM |
| [[T04 - Advanced Graphics and Vision\|T04]] | Spectral Monte Carlo Path Tracer with Volumetric Scattering and Neural Denoising |
| [[T05 - Advanced Programming Languages and Compilers\|T05]] | End-to-End Optimizing Compiler targeting RISC-V with Mechanized Type Soundness Proof |
| [[T06 - Advanced Computer Engineering\|T06]] | Tapeout-Ready 32-bit RISC-V SoC with AXI Bus, Peripherals, and Silicon DRC/LVS Verification |
| [[T07 - TinyML and Edge AI\|T07]] | Autonomous Real-Time Keyword Spotting & Vision Anomaly Detection on Bare-Metal Microcontroller |
| [[T08 - Quantum Information and Computing\|T08]] | End-to-End Quantum Compiler & Variational Quantum Eigensolver (VQE) Pipeline |
| [[T09 - Autonomous Robotics\|T09]] | Autonomous Indoor Navigation & Exploration System in ROS 2 / Gazebo |
| [[T10 - Full-Stack and Product Engineering\|T10]] | A deployed, tested, multi-user web product with authentication, a relational database, CI/CD and monitoring, used by real people other than you. Ship a written design doc and a postmortem of one real incident or failed assumption. |
| [[T11 - Signal Processing and Communications\|T11]] | A software-defined-radio receiver for a real over-the-air digital signal, written by you from the IQ samples up: filtering, timing and carrier recovery, demodulation, decoding and error correction (reuse your Block 32 LDPC or Hamming code where it fits). Ship measured BER or packet-success curves and a write-up comparing them to theory. |

The program capstone: [[B30 - Magnum Opus Capstone|Block 30, Autonomous Drone Swarm Prototype]] (milestones M0–M6 + M2b).

---

## 💡 Weekly Mini-Build Ideas (after Week 12)
- **Year 1:** CS61A *Hog* dice-game strategies; Scheme turtle art; Desmos animations for calculus; phyphox experiments for physics; a Jack game (Snake or Tetris) on your Nand2Tetris computer; a C text adventure; Wokwi/Arduino gadgets in Maker Lab 1.
- **Year 2:** a tiny Unix shell (CS:APP); image compression with SVD (linear algebra); a new feature in your own language (interpreters); a maze generator and solver visualizer (algorithms); an LED game on the FPGA (architecture); a Monte Carlo casino simulator (probability); a live audio spectrum visualizer (signals); a 3D-printed phone stand (CAD).
- **Year 3:** a new xv6 system call; a Raspberry Pi camera timelapse; a chat server (networking); an ESP-NOW mesh between two boards; an LED badge PCB; analysis of your own study-log hours (statistics); a handwritten-digit recognizer (ML).
- **Year 4:** a Raft visualizer (distributed systems); a CUDA Mandelbrot zoom (parallel); Cryptopals sets (crypto); a trajectory planner with CVXPY (optimization); a tiny GPT trained on your own writing (deep learning); SITL missions (Drone Lab).
- **Year 5:** the capstone milestones are the builds.

*Back to [[00 - Start Here|Start Here]] · [[Projects Hub]]*
