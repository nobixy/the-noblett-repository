# How I Will Study: The Deep Learner's Manifesto
*Last revised: 2026-09-25 (Next scheduled revision: 2027-03-25)* · Home: [[00 - Start Here|Start Here]]

> [!QUOTE]
> "Don't let note-taking become the hobby. Notes exist to support retrieval, synthesis, and building."

---

## 1. Core Cognitive Learning Principles

### A. Retrieval Practice (Testing Effect)
- Reading and highlighting create an **illusion of competence**. They feel fluent because the material is in front of the eyes, not because it is stored in long-term memory.
- The only reliable way to cement understanding is active retrieval: close the book, shut the notes, and recall or explain the concept from scratch.
- Use the **Spaced Blank-Sheet Retrieval Protocol** after every study block: 15 minutes of zero-hint memory dump ([[Blank-Sheet Retrieval Template]]).

### B. The Feynman Technique (Radical Simplicity)
- Strip all jargon. If an idea cannot be explained in simple words and physical analogies to a 12-year-old, the underlying concept is not understood.
- Isolate friction points where you hesitate; those are your true knowledge gaps ([[Feynman Technique Note Template]]).

### C. Elaborative Interrogation (The "Why?" Reflex)
- Never accept a formula, algebraic step, or grammatical rule passively.
- Constantly interrogate: *"Why does this step follow from the previous one?", "What breaks if this assumption is dropped?"*

### D. Subgoal Labeling & Worked Examples
- Label the conceptual milestones inside worked math derivations and code architectures before attempting unassisted problem sets.

### E. Spacing & Interleaving (Desirable Difficulties)
- Cramming produces zero durable storage strength. Space repetitions over days, weeks, and months.
- Interleave problem types (never drill 50 identical problems in a row); force the brain to practice *selecting the correct tool*.

### F. Benjamin Franklin Copywork (For Writing & Grammar)
- Master English prose by analyzing master passages, outlining them, putting them aside for 3 days, and reconstructing the prose from memory ([[Franklin Copywork Template]]).

### G. Focused vs. Diffuse Mode
- **Focused mode:** High-intensity, distraction-free concentration on problem formulation.
- **Diffuse mode:** Unconscious background processing during rest, walks, sleep, or low-cognitive activities. When genuinely stuck on a hard proof after deep focused effort, step away to let diffuse connections form.

---

## 2. The Weekly Shape (Part-Time: ~20 Hours/Week)

| Time Block | Focus | Purpose |
| :--- | :--- | :--- |
| **Weekday mornings (90 min before work)** | Hardest material | Protected time for proofs, arithmetic first principles, theory, algorithms. Uninterrupted focus. |
| **Weekday evenings (60 min)** | Lectures, reading, Anki, writing | Lower cognitive overhead: grammar drills, reading companion texts, Anki card review, daily 500 words. |
| **Saturday (4–6 hrs)** | Build block | Deep continuous flow for systems programming, labs, compilers, CPU verilog, kernels. |
| **Sunday (2 hrs)** | Review & planning | Problem set wrap-up, weekly review in [[log]], writing, planning next week's schedule. |

### 2a. Reading Ramp
*[[DR-008 - Project-First Start and Projects Ladder|DR-008]]: I learn best by building, so the build comes first and reading grows as the habit does.*

| When | Reading per day | What |
| :--- | :--- | :--- |
| Weeks 1–4 | 0–15 min, optional | Builds only. If you feel like it: Lockhart, *Arithmetic*, ch. 1–2. |
| Weeks 5–8 | 15–20 min | Lockhart (about a chapter a week); Williams *Style*, lessons 1–2. |
| Weeks 9–12 | 20–30 min | Add the *Learning How to Learn* videos (Coursera Plus) and Oakley, *A Mind for Numbers*. |
| Phase 0 (P1–P5) | up to 45 min | Each block's reading, always tied to that block's build. |
| Year 1 onward | what the block assigns | Build first: read what the current build needs, when it needs it. |

*Rule: if reading feels like a wall two days running, drop back one row for a week. The builds keep going either way. Reading volume goes up only as the habit holds.*

