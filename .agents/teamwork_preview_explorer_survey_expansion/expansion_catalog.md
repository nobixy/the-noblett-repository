# Graduate Expansion Catalog: R2 (Vertical Rigor) & R3 (Horizontal Modern Paradigms)

> **Document Type:** Architectural Blueprint & Research Catalog  
> **Author:** Expansion & Paradigms Explorer  
> **Repository:** The Noblett Repository — Independent EECS Curriculum  
> **Target Standards:** Exceeding MIT EECS (Course 6-1, 6-2, 6-3, 6-4, 6-P) + CMU SCS + Stanford CS PhD Qualifying Foundations  
> **Date:** 2026-09-25  

---

## Executive Summary & Curriculum Architecture

This catalog establishes the comprehensive architectural blueprint for:
1. **R2 Vertical Expansion (Graduate-Level Depth):** Injecting graduate-level mathematical foundations, foundational seminal PhD-level papers (3–5 per core area), and rigorous formal textbook proofs into the existing 32-block core curriculum.
2. **R3 Horizontal Expansion (Modern Paradigms):** Designing 6 complete, cutting-edge specialization tracks (TinyML & Edge AI, Rust for Systems Engineering, Hardware-in-the-Loop Virtualization, Formal Verification with Lean 4/Coq, Quantum Information & Computing, Neuromorphic & Heterogeneous Architectures), each complete with learning outcomes, modular syllabi, seminal literature, and industrial-grade lab builds.

```
========================================================================================================
                               THE EXPANDED ELITE EECS CURRICULUM ARCHITECTURE
========================================================================================================
[Phase -1 & 0]   Bedrock Foundations & Tooling (First principles, math foundations, C, headless Linux)
--------------------------------------------------------------------------------------------------------
[Years 1-3 Core] Undergrad Core + R2 Graduate Injections:
                 - Math: Measure Theory, Topology, Category Theory, Abstract Algebra, Spectral Graphs
                 - Systems: FLP Impossibility, ARIES WAL, Cache Coherence Invariants, Little's Law
                 - Theory: Cook-Levin, PCP Theorem, Cheeger's Inequality, Algorithm W Soundness
--------------------------------------------------------------------------------------------------------
[Years 4-5]      MEng & Dual Specializations ("Two deep beats six shallow"):
                 CLASSICAL TRACKS:
                 - Track 1: AI & Machine Learning       | Track 4: Computer Graphics & Vision
                 - Track 2: Systems & Performance        | Track 5: Programming Languages & Compilers
                 - Track 3: Security & Cryptography      | Track 6: Computer Engineering (Deep Hardware)
                 
                 MODERN PARADIGMS (R3):
                 - Track 7: TinyML & Edge AI             | Track 10: Formal Verification (Lean 4 / Coq)
                 - Track 8: Rust Systems Engineering     | Track 11: Quantum Information & Computing
                 - Track 9: HIL Virtualization & CPS     | Track 12: Neuromorphic & Heterogeneous Arch
========================================================================================================
```

---

# Part I: R2 Vertical Expansion — Graduate-Level Mathematical Foundations

Standard undergraduate EECS math covers differential calculus, multivariable calculus, introductory discrete math, introductory linear algebra, and basic probability. To achieve PhD-qualifying depth, the curriculum must vertically integrate six advanced mathematical foundations.

---

### 1. Measure-Theoretic Probability & Stochastic Processes

#### 1.1 Mathematical Core & Conceptual Scope
Transitioning from elementary probability (PDFs, PMFs, discrete conditioning) to rigorous measure spaces $(\Omega, \mathcal{F}, P)$, Borel $\sigma$-algebras, Carathéodory extension, Lebesgue integration, conditional expectation as an orthogonal projection in $L^2$ (Radon-Nikodym derivative), filtration $(\mathcal{F}_t)_{t \ge 0}$, martingales, stopped processes, Brownian motion, and stochastic differential equations (Itô calculus).

#### 1.2 Curriculum Injection Targets
- **Block 15 (Probability — Year 2 Spring):** Inject $\sigma$-algebras, measure spaces, and martingale stopping theorems.
- **Block 22 (Statistics — Year 3 Spring):** Rigorous convergence in probability, almost sure convergence, convergence in distribution, and empirical process theory.
- **Track 1 & Track 7 (AI/ML & TinyML):** Continuous-time diffusion models, stochastic gradient Langevin dynamics (SGLD), score-based generative modeling via reverse SDEs.

#### 1.3 Required Rigorous Textbook Proofs
1. **Carathéodory's Extension Theorem:** Construction of unique measure on $\sigma(\mathcal{A})$ from pre-measure on algebra $\mathcal{A}$; derivation of Lebesgue measure on $\mathbb{R}^n$.
2. **Radon-Nikodym Theorem:** Proving that for measures $\nu \ll \mu$ on $(\Omega, \mathcal{F})$, there exists a unique non-negative measurable function $f = \frac{d\nu}{d\mu}$ such that $\nu(A) = \int_A f \, d\mu$, establishing the rigorous foundation of conditional expectation $\mathbb{E}[X|\mathcal{G}]$.
3. **Doob's Martingale Convergence Theorem:** If $(X_n)_{n \ge 0}$ is a submartingale bounded in $L^1$ ($\sup_n \mathbb{E}[X_n^+] < \infty$), then $X_n \to X_\infty$ almost surely.
4. **Itô's Lemma & Itô Isometry:** Proving $\mathbb{E}[(\int_0^T X_t \, dB_t)^2] = \int_0^T \mathbb{E}[X_t^2] \, dt$ and establishing the second-order Taylor expansion for stochastic differentials $df(t, B_t) = \frac{\partial f}{\partial t} dt + \frac{\partial f}{\partial x} dB_t + \frac{1}{2} \frac{\partial^2 f}{\partial x^2} dt$.

#### 1.4 Seminal Graduate-Level Papers
1. **Kolmogorov, A. N. (1933).** *Grundbegriffe der Wahrscheinlichkeitsrechnung* (Foundations of the Theory of Probability). Julius Springer, Berlin.
2. **Doob, J. L. (1953).** *Stochastic Processes*. John Wiley & Sons. (Foundations of modern martingale theory).
3. **Sohl-Dickstein, J., Weiss, E., Khan, N., & Sompolinsky, H. (2015).** *Deep Unsupervised Learning using Nonequilibrium Thermodynamics*. ICML 2015. (The physical-mathematical origin of diffusion generative models).
4. **Song, Y., Sohl-Dickstein, J., Kingma, D. P., Kumar, A., Ermon, S., & Poole, B. (2020).** *Score-Based Generative Modeling through Stochastic Differential Equations*. ICLR 2021. (Unified continuous-time SDE formulation of diffusion).

#### 1.5 Authoritative Reference Texts
- Rick Durrett, *Probability: Theory and Examples*, 5th ed., Cambridge University Press.
- David Williams, *Probability with Martingales*, Cambridge University Press.
- Patrick Billingsley, *Convergence of Probability Measures*, 2nd ed., Wiley.
- Bernt Øksendal, *Stochastic Differential Equations: An Introduction with Applications*, 6th ed., Springer.

---

### 2. Advanced Convex Optimization & Non-Smooth Analysis

#### 2.1 Mathematical Core & Conceptual Scope
Advancing beyond introductory convex sets and basic gradient descent into infinite-dimensional convex analysis, subgradient calculus, proximal operators, Fenchel-Legendre conjugates, monotone operator theory, interior-point methods, Douglas-Rachford splitting, Alternating Direction Method of Multipliers (ADMM), and non-convex landscape analysis.

#### 2.2 Curriculum Injection Targets
- **Block 25 (Convex Optimization — Year 4 Fall):** Elevate from standard Boyd EE364A homework into rigorous convergence rate proofs, proximal operators, and non-smooth duality.
- **Block 20 (Algorithms II — Year 3 Spring):** Primal-dual schema for approximation algorithms and linear programming relaxations.
- **Track 1 & Track 2 (AI/ML & Systems Performance):** High-dimensional optimization, stochastic variance-reduced gradient (SVRG), and parallel distributed consensus optimization.

#### 2.3 Required Rigorous Textbook Proofs
1. **Hahn-Banach Separation Theorem & Supporting Hyperplanes:** Proving that for any two disjoint non-empty convex sets $C, D \subset \mathbb{R}^n$ with $C$ compact and $D$ closed, there exists a hyperplane strictly separating them.
2. **Karush-Kuhn-Tucker (KKT) Optimality with Slater's Condition:** Formal derivation of saddle-point duality; proving that under convexity and Slater's constraint qualification ($\exists x \in \text{relint}(D) \text{ s.t. } f_i(x) < 0$), the duality gap is zero ($p^* = d^*$) and dual optimum is attained.
3. **Fenchel-Rockafellar Duality Theorem:** Derivation of the Fenchel dual problem $\inf_{x} \{f(x) + g(Ax)\} = \sup_{y} \{-f^*(-A^Ty) - g^*(y)\}$ and establishing subdifferential calculus $\partial(f+g) = \partial f + \partial g$.
4. **Nesterov Accelerated Gradient Lower Bound & Optimal Convergence:** Proving the fundamental lower complexity bound $\Omega(1/k^2)$ for first-order black-box optimization of $L$-smooth convex functions, and proving convergence of Nesterov's 1983 accelerated scheme achieving $\mathcal{O}(L/k^2)$.
5. **ADMM Convergence Proof:** Proving asymptotic objective convergence and residual vanishing for the 2-block alternating direction method of multipliers using Lyapunov energy functions.

#### 2.4 Seminal Graduate-Level Papers
1. **Nesterov, Y. (1983).** *A method for solving the convex programming problem with convergence rate $O(1/k^2)$*. Soviet Mathematics Doklady, 27(2), 372–376.
2. **Boyd, S., Parikh, N., Chu, E., Peleato, B., & Eckstein, J. (2011).** *Distributed Optimization and Statistical Learning via the Alternating Direction Method of Multipliers*. Foundations and Trends in Machine Learning, 3(1), 1–122.
3. **Candès, E. J., Romberg, J., & Tao, T. (2006).** *Robust uncertainty principles: Exact signal reconstruction from highly incomplete frequency information*. IEEE Transactions on Information Theory, 52(2), 489–509.
4. **Duchi, J., Hazan, E., & Singer, Y. (2011).** *Adaptive Subgradient Methods for Online Learning and Stochastic Optimization*. Journal of Machine Learning Research, 12, 2121–2159.

#### 2.5 Authoritative Reference Texts
- Stephen Boyd & Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press.
- R. Tyrrell Rockafellar, *Convex Analysis*, Princeton University Press.
- Neal Parikh & Stephen Boyd, *Proximal Algorithms*, Foundations and Trends in Optimization.
- Sébastien Bubeck, *Convex Optimization: Algorithms and Complexity*, Foundations and Trends in Machine Learning.

---

### 3. Real Analysis, Metric Spaces & General Topology for CS

#### 3.1 Mathematical Core & Conceptual Scope
Moving beyond single-variable real analysis (Abbott) into metric spaces, Cauchy completeness, general topological spaces, compactness (Heine-Borel, Bolzano-Weierstrass, Tychonoff), connected spaces, uniform structures, Function spaces $C(X, Y)$ and $L^p(\mu)$, Banach and Hilbert spaces, contraction mappings, and Scott-continuous domain theory for semantics.

