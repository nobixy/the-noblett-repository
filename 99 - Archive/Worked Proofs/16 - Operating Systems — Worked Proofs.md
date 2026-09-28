---
title: "16 - Operating Systems — Worked Proofs"
type: reference
tags:
  - reference
  - answer-key
---

# 16 - Operating Systems — Worked Proofs

> [!WARNING] Answer key — open only after your own attempt
> These derivations were generated as reference material, not study notes. Reading them first creates the illusion of competence that [[how-i-study]] warns about.
> Protocol: attempt the proof from a blank sheet in [[16 - Operating Systems]] → compare here → log every gap you found.
> They are unverified; treat any step you cannot justify as a possible error, not as authority.

Back to: [[16 - Operating Systems]] · [[Worked Proofs Index]]

---

### 1. The Vector Clock Causal Ordering Theorem
> [!NOTE] Distributed Systems Reciprocity
> For the foundational scalar logical clock and distributed state-machine replication models, see [[01 - Curriculum/Year 4 - Specialization/23 - Distributed Systems|23 - Distributed Systems]] and [[03 - Papers/Paper Reading Hub|Paper Reading Hub]] (Paper 21: Leslie Lamport 1978, "Time, Clocks, and the Ordering of Events in a Distributed System").

**Theorem (Fidge 1988, Mattern 1989):** In an asynchronous distributed system of $N$ processes without synchronized clocks, the Vector Clock algorithm establishes an exact isomorphism between event timestamps and the causal happened-before partial order ($\to$):
$$a \to b \iff V(a) < V(b)$$
where $V(a) < V(b) \iff (\forall k \in [1, N]: V(a)[k] \le V(b)[k]) \land (\exists k \in [1, N]: V(a)[k] < V(b)[k])$.

#### The Vector Clock Protocol Rules:
Each process $P_i$ maintains vector clock $V_i \in \mathbb{N}^N$, initialized to $[0, \dots, 0]$.
1. **Local Action:** Before executing an internal or send event, $P_i$ increments its own entry: $V_i[i] \gets V_i[i] + 1$.
2. **Message Send:** $P_i$ attaches its current timestamp $V(e) = V_i$ to message $m$.
3. **Message Receive:** Upon receiving $(m, V_{msg})$, $P_i$ updates its clock:
   $$V_i[k] \gets \max(V_i[k], V_{msg}[k]) \quad \forall k \in [1, N]$$
   and then increments $V_i[i] \gets V_i[i] + 1$ for the receive event $e_r$.

#### Proof of Equivalence ($a \to b \iff V(a) < V(b)$):
1. **Soundness ($a \to b \implies V(a) < V(b)$):**
   Proof by induction on the length $k$ of the causal path connecting $a$ and $b$:
  - Base case ($k=1$):
    - If $a$ and $b$ occur on the same process $P_i$ with $a$ preceding $b$, rule 1 guarantees $V(a)[i] < V(b)[i]$ and $V(a)[j] \le V(b)[j] \quad (j \ne i)$. Thus $V(a) < V(b)$.
    - If $a$ is the send of message $m$ on $P_i$ and $b$ is the receive of $m$ on $P_j$, rule 3 sets $V(b)[k] \ge V_{msg}[k] = V(a)[k]$ for all $k$, and increments $V(b)[j] > V(a)[j]$. Thus $V(a) < V(b)$.
  - Inductive step: If $a \to c \to b$, by induction hypothesis $V(a) < V(c)$ and $V(c) < V(b)$. By transitivity of the strict partial order, $V(a) < V(b)$.
2. **Completeness ($V(a) < V(b) \implies a \to b$):**
   We prove the contrapositive: $a \not\to b \implies V(a) \not< V(b)$.
   Let $P_i$ be the process where event $a$ occurred.
   The timestamp component $V(a)[i]$ records the exact sequence number of event $a$ on process $P_i$.
   For process $P_j$ (the host of event $b$) to satisfy $V(b)[i] \ge V(a)[i]$, process $P_j$ must have received a message carrying knowledge of $P_i$'s state at or after event $a$.
   By the definition of causal happened-before ($\to$), this can occur if and only if there exists a causal message chain from $a$ to $b$ ($a \to b$).
   Therefore, if $a \not\to b$, it is impossible for $P_j$ to have received causal knowledge of event $a$, which implies $V(b)[i] < V(a)[i]$.
   Hence, $V(a) \not\le V(b)$, which directly implies $V(a) \not< V(b)$. $\blacksquare$

