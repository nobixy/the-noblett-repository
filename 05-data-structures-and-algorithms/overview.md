---
title: "05 — Data Structures and Algorithms"
module: "05-data-structures-and-algorithms"
hours: 190
tags: [module, algorithms, data-structures]
---

# 05 — Data Structures and Algorithms

**How to make programs fast — and know they're right.** You'll build the classic data structures yourself (dynamic arrays, linked lists, hash tables, heaps, tries, trees, graphs) and the classic algorithms (sorting, searching, graph search, shortest paths, dynamic programming), and you'll measure every one of them. Then you'll use them in four tools you'll keep using: a diff engine that checks your copywork, a search engine for your own notes, a route planner on the real map of your town, and the core of a text editor.

---

## Prerequisites

- [02 Programming Fundamentals](../02-programming-fundamentals/overview.md) and [03 Discrete Math](../03-discrete-math/overview.md) (Units 2, 3, 6, 7 at least).
- Math **M11** (logarithms and growth) — essential.
- English **E10** (every project here starts with a full design doc; Copydiff's was written in E10).

## Objectives

By the end you will be able to:
1. Describe running time and memory with big-O notation, **and** confirm it by measurement (log-log plots).
2. Implement and explain dynamic arrays (with amortised analysis), linked lists, stacks, queues, circular buffers, hash tables (two collision strategies), binary heaps, binary search trees, tries, and graph representations.
3. Implement and compare sorting algorithms, and explain why comparison sorting needs about n log n comparisons.
4. Use BFS, DFS, topological sort, Dijkstra, and A*, and argue their correctness.
5. Recognise dynamic-programming problems and solve them (edit distance, longest common subsequence).
6. Choose a data structure for a real workload by measuring alternatives, and justify the choice in a design doc.

## The topics

| Topic | Key ideas | Where you build it |
| :-- | :-- | :-- |
| Analysis | big-O/Θ/Ω; best/worst/average; amortised cost; log-log measurement | [Lab 01](labs/lab-01-big-o-by-measurement.md); every project's benchmarks |
| Linear structures | dynamic arrays; linked lists; stacks; queues; circular buffers; deques | [Lab 01](labs/lab-01-big-o-by-measurement.md), [Lab 03](labs/lab-03-stacks-queues-and-lists.md), Edit Buffer |
| Sorting and searching | insertion, merge, quick, heap, counting sort; stability; n log n bound; binary search | [Lab 02](labs/lab-02-sorting-workshop.md), Vault Search |
| Hashing | hash functions; chaining vs open addressing; load factor; resizing; collisions (Module 03's birthday bound) | [Vault Search](projects/vault-search/spec.md) |
| Trees | binary search trees; balance; tries; heaps; (B-trees in Module 11) | Vault Search (trie), Route Planner (heap), Edit Buffer (stretch: rope) |
| Graphs | adjacency lists; BFS; DFS; connected components; topological sort; Dijkstra; A* | [Route Planner](projects/route-planner/spec.md) |
| Dynamic programming | overlapping subproblems; memoisation (Module 02 Lab 01!) vs tables; LCS; edit distance | [Copydiff](projects/copydiff/spec.md) |
| Text structures | gap buffers; piece tables; line indexes | [Edit Buffer](projects/edit-buffer/spec.md) |

## Sequence and time

| Order | Item | Hours |
| :-- | :-- | --: |
| 1 | [Lab 01 — Big-O by Measurement](labs/lab-01-big-o-by-measurement.md) | 10 |
| 2 | [Lab 02 — Sorting Workshop](labs/lab-02-sorting-workshop.md) | 12 |
| 3 | [Lab 03 — Stacks, Queues, and Lists](labs/lab-03-stacks-queues-and-lists.md) | 10 |
| 4 | **[Copydiff](projects/copydiff/spec.md)** — dynamic programming, diff algorithms | 35 |
| 5 | **[Vault Search](projects/vault-search/spec.md)** — hash tables, inverted indexes, tries, ranking | 45 |
| 6 | **[Route Planner](projects/route-planner/spec.md)** — graphs, heaps, Dijkstra, A* on real map data | 40 |
| 7 | **[Edit Buffer](projects/edit-buffer/spec.md)** — gap buffers, piece tables, undo, a tiny editor | 38 |
| | **Total** | **~190** |

About 12 hours a week → 16 weeks. Labs first, then projects in the order shown (Copydiff first, because its design doc already exists).

**Study the theory alongside the builds.** For each topic, read the matching chapter of a free text (below) *when the project needs it* — not before. Then do 5–10 problems from that chapter, mixed with earlier topics [I].

**Free texts:** Jeff Erickson, ***Algorithms*** (jeffe.cs.illinois.edu, free); Pat Morin, ***Open Data Structures*** (opendatastructures.org, free); MIT **6.006** lectures and problem sets on OCW. Reference: CLRS (*Introduction to Algorithms*).

## How the study methods run through this module

| Protocol | In this module |
| :-- | :-- |
| **R** | Blank-sheet each data structure's invariants and each algorithm's steps before implementing it. Milestone Checkpoints. Study Deck cards for complexities **with the reason** ("binary search is O(log n) *because* each step halves the range"). |
| **F** | Each project's core algorithm explained plainly and recorded: the DP table; hashing; Dijkstra's "settled" set; the piece table. |
| **W** | Every design choice gets a contrast why-ladder in the design doc: chaining or probing? heap or sorted list? piece table or gap buffer? — **answered with measurements**. |
| **S** | Algorithms written as subgoal comments first; worked examples traced on paper with labels (Erickson's book is excellent for this). |
| **I** | Problem practice mixes topics; Friday problem sets mix this module with Module 03. |
| **D** | Off-by-one and invariant bugs: the 90-minute rule; invariant asserts (Module 03 Lab 02) are your best debugging tool here. |
| **T** | **Full design docs** (E10 level) before each project; lab reports for benchmarks; demos. |

## Connections

- **Back:** M11 (growth rates), Module 03 (induction proves algorithms correct; counting analyses them; the birthday bound predicts hash collisions), Module 02 (recursion, memoisation, testing), [Growth and Halving Lab](../00-foundations/math/projects/growth-and-halving-lab/spec.md).
- **Forward:** Module 07 (the same structures in C, with real memory), Module 08 (schedulers use queues and heaps; file systems use trees), Module 09 (Courier's send window is a circular buffer), Module 10 (the DOM is a tree; layout walks it), Module 11 (B+trees, hash indexes, sorting for joins).

## Module close

1. **Cumulative retrieval [R] (60 min):** every data structure's invariant and operations with costs; every algorithm's steps and cost, with reasons.
2. **Timed problem set (2 hours):** 8 unseen problems (from Erickson's exercises or a 6.006 problem set) — design an algorithm, argue correctness, give its running time. Grade honestly with solutions where available.
3. **Pick-the-structure exercise [W]:** for five realistic tasks (e.g. "undo history," "top 10 scores," "autocomplete," "routing table," "duplicate detection"), write which structure you'd choose and why, in two sentences each.
4. Tick the module in [Start Here](<../00 - Start Here.md>).

**Next:** [06 Computer Architecture](../06-computer-architecture/overview.md) and [07 Systems Programming](../07-systems-programming/overview.md).
