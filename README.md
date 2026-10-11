# The Noblett Repository

A from-the-ground-up, project-first self-study curriculum in Electrical Engineering and Computer Science.

You start at the very bottom: spelling and sentences, counting and place value. You end by building real systems on your own machine: a computer you designed, a shell, a memory allocator, a small operating system kernel, a reliable transport protocol, a web server, a document browser, and a database engine. Every step between is a project you build, test, and explain.

**Start here:** [00 - Start Here](<00 - Start Here.md>) is the checklist and dashboard. This README explains how the whole thing works. Read it once, all the way through, then go to Start Here.

---

## Who this is for

One learner, working a job and studying alongside it. Restarting English and math from the absolute basics, because both are needed to solve problems and to explain technical ideas clearly in writing and out loud. Learns best by building real things on a real machine.

This repository is written in plain English on purpose. Short sentences. Common words. Technical words are defined the first time they appear. That is also the writing style you are working toward.

---

## The ideas behind it

1. **Projects first. Theory serves the build.** You learn a concept because the thing you are building needs it. Reading supports building; it does not replace it.
2. **Every major project makes a real, working artifact on your own machine.** Linux is the home base. Core work stays portable (macOS and WSL notes below).
3. **Projects are deep.** Many sessions long, with milestones, success tests, common pitfalls, and stretch goals. You always know when you are done.
4. **Communication is part of every project.** A design doc, a lab report, or a recorded demo. A project is not finished until someone else could understand it.
5. **The foundations are real foundations.** English starts at spelling. Math starts at whole numbers and place value. Nothing is assumed. Every early stage points at the later system it will help you build.
6. **Proven study methods are built in, not bolted on.** Retrieval, Feynman explanations, why-questions, subgoal labels, spacing and interleaving, Franklin copywork, focused and diffuse thinking, and formal write-ups appear as concrete steps inside every module and project. See [study-protocols.md](study-protocols.md).
7. **Original projects.** Every project here is an original design for self-study. None of them recreate a famous course's assignment (see [Originality](#originality)).

---

## The sequence

The curriculum has five phases. Phases are groupings in order, not time periods. English and math run as **tracks** underneath everything (their own sessions, in rotation with build sessions); the build modules run on top.

```
Phase A  Foundations + first taste       ── 00 English E01–E05 · 00 Math M01–M05 · 01 Intro CS Taste
Phase B  Learn to program and to reason   ── 02 Programming · 03 Discrete Math · 04 Circuits & Logic
                                              (English E06–E08 · Math M06–M09 continue as tracks)
Phase C  Machines and algorithms          ── first finish English E09–E10 and Math M10–M11 (both track assessments),
                                              then 05 Data Structures & Algorithms · 06 Architecture · 07 Systems Programming
                                              (12 Math for Engineering starts as the math track after M11)
Phase D  The big systems                  ── 08 Operating Systems · 09 Networking · 10 Browser Engine · 11 Databases
                                              (12 continues; its Chance Lab comes after 09's Courier)
Phase E  Capstone                         ── 13 Capstone: connect your systems into one working stack
```

