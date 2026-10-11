---
title: "DR-011: Sectioned Curriculum and Frontmatter Schema"
type: decision-record
status: accepted
date: 2026-10-10
accepted: 2026-10-10
tags:
  - adr
  - decision-record
---

# DR-011: Sectioned Curriculum and Frontmatter Schema

*Uses the [[Decision Record]] template. Follows and amends [[DR-010 - Project-First Original Curriculum|DR-010]]; supersedes [[DR-001 - Program Scope, Phases, and Timeline|DR-001]] to [[DR-009 - Learning Method Deep Dives|DR-009]] together with DR-010. Accepted 2026-10-10 after a full review of the vault.*

## Context

A review of the vault after DR-010 found:

1. **Time everywhere.** Hours, weeks, "Week 1", day names, minute targets, pace estimates and Hours/Weeks columns were spread across Start Here, the README, the protocols, every stage, overview and project. They contradicted each other and turned the plan into a schedule to fall behind on — the same "too big to begin" problem DR-010 described.
2. **No shared frontmatter.** Curriculum notes used different field sets (some with `hours`/`weeks`, some with v1 fields), so order and prerequisites could not be read reliably.
3. **Ordering conflicts.** The Module 05 gate, the place of Module 12, and the "one project at a time" rule were stated differently in different notes.
4. **v1 leftovers in active notes:** v1 fields in the Daily Log template and `log.md`, v1 placeholders in two templates, Atlas notes still pointing to v1 blocks as the current plan, broken heading links, and decision records DR-001 to DR-009 still marked accepted.
5. **Folder names in DR-007 are out of date.** DR-007 describes `02 - Notes/`, `03 - Projects/`, `04 - Reference/`, `05 - Decisions/`, `06 - Templates/`, `07 - Daily Log/`. The vault actually uses `02 - Atlas/`, `03 - Journal/` and `04 - System/`.
6. **No English placement**, and no way to skip Lab 00 or Lab 01 for someone who already knows the material.

## Decision

