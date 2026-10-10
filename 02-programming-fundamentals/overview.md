---
title: "02 — Programming Fundamentals"
module: "02-programming-fundamentals"
hours: 160
tags: [module, programming]
---

# 02 — Programming Fundamentals

**From "I can write a script" to "I can build and maintain a real program."** This module deepens your Python into the habits of a working programmer: breaking problems into functions, recursion, modelling data with classes, handling errors on purpose, reading and writing files in formats you design, testing seriously, and using git like a professional. You learn them by building three programs you'll actually use or enjoy: your own spaced-repetition study app, a sound synthesizer that writes audio files byte by byte, and an engine for text adventures whose worlds are data files.

---

## Prerequisites

- [01 Intro CS Taste](../01-intro-cs-taste/overview.md) done (all three labs and at least three of the four projects).
- English **E05+** (you'll write READMEs and short design notes). Math **M05+** (fractions and ratios matter in Tone Loom; exponents arrive with M07 — Tone Loom's pitch formula is explained in the spec).

## Objectives

By the end you will be able to:
1. Decompose a problem into functions and modules with clear names and single jobs.
2. Write recursive functions and explain them with a base case and a smaller subproblem.
3. Model data with classes and dataclasses, and state the **invariants** that must always hold.
4. Design simple file formats (text and binary) and write robust parsers with helpful error messages.
5. Handle errors deliberately: validate input, raise meaningful exceptions, never lose user data.
6. Test with pytest: unit tests, round-trip tests, regression tests, golden-file tests, and tests with a fake clock.
7. Use git branches, meaningful commits, and a README that lets a stranger run your project.
8. Write a short design note *before* building, and compare it with what you built.

## Sequence and time

| Order | Item | Hours | Concepts |
| :-- | :-- | --: | :-- |
| 1 | [Lab 01 — Recursion and Decomposition](labs/lab-01-recursion-and-decomposition.md) | 10 | breaking problems down; recursion; Pólya |
| 2 | [Lab 02 — Testing and Git Workflow](labs/lab-02-testing-and-git-workflow.md) | 8 | pytest fixtures, parametrised tests, branches, merges |
| 3 | [Lab 03 — Classes and Data Modelling](labs/lab-03-classes-and-data-modelling.md) | 10 | classes, dataclasses, invariants, `__repr__`, enums |
| 4 | **[Project: Study Deck](projects/study-deck/spec.md)** | 45 | data model, plain-text formats, scheduling algorithms, fake clocks, a CLI you use daily |
| 5 | **[Project: Tone Loom](projects/tone-loom/spec.md)** | 40 | binary file formats, bytes and endianness, sampling, ratios and exponents in pitch, a song text format |
| 6 | **[Project: Worldfile](projects/worldfile/spec.md)** | 45 | parsing a format you design, state machines, a tiny condition language (recursion), save/load, golden-file testing |
| | **Total** | **~160** | |

At about 12 hours a week on this module (with foundations continuing), roughly 13–14 weeks. Do the labs first; then the projects in any order (Study Deck first is recommended: you'll use it for the rest of the curriculum).

## How the projects map to concepts

| Concept | Study Deck | Tone Loom | Worldfile |
| :-- | :-- | :-- | :-- |
| Decomposition into modules | storage / scheduler / CLI | synth / mixer / writer / song parser | parser / engine / UI |
| Data modelling with invariants | `Card`, review history | `Note`, `Track`, sample buffers | `Room`, `Item`, `GameState` |
| File formats | Markdown cards + review log (text) | WAV (binary, little-endian) + song text | world file (text) + save file |
| Parsing with good errors | card files | song files | world files (line numbers) |
| Recursion | (stretch) | (stretch: arpeggio patterns) | condition expressions |
| Testing style | fake clock, simulation | byte-exact headers, golden waveforms | golden-file playthroughs |
| Math | spacing intervals, averages | fractions, ratios, exponents, sine | Boolean logic |

## Connections

- **Back:** [Spelling Engine](../00-foundations/english/projects/spelling-engine/spec.md) becomes one card type in Study Deck; [Base Workshop](../00-foundations/math/projects/base-workshop/spec.md)'s `minihex.py` is how you'll inspect Tone Loom's WAV bytes; Lab 01's adventure grows into Worldfile.
- **Forward:** [03 Discrete Math](../03-discrete-math/overview.md) (the logic in Worldfile's conditions becomes a full logic engine); [05 DSA](../05-data-structures-and-algorithms/overview.md) (your parsers and data models get faster data structures); [07](../07-systems-programming/overview.md) (binary formats again, in C); [12](../12-math-for-engineering/overview.md) (Tone Loom's waves become signals).

## How the study methods run through this module

| Protocol | In this module |
| :-- | :-- |
| **R** | After every lab session: rewrite its key function from memory. After every milestone: Milestone Checkpoint. **Study Deck itself becomes your retrieval tool** — from now on, every flashcard in the curriculum lives in it. |
| **F** | Each project has one core idea to explain plainly: spacing algorithms; how a WAV file stores sound; how a recursive evaluator works. |
| **W** | Every spec lists design choices to justify ("Why plain text and not a database?", "Why little-endian?", "Why golden files?"). Answers go in your design notes. |
| **S** | Subgoal comments before every non-trivial function, as in Module 01. Lab 01 teaches subgoals for recursion specifically. |
| **I** | Lab exercises mix recursion, iteration, and data modelling. Weekly Study Deck reviews interleave every subject you've studied. |
| **D** | Recursion and parsers produce confusing bugs. Stuck notes; the 90-minute rule. |
| **T** | Each project: README, a short design note written **before** building (E06–E08 level), and a recorded demo. |

### Communication deliverables, sized for you

You're likely around E05–E08 during this module. Each project asks for:
- a **design note** (1–2 pages) written *before* the main build: what it does, the data, the file formats, two choices with reasons. Update it after.
- a **README** that passes the five-minute stranger test (E09 preview).
- a **recorded demo** (4–6 minutes).

## Environment

Python 3.12+, pytest, git. For Tone Loom: any audio player (`aplay` on Linux, `afplay` on macOS) and optionally Audacity (free) to look at waveforms. No third-party libraries are required for any milestone; the specs say where a library is allowed for a stretch goal.

## Module close

1. **Cumulative retrieval [R] (45 min):** on a blank page, draw the module structure of all three projects and list each one's file formats and invariants.
2. **Refactor review [W]:** pick your messiest function from any project. Rewrite it with better decomposition and names. Write three sentences: what was wrong, what you changed, why it's better.
3. **Showcase [T]:** a 6-minute recording: all three projects, two minutes each.
4. Tick the module in [Start Here](<../00 - Start Here.md>).

**Next:** [03 Discrete Math](../03-discrete-math/overview.md) and [04 Circuits and Digital Logic](../04-circuits-and-digital-logic/overview.md) (these two can run side by side).
