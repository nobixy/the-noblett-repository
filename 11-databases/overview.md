---
title: "11 — Databases"
module: "11-databases"
hours: 170
tags: [module, databases, storage]
---

# 11 — Databases

**Store data so it's fast to find and impossible to lose.** You'll use SQL seriously on your own study data, run experiments on what disks actually guarantee, and then build **Stratum**, a small database engine from the bottom up: a page file, slotted pages, a buffer pool, a B+tree index, a write-ahead log with crash recovery that you test by "pulling the plug" thousands of times, and a SQL-like query language with a parser, a planner that uses indexes, and an iterator-based executor — checked against SQLite.

---

## Prerequisites

- [05 DSA](../05-data-structures-and-algorithms/overview.md) (trees, hash maps, sorting, measurement).
- [07 Systems Programming](../07-systems-programming/overview.md) (binary formats, fsync, Crate) and [08 OS](../08-operating-systems/overview.md) (Tagfs's journal; caching).
- [06 Cache Simulator](../06-computer-architecture/projects/cache-sim/spec.md) (replacement policies return as buffer pools).
- Module 03 Unit 4 (sets and relations).

## Objectives

By the end you will be able to:
1. Design a relational schema, write SQL with joins and aggregates, and read query plans.
2. Explain what `write`, `fsync`, and `rename` guarantee on a real system, and design for crashes.
3. Implement page-based storage with slotted pages and a buffer pool with a replacement policy.
4. Implement a B+tree with search, insertion with splits, range scans, and an invariant checker.
5. Implement write-ahead logging and crash recovery, and test it with fault injection.
6. Implement a query language: parser, planner (index selection), and iterator executor with joins.
7. Measure your engine against SQLite and explain the differences.

## Sequence and time

| Order | Item | Hours | Concepts |
| :-- | :-- | --: | :-- |
| 1 | [Lab 01 — SQL on Your Own Data](labs/lab-01-sql-on-your-own-data.md) | 12 | schemas, keys, joins, aggregates, indexes, EXPLAIN |
| 2 | [Lab 02 — What Disks Promise](labs/lab-02-what-disks-promise.md) | 8 | write vs fsync, atomic rename, torn writes, SQLite's journals |
| 3 | **[Stratum Storage](projects/stratum-storage/spec.md)** | 70 | pages, slotted pages, records, buffer pool, B+tree, catalog |
| 4 | **[Stratum Query and Recovery](projects/stratum-query-and-recovery/spec.md)** | 80 | WAL, recovery, fault injection, StratumQL, planner, executor, differential testing |
| | **Total** | **~170** | |

About 12 hours a week → 14 weeks. Language: **Python** is recommended (clarity — the ideas are the point; performance targets are set for Python) or C (for the brave; Crate and Heapsmith prepared you).

## How the study methods run through this module

| Protocol | In this module |
| :-- | :-- |
| **R** | Draw a slotted page, a B+tree split, the WAL protocol, and an iterator plan from memory before each milestone. Study Deck cards for SQL syntax, recovery rules, and B+tree invariants. |
| **F** | Recorded explanations: why a B+tree stays shallow; the write-ahead rule; how a query plan executes one row at a time. |
| **W** | Steal/no-steal and force/no-force decisions; page size; replacement policy; join algorithms — each defended with measurements. |
| **S** | Subgoals for insert-with-split, recovery passes, and each executor operator. |
| **I** | SQL practice mixed with building the engine that runs it. |
| **D** | Recovery bugs appear only after crashes: deterministic fault injection makes them repeatable; stuck notes for the rest. |
| **T** | Design docs, a file-format spec, a recovery-testing report, a benchmark report, demos. |

## Connections

- **Back:** Study Deck and Tagfs (append-only logs, replay), Crate (page-like binary formats, CRCs, fsync, fuzzing), Cache Simulator (LRU/CLOCK), Vault Search (indexes, hash tables), Ember/Worldfile (parsers), Module 05 (B-trees' cousins: BSTs and heaps; sorting; merging).
- **Forward:** [13 Capstone](../13-capstone/overview.md) — Lantern's dynamic pages backed by Stratum.

## Module close

1. **Cumulative retrieval [R] (60 min):** from `INSERT` in the REPL to bytes on disk and back after a crash — every layer on one page.
2. **Rewrite [Explain-a-System](../00-foundations/english/projects/explain-a-system/spec.md) explainer 5** (the bank account and the power cut) from scratch, using your own engine's design as the example.
3. **Showcase [T]:** a 5-minute demo: your study data in Stratum, a query plan using an index, and a crash-and-recover run.
4. Tick the module in [Start Here](<../00 - Start Here.md>).

**Next:** [12 Math for Engineering](../12-math-for-engineering/overview.md) (if not running already) and [13 Capstone](../13-capstone/overview.md).
