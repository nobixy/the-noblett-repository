---
title: "13 - Algorithms I — Worked Proofs"
type: reference
tags:
  - reference
  - answer-key
---

# 13 - Algorithms I — Worked Proofs

> [!WARNING] Answer key — open only after your own attempt
> These derivations were generated as reference material, not study notes. Reading them first creates the illusion of competence that [[how-i-study]] warns about.
> Protocol: attempt the proof from a blank sheet in [[13 - Algorithms I]] → compare here → log every gap you found.
> They are unverified; treat any step you cannot justify as a possible error, not as authority.

Back to: [[13 - Algorithms I]] · [[Worked Proofs Index]]

---

### 1. The Akra-Bazzi Theorem for Divide-and-Conquer Recurrences
**Theorem (Akra & Bazzi 1998, Leighton 1996):** Consider the general divide-and-conquer recurrence:
$$T(x) = g(x) + \sum_{i=1}^k a_i T(b_i x + h_i(x)) \quad \text{for } x \ge x_0$$
where:
1. $a_i > 0$ and constants $b_i \in (0, 1)$.
2. Non-homogeneous driving function $g(x) \ge 0$ satisfies the polynomial growth condition: $|g'(x)| = \mathcal{O}(x^c)$ for some constant $c$.
3. Perturbation functions satisfy $|h_i(x)| = \mathcal{O}\left(\frac{x}{\log^2 x}\right)$ (accounting for floor/ceiling functions and uneven splits).

Let $p \in \mathbb{R}$ be the unique real number satisfying the characteristic equation:
$$\sum_{i=1}^k a_i b_i^p = 1$$

Then the asymptotic solution to the recurrence is given by:
$$T(x) = \Theta\left(x^p \left(1 + \int_1^x \frac{g(u)}{u^{p+1}} \, du\right)\right)$$

#### Mathematical Intuition & Proof Sketch:
1. **Uniqueness of $p$:**
   Define $f(s) = \sum_{i=1}^k a_i b_i^s$. Because $b_i \in (0, 1)$, $f(s)$ is strictly decreasing and continuous on $\mathbb{R}$, with $\lim_{s \to -\infty} f(s) = \infty$ and $\lim_{s \to \infty} f(s) = 0$. By the Intermediate Value Theorem, there exists a unique real $p$ such that $f(p) = 1$.
2. **Homogeneous Normalization:**
   Divide $T(x)$ by $x^p$ and substitute $u = \ln x$. The scaled recurrence satisfies:
   $$\frac{T(x)}{x^p} = \frac{g(x)}{x^p} + \sum_{i=1}^k a_i b_i^p \frac{T(b_i x)}{(b_i x)^p}$$
   Because $\sum_{i=1}^k a_i b_i^p = 1$, the linear combination on the right behaves as a convex combination (an expectation over scale shifts), converting the discrete recurrence into a continuous differential/integral equation.
3. **Integral Formulation:**
   Summing the non-homogeneous driving term across continuous recursion levels yields the integral $\int_1^x \frac{g(u)}{u^{p+1}} du$.
  - **Case 1 ($g(u) = \mathcal{O}(u^{p-\epsilon})$):** The integral converges to a constant $\mathcal{O}(1)$, yielding $T(x) = \Theta(x^p)$.
  - **Case 2 ($g(u) = \Theta(u^p \log^k u)$):** $\int_1^x \frac{u^p \log^k u}{u^{p+1}} du = \int_1^x \frac{\log^k u}{u} du = \Theta(\log^{k+1} x)$, yielding $T(x) = \Theta(x^p \log^{k+1} x)$.
  - **Case 3 ($g(u) = \Omega(u^{p+\epsilon})$):** The driving function dominates, yielding $T(x) = \Theta(g(x))$.

---

### 2. The Potential Method of Amortized Analysis
**Framework:** Let $D_0$ be the initial state of a data structure. A sequence of $n$ operations is performed, where operation $i$ transforms state $D_{i-1}$ to $D_i$ with actual cost $c_i$.

