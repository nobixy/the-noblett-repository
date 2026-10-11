---
title: "Project: Base Workshop"
id: "FND-MA-PRJ-base-workshop"
type: "project"
module: "00-foundations"
track: "math"
phase: "A"
order: 190
prerequisites: [M01]
stages: "M01–M02, then after 01 Lab 01"
artifact: "A paper counting board and adding sheets; bases.py, odometer.py, and minihex.py"
deliverable: "5–8 sentence explanation + short recorded demo"
---

# Project: Base Workshop

| | |
| :-- | :-- |
| **You build** | A physical counting board for bases 2, 5, 10, 16; hand-decoded secret messages; then a base converter, an odometer simulator, and a tiny hex-dump tool that shows the real bytes inside any file on your computer |
| **Deliverable** | A short written explanation (5–8 sentences) and a short recorded demo |

---

## Why this matters

Every file on your computer — every photo, song, program, and this very document — is a long list of bytes, and every byte is a number from 0 to 255, usually shown in hex. By the end of this project you'll have built a tool that opens any file and shows you those bytes, and you'll be able to read them.

That's the doorway to everything in this curriculum's systems half: the CPU you design reads instructions as bytes (Module 06), the archive format you design is bytes on disk (Module 07), and network packets are bytes on a wire (Module 09). Learning to see bytes starts here.

**Real-world analogs:** `xxd` and `hexdump` (tools every systems programmer uses), the base-conversion features of every programmer's calculator, the odometer in every car.

---

## Milestones

### Milestone 1 — The counting board (M01, paper)

**Build:** on a large sheet of paper, draw four rows of columns, one row per base:

```
base 10:  [ 1000 ] [ 100 ] [ 10 ] [ 1 ]
base 5:   [  125 ] [  25 ] [  5 ] [ 1 ]
base 2:   [ 16 ] [ 8 ] [ 4 ] [ 2 ] [ 1 ]
base 16:  [ 4096 ] [ 256 ] [ 16 ] [ 1 ]
```

Get about 40 small counters (coins, beans, paper clips).

**Do:**
1. **Count from 0 to 40 in base 5** by placing counters in the ones column. Whenever a column reaches 5 counters, remove them and put 1 counter in the next column left (that's **carrying** — you're physically doing it). Write each number as you go.
2. **Do the same in base 2** from 0 to 32. (Columns hold at most 1 counter: the second one forces a carry.)
3. **Make a table** of 0–32 in bases 10, 2, 5, and 16 from what you counted. Check it against M01's binary/hex table.

**Done when:** your table is complete and correct, and you can say, without looking, what happens on the board when you add 1 to 1111₂.

**[W]:** Why does the base-2 row need more columns than the base-10 row to show the same number?

### Milestone 2 — Secret messages (M01, paper)

Computers store letters as numbers. The standard code for English letters is **ASCII**: for example, `A` = 65 = 0x41, `B` = 0x42, …, `Z` = 0x5A; `a` = 0x61, …, `z` = 0x7A; space = 0x20. On Linux, `man ascii` shows the full table. (If `man ascii` is missing, any "ASCII table" search works.)

**Do:**
1. **Decode by hand:** `4E 4F 42 4C 45 54 54` (hex bytes). Then: `01001000 01001001` (binary bytes).
2. **Encode your first name** in hex and in binary, by hand.
3. **Find the pattern:** what's the difference, in hex, between `A` and `a`? Between `B` and `b`? Write it in binary. Which single bit is different? (This is a real trick programmers use to change letter case.)
4. Write a 5-word message in hex for a friend (or future you) to decode.

**Done when:** both messages decoded, your name encoded both ways, and the case-bit pattern explained in one sentence.

<details>
<summary>Answers (step 1 and the pattern)</summary>

`4E 4F 42 4C 45 54 54` = **NOBLETT**. `01001000 01001001` = 0x48 0x49 = **HI**. Lowercase is uppercase + 0x20 = 32 = 00100000₂: exactly one bit (the one worth 32) differs.
</details>

### Milestone 3 — The paper adding machine (M02, paper)

**Do:**
1. **Odometer strips:** cut 4 paper strips, each with `0` and `1` written alternately along it, to make a 4-wheel binary odometer you can slide. Count from 0000 to 1111 and then once more. Record what happens on the last step.
2. **Adding sheets:** do 10 binary additions and 5 hex additions in columns, writing every carry above its column (M02 Part 6). Mix in some that overflow 8 bits (e.g. 11001000 + 01000000).
3. **Carry chains:** find, by experiment, the 4-bit addition that causes the **most** carries. How many is the maximum? Why?

**Done when:** all sums checked by converting to decimal, and you've written one sentence explaining what overflow is.

**Checkpoint:** [Milestone Checkpoint](<../../../../04 - System/Milestone Checkpoint Template.md>). Feynman target: explain why carrying works in any base, using your counting board.

### Milestone 4 — `bases.py` (after 01 Lab 01)

Write a Python module with two functions:

```python
def to_base(n: int, base: int) -> str:
    """Return the digits of n (n >= 0) in the given base (2 to 36), as a string.
    Digits beyond 9 use letters: 10 -> 'A', 11 -> 'B', ..., 35 -> 'Z'."""

def from_base(digits: str, base: int) -> int:
    """Return the value of a digit string in the given base. Accept upper- or lowercase letters.
    Raise ValueError if a digit is not valid for the base."""
```

