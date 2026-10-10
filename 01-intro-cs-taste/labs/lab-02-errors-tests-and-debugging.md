---
title: "Lab 02 — Errors, Tests, and Debugging"
module: "01-intro-cs-taste"
hours: 4
---

# Lab 02 — Errors, Tests, and Debugging

**Goal:** stop fearing error messages; write tests that prove your code works; and have a calm, step-by-step method for finding bugs.

**Time:** about 4 hours, in two sessions.

**Before you start:** [Lab 01](lab-01-python-first-steps.md) done.

---

## Session 1 — Reading errors (2 hours)

### An error message is a bug report written by the computer

When Python hits a problem, it prints a **traceback**. It looks scary. It's actually a precise, helpful report — exactly the kind you're learning to write in E09.

```
Traceback (most recent call last):
  File "/home/you/workbench/01-python/scores.py", line 12, in <module>
    print(average(scores))
  File "/home/you/workbench/01-python/scores.py", line 4, in average
    return sum(numbers) / len(numbers)
ZeroDivisionError: division by zero
```

**Read it from the bottom up** [S]:
1. **Last line — what went wrong:** `ZeroDivisionError: division by zero`. The *type* of error, then a description.
2. **The line just above — where:** line 4, inside the function `average`: `return sum(numbers) / len(numbers)`. `len(numbers)` must have been 0: the list was empty.
3. **Further up — how you got there:** line 12 called `average(scores)`. So `scores` was empty when it was called.
4. **Ask:** why was it empty? *That's* the real bug. The crash is only where it showed up.

### The common error types

| Error | Usually means | Example |
| :-- | :-- | :-- |
| `SyntaxError` | Python can't even read the line: missing bracket, colon, or quote | `if x > 3` (missing `:`) |
| `IndentationError` | spaces don't line up | a line inside an `if` not indented |
| `NameError` | a name that doesn't exist (often a typo — your spelling log helps here!) | `pirnt("hi")` |
| `TypeError` | the wrong kind of value for an operation | `"5" + 5` |
| `ValueError` | the right kind, but a bad value | `int("five")` |
| `IndexError` | a list index past the end | `[1, 2, 3][3]` |
| `KeyError` | a dictionary key that isn't there | `{"a": 1}["b"]` |
| `FileNotFoundError` | the path is wrong, or you ran from the wrong folder | `open("nots.txt")` |
| `ZeroDivisionError` | dividing by zero (M03 explains why it's impossible) | `1 / 0` |

### Practice: break things on purpose

Write a tiny program and cause **each** error in the table above on purpose. For each, read the traceback bottom-up and write one sentence: *what happened, and on which line*. Breaking things deliberately makes real errors familiar.

**[W]:** why is it better for a program to crash loudly with a clear error than to keep running with a wrong value? (Think about a bank, or the `0.1 + 0.2` problem.)

---

## Session 2 — Tests and debugging (2 hours)

### Tests: code that checks code

A **test** runs your code on an input where you already know the right answer, and complains if the answer is wrong.

The simplest test is an `assert`:

```python
from conversions import to_binary

assert to_binary(0) == "0"
assert to_binary(5) == "101"
assert to_binary(255) == "11111111"
print("all tests passed")
```

If an `assert` is false, Python stops with `AssertionError`.

### pytest

**pytest** finds and runs tests for you and reports clearly. (Install: `sudo pacman -S python-pytest`, or `pip install pytest` inside a virtual environment.)

1. Put tests in a file whose name starts with `test_`, e.g. `test_conversions.py`.
2. Each test is a function whose name starts with `test_`:

```python
# test_conversions.py
from conversions import to_binary, from_binary

def test_small_numbers():
    assert to_binary(0) == "0"
    assert to_binary(1) == "1"
    assert to_binary(5) == "101"

def test_round_trip():
    for n in range(1000):
        assert from_binary(to_binary(n)) == n

def test_matches_builtin():
    for n in range(1000):
        assert to_binary(n) == bin(n)[2:]
```

3. Run `pytest` in that folder. Green dots mean passed; `F` means failed, with a report showing the values.

### What to test

For every function, write tests for:
- **Typical cases:** normal inputs with known answers (worked by hand first!).
- **Edge cases:** the smallest, largest, empty, zero, one, negative. Most bugs live at the edges.
- **Round trips:** if you have a pair of functions that undo each other (to/from binary, save/load), check that doing both gives back the start.
- **A second witness:** compare with a slower, simpler, or built-in way of getting the same answer.
- **Every bug you fix:** write a test that fails with the bug and passes without it, *before* fixing it. This is called a **regression test**, and it stops the bug from coming back.

### Debugging: a calm method

When something's wrong, don't randomly change things. Follow these subgoals [S]:

1. **Reproduce:** find the exact input that makes it go wrong. Write it down. (This is the "steps to reproduce" of a bug report.)
2. **Shrink:** make the input as small as possible while it still fails.
3. **Predict, then look:** add `print()` lines that show the values at key points. **Before running, write what you expect each to print.** The first place where reality differs from your prediction is where the bug is.
4. **Explain:** say out loud what the code does, line by line, to an imaginary listener (or a rubber duck — programmers really do this). You'll often hear yourself say the wrong thing.
5. **Fix, then test:** add a regression test, fix the code, run all tests.
6. **Write it down:** a two-line note in your log: the symptom, and the cause. You'll start to see your own patterns.

**The 90-minute rule [D]:** if you're still stuck after 90 minutes in one sitting, write a **stuck note** (what you're trying to do; what you tried; what you think is wrong), and stop. Walk. Sleep. Tomorrow, read only the stuck note and start from step 2.

### Practice

The function below has **three** bugs. Write tests first that expose them, then find and fix them using the method above.

```python
def median(numbers):
    """Return the middle value of a list of numbers (average of the two middles if even)."""
    numbers.sort()
    mid = len(numbers) / 2
    if len(numbers) % 2 == 1:
        return numbers[mid]
    return numbers[mid] + numbers[mid + 1] / 2
```

<details>
<summary>Hints (open only after trying for 25 minutes)</summary>

1. What type is `len(numbers) / 2`? Can you use it as a list index? (`/` vs `//`.)
2. For an even-length list like `[1, 2, 3, 4]`, which two indexes are the middle ones? (1 and 2, not 2 and 3.)
3. Order of operations (M07): what does `a + b / 2` compute?
4. A fourth, sneakier issue: `numbers.sort()` changes the caller's list. Is that OK? (Use `sorted(numbers)` to avoid surprising the caller.)
</details>

---

## Done when

- [ ] You've caused and read every error type in the table.
- [ ] `test_conversions.py` (or similar) runs green under `pytest`.
- [ ] The `median` function is fixed, with tests that would have caught all its bugs.
- [ ] You can recite the six debugging subgoals from memory [R].

## Retrieval and reflection

1. **Blank sheet (10 min):** how to read a traceback; five kinds of tests; the six debugging steps.
2. **Feynman (spoken, 1 min):** "Why write a test before fixing a bug?"

**Next:** the projects. Start with [Nib, a tiny computer](../projects/nib-machine/spec.md).
