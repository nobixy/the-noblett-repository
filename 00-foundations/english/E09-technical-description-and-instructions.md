---
title: "E09 — Technical Description and Instructions"
id: "E09"
type: "lesson"
module: "00-foundations"
track: "english"
stage: "E09"
phase: "C"
order: 670
prerequisites: [E08]
---

# E09 — Technical Description and Instructions

**In this stage you will:** learn the four everyday forms of technical writing: **describing a system**, **writing instructions**, **reporting a bug**, and **writing a README**. You will also define terms precisely, write captions for diagrams, and give short spoken explanations with structure. Projects: [Bug Report Gauntlet](projects/bug-report-gauntlet/spec.md); continue [Explain-a-System](projects/explain-a-system/spec.md).

**Before you start:** E08 done. You can write a clear paragraph and revise it with the checklist.

---

## Why this matters

This stage is the job. These four forms are most of the writing a working engineer does:

| Form | Reader's question | Your goal |
| :-- | :-- | :-- |
| **Description** | "How does this work?" | The reader builds an accurate picture in their head |
| **Instructions** | "How do I do this?" | The reader succeeds without asking you anything |
| **Bug report** | "What's wrong, and how do I see it?" | The reader can reproduce the problem on their machine |
| **README** | "What is this, and how do I start?" | The reader is running it in five minutes |

Each form has a **reader** with a **task**. Good technical writing serves that task and nothing else. That's the whole secret.

---

## Part 1 — Precise words

Technical writing fails on vague words more than on bad grammar.

### Replace vague words with specific ones

| Vague | Specific |
| :-- | :-- |
| It doesn't work. | The program exits with the error `Segmentation fault` after I press Enter. |
| It's slow. | The page takes 8 seconds to load; it used to take 1 second. |
| Some files | 3 of the 40 files in `data/` |
| Recently | Since the update on October 3 |
| A big file | A 2.1 GB video file |
| The thing / the stuff | the config file / the log output |
| It crashes sometimes. | It crashes about 1 time in 10 when the Wi-Fi is off. |

**Rule:** if a reader could ask "how much?", "which one?", "when?", or "what exactly?", answer it in the sentence.

### Define terms on first use

The first time you use a technical term your reader might not know, define it in the same sentence or the next one.

> A **packet** is a small chunk of data, usually less than 1,500 bytes, sent across a network as one unit.

**A good definition has two parts:** the **category** (what kind of thing it is) and the **difference** (what makes it special within that category).
> A **router** (term) is a network device (category) that forwards packets between different networks (difference).
> A **compiler** is a program that translates source code into machine code before the program runs.

### Use one word for one thing

In fiction, writers vary words to avoid repetition. **In technical writing, don't.** If you call it "the server" in one sentence and "the host" in the next, a reader will think they are two different machines. Choose one name and use it every time. Define it once; use it consistently. (This is exactly like a variable name in code.)

### Use *must*, *should*, *may* precisely

