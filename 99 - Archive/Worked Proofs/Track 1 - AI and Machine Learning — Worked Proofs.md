---
title: "Track 1 - AI and Machine Learning — Worked Proofs"
type: reference
tags:
  - reference
  - answer-key
---

# Track 1 - AI and Machine Learning — Worked Proofs

> [!WARNING] Answer key — open only after your own attempt
> These derivations were generated as reference material, not study notes. Reading them first creates the illusion of competence that [[how-i-study]] warns about.
> Protocol: attempt the proof from a blank sheet in [[Track 1 - AI and Machine Learning]] → compare here → log every gap you found.
> They are unverified; treat any step you cannot justify as a possible error, not as authority.

Back to: [[Track 1 - AI and Machine Learning]] · [[Worked Proofs Index]]

---

### Proof 1: Universal Approximation Theorem (Hornik 1989 / Cybenko 1989)
**Theorem**: Let $\sigma: \mathbb{R} \to \mathbb{R}$ be any continuous bounded, non-constant sigmoidal activation function (or continuous non-polynomial function). Let $K \subset \mathbb{R}^d$ be a compact subset. Let $C(K)$ denote the Banach space of continuous functions on $K$ endowed with the supremum norm $\|f\|_\infty = \sup_{x \in K} |f(x)|$.
Define the family of single-hidden-layer feedforward networks:
$$\Sigma_d(\sigma) = \left\{ F(x) = \sum_{i=1}^m \alpha_i \sigma(w_i^T x + b_i) : m \in \mathbb{N}, \, \alpha_i, b_i \in \mathbb{R}, \, w_i \in \mathbb{R}^d \right\}$$
Then $\Sigma_d(\sigma)$ is dense in $C(K)$; that is, for any $f \in C(K)$ and any $\epsilon > 0$, there exists $F \in \Sigma_d(\sigma)$ such that:
$$\|F - f\|_\infty < \epsilon$$

**Proof (Functional Analysis via Hahn-Banach and Riesz Representation Theorem)**:
1. By the Hahn-Banach theorem and the Riesz-Markov-Kakutani representation theorem, a linear subspace $\mathcal{M} \subset C(K)$ is dense in $C(K)$ if and only if the only bounded signed regular Borel measure $\mu \in \mathcal{M}(K)$ that annihilates $\mathcal{M}$ (i.e., $\int_K g(x) d\mu(x) = 0$ for all $g \in \mathcal{M}$) is the zero measure $\mu = 0$.
2. Note that the linear span of $\Sigma_d(\sigma)$ is $\Sigma_d(\sigma)$ itself. Suppose $\mu \in \mathcal{M}(K)$ satisfies:
   $$\int_K \sigma(w^T x + b) \, d\mu(x) = 0 \quad \forall w \in \mathbb{R}^d, \, b \in \mathbb{R}$$
3. For fixed $w \in \mathbb{R}^d$ and $b \in \mathbb{R}$, define the one-dimensional pushforward measure $\nu_w = w_\sharp \mu$ on $\mathbb{R}$ by $\nu_w(E) = \mu(\{x \in K : w^T x \in E\})$. Then:
   $$\int_{\mathbb{R}} \sigma(y + b) \, d\nu_w(y) = 0 \quad \forall b \in \mathbb{R}$$
4. Convolve the activation $\sigma$ with the measure $\nu_w$:
   $$(\sigma * \nu_w)(b) = \int_{\mathbb{R}} \sigma(y + b) \, d\nu_w(y) = 0$$
   Since this convolution is identically zero for all shifts $b$, its Fourier transform (in the sense of tempered distributions) vanishes:
   $$\widehat{\sigma * \nu_w} = \hat{\sigma} \cdot \hat{\nu}_w = 0$$
5. Because $\sigma$ is a non-constant bounded function, its distribution derivative $\sigma'$ is non-zero and has non-empty support in the frequency domain. Specifically, the set where $\hat{\sigma} = 0$ is isolated or nowhere dense. Since $\hat{\nu}_w(t) = \int_{\mathbb{R}} e^{-i t y} d\nu_w(y)$ is real-analytic (as $\mu$ has compact support $K$), $\hat{\nu}_w$ can only vanish on an open set if it is identically zero everywhere.
6. Thus, $\hat{\nu}_w(t) = 0$ for all $t \in \mathbb{R}$, which implies:
   $$\int_K e^{-i t w^T x} \, d\mu(x) = 0 \quad \forall t \in \mathbb{R}, \, w \in \mathbb{R}^d$$
7. Setting $t=1$, we have that the Fourier transform of $\mu$:
   $$\hat{\mu}(w) = \int_K e^{-i w^T x} \, d\mu(x) = 0 \quad \forall w \in \mathbb{R}^d$$
8. By the uniqueness theorem for Fourier transforms of finite Borel measures on $\mathbb{R}^d$, $\hat{\mu} \equiv 0 \implies \mu = 0$.
9. Since the only annihilating measure is the zero measure, $\Sigma_d(\sigma)$ is dense in $C(K)$ with respect to the uniform topology. $\blacksquare$

---

### Proof 2: Deep Neural Network Generalization & Contraction Bounds (Talagrand's Lemma)

> [!NOTE]
> The general statistical learning framework—including McDiarmid's bounded differences inequality, ghost sample symmetrization, and uniform PAC bounds via empirical Rademacher complexity and VC-dimension—is rigorously established in [[Statistics|22 - Statistics]] (see Proof 3: Vapnik-Chervonenkis Dimension & PAC Generalization Bounds). 
> Below, Track 1 specializes these bounds to deep neural architectures using **Talagrand's Contraction Lemma** and layer-wise Lipschitz bounds.

