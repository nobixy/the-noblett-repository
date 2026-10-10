---
title: "01 — Intro CS Taste"
module: "01-intro-cs-taste"
hours: 90
tags: [module, intro, projects]
---

# 01 — Intro CS Taste

**Four small, real versions of the big systems you'll build later.** In this module you build a tiny computer, two programs that talk across a network (even when the network loses messages), a mini shell that launches programs, and a document viewer that fetches pages and lets you follow links. Each one works, runs on your own machine, and fits in a few hundred lines of Python.

Then, years from now in this curriculum, you'll build the full-size versions: your own CPU, your own reliable transport protocol, your own Unix shell in C, your own browser engine. When you get there, you'll recognise them. That's the point of this module: **here is a small, real version of the kind of thing you will eventually construct.**

---

## When to start

After **English E01** and **Math M01** (about week 3). The projects use only whole numbers and short sentences. You learn the Python you need in [Lab 01](labs/lab-01-python-first-steps.md), as you go.

Run this module alongside the foundations: English in the evenings, math in the mornings, **this module on Saturdays** (plus one or two weekday sessions if you have energy).

---

## Objectives

By the end of this module you will be able to:
1. Use a Linux terminal, a text editor, git, and Python to build and run programs.
2. Write Python programs with variables, conditions, loops, functions, lists, dictionaries, files, and tests.
3. Explain, in plain words, how a computer runs a program (fetch, decode, execute).
4. Explain how two programs talk over a network, and one way to make delivery reliable when messages get lost.
5. Explain what a shell does and what a process is.
6. Explain how a browser gets a page and turns it into something you can read and click.
7. Give a short spoken demo of something you built.

---

## Sequence and time

| Order | Item | What | Hours | English/Math needed |
| :-- | :-- | :-- | --: | :-- |
| 1 | [Lab 00 — Machine Setup](labs/lab-00-machine-setup.md) | Terminal, editor, git, Python, your workbench repository | 6 | E01, M01 |
| 2 | [Lab 01 — Python First Steps](labs/lab-01-python-first-steps.md) | Ten short sessions: just enough Python, learned by building | 20 | E01, M01 |
| 3 | [Lab 02 — Errors, Tests, and Debugging](labs/lab-02-errors-tests-and-debugging.md) | Reading tracebacks, `assert`, `pytest`, print-debugging, stuck notes | 4 | E02 |
| 4 | **[Project 1: Nib, a tiny computer](projects/nib-machine/spec.md)** | An emulator for an 8-bit machine you can program, plus a tiny assembler | 18 | M01–M02 |
| 5 | **[Project 2: Relay, talking programs](projects/relay-chat/spec.md)** | A chat over TCP with your own protocol; then over a lossy link with your own acknowledgments | 16 | M01–M03 |
| 6 | **[Project 3: Burrow Jr., a mini shell](projects/shell-sketch/spec.md)** | A command loop that starts programs as real processes, with built-ins, redirection, and a pipe | 12 | M01 |
| 7 | **[Project 4: Pagelet, a page viewer](projects/pagelet/spec.md)** | Fetch pages over HTTP with a hand-written request, parse a small markup language, wrap text, follow links | 14 | M01–M02 |
| | **Total** | | **~90** | |

At about 6–8 hours a week (Saturdays plus a little), that's 3 months, ending around the time you reach English E05 and Math M04. The four projects can be done in any order after Lab 02, but the order above builds skills best.

---

## How the projects map to concepts — and to later modules

