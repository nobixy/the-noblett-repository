---
title: "Project: Stratum Query and Recovery"
id: "MOD11-PRJ-stratum-query-and-recovery"
type: "project"
module: "11-databases"
phase: "D"
order: 1350
prerequisites: [MOD11-PRJ-stratum-storage, MOD06-PRJ-ember-compiler]
artifact: "The upper half of Stratum: a write-ahead log with transactions and crash recovery proven under thousands of injected crashes; StratumQL (a SQL subset) with a parser, a planner that chooses index scans and join methods, an iterator executor, EXPLAIN, and a REPL — differentially tested against SQLite"
deliverable: "Design doc + recovery testing report + StratumQL reference + query-engine test report + short demo"
---

# Project: Stratum Query and Recovery

| | |
| :-- | :-- |
| **Module** | 11 Databases |
| **Prerequisites** | [Stratum Storage](../stratum-storage/spec.md); Lab 02 (fault injection); Ember (parsers and interpreters); Lab 01 (SQL and operator trees) |
| **You build** | The two things that make storage a database. **Recovery:** transactions that are all-or-nothing and durable, using a write-ahead log, tested by crashing the engine thousands of times at random moments. **Queries:** StratumQL, a small SQL, with a parser, a planner that decides how to run each query (and uses your B+tree when it helps), an executor that streams rows through a tree of operators, and `EXPLAIN` to show the plan — checked against SQLite on thousands of random queries |
| **Deliverable** | Design doc, two test reports, a language reference, and a demo |

---

## Why this matters

Your Lab 02 experiments showed that disks lose unsynced writes and can tear pages. Yet banks and hospitals trust databases with data that must never be lost or half-written. The technique that makes this possible — **write-ahead logging** with **recovery** — is one of the great ideas in systems, and you've been circling it since Study Deck's append-only log and Tagfs's journal. Here you make it rigorous, and you prove it works the only convincing way: by crashing it relentlessly.

On top, a query language turns your storage engine into something people can use. Parsing, planning, and executing queries ties together every compiler-ish skill you have (Ember, Worldfile, Truth Engine) with the operator trees from Lab 01.

**Real-world analogs:** ARIES-style recovery in DB2, SQL Server, PostgreSQL's WAL; SQLite's WAL mode; the Volcano iterator model used by most query engines.

---

## Part A — Transactions and recovery

### The rules you'll implement

- A **transaction** is a group of changes that must happen **all or nothing** (atomicity) and, once committed, must survive crashes (durability).
- **Write-ahead rule:** a log record describing a change must reach stable storage **before** the changed page does.
- **Commit rule:** a transaction is committed when its COMMIT log record is **fsynced**.
- **Log records:** `BEGIN t`, `INSERT t page slot after-image`, `DELETE t page slot before-image`, `UPDATE t page slot before after`, `COMMIT t`, `ABORT t`, `CHECKPOINT …` — each with an **LSN** (log sequence number), a length, and a CRC32.
- **Page LSN:** each page records the LSN of the last log record applied to it, so recovery knows whether a change is already on the page.

### The big design decision [W]

| Buffer policy | Meaning | Recovery needs |
| :-- | :-- | :-- |
| **No-steal** | dirty pages of uncommitted transactions are never written to disk | **redo only** (uncommitted changes never reach disk) — simpler, but transactions must fit in memory |
| **Steal** | the buffer pool may write any dirty page | **undo** too (uncommitted changes may be on disk) — the general case |
| **Force** | all of a transaction's pages written at commit | slow commits, simple recovery |
| **No-force** | pages written later | redo needed |

**Start with no-steal / no-force (redo-only recovery).** Then, as the stretch-sized final milestone, implement steal with undo. Defend the choices in the design doc.

### Milestone 1 — Design doc and the log

1. **Design doc v1** (5 pages): the transaction model (one transaction at a time to begin with — concurrency is a stretch goal), log record formats, the WAL and commit rules, buffer policy, recovery algorithm, checkpointing, and the crash-testing harness.
2. **Log manager:** append records (buffered), `flush(up_to_lsn)` with fsync, read records forward, detect a torn final record by CRC.
3. **Transactions:** `begin()`, `commit()` (append COMMIT, flush the log), `abort()` (undo in memory using before-images — easy under no-steal).