### 2b. Weekly Mini-Build
Every week ends with one small build (≤2 h, usually the Saturday block) tied to what I studied that week, logged in [[log]]. Weeks 1–12 use the [[Projects Ladder#🪜 Starter Sprint (Weeks 1–12)|Starter Sprint]]; after that, pick from the ideas for the current year in the [[Projects Ladder]].

---

## 3. How to Grade Myself Without a TA

1. **Autograders & Test Suites:** `make grade` in MIT 6.1810, Gradescope for CMU 15-445, full test suites in CS144, BusTub, clox, Monkey, and MIT 6.5840. Tests must pass cleanly.
2. **Timed, Closed-Book Past Exams:** Sit MIT OCW, Berkeley HKN, and CMU exams under strict real conditions without notes. Passing threshold is objective signal.
3. **Formal Write-ups:** If the solution or proof write-up is vague, the understanding is vague.
4. **Strangers' Code Review:** Open PRs and contribute to open source.
5. **The Feynman Technique / Teaching:** Write clear technical blog posts explaining the hardest concept in each block.

---

## 4. Time, Honestly
- MIT counts one "unit" as roughly 1 hr/wk for a 14-week term; a 12-unit subject is ~170 hours.
- The Program (Phase −1 → Capstone, core + two tracks + habits) is roughly **6,500–8,000 hours**; unchosen tracks are Lifelong Continuation and not counted.
- Below 15 hrs/wk, cut scope (Physics → Statistics → second track) rather than extending the Program beyond ~8 years.

---

## 5. Community — Do Not Skip
- **Recurse Center (`recurse.com`):** Free, self-directed 6- or 12-week retreat (remote or NYC). Highest-value single thing available to a self-taught programmer. Apply after Block 12.
- **Study Partner:** One person on the same path, weekly video call, screen-share psets. Roughly doubles completion rates.
- **Communities:** Papers We Love, OSSU Discord, language Discords (Rust, Zig, Haskell), auditing local university lectures.

---

## 6. Notes System Taxonomy
```text
/  (vault root)
  00 - Start Here.md           # the one hub: dashboard, The Path, rules
  how-i-study.md               # written in P1, revised every 6 months
  log.md                       # daily log dashboard (entries in 07 - Daily Log)
  01 - Curriculum/             # one folder per stage, in study order
  02 - Notes/                  # topic indexes (math, systems, theory, hardware, languages) + papers, writing, breadth hubs
  03 - Projects/               # every build, one spec per project
  04 - Reference/              # source program PDF, appendices, book shelf
  05 - Decisions/              # DR-001 … (why the system changed)
  06 - Templates/
  07 - Daily Log/
  99 - Archive/                # cut blocks + the removal list
```
*(Layout set by [[DR-007 - Repo Cleanup|DR-007]]. Calendar and Telemetry Log stay in the root because the iPhone Shortcut automation writes to them by path.)*

Standard note structures are standardized using templates:
- Course syllabus and progress notes use the [[Block Note Template|Block Note Template]].
- Topic notes in `02 - Notes/` (linked from the five topic indexes) use the [[Zettelkasten Atomic Note Template|Zettelkasten Atomic Note Template]].

---

## 7. Mindset, Habits, and Research Practices

### A. Mindset and Habits
*Merged here from the old Mindset Hub by [[DR-007 - Repo Cleanup|DR-007]].*

#### 1. Core Mindset: Grit & Growth
- **Grit (Angela Duckworth):** Focus on passion and perseverance. Talent is merely a multiplier for effort; effort counts twice.
- **Growth Mindset:** Frame every setback as a stepping stone. Avoid "I am not smart enough"; use "I haven't learned this yet."

#### 2. Habits of Successful People
- **Time-Blocking:** Protect the calendar. Assign specific tasks to specific blocks of time (Cal Newport's *Deep Work*).
- **The Eisenhower Matrix:** Categorize tasks into Urgent/Important. Ruthlessly eliminate the non-important.
- **Consistency:** Daily 1% improvements compound over years.

#### 3. High-Leverage Hobbies
- **Aerobic Exercise:** Regular cardio enhances neuroplasticity and clears the diffuse mode of thinking.
- **Mindfulness & Meditation:** Builds the metacognitive muscle to notice when focus drifts, bringing attention back to the present task.

### B. CS Research Practices
- **Version Control:** Commit early and cleanly using Git.
- **Reproducibility:** Code must be reproducible. Use Docker to build reliable, reproducible execution environments.

---

## 8. Revision History

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
| 2026-10-10 | Phase -1 (Bedrock Foundation) | [[DR-007 - Repo Cleanup\|DR-007]]: Repo cleanup — 61 AI-generated or one-off archive files removed (recoverable from git), Mindset Hub merged into §7A, 11 → 8 top-level folders, decisions moved to `05 - Decisions/`. Hours unchanged (6,005). |
| 2026-10-10 | Phase -1 (Bedrock Foundation) | [[DR-008 - Project-First Start and Projects Ladder\|DR-008]]: Build first — Week 1 checklist, 12-week Starter Sprint of fun builds, books become companions on a stated Reading Ramp (§2a), weekly mini-build (§2b), every block has a build, [[Projects Ladder]]. Hours unchanged (6,005). |
