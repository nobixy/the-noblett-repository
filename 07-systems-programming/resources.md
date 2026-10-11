---
title: "07 — Resources"
id: "MOD07-RES"
type: "reference"
module: "07-systems-programming"
phase: "C"
order: 1070
prerequisites: []
---

# 07 — Resources

*Pointers only. The projects are the course.*

## C
- **Kernighan & Ritchie, *The C Programming Language*** (2nd ed.) — short, exact, still the best introduction; do its exercises alongside Lab 01. (And Level 4 copywork.)
- **Jens Gustedt, *Modern C*** (free PDF from the author) — C17 done properly, with care about undefined behaviour.
- **Beej's Guide to C Programming** (beej.us, free) — friendly second explanations.
- **cppreference.com, C section** — the best quick reference for the standard library.

## Systems
- **Bryant & O'Hallaron, *Computer Systems: A Programmer's Perspective*** (book) — chapters 3 (machine-level programs), 6 (memory hierarchy), 8 (exceptional control flow: processes and signals), 9 (virtual memory and dynamic memory allocation), 10 (system-level I/O). Read the chapters as second explanations; **do your own projects**, not the book's labs.
- **Michael Kerrisk, *The Linux Programming Interface*** (book) — the definitive reference for every system call here. Chapters on file I/O, processes, signals, pipes, process groups, sessions, job control, and terminals.
- **GNU C Library manual** (gnu.org, free) — chapter "Job Control" (Burrow Milestone 4).
- **`man 2`** pages for every system call; **`man 7 signal`, `man 7 signal-safety`, `man 7 credentials`**.

## Tools
- **gdb:** "Debugging with GDB" (sourceware.org); Julia Evans' "How to use gdb" zines and posts.
- **Valgrind** user manual (valgrind.org); **AddressSanitizer** wiki (github.com/google/sanitizers).
- **Brendan Gregg's perf examples** (brendangregg.com/perf.html).

## Per project
- **Heapsmith:** Paul Wilson et al., "Dynamic Storage Allocation: A Survey and Critical Review" (1995) — the classic survey; the jemalloc and mimalloc design documents for modern ideas.
- **Burrow:** the POSIX Shell Command Language specification (pubs.opengroup.org) — the exact rules your subset follows.
- **Crate:** "A Painless Guide to CRC Error Detection Algorithms" (Ross Williams, free); the zip and PNG specifications (for comparison, not copying); the AFL++ documentation; search "Zip Slip vulnerability" for the path-traversal history.

## Video course

*Companions, not replacements: your labs and projects are the course. Watch with the [V protocol](../study-protocols.md#v--watch-actively) (pause, predict, then blank-sheet [R]), take lectures and quizzes as second explanations, and build this module's own projects, not the course's assignments. How courses fit your sessions: [study-protocols § Using video courses](../study-protocols.md#using-video-courses).*

**Primary — CMU 15-213 Introduction to Computer Systems**, Carnegie Mellon University.
- Course page with slides and code for every lecture: [15-213 course page](https://www.cs.cmu.edu/afs/cs/academic/class/15213-f15/www/schedule.html) · lecture recordings on YouTube: [CMU 15-213 Introduction to Computer Systems playlist](https://www.youtube.com/playlist?list=PLpIxOj-HnDsPZIJYO4U9f-xRI8bBadaso)
- **Why it fits:** *CS:APP* (Bryant & O'Hallaron) is this course's textbook, and this module already reads CS:APP chapters 3, 6, 8, 9 and 10. The lectures on processes and signals, virtual memory and dynamic memory allocation are the classic explanations of exactly what Heapsmith and Burrow build, in C on Linux.
- **Caveat:** CMU's own recordings sit on CMU's video server, which asks for a login. The YouTube playlist is a re-upload of the lectures by a third party (Abhinav Maurya), not an official CMU channel. It may disappear; the slides on the course page are official.

**Alternate — CS50x (CS50's Introduction to Computer Science)**, Harvard (David J. Malan). Free: [YouTube lectures](https://www.youtube.com/playlist?list=PLhQjrBD2T380hlTqAU8HfvVepCcjCqTg6) · [course site](https://cs50.harvard.edu/x/).
- **Why:** the friendliest free introduction to C, pointers and memory for someone coming from Python. Use it for Lab 01 if 15-213 starts too fast; it does not go as far as allocators, signals or job control.

### Lecture-to-vault map

15-213 numbers are lecture numbers as titled in the playlist.

| Vault item | CMU 15-213 (primary) | CS50x (alternate) |
| :-- | :-- | :-- |
| [Lab 01 — C for Python programmers](labs/lab-01-c-for-python-programmers.md) | Lectures 02–03 Bits, Bytes and Integers · 04 Floating Point | Lecture 1 C · Lecture 2 Arrays · Lecture 4 Memory |
| [Lab 02 — Debugging tools](labs/lab-02-debugging-tools.md) | Lectures 05–09 Machine-Level Programming I–V (reading what gdb shows you) | Lecture 2 Arrays (debugging) · Lecture 4 Memory (pointers, segmentation faults, dynamic memory allocation) |
| [Lab 03 — System calls and strace](labs/lab-03-system-calls-and-strace.md) | Lecture 13 Exceptional Control Flow: Exceptions and Processes · Lecture 15 System-Level I/O | — |
| [Lab 04 — Measuring the memory hierarchy](labs/lab-04-measuring-the-memory-hierarchy.md) | Lecture 10 The Memory Hierarchy · Lecture 11 Cache Memories | — |
| [Heapsmith](projects/heapsmith/spec.md) (malloc) | Lectures 16–17 Virtual Memory · Lecture 18 Dynamic Memory Allocation: Basic Concepts · Lecture 19 Advanced Concepts | Lecture 5 Data Structures (linked lists) |
| [Burrow](projects/burrow/spec.md) (shell with job control) | Lecture 13 Exceptions and Processes · Lecture 14 Multitasking: Shells, Signals, Nonlocal Jumps | — |
| [Crate](projects/crate/spec.md) (archive format) | Lecture 15 System-Level I/O | Lecture 4 Memory (file I/O) |

**Gaps:** CRC checksums and fuzzing (Crate) are not in either course; use the pointers above.
