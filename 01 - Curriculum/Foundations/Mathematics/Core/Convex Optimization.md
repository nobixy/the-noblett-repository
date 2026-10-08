---
block_id: "Block 21"
title: "Convex Optimization (Stanford EE364A & Boyd)"
category: "core"
term: "Year 4 Fall"
status: not-started
prerequisites:
  - "Linear Algebra"
  - "Multivariable Calculus"
hours_estimate: 150
hours_actual: 0
primary_resource: "Stephen Boyd & Lieven Vandenberghe & Stanford EE364A"
milestone: "EE364A homework sets 1–8 completed; CVXPY project + manual KKT derivation"
date_started: ""
date_completed: ""
tier: "Tier 3 - Depth"
---

# Block 21 — Convex Optimization (Stanford EE364A & Boyd)

[[00 - Dashboard|Dashboard]] / [[Checklist|Checklist]] / [[Math Index|Math Index]]

> [!INFO] Block Overview
> - **Term / Position:** Year 4 Fall
> - **Estimated Hours:** ~150 hrs
> - **Status:** `not-started`
> - **Primary Resource:** Stephen Boyd & Lieven Vandenberghe & Stanford EE364A
> - **Key Milestone:** EE364A homework sets 1–8 completed; CVXPY project + manual KKT derivation

---

## 📚 Curriculum Tier: Tier 3 - Depth
> **Tier 3 - Depth**: Optional deep dive for specialized mastery.

## 🎯 Why This Block Matters
Optimization is the unified mathematical engine underlying machine learning, control systems, signal processing, and quantitative engineering.

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[Linear Algebra]]
- [[Multivariable Calculus]]


## 📖 Primary Syllabus & Core Content
- [ ] Convex sets: Affine sets, cones, hyperplanes, dual cones
- [ ] Convex functions: Epigraphs, Jensen's inequality, quasiconvexity
- [ ] Convex optimization problems: LP, QP, QCQP, SOCP, SDP
- [ ] Duality: Lagrange dual function, weak and strong duality, Slater's conditions
- [ ] KKT optimality conditions: Complementary slackness, sensitivity analysis
- [ ] Unconstrained and equality constrained optimization: Gradient descent, Newton's method
- [ ] Interior-point methods: Barrier method, primal-dual interior-point

---

## 🛠️ Build Requirement
Formulate and solve large-scale convex optimization problems in `python` using `numpy`, `scipy`, `cvxpy`, and `pytest`, verified against formal derivations written in `latex`:
1. **Primal-Dual Interior-Point Solver**: Implement a custom barrier method and infeasible primal-dual interior-point algorithm from scratch in Python/NumPy for Quadratic Programs (QP) and Second-Order Cone Programs (SOCP).
2. **First-Order Accelerated Methods**: Code Nesterov's accelerated gradient descent and FISTA (Fast Iterative Shrinkage-Thresholding Algorithm) for $\ell_1$-regularized Lasso; empirically confirm the $\mathcal{O}(1/k^2)$ convergence rate versus standard gradient descent $\mathcal{O}(1/k)$.
3. **KKT Sensitivity & Duality**: Solve a high-dimensional portfolio allocation or Model Predictive Control (MPC) problem using `cvxpy`; analytically derive the Karush-Kuhn-Tucker (KKT) conditions and verify Lagrange multiplier shadow prices against CVXPY dual variables.
4. **Toolchain & Verification**: Automated regression unit tests orchestrated with `pytest`, build pipelines configured in `bash`, and version-controlled with `git`.

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> Stanford EE364A homework sets 1 through 8 completed. Custom interior-point solver matches CVXPY optimal objective value to within $10^{-7}$ relative tolerance. Proofs below are derived and verified.

---

## 📝 Study Notes, Psets & Proofs

*Your atomic notes, problem-set proofs, and build notes go here — written by you, from a blank page.*

> [!TIP]- Check your work (only after your own blank-sheet attempt)
> No public solution set. Check numerical answers by solving the same problem in CVXPY; derive the KKT conditions by hand and confirm they hold at the solver's optimum.

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- Stanford EE364B (sequel); Nocedal & Wright, Numerical Optimization.

---

## ➡️ Next Steps
- **Topic Hub:** [[Math Index|Math Index]] | [[Checklist|Master Checklist]]
- **Sequential Flow:** [[Real Analysis|← Real Analysis]] | [[00 - Dashboard|Dashboard]] | [[Algorithms I|Algorithms I →]]
