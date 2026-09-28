---
title: "08a - Circuits and Electronics Bridge — Worked Proofs"
type: reference
tags:
  - reference
  - answer-key
---

# 08a - Circuits and Electronics Bridge — Worked Proofs

> [!WARNING] Answer key — open only after your own attempt
> These derivations were generated as reference material, not study notes. Reading them first creates the illusion of competence that [[how-i-study]] warns about.
> Protocol: attempt the proof from a blank sheet in [[08a - Circuits and Electronics Bridge]] → compare here → log every gap you found.
> They are unverified; treat any step you cannot justify as a possible error, not as authority.

Back to: [[08a - Circuits and Electronics Bridge]] · [[Worked Proofs Index]]

---

### 1. Thévenin-Norton Equivalence Theorem
**Theorem:** Any linear one-port electrical network $\mathcal{N}$ composed of linear resistors, independent voltage/current sources, and linear dependent sources can be modeled at its accessible terminal pair $(A, B)$ by:
1. **Thévenin Equivalent:** An ideal voltage source $v_{th}$ in series with an equivalent resistance $R_{th}$:
   $$v(t) = v_{th}(t) - R_{th} i(t)$$
   where $v_{th} = v_{oc}$ is the open-circuit voltage across terminals $A-B$ when $i = 0$, and $R_{th}$ is the driving-point resistance when all internal independent sources are deactivated.
2. **Norton Equivalent:** An ideal current source $i_N$ in parallel with equivalent conductance $G_N = 1/R_{th}$:
   $$i(t) = i_N(t) - G_N v(t)$$
   where $i_N = i_{sc} = v_{th} / R_{th}$ is the short-circuit current flowing from $A$ to $B$ when $v = 0$.

#### Mathematical Derivation:
1. **Linearity of Lumped Resistive Networks:**
   Under Maxwell's equations reduced to the lumped matter discipline, the constitutive equations of all internal elements (resistors $v_k = R_k i_k$, linear dependent sources) and Kirchhoff's laws (KCL, KVL) form a system of linear algebraic equations.
   Let an external test current source $i_{\text{test}} = i$ be connected across the network terminals $A$ and $B$, injecting current into terminal $A$ and returning out of terminal $B$.
   By linearity, the terminal voltage $v$ between $A$ and $B$ is an affine linear function of the external excitation $i$ and all internal independent source excitations $\{v_{s,k}, i_{s,j}\}$.

2. **Decomposition via the Superposition Principle:**
   By the Superposition Theorem, the total terminal response $v$ is the sum of two mutually exclusive operational states:
   $$v = v^{(1)} + v^{(2)}$$
  - **State 1 ($v^{(1)}$ - Internal Sources Active, Zero External Drive):**
    Set the external test current to zero: $i_{\text{test}} = 0$. This corresponds to an open circuit between terminals $A$ and $B$.
    All internal independent sources operate at their nominal values.
    The resulting voltage appearing across terminals $A-B$ is by definition the open-circuit voltage:
    $$v^{(1)} \equiv v_{oc} = v_{th}$$
  - **State 2 ($v^{(2)}$ - Internal Sources Deactivated, External Drive Active):**
    Deactivate all internal independent sources within network $\mathcal{N}$:
    - Replace all independent voltage sources with short circuits ($v_{s,k} = 0$).
    - Replace all independent current sources with open circuits ($i_{s,j} = 0$).
    All linear resistors and linear dependent sources remain active.
    The external test current source $i_{\text{test}} = i$ is applied across $A-B$.
    Since the deactivated network $\mathcal{N}_0$ contains zero independent sources, the resulting terminal voltage $v^{(2)}$ is strictly linear and homogeneous with respect to $i_{\text{test}}$:
    $$v^{(2)} = R_{th} \cdot i_{\text{test}} = R_{th} \cdot i$$
    where $R_{th} = \left.\frac{v_{\text{test}}}{i_{\text{test}}}\right|_{\text{internal independent sources} = 0}$ is the equivalent driving-point resistance.

