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

## SQL
- **SQLite's SQL reference** (sqlite.org/lang.html) and **Use The Index, Luke** (use-the-index-luke.com, free) — the best guide to how indexes and queries really interact.

## Video course

*Companions, not replacements: your labs and projects are the course. Watch with the [V protocol](../study-protocols.md#v--watch-actively) (pause, predict, then blank-sheet [R]), take lectures and quizzes as second explanations, and build this module's own projects, not the course's assignments. How courses fit your sessions: [study-protocols § Using video courses](../study-protocols.md#using-video-courses).*

**Primary — CMU 15-445/645 Intro to Database Systems**, CMU Database Group (Prof. Andy Pavlo). Free on YouTube: [lecture playlist](https://www.youtube.com/playlist?list=PLSE8ODhjZXjYDBpQnSymaectKjxCy6BYq) · [course site](https://15445.courses.cs.cmu.edu/fall2024/).
- **Why it fits:** the best free course on how a database engine is built inside: pages, buffer pool, B+trees, query execution, logging and ARIES recovery. That is Stratum's design, in the same order. Watch the lectures as second explanations; **don't** use its course projects or skeleton code. Stratum is your own design.

**Alternate — CS50's Introduction to Databases with SQL (CS50 SQL)**, Harvard (Carter Zenke). Free: [YouTube playlist](https://www.youtube.com/playlist?list=PLhQjrBD2T382v1MBjNOhPu9SiJ1fsD4C0) · [course site](https://cs50.harvard.edu/sql/).
- **Why:** taught with SQLite, the database this module's SQL lab and references use. Friendlier than 15-445's SQL lectures, and the right companion for Lab 01 if SQL is new to you.

### Lecture-to-vault map

15-445 numbers are the lecture numbers in the video titles.

| Vault item | CMU 15-445 (primary) | CS50 SQL (alternate) |
| :-- | :-- | :-- |
| [Lab 01 — SQL on your own data](labs/lab-01-sql-on-your-own-data.md) | #01 Relational Model & Algebra · #02 Modern SQL | Lecture 0 Querying · Lecture 1 Relating · Lecture 2 Designing · Lecture 3 Writing · Lecture 4 Viewing |
| [Lab 02 — What disks promise](labs/lab-02-what-disks-promise.md) | #03 Database Storage: Files & Pages · #06 Memory & Disk I/O Management · #20 Database Logging | — |
| [Stratum Storage](projects/stratum-storage/spec.md) (pages, buffer pool, B+tree) | #03 Database Storage: Files & Pages · #04 Log-Structured Merge Trees & Tuples · #06 Memory & Disk I/O Management · #08 Tree Indexes: B+Trees · #10 Index Concurrency Control | Lecture 5 Optimizing (indexes) |
| [Stratum Query & Recovery](projects/stratum-query-and-recovery/spec.md) (WAL, ARIES, planner, executor) | #11 Sorting & Aggregation Algorithms · #12 Join Algorithms · #13–14 Query Execution · #15 Query Planning & Optimization · #20 Database Logging · #21 Database Recovery with ARIES | Lecture 5 Optimizing (transactions) |

**Note:** CMU publishes a new playlist for each offering; the lecture topics are stable, so a later playlist is fine if this one moves.
