---
title: "02 — Resources"
id: "MOD02-RES"
type: "reference"
module: "02-programming-fundamentals"
phase: "B"
order: 490
prerequisites: []
---

# 02 — Resources

*Pointers only. The projects are the course.*

## Python, deeper
- **The Python Tutorial**, sections 9 (classes) and 10–11 (standard library tour) — docs.python.org/3/tutorial.
- **Python docs** for `dataclasses`, `enum`, `struct`, `typing.Protocol`, `pathlib`, `json`, `random`, `math`.
- **Brett Slatkin, *Effective Python*** (book) — short items on writing clear Python; dip in, don't read straight through.
- **Fluent Python** (Luciano Ramalho, book) — for later, when you want to know how Python really works.

## Program design
- **John Ousterhout, *A Philosophy of Software Design*** (book, short) — "deep modules," information hiding, and why complexity grows. Read chapters 1–6 during this module.
- **Kernighan & Pike, *The Practice of Programming*** (book) — chapters on style, design, testing, and debugging. Older, still excellent; also a Level 4 copywork source.

## Testing and git
- **pytest documentation** — "Get started," "How to parametrize," "Fixtures."
- **Pro Git** (Scott Chacon & Ben Straub, free at git-scm.com/book) — chapters 2–3 (basics and branching), 7.10 (debugging with bisect).

## Spaced repetition (Study Deck)
- **Piotr Woźniak's description of the SM-2 algorithm** (supermemo.com, "Application of a computer to improve the results obtained in working with the SuperMemo method") — the original source of the formula.
- **Michael Nielsen, "Augmenting Long-term Memory"** (essay, free online) — a thoughtful long read on using spaced repetition seriously.
- **The FSRS project** (open-spaced-repetition on GitHub) — for the stretch goal.

## Sound (Tone Loom)
- **The WAV/RIFF format** — many free pages document the 44-byte PCM header; check yours against two of them.
- **Audacity** (free) — waveform and spectrum views.
- **3Blue1Brown, "But what is the Fourier Transform?"** (YouTube) — for the "why do square waves buzz" question; full treatment in Module 12.

## Parsing (Worldfile)
- **Crafting Interpreters** (Robert Nystrom, free at craftinginterpreters.com), chapters 4–6 — a beautifully written explanation of scanning and recursive-descent parsing. Read them as a *second explanation* after you've written your own condition parser.

## Video course

*Companions, not replacements: your labs and projects are the course. Watch with the [V protocol](../study-protocols.md#v--watch-actively) (pause, predict, then blank-sheet [R]), take lectures and quizzes as second explanations, and build this module's own projects, not the course's assignments. How courses fit your sessions: [study-protocols § Using video courses](../study-protocols.md#using-video-courses).*

**Primary — MIT 6.100L Introduction to CS and Programming using Python**, MIT OpenCourseWare (Dr. Ana Bell). Free.
- Lectures: [YouTube playlist](https://www.youtube.com/playlist?list=PLUl4u3cNGP62A-ynp6v6-LGBCzeH3VAQB) · course page with notes and problem sets: [MIT OCW 6.100L](https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/)
- **Why it fits:** Python, aimed at people with little or no programming background, and it covers this module's three labs in the same order of ideas: decomposition and functions, recursion, testing and debugging, exceptions, dictionaries, and classes and inheritance. It goes one step deeper than CS50P (Module 01) without leaving Python.

**Alternate — The Missing Semester of Your CS Education**, MIT CSAIL. Free: [YouTube playlist](https://www.youtube.com/playlist?list=PLyzOVJj3bHQuloKGG59rS43e29ro7I57J) · [course site](https://missing.csail.mit.edu/2020/).
- **Why:** Lab 02 is as much about tools (git, bisect, the debugger, the shell) as about Python. Missing Semester is the best free course on exactly those tools, and it is Linux-first.

### Lecture-to-vault map

| Vault item | MIT 6.100L (primary) | Missing Semester (alternate) |
| :-- | :-- | :-- |
| [Lab 01 — Recursion and decomposition](labs/lab-01-recursion-and-decomposition.md) | Lecture 7 Decomposition, Abstraction, and Functions · Lecture 15 Recursion · Lecture 16 Recursion on Non-numerics | — |
| [Lab 02 — Testing and git workflow](labs/lab-02-testing-and-git-workflow.md) | Lecture 12 List Comprehension, Functions as Objects, Testing, and Debugging · Lecture 13 Exceptions and Assertions | Lecture 6 Version Control (git) · Lecture 7 Debugging and Profiling |
| [Lab 03 — Classes and data modelling](labs/lab-03-classes-and-data-modelling.md) | Lecture 17 Python Classes · Lecture 18 More Python Class Methods · Lecture 19 Inheritance · Lecture 20 Fitness Tracker OOP Example | — |
| [Study Deck](projects/study-deck/spec.md) (spaced repetition) | Lecture 14 Dictionaries · Lectures 17–20 (classes) | Lecture 2 Shell Tools and Scripting |
| [Tone Loom](projects/tone-loom/spec.md) (WAV synthesis) | Lecture 5 Floats and Approximation Methods · Lecture 25 Plotting | — |
| [Worldfile](projects/worldfile/spec.md) (parser, state machines) | Lecture 13 Exceptions and Assertions · Lecture 16 Recursion on Non-numerics | Lecture 4 Data Wrangling |

**Gaps:** no course covers the WAV format, Leitner/SM-2 scheduling algorithms, or state-machine parsers directly; the books and docs above do.
