---
title: "22 - Statistics — Worked Proofs"
type: reference
tags:
  - reference
  - answer-key
---

# 22 - Statistics — Worked Proofs

> [!WARNING] Answer key — open only after your own attempt
> These derivations were generated as reference material, not study notes. Reading them first creates the illusion of competence that [[how-i-study]] warns about.
> Protocol: attempt the proof from a blank sheet in [[Statistics]] → compare here → log every gap you found.
> They are unverified; treat any step you cannot justify as a possible error, not as authority.

Back to: [[Statistics]] · [[Worked Proofs Index]]

---

### Proof 1: The Neyman-Pearson Lemma (Most Powerful Test)
**Theorem**: Let $X$ be a random vector with joint density $f(x;\theta)$ on sample space $\mathcal{X}$. Consider testing the simple null hypothesis $H_0: \theta = \theta_0$ against the simple alternative $H_1: \theta = \theta_1$. Let the likelihood ratio be defined as:
$$\Lambda(x) = \frac{f(x; \theta_1)}{f(x; \theta_0)}$$
Define a critical test function $\phi^*(x) \in [0, 1]$ (where $\phi(x)$ represents the probability of rejecting $H_0$ given observation $x$):
$$\phi^*(x) = \begin{cases} 1 & \text{if } \Lambda(x) > k \\ \gamma & \text{if } \Lambda(x) = k \\ 0 & \text{if } \Lambda(x) < k \end{cases}$$
where constants $k \ge 0$ and $\gamma \in [0, 1]$ are chosen such that the test has exact size $\alpha$:
$$\mathbb{E}_{\theta_0}[\phi^*(X)] = \int_{\mathcal{X}} \phi^*(x) f(x; \theta_0) \, dx = \alpha$$
Then for any competing test function $\phi(x)$ satisfying $\mathbb{E}_{\theta_0}[\phi(X)] \le \alpha$, the power of $\phi^*$ is at least that of $\phi$:
$$\mathbb{E}_{\theta_1}[\phi^*(X)] \ge \mathbb{E}_{\theta_1}[\phi(X)]$$

**Proof**:
1. Consider the product quantity for any observation $x \in \mathcal{X}$:
   $$\Delta(x) = (\phi^*(x) - \phi(x)) \big( f(x; \theta_1) - k f(x; \theta_0) \big)$$
2. We analyze the sign of $\Delta(x)$ across the three partitions of $\mathcal{X}$:
  - If $\Lambda(x) > k$, then $f(x; \theta_1) - k f(x; \theta_0) > 0$. By definition, $\phi^*(x) = 1$. Since $\phi(x) \le 1$, $\phi^*(x) - \phi(x) = 1 - \phi(x) \ge 0$. Hence $\Delta(x) \ge 0$.
  - If $\Lambda(x) < k$, then $f(x; \theta_1) - k f(x; \theta_0) < 0$. By definition, $\phi^*(x) = 0$. Since $\phi(x) \ge 0$, $\phi^*(x) - \phi(x) = -\phi(x) \le 0$. The product of two non-positive quantities is non-negative: $\Delta(x) \ge 0$.
  - If $\Lambda(x) = k$, then $f(x; \theta_1) - k f(x; \theta_0) = 0$, so $\Delta(x) = 0$.
   Therefore, $\Delta(x) \ge 0$ pointwise for all $x \in \mathcal{X}$.
3. Integrate $\Delta(x)$ over the entire sample space $\mathcal{X}$:
   $$\int_{\mathcal{X}} (\phi^*(x) - \phi(x)) \big( f(x; \theta_1) - k f(x; \theta_0) \big) \, dx \ge 0$$
4. Expanding the integral:
   $$\int_{\mathcal{X}} (\phi^*(x) - \phi(x)) f(x; \theta_1) \, dx - k \int_{\mathcal{X}} (\phi^*(x) - \phi(x)) f(x; \theta_0) \, dx \ge 0$$
   $$\implies \Big( \mathbb{E}_{\theta_1}[\phi^*(X)] - \mathbb{E}_{\theta_1}[\phi(X)] \Big) \ge k \Big( \mathbb{E}_{\theta_0}[\phi^*(X)] - \mathbb{E}_{\theta_0}[\phi(X)] \Big)$$
5. By construction, $\mathbb{E}_{\theta_0}[\phi^*(X)] = \alpha$, and by assumption for the competitor test, $\mathbb{E}_{\theta_0}[\phi(X)] \le \alpha$. Hence:
   $$\mathbb{E}_{\theta_0}[\phi^*(X)] - \mathbb{E}_{\theta_0}[\phi(X)] \ge \alpha - \alpha = 0$$
   Since $k \ge 0$, the right-hand side is non-negative:
   $$\mathbb{E}_{\theta_1}[\phi^*(X)] - \mathbb{E}_{\theta_1}[\phi(X)] \ge k \cdot 0 = 0$$
   $$\implies \mathbb{E}_{\theta_1}[\phi^*(X)] \ge \mathbb{E}_{\theta_1}[\phi(X)] \quad \blacksquare$$

