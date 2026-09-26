---
title: "11 - Linear Algebra — Worked Proofs"
type: reference
tags:
  - reference
  - answer-key
---

# 11 - Linear Algebra — Worked Proofs

> [!WARNING] Answer key — open only after your own attempt
> These derivations were generated as reference material, not study notes. Reading them first creates the illusion of competence that [[how-i-study]] warns about.
> Protocol: attempt the proof from a blank sheet in [[11 - Linear Algebra]] → compare here → log every gap you found.
> They are unverified; treat any step you cannot justify as a possible error, not as authority.

Back to: [[11 - Linear Algebra]] · [[Worked Proofs Index]]

---

### 1. The Spectral Theorem for Real Symmetric Matrices
**Theorem:** Let $A \in \mathbb{R}^{n \times n}$ be a real symmetric matrix ($A = A^T$). Then:
1. All eigenvalues of $A$ are real ($\lambda_i \in \mathbb{R}$).
2. Eigenvectors corresponding to distinct eigenvalues are mutually orthogonal.
3. There exists an orthonormal matrix $Q \in \mathbb{R}^{n \times n}$ ($Q^T Q = I$) and diagonal matrix $\Lambda = \text{diag}(\lambda_1, \dots, \lambda_n)$ such that $A = Q \Lambda Q^T$.

#### Step-by-Step Derivation & Proof:
1. **Eigenvalues are Real:**
   Let $\lambda \in \mathbb{C}$ be an eigenvalue with non-zero eigenvector $v \in \mathbb{C}^n$ such that $Av = \lambda v$.
   Consider the conjugate transpose scalar quantity $v^* A v$:
   $$v^* A v = v^* (A v) = v^* (\lambda v) = \lambda (v^* v) = \lambda \|v\|^2$$
   Taking the complex conjugate transpose of the scalar:
   $$(v^* A v)^* = v^* A^* v = v^* A^T v = v^* A v$$
   because $A$ is real symmetric ($A^* = A^T = A$). Thus $v^* A v \in \mathbb{R}$.
   Since $\|v\|^2 = \sum_{i=1}^n |v_i|^2 > 0$ is a strictly positive real number, $\lambda = \frac{v^* A v}{\|v\|^2} \in \mathbb{R}$.

2. **Orthogonality of Distinct Eigenspaces:**
   Let $A v_1 = \lambda_1 v_1$ and $A v_2 = \lambda_2 v_2$ with $\lambda_1 \ne \lambda_2$.
   $$\lambda_1 \langle v_1, v_2 \rangle = \langle \lambda_1 v_1, v_2 \rangle = \langle A v_1, v_2 \rangle = (A v_1)^T v_2 = v_1^T A^T v_2 = v_1^T A v_2 = \langle v_1, A v_2 \rangle = \lambda_2 \langle v_1, v_2 \rangle$$
   Therefore:
   $$(\lambda_1 - \lambda_2) \langle v_1, v_2 \rangle = 0 \implies \langle v_1, v_2 \rangle = 0 \quad (\text{since } \lambda_1 \ne \lambda_2)$$

3. **Inductive Orthonormal Decomposition:**
   By the Fundamental Theorem of Algebra, $A$ has at least one real eigenvalue $\lambda_1$ with unit eigenvector $q_1 \in \mathbb{R}^n$.
   Extend $\{q_1\}$ to an orthonormal basis $\{q_1, w_2, \dots, w_n\}$ of $\mathbb{R}^n$, forming orthogonal matrix $W_1 = [q_1 \mid W]$.
   Compute:
   $$W_1^T A W_1 = \begin{bmatrix} q_1^T \\ W^T \end{bmatrix} A \begin{bmatrix} q_1 & W \end{bmatrix} = \begin{bmatrix} q_1^T A q_1 & q_1^T A W \\ W^T A q_1 & W^T A W \end{bmatrix} = \begin{bmatrix} \lambda_1 & 0 \\ 0 & A_1 \end{bmatrix}$$
   Because $W_1^T A W_1$ is symmetric, $q_1^T A W = (W^T A q_1)^T = (\lambda_1 W^T q_1)^T = 0$.
   The submatrix $A_1 = W^T A W$ is an $(n-1) \times (n-1)$ real symmetric matrix.
   By mathematical induction on dimension $n$, there exists an orthogonal matrix $Q_1$ such that $Q_1^T A_1 Q_1 = \Lambda_1$.
   Setting $Q = W_1 \begin{bmatrix} 1 & 0 \\ 0 & Q_1 \end{bmatrix}$ yields $Q^T A Q = \Lambda$, completing the proof. $\blacksquare$

