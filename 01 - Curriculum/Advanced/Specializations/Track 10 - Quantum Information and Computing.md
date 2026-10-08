---
block_id: "Block 51"
track_id: "Track 10"
title: "Quantum Information and Computing"
category: "advanced"
term: "Years 4 & 5"
status: not-started
prerequisites:
  - "Physics II"
  - "Linear Algebra"
  - "Probability"
  - "Theory of Computation"
target_profile: "Quantum Software Engineer, Quantum Algorithms Researcher, Quantum Information Scientist"
aliases: [Track 10 - Quantum Information and Computing, Track 10 - Quantum Computing]
tier: "Tier 3 - Depth"
hours_estimate: 400
hours_actual: 0
---

# Track 10: Quantum Information and Computing

> [!INFO] Track Overview
> - **Track ID:** Track 10
> - **Prerequisites:** [[Physics II]], [[Linear Algebra]], [[Probability]], [[Theory of Computation]]
> - **Target Profile:** Quantum Software Engineer, Quantum Algorithms Researcher, Quantum Information Scientist
> - **Structure:** Two core courses plus three progressive labs and one comprehensive capstone build deliverable.
> - **Curriculum Position:** Elective specialization block across Years 4 & 5 (*"Two deep beats six shallow"*).

---

## 🎯 Why This Track Matters

Classical computational complexity is founded on the Church-Turing thesis: any physically realizable computing machine can be simulated by a probabilistic Turing machine with at most polynomial slowdown. Quantum computing shatters this foundational premise. By exploiting the physical phenomena of quantum linear superposition, quantum entanglement, and complex probability amplitude interference, quantum algorithms can solve specific computational problems exponentially or quadratically faster than any classical algorithm known.

Shor's algorithm solves prime factorization and discrete logarithms in polynomial time $\mathcal{O}((\log N)^3)$, rendering classical RSA and elliptic-curve cryptography obsolete, while quantum simulation provides polynomial-time solutions to molecular Hamiltonian dynamics and condensed matter physics. However, building practical quantum systems requires bridging deep mathematical physics with concrete software engineering. This track equips students with the linear algebraic postulates of quantum mechanics, universal circuit synthesis, quantum phase estimation, stabilizer error-correcting codes (surface codes), minimum-weight matching decoders, and hybrid quantum-classical NISQ algorithm compilation using industry-standard toolchains (Qiskit, Cirq).

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[Physics II]]
- [[Linear Algebra]]
- [[Probability]]
- [[Theory of Computation]]




## 📚 Core Courses

### Course 1: Foundations of Quantum Information & Algorithms

This course establishes the rigorous linear-algebraic postulates of quantum computation, universal quantum gate sets, and foundational quantum algorithms.

#### Module 1: The Linear-Algebraic Postulates of Quantum Mechanics
- State space postulate: complex Hilbert space $\mathcal{H}_d$, state vectors $|\psi\rangle$, and Dirac bra-ket notation.
- Operator algebra: unitary transformations ($U^\dagger U = I$), Hermitian observables ($H = H^\dagger$), and spectral decomposition:
  $$H = \sum_i \lambda_i |v_i\rangle \langle v_i|$$
- Measurement postulate: Projective (von Neumann) measurements and Positive Operator-Valued Measures (POVMs); Born's rule ($P(m) = \langle\psi|M_m^\dagger M_m|\psi\rangle$).
- Composite systems and tensor products: $\mathcal{H}_{AB} = \mathcal{H}_A \otimes \mathcal{H}_B$, state vector expansion, and tensor contraction.

#### Module 2: Qubits, Entanglement & Bell Non-Locality
- The single-qubit state space: the Bloch sphere representation ($|\psi\rangle = \cos(\theta/2)|0\rangle + e^{i\phi}\sin(\theta/2)|1\rangle$).
- Multi-qubit states, product states, and entangled states: the 4 canonical Bell states ($|\Phi^\pm\rangle, |\Psi^\pm\rangle$).
- Entanglement quantification: Schmidt decomposition, Schmidt rank, concurrence, and von Neumann entanglement entropy.
- The No-Cloning Theorem: algebraic proof of the impossibility of unitary state duplication.
- Protocols: quantum teleportation, superdense coding, and Bell-CHSH inequality violations.