---

### Proof 2: The Cramér-Rao Lower Bound & Fisher Information
**Theorem**: Let $X \sim f(x; \theta)$ where $\theta \in \Theta \subseteq \mathbb{R}$. Assume the standard regularity conditions:
1. The support $\{x : f(x; \theta) > 0\}$ does not depend on $\theta$.
2. The log-likelihood is twice differentiable with respect to $\theta$.
3. The integral $\int f(x; \theta) dx$ can be differentiated under the integral sign.

Define the score function $S(X; \theta) = \frac{\partial}{\partial \theta} \ln f(X; \theta)$, and the Fisher Information $I(\theta) = \mathbb{E}_\theta \left[ \left( \frac{\partial \ln f(X; \theta)}{\partial \theta} \right)^2 \right]$.
Let $T(X)$ be any unbiased estimator of $\psi(\theta)$, so $\mathbb{E}_\theta[T(X)] = \psi(\theta)$.
Then:
$$\text{Var}_\theta(T(X)) \ge \frac{[\psi'(\theta)]^2}{I(\theta)}$$
In particular, for an unbiased estimator of $\theta$ itself ($\psi(\theta) = \theta$), $\text{Var}_\theta(T(X)) \ge \frac{1}{I(\theta)}$.

**Proof**:
1. First, we establish the mean of the score function. Since $\int f(x; \theta) dx = 1$, differentiate both sides with respect to $\theta$:
   $$\frac{\partial}{\partial \theta} \int f(x; \theta) \, dx = \int \frac{\partial f(x; \theta)}{\partial \theta} \, dx = 0$$
   Using $\frac{\partial f(x; \theta)}{\partial \theta} = f(x; \theta) \frac{\partial \ln f(x; \theta)}{\partial \theta}$:
   $$\int \left( \frac{\partial \ln f(x; \theta)}{\partial \theta} \right) f(x; \theta) \, dx = \mathbb{E}_\theta[S(X; \theta)] = 0$$
2. Second, differentiate the unbiasedness relation $\mathbb{E}_\theta[T(X)] = \int T(x) f(x; \theta) dx = \psi(\theta)$ with respect to $\theta$:
   $$\frac{\partial}{\partial \theta} \int T(x) f(x; \theta) \, dx = \int T(x) \frac{\partial f(x; \theta)}{\partial \theta} \, dx = \psi'(\theta)$$
   Rewriting with the score function:
   $$\int T(x) \left( \frac{\partial \ln f(x; \theta)}{\partial \theta} \right) f(x; \theta) \, dx = \mathbb{E}_\theta [T(X) S(X; \theta)] = \psi'(\theta)$$
3. Now evaluate the covariance between $T(X)$ and $S(X; \theta)$:
   $$\text{Cov}_\theta(T(X), S(X; \theta)) = \mathbb{E}_\theta[T(X) S(X; \theta)] - \mathbb{E}_\theta[T(X)] \mathbb{E}_\theta[S(X; \theta)]$$
   Since $\mathbb{E}_\theta[S(X; \theta)] = 0$:
   $$\text{Cov}_\theta(T(X), S(X; \theta)) = \psi'(\theta)$$
4. By the Cauchy-Schwarz inequality for random variables:
   $$\big[ \text{Cov}_\theta(T(X), S(X; \theta)) \big]^2 \le \text{Var}_\theta(T(X)) \cdot \text{Var}_\theta(S(X; \theta))$$
   Note that $\text{Var}_\theta(S(X; \theta)) = \mathbb{E}_\theta[S(X; \theta)^2] - (\mathbb{E}_\theta[S(X; \theta)])^2 = I(\theta)$.
   Substituting these terms:
   $$[\psi'(\theta)]^2 \le \text{Var}_\theta(T(X)) \cdot I(\theta)$$
   Assuming $I(\theta) > 0$, dividing by $I(\theta)$ yields:
   $$\text{Var}_\theta(T(X)) \ge \frac{[\psi'(\theta)]^2}{I(\theta)} \quad \blacksquare$$

---

### Proof 3: Vapnik-Chervonenkis (VC) Dimension & PAC Generalization Bounds
**Theorem**: Let $\mathcal{H}$ be a binary hypothesis class with finite VC-dimension $d = \text{VC}(\mathcal{H}) < \infty$ mapping domain $\mathcal{X} \to \{0, 1\}$. Let $\mathcal{D}$ be an arbitrary distribution over $\mathcal{X}$, and let $S = \{x_1, \dots, x_m\} \sim \mathcal{D}^m$ be an i.i.d. training sample.
Define true risk $R(h) = \mathbb{P}_{x \sim \mathcal{D}}(h(x) \ne y)$ and empirical risk $R_S(h) = \frac{1}{m} \sum_{i=1}^m \mathbb{I}(h(x_i) \ne y_i)$.
Then for any $\delta \in (0, 1)$, with probability at least $1 - \delta$ over the draw of $S$:
$$\sup_{h \in \mathcal{H}} |R(h) - R_S(h)| \le \mathcal{O}\left( \sqrt{\frac{d \ln(m/d) + \ln(1/\delta)}{m}} \right)$$

**Derivation Chain**:
1. **Symmetrization via Ghost Sample**:
   Let $S' = \{x'_1, \dots, x'_m\}$ be an independent ghost sample drawn from $\mathcal{D}^m$. By Chebyshev's inequality, if $|R(h) - R_S(h)| > \epsilon$, then with high probability $R_{S'}(h)$ is close to $R(h)$ for $m \ge 2/\epsilon^2$. Thus:
   $$\mathbb{P}_S \left( \sup_{h \in \mathcal{H}} |R(h) - R_S(h)| > \epsilon \right) \le 2 \, \mathbb{P}_{S, S'} \left( \sup_{h \in \mathcal{H}} |R_{S'}(h) - R_S(h)| > \frac{\epsilon}{2} \right)$$
2. **Rademacher Symmetrization**:
   Introduce independent Rademacher random variables $\sigma_i \in \{-1, +1\}$ with $\mathbb{P}(\sigma_i = 1) = \mathbb{P}(\sigma_i = -1) = 1/2$. The distribution of $R_{S'}(h) - R_S(h) = \frac{1}{m} \sum_{i=1}^m (L(h, x'_i) - L(h, x_i))$ is identical to $\frac{1}{m} \sum_{i=1}^m \sigma_i (L(h, x'_i) - L(h, x_i))$. Applying triangle inequality bounds this by $4 \mathcal{R}_m(\mathcal{H})$ where $\mathcal{R}_m(\mathcal{H})$ is the empirical Rademacher complexity:
   $$\mathcal{R}_m(\mathcal{H}) = \mathbb{E}_\sigma \left[ \sup_{h \in \mathcal{H}} \frac{1}{m} \sum_{i=1}^m \sigma_i h(x_i) \right]$$
3. **Sauer-Shelah Lemma**:
   The growth function $\Pi_{\mathcal{H}}(m) = \max_{x_1, \dots, x_m} |\{(h(x_1), \dots, h(x_m)) : h \in \mathcal{H}\}|$. By the Sauer-Shelah lemma, for all $m$:
   $$\Pi_{\mathcal{H}}(m) \le \sum_{i=0}^d \binom{m}{i} \le \left( \frac{e m}{d} \right)^d$$
4. **Massart's Finite Class Lemma**:
   For a finite hypothesis class of size $|\mathcal{H}_{|S}| \le \Pi_{\mathcal{H}}(m)$, Massart's lemma yields:
   $$\mathcal{R}_m(\mathcal{H}_{|S}) \le \sqrt{\frac{2 \ln \Pi_{\mathcal{H}}(m)}{m}} \le \sqrt{\frac{2 d \ln(e m / d)}{m}}$$
5. **Concentration via McDiarmid's Inequality**:
   Let $g(S) = \sup_{h \in \mathcal{H}} |R(h) - R_S(h)|$. Replacing a single sample point changes $g(S)$ by at most $1/m$. McDiarmid's inequality guarantees:
   $$\mathbb{P}(g(S) - \mathbb{E}[g(S)] \ge \epsilon) \le \exp\left( -2 m \epsilon^2 \right)$$
   Setting $\delta = \exp(-2 m \epsilon^2)$ and solving for $\epsilon$, we combine with the Rademacher bound to obtain:
   $$\sup_{h \in \mathcal{H}} |R(h) - R_S(h)| \le 2 \sqrt{\frac{2 d \ln(e m / d)}{m}} + \sqrt{\frac{\ln(2/\delta)}{2m}} = \mathcal{O}\left( \sqrt{\frac{d \ln(m/d) + \ln(1/\delta)}{m}} \right) \quad \blacksquare$$

---

### 📄 Landmark Research Papers (from [[Paper Reading Hub|Paper Reading Hub]])

The following foundational paper from the [[Paper Reading Hub|Paper Reading Hub]] is assigned to Block 22. Analyze using the Keshav Three-Pass Methodology:

1. **"Proximal Policy Optimization Algorithms"** (John Schulman et al., 2017)
    - *Venue:* arXiv:1707.06347 (Paper 30 in [[Paper Reading Hub|Paper Reading Hub]])
    - *Landmark Invariant:* Clipped surrogate objective preventing destructively large policy updates in reinforcement learning: $L^{\text{CLIP}}(\theta) = \hat{\mathbb{E}}_t [\min(r_t(\theta)\hat{A}_t, \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon)\hat{A}_t)]$.
    - *Reading Guidance:* Focus Pass 2 on the variance reduction derivation of Generalized Advantage Estimation (GAE) and the comparison to Trust Region Policy Optimization (TRPO).