| # | Module | What you build (headline) | Phase |
| :-- | :-- | :-- | :-- |
| 00 | [Foundations: English](00-foundations/english/overview.md) | Spelling engine, machine manuals, bug reports, your first design doc | A–C (track) |
| 00 | [Foundations: Math](00-foundations/math/overview.md) | Base-counting board, prime factory, fare models, scale floor plans, growth curves | A–C (track) |
| 01 | [Intro CS Taste](01-intro-cs-taste/overview.md) | A tiny computer emulator, a talking pair of programs, a toy shell, a terminal page viewer | A |
| 02 | [Programming Fundamentals](02-programming-fundamentals/overview.md) | Your own spaced-repetition app, a sound synthesizer, a data-driven adventure engine | B |
| 03 | [Discrete Math](03-discrete-math/overview.md) | A logic solver, a toy cipher and its break, a counting verifier, a proof journal | B |
| 04 | [Circuits & Digital Logic](04-circuits-and-digital-logic/overview.md) | Breadboard circuits, your own logic simulator, chip-built adders and counters | B |
| 05 | [Data Structures & Algorithms](05-data-structures-and-algorithms/overview.md) | A word-diff tool, a search engine for your notes, a route planner, an editor buffer | C |
| 06 | [Computer Architecture](06-computer-architecture/overview.md) | A 16-bit CPU you design (ISA, emulator, assembler, gate-level datapath), a compiler for your own language, a cache simulator | C |
| 07 | [Systems Programming](07-systems-programming/overview.md) | A memory allocator, a shell, a checksummed archive format (all in C) | C |
| 08 | [Operating Systems](08-operating-systems/overview.md) | A scheduler arena, a tag-based FUSE file system, a small RISC-V kernel | D |
| 09 | [Networking](09-networking/overview.md) | A packet decoder, a reliable transport over UDP, an HTTP server | D |
| 10 | [Browser Engine](10-browser-engine/overview.md) | A document browser: fetch, parse, style, lay out, render, navigate | D |
| 11 | [Databases](11-databases/overview.md) | A crash-safe storage engine with B+tree index and a small query language | D |
| 12 | [Math for Engineering](12-math-for-engineering/overview.md) | Calculus, linear algebra and probability through simulations and image tools | C–D (math track) |
| 13 | [Capstone](13-capstone/overview.md) | Your browser, over your transport, from your server, on your stack | E |

There is no schedule and no deadline. You move to the next item when the current one's "Done when" list is true. It is not a race.

*Historical:* the [archived v1 plan](<99 - Archive/v1 - Course-Based Curriculum/>) (superseded by DR-010) lists advanced tracks (machine learning, robotics, security, the drone-swarm capstone). It is kept for reference only; taking any of it on after the core would need a new Decision Record.

### Videos, courses, and fun

- **[courses-and-videos.md](courses-and-videos.md)** maps free YouTube series, Coursera courses, Khan Academy, MIT OpenCourseWare, and more to every stage and module. They're companions to the builds, not replacements.
- **[The first sections](00-foundations/first-sections.md)** lays out the start as Sections 1–12, with badges.
- **[Writing prompts](00-foundations/english/writing-prompts.md)** and **[math puzzles and games](00-foundations/math/puzzles-and-games.md)** keep practice fun.

### When to start what

- **Placement first:** take the [English placement diagnostic](00-foundations/english/placement.md) and the M01 diagnostic. Skip what you already know; each stage and lab says how.
- **Section 1:** English E01 and Math M01 start. Set up your machine ([Lab 00](01-intro-cs-taste/labs/lab-00-machine-setup.md); it has a skip check).
- **Section 3 (after E01 and M01):** Start [01 Intro CS Taste](01-intro-cs-taste/overview.md). Its first lab teaches you just enough Python to begin (skip check at the top). Its projects use only whole numbers and short sentences.
- **From then on:** follow the order in [Start Here](<00 - Start Here.md>). **One build project at a time** (Start Here, operating rule 2). English and math continue as tracks at their own pace. Each item's `prerequisites` (in its frontmatter) and each module overview's Prerequisites section say what must be done first.

---

## How to work through a module

1. **Read the module's `overview.md`.** Objectives, sequence, how projects map to concepts, and which study protocols this module leans on.
2. **Do the labs** in `labs/` when the overview says to. Labs are short and guided. They give you the tools a project needs.
3. **Build the projects** in `projects/`. Each project folder has a `spec.md` with:
   - why it matters and what real system it mirrors
   - exact requirements and the format of every file or message
   - milestones, each with a "done when" test and a **Milestone Checkpoint** (retrieval, Feynman pass, why-ladder)
   - testing guidance, common pitfalls, and stretch goals
   - the communication deliverable
   - a self-grading rubric
4. **Write the deliverable.** Design doc before the main build, then update it. Lab report or demo at the end.
5. **Check `resources.md`** only when you need a second explanation. Resources are pointers. The projects are the course.
6. **Close the module** with the module's cumulative retrieval session (in each overview; checkpoint id `MODxx-CLOSE`) and tick it off in [Start Here](<00 - Start Here.md>).

### The session structure

