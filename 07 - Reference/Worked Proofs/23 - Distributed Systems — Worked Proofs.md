---
title: "23 - Distributed Systems — Worked Proofs"
type: reference
tags:
  - reference
  - answer-key
---

# 23 - Distributed Systems — Worked Proofs

> [!WARNING] Answer key — open only after your own attempt
> These derivations were generated as reference material, not study notes. Reading them first creates the illusion of competence that [[how-i-study]] warns about.
> Protocol: attempt the proof from a blank sheet in [[23 - Distributed Systems]] → compare here → log every gap you found.
> They are unverified; treat any step you cannot justify as a possible error, not as authority.

Back to: [[23 - Distributed Systems]] · [[Worked Proofs Index]]

---

### Proof 1: Raft Consensus State Machine Safety Invariant
**Theorem (State Machine Safety)**: In the Raft consensus protocol, if a server has applied a log entry at a given index $k$ to its state machine, no other server will ever apply a different log entry for the same index $k$.

**Formal Protocol Lemmas**:
1. **Election Safety**: At most one leader can be elected in a given term $T$.
  - *Proof*: Electing a leader requires a majority vote ($> N/2$ servers). Any two majorities must overlap by at least one server. Since each server casts at most one vote per term, two distinct leaders cannot receive majorities in the same term $T$.
2. **Leader Append-Only**: A leader never overwrites or truncates its own log entries; it only appends new entries.
3. **Log Matching Property**: If two logs contain an entry with the same index $i$ and term $t$:
  - The entries store the same command.
  - The logs are identical in all entries up through index $i$.
  - *Proof by Induction on $i$*:
    - *Base Case ($i=1$)*: Follows trivially from Election Safety and single-entry commit.
    - *Inductive Step*: The leader AppendEntries consistency check verifies that the follower's log contains an entry at $(i-1)$ with matching term before appending entry $i$. If the follower accepts, then by induction its log matches the leader's up to $i-1$, and now includes entry $i$.
