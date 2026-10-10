---
block_id: "P3"
title: "Math Prerequisites"
category: "core"
subject: "Mathematics"
term: "Phase 0 (0–5 mo)"
status: not-started
prerequisites:
  - "BM - Bedrock Mathematics"
hours_estimate: 90
hours_actual: 0
primary_resource: "Khan Academy -> Velleman, How to Prove It (ch 1-3)"
milestone: "Cold exit test passed; induction & contradiction proofs written"
date_started: ""
date_completed: ""
tier: "Tier 1 - Core"
job_ready: 1 # job-ready path, phase 1 (DR-003)
aliases: ["Math Prerequisites"]
---

# P3 — Math Prerequisites

> [!INFO] Block Overview
> - **Term / Position:** Phase 0
> - **Estimated Hours:** 60–120 hrs
> - **Status:** `not-started`
> - **Primary Practice:** Khan Academy (Algebra II → Precalculus → Trigonometry) as needed
> - **Primary Proofs:** Velleman, *How to Prove It* (Chapters 1–3, every exercise)
> - **Companion Reading:** Lockhart, *Arithmetic*, is read in [[BM - Bedrock Mathematics|BM]]. Revisit it before Nand2Tetris as a warm-up for binary.
> - **Transition Guide:** Lara Alcock, *How to Study as a Mathematics Major* (Ch 1–4)

---

## 📚 Curriculum Tier: Tier 1 - Core
> **Tier 1 - Core**: Must complete before advancing.

## 🎯 Why This Block Matters
Mathematics in EECS is not calculation; it is proof and structure. Before starting calculus and discrete math, you must transition from manipulative algebra to formal reasoning.

---

## 🧪 Cold Exit Test (Can Skip Khan Academy if Passed)
*Cold, on paper, unaided:*
- [ ] Simplify a nested log/exponent expression
- [ ] Solve a $3 \times 3$ linear system
- [ ] Expand $(a+b)^5$ via binomial theorem
- [ ] Prove $\sqrt{2}$ is irrational
*(Pass all four → skip Khan Academy, but still do Velleman chapters 1–3!)*

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[BM - Bedrock Mathematics|Bedrock Mathematics]]


## 📖 Primary Syllabus
- [ ] Khan Academy Algebra II, Precalculus, Trigonometry (refresh weak spots).
- [ ] **Velleman, *How to Prove It***:
  - [ ] Chapter 1: Sentential Logic
  - [ ] Chapter 2: Set Theory
  - [ ] Chapter 3: Proofs (Direct, Contrapositive, Contradiction)
  - [ ] Complete *every single exercise*.

---

## 🛠️ Build Requirement
Write rigorous, complete formal solutions to all Velleman Chapters 1–3 exercises and the Cold Exit Test in `latex`, verifying analytical expressions and combinatorial identities using `python` and SymPy.

**Project build (DR-008):** a Python **truth-table and set toolkit**: prints the truth table of any formula, decides whether it is a tautology, and draws Venn diagrams for set expressions. Use it to check your Velleman ch. 1–2 answers *after* you write them by hand. **Done when** it agrees with your hand answers on every ch. 1 truth-table exercise and 5 ch. 2 set exercises. Replaces the SymPy checks for ch. 1–2.

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> The cold exit test passes and you can write a clean induction proof and a clean contradiction proof from scratch on paper without notes.

---

## 🎮 Fun Build & Extras (DR-006, 2026-10-09)
- **Fun build:** **Desmos art** (desmos.com/calculator, free): draw a picture using only the functions you are refreshing (lines, parabolas, trig, restricted domains); it replaces one Khan precalculus practice set. Optional preview: 3Blue1Brown *Essence of Linear Algebra*.

---

## 🔎 Verified Resources (DR-004, checked 2026-10-09)
**Verdict:** KEEP. Proof fluency before CS61A and 6.1200.
- 💲 Velleman *How to Prove It*; free alternatives: *Infinite Descent* (infinitedescent.xyz) or Hammack *Book of Proof* (free PDF).

---

## 📝 Study Notes, Psets & Proofs

*Your atomic notes, problem-set proofs, and build notes go here — written by you, from a blank page.*

> [!TIP]- Check your work (only after your own blank-sheet attempt)
> Velleman's starred exercises have solutions or hints in the back of the book (*Solutions to Selected Exercises*). For the rest, check each line against the definitions, or ask for a Socratic proof check.

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- Richard Hammack, *Book of Proof* (free PDF)
- Paul Lockhart, *A Mathematician's Lament* (free essay)

---

## ➡️ Next Steps
*Why does the next subject come next?*
- Next Block

- **Sequential Flow:** [[P2 - Reading, Thinking, and Writing|← Reading, Thinking, and Writing]] | [[00 - Start Here|Start Here]] | [[P4 - Programming On-Ramp|Programming On-Ramp →]]
