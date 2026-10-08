---
title: "32 - Information Theory — Worked Proofs"
type: reference
tags:
  - reference
  - answer-key
---

# 32 - Information Theory — Worked Proofs

> [!WARNING] Answer key — open only after your own attempt
> These derivations were generated as reference material, not study notes. Reading them first creates the illusion of competence that [[how-i-study]] warns about.
> Protocol: attempt the proof from a blank sheet in [[Information Theory]] → compare here → log every gap you found.
> They are unverified; treat any step you cannot justify as a possible error, not as authority.

Back to: [[Information Theory]] · [[Worked Proofs Index]]

---

### Proof 1: Shannon's Source Coding Theorem & Asymptotic Equipartition Property (AEP)
**Theorem**: Let $X_1, X_2, \dots, X_n$ be i.i.d. discrete random variables drawn from alphabet $\mathcal{X}$ with probability mass function $p(x)$ and Shannon entropy $H(X) = -\sum_{x \in \mathcal{X}} p(x) \log_2 p(x)$.
1. For any $\epsilon > 0$, the typical set $A_\epsilon^{(n)}$ satisfies:
  - For all $x^n \in A_\epsilon^{(n)}$, $2^{-n(H(X) + \epsilon)} \le p(x_1, \dots, x_n) \le 2^{-n(H(X) - \epsilon)}$.
  - $\mathbb{P}(A_\epsilon^{(n)}) > 1 - \epsilon$ for sufficiently large $n$.
  - $(1 - \epsilon) 2^{n(H(X) - \epsilon)} \le |A_\epsilon^{(n)}| \le 2^{n(H(X) + \epsilon)}$.
2. Consequently, the minimum expected codeword length per symbol $L_n$ for lossless data compression satisfies:
   $$\lim_{n \to \infty} \frac{L_n}{n} = H(X)$$

**Proof**:
1. By the **Weak Law of Large Numbers (WLLN)**:
   Consider the random variables $Y_i = -\log_2 p(X_i)$. Notice that $Y_1, \dots, Y_n$ are i.i.d. with mean:
   $$\mathbb{E}[Y_i] = -\sum_{x \in \mathcal{X}} p(x) \log_2 p(x) = H(X)$$
   and finite variance $\sigma^2 = \text{Var}(-\log_2 p(X)) < \infty$.
   The sample average is $-\frac{1}{n} \log_2 p(X_1, \dots, X_n) = \frac{1}{n} \sum_{i=1}^n Y_i$.
   By WLLN, as $n \to \infty$, the sample average converges in probability to its mean:
   $$\forall \epsilon > 0, \quad \lim_{n \to \infty} \mathbb{P}\left( \left| -\frac{1}{n} \log_2 p(X_1, \dots, X_n) - H(X) \right| < \epsilon \right) = 1$$
2. Define the typical set $A_\epsilon^{(n)}$:
   $$A_\epsilon^{(n)} = \left\{ x^n \in \mathcal{X}^n : \left| -\frac{1}{n} \log_2 p(x^n) - H(X) \right| \le \epsilon \right\}$$
   By WLLN, $\mathbb{P}(A_\epsilon^{(n)}) > 1 - \epsilon$ for $n$ sufficiently large.
3. For any $x^n \in A_\epsilon^{(n)}$:
   $$H(X) - \epsilon \le -\frac{1}{n} \log_2 p(x^n) \le H(X) + \epsilon \implies 2^{-n(H(X) + \epsilon)} \le p(x^n) \le 2^{-n(H(X) - \epsilon)}$$
4. To bound the cardinality $|A_\epsilon^{(n)}|$:
   $$1 = \sum_{x^n \in \mathcal{X}^n} p(x^n) \ge \sum_{x^n \in A_\epsilon^{(n)}} p(x^n) \ge |A_\epsilon^{(n)}| 2^{-n(H(X) + \epsilon)} \implies |A_\epsilon^{(n)}| \le 2^{n(H(X) + \epsilon)}$$
   Similarly, for large $n$:
   $$1 - \epsilon < \mathbb{P}(A_\epsilon^{(n)}) = \sum_{x^n \in A_\epsilon^{(n)}} p(x^n) \le |A_\epsilon^{(n)}| 2^{-n(H(X) - \epsilon)} \implies |A_\epsilon^{(n)}| \ge (1 - \epsilon) 2^{n(H(X) - \epsilon)}$$