Specifications use these words with exact meanings (formalised in the internet standard RFC 2119, which you'll meet in Module 09):
- **must** = required. No exceptions.
- **should** = recommended; there may be good reasons not to, but understand them first.
- **may** = optional.

---

## Part 2 — Describing a system

A description answers *how does this work?* Use this order:

1. **Purpose** (1–2 sentences): what the system does and why it exists.
2. **Parts** (a list or a diagram): the main components, each with a one-line job description.
3. **Connections:** how the parts talk to each other.
4. **Walk-through of one flow:** follow one thing (a key press, a packet, a request, a drop of water) through the system from start to end, step by step.
5. **Limits / edge cases:** what happens when something goes wrong.

**Example (short):**

> **How a home thermostat works**
>
> A thermostat keeps a room at a chosen temperature by switching the heater on and off.
>
> It has three parts: a **sensor** that measures the room's temperature, a **setpoint** (the temperature you choose), and a **switch** that turns the heater on or off.
>
> Every few seconds, the thermostat compares the sensor's reading with the setpoint. If the room is colder than the setpoint, it closes the switch, and the heater turns on. When the room warms past the setpoint, it opens the switch, and the heater turns off.
>
> To stop the heater from clicking on and off every few seconds, most thermostats wait until the temperature is about one degree past the setpoint before switching. This gap is called **hysteresis**.

Notice: purpose first; parts named once and then used consistently; a flow walk-through in time order; the edge case last, with a defined term.

### Diagrams and captions

A diagram with boxes and arrows is often worth a page of text. Rules:
- Every box has a **label** (a noun). Every arrow means **one** thing (data flows, or calls, or "is part of") — say which in the caption.
- Every diagram has a **caption**: one or two sentences telling the reader what to notice. "*Figure 1: A request travels from the browser (left) through the router to the server (right). The reply follows the same path back.*"
- Refer to the diagram from the text: "*As Figure 1 shows…*"

Tools: paper and a phone photo are fine. Excalidraw (excalidraw.com, free) is great for clean diagrams. Mermaid diagrams work inside Markdown.

---

## Part 3 — Writing instructions

Instructions answer *how do I do this?* The test of instructions is simple: **can a stranger follow them without asking you anything?**

**Structure:**
1. **Title** that says the task: "*Install the Nib emulator on Linux*" (not "*Installation*").
2. **What you'll end up with** (one sentence).
3. **Before you start** (prerequisites): what they need already installed, known, or prepared.
4. **Numbered steps.**
5. **Check it worked:** what they should see.
6. **Troubleshooting:** the two or three most likely problems and their fixes.

**Rules for steps:**
- **One action per step.** "Open the terminal and type the command and press Enter" is three steps, or one step with one command.
- **Start with an imperative verb** (E05): *Open, Type, Click, Wait, Check.*
- **Put conditions first:** "*If you use macOS, skip to step 6.*" — not "*Skip to step 6 if you use macOS*" (by the time they read the condition, they've already started the step).
- **Commands in code format, exactly as typed** (E06 Part 8).
- **Show the expected result** after any step where something visible happens: "*You should see `Python 3.12.4`.*"
- **Don't explain inside the steps.** If an explanation is needed, put it before the steps or in a short note after.

**Example:**

> **Check which version of Python you have**
>
> You'll find out whether Python is installed and which version you have.
>
> 1. Open a terminal.
> 2. Type `python3 --version` and press Enter.
>
>    You should see something like `Python 3.12.4`.
>
> **If you see `command not found`:** Python is not installed. Follow *Lab 00, Part 3* to install it.

### The usability test

The only real test of instructions: give them to someone who has never done the task, **watch silently**, and note every place they hesitate, ask a question, or make a mistake. Each one is a bug in your writing. Fix and repeat. (You did a version of this in the Machine Manual.)

---

## Part 4 — Bug reports

A bug report answers *what's wrong, and how can I see it myself?* A good report saves hours. A bad one ("it's broken lol") is often ignored.

**Structure:**

```
Title: [What goes wrong] when [what you did]
  e.g. "Program crashes when the input file is empty"

Environment:
  - OS and version (e.g. Arch Linux, kernel 6.11)
  - Program version (e.g. nib 0.3, commit a1b2c3d)
  - Anything else relevant (Python 3.12.4, 8 GB RAM)

Steps to reproduce:
  1. Create an empty file: `touch empty.txt`
  2. Run: `nib run empty.txt`

Expected result:
  The program prints "Error: input file is empty" and exits.

Actual result:
  The program crashes with:
    Traceback (most recent call last):
      ...
    IndexError: list index out of range

Frequency: every time (5 of 5 tries)

Notes (optional):
  - Started after commit a1b2c3d; commit 9f8e7d6 works.
  - Possible cause: line 42 reads lines[0] without checking the length.
```

**Rules:**
- **The title states the symptom and the trigger.** Someone scanning a list of 200 bug titles should understand yours.
- **Steps must be complete and minimal.** Complete: a stranger can follow them from scratch. Minimal: remove every step that isn't needed to trigger the bug. (Finding the minimal steps often reveals the cause. It's half of debugging.)
- **Expected vs actual** is the heart of the report. Never skip "expected": the reader may not know what's supposed to happen.
- **Copy error messages exactly**, in code format. Never paraphrase them; people search for exact text.
- **Facts first, guesses last**, and label guesses as guesses ("Possible cause:").
- **One bug per report.**

---

## Part 5 — The README

A README is the front door of a project. Every project you build from now on has one.

**Structure (in this order):**
1. **Name and one-sentence description.** "*Nib: an emulator for a tiny 8-bit computer, written in Python.*"
2. **What it does** (2–4 sentences, maybe a screenshot or sample output).
3. **Quick start:** install and run in as few steps as possible.
4. **Usage:** the main commands or options, with examples.
5. **How to run the tests.**
6. **How it works** (short; link to a design doc for detail).
7. **Status and limits:** what works, what doesn't yet.

**Test:** a stranger should get from "never heard of it" to "running it" in five minutes using only the README.

---

## Part 6 — Speaking with structure

Your section recordings continue. Add structure:

**The short explainer shape:**
1. **The point** (one sentence): "*A thermostat keeps a room at one temperature by switching a heater on and off.*"
2. **The map:** "*It has three parts, and I'll walk through one cycle.*"
3. **The walk-through:** follow one flow, with signposts (*first, then, when, finally*).
4. **The edge case:** "*There's one clever detail…*"
5. **The point again**, in different words.

Practise with a diagram on paper you can point at. Record. Listen back. Count fillers. Note one improvement.

---

## Part 7 — Practice routine (5 sections)

| Section | Focus |
| :-- | :-- |
| 1 | Sessions 1–2: precise words; rewrite 10 vague sentences from your journal · Session 3: definitions (write 10 for terms from Module 01–02) · Sessions 4–5: Practice Set 1 |
| 2 | Sessions 1–3: describing a system; write a description of your Module 01 Nib emulator with a diagram · Sessions 4–5: Explain-a-System explainer 2 |
| 3 | Sessions 1–2: instructions; write install instructions for one of your projects · Sessions 3–4: usability test with a real person · Session 5: revise |
| 4 | Sessions 1–5: Bug Report Gauntlet (Milestones 1–3) |
| 5 | Sessions 1–2: READMEs for two of your projects · Session 3: Explain-a-System explainer 3 · Session 4: section recording · Session 5: self-check |

**Every session:**
- **Warm-up [R]:** from memory, write the structure of one of the four forms (rotate each session).
- **Spelling** + **copywork [C]** at Level 3, moving to **Level 4** (RFC 768, Rob Pike) when ready. Diff for precision: where did the author use an exact word where you used a vague one?

**Study protocols:**
- **[S]** Each form's structure is a set of subgoal labels. Write them as headings *before* you write any content.
- **[W]** For each rule (e.g. "conditions first in steps"), ask what goes wrong without it. Find a real example in a manual or website that breaks the rule.
- **[F]** Your Explain-a-System pieces are Feynman passes made public.
- **[T]** The usability test and bug reproductions are teach-back with a hard pass/fail.
- **[I]** Rotate the forms; don't write four bug reports in one sitting.

---

## Practice sets

### Practice Set 1 — Precision (8 items)

Rewrite each vague sentence as a specific one. Invent reasonable details.

1. The app is kind of slow lately.
2. Some of the tests failed.
3. It crashes when you do stuff with big files.
4. The server was down for a while.
5. Use a good password.
6. Click the button.
7. The new version is better.
8. Make sure everything is set up.

<details>
<summary>Sample answers (Set 1)</summary>

1. Since the October 3 update, the app takes about 6 seconds to open; before, it took 1 second.
2. 4 of the 52 tests failed, all in `test_parser.py`.
3. The program crashes with `MemoryError` when the input file is larger than about 2 GB.
4. The server was unreachable from 14:05 to 14:40 on October 9.
5. Use a password of at least 14 characters that you don't use anywhere else.
6. Click **Save** at the bottom right of the window.
7. Version 2.0 starts twice as fast and uses 30% less memory than version 1.4.
8. Before you start, install Python 3.12 or newer and clone the repository (see *Before you start*).
</details>

### Practice Set 2 — Find the problems in these instructions

> **Setup**
> To get started with the project you'll first want to make sure you have all the required things and then you can download it and run the main file, but if you're on Windows some of this is different, you should use the other command. Then it should work. If not check the settings.

List every problem you can find (target: 8), then rewrite it as proper instructions for a made-up project called `notegrep`.

<details>
<summary>Problems to find</summary>

1. Title doesn't say the task. 2. No statement of the end result. 3. Prerequisites are vague ("required things"). 4. Steps are not numbered; several actions in one sentence. 5. No commands given. 6. Condition (Windows) comes after the action, and "the other command" is not specified. 7. No expected result ("it should work" isn't checkable). 8. Troubleshooting is vague ("check the settings": which settings?). Also: run-on sentence; "you'll first want to" is wordy.
</details>

