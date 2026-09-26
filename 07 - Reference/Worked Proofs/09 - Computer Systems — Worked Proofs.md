---
title: "09 - Computer Systems — Worked Proofs"
type: reference
tags:
  - reference
  - answer-key
---

# 09 - Computer Systems — Worked Proofs

> [!WARNING] Answer key — open only after your own attempt
> These derivations were generated as reference material, not study notes. Reading them first creates the illusion of competence that [[how-i-study]] warns about.
> Protocol: attempt the proof from a blank sheet in [[09 - Computer Systems]] → compare here → log every gap you found.
> They are unverified; treat any step you cannot justify as a possible error, not as authority.

Back to: [[09 - Computer Systems]] · [[Worked Proofs Index]]

---

### Core Concepts & Derivations
- **IEEE 754 Floating-Point Representation:** Sign, biased exponent ($E = e - \text{Bias}$), normalized mantissa ($1.f$), subnormal numbers, representation of infinities and NaNs, and rounding error bounds.
- **Cache Hit/Miss Derivation & B/S/T Geometry:** Address decomposition into tag ($t$), set index ($s$), and block offset ($b$). Derivation of hit/miss latency formulas and loop tiling / blocking for spatial/temporal cache locality.
- **Virtual Address Translation & Multi-Level Page Tables:** Translation of virtual page numbers (VPN) to physical frame numbers (PFN) via hierarchical page directory traversal, TLB hit rates, and page fault interrupt handlers.
- **Segregated Free List Allocator Invariants:** Boundary-tag coalescing algorithm, segregated size classes, space utilization bounds, and throughput trade-offs in dynamic memory management.

---

### 1. Cache Complexity and Hong-Kung I/O Bound for Blocked Matrix Multiplication
**Theorem (Hong & Kung 1981):** Let two $n \times n$ dense matrices $A, B$ of 8-byte elements be multiplied ($C = A \cdot B$) on a machine with cache capacity $M$ words and cache line transfer block size $L$ words ($M \gg L$).
1. The standard naive 3-nested loop algorithm exhibits $\Theta(n^3)$ memory transfers (cache misses) when $n > \sqrt{M}$.
2. Under blocked (tiled) matrix multiplication with square tile size $b \times b$ chosen such that $3 b^2 \le M$, the total number of cache misses satisfies:
$$Q(n, M, L) = \Theta\left( \frac{n^3}{L \sqrt{M}} \right)$$
which asymptotically meets the theoretical Hong-Kung I/O lower bound $\Omega\left( \frac{n^3}{L \sqrt{M}} \right)$, reducing memory bus traffic by a factor of $\Theta(\sqrt{M})$.

#### Step-by-Step Derivation & Proof:
1. **Memory Traffic Analysis of the Naive Algorithm:**
   The canonical loop ordering `(i, j, k)` evaluates:
   $$C[i][j] = \sum_{k=0}^{n-1} A[i][k] \cdot B[k][j]$$
  - Matrix $A$ is scanned row-wise: sequential accesses exploit spatial locality, incurring $n / L$ misses per row, yielding $n \cdot (n/L) = n^2 / L$ misses.
  - Matrix $B$ is scanned column-wise with stride $n$: each successive read $B[k][j]$ accesses a different cache line. When matrix dimension $n > M/L$ (the working line set exceeds cache capacity), every element read from $B$ causes a cache miss.
  - The total cache misses for matrix $B$ across all $n^2$ inner loop runs is $n^2 \cdot n = n^3$.
  - Thus, total naive cache misses are:
    $$Q_{\text{naive}} = \frac{n^2}{L} + n^3 + \frac{n^2}{L} = \Theta(n^3)$$

