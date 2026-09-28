---
title: "25 - Convex Optimization — Worked Proofs"
type: reference
tags:
  - reference
  - answer-key
---

# 25 - Convex Optimization — Worked Proofs

> [!WARNING] Answer key — open only after your own attempt
> These derivations were generated as reference material, not study notes. Reading them first creates the illusion of competence that [[how-i-study]] warns about.
> Protocol: attempt the proof from a blank sheet in [[25 - Convex Optimization]] → compare here → log every gap you found.
> They are unverified; treat any step you cannot justify as a possible error, not as authority.

Back to: [[25 - Convex Optimization]] · [[Worked Proofs Index]]

---

### Proof 1: Karush-Kuhn-Tucker (KKT) Optimality Conditions & Slater's Condition
**Theorem**: Consider the primal convex optimization problem:
$$\begin{aligned}
\text{minimize} \quad & f_0(x) \\
\text{subject to} \quad & f_i(x) \le 0, \quad i = 1, \dots, m \\
& A x = b
\end{aligned}$$
where $f_0, \dots, f_m: \mathbb{R}^n \to \mathbb{R}$ are convex and continuously differentiable, and $A \in \mathbb{R}^{p \times n}$ with $\text{rank}(A) = p$.
Assume **Slater's Constraint Qualification**: there exists an strictly feasible point $\tilde{x} \in \text{relint}(\mathcal{D})$ such that:
$$f_i(\tilde{x}) < 0, \quad i = 1, \dots, m \quad \text{and} \quad A \tilde{x} = b$$
Then strong duality holds ($p^* = d^*$), and a primal-dual pair $(x^*, (\lambda^*, \nu^*))$ is optimal if and only if the Karush-Kuhn-Tucker (KKT) conditions hold:
1. **Primal Feasibility**: $f_i(x^*) \le 0$ for $i=1,\dots,m$, and $A x^* = b$
2. **Dual Feasibility**: $\lambda_i^* \ge 0$ for $i=1,\dots,m$
3. **Complementary Slackness**: $\lambda_i^* f_i(x^*) = 0$ for $i=1,\dots,m$
4. **Stationarity**: $\nabla f_0(x^*) + \sum_{i=1}^m \lambda_i^* \nabla f_i(x^*) + A^T \nu^* = 0$

