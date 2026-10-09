---
title: "03 - Physics I — Worked Proofs"
type: reference
tags:
  - reference
  - answer-key
---

# 03 - Physics I — Worked Proofs

> [!WARNING] Answer key — open only after your own attempt
> These derivations were generated as reference material, not study notes. Reading them first creates the illusion of competence that [[how-i-study]] warns about.
> Protocol: attempt the proof from a blank sheet in [[B03 - Physics I|Physics I]] → compare here → log every gap you found.
> They are unverified; treat any step you cannot justify as a possible error, not as authority.

Back to: [[B03 - Physics I|Physics I]] · [[Worked Proofs Index]]

---

### Core Concepts & Derivations
- **Work-Energy Theorem:** $\Delta K = W_{\text{net}} = \int_{\mathbf{r}_1}^{\mathbf{r}_2} \mathbf{F}_{\text{net}} \cdot d\mathbf{r} = \int_{t_1}^{t_2} m \frac{d\mathbf{v}}{dt} \cdot \mathbf{v}\,dt = \frac{1}{2}m v_2^2 - \frac{1}{2}m v_1^2$.
- **Conservation of Angular Momentum:** $\boldsymbol{\tau}_{\text{net}} = \frac{d\mathbf{L}}{dt}$. When external torque vanishes, $\mathbf{L} = \mathbf{r} \times \mathbf{p} = \text{const}$.
- **Simple Harmonic Oscillator Equation:** Derivation of $\ddot{x} + \omega_0^2 x = 0$ with solution $x(t) = A \cos(\omega_0 t + \phi)$, where $\omega_0 = \sqrt{k/m}$.
- **Gravitational Central Force Invariants:** Keplerian orbital mechanics derived from conservation of mechanical energy and angular momentum in effective potential $U_{\text{eff}}(r) = -\frac{GMm}{r} + \frac{L^2}{2mr^2}$.

---

### 1. The Work-Kinetic Energy Theorem & Mechanical Energy Conservation
**Theorem:** For a particle of mass $m$ traversing a smooth spatial trajectory $\mathcal{C}$ parametrized by position vector $\mathbf{r}(t)$ from $t_1$ to $t_2$ under a net vector force $\mathbf{F}_{\text{net}}$:
1. The total line integral work performed on the particle equals the net change in its translational kinetic energy:
$$W_{\text{net}} = \int_{\mathcal{C}} \mathbf{F}_{\text{net}} \cdot d\mathbf{r} = \Delta K = \frac{1}{2}m v(t_2)^2 - \frac{1}{2}m v(t_1)^2$$
2. If $\mathbf{F}_{\text{net}}$ is conservative ($\nabla \times \mathbf{F}_{\text{net}} = \mathbf{0}$, such that $\mathbf{F}_{\text{net}} = -\nabla U(\mathbf{r})$ for scalar potential $U$), then total mechanical energy $E = K + U$ is a strict invariant of motion:
$$\frac{dE}{dt} = 0 \implies E(t_1) = E(t_2)$$

#### Step-by-Step Derivation & Proof:
1. **Newton's Second Law Formulation:**
   The particle's motion is governed by Newton's Second Law:
   $$\mathbf{F}_{\text{net}} = m \mathbf{a}(t) = m \frac{d\mathbf{v}}{dt}$$

2. **Parametric Differential Displacement:**
   The differential displacement along trajectory $\mathcal{C}$ is:
   $$d\mathbf{r} = \frac{d\mathbf{r}}{dt} dt = \mathbf{v}(t) \, dt$$

3. **Line Integral Transformation:**
   Substitute $\mathbf{F}_{\text{net}}$ and $d\mathbf{r}$ into the work line integral:
   $$W_{\text{net}} = \int_{\mathcal{C}} \mathbf{F}_{\text{net}} \cdot d\mathbf{r} = \int_{t_1}^{t_2} \left( m \frac{d\mathbf{v}}{dt} \right) \cdot \mathbf{v}(t) \, dt$$

4. **Vector Scalar Product Differentiation Identity:**
   Differentiating the scalar square of the velocity vector $v^2 = \mathbf{v} \cdot \mathbf{v}$:
   $$\frac{d}{dt} (v^2) = \frac{d}{dt} (\mathbf{v} \cdot \mathbf{v}) = \frac{d\mathbf{v}}{dt} \cdot \mathbf{v} + \mathbf{v} \cdot \frac{d\mathbf{v}}{dt} = 2 \mathbf{v} \cdot \frac{d\mathbf{v}}{dt}$$
   Rearranging yields the exact integrand identity:
   $$\left( \frac{d\mathbf{v}}{dt} \right) \cdot \mathbf{v} = \frac{1}{2} \frac{d}{dt}(v^2)$$

5. **Direct Integration of Kinetic Energy:**
   Substitute into the work integral:
   $$W_{\text{net}} = \int_{t_1}^{t_2} m \left( \frac{1}{2} \frac{d}{dt}(v^2) \right) dt = \frac{1}{2} m \int_{t_1}^{t_2} \frac{d}{dt}(v^2) \, dt = \frac{1}{2} m \left[ v(t_2)^2 - v(t_1)^2 \right]$$
   $$W_{\text{net}} = K_2 - K_1 = \Delta K$$

6. **Conservative Potential Integration:**
   If $\mathbf{F}_{\text{net}} = -\nabla U(\mathbf{r})$, the work done along trajectory $\mathcal{C}$ depends only on endpoints:
   $$W_{\text{net}} = \int_{\mathbf{r}(t_1)}^{\mathbf{r}(t_2)} (-\nabla U) \cdot d\mathbf{r} = -\int_{t_1}^{t_2} \left( \frac{\partial U}{\partial x} \frac{dx}{dt} + \frac{\partial U}{\partial y} \frac{dy}{dt} + \frac{\partial U}{\partial z} \frac{dz}{dt} \right) dt = -\int_{t_1}^{t_2} \frac{dU}{dt} dt = -(U_2 - U_1) = -\Delta U$$

7. **Conservation Invariant:**
   Equating the two expressions for $W_{\text{net}}$:
   $$\Delta K = -\Delta U \iff \Delta K + \Delta U = 0 \iff \Delta(K + U) = 0$$
   Defining total mechanical energy $E = K + U$:
   $$\frac{dE}{dt} = 0 \implies E(t) = \frac{1}{2} m v(t)^2 + U(\mathbf{r}(t)) = \text{constant} \quad \blacksquare$$
