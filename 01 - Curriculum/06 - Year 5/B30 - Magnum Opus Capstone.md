---
block_id: "Block 30"
title: "Capstone Project & Thesis (MEng Year)"
category: "core"
subject: "Capstone"
term: "Year 5 (Two Semesters)"
status: not-started
prerequisites:
  - "B23 - Distributed Systems"
  - "B24 - Theory of Computation"
  - "B25 - Convex Optimization"
  - "B27 - Intensive Cryptopals"
hours_estimate: 400
hours_actual: 0
primary_resource: "Primary Engineering / Research project"
milestone: "Public Artifact + 15k-25k word Thesis + 30-min Talk + Outside Review"
date_started: ""
date_completed: ""
tier: "Tier 3 - Depth"
aliases: ["Magnum Opus Capstone"]
---

# Block 30 — Capstone Project & Thesis (MEng Year)

[[00 - Start Here|Start Here]] / [[00 - Start Here#The Path|The Path]] / [[Projects Hub|Projects Hub]]

> [!INFO] Block Overview
> - **Term / Position:** Year 5 (Two Semesters)
> - **Estimated Hours:** ~400 hrs
> - **Status:** `not-started`
> - **Primary Resource:** Primary Engineering / Research project
> - **Key Milestone:** Public Artifact + 15k-25k word Thesis + 30-min Talk + Outside Review

---

## 🎯 Why This Block Matters
What makes the program MEng-equivalent rather than SB-equivalent: producing novel, production-grade engineering or research.

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[B23 - Distributed Systems|Distributed Systems]]
- [[B24 - Theory of Computation|Theory of Computation]]
- [[B25 - Convex Optimization|Convex Optimization]]
- [[B27 - Intensive Cryptopals|Intensive Cryptopals]]
*In practice: all Year 4 blocks, Specialization A, and the Year 4 capstone proposal (3,000 words).*


## 📖 Primary Syllabus & Core Content
- [ ] Select one of the 4 paths:
- [ ]   A. Build a serious system: A database, a language with optimizing compiler, a kernel, a distributed store, a renderer, or an ML framework (10,000+ lines, real tests, benchmarks).
- [ ]   B. Replicate and extend research: One paper from last 3 years of OSDI, SOSP, SIGCOMM, PLDI, ISCA, NeurIPS, or SIGMOD.
- [ ]   C. Substantial open-source contribution: Ship a major feature in Linux, LLVM, PostgreSQL, Rust, CPython, SQLite, or Kubernetes.
- [ ]   D. Tape out a chip: Via Tiny Tapeout or Efabless with SkyWater open-source PDK.
- [ ] Mandatory Human-Computer Interaction (HCI) & Usability Engineering Verification:
  - Formative and summative empirical usability testing: Structured testing protocol with representative users or domain developers measuring task completion rates ($\ge 85\%$), time-on-task, and error recovery.
  - Formal Cognitive Walkthrough: Action-by-action cognitive walkthrough across core user journeys against the 4 canonical walkthrough questions (Goal alignment, action visibility, semantic mapping, progress feedback).
  - W3C WCAG 2.1 AA Accessibility Compliance: Automated test suite integration (axe-core/pa11y) plus manual keyboard-only navigation verification and screen-reader audit for all user-facing interfaces (CLI, TUI, GUI, web dashboard, or developer telemetry tool).
- [ ] Professional ethics, safety, and societal impact assessment (ACM/IEEE Code of Ethics compliance, algorithmic fairness, security risk analysis, and accessibility guarantees).

---

## 🛠️ Build Requirement
Deliver a complete, production-grade engineering artifact developed in `c`, `c++`, `rust`, or `python` on `linux` using `cargo`, `cmake`, `make`, `valgrind`, `pytest`, `qemu`, `tiny tapeout`, or `verilog`:
1. **Public Codebase Artifact**: Monolithic systems codebase ($> 10,000$ SLOC) with continuous integration, automated unit and integration tests run via `pytest` or `cargo test`, and zero memory leaks under AddressSanitizer / `valgrind`.
2. **Reproducible Benchmarks**: Standardized performance telemetry harness orchestrated via `bash` measuring throughput, latency distributions, and hardware resource scaling.
3. **Academic Monograph**: 15,000–25,000-word written thesis compiled in `latex`, accompanied by complete replication scripts in `git`.
4. **HCI Usability & Accessibility Deliverable**: For any interactive system, developer interface, CLI, GUI, or web dashboard:
  - *Empirical Usability Testing Report:* Documented user testing sessions with task success metrics, error frequency analysis, and System Usability Scale (SUS) evaluation (target score $\ge 75$).
  - *Cognitive Walkthrough Documentation:* Complete action-by-action walkthrough covering primary user journeys, validating user mental model alignment against system image.
  - *WCAG 2.1 AA Accessibility Audit:* Automated verification showing zero critical/serious accessibility violations, verified non-mouse full keyboard traversal (no focus traps, visible focus rings), and contrast ratios satisfying $\ge 4.5:1$.

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> Deliverables completed: (1) Public artifact with documentation; (2) 15,000–25,000-word written thesis; (3) 30-minute recorded technical presentation; (4) Written feedback from at least one external expert reviewer; (5) Mandatory HCI usability testing, cognitive walkthrough, and WCAG accessibility compliance verification completed and documented.

---

## 🔎 Verified Resources (DR-004, checked 2026-10-09)
**Verdict:** KEEP. The HCI deliverable applies only to interactive systems, as written.

---

## 📝 Study Notes, Psets & Proofs

*Your atomic notes, problem-set proofs, and build notes go here — written by you, from a blank page.*

> [!TIP]- Check your work (only after your own blank-sheet attempt)
> Your outside reviewer's written critique (part of *Done when*).

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- None. This is the synthesis of the entire degree.

---

## ➡️ Next Steps
- **Topic Hub:** [[Projects Hub|Projects Hub]] | [[00 - Start Here#The Path|The Path]]
- **Sequential Flow:** [[Specialization Branches|← Specialization B, Course 1]] | [[00 - Start Here|Start Here]] | [[B32 - Information Theory|Information Theory →]]
