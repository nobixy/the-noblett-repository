# Handoff Report: Milestone M4 (Bridge Syllabi Proofs Explorer - F28 / T1.28)

**Agent:** explorer_m4_2  
**Date:** 2026-09-25  
**Scope:** Feature F28 / Test T1.28 (Bridge Course Rigorous Proof Expansions)  
**Target Files:**  
- `01 - Curriculum/Year 1 - Fundamentals/04a - Differential Equations Bridge.md`
- `01 - Curriculum/Year 1 - Fundamentals/08a - Circuits and Electronics Bridge.md`
- `01 - Curriculum/Year 2 - Systems/15a - Signals and Systems Bridge.md`

---

## 1. Observation

Direct programmatic observations across the codebase and test suite:

1. **Test Assertion in `.agents/test_suite/run_e2e_tests.py` (lines 995–1022):**
   ```python
   def test_t1_28_bridge_course_rigorous_proof_expansions(self) -> TestResult:
       """T1.28: Bridge courses 04a, 08a, 15a contain step-by-step mathematical proofs."""
       bridges = [
           "01 - Curriculum/Year 1 - Fundamentals/04a - Differential Equations Bridge.md",
           "01 - Curriculum/Year 1 - Fundamentals/08a - Circuits and Electronics Bridge.md",
           "01 - Curriculum/Year 2 - Systems/15a - Signals and Systems Bridge.md"
       ]
       defects: List[str] = []
       for b in bridges:
           if b in self.context.md_files:
               md = self.context.md_files[b]
               # Look for proof section
               proof_section = re.search(r"## 📝 Study Notes[^\n]*\n(.*?)(?=\n## |\Z)", md.raw_content, re.DOTALL)
               if not proof_section:
                   defects.append(f"{b}: Missing proof section")
                   continue
               body = proof_section.group(1)
               # Verify it's not just "Prove that..." prompts without proofs
               # A full derivation should contain multiple display math blocks and explanation
               num_display_math = len(re.findall(r"\$\$", body))
               if num_display_math < 6:
                   defects.append(f"{b}: Contains only {num_display_math//2} display math environments (prompts rather than derivations)")
   ```

2. **Current Baseline Failure in `test_report.json` (line 817):**
   ```json
   "message": "Bridge proof deficiencies: 01 - Curriculum/Year 1 - Fundamentals/04a - Differential Equations Bridge.md: Contains only 0 display math environments (prompts rather than derivations), 01 - Curriculum/Year 1 - Fundamentals/08a - Circuits and Electronics Bridge.md: Contains only 0 display math environments (prompts rather than derivations), 01 - Curriculum/Year 2 - Systems/15a - Signals and Systems Bridge.md: Contains only 0 display math environments (prompts rather than derivations)"
   ```

3. **Existing Content in Target Files:**
   - **`04a - Differential Equations Bridge.md` (lines 197–204):**
     Contains section `## 📝 Study Notes, Psets & Proofs` with subhead `### Essential Theoretical Proofs for Mastery` and 4 bullet-point homework prompts ("1. **Abel's Theorem on the Wronskian:** Prove that...", etc.) with 0 display math environments (`$$...$$`).
   - **`08a - Circuits and Electronics Bridge.md` (lines 162–169):**
     Contains section `## 📝 Study Notes, Psets & Proofs` with subhead `### Essential Theoretical Proofs for Mastery` and 4 bullet-point prompts ("1. **Thevenin's Theorem Derivation:** Prove that...", etc.) with 0 display math environments.
   - **`15a - Signals and Systems Bridge.md` (lines 196–203):**
     Contains section `## 📝 Study Notes, Psets & Proofs` with subhead `### Essential Theoretical Proofs for Mastery` and 4 bullet-point prompts ("1. **Derivation of the Convolution Property:** Prove that...", etc.) with 0 display math environments.

4. **Formatting and Interface Contracts in `PROJECT.md` (lines 85–90):**
   - "No section may contain empty placeholder text, TODO stubs, or parenthetical directives."
   - "Every proof section (`## 📝 Study Notes, Psets & Proofs`) must provide complete, step-by-step mathematical or architectural derivations."
   - "Every formal proof must conclude with a standard Q.E.D. tombstone: `$\blacksquare$`."