4. **Leader Completeness Property**: If a log entry is committed in term $T$, then that entry will be present in the logs of the leaders for all higher terms $U > T$.
  - *Proof by Contradiction and Induction on Term Difference $(U - T)$*:
    - Suppose an entry $e = (index, term = T)$ is committed in term $T$, but some leader $L_U$ for term $U > T$ does not possess $e$ in its log.
    - Let $U$ be the *smallest* term greater than $T$ whose leader $L_U$ lacks $e$.
    - Because $e$ was committed in term $T$, it must have been stored on a majority of servers $S_{commit}$.
    - Because $L_U$ was elected leader in term $U$, it must have received votes from a majority of servers $S_{vote}$.
    - By the pigeonhole principle, $S_{commit} \cap S_{vote} \ne \emptyset$. There exists at least one voter $V \in S_{commit} \cap S_{vote}$.
    - Server $V$ accepted entry $e$ during term $T$, and also voted for $L_U$ in term $U$.
    - Since $V$ accepted $e$ before voting for $L_U$, $V$'s log contained $e$ when it evaluated the RequestVote RPC from $L_U$.
    - Raft's voting rule dictates that a voter $V$ grants a vote to candidate $L_U$ only if $L_U$'s log is at least as up-to-date as $V$'s log:
       $$\text{lastTerm}(L_U) > \text{lastTerm}(V) \quad \lor \quad (\text{lastTerm}(L_U) == \text{lastTerm}(V) \land \text{len}(L_U) \ge \text{len}(V))$$
    - If $\text{lastTerm}(V) == T$, then since $V$ contains entry $e$ (at least at index $k$), $L_U$'s last term must be at least $T$. If $L_U$'s last term is $T$, $L_U$'s log must be at least as long as $V$'s, meaning $L_U$ contains all entries of term $T$ up through $k$, so $L_U$ contains $e$. Contradiction.
    - If $\text{lastTerm}(V) > T$, say $T' \in (T, U)$, then $V$'s log contains an entry created by leader $L_{T'}$. Since $T' < U$, by the inductive hypothesis, leader $L_{T'}$ contained entry $e$. By the Log Matching Property, $V$ retained entry $e$. For $L_U$ to have a more up-to-date log than $V$, $L_U$'s last term must be $\ge T'$, meaning $L_U$ received its tail entries from a leader that already preserved $e$. Contradiction.
    - Therefore, leader $L_U$ must contain entry $e$.

**Main Proof**:
From Leader Completeness, any committed entry $e$ at index $k$ persists across all subsequent leaders. Since servers only apply entries to their state machines once committed or verified through a leader's log matching invariant, every server that applies an entry at index $k$ will apply the unique entry $e$ guaranteed by the Leader Completeness and Log Matching properties. Hence, State Machine Safety holds. $\blacksquare$

---

### Proof 2: Byzantine Fault Tolerance Lower Bound ($3f + 1$)
**Theorem (Pease, Shostak, Lamport 1980)**: In a synchronous distributed system with unauthenticated point-to-point communication, consensus among $n$ processes is impossible in the presence of $f$ Byzantine (arbitrary) faulty processes if $n \le 3f$.

**Proof for $n=3, f=1$**:
1. Consider a 3-process system $P = \{A, B, C\}$ where at most one process can be Byzantine ($f=1$). Each correct process starts with an initial binary input $v \in \{0, 1\}$ and must decide a value $d \in \{0, 1\}$ satisfying:
  - **Agreement**: All non-faulty processes decide the same value.
  - **Validity**: If all non-faulty processes start with value $v$, they must decide $v$.
2. Assume towards contradiction that there exists a deterministic consensus protocol $\Pi$ that succeeds for $n=3, f=1$.
3. We construct a 6-node virtual system graph $G = (A_0, B_0, C_0, A_1, B_1, C_1)$ arranged in a cycle:
   $$A_0 - B_0 - C_0 - A_1 - B_1 - C_1 - A_0$$
   where subscript indicates initial input (e.g., $A_0$ runs protocol $\Pi$ with input 0; $B_1$ runs $\Pi$ with input 1).
4. Each node communicates only with its two adjacent neighbors along the cycle using protocol $\Pi$.
5. Notice that from the perspective of any pair of adjacent nodes $(X, Y)$:
  - The messages exchanged between $X$ and $Y$ are identical to a real 3-node execution where the third process $Z$ is Byzantine and lies to $X$ as if it were on the left side of the cycle, and lies to $Y$ as if it were on the right side of the cycle.
6. Specifically:
  - Consider edge $(A_0, B_0)$: Both have input 0. In a real 3-node system with correct nodes $\{A, B\}$ with input 0 and Byzantine node $C$, $C$ could simulate $(C_1, A_1, B_1, C_0)$ and send messages to $A$ as $C_1$ and to $B$ as $C_0$. By the **Validity** property of $\Pi$, both $A_0$ and $B_0$ must decide **0**.
  - By symmetric reasoning on edge $(A_1, B_1)$: Both have input 1. With a Byzantine $C$, Validity forces $A_1$ and $B_1$ to decide **1**.
  - By transitivity along the cycle:
    - For edge $(B_0, C_0)$: Under Byzantine $A$, Validity forces $B_0$ and $C_0$ to decide **0**.
    - For edge $(C_0, A_1)$: $C_0$ decides 0. But by Agreement, in a system where $C$ and $A$ are correct with $B$ Byzantine, $C_0$ and $A_1$ must agree! Since $C_0$ decides 0, $A_1$ must decide 0.
    - But we already established from edge $(A_1, B_1)$ that $A_1$ must decide 1!
7. This produces an irreconcilable contradiction: $A_1$ must simultaneously decide 0 (to satisfy Agreement with $C_0$) and 1 (to satisfy Validity with $B_1$).
8. Thus, no deterministic protocol $\Pi$ can solve Byzantine consensus for $n=3, f=1$.
9. **Generalization to $n \le 3f$**:
  - Divide $n$ processes into three disjoint sets $S_1, S_2, S_3$, each with $|S_i| \le f$.
  - Any consensus protocol for $n \le 3f$ would allow three meta-nodes (each simulating one partition) to solve the 3-node Byzantine problem by internal majority voting.
  - Since the 3-node problem is impossible, consensus is impossible for any $n \le 3f$. Thus, $n \ge 3f + 1$ is strictly required. $\blacksquare$

---

### 📄 Landmark Research Papers (from [[03 - Papers/Paper Reading Hub|Paper Reading Hub]])

The following foundational papers from the [[03 - Papers/Paper Reading Hub|Paper Reading Hub]] are assigned to Block 23. Analyze each using the Keshav Three-Pass Methodology:

1. **"Time, Clocks, and the Ordering of Events in a Distributed System"** (Leslie Lamport, 1978)
    - *Venue:* Communications of the ACM (Paper 21 in [[03 - Papers/Paper Reading Hub|Paper Reading Hub]])
    - *Landmark Invariant:* Logical clocks, happened-before partial order ($\to$), total ordering of events, and state machine replication foundations.
    - *Reading Guidance:* Relate Lamport clocks and vector clocks to distributed causality, state machine replication, and inter-process ordering invariants in [[16 - Operating Systems]].
2. **"Impossibility of Distributed Consensus with One Faulty Process"** (Michael J. Fischer, Nancy A. Lynch, Michael S. Paterson (FLP), 1985)
    - *Venue:* Journal of the ACM (Paper 22 in [[03 - Papers/Paper Reading Hub|Paper Reading Hub]])
    - *Landmark Invariant:* Proof by bivalence perturbation that no deterministic asynchronous protocol can guarantee consensus in the presence of even a single crash failure.
    - *Reading Guidance:* Compare the Fischer-Lynch-Paterson (FLP) impossibility result in asynchronous systems with kernel-level crash recovery and single-node fail-stop assumptions in [[16 - Operating Systems]].
3. **"In Search of an Understandable Consensus Algorithm" (Raft)** (Diego Ongaro & John Ousterhout, 2014)
    - *Venue:* USENIX ATC '14 (Paper 23 in [[03 - Papers/Paper Reading Hub|Paper Reading Hub]])
    - *Landmark Invariant:* Decomposed consensus via leader election, randomized timers, and log matching invariant; provably safe state machine replication.
    - *Reading Guidance:* Trace the Election Safety and Leader Completeness invariants, mapping them to the MIT 6.5840 Lab 2 implementation.
