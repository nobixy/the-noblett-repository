---
title: "04a - Differential Equations Bridge — Worked Proofs"
type: reference
tags:
  - reference
  - answer-key
---

# 04a - Differential Equations Bridge — Worked Proofs

> [!WARNING] Answer key — open only after your own attempt
> These derivations were generated as reference material, not study notes. Reading them first creates the illusion of competence that [[how-i-study]] warns about.
> Protocol: attempt the proof from a blank sheet in [[04a - Differential Equations Bridge]] → compare here → log every gap you found.
> They are unverified; treat any step you cannot justify as a possible error, not as authority.

Back to: [[04a - Differential Equations Bridge]] · [[Worked Proofs Index]]

---

### 1. Abel's Theorem on the Wronskian
**Theorem:** Let $I \subseteq \mathbb{R}$ be an open interval, and let $p, q: I \to \mathbb{R}$ be continuous functions. Consider the second-order linear homogeneous ordinary differential equation:
$$y'' + p(t)y' + q(t)y = 0$$
Let $y_1(t)$ and $y_2(t)$ be any two solutions of this equation on $I$. The Wronskian determinant $W(y_1, y_2)(t)$ defined by:
$$W(t) = W(y_1, y_2)(t) = \det \begin{pmatrix} y_1(t) & y_2(t) \\ y_1'(t) & y_2'(t) \end{pmatrix} = y_1(t) y_2'(t) - y_1'(t) y_2(t)$$
satisfies the first-order differential equation:
$$\frac{dW}{dt} + p(t) W(t) = 0$$
Consequently, for any fixed initial point $t_0 \in I$, the Wronskian is given by Abel's Formula:
$$W(t) = W(t_0) \exp\left( -\int_{t_0}^t p(s) \, ds \right)$$
Hence, $W(t)$ is either identically zero for all $t \in I$ or never zero for any $t \in I$. Furthermore, $y_1$ and $y_2$ form a fundamental set of solutions (i.e., are linearly independent) if and only if $W(t) \neq 0$ on $I$.

#### Mathematical Derivation:
1. **Differentiating the Wronskian Determinant:**
   Compute the derivative of $W(t) = y_1(t) y_2'(t) - y_1'(t) y_2(t)$ with respect to $t$ using the product rule:
   $$W'(t) = \frac{d}{dt}\left[y_1(t) y_2'(t) - y_1'(t) y_2(t)\right] = y_1'(t) y_2'(t) + y_1(t) y_2''(t) - \left[ y_1''(t) y_2(t) + y_1'(t) y_2'(t) \right]$$
   The product rule cross-terms $y_1'(t) y_2'(t)$ cancel identically, leaving:
   $$W'(t) = y_1(t) y_2''(t) - y_1''(t) y_2(t)$$