---

## 2. Logic Chain

1. **Defect Causation:** All 3 bridge notes (`04a`, `08a`, `15a`) currently contain only assignment prompts (e.g. "Prove that...") rather than the actual mathematical derivations. In each file, `num_display_math` is 0, which violates the test threshold `num_display_math >= 6` in `test_t1_28`.
2. **Expansion Requirement:** To satisfy F28 and achieve full textbook depth (R2 Vertical Expansion), each bridge note must be populated with rigorous, complete derivations. For each note, three canonical, foundational theorems must be derived from first principles with full intermediate algebra and display math blocks.
3. **Mathematical Completeness:**
   - For `04a`:
     1. Abel's Theorem on the Wronskian ($W(t) = W(t_0)\exp(-\int_{t_0}^t p(s)ds)$) establishes the zero/non-zero dichotomy of solution independence.
     2. Matrix Exponential Solution ($\mathbf{x}(t) = e^{A(t-t_0)}\mathbf{x}_0$) establishes power series convergence, term-by-term differentiation, and IVP uniqueness.
     3. Picard-Lindelöf Existence and Uniqueness Theorem rigorously establishes the Volterra integral formulation, contraction mapping on a Banach space of continuous functions with Chebyshev norm, and Banach Fixed-Point Theorem application.
   - For `08a`:
     1. Thévenin-Norton Equivalence Theorem rigorously proves affine one-port $V-I$ characteristics via the Superposition Theorem and source deactivation.
     2. KCL/KVL Linear Solvability & Node-Voltage Matrix Formulation establishes topological incidence matrices ($A \in \mathbb{R}^{(n-1) \times b}$), Tellegen's orthogonality, and proves that the nodal admittance matrix $Y_n = A G_b A^T$ is symmetric positive-definite (SPD) and therefore uniquely invertible.
     3. Series/Parallel RLC Second-Order Transient Response & Damping Classification derives the second-order ODE from KVL/constitutive equations and exhaustively classifies the three distinct dynamic regimes (overdamped, critically damped, underdamped).
   - For `15a`:
     1. DTFT Convolution-Multiplication Duality proves both time-convolution $\leftrightarrow$ frequency-multiplication and time-multiplication $\leftrightarrow$ frequency-periodic-convolution via Fubini-Tonelli summation/integral swaps.
     2. Nyquist-Shannon Sampling Theorem & Whittaker-Shannon Reconstruction Formula proves Dirac comb Fourier series, spectral replication without aliasing ($\Omega_s > 2\Omega_M$), ideal low-pass filter inversion, and exact time-domain cardinal sinc interpolation.
     3. Z-Transform Region of Convergence (ROC) Stability Criterion proves BIBO stability $\iff h \in \ell^1(\mathbb{Z}) \iff$ ROC contains the unit circle $\mathbb{T} = \{|z|=1\}$, and specializes to the causal pole condition $\max_k |p_k| < 1$.
4. **Structural Conformance:** Each derivation terminates with `$\blacksquare$`, contains at least 4–8 display math environments (`$$...$$`), uses standard 2/4 space indentation, and adheres to vault heading hierarchy (`###` for proof title, `####` for sub-sections).

---

## 3. Caveats

- **Scope Boundary:** This explorer is read-only. No edits were made to vault content files. The blueprints below are ready for direct drop-in integration by the Worker.
- **Display Math Count:** The E2E test `test_t1_28` requires `len(re.findall(r"\$\$", body)) >= 6` (at least 3 display math blocks). The blueprints provided below contain between 15 and 25 display math environments per bridge note, exceeding the test threshold by an order of magnitude.
- **No Invalidation of Other Sections:** The proposed proof sections replace only the text between `## 📝 Study Notes, Psets & Proofs` and `---` / `## 🔄 Appendix A Alternatives (Failover)`, preserving all preceding course modules, build requirements, and navigation blocks.

---

## 4. Conclusion & Actionable Blueprints for Worker

The Worker should replace the existing stub prompt list under `## 📝 Study Notes, Psets & Proofs` in `04a`, `08a`, and `15a` with the complete, drop-in replacement markdown sections detailed below.

---

### Blueprint 1: `01 - Curriculum/Year 1 - Fundamentals/04a - Differential Equations Bridge.md`