**Theorem (Talagrand's Contraction Lemma for Neural Networks):**
Let $\phi_i: \mathbb{R} \to \mathbb{R}$ be $L$-Lipschitz functions with $\phi_i(0) = 0$ for all $i \in \{1, \dots, m\}$. For any bounded hypothesis set $\mathcal{H} \subset \mathbb{R}^{\mathcal{X}}$ and empirical sample $S = \{x_1, \dots, x_m\}$, the empirical Rademacher complexity satisfies:
$$\hat{\mathcal{R}}_S(\phi \circ \mathcal{H}) \le L \, \hat{\mathcal{R}}_S(\mathcal{H})$$
Consequently, for an $L$-layer feedforward neural network $f(x) = W_L \sigma(W_{L-1} \dots \sigma(W_1 x))$ with 1-Lipschitz activation functions $\sigma$ (e.g., ReLU or GELU) with $\|x\|_2 \le B$ and spectral norm bounds $\|W_l\|_2 \le M_l$, the generalization error scales with the product of spectral norms rather than parameter count:
$$R(f) \le R_S(f) + \mathcal{O}\left( \frac{B \prod_{l=1}^L M_l}{\sqrt{m}} \right) + 3 \sqrt{\frac{\ln(2/\delta)}{2m}}$$

**Proof Derivation:**
1. **Reduction to Single Coordinate Contraction:**
   By induction on the sample size $m$, it suffices to establish that for any coordinate function $\phi: \mathbb{R} \to \mathbb{R}$ that is $L$-Lipschitz with $\phi(0) = 0$:
   $$\mathbb{E}_\sigma \left[ \sup_{h \in \mathcal{H}} \left( \sum_{i=1}^{m-1} \sigma_i h(x_i) + \sigma_m \phi(h(x_m)) \right) \right] \le L \, \mathbb{E}_\sigma \left[ \sup_{h \in \mathcal{H}} \left( \sum_{i=1}^{m-1} \sigma_i h(x_i) + \sigma_m h(x_m) \right) \right]$$
2. **Conditional Expectation over the Final Rademacher Variable:**
   Without loss of generality, assume $L = 1$ (dividing $\phi$ by $L$). Conditioning on $\sigma_1, \dots, \sigma_{m-1}$ and denoting $u(h) = \sum_{i=1}^{m-1} \sigma_i h(x_i)$, the expectation over $\sigma_m \in \{-1, +1\}$ is:
   $$E = \frac{1}{2} \sup_{h_1 \in \mathcal{H}} [u(h_1) + \phi(h_1(x_m))] + \frac{1}{2} \sup_{h_2 \in \mathcal{H}} [u(h_2) - \phi(h_2(x_m))]$$
   $$E = \frac{1}{2} \sup_{h_1, h_2 \in \mathcal{H}} [u(h_1) + u(h_2) + \phi(h_1(x_m)) - \phi(h_2(x_m))]$$
3. **Application of the Lipschitz Condition:**
   Since $\phi$ is 1-Lipschitz, $|\phi(a) - \phi(b)| \le |a - b|$. 
    - If $h_1(x_m) \ge h_2(x_m)$, then $\phi(h_1(x_m)) - \phi(h_2(x_m)) \le h_1(x_m) - h_2(x_m)$.
    - If $h_1(x_m) < h_2(x_m)$, then $\phi(h_1(x_m)) - \phi(h_2(x_m)) \le h_2(x_m) - h_1(x_m)$.
   In both cases:
   $$\phi(h_1(x_m)) - \phi(h_2(x_m)) \le |h_1(x_m) - h_2(x_m)|$$
   Substituting back:
   $$E \le \frac{1}{2} \sup_{h_1, h_2 \in \mathcal{H}} [u(h_1) + u(h_2) + h_1(x_m) - h_2(x_m)] = \mathbb{E}_{\sigma_m} \left[ \sup_{h \in \mathcal{H}} [u(h) + \sigma_m h(x_m)] \right]$$
4. **Inductive Composition Across Layers:**
   Repeating this argument across all $m$ coordinates yields $\hat{\mathcal{R}}_S(\phi \circ \mathcal{H}) \le L \, \hat{\mathcal{R}}_S(\mathcal{H})$.
   Applying this layer-by-layer through network $f(x) = W_L \sigma(W_{L-1} \dots \sigma(W_1 x))$:
   Because the activation $\sigma$ is 1-Lipschitz ($\sigma(0)=0$ for ReLU/GELU), each non-linear activation contracts without blowing up Rademacher complexity. 
   The linear transformation at layer $l$ scales the complexity by at most the matrix operator norm $\|W_l\|_2$.
5. **Final Bound Integration:**
   Composing the contraction lemma with the foundational concentration bounds in [[Statistics|22 - Statistics]] yields the norm-based uniform generalization bound:
   $$R(f) \le R_S(f) + 2 \hat{\mathcal{R}}_S(\mathcal{H}_{\text{NN}}) + 3 \sqrt{\frac{\ln(2/\delta)}{2m}} \le R_S(f) + \mathcal{O}\left( \frac{B \prod_{l=1}^L \|W_l\|_2}{\sqrt{m}} \right) + 3 \sqrt{\frac{\ln(2/\delta)}{2m}} \quad \blacksquare$$