#### 3.2 Curriculum Injection Targets
- **Block 18 (Real Analysis — Year 3 Fall):** Upgrade from basic $\mathbb{R}^1$ analysis to abstract metric spaces and functional analysis.
- **Block 24 (Theory of Computation — Year 4 Fall):** Topological dynamics, Cantor space representations of languages, and undecidability via topology.
- **Track 5 (Programming Languages):** Domain theory, complete partial orders (CPOs), and Scott topology for denotational semantics of recursive programs.

#### 3.3 Required Rigorous Textbook Proofs
1. **Baire Category Theorem:** In a complete metric space $(X, d)$, the intersection of any countable collection of dense open sets is dense in $X$; consequence: $\mathbb{R}$ is uncountable and existence of continuous nowhere-differentiable functions.
2. **Banach Fixed Point Theorem & Picard-Lindelöf Existence:** Contraction mapping principle in Banach spaces, guaranteeing existence and uniqueness of fixed points and solutions to Lipschitz differential equations.
3. **Tychonoff's Theorem:** The product of any collection of compact topological spaces is compact with respect to the product topology (requiring the Axiom of Choice / Zorn's Lemma).
4. **Arzelà-Ascoli Theorem:** Characterization of relatively compact subsets of $C(K)$ (where $K$ is compact) via uniform boundedness and equicontinuity.
5. **Knaster-Tarski Fixpoint Theorem & Kleene's Fixed Point Theorem:** In a complete lattice $L$, every order-preserving map $f: L \to L$ has a complete lattice of fixed points, with least fixed point $\mu f = \bigwedge \{x \in L \mid f(x) \le x\}$; proving equivalence to least fixpoint iteration $\bigvee_{n \ge 0} f^n(\bot)$ in $\omega$-CPOs.

#### 3.4 Seminal Graduate-Level Papers
1. **Scott, D. (1970).** *Outline of a Mathematical Theory of Computation*. Oxford University Computing Laboratory Technical Monograph PRG-2. (Foundational establishment of domain theory).
2. **Smale, S. (1967).** *Differentiable Dynamical Systems*. Bulletin of the American Mathematical Society, 73(6), 747–817.
3. **Vapnik, V. N., & Chervonenkis, A. Y. (1971).** *On the uniform convergence of relative frequencies of events to their probabilities*. Theory of Probability & Its Applications, 16(2), 264–280.
4. **Dudley, R. M. (1967).** *The sizes of compact subsets of Hilbert space and terms of Gaussian processes*. Journal of Functional Analysis, 1(3), 290–330. (Chaining and metric entropy).

#### 3.5 Authoritative Reference Texts
- Walter Rudin, *Principles of Mathematical Analysis*, 3rd ed. (Baby Rudin), McGraw-Hill.
- James Munkres, *Topology*, 2nd ed., Pearson.
- Gerald B. Folland, *Real Analysis: Modern Techniques and Their Applications*, 2nd ed., Wiley.
- Roberto M. Amadio & Pierre-Louis Curien, *Domains and Lambda-Calculi*, Cambridge University Press.

---

### 4. Category Theory, Type Theory & Formal Logic

#### 4.1 Mathematical Core & Conceptual Scope
Functors, natural transformations, adjunctions, monads, Cartesian closed categories (CCCs), topos theory, dependent type theory, Martin-Löf Type Theory (MLTT), Calculus of Inductive Constructions (CIC), Curry-Howard-Lambek correspondence, and Homotopy Type Theory (univalence axiom, higher inductive types).

#### 4.2 Curriculum Injection Targets
- **Block 17 (Software Construction — Year 3 Fall):** Type invariants, parametric polymorphism, algebraic data types, and equational reasoning.
- **Track 5 (Programming Languages & Compilers):** Category-theoretic semantics, monadic effects, dependent typing.
- **Track 10 (Formal Verification — New R3 Track):** Proof assistants (Lean 4, Coq), mechanized foundations.

#### 4.3 Required Rigorous Textbook Proofs
1. **Yoneda Lemma:** For any category $\mathcal{C}$ with locally small hom-sets, the natural transformations $\text{Nat}(\mathcal{C}(A, -), F)$ are in natural bijection with $F(A)$ for any object $A \in \mathcal{C}$ and functor $F: \mathcal{C} \to \mathbf{Set}$.
2. **Curry-Howard-Lambek Isomorphism:** Rigorous bijection between Intuitionistic Propositional Logic (constructive proofs), Simply Typed Lambda Calculus $\lambda^\to$ (terms and normalization), and Cartesian Closed Categories (objects, morphisms, exponential objects).
3. **Strong Normalization for System F via Tait's Reducibility Candidates:** Proving that every well-typed term in polymorphic lambda calculus terminates under $\beta$-reduction; formal proof that type erasure does not induce non-termination.
4. **Church-Rosser Theorem (Confluence of $\beta$-reduction):** Proving the diamond property of parallel reduction ($\implies$) and using the strip lemma to prove confluence of multi-step $\beta$-reduction ($\to_\beta^*$) on untyped $\lambda$-terms.
5. **Gödel's Incompleteness Theorems (Mechanized Formulation):** Formal proof of First Incompleteness (any consistent, effectively generated formal system capable of Robinson arithmetic is incomplete) and Second Incompleteness (cannot prove its own consistency) via Gödel numbering and diagonal lemma.

#### 4.4 Seminal Graduate-Level Papers
1. **Girard, J.-Y. (1972).** *Une extension de l'interprétation de Gödel à l'analyse, et son application à l'élimination des coupures dans l'analyse et la théorie des types*. Doctoral dissertation, Université Paris VII. (Introduction of System F).
2. **Reynolds, J. C. (1974).** *Towards a Theory of Type Structure*. Programming Symposium, Paris, LNCS 19, 408–425.
3. **Moggi, E. (1991).** *Notions of computation and monads*. Information and Computation, 93(1), 55–92. (Unifying semantics of side effects).
4. **Wadler, P. (1989).** *Theorems for free!* FPCA '89: Functional Programming Languages and Computer Architecture, 347–359.
5. **Voevodsky, V. (2014).** *The Univalent Foundations of Mathematics*. Talks and foundational papers on Homotopy Type Theory.

#### 4.5 Authoritative Reference Texts
- Saunders Mac Lane, *Categories for the Working Mathematician*, 2nd ed., Springer GTM.
- Benjamin C. Pierce, *Types and Programming Languages* (TAPL), MIT Press.
- Steve Awodey, *Category Theory*, 2nd ed., Oxford University Press.
- The Univalent Foundations Program, *Homotopy Type Theory: Univalent Foundations of Mathematics*, Institute for Advanced Study.
- Morten Heine Sørensen & Pawel Urzyczyn, *Lectures on the Curry-Howard Isomorphism*, Elsevier.

---

### 5. Abstract Algebra & Number Theory for Cryptography & Coding