#### Module 3: Universal Circuit Synthesis & Quantum Compilers
- Single-qubit Pauli gates ($X, Y, Z$), Hadamard ($H$), Phase ($S$), and $\pi/8$ gate ($T$).
- Multi-qubit controlled gates: Controlled-NOT (CNOT), Controlled-Phase, Toffoli (CCNOT), and Fredkin (CSWAP).
- Universality proofs: proving the Clifford + $T$ gate set is universal for quantum computation.
- The Solovay-Kitaev Theorem: approximating arbitrary single-qubit unitaries within accuracy $\epsilon$ using a gate sequence of length $\mathcal{O}(\log^c(1/\epsilon))$.

#### Module 4: Quantum Fourier Transform & Phase Estimation
- The Discrete Fourier Transform vs the Quantum Fourier Transform (QFT).
- Circuit implementation of QFT: product representation and decomposition into $\mathcal{O}(n^2)$ Hadamard and controlled phase-shift gates ($R_k$).
- Quantum Phase Estimation (QPE): extracting eigenvalues of unitary operators with high probability.
- Analytical derivation of precision, error bounds, and success probabilities under finite register lengths.

#### Module 5: Breakthrough Quantum Algorithms
- Oracular algorithms: Deutsch-Jozsa, Bernstein-Vazirani, and Simon's period-finding algorithm with exponential query separation.
- Shor's algorithm: order-finding via QPE, reduction of factoring to order-finding, and continued fraction expansion for period recovery.
- Grover's quantum search algorithm: amplitude amplification, geometric state space rotation, and proving the optimal asymptotic lower bound $\Omega(\sqrt{N})$.

---

### Course 2: Fault Tolerance, Quantum Error Correction & NISQ Systems

This course explores decoherence, open quantum systems, stabilizer codes, topological surface codes, and variational algorithms for noisy intermediate-scale quantum (NISQ) processors.

#### Module 1: Density Operators & Open Quantum Systems
- The density matrix formalism: pure vs mixed states ($\rho = \sum p_i |\psi_i\rangle \langle\psi_i|$); purity and trace-class properties ($\text{Tr}(\rho) = 1, \rho \ge 0$).
- Partial trace and reduced density operators: describing sub-system entanglement.
- Quantum noise channels: completely positive trace-preserving (CPTP) maps and Kraus operator representations:
  $$\mathcal{E}(\rho) = \sum_k E_k \rho E_k^\dagger, \quad \sum_k E_k^\dagger E_k = I$$
- Physical decoherence channels: bit-flip, phase-flip, amplitude damping ($T_1$ relaxation), and depolarizing noise ($T_2$ dephasing).

#### Module 2: The Stabilizer Formalism & Gottesman-Knill
- The $n$-qubit Pauli group $\mathcal{G}_n$ and its algebraic structure.
- Stabilizer groups: abelian subgroups $S \subset \mathcal{G}_n$ not containing $-I$.
- The stabilizer subspace: $V_S = \{|\psi\rangle : M|\psi\rangle = |\psi\rangle, \forall M \in S\}$.
- The Clifford Group: normalizer of the Pauli group ($C \mathcal{G}_n C^\dagger = \mathcal{G}_n$).
- The Gottesman-Knill Theorem: rigorous proof that quantum circuits initialized in computational basis states consisting solely of Clifford gates can be simulated efficiently in classical polynomial time $\mathcal{O}(n^2)$.

#### Module 3: Quantum Error-Correcting Codes (QECC)
- The quantum error correction conditions (Knill-Laflamme theorem).
- 3-qubit bit-flip and phase-flip repetition codes.
- Shor's 9-qubit code: concatenated protection against arbitrary single-qubit errors.
- Calderbank-Shor-Steane (CSS) codes: constructing quantum codes from classical linear codes ($C_1, C_2^\perp$).
- Steane's $[7, 1, 3]$ code and transversal gate implementations.