The curriculum is measured in **sessions** and **sections**, never in hours or dates. The one canonical description is [study-protocols.md § The session loop](study-protocols.md#the-session-loop); in short:

| Unit | What it is |
| :-- | :-- |
| **Session** | One sitting on one track: warm-up recall → focused work on one thing → blank-sheet retrieval [R] → log entry. |
| **Track sessions** | Three kinds rotate: **math** (stage lesson and practice; do the hardest thinking when you are freshest), **English** (stage lesson, spelling, copywork [C], an optional fun write), and **build** (the next lab session or project milestone). Flashcard review [I] fits in any session. |
| **Section** | A numbered group of sessions. Stage practice routines are written as Section 1, 2, 3…, each with Sessions 1–5. The start of the curriculum is laid out as [Sections 1–12](00-foundations/first-sections.md). |
| **Section Review** | Closes every section: flashcards, a cold re-do of old problems, a spoken recording [F], and the plan for the next section ([template](<04 - System/Section Review Template.md>)). |
| **Milestone Checkpoint** | Closes every project milestone: R + F + W ([template](<04 - System/Milestone Checkpoint Template.md>)). |

The same structure is summarised in [how-i-study.md](how-i-study.md) §2. If a session goes wrong, do the **minimum session**: flashcards plus one copywork sentence, then a two-line log entry. Many small sessions beat occasional big ones.

---

## How the study methods are woven in

Every spec uses letter codes from [study-protocols.md](study-protocols.md):

| Code | Method | Where you will see it |
| :-- | :-- | :-- |
| **R** | Blank-sheet retrieval | End of every session; inside every Milestone Checkpoint |
| **F** | Feynman pass | Every new concept; every component you finish; spoken once per section |
| **W** | Why-ladder (elaborative interrogation) | Every rule in English and math; every design choice in a project |
| **S** | Subgoal labels on worked examples | Every math procedure; every hard function (labels as comments first) |
| **I** | Interleaving and spacing | Mixed practice sets in every stage; flashcard spacing (the review intervals are part of the technique; see [LM09](<02 - Atlas/LM09 - Spacing and Spaced Repetition.md>)) |
| **C** | Franklin copywork | Every English stage; technical prose later |
| **D** | Diffuse break and stuck notes | The stuck rule in every project (three honest attempts, then a stuck note and a break) |
| **T** | Teach-back and formal write-up | The communication deliverable in every project |
| **V** | Watch actively | Every video or online course: pause and predict, then recall and practise |

The methods are not extra homework. They replace rereading and passive watching. Most protocols are short steps inside a session.

---

## Tracking progress

- **[00 - Start Here](<00 - Start Here.md>):** the checklist. Tick a stage or project only when its "done when" line is true.
- **Frontmatter:** every stage, lab, project and overview carries `id`, `type`, `module`, `order` and `prerequisites`, documented in [Frontmatter Schema](<04 - System/Frontmatter Schema.md>). A progress-tracker app reads these.
- **Session log** ([log.md](log.md), entries in `03 - Journal/`): a few lines at the end of each session: worked on, did, stuck, next. Include stuck notes [D].
- **Your code:** keep all project code in a separate git repository on your machine, for example `~/workbench/`, with one folder per project (`~/workbench/01-nib/`, `~/workbench/09-courier/`). Commit at least once per session. Your commit history is your evidence.
- **Your writing:** design docs, lab reports and demo scripts go in the project's folder in `~/workbench/` (so they live next to the code), with a link from that session's journal entry.
- **Flashcards:** Anki at first; your own Study Deck app after Module 02.
- **Decisions:** if you change the plan, write a short [Decision Record](<04 - System/Decision Record.md>) in `04 - System/`. Don't rebuild the system on impulse.

---

## Environment

**Home base:** a Linux machine (this repo was written on Arch Linux). Everything also works on macOS or on Windows through WSL2, except where a project says otherwise (the FUSE file system and the raw-packet work need Linux or WSL2; use a Linux VM on a Mac).

**What you need, by phase.** Lab 00 walks you through installing these. Install only what the current phase needs (the C tools in row B are first used in Module 06 Lab 01 and Module 07, so you can wait until then).

| Phase | Tools | Arch package names (others similar) |
| :-- | :-- | :-- |
| A | A text editor (VS Code or Neovim), terminal, git, Python 3.12+, a spell checker | `git python code` or `neovim`, `hunspell hunspell-en_us` |
| B | C compiler and tools; circuit simulator; breadboard kit (see Module 04) | `gcc make gdb valgrind`; Falstad simulator (browser); `digital` (hneemann's Digital, AUR) or Logisim Evolution |
| C | Debugging and measurement | `clang lldb strace ltrace perf` |
| D | Virtual machines, networking and file system tools | `qemu-full riscv64-elf-gcc riscv64-elf-binutils wireshark-qt tcpdump fuse3 sqlite` |

**Hardware (optional until Module 04):** a starter electronics kit, a multimeter, a few 74HC-series logic chips, and a Raspberry Pi Pico (about $5). Module 04's overview has an exact shopping list, about $60–90 total. Every hardware lab has a simulator path first, so money is never a blocker.

**Writing tools:** a spell checker is allowed and encouraged for final drafts, but **not** for spelling practice or copywork. Your English stages say when. Grammar checkers (like LanguageTool) are allowed after you have tried to fix the draft yourself; treat their suggestions as questions, not orders [W].

**AI assistants:** allowed for explaining an idea a second way, or for reviewing your finished writing. Not allowed for writing your code, solving your exercises, or writing your deliverables. The point is that *you* can do it. If you use one, note it in the log.

---

## Originality

Every project in this repository is an original specification written for self-study. They teach the same core ideas as famous university courses, but they are not recreations of those courses' assignments. Specifically, nothing here copies the projects of Nand2Tetris, Berkeley CS61A/B/C, Stanford CS144, MIT 6.S081 (xv6), *Web Browser Engineering*, Harvard CS50, CMU 15-213/15-445, or similar.

How the projects differ:
- **Different designs.** You design your own CPU instruction set within given constraints, your own netlist format, your own transport protocol with its own packet layout, your own markup subset and storage format.
- **Different breakdowns.** Milestones follow what a self-learner can test alone, often building the testing tool first (a network "gremlin" that damages packets; a crash harness that kills your database mid-write).
- **No starter code, no autograders.** You write everything. Each spec gives requirements, formats, test ideas, and a self-grading rubric, so you can tell when you have succeeded.

Where a famous course covers the same topic, `resources.md` may point to its *lectures or readings* as a second explanation. Never to its assignments.

---

## Repository layout

```
README.md                    you are here
00 - Start Here.md           the checklist and dashboard
how-i-study.md               your study manifesto (the methods)
study-protocols.md           the methods as exact routines (R F W S I C D T V)
courses-and-videos.md        YouTube, Coursera, Khan, and other free courses mapped to every stage and module
log.md                       session log dashboard

00-foundations/
  first-sections.md          the start, as Sections 1–12
  english/                   placement.md, E01–E10: spelling → sentences → paragraphs → technical writing
  math/                      M01–M11: place value → fractions → algebra → geometry → logarithms
01-intro-cs-taste/           four small real systems, plus setup and Python labs
02-programming-fundamentals/
03-discrete-math/
04-circuits-and-digital-logic/   (EE: circuits, logic, maker labs)
05-data-structures-and-algorithms/
06-computer-architecture/
07-systems-programming/
08-operating-systems/
09-networking/
10-browser-engine/
11-databases/
12-math-for-engineering/     calculus, linear algebra, probability (applied)
13-capstone/

  each module:  overview.md · projects/<name>/spec.md · labs/*.md · resources.md

02 - Atlas/                  learning-method deep dives (LM01–LM16), topic indexes, reference hubs
03 - Journal/                session log entries (one file per date, created by Obsidian's daily-notes plugin)
04 - System/                 templates (design doc, lab report, demo, checkpoint …), decision records, Frontmatter Schema
99 - Archive/                historical: the superseded v1 course-based plan and other cut material
```

This folder is also an Obsidian vault. Curriculum files use standard Markdown links, so they work in Obsidian, on GitHub, and in any editor. Some notes in `02 - Atlas/` and `04 - System/` also use Obsidian `[[wikilinks]]`.

Personal financial, health, identity and relationship data never goes in this repository.