1. **Folder names (records what exists).** Top level: `00 - Start Here.md`, `README.md`, `how-i-study.md`, `study-protocols.md`, `courses-and-videos.md`, `log.md`; curriculum folders `00-foundations/` … `13-capstone/`; `02 - Atlas/` (topic indexes, learning methods, hubs, appendices); `03 - Journal/` (session log entries); `04 - System/` (templates, decision records, this schema); `99 - Archive/` (v1 plan and cut content, historical only). DR-007's folder list is historical.
2. **No time in the curriculum.** The curriculum is measured in **sessions** and **sections**, never hours, days, weeks, months or years:
   - Every session has the same loop — warm-up recall, focused work, retrieval [R], log ([study-protocols § The session loop](<../study-protocols.md#the-session-loop>), the one canonical description; README and how-i-study §2 summarise it and link there).
   - Sessions group into numbered sections; stage routines are written as Section N, Sessions 1–5; every section closes with a **Section Review** (replaces the Weekly Review). Section 1 in Start Here is laid out as Sessions 0–7.
   - Phases A–E stay as groupings, without durations.
   - Removed: Hours/Time/Weeks columns, pace estimates, minute targets for demos, talks and recordings (now "short"), time-boxed stuck rules (now **three honest attempts**, then a stuck note and a break), day names (now Session numbers).
   - **Kept on purpose** (not schedule): dates in journal entries, decision-record history, git and backup metadata, everything in `99 - Archive/`; time inside subject matter (word problems, timing experiments, measured quantities); timings that are part of a technique (spaced-repetition intervals in LM09 and the review schedule, Keshav's pass times, Pomodoro, dictation pauses, fluency drills such as a one-minute facts sheet); software features (Study Deck due dates and streaks); and life-admin items in Human Systems.
3. **Frontmatter schema.** All curriculum notes use `title`, `id`, `type`, `module`, `track`, `stage`, `phase`, `order`, `prerequisites`, `checkpoints` (plus a few optional fields), defined in [Frontmatter Schema](<Frontmatter Schema.md>). `order` is one global sequence in steps of 10; Start Here's checklist follows it. `type: maker-lab` became `type: lab` + `kind: maker`.
4. **Ordering resolutions:**
   - **One build project at a time** (Start Here rule 2): a build project is any project spec (foundation, module or Module 12). Stage lessons, labs and units may run alongside it, and up to two modules may be open at once.
   - **Module 05 gate:** Module 05 starts only after both foundation track assessments (English after E10, Math after M11) are passed, and after Modules 02 and 03.
   - **Module 12 placement:** Module 12 runs alongside Modules 06–11 as the math sessions, after M11 and the math track assessment. Its projects count as the open build project. **Chance Lab comes last** — it waits until Courier (Module 09) and sits in Phase D.
5. **Placement and skip checks:** a new [English placement diagnostic](<../00-foundations/english/placement.md>) (`FND-EN-PLACEMENT`) is Session 0 of Section 1, next to the M01 diagnostic. [Lab 00](<../01-intro-cs-taste/labs/lab-00-machine-setup.md#skip-check>) and [Lab 01](<../01-intro-cs-taste/labs/lab-01-python-first-steps.md#skip-check>) got skip checks.
6. **Session log fields:** the [Daily Log Entry Template](<Daily Log Entry Template.md>) and [log.md](<../log.md>) use `worked_on`, `sessions`, `flashcards`, `copywork`. The v1 fields (`block`, `study_hours`, `anki`, `words_500`) are gone from both; old journal entries keep them as historical records.
7. **Templates:**
   - `Weekly Review Template` → [Section Review Template](<Section Review Template.md>).
   - `Project Build Spec Template` rewritten as a v2 build log (`type: build-log`, project id instead of `associated_block`; no `valgrind_clean`, dates or hours).
   - `Block Note Template` (v1 only) moved to `99 - Archive/v1 - Course-Based Curriculum/`.
   - Time removed from the Milestone Checkpoint, Demo Script (numbered parts instead of timestamps), Blank-Sheet Retrieval (no timer field) and Franklin Copywork (a later session instead of "3 days") templates; the 500-Word Essay type `daily-500` became `essay`.
8. **Renames:** `00-foundations/first-twelve-weeks.md` → [first-sections.md](<../00-foundations/first-sections.md>) (Sections 1–12).
9. **Atlas v1 retirement:** Atlas notes no longer present v1 blocks or v1 hours as the plan. Topic indexes point to the modules that teach each topic; v1 courses stay only as plain text under headings marked *historical*. The Learning Methods hub maps each method to its protocol in the curriculum. Links into `99 - Archive/` remain only where labelled historical (and in DR-001 to DR-009 and old journal entries).
10. **DR-001 to DR-009** are marked `status: superseded` (by DR-010 and DR-011). They are kept unchanged otherwise as history.
11. **No job track.** The curriculum will **not** add a job-readiness or employability track. The v1 "job-ready" path (DR-003) and the Employability Portfolio stay archived; the Monkeytype OSS note no longer links to them.
12. **Other fixes in the same change:** Module 08 Lab 03 carries an "untested" warning (as DR-010 noted, its RISC-V code has not been run); Appendix F's SICP link points to the official free full text, and the CS:APP labs link uses https; orphan notes are linked; broken heading links are fixed.

## Status

**Accepted**: 2026-10-10.

## Consequences

- **Easier:** no schedule to fall behind on — progress is "which section, which session"; one place defines the session loop; order and prerequisites are machine-readable; a learner who already knows something can test out of it.
- **Harder:** there is no estimate of how long anything takes. The only pacing hint left is one rough guide in the Module 01 overview (which English and Math stages you are likely on when it ends). If a sense of pace is needed later, measure it from the session log rather than writing it into the curriculum.
- **Watch:** new notes must follow the [Frontmatter Schema](<Frontmatter Schema.md>) and use sessions/sections, not time. Module 08 Lab 03 still needs a real run.
