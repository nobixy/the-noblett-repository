---
title: "20 - Algorithms II — Worked Proofs"
type: reference
tags:
  - reference
  - answer-key
---

# 20 - Algorithms II — Worked Proofs

> [!WARNING] Answer key — open only after your own attempt
> These derivations were generated as reference material, not study notes. Reading them first creates the illusion of competence that [[how-i-study]] warns about.
> Protocol: attempt the proof from a blank sheet in [[Algorithms II]] → compare here → log every gap you found.
> They are unverified; treat any step you cannot justify as a possible error, not as authority.

Back to: [[Algorithms II]] · [[Worked Proofs Index]]

---

### 1. Linear Programming Duality & Strong Duality Theorem
Consider the primal Linear Program in standard inequality form:
$$\text{Primal } (P): \quad \max \; c^T x \quad \text{s.t.} \quad A x \le b, \; x \ge 0$$
where $A \in \mathbb{R}^{m \times n}, b \in \mathbb{R}^m, c \in \mathbb{R}^n$.

The associated dual Linear Program is:
$$\text{Dual } (D): \quad \min \; b^T y \quad \text{s.t.} \quad A^T y \ge c, \; y \ge 0$$

#### Weak Duality Theorem:
If $x$ is primal-feasible ($A x \le b, x \ge 0$) and $y$ is dual-feasible ($A^T y \ge c, y \ge 0$), then:
$$c^T x \le b^T y$$
*Proof:*
$$c^T x \le (A^T y)^T x = y^T (A x) \le y^T b = b^T y$$
*Corollary (Optimality Certificate):* If $c^T x^* = b^T y^*$ for feasible $x^*$ and $y^*$, then $x^*$ is an optimal solution to $(P)$ and $y^*$ is an optimal solution to $(D)$.

#### Strong Duality Theorem via Farkas' Lemma:
**Farkas' Lemma:** Let $M \in \mathbb{R}^{m \times n}$ and $q \in \mathbb{R}^m$. Exactly one of the following two statements is true:
1. $\exists x \ge 0$ such that $M x = q$.
2. $\exists y \in \mathbb{R}^m$ such that $M^T y \ge 0$ and $q^T y < 0$.
*(Proof follows from the Separating Hyperplane Theorem applied to the closed convex cone $K = \{ M x \mid x \ge 0 \}$. If $q \notin K$, there exists a strictly separating hyperplane separating $q$ from $K$.)*

**Theorem (Strong Duality):** If either $(P)$ or $(D)$ has a finite optimal solution, then both have optimal solutions $x^*$ and $y^*$, and their optimal objective values coincide:
$$c^T x^* = b^T y^* \quad \blacksquare$$

---

### 2. The Ellipsoid Algorithm Polynomial-Time Bound (Khachiyan 1979)
**Problem:** Decide the feasibility of a system of linear inequalities $P = \{ x \in \mathbb{R}^n \mid A x \le b \}$ with bit-length encoding $L$.

#### Geometric Algorithm:
An ellipsoid $E(z, B)$ centered at $z \in \mathbb{R}^n$ with positive-definite shape matrix $B \succ 0$ is defined as:
$$E(z, B) = \{ x \in \mathbb{R}^n \mid (x - z)^T B^{-1} (x - z) \le 1 \}$$
1. **Initial Bounding Ellipsoid:** Start with $E_0 = E(0, R^2 I)$ where radius $R = \sqrt{n} \cdot 2^L$, guaranteeing $P \subseteq E_0$.
2. **Separation Oracle Iteration:** At step $k$, evaluate center $z_k$:
  - If $z_k \in P$, return **FEASIBLE** with witness $z_k$.
  - If $z_k \notin P$, identify a violated constraint $a_i^T z_k > b_i$.
  - The hyperplane $a_i^T (x - z_k) \le 0$ cuts the ellipsoid $E_k$ in half.
3. **Minimum-Volume Enclosing Ellipsoid:**
   Construct the unique minimum-volume ellipsoid $E_{k+1} = E(z_{k+1}, B_{k+1})$ enclosing the half-ellipsoid $E_k \cap \{ x \mid a_i^T x \le a_i^T z_k \}$:
   $$z_{k+1} = z_k - \frac{1}{n+1} \frac{B_k a_i}{\sqrt{a_i^T B_k a_i}}$$
   $$B_{k+1} = \frac{n^2}{n^2 - 1} \left( B_k - \frac{2}{n+1} \frac{(B_k a_i)(B_k a_i)^T}{a_i^T B_k a_i} \right)$$

