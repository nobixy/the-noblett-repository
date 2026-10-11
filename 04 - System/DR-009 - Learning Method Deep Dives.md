---
title: "DR-009: Learning Method Deep Dives"
type: decision-record
status: superseded
superseded_by: [DR-010, DR-011]
date: 2026-10-10
accepted: 2026-10-10
tags:
  - adr
  - decision-record
---

# DR-009: Learning Method Deep Dives

> [!WARNING] Superseded
> Superseded by [[DR-010 - Project-First Original Curriculum|DR-010]] and [[DR-011 - Sectioned Curriculum and Frontmatter Schema|DR-011]]. Kept as a historical record: its dates, hours, weeks, phases and links into `99 - Archive/` describe the v1 plan and are not current instructions.

*Uses the [[Decision Record]] template. Follows [[DR-008 - Project-First Start and Projects Ladder|DR-008]]. Accepted and applied 2026-10-10. Checkpoint before this change: git commit `edd2829`.*

## Context
"For each learning style/framework, can you make a project? Just do a deep dive on each and have a project for each."

The vault named about 16 methods across [[how-i-study]] §1, [[B0 - The Deep Learner's Toolkit|B0]], [[P1 - Learning How to Learn|P1]], [[P2 - Reading, Thinking, and Writing|P2]], the templates and the mindset section. None had a project, and their evidence was never graded. The hour cap leaves ~15 h of margin, so the projects have to be swaps, not additions.

## Decision
- **16 deep-dive notes** in `01 - Curriculum/09 - Supporting Systems/Learning Methods/`. Each has: the method in plain words, the evidence with real sources and an honest rating, how to use it in EECS, common mistakes, and a 2–5 h project with a done-when line. Duplicates were merged: blank-sheet retrieval → LM02; spacing and Anki → LM09; deep work, time-blocking and Pomodoro → LM12; *Learning How to Learn* content → LM08, LM11, LM12.
- **A [[Learning Styles Myth]] note** (Pashler et al. 2008): VARK-type "learning styles" are not supported; methods are.
- **A [[LM00 - Learning Methods Hub|Learning Methods Hub]]** with a suggested order: no-code and Scratch first, Python beginner next, intermediate Python last.
- **Wired in:**
  - how-i-study §1 links each method to its deep dive.
  - The mindset section links the evidence check.
  - The [[Projects Ladder]] Starter Sprint gets a "method of the week" column, plus a Phase 0 list.
  - B0, BM, BW, P1, P2, P4 and P5 each list the projects they count, and what each project replaces.
  - Start Here links the hub.

| ID | Method | Evidence | Project | h | Counts toward |
| :-- | :--- | :--- | :--- | :-- | :-- |
| LM01 | Feynman Technique | Not tested directly; built on stronger effects (moderate) | Explain-It: a video or post about your Week 1 build | 2 | B0 |
| LM02 | Retrieval Practice | Strong | Blank-Sheet Timer (Scratch first, Python later) | 3 | B0 |
| LM03 | Elaborative Interrogation | Moderate | Why-Ladders for 10 math rules (+ optional why-bot) | 2 | BM |
| LM04 | Dual Coding | Moderate | Draw-It set in Excalidraw | 2 | BM |
| LM05 | Interleaving | Moderate | Shuffle Drill: mixed-problem generator | 3 | BM |
| LM06 | Franklin Copywork | Anecdotal; no controlled studies | Copywork Diff tool | 3 | BW |
| LM07 | Self-Explanation | Moderate to strong | Narrated Solutions | 2 | BW |
| LM08 | Chunking and the Illusion of Competence | Strong (chunking); strong (illusions of competence) | Calibration Tracker | 3 | BM |
| LM09 | Spacing and Spaced Repetition | Strong | Your own spaced-repetition app (Leitner → SM-2 → FSRS) | 5 | P1 |
| LM10 | Worked Examples and Subgoal Labeling | Strong for beginners | Subgoal Annotator | 3 | P4 |
| LM11 | Focused and Diffuse Thinking | Useful metaphor; incubation evidence moderate | Stuck-Log experiment | 2 | P5 |
| LM12 | Deep Work, Time-Blocking and Pomodoro | Weak to moderate; mostly practitioner advice | Focus Timer CLI | 4 | P5 |
| LM13 | Three-Pass Paper Reading | Practitioner advice; not tested | One paper, three passes (twice) | 3 | P2 |
| LM14 | Pólya's Problem Solving | Classic framework; works with practice and self-monitoring | Puzzle week with labeled steps | 3 | P2 |
| LM15 | Growth Mindset and Grit | Contested; small effects | Then-vs-Now | 2 | P1 |
| LM16 | Zettelkasten | Practitioner method; not tested | Vault Link-Graph Analyzer | 5 | P5 |

Sources were checked 2026-10-10:
- Roediger & Karpicke 2006; Cepeda et al. 2006 (839 assessments); Rohrer & Taylor 2007.
- Sweller & Cooper 1985; Margulieux et al. 2012; Bisra et al. 2018 (g ≈ 0.55).
- Sio & Ormerod 2009; Biwer et al. 2023; Sisk et al. 2018 (r ≈ 0.10); Credé et al. 2017.
- Pashler et al. 2008; Anki FSRS since 23.10.
- Dunlosky et al. 2013 ratings as published.

## Consequences
**Hours:** unchanged, **6,005 h** core. Project work is about 47 h, 37 h of it new activity, all swapped inside existing block hours:
- B0 +5
- BM +10
- BW +5
- P1 +3
- P4 +3
- P5 +11
- P2 +0

The total stays ≈7,805–8,305 h with ~15 h of margin.

**Flags:**
- B0 and P5 are now full. If the projects run long, the hours to watch are B0 (20 h) and P5 (40 h).
- Several methods are rated practitioner advice, anecdotal or contested: Feynman, Franklin copywork, three-pass reading, Zettelkasten, Pomodoro, growth mindset and grit. They stay because they're cheap and useful, but don't expect miracles from them.
- The day-job weekly schedule was not changed.

**Undo:** `git checkout -- . && git clean -fd` (back to `edd2829`).

> [!WARNING] Do not run this Undo line now
> It was written for the moment right after this change, before it was committed. Today `git checkout -- . && git clean -fd` would throw away **all** uncommitted edits and delete every untracked file in the vault (new notes, today's log). To undo this decision now, use `git revert <commit>` or restore single files with `git checkout <commit> -- "<path>"`.
