---
title: "E10 — Argument and Design Documents"
id: "E10"
type: "lesson"
module: "00-foundations"
track: "english"
stage: "E10"
phase: "C"
order: 680
prerequisites: [E09]
---

# E10 — Argument and Design Documents

**In this stage you will:** learn to make a case: state a claim, support it with reasons and evidence, deal honestly with the other side, and compare options with a trade-off table. You will write a full design document, get it reviewed, and revise it. You will also learn the lab report and the recorded demo, the other two deliverables used in every later project. Project: [First Design Doc](projects/first-design-doc/spec.md).

**Before you start:** E09 done. You can describe a system and write instructions that pass a usability test.

---

## Why this matters

Descriptions and instructions explain what *is*. Engineering is mostly about what *should be*: which design to build, which bug to fix first, which tool to use, why this approach and not that one. Those are **arguments**. Not fights — reasoned cases for a choice.

A **design document** is an argument for a plan: "*Here is the problem. Here are the options. Here is what I propose, and why.*" Writing one before you build:
- forces you to find the holes in your plan while they are cheap to fix;
- lets other people improve your plan before you spend many sessions on it;
- leaves a record of *why* things are the way they are (the most-asked question in any codebase).

From here on, every major project in this curriculum starts with a design doc.

---

## Part 1 — The shape of an argument

**Claim → Reasons → Evidence → Other side → Response → Conclusion**

| Part | What it is | Example |
| :-- | :-- | :-- |
| **Claim** | What you want the reader to accept | *My flashcard app should store cards in plain text files, not a database.* |
| **Reasons** | Why the claim is true (2–3) | *Plain text is easy to edit by hand, works with git, and needs no extra software.* |
| **Evidence** | Facts, measurements, examples that support each reason | *I edit my cards in Vim every day. A 2,000-card text file loads in 40 ms in my test.* |
| **Other side** | The best objection to your claim, stated fairly | *A database would make searching faster and prevent two programs from corrupting the file.* |
| **Response** | Why your claim still holds, or how you adjust it | *With fewer than 10,000 cards, search is fast enough in text. Only one program writes the file. If either changes, I will switch to SQLite.* |
| **Conclusion** | The claim again, now earned | *Plain text is the right choice for now.* |

**Rules:**
- **State the claim early.** Readers should know what you're arguing for in the first paragraph. Mystery is for novels.
- **Evidence beats opinion.** "*It's faster*" is opinion. "*It loads in 40 ms instead of 900 ms*" is evidence. Measure when you can.
- **State the other side at its strongest.** If you only argue against a weak version of the objection, a smart reader stops trusting you. Stating the strong version and still winning is very persuasive. And sometimes you discover you were wrong, which is the most valuable outcome of all.
- **Separate facts from guesses.** "*I measured…*" vs "*I expect…*". Both are allowed. Mixing them up is not.

---

## Part 2 — Trade-offs

Almost every engineering choice is a trade-off: gaining something costs something else. Strong engineering writing makes the trade-off explicit.

**The trade-off table:**

| Criterion | Option A: text files | Option B: SQLite database |
| :-- | :-- | :-- |
| Edit by hand | ✅ any editor | ❌ needs a tool |
| Works with git | ✅ readable diffs | ⚠️ binary file, no useful diffs |
| Search speed at 10k cards | ⚠️ ~200 ms (estimated) | ✅ < 5 ms |
| Safe with two writers | ❌ can corrupt | ✅ built in |
| Extra dependencies | ✅ none | ✅ in Python's standard library |
| **Decision** | **Chosen** | Revisit if cards > 10k or a second writer appears |

**Rules:**
- Pick criteria that **matter for this project**, and say why they matter.
- Fill every cell honestly, including the cells that hurt your favourite option.
- End with a **decision and a trigger**: what would make you change your mind. This shows you understand the trade-off, not just the answer.

This table is the written form of the why-ladder's contrast question [W]: "*Why A instead of B? What would break with B?*"

---

## Part 3 — Writing for the reader

Two ideas from writing teachers who work with scientists and engineers (notably Larry McEnerney at the University of Chicago):

