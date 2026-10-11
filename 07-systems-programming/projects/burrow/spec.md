---
title: "Project: Burrow"
id: "MOD07-PRJ-burrow"
type: "project"
module: "07-systems-programming"
phase: "C"
order: 1050
prerequisites: [MOD07-LAB03, MOD01-PRJ-shell-sketch]
artifact: "burrow: a Unix shell in C — tokenizer, parser to an AST, pipelines, redirections, && and ||, variables and quoting, job control with process groups and terminal handover, if/while scripting, a trace timeline, and a test harness that compares behaviour with dash"
deliverable: "Design doc + BURROW.md user manual + test report + short demo"
---

# Project: Burrow

| | |
| :-- | :-- |
| **Module** | 07 Systems Programming |
| **Prerequisites** | Labs 01–03 of this module; [Burrow Jr.](../../../01-intro-cs-taste/projects/shell-sketch/spec.md) (reread your code and notes) |
| **Platform** | Linux (or WSL2) |
| **You build** | A real shell in C. Commands, pipelines of any length, every common redirection, sequences with `;`, `&&`, `||`, variables and quoting, **job control** (Ctrl+Z, `jobs`, `fg`, `bg`, background `&`), a small scripting language (`if`, `while`, script files), a `--trace` timeline of every process event, and a test harness that checks your shell against `dash`, a standard shell |
| **Deliverable** | Design doc, user manual, test report, and demo |

---

## Why this matters

Burrow Jr. showed you `fork`, `exec`, and `wait`. A real shell adds the hard parts: a proper grammar, many processes at once, and **job control** — the cooperation between the shell, the kernel, and the terminal that lets you press Ctrl+Z to pause a program and `fg` to bring it back. Getting job control right requires understanding process groups, sessions, signals, and terminal ownership — operating-system concepts you'll implement yourself in Module 08.

It's also a real language implementation: tokenizer, parser, AST, interpreter (Ember again, for commands instead of arithmetic).

**Real-world analogs:** `bash`, `dash`, `zsh`, `fish`; init systems and process supervisors.

---

## The language (subset to support)

```
command  := word+ redirect*
pipeline := command ('|' command)*
and_or   := pipeline (('&&' | '||') pipeline)*
list     := and_or ((';' | '&' | newline) and_or)* [';' | '&']
redirect := '<' word | '>' word | '>>' word | '2>' word | '2>&1'
compound := 'if' list 'then' list ['else' list] 'fi'
          | 'while' list 'do' list 'done'
```

- **Words:** unquoted, `'single quoted'` (no expansion), `"double quoted"` (expands `$VAR` and `$?`), backslash escapes outside single quotes.
- **Variables:** `NAME=value` (shell variable), `export NAME[=value]` (to the environment), `$NAME`, `${NAME}`, `$?` (last status), `$$` (shell PID).
- **Built-ins:** `cd`, `exit`, `export`, `unset`, `jobs`, `fg [%n]`, `bg [%n]`, `history`, `source file`, `type name`.
- **Comments:** `#` to end of line.

Write the exact grammar in `BURROW.md` before coding. You may extend it; document every extension.

---

## Milestones

### Milestone 1 — Design doc, tokenizer, parser

1. **Design doc v1** (4–6 pages): architecture (read → tokenize → parse → expand → execute), the AST types, the job table, the signal-handling plan (which signals the shell ignores, which children restore), and the test strategy.
2. **Tokenizer** (quotes, escapes, operators `| || & && ; < > >> 2> 2>&1`, newlines, comments). Tokens keep their quoting information (needed later for expansion).
3. **Parser** → AST (`Command`, `Pipeline`, `AndOr`, `List`, `If`, `While`, `Redirect`), with precise syntax errors (`burrow: syntax error near unexpected token '|'`).
4. **AST printer** and parser tests (at least 30 cases including errors).

**Done when:** parser tests pass.

### Milestone 2 — Execution: commands, pipelines, redirections, lists

