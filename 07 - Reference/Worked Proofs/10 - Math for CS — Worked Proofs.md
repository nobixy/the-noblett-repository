---
title: "10 - Math for CS — Worked Proofs"
type: reference
tags:
  - reference
  - answer-key
---

# 10 - Math for CS — Worked Proofs

> [!WARNING] Answer key — open only after your own attempt
> These derivations were generated as reference material, not study notes. Reading them first creates the illusion of competence that [[how-i-study]] warns about.
> Protocol: attempt the proof from a blank sheet in [[10 - Math for CS]] → compare here → log every gap you found.
> They are unverified; treat any step you cannot justify as a possible error, not as authority.

Back to: [[10 - Math for CS]] · [[Worked Proofs Index]]

---

### 1. The Curry-Howard Isomorphism (Propositions-as-Types)
The Curry-Howard correspondence establishes a deep, structural isomorphism between constructive logic (Intuitionistic Propositional Logic, IPL) and typed computational calculi (Simply Typed Lambda Calculus, $\lambda^\to$).

#### Formal Correspondence Dictionary
| Logical Concept (Intuitionistic Logic) | Computational Concept (Type Theory / $\lambda^\to$) |
|:---|:---|
| Proposition $A$ | Type $A$ |
| Proof of Proposition $A$ | Program / Term $t$ of type $A$ ($t : A$) |
| Implication $A \implies B$ | Function Type $A \to B$ |
| Conjunction $A \land B$ | Product Type $A \times B$ (Pair `(a, b)`) |
| Disjunction $A \lor B$ | Sum Type $A + B$ (`Either A B`) |
| True ($\top$) | Unit Type $1$ (`()`) |
| False / Absurdity ($\bot$) | Empty / Bottom Type $0$ (`Void`) |
| Modus Ponens $\frac{A \implies B \quad A}{B}$ | Function Application $\frac{f : A \to B \quad x : A}{f(x) : B}$ |
| Implication Introduction $\frac{\Gamma, x: A \vdash e : B}{\Gamma \vdash \lambda x. e : A \to B}$ | $\lambda$-Abstraction |
| Conjunction Elimination $\pi_1 : A \land B \implies A$ | First Projection $\text{fst} : A \times B \to A$ |
| Disjunction Introduction $\text{inl} : A \implies A \lor B$ | Left Injection $\text{inl} : A \to A + B$ |
| Proof Normalization (Gentzen Cut Elimination) | $\beta$-Reduction: $(\lambda x. e) v \to_\beta e[x \mapsto v]$ |

#### Soundness and Consistency Invariant
- **Strong Normalization Theorem:** Every well-typed closed term in $\lambda^\to$ terminates under $\beta$-reduction to a unique normal form (Church-Rosser theorem).
- **Logical Consistency Corollary:** Because there are no closed values (canonical forms) of type `Void` ($0$), it is impossible to construct a term $\vdash t : \bot$. Hence, Intuitionistic Propositional Logic is provably sound and consistent: $\not\vdash \bot$.

---

### 2. The Cook-Levin Theorem Reduction Proof Sketch (Tableau Reduction)
**Theorem (Cook 1971, Levin 1973):** The Boolean Satisfiability problem ($\text{SAT}$) is $\text{NP}$-complete.

#### Proof Architecture: Generic Polynomial-Time Reduction
To prove any language $L \in \text{NP}$ reduces to $\text{SAT}$ in polynomial time ($L \le_P \text{SAT}$):
Let $M = (Q, \Sigma, \Gamma, \delta, q_0, q_{accept}, q_{reject})$ be a non-deterministic Turing Machine deciding $L$ in polynomial time $p(n)$, where $n = |w|$.
An accepting computation of $M$ on $w$ is represented by a $p(n) \times p(n)$ grid (*tableau*), where row $i$ represents the configuration of $M$ at time step $i$.

#### Variable Encoding
For each cell $(i, j) \in [1, p(n)] \times [1, p(n)]$ and each tape symbol or state-tape pair $\sigma \in \Gamma \cup (Q \times \Gamma)$, define a Boolean variable:
$$x_{i, j, \sigma} = 1 \iff \text{cell } (i, j) \text{ contains symbol } \sigma$$

#### Formula Construction: $\Phi = \phi_{cell} \land \phi_{start} \land \phi_{accept} \land \phi_{move}$
1. **$\phi_{cell}$ (Valid Cell Contents):** Every cell in the tableau contains exactly one symbol:
   $$\phi_{cell} = \bigwedge_{i=1}^{p(n)} \bigwedge_{j=1}^{p(n)} \left( \left( \bigvee_{\sigma} x_{i, j, \sigma} \right) \land \bigwedge_{\sigma \ne \sigma'} (\neg x_{i, j, \sigma} \lor \neg x_{i, j, \sigma'}) \right)$$
