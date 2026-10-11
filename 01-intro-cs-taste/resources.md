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
- **Ben Eater's 8-bit breadboard computer** videos (YouTube, free) — someone building a computer from chips, step by step. Watch for inspiration; Module 04 is where you'll do similar things.

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

## Video and course companions
Free YouTube series and Coursera/edX/MIT OCW courses for this module are listed in [courses-and-videos.md](../courses-and-videos.md#modules-0113). Use them with the [V protocol](../study-protocols.md#v--watch-actively): lectures and quizzes as second explanations; this module's own projects, not the courses' assignments.