---

### 2. Derivation of the Singular Value Decomposition (SVD)
**Theorem:** For any matrix $A \in \mathbb{R}^{m \times n}$ of rank $r \le \min(m, n)$, there exist orthogonal matrices $U \in \mathbb{R}^{m \times m}$ ($U^T U = I_m$), $V \in \mathbb{R}^{n \times n}$ ($V^T V = I_n$), and a diagonal matrix $\Sigma \in \mathbb{R}^{m \times n}$ with non-negative entries $\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_r > 0$ such that:
$$A = U \Sigma V^T = \sum_{i=1}^r \sigma_i u_i v_i^T$$

#### Mathematical Derivation:
1. **Symmetric Positive Semi-Definite Gram Matrix:**
   Form the matrix $S = A^T A \in \mathbb{R}^{n \times n}$.
   $S^T = (A^T A)^T = A^T A = S$, so $S$ is symmetric.
   For any $x \in \mathbb{R}^n$, $x^T S x = x^T A^T A x = (Ax)^T (Ax) = \|Ax\|^2 \ge 0$, so $S$ is positive semi-definite.
2. **Eigenbasis Construction for $V$:**
   By the Spectral Theorem, $A^T A$ has an orthonormal eigenbasis $\{v_1, \dots, v_n\}$ with real eigenvalues $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_n \ge 0$.
   Since $\text{rank}(A^T A) = \text{rank}(A) = r$, exactly $r$ eigenvalues are strictly positive: $\lambda_1 \ge \dots \ge \lambda_r > 0$, and $\lambda_{r+1} = \dots = \lambda_n = 0$.
   Define the *singular values* $\sigma_i = \sqrt{\lambda_i}$ for $i \in \{1, \dots, r\}$.
3. **Construction of Left Singular Vectors $U$:**
   For $1 \le i \le r$, define:
   $$u_i = \frac{1}{\sigma_i} A v_i \in \mathbb{R}^m$$
   Verify orthonormality of $\{u_1, \dots, u_r\}$:
   $$\langle u_i, u_j \rangle = u_i^T u_j = \left(\frac{A v_i}{\sigma_i}\right)^T \left(\frac{A v_j}{\sigma_j}\right) = \frac{v_i^T (A^T A v_j)}{\sigma_i \sigma_j} = \frac{v_i^T (\lambda_j v_j)}{\sigma_i \sigma_j} = \frac{\lambda_j}{\sigma_i \sigma_j} v_i^T v_j = \frac{\sigma_j^2}{\sigma_i \sigma_j} \delta_{ij} = \delta_{ij}$$
   Extend $\{u_1, \dots, u_r\}$ to an orthonormal basis $\{u_1, \dots, u_m\}$ of $\mathbb{R}^m$ using the Gram-Schmidt process.
4. **Synthesizing the Factorization:**
   For $1 \le j \le r$: $A v_j = \sigma_j u_j$.
   For $r < j \le n$: $\|A v_j\|^2 = v_j^T (A^T A v_j) = \lambda_j v_j^T v_j = 0 \implies A v_j = 0$.
   Therefore, in block form:
   $$A [v_1 \dots v_n] = [u_1 \dots u_m] \Sigma \implies A V = U \Sigma \implies A = U \Sigma V^T \quad \blacksquare$$

---

### 3. Courant-Fischer Min-Max Theorem
**Theorem:** Let $A \in \mathbb{R}^{n \times n}$ be a real symmetric matrix with eigenvalues sorted in descending order: $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_n$.
Let $R_A(x) = \frac{x^T A x}{x^T x}$ denote the Rayleigh quotient for $x \ne 0$. Then for every $k \in \{1, \dots, n\}$:
$$\lambda_k = \max_{\substack{S \subseteq \mathbb{R}^n \\ \dim(S) = k}} \min_{\substack{x \in S \\ x \ne 0}} R_A(x) = \min_{\substack{T \subseteq \mathbb{R}^n \\ \dim(T) = n - k + 1}} \max_{\substack{x \in T \\ x \ne 0}} R_A(x)$$

