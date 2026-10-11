---
title: "Research Paper Reading Hub"
type: hub
tags:
  - hub
  - navigation
---

# Research Paper Reading Hub

*Track, analyze, and synthesize foundational computer science research using the Three-Pass Method from Keshav (2007).*

---

> [!TIP]
> Use the template [[Paper Summary (3-Pass) Template]] whenever starting a new paper note. Every paper read should yield an atomic synthesis note linked to its nearest module.

---

## 🧭 The Keshav Three-Pass Methodology
*Deep dive + project: [[LM13 - Three-Pass Paper Reading|LM13]]. The pass lengths below are Keshav's own guidance for the technique, not a curriculum schedule.*

1. **Pass 1 (Bird's Eye — 10–15 min):** Read title, abstract, section headings, conclusion, and skim references. Determine the category, context, correctness plausibility, and contributions ($C^5$).
2. **Pass 2 (Grasp Content — 1–2 hours):** Read with attention to figures, diagrams, and proofs. Mark unfamiliar terms, skipped proofs, and core assumptions.
3. **Pass 3 (Virtually Re-implement — 3–5 hours):** Re-create the paper from first principles. Virtually re-derive every lemma, re-evaluate experimental setups, and identify implicit edge conditions or hidden flaws.

---

## 📚 Seminal PhD-Level Paper Curriculum (35 Landmark Papers)

This curated catalog contains foundational PhD-level papers categorized across 7 core computer science disciplines. Each entry links to the **nearest module** of the current curriculum by topic, or says it is beyond the core. The papers are optional enrichment; no module requires them.

---

### 1. Computer Systems, Operating Systems & Networks

| # | Paper Title & Authors | Year | Venue | Landmark Invariant / Contribution | Nearest module |
|:---|:---|:---:|:---:|:---|:---|
| 1 | **"The UNIX Time-Sharing System"** (Dennis M. Ritchie & Ken Thompson) | 1974 | *Communications of the ACM* | Unified hierarchical file system, uniform I/O interface via file descriptors, orthogonal composability via kernel pipelines. | [08](<../08-operating-systems/overview.md>) |
| 2 | **"Exokernel: An Operating System Architecture for Application-Level Resource Management"** (Dawson R. Engler, M. Frans Kaashoek, James O'Toole) | 1995 | *SOSP '95* | End-to-end principle applied to OS kernels: separate protection from management; expose raw hardware securely via library OSs. | [08](<../08-operating-systems/overview.md>) |
| 3 | **"The Design Philosophy of the DARPA Internet Protocols"** (David D. Clark) | 1988 | *SIGCOMM '88* | Fate-sharing state distribution model; packet switching resilience where intermediate router crashes do not drop connection state. | [09](<../09-networking/overview.md>) |
| 4 | **"Hints for Computer System Design"** (Butler W. Lampson) | 1983 | *ACM Operating Systems Review* | Engineering invariants: worst-case interfaces, hints vs. absolute truth, crash recovery by idempotent state reconstruction. | [07](<../07-systems-programming/overview.md>) |
| 5 | **"seL4: Formal Verification of an OS Kernel"** (Gerwin Klein et al.) | 2009 | *SOSP '09* | First machine-checked formal proof of functional correctness and security enforcement (Isabelle/HOL) for a general-purpose microkernel. | [08](<../08-operating-systems/overview.md>) |

---

### 2. Computer Architecture & Hardware Systems

| # | Paper Title & Authors | Year | Venue | Landmark Invariant / Contribution | Nearest module |
|:---|:---|:---:|:---:|:---|:---|
| 6 | **"The Case for the Reduced Instruction Set Computer"** (David A. Patterson & David R. Ditzel) | 1980 | *ACM SIGARCH Computer Architecture News* | Quantified execution efficiency of simplified instruction sets with single-cycle register-to-register datapaths and compiler-driven scheduling. | [06](<../06-computer-architecture/overview.md>) |
| 7 | **"A Case for Redundant Arrays of Inexpensive Disks (RAID)"** (David A. Patterson, Garth Gibson, Randy H. Katz) | 1988 | *SIGMOD '88* | Formalization of RAID levels 0 through 5; parity calculations and mean-time-to-data-loss (MTTDL) reliability derivations. | [06](<../06-computer-architecture/overview.md>) |
| 8 | **"In-Datacenter Performance Analysis of a Tensor Processing Unit"** (Norman P. Jouppi et al.) | 2017 | *ISCA '17* | Microarchitecture of Google TPU v1: 2D matrix multiply unit (systolic array) optimizing roofline operational intensity for deep learning inference. | [06](<../06-computer-architecture/overview.md>) |
| 9 | **"Memory Consistency and Event Ordering in Scalable Shared-Memory Multiprocessors"** (Kourosh Gharachorloo et al.) | 1990 | *ISCA '90* | Formalization of weak ordering and release consistency memory models; decoupling synchronization operations from data access reordering. | [07](<../07-systems-programming/overview.md>) |
| 10 | **"Simultaneous Multithreading: Maximizing On-Chip Parallelism"** (Dean M. Tullsen, Susan J. Eggers, Henry M. Levy) | 1995 | *ISCA '95* | Dynamic hardware sharing of out-of-order execution pipelines across multiple hardware thread contexts to eliminate horizontal and vertical stalls. | [06](<../06-computer-architecture/overview.md>) |

---

### 3. Theoretical Computer Science & Advanced Algorithms

| # | Paper Title & Authors | Year | Venue | Landmark Invariant / Contribution | Nearest module |
|:---|:---|:---:|:---:|:---|:---|
| 11 | **"The Complexity of Theorem-Proving Procedures"** (Stephen A. Cook) | 1971 | *STOC '71* | Foundational proof of NP-completeness: generic polynomial-time reduction of non-deterministic Turing machines to Boolean Satisfiability (SAT). | — (beyond the core) |
| 12 | **"Reducibility Among Combinatorial Problems"** (Richard M. Karp) | 1972 | *Complexity of Computer Computations* | Karp's 21 NP-complete problems; establishing standard polynomial-time reductions for Clique, Vertex Cover, Set Cover, and Hamiltonian Cycle. | — (beyond the core) |
| 13 | **"Efficiency of a Good But Not Linear Set Union Algorithm"** (Robert E. Tarjan) | 1975 | *Journal of the ACM* | Tight amortized complexity bound $\mathcal{O}(m \alpha(n))$ for Disjoint Set Union with path compression and union-by-rank using potential methods. | [05](<../05-data-structures-and-algorithms/overview.md>) |
| 14 | **"Nearly-Linear Time Algorithms for Graph Partitioning, Graph Sparsification, and Solving Linear Systems"** (Daniel A. Spielman & Shang-Hua Teng) | 2004 | *STOC '04* | Spectral graph theory breakthrough: solving symmetric diagonally dominant (SDD) linear systems in $\tilde{\mathcal{O}}(m \log^c n)$ time via Cheeger cuts. | [05](<../05-data-structures-and-algorithms/overview.md>) |
| 15 | **"Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer"** (Peter W. Shor) | 1997 | *SIAM Journal on Computing* | Quantum Fourier Transform applied to modular period finding; exponential speedup factoring integers in $\mathcal{O}((\log N)^3)$ time. | — (beyond the core) |

---

### 4. Programming Languages, Compilers & Formal Methods

| # | Paper Title & Authors | Year | Venue | Landmark Invariant / Contribution | Nearest module |
|:---|:---|:---:|:---:|:---|:---|
| 16 | **"A Theory of Type Polymorphism in Programming"** (Robin Milner) | 1978 | *Journal of Computer and System Sciences* | Hindley-Milner type system and Algorithm W; provable type soundness and principal type inference without explicit type annotations. | — (beyond the core) |
| 17 | **"Abstract Interpretation: A Unified Lattice Model for Static Analysis of Programs"** (Patrick Cousot & Radhia Cousot) | 1977 | *POPL '77* | Galois connections between concrete trace semantics and abstract property lattices; sound static program analysis via widening operators. | — (beyond the core) |
| 18 | **"Efficiently Computing Static Single Assignment Form and the Control Dependence Graph"** (Ron Cytron, Jeanne Ferrante, Barry K. Rosen, Mark N. Wegman, F. Kenneth Zadeck) | 1991 | *ACM TOPLAS* | Dominance frontier algorithm for optimal $\phi$-function placement in SSA intermediate representation, transforming compiler optimization pipelines. | — (beyond the core) |
| 19 | **"A Syntactic Approach to Type Soundness"** (Andrew K. Wright & Matthias Felleisen) | 1994 | *Information and Computation* | Standard inductive proof technique for language type soundness via Progress ($e: \tau \implies e \text{ value} \lor e \to e'$) and Preservation ($e: \tau \land e \to e' \implies e': \tau$). | [03](<../03-discrete-math/overview.md>) |
| 20 | **"RustBelt: Securing the Foundations of the Rust Programming Language"** (Ralf Jung, Jacques-Henri Jourdan, Robbert Krebbers, Derek Dreyer) | 2017 | *POPL 2018* | Machine-checked semantic model (Iris separation logic in Coq) proving memory safety of Rust's type system and encapsulated unsafe abstractions. | — (beyond the core) |

---

### 5. Databases & Distributed Systems

| # | Paper Title & Authors | Year | Venue | Landmark Invariant / Contribution | Nearest module |
|:---|:---|:---:|:---:|:---|:---|
| 21 | **"Time, Clocks, and the Ordering of Events in a Distributed System"** (Leslie Lamport) | 1978 | *Communications of the ACM* | Logical clocks, happened-before partial order ($\to$), total ordering of events, and state machine replication foundations. | — (beyond the core) |
| 22 | **"Impossibility of Distributed Consensus with One Faulty Process"** (Michael J. Fischer, Nancy A. Lynch, Michael S. Paterson (FLP)) | 1985 | *Journal of the ACM* | Proof by bivalence perturbation that no deterministic asynchronous protocol can guarantee consensus in the presence of even a single crash failure. | — (beyond the core) |
| 23 | **"In Search of an Understandable Consensus Algorithm" (Raft)** (Diego Ongaro & John Ousterhout) | 2014 | *USENIX ATC '14* | Decomposed consensus via leader election, randomized timers, and log matching invariant; provably safe state machine replication. | — (beyond the core) |
| 24 | **"ARIES: A Transaction Recovery Method Supporting Fine-Granularity Locking and Partial Rollbacks Using Write-Ahead Logging"** (C. Mohan, Don Haderle, Bruce Lindsay, Hamid Pirahesh, Peter Schwarz) | 1992 | *ACM Transactions on Database Systems* | Physiological logging, Compensation Log Records (CLRs), and repeating history during Redo to guarantee idempotent crash recovery. | [11](<../11-databases/overview.md>) |
| 25 | **"Spanner: Google's Globally Distributed Database"** (James C. Corbett et al.) | 2012 | *OSDI '12* | External consistency (linearizability) across wide-area networks using TrueTime atomic/GPS uncertainty bounds ($2\epsilon$ commit-wait invariant). | [11](<../11-databases/overview.md>) |

---

### 6. Machine Learning, Deep Learning & Generative Modeling

| # | Paper Title & Authors | Year | Venue | Landmark Invariant / Contribution | Nearest module |
|:---|:---|:---:|:---:|:---|:---|
| 26 | **"Multilayer Feedforward Networks are Universal Approximators"** (Kurt Hornik, Maxwell Stinchcombe, Halbert White) | 1989 | *Neural Networks* | Stone-Weierstrass and Hahn-Banach derivation proving single-hidden-layer feedforward networks with non-polynomial activations are dense in $C(K)$. | [12](<../12-math-for-engineering/overview.md>) |
| 27 | **"Attention Is All You Need"** (Ashish Vaswani et al.) | 2017 | *NeurIPS 2017* | Scaled dot-product multi-head self-attention mechanism: $\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$, eliminating recurrent bottleneck. | [12](<../12-math-for-engineering/overview.md>) |
| 28 | **"Deep Unsupervised Learning using Nonequilibrium Thermodynamics"** (Jascha Sohl-Dickstein, Eric A. Weiss, Niru Maheswaranathan, Surya Ganguli) | 2015 | *ICML 2015* | Physical foundation of diffusion probabilistic models: reversing a forward Markovian Gaussian perturbation process to learn complex data distributions. | [12](<../12-math-for-engineering/overview.md>) |
| 29 | **"Neural Ordinary Differential Equations"** (Ricky T. Q. Chen, Yulia Rubanova, Jesse Bettencourt, David Duvenaud) | 2018 | *NeurIPS 2018 (Best Paper)* | Continuous-depth residual networks formulated as ODEs; adjoint sensitivity method for constant memory $\mathcal{O}(1)$ backpropagation. | — (beyond the core) |
| 30 | **"Proximal Policy Optimization Algorithms"** (John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, Oleg Klimov) | 2017 | *arXiv:1707.06347* | Clipped surrogate objective preventing destructively large policy updates in reinforcement learning: $L^{\text{CLIP}}(\theta) = \hat{\mathbb{E}}_t [\min(r_t(\theta)\hat{A}_t, \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon)\hat{A}_t)]$. | [12](<../12-math-for-engineering/overview.md>) |

---

### 7. Security, Cryptography & Information Theory

| # | Paper Title & Authors | Year | Venue | Landmark Invariant / Contribution | Nearest module |
|:---|:---|:---:|:---:|:---|:---|
| 31 | **"New Directions in Cryptography"** (Whitfield Diffie & Martin E. Hellman) | 1976 | *IEEE Transactions on Information Theory* | Asymmetric public-key cryptography; Diffie-Hellman key exchange over discrete logarithm groups; computational one-way trapdoor functions. | [03](<../03-discrete-math/overview.md>) |
| 32 | **"A Method for Obtaining Digital Signatures and Public-Key Cryptosystems"** (Ronald L. Rivest, Adi Shamir, Leonard Adleman) | 1978 | *Communications of the ACM* | The RSA cryptosystem; Euler's totient theorem and integer factorization hardness for digital signatures and encryption. | [03](<../03-discrete-math/overview.md>) |
| 33 | **"On Lattices, Learning with Errors, Random Linear Codes, and Cryptography"** (Oded Regev) | 2005 | *STOC '05* | Reduction from worst-case lattice problems (GapSVP, SIVP) to average-case Learning With Errors (LWE), foundational to post-quantum cryptography. | — (beyond the core) |
| 34 | **"A Mathematical Theory of Communication"** (Claude E. Shannon) | 1948 | *Bell System Technical Journal* | Information entropy $H(X) = -\sum p_i \log_2 p_i$, source coding theorem, and noisy channel coding theorem capacity limit $C = B \log_2(1 + \text{SNR})$. | — (beyond the core) |
| 35 | **"How to Share a Secret"** (Adi Shamir) | 1979 | *Communications of the ACM* | $(k, n)$-threshold secret sharing via Lagrange polynomial interpolation over finite fields $\mathbb{F}_p$; information-theoretically secure against $<k$ colluding shares. | [03](<../03-discrete-math/overview.md>) |

---

## 📈 When to read

Read a paper once you are in, or have finished, its nearest module; papers marked *beyond the core* are for after the curriculum. Start with Pass 1 only. *(The v1 year-by-year roadmap was removed by [DR-011](<../04 - System/DR-011 - Sectioned Curriculum and Frontmatter Schema.md>).)*
