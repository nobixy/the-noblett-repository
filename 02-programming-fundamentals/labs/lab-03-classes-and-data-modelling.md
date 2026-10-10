---
title: "Lab 03 — Classes and Data Modelling"
module: "02-programming-fundamentals"
hours: 10
---

# Lab 03 — Classes and Data Modelling

**Goal:** model the things your program is about as **classes** with clear **invariants** — rules that must always be true — so that whole categories of bugs become impossible.

**Time:** about 10 hours, in three sessions.

**You'll finish with:** a `Ratio` class (an exact fraction type, built from M04–M05) whose invariant guarantees it's always in simplest form, and a small `Library` model with loans and due dates.

---

## Session 1 — Classes (3 hours)

### Why classes?

So far you've stored records as dictionaries: `{"wrong": "seperate", "right": "separate", "box": 2}`. That works, but nothing stops `box` from being `-7` or `"two"`, or a typo like `"bxo"` from creating a new key. A **class** defines a kind of thing, with named attributes and the operations that make sense for it.

```python
class Card:
    """One flashcard: a question, an answer, and its Leitner box (1–5)."""

    def __init__(self, question: str, answer: str, box: int = 1):
        if not 1 <= box <= 5:
            raise ValueError(f"box must be 1-5, got {box}")
        self.question = question
        self.answer = answer
        self.box = box

    def promote(self):
        """Move up one box after a correct answer (max 5)."""
        self.box = min(self.box + 1, 5)

    def demote(self):
        """Back to box 1 after a wrong answer."""
        self.box = 1

    def __repr__(self):
        return f"Card({self.question!r}, box={self.box})"
```

- `__init__` runs when you create one: `c = Card("7 x 8?", "56")`.
- `self` is the particular card the method is working on.
- **Methods** are functions that belong to the class: `c.promote()`.
- `__repr__` controls how it prints in the REPL and in error messages. Always write one; debugging is much easier.
- **Type hints** (`question: str`) document what each attribute should be. Python doesn't enforce them, but your editor and readers use them.

### Invariants

An **invariant** is a statement that must be true for every object of the class, at every moment between method calls. For `Card`: *`box` is an integer from 1 to 5.*

**Rules for keeping invariants:**
1. Check them when the object is created (`__init__`).
2. Make sure **every method** keeps them true.
3. Don't let outside code change attributes in ways that break them. (In Python this is a convention: outside code shouldn't assign `c.box = 9`. Methods like `promote` are the way to change state.)

Write the invariants in the class docstring. When a bug appears, the first question is: *which invariant was broken, and by whom?*

### Dataclasses: less typing

```python
from dataclasses import dataclass, field
from datetime import date

@dataclass
class Review:
    card_id: str
    when: date
    correct: bool
```

`@dataclass` writes `__init__`, `__repr__`, and `__eq__` for you. Add checks in `__post_init__`:

```python
@dataclass
class Card:
    question: str
    answer: str
    box: int = 1
    def __post_init__(self):
        if not 1 <= self.box <= 5:
            raise ValueError("box must be 1-5")
```

`@dataclass(frozen=True)` makes objects **immutable** (attributes can't change after creation). Immutable objects can't break their invariants later, can be dictionary keys, and are safe to share. The cost: to "change" one, you make a new one.

### Enums: a fixed set of choices

```python
from enum import Enum

class Grade(Enum):
    AGAIN = 0
    HARD = 1
    GOOD = 2
    EASY = 3
```

Better than strings like `"good"`, where a typo silently becomes a new value.

---

## Session 2 — Build: the `Ratio` class (4 hours)

Build your own exact fraction type, using M04 (GCD) and M05 (fractions). Python already has `fractions.Fraction` — you'll use it as a second witness in your tests.

**Invariants (write them in the docstring):**
1. `den > 0` (the sign lives in the numerator).
2. `gcd(abs(num), den) == 1` (always in simplest form).
3. Zero is stored as `0/1`.

**Required:**
- `Ratio(num, den=1)` — normalises on creation: `Ratio(6, -8)` becomes `-3/4`. `den == 0` raises `ZeroDivisionError`.
- `+ − × ÷` via the special methods `__add__`, `__sub__`, `__mul__`, `__truediv__` — each returns a **new** `Ratio` (so make it frozen).
- `==` and `<` (`__eq__`, `__lt__`).
- `__repr__` → `Ratio(-3, 4)`; `__str__` → `-3/4`; a method `mixed()` → `"1 1/3"` for 4/3. Decide how to show negative mixed numbers (for example `-1 1/3` meaning −(1 + 1/3)), and document the choice [W].
- `Ratio.parse("1 1/3")` → `4/3` (mixed numbers, as in the Ratio Workshop).
- `to_float()`.

**Subgoal labels [S]** for `__init__`:
```python
# 1. Reject den == 0
# 2. Move the sign to the numerator
# 3. Divide both by their GCD
# 4. Store; zero becomes 0/1
```

**Tests:**
- Every invariant holds after **every** operation: write a helper `check_invariants(r)` and call it in every test.
- Compare with `fractions.Fraction` on 10,000 random operations (random numerators −100…100, denominators 1…100). This is **differential testing**: two independent implementations must agree.
- Division by a zero `Ratio` raises `ZeroDivisionError`.

**[W]:** Why is "always in simplest form" a good invariant? (Hint: what would `==` have to do otherwise? How big would the numbers get after 50 additions?)

---

## Session 3 — Modelling a small domain (3 hours)

### Model a lending library

A library lends items to members. Design the classes **on paper first**:

- What are the *things*? (Item, Member, Loan…)
- What are each thing's attributes, and their types?
- What are the **invariants**? Some to consider:
  - An item is on at most one active loan.
  - A loan's due date is after its start date.
  - A member has at most 5 active loans.
  - Returning an item that isn't on loan is an error.
- What **operations** change state? (`lend(item, member, today)`, `return_item(item, today)`, `overdue(today)`.)

Then build `library.py` with a `Library` class that owns the items, members, and loans, and enforces every invariant in its methods. Pass `today` in (fake clock, Lab 02).

**Tests:** one test per invariant that tries to break it and expects an exception; a 30-day simulated scenario with lends, returns, and an overdue report.

### Composition vs inheritance (a short note)

You can build classes from other classes in two ways:
- **Composition:** a `Library` *has* items and members (attributes that are other objects).
- **Inheritance:** a `Book` *is an* `Item` (`class Book(Item):`), getting its attributes and methods.

Prefer composition. Use inheritance only for a true "is a" relationship where the child really can be used anywhere the parent is expected. Deep inheritance trees are one of the most common causes of hard-to-change code.

---

## Done when

- [ ] `Ratio` passes invariant checks after every operation and agrees with `Fraction` on 10,000 random cases.
- [ ] `library.py` enforces all invariants, with a test trying to break each.
- [ ] Your design sketch for the library (paper photo or Markdown) is committed beside the code.

## Retrieval and reflection

1. **[R] Blank sheet (10 min):** what a class is; what an invariant is and the three rules for keeping one; dataclass vs class; frozen and why; composition vs inheritance.
2. **[F] (spoken, 2 min):** "What is an invariant? Use your `Ratio` class."
3. **[W]:** pick one invariant from the library. Which *method* would break it if you forgot one line? What test catches that?

**Next:** the projects, starting with [Study Deck](../projects/study-deck/spec.md).
