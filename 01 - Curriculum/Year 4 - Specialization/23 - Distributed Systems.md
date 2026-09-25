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
Labs 1–5 in Go: (1) MapReduce, (2) Raft consensus algorithm, (3) Fault-tolerant KV store on Raft, (4) Sharded KV store, (5) Concurrency optimizations.

---

## 🏁 Done When
> [!IMPORTANT]
> All labs pass 500 consecutive test runs without a single failure or race condition under `go test -race`.

---

## 📝 Study Notes, Psets & Proofs
*(Atomic notes, problem set proofs, and project notes)*

---

## 🔄 Appendix A Alternatives (Failover)
*Only consult if primary genuinely isn't working after two honest weeks:*
- Maarten van Steen & Andrew Tanenbaum, Distributed Systems (free); core distributed papers.
