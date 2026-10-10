---
block_id: "Block 21"
title: "Database Systems (CMU 15-445/645 & DDIA)"
category: "core"
subject: "Software Engineering"
term: "Year 3 Spring"
status: not-started
prerequisites:
  - "B16 - Operating Systems"
  - "B13 - Algorithms I"
hours_estimate: 200
hours_actual: 0
primary_resource: "CMU 15-445/645 (Andy Pavlo) & Kleppmann, Designing Data-Intensive Applications"
milestone: "All 4 BusTub projects pass Gradescope; DDIA read cover to cover"
date_started: ""
date_completed: ""
tier: "Tier 1 - Core"
optional: true # outside the hour budget since DR-005
job_ready: 5 # job-ready path, phase 5 (DR-003)
aliases: ["Databases"]
---

# Block 21 — Database Systems (CMU 15-445/645 & DDIA)

[[00 - Start Here|Start Here]] / [[00 - Start Here#The Path|The Path]] / [[Systems Index|Systems Index]]

> [!NOTE] Optional since [[DR-005 - Capstone and Maker Thread|DR-005]] (2026-10-09)
> Outside the hour budget, to make room for the Maker Labs, Block 19a and Block 24a within the DR-001 cap. Database internals are the least swarm-relevant 💼5 course; replication and partitioning stay core in Block 23 (DDIA). Do it before Track 2 or Track 10, or after the Capstone.

> [!INFO] Block Overview
> - **Term / Position:** Year 3 Spring
> - **Estimated Hours:** ~200 hrs
> - **Status:** `not-started`
> - **Primary Resource:** CMU 15-445/645 (Andy Pavlo) & Kleppmann, Designing Data-Intensive Applications
> - **Key Milestone:** All 4 BusTub projects pass Gradescope; DDIA read cover to cover

---

## 📚 Curriculum Tier: Tier 1 - Core
> **Tier 1 - Core**: Must complete before advancing.

## 🎯 Why This Block Matters
Databases are the apex software engineering system: memory management, disk I/O, concurrency control, query planning, recovery, and distributed replication.

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[B16 - Operating Systems|Operating Systems]]
- [[B13 - Algorithms I|Algorithms I]]


## 📖 Primary Syllabus & Core Content
- [ ] Relational model, relational algebra, SQL
- [ ] Database storage architecture: Buffer pools, slotted pages, log-structured storage
- [ ] Index concurrency and structures: B+ trees, hash indexes
- [ ] Query execution: Volcano iterator model, vectorization, hash joins, sorting
- [ ] Query optimization: Cost-based optimization, system-R, rules
- [ ] Concurrency control: Two-Phase Locking (2PL), MVCC, snapshot isolation, serializability
- [ ] Crash recovery: ARIES, write-ahead logging (WAL), checkpoints
- [ ] Read Kleppmann, Designing Data-Intensive Applications cover to cover

---

## 🛠️ Build Requirement
Implement all four CMU BusTub projects in `c++` using `cmake`, debugged with `gdb`, tested with GoogleTest and `sql` validation suites: (1) Buffer Pool Manager with LRU-K eviction, (2) B+ Tree Index with concurrent lock crabbing, (3) Query Execution Engines & Hash Joins under the Volcano model, (4) Concurrency Control with Two-Phase Locking and Multi-Version Concurrency Control (MVCC).

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> All four projects pass CMU Gradescope autograders with 100% test coverage.

---

## 🔎 Verified Resources (DR-004, checked 2026-10-09)
**Verdict:** UPGRADE. Uses the public autograder.
- **CMU 15-445** (Fall 2025 site; Fall 2026 is live): 15445.courses.cs.cmu.edu/fall2025/. The course FAQ lists a public Gradescope for non-CMU students (autograders open after CMU due dates; keep your solutions private, as the FAQ asks). Lectures on the CMU-DB YouTube channel.
- 💲 DDIA; free alternative: the Red Book (redbook.io) and the 15-445 lectures.

---

## 📝 Study Notes, Psets & Proofs

*Your atomic notes, problem-set proofs, and build notes go here — written by you, from a blank page.*

> [!TIP]- Check your work (only after your own blank-sheet attempt)
> BusTub's local tests, then the Gradescope autograder.

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- Berkeley CS186; Alex Petrov, Database Internals; the Red Book (redbook.io).

---

## ➡️ Next Steps
- **Topic Hub:** [[Systems Index|Systems Index]] | [[00 - Start Here#The Path|The Path]]
- **Sequential Flow:** [[B20 - Algorithms II|← Algorithms II]] | [[00 - Start Here|Start Here]] | [[B21a - Maker Lab 5 - PCB Design|Maker Lab 5 →]]
