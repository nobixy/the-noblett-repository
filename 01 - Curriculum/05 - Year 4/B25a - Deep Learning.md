---
block_id: "Block 25a"
title: "Deep Learning (Karpathy Zero to Hero + Stanford CS231n)"
category: "core"
subject: "Computer Science"
term: "Year 4 Fall"
status: not-started
prerequisites:
  - "B22a - Machine Learning"
  - "B25 - Convex Optimization"
  - "B23a - Parallel Computing"
hours_estimate: 160
hours_actual: 0
primary_resource: "Karpathy, Neural Networks: Zero to Hero & Stanford CS231n assignments & Prince, Understanding Deep Learning (free)"
milestone: "Autograd engine and a GPT trained from scratch; CS231n assignments 1–3 pass their bundled checks"
date_started: ""
date_completed: ""
tier: "Tier 1 - Core"
---

# Block 25a — Deep Learning (Karpathy Zero to Hero + Stanford CS231n)

[[00 - Start Here|Start Here]] / [[00 - Start Here#The Path|The Path]] / [[Math Index|Math Index]]

> [!INFO] Block Overview
> - **Term / Position:** Year 4 Fall
> - **Estimated Hours:** ~160 hrs
> - **Status:** `not-started`
> - **Primary Resource:** Karpathy, Neural Networks: Zero to Hero & Stanford CS231n assignments & Prince, Understanding Deep Learning (free)
> - **Key Milestone:** Autograd engine and a GPT trained from scratch; CS231n assignments 1–3 pass their bundled checks
> - **Added by:** [[DR-004 - Content Overhaul|DR-004]] (2026-10-09)

---

## 📚 Curriculum Tier: Tier 1 - Core

## 🎯 Why This Block Matters
Modern EECS runs on deep learning: vision, speech, language models, recommendation, and the hardware and systems built to serve them. A 2026 EECS engineer who cannot build and train a transformer from scratch has a hole in the middle of the field. This block makes it core, after the math (linear algebra, probability, optimization) and the systems (parallel computing) it depends on.

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[B22a - Machine Learning|Machine Learning]]
- [[B25 - Convex Optimization|Convex Optimization]]
- [[B23a - Parallel Computing|Parallel Computing]]

---

## 📖 Primary Syllabus & Core Content
- [ ] Automatic differentiation and computational graphs
- [ ] MLPs, initialization, normalization, residual connections
- [ ] Optimizers (SGD, momentum, Adam), learning-rate schedules, regularization
- [ ] Convolutional networks for vision
- [ ] Sequence models, attention and the transformer
- [ ] Tokenization, language-model pretraining, sampling
- [ ] Training at scale on a GPU: mixed precision, batching, profiling
- [ ] Evaluation, ablations and reading papers critically

---

## 🛠️ Build Requirement
1. Follow *Neural Networks: Zero to Hero* end to end, typing every line yourself: micrograd (autograd engine), makemore, and a GPT trained on a text corpus. 2. Complete Stanford CS231n assignments 1–3 (kNN/SVM/softmax, fully-connected and conv nets, RNN/transformer captioning) in the provided notebooks. 3. Reproduce one result from a published paper at small scale and write it up in [[Paper Reading Hub|Paper Reading Hub]].

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> Your micrograd matches PyTorch gradients on random graphs; your GPT trains to a sensible loss and samples coherent text; CS231n assignments 1–3 pass their gradient checks and bundled tests; the paper reproduction is written up with what matched and what didn't.

---

## 🔎 Verified Resources (DR-004, checked 2026-10-09)
- **Karpathy, Neural Networks: Zero to Hero** (free videos + code): karpathy.ai/zero-to-hero.html; nanoGPT reference: github.com/karpathy/nanoGPT.
- **Stanford CS231n** (free notes and assignments): cs231n.github.io; current course page cs231n.stanford.edu.
- **Prince, *Understanding Deep Learning*** (free PDF + notebooks): udlbook.github.io/udlbook/ — the textbook for this block.
- **MIT 6.7960 Deep Learning** (OCW, Fall 2024) for lecture-style coverage: ocw.mit.edu/courses/6-7960-deep-learning-fall-2024/.
- 💲 A local NVIDIA GPU helps but is not required. Free alternative: the free GPU tier of a hosted notebook service (e.g. Google Colab); all of the above runs there.

---

## 📝 Study Notes, Psets & Proofs

*Your atomic notes, problem-set proofs, and build notes go here — written by you, from a blank page.*

> [!TIP]- Check your work (only after your own blank-sheet attempt)
> PyTorch as the reference for every gradient; CS231n's bundled gradient checks and tests.

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- UMich EECS 498-007 Deep Learning for Computer Vision (Justin Johnson, Winter 2022: public assignments with autograded-style checks); fast.ai Practical Deep Learning (course.fast.ai, free, top-down).

---

## ➡️ Next Steps
- **Topic Hub:** [[Math Index|Math Index]] | [[00 - Start Here#The Path|The Path]]
- **Sequential Flow:** [[B25 - Convex Optimization|← Convex Optimization]] | [[00 - Start Here|Start Here]] | [[Specialization Branches|Specialization A, Course 1 →]]
