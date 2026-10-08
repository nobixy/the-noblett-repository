---
title: "06 - C Fluency — Worked Proofs"
type: reference
tags:
  - reference
  - answer-key
---

# 06 - C Fluency — Worked Proofs

> [!WARNING] Answer key — open only after your own attempt
> These derivations were generated as reference material, not study notes. Reading them first creates the illusion of competence that [[how-i-study]] warns about.
> Protocol: attempt the proof from a blank sheet in [[C Fluency]] → compare here → log every gap you found.
> They are unverified; treat any step you cannot justify as a possible error, not as authority.

Back to: [[C Fluency]] · [[Worked Proofs Index]]

---

### Core Concepts & Derivations
- **Pointer Arithmetic & Memory Representation:** Word alignment, pointer offset scaling by `sizeof(T)`, and pointer decay rules in C arrays.
- **Data Alignment & Structure Padding:** Memory bus word-boundary alignment rules ($\text{offset} \equiv 0 \pmod{\text{alignof}(T)}$) and optimal struct field ordering to minimize padding waste.
- **Call Stack & Calling Conventions:** x86-64 System V ABI calling convention (arguments in `%rdi, %rsi, %rdx, %rcx, %r8, %r9`), stack frame layout, return address protection, and callee-saved registers.
- **Dynamic Memory Allocator Invariants:** Boundary-tag coalescing, explicit free list traversal, heap fragmentation bounds, and arena allocator lifetime guarantees.

---

### 1. Optimal Struct Field Alignment & Memory Waste Minimization Theorem
**Theorem:** Let a C structure $S$ consist of $k$ scalar member fields $\{f_1, f_2, \dots, f_k\}$, where each field $f_i$ has byte size $s_i$ and hardware natural alignment requirement $a_i = 2^{p_i}$ with $p_i \in \mathbb{N}_0$ under the System V AMD64 ABI ($s_i$ is an integer multiple of $a_i$).
The byte offset $\text{off}(f_{i+1})$ is determined recursively by the alignment padding constraint:
$$\text{off}(f_1) = 0, \qquad \text{off}(f_{i+1}) = \left\lceil \frac{\text{off}(f_i) + s_i}{a_{i+1}} \right\rceil \cdot a_{i+1}$$
The total struct size is padded to a multiple of the struct's maximum alignment $A_{\max} = \max_{1 \le i \le k} a_i$:
$$\text{sizeof}(S) = \left\lceil \frac{\text{off}(f_k) + s_k}{A_{\max}} \right\rceil \cdot A_{\max}$$
**Theorem Statement:** Ordering the member fields in non-increasing order of their alignment constraints:
$$a_{\pi(1)} \ge a_{\pi(2)} \ge \dots \ge a_{\pi(k)}$$
strictly minimizes the total structure size $\text{sizeof}(S)$ and eliminates all internal padding between fields ($\text{pad}_i = 0$ for all $1 \le i < k$).

#### Step-by-Step Derivation & Proof:
1. **Divisibility of Power-of-Two Alignments:**
   Under the System V ABI, every primitive scalar type satisfies $s_i = c_i \cdot a_i$ for some positive integer $c_i \ge 1$ (e.g., `uint32_t` has size 4 and alignment 4; `double` has size 8 and alignment 8).
   Because every alignment is a power of two ($a_i = 2^{p_i}$), the ordering condition $a_{\pi(i)} \ge a_{\pi(i+1)}$ implies:
   $$2^{p_{\pi(i)}} \ge 2^{p_{\pi(i+1)}} \implies a_{\pi(i+1)} \mid a_{\pi(i)}$$
   Every higher alignment requirement is an exact integer multiple of any subsequent lower alignment requirement.

2. **Inductive Proof of Zero Internal Padding:**
   We prove by mathematical induction on $m \in \{1, 2, \dots, k\}$ that under descending alignment order, the cumulative byte offset before placing field $f_{\pi(m+1)}$:
   $$O_m = \sum_{j=1}^m s_{\pi(j)}$$
   is an exact integer multiple of $a_{\pi(m+1)}$.
  - **Base Case ($m = 1$):**
    $O_1 = s_{\pi(1)} = c_{\pi(1)} \cdot a_{\pi(1)}$.
    Since $a_{\pi(2)} \mid a_{\pi(1)}$, $a_{\pi(1)} = q \cdot a_{\pi(2)}$ for some integer $q \ge 1$.
    Thus $O_1 = (c_{\pi(1)} q) \cdot a_{\pi(2)}$, which is a multiple of $a_{\pi(2)}$.
    Therefore:
    $$\text{off}(f_{\pi(2)}) = \left\lceil \frac{O_1}{a_{\pi(2)}} \right\rceil \cdot a_{\pi(2)} = O_1$$
    Zero internal padding bytes are inserted: $\text{pad}_1 = \text{off}(f_{\pi(2)}) - O_1 = 0$.
  - **Inductive Step:**
    Assume $O_m = \sum_{j=1}^m s_{\pi(j)}$ is an exact multiple of $a_{\pi(m)}$.
    Because $a_{\pi(m+1)} \mid a_{\pi(m)}$, $O_m$ is also an integer multiple of $a_{\pi(m+1)}$.
    Field $f_{\pi(m+1)}$ has size $s_{\pi(m+1)} = c_{\pi(m+1)} \cdot a_{\pi(m+1)}$, which is also a multiple of $a_{\pi(m+1)}$.
    The cumulative offset after adding field $m+1$ is:
    $$O_{m+1} = O_m + s_{\pi(m+1)}$$
    Being the sum of two multiples of $a_{\pi(m+1)}$, $O_{m+1}$ is an exact multiple of $a_{\pi(m+1)}$.
    Now consider the subsequent field $f_{\pi(m+2)}$ (for $m+1 < k$):
    Since $a_{\pi(m+2)} \mid a_{\pi(m+1)}$, $O_{m+1}$ is also an exact integer multiple of $a_{\pi(m+2)}$.
    Consequently:
    $$\text{off}(f_{\pi(m+2)}) = \left\lceil \frac{O_{m+1}}{a_{\pi(m+2)}} \right\rceil \cdot a_{\pi(m+2)} = O_{m+1}$$
    The internal padding $\text{pad}_{m+1} = \text{off}(f_{\pi(m+2)}) - O_{m+1} = 0$.

3. **Total Allocation Minimality:**
   Because every internal padding term is zero:
   $$\sum_{i=1}^{k-1} \text{pad}_i = 0$$
   The offset immediately following the final field is:
   $$\text{off}(f_{\pi(k)}) + s_{\pi(k)} = \sum_{j=1}^k s_j$$
   The total allocated structure size is then:
   $$\text{sizeof}(S_{\text{sorted}}) = \left\lceil \frac{\sum_{j=1}^k s_j}{A_{\max}} \right\rceil \cdot A_{\max}$$
   Because any valid struct layout must allocate at least $\sum_{j=1}^k s_j$ data bytes and must be a multiple of $A_{\max}$ to ensure array element alignment, $\lceil (\sum s_j) / A_{\max} \rceil \cdot A_{\max}$ is the absolute theoretical lower bound on struct size. Hence, sorting by descending alignment achieves the global minimum. $\blacksquare$