3. **Synthesizing the Thévenin V-I Characteristic:**
   Superimposing the two states:
   $$v = v^{(1)} + v^{(2)} = v_{th} + R_{th} i$$
   Under the standard load sign convention where $i_{\text{load}}$ flows *out* of terminal $A$ into an external load ($i_{\text{load}} = -i$):
   $$v = v_{th} - R_{th} i_{\text{load}}$$
   This matches the V-I equation of an ideal voltage source $v_{th}$ in series with $R_{th}$.

4. **Derivation of the Norton Dual Form:**
   Solving the Thévenin relation for the load current $i_{\text{load}}$:
   $$i_{\text{load}} = \frac{v_{th} - v}{R_{th}} = \frac{v_{th}}{R_{th}} - \frac{1}{R_{th}} v$$
   Setting $v = 0$ (short circuit across terminals $A-B$) gives the short-circuit current:
   $$i_{sc} \equiv \left. i_{\text{load}} \right|_{v=0} = \frac{v_{th}}{R_{th}} \equiv i_N$$
   Defining equivalent Norton conductance $G_N = \frac{1}{R_{th}}$:
   $$i_{\text{load}} = i_N - G_N v$$
   which is the exact terminal relation of an ideal current source $i_N$ in parallel with conductance $G_N$. $\blacksquare$

---

### 2. KCL/KVL Linear Solvability & Node-Voltage Matrix Formulation
**Theorem:** Let $\mathcal{N}$ be a connected lumped electrical circuit with $n$ nodes and $b$ branches consisting of strictly positive linear conductances $g_k > 0$ for all $k \in \{1, \dots, b\}$, excited by nodal current sources $\mathbf{i}_{src} \in \mathbb{R}^{n-1}$.
Let $A \in \mathbb{R}^{(n-1) \times b}$ be the reduced node-to-branch incidence matrix with node 0 designated as ground ($v_0 = 0$).
Then:
1. The circuit equations formulate compactly as:
   $$Y_n \mathbf{e} = \mathbf{i}_{src}, \quad \text{where } Y_n = A G_b A^T \in \mathbb{R}^{(n-1) \times (n-1)}$$
   where $G_b = \text{diag}(g_1, \dots, g_b)$ is the branch conductance matrix and $\mathbf{e} \in \mathbb{R}^{n-1}$ is the node-voltage vector.
2. The nodal admittance matrix $Y_n$ is strictly symmetric positive-definite (SPD):
   $$\mathbf{x}^T Y_n \mathbf{x} > 0 \quad \forall \mathbf{x} \in \mathbb{R}^{n-1} \setminus \{\mathbf{0}\}$$
3. Consequently, $Y_n$ is non-singular ($\det(Y_n) > 0$), and a unique node-voltage solution $\mathbf{e} = Y_n^{-1} \mathbf{i}_{src}$ exists for any excitation.

#### Mathematical Derivation:
1. **Graph Incidence Matrix & Topological Rank:**
   Model the circuit network as a connected directed graph $G = (V, E)$ with $|V| = n$ and $|E| = b$.
   The complete incidence matrix $\tilde{A} \in \{-1, 0, 1\}^{n \times b}$ has entries:
   $$\tilde{a}_{ik} = \begin{cases} +1 & \text{if branch } k \text{ leaves node } i \\ -1 & \text{if branch } k \text{ enters node } i \\ 0 & \text{otherwise} \end{cases}$$
   Every column of $\tilde{A}$ has exactly one $+1$ and one $-1$, hence $\mathbf{1}^T \tilde{A} = \mathbf{0}^T$.
   Deleting the row corresponding to the reference ground node 0 yields the reduced incidence matrix $A \in \mathbb{R}^{(n-1) \times b}$.
   Because the network graph is connected, $A$ has full row rank:
   $$\text{rank}(A) = n - 1$$

