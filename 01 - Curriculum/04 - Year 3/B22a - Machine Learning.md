---
block_id: "Block 22a"
title: "Machine Learning (MIT 6.390 + Stanford CS229)"
category: "core"
subject: "Computer Science"
term: "Year 3 Spring"
status: not-started
prerequisites:
  - "B11 - Linear Algebra"
  - "B13 - Algorithms I"
  - "B15 - Probability"
  - "B07 - Multivariable Calculus"
hours_estimate: 150
hours_actual: 0
primary_resource: "MIT 6.390 Intro to Machine Learning (notes + MITx 6.036 Open Learning Library, autograded) & Stanford CS229 notes"
milestone: "All 6.036 OLL exercises/labs pass the autograder; regression, classifiers, a neural net and k-means built from scratch in NumPy"
date_started: ""
date_completed: ""
tier: "Tier 1 - Core"
---

# Block 22a — Machine Learning (MIT 6.390 + Stanford CS229)

[[00 - Start Here|Start Here]] / [[00 - Start Here#The Path|The Path]] / [[Math Index|Math Index]]

> [!INFO] Block Overview
> - **Term / Position:** Year 3 Spring
> - **Estimated Hours:** ~150 hrs
> - **Status:** `not-started`
> - **Primary Resource:** MIT 6.390 Intro to Machine Learning (notes + MITx 6.036 Open Learning Library, autograded) & Stanford CS229 notes
> - **Key Milestone:** All 6.036 OLL exercises/labs pass the autograder; regression, classifiers, a neural net and k-means built from scratch in NumPy
> - **Added by:** [[DR-004 - Content Overhaul|DR-004]] (2026-10-09)

---

## 📚 Curriculum Tier: Tier 1 - Core

## 🎯 Why This Block Matters
Machine learning is now a core EECS subject, not an elective: MIT runs 6.390 every semester as its department-wide intro ML subject (Spring and Fall 2026 offerings), and every later block here (deep learning, optimization, information theory, most tracks) leans on it. This replaces the old optional E2 elective and makes it required.

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[B11 - Linear Algebra|Linear Algebra]]
- [[B13 - Algorithms I|Algorithms I]]
- [[B15 - Probability|Probability]]
- [[B07 - Multivariable Calculus|Multivariable Calculus]]

---

## 📖 Primary Syllabus & Core Content
- [ ] Problem formulation, loss functions, empirical risk, generalization, train/validation/test
- [ ] Linear regression, ridge, gradient descent and SGD
- [ ] Linear classifiers, logistic regression, margins
- [ ] Feature engineering, regularization, cross-validation, bias–variance
- [ ] Neural networks and backpropagation by hand
- [ ] Convolutional and sequence models (overview; depth comes in Block 25a)
- [ ] Unsupervised learning: clustering, PCA
- [ ] Markov decision processes and reinforcement learning basics

---

## 🛠️ Build Requirement
Implement from scratch in `python` + `numpy` (no frameworks): linear and ridge regression with closed form and SGD, logistic regression, a 2-layer neural net with hand-written backprop (gradient-checked), k-means and PCA. Then one end-to-end project on a real public dataset with a written evaluation (baselines, error analysis, what failed).

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> Every exercise and lab in the MITx 6.036 Open Learning Library course passes its autograder; your from-scratch implementations match scikit-learn on the same data to within numerical tolerance; you can derive the gradient of logistic loss and backprop for a 2-layer net on paper.

---

## 🔎 Verified Resources (DR-004, checked 2026-10-09)
- **MIT 6.390 lecture notes** (free, current): introml.mit.edu/notes — the course runs Fall 2026 at introml.mit.edu/fall26 (MIT-only submission).
- **MITx 6.036 on the Open Learning Library** (free, autograded exercises and labs, no enrollment needed): openlearninglibrary.mit.edu/courses/course-v1:MITx+6.036+1T2019/about. OCW mirror with lecture videos: ocw.mit.edu/courses/6-036-introduction-to-machine-learning-fall-2020/.
- **Stanford CS229** (free notes and problem sets): cs229.stanford.edu; lecture videos via Stanford Engineering Everywhere: see.stanford.edu/Course/CS229. Use for the math-heavier derivations.
- **ISLP / ISLR** (free book + labs): statlearning.com — for the statistical view, pairs with Block 22.

---

## 📝 Study Notes, Psets & Proofs

*Your atomic notes, problem-set proofs, and build notes go here — written by you, from a blank page.*

> [!TIP]- Check your work (only after your own blank-sheet attempt)
> The OLL autograder, then `sklearn` on the same data as a reference implementation; `numpy` finite-difference gradient checks.

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- Stanford CS229 as the primary instead of 6.390 (more math, no autograder); *Dive into Deep Learning* (d2l.ai, free) for code-first practice.

---

## ➡️ Next Steps
- **Topic Hub:** [[Math Index|Math Index]] | [[00 - Start Here#The Path|The Path]]
- **Sequential Flow:** [[B22 - Statistics|← Statistics]] | [[00 - Start Here|Start Here]] | [[B23 - Distributed Systems|Distributed Systems →]]