#### Module 4: Topological Surface Codes & Syndrome Decoders
- 2D planar and toric surface codes: star ($A_s = \prod_{i \in s} X_i$) and plaquette ($B_p = \prod_{j \in p} Z_j$) stabilizer operators.
- Anyonic excitations: creation, movement, and braiding of electric ($e$) and magnetic ($m$) quasiparticles.
- Syndrome extraction circuits and fault-tolerant stabilizer measurement.
- Decoding algorithms: Minimum-Weight Perfect Matching (MWPM) via Edmonds' Blossom algorithm, and Union-Find decoders.
- The Quantum Threshold Theorem: proving that when physical gate error rates fall below a critical threshold ($\approx 1\%$), arbitrary quantum circuits can be executed with arbitrary logical fidelity.

#### Module 5: Variational Quantum Algorithms for NISQ Hardware
- Noisy Intermediate-Scale Quantum (NISQ) constraints: finite coherence times, gate errors, and constrained physical connectivity.
- Variational Quantum Eigensolver (VQE): Rayleigh-Ritz variational principle, parameterized ansatz state generation ($U(\theta)$), and Hamiltonian expectation value measurement.
- Fermion-to-qubit mappings: Jordan-Wigner transformation and Bravyi-Kitaev transformation.
- Barren plateaus in quantum neural networks: vanishing gradient concentration of measure proofs.

---

## 📑 Seminal Papers & Advanced Textbooks

