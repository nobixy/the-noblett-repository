---
title: "05 — Resources"
id: "MOD05-RES"
type: "reference"
module: "05-data-structures-and-algorithms"
phase: "C"
order: 840
prerequisites: []
---

# 05 — Resources

*Pointers only. Read the matching chapter when a project needs it — not before.*

## Main texts (free)
- **Jeff Erickson, *Algorithms*** (jeffe.cs.illinois.edu/teaching/algorithms) — recursion, dynamic programming, graphs, shortest paths. Superb explanations; exercises without solutions (good for the module-close test).
- **Pat Morin, *Open Data Structures*** (opendatastructures.org, Python edition) — arrays, lists, hash tables, heaps, trees, with code and analysis.

## References
- **CLRS, *Introduction to Algorithms*** — the encyclopedia. Look things up; don't read cover to cover.
- **Steven Skiena, *The Algorithm Design Manual*** — its second half ("catalog of algorithmic problems") is the best guide to *which* algorithm fits a real problem.

## Per project
- **Copydiff:** Eugene Myers, "An O(ND) Difference Algorithm and Its Variations" (1986, *Algorithmica*) — the original, readable paper; James Coglan's blog series "The Myers diff algorithm" — excellent illustrated walkthrough.
- **Vault Search:** Manning, Raghavan & Schütze, ***Introduction to Information Retrieval*** (free at nlp.stanford.edu/IR-book) — chapters 1–2 (inverted indexes), 3 (tolerant retrieval: tries, edit distance), 6 (TF-IDF), 8 (evaluation).
- **Route Planner:** Amit Patel's **Red Blob Games** pages on A* and pathfinding (redblobgames.com) — interactive and beautiful; the OpenStreetMap wiki for the XML format and tags; geojson.io for viewing output.
- **Edit Buffer:** Charles Crowley, "Data Structures for Text Sequences" (1998) — the classic comparison paper; the VS Code team's blog post "Text Buffer Reimplementation" (2018) on their piece tree.

## Practice problems
- Erickson's chapter exercises; 6.006 problem sets; **Codeforces** or **LeetCode** "easy/medium" problems by topic — a few per section, mixed across topics [I], as a supplement, not a replacement for the projects.

## Video course

*Companions, not replacements: your labs and projects are the course. Watch with the [V protocol](../study-protocols.md#v--watch-actively) (pause, predict, then blank-sheet [R]), take lectures and quizzes as second explanations, and build this module's own projects, not the course's assignments. How courses fit your sessions: [study-protocols § Using video courses](../study-protocols.md#using-video-courses).*

**Primary — NeetCode: Algorithms & Data Structures for Beginners, then Advanced Algorithms**, NeetCode.io. Included in your NeetCode Pro ([DR-006](<../04 - System/DR-006 - Digital Twin, EW Resilience and Fun Prerequisites.md>)).
- Courses: [Algorithms & Data Structures for Beginners](https://neetcode.io/courses/dsa-for-beginners/0) · [Advanced Algorithms](https://neetcode.io/courses/advanced-algorithms/0) · [all NeetCode courses](https://neetcode.io/courses)
- **Access:** both are NeetCode Pro courses. If your Pro access has ended when you reach this module, swap the picks: MIT 6.006 (free) becomes the primary, and NeetCode's free problem videos on YouTube stay available for practice.
- **Why it fits:** Python code for every lesson (the module's language), a written article and animations for each video, and coding exercises with video solutions. That is ideal for the [I] and [R] protocols. The beginner course starts at arrays and builds in a deliberate order to heaps, hashing, graphs and dynamic programming. The advanced course adds tries, Dijkstra and longest common subsequence, which Vault Search, Route Planner and Copydiff need.

**Alternate — MIT 6.006 Introduction to Algorithms**, MIT OpenCourseWare (Erik Demaine, Jason Ku, Justin Solomon). Free.
- Lectures: [YouTube playlist](https://www.youtube.com/playlist?list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY) · course page with problem sets *and solutions*: [MIT OCW 6.006](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/)
- **Why:** the rigorous version: proofs of correctness and running time, and the best free treatment of dynamic programming (SRTBOT). Use it when NeetCode shows you *how* but you need *why*, and its problem sets for the module-close test.

### Lecture-to-vault map

NeetCode is listed by topic, as the course pages are organised. 6.006 numbers are lecture numbers.

| Vault item | NeetCode (primary) | MIT 6.006 (alternate) |
| :-- | :-- | :-- |
| [Lab 01 — Big-O by measurement](labs/lab-01-big-o-by-measurement.md) | Beginners: Arrays (dynamic arrays and their costs) | Lecture 1 Algorithms and Computation · Lecture 2 Data Structures and Dynamic Arrays |
| [Lab 02 — Sorting workshop](labs/lab-02-sorting-workshop.md) | Beginners: Sorting · Heap / Priority Queue | Lecture 3 Sets and Sorting · Lecture 5 Linear Sorting · Lecture 8 Binary Heaps |
| [Lab 03 — Stacks, queues and lists](labs/lab-03-stacks-queues-and-lists.md) | Beginners: Arrays (stacks) · Linked Lists (queues) | Lecture 2 Data Structures and Dynamic Arrays |
| [Copydiff](projects/copydiff/spec.md) (LCS, edit distance) | Beginners: Dynamic Programming · Advanced: LCS | Lecture 15 Dynamic Programming Part 1 · Lecture 16 Dynamic Programming Part 2: LCS, LIS, Coins |
| [Vault Search](projects/vault-search/spec.md) (hashing, trie, top-k) | Beginners: Hashing · Heap / Priority Queue · Advanced: Trie | Lecture 4 Hashing · Lecture 8 Binary Heaps |
| [Route Planner](projects/route-planner/spec.md) (BFS, DFS, Dijkstra) | Beginners: Graphs · Advanced: Dijkstra's | Lecture 9 Breadth-First Search · Lecture 10 Depth-First Search · Lecture 11 Weighted Shortest Paths · Lecture 13 Dijkstra |
| [Edit Buffer](projects/edit-buffer/spec.md) (gap buffer, piece table, rope) | Beginners: Arrays · Linked Lists · Trees | Lecture 6 Binary Trees Part 1 · Lecture 7 Binary Trees Part 2: AVL |

**Gaps:** neither course covers the Myers diff algorithm, A*, inverted indexes, or gap buffers, piece tables and ropes by name; the per-project pointers above do. Module 11's [CMU 15-445 lecture #09](../11-databases/resources.md#video-course) covers inverted indexes and tries.
