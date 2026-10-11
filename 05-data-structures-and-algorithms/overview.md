---
title: "05 — Data Structures and Algorithms"
id: "MOD05"
type: "overview"
module: "05-data-structures-and-algorithms"
phase: "C"
order: 760
prerequisites: [MOD02, MOD03, M11, E10]
checkpoints: [MOD05-CLOSE]
tags: [module, algorithms, data-structures]
---

# 05 — Data Structures and Algorithms

**How to make programs fast — and know they're right.** You'll build the classic data structures yourself (dynamic arrays, linked lists, hash tables, heaps, tries, trees, graphs) and the classic algorithms (sorting, searching, graph search, shortest paths, dynamic programming), and you'll measure every one of them. Then you'll use them in four tools you'll keep using: a diff engine that checks your copywork, a search engine for your own notes, a route planner on the real map of your town, and the core of a text editor.

---

## Prerequisites

**Gate:** this module starts only after both foundation track assessments (English E10 and Math M11) are passed, and after Modules 02 and 03. The frontmatter `prerequisites` list says the same.

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

| Order | Item |
| :-- | :-- |
| 1 | [Lab 01 — Big-O by Measurement](labs/lab-01-big-o-by-measurement.md) |
| 2 | [Lab 02 — Sorting Workshop](labs/lab-02-sorting-workshop.md) |
| 3 | [Lab 03 — Stacks, Queues, and Lists](labs/lab-03-stacks-queues-and-lists.md) |
| 4 | **[Copydiff](projects/copydiff/spec.md)** — dynamic programming, diff algorithms |
| 5 | **[Vault Search](projects/vault-search/spec.md)** — hash tables, inverted indexes, tries, ranking |
| 6 | **[Route Planner](projects/route-planner/spec.md)** — graphs, heaps, Dijkstra, A* on real map data |
| 7 | **[Edit Buffer](projects/edit-buffer/spec.md)** — gap buffers, piece tables, undo, a tiny editor |

Labs first, then projects in the order shown (Copydiff first, because its design doc already exists).

**Study the theory alongside the builds.** For each topic, read the matching chapter of a free text (below) *when the project needs it* — not before. Then do 5–10 problems from that chapter, mixed with earlier topics [I].

**Free texts:** Jeff Erickson, ***Algorithms*** (jeffe.cs.illinois.edu, free); Pat Morin, ***Open Data Structures*** (opendatastructures.org, free); MIT **6.006** lectures and problem sets on OCW. Reference: CLRS (*Introduction to Algorithms*).

## How the study methods run through this module

| Protocol | In this module |
| :-- | :-- |
| **R** | Blank-sheet each data structure's invariants and each algorithm's steps before implementing it. Milestone Checkpoints. Study Deck cards for complexities **with the reason** ("binary search is O(log n) *because* each step halves the range"). |
| **F** | Each project's core algorithm explained plainly and recorded: the DP table; hashing; Dijkstra's "settled" set; the piece table. |
| **W** | Every design choice gets a contrast why-ladder in the design doc: chaining or probing? heap or sorted list? piece table or gap buffer? — **answered with measurements**. |
| **S** | Algorithms written as subgoal comments first; worked examples traced on paper with labels (Erickson's book is excellent for this). |
| **I** | Problem practice mixes topics; Session-5 problem sets mix this module with Module 03. |
| **D** | Off-by-one and invariant bugs: the stuck rule (three honest attempts); invariant asserts (Module 03 Lab 02) are your best debugging tool here. |
| **T** | **Full design docs** (E10 level) before each project; lab reports for benchmarks; demos. |

## Video course

- **Primary:** **NeetCode: Algorithms & Data Structures for Beginners**, then **Advanced Algorithms** (NeetCode.io, NeetCode Pro) — [beginners](https://neetcode.io/courses/dsa-for-beginners/0) · [advanced](https://neetcode.io/courses/advanced-algorithms/0).
- **Alternate:** **MIT 6.006 Introduction to Algorithms** (MIT OpenCourseWare) — [YouTube playlist](https://www.youtube.com/playlist?list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY) · [OCW course page](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/). If your NeetCode Pro access has ended, this becomes the primary.
- **Which lectures go with which lab and project:** the map in [resources](<resources.md#lecture-to-vault-map>). Watch with the [V protocol](../study-protocols.md#v--watch-actively) and [use courses as companions](../study-protocols.md#using-video-courses).

---

## Connections

- **Back:** M11 (growth rates), Module 03 (induction proves algorithms correct; counting analyses them; the birthday bound predicts hash collisions), Module 02 (recursion, memoisation, testing), [Growth and Halving Lab](../00-foundations/math/projects/growth-and-halving-lab/spec.md).
- **Forward:** Module 07 (the same structures in C, with real memory), Module 08 (schedulers use queues and heaps; file systems use trees), Module 09 (Courier's send window is a circular buffer), Module 10 (the DOM is a tree; layout walks it), Module 11 (B+trees, hash indexes, sorting for joins).

## Module close

1. **Cumulative retrieval [R]:** every data structure's invariant and operations with costs; every algorithm's steps and cost, with reasons.
2. **Timed problem set:** 8 unseen problems (from Erickson's exercises or a 6.006 problem set) — design an algorithm, argue correctness, give its running time. Grade honestly with solutions where available.
3. **Pick-the-structure exercise [W]:** for five realistic tasks (e.g. "undo history," "top 10 scores," "autocomplete," "routing table," "duplicate detection"), write which structure you'd choose and why, in two sentences each.
4. Tick the module in [Start Here](<../00 - Start Here.md>).

**Resources:** books, docs, and tools for this module are in [resources.md](resources.md) (pointers only — the projects are the course).

**Next:** [06 Computer Architecture](../06-computer-architecture/overview.md) and [07 Systems Programming](../07-systems-programming/overview.md).
