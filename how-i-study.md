---
title: "How I Will Study"
type: hub
tags: [hub, study-methods]
---

# How I Will Study: The Deep Learner's Manifesto
*Revised whenever a Decision Record changes the method (latest: [DR-011](<04 - System/DR-011 - Sectioned Curriculum and Frontmatter Schema.md>)).* · Home: [[00 - Start Here|Start Here]] · Exact routines: [study-protocols](study-protocols.md)

> [!QUOTE]
> "Don't let note-taking become the hobby. Notes exist to support retrieval, synthesis, and building."

---

## 1. Core Cognitive Learning Principles
*Every one of these is turned into a short, exact routine with a letter code (R, F, W, S, I, C, D, T, V) in [study-protocols](study-protocols.md). Every stage, lab, and project in the curriculum uses those codes ([DR-010](<04 - System/DR-010 - Project-First Original Curriculum.md>)).*

*Deep dive + a project for every method below and more (spacing, interleaving, dual coding, self-explanation, chunking, deep work, Zettelkasten, three-pass reading, Pólya, mindset): [[LM00 - Learning Methods Hub|Learning Methods Hub]] ([[DR-009 - Learning Method Deep Dives|DR-009]]). There is no such thing as a personal "learning style": [[Learning Styles Myth]].*

### A. Retrieval Practice (Testing Effect)
- Reading and highlighting create an **illusion of competence**. They feel fluent because the material is in front of the eyes, not because it is stored in long-term memory.
- The only reliable way to cement understanding is active retrieval: close the book, shut the notes, and recall or explain the concept from scratch.
- Use the **Blank-Sheet Retrieval Protocol** [R] at the end of every session: a zero-hint memory dump ([[Blank-Sheet Retrieval Template]]).
- → [[LM02 - Retrieval Practice|LM02 deep dive + project]]

### B. The Feynman Technique (Radical Simplicity)
- Strip all jargon. If an idea cannot be explained in simple words and physical analogies to a 12-year-old, the underlying concept is not understood.
- Isolate friction points where you hesitate; those are your true knowledge gaps ([[Feynman Technique Note Template]]).
- → [[LM01 - Feynman Technique|LM01 deep dive + project]]

### C. Elaborative Interrogation (The "Why?" Reflex)
- Never accept a formula, algebraic step, or grammatical rule passively.
- Constantly interrogate: *"Why does this step follow from the previous one?", "What breaks if this assumption is dropped?"*
- → [[LM03 - Elaborative Interrogation|LM03 deep dive + project]]

### D. Subgoal Labeling & Worked Examples
- Label the conceptual milestones inside worked math derivations and code architectures before attempting unassisted problem sets.
- → [[LM10 - Worked Examples and Subgoal Labeling|LM10 deep dive + project]]

### E. Spacing & Interleaving (Desirable Difficulties)
- Cramming produces zero durable storage strength. Space repetitions out over growing gaps (the intervals are part of the technique: see LM09).
- Interleave problem types (never drill 50 identical problems in a row); force the brain to practice *selecting the correct tool*.
- → [[LM09 - Spacing and Spaced Repetition|LM09 deep dive + project]] · [[LM05 - Interleaving|LM05 deep dive + project]]

### F. Benjamin Franklin Copywork (For Writing & Grammar)
- Master English prose by analyzing master passages, outlining them, putting them aside until a later session, and reconstructing the prose from memory ([[Franklin Copywork Template]]).
- → [[LM06 - Franklin Copywork|LM06 deep dive + project]]

### G. Focused vs. Diffuse Mode
- **Focused mode:** High-intensity, distraction-free concentration on problem formulation.
- **Diffuse mode:** Unconscious background processing during rest, walks, sleep, or low-cognitive activities. When genuinely stuck on a hard proof after deep focused effort, step away to let diffuse connections form.
- → [[LM11 - Focused and Diffuse Thinking|LM11 deep dive + project]]

---

## 2. The Session Structure

