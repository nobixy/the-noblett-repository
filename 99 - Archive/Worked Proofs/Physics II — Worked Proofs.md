---
title: "08 - Physics II — Worked Proofs"
type: reference
tags:
  - reference
  - answer-key
---

# 08 - Physics II — Worked Proofs

> [!WARNING] Answer key — open only after your own attempt
> These derivations were generated as reference material, not study notes. Reading them first creates the illusion of competence that [[how-i-study]] warns about.
> Protocol: attempt the proof from a blank sheet in [[B08 - Physics II|Physics II]] → compare here → log every gap you found.
> They are unverified; treat any step you cannot justify as a possible error, not as authority.

Back to: [[B08 - Physics II|Physics II]] · [[Worked Proofs Index]]

---

### Core Concepts & Derivations
- **Gauss's Law & Electrostatic Potential:** $\oint_{\partial V} \mathbf{E} \cdot d\mathbf{A} = \frac{Q_{\text{enc}}}{\epsilon_0}$, and conservative field potential $V(\mathbf{b}) - V(\mathbf{a}) = -\int_{\mathbf{a}}^{\mathbf{b}} \mathbf{E} \cdot d\mathbf{l}$.
- **Ampère-Maxwell Law & Displacement Current:** $\oint \mathbf{B} \cdot d\mathbf{l} = \mu_0 I_{\text{enc}} + \mu_0 \epsilon_0 \frac{d\Phi_E}{dt}$, demonstrating current continuity across capacitor dielectric gaps.
- **Faraday's Law of Electromagnetic Induction:** $\mathcal{E} = -\frac{d\Phi_B}{dt} = \oint \mathbf{E} \cdot d\mathbf{l}$, governing transformer operation, mutual inductance, and back-EMF in electrical circuits.
- **Wave Equation from Maxwell's Equations:** Derivation in free space $\nabla^2 \mathbf{E} = \mu_0 \epsilon_0 \frac{\partial^2 \mathbf{E}}{\partial t^2}$, establishing wave speed $c = \frac{1}{\sqrt{\mu_0 \epsilon_0}}$.

---

### 1. Derivation of the Electromagnetic Wave Equation and Speed of Light ($c$)
**Theorem (Maxwell, 1865):** In a charge-free ($\rho = 0$) and conduction current-free ($\mathbf{J} = \mathbf{0}$) vacuum, Maxwell's equations:
$$\nabla \cdot \mathbf{E} = 0, \qquad \nabla \cdot \mathbf{B} = 0$$
$$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}, \qquad \nabla \times \mathbf{B} = \mu_0 \epsilon_0 \frac{\partial \mathbf{E}}{\partial t}$$
rigorously decouple into independent homogeneous 3D wave equations for the electric field $\mathbf{E}$ and magnetic field $\mathbf{B}$:
$$\nabla^2 \mathbf{E} = \frac{1}{c^2} \frac{\partial^2 \mathbf{E}}{\partial t^2} \qquad \text{and} \qquad \nabla^2 \mathbf{B} = \frac{1}{c^2} \frac{\partial^2 \mathbf{B}}{\partial t^2}$$
where the propagation velocity is strictly determined by fundamental electromagnetic constants:
$$c = \frac{1}{\sqrt{\mu_0 \epsilon_0}}$$

#### Step-by-Step Derivation & Proof:
1. **Taking the Curl of Faraday's Law:**
   Apply the vector curl operator to both sides of Faraday's Law:
   $$\nabla \times (\nabla \times \mathbf{E}) = \nabla \times \left( -\frac{\partial \mathbf{B}}{\partial t} \right)$$
   Assuming continuous spatio-temporal partial derivatives, interchange spatial and temporal differentiation:
   $$\nabla \times (\nabla \times \mathbf{E}) = -\frac{\partial}{\partial t} (\nabla \times \mathbf{B})$$

