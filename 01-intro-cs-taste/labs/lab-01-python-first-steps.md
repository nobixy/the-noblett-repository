---
title: "Lab 01 — Python First Steps"
id: "MOD01-LAB01"
type: "lab"
module: "01-intro-cs-taste"
phase: "A"
order: 240
prerequisites: [MOD01-LAB00]
sessions: 10
---

# Lab 01 — Python First Steps

**Goal:** enough Python to build the four Module 01 projects, learned in ten short sessions. Each session teaches a few ideas, then you build a small working program with them.

**Sessions:** ten, as build sessions alongside the foundations.

**Before you start:** [Lab 00](lab-00-machine-setup.md) done. Python runs.

---

## Skip check

Already written some Python? Try this **cold**, with only the official Python docs open. If you can do all of it, tick Lab 01 as done and go to [Lab 02](lab-02-errors-tests-and-debugging.md).

1. Write `time_split.py` (Session 1): turn a number of seconds into hours, minutes, and seconds using `//` and `%`.
2. Write a function that takes a list of words and returns a dictionary of word counts, then prints the five most common, sorted.
3. Read a text file line by line, skip blank lines, and write the results to a new file with `with open(...)`.
4. Split a program into two files and `import` one from the other; read a file name from `sys.argv`.
5. Explain out loud: what a variable is, what a function is, and the difference between a list and a dictionary.

Partial pass? Start at the first session whose topic you missed (Sessions 1–10 are listed below) and do every session from there; the Session 10 adventure is worth doing either way.

---

## How each session works

1. **Learn:** read the short explanation. Type every example yourself — **don't copy and paste**. Typing is how your fingers learn the syntax (this is copywork [C] for code).
2. **Try:** the small exercises. Predict the output *before* running each one. Wrong predictions are where you learn the most.
3. **Build:** a small program using the session's ideas. Write the **subgoal labels as comments first** [S], then fill in code.
4. **Recall [R]:** close everything. On paper, write the session's key code from memory. Then check.
5. **Review [I]:** answer the review questions, which mix this session with earlier ones.
6. **Commit** your work to `~/workbench/01-python/`, with an imperative message.

**Flashcards:** add 3–5 cards per session (syntax and meanings). Example: *Q: What does `7 // 2` give? A: 3 (integer division).*

**Stuck?** Three honest attempts, then a stuck note and a break [D]. Read the error message slowly, word by word (Lab 02 teaches this properly).

---

## Session 1 — Numbers and variables

### Learn

Start the REPL with `python3`. Python is a calculator:

```python
>>> 7 + 3
10
>>> 7 - 3
4
>>> 7 * 3
21
>>> 7 / 2          # division always gives a decimal number
3.5
>>> 7 // 2         # integer division: how many whole 2s fit (M03)
3
>>> 7 % 2          # modulo: the remainder (M03)
1
>>> 2 ** 10        # power (M07)
1024
```

Python follows the **order of operations** (M07): `2 + 3 * 4` is `14`. Use brackets to be clear: `(2 + 3) * 4` is `20`.

**Variables** are names for values. `=` means **put this value into this name** (assignment — not "equals" as in algebra; see M08 Part 1).

```python
>>> seconds = 7530
>>> hours = seconds // 3600
>>> hours
2
>>> seconds = seconds % 3600   # replace with what's left over
>>> seconds
330
```

**Names:** lowercase words joined by underscores: `total_bytes`, `user_count`. A name says what's inside (E04 Part 3).

**Two kinds of number:** `int` (whole: `7`, `-3`, `1024`) and `float` (decimal: `3.5`, `0.1`). `type(7)` tells you which.

`print()` shows values when you run a file (the REPL shows them automatically):

```python
print(hours, "hours")
```

### Try (predict first, then run)

