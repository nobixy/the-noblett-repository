---
block_id: "Block 15a"
title: "Signals and Systems Bridge (MIT 6.3000)"
term: "Year 2 Spring"
status: not-started
optional: true # computer-engineering path; excluded from the hour budget
hours_estimate: 160
hours_actual: 0
primary_resource: "Alan Oppenheim & Alan Willsky, Signals and Systems (2e) & MIT 6.003 / 6.3000 OCW"
milestone: "All 10 MIT 6.003 problem sets solved; discrete-time DSP audio processing suite built from scratch; MIT 6.003 final exam passed ≥80%"
date_started: ""
date_completed: ""
---

# Block 15a — Signals and Systems Bridge (MIT 6.3000)

[[00 - Dashboard|Dashboard]] / [[Checklist|Checklist]] / [[Math Index|Math Index]]

> [!NOTE] Optional — computer-engineering path
> Not required for MIT 6-3 (the [6-3 degree chart](https://catalog.mit.edu/degree-charts/computer-science-engineering-course-6-3/) doesn't require 6.3000). The source program adds 6.003 signals only for the full computer-engineering degree, where it is also [[Track 6 - Computer Engineering|Track 6]]'s second course. It sits outside the hour budget. [[Track 7 - TinyML and Edge AI|Track 7]] and [[Track 11 - Autonomous Robotics and Cyber-Physical Systems|Track 11]] list it as a prerequisite.

> [!INFO] Block Overview
> - **Term / Position:** Year 2 Spring (Following [[Linear Algebra]] and [[Probability]], preceding [[Operating Systems]] and Year 3 Depth)
> - **Estimated Hours:** ~160 hrs
> - **Status:** `not-started`
> - **Primary Resource:** Alan V. Oppenheim & Alan S. Willsky with S. Hamid Nawab, *Signals and Systems*, 2nd ed. (Prentice Hall) & MIT 6.003 / 6.3000 *Signal Processing*
> - **Key Milestone:** All 10 MIT 6.003 problem sets solved; discrete-time DSP audio processing suite built from scratch; MIT 6.003 final exam passed ≥80%

---

## 🎯 Why This Block Matters

Signals and Systems is the universal mathematical bridge linking physical analog reality to digital computation. 

In computer science curricula, data is typically modeled as discrete arrays, graphs, or hash maps. However, all physical information—audio speech waveforms, radio-frequency electromagnetic waves, medical MRI scanners, autonomous vehicle radar/LiDAR returns, and biological signals—originates as continuous-time functions of physical variables.

1. **The Frequency Domain Paradigm:** Time-domain representations often obscure essential structural properties. Transforming signals into the frequency domain decomposes complex waveforms into orthogonal complex exponential basis functions ($e^{j\omega t}$ and $z^n$), converting intractable differential/difference equations into simple algebraic multiplications ($Y(\omega) = H(\omega)X(\omega)$).
2. **Convolution & LTI System Theory:** The bedrock understanding of Linear Time-Invariant (LTI) systems guarantees that any system can be completely characterized by its response to an infinitely sharp impulse ($\delta(t)$ or $\delta[n]$), and its response to *any* arbitrary input is computed via convolution.
3. **The Information Bridge (Nyquist-Shannon Sampling):** The sampling theorem provides the mathematical guarantee of digital media: it specifies the exact condition under which a continuous physical signal can be sampled, digitized, stored in memory ([[Computer Systems]]), processed by software, and reconstructed back into physical reality with zero mathematical loss of information.
4. **Foundation for Cutting-Edge Disciplines:** Signals and systems directly underpins Digital Signal Processing (DSP), software-defined radio, audio/speech synthesis, computer vision convolutions, robotic feedback control ([[Differential Equations Bridge]]), and edge AI feature extraction ([[Track 7 - TinyML and Edge AI]]).

---

## 📖 Primary Syllabus & Core Content

The curriculum follows the canonical text by Oppenheim & Willsky (2nd Edition), synchronized with MIT 6.003 / 6.3000 lectures.

### Phase 1: Signal Foundations & Linear Time-Invariant Systems
- [ ] **Module 01: Mathematical Representation of Continuous and Discrete Signals**
  - Continuous-time (CT) signals $x(t)$ and discrete-time (DT) signals $x[n]$.
  - Signal energy $E_\infty = \int_{-\infty}^\infty |x(t)|^2 dt$ and power $P_\infty = \lim_{T \to \infty} \frac{1}{2T}\int_{-T}^T |x(t)|^2 dt$.
  - Independent variable transformations: time shifting $x(t - t_0)$, time scaling $x(at)$, time reversal $x(-t)$.
  - Periodic signals, fundamental period $T_0$, fundamental frequency $\omega_0 = 2\pi / T_0$.
  - Elementary mathematical signals: unit impulse $\delta(t)$ and $\delta[n]$, unit step $u(t)$ and $u[n]$, ramp function.
  - Complex exponential signals: $e^{st}$ where $s = \sigma + j\omega$; harmonically related complex exponentials $\phi_k(t) = e^{jk\omega_0 t}$.
  - Fundamental differences between CT and DT complex exponentials: periodicity of DT exponentials with respect to frequency ($e^{j(\omega + 2\pi)n} = e^{j\omega n}$), highest oscillation frequency at $\omega = \pi$.
- [ ] **Module 02: Linear Time-Invariant (LTI) Systems & Convolution**
  - System classifications: memoryless vs with memory, causal vs non-causal, invertible vs non-invertible, stable (BIBO stability) vs unstable, time-invariant vs time-varying, linear (superposition) vs non-linear.
  - Representation of DT signals as weighted superpositions of shifted impulses: $x[n] = \sum_{k=-\infty}^\infty x[k]\delta[n-k]$.
  - The discrete-time convolution sum: $y[n] = x[n] * h[n] = \sum_{k=-\infty}^\infty x[k]h[n-k]$.
  - Representation of CT signals as integrals of impulses: $x(t) = \int_{-\infty}^\infty x(\tau)\delta(t-\tau)d\tau$.
  - The continuous-time convolution integral: $y(t) = x(t) * h(t) = \int_{-\infty}^\infty x(\tau)h(t-\tau)d\tau$.
  - Mathematical properties of convolution: commutative, associative, distributive over addition.
  - Properties of LTI systems in terms of the impulse response $h$:
    - Memoryless condition: $h(t) = K\delta(t)$ or $h[n] = K\delta[n]$.
    - Invertibility: $h(t) * h_{inv}(t) = \delta(t)$.
    - Causality: $h(t) = 0$ for $t < 0$, $h[n] = 0$ for $n < 0$.
    - BIBO Stability: absolutely integrable impulse response $\int_{-\infty}^\infty |h(t)|dt < \infty$ or $\sum_{n=-\infty}^\infty |h[n]| < \infty$.
  - Step response $s(t) = \int_{-\infty}^t h(\tau)d\tau$ and $s[n] = \sum_{k=-\infty}^n h[k]$.

### Phase 2: Fourier Representations of Periodic & Aperiodic Signals
- [ ] **Module 03: Continuous-Time & Discrete-Time Fourier Series**
  - Response of LTI systems to complex exponentials: $e^{st} \to H(s)e^{st}$, where eigenvalue $H(s) = \int h(\tau)e^{-s\tau}d\tau$.
  - Continuous-Time Fourier Series (CTFS) of periodic signals:
    - Synthesis equation: $x(t) = \sum_{k=-\infty}^\infty a_k e^{jk\omega_0 t}$.
    - Analysis equation: $a_k = \frac{1}{T}\int_T x(t) e^{-jk\omega_0 t} dt$.
  - Convergence of Fourier series: Dirichlet conditions (bounded variation, finite discontinuities, absolutely integrable over a period).
  - Gibbs phenomenon at discontinuities; overshoot factor ($\approx 8.95\%$).
  - Parseval's relation for periodic signals: $\frac{1}{T}\int_T |x(t)|^2 dt = \sum_{k=-\infty}^\infty |a_k|^2$.
  - Discrete-Time Fourier Series (DTFS): finite summation over $N$ harmonics due to frequency periodicity.
- [ ] **Module 04: Continuous-Time Fourier Transform (CTFT)**
  - Derivation of CTFT as the continuous limit of CTFS as period $T \to \infty$.
  - The CTFT pair:
    - Synthesis (inverse transform): $x(t) = \frac{1}{2\pi}\int_{-\infty}^\infty X(j\omega)e^{j\omega t}d\omega$.
    - Analysis (forward transform): $X(j\omega) = \int_{-\infty}^\infty x(t)e^{-j\omega t}dt$.
  - Physical interpretation of magnitude spectrum $|X(j\omega)|$ and phase spectrum $\angle X(j\omega)$.
  - CTFT properties: linearity, time shifting ($x(t - t_0) \leftrightarrow e^{-j\omega t_0}X(j\omega)$), frequency shifting ($e^{j\omega_0 t}x(t) \leftrightarrow X(j(\omega - \omega_0))$), conjugation and conjugate symmetry, differentiation ($\frac{dx}{dt} \leftrightarrow j\omega X(j\omega)$), integration, time scaling ($x(at) \leftrightarrow \frac{1}{|a|}X(j\frac{\omega}{a})$), duality principle.
  - The Convolution Property: $x(t) * h(t) \stackrel{\mathcal{F}}{\longleftrightarrow} X(j\omega)H(j\omega)$.
  - The Modulation / Multiplication Property: $x(t)p(t) \stackrel{\mathcal{F}}{\longleftrightarrow} \frac{1}{2\pi}[X(j\omega) * P(j\omega)]$.
  - Parseval's theorem: $\int_{-\infty}^\infty |x(t)|^2 dt = \frac{1}{2\pi}\int_{-\infty}^\infty |X(j\omega)|^2 d\omega$.
- [ ] **Module 05: Discrete-Time Fourier Transform (DTFT)**
  - The DTFT pair for discrete sequences:
    - Synthesis equation: $x[n] = \frac{1}{2\pi}\int_{2\pi} X(e^{j\omega})e^{j\omega n}d\omega$.
    - Analysis equation: $X(e^{j\omega}) = \sum_{n=-\infty}^\infty x[n]e^{-j\omega n}$.
  - Inherent $2\pi$-periodicity of DTFT: $X(e^{j(\omega + 2\pi)}) = X(e^{j\omega})$.
  - Properties of DTFT: linearity, time and frequency shifts, differencing, accumulation, convolution in DT, duality between DTFS and DTFT.
- [ ] **Module 06: Discrete Fourier Transform (DFT) & Fast Fourier Transform (FFT)**
  - Sampling the DTFT at $N$ uniformly spaced frequency points $\omega_k = \frac{2\pi k}{N}$.
  - The $N$-point Discrete Fourier Transform (DFT):
    - Forward DFT: $X[k] = \sum_{n=0}^{N-1} x[n] W_N^{kn}$, where twiddle factor $W_N = e^{-j\frac{2\pi}{N}}$.
    - Inverse DFT (IDFT): $x[n] = \frac{1}{N}\sum_{k=0}^{N-1} X[k] W_N^{-kn}$.
  - Circular convolution vs linear convolution; zero-padding techniques to achieve linear convolution via DFT.
  - The Cooley-Tukey Radix-2 Decimation-in-Time (DIT) FFT algorithm:
    - Decomposition into even and odd index sub-transforms: $X[k] = E[k] + W_N^k O[k]$.
    - Butterfly computation structure; bit-reversal indexing.
    - Computational complexity proof: reducing arithmetic from $\mathcal{O}(N^2)$ to $\mathcal{O}(N \log_2 N)$.

### Phase 3: The Sampling Theorem & Transform Analysis
- [ ] **Module 07: The Nyquist-Shannon Sampling Theorem & Aliasing**
  - Mathematical model of sampling: multiplication by an impulse train $p(t) = \sum_{n=-\infty}^\infty \delta(t - nT)$.
  - Spectrum of sampled signal: $X_p(j\omega) = \frac{1}{T}\sum_{k=-\infty}^\infty X(j(\omega - k\omega_s))$, where $\omega_s = \frac{2\pi}{T}$.
  - Nyquist Criterion: exact, distortionless recovery of $x(t)$ requires sampling rate $\omega_s > 2\omega_M$ (where $\omega_M$ is the highest frequency present in $x(t)$).
  - Aliasing distortion: spectral overlap when $\omega_s < 2\omega_M$; high frequencies folding into low-frequency spectrum.
  - Ideal bandlimited reconstruction: filtering $X_p(j\omega)$ through an ideal low-pass filter of gain $T$ and cutoff $\omega_c = \omega_s / 2$.
  - Time-domain interpolation: Whittaker-Shannon interpolation formula $x(t) = \sum_{n=-\infty}^\infty x(nT) \text{sinc}\left(\frac{\pi(t - nT)}{T}\right)$.
  - Practical considerations: anti-aliasing low-pass analog filters; Zero-Order Hold (ZOH) digital-to-analog reconstruction and aperture distortion correction.
- [ ] **Module 08: The Laplace Transform & s-Domain Transfer Functions**
  - Bilateral Laplace transform: $X(s) = \int_{-\infty}^\infty x(t)e^{-st}dt$, where complex frequency $s = \sigma + j\omega$.
  - The Region of Convergence (ROC): geometry in the complex $s$-plane (vertical strips); properties of the ROC (does not contain poles; bounded by poles; for right-sided signals, ROC is $\text{Re}\{s\} > \sigma_{max}$).
  - Pole-zero constellations in the $s$-plane.
  - System transfer function $H(s) = \frac{Y(s)}{X(s)}$.
  - LTI System properties determined by poles and ROC:
    - Causality: ROC is an open right-half plane to the right of the rightmost pole.
    - BIBO Stability: ROC includes the imaginary axis ($j\omega$-axis), meaning all poles of a causal stable system must satisfy $\text{Re}\{s_p\} < 0$ (strict left-half plane).
  - Inverse Laplace transform via partial fraction expansion.
  - Unilateral Laplace transform and solution of linear ordinary differential equations with non-zero initial conditions.
- [ ] **Module 09: The Z-Transform & Discrete System Dynamics**
  - Bilateral Z-transform: $X(z) = \sum_{n=-\infty}^\infty x[n]z^{-n}$, where complex variable $z = r e^{j\omega}$.
  - Region of Convergence (ROC) geometry in the $z$-plane (concentric rings).
  - Mapping between $s$-plane and $z$-plane: $z = e^{sT}$; mapping the left-half $s$-plane into the interior of the unit circle $|z| < 1$, and the imaginary axis $j\omega$ onto the unit circle $|z| = 1$.
  - System transfer function $H(z) = \frac{\sum b_k z^{-k}}{\sum a_k z^{-k}}$.
  - Causality and stability in the $z$-plane:
    - A causal discrete LTI system is BIBO stable if and only if all poles of $H(z)$ lie strictly inside the unit circle ($|z_p| < 1$).
  - Inverse Z-transform via partial fraction expansion and long division.
  - Difference equations to rational $Z$-domain transfer functions: $y[n] - \sum a_k y[n-k] = \sum b_k x[n-k]$.

### Phase 4: Filter Design, Bode Plots & Feedback
- [ ] **Module 10: Frequency Response, Linear Phase & Group Delay**
  - Frequency response magnitude $|H(e^{j\omega})|$ and unwrapped phase $\theta(\omega) = \arg H(e^{j\omega})$.
  - Ideal delay system: linear phase response $\theta(\omega) = -\alpha \omega$; group delay $\tau_g(\omega) = -\frac{d\theta(\omega)}{d\omega} = \alpha$.
  - Phase distortion vs magnitude distortion; the necessity of linear-phase filters in audio and image processing.
  - First-order and second-order discrete-time systems: pole placement, resonance, bandwidth, and damping.
- [ ] **Module 11: Digital Filter Design (FIR and IIR)**
  - Filter specifications: passband ripple $\delta_1$, stopband attenuation $\delta_2$, transition band $\Delta \omega$.
  - Finite Impulse Response (FIR) filters:
    - Linear phase conditions: symmetric vs antisymmetric impulse responses (Types I, II, III, IV).
    - Windowing design method: truncation of ideal sinc impulse response using rectangular, Hamming, Hanning, and Blackman windows; spectral trade-off between main-lobe width and side-lobe leakage.
  - Infinite Impulse Response (IIR) filters:
    - Classical analog prototypes: Butterworth (maximally flat magnitude), Chebyshev Type I (equiripple passband), Chebyshev Type II (equiripple stopband), Elliptic (equiripple passband and stopband).
    - The Bilinear Transformation: algebraic mapping $s = \frac{2}{T}\left(\frac{1 - z^{-1}}{1 + z^{-1}}\right)$; preservation of stability; non-linear frequency warping $\Omega = \frac{2}{T}\tan\left(\frac{\omega}{2}\right)$ and pre-warping design steps.
- [ ] **Module 12: Feedback, Stability & Control Theory Foundations**
  - Closed-loop feedback systems: open-loop transfer function $G(s)$, feedback path $H(s)$, closed-loop transfer function $T(s) = \frac{G(s)}{1 + G(s)H(s)}$.
  - Root Locus analysis: trajectory of closed-loop poles as open-loop gain $K$ varies from $0 \to \infty$.
  - The Nyquist Stability Criterion: Cauchy's argument principle; encirclement of the critical $-1 + j0$ point in the complex plane.
  - Gain margin and phase margin: metrics of closed-loop robustness.

---

## 🛠️ Build Requirement

### The Deliverable: Standalone Discrete-Time DSP Audio Suite & Spectral Analyzer in C / Rust
You must implement a production-grade, zero-dependency digital signal processing engine from scratch in pure C or Rust (no external libraries like `FFTW`, `scipy.signal`, or `numpy` allowed for the core mathematical engine):

1. **Core Mathematical Engines (from first principles):**
  - **Radix-2 Cooley-Tukey FFT & IFFT:** In-place decimation-in-time implementation supporting power-of-two transforms ($N=64$ to $N=16384$). Must use bit-reversal permutation and precomputed twiddle factor tables.
  - **Direct Convolution Engine:** Both direct time-domain convolution $\mathcal{O}(N^2)$ and fast FFT-based overlap-add convolution $\mathcal{O}(N \log N)$ for arbitrary length audio streams.
2. **Filter Synthesis & Application Modules:**
  - **FIR Filter Generator:** Windowed-sinc FIR filter designer supporting Low-Pass, High-Pass, and Band-Pass responses with selectable Hamming, Hanning, and Blackman windows.
  - **IIR Biquad Cascade Filter:** 2nd-order Direct Form II Transposed biquad filter structure ($y[n] = b_0 x[n] + b_1 x[n-1] + b_2 x[n-2] - a_1 y[n-1] - a_2 y[n-2]$). Implement digital Butterworth low-pass and high-pass filters via bilinear transformation with frequency pre-warping.
3. **Parametric Audio Graphic Equalizer:**
  - Cascade a 5-band parametric equalizer for standard 16-bit 44.1 kHz PCM audio files (`.wav`):
    - Band 1: Sub-bass low-shelf ($80\text{ Hz}$)
    - Band 2: Low-mid peaking ($300\text{ Hz}$)
    - Band 3: Mid peaking ($1\text{ kHz}$)
    - Band 4: High-mid peaking ($3.5\text{ kHz}$)
    - Band 5: Treble high-shelf ($10\text{ kHz}$)
  - User-configurable gain ($-12\text{ dB}$ to $+12\text{ dB}$) per band.
4. **Short-Time Fourier Transform (STFT) Spectral Analyzer:**
  - Compute the STFT of input audio using a sliding analysis window (length $N=1024$, $75\%$ overlap).
  - Generate a 2D ASCII or BMP spectrogram displaying energy distribution across time and frequency.
5. **Verification & Test Suite:**
  - Unit test verifying FFT output against analytical Discrete Fourier Transforms with mean squared error $< 10^{-7}$.
  - Numerical test verifying Parseval's energy conservation theorem between time domain and frequency domain.
  - Filtering test demonstrating $\ge 40\text{ dB}$ stopband attenuation on a dual-tone synthetic test signal ($1\text{ kHz} + 10\text{ kHz}$).

---

## 🏁 Done When

> [!IMPORTANT]
> A block is done when this condition is true. Not before.
- [ ] All 10 MIT 6.003 problem sets completed with full mathematical solutions.
- [ ] Custom FFT engine passes precision unit tests and executes within $3\times$ the speed of unvectorized C reference code on $N=4096$.
- [ ] Audio DSP engine successfully parses, filters, and outputs a valid 16-bit PCM WAV file with measured frequency attenuation matching specifications.
- [ ] STFT spectrogram generator outputs an accurate visual time-frequency representation of a frequency chirp signal.
- [ ] MIT 6.003 / 6.3000 Final Examination completed under strict closed-book conditions (3 hours) scoring $\ge 80\%$.

---

## 📝 Study Notes, Psets & Proofs

*Your atomic notes, problem-set proofs, and build notes go here — written by you, from a blank page.*

> [!TIP]- Check your work (only after your own blank-sheet attempt)
> OCW [6.003 (Fall 2011)](https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/) posts quiz solutions, including quizzes from earlier terms.

---

## 🔄 Appendix A Alternatives (Failover)

*Only consult if primary genuinely isn't working after two honest weeks:*
- **Textbooks:**
  - John G. Proakis & Dimitris G. Manolakis, *Digital Signal Processing: Principles, Algorithms, and Applications*, 5th ed., Pearson. (Comprehensive, industry standard for digital filters and multirate DSP).
  - Steven W. Smith, *The Scientist and Engineer's Guide to Digital Signal Processing*, California Technical Publishing (Available free online at dspguide.com; the best practical intuition guide).
- **Online Courses:**
  - Berkeley EECS 120: *Signals and Systems* (inst.eecs.berkeley.edu/~ee120/).
  - Stanford EE 261: *The Fourier Transform and its Applications* (Brad Osgood).

---

## 🧭 Navigation
- **Topic Hub:** [[Math Index|Math Index]] | [[Checklist|Master Checklist]]
- **Sequential Flow:** [[Probability|← 15 - Probability]] | [[00 - Dashboard|Dashboard]] | [[Operating Systems|16 - Operating Systems →]]