### Milestone 2 — Redo recovery and checkpoints

1. **Recovery:** on open, scan the log from the last checkpoint; find committed transactions; **redo** each committed change whose LSN is greater than the page's LSN; ignore uncommitted ones.
2. **Checkpoints:** periodically flush all dirty pages of committed work, write a CHECKPOINT record, and allow truncating the log before it.
3. Tests: committed data present after a clean restart; uncommitted absent.

### Milestone 3 — Crash testing (the heart of Part A)

Using Lab 02's **fault-injecting file layer** under both the data file and the log:
1. Run a random workload of transactions (inserts, updates, deletes, aborts) against Stratum **and** against an in-memory model that applies only committed transactions.
2. At a random moment (a random write or sync number), **crash**: drop all unsynced writes; optionally tear the last page written.
3. Reopen (run recovery). Check: the database equals the model **as of the last successful commit**; all B+tree and page invariants hold; every checksum verifies.
4. Repeat **5,000 times** with different seeds. Every failure is saved with its seed, shrunk, fixed, and kept as a regression test.

**Done when:** 5,000 crashes, zero failures.

**Checkpoint:** [Milestone Checkpoint](<../../../04 - System/Milestone Checkpoint Template.md>). Feynman target: *why the write-ahead rule makes crashes safe*. Why-ladder target: *why must the B+tree's splits also be logged?* (What happens if a split's two new pages reach disk but the parent's update doesn't?)

### Milestone 4 (stretch-sized) — Steal and undo

Allow the buffer pool to evict uncommitted dirty pages (after flushing the log up to their page LSN — the WAL rule). Recovery gains an **undo** pass that rolls back uncommitted transactions using before-images, writing **compensation log records** so that a crash *during* recovery is also safe. Re-run the 5,000-crash campaign. This is the core of the ARIES algorithm — read the paper's introduction after building your version.

---

## Part B — StratumQL

### The language (write the exact grammar in `STRATUMQL.md`)

```sql
CREATE TABLE review (id INT PRIMARY KEY, card TEXT, day TEXT, grade TEXT);
CREATE INDEX review_day ON review (day);
INSERT INTO review VALUES (1, 'm04-euclid-why', '2027-02-01', 'good');
SELECT card, COUNT(*) FROM review WHERE grade = 'again' GROUP BY card ORDER BY 2 DESC LIMIT 10;
SELECT r.day, c.deck FROM review r JOIN card c ON r.card = c.id WHERE r.day >= '2027-01-01';
UPDATE review SET grade = 'hard' WHERE id = 1;
DELETE FROM review WHERE day < '2026-01-01';
BEGIN; …; COMMIT;   ROLLBACK;
EXPLAIN SELECT …;
```

Types: INT, TEXT (and REAL as a stretch). Expressions: comparisons, AND/OR/NOT, arithmetic, `IS NULL`, string equality. Aggregates: COUNT, SUM, MIN, MAX, AVG with GROUP BY. NULL semantics: decide how much of SQL's three-valued logic you implement and document it (Module 03's truth tables — now with a third value!).

### Milestone 5 — Parser and binder