2. **Partitioning into Sub-Matrix Tiles:**
   Divide $A, B, C$ into sub-blocks of dimension $b \times b$, where there are $N = n / b$ blocks along each matrix dimension:
   $$C_{i', j'} = \sum_{k'=1}^{n/b} A_{i', k'} \cdot B_{k', j'} \quad (1 \le i', j' \le n/b)$$
   The outer loops iterate over $(n/b)^3$ block multiplications.

3. **Cache Capacity Working Set Invariant:**
   During the inner block multiplication $C_{i', j'} += A_{i', k'} \cdot B_{k', j'}$, the working set consists of three $b \times b$ blocks (one block from $A$, one from $B$, and one from $C$).
   To prevent capacity thrashing and ensure each tile remains resident in cache during the block product:
   $$3 b^2 \le M \implies b \le \sqrt{\frac{M}{3}}$$

4. **I/O Miss Accounting per Block Operation:**
   With $3 b^2 \le M$:
  - Loading block $A_{i', k'}$ requires $\lceil b^2 / L \rceil$ cache line transfers.
  - Loading block $B_{k', j'}$ requires $\lceil b^2 / L \rceil$ cache line transfers.
  - Accumulating into $C_{i', j'}$ is held in cache across all $k'$ iterations and written back once, incurring $2 \frac{b^2}{L}$ transfers per $(i', j')$ pair.
   Across all $(n/b)^3$ block products, the total cache line misses for $A$ and $B$ are:
   $$Q_{\text{tiled}} = \left( \frac{n}{b} \right)^3 \cdot \left( \frac{b^2}{L} + \frac{b^2}{L} \right) = \frac{n^3}{b^3} \cdot \frac{2 b^2}{L} = \frac{2 n^3}{b \cdot L}$$

5. **Optimal Parameter Choice and Bound Derivation:**
   To minimize $Q_{\text{tiled}}$, select the maximal permissible block size that satisfies the cache capacity constraint:
   $$b = \sqrt{\frac{M}{3}} = \Theta(\sqrt{M})$$
   Substituting $b = \Theta(\sqrt{M})$ into the miss equation:
   $$Q_{\text{tiled}} = \frac{2 n^3}{\sqrt{M/3} \cdot L} = \Theta\left( \frac{n^3}{L \sqrt{M}} \right)$$

6. **Optimality via Hong-Kung Lower Bound:**
   By the Hong-Kung computational DAG pebble game theorem (1981), any valid schedule of the $2n^3$-operation matrix multiply graph on an I/O model with capacity $M$ requires at least $\Omega(n^3 / \sqrt{M})$ word transfers, corresponding to $\Omega(n^3 / (L \sqrt{M}))$ cache line transfers.
   Because $Q_{\text{tiled}} = \mathcal{O}(n^3 / (L \sqrt{M}))$, blocked matrix multiplication is asymptotically optimal. $\blacksquare$

---

### 📄 Landmark Research Papers (from [[03 - Papers/Paper Reading Hub|Paper Reading Hub]])

The following foundational papers from the [[03 - Papers/Paper Reading Hub|Paper Reading Hub]] are assigned to Block 09. Analyze each using the Keshav Three-Pass Methodology:

1. **"Hints for Computer System Design"** (Butler W. Lampson, 1983)
    - *Venue:* ACM Operating Systems Review (Paper 4 in [[03 - Papers/Paper Reading Hub|Paper Reading Hub]])
    - *Landmark Invariant:* Engineering invariants: worst-case interfaces, hints vs. absolute truth, crash recovery by idempotent state reconstruction.
    - *Reading Guidance:* Focus Pass 2 on the distinction between correctness and performance interfaces, and Lampson's principles on caching and end-to-end completeness.
2. **"Memory Consistency and Event Ordering in Scalable Shared-Memory Multiprocessors"** (Kourosh Gharachorloo et al., 1990)
    - *Venue:* ISCA '90 (Paper 9 in [[03 - Papers/Paper Reading Hub|Paper Reading Hub]])
    - *Landmark Invariant:* Formalization of weak ordering and release consistency memory models; decoupling synchronization operations from data access reordering.
    - *Reading Guidance:* Trace the distinction between sequential consistency, processor consistency, weak consistency, and release consistency (acquire/release memory barriers).
