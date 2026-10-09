---
block_id: "Block 11"
title: "Structure and Interpretation of Computer Programs (SICP)"
category: "core"
term: "Year 1 Spring"
status: not-started
prerequisites:
  - "CS61A"
hours_estimate: 120
hours_actual: 0
primary_resource: "Abelson & Sussman, SICP (Ch 1-4) & 1986 MIT Lectures"
milestone: "Write the metacircular evaluator from memory in under 1 hour"
date_started: ""
date_completed: ""
tier: "Tier 3 - Depth"
---

# Block 11 — Structure and Interpretation of Computer Programs (SICP)

[[00 - Dashboard|Dashboard]] / [[Checklist|Checklist]] / [[Languages Index|Languages Index]]

> [!INFO] Block Overview
> - **Term / Position:** Year 1 Spring
> - **Estimated Hours:** ~120 hrs
> - **Status:** `not-started`
> - **Primary Resource:** Abelson & Sussman, SICP (Ch 1-4) & 1986 MIT Lectures
> - **Key Milestone:** Write the metacircular evaluator from memory in under 1 hour

---

## 📚 Curriculum Tier: Tier 3 - Depth
> **Tier 3 - Depth**: Optional deep dive for specialized mastery.

## 🎯 Why This Block Matters
MIT's legendary 6.001 for thirty years. Explores CS61A's deepest ideas at full depth, in Scheme.

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[CS61A]]


## 📖 Primary Syllabus & Core Content
- [ ] Chapter 1: Building Abstractions with Procedures (higher-order procedures, recursion vs iteration)
- [ ] Chapter 2: Building Abstractions with Data (closure, data-directed programming, message passing)
- [ ] Chapter 3: Modularity, Objects, and State (mutable state, streams, delayed evaluation)
- [ ] Chapter 4: Metalinguistic Abstraction (§4.1 Metacircular Evaluator, §4.2 Lazy Evaluator)
- [ ] Companion: Watch Hal Abelson & Gerald Jay Sussman's 1986 MIT lectures on YouTube

---

## 🛠️ Build Requirement
Implement the Metacircular Evaluator (§4.1) and the Lazy Evaluator (§4.2) from scratch in `scheme` (MIT/GNU Scheme or Racket) or `python`:
1. **Core Evaluator**: Parse and evaluate environments, procedures, closures, dynamic scoping, and macro expansions in `scheme`.
2. **Lazy Evaluator & Streams**: Construct delayed thunks with memoization, infinite stream pipelines, and non-deterministic amb-evaluator.
3. **Toolchain & Verification**: Automated evaluation test suite orchestrated with `bash` and version-controlled with `git`.

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> You can write the complete Scheme metacircular evaluator from memory, correctly, in under an hour.

---

## 📝 Study Notes, Psets & Proofs

*Your atomic notes, problem-set proofs, and build notes go here — written by you, from a blank page.*

> [!TIP]- Check your work (only after your own blank-sheet attempt)
> SICP has no official solutions. Run every exercise in a Scheme REPL and test the edge cases; compare with community solutions only after your own attempt.

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- SICP: JavaScript Edition; Brian Harvey's CS61A Scheme lectures (YouTube).

---

## ➡️ Next Steps
- **Topic Hub:** [[Languages Index|Languages Index]] | [[Checklist|Master Checklist]]
- **Sequential Flow:** [[Differential Equations Bridge|← Differential Equations Bridge]] | [[00 - Dashboard|Dashboard]] | [[C Fluency|C Fluency →]]
