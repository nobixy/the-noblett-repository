---
block_id: "Block 23"
title: "Distributed Systems (MIT 6.5840 / 6.824)"
term: "Year 4 Fall"
status: not-started
hours_estimate: 220
hours_actual: 0
primary_resource: "MIT 6.5840 (Robert Morris) & Martin Kleppmann Cambridge Lectures"
milestone: "All Go labs pass 500 consecutive runs under go test -race"
date_started: ""
date_completed: ""
---

# Block 23 — Distributed Systems (MIT 6.5840 / 6.824)

[[00 - Dashboard|Dashboard]] / [[Checklist|Checklist]] / [[02 - Notes/Systems/Systems Index|Systems Index]]

> [!INFO] Block Overview
> - **Term / Position:** Year 4 Fall
> - **Estimated Hours:** ~220 hrs
> - **Status:** `not-started`
> - **Primary Resource:** MIT 6.5840 (Robert Morris) & Martin Kleppmann Cambridge Lectures
> - **Key Milestone:** All Go labs pass 500 consecutive runs under go test -race

---

## 🎯 Why This Block Matters
How multiple computers collaborate, achieve consensus, and survive arbitrary machine failures and network partitions.

---

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

## 🏁 Done When
> [!IMPORTANT]
> All labs pass 500 consecutive test runs without a single failure or race condition under `go test -race`. Proofs below are mastered and verified against the implementation state machine.

---

## 📝 Study Notes, Psets & Proofs

*Your atomic notes, problem-set proofs, and build notes go here — written by you, from a blank page.*

> [!TIP]- Answer key (open only after a blank-sheet attempt)
> [[23 - Distributed Systems — Worked Proofs]]

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- Maarten van Steen & Andrew Tanenbaum, Distributed Systems (free); core distributed papers.

---

## 🧭 Navigation
- **Topic Hub:** [[02 - Notes/Systems/Systems Index|Systems Index]] | [[Checklist|Master Checklist]]
- **Sequential Flow:** [[01 - Curriculum/Year 3 - Depth/22 - Statistics|← 22 - Statistics]] | [[00 - Dashboard|Dashboard]] | [[01 - Curriculum/Year 4 - Specialization/24 - Theory of Computation|24 - Theory of Computation →]]
