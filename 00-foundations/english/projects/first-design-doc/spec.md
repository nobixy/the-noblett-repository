---
title: "Project: First Design Doc"
track: english
stages: "E10"
hours: 15
artifact: "A reviewed and revised design document for Copydiff (Module 05)"
deliverable: "Design doc v1, review notes, design doc v2, and a change log between them"
---

# Project: First Design Doc

| | |
| :-- | :-- |
| **When** | E10, weeks 2–3 |
| **Time** | About 15 hours |
| **You build** | The design document for **Copydiff**, the copywork-comparison tool you will build in [Module 05](../../../../05-data-structures-and-algorithms/projects/copydiff/spec.md). You write it now, get it reviewed, and revise it. When you reach Module 05, you build from it |
| **Deliverable** | v1, review notes, v2, and a change log |

> **If you are already past Module 05** (or your path changed), write this design doc for whichever major project is next on your path instead. The process is the same.

---

## Why this matters

This is the bridge between the English track and the rest of the curriculum. From Module 05 on, every major project starts with a design doc. This is your first one, done carefully, with a real review, on a tool you actually want.

**Why Copydiff?** You have been doing Franklin copywork for months. Step 6, the diff (comparing your rebuild to the original word by word), is slow by hand. Copydiff does it for you: it lines up your version against the original and shows exactly which words you dropped, added, or changed, and which spelling and punctuation differed. You know this problem better than anyone, because you have done it by hand hundreds of times. That makes you the ideal person to design the solution.

**Real-world analogs:** design docs at software companies (often called RFCs or one-pagers), engineering proposals, grant proposals.

---

## What Copydiff must do (the problem, not the solution)

These are the user needs. Your design doc decides *how*. Don't look ahead at the Module 05 spec until you've finished v2; designing it yourself is the point.

1. **Input:** two texts: the original passage and your rebuild.
2. **Output:** a comparison that shows, for each part of the text, whether it matches, was removed, was added, or was changed.
3. It must be able to tell **spelling differences** (*seperate* vs *separate*) apart from **word-choice differences** (*quick* vs *fast*).
4. It must handle **punctuation** differences, and the user should be able to turn punctuation checking on or off.
5. It must produce **counts** you can log over time (e.g. words changed, spelling errors, punctuation differences).
6. It must work in the terminal on your machine. Reading from files is enough.
7. Optional: send new spelling errors to your Spelling Engine log.

---

## Milestones

### Milestone 1 — Understand the problem (3 hours)

1. **Interview yourself.** Do two copywork diffs by hand today. Time them. While doing them, write down every decision you make: *How do I decide this is a spelling error and not a different word? What do I do when I skipped a whole sentence? What counts as one difference?* These decisions are your hidden requirements.
2. **Look at existing tools** for 30 minutes: `diff` and `diff -y` on two text files; `git diff --word-diff`; `wdiff` (if installed); any online "text compare" site. For each, note one thing it does well and one thing it gets wrong for copywork.
3. **Write user stories**, at least six, in the form: *"As a copywork student, I want __ so that __."* Example: *"As a copywork student, I want spelling errors counted separately from word changes, so that I can see my spelling improve over time."*

**Done when:** timed hand diffs, tool notes, and 6+ user stories.

### Milestone 2 — Write v1 (5 hours)

Use the [Design Doc Template](<../../../../04 - System/Design Doc Template.md>). Required content:

- **Summary** (3–5 sentences).
- **Goals** — testable. For example: *"For a 100-word passage, Copydiff produces its output in under 1 second."* *"On my 10 hand-diffed passages, Copydiff's spelling-error count matches mine within ±1 for at least 8."*
- **Non-goals** — at least three (e.g. no GUI, no grammar checking, no other languages).
- **Background** — define *diff*, *token* (one unit of text, like a word or punctuation mark), and any other term you use.
- **Design:**
  - a diagram of the pipeline (e.g. *read files → split into tokens → align → classify differences → print and count*);
  - the **output format**, with a real example from one of your copywork passages;
  - how you'll decide "spelling error vs different word" (this is the hardest design question; propose something and explain it);
  - what happens with empty input, very different texts, or a missing file.
