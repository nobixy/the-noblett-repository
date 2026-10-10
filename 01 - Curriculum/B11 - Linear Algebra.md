---
block_id: "Block 11"
stage: "03 - Year 2"
title: "Linear Algebra (MIT 18.06 & Axler LADR)"
category: "core"
subject: "Mathematics"
term: "Year 2 Fall"
status: not-started
prerequisites:
  - "B07 - Multivariable Calculus"
hours_estimate: 200
hours_actual: 0
primary_resource: "MIT 18.06 (Gilbert Strang) + Axler, Linear Algebra Done Right, 4e"
milestone: "18.06 final passed, Axler ch 1–5 exercises done, NumPy matrix algorithms built"
date_started: ""
date_completed: ""
tier: "Tier 1 - Core"
aliases: ["Linear Algebra"]
---

# Block 11 — Linear Algebra (MIT 18.06 & Axler LADR)

[[00 - Start Here|Start Here]] / [[00 - Start Here#The Path|The Path]] / [[Math Index|Math Index]]

> [!INFO] Block Overview
> - **Term / Position:** Year 2 Fall
> - **Estimated Hours:** ~200 hrs
> - **Status:** `not-started`
> - **Primary Resource:** MIT 18.06 (Gilbert Strang) + Axler, Linear Algebra Done Right, 4e
> - **Key Milestone:** 18.06 final passed, Axler ch 1–5 exercises done, NumPy matrix algorithms built

---

## 📚 Curriculum Tier: Tier 1 - Core
> **Tier 1 - Core**: Must complete before advancing.

## 🎯 Why This Block Matters
The most important mathematics for CS, taken twice on purpose: once computationally with Strang, once abstractly with Axler.


## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[B07 - Multivariable Calculus|Multivariable Calculus]]

---

## 📖 Primary Syllabus & Core Content
- [ ] Part 1 (Computational): MIT 18.06 with Strang (elimination, subspaces, orthogonality, determinants, eigenvalues/eigenvectors, SVD)
- [ ] Part 2 (Abstract): Axler LADR 4e Ch 1–7 (vector spaces, finite-dimensional spaces, linear maps, polynomials, eigenvalues, inner product spaces, operators on inner product spaces)

---

## 🛠️ Build Requirement
Build from scratch in `python` using `numpy`: LU factorization with partial pivoting, Modified Gram-Schmidt, QR decomposition via Householder reflections, and the Power Method / Lanczos iteration for eigenvalues. Benchmark against LAPACK/`scipy.linalg` and write a formal analysis of conditioning, backward stability, and floating-point errors in `latex`.

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> 18.06 final passed and Axler chapters 1–5 exercises completed.

---

## 🎓 Companion Courses (DR-006, 2026-10-09)
- **Coursera Plus:** *Mathematics for Machine Learning: Linear Algebra* (Imperial) as a companion to 18.06; it replaces some drill, so no extra hours.

---

## 🔎 Verified Resources (DR-004, checked 2026-10-09)
**Verdict:** KEEP.
- **MIT 18.06SC** (OCW Scholar, exams with solutions): ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/; Axler *LADR* 4e is free: linear.axler.net; 3Blue1Brown *Essence of Linear Algebra*: 3blue1brown.com/topics/linear-algebra.

---

## 📝 Study Notes, Psets & Proofs

*Your atomic notes, problem-set proofs, and build notes go here — written by you, from a blank page.*

> [!TIP]- Check your work (only after your own blank-sheet attempt)
> OCW [18.06SC](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/) posts problem-set and exam solutions. Axler has no official solutions, so check each proof line by line against the definitions.

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- 3Blue1Brown Essence of Linear Algebra (intuition); Trefethen & Bau, Numerical Linear Algebra.

---

## ➡️ Next Steps
- **Topic Hub:** [[Math Index|Math Index]] | [[00 - Start Here#The Path|The Path]]
- **Sequential Flow:** [[B10 - Math for CS|← Math for CS]] | [[00 - Start Here|Start Here]] | [[B12 - Interpreters|Interpreters →]]
