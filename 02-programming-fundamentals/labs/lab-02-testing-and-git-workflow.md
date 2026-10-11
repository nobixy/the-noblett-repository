---
title: "Lab 02 — Testing and Git Workflow"
id: "MOD02-LAB02"
type: "lab"
module: "02-programming-fundamentals"
phase: "B"
order: 440
prerequisites: [MOD02-LAB01]
---

# Lab 02 — Testing and Git Workflow

**Goal:** testing habits and git habits that working programmers use daily: test-first development, fixtures, parametrised tests, golden files, fake clocks, branches, merges, conflicts, and bisect.

**Sessions:** three.

**You'll finish with:** `roman.py` built test-first; a deliberately caused and resolved merge conflict; and a bug found with `git bisect`.

---

## Session 1 — pytest beyond `assert`

### Parametrised tests: one test, many cases

```python
import pytest
from roman import to_roman

@pytest.mark.parametrize("n, expected", [
    (1, "I"), (4, "IV"), (9, "IX"), (14, "XIV"),
    (40, "XL"), (90, "XC"), (400, "CD"), (1994, "MCMXCIV"), (2026, "MMXXVI"),
])
def test_to_roman(n, expected):
    assert to_roman(n) == expected
```

Each row runs as its own test, and failures name the row.

### Testing errors

```python
def test_rejects_zero():
    with pytest.raises(ValueError):
        to_roman(0)
```

### Floats: never `==`

```python
assert 0.1 + 0.2 == pytest.approx(0.3)     # M06 Part 7
```

### Fixtures: shared setup

A **fixture** is a function that prepares something a test needs. pytest passes it in by name.

```python
def test_writes_file(tmp_path):          # tmp_path is a built-in fixture: a fresh empty folder
    out = tmp_path / "out.txt"
    save_report(out, ["a", "b"])
    assert out.read_text() == "a\nb\n"
```

Your own fixture:

```python
@pytest.fixture
def sample_deck(tmp_path):
    p = tmp_path / "deck.md"
    p.write_text("Q: 7 x 8?\nA: 56\n")
    return p
```

### Test-first development (red → green → refactor)

1. **Red:** write one small failing test for the next bit of behaviour.
2. **Green:** write the simplest code that makes it pass.
3. **Refactor:** clean up the code while all tests stay green.
4. Repeat.

Writing the test first forces you to decide *what* the function should do before *how*. That's the contract from Lab 01, written as code.

### Build: `roman.py`, test-first

`to_roman(n)` for 1–3,999 and `from_roman(s)` back again. Strict red-green-refactor: commit after each green (`git commit -m "Handle subtractive pairs like IV and IX"`). Final tests must include:
- a parametrised table of at least 15 cases each way;
- a **round-trip** test: `from_roman(to_roman(n)) == n` for all 1–3,999;
- errors: 0, 4,000, `"IIII"`, `"IC"`, `"ABC"` all raise `ValueError` (decide which invalid forms you reject, and document it).

---

## Session 2 — Golden files and fake clocks

### Golden files

When output is long (a rendered page, a game transcript, a WAV file), store a known-good copy — the **golden file** — and compare future output against it.

```python
from pathlib import Path

GOLDEN = Path(__file__).parent / "golden"

def test_render_matches_golden():
    out = render(parse(Path("pages/example.pml").read_text()), width=60)
    expected = (GOLDEN / "example_60.txt").read_text()
    assert "\n".join(out) + "\n" == expected
```

**Rules:**
- Create the golden file once, **inspect it carefully by eye**, then commit it.
- When output changes on purpose, regenerate it (a `--update-golden` option or a small script) and review the `git diff` of the golden file. That diff *is* your review.
- Never regenerate golden files to make a failing test pass without understanding why it failed.

### Fake clocks: testing code that depends on time

Code that uses `datetime.date.today()` is hard to test: tomorrow, the answer changes. Fix: **pass the clock in** as a parameter.

```python
from datetime import date

def due_cards(cards, today):          # today is passed in, not looked up inside
    return [c for c in cards if c.due <= today]

def test_due_cards():
    cards = [Card(due=date(2026, 10, 1)), Card(due=date(2026, 10, 20))]
    assert len(due_cards(cards, today=date(2026, 10, 10))) == 1
```

The real program calls `due_cards(cards, today=date.today())`. Tests pass any date they like, including "100 days from now." This idea — **give a function what it needs instead of letting it reach out for it** — is called **dependency injection**, and it's the key to testing [Study Deck](../projects/study-deck/spec.md).

**Exercise:** take any time-dependent function from your earlier projects (the Spelling Engine's quiz is a good one) and refactor it to take `today` as a parameter. Write two tests that simulate a week of use.

---

## Session 3 — Git like a professional

### Branches

A **branch** is a separate line of commits. Work on a feature without disturbing `main`, then merge it in.

```bash
git switch -c add-from-roman      # create and switch to a new branch
# ... edit, test, commit ...
git switch main
git merge add-from-roman          # bring the work into main
git branch -d add-from-roman      # delete the finished branch
```

See the shape: `git log --oneline --graph --all`.

### Make a conflict on purpose (and fix it)

1. On `main`, change line 1 of `README.md` to "Roman numeral converter". Commit.
2. `git switch -c other HEAD~1` (a branch from *before* that commit). Change line 1 to "Roman numerals, both ways". Commit.
3. `git switch main` then `git merge other`. Git reports a **conflict**.
4. Open `README.md`. You'll see:
   ```
   <<<<<<< HEAD
   Roman numeral converter
   =======
   Roman numerals, both ways
   >>>>>>> other
   ```
5. Edit it into the line you actually want, remove the markers, then `git add README.md` and `git commit`.

**[W]:** why can't git decide this automatically? (Both changes are "correct"; only a human knows the intent.)

### Find a bug with `git bisect`

`git bisect` finds the commit that introduced a bug by **binary search** through history (M11: about log₂ n steps for n commits).

1. In `roman.py`, make 10 small harmless commits. In the 6th, quietly introduce a bug (e.g. break the `"CM"` case). Don't note which one.
2. Wait until a later session (so you forget).
3. ```bash
   git bisect start
   git bisect bad                 # the current commit is broken
   git bisect good HEAD~10        # this old one was fine
   # git checks out a middle commit. Run the tests, then:
   git bisect good   # or: git bisect bad
   # ... repeat until git names the first bad commit ...
   git bisect reset
   ```
4. Automate it: `git bisect run pytest -q`.

How many steps did it take for 10 commits? Compare with log₂ 10.

### Habits

- **Small commits** with imperative messages (E05). One logical change each.
- **Never commit broken tests to `main`.** Run `pytest` before every commit.
- **Read your diff** (`git diff --staged`) before committing. It's proofreading for code.
- **A README in every project** (E09 Part 5).

---

## Done when

- [ ] `roman.py` built test-first, with commits showing red-green steps; round-trip and error tests pass.
- [ ] One golden-file test and one fake-clock test written for earlier work.
- [ ] A merge conflict resolved; `git bisect run` found your planted bug.

## Retrieval and reflection

1. **[R] Blank sheet:** red-green-refactor; three kinds of pytest helpers (parametrize, raises, fixtures); the golden-file rules; why inject the clock; the branch-merge commands; how bisect works and why it's fast.
2. **[F] (spoken):** "What is a golden file, and when is it dangerous?"

**Next:** [Lab 03 — Classes and Data Modelling](lab-03-classes-and-data-modelling.md).
