---
title: "Lab 01 — Reading Real Machine Code"
id: "MOD06-LAB01"
type: "lab"
module: "06-computer-architecture"
phase: "C"
order: 910
prerequisites: []
---

# Lab 01 — Reading Real Machine Code

**Goal:** see what a real compiler produces for a real processor (x86-64, the one in most laptops — or ARM64 if that's your machine), and recognise the ideas you'll design into Kestrel: registers, loads and stores, compares and branches, calls, returns, and stack frames.

**Sessions:** two. You don't need to know C yet; the examples are small and explained.

---

## Session 1 — Compiler Explorer

**Compiler Explorer** (godbolt.org) shows source code on the left and the compiler's assembly on the right, colour-matched line by line. Choose **C** and the compiler **x86-64 gcc** (latest).

### Example 1 — arithmetic

```c
int add3(int a, int b, int c) {
    return a + b + c;
}
```

With `-O0` (no optimisation), you'll see the function store its arguments to the stack and load them back — clumsy. Switch to `-O2`: it becomes two or three instructions. Find:
- where the arguments arrive (**registers `edi`, `esi`, `edx`** — the System V calling convention used on Linux: the first six integer arguments go in `rdi, rsi, rdx, rcx, r8, r9`, and `eax`/`rax` holds the return value);
- the `ret` instruction (return to the caller — the return address was pushed on the stack by `call`).

**Compare with Kestrel [W]:** your baseline passes arguments in r1–r3 and returns in r1. x86-64 puts the return address on the stack automatically; your baseline uses a link register. What does each choice cost?

### Example 2 — a loop

```c
int sum(int *a, int n) {
    int s = 0;
    for (int i = 0; i < n; i++)
        s += a[i];
    return s;
}
```

At `-O1`, find: the loop's label, the compare (`cmp`), the conditional jump back (`jl`, `jne`, …), and the load from memory (`mov eax, DWORD PTR [rdi+rax*4]` — "4" because each `int` is 4 bytes: **byte addressing**, unlike your word-addressed Kestrel). At `-O3` the compiler may **vectorise** (use instructions that add several numbers at once). Note it, don't decode it.

### Example 3 — a recursive call

```c
int fib(int n) {
    if (n < 2) return n;
    return fib(n - 1) + fib(n - 2);
}
```

At `-O1`, find: the comparison and early return, the **`push`** instructions saving registers the function needs across calls (**callee-saved** registers like `rbx`, `rbp`), the two `call fib`, and the matching `pop`s before `ret`. Draw the stack for `fib(2)` calling `fib(1)` [R]. Compare with the `fib` you'll write by hand in Kestrel assembly.

### Questions to answer in writing [W]
1. Why does `-O0` code store everything to the stack? (Hint: debuggers and the meaning of "no optimisation".)
2. Why does the compiler use `lea` for some additions? (Look it up: it's an address-calculation instruction used as a cheap adder.)
3. Find one instruction you don't recognise in each example and look it up.

---

## Session 2 — On your own machine

### Compile and disassemble locally

```bash
cat > fib.c <<'EOF2'
int fib(int n) { return n < 2 ? n : fib(n - 1) + fib(n - 2); }
int main(void) { return fib(10); }
EOF2
gcc -O1 -c fib.c -o fib.o        # compile to an object file
objdump -d fib.o                  # disassemble: addresses, raw bytes, instructions
gcc -O1 fib.c -o fib && ./fib; echo $?    # exit status is fib(10) = 55
```

In the `objdump` output, notice **the raw bytes** next to each instruction. x86-64 instructions have **variable length** (1 to 15 bytes). Find the shortest and longest instructions in your output. [W] Kestrel uses fixed 16-bit instructions; what does each approach make easier or harder (for decoding hardware; for code size)?

### Look inside a real program

```bash
objdump -d /bin/true | head -60
```

Find `_start` or `main`-like code and a `syscall` instruction if present (how a program asks the kernel for something — Module 07 and 08).

### Step through it with gdb

```bash
gcc -O0 -g fib.c -o fib
gdb ./fib
(gdb) break fib
(gdb) run
(gdb) info registers rdi rsp rip
(gdb) stepi            # one machine instruction
(gdb) x/8gx $rsp       # show 8 stack words
(gdb) bt               # backtrace: the chain of calls on the stack
(gdb) continue
```

Watch `rsp` (the stack pointer) go down as calls nest and up as they return. `bt` shows the frames — Module 07 uses gdb constantly.

---

## Done when

- [ ] All three Compiler Explorer examples annotated (screenshot or copy with your comments on each line).
- [ ] `objdump` and `gdb` sessions done; stack drawn for nested `fib` calls.
- [ ] The written questions answered.

## Retrieval and reflection

1. **[R]:** the x86-64 argument and return registers; what `call` and `ret` do with the stack; what callee-saved means.
2. **[F] (spoken):** "What does a compiler turn a function call into?"
3. **[W]:** list three design decisions in x86-64 you'd copy for Kestrel, and three you wouldn't — with reasons. Use them in your ISA manual's rationale section.

**Next:** [Kestrel ISA](../projects/kestrel-isa/spec.md).