---

### 2. The FLP Impossibility Theorem (Fischer, Lynch, Paterson 1985)
> [!NOTE] Distributed Consensus Reciprocity
> For the complete study of how distributed systems resolve or circumvent consensus impossibility in asynchronous networks, see [[01 - Curriculum/Year 4 - Specialization/23 - Distributed Systems|23 - Distributed Systems]] and [[03 - Papers/Paper Reading Hub|Paper Reading Hub]] (Paper 22: Michael J. Fischer, Nancy A. Lynch, Michael S. Paterson 1985, "Impossibility of Distributed Consensus with One Faulty Process").

**Theorem:** In an asynchronous network model, no deterministic consensus protocol can guarantee both safety (agreement, validity) and liveness (termination) in the presence of even a single unannounced crash failure.

#### Formal System Model:
- A configuration $C$ consists of the internal states of all processes and the contents of the global message buffer $M$.
- A step consists of an event $e = (p, m)$, where process $p$ receives message $m \in M$ (or $\emptyset$), transitions to a new internal state, and emits a set of new messages.
- An execution is *fair* if every message sent is eventually received by its destination.

#### Core Proof Architecture:
1. **Valency of Configurations:**
  - A configuration $C$ is **bivalent** if both 0 and 1 are reachable decision values from $C$ via legal execution schedules.
  - A configuration $C$ is **univalent** if all reachable decision states from $C$ yield the same decision ($0$-valent or $1$-valent).
2. **Lemma 1 (Initial Bivalence):**
   There exists an initial configuration $C_0$ that is bivalent.
   *Proof Sketch:* Assume for contradiction that all initial configurations are univalent. Since the protocol is non-trivial, there exists an initial configuration $C_{init}^0$ yielding 0 (all inputs 0) and $C_{init}^1$ yielding 1 (all inputs 1). We can order all $2^N$ initial configurations such that adjacent configurations differ in the input bit of exactly one process $P_k$. Consider adjacent configurations $C_0^A$ (0-valent) and $C_0^B$ (1-valent) differing only at $P_k$. If $P_k$ crashes at time 0 (sends no messages), the executions of the remaining processes from $C_0^A$ and $C_0^B$ are identical, which contradicts deterministic agreement.
