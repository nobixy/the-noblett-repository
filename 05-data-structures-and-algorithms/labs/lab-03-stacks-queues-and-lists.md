---
title: "Lab 03 — Stacks, Queues, and Lists"
id: "MOD05-LAB03"
type: "lab"
module: "05-data-structures-and-algorithms"
phase: "C"
order: 790
prerequisites: [MOD05-LAB02]
---

# Lab 03 — Stacks, Queues, and Lists

**Goal:** build linked lists, stacks, queues, and a circular buffer; use a stack to check brackets and to replace recursion; and use BFS and DFS to solve mazes.

**Sessions:** three.

---

## Session 1 — Linked lists

A **linked list** stores each item in a **node** that points to the next node. Unlike an array, items aren't side by side in memory.

```python
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
```

Build `LinkedList` with `push_front`, `pop_front`, `push_back` (keep a `tail` pointer so it's O(1)), `find`, `remove(value)`, `__iter__`, `__len__`.

| Operation | Array (Python list) | Linked list |
| :-- | :-- | :-- |
| get item i | O(1) | O(n) — walk from the head |
| insert/remove at front | O(n) — shift everything | O(1) |
| insert/remove in middle, given the node | O(n) | O(1) |
| memory per item | small | an extra pointer (or two) |

**[W]** If linked lists insert at the front in O(1), why are arrays usually faster in practice? (Module 06's caches will answer this precisely: walking a linked list jumps around memory; scanning an array doesn't. Write your guess now; check it in Module 06/07.)

**Draw it [R]:** draw the boxes and arrows for removing a middle node. The classic bug is losing the rest of the list by overwriting a pointer too early. Write the steps as subgoals first.

---

## Session 2 — Stacks, queues, and the circular buffer

### Stack (last in, first out)

`push`, `pop`, `peek`, `is_empty` — a Python list's `append`/`pop` are perfect.

**Build: bracket checker.** Check that `([]{()})` is balanced and `([)]` isn't, reporting the position of the first error. Push every opening bracket; on a closing bracket, pop and check it matches. [W] Why is a stack exactly the right structure? (The most recent unclosed bracket must close first.)

**Build: recursion → iteration.** Your Module 02 `treesize.py` used recursion. Rewrite `size_of` with an **explicit stack** of folders still to visit. This is what the computer's call stack does for you (Module 06 builds a call stack for Kestrel; Module 07 shows the real one in memory).

### Queue (first in, first out) and the circular buffer

A queue from a Python list with `pop(0)` is O(n) per dequeue (Lab 01). Fix it with a **circular buffer**: a fixed array with `head` and `tail` indices that wrap around with `% capacity` (M03!).

```python
# enqueue: buf[tail] = x; tail = (tail + 1) % cap; size += 1
# dequeue: x = buf[head]; head = (head + 1) % cap; size -= 1
```

Build `RingQueue` with a fixed capacity: `enqueue` raises (or returns False) when full, `dequeue` when empty. Then a growing version that doubles when full (copying items in **queue order** into the new array — the tricky part; draw it first).

**Invariant:** the items in the queue are `buf[head], buf[(head+1) % cap], …` for `size` items. Assert it in tests.

You'll meet this exact structure again in Module 09 (Courier's send and receive windows), Module 07 (a ring buffer in C), and Tone Loom's echo stretch goal.

---

## Session 3 — Mazes: BFS vs DFS

Text mazes:

```
##########
#S   #   #
# ## # # #
#  #   # #
## ##### #
#      #E#
##########
```

Build `maze.py`:
1. Parse the maze into a grid; neighbours are up/down/left/right open cells.
2. **DFS** (depth-first) with an explicit **stack**: find *a* path from S to E.
3. **BFS** (breadth-first) with your **queue**: find the **shortest** path. Keep a `came_from` dictionary to rebuild the path.
4. Print the maze with the path drawn in `.`, and report the number of cells each search **visited**.
5. Generate random mazes (a randomised DFS that knocks down walls is the classic method — look it up after trying to invent one) of size 51 × 51 and compare the two searches on 100 mazes.

**[W] Why does BFS find the shortest path?** (It explores all cells at distance 1, then all at distance 2, and so on — so the first time it reaches E, no shorter path exists. Write this as a short proof in your Proof Journal.) **Why doesn't DFS?**

---

## Done when

- [ ] `LinkedList`, bracket checker, iterative `size_of`, `RingQueue` (fixed and growing), all tested with invariant asserts.
- [ ] Maze solver with BFS and DFS; comparison on 100 random mazes; the BFS proof written.

## Retrieval and reflection

1. **[R]:** linked list vs array costs with reasons; stack and queue uses; circular buffer index math; BFS vs DFS behaviour.
2. **[F] (spoken):** "Why does BFS find the shortest path in a maze?"

**Next:** [Copydiff](../projects/copydiff/spec.md).