1. Lexer and recursive-descent parser (your fifth: Worldfile, Truth Engine, Ember, Glimpse's CSS — reuse your patterns) into an AST, with precise errors.
2. **Binder:** resolve table and column names against the catalog (with aliases), check types, and report errors like a real database (`no such column: r.dya`).

### Milestone 6 — Executor: the iterator model

Each operator has `open()`, `next() → row or None`, `close()`. Operators:
- **SeqScan** (heap file), **IndexScan** (B+tree point or range lookup → fetch rows by RID),
- **Filter**, **Project**, **Limit**,
- **Sort** (in memory; external merge sort for data bigger than a memory budget as a stretch — Module 05's merge),
- **HashAggregate** (GROUP BY with a hash map),
- **NestedLoopJoin**, **IndexNestedLoopJoin** (look up each outer row's key in the inner table's index), **HashJoin** (build a hash table on the smaller input).

`EXPLAIN` prints the operator tree with estimated row counts.

### Milestone 7 — The planner

1. Build a plan tree from the AST: scans → joins → filter → aggregate → sort → project → limit.
2. **Push filters down** below joins when they only mention one table (Lab 01 Session 4's question).
3. **Choose an IndexScan** when a WHERE condition on an indexed column is an equality or a range with constants.
4. **Choose a join method** using simple statistics you keep in the catalog (row counts per table; distinct counts per indexed column): e.g. index nested loop when the inner side has an index on the join key and the outer side is small; hash join otherwise. Write down your cost formulas [W] and compare their predictions with measured times on three queries.

### Milestone 8 — Differential testing, the REPL, and your data

1. **Differential testing against SQLite:** generate random schemas, random data (with NULLs and duplicates), and random queries in the common subset of StratumQL and SQLite; run each in both; compare result **multisets** (or ordered lists when ORDER BY fully determines order). 10,000 queries; shrink and keep failures.
2. **REPL:** `stratum mydb.db` with a prompt, multi-line statements, results as aligned tables, timing, and `.tables` / `.schema` meta-commands.
3. **Your data:** load your Lab 01 study data into Stratum and run your eight Lab 01 queries (adapted). Compare answers and times with SQLite.

---

## Testing guidance

- **Crash campaign** (Part A) and **differential query campaign** (Part B) are the two pillars; both seeded, both shrinking failures into regressions.
- **Plan tests:** for chosen queries, assert the plan shape (e.g. "uses IndexScan on review_day").

## Common pitfalls

- **Logging after modifying the page** (violates the WAL rule) — the crash campaign will find it.
- **Forgetting the directory fsync** when the database or log file is first created.
- **B+tree structure changes not logged** (splits) — corruption after crashes.
- **NULL comparisons** (`NULL = NULL` is not true in SQL).
- **Iterator resource leaks** (pinned pages left by operators that weren't closed).

## Communication deliverable

1. **Design doc** v1 → v2 (with the recovery argument written as carefully as a proof — Module 03).
2. **Recovery testing report** (2 pages): the harness, crash counts, failures found and fixed, the steal/undo results if done.
3. **`STRATUMQL.md`** — the language reference, including NULL semantics and differences from SQLite.
4. **Query-engine test report** (2 pages): differential testing, planner choices vs measurements, your-data comparison.
5. **Demo:** the REPL on your study data, EXPLAIN showing an index plan, then a crash-and-recover run with a live count of verified crashes.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | WAL and commit rules, recovery passes, operator interfaces — from memory |
| **F** | The write-ahead rule; one query flowing through iterators |
| **W** | Steal/force choices; logging splits; join cost formulas; NULL semantics |
| **S** | Recovery and planner subgoals |
| **I** | Systems, languages, and testing in one project |
| **D** | Recovery bugs: reproduce from the seed first, then reason |
| **T** | Design doc, two reports, language reference, demo |

## Stretch goals

- **Concurrency:** multiple transactions with two-phase locking (row or page locks), deadlock detection (a cycle in the waits-for graph — Module 05 DFS), and tests with threads.
- **MVCC:** readers see a snapshot without blocking writers.
- **Group commit:** batch fsyncs across transactions; measure commits per second.
- **Lantern endpoint:** serve query results over HTTP (capstone building block).

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Log and transactions | CRC'd records; commit/abort; checkpoints | Works | Missing pieces |
| Recovery | 5,000 injected crashes clean (steal/undo is extra credit) | Fewer crashes | Untested |
| Parser and binder | Full grammar; precise errors | Works | Fragile |
| Executor | All listed operators incl. three joins and aggregates | Most | Scans only |
| Planner | Pushdown, index selection, cost-based join choice, measured | Some | Fixed plans |
| Differential testing | 10,000 random queries agree with SQLite | Hand queries | None |
| Communication | Doc, reports, reference, demo | Most | Few |

**Done when:** every area at least 2; Recovery and Differential testing at 3.

## Connections

- **Back:** Stratum Storage, Lab 02, Study Deck and Tagfs (logs), Ember (front end), Lab 01 (SQL and operator trees), Module 03 (proof-style reasoning; three-valued logic), Module 05 (hash joins, merge sort).
- **Forward:** [13 Capstone](../../../13-capstone/overview.md).

> **Originality note:** Stratum's query language subset, recovery design path (no-steal first, then steal with undo), crash-testing harness, and milestones were designed for this curriculum.
