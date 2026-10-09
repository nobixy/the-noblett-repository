---
title: "DR-001: Program Scope, Phases, and Timeline"
type: decision-record
status: accepted
date: 2026-10-09
accepted: 2026-10-09
tags:
  - adr
  - decision-record
---

# DR-001: Program Scope, Phases, and Timeline

*Uses the [[Decision Record]] template. Written under Operating Rule 10 in [[00 - Start Here]]. Accepted 2026-10-09; the edits listed under Consequences were applied the same day.*

## Context
Four statements in the vault disagree about how big the program is, how long it should take, how it is divided, and when the specializations open. Each piece is fine on its own, but together they don't give one clear rule to follow.

### C1. Lifelong, or about 8 years?
- [[00 - Dashboard]] (Budget line): *"This is a lifelong endeavor. There is no longer an 8-year completion constraint."*
- [[how-i-study]] §4: *"Below 15 hrs/wk, cut scope rather than extending the timeline beyond 8 years."*
- Source, [[The Independent EECS Program.pdf]] §5.2: *"Seven and a half years at 20 hrs/wk. If that's too long, cut scope (skip Physics, skip Block 22, do one specialization) — don't stretch the timeline further; past ~8 years the completion rate goes to zero."*

### C2. How many hours?
- [[how-i-study]] §4: *"The whole program is roughly 6,500–8,000 hours."*
- [[00 - Dashboard]] (Degree Progress table): adds up `hours_estimate` for every block that isn't `optional: true`. That comes to **≈11,285 planned hours**, because all 14 specialization tracks (400 h each, 5,600 h total) are counted.
- What the vault plans in course hours:

| Bucket | Hours |
|---|---|
| Phase −1 + Phase 0 + Years 1–5 core blocks (incl. Information Theory) | ≈4,595 |
| Four Tier 1 blocks with no Checklist slot (AI, Intro ML, Computer Security, Parallel Computing) | 560 |
| Intensive Cryptopals/TLA+ + Capstone | 530 |
| Two specialization tracks (the source program says "pick two") | 800 |
| **Program total in course hours** | **≈5,925–6,485** |
| Habits on top (500 words/day, Anki, 8 breadth subjects, language, talks) | ≈1,000–1,500 over the program |
| Remaining 12 tracks (counted on the Dashboard today) | 4,800 |

  Core + two tracks + capstone + habits lands inside 6,500–8,000. **The 11,285 figure only appears because every track is counted.**
- The time math: 20 h/wk × ~48 wk ≈ 960 h/yr, so 6,500–8,000 h ≈ 7–8.5 years. At 15 h/wk (≈720 h/yr) it's 9–11 years, which is why §4 says to cut scope below 15 h/wk. At 20 h/wk, 11,285 h is about 12 years.

### C3. "17 sequential phases" vs 5 phases
- [[00 - Dashboard]] (Budget line): *"The curriculum spans 17 sequential phases (from Arithmetic to advanced Computational Biology and Quantum Information)."*
- [[00 - Start Here]] (The Core Spine): **5 phases**, from Foundations & Programming Intro to Employability & Scale.
- [[Checklist]] and the source PDF: **7 stages**: Phase −1 (Bedrock), Phase 0 (Prerequisites), and Years 1–5.
- Nothing in the vault is divided into 17 phases. The only "17" anywhere is the 17 ACM/IEEE CS2023 Knowledge Areas in the archived gap report (`99 - Archive/Baseline Gap Analysis and Audit Report.md`). The Dashboard number looks like a leftover from that report, not a real structure.
- Start Here's 5 phases and the Checklist's 7 stages aren't really in conflict: they are two different views of the program. The spine is a subset, the "get employable" path from §5.3 of the source, and the Checklist is the full program. They just need to be named as such.

### C4. When do specializations open?
- [[00 - Start Here]] (Specialization Branches): *"Enter these only after completing Phase 5 or when professionally required. Pick one primary branch at a time."*
- [[05 - Specialization Branches]]: *"Deep elective domains unlocked only after reaching baseline employability."*
- [[Checklist]] Year 4: Distributed Systems (Block 23) → Theory of Computation (24) → Convex Optimization (25) → **Specialization A, Course 1 (Block 26)** → Intensive (27) → Spec A, Course 2 (28) → Spec B, Course 1 (29). Spec B, Course 2 runs alongside the Capstone in Year 5.
- Check: every Phase 5 course (Databases, Software Construction, Distributed Systems) comes before Block 26 in the Checklist. So "after Phase 5" and "Year 4" describe **the same point** in the course order. The real difference is the gate: Start Here and the hub also require the Employability Portfolio (Phase 5 milestone, "baseline employability"), but the Checklist doesn't track it.

## Decision
*Rulings (accepted 2026-10-09):*