2. **Topological Expression of KCL and KVL:**
  - **Kirchhoff's Current Law (KCL):** The sum of branch currents leaving each non-ground node equals the external injected current:
    $$A \mathbf{i}_b = \mathbf{i}_{src}$$
    where $\mathbf{i}_b = [i_1, \dots, i_b]^T \in \mathbb{R}^b$.
  - **Kirchhoff's Voltage Law (KVL):** The branch voltages $\mathbf{v}_b \in \mathbb{R}^b$ are the potential differences between incident nodes. By matrix transposition:
    $$\mathbf{v}_b = A^T \mathbf{e}$$
    where $\mathbf{e} = [e_1, \dots, e_{n-1}]^T \in \mathbb{R}^{n-1}$ are the node potentials relative to ground.

3. **Constitutive Relations and Matrix Synthesis:**
   By Ohm's law in matrix form, the branch currents are:
   $$\mathbf{i}_b = G_b \mathbf{v}_b = G_b (A^T \mathbf{e})$$
   where $G_b = \text{diag}(g_1, g_2, \dots, g_b) \in \mathbb{R}^{b \times b}$ with $g_k > 0$.
   Substituting $\mathbf{i}_b$ into KCL yields the Node-Voltage Equation:
   $$A (G_b A^T \mathbf{e}) = \mathbf{i}_{src} \implies (A G_b A^T) \mathbf{e} = \mathbf{i}_{src}$$
   Defining $Y_n = A G_b A^T$, this is $Y_n \mathbf{e} = \mathbf{i}_{src}$.

4. **Proof of Symmetric Positive Definiteness:**
  - **Symmetry:**
    $$Y_n^T = (A G_b A^T)^T = (A^T)^T G_b^T A^T = A G_b A^T = Y_n$$
    (since $G_b$ is a diagonal matrix, $G_b^T = G_b$).
  - **Positive Definiteness:**
    Let $\mathbf{x} \in \mathbb{R}^{n-1}$ be any non-zero vector ($\mathbf{x} \neq \mathbf{0}$).
    Evaluate the quadratic form:
    $$\mathbf{x}^T Y_n \mathbf{x} = \mathbf{x}^T (A G_b A^T) \mathbf{x} = (A^T \mathbf{x})^T G_b (A^T \mathbf{x})$$
    Let $\mathbf{y} = A^T \mathbf{x} \in \mathbb{R}^b$. Since $g_k > 0$ for all $k$:
    $$\mathbf{y}^T G_b \mathbf{y} = \sum_{k=1}^b g_k y_k^2 \ge 0$$
    Notice that $\mathbf{y}^T G_b \mathbf{y} = 0$ if and only if $\mathbf{y} = \mathbf{0}$, which means $A^T \mathbf{x} = \mathbf{0}$.
    However, because the network is connected, $\text{rank}(A) = n - 1$. By the Fundamental Theorem of Linear Algebra, the null space of $A^T$ is trivial:
    $$\ker(A^T) = \{\mathbf{0}\}$$
    Since $\mathbf{x} \neq \mathbf{0}$, we have $\mathbf{y} = A^T \mathbf{x} \neq \mathbf{0}$.
    Therefore:
    $$\mathbf{x}^T Y_n \mathbf{x} = \sum_{k=1}^b g_k (A^T \mathbf{x})_k^2 > 0$$
  - **Invertibility:**
    Because $Y_n$ is strictly positive-definite, all its eigenvalues are strictly positive ($\lambda_i > 0$).
    Thus $\det(Y_n) = \prod_{i=1}^{n-1} \lambda_i > 0$, guaranteeing that $Y_n$ is non-singular and uniquely invertible:
    $$\mathbf{e} = Y_n^{-1} \mathbf{i}_{src} \quad \blacksquare$$

---