1. `17 // 5` and `17 % 5`
2. `-7 // 2` (surprise! Python rounds *down*, toward minus infinity)
3. `2 ** 8 - 1`
4. `0.1 + 0.2` (M06 Part 7 explains this)
5. `x = 5`, then `x = x + 1`, then `x` (what's in `x` now, and why does this make sense in code but not in algebra?)

### Build: `time_split.py`

A program that turns a number of seconds into hours, minutes, and seconds.

```python
# 1. Choose a number of seconds
# 2. Work out the whole hours, and what's left
# 3. Work out the whole minutes from what's left, and the seconds remaining
# 4. Print the result as H:M:S
```

For 7,530 seconds it should print `2 h 5 min 30 s`. Check against M01 Practice Set 2, problem 5.

### Review

1. What do `//` and `%` give for 100 and 7? (M03 connection.)
2. Why does `x = x + 1` make sense in Python?

---

## Session 2 — Text (strings) and input

### Learn

Text in Python is a **string**, written in quotes: `"hello"` or `'hello'`.

```python
name = "Noblett"
print(len(name))       # 7: number of characters
print(name[0])         # 'N': the first character (counting starts at 0!)
print(name[-1])        # 't': the last character
print(name[0:3])       # 'Nob': characters 0, 1, 2 (stops before 3)
print(name.upper())    # 'NOBLETT'
print(name.lower())    # 'noblett'
print("ob" in name)    # True
```

**Counting from 0:** the first character is at **index** 0. This is true in almost every programming language. (You'll see why in Module 07: the index is how far from the start you move.)

**f-strings** put values into text:

```python
bytes_used = 4096
print(f"The page is {bytes_used} bytes, which is {bytes_used // 1024} KiB.")
```

**Input from the user:**

```python
answer = input("What's your name? ")
print(f"Hello, {answer}!")
```

`input()` always gives a **string**. To get a number: `age = int(input("Age? "))`.

**Joining and repeating:** `"ab" + "cd"` is `"abcd"`; `"-" * 10` is `"----------"`.

### Try

1. `"computer"[3:6]`
2. `"computer"[::-1]` (look up what `[::-1]` does after predicting)
3. `int("42") + 1` vs `"42" + "1"`
4. `f"{7 / 3:.2f}"` (the `:.2f` means "2 decimal places")
5. `"Hello".find("l")`

### Build: `name_card.py`

Ask for a first name, last name, and a favourite number. Print:

```
+----------------------+
| Name:   ADA LOVELACE |
| Initials: A.L.       |
| Number in binary:    |
|   101010             |
+----------------------+
```

(Use `bin(n)[2:]` for binary for now; in Session 6 you'll write your own.) Make the box width fit the longest line (`len()` and `"-" * width`).

### Review

1. What's the index of the last character of a 10-character string?
2. What's the difference between `"5" + "5"` and `5 + 5`?
3. What does `17 % 5` give? (Session 1)

---

## Session 3 — Decisions

### Learn

A **boolean** is `True` or `False`. Comparisons give booleans:

```python
>>> 5 > 3
True
>>> 5 == 3          # == asks "equal?"  (= assigns)
False
>>> 5 != 3          # not equal
True
```

Combine them with `and`, `or`, `not`:

```python
age = 30
print(age >= 18 and age < 65)    # True
```

**if / elif / else** — do something only when a condition is true. The indented lines (4 spaces) belong to the `if`:

```python
temperature = 23
if temperature > 30:
    print("hot")
elif temperature > 15:
    print("mild")
else:
    print("cold")
```

Python checks the conditions **in order** and runs only the first block whose condition is true.

**Indentation is part of the language.** It shows which lines belong to which block. Use 4 spaces (your editor does this when you press Tab).

### Try

1. `not (3 > 2)`
2. `True and False or True` (and is done before or)
3. `10 % 2 == 0` (what does this test?)
4. What prints if `temperature = 30` in the example above? Why not "hot"?
5. `"a" < "b"`, `"B" < "a"` (strings compare by their character codes — Base Workshop Milestone 2!)

### Build: `password_check.py`

Ask for a password. Report whether it is **strong**: at least 12 characters, contains at least one digit, and isn't in a short list of terrible passwords (`"password123456"`, `"qwertyuiop12"`). Print one clear message per failed rule.

Hints: `any(c.isdigit() for c in pw)` checks for a digit (you'll understand this line fully after Session 5). `pw in ["...", "..."]` checks the list.

**[W]:** why print *every* failed rule rather than stopping at the first one? (Think about the person using it — E09 instructions.)

### Review

1. What's the difference between `=` and `==`?
2. In an `if/elif/else`, how many blocks can run?
3. What is `"Nob" + "lett"`? (Session 2)

---

## Session 4 — Loops

### Learn

**while** repeats as long as a condition is true:

```python
count = 3
while count > 0:
    print(count)
    count = count - 1
print("liftoff")
```

**for** repeats once for each item in a sequence. `range(n)` gives 0, 1, …, n − 1:

```python
for i in range(5):
    print(i, i * i)
```

`range(1, 11)` gives 1 to 10. `range(10, 0, -1)` counts down from 10 to 1.

**Looping over a string:**

```python
for letter in "hex":
    print(letter.upper())
```

**Building up a total** (a very common pattern):

```python
total = 0
for n in range(1, 101):
    total = total + n      # or: total += n
print(total)               # 5050 — Gauss! (M11)
```

`break` leaves a loop early. `continue` skips to the next repetition.

**Infinite loops:** a `while` whose condition never becomes false runs forever. Stop it with `Ctrl+C`.

### Try

1. What does `for i in range(2, 20, 3): print(i)` print?
2. Write a loop that prints the powers of 2 from 2⁰ to 2¹⁰.
3. Count how many numbers from 1 to 1,000 are divisible by 7.
4. What happens if you forget `count = count - 1` in the countdown?
5. Print the 7 times table as `7 x 1 = 7`, …, `7 x 12 = 84`.

### Build: `times_tables.py`

Print a full 12 × 12 multiplication grid with neat columns (use f-string widths: `f"{n:4}"` pads to 4 characters). Then add: ask the user for a number and quiz them with 10 random facts from its table (`import random`; `random.randint(1, 12)`), counting correct answers. (Use it for M03's facts practice!)

### Review

1. What numbers does `range(5)` produce? `range(1, 5)`?
2. What's the difference between `while` and `for`?
3. What does `x != 3` mean? (Session 3)

---

## Session 5 — Lists

### Learn

A **list** holds many values in order:

```python
scores = [72, 85, 90, 64]
print(scores[0])          # 72 (index 0 again)
print(len(scores))        # 4
scores.append(88)         # add to the end
print(scores)             # [72, 85, 90, 64, 88]
print(sum(scores), min(scores), max(scores))
print(sorted(scores))     # a new, sorted list
print(85 in scores)       # True
```

**Loop over a list:**

```python
for s in scores:
    if s >= 80:
        print(s, "is a B or better")
```

**Change an item:** `scores[1] = 87`. **Remove:** `scores.remove(64)` (by value) or `scores.pop()` (the last one).

**Lists of lists** (a grid):

```python
grid = [[1, 2, 3],
        [4, 5, 6]]
print(grid[1][2])         # 6: row 1, column 2
```

(Nib's memory will be one list of 256 numbers. Pagelet's page will be a list of lines.)

**List comprehensions** — a short way to build a list:

```python
squares = [n * n for n in range(10)]
evens = [n for n in range(20) if n % 2 == 0]
```

### Try

1. `[1, 2, 3] + [4]`
2. `[0] * 5`
3. `words = "the quick brown fox".split()` then `len(words)` and `words[-1]`
4. `" ".join(["a", "b", "c"])`
5. Make a list of the first 10 multiples of 9 with a comprehension. What do their digits add up to? (M04's divisibility test.)

### Build: `score_stats.py`

Let the user type scores one per line until they type `done`. Then print: how many, the average (1 decimal place), the highest, the lowest, the **median** (middle value of the sorted list; if the count is even, the average of the two middle ones), and a text histogram:

```
60-69 | ##
70-79 | #
80-89 | ###
90-99 | #
```

### Review

1. What's the index of the last item of a list with `n` items?
2. What does `sorted(x)` do that `x.sort()` doesn't? (Look it up after guessing.)
3. Write a loop that prints 10, 9, …, 1. (Session 4)

---

## Session 6 — Functions

### Learn

A **function** is a named, reusable piece of code. It takes **inputs** (parameters) and gives back an **output** (with `return`).

```python
def area_of_rectangle(width, height):
    """Return the area of a width-by-height rectangle."""
    return width * height

print(area_of_rectangle(3, 4))   # 12
```

- `def` defines it. The text in triple quotes is a **docstring**: a one-line description of what the function does.
- `return` sends the answer back. A function without `return` gives back `None`.
- **Names:** functions are verbs or verb phrases (E04 Part 3): `area_of_rectangle`, `count_words`, `to_binary`.

**Why functions?**
1. **Name an idea.** `is_prime(n)` reads like English.
2. **Write it once, use it many times.**
3. **Test it alone** (Lab 02).

**Variables inside a function are local:** they exist only while the function runs.

**Subgoal labels as comments** [S] — always start a function this way:

```python
def to_binary(n):
    """Return the binary digits of n (n >= 0) as a string."""
    # 1. Special case: 0 is "0"
    # 2. Repeatedly divide by 2; each remainder is the next digit from the right
    # 3. Stop when the quotient reaches 0
    # 4. Return the digits in the right order
```

### Try

1. Write `def double(x): return x * 2`, then `double(double(3))`.
2. What does a function return if it has no `return`? Test it.
3. Write `def is_even(n)` that returns `True` or `False`.
4. Write `def average(numbers)` for a list. What should it do for an empty list? (Decide [W].)
5. Call `area_of_rectangle(width=5, height=2)` with named arguments.

### Build: `conversions.py`

Write and use these functions (M01, M03):

```python
def to_binary(n): ...          # repeated division — no bin()!
def from_binary(digits): ...   # place values — no int(x, 2)!
def seconds_to_hms(total): ...  # returns a string "H:MM:SS"
```

At the bottom, print a table of 0–20 in decimal and binary using your functions, and check a few values against `bin()`.

### Review

1. What's the difference between `print` and `return`?
2. Why write subgoal comments before the code?
3. How do you get the last item of a list? (Session 5)

---

## Session 7 — Dictionaries

### Learn

A **dictionary** (`dict`) stores **key → value** pairs. Look things up by key, not by position.

```python
ages = {"Ada": 36, "Alan": 41}
print(ages["Ada"])           # 36
ages["Grace"] = 85           # add a new pair
ages["Ada"] = 37             # change a value
print("Alan" in ages)        # True (checks keys)
for name, age in ages.items():
    print(name, age)
```

**Counting with a dictionary** — one of the most useful patterns in programming:

```python
text = "the cat and the hat and the bat"
counts = {}
for word in text.split():
    counts[word] = counts.get(word, 0) + 1
print(counts)    # {'the': 3, 'cat': 1, 'and': 2, 'hat': 1, 'bat': 1}
```

`counts.get(word, 0)` means "the value for this word, or 0 if it's not there yet."

**Sorting by count:**

```python
for word, n in sorted(counts.items(), key=lambda pair: pair[1], reverse=True):
    print(word, n)
```

(`lambda pair: pair[1]` is a tiny unnamed function: "sort by the second item of each pair." Module 02 explains it properly.)

**When to use what:** a **list** when order matters and you look things up by position; a **dict** when you look things up by a name or key. (Module 05 explains *why* dict lookups are fast: hash tables.)

### Try

1. `d = {"a": 1}`; what happens with `d["b"]`? With `d.get("b")`?
2. Build a dict mapping `"A"`…`"F"` to 10…15 (for hex, M01).
3. `list(ages.keys())`, `list(ages.values())`
4. Count the letters (not words) in your name.
5. Make a dict of English words to their opposites; look one up.

### Build: `letter_stats.py`

Count every letter (ignore case and non-letters) in a paragraph you paste into the code as a string — use one of your copywork passages. Print the counts as a sorted histogram, most common first. Which letter is most common in English? Does your passage agree?

### Review

1. What's the difference between a list and a dict?
2. What does `counts.get(word, 0)` do?
3. Write a function that returns the largest number in a list without using `max`. (Session 6)

---

## Session 8 — Files

### Learn

**Read a whole file:**

```python
with open("notes.txt") as f:
    text = f.read()
```

`with` makes sure the file is closed afterwards, even if something goes wrong.

**Read line by line:**

```python
with open("notes.txt") as f:
    for line in f:
        line = line.strip()       # remove the newline and surrounding spaces
        if line:                  # skip empty lines
            print(line)
```

**Write a file** (`"w"` replaces the file; `"a"` appends to the end):

```python
with open("out.txt", "w") as f:
    f.write("first line\n")      # \n is a newline
    f.write("second line\n")
```

**Tab-separated files** (like your spelling log):

```python
with open("spelling-log.tsv") as f:
    header = f.readline().strip().split("\t")
    for line in f:
        fields = line.rstrip("\n").split("\t")
        row = dict(zip(header, fields))     # {"date": "...", "wrong": "...", ...}
        print(row["wrong"], "->", row["right"])
```

`zip` pairs up two lists item by item; `dict(zip(...))` turns the pairs into a dictionary.

**Binary files** (bytes, not text): `open(path, "rb")` — you'll use this in Base Workshop's `minihex.py` and in Nib.

**Paths:** a file name without a folder is looked for in the folder you ran Python *from*, not where the script lives. Use full paths or run from the right folder.

### Try

1. Write three lines to a file, then read them back and print them numbered.
2. What happens when you open a file that doesn't exist? Read the error message.
3. Append a line to an existing file. Check with `cat` in the terminal.
4. Count the lines in a file.
5. Read your spelling log and print how many entries it has.

### Build: `word_freq.py`

Read any text file (a journal entry, a copywork passage, a man page saved with `man ls > ls.txt`). Print:
- total words and unique words;
- the 15 most common words, with counts;
- the 15 most common words **of 6+ letters** (more interesting).

Run it on a section's worth of your journal entries. What do you write about most?

### Review

1. Why use `with open(...)`?
2. What's the difference between `"w"` and `"a"`?
3. Count how many times each word appears in a list. (Session 7)

---

## Session 9 — Modules and the command line

### Learn

**Modules** are Python files of useful code. Import them:

```python
import random
import time
import sys

print(random.randint(1, 100))   # a random whole number from 1 to 100
start = time.perf_counter()
# ... some work ...
print(time.perf_counter() - start, "seconds")
```

**Your own modules:** any `.py` file is a module. If `conversions.py` (Session 6) is in the same folder: `from conversions import to_binary`.

**Command-line arguments:** `sys.argv` is the list of words typed after `python3`:

```bash
python3 greet.py Ada 3
```

```python
import sys
name = sys.argv[1]           # "Ada"  (sys.argv[0] is "greet.py")
times = int(sys.argv[2])     # 3
for _ in range(times):
    print(f"Hi {name}")
```

**The main guard** — run code only when the file is run directly, not when imported:

```python
def main():
    ...

if __name__ == "__main__":
    main()
```

Every program from now on should use this shape. It lets tests import your functions without running the program.

### Try

1. `random.choice(["rock", "paper", "scissors"])`
2. `random.shuffle(my_list)` — what does it return? What happens to the list?
3. Time how long `sum(range(10_000_000))` takes.
4. Write a script that prints its arguments, one per line.
5. Import your `to_binary` into the REPL and use it.

### Build: `guess.py`

A number-guessing game: the computer picks a secret number from 1 to N (N from the command line, default 100). The player guesses; the program says "higher" or "lower." At the end, print the number of guesses and the best possible maximum, ⌈log₂ N⌉ (`math.ceil(math.log2(N))` — you'll understand this fully in M11; for N = 100 it's 7). Save each game's result to `guess_history.tsv` (date, N, guesses) and print the player's average.

### Review

1. What is `sys.argv[0]`?
2. Why use `if __name__ == "__main__":`?
3. How do you read a file line by line? (Session 8)

---

## Session 10 — Putting it together: a tiny adventure

### Learn

Nothing new — this session combines everything. A **text adventure** is a perfect small system: it has **state** (where you are, what you carry), **data** (the rooms), and a **loop** that reads commands and changes the state. That shape — state + data + a command loop — is the shape of Nib (the machine's state), Burrow Jr. (the shell's loop), and Pagelet (the current page).

### Build: `adventure.py`

**Data** — rooms in a dictionary:

```python
ROOMS = {
    "hall":    {"text": "A dusty hall. Doors lead north and east.",
                "exits": {"north": "library", "east": "kitchen"},
                "items": []},
    "library": {"text": "Shelves of old manuals. A door leads south.",
                "exits": {"south": "hall"},
                "items": ["manual"]},
    "kitchen": {"text": "A kitchen with a locked cupboard. A door leads west.",
                "exits": {"west": "hall"},
                "items": ["key"]},
}
```

**State:** `location = "hall"`, `inventory = []`.

**Commands:** `look`, `go <direction>`, `take <item>`, `inventory`, `quit`. Add one goal: the game is won when you carry both the key and the manual back to the hall.

**Subgoal labels [S]:**

```python
# 1. Show the current room
# 2. Read a command and split it into a verb and (maybe) a noun
# 3. Do what the verb says, changing the state if allowed
# 4. Explain clearly when something isn't allowed ("You can't go west.")
# 5. Check whether the player has won
# 6. Repeat until quit or won
```

**Extensions (pick one or two):** load the rooms from a text file instead of the code; add a `save` command that writes the state to a file and `load` to restore it; add a room that needs the key.

### Review and final recall [R]

On a blank page, without looking, write:
1. A function with a docstring and a return value.
2. A `for` loop over a list, and a `while` loop that counts down.
3. Counting words with a dictionary.
4. Reading a file line by line.
5. The main guard.

Check against this lab. Every miss becomes a flashcard.

---

## Done when

- [ ] All ten Build programs work and are committed to `~/workbench/01-python/`.
- [ ] Final recall done; misses on flashcards.
- [ ] You can explain, out loud, briefly [F]: what a variable is, what a function is, the difference between a list and a dictionary.

**Next:** [Lab 02 — Errors, Tests, and Debugging](lab-02-errors-tests-and-debugging.md). After that, the projects.