#### Proof:
Let $\{v_1, \dots, v_n\}$ be an orthonormal eigenbasis of $A$ with $A v_i = \lambda_i v_i$.
1. **Lower Bound via Subspace Choice:**
   Choose $S_k = \text{span}\{v_1, v_2, \dots, v_k\}$. Clearly $\dim(S_k) = k$.
   Any unit vector $x \in S_k$ can be written $x = \sum_{i=1}^k c_i v_i$ with $\sum_{i=1}^k c_i^2 = 1$.
   $$R_A(x) = x^T A x = \sum_{i=1}^k \lambda_i c_i^2 \ge \lambda_k \sum_{i=1}^k c_i^2 = \lambda_k$$
   Because equality holds for $x = v_k$, we have $\min_{x \in S_k, x \ne 0} R_A(x) = \lambda_k$.
   Therefore:
   $$\max_{\dim(S)=k} \min_{x \in S, x \ne 0} R_A(x) \ge \lambda_k$$
2. **Upper Bound for Arbitrary Subspaces:**
   Now let $S$ be *any* arbitrary subspace of $\mathbb{R}^n$ with $\dim(S) = k$.
   Define $W_{k-1} = \text{span}\{v_k, v_{k+1}, \dots, v_n\}$. The dimension of $W_{k-1}$ is $n - k + 1$.
   By the dimension theorem for vector subspaces:
   $$\dim(S \cap W_{k-1}) = \dim(S) + \dim(W_{k-1}) - \dim(S + W_{k-1}) \ge k + (n - k + 1) - n = 1$$
   Thus, there exists at least one non-zero vector $y \in S \cap W_{k-1}$.
   Since $y \in W_{k-1}$, $y = \sum_{i=k}^n d_i v_i$. Normalizing $\|y\|^2 = \sum_{i=k}^n d_i^2 = 1$:
   $$R_A(y) = y^T A y = \sum_{i=k}^n \lambda_i d_i^2 \le \lambda_k \sum_{i=k}^n d_i^2 = \lambda_k$$
   Since $y \in S$, the minimum over all vectors in $S$ cannot exceed $R_A(y)$:
   $$\min_{x \in S, x \ne 0} R_A(x) \le R_A(y) \le \lambda_k$$
   Since this holds for every subspace $S$ of dimension $k$, the maximum over all such subspaces must satisfy $\le \lambda_k$.
   Combining both bounds proves the equality: $\max_{\dim(S)=k} \min_{x \in S, x \ne 0} R_A(x) = \lambda_k$. $\blacksquare$

---

### 📄 Landmark Research Papers (from [[03 - Papers/Paper Reading Hub|Paper Reading Hub]])

The following foundational papers from the [[03 - Papers/Paper Reading Hub|Paper Reading Hub]] are assigned to Block 11. Analyze each using the Keshav Three-Pass Methodology:

1. **"Multilayer Feedforward Networks are Universal Approximators"** (Kurt Hornik, Maxwell Stinchcombe, Halbert White, 1989)
    - *Venue:* Neural Networks (Paper 26 in [[03 - Papers/Paper Reading Hub|Paper Reading Hub]])
    - *Landmark Invariant:* Stone-Weierstrass and Hahn-Banach derivation proving single-hidden-layer feedforward networks with non-polynomial activations are dense in $C(K)$.
    - *Reading Guidance:* Focus Pass 2 on the functional analysis arguments and cosine basis approximation mechanisms.
2. **"Attention Is All You Need"** (Ashish Vaswani et al., 2017)
    - *Venue:* NeurIPS 2017 (Paper 27 in [[03 - Papers/Paper Reading Hub|Paper Reading Hub]])
    - *Landmark Invariant:* Scaled dot-product multi-head self-attention mechanism: $\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$, eliminating recurrent bottleneck.
    - *Reading Guidance:* Trace the matrix multiplication dimensions, computational complexity per layer ($\mathcal{O}(n^2 \cdot d)$), and multi-head projection subspaces.
