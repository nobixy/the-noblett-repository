---
title: "Lab 01 — Fourier by Ear"
module: "12-math-for-engineering"
hours: 15
unit: S1
---

# Lab 01 — Fourier by Ear

**Goal:** understand the idea that every signal is a sum of sine waves — by building it, hearing it, and seeing it: implement the discrete Fourier transform (DFT), then the fast Fourier transform (FFT) by divide and conquer, analyse your Tone Loom sounds and your Pico Thermostat's sensor noise, and design a simple filter.

**Time:** about 15 hours, in five sessions.

**Deliverable:** a lab report: *"What frequencies are in my signals, and what does a filter do to them?"*

---

## Session 1 — Adding waves (3 hours)

1. With Tone Loom (or NumPy), build a **square wave** as a sum of sines: sin(x) + sin(3x)/3 + sin(5x)/5 + … (odd harmonics, decreasing amplitude). Plot the sum with 1, 3, 10, 50 terms. Listen to each at 220 Hz. Watch the corners sharpen (and the overshoot at the corners that never goes away — the Gibbs phenomenon).
2. Answer Tone Loom's old question [W]: *why does a square wave sound buzzy?* (It *is* a stack of higher frequencies.)
3. **Complex numbers, briefly:** a point on the unit circle at angle θ is cos θ + i·sin θ = e^{iθ} (M10's circle picture, written as one number). Multiplying by e^{iθ} rotates. Practise with Python's `cmath`. This is the language the DFT is written in.

---

## Session 2 — The DFT (3 hours)

For N samples x₀ … x_{N−1}, the DFT gives N complex numbers:

$$X_k = \sum_{n=0}^{N-1} x_n \, e^{-2\pi i k n / N}$$

**In words:** X_k measures "how much of the frequency that completes k cycles in the window" the signal contains — by spinning the signal around the circle at that frequency and seeing whether it adds up or cancels out. |X_k| is the strength; the angle is the phase.

1. Implement it directly (two nested loops — O(N²), M11). Test: a pure sine at bin 5 gives peaks at k = 5 and k = N − 5 (the mirror image for real signals [W: why?]).
2. Frequency of bin k = k × sample rate ÷ N. Analyse 0.1 s of a Tone Loom note: does the peak land at the note's frequency?
3. Compare your DFT with `numpy.fft.fft` (second witness): differences under 1e-9.

---

## Session 3 — The FFT (3 hours)

The DFT for N a power of 2 can be computed in O(N log N) by **splitting the samples into even- and odd-indexed halves**, transforming each half (recursively — Module 02 Lab 01!), and combining them with "twiddle factors" e^{−2πik/N}. Derive the combination step from the formula (write the sum as even terms + odd terms) [S], then implement the recursive radix-2 FFT.

1. Test against your DFT and NumPy.
2. Time DFT vs your FFT vs NumPy for N = 2⁸ … 2¹⁶. Plot on log-log axes; read off the slopes (Module 05 Lab 01): ≈ 2 vs ≈ 1 (plus a little).
3. **[W]:** this is divide and conquer, like merge sort. Where exactly does the saving come from?

---

## Session 4 — Spectra of your own signals (3 hours)

1. **Tone Loom:** the spectrum of a sine, a square, a sawtooth, and a chord. Then the **aliasing** files from Tone Loom Milestone 5: show the 30 kHz tone appearing at 14.1 kHz in the spectrum, and explain it with the sampling picture.
2. **Windowing:** analyse a tone whose frequency doesn't fit a whole number of cycles in the window. The peak smears ("spectral leakage"). Multiply by a Hann window first and compare. [W] Why does tapering the ends help?
3. **Your voice:** record a sustained vowel (Audacity → WAV) and find its fundamental frequency and harmonics.
4. **Pico Thermostat noise:** take a long logged sensor series (heater off). Its spectrum: is the noise "white" (flat) or concentrated at some frequencies? (Mains hum at 50/60 Hz can't appear in a 1 Hz log — why not? Aliasing again.)

---

## Session 5 — Filters (3 hours)

1. **Moving average** of M samples is a filter. Compute its **frequency response** (the DFT of its M-sample impulse response, zero-padded) and plot it: it's a low-pass filter with ripples.
2. Apply it to a Tone Loom chord with high-frequency noise added; listen before and after; show both spectra.
3. Apply it to the thermostat's noisy readings; compare with Pico Thermostat Milestone 1's averaging (same idea, now with a frequency-domain explanation).
4. **Convolution theorem (look it up):** filtering in time = multiplying spectra. Verify numerically: filter by direct convolution and by FFT → multiply → inverse FFT; same result.

---

## Lab report

Question, methods, the square-wave build-up, DFT vs FFT timing, spectra of your signals (including aliasing and windowing), and the filter's effect in both domains. End with three sentences explaining the Fourier idea to a beginner.

## Done when

- [ ] DFT and FFT implemented and witnessed by NumPy; timing plot.
- [ ] Spectra of four kinds of your own signals; windowing comparison.
- [ ] Moving-average filter analysed and applied; convolution theorem verified.
- [ ] Report written.

## Retrieval and reflection

1. **[R]:** the DFT formula and its meaning; bin frequency; the FFT's split; aliasing; leakage and windows; what a low-pass filter does.
2. **[F] (spoken, 3 min):** "What does a Fourier transform do?" — with a chord as the example.
