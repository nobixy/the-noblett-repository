---
title: "07 - Multivariable Calculus — Worked Proofs"
type: reference
tags:
  - reference
  - answer-key
---

# 07 - Multivariable Calculus — Worked Proofs

> [!WARNING] Answer key — open only after your own attempt
> These derivations were generated as reference material, not study notes. Reading them first creates the illusion of competence that [[how-i-study]] warns about.
> Protocol: attempt the proof from a blank sheet in [[07 - Multivariable Calculus]] → compare here → log every gap you found.
> They are unverified; treat any step you cannot justify as a possible error, not as authority.

Back to: [[07 - Multivariable Calculus]] · [[Worked Proofs Index]]

---

### Core Concepts & Derivations
- **Gradient Vector & Directional Derivative:** $\nabla f(\mathbf{x}) = \left(\frac{\partial f}{\partial x_1}, \dots, \frac{\partial f}{\partial x_n}\right)^T$; directional derivative $D_{\mathbf{u}} f = \nabla f \cdot \mathbf{u} = \|\nabla f\| \cos\theta$, maximized when $\mathbf{u} = \frac{\nabla f}{\|\nabla f\|}$.
- **Lagrange Multipliers for Constrained Extrema:** At a local extremum of $f(\mathbf{x})$ subject to $g(\mathbf{x}) = c$, the gradient of $f$ is collinear with the gradient of the constraint surface: $\nabla f(\mathbf{x}) = \lambda \nabla g(\mathbf{x})$.
- **Change of Variables & Jacobian Determinant:** $dx\,dy = |\det J|\,du\,dv$ where $J = \frac{\partial(x, y)}{\partial(u, v)}$ represents the infinitesimal local linear area transformation ratio.
- **Green's, Stokes', and Divergence Theorems:** The unifying generalized Stokes' theorem $\int_{\partial \Omega} \omega = \int_\Omega d\omega$, linking boundary flux and circulation to interior divergence ($\nabla \cdot \mathbf{F}$) and curl ($\nabla \times \mathbf{F}$).

---

### 1. Green's Theorem in the Plane
**Theorem (Green, 1828):** Let $D \subset \mathbb{R}^2$ be a bounded, simply connected planar region whose boundary $C = \partial D$ consists of a piecewise smooth, simple closed curve oriented counterclockwise (positively oriented). Let $\mathbf{F}(x, y) = P(x, y)\mathbf{i} + Q(x, y)\mathbf{j}$ be a vector field where partial derivatives $\frac{\partial P}{\partial y}$ and $\frac{\partial Q}{\partial x}$ exist and are continuous on an open domain containing $D$. Then:
$$\oint_C (P\,dx + Q\,dy) = \iint_D \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA$$

#### Step-by-Step Derivation & Proof:
1. **Decomposition into Orthogonal Vector Components:**
   We decompose the identity into two independent scalar equalities:
   $$\oint_C P\,dx = -\iint_D \frac{\partial P}{\partial y}\,dA \qquad \text{and} \qquad \oint_C Q\,dy = \iint_D \frac{\partial Q}{\partial x}\,dA$$
   Adding these two equalities directly yields Green's Theorem.

2. **Proof of First Component on a Vertically Simple (Type I) Region:**
   Let $D$ be a Type I region bounded by continuous curves:
   $$D = \{(x, y) \in \mathbb{R}^2 \mid a \le x \le b, \, g_1(x) \le y \le g_2(x)\}$$
   Compute the double integral using Fubini's theorem:
   $$\iint_D \frac{\partial P}{\partial y}\,dA = \int_a^b \left( \int_{g_1(x)}^{g_2(x)} \frac{\partial P}{\partial y}(x, y)\,dy \right) dx$$

3. **Evaluation via the Single-Variable Fundamental Theorem of Calculus:**
   Evaluating the inner integral:
   $$\int_{g_1(x)}^{g_2(x)} \frac{\partial P}{\partial y}(x, y)\,dy = P(x, g_2(x)) - P(x, g_1(x))$$
   Substituting into the outer integral:
   $$\iint_D \frac{\partial P}{\partial y}\,dA = \int_a^b P(x, g_2(x))\,dx - \int_a^b P(x, g_1(x))\,dx$$

4. **Line Integral Evaluation Around the Boundary $C = \partial D$:**
   The closed curve $C$ decomposes into four smooth directed paths $C = C_1 \cup C_2 \cup C_3 \cup C_4$:
  - $C_1$ (bottom): $y = g_1(x)$ traversed from $x = a$ to $x = b$. $\int_{C_1} P\,dx = \int_a^b P(x, g_1(x))\,dx$.
  - $C_2$ (right edge): $x = b$ is constant, so $dx = 0$. $\int_{C_2} P\,dx = 0$.
  - $C_3$ (top): $y = g_2(x)$ traversed from $x = b$ to $x = a$. $\int_{C_3} P\,dx = \int_b^a P(x, g_2(x))\,dx = -\int_a^b P(x, g_2(x))\,dx$.
  - $C_4$ (left edge): $x = a$ is constant, so $dx = 0$. $\int_{C_4} P\,dx = 0$.
   Summing the four paths:
   $$\oint_C P\,dx = \int_a^b P(x, g_1(x))\,dx - \int_a^b P(x, g_2(x))\,dx = -\iint_D \frac{\partial P}{\partial y}\,dA$$

5. **Proof of Second Component on a Horizontally Simple (Type II) Region:**
   Let $D$ be a Type II region: $D = \{(x, y) \in \mathbb{R}^2 \mid c \le y \le d, \, h_1(y) \le x \le h_2(y)\}$.
   $$\iint_D \frac{\partial Q}{\partial x}\,dA = \int_c^d \left( \int_{h_1(y)}^{h_2(y)} \frac{\partial Q}{\partial x}(x, y)\,dx \right) dy = \int_c^d \left( Q(h_2(y), y) - Q(h_1(y), y) \right) dy$$
   Parametrizing the boundary oriented counterclockwise gives identically:
   $$\oint_C Q\,dy = \iint_D \frac{\partial Q}{\partial x}\,dA$$

6. **Generalization to Regular Planar Domains:**
   Any piecewise smooth planar domain $D$ can be partitioned into a finite union of regions $D = \bigcup_{k=1}^m D_k$ that are simultaneously Type I and Type II.
   Across internal shared dividing boundaries, the line integrals run in opposite directions and cancel out identically ($\int_{C_{ij}} + \int_{C_{ji}} = 0$).
   The sum of boundary line integrals reduces to the external boundary $C = \partial D$:
   $$\oint_C (P\,dx + Q\,dy) = \sum_{k=1}^m \oint_{\partial D_k} (P\,dx + Q\,dy) = \sum_{k=1}^m \iint_{D_k} \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA = \iint_D \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA \quad \blacksquare$$