#### Definition & Fundamental Telescoping Theorem:
Define a potential function $\Phi : \mathcal{D} \to \mathbb{R}$ mapping any data structure state to a real number, satisfying the non-negativity condition:
$$\Phi(D_i) \ge \Phi(D_0) \quad \forall i \ge 1$$
The *amortized cost* $\hat{c}_i$ of the $i$-th operation with respect to $\Phi$ is defined as:
$$\hat{c}_i = c_i + \Phi(D_i) - \Phi(D_{i-1})$$

Summing over all $n$ operations:
$$\sum_{i=1}^n \hat{c}_i = \sum_{i=1}^n \left( c_i + \Phi(D_i) - \Phi(D_{i-1}) \right) = \sum_{i=1}^n c_i + \Phi(D_n) - \Phi(D_0)$$
Since $\Phi(D_n) - \Phi(D_0) \ge 0$, the total amortized cost constitutes a rigorous upper bound on the total actual cost:
$$\sum_{i=1}^n c_i \le \sum_{i=1}^n \hat{c}_i$$

#### Application 1: Dynamic Array Table Doubling
Consider a dynamic array that doubles its capacity when full upon inserting an element.
- Actual cost $c_i$: $c_i = 1$ if no resize occurs; $c_i = k + 1$ if resizing from size $k$ to $2k$.
- Choose potential function:
  $$\Phi(D) = 2 \cdot \text{size}(D) - \text{capacity}(D)$$
  Notice $\Phi(D_0) = 2(0) - 0 = 0$. Just after doubling (size $k$, capacity $2k$), $\Phi = 2k - 2k = 0 \ge 0$. Just before doubling (size $2k$, capacity $2k$), $\Phi = 4k - 2k = 2k > 0$. Thus $\Phi(D_i) \ge \Phi(D_0)$ always.

**Amortized Cost Calculation:**
- **Case A (No resize):** $\text{size}_i = \text{size}_{i-1} + 1$, $\text{capacity}_i = \text{capacity}_{i-1}$.
  $$\Delta \Phi = \Phi(D_i) - \Phi(D_{i-1}) = (2(\text{size}+1) - \text{cap}) - (2\,\text{size} - \text{cap}) = 2$$
  $$\hat{c}_i = c_i + \Delta \Phi = 1 + 2 = 3 = \mathcal{O}(1)$$
- **Case B (Resize from $k$ to $2k$):** $\text{size}_i = k+1$, $\text{capacity}_i = 2k$, actual cost $c_i = k+1$.
  $$\Phi(D_{i-1}) = 2k - k = k$$
  $$\Phi(D_i) = 2(k+1) - 2k = 2$$
  $$\Delta \Phi = 2 - k$$
  $$\hat{c}_i = c_i + \Delta \Phi = (k+1) + (2 - k) = 3 = \mathcal{O}(1)$$
Thus, every append operation runs in strictly $\mathcal{O}(1)$ amortized time. $\blacksquare$

---

### 📄 Landmark Research Papers (from [[03 - Papers/Paper Reading Hub|Paper Reading Hub]])

The following foundational paper from the [[03 - Papers/Paper Reading Hub|Paper Reading Hub]] is assigned to Block 13. Analyze using the Keshav Three-Pass Methodology:

1. **"Efficiency of a Good But Not Linear Set Union Algorithm"** (Robert E. Tarjan, 1975)
    - *Venue:* Journal of the ACM (Paper 13 in [[03 - Papers/Paper Reading Hub|Paper Reading Hub]])
    - *Landmark Invariant:* Tight amortized complexity bound $\mathcal{O}(m \alpha(n))$ for Disjoint Set Union with path compression and union-by-rank using potential methods.
    - *Reading Guidance:* Focus Pass 2 on the potential function based on the inverse Ackermann function $\alpha(n)$ and the rank grouping charging argument.