**Proof (Separating Hyperplane Theorem & Slater's Condition)**:
1. Define the set $\mathcal{A} \subset \mathbb{R}^{m} \times \mathbb{R}^p \times \mathbb{R}$:
   $$\mathcal{A} = \left\{ (u, v, t) : \exists x \in \mathcal{D}, \, f_i(x) \le u_i \, (i=1,\dots,m), \, A x - b = v, \, f_0(x) \le t \right\}$$
   Because $f_0, \dots, f_m$ are convex functions and affine constraints preserve convexity, $\mathcal{A}$ is a non-empty convex set.
2. Define the optimal primal value $p^* = \inf \{ f_0(x) : f_i(x) \le 0, \, Ax = b \}$.
   Define the second set $\mathcal{B} \subset \mathbb{R}^m \times \mathbb{R}^p \times \mathbb{R}$:
   $$\mathcal{B} = \{ (0, 0, s) : s < p^* \}$$
   $\mathcal{B}$ is convex and clearly disjoint from $\mathcal{A}$, because if $(0, 0, s) \in \mathcal{A}$ with $s < p^*$, there would exist a feasible $x$ with $f_0(x) \le s < p^*$, contradicting the minimality of $p^*$.
3. By the **Supporting / Separating Hyperplane Theorem**, there exists a non-zero hyperplane normal $(\tilde{\lambda}, \tilde{\nu}, \mu) \ne (0, 0, 0)$ and constant $\alpha$ such that:
   $$\forall (u, v, t) \in \mathcal{A}: \quad \tilde{\lambda}^T u + \tilde{\nu}^T v + \mu t \ge \alpha$$
   $$\forall (0, 0, s) \in \mathcal{B}: \quad \mu s \le \alpha$$
4. Since $s < p^*$ can be made arbitrarily negative, we must have $\mu \ge 0$ (otherwise $\mu s \to +\infty$).
   Similarly, because $u_i$ and $t$ can be increased arbitrarily within $\mathcal{A}$, we must have $\tilde{\lambda} \ge 0$ componentwise.
   Furthermore, taking $s \to p^*$, $\mu p^* \le \alpha$. Hence:
   $$\tilde{\lambda}^T u + \tilde{\nu}^T v + \mu t \ge \mu p^* \quad \forall (u, v, t) \in \mathcal{A}$$
   Substituting $(f_1(x), \dots, f_m(x), A x - b, f_0(x)) \in \mathcal{A}$:
   $$\sum_{i=1}^m \tilde{\lambda}_i f_i(x) + \tilde{\nu}^T (A x - b) + \mu f_0(x) \ge \mu p^* \quad \forall x \in \mathcal{D}$$
5. **We claim $\mu > 0$ under Slater's Condition**:
   Suppose for contradiction that $\mu = 0$. Then $(\tilde{\lambda}, \tilde{\nu}) \ne (0, 0)$, and:
   $$\sum_{i=1}^m \tilde{\lambda}_i f_i(x) + \tilde{\nu}^T (A x - b) \ge 0 \quad \forall x \in \mathcal{D}$$
   Evaluating this at the Slater point $\tilde{x}$ (where $A \tilde{x} = b$ and $f_i(\tilde{x}) < 0$):
   $$\sum_{i=1}^m \tilde{\lambda}_i f_i(\tilde{x}) \ge 0$$
   Since $\tilde{\lambda}_i \ge 0$ and $f_i(\tilde{x}) < 0$, each term $\tilde{\lambda}_i f_i(\tilde{x}) \le 0$. The sum can only be $\ge 0$ if $\tilde{\lambda}_i = 0$ for all $i=1,\dots,m$.
   If $\tilde{\lambda} = 0$, then $\tilde{\nu}^T (Ax - b) \ge 0$ for all $x \in \mathcal{D}$. Since $A$ has full rank and $\tilde{x} \in \text{relint}(\mathcal{D})$, this requires $\tilde{\nu} = 0$.
   This contradicts $(\tilde{\lambda}, \tilde{\nu}, \mu) \ne (0, 0, 0)$. Thus, $\mu > 0$.
6. Dividing by $\mu > 0$, define $\lambda^* = \tilde{\lambda}/\mu \ge 0$ and $\nu^* = \tilde{\nu}/\mu$:
   $$L(x, \lambda^*, \nu^*) = f_0(x) + \sum_{i=1}^m \lambda_i^* f_i(x) + {\nu^*}^T (A x - b) \ge p^* \quad \forall x \in \mathcal{D}$$
   Taking the infimum over $x$ yields $g(\lambda^*, \nu^*) \ge p^*$. Since weak duality guarantees $g(\lambda^*, \nu^*) \le p^*$, we have $g(\lambda^*, \nu^*) = p^*$, establishing **strong duality**.
7. At an optimal primal point $x^*$, $f_0(x^*) = p^*$, so:
   $$p^* = g(\lambda^*, \nu^*) \le L(x^*, \lambda^*, \nu^*) = f_0(x^*) + \sum_{i=1}^m \lambda_i^* f_i(x^*) \le p^*$$
   This forces $\sum_{i=1}^m \lambda_i^* f_i(x^*) = 0$. Since $\lambda_i^* \ge 0$ and $f_i(x^*) \le 0$, each term must be zero: $\lambda_i^* f_i(x^*) = 0$ (**Complementary Slackness**).
   Finally, $x^*$ minimizes the unconstrained convex function $x \mapsto L(x, \lambda^*, \nu^*)$, so its gradient must vanish at $x^*$:
   $$\nabla_x L(x^*, \lambda^*, \nu^*) = \nabla f_0(x^*) + \sum_{i=1}^m \lambda_i^* \nabla f_i(x^*) + A^T \nu^* = 0 \quad (\textbf{Stationarity}) \quad \blacksquare$$

---

### Proof 2: Nesterov's Accelerated Gradient $\Omega(1/k^2)$ Lower Complexity Bound
**Theorem (Nesterov 1983, 2004)**: For any first-order black-box optimization algorithm generating iterates $x_k \in x_0 + \text{span}\{\nabla f(x_0), \dots, \nabla f(x_{k-1})\}$, and for any iteration limit $1 \le k \le \frac{1}{2}(n-1)$, there exists an $L$-smooth convex function $f: \mathbb{R}^n \to \mathbb{R}$ such that:
$$f(x_k) - f^* \ge \frac{3 L \|x_0 - x^*\|_2^2}{32 (k + 1)^2}$$
Hence, the convergence rate $\mathcal{O}(1/k^2)$ achieved by Nesterov Accelerated Gradient (NAG) is information-theoretically optimal.

**Proof**:
1. **Nesterov's "Worst Function in the World"**:
   Consider the tridiagonal quadratic function on $\mathbb{R}^{2k+1}$:
   $$f(x) = \frac{L}{4} \left( \frac{1}{2} x_1^2 + \frac{1}{2} \sum_{i=1}^{2k} (x_i - x_{i+1})^2 + \frac{1}{2} x_{2k+1}^2 - x_1 \right) = \frac{L}{8} x^T A x - \frac{L}{4} e_1^T x$$
   where $A$ is the tridiagonal matrix:
   $$A = \begin{pmatrix} 2 & -1 & 0 & \dots & 0 \\ -1 & 2 & -1 & \dots & 0 \\ \vdots & \ddots & \ddots & \ddots & \vdots \\ 0 & \dots & -1 & 2 & -1 \\ 0 & \dots & 0 & -1 & 2 \end{pmatrix}$$
2. The eigenvalues of $A$ are $\lambda_i(A) = 2 - 2\cos\left(\frac{i\pi}{2k+2}\right) = 4\sin^2\left(\frac{i\pi}{4k+4}\right) \in (0, 4)$.
   Thus $\nabla^2 f(x) = \frac{L}{4} A \implies \|\nabla^2 f(x)\|_2 \le \frac{L}{4} \cdot 4 = L$. The function $f$ is convex and $L$-smooth.
3. **Krylov Subspace Property**:
   Start at $x_0 = 0$. The gradient at $x_0$ is $\nabla f(0) = -\frac{L}{4} e_1 \in \text{span}\{e_1\}$.
   By induction, since $A$ is tridiagonal, multiplying $A$ by any vector in $\text{span}\{e_1, \dots, e_i\}$ yields a vector in $\text{span}\{e_1, \dots, e_{i+1}\}$.
   Therefore, for any algorithm satisfying the first-order linear span assumption:
   $$x_k \in \text{span}\{\nabla f(x_0), \dots, \nabla f(x_{k-1})\} \subseteq \text{span}\{e_1, e_2, \dots, e_k\}$$
   Consequently, for all coordinates $j > k$, the $j$-th coordinate of $x_k$ must be identically zero: $(x_k)_j = 0$ for $j = k+1, \dots, 2k+1$.
4. **Analytical Minimizer**:
   Setting $\nabla f(x^*) = 0 \implies A x^* = e_1$.
   The exact solution to this linear recurrence $-(x^*)_{i-1} + 2(x^*)_i - (x^*)_{i+1} = 0$ with boundary conditions is:
   $$(x^*)_i = 1 - \frac{i}{2k+2}, \quad i = 1, \dots, 2k+1$$
5. Evaluating the minimum value $f^* = f(x^*)$:
   $$f^* = \frac{L}{8} (x^*)^T A x^* - \frac{L}{4} e_1^T x^* = -\frac{L}{8} (x^*)_1 = -\frac{L}{8} \left( 1 - \frac{1}{2k+2} \right)$$
6. Since $x_k$ has non-zero entries only up to index $k$, the best possible value $x_k$ can attain is the constrained minimum over $\mathbb{R}^k \times \{0\}^{k+1}$.
   By solving the subproblem on $\mathbb{R}^k$, the optimal value among all such vectors is:
   $$\min_{x \in \text{span}\{e_1,\dots,e_k\}} f(x) = -\frac{L}{8} \left( 1 - \frac{1}{k+1} \right)$$
7. Subtracting $f^*$:
   $$f(x_k) - f^* \ge -\frac{L}{8} \left( 1 - \frac{1}{k+1} \right) + \frac{L}{8} \left( 1 - \frac{1}{2k+2} \right) = \frac{L}{8} \left( \frac{1}{k+1} - \frac{1}{2(k+1)} \right) = \frac{L}{16 (k+1)}$$
   Now evaluate the initial distance $\|x_0 - x^*\|_2^2$:
   $$\|x^*\|_2^2 = \sum_{i=1}^{2k+1} \left( 1 - \frac{i}{2k+2} \right)^2 = \frac{1}{(2k+2)^2} \sum_{j=1}^{2k+1} j^2 = \frac{(2k+1)(2k+2)(4k+3)}{6 (2k+2)^2} < \frac{2k+2}{3}$$
   Thus $\|x_0 - x^*\|_2^2 \le \frac{2(k+1)}{3} \implies k+1 \ge \frac{3}{2} \frac{\|x_0 - x^*\|_2^2}{k+1}$.
   Substituting gives:
   $$f(x_k) - f^* \ge \frac{3 L \|x_0 - x^*\|_2^2}{32 (k+1)^2} \quad \blacksquare$$

---

### 📄 Landmark Research Papers (from [[03 - Papers/Paper Reading Hub|Paper Reading Hub]])

The following foundational paper from the [[03 - Papers/Paper Reading Hub|Paper Reading Hub]] is assigned to Block 25. Analyze using the Keshav Three-Pass Methodology:

1. **"Neural Ordinary Differential Equations"** (Ricky T. Q. Chen et al., 2018)
    - *Venue:* NeurIPS 2018 (Best Paper) (Paper 29 in [[03 - Papers/Paper Reading Hub|Paper Reading Hub]])
    - *Landmark Invariant:* Continuous-depth residual networks formulated as ODEs; adjoint sensitivity method for constant memory $\mathcal{O}(1)$ backpropagation.
    - *Reading Guidance:* Focus Pass 2 on the continuous adjoint state dynamics $a(t) = \frac{\partial L}{\partial z(t)}$ and the instantaneous change of variables formula for continuous normalizing flows.
