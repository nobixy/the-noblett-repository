---
title: "12 — Math for Engineering"
id: "MOD12"
type: "overview"
module: "12-math-for-engineering"
phase: "C"
order: 850
prerequisites: [FND-MA-ASSESS, MOD03-U6, MOD03-U8]
checkpoints: [MOD12-C1, MOD12-C2, MOD12-C3, MOD12-L1, MOD12-L2, MOD12-L3, MOD12-L4, MOD12-P1, MOD12-P2, MOD12-P3, MOD12-S1, MOD12-CLOSE]
tags: [module, math, calculus, linear-algebra, probability]
---

# 12 — Math for Engineering

**Calculus, linear algebra, probability, and signals — learned by computing with them on your own data.** Measure your own motion with your phone and integrate it into a path; simulate springs and circuits and see why some numerical methods drift; transform and compress images with matrices; rank the notes in your vault by their links with eigenvectors; fit your own forgetting curve with confidence intervals; and hear the Fourier transform at work in your Tone Loom sounds.

This module runs **alongside** Modules 06–11 as your math sessions (the same rotation as the foundations), starting after [Math M11](../00-foundations/math/M11-functions-exponentials-and-logarithms.md) and its [track assessment](../00-foundations/math/overview.md#track-assessment). It is a math track, not a build module: its labs and units can run beside your current build project; its three projects (Motion Lab, Matrix Studio, Chance Lab) each count as your one open build project while you work on them (rule 2 in [Start Here](<../00 - Start Here.md>)).

---

## Prerequisites

- Math foundations **M01–M11** complete (the track assessment passed).
- [03 Discrete Math](../03-discrete-math/overview.md) Units 6 and 8 (counting, discrete probability).
- Python with NumPy and matplotlib (`sudo pacman -S python-numpy python-matplotlib`). Rule: **implement each core algorithm yourself first** (in plain Python or with NumPy arrays), then use NumPy's version as a second witness and for speed.

## Objectives

By the end you will be able to:
1. Explain derivatives and integrals as rates and accumulations, compute them exactly for common functions and numerically for data, and estimate numerical error.
2. Solve differential equations numerically (Euler, RK4) and explain stability and drift.
3. Use vectors and matrices for geometry and data: transformations, linear systems, least squares, eigenvectors, and the SVD.
4. Model randomness with distributions; use expectation and variance; explain the law of large numbers and the central limit theorem by simulation.
5. Estimate quantities from data with confidence intervals, and run an honest experiment with a test.
6. Explain sampling and frequency, implement the DFT and FFT, and design a simple filter.

## The units

Each unit lists what to learn, where (free texts), and which project uses it. Study the way Module 03 does: worked examples with subgoal labels [S], mixed problem sets [I], blank-sheet recall [R], a Feynman pass per unit [F], and a why-ladder on every definition [W].

**Free texts:** **OpenStax *Calculus* Volumes 1–3** (openstax.org) · **3Blue1Brown, *Essence of Calculus* and *Essence of Linear Algebra*** (YouTube — watch these first in each area; they build intuition superbly) · **Gilbert Strang, *Introduction to Linear Algebra*** (book) with **MIT 18.06** on OCW (lectures and problem sets with solutions) · **Grinstead & Snell, *Introduction to Probability*** (free PDF) · **Allen Downey, *Think Stats*** (free) · **Seeing Theory** (seeing-theory.brown.edu, interactive).

| Unit | Title | Key ideas | Project |
| :-- | :-- | :-- | :-- |
| C1 | Rates and derivatives | slope as a limit; derivative rules; numerical differentiation and its error; Newton's method | [Motion Lab](projects/motion-lab/spec.md) |
| C2 | Accumulation and integrals | area as a limit of sums; the fundamental theorem; numerical integration (trapezoid, Simpson) and error | Motion Lab |
| C3 | Differential equations | rates that depend on the state; exponential growth/decay (your RC circuit, your forgetting curve); oscillators; Euler vs RK4; stability | Motion Lab |
| L1 | Vectors | geometry; dot product, length, angle; cosine similarity | [Matrix Studio](projects/matrix-studio/spec.md) |
| L2 | Matrices as transformations | composition; inverses; determinants as area scaling; homogeneous coordinates | Matrix Studio |
| L3 | Linear systems and least squares | Gaussian elimination with pivoting; LU; projections; least squares | Matrix Studio |
| L4 | Eigenvectors and the SVD | power iteration; Markov chains and PageRank; singular values; low-rank approximation | Matrix Studio, Chance Lab |
| P1 | Random variables | distributions (Bernoulli, binomial, geometric, Poisson, uniform, exponential, normal); simulation | [Chance Lab](projects/chance-lab/spec.md) |
| P2 | Expectation and limits | expectation, variance, covariance; law of large numbers; central limit theorem | Chance Lab |
| P3 | Inference | estimators; confidence intervals; bootstrap; hypothesis tests; permutation tests; experimental design | Chance Lab |
| S1 | Signals | sampling and aliasing; the DFT and FFT; frequency response; simple filters | [Lab 01](labs/lab-01-fourier-by-ear.md) |

The projects (Motion Lab, Matrix Studio, Chance Lab) are built on the units they use and run beside the build modules. **Chance Lab comes last:** it models Courier's packet loss and reuses its throughput measurements, so it waits until [Courier](../09-networking/projects/courier/spec.md) (Module 09) is done (Phase D in Start Here). Motion Lab and Matrix Studio do not depend on any build module after 05.

**Suggested order:** C1 → C2 → L1 → L2 → C3 → L3 → P1 → P2 → L4 → P3 → S1, interleaving projects as their units finish.

## How the study methods run through this module

| Protocol | In this module |
| :-- | :-- |
| **R** | Warm-up, every session: a derivation or procedure from a blank page (e.g. the trapezoid rule's error, Gaussian elimination's steps, the CLT statement). |
| **F** | One plain-words explanation per unit, spoken: "what a derivative is," "what an eigenvector is," "what a confidence interval does and doesn't say." |
| **W** | Every definition and formula: why this and not something else ("why divide by n − 1?", "why does RK4 beat Euler?"). |
| **S** | Worked examples labelled by purpose; numerical algorithms as subgoal comments. |
| **I** | Problem sets mix calculus, linear algebra, and probability once all three have started. |
| **D** | Proofs and derivations benefit from the walk-and-return habit. |
| **T** | Each project is a lab report with plots; one recorded explainer per area. |

## Connections

- **Back:** M09 (linear models), M10 (rotations), M11 (exponentials, logs, sums); Fare Detective (least squares at last), Study Deck (your forgetting curve), Tone Loom (signals), Pico Thermostat (RC-like heating, noise), Courier (loss models), Vault Search (cosine similarity, PageRank stretch), Scheduler Arena (random arrivals).
- **Forward:** the advanced tracks in the [archived v1 plan](<../99 - Archive/v1 - Course-Based Curriculum/>) (machine learning, signals and communications, robotics) all start here.

## Module close

1. **Cumulative retrieval [R]:** one page each for calculus, linear algebra, probability, and signals: definitions, key theorems, the numerical methods, and one worked example.
2. **Timed problem set:** unseen problems from OCW 18.01 / 18.06 / 6.041 past exams or OpenStax review sections — mixed [I]. Grade honestly.
3. **Showcase [T]:** a short recording: your phone-motion path, your vault's PageRank top 10, and your forgetting curve with confidence bands.
4. Tick the module in [Start Here](<../00 - Start Here.md>).

**Resources:** books, docs, and tools for this module are in [resources.md](resources.md) (pointers only — the projects are the course).