### 3. Series/Parallel RLC Second-Order Transient Response & Damping Classification
**Theorem:** Consider a series RLC circuit with inductance $L > 0$, capacitance $C > 0$, and resistance $R \ge 0$, with initial capacitor voltage $v_C(0) = V_0$ and initial inductor current $i_L(0) = I_0$ under unforced conditions ($t \ge 0$).
The capacitor voltage $v_C(t)$ obeys the canonical second-order differential equation:
$$\frac{d^2 v_C}{dt^2} + 2\alpha \frac{dv_C}{dt} + \omega_0^2 v_C = 0$$
where $\omega_0 = \frac{1}{\sqrt{LC}}$ is the undamped natural frequency and $\alpha = \frac{R}{2L}$ is the attenuation factor (with damping ratio $\zeta = \alpha / \omega_0 = \frac{R}{2}\sqrt{\frac{C}{L}}$).
The transient response is partitioned into three distinct analytical regimes:
1. **Overdamped ($\zeta > 1 \iff \alpha > \omega_0$):**
   $$v_C(t) = A_1 e^{s_1 t} + A_2 e^{s_2 t}, \quad s_{1,2} = -\alpha \pm \sqrt{\alpha^2 - \omega_0^2} < 0$$
2. **Critically Damped ($\zeta = 1 \iff \alpha = \omega_0$):**
   $$v_C(t) = (A_1 + A_2 t) e^{-\alpha t}, \quad s_1 = s_2 = -\alpha$$
3. **Underdamped ($\zeta < 1 \iff \alpha < \omega_0$):**
   $$v_C(t) = e^{-\alpha t} \Big( C_1 \cos(\omega_d t) + C_2 \sin(\omega_d t) \Big) = A e^{-\alpha t} \cos(\omega_d t - \phi)$$
   where $\omega_d = \sqrt{\omega_0^2 - \alpha^2} = \omega_0 \sqrt{1 - \zeta^2}$ is the damped ringing frequency.

#### Mathematical Derivation:
1. **Derivation of the Governing Second-Order ODE:**
   Apply KVL around the series loop:
   $$v_R(t) + v_L(t) + v_C(t) = 0$$
   Substitute element constitutive relations:
   $$v_R(t) = R i(t), \quad v_L(t) = L \frac{di(t)}{dt}, \quad i(t) = C \frac{dv_C(t)}{dt}$$
   Differentiating the current gives $\frac{di}{dt} = C \frac{d^2 v_C}{dt^2}$.
   Substituting into KVL:
   $$R \left( C \frac{dv_C}{dt} \right) + L \left( C \frac{d^2 v_C}{dt^2} \right) + v_C = 0 \implies L C \frac{d^2 v_C}{dt^2} + R C \frac{dv_C}{dt} + v_C = 0$$
   Dividing through by $LC$:
   $$\frac{d^2 v_C}{dt^2} + \frac{R}{L} \frac{dv_C}{dt} + \frac{1}{LC} v_C = 0$$
   Setting $\alpha = \frac{R}{2L}$ and $\omega_0^2 = \frac{1}{LC}$, this yields the standard equation:
   $$\frac{d^2 v_C}{dt^2} + 2\alpha \frac{dv_C}{dt} + \omega_0^2 v_C = 0$$

2. **Characteristic Roots:**
   Substitute the trial solution $v_C(t) = e^{st}$:
   $$(s^2 + 2\alpha s + \omega_0^2) e^{st} = 0 \implies s^2 + 2\alpha s + \omega_0^2 = 0$$
   Applying the quadratic formula gives the characteristic roots:
   $$s_{1,2} = -\alpha \pm \sqrt{\alpha^2 - \omega_0^2} = -\zeta \omega_0 \pm \omega_0 \sqrt{\zeta^2 - 1}$$
   The discriminant $\mathcal{D} = \alpha^2 - \omega_0^2 = \omega_0^2(\zeta^2 - 1)$ dictates the solution regime.

