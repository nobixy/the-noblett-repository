---
title: "15 - Probability — Worked Proofs"
type: reference
tags:
  - reference
  - answer-key
---

# 15 - Probability — Worked Proofs

> [!WARNING] Answer key — open only after your own attempt
> These derivations were generated as reference material, not study notes. Reading them first creates the illusion of competence that [[how-i-study]] warns about.
> Protocol: attempt the proof from a blank sheet in [[B15 - Probability|Probability]] → compare here → log every gap you found.
> They are unverified; treat any step you cannot justify as a possible error, not as authority.

Back to: [[B15 - Probability|Probability]] · [[Worked Proofs Index]]

---

### 1. Carathéodory's Extension Theorem & Outer Measures
**Theorem (Carathéodory 1914):** Let $\Omega$ be an arbitrary set, $\mathcal{A} \subseteq 2^\Omega$ an algebra of subsets, and $\mu_0 : \mathcal{A} \to [0, \infty]$ a pre-measure (satisfying $\mu_0(\emptyset) = 0$ and countable additivity on disjoint sets in $\mathcal{A}$ whose union is in $\mathcal{A}$).

#### Construction of Outer Measure:
For any arbitrary subset $E \subseteq \Omega$, define the outer measure $\mu^* : 2^\Omega \to [0, \infty]$:
$$\mu^*(E) = \inf \left\{ \sum_{n=1}^\infty \mu_0(A_n) : A_n \in \mathcal{A}, \, E \subseteq \bigcup_{n=1}^\infty A_n \right\}$$
$\mu^*$ satisfies:
1. $\mu^*(\emptyset) = 0$.
2. Monotonicity: $E_1 \subseteq E_2 \implies \mu^*(E_1) \le \mu^*(E_2)$.
3. Countable Subadditivity: $\mu^*(\bigcup_{n=1}^\infty E_n) \le \sum_{n=1}^\infty \mu^*(E_n)$.

#### Carathéodory Measurability Condition:
A set $A \subseteq \Omega$ is called *$\mu^*$-measurable* (written $A \in \mathcal{M}$) if for every test set $E \subseteq \Omega$:
$$\mu^*(E) = \mu^*(E \cap A) + \mu^*(E \cap A^c)$$
*(By subadditivity, $\mu^*(E) \le \mu^*(E \cap A) + \mu^*(E \cap A^c)$ is automatic; measurability requires the reverse inequality $\mu^*(E) \ge \mu^*(E \cap A) + \mu^*(E \cap A^c)$).*

#### Extension Guarantee:
1. The collection $\mathcal{M}$ of $\mu^*$-measurable sets forms a $\sigma$-algebra.
2. $\sigma(\mathcal{A}) \subseteq \mathcal{M}$ (every element of the generated $\sigma$-algebra is measurable).
3. The restriction $\mu = \mu^*|_{\mathcal{M}}$ is a countably additive measure, and for all $A \in \mathcal{A}$, $\mu(A) = \mu_0(A)$.
4. If $\mu_0$ is $\sigma$-finite, the extension of $\mu_0$ to $\sigma(\mathcal{A})$ is strictly unique. $\blacksquare$

---

### 2. The Radon-Nikodym Theorem & Conditional Expectation
**Theorem (Radon 1913, Nikodym 1930):** Let $(\Omega, \mathcal{F}, \mu)$ be a $\sigma$-finite measure space, and let $\nu$ be a $\sigma$-finite measure on $(\Omega, \mathcal{F})$ that is *absolutely continuous* with respect to $\mu$ (written $\nu \ll \mu$, defined as $\forall A \in \mathcal{F}: \mu(A) = 0 \implies \nu(A) = 0$).

Then there exists a non-negative $\mathcal{F}$-measurable function $f : \Omega \to [0, \infty)$, unique up to $\mu$-almost everywhere equivalence, such that for all $A \in \mathcal{F}$:
$$\nu(A) = \int_A f \, d\mu$$
The function $f$ is the *Radon-Nikodym derivative*, denoted $f = \frac{d\nu}{d\mu}$.

#### Foundation of Measure-Theoretic Conditional Expectation:
Let $(\Omega, \mathcal{F}, P)$ be a probability space, $X \in L^1(\Omega, \mathcal{F}, P)$ an integrable random variable, and $\mathcal{G} \subseteq \mathcal{F}$ a sub-$\sigma$-algebra representing partial information.
1. Define a signed measure $\nu_X$ on $(\Omega, \mathcal{G})$ by:
   $$\nu_X(G) = \int_G X \, dP \quad \text{for } G \in \mathcal{G}$$