#### 5.1 Mathematical Core & Conceptual Scope
Group theory, ring theory, ideal theory, unique factorization domains (UFDs), Euclidean domains, Galois theory, structure of finite fields $\mathbb{F}_{p^k}$, algebraic number fields, geometry of numbers (Minkowski's theorems), elliptic curves over finite fields, pairing-based cryptography (Weil and Tate pairings), and lattice theory (LWE, SIS).

#### 5.2 Curriculum Injection Targets
- **Block 10 (Mathematics for CS — Year 2 Fall):** Modular arithmetic, group axioms, cyclic groups.
- **Track 3 (Security and Cryptography):** Modern asymmetric schemes, post-quantum cryptography, zero-knowledge proofs.
- **Block 27 (Intensive Cryptopals — Year 4 Winter):** Elliptic curve point addition, Pollard's $\rho$, invalid curve attacks, lattice reduction.

#### 5.3 Required Rigorous Textbook Proofs
1. **Structure Theorem for Finitely Generated Abelian Groups & Finite Field Uniqueness:** Proving that any finite abelian group is isomorphic to a direct product of cyclic groups; proving that for any prime $p$ and integer $n \ge 1$, there exists a unique finite field $\mathbb{F}_{p^n}$ up to isomorphism, with cyclic multiplicative group $\mathbb{F}_{p^n}^\times$.
2. **Hasse's Theorem on Elliptic Curves:** Proving that for an elliptic curve $E$ over $\mathbb{F}_q$, the number of $\mathbb{F}_q$-rational points satisfies $| \#E(\mathbb{F}_q) - (q + 1) | \le 2\sqrt{q}$, via the Frobenius endomorphism characteristic polynomial.
3. **Regev's Reduction for Learning With Errors (LWE):** Quantum and classical reductions from worst-case lattice problems ($\text{GapSVP}_{\tilde{\mathcal{O}}(n/\alpha)}$ and $\text{SIVP}$) to the average-case Learning With Errors problem ($\text{LWE}_{n, q, \alpha}$).
4. **Minkowski's Convex Body Theorem:** Proving that any symmetric convex set $S \subset \mathbb{R}^n$ with $\text{vol}(S) > 2^n \det(\Lambda)$ contains at least one non-zero lattice point of $\Lambda$; applying to the Shortest Vector Problem upper bound $\lambda_1(\Lambda) \le \sqrt{n} (\det \Lambda)^{1/n}$.
5. **Weil Pairing Non-Degeneracy and Bilinearity:** Proving that the Weil pairing $e_m: E[m] \times E[m] \to \mu_m$ is bilinear, alternating, and non-degenerate via divisor theory on algebraic curves.

#### 5.4 Seminal Graduate-Level Papers
1. **Diffie, W., & Hellman, M. (1976).** *New Directions in Cryptography*. IEEE Transactions on Information Theory, 22(6), 644–654.
2. **Rivest, R. L., Shamir, A., & Adleman, L. (1978).** *A Method for Obtaining Digital Signatures and Public-Key Cryptosystems*. Communications of the ACM, 21(2), 120–126.
3. **Miller, V. S. (1985).** *Use of Elliptic Curves in Cryptography*. CRYPTO '85, LNCS 218, 417–426.
4. **Regev, O. (2005).** *On lattices, learning with errors and access control*. STOC '05, 84–93. (Foundational establishment of LWE).
5. **Gentry, C. (2009).** *Fully homomorphic encryption using ideal lattices*. STOC '09, 169–178. (First construction of FHE).

#### 5.5 Authoritative Reference Texts
- David S. Dummit & Richard M. Foote, *Abstract Algebra*, 3rd ed., Wiley.
- Kenneth Ireland & Michael Rosen, *A Classical Introduction to Modern Number Theory*, 2nd ed., Springer GTM.
- Joseph H. Silverman, *The Arithmetic of Elliptic Curves*, 2nd ed., Springer GTM.
- Chris Peikert, *A Decade of Lattice Cryptography*, Foundations and Trends in Theoretical Computer Science.

---

### 6. Spectral Graph Theory & Theoretical Computer Science

#### 6.1 Mathematical Core & Conceptual Scope
Algebraic graph theory, adjacency matrices, normalized graph Laplacians, Courant-Fischer min-max theorem, Cheeger's isoperimetric inequality, expander graphs, Ramanujan graphs, random walks on graphs, mixing times, spectral clustering, graph sparsification (Spielman-Srivastava), and modern computational complexity (PCP theorem, hard-core predicates, fine-grained complexity).

#### 6.2 Curriculum Injection Targets
- **Block 13 & 20 (Algorithms I & II — Years 2 & 3):** Spectral graph algorithms, minimum cut approximations, randomized algorithms.
- **Block 24 (Theory of Computation — Year 4 Fall):** Hardness of approximation, interactive proofs, PCP theorem.

#### 6.3 Required Rigorous Textbook Proofs
1. **Cheeger's Inequality:** Proving $\frac{\lambda_2}{2} \le h(G) \le \sqrt{2\lambda_2}$ for the normalized graph Laplacian eigenvalue $\lambda_2$ and Cheeger conductance constant $h(G) = \min_{S \subset V, 0 < |S| \le |V|/2} \frac{|\partial(S)|}{|S|}$, connecting continuous differential geometry to discrete algorithms.
2. **Expander Mixing Lemma:** Proving that for any $d$-regular graph $G$ with second largest absolute eigenvalue $\lambda$, and for any subsets $S, T \subseteq V$, $\left| e(S, T) - \frac{d|S||T|}{n} \right| \le \lambda \sqrt{|S||T| \left(1 - \frac{|S|}{n}\right)\left(1 - \frac{|T|}{n}\right)}$.
3. **Perron-Frobenius Theorem for Non-Negative Matrices:** Proving that an irreducible non-negative matrix $A$ has a unique positive maximal eigenvalue $\rho(A)$ with a strictly positive eigenvector, establishing convergence of PageRank and random walk stationary distributions.
4. **The Cook-Levin Theorem (Full Tableau Reduction):** Rigorous formal reduction of generic polynomial-time non-deterministic Turing machines to 3-CNF Boolean satisfiability formulas by encoding the machine's configuration tape-head tableau.
5. **The PCP Theorem (Dinur's Combinatorial Proof):** Proving that $\text{NP} = \text{PCP}(\mathcal{O}(\log n), \mathcal{O}(1))$ via graph amplification, power graphs, and assignment testers, proving that approximating MAX-3SAT within a factor of $7/8 + \epsilon$ is NP-hard.

#### 6.4 Seminal Graduate-Level Papers
1. **Spielman, D. A., & Teng, S.-H. (2004).** *Nearly-linear time algorithms for graph partitioning, graph sparsification, and solving linear systems*. STOC '04, 81–90. (Gödel Prize).
2. **Batson, J., Spielman, D. A., & Srivastava, N. (2012).** *Twice-Ramanujan Sparsifiers*. SIAM Journal on Computing, 41(6), 1704–1721.
3. **Alon, N. (1986).** *Eigenvalues and expanders*. Theory of Computing Systems (Mathematical Systems Theory), 19(1), 267–287.
4. **Dinur, I. (2007).** *The PCP theorem by gap amplification*. Journal of the ACM, 54(3), Article 12.
5. **Valiant, L. G. (1979).** *The complexity of computing the permanent*. Theoretical Computer Science, 8(2), 189–201.

#### 6.5 Authoritative Reference Texts
- Daniel A. Spielman, *Spectral and Algebraic Graph Theory*, Yale University Lecture Monograph.
- Fan R. K. Chung, *Spectral Graph Theory*, CBMS Regional Conference Series in Mathematics.
- Sanjeev Arora & Boaz Barak, *Computational Complexity: A Modern Approach*, Cambridge University Press.
- Shlomo Hoory, Nathan Linial, & Avi Wigderson, *Expander graphs and their applications*, Bulletin of the AMS, 43(4), 439–561.

---

# Part II: R2 Vertical Expansion — Core EECS Disciplines Depth Injection

Undergraduate curricula frequently teach practical APIs and programming patterns without requiring students to master the seminal breakthrough papers or the mathematical impossibility proofs that define the limits of computing. Below is the graduate injection plan for each core EECS discipline.

---

### 1. Computer Systems, Operating Systems & Distributed Infrastructure

#### 1.1 Injected Seminal PhD-Level Papers
1. **Fischer, M. J., Lynch, N. A., & Paterson, M. S. (1985).** *Impossibility of Distributed Consensus with One Faulty Process* (FLP Impossibility). Journal of the ACM, 32(2), 374–382.
2. **Lamport, L. (1978).** *Time, Clocks, and the Ordering of Events in a Distributed System*. Communications of the ACM, 21(5), 558–565.
3. **Engler, D. R., Kaashoek, M. F., & O'Toole, J. (1995).** *Exokernel: An Architecture for Bug-Free, High-Performance Extensible Operating Systems*. SOSP '95, 251–266.
4. **Clark, D. (1988).** *The Design Philosophy of the DARPA Internet Protocols*. SIGCOMM '88, 102–114.
5. **Liskov, B., & Cowling, J. (2012).** *Viewstamped Replication Revisited*. MIT-CSAIL-TR-2012-008.

#### 1.2 Rigorous Textbook Proofs & Theoretical Invariants
- **FLP Impossibility Theorem Proof:** Mathematical proof by induction on configurations; proving the existence of an initial bivalent configuration, followed by the lemma that a decider event can always be delayed to preserve bivalence, showing that deterministic asynchronous consensus in the presence of even a single unannounced crash failure is impossible.
- **Gilbert & Lynch (2002) Formal Proof of the CAP Theorem:** Proving that in an asynchronous network model where messages may be delayed or lost, no distributed read/write register can simultaneously guarantee strict linearizable consistency and 100% availability.
- **Cache Coherence Verification (Formal Model Checking of MESI/MOESI):** Modeling the protocol as a finite state automaton; establishing safety invariant $\forall a: (\text{State}(c_1, a) = M \implies \forall c_2 \ne c_1: \text{State}(c_2, a) = I)$ and liveness invariant (freedom from deadlock/starvation).
- **Little's Law and Queueing Derivations:** Formal proof that average occupancy $L = \lambda W$ holds under non-preemptive ergodic arrivals; derivation of the Pollaczek-Khinchine formula for $M/G/1$ queues.

#### 1.3 Concrete Syllabus Additions
- Added to **Block 16 (OS)** and **Block 23 (Distributed Systems)**: Complete trace of FLP impossibility, TLA+ formal specification of Raft leader election, and queueing network performance modeling under bursty arrival processes.

---

### 2. Database Systems & Storage Internals

#### 2.1 Injected Seminal PhD-Level Papers
1. **Mohan, C., Haderle, D., Lindsay, B., Pirahesh, H., & Schwarz, P. (1992).** *ARIES: A Transaction Recovery Method Supporting Fine-Granularity Locking and Partial Rollbacks Using Write-Ahead Logging*. ACM TODS, 17(1), 94–162.
2. **Gray, J., Lorie, R., Putzolu, G., & Traiger, I. (1975).** *Granularity of Locks and Degrees of Consistency in a Shared Data Base*. IBM Research Report RJ1654.
3. **O'Neil, P., Cheng, E., Gawlick, D., & O'Neil, E. (1996).** *The Log-Structured Merge-Tree (LSM-tree)*. Acta Informatica, 33(4), 351–385.
4. **Berenson, H., Bernstein, P., Gray, J., Melton, J., O'Neil, E., & O'Neil, P. (1995).** *A Critique of ANSI SQL Isolation Levels*. SIGMOD '95, 1–10.
5. **Corbett, J. C. et al. (2013).** *Spanner: Google's Globally Distributed Database*. ACM TOCS, 31(3), Article 8.

#### 2.2 Rigorous Textbook Proofs & Theoretical Invariants
- **Conflict Serializability Theorem:** Proving that a schedule $S$ is conflict serializable if and only if its serialization precedence graph $\mathcal{P}(S)$ is acyclic.
- **Two-Phase Locking (2PL) Correctness Proof:** Proving by induction on the topological sort of transactions that any schedule produced by strict 2PL yields an acyclic serialization graph.
- **ARIES Physiological Logging Correctness & Idempotence:** Proving that the Analysis, Redo, and Undo passes restore the database to an exact committed state after arbitrary crash points during crash recovery, guaranteed by Compensation Log Records (CLRs) ensuring non-divergence during recurring crashes.
- **TrueTime Uncertainty Bounds & External Consistency:** Proof that Spanner achieves strict serializability (external consistency) across wide-area networks by enforcing the commit wait invariant: wait duration $2\epsilon$ exceeds maximum GPS/atomic clock uncertainty.

#### 2.3 Concrete Syllabus Additions
- Added to **Block 21 (Databases)**: Deep dive into the ARIES paper and implementation of a crash-recovery manager with CLRs and physiological logging in C++; write-skew and phantom read detection formalization.

---

### 3. Theoretical Computer Science & Advanced Algorithms

#### 3.1 Injected Seminal PhD-Level Papers
1. **Tarjan, R. E. (1975).** *Efficiency of a Good But Not Linear Set Union Algorithm*. Journal of the ACM, 22(2), 215–225. (First proof of the inverse Ackermann bound $\alpha(n)$).
2. **Karger, D. R., & Stein, C. (1996).** *A New Approach to the Minimum Cut Problem*. Journal of the ACM, 43(4), 601–640.
3. **Shor, P. W. (1997).** *Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer*. SIAM Journal on Computing, 26(5), 1484–1509.
4. **Hastad, J. (2001).** *Some optimal inapproximability results*. Journal of the ACM, 48(4), 798–859.
5. **Williams, R. (2014).** *Faster All-Pairs Shortest Paths via Circuit Complexity*. STOC '14, 664–673.

#### 3.2 Rigorous Textbook Proofs & Theoretical Invariants
- **Inverse Ackermann Complexity of Disjoint Set Union:** Complete amortized potential function proof showing that Disjoint Set Union with path compression and union-by-rank requires $\mathcal{O}(m \alpha(n))$ time for $m$ operations on $n$ elements.
- **Chernoff-Hoeffding Bounds via Moment Generating Functions:** Derivation of large deviation bounds: $P(\sum X_i - \mu \ge \epsilon \mu) \le \exp(-\frac{\epsilon^2 \mu}{2 + \epsilon})$ using Markov's inequality applied to $e^{\lambda X}$.
- **Approximation Inapproximability Bounds via Hastad's Parity Check:** Proving that finding a $7/8 + \epsilon$ approximation for MAX-3SAT is NP-hard unless $\text{P} = \text{NP}$.
- **Sipser-Lautemann Theorem:** Proving that the bounded-error probabilistic polynomial time complexity class $\text{BPP} \subseteq \Sigma_2^{\text{P}} \cap \Pi_2^{\text{P}}$ in the polynomial hierarchy.

#### 3.3 Concrete Syllabus Additions
- Added to **Block 20 (Algorithms II)** and **Block 24 (Theory of Computation)**: Strict amortized potential proofs, hardness of approximation reductions, and derandomization techniques via conditional expectations.

---

### 4. Programming Languages & Compilers

#### 4.1 Injected Seminal PhD-Level Papers
1. **Milner, R. (1978).** *A Theory of Type Polymorphism in Programming*. Journal of Computer and System Sciences, 17(3), 348–375.
2. **Cousot, P., & Cousot, R. (1977).** *Abstract Interpretation: A Unified Lattice Model for Static Analysis of Programs by Construction or Approximation of Fixpoints*. POPL '77, 238–252.
3. **Cytron, R., Ferrante, J., Rosen, B. K., Wegman, M. N., & Zadeck, F. K. (1991).** *Efficiently Computing Static Single Assignment Form and the Control Dependence Graph*. ACM TOPLAS, 13(4), 451–490.
4. **Chaitin, G. J. (1982).** *Register Allocation & Spilling via Graph Coloring*. SIGPLAN '82, 17(6), 98–101.
5. **Wright, A. K., & Felleisen, M. (1994).** *A Syntactic Approach to Type Soundness*. Information and Computation, 115(1), 38–94.

#### 4.2 Rigorous Textbook Proofs & Theoretical Invariants
- **Wright-Felleisen Syntactic Type Soundness (Progress & Preservation):** Proving that well-typed terms do not get stuck: Progress ($e: \tau \implies e \text{ is a value} \lor \exists e': e \to e'$) and Preservation ($e: \tau \land e \to e' \implies e': \tau$).
- **Soundness & Completeness of Hindley-Milner Algorithm W:** Proving that if $\Gamma \vdash e : \tau$, Algorithm W returns a substitution $\sigma$ and type $\tau'$ such that $\tau = \sigma' \tau'$, and proving that the inferenced type is principal (subsumes all other valid types).
- **Correctness of Abstract Interpretation via Galois Connections:** Proving that the abstract semantics $\alpha(c)$ soundly approximates the concrete collecting semantics: $\alpha(F(c)) \sqsubseteq F^\sharp(\alpha(c))$ and proving convergence to post-fixpoints via widening operators ($\nabla$).
- **Dominance Frontier & Minimal SSA Placement:** Proving that placing $\phi$-nodes at the iterated dominance frontier $IDF(S)$ is both necessary and sufficient for minimal SSA form.

#### 4.3 Concrete Syllabus Additions
- Added to **Block 17 (Software Construction)** and **Track 5 (PL & Compilers)**: Complete formal verification of a small typed language in Coq/Lean, implementing an SSA construction pass with dominance frontiers in an optimizing compiler.

---

### 5. Machine Learning & Deep Generative Foundations

#### 5.1 Injected Seminal PhD-Level Papers
1. **Hornik, K., Stinchcombe, M., & White, H. (1989).** *Multilayer feedforward networks are universal approximators*. Neural Networks, 2(5), 359–366.
2. **Hochreiter, S., & Schmidhuber, J. (1997).** *Long Short-Term Memory*. Neural Computation, 9(8), 1735–1780.
3. **Vaswani, A. et al. (2017).** *Attention Is All You Need*. NeurIPS 2017.
4. **Schulman, J., Wolski, F., Dhariwal, P., Radford, A., & Klimov, O. (2017).** *Proximal Policy Optimization Algorithms*. arXiv:1707.06347.
5. **Chen, R. T. Q., Rubanova, Y., Bettencourt, J., & Duvenaud, D. K. (2018).** *Neural Ordinary Differential Equations*. NeurIPS 2018 (Best Paper Award).

#### 5.2 Rigorous Textbook Proofs & Theoretical Invariants
- **Universal Approximation Theorem:** Proving that single-hidden-layer feedforward networks with continuous non-polynomial activation functions are dense in $C(K)$ for any compact $K \subset \mathbb{R}^n$, using the Stone-Weierstrass theorem and Hahn-Banach representation.
- **Rademacher Complexity and Uniform Generalization Bounds:** Proving that with probability at least $1 - \delta$, $\sup_{h \in \mathcal{H}} |R(h) - \hat{R}(h)| \le 2\mathcal{R}_n(\mathcal{H}) + \sqrt{\frac{\ln(2/\delta)}{2n}}$ through McDiarmid's bounded differences inequality.
- **Policy Gradient Theorem Derivation:** Rigorous derivation of $\nabla_\theta J(\pi_\theta) = \mathbb{E}_{\tau \sim \pi_\theta} \left[ \sum_{t=0}^T \nabla_\theta \log \pi_\theta(a_t|s_t) Q^{\pi_\theta}(s_t, a_t) \right]$ using the log-derivative trick and Markov chain transition kernel perturbation.
- **Adjoint Sensitivity Method for Neural ODEs:** Proving that the gradient of a scalar loss with respect to continuous dynamics parameters $\frac{dz}{dt} = f(z(t), t, \theta)$ can be computed by solving an augmented ODE backwards in time without storing intermediate activation graphs: $\frac{da(t)}{dt} = -a(t)^T \frac{\partial f(z(t), t, \theta)}{\partial z}$.

#### 5.3 Concrete Syllabus Additions
- Added to **Track 1 (AI & Machine Learning)**: Proof of universal approximation, implementation of Neural ODEs with custom adjoint backward pass, and derivation of the ELBO bound for variational autoencoders and diffusion SDEs.

---

### 6. Security, Cryptography & Network Security

#### 6.1 Injected Seminal PhD-Level Papers
1. **Goldwasser, S., & Micali, S. (1984).** *Probabilistic Encryption*. Journal of Computer and System Sciences, 28(2), 270–299.
2. **Bellare, M., & Rogaway, P. (1993).** *Random Oracles are Practical: A Paradigm for Designing Efficient Protocols*. CCS '93, 62–73.
3. **Canetti, R. (2001).** *Universally Composable Security: A New Paradigm for Cryptographic Protocols*. FOCS '01, 136–145.
4. **Shamir, A. (1979).** *How to Share a Secret*. Communications of the ACM, 22(11), 612–613.
5. **Ben-Sasson, E., Chiesa, A., Tromer, E., & Virza, M. (2014).** *Succinct Non-Interactive Zero Knowledge for a von Neumann Architecture* (zk-SNARKs). USENIX Security '14.

#### 6.2 Rigorous Textbook Proofs & Theoretical Invariants
- **Equivalence of Semantic Security and IND-CPA:** Formal game-hopping proof showing that an encryption scheme is semantically secure if and only if it is indistinguishable under chosen-plaintext attack (IND-CPA).
- **Security Reduction of RSA-FDH (Full Domain Hash):** Rigorous reduction proving that under the RSA assumption in the Random Oracle Model, an adversary that can forge an RSA-FDH signature can be converted into an algorithm that inverts RSA permutations.
- **Soundness, Completeness, and Zero-Knowledge of Schnorr Identification Protocol:** Constructing the probabilistic polynomial-time simulator $S$ producing indistinguishable transcripts without knowing the secret key, and constructing the knowledge extractor obtaining the secret key from two accepting transcripts with distinct challenges (special soundness).
- **Encrypt-then-MAC IND-CCA2 Theorem:** Proving that if an encryption scheme is IND-CPA secure and the MAC is strongly unforgeable (SUF-CMA), the Encrypt-then-MAC (EtM) composition is provably IND-CCA2 secure.

#### 6.3 Concrete Syllabus Additions
- Added to **Track 3 (Security & Cryptography)** and **Block 27 (Intensive Cryptopals)**: Formal game-hopping security reductions, implementation and cryptanalysis of zero-knowledge pairing-based SNARKs, and side-channel timing attack mitigations.

---

# Part III: R3 Horizontal Expansion — Modern Paradigm Specialization Tracks

Six new specialization tracks are designed to integrate cutting-edge disciplines not covered by traditional curricula. Each track follows the established two-course + substantial build deliverable structure of The Noblett Repository.

---

## Track 7: TinyML & Edge Artificial Intelligence

### Overview & Motivation
Standard deep learning focuses on hyperscale data centers with gigawatt power budgets. TinyML is the engineering science of executing machine learning inference and real-time on-device training on microcontrollers (ARM Cortex-M, RISC-V RV32IMAC), DSPs, and edge NPUs under extreme energy constraints (< 1 mW), memory ceilings (< 256 KB SRAM, < 1 MB Flash), and hard real-time latency budgets.

### Prerequisites
- Block 06 (C Fluency), Block 09 (Computer Systems), Block 14 (Computer Architecture), Track 1 (AI/ML Course 1).

### Learning Outcomes
1. **Mathematical Quantization:** Master symmetric and asymmetric integer quantization (INT8, INT4, FP4), per-tensor and per-channel scaling factor derivations, and zero-point calibration.
2. **Sparsification & Pruning:** Apply structured and unstructured weight pruning, lottery ticket hypothesis, and second-order Taylor expansion pruning (Optimal Brain Surgeon).
3. **Hardware-Aware Neural Architecture Search (NAS):** Formulate multi-objective optimization algorithms maximizing accuracy while constraining peak SRAM and FLOPs.
4. **Bare-Metal Inference Engine Development:** Write bare-metal C/assembly kernels for 2D convolutions, depthwise separable convolutions, matrix multiplications, and attention blocks without dynamic memory allocation (`malloc`).
5. **Energy & Thermal Profiling:** Interface physical current measurement hardware (e.g. Nordic Power Profiler Kit II) to quantify microjoules-per-inference and power-state transitions.
6. **On-Device Continual Learning:** Implement quantized memory-efficient transfer learning (TinyTL) and streaming anomaly detection on resource-constrained microcontrollers.

### Modular Syllabus Structure

#### Course 1: Foundations of Efficient Deep Learning (MIT 6.5940 Equivalent)
- **Module 1: Numeric Formats & Post-Training Quantization (PTQ):**
  FP32 vs FP16 vs BF16 vs INT8 vs INT4; affine quantization equations: $q = \text{round}(r/S) + Z$; quantization of weights, biases, and activations; KL-divergence calibration; overflow avoidance.
- **Module 2: Quantization-Aware Training (QAT):**
  Straight-Through Estimator (STE); fake-quantization operators; learned step-size quantization (LSQ); weight rounding optimization (AdaRound).
- **Module 3: Pruning & Compression:**
  Magnitude pruning, iterative pruning; unstructured vs structured (block, channel) pruning; Huffman coding and compressed sparse row (CSR) representations.
- **Module 4: Compact Network Architectures:**
  MobileNet (v1, v2, v3) inverted residuals; ShuffleNet channel shuffle; SqueezeNet; EfficientNet compound scaling; depthwise separable convolution speedup derivations.
- **Module 5: Hardware-Aware NAS & Once-for-All (OFA):**
  Decoupling training and search; supernet training; evolutionary search algorithms subject to edge latency look-up tables (LUT).

#### Course 2: Embedded Edge Systems & Microcontroller Deployment
- **Module 1: Microcontroller Architectures & Memory Hierarchy:**
  ARM Cortex-M4/M7/M55/M85 architectures; CMSIS-NN SIMD vector instructions; tightly-coupled memory (TCM), SRAM banks, cache misses, Flash wait states.
- **Module 2: Memory-Constrained Runtime Scheduling:**
  Tensor memory arena allocation; peak memory lifetime analysis; in-place activation reuse; operator fusion (Conv + BatchNorm + ReLU).
- **Module 3: Edge NPUs & Hardware Accelerators:**
  Google Coral Edge TPU, Arm Ethos-U55 microNPU; fixed-point systolic arrays; weight stationary vs output stationary dataflows.
- **Module 4: Low-Power Sensors & Interfacing:**
  I2C, SPI, PDM microphones, camera interfaces (DVP); direct memory access (DMA) double-buffering for zero-CPU-overhead continuous sensor streaming.
- **Module 5: On-Device Continual Learning & Streaming Inference:**
  Memory-efficient partial backpropagation; episodic memory replay on MCU; tiny anomaly detection with autoencoders on industrial vibration sensor streams.

### Seminal Graduate-Level Papers & Textbooks
1. **Han, S., Mao, H., & Dally, W. J. (2016).** *Deep Compression: Compressing Deep Neural Networks with Pruning, Trained Quantization and Huffman Coding*. ICLR 2016 (Best Paper Award).
2. **Jacob, B. et al. (2018).** *Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference*. CVPR 2018.
3. **Lin, J., Chen, W.-M., Cai, H., & Han, S. (2020).** *MCUNet: Tiny Deep Learning on IoT Devices*. NeurIPS 2020.
4. **Frankle, J., & Carbin, M. (2019).** *The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks*. ICLR 2019 (Best Paper Award).
5. **Textbook:** Pete Warden & Daniel Situnayake, *TinyML: Machine Learning with TensorFlow Lite on Arduino and Ultra-Low-Power Microcontrollers*, O'Reilly.
6. **Textbook:** Song Han & William J. Dally, *Efficient Deep Learning: Algorithms and Systems*, MIT Press (forthcoming / course notes).

### Hands-On Lab Specifications & Track Build Deliverable
- **Lab 1: Fixed-Point Arithmetic & Quantization Kernel:**
  Implement an INT8 convolution operator in pure C99 with manual fixed-point accumulator shift ($S_{\text{mult}} = S_1 S_2 / S_3$). Prove bit-exact equivalence to PyTorch quantized inference on a 10-layer CNN.
- **Lab 2: CMSIS-NN Vectorized Acceleration:**
  Rewrite the convolution kernel using ARM Cortex-M DSP assembly/intrinsics (`__SMLAD`, `__QADD8`). Benchmark cycle count against naive C on an STM32F4 / RP2040 using DWT cycle counter; achieve $\ge 4\times$ speedup.
- **Lab 3: Zero-Allocation Tensor Runtime Arena:**
  Build a static C memory scheduler that parses a quantized FlatBuffer/ONNX model graph, builds a lifetime graph of activation tensors, and computes the optimal memory layout fitting into a 128 KB SRAM arena without fragmentation.
- **🏁 Capstone Track Build Deliverable:**
  **An Autonomous, Real-Time Keyword Spotting & Vision Anomaly Detection System on Bare-Metal Microcontroller.**
  - Target hardware: ARM Cortex-M4/M7 (e.g. STM32H7 or Raspberry Pi Pico 2 RISC-V).
  - Model: A MobileNetV2-based 8-bit quantized visual wake-word classifier (< 250 KB Flash, < 80 KB RAM).
  - Pipeline: Real-time camera capture via DMA, zero-copy buffer handoff, bare-metal inference execution, and LED/GPIO actuation.
  - Verification: Complete inference must run in $< 100 \text{ ms}$ at $< 50 \text{ mW}$ average power, verified via oscilloscope or current profiler, passing 500 consecutive test images with zero memory corruption.

---

## Track 8: Rust for High-Assurance Systems Engineering

### Overview & Motivation
C and C++ have powered systems engineering for 50 years, but 70% of high-severity CVEs in critical infrastructure stem from memory safety violations (use-after-free, buffer overflows, data races). Rust provides compile-time memory safety without a garbage collector through affine type theory, ownership, and lifetime semantics. This track covers the systems engineering science of building verifiable, crash-resilient kernels, async runtimes, and lock-free data structures in Rust.

### Prerequisites
- Block 06 (C Fluency), Block 09 (Computer Systems), Block 16 (Operating Systems), Block 17 (Software Construction).

### Learning Outcomes
1. **Linear & Affine Type Semantics:** Mathematically model the Rust borrow checker as an substructural type system; rigorously prove safety of shared references (`&T` as immutable/aliased) versus mutable references (`&mut T` as unique/non-aliased).
2. **Unsafe Rust Invariant Auditing:** Write and formally audit `unsafe` blocks; implement custom data structures with raw pointers (`*const T`, `*mut T`, `NonNull<T>`) while upholding non-aliasing and initialization invariants verified by Miri.
3. **Lock-Free Concurrency & Memory Models:** Implement atomic operations under the C++20 / Rust memory model (SeqCst, Acquire-Release, Relaxed); construct ABA-immune lock-free data structures.
4. **Bare-Metal Kernel Architecture:** Develop a freestanding `no_std` operating system kernel on x86-64 or RISC-V with virtual memory paging, interrupt handling, and cooperative/preemptive multitasking.
5. **Async Runtime Mechanics:** Design an asynchronous runtime from scratch, implementing `Future`, `Waker`, reactor-executor patterns, and lock-free work-stealing schedulers.
6. **Formal Verification of Rust:** Apply modern deductive verification engines (Kani Rust Model Checker, Creusot, Prusti) to mathematically prove safety contracts and functional correctness of unsafe systems code.

### Modular Syllabus Structure

#### Course 1: Advanced Rust Systems & Memory Safety Internals
- **Module 1: The Rust Type System & Lifetime Mechanics:**
  Affine types, move semantics, subtyping, and variance (covariance, contravariance, invariance in generic parameters and raw pointers); higher-ranked trait bounds (HRTBs, `for<'a>`); phantom data.
- **Module 2: Deep Unsafe Rust & Pointer Invariants:**
  Undefined Behavior (UB) boundaries in Rust; stacked borrows and tree borrows operational models; interior mutability (`UnsafeCell<T>`); pointer provenance; running and passing Miri test suites.
- **Module 3: Advanced Trait Engineering & Metaprogramming:**
  Trait resolution algorithms; associated types vs generics; dynamic dispatch and vtable layout; procedural macros (custom derives, attribute-like, function-like) via AST manipulation with `syn` and `quote`.
- **Module 4: High-Performance Allocators & Memory Management:**
  Custom allocators with `std::alloc::Allocator`; slab, arena, and bump allocators; zero-copy parsing with `zerocopy` and `nom`.
- **Module 5: FFI & Cross-Language Boundary Hardening:**
  C-ABI compatibility; `extern "C"`; sound memory ownership transfers across FFI boundaries; panic propagation safety; bindgen and cbindgen automation.

#### Course 2: Asynchronous Runtimes, Kernels & Formal Rust Verification
- **Module 1: Async/Await Mechanics & State Machine Generation:**
  The `Future` trait; poll-based state machine compilation; pinned memory (`Pin<&mut T>`) and self-referential structs; structural pinning invariants.
- **Module 2: Building an Async Executor from Scratch:**
  Event loop mechanics with `epoll` / `kqueue` / `io_uring`; task waking via `Arc<Wake>`; lock-free Chase-Lev work-stealing deque implementation.
- **Module 3: Bare-Metal `no_std` Kernel Development:**
  Target specifications, linker scripts, bootloader handoff; GDT, IDT, page table manipulation, physical page frame allocator; preemptive context switching.
- **Module 4: Hardware Driver Development & Device Trees:**
  Memory-mapped I/O (MMIO) with volatile access; safe register abstractions with type-state patterns; UART, VirtIO block devices, and timer drivers.
- **Module 5: Formal Verification of Rust Code:**
  SAT/SMT-based model checking with Kani; unbounded verification of unsafe blocks; deductive functional verification using Creusot / Why3.

### Seminal Graduate-Level Papers & Textbooks
1. **Jung, R., Jourdan, J.-H., Krebbers, R., & Dreyer, D. (2017).** *RustBelt: Securing the Foundations of the Rust Programming Language*. POPL 2018 (ACM SIGPLAN Distinguished Paper).
2. **Jung, R., Dang, H.-H., Kang, J., & Dreyer, D. (2020).** *Stacked Borrows: An Operational Model for Rust's Pointer Tracking*. POPL 2020.
3. **Levy, A. et al. (2017).** *Multiprogramming a 64kB Computer Safely and Efficiently* (Tock OS). SOSP '17.
4. **Denis, X., Jourdan, J.-H., & Marché, C. (2022).** *Creusot: a Foundry for the Deductive Verification of Rust Programs*. ICFEM 2022.
5. **Textbook:** Jon Gjengset, *Rust for Rustaceans: Idiomatic Programming for Experienced Developers*, No Starch Press.
6. **Textbook:** Philipp Oppermann, *Writing an OS in Rust* (online comprehensive monograph).

### Hands-On Lab Specifications & Track Build Deliverable
- **Lab 1: Sound Lock-Free Queue Verified by Miri:**
  Implement the Michael-Scott lock-free queue in Rust using atomic pointers and `UnsafeCell`. Pass full test suite under `cargo miri test` with no UB, no memory leaks, and verification under `loom` for all thread interleavings.
- **Lab 2: Mini-Tokio Async Runtime with `io_uring`:**
  Build a complete asynchronous executor and reactor using Linux `io_uring`. Implement `Waker`, thread-pool work-stealing, and asynchronous TCP socket primitives. Benchmark against Tokio; achieve within 20% throughput.
- **Lab 3: Deductive Verification with Kani/Creusot:**
  Take an unsafe implementation of an intrusive circular doubly-linked list. Specify memory safety invariants and functional contracts; verify using the Kani model checker across all symbolic inputs up to bound $k=32$.
- **🏁 Capstone Track Build Deliverable:**
  **A Bootable, Multi-Core `no_std` Microkernel with Verified Device Drivers in Rust.**
  - Target: Bare-metal x86-64 or RISC-V (QEMU virt).
  - Features: Multi-level page table management, heap allocator, preemptive round-robin scheduler, user-space separation (Ring 3), and VirtIO block device driver.
  - Assurance: Zero compiler warnings under `clippy --pedantic`; core unsafe synchronization primitives formally verified via Kani; passes continuous integration stress-testing running 10,000 process context switches without panic or leakage.

---

## Track 9: Hardware-in-the-Loop (HIL) Virtualization & Cyber-Physical Systems

### Overview & Motivation
Cyber-physical systems (autonomous vehicles, avionics, industrial robotics, power grids) operate where software errors cause physical destruction. Developing and certifying these systems requires deterministic Hardware-in-the-Loop (HIL) virtualization: orchestrating real embedded hardware controllers in closed-loop simulation with mathematically rigorous digital twins of physical plants, emulated sensor buses (CAN, LIN, ARINC 429, Ethernet-TSN), and fault injection engines running under microsecond hard real-time guarantees.

### Prerequisites
- Block 08 (Physics II), Block 09 (Computer Systems), Block 14 (Computer Architecture), Block 16 (Operating Systems), Track 6 (Computer Engineering).

### Learning Outcomes
1. **Cyber-Physical Plant Modeling:** Formulate continuous-time state-space ordinary differential equations (ODEs) and discrete-time hybrid automata for physical systems (e.g., flight dynamics, brushless DC motors).
2. **Deterministic Hard Real-Time Execution:** Master Linux PREEMPT_RT, Xenomai, and real-time hypervisors; eliminate jitter, page faults, and cache contention to achieve $< 10 \, \mu\text{s}$ worst-case execution time (WCET).
3. **Full-System Emulator Co-Simulation:** Configure and extend QEMU and Renode to emulate multi-core embedded SoC targets with cycle-accurate peripheral models synchronized to physical plant models via lockstep time synchronization.
4. **Automotive & Avionics Industrial Protocols:** Decode, transmit, and bridge CAN-FD, FlexRay, ARINC 429, and Time-Sensitive Networking (IEEE 802.1Qbv TSN) frames with deterministic schedule enforcement.
5. **Systematic Fault Injection & Fuzzing:** Build physical and simulated fault injection harnesses (corrupted clock signals, short-circuited buses, bit-flips, sensor drift) to validate system resilience against ISO 26262 / DO-178C functional safety requirements.
6. **Formal Hybrid System Verification:** Specify and verify safety envelopes using reachability analysis tools (SpaceEx, dReach) to prove that the cyber-physical state never enters an unsafe region.

### Modular Syllabus Structure

#### Course 1: Real-Time Systems, Hypervisors & Plant Modeling
- **Module 1: Real-Time Scheduling Theory & Analysis:**
  Rate-Monotonic Scheduling (RMS), Earliest Deadline First (EDF); Response Time Analysis (RTA); Priority Inversion, Priority Inheritance, and Priority Ceiling Protocols (PCP).
- **Module 2: Hard Real-Time OS Architecture:**
  Linux PREEMPT_RT patch internals; high-resolution timers (`hrtimer`), interrupt threadification, memory locking (`mlockall`), CPU isolation (`isolcpus`), cache coloring with CAT (Cache Allocation Technology).
- **Module 3: Continuous & Hybrid Dynamical Systems:**
  State-space representation: $\dot{x}(t) = Ax(t) + Bu(t), y(t) = Cx(t) + Du(t)$; Runge-Kutta numerical integration (RK4) for real-time simulation; hybrid automata transitions.
- **Module 4: Real-Time Hypervisors & Virtualization:**
  Type-1 embedded hypervisors (Xen, Jailhouse, ACRN); hardware-assisted virtualization (ARM TrustZone, Intel VT-x); static resource partitioning without overcommit.
- **Module 5: Industrial Bus Protocols & Deterministic Ethernet:**
  CAN 2.0B / CAN-FD arbitration mechanics, bit stuffing, CRC calculation; Time-Sensitive Networking (TSN) credit-based and time-aware shapers (802.1Qbv).

#### Course 2: Hardware-in-the-Loop Testbeds, Emulation & Fault Injection
- **Module 1: Co-Simulation Architecture & Time Synchronization:**
  Master-slave co-simulation; Functional Mock-up Interface (FMI) standards (FMU-ME, FMU-CS); lockstep time coordination between virtual time and wall-clock time.
- **Module 2: Peripheral Emulation in QEMU & Renode:**
  Writing custom hardware peripheral models in C and Python; memory-mapped register handling, interrupt generation, DMA simulation.
- **Module 3: Physical Interface Bridging (Hardware-in-the-Loop):**
  FPGA-based high-speed digital I/O; digital-to-analog (DAC) and analog-to-digital (ADC) interfaces; level shifters, optoisolators, CAN transceivers.
- **Module 4: Automated Fault Injection & Safety Certification:**
  Hardware fault injection (glitching, brownouts); software fault injection (SIMD register bit flips, frame dropping); ISO 26262 ASIL-D and DO-178C DAL-A safety cases.
- **Module 5: Reachability Analysis & Safety Envelopes:**
  Zonotopes, support functions, and interval arithmetic; computing forward reachable sets of cyber-physical systems; proving collision avoidance.

### Seminal Graduate-Level Papers & Textbooks
1. **Sha, L., Rajkumar, R., & Lehoczky, J. P. (1990).** *Priority Inheritance Protocols: An Approach to Designing High-Performance Real-Time Systems*. IEEE Transactions on Computers, 39(9), 1175–1185.
2. **Alur, R., Courcoubetis, C., Henzinger, T. A., & Ho, P.-H. (1993).** *Hybrid Automata: An Algorithmic Approach to the Specification and Verification of Hybrid Systems*. Hybrid Systems, LNCS 736, 209–229.
3. **Cucinotta, T. et al. (2009).** *Real-Time Virtualization on Multi-Core Architectures*. IEEE Transactions on Industrial Informatics.
4. **Textbook:** Edward A. Lee & Sanjit A. Seshia, *Introduction to Embedded Systems: A Cyber-Physical Systems Approach*, 2nd ed., MIT Press.
5. **Textbook:** Giorgio C. Buttazzo, *Hard Real-Time Computing Systems: Predictable Scheduling Algorithms and Applications*, 3rd ed., Springer.
6. **Textbook:** Rajeev Alur, *Principles of Cyber-Physical Systems*, MIT Press.

### Hands-On Lab Specifications & Track Build Deliverable
- **Lab 1: PREEMPT_RT Worst-Case Jitter Benchmarking:**
  Configure and flash a PREEMPT_RT Linux kernel on an embedded single-board computer (Raspberry Pi CM4 or BeagleBone Black). Write a cyclictest harness; eliminate all latency spikes exceeding $15 \, \mu\text{s}$ across 24 hours under 100% stress-ng load.
- **Lab 2: Custom CAN-FD Peripheral in Renode:**
  Write an emulated CAN-FD controller in C# for the Renode simulation platform. Run compiled Zephyr RTOS firmware in Renode; verify that messages are accurately transmitted, filtered, and timestamped matching physical bus logic analyzer captures.
- **Lab 3: SpaceEx Reachability Analysis of Inverted Pendulum:**
  Construct a hybrid automaton model of an inverted pendulum on a cart controlled via a sampled-data digital controller with network latency. Compute reachable state tubes using SpaceEx; prove mathematically that the cart never exceeds track boundaries for all initial perturbations in $[-0.2, 0.2] \text{ rad}$.
- **🏁 Capstone Track Build Deliverable:**
  **A Complete Hardware-in-the-Loop (HIL) Testbed for an Autonomous Drone Flight Controller.**
  - Setup: Real physical microcontroller (STM32F7 / Pixhawk) running real-time flight firmware connected over physical SPI/I2C/CAN buses to a Linux PREEMPT_RT host running a real-time 6-DOF aerodynamic physics simulator.
  - Operation: The simulator computes vehicle state at $1 \, \text{kHz}$, synthesizes simulated IMU (gyro/accel), barometer, and GPS sensor signals, transmits them over physical GPIO/buses into the MCU, reads back PWM actuator commands, and updates flight dynamics in closed loop.
  - Acceptance Test: The HIL system must execute a 10-minute automated autonomous waypoint flight mission with zero packet drops, jitter $< 20 \, \mu\text{s}$, and successfully recover from simulated physical motor failure and sensor freeze fault injections within $200 \text{ ms}$.

---

## Track 10: Formal Methods & Mechanized Verification (Lean 4 & Coq)

### Overview & Motivation
Testing can prove the presence of bugs, but never their absence (Dijkstra). In mission-critical software, operating system kernels, cryptographic primitives, and pure mathematics, formal verification provides machine-checked mathematical proof that code conforms to its formal specification across all possible inputs. Lean 4 and Coq (Rocq) are the premier proof assistants powering modern breakthroughs in verified computing (seL4 microkernel, CompCert C compiler) and mechanized mathematics (Liquid Tensor Experiment).

### Prerequisites
- Block 05 (SICP), Block 10 (Math for CS), Block 17 (Software Construction), Block 18 (Real Analysis), Track 5 (PL & Compilers).

### Learning Outcomes
1. **Constructive Logic & Proof Theory:** Master natural deduction, the sequent calculus, constructive propositional and first-order logic, and inductive datatypes under the Calculus of Inductive Constructions (CIC).
2. **Interactive Proof Assistant Fluency:** Attain fluency in writing tactics, custom automation macros, and dependent type definitions in both Lean 4 and Coq/Rocq.
3. **Mechanized Operational Semantics:** Define small-step and big-step operational semantics, define evaluation relations, and prove syntactic type soundness (progress and preservation) in Lean 4.
4. **Compiler Verification (CompCert Paradigm):** Formulate compiler simulation conventions (forward and backward simulations); verify correctness of optimization passes (dead code elimination, constant folding).
5. **Interactive Software Verification:** Prove functional correctness of non-trivial algorithms (sorting, red-black trees, cryptographic hashing) against abstract algebraic specifications.
6. **SMT Solver Integration & Auto-Active Verification:** Combine interactive theorem provers with automated SMT solvers (Z3, CVC5) through SMT-lib and tactics to automate tedious proof obligations.

### Modular Syllabus Structure

#### Course 1: Proof Theory, Inductive Types & Mechanized Logic in Lean 4
- **Module 1: Functional Programming & Dependent Types in Lean 4:**
  Pure functional programming in Lean 4; dependent functions ($\Pi$-types), dependent pairs ($\Sigma$-types); universe levels; the Lean 4 metaprogramming framework and elaboration.
- **Module 2: Propositions as Types & Interactive Tactics:**
  Constructive vs classical logic; proving tautologies using `intro`, `apply`, `exact`, `cases`, `induction`, `constructor`; proofs by contradiction and excluded middle in classical mode.
- **Module 3: Inductive Types & Well-Founded Recursion:**
  Defining natural numbers, lists, trees, and custom inductive predicates; mutual induction, induction-recursion; termination proofs via well-founded relations and measures.
- **Module 4: Algebraic Structures & Typeclasses:**
  Monoids, groups, rings, lattices; typeclass resolution mechanisms; quotient types and equivalence relations; formalizing fundamental mathematical proofs.
- **Module 5: Metaprogramming & Custom Tactic Development:**
  The `MetaM` and `TacticM` monads; manipulating expressions (`Expr`); writing automated tactics that inspect local hypotheses and discharge arithmetic or equality goals.

#### Course 2: Certified Software, Compilers & Systems Verification
- **Module 1: Mechanizing Language Syntax & Operational Semantics:**
  Abstract syntax trees (ASTs); small-step structural operational semantics ($\to$); big-step evaluation ($\Downarrow$); proving equivalence between semantics.
- **Module 2: Type Systems & Mechanized Type Soundness:**
  Simply Typed Lambda Calculus ($\lambda^\to$) in Lean/Coq; typing context representations (de Bruijn indices vs nominal variables); machine-checked proofs of Progress and Preservation.
- **Module 3: Program Logics & Hoare Logic:**
  Axiomatic semantics; pre-conditions, post-conditions, and loop invariants; proving Hoare triples $\{P\} c \{Q\}$; weakest precondition calculus ($wp$) and verification condition generation (VCG).
- **Module 4: Verified Compilation & Simulation Relations:**
  Target assembly languages; compiler correctness theorem formulation: $\text{Compile}(S) = T \implies \forall B: S \Downarrow B \iff T \Downarrow B$; forward simulation with step-indexing.
- **Module 5: Microkernel & Separation Logic Verification:**
  Pointers, mutable heap memories; concurrent separation logic (CSL); framing rule; case studies of seL4 (Isabelle/HOL) and CertiKOS (Coq).

### Seminal Graduate-Level Papers & Textbooks
1. **Leroy, X. (2009).** *Formal verification of a realistic compiler*. Communications of the ACM, 52(7), 107–115. (CompCert).
2. **Klein, G. et al. (2009).** *seL4: Formal verification of an OS kernel*. SOSP '09, 207–220. (First formally verified operating system microkernel).
3. **Moura, L. de, & Ullrich, S. (2021).** *The Lean 4 Theorem Prover and Programming Language*. CADE '21, 625–635.
4. **Chlipala, A. (2013).** *Certified Programming with Dependent Types*. MIT Press (free online).
5. **Textbook:** Benjamin C. Pierce et al., *Software Foundations* (5 volumes: Logical Foundations, Programming Language Foundations, Verified Functional Algorithms, QuickChick, Separation Logic Foundations), University of Pennsylvania.
6. **Textbook:** Jeremy Avigad, Leonardo de Moura, Soonho Kong, *Theorem Proving in Lean 4*, Lean Community Monograph.

### Hands-On Lab Specifications & Track Build Deliverable
- **Lab 1: Complete Mechanized Logic & Arithmetic in Lean 4:**
  Formalize Peano arithmetic from first principles in Lean 4. Prove commutativity, associativity, and distributivity of multiplication, and prove the infinitude of primes without using standard library shortcuts (`sorry`).
- **Lab 2: Verified Red-Black Tree in Coq:**
  Implement persistent Red-Black Trees in Coq. Specify the Binary Search Tree invariant and the Red-Black height balance invariant as dependent inductive types. Mechanically prove that insertion preserves all invariants and that lookup is sound and complete.
- **Lab 3: Verified Mini-Compiler with Simulation Proof:**
  Define the source language `Imp` (while-loops, conditionals, mutable variables) and a stack-machine target bytecode language in Lean 4. Write an optimizing compiler pass (constant folding + dead code elimination); prove a forward simulation theorem showing semantic preservation for all terminating and non-terminating executions.
- **🏁 Capstone Track Build Deliverable:**
  **A Formally Verified Cryptographic Library or Bytecode Virtual Machine in Lean 4.**
  - Specification: Implement a complete cryptographic algorithm (e.g., ChaCha20 or SHA-256) or a stack-based bytecode VM.
  - Formal Claims: Mechanically prove functional equivalence against the authoritative reference specification (RFC 7539 / RFC 6234).
  - Safety Claims: Mechanically prove total memory safety, absence of integer overflow, termination, and constant-time execution properties (absence of secret-dependent branching).
  - Delivery: Clean Lean 4 codebase with 0 `sorry` statements, building deterministically under `lake build`, verified by independent CI proof check.

---

## Track 11: Quantum Information Science & Quantum Computing

### Overview & Motivation
Quantum computation leverages the physical principles of superposition, quantum entanglement, and interference to solve specific mathematical problems exponentially faster than any classical Turing machine (factoring via Shor's algorithm, quantum chemical simulation). This track provides a rigorous, linear-algebraic and physical foundation for quantum information, quantum circuit synthesis, quantum algorithms, quantum error correction (surface codes), and practical circuit compilation on NISQ and fault-tolerant architectures.

### Prerequisites
- Block 08 (Physics II), Block 11 (Linear Algebra / Axler), Block 15 (Probability), Block 24 (Theory of Computation).

### Learning Outcomes
1. **Quantum State Formalism & Postulates:** Master state vectors in Hilbert space $\mathcal{H}$, density operators $\rho$, pure versus mixed states, partial trace, von Neumann entropy, and projective vs POVM measurements.
2. **Quantum Circuit Synthesis & Universality:** Prove universality of gate sets (e.g. Clifford + $T$, Solovay-Kitaev theorem); synthesize multi-qubit unitary operators using CNOT, Hadamard, and Phase gates.
3. **Core Quantum Algorithms:** Implement, trace, and analyze asymptotic speedups of the Deutsch-Jozsa algorithm, Bernstein-Vazirani, Simon's algorithm, Quantum Phase Estimation (QPE), Shor's factoring algorithm, and Grover's search algorithm.
4. **Quantum Noise & Open Quantum Systems:** Model decoherence (dephasing, amplitude damping, depolarizing channels) via Kraus operator representations and Lindblad master equations.
5. **Quantum Error Correction & Fault Tolerance:** Construct stabilizer codes (CSS codes, Steane 7-qubit code, Shor 9-qubit code); analyze the 2D surface code, syndrome decoding with minimum-weight perfect matching (MWPM), and the threshold theorem.
6. **Quantum Programming Fluency:** Program, simulate, and compile quantum algorithms targeting real superconducting / trapped-ion quantum processors using Qiskit, Cirq, and Pennylane.

### Modular Syllabus Structure

#### Course 1: Foundations of Quantum Information & Algorithms
- **Module 1: Quantum Mechanics in Finite Dimensions:**
  Hilbert spaces, inner products, bra-ket notation; tensor products; unitary operators, Hermitian observables, spectral decomposition; the four postulates of quantum mechanics.
- **Module 2: Qubits, Multi-Qubit Systems & Entanglement:**
  Bloch sphere geometry; Bell states; entanglement measures (concurrence, entanglement of formation); no-cloning theorem; quantum teleportation and superdense coding protocols.
- **Module 3: Quantum Circuit Model & Universality:**
  Single-qubit rotations ($R_x, R_y, R_z$); CNOT, Toffoli, Fredkin gates; universality proofs; the Solovay-Kitaev theorem for efficient gate compilation.
- **Module 4: Quantum Fourier Transform & Phase Estimation:**
  Discrete Fourier transform vs QFT; circuit implementation of QFT with $\mathcal{O}(n^2)$ gates; Quantum Phase Estimation (QPE) precision analysis.
- **Module 5: Seminal Algorithms (Shor & Grover):**
  Period finding via QPE; order-finding reduction to integer factorization (Shor); amplitude amplification, geometric visualization, and optimality of Grover's $\mathcal{O}(\sqrt{N})$ search.

#### Course 2: Fault Tolerance, Quantum Error Correction & NISQ Systems
- **Module 1: Open Quantum Systems & Quantum Channels:**
  Density matrix formalism; completely positive trace-preserving (CPTP) maps; Kraus representation theorem; phase flip, bit flip, depolarizing channels.
- **Module 2: The Stabilizer Formalism:**
  The Pauli group $\mathcal{G}_n$; stabilizer groups and codes; syndrome measurements; Clifford group and the Gottesman-Knill theorem (efficient classical simulation of Clifford circuits).
- **Module 3: Quantum Error-Correcting Codes:**
  3-qubit bit-flip and phase-flip codes; Shor 9-qubit code; Calderbank-Shor-Steane (CSS) codes; Steane 7-qubit code; fault-tolerant gate implementations (transversal gates).
- **Module 4: Topological Surface Codes & Decoders:**
  Planar and toric codes; star and plaquette operators; anyonic excitations (fermionic/bosonic braiding); Minimum-Weight Perfect Matching (MWPM) and Union-Find decoders; fault-tolerant threshold calculation.
- **Module 5: Variational Quantum Algorithms for NISQ:**
  Variational Quantum Eigensolver (VQE) for molecular ground state energy; Quantum Approximate Optimization Algorithm (QAOA); barren plateaus and gradient mitigation strategies.

### Seminal Graduate-Level Papers & Textbooks
1. **Shor, P. W. (1994).** *Algorithms for quantum computation: discrete logarithms and factoring*. FOCS '94, 124–134.
2. **Grover, L. K. (1996).** *A fast mechanical quantum search algorithm*. STOC '96, 212–219.
3. **Fowler, A. G., Mariantoni, M., Martinis, J. M., & Cleland, A. N. (2012).** *Surface codes: Towards practical large-scale quantum computation*. Physical Review A, 86(3), 032324.
4. **Kitaev, A. Y. (2003).** *Fault-tolerant quantum computation by anyons*. Annals of Physics, 303(1), 2–30.
5. **Textbook:** Michael A. Nielsen & Isaac L. Chuang, *Quantum Computation and Quantum Information* (10th Anniversary Edition), Cambridge University Press.
6. **Textbook:** John Preskill, *Quantum Information and Computation* (Caltech Physics 219 Lecture Notes).

### Hands-On Lab Specifications & Track Build Deliverable
- **Lab 1: Quantum Circuit Simulator from Scratch in Python/Rust:**
  Build a statevector quantum circuit simulator supporting arbitrary single-qubit gates and multi-qubit controlled gates via tensor contraction. Verify correctness by simulating Shor's algorithm for $N = 15$ with exact probability state evolution.
- **Lab 2: Stabilizer Simulator & Gottesman-Knill Engine:**
  Implement a tableau-based stabilizer simulator using bitwise binary operations ($X$ and $Z$ vectors) capable of simulating Clifford circuits with 1,000+ qubits in polynomial time. Verify equivalence to full statevector simulation on 10-qubit random Clifford circuits.
- **Lab 3: Surface Code MWPM Decoder:**
  Implement a 2D surface code simulator under depolarizing noise. Construct the syndrome matching graph and integrate Edmonds' Blossom minimum-weight perfect matching algorithm. Plot the error threshold curve across distances $d=3, 5, 7$; demonstrate the crossing threshold at $\approx 1\%$.
- **🏁 Capstone Track Build Deliverable:**
  **An End-to-End Quantum Compiler & Variational Quantum Algorithm Pipeline.**
  - Scope: A software system that takes an abstract molecular Hamiltonian (e.g. $\text{H}_2$ or $\text{LiH}$), maps fermionic operators to qubit operators via Jordan-Wigner transformation, synthesizes an optimized ansatz circuit, and executes VQE.
  - Optimization: Implement circuit optimization passes (commuting gate cancellation, 2-qubit gate routing on a constrained hardware topology graph via swap-insertion).
  - Validation: Execute on both a noisy local density-matrix simulator and run jobs on a real public quantum cloud backend (IBM Quantum / IonQ via Qiskit), achieving convergence within chemical accuracy ($1.6 \times 10^{-3} \text{ Hartree}$) of the true ground-state energy.

---

## Track 12: Neuromorphic Computing & Heterogeneous Domain-Specific Architectures

### Overview & Motivation
As Dennard scaling has ended and Moore's Law slows, general-purpose CPUs cannot meet the computational and energy demands of modern workloads. The future of high-performance and low-power systems lies in domain-specific architectures (DSAs): systolic tensor processors (TPUs), massively parallel GPUs (CUDA warp architectures), spatial FPGA pipelines, and brain-inspired neuromorphic processors (Intel Loihi, IBM TrueNorth) processing asynchronous, event-driven spikes with co-located computation and non-volatile memory.

### Prerequisites
- Block 09 (Computer Systems), Block 14 (Computer Architecture), Track 1 (AI/ML), Track 6 (Computer Engineering).

### Learning Outcomes
1. **Biological & Computational Spiking Neuron Models:** Derive, simulate, and mathematically analyze Leaky Integrate-and-Fire (LIF), Izhikevich, and Hodgkin-Huxley dynamical neuron models.
2. **Event-Driven Neuromorphic Architecture Design:** Design asynchronous, non-von Neumann spatial core arrays communicating via Address-Event Representation (AER) packet-switched routing networks-on-chip (NoC).
3. **Spike-Timing-Dependent Plasticity (STDP):** Implement unsupervised local synaptic learning rules (Hebbian plasticity, STDP) directly in hardware microarchitecture without global backpropagation.
4. **GPU Microarchitecture & CUDA Warp Optimization:** Master the Nvidia GPU hardware execution model: streaming multiprocessors (SMs), warp schedulers, shared memory bank conflicts, coalesced global memory access, and tensor cores using PTX / CUDA C++.
5. **Systolic Arrays & Tensor Processing Accelerators:** Design and verify in Verilog/Chisel a parameterized 2D weight-stationary / output-stationary matrix multiplication systolic array with double-buffered register chains.
6. **FPGA Spatial Dataflow Acceleration:** Implement high-throughput computing pipelines on modern FPGAs using High-Level Synthesis (HLS) and RTL, optimizing loop unrolling, pipelining (II=1), and memory banking.

### Modular Syllabus Structure

#### Course 1: Neuromorphic Systems & Spiking Neural Networks
- **Module 1: Neurobiology & Mathematical Neuron Dynamics:**
  Membrane potentials, ion channel conductances, action potentials; Leaky Integrate-and-Fire (LIF) equations: $\tau_m \frac{dV}{dt} = -(V - V_{\text{rest}}) + R I(t)$; refractory periods; numerical integration.
- **Module 2: Information Encoding with Spikes:**
  Rate coding, temporal coding, time-to-first-spike (TTFS), phase coding; energy efficiency analysis: bit-ops vs multiply-accumulate (MAC) operations in neuromorphic silicon.
- **Module 3: Asynchronous Hardware & AER Routing:**
  Address-Event Representation (AER) protocol; quasi-delay-insensitive (QDI) asynchronous circuits; 2D mesh network-on-chip (NoC) multicast routing for million-neuron chips.
- **Module 4: Neuromorphic Silicon Case Studies:**
  Intel Loihi 1 & 2 (programmable microcode pipelines); IBM TrueNorth (crossbar arrays); BrainScaleS (analog physical emulation); SpiNNaker (massive multi-core ARM mesh).
- **Module 5: SNN Training Methodologies:**
  Surrogate gradient backpropagation through time (BPTT); ANN-to-SNN conversion methods; Spike-Timing-Dependent Plasticity (STDP) and equilibrium propagation.

#### Course 2: Heterogeneous Accelerators, CUDA & Spatial Silicon
- **Module 1: GPU Microarchitecture & Execution Hierarchy:**
  Streaming Multiprocessors (SMs), thread warps, SIMT (Single Instruction, Multiple Threads); instruction issue latency, register file pressure, occupancy calculation.
- **Module 2: High-Performance CUDA Kernel Optimization:**
  Tiled matrix multiplication (GEMM) in CUDA; avoiding shared memory bank conflicts; memory coalescing rules; warp shuffle instructions (`__shfl_sync`); asynchronous copy (`cuda::memcpy_async`).
- **Module 3: Tensor Core Architecture & Mixed-Precision Hardware:**
  Nvidia Tensor Cores (WMMA / MMA PTX instructions); systolic execution within warp units; FP16, BF16, INT8, and FP4 precision mechanics.
- **Module 4: Spatial Computing & Systolic Array Microarchitecture:**
  2D systolic array design; PE (Processing Element) datapath; weight-stationary vs weight-streaming vs output-stationary dataflows; FIFO interconnects; roofline model performance bounds.
- **Module 5: FPGA Acceleration & High-Level Synthesis (HLS):**
  Spatial architectures on AMD/Xilinx UltraScale+ / Intel Agilex; pragmas for initiation interval (`#pragma HLS pipeline II=1`), loop tiling, array partitioning; AXI4 bus interfacing.

### Seminal Graduate-Level Papers & Textbooks
1. **Davies, M. et al. (2018).** *Loihi: A Neuromorphic Manycore Processor with On-Chip Learning*. IEEE Micro, 38(1), 82–99.
2. **Jouppi, N. P. et al. (2017).** *In-Datacenter Performance Analysis of a Tensor Processing Unit*. ISCA '17, 1–12. (Google TPU v1).
3. **Merolla, P. A. et al. (2014).** *A million spiking-neuron integrated circuit with a scalable communication network and interface* (IBM TrueNorth). Science, 345(6197), 668–673.
4. **Neftci, E. O., Mostafa, H., & Zenke, F. (2019).** *Surrogate Gradient Learning in Spiking Neural Networks*. IEEE Signal Processing Magazine, 36(6), 51–63.
5. **Textbook:** Carver Mead, *Analog VLSI and Neural Systems*, Addison-Wesley. (The foundational text of neuromorphic engineering).
6. **Textbook:** David B. Kirk & Wen-mei W. Hwu, *Programming Massively Parallel Processors: A Hands-on Approach*, 4th ed., Morgan Kaufmann.
7. **Textbook:** John L. Hennessy & David A. Patterson, *Computer Architecture: A Quantitative Approach* (Chapter 7: Domain-Specific Architectures), 6th ed.

### Hands-On Lab Specifications & Track Build Deliverable
- **Lab 1: Event-Driven Spiking Neural Network Simulator:**
  Build a high-performance C++/Rust event-driven simulator for an SNN with 10,000 LIF neurons and dynamic synapses. Process asynchronous event queues without global timestep ticks; demonstrate $\ge 10\times$ speedup over fixed-timestep simulation on sparse event streams.
- **Lab 2: Peak-Performance CUDA GEMM Kernel:**
  Write a custom matrix multiplication (GEMM) CUDA kernel from scratch using shared memory double-buffering, register tiling, and warp shuffle instructions. Benchmark against cuBLAS on an Nvidia GPU (RTX 30xx/40xx or A100); achieve $\ge 85\%$ of cuBLAS peak TFLOPs.
- **Lab 3: Verilog/SystemVerilog Systolic Array with Open-Source Verification:**
  Design a $16 \times 16$ INT8 output-stationary systolic array in SystemVerilog. Synthesize and simulate using Verilator and Cocotb; verify bit-accurate execution of a convolutional layer with zero pipeline stalls.
- **🏁 Capstone Track Build Deliverable:**
  **A Complete Neuromorphic Processor / Domain-Specific Accelerator Synthesized on FPGA or Tapeout Flow.**
  - Option A (Neuromorphic): A multi-core spiking neural network accelerator written in SystemVerilog, featuring 16 neural cores, AER packet router, on-chip SRAM for weights, and surrogate-gradient trained weights for real-time classification of DVS (Dynamic Vision Sensor) event camera streams.
  - Option B (Systolic TPU): A complete RISC-V coprocessor containing a $16 \times 16$ matrix multiplication engine, DMA controller, and custom RISC-V instruction extensions (via RoCC interface), validated in RTL simulation and deployed to an FPGA board (e.g. Xilinx Artix-7 / Kria KV260), demonstrating live quantized image inference.

---

# Part IV: Integration Matrix & Synergies with Existing Vault

### 1. Mapping R2 Mathematical Injections into the Existing 32-Block Syllabi

| Injected Mathematical Foundation | Primary Target Block | Secondary Infiltration | Specific Upgrade Over Existing Vault Content |
|---|---|---|---|
| **Measure-Theoretic Probability** | Block 15 (Probability) | Block 22 (Statistics), Track 1 | Upgrades Tsitsiklis 6.041 to Durrett measure spaces, Radon-Nikodym conditional expectation, and martingales. |
| **Advanced Convex Optimization** | Block 25 (Convex Optimization) | Block 20 (Algorithms II), Track 1 | Upgrades standard CVXPY usage to Nesterov accelerated lower bounds, Fenchel duality, and ADMM Lyapunov convergence proofs. |
| **Metric Spaces & Topology for CS** | Block 18 (Real Analysis) | Block 24 (Theory of Computation), Track 5 | Upgrades Abbott's single-variable $\mathbb{R}^1$ theorems to general metric spaces, Baire category, and Scott domain theory. |
| **Category Theory & Type Theory** | Block 17 (Software Construction) | Track 5 (Compilers), Track 10 (Formal Methods) | Bridges basic Java/TypeScript patterns into Yoneda Lemma, Curry-Howard-Lambek isomorphism, and System F strong normalization. |
| **Abstract Algebra & Number Theory** | Block 10 (Math for CS) | Block 27 (Cryptopals), Track 3 (Crypto) | Supplements basic modular arithmetic with Galois fields $\mathbb{F}_{p^n}$, Elliptic Curve group laws, and Regev's LWE reduction proofs. |
| **Spectral Graph Theory** | Block 13 & 20 (Algorithms I & II) | Block 24 (Theory of Computation) | Adds normalized Laplacian spectrum, Cheeger's inequality, Ramanujan expanders, and Dinur's PCP theorem proof. |

---

### 2. Modern Paradigms (R3) Integration into the Specializations Architecture

The Noblett Repository currently specifies a dual-specialization structure across Years 4 & 5 (*"Two deep beats six shallow"*). The six modern paradigm tracks expand the available tracks from 6 to 12:

```
========================================================================================================
                                 THE COMPLETE 12-TRACK SPECIALIZATION CATALOG
========================================================================================================
TRADITIONAL CORE TRACKS:                               MODERN CUTTING-EDGE PARADIGM TRACKS:
- Track 1: AI & Machine Learning                      - Track 7: TinyML & Edge Artificial Intelligence
- Track 2: Systems & Performance                      - Track 8: Rust for High-Assurance Systems
- Track 3: Security & Cryptography                     - Track 9: HIL Virtualization & Cyber-Physical Systems
- Track 4: Computer Graphics & Vision                 - Track 10: Formal Methods & Mechanized Verification
- Track 5: Programming Languages & Compilers          - Track 11: Quantum Information & Quantum Computing
- Track 6: Computer Engineering (Deep Hardware)       - Track 12: Neuromorphic & Heterogeneous Architectures
========================================================================================================
```

#### Natural High-Impact Track Pairings:
1. **The Modern Ultra-Systems Engineer:** Track 8 (Rust Systems) + Track 2 (Systems & Performance)
2. **The Autonomous Cyber-Physical Architect:** Track 7 (TinyML) + Track 9 (HIL Virtualization)
3. **The High-Assurance Hardware/Software Verifier:** Track 10 (Formal Methods) + Track 5 (Compilers) or Track 6 (Computer Engineering)
4. **The Post-Silicon Architecture Pioneer:** Track 12 (Neuromorphic/Heterogeneous) + Track 11 (Quantum Computing)
5. **The Next-Gen Edge AI Specialist:** Track 1 (AI/ML) + Track 7 (TinyML & Edge AI)

---

# Part V: Handoff Specifications & Concrete File Deliverables

To transition this catalog into concrete additions to The Noblett Repository vault, downstream builder agents should execute the following operations:

1. **Update `01 - Curriculum/Specializations/Specializations Hub.md`:**
   - Add links to Tracks 7, 8, 9, 10, 11, and 12.
   - Expand the "Extra Math for Specializations" list with references to Durrett, Rockafellar, Mac Lane, Dummit & Foote, and Spielman.
2. **Create New Specialization Track Files in `01 - Curriculum/Specializations/`:**
   - `Track 7 - TinyML and Edge AI.md`
   - `Track 8 - Rust for Systems Engineering.md`
   - `Track 9 - Hardware-in-the-Loop Virtualization.md`
   - `Track 10 - Formal Verification with Lean and Coq.md`
   - `Track 11 - Quantum Information and Computing.md`
   - `Track 12 - Neuromorphic and Heterogeneous Architectures.md`
3. **Inject R2 Mathematical Rigor & PhD Papers into Core Blocks:**
   - Update `01 - Curriculum/Year 2 - Systems/15 - Probability.md` with Measure Theory and Martingales.
   - Update `01 - Curriculum/Year 3 - Depth/18 - Real Analysis.md` with Metric Spaces and Domain Theory.
   - Update `01 - Curriculum/Year 4 - Specialization/25 - Convex Optimization.md` with Nesterov accelerated lower bounds and ADMM proofs.
   - Update `01 - Curriculum/Year 4 - Specialization/23 - Distributed Systems.md` with formal FLP impossibility proof.
4. **Expand `03 - Papers/Paper Reading Hub.md`:**
   - Inject the curated seminal PhD-level papers catalog (Section I & II above) into the checklist of required papers.
5. **Update `Checklist.md`:**
   - Add tracking checkboxes for the new specialization tracks and graduate mathematical milestones.

---
*Catalog formulation complete. Ready for vault integration by implementation agents.*
