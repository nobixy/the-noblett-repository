---
title: "Project: Ember Compiler"
module: "06-computer-architecture"
hours: 70
artifact: "ember: a small programming language with a lexer, parser, checker, tree-walking interpreter, and a compiler to Kestrel assembly; a differential tester; Game of Life written in Ember running on Kestrel"
deliverable: "EMBER.md language reference + design doc + differential-testing report + 5-minute 'whole stack' demo"
---

# Project: Ember Compiler

| | |
| :-- | :-- |
| **Module** | 06 Computer Architecture |
| **Time** | About 70 hours |
| **Prerequisites** | [Kestrel ISA](../kestrel-isa/spec.md) (emulator, assembler, library, calling convention); Module 02's parsers (Worldfile) and Module 03's [Truth Engine](../../../03-discrete-math/projects/truth-engine/spec.md); Module 05 (hash tables, trees) |
| **You build** | **Ember**, a small language with 16-bit integers, global arrays, functions, recursion, `if`/`while`, and direct memory access for devices. You write its lexer, parser, semantic checker, an **interpreter** (the reference meaning of every program), and a **compiler** that emits Kestrel assembly. A tester runs every program both ways and demands identical output. Finally you write Game of Life in Ember and run it on your CPU |
| **Deliverable** | Language reference, design doc, testing report, and the "whole stack" demo |

---

## Why this matters

You've written machine code by hand (Nib) and assembly (Kestrel). Every programmer since the 1950s has wanted something better: a language where you write `fib(n - 1) + fib(n - 2)` and a program figures out the registers, the stack, and the jumps. That program is a **compiler**, and building one — even a small one — is one of the great experiences in computer science. It ties together parsing (Module 02), trees and symbol tables (Module 05), and the machine (this module).

You'll also build an **interpreter** first. It defines what each program *means*, and becomes the oracle for testing the compiler: any program whose compiled output differs from the interpreter's has found a bug in one of them.

**Real-world analogs:** C compilers (gcc, clang), language interpreters (CPython), the tiny compilers used for embedded and teaching languages.

---

## The Ember language (starting point)

```
// life.em (excerpt)
var board[128];          // global array of 16-bit words
var next[128];

fn get(x, y) {
    let word = board[y * 4 + (x >> 4)];
    return (word >> (15 - (x & 15))) & 1;
}

fn count_neighbours(x, y) {
    let n = 0;
    let dy = -1;
    while dy <= 1 {
        let dx = -1;
        while dx <= 1 {
            if dx != 0 or dy != 0 {
                n = n + get((x + dx) & 63, (y + dy) & 31);
            }
            dx = dx + 1;
        }
        dy = dy + 1;
    }
    return n;
}

fn main() {
    puts("Life on Kestrel\n");
    // ...
}
```

