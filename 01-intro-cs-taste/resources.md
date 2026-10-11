---
title: "01 — Resources"
id: "MOD01-RES"
type: "reference"
module: "01-intro-cs-taste"
phase: "A"
order: 300
prerequisites: []
---

# 01 — Resources

*Pointers only. The projects are the course. Open these when you want a second explanation, never instead of building.*

## Python
- **The Python Tutorial** — docs.python.org/3/tutorial. Sections 3–7 match Lab 01. (Also a Level 2 copywork source.)
- **Automate the Boring Stuff with Python** (Al Sweigart) — free to read at automatetheboringstuff.com. Friendly second explanations of Lab 01 topics.
- **Python standard library docs** for the modules these projects use: `socket`, `selectors`, `os` (fork, exec, pipe, dup2), `signal`, `shlex`, `urllib.parse`, `shutil`.

## How computers run programs (Nib)
- Charles Petzold, ***Code: The Hidden Language of Computer Hardware and Software*** (2nd ed.) — the best book-length story of how switches become a computer. Chapters on binary, logic, and memory pair with Nib and Module 04.
- **Ben Eater's 8-bit breadboard computer** videos (YouTube, free) — someone building a computer from chips, step by step. Watch for inspiration; it is [Module 04's video course](../04-circuits-and-digital-logic/resources.md#video-course), where you'll do similar things.

## Networking (Relay)
- **Julia Evans, "Networking! ACK!"** zine (wizardzines.com, paid) and the free networking posts on jvns.ca.
- **Beej's Guide to Network Programming** (beej.us/guide/bgnet, free) — written for C, but its explanations of sockets, TCP, and UDP apply directly.

## Shells and processes (Burrow Jr.)
- **William Shotts, *The Linux Command Line*** (linuxcommand.org, free PDF) — the user's view of the shell.
- `man 2 fork`, `man 2 execve`, `man 2 pipe`, `man 2 dup2`, `man 7 signal` — the real documentation of the calls you're using. Read the DESCRIPTION sections.

## The web (Pagelet)
- **MDN Web Docs: "How the web works"** and **"An overview of HTTP"** (developer.mozilla.org, free).
- `curl -v http://example.com/` shows a real HTTP request and response; compare with what Pagelet sends.

## When you're stuck
- Read the error from the bottom up (Lab 02). Write a stuck note. Sleep on it.
- Search the exact error message in quotes.
- Ask in a beginner-friendly community (the Python Discord, r/learnpython). Include what you tried — your bug-report skills from E09 make people want to help.

## Video course

*Companions, not replacements: your labs and projects are the course. Watch with the [V protocol](../study-protocols.md#v--watch-actively) (pause, predict, then blank-sheet [R]), take lectures and quizzes as second explanations, and build this module's own projects, not the course's assignments. How courses fit your sessions: [study-protocols § Using video courses](../study-protocols.md#using-video-courses).*

**Primary — CS50's Introduction to Programming with Python (CS50P)**, Harvard (David J. Malan). Free on YouTube and at the course site.
- Lectures: [YouTube playlist](https://www.youtube.com/playlist?list=PLhQjrBD2T3817j24-GogXmWqO5Q5vYy0V) · course site with notes and problem sets: [cs50.harvard.edu/python](https://cs50.harvard.edu/python/)
- **Why it fits:** every project here is written in Python, and the labs teach exactly what CS50P's early lectures teach: functions, conditionals, loops, exceptions, unit tests and files. It assumes no prior programming, it is very well produced, and its lecture on unit tests (pytest) matches Lab 02.

**Alternate — Crash Course Computer Science**, CrashCourse (Carrie Anne Philbin). Free on YouTube: [playlist](https://www.youtube.com/playlist?list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo).
- **Why:** short, visual episodes on the ideas behind each project (gates and CPUs for Nib, networks for Relay, operating systems for Burrow Jr., the Web for Pagelet). Use it when you want the big picture, not Python practice.

### Lecture-to-vault map

| Vault item | CS50P (primary) | Crash Course CS (alternate) |
| :-- | :-- | :-- |
| [Lab 00 — Machine setup](labs/lab-00-machine-setup.md) | — (use the lab; CS50P uses its own online editor) | — |
| [Lab 01 — Python first steps](labs/lab-01-python-first-steps.md) | Lecture 0 Functions, Variables · Lecture 1 Conditionals · Lecture 2 Loops | #12 Programming Basics: Statements & Functions |
| [Lab 02 — Errors, tests and debugging](labs/lab-02-errors-tests-and-debugging.md) | Lecture 3 Exceptions · Lecture 5 Unit Tests | — |
| [Nib](projects/nib-machine/spec.md) (8-bit emulator) | Lecture 2 Loops · Lecture 8 Object-Oriented Programming | #3 Boolean Logic & Logic Gates · #4 Representing Numbers and Letters with Binary · #5 the ALU · #6 Registers and RAM · #7 the CPU · #8 Instructions & Programs |
| [Relay](projects/relay-chat/spec.md) (TCP chat) | Lecture 4 Libraries · Lecture 6 File I/O | #28 Computer Networks · #29 The Internet |
| [Burrow Jr.](projects/shell-sketch/spec.md) (mini shell) | Lecture 7 Regular Expressions (parsing input) | #18 Operating Systems · #22 Keyboards & Command Line Interfaces |
| [Pagelet](projects/pagelet/spec.md) (HTTP page viewer) | Lecture 4 Libraries · Lecture 7 Regular Expressions | #30 The World Wide Web |

**Gaps:** neither course covers `fork`/`exec`/pipes or raw sockets at the depth Burrow Jr. and Relay need; use the Python docs listed above, and Module 07 and Module 09 later.
