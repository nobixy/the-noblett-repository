---
title: "Study Protocols"
type: hub
tags: [hub, study-methods]
---

# Study Protocols

This page turns the methods in [how-i-study.md](how-i-study.md) into short, exact routines. Every module, project and lab in this repository uses these routines by their letter code. When a spec says **[R]**, it means "do the R protocol below, now."

You do not need to read the research to use them. The deep dives are in `02 - Atlas/` (LM01–LM16) if you want the why.

> **The one rule behind all of them:** learning happens when you *pull* an idea out of your own head, not when you push it in by reading. Every protocol below is a different way to pull.

---

## Quick card

| Code | Name | Time | When | Where it comes from |
| :-- | :-- | :-- | :-- | :-- |
| **R** | Blank-sheet retrieval | 10–15 min | End of every study session and every project milestone | how-i-study §1A · [LM02](<02 - Atlas/LM02 - Retrieval Practice.md>) |
| **F** | Feynman pass | 15–20 min | When you finish a concept or a component | how-i-study §1B · [LM01](<02 - Atlas/LM01 - Feynman Technique.md>) |
| **W** | Why-ladder | 5–10 min | Every rule, formula, or design choice | how-i-study §1C · [LM03](<02 - Atlas/LM03 - Elaborative Interrogation.md>) |
| **S** | Subgoal labels | 10–20 min | Before you solve problems alone, and before you code a hard part | how-i-study §1D · [LM10](<02 - Atlas/LM10 - Worked Examples and Subgoal Labeling.md>) |
| **I** | Interleave and space | built in | Practice sets and review | how-i-study §1E · [LM05](<02 - Atlas/LM05 - Interleaving.md>), [LM09](<02 - Atlas/LM09 - Spacing and Spaced Repetition.md>) |
| **C** | Franklin copywork | 20–30 min | English, every weekday; later, technical prose | how-i-study §1F · [LM06](<02 - Atlas/LM06 - Franklin Copywork.md>) |
| **D** | Diffuse break | 10–30 min | When you are stuck after real effort | how-i-study §1G · [LM11](<02 - Atlas/LM11 - Focused and Diffuse Thinking.md>) |
| **T** | Teach-back and write-up | varies | End of every project; some milestones | how-i-study §3 (items 3 and 5) |
| **V** | Watch actively | video length + 10 min | Any video lesson or online course | how-i-study §1A (illusion of competence) · [LM08](<02 - Atlas/LM08 - Chunking and the Illusion of Competence.md>) |

A **Milestone Checkpoint** is R + F + W together, about 30 minutes. Every project milestone in this repository ends with one. Use the [Milestone Checkpoint Template](<04 - System/Milestone Checkpoint Template.md>).

---

## R — Blank-sheet retrieval

**Goal:** find out what you actually know, without help.

1. Close the book, the spec, the code, and every browser tab.
2. Set a timer for 10 minutes (15 after a long session).
3. On a blank page, write everything you remember. Use words, lists, sketches, code fragments, formulas, examples. Spelling does not matter here; speed does.
4. When you run dry, wait one full minute. More will come.
5. Now open the source. In a different colour, mark what you missed and what you got wrong.
6. Turn each miss into one flashcard (one fact per card). Put it in your review deck.

**Prompt starters, if the page stays blank:**
- What were the main parts? Draw them as boxes.
- What is one example? What is one thing that is *not* an example?
- What went wrong today, and why?
- If I had to do this again tomorrow with no notes, what would I do first?

**Rules:** never skip step 5 (checking is where the learning locks in). Never reread instead of recalling. A bad recall is still worth more than a good reread.

Template: [Blank-Sheet Retrieval Template](<04 - System/Blank-Sheet Retrieval Template.md>).

---

## F — Feynman pass

**Goal:** find the exact spot where your understanding breaks.

1. Name the idea at the top of a page (e.g. "Why we carry in addition", "What a socket is").
2. Explain it in plain words, as if to a smart friend who has never studied it. No jargon. If you must use a technical word, define it in the same sentence.
3. Give one concrete example and one everyday analogy.
4. Mark every place you hesitated, waved your hands, or used a word you could not define. These are your **gaps**.
5. Go back to the source for only those gaps. Fix them.
6. Rewrite the explanation shorter. End with one sentence that holds the whole idea.