3. **Case 1: Overdamped Regime ($\zeta > 1 \iff \alpha > \omega_0$):**
   Here $\mathcal{D} > 0$. The roots $s_1, s_2$ are real, distinct, and strictly negative:
   $$s_1 = -\alpha + \sqrt{\alpha^2 - \omega_0^2} < 0, \quad s_2 = -\alpha - \sqrt{\alpha^2 - \omega_0^2} < 0$$
   The general solution is a sum of two distinct exponential decays:
   $$v_C(t) = A_1 e^{s_1 t} + A_2 e^{s_2 t}$$
   Applying initial conditions $v_C(0) = A_1 + A_2 = V_0$ and $v_C'(0) = s_1 A_1 + s_2 A_2 = \frac{I_0}{C}$:
   $$A_1 = \frac{\frac{I_0}{C} - s_2 V_0}{s_1 - s_2}, \quad A_2 = \frac{s_1 V_0 - \frac{I_0}{C}}{s_1 - s_2}$$
   The response decays monotonically without oscillation, governed asymptotically by the slower pole $s_1$.

4. **Case 2: Critically Damped Regime ($\zeta = 1 \iff \alpha = \omega_0$):**
   Here $\mathcal{D} = 0$. The characteristic equation has a repeated real root $s_1 = s_2 = -\alpha$.
   The first solution is $v_1(t) = e^{-\alpha t}$. To find the second independent solution, apply reduction of order: $v_2(t) = u(t) e^{-\alpha t}$.
   Substituting into the ODE:
   $$\frac{d^2}{dt^2}\big[u e^{-\alpha t}\big] + 2\alpha \frac{d}{dt}\big[u e^{-\alpha t}\big] + \alpha^2 \big[u e^{-\alpha t}\big] = 0$$
   Expanding derivatives:
   $$\big(u'' - 2\alpha u' + \alpha^2 u\big) e^{-\alpha t} + 2\alpha \big(u' - \alpha u\big) e^{-\alpha t} + \alpha^2 u e^{-\alpha t} = 0 \implies u''(t) e^{-\alpha t} = 0$$
   Since $e^{-\alpha t} \neq 0$, $u''(t) = 0 \implies u(t) = A_1 + A_2 t$.
   Thus the general solution is:
   $$v_C(t) = (A_1 + A_2 t) e^{-\alpha t}$$
   Initial conditions give $A_1 = V_0$ and $A_2 = \frac{I_0}{C} + \alpha V_0$. This provides the fastest non-oscillatory return to equilibrium.

5. **Case 3: Underdamped Regime ($\zeta < 1 \iff \alpha < \omega_0$):**
   Here $\mathcal{D} < 0$. The roots are complex conjugates:
   $$s_{1,2} = -\alpha \pm j \sqrt{\omega_0^2 - \alpha^2} = -\alpha \pm j \omega_d$$
   where $\omega_d = \sqrt{\omega_0^2 - \alpha^2} = \omega_0 \sqrt{1 - \zeta^2} > 0$ is the damped natural frequency.
   The general solution in complex exponential form is:
   $$v_C(t) = B_1 e^{(-\alpha + j\omega_d)t} + B_2 e^{(-\alpha - j\omega_d)t} = e^{-\alpha t} \left( B_1 e^{j\omega_d t} + B_2 e^{-j\omega_d t} \right)$$
   Using Euler's formula $e^{\pm j\omega_d t} = \cos(\omega_d t) \pm j \sin(\omega_d t)$ and enforcing real boundary conditions ($B_2 = B_1^*$):
   $$v_C(t) = e^{-\alpha t} \Big( C_1 \cos(\omega_d t) + C_2 \sin(\omega_d t) \Big)$$
   where $C_1 = B_1 + B_2 = V_0$ and $C_2 = \frac{\frac{I_0}{C} + \alpha V_0}{\omega_d}$.
   In compact amplitude-phase form:
   $$v_C(t) = A e^{-\alpha t} \cos(\omega_d t - \phi), \quad \text{where } A = \sqrt{C_1^2 + C_2^2}, \quad \phi = \arctan\left(\frac{C_2}{C_1}\right)$$
   The voltage exhibits damped sinusoidal ringing bounded by the exponential envelope $\pm A e^{-\alpha t}$. $\blacksquare$