- **Alternatives** — at least two trade-off tables. Suggestions:
  1. Compare **letters**, **words**, or **sentences** first?
  2. **Spelling vs different word:** count letter differences? check against a dictionary? compare word length? something else?
  3. Output for the **terminal** (colours, symbols) vs an **HTML file** you open in a browser.
- **Testing plan** — at least 8 test cases, including: identical texts; one missing word; one extra word; one misspelling; one swapped word; a missing sentence; punctuation only; empty rebuild.
- **Risks and open questions** — at least three. (One honest one: *"I don't yet know an algorithm for lining up two texts. I expect to learn one in Module 05."* That is a perfectly good risk to write down.)

**Length:** 3–5 pages.

**Done when:** v1 is complete, has had a two-day cooling-off [D], and has been self-reviewed with the E08 checklist.

### Milestone 3 — Review (3 hours + waiting)

Get **one** review, in this order of preference:
1. a person who programs (study partner, friend, online community — many programming communities welcome design-doc feedback requests);
2. a person who doesn't program (they'll find unclear writing, which is still valuable);
3. a self-review after a 3-day cooling-off, *reading as a stranger*, plus an AI review of the finished draft (see the README's rules: comments are questions, not orders).

**Ask specific questions** (E10 Part 6): *"Is the output format clear from the example? Is my spelling-vs-word rule convincing? Which alternative would you have chosen?"*

Record every comment in `review-notes.md`. For each: **accept**, **clarify**, or **decline with a reason**.

**Done when:** at least 8 comments recorded and each one decided.

### Milestone 4 — Write v2 and the change log (3 hours)

Revise to v2. Then write `changes.md`:
- every significant change from v1 to v2, and **why** (link to the review comment that caused it);
- what you learned about writing design docs, in three sentences.

**Freeze v2.** When you reach Module 05, build from it, and fill in section 8 ("After the build") honestly. Then compare your design with the Module 05 spec. Where they differ, neither is automatically right; write down which you'd choose now and why.

**Done when:** v2 and `changes.md` complete.

**Checkpoint:** [Milestone Checkpoint](<../../../../04 - System/Milestone Checkpoint Template.md>). Feynman target: explain your design out loud in 2 minutes with your diagram, as if in a design review meeting. Why-ladder target: the decision you changed most because of review.

---

## Common pitfalls

- **Designing the code instead of the system.** Don't list function names. Describe parts, data, and flow.
- **Untestable goals.** "Accurate" and "fast" are not goals until they have numbers.
- **Fake alternatives.** If you list "Option B: do it badly," you haven't considered alternatives. Each option should be something a reasonable person might choose.
- **Hiding uncertainty.** You don't yet know the algorithms; say so. Reviewers trust honest docs.
- **Defending during review.** Write the comment down. Decide tomorrow.

## Communication deliverable

In `~/workbench/05-copydiff/docs/`: `design-v1.md`, `review-notes.md`, `design-v2.md`, `changes.md`, plus the Milestone 1 notes (`problem-notes.md`).

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Write the eight design-doc sections and their jobs from memory before starting v1 |
| **W** | Every alternative table; the accept/clarify/decline decisions |
| **S** | Template headings first, content second |
| **F** | The 2-minute spoken design review |
| **D** | Cooling-off before self-review and between review and revision |
| **T** | The review itself |

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Problem understanding | Hand-diff decisions captured; 6+ user stories | Some stories | None |
| Goals | All testable, with numbers | Mostly testable | Vague |
| Design clarity | Diagram, real output example, edge cases | Diagram and some examples | Prose only |
| Alternatives | 2+ honest tables with decisions and triggers | One table | None or straw men |
| Testing plan | 8+ cases including failures | Some cases | "Test it" |
| Review cycle | 8+ comments, each decided, v2 reflects them | Some comments | No review |
| Writing | Clear, revised, skim test passes | Mostly clear | Hard to follow |

**Done when:** all areas at least 2, and Goals, Alternatives, and Review cycle at 3.

## Connections

- **Back:** all of E08–E10; your months of copywork (you are the user).
- **Forward:** [Module 05 Copydiff](../../../../05-data-structures-and-algorithms/projects/copydiff/spec.md), where you build it; every later design doc uses this process.
