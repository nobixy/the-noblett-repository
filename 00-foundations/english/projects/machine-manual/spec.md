---
title: "Project: Machine Manual"
id: "FND-EN-PRJ-machine-manual"
type: "project"
module: "00-foundations"
track: "english"
phase: "A"
order: 110
prerequisites: [E03]
stages: "E04–E06"
artifact: "A tested user manual for a real household machine, plus a beginner's manual for five terminal commands"
deliverable: "The manuals themselves + usability-test log"
---

# Project: Machine Manual

| | |
| :-- | :-- |
| **You build** | A user manual for a real machine in your home, tested by a real person; then a beginner's manual for five Linux terminal commands |
| **Deliverable** | Both manuals (Markdown) and a usability-test log |

---

## Why this matters

Writing about a physical machine forces precision. You can't wave your hands: either the person can make coffee with your instructions, or they can't. This is the simplest possible version of every technical document you'll write later: name the parts, describe what they do, give steps, handle problems.

Using simple sentences is not a limitation here; it's the goal. The best manuals in the world (the kind that come with good tools and appliances) are written in short, simple, exact sentences. You are practising exactly the sentence skills of E04–E06 on a real task.

Then you do it again for terminal commands, which is your first piece of real software documentation.

**Real-world analogs:** product manuals, man pages, quick-start guides, the "Getting Started" page of every software project.

---

## Choose your machine

Pick a machine in your home that has **at least 4 parts you can name** and **at least 3 different tasks**. Good choices:

- coffee maker or espresso machine
- washing machine
- microwave or oven
- bicycle (gears, brakes, tyre pressure)
- printer
- home router (lights, reset, connecting a device)
- power drill
- a game console and controller

Avoid anything dangerous to test on someone else (no mains electrical work, no gas).

---

## Milestones

### Milestone 1 — Inventory (E04)

**Do:**
1. **Draw or photograph** the machine. Label every part you will mention. (Paper and a phone photo are fine.)
2. **Parts list (nouns):** each part with a one-line description. Use a determiner and a noun, then what it does.
   > **The water tank** holds up to 1.2 litres of water.
   > **The power button** turns the machine on and off.
3. **Actions list (verbs):** every action a user performs (*fill, press, turn, wait, remove, clean*) and every action the machine performs (*heats, beeps, blinks, pumps*).
4. **States list (adjectives):** the states the machine or its parts can be in (*on, off, empty, full, hot, blinking, locked*).

**Done when:** at least 6 parts, 10 actions, and 5 states, every word spelled correctly (check your list against a dictionary *after* writing it; log errors in your spelling log).

**[W]:** Why does a manual name the parts *before* the steps? What would happen if it didn't?

### Milestone 2 — Description and procedures (E05)

**Do:**
1. **"How it works"** (5–8 simple sentences, present tense): what the machine does, from the user's first action to the result. Use Pattern 1–3 sentences (E05). Mark the subject and verb of each sentence on a printout or in a copy.
2. **Three procedures**, one per task (e.g. *make one cup of coffee*, *descale the machine*, *empty the drip tray*). Each:
   - a title that names the task;
   - "You need:" (what to have ready);
   - numbered steps, each **one imperative sentence** (E05 Part 6);
   - "Result:" one sentence saying what the user should see when done.

**Done when:** every sentence is complete (no fragments except labels like "You need:"), every verb agrees with its subject, and the tense is consistent.

### Milestone 3 — Troubleshooting, punctuation, and the usability test (E06)

**Do:**
1. **Troubleshooting table:**

   | Problem | Likely cause | What to do |
   | :-- | :-- | :-- |
   | The light blinks red. | The water tank is empty. | Fill the tank to the MAX line. |

   At least 4 rows. Each cell in full sentences.
2. **Format** the manual in Markdown: a title, headings for each section, numbered lists for steps, bold for button names, a table for troubleshooting.
3. **Punctuation pass:** check every comma with the E06 subgoal checklist. Check every apostrophe.
4. **Usability test:** give the manual to someone who has never used the machine (or has used it least). Ask them to do one procedure using **only** the manual. **Watch in silence.** Do not help. Write down:
   - every hesitation (they stop, re-read, or look confused);
   - every question they ask (answer only "What does the manual say?");
   - every mistake.