1. **Readers don't read to learn what you think. They read to solve their own problem.** Start from *their* problem, not your work. "*Studying from flashcards fails when you can't edit cards fast*" beats "*I built a flashcard app.*"
2. **Value comes from changing what the reader believes or does.** Ask: after reading this, what will my reader do differently? If the answer is "nothing," the document has no job.

**Practical habits:**
- **Name your reader** before writing (a beginner? a teammate who knows Python? future you?). Write it at the top of your draft, then delete it later.
- **Put the conclusion first** in anything a busy person will read. Engineers call this BLUF: *bottom line up front*.
- **Show, don't just tell:** include one concrete example of each important idea (a real input and output, a real packet, a real error).

---

## Part 4 — The design document

Use the [Design Doc Template](<../../04 - System/Design Doc Template.md>). Its sections, and what each one must do:

| Section | Job | Common mistake |
| :-- | :-- | :-- |
| **1. Summary** | A reader who stops here knows what and why | Writing history instead of the point |
| **2. Goals and non-goals** | Testable goals; non-goals prevent scope creep | Goals that can't be tested ("fast", "easy") |
| **3. Background** | Just enough context and definitions | A textbook chapter |
| **4. Design** | Diagram, data formats with real examples, the main flow, error handling | No examples; describing code line by line |
| **5. Alternatives** | At least two choices with trade-off tables | Only straw-man alternatives |
| **6. Testing plan** | How you'll know it works, including failure cases | "I'll test it" |
| **7. Risks and open questions** | What you're unsure about | Pretending there are none |
| **8. After the build** | What changed and why | Skipping it |

**Goals must be testable.** Compare:
- ✗ *The app should be fast.*
- ✓ *The app shows the next card within 100 ms on my laptop with 5,000 cards.*
- ✗ *Easy to use.*
- ✓ *A new user can add and review their first card in under 2 minutes without reading the docs.*

**Write v1 before building**, even if it's short and partly wrong. Then build. Then update the doc in section 8. The difference between v1 and the final version is a map of what you learned.

---

## Part 5 — Lab reports and demos

Two more deliverable forms you will use in every module from now on.

### The lab report

Use the [Lab Report Template](<../../04 - System/Lab Report Template.md>). A lab report answers **one question** with **evidence**: *Question → Prediction (with a reason) → Setup → Results → Analysis → Sources of error → Conclusion.*

- **Predictions** are written *before* measuring, with a reason. Being wrong is fine and often the most interesting outcome. Having no reason is not fine.
- **Results** come before analysis. First say what the data shows; then say why.
- **Every number has a unit**; every plot has labelled axes.
- **Past tense** for what you did ("*I measured…*"); **present tense** for what the results show ("*The time grows linearly…*") — E05.

### The recorded demo

Use the [Demo Script Template](<../../04 - System/Demo Script Template.md>): *Hook → Show it working → How it works (one diagram, one flow) → Hardest part → Limits and next steps.* Keep it short.

**Delivery tips:**
- Write the script in short lines you can say in one breath. Read it aloud twice before recording.
- Show, then explain. Never explain at length before anything happens on screen.
- Prepare your terminal: large font, clean prompt, commands ready.
- One take is fine. Mistakes recovered calmly look professional.

---

## Part 6 — Reviews: giving and getting feedback

Professional engineering writing goes through **review**. You will practise both sides.

**Getting a review:**
1. Tell the reviewer what you want: "*Is the design clear? Did I miss an alternative?*" (not "*thoughts?*").
2. Don't defend while listening. Write everything down. Decide later.
3. For each comment: **accept** (change it), **clarify** (the reader misunderstood — so the writing needs fixing anyway), or **decline with a reason**.

