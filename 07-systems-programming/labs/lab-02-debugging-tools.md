---
title: "Lab 02 — Debugging Tools"
id: "MOD07-LAB02"
type: "lab"
module: "07-systems-programming"
phase: "C"
order: 1010
prerequisites: [MOD07-LAB01]
---

# Lab 02 — Debugging Tools

**Goal:** catch C's silent bugs loudly: `gdb` for stepping and inspecting, Valgrind and AddressSanitizer for memory errors, UndefinedBehaviorSanitizer for undefined behaviour.

**Sessions:** three.

---

## Session 1 — gdb

Compile with `-g -O0` so the debugger can map machine code back to your lines.

| Command | Does |
| :-- | :-- |
| `gdb ./prog` then `run args…` | start |
| `break file.c:42` / `break func` | stop there |
| `next` / `step` | next line (over calls) / into calls |
| `finish` | run until the current function returns |
| `print expr` / `print *p` / `print a[0]@5` | show values (the last shows 5 array elements) |
| `display x` | show x after every step |
| `bt` | backtrace: the stack of calls |
| `frame 2` / `info locals` | move up the stack; see that frame's variables |
| `watch x` | stop when x changes — superb for "who changed this?" |
| `x/16xb p` | examine 16 bytes at p in hex (your `minihex`, inside gdb) |

**Exercise — the crash:** write a linked-list program that frees a node and then uses it (deliberately). Run it until it crashes (or misbehaves). Use `bt` to see where, `print` to see the bad pointer, and `watch` on a list field to catch the moment it's overwritten.

**Exercise — the infinite loop:** a binary search with the classic `lo = mid` bug (never moves when `hi = lo + 1`). Run it, press Ctrl+C in gdb, and use `print lo`, `print hi`, `print mid` to see why.

**Core dumps:** `ulimit -c unlimited` (and, on systemd systems, `coredumpctl`) let you open a crashed program's memory after the fact: `coredumpctl gdb`. Try it once.

---

## Session 2 — Memory error detectors

Create a file `bugs.c` with five deliberate bugs, each in its own function selected by a command-line argument:
1. a **leak** (malloc, never free);
2. **use after free**;
3. **double free**;
4. **heap overflow** (write one element past a malloc'd array);
5. **stack overflow** of an array (write past a local array);
6. (bonus) **uninitialised read** (use a malloc'd value before setting it).

### Valgrind

```bash
gcc -g -O0 bugs.c -o bugs
valgrind --leak-check=full ./bugs 1
```

Read each report **slowly, bottom-up like a Python traceback**: what kind of error, the address, where it happened, and (for heap errors) where the block was allocated and freed. Write one line per bug: what Valgrind said, in your own words.

### AddressSanitizer (ASan) and UBSan

```bash
gcc -g -O1 -fsanitize=address,undefined -fno-omit-frame-pointer bugs.c -o bugs_asan
./bugs_asan 4
```

ASan is compiled into the program; it's much faster than Valgrind (about 2× slowdown vs 20–50×) and catches **stack** overflows that Valgrind misses. Compare: which bugs does each tool catch? Make a table.

**UndefinedBehaviorSanitizer** catches signed overflow, invalid shifts, misaligned pointers, and more. Add a function computing `INT_MAX + 1` and `1 << 40` on an `int`, and see what UBSan reports.

**[W]:** why is undefined behaviour worse than a crash? (Hint: the optimiser may *assume* it never happens and delete your checks. Search "undefined behavior can result in time travel" — a famous blog post — after writing your own answer.)

---

## Session 3 — Habits

1. **Two builds for every project:** a debug build (`-g -O0`) and a sanitizer build (`-fsanitize=address,undefined`). Your test suite runs under the sanitizer build. Add both to every Makefile as targets (`make debug`, `make asan`).
2. **Valgrind in tests:** `valgrind --error-exitcode=1 --leak-check=full ./tests` fails the test run on any memory error.
3. **Assertions for invariants** (`#include <assert.h>`), enabled in debug builds.
4. **The debugging method from Module 01 Lab 02** still applies: reproduce, shrink, predict-then-look, explain, fix with a regression test, log it.

**Exercise:** take your Lab 01 hash map, add a subtle bug (forget to free the old bucket array on resize), and find it with each tool. Then fix it and add a test that runs under Valgrind.

---

## Done when

- [ ] gdb exercises done, including `watch` and a backtrace.
- [ ] The tool comparison table for all six bugs.
- [ ] Your Makefile template has `debug`, `asan`, and `test` targets, and tests fail on any Valgrind error.

## Retrieval and reflection

1. **[R]:** the ten gdb commands; what Valgrind, ASan, and UBSan each catch; why undefined behaviour is dangerous.
2. **[F] (spoken):** "How does a tool know I used memory after freeing it?" (Guess first; then look up "shadow memory" and "redzones.")