**Rules:**
- `to_base` must use **repeated division** (M03 Part 7). `from_base` must use **place values** (M01). Don't use Python's built-in `int(s, base)`, `bin()`, `hex()`, or `format()` inside your functions. (You *will* use them in your tests, as a second witness.)
- `to_base(0, b)` returns `"0"`.
- Add a small command-line interface: `python3 bases.py 200 16` prints `C8`; `python3 bases.py --from C8 16` prints `200`.

**Subgoal labels [S]:** write the M01/M03 subgoal labels as comments first, then fill in the code under each.

**Tests** (`test_bases.py`):
- For every n from 0 to 10,000 and every base in 2, 5, 8, 10, 16, 36: `from_base(to_base(n, b), b) == n` (a **round-trip** test).
- `to_base(n, 2) == bin(n)[2:]` and `to_base(n, 16) == hex(n)[2:].upper()` for 0–10,000.
- `from_base("ff", 16) == 255`; `from_base("2", 2)` raises `ValueError`.

**Done when:** all tests pass and the command line works.

### Milestone 5 — `odometer.py` and `minihex.py`

**`odometer.py`:** simulate an odometer with a fixed number of digits in any base.
- `python3 odometer.py --base 2 --digits 4 --start 13 --steps 5` prints each reading (`1101`, `1110`, `1111`, `0000 OVERFLOW`, `0001`, `0010`).
- Store the reading as a **list of digits** and add 1 **with carrying, digit by digit** (don't convert to a number and back). This is a software version of the adder circuit you'll build in Module 04.

**`minihex.py`:** a tiny hex-dump tool.
- `python3 minihex.py somefile` prints the file's bytes, 16 per line: the **offset** (position in the file, in hex), the bytes in hex, and the printable ASCII characters (show `.` for non-printable bytes):

```
00000000  4e 4f 42 4c 45 54 54 0a                          |NOBLETT.|
```

- Use your own `to_base` for the hex (padded with zeros to two digits per byte, eight digits for the offset).
- Read the file in binary mode: `open(path, "rb").read()` gives you a `bytes` object; each element is an integer 0–255.

**Explore with it:** dump a `.txt` file, a `.png` image (look at the first 8 bytes: every PNG starts with the same "magic number"), and a program like `/bin/ls` (the first 4 bytes of every Linux program are `7f 45 4c 46`: what letters are bytes 2–4?). Compare your output to `xxd somefile | head`.

**Done when:** your output matches `xxd` (apart from spacing) for three different files, and you've written down what the magic numbers of PNG and Linux programs say in ASCII.

**Checkpoint:** Milestone Checkpoint. Why-ladder target: *why do programmers show bytes in hex rather than decimal or binary?* (Answer from M01: one hex digit = 4 bits, so every byte is exactly two hex digits.)

---

## Common pitfalls

- **Reading the remainders in the wrong order** in repeated division. The first remainder is the *rightmost* digit.
- **Forgetting zero.** `to_base(0, 2)` must return `"0"`, not `""`.
- **Letters beyond F.** Base 36 uses A–Z. Uppercase/lowercase both must work in `from_base`.
- **Text mode vs binary mode.** Opening a file with `"r"` instead of `"rb"` gives you characters, not bytes, and can crash on images.
- **Off-by-one in the odometer:** the carry must keep moving left as long as digits roll over (1111 → 0000 involves four carries).

## Communication deliverable

Sized for where you are in English (E02–E05):
1. **Explanation (5–8 sentences)** in `README.md`: what the tools do and how `to_base` works. Short, correct sentences; every term explained.
2. **short recorded demo:** show the counting board briefly, run `bases.py`, run `odometer.py` until it overflows, and dump a PNG with `minihex.py`. Say what the magic number spells.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Before Milestone 4, write both conversion procedures from memory |
| **F** | Milestone 3 checkpoint: why carrying works in any base |
| **W** | Why more binary columns; why hex for bytes |
| **S** | Subgoal comments before code |
| **I** | Adding sheets mix binary, hex, and overflow cases |
| **T** | The demo |

## Stretch goals

- **Fractions:** extend `to_base` to print fractional digits (e.g. 0.625 → `0.101` in base 2) and show why 0.1 never ends in binary (M06 Part 7).
- **Signed mode:** add `--signed` to `odometer.py` for base 2: show each reading as a two's-complement value too (after M07).
- **Colour picker:** a script that takes `#RRGGBB` and prints the red, green, and blue values, and the reverse.

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Paper work | Board, table, messages, adding sheets all correct | Minor errors | Incomplete |
| `bases.py` | All tests pass, no built-in conversions inside | Works, few tests | Fails tests |
| Odometer | Digit-by-digit carry, overflow shown | Works via int conversion | Missing |
| Minihex | Matches `xxd`, magic numbers explained | Works | Missing |
| Communication | Clear explanation and demo | One of them | Neither |

**Done when:** every area at least 2.

## Connections

- **Back:** M01 (place value, bases), M02 (carrying), M03 (repeated division).
- **Forward:** [01 Nib project](../../../../01-intro-cs-taste/projects/nib-machine/spec.md) (memory as bytes), Module 04 (adder circuits), Module 06 (machine code), Module 07 (binary file formats, where `minihex.py` becomes your go-to debugging tool).
