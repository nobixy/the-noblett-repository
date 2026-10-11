---
title: "Project: Edit Buffer"
id: "MOD05-PRJ-edit-buffer"
type: "project"
module: "05-data-structures-and-algorithms"
phase: "C"
order: 830
prerequisites: [MOD05-LAB03]
artifact: "Four interchangeable text-buffer implementations (naive, list of lines, gap buffer, piece table) behind one API, with undo/redo, a line index, a benchmark suite driven by edit traces, and a small terminal editor that uses the fastest one"
deliverable: "Design doc + benchmark report + short demo of editing your journal in your own editor"
---

# Project: Edit Buffer

| | |
| :-- | :-- |
| **Module** | 05 Data Structures and Algorithms |
| **Prerequisites** | Labs 01–03 |
| **You build** | The data structure at the heart of every text editor: a buffer that supports fast insertion and deletion anywhere, undo and redo, and finding lines quickly. You build four versions behind one interface, test them all with the same suite, race them on realistic editing traces, and then put the winner inside a small terminal editor — which you use to write a journal entry |
| **Deliverable** | Design doc, benchmark report, and demo |

---

## Why this matters

Typing a letter in the middle of a 10 MB file looks instant in a good editor. With a plain string, every keystroke would copy megabytes. Editors solve this with clever structures: **gap buffers** (used by Emacs), **piece tables** (used by early Microsoft Word and by VS Code today), and **ropes** (used by some newer editors). Each makes different trade-offs.

This project is a pure study in **choosing a data structure for a workload**: you define the operations, write one test suite for all implementations, generate realistic workloads, and let measurements decide — then argue the choice in writing. That's exactly how engineers pick structures in real systems.

**Real-world analogs:** Emacs's gap buffer, VS Code's piece tree, the rope in Xi and Zed editors, undo stacks in every application.

---

## The API

Every implementation provides:

```python
class Buffer(Protocol):
    def insert(self, pos: int, text: str) -> None: ...
    def delete(self, pos: int, length: int) -> None: ...
    def text(self) -> str: ...                       # the whole content (may be slow)
    def slice(self, start: int, end: int) -> str: ...
    def __len__(self) -> int: ...
    def line_count(self) -> int: ...
    def line(self, n: int) -> str: ...               # 0-based line n, without its newline
    def pos_of_line(self, n: int) -> int: ...        # offset where line n starts
    def line_of_pos(self, pos: int) -> int: ...
    def undo(self) -> bool: ...                      # False if nothing to undo
    def redo(self) -> bool: ...
```

Positions are character offsets (Python string indices). Invalid positions raise `IndexError`.

---

## Milestones

### Milestone 1 — Design doc, API, naive buffer, and the shared test suite

