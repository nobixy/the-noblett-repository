---
block_id: "Block 23"
title: "Distributed Systems (MIT 6.5840 / 6.824)"
category: "core"
subject: "Software Engineering"
term: "Year 4 Fall"
status: not-started
prerequisites:
  - "B19 - Networking"
hours_estimate: 220
hours_actual: 0
primary_resource: "MIT 6.5840 (Robert Morris) & Martin Kleppmann Cambridge Lectures"
milestone: "All Go labs pass 500 consecutive runs under go test -race"
date_started: ""
date_completed: ""
tier: "Tier 1 - Core"
job_ready: 5 # job-ready path, phase 5 (DR-003)
aliases: ["Distributed Systems"]
---

# Block 23 — Distributed Systems (MIT 6.5840 / 6.824)

[[00 - Start Here|Start Here]] / [[00 - Start Here#The Path|The Path]] / [[Systems Index|Systems Index]]

> [!INFO] Block Overview
> - **Term / Position:** Year 4 Fall
> - **Estimated Hours:** ~220 hrs
> - **Status:** `not-started`
> - **Primary Resource:** MIT 6.5840 (Robert Morris) & Martin Kleppmann Cambridge Lectures
> - **Key Milestone:** All Go labs pass 500 consecutive runs under go test -race

---

## 📚 Curriculum Tier: Tier 1 - Core
> **Tier 1 - Core**: Must complete before advancing.

## 🎯 Why This Block Matters
How multiple computers collaborate, achieve consensus, and survive arbitrary machine failures and network partitions.

---

## 🔗 Prerequisites
*What must you have mastered before starting this block?*
- [[B19 - Networking|Networking]]


## 📖 Primary Syllabus & Core Content
- [ ] RPC, threads, concurrency, and event-driven architecture
- [ ] Fault tolerance: Primary-backup replication, state machine replication
- [ ] Consensus: Raft protocol, leader election, log replication, safety invariants
- [ ] Fault-tolerant key/value service
- [ ] Sharded key/value service with dynamic shard configuration transfer
- [ ] Classical papers: Lamport 'Time, Clocks', Paxos Made Simple, MapReduce, GFS, Bigtable, Spanner

---

## 🛠️ Build Requirement
Complete the MIT 6.5840 / 6.824 distributed systems laboratory suite in `go` orchestrated with `bash`, `python`, `git`, and `make`:
1. **Lab 1 (MapReduce)**: Multi-threaded worker and master coordination with RPC heartbeats, dynamic worker failure recovery, and deterministic file outputs.
2. **Lab 2 (Raft Consensus)**: Full consensus engine with randomized election timers, leader heartbeats, log replication RPCs, persistence to disk, and log compaction via snapshotting.
3. **Lab 3 (Fault-Tolerant KV Service)**: Linearizable key-value storage built atop Raft, handling duplicate RPC detection via client session IDs, snapshotting, and leader re-election churn.
4. **Lab 4 (Sharded KV Service)**: Dynamic multi-raft shard controller with incremental config migrations, linearizable cross-shard handoffs, and garbage collection of stale shards.
5. **Toolchain & Verification**: Automated stress tests run via `go test -race -count=500` under simulated network partitions, asynchronous delays, and random process crashes injected via `python` chaos scripts and `bash` test runners.

---

## 🏁 Mastery Criteria & Assessments
> [!IMPORTANT]
> All labs pass 500 consecutive test runs without a single failure or race condition under `go test -race`. Proofs below are mastered and verified against the implementation state machine.

---

## 🔎 Verified Resources (DR-004, checked 2026-10-09)
**Verdict:** KEEP.
- **MIT 6.5840** (Spring 2026; labs ship Go test suites): pdos.csail.mit.edu/6.5840/.

---

## 📝 Study Notes, Psets & Proofs

*Your atomic notes, problem-set proofs, and build notes go here — written by you, from a blank page.*

> [!TIP]- Check your work (only after your own blank-sheet attempt)
> The labs' `go test` suites, run repeatedly with `-race` (*Done when*: 500 consecutive passes).

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- Maarten van Steen & Andrew Tanenbaum, Distributed Systems (free); core distributed papers.

---

## ➡️ Next Steps
- **Topic Hub:** [[Systems Index|Systems Index]] | [[00 - Start Here#The Path|The Path]]
- **Sequential Flow:** [[B22a - Machine Learning|← Machine Learning]] | [[00 - Start Here|Start Here]] | [[B23a - Parallel Computing|Parallel Computing →]]
