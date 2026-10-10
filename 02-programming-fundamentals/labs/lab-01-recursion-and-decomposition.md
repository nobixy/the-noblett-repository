---
title: "Lab 01 — Recursion and Decomposition"
module: "02-programming-fundamentals"
hours: 10
---

# Lab 01 — Recursion and Decomposition

**Goal:** two ways of making big problems small. **Decomposition**: split a problem into named pieces, each a function with one job. **Recursion**: solve a problem by solving a smaller copy of the same problem.

**Time:** about 10 hours, in four sessions.

**You'll finish with:** `calendar_print.py` (a decomposed program), a set of recursive functions with tests, and `treesize.py` — a tool that walks a real folder tree and reports sizes, like `du` and `tree` combined.

---

## Session 1 — Decomposition (2 hours)

### The idea

A program that does one big thing is hard to write, read, test, and fix. Split it into functions, each with **one job you can describe in one sentence**. Then each function is easy, and the big thing is just the small things in order.

**Top-down design [S]:**
1. Write the whole task as one sentence.
2. Write the 3–6 steps it needs, as **function names with a one-line description each** (no code yet).
3. For each step that's still too big, repeat step 2 inside it.
4. Stop when every function's body would be about 5–15 lines.
5. Write the small ones first, test each, then assemble.

### The contract of a function

For every function, before writing it, write three things in its docstring:
- **Takes:** what inputs, of what type, with what limits.
- **Returns:** what output.
- **Promises / requires:** anything else true before or after (e.g. "never changes the input list", "raises `ValueError` if `month` isn't 1–12").

This is called the function's **contract**. If every function keeps its contract, the program works. When something breaks, you check contracts one by one.

### Build: `calendar_print.py`

Print a month like this, for any month and year given on the command line, **without** using Python's `calendar` module:

```
    October 2026
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31
```

**First, decompose on paper.** A possible top level (yours may differ):

```python
def print_month(year, month): ...           # the whole task
def is_leap_year(year): ...                  # every 4 years, except centuries, except every 400
def days_in_month(year, month): ...
def weekday_of(year, month, day): ...        # 0 = Monday ... 6 = Sunday
def month_grid(year, month): ...             # list of weeks; each week a list of 7 day-numbers or None
def format_grid(title, grid): ...            # list of text lines
```

For `weekday_of`, count days from a date whose weekday you know (January 1, 2001 was a Monday), and use `% 7` (M03!). Test it against a real calendar for five dates.

**Tests:** `is_leap_year` for 1900 (no), 2000 (yes), 2024 (yes), 2026 (no); `days_in_month(2024, 2) == 29`; `month_grid` has the right first weekday for three known months.

