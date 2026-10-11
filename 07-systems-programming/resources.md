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

## Video and course companions
Free YouTube series and Coursera/edX/MIT OCW courses for this module are listed in [courses-and-videos.md](../courses-and-videos.md#modules-0113). Use them with the [V protocol](../study-protocols.md#v--watch-actively): lectures and quizzes as second explanations; this module's own projects, not the courses' assignments.