- **Shor, P. W. (1994).** *Algorithms for quantum computation: discrete logarithms and factoring*. Proceedings of the 35th Annual IEEE Symposium on Foundations of Computer Science (FOCS '94), 124–134.
- **Grover, L. K. (1996).** *A fast mechanical quantum search algorithm*. Proceedings of the 28th Annual ACM Symposium on Theory of Computing (STOC '96), 212–219.
- **Fowler, A. G., Mariantoni, M., Martinis, J. M., & Cleland, A. N. (2012).** *Surface codes: Towards practical large-scale quantum computation*. Physical Review A, 86(3), Article 032324.
- **Kitaev, A. Y. (2003).** *Fault-tolerant quantum computation by anyons*. Annals of Physics, 303(1), 2–30.
- **Nielsen, M. A., & Chuang, I. L. (2010).** *Quantum Computation and Quantum Information, 10th Anniversary Edition*. Cambridge University Press.
- **Preskill, J. (2023).** *Quantum Information and Computation*. California Institute of Technology (Physics 219 Lecture Notes).

---

## 🛠️ Progressive Labs

### Lab 1: Statevector Quantum Circuit Simulator in Python/Rust
- **Objective:** Build a high-performance statevector quantum circuit simulator from scratch supporting arbitrary single-qubit rotations and multi-qubit controlled gates.
- **Deliverables:**
  - Python / Rust library executing exact tensor product contractions and state evolution across an $n$-qubit register ($2^n$ complex amplitudes).
  - Validation test suite executing Shor's algorithm for $N = 15$ with exact probability output distribution.
- **Acceptance Criteria:**
  - The simulator must execute an arbitrary 20-qubit circuit with $> 100$ gates in $< 5 \text{ seconds}$ on standard desktop CPU.
  - Verification tests prove bit-exact numerical parity ($\ell_2$-norm difference $< 10^{-12}$) against Qiskit Aer statevector simulator outputs.

### Lab 2: Stabilizer Simulator & Gottesman-Knill Engine
- **Objective:** Implement a polynomial-time stabilizer tableau simulator using binary symplectic linear algebra over $\mathbb{F}_2$.
- **Deliverables:**
  - Simulator implementing the Aaronson-Gottesman tableau representation ($2n \times 2n$ binary matrix and phase vector).
  - Clifford gate execution routines ($H, S, \text{CNOT}$) and projective Pauli measurement updating stabilizer generators.
- **Acceptance Criteria:**
  - Automated benchmarking proves polynomial-time scaling $\mathcal{O}(n^2)$ by simulating a 1,000-qubit random Clifford circuit across 5,000 gates in $< 2.0 \text{ seconds}$.
  - Full equivalence verified against statevector simulation on 10-qubit circuits across 1,000 random Clifford test runs.

### Lab 3: 2D Surface Code Minimum-Weight Perfect Matching (MWPM) Decoder
- **Objective:** Construct a simulation harness for the rotated 2D surface code subject to independent bit-flip and phase-flip phenomenological noise, integrating an Edmonds' Blossom MWPM decoder.
- **Deliverables:**
  - Surface code lattice generator supporting code distances $d \in \{3, 5, 7\}$.
  - Matching graph generator and PyMatching / Blossom V interface solving for minimum-weight error chains from syndrome measurements.
- **Acceptance Criteria:**
  - Monte Carlo simulation sweeping physical error rates from $p = 0.001$ to $p = 0.05$ over $10^5$ shots per point.
  - The decoder must reproduce the logical error suppression threshold curve demonstrating a clear crossing point at threshold error rate $p_{\text{th}} \approx 1.0\%$.

---

## 🏆 Capstone Build Deliverable

### End-to-End Quantum Compiler & Variational Quantum Eigensolver (VQE) Pipeline

A complete software compilation and quantum algorithm pipeline that maps molecular electronic structure Hamiltonians into optimized quantum circuits and determines ground-state energies via VQE.

```text
+-----------------------------------------------------------------------------------+
|                        VQE QUANTUM ALGORITHM PIPELINE                             |
|                                                                                   |
|  [ Molecular Coordinates ] ---> [ PySCF Hamiltonian ] ---> [ Jordan-Wigner Map ]  |
|                                                                    |              |
|                                                                    v              |
|  [ Qiskit / Cirq Backend ] <--- [ Hardware Swap Router ] <--- [ Ansatz Generator ]|
|              |                                                                    |
|              v                                                                    |
|  [ Expectation Estimator ] ---> [ Classical Optimizer ] ---> [ Ground-State E ]   |
+-----------------------------------------------------------------------------------+
```

#### System Architecture & Specifications
1. **Hamiltonian Mapper:** Ingest molecular geometries (e.g. $\text{H}_2, \text{LiH}$), compute 1-electron and 2-electron integrals via PySCF, and perform Jordan-Wigner / Parity transformation into a weighted sum of Pauli strings:
   $$H = \sum_j c_j P_j, \quad P_j \in \{I, X, Y, Z\}^{\otimes n}$$
2. **Circuit Synthesis & Routing:** Construct hardware-efficient parameterized ansatz circuits ($R_y$ single-qubit rotations with linear/all-to-all entangling CNOT layers); implement an A* or heuristic SWAP router that maps logical gates onto a constrained physical hardware topology coupling graph (e.g. IBM Eagle / Falcon heavy-hex layout).
3. **Hybrid Optimization:** Classical optimization loop utilizing COBYLA / SPSA / Adam with analytical parameter-shift gradient evaluation.

#### Verification & Acceptance Criteria
- **Chemical Accuracy:** The VQE pipeline must compute the ground-state dissociation curve of molecular Hydrogen ($\text{H}_2$) across interatomic distances $R \in [0.2, 2.5] \text{ \AA}$, converging within chemical accuracy ($\le 1.6 \times 10^{-3} \text{ Hartree} \approx 1.0 \text{ kcal/mol}$) of Full Configuration Interaction (FCI) exact diagonalization.
- **Hardware Noise Mitigation:** Must execute on both an ideal statevector backend and a noisy density-matrix backend with depolarizing and readout noise, successfully applying Zero-Noise Extrapolation (ZNE) error mitigation to recover true ground state energy.
- **Test Commands:**
  ```bash
  # Execute unit tests for circuit synthesis and Clifford gates
  pytest tests/test_quantum_compiler.py -v
  # Run VQE ground-state convergence on H2 molecule
  python3 scripts/run_vqe_simulation.py --molecule H2 --ansatz hardware_efficient --optimizer SPSA
  # Run SWAP routing benchmark on heavy-hex topology
  python3 scripts/benchmark_router.py --coupling heavy_hex --circuits qasm_benchmarks/
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

- **Sequential Flow:** [[Track 9 - Hardware-in-the-Loop Virtualization, Digital Twins and CPS|← Track 9 - Hardware-in-the-Loop Virtualization, Digital Twins and CPS]] | [[00 - Dashboard|Dashboard]] | [[Track 11 - Autonomous Robotics and Cyber-Physical Systems|Track 11 - Autonomous Robotics and Cyber-Physical Systems →]]