**Target Location:** Replace lines 197–205 (the entire section from `## 📝 Study Notes, Psets & Proofs` up to `---` before `## 🔄 Appendix A Alternatives`) with the following block:

```markdown
## 📝 Study Notes, Psets & Proofs

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
```

---

### Blueprint 2: `01 - Curriculum/Year 1 - Fundamentals/08a - Circuits and Electronics Bridge.md`

**Target Location:** Replace lines 162–170 (the entire section from `## 📝 Study Notes, Psets & Proofs` up to `---` before `## 🔄 Appendix A Alternatives`) with the following block:

```markdown
## 📝 Study Notes, Psets & Proofs

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
```

---

### Blueprint 3: `01 - Curriculum/Year 2 - Systems/15a - Signals and Systems Bridge.md`

**Target Location:** Replace lines 196–204 (the entire section from `## 📝 Study Notes, Psets & Proofs` up to `---` before `## 🔄 Appendix A Alternatives`) with the following block:

```markdown
## 📝 Study Notes, Psets & Proofs

### 1. DTFT Convolution-Multiplication Duality
**Theorem:** Let $x[n], y[n] \in \ell^1(\mathbb{Z})$ be discrete-time signals with Discrete-Time Fourier Transforms (DTFT) $X(e^{j\omega})$ and $Y(e^{j\omega})$:
$$X(e^{j\omega}) = \sum_{n=-\infty}^\infty x[n] e^{-j\omega n}, \quad x[n] = \frac{1}{2\pi} \int_{-\pi}^\pi X(e^{j\omega}) e^{j\omega n} \, d\omega$$
Then the DTFT satisfies exact time-frequency duality between convolution and multiplication:
1. **Time Convolution $\implies$ Frequency Multiplication:**
   If $w[n] = (x * y)[n] = \sum_{k=-\infty}^\infty x[k] y[n - k]$, then:
   $$W(e^{j\omega}) = X(e^{j\omega}) \cdot Y(e^{j\omega})$$
2. **Time Multiplication $\implies$ Frequency Periodic Convolution:**
   If $v[n] = x[n] \cdot y[n]$, then:
   $$V(e^{j\omega}) = \frac{1}{2\pi} \int_{-\pi}^\pi X(e^{j\theta}) Y(e^{j(\omega - \theta)}) \, d\theta \equiv \frac{1}{2\pi} \Big( X(e^{j\omega}) \circledast Y(e^{j\omega}) \Big)$$

#### Mathematical Derivation:
1. **Time-Domain Convolution to Frequency Multiplication:**
   By definition of the forward DTFT on the convolution sum:
   $$W(e^{j\omega}) = \sum_{n=-\infty}^\infty w[n] e^{-j\omega n} = \sum_{n=-\infty}^\infty \left( \sum_{k=-\infty}^\infty x[k] y[n - k] \right) e^{-j\omega n}$$
   Because $x, y \in \ell^1(\mathbb{Z})$, the series converges absolutely:
   $$\sum_{n=-\infty}^\infty \sum_{k=-\infty}^\infty |x[k] y[n - k]| = \sum_{k=-\infty}^\infty |x[k]| \sum_{n=-\infty}^\infty |y[n - k]| = \|x\|_{\ell^1} \|y\|_{\ell^1} < \infty$$
   By Fubini's/Tonelli's Theorem, we interchange the order of summation:
   $$W(e^{j\omega}) = \sum_{k=-\infty}^\infty x[k] \left( \sum_{n=-\infty}^\infty y[n - k] e^{-j\omega n} \right)$$
   Substitute index $m = n - k$, so $n = m + k$. As $n \to \pm\infty$, $m \to \pm\infty$:
   $$\sum_{n=-\infty}^\infty y[n - k] e^{-j\omega n} = \sum_{m=-\infty}^\infty y[m] e^{-j\omega(m + k)} = e^{-j\omega k} \sum_{m=-\infty}^\infty y[m] e^{-j\omega m} = e^{-j\omega k} Y(e^{j\omega})$$
   Substituting this result into the outer sum:
   $$W(e^{j\omega}) = \sum_{k=-\infty}^\infty x[k] e^{-j\omega k} Y(e^{j\omega}) = \left( \sum_{k=-\infty}^\infty x[k] e^{-j\omega k} \right) Y(e^{j\omega}) = X(e^{j\omega}) Y(e^{j\omega})$$

2. **Time-Domain Multiplication to Frequency Periodic Convolution:**
   By definition of the forward DTFT of the product sequence $v[n] = x[n] y[n]$:
   $$V(e^{j\omega}) = \sum_{n=-\infty}^\infty x[n] y[n] e^{-j\omega n}$$
   Substitute the inverse DTFT integral representation for $x[n]$:
   $$x[n] = \frac{1}{2\pi} \int_{-\pi}^\pi X(e^{j\theta}) e^{j\theta n} \, d\theta$$
   yielding:
   $$V(e^{j\omega}) = \sum_{n=-\infty}^\infty \left( \frac{1}{2\pi} \int_{-\pi}^\pi X(e^{j\theta}) e^{j\theta n} \, d\theta \right) y[n] e^{-j\omega n}$$
   Since $y \in \ell^1(\mathbb{Z})$ and $X(e^{j\theta})$ is continuous and bounded, we interchange summation and integration:
   $$V(e^{j\omega}) = \frac{1}{2\pi} \int_{-\pi}^\pi X(e^{j\theta}) \left( \sum_{n=-\infty}^\infty y[n] e^{-j(\omega - \theta) n} \right) d\theta$$
   Recognizing the inner summation as the DTFT of $y[n]$ evaluated at frequency $\omega - \theta$:
   $$\sum_{n=-\infty}^\infty y[n] e^{-j(\omega - \theta) n} = Y(e^{j(\omega - \theta)})$$
   Therefore:
   $$V(e^{j\omega}) = \frac{1}{2\pi} \int_{-\pi}^\pi X(e^{j\theta}) Y(e^{j(\omega - \theta)}) \, d\theta$$
   This is the periodic convolution of $X(e^{j\omega})$ and $Y(e^{j\omega})$, concluding the duality proof. $\blacksquare$

---

### 2. Nyquist-Shannon Sampling Theorem & Whittaker-Shannon Reconstruction Formula
**Theorem:** Let $x(t) \in L^2(\mathbb{R}) \cap C(\mathbb{R})$ be a continuous-time signal strictly bandlimited to maximum angular frequency $\Omega_M$, such that its Continuous-Time Fourier Transform (CTFT) satisfies:
$$X(j\Omega) = \int_{-\infty}^\infty x(t) e^{-j\Omega t} \, dt = 0 \quad \text{for } |\Omega| > \Omega_M$$
Let $x(t)$ be sampled uniformly at period $T_s$, with sampling frequency $\Omega_s = \frac{2\pi}{T_s}$.
1. **Nyquist Criterion:** If $\Omega_s > 2\Omega_M$, $x(t)$ is uniquely and completely determined by its sample values $\{x(n T_s)\}_{n=-\infty}^\infty$.
2. **Whittaker-Shannon Reconstruction Formula:** The original continuous waveform $x(t)$ can be reconstructed exactly for all $t \in \mathbb{R}$ via:
   $$x(t) = \sum_{n=-\infty}^\infty x(n T_s) \, \text{sinc}\left( \frac{t - n T_s}{T_s} \right) = \sum_{n=-\infty}^\infty x(n T_s) \frac{\sin\left(\frac{\pi(t - n T_s)}{T_s}\right)}{\frac{\pi(t - n T_s)}{T_s}}$$

#### Mathematical Derivation:
1. **Impulse Train Sampling Model:**
   Represent the ideal sampling process as multiplication by a Dirac impulse train $p(t) = \sum_{n=-\infty}^\infty \delta(t - n T_s)$:
   $$x_p(t) = x(t) p(t) = x(t) \sum_{n=-\infty}^\infty \delta(t - n T_s) = \sum_{n=-\infty}^\infty x(n T_s) \delta(t - n T_s)$$
   by the sifting property of the Dirac delta.

2. **Fourier Series and Transform of the Sampling Comb:**
   Since $p(t)$ is periodic with period $T_s$, expand it as a complex Fourier series:
   $$p(t) = \sum_{k=-\infty}^\infty c_k e^{j k \Omega_s t}, \quad \Omega_s = \frac{2\pi}{T_s}$$
   The Fourier coefficients are:
   $$c_k = \frac{1}{T_s} \int_{-T_s/2}^{T_s/2} \delta(t) e^{-j k \Omega_s t} \, dt = \frac{1}{T_s} e^0 = \frac{1}{T_s}$$
   Thus $p(t) = \frac{1}{T_s} \sum_{k=-\infty}^\infty e^{j k \Omega_s t}$.
   Taking the CTFT of $p(t)$:
   $$P(j\Omega) = \mathcal{F}\left\{ \frac{1}{T_s} \sum_{k=-\infty}^\infty e^{j k \Omega_s t} \right\} = \frac{2\pi}{T_s} \sum_{k=-\infty}^\infty \delta(\Omega - k \Omega_s) = \Omega_s \sum_{k=-\infty}^\infty \delta(\Omega - k \Omega_s)$$

3. **Spectrum of the Sampled Signal:**
   By the modulation/multiplication property of the CTFT:
   $$X_p(j\Omega) = \frac{1}{2\pi} \Big[ X(j\Omega) * P(j\Omega) \Big] = \frac{1}{2\pi} \left[ X(j\Omega) * \left( \frac{2\pi}{T_s} \sum_{k=-\infty}^\infty \delta(\Omega - k \Omega_s) \right) \right]$$
   Convolving with each shifted delta function:
   $$X_p(j\Omega) = \frac{1}{T_s} \sum_{k=-\infty}^\infty X(j(\Omega - k \Omega_s))$$
   The sampled spectrum consists of infinitely repeated copies of $X(j\Omega)$, scaled by $1/T_s$ and shifted by integer multiples of $\Omega_s$.

4. **Aliasing Avoidance (Nyquist Criterion):**
   The baseband spectrum ($k=0$) occupies $[-\Omega_M, \Omega_M]$. The first adjacent positive replica ($k=1$) occupies $[\Omega_s - \Omega_M, \Omega_s + \Omega_M]$.
   To ensure no spectral overlap occurs:
   $$\Omega_s - \Omega_M > \Omega_M \iff \Omega_s > 2\Omega_M$$
   When this condition holds, $X(j\Omega)$ is isolated in the interval $|\Omega| \le \Omega_s / 2$.

5. **Ideal Low-Pass Reconstruction:**
   Extract the baseband spectrum by passing $x_p(t)$ through an ideal brick-wall low-pass filter $H_r(j\Omega)$ with cutoff $\Omega_c = \Omega_s / 2 = \pi / T_s$ and passband gain $T_s$:
   $$H_r(j\Omega) = \begin{cases} T_s & |\Omega| \le \frac{\pi}{T_s} \\ 0 & |\Omega| > \frac{\pi}{T_s} \end{cases}$$
   Then the filtered spectrum is:
   $$X_r(j\Omega) = H_r(j\Omega) X_p(j\Omega) = T_s \left( \frac{1}{T_s} X(j\Omega) \right) = X(j\Omega)$$
   Hence $x_r(t) = x(t)$ for all $t \in \mathbb{R}$.

6. **Whittaker-Shannon Cardinal Sinc Interpolation:**
   Compute the time-domain impulse response $h_r(t)$ of the reconstruction filter:
   $$h_r(t) = \frac{1}{2\pi} \int_{-\pi/T_s}^{\pi/T_s} T_s e^{j\Omega t} \, d\Omega = \frac{T_s}{2\pi} \left[ \frac{e^{j\Omega t}}{j t} \right]_{-\pi/T_s}^{\pi/T_s} = \frac{T_s}{\pi t} \sin\left(\frac{\pi t}{T_s}\right) = \text{sinc}\left( \frac{t}{T_s} \right)$$
   The reconstructed continuous signal is the continuous-time convolution $x(t) = x_p(t) * h_r(t)$:
   $$x(t) = \left( \sum_{n=-\infty}^\infty x(n T_s) \delta(t - n T_s) \right) * \text{sinc}\left( \frac{t}{T_s} \right) = \sum_{n=-\infty}^\infty x(n T_s) \Big( \delta(t - n T_s) * \text{sinc}\left( \frac{t}{T_s} \right) \Big)$$
   Since $\delta(t - n T_s) * f(t) = f(t - n T_s)$:
   $$x(t) = \sum_{n=-\infty}^\infty x(n T_s) \, \text{sinc}\left( \frac{t - n T_s}{T_s} \right) \quad \blacksquare$$

---

### 3. Z-Transform Region of Convergence (ROC) Stability Criterion
**Theorem:** Let $\mathcal{H}$ be a discrete-time Linear Time-Invariant (LTI) system with impulse response $h[n]$ and system transfer function $H(z) = \mathcal{Z}\{h[n]\} = \sum_{n=-\infty}^\infty h[n] z^{-n}$.
1. **General LTI Stability:** $\mathcal{H}$ is Bounded-Input Bounded-Output (BIBO) stable if and only if the Region of Convergence (ROC) of $H(z)$ contains the unit circle:
   $$\mathbb{T} = \{z \in \mathbb{C} : |z| = 1\} \subset \text{ROC}(H)$$
2. **Causal LTI Stability:** If $\mathcal{H}$ is a **causal** system ($h[n] = 0$ for $n < 0$) with rational transfer function $H(z) = \frac{B(z)}{A(z)}$, then $\mathcal{H}$ is BIBO stable if and only if **all poles of $H(z)$ lie strictly inside the open unit circle**:
   $$\forall p \in \mathbb{C} \text{ such that } A(p) = 0, \quad |p| < 1$$

#### Mathematical Derivation:
1. **BIBO Stability is Equivalent to Absolute Summability of $h[n]$:**
   A system is BIBO stable if for every bounded input sequence with $\|x\|_\infty = \sup_{n} |x[n]| \le M_x < \infty$, the output sequence $y[n] = (x * h)[n]$ satisfies $\|y\|_\infty \le M_y < \infty$.
   - **Sufficiency:** Suppose $\sum_{k=-\infty}^\infty |h[k]| = S < \infty$. Then:
     $$|y[n]| = \left| \sum_{k=-\infty}^\infty h[k] x[n - k] \right| \le \sum_{k=-\infty}^\infty |h[k]| |x[n - k]| \le M_x \sum_{k=-\infty}^\infty |h[k]| = M_x S < \infty$$
     Thus $\|y\|_\infty \le M_x S < \infty$, establishing stability.
   - **Necessity:** Suppose $\sum_{k=-\infty}^\infty |h[k]| = \infty$. Choose the bounded input:
     $$x[-k] = \begin{cases} \frac{h^*[k]}{|h[k]|} & \text{if } h[k] \neq 0 \\ 0 & \text{if } h[k] = 0 \end{cases}$$
     Clearly $|x[n]| \le 1$ for all $n$, so $\|x\|_\infty = 1$. The output at $n = 0$ is:
     $$y[0] = \sum_{k=-\infty}^\infty h[k] x[-k] = \sum_{k=-\infty}^\infty |h[k]| = \infty$$
     Hence the output is unbounded. Thus BIBO stability holds if and only if $h \in \ell^1(\mathbb{Z})$ ($\sum_{n=-\infty}^\infty |h[n]| < \infty$).

2. **Connecting Summability to the Region of Convergence:**
   By definition, the bilateral Z-transform converges absolutely on the set:
   $$\text{ROC}(H) = \left\{ z \in \mathbb{C} : \sum_{n=-\infty}^\infty |h[n] z^{-n}| < \infty \right\} = \left\{ z = r e^{j\omega} : \sum_{n=-\infty}^\infty |h[n]| r^{-n} < \infty \right\}$$
   Convergence depends only on the radius $r = |z|$.
   Evaluate this absolute convergence condition specifically on the unit circle $|z| = r = 1$:
   $$\left. \sum_{n=-\infty}^\infty |h[n]| |z|^{-n} \right|_{|z|=1} = \sum_{n=-\infty}^\infty |h[n]| (1)^{-n} = \sum_{n=-\infty}^\infty |h[n]|$$
   Therefore, the Z-transform sum converges absolutely on the unit circle if and only if $\sum_{n=-\infty}^\infty |h[n]| < \infty$.
   Combining with Step 1:
   $$\text{BIBO Stability} \iff \sum_{n=-\infty}^\infty |h[n]| < \infty \iff \{z \in \mathbb{C} : |z| = 1\} \subset \text{ROC}(H)$$
   This proves that BIBO stability is equivalent to the ROC encompassing the unit circle.

3. **Causal Rational Systems:**
   If $\mathcal{H}$ is causal, $h[n] = 0$ for all $n < 0$. The Z-transform is:
   $$H(z) = \sum_{n=0}^\infty h[n] z^{-n}$$
   For a causal system with rational transfer function $H(z) = \frac{B(z)}{A(z)}$, the ROC is the exterior of a disk bounded by the magnitude of its outermost pole:
   $$\text{ROC}(H) = \left\{ z \in \mathbb{C} : |z| > R_{\max} \right\}, \quad \text{where } R_{\max} = \max_{k} |p_k|$$
   where $\{p_k\}$ are the poles of $H(z)$ (roots of $A(z)$).

4. **Pole Placement Criterion:**
   For the unit circle $\{z \in \mathbb{C} : |z| = 1\}$ to be contained in the open region $\{z \in \mathbb{C} : |z| > R_{\max}\}$, we must have:
   $$R_{\max} < 1 \iff \max_k |p_k| < 1 \iff |p_k| < 1 \quad \forall k$$
   If any pole satisfies $|p_k| \ge 1$, then $R_{\max} \ge 1$, which forces the ROC to exclude the unit circle (or causes the sum on the unit circle to diverge), rendering the causal system unstable.
   Thus, a causal LTI system is BIBO stable if and only if all poles of $H(z)$ lie strictly inside the unit circle. $\blacksquare$
```