**Core features (required):**
- **Type:** 16-bit signed integers only. Arithmetic wraps around (two's complement, M07) — exactly like the hardware.
- **Declarations:** `var name;` and `var name[size];` (globals); `let name = expr;` (locals, in function bodies).
- **Statements:** assignment (`x = e;`, `a[i] = e;`), `if … { } else { }`, `while … { }`, `return e;`, expression statements (calls), blocks.
- **Expressions**, with this precedence (lowest first): `or` · `and` · `not` · comparisons `== != < <= > >=` · `|` · `^` · `&` · `<< >>` · `+ -` · `* / %` · unary `-` and `~` · calls, indexing, brackets. `and`/`or` **short-circuit**. Comparisons give 1 or 0.
- **Functions:** `fn name(params) { … }` with up to 3 parameters (matching the calling convention's argument registers — or more via the stack, as a stretch), recursion, `return`.
- **Built-ins:** `putc(c)`, `puts("literal")`, `print(n)` (signed decimal), `getc()`, `peek(addr)`, `poke(addr, value)` (memory-mapped devices: the framebuffer, FB_FLUSH, the cycle counter).
- **Program entry:** `fn main()`.

Write the full grammar in `EMBER.md` before coding. You may change the syntax; the semantics above (16-bit wrap-around, short-circuit logic, 1/0 comparisons) are part of the spec because the interpreter and compiler must agree on them exactly.

---

## Milestones

### Milestone 1 — The language reference and the lexer

1. **`EMBER.md`** (E10 quality): the grammar (in the same style as Worldfile's and Truth Engine's), every operator with precedence and associativity, the exact semantics of division and modulo on negative numbers (**decide**: round toward zero like C, or toward minus infinity like Python? [W] — and make the interpreter and the runtime library agree), what happens on division by zero, whether `>>` is a logical or an arithmetic shift for negative numbers (your ALU only has a logical shift-by-one — what does an arithmetic shift cost?), scoping rules (can a `let` shadow a global? a parameter?), and example programs.
2. **Lexer:** tokens with line and column; integer literals (decimal, hex, char literals like `'A'`), identifiers, keywords, operators, string literals (only for `puts`), comments.

**Done when:** the reference is complete and the lexer tokenises all your example programs, with errors for bad characters and unterminated strings.

### Milestone 2 — Parser and AST

1. **AST** as dataclasses (`Binary(op, left, right)`, `Call(name, args)`, `While(cond, body)`, …), each node keeping its source position.
2. **Recursive-descent parser** for statements; **precedence climbing** (or one function per precedence level) for expressions.
3. **Pretty-printer** from AST back to source; **round-trip test**: `parse(pretty(parse(src)))` equals `parse(src)` for all test programs and for randomly generated expression trees (Truth Engine's technique).
4. **Error messages** with file:line:col, a caret, and what was expected. At least 10 tested errors.

**Done when:** round-trip and error tests pass.

### Milestone 3 — Checker and interpreter

1. **Semantic checker:** undefined variables and functions, wrong argument counts, `return` outside functions, assignment to an undeclared name, duplicate definitions, `main` missing. **Scopes** with a stack of symbol tables (your Vault Search `HashMap`, or `dict` here).
2. **Tree-walking interpreter:** `evaluate(expr, env)` and `execute(stmt, env)`, recursive. **Every arithmetic result is wrapped to 16-bit signed** (write `wrap16(x)` and use it everywhere — the single most important function for compiler agreement). `peek`/`poke` operate on a simulated 64K-word memory with the same memory map, so device programs can run in the interpreter too (the framebuffer can be drawn the same way as the emulator draws it).
3. **Test programs** (at least 25), each with expected output: arithmetic edge cases (32767 + 1, −32768 / −1 [W: what happens?], negative modulo), short-circuit evaluation (a function with a visible side effect on the right of `and`), recursion (fib, factorial, Ackermann with small inputs), arrays, nested loops, shadowing.

**Done when:** all programs give their expected output in the interpreter.

**Checkpoint:** [Milestone Checkpoint](<../../../04 - System/Milestone Checkpoint Template.md>). Feynman target: *how a tree-walking interpreter evaluates `fib(3)`* — draw the tree and the order of visits.

### Milestone 4 — Code generation: expressions and globals

Generate Kestrel assembly. Start with the simplest correct strategy: a **stack machine on top of registers**.

**Subgoal labels [S] for generating an expression:**
```
# gen(expr) leaves the value of expr in r1.
# Number:     LI r1, n
# Global var: LI r2, addr;  LD r1, r2, 0
# Binary a op b:
#   gen(a);  PUSH r1          (save left value)
#   gen(b);  MOV r2, r1       (right value into r2)
#   POP r1                    (left value back)
#   <op r1, r1, r2>           (ADD/SUB/AND/…; * / % via library calls)
# Comparison: CMP r1, r2; then branch to set r1 = 1 or 0 (signed conditions LT/GE!)
```

1. Globals and arrays in a data section (`.space`); array indexing with address arithmetic (base + index).
2. `if` and `while` with **generated labels** (unique names like `L17_else`).
3. `and`/`or` with short-circuit jumps.
4. Assemble with `kasm.py`, link in `lib.kasm` (your runtime: `mul`, `udiv`, signed division wrappers matching the Ember semantics, `print_dec`, `puts`).

**Done when:** programs using only `main`, globals, expressions, `if`, and `while` give identical output in the interpreter and on the emulator.

### Milestone 5 — Functions, locals, and recursion

Implement functions with **stack frames** following your Kestrel calling convention:

```
# Prologue:  PUSH r6 (link); PUSH r4 (old frame pointer); MOV r4, r7 (new frame pointer)
#            reserve space for locals: ADDI r7, r7, -(number of locals)
#            store arguments (r1–r3) into their local slots
# Locals:    at fixed offsets from r4 (e.g. r4 − 1, r4 − 2, …)
# Return:    result in r1; MOV r7, r4; POP r4; POP r6; RET
# Call:      evaluate arguments (saving each on the stack), pop them into r1–r3, CALL f
```

Draw a stack frame for `count_neighbours` before writing code [R]. Update `KESTREL.md`'s calling-convention section if the compiler forced a change — and say why.

**Done when:** recursion (fib, Ackermann) and nested calls match the interpreter.

### Milestone 6 — Differential testing, at scale

1. **`ember test`** runs every program in `tests/` through the interpreter and through compile → assemble → emulate, and compares outputs. Any difference is a bug in the interpreter, the compiler, the assembler, the library, or the emulator — and the test tells you which program finds it.
2. **Random program generator** (seeded): random expressions with random constants and variables, random `if`/`while` with bounded loops, small functions. Generate 5,000 programs; run both ways. (Avoid generating division by zero, or make its semantics defined and test it.)
3. When a random program finds a difference, **shrink it** (Edit Buffer's technique: remove statements while it still fails) and keep the minimal version as a regression test.

**Done when:** 5,000 random programs agree, and every bug found along the way has a minimal regression test.

**Checkpoint:** Milestone Checkpoint. Why-ladder target: *why is an interpreter a better oracle than hand-written expected outputs?* (And when is it worse?)

### Milestone 7 — Life on Kestrel, and optimisation

1. Write **Game of Life in Ember** using `peek`/`poke` on the framebuffer. Run it on the emulator (and, if your datapath supports the framebuffer, on the gates).
2. **Measure** cycles per generation with the cycle counter. Compare with your hand-written assembly version from Kestrel ISA Milestone 6.
3. **Optimise the compiler**, measuring each change:
   - **Constant folding:** compute `3 * 4` at compile time.
   - **Avoid push/pop** when the right operand is a constant or a variable (load it straight into r2).
   - **Peephole optimisation:** scan the generated assembly for wasteful patterns (`PUSH r1` immediately followed by `POP r1`) and remove them.
   - (Stretch) a simple **register allocator** for locals.
4. The differential tests must still pass after every optimisation.

**Done when:** Life runs, and a table shows cycles per generation for hand-written assembly and for each compiler version.

---

## Testing guidance

- **The interpreter is the oracle;** the 25+ hand-written programs check the interpreter itself.
- **Differential testing** of every program through two complete, independent paths.
- **Random generation plus shrinking** finds the bugs humans don't imagine.
- **Assembly inspection:** for small programs, read the generated assembly; it should look like what you'd write by hand, only clumsier.

## Common pitfalls

- **Forgetting `wrap16`** in one interpreter operation (comparison of large values, shift amounts…).
- **Signed vs unsigned branches** after `CMP`: Ember's `<` is signed (use LT/GE), but array bounds or addresses might want unsigned.
- **Division semantics** differing between interpreter and runtime library (negative numbers!). Write the rule in `EMBER.md` and test both.
- **Branch range:** generated code can get long; your assembler's range errors (Kestrel ISA Milestone 3) will catch far branches. Teach the code generator to emit long jumps when needed.
- **Clobbered registers across calls:** the caller must save anything it needs that a call may change (r1–r3, r5).

## Communication deliverable

1. **`EMBER.md`** — the language reference.
2. **Design doc** (v1 before Milestone 4, final after Milestone 7): code-generation strategy, stack frame layout (diagram), runtime library, optimisations considered and measured.
3. **Testing report** (1–2 pages): the oracle strategy, the random generator, bugs found (with the layer each was in), and the minimal regression tests.
4. **The whole-stack demo** (5 minutes — this doubles as the module's showcase): Ember source → compiler → assembly listing → emulator running Life → (if available) the same on your datapath.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | Grammar and precedence table from memory; a stack frame drawn from memory |
| **F** | Interpreter evaluating `fib(3)`; how a function call compiles |
| **W** | Division semantics; why an interpreter is a good oracle; each optimisation measured |
| **S** | Code-generation subgoals per construct |
| **I** | Language design, trees, and machine details interleaved |
| **D** | Compiler bugs hide in layers: shrink first, then stuck notes |
| **T** | Reference, design doc, report, demo |

## Stretch goals

- **More than 3 parameters** (passed on the stack).
- **Byte strings and `char` arrays** with packed storage.
- **A real register allocator** (linear scan) and a comparison with the stack-machine strategy.
- **Self-hosting dreams:** write an Ember interpreter *in Ember* for a tiny subset, running on Kestrel. (A classic rite of passage.)
- **Error recovery** in the parser: report several errors per run instead of stopping at the first.

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Language reference | Complete grammar and exact semantics, including edge cases | Mostly | Vague |
| Front end | Lexer, parser, round trips, 10+ tested errors, checker with scopes | Works | Fragile |
| Interpreter | 25+ programs; wrap16 everywhere; devices simulated | Works | Edge bugs |
| Code generation | Expressions, control flow, functions, recursion, short-circuit | Most | Partial |
| Differential testing | 5,000 random programs agree; shrinking; regressions | Hand programs only | Missing |
| Life and optimisation | Runs; measured table across compiler versions | Runs | Missing |
| Communication | Reference, doc, report, demo | Most | Few |

**Done when:** every area at least 2; Interpreter and Differential testing at 3.

## Connections

- **Back:** Worldfile (recursive descent, ASTs), Truth Engine (precedence, random trees, round trips), Module 05 (hash tables, trees, shrinking), Kestrel ISA (everything), M07 (wrap-around arithmetic), Module 03 (induction: proving a recursive evaluator terminates).
- **Forward:** Module 07 (you'll read the assembly that gcc produces for C, and now recognise its stack frames), Module 10 (your browser's parser), Module 11 (StratumQL: a query language with its own parser and executor).

> **Originality note:** the Ember language, its semantics, and this milestone plan (with the interpreter-as-oracle differential testing) were designed for this curriculum and target your own CPU.
