---
block_id: "Block 22"
title: "Statistical Inference & Modeling"
term: "Year 3 Spring"
status: not-started
hours_estimate: 150
hours_actual: 0
primary_resource: "Larry Wasserman, All of Statistics & McElreath, Statistical Rethinking"
milestone: "Derive MLE, CI, hypothesis tests, and Bayesian MCMC models on real data"
date_started: ""
date_completed: ""
---

# Block 22 — Statistical Inference & Modeling

[[00 - Dashboard|Dashboard]] / [[Checklist|Checklist]] / [[02 - Notes/Math/Math Index|Math Index]]

> [!INFO] Block Overview
> - **Term / Position:** Year 3 Spring
> - **Estimated Hours:** ~150 hrs
> - **Status:** `not-started`
> - **Primary Resource:** Larry Wasserman, All of Statistics & McElreath, Statistical Rethinking
> - **Key Milestone:** Derive MLE, CI, hypothesis tests, and Bayesian MCMC models on real data

---

## 🎯 Why This Block Matters
Provides the rigorous theoretical grounding for modern data analysis, machine learning loss functions, uncertainty quantification, and experimental evaluation.

---

## 📖 Primary Syllabus & Core Content
- [ ] Wasserman Chapters 1–13: Probability foundations, convergence of random variables, CDFs
- [ ] Point Estimation: Maximum Likelihood Estimation (MLE), properties, Fisher information
- [ ] Hypothesis Testing & p-values, Neyman-Pearson lemma, likelihood ratio tests
- [ ] Confidence Intervals and bootstrapping
- [ ] Bayesian Inference: Priors, posteriors, conjugate models
- [ ] Richard McElreath, Statistical Rethinking video lectures: Generative models, MCMC sampling, regression, causal DAGs

---

## 🛠️ Build Requirement
Implement a complete statistical inference and modeling testbench in `python` using `numpy`, `scipy`, `pytest`, and `latex`.
1. **MLE & Fisher Information**: Program numerical optimization routines for high-dimensional MLE; compute empirical and expected Fisher Information matrices, validating asymptotic normality $\sqrt{n}(\hat{\theta}_{MLE} - \theta_0) \xrightarrow{d} \mathcal{N}(0, I(\theta_0)^{-1})$.
2. **Hypothesis Testing**: Implement Likelihood Ratio Tests, Wald tests, and score (Rao) tests; simulate empirical power curves to verify the Neyman-Pearson optimality bound.
3. **MCMC & Causal DAGs**: Build a Hamiltonian Monte Carlo (HMC) or Metropolis-Hastings sampler from scratch; evaluate Gelman-Rubin convergence diagnostic $\hat{R} < 1.01$ and effective sample size (ESS) on Bayesian hierarchical regression models.
4. **Toolchain & Verification**: Automated regression tests executed via `pytest`, reproducible shell workflows orchestrated in `bash`, version-controlled with `git`, and formal derivation writeups generated in `latex`.

---

## 🏁 Done When
> [!IMPORTANT]
> On a real dataset, you can execute MLE, confidence intervals, hypothesis tests, and Bayesian inference with MCMC, and explain when each is the wrong tool. All proofs below are independently derived and coded in `python`.

---

## 📝 Study Notes, Psets & Proofs

*Your atomic notes, problem-set proofs, and build notes go here — written by you, from a blank page.*

> [!TIP]- Check your work (only after your own blank-sheet attempt)
> McElreath posts weekly homework solutions in each *Statistical Rethinking* course repo (e.g. [rmcelreath/stat_rethinking_2024](https://github.com/rmcelreath/stat_rethinking_2024)). Wasserman has no official solutions.

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- MIT 6.3800 Introduction to Inference; Gelman et al., Regression and Other Stories.

---

## 🧭 Navigation
- **Topic Hub:** [[02 - Notes/Math/Math Index|Math Index]] | [[Checklist|Master Checklist]]
- **Sequential Flow:** [[01 - Curriculum/Year 3 - Depth/21 - Databases|← 21 - Databases]] | [[00 - Dashboard|Dashboard]] | [[01 - Curriculum/Year 4 - Specialization/23 - Distributed Systems|23 - Distributed Systems →]]
