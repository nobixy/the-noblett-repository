---
title: "21 - Databases — Worked Proofs"
type: reference
tags:
  - reference
  - answer-key
---

# 21 - Databases — Worked Proofs

> [!WARNING] Answer key — open only after your own attempt
> These derivations were generated as reference material, not study notes. Reading them first creates the illusion of competence that [[how-i-study]] warns about.
> Protocol: attempt the proof from a blank sheet in [[B21 - Databases|Databases]] → compare here → log every gap you found.
> They are unverified; treat any step you cannot justify as a possible error, not as authority.

Back to: [[B21 - Databases|Databases]] · [[Worked Proofs Index]]

---

### 1. Conflict vs. View Serializability & NP-Completeness
Let $T = \{T_1, \dots, T_n\}$ be a set of transactions. A schedule $S$ is a sequence of read ($r_i[x]$) and write ($w_i[x]$) operations conforming to the individual transaction orderings.

#### Conflict Serializability:
Two operations $o_i, o_j \in S$ are in *conflict* if they access the same data item $x$, belong to distinct transactions ($i \ne j$), and at least one is a write.
- A schedule $S$ is *conflict serializable* if it can be transformed into a serial schedule by a sequence of swaps of non-conflicting adjacent operations.
- **Precedence Graph (Serialization Graph) $\mathcal{P}(S)$:** A directed graph whose vertices are transactions $T_i$, with a directed edge $T_i \to T_j$ whenever an operation of $T_i$ precedes and conflicts with an operation of $T_j$.
- **Theorem:** Schedule $S$ is conflict serializable if and only if $\mathcal{P}(S)$ is an acyclic directed graph (DAG).
  *Proof:* If $\mathcal{P}(S)$ is acyclic, its topological sort defines a valid serial schedule $S_{serial}$ equivalent to $S$. If $\mathcal{P}(S)$ contains a cycle $T_1 \to T_2 \to \dots \to T_1$, any equivalent serial schedule would require $T_1$ to precede $T_2$ and $T_2$ to precede $T_1$, an impossibility. $\blacksquare$

#### View Serializability & Computational Complexity:
Two schedules $S$ and $S'$ are *view equivalent* ($S \approx_v S'$) if:
1. **Initial Reads:** For each item $x$, if $T_i$ reads the initial value of $x$ in $S$, then $T_i$ reads the initial value of $x$ in $S'$.
2. **Read-From Dependencies:** If $T_j$ reads the value written by $T_i$ on $x$ in $S$, then $T_j$ reads the value written by $T_i$ on $x$ in $S'$.
3. **Final Writes:** For each item $x$, if $T_k$ executes the final write on $x$ in $S$, then $T_k$ executes the final write on $x$ in $S'$.
A schedule $S$ is *view serializable* if it is view equivalent to some serial schedule.
- Conflict serializability is a strict subset of view serializability: $\text{Conflict-Serializable} \subset \text{View-Serializable}$.
- **Theorem (Papadimitriou 1979):** Deciding whether an arbitrary concurrent schedule $S$ is view serializable is **$\text{NP}$-complete**.
  *Proof Sketch:* Reduction from Monotone 3-SAT (or 3-SAT). The reduction maps Boolean variables and clauses to database transactions that perform "blind writes" ($w[x]$ without prior $r[x]$). Choosing which transaction executes the final write on shared dummy items forces a consistent truth assignment without violating read-from relations. Thus view serializability testing requires exhaustive search over all $n!$ serial schedules in the worst case. $\blacksquare$

---

### 2. ARIES Write-Ahead Logging (WAL) Correctness & Idempotence
**Protocol (Mohan et al. 1992):** Algorithms for Recovery and Isolation Exploiting Semantics (ARIES) guarantees ACID durability and atomicity through physiological logging and write-ahead logging invariants.

#### Core Structural Invariants:
1. **The WAL Protocol Invariant:**
   Before a dirty page $P$ in the volatile buffer pool is written to disk, the log record describing the update must be flushed to non-volatile disk storage:
   $$PageLSN(P) \le FlushedLSN$$
2. **Compensation Log Records (CLRs):**
   When an operation is rolled back during transaction abort or crash recovery, a CLR is written to the log. The CLR contains a pointer `UndoNextLSN` pointing to the `PrevLSN` of the update being undone. **CLRs are never undone**.

#### The Three Recovery Passes:
1. **Analysis Pass:**
   Scans the log forward from the most recent checkpoint.
  - Reconstructs the Transaction Table (TT) identifying active "loser" transactions at crash time.
  - Reconstructs the Dirty Page Table (DPT) identifying the earliest unwritten modification ($\min(RecLSN)$).
2. **Redo Pass ("Repeating History"):**
   Scans forward from $\min(RecLSN)$ to the physical end of the log.
  - Re-applies *all* logged changes (for both committed and uncommitted transactions) to restore the exact pre-crash system state.
  - Optimization: If $PageLSN \ge LSN$ on disk, the redo operation is skipped.
3. **Undo Pass:**
   Scans backward from the largest $LSN$ of active loser transactions in TT.
  - Undoes uncommitted operations in reverse chronological order.
  - When encountering a CLR, the undo engine directly follows `UndoNextLSN`, skipping already-undone actions.

#### Idempotence Proof (Resilience to Recurring Crashes):
**Theorem:** The ARIES recovery procedure is strictly idempotent: a crash occurring at any arbitrary point during Analysis, Redo, or Undo does not cause state divergence; re-running ARIES from the new crash state converges to the correct committed database state without cascading rollbacks.
- *Proof:*
  - A crash during Analysis simply restarts Analysis from the same checkpoint.
  - A crash during Redo: Since Redo updates $PageLSN$ on disk as pages are written, the subsequent Redo pass observes $PageLSN \ge LSN$ for already-applied records and skips them without re-execution.
  - A crash during Undo: Because every undone action appends a CLR with an explicit `UndoNextLSN` pointer, the subsequent recovery observes the CLRs written before the second crash. The new Undo pass skips all previously undone updates by jumping directly to `UndoNextLSN`. This guarantees that the undo frontier advances monotonically backward through the log, preventing infinite rollback cycles. $\blacksquare$

---

### 📄 Landmark Research Papers (from [[Paper Reading Hub|Paper Reading Hub]])

The following foundational papers from the [[Paper Reading Hub|Paper Reading Hub]] are assigned to Block 21. Analyze each using the Keshav Three-Pass Methodology:

1. **"ARIES: A Transaction Recovery Method Supporting Fine-Granularity Locking and Partial Rollbacks Using Write-Ahead Logging"** (C. Mohan et al., 1992)
    - *Venue:* ACM Transactions on Database Systems (Paper 24 in [[Paper Reading Hub|Paper Reading Hub]])
    - *Landmark Invariant:* Physiological logging, Compensation Log Records (CLRs), and repeating history during Redo to guarantee idempotent crash recovery.
    - *Reading Guidance:* Focus Pass 2 on the Analysis, Redo, and Undo passes, and the monotonic backward progression of `UndoNextLSN` pointers.
2. **"Spanner: Google's Globally Distributed Database"** (James C. Corbett et al., 2012)
    - *Venue:* OSDI '12 (Paper 25 in [[Paper Reading Hub|Paper Reading Hub]])
    - *Landmark Invariant:* External consistency (linearizability) across wide-area networks using TrueTime atomic/GPS uncertainty bounds ($2\epsilon$ commit-wait invariant).
    - *Reading Guidance:* Trace the TrueTime API bounds $[t.earliest, t.latest]$ and prove why commit-wait guarantees disjoint timestamps for causally related transactions.