### Practice Set 3 — Write a bug report

Find a real bug or annoyance in any software you use (a website, an app, a game). Write a full bug report using the structure in Part 4. Then ask yourself: could a stranger see this bug from my steps alone?

---

## Watch, practise, and write

*Companions, not replacements: the lessons above come first. Video course for this track: [English resources](resources.md#video-course).*

- **Watch:** Google Technical Writing One (free). Technology Connections or Steve Mould (YouTube): watch one explanation of an everyday machine, then write your own.
- **Practise:** Google Technical Writing One's in-class exercises, done on paper first.
- **Fun writes this stage** ([prompt bank](writing-prompts.md)): #70 instructions for an alien · #71 bug report for your cat · #72 README for your fridge · #73 rewrite bad error messages

---

## Self-check

1. **[R] Blank sheet:** the structure of all four forms; the rules for steps; the parts of a definition; must/should/may.
2. **Description:** in 250–350 words plus one diagram, describe how a system you use daily works (a bike's gears, a fridge, a microwave, a phone charger). Use the five-part structure.
3. **Instructions:** write instructions for a task you know well on a computer. Run a usability test with a real person. Record how many times they hesitated or asked. Revise until zero.
4. **Spoken:** a short explainer using the shape in Part 6. Fillers counted.

## Done when

- [ ] Practice Sets 1–3 done.
- [ ] One description with a captioned diagram, revised with the E08 checklist.
- [ ] One set of instructions that passed a usability test with zero questions.
- [ ] [Bug Report Gauntlet](projects/bug-report-gauntlet/spec.md) complete.
- [ ] READMEs written for at least two of your projects.
- [ ] [Explain-a-System](projects/explain-a-system/spec.md) explainers 2–3 done.

**Next:** [E10 — Argument and Design Documents](E10-argument-and-design-documents.md).