1. **Simple commands** with fork/exec/wait (Lab 03), exit statuses, 127 for not found, 126 for not executable.
2. **Built-ins** run in the shell process (Burrow Jr.'s `cd` why-ladder). Built-ins in a pipeline (`cd /tmp | cat`) run in a child — decide and document.
3. **Pipelines of any length:** create n − 1 pipes; each child dup2's its ends and **closes all pipe fds**; the parent closes all of them and waits for all children. The pipeline's status is the **last** command's status.
4. **Redirections** in the child before exec, in order (so `cmd > f 2>&1` and `cmd 2>&1 > f` differ, as in real shells — [W] why do they differ?).
5. **Lists:** `;`, `&&` (run the next only if the status was 0), `||`.

**Done when:** the harness (Milestone 6's runner can be started now) passes for all of these.

**Checkpoint:** [Milestone Checkpoint](<../../../04 - System/Milestone Checkpoint Template.md>). Retrieval target: write the system-call sequence for `a | b | c > out` from memory, including every `close`.

### Milestone 3 — Variables, quoting, and the environment

1. Expansion step between parsing and execution: `$NAME`, `${NAME}`, `$?`, `$$` inside unquoted and double-quoted words; nothing inside single quotes.
2. Shell variables vs exported environment variables; children receive the environment (`execve` with a built `envp`, or `setenv` + `execvp`).
3. **Word splitting:** unquoted `$X` containing spaces becomes several words; quoted `"$X"` stays one. (A famous source of shell bugs — [W] why does `rm $FILE` go wrong when `FILE="my notes.txt"`?)

**Done when:** expansion tests pass, including the word-splitting cases.

### Milestone 4 — Job control

This is the hardest milestone. Read the GNU C Library manual's chapter **"Job Control"** (especially "Implementing a Job Control Shell") as your reference for the exact system calls — then write your own implementation.

**Concepts:**
- A **process group** holds all processes of one job (one pipeline). The first child's PID becomes the group ID: call `setpgid(child, pgid)` in **both** the child and the parent (to avoid a race — [W] which race?).
- The terminal has one **foreground process group**: it receives Ctrl+C (`SIGINT`) and Ctrl+Z (`SIGTSTP`). The shell gives the terminal to a foreground job with `tcsetpgrp`, and takes it back when the job stops or ends.
- The shell itself **ignores** `SIGINT`, `SIGTSTP`, `SIGTTOU`, and `SIGTTIN` (so Ctrl+C never kills the shell); children **restore** the defaults before exec (Burrow Jr.'s lesson, with more signals).
- **Background jobs** (`&`) run in their own group without the terminal.
- **Reaping:** a `SIGCHLD` handler sets a flag; the main loop calls `waitpid(-1, &status, WNOHANG | WUNTRACED | WCONTINUED)` repeatedly to update the **job table** (Running / Stopped / Done) and prints `[1]+ Done  sleep 5` notices before the next prompt.
- `jobs`, `fg %n` (give it the terminal, send `SIGCONT` to the group, wait), `bg %n` (send `SIGCONT`, don't wait).

**Manual tests (record them in your test report):** `sleep 30` then Ctrl+Z, `jobs`, `bg`, `fg`, Ctrl+C; `sleep 5 &` then keep working until "Done" appears; `vim` (or `less`) started, stopped with Ctrl+Z, and resumed with `fg` — the screen must restore correctly; `cat | cat | cat` and Ctrl+C kills all three.

**Done when:** every manual test behaves like bash.

**Checkpoint:** Milestone Checkpoint. Feynman target: *what happens, step by step, between pressing Ctrl+Z and seeing `[1]+ Stopped`*.

### Milestone 5 — Scripting

1. `if … then … else … fi` and `while … do … done`: the condition is a command list; its exit status decides.
2. **Script files:** `burrow script.bsh`, and `source file`; `#!/path/to/burrow` shebang support (so `./script.bsh` works when executable).
3. Non-interactive mode: no prompt, no job control, exit on end of file; `exit n` sets the script's status.

**Done when:** a 50-line script of your own (e.g. a backup script that uses `if`, `while`, pipes, and redirections) runs correctly.

### Milestone 6 — Trace timeline and the test harness

1. **`--trace FILE`:** like Burrow Jr., log every fork, exec, setpgid, tcsetpgrp, signal sent, and wait result with millisecond timestamps. Use it to debug Milestone 4.
2. **Test harness:** test files with a script, expected stdout, expected stderr (or a pattern), and expected exit status. A runner executes each through Burrow (non-interactive) and reports differences.
3. **Differential testing against `dash`:** for every test script within your supported subset, run it in both Burrow and `dash` and compare outputs and statuses. (`dash` is a small POSIX shell, `sudo pacman -S dash`. Bash also works, but its extensions differ more.) At least **50** scripts, including tricky quoting, redirection order, `&&`/`||` chains, nested `if`/`while`, and variable expansion.

**Done when:** all 50 agree with dash, and the trace mode helped you fix at least one job-control bug (write it up).

---

## Testing guidance

- **Parser tests** (AST text), **harness tests** (behaviour), **differential tests** (vs dash), **manual job-control tests** (written procedures with expected behaviour — a usability test for a system, E09 style).
- **Run the harness under Valgrind** regularly: no leaks per command (a shell runs for hours; leaks add up).

## Common pitfalls

- **Unclosed pipe fds** → hangs (in the parent *and* in every child).
- **The setpgid race:** the child may exec before the parent sets its group, or vice versa — do it in both.
- **Forgetting `WUNTRACED`** → stopped jobs look like they never finish.
- **Calling non-async-signal-safe functions in handlers** (printf, malloc). Set flags only.
- **Terminal not returned to the shell** after a job stops → the shell itself gets stopped by `SIGTTOU`/`SIGTTIN`.
- **Expanding variables before parsing** (they must be expanded after, or `X="a | b"; echo $X` would create a pipe).

## Communication deliverable

1. **Design doc** v1 → v2.
2. **`BURROW.md` user manual:** everything a user needs — grammar, built-ins, job control, scripting, differences from dash (E09: a manual that passes a usability test with one person).
3. **Test report** (1–2 pages): the harness, the 50 differential scripts, manual job-control procedures and results, and one bug story told through trace output.
4. **Demo:** a pipeline with redirections, a stopped and resumed `vim`, background jobs finishing, and a script running.

## Study-method integration

| Protocol | Where |
| :-- | :-- |
| **R** | The pipeline system-call sequence; the job-control sequence |
| **F** | Ctrl+Z, step by step; word splitting |
| **W** | Redirection order; the setpgid race; expand-after-parse; `rm $FILE` |
| **S** | Subgoal comments for pipelines and job control |
| **D** | Job control is hard: trace mode first, then stuck notes, then a night's sleep |
| **T** | Design doc, manual, test report, demo |

## Stretch goals

- **Command substitution** `$(cmd)` (fork, capture output through a pipe).
- **Line editing and history** with a raw-mode terminal (or link GNU readline).
- **Globbing** `*.txt` with `glob(3)` or your own matcher.
- **Functions** `name() { … }` in the scripting language.

## Self-grading rubric

| Area | Excellent (3) | OK (2) | Not yet (1) |
| :-- | :-- | :-- | :-- |
| Parsing | Full grammar, quoting, 30+ tests, good errors | Most | Fragile |
| Execution | N-stage pipelines, all redirections, lists, statuses | Most | Hangs |
| Expansion | Variables, environment, word splitting correct | Partial | Wrong |
| Job control | All manual tests behave like bash | Background jobs only | Missing |
| Scripting | if/while/source/shebang; real script works | Partial | Missing |
| Testing | Harness + 50 dash-differential scripts + Valgrind | Harness only | Ad hoc |
| Communication | Doc, manual, report, demo | Most | Few |

**Done when:** every area at least 2; Job control and Testing at 3.

## Connections

- **Back:** Burrow Jr. (01), Worldfile/Ember (parsers and interpreters), Lab 03 (system calls, signals), Crosswalk (job states are an FSM).
- **Forward:** Module 08 (processes, scheduling, and signals from the kernel's side; your Seedling kernel's own tiny shell), Module 13 (the capstone runs on scripts you'll write in Burrow).

> **Originality note:** Burrow's scope, trace timeline, and differential-testing harness were designed for this curriculum; it isn't based on any course's shell lab or starter code. The glibc manual is cited as a reference for the job-control system calls, as any engineer would use it.