**Spoken version (recommended once a week):** record yourself explaining it out loud for 2–3 minutes on your phone. Play it back. Every "um, basically, kind of" is a gap. Speaking is half of technical communication, and this is free practice.

Template: [Feynman Technique Note Template](<04 - System/Feynman Technique Note Template.md>).

---

## W — Why-ladder

**Goal:** never accept a rule you cannot justify.

For any rule, step, or design decision, ask "why?" and answer in one sentence. Then ask "why?" about your answer. Go three rungs down.

> **Rule:** "To add fractions, you need a common denominator."
> 1. *Why?* Because the bottom number tells you the size of the pieces, and you can only count pieces of the same size together.
> 2. *Why can you only count same-size pieces?* Because "2 of these plus 3 of those" is not 5 of anything unless "these" and "those" are the same unit.
> 3. *Why does a common denominator make them the same?* Because multiplying top and bottom by the same number cuts every piece into equal smaller pieces without changing the amount.

**For design decisions, use the contrast form:** "Why did I choose A instead of B? What would break, or get worse, if I chose B?" Every project spec lists some of these. Answer them in your design doc.

**When the ladder breaks** (you cannot answer a rung), that is a gap. Write it down and look it up. That is the method working, not failing.

---

## S — Subgoal labels

**Goal:** see the *structure* of a solution, not just its steps.

1. Take a worked example (from the module, a book, or your own past solution).
2. Group its steps into chunks. Give each chunk a short label that says *what it achieves*, not what it does: "Get both fractions into the same unit," not "multiply by 3."
3. Cover the example. Using only your labels, solve a new problem of the same kind.
4. Keep your list of labels. For each problem type, the list of labels *is* the method. Put it on a flashcard.

**In code:** before writing a hard function, write the subgoal labels as comments first. Then fill in code under each comment. Example:

```python
# 1. Read the packet header and check it is complete
# 2. Decide if this packet is new, a duplicate, or out of order
# 3. Store it or drop it
# 4. Build the acknowledgment to send back
```

---

## I — Interleave and space

**Interleaving (mixing):** never do 20 problems of one type in a row. Each module's practice sets are already mixed. When you make your own, take 3–4 problem types and shuffle them. The hard part, *choosing which method to use*, is the skill that tests and real projects need.

**Spacing (reviewing over time):** review each new thing on this schedule after you first learn it:

| Review | 1 | 2 | 3 | 4 | 5 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Days after learning | 1 | 3 | 7 | 21 | 60 |

You do not need to track this by hand. Put cards in a flashcard tool (Anki, or the Study Deck you build in Module 02) and it will schedule them. Until then, a paper Leitner box works: five envelopes, move a card right when you get it right, back to box 1 when you get it wrong.

**Daily review budget:** 10–20 minutes. If the pile grows past 20 minutes, add fewer new cards for a week. Do not skip reviews to "catch up later."

**Cumulative review in every module:** each module's practice includes problems from earlier modules on purpose. Do not skip them as "old stuff."

---

## C — Franklin copywork

**Goal:** learn good sentences by rebuilding them from memory.

This is how Benjamin Franklin learned to write. It works because you compare your own sentences to a skilled writer's, word by word.

