---
title: "DR-012: Video Course Picks"
type: decision-record
status: accepted
date: 2026-10-10
accepted: 2026-10-10
tags:
  - adr
  - decision-record
---

# DR-012: Video Course Picks

*Uses the [[Decision Record]] template. Builds on [[DR-011 - Sectioned Curriculum and Frontmatter Schema|DR-011]] (no time in the curriculum; frontmatter schema).*

## Context

The central index `courses-and-videos.md` listed many courses and channels per stage and module (often five or more), without saying which one to use or which lectures go with which lab. Several entries were weak fits (general overviews for deep modules), some Coursera links no longer worked at the slugs checked, and Coursera has since replaced free auditing with a free preview for most courses. The two foundation tracks had no resources note at all.

## Decision

1. **One primary and at most one alternate video course** for each foundation track and each module, reviewed for fit with the module's labs and projects, level, language (Python, C, RISC-V), quality, completeness and free access. Every pick was checked as reachable when chosen.
2. **Where the picks live:** each module's `resources.md` has a **Video course** section with the primary, the alternate, why each fits, a **lecture-to-vault map** (lecture numbers → stages, labs, projects) and the gaps no course covers. New notes [Foundations: English — Resources](<../00-foundations/english/resources.md>) (`FND-EN-RES`) and [Foundations: Math — Resources](<../00-foundations/math/resources.md>) (`FND-MA-RES`) do the same for the tracks.
3. **Videos live in each course's own notes — no central index.** Joseph removed `courses-and-videos.md` himself: *"I want videos to be in the markdown of the course."* So every track and module **overview** has a short **Video course** section (primary and alternate with links, plus a link to the map), and the full section with the lecture-to-vault map stays in that course's `resources.md`. Weak and duplicate recommendations were removed from the resources notes; per-stage "Watch" lists in the stage files stay as optional extras.
   - The index's other content moved: the rules for using courses, the Coursera note and the session-loop table to [study-protocols § Using video courses](<../study-protocols.md#using-video-courses>); touch typing and *Learning How to Learn* / *Mindshift* to [The First Sections](<../00-foundations/first-sections.md>).
   - Every link to the index in active notes now points to the course's own overview or resources note. README, how-i-study and Start Here no longer list the file.
4. **No new frontmatter field.** The picks are content, not metadata; the two new notes use the existing `reference` schema (ID patterns added to the [Frontmatter Schema](<Frontmatter Schema.md>)).
5. **No time.** Maps use lecture, chapter or playlist numbers only — no durations, terms or pace.

| Track / module | Primary | Alternate |
| :-- | :-- | :-- |
| Foundations: English | Khan Academy Grammar | Writing in the Sciences (Stanford, Coursera) |
| Foundations: Math | Khan Academy math (Arithmetic → Algebra 2) | Math Antics |
| 01 | CS50P (Harvard) | Crash Course Computer Science |
| 02 | MIT 6.100L | The Missing Semester (MIT) |
| 03 | MIT 6.042J | Trefor Bazett, Discrete Math |
| 04 | Ben Eater, 8-bit breadboard computer | Understanding PID Control (MATLAB) |
| 05 | NeetCode: DSA for Beginners + Advanced Algorithms | MIT 6.006 |
| 06 | ETH Digital Design and Computer Architecture (Mutlu) | Ben Eater, 8-bit breadboard computer |
| 07 | CMU 15-213 | CS50x |
| 08 | MIT 6.S081 | Berkeley CS162 |
| 09 | Kurose & Ross video lectures | Ben Eater, Networking tutorial |
| 10 | Chrome University (selected talks) | CS50W |
| 11 | CMU 15-445 | CS50 SQL |
| 12 | 3Blue1Brown, Essence of Calculus + Linear Algebra | Harvard Stat 110 |
| 13 | Simon Peyton Jones, paper and talk advice | none (rewatch the path's module course) |

## Status

**Accepted**: 2026-10-10.

## Consequences

- **Easier:** one obvious companion per module, named in the module's own overview, and each lab and project names the lectures to watch.
- **Harder:** links can move. Two picks rest on sources outside the provider's control: the CMU 15-213 lectures on YouTube are a third-party re-upload (CMU's own recordings need a login), and Khan Academy pages block automated checking, so they were confirmed by search rather than fetched.
- **Watch:** NeetCode Pro access ends Feb 6, 2027 ([[DR-006 - Digital Twin, EW Resilience and Fun Prerequisites|DR-006]]); Module 05's note says to swap to MIT 6.006 if access has ended. Re-check links when a module starts.
