---
title: "02 - Calculus I — Worked Proofs"
type: reference
tags:
  - reference
  - answer-key
---

# 02 - Calculus I — Worked Proofs

> [!WARNING] Answer key — open only after your own attempt
> These derivations were generated as reference material, not study notes. Reading them first creates the illusion of competence that [[how-i-study]] warns about.
> Protocol: attempt the proof from a blank sheet in [[02 - Calculus I]] → compare here → log every gap you found.
> They are unverified; treat any step you cannot justify as a possible error, not as authority.

Back to: [[02 - Calculus I]] · [[Worked Proofs Index]]

---

### Core Concepts & Derivations
- **Fundamental Theorem of Calculus (Parts 1 & 2):** If $f$ is continuous on $[a, b]$ and $F(x) = \int_a^x f(t)\,dt$, then $F'(x) = f(x)$. Furthermore, $\int_a^b f(x)\,dx = F(b) - F(a)$ where $F' = f$.
- **Mean Value Theorem:** If $f \in C[a, b]$ and differentiable on $(a, b)$, then $\exists c \in (a, b)$ such that $f'(c) = \frac{f(b) - f(a)}{b - a}$.
- **Taylor Remainder Bound:** Derivation of Lagrange remainder $R_n(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}(x - c)^{n+1}$ via Cauchy's Generalized Mean Value Theorem.
- **Riemann Integrability:** Upper and lower Darboux sums satisfying $U(f, P) - L(f, P) < \epsilon$ for sufficiently fine partitions $P$.

---

### 1. The Fundamental Theorem of Calculus (FTC Parts 1 & 2)
**Theorem (FTC 1 — Derivative of Accumulation Function):** Let $f: [a, b] \to \mathbb{R}$ be continuous on $[a, b]$. Define the accumulation function $F: [a, b] \to \mathbb{R}$ by:
$$F(x) = \int_a^x f(t)\,dt$$
Then $F$ is continuous on $[a, b]$, differentiable on $(a, b)$, and for every $x \in (a, b)$:
$$F'(x) = f(x)$$

**Theorem (FTC 2 — Evaluation Theorem):** If $g: [a, b] \to \mathbb{R}$ is differentiable on $(a, b)$ with continuous derivative $g'(x) = f(x)$ on $[a, b]$, then:
$$\int_a^b f(t)\,dt = g(b) - g(a)$$

#### Step-by-Step Derivation & Proof:
1. **Difference Quotient Formation (FTC 1):**
   Fix $x \in (a, b)$. For any $h \ne 0$ such that $x + h \in [a, b]$, form the Newton difference quotient:
   $$\frac{F(x+h) - F(x)}{h} = \frac{1}{h} \left( \int_a^{x+h} f(t)\,dt - \int_a^x f(t)\,dt \right) = \frac{1}{h} \int_x^{x+h} f(t)\,dt$$

2. **Integral Mean Value Bounds:**
   Since $f$ is continuous on the compact interval $I_h = [\min(x, x+h), \max(x, x+h)]$, by the Extreme Value Theorem, $f$ attains a minimum $m_h = \min_{t \in I_h} f(t)$ and a maximum $M_h = \max_{t \in I_h} f(t)$.
   By the monotonicity of the Riemann integral:
   $$m_h \cdot h \le \int_x^{x+h} f(t)\,dt \le M_h \cdot h \quad (\text{for } h > 0)$$
   Dividing through by $h$:
   $$m_h \le \frac{1}{h} \int_x^{x+h} f(t)\,dt \le M_h$$
   (An identical bound holds with reversed inequality signs when $h < 0$, preserved upon dividing by $h$).

3. **Limit Evaluation via Squeeze Theorem:**
   Because $f$ is continuous at $x$, for any $\epsilon > 0$, there exists $\delta > 0$ such that $|t - x| < \delta \implies |f(t) - f(x)| < \epsilon$.
   For $0 < |h| < \delta$, every point $t \in I_h$ satisfies $|t - x| < \delta$. Consequently:
   $$f(x) - \epsilon < m_h \le \frac{F(x+h) - F(x)}{h} \le M_h < f(x) + \epsilon$$
   Taking the limit as $h \to 0$:
   $$\lim_{h \to 0} m_h = \lim_{h \to 0} M_h = f(x) \implies F'(x) = \lim_{h \to 0} \frac{F(x+h) - F(x)}{h} = f(x)$$
   This proves FTC 1.

4. **Derivation of FTC 2:**
   Let $g(x)$ be any antiderivative of $f$ on $[a, b]$, so $g'(x) = f(x)$.
   Define the auxiliary function $H(x) = F(x) - g(x)$ on $[a, b]$.
   For all $x \in (a, b)$:
   $$H'(x) = F'(x) - g'(x) = f(x) - f(x) = 0$$
   By the Mean Value Theorem, any function whose derivative vanishes identically on an interval is constant: $\exists C \in \mathbb{R}$ such that $H(x) = C$ for all $x \in [a, b]$.
   Evaluating at $x = a$:
   $$C = H(a) = F(a) - g(a) = \int_a^a f(t)\,dt - g(a) = 0 - g(a) = -g(a)$$
   Now evaluate at $x = b$:
   $$H(b) = F(b) - g(b) = C \implies F(b) - g(b) = -g(a) \implies F(b) = g(b) - g(a)$$
   Substituting the definition $F(b) = \int_a^b f(t)\,dt$:
   $$\int_a^b f(t)\,dt = g(b) - g(a) \quad \blacksquare$$