1. **Pick** a short passage (3–8 sentences) from the current copywork level (see [English overview](00-foundations/english/overview.md#copywork-ladder)).
2. **Copy** it by hand once, slowly. Notice each spelling and each comma.
3. **Hint notes:** for each sentence, write 2–5 words that remind you of its meaning. Not its wording.
4. **Hide** the original. Wait. (Franklin waited days. Start with the next day; build to 3 days.)
5. **Rebuild** the passage from your hints only.
6. **Diff:** put yours next to the original. Mark every difference: spelling, word choice, order, punctuation, length.
7. **Log** one lesson in one sentence: "The writer put the main point first; I buried it."

**Fast version (10 min, for busy days):** copy one sentence, hide it, rewrite it from memory 5 minutes later, diff.

Template: [Franklin Copywork Template](<04 - System/Franklin Copywork Template.md>). In Module 05 you build a tool that does the diff for you.

---

## D — Diffuse break

**Goal:** get unstuck without quitting and without banging your head for hours.

1. Work on the problem with full focus for at least 25 minutes.
2. If you are still stuck, write a **stuck note** (3 lines): what I am trying to do · what I tried · what I think is wrong.
3. Leave. Walk, shower, wash dishes, sleep. No phone, no other study.
4. Come back and reread only the stuck note. Try again.
5. If still stuck after two rounds, change the size of the problem: build a smaller version, print more, draw it, or ask someone.

**Stuck rule for projects:** never stay stuck on one bug for more than 90 minutes in one sitting. The stuck note is how you hand the problem to tomorrow's brain.

The stuck notes go in your daily log. They are useful later: they show you which kinds of problems trip you up.

---

## T — Teach-back and write-up

**Goal:** prove your understanding by producing something another person can use.

Every project ends with a communication deliverable. These are graded as part of the project. A project is **not done** until its deliverable is done. The forms you will use:

| Deliverable | What it is | Length | Template |
| :-- | :-- | :-- | :-- |
| **Design doc** | What you will build, how, and why; written *before* the main build and updated after | 1–6 pages | [Design Doc Template](<04 - System/Design Doc Template.md>) |
| **Lab report** | What you measured, how, what you found, what it means | 1–4 pages | [Lab Report Template](<04 - System/Lab Report Template.md>) |
| **Demo script** | A 3–8 minute spoken walk-through of a working build, recorded | 1–2 pages of script | [Demo Script Template](<04 - System/Demo Script Template.md>) |
| **Explainer** | A blog-style explanation of the hardest idea in the project for a beginner | 600–1,500 words | (none; use the Feynman pass as a draft) |
| **README** | How to build, run and test the project | 1 page | (see Module 02 lab) |

**Teach-back:** once a month, explain something to a real person (a friend, a partner, an online study group). Their questions are better than any test.

**Writing grows with you:** in the first months the deliverables are short and simple (a half-page with five clear sentences is a real achievement). The English stages tell you which deliverable sizes fit where you are. Do the deliverable at your current level; do not skip it because your writing is not "good enough" yet. Writing these *is* how it gets good.

---

## V — Watch actively

**Goal:** learn from videos and online courses without falling into the "I watched it, so I know it" trap.

Watching a clear explainer feels like learning, just like rereading does. Most of that feeling is the illusion of competence. These steps turn a video into practice:

1. **Before (1 min):** write the video's title and one question you hope it answers.
2. **During:** watch at normal speed. **Pause at least every 5 minutes** and predict what comes next, or do the example yourself before the presenter does. Keep the notes short (key words and sketches, not transcripts).
3. **After (10 min):** close the video and do a blank-sheet recall [R] of what it said. Then do **3–5 practice problems** or write a short paragraph using the idea. A video with no practice afterwards counts as entertainment, not study.
4. **Rule of thumb:** at most **1 minute of video for every 2 minutes of doing** in a study session. Courses (Coursera, Khan, edX) count toward your hours only for the parts where you answer questions, write, or code.

All the videos and courses mapped to each stage and module are in [courses-and-videos.md](courses-and-videos.md).

---

## The session loop

Every study session, in any module, has the same shape:

1. **Warm-up recall (5 min):** without notes, write what you did last session and what is next.
2. **Focused work (25–90 min):** one thing. Phone in another room.
3. **Retrieval [R] (10 min):** blank sheet on what you just did.
4. **Log (2 min):** today's journal entry: did, stuck, next.

Every project milestone adds a **Milestone Checkpoint** (R + F + W, 30 min).
Every week ends with the **Weekly Review** (Sunday, 30–60 min): run your flashcard reviews, re-do one old problem from each active module cold, and pick next week's targets. Template: [Weekly Review Template](<04 - System/Weekly Review Template.md>).

---

## Honest notes on the evidence

- Retrieval practice, spacing, and worked examples with subgoals have strong evidence.
- Elaborative interrogation and interleaving have good evidence, with limits.
- Feynman and Franklin copywork are practitioner methods. They are built on the strong effects above (retrieval, feedback, comparison), but have not been tested directly as named techniques.
- "Learning styles" (visual learner, etc.) are a myth. Everyone benefits from words plus pictures. See [Learning Styles Myth](<02 - Atlas/Learning Styles Myth.md>).

Watch what works for you. If a protocol is not paying off after a fair trial (four weeks), change it and write down why in a [Decision Record](<04 - System/Decision Record.md>).
