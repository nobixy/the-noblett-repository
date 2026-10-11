---
title: "11 — Resources"
id: "MOD11-RES"
type: "reference"
module: "11-databases"
phase: "D"
order: 1360
prerequisites: []
---

# 11 — Resources

*Pointers only. Stratum is the course.*

## Books
- **Martin Kleppmann, *Designing Data-Intensive Applications*** (book) — chapter 3 (storage and retrieval: logs, B-trees, LSM-trees) and chapter 7 (transactions) are the best readable companions to this module.
- **Ramakrishnan & Gehrke, *Database Management Systems*** (book) — the classic textbook on buffer management, B+trees, query evaluation, and recovery.
- **Petrov, *Database Internals*** (book) — Part I (storage engines, B-trees, buffer management, logging) is very practical.

## Papers and primary sources
- **Bayer & McCreight, "Organization and Maintenance of Large Ordered Indexes" (1972)** — the original B-tree paper.
- **Mohan et al., "ARIES: A Transaction Recovery Method…" (1992)** — read the introduction and overview after Part A's Milestone 4.
- **Graefe, "Volcano — An Extensible and Parallel Query Evaluation System" (1994)** — the iterator model.
- **SQLite documentation:** "Atomic Commit In SQLite," "Write-Ahead Logging," "The SQLite Query Optimizer Overview," and "Database File Format" (sqlite.org) — superb, honest engineering writing.

## Lectures (second explanations)
- **CMU 15-445 Database Systems** lectures (Andy Pavlo, YouTube) — excellent on buffer pools, B+trees, query execution, and recovery. Watch lectures as second explanations; **don't** use its course projects or skeleton code — Stratum is your own design.

## SQL
- **SQLite's SQL reference** (sqlite.org/lang.html) and **Use The Index, Luke** (use-the-index-luke.com, free) — the best guide to how indexes and queries really interact.

## Video and course companions
Free YouTube series and Coursera/edX/MIT OCW courses for this module are listed in [courses-and-videos.md](../courses-and-videos.md#modules-0113). Use them with the [V protocol](../study-protocols.md#v--watch-actively): lectures and quizzes as second explanations; this module's own projects, not the courses' assignments.
