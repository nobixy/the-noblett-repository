---
title: "18 - Real Analysis — Worked Proofs"
type: reference
tags:
  - reference
  - answer-key
---

# 18 - Real Analysis — Worked Proofs

> [!WARNING] Answer key — open only after your own attempt
> These derivations were generated as reference material, not study notes. Reading them first creates the illusion of competence that [[how-i-study]] warns about.
> Protocol: attempt the proof from a blank sheet in [[B18 - Real Analysis|Real Analysis]] → compare here → log every gap you found.
> They are unverified; treat any step you cannot justify as a possible error, not as authority.

Back to: [[B18 - Real Analysis|Real Analysis]] · [[Worked Proofs Index]]

---

### 1. The Baire Category Theorem
**Theorem (Baire 1899):** In any complete metric space $(X, d)$, the intersection of any countable collection of dense open subsets is dense in $X$:
$$U_n \subseteq X \text{ open and dense for } n \in \mathbb{N} \implies \bigcap_{n=1}^\infty U_n \text{ is dense in } X$$

#### Proof via Nested Closed Balls:
Let $W \subseteq X$ be an arbitrary non-empty open set. We must show $W \cap \left( \bigcap_{n=1}^\infty U_n \right) \ne \emptyset$.
1. Since $U_1$ is dense, $W \cap U_1$ is a non-empty open set. Choose $x_1 \in W \cap U_1$ and radius $0 < r_1 < 1$ such that the closed ball $\overline{B}(x_1, r_1) \subseteq W \cap U_1$.
2. Inductively, suppose closed ball $\overline{B}(x_{n-1}, r_{n-1})$ has been chosen. Because $U_n$ is dense, the interior $B(x_{n-1}, r_{n-1}) \cap U_n$ is non-empty and open. Choose $x_n$ and radius $0 < r_n < \min(r_{n-1}/2, 1/n)$ such that:
   $$\overline{B}(x_n, r_n) \subseteq B(x_{n-1}, r_{n-1}) \cap U_n$$
3. By construction, for all $m \ge n$, $x_m \in \overline{B}(x_n, r_n)$, which implies $d(x_n, x_m) \le r_n < 1/n$.
   Since $r_n \to 0$, $(x_n)_{n \ge 1}$ is a Cauchy sequence in $X$.
4. By completeness of $(X, d)$, there exists a limit point $x^* = \lim_{n \to \infty} x_n \in X$.
5. For any fixed $k$, since $x_n \in \overline{B}(x_k, r_k)$ for all $n \ge k$ and closed balls are closed, $x^* \in \overline{B}(x_k, r_k) \subseteq U_k$.
6. Thus $x^* \in \bigcap_{n=1}^\infty U_n$. Furthermore, $x^* \in \overline{B}(x_1, r_1) \subseteq W$.
   Therefore $W \cap \left( \bigcap_{n=1}^\infty U_n \right) \ne \emptyset$, completing the proof. $\blacksquare$

---

### 2. Banach Fixed Point Theorem & Picard-Lindelöf Existence
**Theorem (Banach 1922):** Let $(X, d)$ be a non-empty complete metric space. Let $T : X \to X$ be a contraction mapping, i.e., there exists a constant $k \in [0, 1)$ such that for all $x, y \in X$:
$$d(T(x), T(y)) \le k \, d(x, y)$$
Then:
1. $T$ has a unique fixed point $x^* \in X$ ($T(x^*) = x^*$).
2. For any arbitrary starting point $x_0 \in X$, the Picard iteration sequence $x_{n+1} = T(x_n)$ converges to $x^*$:
   $$\lim_{n \to \infty} x_n = x^*, \quad \text{with error bound } d(x_n, x^*) \le \frac{k^n}{1 - k} d(x_0, x_1)$$

#### Application: Picard-Lindelöf Theorem for ODEs
Consider the initial value problem $\frac{dy}{dt} = f(t, y)$ with $y(t_0) = y_0$, where $f$ is continuous and Lipschitz in $y$: $|f(t, y_1) - f(t, y_2)| \le L |y_1 - y_2|$.
1. Formulate the equivalent integral equation:
   $$y(t) = y_0 + \int_{t_0}^t f(s, y(s)) \, ds$$
2. Define the Picard operator on the Banach space $C([t_0 - \delta, t_0 + \delta])$ equipped with the supremum norm $\|y\|_\infty = \sup_t |y(t)|$:
   $$T(y)(t) = y_0 + \int_{t_0}^t f(s, y(s)) \, ds$$
3. For sufficiently small time horizon $\delta < 1/L$, $T$ is a strict contraction:
   $$\|T(y_1) - T(y_2)\|_\infty \le \delta L \|y_1 - y_2\|_\infty$$
4. By the Banach Fixed Point Theorem, $T$ has a unique fixed point $y^*$, guaranteeing existence and uniqueness of the ODE trajectory. $\blacksquare$

---

### 3. The Arzelà-Ascoli Theorem
**Theorem:** Let $(K, d)$ be a compact metric space, and let $C(K)$ be the Banach space of continuous real-valued functions on $K$ with supremum norm $\|f\|_\infty = \sup_{x \in K} |f(x)|$.
A subset $\mathcal{F} \subset C(K)$ is relatively compact (its closure is compact in $C(K)$) if and only if $\mathcal{F}$ is:
1. **Pointwise Bounded:** For every $x \in K$, $\sup_{f \in \mathcal{F}} |f(x)| < \infty$.
2. **Equicontinuous:** For every $\epsilon > 0$, there exists $\delta > 0$ such that:
   $$\forall x, y \in K: d(x, y) < \delta \implies \forall f \in \mathcal{F}: |f(x) - f(y)| < \epsilon$$
*(Proof uses Cantor's diagonal argument on a countable dense subset of $K$ combined with the total boundedness of compact metric spaces).* $\blacksquare$
