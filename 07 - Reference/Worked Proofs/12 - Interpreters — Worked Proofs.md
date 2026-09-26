---
title: "12 - Interpreters — Worked Proofs"
type: reference
tags:
  - reference
  - answer-key
---

# 12 - Interpreters — Worked Proofs

> [!WARNING] Answer key — open only after your own attempt
> These derivations were generated as reference material, not study notes. Reading them first creates the illusion of competence that [[how-i-study]] warns about.
> Protocol: attempt the proof from a blank sheet in [[12 - Interpreters]] → compare here → log every gap you found.
> They are unverified; treat any step you cannot justify as a possible error, not as authority.

Back to: [[12 - Interpreters]] · [[Worked Proofs Index]]

---

### Core Concepts & Derivations
- **Top-Down Operator Precedence (Pratt Parsing):** Binding power invariants, prefix parselets (`nud`), and infix parselets (`led`) eliminating grammar ambiguity for binary/unary operator expressions without recursive descent backtracking.
- **Stack-Based Bytecode VM Execution:** The core dispatch loop (`FETCH-DECODE-EXECUTE`), instruction pointer arithmetic, and stack manipulation invariants for operand evaluation.
- **Upvalue Closure Abstraction:** Representation of open and closed upvalues in `clox`, preserving local variable references on the stack before frame exit and hoisting them to heap-allocated upvalue structs.
- **Tri-Color Mark-and-Sweep Garbage Collection:** White/Gray/Black node coloring invariants, root set traversal (VM stack, globals, compiler tokens), and heap sweep phase correctness.

---

### 1. Dijkstra's Tri-Color Mark-and-Sweep Invariant and GC Correctness
**Theorem (Dijkstra et al., 1978):** Let an interpreter heap be modeled as a directed graph $G = (V, E)$, where vertices $V$ represent allocated memory objects and directed edges $(u, v) \in E$ represent reference pointers from object $u$ to object $v$. Let $R \subseteq V$ denote the root set (registers, VM evaluation stack, global environment).
Partition the vertices into three mutually exclusive sets: White ($W$), Gray ($G$), and Black ($B$), such that $V = W \uplus G \uplus B$:
- **White ($W$):** Unvisited candidate objects subject to reclamation.
- **Gray ($G$):** Reachable objects whose payload pointers have not yet been traced.
- **Black ($B$):** Reachable objects whose direct references have been fully traversed.

**The Strong Tri-Color Invariant:**
$$\text{Inv}: \forall (u, v) \in E, \quad (u \in B \implies v \notin W)$$
That is, no direct reference exists from a black object to a white object.

**Theorem Statement:** Under the mark-and-sweep transition system:
1. **Safety:** Upon termination (when $G = \emptyset$), every object reachable from the root set $R$ is Black, and every White object is unreachable from $R$. Sweeping $W$ reclaims strictly unreachable garbage and creates zero dangling pointers.
2. **Termination:** The marking algorithm terminates in at most $2|V|$ discrete object transition steps.

#### Step-by-Step Derivation & Proof:
1. **State Machine Initialization:**
   At the start of the garbage collection cycle:
   $$B_0 = \emptyset, \qquad G_0 = R, \qquad W_0 = V \setminus R$$
   Since $B_0$ contains no elements, the implication $(u \in B_0 \implies v \notin W_0)$ is vacuously true. Hence, $\text{Inv}$ holds at step 0.

2. **Transition Semantics:**
   At each step $k$, while $G_k \ne \emptyset$, the collector selects an object $g \in G_k$ and executes:
  - For all outgoing edges $(g, v) \in E$: if $v \in W_k$, move $v$ from $W$ to $G$:
    $$W_{k+1} = W_k \setminus \{v \mid (g, v) \in E\}, \quad G_{k+1}' = G_k \cup \{v \in W_k \mid (g, v) \in E\}$$
  - Transition $g$ from Gray to Black:
    $$B_{k+1} = B_k \cup \{g\}, \quad G_{k+1} = G_{k+1}' \setminus \{g\}$$

3. **Inductive Invariant Preservation:**
   Assume $\text{Inv}$ holds at step $k$. We prove $\text{Inv}$ holds at step $k+1$.
   Suppose for contradiction that there exists $(u, v) \in E$ such that $u \in B_{k+1}$ and $v \in W_{k+1}$.
  - **Case 1 ($u \in B_k$):** By inductive hypothesis, $v \notin W_k$. Since $W_{k+1} \subseteq W_k$, $v \notin W_{k+1}$, contradiction.
  - **Case 2 ($u = g$):** Object $g$ was transitioned from $G$ to $B$ at this step. By the transition definition, every successor $w$ satisfying $(g, w) \in E$ that was in $W_k$ was explicitly moved into $G_{k+1}$. Therefore, no successor of $g$ remains in $W_{k+1}$, so $v \notin W_{k+1}$, contradiction.
   Thus, $\text{Inv}$ is an inductive invariant of the collector.

4. **Termination Proof via Potential Function:**
   Define the non-negative integer potential function:
   $$\Phi(W, G, B) = 2|W| + |G|$$
   At each transition step, an object $g$ leaves $G$. Let $m = |\{v \in W_k \mid (g, v) \in E\}| \ge 0$ be the number of white successors shifted to gray:
   $$\Delta |W| = -m, \qquad \Delta |G| = m - 1$$
   The change in potential is:
   $$\Delta \Phi = 2(-m) + (m - 1) = -m - 1 \le -1$$
   Since $\Phi$ is strictly decreasing and bounded below by 0 ($\Phi \ge 0$), the marking phase must terminate in at most $\Phi(W_0, G_0, B_0) \le 2|V|$ steps, halting precisely when $G = \emptyset$.

5. **Correctness at Termination ($G = \emptyset$):**
   When the algorithm halts, $G = \emptyset$, so $V = B \uplus W$.
   Let $x \in V$ be any live object reachable from $R$.
   There exists a directed path of references:
   $$r = v_0 \xrightarrow{e_1} v_1 \xrightarrow{e_2} \dots \xrightarrow{e_m} v_m = x \quad (r \in R)$$
   We prove by induction on path index $i$ that $v_i \in B$:
  - For $i = 0$: $v_0 = r \in R \subseteq G_0 \cup B_0$. Since $G = \emptyset$ and objects never transition to $W$, $v_0 \in B$.
  - Inductive step: Assume $v_i \in B$. By the Tri-Color Invariant $\text{Inv}$, $(v_i, v_{i+1}) \in E \implies v_{i+1} \notin W$. Because $V = B \uplus W$, $v_{i+1} \notin W \implies v_{i+1} \in B$.
   By induction, $v_m = x \in B$.
   By contrapositive, if an object $w \in W$ at termination, it is unreachable from $R$. Reclaiming all memory in $W$ preserves all reachable objects and introduces zero dangling references. $\blacksquare$