1. **Design doc v1** (3–4 pages): the workloads you expect (typing, deleting words, pasting big blocks, jumping to line numbers, undo), predicted costs for each implementation, how undo will work in each, and goals with numbers.
2. **`NaiveBuffer`:** a single Python string. Correct and simple — your **reference model**.
3. **Shared test suite:** parametrised over all implementations (Module 02 Lab 02). Unit tests for every method, edge cases (insert at 0, at the end; delete everything; empty buffer; text with no trailing newline; consecutive newlines), and **differential random testing**: 10,000 random operation sequences (seeded), applied to the implementation under test and to `NaiveBuffer`; contents must match after every operation.
4. **Undo/redo semantics** (decide and document [W]): does undo revert one keystroke or one "word"? What happens to the redo history after a new edit? (Usually: it's discarded.)

**Done when:** `NaiveBuffer` passes the suite (including undo/redo).

### Milestone 2 — List of lines

`LinesBuffer`: a Python list of strings, one per line. Line lookups are now O(1); inserting a character copies only one line. But inserting text with newlines splits lines, and deleting across lines merges them — the tricky part. Write those as subgoals first [S]. Passes the suite.

### Milestone 3 — Gap buffer

A **gap buffer** is an array with an empty **gap** at the cursor:

```
[ H e l l o _ _ _ _ _ w o r l d ]
            ^gap_start  ^gap_end
```

Inserting at the gap just fills it: O(1). Moving the edit point means moving characters across the gap: O(distance moved). When the gap is full, grow it (Lab 01's doubling).

1. Implement it over a Python list of characters (or a `bytearray` for ASCII — decide and say why).
2. Undo: keep a stack of inverse operations (insert ↔ delete with the deleted text).
3. **Invariant** (assert in tests): `gap_start ≤ gap_end`, and the text equals `buf[:gap_start] + buf[gap_end:]`.

**[W]:** gap buffers are fast for typing in one place, slow for edits that jump around. Why does that match how people actually type?

### Milestone 4 — Piece table, and a line index

A **piece table** never modifies text. It keeps two strings:
- the **original** file contents (read-only),
- an **add** buffer (append-only: every inserted character is appended here),

and a list of **pieces**, each saying "take `length` characters from buffer B starting at `start`." The document is those pieces, in order.

- **Insert:** append the new text to the add buffer; split the piece at the insertion point into two, with a new piece in between.
- **Delete:** shrink or split pieces; no text is ever erased.
- **Undo** becomes elegant: since buffers never change, undo just restores an earlier **piece list**. Store piece-list snapshots or inverse piece operations on a stack. [W] Why is the append-only design so good for undo — and for crash safety? (Compare Study Deck's append-only log — and Module 11.)

**Line index:** for each piece, store how many newlines it contains (computed once when the piece is created). Then `line_of_pos` and `pos_of_line` can skip whole pieces. With the pieces in a list, finding the piece for a position is O(number of pieces); keep a list of **cumulative lengths** and use **binary search** to make it O(log pieces) (rebuilding the cumulative list after each edit costs O(pieces) — note this, and see the stretch goal for a balanced tree).

**Done when:** `PieceTable` passes the full suite, including line methods.

**Checkpoint:** [Milestone Checkpoint](<../../../04 - System/Milestone Checkpoint Template.md>). Feynman target: *how a piece table represents a document without changing any text*. Draw the pieces after three edits [R].

### Milestone 5 — Edit traces and the race

Realistic benchmarks need realistic workloads.

1. **Record a real trace:** write a tiny recorder that logs your edits as you type (Milestone 6's editor can do it; until then, generate one by "replaying" the diff between two versions of a long note from git history — Copydiff's edit scripts!).
2. **Synthetic traces** (seeded): (a) typing a 50,000-character document from start to end; (b) typing with frequent backspaces; (c) random edits jumping around a 1 MB file; (d) pasting 100 KB blocks in the middle; (e) jump to random line numbers and insert there; (f) 1,000 edits then 1,000 undos.
3. **Benchmark** all four implementations on every trace with `bench.py`: total time, time per operation (and the worst single operation — a pause the user would notice), and memory (`tracemalloc`).
4. **Predict first**, in a table, which implementation wins each trace and why. Then measure.

**Done when:** the full results table, with predictions beside measurements.

### Milestone 6 — A tiny editor

Build `ed5.py` (name it what you like), a terminal editor using Python's `curses` module and your fastest general-purpose buffer:
- open and save a file; arrow keys; typing; backspace and delete; Enter;
- Ctrl+Z / Ctrl+Y undo and redo;
- a status line: file name, line and column, "modified" marker;
- scrolling for files longer than the screen (only draw the visible lines — your line index makes this fast);
- **Ctrl+S saves safely:** write to a temporary file, then rename over the original (Spelling Engine's rule — and Module 11's).

**Use it:** write one real journal entry in your own editor. Note every annoyance — each is a feature request or a bug report (E09!).

**Done when:** you've written and saved a journal entry with it, and opened a 1 MB file without lag.

---

## Testing guidance

- **One suite, all implementations** — the most important design decision in this project.
- **Differential random testing** against the naive buffer, with seeds; when a sequence fails, **shrink** it (remove operations one at a time while it still fails) to find a minimal failing case — then make that a permanent regression test. (This is how professional property-based testing tools work.)
- **Invariant asserts** inside each structure in test mode.

## Common pitfalls

- **Off-by-one at piece boundaries** — the classic piece-table bug. Random differential tests find these fast.
- **Undo after a redo after an undo…** — write the sequence on paper and test it explicitly.
- **Newline handling:** `\r\n` files, a final line without `\n`, an empty file (zero lines or one?). Decide and document.
- **Benchmarking `text()`** by accident in every operation (it's O(n) for most structures).
- **curses quirks:** the terminal must be restored on exit even after an exception (`curses.wrapper` does this).

## Communication deliverable

1. **Design doc** v1 → v2 (with section 8: which predictions were wrong, and why).
2. **Benchmark report** (2 pages): predictions vs results per trace, worst-case pauses, memory, and your recommendation for a real editor.
3. **Demo:** your editor opening a large file, editing, undoing, and saving; then the results table.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Before Milestones 3 and 4, draw the gap buffer and piece table after a sequence of edits from memory |
| **F** | Piece tables; why gap buffers suit human typing |
| **W** | Undo semantics; append-only and crash safety; which structure for which trace |
| **S** | Subgoals for line splitting/merging, piece splitting |
| **I** | Arrays, lists, binary search, stacks, and amortisation in one project |
| **T** | Design doc, report, demo — and a journal entry written in your own editor |

## Stretch goals

- **Piece tree:** store pieces in a balanced binary tree (e.g. a treap or red-black tree) keyed by position, so finding and splitting a piece is O(log n) without rebuilding a cumulative array — the design VS Code uses.
- **Rope:** a balanced tree of string chunks; compare with the piece tree.
- **Multiple cursors** in the editor.
- **Search** in the editor using Vault Search's tokenizer — or simple substring search with the Knuth–Morris–Pratt algorithm.

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Test suite | Shared, differential, shrinking, regression cases | Shared unit tests | Per-implementation tests |
| Implementations | Four, all passing, with invariants | Three | Fewer |
| Undo/redo | Semantics documented and tested in every implementation | Most | Missing |
| Benchmarks | Real + 6 synthetic traces; predictions vs measurements; worst-case and memory | Partial | Missing |
| Editor | Used for a real entry; safe save; large files smooth | Basic | Missing |
| Communication | Doc lifecycle, report, demo | Most | Few |

**Done when:** every area at least 2; Test suite at 3.

## Connections

- **Back:** Lab 01 (amortised growth), Lab 03 (stacks), Copydiff (edit scripts as traces), Study Deck (append-only design), Spelling Engine (safe saves).
- **Forward:** Module 07 (the gap buffer in C, with real memory), Module 11 (append-only logs and crash safety in a database), Module 10 (your browser's text layout reads lines from a buffer).

> **Originality note:** the multi-implementation framework, trace-driven benchmarks, and milestones were written for this curriculum. Gap buffers and piece tables are classic published techniques used here as components.