**Giving a review** (to a study partner, or on someone's open-source docs):
1. Start with what works and why.
2. Point to the **specific** sentence or section.
3. Describe your *experience as a reader* ("*I got lost here; I didn't know what 'it' meant*") rather than issuing orders.
4. Separate **must-fix** (wrong, confusing) from **nice-to-have** (style).

**No reviewer available?** Use the cooling-off method: put the doc away until a later session (a few sessions later is better), then review it yourself as a stranger, with the checklist. Online communities (a study Discord, r/learnprogramming, a project's issue tracker) are also good places to ask for a doc review. An AI assistant can review a *finished* draft (see the README's rules); treat its comments as questions, not orders.

---

## Part 7 — Practice routine (5 sections)

| Section | Focus |
| :-- | :-- |
| 1 | Sessions 1–2: argument shape; write a 400-word argument on a technical choice you've made (Practice Set 1) · Sessions 3–4: trade-off tables (Practice Set 2) · Session 5: reader and BLUF |
| 2 | Sessions 1–5: First Design Doc Milestones 1–2 (draft v1) |
| 3 | Sessions 1–3: review cycle (Milestone 3) · Sessions 4–5: revise |
| 4 | Sessions 1–2: lab report on a small experiment (Practice Set 3) · Sessions 3–4: demo script and recording of a Module 01 project · Session 5: section recording |
| 5 | Sessions 1–4: track assessment (see the [English overview](overview.md#track-assessment)) · Session 5: write your "then vs now" note |

**Every session:**
- **Warm-up [R]:** from memory, write the argument shape or the design doc sections (alternate sessions).
- **Spelling** + **copywork [C]** at **Level 4** (RFC 768, Pike's notes, Go proposals, AOSA chapters). In the diff, notice how expert writers state a claim and handle objections.

**Study protocols:**
- **[W]** Every design choice gets a contrast why-ladder, written into section 5 of the design doc.
- **[S]** The design doc headings are the subgoal labels. Write all headings first; fill them in any order.
- **[F]** Before writing section 4, explain your design out loud, briefly, with a diagram. Where you hesitate is where the doc needs the most care.
- **[D]** Cooling-off until a later session before self-review.
- **[T]** The review cycle and the demo.

---

## Practice sets

### Practice Set 1 — Build an argument

Pick one real choice you made in Module 01 or 02 (a data format, a language, a library, an algorithm). Write a 300–500 word argument for it using all six parts. Then write the strongest objection you can, and decide honestly whether it beats your claim.

### Practice Set 2 — Trade-off tables (3 short ones)

Make a trade-off table (at least 4 criteria) and a decision with a trigger for each:
1. Paper notebook vs a notes app for your study log.
2. Python vs C for a program that converts 1,000 images.
3. Storing your flashcards in one big file vs one file per card.

### Practice Set 3 — A mini lab report

**Question:** *How long does it take your computer to count to ten million in Python?*
Write a prediction with a reason. Write a 3-line Python loop and time it with `time python3 count.py`. Run it 5 times. Report the results (all 5 runs and the average), analysis, sources of error, and conclusion, using the template. One page maximum.

---

## Watch, practise, and write

*Companions, not replacements: the lessons above come first. Video course for this track: [English resources](resources.md#video-course).*

- **Watch:** Google Technical Writing Two (free). *English Composition I* (Duke, Coursera) for argument. *Successful Presentation* (University of Colorado Boulder, Coursera) for demos.
- **Practise:** Review someone else's writing with the E10 review rules (an online community, a friend's email, a project's README).
- **Fun writes this stage** ([prompt bank](writing-prompts.md)): #82 tabs vs spaces (argue the other side) · #83 design doc for a time machine · #84 pizza trade-off table · #88 the steelman

---

## Self-check

1. **[R] Blank sheet:** the six parts of an argument; the rules for trade-off tables; McEnerney's two ideas; the eight design-doc sections and each one's job; the lab report sections; the demo shape; how to receive a review.
2. **Your design doc** has passed one review cycle and been revised.
3. **Your demo** is recorded and watched back, with three notes for improvement.
4. **Track assessment** completed (see the overview).

## Done when

- [ ] Practice Sets 1–3 done.
- [ ] [First Design Doc](projects/first-design-doc/spec.md) complete, reviewed, and revised.
- [ ] One lab report and one recorded demo done.
- [ ] Track assessment done and filed in your journal, with your E01 baseline numbers next to the new ones.

**After E10:** The English track becomes a short part of every English session: spelling review, copywork at Level 4, and the section recording. Every project's deliverable is now your main writing practice. Return to any stage's practice sets whenever your project writing shows a weak spot (your reviewers and your error log will tell you where).
