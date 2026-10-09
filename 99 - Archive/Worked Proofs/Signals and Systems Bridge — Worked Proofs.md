---
title: "15a - Signals and Systems Bridge — Worked Proofs"
type: reference
tags:
  - reference
  - answer-key
---

# 15a - Signals and Systems Bridge — Worked Proofs

> [!WARNING] Answer key — open only after your own attempt
> These derivations were generated as reference material, not study notes. Reading them first creates the illusion of competence that [[how-i-study]] warns about.
> Protocol: attempt the proof from a blank sheet in [[B15a - Signals and Systems Bridge|Signals and Systems Bridge]] → compare here → log every gap you found.
> They are unverified; treat any step you cannot justify as a possible error, not as authority.

Back to: [[B15a - Signals and Systems Bridge|Signals and Systems Bridge]] · [[Worked Proofs Index]]

---

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