2. **Substitution of the Ampère-Maxwell Law:**
   Substitute the curl of the magnetic field from the vacuum Ampère-Maxwell equation ($\mathbf{J} = \mathbf{0}$):
   $$\nabla \times \mathbf{B} = \mu_0 \epsilon_0 \frac{\partial \mathbf{E}}{\partial t}$$
   yielding:
   $$\nabla \times (\nabla \times \mathbf{E}) = -\frac{\partial}{\partial t} \left( \mu_0 \epsilon_0 \frac{\partial \mathbf{E}}{\partial t} \right) = -\mu_0 \epsilon_0 \frac{\partial^2 \mathbf{E}}{\partial t^2}$$

3. **Application of the Vector Laplacian Identity:**
   For any twice continuously differentiable vector field $\mathbf{V}$, the curl of the curl satisfies the standard differential identity:
   $$\nabla \times (\nabla \times \mathbf{V}) = \nabla (\nabla \cdot \mathbf{V}) - \nabla^2 \mathbf{V}$$
   where $\nabla^2 \mathbf{V} = \left(\nabla^2 V_x\right)\mathbf{i} + \left(\nabla^2 V_y\right)\mathbf{j} + \left(\nabla^2 V_z\right)\mathbf{k}$.
   Applying this to $\mathbf{E}$:
   $$\nabla \times (\nabla \times \mathbf{E}) = \nabla (\nabla \cdot \mathbf{E}) - \nabla^2 \mathbf{E}$$

4. **Enforcing Vacuum Gauss's Law:**
   In vacuum, the free charge density vanishes ($\rho = 0$), so Gauss's Law states $\nabla \cdot \mathbf{E} = 0$.
   Therefore, the gradient of the divergence vanishes identically:
   $$\nabla (\nabla \cdot \mathbf{E}) = \nabla (0) = \mathbf{0}$$
   The left-hand side reduces directly to:
   $$\nabla \times (\nabla \times \mathbf{E}) = -\nabla^2 \mathbf{E}$$

5. **Equating Expressions for the Electric Field:**
   Equating step 3 and step 4:
   $$-\nabla^2 \mathbf{E} = -\mu_0 \epsilon_0 \frac{\partial^2 \mathbf{E}}{\partial t^2} \implies \nabla^2 \mathbf{E} = \mu_0 \epsilon_0 \frac{\partial^2 \mathbf{E}}{\partial t^2}$$

6. **Symmetric Derivation for the Magnetic Field:**
   Take the curl of the Ampère-Maxwell Law in vacuum:
   $$\nabla \times (\nabla \times \mathbf{B}) = \mu_0 \epsilon_0 \frac{\partial}{\partial t} (\nabla \times \mathbf{E})$$
   Substitute Faraday's Law ($\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$):
   $$\nabla \times (\nabla \times \mathbf{B}) = -\mu_0 \epsilon_0 \frac{\partial^2 \mathbf{B}}{\partial t^2}$$
   Using Gauss's Law for Magnetism ($\nabla \cdot \mathbf{B} = 0$):
   $$\nabla (\nabla \cdot \mathbf{B}) - \nabla^2 \mathbf{B} = \mathbf{0} - \nabla^2 \mathbf{B} = -\nabla^2 \mathbf{B}$$
   Equating expressions yields:
   $$\nabla^2 \mathbf{B} = \mu_0 \epsilon_0 \frac{\partial^2 \mathbf{B}}{\partial t^2}$$

7. **Identification of Wave Propagation Speed:**
   The general three-dimensional d'Alembert wave equation for a scalar or vector quantity $\psi$ propagating at phase speed $v$ is:
   $$\nabla^2 \psi = \frac{1}{v^2} \frac{\partial^2 \psi}{\partial t^2}$$
   Matching coefficients:
   $$\frac{1}{c^2} = \mu_0 \epsilon_0 \implies c = \frac{1}{\sqrt{\mu_0 \epsilon_0}}$$
   Evaluating with vacuum permeability $\mu_0 = 4\pi \times 10^{-7} \text{ N/A}^2$ and permittivity $\epsilon_0 \approx 8.854187 \times 10^{-12} \text{ F/m}$:
   $$c = \frac{1}{\sqrt{(4\pi \times 10^{-7})(8.854187 \times 10^{-12})}} \approx 2.99792 \times 10^8 \text{ m/s} \quad \blacksquare$$
