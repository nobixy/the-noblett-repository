---
title: "Engineering Practice"
aliases: ["03 - Engineering Practice"]
type: hub
tags:
  - hub
  - engineering
  - practice
---

# Engineering Practice

Applied tooling, building, testing, and operational skills that run parallel to theory. No separate module and no separate sessions: each skill is learned inside the module that first needs it, then used in every module after.

## Continuous Engineering Curriculum

| Skill | Learned in | Practice from then on | Done when |
| :--- | :--- | :--- | :--- |
| **Version Control (Git)**: branching, rebasing, resolving conflicts, semantic commits | [Module 01 Lab 00](<../01-intro-cs-taste/labs/lab-00-machine-setup.md>), [Module 02 Lab 02](<../02-programming-fundamentals/labs/lab-02-testing-and-git-workflow.md>) | `~/workbench/` and every build live in git | You rebase and resolve a conflict without looking anything up |
| **Operating Systems (Linux)**: command line, shell scripting, permissions, processes | [Module 01 Lab 00](<../01-intro-cs-taste/labs/lab-00-machine-setup.md>) | Every module; deepened in [07](<../07-systems-programming/overview.md>) and [08](<../08-operating-systems/overview.md>) | You can do a whole project's work from the terminal |
| **Debugging & Profiling**: GDB, Valgrind, flame graphs, browser DevTools | [Module 01 Lab 02](<../01-intro-cs-taste/labs/lab-02-errors-tests-and-debugging.md>); GDB in [06 Lab 01](<../06-computer-architecture/labs/lab-01-reading-real-machine-code.md>); Valgrind in [07](<../07-systems-programming/overview.md>) | Every C build | Every C build is Valgrind-clean; you find a hot path with a profiler before guessing |
| **Testing**: unit, integration, property-based, TDD | [Module 01 Lab 02](<../01-intro-cs-taste/labs/lab-02-errors-tests-and-debugging.md>), [Module 02 Lab 02](<../02-programming-fundamentals/labs/lab-02-testing-and-git-workflow.md>) | Every build after that | Every project ships with a test suite that runs in one command |
| **CI/CD**: GitHub Actions, automated test pipelines, deployment | Outside the core (e.g. the [[OSS Project - Embeddable Typing Test (Monkeytype)\|OSS project]], stage S5) | All public repos | Every public repo goes green on push |
| **Containerization (Docker)**: Dockerfiles, docker-compose | Outside the core; learn it when a project needs a reproducible environment | From then on | Any project runs from a clean machine with one command |

## Rules
- Learn a tool when a module needs it, not before. No tooling rabbit holes (Operating Rule 7, Scope Control).
- Evidence is the repo: commits, green CI, passing tests. Not notes about tools.