*Summary only. The canonical description is [study-protocols § The session loop](study-protocols.md#the-session-loop); the [README](README.md#the-session-structure) has the same table.* There are no hours, dates or deadlines in this curriculum: it is measured in **sessions** and **sections**.

| Unit | Shape |
| :--- | :--- |
| **Session** | Warm-up recall → focused work on one thing → blank-sheet retrieval [R] → log entry. |
| **Math session** | Hardest material, when I'm freshest: proofs, arithmetic from first principles, algorithms. |
| **English session** | Stage lesson, spelling, copywork [C], optional fun write. |
| **Build session** | The next lab session or project milestone: systems programming, circuits, the CPU in Digital, kernels. One build project at a time. |
| **Section** | A numbered group of sessions, closed by a **Section Review** in [[log]] (flashcards, cold re-do, a spoken recording, plan the next section). |
| **Minimum session** | Flashcards + one copywork sentence + a two-line log. |

### 2a. Reading Ramp
*[[DR-008 - Project-First Start and Projects Ladder|DR-008]] (historical), kept by [DR-010](<04 - System/DR-010 - Project-First Original Curriculum.md>): I learn best by building, so the build comes first and reading grows as the habit does.*

| When | Reading | What |
| :--- | :--- | :--- |
| Sections 1–4 | optional | Stage lessons and builds only. If I feel like it: Lockhart, *Arithmetic*, alongside M01–M02. |
| Sections 5–12 | a little, in most sessions | Lockhart with M03–M05; copywork passages count as reading. |
| From E08 | a little more | Williams, *Style*, as a companion to E08–E10. |
| Modules 02+ | what the build needs | Each module's `resources.md` lists second explanations. Read the chapter a milestone needs, when it needs it. |

*Rule: if reading feels like a wall two sessions running, drop back one row for a section. The builds keep going either way.*

### 2b. Build Sessions
Every build session works on the next milestone of the current project ([Start Here](<00 - Start Here.md>) shows which). Each milestone ends with a Milestone Checkpoint (R + F + W). Log it in [[log]].

---

## 3. How to Grade Myself Without a TA

1. **My own test suites:** every project spec says what to test. Tests must pass cleanly — including the hard kinds: random differential tests against a second implementation, crash tests, and fuzzing.
2. **"Done when" lists and rubrics:** every stage and project has one. I score myself honestly, and I don't tick a box early.
3. **Closed-book problem sets:** at each module close (MIT OCW and similar past exams for the math modules). The score is objective signal.
4. **Formal write-ups:** design docs, lab reports, specifications. If the write-up is vague, the understanding is vague.
5. **Other people:** usability tests of my instructions, reviews of my design docs, strangers' code review, playtesters.
6. **The Feynman technique / teaching:** recorded explanations, one per section, and an explainer for the hardest idea in each project.

---

## 4. Pace, Honestly
- There is no schedule. I move on when an item's "Done when" list is true, in the order of [Start Here](<00 - Start Here.md>) and each item's `prerequisites`.
- *Historical:* the advanced tracks from the superseded v1 plan (in `99 - Archive/`) are not part of this curriculum. Taking any of them on after the core would need a new Decision Record.
- When life gets busy, slow down rather than skip foundations; the minimum session (flashcards + one copywork sentence) keeps the habit alive.

---

## 5. Community — Do Not Skip
- **Recurse Center (`recurse.com`):** Free, self-directed retreat (remote or NYC). Highest-value single thing available to a self-taught programmer. Apply after Module 05.
- **Study Partner:** One person on the same path, a regular video call, screen-share psets. Roughly doubles completion rates.
- **Communities:** Papers We Love, OSSU Discord, language Discords (Rust, Zig, Haskell), auditing local university lectures.

---

## 6. Notes System Taxonomy
```text
/  (vault root)
  README.md                    # how the curriculum works
  00 - Start Here.md           # dashboard and checklist
  how-i-study.md               # this manifesto, revised by Decision Record
  study-protocols.md           # the methods as exact routines (R F W S I C D T V) and the session loop
  log.md                       # session log dashboard (entries in 03 - Journal)
  00-foundations/              # first-sections.md; english/ (placement, E01–E10) and math/ (M01–M11), each with projects/
  01-intro-cs-taste/ … 13-capstone/   # one folder per module: overview.md (with its Video course), labs/, projects/<name>/spec.md, resources.md (with the lecture map)
  02 - Atlas/                  # learning-method deep dives (LM00–LM16), topic indexes, hubs, book shelf
  03 - Journal/                # session log entries (YYYY-MM-DD, from the daily-notes plugin)
  04 - System/                 # templates, decision records (DR-001 …), Frontmatter Schema
  99 - Archive/                # historical: the superseded v1 course-based plan and cut material
~/workbench/                   # (outside the vault) my code, design docs, lab reports, recordings — one folder per project
```

Templates in `04 - System/`: Milestone Checkpoint, Design Doc, Lab Report, Demo Script, Blank-Sheet Retrieval, Feynman Note, Franklin Copywork, Section Review, Daily Log (session log). Every curriculum file's frontmatter follows the [Frontmatter Schema](<04 - System/Frontmatter Schema.md>).

---

## 7. Mindset, Habits, and Research Practices

### A. Mindset and Habits
*Merged here from the old Mindset Hub by [[DR-007 - Repo Cleanup|DR-007]].*

#### 1. Core Mindset: Grit & Growth
- **Grit (Angela Duckworth):** Focus on passion and perseverance. Talent is merely a multiplier for effort; effort counts twice.
- **Growth Mindset:** Frame every setback as a stepping stone. Avoid "I am not smart enough"; use "I haven't learned this yet."

#### 2. Habits of Successful People
- **Session-Blocking:** Protect study sessions. Assign one specific task to each session (Cal Newport's *Deep Work*).
- **The Eisenhower Matrix:** Categorize tasks into Urgent/Important. Ruthlessly eliminate the non-important.
- **Consistency:** Small improvements every session compound.

*Evidence check: both ideas are weaker than they sound; see [[LM15 - Growth Mindset and Grit|LM15]]. Deep work and Pomodoro: [[LM12 - Deep Work, Time-Blocking and Pomodoro|LM12]].*

#### 3. High-Leverage Hobbies
- **Aerobic Exercise:** Regular cardio enhances neuroplasticity and clears the diffuse mode of thinking.
- **Mindfulness & Meditation:** Builds the metacognitive muscle to notice when focus drifts, bringing attention back to the present task.

### B. CS Research Practices
- **Version Control:** Commit early and cleanly using Git.
- **Reproducibility:** Code must be reproducible. Use Docker to build reliable, reproducible execution environments.

---

## 8. Revision History

*Historical record: rows are kept as written at the time, including v1 hours and phases. Links to archived v1 notes are historical.*

| Date | Phase / Block Reached | Major Adjustments Made |
| :--- | :--- | :--- |
| 2026-09-25 | Phase -1 (Bedrock Setup) | Added the 8 core cognitive study systems (Feynman, Franklin, Blank-Sheet, Elaborative Interrogation) and Bedrock Math/English. |
| 2026-09-25 | Phase -1 (Mindset Update) | Added Mindset, Deep Work, and CS Research Practices sections. |
| 2026-10-09 | Phase -1 (Bedrock Foundation) | [[DR-001 - Program Scope, Phases, and Timeline\|DR-001]]: Program timeboxed ~8 yrs inside a lifelong system; hour budget = core + two tracks. |
| 2026-10-09 | Phase -1 (Bedrock Foundation) | [[DR-002 - Vault Refactor and Canonical Numbering\|DR-002]]: Checklist numbering made canonical; E1–E4 made optional electives; Track 15 (Full-Stack) added; hubs fleshed out. |
| 2026-10-09 | Phase -1 (Bedrock Foundation) | [[DR-003 - One Path Restructure\|DR-003]]: Curriculum folders follow study order (Phase −1 → Year 5); Dashboard, Checklist and Start Here merged into one hub, [[00 - Start Here\|Start Here]], with the job-ready path as 💼 markers on The Path. |
| 2026-10-09 | Phase -1 (Bedrock Foundation) | [[DR-004 - Content Overhaul\|DR-004]]: Content overhaul — EE core (circuits, signals, diff eq), ML, deep learning and parallel/GPU made core; SICP, two non-EECS tracks cut; three tracks merged; every track tied to real free courses. Planned hours 5,805. |
| 2026-10-09 | Phase -1 (Bedrock Foundation) | [[DR-005 - Capstone and Maker Thread\|DR-005]]: Capstone redesigned as an autonomous drone-swarm prototype (civilian/dual-use, no weapons); 🔧 Maker thread (5 labs + Drone Lab); Block 19a network science and mesh; Block 24a applied crypto core; Cryptopals required; Databases and Theory of Computation optional. Planned hours 5,995. |
| 2026-10-09 | Phase -1 (Bedrock Foundation) | [[DR-006 - Digital Twin, EW Resilience and Fun Prerequisites\|DR-006]]: Capstone gains a digital twin (M2b) and defensive, simulation-only EW resilience; every Phase −1/0 block gets a fun build; Coursera Plus companions and a NeetCode Pro sprint (ends Feb 6, 2027) added. Planned hours 6,005. |
| 2026-10-10 | Phase -1 (Bedrock Foundation) | [[DR-007 - Repo Cleanup\|DR-007]]: Repo cleanup — 61 AI-generated or one-off archive files removed (recoverable from git), Mindset Hub merged into §7A, 11 → 8 top-level folders, decisions given their own folder. Hours unchanged (6,005). |
| 2026-10-10 | Phase -1 (Bedrock Foundation) | [[DR-008 - Project-First Start and Projects Ladder\|DR-008]]: Build first — Week 1 checklist, 12-week Starter Sprint of fun builds, books become companions on a stated Reading Ramp (§2a), weekly mini-build (§2b), every block has a build, [[Projects Ladder]]. Hours unchanged (6,005). |
| 2026-10-10 | Phase -1 (Bedrock Foundation) | [[DR-009 - Learning Method Deep Dives\|DR-009]]: 16 learning-method deep dives with honest evidence ratings and a 2–5 h project each, plus a learning-styles myth note; [[LM00 - Learning Methods Hub\|hub]] with suggested order; slotted into the Starter Sprint and Phase 0 as swaps. Hours unchanged (6,005). |
| 2026-10-10 | Phase A (Foundations) | [DR-010](<04 - System/DR-010 - Project-First Original Curriculum.md>): Curriculum rebuilt project-first with original projects: English E01–E10 and Math M01–M11 from absolute basics, an Intro CS Taste module, Modules 02–13 with original specs; methods made into exact routines ([study-protocols](study-protocols.md)); v1 course-based plan archived. Core ≈ 2,900 h. |
| 2026-10-10 | Phase A (Foundations) | [DR-011](<04 - System/DR-011 - Sectioned Curriculum and Frontmatter Schema.md>): time removed from the curriculum (sessions and sections instead of hours, weeks and dates); frontmatter schema for the tracker; one canonical session structure; English placement and Lab 00/01 skip checks; ordering conflicts resolved; v1 residue retired from active notes; no job track. |
