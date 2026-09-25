---
block_id: "Block 21"
title: "Database Systems (CMU 15-445/645 & DDIA)"
term: "Year 3 Spring"
status: not-started
hours_estimate: 200
hours_actual: 0
primary_resource: "CMU 15-445/645 (Andy Pavlo) & Kleppmann, Designing Data-Intensive Applications"
milestone: "All 4 BusTub projects pass Gradescope; DDIA read cover to cover"
date_started: ""
date_completed: ""
---

# Block 21 — Database Systems (CMU 15-445/645 & DDIA)

> [!INFO] Block Overview
> - **Term / Position:** Year 3 Spring
> - **Estimated Hours:** ~200 hrs
> - **Status:** `not-started`
> - **Primary Resource:** CMU 15-445/645 (Andy Pavlo) & Kleppmann, Designing Data-Intensive Applications
> - **Key Milestone:** All 4 BusTub projects pass Gradescope; DDIA read cover to cover

---

## 🎯 Why This Block Matters
Databases are the apex software engineering system: memory management, disk I/O, concurrency control, query planning, recovery, and distributed replication.

---

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
All four CMU BusTub projects in C++: (1) Buffer Pool Manager, (2) B+ Tree Index, (3) Query Execution Engines & Hash Joins, (4) Concurrency Control (Lock Manager & MVCC).

---

## 🏁 Done When
> [!IMPORTANT]
> All four projects pass CMU Gradescope autograders with 100% test coverage.

---

## 📝 Study Notes, Psets & Proofs
*(Atomic notes, problem set proofs, and project notes)*

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- Berkeley CS186; Alex Petrov, Database Internals; the Red Book (redbook.io).