1. **Two layers: a timeboxed Program inside a lifelong system (C1).** *The Program* runs from Phase −1 through Year 5 (Capstone): the core blocks, **two** specialization tracks, the January intensive, the Capstone, and the habits. It is timeboxed at about 8 years. Below 15 h/wk, cut scope using the source program's own order: skip Physics, skip Statistics (Block 22), do one specialization. Don't extend the timeline. *Lifelong Continuation* starts after the Capstone: the other tracks and anything beyond them, with no deadline. This keeps the Dashboard's "lifelong" north star and the evidence-based ~8-year completion rule. It also fits Operating Rule 7 (Scope Control: don't let electives stall the core).
2. **Count only what's in the Program (C2).** Specialization tracks are excluded from planned hours until chosen. Mark all 14 tracks `optional: true` now. When the two tracks are picked (before Block 26), remove the flag from those two only. The Dashboard total then lands at ≈6,485 once two tracks are chosen; habits bring it into range. The four unscheduled Tier 1 blocks stay counted until they're placed or marked optional (that's a separate decision).
3. **Use the real structure and drop "17" (C3).** The full program has **7 stages** (Phase −1, Phase 0, Years 1–5) and is tracked in the [[Checklist]]. The 5-phase **Core Spine** in Start Here is labeled as the employability path through those stages, not a separate count. Remove the "17 sequential phases" wording.
4. **Gate = Phase 5 courses done, i.e. Checklist Block 26 (C4).** Specialization A starts at Checklist Block 26, which by construction comes after all Phase 5 courses, so Start Here and the Checklist agree once that's stated. The Employability Portfolio is **not** a gate for the specializations. It's due by the end of Year 4, before the Capstone proposal, so it can't block the curriculum. "When professionally required" stays as an exception, but using it needs its own decision record. "One primary branch at a time" stays: two tracks, run one after the other.

## Status
**Accepted**: 2026-10-09 (proposed 2026-10-09).

## Consequences
**Easier:** one answer to "how big, how long, what order." The Dashboard totals become a real planning number. Phase talk uses one vocabulary: stages for the full program, spine phases for the employability path. Electives stop inflating the plan.

**Harder / costs:** I have to choose two tracks before Block 26 and treat the other 12 as post-Program. Cutting scope below 15 h/wk means dropping real content (Physics, Statistics, a track). The Portfolio needs its own deadline, because nothing else forces it.

### Changes if accepted
1. **`00 - Dashboard.md`**: replace the **Budget:** line with:
   > **Budget:** The *Program* (Phase −1 → Year 5 Capstone: core blocks + two specialization tracks + habits, ≈6,500–8,000 h) is timeboxed at ~8 years; below 15 hrs/wk, cut scope (Physics → Statistics → second track) instead of extending. After the Capstone, *Lifelong Continuation* (remaining tracks and beyond) has no deadline. Structure: 7 stages (Phase −1, Phase 0, Years 1–5) in the [[Checklist]]; the 5-phase Core Spine in [[00 - Start Here]] is the employability path through them. See [[DR-001 - Program Scope, Phases, and Timeline|DR-001]].
2. **`00 - Dashboard.md`**: in the Degree Progress caption, change "(the 04a/08a/15a bridges)" to "(the 04a/08a/15a bridges and any specialization track not yet chosen)".
3. **14 track notes in `01 - Curriculum/EECS Core/Advanced/`**: add `optional: true # specialization track not yet chosen (DR-001)` to the frontmatter of: Advanced Computer Engineering, Advanced Graphics and Vision, Advanced Programming Languages and Compilers, Advanced Pure Mathematics, Advanced Security and Cryptography, Advanced Systems and Performance, Autonomous Robotics, Computational Biology and Bioinformatics, Deep AI and Machine Learning, Hardware-in-the-Loop Virtualization and Digital Twins, Quantum Information and Computing, Rust for Systems Engineering, Systems Formal Verification, TinyML and Edge AI. (Intensive Cryptopals and Magnum Opus Capstone stay counted.)
4. **`how-i-study.md` §4**: replace the two bullets "The whole program is roughly 6,500–8,000 hours" and "Below 15 hrs/wk…" with:
   - The Program (Phase −1 → Capstone, core + two tracks + habits) is roughly **6,500–8,000 hours**; unchosen tracks are Lifelong Continuation and not counted.
   - Below 15 hrs/wk, cut scope (Physics → Statistics → second track) rather than extending the Program beyond ~8 years.

   Also add a row to §8 Revision History: `2026-10-09 | Phase −1 | DR-001: Program timeboxed ~8 yrs inside a lifelong system; hour budget = core + two tracks.`
5. **`01 - Curriculum/00 - Start Here.md`**: replace the italic line under *Specialization Branches (Elective)* with:
   > *Specialization A starts at Checklist Block 26, after every Phase 5 course is done (Year 4 in the [[Checklist]]). Pick two tracks for the Program and run them one at a time; the rest are Lifelong Continuation. Entering early "when professionally required" needs a Decision Record.*
6. **`01 - Curriculum/05 - Specialization Branches.md`**: replace "Deep elective domains unlocked only after reaching baseline employability." with "Deep elective domains. Specialization A opens at Checklist Block 26, after the Phase 5 courses ([[DR-001 - Program Scope, Phases, and Timeline|DR-001]]). Two tracks belong to the Program; the rest are Lifelong Continuation."
7. **`01 - Curriculum/Employability Portfolio and Review.md`**: add under the title: "*Due by the end of Year 4, before the Capstone proposal. Not a gate for specializations ([[DR-001 - Program Scope, Phases, and Timeline|DR-001]]).*"
8. **`Checklist.md`**: under `## Year 4: Advanced Core and Specializations`, add: "*Specialization A opens at Block 26, once Blocks 23–25 are done. Choose both tracks before Block 26 and clear `optional: true` on those two notes (DR-001). Employability Portfolio due by end of Year 4.*"
9. **This note**: set `status: accepted` and fill in the acceptance date.
