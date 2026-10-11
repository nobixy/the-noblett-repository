---
title: "Project: Explain-a-System"
id: "FND-EN-PRJ-explain-a-system"
type: "project"
module: "00-foundations"
track: "english"
phase: "C"
order: 690
prerequisites: [E07]
stages: "E08–E09"
artifact: "Five written explainers (400–700 words + diagram each) and five short recordings"
deliverable: "The explainers and recordings themselves, plus reader questions and your fixes"
---

# Project: Explain-a-System

| | |
| :-- | :-- |
| **You build** | Five plain-English explanations of everyday systems, each with a diagram and a spoken version. Each one previews a system you will build later in this curriculum |
| **Deliverable** | The explainers, the recordings, and a log of reader questions and fixes |

---

## Why this matters

Explaining something clearly is the strongest test of understanding there is. That's the Feynman technique, and this project makes it public: a real reader reads each explainer, and their questions show you exactly where your understanding or your writing failed.

The five topics are chosen on purpose. Each is something you use every day, and each is a small version of something you will **build** later. By the time you reach those modules, you will already have a mental model, a diagram, and a vocabulary. You will be refining an understanding, not starting from zero.

**Real-world analogs:** technical blog posts, documentation "concepts" pages, conference lightning talks, the explanations you give in code reviews and interviews.

---

## The five systems

| # | System | The question to answer | Later module where you build it |
| :-- | :-- | :-- | :-- |
| 1 | **A thermostat** | How does it keep a room at one temperature? | 04 (feedback, state machines), 13 |
| 2 | **A key press** | What happens between pressing a key and seeing the letter on screen? | 06 (hardware), 07–08 (OS, interrupts, drivers) |
| 3 | **A calculator adding two numbers** | How does a machine made of switches add? | 04 (logic gates, adders), 06 (CPU) |
| 4 | **Loading a web page** | What happens between typing an address and seeing the page? | 09 (networking), 10 (browser) |
| 5 | **A bank account surviving a power cut** | How does a bank make sure your money isn't lost or doubled if the power fails mid-transfer? | 11 (databases: logs, transactions, recovery) |

You may swap one topic for another everyday system you're curious about (GPS, a microwave, a phone charger, a traffic light), as long as you can name the later module it connects to.

---

## The process for each explainer

Each explainer follows the same six steps. They are the subgoal labels [S] for "explain a system."

### Step 1 — Blank-sheet first [R]

Before any research, write everything you already believe about how the system works. Draw a diagram. Be wrong freely. Save this as `N-before.md`. **This is important:** comparing it with your final version shows you what you learned.

### Step 2 — Research, limited

Find **two or three** good sources: an encyclopedia article, a well-known explainer (e.g. "How Stuff Works"), a textbook chapter, a good video. Read or watch. Then **close them** and take notes from memory. Return to the sources only to check specific points. Keep a list of sources (title, author, link).

**Limit:** one session. You are writing an explainer, not a thesis. Mark what you don't understand as an open question instead of researching forever.

### Step 3 — Feynman draft [F]

Write 400–700 words for a curious adult with no technical background. Use the E09 description structure: **purpose → parts → connections → walk-through of one flow → edge case**. Mark every spot where you hesitated or used a word you couldn't define with `??`. Go back to the sources for only those spots.

### Step 4 — Diagram and caption

One diagram: boxes and arrows (Excalidraw, Mermaid, or paper). Every box labelled. One caption that tells the reader what to notice. Refer to it from the text.

### Step 5 — Revise and get a reader (plus waiting)

Revise with the E08 checklist (after a break until a later session [D]). Then give it to **one reader** who doesn't know the topic. Ask them for:
1. the one place they got lost;
2. one question they still have after reading.

Fix the first. Answer the second in the text if it fits, or in a "Questions readers asked" section at the end.

### Step 6 — Record it [T]

A short spoken version using the E09 explainer shape (*point → map → walk-through → edge case → point again*), pointing at your diagram on screen or paper. Don't read the text; speak from the diagram. Listen back once. Count filler words. Note one improvement.

**Each explainer's checkpoint:** compare `N-before.md` with the final version. Write three sentences: what you believed before that was wrong, what you now understand, and what you still don't understand. That last one is your list of things to look forward to in the later module.

---

## Guidance for each topic

These are hints about what a good explainer must include. Don't read them until you've done Step 1.

<details>
<summary>1. Thermostat</summary>