2. Observe that $\nu_X \ll P|_\mathcal{G}$ (if $P(G) = 0$, then $\int_G X dP = 0$).
3. By the Radon-Nikodym Theorem, there exists a unique $\mathcal{G}$-measurable random variable, denoted $\mathbb{E}[X \mid \mathcal{G}] = \frac{d\nu_X}{d(P|_\mathcal{G})}$, satisfying:
   $$\int_G \mathbb{E}[X \mid \mathcal{G}] \, dP = \int_G X \, dP \quad \forall G \in \mathcal{G}$$
4. **Hilbert Space Geometry ($L^2$ Projection):** When $X \in L^2(P)$, $\mathbb{E}[X \mid \mathcal{G}]$ is the unique orthogonal projection of $X$ onto the closed subspace $L^2(\Omega, \mathcal{G}, P)$, minimizing the mean-square error $\mathbb{E}[(X - Y)^2]$ over all $\mathcal{G}$-measurable $Y$. $\blacksquare$

---

### 3. Doob's Martingale Convergence Theorem
**Theorem (Doob 1953):** Let $(X_n)_{n \ge 0}$ be a submartingale adapted to filtration $(\mathcal{F}_n)_{n \ge 0}$, satisfying the $L^1$ boundedness condition:
$$\sup_{n \ge 0} \mathbb{E}[X_n^+] < \infty \quad (\text{where } X_n^+ = \max(X_n, 0))$$
Then there exists a random variable $X_\infty$ such that $X_n \to X_\infty$ almost surely as $n \to \infty$, with $\mathbb{E}[|X_\infty|] < \infty$.

#### Proof via Doob's Upcrossing Inequality:
For any interval $[a, b]$ with $-\infty < a < b < \infty$, let $U_N[a, b]$ denote the number of upcrossings of $[a, b]$ completed by the sample path $X_0, X_1, \dots, X_N$.
1. **Doob's Upcrossing Lemma:**
   $$(b - a) \mathbb{E}[U_N[a, b]] \le \mathbb{E}[(X_N - a)^+] - \mathbb{E}[(X_0 - a)^+] \le \mathbb{E}[X_N^+] + |a|$$
2. **Infinite Upcrossing Bound:**
   Taking the limit as $N \to \infty$ via the Monotone Convergence Theorem:
   $$\mathbb{E}[U_\infty[a, b]] = \lim_{N \to \infty} \mathbb{E}[U_N[a, b]] \le \frac{\sup_{n} \mathbb{E}[X_n^+] + |a|}{b - a} < \infty$$
   Because the expectation is finite, $P(U_\infty[a, b] = \infty) = 0$.
3. **Almost Sure Convergence:**
   The divergence event $\{\lim_{n \to \infty} X_n \text{ does not exist}\}$ occurs if and only if $\liminf_{n \to \infty} X_n < \limsup_{n \to \infty} X_n$.
   $$\left\{ \liminf_{n \to \infty} X_n < \limsup_{n \to \infty} X_n \right\} = \bigcup_{\substack{a < b \\ a, b \in \mathbb{Q}}} \left\{ \liminf_{n \to \infty} X_n < a < b < \limsup_{n \to \infty} X_n \right\} \subseteq \bigcup_{\substack{a < b \\ a, b \in \mathbb{Q}}} \{ U_\infty[a, b] = \infty \}$$
   Since the set of rational pairs $(a, b) \in \mathbb{Q}^2$ is countable, by countable subadditivity:
   $$P\left( \liminf_{n \to \infty} X_n < \limsup_{n \to \infty} X_n \right) \le \sum_{\substack{a < b \\ a, b \in \mathbb{Q}}} P(U_\infty[a, b] = \infty) = 0$$
   Therefore, $\lim_{n \to \infty} X_n = X_\infty$ exists almost surely. Fatou's Lemma guarantees $\mathbb{E}[|X_\infty|] \le \liminf \mathbb{E}[|X_n|] < \infty$. $\blacksquare$

---

### 📄 Landmark Research Papers (from [[Paper Reading Hub|Paper Reading Hub]])

The following foundational paper from the [[Paper Reading Hub|Paper Reading Hub]] is assigned to Block 15. Analyze using the Keshav Three-Pass Methodology:

1. **"Deep Unsupervised Learning using Nonequilibrium Thermodynamics"** (Jascha Sohl-Dickstein, Eric A. Weiss, Niru Maheswaranathan, Surya Ganguli, 2015)
    - *Venue:* ICML 2015 (Paper 28 in [[Paper Reading Hub|Paper Reading Hub]])
    - *Landmark Invariant:* Physical foundation of diffusion probabilistic models: reversing a forward Markovian Gaussian perturbation process to learn complex data distributions.
    - *Reading Guidance:* Focus Pass 2 on the forward diffusion kernel, reverse trajectory transition probability formulation, and variational lower bound on log-likelihood.
