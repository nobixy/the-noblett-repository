# How I Will Study: The Deep Learner's Manifesto
*Last revised: 2026-09-25 (Next scheduled revision: 2027-03-25)*

> [!QUOTE]
> "Don't let note-taking become the hobby. Notes exist to support retrieval, synthesis, and building."

---

## 1. Core Cognitive Learning Principles

### A. Retrieval Practice (Testing Effect)
- Reading and highlighting create an **illusion of competence**. They feel fluent because the material is in front of the eyes, not because it is stored in long-term memory.
- The only reliable way to cement understanding is active retrieval: close the book, shut the notes, and recall or explain the concept from scratch.
- Use the **Spaced Blank-Sheet Retrieval Protocol** after every study block: 15 minutes of zero-hint memory dump (`[[08 - Templates/Blank-Sheet Retrieval Template.md]]`).

### B. The Feynman Technique (Radical Simplicity)
- Strip all jargon. If an idea cannot be explained in simple words and physical analogies to a 12-year-old, the underlying concept is not understood.
- Isolate friction points where you hesitate; those are your true knowledge gaps (`[[08 - Templates/Feynman Technique Note Template.md]]`).

### C. Elaborative Interrogation (The "Why?" Reflex)
- Never accept a formula, algebraic step, or grammatical rule passively.
- Constantly interrogate: *"Why does this step follow from the previous one?", "What breaks if this assumption is dropped?"*

### D. Subgoal Labeling & Worked Examples
- Label the conceptual milestones inside worked math derivations and code architectures before attempting unassisted problem sets.

### E. Spacing & Interleaving (Desirable Difficulties)
- Cramming produces zero durable storage strength. Space repetitions over days, weeks, and months.
- Interleave problem types (never drill 50 identical problems in a row); force the brain to practice *selecting the correct tool*.

### F. Benjamin Franklin Copywork (For Writing & Grammar)
- Master English prose by analyzing master passages, outlining them, putting them aside for 3 days, and reconstructing the prose from memory (`[[08 - Templates/Franklin Copywork Template.md]]`).

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
| **Sunday (2 hrs)** | Review & planning | Problem set wrap-up, weekly review in [[log.md]], writing, planning next week's schedule. |

---

## 3. How to Grade Myself Without a TA

1. **Autograders & Test Suites:** `make grade` in MIT 6.1810, Gradescope for CMU 15-445, full test suites in CS144, BusTub, clox, Monkey, and MIT 6.5840. Tests must pass cleanly.
2. **Timed, Closed-Book Past Exams:** Sit MIT OCW, Berkeley HKN, and CMU exams under strict real conditions without notes. Passing threshold is objective signal.
3. **Formal Write-ups:** If the solution or proof write-up is vague, the understanding is vague.
4. **Strangers' Code Review:** Open PRs and contribute to open source.
5. **The Feynman Technique / Teaching:** Write clear technical blog posts explaining the hardest concept in each block.

---

## 4. Revision History

| Date | Phase / Block Reached | Major Adjustments Made |
| :--- | :--- | :--- |
| 2026-09-25 | Phase -1 (Bedrock Setup) | Added the 8 core cognitive study systems (Feynman, Franklin, Blank-Sheet, Elaborative Interrogation) and Bedrock Math/English. |
