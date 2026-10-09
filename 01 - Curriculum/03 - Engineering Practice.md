---
title: "03 - Engineering Practice"
type: hub
tags:
  - hub
  - engineering
  - practice
---

# 03 - Engineering Practice

Applied tooling, building, testing, and operational skills that run parallel to theory. No separate block and no separate hours: each skill is learned inside the block that first needs it, then used in every block after. (Operating Rule 4 in [[00 - Start Here]].)

## Continuous Engineering Curriculum

| Skill | Learned in | Practice from then on | Done when |
| :--- | :--- | :--- | :--- |
| **Version Control (Git)**: branching, rebasing, resolving conflicts, semantic commits | [[Tooling\|P5 Tooling]] (Missing Semester) | `log.md` and every build live in git | You rebase and resolve a conflict without looking anything up |
| **Operating Systems (Linux)**: command line, shell scripting, permissions, processes | [[Tooling\|P5 Tooling]] (*How Linux Works* 1–7) | Every block; deepened in [[Operating Systems\|Block 16]] | You work a full week headless |
| **Debugging & Profiling**: GDB, Valgrind, flame graphs, browser DevTools | [[C Fluency\|Block 6]], [[Computer Systems\|Block 9]] | Every C/C++/Rust build | Every C build is Valgrind-clean; you find a hot path with a profiler before guessing |
| **Testing**: unit, integration, property-based, TDD | [[Software Construction\|Block 17]] | Every build after Block 17 | Every project ships with a test suite that runs in one command |
| **CI/CD**: GitHub Actions, automated test pipelines, deployment | [[Employability Portfolio and Review\|Portfolio]] project 3 | All public repos | Every public repo goes green on push |
| **Containerization (Docker)**: Dockerfiles, docker-compose | Year 3 writing deliverable (reproducible environments) | All code from Year 3 on | Any project runs from a clean machine with one command |

## Rules
- Learn a tool when a block needs it, not before. No tooling rabbit holes (Operating Rule 7, Scope Control).
- Evidence is the repo: commits, green CI, passing tests. Not notes about tools.
