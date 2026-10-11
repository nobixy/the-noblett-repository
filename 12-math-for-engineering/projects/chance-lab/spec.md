---
title: "Project: Chance Lab"
id: "MOD12-PRJ-chance-lab"
type: "project"
module: "12-math-for-engineering"
phase: "D"
order: 1240
prerequisites: [MOD12-P1, MOD12-P2, MOD12-P3, MOD12-L4, MOD09-PRJ-courier]
units: "P1, P2, P3, L4"
artifact: "A simulation toolkit for distributions, the law of large numbers, and the central limit theorem; a Markov-chain model of your Leitner boxes; a fitted packet-loss model; and an honest, pre-registered self-experiment comparing two study methods"
deliverable: "Lab report + a pre-registration document + a short explainer on confidence intervals"
---

# Project: Chance Lab

| | |
| :-- | :-- |
| **Module** | 12 Math for Engineering (Units P1–P3, with L4) |
| **Prerequisites** | Units P1–P3 and L4; [Courier](../../../09-networking/projects/courier/spec.md) (Module 09) done — this project models Courier's packet loss and reuses its throughput measurements |
| **You build** | Simulations that make probability's big theorems visible; models of two systems you built (your Leitner boxes as a Markov chain, Courier's packet loss as a two-state model); and a small, honest experiment on yourself: does one study method beat another *for you*? |
| **Deliverable** | A lab report, a pre-registration, and a recorded explainer |

---

## Why this matters

Engineering is full of uncertainty: noisy sensors, random packet loss, variable request times, and measurements that differ every run. Probability tells you what to expect; statistics tells you what your data can and can't support. The most valuable skill here is honesty: knowing how sure you can be, and not fooling yourself. You'll practise it on the most personal data possible — your own learning.

---

## Milestones

### Milestone 1 — See the theorems (Units P1–P2)

1. **Sampling from distributions** using only `random.random()` (uniform on [0, 1)): Bernoulli, binomial, geometric, exponential (by the inverse-CDF method: −ln(U)/λ — derive why it works [W]), and normal (Box–Muller). Check each against its known mean and variance with 100,000 samples, and against `numpy.random` histograms.
2. **Law of large numbers:** plot the running average of die rolls over 10,000 rolls, for 20 independent runs on one chart. Watch them squeeze together.
3. **Central limit theorem:** take averages of n samples from a very non-normal distribution (exponential, or a lopsided die) for n = 1, 2, 5, 30; histogram 10,000 such averages each. Watch them become bell-shaped, with spread shrinking like 1/√n. (Your Pico Thermostat averaging result from Module 04 — now explained.)
4. **[F]** record a short explanation of why averages are more predictable than single measurements.

### Milestone 2 — Model your systems (Units P1, L4)

1. **Leitner boxes as a Markov chain:** a card is in box 1–5; with probability p (its recall probability for that box's interval) it moves up, otherwise back to box 1. Write the 5 × 5 transition matrix; find the **steady-state** distribution (the eigenvector for eigenvalue 1 — Matrix Studio's power iteration) for your real p values estimated from Study Deck's log. Compare with how your actual cards are spread across boxes.
2. **Packet loss in Courier:** from Gremlin 2 runs with burst loss, or from your real Wi-Fi (ping 10,000 times, record losses), fit the **Gilbert–Elliott** model (a two-state Markov chain: good/bad states with different loss rates). Estimate the transition probabilities from runs of losses. Does the model reproduce the observed distribution of burst lengths better than independent loss does?

### Milestone 3 — Estimates with honest uncertainty (Unit P3)

1. **Confidence intervals** for your Study Deck retention rate (a proportion) using the normal approximation and the **bootstrap** (resample your data with replacement many times — simple, general, powerful). Do they agree?
2. **Simulation check:** generate fake data with a *known* true value, build a 95% interval, repeat 1,000 times, and count how often the interval contains the truth. It should be about 950. [W] What exactly does "95% confidence" promise — and what doesn't it promise? (This is the most misunderstood idea in statistics.)
3. Your Courier throughput measurements from Module 09: intervals for the mean throughput at each loss rate. Were your report's comparisons with TCP meaningful given the uncertainty?

### Milestone 4 — A pre-registered self-experiment (Unit P3)

Does one study method work better for **you**? Example: learning 60 new technical terms with **retrieval practice** (flashcards, testing yourself) vs **rereading** (studying the list repeatedly), tested one week later.

1. **Pre-registration** (write it *before* collecting data — this is what makes the result trustworthy [W]): the question; the two conditions; the materials (two matched sets of 30 items, randomly assigned to conditions by a seeded shuffle); the schedule; the outcome measure (items recalled correctly at the one-week test); the analysis (difference in proportions, a **permutation test**, and a bootstrap confidence interval); what result would change your study habits. Commit it to git with a date.
2. Run it. Follow the plan exactly; note any deviation.
3. Analyse exactly as planned. Report the effect with its interval and p-value — and the limits: one person, one material type, possible order effects.

**Done when:** pre-registration committed before data collection, analysis done as planned, honest conclusion written.

---

## Communication deliverable

1. **Pre-registration document** (1 page), committed before the experiment.
2. **Lab report** (4 pages, E10): the theorem simulations, the two system models, the confidence-interval experiments, and the self-experiment with an honest discussion.
3. **Explainer (short, recorded):** "What a 95% confidence interval means," for a beginner, using your simulation.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Distribution formulas, LLN and CLT statements, interval recipes from memory |
| **F** | Averages; confidence intervals |
| **W** | Inverse-CDF sampling; what 95% means; why pre-register |
| **S** | Bootstrap and permutation-test procedures as labelled steps |
| **T** | Pre-registration, report, explainer |

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Simulations | All samplers checked; LLN and CLT shown clearly | Most | Few |
| System models | Leitner steady state vs real data; Gilbert–Elliott fit | One | None |
| Intervals | Normal and bootstrap; coverage simulation; Courier revisited | Partial | Missing |
| Self-experiment | Pre-registered, executed as planned, honest analysis | Done without pre-registration | Missing |
| Communication | Pre-registration, report, explainer | Two | One |

**Done when:** every area at least 2; Self-experiment at 3.

## Connections

- **Back:** Module 03 Unit 8, Counting Verifier, Study Deck (your data), Courier and Gremlin 2, Pico Thermostat (averaging), Matrix Studio (eigenvectors), [LM09](<../../../02 - Atlas/LM09 - Spacing and Spaced Repetition.md>) and [LM02](<../../../02 - Atlas/LM02 - Retrieval Practice.md>) (the research behind your experiment).
- **Forward:** machine learning and data tracks; every benchmark you report from now on (always with uncertainty).

> **Originality note:** these experiments, especially the self-experiment design, were written for this curriculum.