5. **Coding Construction**:
   Assign binary strings of length $\lceil n(H(X) + \epsilon) \rceil + 1$ to each sequence in $A_\epsilon^{(n)}$ (with leading prefix bit 0).
   Assign binary strings of length $\lceil n \log_2 |\mathcal{X}| \rceil + 1$ to the remaining non-typical sequences (with leading prefix bit 1).
   The expected codeword length is:
   $$\begin{aligned}
   \mathbb{E}[\ell(X^n)] &= \sum_{x^n \in A_\epsilon^{(n)}} p(x^n) \ell(x^n) + \sum_{x^n \notin A_\epsilon^{(n)}} p(x^n) \ell(x^n) \\
   &\le (n(H(X) + \epsilon) + 2) + \epsilon (n \log_2 |\mathcal{X}| + 2)
   \end{aligned}$$
   Dividing by $n$ and taking $n \to \infty$ then $\epsilon \to 0$:
   $$\lim_{n \to \infty} \frac{\mathbb{E}[\ell(X^n)]}{n} \le H(X)$$
   By Kraft's inequality and the converse of source coding, no uniquely decodable code can achieve expected length less than $H(X)$. Hence $\lim_{n \to \infty} \frac{L_n}{n} = H(X)$. $\blacksquare$

---

### Proof 2: Shannon's Noisy-Channel Coding Theorem
**Theorem**: Consider a Discrete Memoryless Channel (DMC) defined by transition probabilities $p(y|x)$ with input alphabet $\mathcal{X}$, output alphabet $\mathcal{Y}$, and channel capacity:
$$C = \max_{p(x)} I(X; Y)$$
For any transmission rate $R < C$ and any $\epsilon > 0$, there exists an integer $n_0$ such that for all block lengths $n \ge n_0$, there exists an $(2^{nR}, n)$ code with maximum probability of error:
$$\lambda^{(n)} = \max_{i \in \{1,\dots,2^{nR}\}} \mathbb{P}(\hat{W} \ne i | W = i) < \epsilon$$
Conversely, any sequence of codes with rate $R > C$ must have probability of error bounded away from zero ($\lambda^{(n)} \to 1$ as $n \to \infty$).

**Proof (Random Coding & Joint Typicality)**:
1. **Random Codebook Generation**:
   Fix the input distribution $p(x)$ that achieves capacity $C = I(X; Y)$.
   Generate $2^{nR}$ independent codewords $X^n(1), X^n(2), \dots, X^n(2^{nR})$ of length $n$, each drawn i.i.d. according to $\mathbb{P}(X^n = x^n) = \prod_{i=1}^n p(x_i)$.
   The codebook $\mathcal{C}$ is revealed to both transmitter and receiver.
2. **Joint Typicality Decoding**:
   The transmitter wishes to send message $W \in \{1, \dots, 2^{nR}\}$. It transmits $X^n(W)$.
   The channel outputs sequence $Y^n \sim \prod_{i=1}^n p(y_i | x_i)$.
   The receiver decodes $\hat{W} = i$ if $(X^n(i), Y^n) \in A_\epsilon^{(n)}$ (jointly typical) and no other $j \ne i$ satisfies $(X^n(j), Y^n) \in A_\epsilon^{(n)}$. Otherwise, the receiver declares an error.
3. **Error Decomposition**:
   By symmetry of the random code construction, the average probability of error does not depend on the transmitted message. Assume $W = 1$:
   $$\bar{P}_e = \mathbb{P}(\hat{W} \ne 1 | W = 1) \le \mathbb{P}\big( (X^n(1), Y^n) \notin A_\epsilon^{(n)} \big) + \sum_{j=2}^{2^{nR}} \mathbb{P}\big( (X^n(j), Y^n) \in A_\epsilon^{(n)} \big)$$
4. **Bounding Error Terms via Joint AEP**:
  - By the Joint Asymptotic Equipartition Property, $(X^n(1), Y^n)$ are generated from the true joint distribution $p(x^n, y^n)$. Thus for $n$ sufficiently large:
     $$\mathbb{P}\big( (X^n(1), Y^n) \notin A_\epsilon^{(n)} \big) < \epsilon / 2$$
  - For any competitor $j \ne 1$, $X^n(j)$ was generated independently of $Y^n$. The pair $(X^n(j), Y^n)$ is distributed according to the product of marginals $p(x^n) p(y^n)$.
  - By the Joint AEP lemma, the probability that two independent sequences are jointly typical is:
     $$\mathbb{P}\big( (X^n(j), Y^n) \in A_\epsilon^{(n)} \big) \le 2^{-n(I(X; Y) - 3\epsilon)}$$