2. **Substituting the Governing Differential Equation:**
   Since $y_1$ and $y_2$ are both solutions to $y'' + p(t)y' + q(t)y = 0$, isolate their second derivatives:
   $$y_1''(t) = -p(t) y_1'(t) - q(t) y_1(t)$$
   $$y_2''(t) = -p(t) y_2'(t) - q(t) y_2(t)$$
   Substitute these expressions into the simplified derivative $W'(t)$:
   $$W'(t) = y_1(t) \Big(-p(t) y_2'(t) - q(t) y_2(t)\Big) - \Big(-p(t) y_1'(t) - q(t) y_1(t)\Big) y_2(t)$$
   Collect like coefficients of $p(t)$ and $q(t)$:
   $$W'(t) = -p(t) \Big(y_1(t) y_2'(t) - y_1'(t) y_2(t)\Big) - q(t) \Big(y_1(t) y_2(t) - y_1(t) y_2(t)\Big)$$
   The coefficient of $q(t)$ is identically zero ($y_1 y_2 - y_1 y_2 = 0$). Recognizing the Wronskian $W(t) = y_1 y_2' - y_1' y_2$:
   $$W'(t) = -p(t) W(t) \iff \frac{dW}{dt} + p(t) W(t) = 0$$

3. **Integration via Integrating Factor:**
   Define the integrating factor $\mu(t) = \exp\left(\int_{t_0}^t p(s) \, ds\right)$. Multiplying the differential equation by $\mu(t)$:
   $$\mu(t) W'(t) + p(t) \mu(t) W(t) = 0 \implies \frac{d}{dt} \Big[ \mu(t) W(t) \Big] = 0$$
   Integrating from $t_0$ to $t$:
   $$\mu(t) W(t) - \mu(t_0) W(t_0) = 0$$
   Because $\mu(t_0) = \exp(0) = 1$, solving for $W(t)$ yields:
   $$W(t) = W(t_0) [\mu(t)]^{-1} = W(t_0) \exp\left( -\int_{t_0}^t p(s) \, ds \right)$$

4. **Linear Independence Dichotomy:**
   Since $p(s)$ is continuous on $I$, the integral $\int_{t_0}^t p(s) ds$ is finite for every $t \in I$. The exponential function satisfies $\exp(u) > 0$ for all real $u \in \mathbb{R}$.
   Consequently:
  - If $W(t_0) = 0$, then $W(t) = 0$ for all $t \in I$.
  - If $W(t_0) \neq 0$, then $W(t) \neq 0$ for all $t \in I$.
   If $y_1, y_2$ are linearly dependent ($c_1 y_1 + c_2 y_2 = 0$ with $(c_1, c_2) \neq (0,0)$), differentiating yields $c_1 y_1' + c_2 y_2' = 0$. The determinant of this system is $W(t)$, which must vanish. Conversely, if $W(t_0) = 0$, the system $\begin{pmatrix} y_1(t_0) & y_2(t_0) \\ y_1'(t_0) & y_2'(t_0) \end{pmatrix} \begin{pmatrix} c_1 \\ c_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$ admits a non-trivial solution, producing a linear combination satisfying zero initial conditions, which by Picard-Lindelöf is identically zero. Thus $W(t) \neq 0$ on $I$ is equivalent to linear independence. $\blacksquare$

---

### 2. Matrix Exponential Solution to First-Order Linear Systems
**Theorem:** Let $A \in \mathbb{C}^{n \times n}$ be a constant matrix, and let $\mathbf{x}_0 \in \mathbb{C}^n$ and $t_0 \in \mathbb{R}$. The initial value problem:
$$\mathbf{\dot{x}}(t) = A \mathbf{x}(t), \quad \mathbf{x}(t_0) = \mathbf{x}_0$$
has a unique global solution defined for all $t \in \mathbb{R}$, given explicitly by:
$$\mathbf{x}(t) = e^{A(t - t_0)} \mathbf{x}_0$$
where the matrix exponential $e^{At}: \mathbb{R} \to \mathbb{C}^{n \times n}$ is defined by the power series:
$$e^{At} = \sum_{k=0}^\infty \frac{A^k t^k}{k!} = I + A t + \frac{A^2 t^2}{2!} + \frac{A^3 t^3}{3!} + \dots$$
Furthermore, $\frac{d}{dt} e^{At} = A e^{At} = e^{At} A$.

#### Mathematical Derivation:
1. **Convergence of the Matrix Power Series:**
   Let $\|\cdot\|$ be a submultiplicative matrix operator norm on $\mathbb{C}^{n \times n}$ (such that $\|MN\| \le \|M\| \|N\|$).
   For any fixed $T > 0$ and any $t \in [-T, T]$:
   $$\sum_{k=0}^\infty \left\| \frac{A^k t^k}{k!} \right\| \le \sum_{k=0}^\infty \frac{\|A\|^k |t|^k}{k!} \le \sum_{k=0}^\infty \frac{(\|A\| T)^k}{k!} = e^{\|A\| T} < \infty$$
   By the Weierstrass M-test on the Banach space $(\mathbb{C}^{n \times n}, \|\cdot\|)$, the series converges absolutely and uniformly on any compact interval $[-T, T]$. Hence $e^{At}$ is well-defined, continuous, and entire for all $t \in \mathbb{R}$.

2. **Term-by-Term Differentiation:**
   Because the formal term-by-term derivative series converges uniformly on compact sets, we can interchange differentiation and summation:
   $$\frac{d}{dt} e^{At} = \frac{d}{dt} \sum_{k=0}^\infty \frac{A^k t^k}{k!} = \sum_{k=1}^\infty \frac{A^k \cdot k t^{k-1}}{k!} = \sum_{k=1}^\infty \frac{A^k t^{k-1}}{(k-1)!}$$
   Re-indexing the summation using $m = k - 1 \ge 0$:
   $$\frac{d}{dt} e^{At} = \sum_{m=0}^\infty \frac{A^{m+1} t^m}{m!} = A \left( \sum_{m=0}^\infty \frac{A^m t^m}{m!} \right) = A e^{At}$$
   Since $A$ commutes with every power $A^m$, factoring $A$ on the right yields identically:
   $$\frac{d}{dt} e^{At} = \left( \sum_{m=0}^\infty \frac{A^m t^m}{m!} \right) A = e^{At} A$$

3. **Verification of the Initial Value Problem:**
   Evaluate $\mathbf{x}(t) = e^{A(t - t_0)} \mathbf{x}_0$ at $t = t_0$:
   $$\mathbf{x}(t_0) = e^{A(0)} \mathbf{x}_0 = I \mathbf{x}_0 = \mathbf{x}_0$$
   Differentiating $\mathbf{x}(t)$ with respect to $t$:
   $$\mathbf{\dot{x}}(t) = \frac{d}{dt} \left[ e^{A(t - t_0)} \right] \mathbf{x}_0 = A e^{A(t - t_0)} \mathbf{x}_0 = A \mathbf{x}(t)$$
   Thus $\mathbf{x}(t) = e^{A(t - t_0)}\mathbf{x}_0$ is a valid trajectory.

4. **Proof of Uniqueness:**
   Let $\mathbf{y}(t)$ be an arbitrary solution satisfying $\mathbf{\dot{y}}(t) = A \mathbf{y}(t)$ and $\mathbf{y}(t_0) = \mathbf{x}_0$. Consider the auxiliary vector function:
   $$\mathbf{z}(t) = e^{-A(t - t_0)} \mathbf{y}(t)$$
   Differentiating $\mathbf{z}(t)$ using the product rule:
   $$\mathbf{\dot{z}}(t) = \left( \frac{d}{dt} e^{-A(t - t_0)} \right) \mathbf{y}(t) + e^{-A(t - t_0)} \mathbf{\dot{y}}(t)$$
   Using $\frac{d}{dt} e^{-A(t - t_0)} = -e^{-A(t - t_0)} A$ and $\mathbf{\dot{y}}(t) = A \mathbf{y}(t)$:
   $$\mathbf{\dot{z}}(t) = -e^{-A(t - t_0)} A \mathbf{y}(t) + e^{-A(t - t_0)} A \mathbf{y}(t) = \mathbf{0}$$
   Since its derivative vanishes identically on $\mathbb{R}$, $\mathbf{z}(t)$ is constant:
   $$\mathbf{z}(t) = \mathbf{z}(t_0) = e^0 \mathbf{y}(t_0) = I \mathbf{x}_0 = \mathbf{x}_0$$
   Multiplying both sides by $e^{A(t - t_0)}$ and observing $e^{A(t - t_0)} e^{-A(t - t_0)} = I$:
   $$\mathbf{y}(t) = e^{A(t - t_0)} \mathbf{z}(t) = e^{A(t - t_0)} \mathbf{x}_0 = \mathbf{x}(t)$$
   Therefore, the solution $\mathbf{x}(t) = e^{A(t - t_0)}\mathbf{x}_0$ is strictly unique. $\blacksquare$

---

### 3. Picard-Lindelöf Existence and Uniqueness Theorem
**Theorem:** Consider the initial value problem:
$$\mathbf{\dot{x}}(t) = \mathbf{f}(t, \mathbf{x}(t)), \quad \mathbf{x}(t_0) = \mathbf{x}_0$$
Let $R = [t_0 - a, t_0 + a] \times \bar{B}(\mathbf{x}_0, b) \subset \mathbb{R} \times \mathbb{R}^n$ be a closed cylinder, where $\bar{B}(\mathbf{x}_0, b) = \{\mathbf{x} \in \mathbb{R}^n : \|\mathbf{x} - \mathbf{x}_0\| \le b\}$.
Suppose:
1. $\mathbf{f}: R \to \mathbb{R}^n$ is continuous on $R$, so by compactness $M = \sup_{(t, \mathbf{x}) \in R} \|\mathbf{f}(t, \mathbf{x})\| < \infty$.
2. $\mathbf{f}$ satisfies a uniform Lipschitz condition in $\mathbf{x}$ on $R$:
   $$\|\mathbf{f}(t, \mathbf{x}) - \mathbf{f}(t, \mathbf{y})\| \le L \|\mathbf{x} - \mathbf{y}\| \quad \forall (t, \mathbf{x}), (t, \mathbf{y}) \in R$$
Choose time radius $h > 0$ such that $h < \min\left(a, \frac{b}{M}, \frac{1}{L}\right)$.
Then there exists a unique continuously differentiable solution $\mathbf{x}: [t_0 - h, t_0 + h] \to \bar{B}(\mathbf{x}_0, b)$ satisfying the initial value problem.

#### Mathematical Derivation:
1. **Volterra Integral Formulation:**
   By the Fundamental Theorem of Calculus, a continuous function $\mathbf{x}(t)$ satisfies $\mathbf{\dot{x}}(t) = \mathbf{f}(t, \mathbf{x}(t))$ with $\mathbf{x}(t_0) = \mathbf{x}_0$ if and only if it satisfies the fixed-point integral equation:
   $$\mathbf{x}(t) = \mathbf{x}_0 + \int_{t_0}^t \mathbf{f}(s, \mathbf{x}(s)) \, ds$$

2. **Banach Space Construction:**
   Let $I = [t_0 - h, t_0 + h]$. Consider the Banach space $X = C(I, \mathbb{R}^n)$ equipped with the uniform (supremum) norm:
   $$\|\mathbf{x}\|_\infty = \sup_{t \in I} \|\mathbf{x}(t)\|$$
   Define the closed subset:
   $$S = \left\{ \mathbf{x} \in X : \|\mathbf{x} - \mathbf{x}_0\|_\infty \le b \right\}$$
   Since $S$ is a closed subset of the complete metric space $(X, \|\cdot\|_\infty)$, $(S, d_\infty)$ is itself a complete metric space.

3. **Invariance of the Picard Operator:**
   Define the Picard integral operator $T$ on $S$ by:
   $$(T\mathbf{x})(t) = \mathbf{x}_0 + \int_{t_0}^t \mathbf{f}(s, \mathbf{x}(s)) \, ds, \quad t \in I$$
   For any $\mathbf{x} \in S$ and $s \in I$, $\|\mathbf{x}(s) - \mathbf{x}_0\| \le b$, so $(s, \mathbf{x}(s)) \in R$ and $\|\mathbf{f}(s, \mathbf{x}(s))\| \le M$.
   Evaluating the deviation from $\mathbf{x}_0$ for any $t \in I$:
   $$\|(T\mathbf{x})(t) - \mathbf{x}_0\| = \left\| \int_{t_0}^t \mathbf{f}(s, \mathbf{x}(s)) \, ds \right\| \le \left| \int_{t_0}^t \|\mathbf{f}(s, \mathbf{x}(s))\| \, ds \right| \le M |t - t_0| \le M h$$
   Since $h \le \frac{b}{M}$, we have $\|(T\mathbf{x})(t) - \mathbf{x}_0\| \le M \left(\frac{b}{M}\right) = b$.
   Taking the supremum over $t \in I$ gives $\|T\mathbf{x} - \mathbf{x}_0\|_\infty \le b$.
   Furthermore, $(T\mathbf{x})(t)$ is continuous on $I$. Thus $T$ maps $S$ into $S$ ($T(S) \subseteq S$).

4. **Contraction Property:**
   Let $\mathbf{u}, \mathbf{v} \in S$. For any $t \in I$:
   $$\|(T\mathbf{u})(t) - (T\mathbf{v})(t)\| = \left\| \int_{t_0}^t \Big( \mathbf{f}(s, \mathbf{u}(s)) - \mathbf{f}(s, \mathbf{v}(s)) \Big) \, ds \right\| \le \left| \int_{t_0}^t \big\| \mathbf{f}(s, \mathbf{u}(s)) - \mathbf{f}(s, \mathbf{v}(s)) \big\| \, ds \right|$$
   Applying the Lipschitz bound:
   $$\|(T\mathbf{u})(t) - (T\mathbf{v})(t)\| \le L \left| \int_{t_0}^t \|\mathbf{u}(s) - \mathbf{v}(s)\| \, ds \right| \le L \|\mathbf{u} - \mathbf{v}\|_\infty |t - t_0| \le L h \|\mathbf{u} - \mathbf{v}\|_\infty$$
   Taking the supremum over all $t \in I$:
   $$\|T\mathbf{u} - T\mathbf{v}\|_\infty \le (L h) \|\mathbf{u} - \mathbf{v}\|_\infty$$
   Since $h < \frac{1}{L}$, the constant $k = L h < 1$.
   Therefore, $T: S \to S$ is a strict contraction on the complete metric space $(S, d_\infty)$.

5. **Banach Fixed-Point Theorem Conclusion:**
   By the Banach Fixed-Point Theorem, $T$ has a unique fixed point $\mathbf{x}^* \in S$ satisfying:
   $$T\mathbf{x}^* = \mathbf{x}^* \iff \mathbf{x}^*(t) = \mathbf{x}_0 + \int_{t_0}^t \mathbf{f}(s, \mathbf{x}^*(s)) \, ds$$
   By the Fundamental Theorem of Calculus, $\mathbf{x}^*(t)$ is continuously differentiable on $I$ with $\mathbf{\dot{x}}^*(t) = \mathbf{f}(t, \mathbf{x}^*(t))$ and $\mathbf{x}^*(t_0) = \mathbf{x}_0$. This establishes existence and uniqueness on $[t_0 - h, t_0 + h]$. $\blacksquare$