5. **Revise** to fix each problem. If possible, test again with a second person.

**Done when:** a person completed one procedure with **zero questions** (after at most two revisions), and the usability-test log is written.

**Checkpoint:** [Milestone Checkpoint](<../../../../04 - System/Milestone Checkpoint Template.md>). Why-ladder target: *the most surprising problem your tester had. Why didn't you see it while writing?* (Hint: you know the machine too well. This is called the "curse of knowledge," and it is the main enemy of all technical writing.)

### Milestone 4 — The terminal manual (E06, end)

Write a beginner's manual for five commands: **`pwd`, `ls`, `cd`, `cp`, `mkdir`** (or swap in `mv`, `rm`, `cat`, `grep` if you know them).

For each command:
1. **What it does** — one sentence, present tense.
2. **Form:** `command [options] arguments`, in code format.
3. **Two examples:** the exact command (code format) and what you see (code format, copied from your real terminal).
4. **One warning** where relevant (e.g. "`cp` overwrites the target file without asking. Use `cp -i` to be asked first.").

Then one **procedure** that uses all five: e.g. *"Make a folder for your notes and copy a file into it."*

**Usability test:** a person who has never used a terminal follows your procedure. Same rules: watch silently, log, revise.

**Done when:** your tester completes the procedure with zero questions, and every command example is copied from a real run.

---

## Common pitfalls

- **Writing for yourself.** You know where the button is. Your reader doesn't. Name it and say where it is.
- **Two actions in one step.** "Fill the tank and press the button" will be done in the wrong order by someone, eventually.
- **Conditions at the end.** "Press the red button if the light is green" — they've already pressed it. Put conditions first: "If the light is green, press the red button."
- **Helping during the test.** Every time you help, you hide a bug in your manual.
- **Fixing the reader instead of the manual.** If they misunderstood, the manual was unclear. Always.

## Communication deliverable

The manuals *are* the deliverable:
- `machine-manual.md` (with the diagram or photo)
- `terminal-manual.md`
- `usability-log.md`: for each test, the tester (first name or "Tester A"), the procedure, every hesitation, question, and mistake, and the change you made for each.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Before Milestone 2, write the parts list from memory (no machine in front of you), then check it |
| **W** | Why parts before steps; why conditions first; the curse-of-knowledge question |
| **S** | Each procedure is a set of subgoals; the step structure is a template you will reuse for the rest of the curriculum and beyond |
| **C** | During this project, choose copywork passages from a well-written manual (e.g. a good appliance manual's first page, or the "DESCRIPTION" of `man cp`) |
| **T** | The usability test is teach-back with a strict pass/fail |

## Stretch goals

- **Quick-start card:** a half-page version for the fridge door: only the most common task and the top two problems.
- **Translate one procedure into a flowchart** (decision diamonds for "Is the light red?").
- **Contribute:** find a beginner tutorial for a command-line tool online with an unclear step. Suggest a fix (many tutorials and project docs welcome small edits).

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Parts and diagram | Every part labelled and used consistently | Most parts labelled | Parts unnamed or inconsistent |
| Sentences | All complete, agree, consistent tense; imperative steps | A few errors | Many fragments or tense jumps |
| Punctuation | Clean after checklist pass | A few errors | Not checked |
| Usability | Zero questions on final test, log complete | One or two questions remain | No test done |
| Terminal manual | Real outputs, warnings, tested | Complete, untested | Missing |

**Done when:** all areas at least 2, Usability at 3.

## Connections

- **Back:** E04 (nouns, verbs, adjectives), E05 (sentence core, imperatives), E06 (punctuation, code formatting).
- **Forward:** E09's instructions and READMEs; every README you write for every project; [01 Lab 00](../../../../01-intro-cs-taste/labs/lab-00-machine-setup.md) uses the same commands you documented here.