5. Combining terms:
   $$\bar{P}_e < \frac{\epsilon}{2} + \sum_{j=2}^{2^{nR}} 2^{-n(I(X; Y) - 3\epsilon)} < \frac{\epsilon}{2} + 2^{nR} \cdot 2^{-n(I(X; Y) - 3\epsilon)} = \frac{\epsilon}{2} + 2^{-n(I(X; Y) - R - 3\epsilon)}$$
6. If $R < I(X; Y) - 3\epsilon = C - 3\epsilon$, the exponent $-n(C - R - 3\epsilon)$ is strictly negative. As $n \to \infty$, $2^{-n(C - R - 3\epsilon)} \to 0$.
   Hence for large $n$, $\bar{P}_e < \epsilon$.
7. Since the ensemble average error over all codebooks $\mathbb{E}_{\mathcal{C}}[\bar{P}_e] < \epsilon$, there exists at least one deterministic codebook $\mathcal{C}^*$ with average error $P_e < \epsilon$.
   Discarding the worst $50\%$ of codewords reduces the maximum error $\lambda^{(n)} \le 2 P_e < 2\epsilon$ while reducing rate by only $\frac{1}{n} \to 0$. $\blacksquare$

---

### Proof 3: The Rate-Distortion Theorem
**Theorem**: Let source $X$ have distribution $p(x)$ with distortion measure $d(x, \hat{x}) \ge 0$. The information rate-distortion function $R(D)$ is given by:
$$R(D) = \min_{p(\hat{x}|x) : \sum_{x, \hat{x}} p(x) p(\hat{x}|x) d(x, \hat{x}) \le D} I(X; \hat{X})$$
$R(D)$ represents the infimum of all rates $R$ such that there exists a sequence of source codes $(2^{nR}, n)$ with distortion $\mathbb{E}\left[\frac{1}{n}\sum_{i=1}^n d(X_i, \hat{X}_i)\right] \le D + \epsilon$ as $n \to \infty$.

**Converse Proof (Information Inequality)**:
1. Suppose we have a code $(2^{nR}, n)$ with encoder $f: \mathcal{X}^n \to \{1, \dots, 2^{nR}\}$ and decoder $g: \{1, \dots, 2^{nR}\} \to \hat{\mathcal{X}}^n$ such that $\mathbb{E}[d(X^n, \hat{X}^n)] \le D$.
2. The rate $nR$ bounds the mutual information between the source block and its reproduction:
   $$nR \ge H(f(X^n)) \ge I(X^n; f(X^n)) \ge I(X^n; \hat{X}^n)$$
3. By the chain rule for mutual information:
   $$I(X^n; \hat{X}^n) = H(X^n) - H(X^n | \hat{X}^n) = \sum_{i=1}^n H(X_i) - \sum_{i=1}^n H(X_i | X^{i-1}, \hat{X}^n)$$
   Conditioning reduces entropy: $H(X_i | X^{i-1}, \hat{X}^n) \le H(X_i | \hat{X}_i)$. Thus:
   $$I(X^n; \hat{X}^n) \ge \sum_{i=1}^n (H(X_i) - H(X_i | \hat{X}_i)) = \sum_{i=1}^n I(X_i; \hat{X}_i)$$
4. Let $D_i = \mathbb{E}[d(X_i, \hat{X}_i)]$. By definition of the rate-distortion function $R(D)$:
   $$I(X_i; \hat{X}_i) \ge R(D_i)$$
5. Since $R(D)$ is a convex function of $D$, by Jensen's inequality:
   $$nR \ge \sum_{i=1}^n R(D_i) \ge n R\left( \frac{1}{n} \sum_{i=1}^n D_i \right) = n R(D)$$
   Dividing both sides by $n$ yields $R \ge R(D)$.
   Hence, no lossy compression code can achieve distortion $D$ with rate less than $R(D)$. $\blacksquare$

---

### 📄 Landmark Research Papers (from [[Paper Reading Hub|Paper Reading Hub]])

The following foundational paper from the [[Paper Reading Hub|Paper Reading Hub]] is assigned to Block 32. Analyze using the Keshav Three-Pass Methodology:

1. **"A Mathematical Theory of Communication"** (Claude E. Shannon, 1948)
    - *Venue:* Bell System Technical Journal (Paper 34 in [[Paper Reading Hub|Paper Reading Hub]])
    - *Landmark Invariant:* Information entropy $H(X) = -\sum p_i \log_2 p_i$, source coding theorem, and noisy channel coding theorem capacity limit $C = B \log_2(1 + \text{SNR})$.
    - *Reading Guidance:* Focus Pass 2 on the axiomatic derivation of entropy, the typical set argument in the noisy channel coding theorem, and the geometric sphere-packing intuition in high dimensions.