| Project | Core ideas you meet | Full-size version later |
| :-- | :-- | :-- |
| **Nib** | Memory as numbered bytes; registers; the fetch–decode–execute cycle; machine code; an assembler; bugs from overflow | [04](../04-circuits-and-digital-logic/overview.md) (the gates underneath), [06](../06-computer-architecture/overview.md) (you design a 16-bit CPU, emulator, assembler, and its hardware datapath) |
| **Relay** | Sockets; clients and servers; protocols as agreements; message framing; loss, duplication, reordering; sequence numbers, acknowledgments, timeouts | [09](../09-networking/overview.md) (Courier: a full reliable transport over UDP with sliding windows; Lantern: an HTTP server) |
| **Burrow Jr.** | Processes; `fork`, `exec`, `wait`; exit codes; why `cd` must be built in; file descriptors; pipes | [07](../07-systems-programming/overview.md) (the full Burrow shell in C), [08](../08-operating-systems/overview.md) (how the kernel creates and schedules processes) |
| **Pagelet** | Requests and responses; HTTP by hand; parsing text into structure; word wrapping (layout); links and history | [10](../10-browser-engine/overview.md) (a document browser with a real parser, styles, and box layout), [09](../09-networking/overview.md) (the server side) |

**When you reach each later module, its overview will send you back here** to reread your Module 01 project and your notes. You'll be surprised how much you understood, and how much more you'll see.

---

## How the study methods run through this module

Every project milestone ends with a **Milestone Checkpoint** (R + F + W, about 30 minutes; [template](<../04 - System/Milestone Checkpoint Template.md>)).

| Protocol | How it shows up here |
| :-- | :-- |
| **R** Blank-sheet retrieval | After every Lab 01 session: write the session's code from memory. After every milestone: draw the system's parts from memory. |
| **F** Feynman pass | Each project has one core idea to explain plainly: fetch–decode–execute; acknowledgments; processes; request–response. Spoken, recorded. |
| **W** Why-ladder | Each spec lists design questions: "Why must `cd` be a built-in?", "Why does the sender need a timer?", "Why are instructions 2 bytes?" |
| **S** Subgoal labels | Write the steps of every function as comments before code. Lab 01 teaches this from session 1. |
| **I** Interleave and space | Lab 01's review questions mix old sessions. Projects alternate hardware-ish and software-ish topics. Flashcards for Python syntax and key terms. |
| **D** Diffuse break | The 90-minute stuck rule. Stuck notes in your log. |
| **T** Teach-back and write-up | Each project: a recorded demo (3–5 minutes) and a short written explanation, sized for your English stage. |

### Communication deliverables, sized for you

You'll be early in the English track (around E02–E05) during this module. So the deliverables are:
- **A recorded spoken demo** for each project (speaking is often easier than writing at first, and it's half of technical communication).
- **A short written explanation**: 5–10 sentences, in simple, correct sentences. Use the stage you're on. Short and correct beats long and messy.
- **A README** with how to run the project (the [Machine Manual](../00-foundations/english/projects/machine-manual/spec.md) project teaches exactly this skill).

Run a spell checker on the final version (allowed for deliverables, not for spelling practice), and put every word it catches into your spelling error log.

---

## Environment

- Linux (your Arch machine) or macOS / WSL2.
- Python 3.12 or newer.
- A text editor: **VS Code** (easy) or **Neovim** (powerful, steeper). Lab 00 helps you choose.
- `git`. Optional: `espeak-ng` (for the Spelling Engine), `tk` (for Python's turtle).
- All code lives in `~/workbench/01-<project>/`, in your git repository.

---

## Originality note

These four projects are original designs for this curriculum. Nib's instruction set, Relay's protocol and lossy-link tests, Burrow Jr.'s milestone breakdown, and Pagelet's markup language are not taken from any course. They teach ideas you'll also find in famous courses, through different builds.

---

## Module close

When all four projects are done:

1. **Cumulative retrieval [R] (45 minutes, nothing open):** on one big sheet, draw all four systems as boxes and arrows. For each, write the one sentence that explains it. Then check against your projects and fix gaps.
2. **Feynman showcase [F] [T]:** record a 5-minute video: "Four tiny systems I built," one minute each, plus one minute on what surprised you.
3. **Reflection (half a page):** which project did you enjoy most, and why? That's a clue about which later modules will feel best — and worth knowing when energy is low.
4. Tick the module in [Start Here](<../00 - Start Here.md>).

**Next:** [02 Programming Fundamentals](../02-programming-fundamentals/overview.md).