---

## 5. Verification Method

Once the Worker applies these blueprints to `04a`, `08a`, and `15a`:

1. **Direct Test Execution:**
   Run the dedicated E2E test runner:
   ```bash
   python3 -m unittest -v .agents/test_suite/run_e2e_tests.py
   ```
   Or execute directly via the Python test framework:
   ```bash
   python3 -c "import sys; sys.path.insert(0, '.agents/test_suite'); from run_e2e_tests import QualityTestSuiteRunner; r = QualityTestSuiteRunner(); res = r.test_t1_28_bridge_course_rigorous_proof_expansions(); print(res.test_id, res.name, res.passed, res.message)"
   ```
   **Pass Condition:** Test `T1.28` reports `passed=True` with message `"All bridge courses contain complete step-by-step mathematical proofs"`.

2. **Display Math Count Validation:**
   In each of the three files, verify that the proof section contains at least 6 `$$` delimiters (each of our blueprints contains $\ge 16$ `$$` delimiters).
   ```bash
   python3 -c "
   import re, glob
   files = [
       '01 - Curriculum/Year 1 - Fundamentals/04a - Differential Equations Bridge.md',
       '01 - Curriculum/Year 1 - Fundamentals/08a - Circuits and Electronics Bridge.md',
       '01 - Curriculum/Year 2 - Systems/15a - Signals and Systems Bridge.md'
   ]
   for f in files:
       text = open(f).read()
       proof = re.search(r'## 📝 Study Notes[^\n]*\n(.*?)(?=\n## |\Z)', text, re.DOTALL).group(1)
       count = len(re.findall(r'\$\$', proof))
       print(f'{f}: {count//2} display math environments (target >= 3)')
   "
   ```

3. **Tombstone Q.E.D. Verification:**
   Verify that each proof ends with `$\blacksquare$`:
   ```bash
   grep -n "\\blacksquare" "01 - Curriculum/Year 1 - Fundamentals/04a - Differential Equations Bridge.md"
   grep -n "\\blacksquare" "01 - Curriculum/Year 1 - Fundamentals/08a - Circuits and Electronics Bridge.md"
   grep -n "\\blacksquare" "01 - Curriculum/Year 2 - Systems/15a - Signals and Systems Bridge.md"
   ```
   Each file will yield 3 matching lines.

4. **Invalidation Conditions:**
   - Any bridge file lacks `## 📝 Study Notes, Psets & Proofs`.
   - `len(re.findall(r"\$\$", body)) < 6` in any bridge file.
   - Any proof is missing a terminal `$\blacksquare$`.
   - Markdown list formatting introduces odd 3-space indentation.