#### Volume Contraction Invariant:
The volume ratio between consecutive ellipsoids satisfies:
$$\frac{\text{vol}(E_{k+1})}{\text{vol}(E_k)} = \left(\frac{n}{n+1}\right) \left(\frac{n}{\sqrt{n^2 - 1}}\right)^{n-1} < \exp\left(-\frac{1}{2(n+1)}\right)$$
- If $P$ is full-dimensional and feasible, $\text{vol}(P) \ge 2^{-(n+2)L}$.
- The number of iterations before $\text{vol}(E_k) < \text{vol}(P)$ is strictly bounded by:
  $$N \le 2(n+1) \ln\left( \frac{\text{vol}(E_0)}{\text{vol}(P)} \right) = \mathcal{O}(n^2 L)$$
Each iteration requires $\mathcal{O}(n^2)$ arithmetic operations. Hence, the Ellipsoid Algorithm decides LP feasibility in polynomial time $\mathcal{O}(n^4 L)$, proving $\text{LP} \in \text{P}$. $\blacksquare$

---

### 3. Cheeger's Inequality on Spectral Graph Partitioning
Let $G = (V, E)$ be a $d$-regular undirected graph with normalized graph Laplacian $\mathcal{L} = I - \frac{1}{d} A$.
Let the eigenvalues of $\mathcal{L}$ be $0 = \lambda_1 \le \lambda_2 \le \dots \le \lambda_n \le 2$.

#### Cheeger Conductance Constant $h(G)$:
For any cut $(S, \bar{S})$ with $0 < |S| \le |V|/2$, the expansion ratio is:
$$\phi(S) = \frac{|E(S, \bar{S})|}{d |S|}, \quad h(G) = \min_{\substack{S \subset V \\ 0 < |S| \le |V|/2}} \phi(S)$$

**Theorem (Cheeger's Inequality):**
$$\frac{\lambda_2}{2} \le h(G) \le \sqrt{2 \lambda_2}$$

#### Proof of Lower Bound ($\lambda_2 \le 2 h(G)$):
By the Courant-Fischer Theorem:
$$\lambda_2 = \min_{\substack{x \ne 0 \\ \sum_u x_u = 0}} \frac{x^T \mathcal{L} x}{x^T x} = \min_{\substack{x \ne 0 \\ \sum_u x_u = 0}} \frac{\frac{1}{d} \sum_{(u, v) \in E} (x_u - x_v)^2}{\sum_{u \in V} x_u^2}$$
Let $S^*$ be the optimal Cheeger cut achieving conductance $h(G) = \phi(S^*)$.
Construct test vector $y \in \mathbb{R}^n$ with zero mean ($\sum_{u} y_u = 0$):
$$y_u = \begin{cases} |\bar{S}^*| & \text{if } u \in S^* \\ -|S^*| & \text{if } u \in \bar{S}^* \end{cases}$$
Compute the Rayleigh quotient:
1. Denominator:
   $$\sum_{u \in V} y_u^2 = |S^*| |\bar{S}^*|^2 + |\bar{S}^*| |S^*|^2 = |S^*| |\bar{S}^*| (|S^*| + |\bar{S}^*|) = n |S^*| |\bar{S}^*|$$
2. Numerator:
   Edges within $S^*$ or within $\bar{S}^*$ have $(y_u - y_v)^2 = 0$.
   Edges crossing the cut have $(y_u - y_v)^2 = (|\bar{S}^*| - (-|S^*|))^2 = (|S^*| + |\bar{S}^*|)^2 = n^2$.
   $$\sum_{(u, v) \in E} (y_u - y_v)^2 = |E(S^*, \bar{S}^*)| \cdot n^2$$
3. Evaluating the ratio:
   $$R_{\mathcal{L}}(y) = \frac{\frac{1}{d} |E(S^*, \bar{S}^*)| n^2}{n |S^*| |\bar{S}^*|} = \frac{|E(S^*, \bar{S}^*)|}{d |S^*|} \cdot \frac{n}{|\bar{S}^*|} = h(G) \left(1 + \frac{|S^*|}{|\bar{S}^*|}\right) \le 2 h(G)$$
   Because $\lambda_2 \le R_{\mathcal{L}}(y)$, this proves $\frac{\lambda_2}{2} \le h(G)$. $\blacksquare$

---

### 📄 Landmark Research Papers (from [[Paper Reading Hub|Paper Reading Hub]])

The following foundational paper from the [[Paper Reading Hub|Paper Reading Hub]] is assigned to Block 20. Analyze using the Keshav Three-Pass Methodology:

1. **"Nearly-Linear Time Algorithms for Graph Partitioning, Graph Sparsification, and Solving Linear Systems"** (Daniel A. Spielman & Shang-Hua Teng, 2004)
    - *Venue:* STOC '04 (Paper 14 in [[Paper Reading Hub|Paper Reading Hub]])
    - *Landmark Invariant:* Spectral graph theory breakthrough: solving symmetric diagonally dominant (SDD) linear systems in $\tilde{\mathcal{O}}(m \log^c n)$ time via Cheeger cuts.
    - *Reading Guidance:* Focus Pass 2 on the relationship between graph Laplacians, low-stretch spanning trees, and spectral sparsification via effective resistances.