**[W]:** why is `format_grid` separate from `month_grid`? (Hint: what if you later want HTML output — like Pagelet's parse/render split?)

---

## Session 2 — Recursion: the idea (3 hours)

### A smaller copy of the same problem

Some problems contain smaller versions of themselves:
- The sum of a list = the first item + **the sum of the rest of the list**.
- A folder's total size = the sizes of its files + **the total sizes of its subfolders**.
- 2¹⁰ = 2 × **2⁹**.

A **recursive function** calls itself on the smaller version.

```python
def total(numbers):
    """Return the sum of a list of numbers."""
    if not numbers:                      # base case: the smallest problem
        return 0
    return numbers[0] + total(numbers[1:])   # recursive case: a smaller problem
```

### The three rules [S]

Every recursive function needs:
1. **A base case:** the smallest input, answered directly without recursion.
2. **A recursive case:** solve a *smaller* input by calling yourself, then combine.
3. **Progress:** every call must move toward the base case. If it doesn't, the function calls itself forever (Python stops it with `RecursionError` after about 1,000 calls).

**Subgoal labels for writing any recursive function:**
1. *What's the smallest input, and its answer?* (base case)
2. *If someone handed me the answer for a slightly smaller input, how would I get the answer for this one?* (recursive case)
3. *Does each call get closer to the base case?* (progress)
4. *Test the base case first, then one step above it, then bigger.*

Step 2 is the magic. You **trust** the recursive call to work (this is called the "recursive leap of faith") and only think about one level.

### The call stack (on paper)

Each call gets its own **frame**: its own copies of its variables. Frames stack up, then unwind. Trace `total([3, 5, 2])`:

```
total([3, 5, 2])
  = 3 + total([5, 2])
          = 5 + total([2])
                  = 2 + total([])
                          = 0          ← base case
                  = 2 + 0 = 2
          = 5 + 2 = 7
  = 3 + 7 = 10
```

Draw this for every function in Session 3's exercises until it feels natural [R]. You'll see the real call stack in memory in Module 07, and build one for Kestrel in Module 06.

> **[W] Why does the leap of faith work?** It's the same reasoning as a proof by induction (Module 03): if the base case is right, and each step is right *assuming* the smaller one is right, then every case is right. Recursion and induction are the same idea, one in code and one in proof.

---

## Session 3 — Recursion: exercises (3 hours)

Write each function recursively (no loops), with a docstring and tests. Predict the result for small inputs on paper first.

1. **`count_down(n)`** — print n, n − 1, …, 1, then "liftoff".
2. **`reverse(s)`** — reverse a string. (*Hint:* reverse of `"abc"` = reverse of `"bc"` + `"a"`.)
3. **`to_binary(n)`** — the binary digits of n as a string. (*Hint:* M03's repeated division, written recursively: the digits of n are the digits of `n // 2`, followed by `n % 2`.)
4. **`power(b, e)`** — bᵉ for whole e ≥ 0, using **fast exponentiation**: if e is even, bᵉ = (b^(e/2))²; if odd, bᵉ = b × bᵉ⁻¹. Count how many multiplications it uses for e = 1,000 compared with the slow way. (You'll use this exact algorithm in Module 03's toy cipher.)
5. **`gcd(a, b)`** — Euclid, recursively: gcd(a, 0) = a; otherwise gcd(b, a % b). (M04.)
6. **`flatten(nested)`** — turn `[1, [2, [3, 4]], 5]` into `[1, 2, 3, 4, 5]`. (*Hint:* `isinstance(x, list)`.)
7. **`paths(rows, cols)`** — the number of ways to walk along the grid lines from the top-left corner to the bottom-right corner of a grid of `rows` × `cols` squares, moving only right or down. (Base case: if `rows` or `cols` is 0, there's exactly one way — a straight line.) Then try `paths(16, 16)`. It's slow. Why? Add a dictionary that remembers answers you've already computed (`memo`). How much faster? (This trick, **memoization**, is the doorway to dynamic programming in Module 05.)
8. **`permutations(items)`** — all orderings of a list. How many for 4 items? For n items? (M11's growth table, and Module 03's counting.)

<details>
<summary>Check your answers</summary>

3. `to_binary(37)` → `"100101"`. 4. Fast exponentiation for e = 1,000 uses about 2 × log₂ 1,000 ≈ 20 multiplications or fewer, versus 999. 6. Recursive case: for each element, if it's a list, extend with `flatten(element)`, else append it. 7. `paths(1, 1)` = 2, `paths(2, 2)` = 6, `paths(16, 16)` = 601,080,390. Without memoization it makes over a billion calls; with it, about 300 (one per distinct (rows, cols) pair). (Module 03 shows the closed form: choose which 16 of the 32 moves go right.) 8. 4! = 24; n! in general.
</details>

**Iteration or recursion?** Anything recursive can be written with a loop, and vice versa. Use recursion when the problem's **shape is recursive** (trees, nested lists, divide-and-conquer). Use loops for simple repetition. Python has a recursion limit of about 1,000, so very deep recursion (like `total` on a list of 10,000 items) should be a loop.

---

## Session 4 — Build: `treesize.py` (2 hours)

A real tool for a truly recursive problem: **folders contain folders**.

`python3 treesize.py ~/workbench --depth 2` prints:

```
~/workbench                         4.2 MiB
├── 01-nib                          120.0 KiB
│   ├── nib.py                       14.1 KiB
│   └── tests                        22.3 KiB
├── 01-pagelet                       88.4 KiB
...
```

**Requirements:**
- `size_of(path)` returns the total bytes of a file or folder, **recursively** (use `os.scandir`; `entry.is_dir(follow_symlinks=False)`; `entry.stat(follow_symlinks=False).st_size`).
- Children sorted by size, largest first.
- `--depth N` limits how deep the *printing* goes (but sizes always include everything below).
- Sizes in human units (KiB, MiB, GiB — M06's 1,024 rule).
- Folders you can't read (permission denied) are shown as `(no access)` and counted as 0, without crashing.
- **Symlinks are not followed.** (Why? [W] Think about a link that points to its own parent folder.)

**Tests:** make a temporary folder tree in a test (pytest's `tmp_path`, see Lab 02) with known file sizes; check `size_of` and the printed order. Compare one real folder against `du -sb <folder>`.

**Decompose first** (Session 1): sizing, sorting, formatting sizes, and printing the tree are separate functions.

---

## Done when

- [ ] `calendar_print.py` matches a real calendar for three months, with tests.
- [ ] All eight recursive exercises written and tested; memoized `paths` explained.
- [ ] `treesize.py` agrees with `du -sb` and handles permission errors and symlinks.

## Retrieval and reflection

1. **[R] Blank sheet (15 min):** top-down design steps; a function contract's three parts; the three rules of recursion; the four recursion subgoals; a traced call stack for `reverse("abc")`.
2. **[F] (spoken, 2 min):** "What is recursion, and why does trusting the smaller call work?"
3. **[W]:** why did memoization make `paths` so much faster? (Draw the tree of calls for `paths(3, 3)` and circle the repeats.)
4. Flashcards: the three rules; fast exponentiation; memoization.

**Next:** [Lab 02 — Testing and Git Workflow](lab-02-testing-and-git-workflow.md).