3. **Lemma 2 (Preservation of Bivalence):**
   Let $C$ be a bivalent configuration, and let $e = (p, m)$ be an event applicable to $C$. Let $\mathcal{C}$ be the set of configurations reachable from $C$ without applying $e$, and let $\mathcal{D} = e(\mathcal{C})$. Then $\mathcal{D}$ contains at least one bivalent configuration.
   *Proof Sketch:* Assume for contradiction that $\mathcal{D}$ contains no bivalent configurations. Then $\mathcal{D}$ contains both 0-valent and 1-valent configurations. By connectivity of reachability graphs, there exist adjacent configurations $C_1, C_2 \in \mathcal{C}$ with $C_2 = e'(C_1)$ such that $e(C_1)$ is 0-valent and $e(C_2) = e(e'(C_1))$ is 1-valent.
  - *Case A ($p \ne p'$):* The events $e$ and $e'$ commute: $e(e'(C_1)) = e'(e(C_1))$. But $e(C_1)$ is 0-valent, so applying $e'$ must yield a 0-valent state, contradicting that $e(C_2)$ is 1-valent.
  - *Case B ($p = p'$):* Consider a run in which process $p$ crashes before taking step $e$. The remaining processes must reach a decision, which again induces a topological contradiction.
4. **Conclusion:**
   By applying Lemma 2 inductively, an adversary can indefinitely delay consensus while maintaining fair message delivery, constructing an infinite execution that never decides. $\blacksquare$

---

### 3. Hardware Memory Consistency Models: x86-TSO & Release Consistency
Multi-core memory consistency defines the legal interleavings of reads and writes to shared physical memory across cores.

#### Total Store Order (x86-TSO) Operational Model:
In x86-TSO, each processor core has a private, local FIFO write buffer (*store buffer*).
- Stores to memory are buffered locally before being drained to shared memory.
- Loads read from the core's local store buffer if a pending write to the same address exists (*store-to-load forwarding*); otherwise, loads read from shared memory.
- **Permitted Reordering:** $W \to R$ (Store-Load reordering). A younger read can bypass an older write to a different address.
- **Prohibited Reorderings:** $R \to R$, $W \to W$, $R \to W$.

#### The Canonical Store-Buffering (SB) Litmus Test:
Initial state: $[x] = 0, [y] = 0$.
```text
Core 0:               Core 1:
(1) mov [x], $1       (3) mov [y], $1
(2) mov EAX, [y]      (4) mov EBX, [x]
```
- Under Sequential Consistency (SC): At least one store must complete before the other core's load reads the variable. The outcome $\text{EAX} = 0 \land \text{EBX} = 0$ is **strictly impossible**.
- Under x86-TSO: Core 0 places $x=1$ in its store buffer; Core 1 places $y=1$ in its store buffer. Both cores execute their reads before the buffers drain to coherent cache lines. The outcome $\text{EAX} = 0 \land \text{EBX} = 0$ is **architecturally legal**.
- **Hardware Barrier:** Inserting `MFENCE` between instructions (1)–(2) and (3)–(4) forces the store buffer to drain completely before proceeding, restoring SC behavior.

#### Release Consistency (Gharachorloo et al. 1990):
Release consistency categorizes memory accesses into ordinary reads/writes and special synchronization operations:
1. **Acquire ($Acq$):** A memory read with one-way acquire semantics. No subsequent read or write can be reordered before the Acquire.
2. **Release ($Rel$):** A memory write with one-way release semantics. No preceding read or write can be reordered after the Release.
- **Data-Race-Free Theorem (DRF-SC):** If all concurrent memory accesses to shared variables are protected by properly paired Acquire-Release operations (e.g. mutex locks or atomic release-acquire pairs), the program execution is guaranteed to be sequentially consistent. $\blacksquare$

---

### 📄 Landmark Research Papers (from [[03 - Papers/Paper Reading Hub|Paper Reading Hub]])

The following foundational papers from the [[03 - Papers/Paper Reading Hub|Paper Reading Hub]] are assigned to Block 16. Analyze each using the Keshav Three-Pass Methodology:

1. **"The UNIX Time-Sharing System"** (Dennis M. Ritchie & Ken Thompson, 1974)
    - *Venue:* Communications of the ACM (Paper 1 in [[03 - Papers/Paper Reading Hub|Paper Reading Hub]])
    - *Landmark Invariant:* Unified hierarchical file system, uniform file descriptor I/O interface, and shell pipelines for orthogonal process composition.
    - *Reading Guidance:* Focus Pass 2 on the kernel implementation of pipes, fork/exec decoupling, and inode allocation invariants.
2. **"Exokernel: An Operating System Architecture for Application-Level Resource Management"** (Dawson R. Engler, M. Frans Kaashoek, James O'Toole, 1995)
    - *Venue:* SOSP '95 (Paper 2 in [[03 - Papers/Paper Reading Hub|Paper Reading Hub]])
    - *Landmark Invariant:* Application of the end-to-end argument to kernel architecture; separation of protection from management via secure hardware exposure and user-space Library OSs.
    - *Reading Guidance:* Analyze how packet filters, secure disk bindings, and downloaded code achieve sub-microsecond protection transitions without sacrificing isolation.
3. **"seL4: Formal Verification of an OS Kernel"** (Gerwin Klein et al., 2009)
    - *Venue:* SOSP '09 (Paper 5 in [[03 - Papers/Paper Reading Hub|Paper Reading Hub]])
    - *Landmark Invariant:* First machine-checked proof of functional correctness and non-interference for a general-purpose microkernel in Isabelle/HOL.
    - *Reading Guidance:* Trace the refinement proof from the high-level abstract specification to the Haskell prototype and executable C code.
