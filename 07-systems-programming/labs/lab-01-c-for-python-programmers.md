---
title: "Lab 01 — C for Python Programmers"
id: "MOD07-LAB01"
type: "lab"
module: "07-systems-programming"
phase: "C"
order: 1000
prerequisites: []
sessions: 8
---

# Lab 01 — C for Python Programmers

**Goal:** enough C to build an allocator, a shell, and an archiver — with a clear picture of what every line does to memory.

**Sessions:** eight. Each session: learn, type the examples (copywork for code), do the exercises, recall from a blank page [R], commit.

**Rule for the whole module:** compile with `-std=c17 -Wall -Wextra -Wpedantic -Werror -g`. A warning is a bug report from the compiler. Don't silence it; understand it.

---

## Session 1 — Compile, run, types

```c
// hello.c
#include <stdio.h>

int main(void) {
    printf("Hello from C\n");
    return 0;      // the exit status (Burrow Jr. read these!)
}
```

```bash
gcc -std=c17 -Wall -Wextra -Wpedantic -Werror -g hello.c -o hello
./hello; echo $?
```

**Differences from Python, all at once:**
- C is **compiled** to machine code before running (Lab 01 of Module 06 showed you what it becomes).
- Every variable has a **fixed type** and size: `int` (usually 32 bits), `char` (8 bits), `long` (64 bits on Linux), `double` (64-bit float), `unsigned` versions, and exact-width types from `<stdint.h>`: `int16_t`, `uint8_t`, `uint32_t`, `uint64_t` — **use these for file formats and bit manipulation.**
- Integers **overflow** like Kestrel: unsigned types wrap around (defined behaviour); **signed overflow is undefined behaviour** (the compiler may assume it never happens — Lab 02's UBSan catches it).
- Blocks use `{ }`; statements end with `;`; `if (x > 3) { … }` needs the brackets.
- `printf` formats: `%d` int, `%u` unsigned, `%ld` long, `%zu` size_t, `%x` hex, `%s` string, `%c` char, `%p` pointer, `%f` double.

**Exercises:** (1) print `sizeof` of every type above; (2) compute 2³¹ − 1 + 1 as `int32_t` and as `uint32_t` and explain both results (M07); (3) port your M03 `time_split` (seconds → h:m:s) to C.

---

## Session 2 — Functions, control flow, header files

```c
// mathx.h
#ifndef MATHX_H
#define MATHX_H
#include <stdint.h>
uint32_t gcd(uint32_t a, uint32_t b);
#endif
```

```c
// mathx.c
#include "mathx.h"
uint32_t gcd(uint32_t a, uint32_t b) {
    while (b != 0) {          // Invariant: gcd(a, b) is unchanged (Module 03 Lab 02)
        uint32_t t = a % b;
        a = b;
        b = t;
    }
    return a;
}
```

- **Declarations** (in `.h` headers) say a function exists and its types; **definitions** (in `.c` files) give the body. The `#ifndef` guard stops a header being included twice.
- Compile several files: `gcc … main.c mathx.c -o prog`.

**A Makefile** so you never type that again:

```make
CC = gcc
CFLAGS = -std=c17 -Wall -Wextra -Wpedantic -Werror -g
prog: main.o mathx.o
	$(CC) $(CFLAGS) $^ -o $@
%.o: %.c mathx.h
	$(CC) $(CFLAGS) -c $< -o $@
clean:
	rm -f *.o prog
```

(Recipe lines start with a **Tab**, not spaces.) `make` rebuilds only what changed.

**Exercises:** port `is_prime`, `gcd`, and `modpow` from Prime Factory / Toy Cipher to C with a header and a Makefile; write a `test_mathx.c` that `assert`s known values.

---

## Session 3 — Pointers

**A pointer is an address** — the number of a memory location (Nib's LOADX, Kestrel's LD with a register base). Everything else follows from that.

```c
int x = 42;
int *p = &x;        // p holds the address of x       (& = "address of")
printf("%d\n", *p); // 42: *p means "the int at address p" (* = "follow the pointer")
*p = 7;             // changes x
printf("%d %p\n", x, (void *)p);
```

**Draw it** [R]: a box for `x` at some address (say 0x7ffd1000) containing 42; a box for `p` containing 0x7ffd1000, with an arrow.

**Why pointers?** (1) To let a function change the caller's variables:

```c
void swap(int *a, int *b) { int t = *a; *a = *b; *b = t; }
swap(&x, &y);
```

(2) To refer to big data without copying it. (3) To build linked structures. (4) To manage memory yourself (Session 6).

**NULL** is the pointer to nothing. Following it crashes the program (**segmentation fault**). Always check pointers that might be NULL.

**Exercises:** (1) write `void divmod(int a, int b, int *q, int *r)`; (2) draw the memory for `int **pp = &p;` and explain `**pp`; (3) predict, then check: what does a function `void inc(int n) { n++; }` do to the caller's variable, and why?

---

## Session 4 — Arrays and pointer arithmetic

```c
int a[5] = {10, 20, 30, 40, 50};
int *p = a;            // an array name decays to a pointer to its first element
printf("%d\n", *(p + 2));   // 30: p + 2 means "2 ints further", i.e. 8 bytes further
printf("%d\n", p[2]);       // same thing: p[i] is *(p + i)
```

- **Pointer arithmetic** moves by **element size**, not bytes. (Module 06 Lab 01: the `[rdi+rax*4]` you saw.)
- **C does not check array bounds.** `a[5]` reads whatever is after the array — a **buffer overflow**, the source of decades of security bugs. AddressSanitizer (Lab 02) catches it.
- Arrays passed to functions arrive as pointers; pass the length too: `int sum(const int *a, size_t n)`. (`const` promises the function won't change the data.)

**Exercises:** (1) `sum` and `max` of an array; (2) reverse an array in place with two pointers; (3) binary search in C (port the Growth and Halving Lab version) — with the loop invariant as a comment.

---

## Session 5 — Strings

A C **string** is an array of `char` ending with a **0 byte** (`'\0'`) — exactly Nib's `.string` and Kestrel's: you've built this.

```c
char name[] = "Ada";        // 4 bytes: 'A' 'd' 'a' '\0'
size_t n = strlen(name);    // 3 — counts until the 0
```

- `<string.h>`: `strlen`, `strcmp` (returns 0 when equal!), `strncpy`/`snprintf` (bounded copying), `strchr`, `memcpy`, `memset`.
- **Never** use `gets` or unbounded `strcpy`/`sprintf` into fixed buffers. Use `fgets` and `snprintf` with sizes.
- Reading lines: `char buf[256]; while (fgets(buf, sizeof buf, stdin)) { … }` — and remember `fgets` keeps the `\n`.

**Exercises:** (1) write your own `my_strlen` and `my_strcmp` with pointers; (2) a word counter reading stdin (port Lab 01 Session 8 from Module 01); (3) split a line into words on spaces **in place** by writing `'\0'` over the spaces and keeping pointers to each word's start — exactly what Burrow's tokenizer will do.

---

## Session 6 — Dynamic memory

The **stack** holds local variables; they vanish when the function returns. For data that must outlive a function, or whose size is known only at run time, use the **heap**:

```c
#include <stdlib.h>
int *a = malloc(n * sizeof *a);   // ask for n ints; returns NULL on failure
if (a == NULL) { perror("malloc"); exit(1); }
/* … use a[0] … a[n-1] … */
free(a);                           // give it back — exactly once
a = NULL;                          // defensive: avoid using it after free
```

- `calloc` (zeroed), `realloc` (resize; may move the block — use the returned pointer).
- **The four classic heap bugs** (Lab 02 shows you how to catch each): **leak** (never freed), **use after free**, **double free**, **overflow** past the end.
- **Ownership:** for every `malloc`, decide which part of the program owns the memory and must free it. Write it in a comment.

**Exercises:** (1) port your Module 05 `DynArray` to C (`struct` in Session 7; for now, a pointer, a length, and a capacity) using `realloc` with doubling; (2) read an entire file of unknown size into memory with a growing buffer; (3) never-returning-NULL wrapper `xmalloc` that exits with a message on failure.

**[W]:** a returned pointer to a local variable (`int *f(void) { int x = 1; return &x; }`) compiles with a warning. Why is it a bug? Draw the stack before and after the return.

---

## Session 7 — Structs and linked structures

```c
typedef struct Node {
    int value;
    struct Node *next;
} Node;

Node *push_front(Node *head, int v) {
    Node *n = malloc(sizeof *n);
    if (!n) return NULL;
    n->value = v;          // n->x is (*n).x
    n->next = head;
    return n;
}
```

- **Padding:** the compiler may insert gaps between fields so each field is aligned. Print `sizeof` and `offsetof` for `struct { char c; int i; char d; }` and explain the size [W]. Reorder the fields to shrink it.
- **Freeing a list:** walk it, saving `next` *before* freeing each node (the classic bug: using `n->next` after `free(n)`).

**Exercises:** (1) port Module 05's linked list and `RingQueue` to C; (2) a hash map from strings to ints with separate chaining (Vault Search's design, in C) — with a `free_map` that releases everything (valgrind must report zero leaks).

---

## Session 8 — Bits, files, and putting it together

**Bit operations:** `&`, `|`, `^`, `~`, `<<`, `>>`. Use **unsigned** types for bit work (shifting signed negative numbers right is implementation-defined). Idioms: test bit k `(x >> k) & 1`; set `x |= 1u << k`; clear `x &= ~(1u << k)`; toggle `x ^= 1u << k`.

**Binary files with stdio:** `fopen(path, "rb")`, `fread`, `fwrite`, `fseek`, `fclose`. Byte order: write multi-byte integers **byte by byte** in a defined order (little-endian, like Tone Loom's WAV) so files are portable — never `fwrite` a whole struct to disk (padding and byte order would leak into your format). [W] Why?

**Capstone exercise:** port Tone Loom's `write_wav` to C: write a 1-second 440 Hz sine WAV with an explicit little-endian `put_u16`/`put_u32` helper. Compare its bytes with your Python version's using `cmp` and `minihex.py`.

---

## Done when

- [ ] Every session's exercises compile cleanly with `-Werror`, and the heap exercises are valgrind-clean (Lab 02).
- [ ] The C hash map passes a differential test against a simple Python reference (feed both the same operations; compare outputs).
- [ ] The WAV writer produces byte-identical output to your Python version.

## Retrieval and reflection

1. **[R] Blank sheet:** pointer syntax and meaning; arrays vs pointers; strings and the 0 byte; malloc/free rules and the four bugs; struct padding; bit idioms; why not `fwrite` a struct.
2. **[F] (spoken):** "What is a pointer?" — draw memory as you talk.
3. **Flashcards:** printf formats; string functions and their dangers; the four heap bugs.

**Next:** [Lab 02 — Debugging Tools](lab-02-debugging-tools.md).