Must include: the sensor, the setpoint, the comparison, the switch, and the loop (measure → compare → act → repeat). The clever detail: **hysteresis** (why it doesn't click on and off every second). Stretch: the difference between a simple on/off thermostat and a "smart" one that predicts. Key idea for later: a **feedback loop** — output affects the next input.
</details>

<details>
<summary>2. Key press</summary>

Must include: the key closes a switch; the keyboard's own small chip notices and sends a code (USB or Bluetooth) to the computer; the computer's processor is interrupted to handle it; the operating system passes it to the program that has focus; the program updates what should be shown; the screen is redrawn. Key ideas for later: **interrupts**, **drivers**, **the operating system as a middleman**, **layers**. Be honest about the parts you can't explain yet; that's expected.
</details>

<details>
<summary>3. Calculator adding</summary>

Must include: numbers stored as binary (on/off); adding two binary digits gives a sum digit and a carry; a tiny circuit made of switches (logic gates) can do that; chain them to add bigger numbers. Show one example: 5 + 3 in binary, column by column, with carries. Key ideas for later: **binary**, **logic gates**, **the adder**.
</details>

<details>
<summary>4. Loading a web page</summary>

Must include: the address (URL) is turned into a computer's number address (DNS, like a phone book); your computer opens a connection to that computer; it sends a request ("give me this page"); the reply is text in a format called HTML; the browser reads the HTML, fetches images and other files, works out where everything goes on screen, and draws it. Key ideas for later: **DNS**, **connections and reliability**, **requests and responses**, **parsing and layout**.
</details>

<details>
<summary>5. Bank account and the power cut</summary>

Must include: the problem — moving money is two steps (take from A, add to B), and power could fail between them; the solution — write down what you're *about to do* in a log first, then do it; after a crash, read the log to finish or undo half-done work. Key ideas for later: **transactions** (all or nothing), **write-ahead logging**, **recovery**. Use a paper-ledger analogy.
</details>

---

## Milestones

| Milestone | Done when |
| :-- | :-- |
| **1** (E08) | Explainer 1 complete: all six steps, reader feedback fixed, recording made |
| **2** (E09, sections 1–2) | Explainer 2 complete |
| **3** (E09, sections 3–4) | Explainer 3 complete |
| **4** (E09, section 5 / after) | Explainers 4 and 5 complete |
| **5** (after all five) | A one-page reflection (see deliverable) |

You don't need a new reader for every explainer, but use at least **two different readers** across the five.

## Common pitfalls

- **Researching forever.** The one-session limit is a feature. Gaps become questions for later modules.
- **Textbook voice.** If it sounds like an encyclopedia, you're hiding behind other people's words. Use your own sentences and your own analogies.
- **Too many parts.** A diagram with 15 boxes explains nothing. Pick the 4–7 parts that matter for the one flow you walk through.
- **Analogies that break.** Every analogy is wrong somewhere. Say where: "*The phone book analogy breaks down because…*". That sentence shows real understanding.
- **Reading the script in the recording.** Speak from the diagram. It sounds natural, and it proves you understand.

## Communication deliverable

For each explainer, in `~/workbench/english/explainers/N-topic/`:
- `before.md` (Step 1), `explainer.md` (final), the diagram file, `sources.md`, the recording, and `feedback.md` (the reader's lost-point and question, and your fixes).

After all five, `reflection.md` (one page): which explainer was hardest and why; how your "before" drafts changed across the five; your filler-word counts from 1 to 5; the three open questions you most want later modules to answer.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Step 1 blank sheet; research notes taken from memory |
| **F** | Step 3 is a Feynman pass; Step 6 is the spoken version |
| **W** | The "where the analogy breaks" sentence; your three open questions |
| **S** | The six steps themselves |
| **I** | Explainers alternate between hardware-ish and software-ish topics |
| **D** | The break (until a later session) before revising |
| **T** | Real readers and recordings |

## Stretch goals

- **Publish** one explainer as a blog post.
- **Make a short video** with your diagram animated (even a sequence of three images).
- **Revisit later:** when you finish the matching module, rewrite that explainer from scratch without looking at the old one. Then compare. This is one of the most satisfying exercises in the whole curriculum.

## Self-grading rubric (per explainer)

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Accuracy | Correct, with honest gaps marked | Minor errors | Major misunderstandings |
| Structure | Purpose → parts → flow → edge case, clear walk-through | Mostly | No flow |
| Plain language | Every term defined; own analogies; analogy limits stated | Some jargon | Textbook voice |
| Diagram | Labelled, captioned, referenced | Present | Missing or cluttered |
| Reader test | Feedback recorded and fixed | Feedback recorded | No reader |
| Recording | From diagram, under 3:30, fillers counted | Recorded | Missing |

**Done when:** all five explainers average at least 2 in every area.

## Connections

- **Back:** E08 (clarity, revision, speaking), E09 (description structure, diagrams, definitions).
- **Forward:** Module 04 (adders, feedback), Module 06 (CPU), Module 08 (interrupts, drivers), Module 09–10 (web), Module 11 (logs and recovery). Each module overview reminds you to reread your explainer before starting.