2. **$\phi_{start}$ (Initial Configuration):** Row 1 represents the initial configuration $(q_0, w_1), w_2, \dots, w_n, \sqcup, \dots, \sqcup$:
   $$\phi_{start} = x_{1, 1, (q_0, w_1)} \land \left( \bigwedge_{j=2}^n x_{1, j, w_j} \right) \land \left( \bigwedge_{j=n+1}^{p(n)} x_{1, j, \sqcup} \right)$$
3. **$\phi_{accept}$ (Acceptance Invariant):** The machine enters $q_{accept}$ at some point within $p(n)$ steps:
   $$\phi_{accept} = \bigvee_{i=1}^{p(n)} \bigvee_{j=1}^{p(n)} \bigvee_{a \in \Gamma} x_{i, j, (q_{accept}, a)}$$
4. **$\phi_{move}$ (Local Transition Invariant):** The state transitions between row $i$ and row $i+1$ strictly obey $\delta$.
  - Any cell $(i+1, j)$ is uniquely determined by its local neighborhood in the previous step: cells $(i, j-1), (i, j), (i, j+1)$.
  - A $2 \times 3$ window of cells is *legal* if the assignment of symbols in row $i+1$ can legally follow from row $i$ under transition relation $\delta$.
  - Because the window size is $2 \times 3 = 6$ cells (finite constant), the condition "window at $(i, j)$ is legal" can be expressed as a CNF clause of size $\mathcal{O}(1)$.
   $$\phi_{move} = \bigwedge_{i=1}^{p(n)-1} \bigwedge_{j=2}^{p(n)-1} \text{LegalWindow}(i, j)$$

#### Complexity and Correctness
- **Polynomial Bound:** The tableau has $p(n)^2$ cells. The number of variables is $|\Gamma \cup (Q \times \Gamma)| \cdot p(n)^2 = \mathcal{O}(p(n)^2)$. The total formula size $|\Phi| = \mathcal{O}(p(n)^2)$, computable in polynomial time $\mathcal{O}(p(n)^2)$.
- **Equivalence:** $M$ accepts $w$ if and only if there exists a valid tableau execution, which holds if and only if $\Phi$ is satisfiable.
- **NP-Completeness:** Since $\text{SAT} \in \text{NP}$ (evaluating a truth assignment takes linear time) and every $L \in \text{NP}$ reduces to $\text{SAT}$ in polynomial time, $\text{SAT}$ is $\text{NP}$-complete. $\blacksquare$

---

### 📄 Landmark Research Papers (from [[03 - Papers/Paper Reading Hub|Paper Reading Hub]])

The following foundational papers from the [[03 - Papers/Paper Reading Hub|Paper Reading Hub]] are assigned to Block 10. Analyze each using the Keshav Three-Pass Methodology:

1. **"A Syntactic Approach to Type Soundness"** (Andrew K. Wright & Matthias Felleisen, 1994)
    - *Venue:* Information and Computation (Paper 19 in [[03 - Papers/Paper Reading Hub|Paper Reading Hub]])
    - *Landmark Invariant:* Standard inductive proof technique for language type soundness via Progress ($e: \tau \implies e \text{ value} \lor e \to e'$) and Preservation ($e: \tau \land e \to e' \implies e': \tau$).
    - *Reading Guidance:* Focus Pass 2 on the small-step operational semantics reductions and substitution lemma invariants.
2. **"New Directions in Cryptography"** (Whitfield Diffie & Martin E. Hellman, 1976)
    - *Venue:* IEEE Transactions on Information Theory (Paper 31 in [[03 - Papers/Paper Reading Hub|Paper Reading Hub]])
    - *Landmark Invariant:* Asymmetric public-key cryptography; Diffie-Hellman key exchange over discrete logarithm groups; computational one-way trapdoor functions.
    - *Reading Guidance:* Trace the mathematical architecture of one-way trapdoor functions and public key distribution protocols.
3. **"A Method for Obtaining Digital Signatures and Public-Key Cryptosystems"** (Ronald L. Rivest, Adi Shamir, Leonard Adleman, 1978)
    - *Venue:* Communications of the ACM (Paper 32 in [[03 - Papers/Paper Reading Hub|Paper Reading Hub]])
    - *Landmark Invariant:* The RSA cryptosystem; Euler's totient theorem and integer factorization hardness for digital signatures and encryption.
    - *Reading Guidance:* Verify the modular exponentiation correctness proof using Euler's totient function and the Chinese Remainder Theorem.
4. **"How to Share a Secret"** (Adi Shamir, 1979)
    - *Venue:* Communications of the ACM (Paper 35 in [[03 - Papers/Paper Reading Hub|Paper Reading Hub]])
    - *Landmark Invariant:* $(k, n)$-threshold secret sharing via Lagrange polynomial interpolation over finite fields $\mathbb{F}_p$; information-theoretically secure against $<k$ colluding shares.
    - *Reading Guidance:* Reconstruct the Lagrange interpolation over $\mathbb{Z}_p$ and prove information-theoretic secrecy for $k-1$ shares.
